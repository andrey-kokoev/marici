# Packet-uniform relative sewing bounds use cut l1, not cut l2

## Positive result and topology boundary

The finite relative sewing maps have packet-independent bounds on the l1 direct sum of their fine record-shape Hilbert spaces. This supplies a continuous extension of the relative form and its coarsening law on that completion. It does not yet prove a completed source receiver is faithful or that the path-derivative maps have uniform bounds.

The original orthogonal-cut Hilbert norm generally cannot supply such a bound: vacuum cut multiplicity alone makes normalization unbounded as packets enlarge. Passing to the l1 topology below changes the completion norm, not any finite Green pairing, slot weight, or source map. It must not be described as a theorem about the original l2 completion.

Inputs:
- `../grothendieck/relative-green-sewing-is-generated-by-slot-collisions-and-tail-flux.md`
- `../nima/nonminimal-relation-factorizations-descend-through-balanced-seam-complexes.md`
- `a-weighted-clark-feature-history-receiver-with-convergent-comparisons.md`
- `relative-green-currents-descend-through-balanced-factorizations.md`

## 1. A fixed normalized carrier and shape norms

Fix one upper-half-plane region and the normalized two-sheet feature carrier with signature J, J^2=1. Do not use the singular raw four-port coefficient as an invertible signature. Take the signature-closed envelope, or its closure, in this fixed carrier. Its signed pairing has norm at most one in the inherited Hilbert norm.

For a fine shape alpha, let H_alpha be the Hilbert tensor product of its feature slots, with the prescribed memory/seam weights incorporated into its positive norm. Retain root and seam factors. The signature tensor has norm at most one. Memory weights are multiplicative, and seam weights are independently fixed.

On a permitted normalization chi, a fixed fine shape maps to one coarse shape c(alpha). On that summand, U_alpha is an isometric ordered tensor reassociation: adjacent memory words concatenate at known lengths. It changes neither seam letters nor ordered feature slots. Overflow, variable weights, and operations crossing a seam are excluded.

Define

    X_fine = l1 direct_sum_alpha H_alpha,
    ||x||_1 = sum_alpha ||x_alpha||.

Use the same norm on coarse shapes. Then

    (N x)_gamma = sum_(c(alpha)=gamma) U_alpha x_alpha,
    ||N x||_1 <= ||x||_1.

This is absolute convergence, so arbitrarily many fine shapes mapping to a coarse shape cause no loss of boundedness.

## 2. Uniform relative-form estimate

Construct T_chi by new shape matches, as in the source-current theorem. For x,y in the algebraic direct sum,

    T_chi(x,y) = sum_(alpha != beta, c(alpha)=c(beta))
                q_gamma(U_alpha x_alpha, U_beta y_beta).

Cauchy--Schwarz in each prescribed signed carrier yields

    |T_chi(x,y)| <= sum_(new matches) ||x_alpha|| ||y_beta||
                  <= ||x||_1 ||y||_1.

Likewise |q_fine(x,y)| and |q_coarse(Nx,Ny)| are at most ||x||_1 ||y||_1. Thus each form extends uniquely and continuously to X_fine. The already established finite identity extends by density:

    N^* q_coarse = q_fine + T_chi.

The constant one is independent of the number of primes, cut labels, and new collisions. For two normalizations from the same fine carrier,

    |(T_L-T_R)(x,y)| <= 2 ||x||_1 ||y||_1.

Nested-cut coherence extends as well:

    T_(psi chi) = T_chi + N_chi^* T_psi.

The direct new-match estimate bounds the total correction by one, even when its decomposition into successive terms is long. No fitted triangle parameter or relation metric is involved.

These are integrated Hilbert-form bounds. Cross-spectral packets retain their indices, but arbitrary point evaluation on a completed L2 feature space is not bounded by this proof. Uniform pointwise packet bounds require a stronger analytic envelope or a separately proved evaluation estimate.

## 3. Compatible packet inclusions

For inclusions that preserve old typed shapes, slot weights, and actual forcing functions, the l1 carrier inclusion is isometric. Refining the chamber partition changes coordinates but not an old event's forcing or function-valued feature. On these inclusions the new-match rule and normalization commute literally, so the relative identity passes to the completion of the compatible union.

This assertion does not apply to arbitrary nonconvex graph changes or unrestricted inclusions of truncated memory algebras. Use the existing common-capacity source templates, or the untruncated weighted history carrier, so admitted words are never lost at a capacity boundary. Nonminimal balancing is the separate normalization operation, not an isometric inclusion of all fine labels into a quotient.

## 4. Why the orthogonal-cut l2 estimate fails

Suppose m fine vacuum records differ only by artificial cuts that normalization forgets. Their images are the same unit vacuum record. On this subspace,

    N=(1,...,1),    ||N||_(l2->C)=sqrt(m),
    T=N^*N-I=ones(m,m)-I.

For m>1 the correction has eigenvalue m-1 in the constant direction and eigenvalue -1 on its orthogonal complement. Degree weights do not suppress this effect: these are vacuum records.

Arbitrarily long intervening forgotten paths supply arbitrarily many admissible artificial cut locations at fixed seam depth. Thus the unrestricted packet tower has no uniform raw orthogonal-cut Hilbert bound for this normalization. This says nothing against the finite estimates, nor against the l1 estimate above. It does rule out transferring this completion claim back to the unmodified l2 cut topology.

## 5. Completed theta forcing: what the bound does and does not need

The estimate is in the fixed feature norm and is independent of a numerical theta approximation. It uses the actual feature carrier already admitted by the source construction. To approximate source currents by finite theta sums uniformly, one still needs an error estimate in the weighted forcing norm. Such an estimate then propagates through the tensor bounds; finite numerical convergence is not a substitute.

Likewise the map from an arbitrarily long source path to its seam derivative is not N. It is a sum over event positions and can grow with path length. The present constant-one result must not be cited as a uniform bound for that derivative. A source-side path-length weight or another explicit bound is required before asserting a completed receiver theorem.

## Verification

`uv run --with sympy python research/voevodsky/checkers/check_packet_uniform_relative_bounds.py`

The exact checker verifies vacuum multiplicities through 32, the resulting correction eigenvector, and an independent complex-coefficient new-match bound. The general l1 inequalities and continuous extension are the proofs above, not extrapolations from these fixtures.

## Next concrete gates

1. Put the source derivatives in an explicit path-length-weighted domain and prove their continuity into the l1 shape carrier.
2. Prove weighted theta truncation estimates for the fixed forcing.
3. Establish completed source separation; finite injectivity alone is insufficient.

The relative pairing and normalization now have uniform bounds in a stated, compatible topology. No terminal-invariant metric or positivity claim has been added.
