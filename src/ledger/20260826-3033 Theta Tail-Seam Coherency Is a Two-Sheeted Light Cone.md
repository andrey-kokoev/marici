---
title: "Theta Tail-Seam Coherency Is a Two-Sheeted Light Cone"
date: 2026-08-26
sequence: 3033
author: marici.Grothendieck
status: finite-exact-theorem
---

# 3033 — Theta Tail-Seam Coherency Is a Two-Sheeted Light Cone

Let (U) and (V) be the half-line transforms of the two reciprocal theta tails. Their powers and the complex transform of the straddling-seam convolution assemble into

\[
H=
\begin{pmatrix}
|U|^2 & UV\\
\overline{UV} & |V|^2
\end{pmatrix}.
\]

This is a positive rank-one coherency matrix. In Stokes coordinates,

\[
S_0=|U|^2+|V|^2,
\qquad
S_1=2\operatorname{Re}(UV),
\]

\[
S_2=-2\operatorname{Im}(UV),
\qquad
S_3=|U|^2-|V|^2,
\]

its determinant identity is

\[
S_0^2=S_1^2+S_2^2+S_3^2.
\]

Completed tail sum and complex seam coherence retain (S_0,S_1,S_2). Hence they determine

\[
|S_3|=\sqrt{S_0^2-S_1^2-S_2^2}.
\]

Only the sign of the Krein coordinate remains. Reciprocal exchange fixes the first three coordinates and reverses (S_3). Thus the continuous antisymmetric kernel of the linear cell observation collapses, on the physical rank-one source image, to a two-sheeted orientation fiber.

After normalization by (S_0), the spatial comparison vector lies on the unit sphere. This is the exact geometric meaning of the previously intuited circle: it is a coherence sphere for two reciprocal sectors, not a circle of zero locations.

The remaining RH-bearing conjecture is sheet preservation: theta/Tate dynamics initializes a definite sign of (S_3) in each open sector and cannot reach (S_3=0) before the unitary seam.

Scope: this exact theorem reconstructs magnitude and reduces the fiber to two signs. It does not select a sign or prove sheet preservation.

## Durable verification

- Packet: `research/grothendieck/theta-tail-seam-coherency-is-a-two-sheeted-light-cone.md`
- Exact checker: `research/grothendieck/checkers/theta_tail_seam_coherency_light_cone.py`
- Result: `research/grothendieck/results/theta_tail_seam_coherency_light_cone.json`
- Graph event: `ev-000000005962-161e5486-102b-40ae-b532-d0b84a38e703`
- No build was run because the operator's standing prohibition remains active.
