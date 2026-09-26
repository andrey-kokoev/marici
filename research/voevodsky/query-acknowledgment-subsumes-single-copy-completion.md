# Query acknowledgment subsumes COPY completion in the isolated retained query

Implemented `acknowledged_membership.py`: each query phase carries c, transferred once on phase changes. Q_S--N and Q_R--B route c through EA; Q_R--N emits DONE directly. EA forwards its r along data and emits DONE only on NIL. ACK is a passive boundary, not a host readiness scan.

Fresh exhaustive test over 31 single-call inputs visits 472 forest classes and 638 edges, including 14 EA-to-COPY waits. Exactly one live query, EA or DONE owns the return path at every state. At every observed DONE, the retained word and Boolean are correct and COPY and all query/cleanup controls are absent.

## Stronger single-call implication

The earlier plan proposed a separate COPY acknowledgment and join. That is unnecessary for this restricted single-copy topology: every query-completion route has consumed the query-side COPY-produced NIL.

* Q_R--N consumes it directly.
* Q_S--N consumes it before cleaning the remaining finite budget.
* Q_R--B delegates the support successor to EA; EA must traverse the remaining query support to its NIL before emitting DONE.

That support NIL is created only by COPY--original-N. The same rewrite simultaneously attaches NIL to the retained branch and removes the unique COPY. Since the retained branch has no active consumer, its full word is already present when query-side NIL can be consumed. Thus DONE implies COPY completion as well as Boolean readiness and garbage exhaustion, for any legal single-call schedule. This follows from the rule topology, not a coincidence of the bounded count.

No analogous claim is made for arbitrary multi-producer pipelines: another branch may retain unrelated pending work. Nor is the pending Boolean alone a cleanup acknowledgment. The current implementation observes DONE but does not use it to release a continuation.

Critical next move: a local gate retaining ownership of the next operation's input boundary until DONE arrives. The single-call implication avoids building a redundant two-signal join. Gate design must keep an inactive next-operation principal away from RET until acknowledgment, while preserving the old result and returned word. Then demonstrate two calls with an internal DONE-triggered transition, not a host callback.
