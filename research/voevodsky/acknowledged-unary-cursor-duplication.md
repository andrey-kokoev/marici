# Acknowledged unary cursor duplication

Implemented `checkers/acknowledged_unary_copy.py` with DC(p,a,b,c). DC--K emits two fresh K cells at a,b, passes the input tail to successor DC.p, attaches new K tails to successor a,b, and forwards c. DC--N emits two distinct fresh NILs and one DONE at c. No generic word-COPY rule was changed.

## Invariant and proof

After j nonterminal steps on K^n N, each output is a separate prefix of j fresh K cells whose tail faces the corresponding auxiliary of the unique DC. Its principal faces the remaining complete K^(n-j) N input. Its c owns the sole acknowledgment continuation. Every consumed input cell is gone; no garbage is created. The invariant holds at j=0 and DC--K preserves it with j+1. DC--N is enabled exactly at j=n; it consumes the original NIL and DC, fills both output tails with distinct NILs and emits DONE in that same rewrite. Thus DONE implies both chains complete and independent and all copying work exhausted. Cost n+1.

For passive contexts, cut the a,b,c interface peers into three leaves. Rules depend only on DC's principal and the next input cell. All three distinct outside port endpoints occur exactly once, so rewiring commutes with the cut even when the endpoints are ports on one agent and the uncut graph has cycles. This proves passive-context isolation, not safety under arbitrary active consumers of partial output.

The executable audit passed130 runs4290 rewrites, lengths0..64, both separate leaf roots and one passive three-port cyclic boundary. Every replacement uses exactly its exposed/fresh ports; final output chains are disjoint and together with roots/DONE account for all live nodes. The terminal guarantee is a written inductive proof plus bounded tests, not formal Python verification.

## Runtime triple-cursor preparation

For the loop, first duplicate the cursor into query candidate A and intermediate B, then duplicate B into insertion candidate C and retained cursor D. Each duplication costs n+1; release the second only after the first DONE and the query only after the second DONE. A fixed latch can hold A and forward the later completion without needing a third copy. No consumer may start from a merely available prefix. This yields three complete disjoint chains using fixed control arities rather than a host copy of n.

Next implement that two-stage preparation and its release latch as a reusable local runtime component; validate that the initial cursor length is not stored as host control state. This is the remaining linear-resource prerequisite before fuel-controller implementation. Loop execution itself remains unimplemented.
