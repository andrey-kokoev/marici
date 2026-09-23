# Rebasing a proof replacement requires new packet and edge identities

On the combined hypothetical x-upper/y-upper bound 7/4 source, the old Q packet and old one-row S packet for target x<=3 both have stale surplus/bounds. Fresh `check_explicit_proof_replacement.py` replaces each with a NEW packet ID using x-upper multiplier 1 and surplus 5/4, checks their exact target equations, and issues a NEW comparison edge whose endpoint IDs refer to those packets. Attempting to carry over the old edge fails `EDGE_ENDPOINT_ID_STALE`.

Although the new comparison may be a trivial identity between numerically identical packets, it is not the old historical Q/S derivation or old edge. Proof catalogue replacement must bind exact new manifest digest, packet IDs, surplus and dependency edges as one candidate transaction. All work is local mathematics: no real primitive-row source was changed and no publisher authorization was granted.

The incremental source-edit branch is complete at conservative row invalidation, atomic rollback/CAS and explicit proof replacement. A nonredundant successor should test CONTENT-ADDRESSABLE proof packet identifiers versus occurrence IDs: two identical new packets may share a math digest but must not be conflated as two recorded proof events. Analytic S,A,R,C,G role map deferred.
