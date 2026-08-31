# Fixed-shell diagonal theta labels remain independent after radial codiagonalization

## Question

Can distinct diagonal theta labels sharing one shell endpoint cancel after the radial codiagonal?

## Claim boundary

No for every summable signed or complex diagonal-label packet on a fixed nontrivial shell. The exact incomplete-gamma kernel assigns label \(n\) the separation-tail scale

\[
\exp\left[-\pi n^2e^{2a}e^{2t}\right].
\]

The least active label decays slowest. A Gaussian-in-label majorant permits coefficient extraction through an infinite sum.

## Fixed-shell diagonal family

For one shell \([a,b]\), define

\[
\rho_{nn}^{[a,b]}(t)
=
\int_a^b\Phi_n(u)\Phi_n(u+t)\,du.
\]

In the exact multiplicative-coordinate formula,

\[
A=\pi n^2,
\qquad
C=\pi n^2e^{2t},
\qquad
\lambda=\pi n^2(1+e^{2t}).
\]

The lower incomplete-gamma endpoint asymptotic is controlled by \(Y_-=e^{2a}\). Consequently,

\[
\rho_{nn}^{[a,b]}(t)
=B_{n,a,b}(t)
\exp\left[-\pi n^2(1+e^{2t})e^{2a}\right]
\left(1+o(1)\right),
\]

where the explicit polynomial prefactor is nonzero for sufficiently large \(t\).

## Label ordering

If \(m>n\), then

\[
\frac{\rho_{mm}^{[a,b]}(t)}
{\rho_{nn}^{[a,b]}(t)}
=
\frac{B_{m,a,b}(t)}{B_{n,a,b}(t)}
\exp\left[
-\pi(m^2-n^2)(1+e^{2t})e^{2a}
\right]
\left(1+o(1)\right)
\longrightarrow0.
\]

Thus label order replaces endpoint order when the shell is fixed.

## Infinite coefficient extraction

Let \(d=(d_n)\) be any coefficient packet for which the labelled theta synthesis converges; projective exponential summability is more than sufficient. Suppose

\[
\sum_{n\ge1}d_n\rho_{nn}^{[a,b]}(t)=0.
\]

If \(d\ne0\), let \(n_0\) be its least active label. Divide by \(\rho_{n_0n_0}^{[a,b]}(t)\). For \(t\ge T\), the exact polynomial factors and endpoint difference give a bound

\[
\left|
\frac{\rho_{nn}^{[a,b]}(t)}
{\rho_{n_0n_0}^{[a,b]}(t)}
\right|
\le
C_{n_0}(1+n)^M
\exp\left[-c_T(n^2-n_0^2)\right].
\]

The right side is summable against every exponentially bounded coefficient packet. Each fixed ratio tends to zero as \(t\to+\infty\), so dominated convergence yields

\[
d_{n_0}=0,
\]

contradicting least activity. Hence \(d=0\).

## Result

For a fixed shell,

\[
\ker(DJ_{\rm or})
\cap
\mathcal A^{\rm fixed\ shell}_{\rm diagonal\ labels}
=\{0\}.
\]

Repeated shell endpoints do not create a radical among diagonal theta labels.

## Scope boundary

This theorem does not yet separate all ordered pairs \((n,m)\). Positive separation first orders the shifted label \(m\); several terms with the same \(m\) can retain different unshifted labels \(n\). Resolving those blocks requires the opposite orientation or linear independence of the unshifted completed atoms inside the endpoint coefficient.

It also does not identify any G4 metric or quotient.

## Next discriminator

For a finite ordered-pair packet, positive separation isolates the least active shifted label \(m\). The leading endpoint coefficient is then a finite linear combination of the values and derivatives of \(\Phi_n\) at \(a\). Negative separation exchanges the roles of \(n\) and \(m\). Combining both orientations is the next candidate for full ordered-pair faithfulness.

## Disposition

The repeated-endpoint obstruction is closed for diagonal theta labels, including signed and complex summable combinations. Any remaining source-level codiagonal kernel must involve off-diagonal ordered-pair mixing rather than diagonal-label cancellation. No RH conclusion is authorized.
