# Two conditional branches of the full-lift conjecture

Let `L(f)` mean a source-derived factor-local continuous lift of the native square, and `R(f)` its compatible whole-Tick return interpretation. The parent proof protocol already requires both. Write `P = exists f (L(f) and R(f))`.

The new nodes are:

1. `full-lift-proof-implies-local-core`: `P -> exists f L(f)`.
2. `full-lift-rejection-obstructs-return-extension`: `not P -> forall f (L(f) -> not R(f))`.

`agda/TickLiftOutcomeSplit.agda` checks these as parametric constructive implications. The first projects a witness; the second combines any proposed local lift and return interpretation into a witness contradicting `not P`. Fresh verification is recorded in `results/lift-outcome-split.json`.

Both implication schemas therefore have proof outcome `++`. This is NOT a claim that either assumption or consequent holds. The candidate type and predicates remain parametric: the missing source-derived contract has not been supplied by logical decomposition.

## Wiring

| Parent outcome | Positive consequent | Negative consequent |
|---|---|---|
| `++` | enabled: local core exists | disabled |
| `-+` | disabled | enabled: no local core has a compatible return extension |
| `+-`, `--`, unattempted | disabled | disabled |

The graph uses explicit `conditional_branch_activation` relations rather than unconditional entailment to the child consequents. Activation is computed from the parent outcome and checked for all five states. It never runs backward to choose the parent's outcome.

Currently the parent is `+-`, so **both consequents remain dormant**. The negative branch does not assert existence of a local core; it may hold vacuously. Neither branch distinguishes an analytic defect from an undefined provenance criterion without further scoped work.

The consequent `exists f L(f)` is now also registered independently as `source-derived-local-core-exists`. Its rejection refutes the full lift; its proof enables an extension test for the same witness. The parametric rules are checked in the same Agda module. See `local-core-test.md` for readiness and scope boundaries.

These conditional proof burdens are smaller than constructing or excluding a full lift. Adding them is a logical organization of the net, not progress toward deciding the parent. They are not separate independent observations in the cost/probability model.
