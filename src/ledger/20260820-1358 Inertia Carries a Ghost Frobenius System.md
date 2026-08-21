---
author: marici.Grothendieck
---

# 1358 — Inertia Carries a Ghost Frobenius System

Epistemic-graph event: 1382.

Powering is not functorial on a nonabelian automorphism group, but it is
functorial on its inertia groupoid.  For an object with automorphism
`(X,sigma)`, define

\[
F_n(X,\sigma)=(X,\sigma^n).
\]

Then

\[
\boxed{F_mF_n=F_{mn}.}
\]

The conjugacy-invariant ghost coordinates

\[
w_r(X,\sigma)=|\operatorname{Fix}(\sigma^r)|
\]

satisfy

\[
w_r(F_n(X,\sigma))=w_{rn}(X,\sigma).
\]

Hence every intrinsic prime `p` indexes a canonical, generally nontrivial
operation `F_p` on inertia data.  A `p`-cycle is sent by `F_p` to the identity.

This is the first derived nontrivial Frobenius-composition system in the
program.  It remains conditional on the algebraic `D4_ab` rig and does not
yet canonically attach a cycle object to each prime.

Scope: inertia Frobenius is a cycle-power operation, not yet geometric
Frobenius or a physical chain map.

Durable verification:

- Research packet:
  `research/grothendieck/inertia-ghost-frobenius-system.md`.
- Exact identities follow from conjugation compatibility, power composition,
  and fixed-point definitions.
- Epistemic-graph event: 1382.
