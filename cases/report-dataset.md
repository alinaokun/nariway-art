# Report Dataset — coded, sourced case rows (master)

The accumulating report-grade dataset behind [[flagship-report]], coded to [[case-template]]. Every figure carries a source or an explicit `unknown`. Net-assets-to-opex ratios are **upper bounds** (net assets include real property), per [[claims-register]] C4. Flagship cases may also get a full standalone note (e.g. [[fisher-sfmoma]]).

**Systematic-unknown finding (process):** `true_endowment_usd` (990 Schedule D Part V) and `fte_headcount` (990 Part I line 5) cannot be pulled from ProPublica's JS-rendered view; they need the downloadable 990 **PDF/XML** (IRS bulk XML is the scalable fix). Expect these `unknown` across many US cases until a PDF/XML pass is run. This itself feeds the report's data-availability chart.

Pilot batch 1 (2026-08), 6 cases across the outcome spectrum. Failure batch (Terra, Corcoran, di Rosa) pending.

---

### 1. Souls Grown Deep Foundation — Atlanta, GA · Spot-verified
pathway **intentional-dispersal** (+univ-partnership branch) · founder **William Arnett** living-at-transition (d. 2020-08-12) · **survived_founder yes** · outcome **stable** · durability **moderate** (depletion by design — endowment lens N/A) · governance family→foundation-exec · **no-building** · coherence **tight-single-thesis** · decision **foundation-executive** · constraints **partial** (gift-purchase terms).
Numbers: **500+ works by 110 artists → 20+ museums** since 2016 [SGD]; anchors Met 57 (2014), FAMSF 62 (2017), High 54. Net assets **$3,175,646**, expenses **$1,065,457** (FY2025 Form 990, declining by design) [ProPublica 27-2457990]. Founding size contested 1,200 vs 1,300. true_endowment/FTE **unknown**.
Sources: propublica.org/nonprofits/organizations/272457990 · soulsgrowndeep.org/resale-royalty-award-program · metmuseum.org/press-releases/souls-grown-deep-2014-news

### 2. Fisher Collection at SFMOMA — San Francisco, CA · Spot-verified · full note [[fisher-sfmoma]]
pathway **long-term-loan** · founders Donald (d.2009) & Doris (d.2026-05-02) Fisher · **survived_founder yes** · outcome **thriving** · durability **strong** · governance **mixed** (family owns, museum displays) · **existing-institution** · coherence coherent-multi · decision collector-alone · friction **community-opposition** (abandoned Presidio museum) · constraints partial.
Numbers: **100-year term** (from 25, renewable in 25s), **720+ works / 100 artists on loan** [SFMOMA, primary]. Total collection ~1,100 (secondary). care-endowment **unknown**.
Sources: sfmoma.org press release (reinstallation) · gapinc.com Doris Fisher obituary

### 3. Neue Galerie → The Met — New York, NY · Spot-verified
pathway **merger-into-institution** (+13-work gift branch) · founder **Ronald Lauder** living · **survived_founder not-yet-testable** (merger effective 2028) · outcome **merged** (pending) · durability **strong** · governance founder-sole→parent-institution · **adapted-residence** (Wm. Starr Miller House) · coherence **tight-single-thesis** (German/Austrian modern) · decision collector-alone · constraints partial.
Numbers: announced **2026-05-14**, effective **2028**; new name "The Met Ronald S. Lauder Neue Galerie"; collection/building/Café Sabarsky stay; Neue Galerie endowment transfers to Met + Lauders fund a dedicated care endowment; **13 works** donated. **All dollar figures undisclosed → unknown.**
Sources: theartnewspaper.com/2026/05/14/neue-galerie-metropolitan-museum-merger · metmuseum.org/press-releases/neue-galerie-merger-announcement (re-fetch; was 429)

### 4. The Phillips Collection — Washington, DC · Spot-verified
pathway **found-standalone-museum** (originated in family residence; flag) · founder **Duncan Phillips** living (d.1966) · **survived_founder yes** (Marjorie→Laughlin Phillips) · outcome **thriving** · durability **strong** · governance family-controlled · **adapted-residence** · coherence coherent-multi · decision collector-alone · constraints no (bylaws unread).
Numbers: opened **1921** (first US museum of modern art), **237 works** at opening → ~6,000. Net assets **$125,438,989**, expenses **$17,368,949** → **7.2x [UPPER BOUND]**; earned rev **$1,472,937**; attendance 135,301 (FY25) [ProPublica 53-0204620]. true_endowment/FTE **unknown**.
Sources: phillipscollection.org/about/history · propublica.org/nonprofits/organizations/530204620

### 5. The Menil Collection — Houston, TX · Spot-verified
pathway **found-standalone-museum** (+foundation branch; multi-building campus) · founders John (d.1973) & Dominique (d.1997) de Menil · **survived_founder yes** · outcome **thriving** · durability **strong** · governance family-controlled · **purpose-built** (Piano, 1987) · coherence coherent-multi · decision collector-alone (Dominique executed) · constraints partial (free admission principle).
Numbers: opened **1987**; net assets **$525,467,914**, expenses **$31,282,405** → **16.8x [UPPER BOUND]**; earned rev **$3,044,838** (admission free) [ProPublica 74-6045327]. Collection size contested 25,000+ vs ~16,000. true_endowment/FTE **unknown**.
Sources: menil.org/about · menil.org/founders · propublica.org/nonprofits/organizations/746045327

### 6. Shelburne Museum — Shelburne, VT · Spot-verified
pathway **found-standalone-museum** (open-air "collection of collections") · founder **Electra Havemeyer Webb** living (d.1960) · **survived_founder yes** · outcome **thriving** · durability **strong** · governance family-controlled · **adapted-other** (39 structures, ~25 relocated historic buildings incl. steamboat *Ticonderoga*) · coherence **broad-survey** · decision collector-alone · constraints no.
Numbers: founded **1947**; net assets **$60,247,427**, expenses **$9,678,671** → **6.2x [UPPER BOUND]**; earned rev **$1,675,064** (FY2025) [ProPublica 03-0179436]. Collection size 100,000+ (official) vs 150,000 (press). attendance/true_endowment/FTE **unknown**.
Sources: shelburnemuseum.org/about · propublica.org/nonprofits/organizations/30179436

---

### Early cross-case signal (pilot, not yet conclusive)
Of the 5 deceased-founder cases here, **all 5 survived the founder** (SGD, Fisher, Phillips, Menil, Shelburne); Neue Galerie is not-yet-testable. Pathways already span standalone-museum, house-origin, loan, dispersal, and merger. This is a small, favorable-by-selection slice, the failure cases (Terra, Corcoran, di Rosa) will balance it. Do not read a survival rate off six hand-picked cases; the point of the pilot is that the template codes cleanly and every cell is sourced or honestly `unknown`.
