import Mathlib.Tactic

/-!
Finite algebraic core of Grothendieck's odd-source skew-adjoint mechanism.
Closed convolution operators, Fourier transforms, and Xi spectral
identification remain external analytic interfaces.
-/

namespace MariciFormal

section OddKernel

variable {X R : Type*} [AddCommGroup R]

def OddUnder (involution : X → X) (kernel : X → R) : Prop :=
  ∀ x, kernel (involution x) = -kernel x

/-- At a fixed point of the involution, an odd coefficient is two-torsion. -/
theorem odd_fixed_point_is_two_torsion
    (involution : X → X) (kernel : X → R)
    (hodd : OddUnder involution kernel) {x : X}
    (hfixed : involution x = x) :
    2 • kernel x = 0 := by
  have hneg : kernel x = -kernel x := by
    rw [← hfixed]
    exact hodd x
  simpa [two_nsmul] using congrArg (fun value ↦ value + kernel x) hneg

/-- Over a coefficient group without two-torsion, oddness forces every
involution-fixed coefficient to vanish. -/
theorem odd_fixed_point_eq_zero
    (involution : X → X) (kernel : X → R)
    (hodd : OddUnder involution kernel)
    (hnoTwoTorsion : ∀ value : R, 2 • value = 0 → value = 0)
    {x : X} (hfixed : involution x = x) :
    kernel x = 0 :=
  hnoTwoTorsion _ (odd_fixed_point_is_two_torsion involution kernel hodd hfixed)

/-- The nonidentity element of `C2`, modeled additively by `ZMod 2`, is its
own inverse; a rational odd kernel therefore vanishes there. -/
theorem c2_odd_direction_vanishes
    (kernel : ZMod 2 → ℚ)
    (hodd : ∀ x, kernel (-x) = -kernel x) :
    kernel 1 = 0 := by
  apply odd_fixed_point_eq_zero (fun x : ZMod 2 ↦ -x) kernel hodd
  · intro value hvalue
    norm_num [two_nsmul] at hvalue ⊢
    linarith
  · norm_num

end OddKernel

end MariciFormal
