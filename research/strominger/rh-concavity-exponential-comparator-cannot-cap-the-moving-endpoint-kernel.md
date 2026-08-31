# The concavity exponential comparator cannot cap the moving endpoint kernel

## Question

Can concavity of the shifted Weibull exponent provide the missing uniform endpoint-kernel bound?

Put \(X=\log q\), \(y\geq0\), and

\[
v_X(y)=\exp\{-2a[(X+y)^\beta-X^\beta]\},\qquad0<\beta<1.
\]

Concavity gives

\[
(X+y)^\beta-X^\beta\leq \beta X^{\beta-1}y,
\]

hence

\[
v_X(y)\geq e^{-\lambda_Xy},
\qquad \lambda_X=2a\beta X^{\beta-1}.
\]

Thus the shifted Weibull norm dominates the exponential Laguerre norm. This is the correct direction for attempting to bound evaluation by a smaller norm.

## Obstruction

Endpoint evaluation is not bounded on the polynomial closure in
\(L^2(e^{-\lambda y}dy)\). For the degree-\(K\) Laguerre kernel,

\[
K_K^{(\lambda)}(0,0)=\lambda(K+1),
\]

which diverges with \(K\). Therefore the norm comparison yields only an infinite endpoint cap. Moreover \(\lambda_X\to0\) as \(X\to\infty\); this does not repair the divergence in degree.

The calculation separates the two limits: for each fixed \(K\),

\[
q^{-1}K_K^{(\lambda_X)}(0,0)
=\frac{2a\beta(K+1)}{q(\log q)^{1-\beta}}
\longrightarrow0,
\]

but the supremum over \(K\) is infinite for every fixed \(q\).

## Disposition

Reject the tangent-exponential comparison as a uniform-degree endpoint cap. It explains the observed fixed-degree decay but cannot justify interchange of the tail-start and degree limits. A successful bound must retain the subexponential Weibull tail responsible for indeterminacy, for example through a quantitative Nevanlinna or orthogonal-kernel estimate.

## Claim boundary

This no-go applies to the concavity-derived exponential lower comparator. It does not show that the moving Weibull endpoint kernel fails to decay after multiplication by \(q^{-1}e^{-2aX^\beta}\).
