# The topological Möbius inverse needs a cross-label differential to survive completion

## Source-native inverse coefficients

Nima's divisor-chamber theorem constructs the Möbius coefficient without
using zeta zeros. For squarefree

\[
n=p_1\cdots p_r,
\]

the order complex of the proper divisor poset is a sphere of dimension
`r-2`, and its reduced Euler characteristic is

\[
\widetilde\chi\bigl(\Delta(\mathcal D(n)\setminus\{1,n\})\bigr)
=(-1)^r=\mu(n).
\]

Repeated-prime labels have zero Möbius coefficient, consistently with the
degeneration of the squarefree top class. Thus every finite coefficient of

\[
\frac1{\zeta(s)}=\sum_{n\ge1}\mu(n)n^{-s}
\]

has an independently source-derived topological origin.

## What this repairs

This answers the constructibility objection at finite label: the signs are
not fitted to the analytic inverse. They arise from factorization-path
coherence. A hostile scalar multiplier cannot simply change them while
claiming the same divisor-category source.

It does not solve the continuation problem. The divisor complexes are
separate fibers indexed by `n`. Their internal differentials compute each
individual Euler characteristic but provide no cancellation or transport
between distinct integer labels.

## Graded completion and its obstruction

Formally place the reduced chain complex of each proper divisor poset in a
graded direct sum and weight its `n`-fiber by `n^{-s}`. Its supertrace has the
desired scalar shadow

\[
\operatorname{Str}(N^{-s})
=\sum_n\mu(n)n^{-s}.
\]

But ordinary Hilbert norms forget the alternating signs. Absolute or
trace-class control is governed by the unsigned chain multiplicities, not by
their Euler-characteristic cancellation. The fiberwise topology therefore
does not improve the analytic convergence boundary by itself.

The missing operation must relate different labels. Concretely, one needs a
source-authorized differential or correspondence

\[
d_{n,m}:C_\bullet(n)\longrightarrow C_{\bullet+1}(m)
\]

whose completed pairing makes the signed supertrace stable while respecting
prime construction, divisor refinement, and reciprocal sewing. Without such
cross-label arrows, the proposed global complex is only a direct sum of local
explanations for `mu(n)` and inherits the classical summation problem intact.

## Relation to the Hardy inner record

In the Euler half-plane, the supertrace is the stable inverse of the zeta
filter. Extending it source-natively into the open critical half-plane would
exclude the Blaschke phase-delay packets of ledger 3823. But the previously
proved primitive-prime continuation theorem shows that scalar continuation
alone is RH-equivalent.

The new opportunity is narrower: derive cross-label cancellation before
scalar supertrace. A chain homotopy with completion-stable bounds could explain
why the inverse remains admissible; merely estimating the already aggregated
Mertens sum would return to the classical formulation.

## Finite falsifier

For the first nontrivial squarefree packet `p q r`, the proper-divisor complex
is a hexagonal circle. Every currently known moving-window, completed Euler,
and source-Gram coefficient system has trivial holonomy around this loop.
Therefore none supplies the required cross-label differential.

A candidate must exhibit an arrow between distinct endpoint labels, not only
an internal boundary map or a flat comparison among factorization orders. If
its scalar shadow is declared to be Möbius cancellation but its chain-level
map is absent, the construction fails.

## Revised target

The best current inverse programme is:

1. retain the divisor-poset chain complex producing each Möbius sign;
2. construct a source-derived cross-label differential before completion;
3. prove its contractions are compatible and bounded on compact subsets of
   each open sector;
4. recover the Möbius inverse only as the completed supertrace;
5. verify that a Blaschke-modified hostile cannot lift to this complex.

This is an actual new constructor request. It does not yet construct the
cross-label differential or prove RH.
