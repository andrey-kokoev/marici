# Reconstruction-aware retained transport

## What is synthesized

The conditional reconstruction theorem is now attached to the actual retained-family numerical transport. The package contains:

- 137 leaf labels, their parent endpoints and three P/Q/C complex values;
- the exact metric, named operators, actual coframe coefficients and source hashes;
- the directed reference mark, independently of any numerical direct reference d;
- a reconstruction-domain certificate and bounded reference-probe conditioning diagnostic;
- explicit operator-valued fallback records where required by the retention policy;
- complete family membership, inherited masses, presentation and route history.

This is not a new physical instrument or a new DG multiplication realization.

## Carrier and placement boundary

The starting point is the existing field-slot preparation (`field_refibration.encode`), which supplies 137 **paired field-occurrence leaves**. These are lifted into the source carrier of the numerical transport diagram. The numerical diagram then uses its existing 12/11/10 and 6/5/4 presentation positions and its two retained-family promotions.

Those numerical presentation positions are not silently identified with native field grades or with the separate six-node field-refibration diagram. The explicit preparation-to-numerical-carrier adapter is the bridge. No matching of rung numbers is being used as a proof of carrier identity.

## The commuting readout square

There are two independently constructed routes:

1. Evaluate each paired field leaf, then call the owner's existing `incoming_promotion` twice.
2. Retain and group the actual paired field occurrences twice, then evaluate the leaves inside each family and form its mass-weighted mean.

The complete resulting numerical trees agree: values, labels, endpoints, masses and recursively retained members. This is checked for both declared policies, `inherited` and `common`.

**Fields are not averaged before the readout.** The comparisons are quadratic, so a pairing of averaged fields is not generally the average of their pairings. The field-side lift retains every occurrence; evaluation distributes through that retained family structure, not through an invented linearity of quadratic observation.

The owner's source/target indexing maps produce both commuting presentation squares. The two complete routes to rung 4 give equal semantic packages but retain different, validated construction histories.

## Reconstruction certificates and their limited conditioning claim

The existing exact decoder checks the selected-arrow span and the reference probe ranks. Full measurement regeneration remains part of validation.

For reconstructible data, let A_ref be the four-row complex linear map of the missing reference triple into the two P and two Q state equations. Normalize the input with the supplied K3 metric and the outputs with a declared Euclidean norm on those four equations. If the decoder provides representative y and scale rho, use

```
N = A_ref(y)* A_ref(y) / rho,
H = K3^{-1} N.
```

H has the same positive eigenvalues as the Hermitian whitened reference Gram. With eigenvalues lambda_1 <= lambda_2 <= lambda_3, the following certified bounds require no floating-point eigensolver:

```
lower = det(H) / trace(H)^2 <= lambda_1,
upper = min_j N[j,j] / K3[j,j] >= lambda_1.
```

The lower bound follows from lambda_2 lambda_3 <= trace(H)^2; each upper bound is a metric Rayleigh quotient. Algebraic signs are certified by rational interval isolation in the chosen source embedding.

The fixture policy freezes a squared-margin threshold of 1/1000 before auditing packets. This is a diagnostic choice, not a physical scale or a fitted normalization.

The dispositions are:

- **reconstructible:** the reference margin is certified above that threshold;
- **reconstructible with weak reference probes:** the upper bound is below threshold;
- **reconstructible, margin unresolved:** the bounds straddle threshold;
- **requires retained operator data:** the generic reconstruction domain fails.

The unresolved category is necessary: a sufficient lower bound below threshold is not evidence that the true margin is small.

These are bounds for the **reference recovery equations only**. They do not certify stability of the whole nonlinear decoder, its anchor selection or the intertwiner solve. The name “reconstructible” does not mean “globally well-conditioned.”

## Explicit fallback, not a hidden original field

The conservative policy retains all 144 operator-valued arrow blocks whenever the packet is weak, unresolved or outside the generic domain. The fully certified reference-margin case does not retain this sidecar.

The blocks are `c_e c_f*` in the declared corner coordinates. This is the prior full outer-product construction expressed in that basis, not a claim that corner and spatial co-moving coordinates coincide. The extra 23 reference-touching blocks are explicit; all 144 blocks are kept because selected-span failures can affect more than the reference triple.

The sidecar does **not** contain an amplitude anchor or a hidden copy of the original field. A nonzero diagonal entry chooses a reconstruction chart: its column is y and its value is rho, so y/sqrt(rho) gives the original field up to common phase. All blocks are regenerated to verify rank-one consistency. The zero packet has its own zero-field case. No global phase is supplied by the fallback.

Validation additionally regenerates all P/Q/C comparisons from this representative and scale. An unrelated or truncated fallback cannot be passed off as belonging to the scalar packet. This is consistency checking, not authentication of an externally observed source.

The fallback is extra matrix-valued data outside the 137 scalar-channel labels. It is not a claim that every stratum has been encoded into 137 scalar values.

## What the checker establishes

Five fixtures exercise both retained policies:

1. the spanning reconstruction fixture;
2. incoming reference probes scaled by 10^-6;
3. a blind-reference fixture with selected span still three;
4. the zero field;
5. a reference-only field.

For each fixture, both diagram squares commute, all six node presentations retain the same 137 leaves, and the independent field-family route equals the numerical route. Certificates, context and fallback records survive unchanged. The terminal package is revalidated from its actual leaves and sidecar.

Two non-faithfulness controls are important:

- A permutation of the two non-reference endpoint labels gives distinct valid labelled packets with the same three terminal channel averages. An average is not the retained package.
- The two blind-reference fields from the reconstruction counterexample have identical scalar leaves but distinct operator sidecars. Retention preserves the missing distinction rather than falsely declaring the scalar data sufficient.

Corruption tests reject context drift, stale certificates, missing/truncated/unrelated fallback data, removal of retained members, wrong family mass and invalid route history. The validator recomputes the expected family trees, not just their final means.

## Durable synthesis

The resulting interface transports **data plus reconstruction obligations**, rather than treating all packets as equally observable. It preserves an explicit distinction between:

- retained field information;
- scalar comparison information;
- conditional reconstruction;
- reference-probe conditioning;
- terminal aggregate observation.

Further work may price or implement the fallback, improve conditioning diagnostics for the complete decoder, or seek a physical measurement implementation. The original fixed 2x2 DG identification, physical calibration and supplied reference d remain separate gates.

## Reproduction

```
python research/strominger/checkers/check_reconstruction_aware_tower.py
```

Receipt: `research/strominger/results/reconstruction-aware-tower/verification.json`. The checker replays the reconstruction experiment and its preceding source checks. Production, viewer and original DG multiplication code are unchanged.
