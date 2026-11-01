# Three-contact simplices: hexagonal closure and history-aware completion

Date: 2026-10-28.

## Scope

This calculation tests the proposed cyclic gluing of three copies of a filled 4-simplex at three distinct contact vertices. It uses the period lattice in the supplied `su32-native-window-operation-v1.md`, an explicitly declared coordinate rotation, and an explicitly declared completion policy. It does not use a recovered native Su-32 port registry. No native port/edge routes or native 4-simplex occurrences were evaluated.

Two results follow. A rank-two hexagonal contact lattice is compatible with the recorded rank-three period lattice. A free, history-aware path completion generates simplicial coherence without filling the original central loop. Neither result establishes that the typed Su-32 operations select these constructions.

A 4-simplex here means the five-vertex, four-dimensional simplex. It is not being identified with the earlier dual-indexed “4-packet = point.” The source's four period generators are likewise not being reinterpreted as five simplex vertices. A planar drawing is an incidence diagram, not a faithful embedding of a four-dimensional cell.

## 1. An exact repeated rotate-and-translate calculation

The supplied source defines

    g_i = (1,1,1,1) - 4 e_i,     sum_i g_i = 0,
    L(a) = a_0 g_0 + a_1 g_1 + a_2 g_2.

The first three g_i are a lattice basis. Lifted ports have distinct integer coordinates, with source edges updating those coordinates by their translation labels.

Choose the candidate coordinate permutation R with

    R(g_0)=g_1, R(g_1)=g_2, R(g_2)=g_0, R(g_3)=g_3.

It preserves the period lattice. In integer basis coordinates,

    R(a_0,a_1,a_2) = (a_2,a_0,a_1).

With the standard Euclidean metric on the displayed coordinates, its restriction to the plane perpendicular to its axis is a 120-degree rotation. The metric convention is used for the hexagonal drawing; the closure calculation below is integral and needs no metric.

For the repeated affine operation F(a)=R(a)+k, direct substitution gives

    F^3(a) = a + k + Rk + R^2k
           = a + (s,s,s),       s=k_0+k_1+k_2.

Consequently the exact lattice closure condition is s=0. This is an all-integer identity, not an extrapolation from a bounded enumeration.

A single period-generator displacement does not pass. With k=(1,0,0), the three increments represent g_0,g_1,g_2 and total -g_3, not zero. These are period displacements, not certified primitive wire edges.

A shortest nonzero passing displacement is

    d = g_0-g_1,
    Rd = g_1-g_2,
    R^2d = g_2-g_0.

Their sum is zero. Their displayed four-coordinate values are

    (-4,4,0,0), (0,-4,4,0), (4,0,-4,0).

Their squared lengths are 32 and consecutive dot products are -16. Thus the three steps turn through 120 degrees. The contact vertices can be placed at

    0, d, d+Rd,

and the repeated affine operation permutes them cyclically.

The full zero-discrepancy sublattice is

    {L(k): k_0+k_1+k_2=0}
      = Z(g_0-g_1) + Z(g_1-g_2).

On this plane, ||L(k)||^2=16(k_0^2+k_1^2+k_2^2). Its six shortest nonzero directions are the positive and negative differences of two of g_0,g_1,g_2. This is a scaled A2 triangular lattice; its nearest-neighbor directions form a hexagon. The drawing therefore has a lattice-compatible basis, rather than being an arbitrary display convention.

All eight order-three permutations of the four coordinate positions preserve the generator set. This verifies only lattice automorphisms. It does not verify preservation of native P/N/E types, face identities, retained histories, or the full wire graph. Nor does lattice closure prove that the proposed blocks intersect only at the prescribed contacts.

More generally, for a linear action R of order m, an affine repeated step R(a)+k closes after m steps precisely when (I+R+...+R^(m-1))k=0. This is a reusable test for other rotation orders; applicability to another construction requires its own period data and typed action.

## 2. The declared three-simplex contact complex

Use the vertex sets

    A={0,1,3,4,5},
    B={1,2,6,7,8},
    C={2,0,9,10,11}.

Include every nonempty face of each simplex. The pairwise intersections are exactly the vertices 1,2,0; the triple intersection is empty. Cyclically permuting the three contact vertices and the three corresponding private-vertex triples is an automorphism of order three.

The face counts in dimensions 0 through 4 are

    (12,30,30,15,3).

The central edges 01,12,02 are present. The face 012 is absent. The script supplies and independently verifies 42 elementary free-face collapses reducing the entire complex to those three vertices and three edges. This is an integral topological certificate: the complex is homotopy equivalent to S1, not merely a space with the same rational Betti numbers.

The oriented central cycle is [01]+[12]-[02]. An exact rational boundary-matrix calculation independently shows that it is not a boundary. Adding the single central face 012 produces a complex that collapses to a point. Filling every graph clique adds exactly that face here and therefore kills the cycle.

For boundary-only blocks, meaning three copies of the boundary of a 4-simplex rather than three filled 4-simplices, the rational Betti numbers are (1,1,0,3). The contractible-piece argument does not apply to that different input.

The ordinary nerve theorem is consistent with the filled-block result: three contractible pieces with contractible nonempty pairwise intersections and no triple intersection have a circular nerve. The explicit collapse avoids relying on a cover theorem to certify this particular finite example.

## 3. Forced coherencers need not kill the original loop

Name the central oriented arrows

    f:0->1, g:1->2, h:2->0.

A compositional local extension adds c=g after f, with a triangular comparison between the two-edge path (f,g) and c. The other route from 0 to 2 is the already present inverse h^(-1), once reversibility is admitted. There is no rule of simplicial incidence that makes c=h^(-1) merely because their endpoints match.

This distinction requires a history-labelled structure or a simplicial set. An abstract simplicial complex has at most one edge with a given pair of vertices, so it cannot retain these two parallel edges as different edges.

A precise candidate completion is the free fundamental groupoid of the contact cycle. Select two of the three edges as a spanning tree solely to express normal forms. Its arrows can then be written

    (i,j,n),   i,j in {0,1,2}, n in Z,

with composition and inversion

    (i,j,n) followed by (j,k,m) = (i,k,n+m),
    (i,j,n)^(-1) = (j,i,-n).

One coordinate choice is

    f=(0,1,0), g=(1,2,0), h=(2,0,1).

Then

    c=(0,2,0), h^(-1)=(0,2,-1),
    h after g after f=(0,0,1) != (0,0,0).

The new composition triangle exists. The original central triangular boundary remains unfilled. Its winding is an arbitrary integer, not an integer modulo three. Three edges in a cycle do not impose a third-power identity.

The nerve of this groupoid is generated in every dimension by finite composable strings. Its face maps compose adjacent arrows, and its degeneracies insert identity arrows. Associativity follows from integer addition. The all-dimensional mathematical result is that this nerve is 1-Segal and 2-coskeletal; it is also Kan because all arrows are invertible. These properties do not require the original central loop to be nullhomotopic. Its realization has the homotopy type BZ, hence S1.

This gives a concrete positive example of conjecture C1 under a declared path-completion policy. It does not establish that Su-32's source selects that policy. Raw construction words and their derivation trees may be stored alongside semantic normal forms. Normalization of an arrow does not recover the raw word, and no permission to discard those retained histories is inferred.

An explicit comparison to the native deck data shows why endpoint closure is weaker than this winding test. Let the three contact locations be b_0=0, b_1=d, b_2=d+Rd. Send (i,j,n) to the displacement b_j-b_i. This preserves composition, but sends every full winding loop to zero deck displacement. Thus a deck-closed native candidate can still have nontrivial history-level winding; the latter needs its own source comparison.

## 4. The immediate fibration construction is transport over the contact cycle

Suppose actual admissible contacts carry reversible transports

    T_01:F_0->F_1, T_12:F_1->F_2, T_20:F_2->F_0.

Their full return is H=T_20 T_12 T_01. These transports extend to a functor from the free contact groupoid. Treating the fibers as discrete sets gives a covering over the geometric contact circle. If instead they are topological spaces and the transports are homeomorphisms, the corresponding construction is the mapping-torus bundle

    E_H=(F_0 x [0,1])/((x,1) ~ (H(x),0)),
    F_0 -> E_H -> S1.

For an explicit witness that nontrivial return can survive coherent composition, take F_i=Z, let the first two transports be the identity, and the third add one. The resulting loop acts by n -> n+1. This is a diagnostic model, not a native payload law.

If all three transports are only complete presentations of the same globally identified wire assignment, T_ij=R_j R_i^(-1), then their product is exactly the identity. Their mapping torus is a product. The supplied native window note establishes a complete labelled wire regrouping, not an additional nontrivial monodromy law.

The bare three-simplex union, although homotopy equivalent to a circle, is not thereby a fiber bundle. Its intersections are points rather than homeomorphic full fibers. The bundle above is a further explicit construction from actual transport data.

This construction concerns a fibration over S1. It does not identify the contact cycle as a fiber of a Hopf bundle. Passing to a self-join and supplying a continuous circle action, as proposed earlier, would be additional operations whose admission still needs proof. No Hopf characteristic class is established here.

## 5. Next native discriminator

The concrete candidate to bind to Su-32 is now the closed step triple

    g_0-g_1, g_1-g_2, g_2-g_0.

For this candidate one must find actual block occurrences and their exact typed contact ports, verify that the coordinate permutation lifts to permitted transformations, and compute the actual composite arrow across the first two contacts. Compare it with the direct reverse of the third-contact arrow on the entire retained carrier, not just endpoint labels or an unlabelled planar picture.

The possible outcomes have different meanings. An actual source comparison can fill the loop; a retained difference can generate monodromy; absence of one of the typed contact transitions rejects this candidate placement. No result is selected in advance to preserve a desired circle or Hopf topology.

The generic path model gives both a compositional control and a distinction the native comparison must resolve. It does not replace the native comparison.

## Verification and references

Run `python check_three_contact.py --output results.json` using Python 3.10 or later. Only the standard library is required. The result file records exact arithmetic checks, the complete elementary-collapse certificates, and the finite ranges used for the nerve-identity tests. The unbounded identities have the direct algebraic proofs above; finite tests are not being substituted for those proofs.

The checker evaluates 729 coefficient displacements and finds 61 with zero three-step discrepancy, including zero. It verifies the finite simplex and flag-completion complexes, the order-three automorphism, the groupoid's sampled algebra, and face/degeneracy identities on deterministic samples through dimension six. Native port records evaluated: zero. No Agda or Lean run, repository modification, or execution of the original native Node checkers occurred.

Sources:

- Supplied `su32-native-window-operation-v1.md`, especially Global source operation and Restrict the global family to the actual window. A byte-for-byte snapshot is included as `source_native_window_note.md`.
- Jacob Lurie, Kerodon, The Nerve of a Groupoid, tag 0035: https://kerodon.net/tag/0035. Proposition 1.3.5.2 and Example 1.3.5.3.
- Kerodon, Coskeletal Simplicial Sets, tag 051Z: https://kerodon.net/tag/051Z. Example 3.5.3.4.
- Kerodon, From Categories to Simplicial Sets, tag 002L: https://kerodon.net/tag/002L, including the nerve and path-category constructions.
- Allen Hatcher, Algebraic Topology, section 4G, especially the nerve result and Exercise 2 on bundles from diagrams of homeomorphisms: https://pi.math.cornell.edu/~hatcher/AT/AT.pdf, printed pages 456-460. PDF page 468 (zero-based) was visually inspected.

The lattice, collapse, and groupoid comparison calculations are the present derivations. The cited literature supplies the general nerve and bundle interpretation, not a source-native Su-32 identification.
