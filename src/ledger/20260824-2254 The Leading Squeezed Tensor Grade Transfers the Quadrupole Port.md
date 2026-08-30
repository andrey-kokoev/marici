# 2254 — The Leading Squeezed Tensor Grade Transfers the Quadrupole Port

## Hard-to-vary claim

The soft-tensor port of Entry 2252 survives the leading squeezed Ward grade
for every radial scalar spectrum with nonzero logarithmic slope.  Gauge/Ward
reduction therefore does not generically kill the two quadrupole directions at
this grade.

## Frozen Ward operator

Let \(P(k)\) be the radial scalar two-point coefficient.  A long traceless
tensor mode acts on the hard momentum by anisotropic dilation.  Its leading
squeezed response is

\[
\mathcal W_sP(k)
=
-e_s^{ij}k_i\partial_{k_j}P(k)
=
-kP'(k)e_s^{ij}\widehat k_i\widehat k_j.
\]

Dividing by \(P(k)\) gives the source-fixed transfer coefficient

\[
-\partial_{\log k}\log P(k).
\]

For the two real tensor polarizations,

\[
e_+^{ij}\widehat k_i\widehat k_j=\cos2\theta,
\qquad
e_\times^{ij}\widehat k_i\widehat k_j=\sin2\theta.
\]

Thus the Ward transfer preserves exactly the quadrupole occurrence adapter.

## Equilateral rank

Together with the scalar score, the scaled angular matrix again has

\[
\det
\begin{pmatrix}
2&2&0\\
2&-1&-1\\
2&-1&1
\end{pmatrix}
=-12.
\]

The transferred readout is rank three whenever

\[
\partial_{\log k}\log P(k)\ne0.
\]

It fails only for a locally scale-flat spectrum.  In particular, an exact
power law with nonzero exponent transfers the port.

## Scope boundary

Established only at the leading squeezed/associated Ward grade:

\[
\boxed{
\text{soft tensor port}
\longrightarrow
\text{quadrupole scalar response}
}
\]

with source-fixed coefficient.

Not established:

- the complete finite-soft-momentum transfer;
- subleading gauge and constraint terms;
- a detector/readout chain selecting both tensor polarizations;
- signal strength or observational feasibility.

Hence this is a coefficient-transfer theorem, not yet an experimental
observability theorem.

## Verification

`research/benincasa/checkers/squeezed_tensor_transfer_grade.rs` verifies the
angular rank and records the exact spectral-slope failure locus.
