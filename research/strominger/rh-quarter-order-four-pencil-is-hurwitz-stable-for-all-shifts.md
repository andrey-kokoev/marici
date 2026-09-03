# Quarter order-four pencil is Hurwitz stable for all shifts

## Question

Can the blocked degree-22 symbolic Routh computation be replaced by a scalable exact certificate?

## Claim boundary

The theorem covers source order four and every \(t\in[0,1]\). Shift covariance promotes zero shift to all real \(s\geq0\). It does not establish order five or an all-order closure theorem.

## Disposition

A principal Hurwitz minor of order \(k\) is a polynomial in \(t\) of degree at most \(k\). Each of the 22 minors was therefore reconstructed exactly from \(k+1\) rational evaluations. Every resulting polynomial has nonnegative Bernstein coefficients on \([0,1]\), and the degree-dropped endpoint is Hurwitz stable. This proves the entire order-four pencil Hurwitz stable. Translation covariance extends the zero-shift result to every nonnegative shift. The interpolation method completes in under one second, replacing the timed-out recursive rational Routh representation. The next leaf is `quarter-order-five-interpolated-hurwitz-minors`, testing whether the same exact method scales to the degree-40 pencil.
