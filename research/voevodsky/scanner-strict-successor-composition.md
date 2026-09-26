# Recurrent scanner as a strict predecessor

Fresh `check_scanner_successor.py` attaches a GM query gate to scanner support/acknowledgment interfaces at construction. The scanner's OUTCOME root stays separate. Runtime release is exclusively GM--DONE, not a host call after a scan.

## Contextual completion argument

Cut GM.s and GM.p to passive RET/ACK leaves. This yields the isolated scanner plus dormant successor resources; the successor's budget has no consumer. Initially GM.p faces FUEL.c; the unique external completion obligation transfers through START/TEST/CHOOSE/NEXT or terminal cleanup phases. Recursive NEXT allocates a new FUEL while keeping exactly those same external continuation peers. No rule examines the two peers' shared agent identity, so each recurrence and cleanup step commutes with the cut.

The scanner's only public completion emitter is SEAL--TOKEN after FINISH has consumed terminal cleanup DONE. Intermediate query, insertion, preparation and erasure tokens face internal latches and cannot activate GM. Hence the scanner phase theorem implies complete returned support and no cursor/fuel/control work at GM eligibility. This remains true when the scanner has already published FOUND or EXHAUSTED: that isolated result pair is not the gate's principal input.

GM release then constructs the ordinary acknowledged membership operation on the returned word. Its correctness and cleanup theorem give final ACK, unchanged support and the correct successor Boolean. The scanner outcome pair remains unchanged through every successor rewrite. The combined cost is scanner cost +1+2n_final+j+3. Final components are precisely RET/word, OUTCOME/tag, successor OUT/Boolean and ACK/DONE; total nodes n_final+8.

## Executable evidence

315 fixtures20541 rewrites pass with words n<=2, cursor0..2, fuel0..4 and successor index0..2, using seeded individual scheduling. Every fixture observes the early outcome with EA still enabled and successor blocked, verifies scanner work absent at gate eligibility, checks combined exact cost and partitions all final agents into the four specified rooted components. This does not exhaust scheduler choices or formally verify Python.

Observation note: in the composed object, inherited `observe().complete` now denotes completion of the whole scanner-plus-successor net, not completion of the scanner alone. Its outcome remains the scanner result; the successor Boolean is a separate root. No intermediate support exposure is added.

## Next critical-path milestone

Composition is now demonstrated for a genuine runtime recurrence. The next useful step is a unified typed finite-program compiler with `scan(cursor,fuel)` alongside member/add/union/ifadd, preserving an ordered heterogeneous observation list (Boolean versus FOUND/EXHAUSTED). Use a fixed release gate that instantiates FUEL and consumes its input DONE. Then induction can reuse the established scanner postcondition; it should not require a new arbitrary-loop claim. Explicitly distinguish snapshot type, pending state and whole-program ACK rather than coercing outcome tags to booleans.
