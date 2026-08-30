import Mathlib.Analysis.SpecialFunctions.Trigonometric.DerivHyp
import Mathlib.Tactic.NormNum

/-!
Sign core of Grothendieck's two-copy sinh/cosine defect-velocity formula.
The radial sign is universal; the relative-coordinate cosine sign is not.
-/

namespace MariciFormal

def radialSinhWeight (y S : ℝ) : ℝ :=
  S * Real.sinh (y * S)

/-- For outward height `y ≥ 0`, the sum-coordinate radial weight is always
nonnegative. -/
theorem radialSinhWeight_nonnegative
    (y S : ℝ) (hy : 0 ≤ y) :
    0 ≤ radialSinhWeight y S := by
  unfold radialSinhWeight
  rcases le_total 0 S with hS | hS
  · exact mul_nonneg hS
      (Real.sinh_nonneg_iff.mpr (mul_nonneg hy hS))
  · exact mul_nonneg_of_nonpos_of_nonpos hS
      (Real.sinh_nonpos_iff.mpr (mul_nonpos_of_nonneg_of_nonpos hy hS))

theorem radialSinhWeight_positive
    (y S : ℝ) (hy : 0 < y) (hS : S ≠ 0) :
    0 < radialSinhWeight y S := by
  unfold radialSinhWeight
  rcases lt_or_gt_of_ne hS with hSneg | hSpos
  · exact mul_pos_of_neg_of_neg hSneg
      (Real.sinh_neg_iff.mpr (mul_neg_of_pos_of_neg hy hSneg))
  · exact mul_pos hSpos
      (Real.sinh_pos_iff.mpr (mul_pos hy hSpos))

def cosineReadout (x D : ℝ) : ℝ :=
  Real.cos (x * D)

/-- A positive one-point source weight can have a negative cosine readout.
Thus radial positivity does not imply fixed-sum Fourier positivity. -/
theorem positive_source_negative_cosine_band :
    (0 : ℝ) < 1 ∧ cosineReadout 1 Real.pi < 0 := by
  constructor
  · norm_num
  · simp [cosineReadout]

/-- Even a strictly positive radial weight can be reversed by the relative
coordinate oscillation. -/
theorem positive_radial_weight_negative_product :
    radialSinhWeight 1 1 * cosineReadout 1 Real.pi < 0 := by
  have hsinh : 0 < Real.sinh 1 := Real.sinh_pos_iff.mpr (by norm_num)
  simpa [radialSinhWeight, cosineReadout] using neg_lt_zero.mpr hsinh

end MariciFormal
