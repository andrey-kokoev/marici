# Quarter order-two condensation pencil is continuously Hurwitz stable

## Question

Can discrete pencil sampling be replaced by an exact certificate for every interpolation parameter?

## Claim boundary

The theorem covers source order two and shift offsets zero through four. It does not establish continuous pencil stability at higher source order or arbitrary shift.

## Disposition

For

\[
P_t(a)=q(a+s+1)-tq(a+s),
\qquad 0\leq t<1,
\]

every numerator and denominator in the symbolic Routh first column has a nonnegative Bernstein expansion in \(t\), with a positive coefficient. The degree-dropped \(t=1\) cubic is separately Hurwitz stable. Therefore the entire pencil is Hurwitz stable for every \(t\in[0,1]\) at each tested shift offset. This is the first continuous, rather than sampled, subtraction certificate. The next leaf is `quarter-order-two-hurwitz-two-parameter-certificate`, retaining the shift as a symbolic nonnegative variable to seek a theorem uniform in both shift and interpolation parameter.
