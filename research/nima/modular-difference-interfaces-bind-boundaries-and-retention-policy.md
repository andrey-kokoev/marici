# Modular difference interfaces bind boundaries and retention policy

## Delivered interface

A separate raw-atom difference-constraint prototype now compiles blocks independently, composes their certified boundary summaries, answers public membership, and distinguishes archive-backed re-exposure from public-only retention.

Independent replay checks ten states, including a contradiction arising only across individually consistent blocks. Modular and monolithic relations agree. Sixteen public membership controls, four compatible fine fillings and four archive-backed re-exposures pass. Seven certificate mutations are rejected.

## Source and structural contract

Node 0 is the fixed zero anchor. Node j+1 represents source atom j with cap 100+2j. An edge u->v of weight w means x_v-x_u<=w.

Each block declares its source nodes, boundary nodes and complete evidence tuple. The compiler adds the owning cap edges. All source atoms must be covered. Every shared node must be a boundary node in every owning block; interiors are disjoint. Exterior edges and public coordinates must lie on the composed boundary. The anchor belongs to every boundary.

These restrictions are checked before compilation. A shared interior is a malformed composition request, not an inconsistent mathematical state. General moment rows and arbitrary linear constraints are not supported by this state language.

## Certified block composition

Each block supplies all-pairs distances and original-edge paths. Its boundary summary contains the distance bound for each distinct ordered boundary pair. Composition identifies nodes by their declared global source indices, retains exterior edges, and closes this boundary graph.

The independent checker does not import the closure algorithm. For every consistent closure it checks:

- each proposed distance has a path of exactly that length;
- all triangle inequalities and zero diagonals;
- every original edge dominates its proposed distance.

Paths prove that original solutions satisfy the summary; triangle closure and domination prove completeness. With disjoint interiors, every compatible boundary assignment extends independently into each block, so replacing blocks by these exact summaries preserves the full public relation.

The public summary is obtained from the composed closure. Monolithic closure is computed separately only as a workload comparison, not as the modular runtime's compilation algorithm.

## Compatible source fillings

For admitted public values y, first extend them to all composed boundary nodes:

    z_v = min_(a public) (y_a + D_interface(a,v)).

For each block extend its boundary assignment similarly using that block's distances. The interface inequalities make both extensions agree with the given values at retained nodes. Original edges are satisfied by the shortest-path inequalities. Shared source nodes receive identical values because they are boundary nodes, not independently chosen hidden interiors.

`LiveState.fill` implements this two-stage construction for archive-backed states. The verifier checks every resulting source cap, fine evidence row, exterior edge and requested public coordinate.

## Negative cycles are mathematical certificates

A local negative cycle proves the entire state inconsistent. A composed negative cycle may instead arise although every block separately has a filling.

The cross-block control has one block implying x_3<=x_1 through hidden node 2, and another implying x_1<=x_3-1 through hidden node 4. Both blocks are individually consistent; their boundary composition is not.

The packet expands every summary edge of the negative cycle into its original block-edge path. The independent verifier checks that the expansion is a closed walk of strictly negative total weight. Summing those original inequalities gives a contradiction without relying on the closure algorithm's status label.

A separate local-cycle case is also tested. No optimizer or external solver is used.

## Continuation policy is part of the statement

Both live-state descriptors and migration certificates bind the expected source context, boundary/public schema and retention policy.

- **archive-backed:** retains the fine block specification. Re-exposure promotes requested raw nodes to block boundaries and recompiles from the same fine constraints. It adds no observed values and does not weaken history.
- **public-only:** retains only the public summary, source/context metadata and origin digest. Attempts to expose a hidden atom or request a fine filling raise `PermissionError`.

The live state is frozen; caller input is copied. The private archive is an implementation resource, not an authenticated external store. This research API's policy guard is not a cryptographic access-control mechanism.

Public membership is available in either mode after accepting the summary's migration certificate. A public-only state cannot recover discarded restrictions merely from its digest. A separately retained archive could support a new explicitly justified transition, but there is no automatic coercion from public-only to archive-backed state.

Producer controls check eight unsupported continuation refusals. Independent replay checks the policy-bound descriptors and all four permitted re-exposure certificates. Altering the policy in a packet and recomputing its hash does not make it match the independently expected state.

## Workload and costs

Two overlapping chain blocks are composed at m=4,8,16,32 under both retention policies. Their public schema is anchor plus first and last atom, so each consistent summary has six rows. The workload also includes the cross-block and local contradictions.

At m=32 the compact JSON accounts are:

| Account | Archive-backed | Public-only |
| --- | ---: | ---: |
| Live descriptor | 265 bytes | 262 bytes |
| Retained fine specification | 1,106 bytes | 0 bytes in the live object |
| Migration certificate | 16,909 bytes | 16,906 bytes |

The exported experiment still retains original contexts and migration proofs. The zero in the public-only live object is not total-system storage reclamation or permission to delete an external archive. The comparison excludes the shared program and does not claim a shortest encoding of the regular chain.

Archive-backed states store the fine specification and recompute distances for fillings/re-exposure; they do not retain the full distance archive in the live object. Dense closure and proof construction still have their ordinary time and temporary-storage costs.

## Reproduction

    python research/nima/checkers/check_modular_difference_interfaces.py
    python research/nima/checkers/verify_modular_difference_interfaces.py

Implementation: `research/nima/checkers/modular_difference_interfaces.py`.

Artifacts: `research/nima/results/modular-difference*`.

This is a separate research prototype, not a refactor of the two-moment interface. It supplies modular composition and continuation-policy checks for the restricted difference language. It does not establish general polyhedral block compression, noisy observation semantics, confidentiality, actual-source inference or a fresh upstream analytical-admission proof.
