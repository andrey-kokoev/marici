# Zero signed delta after compensating edits can hide invalid proof packets

Change BOTH x-upper and y-upper square bounds from 1 to 2. The old signed comparison k=Q-P has coefficients (-1,-1,1,1). Its bound change cancels between the two edited upper rows, so k STILL has zero normal and bound. But each individual old P and Q packet now has implied bound 4, not the original target bound 2; restoring target 2 with their fixed coefficients would require surplus -2, forbidden by Farkas nonnegativity. Fresh `check_compensating_bound_edits.py` checks all these rational equations. The target x<=2 nevertheless remains true, now directly from edited x-upper row.

A checker that tests only final signed comparison closure would mistakenly accept a path whose endpoint proof packets are invalid for the requested target. Incremental verification must check every affected endpoint/segment packet's normal, bound, surplus and row-manifest generation, not merely that signed differences telescope. Source-owner authorization does not move to the new manifest.

Next test a MIXED dependency index covering proof packets AND signed comparison edges: editing x-upper touches both P and Q even though k's net sensitivity to a coupled edit cancels; calculate per-edit affected sets before algebraic cancellation. Analytic S,A,R,C,G correspondence remains deferred.
