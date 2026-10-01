# Recursive promoted endpoints and versioned returns

## Explicit recursive endpoint policy

A promoted record retains its child IDs and descendant leaf IDs. Its source
endpoint is an interned identity for the set of child source endpoints; its
target endpoint is similarly an interned target set. These sets are endpoint
footprints, not replacements for member incidence or multiplicity. Complete
child records retain that information.

The first promotion groups leaf records by source. The second groups those
family records by their target footprint ID. Families with matching target
footprints can therefore participate in a common second-level record. This
is an explicit test policy, not a uniquely selected successor endpoint law.

Family identity is persistent by (depth, grouping direction, group key).
Endpoint-footprint identity is persistent by (depth, endpoint role, endpoint
set). A family whose content changes keeps its group-key identity but receives
a new version. An endpoint footprint change can move a record into another
parent group. IDs are globally tagged in the prototype to avoid collision
between leaf and promoted identities.

## Derived content and version propagation

Promoted scalar values are means over descendant LEAVES, so larger child
families receive their correct member weights. Each record retains its ordered
child-version tuple. Any child revision propagates even if two edits cancel
in the aggregate mean. Rebuilding an unchanged hierarchy preserves all IDs,
versions, means and endpoint references.

The fixture rebuilds the hierarchy after each commit; it does not yet optimize
incremental recursive maintenance. The prior dynamic one-level fixture tests
incremental indexing separately.

## Transaction contract

An edit snapshot stores target level, family ID, family version, descendant
leaf IDs and versions, and a requested mean shift. Before mutation, validate
all of them. If valid, shift each addressed leaf by the requested amount and
rebuild the derived hierarchy. Otherwise reject without mutation.

This is a serialized atomic-commit model. Actual concurrent execution would
need a lock or storage transaction covering validation and mutation. It does
not supply distributed consensus, persistence, crash recovery, or automatic
conflict resolution. Rejected edits require a fresh read and explicit retry.

Tests show that two stale edits to the same family cannot both commit, while
an edit to an unaffected disjoint family survives intervening work elsewhere.
Restoring a leaf's old value does not restore its old version (ABA control).
Changing endpoint footprints invalidates old ancestor requests. The policy
can conservatively reject requests even when a more elaborate merge could
safely commute them.

## Verification

    python research/nima/checkers/check_recursive_record_transactions.py

The exact Fraction-based fixture constructs two promotion levels, checks full
descendant reconstruction, leaf-weighted means, version propagation and rebuild
idempotence after100 dynamic operations. Separate interleavings test overlapping
edits, disjoint edits, endpoint movement and ABA restoration. No network or
threaded execution is claimed.

## Incremental structural result

Promoted records now have executable next-level endpoints and state-dependent
edit admissibility. Coherence extends to a two-level changing hierarchy under
one declared endpoint/identity/version policy. An ID alone is insufficient:
its version and retained membership define the object an edit addresses.

The Store now also retains accepted old/new event batches and supports serialized
LIFO compensation with fresh versions. See [recursive history and return coherence](recursive-history-and-return-coherence.md)
for the integrated tests and serialization audit. Crash-safe durable storage,
a general HoTT formalization, a policy-selection argument, and physical dynamics
remain open.
