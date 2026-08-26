import Mathlib

/-!
Finite weighted duality for scalar traces, including the sharp extremizer.
-/

namespace MariciFormal

section FiniteWeightedTrace

variable {n : Nat}

def weightedNormSq (weight : Fin n → Real) (x : Fin n → Real) : Real :=
  ∑ i, weight i * x i ^ 2

def finiteTrace (coefficient x : Fin n → Real) : Real :=
  ∑ i, coefficient i * x i

noncomputable def weightedDualSq (weight coefficient : Fin n → Real) : Real :=
  ∑ i, coefficient i ^ 2 / weight i

/-- Weighted Cauchy--Schwarz in the exact squared form used by the trace bound. -/
theorem finiteTrace_sq_le_weightedDualSq_mul_weightedNormSq
    (weight coefficient x : Fin n → Real)
    (weight_pos : ∀ i, 0 < weight i) :
    finiteTrace coefficient x ^ 2 ≤
      weightedDualSq weight coefficient * weightedNormSq weight x := by
  unfold finiteTrace weightedDualSq weightedNormSq
  apply Finset.sum_sq_le_sum_mul_sum_of_sq_le_mul
  · intro i hi
    exact div_nonneg (sq_nonneg _) (weight_pos i).le
  · intro i hi
    exact mul_nonneg (weight_pos i).le (sq_nonneg _)
  · intro i hi
    apply le_of_eq
    field_simp [(weight_pos i).ne']

/-- The coefficient divided by the weight is the finite sharpness witness. -/
noncomputable def weightedExtremizer (weight coefficient : Fin n → Real) : Fin n → Real :=
  fun i => coefficient i / weight i

theorem finiteTrace_weightedExtremizer
    (weight coefficient : Fin n → Real)
    (weight_pos : ∀ i, 0 < weight i) :
    finiteTrace coefficient (weightedExtremizer weight coefficient) =
      weightedDualSq weight coefficient := by
  unfold finiteTrace weightedExtremizer weightedDualSq
  apply Finset.sum_congr rfl
  intro i hi
  field_simp [(weight_pos i).ne']

theorem weightedNormSq_weightedExtremizer
    (weight coefficient : Fin n → Real)
    (weight_pos : ∀ i, 0 < weight i) :
    weightedNormSq weight (weightedExtremizer weight coefficient) =
      weightedDualSq weight coefficient := by
  unfold weightedNormSq weightedExtremizer weightedDualSq
  apply Finset.sum_congr rfl
  intro i hi
  field_simp [(weight_pos i).ne']

/-- If the weighted dual square is nonzero, the bound is attained exactly. -/
theorem finiteTrace_bound_is_sharp
    (weight coefficient : Fin n → Real)
    (weight_pos : ∀ i, 0 < weight i) :
    finiteTrace coefficient (weightedExtremizer weight coefficient) ^ 2 =
      weightedDualSq weight coefficient *
        weightedNormSq weight (weightedExtremizer weight coefficient) := by
  rw [finiteTrace_weightedExtremizer weight coefficient weight_pos,
    weightedNormSq_weightedExtremizer weight coefficient weight_pos]
  ring

end FiniteWeightedTrace

end MariciFormal
