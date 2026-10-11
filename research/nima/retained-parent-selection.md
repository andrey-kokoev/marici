# Native parent retention does not itself select the next physical state

## Question

Does the retained first hydrogen composite impose a source-derived restriction on the second electron attachment? Distinguish recovering the original parent record from requiring an orbital in the present state to remain unchanged. Active obligation: native source retention and target-selection audit.

## Actual native constructor

`IndexedConstructorTables.Core.Result` sends `retain-header A x B` to B. `NativeTableRules.Native.remember a b` stores a in the expression while preserving b as the active value. Thus the earlier composite is retained in the typed syntax, not imposed as an invariant of the target's active physical state.

`agda/RetainedParentSelectionAudit.agda` states this using the actual native definitions. For any fixed parent, target type B, code for B and supplied x:B, the active value of the retained package is definitionally x. The parent header is unchanged for every x, and every supplied target value is in the image of that active-value map. Retention therefore introduces no additional value filter.

This is a packaging theorem, not a theorem that arbitrary targets are reachable from one native seed. Rule admissibility and required premises remain separate. The result identifies what retention alone does not supply without bypassing the existing reachability gates.

## Physical discriminator

Keep the identical hydrogen parent record, exponent 1 and energy -1/2, for three supplied exchange-symmetric Coulomb trial targets. Positive attachment binding means energy below the hydrogen-plus-free-electron threshold. The negative value in the first row is only a trial-state excess, not proof that the physical ion is unbound.

| Target restriction | Energy, model atomic units | Signed attachment binding, eV |
|---|---:|---:|
| Equal orbital exponents | -0.47265625 | -0.7436625 |
| Compact exponent frozen at parent value 1 | -0.5125894323 | 0.3423922732 |
| Both orbital roles allowed to relax | -0.5133027718 | 0.3617928244 |

The prior hydrogen energy calibration and fixed-proton Hamiltonian are unchanged. All targets recover the same parent; all obey spatial exchange symmetry. The frozen-compact trial is minimized over the same declared rational outer-exponent grid. The relaxed trial uses the previously selected values, not a new fit. Recovering the parent succeeds even though the final compact exponent differs from its stored value.

## Disposition

There is no additional orbital-freezing constraint supplied by the inspected retention constructor. Nested records may constrain later computation when a specific generating rule consumes their contents, but the nesting itself does not choose that rule. The distinct target energies provide a concrete discriminator for any future proposed rule; they do not authorize choosing one after looking at the desired mass.

The current native packaging and supplied Coulomb benchmarks therefore establish faithful retention, not an extra physical prediction. The first missing object remains an actual second-attachment generation/admission law depending on the retained composite. This branch should not be extended by inventing more retention constraints without such a source law.

Verification: exact executable test `python research/nima/checkers/check_retained_parent_selection.py` passed via `structured_command_execution:e_32876_1791226495617775400_39`; result: `results/retained-parent-selection.json`. Fresh safe Cubical Agda verification passed via `structured_command_execution:e_32876_1791226463245036000_38`; receipt: `results/agda-RetainedParentSelectionAudit.json`. No commit or publication is claimed.
