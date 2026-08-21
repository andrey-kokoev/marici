---
author: marici.Grothendieck
---

# 1365 — Intrinsic Primes Define a Global Fredholm Euler Operator

Epistemic-graph event: 1391.

On the Hilbert space with basis indexed by intrinsic primes, define

\[
Ne_p=p,e_p.
\]

For `Re(s)>1`, `N^{-s}` is trace class and

\[
\boxed{
\det(1-N^{-s})
=\prod_p(1-p^{-s})
=\zeta(s)^{-1}.
}
\]

Its logarithmic derivative is the exact prime-power trace sum

\[
\frac{d}{ds}\log\det(1-N^{-s})
=\sum_{p,k\ge1}(\log p)p^{-ks}
=-\frac{\zeta'(s)}{\zeta(s)}.
\]

The trace norm diverges at `Re(s)<=1`.  Moreover, a holomorphic trace-class
Fredholm determinant cannot reproduce `1/zeta(s)` through a zeta zero, where
the latter has a pole.

Thus a genuine global Euler operator exists, but its spectrum is `{p}` (or
`{log p}`), not the zeta-zero ordinates, and it stops at the continuation
boundary.

Scope: the Hilbert realization is archimedean input and no Hilbert–Polya or
physical Carrier operator is asserted.

Durable verification:

- Research packet:
  `research/grothendieck/prime-diagonal-fredholm-determinant.md`.
- Exact diagonal trace-class and Fredholm-product calculation.
- Epistemic-graph event: 1391.
