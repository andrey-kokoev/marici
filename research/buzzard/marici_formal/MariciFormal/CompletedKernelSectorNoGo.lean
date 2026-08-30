import Mathlib

/-!
The primewise diagonal obstruction in the completed Herglotz kernel.

This theorem is local to one explicitly supplied positive coefficient and
positive real evaluation point.  It does not define the von Mangoldt series
or assert positivity of the completed endpoint--gamma--prime kernel.
-/

namespace MariciFormal

/-- Diagonal contribution of one negative exponential prime channel. -/
def primeChannelDiagonal (coefficient rate x : Real) : Real :=
  -coefficient * Real.exp (-x * rate) / x

theorem primeChannelDiagonal_strictly_negative
    {coefficient rate x : Real} (hcoefficient : 0 < coefficient)
    (hx : 0 < x) :
    primeChannelDiagonal coefficient rate x < 0 := by
  unfold primeChannelDiagonal
  have hexp : 0 < Real.exp (-x * rate) := Real.exp_pos _
  exact div_neg_of_neg_of_pos (mul_neg_of_neg_of_pos (neg_neg_of_pos hcoefficient) hexp) hx

end MariciFormal
