# Actual source attachment, reconstruction fibers, and the cut-descent defect

Date: 2026-10-19.
Repository read: `andrey-kokoev/marici`, connected default branch. Search results identified commit `ace56bdce2a23bc7627649366c2a1bd49fc26414`.

## Outcome

This increment follows a concrete existing `/research` implementation rather than selecting another speculative WG successor. The upstream joint-record attachment checker was copied from its GitHub connector response, verified byte-for-byte by the Git blob hash, and executed without changes. It passes. New exact calculations characterize the full marginal reconstruction fiber, retain its integral cycle coordinates, and give a counterexample to reconstructing a marked source diagram from an unmarked cofiber and a terminal observation.

The central result is an exact sequence for the existing three-event, two-feature coefficient fixture:

    0 -> Z^51 -> Z^162 -> Z^63 + Z^63 -> Z^15 -> 0.

It distinguishes compatibility of the two cut observations from unique reconstruction of the joint source. The source has a 51-dimensional family of joint coefficients over each compatible pair of observations. This is not a statement that spacetime has 51 dimensions, that there are 51 new particles, or that the underlying norm-topological vector space has nontrivial homotopy groups.

## 1. Upstream implementation and provenance

Primary source note:

`research/nima/joint-records-type-as-attachment-parameters-not-cofiber-objects.md`

Blob: `b33b4d6f9883646e50648213e610f22c1d5d36da`.

Primary checker:

`research/nima/checkers/check_joint_record_interval_attachment.py`

Blob: `253c83788e7e4a23b489f836c0d8b8830026f5ff`.

The local copy's Git object hash is recomputed as SHA1(`blob <byte-count>\0<bytes>`). It matches the connector's blob hash. No claim relies on unverified manual transcription. The source is included under `source/`, and its complete output is `source_checker.log`.

Additional source note:

`research/nima/three-prime-cut-duality-locates-the-ghosts-in-the-marginal-cofiber.md`

Blob: `e055856a7444baf258d9519dc2910d6b8ecfd7b0`.

These sources distinguish marked paths, their split faithful analytical refinement, actual attachment maps, interval cofibers, and subsequent lossy terminal observations. They already prove two particular invisible source classes exist; they do not assert that those two exhaust the ambient kernel.

Canonical URLs are obtained by appending the above paths to:

https://github.com/andrey-kokoev/marici/blob/ace56bdce2a23bc7627649366c2a1bd49fc26414/

## 2. The actual attachment rule

For vertex projectives P_x in the supplied finite typed path algebra, a joint coefficient h is a map P_2 -> P_end. It is not itself a cofiber object.

At a chosen cut, let U_m = Hom(P_2,P_m), V_m = Hom(P_m,P_end), and

    Z = direct_sum_m U_m^* tensor P_m.

There is a fixed coevaluation u:P_2 -> Z. A joint coefficient h determines v_h:Z -> P_end, with

    v_h u = h.

Reading v_h at the named typed units recovers h exactly. The upstream code tests this on every one of the 18 diamond and 162 three-event joint basis elements.

The filtration is

    0 -> P_2 --u--> Z --v_h--> P_end.

Its interval cofibers and their comparison are constructed from u and v_h. The cone-of-cone calculation retains the specified nullhomotopy; it does not replace a nonzero chain map by the zero chain map.

Thus the branch supplies actual attachment maps and comparison homotopies. Merely storing a record, forming an attachment, and passing to the equivalence class of its cofiber are three different operations.

## 3. The exact cut diagram

The source goes from 2 to 60 by inserting the distinct prime directions 2,3,5 in any of six orders. Every event slot has three possible basis labels: 0 (retained empty-event slot), 1, or 2. The full typed joint coefficient space J has dimension 6*3^3=162.

For a full basis path `(vertices,letters)`, the two marginal observations are:

    A: (v_1, delete_zero(letters[:1]), delete_zero(letters[1:]))
    B: (v_2, delete_zero(letters[:2]), delete_zero(letters[2:]))

Each has 63 coordinates. Terminal composition deletes the remaining cut and intermediate-vertex labels and all zero letters. Its outputs are all words over {1,2} of lengths 0 through 3, giving dimension 1+2+4+8=15.

Write L:Y_left -> T and R:Y_right -> T for the terminal maps. Direct construction verifies

    L A = R B = Q.

Put M=(A,B) and Delta=(L,-R). Then Delta M=0.

The computed ranks over Q are:

    rank A = rank B = 63,
    rank M = 111,
    rank Q = rank Delta = 15.

The integral results below prove these are not artifacts of a floating-point tolerance or a special characteristic.

## 4. Why compatibility is sufficient for existence but not uniqueness

Make a bipartite graph with the 63 left marginal coordinates and the 63 right marginal coordinates as vertices. Each of the 162 joint basis records is an edge joining its two observations. Multiplying the right block of M by -1 turns M into its oriented incidence matrix D.

Each connected component is labelled by one terminal word. There are 15 components. They are connected within that word: the checker explicitly constructs a spanning forest. Hence

    rank D = 126-15 = 111,
    rank H_1(graph;Z) = 162-126+15 = 51.

A forest gives a primitive integral fundamental-cycle basis K with 51 columns. It has an identity submatrix on its 51 non-tree edges, so its columns are independent and generate the whole integral cycle lattice. The checker verifies M K=0 and exact reconstruction on every joint basis element.

The last map Delta sums left demands minus right demands within each terminal-word component. Therefore its kernel is exactly the image of M, over Z. Its cokernel is zero. This proves

    0 -> Z^51 --K--> Z^162 --M--> Z^126 --Delta--> Z^15 -> 0.

In particular, a pair (a,b) is compatible precisely when L(a)=R(b). For every compatible pair there is an integral joint lift. After one lift is selected, all lifts are its translates by im K.

The corresponding matching object is

    P = Y_left x_T Y_right,

of linear dimension 111. The comparison J -> P is surjective but is not an equivalence. In the derived category of cochain complexes concentrated in degree zero, the derived pullback is also represented by P because Delta is surjective; the comparison fiber is K in degree zero. This is a derived-linear statement, not a claim about the ordinary topology of C^162.

## 5. Source-derived loops, not added memory coordinates

For a terminal word of length 0 or 3, the corresponding bipartite graph has six vertices and six edges: one cycle. There are 1+8=9 such components.

For a terminal word of length 1 or 2, its component has twelve vertices and eighteen edges: cycle rank seven. There are 2+4=6 such components.

Consequently the geometric realization of this *specific incidence graph*, before any further cells are attached, has homotopy type

    disjoint_union_(9 copies) S1
    disjoint_union
    disjoint_union_(6 copies) (wedge_(7 copies) S1).

This graph is a diagnostic constructed from the actual marginal maps. It is not asserted to be the whole native source realization. Its 51 abelianized cycle coordinates already exist in the joint records. They need not be postulated as an extra memory sector.

## 6. A reversible reduced presentation

Choose a spanning forest F and retain the choice as presentation data. Given a compatible pair (a,b), solve the tree incidence equation with zero values on the non-tree edges, obtaining h_F(a,b).

For any joint coefficient h,

    h = h_F(Ah,Bh) + K_F z_F(h),

where z_F(h) reads the 51 non-tree edge coefficients.

This is an exact linear representation using the compatible cut observations and their residual cycle coordinates. It is not a global physical selection of a preferred forest.

The checker constructs two different forests, proves both reconstruct all 162 basis vectors, and verifies that their kernel-coordinate transition and inverse are integral matrices whose products are identity. The transition determinant is +/-1. Over nonzero observations the change of residual coordinates is affine because the two selected tree lifts can differ.

The actual cut diagram is compatible with all six permutations of the three prime-direction names. The diagram's equivariance is checked. An arbitrary chosen forest is not claimed invariant under those permutations; its record must be transported as part of the presentation.

Discarding both cut labels and event positions entirely leaves only Q(h). That map has rank 15 and kernel dimension 147. The 51-dimensional marginal kernel and the 147-dimensional terminal kernel are different losses and must not be conflated.

## 7. Prepared source and fixture dependence

The primary source also carries 48 marked source histories. The full 162-dimensional ambient joint space should not be relabelled as 162 independent prepared physical source histories.

Using the exact two-component complex event features in the retrieved checker, the preparation matrix has rank 48. Its paired marginal image has rank 44, leaving four invisible combinations. By retained degree:

    degree 0: 6 -> 5  (kernel 1),
    degree 1: 18 -> 15 (kernel 3),
    degree 2: 18 -> 18 (kernel 0),
    degree 3: 6 -> 6 (kernel 0).

Both previously exhibited source ghosts are independently verified. They are not the entire kernel of this particular two-component fixture.

A separately declared control replaces the event features with seven independent chamber-coordinate vectors. It has paired marginal ranks [5,17,18,6] in the same degrees, hence total rank 46 and kernel dimension two. This distinguishes structural source ambiguity from extra collapse introduced by a small feature realization. The control is not an analytical completion theorem about the physical spectral family.

## 8. Equal terminal records and isomorphic bare cones do not recover a marked diagram

In the actual diamond model, joint coefficients form two 3-by-3 blocks H_4,H_6. Construct

    h0: H_4=I3, H_6=I3,
    h1: H_4=diag(1,1,3/2), H_6=diag(1,1,1/2).

The two joint coefficients are distinct but have the same terminal word coefficients: contributions from the two internal paths add to the same result. The named typed-unit readout distinguishes them exactly.

Their attachment maps v0,v1 have shape 25-by-24 and rank 24. There is an explicit invertible diagonal D on the 24-dimensional middle projective input such that

    v1 = v0 D.

It multiplies the coefficient-dual block with first letter 2 by 3/2 on the m=4 branch and by 1/2 on the m=6 branch, leaving the others unchanged. Therefore (D,id) is a chain isomorphism of the two *underlying vector-space mapping cones*. Each cone has H^-1=0 and H^0=C.

But D u != u, and v1 u=h1 != h0=v0 u. No intertwiner fixing the specified source and final endpoint maps can identify the whole filtrations: such an intertwiner would force h1=h0 after composition with u.

This does not claim the two full module diagrams are equivalent, or that every physical observer distinguishes them. It proves that the isomorphism class of an unmarked, underlying-vector-space cone, even combined with the specified terminal record, is insufficient to reconstruct this labelled source attachment.

## 9. Recursive information budget in this declared family

For n distinct independent event directions and two nonzero letter labels, the full ordered joint basis has n!*3^n elements. The terminal word basis has

    sum_(k=0)^n 2^k = 2^(n+1)-1

elements. Terminal composition is onto: every output word has a lift obtained by choosing a direction order and padding with zero event slots. Consequently

    dim kernel(Q_n) = n!*3^n - (2^(n+1)-1).

A word of length k has n!*binomial(n,k) preimages. These disjoint fibers give an immediate exact rank certificate. The checker verifies the fiber formula through n=5.

This is the budget for the specific finite event-record family, not a lower bound for all possible WG encodings, tensor networks, or physical states. Recursive compression can remain faithful by retaining an appropriate residual representation; equality of terminal observations cannot establish that such a representation has been retained.

## 10. Structural synthesis consequence

The next stronger condition is not merely that a source/rung square commutes. It is whether its source-to-matching map is an equivalence, or what its reconstruction fiber is.

The existing model demonstrates the distinction exactly:

- Full typed coefficients embed faithfully into actual attachment maps and are recovered by typed-unit readout.
- Reassociation/cofiber comparison has an explicit homotopy.
- The two cut marginals obey the complete terminal compatibility equation.
- Their comparison to the full source nevertheless has an exactly computed nontrivial fiber.
- Passing to a bare cone or terminal observer forgets additional source structure.

Thus there is a concrete source-defined family of spaces of compatible reconstructions. In this linear fixture each nonempty reconstruction fiber is an affine space modelled on ker M. The incidence graph supplies a corresponding combinatorial cycle description. No identification with the intended T9 or an all-physics universal space is claimed.

## Reproduction

Requirements: Python 3 and SymPy.

From this folder:

    python source/research/nima/checkers/check_joint_record_interval_attachment.py
    python check_actual_attachment.py

The first command executes the unchanged upstream checker. The second verifies the source hash, uses its actual PathModel and attachment/readout code, and executes the new exact tests. Outputs:

- `source_checker.log`: fresh upstream run output;
- `source/research/nima/results/joint-record-interval-attachment.json`: fresh upstream receipt;
- `actual_source_attachment_results.json`: new calculation results;
- `marginal_chain_certificate.json`: integer maps, fundamental-cycle basis and coordinate-change matrix;
- `extension_checker.log`: fresh extension run output.

No proof assistant was executed. No remote repository file was changed. All computations were performed in a local copy under /mnt/data.
