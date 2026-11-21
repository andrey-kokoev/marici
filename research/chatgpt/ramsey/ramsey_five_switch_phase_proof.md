# Five-way closure: a cyclic domain-wall proof and transfer of the Hall center

Use the five switches in intrinsic C5 order as recorded in ramsey_five_switch_domain_walls.json (NOT increasing vertex-label order). Write x_i in {0,1} for whether switch i is applied, indices mod5.

## Short proof that no nonconstant phase pattern is valid

The seven-set S={2,3,5,8,9,13,19} has exactly one red edge in the original graph, (2,13), removed by switch0. Among all added switch edges, exactly one lies in S: (5,19), added by switch2. Hence S is independent EXACTLY when x_0=1 and x_2=0, irrespective of the other three bits. This can be verified directly from the source adjacency and the ten listed changed edges, without searching seven-subsets.

Apply the independently recovered C5 automorphism to S. Its five images give explicit obstructions for x_i=1,x_(i+2)=0. Step2 generates a connected five-cycle. Every nonconstant binary pattern has a 1->0 boundary on this cycle. Therefore every nonempty proper collection of switches is invalid. This is the structural reason for irreducibility, not merely a list of30 failed subsets.

The all-zero pattern is the original valid graph. The all-one pattern is isomorphic to it via the involution
(0 1)(2 7)(3 8)(4 10)(5 9)(6 11)(12 14)(15 16)(17 19)(18 20),
fixing13,21. The mapping is independently checked on every vertex pair. Thus both uniform patterns are valid, completing the proof that valid states in this five-bit cube are EXACTLY the two uniform ones.

## Exact obstruction counts

The exploratory script finds35 distinct seven-sets that become independent somewhere on the cube. Their exact Boolean conditions comprise the following C5 orbit families:
- two copies each of x_i(1-x_(i+2)) and x_i(1-x_(i-2));
- one copy of x_i(1-x_(i-1));
- one copy of x_i x_(i+1)(1-x_(i+3));
- one copy of x_i(1-x_(i+2))(1-x_(i+3)).
Summing gives N_7(x)=3 sum_i |x_i-x_(i+2)|. To see the reduction, the first line gives2D. Expanding the remaining three lines cancels adjacent-pair terms and cubic terms, leaving2 sum x_i-2 sum x_i x_(i+2)=D. Exhaustiveness of the35-set classification is computationally verified; the short irreducibility proof above does NOT depend on it.

## What the complete operation actually does

The output's unique Hall center is vertex1, whereas the input's is vertex0. The operation fixes both vertices and their neighbor sets as labeled graph data (none of its switched edges touches0 or1), yet transfers which one satisfies the global pair-signature condition. Thus it preserves the unlabelled graph type but changes the distinguished structural center. This gives substantive meaning to the collective reorganization beyond returning to an isomorphic graph.

Caution: x_i are switch-application bits, not automatically BRNN row marks, and the center-exchanging involution has not been identified with the original seed's prescribed duality. Such an identification would require explicit transport of the marks.
