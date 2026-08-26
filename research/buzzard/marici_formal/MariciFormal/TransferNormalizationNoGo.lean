import Mathlib.Tactic

/-!
Scalar core of Grothendieck's transfer-normalization selector no-go.
Splitting a degree-`d` pull--push norm forces scale `1/d`, while preserving a
distinguished delta selector forces scale `1`.
-/

namespace MariciFormal

variable {K : Type*} [Field K]

/-- For nontrivial invertible degree, norm splitting and delta preservation
cannot be satisfied by one scalar transfer normalization. -/
theorem no_scalar_transfer_normalization
    (degree scale : K) (hdegree : degree ≠ 1)
    (hsplitsNorm : scale * degree = 1)
    (hpreservesSelector : scale = 1) : False := by
  rw [hpreservesSelector, one_mul] at hsplitsNorm
  exact hdegree hsplitsNorm

theorem scalar_splitting_forces_inverse
    (degree scale : K) (hdegree : degree ≠ 0)
    (hsplitsNorm : scale * degree = 1) :
    scale = degree⁻¹ := by
  apply (mul_right_cancel₀ hdegree)
  simpa [hsplitsNorm]

/-- Exact degree-two scalar fixture. -/
theorem degree_two_normalizations_are_incompatible :
    ¬ ∃ scale : ℚ, scale * 2 = 1 ∧ scale = 1 := by
  rintro ⟨scale, hsplit, hselector⟩
  exact no_scalar_transfer_normalization (2 : ℚ) scale (by norm_num)
    hsplit hselector

end MariciFormal
