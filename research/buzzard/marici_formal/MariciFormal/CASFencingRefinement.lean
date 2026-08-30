import MariciFormal.FiniteConcurrentHistory

namespace MariciFormal.TemporalAuthority.LinearConsumption

/-! Concrete compare-and-set refinement of the token-4 fenced specification. -/

/-- `false` abstracts to unused token state; `true` to one completed token-4 use. -/
def boolToFencedState : Bool → FencedEffectState
  | false => initialFencedEffect
  | true => ⟨⟨4⟩, 1⟩

theorem compareAndSet_refines_token4_fenced_effect (memory : Bool) :
    (boolToFencedState (compareAndSet memory).1,
        (compareAndSet memory).2) =
      attemptFencedEffect (boolToFencedState memory) 4 := by
  cases memory <;> rfl

theorem concrete_consumed_state_matches_atomic_fenced_result :
    boolToFencedState true =
      (attemptFencedEffect (boolToFencedState false) 4).1 := by
  rfl

theorem two_compareAndSet_operations_refine_fenced_order
    (order : TwoSiteOrder) :
    runTwoCAS order = executeConcurrentFenceOrder overlappingSameToken order := by
  cases order <;> rfl

theorem every_two_CAS_schedule_has_one_success (order : TwoSiteOrder) :
    ExactlyOne (executeConcurrentFenceOrder overlappingSameToken order) := by
  rw [← two_compareAndSet_operations_refine_fenced_order]
  exact two_compareAndSet_exactly_one order

/-- The non-atomic split trace observes an outcome no fenced order can explain. -/
theorem split_read_write_has_no_fenced_refinement :
    splitOutcome lostUpdateTrace = duplicatedConcurrentSuccess.observed ∧
      IsEmpty (ConcurrentFenceRefinement duplicatedConcurrentSuccess) := by
  exact ⟨rfl, duplicated_concurrent_success_has_no_sequential_refinement⟩

theorem CAS_refinement_does_not_supply_persistence_atomicity :
    compareAndSet false = (true, true) ∧
      fenceOnlyCrash.effectCount = 0 ∧ effectOnlyCrash.effectCount = 1 := by
  decide

/-- Source authority remains external to the transition-level simulation. -/
theorem unauthorized_CAS_repair_remains_unauthorized :
    ¬ RepairAuthorized ⟨.sharedLinearization, none⟩ :=
  every_repair_requires_additional_source_authority .sharedLinearization

end MariciFormal.TemporalAuthority.LinearConsumption
