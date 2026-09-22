# Coherent witness sets compose without selecting an origin

## Question and independent input

Nima's source-bound runtime packet distinguishes existential local membership from a coherent live origin witness. Test a third representation: retain the complete current set of compatible behavioral witnesses when the actual origin is unknown.

The owning independent relational/live-witness verifier is freshly replayed. Runtime computation then uses only its 70 behavioral rows, local view tuples, origin bits and eighteen-label accepted/rejected transitions. It consults no original concrete-state identifiers or source words. Packet indices in the checker are addresses of retained behavioral rows.

## Exact construction

For a current witness set K, observed label/admission stratum R and next observed view v, update by

    K' = R[K] intersect fiber(v).

The input K retains all prior evidence. It is never reset to the full fiber merely because the current view is compatible with that fiber.

Transpose of R supplies backward compatibility queries using the same construction. This is retrospective constraint propagation, not a reverse execution constructor.

Explore all updates from each of the 61 admitted local-view fibers, in both logical directions. The resulting family has 80 states:

- 70 singleton behavioral witnesses;
- nine unresolved two-witness sets;
- one empty set for an inconsistent observed history.

These are all subsets of one observed-view fiber. A bound on this finite representation does not establish a universal provenance-storage bound.

## Composition and counterexample repair

Relational image satisfies

    S[R[K]] = (S composed with R)[K].

This equality keeps the intermediate behavioral witness shared. The checker verifies all 1,296 ordered stratum pairs on all 80 knowledge states: 103,680 exact identities. It also verifies 5,688 forward/backward updates and 2,880 view-filter partition identities. Intersections with observed-view fibers are diagonal relations and participate in the same relational composition theorem.

At each of the nine ambiguous tuples, accepted audit-origin(0) reduces the witness set to its origin-zero member. A subsequent accepted audit-origin(1) produces the empty set. All nine false projected paths are rejected. Resetting the intermediate set to the full fiber reproduces the original failure.

Known sound initialization plus exact updates proves by induction that K contains exactly the behavioral endpoints of coherent paths matching the entire observed execution. A singleton identifies a behavioral state; a doubleton preserves unresolved possibilities. Neither representation reconstructs a unique concrete past.

## Structural synthesis

A coherent history can be represented by a transported set of possible witnesses. Unique selection is optional; persistence of the relation between successive witnesses is essential. Projection at each step followed by a fresh existential choice destroys that persistence.

This supplies a precise history-possibility propagation rule: the retained possibility set is the residual of the whole observed history. The rule composes in either logical orientation because it acts on the source-bound witness relations before forgetting them.

The construction assumes a sound initial possibility set, truthful observed event outcomes and the owning protocol bindings. It does not authenticate an observed audit outcome, prove storage completeness, or turn an unknown origin into authority to execute one of its mutually exclusive audits. The empty state is a consistency failure, not a physical-source infeasibility verdict.

## Reproduction

    python research/voevodsky/checkers/check_coherent_witness_set_transport.py

Artifacts:

- `results/coherent-witness-set-transport-contract.json`
- `results/coherent-witness-set-transport.json`
