# A zero signed comparison does not repair invalid endpoint proofs

Take two identical x-upper proof packets for x<=0 with multiplier 1 and surplus -1. Their signed multiplier difference and surplus difference are BOTH zero, and their exact target equations match. Yet each packet is invalid because surplus is negative; `check_invalid_endpoint_zero_delta.py` rejects the comparison at its endpoint gate. Two identical valid x<=2 packets with surplus +1 yield the same zero differences and pass local comparison. Hence zero deltas alone do not certify endpoints, proof validity or historical identity.

Validation order: bind current row manifest, validate each endpoint's exact normal/bound and all nonnegative multipliers/surplus, check the common target, and only then form the signed difference. Even a passing local comparison is not observed source history or publication authority. Analytic S,A,R,C,G remains deferred.

Next test a NONZERO signed delta between two individually valid packets but with distinct targets. A signed vector is algebraically definable, but a comparison edge labelled same-target must reject mismatch rather than quietly reinterpret as a proof transformation.
