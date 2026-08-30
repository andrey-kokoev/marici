import Mathlib.Algebra.Ring.Hom.Defs

/-!
Concrete initial-semiring core of Grothendieck's Frobenius-rigidity packet.
Every unital semiring endomorphism of `Nat` is the identity, while the
nontrivial additive scaling maps do not preserve the unit.
-/

namespace MariciFormal

/-- Initiality of `Nat` makes its unital semiring endomorphism unique. -/
theorem nat_semiringEndomorphism_eq_identity
    (endomorphism : ℕ →+* ℕ) :
    endomorphism = RingHom.id ℕ := by
  ext n
  simp

def natScalingAddHom (scale : ℕ) : ℕ →+ ℕ where
  toFun n := scale * n
  map_zero' := by simp
  map_add' left right := by simp [mul_add]

theorem natScalingAddHom_comp
    (left right : ℕ) :
    (natScalingAddHom left).comp (natScalingAddHom right) =
      natScalingAddHom (left * right) := by
  ext n
  simp [natScalingAddHom, mul_assoc]

/-- The power-indexed additive scaling preserves the multiplicative unit
exactly in the trivial case. -/
theorem natScalingAddHom_preserves_one_iff (scale : ℕ) :
    natScalingAddHom scale 1 = 1 ↔ scale = 1 := by
  simp [natScalingAddHom]

theorem nontrivial_natScaling_is_not_unital
    (scale : ℕ) (hscale : scale ≠ 1) :
    natScalingAddHom scale 1 ≠ 1 := by
  exact (not_congr (natScalingAddHom_preserves_one_iff scale)).mpr hscale

end MariciFormal
