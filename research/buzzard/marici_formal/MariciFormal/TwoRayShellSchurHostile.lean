import Mathlib.Data.Complex.Basic
import Mathlib.Tactic.FieldSimp
import Mathlib.Tactic.NormNum
import Mathlib.Tactic.Ring

/-!
Finite two-ray hostile from Grothendieck's shell Schur-determinant packet.
The native determinant retains the oriented phase product and is not the
positive leakage Gram correction.
-/

namespace MariciFormal

def twoRayAverage (z₁ z₂ : ℂ) : ℂ := (z₁ + z₂) / 2

def twoRayDifference (z₁ z₂ : ℂ) : ℂ := (z₁ - z₂) / 2

/-- The determinant of the constant/difference-basis height block is the
oriented product of the two ray phases. -/
theorem twoRay_native_determinant
    (z₁ z₂ : ℂ) :
    twoRayAverage z₁ z₂ ^ 2 - twoRayDifference z₁ z₂ ^ 2 = z₁ * z₂ := by
  simp [twoRayAverage, twoRayDifference]
  ring

/-- When the retained average is invertible, its Schur factor reconstructs
the same native determinant. -/
theorem twoRay_schur_reconstructs_native_determinant
    (z₁ z₂ : ℂ) (haverage : twoRayAverage z₁ z₂ ≠ 0) :
    twoRayAverage z₁ z₂ *
        (twoRayAverage z₁ z₂ -
          twoRayDifference z₁ z₂ ^ 2 / twoRayAverage z₁ z₂) =
      z₁ * z₂ := by
  rw [mul_sub, mul_div_cancel₀ _ haverage]
  exact twoRay_native_determinant z₁ z₂

def twoRayPositiveLeakage (z₁ z₂ : ℂ) : ℂ :=
  1 + twoRayDifference z₁ z₂ *
    Complex.conj (twoRayDifference z₁ z₂)

/-- At phases `1` and `i`, the native determinant is `i` whereas the positive
leakage correction is `3/2`; the latter cannot replace the former. -/
theorem one_i_native_and_leakage_hostile :
    twoRayAverage 1 Complex.I ^ 2 -
          twoRayDifference 1 Complex.I ^ 2 = Complex.I ∧
      twoRayPositiveLeakage 1 Complex.I = (3 / 2 : ℂ) ∧
      Complex.I ≠ (3 / 2 : ℂ) := by
  constructor
  · simpa using twoRay_native_determinant (1 : ℂ) Complex.I
  constructor
  · norm_num [twoRayPositiveLeakage, twoRayDifference, Complex.conj_I]
    ring
  · intro h
    have him := congrArg Complex.im h
    norm_num at him

end MariciFormal
