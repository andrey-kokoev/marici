import Mathlib

/-!
Regular gauge factors preserve the local vanishing order of a determinant
coordinate; singular factors can counterfeit extra multiplicity.
-/

namespace MariciFormal

open Polynomial

def seamVanishingOrder (p : Rat[X]) : Nat := p.natTrailingDegree

theorem regularGauge_preserves_vanishingOrder
    (character determinant : Rat[X])
    (hCharacterConstant : character.coeff 0 ≠ 0)
    (hDeterminant : determinant ≠ 0) :
    seamVanishingOrder (character * determinant) =
      seamVanishingOrder determinant := by
  change (character * determinant).natTrailingDegree =
    determinant.natTrailingDegree
  have hCharacter : character ≠ 0 := by
    intro h
    apply hCharacterConstant
    simp [h]
  rw [Polynomial.natTrailingDegree_mul hCharacter hDeterminant]
  have hOrder : character.natTrailingDegree = 0 :=
    Polynomial.natTrailingDegree_eq_zero.mpr (.inr hCharacterConstant)
  simp [hOrder]

theorem singularQuadraticFactor_adds_two
    (determinant : Rat[X]) (hDeterminant : determinant ≠ 0) :
    seamVanishingOrder (X ^ 2 * determinant) =
      seamVanishingOrder determinant + 2 := by
  change (X ^ 2 * determinant).natTrailingDegree =
    determinant.natTrailingDegree + 2
  rw [Polynomial.natTrailingDegree_mul (pow_ne_zero 2 Polynomial.X_ne_zero)
      hDeterminant,
    Polynomial.natTrailingDegree_X_pow]
  omega

noncomputable def determinantGerm : Rat[X] := X ^ 4 * (1 + 2 * X ^ 2)

noncomputable def regularCharacterGerm : Rat[X] := 3 + X ^ 2

noncomputable def singularCharacterGerm : Rat[X] := X ^ 2

theorem determinantGerm_order : seamVanishingOrder determinantGerm = 4 := by
  have hFactor : (1 + 2 * X ^ 2 : Rat[X]) ≠ 0 := by
    intro h
    have hCoeff := congrArg (fun p : Rat[X] => p.coeff 0) h
    norm_num at hCoeff
  change (X ^ 4 * (1 + 2 * X ^ 2) : Rat[X]).natTrailingDegree = 4
  rw [Polynomial.natTrailingDegree_mul (pow_ne_zero 4 Polynomial.X_ne_zero)
      hFactor,
    Polynomial.natTrailingDegree_X_pow]
  have hConstant : (1 + 2 * X ^ 2 : Rat[X]).coeff 0 ≠ 0 := by norm_num
  rw [Polynomial.natTrailingDegree_eq_zero.mpr (.inr hConstant)]

theorem regularGaugeFixture :
    seamVanishingOrder (regularCharacterGerm * determinantGerm) = 4 := by
  have hCharacter : regularCharacterGerm.coeff 0 ≠ 0 := by
    norm_num [regularCharacterGerm]
  have hDeterminant : determinantGerm ≠ 0 := by
    intro h
    have hOrder := determinantGerm_order
    simp [h, seamVanishingOrder] at hOrder
  rw [regularGauge_preserves_vanishingOrder regularCharacterGerm determinantGerm
    hCharacter hDeterminant, determinantGerm_order]

theorem singularGaugeFixture :
    seamVanishingOrder (singularCharacterGerm * determinantGerm) = 6 := by
  have hDeterminant : determinantGerm ≠ 0 := by
    intro h
    have hOrder := determinantGerm_order
    simp [h, seamVanishingOrder] at hOrder
  change seamVanishingOrder (X ^ 2 * determinantGerm) = 6
  rw [singularQuadraticFactor_adds_two determinantGerm hDeterminant,
    determinantGerm_order]

/-- Dropping regularity permits a presentation factor to manufacture depth. -/
theorem vanishingOrder_requires_regularGauge :
    ∃ character determinant : Rat[X],
      determinant ≠ 0 ∧ character.coeff 0 = 0 ∧
      seamVanishingOrder (character * determinant) ≠
        seamVanishingOrder determinant := by
  refine ⟨singularCharacterGerm, determinantGerm, ?_, ?_, ?_⟩
  · intro h
    have hOrder := determinantGerm_order
    simp [h, seamVanishingOrder] at hOrder
  · norm_num [singularCharacterGerm]
  · rw [determinantGerm_order, singularGaugeFixture]
    norm_num

end MariciFormal
