# Conditional preservation for the query/boolean splits

Examined executable branches in `checkers/check_copy_two_queries_interleavings.py`: Q_S--N and Q_R--B0/B1. These are three typed cases, not two. The following are mathematical boundary arguments, not machine-checked universal theorems.

Assume a finite port-linear forest with the declared arities, matching OUT_i--Q_i.r edges, recursively typed tails, and independently rooted COPY output branches. All boundary wires below denote the actual outside peers of removed auxiliary ports, not arbitrary potentially aliased names.

## Q_S--N

The removed subgraph has exactly two outside connections: Q_S.r to unary OUT_i.p and Q_S.a to the budget head K/N.p. NIL has no auxiliary port. Replace it by FALSE.p--OUT_i.p and E.p--the same budget head. Removing the unary OUT branch cannot disconnect anything else; the remaining budget side acquires its own eraser root. Budget type is accepted by E. The removed principal NIL and query do not own original support. No COPY-facing branch loses its root: the budget is a finite K/N chain, hence cannot reach COPY under the tail grammar. The result is two rooted components, with all unrelated components unchanged.

## Q_R--B_b, b in {0,1}

The two outside connections are Q_R.r--OUT_i.p and B_b.a--support successor. Replace them by BOOL_b.p--OUT_i.p and E.p--the same support successor. The successor is B0/B1/N.p or COPY.a/b. In the former case E has an admitted active pair; in the latter it has a permitted wait. The consumed bit is copied, not original. The suffix side formerly anchored through Q_R/OUT now has the fresh E anchor. If that side reaches COPY, its branch retains an independent root; no connection is introduced between the two COPY sides. The boolean component is separately rooted at OUT_i. In a forest the replacement cannot hide an additional outside connection or cycle.

## Scope and next obligation

These arguments require the complete typed forest premises, not root membership alone. They establish local preservation for the stated splits conditional on those premises and accurate rule implementation. Together with COPY--N and E--K they address five of fifteen typed cases. The remaining cases are COPY--B0/B1, Q_B--K/N, Q_S--B0/B1, Q_R--N, E--B0/B1/N. Next assemble a single explicit invariant (including arities, forest property, original ownership and phase ports) and a ten-case remaining ledger. Arbitrary-n reachability, semantic correctness, and commuting-rewrite/confluence proofs remain separate obligations. No correspondence with the nine-point superform problem is asserted.
