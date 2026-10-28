# Shared overlap selection: covariance and reversal invariance separate

## Positive construction

A shared ordered-pair selector uses the first chart's endpoint policy, then applies that same endpoint bit to both legs of the common edge port. It therefore produces an actual common vertex, unlike independently selecting endpoints in each chart.

Full common-port transport is defined using the existing edge-permit maps, and vertex-common transport uses the existing vertex-permit maps. Kernel naturality holds for arbitrary common-port witnesses. The ordered selector is covariant under the complementary involution.

## Quantified obstruction

A concrete nonempty chart0/chart7 common port lies on edge01, with facet2 and facet3 permits. Its transported common witness is definitionally its reversed pair of ports. The edge itself is fixed but its endpoints exchange.

For any deterministic selector depending on the **full common-port witness**, covariance demands an endpoint flip there, while literal pair-reversal invariance demands the same endpoint. The kernel derives a contradiction. This is stronger than an edge-only selector obstruction and does not depend on a finite search cutoff.

The two requirements are individually satisfiable:

- the ordered shared selector is covariant but not reversal invariant;
- the constant-left selector is reversal invariant but not covariant.

The selected vertices of the ordered selector and its reversed pair are proved different on the actual witness. A hostile reversal-promotion assertion is rejected.

## Scope boundary

The refuted condition is an invariant **single-endpoint** selection with the stated literal reversal law. It is not a new requirement imposed on the parent conjecture. Retaining both endpoint incidences, or explicitly transporting endpoint order, remains available. Neither parent descent nor the independent-input retained correspondence is refuted.

No native operation is added and complementary input admission remains required.

## Next executable construction

Construct the retained two-endpoint restriction family on full common ports. Prove covariance with the endpoint-bit permutation and pair-reversal compatibility separately, then check their interchange law. This should preserve the incidence information without assuming the impossible invariant singleton selection.

## Verification

- `fixtures/ramsey-common-selection/RamseyCommonSelection.agda`
- `checkers/check_ramsey_common_selection.py`
- `results/ramsey-common-selection-v1.json`
- passing freeze `scc-freezes/ramsey-common-selection-v1.a6d4d8a166b00a73.json`

Fresh safe Cubical positive and hostile checks passed with `--ignore-interfaces`. Local net revision25, external admission revision19 and scientific verdicts remain unchanged. This receipt awaits consolidation; no graph event or Git checkpoint occurred.
