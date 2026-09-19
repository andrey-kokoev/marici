# The half-density prime row is Holder below one half and gives a trace-norm continuous spectral density

On the Fourier side of the translation generator, the labelled incidence row
has the form

\[
\beta_{p,k}(\xi)
=a_{p,k}e^{i\xi L_{p,k}}\widehat c_k(\xi),
\qquad
a_{p,k}=k^{-1}p^{-k/2},\quad L_{p,k}=k\log p,
\]

up to the already retained finite endpoint orientation matrix.  The base cut
profiles have bounded Fourier transforms; their completed-theta decay also
gives the local regularity needed below.

Use the seam-weighted source norm, whose normalized prime basis contributes a
factor `(log p)^(-1/2)`.  Then

\[
\|\beta(\xi)\|_{U^*}^2
\lesssim
\sum_{p,k}\frac{p^{-k}}{k^2\log p}<\infty.
\]

For `0<alpha<1/2`, the elementary phase estimate

\[
|e^{i\xi L}-e^{i\eta L}|
\le C_\alpha|\xi-\eta|^\alpha L^\alpha
\]

gives, for the primitive grade,

\[
\sum_p\frac{p^{-1}(\log p)^{2\alpha}}{\log p}
=
\sum_p\frac{(\log p)^{2\alpha-1}}p<\infty.
\]

The last convergence follows from the prime-density comparison with
`integral du/u^(2-2alpha)`. Higher grades converge more strongly. Hence the
row `beta(xi):U->C` is locally Holder continuous of every order
`alpha<1/2`.

The sandwiched spectral density is the rank-one trace-class operator

\[
G(\xi)=\beta(\xi)^*\beta(\xi).
\]

The ideal estimate

\[
\|G(\xi)-G(\eta)\|_1
\le
(\|\beta(\xi)\|+\|\beta(\eta)\|)
\|\beta(\xi)-\beta(\eta)\|
\]

therefore makes `G` trace-norm Holder continuous for every `alpha<1/2`.
Finite reciprocal/endpoint polarity only replaces rank one by fixed finite
rank and preserves the estimate.

This supplies the regularity hypothesis missing from the bare
Hilbert--Schmidt argument. Standard vector-valued Plemelj theory then gives
trace-norm principal-value boundary values locally at every real spectral
parameter where the displayed source chart applies. The remaining work is to
match normalization and signs with the declared Green boundary convention and
to propagate the result through the Euler inverse at seam points where that
inverse is admitted.
