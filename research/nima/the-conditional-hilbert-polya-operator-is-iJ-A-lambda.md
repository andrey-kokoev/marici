# The conditional Hilbert--Polya operator is \(iJ\mathcal A_{\Lambda}\)

The \(J\)-skew Green identity identifies the exact operator that would realize the Hilbert--Pólya programme.

Let \(\mathcal A_{\Lambda}\) be the closed doubled source generator with boundary traces restricted to a conservative sewing relation
\[
\Gamma\Psi\in\Lambda.
\]
Assume first the lossless identity
\[
\mathcal A_{\Lambda}^{*}J
+
J\mathcal A_{\Lambda}
=
0.
\]

Define
\[
B_{\Lambda}
=
J\mathcal A_{\Lambda}.
\]
Since \(J=J^{*}=J^{-1}\),
\[
B_{\Lambda}^{*}
=
\mathcal A_{\Lambda}^{*}J
=
-J\mathcal A_{\Lambda}
=
-B_{\Lambda}.
\]
Thus \(B_{\Lambda}\) is skew-symmetric. If \(\Lambda\) is maximal isotropic and the boundary system is complete, the extension theorem should upgrade this to
\[
B_{\Lambda}^{*}=-B_{\Lambda},
\]
so \(B_{\Lambda}\) is skew-adjoint.

The Hilbert--Pólya candidate is then
\[
H_{\Lambda}
=
iB_{\Lambda}
=
iJ\mathcal A_{\Lambda}.
\]
It is self-adjoint.

The centered source equation
\[
(\mathcal A_{\Lambda}+\lambda J)\Psi=0
\]
becomes, after multiplying by \(J\),
\[
(B_{\Lambda}+\lambda)\Psi=0.
\]
Equivalently,
\[
H_{\Lambda}\Psi
=
-i\lambda\,\Psi.
\]
Because the spectrum of \(H_{\Lambda}\) is real,
\[
-i\lambda\in\mathbb R,
\]
hence
\[
\operatorname{Re}\lambda=0.
\]

This is stronger and cleaner than proving a separate norm contraction for every parameter. The scattering return and its Schur property become the characteristic-function shadow of one self-adjoint extension.

The exact obligations are now sharply separated:

1. Formal symmetry:
   prove the core Green identity
   \[
   \mathcal A_0^{*}J+J\mathcal A_0
   =
   \Gamma^{*}\Sigma\Gamma.
   \]
2. Boundary completeness:
   prove \(\Gamma\) is onto the reduced boundary phase space, or use the corresponding boundary relation theorem.
3. Maximal sewing:
   prove \(\Lambda=\Lambda^{\perp_{\Sigma}}\), not only \(\Lambda\subseteq\Lambda^{\perp_{\Sigma}}\).
4. Closed realization:
   prove \(\mathcal A_{\Lambda}\) is closed and densely defined.
5. Self-adjointness:
   prove \(iJ\mathcal A_{\Lambda}\) has zero deficiency indices.
6. Spectral identification:
   prove its characteristic boundary determinant equals \(\xi\) up to a nowhere-zero factor.
7. Multiplicity:
   identify algebraic zero order with spectral multiplicity.

An isotropic but nonmaximal boundary condition yields only a symmetric \(H_{\Lambda}\). Symmetric operators can have nonreal eigenvalues in extensions or incomplete resolvent data; formal energy identities alone do not complete Hilbert--Pólya.

If the doubled identity contains dissipation
\[
\mathcal A_{\Lambda}^{*}J
+
J\mathcal A_{\Lambda}
=
-\mathcal Q,
\qquad
\mathcal Q\ge0,
\]
then \(iJ\mathcal A_{\Lambda}\) is not self-adjoint. The correct conclusion is maximal dissipativity and half-plane exclusion, not a Hilbert--Pólya operator. Exact losslessness is therefore required on the final closed seam system, even if strict dissipation is useful before sewing.

The constant theta source channel is crucial here. Without it, the inhomogeneous tail equation does not define a linear operator domain and \(H_{\Lambda}\) is not an honest homogeneous spectral operator.

The minimal hostile verifies
\[
\langle
(\mathcal A_{\Lambda}^{*}J+J\mathcal A_{\Lambda})\Psi,
\Psi
\rangle=0
\]
on a core but chooses a nonmaximal \(\Lambda\). It obtains a symmetric \(H_{\Lambda}\) with unresolved deficiency spaces and falsely declares self-adjointness.

A second hostile constructs \(H_{\Lambda}\) correctly but identifies \(\xi\) only by fitting a boundary coefficient. It solves seam confinement without proving that zeta zeros are its spectrum.

Thus the programme has reached a conditional categorical resolution:

\[
\text{source doubled generator}
+
\text{complete Green trace}
+
\text{maximal reciprocal sewing}
\Longrightarrow
H_{\Lambda}=iJ\mathcal A_{\Lambda}\text{ self-adjoint}.
\]

The sole remaining bridge to RH is then the independently authorized characteristic-determinant identification.
