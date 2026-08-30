import Mathlib

/-!
Universal Möbius and cocycle algebra for the Li feature family.

The construction is source-linear and independent of zero locations.  A
positive pairing, completed Weil-domain membership, and the arithmetic
explicit-formula comparison are deliberately not assumed.
-/

namespace MariciFormal

section Mobius

variable {K : Type*} [Field K]

def liMobiusCoordinate (s : K) : K := 1 - 1 / s

theorem liMobiusCoordinate_eq (s : K) :
    liMobiusCoordinate s = (s - 1) / s := by
  unfold liMobiusCoordinate
  ring

/-- Functional-equation reflection becomes inversion of the rigid Möbius
coordinate. -/
theorem liMobiusCoordinate_reflection
    (s : K) (hs : s ≠ 0) (hs1 : 1 - s ≠ 0) :
    liMobiusCoordinate (1 - s) = (liMobiusCoordinate s)⁻¹ := by
  unfold liMobiusCoordinate
  field_simp
  ring

/-- The inverse-square endpoint factor is the product of the two Möbius
coboundaries; it is forced rather than chosen degree by degree. -/
theorem liMobius_coboundary_product
    (s : K) (hs : s ≠ 0) (hs1 : 1 - s ≠ 0) :
    (1 - liMobiusCoordinate s) *
        (1 - (liMobiusCoordinate s)⁻¹) = 1 / (s * (1 - s)) := by
  unfold liMobiusCoordinate
  field_simp
  ring

end Mobius

section Cocycle

variable {R : Type*} [CommRing R]

def liCocycleFeature (u : R) (n : Nat) : R := 1 - u ^ n

/-- One uniform feature family obeys the additive cocycle law for
multiplicative iterates of `u`. -/
theorem liCocycleFeature_add
    (u : R) (m n : Nat) :
    liCocycleFeature u (m + n) =
      liCocycleFeature u m + u ^ m * liCocycleFeature u n := by
  unfold liCocycleFeature
  rw [pow_add]
  ring

theorem liCocycleFeature_zero (u : R) : liCocycleFeature u 0 = 0 := by
  simp [liCocycleFeature]

end Cocycle

end MariciFormal
