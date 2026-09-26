# Linear cleanup acknowledgment and query return interface

Critical-path decision: strict barriers require a causal return path from cleanup; this is the necessary primitive before joining readiness signals. Implemented isolated EA(p,r), DONE(p), ACK(p) prototype in `acknowledging_eraser.py` using the existing port-linear replacement routine. ACK is a passive test boundary, not a polling mechanism in the net.

Rules: EA--B0/B1/K removes the data head, passes its successor to fresh EA.p, and transfers the old r peer to fresh EA.r. EA--N removes both and attaches fresh DONE.p to the old r peer. There are four typed cases. All external and fresh ports occur exactly once.

For a finite tail of length m (excluding NIL), induction gives exactly m+1 rewrites, exactly one EA-or-DONE at every step, and DONE iff the owned data tail has been exhausted. Its r wire never disappears before the DONE handoff. Port-linearity prevents copying the acknowledgment. Fresh test covers all 1,093 B0/B1/K chains of lengths <=6, checking 8,201 intermediate states, acyclicity, no early signal, uniqueness and exact counts. Mixed B/K tails are allowed by this primitive even though normal query tails are homogeneous.

## Query integration design (not yet implemented)

Give each query phase an additional return auxiliary c, alongside its current data/result ports. Every nonfinal phase transition must forward c exactly once. Q_S--N and Q_R--B produce their Boolean at OUT and route c to fresh EA.r, with EA.p receiving the leftover budget/support. Q_R--N has no leftover tail and emits DONE directly at c while producing FALSE at OUT. These cases partition query completion: one deferred cleanup acknowledgment or one direct acknowledgment, never both. An EA waiting at a COPY auxiliary cannot fire until data is produced, so it cannot prematurely acknowledge an unmaterialized suffix.

This acknowledges only the query's owned branch. It is NOT a whole-operation done signal: retained support completion and any other producer branches require separate obligations. The isolated test does not establish integration behavior when producer and query reductions interleave. Next implement the return-bearing query phases with the retained copier, check absence of early DONE under all small redex schedules, then connect a retained-word completion signal and join. Existing dataflow rules are unchanged.
