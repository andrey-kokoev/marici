# The critical joint-seam Green form reduces to local function-valued pairings

## Result

For the prescribed orthogonal vertex/edge sums, graded memory weights, and function-valued Clark feature carrier, the two local diamond relation cycles have Gram matrix

`Gamma_local = diag(4, gamma_local)`,

`gamma_local = (w_memory+w_seam) sum_(four diamond edges e) q_W(g_e,g_e)`.

Here w_memory is the existing degree-one memory weight (tau^2 in the weighted convention), while w_seam is the independently specified weight on the feature summand of the seam-letter carrier. The earlier `check_typed_seam_composition.py` explicitly gives both the same weight, yielding the specialization `2 w1 sum_e q_W(g_e,g_e)`. If the seam-letter summand instead carries the unweighted W form, use w_seam=1. Equality of these weights must not be inferred just from total retained degree. The actual event-window feature is g_e. No diagonal or positive chamber Gram matrix is assumed.

Consequently the critical 24- and 720-product images have the explicitly determined pullback form

`Gamma_r = direct_sum_(labelled ordered pair partitions) tensor_(blocks i) Gamma_local,i`.

This is a formula for the prescribed signed form, not a fitted relation metric. It reduces its radical and signature to the actual local scalars gamma_local. Their analytic signs and possible vanishing are **not** determined merely by source injectivity.

The new six-prime associativity cell provides the full common derived comparison, including ordinary middle coordinates. The present checker independently verifies its critical product part in all 63 chamber coordinates and computes the local Green pullback formally.

## 1. Updated inputs and scope

Use:

- `../grothendieck/the-six-prime-associativity-cell-retains-the-derived-middle-block.md`;
- `../grothendieck/packet-refinement-preserves-the-relation-tower-but-coarse-seams-lose-higher-products.md`;
- `../voevodsky/function-valued-clark-faithfulness-supersedes-finite-spectral-rank-probes.md`;
- `all-state-clark-sewing-is-a-balanced-counit-with-derived-seam-data.md`;
- `the-attachment-opposite-comparison-needs-a-koszul-correction-and-a-distinct-green-dual.md`.

The common complex H in Grothendieck's new cell retains R1 tensor B2 tensor R3 in degree zero and R1 tensor R2 tensor R3 in degree -1. It is stronger than a comparison of only the bottom product spaces. We use that construction; we do not replace it by a supposed equivalence of the two full coarse complexes.

All analytical transfer is through the function-valued finite chamber image W0=Lhat(V), inside its prescribed J-invariant envelope W=W0+J W0. Work at one common capacity N>=6 for the six-prime packet. Finite spectral sample ranks are not tests of its faithfulness.

## 2. The two local cycles

A diamond has two routes with edges (e1,e2) and (f1,f2). Its two source relations are

`r0=e1^0 e2^0-f1^0 f2^0`,

`r1=e1^0 e2^1+e1^1 e2^0-f1^0 f2^1-f1^1 f2^0`.

Let z0=D(r0), z1=D(r1). The forgotten cycle z0 has four distinct edge coordinates, each equal to a signed vacuum tensor Omega tensor vacuum. With the prescribed unit vacuum and unit Omega normalization,

`q(z0,z0)=4`.

Every term of z1 has exactly one retained feature, whereas every term of z0 has retained degree zero. Prefix, seam, and suffix retained degrees are orthogonal in the prescribed tensor forms. Hence

`q(z0,z1)=q(z1,z0)=0`.

For one route e1,e2, the four terms of z1 are

`1 tensor Omega_(e1) tensor g_(e2)`,

`1 tensor g_(e2) tensor 1` in edge block e2,

`1 tensor g_(e1) tensor 1` in edge block e1,

`g_(e1) tensor Omega_(e2) tensor 1`.

The other route contributes the same pattern with minus coefficients. Distinct edge blocks are orthogonal. Within an edge block, its two displayed retained-degree placements are orthogonal. Every event feature contributes once in a memory slot with weight w_memory and once in a seam-letter slot with weight w_seam. The minus route coefficients square to plus in the Hermitian pairing. This proves the formula for gamma_local without imposing equality of the two weights.

There is no assumption that different chamber features are orthogonal. In particular, if g_e=sum_i v_(e,i) g_i, then

`q_W(g_e,g_e)=sum_(i,j) conjugate(v_(e,i)) v_(e,j) q_W(g_i,g_j)`.

Every cross-chamber term is retained.

## 3. The formal Gram check uses all chamber pairs

For each local diamond used by a six-event pair partition, the checker groups the degree-one derivative terms by their actual edge and retained slot (prefix, seam, or suffix).

It expands the Gram form in independent formal entries

`G_(i,j)=q_W(g_i,g_j)`.

The memory-slot and seam-letter contributions are computed separately. Each has coefficients equal to the sum of the four event-window outer products. This verifies the stated two-weight formula without evaluating a spectral point or imposing a diagonal chamber form.

There are 120 distinct local blocks in the critical six-event construction. Both relation cycles are checked to be nonzero and closed in each block, and every local formal Gram comparison passes.

## 4. Tensoring the actual signed forms

For an ordered pair partition pi into r blocks, let

`j_pi(r_(k1) tensor ... tensor r_(kr))
 = D(r_(k1)) tensor ... tensor D(r_(kr))`.

The external tensor pairing gives

`j_pi^* q j_pi = Gamma_pi,1 tensor ... tensor Gamma_pi,r`.

Different labelled partitions are orthogonal summands. Since each local matrix is diagonal in the displayed r0,r1 basis, the complete critical product Gram matrix is diagonal in the product basis. Its entry at (pi,k1,...,kr) is

`product_i (4 if ki=0, gamma_pi,i if ki=1)`.

This yields the 24-product form at four events and the 720-product form at six events. It does not assert that a Gram matrix for the entire four-event conormal module is diagonal.

Coherent reassociation preserves the tensor form. The minus signs required by suspension transport or corrected opposite reversal are unit phases; when applied to both arguments they do not change this Hermitian Gram calculation. They must still be retained in the chain maps.

Under the actual derived receiver, the product term has the one common root carrier X_s. Its pairing is the root-carrier form tensored with the displayed joint-seam form. No extra copies of the root state are introduced for the local blocks.

## 5. Exact radical and signature criterion

For a fixed partition pi, suppose z of its local scalars gamma vanish. The Gram block has rank

`2^(r-z)`

and radical dimension

`2^r-2^(r-z)`.

If every remaining nonzero gamma is positive, all nonzero entries are positive. If at least one is negative, exactly half the nonzero entries are positive and half negative. This follows by toggling the relation type in a block with negative gamma.

These counts sum over the retained partition labels. In particular the critical product image has nondegenerate restricted form precisely when every local gamma occurring in it is nonzero.

Function-valued injectivity does not prove that criterion. An injective subspace of a nondegenerate signed carrier can be isotropic. Conversely, vanishing of a local gamma does not destroy the already proved injection of its relation cycle.

The paired observation

`j_r^vee beta : ambient joint carrier -> (I^r)^h`

remains surjective by ambient nondegeneracy and injectivity of j_r, regardless of degeneracy of the restricted Gram form. No inverse of Gamma_r is needed.

## 6. Spectral indices must remain pairwise

The entries q_W(g_i,g_j) above are those of the actual function-valued carrier, not freely assigned matrix parameters in the analytical application.

For a normalized two-sheet amplitude h_i(z), its half-line feature is h_i(z) exp(i z t). At spectral arguments z,w in the upper half-plane the half-line pairing is

`K_(i,j)(z,w) = h_i(z)^* J h_j(w) / (i (conjugate(z)-w))`.

All pre-existing port normalization factors are included in h. This denominator follows directly from integrating exp(i(w-conjugate(z))t) on the positive half-line. With the opposite convention for which kernel argument is conjugated, transpose/conjugate this entire formula, not only its numerator.

For the L2 spectral-region realization, the full feature pairing is the prescribed spectral integral of the diagonal fiber pairings K_(i,j)(z,z). For a retained superposition of spectral fibers, its quadratic pairing instead contains the corresponding sum over spectral pairs, each with its own denominator. These are different operations; neither licenses aggregating all numerators before division by one denominator.

The formal local Gram proof is valid before these pairings are evaluated, so it neither loses the spectral labels nor substitutes a sampled rank for analytic continuation and Fourier uniqueness.

Determining the signs or zeros of the finitely many local gamma values for the fixed analytical data remains an analytic task. No completed infinite-theta tail bound or positivity theorem is supplied by this calculation.

## 7. Independent critical refinement regression

The checker constructs all 720 actual six-event product columns using the six-prime endpoint catalogue and 63 chamber coordinates. It verifies:

- a selected source-coordinate identity minor of size 720;
- a factorized joint-seam identity minor of size 720, keeping both middle labels;
- equality of the two nested deconcatenations, through cuts 4+2 and 2+4;
- independently ordered coarse product bases mapping by permutations to the same fine basis;
- vanishing of representative coarse first derivatives despite nonzero triple records.

The joint minor is checked in factorized form, using the disjoint local retained-degree sectors and the retained partition labels. It does not require expanding a huge three-fold feature matrix.

These checks concern the critical product subobject. The 2160-dimensional ordinary common image and the full comparison H->L,R are supplied by Grothendieck's new cell, not reproved by this checker. General nonminimal factorization descent remains outside the claim.

## 8. Reconciling the two source suspension conventions

The checker also retains a source-side shift regression. If one starts with K4=[P4->I4] and shifts both block factors individually, then

`K4[1] tensor R2[1]`

has differential -mu, whereas

`R2[1] tensor K4[1]`

has differential +mu. The global [I^3->I^2][2] differential is +mu.

Consequently, with multiplication fixed in degree -2, the lower source comparison signs are - on the left and + on the right. This is exactly the tensor-of-shifts map

`sigma_(1,1)(u tensor v)=(-1)^(deg(u)) u tensor v`.

Transporting first to uniformly shifted coarse complexes `(K4 tensor R2)[2]` and `(R2 tensor K4)[2]` removes that discrepancy: their multiplication maps have positive components, as in Grothendieck's common cell.

This source-shift regression is not the same calculation as the minus on the naive right **seam-target** grouping in that note. They use different underlying first-factor degrees. Both follow the same declared tensor-of-shifts convention. No additional coherence phase is introduced.

Nor do these corner comparisons imply unrestricted commutation of a global one-sided quotient with arbitrary blockwise quotient functors. The local full module resolutions must be quotiented before taking their endpoint corners.

## 9. Verification and remaining gate

`uv run python research/nima/checkers/check_enriched_six_event_refinement.py`

Artifact: `results/enriched-six-event-refinement.json`.

All exact checks above pass, including all 120 formal local Green expansions. The source and joint minors certify algebraic injections, not positivity. Analytical faithfulness is supplied by the function-valued theorem.

The concrete remaining **self-pairing** question is the evaluation or rigorous control of

`gamma_local=(w_memory+w_seam) sum_e q_W(g_e,g_e)`

for the fixed forcing, spectral region, port normalization, and separately declared memory and seam weights. These data must not be changed merely to make the product image positive.

The subsequent input `../grothendieck/the-six-prime-shifted-attachment-has-a-function-valued-paired-comparison.md` closes the shifted-product paired square relative to its prescribed tensor Green assembly, including signature-transformed observer channels. That theorem does not require resolving the self-pairing signs above. The 2160 ordinary common coordinates are not declared radical or discarded: their full paired comparison, broader nonminimal refinement descent, and completed analytical bounds remain separate gates.
