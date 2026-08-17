# Frozen run specification

Date: 2026-08-17

- Protocol: docs/delegated-cognition-organization-protocol.md
- Evidence: evidence.json only
- Answer key: answer-key.md; never injected into worker sessions
- One-pass prompt: use the evidence question and return the strongest justified
  result, separating constructed facts from compatible hypotheses.
- Cognition mapping (native runtime readback):
  - low: codex-subscription / gpt-5.6-luna / max
  - medium: codex-subscription / gpt-5.6-terra / max
  - high: codex-subscription / gpt-5.6-sol / max
- Authority: read-only
- Filesystem: admitted Marici site root; each worker preflight receives only
  evidence.json unless a predecessor output is explicitly imported
- Network: not requested
- Runtime bound: 300000 ms per worker
- Output contract: bounded structured JSON; no transcript import
- Sequential repetitions: 2
- Fresh worker sessions: required
- Automation prerequisite: passed by neutral A-to-B-to-C durable-event test on
  2026-08-17 before this run
