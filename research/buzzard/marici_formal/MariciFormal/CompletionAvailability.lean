import MariciFormal.BoundedMultiplicity
import MariciFormal.FiniteObservation

namespace MariciFormal.TemporalAuthority.LinearConsumption

/-! Availability is separate from the value of completion evidence. -/

inductive CompletionStatus where
  | completed
  | incomplete
  | unknown
  deriving DecidableEq, Repr

abbrev CompletionReadout := Option CompletionStatus

def unavailableCompletion : CompletionReadout := none
def availableIncomplete : CompletionReadout := some .incomplete
def availableUnknown : CompletionReadout := some .unknown

theorem unavailable_completion_is_not_negative_evidence :
    unavailableCompletion ≠ availableIncomplete := by
  decide

theorem unavailable_completion_is_not_available_unknown :
    unavailableCompletion ≠ availableUnknown := by
  decide

inductive RecoveryAction where
  | retry
  | doNotRetry
  | defer
  deriving DecidableEq, Repr

def decideCompletionRecovery : CompletionStatus → RecoveryAction
  | .completed => .doNotRetry
  | .incomplete => .retry
  | .unknown => .defer

def SoundForStatus (status : CompletionStatus) (action : RecoveryAction) : Prop :=
  match status, action with
  | .completed, .doNotRetry => True
  | .incomplete, .retry => True
  | .unknown, .defer => True
  | _, _ => False

theorem three_valued_recovery_policy_is_sound (status : CompletionStatus) :
    SoundForStatus status (decideCompletionRecovery status) := by
  cases status <;> trivial

theorem unknown_status_forces_deferral (action : RecoveryAction)
    (h : SoundForStatus .unknown action) : action = .defer := by
  cases action <;> simp [SoundForStatus] at h ⊢

theorem incomplete_status_justifies_retry :
    decideCompletionRecovery .incomplete = .retry := by
  rfl

theorem completed_status_forbids_retry :
    decideCompletionRecovery .completed = .doNotRetry := by
  rfl

/-- Hostile implementation: absence is silently coerced to `incomplete`. -/
def defaultUnavailableToIncomplete (readout : CompletionReadout) : CompletionStatus :=
  readout.getD .incomplete

theorem defaulting_unavailable_to_incomplete_requests_retry :
    decideCompletionRecovery
      (defaultUnavailableToIncomplete unavailableCompletion) = .retry := by
  rfl

theorem unavailable_default_can_duplicate_completed_effect :
    let action := decideCompletionRecovery
      (defaultUnavailableToIncomplete unavailableCompletion)
    action = .retry ∧ ¬ RecoveryCorrect true true := by
  simp [defaultUnavailableToIncomplete, unavailableCompletion,
    decideCompletionRecovery, RecoveryCorrect]

/-- The observation-sector distinction has the same `Option` shape. -/
theorem unavailable_port_and_available_zero_remain_distinct
    {V F : Type*} [Field F] [AddCommGroup V] [Module F V] :
    (MariciFormal.FiniteObservation.unavailablePort :
        MariciFormal.FiniteObservation.AuthorizedPort V F) ≠
      MariciFormal.FiniteObservation.availableZeroPort :=
  MariciFormal.FiniteObservation.unavailable_ne_availableZero

end MariciFormal.TemporalAuthority.LinearConsumption
