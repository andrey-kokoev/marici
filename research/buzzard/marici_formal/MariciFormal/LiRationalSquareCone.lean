import Mathlib.Tactic.FieldSimp
import Mathlib.Tactic.NormNum
import Mathlib.Tactic.Ring

/-!
Algebraic pullback core of Grothendieck's Li rational-square test cone.
Arithmetic explicit-formula positivity is deliberately not assumed.
-/

namespace MariciFormal

section AlgebraicCone

variable {K : Type*} [Field K]

def liCoordinate (s : K) : K :=
  (s - 1) / s

theorem liCoordinate_reflection
    (s : K) (hs : s ≠ 0) (hreflected : 1 - s ≠ 0) :
    liCoordinate (1 - s) = (liCoordinate s)⁻¹ := by
  have hsone : s ≠ 1 := by
    intro h
    apply hreflected
    simp [h]
  have hsm1 : s - 1 ≠ 0 := sub_ne_zero.mpr hsone
  field_simp [liCoordinate, hs, hreflected, hsm1] <;> ring

/-- The inverse-square weight is the coboundary of the rigid coordinate. -/
theorem liCoordinate_coboundary_weight
    (s : K) (hs : s ≠ 0) (hreflected : 1 - s ≠ 0) :
    (1 - liCoordinate s) * (1 - (liCoordinate s)⁻¹) =
      1 / (s * (1 - s)) := by
  have hsone : s ≠ 1 := by
    intro h
    apply hreflected
    simp [h]
  have hsm1 : s - 1 ≠ 0 := sub_ne_zero.mpr hsone
  field_simp [liCoordinate, hs, hreflected, hsm1] <;> ring

/-- `p` may be polynomial evaluation, but reflection invariance uses only its
being one fixed function on the coordinate algebra. -/
def liRationalSquareTest (p : K → K) (s : K) : K :=
  p (liCoordinate s) * p ((liCoordinate s)⁻¹) /
    (s * (1 - s))

theorem liRationalSquareTest_reflection
    (p : K → K) (s : K) (hs : s ≠ 0) (hreflected : 1 - s ≠ 0) :
    liRationalSquareTest p (1 - s) = liRationalSquareTest p s := by
  unfold liRationalSquareTest
  rw [liCoordinate_reflection s hs hreflected, inv_inv]
  ring

end AlgebraicCone

section PositivityAuthorityHostile

def constantPolynomialEvaluation : ℚ → ℚ := fun _ => 1

theorem constant_test_at_center :
    liRationalSquareTest constantPolynomialEvaluation (1 / 2 : ℚ) = 4 := by
  norm_num [liRationalSquareTest, liCoordinate,
    constantPolynomialEvaluation]

/-- A negative linear readout on the same algebraic test proves that
reflection-invariant square construction alone does not authorize positivity
of the arithmetic functional. -/
def hostileConeReadout : ℚ →ₗ[ℚ] ℚ :=
  -(LinearMap.id : ℚ →ₗ[ℚ] ℚ)

theorem hostileConeReadout_is_negative_on_constant_test :
    hostileConeReadout
        (liRationalSquareTest constantPolynomialEvaluation (1 / 2 : ℚ)) < 0 := by
  norm_num [hostileConeReadout, liRationalSquareTest, liCoordinate,
    constantPolynomialEvaluation]

end PositivityAuthorityHostile

end MariciFormal
