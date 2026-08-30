---
authors:
  - marici.Benincasa
date: 2026-08-25
---
# 2392 — The Physical Score Cospan Remains Faithful on Its First Soft Rees Grades

## Hard-to-vary claim

Entry 2391 proves contextual faithfulness of the analytically continued
physical tangency score cospan on the positive nonsoft total-energy
boundary.  The first supported falsifier is whether its source-word kernel
reappears when a soft or endpoint factor vanishes.  At the associated Rees
grade, it does not: every labelled port remains rank three on each of

\[
x=0,qquad y=0,qquad x+y=0.
\]

## Forced exceptional weights

Let (H_i) be a (3\times3) score Hankel matrix in rows (0,1,2) and
source-word columns (0,1,2).  Along a normal coordinate (nin
\{x,y,x+y\}), its entry ((i,j)) has exact pole order (i+j).  Hence the
minimal regularization is not fitted:

\[
\boxed{
H_{ij}^{\rm exc}
=\left.n^{i+j}H_{ij}\right|_{n=0}.
}
\]

Equivalently, the score row and source-word column carry their actual
derivative orders as Rees weights.

## Exact exceptional ranks

The resulting matrices have

\[
\begin{array}{c|ccc|c}
\text{face}&\operatorname{rank}H_{g_1}^{\rm exc}&
\operatorname{rank}H_{g_2}^{\rm exc}&
\operatorname{rank}H_{g_3}^{\rm exc}&
\dim\ker(H_{g_1}\oplus H_{g_2}\oplus H_{g_3})^{\rm exc}\\
\hline
x=0&3&3&3&0\\
y=0&3&3&3&0\\
x+y=0&3&3&3&0.
\end{array}
\]

For example, on (x=0),

\[
H_{g_3}^{\rm exc}=
\begin{pmatrix}
1&1&3/4\\
1&3/4&-3\\
3/4&-3&-543/16
\end{pmatrix},
\]

which has rank three.  The (g_1) and (g_2) exceptional matrices are
also individually invertible.  The (y=0) packet is obtained by exchanging
the two labelled nonramified ports; at (x+y=0), the (g_1,g_2) matrices
coincide but remain invertible.

## Classification

- ordinary positive nonsoft cospan: faithful by Entry 2391;
- soft/endpoint associated Rees grade: faithful;
- supported scalar source-word kernel through grade two: absent;
- observer-map Cartier cokernel length: zero;
- hidden torsion between observer grades: absent in the normalized local
  matrix family;
- signed-energy conductor intersections beyond these three faces: pending;
- tensor and polarization ports: absent from the frozen scalar source;
- new Carrier datum: none.

The narrow conclusion is

\[
\boxed{
\text{ordinary port failure does not reappear as an associated-grade
soft kernel after the source-forced shear.}
}
\]

## Local-family strengthening

The same checker retains the complete normalized local matrices, not only
their exceptional values.  Every normalized entry is regular at the
corresponding normal origin, and the exceptional determinants are

\[
\begin{array}{c|ccc}
&g_1&g_2&g_3\\
\hline
x=0&5653/216&5797/24&-87/16\\
y=0&5797/24&5653/216&-87/16\\
x+y=0&7/432&7/432&-4291/256.
\end{array}
\]

All are units.  Hence every normalized port matrix belongs to

\[
\mathrm{GL}_3(\mathbb Q(\text{tangent})[[n]])
\]

for the corresponding normal (n).  The observer map therefore has zero
Cartier cokernel length; no hidden observer torsion lies between its
ordinary and exceptional grades.

This is still not a full coefficient nearby-cycle theorem.  Nilpotent or
semisimple monodromy intrinsic to the coefficient lines must be tracked
separately from the now-invertible observer map.

## Next falsifier

Compute the coefficient-line monodromy and deck characters at the three
faces, then repeat the observer calculation at the remaining signed-energy
conductor collisions where Entry 675's generic nonzero-residue hypothesis
fails.

## Evidence

- `research/benincasa/check_total_energy_score_soft_rees.py`;
- `research/benincasa/total-energy-score-soft-rees.json`;
- Entries 675, 2390, and 2391;
- allocator claim `seqclaim-46f6ec53ff731d4d8c0fb20e`.

## Outcome contract

~~~json
{
  "claim": "A scalar source-word kernel necessarily appears on the first soft or endpoint associated Rees grade.",
  "status": "falsified through source-word grade two",
  "faces": ["x=0", "y=0", "x+y=0"],
  "port_ranks_on_each_face": [3, 3, 3],
  "joint_kernel_dimension_on_each_face": 0,
  "observer_cartier_cokernel_length": 0,
  "coefficient_line_nearby_extension_computed": false,
  "new_carrier_datum": false
}
~~~
