# Assurance and reproduction index

Current supported language: member/add/union-literal/ifadd/scan with finite unary operands. Client facade: `checkers/program_runtime.py`; conservative admission: `program_preflight.py`; bounded semantic trace intake: `bounded_replay.py`.

## Review order

1. `mixed-recurrent-program-theorem.md`: semantic/termination statement and premises.
2. `reachable-concurrency-confluence.md`, `schedule-observation-contract.md`: root-fixed final agreement versus schedule-dependent publication.
3. `recurrent-program-review-packet.md`: claim-to-source/check map and minimal kernel.
4. `replay-assurance-levels.md`, `declaration-bound-replay-v3.md`, `replay-source-semantics-comparison.md`: recognition, replay, semantic cross-check and absent authentication.
5. `runtime-resource-envelope.md`, `constructor-resource-accounting.md`, `bounded-replay-intake.md`: logical bounds and exclusions.

## Fresh reproduction

```
python research/voevodsky/checkers/check_recurrent_program_closure.py
python research/voevodsky/checkers/evidence_freshness.py
python research/voevodsky/checkers/check_evidence_freshness.py
```

The latest closure passes29 suites, separately reporting categories and subprocess outputs. It now compares all local checker Python source hashes before/after execution, fails its aggregate status on drift, records the replay contract digest, and hashes the generated signature table and example trace used by offline checks. The freshness command fails closed if source inventory/content, either dependency artifact or current replay contract differs. Three isolated source/artifact changes are detected by the freshness test. Run this test after the closure, not inside it: it consumes the completed closure report.

Mutation sensitivity remains separately reproducible via `check_closure_mutations.py` and `check_shared_semantic_mutation.py`. Their reports are not implicitly certified fresh by the closure. Nor are all historical JSON reports: authoritative current suite evidence is the closure's embedded stdout/stderr, with the two explicitly hashed replay dependencies.

## Limits of freshness

Hashes detect content mismatch against a supplied report; they do not authenticate the report or prove the machine executed it. They are not a time-of-check/time-of-use lock. Python version, OS/dependencies, Markdown proof text and external toolchain are not included in the current source hash inventory. A matching report therefore supports reproducibility at a stated local boundary, not independent review or formal certification.

Next review-readiness task is freeze a small portable audit bundle containing the actual replay kernel, manifest/signature contract, declared source trace and explicit file hashes, with a verifier that works from the bundle rather than repository-relative generated results. Test missing/altered files in a separate directory. Keep authenticity unclaimed; this addresses portability and accidental dependency drift, not digital signing or publication authority.
