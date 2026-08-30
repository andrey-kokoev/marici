import Mathlib.Data.Matrix.Notation
import Mathlib.Tactic.NormNum
import Mathlib.Tactic.Ring

/-!
Finite algebraic core of Grothendieck's three-height Pick correlation gate.
The theta-source inequalities needed to instantiate the correlations are not
assumed here.
-/

namespace MariciFormal

open Matrix

section CorrelationTriangle

variable {R : Type*} [CommRing R]

def correlationTriangleMatrix (r12 r13 r23 : R) :
    Matrix (Fin 3) (Fin 3) R :=
  !![1, r12, r13;
     r12, 1, r23;
     r13, r23, 1]

/-- The normalized three-height determinant is the correlation-triangle
polynomial. -/
theorem correlationTriangleMatrix_det (r12 r13 r23 : R) :
    (correlationTriangleMatrix r12 r13 r23).det =
      1 + 2 * r12 * r13 * r23 - r12 ^ 2 - r13 ^ 2 - r23 ^ 2 := by
  simp [correlationTriangleMatrix, Matrix.det_fin_three]
  ring

end CorrelationTriangle

/-- Pairwise correlations can all lie in the unit interval while the
three-by-three correlation determinant is negative. -/
theorem pairwise_bounds_do_not_force_triangle :
    let r12 : ℚ := 1
    let r13 : ℚ := 1
    let r23 : ℚ := 0
    (0 ≤ r12 ∧ r12 ≤ 1) ∧
      (0 ≤ r13 ∧ r13 ≤ 1) ∧
      (0 ≤ r23 ∧ r23 ≤ 1) ∧
      (correlationTriangleMatrix r12 r13 r23).det < 0 := by
  norm_num [correlationTriangleMatrix, Matrix.det_fin_three]

/-- Grothendieck's exact edgewise-contraction hostile: every two-cell minor
is `7/16`, but the three-cell determinant is `-49/32`. -/
theorem negative_three_quarter_triangle_hostile :
    let r : ℚ := -3 / 4
    1 - r ^ 2 = 7 / 16 ∧
      (correlationTriangleMatrix r r r).det = -49 / 32 := by
  norm_num [correlationTriangleMatrix, Matrix.det_fin_three]

end MariciFormal
