# Boundary adjointness and the spectral seam: Lean packet

## Source boundary

This increment formalizes the convention-fixed infinitesimal core of
Grothendieck's
`adjointness-of-the-boundary-cocycle-characterizes-the-critical-seam.md`.
The packet distinguishes the algebraic seam criterion from the missing
continuous extension theorem.

## Formal objects

The coefficient type is Lean's complex numbers. For spectral parameter `z`,
the reciprocal and adjoint infinitesimal generators are

\[
-iz,
\qquad
-i\overline z.
\]

`InfinitesimallyStarCompatible z` asserts equality of these two generators.

## Theorems and hostile

- `infinitesimal_starCompatible_iff_im_eq_zero` proves that generator
  compatibility is equivalent to `z.im = 0`.
- `infinitesimal_starCompatible_of_real` supplies the real-axis instance.
- `SummableBoundaryRecord` deliberately stores only a complex boundary value,
  not an adjointness witness.
- `summable_record_does_not_force_starCompatibility` gives a finite hostile:
  a record with value `i` exists but is off the seam and is not compatible.

This makes the typing distinction exact: completion-class membership is not
star-compatible descent.

## Missing interfaces

The source argument from equality of the full continuous boundary family to
equality of infinitesimal generators needs a typed family indexed by positive
length, differentiability at the seam endpoint, strict positivity/nonvanishing
of the source amplitude, and compatibility of reciprocal transport with
complex conjugation. Most importantly, the zero-induced discrete prime record
must be shown to extend to that family. That extension is the active
RH-strength conjectural gate and is not assumed.

## Verification boundary

The intended targeted command is:

```text
lake env lean MariciFormal/BoundaryAdjointSeam.lean
```

It was not run because Nima's active no-build instruction remains in force.
The module remains outside `MariciFormal.lean`.
