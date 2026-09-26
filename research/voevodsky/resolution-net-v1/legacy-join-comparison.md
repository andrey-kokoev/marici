# First legacy comparison: a bounded positive result, not yet a smaller executor

Audited the existing four_cell_completion_barrier_net.py and its GATE dependency. The chosen fixture isolates the actual legacy binary-join suffix after all four READY tokens already exist. It executes the real BarrierNet JOIN/HOLD code, not a reimplementation. Legacy files remain unchanged.

The v1 adapter maps each READY admission to a complete package/witness seed and each join to an explicit binary rule witness. Domain output formation (ordered token union, with duplicate ownership rejection) is visible in the adapter. There is no hidden legacy evaluator callback. The flattening net normalizes the resulting layered derivation.

Fresh exhaustive result:

* Legacy suffix:10 schedules,6 rewrites each; final boundary is READY at BARRIER.
* Resolution prototype:80 schedules,7 rewrites each; readback is the same full ordered witnessed derivation in every case.
* Duplicate-input ownership and all four missing-admission cases are rejected by the fixture adapter.

Primitive comparison: the legacy suffix has READY, JOIN, HOLD, BARRIER (four kinds). The generic prototype supports five fixed-arity signatures and three structural rewrite schemas; this fixture uses four signatures (not unary step). Domain joins become one rule-data schema with three witnesses. Thus there is NO demonstrated total primitive-count or step-count reduction on this small suffix. The potential gain is reuse of a uniform calculus across domains, not a claim that this example is faster or smaller.

Semantic boundary: reference resolution represents already witnessed steps. This fixture supplies all four completed admissions before compilation. It does not preserve online intermediate READY/GATE timing, implement the upstream cleanup protocol, or prove a bisimulation. The history contains more provenance than the legacy final token, but that does not automatically replace the legacy runtime ownership checks. Calling this a full legacy-net translation would be misleading.

Result: results/legacy-join-fixture.json. Reproduce with python research/voevodsky/resolution-net-v1/check_legacy_join_fixture.py.

Next investigate whether a pending resolution can accept seed evidence incrementally without adding domain-specific waiting machinery. That is the decisive missing operational feature exposed here. Specify an explicit boundary for unavailable evidence, avoid manufacturing Rule witnesses for future computations, and test release gating/ownership against the legacy prefix. Keep this extension separate from the admitted closed-tree calculus and its soundness argument.
