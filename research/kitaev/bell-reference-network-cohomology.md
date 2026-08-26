# Bell-reference networks separate common-mode and measurement faults cohomologically

Owner: `marici.Kitaev`

## Bounded question

What exact Carrier object organizes logical block faults, relative Bell records,
trusted anchors, and comparison-measurement faults in a reference network?

## Comparison complex

Let \(G=(V_G,E_G)\) be the graph of Bell comparisons and let

\[
P=\mathbf F_2^{2k}
\]

be the logical Pauli-label space of one mixed-boundary block. The comparison
network is the cochain complex

\[
C^0(G;P)\xrightarrow{\delta}C^1(G;P),
\qquad
(\delta e)_{ij}=e_i+e_j.
\]

For \(n\) vertices, \(m\) edges, and \(c\) connected components,

\[
\dim H^0(G;P)=2kc,
\qquad
\dim H^1(G;P)=2k(m-n+c).
\]

The first group is the common-mode Pauli kernel. The second is the space of
edge-record patterns not explainable by any assignment of block Pauli labels.

## Anchors as a relative condition

Let \(A\subseteq V_G\) be the trusted anchor set and fix \(e_a=0\) for
\(a\in A\). The restricted comparison map on unanchored coordinates is
injective exactly when every connected component of \(G\) meets \(A\).

Therefore the minimum number of trusted anchors is the number \(c\) of
connected components. Extra anchors create additional consistency relations;
they do not increase the number of free relational coordinates.

Trust is not supplied by graph incidence. It must come from preparation,
timing, an independently protected block, or another source-authorized
absolute effect.

## Why cycles help differently

A spanning forest has \(H^1=0\). Every edge-record pattern can be explained by
some vertex-label assignment, so comparison-measurement faults cannot be
distinguished from block faults using relational data alone.

Each independent cycle adds \(2k\) parity checks. A valid relative record has
zero sum around every cycle. A nonzero cycle sum is an edge-measurement fault
class in \(H^1(G;P)\).

Thus:

- tree edges establish maximal relative label rank;
- cycle edges add measurement-fault detection;
- anchors remove vertex common modes;
- neither cycles nor replication manufacture anchor authority.

## Three-block witnesses

For a three-block path, the relative map has rank \(4k\), common-mode kernel
dimension \(2k\), and no cycle check. Any two edge records are compatible with
some block labels.

For a three-block triangle, the relative rank is still \(4k\), but
\(H^1\) has dimension \(2k\). The sum of the three edge records must vanish.
A single flipped comparison bit violates that constraint.

## Mixed-boundary typing

The coefficient space \(P\) contains handle, boundary-loop, and relative-arc
Pauli coordinates. Graph cohomology treats them uniformly, but their physical
comparison operators retain distinct supports. Carrier geometry supplies the
network complex and its support labels; the quantum coefficient lens supplies
the Pauli module, Bell parity instrument, and fault meaning.

## Falsifiers

- common-mode dimension different from \(2kc\);
- cycle-fault dimension different from \(2k(m-n+c)\);
- an anchored component retaining a common-mode kernel;
- an unanchored component claimed absolutely identifiable;
- a tree comparison claimed to detect arbitrary edge-record faults;
- a cycle parity that does not annihilate valid relative records.

## Disposition

The correct shared object is a graph cochain complex with quantum Pauli
coefficients. Its degree-zero cohomology is reference drift; its degree-one
cohomology is comparison-record inconsistency. Anchors and cycles repair
different faults and cannot substitute for one another.

## Claim strength

Exact finite cohomological fault-classification theorem.

## Verification

Run
`uv run --with sympy python research/kitaev/checkers/check_bell_reference_network_cohomology.py`.
The result is written to
`research/kitaev/results/bell-reference-network-cohomology.json`.

