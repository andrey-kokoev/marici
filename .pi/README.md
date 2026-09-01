# Coach and output contracts

This project-local Pi extension is loaded from `.pi/extensions/coach-contract.ts`.
Project trust must be enabled for Pi to load it.

## Coach

```text
/coach dpc [focus]
/coach ask [dpc] <question>
/coach status
/coach stop
```

`/coach ask` performs one direct, bounded coach review without sending the
question to the main agent. The response is displayed as a coach notification.
The DPC coach also runs once after each settled main-agent run. It receives a bounded
projection of visible messages and tool results; hidden reasoning is omitted.
It may notify the operator or inject one bounded follow-up advisory. Repeated
unchanged advice is suppressed. The coach has no file or session mutation
authority.

## Output contracts

```text
/contract list
/contract use dpc-report@1 report
/contract use dpc-report@1 repair
/contract check [schema-id]
/contract status
/contract off
```

`report` records validation failures. `repair` injects at most two bounded
repair requests before stopping automatic repair. A contract checks output
shape, not scientific truth or evidential validity.

Schemas are JSON files in `.pi/schemas/`. Project schemas override global
schemas with the same `$id`. Schema versions are immutable by convention;
changing a schema requires a new version.

The current DPC report contract requires:

- problem
- conjecture
- at least one named rival with claim and discriminator
- at least one risky consequence
- falsification test and exact residual
- disposition

The agent must include one JSON object conforming to the active contract,
preferably in a fenced `json` block. Contract validation results are persisted
as session custom entries with the schema ID, source path, boundary, output
hash, and errors.
