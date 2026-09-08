# 1827 — A Disjoint Region Pair Survives the Physical Pullback Gate

## Discovery and exact reduction

A bounded physical-loop scan of Entry 1826's seven disjoint-cut candidates
finds one candidate orbit:

\[
(g_{123},g_{125}),
\qquad
\partial g_{123}=\{2,4\},quad
\partial g_{125}=\{1,3\}.
\]

The source geometry has an involutive isometry exchanging these two labelled
cut pairs.  Its fixed line can be written

\[
L(q)=M_{14}+q(M_{23}-M_{14}).
\]

On this line the two wall sums agree identically.  The physical gradient
condition reduces to stationarity of one distance sum along the line.

## Exact parameter

After clearing a positive factor, the squared stationarity equation is

\[
(70+25\sqrt5)q^2
-(170+60\sqrt5)q
+(85+30\sqrt5)=0.
\]

It has exactly one root in \((0,1)\):

\[
q_*
=
\frac{17+6\sqrt5-\sqrt{81+35\sqrt5}}
{14+5\sqrt5},
\qquad
0.7067<q_*<0.7068.
\]

The exact interval checker proves opposite signs at the isolating endpoints
and a strictly negative derivative throughout the interval.  Since
\((q_*-1)q_*<0\), the root also passes the unsquared stationarity sign gate.

## Physical Landau conditions

The two focal-line Gram determinants are strictly positive on the isolating
interval.  Therefore neither region gradient vanishes.  The source isometry
and fixed-line stationarity give

\[
\nabla_\ell g_{125}=-\nabla_\ell g_{123},
\]

so the positive multiplier ratio is exactly one.  The wall equations set

\[
t
=-\frac{y_2+y_4}{3}
=-\frac{y_1+y_3}{3}<0,
\]

with all internal distances positive.

Hence

\[
\boxed{
(g_{123},g_{125})
\text{ is an exact smooth physical two-region Landau survivor.}
}
\]

## Scope and next gates

This certifies physical criticality only.  It does not yet establish a
nondegenerate pinch or a nonzero contribution of the frozen source form.
The next mandatory gates are:

1. transverse Hessian/Morse nondegeneracy;
2. separation from every remaining source wall;
3. exact summed source residue;
4. only then Picard--Lefschetz and coefficient interpretation.

The bounded null results for the other six disjoint profiles remain discovery
evidence, not exact exclusions.

## Evidence

- `research/benincasa/marici-gm/src/bin/five_site_disjoint_region_pair_physical_discovery.rs`
- `research/benincasa/results/five-site-disjoint-region-pair-physical-discovery.json`
- `research/benincasa/marici-gm/src/bin/five_site_disjoint_region_pair_symmetry_polynomial.rs`
- `research/benincasa/results/five-site-disjoint-region-pair-symmetry-polynomial.json`
- `research/benincasa/checkers/five_site_disjoint_region_pair_exact_survivor.py`
- `research/benincasa/results/five-site-disjoint-region-pair-exact-survivor.json`
- allocator claim: `seqclaim-57284b81e2ce7eded47808f6`