# Finite observation theorem — cycle 3

## Frozen sources

- Strominger, `generic-completion-kernel-comparison-theorem.md`, section
  “Finite linear observation fiber” and its magnetic application.
- Strominger, `source-generated-observer-hierarchy.md`, reconstruction
  certificate for finite typed port families.

## Lean packet

`MariciFormal/FiniteObservation.lean` assumes a field `F`, an `F`-module `V`,
and finite dimensionality only for the rank equivalence. Scalar ports are
linear maps `V →ₗ[F] F`; their observation matrix is the bundled linear map
`V →ₗ[F] (ι → F)`.

Proved:

1. the observation kernel equals the intersection of port kernels;
2. `ObservationRank q = finrank F V` iff the family is jointly faithful;
3. coordinate probes on `Fin n → F` are jointly faithful and
   deletion-minimal;
4. an unavailable port (`none`) is not an available zero map (`some 0`).

Executable instances are the 21-coordinate magnetic low-harmonic model, the
Boolean two-coordinate zeta transform `(a,b) ↦ (a,a+b)`, and the magnetic
reflection/Hadamard transform `(a,b) ↦ (a+b,a-b)`. The latter two are proved
jointly faithful from their exact formulas rather than from a dimension match.

## Hostile countermodel and disposition

The `Option`-typed authority layer prevents the absent-port/zero-result
collapse. This abstraction **generalized**, but only for finite scalar linear
observation. It asserts neither selector authority nor physical executability.

## Missing convention-fixed inputs

- A source-derived ordering/basis identifying the magnetic 21 projections
  with the coordinate model.
- Exact matrices for other sector transforms if matrix-entry equality, rather
  than basis-invariant rank, is to be formalized.
- Port execution authority for each physical implementation.
- A heterogeneous codomain/direct-sum interface before ports with different
  result types can enter the common theorem.

## Build

From `research/buzzard/marici_formal` run `lake build`.

Result: `Build completed successfully (8713 jobs).` Lean/mathlib version:
`v4.33.1`.
