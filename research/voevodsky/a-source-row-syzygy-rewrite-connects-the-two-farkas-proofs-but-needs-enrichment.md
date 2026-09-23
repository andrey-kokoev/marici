# A source-row syzygy rewrite connects the two Farkas proofs, but needs enrichment

The direct/staged nonfunctoriality example has a concrete candidate comparison rewrite. On primitive source rows `-x<=0` and `x<=1`, a Farkas proof of `x<=T` is `(a,b;c)` with b-a=1, b+c=T and a,b,c>=0. The normal relation `(-1,1)·(1,1)=0` permits

    (a,b;c) -> (a+c,b+c;0).

The extra source-bound contribution is exactly c, compensating the removed surplus. Thus the staged proof `(1,2;1)` rewrites to the directly selected `(2,3;0)` for T=3, including the reference shift to 1/2. Fresh exact-rational `check_farkas_proof_comparison_rewrite.py` checks 151 bounded rational proofs and finds the same zero-surplus normal form `(T-1,T;0)` for this fixed interval family. The all-at-once rewrite terminates in one step; partial rational rewrites are not claimed terminating. If the primitive upper bound becomes 2, this rewrite is no longer sound with the same c-compensation. The primitive ROW BOUNDS, not only their normals, must support the comparison.

This changes the diagnosis: the two proofs are not irreconcilable mathematically. There is a source-derived directed rewrite when the original rows and bound are retained. But the existing Farkas category declares 1-arrows and their composition, not a 2-cell identifying them. The staged intermediate `x<=2` by itself lacks access to the two primitive rows needed for this rewrite. An enriched proof category would have to retain the source-row derivation and install this rewrite with its type, support DAG and naturality/coherence laws. Equality of public inclusion is not its authority; a source-rooted DAG can support an already constructed cell, not fabricate it.

The finite record/continuation polarity now predicts exactly why the extra retention matters: public-answer controls identify the two paths; proof-replay controls distinguish them; a comparison control exists only after specifying this source-rooted rewrite and what it promises (directed normalization versus invertible proof equivalence). No analytic S,A,R,C,G identification follows.
