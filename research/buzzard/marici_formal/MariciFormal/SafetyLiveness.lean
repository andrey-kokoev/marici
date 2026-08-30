import MariciFormal.SemanticFidelity

/-!
Safety does not imply liveness for the distributed single-consumption fixture.

The definitions are intentionally trace-level.  No scheduler fairness or
physical timing assumption is hidden in the transition relation.
-/

namespace MariciFormal.TemporalAuthority.LinearConsumption

abbrev InfiniteTrace (State : Type*) := ℕ → State

def Eventually {State : Type*} (goal : State → Prop) (trace : InfiniteTrace State) : Prop :=
  ∃ n, goal (trace n)

def PrefixSafe {State : Type*} (safe : State → Prop)
    (bound : ℕ) (trace : InfiniteTrace State) : Prop :=
  ∀ n ≤ bound, safe (trace n)

/-- `false` is waiting; `true` is completed. Completion is irreversible. -/
def progressStep : Bool → Bool → Prop
  | false, _ => True
  | true, next => next = true

def ValidProgressTrace (trace : InfiniteTrace Bool) : Prop :=
  ∀ n, progressStep (trace n) (trace (n + 1))

/-- Local safety: a completed capability cannot return to waiting. -/
def CompletionClosed (trace : InfiniteTrace Bool) : Prop :=
  ∀ n, trace n = true → trace (n + 1) = true

theorem every_valid_trace_is_completion_closed
    {trace : InfiniteTrace Bool} (valid : ValidProgressTrace trace) :
    CompletionClosed trace := by
  intro n completed
  have step := valid n
  simp [progressStep, completed] at step
  exact step

def stutteringTrace : InfiniteTrace Bool := fun _ => false

theorem stutteringTrace_valid : ValidProgressTrace stutteringTrace := by
  intro n
  simp [stutteringTrace, progressStep]

theorem every_finite_stuttering_prefix_is_safe (bound : ℕ) :
    PrefixSafe (fun state => state = false ∨ state = true) bound stutteringTrace := by
  intro n hn
  exact Or.inl rfl

/-- Hostile trace: all finite safety prefixes pass, but completion never occurs. -/
theorem finite_safety_cannot_supply_liveness :
    (∀ bound, PrefixSafe (fun state => state = false ∨ state = true)
      bound stutteringTrace) ∧
    ValidProgressTrace stutteringTrace ∧
    ¬ Eventually (· = true) stutteringTrace := by
  refine ⟨every_finite_stuttering_prefix_is_safe, stutteringTrace_valid, ?_⟩
  rintro ⟨n, completed⟩
  contradiction

/-- A trace that completes at its first transition and remains completed. -/
def completingTrace : InfiniteTrace Bool
  | 0 => false
  | _ + 1 => true

theorem completingTrace_valid : ValidProgressTrace completingTrace := by
  intro n
  cases n <;> simp [completingTrace, progressStep]

theorem completingTrace_eventually_completes :
    Eventually (· = true) completingTrace := by
  exact ⟨1, rfl⟩

/-- Explicit scheduler/environment progress premise. -/
def CompletionScheduled (trace : InfiniteTrace Bool) : Prop :=
  ∃ n, trace (n + 1) = true

theorem liveness_of_completion_scheduled
    (trace : InfiniteTrace Bool) (scheduled : CompletionScheduled trace) :
    Eventually (· = true) trace := by
  rcases scheduled with ⟨n, hn⟩
  exact ⟨n + 1, hn⟩

theorem validity_does_not_imply_completion_scheduled :
    ValidProgressTrace stutteringTrace ∧
      ¬ CompletionScheduled stutteringTrace := by
  refine ⟨stutteringTrace_valid, ?_⟩
  rintro ⟨n, hn⟩
  contradiction

/-- Bounded schedule coverage and semantic fidelity remain true without liveness. -/
theorem finite_audit_interfaces_do_not_supply_liveness :
    splitSemanticCheck.domain.Covers ∧
      splitSemanticCheck.Faithful ∧
      ValidProgressTrace stutteringTrace ∧
      ¬ Eventually (· = true) stutteringTrace := by
  refine ⟨legalSplitDomain_covers, split_semantics_faithful,
    stutteringTrace_valid, ?_⟩
  rintro ⟨n, hn⟩
  contradiction

end MariciFormal.TemporalAuthority.LinearConsumption
