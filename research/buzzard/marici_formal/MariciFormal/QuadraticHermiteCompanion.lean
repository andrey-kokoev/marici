import Mathlib.Data.Matrix.Notation
import Mathlib.Tactic.FinCases
import Mathlib.Tactic.Ring

/-!
Degree-two coefficient core of Grothendieck's canonical Hermite companion
realization.  Symmetry is derived from the Newton recurrence; positivity is
kept separate and is explicitly false for the polynomial `z^2 + 1`.
-/

namespace MariciFormal

open Matrix

section QuadraticHermite

variable {R : Type*} [CommRing R]

def quadraticCompanion (a₀ a₁ : R) : Matrix (Fin 2) (Fin 2) R :=
  !![0, -a₀;
     1, -a₁]

def quadraticHermite (s₀ s₁ s₂ : R) : Matrix (Fin 2) (Fin 2) R :=
  !![s₀, s₁;
     s₁, s₂]

/-- The first coefficient recurrence is exactly what makes the quadratic
companion symmetric for its coefficient-derived Hankel/Hermite form. -/
theorem quadraticHermite_companion_symmetry
    (a₀ a₁ s₀ s₁ s₂ : R)
    (hrecurrence : s₂ = -a₀ * s₀ - a₁ * s₁) :
    quadraticHermite s₀ s₁ s₂ * quadraticCompanion a₀ a₁ =
      (quadraticCompanion a₀ a₁)ᵀ * quadraticHermite s₀ s₁ s₂ := by
  ext i j
  fin_cases i <;> fin_cases j <;>
    simp [quadraticHermite, quadraticCompanion, Matrix.mul_apply,
      hrecurrence] <;> ring

end QuadraticHermite

section QuadraticHermiteHostile

def nonrealPairCompanion : Matrix (Fin 2) (Fin 2) ℚ :=
  quadraticCompanion 1 0

def nonrealPairHermite : Matrix (Fin 2) (Fin 2) ℚ :=
  quadraticHermite 2 0 (-2)

theorem nonrealPair_companion_symmetric_for_Hermite :
    nonrealPairHermite * nonrealPairCompanion =
      nonrealPairCompanionᵀ * nonrealPairHermite := by
  exact quadraticHermite_companion_symmetry 1 0 2 0 (-2) (by norm_num)

def negativeHermiteDirection : Fin 2 → ℚ
  | 0 => 0
  | 1 => 1

theorem negativeHermiteDirection_ne_zero : negativeHermiteDirection ≠ 0 := by
  intro hzero
  have hatOne := congrFun hzero (1 : Fin 2)
  norm_num [negativeHermiteDirection] at hatOne

/-- Companion symmetry does not imply positivity: the coefficient data for
`z^2 + 1` gives an explicit negative Hermite direction. -/
theorem nonrealPair_Hermite_has_negative_direction :
    dotProduct negativeHermiteDirection
      (nonrealPairHermite *ᵥ negativeHermiteDirection) = -2 := by
  norm_num [negativeHermiteDirection, nonrealPairHermite, quadraticHermite,
    Matrix.mulVec, dotProduct]

end QuadraticHermiteHostile

end MariciFormal
