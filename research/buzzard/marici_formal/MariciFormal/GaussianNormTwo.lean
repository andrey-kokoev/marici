import Mathlib.Data.Matrix.Notation
import Mathlib.Tactic.NormNum
import Mathlib.Tactic.Ring

/-!
Integral two-dimensional core of Grothendieck's Gaussian norm-two
half-rotation correspondence. Smith cokernels, real unitary normalization,
and physical boundary realization remain external interfaces.
-/

namespace MariciFormal

open Matrix

def gaussianQuarterTurn : Matrix (Fin 2) (Fin 2) ℤ :=
  !![0, -1;
     1,  0]

def gaussianNormTwoMap : Matrix (Fin 2) (Fin 2) ℤ :=
  1 + gaussianQuarterTurn

theorem gaussianQuarterTurn_square :
    gaussianQuarterTurn * gaussianQuarterTurn =
      -(1 : Matrix (Fin 2) (Fin 2) ℤ) := by
  ext i j
  fin_cases i <;> fin_cases j <;>
    norm_num [gaussianQuarterTurn, Matrix.mul_apply, Fin.sum_univ_two]

/-- The integral half-rotation candidate squares to twice the quarter-turn. -/
theorem gaussianNormTwoMap_square :
    gaussianNormTwoMap * gaussianNormTwoMap = 2 • gaussianQuarterTurn := by
  ext i j
  fin_cases i <;> fin_cases j <;>
    norm_num [gaussianNormTwoMap, gaussianQuarterTurn, Matrix.mul_apply,
      Fin.sum_univ_two]

/-- The transpose norm of `1+J` is exactly two. -/
theorem gaussianNormTwoMap_transpose_mul :
    gaussianNormTwoMapᵀ * gaussianNormTwoMap =
      2 • (1 : Matrix (Fin 2) (Fin 2) ℤ) := by
  ext i j
  fin_cases i <;> fin_cases j <;>
    norm_num [gaussianNormTwoMap, gaussianQuarterTurn, Matrix.mul_apply,
      Fin.sum_univ_two]

theorem gaussianNormTwoMap_det : gaussianNormTwoMap.det = 2 := by
  norm_num [gaussianNormTwoMap, gaussianQuarterTurn, Matrix.det_fin_two]

end MariciFormal
