# Typed Executable Frontier Protocol

## Purpose

The Typed Executable Frontier Protocol (TEFP) organizes research as typed objective decomposition whose actionable frontier contains only presently executable issue-boundary work. The graph may display blocked leaves for reconciliation, but they are not actionable. A disposition enables successors; transport, approval, or graph admission does not constitute scientific evidence.

## Structure

A research tree has the form

```text
programme objective
→ bounded research objectives
→ executable issue-boundary tests
→ evidence-bearing dispositions
→ conditionally enabled successors
```

Each child must resolve a necessary subquestion, discriminate a rival, or construct a typed object required by its parent. Topical similarity alone does not define a parent–child relation.

## Executable frontier

The frontier is an antichain of work executable under current authority and available evidence. It may contain zero, one, or several leaves. Selection identifies current focus; it is not required when no work is active.

Do not create an open leaf whose only action is to wait for another owner, source, map, credential, or authority transition. Attach that blocker and its reopening condition to the research leaf that encountered it, then remove the blocked branch from the actionable frontier.

## Issue-boundary record

Apply DPC once at each substantive explanatory issue boundary, not recursively to every proof step. Record:

1. problem;
2. bold conjecture;
3. named rivals;
4. risky consequences;
5. strongest falsification attempt and exact residual;
6. disposition and surviving scope.

Administrative cleanup and authority-only blockers are not substantive DPC cases.

## Evidence and transitions

Proofs, sources, checkers, datasets, and result artifacts carry evidence. Graph records coordinate objective state and cite that evidence; graph admission does not certify truth.

Attach evidence using the structured field:

```json
{
  "evidence": {
    "graph_entity_ids": ["source-or-result-id"],
    "artifact_paths": ["research/owner/checker.py"]
  }
}
```

`graph_entity_ids` create `derived_from` relations. `artifact_paths` are durable repository locators retained on the issue record. A path reference does not certify its contents. The compatibility field `evidence_ids` remains readable, but new transitions use `evidence`.

Every revision uses a distinct successor `node_id`, increments `version`, and names the immediate prior entity with `predecessor_id`. Reusing the predecessor's entity ID is refused because it would create a self-superseding relation.

Prefer the ordinary selected-leaf transition for research progress: supply the freshly resumed `selected_node_id`, `expected_node_version`, a fresh idempotency key, one typed disposition, structured evidence, and only the successors enabled by that disposition. Use administrative `nodes` batches for bootstrap, repair, or explicit multi-node revisions rather than ordinary closeout.

When a leaf reaches a disposition:

1. record structured evidence references, checker outcomes, and the exact residual;
2. mark the leaf disposed rather than leaving it actionable;
3. enable only successors licensed by that disposition;
4. preserve negative results as closed boundaries rather than recurring work;
5. open a rival branch only when it can change the parent disposition;
6. resume the tree and verify the selected node, frontier, version, and evidence-reference count.

A failed transport or malformed transition payload is an execution defect, not a scientific residual. Correct validation-refused content before retry; if a failed pre-admission attempt reserved a caller-defined idempotency key, use a fresh key for corrected content.

## Operational loop

At each natural work boundary:

1. resume the durable tree and read the selected node plus bounded frontier;
2. reject stale local assumptions about node identity or version;
3. perform one coherent executable objective and verify it in its owning evidence system;
4. use verbose tool inspection when a transition contract is unfamiliar;
5. transition atomically with disposition, structured evidence, and enabled successors;
6. resume again to verify durable readback before reporting or continuing.

Compact resume is sufficient for familiar continuation. Detailed resume is required when titles, rationales, blockers, or evidence counts affect the decision. Selection records focus, not ownership, truth, or live process presence.

## Completion

A bounded objective closes only when its declared completion criterion is met or a typed obstruction proves that criterion unavailable under the stated source envelope. Closing a child does not close its parent unless the parent completion criterion follows.

## Specializations

A vertical TEFP instance has a dependency chain whose frontier normally advances through one selected leaf. A comparative TEFP instance may retain several independent executable rivals. These are specializations of the same protocol; neither frontier cardinality is universal.

## Related protocol

See [`../delegated-cognition-organization-protocol.md`](../delegated-cognition-organization-protocol.md) for delegation and organizational structure.
