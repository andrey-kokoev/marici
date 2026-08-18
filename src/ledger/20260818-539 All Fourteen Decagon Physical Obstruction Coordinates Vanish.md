---
id: 539
date: 2026-08-18
title: All Fourteen Decagon Physical Obstruction Coordinates Vanish
---

# All Fourteen Decagon Physical Obstruction Coordinates Vanish

Entry 538 found the free obstruction group

\[
H_2(N_{m Cut}^{(10)};\mathbb Z)\cong\mathbb Z^{14}
\]

and proved that the native Thom lines cancel the local (S_3) sign character.
This entry evaluates the actual framed physical comparison rather than only
its signs.

Every one of the fifty-five compatible Cut triples is a complete
quadrangulation of the decagon.  Direct planar enumeration gives the same
region profile in every case:

\[
\boxed{(4,4,4,4)}.
\]

Hence each triple overlap is the tensor product of four already fixed
primitive four-point units.  There is no new coefficient object at the top
intersection.  For every one of the six restriction orders:

- all four lower-arity unit coefficients are (+1);
- all three source-derived restriction coefficients are (+1);
- the Koszul permutation character is (operatorname{sgn}(sigma)); and
- the three odd Thom normals contribute the same
  (operatorname{sgn}(sigma)).

Therefore all (55\cdot6=330) ordered composites are exactly (+1).  Relative
to the fixed positive composite, the physical obstruction 2-cochain is
literally

\[
\boxed{0in C^2(N_{m Cut}^{(10)};\mathbb Z)}.
\]

It follows without choosing a basis for top homology that its fourteen
coordinates are

\[
\boxed{(0,ldots,0)in\mathbb Z^{14}}.
\]

Thus the decagon framed physical Cut data have no global (H^2) descent
obstruction.  This is stronger than cancellation after pairing with selected
cycles: the cocycle vanishes on every top simplex.

The scope remains the framed physical line assembled from the already rigid
(n=4,6,8) factors.  A full loaded decagon PC/Čech chain map has not been
enumerated.  The next gate is to prove that lower-arity rigidity makes the
framed gluing space contractible, or else construct the full loaded decagon
totalization and verify its restrictions cell by cell.

The executable audit is
`research/voevodsky/check_n10_physical_cut_obstruction.py`.
