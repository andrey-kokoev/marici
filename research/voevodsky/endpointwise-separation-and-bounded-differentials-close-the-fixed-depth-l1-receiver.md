# Endpointwise separation and bounded differentials close the fixed-depth l1 receiver

## Result, with the completion specified

For the increasing monotone finite-prime source, fixed relation depth r, fixed normalized feature carrier and weights, there is a continuous injective associated-layer map on the endpointwise weighted-l1 completion. Its balanced target is a Banach complex with bounded differential. The finite relative pairing and pentagon identities extend to this complex in the integrated-form sense already established.

This is a statement about a particular summable direct-limit completion of coefficient layers. It is not an injectivity theorem for arbitrary projective-limit families, not a uniform lower frame bound, and not a claim that all homology commutes with completion.

Inputs:
- `../grothendieck/packet-refinement-preserves-the-relation-tower-but-coarse-seams-lose-higher-products.md`
- `../nima/nonminimal-relation-factorizations-descend-through-balanced-seam-complexes.md`
- `../nima/the-balanced-relative-seam-construction-satisfies-the-finite-pentagon.md`
- `weighted-theta-tails-and-path-length-domains-give-uniform-seam-bounds.md`
- `the-relative-normalization-pentagon-extends-to-the-cut-l1-completion.md`

## 1. Fixed endpoint intervals stabilize

Index vertices by finite prime subsets (or their specified arithmetic labels). Paths add primes monotonically. For fixed endpoints x<=y, every intermediate vertex is contained in y and contains x. No newly adjoined prime can enter and then leave such a path.

Consequently the entire path corner, record kernel corner, and associated-layer corner G^r_(x,y) stabilize once the packet contains y. Each is finite dimensional: the interval has finitely many vertices, marked paths, and r-factor presentations. Refining shell coordinates changes none of the actual old forcing functions.

This is the convex-corner property from the source tower, not an assumption that larger packets have no new endpoint corners.

## 2. Source norm and closed balancing quotient

For each endpoint pair c=(x,y), let P_c be the finite-dimensional r-factor relation presentation, equipped with the norm induced from its finite marked-path tuple expansion using weight

    (1+n)^r a^n,

where n is total event length and a is the fixed uniform letter bound from the theta-tail note. Let K_c be the kernel of multiplication to G^r_c. It includes action balancing and the factors mapping into I^(r+1). The finite source theorem identifies this quotient and supplies its injective balanced analytical map.

Set

    P = l1 direct_sum_c P_c,
    K = {p in P : p_c in K_c for every c}.

Each K_c is closed. Hence K is closed, since coordinate projections are bounded. Truncating the endpoint support shows K is exactly the closure of the algebraic direct sum of the K_c. The Banach quotient is canonically

    P/K = l1 direct_sum_c (P_c/K_c),

with quotient norms on each finite corner. To verify the norm identity, minimize separately in each coordinate for one inequality; for the other choose approximating lifts with a summable sequence of errors. Finite-dimensionality also gives attainment if desired.

Thus completing this presentation does not add unidentified balancing relations between different endpoints. This conclusion depends on retaining endpoints and the l1 norm; it is not automatic for other topologies.

## 3. Completed injectivity needs no uniform inverse

Let Y_r be the completed cut-l1 balanced target in bottom degree, with every outer endpoint retained. The source path bound and contractive normalization give a bounded map P->Y_r, vanishing on K. Let j:P/K->Y_r be the induced map.

For every c, its component is exactly the stabilized finite map

    j_c:G^r_c -> (Y_r)_c.

That map is injective by balanced function-valued descent. Both source and target endpoint projections are continuous and commute with j. If j(v)=0, then j_c(v_c)=0 for every c, whence v_c=0 for every c. An l1 sequence with all coordinates zero is zero. Therefore j is injective.

The norms of the finite inverses may diverge with c. No inverse bound was used. The image need not be closed and an approximate-null sequence can still exist. What is excluded is a nonzero element of this summable completion with identically zero observation.

This concerns coefficient layers. It does not substitute their dimensions for full receiver modules or discard the actual root/state factors in those modules.

## 4. A bounded differential on the normalized target

Use the untruncated shape-graded memory carrier. A seam term has prefix memory, one vacuum/feature seam letter, and suffix memory. Its boundary inserts that letter into one adjoining memory buffer and replaces the seam edge by its appropriate endpoint vertex, with the usual two signs.

The vacuum insertion has norm one. A feature insertion changes its norm multiplier from sqrt(w_seam) to tau, so its norm is at most

    lambda=max(1,tau/sqrt(w_seam)),

assuming the fixed seam weight is strictly positive. For edge-dependent weights the same argument requires a finite supremum of these ratios. These are positive carrier norms; no signed self-pairing inverse is involved.

Each insertion is a tensor reassociation on a fixed shape. When different shapes land in the same output, the l1 triangle inequality handles the collision. Thus a single seam boundary has norm at most 2 lambda. At depth r, the tensor differential has at most r such terms and

    ||d|| <= 2 r lambda.

Signs have modulus one. This bound holds in every cohomological degree, including mixed edge/vertex terms. Algebraic tensor records are dense, so d extends uniquely to a bounded, everywhere-defined operator on the Banach complex. Its square is zero by continuity from the algebraic identity. It is therefore closed.

This uses the shape-l1 norm, not Hilbert-Fock multiplication across unrestricted degree sums, and not a capacity projection that destroys records.

## 5. Coherence and bottom homology

The bounded normalizations and balanced associators commute with d on the dense algebraic domain. Continuity extends the chain identities. The finite pentagon, including its tensor-of-shifts signs, therefore extends as a chain comparison in this fixed-depth Banach model, in addition to the previously extended relative-packet identity.

The image of j lies in ker d, because this is true in every finite corner and d is continuous. The r-fold complex has no degree below -r. Thus no boundaries enter its bottom degree, even after this completion. The injected completed layer is detected in bottom homology. This says nothing about possible nonclosed images of differentials in higher degrees.

The shift placing the attachment in degree -1 is still [1-r]. No new shift or inverse-limit exactness assertion is required.

## 6. Relative pairing and approximation

On the completed external presentation the source-generated collision current remains bounded and satisfies

    q_external+T_N = N^* q_balanced.

It annihilates K after the associated-layer source map, so the corrected sum has the completed balanced paired presentation. The separate summands need not descend. Neither injectivity nor this formula implies a nondegenerate restricted self-form.

Theta truncations converge uniformly as operators on the stronger source weight (1+n)^(r+1) a^n, with the explicit error from the tail note. This supplies a dense stronger domain for quantitative approximations while injectivity above concerns the stated r-weight quotient completion.

## 7. Remaining scope

Closed for this fixed-depth summable completion: source-layer separation, bounded seam differential, relative paired descent, and balanced pentagon coherence.

Still not established: a bounded inverse or closed range for j, arbitrary inverse/projective-limit noncollapse, simultaneous uniform control over all depths r, a canonical physical choice of this completion, or positivity of the source self-form. The infinite typed source algebra is handled cornerwise here; no global hereditary assertion for a new completed algebra is used.

## Verification

`uv run python research/voevodsky/checkers/check_completed_seam_domain_controls.py`

Passed 680 mixed-degree differential-square fixtures and 120 convex endpoint-interval fixtures. The completion and injectivity arguments are the proofs above, using the previously checked finite balanced injections. These finite regressions are not a sampled-rank proof of completed injectivity.
