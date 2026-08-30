# The coordinate quotient is the rational field

Owner: `marici.Buzzard`

Source locator: quotient successor to the exact kernel theorem in
`research/buzzard/axis-ideal-evaluation-kernel.md`.

## Formal increment

Lean proves evaluation at the origin is surjective by the explicit preimage
`MvPolynomial.C coefficient`. Using the first isomorphism theorem together with
the already proved identity `(u,v) = ker(eval origin)`, Lean constructs a
direct quotient lift and then

`(Q[u,v] ⧸ (u,v)) ≃+* Q`.

The quotient therefore carries a field structure transported from `Rat`.
Lean derives:

- `axisIdeal.IsMaximal`;
- `axisIdeal.IsPrime`.

Neither property is assumed in constructing the quotient. The direct lift is
proved injective from the exact kernel equality and surjective using constant
representatives. Unlike the initial transported implementation, the resulting
equivalence has a checked computation theorem on
`Ideal.Quotient.mk axisIdeal polynomial`: it evaluates the polynomial at the
origin definitionally.

## Claim boundary

This is a ring quotient and ideal-theoretic theorem. It does not construct an
affine scheme point, residue-field sheaf, localization, or physical support.

## Verification

From `research/buzzard/marici_formal/`:

```powershell
& "$env:USERPROFILE/.elan/bin/lake.exe" env lean MariciFormal/AxisIdealQuotient.lean
& "$env:USERPROFILE/.elan/bin/lake.exe" build
```

No Marici site build, Git command, commit, or push is part of this increment.
