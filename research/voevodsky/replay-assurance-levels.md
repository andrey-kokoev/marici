# Review-ready audit assurance levels

## Explicit commands

From repository root:

```
python research/voevodsky/checkers/check_recurrent_program_closure.py
python research/voevodsky/checkers/offline_replay.py research/voevodsky/results/replay-example.json
python research/voevodsky/checkers/semantic_replay.py research/voevodsky/results/replay-example.json
python research/voevodsky/checkers/check_shared_semantic_mutation.py
```

The fresh standard closure has28 passing suites. Mutation experiments remain separate and operate on temporary copies. Reports include local source hashes; no cryptographic signer or independent reviewer is asserted.

## What each layer establishes

1. Structural declaration recognition: the supplied initial graph has the declared word, ordered instruction gates, operands and roots, with no extra nodes. This checks a relation, not historical authorship.
2. Legal replay: every certificate matches the local57-template contract, typed signatures and allocator interval; the pure evaluator reconstructs its graph. Complete traces must have exactly the terminal result components. Partial legal traces are accepted as partial.
3. Semantic replay: the new separate command requires complete legal replay and compares its extracted terminal word/typed observations against the direct source interpreter. It returns source_semantics=matched and assurance=executable-cross-check-not-formal-proof. It does not silently change the partial-trace behavior of ordinary replay.
4. Schedule independence: the written reachable-family diamond/termination argument applies to the intended constructor/rule domain. A single accepted trace does not by itself prove this theorem for all schedules or programs. Bounded exhaustive and diamond tests support it.
5. Authenticity: absent. All modes return authenticated=false. Digests bind local contents, not operator intent, historical allocation or a trusted author. A changed but internally consistent source/graph/manifest can still describe another program.

## Sensitivity and remaining assumptions

The shared GS operand-swap experiment passes legal certificate checks but fails the direct-source comparison. This demonstrates separation of layers2 and3. The semantic replay tests also reject partial claims and comparator mismatches and exercise its CLI; the70-step example succeeds. Manifest and source interpreter still have common authorship, normalization is shared, and no proof-assistant certificate or independent external review exists.

These tools are single-threaded finite-input research audits, not hostile-file services. JSON parsing, normalization, expected unary-chain traversal and direct interpretation lack byte/work limits. Production failure-safe mutation and persisted allocator recovery remain excluded.

Next best task is resource-safe replay intake: bound serialized bytes, certificate count and declared unary sizes before expensive graph recognition/interpretation, with explicit caller policy and rejection tests. This closes an operational gap at the new file boundary rather than adding more instruction forms. Do not describe bounded intake as a complete process sandbox; parsed nesting and runtime costs require carefully stated limits.
