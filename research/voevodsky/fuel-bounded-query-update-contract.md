# Fuel-bounded runtime query/update repetition

Status: semantic and ownership contract, not an implemented loop or a complete interaction-rule table. The next implementation prerequisite is a retained unary-cursor duplicator with completion acknowledgment. No new termination claim for unrestricted programs is made.

## Why not repeat the same query and insertion?

Repeatedly testing a fixed index i and inserting at a fixed index j is a poor expressivity milestone: if i=j it succeeds by the second query, otherwise a false query remains false until exhaustion. Instead use a runtime cursor which advances after each failed test. This supports arbitrarily many iterations with a fixed control signature and finite runtime fuel, without compiling one instruction per iteration.

## Precise sequential semantics

Inputs: complete finite support word w, unary starting cursor c, unary fuel F. One fuel unit permits one query, including its possible failed-query update. There is one final outcome root, not a preallocated OUT per potential iteration.

At an iteration boundary:

1. If fuel is zero, return EXHAUSTED and the current word. Perform no query, even if the current cursor would test true.
2. Otherwise consume one fuel K and test member(c) on the current word.
3. If true, return FOUND and the unchanged current word; erase unused fuel and cursor resources before final ACK.
4. If false, perform add(c), wait for its full completion, increment c by one and repeat with the remaining fuel.

There is no final extra query after the last permitted update. A false test on the last unit still inserts its bit before returning EXHAUSTED. FOUND/EXHAUSTED are distinct terminal tags, not Boolean aliases: EXHAUSTED certifies a fuel boundary, not nonmembership everywhere.

Examples: w=(0,0,1), c=0, F=2 yields EXHAUSTED with (1,1,1); F=3 yields FOUND with (1,1,1). F=0 always yields EXHAUSTED and unchanged w. Empty w, c=0, F=3 yields EXHAUSTED with (1,1,1). These are semantic examples, not execution test results.

## Runtime representation and linear ownership

Use a fixed-size controller family plus data chains for support, cursor and fuel. Program compilation must not allocate F query gates or a list of F instruction descriptions. Dynamic rewrites recreate the boundary controller after each failed insertion. A persistent graph backedge is not itself required: recurrence through a fixed set of rewrite rules suffices.

A query consumes its index budget, but a failed query must still supply that same index to insertion and retain its successor for the next iteration. A Python integer cached in a controller payload, a host loop invoking start/insert, or sharing one cursor chain across two ports would evade this obligation.

Required linear preparation: from cursor K^c N produce three disjoint completed chains of the same length: query budget, candidate insertion budget and retained cursor. This can be built by two sequential acknowledged binary cursor duplications. The existing support COPY handles binary word cells, not automatically K; its current rules must not be assumed to duplicate unary budgets. Increment of the retained cursor is one local K allocation after the false-branch insertion completes.

## Boundary phases and completion obligations

* FUEL owns the complete word, cursor and fuel, plus external RET/outcome/ACK. Its principal consumes K or N; only the K case enters preparation.
* PREP owns cursor copying and releases the query only when all three cursor chains are complete. No query or insertion budget may be used by a second consumer.
* QUERY owns the acknowledging membership operation and holds both unused cursor copies and residual fuel passively. A Boolean alone is insufficient to select the next phase; wait for query DONE as in WAIT/PICK.
* TRUE cleanup erases candidate insertion cursor, retained cursor and residual fuel. Support is returned unchanged. A finite local join consumes all cleanup acknowledgments before final DONE.
* FALSE releases exactly one insertion with the candidate budget. Retained cursor and fuel remain passive. Its DONE enables cursor increment and reinstates FUEL; no next query overlaps the insertion.
* ZERO cleanup erases the retained cursor. It returns the complete word and emits EXHAUSTED; final DONE waits for cursor cleanup.

FOUND/EXHAUSTED may be published before the terminal cleanup ends, but public word access is gated by final ACK, as in the existing observation contract. A simpler implementation may delay outcome publication until that cleanup finishes. Pick and document one convention before coding.

## Termination and final accounting argument to discharge

At each completed FUEL boundary the remaining unary fuel length strictly decreases on every nonterminal cycle. All work between boundaries must terminate: finite cursor duplication, acknowledged membership, insertion, increment, or finite cleanup joins. Therefore at most F queries and F insertions occur; cursor length is at most c+F and support length at most max(|w|,c+F). This is a compositional proof plan conditional on the new local preparation and controller rules; it is not a proof of code that does not yet exist.

Final live components must be exactly RET plus support/NIL, OUTCOME plus one terminal tag, and ACK plus DONE. Every unused copy, remaining fuel cell, intermediate Boolean and control agent must be consumed. No per-iteration history is retained unless a separate linear output-log interface is designed.

## Selected next prerequisite

Implement and prove a completed unary-cursor duplicator: input K^c N, two independent outputs of length c and one DONE only after both tails are complete. Specify fixed arities, boundary slot use and a local terminal acknowledgment; test c=0, nonzero cursors and passive cyclic continuation contexts. Only then implement the fuel controller. This ordering addresses the missing resource operation rather than disguising compile-time unrolling as a runtime loop.
