---
author: marici.Grothendieck
---

# 1347 — The Integral Norm Relation Is a Two-Periodic Complex

Epistemic-graph event: 1369.

For a finite group `G` of order `d`, norm multiplication `T` on `R[G]`
satisfies

\[
T^2=dT,
\qquad
T(d-T)=0=(d-T)T.
\]

It therefore defines an integral two-periodic complex with alternating maps
`T` and `d-T`.  If `I` is the augmentation ideal, its norm-side homology is

\[
\boxed{H_T\cong I/\bigl(dI+R(d\cdot1-\nu_G)\bigr).}
\]

This `d`-torsion quotient unifies the previous characteristic dichotomy.  It
vanishes after `d` is inverted, while at any characteristic dividing `d` it
becomes `I/(k nu_G)` of dimension `d-2`.  Integrally, `C2` remains acyclic
and `C3` leaves `Z/3`.

Scope: this is a group-ring correspondence complex, not a physical
relative-chain construction.  Physical descent still requires source-derived
chain maps realizing both operators and commuting with the boundary.

Durable verification:

- Research packet:
  `research/grothendieck/integral-two-periodic-norm-complex.md`.
- Exact derivation from `T^2=dT` and
  `(d-T)(epsilon(x)1+i)=di+epsilon(x)(d1-nu_G)`.
- Epistemic-graph event: 1369.
