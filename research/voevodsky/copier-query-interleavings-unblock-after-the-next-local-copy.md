# Copier/query interleavings unblock after the next local copy

Fresh `check_copy_two_queries_interleavings.py` runs the same fully wired fixed-signature support copier and two destructive membership queries under four different enabled-redex priority schedules. For all 9,720 runs (support length 0..5, both indices 0..n+1), both outputs match membership and each local rewrite preserves one symmetric wire per live port; every run reaches two BOOL--OUT normal-form components. In 7,290 runs a query rewrite occurs before the first COPY rewrite. A query waiting with its principal port wired to a COPY auxiliary output is temporarily inactive, but COPY's next local rewrite creates a bit principal and reconnects it, unblocking that query.

These four bounded priority schedules are not an exhaustive confluence proof for arbitrary fair schedules or net contexts. The support is still consumed by both probes and add(i)/union remain unimplemented. No Nima work is used.

Next enumerate all enabled-redex choices for tiny supports (n<=2) up to alpha-equivalence of fresh agent IDs; test normal-form uniqueness and termination without priority assumptions. This will isolate any critical pair missed by the four schedules.
