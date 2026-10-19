# Restricted grammar executes through native table operations

Target: `parent:formulation-and-quantifiers`, still open.
Source: `research/voevodsky/agda/RestrictedNativeTableExecution.agda`.
Checker: `research/voevodsky/checkers/check_restricted_native_table_execution.py`.
Receipt: `research/voevodsky/results/restricted-native-table-execution-v1.json`.

## New semantic bridge

The earlier Bool flip-word codec preserved syntax but did not execute the restricted grammar's actual operations. This construction instead evaluates the same source Terms using the existing independently implemented native table primitives:

- the sole literal becomes the native Bool atom table with selected false;
- identity uses `Native.identity-comparison`, not an identity action on a bit;
- pair uses `Native.Pi-package` on the two-element family;
- select uses `Native.E-package` with both children and the explicit selected index.

The evaluator `native` contains no old-code decoder. Its return type is the actual native Package, with its declaration, typed children and selected value. Nothing in this construction introduces a physical operation library or changes the original seed/arity policy.

## Checked obligations

`agreement t` proves native evaluation equals `encode-package (eval t)` for EVERY term in the restricted inductive grammar. It is not a finite enumeration result. Its induction uses the original rule-output commuting theorem and an explicit function-extensionality comparison for the Bool-indexed input family. That family comparison is necessary; endpoint values alone do not supply dependent family agreement.

`native-closed t` applies the existing `ForOldSeeds` retained-closure equivalence to the original compiled derivation. `native-history-endpoint` identifies its endpoint with the separately computed native evaluator. Thus actual native computation and transferred proof history are compared, rather than defining native evaluation by decoding or assuming endpoint coincidence.

`original-derivation-recovered` is the inverse law of that existing equivalence instantiated on the actual compiled source. It recovers the complete original endpoint-and-derivation pair up to the adopted type theory's equality. The native history construction uses the existing transfer theorem; no new independently derived native closure equivalence is claimed.

`run-native` retains the source syntax together with the native history and endpoint agreement. `syntax-recovered` recovers it exactly. This does not assert that an endpoint determines its syntax, or that the entire semantic seed closure is identical to the restricted grammar.

## Resource and physical boundaries

The previous syntax-node cost remains available from the retained Term, including both E branches. No operational step-count theorem for Agda evaluation, proof normalization, table allocation or a physical device follows. A resource-sensitive machine implementation still needs its own state, transitions, budget guards and cost theorem.

The three native rules are a real mathematical semantics bridge, unlike raw flip-word encoding. They do not constitute an independently justified physical account P. The physical register still has distinct source candidates and missing preparation/clock/operation comparisons. Neither a full UF interpretation nor unrestricted analytic completion is supplied.

## Verification

Fresh headless safe Cubical compilation with ignored interfaces passes for the new module and imported native rule/closure sources. Two separate negative modules reject (1) changing the native selected index to true in the false-selected example, and (2) replacing the retained compound source syntax with its literal leaf. No holes or postulates were introduced.

This advances a bounded F/K candidate; it does not close the parent formulation gate or select it as the universe of valid mathematics. Next: define a resource-sensitive operational machine for these three operations, or explicitly keep mathematical evaluation and physical process realization as separate candidate obligations. The universal foundation/scope decision remains open rather than being inferred from this fragment's success.
