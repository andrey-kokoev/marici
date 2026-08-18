# Marici ledger-number sequence

Numbered Marici ledger entries obtain their numbers from the epistemic-graph
sequence allocator. A directory scan, Git history, branch state, chat message,
or manually incremented filename is not allocation authority.

## Authority

- Direct MCP binding: `marici-epistemic-graph`
- Sequence name: `marici-ledger-entry`
- Sequence ID: `seq-3475727b9d10d9e7689ae83e`
- Initial value: `678`, after an audited maximum ledger number of `677` on
  2026-08-18

## Creating an entry

1. Directly load or rebind `marici-epistemic-graph`.
2. Before choosing a filename, call
   `epistemic_graph_sequence_claim_next` with:
   - `sequence_name: marici-ledger-entry`
   - the stable Marici actor identity;
   - an authority basis naming the entry being created; and
   - a unique, intent-specific idempotency key.
3. Use the returned integer exactly once in the filename and entry heading.
4. Inspect `epistemic_graph_sequence_status` or
   `epistemic_graph_sequence_claims` when an audit is needed.

Claims are permanent, monotonic, and never released or reused. If the proposed
entry is abandoned, its claimed number remains an auditable gap. Retrying the
same allocation intent must reuse its original idempotency key; a distinct
entry must use a new key.

Existing historical collisions are not silently renumbered. Repairing them
requires an explicit migration with preserved provenance.

## Example request

```text
sequence_name: marici-ledger-entry
actor: marici.Benincasa
authority_basis: Creating the next numbered Marici ledger entry
idempotency_key: marici-benincasa-<entry-topic>-<date>
```

The returned claim, rather than the currently visible maximum, is the sole
authority for the new entry number.
