---
author: marici.Nima
kind: mixed-trust-computational-result
description: A bounded Layer 4 view engine clears registered Boolean caches while retaining requests and dependencies, replay-checks data, and restores prior visibility from a saved plan.
---
# 4231 — Registered Active Views Permit Replay-Checked Clearing and Exact Undo

## Claim

For closed Boolean histories built from ordered `stay`/`turn` instructions, the formal model supports four cache-visibility modes (full, output-only, trace-only, compact). Cache values are paired with correctness paths; changing a fixed mode is a Layer 4 certified reduction that preserves the original request, agrees with the Layer 3 evaluator, and inherits the all-dimensional certificate. Explicit stays and source history remain retained.

A standard-library Python CLI implements allowlisted output/trace caching, deterministic byte/replay-budget selection, source-bound planning and application, replay validation of supplied caches, dependency retention, recovery, and exact undo using a saved plan. The audit covers 126 requests across four modes and 17 runtime tests, including hostile plans/JSON and an independent parity oracle. In the fixed demo, active-view bytes fall from 2,019 to 271 while 2,091 dependency bytes remain; total artifact bytes go from 4,242 to 2,494. The undo plan is 1,033 bytes (compact plus plan: 3,527 bytes); recovery replays 258 steps and reproduces the original canonical JSON.

## Scope

This is a closed Boolean replay prototype, not an arbitrary typed-payload engine or a globally optimal compressor. Python/JSON is tested but is not extracted from Agda or proved to refine it. Hashes are integrity/version guards, not authentication or proof terms. Replay counts are not CPU/latency claims, and the saved undo plan can outweigh savings for tiny records.

## Durable verification

Packet: `research/nima/active-view-engine.md`; Agda: `research/nima/agda/ActiveViewMachine.agda`; runtime: `research/nima/checkers/active_view.py`; tests: `research/nima/checkers/test_active_view.py`; audit runner: `research/nima/checkers/check_active_view.py`; formal receipt: `research/nima/results/active-view-machine-formal-audit.json`; runtime audit: `research/nima/results/active-view-audit.json`; SCC model: `research/nima/scc-models/active-view-machine.json`. The proposal reports fresh safe Cubical closure, two intended rejections, 17 runtime tests and a source-bound audit; not rerun for this entry.

Proposal `ep_5e5b6b23-2b1e-4174-b8ab-fbb6b14d6423`, event `ev-000000015703-3e28c571-f0ce-4c16-bdc5-bcade1faaa08`. Sequence claim: `seqclaim-9893657f9a2377ec83626708` (entry 4231). Graph admission proposal: `ep_337dd27d-1dcd-4ab9-a758-e5cd98303092`; admitted event: `ev-000000015711-7b1df817-4965-4aa5-81ca-4d85e03226f1` (ledger head `575c0d608b4b6d746e7712bbbc00da26348c185ef99670e8e2bbcd8a9c272523`).
