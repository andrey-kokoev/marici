import Mathlib.Analysis.Fourier.FiniteAbelian.PontryaginDuality
import Mathlib.Tactic

/-!
Finite-abelian character completeness for Grothendieck's squarefree Walsh
packet. This module supplies the Fourier basis but does not identify an
arithmetic kernel as Hermitian or positive semidefinite.
-/

namespace MariciFormal

open scoped BigOperators

variable {G : Type*} [Fintype G] [AddCommGroup G]

/-- Complex additive characters form a complete basis on every finite
abelian group. -/
noncomputable def finiteCharacterBasis :
    Basis (AddChar G ℂ) ℂ (G → ℂ) :=
  AddChar.complexBasis G

theorem finiteCharacterBasis_apply (character : AddChar G ℂ) :
    finiteCharacterBasis character = (character : G → ℂ) := by
  exact AddChar.complexBasis_apply character

theorem finiteCharacter_count :
    Fintype.card (AddChar G ℂ) = Fintype.card G := by
  exact AddChar.card_eq

def complexFiniteConvolution (kernel vector : G → ℂ) (x : G) : ℂ :=
  ∑ y, kernel y * vector (x - y)

def complexCharacterEigenvalue
    (kernel : G → ℂ) (character : AddChar G ℂ) : ℂ :=
  ∑ y, kernel y * (character y)⁻¹

/-- The complete character basis diagonalizes finite convolution. -/
theorem complexFiniteConvolution_apply_character
    (kernel : G → ℂ) (character : AddChar G ℂ) (x : G) :
    complexFiniteConvolution kernel character x =
      complexCharacterEigenvalue kernel character * character x := by
  unfold complexFiniteConvolution complexCharacterEigenvalue
  calc
    (∑ y, kernel y * character (x - y)) =
        ∑ y, character x * (kernel y * (character y)⁻¹) := by
      apply Finset.sum_congr rfl
      intro y hy
      rw [AddChar.map_sub_eq_div]
      simp only [div_eq_mul_inv]
      ring
    _ = character x * ∑ y, kernel y * (character y)⁻¹ := by
      rw [Finset.mul_sum]
    _ = (∑ y, kernel y * (character y)⁻¹) * character x := by ring

/-- Any vector has unique coordinates in the finite character basis. -/
theorem finiteCharacterBasis_repr_injective :
    Function.Injective (finiteCharacterBasis (G := G)).repr :=
  (finiteCharacterBasis (G := G)).repr.injective

end MariciFormal
