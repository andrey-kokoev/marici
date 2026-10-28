# Deeper search: a prior moving-reference adapter, but no native bridge yet

## Main discovery and correction

`research/strominger/T-seam-transition-v1.md` and its executable `check_T_seam_transition.mjs` already construct the specific adapter sought after the last audit:

- Incoming reference: `[C0,M0,C1,M1,C2]`.
- Outgoing reference: `[M0,C1,M1,C2,M2]`.
- Occurrence transformation: `J_r(role,i)=(opposite(role),2r+2-i)`.
- Induced coefficient map between these different references: `Q=[4,3,2,1,0]`.
- Exact identities: `Q NE^-1 Q=PN`, `Q PN^-1 Q=NE`.

Q is one of the four conjugacies independently found in the previous audit. Unlike an arbitrary conjugacy, this prior construction derives its selection from J between two named reference sets. Old C0 is carried to outgoing M2; no sixth independent coefficient or zero-filled missing mode is invented.

The previous failure remains correct **for the unchanged carried-basis convention**. It must not be generalized to absence of a prior coefficient adapter. This overlooked source supplies one as an explicitly chosen chart law.

The prior checker reports264 saved-data cases (24 markings, origins0..10). Its source was inspected here; that suite was not rerun. It checks local phase frames, occurrence identities and symbolic coefficient traces. It does not invoke complete native chart construction, native transfer validation or a native reversal generator.

## Fresh follow-up: numerical binding succeeds in the eight regular cases

New checker: `checkers/check_ramsey_prior_dual_basis.mjs`.

Freshly generated all24 PNE traces using the existing Nima native rules. For the8 regular-E cases, construct the reversed full charts and transform every retained packet permutation by the prior Q. Both reversed PN and NE now pass the actual native validator. Calling outgoing on the separately configured reversed root generates exactly those rebased target packets.

The16 split-E cases remain shape-ineligible. Original electrons remain terminal. This repairs the earlier numerical coefficient mismatch for the8 cases; it does not produce a bridge from the original packet or make the target independently configured root source-reachable.

Receipt: `results/ramsey-prior-dual-basis-v1.json`. This is fresh runtime evidence, not kernel-verified source semantics.

## A remaining typed binding issue the numerical validator cannot decide

The prior Q has its output labelled by the **outgoing** reference. Native packet readout uses the **incoming** reference and fixed species-dependent active slots. Substituting the same five numbers without their basis labels conflates these types:

| Reader | Native active slots | Required marks | Literal outgoing-basis marks at those slots |
|---|---|---|---|
|P|0,1,2|C0,M0,C1|M0,C1,M1|
|N|1,2,3|M0,C1,M1|C1,M1,C2|
|E|3,2,4|M1,C1,C2|C2,C1,M2|

This table is freshly checked against `activePhaseSlots` and `windowProtocol`, not inferred from prose. The outgoing basis does not contain new C0, which is required by the reversed P active window. In the fixed-coordinate frame reversal, that is the old M2 context point.

Native packets contain chart, origin and permutation, but no independent outgoing-basis tag. Passing their numerical transfer validator therefore does not establish the missing labelled-basis/readout interpretation. A source-supported transport between the two reference types could resolve it; a silent numeric cast does not.

This is not a theorem that all coefficient transports are impossible, nor a demand for six independent amplitudes. It is the exact typed map/readout compatibility square still to supply.

## Other relevant sources and why they do not complete admission

1. **`T-transition-law-v1.md`:** chart-dependent frames produce coherent coefficient transport, including an inverse-composite E-to-P map and27 composition triangles. The note explicitly distinguishes that flat comparison model from native E-to-P dynamics. Useful for coherence after binding, not admission by itself.
2. **`T-metric-gluing-v1.md`:** an intrinsic seam and rank-four metric realization retain the distinction between spatial C0 and M2. Its8/16 reflection split agrees with the native shape split. Abstract seam identification is not equality of fixed ambient vertices or the coefficient adapter.
3. **`contraction-coherence-cube-v1.md`:** backward boundary conditions are obtained by transporting the forward rule. This is a useful direction-aware witness design, but the backward rule and occupancy permission are explicit experimental additions, not independently derived forward native events.
4. **`cavity-reference-closure-v1.md`:** actual complete boundary records recover missing reference variables. The note separately tests and distinguishes reference recovery, experimental vacancy permission and original native admission. Its common-root comparison is rejected as a native local reader advance. Recovery cannot supply the missing permission here.
5. **`identity-bearing-port-equations-v1.md`:** a full six-vertex geometric port network has explicit frame transport, retained histories and exact recovery. Its flat geometric connection is explicitly not the native five-coefficient law or primitive operation signature.
6. **`research/nima/boundary-prepared-witness-update-law.md`:** preparation and transport have executable typed composition and inverse laws, but preparation is independent supplied data on a different carrier. It does not choose an M2 amplitude or admit this reversal.
7. **`T-projector-field-v1.md` / `T-channel-incidence-v1.md`:** source projector/image-field comparisons have unresolved preferred intertwiners and rank/multiplicity mismatches. These are not a ready-made reference adapter for the PN packet.

A repository search for the T-seam checker, its named incoming/outgoing reference fields and dual-map receipt fields found the candidate note/checker, not a downstream native packet binding. This is bounded search evidence, not an exhaustive impossibility result.

## Sharper next target

Do not search for an arbitrary five-slot conjugacy again: the prior J-induced Q is available.

Seek an existing **direction-dependent packet/reference and readout interface** that:

1. types Q's outgoing reference without silently changing its marks;
2. relates it to the complete reversed native chart, including new C0/old M2 and old C0/new M2;
3. transports the named active readout and complementary reference together;
4. admits the reversed boundary with retained direction/history rather than injecting an independent root;
5. supports overlap coherence beyond one complete PNE packet.

If no such interface is supplied by the owning source, report that exact binding/admission gap. Do not install the candidate chart law as a native operation merely because its matrices now pass.

No owner rule, seed policy, net verdict or external graph was changed.
