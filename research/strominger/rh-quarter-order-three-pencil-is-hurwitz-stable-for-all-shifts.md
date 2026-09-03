# Quarter order-three pencil is Hurwitz stable for all shifts

## Question

Does the order-three continuous pencil theorem extend from fixed offsets to every nonnegative shift?

## Claim boundary

The promotion applies to source order three. It does not establish stability of the order-four pencil or an all-order condensation theorem.

## Disposition

The recurrence is translation covariant:

\[
D_n(a;s)=D_n(a+s;0).
\]

This follows algebraically by induction because every occurrence of \(q\) and every recursive shift depends only on \(a+s\). Both terms of the order-three condensation pencil inherit the same covariance. Therefore the roots at shift \(s\) are the roots at shift zero translated by \(-s\). Combining this identity with the continuous shift-zero Bernstein certificate proves that the order-three pencil is Hurwitz stable for every real \(s\geq0\) and \(t\in[0,1]\). Exact coefficient checks verify 63 source cases and nine pencil shifts. The next leaf is `quarter-order-four-hurwitz-bernstein-certificate`; shift covariance reduces it to the zero-shift continuous pencil.
