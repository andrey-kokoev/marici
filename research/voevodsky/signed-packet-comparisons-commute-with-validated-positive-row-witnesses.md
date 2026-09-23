# Signed packet comparisons commute with validated positive row witnesses

For square source packets A,B,C from the partial-selector branch, let a positive monomial row witness reorder source rows as (3,0,2,1) with scales (2,3,1/2,4). Each packet multiplier transports by dividing by its new row's scale and its surplus remains unchanged. The comparison square holds exactly: `transport(Y-X)=transport(Y)-transport(X)` for A->B, B->C and A->C, even when the delta's multipliers or surplus are signed. Fresh `check_comparison_row_witness_square.py` checks all three.

The witness is validated AGAINST BOTH ordered row manifests and their digests before applying it. A stale destination digest, negative factor, or wrong permutation is refused. In particular the two manifests' different hashes are expected; this explicit row isomorphism is the bridge between mathematical proof coordinates. It is NOT a bridge between issuer grants, publication events, or actual proof execution histories.

Next test a compositional diamond involving two independent row witnesses and one signed selector comparison, retaining BOTH witness IDs and row manifests: endpoint signed delta may agree despite different witness paths, so identify the minimal transport-path provenance needed for replay. Analytic S,A,R,C,G assignment remains deferred.
