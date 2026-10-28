# Correction: the outgoing E reader and retained complement pass

Node: `T-seam-based-port-readout-binding`.

The previous test's full36-coordinate field construction remains valid. Its named-reader blocker was misdirected: it tested unchanged N slots against the outgoing reference, rather than selecting E's ordered window. The operator correctly identified the intended window as M1,C1,C2.

## Source-bound selector

The fresh checker imports the live `windowProtocol` and `activePhaseSlots` from the owning JavaScript modules. They give E's ordered window M1,C1,C2 with context M2. Native E uses slots3,2,4 in the incoming reference C0,M0,C1,M1,C2.

In the outgoing reference M0,C1,M1,C2,M2, the same ordered window uses slots2,1,3. The complementary slots0,4 carry M0,M2. Order matters: C1,M1,C2 is not the declared E order.

This is a reference-aware selector, not a replacement of the native E slot rule. Reusing either N's slots or the incoming E indices in the outgoing reference fails the controls.

## Exact full-field equations

Keep the previously constructed U, unchanged five-column neutron seed B, metric-adjoint readout R and Q. They satisfy UB=BQ and RU=QR.

Let S_E select outgoing slots2,1,3 and S_C select slots0,4. Exact matrix checks give

    (S_E R) U = S_E Q R,
    (S_C R) U = S_C Q R.

Both hold on all36 field coordinates. Stacking S_E and S_C is an invertible five-coordinate permutation, so all five transported coefficients are recovered exactly. Either discarded complementary direction is invisible to the active triple and destroys full recovery.

The E triple reads source slots2,3,1 after Q, in that order. The output packet retains its explicit window labels and the M0,M2 complement; there is no fabricated sixth coefficient or silent M2-to-C0 rename.

A separate floating-point regression invokes the existing `spectralReadout('electron', ...)` API with the ordered triple placed in its native active slots. Its reconstruction passes tolerance1e-12. This scratch-array arithmetic test is not a native packet/geometry admission or an exact algebra certificate; the selector equations above use exact rational/multiradical arithmetic.

## Disposition

**The ordered outgoing E readout and full complementary recovery pass.** The earlier unchanged-N-selector mismatch is not a blocker for that claim.

Still separate:

- independent source selection of the prior window-to-sector seed/Q ansatz;
- identification with the native8-coordinate E field and joint44 NE exchange;
- complete occurrence/geometry witnesses, native transition admission and global coherence.

An E-labelled observation on the retained36-coordinate field does not alone establish those interfaces. The current result therefore corrects the failed test target without promoting the entire parent conjecture.

## Reproduction and evidence

    python research/voevodsky/checkers/check_ramsey_outgoing_E_readout.py

Fresh execution passes. Receipt: `results/ramsey-outgoing-E-readout-v1.json`. It pins the prior test's sources, the live reader source files and the new checker; prior owner scientific suites were not rerun. The original receipt is preserved as historical evidence and explicitly superseded for its named-reader interpretation.

No owner rules, native admission policy or conjecture-net outcome were changed.
