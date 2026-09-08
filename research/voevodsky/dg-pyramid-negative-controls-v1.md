# DG pyramid negative controls — iteration 3

`agda/DGPyramidNegativeControls.agda` encodes the three requested exclusions.

1. `normalizedSourceCannotBeBoundary` reuses the checked primitive-cycle theorem: a map taking the source cycle to one cannot have a zero-preserving nullhomotopy.
2. `EndpointJetControl` retains separate source, endpoint, ambient, and jet types. Its pointwise annihilation hypothesis yields zero after arbitrary precomposition through literal endpoint inclusion. No converse from zero readout to zero cochain is provided, and extraordinary support-changing maps are outside the theorem.
3. `TargetTriangleMasquerade` requires both physical-source provenance and normalization identification. Distinct origin constructors give one contradiction; the normalized-to-exact comparison gives an independent contradiction. Thus a valid target-derived obstruction presentation cannot be silently installed as the physical source.

An additional frame regression proves that an unframed boundary filler cannot populate a frame with an impossible support predicate. This complements the one-way `forgetFrame` interface.

These are scoped controls, not a theorem that every future physical filler is impossible. In particular, an independently constructed extraordinary adapter need not factor through literal endpoint inclusion and is not rejected merely for being support-changing.

Agda 2.8.0.1/Cubical 0.9 accepted `DGPyramidNegativeControls.agda` under `--safe --cubical --guardedness`, exit0 without warnings. The first check found that implicit P/Frame were unavailable in the clause body; explicitly binding them repaired the error. No holes or postulates.

```
pwsh -NoProfile -Command "& 'C:/Users/andrey/tools/agda-2.8.0.1/agda.exe' --transliterate -i research/voevodsky/agda -i C:/Users/andrey/tools/cubical-agda/cubical-0.9 research/voevodsky/agda/DGPyramidNegativeControls.agda"
```

Next iteration: adapter interface for concrete object comparisons, map transports, and endpoint connector cells. No Git operations or analytic-interface changes.
