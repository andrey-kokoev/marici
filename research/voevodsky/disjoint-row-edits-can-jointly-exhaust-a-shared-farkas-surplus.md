# Disjoint row edits can jointly exhaust a shared Farkas surplus

Fix local target x<=3 and required packet Q=(0,1,1,1). On the original unit-square rows Q has implied bound 2 and surplus 1. Candidate A raises x-upper bound by 3/4; candidate B raises y-upper bound by 3/4. EACH separately leaves Q valid with surplus 1/4. After A wins a hypothetical local version CAS, rebasing B onto A makes Q's implied bound 7/2, requiring surplus -1/2, so the combined candidate must be refused as `REBASE_PROOF_INVALID`. Fresh `check_noncommuting_row_edit_rebase.py` checks all rational values.

The target x<=3 can still be reproved by x-upper alone with nonnegative surplus 5/4 on the combined row source. That NEW packet is not permission to silently replace the required historical Q packet in a candidate transaction. Row edits on distinct IDs can interact through the shared target-bound slack of one proof; stale candidates require full catalogue validation, not disjoint-row heuristics. All versions are mathematical fixtures, not owner-issued rows.

Next test whether a caller may REQUEST a proof-catalogue replacement as part of B's rebase. Require explicit old/new proof IDs, target, row-manifest digest and signed comparison path updates; replacing Q must not retain stale path identity. Source publication and analytic S,A,R,C,G mapping remain blocked.
