# Recursive history and return coherence

The existing two-level Store now records every accepted mutation as a batch of
old/new leaf records. Its promotion endpoints, retained descendants, versions,
and mean-return rules remain those of recursive-promotion-and-versioned-return.md.

## Compensation

Serialized LIFO compensation checks the current payload against the event's
expected result and applies its inverse content change. Every restored or
removed leaf gets a new version counter; ancestors are rebuilt and versioned.
The original event stays in the log and a compensating event is appended.
Thus live values can return to an earlier state without reviving stale requests.
Generated family/endpoint identities remain allocated.

This is a serialized model: validation and mutation are one logical operation.
There is no concurrent lock, crash-safe journal or distributed transaction
implementation. Compensation is LIFO and content-restoring, not arbitrary
history deletion or numeric version rollback.

## Route coherence after membership changes

For an upper family, a direct mean shift delta makes the same leaf-value change
as shifting each of its child family means by delta under the existing
minimum-change contract. The test passes in three membership states: before an
insertion, after the insertion, and after deleting that inserted member.
Each request uses a fresh snapshot for its chosen route.

The routes have different numbers of commits and different ancestor-version
histories. The proven/tested comparison is equality of final leaf payloads and
means, not equality of audit history. Interleaved conflicting edits would require
retry/transaction semantics beyond these sequential route fixtures.

## Replay

An exact rational event packet including compensation is serialized to a
 temporary JSON file and read back. Replay validates each whole batch's old
records before applying new records. The16-event fixture returns to the empty
live state. A corrupted old-record precondition is rejected.

This is an audit serialization roundtrip. It does not establish durable commit,
crash recovery, or recovery of the entire interned identity registry from the
leaf log. Such persistence needs a storage protocol for identity allocation
and derived-view reconstruction.

## Structural result

One implementation now combines recursive family identity, scoped/versioned
returns, reversible content changes, and preserved event history. It separates
three notions: same current content, same versioned object, and same history.
That distinction makes presentation-route equivalence and stale-edit rejection
compatible rather than contradictory.

## Verification

    python research/nima/checkers/check_recursive_history_coherence.py

The test first runs the existing100-operation recursive transaction checks,
then tests route coherence across membership changes, compensation with stale
snapshot rejection, rational serialization/replay and a corruption control.
The Store remains a finite executable prototype, not a general dependent-type
formalization.
