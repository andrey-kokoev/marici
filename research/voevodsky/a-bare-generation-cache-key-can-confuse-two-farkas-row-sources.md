# A bare generation cache key can confuse two Farkas row sources

Two independent row-source branches both labelled generation 1 use identical multiplier packet (0,1,0,0), but one x-upper row is x<=1 and the other is x<=2. Their mathematical outputs differ while a cache key of ONLY generation and packet digest collides. Fresh `check_cache_key_source_collision.py` shows an unsafe cache returns the first branch's bound for the second; adding the COMPLETE ordered-row manifest digest separates keys. The independently rerun `check_proof_math_cache_vs_occurrences.py` also confirms that a safe cache hit reuses arithmetic without conflating fictional occurrence IDs.

This fixes local arithmetic lookup, not source authenticity. A manifest digest under a local encoding plus generation prevents this specific cross-source cache collision; it does not prove which owner issued those rows or which proof occurrence happened. The Farkas row issuer remains unknown and analytic S,A,R,C,G mapping deferred.

Next test a malicious PACKET KEY that omits surplus or target: two packets with identical multipliers and source rows can have different exact target bounds. Separate raw row-linear evaluation reuse from full certificate-result reuse, and refuse cache promotion across target scope.
