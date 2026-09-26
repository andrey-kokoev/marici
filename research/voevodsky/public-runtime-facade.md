# Supported runtime facade

Audit found inherited `start`, `replace`, graph dictionaries and a legacy `run` priority list on the combined prototype. These are not safe compiled-program client operations: start can host-wire new work outside the program contract, replace mutates raw graph state, and legacy run does not cover the combined control signature. No claim is made that these inherited methods were removed from research classes.

Added composition-based `ProgramRuntime(bits,program)` with only `observe()` and `advance(max_steps=1)` as public methods. It never exposes the graph through its supported interface. Advance accepts exact nonnegative integer budgets, performs at most that many first-enabled local rewrites and returns their count. A spent host budget is not program completion. Completion remains the separate observe flag. No enabled rewrite in an incomplete net raises an error rather than silently presenting success. The facade rejects optimized Python because internal invariants still depend on assertions.

Tests cover the public method list, negative/bool/float/None budgets, zero-step identity, detached report mutation, single-step execution equivalence to the raw net, completion idempotence, empty programs and optimized-execution rejection. Constructor validation and facade tests are now included in the headless closure: all13 suites pass fresh.

This is an API discipline, not a Python security boundary: deliberate reflection can access name-mangled internals. It is single-threaded, has no restore/import API and does not promise transactional recovery from internal failures. Large finite programs remain caller resource obligations. The chosen scheduler is deterministic; the written net theorem covers other maximal rewrite schedules, not concurrent host mutation.

Next priority is bounded execution evidence beyond tiny unary operands: derive and measure peak live-agent/allocation growth for scan and the mixed runtime, distinguishing host step budgets from memory/fuel bounds. This addresses the remaining practical risk of a finite but enormous unary input without weakening the local rewrite semantics or claiming a general resource sandbox.
