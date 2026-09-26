# Constructor establishment and a linear normalization bound

This integrates the constructor obligation with a sharper termination calculation. It is a written proof argument for the restricted net, conditional on the previously stated universal structural closure lemma; no claim of machine-checked full closure is made.

## Constructor establishment

For finite w of length n and nonnegative i,j, `Twin` builds disjoint finite chains: one original bit word ending in NIL, and two K budgets ending in NIL. COPY.p meets the original head. Each COPY auxiliary meets its channel's Q_B.a; Q_B.p meets its budget head; Q_B.r meets its distinct OUT. All live ports are paired exactly once. The assembled graph is a tree: joining three disjoint chains through COPY and the two queries cannot introduce a cycle. Deleting COPY exposes exactly its original source chain and two disjoint query/budget/OUT branches, each independently rooted. Every phase, source and copied-budget condition of I therefore holds. The internal COPIED tag on initial budgets denotes non-original data, not literal duplication.

The allocator starts at zero; each chain node is created using fresh, and fixed OUT/COPY/Q names do not collide with underscore-numbered allocations. Thus the high-water execution premise holds at construction. Initial live query interpretations are M(w,i), M(w,j).

## A single natural-number potential

Let O count original B/N nodes and C count non-original B/N/K nodes. Define P=3O+C. COPY--B or COPY--N removes one original data node and creates exactly two non-original data nodes, hence delta P=-3+2=-1. Every other admitted rule consumes exactly one non-original B/N/K head and creates no such data nodes, hence delta P=-1. Query, COPY, E, BOOL and OUT agent counts are deliberately not part of P.

This replaces the lexicographic termination argument by a unit-decreasing natural potential. Initially O=n+1 and C=i+j+2, so P0=3n+i+j+5. If structural closure ensures that every admitted reduction has the stated provenance effect, any reduction sequence has at most P0 steps. If progress and closure ensure that maximal sequences end in exactly two BOOL--OUT pairs, then O=C=0 there and every complete execution takes EXACTLY 3n+i+j+5 rewrites, irrespective of schedule or bit values. Garbage collection is essential: a Boolean may be available earlier, but the bound counts full normalization including erasers.

This is not an asymptotic Python runtime bound: graph scans, copying, recursive encodings and instrumentation add overhead. It is a precise count of net rewrite steps. It is also not valid if a schedule stops early or takes actions other than admitted rewrites.

## Remaining gate and next experiment

The potential calculation is universal arithmetic over the audited rule effects. The constructor argument establishes the initial premises for all finite valid inputs. The structural closure proof still needs final integrated review to promote the complete normalization theorem. Next instrument P on every executable edge and test the exact total-step formula across multiple schedules, including long budgets that force E--K. This supplies an independent consistency check and a useful sharp complexity result without confusing tests with the closure proof.
