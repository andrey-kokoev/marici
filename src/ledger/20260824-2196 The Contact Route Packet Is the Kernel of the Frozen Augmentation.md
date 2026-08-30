---
authors:
  - marici.Benincasa
date: 2026-08-24
---
# 2196 — The Contact Route Packet Is the Kernel of the Frozen Augmentation

## Use only the source-defined star

The frozen correlator supplies eight independently defined deletion sectors
and one augmentation to the common readout. It does not supply differentials
between adjacent sectors. Restrict the augmentation to the six-dimensional
contact-route space, with grade-two and grade-three routes for each labelled
edge.

In the ordered route basis

\[
(a_{12},b_{12},a_{23},b_{23},a_{31},b_{31}),
\]

the contact augmentation is

\[
\epsilon_{\rm ct}=
\begin{pmatrix}
8C_{12}&-8C_{12}&0&0&0&0\\
0&0&8C_{23}&-8C_{23}&0&0\\
0&0&0&0&8C_{31}&-8C_{31}
\end{pmatrix}.
\]

At generic contact kinematics it has rank three. Therefore

\[
\boxed{
\ker\epsilon_{\rm ct}
=\mathbb Q\langle p_{12},p_{23},p_{31}\rangle,
\qquad p_e=a_e+b_e.
}
\]

This derives the three hidden packets from the actual augmented star. No
Boolean-cube differential, adjacent-sector map, or fitted cone is required.

## Type of the result

The packet is a relation among source ports before aggregation. It is not a
class of any individual graph sector, and it is not visible in the scalar
readout. The earlier failure to construct an inter-grade edge-erasure map is
therefore harmless for the existence of this kernel and decisive against
retyping it as adjacent-sector cohomology.

## Evidence

- `research/benincasa/correlator-augmented-star-architecture.md`
- `research/benincasa/edge12-intergrade-localization-audit.md`
- Entries 2172–2195
- `research/benincasa/checkers/contact_augmentation_kernel.rs`

