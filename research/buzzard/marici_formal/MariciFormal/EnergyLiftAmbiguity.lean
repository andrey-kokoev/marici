import Mathlib

/-!
One scalar incidence value does not determine a coercive energy lift.
-/

namespace MariciFormal

abbrev TwoChannelState := Fin 2 → Rat

def distinguishedState : TwoChannelState := ![1, 0]

def hiddenState : TwoChannelState := ![0, 1]

/-- Clark reference form `Q = I₂`. -/
def clarkForm (x : TwoChannelState) : Rat :=
  x 0 ^ 2 + x 1 ^ 2

/-- Positive energy lift `diag(1,1)`. -/
def positiveEnergyLift (x : TwoChannelState) : Rat :=
  x 0 ^ 2 + x 1 ^ 2

/-- Indefinite energy lift `diag(1,-1)`. -/
def indefiniteEnergyLift (x : TwoChannelState) : Rat :=
  x 0 ^ 2 - x 1 ^ 2

theorem positiveEnergyLift_eq_clarkForm :
    positiveEnergyLift = clarkForm := rfl

theorem positiveEnergyLift_nonnegative (x : TwoChannelState) :
    0 ≤ positiveEnergyLift x := by
  unfold positiveEnergyLift
  positivity

/-- Both lifts return the same scalar incidence on the distinguished state. -/
theorem energyLifts_agree_on_distinguishedState :
    positiveEnergyLift distinguishedState = 1 ∧
      indefiniteEnergyLift distinguishedState = 1 := by
  norm_num [positiveEnergyLift, indefiniteEnergyLift, distinguishedState]

/-- The unseen channel exposes the opposite orientation. -/
theorem indefiniteEnergyLift_negative_on_hiddenState :
    indefiniteEnergyLift hiddenState = -1 := by
  norm_num [indefiniteEnergyLift, hiddenState]

theorem indefiniteEnergyLift_not_nonnegative :
    ¬ ∀ x : TwoChannelState, 0 ≤ indefiniteEnergyLift x := by
  intro nonnegative
  have h := nonnegative hiddenState
  rw [indefiniteEnergyLift_negative_on_hiddenState] at h
  norm_num at h

/-- Equal scalar observation is compatible with coercive and noncoercive lifts. -/
theorem scalarIncidence_does_not_determine_energyOrientation :
    ∃ positiveLift indefiniteLift : TwoChannelState → Rat,
      positiveLift distinguishedState = indefiniteLift distinguishedState ∧
      (∀ x, 0 ≤ positiveLift x) ∧
      ¬ (∀ x, 0 ≤ indefiniteLift x) := by
  refine ⟨positiveEnergyLift, indefiniteEnergyLift, ?_,
    positiveEnergyLift_nonnegative, indefiniteEnergyLift_not_nonnegative⟩
  rw [energyLifts_agree_on_distinguishedState.1,
    energyLifts_agree_on_distinguishedState.2]

end MariciFormal
