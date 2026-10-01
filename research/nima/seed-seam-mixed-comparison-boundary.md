# Actual seed seam versus the existing shared-leg mixed response

## Exact port match

Use the co-constructed reciprocal seam and its existing vertex-simple path families:

    x0=AB, x1=AD DB : A->B
    y0=BA, y1=BC CA : B->A.

Their composites C_ij=y_j after x_i are four parallel A->A paths. Relative to the shared-leg notation, the common intermediate object is the seed's B and the output is the same seed A as the input. This is an endpoint-type match for these four products, not an equivalence of the seed with the entire 137-slot DG fixture.

## What is source-derived at the retained-word level

In the formal rational span of retained directed words,

    Delta = C11-C10-C01+C00
          = (y1-y0)(x1-x0)
          = [AD DB BC CA] - [AD DB BA] - [AB BC CA] + [AB BA].

All four words have matching A->A endpoints and are distinct. Delta is therefore nonzero as a formal chain. The additive completion is a declared diagnostic representation of the words, not an assertion that physical executions subtract.

`check_seed_seam_mixed_boundary.py` reuses the actual seed path extraction and the shared-leg checker's word/chain arithmetic. It verifies factorization, word support and transport to the B-based boundary under seam reversal. No matrices, physical coefficients or equivalence fillers are assigned.

## Crucial control: positive additive resource sees zero

Every primitive arrow occurs with net coefficient zero in Delta. Consequently EVERY readout that sums fixed primitive-edge contributions annihilates it, including arbitrary positive traversal costs. The four path lengths are 4,3,3,2, and 4-3-3+2=0.

Likewise any response of the form forward-leg contribution + return-leg contribution + common offset cancels. A mixed signal therefore requires a reader sensitive to joint composition/order, not merely to the existence of retained histories or positive traversal cost. Retaining the full words makes such distinctions available; it does not physically realize their interrogation.

A full-word indicator detects Delta, but that is only an information-theoretic witness. It is not an authorized physical probe or interaction.

## What the old shared-leg construction adds

`check_shared_leg_dg_realization.py` explicitly ADJOINS degree-one generators h and k with boundaries x1-x0 and y1-y0. Its degree-two product fills the difference between the two comparison routes. Those generators are free witness data in that model. Primitive endpoint incidence alone does not provide them for this seed.

The prior matrix response also supplies leg values and their multiplication. Under a separately justified compositional linear realization rho, the numerical boundary would be

    rho(Delta) = (Y1-Y0)(X1-X0).

This factorization does not imply nonzero response: one difference can vanish, or their product can vanish. A common reference subtracted from all four C_ij cancels from Delta, but no common-reference cancellation supplies the missing leg values or their physical interpretation.

Thus the seed supplies the actual mixed BOUNDARY. The existing machinery supplies a conditional filler and readout pattern. It does not supply a source-admitted seed filler or calibrated numerical response merely by matching this pattern.

## Precise remaining law

To turn this into a response construction, supply an operation interpreting the retained direct/indirect paths, how that operation composes at B, and an independently justified joint reader. If the DG higher-comparison route is intended, additionally supply/admit the actual leg-comparison witnesses rather than asserting that parallel endpoints make them exist.

This is more specific than choosing a global connection or scheduler: test the comparison of AB with AD DB and BA with BC CA on their actual common boundaries. An additive resource rule alone cannot produce the mixed signal. No new such rule is selected here.

## Verification

    python research/nima/checkers/check_seed_seam_mixed_boundary.py

Fresh exact checks pass. The imported existing seed and shared-leg tests also pass. New controls cover the explicit four-word boundary, factorization, all six additive edge-basis readers, separate-leg offsets and seam covariance. No new Agda closure or physical interaction theorem is claimed.
