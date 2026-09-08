# DG pyramid offline-output adapter — iteration 4

`agda/DGPyramidAdapter.agda` adds the requested adapter without modifying the boundary or filler records.

`AdapterSpecification P` declares concrete source/generic/supported object types; types of their comparison maps; validity predicates for each map; concrete q,e,hM,HC cells and realization functions into the exact Hom degrees of P; two separately typed endpoint connector cells; and separately typed generic-Q and Rees/Cartier comparison cells with validity predicates.

`DGPyramidAdapter Spec` requires inhabitants and witnesses for every item. Paths `identifiesQ`, `identifiesE`, `identifiesHM`, and `identifiesHC` force the concrete cells to instantiate the selected boundary rather than merely match scalar outputs. Plus and minus endpoint connectors cannot be reconstructed from one another or from generic-Q data.

Closure is inherited from `pyramidDiscrepancyClosed`; the adapter cannot submit closure as an independent assertion. `AdaptedFiller` pairs an adapter with the unchanged four-condition framed filler. Adapter data alone do not produce a filler.

This interface permits a packet to model strict maps, roofs, or richer comparison records by its chosen concrete types and validity predicates. It checks internal typing once instantiated; it does not certify provenance merely because predicates were named. There is deliberately no constructor from artifact paths, scalar signatures, target-derived triangles, or literal endpoint readouts.

Agda 2.8.0.1/Cubical 0.9 accepted the module under `--safe --cubical --guardedness`, exit0 without warnings. The first run left the implicit boundary record unresolved in the inherited-closure theorem; binding P explicitly repaired it. No holes or postulates.

```
pwsh -NoProfile -Command "& 'C:/Users/andrey/tools/agda-2.8.0.1/agda.exe' --transliterate -i research/voevodsky/agda -i C:/Users/andrey/tools/cubical-agda/cubical-0.9 research/voevodsky/agda/DGPyramidAdapter.agda"
```

The five requested architecture items now exist at interface level. Remaining iterations should add concrete regression fixtures and an aggregate checked import before assessing completion; they must not invent a physical adapter instance. No Git operations or analytic changes.
