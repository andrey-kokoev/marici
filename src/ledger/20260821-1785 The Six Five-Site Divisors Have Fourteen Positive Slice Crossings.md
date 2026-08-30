# 1785 — The Six Five-Site Divisors Have Fourteen Positive Slice Crossings

## Question

After repairing the auxiliary convention in Entry 1784, how many positive
real values of

\[
x=t^2>0
\]

lie on each of the six exact degree-six anomalous-threshold eliminants?

This is a real-algebraic support census. It does not by itself determine a
physical pinch, which additionally requires the correct Landau-multiplier and
relative-cycle intersection data.

## Exact method

For each saturated polynomial

\[
L_r(x)\in\mathbb Q(\sqrt5)[x],
\qquad \deg L_r=6,
\]

construct its Sturm chain over the ordered real field
(mathbb Q(\sqrt5)\). Signs of (a+b\sqrt5) are decided exactly by comparing
(a^2) with (5b^2), not by floating-point evaluation.

The positive-root count is

\[
N_r=V_r(0^+)-V_r(+\infty).
\]

## Result

In source representative order

\[
(g_3,g_4,g_5,g_{34},g_{45},g_{345}),
\]

the exact counts are

\[
\boxed{(1,2,4,1,3,3).}
\]

Therefore

\[
\boxed{\sum_r N_r=14.}
\]

Every source occurrence orbit is free under (C_5), so the labelled cyclic
assembly contains

\[
\boxed{5\times14=70}
\]

positive-real crossings of the frozen one-parameter slice.

## Scope

These 70 crossings are not 70 new carrier strata. They are real points on the
thirty occurrence-resolved coefficient divisors of Entry 1782.

Numerical root recovery also finds compatible real critical points and suggests
a nonuniform split of Landau-multiplier signs. Those signs are retained as
discovery output only. No physical discontinuity is claimed until the signs
and the source-cycle intersection are certified together.

## Evidence

- `research/benincasa/checkers/five_site_disjoint_mixed_pair_real_branches.py`
- `research/benincasa/results/five-site-disjoint-mixed-pair-real-branches.json`
- allocator claim: `seqclaim-f9c2cdbfea091e5d9dca530e`
