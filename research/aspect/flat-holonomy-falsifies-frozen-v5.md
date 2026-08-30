# Flat holonomy falsifies frozen v5

## Result

Version 5 is falsified as a global network signature.

Its resolved metric, valuation, radical, and chart-gluing data do not determine global transport coherence. Two packets can agree on every field required by v5 while having different spaces of globally parallel records.

## Hostile packet

Take one resolved rank-one route line over a circle. Give it the constant Gram matrix

\[
G=(1).
\]

There is no determinant divisor, the radical is zero, every valuation vector is zero, and the chart bundle may be glued with identity transition maps.

Now put either of two flat unitary connections on that same bundle:

- trivial loop holonomy, (H_+=(1));
- half-turn loop holonomy, (H_-=(-1)).

Both preserve (G). They have identical rank, determinant, radical, valuation, crossing-form, resolved-chart, and bundle-transition data. Consequently every declared v5 field can be held fixed.

## Decisive difference

A global parallel record (s) must satisfy

\[
Hs=s.
\]

For (H_+), every scalar record satisfies this equation, so the invariant space has dimension one. For (H_-), the equation is (-s=s), so only (s=0) survives.

Thus the two packets have different global descent while sharing all v5 data.

## Exact failure

Chart transition maps describe the underlying resolved bundle. They do not specify a connection on that bundle. Metric preservation constrains holonomy to the isometry group but does not select an isometry-group representation of the loop group.

The absent datum is therefore not another exceptional divisor. It is transport around loops of a resolved stratum.

Nima's norm-one log-window leakage has the same shape: local resolved charts can be exact while a unit-modulus boundary channel survives global closure.

## Required successor

A successor must add:

- a transport local system on every resolved stratum;
- a functor from the stratum path groupoid into metric route isometries;
- compatibility of holonomy with exceptional specialization and completed sewing;
- an explicit boundary-port obstruction preventing strict descent when loop transport has no invariant vectors.

The next unused hostile should combine nontrivial holonomy with a degeneration so that specialization changes the loop representation.

## Verification

```text
uv run --with sympy python research/aspect/checkers/check_v5_flat_holonomy_falsifier.py
```
