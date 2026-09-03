# The extremal Hasse cell is a five-vertex path, not complete bipartite

## Bold conjecture

The minimum two-demand cut has complete three-supply/two-demand topology \(K_{2,3}\).

## Falsification

The complete Hasse-neighbor graph has four, not six, edges. Its degrees are

\[
(1,2,1)\quad\text{on supplies},\qquad (2,2)\quad\text{on demands}.
\]

Hence the exact topology is the alternating path

\[
P_0-D_0-P_1-D_1-P_2.
\]

The central supply is shared by both demands; each endpoint supply is private. Two conjectured cross edges are absent, so the \(K_{2,3}\) conjecture is rejected.

## Surviving conjecture

This path is the irreducible branching cell. Its Hall system consists of two singleton inequalities and one collective inequality. Test whether the collective slack is strictly smaller than both singleton slacks. If so, the multi-demand constraint is independent and genuinely controls the extremum; otherwise the path cut reduces to singleton bounds.

## Disposition

The five-vertex path topology is verified exactly at fixed \(k=8\). It supplies a sharper local target for an all-order Hasse-Hall proof.
