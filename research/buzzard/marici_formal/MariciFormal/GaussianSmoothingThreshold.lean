import Mathlib.Analysis.SpecialFunctions.Hyperbolic.Basic
import Mathlib.Tactic

/-!
Finite scalar core of Grothendieck's signed three-atom Gaussian-smoothing
hostile.  The analytic substitution `r = exp (-1 / (4 * sigma))` and the
completed Weil distribution remain external interfaces.
-/

namespace MariciFormal

/-- After factoring out the positive central Gaussian, the signed measure
`delta_{-1} + delta_1 - delta_0` has this bracket. -/
def threeAtomGaussianBracket (r x : ℝ) : ℝ :=
  2 * r * Real.cosh x - 1

theorem threeAtomGaussianBracket_nonnegative
    (r x : ℝ) (hr : 1 / 2 ≤ r) :
    0 ≤ threeAtomGaussianBracket r x := by
  have hr0 : 0 ≤ 2 * r := by linarith
  have hcosh : 0 ≤ Real.cosh x - 1 := by
    linarith [Real.one_le_cosh x]
  have hproduct : 0 ≤ (2 * r) * (Real.cosh x - 1) :=
    mul_nonneg hr0 hcosh
  unfold threeAtomGaussianBracket
  nlinarith

theorem threeAtomGaussianBracket_at_zero (r : ℝ) :
    threeAtomGaussianBracket r 0 = 2 * r - 1 := by
  simp [threeAtomGaussianBracket]

/-- The bracket is nonnegative at every character exactly at and above the
half-amplitude threshold. -/
theorem threeAtomGaussianBracket_nonnegative_iff (r : ℝ) :
    (∀ x : ℝ, 0 ≤ threeAtomGaussianBracket r x) ↔ 1 / 2 ≤ r := by
  constructor
  · intro hall
    have hzero := hall 0
    rw [threeAtomGaussianBracket_at_zero] at hzero
    linarith
  · intro hr x
    exact threeAtomGaussianBracket_nonnegative r x hr

/-- Below the threshold the center is an explicit negative witness. -/
theorem threeAtomGaussianBracket_center_hostile
    (r : ℝ) (hr : r < 1 / 2) :
    threeAtomGaussianBracket r 0 < 0 := by
  rw [threeAtomGaussianBracket_at_zero]
  linarith

end MariciFormal
