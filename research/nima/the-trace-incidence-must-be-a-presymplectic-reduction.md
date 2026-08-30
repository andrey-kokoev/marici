# The trace incidence must be a presymplectic reduction

The rank correction has a sharper invariant formulation. The coefficient observer space and the analytic trace space are related not merely by a linear map, but by their Green boundary forms.

Let \(\mathcal W\) be the finite coefficient observer space with source boundary form \(\omega_{\mathcal W}\), and let \(\mathcal B\) be the deficiency trace space with canonical Green form
\[
\omega_{\mathcal B}\big((x_0,x_1),(y_0,y_1)\big)
=
\langle x_1,y_0\rangle-\langle x_0,y_1\rangle .
\]
A source-authorized incidence
\[
\mathcal T:\mathcal W\longrightarrow\mathcal B
\]
must satisfy the pullback identity
\[
\omega_{\mathcal W}(u,v)
=
\omega_{\mathcal B}(\mathcal Tu,\mathcal Tv).
\]

This immediately identifies the passive coefficient directions. If the pullback identity holds, then
\[
\ker\mathcal T\subseteq\operatorname{rad}\omega_{\mathcal W}.
\]
For the reachable quotient to carry exactly the analytic Green geometry, the stronger equality is required:
\[
\ker\mathcal T
=
\operatorname{rad}\omega_{\mathcal W}.
\]
Then \(\mathcal T\) induces a symplectic isomorphism
\[
\overline{\mathcal T}:
\mathcal W/\operatorname{rad}\omega_{\mathcal W}
\longrightarrow
\operatorname{ran}\mathcal T.
\]

Three failure modes are now separate:

1. If \(\ker\mathcal T\) is larger than the coefficient radical, a genuinely observed coefficient direction becomes analytically dark.
2. If the coefficient radical is larger than \(\ker\mathcal T\), a null source coordinate is represented as nonzero analytic boundary data.
3. If the forms disagree after quotienting, the map preserves rank but reverses or distorts the Green orientation.

The arithmetic boundary condition must descend through the same reduction. If \(\Theta_{\mathcal W}(s)\) is first written on coefficient coordinates, it is admissible only when it preserves the radical and factors as
\[
\Theta_{\mathcal W}(s)
=
\mathcal T^{*}\Theta_{\mathcal B}(s)\mathcal T
\]
as a form on \(\mathcal W\), with the appropriate quotient interpretation. The spectral collision is then
\[
\ker\bigl(\Theta_{\mathcal B}(s)-M(s)\bigr)\neq0
\]
on \(\operatorname{ran}\mathcal T\), not on the unreduced observer space.

This also gives the correct determinant comparison. After choosing source-authorized volume lines,
\[
\det_{\mathcal W/\operatorname{rad}}
\bigl(\Theta_{\mathcal W}(s)-\mathcal T^{*}M(s)\mathcal T\bigr)
\]
and
\[
\det_{\operatorname{ran}\mathcal T}
\bigl(\Theta_{\mathcal B}(s)-M(s)\bigr)
\]
may differ by the square of the incidence determinant. That factor is harmless only if it is nonzero and zero-free in \(s\). An \(s\)-dependent degenerating incidence can manufacture or cancel zeros even when the two kernels agree pointwise away from degeneration.

Thus completion requires a sixth-looking but upstream realization estimate:
\[
c\,\|[u]\|_{\mathcal W}
\le
\|\mathcal Tu\|_{\mathcal B}
\le
C\,\|[u]\|_{\mathcal W},
\]
uniformly on compact off-seam sets. This is not a new global Green margin; it is the uniform nondegeneracy of the coefficient-to-trace coordinate change.

The next source theorem is therefore exact:

> The four-port coefficient boundary form descends by its radical to the deficiency trace space, and the induced incidence is a uniformly bi-bounded Green-form isomorphism onto the reachable trace sector.

The minimal hostile has the correct quotient dimension and identical scalar determinant zeros, but \(\det\overline{\mathcal T}(s)\to0\) near the seam. Finite spectral identification survives while completion-stable observability fails.

This turns the rank audit into a presymplectic reduction theorem and specifies precisely which part of the five-wall packet may enter the Weyl pencil.
