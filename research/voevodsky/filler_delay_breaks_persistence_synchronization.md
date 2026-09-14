# Filler delay breaks persistence synchronization

## Question

Is zero-length positive-dimensional persistence forced by the cubical incidence alone, or by the exact alignment of the Carrier grade with its filler cells?

## Claim boundary

This is a controlled counterfactual on the multiplicative-degree-two distinct-shell sector through original grade 20000. It changes filtration grades but not cells or boundary maps. The delayed filtration is not asserted to be source-derived or physical.

## Structural identity

For a cell \([D;I]\), write \(m=\max I\), \(D=k\prod_{i\in I}p_i\), and

\[
g[D;I]=k p_m\prod_{i\in I}p_{i+1}.
\]

If \(j\in I\) and \(j<m\), the upper \(j\)-face has base \(D p_{j+1}/p_j\) and satisfies

\[
g(\partial_j^+[D;I])=g[D;I].
\]

Thus every cell of dimension at least two arrives with at least one same-grade codimension-one face. This identity is the candidate synchronization mechanism.

## Intervention

Keep vertex and edge grades unchanged. Delay every square by one grade:

\[
g_{\mathrm{delay}}(c)=g(c)+1
\]

for \(\dim c=2\). Cell incidence and coefficients remain unchanged. This breaks the same-grade edge--square alignment without deleting a filler.

## Bold prediction

The 73 zero-length one-bars in the original degree-two scan become positive-length bars under the delayed filtration. If no other pairing rearrangement intervenes, each should have lifetime one.

## Rivals

1. Cubical incidence alone forces zero persistence despite delayed squares.
2. Pairing rearrangement produces a different number or distribution of positive bars.
3. The delayed grades violate face monotonicity and fail to define a filtration.

## Test

Recompute the entire degree-two persistence reduction over two prime fields using delayed square grades. Require every face grade to be at most its cell grade. Compare barcodes with the original filtration and record counts and lifetimes.

## Falsifier

No positive-length bar falsifies dependence on same-grade alignment. A face-monotonicity failure invalidates the intervention rather than supporting any prediction.

## Computed result

The intervention preserves face monotonicity. In the original filtration all 73 one-bars have lifetime zero. After delaying every square by one grade, the same census has exactly 73 positive-length bars, every one of lifetime one; none is zero-length or right-censored. Both fields agree.

## Disposition

The bold prediction survives exactly. Cubical incidence alone does not force zero persistence. Same-grade filler alignment is the mechanism suppressing positive bars in the Carrier filtration. A one-grade failure to preserve that alignment exposes every previously simultaneous route relation as a one-grade bar. This is a counterfactual filtration result, not evidence that any physical sector implements the delay.
