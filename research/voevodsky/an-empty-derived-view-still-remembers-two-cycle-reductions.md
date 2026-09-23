# An empty derived view still remembers two cycle reductions

Fresh `check_repeated_cycle_reduction_lineage.py` starts with four synthetic edge occurrences A->B->A->B->A. Two successive closed-pair reductions yield an EMPTY remaining edge tuple, but the derived view retains the four-edge origin digest and two ordered reduction records, each pinning its parent path and removed IDs/digest. It is unequal to an original zero-length A identity with empty origin and no reduction lineage. Empty current math/path shape cannot erase the original event-sequence hypothesis.

All occurrences are fictional. No source issuer or analytic S,A,R,C,G map is established.

The bounded cycle-versus-identity branch is resolved: nonempty zero-net cycles, nondestructive shortening, overlapping choices and repeated reduction lineage. A new successor should test a DIGEST DOMAIN SEPARATION pitfall: hashing an empty edge tuple identically for original identity and reduced empty view is unsafe unless the commitment includes kind, origin and lineage.
