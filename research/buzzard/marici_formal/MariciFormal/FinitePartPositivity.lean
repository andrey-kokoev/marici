import Mathlib

/-!
Finite-part extraction does not preserve positivity: a nonnegative regulated
Laurent expression can have a negative constant coefficient.
-/

namespace MariciFormal

/-- The three coefficients of `pole * ε⁻² + constant + tail * ε²`. -/
structure SymmetricLaurentWindow where
  pole : Real
  constant : Real
  tail : Real

noncomputable def SymmetricLaurentWindow.evaluate
    (window : SymmetricLaurentWindow) (epsilon : Real) : Real :=
  window.pole / epsilon ^ 2 + window.constant + window.tail * epsilon ^ 2

def SymmetricLaurentWindow.finitePart
    (window : SymmetricLaurentWindow) : Real :=
  window.constant

/-- The literal regulated square `(ε⁻¹-ε)²`. -/
def squareWindow : SymmetricLaurentWindow where
  pole := 1
  constant := -2
  tail := 1

theorem squareWindow_evaluate_eq_square
    {epsilon : Real} (epsilon_ne_zero : epsilon ≠ 0) :
    squareWindow.evaluate epsilon = (epsilon⁻¹ - epsilon) ^ 2 := by
  unfold SymmetricLaurentWindow.evaluate squareWindow
  field_simp [epsilon_ne_zero]
  ring

theorem squareWindow_pointwise_nonnegative
    (epsilon : Real) (epsilon_ne_zero : epsilon ≠ 0) :
    0 ≤ squareWindow.evaluate epsilon := by
  rw [squareWindow_evaluate_eq_square epsilon_ne_zero]
  exact sq_nonneg _

theorem squareWindow_finitePart_negative :
    squareWindow.finitePart = -2 ∧ squareWindow.finitePart < 0 := by
  norm_num [SymmetricLaurentWindow.finitePart, squareWindow]

/-- Positivity of every regulated value does not orient the finite-part quotient. -/
theorem finitePartExtraction_not_positivity_preserving :
    ∃ window : SymmetricLaurentWindow,
      (∀ epsilon : Real, epsilon ≠ 0 → 0 ≤ window.evaluate epsilon) ∧
      window.finitePart < 0 := by
  exact ⟨squareWindow, squareWindow_pointwise_nonnegative,
    squareWindow_finitePart_negative.2⟩

end MariciFormal
