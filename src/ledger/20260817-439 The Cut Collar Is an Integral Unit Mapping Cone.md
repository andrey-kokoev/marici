---
id: 439
date: 2026-08-17
title: The Cut Collar Is an Integral Unit Mapping Cone
---

# The Cut Collar Is an Integral Unit Mapping Cone

Entry 438 isolated two copies of the 1,075-cell \(D_{05}\) carrier inside the
loaded octagon: the unmarked Cut facet \(U\) and the degree-shifted copy \(N\)
in which the Cut is marked. The PC normal differential removes that marking.
On every cell it is a unit
\[
\epsilon:N\longrightarrow U,\qquad \epsilon_{(F,H)}=\pm1.
\]

The signs are not decorative. For every internal radial or marking-removal
arrow, the two routes through the normal bridge cancel. The checker verifies
3,470 such \(d^2\)-squares: 1,735 radial and 1,735 marking squares. After the
cellwise unit reorientation supplied by \(\epsilon\), the collar differential
is exactly
\[
\operatorname{Cone}(\operatorname{id}_{C_{D_{05}}}).
\]
It is therefore integrally contractible. The contraction uses only diagonal
units, so it creates no torsion.

The same bridge commutes stalkwise with the primitive conductor row
\((1,-1)\). Thus tensoring with the mixed-variance conductor kernel does not
remove the contraction and does not create a hidden kernel in the normal
direction.

This gives the first genuine extension constraint. The primitive six-by-four
line cannot be promoted to an eight-point cycle by a representative supported
only on the closed Cut facet and its marked normal copy: that entire collar is
acyclic. Any eight-point extension must have nonzero components on cells not
containing \(D_{05}\), whose differential cancels the primitive normal demand.

This is not yet a no-go for Cut naturality. It converts the problem into a
relative lifting problem with a sharp support requirement. The next gate is to
enumerate the off-collar cells incident to the Cut collar and compute whether
their integral image contains the primitive normal generator.

The executable audit is
research/voevodsky/check_n8_cut_normal_mapping_cone.py.
