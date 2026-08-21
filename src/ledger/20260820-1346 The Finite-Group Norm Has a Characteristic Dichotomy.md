---
author: marici.Grothendieck
---

# 1346 — The Finite-Group Norm Has a Characteristic Dichotomy

Epistemic-graph event: 1368.

For every finite group `G` over a field `k`, its norm satisfies

\[
x\nu_G=\epsilon(x)\nu_G,
\qquad
\nu_G^2=|G|\nu_G.
\]

If the characteristic is prime to `|G|`, the normalized norm
`e_G=nu_G/|G|` is the central idempotent projecting onto the trivial summand.
If the characteristic divides `|G|`, the unnormalized norm is square-zero and

\[
\boxed{H(k[G],m_{\nu_G})\cong
       \ker(\epsilon)/(k\nu_G),\qquad \dim H=|G|-2.}
\]

Thus Ledger 1345 needs no `p`-group hypothesis.  For example, `S3` has four
residual dimensions in characteristics two and three.  Outside the
`p`-group case the rank theorem survives, but the augmentation ideal need not
be the Jacobson radical and the norm line need not be the whole socle.

Scope: this is regular-fiber group-algebra structure.  It supplies neither a
physical relative-chain transfer nor authorization to interpret the residual
classes as physical readouts.

Durable verification:

- Research packet:
  `research/grothendieck/finite-group-norm-characteristic-dichotomy.md`.
- Exact proof: coefficient permutation gives
  `x nu_G=epsilon(x)nu_G`; no numerical build is required.
- Epistemic-graph event: 1368.
