# Coordinatewise pivot monotonicity would close central rank five

Let `d_5(x_1,...,x_5)` be the fifth Newton--`LDL*` pivot of the normalized
rank-five Loewner matrix. The complete anchor audit places its minimum at the
fully confluent upper endpoint. A hostile midpoint-source sweep differentiated
all five coordinates at all 3003 nondecreasing `0.001`-grid anchors:

- derivative count: 15,015;
- positive derivatives: zero;
- all sampled finite-difference signs were negative;
- the reported extremal magnitudes are withdrawn: differentiating the
  interval `LDL*` recursion analytically at `(0.003,0.003,0.003,0.01,0.01)`
  gives coordinate intervals from about `-1.23e-27` to `-1.35e-28`, whereas
  the binary finite-difference probe had reported `-6.77e-29` there.

This suggests the local theorem

\[
 \partial_{x_j}d_5(x_1,\ldots,x_5)<0
 \quad(0\le x_1\le\cdots\le x_5\le0.01).
\]

If certified, coordinatewise monotonicity makes the already proved endpoint-
cell lower bound global on the ordered simplex, completing central rank five.

The sweep is numerical sign reconnaissance, not a sign proof or a reliable
extremum search: subtracting fifth pivots of order `10^-26` to recover changes
of order `10^-31` loses decisive binary digits. A first directed analytic
audit at `(0.003,0.003,0.003,0.01,0.01)` proves all five derivatives strictly
negative, with analytic source tails included. The next certificate should
apply that differentiated Newton--`LDL*` recursion to all anchors, then add a
centered Taylor remainder for each derivative.

That all-anchor analytic audit is now complete. Directed Decimal intervals,
including the Cauchy source tails, prove all 15,015 anchor-coordinate
derivatives strictly negative. The closest certified upper endpoint to zero is

\[
 -1.3533618853656590\,10^{-28},
\]

at the fully confluent anchor `(0.01,0.01,0.01,0.01,0.01)`, coordinate 3
(zero-based variable 2). The most negative lower endpoint is
`-1.2342190e-27`, at the fully confluent zero anchor, variable 5. Thus the
remaining gate is no longer an anchor-sign question: it is to prove that each
derivative moves by less than `1.35336e-28` between an anchor and every point
of its ordered half-grid cell. See
`results/central-rank-five-derivative-interval-grid.json`.

A first continuum-carrier stress test distinguishes mathematics from interval
loss. Differentiating the existing degree-five endpoint pivot jet and summing
absolute coefficient radii gives a derivative-variation budget near
`2.08e-28`, too large to preserve the sign. But all six ordered vertices of
the endpoint half-grid cell are directly interval-negative, and their closest
upper endpoints vary by only about `2.5e-33`. The box budget is therefore five
orders too pessimistic because it forgets ordered-node correlation and repeats
source-tail uncertainty coefficient by coefficient. The next carrier should
propagate the Hessian of the pivot directly (with one analytic-tail budget),
then use a mean-value bound on each ordered cell.

The shallow degree-29 version of that direct Hessian attack fails: its Cauchy
tail amplifies to row sums near `2.94e-22`. Extending the same directed Xi-log
construction from order 61 to 81 supplies `F` through degree 39 and repairs
the loss. At the fully confluent upper anchor the certified Hessian row sums
then range from `4.3175e-30` to `4.5561e-29`; their half-grid products range
from `2.1588e-33` to `2.2781e-32`, thousands of times below the derivative
margin. This is an anchor Hessian certificate, not a cell supremum. The next
gate is a directed enclosure of Hessian variation over the endpoint cell.

All six ordered endpoint-cell vertices have now been audited with the deeper
Hessian evaluator. Their maximum row sums range only from `4.556095e-29` to
`4.556191e-29`; the corresponding half-grid costs remain below
`2.278096e-32`. No vertex inflation is visible. A directed third-derivative
bound only needs to control the interior excess by roughly four orders less
than the available sign margin.

The correlated degree-five Taylor Hessian using the degree-39 source now
quantifies that interior stability. Hessian-row variation from Taylor degrees
3, 4, and 5 is at most `6.4271477454e-34`; degree three dominates, while the
next budgets fall to `6.02e-39` and `7.42e-43`. Thus the certified finite jet
changes the endpoint Hessian by only about one part in 70,000. The sole
endpoint-cell obligation is now the degree-six-and-higher Hessian remainder.

Extending the same directed jet through degree seven gives additional row
budgets `1.1395e-42` and `1.4252e-42`. Their slight rebound identifies the
coefficientwise analytic-tail uncertainty floor, not growth at a meaningful
scale; the cumulative variation remains `6.4271477711e-34`. The unresolved
remainder now begins at degree eight, but it must be bounded by aggregating the
analytic source tail once rather than summing infinitely repeated coefficient
boxes.

That aggregated all-orders `C^2` Taylor-model propagation now succeeds. The
degree-eight-and-higher fifth-pivot Hessian remainder is at most
`1.6707041856e-41`, including analytic source and rational reciprocal tails.
Combining the endpoint-anchor Hessian, the degree-3--7 correlated variation,
and this remainder keeps every half-cell derivative displacement below
`2.279e-32`, against the smallest directed derivative margin
`1.3533618854e-28`. Hence all five fifth-pivot coordinate derivatives are
strictly negative throughout `[0.0095,0.01]^5`. Endpoint-cell pivot
monotonicity is proved. Uniform transport over the other ordered cells remains.

A directed longitudinal audit at all eleven fully confluent grid anchors shows
no Hessian growth: the maximum row sum decreases smoothly from
`4.5580195455e-29` at zero to `4.5560947202e-29` at `0.01`, only `4.2e-4`
relative variation. This is strong evidence that the endpoint scale is global,
but mixed anchors remain the hostile cases and no global Hessian bound is yet
claimed.

The full distinct-node grid family is now directed-certified as well. All 462
distinct anchors complete, with hostile anchor `(0,0.001,0.002,0.003,0.004)`
and maximum Hessian row sum `4.5573544585e-29`, still below the fully
confluent zero value. Only mixed collision patterns remain in the discrete
Hessian audit.

Every anchor with at most two distinct grid values is now certified: 231
collision-heavy cases covering all multiplicity splits. Their hostile case is
the fully confluent zero anchor, with maximum Hessian row sum
`4.5580195455e-29`. Together with the 462 distinct anchors, 693 directed
Hessian anchors have been closed. The remaining discrete strata have exactly
three or four distinct node values.

All 990 exactly-three-value anchors now pass. Their hostile case is
`(0,0,0,0.001,0.002)` with maximum Hessian row sum
`4.5577067841e-29`, again below the fully confluent zero ceiling. Only the
1,320 exactly-four-value anchors remain in the discrete audit.

The exactly-four-value stratum now also closes: all 1,320 anchors pass, with
hostile anchor `(0,0,0.001,0.002,0.003)` and row sum
`4.5575360646e-29`. Therefore all 3003 nondecreasing grid anchors have directed
Hessian certificates. The global discrete maximum is
`4.5580195455e-29` at the fully confluent zero anchor. The sole remaining
monotonicity gate is a uniform between-anchor Hessian enclosure; no discrete
collision or separation pattern remains unaudited.

The final continuum target has generous quantitative slack. A half-grid cell
has coordinate `l1` radius at most `5(0.0005)=0.0025`. The smallest derivative
margin `1.3533618854e-28` therefore permits a uniform Hessian row-sum ceiling

\[
 1.3533618854\,10^{-28}/0.0025 > 5.4134\,10^{-26},
\]

about 1,188 times the complete anchor ceiling. It is enough to prove a global
third-derivative row bound below approximately `2.16e-23`, because transporting
the anchor Hessian across another `0.0025` would still remain under the allowed
ceiling. This deliberately coarse third-derivative majorant is now the smallest
remaining falsifier.

Natural interval Hessian propagation over the endpoint cell is now explicitly
falsified as a carrier: it produces maximum row sum `4.9184e-21`, five orders
above the permitted `5.4134e-26`, despite the true anchor scale `4.56e-29`.
Correlation-preserving Taylor models remain necessary.

The complete pivot audit now retains coordinatewise denominator minima. All
five Newton--`LDL*` pivots are minimized on the grid at the fully confluent
upper endpoint. The first four lower bounds are `9.2454e-2`, `3.3771e-7`,
`4.4596e-13`, and `2.1680e-19`. Thus the endpoint-centered rational model is
already centered at the worst discrete conditioning. The remaining global
majorant needs only a cellwise allowance proving these first four denominators
stay above safe fractions of those values between anchors.

The determinant quotient eliminates that last denominator-stability concern.
The whole-domain rank-three matrix enclosure gives
`Q_2 in [3.1217673843e-8,3.1234369675e-8]`. Combining directed lower bounds
for `Q_1,...,Q_4` with Hadamard upper bounds for preceding determinants proves
the continuum pivot floors

`d_1>9.2454e-2`, `d_2>3.3764e-7`, `d_3>2.5127e-13`, and
`d_4>4.3406e-21`.

Thus every local rational Taylor jet is globally well-typed without assuming
pivot monotonicity. A cancellation-free global `C^3` propagation was then
tested and rejected: repeated absolute-value division inflates the third norm
to `3.53e112`, versus target `2.16e-23`. Together with the natural-box failure,
this proves that the final carrier must be correlated cell-centered Taylor
algebra; purely absolute global norms cannot close rank five.

The first correlated `C^3` jets now restore the true scale. At the zero and
upper confluent anchors and the hostile three-/four-value Hessian anchors, the
full third-derivative tensor `l1` bounds lie in the narrow range
`1.80024e-30`--`1.80091e-30`, roughly twelve million times below the required
`2.16e-23`. Degree-four correlated jets on the two extreme cells add third-
tensor variation at most `3.29394e-35`. The next obligations are (i) an
all-orders degree-five-and-higher third-tensor remainder and (ii) uniformizing
the correlated center coefficients without an eight-hour naive anchor sweep.

Both obligations now close through a six-chart binary cover. Split every
coordinate interval into `[0,.005]` and `[.005,.01]`. Ordered points admit
only the six patterns consisting of `k` lower coordinates followed by `5-k`
upper coordinates. A correlated degree-seven Taylor model at each pattern's
midpoint, with radius `.0025`, therefore covers the entire ordered simplex.
The largest directed degree-five-and-higher third-tensor remainder is
`1.312984329805715e-29`; the largest full ordered third-tensor `l1` bound is
`1.493074357349845e-29 < 2.16e-23`.

Thus six correlated evaluations replace the 3,003-anchor naive sweep. The
failed one-chart radius-`.01` experiment is also informative: its reciprocals
remain typed, but its degree-eight tail inflates to `1.17397e-17`, so some
subdivision is essential for this carrier.

The final directed mean-value transports start from the complete anchor
Hessian maximum `4.558019545447019e-29`. The tensor cover adds at most
`3.732685893374612e-32` inside a half-grid cell, and the resulting derivative
displacement is at most `1.140438057835099e-31`, against the smallest anchor
margin `1.353361885365659e-28`. Consequently

\[
 \partial_{x_j}d_5(x_1,\ldots,x_5)<0
 \quad (j=1,\ldots,5;\ 0\le x_1\le\cdots\le x_5\le .01).
\]

The coordinate-monotonicity target is proved for the certified central source
model. See `results/central-rank-five-third-tensor-six-chart-cover.json` and
`results/central-rank-five-global-coordinate-monotonicity.json`.

RH is not proved.
