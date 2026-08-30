import Mathlib.Tactic

/-!
Polynomial sign core of Grothendieck's primitive-scale susceptibility packet.
The theta moment derivation of this response and the nonlinear primitive
scale constraint remain external interfaces.
-/

namespace MariciFormal

def cubicScaleSusceptibility (scale : ℚ) : ℚ :=
  -112 * scale ^ 2 * (10 * scale ^ 3 - 27 * scale ^ 2 + 5)

/-- A sufficiently separated reciprocal scale orbit points out of the cubic
positive cone; scale three is an exact rational hostile. -/
theorem cubicScaleSusceptibility_three_negative :
    cubicScaleSusceptibility 3 < 0 := by
  norm_num [cubicScaleSusceptibility]

/-- The response vanishes at the undeformed scale parameter zero. -/
theorem cubicScaleSusceptibility_zero :
    cubicScaleSusceptibility 0 = 0 := by
  norm_num [cubicScaleSusceptibility]

end MariciFormal
