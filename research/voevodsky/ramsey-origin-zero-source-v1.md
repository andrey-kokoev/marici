# The exact canonical complementary seed is not generated at origin zero

## Declared operational signature

Fresh source inspection distinguishes host seed configuration (`completeP`/constructor bindings) from the emitted local operations. In `GenerativeAssemblyRules`, reader-phase and NN-phase steps increment the natural-number origin by one. PN, inverse-PN and NE have zero increment and validate equality of all five named references.

The target here is exactly the complementary origin-zero proton seed used by chart7, including its named references and full coefficient permutation. It is not an unspecified higher-origin context with similar geometry.

## Generic kernel invariant

Safe Cubical proves: for any finite walk whose steps either preserve origin and references or increase origin by one, a walk ending at origin zero preserves its reference value from start to finish. Positive-increment steps cannot occur in such a walk because origins are natural numbers and no step decreases them.

The formal example separates two origin-zero states by a fixed Boolean reference observation. A purported zero-increment reference-changing step is rejected.

## Actual source closure

The checker freshly executes the owning local rules from the default seed and exhausts the entire zero-increment closure with no depth cutoff. It contains exactly3 packet states and3 zero-increment operations: the proton/neutron return and terminal electron continuation. Three positive-increment outgoing operations are excluded by the origin invariant, not by an arbitrary search depth.

Every reachable zero-increment state retains the starting five-reference packet. The complementary target has different named references and is absent. It is nevertheless valid when supplied as a separately configured seed, and its profile is bound to the checked chart7 base record.

Hostile mutations of a zero-step target's origin or named references are rejected by the actual transfer validator.

## Exact conclusion and boundary

Under this declared local operational signature, the exact canonical complementary origin-zero input is not generated from the default canonical seed by a finite operational walk. This is stronger than bounded-search failure: the generic origin invariant reduces the question to an exhausted zero-increment subgraph.

The kernel theorem is generic. Its binding to the JavaScript operation signature is source/runtime evidence, not a machine-verified semantics of JavaScript. Raw higher native package equality is a different interface and is not substituted for this operational walk relation.

No result is claimed about complementary contexts at higher origins, extra operations, altered observation quotients or the broader face-chart descent conjecture. The independently admitted retained-correspondence theorem remains valid.

## Next step

The remaining operational alternative is a higher-origin complementary context with an explicit provenance-preserving comparison to the intended input. Before attempting unbounded search, test a candidate role/reference invariant of the full local signature, or declare exactly what higher-origin target data can vary. Do not silently reset origin or erase the reference history to turn a later context into the canonical seed.

## Verification

- Contract: `contracts/ramsey-origin-zero-source-attempt.v1.json`.
- Generic theorem: `agda/RamseyOriginZeroPaths.agda`.
- Operational checker: `checkers/check_ramsey_origin_zero_source.mjs`.
- Combined checker: `checkers/check_ramsey_origin_zero_source.py`.
- Receipts: `results/ramsey-origin-zero-source-runtime-v1.json`, `results/ramsey-origin-zero-source-v1.json`.
- Passing freeze: `scc-freezes/ramsey-origin-zero-source-v1.730603a646ae1329.json`.

The frozen challenge passes fresh safe Cubical checks and actual operational validation/closure tests. Owning source files are pinned and unchanged. Net revision23, previous scientific verdicts and graph admission remain unchanged; no Git checkpoint occurred.
