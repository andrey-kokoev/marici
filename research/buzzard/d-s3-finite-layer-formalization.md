# Frozen finite `D(S3)` layer in Lean

Owner: `marici.Buzzard`

Source: `research/kitaev/s3-quantum-double-ribbon-typing.md` and its exact
checker `research/kitaev/checkers/check_s3_quantum_double_ribbon.py`.

Strength: exact finite algebraic census and explicit permutation calculation.
This packet does not claim a braided fusion category or a physical ribbon
implementation.

## Formal objects

- `ConjugacyClass` is the three-element cycle-type label: identity,
  transposition, or three-cycle.
- `classSize` is the frozen table `1, 3, 2`.
- `centralizerOrder` is the frozen table `6, 2, 3`.
- `CentralizerIrrep` is a class-indexed family with the three `S3` irreps, two
  `C2` irreps, and three `C3` irreps. `irrepDimension` records dimensions
  `1,1,2`, `1,1`, and `1,1,1`.
- `AnyonLabel` is the eight-element frozen label type. `labelClass` and
  `quantumDimension` record the class and the dimension `|C| dim(rho)`.
- `TranspositionFlux` is the ordered basis `(01),(12),(02)`.
  `conjugationBraid` is the permutation `[0,2,1]` induced by conjugation by
  `(01)`.
- `t01Perm`, `t12Perm`, and `t02Perm` are concrete functions on `Fin 3`.
  `conjugate_t12_by_t01` proves the underlying pointwise permutation identity.

## Certified theorems

- `centralizer_irrep_square_census`: each centralizer irrep list satisfies the
  finite sum-of-squares identity for its frozen centralizer order.
- `allLabels_exhaustive`: the explicit eight-label list is duplicate-free and
  contains every constructor.
- `quantum_dimension_list`: the dimensions are exactly
  `[1,1,2,3,3,2,2,2]`.
- `quantum_dimension_square_sum`: their squared sum is `6^2 = 36`.
- `conjugation_braid_permutation` and `conjugation_braid_involutive`: the
  transposition basis action fixes `(01)` and exchanges `(12)` with `(02)`.
- `conjugation_braid_not_scalar`: a scalar action cannot relabel a basis
  element, while this action sends `(12)` to `(02)`.
- `conjugate_t12_by_t01`: the table is grounded in the explicit equality
  `(01)(12)(01) = (02)` on `Fin 3`.

## Assumptions and coefficient types

The module uses only finite inductive types, natural-number dimensions, lists,
and functions `Fin 3 -> Fin 3`. There is no field of complex coefficients and
no imported physical or categorical axiom. The phrase "not scalar" is typed
only at the flux-label level: a scalar phase preserves a basis label, whereas
the proved conjugation action changes one. It is not a theorem about a full
linear `R`-matrix.

The class sizes, centralizer orders, irrep labels, and irrep dimensions are
frozen source data. Lean verifies every stated consequence of those tables; it
does not derive the representation classification of `S3` from group axioms.

## Exact boundary and missing interfaces

The finite layer cannot faithfully support fusion or coherence claims without:

1. a source-frozen oriented ribbon-operator type and multiplication law;
2. fusion spaces or fusion multiplicities derived from that multiplication;
3. typed associator and braiding maps on those spaces;
4. pentagon and hexagon witnesses;
5. endpoint framing/base conventions and comparison transport;
6. a physical realization map if laboratory availability is claimed.

`FrozenFiniteLayer` intentionally contains none of these fields. Therefore the
verified census cannot be promoted to a braided fusion category merely by
transport or naming.

## Verification

Run from `research/buzzard/marici_formal/`:

```powershell
& "$env:USERPROFILE/.elan/bin/lake.exe" env lean MariciFormal/DS3Finite.lean
& "$env:USERPROFILE/.elan/bin/lake.exe" build
```

Results on 2026-08-25:

- targeted file: exit code `0`, no diagnostics;
- project build: `Build completed successfully (8731 jobs)`;
- no Marici site build was run.

Changed owned files:

- `research/buzzard/marici_formal/MariciFormal/DS3Finite.lean`
- `research/buzzard/marici_formal/MariciFormal.lean`
- `research/buzzard/d-s3-finite-layer-formalization.md`

No Git command was used. Nothing was committed or pushed.
