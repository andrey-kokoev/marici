# Fourier anti-symplecticity would canonically split wall values from tail fluxes

The corrected joint-trace picture suggests a source-native Darboux splitting. The four-port observer already decomposes under Fourier square:
\[
\mathcal W
=
\mathcal W_{+}\oplus\mathcal W_{-},
\qquad
\mathcal W_{+}=\operatorname{span}\{1,\delta_0\},
\qquad
\mathcal W_{-}=\operatorname{span}\{K,V\}.
\]

The decisive identity is not merely Fourier invariance of a positive Gram. It is anti-symplecticity of the boundary Green form:
\[
\omega_{\mathcal W}(Fu,Fv)
=
-\omega_{\mathcal W}(u,v).
\]

If \(u,v\in\mathcal W_{+}\), then
\[
\omega_{\mathcal W}(u,v)
=
-\omega_{\mathcal W}(u,v),
\]
so \(\omega_{\mathcal W}(u,v)=0\). The same argument applies to \(\mathcal W_{-}\), since both vectors acquire a minus sign. Therefore both Fourier-character planes are isotropic:
\[
\omega_{\mathcal W}|_{\mathcal W_{+}}=0,
\qquad
\omega_{\mathcal W}|_{\mathcal W_{-}}=0.
\]

In the ordered basis
\[
(1,\delta_0\mid K,V),
\]
the Green matrix must consequently have the form
\[
\Omega_{\mathcal W}
=
\begin{pmatrix}
0 & J\\
-J^{*} & 0
\end{pmatrix},
\]
where the \(2\times2\) cross matrix \(J\) contains the wall-to-tail boundary pairing.

This reduces the rank theorem to one finite determinant:
\[
\Omega_{\mathcal W}\text{ nondegenerate}
\quad\Longleftrightarrow\quad
\det J\neq0.
\]
When this holds, \(\mathcal W_{+}\) and \(\mathcal W_{-}\) are complementary Lagrangians. They provide a source-selected polarization:
\[
\Gamma_0\text{-plane}=\mathcal W_{+},
\qquad
\Gamma_1\text{-plane}=\mathcal W_{-},
\]
or the reversed assignment if fixed by the Green sign convention.

The exact observer matrix already found for endpoint currents,
\[
T=
\begin{pmatrix}
1/2&1/4\\
1/2&-1/4
\end{pmatrix},
\qquad
\det T=-1/4,
\]
is now a candidate for \(J\), up to source-derived row and column normalizations. If the Green/Stokes computation proves \(J=T\), then
\[
\sigma_{\min}(J)=\frac{1}{2\sqrt2}
\]
gives an explicit finite transversality margin between wall values and tail fluxes.

This must not be inferred from the additive observer alone. The source theorem must show:

1. Fourier acts on the coefficient boundary packet with the frozen wall/tail characters.
2. The Green form is Fourier anti-symplectic, not symplectic.
3. The cross block \(J\) is exactly the trace observer matrix, with signs and half-densities fixed.
4. The analytic incidence transports this polarization to the \((\Gamma_0,\Gamma_1)\) trace polarization.
5. The lower singular bound survives prime assembly and compact off-seam completion.

If Fourier instead preserves \(\omega_{\mathcal W}\), then the argument reverses: the cross wall-tail block vanishes, and each character plane carries its own symplectic form. That would produce a different boundary triple. The sign of the Fourier covariance is therefore an empirical constructor fact, not a stylistic convention.

The smallest hostile has the correct four-dimensional rank and the correct positive saturated Gram, but Fourier is symplectic rather than anti-symplectic. Assigning wall ports to values and tail ports to fluxes then yields zero Green coupling even though every scalar observer remains faithful.

Thus the next finite calculation is a single signed covariance:
\[
F^{*}\Omega_{\mathcal W}F
\stackrel{?}{=}
-\Omega_{\mathcal W}.
\]
If it holds and \(J\) is invertible, the source has supplied the Darboux splitting that the Weyl-pencil construction needs.
