# Iteration 6: verification gateway, safe reuse and measured costs

## Unified entry point

`merkle_verify.py` dispatches six explicit versioned schemas: polynomial judgments, identity surfaces, unglued witnessed faces, gluing-proof bundles, cone fillers and scoped witness transports. It invokes their existing mathematical verifiers rather than replacing different policies with one boolean. The earlier standalone CRT/Cardano stores are not migrated into this gateway.

`--require-global` requires a surface report with global path independence. `--require-unconditional` requires an unconditional polynomial judgment. Applying an unsupported policy to another artifact type is rejected rather than silently ignored. Verifying an unglued face packet does not imply that gluing exists.

## Trusted-session incremental cache

Polynomial term normal forms and verified proof judgments are cached under implementation fingerprint, exact context hash, record kind and content hash. The cache is bounded and reused only inside a trusted running process. It is not deserialized from disk or accepted as remote proof evidence. Other artifact families currently use uncached verification.

Every call rehashes all supplied polynomial objects and traverses the current dependency closure before any shared cache hit. Missing or mutated premises therefore cannot hide behind a prior successful verification. Changed contexts get distinct cache keys, including changed assumptions even when the proof-node hash itself is unchanged. Implementation changes invalidate the namespace. The cache stores only successfully checked semantic results and returns copies.

This saves mathematical recomputation on unchanged subproofs, not the cost of reading or hashing the current artifact. A warm run is still linear in supplied object-store size. There is no persistent cross-process cache or incremental storage/network protocol yet.

## Input checks

The gateway rejects duplicate JSON keys, nonfinite numbers, floating-point scalars, oversized strings/integers/containers, excessive nesting and excessive dependency height. Polynomial arithmetic now bounds coefficient bit growth in addition to existing degree and monomial limits. Unknown schemas and unsupported policy requests fail closed. Existing verifiers retain exact hash, type, endpoint and witness checks.

These are prototype defensive checks, not a production security audit. Complete fuzzing, total work/memory budgets for every algorithm, authenticated roots and multi-process cache hardening remain open. Direct legacy APIs do not all use the gateway's JSON reader.

## Benchmark

The fixture has 128 independently witnessed leaves combined in a balanced congruence proof DAG: 1,026 supplied objects, 266,483 bytes in the measured ordinary JSON encoding. Five local repetitions include input guarding, integrity hashing, closure checks and mathematical verification.

| Scenario | Median local time | Semantic cache hits | Semantic cache misses |
| --- | ---: | ---: | ---: |
| Cold verification | 16.34 ms | 0 | 1,024 |
| Unchanged warm verification | 5.53 ms | 1 | 0 |
| One edited leaf, both theorem endpoints updated | 6.14 ms | 24 | 26 |

The warm proof-root hit covers the complete previously checked derivation after current-input integrity is rechecked. The edited run reuses unaffected terms/subproofs. Timings are observations on this machine, not portable performance guarantees; no timing ratio is asserted by the tests. The raw samples and semantic counts are in the receipt.

## Tests

All 26 new checks passed. They cover dispatcher families, policy separation, cold/warm/edited verification, current dependency validation on cache hits, corrupted and missing objects, changed assumptions, implementation namespaces, eviction bounds, hostile JSON, coefficient growth and fresh CLI execution.

Fresh runs of the nine preceding suites also passed: CRT edge reassembly (9), CRT Merkle (17), Cardano (24), surface (14), torus (19), polynomial kernel (27), gluing (20), filler (22) and witness transport (21). Together with engineering this is 199 reported checks across ten suites, not 199 independent mathematical theorems.

## Reproduction

```text
python research/voevodsky/checkers/check_merkle_engineering.py
python research/voevodsky/checkers/merkle_verify.py research/voevodsky/results/merkle_engineering_proof.json --require-unconditional
python research/voevodsky/checkers/merkle_verify.py research/voevodsky/results/merkle_identity_surface_store.json --require-global
python research/voevodsky/checkers/merkle_verify.py research/voevodsky/results/merkle_gluing_proof_bundle.json
python research/voevodsky/checkers/merkle_verify.py research/voevodsky/results/merkle_cube_cone_filler.json
python research/voevodsky/checkers/merkle_verify.py research/voevodsky/results/merkle_witness_transport_store.json
```

For reuse across calls, import `VerifiedCache` and pass the same instance as `verify(artifact, cache=cache)`. A fresh CLI invocation starts with an empty cache.

Artifacts:

- `research/voevodsky/checkers/merkle_verify.py`: gateway, strict reader and cache.
- `research/voevodsky/checkers/check_merkle_engineering.py`: tests and benchmark generator.
- `research/voevodsky/results/merkle_engineering.json`: test receipt, raw timings and fingerprints.
- `research/voevodsky/results/merkle_engineering_proof.json`: reproducible benchmark proof.
- `research/voevodsky/results/merkle_gluing_proof_bundle.json`: unified gluing-certificate input.

## Six-iteration disposition

All six requested areas now have bounded executable prototypes: expression/proof input, constrained gluing discovery, exact affine global transport, explicit thin cone fillers, scoped proof substitution and common verification tooling. This does not complete arbitrary mathematical identities, unrestricted surface discovery, dependent higher coherence or production deployment. Ledger 4312 retains those remaining scope limits and follow-up tests.
