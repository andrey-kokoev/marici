# The first two completed filtered attachments form a compatible comparison

## Result

In one common path-norm scale, the first and second filtered extensions admit compatible bounded forcing/Clark attachment roofs. The new triple-layer observation detects J_3/J_4, and refinement of the old extension model has a contractible kernel. The new attachment restricts to the adjacent-layer attachment by an actual commuting square of complexes.

This is a coherent TWO-STAGE filtered realization, not merely a third graded injection. It does not identify an inverse limit of all filtration quotients or assert a topological projective resolution for completed ideals.

Inputs:
- `the-first-filtered-extension-is-strictly-exact-and-source-nonsplit.md`
- `the-completed-first-filtered-extension-has-a-nonzero-balanced-attachment.md`
- `../nima/nonminimal-relation-factorizations-descend-through-balanced-seam-complexes.md`

## 1. Common source topology

Use the common marked-path weight (1+n)^3 A^n, with A large enough for the fixed forcing and normalized feature bounds. For stronger current radii use its compatible radius scale. Let J_k be the closure of the algebraic I^k in that same completed path algebra.

Set

    E2=J_1/J_3, E3=J_1/J_4,
    G1=J_1/J_2, G2=J_2/J_3, G3=J_3/J_4,
    F23=J_2/J_4.

Closed nested subspaces give strictly exact sequences

    0 -> G3 -> E3 -> E2 -> 0,
    0 -> G3 -> F23 -> G2 -> 0,
    0 -> F23 -> E3 -> G1 -> 0.

The earlier sequence 0->G2->E2->G1->0 is considered in this same, now cubic, path-norm topology. Radius loss compares it with the earlier quadratic scale; no equality of independently chosen Banach norms is presumed.

## 2. Ordered three-seam derivative

For a path, D3 sums over event positions i<j<k, retaining the three actual seam edges and the four intervening terminal buffers. Expanding a product of three source relations gives

    D3(abc)=D(a) tensor_balanced D(b) tensor_balanced D(c).

All other choices of seam positions leave one relation factor wholly recorded and therefore contribute zero. Similarly D3(I^4)=0. The higher product rule shows source equivariance on I^3: terms differentiating an outer multiplier multiply a lower derivative of I^3, which is zero.

D3 has at most binomial(n,3) terms of norm at most A^n. It therefore extends boundedly from G3 into bottom cycles of the balanced three-seam target J_(R,3). Its injection follows from stabilized finite endpoint corners and the finite balanced-layer theorem.

Use D3:G3[1]->J_(R,3)[-2] for the connecting observation, placing the cycles in degree -1. This is the same attachment shift as in the six-prime construction, not a new degree convention.

## 3. New extension and its adjacent restriction

Define the two-term complexes

    H=[G3 -> E3],
    H_adj=[G3 -> F23],

in degrees -1,0. They are strictly quasi-isomorphic to E2 and G2 respectively. Their degree-minus-one projections represent the connecting maps to G3[1].

There is a chain map H_adj->H which is identity on G3 and the actual inclusion F23->E3 in degree zero. Composing either projection with D3 gives literally the same map to J_(R,3)[-2]. Thus the new full extension observation restricts to the adjacent-layer observation, before any pairing.

For H one can also retain the ordinary component D:E3->T1[-1]. The map with components D in degree zero and D3 in degree -1 is a bounded chain map: D annihilates J_2, and D3 lands in cycles. It is first constructed on forcing records and then transferred by the normalized Clark map.

## 4. Compatibility with the old attachment

The refined model of G1 is

    L=[F23 -> E3].

The old model is

    K=[G2 -> E2].

The two quotient maps form a chain map q:L->K. Its kernel is exactly

    [G3 --identity--> G3],

with its bounded identity contraction. Consequently q is a strict quasi-isomorphism. This is a concrete common refinement of the earlier attachment model, not a chosen splitting of E3.

The old two-seam component on L is D2 on F23, factoring through G2 because D2(J_3)=0. The degree-zero component is D on E3. Their composite agrees exactly with the old attachment map after q. Thus refinement preserves the first attachment class, while H separately records the new extension E3 of E2.

Do NOT put D3 on all of F23 and declare that to be another equivariant bottom component of L: D3 is only asserted to be an equivariant cycle map on J_3/J_4. Keeping the two extension roofs and their actual comparison maps avoids that grade error.

## 5. The new extension is not a split graded replacement

Take three consecutive forgotten diamond relations a,b,c. In the six-event corner I^4=0 and abc is nonzero. If a source-linear section E2->E3 existed, its value on [bc] would have to be [bc]: that four-event corner has I^3=0. But a[bc]=0 in E2, whereas a[bc]=[abc] is nonzero in E3. This contradicts source linearity.

For the analytical connecting observation the same witness has nonzero D3(abc). On the finite six-event restriction, [I^3->I] is a projective model over the hereditary source. A source-equivariant nullhomotopy would require D3(abc)=a H(bc)=0 because the joint target's outer I-action vanishes. Thus the finite derived morphism is nonzero, and the completed roof cannot be zero in the strict localization: finite restriction followed by forgetting topology preserves its quasi-isomorphism comparison.

The argument relies on the finite projective restriction, not a projectivity assertion for the completed model.

## 6. Currents and topology

Each arrow above is built from quotient maps, source inclusions, or ordered derivatives before pairing. On the forcing-resolved domains the earlier separate-current bounds apply to all retained feature slots. Their radius losses can be taken simultaneously for these finitely many maps. The normalized analytical comparison then commutes by continuity.

Relative collision currents compare rich external records with balanced normal forms. They do not supply or modify the source extension maps. The bulk, forcing, vacuum, and root-state channels stay distinct; no restricted relation metric is inverted.

## Verification

`uv run python research/voevodsky/checkers/check_two_stage_filtered_attachment.py`

Passed eight actual triple-cycle identities, sixteen I^4 vanishings, vanishing of the old two-seam derivative on the new layer, and the nonzero six-event witness. The identity-kernel contraction is checked as an elementary complex fixture. Strict completed exactness, the roofs, and nonzero localization arguments are proved above, not inferred from finite spectral samples.

## Boundary

Closed: two stages of the filtered source and their compatible forcing/Clark attachments in one specified topology. Still separate: an unrestricted filtered inverse-limit realization, completed perfect-dual comparison, and equality with an independently specified arithmetic Green operator. No stable inverse or positivity statement has been added.
