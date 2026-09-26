# Row permutation transports weights but not source history

Fresh `check_row_permutation_transport.py` reorders the unit-square rows by old-slot sequence (2,0,3,1). Transporting x-upper-only multiplier weights by the SAME permutation preserves the exact implied normal/bound x<=1. Reusing the OLD weight tuple without transport produces a different implied normal/bound. The ordered row manifest and full packet commitments differ despite mathematical equivalence. An explicit permutation witness records old/new digests and slot map, but its authority is NONE.

A row permutation can transport local mathematics; it cannot assert the reordered source was owner-issued or that the original proof occurrence happened under new slot IDs. Analytic S,A,R,C,G remains deferred.

Next test a FALSE PERMUTATION WITNESS that duplicates one row index and omits another: even when duplicate rows make the final math coincide, reject non-bijective slot maps before proof transport.
