import Mathlib.Data.Matrix.Notation
import Mathlib.Data.Polynomial.Eval.Defs
import Mathlib.LinearAlgebra.Matrix.Determinant.Basic
import Mathlib.LinearAlgebra.Matrix.Hermitian
import Mathlib.Tactic

/-!
Smallest polynomial obstruction in Grothendieck's finite-cutoff Pfaffian
no-go. A general Pfaffian API is not assumed.
-/

namespace MariciFormal

open Matrix Polynomial

/-- Scalar transfer determinant `det(1-C*C)` for `C=[X]`. -/
def scalarTransferDefect : ℝ[X] := 1 - X ^ 2

@[simp]
theorem scalarTransferDefect_eval (x : ℝ) :
    scalarTransferDefect.eval x = 1 - x ^ 2 := by
  simp [scalarTransferDefect]

theorem scalarTransferDefect_positive_of_abs_lt_one
    (x : ℝ) (hcontractive : |x| < 1) :
    0 < scalarTransferDefect.eval x := by
  rw [scalarTransferDefect_eval]
  rcases abs_lt.mp hcontractive with ⟨hleft, hright⟩
  nlinarith

/-- The scalar transfer defect is not a polynomial square. Evaluation at two
already contradicts nonnegativity of real squares. -/
theorem scalarTransferDefect_not_polynomial_square :
    ¬ ∃ squareRoot : ℝ[X], squareRoot ^ 2 = scalarTransferDefect := by
  rintro ⟨squareRoot, hsquare⟩
  have heval := congrArg (Polynomial.eval (2 : ℝ)) hsquare
  simp [scalarTransferDefect] at heval
  nlinarith [sq_nonneg (squareRoot.eval 2)]

/-- The canonical two-by-two skew doubling of a scalar. -/
def scalarSkewDoubling {R : Type*} [Ring R]
    (entry : R) : Matrix (Fin 2) (Fin 2) R :=
  !![0, entry; -entry, 0]

theorem scalarSkewDoubling_isSkewAdjoint (entry : ℝ) :
    (scalarSkewDoubling entry).IsSkewAdjoint := by
  ext i j
  fin_cases i <;> fin_cases j <;> simp [scalarSkewDoubling]

/-- Skew doubling squares its scalar entry at the determinant level. -/
theorem scalarSkewDoubling_det {R : Type*} [CommRing R] (entry : R) :
    (scalarSkewDoubling entry).det = entry ^ 2 := by
  simp [scalarSkewDoubling, Matrix.det_fin_two]
  ring

/-- Consequently, inserting the transfer defect itself into the doubled block
produces its square, not a polynomial square root. -/
theorem scalarSkewDoubling_transferDefect_det :
    (scalarSkewDoubling scalarTransferDefect).det =
      scalarTransferDefect ^ 2 := by
  exact scalarSkewDoubling_det scalarTransferDefect

end MariciFormal
