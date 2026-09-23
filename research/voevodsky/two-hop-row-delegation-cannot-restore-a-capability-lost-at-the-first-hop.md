# Two-hop row delegation cannot restore a capability lost at the first hop

In a FICTIONAL chain, a root grant has BOTH row-origin and proof-use actions. The first edge grants the delegate ONLY row-origin. The second delegate then requests proof-use. The root's broader scope does not restore an action already removed from the running intersection: fresh `check_two_hop_capability_intersection.py` rejects the second edge as `INTERMEDIATE_CAPABILITY_ESCALATION`. A legitimate origin-only second edge yields only the origin action in this TEST-ONLY model. The checker also takes minimum expiry across hops and refuses a broken principal/manifest chain.

Each grant must be constrained by every intermediate action set, generation and time bound, not merely the root and final edge. This calculation is a structural prerequisite, NOT proof that any fictional edge was signed or externally admitted. The actual Farkas owner/event remain unassigned and no publication authority is present.

Next test a DELEGATION DIAMOND: two distinct chains from the same hypothetical root to the same final participant, one origin-only and one use-only. Their permissions may be taken as a union ONLY if each chain independently passes its own issuer/event/scope/freshness verification; their proofs of authority cannot be spliced across paths. Analytic S,A,R,C,G correspondence remains deferred.
