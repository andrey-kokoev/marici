# Verification closure mutation sensitivity

Fresh `check_closure_mutations.py` runs four representative defects in separate temporary source copies. Each case first reruns its unchanged baseline checker successfully, compiles the mutation, removes bytecode caches and executes the selected checker with assertions enabled. Production Python hashes match before/after. Temporary result files never overwrite production checker results.

All four mutants were rejected by the intended assertion, with tracebacks retained in `results/closure-mutations.json`:

* Duplicate GS fuel boundary in place of cursor: production-call external/fresh port multiset assertion fails.
* Swap GS fuel and cursor roles (still linear): sequential oracle comparison fails. This distinguishes semantic routing from mere slot conservation.
* Invert published Boolean decoding: typed final observation comparison fails.
* Treat scanner outcome publication as completion: delayed-cleanup prefix observation assertion fails.

The last mutation is an observation-contract defect, not an actual premature DONE rewrite. This test does not claim the same witness detects every early-ACK topology defect. Four detected examples are sensitivity evidence, not a mutation score over a defined exhaustive population. Syntax/import crashes are not counted as detection; each recorded traceback was freshly read and identifies the intended checker assertion.

Next assurance priority: the inherited constructor currently normalizes arbitrary truthy word elements to B1 rather than strictly enforcing the theorem's binary-word input domain in every entrypoint. Inspect and define a uniform public input validation contract before calling these runtimes reusable APIs. Test invalid words, bool-as-index, negative/oversized-shape operands and one-shot iterables; reject before graph allocation where practical. This is a boundary hardening task, not arbitrary imported-graph validation or transactional rewrite recovery.
