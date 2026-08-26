# Joint reference-fault distance equals minimum unanchored degree plus one

Owner: `marici.Kitaev`

## Bounded question

Does the anchored cut formula require a global expansion audit, or can its
minimum be classified exactly for simple comparison graphs?

## Exact theorem

Let \(G\) be a finite simple graph with trusted anchor set \(A\), and assume
there is at least one unanchored vertex. Define

\[
\delta_A(G)=\min_{v\notin A}\deg(v).
\]

Then the joint block-and-record fault distance is

\[
d_{\mathrm{mix}}(G,A)
=
\min_{\varnothing\ne S\subseteq V_G\setminus A}
\bigl(|S|+|\partial S|\bigr)
=1+\delta_A(G).
\]

The upper bound is attained by a minimum-degree singleton.

For the lower bound, write \(|S|=s\). If \(s\ge\delta_A+1\), vertex weight
alone gives the result. If \(1\le s\le\delta_A\), simplicity bounds each
vertex by at most \(s-1\) neighbors inside \(S\), hence

\[
|\partial S|
\ge
s(\delta_A-s+1).
\]

Therefore

\[
|S|+|\partial S|
\ge
s(\delta_A-s+2)
\ge
\delta_A+1.
\]

The last concave quadratic takes its minimum on the interval endpoints.

## Correction criterion

Unique correction of every joint fault of total weight at most \(t\) requires
and, for this linear code, is guaranteed by

\[
2t<d_{\mathrm{mix}}.
\]

Using the exact identity,

\[
t\text{-fault correction}
\quad\Longleftrightarrow\quad
\delta_A(G)\ge2t.
\]

Thus higher joint-fault distance is local in the unweighted simple-graph model.
Large-set expansion does not become the active obstruction because the block
fault weight \(|S|\) is already part of the codeword weight.

## Consequences

- anchored paths and trees have an unanchored leaf and distance two;
- cycles have minimum degree two and distance three;
- \(d\)-regular unanchored comparison networks have distance \(d+1\);
- the complete graph \(K_n\) has distance \(n\);
- correcting \(t\) arbitrary joint faults requires at least \(2t+1\) total
  vertices, since a simple graph has degree at most \(n-1\).

## Scope boundary

The identity uses a simple unweighted graph and unit cost for every block and
record fault. Parallel repeated comparisons, hyperedges, time-labelled checks,
correlated faults, and unequal weights \(\alpha|e|+\beta|f|\) define different
codes. Their distances need not equal minimum degree plus one.

Physical locality also remains separate: high graph degree may require long
mixed-boundary arc couplings or congested schedules.

## Correction to the prior boundary

Milestone 2620 correctly proved the \(t=1\) edge minimum but stated that
minimum degree would not suffice for larger \(t\). The exact theorem above
falsifies that sentence under the frozen simple unweighted model. The prior
packet and ledger were repaired to preserve the stronger result and its scope.

## Falsifiers

- a simple graph with distance different from one plus minimum unanchored
  degree;
- a subset beating the minimum-degree singleton;
- \(t\)-fault correction with an unanchored degree below \(2t\);
- failure of correction with all unanchored degrees at least \(2t\);
- applying the identity to weighted, parallel-edge, or hypergraph models.

## Disposition

The joint-fault distance is completely classified in the simple unweighted
comparison model. Network synthesis for a target correction radius reduces to
a minimum-degree design problem plus separately typed physical locality and
resource constraints.

## Claim strength

Exact finite all-distance graph-code theorem and explicit correction of a
prior scope statement.

## Verification

Run
`uv run --with sympy python research/kitaev/checkers/check_bell_reference_min_degree_distance.py`.
The result is written to
`research/kitaev/results/bell-reference-min-degree-distance.json`.

