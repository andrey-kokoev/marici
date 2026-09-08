# DG pyramid public-contract audit — iteration 8

The checked implementation already had the requested semantics, but several mathematical names were only documented rather than exported. This audit adds compatibility accessors:

- `J`, `Q`, `F` for the source, generic, and supported object labels;
- `h_M`, `H_C` for the two homotopy cells;
- `Hom⁰JF` for the frame's degree-zero candidate type;
- `concreteSourceComparison`, `concreteGenericComparison`, and `concreteTargetComparison` for the applied adapter maps.

The underlying record fields and closure proof are unchanged. `DGPyramidBoundary` still contains no filler. The applied adapter accessors ensure a packet exposes actual functions on its concrete object types, while validity and connector witnesses remain separate.

The terminal fixture now checks all aliases and applies both source and target comparisons. During the audit, Cubical Prelude's existing eliminator `J` clashed with the requested object name; the boundary module now hides that import locally, and external uses can qualify `DGPyramidBoundary.J`. A subsequent fixture annotation using product notation was incompatible with the transliteration invocation, so it was replaced by the equivalent nested Sigma spelling used elsewhere.

A fresh aggregate build with Agda 2.8.0.1/Cubical 0.9 passed under `--safe --cubical --guardedness`, exit0 without warnings, holes, or postulates. Mutable offline state was checked; no result newer than the partial relative comparison is present.

Remaining nonredundant work: prove accessor-level equations showing the named discrepancy is literally `H_C - e ∘ h_M`, rerun positive and negative suites, then produce the final requirements matrix. No Git operations or analytic changes.
