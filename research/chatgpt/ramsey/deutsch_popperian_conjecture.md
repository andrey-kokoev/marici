# Deutsch–Popperian Conjecture: coupled header paths

This is our conjecture. The name describes the test method. It does not attribute the conjecture to David Deutsch or Karl Popper.

**Conjecture.** A single rule for transport between the row and column headers of a two-color pair matrix determines the largest order at which the red and blue paths can coexist without a forbidden closure. For targets (l,k), this order is R(l,k)-1. The rule uses the same transport law for all targets. It does not take a Ramsey number as input.

A header is a vertex in a row role or a column role, not an additional Ramsey vertex. Every off-diagonal pair has one color. The diagonal is unused. A candidate law must specify the state, the allowed continuations at a header, and the closure test before comparison with data. Relabeling vertices must relabel the paths. Exchanging colors and targets together must preserve the verdict. A scan for the forbidden cliques followed by a path description is not a transport explanation.

**First tests.** For targets (3,3), admit the red five-cycle with its blue complement. Reject the red seven-cycle with its blue complement, despite its complete red header circuit: vertices 0,2,4 in red cycle order form a blue triangle. Derive failure at six for every coloring, not just one extension of the five-cycle. Passing these tests is necessary but not sufficient. Freeze the law and test (3,4): admit an eight-vertex witness and derive failure at nine without changing the law.

No transport law with these properties has been established here. A failed prediction refutes the specified law, not every possible transport explanation.
