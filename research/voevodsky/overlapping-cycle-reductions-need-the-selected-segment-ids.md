# Overlapping cycle reductions need the selected segment IDs

Fresh `check_overlapping_cycle_reductions.py` uses a four-edge A->B->A->B->A synthetic walk with unique edge occurrence IDs e1..e4. There are three overlapping two-edge closed subpaths. Removing the first pair or the middle pair yields the same residual VERTEX walk A->B->A but different retained edge IDs, removed segment digests, and residual digests. Each derived view must commit its chosen segment and original full path; equal vertex shapes do not establish a unique rewrite history. The four-edge original remains intact.

These labels are synthetic, not actual observed audit events. No owner-issued Farkas source or analytic S,A,R,C,G map is established.

Next test REPEATED REDUCTION: after two reductions produce an empty derived view, it must still retain a chain of both reduction records and original path digest; it must not masquerade as the original zero-length identity occurrence.
