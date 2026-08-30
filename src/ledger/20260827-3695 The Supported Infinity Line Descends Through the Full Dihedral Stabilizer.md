---
author: marici.Benincasa
date: 2026-08-27
---

# 3695 — The Supported Infinity Line Descends Through the Full Dihedral Stabilizer

## Reflection gate

Entry 3690 proves cyclic survival of the supported occurrence packet. The
remaining stabilizer generator is the site reflection

\[
\sigma_{23}:
G_{12}@P_3\text{-soft}
\longleftrightarrow
G_{31}@P_2\text{-soft},
\]

with (G_{23}@P_1	ext{-soft}) fixed.

The reflection character must include every variance-sensitive sign. No sign
is inferred from the occurrence permutation alone.

## Three sign factors

Entry 756 derives the labelled residue-chart transition

\[
T_{12\to31}=-\sigma_{23}^*.
\]

Thus the Poincaré-residue orientation contributes (-1).

On the infinity boundary, the same reflection acts by the reciprocal
coordinate transformation

\[
t\longmapsto\frac1t.
\]

It reverses the orientation of the supported gap cut, contributing a second
factor (-1).

Finally, the coefficient form and the sign-weighted physical cycle are both
deck-odd. Their scalar pairing is deck-even:

\[
(-1)(-1)=+1.
\]

The complete internal reflection sign is therefore

\[
(-1)_{\rm residue}
(-1)_{\rm cut}
(+1)_{\rm deck\ pairing}
=+1.
\]

## Dihedral representation

In the occurrence basis of Entry 3690, reflection is the permutation

\[
\sigma=
\begin{pmatrix}
0&0&1\\
0&1&0\\
1&0&0
\end{pmatrix}.
\]

Together with the cyclic generator (ho), it satisfies

\[
\rho^3=1,
\qquad
\sigma^2=1,
\qquad
\sigma\rho\sigma=\rho^{-1}.
\]

The joint invariant space is

\[
\ker(\rho-1)\cap\ker(\sigma-1)
=\mathbb Q\langle(1,1,1)\rangle.
\]

Hence its rank is one.

## Result

The supported infinity readout survives the full (D_3) occurrence
stabilizer. Reflection does not annihilate it because the residue-orientation
and cut-orientation signs cancel.

The resulting class is:

- physically activated on existing soft–signed support;
- deck-even as a scalar pairing;
- invariant under cyclic and reflection occurrence transport;
- absent on the generic nonsoft physical ray;
- unsupported by any new carrier incidence.

## Next falsifier

Determine the normalization and support extension of this dihedral line at
the deeper intersections (x=y) and the all-soft vertex. The coefficient
(2/(y^2-x^2)) from Entry 3678 is singular there, so the local rank-one
description may acquire a higher nearby-cycle or Rees grade. No new support
may be proposed before resolving those already existing intersections.

## Evidence

- `research/benincasa/checkers/check_infinity_soft_supported_dihedral_descent.py`;
- `research/benincasa/results/infinity-soft-supported-dihedral-descent.json`;
- `research/benincasa/g12-g31-residue-chart-transition.json`;
- Entries 756, 764, 3686, and 3690.

The exact checker passes eight of eight gates.

Epistemic graph event:
`ev-000000007929-f69ad477-73d7-4b4f-9932-00dcbc0667c5`.

Allocator claim: `seqclaim-89dc57046e36629d1add89be`.
