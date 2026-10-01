# Nine rounds of spectral identity re-entry

## Run definition

One round reopens the preceding identity's history window, recovers its three primitive triangle packets, reconstructs both folds and the nested return, and promotes the selected spectral mode again. The first round starts from the original nested root. The same procedure is tested separately for the common, positive-phase and negative-phase modes.

This is the operation currently implemented in `record4-spectral-promotion.md`. The return operator remains the cyclic successor on the same three packet slots. A new next-level composition rule is not introduced by calling the operation repeatedly.

The depth-three packet tree is reused through its window. Each round receives a fresh identity label and an execution receipt naming its input and output identities. The nine chronological receipts are retained separately from the packet ancestry; no parent tree is relabelled as depth zero or silently truncated.

## Results

All nine rounds pass for all three modes:

| Quantity | Result |
|---|---:|
| Rounds per mode | 9 |
| Modes | 3 |
| Fresh identity records | 27 |
| Original primitive arrow occurrences | 3 |
| Retained nested roots | 1 |
| Maximum packet ancestry depth | 3 |
| Rank of each promoted projector | 1 |

The projector in each mode is identical across all rounds, satisfies E²=E, and retains its eigenvalue. Each output window reconstructs the exact original entry, continuation and primitive occurrence IDs. Fresh labels distinguish separate promotion occurrences. Distinct modes remain orthogonal.

Thus the implemented promotion reaches a stable mode identity. Repeating this operation adds execution provenance while preserving that identity and its source data. It does not generate an expanding family of new triangle operands.

## Separate phase-power diagnostic

For comparison, the checker also evaluates C^n and S^n on each selected eigenvector, where C is the packet cycle and S its existing short half-phase root. These calculations track powers of the existing operators. Promotion itself does not execute either rotation.

For the positive complex mode, with omega=exp(2*pi*i/3) and h=exp(pi*i/3):

| Round index n | C^n phase, omega^n | S^n phase, h^n |
|---:|---|---|
| 3 | +1 | -1 |
| 6 | +1 | +1 |
| 9 | +1 | -1 |

The negative mode has conjugate phases; the common mode has phase +1 throughout. Both propagated vectors remain in their original eigenline and retain their norm, so their identity projectors remain unchanged. The cycle-power period is three and the half-phase-power period is six.

These are phase diagnostics alongside nine promotion rounds, not a new physical-time law or a change in the history depth policy.

## Verification

    python research/nima/checkers/check_spectral_promotion_nine_cycles.py

Exact rational and Q(i*sqrt(3)) checks cover all 27 promotions, ordered input/output receipts, full window recovery, both folds, idempotence, Hermitian rank one, mode orthogonality, fresh labels, fixed packet depth, and phase-power/norm identities.

Artifact: `results/spectral-promotion-nine-cycles.json`.
