import MariciFormal.ProtocolTrace

namespace MariciFormal.TemporalAuthority.LinearConsumption

/-! Real-time refinement of two concurrent fence attempts. -/

structure TimedFenceAttempt where
  token : Nat
  interval : OperationInterval

structure ConcurrentFenceHistory where
  left : TimedFenceAttempt
  right : TimedFenceAttempt
  observed : Bool × Bool

/-- Execute the attempts sequentially and return outcomes in site order. -/
def executeConcurrentFenceOrder (h : ConcurrentFenceHistory)
    (order : TwoSiteOrder) : Bool × Bool :=
  match order with
  | .AthenB =>
      let first := attemptFencedEffect initialFencedEffect h.left.token
      let second := attemptFencedEffect first.1 h.right.token
      (first.2, second.2)
  | .BthenA =>
      let first := attemptFencedEffect initialFencedEffect h.right.token
      let second := attemptFencedEffect first.1 h.left.token
      (second.2, first.2)

structure ConcurrentFenceRefinement (h : ConcurrentFenceHistory) where
  order : TwoSiteOrder
  agrees : h.observed = executeConcurrentFenceOrder h order
  respectsLeftRight :
    RealTimePrecedes h.left.interval h.right.interval → order = .AthenB
  respectsRightLeft :
    RealTimePrecedes h.right.interval h.left.interval → order = .BthenA

def overlappingSameToken : ConcurrentFenceHistory where
  left := ⟨4, interval 0 3 (by decide)⟩
  right := ⟨4, interval 1 2 (by decide)⟩
  observed := (true, false)

def overlappingSameTokenRefines : ConcurrentFenceRefinement overlappingSameToken where
  order := .AthenB
  agrees := rfl
  respectsLeftRight := by
    simp [RealTimePrecedes, overlappingSameToken, interval]
  respectsRightLeft := by
    simp [RealTimePrecedes, overlappingSameToken, interval]

theorem concurrent_refinement_matches_finite_trace_accounting :
    let finite := runFencedTrace initialFencedEffect [4, 4]
    overlappingSameToken.observed = (true, false) ∧
      finite.successes = 1 ∧ finite.finalState.effectCount = 1 := by
  decide

def duplicatedConcurrentSuccess : ConcurrentFenceHistory where
  left := ⟨4, interval 0 3 (by decide)⟩
  right := ⟨4, interval 1 2 (by decide)⟩
  observed := (true, true)

theorem duplicated_concurrent_success_has_no_sequential_refinement :
    IsEmpty (ConcurrentFenceRefinement duplicatedConcurrentSuccess) := by
  constructor
  intro w
  have hagree := w.agrees
  cases horder : w.order <;>
    simp [duplicatedConcurrentSuccess, executeConcurrentFenceOrder,
      attemptFencedEffect, initialFencedEffect, initialFence, horder] at hagree

/-- Right completes first, but the observation claims the left operation won. -/
def fencePrecedenceViolation : ConcurrentFenceHistory where
  left := ⟨4, interval 2 3 (by decide)⟩
  right := ⟨4, interval 0 1 (by decide)⟩
  observed := (true, false)

theorem fence_precedence_violation_has_no_real_time_refinement :
    IsEmpty (ConcurrentFenceRefinement fencePrecedenceViolation) := by
  constructor
  intro w
  have horderA : w.order = .AthenB := by
    cases horder : w.order
    · rfl
    · have hagree := w.agrees
      simp [fencePrecedenceViolation, executeConcurrentFenceOrder,
        attemptFencedEffect, initialFencedEffect, initialFence, horder] at hagree
  have horderB : w.order = .BthenA := by
    apply w.respectsRightLeft
    norm_num [RealTimePrecedes, fencePrecedenceViolation, interval]
  rw [horderA] at horderB
  contradiction

end MariciFormal.TemporalAuthority.LinearConsumption
