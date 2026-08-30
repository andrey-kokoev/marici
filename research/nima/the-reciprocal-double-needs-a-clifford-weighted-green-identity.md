# The reciprocal double needs a Clifford-weighted Green identity

The doubled theta-tail system will not yield seam coercivity by simply adding the two one-sided energy identities. The reciprocal parameter has the opposite centered real part.

Write
\[
s=\frac12+\lambda,
\qquad
1-s=\frac12-\lambda.
\]
Let \(G_{+}\) be the positive-orientation tail and \(G_{-}\) the reciprocal tail. Their centered bulk coefficients are \(+\operatorname{Re}\lambda\) and \(-\operatorname{Re}\lambda\).

If the raw identities are added with the same sign, the centered contribution is indefinite:
\[
\operatorname{Re}\lambda
\left(
\|G_{+}\|^{2}-\|G_{-}\|^{2}
\right).
\]
This cannot force \(\operatorname{Re}\lambda=0\).

The reciprocal component must instead be paired with the opposite Clifford sign. On
\[
\mathcal H_{+}\oplus\mathcal H_{-},
\]
introduce the fundamental symmetry
\[
J=
\begin{pmatrix}
I&0\\
0&-I
\end{pmatrix}.
\]
Testing the doubled system against \(J\Psi\), rather than \(\Psi\), converts the two opposite centered coefficients into the same positive bulk energy:
\[
\operatorname{Re}\lambda
\left(
\|G_{+}\|^{2}+\|G_{-}\|^{2}
\right).
\]

This is the exact algebraic reason the reciprocal sheet is needed. It is not a second copy added for scalar functional-equation symmetry. Its orientation sign turns the centered spectral parameter into a definite doubled bulk term.

The desired integrated identity has the form
\[
2\operatorname{Re}\lambda\,
\mathcal E_{\mathrm{tail}}(\Psi)
+
\mathcal D_{\mathrm{int}}(\Psi)
=
\mathcal F_{\partial}(\Gamma\Psi),
\]
where
\[
\mathcal E_{\mathrm{tail}}(\Psi)
=
\|G_{+}\|^{2}+\|G_{-}\|^{2},
\]
\(\mathcal D_{\mathrm{int}}\ge0\) is any residual interior dissipation, and \(\mathcal F_{\partial}\) is the complete wall, seam, prime, and archimedean flux.

For a closed resonant state, conservative sewing should impose
\[
\mathcal F_{\partial}(\Gamma\Psi)=0.
\]
If the system is lossless,
\[
\mathcal D_{\mathrm{int}}=0,
\]
and any nonzero resonant state then satisfies
\[
\operatorname{Re}\lambda=0.
\]
If there is strict interior dissipation in one sector, the identity instead excludes the resonance there.

The source burden is in the forcing terms. The doubled one-sided equations generate
\[
-2\operatorname{Re}\langle f_{+},G_{+}\rangle
+
2\operatorname{Re}\langle f_{-},G_{-}\rangle
\]
after the \(J\)-weighting. Bilateral modular sewing must identify this signed combination with the complete boundary flux. Any uncancelled component is an indefinite source residue and destroys the argument.

Thus the finite audit should retain four columns:

\[
\begin{array}{c|c|c|c}
\text{sheet}&\text{orientation sign}&\text{centered parameter}&\text{forcing current}\\
+&+1&+\lambda&f_{+}\\
-&-1&-\lambda&f_{-}
\end{array}
\]

Every endpoint, wall, and archimedean term must be assigned the same orientation sign before cancellation is tested.

The Green form produced by \(J\) is initially indefinite. The physical positive energy is not the \(J\)-metric itself; it is the coefficient of \(\operatorname{Re}\lambda\) after the reciprocal signs have been multiplied. Confusing these two forms would falsely claim Krein positivity.

The smallest hostile doubles the system but adds the two ordinary Hilbert identities. It obtains only
\[
\operatorname{Re}\lambda
(\|G_{+}\|^{2}-\|G_{-}\|^{2})=0,
\]
which permits balanced off-seam states.

A second hostile uses the correct \(J\)-weight but omits an archimedean forcing residue. The resulting bulk energy is definite, yet the uncancelled boundary source can support an off-seam state.

The next executable theorem is therefore:

> The source reciprocal involution intertwines the two theta-tail equations so that their Clifford-weighted Green identity has definite centered bulk energy and exactly the complete source boundary flux.

If proved, this identity is the differential-system counterpart of strict Schur return plus unitary feedback. It would supply seam confinement before determinant identification.
