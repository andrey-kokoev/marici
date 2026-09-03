# A naive two-region Weibull split does not cap endpoint evaluation

## Question

Can the moving endpoint kernel be bounded by splitting the translated Weibull norm into a local Laguerre window and a far subexponential tail?

For a cut \(Y>0\), write

\[
Q_X(p)=Q_{X,[0,Y]}(p)+Q_{X,[Y,\infty)}(p).
\]

Both terms are positive, but positivity alone does not turn either term into a quantitative endpoint bound.

## Local region

On \([0,Y]\), the shifted Weibull weight is continuous and bounded above and below by positive constants. Polynomial endpoint evaluation is unbounded in this \(L^2\) norm. One explicit witness is

\[
p_K(y)=(1-y/Y)^K.
\]

It satisfies \(p_K(0)=1\), while

\[
\int_0^Y |p_K(y)|^2dy=\frac{Y}{2K+1}\longrightarrow0.
\]

Weight equivalence on the compact interval preserves this conclusion. The local window alone therefore has infinite endpoint-kernel norm.

## Far region

The far term retains the subexponential Weibull tail, but its support begins at \(Y\), whereas the evaluation point remains \(0\). After translating the far support back to its endpoint, the requested quantity becomes an exterior-evaluation kernel, not the endpoint kernel already studied. Positivity supplies

\[
Q_X(p)\geq Q_{X,[Y,\infty)}(p),
\]

but using this inequality requires a quantitative bound for that exterior evaluation. No current artifact supplies it.

## Disposition

Reject the naive two-region argument that bounds the local and far pieces independently. The local piece is determinate and has unbounded endpoint evaluation; the far piece replaces the original unknown by an uncomputed exterior kernel. A successful split must include a coupling estimate—such as an orthogonal-polynomial transfer or Nevanlinna matrix relation—between the two regions.

## Claim boundary

This does not rule out all two-region estimates. It rules out the positivity-only decomposition and identifies the missing cross-region constructor.
