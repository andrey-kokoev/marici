# Passive E/P semantics: a concrete conditional obstruction

## Result

The structural adapter from the preceding test is valid under its independently admitted-input policy. Its semantic strengthening is **not automatic**.

With the unchanged five-mode P coupling, two explicit geometry-induced comparisons fail both preparation preservation and the retained C2/M2 readout test. Nevertheless their full PN readout squares pass.

This establishes a real incompatibility among these fixed choices, not intrinsic mathematical hardness and not a refutation of every passive comparison or the parent theorem.

## What was tested, without fitting a repair

The complete negative-direction E context is the reversed old P packet. Its retained field binding is

    B_E = B_P Q,        Q = reversal of the five coefficients,

on the old P36 carrier, with zero prepared E8 complement. This is checked against the earlier complete-reversal field receipt. Its outgoing coefficient names are M0,C1,M1,C2,M2.

We do NOT replace this retained carrier silently by a forward native E8 field. A test using the canonical dual-carrier identification would require its explicit conjugation and reader transport.

The complementary target P chart has body order BADC relative to the original ABCD. Two explicit isometric field maps G were tested:

1. relabel directed edge coordinates, keeping global xyz components fixed;
2. also transform xyz components by the corresponding co-moving tetrahedral frame.

Both use the existing36-coordinate proton dictionary and exact tetrahedral rotation routine. No phase fitting or seed alteration occurs. The target P origin is2; the existing P reader has square identity on both field and coefficient frames, so two reader steps do not by themselves repair the fixed seed.

The source/target occurrence convention is bound to all24 actual contextual records. The matrix calculation is in their declared common co-moving field model, not a new proof of arbitrary geometric covariance.

## Exact test that is stronger than norm or dimension matching

Let R_P = B_P*, with R_P B_P = I5. For a given G, the only possible coefficient map satisfying

    G B_E = B_P T

is

    T = R_P G B_E.

Therefore the residual

    L = G B_E - B_P T

is a decisive test, not a search over convenient permutations. Both tested maps have L nonzero: no five-by-five coefficient map can make that binding equation hold with those fixed G and B_P.

The checker also verifies exactly

    L* L = I5 - T* T.

Full-field norm preservation is thus compatible with information leaving the chosen target five-preparation.

## A small explicit witness

For the co-moving convention, the induced five-readout matrix has the form

    T = [ 0  0  0  0  1 ]
        [ 0  0  0  1  0 ]
        [ 0  0  1  0  0 ]
        [ 0  0  0  0  0 ]
        [ a  0  0  0  0 ],     a != 0.

The exact radical a is retained in the receipt. This matrix has rank4, established by its exact sparsity and nonzero entries, without a floating-point rank threshold.

Take the unit input at outgoing E slot1, named C1. Its geometric image has full-field squared norm1, but **all five target P readouts are zero**. The information remains in the full36 field, outside the chosen target preparation; it was not destroyed by G.

There is also a failure at the genuinely retained occurrences, independent of a choice about the advancing C1/M1 pair:

- E.C2 is outgoing slot3 and should be target P slot0 at origin2;
- the geometric comparison instead puts its coefficient in target slot1, named M2;
- E.M2 similarly appears in target slot0 rather than slot1.

Thus this is not merely a disputed continuation rule for the two advancing occurrences.

## Why PN compatibility alone did not detect it

The unchanged candidate already satisfies the all-input identity

    R_N S_PN = Pi_PN R_P.

Consequently, for either tested G,

    R_N S_PN G = Pi_PN R_P G

holds on all36 inputs. Both tests pass this exact PN readout square despite failing the desired E/P binding.

It is a transport identity, not a proof that R_P G represents the requested E readout or retains the source preparation. No edge/triple geometric restriction theorem is inferred from this square.

## An explicit ambiguity control

For contrast, prescribe the coefficient maps

    T_plus  x = (x3,x4,x1,x2, x0),
    T_minus x = (x3,x4,x1,x2,-x0).

Both preserve the retained C2/M2 coefficients, carry the other two body coefficients under the declared continuation convention, and preserve the five-coefficient norm. The corresponding prepared-space maps B_P T_plus R_E and B_P T_minus R_E satisfy the PN binding equation by construction.

They are partial isometries on the prepared spaces, **not claimed full36 unitaries**. They are deliberately not substituted for the tested geometric G.

The two choices even give identical active PN-window readouts; the full PN context distinguishes their fifth coefficient. The sign assigned to old outside M0 versus the target's new outside C4 is not forced by norm, the retained pair, or the active PN window. No occurrence identity between those outside references was established.

This demonstrates why freely constructing a compatible comparison would not settle source selection.

## Consequence for the hard-problem question

We now have more than an unspecified missing proof:

- **Structural contextual admission:** passes under the stated policy.
- **Geometry-induced re-reading with the unchanged target preparation:** fails by exact witnesses.
- **An arbitrary prepared-space comparison:** easy to construct, but not uniquely selected or source-justified.

The next decision is whether the intended semantics requires the geometric comparison G, the particular fixed five-preparation B_P, or neither. If both are required, this tested candidate needs revision; more coherence checking cannot remove the residual. If a moving target preparation is permitted, it must be stated and tested against the parent's actual full-reference/PN semantics rather than introduced silently as a repair.

No need for an active E->P operation follows from this result. No universal no-go, parent resolution or intrinsic-hardness theorem is claimed.

## Verification

    python research/voevodsky/checkers/check_ramsey_passive_EP_semantics.py

Fresh exact multiradical execution passes: the checker verifies the stated failures and controls, rather than reporting the candidate binding as successful.

Receipt: `results/ramsey-passive-EP-semantics-v1.json`, including both geometric maps, induced coefficient maps, every nonzero residual, norm deficits, the unit witness and competing prepared comparisons. Input source pins are rechecked.

This is exact computational algebra with source-bound runtime records, not new formal-kernel verification. No owner source, previous scientific receipt, conjecture-net verdict or graph admission was changed.
