# Explicit odd H1 coherence obstruction

## Question

Is Grothendieck's explicit reciprocal-odd \(H_1\) generator the boundary of any declared representative-change 2-cell combination?

## Claim boundary

The audit covers the ten-edge finite fixture and its four declared detour triangles. It does not infer absence from an undeclared source complex.

## Generator

The labelled 1-cycle is

\[
h=-[w,-w]+[-w,w]+[w,a]-[-w,-a]-[-w,a]+[w,-a].
\]

Exact boundary computation gives \(d_1h=0\).

## Existing 2-cells

The four declared triangles span a rank-four image of \(d_2\). Appending \(h\) raises the rank by one, and the exact linear system

\[
d_2x=h
\]

has no solution. Hence \(h\) is not the boundary of any declared 2-cell combination.

## Exhaustive skeleton correction

The four declared triangles do not exhaust the triangles supported by the existing 1-skeleton. Enumerating all distinct composable triples gives 12 oriented triangles whose boundary span has rank 7, equal to the full cycle-space dimension.

The residual has the exact fill

\[
-[w,-w,-a]+[-w,w,a].
\]

Thus no new edge and no formally new triangle shape are needed. The two triangles are available simplices but are not among the declared source-authorized coherence cells.

## Disposition

The relative selector torsor remains one-dimensional in the declared complex. Its first missing datum is source admission of the reciprocal-odd triangle pair, together with modular and cutoff coherence. In the maximal simplicial closure of the existing skeleton the class vanishes.

## Verification

- `research/voevodsky/checkers/check_odd_h1_coherence_obstruction_v2.py`
- `research/voevodsky/results/odd_h1_coherence_obstruction_v2.json`
- `research/grothendieck/results/voevodsky-fixture-homology-characters.json`
