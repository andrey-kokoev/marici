# Prime staircase logarithmic-chart boundary: Lean packet

## Source boundary

This increment formalizes the typing distinction in Grothendieck's
`the-prime-staircase-is-a-logarithmic-chart-not-a-zero-state.md` and classifies
the analytic theorem in
`hurwitz-forbids-zero-creation-by-stable-euler-completion.md`.

## Formal objects and coefficient types

Over an arbitrary field, `logarithmicDerivativeChart value derivative` returns
an `Option`: it is `some (derivative/value)` only when the scalar value is
nonzero, and `none` on the divisor. `LogarithmicChartAvailable` records
inhabitation of this partial chart.

Finite Euler packets use arbitrary decidable label types and field-valued
local factors.

## Theorems and hostile examples

- `logarithmicChart_available_iff` proves chart availability is exactly scalar
  nonvanishing.
- `logarithmicChart_unavailable_at_zero` forbids using the chart as a regular
  zero-state.
- `totalizedDivision_is_not_chart_hostile` records that Lean proves `1/0=0`
  while the typed chart correctly returns `none`.
- `finiteEulerProduct_ne_zero` and
  `finiteEuler_logarithmicChart_available` prove finite nonzero local factors
  support the multiplicative object and its logarithmic chart.
- `multiplicative_nonzero_additive_cancel_hostile` shows a nonzero product can
  coexist with a zero additive coordinate.

This preserves the constructor distinction: logarithmic differentiation is a
partial tangent chart, not a linear compression and not a divisor state.

## Hurwitz gate and missing interfaces

The stable-completion theorem requires connected complex domains, holomorphic
nowhere-zero finite sections, locally uniform convergence, and Hurwitz's
zero-free-or-identically-zero theorem. Those complex-analytic interfaces are
not encoded here and the dichotomy is not assumed as an abstraction. Its
established consequence is classified explicitly: an isolated-zero completed
section cannot be the locally uniform holomorphic limit of ordinary nowhere-zero
finite Euler sections. A relative determinant must therefore alter the finite
objects, transition data, topology, or boundary channels before the limit.

## Verification boundary

The intended targeted command is:

```text
lake env lean MariciFormal/LogarithmicChartBoundary.lean
```

It was not run because Nima's active no-build instruction remains in force.
The module remains outside `MariciFormal.lean`.
