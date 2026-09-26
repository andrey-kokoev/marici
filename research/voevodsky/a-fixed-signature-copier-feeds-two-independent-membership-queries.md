# A fixed-signature copier feeds two independent membership queries

Fresh `check_copy_two_queries_port_graph.py` constructs ONE explicit wired graph: a B0/B1 support chain feeds COPY; COPY has two output wires connected to independent unary-index query agents. Fixed local COPY--B0/B1/NIL rules generate two fresh chains. Both queries then destructively normalize via Q_B/Q_S/Q_R and eraser rules. Exhaustive 2,430 support/index-pair cases (n=0..5, each index 0..n+1) match both expected membership answers. After EVERY rewrite, every live port has exactly one symmetric wire; final graph has exactly two BOOL--OUT components. Maximum observed rewrites: 32.

This demonstrates explicit local copying can supply two continuations without fanout. It is NOT reusable beyond those two queries: both copies are consumed. The scheduler runs COPY to completion before either query; arbitrary interleavings/confluence are not tested. Local add(i)/union and any translation from Nima's mathematics remain open.

Next test adversarial fair interleavings of COPY and queries. A query can encounter COPY's auxiliary output port before the next bit is materialized; determine whether this is a benign temporarily inactive configuration that later unblocks or a deadlock. Require the same two outputs under every tested schedule, then study general confluence.
