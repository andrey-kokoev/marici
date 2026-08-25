import MariciFormal.RecoveryEvidence

namespace MariciFormal.TemporalAuthority.LinearConsumption

/-! Request identity is qualified by an authority-owned issuer namespace. -/

abbrev IssuerId := String
abbrev LocalRequestId := Nat

structure QualifiedRequestId where
  issuer : IssuerId
  localId : LocalRequestId
  deriving DecidableEq, Repr

structure NamespaceGrant where
  issuer : IssuerId
  sourceAuthority : SourceAuthority

def MayIssue (grant : NamespaceGrant) (id : QualifiedRequestId) : Prop :=
  grant.issuer = id.issuer

def issuerA : IssuerId := "issuer-A"
def issuerB : IssuerId := "issuer-B"

def grantA : NamespaceGrant := ⟨issuerA, requestAuthority⟩
def idA7 : QualifiedRequestId := ⟨issuerA, 7⟩
def idB7 : QualifiedRequestId := ⟨issuerB, 7⟩

theorem qualified_ids_separate_independent_issuer_namespaces :
    idA7.localId = idB7.localId ∧ idA7 ≠ idB7 := by
  simp [idA7, idB7, issuerA, issuerB]

theorem issuer_grant_cannot_allocate_in_another_namespace :
    MayIssue grantA idA7 ∧ ¬ MayIssue grantA idB7 := by
  simp [MayIssue, grantA, idA7, idB7, issuerA, issuerB]

/-- Forgetting the issuer recreates a collision between distinct requests. -/
def eraseIssuer (id : QualifiedRequestId) : LocalRequestId := id.localId

theorem erasing_namespace_authority_collapses_distinct_requests :
    idA7 ≠ idB7 ∧ eraseIssuer idA7 = eraseIssuer idB7 := by
  exact ⟨qualified_ids_separate_independent_issuer_namespaces.2, rfl⟩

/-- Transport preserves the issuer named by the original namespace grant. -/
def transportNamespaceGrant (grant : NamespaceGrant) : NamespaceGrant := grant

theorem transport_does_not_change_namespace_authority :
    (transportNamespaceGrant grantA).issuer = issuerA ∧
      ¬ MayIssue (transportNamespaceGrant grantA) idB7 := by
  simp [transportNamespaceGrant, grantA, issuerA, MayIssue, idB7, issuerB]

/-- Qualification alone cannot coordinate two allocators using the same issuer. -/
structure DisconnectedAllocators where
  leftIssuer : IssuerId
  rightIssuer : IssuerId
  leftNext : LocalRequestId
  rightNext : LocalRequestId

def duplicatedIssuerAllocator : DisconnectedAllocators :=
  ⟨issuerA, issuerA, 7, 7⟩

def allocateLeft (a : DisconnectedAllocators) : QualifiedRequestId :=
  ⟨a.leftIssuer, a.leftNext⟩

def allocateRight (a : DisconnectedAllocators) : QualifiedRequestId :=
  ⟨a.rightIssuer, a.rightNext⟩

theorem same_namespace_disconnected_allocators_can_collide :
    allocateLeft duplicatedIssuerAllocator =
      allocateRight duplicatedIssuerAllocator := by
  rfl

theorem issuer_qualification_does_not_supply_local_linearization :
    MayIssue grantA (allocateLeft duplicatedIssuerAllocator) ∧
      MayIssue grantA (allocateRight duplicatedIssuerAllocator) ∧
      allocateLeft duplicatedIssuerAllocator =
        allocateRight duplicatedIssuerAllocator := by
  simp [MayIssue, grantA, allocateLeft, allocateRight,
    duplicatedIssuerAllocator, issuerA]

end MariciFormal.TemporalAuthority.LinearConsumption
