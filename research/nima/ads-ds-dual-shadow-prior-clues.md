# Prior clues for the precise dual-shadow programme

## Review scope

Read source notes and checker implementations for projective interval geometry, Plucker/Ptolemy coordinates, hyperbolic geodesics, entropy, actual NNMHV boundary transports and the history6 twistor coefficient. No checkers rerun, original files changed or conjecture outcomes promoted.

## 1. The invariant-metric calculation already exists

`projective-interval-metric-selection.md` proves that every smooth nondegenerate symmetric two-tensor invariant under the supplied diagonal local PSL(2,R) action is

    g_C=C du dv/(v-u)^2, C!=0.

Its scalar curvature is 8/C. Modulo positive constant scale there are exactly two classes. The older failure to select a sign/scale is therefore positive evidence for the revised *pair of shadows* question: it does not obstruct admitting both classes. Reuse this proof in DSH-2; the missing comparison is sewing the fixed projections and causal assignments to it, not recomputing a familiar curvature formula.

The original `check_nnmhv_projective_interval_desitter_bridge.py` inserts both the fractional-linear action and metric. Its output phrase 'continuum limit' is stronger than the calculation performed: it checks invariance and curvature, not convergence from the finite history source. The later classification note explicitly restores that boundary.

## 2. Plucker/Ptolemy data are a concrete clue for projective provenance

`check_nnmhv_plucker_poincare_cluster_bridge.py` starts with C_i=(1,x_i) and Delta_ij=x_j-x_i. It proves the four-endpoint Plucker/Ptolemy identity symbolically and tests ordered positive configurations. Ratios of products of these minors give projectively invariant cross-ratios: a stronger structure to track than interval order alone.

But this checker **supplies** the x_i and the rank-two columns; it does not reconstruct them from the source's interval edits. A source-origin test should seek an independently constructed rank-two coefficient/minor packet and show how actual source operations act on it. Merely renaming endpoint differences as minors would repeat the premise.

`research/benincasa/history6-twistor-cross-ratio-2026-10-13.md` is a more source-specific precedent: an actual transported boundary coefficient is derived as

    c6=1-<6812><5123>/(<5812><6123>).

Its symbolic incidence calculation establishes balanced projective weights on a localized domain. This is evidence that actual history transports can furnish projective scalar data, not a proof that this coefficient supplies the real endpoint PSL(2,R) action. Its GL4 twistor domain, denominators and target-dependent extension must be compared explicitly with our interval source.

**A finite-size consequence:** the current m=3 metric-visible chart has only three endpoint positions. Three distinct ordered points carry no nontrivial projective cross-ratio. Distinguishing projective endpoint structure from arbitrary monotone placement needs at least four endpoint positions. An m>=4 abstract source test is therefore a different scope from the existing three-round ten-mode optical comparison; no extra cavity round is silently available.

## 3. Actual boundary transports are not all group elements

`check_nnmhv_projective_transport_correspondences.py` constructs 2-by-2 transport matrices from actual NNMHV prefixes and boundary replacements. In its declared n=7 fixture it finds both rank-two automorphisms and rank-one collapse correspondences; the latter have zero determinant and no inverse.

This is a direct warning against promoting 'projective transport' to a universal PSL action. The shared chart symmetry and the dynamical/source transports are different types. A proposed native bridge must either retain the rank-stratified correspondence category, restrict to a justified nonsingular domain, or specify a lift retaining the lost data. It may not delete the rank-one histories by terminology. The fixture is not an all-history classification theorem.

## 4. A prior geometric shadow correspondence is already explicit

`check_nnmhv_hyperbolic_geodesic_rt_bridge.py` sends an endpoint pair (u,v) to a semicircle in the upper half-plane H^2 with center (u+v)/2 and radius (v-u)/2. The space of these geodesics has the dS2-type interval metric. This is a useful incidence-correspondence model: one geometric object and its space of subobjects need not have the same metric or dimension.

It is **not** the AdS2/dS2 pair of DSH-0. H^2 is Riemannian and can be interpreted as an AdS3 time slice only with additional spacetime structure. The checker supplies that geometry and the entropy/regulated-length formulas; it does not establish an AdS3 reconstruction or holographic duality. Keep this as an alternative correspondence route, not a proof imported into the current two-dimensional target.

## 5. Entropy is an additional premise, not a free normalization

`check_nnmhv_entanglement_crofton_bridge.py` supplies S=(c/3)log((v-u)/epsilon), differentiates it, and multiplies the Hessian by 12/c. It produces the positive metric class, but neither this entropy law nor its metric conversion factor follows there from the interval grammar. For the revised target this is one possible decorated realization, not a requirement to exclude the negative class.

## Consequence for the next work

The existing `dual-shadow-transport-audit` remains a meaningful conditional sewing test. It should explicitly distinguish projective chart relabelling, retained interval edits and potentially singular NNMHV coefficient transports. Its success would not derive the native projective premise.

For that stronger premise, the best concrete clue found is the source-derived twistor coefficient/minor route, with a four-endpoint comparison and rank/localization guards. This is a proposed follow-up, not a newly admitted ready task or a closed derivation. The search found no source establishing that bridge to our real endpoint action.
