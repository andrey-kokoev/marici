import MariciFormal.RequestNamespace

namespace MariciFormal.TemporalAuthority.LinearConsumption

/-! Prior request-namespace partition as a coordination-free repair. -/

abbrev ShardId := Nat

structure PartitionedRequestId where
  issuer : IssuerId
  shard : ShardId
  localId : LocalRequestId
  deriving DecidableEq, Repr

structure ShardGrant where
  issuer : IssuerId
  shard : ShardId
  sourceAuthority : SourceAuthority

def MayIssueFromShard (grant : ShardGrant) (id : PartitionedRequestId) : Prop :=
  grant.issuer = id.issuer ∧ grant.shard = id.shard

def allocateFromShard (grant : ShardGrant) (localId : LocalRequestId) :
    PartitionedRequestId :=
  ⟨grant.issuer, grant.shard, localId⟩

theorem shard_grant_authorizes_its_allocations
    (grant : ShardGrant) (localId : LocalRequestId) :
    MayIssueFromShard grant (allocateFromShard grant localId) := by
  simp [MayIssueFromShard, allocateFromShard]

/-- Disjoint shards cannot allocate the same qualified request identifier. -/
theorem disjoint_shards_prevent_collision
    (left right : ShardGrant) (hshard : left.shard ≠ right.shard)
    (leftLocal rightLocal : LocalRequestId) :
    allocateFromShard left leftLocal ≠ allocateFromShard right rightLocal := by
  intro h
  have hs := congrArg PartitionedRequestId.shard h
  exact hshard hs

def shardZero : ShardGrant := ⟨issuerA, 0, requestAuthority⟩
def shardOne : ShardGrant := ⟨issuerA, 1, requestAuthority⟩

theorem disconnected_disjoint_shards_allocate_same_local_without_collision :
    (allocateFromShard shardZero 7).localId =
        (allocateFromShard shardOne 7).localId ∧
      allocateFromShard shardZero 7 ≠ allocateFromShard shardOne 7 := by
  constructor
  · rfl
  · exact disjoint_shards_prevent_collision shardZero shardOne (by decide) 7 7

theorem shard_grant_supplies_prior_partition_source_authority
    (grant : ShardGrant) :
    RepairAuthorized ⟨.priorPartition, some grant.sourceAuthority⟩ := by
  exact ⟨grant.sourceAuthority, rfl⟩

/-- Erasing the shard destroys the distinction established by partitioning. -/
def eraseShard (id : PartitionedRequestId) : QualifiedRequestId :=
  ⟨id.issuer, id.localId⟩

theorem erasing_shard_collapses_disjoint_allocations :
    allocateFromShard shardZero 7 ≠ allocateFromShard shardOne 7 ∧
      eraseShard (allocateFromShard shardZero 7) =
        eraseShard (allocateFromShard shardOne 7) := by
  exact ⟨disconnected_disjoint_shards_allocate_same_local_without_collision.2, rfl⟩

/-- Partitioning does not coordinate two allocators assigned the same shard. -/
def duplicatedShardGrant : ShardGrant := shardZero

theorem same_shard_disconnected_allocators_still_collide :
    allocateFromShard shardZero 7 = allocateFromShard duplicatedShardGrant 7 := by
  rfl

theorem local_allocation_uniqueness_is_a_separate_premise :
    MayIssueFromShard shardZero (allocateFromShard shardZero 7) ∧
      MayIssueFromShard duplicatedShardGrant
        (allocateFromShard duplicatedShardGrant 7) ∧
      allocateFromShard shardZero 7 =
        allocateFromShard duplicatedShardGrant 7 := by
  simp [MayIssueFromShard, allocateFromShard, duplicatedShardGrant]

end MariciFormal.TemporalAuthority.LinearConsumption
