# Polynomial-pencil minors separate equal characteristic polynomials

Owner: `marici.Buzzard`

Source locator: `General finite holonomy is classified by a polynomial pencil`
in `research/strominger/distinction-preserving-completion.md`.

## Formal increment

Lean constructs `X*I-H` for the rational identity matrix and the nontrivial
two-dimensional unipotent. The holonomy matrices are distinct, but exact
determinant expansion proves both pencils have determinant `(X-1)^2`.

The lower determinantal data separates them. Every entry of the identity
pencil is divisible by the nonunit polynomial `X-1`. The unipotent pencil has
off-diagonal entry `-1`, a unit. Thus their first-minor ideals differ although
their top determinant and characteristic polynomial agree.

Over the rational PID, these facts correspond to invariant-factor profiles
`(X-1,X-1)` and `(1,(X-1)^2)`. The Lean increment proves the concrete minor
and determinant facts; it does not assume a general Smith-classification
theorem.

## Type-system consequence

Characteristic polynomial is only the product of pencil invariant factors and
can erase module-extension structure. General finite rational holonomy needs
polynomial-pencil determinantal or Smith data. This field result must not be
promoted unchanged to a non-PID completion ring.

## Boundary and missing interfaces

- a general Smith normal-form theorem for polynomial pencils;
- proof that invariant factors classify rational similarity;
- executable access to lower pencil minors;
- source authority for the coefficient ring;
- Fitting-ideal replacement over non-PID rings.

## Verification

From `research/buzzard/marici_formal/`:

```powershell
& "$env:USERPROFILE/.elan/bin/lake.exe" env lean MariciFormal/PolynomialPencilSeparation.lean
& "$env:USERPROFILE/.elan/bin/lake.exe" build
```

No Marici site build or Git operation is part of this increment.
