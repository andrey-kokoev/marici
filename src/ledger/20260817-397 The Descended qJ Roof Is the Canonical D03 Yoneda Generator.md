---
id: 397
date: 2026-08-17
title: The Descended qJ Roof Is the Canonical D03 Yoneda Generator
---

# The Descended qJ Roof Is the Canonical D03 Yoneda Generator

Entry 396 constructed normalized blowdown and left one identification: whether
the descended corrected roof \(q_J\) represents the canonical \(D03\)
component of the support-filtration Yoneda class.

The support-level-two face poset of the labelled hexagon is especially rigid.
Its only faces are the top face and the three long facets
\[
 D03,\qquad D14,\qquad D25.
\]
The long diagonals cross pairwise, so no face contains two of them. Therefore
the normalized barycentric relative \(Q\)-carrier has the three primitive
edges
\[
 [\mathrm{top},D03],\quad
 [\mathrm{top},D14],\quad
 [\mathrm{top},D25]
\]
and has no normalized two-simplex whose boundary could produce a relation
among them.

After the normalized blowdown of Entry 396,
\[
 q_J=-[\mathrm{top},v_+]+[\mathrm{top},D03]
       +X_{D03}[D03,c].
\]
Projection to the \(Q\)-associated grade is therefore
\[
 \operatorname{gr}_2(q_J)=[\mathrm{top},D03],
\]
with coordinate vector \((1,0,0)\) in the ordered long-facet basis. It is
primitive and cannot be a boundary. The other two summands are precisely the
successive roof corrections: \(X_{D03}[D03,c]\) lies over the short-facet
grade \(F_1/F_0\), and \(-[\mathrm{top},v_+]\) lies over \(F_0\).
Their signs and coefficients were already forced by the loaded chain
identity.

Consequently the descended \(q_J\) roof is not merely some generic class
with the correct degree. It is the canonical \(D03\) basis component of the
Yoneda extension
\[
 0\longrightarrow F_0\longrightarrow F_1
 \longrightarrow F_2/F_0\longrightarrow F_2/F_1
 \longrightarrow 0.
\]

## Consequence for the connector

Entries 393--397 now supply, in the absolute unlocalized occurrence-loaded
support model:

1. the forced generic and closed coefficients;
2. the expanded logarithmic carrier and its Morse comparison;
3. an integral normalized blowdown counit;
4. identification of its generic roof with the canonical Yoneda generator.

Thus the \(D03\) connector exists in this model. Entry 388 then applies:
the connector is unique under the previously proved endpoint and degree
constraints, and its reflection defect vanishes. The separate fixed-beta
Cartier comparison remains the stated scope for converting its closed normal
line to the physical \([dX_{D03}]\) residue; no universal integral
\(U_{D03}\)-to-\(X_{D03}\) identification is added here.

The executable audit is
research/voevodsky/check_d03_descended_yoneda_roof.py.
