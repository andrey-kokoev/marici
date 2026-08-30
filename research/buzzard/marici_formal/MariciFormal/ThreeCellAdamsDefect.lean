import Mathlib.Analysis.Complex.Basic
import Mathlib.Data.Matrix.Notation
import Mathlib.LinearAlgebra.Matrix.Determinant.Basic
import Mathlib.LinearAlgebra.Matrix.Hermitian
import Mathlib.Tactic

/-!
Complex scalar determinant and defect identity for Grothendieck's three-cell
Adams positivity packet. Operator-valued Parrott completion is not assumed.
-/

namespace MariciFormal

open Matrix

/-- The normalized Hermitian three-cell Gram matrix. -/
def threeCellGramMatrix (a b c : ℂ) : Matrix (Fin 3) (Fin 3) ℂ :=
  !![1, a, c;
     conj a, 1, b;
     conj c, conj b, 1]

theorem threeCellGramMatrix_isHermitian (a b c : ℂ) :
    (threeCellGramMatrix a b c).IsHermitian := by
  ext i j
  fin_cases i <;> fin_cases j <;> simp [threeCellGramMatrix]

/-- Determinant expression of the normalized Hermitian three-cell Gram matrix
with consecutive correlations `a`, `b` and direct correlation `c`. -/
def threeCellGramDeterminant (a b c : ℂ) : ℝ :=
  1 - Complex.normSq a - Complex.normSq b - Complex.normSq c +
    2 * (a * b * conj c).re

/-- The actual matrix determinant is the complex coercion of the real scalar
determinant expression. -/
theorem threeCellGramMatrix_det (a b c : ℂ) :
    (threeCellGramMatrix a b c).det =
      (threeCellGramDeterminant a b c : ℂ) := by
  apply Complex.ext
  · simp [threeCellGramMatrix, Matrix.det_fin_three,
      threeCellGramDeterminant, Complex.normSq_apply, Complex.mul_re,
      Complex.mul_im, Complex.conj_re, Complex.conj_im]
    ring
  · simp [threeCellGramMatrix, Matrix.det_fin_three,
      threeCellGramDeterminant, Complex.normSq_apply, Complex.mul_re,
      Complex.mul_im, Complex.conj_re, Complex.conj_im]
    ring

/-- Exact completion of the determinant square. -/
theorem threeCellGramDeterminant_defect_identity (a b c : ℂ) :
    threeCellGramDeterminant a b c =
      (1 - Complex.normSq a) * (1 - Complex.normSq b) -
        Complex.normSq (c - a * b) := by
  simp only [threeCellGramDeterminant, Complex.normSq_apply,
    Complex.mul_re, Complex.mul_im, Complex.conj_re, Complex.conj_im,
    Complex.sub_re, Complex.sub_im]
  ring

/-- Nonnegative three-cell determinant is exactly contractivity of the direct
composition defect against the two local contraction deficiencies. -/
theorem threeCellGramDeterminant_nonnegative_iff (a b c : ℂ) :
    0 ≤ threeCellGramDeterminant a b c ↔
      Complex.normSq (c - a * b) ≤
        (1 - Complex.normSq a) * (1 - Complex.normSq b) := by
  rw [threeCellGramDeterminant_defect_identity]
  linarith

/-- Exact Adams composition has zero defect and leaves the product of the two
local contraction deficiencies. -/
theorem exactAdams_threeCellGramDeterminant (a b : ℂ) :
    threeCellGramDeterminant a b (a * b) =
      (1 - Complex.normSq a) * (1 - Complex.normSq b) := by
  rw [threeCellGramDeterminant_defect_identity]
  simp

theorem exactAdams_threeCell_nonnegative
    (a b : ℂ) (ha : Complex.normSq a ≤ 1)
    (hb : Complex.normSq b ≤ 1) :
    0 ≤ threeCellGramDeterminant a b (a * b) := by
  rw [exactAdams_threeCellGramDeterminant]
  exact mul_nonneg (sub_nonneg.mpr ha) (sub_nonneg.mpr hb)

/-- Separate edge contraction does not control an arbitrary direct edge. -/
theorem threeCell_uncontrolled_direct_edge_hostile :
    Complex.normSq (1 / 2 : ℂ) ≤ 1 ∧
      Complex.normSq (1 / 2 : ℂ) ≤ 1 ∧
      threeCellGramDeterminant (1 / 2) (1 / 2) (-1) < 0 := by
  norm_num [threeCellGramDeterminant, Complex.normSq_apply]

end MariciFormal
