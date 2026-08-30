import Mathlib.Data.Complex.Basic
import Mathlib.Tactic

/-!
Finite Gram-orientation and aggregation core of Grothendieck's reciprocal
quarter-density overlap audit. Infinite series and theta amplitudes are external.
-/

namespace MariciFormal

section RealGram

def selfEnergy2 (x₀ x₁ : ℝ) : ℝ := x₀ ^ 2 + x₁ ^ 2

def crossOverlap2 (u₀ u₁ v₀ v₁ : ℝ) : ℝ :=
  u₀ * v₀ + u₁ * v₁

theorem gramDet_lagrange_identity (u₀ u₁ v₀ v₁ : ℝ) :
    selfEnergy2 u₀ u₁ * selfEnergy2 v₀ v₁ -
        crossOverlap2 u₀ u₁ v₀ v₁ ^ 2 =
      (u₀ * v₁ - u₁ * v₀) ^ 2 := by
  simp [selfEnergy2, crossOverlap2]
  ring

theorem gram_principal_data_nonnegative (u₀ u₁ v₀ v₁ : ℝ) :
    0 ≤ selfEnergy2 u₀ u₁ ∧
      0 ≤ selfEnergy2 v₀ v₁ ∧
      0 ≤ selfEnergy2 u₀ u₁ * selfEnergy2 v₀ v₁ -
        crossOverlap2 u₀ u₁ v₀ v₁ ^ 2 := by
  constructor
  · simp [selfEnergy2]
    positivity
  constructor
  · simp [selfEnergy2]
    positivity
  · rw [gramDet_lagrange_identity]
    positivity

/-- Two nonzero positive-energy feature vectors can have exactly zero cross
overlap while the Gram determinant stays positive. -/
theorem orthogonal_positiveGram_hostile :
    selfEnergy2 1 1 = 2 ∧
      selfEnergy2 1 (-1) = 2 ∧
      crossOverlap2 1 1 1 (-1) = 0 ∧
      selfEnergy2 1 1 * selfEnergy2 1 (-1) -
        crossOverlap2 1 1 1 (-1) ^ 2 = 4 := by
  norm_num [selfEnergy2, crossOverlap2]

end RealGram

section ReciprocalConjugacy

/-- Reciprocal conjugacy still permits a vanishing bilinear square sum. -/
theorem conjugate_reciprocal_cross_hostile :
    (1 : ℂ) ≠ 0 ∧ Complex.I ≠ 0 ∧
      (1 : ℂ) ^ 2 + Complex.I ^ 2 = 0 := by
  constructor
  · norm_num
  constructor
  · exact Complex.I_ne_zero
  · rw [Complex.I_sq]
    norm_num

end ReciprocalConjugacy

section LocalOverlap

variable {K : Type*} [Field K]

def normalizedGeometricOverlap (r phase : K) : K :=
  ((1 - r) * phase) / (1 - r * phase)

/-- Once the geometric-series formula is supplied, its normalized local
overlap is nonzero under exactly the visible numerator and denominator gates. -/
theorem normalizedGeometricOverlap_ne_zero
    (r phase : K) (hr : r ≠ 1) (hphase : phase ≠ 0)
    (hdenominator : 1 - r * phase ≠ 0) :
    normalizedGeometricOverlap r phase ≠ 0 := by
  apply div_ne_zero
  · exact mul_ne_zero (sub_ne_zero.mpr (Ne.symm hr)) hphase
  · exact hdenominator

/-- Finite tensor-style aggregation preserves nonvanishing. -/
theorem finite_product_overlap_ne_zero
    {Index : Type*} (packet : Finset Index) (overlap : Index → K)
    (hnonzero : ∀ i ∈ packet, overlap i ≠ 0) :
    ∏ i ∈ packet, overlap i ≠ 0 := by
  exact Finset.prod_ne_zero_iff.mpr hnonzero

/-- Direct-sum aggregation can cancel even when every local overlap is
nonzero. -/
theorem additive_overlap_cancellation_hostile :
    (1 : ℚ) ≠ 0 ∧ (-1 : ℚ) ≠ 0 ∧ (1 : ℚ) + (-1) = 0 := by
  norm_num

end LocalOverlap

end MariciFormal
