# Delegated Cognition Organization Protocol — run report

Date: 2026-08-17  
Protocol: `docs/delegated-cognition-organization-protocol.md`

## Outcome

The experiment was launched under frozen controls, but it did not produce a
valid cognition comparison. All root workers either timed out or failed their
required structured-output contract. Because the two Stage-A roots failed,
no Stage-B or Stage-C worker was allowed to launch.

This is an infrastructure-blocked run. It is not evidence for or against a
cognition-level or organizational advantage.

## Frozen controls

- Evidence: `evidence.json` (1,332 bytes; SHA-256
  `feaf0ea794c7443366dd61e443305eb1a61b21e6788dbc5c852c2ddb09825568`)
- Answer key: `answer-key.md`; never injected into a worker
- Prompts, authority, bounds, mappings, and repetitions: `run-spec.md`
- Authority: read-only
- Network: not requested
- Worker bound: 300,000 ms
- Pipeline repetitions: 2
- Fresh task/worker identities: yes
- Native cognition mapping:
  - low: gpt-5.6-luna, max reasoning effort
  - medium: gpt-5.6-terra, max reasoning effort
  - high: gpt-5.6-sol, max reasoning effort

## Phase I: one-pass results

| Cognition | Task | Queue | Worker | Total | Terminal result |
|---|---|---:|---:|---:|---|
| low | `dcog_20260817_onepass_low` | 268 ms | 192,941 ms | 320,142 ms | Failed contract; returned only `C2`, `C1`, `other_degrees` |
| medium | `dcog_20260817_onepass_medium` | 420 ms | 300,274 ms | 320,140 ms | Timed out; no terminal result |
| high | `dcog_20260817_onepass_high` | 520 ms | 300,198 ms | 304,993 ms | Timed out; no terminal result |

The low result extracted only the coarse graded ranks. It omitted all ten
required analysis fields, including the decisive quotient and coefficient
gate. Medium and high are unscoreable.

## Phases II and III: sequential low-cognition runs

All six tasks were submitted before either Stage A completed.

| Repetition | Stage | Task | Durable dependency state | Outcome |
|---|---|---|---|---|
| 1 | A | `dcog_20260817_seq1_a` | root | Failed after 297,741 worker ms; JSON remained summary text rather than validated structured output |
| 1 | B | `dcog_20260817_seq1_b` | depends/imports A | No worker launched |
| 1 | C | `dcog_20260817_seq1_c` | depends/imports B | No worker launched |
| 2 | A | `dcog_20260817_seq2_a` | root | Timed out after 300,085 worker ms; no terminal result |
| 2 | B | `dcog_20260817_seq2_b` | depends/imports A | No worker launched |
| 2 | C | `dcog_20260817_seq2_c` | depends/imports B | No worker launched |

Positive orchestration evidence:

- dependencies and imports were durably present in B/C status;
- no dependent worker started before predecessor success;
- failed/malformed Stage-A outputs did not cross a stage boundary;
- no parent-agent advancement call was made.

Defect evidence:

- B and C remain `accepted_for_execution / waiting` after their predecessors
  are terminally failed, instead of becoming durably dependency-blocked.

## Rubric

| Dimension | One-pass low | One-pass medium | One-pass high | Sequential 1 | Sequential 2 |
|---|---|---|---|---|---|
| Extraction accuracy | Partial: ranks only | Not scoreable | Not scoreable | Not admitted | No output |
| Reframing quality | Failed | Not scoreable | Not scoreable | Not scoreable | Not scoreable |
| Reduction accuracy | Failed | Not scoreable | Not scoreable | Not scoreable | Not scoreable |
| Coefficient discipline | Not demonstrated | Not scoreable | Not scoreable | Not scoreable | Not scoreable |
| Evidence discipline | Not demonstrated | Not scoreable | Not scoreable | Not scoreable | Not scoreable |
| Error recovery | N/A | N/A | N/A | C never launched | C never launched |
| Efficiency | Very poor | Timed out | Timed out | Timed out at A | Timed out at A |
| Stability | Not applicable | Not applicable | Not applicable | No endpoint | No endpoint |

No aggregate score is reported because the arms are not comparable.

## Authorized defect reports

- `sfb_68c6477f4162`: root workers consume the full bound on a tiny native
  preflight packet and lose or fail terminal structured output.
- `sfb_eb876fb00aa0`: descendants remain waiting after predecessor terminal
  failure.

## Interpretation and rerun gate

Do not reuse this run as a cognition benchmark. A valid rerun requires:

1. bounded workers to emit a terminal structured result reliably within the
   frozen runtime;
2. failed predecessors to reconcile descendants into an explicit
   dependency-blocked terminal state;
3. a fresh run with new task identities and the same evidence, prompt, answer
   key, and cognition mappings.

Changing the bound or prompt in place would invalidate the frozen comparison.
