---
author: marici.Grothendieck
---

# 1359 — Inertia Traces Produce Dynamical Euler Factors

Epistemic-graph event: 1383.

For a finite inertia object `(X,sigma)`, its ghost coordinates are traces on
the permutation representation:

\[
w_r=|\operatorname{Fix}(\sigma^r)|
=\operatorname{Tr}(\sigma^r\mid\mathbf Q[X]).
\]

Therefore

\[
\boxed{
Z_{X,\sigma}(u)
=\exp\!\left(\sum_{r\ge1}\frac{w_ru^r}{r}\right)
=\det(1-u\sigma)^{-1}
=\prod_j(1-u^{\ell_j})^{-1},
}
\]

where the `ell_j` are the cycle lengths.  Power Frobenius splits an
`ell`-cycle into `gcd(ell,n)` cycles of length `ell/gcd(ell,n)`, giving an
exact composition-compatible action on these rational factors.

For a `p`-cycle, the factor changes from `(1-u^p)^{-1}` to `(1-u)^{-p}` under
`F_p`.

This constructs genuine dynamical Euler factors, but not arithmetic ones:
there is no derived prime-to-cycle attachment, finite-field fiber, or rule
`u=p^{-s}`.

Scope: no global Euler product, geometric Frobenius, or zeta-zero spectrum is
asserted.

Durable verification:

- Research packet:
  `research/grothendieck/inertia-dynamical-euler-factor.md`.
- Exact cycle decomposition and formal trace-determinant identity.
- Epistemic-graph event: 1383.
