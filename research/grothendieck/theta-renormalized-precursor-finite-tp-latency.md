# Finite total-positivity latency of the renormalized precursor

## Hostile reconnaissance

For

\[
K(u)=\cosh(u/2)-\frac12e^{u/2}\Theta(e^{2u}),
\]

the first translation-kernel tests are unexpectedly clean.

On the grid

\[
\{-2,-1.5,\ldots,1.5,2\},
\]

binary64 reconnaissance found no resolved negative ordered minors of
\(K(x_i-y_j)\) through order four:

\[
\begin{array}{c|r}
\text{order}&\text{minors tested}\\ \hline
2&1296\\
3&7056\\
4&15876.
\end{array}
\]

A separate jet scan on \(0\le u\le4\) found \(K>0\) and

\[
KK''-(K')^2\le0
\]

at every sample. The apparent zero curvature in the far tail agrees with the
single exponential asymptotic.

These calculations are not interval-certified. Tiny negative determinants
were well inside a scale-aware floating-point cancellation threshold and are
not treated as sign failures.

## Why PF-infinity is nevertheless impossible

The finite pattern must not be extrapolated to a Pólya-frequency theorem of
all orders. In the open critical strip,

\[
Z(z)=\left(\frac14-z^2\right)F(z),
\qquad
F(z)=\int_{\mathbb R}e^{zu}K(u)\,du.
\]

At every established critical-line Xi zero \(z=i\gamma\), the polynomial
factor is nonzero, so

\[
F(i\gamma)=0.
\]

But the bilateral transform of a nondegenerate PF\(_\infty\) translation
kernel has the Schoenberg reciprocal-Laguerre--Pólya form. In particular, it
cannot have such Fourier-axis zeros in its strip of convergence. Therefore

\[
\boxed{K(x-y)\text{ is not PF}_{\infty}.}
\]

This conclusion uses only already established critical-line zeros, not RH.
One such zero suffices.

## Interpretation

The low-order minors exhibit **finite total-positivity latency**: the kernel
looks PF-like at small matrix orders and ordinary spacings, while its spectral
zeros force failure at some higher order or more hostile geometry.

This is another instance of finite-to-one not being one-to-one. Low-rank
variation diminution is a genuine property but cannot identify the global
spectral mechanism.

The correct positive object cannot be the raw translation kernel \(K(x-y)\).
It must allow the boundary zeros rather than forbid them. The angular
Herglotz current does exactly that: real \(w\)-axis zeros contribute positive
Poisson kernels, while upper-half-plane zeros are forbidden.

## Revised direction

Do not accumulate higher finite TP minors as evidence for PF\(_\infty\).
Instead seek a **centered resolvent or Loewner kernel** whose positive measure
may carry atoms at the allowed real \(w=-\gamma^2\) locations. Its positivity
should encode where zeros are permitted, rather than demanding that the
Fourier transform have no zeros at all.

That kernel is now explicit in denominator-free form; see
`theta-denominator-free-loewner-kernel.md`.

The finite-minor scan remains useful as a latency diagnostic: locating its
first robust failure may reveal the scale at which critical-line oscillation
enters the real-space precursor. It is not the leading proof path.

Artifacts:

- checkers/theta_renormalized_precursor_log_concavity.py
- results/theta-renormalized-precursor-log-concavity.json
- checkers/theta_renormalized_precursor_tp3.py
- results/theta-renormalized-precursor-tp3.json
