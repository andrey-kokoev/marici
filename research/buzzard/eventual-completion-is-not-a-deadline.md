# Eventual completion is not a deadline

Owner: `marici.Buzzard`

Strength: bounded execution-trace theorem and hostile delay family.

## Result

`CompletesBy bound trace` records an explicit logical-step witness no later
than `bound`. Lean proves bounded completion implies eventual completion.

The converse fails uniformly. For every proposed bound `b`,
`delayedCompletionTrace (b + 1)` is transition-valid and eventually completes,
but does not complete by `b`. Thus liveness supplies no finite deadline.

`Deadline` keeps the natural-number amount and `TimeUnit` distinct. A one-step
deadline is not interchangeable with a one-millisecond deadline. A positive
fixture certifies `completingTrace` by one logical step.

`DeadlineGrant` separately carries optional source authority. Lean exhibits
real one-step completion evidence together with an unauthorized deadline
grant, proving that observation does not authorize a promise.

## Missing interfaces

A physical deadline requires a source clock, a conversion between clock units,
scheduler and failure-delay bounds, a start event, endpoint convention,
confidence/error semantics where applicable, and source authority for the
promise. None is inferred from eventual completion.

## Verification

From `research/buzzard/marici_formal/`:

```powershell
& "$env:USERPROFILE/.elan/bin/lake.exe" env lean MariciFormal/BoundedLiveness.lean
& "$env:USERPROFILE/.elan/bin/lake.exe" build
```

Results on 2026-08-25: targeted exit code `0`; full build completed
successfully with `8735 jobs`. No site build or Git command was run.

Changed owned files:

- `research/buzzard/marici_formal/MariciFormal/BoundedLiveness.lean`
- `research/buzzard/marici_formal/MariciFormal.lean`
- `research/buzzard/eventual-completion-is-not-a-deadline.md`
