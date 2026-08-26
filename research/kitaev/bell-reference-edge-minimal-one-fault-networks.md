# One cycle is the minimum comparison redundancy for one joint-fault correction

Owner: `marici.Kitaev`

## Bounded question

Among connected Bell-reference comparison graphs with one trusted anchor, what
is the minimum edge cost required to correct one arbitrary block-or-record
fault?

## Exact local criterion

The joint-fault distance is

\[
d_{\mathrm{mix}}(G,A)
=
\min_{\varnothing\ne S\subseteq V_G\setminus A}
\bigl(|S|+|\partial S|\bigr).
\]

For a connected graph with one anchor,

\[
d_{\mathrm{mix}}\ge3
\quad\Longleftrightarrow\quad
\deg(v)\ge2
\text{ for every unanchored vertex }v.
\]

Necessity follows by taking \(S=\{v\}\). For sufficiency, singleton sets have
weight at least three; two-vertex sets have a nonempty cut because they cannot
form an unanchored connected component; and sets of size at least three meet
the bound from their vertex weight alone.

Hence one arbitrary joint fault is correctable exactly when the comparison
network has no unanchored leaf.

## Edge minimum

Every tree on at least two vertices has at least two leaves. At most one leaf
can be the trusted anchor, so every anchored tree has an unanchored leaf and
distance two. Therefore a one-fault-correcting network must contain a cycle and
has at least

\[
m\ge n
\]

edges.

The lower bound is attained. A cycle through all vertices has \(m=n\) and
distance three. More generally, a connected unicyclic graph is admissible when
the anchor is its only possible leaf; for example, the anchor may terminate a
path leading into a cycle. Thus exactly one independent cycle is the minimum
comparison redundancy.

## Resource interpretation

A spanning tree uses \(n-1\) comparisons and recovers every relative Pauli
label but cannot distinguish a leaf block fault from its adjacent record fault.
One additional comparison edge creates the first cycle parity and can remove
all unanchored leaves when placed appropriately. Placement, not merely edge
count, matters: a cycle elsewhere while retaining an unanchored dangling tree
still leaves distance two.

## Higher-distance continuation

For correction of \(t\) arbitrary joint faults, one needs

\[
d_{\mathrm{mix}}ge2t+1.
\]

The singleton bound forces every unanchored degree to be at least \(2t\). A
subsequent exact theorem strengthens this: for simple comparison graphs,
\(d_{\mathrm{mix}}=1+\min_{v\notin A}\deg(v)\), so the degree condition is also
sufficient for every \(t\). This packet retains the edge-minimal \(t=1\)
synthesis; the general distance identity is proved separately.

## Mixed-boundary typing

The graph criterion applies independently to every handle, loop, and relative
arc Pauli coordinate. A physical architecture must still realize each edge
comparison on its typed support. Topological graph redundancy does not price
the length or locality of a mixed-boundary arc coupling.

## Falsifiers

- a distance-three network with an unanchored leaf;
- an anchored tree correcting one arbitrary joint fault;
- a connected distance-three graph with fewer than \(n\) edges;
- a cycle graph with distance below three;
- edge count alone claimed sufficient despite a dangling unanchored leaf;
- a claimed higher-distance degree law without the simple-graph hypothesis.

## Disposition

One independent comparison cycle is necessary and sufficient at minimum edge
cost for correction of one arbitrary joint fault, provided its placement leaves
no unanchored leaf. Trees are optimal for relative reconstruction but strictly
insufficient for joint fault correction.

## Claim strength

Exact finite graph-synthesis theorem for one joint fault.

## Verification

Run
`uv run --with sympy python research/kitaev/checkers/check_bell_reference_edge_minimum.py`.
The result is written to
`research/kitaev/results/bell-reference-edge-minimum.json`.
