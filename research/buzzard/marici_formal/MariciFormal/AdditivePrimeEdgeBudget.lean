import Mathlib.Algebra.BigOperators.Group.Finset.Basic
import Mathlib.Data.Real.Basic
import Mathlib.Tactic

/-!
Finite Walsh-spectrum core of Grothendieck's additive prime-edge budget.
This file does not identify a completed Weil form or supply archimedean energy.
-/

namespace MariciFormal

open scoped BigOperators

variable {ι : Type*} [Fintype ι]

/-- A Boolean polarity chooses either the positive or negative contribution of
one real edge coefficient. -/
def signedEdge (coefficient : ℝ) (negative : Bool) : ℝ :=
  if negative then -coefficient else coefficient

/-- Walsh eigenvalue of the identity-plus-single-edge kernel on a finite
Boolean cube. -/
def additiveEdgeEigenvalue (coefficient : ι → ℝ) (polarity : ι → Bool) : ℝ :=
  1 + ∑ i, signedEdge (coefficient i) (polarity i)

def oppositePolarity (coefficient : ι → ℝ) (i : ι) : Bool :=
  decide (0 ≤ coefficient i)

theorem signedEdge_oppositePolarity (coefficient : ι → ℝ) (i : ι) :
    signedEdge (coefficient i) (oppositePolarity coefficient i) =
      -|coefficient i| := by
  by_cases h : 0 ≤ coefficient i
  · simp [signedEdge, oppositePolarity, h, abs_of_nonneg h]
  · have hneg : coefficient i < 0 := lt_of_not_ge h
    simp [signedEdge, oppositePolarity, h, abs_of_neg hneg]

theorem negative_abs_le_signedEdge (coefficient : ℝ) (negative : Bool) :
    -|coefficient| ≤ signedEdge coefficient negative := by
  cases negative <;> simp [signedEdge, neg_abs_le, le_abs_self]

/-- Every Walsh eigenvalue is nonnegative exactly when all visible edges fit
inside one shared `l1` contraction budget. -/
theorem additiveEdgeSpectrum_nonnegative_iff (coefficient : ι → ℝ) :
    (∀ polarity : ι → Bool,
        0 ≤ additiveEdgeEigenvalue coefficient polarity) ↔
      ∑ i, |coefficient i| ≤ 1 := by
  constructor
  · intro hspectrum
    have hopposite := hspectrum (oppositePolarity coefficient)
    have hsum :
        (∑ i, signedEdge (coefficient i) (oppositePolarity coefficient i)) =
          -(∑ i, |coefficient i|) := by
      rw [Finset.sum_neg_distrib]
      apply Finset.sum_congr rfl
      intro i hi
      exact signedEdge_oppositePolarity coefficient i
    rw [additiveEdgeEigenvalue, hsum] at hopposite
    linarith
  · intro hbudget polarity
    have hterm : ∀ i : ι,
        -|coefficient i| ≤ signedEdge (coefficient i) (polarity i) :=
      fun i => negative_abs_le_signedEdge (coefficient i) (polarity i)
    have hsum :
        ∑ i, -|coefficient i| ≤
          ∑ i, signedEdge (coefficient i) (polarity i) := by
      exact Finset.sum_le_sum fun i hi => hterm i
    rw [Finset.sum_neg_distrib] at hsum
    simp only [additiveEdgeEigenvalue]
    linarith

/-- Two individually contractive edges need not fit the shared budget. -/
theorem twoEdge_individual_bounds_do_not_glue :
    |(3 / 5 : ℝ)| ≤ 1 ∧ |(3 / 5 : ℝ)| ≤ 1 ∧
      additiveEdgeEigenvalue (fun _ : Fin 2 => (3 / 5 : ℝ))
        (fun _ => true) < 0 := by
  norm_num [additiveEdgeEigenvalue, signedEdge, Fin.sum_univ_two]

end MariciFormal
