# Kernel and adjoint-kernel variance

Owner: `marici.Buzzard`

Source locator: `Kernel and cokernel carry opposite variance`, `Self-duality
requires two additional cells`, and `The Green current is the adjointness
residual` in `research/strominger/distinction-preserving-completion.md`.

## Formal increment

Lean implements the rational observation matrix `[[1,1],[0,0]]` and its
transpose `[[1,0],[1,0]]`. It characterizes their kernels exactly:

- the ordinary kernel is the line `(-t,t)`;
- the adjoint kernel is the line `(0,t)`.

Both are one-parameter lines, but explicit nonzero witnesses show neither is
the other. Thus equality of defect dimensions does not identify invisible
parameter directions with dual unattainable-observation directions.

With identity pairings, Lean defines the Green residual `M-M^T` and proves it
acts as `(x,y) -> (y,-x)`. The residual is nonzero and the two maps remain
unequal. Retaining the current therefore records failed adjointness; it does
not restore it.

## Type-system consequence

Kernel and cokernel witnesses require distinct variance labels even when their
dimensions agree. Identifying them needs both a perfect parameter-observation
duality and an adjointness cell. A boundary residual is evidence of the missing
cell, not a constructor for it.

This increment specializes the Smith-profile defect data by preserving cause
versus readout variance.

## Boundary and missing interfaces

- typed parameter and observation modules rather than a shared coordinate type;
- a source-derived perfect pairing between those modules;
- the physical observability operator and its adjoint;
- a boundary condition annihilating the Green residual on an admitted domain;
- cokernel duality and derived-specialization interfaces.

## Verification

From `research/buzzard/marici_formal/`:

```powershell
& "$env:USERPROFILE/.elan/bin/lake.exe" env lean MariciFormal/KernelCokernelVariance.lean
& "$env:USERPROFILE/.elan/bin/lake.exe" build
```

No Marici site build or Git operation is part of this increment.
