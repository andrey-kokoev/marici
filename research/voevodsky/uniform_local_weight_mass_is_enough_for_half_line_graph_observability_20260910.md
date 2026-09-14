# Uniform local weight mass is enough for half-line graph observability

## Question

Can the pointwise tail lower bound on a bulk weight be weakened to a distributed thickness condition while retaining stable half-line observation?

## Claim boundary

Yes. A bounded weight whose squared modulus has a uniform positive integral on every interval of one fixed length makes derivative plus weighted bulk observation bounded below on \(H^1(0,\infty)\). Pointwise positivity is unnecessary. The condition is sufficient; no full necessity claim is made.

## Problem

The previous repair assumed

\[
|w(r)|\ge c
\]

beyond a finite cutoff. This excludes weights with recurrent zeros even when their nonzero regions are distributed densely enough to prevent broad invisible packets.

## Bold conjecture

Stable derivative-plus-weight observation requires the weight to be pointwise bounded away from zero outside a compact set.

## Named rivals

1. Uniform local \(L^2\) mass is sufficient.
2. Positive average only on an expanding sequence of intervals suffices.
3. Isolated or recurrent zeros are harmless when every fixed-scale window contains enough weight.
4. Boundary traces can compensate for arbitrarily large weight-free gaps.

## Thickness hypothesis

Let

\[
w\in L^\infty(0,\infty),
\qquad
\|w\|_\infty=M.
\]

Assume there exist \(\ell>0\) and \(\beta>0\) such that

\[
\int_I|w(r)|^2\,dr\ge\beta
\]

for every interval \(I\subset(0,\infty)\) of length \(\ell\).

This is a fixed-scale thickness condition. It permits zeros and oscillatory support.

## Local weighted Poincare lemma

For every interval \(I\) of length \(\ell\) and every \(f\in H^1(I)\),

\[
\|f\|_{L^2(I)}^2
\le
2\ell^2\|f'\|_{L^2(I)}^2
+
\frac{8M^2\ell^2}{\beta^2}
\|wf\|_{L^2(I)}^2.
\]

### Proof

Set

\[
a^2=\frac{\beta}{2\ell}
\]

and

\[
E=\{r\in I:|w(r)|\ge a\}.
\]

Since

\[
\int_I|w|^2
\le
a^2\ell+M^2|E|,
\]

the thickness hypothesis gives

\[
|E|\ge\frac{\beta}{2M^2}.
\]

Choose \(y\in E\) such that

\[
|f(y)|^2
\le
|E|^{-1}\int_E|f|^2.
\]

On \(E\), \(|w|\ge a\), so

\[
|f(y)|^2
\le
\frac{4M^2\ell}{\beta^2}
\|wf\|_{L^2(I)}^2.
\]

For every \(x\in I\),

\[
|f(x)|^2
\le
2|f(y)|^2+2\ell\|f'\|_{L^2(I)}^2.
\]

Integrating over \(x\) yields the claim.

## Global stability theorem

Partition the half-line into intervals

\[
I_n=(n\ell,(n+1)\ell).
\]

Summing the local estimate gives

\[
\|f\|_{L^2(0,\infty)}^2
\le
C_{w,\ell,\beta}
\left(
\|f'\|_{L^2}^2+
\|wf\|_{L^2}^2
\right),
\]

where

\[
C_{w,\ell,\beta}
=
\max\left\{
2\ell^2,
\frac{8M^2\ell^2}{\beta^2}
\right\}.
\]

Therefore

\[
Q_wf=(f',wf)
\]

is bounded below from \(H^1(0,\infty)\) to \(L^2\oplus L^2\):

\[
\|Q_wf\|^2
\ge
\frac1{1+C_{w,\ell,\beta}}
\|f\|_{H^1}^2.
\]

No endpoint trace is needed under global thickness.

## Tail-thickness variant

If the thickness condition holds only on intervals contained in \((R,\infty)\), then add the endpoint trace. The bounded segment \((0,R)\) is controlled by

\[
\int_0^R|f|^2
\le
2R|f(0)|^2+R^2\|f'\|^2,
\]

while the local weighted estimates control the tail. Thus

\[
f\longmapsto(f',f(0),wf)
\]

is bounded below.

## Recurrent zeros are admissible

A periodic weight may vanish on subintervals and still satisfy the thickness hypothesis. For example, any nonzero bounded periodic weight with positive squared integral over one period has a uniform lower mass on intervals of a sufficiently enlarged fixed length.

Therefore rival 3 survives and the bold conjecture fails. Pointwise tail positivity is sufficient but not necessary.

## Large-gap obstruction

If there are weight-poor intervals whose lengths tend to infinity, the broad-packet construction may make both derivative and weighted norms tend to zero. Uniform local mass explicitly forbids such gaps.

Positive averages on only a sparse sequence of intervals do not control packets supported between them, rejecting rival 2.

No finite family of endpoint traces sees packets supported in remote gaps, rejecting rival 4.

## Reciprocal and Real compatibility

On the radial double define

\[
M_w^{\rm dbl}=\operatorname{diag}(M_w,M_w).
\]

For real-valued \(|w|\), or more generally with the target Real structure chosen compatibly,

\[
M_w^{\rm dbl}W_u=W_uM_w^{\rm dbl},
\qquad
M_w^{\rm dbl}J_u=J_uM_w^{\rm dbl}.
\]

The scalar local estimate applies to both parity sectors. Phase gauges also commute with the diagonal multiplier. Hence the stability bound descends through every enriched radial comparison.

## Constructor-role refinement

A `thick_bulk_complement` declares:

- graph-domain source;
- fixed observation scale \(\ell\);
- uniform local mass \(\beta\);
- multiplier bound \(M\);
- resulting graph lower bound;
- reciprocal, Real, and gauge covariance.

This is weaker than `pointwise_tail_complement` but stronger than `nonzero_bulk_weight`. The roles must not be merged because their acceptance tests differ.

## Strongest falsification attempt

Weights with dense zeros appear hostile to pointwise control. The local lemma shows that derivative energy transports information from the weighted subset to the rest of each fixed interval. The argument fails precisely when the weighted subset can disappear on intervals of unbounded length, matching the broad-packet obstruction.

## Disposition

Uniform local weight mass is enough for stable half-line graph observation. The derivative and weighted bulk channel form a complementary pair: the weight anchors each fixed-scale window, and the derivative controls variation within it. Endpoint data are needed only for an uncontrolled bounded initial segment, not for the essential tail margin.
