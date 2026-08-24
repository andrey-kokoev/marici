# Directed compact rank-two certificate contract

## Target

With

\[
\mathcal N(H)=2H'H'''-3(H'')^2,
\]

certify

\[
\boxed{
\mathcal N(H)(x)>0
\qquad(1/4<x\le400).
}
\]

Together with the analytic far-ray theorem, this gives global rank-two
Schwarzian positivity on the outer ray.  It does not prove RH or all-rank
Loewner positivity.

## Fixed source object

Use only the completed fixed-contour transform

\[
C(x)=\int_0^\infty\Phi(u)\cosh(\sqrt x,u)\,du,
\]

with analytic differentiation of the kernel through the fifth \(x\)-jet.
No thimble decomposition, zero data, fitted spectral atoms, or moving contour
is admissible in the certificate.

## Predeclared finite cover

Let

\[
x_j=\frac14\exp\left(
\frac{j}{64}\log1600
\right),
\qquad 0\le j\le64.
\]

On every declared interval \([x_j,x_{j+1}]\), certify directed bounds

\[
\mathcal N(x_{j+1})\ge n_j>0,
\qquad
\sup_{x_j\le x\le x_{j+1}}|\mathcal N'(x)|\le d_j,
\]

and check

\[
\boxed{
n_j-d_j(x_{j+1}-x_j)>0.
}
\]

No adaptive repartition after inspecting a failed sign is allowed.  A failed
box may be subdivided only under a predeclared uniform refinement rule.

## Reconnaissance margin

A 64-box fixed-contour scan uses the hostile provisional envelope

\[
d_j=2\max\bigl(
|\mathcal N'(x_j)|,
|\mathcal N'(x_{j+1})|
\bigr).
\]

Every box passes.  The weakest is approximately

\[
[356.44754,400],
\]

where the provisional directed lower margin is

\[
1.3541\times10^{-10}>0.
\]

The smallest relative box margin is approximately \(0.3341\).  Independent
2,000-step and 4,000-step Simpson evaluations on all 65 endpoints disagree by
at most

\[
2.2\times10^{-12}
\]

relatively for \(\mathcal N\), and

\[
1.5\times10^{-11}
\]

relatively for \(\mathcal N'\).  These figures demonstrate conditioning only;
they are not outward-rounded error bounds.

## Required directed enclosures

For each endpoint and box, the final certificate must include:

1. the omitted theta-label tail \(n>N\), bounded uniformly in \(u\);
2. the contour tail \(u>U\), bounded uniformly in the box and through the
   fifth \(x\)-jet;
3. outward-rounded quadrature enclosures on \([0,U]\);
4. interval propagation from the enclosed \(C,C',\ldots,C^{(5)}\) to
   \(H',\ldots,H^{(4)}\), \(\mathcal N\), and \(\mathcal N'\); and
5. proof that the interval enclosure of \(|\mathcal N'|\) lies below the
   declared factor-two envelope.

The completed source is positive and superexponentially decaying, so both
tails admit elementary exponential majorants.  The difficulty is preserving
correlations among the logarithmic derivatives when forming the small
Schwarzian numerator; evaluating each quotient jet as an unrelated wide
interval is inadmissible if it destroys the sign.

## Sharp falsifiers

The proposed certificate fails if any one of the following occurs:

1. an outward-rounded endpoint enclosure contains a nonpositive value of
   \(\mathcal N\);
2. a certified derivative supremum exceeds its factor-two envelope;
3. a declared box has nonpositive final lower margin; or
4. the first box fails to retain strict positivity immediately to the right
   of the regular boundary value at \(x=1/4\).

Such a failure does not prove \(\mathcal N<0\); it falsifies this particular
64-box certificate geometry and must be reported before refinement.

## Weakest-endpoint interval prototype

A dependency-free decimal interval prototype was applied first at \(x=400\).
The initial cellwise range/Riemann method failed: it widened the source jets
by roughly \(2.5\%\) and produced a Schwarzian interval spanning both signs.
This is a useful mechanism falsifier.  Correlations among the transform jets
must be retained by the quadrature rule; brute interval ranges are too lossy.

A correlated composite-Simpson evaluation was then upgraded from empirical
resolution inflation to a formal fourth-order interval-jet Peano remainder.
It includes outward-rounded decimal arithmetic, explicit theta-label and
contour tails, and a terminal geometric bound for the differentiated kernel
series.  The resulting enclosure is

\[
\mathcal N(400)\in
[4.05287401383748,4.05298120716449]\times10^{-10}>0,
\]

and

\[
\mathcal N'(400)\in
[-2.20696083331164,-2.20595281377019]\times10^{-12}<0.
\]

The formal contour-tail bounds through the fifth jet range from approximately
\(1.55\times10^{-54}\) to \(1.59\times10^{-51}\).  With eight explicit theta
labels, the omitted-label bounds are below \(3.73\times10^{-88}\).  Both fit
comfortably inside the declared \(10^{-30}\) tail allowance.  The formal
Simpson remainders range from approximately \(3.09\times10^{-8}\) for \(C\)
to \(9.29\times10^{-17}\) for \(C^{(5)}\), and their correlated propagation
retains both required signs.

Therefore

\[
\boxed{x=400\text{ is directed-certified}.}
\]

The same formal computation at 2,000 rather than 4,000 Simpson panels also
retains the signs,

\[
\mathcal N(400)\in
[4.05124562922238,4.05460959172604]\times10^{-10},
\]

\[
\mathcal N'(400)\in
[-2.22227395593509,-2.19063969058180]\times10^{-12}.
\]

Resolution probes show that the cost can fall rapidly toward the interior.
The following point enclosures are all formal and strictly positive:

| (x) | panels | enclosure for \(\mathcal N(x)\) |
|---:|---:|---:|
| (100) | 1,000 | \([4.6969241,4.6982857]\times10^{-9}\) |
| (25) | 500 | \([1.4521441,1.4531596]\times10^{-8}\) |
| (6.25) | 250 | \([2.0577832,2.0739277]\times10^{-8}\) |
| (1.5625) | 126 | \([2.0630281,2.4747279]\times10^{-8}\) |
| (0.390625) | 256 | \([2.3182390,2.3289323]\times10^{-8}\) |
| (0.25) | 512 | \([2.3300912,2.3304324]\times10^{-8}\) |

Every listed enclosure also gives \(\mathcal N'(x)<0\).  A deliberately
under-resolved 64-panel run at (x=0.390625) spanned both signs; 256 panels
resolved it.  Thus a globally scale-proportional panel rule is falsified near
the regular boundary, but no boundary collar is required: the closure value
at (x=1/4) itself is directed-certified and positive.

The compact interval is not yet certified.  The same directed engine must be
extended to the remaining grid endpoints and, more importantly, must enclose
the derivative supremum on every declared box.  Endpoint positivity is no
longer the conceptual bottleneck.  The live target is a box-valued source-jet
calculus retaining the correlations needed to certify
\(\sup_I|\mathcal N'|\) (or a stronger monotonicity/convexity substitute).

## Direct interval-x falsifier

The first box-valued implementation retained (x) as one outward interval in
every positive coefficient of the kernel series and propagated the resulting
source jets through the logarithmic quotients.  On the hostile terminal box

\[
I=[356.44753572825886,400]
\]

it produced

\[
\mathcal N(I)\subset[-0.00606881,0.00566774],
\qquad
\mathcal N'(I)\subset[-0.00097150,0.00101268].
\]

The endpoint signal is only of order (10^{-10}).  Thus raw interval-x
propagation loses roughly seven orders of magnitude through repeated-variable
dependency.  Quadrature refinement cannot repair this failure, because its
dominant width is induced by forgetting that every quotient jet is derived
from the same (x) and the same completed theta source.

This falsifies the direct interval-box mechanism, not compact positivity.  It
also identifies the required replacement: for each box (I=[c-r,c+r]), keep
\(\delta=x-c\) as a single formal variable, compute certified Taylor models
for (C^{(m)}(c+\delta)), form the logarithmic jets and \(\mathcal N\) in the
truncated polynomial algebra, and interval-evaluate only the final polynomial
plus its remainder.  A degree-(d) model for \(\mathcal N'\) requires theta
source derivatives through at least (C^{(5+d+1)}): five for the displayed
formula, (d) Taylor coefficients, and one derivative for the remainder.
The positive kernel series makes the last derivative's box supremum available
at the right endpoint.

## First correlated whole-box certificate

A centered Taylor-model algebra was implemented with interval polynomial
coefficients and a uniform remainder.  Multiplication explicitly encloses all
discarded powers.  Reciprocals are certified by the residual identity

\[
P^{-1}-Q=\frac{1-PQ}{P},
\]

so the logarithmic-jet divisions do not rely on an unchecked formal-series
truncation.  Degree (d) source models use directed center jets through the
required order and bound their Taylor remainder by the positive next kernel
derivative at the right endpoint.

On the hostile terminal box, degree six and 1,000 Simpson panels give

\[
\boxed{
\mathcal N([356.44753572825886,400])
\subset
[2.51602679526341,6.63450903641395]\times10^{-10}>0.
}
\]

The simultaneous enclosure of \(\mathcal N'\) still spans zero,

\[
\mathcal N'(I)\subset
[-1.69013,1.16917]\times10^{-11},
\]

but it is unnecessary here because \(\mathcal N\) itself is certified on the
entire box.  This is the first directed whole-box component of the compact
certificate.  It also demonstrates quantitatively that preserving the single
shared source displacement recovers more than seven orders of cancellation
lost by raw interval quotients.

The same architecture also closes the opposite conditioning regime.  On the
first boundary box, degree four and 500 panels give

\[
\boxed{
\mathcal N([0.25,0.2805461953768028])
\subset
[2.32858311263112,2.33048792501745]\times10^{-8}>0,
}
\]

and additionally

\[
\mathcal N'(I)
\subset[-4.75913151170404,-4.74939477680577]\times10^{-10}<0.
\]

Thus the correlated model works at both extremes of the compact bridge: the
regular completed boundary and the weakest far box.  The remaining finite
task is an adaptive sweep of the 62 intervening boxes, beginning at degree
four/500 panels and escalating only when the emitted polynomial or quadrature
remainder fails to preserve positivity.

## Completed compact sweep

The adaptive sweep is complete.  All 64 declared logarithmic boxes have a
strictly positive directed enclosure.  The selected tiers were:

- degree two / 250 panels through box 47;
- degree four / 500 panels through box 57; and
- degree six / 1,000 panels for boxes 58--63.

The weakest directed lower bound occurs on terminal box 63:

\[
\mathcal N(I_{63})
\ge 2.5160267952633994\times10^{-10}>0.
\]

The floating logarithmic grid ends at (399.99999999999994).  A separately
audited, overlapping Decimal box certificate reaches exact (400), so the
union has no rounding gap.  The consolidated manifest verifies 64 unique
indices, exact adjacency of all declared grid endpoints, strict positivity of
every selected enclosure, overlap of the exact-(400) closure, and reports

```text
compact_interval_certified: true
rh_proved_or_disproved: false
```

Consequently the directed compact theorem is

\[
\boxed{\mathcal N(H)(x)>0\quad(1/4\le x\le400).}
\]

Combining it with the previously proved analytic far-ray theorem gives the
first universal coupled positivity theorem of this lane:

\[
\boxed{\mathcal N(H)(x)>0\quad\text{for every }x\ge1/4.}
\]

This is not a proof of RH.  The remaining logical work is to prove that this
global rank-two positivity yields the required order-two Stieltjes/operator
representation with support in \([1/4,\infty)\), while auditing continuation,
multiplicities, and possible polynomial or boundary contributions.

## Artifacts

- checkers/theta_outer_schwarzian_scan.py
- results/theta-outer-schwarzian-scan.json
- checkers/theta_compact_endpoint_decimal_interval.py
- checkers/theta_compact_box_decimal_interval.py
- checkers/theta_compact_box_taylor_interval.py
- results/theta-compact-endpoint-decimal-interval.json
- results/theta-compact-endpoints/
- results/theta-compact-boxes/
- checkers/theta_compact_box_taylor_sweep.py
- checkers/theta_compact_box_taylor_audit.py
- results/theta-compact-box-taylor-manifest.json
