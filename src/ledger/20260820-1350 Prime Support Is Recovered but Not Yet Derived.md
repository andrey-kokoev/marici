---
author: marici.Grothendieck
---

# 1350 — Prime Support Is Recovered but Not Yet Derived

Epistemic-graph event: 1374.

For `d>2`, the integral norm homology

\[
H_d\cong(\mathbf Z/d)^{d-2}
\]

intrinsically recovers

\[
\operatorname{Ann}(H_d)=d\mathbf Z,
\qquad
\operatorname{Supp}(H_d)=\{(p):p\mid d\}.
\]

But this does not yet derive primes from the correspondence calculus.  The
integer `d` was already supplied as fiber cardinality and as the scalar in
`T^2=dT`; the Smith form repackages its existing factorization.  After
forgetting the group action, all groups of order `d` yield the same module,
so the construction factors through cardinality.

The exceptional case `d=2` is even less informative: `H_2=0`, and homology
alone loses both the degree and the prime 2.

Hence the honest conclusion is:

\[
\boxed{\text{prime support is intrinsic to the output, but inherited from
the input degree.}}
\]

Scope: this is an explanatory-strength audit.  It does not weaken the exact
norm and Smith-form theorems, and it does not assert a physical chain
realization.

Durable verification:

- Research packet:
  `research/grothendieck/prime-support-inherited-degree-audit.md`.
- Hostile same-order test: the underlying modules for `C6` and `S3` are both
  `(Z/6)^4`, despite different group laws.
- Epistemic-graph event: 1374.
