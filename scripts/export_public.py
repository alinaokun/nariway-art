#!/usr/bin/env python3
"""Export the PUBLIC projection of the case corpus to export/nariway-public.json.

Contract (see marketing/collection-index-build-brief.md §9):
- A case exports only if `public_page_eligible: true` AND `public_verified: true`.
- Only PUBLIC fields (the flat `public_*` frontmatter, per cases/case-template.md) are emitted.
- Internal fields (outcome_category, verification, decision_owner, *_confidence, sourcing notes,
  the whole research body) are NEVER read into the export.
- Dependency-free: no PyYAML. Flat `key: value` frontmatter only; lists split on '; '.

Run:  python scripts/export_public.py            (from the vault root)
      python scripts/export_public.py 2026-08-22 (override the stamp date)
"""
import glob, json, os, re, sys

# Fields that are, by policy, NEVER emitted even if present in frontmatter:
NEVER_EXPORT = {
    "outcome", "outcome_category", "durability_signal", "verification", "decision_owner",
    "status", "priority", "founder_status", "hypotheses", "interview_status",
}

def parse_frontmatter(text):
    m = re.match(r"^---\s*\n(.*?)\n---\s*\n", text, re.S)
    if not m:
        return {}
    fm = {}
    for line in m.group(1).splitlines():
        if not line.strip() or line.lstrip().startswith("#"):
            continue
        if ": " in line:
            k, v = line.split(": ", 1)
        elif line.rstrip().endswith(":"):
            k, v = line.rstrip()[:-1], ""
        else:
            continue
        k = k.strip()
        v = v.strip().strip('"').strip("'")
        fm[k] = v
    return fm

def as_list(v):
    return [x.strip() for x in v.split(";")] if v else []
    # note: values use "; " as the delimiter; split on ";" then strip handles both "; " and ";"

def truthy(v):
    return str(v).strip().lower() == "true"

def parse_timeline(v):
    events = []
    if not v:
        return events
    for chunk in v.split(" ;; "):
        parts = chunk.split("|")
        parts += [""] * (4 - len(parts))
        year, family, coded, event = parts[0].strip(), parts[1].strip(), parts[2].strip(), parts[3].strip()
        ev = {"event": event}
        ev["year"] = int(year) if year.isdigit() else year
        if family:
            ev["familyId"] = family
        if coded:
            ev["codedPathway"] = coded
        events.append(ev)
    return events

def project(path):
    fm = parse_frontmatter(open(path, encoding="utf-8").read())
    if not (truthy(fm.get("public_page_eligible")) and truthy(fm.get("public_verified"))):
        return None
    slug = os.path.basename(path)[:-3]
    profile = {}
    for src, dst in [("public_founded", "founded"), ("public_collecting_began", "collectingBegan"),
                     ("public_structure", "structure"), ("public_access", "publicAccess"),
                     ("public_status_text", "currentState"), ("public_size", "size")]:
        if fm.get(src):
            val = fm[src]
            profile[dst] = int(val) if src == "public_founded" and val.isdigit() else val
    composition = {}
    for src, dst, is_list in [("public_focus", "focus", False), ("public_movements", "movements", True),
                              ("public_period", "period", False), ("public_media", "media", True),
                              ("public_selected_artists", "selectedArtists", True),
                              ("public_recipients", "recipients", True)]:
        if fm.get(src):
            composition[dst] = as_list(fm[src]) if is_list else fm[src]
    rec = {"slug": slug, "publicDepth": fm.get("public_depth", "record")}
    if fm.get("public_name"): rec["name"] = fm["public_name"]
    if fm.get("public_founder"): rec["founder"] = fm["public_founder"]
    if fm.get("public_location"): rec["location"] = fm["public_location"]
    if profile: rec["profile"] = profile
    if composition: rec["composition"] = composition
    tl = parse_timeline(fm.get("public_pathway_timeline", ""))
    if tl: rec["classification"] = {"pathwayTimeline": tl}
    if fm.get("public_origin"): rec["origin"] = fm["public_origin"]
    rec["image"] = {"status": fm.get("hero_image_status", "no_usable_image")}
    if fm.get("public_sources"): rec["sources"] = as_list(fm["public_sources"])
    if fm.get("last_reviewed"): rec["lastReviewed"] = fm["last_reviewed"]
    if truthy(fm.get("living_collector")): rec["livingCollector"] = True
    return rec

TAXONOMY = {
    "pathwayFamilies": [
        {"id": "build-institution", "label": "Build an institution", "hasPublicPage": True},
        {"id": "partner-institution", "label": "Partner with an institution", "hasPublicPage": True},
        {"id": "give-institution", "label": "Give to an institution", "hasPublicPage": False},
        {"id": "disperse", "label": "Disperse deliberately", "hasPublicPage": False},
        {"id": "sell", "label": "Sell", "hasPublicPage": False},
        {"id": "keep-family", "label": "Keep it in the family", "hasPublicPage": False},
    ],
    "partnerAxes": {
        "ownership": ["gift", "long-term-loan", "partial", "co-ownership", "staged", "contested"],
        "partner": ["museum", "university", "foundation", "archive-library", "network", "government"],
        "publicModel": ["dedicated-galleries", "integrated", "rotating", "lending-program"],
    },
}

def main():
    today = sys.argv[1] if len(sys.argv) > 1 else __import__("datetime").date.today().isoformat()
    collections = sorted((c for c in (project(p) for p in glob.glob("cases/*.md")) if c),
                         key=lambda c: c.get("name", c["slug"]))
    out = {
        "generated": today,
        "taxonomy": TAXONOMY,
        "collections": collections,
        "decisions": [],      # authored separately; added in a later export iteration
        "topics": [],         # authored separately; added in a later export iteration
        "conversations": [],  # authored separately; added in a later export iteration
    }
    os.makedirs("export", exist_ok=True)
    with open("export/nariway-public.json", "w", encoding="utf-8") as f:
        json.dump(out, f, ensure_ascii=False, indent=2)
    print(f"exported {len(collections)} public collections -> export/nariway-public.json")
    for c in collections:
        print(f"  - {c.get('name', c['slug'])} ({c['publicDepth']})")

if __name__ == "__main__":
    main()
