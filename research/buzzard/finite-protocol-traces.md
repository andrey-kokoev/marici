# Finite protocol traces

`runFencedTrace` executes an arbitrary finite list of fencing tokens. Its main
accounting theorem states that the final protected-effect count equals the
initial count plus the number of successful trace steps. A second theorem bounds
successes by trace length.

Executable histories show:

- repeated token `[4,4,4]` executes once against one authoritative register;
- two disconnected one-step histories each execute token `4`, totaling two
  global effects despite satisfying the local invariant;
- issuer-qualified requests `[A/7,B/7]` are duplicate-free, while erasing issuer
  authority produces the ambiguous history `[7,7]`;
- a witness trace is usable only when every entry is scoped, authentic, fresh,
  and current; one forged entry invalidates the trace.

The trace model proves safety/accounting properties only. It does not claim
liveness, fairness, eventual communication, or recoverability from an in-doubt
external effect.

Missing convention-fixed inputs:

- scheduler and concurrency-to-trace linearization interface;
- crash/restart events and persistence boundaries;
- fairness or progress assumptions;
- trace equivalence for genuinely concurrent histories.

Verification commands from `research/buzzard/marici_formal`:

```text
lake env lean MariciFormal/ProtocolTrace.lean
lake build
```

Result: both commands passed under Lean `v4.33.1`; the project reported
`Build completed successfully (8719 jobs).` The site build was not run.
