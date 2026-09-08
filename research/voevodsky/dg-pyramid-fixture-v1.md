# DG pyramid concrete architecture fixture — iteration 5

`agda/DGPyramidFixture.agda` instantiates the boundary, closure theorem, frame, admissible filler, adapter specification, adapter, and adapted filler end-to-end.

The fixture is deliberately terminal and nonphysical. Its map tokens, positive connector, negative connector, generic-Q cell, and Rees/Cartier cell have distinct nominal types. This verifies that the adapter does not conflate connector directions or derive compatibility cells from scalar equality. The filler supplies all four frame witnesses separately.

The fixture validates type architecture only. Unit-valued validity predicates provide no Marici provenance and are explicitly not exported as physical evidence. No existing research packet is claimed to instantiate the adapter.

Agda 2.8.0.1/Cubical 0.9 accepted the module on its first run under `--safe --cubical --guardedness`, exit0 without warnings, holes, or postulates.

```
pwsh -NoProfile -Command "& 'C:/Users/andrey/tools/agda-2.8.0.1/agda.exe' --transliterate -i research/voevodsky/agda -i C:/Users/andrey/tools/cubical-agda/cubical-0.9 research/voevodsky/agda/DGPyramidFixture.agda"
```

Next iteration: add an aggregate module importing boundary, filler, negative controls, adapter, and fixture; run a fresh closure check and assess any missing requested behavior. No Git operations or analytic changes.
