# Incremental difference refinement reuses only bound block proofs

## Delivered gate

A persistent refinement adapter now updates the modular difference interface without recomputing every block closure. It also supports public-only refinement directly on a certified public relation, without reconstructing hidden state.

Independent replay checks 22 transitions against fresh compilation. All agree. A newly added block constraint creates a certified cross-block contradiction while both local blocks remain consistent. Ten cache/state mutations are rejected, and six hidden continuations from public-only states are refused.

## Archive-backed append operations

`ArchivedHistory.refine_block(index, edge)` appends one raw difference edge to the selected block. `refine_public(edge)` appends an edge between currently public nodes to the exterior relation.

Earlier snapshots are copied, not modified. Source binding, atom count, block ownership, boundaries and retention policy are fixed by these operations. They cannot silently alter the chart, schema or representation class.

A block proof depends on:

    source rule + m + source binding + complete block specification.

The block specification includes its nodes, boundary and ordered evidence. A changed block receives a fresh closure. Every unchanged block is reused only when its dependency digest matches; its prior certificate must already verify against the expected predecessor state.

The composed boundary graph is then rebuilt and closed. This implementation does not incrementally update the boundary closure itself.

## Transition certificates

Each transition records the expected predecessor digest, the predecessor proof digest, the exact append operation, before/after block dependencies, reused/recomputed block indices and the new composition certificate.

The independent verifier obtains the expected initial state and operation sequence from the frozen contract. It constructs each successor itself, checks the predecessor and successor arithmetic, and verifies equality of reused proof objects under unchanged dependencies. A packet's own claimed history is not the authority for its expected predecessor.

Digests provide statement binding, not observational authentication. Dependency equality is deliberately conservative: a redundant new edge changes the syntactic dependency and triggers recomputation even if its old closure would remain mathematically valid.

## Public-only append operations

`PublicHistory` begins from a separately checked public-only migration summary. It stores that base public relation, source/context metadata and the full tuple of subsequently accepted public edges.

A public refinement closes the base summary plus every retained public edge. An exact projected image is a congruence under such public evidence additions, so this gives the same public relation as appending those edges to the original fine carrier and projecting again.

No block rows or hidden-node distances are stored in this object. Hidden block refinement and hidden-node re-exposure raise `PermissionError`. These refusals remain in force after the public relation becomes inconsistent.

The initial summary must have a valid migration certificate. `PublicHistory.from_live` is not an authentication service for arbitrary supplied descriptors; the replay independently checks its initial migration and origin binding.

## Contradiction and persistence controls

At m=4,8,16, archive-backed sequences tighten one block, then another, then append a conflicting public edge. A further append preserves inconsistency. Public-only sequences likewise become inconsistent after two public constraints and remain inconsistent after a third.

A separate control starts with two compatible blocks. Tightening only the second introduces a negative cycle across their shared boundary. The updated block remains locally consistent, so checking only local feasibility would miss the contradiction. Recomposition exports the negative cycle and its original-edge expansion, independently checked by the existing verifier.

The tests reject stale changed-block proofs, false cache-hit declarations, altered dependencies, a foreign predecessor proof, changed operations, policy changes, dropped fine history, altered public origins and dropped public evidence.

Four-field gain rows are rejected rather than interpreted as difference edges. Incremental gain-chart changes are not implemented by this adapter.

## Cost boundary

Across 13 archive-backed transitions:

- seven block closures are recomputed;
- nineteen block closures are reused;
- fresh compilation would compute twenty-six block closures.

These counts exclude initial compilation. Boundary closure still runs on every update. Arithmetic verification deliberately replays all blocks; this is not an incremental-verification speed claim.

The prototype copies states and packets to preserve snapshot behavior and retains complete local closure proofs for reuse. Saved snapshots, proof caches and full evidence tuples therefore remain charged. Selective recomputation is not evidence compression or a uniform runtime improvement.

## Reproduction

    python research/nima/checkers/check_incremental_difference_interfaces.py
    python research/nima/checkers/verify_incremental_difference_interfaces.py

Implementation: `research/nima/checkers/incremental_difference_interfaces.py`.

Artifacts: `research/nima/results/incremental-difference*`.

The modular engine now exposes a shared proposal-assembly helper so fresh and selective compilation use the same composition code. The existing modular and balanced-gain workloads were regenerated and independently verified after this refactor. No gain semantics, upstream source admission or public measurement authority was added.
