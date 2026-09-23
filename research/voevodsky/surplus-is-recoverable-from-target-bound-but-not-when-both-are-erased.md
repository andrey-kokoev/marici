# Surplus is recoverable from target bound but not when both are erased

On the frozen square rows, the proof multiplier p=(0,1,0,1) has normal (1,1) and source-bound sum 2. If exact target bound 3 is retained, its Farkas surplus is uniquely `3-2=1`; omitting the separate surplus field need not lose information. Fresh `check_surplus_bound_recovery.py` verifies this and rejects target bound 1 because it would require negative surplus.

If BOTH target bound and surplus are erased, the identical retained row manifest, multipliers and normal admit distinct valid completions (bound,surplus)=(2,0),(3,1),(4,2), and indeed arbitrarily many larger rational bounds. No commitment-chain datum in this local example constrains which mathematical target was meant. Thus a verifier refusing a missing explicit surplus field is a FORMAT requirement; genuine underdetermination here requires loss of both coupled quantities. This distinction prevents an exaggerated retention-minimality claim.

Next test analogous redundancy between the row MANIFEST and row labels: if the digest is erased but full ordered row coefficients remain, it can be recomputed; if both ordered rows and digest are erased, the same multiplier tuple can prove different normals/bounds under different manifests. Keep source issuer grant and analytic S,A,R,C,G mapping separate.
