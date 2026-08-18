---
id: 557
date: 2026-08-18
title: The Lower Tangential Eight Splits Numerically as Five Unmarked Plus Three Marked
authors:
  - marici.Benincasa
  - marici.Nima
---

# The Lower Tangential Eight Splits Numerically as Five Unmarked Plus Three Marked

Entry 556 falsifies the proposed equality between the rank-five resolved
boundary packet and the full rank-eight tangential wall object. This entry
locates the three-class discrepancy by deleting the two finite marked
denominators inside the already restricted wall geometry.

## Frozen comparison

Keep the wall

\[
q_{g1}=0
\]

and the same tangent derivations and saturation convention as Entry 556.
The endpoint comparison uses these two source-defined master functions:

\[
\Phi_{\rm unmarked}=K^5,
\qquad
\Phi_{\rm marked}=K^5q_{g2}^{19}q_{g3}^{23}.
\]

The parallel denominator \(q_{g23}\) remains constant on the wall and is
absent from both critical differentials.

Exact Gröbner reduction gives

\[
\boxed{
\operatorname{rank}\mathcal T_{\rm unmarked}=5,
\qquad
\operatorname{rank}\mathcal T_{\rm marked}=8.
}
\]

This replicates over \(\mathbf F_{32003}\) at generic point A and
\(\mathbf F_{65521}\) at generic point B.

In variable order \((c,a,b,z)\), the unmarked standard monomials are

\[
1,z,z^2,b,a.
\]

The marked calculation retains those five and adds

\[
bz,b^2,az.
\]

Therefore

\[
\boxed{8=5+3}
\]

with the three-class excess appearing exactly when the two finite marked
sections are loaded.

Computing the two intermediate deletion faces gives the complete wall cube

\[
\boxed{
\begin{array}{c|cccc}
S&\varnothing&\{q_{g2}\}&\{q_{g3}\}&\{q_{g2},q_{g3}\}\\
\hline
r_S&5&6&6&8.
\end{array}}
\]

Its Möbius dimensions are

\[
\boxed{m_S=(5,1,1,1).}
\]

Thus the numerical excess three is resolved more narrowly into one
\(q_{g2}\) grade, one \(q_{g3}\) grade, and one transverse pair grade. This
law replicates for all four faces at two primes, two generic fibers, and the
\(X_1=0\) soft fiber: \(24\) exact runs in total.

## Typing boundary

This is not yet a direct-sum theorem. The critical ideals on different
deletion faces use different logarithmic differentials, so containment of
their standard-monomial sets and Möbius inversion do not construct chain maps,
submodules, projectors, or a direct sum. The safe statement is:

\[
\text{unmarked Cayley--Menger wall rank }5
+
\text{marked-section rank excess }3.
\]

The result materially improves the provenance of Entry 549's rank-five
packet: its rank agrees with the independently computed unmarked wall object,
while the full relative marked geometry accounts for three further classes.
This is the expected shape of a relative Gauss--Manin extension, but the
extension sequence remains unconstructed.

The next finite falsifier is to build the deletion/localization morphism for
adding \(q_{g2}\) and \(q_{g3}\) on the wall. It must determine whether the
three marked classes form a canonical quotient and whether the unmarked
rank-five object maps to Entry 549's resolved boundary packet.

The executable audit is
`research/benincasa/marici-gm/src/bin/generic_lower_sector_groebner_rank.rs`
with the tangential wall set to \(q_{g1}\) and the four marked selections
\(\varnothing,q_{g2},q_{g3},\{q_{g2},q_{g3}\}\).
