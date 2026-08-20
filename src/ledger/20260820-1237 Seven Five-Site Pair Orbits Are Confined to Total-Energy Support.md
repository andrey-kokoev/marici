# Entry 1237 — Seven Five-Site Pair Orbits Are Confined to Total-Energy Support

## Frozen input

Use the 49 compatible labelled pair orbits admitted by Entry 1236. On the cyclic physical slice, write the total-energy wall as

\[
q_G=5t
\]

and a connected-region wall as

\[
q_A=|A|t+y_i+y_j,
\]

where \(i,j\) are the two labelled cut occurrences of the connected region \(A\).

## First algebraic gate

Two source-derived pair classes force \(t=0\) before any Landau stationarity equation is imposed.

First, every pair containing \(G\) obeys

\[
q_G=0\quad\Longrightarrow\quad t=0.
\]

There are five such free \(C_5\)-orbits.

Second, suppose two distinct connected regions have the same two cut occurrences. For the five-cycle they are complementary, so their cardinalities are unequal. Their two wall equations have the form

\[
|A|t+y_i+y_j=0,
\qquad
(5-|A|)t+y_i+y_j=0.
\]

Subtracting gives

\[
(2|A|-5)t=0.
\]

Since \(2|A|-5\neq0\), these pairs also force \(t=0\). There are two such free \(C_5\)-orbits.

## Exact census consequence

Therefore

\[
\boxed{
7\text{ of }49\text{ compatible pair orbits}
}
\]

or equivalently

\[
\boxed{35\text{ of }245\text{ labelled compatible pairs}}
\]

cannot generate a nonzero-\(t\) Landau factor.

The remaining search has

\[
\boxed{42\text{ pair orbits}}
\]

before stationarity and boundary-admissibility tests.

## Narrow interpretation

This is a necessary-support elimination only. It does not assert that the seven classes possess a Landau solution at \(t=0\), and it does not assert that any of the remaining 42 classes possesses one.

The result excludes only a new nonzero-\(t\) factor from these seven source classes. Their possible support is confined to the already frozen total-energy locus and its marked intersections.

## Artifact update

`research/benincasa/results/five-site-compatible-landau-subsets.json` now preserves, for every representative, its exact walls, cut supports, source multiplicity, and first-gate disposition. The checker no longer emits the entire packet to stdout.

## Next falsifier

The frozen census contains no pair of distinct one-cut walls, so such a pair is not an admissible next test. Solve instead the source-present mixed pairs

\[
q_e=5t+2y_e,
\qquad
q_A=|A|t+y_i+y_j,
\]

separately for \(e\in\{i,j\}\) and \(e\notin\{i,j\}\). Retain signed roots and exact labelled routing data, and compare every elimination factor with the one-wall polynomial and existing incidence supports.
