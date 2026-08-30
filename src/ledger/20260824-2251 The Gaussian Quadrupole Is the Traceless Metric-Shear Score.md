# 2251 — The Gaussian Quadrupole Is the Traceless Metric-Shear Score

## Hard-to-vary claim

The rank-two quadrupole adapter of Entries 2235–2237 is not merely an
admissible anisotropic Gaussian deformation.  It is generated canonically by
the traceless spatial-metric response of any isotropic radial Gaussian kernel
with nonzero logarithmic radial slope.

## Frozen source operation

Let the Gaussian boundary kernel be radial,

\[
a_0=a_0(k),\qquad k=\sqrt{g^{ij}p_i p_j}.
\]

Vary the inverse spatial metric by a traceless shear

\[
\delta g=
\begin{pmatrix}
h_+&h_\times\\
h_\times&-h_+
\end{pmatrix}.
\]

For \(p=k(\cos\theta,\sin\theta)\), direct differentiation gives

\[
\delta k
=
\frac{k}{2}
\left(h_+\cos2\theta+h_\times\sin2\theta\right),
\]

and therefore

\[
\delta\log a_0(k)
=
\frac{k}{2}\partial_k\log a_0(k)
\left(h_+\cos2\theta+h_\times\sin2\theta\right).
\]

Thus the two quadrupole score directions have a source-fixed relative
normalization.  No occurrence projector is chosen.

## Equilateral occurrence test

At the three equilateral directions, twice the evaluation matrix of
\((1,\cos2\theta,\sin2\theta)\) is

\[
\begin{pmatrix}
2&2&0\\
2&-1&-1\\
2&-1&1
\end{pmatrix},
\qquad
\det=-12.
\]

Consequently the isotropic score together with the two metric-shear scores is
faithful on the three labelled occurrences whenever

\[
k\partial_k\log a_0(k)\ne0.
\]

The exact failure locus is a locally white Gaussian kernel,
\(\partial_k a_0=0\), where metric shear cannot be observed through this
state.

## Classification

\[
\boxed{
\text{existing occurrence Carrier}
+\text{source-derived traceless-metric lens}
\Longrightarrow
\text{faithful homogeneous readout}.
}
\]

This strengthens Entries 2235–2237: the quadrupole is not an arbitrary
positive anisotropic enlargement.  It is the canonical shear susceptibility
of the isotropic Gaussian state.  It still does not prove that a particular
experiment exposes this port; physical instrument accessibility remains a
separate readout question.

## Verification

`research/benincasa/checkers/gaussian_shear_score_source.rs` verifies the
equilateral rank and records the source operation, normalization, and precise
failure locus.
