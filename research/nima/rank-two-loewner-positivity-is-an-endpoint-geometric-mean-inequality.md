# Rank-two Loewner positivity is an endpoint-geometric-mean inequality

The first nontrivial Gram gate admits an exact scalar form.

Let the mixed response be decreasing on a real zero-free interval and set

\[
q(x)=-R'(x)>0.
\]

Use the positive divided-difference kernel

\[
L_R(x,y)=\frac{R(x)-R(y)}{y-x},
\qquad
L_R(x,x)=q(x).
\]

For two points \(x<y\), positivity of the \(2\times2\) Loewner matrix is
equivalent to

\[
q(x)q(y)
\ge
\left(
\frac{1}{y-x}\int_x^y q(t)\,dt
\right)^2.
\]

Thus the mean response density on an interval may not exceed the geometric
mean of its endpoint response densities:

\[
\frac{1}{y-x}\int_x^y q(t)\,dt
\le
\sqrt{q(x)q(y)}.
\]

This is much stronger than monotonicity of \(R\), positivity of \(q\), or
ordinary log-convexity. It is the exact rank-two source target.

The confluent local limit gives a useful curvature law. Expanding at
\(y=x+h\), the determinant condition begins with

\[
2q q''-3(q')^2\ge0.
\]

Equivalently,

\[
\left(q^{-1/2}\right)''\le0.
\]

So reciprocal square-root concavity of the response density is the local
rank-two shadow. It is necessary, but by itself need not establish the
two-point integral inequality across a whole interval.

For a source-derived proof, one should not differentiate the scalar Xi
response and verify the inequality retrospectively. The desired Green
factorization must identify source vectors \(r_x,r_y\) satisfying

\[
q(x)=\|r_x\|^2,
\qquad
\frac{1}{y-x}\int_x^yq(t)\,dt
=
\langle r_x,r_y\rangle.
\]

Then Cauchy--Schwarz proves the rank-two gate with the correct equality
classification. This formula is considerably more rigid than assigning
arbitrary Cholesky vectors: the cross overlap is fixed as the interval average
of the diagonal energy.

The first source-native attack is therefore an endpoint transport theorem:

> Transport the theta Green state from \(x\) to \(y\) so that its endpoint
> overlap equals the average response energy along the parameter interval.

The transport must be Poisson-covariant and must carry the external boundary
ports. If it is unitary, the endpoint norms are fixed; if merely contractive,
the exact geometric-mean bound needs an additional comparison.

The sharp hostile has \(q>0\) and \(q^{-1/2}\) locally concave near each
tested point, but violates the finite-interval mean inequality. Another has
the scalar inequality but obtains the cross term from fitted Cholesky data
rather than source transport.

This identifies the first executable constructor more precisely: not an
arbitrary rank-two Gram, but a Green parallel transport whose cross matrix
coefficient is the interval-averaged response density.
