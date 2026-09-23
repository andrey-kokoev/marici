# Proof-math cache can reuse arithmetic without merging proof occurrences

An in-memory arithmetic cache keyed by complete ordered row digest, local source generation and packet digest computes an x-upper one-row result once, then reuses it for a second FICTIONAL proof occurrence on the same version. Fresh `check_proof_math_cache_vs_occurrences.py` retains two distinct occurrence IDs and predecessor IDs despite the cache hit. If the x-upper row changes from x<=1 to x<=2, the identical multiplier packet has a different bound and the cache misses; even with unchanged row bytes a new generation misses under this conservative source-version key. Four occurrence records coexist with three cache entries.

Math-cache reuse is not historical deduplication, source-owner authorization or publication. Occurrence IDs and dependencies must remain independent audit data. The real Farkas row issuer and analytic S,A,R,C,G role mapping remain unresolved.

Next test a CACHE-KEY OMISSION attack: remove source-row digest from the key while retaining generation number, then two independent source branches both labelled generation 1 can yield different math under one cache entry. Require globally unambiguous source identity plus manifest and generation, not a bare version counter.
