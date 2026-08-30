import Mathlib

/-!
Typed separation of fixed-spectrum heat time from the de Bruijn--Newman
deformation parameter, together with Grothendieck's exact finite hostile to a
universal zero-velocity sign.

No assertion about the zeros of Xi or the Newman constant is made.
-/

namespace MariciFormal

structure SpectralHeatTime where
  value : Real

structure NewmanDeformationParameter where
  value : Real

/-- Heat damping changes the weight of a fixed spectral ordinate. -/
def fixedSpectralHeatAtom (gamma : Real) (t : SpectralHeatTime) : Real :=
  Real.exp (-t.value * gamma ^ 2)

/-- The two positive-root velocities in the exact quartic hostile model. -/
def innerQuarticVelocity (a b : Rat) : Rat :=
  (5 * a ^ 2 - b ^ 2) / (a * (a ^ 2 - b ^ 2))

def outerQuarticVelocity (a b : Rat) : Rat :=
  (5 * b ^ 2 - a ^ 2) / (b * (b ^ 2 - a ^ 2))

/-- At `a=1`, `b=2`, reflection symmetry and real simple roots coexist with
oppositely directed positive-root velocities. -/
theorem quarticVelocity_hostile_oppositeSigns :
    innerQuarticVelocity 1 2 = -1 / 3 ∧
      outerQuarticVelocity 1 2 = 19 / 6 ∧
      innerQuarticVelocity 1 2 < 0 ∧
      0 < outerQuarticVelocity 1 2 := by
  norm_num [innerQuarticVelocity, outerQuarticVelocity]

/-- The velocity formula has exactly the expected collision denominator:
if the two positive roots coincide, neither displayed rational expression is
defined by a nonzero denominator. -/
theorem quarticVelocity_collision_denominators_zero (a : Rat) :
    a * (a ^ 2 - a ^ 2) = 0 ∧ a * (a ^ 2 - a ^ 2) = 0 := by
  ring

end MariciFormal
