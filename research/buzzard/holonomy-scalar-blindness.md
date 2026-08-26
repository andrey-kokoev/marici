# Scalar holonomy ports are not jointly faithful

Owner: `marici.Buzzard`

Source locator: `Scalar holonomy ports are not jointly faithful` in
`research/strominger/distinction-preserving-completion.md`.

## Formal increment

Lean compares the rational identity matrix with the nontrivial unipotent
matrix `[[1,1],[0,1]]`. They are distinct, but both have trace two and
determinant one. The paired scalar observation `(trace,determinant)` is
therefore not injective even on this two-element fixture.

Lean defines displacement as `(H-I)v`. Identity displacement is zero on every
vector. Unipotent displacement is exactly `(x,y) -> (y,0)`, and Lean proves
its range is precisely the first coordinate line and supplies an explicit
nonzero displaced vector. This is the structural rank-one discriminator.

## Type-system consequence

Conjugacy-invariant scalar characters can miss nonidentity holonomy. A faithful
obstruction packet needs additional Jordan, nilpotent, or displacement data.
The existence of that mathematical discriminator does not authorize a sector
readout port measuring it.

This increment specializes the matrix-valued residue holonomy theorem with a
hostile probe-faithfulness test.

## Boundary and missing interfaces

- a general matrix-rank or Jordan-type observation interface;
- conjugacy invariance of the chosen displacement data;
- higher-dimensional unipotent countermodels;
- source-authorized non-scalar holonomy probes;
- operational realization of displacement readout.

## Verification

From `research/buzzard/marici_formal/`:

```powershell
& "$env:USERPROFILE/.elan/bin/lake.exe" env lean MariciFormal/HolonomyScalarBlindness.lean
& "$env:USERPROFILE/.elan/bin/lake.exe" build
```

No Marici site build or Git operation is part of this increment.
