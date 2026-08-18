---
id: 441
date: 2026-08-17
title: Eight-Point Cut Naturality Holds in the Cellular Kato Sector
---

# Eight-Point Cut Naturality Holds in the Cellular Kato Sector

Entry 87 supplies the complete generic occurrence-resolved PC primitive
\[
H_8^{\rm PC}=\sum_D\operatorname{Ins}^{\rm PC}_D(H_{6,D}^{\rm mark})+H_{\rm ct}^{\rm PC}.
\]
Entry 440 removes the last coefficient-carrier gap by extending the primitive
mixed-variance conductor kernel to all 12,425 loaded octagon stalks. We can
therefore apply the cellular sheet transform and logarithmic Thom trace to the
whole certificate, rather than only to one six-point boundary.

The octagon stalk system is exactly \(D_8\)-equivariant. The audit checks every
loaded cell under all 16 dihedral actions, for 198,800 cell actions, including
equivariance of the localization set and the conductor row \((1,-1)\).

The eight physical six-by-four diagonals form one \(D_8\)-orbit. Every link has
1,075 loaded cells, and the normal-suspension orientation of Entry 438 agrees
on all \(8\cdot369=2,952\) radial incidences. On each cut the five independent
primitive factors are all \(+1\): Entry 87's primary PC residue, conductor base
change, logarithmic Thom trace, Entry 436's physical six-point line, and the
four-point unit. Hence
\[
\operatorname{Res}_D\Phi(H_8^{\rm PC})
=\Phi(H_{6,D}^{\rm mark})\boxtimes\mathbf1_4
\]
with primitive coefficient \(+1\) for all eight side-ordered cuts.

Because the transform is exact and additive on this finite Kato carrier, it
also preserves the remainder of Entry 87's cut table: 24 compatible nested,
32 crossing ordered, eight contact, and 24 double residues remain zero.

Thus the first higher-multiplicity test succeeds:
\[
\boxed{\text{eight-point Cut naturality holds in the cellular fs/Kato sector}.}
\]
This is stronger than a single-boundary cardinality match: it transports the
complete off-collar homotopy and all eight physical residue squares.

The scope remains essential. This does not construct a raw global scheme-level
six-functor span, a privileged tubular current, or a resonant specialization
after forgetting nearby-cycle filtration. The next problem is coherence among
multiple compatible cuts: compare the two iterated restrictions on every
nested codimension-two face after the transform.

The executable audit is
research/voevodsky/check_n8_cut_naturality_after_sheet_transform.py.
