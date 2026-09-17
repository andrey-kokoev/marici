# Legendre--Sturm order aligns the certified block with the coercive complement

On `(-L,L)`, define the nonnegative Legendre operator by the closed form

\[
a_L(f)=\int_{-L}^L\left(1-\frac{x^2}{L^2}\right)|f'(x)|^2dx.
\]

Its normalized Legendre eigenfunctions have eigenvalues `n(n+1)/L^2`.
The Dirichlet Laplacian form satisfies

\[
\langle f,-\Delta_D f\rangle=\int|f'|^2\ge a_L(f).
\]

Operator monotonicity of the square root and logarithm gives

\[
\log(1+\sqrt{-\Delta_D})
\ge \log(1+\sqrt{A_L}).
\]

Therefore, on the orthogonal complement of Legendre degrees `0,...,N-1`,

\[
\log(1+\sqrt{-\Delta_D})
\ge
\log\left(1+\frac{\sqrt{N(N+1)}}L\right).
\]

This removes the earlier basis mismatch: a Legendre low block and its
Legendre orthogonal complement form a valid coercive decomposition. With the
current total order-zero constant

\[
C=2.6947343670010686+
\left(\frac\pi{\sqrt3}+\log2-\frac38\right)+
0.4504638081309234,
\]

the sufficient Legendre complement rank is the least `N` satisfying

\[
\frac12\log\left(1+\frac{\sqrt{N(N+1)}}L\right)>C.
\]

Endpoint and image terms are already included in the bounded remainder, so no
separate pure-tail endpoint representer is required for this coarse theorem.
The finite low block and its coupling still require a Schur certificate; the
point here is that they now use the same Legendre decomposition as the
existing rank-160 certificate.
