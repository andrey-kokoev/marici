# Conditional propagation of a Suzuki--divisor cell by edgewise-subdivision functoriality

## Status correction

The formal subdivision argument in this note was already present in prior research for the established signed asymptotic simplex. It does not prove that the proposed Suzuki--divisor overlay is that simplex, nor does it construct canonical fine-stage alignment on all six analytic edges. The implication below is conditional on first constructing the parent Suzuki--divisor diagram as a homotopy-coherent simplex in the same realization category. That premise remains open.

## Input simplex

Let

\[
\Phi_Z:
\Delta^3
\to
N_\Delta(\mathcal C_{form})
\]

be the signed source-labelled tetrahedron with vertices:

\[
V_1=
\text{coefficient source},
\]

\[
V_2=
\text{Suzuki }L^2\text{ feature},
\]

\[
V_3=
\text{arithmetic divisor/Krein feature},
\]

\[
V_4=
\text{completed scalar readout}.
\]

Its six edges are source-labelled maps or closed relations, its four faces are the corresponding comparison homotopies, and its 3-simplex is the signed tetrahedral modification.

For a finite symmetry-closed divisor packet \(Z\), the nontrivial metric face has residual

\[
J_{\Xi,Z}-G_{F,Z}.
\]

The residual is retained as face data, so the signed tetrahedron is an actual simplex even when that operator is indefinite.

## Edgewise-subdivision functor

Edgewise subdivision is functorial. Applying the seventh edgewise subdivision gives

\[
\operatorname{esd}_7(\Phi_Z):
\operatorname{esd}_7(\Delta^3)
\to
\operatorname{esd}_7
N_\Delta(\mathcal C_{form}).
\]

Use the canonical comparison from the subdivided nerve to the nerve of composable source-labelled presentation strings. This yields the signed lattice diagram

\[
\Phi_Z^{(7)}:
\operatorname{esd}_7(\Delta^3)
\to
N_\Delta(\mathcal C_{form}^{chain}).
\]

No independent assignment of the interior lattice nodes is required.

## Meaning of a subdivision vertex

A subdivision vertex is not interpreted as a barycentric linear combination of the four analytic presentations.

It records a finite ordered stage of elementary transfers among them. Its image under \(\Phi_Z^{(7)}\) is the corresponding source-labelled chain of edge maps or relations.

Thus a lattice coordinate

\[
(a_1,a_2,a_3,a_4),
\qquad
\sum_i a_i=7,
\]

records subdivision position and transfer history. It does not denote

\[
a_1V_1+
\cdots+
a_4V_4.
\]

This resolves the earlier semantic ambiguity of the 120 interior nodes.

## Edges

Every subdivided edge is the image of one elementary transfer in the parent tetrahedron. Hence its analytic label is one of:

1. Suzuki synthesis;
2. divisor observation;
3. direct arithmetic observation;
4. Suzuki Gram readout;
5. divisor Gram readout;
6. the source-labelled Suzuki--divisor relation;

whiskered by the transfer history already accumulated at its source vertex.

Composition is inherited from the parent simplex. No new operator formula is introduced at an interior edge.

## Triangular faces

Every lattice triangle is sent to a whiskered instance of one of

\[
H_{123},
\qquad
H_{124},
\qquad
H_{134},
\qquad
H_{234}.
\]

The face type is determined by which one of the four parent vertices is absent from its direction set.

The comparison residual on every translated \(H_{234}\) face is the corresponding source pullback of

\[
J_{\Xi,Z}-G_{F,Z}.
\]

Therefore subdivision does not create new defect operators.

## Elementary tetrahedra

Every elementary 3-simplex of the subdivision is sent to a whiskered copy of the parent signed tetrahedral modification.

The local equation is always

\[
H_{124}
\circ
(H_{234}*d_{12})
=
H_{134}
\circ
(d_{34}*H_{123}),
\]

with the appropriate accumulated whiskers.

Associativity of source-labelled relation composition and the parent 3-simplex imply compatibility on shared triangular faces.

Thus the hundreds of translated local equations are images of one simplicial identity rather than independent analytical obligations.

## Boundary strata

Edgewise-subdivision functoriality automatically preserves restriction to every parent face, edge, and vertex.

Therefore:

1. a lattice face lying in parent face \(ijk\) uses only \(H_{ijk}\);
2. a lattice edge lying in parent edge \(ij\) uses only \(d_{ij}\) and its subdivisions;
3. repeated coordinates on a boundary are interpreted by degeneracy maps;
4. shared boundary cells receive identical labels from adjacent elementary tetrahedra.

No separate boundary prototype is needed once the parent simplex is supplied as an actual simplicial map.

## Dagger equivariance

The source dagger defines an anti-simplicial equivalence

\[
D:
N_\Delta(\mathcal C_{form}^+)
\to
N_\Delta(\mathcal C_{form}^-)^{op}.
\]

Let \(r\) reverse the parent tetrahedron orientation. The parent cells satisfy

\[
\Phi_Z^-
=
D\Phi_Z^+r.
\]

Functoriality gives

\[
\operatorname{esd}_7(\Phi_Z^-)
=
\operatorname{esd}_7(D)
\operatorname{esd}_7(\Phi_Z^+)
\operatorname{esd}_7(r).
\]

Hence the entire negative-polarity lattice is derived from the positive-polarity signed lattice. No second collection of interior homotopies must be selected. Dagger commutes with subdivision up to the declared orientation reversal.

## Successor naturality

Let \(S\) be a source successor for which the four parent vertex observations and six parent edges are natural. If the four parent face homotopies and tetrahedral modification are also natural, then

\[
S\Phi_Z
\simeq
\Phi_{Z'}S
\]

is a simplicial natural transformation.

Applying edgewise subdivision gives

\[
S\Phi_Z^{(7)}
\simeq
\Phi_{Z'}^{(7)}S.
\]

Therefore prime-packet inclusion, convolution degree, aperture restriction, and seam successors propagate over the full lattice whenever they are defined on the parent tetrahedron.

## Positive lifting

Let

\[
F:
\mathcal C_{Pos}
\to
\mathcal C_{form}
\]

be the positive-to-signed forgetful functor.

A positive lattice lift of \(\Phi_Z^{(7)}\) exists if a positive lift of the parent simplex \(\Phi_Z\) exists. Applying subdivision to that positive parent simplex then fills every positive lattice cell coherently.

Conversely, restriction of any positive lattice lift to the selected elementary cell gives a positive parent metric face. Since translated Gaussian observations detect the divisor defect, this restriction forces the same augmented Schur condition.

Hence

\[
\operatorname{Lift}_{Pos}
(\Phi_Z^{(7)})
\ne\varnothing
\]

if and only if the parent positive lift exists, subject to the declared bounded-completion hypotheses.

Subdivision introduces no new positivity obstruction.

## Relation-valued edges

The signed category must admit closed source-labelled linear relations, not only bounded operators. This is essential for the edge comparing Suzuki and divisor features before Gram domination is proved.

If a relation becomes the graph of a bounded operator after Douglas acceptance, its subdivided copies become operator edges automatically. If acceptance fails, the entire lattice remains valid in the relation-valued signed category.

## Global result

For every finite symmetry-closed divisor packet \(Z\), the parent signed Suzuki--divisor tetrahedron determines:

1. all lattice vertices as transfer histories;
2. all subdivided edges as whiskered parent edges;
3. all triangular homotopies as whiskered parent faces;
4. all elementary tetrahedra as whiskered parent modifications;
5. all shared-boundary identifications;
6. the dagger-opposite lattice;
7. all admitted successor naturalities.

No manual enumeration of the subdivision cells is analytically necessary.

## Remaining qualifications

The construction assumes that the signed parent tetrahedron is represented in a simplicial nerve of a category or bicategory of source-labelled forms and closed relations.

A fully formal implementation still requires:

1. declaring that enriched relation category;
2. materializing \(\Phi_Z\) as a simplicial map in the proof assistant;
3. attaching bounded graph completions to each parent edge;
4. proving infinite-packet convergence before passing from finite \(Z\) to the complete divisor.

These are implementation and completion tasks. They do not create new local analytic defects.

## Disposition

The local Suzuki--divisor cell extends canonically to the entire canonical eight-level tetrahedral lattice by edgewise-subdivision functoriality.

The 120 interior nodes acquire semantics as source-labelled transfer histories. Every face and tetrahedral relation is inherited from the one parent signed simplex.

The only positive obstruction remains the parent augmented metric face; the subdivision contributes no additional positivity gate.
