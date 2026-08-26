# Lower determinantal data resolves deeper rank strata

Owner: `marici.Buzzard`

Source locator: `Over a non-PID, Fitting ideals replace Smith factors` and
`Fitting ideals recover the nested rank strata` in
`research/strominger/distinction-preserving-completion.md`.

## Formal increment

Lean uses the actual multivariable polynomial ring `Q[u,v]` and constructs the
matrices

`A = diag(u,v)` and `B = diag(1,u*v)`.

Exact determinant expansion proves both determinants equal `u*v`. Lean then
specializes at the origin. Matrix `A` becomes zero and annihilates every
vector, while `B` becomes `diag(1,0)` and has an explicit nonzero image.

Thus the shared top determinant locus does not determine the deeper rank-zero
stratum. Lower minors separate the presentations: `B` visibly contains the
unit entry one, while every entry of `A` vanishes at the origin.

## Type-system consequence

Smith-factor interfaces are coefficient-ring dependent and cannot be copied
unchanged from a PID to a multivariable completion ring. Determinantal or
Fitting ideals are the presentation-stable replacement for nested rank
strata. This increment proves the finite rank-stratum distinction but does not
formalize nonprincipality of the ideal `(u,v)`.

## Boundary and missing interfaces

- formal ideals of all minors and their Fitting-module interpretation;
- a proof that `(u,v)` is nonprincipal in `Q[u,v]`;
- presentation invariance under row and column equivalences;
- identification of the source-authorized completion ring;
- executable access to lower-minor strata.

## Verification

From `research/buzzard/marici_formal/`:

```powershell
& "$env:USERPROFILE/.elan/bin/lake.exe" env lean MariciFormal/FittingRankStrata.lean
& "$env:USERPROFILE/.elan/bin/lake.exe" build
```

No Marici site build or Git operation is part of this increment.
