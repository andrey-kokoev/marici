import MariciFormal.FiniteCharacterOrthogonality
import MariciFormal.FiniteCharacterCompleteness
import Mathlib.Tactic

/-!
Invariant spectral reconstruction of finite convolution from the complete
finite-abelian character basis.
-/

namespace MariciFormal

open scoped BigOperators

variable {G : Type*} [Fintype G] [AddCommGroup G]

/-- Finite convolution bundled as a complex linear operator. -/
noncomputable def complexFiniteConvolutionLinearMap (kernel : G → ℂ) :
    (G → ℂ) →ₗ[ℂ] (G → ℂ) where
  toFun vector := complexFiniteConvolution kernel vector
  map_add' first second := by
    funext x
    simp [complexFiniteConvolution, mul_add, Finset.sum_add_distrib]
  map_smul' scalar vector := by
    funext x
    simp [complexFiniteConvolution, Finset.mul_sum, mul_assoc, mul_comm,
      mul_left_comm]

/-- The diagonal operator reconstructed from the character eigenvalues. -/
noncomputable def finiteCharacterDiagonalOperator (kernel : G → ℂ) :
    (G → ℂ) →ₗ[ℂ] (G → ℂ) :=
  (AddChar.complexBasis G).constr ℂ fun character =>
    complexCharacterEigenvalue kernel character • (character : G → ℂ)

/-- Finite convolution is exactly the unique operator diagonal on the complete
character basis with the Fourier coefficients as eigenvalues. -/
theorem complexFiniteConvolution_eq_characterDiagonal
    (kernel : G → ℂ) :
    complexFiniteConvolutionLinearMap kernel =
      finiteCharacterDiagonalOperator kernel := by
  apply (AddChar.complexBasis G).ext
  intro character
  rw [finiteCharacterDiagonalOperator, Module.Basis.constr_basis]
  rw [AddChar.complexBasis_apply]
  funext x
  change complexFiniteConvolution kernel character x =
    complexCharacterEigenvalue kernel character * character x
  exact complexFiniteConvolution_apply_character kernel character x

end MariciFormal
