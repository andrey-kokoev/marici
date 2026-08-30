# Residue-flag comparison holonomy

Owner: `marici.Buzzard`

Source locator: `Comparison cells themselves form a torsor` and `Pairwise
comparison can carry triangle holonomy` in
`research/strominger/distinction-preserving-completion.md`.

## Formal increment

Lean defines three rational flag generators and three invertible comparison
matrices carrying each flag to the next. Every edge comparison is valid, but
their cycle product is exactly

`[[1,1],[0,-1]]`.

This holonomy is not the identity, although it stabilizes the starting flag.
Lean therefore proves an explicit pairwise-valid but triple-incoherent
comparison fixture.

Lean also supplies two distinct invertible matrices carrying the same first
flag to the same second flag. Comparison existence therefore does not select a
unique comparison cell; the choice retains stabilizer freedom.

## Type-system consequence

Endpoint maps and residue flags do not determine comparison cells. Pairwise
comparability also does not imply coherent descent: the cycle product must be
the identity or be accounted for by a separately authorized higher cell.

The existing generic `HolonomyAudit` records only a declared defect value. This
increment specializes rather than broadens it by computing the matrix-valued
residual that justifies a nonzero defect declaration.

## Boundary and missing interfaces

- a typed groupoid of residue flags and comparison cells;
- stabilizer actions and an explicit torsor proof;
- gauge transformation and conjugacy invariance of holonomy;
- source-authorized comparison or triangle cells;
- executable scalar and non-scalar holonomy probes.

## Verification

From `research/buzzard/marici_formal/`:

```powershell
& "$env:USERPROFILE/.elan/bin/lake.exe" env lean MariciFormal/ResidueFlagHolonomy.lean
& "$env:USERPROFILE/.elan/bin/lake.exe" build
```

No Marici site build or Git operation is part of this increment.
