import MariciFormal.TemporalAuthority

namespace MariciFormal.TemporalAuthority.LinearConsumption

def ExpiryOnlyExecutable (lease : ExecutionLease) (now : Nat) : Prop :=
  now < lease.expiresAt

def FencedExecutable (lease : ExecutionLease) (state : LeaseState)
    (now : Nat) : Prop :=
  now < lease.expiresAt ∧ lease.validatedEpoch = state.liveEpoch

theorem stale_lease_passes_expiry_only_after_revocation :
    ExpiryOnlyExecutable liveLease 5 := by
  norm_num [ExpiryOnlyExecutable, liveLease]

theorem stale_lease_rejected_by_fenced_target_after_revocation :
    ¬ FencedExecutable liveLease (revokeEpoch freshLeaseState) 5 := by
  simp [FencedExecutable, liveLease, revokeEpoch, freshLeaseState]

theorem expiry_check_alone_does_not_enforce_epoch_revocation :
    ExpiryOnlyExecutable liveLease 5 ∧
      ¬ FencedExecutable liveLease (revokeEpoch freshLeaseState) 5 :=
  ⟨stale_lease_passes_expiry_only_after_revocation,
    stale_lease_rejected_by_fenced_target_after_revocation⟩

theorem fenced_execution_supplies_live_epoch
    (lease : ExecutionLease) (state : LeaseState) (now : Nat)
    (h : FencedExecutable lease state now) :
    lease.validatedEpoch = state.liveEpoch := h.2

def transportLease (lease : ExecutionLease) : ExecutionLease := lease

theorem transport_does_not_bypass_fence :
    ¬ FencedExecutable (transportLease liveLease)
      (revokeEpoch freshLeaseState) 5 :=
  stale_lease_rejected_by_fenced_target_after_revocation

structure FencedResourceState where
  lastAccepted : Nat

def attemptOrderedFence (state : FencedResourceState) (token : Nat) :
    FencedResourceState × Bool :=
  if state.lastAccepted < token then (⟨token⟩, true) else (state, false)

theorem ordered_fence_success_iff (state : FencedResourceState) (token : Nat) :
    (attemptOrderedFence state token).2 = true ↔ state.lastAccepted < token := by
  by_cases h : state.lastAccepted < token <;> simp [attemptOrderedFence, h]

theorem ordered_fence_success_advances_to_presented_token
    (state : FencedResourceState) (token : Nat)
    (h : (attemptOrderedFence state token).2 = true) :
    (attemptOrderedFence state token).1.lastAccepted = token := by
  have hlt := (ordered_fence_success_iff state token).mp h
  simp [attemptOrderedFence, hlt]

def initialFence : FencedResourceState := ⟨3⟩

theorem one_authoritative_register_rejects_duplicate_token :
    let first := attemptOrderedFence initialFence 4
    let second := attemptOrderedFence first.1 4
    first.2 = true ∧ second.2 = false := by decide

structure ReplicatedFenceView where
  left : FencedResourceState
  right : FencedResourceState

def duplicatedFenceView : ReplicatedFenceView := ⟨initialFence, initialFence⟩

theorem duplicated_local_fence_registers_accept_twice :
    (attemptOrderedFence duplicatedFenceView.left 4).2 = true ∧
      (attemptOrderedFence duplicatedFenceView.right 4).2 = true := by decide

theorem local_fencing_does_not_supply_global_single_consumption :
    let outcomes :=
      ((attemptOrderedFence duplicatedFenceView.left 4).2,
       (attemptOrderedFence duplicatedFenceView.right 4).2)
    outcomes = (true, true) ∧ outcomes ≠ (true, false) ∧
      outcomes ≠ (false, true) := by decide

structure FencedEffectState where
  fence : FencedResourceState
  effectCount : Nat

def initialFencedEffect : FencedEffectState := ⟨initialFence, 0⟩

def attemptFencedEffect (state : FencedEffectState) (token : Nat) :
    FencedEffectState × Bool :=
  if state.fence.lastAccepted < token then
    (⟨⟨token⟩, state.effectCount + 1⟩, true)
  else (state, false)

theorem atomic_fence_and_effect_reject_retry_without_duplication :
    let first := attemptFencedEffect initialFencedEffect 4
    let retry := attemptFencedEffect first.1 4
    first.2 = true ∧ retry.2 = false ∧ retry.1.effectCount = 1 := by decide

def fenceOnlyCrash : FencedEffectState := ⟨⟨4⟩, 0⟩

theorem fence_only_crash_permanently_rejects_missing_effect_retry :
    (attemptFencedEffect fenceOnlyCrash 4).2 = false ∧
      (attemptFencedEffect fenceOnlyCrash 4).1.effectCount = 0 := by decide

def effectOnlyCrash : FencedEffectState := ⟨initialFence, 1⟩

theorem effect_only_crash_allows_duplicate_effect_on_retry :
    (attemptFencedEffect effectOnlyCrash 4).2 = true ∧
      (attemptFencedEffect effectOnlyCrash 4).1.effectCount = 2 := by decide

theorem fence_effect_atomicity_is_independent_of_ordered_comparison :
    fenceOnlyCrash.fence.lastAccepted = 4 ∧
      effectOnlyCrash.fence.lastAccepted < 4 ∧
      (attemptFencedEffect fenceOnlyCrash 4).1.effectCount = 0 ∧
      (attemptFencedEffect effectOnlyCrash 4).1.effectCount = 2 := by decide

end MariciFormal.TemporalAuthority.LinearConsumption
