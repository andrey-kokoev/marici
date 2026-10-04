# Infinite witnessed executions

`agda/InfiniteWitnessedExecutions.agda` defines a guarded coinductive `Trace` with a next state, full relation witness, and continuation indexed by that next state. `execute` productively unfolds any supplied total WG forever. This is not a termination or liveness claim: a generator may repeatedly return the same state.

For two compatible specializations, `trace-iso` gives inverse flatten/unflatten maps on arbitrary infinite witnessed traces. The inverse laws are Cubical paths built by guarded copatterns; no truncation or extra axioms are used. `execute-commutes` gives a path between flattening the nested execution and executing the independently defined direct flattened generator. A certified-selection instance checks this equality.

`prefix-execute` connects infinite execution to the existing finite `run`. `prefix-flatten` checks that taking a finite prefix commutes with flattening. Thus the coinductive representation agrees with the previously checked finite histories.

Scope: infinite trace equivalence for the existing relative two-stage specialization. No infinite four-domain pentagon, general composition algebra, fairness, progress, or termination theorem is asserted. The certified-selection fixture is a structural instance, not evidence of infinitely many distinct selection events.

Verification: fresh Agda with `--ignore-interfaces --safe --cubical --guardedness --transliterate`, the research Agda and adapter include paths, and Cubical 0.9 passed. The pre-existing TypedGeneratorLayers import warning remains. Log: `.ai/tmp/infinite-wg-check.log`.
