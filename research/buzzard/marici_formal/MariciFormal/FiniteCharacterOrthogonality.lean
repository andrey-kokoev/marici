import MariciFormal.FiniteCharacterSynthesis
import Mathlib.Analysis.Fourier.FiniteAbelian.Orthogonality
import Mathlib.Data.Matrix.Basic

/-!
Normalized orthogonality of the complete finite-abelian character family.
The normalization is the uniform average over the finite group.
-/

namespace MariciFormal

variable {G : Type*} [Fintype G] [AddCommGroup G]

/-- Uniformly normalized character Gram matrix. -/
noncomputable def finiteCharacterNormalizedGram :
    Matrix (AddChar G ℂ) (AddChar G ℂ) ℂ :=
  fun first second =>
    ⟪(first : G → ℂ), (second : G → ℂ)⟫ₙ_[ℂ]

/-- The complete character family is orthonormal for the uniform finite-group
inner product. -/
theorem finiteCharacters_weighted_orthonormal
    (first second : AddChar G ℂ) :
    ⟪(first : G → ℂ), (second : G → ℂ)⟫ₙ_[ℂ] =
      if first = second then 1 else 0 := by
  exact AddChar.wInner_cWeight_eq_boole first second

/-- Equivalently, the normalized character Gram matrix is the identity. -/
theorem finiteCharacterNormalizedGram_eq_one :
    finiteCharacterNormalizedGram (G := G) = 1 := by
  classical
  ext first second
  rw [finiteCharacterNormalizedGram,
    finiteCharacters_weighted_orthonormal]
  simp [Matrix.one_apply]

/-- Distinct characters have zero normalized overlap. -/
theorem distinctCharacters_weighted_inner_zero
    {first second : AddChar G ℂ} (hne : first ≠ second) :
    ⟪(first : G → ℂ), (second : G → ℂ)⟫ₙ_[ℂ] = 0 := by
  rw [finiteCharacters_weighted_orthonormal, if_neg hne]

end MariciFormal
