# The restricted heat-polynomial image is not sparse

## Question

Does the source map avoid the full Weil difficulty by restricting positivity to a small exceptional family of Schwartz tests?

## Claim boundary

The small-mesh image contains limits of every odd monomial-Gaussian. This falsifies finite-dimensional or sparse-family explanations. Full Schwartz-topology density and whether the odd sector determines RH remain open.

## Source map

Let

\[
q_h(u)
=
u\sqrt{\frac{1-e^{-hu^2}}{u^2}}
\]

with the smooth odd extension, and

\[
G_{t,h,p}(u)
=
e^{-tu^2/2}q_h(u)p(e^{-hu^2}).
\]

Then

\[
|G_{t,h,p}(u)|^2
=
e^{-tu^2}(1-e^{-hu^2})|p(e^{-hu^2})|^2.
\]

This identifies the exact pre-GNS localizer tests.

## Small-mesh limits

The multiplier satisfies

\[
\frac{q_h(u)}{\sqrt h}
\longrightarrow u.
\]

For each nonnegative integer \(k\), choose the mesh-dependent polynomial

\[
p_{h,k}(y)=\frac{(1-y)^k}{h^k}.
\]

Then

\[
p_{h,k}(e^{-hu^2})
=
\frac{(1-e^{-hu^2})^k}{h^k}
\longrightarrow u^{2k}.
\]

Consequently

\[
\frac{G_{t,h,p_{h,k}}(u)}{\sqrt h}
\longrightarrow
 e^{-tu^2/2}u^{2k+1}.
\]

The first multiplier correction is

\[
\frac{q_h(u)}{\sqrt h}
=u-\frac h4u^3+O(h^2u^5).
\]

Thus the source family approaches every odd monomial times a Gaussian.

## Density consequence

Odd polynomial-Gaussians span the odd Hermite sector densely in odd \(L^2(\mathbb R)\). Standard Gaussian domination should upgrade the displayed limits to every Schwartz seminorm for fixed \(k,t>0\), but those estimates have not yet been written.

Therefore the union over small meshes and polynomial probes is not:

- finite-dimensional;
- finite-rank;
- spectrally sparse;
- protected from the ordinary odd Gaussian test sector.

Any explanation based on the test family being too small to detect the Weil obstruction is falsified.

## What remains unresolved

This result does not prove that the image is dense in the entire admissible Weil test space. It reaches the odd Hermite sector. A complete reverse argument must determine whether positivity on odd convolution squares alone already implies the full Weil criterion, perhaps using parity, translation, or differentiation identities.

The source map itself remains valuable: it supplies exact mesh composition and a pre-GNS formulation. What fails is the hope that restriction makes positivity substantially weaker.

## Common-center interpretation

For

\[
G_0=e^{-tu^2/2}q_h,
\qquad
G_r=G_0(e^{-hu^2}-r),
\]

the rank-two quantities are restrictions of the same Weil sesquilinear form. The identity

\[
D_2=A_0C_r-|B_r|^2
\]

is a two-test determinant. Applying Cauchy--Schwarz would assume positivity of that restricted form and would therefore be circular.

## Disposition

The restricted source image is large in the small-mesh limit. The next falsification gate is parity: test whether the odd Hermite sector is Weil-determining. If it is, the heat-polynomial cone is another complete RH criterion rather than a weaker tractable subcone.

## Verification

- `research/voevodsky/restricted-heat-polynomial-density-falsifier-v1.json`
- `research/voevodsky/checkers/check_restricted_heat_polynomial_density_falsifier.py`
- `research/voevodsky/results/restricted_heat_polynomial_density_falsifier.json`
