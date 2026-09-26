# Candidate unified invariant and remaining ten preservation cases

Status: explicit mathematical proof ledger checked against the executable branches of `checkers/check_copy_two_queries_interleavings.py`; not a machine-checked theorem. No new exhaustive test counts are asserted here.

## Candidate invariant I

Graphs are finite port-linear forests (including exclusion of self-loops and parallel-edge cycles), using exactly the declared agent arities. There are exactly two distinct OUT nodes, at most one COPY, and at most one Q per output channel. Each OUT_i.p meets Q_i.r or a unary BOOL.p; every Q result meets its corresponding OUT. Every connected component contains OUT or E.

The constructor marks a finite original B/N chain. Live originals form its suffix, attached only at its head to COPY.p; originals exist iff COPY exists. No Q/E consumes an original and no rewrite creates an original. All remaining B/N and K are non-original. Original B successors remain original, K successors are K/N principals, and copied B successors are copied B/N principals or COPY.a/b. Every such successor walk is finite.

Q_B.p meets a budget K/N principal and Q_B.a meets copied support B/N principal or COPY auxiliary. Q_S.p meets copied support or COPY auxiliary and Q_S.a meets budget K/N principal. Q_R.p meets copied support or COPY auxiliary and has no saved tail. E.p meets non-original B/K/N principal or COPY auxiliary. COPY auxiliary peers are restricted to Q_B.a, Q_S.p, Q_R.p, E.p, or copied B.a. After removing COPY, its two auxiliary components are disjoint and each contains OUT or E; its source component is precisely the original suffix. These conditions include constraints missing from the earlier coarse root-coverage invariant.

## Ten cases not covered by the preceding split/NIL lemmas

* COPY--B0 and COPY--B1 (2): remove original head, insert one fresh copied B on each auxiliary side and a fresh COPY owning the old original successor. Cutting the new COPY exposes exactly the old independently rooted sides extended by one bit. No sides merge, no original is created. The source suffix loses one head.
* Q_B--K (1): the old support peer of Q_B.a becomes Q_S.p's peer; K's budget successor becomes Q_S.a's peer; the result peer stays OUT_i. The three boundary attachments remain connected through the replacement query. Phase roles interchange correctly, including support waiting at COPY. No branch loses its output root.
* Q_B--N (1): budget NIL and Q_B are replaced by Q_R, retaining OUT_i and the old support peer. There is no third budget boundary to detach. COPY waiting is allowed at Q_R.p.
* Q_S--B0 and Q_S--B1 (2): the saved budget becomes Q_B.p's peer, and the consumed bit's support successor becomes Q_B.a's peer; OUT_i is retained. The three external boundaries remain joined by a query with the correct phase. The consumed bit is non-original.
* Q_R--N (1): the only external boundary is OUT_i. Replace the query/NIL by FALSE attached to OUT_i. There is no residual tail and no COPY branch through this pair.
* E--B0 and E--B1 (2): transfer E to the bit successor, which is copied B/N or COPY auxiliary. The same residual side retains an eraser root; no other side is connected or disconnected except the deleted head. Waiting at COPY remains permitted.
* E--N (1): two unary nodes form an isolated component. Deleting that entire component cannot remove the sole root of a surviving component or a COPY side.

Together with COPY--N, E--K, Q_S--N, and Q_R--B0/B1, this enumerates all fifteen typed pairs. For the connected-boundary replacement cases, forest preservation requires the removed active-pair subgraph to be a tree whose distinct outside attachments have no alternative connecting path; otherwise the original graph would already contain a cycle. This assumption is why a genuine multigraph forest condition matters.

## Outstanding verification

The ledger suggests closure of I, but its premises must be implemented as ONE validator and tested on adversarial graphs, not inferred from scattered partial validators. In particular the old forest checker collapsed parallel edges, and provenance-blind canonicalization needs justification when used for tagged graphs. Next implement a port-edge multigraph forest audit that rejects parallel edges and combine it with explicit COPY peer/source and tail-tag checks. Constructor establishment, universal closure, Boolean semantics, and commuting reductions remain separately reviewable obligations. The physical nine-point contour problem is not encoded here.
