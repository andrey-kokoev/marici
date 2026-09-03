# Quarter order-five pencil is Hurwitz stable for all shifts

## Question

Does exact Hurwitz-minor interpolation scale from pencil degree 22 to degree 40?

## Claim boundary

The theorem covers source order five and all nonnegative shifts through translation covariance. It does not establish order six or an all-order closure theorem.

## Disposition

All 40 principal Hurwitz minors were reconstructed exactly from degree-bounded rational evaluations. Every interpolated polynomial has strictly positive Bernstein coefficients; no zero coefficients occur. The degree-dropped endpoint is Hurwitz stable. Therefore the complete order-five pencil is Hurwitz stable for every \(t\in[0,1]\), and shift covariance promotes the result to every real \(s\geq0\). The run completes in 37 seconds. The next leaf is `quarter-order-six-batched-hurwitz-interpolation`, replacing separate determinant evaluations by a common parameter grid and numeric Routh products so all degree-64 minors can be reconstructed in one batch.
