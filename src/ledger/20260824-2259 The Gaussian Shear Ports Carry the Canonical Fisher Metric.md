# 2259 — The Gaussian Shear Ports Carry the Canonical Fisher Metric

For one centered Gaussian mode, the normalized kernel score has variance
\(1/2\).  Combining this with

\[
\langle\cos2\theta\rangle=\langle\sin2\theta\rangle=0,
\qquad
\langle\cos^22\theta\rangle=\langle\sin^22\theta\rangle=\frac12
\]

gives, at unit logarithmic radial slope, the Fisher metric

\[
G=\operatorname{diag}\left(\frac12,\frac14,\frac14\right)
\]

on the scalar, plus, and cross score ports.  The two shear directions are
orthogonal and have equal norm.  Their relative geometry is therefore fixed
by the Gaussian source and rotational measure; it is not a basis fitted to the
three occurrences.

The scalar normalization may differ from the shear normalization, but the
rank-two shear plane has a canonical Euclidean metric up to its common radial
slope.  This strengthens the interpretation of the adapter as a physical
susceptibility space while remaining prior to detector selection.

Verified by
`research/benincasa/checkers/quadrupole_information_geometry.rs`.
