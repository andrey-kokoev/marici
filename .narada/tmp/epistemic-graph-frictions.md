# Epistemic Graph Ergonomics — Running Friction List

Temporary working log. Update after each Marici graph pass; remove items when verified resolved.

## Active

- None from this pass. Continue recording newly observed friction here.

## Resolved and verified

- Batch duplicate discovery is available through `epistemic_graph_query_batch` and was verified live with three grouped queries.
- Bounded structural ledger inspection is available through `epistemic_graph_source_inspect`; live verification returned all relevant sections with exact line ranges and explicit truncation.
- Loader-wrapped structured results no longer duplicate textual content; the compact structured envelope was verified live.
- Immutable correction is available through `epistemic_graph_proposal_resubmit`; live verification removed one named relation from a 31-operation proposal without paging and the verification draft was rejected.
- Compact capture receipts now remain compact through the loader boundary; detailed proposal reads remain explicitly paged.
- The `mcp-surfaces` Site is explicitly admitted by the carrier contract, preserving Site isolation while making its Git MCP available after restart.
- Native Registrar advertises all 14 epistemic tools, and native release refreshes canonical Site sidecar artifact pins before rebuilding admission metadata. The complete release and carrier transaction passed.

- Source declarations can be batched with `epistemic_graph_capture_sources`.
- Capture reports exact existing-identity collisions.
- Review and admission remain explicit separate actions.
- Proposal readback derives admitted/rejected/reviewed lifecycle state and exposes event identity.
- Core and namespaced extension relation vocabulary is discoverable.
