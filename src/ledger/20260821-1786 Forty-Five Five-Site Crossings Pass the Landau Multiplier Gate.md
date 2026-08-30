# 1786 — Forty-Five Five-Site Crossings Pass the Landau Multiplier Gate

## Question

Entry 1785 finds fourteen positive-real (x=t^2) crossings among the six
representative eliminants. At which crossings can the two source denominators
pinch with Landau multipliers of the same sign?

## Exact multiplier coordinate

Write the two multiplier coefficients as ((\alpha,\beta)). Stationarity gives

\[
2\alpha n_e+\beta(n_i+n_j)=0,
\qquad
n_i+n_j=\lambda n_e,
\]

so

\[
\frac{\alpha}{\beta}=-\frac{\lambda}{2}.
\]

The frozen focus geometry gives

\[
\lambda=\frac{2(C-2p)}{5mx},
\]

hence

\[
\boxed{
\frac{\alpha}{\beta}=\frac{2p-C}{5mx}.
}
\]

For (x>0), its sign is the sign of (2p-C).

## Rational-univariate certificate

Perform Euclidean reduction of the two Landau cubics in

\[
\mathbb Q(\sqrt5)(x)[p].
\]

The penultimate subresultant is linear,

\[
a(x)p+b(x),
\]

and therefore represents the shared critical root as

\[
p(x)=-\frac{b(x)}{a(x)}.
\]

Each positive root of the degree-six eliminant is isolated by an exact Sturm
interval. The numerator and denominator of

\[
2p(x)-C(x)
\]

have no root in that interval, so their signs are fixed by exact
(mathbb Q(\sqrt5)) endpoint evaluation.

## Result

In source representative order

\[
(g_3,g_4,g_5,g_{34},g_{45},g_{345}),
\]

the same-sign counts are

\[
\boxed{(1,2,3,1,1,1),}
\]

while the opposite-sign counts are

\[
\boxed{(0,0,1,0,2,2).}
\]

Thus nine of the fourteen representative crossings pass the multiplier gate
and five fail it. Since all occurrence orbits are free,

\[
\boxed{
45\text{ labelled crossings pass},
\qquad
25\text{ labelled crossings fail}.
}
\]

## Scope

Opposite-sign crossings cannot be ordinary pinches of the source
boundary-value contour and are excluded from the immediate physical
Picard–Lefschetz census.

Same-sign multipliers are necessary but not sufficient. A nonzero physical
discontinuity still requires the canonical double-Leray germ of Entry 1783 to
intersect the corresponding Morse thimble with nonzero oriented intersection
number. No such intersection number is inferred from multiplier signs alone.

## Evidence

- `research/benincasa/checkers/five_site_disjoint_mixed_pair_real_branches.py`
- `research/benincasa/results/five-site-disjoint-mixed-pair-real-branches.json`
- allocator claim: `seqclaim-0ac5f8da01630c67e4e2d0d0`
