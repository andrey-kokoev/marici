---
id: 566
date: 2026-08-18
title: The Physical Half-Weight Lower Critical Rank Is Five but Infinity Is Resonant
authors:
  - marici.Nima
---

# The Physical Half-Weight Lower Critical Rank Is Five but Infinity Is Resonant

Entry 565's equivariant obstruction was conditional on the unmarked
tangential rank five persisting at the physical Cayley--Menger exponent
\(\tfrac12\). This entry tests that premise at critical-scheme level.

The tangential critical equations for the \(K\)-only master function contain

\[
\alpha\,\partial_aK,
\qquad
\alpha\,(\partial_b-\partial_c)K,
\]

with \(\alpha\ne0\). Over each exact finite field, set
\(\alpha=2^{-1}\). The saturated quotient on \(q_{g1}=0\) has

\[
\boxed{\dim\operatorname{Crit}(K^{1/2})=5.}
\]

The result replicates at:

- \(\mathbf F_{32003}\) and \(\mathbf F_{65521}\);
- generic kinematic points A and B;
- the soft fiber \(X_1=0\).

All six runs have the same standard monomials

\[
1,\ z,\ z^2,\ b,\ a.
\]

Thus the physical half-weight does not change the exact critical rank.

## Infinity qualification

This is not yet a theorem that the physical twisted cohomology is
five-dimensional. The restricted polynomial has quartic order at infinity,
and

\[
4\cdot\frac12=2\in\mathbb Z.
\]

Therefore the physical local system is resonant at infinity. Generic
critical-point concentration theorems cannot be applied without an explicit
boundary calculation. Extra cohomology may appear in other degrees while
preserving the Euler characteristic.

The correct conclusion is

\[
\boxed{
\text{physical critical rank}=5,
\qquad
\text{physical deck-odd cohomology rank still unproved}.
}
\]

Entry 565's character obstruction is consequently strengthened at the
critical level but remains conditional at the full cohomological level.

## Next gate

Compute the anti-invariant logarithmic de Rham complex on the resolved double
cover \(w^2=K|_{q_{g1}}\), including the four-component infinity divisor and
its conductor cycle. Its hypercohomology, not the critical quotient, decides
whether three additional odd classes survive away from the raw boundary
packet.

The executable audit is
\`research/benincasa/marici-gm/src/bin/generic_lower_sector_groebner_rank.rs\`
with the physical half-weight option.
