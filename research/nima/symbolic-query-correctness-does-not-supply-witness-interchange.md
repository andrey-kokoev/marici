# Symbolic query correctness does not supply witness interchange

## Result

The running symbolic tail interface now has separate tests for persistent refinement, observer saturation and the identity of returned source witnesses. All use the owning admitted normalized tail faces, not a new tagged-state fixture.

The distinctions matter operationally: a correct observable answer and a valid source certificate do not establish that arbitrary routes through certificates transport the same source witness.

## 1. Persistent refinement is order-independent

Freeze the three observable frames

    U<=50, U>=25, V<=U/2.

Run all six permutations, four linear objectives, and m=2,3,16,64,1024. All 120 queries have independently replayed primal/dual certificates. In each of the 20 comparison groups, the final objective value, observable optimizer and the engine's chosen lift agree across all permutations.

Refinement states are immutable; earlier snapshots retain their previous frames. This is ordinary conjunction on one fixed source relation. It does not alternately reopen fibers of different observers.

The general answer-level order independence follows from conjunction and the engine's exact query certificates. Equality of selected witnesses here is a result about this fixed deterministic selector and workload, not a theorem about all possible witness constructions.

## 2. The same source has a noncommuting saturation diamond

At m=3, the slopes are 1,1/128,1/16384. Let a=1/16384 and take admitted source points

    start  = (0,a,0),
    middle = (a,0,0),
    end    = (0,0,1).

The first pair agrees in U; the second agrees in V. The reverse-order middle would require

    U=1, V=1/128^3.

But every source point satisfies

    V >= U/128^2.

The required point violates this nonnegative source inequality. The engine's membership oracle produces an exact separating support certificate for it.

Thus the successful refinement-order tests coexist with failed saturation commutation on the same analytical source. Intersecting evidence and forgetting through an observer are different operations.

## 3. Two valid lift routes disagree on an atom audit

Use the source endpoints

    t_left=(0,0,0), t_right=(100,102,0).

At the midpoint of their observable images, compare:

- the source lift returned directly by the engine's greedy-profile membership constructor;
- the midpoint of the two displayed source lifts, namely (50,51,0).

Both are admitted box points. Both have exactly the same U and V. They are nevertheless different: the direct engine lift has strictly positive third-atom mass, whereas the interpolated lift has third-atom mass zero.

The atom-level audit t_2<=0, using zero-based indexing, separates them. That audit is outside the declared two-observable interface language. It cannot be answered by treating an arbitrary returned feasibility witness as the actual source.

This shows that the engine's chosen section is not affine. It does not assert that these two constructions are a braid, that no other transport can be coherent, or that their witness spaces lack an independently specified equivalence. In the convex source their segment is admitted, but identifying its endpoints would still have to respect whichever audits the identity contract promises.

## 4. Consequence for the implementation

The interface currently promises:

- exact source-admitted observable feasibility;
- persistent conjunction of accepted frames;
- verified extrema or inconsistency certificates;
- an admitted source witness for each positive answer.

It does not promise actual-source selection, proof-relevant interchange of all witness choices, or coherence of unspecified comparison maps. Any such extension needs a separately declared transport and identity contract. In particular, coordinate relabeling must not be used to erase an observable audit difference while leaving the audit semantics fixed.

This keeps the recent saturation and braid results as boundaries of the executable synthesis, rather than silently promoting its endpoint-correct certificates into stronger claims.

## Verification

    python research/nima/checkers/check_symbolic_interface_coherence_levels.py
    python research/nima/checkers/verify_symbolic_interface_coherence_levels.py

The new verifier reuses only the independent certificate checker, not the producer or query engine. It verifies all 120 certificates, closed-form expected optima, the reverse-fiber separator and both unequal source lifts. It passes.

Artifacts:

- `research/nima/results/symbolic-interface-coherence-levels-contract.json`
- `research/nima/results/symbolic-interface-coherence-levels-packet.json.gz`
- `research/nima/results/symbolic-interface-coherence-levels.json`
- `research/nima/results/symbolic-interface-coherence-levels-verification.json`
