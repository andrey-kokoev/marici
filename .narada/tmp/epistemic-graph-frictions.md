# Epistemic Graph Ergonomics — Running Friction List

Temporary working log. Update after each Marici graph pass; remove items when verified resolved.

## Active

1. **Semantic duplicate checks are single-query only**
   - A pass with several candidate concepts requires repeated `epistemic_graph_query` calls.
   - Desired: one bounded batch-query accepting multiple search terms and returning compact grouped matches.

2. **Ledger extraction still requires manual section discovery**
   - Each source needs a headings search followed by selected range reads.
   - Desired: a bounded source-inspection helper returning title, status, epistemic-boundary, decision, and exact line locators without attempting semantic admission.

3. **Loader-wrapped child results duplicate representations**
   - Child data is commonly present in both textual `content` and `structuredContent` inside the loader result.
   - This wastes context even when the caller uses only the structured projection.
   - Desired: a compact structured-result mode that preserves errors, paging references, and typed summaries.

## Resolved and verified

- Source declarations can be batched with `epistemic_graph_capture_sources`.
- Capture reports exact existing-identity collisions.
- Review and admission remain explicit separate actions.
- Proposal readback derives admitted/rejected/reviewed lifecycle state and exposes event identity.
- Core and namespaced extension relation vocabulary is discoverable.
