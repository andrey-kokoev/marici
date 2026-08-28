# 3862 — The Six Normalized Conductor Ports Form Two Free Cyclic Orbits

## Question

Does the finite grade-zero conductor packet of Entry 3861 transport naturally among the three deletion charts, or is it an artifact of the (G_{12}) presentation?

## Source cyclic action

Use

\[
(X_1,X_2,X_3;y_{12},y_{23},y_{31})
\longmapsto
(X_2,X_3,X_1;y_{23},y_{31},y_{12}).
\]

The three residue-chart orientations are

\[
G_{12}:dy_{23}\wedge dy_{31},
\]

\[
G_{23}:dy_{31}\wedge dy_{12},
\]

\[
G_{31}:dy_{12}\wedge dy_{23}.
\]

The cyclic generator transports each orientation with sign (+1).

## Labelled port packet

The two active conductors in each chart are

\[
G_{12}:(g_1,g_2),
\qquad
G_{23}:(g_2,g_3),
\qquad
G_{31}:(g_3,g_1).
\]

They assemble into two free labelled orbits:

\[
G_{12}:g_1
\longmapsto
G_{23}:g_2
\longmapsto
G_{31}:g_3
\longmapsto
G_{12}:g_1,
\]

\[
G_{12}:g_2
\longmapsto
G_{23}:g_3
\longmapsto
G_{31}:g_1
\longmapsto
G_{12}:g_2.
\]

Both generic residue formulas close after three substitutions. The common source normalization contains the triangle-volume factor

\[
(X_1+X_2+X_3)(-X_1+X_2+X_3)(X_1-X_2+X_3)(X_1+X_2-X_3),
\]

which is cyclic invariant.

At the asymmetric sample ((2,3,4)), all six transported port values are nonzero, so closure is not caused by a degenerate symmetric point.

## Result

The normalized grade-zero conductor packet is occurrence-covariant. It consists of two free (C_3)-orbits with no transition sign or chart unit.

This proves cyclic descent of the labelled local coefficient data. It does not authorize summing the six ports into a scalar, and it does not prove Gauss–Manin horizontality.

## Classification

- cyclic labels and chart orientations: existing Carrier data;
- conductor values: sector-specific coefficient costalks;
- cyclic transport: source-defined equivariance;
- physical aggregation: unconstructed;
- new Carrier datum: none.

## Durable artifacts

- `research/benincasa/checkers/check_rank26_conductor_cyclic_occurrence_packet.py`
- `research/benincasa/results/rank26-conductor-cyclic-occurrence-packet.json`

The checker passes six exact gates.

## Next falsifier

Embed one two-port chart packet into the fixed rank-26 coefficient basis and apply both generic base derivatives. Test whether the resulting six-port cyclic submodule is horizontal. If the connection leaves the span, export the exact off-diagonal defect rather than enlarging the packet after inspection.
