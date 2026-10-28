# Kernel-computed chart requests over the validated port family

Fresh inspection of `RamseyNativePNOverlapSpan.agda` showed that the native selected span, full source/target retention and triple-domain composition already exist. No new comparison or composition constructor was needed.

The new contribution is a decision adapter. A request consists of a source chart, face, source permit and requested target chart. It computes the target permit decision:

- success carries the actual target permit and the existing `selected-proof` native derivation;
- refusal carries a function from a purported target permit to the empty type.

The target remains an independently admitted input. The adapter does not build a target packet from a source packet or erase the requested chart.

## Complete finite instance

The generated module includes all24 charts, all48 full literal port records, and96 permit decisions. Its permits are computed from each chart's actual C/M roles and the three geometric vertices of the requested face. Both permitted and refused branches are kernel checked; the latter use the proved inequality of one and two M vertices.

All1152 requests (48 valid source ports times24 target charts) are individually checked by reflexivity against the computed adapter result:

-576 accepted;
-576 refused.

This is not merely a host count asserted in a receipt. The generated Agda case equations force the decision procedure to reduce correctly in each case. Accepted branches construct the already proved native selected span. A hostile request asserting acceptance where the target permit is absent fails typechecking.

## Retention and composition boundary

The existing selector retains both complete packet records and permits; its middle seam and triple common-domain composition remain the existing theorems. The adapter invokes that constructor rather than creating a lookalike wrapper or seeding comparison results.

This turn does not add a new theorem about arbitrary field restriction, cross-facet geometric locality, or total PN transport. It does not extend the earlier same-face composition to triples outside the common domain.

The request/interface gap is now closed at the declared finite input policy. Further wrappers around this same decision would be redundant. The active parent obligation returns to cross-facet geometric support and semantic restriction cells: they must be checked against the full retained observation dependencies, not inferred from a successful same-face request.

## Verification

- Contract: `contracts/ramsey-requested-port-attempt.v1.json`.
- Adapter: `agda/RamseyRequestedPort.agda`.
- Generated complete instance and hostile: `fixtures/ramsey-requested-port/`.
- Checker: `checkers/check_ramsey_requested_port.py`.
- Receipt: `results/ramsey-requested-port-v1.json`.
- Passing freeze: `scc-freezes/ramsey-requested-port-v1.868f3d3cb3b6a9a6.json`.

The frozen SCC challenge passes fresh safe Cubical checks with ignored interfaces. Direct source pins for the validated input family, compiler digest and formal source inventories remain stable.

The persisted net remains revision20. No parent outcome, external graph event or Git checkpoint changed.
