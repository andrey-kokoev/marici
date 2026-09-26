# Finite strict query chains

Implemented `strict_query_chain.py` by composing the existing six-port gates at construction. Runtime uses the existing GATE--DONE and acknowledging membership rules unchanged. Gate/output lists are diagnostic/observation metadata, not an instruction dispatcher. Empty programs return the unchanged word and initial DONE; one query has no gate. Each additional query inserts a gate between the current support/acknowledgment endpoints and the final RET/ACK.

## Induction on remaining calls

Before the first call completes, the suffix of gates is passive: the first gate's principal faces its active query/EA return auxiliary, and every later gate principal faces the previous gate's c auxiliary. None is a DONE principal pair. Budgets and outputs are passive. Cut the first pending gate's s,p interfaces as in the two-call proof; the entire suffix replaces the former four dormant resources but still has no enabled redex. Thus the active call simulates an isolated acknowledged membership operation.

Its completion supplies DONE only after COPY/query/cleanup exhaustion. Exactly the first pending gate then becomes enabled. Its one rewrite consumes that DONE and gate and creates the next COPY/QB, threading its retained and return outputs into the remaining gate suffix. This restores the same invariant with one fewer pending call. Earlier BOOL--OUT pairs stay isolated and cannot change. There is no mechanism by which a later gate can receive DONE first.

Induction yields strict no-overtaking, correct ordered membership answers, unchanged retained word and eventual final acknowledgment along every maximal actual-rewrite execution. For r queries, the exact count is sum_t(2n+i_t+3)+max(0,r-1). This is a written argument based on the cut-interface lemma, not formal verification of Python or arbitrary cyclic networks.

Fresh `check_strict_query_chain.py` tests 847 runs through sequences of length0..4 with indices0,1,3 and words n<=2, using seeded random individual choices. It checks 23,584 rewrites and 2,142 ordered gate releases, absence of previous-call controls at release, correct prior results, exact counts and no final ACK while work remains.

Next critical milestone is mixed strict programs, not further samples of query-only chains. Insertion and union currently lack return-bearing finalization. Unlike membership cleanup, these operations can finish their active zipper while forwarding an upstream tail in a dataflow context; their acknowledgment contract must explicitly require a completed isolated input or certify the forwarded stream. For strict programs each gate can supply completed inputs, simplifying this obligation. Specify return-bearing add/union and gate variants with fixed arities, then establish a common postcondition suitable for induction over operation kinds.
