# Selected source K, version 1

The user explicitly selected the previously optional cycle-defect constructor:

    H_native = L + 2I - T - Tdagger,
    K_pair = H_native tensor I10 + I10 tensor conjugate(H_native),
    K = K_pair direct_sum 0_vacuum.

The selection is frozen in `contracts/retained-reaggregation-source-k.v1.json`.
Both chiralities and both doublet choices are retained. Both doublets use the
displayed-lift transport (not a different ground-state lift for option 1).
There is no extra pi/4 multiplier, orbital operator or sector-mixing term in this
101-state matter version. The record and coupling remain those of the original
frozen comparison. K has zero vacuum energy; the full empty-ready energy is
g=1/2 before the common subtraction and zero after it.

This is an approved constructor convention, not a uniquely source-derived
Hamiltonian, physical calibration, or claim admission.

## Fresh exact check

`checkers/check_selected_source_k.py` freshly reruns the native source audit,
constructs the full 100-state pair K and its 101-state zero extension, and checks:

- self-adjointness and zero vacuum row/column for both chiralities;
- commutation with the carrier projector;
- KJ=epsilon J and KPi=PiK=epsilon Pi for all four native choices;
- the previously derived exact record-occupation separation for this selected K.

Results: `results/selected_source_k.v1.json`. These results are checkpoint evidence,
not a complete umbrella or consumer admission. The historical
`sector-theorem-progress.v1.md` and its result remain immutable checkpoints of the
previously ambiguous input; this selection resolves their first two blockers.

## Lifecycle and remaining proof

The migration preserves all nine pre-selection ledger events and the active
common-resource-accounting nonce `1095ff630f5e410ab6f0a20880bf7d7a`. Seven EU remain
charged and eleven remain available. No new attempt or probability prior is added.
Existing signed-rule receipts are unchanged and do not retroactively prove K.

Future resource accounting, classification, discriminator and final comparison
receipts must pin the selected-K contract, even when not using the umbrella
bundle. Umbrella bundles must also pin it. Changes require a versioned,
history-preserving migration; the harness rejects unpinned/stale choices.

Next: complete joint-energy and retained post-readout accounting, state the
variable-phase contract and typed sector result, and admit reviewed nonce-bound
conclusion receipts. No additional main-node or umbrella outcome has changed.
