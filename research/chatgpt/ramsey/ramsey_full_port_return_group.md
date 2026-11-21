# Return group is S4, not C4 or D8

ramsey_port_return_group.py exhaustively constructs all288 perfect-incidence-matching outputs in the fixed center0 chart. Connect two outputs when they differ by four removed/four added red edges. This graph has288 vertices, degree10 everywhere, and is CONNECTED. Distances from catalogue191 are {0:1,1:10,2:45,3:97,4:96,5:37,6:2}.

Fix square Q={0,1,3,11} pointwise and ports[2,4,5,6]. Every permutation of the four ports extends uniquely to a six-label permutation fixing the other two labels and hence to its canonical permutation of all fifteen duads. Its image of the source graph is one of the288 outputs. ALL24 images are reachable. Shortest-path distances for the24 endpoint identifications are {0:1,2:5,4:16,6:2}. The JSON saves all24 paths, exact changed edges, and endpoint isomorphisms. Every intermediate along every saved path is independently checked6-regular, triangle-free and without independent sevens.

Therefore the return group on four ports, after closing paths by square-preserving graph isomorphisms, is EXACTLY S4. It cannot be larger, and every S4 element is realized. This settles the three competing conjectures in this stated quotient: cyclic-memory and dihedral/opposition-memory are refuted; full-frame conjecture holds computationally with explicit finite certificates.

A small independent generator certificate: the earlier two-step return realizes the four-cycle (2 4 6 5). Another two-step path realizes the transposition (2 4), fixing ports5,6. Together these generate S4 and destroy the opposition pairing preserved by the four-cycle. The transposition path is:
1 remove (10,18),(11,20),(12,19),(14,17); add (10,14),(11,12),(17,20),(18,19).
2 remove (7,20),(8,18),(9,16),(12,14); add (7,16),(8,14),(9,12),(18,20).
Endpoint isomorphism fixes Q and swaps2,4 on the label ports, canonically extending to duads. A closed return using the inverse endpoint identification acts by the inverse permutation; the realized group is unchanged.

Minimal-state consequence in this graph+square setting:
- to specify only the row comparison, carry one of the THREE pairings of the off-square ports;
- to specify the complete ordered-port frame, carry one of24 frames. One fixed port leaves S3 ambiguity, two ordered ports leave S2, three ordered port identities determine the fourth.
No opposition pairing is invariant under all quotient returns. Calling the frame intrinsic would therefore discard information that the operations can change. Extra marking or restrictions on admissible endpoint identifications are necessary.

Scope: these are quotient returns, not literal closed paths to the same labeled adjacency matrix. They do not contradict bounded labeled-loop flatness. The operations used here never leave the two Hall graph types. This also does not prove the full regular-witness four-edge connectivity conjecture. Nor should this port S4 be identified with the original tetrahedral column S4 merely because orders agree: the endpoint identifications preserve graph and square, but need not preserve additional tetrahedral column incidence. Adding such marks restricts the admissible identification group and changes the question.
