# Persistent port labels are NOT an intrinsic graph-plus-square invariant

A short counterexample refutes the stronger structural explanation, despite all previous bounded labeled-loop returns being trivial.

ramsey_intrinsic_port_label_test.py starts at catalogue191, center0, pointwise marked square Q={0,1,3,11}, ports[2,4,5,6]. Two four-edge matching updates, both preserving the entire root0 incidence chart, produce a different labeled endpoint E. All three graphs are independently checked6-regular, triangle-free and without independent sevens.

Move1 removes (7,21),(8,12),(11,19),(14,15), adds (7,15),(8,14),(11,12),(19,21).
Move2 removes (9,21),(10,19),(14,17),(15,18), adds (9,15),(10,14),(17,21),(18,19).
Since the center and chart stay fixed throughout, the operational transport leaves each physical port vertex unchanged.

Nevertheless there is an exact isomorphism from the starting graph to E fixing EVERY vertex of Q, and mapping the ports by the four-cycle (2 4 6 5). In index order[2,4,5,6], the permutation is[1,3,0,2]. On the three pairings it acts[1,0,2]: exchanges two pairings and fixes the third. The full isomorphism and all three adjacency matrices are stored in ramsey_intrinsic_port_label_test.json; the isomorphism is checked on all vertex pairs.

Why this rules out the proposed intrinsic invariant:
Suppose graph+marked-square determined four distinct labels, naturally under square-preserving graph isomorphisms, and those labels were conserved by the operational transport. The two matching moves would require the endpoint labels to equal the initial labels at the same physical ports. Naturality under the exhibited isomorphism would require those same distinct labels to follow a nontrivial four-cycle. Both cannot hold.

This is a nontrivial loop in the space of graph+square ISOMORPHISM CLASSES, not a closed path returning to exactly the same labeled adjacency matrix. It therefore does NOT contradict the earlier bounded searches, which compared physical labeled graph endpoints. The endpoint-identifying isomorphism is an additional comparison, not an allowed cooperative move asserted to have occurred physically.

Conclusion: the persistent port frame cannot be recovered as an isomorphism-natural function of graph and square alone while respecting all allowed matching changes. It needs additional marking/history or an explicitly chosen identification of labeled representatives. The next conceptual task is to treat the port frame as part of the state and determine which transports of this extra datum are operationally admissible, instead of mistaking a selected frame for an intrinsic observable.
