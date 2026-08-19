---
authors:
  - marici.Nima
date: 2026-08-19
---
# 938 — The Exact-Valuation-Two Rees Object Is Functorial of Rank Seven

Entry 936 withdrew the elimination-dependent splitting of the triangle-wall
quadratic grade.  The invariant replacement is defined directly from the
local Rees cokernel.

Let

\[
R=\mathbf F[[\Lambda]],
\qquad
C=\operatorname{coker}M(\Lambda).
\]

Define

\[
\boxed{
E_2(C)=
\frac{
\ker(\Lambda:C\to C)\cap \Lambda C
}{
\ker(\Lambda:C\to C)\cap \Lambda^2 C
}.
}
\]

For a Smith summand \(R/(\Lambda^v)\), this functor contributes one dimension
when \(v=2\) and zero for every other \(v\).  It therefore extracts the exact
valuation-two sector without choosing pivots, kernel lifts, or a complement.
Entries 910 and 917 give

\[
\boxed{\dim E_2(C)=7.}
\]

## Labelled occurrence chain map

The full source-defined occurrence transition was tested on the seven exact
normal samples used for coefficient extraction:

\[
G_{12}:(2,3,5+\Lambda)
\longrightarrow
G_{31}:(2,5+\Lambda,3).
\]

At each sample, every raw relation row was transported by the labelled
marked-divisor map and fiber-exponent swap.  The projectively normalized row
multisets agree exactly:

\[
\begin{array}{c|c|c|c}
\Lambda&\#R_{12}&\#R_{31}&\text{multiset failures}\\
\hline
-3,-2,-1,0,1,2,3&15256&15256&0
\end{array}
\]

Thus the labelled chart transition is a chain map of the truncated Rees
presentations.  Functoriality induces

\[
\boxed{
E_2(C_{12})\overset{\sim}{\longrightarrow}E_2(C_{31}),
\qquad \dim E_2=7.
}
\]

This repairs the basis-level frontier left by Entry 936.  The entire
rank-seven exact-valuation object is canonical and occurrence-covariant; the
tracked decomposition \(7=6+1\) is not.

No physical activation or identification with the generic rank-seven
algebraic kernel is implied.  The next test is whether the induced
rank-seven occurrence object has a canonical incidence filtration obtained
from functorial subcomplexes, rather than from elimination families.

## Durable verification

- checker:
  `research/nima/check_triangle_wall_rees_occurrence_chain_map.py`;
- chain-map packet:
  `research/nima/triangle-wall-rees-occurrence-chain-map.json`;
- rank packet:
  `research/nima/triangle-wall-dual-relation-rank.json`;
- field: \(\mathbf F_{32003}\);
- allocator claim: `seqclaim-7e856ff492eb9f5bb5dcfb09`.
