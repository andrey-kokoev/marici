# Sector-derived product metrics are noise-whitened readout metrics, not arbitrary direct sums

## Question

What additional sector data turns the mathematically declared bulk--moduli product metric into a physical metric for the Green--Real radial example?

## Claim boundary

This packet gives the conditional construction from a calibrated physical readout and noise covariance. It proves when the metric is a direct product and when cross-covariance forces a coupled metric. The current radial interface contract does not contain the required calibration object, so no numerical physical metric is claimed for that contract.

## Required sector datum

Let the physical state variables be

\[
(x,m)\in X_{\mathrm{phys}}\times\mathcal M_\Gamma,
\]

where \(X_{\mathrm{phys}}\) is a declared bulk state space and \(\mathcal M_\Gamma\) is the sewing-moduli quotient.

A sector-derived metric requires a physical record map

\[
\mathcal R:
X_{\mathrm{phys}}\times\mathcal M_\Gamma
\longrightarrow
\mathcal Y_X\oplus\mathcal Y_M
\]

and a strictly positive noise covariance

\[
\Sigma:
\mathcal Y_X\oplus\mathcal Y_M
\longrightarrow
\mathcal Y_X\oplus\mathcal Y_M.
\]

The associated noise-whitened record distance is

\[
d_{\mathrm{rec}}(z,z')^2
=
\left\langle
\mathcal R(z)-\mathcal R(z'),
\Sigma^{-1}
\bigl(\mathcal R(z)-\mathcal R(z')\bigr)
\right\rangle.
\]

This metric is source-derived only when the record map, units, covariance, and calibration provenance are supplied by the sector. Positivity of \(\Sigma\) is a measurement assumption, not a consequence of Green sewing.

## Linearized Fisher form

At a regular point \(z=(x,m)\), the pullback quadratic form is

\[
g_z(v,w)
=
\left\langle
D\mathcal R_z v,
\Sigma^{-1}D\mathcal R_z w
\right\rangle.
\]

This is the Gaussian Fisher information form for a location family with covariance \(\Sigma\). It is positive definite precisely when the differentiated record map is injective on the physical quotient under discussion.

A probability model is not required for the algebraic whitening formula, but calling the form Fisher information requires the declared statistical model.

## Product criterion

Write

\[
\mathcal R(x,m)=
\bigl(R_Xx,\Psi_\Gamma(m)\bigr).
\]

If the covariance is block diagonal,

\[
\Sigma=
\begin{pmatrix}
\Sigma_X&0\\
0&\Sigma_M
\end{pmatrix},
\]

then

\[
d_{\mathrm{rec}}^2
=
\|\Sigma_X^{-1/2}R_X(x-x')\|^2
+
\|\Sigma_M^{-1/2}
(\Psi_\Gamma(m)-\Psi_\Gamma(m'))\|^2.
\]

This is an explicit sector-derived product metric. The relative scaling between bulk and moduli is fixed by calibrated noise, not chosen for convenience.

If \(\Sigma^{-1}\) has a nonzero off-diagonal block \(Q\), then

\[
d_{\mathrm{rec}}^2
=
d_X^2+d_M^2
+2\operatorname{Re}
\langle R_X\Delta x,
Q\,\Delta\Psi\rangle.
\]

The physical metric is then coupled. Replacing it by a direct product silently discards measured cross-correlation.

## Controlled product approximation

Suppose the whitened quadratic form has block representation

\[
G=
\begin{pmatrix}
G_X&E\\
E^*&G_M
\end{pmatrix}
\]

with \(G_X,G_M>0\). Define

\[
\eta=
\|G_X^{-1/2}EG_M^{-1/2}\|.
\]

If \(\eta<1\), then

\[
(1-\eta)(d_X^2+d_M^2)
\le
d_{\mathrm{rec}}^2
\le
(1+\eta)(d_X^2+d_M^2).
\]

Thus a product metric is a controlled comparison presentation when the normalized cross block is strictly below one. It is exact only when \(E=0\).

## Edge weights from phase calibration

Suppose each edge phase has a local complex record with isotropic variance \(\sigma_e^2\), and distinct edge records are uncorrelated. Whitening gives

\[
\lambda_e=\sigma_e^{-2}
\]

in the edge chord metric

\[
d_E(z,z')^2
=
\sum_e\lambda_e|z_e-z'_e|^2.
\]

The quotient metric

\[
d_\Gamma([z],[z'])
=
\inf_g d_E(z,g\cdot z')
\]

is then sector-derived from phase-readout precision. The explicit Wilson lower bound becomes

\[
\alpha_\Gamma
\ge
\left(
\min_T\max_{e\notin T}\sigma_e^{-2}
\right)^{-1/2}.
\]

This formula is relative to the convention that target Wilson quadratures have unit Euclidean noise. If their covariance is nontrivial, the target norm and bound must be whitened as well.

## Bulk metric from physical readout

A graph norm

\[
\|x\|^2+\|Dx\|^2
\]

is analytically natural but is not automatically a physical metric. A sector-derived bulk metric requires one of:

1. an energy or action Hessian with declared units and positivity domain;
2. a calibrated bulk record covariance and response map;
3. an independently sourced positive quadratic form proved equivalent to the graph norm.

If a physical bulk form \(G_{\mathrm{phys}}\) satisfies

\[
c_-\|x\|_D^2
\le
\langle G_{\mathrm{phys}}x,x\rangle
\le
c_+\|x\|_D^2,
\]

then every graph-observer lower constant \(\delta_D\) transports to physical norm with lower constant at least

\[
\frac{\delta_D}{\sqrt{c_+}}.
\]

This is a boundedly invertible metric comparison, not an identification of analytic and physical norms.

## Combined physical lower bound

Assume:

- the bulk physical norm is bounded above by \(c_+\|x\|_D^2\);
- the bulk observer has graph lower constant \(\delta_D\);
- edge and Wilson covariances provide a moduli lower constant \(\alpha_{\Gamma,\mathrm{phys}}\);
- the normalized bulk--moduli cross block has size \(\eta<1\).

Then the physical record observer has a lower constant bounded by

\[
\sqrt{1-\eta}
\min\left(
\frac{\delta_D}{\sqrt{c_+}},
\alpha_{\Gamma,\mathrm{phys}}
\right)
\]

relative to the corresponding uncoupled physical product metric.

The four factors have distinct provenance: graph stability, metric comparison, phase calibration, and cross-covariance control.

## Green--Real compatibility

The record covariance must respect the declared Real grading if Real-even and Real-odd channels are to remain orthogonal noise sectors. Block diagonality between even and odd quadratures is an empirical or design condition. Real covariance of the noiseless map does not imply it.

Likewise, Green anti-isometry of a reciprocal wall comparison does not determine detector noise or energy normalization. Green sewing supplies coherence; calibration supplies metric scale.

## Audit of the current radial contract

The current radial interface specifies boundary identifications, phase behavior, Green/Real comparison requirements, and constructor-role restrictions. It does not supply:

- a physical bulk record map with units;
- a positive bulk noise covariance or energy Hessian;
- edge-phase variances;
- Wilson-record covariance;
- bulk--moduli cross-covariance;
- a source-authorized statement identifying the physical quotient.

Therefore the present programme has mathematically explicit product metrics and conditional physical transport formulas, but no numerically sector-derived physical product metric.

The first missing typed object is a calibration packet

\[
\mathfrak C_{
\mathrm{phys}}
=(\mathcal R,\Sigma,\text{units},
\text{quotient},\text{provenance}).
\]

Acceptance requires positive covariance on the admitted record subspace, declared units, source provenance, and compatibility with the quotient and Real grading.

## Deliberate failures

1. An analytic graph norm is not a physical metric without a source-derived comparison.
2. Detector covariance cannot be inferred from Green or Real covariance.
3. A block product metric is invalid when measured cross-covariance is retained but omitted.
4. Edge weights are not physically canonical without phase calibration.
5. Fisher terminology is invalid without a statistical record model.
6. Whitening a gauge-dependent edge record does not remove the need to quotient vertex gauge.

## Disposition

A physical bulk--moduli metric is the pullback of a calibrated noise-whitened record metric. It is a direct product exactly under block-separable response and covariance, and it is quantitatively comparable to a product when the normalized cross block is below one. The current radial contract lacks the calibration packet needed for a numerical physical metric. This is an authority boundary, not a mathematical defect; the branch stops at that first missing typed object.
