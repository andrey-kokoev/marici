import Mathlib.Tactic.FieldSimp
import Mathlib.Tactic.Ring

/-!
Algebraic factorization of the first coupled two-height Pick determinant from
Grothendieck's Xi packet. Theta monotonicity and Stieltjes consequences remain
separate analytic inputs.
-/

namespace MariciFormal

variable {K : Type*} [Field K]

def twoHeightPickDeterminant
    (a₁ a₂ y₁ y₂ : K) : K :=
  a₁ * a₂ / (y₁ * y₂) - (a₁ + a₂) ^ 2 / (y₁ + y₂) ^ 2

/-- Clearing the positive-height denominators factors the determinant into
the two scalar monotonicity channels. -/
theorem twoHeightPickDeterminant_factorization
    (a₁ a₂ y₁ y₂ : K)
    (hy₁ : y₁ ≠ 0) (hy₂ : y₂ ≠ 0) (hsum : y₁ + y₂ ≠ 0) :
    y₁ * y₂ * (y₁ + y₂) ^ 2 *
        twoHeightPickDeterminant a₁ a₂ y₁ y₂ =
      (y₁ * a₂ - y₂ * a₁) * (y₁ * a₁ - y₂ * a₂) := by
  unfold twoHeightPickDeterminant
  field_simp [hy₁, hy₂, hsum]
  ring

end MariciFormal
