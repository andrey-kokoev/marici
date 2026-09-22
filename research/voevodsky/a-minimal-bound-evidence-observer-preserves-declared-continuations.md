# A minimal bound evidence observer preserves declared continuations

## Construction and result

Construct a deterministic, partially admitted continuation system from two separately bound evidence families:

- the four primitive branch states P, A, B, AB for the frozen middle threshold;
- the three recorded signed-refinement stages for the frozen midpoint.

The observable state contains the frozen problem binding and its certified status. Continuation admission is itself observable. Branch labels merge A or B through exact primitive intersection. Ladder labels admit stage 2 after stage 1 and stage 3 after stage 2, implementing the recorded sequential schedule. Other labels are rejected with the state unchanged. This is a declared finite wrapper around those artifacts, not a discovered universal evidence-admission mechanism.

Partition refinement computes the coarsest equivalence preserving these outputs and all admitted/rejected continuations. It stabilizes after two rounds with seven classes. Every pair has an exported distinguishing continuation; different problem bindings are already distinguishable by the empty continuation. Thus the minimal deterministic observer for this closed contract has seven states.

The four branch states remain distinct despite three sharing UNRESOLVED. Their future response to A or B differs. The first two ladder stages likewise share UNRESOLVED but differ in admitted next refinements. Their separation depends on the explicitly sequential schedule; an alternative catch-up protocol would require a new admission test.

## Lineage reconciliation

The old branch trial's hash mismatch is preserved. The producer and independent verifier were rerun against current artifacts with their output directory redirected to `results/continuation-quotient/`. This creates a separate current-input contract and report, leaving the original frozen trial untouched.

Both replay passes succeed. The current primitive boxes exactly equal the archived boxes. Consequently the previous conditional verdict-compression counterexample now has a fresh composition replay under current bindings. This does not diagnose the byte-level cause of the earlier hash change or establish analytical truth from hashes; the owning analytical proofs remain the source of bound validity.

The existing midpoint ladder checker also passes fresh replay, including stage order, exact threshold comparison, accepted witness and calibration/code bindings.

## Composition and preservation

The checker verifies the quotient congruence against every label and exports pairwise distinguishing words as a minimality certificate. It checks 11,151 cut-composition instances and verifies branch commutativity and idempotence.

The quotient compresses repeated and reordered histories into retained evidence states. It performs no further merger of the seven distinct declared states. On this finite family, a transition table preserves continuation behavior without carrying every numeric primitive in the running state, provided the validated artifact bindings and closed admission table remain available. Arbitrary future proofs require a richer state or a new quotient construction.

This is a concrete finite interpretation of preserving T: retain exactly the distinctions needed to preserve the declared continuation admissions and their observable effects. The conjecture of a finite quotient is automatic once a finite closed transition system is fixed; the substantive work here binds that system to real replayed artifacts and establishes its minimality. No bound is established for an open-ended refinement language.

## Reproduction

    uv run --with python-flint python research/voevodsky/checkers/construct_evidence_continuation_quotient.py

Main certificate:

`results/continuation-quotient/minimal-evidence-continuation-quotient.json`

The same directory contains the separately frozen current branch contract, construction and independent verification.
