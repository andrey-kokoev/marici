# C8 rank-four minimal-circuit attachment graph

## Purpose

This audit asks how far source sewing can proceed using only equality of labelled minimal-circuit boundaries. It deliberately stops before assigning residue signs or a physical relative current.

## Construction

For each of the 288 labelled rank-four occurrences, enumerate every primitive support-minimal dependence

\[
\sum_{a\in S}c_aN_{y,a}=0.
\]

Normalize the global sign by ordering the labelled pairs \((q_a,c_a)\). Equal normalized expressions define one circuit-support vertex. Attach each occurrence to every circuit it contains.

This equality relation is source-labelled and does not depend on a nullspace basis.

## Result

\[
|V_{\rm occ}|=288,
\qquad
|V_{\rm circ}|=182,
\qquad
|E|=1520.
\]

The attachment multiplicities of circuit vertices are

\[
\begin{array}{c|rrrrrrrrrrr}
m&1&3&4&5&8&10&12&16&32&42&64\\
\#&32&32&40&16&16&8&8&16&4&8&2.
\end{array}
\]

There are precisely two connected components of shape \((144,91)\). One cyclic step exchanges them and two steps preserve them. The graph cycle rank is (1052).

The sharp obstruction is the multiplicity-one sector:

\[
32\ \text{private circuit supports},
\qquad
32\ \text{with mixed regulator sign}.
\]

No second occurrence carries an equal labelled boundary against which any of these 32 can cancel.

## Interpretation boundary

This rejects only the pairwise-identical-support sewing model. It does not reject higher Čech, Orlik--Solomon, global-residue, or physical-current coherence. Those require explicit source maps and cannot be inferred from this graph's large cycle rank.

## Artifacts

- `checkers/eight_site_rank4_circuit_attachment_graph.py`
- `results/eight-site-rank4-circuit-attachment-graph.json`
