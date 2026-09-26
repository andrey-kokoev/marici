# Fail-closed admission without semantic execution

`admission.py` now validates explicit signature/arity, immutable finite package and rule payloads, port reciprocity and entry direction, allocator freshness, pure pending regions, premise package/layer compatibility, and absence of aliases/cycles/unreachable agents. It propagates only package/layer pairs; it neither constructs a flattened history nor calls the reference oracle. Explicit ValueError guards remain effective under python -O.

`Net.validate` delegates to this checker. Public rewrite validates the pre-state and requested active pair, copies the two mutable stores into a private candidate, rewrites and validates the candidate, then publishes the stores and allocator together by assignment. No published net state changes when preflight or candidate processing raises. This is an in-memory single-threaded transaction pattern, not persistence or concurrency/CAS. Private helpers and direct mutation of public dictionaries remain outside the trusted entry-point contract.

Eleven rejection/fault cases verify unchanged agents, wires and next_id, including a deliberately injected exception AFTER a candidate successfully rewrites. Both normal Python and python -O runs pass. Disabling reference.flatten with a throwing sentinel does not prevent net execution/readback. Thus admission is not an opaque invocation of the reference evaluator.

The prior semantic observer in tree_audit.py remains useful for simulation checks and still calls reference flatten as an OUTSIDE oracle. The earlier topology-only limitation in tree-soundness.md is historical: typed admission is now integrated, while semantic observation remains separate.

Fresh regressions: check_admission.py, python -O check_admission.py, check_local_net.py and check_tree_soundness.py all pass. Results are in results/admission.json, admission-optimized.json, local-net.json and tree-soundness.json.

Important cost boundary: whole-net validation and dictionary copying are instrumentation/safety overhead, not bounded-local work. Only the rewrite kernel has a constant-size active-pair interface. No speed or overall complexity advantage over legacy nets is claimed. Next translate an actual legacy fixture and count what is simplified versus merely moved into rule data; keep the formal semantic crosswalk branch open.
