import Mathlib.Analysis.SpecialFunctions.Trigonometric.Basic
import Mathlib.Tactic.Positivity

/-!
One-prime phase-distance core of Grothendieck's valuation Dirichlet-energy
no-go. The energy is positive and phase-sensitive, but this file does not
identify its global zero set with any spectral divisor.
-/

namespace MariciFormal

def primePhaseEnergy (radius phase : ℝ) : ℝ :=
  2 * radius * (1 - Real.cos phase) / (1 - radius ^ 2)

theorem primePhaseEnergy_nonnegative
    (radius phase : ℝ) (hradius : 0 ≤ radius) (hcontractive : radius < 1) :
    0 ≤ primePhaseEnergy radius phase := by
  have hdenominator : 0 < 1 - radius ^ 2 := by
    nlinarith [sq_nonneg radius]
  have hcos : 0 ≤ 1 - Real.cos phase := by
    linarith [Real.neg_one_le_cos phase, Real.cos_le_one phase]
  unfold primePhaseEnergy
  positivity

theorem primePhaseEnergy_eq_zero_iff_cos_eq_one
    (radius phase : ℝ) (hradius : 0 < radius) (hcontractive : radius < 1) :
    primePhaseEnergy radius phase = 0 ↔ Real.cos phase = 1 := by
  have hdenominator : 1 - radius ^ 2 ≠ 0 := by
    have : 0 < 1 - radius ^ 2 := by nlinarith [sq_nonneg radius]
    exact ne_of_gt this
  unfold primePhaseEnergy
  rw [div_eq_zero_iff]
  simp [hdenominator, hradius.ne', sub_eq_zero]

/-- The reference phase vanishes exactly. -/
theorem primePhaseEnergy_zero_phase (radius : ℝ) :
    primePhaseEnergy radius 0 = 0 := by
  simp [primePhaseEnergy]

end MariciFormal
