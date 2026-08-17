---
id: 398
date: 2026-08-17
title: The Three Connectors Assemble by Full Cech Coherence
---

# The Three Connectors Assemble by Full Cech Coherence

Entry 397 established the \(D03\) connector. Rotation by two vertices carries
it successively to the \(D25\) and \(D14\) connectors. The normalized
blowdown construction, lcm coefficients, and positive long-normal orientation
are transported by the labelled rotation, while Entry 388 makes the
reflection coherence automatic from uniqueness.

On the \(Q\)-associated grade, the three roofs have coordinates
\[
 e_{03}=(1,0,0),\qquad
 e_{25}=(0,1,0),\qquad
 e_{14}=(0,0,1).
\]
Their sum is
\[
 \Delta_Q=(1,1,1),
\]
which is exactly the boundary of the geometric relative-associahedral
relation cell from Entry 98:
\[
 d\mathcal K_{\rm rel}^{\rm PC}
 =\mathcal T_0^{\rm PC}
  +\mathcal T_1^{\rm PC}
  +\mathcal T_2^{\rm PC}.
\]

## The apparent factor of three

Every rotated roof contains the same labelled endpoint correction
\(-[\mathrm{top},v_+]\). A direct sum of the three local formulas therefore
counts the endpoint three times. This is not an index-three obstruction: the
three connector carriers have all three pairwise endpoint overlaps and their
common triple endpoint overlap.

Their overlap nerve is the full augmented two-simplex
\[
 C_2\longrightarrow C_1\longrightarrow C_0
 \longrightarrow \mathbb Z,
\]
with ranks
\[
 1\longrightarrow3\longrightarrow3\longrightarrow1
\]
and differential ranks \((1,2,1)\). Its nonzero Smith factors are all one.
Thus it is integrally exact and saturated. On the shared endpoint its
inclusion--exclusion multiplicity is
\[
 3-3+1=1.
\]
Pairwise overlaps alone would leave the assembly incomplete; the triple/top
coherence is essential.

## Consequence

The three local connectors assemble into one integral \(D_3\)-equivariant
map to the geometric three-road relation object. There is no integer torsion,
no division by three, and no residual cyclic holonomy in this assembly.

This closes the three-road overlap and top-coherence gate in the scoped
absolute occurrence-loaded support model. The next frontier is no longer
geometric gluing. It is to place the assembled connector into the complete
normalization/conductor source object, including both polarity branches and
both retained Tor grades, and then evaluate the resulting framed physical
class.

The executable audit is
research/voevodsky/check_three_connector_cech_assembly.py.
