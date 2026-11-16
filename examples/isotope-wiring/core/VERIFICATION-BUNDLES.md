# Replayable selective-verification bundles

`verification-bundles.mjs` makes the process-local result transport in
[SELECTIVE.md](SELECTIVE.md) replayable in another fresh process running the exact
same engine sources. Ordinary revision bundles still omit verification reports.

## Export and replay

```
const baseline = store.verifyAt(sourceRevision)
const result = store.verifyAt(targetRevision, { reuseFrom: sourceRevision })
const bundle = exportVerificationBundle(store, [result.id])

// Serialize as JSON; in another process:
const { store: replayed, reports } = replayVerificationBundle(parsedBundle)
```

The bundle contains the complete revision bundle, requested verification roots,
and their baseline dependency closure in deterministic topological order. The
revision history is dependency-complete, not minimized to the requested reports.
Reports and the outer envelope have content identities and engine bindings.

Replay uses an isolated store. It first replays the construction history, then:

1. Fully recomputes every report with no transport baseline.
2. Resolves each selective report's exact earlier baseline verification ID.
3. Runs selective checking against that freshly reconstructed, trusted report.
4. Compares the complete computed receipt with the serialized claim, including
   status, residuals, read digests, reused/computed modes, and all state bindings.
5. Re-exports the requested dependency closure to check canonical completeness.

Raw serialized reports never enter the trusted baseline cache. The existing
`verifyModelSelectively` rejection of deserialized reports is unchanged.

## Exact baseline identity

A revision can have multiple reports: for example, a full check followed by a
selective check using another baseline. They need not share a verification ID,
even if their predicate results agree. Replay cannot substitute whichever report
happens to be latest at that revision.

The store now accepts `verifyAt(target,{reuseVerificationId:id})`, optionally with
`reuseFrom:sourceRevision` as an additional binding check. It resolves the archived
report by its exact ID. The original `reuseFrom`-only API still selects the latest
report at the named source revision.

The bundle follows these exact ID dependencies, not revision names alone. A
missing dependency, wrong baseline revision, wrong state, or mismatched engine is
refused. Duplicate reports, unreferenced reports, and noncanonical dependency
orders are also refused. Export and replay admit at most 1,024 reports per bundle;
this is not a complete resource sandbox.

## Evidence boundary

These are replayable implementation-level certificates, not signatures or formal
proof terms. Recomputed content hashes alone do not validate a false claim: the
checker and read-projection logic must reproduce it. Conversely, anyone can
produce another valid bundle for data of their choosing; no authorship or external
truth is authenticated.

The mechanism depends on the manually maintained predicate read contracts, whose
current evidence is source review and differential tests. It does not establish
a universal predicate-preservation theorem for rules. Typed-rule provenance in
the underlying history still requires the separate `verifyRuleHistory` audit;
ordinary ground replay and model verification do not certify that declaration.

A bundle can be serialized and replayed across processes, but there is no automatic
disk store, source-version migration, distributed publication protocol, or
cryptographic trust infrastructure. Engine-source changes intentionally invalidate
previous-engine bundles until a migration mechanism is supplied.

## Executed checks

Seven tests in `tests/isotope-wiring-verification-bundles.test.mjs` cover normal
transport, a real fresh Node subprocess, multiple reports at one revision,
missing/duplicate dependencies, exact baseline bindings, unreferenced reports,
missing construction history, and engine mismatch. Forged statuses and reuse modes
are refused even after both report and envelope hashes are recomputed.

The later matching, join-search, isomorphic-join/search, persistent-join, and
[context-lifting](CONTEXT-LIFTING.md) and [context-composition](CONTEXT-COMPOSITION.md)
suites bring the sixteen structural suites to 162 tests. Legacy editor TODO failures remain separate; visualization and
website behavior are unchanged.
