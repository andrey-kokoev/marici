# Yang–Mills downloads and indexed search

## Downloaded PDFs

All files below were checked for a PDF header before saving. arXiv URLs retrieve the available version, not a pinned historical version.

- `yang-mills-jaffe-witten.pdf`: https://www.claymath.org/wp-content/uploads/2022/06/yangmills.pdf
- `yang-mills-chevyrev-review-2202.13359.pdf`: https://arxiv.org/pdf/2202.13359
- `yang-mills-higgs-3d-2201.03487.pdf`: https://arxiv.org/pdf/2201.03487
- `yang-mills-renormalisation-2503.03060.pdf`: https://arxiv.org/pdf/2503.03060
- `yang-mills-torus-1808.09196.pdf`: https://arxiv.org/pdf/1808.09196
- `yang-mills-invariant-measure-2302.12160.pdf`: https://arxiv.org/pdf/2302.12160 (downloaded text dated April 7, 2026).

## Not obtained

Do not treat these as locally read primary papers:

- Magnen–Rivasseau–Sénéor (1993), DOI 10.1007/BF02097397: Springer PDF URL and Project Euclid returned non-PDF responses.
- Balaban (1987), DOI 10.1007/BF01215223: Springer PDF URL returned a non-PDF response. An additional repository lead, not downloaded: https://scholarship.libraries.rutgers.edu/esploro/outputs/journalArticle/Renormalization-group-approach-to-lattice-gauge/991031665200104646
- Osterwalder–Schrader I/II: Project Euclid download routes for euclid.cmp/1103858969 and euclid.cmp/1103899050 returned non-PDF responses. DOIs 10.1007/BF01645738 and 10.1007/BF01608978.

No HTML challenge pages were saved as PDFs. The earlier Osterwalder–Seiler and scalar-model bibliography remains additional acquisition work, not a completed download.

## ScienceMadeReadable follow-up

At the operator's request, searched https://ask.sciencemadereadable.com using exact-title phrases, author/topic queries with year_to=1995, and its documented `/api/data/works/{doi}` lookup for all four missing papers. DOI lookups returned HTTP 404 (both original and lowercase DOI spellings). Title searches returned unrelated material or later papers mentioning the titles, not the requested originals. Author/topic search surfaced Zinoviev's *Equivalence of the Euclidean and Wightman Field Theories* (hep-th/9408009) as a related lead, not an Osterwalder–Schrader replacement. No missing PDF was obtained through this service; no new PDFs were added and no index rebuild was needed. These search failures are not evidence that the original papers are unavailable elsewhere.

## Commands executed

`pnpm pdf:reindex` completed after the downloads: 5,198 pages from 54 PDFs.

Searches included:

```sh
pnpm pdf:search 'infrared|Balaban|invariant measure|reflection positiv|lattice approximation' -Regex -Book '*yang-mills*' -Limit 25 -Context 180
pnpm pdf:search 'continuum limit|reflection positivity|infrared cutoff' -Regex -Limit 12 -Context 160
pnpm pdf:search 'lattice|invariant|universality' -Regex -Book '*2302*' -Limit 5 -Context 200
```

These are bounded searches, not exhaustive paper review. PDF page numbers below are reliable locators; inferred printed-page labels in the index can be wrong.

## Findings relevant to our conjecture net

1. **More precise scope for the historical ultraviolet results.** Chevyrev review PDF p3 characterizes Balaban and MRS as ultraviolet-stability results, and explicitly distinguishes these from constructing gauge-invariant observables. The previous conversational description of MRS should not be read as a verified full observable-level continuum construction.
2. **A genuinely useful lattice-to-continuum worked example exists in 2D.** Chevyrev–Shen 2302.12160, PDF p6 (read in full), states universality for Wilson, Manton, and Villain actions on T2 under Assumptions 2.6 and 9.12, with Corollary 2.26. Theorem 2.12 supplies dynamic universality; uniqueness of the dynamic is used to identify the limiting measure. The same page states existence and uniqueness of its invariant measure by SPDE methods. This is a concrete model for source/observable identification, not merely a reconstruction axiom checklist.
3. **The 2D result supersedes part of the older review's open-problem list.** The review PDF p27 asks about invariant measures. One must not repeat that question as uniformly unresolved after the newer 2D result.
4. **3D still has a separate missing step in the retrieved sources.** 2503.03060, PDF p2 explicitly says existence of the invariant measure would construct the 3D YMH measure on T3 and is open there. Gauge-covariant local stochastic evolution does not itself supply that measure.
5. **Do not confuse stochastic time with physical time.** None of these passages constructs our four-dimensional Lorentzian Yang–Mills dynamics or repairs the retained fixed-clock scaling obstruction.

Next close reading: 2302.12160 Assumptions 2.6/9.12, Theorem 2.12, and Corollary 2.26, comparing the observable topology and regulator hypotheses against our source. Separately obtain the Balaban/MRS primary texts before proposing to import their estimates. No conjecture-graph claims or proof status were changed by this search.
