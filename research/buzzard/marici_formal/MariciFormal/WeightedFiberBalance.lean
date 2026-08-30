import Mathlib.Tactic

/-!
Two-point scalar core of Grothendieck's weighted coefficient--Betti Mackey
adjunction gate. General weighted Hilbert adjoints and prime-power metrics
remain external interfaces.
-/

namespace MariciFormal

def twoFiberWeightedDegree (upstairsZero upstairsOne downstairs : ℚ) : ℚ :=
  (upstairsZero + upstairsOne) / downstairs

/-- Degree-two weighted norm and coefficient-one transfer of the selected
zero point are simultaneously possible exactly for balanced fiber weights. -/
theorem c2_weight_balance_and_selection_iff
    (upstairsZero upstairsOne downstairs : ℚ) :
    (downstairs = (upstairsZero + upstairsOne) / 2 ∧
        downstairs = upstairsZero) ↔
      (upstairsZero = upstairsOne ∧ downstairs = upstairsZero) := by
  constructor <;> rintro ⟨hbalance, hselected⟩
  · constructor
    · linarith
    · exact hselected
  · constructor
    · linarith
    · exact hselected

/-- A nonconstant positive fiber metric gives the concrete normalization
conflict. -/
theorem c2_unbalanced_weight_hostile :
    ¬ ((1 : ℚ) = (1 + 3) / 2 ∧ (1 : ℚ) = 1) := by
  norm_num

end MariciFormal
