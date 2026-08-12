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

### 7. Terra Museum of American Art — Chicago, IL · Spot-verified
pathway **found-standalone-museum** (→foundation + AIC long-term loan) · founder **Daniel Terra** living (d.1996) · **survived_founder NO** (operated 8 yrs after death but on continuous governance litigation, no succession, did not continue in founded form) · outcome **closed-dispersed** (2004) · durability **failed** · governance **founder-sole** (Terra + son the only original directors) · coherence tight-single-thesis (American art to 1945) · decision **foundation-executive** (widow Judith Terra the contested driver) · **friction governance-conflict** (+succession-failure, legal-challenge) · constraints partial (donor-intent litigated by IL AG).
Numbers: museum closed **2004** after board/widow litigation; the *successor grantmaking foundation* holds **$614.5M** net assets (FY2025) — **NOT museum durability**; founder gave ~$450M lifetime [ProPublica 36-2999442, primary; IL appellate opinion, primary]. **Flag: a "50-year stay-in-Illinois" settlement term is reported by Wikipedia but ABSENT from the appellate opinion — unresolved.** Museum-era financials/attendance **unknown**.
Sources: illinoiscourts.gov opinion 1013152 · fnewsmagazine.com/2004-nov · propublica.org/nonprofits/organizations/362999442

### 8. Corcoran Gallery of Art — Washington, DC · Spot-verified
pathway **donate-existing-museum-scattered** (+merger of school/building into GWU) · founder **W.W. Corcoran** (d.1888) · **survived_founder YES** (ran ~126 yrs, then dissolved) · outcome **dissolved** (2014 cy pres) · durability **failed** · governance **independent-board** · **purpose-built** (Flagg Bldg 1897) · coherence broad-survey · decision foundation-executive (Judge Robert Okun approved) · **friction funding-gap** (+legal-challenge "Save the Corcoran") · **constraints yes** (1869 deed of trust, broken by cy pres).
Numbers: dissolved **Aug 2014**; **19,493 objects distributed** (8,300+ to NGA as "The Corcoran Collection at the NGA," ~10,862 to 22 DC-area institutions) [Art Newspaper]. Endowment fell **$23.2M (2009)→$14.1M (2013)** ≈ 0.45x coverage — the real signal; net assets **$76.8M** / expenses **$28.6M** FY2014 [ProPublica 53-0196641] but **rising book net assets were restricted acquisition funds during failure, NOT health** (C4). $33.8M Clark carpet sale (2013) was restricted to acquisitions.
Sources: corcoran.gwu.edu/history · news.artnet.com judge-approves-dissolution · nga.gov/artworks/corcoran-collection · propublica 530196641

### 9. di Rosa Center for Contemporary Art — Napa, CA · Spot-verified
pathway **found-art-park** (+foundation) · founder **Rene di Rosa** living (d.2010) · **survived_founder YES** (16 yrs, still operating but distressed) · outcome **distressed** · durability **weak** · governance independent-board (founder-as-chair) · **adapted-residence** · coherence tight-single-thesis (NorCal contemporary) · decision foundation-executive · **friction funding-gap** · constraints partial (land protected in perpetuity by Land Trust of Napa County; collection was not).
Numbers: **CORRECTION — the 2019 deaccession was announced then HALTED in 2020; $0 raised, no works ever sold** (the "Bechtle sale" premise is false; that painting is at the Whitney) [Art Newspaper]. Operating entity net assets **−$2.49M (FY2024)** [ProPublica 94-3367956]; asset-holding foundation $8.86M [94-2856000]. **217-acre campus listed $10.9M, Jan 2026** (collection excluded) [Press Democrat]. Collection size contested 1,600 vs 2,200. Founder-estimated ~$4M endowment (2011).
Sources: theartnewspaper.com 2026/01/22 di-rosa · propublica 943367956 & 942856000 · pressdemocrat.com 2026/01/21

---

## Preliminary patterns (~30 cases coded, PROVISIONAL)
From the first 30 coded cases. **Not conclusions.** The set is hand-selected for variation, not random, so no rates are published off it; these are hypotheses sharpened enough to test across all 50. Data gaps are named, not hidden.

1. **Governance, not money, decides whether a collection survives its founder.** Among the deceased-founder cases, survival is the norm, and the failures locate the cause. Terra had roughly $450M behind it and still failed, its governance was **founder-sole** (the only original directors were the founder and his son), so his death was a control vacuum that became litigation and closure. The survivors consistently had **independent boards and succession set before death**: McNay's self-perpetuating board, Grounds For Sculpture's board that predated the founder's death by 20 years, the de Menils, Phillipses, and Havemeyer Webbs all handing to professional successors. Emerging read: **governance design at founding predicts survival better than endowment size.** Test at 50.

2. **Two failure modes, on two clocks.** Governance failure kills fast (Terra, on the founder's death). Funding failure kills slow (Corcoran dissolved after 126 years as its endowment eroded below ~0.5x operating coverage; di Rosa distressed and now selling its campus). Institutional mortality is two curves, not one.

3. **The eponymous museum is losing share to lighter models, especially among living founders.** The set spans nine pathways, and the newer/living-founder cases cluster on the alternatives: the Broad's lending library, the Cisneros and Daskalopoulos gift-and-co-ownership dispersals, the Fisher 100-year loan, the Neue Galerie merger, the traveling Kinsey. Consistent with the wealth-transfer thesis, the generation now deciding reaches for models that avoid a standalone institution's cost and fragility. Real shift or selection artifact is a 50-case question.

4. **A data-availability finding the report can own.** The durability metric everyone wants, endowment coverage, is largely **unmeasurable from public data**: the true endowment (IRS Schedule D) is `unknown` for most cases, the headline net-assets ratios are all upper bounds inflated by real property, and they are meaningless for grantmaking/lending vehicles (Broad ~109x, Longleaf ~111x are non-signals). How rarely a collection's durability can be verified from the outside is itself a finding, and a reason collectors cannot benchmark themselves.

5. **The living-founder cohort is the report's forward-looking core.** A large share (Glenstone, Crystal Bridges, Magazzino, Bechtler, Audain, Thoma) code as survival **not-yet-testable**, these are exactly the significant collections about to enter the transition the report is about. Analyze survival on the deceased-founder set; frame the living-founder set as the coming decisions, tying the historical data straight to the wealth-transfer moment.

---

### First real signal (pilot complete, 9 cases + McNay)
The **survived_founder field is doing exactly the work the report needs**, it separates failure modes that a crude "closed = failed" would flatten:
- **Terra** = did **not** survive the founder (governance vacuum on his death → litigation → closure). Friction: governance.
- **Corcoran** = survived 126 years, then **dissolved on money** (endowment coverage fell below ~0.5x). Friction: funding.
- **di Rosa** = survived, still open, but **distressed and drifting** from founding intent (campus for sale). Friction: funding.
- The 5 thriving/stable survivors (SGD, Fisher, Phillips, Menil, Shelburne) all cleared succession.
Emerging hypothesis to test at scale: **governance design at founding (independent board + succession plan) predicts survival better than collection value or endowment size** — Terra had ~$450M behind it and still failed on governance; the durable ones had board continuity locked before the founder's death. This is H8-adjacent and must be tested across all 50, not asserted from ten. **Do not publish any rate off ten hand-picked cases;** the pilot proves the template codes cleanly, every cell is sourced or honestly `unknown`, and the agents catch false premises (di Rosa).
