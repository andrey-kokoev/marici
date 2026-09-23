# Three independent swap routes have one endpoint but distinct certificates

In a source-rooted square event DAG, Z precedes three mutually independent branch events W,V,U, and T depends on all three. From `(Z,W,V,U,T)`, adjacent swaps at positions (1,2,1) and (2,1,2) both reach `(Z,U,V,W,T)`. Each swap is valid under the shared predecessor and frozen manifest; swapping Z with W is refused. Fresh `check_three_branch_swap_braid.py` checks both endpoint traces and records the individual event pairs and source/target trace digests. Their swap-certificate SEQUENCES differ, although endpoints match.

The braid-shaped endpoint equality suggests a possible higher coherence cell BETWEEN the two swap paths. It is not itself such a cell and does not equate the recorded swap histories. A declared trace-equivalence quotient may choose to identify them, but must carry pairwise independence, manifest and chain-compatible trace digests before doing so. No recorded external execution or row-owner grant follows from a synthetic proof-event DAG.

Next test a hostile hidden dependency that is NOT a row-derivation prerequisite but is a side-effect/read-write edge. Show that a row-DAG-only independence test would allow an unsafe swap and that a typed effect-conflict dependency rejects it. Analytic S,A,R,C,G remains deferred.
