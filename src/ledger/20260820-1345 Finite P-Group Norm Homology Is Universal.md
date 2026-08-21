---
author: marici.Grothendieck
---

# 1345 — Finite P-Group Norm Homology Is Universal

Epistemic-graph event: 1367.

Let `K` be any nontrivial finite `p`-group and `A=F_p[K]`.  For the group norm
`nu_K=sum_(g in K)g`, multiplication satisfies

\[
x\nu_K=\epsilon(x)\nu_K,
\qquad
\nu_K^2=|K|\nu_K=0.
\]

Thus its kernel is the augmentation ideal `I`, its image is the norm line,
and

\[
\boxed{H(A,m_{\nu_K})\cong I/(F_p\nu_K),\qquad
       \dim H=|K|-2.}
\]

For `m` regular fibers the residual dimension is `m(|K|-2)`.  Therefore the
hostile modular norm is acyclic only for `K=C2`; nonabelian order-eight
kernels already leave six dimensions per fiber.  Group structure can still
change the Loewy filtration even though it cannot change this rank.

Scope: this is regular-fiber modular deck algebra.  It neither supplies the
missing physical relative-chain pushforward nor promotes the residual module
to a physical readout.

Durable verification:

- Research packet:
  `research/grothendieck/finite-p-group-norm-socle-homology.md`.
- Exact proof uses the coefficient-permutation identity
  `x nu_K=epsilon(x)nu_K`; no numerical build or checker is required.
- Epistemic-graph event: 1367.
