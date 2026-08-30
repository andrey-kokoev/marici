# 1885 — The Homogeneous Hexagon Slice Is Singular Before Landau Elimination

## Frozen test

Entry 1884 admits the six-site incidence

\[
g_{12}\mid g_{34}\mid g_{56}
\]

in nine source terms.  The next proposed step was to repeat the five-site
homogeneous cyclic Cayley--Menger elimination on a regular hexagon.

Before forming the cover equations, audit the routing Gram matrix itself.

## Exact obstruction

For the four cumulative routing vectors, the regular-hexagon pairing gives

\[
H_6=
\begin{pmatrix}
2&7/2&4&4\\
7/2&7&9&19/2\\
4&9&13&15\\
4&19/2&15&19
\end{pmatrix}.
\]

Exact arithmetic yields

\[
\det H_6=0,
\qquad
\operatorname{rank}H_6=3,
\]

with nonzero leading \(3\times3\) minor \(3/4\) and primitive null direction

\[
\boxed{(3,-4,3,-1)}.
\]

Therefore the operation used at five sites,

\[
c=H^{-1}b,
\]

is undefined on this homogeneous six-site slice.  Attempting it produces an
indeterminate final cover equation; that output is rejected rather than
interpreted as a Landau divisor.

## Narrow conclusion

\[
\boxed{
\text{The naive homogeneous five-to-six-site continuation is mistyped.}
}
\]

This does not falsify the six-site incidence or H2.  It shows that the
regular hexagon lies on a pre-existing Gram-degeneracy support and cannot be
used as a generic higher-arity falsifier without resolving its null routing
direction.

The changed behavior is geometrically meaningful: odd-site regular polygons
gave a nondegenerate routing block in the tested model, whereas the even-site
hexagon introduces an opposite-momentum relation.

## Corrected frontier

Two admissible continuations remain:

1. deform to generic six-site kinematics, derive the full-rank cover, and
   specialize only after the Landau object is typed;
2. derive a canonical quotient by the labelled null line
   \(\langle(3,-4,3,-1)\rangle\), including the induced measure and support
   maps, before performing the symmetric elimination.

The quotient may not be chosen merely for computational convenience.  Its
compatibility with occurrence labels, Cayley--Menger measure, and the nine
source completions must be derived first.

## Durable verification

- `research/benincasa/marici-gm/src/bin/six_site_disjoint_pair_triple_symmetric_landau.rs`
- `research/benincasa/results/six-site-disjoint-pair-triple-symmetric-landau.json`
- allocator claim: `seqclaim-1ba5245f35592803d1664371`
- epistemic event: `ev-000000002244-2a392d3a-6837-4798-b24a-4f6365208137`
