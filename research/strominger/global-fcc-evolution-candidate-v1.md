# Executable whole-FCC evolution candidate

## Prior research checked first

The implementation follows the earlier [whole-state prior-clues search](global-28-stage-pe-prior-clues.md), rather than demanding unique local operations again.

| Prior result inspected | What is reused or respected |
|---|---|
| [Marked table fibration](../nima/table-fibration.md) | Group a whole labelled table while retaining the selector, row identities and full recovery data. Regrouping alone does not create physical evolution. |
| [Arrow/history windows](../nima/arrow-history-window.md) | Keep the original whole and an ordered presentation ledger; repeated displays do not erase history. |
| [Operational whole return](../nima/operational-whole-return-downstream-paths.md) | Whole-state realizations need not be uniquely selected by local admissibility. The exported analytic certificate is not imported or claimed here. |
| [FCC Gaussian grains](fcc-gaussian-boundary-v1.md) | Reuse the existing cell-additive microscopic kernel, including its finite-boundary convention. The new assembled matrix is checked exactly against the old implementation. |
| [Full graded esd7 realization](../nima/full-esd7-graded-tate-torus-realization.md) | Reuse actual signed incidence and chart rotation. Do not identify a recorded grade wrap with an implemented Fourier/suspension operator. |
| [Full PN and E-return maps](global-PN-and-two-channel-E-v1.md), [reader field transport](reader-field-transport-v1.md) | Existing field maps have unresolved five-slot, complementary-mode and second-E-channel bindings. This candidate does not quietly identify them with a scalar field. |
| [Two-ended sector trace](two-ended-sector-trace-v1.md) | Do not repeat a periodic relabelling and declare P/E exchange. Test a genuinely changing coefficient field against an independent target. |

These notes were read; their external formal/analytic proofs were not freshly recompiled. Only the reused Gaussian constructor and the new numerical/incidence implementation are replayed here.

## One update on the whole retained state

The state contains:

- one complex field on all120 FCC sites;
- all175 unsplit tetrahedral/octahedral cells used by the microscopic action;
- the complete original1807-cell esd7 census and its annotations;
- a central-flag zipper, a chart frame and four views of the **same** field;
- an ordered update ledger and formal chart-wrap grade.

There is one function `GlobalFCCEvolution.step(state)`. Each call updates the entire coefficient field, advances the structural presentation controller and appends history. It does not choose PN versus reader advance at a local packet.

### Dynamical part

Use the prior exact kernel

    K = sum_cells (I_vertices/14 + L_nearest_edges/4).

Only FCC nearest-neighbour edges enter it, not the56 selected subdivision diagonals. Promote this real symmetric Gaussian kernel to a **declared Hamiltonian candidate**, and take the fixed dimensionless Cayley step

    U = (I + i K/2)^(-1) (I - i K/2).

This promotion, the counting inner product and the interval tau=1 are new model assumptions, not consequences of Gaussian gluing. Nothing is fitted to seven,28 or the E target.

Since K is real symmetric, U is unitary algebraically. The code solves the full120-site complex system and checks the update residual and inverse recovery. The kernel is exactly S4-covariant. It also commutes with the actual quarter-chart permutation, so chart transport and dynamical update give the same field whichever is performed first.

### Presentation part

Traverse an actual central flag upward, then its rho-transported return flag downward. A zipper stores the current cell, unvisited children and retained parents. When the parent stack is exhausted, hand off the chart and restart from its transported endpoint.

There is no `tick % 7` condition or seven-entry execution table. A length-four flag produces seven visits by this traversal convention. **The convention itself is an explicit candidate controller**, not a derived physical timing law. One field update per controller action is likewise declared.

At each tick, all1807 labelled rows are grouped by their intersection with the active window. Four chart-offset views share the one whole field and source payload. Every grouping reconstructs every row, including all original annotations. Scalar values on shared faces are restrictions of one vertex field; all incidence-route restrictions agree. The source signed boundary identities remain valid under chart transport.

This implements scalar restriction coherence. It does not prove the native analytical transfer equations attached to the source cells, nor supply the36-component P/N field or channel Fourier action.

## Independent native target

Use the existing [native end-to-end fixture](native-fcc-end-to-end-binding.md), not a new endpoint label. Embed its five complex coefficients at their actual C0,M0,C1,M1,C2 reference vertices, including the external context. Set the other115 initial vertex amplitudes to zero. This scalar embedding and zero completion are declared candidate assumptions.

Construct the target field separately from the native PN,NE endpoint coefficients at the same marked vertices. The initial and target fields have equal norm and differ as full vectors. No phase, grade or stage number is used to label a result E.

## Measured result

The same global update ran for28 steps.

| Test | Result |
|---|---|
| Full-field dynamics | Nontrivial; spreads outside the initial five-site support |
| Maximum relative norm error |3.03e-15|
| Maximum update-equation residual |4.55e-14|
| Structural chart handoffs |7,14,21,28|
| Whole reconstruction |All1807 rows, all four views, all29 recorded states|
| Shared scalar face restrictions |Agree throughout|
| Formal grade after four handoffs |1; not an analytic suspension proof|
| Normalized squared overlap with native E target at28 |0.0084236126|
| Relative full-field error against that target |1.3550989|

**The candidate fails the native E endpoint test under this embedding.** The overlap is small even after ignoring an overall phase. Seven-visit bookkeeping is not counted as success of the proposed P/E law.

The field is not four-periodic or28-periodic merely because its chart returns. This is a genuine dynamical implementation, not another static table cycle. What now needs revision is the declared action/field/readout binding, not an attempt to prove that the local menu has a unique next operation.

## Reproduction and implementation

```sh
python research/strominger/checkers/check_global_fcc_evolution.py
```

- [Reusable state/update implementation](checkers/global_fcc_evolution.py)
- [Checker](checkers/check_global_fcc_evolution.py)
- [Receipt and full29-state field trace](results/global-fcc-evolution.json)

**19 checks passed; candidate endpoint failed.** The receipt separates these outcomes. It includes every site amplitude at each tick, the event ledger, assumptions, target, numerical residuals and source hashes. Hostile tests reject a dropped retained row and an independently corrupted face value. The structural visit profile is checked on all24 central flags.

No native constructor, prior kernel rule or source census was modified. This is one explicit whole-state candidate, not a claimed physical global evolution or28-stage theorem.
