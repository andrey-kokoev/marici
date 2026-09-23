# Two delegation routes can union actions only after independent validation

A FICTIONAL root with origin and proof-use actions delegates origin through A->C and proof use through B->C. Each full path has its own running action intersection, row manifest, principal continuity and live epoch. Fresh `check_delegation_diamond.py` checks that A yields origin only and B yields proof use only; a TEST-ONLY union contains both ONLY if both paths independently pass. Splicing A's first edge with B's last edge is `BROKEN_PATH`. A stale B edge is `STALE_PATH`, so only A's origin action remains structurally available.

This local test does not validate signatures or create real capabilities. The actual Farkas request still has no designated issuer, authenticated parent or signed intermediary events; therefore the true authorization union is empty. Matching recipient names are insufficient to merge evidence from different grant paths, and graph admission cannot serve as an issuer trust root.

Next test a SHARED REVOCATION at root after both hypothetical paths are checked. Even individually intact edge records must lose authority at use time if their common root is revoked; require a common atomic epoch rather than independently fresh-looking stale route snapshots. Analytic S,A,R,C,G correspondence deferred.
