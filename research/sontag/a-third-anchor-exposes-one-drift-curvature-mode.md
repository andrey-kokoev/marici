# A Third Anchor Exposes One Drift Curvature Mode

## Question

What does a midpoint reference measurement actually establish beyond the
two-anchor affine gain design?

## Endpoint alias under quadratic drift

The five-record schedule

\[
(XX,YY,XY,YX,XX)
\]

at times zero through four identifies affine common drift and three relative
setting offsets. It does not distinguish those offsets from a quadratic common
drift sampled only once at each interior setting.

Take

\[
g(t)=t(t-4).
\]

The endpoint reference records vanish, while the interior records are

\[
(-3,-4,-3).
\]

The same five-record packet is produced by zero common drift and static setting
offsets \((-3,-4,-3)\). Endpoint anchoring alone aliases curvature with setting
dependence.

## Three-reference schedule

Use the six-record schedule

\[
(XX,YY,XX,XY,XX,YX)
\]

at times zero through five. The reference setting is now sampled at times zero,
two, and four. For the quadratic model

\[
z(t,i)=a+bt+ct^2+\delta_i,
\qquad
\delta_{XX}=0,
\]

the six unknown coordinates are \(a,b,c\) and the three relative setting
offsets. The design matrix has rank six.

The reference curvature contrast is

\[
z(0,XX)-2z(2,XX)+z(4,XX)=8c.
\]

It vanishes for affine drift and detects the hostile \(g(t)=t(t-4)\), for which
it equals eight. The full six-record schedule recovers the quadratic drift and
finds zero setting offsets in that hostile.

## Exact meaning of the added record

The third reference anchor adds one independently observable drift coordinate.
It does not “prove drift is controlled.” It distinguishes affine drift from one
quadratic extension and makes that extension identifiable.

For a polynomial common drift of degree \(d\), at least \(d+1\) reference
samples at distinct times are required to identify its coefficients before
three independent setting offsets can be separated. The total direct-record
count is therefore at least \(d+4\) under this design family.

Arbitrary drift is infinite-dimensional. No finite anchor schedule identifies
it without a bandwidth, smoothness, bounded-rate, stochastic, or state-space
assumption.

## Bounded-error curvature test

With reference intervals \(Z_0,Z_2,Z_4\), propagate their interval combination

\[
Z_0-2Z_2+Z_4.
\]

If zero is excluded, the affine model is falsified. If zero remains included,
the packet bounds curvature only at the declared resolution. When a quadratic
model is retained, divide the contrast interval by eight to obtain the
reachable coefficient set for \(c\).

## Schedule design beyond curvature

Different additional repetitions expose different defects:

- equally spaced reference repeats expose polynomial curvature;
- reversing the setting order exposes hysteresis;
- immediate repeats expose switching transients;
- randomized ordering weakens deterministic correlation between setting and
  slow drift;
- continuous monitoring supplies a higher-bandwidth nuisance-state observer.

These are not interchangeable redundancy. Each creates observability in a
different nuisance direction.

## Marici consequence

Experiment completion is relative to a disturbance model. Adding a record is
meaningful when it increases rank against a named model extension. “More
calibration” without a declared hostile direction has no precise completion
content.

## Verification boundary

The dependency-free checker computes rank five for the endpoint schedule under
the six-parameter quadratic model, constructs the exact curvature/setting
alias, computes rank six for the three-reference schedule, verifies the second
difference, and recovers the quadratic coefficients and zero offsets.

The theorem is finite and exact for quadratic common drift with constant
setting offsets. It does not cover arbitrary drift, hysteresis, or detector
dead time.

