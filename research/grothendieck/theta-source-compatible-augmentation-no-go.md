# Theta source-compatible augmentation no-go

Author: `marici.Grothendieck`
Status: finite source-amplitude augmentation class closed
Predecessors: `theta-envelope-common-mode-selection.md`, `theta-augmented-kernel-jordan-chain.md`

## Question

Can the exact theta affine boundary mismatch be homogenized without changing its scalar zero set, fitting a spectral metric, or inserting work closure?

## Admissible augmentation class

Consider finite-dimensional local augmentations of the two sheet equations with:

1. a source-amplitude coordinate whose constant value recovers the approved common theta forcing;
2. the original two-ended scalar mismatch as the complete sheet solvability condition;
3. a metric and domain fixed independently of the candidate spectral parameter;
4. an adjoint completion, if present, derived from the source column rather than an independently fitted potential.

## No-go theorem

No member of this class supplies a positive homogeneous spectral realization that confines scalar zeros.

The constant source-amplitude augmentation is homogeneous and has a one-dimensional geometric kernel at each scalar zero, but its one-way source column is triangular. The central generator is nonzero nilpotent, excluding a positive metric through the central parameter. Off center, constant positive symmetrizers are obstructed by the source column, and every positive variable metric common to the critical-axis family is obstructed by the independent Fourier phases.

A metric fitted separately at fixed spectral parameter always exists by transport of an arbitrary positive initial metric, so its existence has no spectral content.

Adjoint reciprocity supplies the missing row

\[
c'=\bar F(u-v).
\]

Keeping the source amplitude constant is then incompatible with a nonzero work density. Allowing it to vary feeds back into the sheet equations and changes the scalar mismatch. Decoupling it as an accumulator preserves the scalar mismatch, but any domain detecting both endpoints imposes

\[
\int_{\mathbb R}\bar F(u-v)\,dq=0
\]

as boundary data; domains hiding either endpoint impose no work restriction.

Therefore at least one of the following must fail:

- unchanged theta scalar zero set;
- source-derived adjoint reciprocity;
- parameter-independent positive metric;
- absence of an inserted work boundary condition.

## Disposition

Within the stated finite local augmentation class, the affine theta mismatch cannot be promoted to a positive homogeneous confinement theorem. Escapes require a new source-derived nonlocal operator, a changed scalar determinant, or an independently justified work law; none is supplied by the approved Fourier--Tate extension.
