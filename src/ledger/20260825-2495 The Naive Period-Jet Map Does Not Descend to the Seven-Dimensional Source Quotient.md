---
author: marici.Benincasa
date: 2026-08-25
---

# 2495 — The Naive Period-Jet Map Does Not Descend to the Seven-Dimensional Source Quotient

## Question

Can Entry 2493's ten integrated Taylor coefficients be quotiented directly
by the three exact source relations to obtain a rank-seven physical period
observer?

Sequence claim: `seqclaim-9c1d86b63ad95b519a19b3ef`.

## Frozen conventions

Use the source ordering

\[
(L_1,L_2,L_3,D_1,D_2,D_3,C_{12},C_{13},C_{23},U)
\]

and the exact relations

\[
\begin{aligned}
p_3(D_1+D_3+C_{13})-p_2(D_1+D_2+C_{12})&=0,\\
p_3(D_2+D_3+C_{23})-p_1(D_1+D_2+C_{12})&=0,\\
p_3U-(D_1+D_2+C_{12})&=0.
\end{aligned}
\]

The initial implementation used a different quadratic serialization.  That
convention defect was repaired before the test reported here.

## Descent test

If the integrated period-jet row were already a covector on the source
quotient, it would annihilate all three relation vectors.  Instead, the
maximum relative residuals are

\[
\begin{array}{c|ccc}
N&r_1&r_2&r_3\\
\hline
28&0.4685&0.2601&1.0000\\
36&0.4697&0.2609&1.0000\\
48&0.4693&0.2605&1.0000.
\end{array}
\]

They are stable and of order one.  The failure is not quadrature error.

Selecting the seven columns

\[
(L_1,L_2,L_3,D_1,D_2,D_3,C_{12})
\]

still gives numerical rank seven, but that number is inadmissible because
the preceding map does not descend.

## Type diagnosis

The source relations live among Cayley--Menger insertion/cohomology classes.
The period Taylor coefficient at order two or three is not simply the period
of the corresponding primitive insertion.  Differentiating
\(1/\prod q\) also produces products of lower derivatives and their exact
coherence terms.

Therefore

\[
\boxed{
\text{normal monomial label}
\ne
\text{source insertion class without an adapter}.}
\]

## Narrow result

\[
\boxed{
\text{The direct ten-to-seven quotient of the integrated Taylor jet is
mistyped and rejected.}
}
\]

Entry 2493's numerical statement about ten Taylor coefficient functions
survives.  What fails is its direct use as a rank-seven source observer.
No new Carrier support is implicated.

## Durable evidence

- `research/benincasa/marici-gm/src/bin/integrated_period_normal_jet.rs`;
- `research/benincasa/integrated-period-source-relation-descent.json`;
- `research/benincasa/generic-lower-interaction-class-faithfulness.json`;
- Entries 2491 and 2493.
- epistemic event `ev-000000003437-b4bbaaa8-ace8-4a1e-9610-5eccb575b7da`.

## Next falsifier

Derive the insertion-to-jet adapter by differentiating the frozen integrand
with source labels retained.  Separate primitive insertion columns from
products of lower insertions, then reduce the complete packet by the same
twisted-de-Rham exact relations used to obtain the source quotient.  Only
the resulting descended map may be tested for rank seven.
