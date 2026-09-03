# Quarter condensation pencil is finitely Hurwitz stable

## Question

Does subtraction remain inside the Hurwitz-stable cone along the interpolation from the first product term to the exact condensation gap?

## Claim boundary

The test covers source orders two through six, shift offsets zero through two, and the nine rational parameters \(t=j/8\). It neither proves stability for every \(t\in[0,1]\) nor closes an all-order induction.

## Disposition

All 135 exact Routh arrays for

\[
P_t(a)=X(a)-tY(a),
\qquad t\in\{0,1/8,\ldots,1\},
\]

have strictly positive first columns. Thus no sampled member leaves the open Hurwitz cone, including both the product and condensation endpoints. This supports a proper-position relation between \(X\) and \(Y\), unlike coefficientwise positivity alone. The next leaf is `quarter-condensation-hurwitz-bernstein-certificate`, expressing Routh first-column numerators in the Bernstein basis on \([0,1]\) to seek a continuous-parameter positivity certificate at bounded order.
