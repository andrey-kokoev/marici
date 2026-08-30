# 1399 — Naive Deck Parity Does Not Preserve the Cubic Affine Kernel

## Status

Replicated modular negative result at \((p,z)=(1019,7)\) and \((1019,13)\).

## Motivation

Entry 1393 constructed a rank-two affine mismatch plane for the occurrence triple

\[
(1,2,3).
\]

The deck-complement triple

\[
(2,3,4)
\]

has the same torsor data, with pair dimensions permuted:

\[
(219,152,152),
\qquad
523,
\qquad
246,
\qquad
2.
\]

Equal dimensions do not define a linear intertwiner.

## Frozen candidate deck action

On the full-Kummer coefficient columns, test the evident character-parity involution

\[
D_{\rm par}:e_S\longmapsto(-1)^{|S|}e_S,
\]

while fixing the scalar affine coefficient.

Let \(A\) be the homogeneous affine matrix. The kernel is preserved exactly when

\[
\operatorname{row}(A D_{\rm par})
=
\operatorname{row}(A),
\]

equivalently when stacking the two matrices does not increase rank.

## Result

At both maximal-rank fibers,

\[
\operatorname{rank}A=1152,
\]

but

\[
\boxed{
\operatorname{rank}
\begin{pmatrix}
A\\
A D_{\rm par}
\end{pmatrix}
=
1921.
}
\]

Since \(1921\) is the full column rank,

\[
D_{\rm par}(\ker A)
\ne
\ker A.
\]

Indeed, the two homogeneous kernels are transverse in the tested ambient coefficient space.

## Narrow conclusion

The equal rank-two mismatch planes for complement-labelled triples are not related by the naive Kummer-character parity action.

Therefore Entry 1393 currently establishes:

\[
\text{dimension covariance}
\]

but not

\[
\text{deck-equivariant coefficient transport}.
\]

## What remains possible

The physical/source deck transformation may act simultaneously on:

- Kummer sheets;
- external kinematic coordinates;
- the affine source column;
- primitive normalizations.

The present calculation excludes only the columnwise parity involution with fixed kinematics.

No corrected deck map may be fitted from the observed equal dimensions.

## Consequence

Until a source-derived combined action is constructed, the rank-two plane remains a chart-level modular object rather than a deck-descended coefficient system.

This is a failure of the strongest interpretation, not evidence for a new carrier stratum.

## Next finite falsifier

Derive the actual cyclic/deck action from the five-cycle source packet, including its induced rational transformation of the asymmetric coordinates \((u_1,u_2,u_3)\).

Then test the full semilinear covariance identity

\[
A(\sigma u)D_\sigma
=
G_\sigma(u)A(u)
\]

before transporting \(\Pi_{123}\).

If no source-derived coordinate action exists in the frozen packet, close the descent claim under the current source rather than choosing one.

## Artifacts

- `research/benincasa/results/five-site-asymmetric-deck-parity-audit.json`
- `research/benincasa/results/five-site-asymmetric-kummer-resolved-ibp-pilot.json`
- `research/benincasa/marici-gm/src/bin/five_site_asymmetric_kummer_resolved_ibp_pilot.rs`

Allocator claim: `seqclaim-af88458cd918dc4e7e621aa2`.
