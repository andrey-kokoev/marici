# Framed dg pyramid filler — iteration 2

## Objective slice

Define the filler as a dependent fibre over the discrepancy from `DGPyramidBoundary`, while keeping support, endpoint, generic-Q, and Rees/Cartier conditions explicit and independent.

## Construction

`agda/DGPyramidFiller.agda` imports the filler-free boundary record. `PyramidFrame P` adds only:

- the degree-zero candidate type Hom^0(J,F), represented as `JFzero`;
- its differential into the already typed Hom^1(J,F);
- four predicates: `PreservesSupport`, `PreservesEndpoints`, `PreservesGenericQ`, and `PreservesReesCartier`.

`PreservesFrame` is an explicit nested Sigma of all four predicates. `AdmissibleFiller P Frame` is

    Sigma K : JFzero,
      Sigma (delta K = pyramidDiscrepancy P),
        PreservesFrame K.

Thus it is the requested framed fibre. The boundary equation does not imply any frame condition. `BoundaryFiller` is the unframed fibre, and `forgetFrame` is intentionally one-way: no constructor promotes an unframed filler to a framed one.

Projection theorems recover the candidate, boundary equation, and each of the four conditions separately. `refineFrame` permits transport to a refined frame only when the client supplies both preservation of the differential and an explicit map of all frame witnesses. This prevents equality of underlying candidates from silently transporting support or filtration admissibility.

## Scope

The predicates are interfaces for source-derived evidence, not declarations that arbitrary predicates encode the physical conditions. No current Marici primitive is installed as a filler. No contractibility, inhabitation, or uniqueness of this fibre is claimed. The boundary record remains unchanged and filler-free.

## Verification

Agda 2.8.0.1/Cubical 0.9 accepted the module with `--safe --cubical --guardedness`, exit0 and no warnings. The first run found blocked implicit boundary-record metavariables in projection theorem result types; passing `P` and `Frame` explicitly to `fillerCandidate` repaired them, and the rerun passed. No holes or postulates.

```
pwsh -NoProfile -Command "& 'C:/Users/andrey/tools/agda-2.8.0.1/agda.exe' --transliterate -i research/voevodsky/agda -i C:/Users/andrey/tools/cubical-agda/cubical-0.9 research/voevodsky/agda/DGPyramidFiller.agda"
```

Next iteration: encode negative controls against false filler promotion and false physical-source instantiation. No Git operations or analytic-interface changes.
