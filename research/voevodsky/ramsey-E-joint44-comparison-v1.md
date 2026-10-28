# Outgoing E readout versus the saved joint44 NE binding

Node: `T-seam-based-port-readout-binding`.

## Result

The two constructions have exactly the same rank2 E / rank3 retained-baryon Gram split and both recover all five coefficients. They are **not identical in the unchanged saved frames**.

The E difference is precisely one power of the already retained native order-three electron action, not an arbitrary fitted unitary. In the provisional full-five output comparison, the baryon difference swaps the two context columns while preserving the common active combination.

## Common comparison convention

Write y=Qx for the outgoing reference coordinates M0,C1,M1,C2,M2. The new field lift gives U B x=B y, where B is the unchanged saved N five-column embedding.

With zero E input, applying the existing NE exchange to B y yields

    actualE = S B,
    actualN = (I-C_N) B.

These reproduce the saved postNEJointEmbedding after its actual native coefficient permutation. The comparison checks this identity before examining the new readout.

For the requested outgoing E order M1,C1,C2, select slots2,1,3. Form its two real contrast coordinates with the same contrast basis as the source. Use the saved electron frame AND saved NE contrast-reflection convention to produce targetE. No electron frame is fitted.

The saved native output places E's active marks at slots3,2,4. Matching those three marks and M0 gives the provisional output-index map

    H=[4,0,1,2,3].

Its remaining slot0 would carry outgoing M2 where the native incoming-reference label is C0. This is explicitly retained as unmatched provenance, not a physical occurrence equality. The E block is independent of that slot; the full baryon comparison is conditional on this numerical bookkeeping.

## Exact checks

- The E Gram projectors agree between actualE and targetE as full5-by5 matrices, not only in trace.
- Both E projectors have rank2.
- The baryon Gram projectors agree, have rank3, and complement E to I5.
- Both complete44-by5 preparations are isometric and recover all five coefficients.
- Nevertheless actualE differs from targetE in24 matrix entries; the provisional baryon blocks also differ in24 entries.

The required E-frame change in the retained contrast basis is

    [-1/2, -sqrt(3)/2]
    [ sqrt(3)/2, -1/2].

This is exactly the source's C3 rotation. Reconstructing the raw electron return frame J and using the saved native dictionary action V verifies

    (J V J*) actualE = targetE.

Thus the electron comparison closes after a known native return-image action. It is not equality under the unchanged NE exchange, nor does the projector-supported J V J* by itself claim invertibility on all8 raw E coordinates.

For the retained baryon block,

    actualN * permutation([4,1,2,3,0]) = targetN.

Only the two context columns move; the three active columns agree. The complete numerical frame difference before exchange is

    A = Pi_NE H = permutation([4,3,1,2,0]),
    [actualN;actualE] A = [targetN;targetE].

A is nonidentity. Its existence records exactly what must be accounted for, not permission to insert a new native transition silently.

## Controls and remaining gate

Exact comparisons reject identity-frame matching despite equal Gram projectors, and reject dropping the saved NE contrast-reflection convention. The previous wrong-N-selector failure is not reused.

The next source question is whether the retained native C3 action and context-frame change belong to the intended labelled outgoing chart transition, including C0/M2 provenance. Rank agreement and an available native action do not alone establish that composition's admission.

No field seed, prior operator, native source or receipt was modified. No conjecture-net outcome or graph admission was changed.

## Reproduction

    python research/voevodsky/checkers/check_ramsey_E_joint44_comparison.py

Fresh exact execution passes. Receipt: `results/ramsey-E-joint44-comparison-v1.json`, containing all residuals, the precise frame change and source hashes. Imported direct source pins were verified; prior owner scientific suites were not rerun.
