import Mathlib.Data.Real.Basic
import Mathlib.Tactic

/-!
Rational-parametrization core of Grothendieck's rank-one Parseval phase no-go.
No Riemann--Siegel or Xi phase is assumed.
-/

namespace MariciFormal

def parsevalCosineCoordinate (u : ℝ) : ℝ :=
  (1 - u ^ 2) / (1 + u ^ 2)

def parsevalSineCoordinate (u : ℝ) : ℝ :=
  2 * u / (1 + u ^ 2)

theorem one_add_sq_pos (u : ℝ) : 0 < 1 + u ^ 2 := by positivity

/-- Every real input produces a normalized rank-one Parseval pair. -/
theorem rationalParseval_identity (u : ℝ) :
    parsevalCosineCoordinate u ^ 2 +
      parsevalSineCoordinate u ^ 2 = 1 := by
  unfold parsevalCosineCoordinate parsevalSineCoordinate
  field_simp [ne_of_gt (one_add_sq_pos u)]
  ring

/-- The oriented complement has exactly the arbitrarily supplied input zero
set; Parseval normalization does not restrict it. -/
theorem parsevalSineCoordinate_eq_zero_iff (u : ℝ) :
    parsevalSineCoordinate u = 0 ↔ u = 0 := by
  unfold parsevalSineCoordinate
  rw [div_eq_zero_iff]
  simp [ne_of_gt (one_add_sq_pos u)]

/-- Reversing the inserted phase coordinate preserves the Parseval cosine and
the squared defect while reversing the oriented determinant. -/
theorem parseval_orientation_reversal (u : ℝ) :
    parsevalCosineCoordinate (-u) = parsevalCosineCoordinate u ∧
      parsevalSineCoordinate (-u) = -parsevalSineCoordinate u ∧
      parsevalSineCoordinate (-u) ^ 2 =
        parsevalSineCoordinate u ^ 2 := by
  constructor
  · simp [parsevalCosineCoordinate]
  constructor
  · simp [parsevalSineCoordinate]
  · simp [parsevalSineCoordinate]

/-- Two inputs with different zero behavior both satisfy the same Parseval
condition, giving the smallest hostile countermodel to zero-set discrimination. -/
theorem rankOneParseval_zeroSet_hostile :
    parsevalCosineCoordinate 0 ^ 2 + parsevalSineCoordinate 0 ^ 2 = 1 ∧
      parsevalCosineCoordinate 1 ^ 2 + parsevalSineCoordinate 1 ^ 2 = 1 ∧
      parsevalSineCoordinate 0 = 0 ∧
      parsevalSineCoordinate 1 ≠ 0 := by
  norm_num [parsevalCosineCoordinate, parsevalSineCoordinate]

end MariciFormal
