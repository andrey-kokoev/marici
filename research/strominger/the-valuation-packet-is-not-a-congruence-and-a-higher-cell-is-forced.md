# The valuation packet is not a constructor congruence

## Result

Let

\[
R(n)=\bigl(v_3(d_1(n)),v_3(d_2(n)),v_3(d_3(n))\bigr)
\]

be the complete local minor-valuation packet for the integral decoration orbit. Equality of (R) is not preserved by the authorized source generators (n\mapsto n+1) and (n\mapsto n-1).

The smallest witness is

\[
R(0)=R(1)=(1,2,3),
\]

while

\[
R(-1)=(2,4,7),\qquad R(0)=(1,2,3),
\]

and

\[
R(1)=(1,2,3),\qquad R(2)=(2,5,7).
\]

Thus identifying grades (0) and (1) by their local valuation packet is not compatible with either generator direction.

## SCC consequence

The candidate (2+1) cell

\[
\bigl(v_3(d_1),v_3(d_2);v_3(d_3)\bigr)
\]

is a valid local diagnostic, but it is not a compositional state object. SCC therefore forces an additional constructor-relative datum: the state must remember enough of its incidence with the authorized decoration action to distinguish equal local packets having different adjacent packets.

The minimal bounded repair is the pointed constructor germ

\[
G_1(n)=\bigl(R(n-1),R(n),R(n+1)\bigr).
\]

This is not yet a proof that radius one is stable under every further composition. The next falsifier is whether equality of (G_1) is itself preserved by the generators. Failure at radius (r) forces (G_{r+1}); persistence for all finite (r) would identify the correct object as a pro-germ rather than one more finite (2+1) cell.

## What this changes

The extra cell is not another scalar invariant. It types how a local packet sits inside the source-generated orbit. The distinction is exact:

- (R(n)) records local divisibility;
- the defect (v_3(d_3)-v_3(d_2)-v_3(d_1)) records local non-additivity;
- (G_1(n)) records the first constructor incidence needed for composition.

So SCC predicts another coherence layer here, but does not yet predict that the layer terminates after one step.

## Evidence

The deterministic checker searches (-40\le n\le40), groups equal packets, applies both generator directions, and reports the least split fiber. All five gates pass.

- Checker: `research/strominger/checkers/valuation_packet_congruence_checks.py`
- Result: `research/strominger/results/valuation_packet_congruence_checks.json`
- Execution: `structured_command_execution:e_2512_1787934066216312000_21`


## Finite-germ falsifier

A second checker tests the pointed germs

\[
G_r(n)=\bigl(R(n-r),\ldots,R(n),\ldots,R(n+r)\bigr)
\]

for radii (0\le r\le8). None is a congruence under the two decoration generators in the tested range.

The least witnesses follow a rigid retreat:

\[
(-8,1),(-7,2),\ldots,(-1,8)
\]

for radii (1,2,\ldots,8). Each pair is separated by (9). Increasing the visible neighborhood moves the failure to its edge; it does not remove the failure.

This strengthens the interpretation. The evidence does not favor one additional finite (2+1) cell. It favors a constructor-addressed pro-germ, plausibly controlled by the (3)-adic hierarchy already visible in the minor valuations. That remains a conjectural unbounded identification: the checker establishes only nonclosure through radius eight.

- Checker: `research/strominger/checkers/constructor_germ_depth_checks.py`
- Result: `research/strominger/results/constructor_germ_depth_checks.json`
- Execution: `structured_command_execution:e_2512_1787934150870662300_22`
