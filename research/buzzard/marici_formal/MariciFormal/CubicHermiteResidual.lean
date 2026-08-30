import Mathlib.Tactic.NormNum
import Mathlib.Tactic.Positivity
import Mathlib.Tactic.Ring

/-!
Finite polynomial core and two-orbit hostile from Grothendieck's cubic
Poisson--Hermite energy audit.
-/

namespace MariciFormal

section ResidualPolynomial

variable {R : Type*} [CommRing R]

def cubicQuadraticReserve (z3 z4 z5 : R) : R :=
  9 * z4 ^ 2 - 7 * z3 * z5

def cubicPointedChannel (z2 z3 z4 z5 : R) : R :=
  35 * z2 * z5 ^ 2 + 162 * z4 ^ 3 - 189 * z3 * z4 * z5

def cubicHermiteResidual (z2 z3 z4 z5 : R) : R :=
  36 * cubicQuadraticReserve z3 z4 z5 ^ 3 -
    cubicPointedChannel z2 z3 z4 z5 ^ 2

/-- A single positive atomic scale has positive residual, with its exact
homogeneous factor exposed. -/
theorem single_scale_residual_identity (w y : R) :
    cubicQuadraticReserve (w * y ^ 3) (w * y ^ 4) (w * y ^ 5) =
        2 * w ^ 2 * y ^ 8 ∧
      cubicPointedChannel (w * y ^ 2) (w * y ^ 3)
          (w * y ^ 4) (w * y ^ 5) = 8 * w ^ 3 * y ^ 12 ∧
      cubicHermiteResidual (w * y ^ 2) (w * y ^ 3)
          (w * y ^ 4) (w * y ^ 5) = 224 * w ^ 6 * y ^ 24 := by
  constructor
  · simp [cubicQuadraticReserve]
    ring
  constructor
  · simp [cubicPointedChannel]
    ring
  · simp [cubicHermiteResidual, cubicQuadraticReserve,
      cubicPointedChannel]
    ring

end ResidualPolynomial

section OrderedSingleScale

theorem single_positive_scale_residual_positive
    (w y : ℝ) (hw : 0 < w) (hy : 0 < y) :
    0 < cubicHermiteResidual (w * y ^ 2) (w * y ^ 3)
      (w * y ^ 4) (w * y ^ 5) := by
  rw [(single_scale_residual_identity w y).2.2]
  positivity

end OrderedSingleScale

section TwoOrbitHostile

def twoOrbitLeadingPacket : Fin 4 → ℤ
  | 0 => 1027
  | 1 => 1081
  | 2 => 1243
  | 3 => 1729

theorem twoOrbit_quadratic_reserve_positive :
    cubicQuadraticReserve (twoOrbitLeadingPacket 1)
      (twoOrbitLeadingPacket 2) (twoOrbitLeadingPacket 3) = 822098 := by
  norm_num [twoOrbitLeadingPacket, cubicQuadraticReserve]

theorem twoOrbit_pointed_channel_negative :
    cubicPointedChannel (twoOrbitLeadingPacket 0)
      (twoOrbitLeadingPacket 1) (twoOrbitLeadingPacket 2)
      (twoOrbitLeadingPacket 3) = -20514280744 := by
  norm_num [twoOrbitLeadingPacket, cubicPointedChannel]

/-- The exact integer packet preserves the quadratic layer but violates the
final cubic Hermite residual. -/
theorem twoOrbit_cubic_residual_negative :
    cubicHermiteResidual (twoOrbitLeadingPacket 0)
      (twoOrbitLeadingPacket 1) (twoOrbitLeadingPacket 2)
      (twoOrbitLeadingPacket 3) = -400833721223554606624 := by
  norm_num [twoOrbitLeadingPacket, cubicHermiteResidual,
    cubicQuadraticReserve, cubicPointedChannel]

end TwoOrbitHostile

section PolarizedObstruction

def orbitMoment (t : ℕ) (lambda : ℤ) : ℤ :=
  1 + lambda * 3 ^ t

theorem polarized_quadratic_reserve (lambda : ℤ) :
    cubicQuadraticReserve (orbitMoment 3 lambda) (orbitMoment 4 lambda)
      (orbitMoment 5 lambda) =
        2 - 432 * lambda + 13122 * lambda ^ 2 := by
  norm_num [orbitMoment, cubicQuadraticReserve]
  ring

theorem polarized_pointed_channel (lambda : ℤ) :
    cubicPointedChannel (orbitMoment 2 lambda) (orbitMoment 3 lambda)
      (orbitMoment 4 lambda) (orbitMoment 5 lambda) =
        8 - 9648 * lambda + 34992 * lambda ^ 2 +
          4251528 * lambda ^ 3 := by
  norm_num [orbitMoment, cubicPointedChannel]
  ring

theorem polarized_cubic_residual (lambda : ℤ) :
    cubicHermiteResidual (orbitMoment 2 lambda) (orbitMoment 3 lambda)
      (orbitMoment 4 lambda) (orbitMoment 5 lambda) =
        224 - 32256 * lambda - 47664288 * lambda ^ 2 -
          4744075392 * lambda ^ 3 + 382484464992 * lambda ^ 4 -
          8331090195456 * lambda ^ 5 + 63264216171744 * lambda ^ 6 := by
  norm_num [orbitMoment, cubicHermiteResidual, cubicQuadraticReserve,
    cubicPointedChannel]
  ring

end PolarizedObstruction

end MariciFormal
