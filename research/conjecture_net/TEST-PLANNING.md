# Per-conjecture probability and test costs

Machine annotations: [conjecture-test-planning.v10.json](contracts/conjecture-test-planning.v10.json).
Validation: `python research/voevodsky/checkers/check_conjecture_test_planning.py` or `python research/aspect/scc/scc.py check common-foundations-net-v1`.

This sidecar is keyed by the same 41 qualified conjecture IDs as the main mathematical/RH port model. It pins the four source contracts without changing their evidence or historical pin files.

## Current population

- 21 open conjectures: dated **assistant forecasts and effort estimates** supplied, with per-task rationale. These are subjective next-test forecasts, not calibrated truth probabilities.
- 20 resolved scoped results: next-test forecasts **not applicable**; their verdicts remain historical evidence, not probabilities. A future rerun needs a separately scoped planning record.
- [Next-test ranking](../voevodsky/results/conjecture-next-test-ranking-v1.json) uses probability of a decisive result divided by assistant effort. No expected information gain is claimed.

The effort is a budget for one attempt. Blocked-task forecasts are conditional on reviewed prerequisite witnesses being available; they do not estimate the probability or total cost of obtaining those prerequisites. An inconclusive result means neither gate was met within the budget.

The bounded four-child interface and mathematical package/export are constructed. The **`rh:rh-math-assembly` goal is complete at its local scope**. The common-witness comparison definition is also constructed, without physical admission. The selection review now records an explicit marked-axis successor and a rejected symmetric full-heat quotient, not a canonical/physical selection. Global next is **`math:stagewise-mathematical-interface`** (5 effort units, 75% decisive-result forecast); the RH goal selects `successor-form-candidate` (6 effort units, 80%). The general mathematical interface remains open. The workbench also reports a separate global efficiency ranking; small score differences do not dictate which scientific goal to pursue. This efficiency recommendation is distinct from the RH graph's existing strategic form-repair priority `successor-form-candidate`. It excludes downstream importance and does not assume independent outcomes.

The interface is split into dictionary (2 units), operation/composition audit (3), identity/continuation audit (4), analytic-domain/completion audit (5), and assembly (2). The latter four forecasts are conditional on their required constructed inputs; budgets must not be mistaken for total end-to-end cost. Prior v1–v9 planning/cards and old source pins remain historical snapshots. Completed inventory, operation, identity, analytic, stagewise assembly and mathematical package witnesses have recorded verdicts rather than next-test forecasts; remaining forecasts are unchanged.

Every record includes its actual acceptance and falsifier, next action, test scope, protocol status, probability event and outcome domain, conditioning/provenance/uncertainty slots, a scalar assistant-effort cost slot, and decision-value limitations.

## Supplying estimates

First specify the actual next test or review in `test`, including preparation, stopping rule and admissible observations, and set `protocol_status` to `specified`. Forecast outcomes are `accepted`, `rejected`, and `inconclusive` for that scoped test—not the truth of the universal conjecture. No independence between conjectures is assumed.

For `probability.status = estimated`, provide normalized `values` for all three outcomes, `conditioning`, an explicit qualitative `uncertainty` limitation, and `basis` identifying the elicitor or calibration evidence and date. Subjective estimates must be labeled as such; they are not proof outcomes. Leave `values` null if unsupported.

For `test_cost.status = estimated`, give a nonnegative scalar `assistant_effort_units`, with a dated assistant estimate and rationale in `basis`. One effort unit means one focused assistant read/edit/test/review cycle: a relative planning unit, not elapsed time, human work hours or compute usage. Fractional units are allowed. A justified zero is permitted; an unknown cost is not zero. The estimate concerns the next scoped test including setup and review, not total programme completion. Probability and effort estimates can remain unknown independently.

Expected information gain and utility stay null until a separately reviewed hypothesis/observation or utility model exists. Predictive outcome entropy alone is not information gain. `check_conjecture_workbench.py` computes the live dependency-aware triage ranking from current estimates without modifying them. It also shows goal-specific ready frontiers, blockers, source-reuse action cards and hypothetical construction/rejection unlocks in [WORKBENCH.md](WORKBENCH.md). `estimate_conjecture_test_planning.py` records the historical assistant elicitation and then refreshes the workbench; rerunning that elicitation intentionally overwrites later revised estimates. Use the workbench checker for normal refreshes.

The checker validates exact conjecture coverage, source drift, historical-verdict boundaries, normalization, finite nonnegative assistant effort, and provenance. Seven corruption controls and a synthetic positive estimate fixture are included; fixture numbers are never written into the research model.
