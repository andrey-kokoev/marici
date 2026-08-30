# Compatible base change need not reflect distinctions

Owner: `marici.Buzzard`

Source locator: hostile audit of the base-change interface formalized in
`research/buzzard/determinantal-profile-base-change.md`.

## Formal increment

Lean defines the rational specialization point `unitPoint` by
`u = 1, v = 1`. Exact evaluation proves that both running fixtures specialize
to the identity matrix:

`diag(u,v) |_(1,1) = 1`

and

`diag(1,u*v) |_(1,1) = 1`.

The source determinantal profiles are already proved unequal. Nevertheless,
their images under `mapTwoByTwoDeterminantalProfile (eval unitPoint)` are
equal. The combined hostile theorem therefore proves:

- profile construction commutes with this base change;
- this base change does not reflect source-profile inequality.

## Audit disposition

This countermodel rejects the premature inference “functorial under
specialization, therefore faithfully reconstructible after specialization.”
It does not claim every coefficient map loses information. At the origin, the
previous increment proved that the same pair remains separated. Faithfulness
is thus an additional property of a chosen map and source class, not a
consequence of base-change compatibility alone.

No flatness, faithful-flatness, geometric-fiber, or physical-observation claim
is encoded.

## Verification

From `research/buzzard/marici_formal/`:

```powershell
& "$env:USERPROFILE/.elan/bin/lake.exe" env lean MariciFormal/BaseChangeNonreflection.lean
& "$env:USERPROFILE/.elan/bin/lake.exe" build
```

No Marici site build, Git command, commit, or push is part of this increment.
