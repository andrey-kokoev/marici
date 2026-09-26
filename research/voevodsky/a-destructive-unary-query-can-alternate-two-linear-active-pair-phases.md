# A destructive unary query can alternate two linear active-pair phases

A QUERY count phase meets a UNIT at principal ports; the successor budget-phase agent reconnects to the budget head and carries the count tail on its auxiliary port. It then meets a KUNIT budget agent; the successor count-phase agent reconnects to the saved count tail and carries the budget tail. Fresh `check_destructive_unary_query_phases.py` verifies that EACH interior active-pair rewrite preserves both external wire endpoints exactly once. For 1,089 (count,k) pairs 0..32, an abstract alternating run returns `count>=k` after `2*min(count,k)` interior rewrites.

This contract is DESTRUCTIVE: one count UNIT and one budget KUNIT are consumed per pair. The checker does not provide NIL interaction, zero-threshold termination, or erasure of remaining tails; it does not claim a complete interaction net or reusable readout. Port-linearity of individual interior rewrites does not establish global closure.

Next implement NIL branch rules and explicit eraser propagation for leftover count/budget lists, checking complete incidence conservation and a single Boolean output for all count/k cases including zero. Only then compare costs with a persistent query design.
