# First hostile scan finds no reduced-source Pick violation

A zero-free complex evaluator was built from:

- Euler-transformed Dirichlet eta and its derivative;
- the exact relation between `eta'/eta` and `zeta'/zeta`;
- recurrence plus asymptotic Bernoulli expansion for digamma;
- the endpoint-reduced formula for `F`.

On a 117-point grid spanning

\[
 -100\le\operatorname{Re}t\le100,qquad
 0.01\le\operatorname{Im}t\le100,
\]

no negative value of `Im F(t)` was found. The smallest sampled value is about
`7.34e-4` at `t=100+0.01i`. A synthetic negative-residue pole produces the
predicted negative sign and verifies that the scan can detect the hostile
mechanism.

This is encouraging but weak evidence. The evaluator is ordinary complex
floating point, the grid is sparse, and near-pole or large-height behavior is
not interval-controlled. It neither proves the Pick condition nor excludes a
small negative lobe between sample points.

## Next falsifier

Build an interval complex evaluator on adaptive boxes near the real positive
axis and near images of the critical strip, where `Im F` can become small.
The first target is a certified compact-region minimum or an explicit negative
box.

## Durable verification

- Checker: `checkers/reduced_source_pick_hostile_scan.py`
- Result: `results/reduced-source-pick-hostile-scan.json`

Normalizing by the boundary height and scanning the diagonal Loewner slope
also finds no negative value across seven decades of positive `x`. See
`reduced-source-pick-boundary-slope-scan.md`.
