# Hardware-bound pushforward acquisition

This layer binds the commuting-square auditor to immutable acquisition identity. It does not claim hardware execution; it defines the packet that hardware must emit and verifies a synthetic reference packet through the same path.

## Bound objects

- `run_id` identifies one immutable acquisition ledger.
- `event_id` is unique and stable across every compiled view.
- `raw_digest` hashes the canonical ordered raw events.
- `packet_digest` hashes the complete acquisition packet.
- `compiler_digest` hashes the exact compiler implementation used to form parent and refined views.
- `contract_digest` hashes the admission contract.
- `parent_view_digest` and `refined_view_digest` bind the two compiled outputs.
- provenance sets declare which raw fields each refined local label may consume.

The admission receipt contains all seven digests, event counts, the exact pushforward verdict, and the claim boundary. A Bell analyzer must consume the receipt rather than an unbound table.

## Hardware handoff

The detector acquisition service must replace the synthetic rows without changing field names or compiler semantics. It must preserve no-click rows, use stable event identifiers before coincidence classification, record setting-source health independently at both wings, and bind the coincidence-window identifier rather than scanning it after seeing Bell statistics.

Changing compiler bytes, packet bytes, event identity, setting maps, outcome maps, provenance, or coincidence policy invalidates the receipt and requires recompilation. Changing the measurement apparatus requires a new `run_id` and parent packet.
