# Straight-line pipeline theorem and exact equivalence boundary

## Statement

For a finite bit word and any finite straight-line program compiled by SequencedSet, with operations add(nonnegative unary index), member(nonnegative unary index), and union(finite literal bit word), every maximal sequence of admitted local reductions terminates. Its RET word and ordered membership outputs equal the sequential word semantics. Terminal graphs are unique up to kind/port isomorphism fixing RET and EACH ordered OUT. This is the consolidated written mathematical argument from the linked proofs, not machine-certified Python verification.

## Proof dependencies (not bounded-test extrapolations)

1. `pipeline-producer-contract-closure.md` defines public S_t, private P_t, insertion A_t, budget K_t and literal L_t paths, plus stage cardinalities and global coverage. The compiler establishes these by attaching disjoint operation trees to a single public stream.
2. Its rule table proves simultaneous contract substitution, including UL--N's direct splice. This splice joins different context trees, preserving the forest. Query splits retain exact data/producer coverage through E roots. Stages never gain backward producer dependencies.
3. Every blocked consumer points to an earlier public producer or its same-stage COPY. Minimal (stage,COPY-before-other) therefore supplies an active pair whenever a control remains. With no control, global coverage gives only RET's complete word and BOOL--OUT pairs.
4. Finite-production induction bounds every stage: add by its finite budget, union by its finite literal, COPY by the finitely many data agents supplied from earlier stages, and query/eraser work by its finite budget/copied branch. A finite number of stages therefore admits no infinite reduction. No fairness is needed when counting actual reduction steps.
5. `pipeline-denotational-simulation.md` defines residual virtual words by strictly decreasing producer stage. Rule equations for A, U and M preserve RET and every ordered query observation, even when later stages execute first. Initial observations are exactly the sequential program fold, so terminal observations are correct.
6. A terminal graph has no hidden garbage or controls by global coverage. The final word plus ordered Booleans uniquely determines its observable-rooted graph. All descendants of a compiler output terminate at that same graph, so any two reductions join there. This yields confluence on compiler-reachable states modulo observable-rooted isomorphism. It is not a theorem about arbitrary graphs or arbitrary splice rewrite systems.

## Two equivalences must not be confused

`pipeline_canonical.key(net, proof=True)` preserves allocation-stage labels, compiler operation declarations and OUT-list positions. Use it when quotienting state searches that validate stage contracts. `proof=False` forgets stage metadata but STILL fixes every ordered output position and RET; use that for the terminal uniqueness statement. Neither comparison identifies a TRUE at query 0 with a TRUE at query 1 merely because output kinds match. Serial allocator state is outside these graph equivalences and must separately remain fresh during execution.

Fresh controls demonstrate that the old unlabelled key equated swapped unequal answers, whereas the new key separates them. Renaming allocation IDs preserves both new keys; computing a key no longer mutates net.tags. The corrected 129-fixture grammar search remains 2,742 proof-labelled classes and 4,684 edges, with all contract/denotation checks passing. Earlier broad priority tests remain useful execution evidence but are not substituted for the proof above.

## Assurance and next scope

The written proof now has an explicit observation-preserving equivalence; independent review/formal verification remains open. Runtime invalid inputs, stale allocator counters, arbitrary Python callbacks/resource limits, loops, dynamic branching, completion barriers and concurrent register ownership are outside this statement. Prefix-driven overlap is inside it.

Critical-path reassessment: further elaboration of the same straight-line proof is lower value than auditing the next semantic extension. The next selected proof task is a strict completion barrier contract: identify whether readiness means a complete RET word, a Boolean available, or all private garbage cleared, and prove that any proposed completion token cannot overtake outstanding work. Begin with a counterexample to using only Boolean readiness or the first support head as a completion signal. Do not implement a misleading host callback and call it an internal barrier.
