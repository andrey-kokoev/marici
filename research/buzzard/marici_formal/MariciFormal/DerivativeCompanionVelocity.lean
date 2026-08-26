import Mathlib.Tactic.NormNum
import Mathlib.Tactic.Ring

/-!
Coordinate algebra of Grothendieck's derivative companion and oriented defect
velocity. Holomorphic differentiation and arithmetic sign are separate
interfaces.
-/

namespace MariciFormal

section CoordinateIdentity

variable {R : Type*} [CommRing R]

abbrev ComplexCoordinates (R : Type*) := R × R

/-- Coordinates of `A + iD`, where `D` is intended to be `A'`. -/
def orientedDerivativeCompanion
    (A D : ComplexCoordinates R) : ComplexCoordinates R :=
  (A.1 - D.2, A.2 + D.1)

/-- Coordinates of `A - iD`. -/
def reflectedDerivativeCompanion
    (A D : ComplexCoordinates R) : ComplexCoordinates R :=
  (A.1 + D.2, A.2 - D.1)

def coordinateNormSq (z : ComplexCoordinates R) : R :=
  z.1 * z.1 + z.2 * z.2

/-- Twice the coordinate expression for the vertical derivative of `|A|²`
when the analytic interface supplies `∂_y A = iD`. -/
def verticalNormVelocity
    (A D : ComplexCoordinates R) : R :=
  2 * (-A.1 * D.2 + A.2 * D.1)

/-- The two oriented sectors have symmetric sum `2A`; no division by two or
characteristic assumption is needed. -/
theorem oriented_add_reflected_eq_two_source
    (A D : ComplexCoordinates R) :
    (orientedDerivativeCompanion A D).1 +
          (reflectedDerivativeCompanion A D).1 = 2 * A.1 ∧
      (orientedDerivativeCompanion A D).2 +
          (reflectedDerivativeCompanion A D).2 = 2 * A.2 := by
  constructor <;>
    simp [orientedDerivativeCompanion, reflectedDerivativeCompanion] <;>
    ring

/-- Exact coordinate form of
`|A+iD|²-|A-iD|² = 2 ∂_y |A|²`. -/
theorem derivativeCompanion_norm_difference
    (A D : ComplexCoordinates R) :
    coordinateNormSq (orientedDerivativeCompanion A D) -
        coordinateNormSq (reflectedDerivativeCompanion A D) =
      2 * verticalNormVelocity A D := by
  simp [coordinateNormSq, orientedDerivativeCompanion,
    reflectedDerivativeCompanion, verticalNormVelocity]
  ring

end CoordinateIdentity

section SimpleCrossing

variable {R : Type*} [CommRing R] [Nontrivial R]

/-- At a real simple crossing `A=0`, the oriented companion retains the
nonzero derivative direction. -/
theorem oriented_companion_survives_simple_real_crossing
    (d : R) (hd : d ≠ 0) :
    orientedDerivativeCompanion (R := R) (0, 0) (d, 0) ≠ (0, 0) := by
  intro h
  have himag := congrArg Prod.snd h
  simp [orientedDerivativeCompanion] at himag
  exact hd himag

end SimpleCrossing

section OrientationHostile

/-- The canonical companion construction permits negative vertical velocity;
its Hermite--Biehler sign is additional source information. -/
theorem derivative_companion_can_have_negative_velocity :
    verticalNormVelocity (R := ℤ) (1, 0) (0, 1) = -2 ∧
      coordinateNormSq (orientedDerivativeCompanion (R := ℤ) (1, 0) (0, 1)) -
          coordinateNormSq
            (reflectedDerivativeCompanion (R := ℤ) (1, 0) (0, 1)) = -4 := by
  norm_num [verticalNormVelocity, coordinateNormSq,
    orientedDerivativeCompanion, reflectedDerivativeCompanion]

end OrientationHostile

end MariciFormal
