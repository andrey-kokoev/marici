# Reading: Mnev, arXiv:2406.01625v2

Read the supplied 24-page PDF `references/2406.01625v2.pdf` in full using extracted text. Some displayed mathematical symbols are damaged by extraction; the account below uses the surrounding definitions and theorem statements, not literal transcription of those displays.

Nikolai Mnev, *K(Z, 2) out of circular permutations*, v2 (2024).

## Construction and theorem

- In degree n, S_n is the symmetric group on n+1 elements, regarded as part of the symmetric crossed simplicial group S. It is not an ordinary simplicial group.
- The cyclic subgroup C_n rotates the positions of a permutation. Its right orbits are oriented circular orders on the n+1 distinct labels. Write SC_n = S_n/C_n; it has n! elements.
- Faces delete a labelled bead and renumber the remaining labels. Degeneracies insert the next label immediately after the specified bead, with renumbering. These descend to circular orders (sections 2.4–2.5, pp. 9–11).
- Theorem 1: |SC| is homotopy equivalent to K(Z,2). The realization of S is a contractible topological group; |C| is U(1), and |S| -> |SC| is the corresponding universal circle bundle (introduction; sections 2.7 and 3, pp. 14–22).
- Pullback over a simplex gives a minimally triangulated circle bundle, via the order-reoriented twisted shuffle product (Lemma 3, pp. 20–21).

The quotient is by rotations, not reflections. Forgetting the initial bead preserves oriented circular order; it does not forget every ordering distinction.

## The subtlety matters

The canonical left crossed cyclic action does not yield the naive simplicial quotient required here. Right cyclic orbits do form a simplicial equivalence relation. Inversion switches left and right actions only after an appropriate order reorientation: it is not a simplicial map with unchanged face indices. The corresponding reorientation realizes to group inversion (sections 3.2–3.5).

Consequently, reversing a wiring presentation cannot simply be identified with this construction's inversion. Its action on orders, faces and degeneracies would need to be exhibited.

## What this changes in our interpretation

Our local sufficiency result remains intact: at a fixed occurrence and binding, the four labelled records determine the contents of the reference join. But that does not settle the global organization of references.

This paper gives a precise model in which a global topological invariant comes from how locally ordered presentations fit together, without requiring an extra transformation of an attached payload. Therefore:

> Failure to find a payload-changing continuation is not evidence that the reference organization has trivial topology.

The converse is equally important: preservation of histories or the presence of finite permutations does not establish a circle bundle. One needs the particular compatible circular-order structure.

A global family of compatible circular orders is distinct from a global choice of compatible linear representatives (cuts). An actual simplicial lift of a base map B -> SC through S supplies a section of its pulled-back bundle, hence trivializes it. Nonzero first Chern class excludes such a lift. We must not require a global cut as part of the definition of globally coherent circular data and thereby exclude the phenomenon in advance. No claim is made that every topologically trivial bundle on a fixed triangulation admits that particular strict simplicial lift.

This is a structural/classifying statement, not a connection or holonomy law. The paper does not give Su-32 dynamical phases, a scattering operator, or an experimentally distinguishing observer.

## Concrete applicability gate for Su-32

Before claiming an application, supply:

1. A native base simplicial or semi-simplicial complex B. Explain what its vertices and simplices represent; do not turn four record labels into a geometric simplex merely by count.
2. For each n-simplex, a native oriented cyclic order of its n+1 labelled vertices/events.
3. Agreement under every actual face restriction (and degeneracies if working simplicially), giving a map B -> SC.
4. The pulled-back bundle and an integral characteristic-class calculation. Neither a nonzero class nor a generator/Hopf identification follows from the existence of the map alone.

The paper's introduction recalls an additional fixed-base restriction from Mnev's earlier work: semi-simplicial triangulability over a specified base B is equivalent to the Chern class admitting a {0,1}-valued simplicial 2-cocycle there. Thus universality of the realization must not be confused with representability of every class by the same fixed finite triangulation.

No such native B -> SC map is supplied by our current layer-4 comparison audit. Its byE/byP join trees are not already circular orders; a square of comparisons is not automatically a circle fiber. The six cyclic orders on four labels are also not canonically the six unordered pairs of four records, despite the equal cardinality.

## Revised productive question

Alongside “what data suffice for each comparison?”, ask:

> What globally compatible order/reference structure do the native incidences actually determine, and what distinctions survive changes of local presentation?

The first check is whether native circular orders exist and restrict compatibly—not whether a newly chosen cochain can be made nonzero. If they do not, this particular classifying model remains conditional machinery rather than a description of Su-32.

No source code, wiring, or scientific status was changed by this reading.
