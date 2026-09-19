# The labelled completed-theta summands have an exact entire jet connection

For label `n>=1`, put

\[
X_n(x)=\pi n^2e^{2x},\qquad
h_{n,k}(x)=e^{x/2}X_n(x)^ke^{-X_n(x)}.
\]

Then

\[
\partial_xh_{n,k}
=\left(\frac12+2k\right)h_{n,k}-2h_{n,k+1}.
\]

The exponential generating section is

\[
H_{n,x}(t)=\sum_{k\ge0}h_{n,k}(x)\frac{t^k}{k!}
=e^{x/2}\exp(X_n(x)(t-1)).
\]

It is entire in `t` and satisfies

\[
\partial_xH_n
=\frac12H_n+2(t-1)\partial_tH_n.
\]

The physical completed-theta summand is recovered without fitting:

\[
\Phi_n(x)
=e^{x/2}e^{-X_n}(4X_n^2-6X_n)
=\left.(4\partial_t^2-6\partial_t)H_{n,x}(t)\right|_{t=0}.
\]

More generally,

\[
\Phi_{n,x}(t)
=(4\partial_t^2-6\partial_t)H_{n,x}(t)
=e^{x/2}e^{X_n(t-1)}(4X_n^2-6X_n)
\]

packages every multiplicative `X_n` jet of the labelled source.

For every compact `x` interval and every strict disc `|t|<=r<1`, the sum over
`n` and all `x` and `t` derivatives converges normally: its terms are bounded
by a polynomial in `n` times `exp(-c n^2)`, with `c>0` uniform on that compact.
Hence

\[
\Phi_x(t)=\sum_{n\ge1}\Phi_{n,x}(t)
\]

is holomorphic in `t` and smooth in `x` locally, and obeys the induced
connection obtained by commuting `4 partial_t^2-6 partial_t` with the displayed
first-order operator.

This proves the labelled recurrence and compact-local normal convergence. It
does not yet prove uniform whole-line `H1_x` bounds as `x -> -infinity`.
Termwise Gaussian estimates degenerate there; the required bound must use the
Poisson/modular cancellation of the completed sum. Consequently this packet
does not yet construct the global history-valued jet graph or the prime
incidence columns.
