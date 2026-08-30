import MariciFormal.SafetyLiveness

/-! Eventual completion does not manufacture a deadline. -/

namespace MariciFormal.TemporalAuthority.LinearConsumption

def CompletesBy (bound : ℕ) (trace : InfiniteTrace Bool) : Prop :=
  ∃ n ≤ bound, trace n = true

theorem completesBy_implies_eventually
    {bound : ℕ} {trace : InfiniteTrace Bool} (h : CompletesBy bound trace) :
    Eventually (· = true) trace := by
  rcases h with ⟨n, _, hn⟩
  exact ⟨n, hn⟩

/-- Wait exactly `delay` logical steps, then remain completed. -/
def delayedCompletionTrace (delay : ℕ) : InfiniteTrace Bool :=
  fun n => decide (delay ≤ n)

theorem delayedCompletionTrace_valid (delay : ℕ) :
    ValidProgressTrace (delayedCompletionTrace delay) := by
  intro n
  by_cases h : delay ≤ n
  · have hnext : delay ≤ n + 1 := h.trans (Nat.le_succ n)
    simp [delayedCompletionTrace, h, hnext, progressStep]
  · simp [delayedCompletionTrace, h, progressStep]

theorem delayedCompletionTrace_eventually (delay : ℕ) :
    Eventually (· = true) (delayedCompletionTrace delay) := by
  exact ⟨delay, by simp [delayedCompletionTrace]⟩

theorem delayedCompletionTrace_misses_prior_bound (bound : ℕ) :
    ¬ CompletesBy bound (delayedCompletionTrace (bound + 1)) := by
  rintro ⟨n, hn, completed⟩
  have hdelay : bound + 1 ≤ n := by
    simpa [delayedCompletionTrace] using completed
  omega

/-- Hostile family: eventual completion supplies no uniform finite deadline. -/
theorem liveness_does_not_supply_any_fixed_bound :
    ∀ bound, ∃ trace,
      ValidProgressTrace trace ∧
      Eventually (· = true) trace ∧
      ¬ CompletesBy bound trace := by
  intro bound
  exact ⟨delayedCompletionTrace (bound + 1),
    delayedCompletionTrace_valid _, delayedCompletionTrace_eventually _,
    delayedCompletionTrace_misses_prior_bound bound⟩

inductive TimeUnit where
  | logicalStep
  | millisecond
  deriving DecidableEq, Repr

/-- A deadline is meaningless without its clock unit. -/
structure Deadline where
  amount : ℕ
  unit : TimeUnit
  deriving DecidableEq, Repr

def BoundedCompletion (deadline : Deadline) (trace : InfiniteTrace Bool) : Prop :=
  deadline.unit = .logicalStep ∧ CompletesBy deadline.amount trace

theorem completingTrace_has_one_step_deadline :
    BoundedCompletion ⟨1, .logicalStep⟩ completingTrace := by
  exact ⟨rfl, ⟨1, Nat.le_refl 1, rfl⟩⟩

theorem same_number_different_clock_is_not_interchangeable :
    (Deadline.mk 1 .logicalStep) ≠ Deadline.mk 1 .millisecond := by
  decide

/-- Deadline promises carry source authority separately from trace evidence. -/
structure DeadlineGrant where
  deadline : Deadline
  sourceAuthority : Option SourceAuthority

def DeadlineAuthorized (grant : DeadlineGrant) : Prop :=
  SourceAuthorized grant.sourceAuthority

def unauthorizedOneStepDeadline : DeadlineGrant where
  deadline := ⟨1, .logicalStep⟩
  sourceAuthority := none

theorem completion_evidence_does_not_authorize_deadline :
    BoundedCompletion unauthorizedOneStepDeadline.deadline completingTrace ∧
      ¬ DeadlineAuthorized unauthorizedOneStepDeadline := by
  exact ⟨completingTrace_has_one_step_deadline, by
    simp [DeadlineAuthorized, unauthorizedOneStepDeadline, SourceAuthorized]⟩

end MariciFormal.TemporalAuthority.LinearConsumption
