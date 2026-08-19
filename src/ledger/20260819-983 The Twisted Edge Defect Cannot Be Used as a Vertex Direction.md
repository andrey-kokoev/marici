# 983 — The Twisted Edge Defect Cannot Be Used as a Vertex Direction

## Variance audit

Entry 982 proposed testing whether Entry 979's twisted chamber defect supplies
the second directions in the ((++)) and ((--)) coefficient planes.
The two sides have different degrees and variances:

\[
\delta_{\rm KN}\lambda
\in C^1_{\rm chamber}(\mathcal K_{\rm KN}),
\]

whereas the two rank-two planes of Entry 982 lie in

\[
C^0_{\rm word}(\mathcal M_{m coeff}).
\]

An edge cochain does not become a vertex vector merely because both serialized
spaces have six coordinates.

## Frozen-packet gate

The source packets used in Entries 895–896, 979, and 982 provide:

- the local half-monodromy/Pochhammer boundary coefficients;
- the six twisted edge defects and their two-cell closure;
- the two degree-zero character planes.

They do not provide:

- an edge-to-vertex contraction;
- a chamber chain/cochain intersection pairing;
- a codifferential;
- a Gysin map changing this degree and variance.

Therefore the proposed direct rank test is not defined.

## Narrow conclusion

\[
\boxed{
\delta_{\rm KN}\lambda
\text{ cannot presently be used as the second vertex direction.}
}
\]

This neither proves nor disproves a derived relation between the two objects.
It prevents a category error. The edge defect and vertex planes must either
remain in a total complex with their degrees intact, or be connected by an
independently normalized pairing/Gysin operation.

No missing carrier incidence is indicated: the chamber vertices, edges, and
oriented two-cell already exist. The missing datum is coefficient-level
variance conversion.

## Next construction

Return to the source regularized intersection pairing and determine whether it
canonically pairs the chamber edge chains with the six-word vertex cochains.
If such a pairing exists, export its exact matrix and verify compatibility
with Pochhammer transport before applying it to the ((++)) and ((--))
defects. Otherwise retain the two modules as independent graded coefficient
objects.

## Durable verification

- checker:
  research/benincasa/marici-gm/src/bin/string_six_point_edge_vertex_type_gate.rs;
- packet:
  research/benincasa/string-six-point-edge-vertex-type-gate.json;
- verified command:
  cargo run --quiet --bin string_six_point_edge_vertex_type_gate;
- allocator claim:
  seqclaim-e854e256f7a52af714f14fb2.
- epistemic event:
  ev-000000000600-bc9e33fe-9e12-4fad-8605-7b936a8c2383.
