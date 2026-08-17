---
id: 404
date: 2026-08-17
title: The PC-to-Jordan Square Comparison Is Unimodular and Equivariant
---

# The PC-to-Jordan Square Comparison Is Unimodular and Equivariant

Entries 402--403 isolated and then killed every rectangular Jordan
square-curvature channel. The remaining concern was whether a geometric PC
source class could disappear through a nonfaithful comparison map.

The relevant geometric source is not the later three-road \(D_3\) connector
complex. It is the occurrence-resolved eight-point PC complex of Entries
83 and 87. Its four fixed-mark square faces and the four Jordan comparison
faces are both the medial squares of the same octagon quadrangulation
cellulation. They therefore have identical canonical labels.

## Generator comparison

Index both square lattices by the four diameter faces. The comparison on
two-cells is
\[
\Phi_2:\mathbb Z^4_{\rm PC}\longrightarrow\mathbb Z^4_{\rm J},
\qquad \Phi_2=I_4.
\]
On the union of their boundary flips, use the identical labelled-edge map
\(\Phi_1=I\). Direct enumeration gives
\[
\partial_{\rm J}\Phi_2=\Phi_1\partial_{\rm PC}
\]
strictly on every square generator. The determinant of \(\Phi_2\) is one,
so the generator comparison is integral, saturated, and has zero kernel.

All sixteen octagon symmetries were applied to the oriented square faces.
Although the central half-turn fixes the four unoriented diameter-square
labels, it reverses every canonical face orientation and therefore acts by
\(-I\) on the square two-chains. The signed action has all sixteen distinct
transformations. Reflections reverse precisely the appropriate face
orientations. The same signed permutation matrices act on both sides, hence
\[
\Phi_2 g=g\Phi_2
\qquad(g\in D_8).
\]

## Curvature conclusion

Entry 87 proves that the complete occurrence-resolved PC polarity primitive
is \(D_8\)-equivariant and that the fixed-mark square ambiguities are filled;
Entry 83 gives zero loaded square/contact curvature. Entry 403 proves that
the corresponding four rectangular Jordan boundary values vanish. Since
the comparison on square generators is unimodular, there is no hidden
geometric kernel in this sector:
\[
\kappa_{\rm PC}=0
\xmapsto[\;\Phi\;]{\cong}
\kappa_{\rm J}=0.
\]

This closes the square-curvature comparison, including the invariant,
alternating, and standard \(D_8\) channels. It does not solve the distinct
atlas problem of gluing local primitive half-lines by invertible transitions,
nor does it construct a privileged smooth representative.

The next coherence locus is the residual octagon/Möbius cycle rather than
the four square faces. The appropriate test is additive: compare the
octagonal class in the residue/Gysin totalization with the Jordan
fundamental-formula homotopy. Multiplicative transition holonomy remains
mistyped unless new equivalences are supplied.

The executable audit is
\`research/voevodsky/check_pc_to_jordan_square_chain_comparison.py\`.
