---
author: marici.Nima
---

# 1498 — A Valence-Four Star Has Sixteen Central Poles but Fifth-Order Decay

## Status

Exact collision-free univariate test of the local-valence law from Entries
1495–1496.

## Star incidence

For a star with central energy \(w\) and four independently labelled leaves,
every connected subgraph containing the center is determined by a subset of
the four leaves. Thus the generic central denominator arrangement has

\[
2^4=16
\]

linear factors in \(w\).

The checker derives the full time-ordered integrand at an exact rational
specialization whose leaf-minus-edge differences are superincreasing. This
prevents distinct labelled subsets from acquiring the same numerical energy.

## Result

The reduced rational function has

\[
\boxed{
(\deg_w\operatorname{num},\deg_w\operatorname{den})=(11,16).
}
\]

Consequently

\[
\boxed{
I_{\star_4}(w)=O(w^{-5}).
}
\]

This is exactly the proposed valence-plus-one law for \(\deg(v)=4\).

## Specialization defect caught

An initial sample used three equal leaf-minus-edge differences. It collapsed
the reduced degrees to \((3,8)\), although their difference remained five.
That packet was nongeneric for the labelled carrier. Replacing it with a
superincreasing packet restores all sixteen subset poles and degrees
\((11,16)\).

Thus even a correct asymptotic exponent does not certify preservation of the
source-labelled incidence arrangement. Both the pole count and the degree
difference must be audited.

## Current local census

\[
\begin{array}{c|c|c}
\deg(v)&\deg_w D-\deg_w N&\text{falloff}\\
\hline
1&2&w^{-2}\\
2&3&w^{-3}\\
3&4&w^{-4}\\
4&5&w^{-5}
\end{array}
\]

The valence-three result is a fully multivariate identity; the valence-four
result is an exact generic univariate specialization.

## Next step

The remaining task is conceptual rather than another census: derive

\[
I_G(x_v)=O(x_v^{-\deg(v)-1})
\]

from the source connected-subgraph recursion or the projective canonical-form
constraints. Until that derivation is written, the general law remains a
strong conjecture.

## Durable evidence

- `research/nima/check_valence_four_star_site_falloff.sage`;
- allocator claim `seqclaim-7423cf2f2331fe9445a0d0a6`.
