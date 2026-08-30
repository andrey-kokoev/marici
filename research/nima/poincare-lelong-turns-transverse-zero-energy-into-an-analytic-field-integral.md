# Poincaré–Lelong turns transverse zero energy into an analytic field integral

Event 10283 defined the continuous divisor energy

\[
E_\eta
=
\sum_\rho
m_\rho
\left(\Re\rho-\frac12\right)^2
e^{-\eta(\Im\rho)^2}.
\]

This still refers explicitly to zero states. Poincaré–Lelong gives a
pre-spectral analytic representation.

Let \(\Xi(s)\) be the entire completed zeta function and write
\(s=\sigma+it\). Distributionally,

\[
\Delta_{\sigma,t}\log|\Xi(s)|
=
2\pi
\sum_\rho m_\rho\delta_\rho.
\]

Choose a smooth strip cutoff \(\chi\) satisfying

\[
\chi(\sigma)>0
\quad(0<\sigma<1),
\]

and vanishing to all orders at \(\sigma=0,1\). A canonical example is

\[
\chi(\sigma)
=
\begin{cases}
\exp[-1/(\sigma(1-\sigma))],&0<\sigma<1,\\
0,&\text{otherwise}.
\end{cases}
\]

Define

\[
w_\eta(\sigma,t)
=
\left(\sigma-\frac12\right)^2
\chi(\sigma)e^{-\eta t^2}.
\]

Then

\[
E_{\eta,\chi}
=
\sum_\rho m_\rho w_\eta(\rho)
\]

is finite, nonnegative, and

\[
E_{\eta,\chi}=0
\quad\Longleftrightarrow\quad
\Re\rho=\frac12
\ \text{for every nontrivial zero}.
\]

Because the cutoff is flat at the strip boundary and the Gaussian controls
height, distributional integration by parts yields

\[
E_{\eta,\chi}
=
\frac1{2\pi}
\int_{\mathbb R^2}
\log|\Xi(\sigma+it)|
\,
\Delta w_\eta(\sigma,t)
\,d\sigma\,dt.
\]

Thus the continuous RH witness can be computed from the analytic potential
\(\log|\Xi|\) without first labeling individual zeros.

## What this does and does not solve

This identity removes the hard seam/off-seam classification from the
definition of the witness. It also makes continuity under zero motion
automatic.

But positivity is not manifest on the field-integral side because
\(\Delta w_\eta\) changes sign. Positivity follows from the divisor identity.
Therefore this is not yet a noncircular Green explanation of RH.

The remaining constructor theorem must factor the analytic field integral as
a source-positive quadratic form before invoking its zero expansion. In
schematic form,

\[
\frac1{2\pi}
\int\log|\Xi|\,\Delta w
\stackrel{?}{=}
\|N_\perp\Psi_w\|^2.
\]

Such a factorization would turn Poincaré–Lelong equality into the desired
operator-energy theorem.

## Arithmetic interface

The explicit formula can transport the same test weight to prime and
archimedean data. However, the test entering the explicit formula is not
\(w_\eta\) directly; it is the corresponding two-dimensional
Laplacian/Green transform. The source comparison must preserve that transform
and its strip cutoff.

The next executable square is therefore

\[
\text{prime plus gamma packet}
\to
\log|\Xi|
\to
\Delta\log|\Xi|
\to
E_{\eta,\chi},
\]

compared with a direct Green-energy construction from the same source weight.

This gives a precise target for the spectral-identification theorem while
keeping the positivity obligation separate and noncircular.
