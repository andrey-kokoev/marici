# 1878 — The Real Source-Sheet Triple Divisors Are Ordinary Folds

## Local question

Entry 1877 leaves two region-only divisors with real (+sqrt5) critical
points and positive loop-energy squares. Determine whether their local
singularities are ordinary folds or higher degenerations.

## Reduced local system

For every region-only representative, the wall equations leave two squared
variables

\[
x,qquad v.
\]

The fifth cover equation is linear in (x):

\[
G_x\,x+G_0(v,z)=0.
\]

After eliminating (x), the first cover equation becomes

\[
P_2(z)v^2+P_1(z)v+P_0(z)=0.
\]

An ordinary fold requires

\[
G_x\ne0,qquad P_2\ne0,qquad d\operatorname{Disc}_v(P)\ne0
\]

at the critical divisor.

## Exact certificate

For the two real source-sheet cases the pivots are

\[
\begin{array}{c|c|c}
&G_x&P_2\\
\hline
g_{123}\mid g_4\mid g_5
&1&\dfrac{-25+3\sqrt5}{32}\\[2mm]
g_{12}\mid g_{34}\mid g_5
&1&-\dfrac{35+4\sqrt5}{16}.
\end{array}
\]

Both are nonzero. Their quadratic-field norms are coprime to the
corresponding quartics. Entry 1875 proves the norm quartics squarefree, so the
branch discriminants cross transversely.

The same test also passes for the two complex-only source branches.
Therefore every one of the four saturated region-only divisors is locally an

\[
\boxed{A_1\text{ fold}.}
\]

## Consequence and scope

At each real (D_3) or (D_4) source-branch point, the local vanishing-cycle
space has rank one. Higher Milnor rank, an undeclared incidence stratum, or a
new carrier cell is not needed.

This still does not determine the intersection number of that vanishing
cycle with the analytically continued Bunch--Davies chain. A rank-one local
cycle may be physically invisible if the source contour has zero pairing.

## Next falsifier

Transport the source contour to the first real (D_3) fold from the
negative-(t) sheet and compute its oriented intersection with the rank-one
vanishing cycle. The only possible local outcomes are now zero or a
source-normalized nonzero integer.

## Durable verification

- `research/benincasa/marici-gm/src/bin/five_site_cyclic_triple_region_pilot.rs`
- `research/benincasa/results/five-site-cyclic-triple-region-census.json`
- allocator claim: `seqclaim-b9550e923aa00c27b2d1087c`
- epistemic event: `ev-000000002235-4bfe7fdd-9723-4808-8186-28cb40f49c32`
