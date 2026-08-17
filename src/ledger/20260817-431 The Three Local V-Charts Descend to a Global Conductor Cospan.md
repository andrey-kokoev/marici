---
id: 431
date: 2026-08-17
title: The Three Local V-Charts Descend to a Global Conductor Cospan
---

# The Three Local V-Charts Descend to a Global Conductor Cospan

Entry 430 replaced the impossible projection to separated sheets by the
normalization–conductor target
\[
\mathfrak N_{\rm cond}=\{c<e_-,\ c<e_+\}.
\]
For each of the three rotated roads there is a unique local map
\[
h_i\mapsto c,qquad r_{i,-}\mapsto e_-,qquad r_{i,+}\mapsto e_+.
\]
These maps now descend globally.

Rotation cyclically permutes the road index and fixes the polarity label.
Reflection reverses the road index, exchanges the two rays, exchanges
\(e_-\) and \(e_+\), and fixes \(c\). The local maps commute with both
generators and are therefore \(D_3\)-equivariant.

Descent must retain the pairwise and triple intersections rather than simply
identify the three copies. Over each of \(c,e_-,e_+\), the Čech fiber is the
full augmented two-simplex
\[
\mathbb Z\longrightarrow\mathbb Z^3
\longrightarrow\mathbb Z^3\longrightarrow\mathbb Z.
\]
Its differential ranks are \((1,2,1)\), every nonzero Smith factor is one,
and its inclusion–exclusion multiplicity is \(3-3+1=1\). Hence all three
descent fibers are integrally acyclic and produce one global conductor point
and one copy of each normalization sheet, without division by three or
residual overlap homology.

On the right, the same full Čech nerve is exactly the assembly of Entry 398.
Entries 422–429 make each local map to the PC target ringed, fs monoidal, and
compatible with its logarithmic Thom trace. Thus the underlying finite/log
cospan and its right ringed projection are globally assembled.

This entry deliberately stops short of calling the entire cospan ringed. The
coefficient rings and restriction maps on
\(c<e_-,c<e_+\) have not yet been fixed as normalization–conductor stalks, so
there is not yet a left ringed morphism. Topological Čech descent cannot supply
those algebra maps. The next gate is exact: derive the three stalk rings from
the normalization–conductor square and test the local V-chart ring maps and
recollement sequence.

The executable audit is
`research/voevodsky/check_global_conductor_cech_cospan.py`.
