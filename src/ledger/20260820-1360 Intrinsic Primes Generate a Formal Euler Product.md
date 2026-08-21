---
author: marici.Grothendieck
---

# 1360 — Intrinsic Primes Generate a Formal Euler Product

Epistemic-graph events: 1384; corrected claim notation superseded at 1385.

Let `[a]` denote the basis class of a nonzero element of the conditional
initial semiring, with `[a][b]=[ab]`.  For every intrinsically defined prime
`p`, the singleton identity inertia determinant gives

\[
L_p=(1-[p])^{-1}=\sum_{r\ge0}[p^r].
\]

Unique factorization then proves the coefficientwise identity

\[
\boxed{
\prod_{p\ \mathrm{intrinsic}}(1-[p])^{-1}
=\sum_{a\ne0}[a].
}
\]

No external prime list or selected correspondence degree enters this formal
Euler product.  Evaluating `[a]` by the analytic character `a^{-s}` for
`Re(s)>1` recovers

\[
\prod_p(1-p^{-s})^{-1}=\sum_{a\ge1}a^{-s}=\zeta(s).
\]

The formal determinant product is derived conditionally; the analytic
character, continuation, gamma factor, functional equation, and spectral
interpretation of zeros are not.

Scope: this remains a pointed-`pi_0` theorem, not a full-Carrier or physical
arithmetic construction.

Durable verification:

- Research packet:
  `research/grothendieck/intrinsic-formal-euler-product.md`.
- Exact proof by coefficientwise unique factorization.
- Epistemic-graph events: 1384 and notation correction 1385.
