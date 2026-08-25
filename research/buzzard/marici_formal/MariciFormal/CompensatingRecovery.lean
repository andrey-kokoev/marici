import MariciFormal.SmallScheduleModelCheck

namespace MariciFormal.TemporalAuthority.LinearConsumption

/-! Compensation records a new action; it does not erase execution history. -/

structure CompensationState where
  effects : Nat
  compensations : Nat
  deriving DecidableEq, Repr

def OutstandingEffects (state : CompensationState) : Nat :=
  state.effects - state.compensations

def applyCompensation (state : CompensationState) : CompensationState × Bool :=
  if state.compensations < state.effects then
    (⟨state.effects, state.compensations + 1⟩, true)
  else (state, false)

def rollbackState : CompensationState := ⟨0, 0⟩
def completedState : CompensationState := ⟨1, 0⟩
def compensatedState : CompensationState := (applyCompensation completedState).1

theorem compensation_clears_outstanding_effect :
    OutstandingEffects compensatedState = 0 := by
  decide

theorem compensation_is_not_rollback :
    OutstandingEffects compensatedState = OutstandingEffects rollbackState ∧
      compensatedState ≠ rollbackState := by
  decide

def UncompensatedExactlyOnce (state : CompensationState) : Prop :=
  state.effects = 1 ∧ state.compensations = 0

theorem compensated_execution_is_not_uncompensated_exactly_once :
    ¬ UncompensatedExactlyOnce compensatedState := by
  simp [UncompensatedExactlyOnce, compensatedState, applyCompensation,
    completedState]

theorem controlled_compensation_rejects_duplicate_compensation :
    let first := applyCompensation completedState
    let second := applyCompensation first.1
    first.2 = true ∧ second.2 = false ∧ second.1 = first.1 := by
  decide

/-- A hostile countermodel that records compensation without an outstanding check. -/
def naiveCompensate (state : CompensationState) : CompensationState :=
  ⟨state.effects, state.compensations + 1⟩

theorem naive_duplicate_compensation_overcompensates :
    let twice := naiveCompensate (naiveCompensate completedState)
    twice.effects = 1 ∧ twice.compensations = 2 := by
  decide

inductive RecoveryResolution where
  | retry
  | abandon
  | compensate
  | manualAdjudication
  deriving DecidableEq, Repr

structure ResolutionGrant where
  resolution : RecoveryResolution
  sourceAuthority : Option SourceAuthority

def ResolutionAuthorized (grant : ResolutionGrant) : Prop :=
  SourceAuthorized grant.sourceAuthority

theorem every_resolution_requires_source_authority
    (resolution : RecoveryResolution) :
    ¬ ResolutionAuthorized ⟨resolution, none⟩ := by
  exact absent_source_authority_is_not_authorized

theorem recovery_resolutions_are_pairwise_noninterchangeable :
    RecoveryResolution.retry ≠ .abandon ∧
      RecoveryResolution.retry ≠ .compensate ∧
      RecoveryResolution.retry ≠ .manualAdjudication ∧
      RecoveryResolution.abandon ≠ .compensate ∧
      RecoveryResolution.abandon ≠ .manualAdjudication ∧
      RecoveryResolution.compensate ≠ .manualAdjudication := by
  decide

def applyResolution (state : CompensationState) :
    RecoveryResolution → CompensationState
  | .retry => ⟨state.effects + 1, state.compensations⟩
  | .abandon => state
  | .compensate => (applyCompensation state).1
  | .manualAdjudication => state

theorem retry_abandon_and_compensate_have_distinct_semantics :
    applyResolution completedState .retry = ⟨2, 0⟩ ∧
      applyResolution completedState .abandon = ⟨1, 0⟩ ∧
      applyResolution completedState .compensate = ⟨1, 1⟩ := by
  decide

/-- State equality of abandon/manual does not identify their authority kind. -/
theorem equal_state_projection_does_not_make_resolutions_interchangeable :
    applyResolution completedState .abandon =
        applyResolution completedState .manualAdjudication ∧
      RecoveryResolution.abandon ≠ .manualAdjudication := by
  exact ⟨rfl, by decide⟩

end MariciFormal.TemporalAuthority.LinearConsumption
