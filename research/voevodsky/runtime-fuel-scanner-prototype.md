# Runtime fuel scanner prototype

Implemented `fuel_scanner.py`: FUEL consumes one runtime unary fuel cell, launches DC/PREP/READY cursor preparation, then START releases an acknowledged query. TEST waits for query DONE before CHOOSE inspects its Boolean. False launches insertion; NEXT waits for insertion DONE, increments the retained cursor by a fresh K and recreates FUEL. This is runtime recurrence with fixed signatures, not compile-time unrolling or host index reuse.

True returns support and FOUND, then serially erases insertion budget, retained cursor and unused fuel through CLEAN/DRAIN/FINISH. Zero fuel returns support and EXHAUSTED and erases the cursor. Terminal outcome publication is early; final ACK waits for all cleanup. FINISH/SEAL remove a private TOKEN and emit final DONE. This extra token is an implementation choice, not an externally visible result.

Fresh headless test passes105 fixtures5720 rewrites with words n<=2, cursor0..2 and fuel0..4, covering repeated false updates and both outcomes. Each replacement's external/fresh port use is checked. Query counts match fuel-first semantics, final support/outcome match the oracle, and exact three rooted components account for all live agents. Bounded random schedules are not formal verification.

Next close the runtime phase invariant and cost/termination argument against these actual templates, especially TEST's completion barrier, NEXT's strict update boundary and true-path serial cleanup. Add pending-aware outcome observation and a delayed-cleanup prefix witness. Do not claim arbitrary loops or a completed universal proof from the present finite tests.
