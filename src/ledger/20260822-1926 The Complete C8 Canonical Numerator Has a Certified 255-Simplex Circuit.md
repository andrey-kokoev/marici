# 1926 — The Complete C8 Canonical Numerator Has a Certified 255-Simplex Circuit

## Source object

Equations (3.8)--(3.11) and (4.1)--(4.3) of arXiv:2305.19686v2 define the canonical function as the oriented contour pushforward of the 24 cosmological-polytope vertices.

For (C_8), freeze

\[
Y=(X_1,\ldots,X_8;y_1,\ldots,y_8)
\]

and the edge-major order of the three vertices and contour variables per edge. The exact source matrix has shape (16\times24), rank (16), and 65 physical facets:

\[
56\ \text{proper connected regions}
+8\ \text{spanning }G\setminus e
+1\ \text{total-energy facet}.
\]

The first source-ordered localization basis has determinant (-256), leaving the expected eight contour variables. All sixteen localized affine denominators and regulator labels are serialized.

## Complete numerator

A deterministic integer lifting (h_i=i^2) gives a strict regular triangulation into 255 projective 15-simplices. Every lower-support inequality was verified exactly. The triangulation has

\[
1016\ \text{internal ridges},
\qquad
2048\ \text{boundary ridges}.
\]

Every internal ridge occurs twice with opposite oriented boundary signs. Every boundary ridge lies on exactly one frozen source facet, and all 65 facets occur. Therefore the simplex sum has no internal pole and only the physical facet denominator.

The complete canonical numerator is the exact polynomial arithmetic circuit

\[
N_{C_8}(Y)
=
\left(\prod_{f=1}^{65}q_f(Y)\right)
\sum_{s=1}^{255}
\frac{1}{|\det Z_s|}
\prod_{i=1}^{16}\frac1{\lambda_{s,i}(Y)}.
\]

Pairwise internal-residue certificates prove polynomiality. Its degree is

\[
65-16=49.
\]

This is a complete exact representation supporting evaluation and residues; no fitted coefficients or unverified monomial expansion is used.

## Cyclic orientation

One cyclic step has ambient-coordinate sign (+1) and contour-variable sign (-1). Transport of the integration-cycle orientation contributes the second (-1), so the canonical scalar has character (+1). All 255 rotated simplex determinants satisfy the labelled sorting-sign audit.

## Consequence

The first gate of the C8 nontransverse specialization program is closed. The next object is the 288-occurrence Leray/relative-current complex derived from this numerator and contour—not from denominator incidence alone.

Allocator claim: `seqclaim-ebcddb2edf7e38986a747356`.

Artifacts:

- `research/benincasa/results/eight-site-canonical-contour-packet.json`;
- `research/benincasa/results/eight-site-canonical-regular-triangulation.json`;
- `research/benincasa/results/eight-site-canonical-numerator-certificate.json`;
- `research/benincasa/results/eight-site-canonical-cyclic-orientation.json`.
