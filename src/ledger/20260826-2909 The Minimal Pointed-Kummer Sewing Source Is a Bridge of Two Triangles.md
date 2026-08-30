# 2909 — The Minimal Pointed-Kummer Sewing Source Is a Bridge of Two Triangles

## Frozen graph

The smallest connected simple graph whose separating Cut returns two complete
one-loop three-site sectors has vertices

\[
V=\{1,2,3,4,5,6\}
\]

and edges

\[
E=
\{12,23,31,34,45,56,64\}.
\]

The left triangle is \(123\), the right triangle is \(456\), and \(34\) is
the unique bridge.

Deleting \(34\) gives exactly

\[
G_L=C_3(1,2,3),
\qquad
G_R=C_3(4,5,6).
\]

The total graph has

\[
b_1(G)=7-6+1=2,
\]

while each Cut component has loop rank one.

## Minimality

Two vertex-disjoint triangle loops require at least six vertices and six
edges.  Connecting them while retaining a separating Cut requires one further
edge.  Thus the six-site, seven-edge double triangle is minimal in the declared
simple-graph class.

## Resolved Cut interface

Retain two bridge occurrences

\[
y_{34,+},
\qquad
y_{34,-}.
\]

The two regional partial energies are

\[
\mathcal E_L=X_1+X_2+X_3+y_{34,+},
\]

\[
\mathcal E_R=X_4+X_5+X_6+y_{34,-}.
\]

Only afterward impose the physical diagonal

\[
y_{34,+}=y_{34,-}=y_{34}.
\]

## Result

This graph is the first correctly typed global source target for Entry 2906.
The five-cycle packet is not a substitute: no Cut of a pentagon returns two
complete triangle factors.

The graph census does not itself define coefficient sewing.  The required
immutable input is now precise:

- complete canonical or OFPT integrand for this labelled graph;
- every simultaneous denominator term;
- source \(i\epsilon\) contour;
- bridge-Cut factorization before finite-part reduction.

Only that packet may determine the map between the two pointed Kummer torsors.

## Next finite construction

Instantiate the general cosmological-polytope contour formula on this graph.
Derive its source vertices, full facet set, orientation, localization Jacobian,
and bridge-Cut residue.  Stop before selecting an affine coefficient adapter.

## Durable artifacts

- `research/benincasa/check_minimal_double_triangle_cut_source.py`
- `research/benincasa/minimal-double-triangle-cut-source.json`
