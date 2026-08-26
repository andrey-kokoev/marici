import Mathlib

/-!
Exact heat-time hostile contributed by a conjugate off-axis squared pole pair.

The fixture only proves that such a pair can contribute negatively.  It does
not assert that the completed Xi divisor contains an off-axis zero or that a
positive background cannot mask the order-zero sign.
-/

namespace MariciFormal

def offAxisPairHeatContribution (alpha beta t : Real) : Real :=
  2 * Real.exp ((alpha ^ 2 - beta ^ 2) * t) *
    Real.cos (2 * alpha * beta * t)

theorem offAxisPairHeatContribution_negative_fixture :
    offAxisPairHeatContribution 1 1 (Real.pi / 2) = -2 := by
  rw [offAxisPairHeatContribution]
  ring_nf
  rw [Real.exp_zero, Real.cos_pi]
  norm_num

/-- At time zero the same hostile is positive, so it cannot have a fixed
nonnegative spectral-heat interpretation merely from its initial value. -/
theorem offAxisPairHeatContribution_at_zero :
    offAxisPairHeatContribution 1 1 0 = 2 := by
  norm_num [offAxisPairHeatContribution]

end MariciFormal
