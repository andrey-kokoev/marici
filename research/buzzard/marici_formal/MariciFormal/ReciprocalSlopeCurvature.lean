import Mathlib

/-!
Exact algebra shared by the central reciprocal-slope and diagonal Loewner
curvature packets.  Analytic differentiability and every source sign are
separate inputs.
-/

namespace MariciFormal

section CurvatureAlgebra

variable {K : Type*} [LinearOrderedField K]

def reciprocalSlopeCurvatureNumerator (g gPrime gSecond : K) : K :=
  2 * g * gSecond - 3 * gPrime ^ 2

def diagonalLoewnerCurvature (g gPrime gSecond : K) : K :=
  g * gSecond / 6 - gPrime ^ 2 / 4

theorem reciprocalSlopeNumerator_eq_twelveLoewner
    (g gPrime gSecond : K) :
    reciprocalSlopeCurvatureNumerator g gPrime gSecond =
      12 * diagonalLoewnerCurvature g gPrime gSecond := by
  unfold reciprocalSlopeCurvatureNumerator diagonalLoewnerCurvature
  ring

theorem reciprocalSlopeNumerator_nonnegative_iff
    (g gPrime gSecond : K) :
    0 ≤ reciprocalSlopeCurvatureNumerator g gPrime gSecond ↔
      0 ≤ diagonalLoewnerCurvature g gPrime gSecond := by
  rw [reciprocalSlopeNumerator_eq_twelveLoewner]
  constructor <;> intro h
  · nlinarith
  · exact mul_nonneg (by norm_num) h

/-- Positive slope alone leaves the coupled curvature sign undetermined. -/
theorem positiveSlope_does_not_force_curvature :
    0 < (1 : Rat) ∧
      reciprocalSlopeCurvatureNumerator (1 : Rat) 1 1 < 0 := by
  norm_num [reciprocalSlopeCurvatureNumerator]

end CurvatureAlgebra

end MariciFormal
