# Capacity bonding is inverse, and the cut-l1 seam differential is bounded

## Strength and result

At a fixed source, fixed feature carrier, and fixed seam depth:

- capacity truncations are inverse algebra and chain maps;
- the obvious direct inclusions have an explicit top-degree chain defect;
- normalization and its collision/loss currents commute with capacity change in a relative square;
- the capacity inverse limit is the formal retained-degree completion;
- uniformly bounded compatible families in the specified cut-l1 norm are exactly the cut-l1 states;
- the untruncated seam differential is bounded in that topology at fixed depth.

Voevodsky has separately proved that last bound and the completed chain pentagon, together with injectivity of the endpointwise weighted-l1 source completion. The new contribution here is capacity bonding, its relative boundary square, and the comparison between formal, cut-l1, and dual observation topologies. Voevodsky also proves that the source image is nonclosed; a bounded inverse is therefore excluded, not merely unproved.

## 1. Fixed common graded carrier

Fix a finite source packet, the normalized signature-closed feature envelope W, and the existing memory and seam weights. Let R_infinity be the typed coefficient algebra with the algebraic full tensor algebra T(W) in each admitted endpoint block. Let R_N be its capacity-N quotient.

The maps

p_N:R_(N+1)->R_N

kill words of length N+1. They are surjective algebra maps. The forward word inclusions are linear isometries for the declared graded norms but are NOT algebra maps: a product killed at cap N can survive at cap N+1.

Use the same analytical arrow space K at every capacity. Its forgotten seam letter has retained degree zero and its feature summand retained degree one. Form T_N and the r-fold balanced complex J_(N,r) over R_N.

Normal-form coordinates have r+1 coefficient buffers and r seam-or-cut markers. Applying p_N to every buffer, and identity to the arrow factors, gives

P_N:J_(N+1,r)->J_(N,r).

The algebra-map property makes P_N a surjective chain map. These maps compose strictly. The same applies to the unbalanced external complexes.

## 2. The direct inclusion has a relative boundary

Let i_N be the degreewise word inclusion in the opposite direction. Set

partial_N=d_(N+1) i_N-i_N d_N.

Only a retained seam feature entering a buffer already at length N can contribute. Such a term was zero at the smaller cap and survives at the larger one. Forgotten seam letters produce no such defect.

Since P_N i_N=id,

partial_N=(1-i_N P_N) d_(N+1) i_N,

P_N partial_N=0.

Also d_(N+1) partial_N+partial_N d_N=0. Thus partial_N represents the connecting map into ker(P_N)[1] for the capacity short exact sequence. The chosen graded section has exposed the comparison cell rather than supplying a false direct chain map.

The exact two-letter fixture from cap one to cap two has a nonzero inclusion defect of rank 16. This certifies failure of that section to be a chain map; it is not by itself a claim that the connecting class is nonzero in every derived category.

## 3. Contragradient variance

The prescribed graded pairings make P_N the Green mate of the word inclusion:

P_N^sharp=i_N.

This does not contradict section 2. The mate of the primal chain map acts on the Green-DUAL complexes, with their cochain dual signs, rather than on the original differentials. Accordingly i_N is a chain map in that dual presentation.

The primal capacity system is inverse. Its finite contragredient observation system is direct. Neither should be substituted for the other when defining a completed receiver.

## 4. Normalization commutes with truncation

Write M_N:U_N->Y_N for the unbalanced-to-balanced normalization. The square

P_Y M_(N+1)=M_N P_U

commutes on all finite input memories, including those at the cap. This is associativity of the actual truncated coefficient maps, not an assumption that inclusions intertwine multiplication.

Let T_N be the independently constructed collision-plus-capacity-loss current of M_N. Let Lambda_U and Lambda_Y be the pure capacity currents of P_U and P_Y. They are the negative forms on the discarded orthogonal degree blocks, so

P_U^* q_(U,N)=q_(U,N+1)+Lambda_U,

P_Y^* q_(Y,N)=q_(Y,N+1)+Lambda_Y.

The relative square is

Lambda_U + P_U^* T_N
 = T_(N+1) + M_(N+1)^* Lambda_Y.

Both sides are the source current for the same composite partial word map: normalize then truncate, or truncate then normalize. A match created at the first step and killed at the second carries its loss term, rather than remaining a spurious positive collision.

Every slot retains its spectral pair and the supplied tail-current channels. The cutoff itself contributes a degree-boundary channel; it is not a new forcing source.

## 5. Associated-layer and attachment compatibility

For a fixed source packet of maximum path length m, take N>=m. The coefficient kernel I is then independent of N. The balanced maps

G^r[r] -> J_(N,r)

commute with P_N: all their source-produced words and the actual feature functions are unchanged. The same is true after the attachment shift [1-r] and composition with the connecting map.

For the prepared right modules X_N, their projections are source-linear and induce natural maps of exact derived receivers on fixed perfect source objects. Consequently their connecting-map squares commute as well. The forward all-state memory inclusions are not silently promoted to such module maps.

These statements keep the full endpoint module structure. A noncritical endpoint-corner dimension is not substituted for a multiplicity of root states.

## 6. Formal inverse limit and its topology

Give J_(infinity,r) the TOTAL retained degree: add all buffer word lengths and the degrees of its retained seam letters. The differential preserves this degree.

Let F^d denote total degree at least d. For the balanced complex,

F^((r+1)N+r+1) is contained in ker(J_infinity->J_N),

ker(J_infinity->J_N) is contained in F^(N+1).

Indeed there are r+1 buffers, each of length at most N in a surviving coordinate, and at most r retained seam letters. Thus the capacity and total-degree filtrations are cofinal. The unbalanced complex has the analogous bound with 2r buffers.

At fixed finite packet and depth, every total-degree piece J_d is finite dimensional. Therefore

lim_N J_(N,r) = product_(d>=0) J_d

as a formal topological complex. This declares an actual product topology, not an unspecified analytical completion.

Its cohomology is product_d H(J_d). Equivalently it agrees with the inverse limit of the finite-capacity cohomologies: the finite-dimensional homology towers satisfy the Mittag-Leffler condition, and each fixed total grade eventually stabilizes. There is no additional inverse-limit homology obstruction in THIS fixed finite-packet formal system.

This says nothing yet about analytical source quotients or an increasing infinite prime packet.

## 7. The formal limit is larger than an analytical receiver

For a nonzero memory feature g, the compatible coefficients

sum_(k<=N) k! g^(tensor k)

define a formal inverse-limit state. For every positive fixed memory weight, its weighted Hilbert norm and its cut-l1 norm diverge. Successive term norms have ratio (k+1) tau ||g||, which eventually exceeds any fixed bound.

Thus arbitrary compatible families cannot be declared analytically convergent. A scalar Green pairing is not automatically defined on two arbitrary formal series either. One may retain its graded coefficient packet, or pair a formal state with a finite-support observation; summing to a scalar requires an analytical domain.

The continuous dual of the fixed-packet product topology is the direct sum of the finite graded duals. This is the formal pro/ind observation pairing, not a Hilbert self-duality theorem.

## 8. Capacity criterion for the supplied cut-l1 completion

Voevodsky supplies a different completion: the l1 sum of the fixed shape Hilbert spaces, over the compatible union of admitted records, with old weights and feature functions unchanged. Denote the resulting untruncated seam space by X_1.

Capacity projection deletes whole memory-degree shapes, so it is contractive on X_1. Its underlying word inclusion is isometric as a linear map. For a compatible family x_N, the coefficients on surviving shapes are fixed, and

||x_M-i_(N,M)x_N||_1=||x_M||_1-||x_N||_1, for M>=N.

Consequently a compatible family represents an X_1 state if and only if sup_N ||x_N||_1 is finite. In that case the partial vectors are Cauchy and converge uniquely in X_1. This is a proof using the positive l1 sum and monotone shape projections, not the invalid general inference that uniform boundedness alone implies completion.

It excludes extra bounded ambient families at this fixed topology. It does not prove that a completed source ideal or associated-layer quotient is separated or faithfully embedded.

## 9. The fixed-depth seam differential is bounded

Use the supplied untruncated cut-l1 carrier, with unit vacuum weight, memory weight tau, and uniform positive feature seam weight w_seam. Each differential branch does one of two things:

- moves a forgotten seam letter into a memory unit, with norm factor one;
- moves a feature seam letter into an adjacent memory, with norm factor tau/sqrt(w_seam).

For each fixed shape this is ordered Hilbert tensor reassociation with the stated scalar factor. There are at most two branches per active seam. The l1 sum controls collisions of output shapes independently of their multiplicities. Hence at depth r,

||d|| <= 2r max(1,tau/sqrt(w_seam)).

The bound is independent of path length, packet cardinality, and memory degree under these fixed weights. It bounds the SEAM DIFFERENTIAL, not the source path derivative, whose separate path-length estimate is supplied in Voevodsky's work.

This is the differential estimate also proved in Voevodsky's endpointwise separation note. Thus d extends to an everywhere-defined bounded, hence closed, operator on the completed complex, and d squared remains zero by density. The given contraction normalizations and balanced associators satisfy their chain equations on a dense domain, so those equations extend continuously.

Together with the supplied finite pentagon and Voevodsky's continuous relative-packet extension, this gives the pentagon of bounded CHAIN maps on the concrete completed seam complexes at fixed depth. It does not assert closed differential RANGE or that homology commutes with analytical completion. Voevodsky's subsequent all-depth scale supplies the additional graph weights b_s(k)=(2 lambda s)^k k!, with ||d||<=1/s and balanced tensoring continuous from scale 2s to scale s. That is a specified stronger topology, not an unweighted uniform-depth claim.

Capacity projections commute with this differential. Their linear sections converge strongly to identity on X_1, and the corresponding defect tends to zero on each fixed state. It need not tend to zero in operator norm: unit inputs concentrated at the current top memory degree keep a nonzero boundary defect.

## 10. Completed contragredient observations use cut-l-infinity

The Banach dual of the cut-l1 carrier is the cut-l-infinity family of dual Hilbert shape spaces. Bounded normalizations and the bounded differential have their contragredient maps there, with reversed composition and the established cochain signs.

Finite nondegenerate beta maps must NOT be promoted to an onto map from completed cut-l1 back to its own Banach dual. Its integrated Green pairing is bounded and separating, but its beta map lands in cut-l-infinity and need not be onto.

The obstruction is already the vacuum multiplicity example: a single coarse unit observation pulls back to one unit observation on every matching fine cut. Its cut-l-infinity norm is one, while its cut-l1 norm is the number of those cuts. In an unbounded family it need not belong to cut-l1 at all.

Thus the completed paired comparison uses the actual Banach dual, not an unproved inverse beta or a bounded same-carrier Green mate. The finite Green-mate equations remain valid at each cap.

## 11. The source observation adjoint is not norm-surjective

Voevodsky's completed receiver has source unit vectors x_n in distinct endpoint corners with ||j x_n|| tending to zero. Finite-endpoint paired observations separate the source and are weak-star dense in its continuous dual, but they do not give stable norm reconstruction.

There is a stronger dual consequence. In each selected finite corner choose a norm-one functional taking value one on x_n. Their bounded product defines a continuous source functional f of norm one. For every fixed continuous target observation y^h,

|(j^h y^h)(x_n)| <= ||y^h|| ||j x_n|| -> 0.

Hence ||f-j^h y^h|| >= 1. The range of the completed observation adjoint is not even norm dense in the full source dual, although the finite observations are weak-star dense. This concerns the source inclusion j, not the finite surjective normalizations M or their mates.

Do not promote finite paired-observer surjectivity to a uniformly bounded lift of the completed source dual.

## 12. What remains

Capacity variance and its explicit relative boundary are specified here. Formal capacity completion and cut-l1 analytical completion have distinct, explicitly related domains. For Voevodsky's stated endpointwise weighted-l1 quotient, separation and faithfulness are proved; nonclosed receiver image and failure of stable inverse reconstruction are also proved.

Still separate are ranges of the differentials in higher degrees, commutation of analytical homology with completion, alternative source completions, and spectral-boundary evaluation. Voevodsky's holomorphic feature closure and additional feature-count weight now give compact-interior cross-spectral evaluation and total relative-packet convergence; that result alone does not imply separate bulk/forcing convergence. The subsequent forcing-resolved completion supplies it using independent weighted forcing estimates, without transferring it to the weaker output-only feature topology. An all-depth faithful scale-intersection receiver is now supplied by Voevodsky; it does not remove the path-length closed-range obstruction. Source quotient multiplication is now controlled with explicit scale loss in `the-completed-associated-source-is-multiplicative-with-controlled-scale-loss.md`. Nonclosed range of the receiver j is not automatically a statement about the range of d. The integrated pairing bounds alone do not authorize arbitrary point evaluation on L2. The new compact-interior theorem instead uses the actual holomorphic feature closure and a stronger feature-degree scale; it does not cover arbitrary L2 vectors or spectral-boundary points.

## Verification

`uv run --with sympy python research/grothendieck/checkers/check_capacity_bonding_and_relative_boundary.py`

Exact checks pass for inverse chain maps, the rank-16 inclusion defect, the dual chain inclusion, normalization/truncation commutation, the full relative-current square, fixed-grade stabilization, the fixed-depth differential bound, and the formal nonsummability/dual-multiplicity hostiles.

These are finite fixtures and structural proofs, not a numerical spectral-rank experiment or a completed source-faithfulness theorem.

References:

- `balanced-green-descent-includes-the-finite-capacity-boundary.md`;
- `research/nima/the-balanced-relative-seam-construction-satisfies-the-finite-pentagon.md`;
- `research/voevodsky/the-relative-normalization-pentagon-extends-to-the-cut-l1-completion.md`;
- `research/voevodsky/packet-uniform-relative-sewing-bounds-use-cut-l1-not-cut-l2.md`;
- `research/voevodsky/endpointwise-separation-and-bounded-differentials-close-the-fixed-depth-l1-receiver.md`;
- `research/voevodsky/the-completed-receiver-has-nonclosed-range-but-separating-finite-observers.md`;
- `research/voevodsky/an-all-depth-seam-scale-has-bounded-differential-and-continuous-balanced-tensoring.md`;
- `research/voevodsky/holomorphic-feature-closure-retains-completed-cross-spectral-packets.md`.
