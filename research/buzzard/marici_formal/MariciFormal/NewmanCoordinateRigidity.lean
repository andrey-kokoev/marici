import Mathlib.Tactic

/-!
Pairwise algebraic core of Grothendieck's Newman coordinate-change anomaly and
affine-conjugacy rigidity. Differentiability and integration are external.
-/

namespace MariciFormal

section PairwiseRigidity

variable {K : Type*} [Field K]

/-- Cross-multiplied form of preservation of the inverse-gap law up to one
global time factor. -/
def PairConjugatesInverseGap
    (timeFactor : K) (derivative transformed : K → K) (x y : K) : Prop :=
  derivative x * (transformed x - transformed y) =
    timeFactor * (x - y)

/-- Applying the same pair law in both orientations forces equal derivative
values whenever the transformed points are distinct. -/
theorem pairConjugacy_forces_equal_derivative
    (timeFactor : K) (derivative transformed : K → K) (x y : K)
    (hxy : PairConjugatesInverseGap timeFactor derivative transformed x y)
    (hyx : PairConjugatesInverseGap timeFactor derivative transformed y x)
    (htransformed : transformed x ≠ transformed y) :
    derivative x = derivative y := by
  have hproduct :
      (derivative x - derivative y) *
        (transformed x - transformed y) = 0 := by
    unfold PairConjugatesInverseGap at hxy hyx
    linear_combination hxy + hyx
  have hderivative : derivative x - derivative y = 0 :=
    (mul_eq_zero.mp hproduct).resolve_right (sub_ne_zero.mpr htransformed)
  exact sub_eq_zero.mp hderivative

/-- A globally injective coordinate satisfying the pair law has constant
declared derivative. Turning this into an affine-function theorem requires the
analytic derivative interface. -/
theorem universalPairConjugacy_forces_constant_derivative
    (timeFactor : K) (derivative transformed : K → K)
    (hinjective : Function.Injective transformed)
    (hpair : ∀ x y, x ≠ y →
      PairConjugatesInverseGap timeFactor derivative transformed x y) :
    ∀ x y, derivative x = derivative y := by
  intro x y
  by_cases hxy : x = y
  · simpa [hxy]
  · apply pairConjugacy_forces_equal_derivative timeFactor derivative transformed x y
    · exact hpair x y hxy
    · exact hpair y x (Ne.symm hxy)
    · exact hinjective.ne hxy

end PairwiseRigidity

section MobilityAnomaly

def mobilityCoordinateAnomalyTerm
    (derivative : ℚ → ℚ) (transformed : ℚ → ℚ)
    (x y : ℚ) : ℚ :=
  derivative x / (x - y) -
    derivative x ^ 2 / (transformed x - transformed y)

def affineCoordinate (slope intercept : ℚ) (x : ℚ) : ℚ :=
  slope * x + intercept

theorem affine_mobilityAnomaly_vanishes
    (slope intercept x y : ℚ) (hslope : slope ≠ 0) (hxy : x ≠ y) :
    mobilityCoordinateAnomalyTerm (fun _ => slope)
      (affineCoordinate slope intercept) x y = 0 := by
  have hdenominator :
      affineCoordinate slope intercept x - affineCoordinate slope intercept y =
        slope * (x - y) := by
    simp [affineCoordinate]
    ring
  unfold mobilityCoordinateAnomalyTerm
  rw [hdenominator]
  field_simp [hslope, hxy]
  ring

def squareCoordinate (x : ℚ) : ℚ := x ^ 2

def squareCoordinateDerivative (x : ℚ) : ℚ := 2 * x

/-- A genuinely nonlinear coordinate has a nonzero mobility anomaly already
on one two-root packet. -/
theorem nonlinear_coordinate_anomaly_hostile :
    mobilityCoordinateAnomalyTerm squareCoordinateDerivative squareCoordinate
      1 2 = -2 / 3 := by
  norm_num [mobilityCoordinateAnomalyTerm, squareCoordinate,
    squareCoordinateDerivative]

end MobilityAnomaly

end MariciFormal
