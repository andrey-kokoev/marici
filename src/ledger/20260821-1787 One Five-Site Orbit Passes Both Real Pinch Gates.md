# 1787 — One Five-Site Orbit Passes Both Real Pinch Gates

## Question

Entry 1786 leaves nine representative crossings with same-sign Landau
multipliers. Which of them also place all three internal energies appearing in
the two wall equations on the positive real contour after continuation to
negative total energy?

## Continued real sheet

Take

\[
t=-\sqrt{x}<0.
\]

The two wall equations imply

\[
y_e=-\frac52t>0,
\qquad
y_i+y_j=-mt=m\sqrt{x}>0.
\]

Writing (p=y_i y_j), the two roots (y_i,y_j) are both real and positive
exactly when

\[
p>0,
\qquad
m^2x-4p\ge0.
\]

## Exact sign audit

Use Entry 1786's rational-univariate representation

\[
p(x)=-\frac{b(x)}{a(x)}
\]

on each exact Sturm interval. The numerator and denominator of both (p(x))
and (m^2x-4p(x)) have no zero in the relevant interval, so their signs are
certified by exact endpoint evaluation in (mathbb Q(\sqrt5)).

For all fourteen positive-real crossings,

\[
m^2x-4p>0.
\]

The product (p) is positive at five crossings, but four of those five have
opposite-sign Landau multipliers. Exactly one crossing satisfies both gates:

\[
\boxed{
g_5,
\qquad
x\approx2.051388039104848,
\qquad
p\approx0.4272016373581.
}
\]

The decimals identify the certified isolating intervals; they are not used to
establish the signs.

## Labelled result

The (g_5) representative belongs to a free (C_5)-orbit. Therefore

\[
\boxed{
5\text{ labelled crossings pass both the multiplier and positive-internal-
energy gates.}
}
\]

The remaining 65 positive-real labelled crossings fail at least one of these
two necessary real-pinch conditions.

## Scope

This is stronger than a Landau-eliminant census but remains one step short of
a physical discontinuity theorem. The five surviving crossings must still
satisfy the complete Cayley–Menger signed-minor domain and have nonzero
oriented intersection between Entry 1783's canonical double-Leray germ and the
local Morse thimble.

No new carrier stratum is indicated. The surviving candidate is one cyclic
orbit inside the existing rank-30 coefficient object.

## Evidence

- `research/benincasa/checkers/five_site_disjoint_mixed_pair_real_branches.py`
- `research/benincasa/results/five-site-disjoint-mixed-pair-real-branches.json`
- allocator claim: `seqclaim-a67c32759e220cf08c222e90`
