# Direct quotient lift removes equality transport

Owner: `marici.Buzzard`

Source locator: ergonomic residual recorded in
`research/buzzard/axis-ideal-quotient.md`.

## Interface repair

The initial quotient equivalence rewrote `(u,v)` to the literal evaluation
kernel before invoking Mathlib's first-isomorphism equivalence. That produced a
valid ring equivalence, but its computation theorem lived behind dependent
transport of the quotient's ideal parameter.

Lean now instead defines `axisEvalLift` directly on
`Q[u,v] ⧸ axisIdeal` using `Ideal.Quotient.lift`:

- well-definedness follows from `axisIdeal = ker(eval origin)`;
- injectivity follows from the reverse kernel containment;
- surjectivity uses constant-polynomial representatives;
- `RingEquiv.ofBijective` packages the direct lift as the quotient
  equivalence.

The resulting theorem
`axisIdealQuotientEquivRat_apply_mk` computes definitionally: applying the
equivalence to the quotient class of a polynomial returns its origin
evaluation.

## Audit disposition

The earlier missing interface was repaired without axioms and without changing
the quotient theorem. The direct quotient lift is explicitly noncomputable,
matching Mathlib's polynomial quotient representation. No geometric or
physical interpretation is added.

## Verification

From `research/buzzard/marici_formal/`:

```powershell
& "$env:USERPROFILE/.elan/bin/lake.exe" env lean MariciFormal/AxisIdealQuotient.lean
& "$env:USERPROFILE/.elan/bin/lake.exe" build
```

No Marici site build, Git command, commit, or push is part of this increment.
