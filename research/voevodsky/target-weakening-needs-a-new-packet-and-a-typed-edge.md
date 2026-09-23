# Target weakening needs a new packet and a typed edge

A unit-square proof of x<=1 uses x-upper multiplier 1 and surplus 0. A typed target-BOUND-WEAKENING creates a NEW x<=2 packet with the SAME multiplier, surplus 1 and a distinct FICTIONAL occurrence ID. Fresh `check_typed_target_weakening.py` checks both exact Farkas equations; it refuses to reuse the original occurrence ID, change the normal, decrease the bound, or retain stale surplus. This is NOT a same-target comparison edge; it is a separately typed cross-target mathematical transformation.

These IDs are fixture labels, not observed events. Exact local weakening does not confer authority to issue new source rows or publish a historical derivation. Analytic S,A,R,C,G roles remain deferred.

Next test TWO-STEP bound weakening x<=1 -> x<=2 -> x<=3 against direct x<=1 -> x<=3: both final math packets coincide, yet intermediate occurrence and two-edge path remain different from a direct one-edge derivation. Require path-event identity, not merely endpoint content equality.
