---
title: "The First-Rees Physical Pairing Extends to Dihedral Occurrence Symmetry"
date: 2026-08-20
entry: 1136
status: established-supported-dihedral
sector: cosmology
---

# 1136 — The First-Rees Physical Pairing Extends to Dihedral Occurrence Symmetry

Sequence claim: `seqclaim-59386b936ee37321764d9a43`.

## Source-labelled reflection

Use the exact transition of Entry 756 under

\[
\sigma_{23}:G_{12}\longrightarrow G_{31}.
\]

It transports

\[
q_{\mathcal G_{12}}\mapsto q_{\mathcal G_{31}},
\qquad (a,b)\mapsto(c,a)=(b,a).
\]

For the canonical residue conventions,

\[
\operatorname{Res}_{G_{12}}=da\wedge db,
\qquad
\operatorname{Res}_{G_{31}}=dc\wedge da,
\]

and

\[
\sigma_{23}^*(dc\wedge da)=db\wedge da=-da\wedge db.
\]

Thus the Poincaré-residue orientation character is \(-1\).

The local branch coordinate is normalized by the source initial form

\[
K_1=-16T+\cdots,
\]

which fixes the sign of \(T\) and transports the ordered sheets without an
additional arbitrary sign.

## Pairing

Both Entry 1133's coefficient covector and Entry 1131's oriented physical
boundary inherit the residue-orientation sign:

\[
\omega\mapsto-\omega,
\qquad
\partial\gamma_{CM}\mapsto-\partial\gamma_{CM}.
\]

Therefore

\[
\boxed{
\langle-\omega,-\partial\gamma_{CM}\rangle
=\langle\omega,\partial\gamma_{CM}\rangle
=\frac14.
}
\]

Applying the reflection twice restores both factors exactly.

## Consequence

Together with Entry 1135, the typed supported first-Rees object extends from
the cyclic group to the full dihedral occurrence group. The coefficient and
physical-boundary factors are matching sign lines; their evaluation is a
trivial-character scalar.

No chart is identified without transporting its labelled residue divisor,
retained coordinates, and orientation. No new carrier datum appears.

## Next falsifier

The local symmetry and support tests are now closed rationally. The next
nonredundant question is global sewing into the rank-twelve nearby-cycle
complex: determine whether the three dihedrally coherent local pairings are
the restrictions of one global supported class, rather than merely an
equivariant family of germs.

Evidence:

- `research/benincasa/checkers/rank12_e6_supported_pairing_reflection.py`;
- `research/benincasa/results/rank12-e6-supported-pairing-reflection.json`;
- Entries 753, 756, and 1131--1135.
