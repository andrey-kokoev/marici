# Exact abstract cost and budget guard for native restricted evaluation

Target: `parent:formulation-and-quantifiers`, still open.
Source: `research/voevodsky/agda/RestrictedNativeBudget.agda`.
Checker: `research/voevodsky/checkers/check_restricted_native_budget.py`.
Receipt: `research/voevodsky/results/restricted-native-budget-v1.json`.

## Fixed resource semantics

The resource algebra for this candidate is natural numbers under addition. The model charges one abstract unit for each literal/identity/Pi/E constructor invocation, with the costs of all premise evaluations added. It is a costed big-step evaluation relation, not a micro-step interpreter, wall-clock complexity result or physical calibration.

`Exec t n q` is an inductive judgement whose constructors apply the actual native package operations. A binary constructor requires both executions, even when E selects one branch. The relation stores the premise execution trees, not just their scalar cost. Identity constructs an actual identity-comparison package; it is not a free no-op.

## Kernel-checked results

- `execute t` builds an execution of every restricted term at its syntax-node cost and actual native output.
- `cost-sound` proves EVERY admitted execution of t has exactly `cost t`, by induction on its execution witness.
- `output-sound` proves EVERY admitted execution returns `native t`; this composes with the previously checked evaluator agreement and native-history endpoint theorem.
- `BudgetRun t b` retains spent units, actual native package, execution witness, remaining units and the equation spent+remaining=b.
- `guard-from-run` and `run-from-guard` give both directions between a budgeted execution and a witness that `cost t + remaining = b`. They are not claimed to identify all proof payloads or define an equivalence of their witness types.
- `no-underfunded-selected` proves no budgeted execution of the actual four-node selected example fits budget three, for ANY output, remaining amount or execution witness. This is stronger than rejecting one proposed certificate.
- `retain-funded` and `syntax-budget-recovered` retain the source syntax along with its budget evidence.

The forward/backward guard statements fix operation availability in this resource model. Equal current output cannot grant an execution whose budget equation has no witness. They do not supply external authority, preparation or replenishment events.

## Controls and verification

Fresh headless safe Cubical closure with ignored interfaces passes. A negative module tries to fund the four-node example with three units; another treats identity construction as free by claiming a two-node execution costs one. Both fail with natural-number type mismatches.

The checker records the command and source hashes; it recompiles the imported closure on every run. No holes or postulates were added. This turn does not require numerical sampling for the general cost or insufficiency theorem.

## Boundary and next decision

This completes the abstract constructor-budget obligation for the explicit restricted F/K profile. It does not bound allocation, equality normalization, machine instructions, compiled proof evaluation or physical energy/time. A lower-level scheduler could refine this relation, but is not necessary to state this candidate's abstract resource semantics and is not claimed here.

The parent formulation remains open because the restricted grammar has not been chosen as its full validity scope, and no common physical account or lowest-level criterion has been selected. Further arbitrary refinements of this toy profile would not decide those universal choices. Next substantive task: consolidate the concrete F/K/resource profile and its exclusions into the formulation comparison, then separate the still-missing universal scope decision from the independently executable source/physical comparison obligations. Do not close the parent by relabelling this bounded cost theorem as universal physical realization.
