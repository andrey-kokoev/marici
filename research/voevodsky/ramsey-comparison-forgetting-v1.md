# Forgetting the comparison input: fixed versus independent admission

## Fresh-state finding

The live revision20 frontier asks whether a target-port comparison descends through forgetting to one source-role packet. Inspection of the actual generated source-bound module reveals its exact admission predicate:

    Valid a = a = actual.

This fixes the *entire* four-port comparison input, not just its source packet. Consequently the admitted domain has no two distinct underlying roots on which to construct the proposed source-only ambiguity witness.

## Positive result under the actual policy

For any fixed root actual, any forgetful map q and any target observation t, define

    h(source) = t(actual).

For every admitted a with a = actual, `h(q(a)) = t(a)`. The safe Cubical theorem proves this by transporting along the admission equality. The concrete instance uses the actual c0 source view and m0 target view from `RamseySourceBoundComparison`.

Therefore **the proposed non-descent test cannot fail under the current singleton-root admission policy**. This is a limitation of the test, not evidence of source-generated role transport. The factor h has the complete canonical target input supplied globally; it does not compute that input from its source argument.

No native source-only derivation policy has been implemented by this extensional factorization. The preceding native comparison still has its full admitted parent available.

## Exact contrasting theorem

For an independent product S times T with S inhabited, target projection factors through source projection iff there is t0 in T equal to every allowed target t. The module constructs both directions explicitly.

It also proves the necessary fiber condition for arbitrary maps: equal forgotten inputs must yield equal target observations whenever a factor exists. Two Boolean target completions over the same source violate this condition. A hostile constant-factor claim on the unrestricted Boolean product is rejected by the typechecker.

The Boolean product is a declared contrasting admission policy, **not** two purportedly source-admitted physical role packets. No actual distinct role completions are fabricated or claimed by this result.

## Effect on the net

Revision20 remains open and unchanged. Its next-attempt question now has a precise answer at the existing concrete policy: constant factorization exists, but cannot distinguish native transport from a supplied target.

To obtain a meaningful source-only test, first declare the allowed varying comparison inputs and which target data must be determined rather than supplied. An executable next step is to inspect the existing validated marking/port family for distinct completions with one fixed source view, retaining exact geometry and permits. Any resulting obstruction must be scoped to that explicitly varying policy. A separately declared canonical completion convention can eliminate ambiguity, but then needs its own source-admission and law-domain justification.

This does not reopen the already proved total face-fixed PN-domain no-go, nor refute higher-context retained incidence, nor establish local field gluing.

## Verification

- Contract: `contracts/ramsey-comparison-forgetting-attempt.v1.json`.
- Generic proofs: `agda/RamseyComparisonForgetting.agda`.
- Actual canonical instance and hostile: `fixtures/ramsey-comparison-forgetting/`.
- Checker: `checkers/check_ramsey_comparison_forgetting.py`.
- Receipt: `results/ramsey-comparison-forgetting-v1.json`.
- Passing freeze: `scc-freezes/ramsey-comparison-forgetting-v1.29b5d52b349cdef2.json`.

Fresh safe Cubical checks with ignored interfaces pass; all live direct input pins and compiler/formal inventories remain stable. The first freeze failed because the product notation import was missing; that mechanical failure is retained in SCC history and is not a mathematical counterexample. After adding the explicit import, the new freeze passes.

No net verdict, graph admission or Git checkpoint was changed.
