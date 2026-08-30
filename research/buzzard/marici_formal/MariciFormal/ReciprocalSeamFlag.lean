import Mathlib.Data.Complex.Basic
import Mathlib.Tactic

/-!
Finite scalar core of Grothendieck's reciprocal-double invariant-flag theorem.
The direct and reciprocal weights can share a nonzero invariant covector only
when the centered spectral parameter lies on the imaginary seam.
-/

namespace MariciFormal

/-- Equality of the direct and reciprocal-conjugate weights is exactly the
centered critical seam. -/
theorem conjugate_eq_negative_iff_realPart_zero (z : ℂ) :
    star z = -z ↔ z.re = 0 := by
  constructor
  · intro h
    have hre := congrArg Complex.re h
    simp at hre
    linarith
  · intro hre
    apply Complex.ext
    · simp [hre]
    · simp

/-- If both sheet coefficients of a constant invariant covector are nonzero,
their two eigenvalue equations force the centered parameter onto the seam. -/
theorem reciprocalInvariantWeights_force_seam
    (z α a b : ℂ) (ha : a ≠ 0) (hb : b ≠ 0)
    (hdirect : (-z) * a = α * a)
    (hreciprocal : (star z) * b = α * b) :
    z.re = 0 := by
  have hdirectWeight : -z = α := mul_right_cancel₀ ha hdirect
  have hreciprocalWeight : star z = α :=
    mul_right_cancel₀ hb hreciprocal
  apply (conjugate_eq_negative_iff_realPart_zero z).1
  exact hreciprocalWeight.trans hdirectWeight.symm

/-- The shared forcing coefficient vanishes precisely on the antisymmetric
sheet line. -/
theorem sharedForcing_cancel_iff_antisymmetric (a b : ℂ) :
    a + b = 0 ↔ b = -a := by
  constructor
  · exact eq_neg_of_add_eq_zero_left
  · intro h
    rw [h, add_neg_cancel]

/-- Off the seam there is no invariant covector with both sheets visible. -/
theorem offSeam_forbids_twoSheetInvariantWeights
    (z : ℂ) (hoffSeam : z.re ≠ 0) :
    ¬ ∃ α a b : ℂ,
      a ≠ 0 ∧ b ≠ 0 ∧
        (-z) * a = α * a ∧ (star z) * b = α * b := by
  rintro ⟨α, a, b, ha, hb, hdirect, hreciprocal⟩
  exact hoffSeam
    (reciprocalInvariantWeights_force_seam
      z α a b ha hb hdirect hreciprocal)

end MariciFormal
