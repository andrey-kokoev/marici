# Marked simplicial bridge: status and stopping criterion

## Result

The attempted bridge from the retained whole-package/higher-comparison generator to simplices is **not complete**. `agda/MarkedSemisimplicial.agda` defines marked triangles and tetrahedra over fixed vertices, projects the four triangular faces, and includes one reflexive edge identity. It does not define a degree-indexed semisimplicial object, all face maps on common domains, degeneracies, or any 4-simplex.

The original identity claims were not well-typed because fixed-vertex face types have different endpoints. They were removed; no evidence for full simplicial identities should be inferred from the remaining projections.

## Why rank four does not follow

A tetrahedron record supplies one tetrahedral coherence witness over four triangle witnesses. It is degree-three data. A genuine 4-simplex requires five tetrahedral faces and their shared-triangle identifications. Grade four in the globular filler tower instead compares two fillers over a fixed boundary. These are different types and neither definition constructs the other automatically.

This matches `coherence-realization-depth-is-a-dependent-filler-tower-not-a-source-cutoff.md`: a four-simplex requires its actual five tetrahedral faces and shared-face identifications; repeated indexing or a filler-comparison does not supply them.

## Verified state

Fresh verification of the current source was rerun during finalization and exited successfully (Agda emitted no diagnostics):

```powershell
pwsh -NoProfile -Command "agda --safe --cubical --guardedness --transliterate -i research/nima/agda -i C:/Users/andrey/tools/cubical-agda/cubical-0.9 research/nima/agda/MarkedSemisimplicial.agda"
```

The current module passes safe Cubical Agda. It contains face projections and `face-identity-01`; no generated claim or receipt for ranks 0–4 exists.

## Smallest next formal obligation

Do not extend the fixed-endpoint projections ad hoc. First specify a single face-compatible simplex family (e.g. maps from standard simplices into a fixed semisimplicial/HIT object, or the ordinary nerve of a declared category). Define all face restrictions on it, prove the semisimplicial identities, and separately prove that the whole-package generator maps into that family preserving retained endpoints and witnesses. To reach degree four, supply five tetrahedral face records and their ten triangular overlaps, with all compatibility paths.

Until those obligations are met, report this effort as an audited partial construction, not proof that this generator produces simplices of ranks 0–4.
