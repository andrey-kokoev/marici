# Prior request-namespace partition

`ShardGrant` is a source-authorized assignment of one issuer/shard pair.
`allocateFromShard` qualifies each local request number by both fields.

The generic theorem `disjoint_shards_prevent_collision` proves that allocators
holding unequal shard assignments cannot emit the same partitioned request ID,
even if they use equal local counters and never communicate at runtime.

The grant also supplies the explicit source authority required by the existing
`priorPartition` repair type.

Hostile boundaries:

- erasing the shard collapses two distinct allocations;
- two disconnected allocators assigned the same shard can still emit exactly
  the same ID;
- partition authority therefore does not imply uniqueness of allocation inside
  each shard.

Missing convention-fixed inputs:

- the authority that assigns disjoint shard identifiers;
- whether shard grants overlap in time or may be reassigned;
- durable local-counter allocation inside a shard;
- retirement rules preventing delayed replay after shard reassignment.

Verification commands from `research/buzzard/marici_formal`:

```text
lake env lean MariciFormal/NamespacePartition.lean
lake build
```

Result: both commands passed under Lean `v4.33.1`; the project reported
`Build completed successfully (8722 jobs).` The site build was not run.
