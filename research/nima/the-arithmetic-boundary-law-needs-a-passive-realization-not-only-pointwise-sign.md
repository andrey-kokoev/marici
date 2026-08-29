# The arithmetic boundary law needs a passive realization, not only pointwise sign

The Nevanlinna reduction creates one further constructor obligation. A \(z\)-dependent boundary condition
\[
\Gamma_1f=\Theta(z)\Gamma_0f
\]
is not a fixed self-adjoint extension merely because \(\Theta(x)\) is self-adjoint for real \(x\), or because its imaginary part has the desired sign pointwise.

The correct global condition is positivity of the anti-Nevanlinna kernel
\[
K_{\Theta}(z,w)
=
-\frac{\Theta(z)-\Theta(w)^{*}}{z-\bar w}.
\]
For every finite choice \(z_1,\ldots,z_m\) in the upper half-plane and boundary vectors \(b_1,\ldots,b_m\), require
\[
\sum_{i,j}
\left\langle
b_i,
K_{\Theta}(z_i,z_j)b_j
\right\rangle
\ge0.
\]

The diagonal case recovers
\[
-\frac{\operatorname{Im}\Theta(z)}{\operatorname{Im}z}\ge0,
\]
but the full kernel condition is stronger. It controls compatibility across spectral parameters and is the certificate that \(\Theta\) can arise as the transfer or Weyl function of a passive auxiliary constructor.

In the cleanest realization one seeks a self-adjoint auxiliary operator \(A_{\mathrm{arith}}\), a coupling \(C\), and a self-adjoint constant \(\Theta_0\) such that
\[
\Theta(z)
=
\Theta_0
-
C^{*}(A_{\mathrm{arith}}-z)^{-1}C,
\]
with sign adjusted to the frozen boundary convention. Then
\[
K_{\Theta}(z,w)
=
C^{*}(A_{\mathrm{arith}}-\bar w)^{-1}
(A_{\mathrm{arith}}-z)^{-1}C
\ge0
\]
as a kernel.

This linearizes the spectral-parameter-dependent boundary law. The history system and arithmetic auxiliary system can be joined into one fixed self-adjoint block operator. Eliminating the arithmetic state by a Schur complement recovers
\[
\Theta(z)-M(z).
\]
Therefore nonreal collision exclusion becomes ordinary reality of the spectrum of the enlarged self-adjoint constructor, rather than a separate inequality at every \(z\).

The source programme should now distinguish:

1. Pointwise dissipativity:
   enough for direct noncollision at one parameter.
2. Kernel anti-Nevanlinna positivity:
   enough for coherent analytic transport across parameters.
3. Passive realization:
   supplies an actual arithmetic constructor behind the boundary law.
4. Minimal realization:
   ensures no dark auxiliary state contributes an invisible determinant factor.
5. Uniform completion:
   controls the realization as prime cutoffs are removed.

For finite prime cutoff \(X\), the arithmetic relation \(\Theta_X(z)\) should have a finite passive realization derived from the Euler packets. Cutoff naturality must intertwine these colligations, not only their transfer functions. Equality of \(\Theta_X(z)\) after scalar compression can conceal nonminimal states.

The smallest hostile is a holomorphic matrix function whose diagonal imaginary part has the correct sign at every tested point but whose two-point Pick matrix
\[
\begin{pmatrix}
K_{\Theta}(z,z)&K_{\Theta}(z,w)\\
K_{\Theta}(w,z)&K_{\Theta}(w,w)
\end{pmatrix}
\]
is indefinite. It passes every one-point margin while admitting no passive Hilbert-space realization.

A second hostile adds an uncoupled self-adjoint summand to \(A_{\mathrm{arith}}\). The transfer function and determinant pencil remain unchanged, but the constructor acquires invisible spectrum. Minimality requires the cyclicity condition
\[
\overline{\operatorname{span}}
\left\{
(A_{\mathrm{arith}}-z)^{-1}Cb
\right\}
=
\mathcal H_{\mathrm{arith}}.
\]

The next finite computation is therefore the two-point Pick test for the source-derived \(2\times2\) arithmetic boundary relation. If it passes for all finite sets and admits a minimal cutoff-compatible realization, the programme gains a fixed self-adjoint dilation whose Schur complement is the RH pencil.

This is stronger than proving a favorable imaginary part, but it is exactly the constructor-level authority needed to turn seam confinement into a self-adjoint spectral theorem.
