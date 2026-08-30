# The Cauchy quadratic breakdown has an explicit simple-pole residue at \(\Re s=1\)

The two-parameter Cauchy covariance identifies the singularity that a
theta-side replacement must absorb.

For \(\sigma,\tau>1/2\), define normalized Euler states

\[
Z_\sigma
=
\frac{1}{\zeta(1+\sigma)}
\sum_{n\ge1}n^{-1/2-\sigma}X_{\log n}.
\]

Their Gram kernel is

\[
G(\sigma,\tau)
=
\frac{1}{\zeta(1+\sigma)\zeta(1+\tau)}
\sum_{n,m\ge1}
\frac{
e^{-\frac12|\log(n/m)|}
}{
n^{1/2+\sigma}m^{1/2+\tau}
}.
\]

Split the sum into \(n\ge m\) and \(m\ge n\). Up to the diagonal correction,

\[
G(\sigma,\tau)
=
\frac{1}{\zeta(1+\sigma)\zeta(1+\tau)}
\left[
\sum_n n^{-1-\sigma}\sum_{m\le n}m^{-\tau}
+
\sum_m m^{-1-\tau}\sum_{n\le m}n^{-\sigma}
-\zeta(1+\sigma+\tau)
\right].
\]

For \(0<\sigma,\tau<1\),

\[
\sum_{m\le n}m^{-\tau}
=
\frac{n^{1-\tau}}{1-\tau}
+O(1+n^{-\tau}),
\]

and similarly in the other sector. Therefore the singular part as
\(\sigma+\tau\downarrow1\) is

\[
G_{\mathrm{sing}}(\sigma,\tau)
=
\frac{
\frac1{1-\tau}+\frac1{1-\sigma}
}{
\zeta(1+\sigma)\zeta(1+\tau)
}
\zeta(\sigma+\tau).
\]

On the diagonal \(\sigma=\tau\downarrow1/2\),

\[
G(\sigma,\sigma)
\sim
\frac{4}{
\zeta(3/2)^2
}
\frac1{2\sigma-1}.
\]

Thus the Hilbert breakdown at the Euler boundary is a genuine simple pole
with an explicit positive residue.

This pole must not be confused with the raw Mellin observer's logarithmic
seam divergence at \(\sigma\downarrow0\). They occur at different walls and
have different asymptotics:

\[
\text{Euler quadratic wall: }
\sigma\downarrow\frac12,
\quad
(2\sigma-1)^{-1};
\]

\[
\text{raw critical seam: }
\sigma\downarrow0,
\quad
\log(1/\sigma).
\]

The first is an interior representation boundary at \(\Re s=1\). The second
belongs to a downstream raw observer approaching the critical line.

The simple-pole coefficient is a necessary matching datum for any
theta/archimedean Schur replacement. A valid comparison must reproduce this
residue from an independently sourced boundary channel and continue only the
regular relative form. Subtracting the pole after scalar evaluation has no
constructor authority.

The next source audit should ask whether the completed theta five-cell has a
boundary Gram whose pullback to the Euler overlap has exactly

\[
\frac{4}{\zeta(3/2)^2}
\]

as its diagonal residue in the frozen Cauchy normalization. A mismatch in
coefficient, sign, or port rank falsifies that interface before any RH
positivity estimate.
