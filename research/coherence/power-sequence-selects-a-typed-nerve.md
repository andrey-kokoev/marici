# The power sequence asks for a typed nerve, not a presumed simplex

## Claim boundary

The sequence

\[
P^1,\;P^2,\;P^3,\;P^4
\]

suggests higher incidence, but the exponents alone do not determine a simplicial object. They record arity or relational rank. The source incidence grammar determines whether the resulting cells are simplicial, cubical, globular, or mixed.

No temporal order is assigned to the arrows below.

## Arity interpretation

A minimal reading is

\[
P^1=\text{position},
\qquad
P^2=\text{typed binary relation},
\]

\[
P^3=\text{comparison of binary relations},
\qquad
P^4=\text{coherence of those comparisons}.
\]

This supports the slogans

\[
\text{observer}=P^2
\]

and

\[
\text{perspective}=P^3,
\]

provided `observer` means a stabilized binary incidence and `perspective` means an oriented comparison between incidences. The exponent is not tensor power until a tensor constructor is declared.

## When the sequence is simplicial

Suppose the source supplies an ordered composable chain

\[
p_0\xrightarrow{f_{01}}p_1\xrightarrow{f_{12}}p_2
\xrightarrow{f_{23}}p_3
\]

and supplies omission maps. Then the natural nerve is simplicial:

- \(P^1\) is a vertex;
- \(P^2\) is an edge;
- \(P^3\) is a triangle comparing a direct edge with a composite;
- \(P^4\) is a tetrahedron comparing the four triangular faces.

Using the shifted convention \(P^{n+1}=X_n\), the required maps are

\[
d_i:P^{n+1}\to P^n,
\qquad
s_i:P^{n+1}\to P^{n+2},
\]

with

\[
d_i d_j=d_{j-1}d_i\quad(i<j)
\]

and the usual face--degeneracy identities. A \(P^4\) boundary is then a 3-horn or tetrahedral shell. Fillability is an additional proposition, not a consequence of having four valid faces.

## When the sequence is cubical

Suppose instead the source supplies three independent binary choices or transports. Pairwise compatibility produces square faces, not triangular faces. The natural \(P^4\)-level object is then a cube:

\[
\{0,1\}^3.
\]

It has six square faces and one three-dimensional interchange residual. Collapsing it to a comparison between two total routes loses the location of a defective interchange.

The cubical structure requires face maps

\[
\partial_i^\epsilon:C_n\to C_{n-1},
\qquad \epsilon\in\{0,1\},
\]

degeneracies, and—when supplied—connections. Its coherence law is a cube-filling law, not the tetrahedral associator law.

## Mixed nature of the boundary object

Different sectors can carry different nerves simultaneously:

- composition and omission chains are simplicial;
- independent transports are cubical;
- comparisons between parallel presentations are globular;
- cyclic observations belong to a cyclic or bar construction.

The common object is therefore best modeled initially as a typed computad or pasting scheme. Functors between its simplicial, cubical, globular, and cyclic components must be declared; equal dimension does not provide such a comparison.

## Relation to the four-port shell

A four-port boundary does not become a tetrahedron merely because it has four named ports. Ports are objects or interfaces, whereas tetrahedral faces are compositional comparisons. The following must be derived separately:

1. which ports are vertices, edges, faces, or coefficient markings;
2. which pairs compose;
3. which directions are independent;
4. which face maps forget or restrict data;
5. which residual is produced by the full boundary;
6. what information a proposed filler or scalar readout forgets.

A coherence defect such as

\[
\Omega=I-CG
\]

may be a representation of the total boundary residual. It is not by itself a proof that the underlying nerve is simplicial. To earn that interpretation, \(C\) and \(G\) must be identified with source-authorized face composites.

## First compiler experiment

For each generating operation, record

```text
constructor_id
arity
variance
ordered_inputs
independent_axes
face_maps
degeneracies
coefficient_system
source_authority
```

Then:

1. derive the nerve shape from this signature;
2. enumerate every codimension-one face;
3. type each face and comparison;
4. compute the signed boundary residual;
5. verify that the residual is closed;
6. classify fillers and their ambiguity;
7. test whether the chosen readout is faithful on coefficient markings.

The smallest hostile examples are:

- four individually valid triangular faces with a nonzero unfillable tetrahedral residual;
- six individually valid square faces with a nonzero cube residual;
- two distinct coefficient markings having the same scalar boundary readout.

## Higher-level interpretation

The defensible conclusion is not that nature uses simplices specifically. It is:

\[
\boxed{\text{relational powers select higher cells, while incidence selects their geometry.}}
\]

Homotopy enters because fillers, alternative fillers, and obstructions are invariant under higher comparison. The more general candidate for atemporal computation is a typed higher incidence object whose admissible global structures are its coherent fillings and whose unresolved distinctions are retained as obstruction classes.
