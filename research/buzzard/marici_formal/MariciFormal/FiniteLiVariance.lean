import MariciFormal.WeightedRigging
import Mathlib.Tactic.Nlinarith

/-!
Finite positive-measure core of Grothendieck's degree-two Li determinant as
a spectral variance.
-/

namespace MariciFormal

open Finset
open scoped BigOperators

section FiniteVariance

variable {n : ℕ}

def weightedMass (weight : Fin n → ℝ) : ℝ :=
  ∑ i, weight i

def weightedFirstMoment (weight coordinate : Fin n → ℝ) : ℝ :=
  ∑ i, weight i * coordinate i

def weightedSecondMoment (weight coordinate : Fin n → ℝ) : ℝ :=
  ∑ i, weight i * coordinate i ^ 2

/-- For a cosine coordinate, `cos(2θ) = 2 cos(θ)^2 - 1`. -/
def degreeTwoCosMoment (weight coordinate : Fin n → ℝ) : ℝ :=
  2 * weightedSecondMoment weight coordinate - weightedMass weight

def degreeTwoLiDeterminant (weight coordinate : Fin n → ℝ) : ℝ :=
  weightedMass weight *
      (weightedMass weight + degreeTwoCosMoment weight coordinate) -
    2 * weightedFirstMoment weight coordinate ^ 2

theorem degreeTwoLiDeterminant_eq_twice_varianceNumerator
    (weight coordinate : Fin n → ℝ) :
    degreeTwoLiDeterminant weight coordinate =
      2 * (weightedMass weight * weightedSecondMoment weight coordinate -
        weightedFirstMoment weight coordinate ^ 2) := by
  unfold degreeTwoLiDeterminant degreeTwoCosMoment
  ring

theorem weightedDual_self_eq_mass
    (weight : Fin n → ℝ) (hweight : ∀ i, 0 < weight i) :
    weightedDualSq weight weight = weightedMass weight := by
  unfold weightedDualSq weightedMass
  apply Finset.sum_congr rfl
  intro i hi
  field_simp [(hweight i).ne']

theorem degreeTwoLiDeterminant_nonneg
    (weight coordinate : Fin n → ℝ) (hweight : ∀ i, 0 < weight i) :
    0 ≤ degreeTwoLiDeterminant weight coordinate := by
  rw [degreeTwoLiDeterminant_eq_twice_varianceNumerator]
  have hcs := finiteTrace_sq_le_weightedDualSq_mul_weightedNormSq
    weight weight coordinate hweight
  rw [weightedDual_self_eq_mass weight hweight] at hcs
  change weightedFirstMoment weight coordinate ^ 2 ≤
    weightedMass weight * weightedSecondMoment weight coordinate at hcs
  nlinarith

end FiniteVariance

/-- A concentrated cosine coordinate has zero determinant, while two
opposite cosine coordinates have strictly positive determinant. -/
theorem degreeTwoLiDeterminant_concentrated_and_spread_controls :
    degreeTwoLiDeterminant (n := 2) (fun _ => 1) (fun _ => 1) = 0 ∧
      degreeTwoLiDeterminant (n := 2) (fun _ => 1)
        (fun i => if i = 0 then -1 else 1) = 8 := by
  norm_num [degreeTwoLiDeterminant, degreeTwoCosMoment, weightedMass,
    weightedFirstMoment, weightedSecondMoment, Fin.sum_univ_two]

end MariciFormal
