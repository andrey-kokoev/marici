# Linear-growth power-weight threshold

Owner: `marici.Buzzard`

Source locator: the power-model fixtures in `Exact weighted-rigging criterion`
within `research/strominger/distinction-preserving-completion.md`.

## Formal increment

For natural `n` and natural weight exponent `beta`, Lean defines the weighted
dual term for linear coefficient growth by

`((n+1):Real)^2 / ((n+1):Real)^beta`.

The successor convention avoids the artificial zero-index singularity. Using
Mathlib's real p-series theorem, Lean proves:

- quadratic weight gives the constant-one series and is not summable;
- cubic weight gives the shifted harmonic series and is not summable;
- quartic weight gives the shifted inverse-square series and is summable.

This exactly verifies Strominger's three named fixtures: quadratic and cubic
weights fail, with cubic on the harmonic boundary, while quartic succeeds
mathematically.

## Boundary and authority

The theorem uses natural exponents and the `n+1` indexing convention. It does
not yet state the general real-exponent equivalence
`beta - 2*alpha > 1`. A general upgrade must choose between natural powers,
integer powers, and real `rpow`, and must state coefficient absolute-value
conventions.

Mathematical success of quartic weight is not source authority for selecting
it. An authorized rigging still needs a source constructor or grammar that
admits and distinguishes the weight.

The abstraction specialized deliberately to independently checkable fixtures
rather than promoting an under-typed general exponent statement.

## Verification

From `research/buzzard/marici_formal/`:

```powershell
& "$env:USERPROFILE/.elan/bin/lake.exe" env lean MariciFormal/PowerWeightThreshold.lean
& "$env:USERPROFILE/.elan/bin/lake.exe" build
```

The targeted command exited `0` without warnings or diagnostics. No site build
or Git command was run.

Changed owned files:

- `research/buzzard/marici_formal/MariciFormal/PowerWeightThreshold.lean`
- `research/buzzard/marici_formal/MariciFormal.lean`
- `research/buzzard/linear-power-weight-threshold.md`
