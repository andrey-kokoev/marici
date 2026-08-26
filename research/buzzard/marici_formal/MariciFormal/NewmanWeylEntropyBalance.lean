import Mathlib.Algebra.BigOperators.Group.Finset.Basic
import Mathlib.Tactic.NormNum
import Mathlib.Tactic.Ring

/-!
Finite algebraic balance behind Grothendieck's nonlinear Weyl-coordinate
Newman flow. Differentiable root paths and collision avoidance are not inputs.
-/

namespace MariciFormal

open Finset
open scoped BigOperators

section AlgebraicBalance

variable {R : Type*} [CommRing R]
variable {ι : Type*}

def transformedRootVelocity
    (mobility field anomaly : ι → R) (i : ι) : R :=
  2 * mobility i * field i + anomaly i

def finiteEntropyRate
    (indices : Finset ι) (field velocity : ι → R) : R :=
  ∑ i ∈ indices, 2 * field i * velocity i

def mobilityDissipation
    (indices : Finset ι) (mobility field : ι → R) : R :=
  4 * ∑ i ∈ indices, mobility i * field i ^ 2

def anomalyFlux
    (indices : Finset ι) (field anomaly : ι → R) : R :=
  2 * ∑ i ∈ indices, field i * anomaly i

theorem finiteEntropyRate_decomposition
    (indices : Finset ι) (mobility field anomaly : ι → R) :
    finiteEntropyRate indices field
        (transformedRootVelocity mobility field anomaly) =
      mobilityDissipation indices mobility field +
        anomalyFlux indices field anomaly := by
  unfold finiteEntropyRate transformedRootVelocity mobilityDissipation anomalyFlux
  rw [← mul_sum, ← mul_sum, ← sum_add_distrib]
  apply sum_congr rfl
  intro i hi
  ring

end AlgebraicBalance

section OrderedCriterion

variable {ι : Type*}

theorem finiteEntropyRate_nonnegative_iff_anomaly_bound
    (indices : Finset ι) (mobility field anomaly : ι → ℝ) :
    0 ≤ finiteEntropyRate indices field
        (transformedRootVelocity mobility field anomaly) ↔
      -mobilityDissipation indices mobility field ≤
        anomalyFlux indices field anomaly := by
  rw [finiteEntropyRate_decomposition]
  linarith

theorem zero_anomaly_positive_mobility_nonnegative
    (indices : Finset ι) (mobility field : ι → ℝ)
    (hmobility : ∀ i ∈ indices, 0 ≤ mobility i) :
    0 ≤ finiteEntropyRate indices field
      (transformedRootVelocity mobility field (fun _ => 0)) := by
  rw [finiteEntropyRate_decomposition]
  have hdiss : 0 ≤ mobilityDissipation indices mobility field := by
    unfold mobilityDissipation
    apply mul_nonneg (by norm_num)
    exact sum_nonneg fun i hi =>
      mul_nonneg (hmobility i hi) (sq_nonneg (field i))
  simpa [anomalyFlux] using hdiss

end OrderedCriterion

/-- Positive mobility does not control the nonlinear-coordinate anomaly. -/
theorem positive_mobility_negative_entropy_hostile :
    let indices : Finset Unit := {()}
    let mobility : Unit → ℝ := fun _ => 1
    let field : Unit → ℝ := fun _ => 1
    let anomaly : Unit → ℝ := fun _ => -3
    finiteEntropyRate indices field
      (transformedRootVelocity mobility field anomaly) = -2 ∧
      mobilityDissipation indices mobility field = 4 ∧
      anomalyFlux indices field anomaly = -6 := by
  norm_num [finiteEntropyRate, transformedRootVelocity, mobilityDissipation,
    anomalyFlux]

end MariciFormal
