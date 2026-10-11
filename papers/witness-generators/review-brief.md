# Independent review record

Review received from the internal reviewer `marici.Buzzard` in proposal `ep_9f867a71-b93e-492b-b93a-ce3e2d332cd5`, read directly on 2026-10-06. The reviewer inspected the goals, baselines, helper and checker and independently reran both positive compilations and all three intended negative controls in the existing checkout.

**Verdict:** mathematically correct for the fixed fixture and pedagogically useful; better suited to library/tutorial documentation than standalone research publication. We adopted that recommendation.

## Corrections applied

- Made state, witness and auxiliary source universes explicit.
- Restricted source-value equality to the fixed records.
- Separated the fresh comparison from historical unit/four-layer coherence checks.
- Bounded preservation to the stated isomorphism fields, without extra semantic naturality.
- Removed Wolfram from the tutorial; retained only a separate-note pointer in README.
- Compressed attribution and moved bookkeeping out of the main explanation.

No mathematical source changed. Clean-checkout reproduction and wider coherence were not part of the independent rerun. The original request follows for context.

## Decision requested

Is `main.md` accurate and useful as an **expository formalization** of selected witnessed steps, displayed refinements and full-step preservation? Recommend publication-oriented revision, library/tutorial documentation only, or rejection of the current exposition. Do not assume that a contribution beyond standard dependent constructions exists.

## Read first

1. `main.md`, especially sections 3–5.
2. `matched-comparison.md` for the fixed obligations, three implementations and accounting boundaries.
3. `claims.md` for evidence freshness and excluded claims.
4. `appendix-wolfram.md` only when assessing the separate appendix; its basic compiler is not an instance of the stronger composer.

## Questions requiring an independent answer

- Does the exposition distinguish the selected outgoing step from an arbitrary composable relation, and selected lifts from general fibrations?
- Does the full-step contract preserve targets, individual witnesses and selected transitions as stated? Are the source-retention and universe qualifications adequate?
- Is the ordinary library baseline fair? Inspect `SigmaReassociation.totalAssoc` for hidden WG-specific assumptions and check that comparison tests were not weakened.
- Does the text accurately separate the fresh two-/three-layer comparison from historically checked units and four-layer coherence?
- After the negative novelty result, is there pedagogical value beyond a short example in the Cubical library? Identify specific material to retain or remove.
- Should the Wolfram appendix remain, or does its separate mechanism distract from the main exposition?

## Reproduction

```text
python research/voevodsky/checkers/check_wg_refinement_comparison.py
```

Override `AGDA` and `CUBICAL_DIR` as necessary. Expect two successful fresh compilations and three intended `false != true` rejections. The checker also requires independent ordinary imports and comparison tests identical except for module/import names. Exact local receipts are under `research/voevodsky/results/wg-refinement-comparison.json`.

Passing the checker is not an independent review of its own adequacy. A reviewer should inspect the driver and goals and state what was actually rerun. A clean-checkout environment is preferable; existing local receipts alone do not constitute that evaluation.

## Response format

Provide an overall disposition, concrete source/section locators for corrections, independently reproduced checks, unverified claims, and the smallest useful final scope. Separate mathematical correctness from exposition quality and publication suitability. No reviewer endorsement, authorship or release authority is implied by a request.
