# Duplicate inequalities do not collapse their row-slot proof identities

Fresh `check_duplicate_row_packet_slots.py` has two distinct synthetic row occurrences, each inequality x<=1. Multiplier packets (1,0) and (0,1) yield the SAME normal/bound mathematics, but bind different ordered row slots and have different packet commitments. Renaming the used row's occurrence ID changes the provenance-aware packet commitment even with identical weights and inequality text.

These are synthetic IDs, not an owner-issued source or actual events. Analytic S,A,R,C,G mapping remains deferred.

The bounded source-row encoding branch now covers exact rational grammar, order, row IDs and duplicate slots. A separate successor should test a ROW-PERMUTATION TRANSPORT: permuting ordered rows and inverse-permuting packet multipliers preserves math but must issue a new packet identity and explicit transport witness rather than treating the original ordered commitment as unchanged.
