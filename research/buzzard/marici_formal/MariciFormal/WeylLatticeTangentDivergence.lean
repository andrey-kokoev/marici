import Mathlib.Analysis.SpecialFunctions.Log.Basic
import Mathlib.Algebra.Order.BigOperators.Group.Finset
import Mathlib.Tactic.NormNum

/-!
Finite convex core of Grothendieck's Weyl-lattice tangent divergence.
The Xi specialization is intentionally absent because it presupposes a real
ordered zero configuration.
-/

namespace MariciFormal

open Finset
open scoped BigOperators

def logarithmicTangentGap (u : ℝ) : ℝ :=
  u - Real.log (1 + u)

theorem logarithmicTangentGap_nonnegative
    (u : ℝ) (hdomain : -1 < u) :
    0 ≤ logarithmicTangentGap u := by
  have hpositive : 0 < 1 + u := by linarith
  have hlog := Real.log_le_sub_one_of_pos hpositive
  dsimp [logarithmicTangentGap]
  linarith

theorem logarithmicTangentGap_eq_zero_iff
    (u : ℝ) (hdomain : -1 < u) :
    logarithmicTangentGap u = 0 ↔ u = 0 := by
  constructor
  · intro hzero
    by_contra hne
    have hpositive : 0 < 1 + u := by linarith
    have hone : 1 + u ≠ 1 := by linarith
    have hstrict := Real.log_lt_sub_one_of_pos hpositive hone
    dsimp [logarithmicTangentGap] at hzero
    linarith
  · rintro rfl
    simp [logarithmicTangentGap]

def finiteTangentDivergence
    {ι : Type*} (indices : Finset ι) (slope : ι → ℝ) : ℝ :=
  2 * ∑ i ∈ indices, logarithmicTangentGap (slope i)

theorem finiteTangentDivergence_nonnegative
    {ι : Type*} (indices : Finset ι) (slope : ι → ℝ)
    (hdomain : ∀ i ∈ indices, -1 < slope i) :
    0 ≤ finiteTangentDivergence indices slope := by
  unfold finiteTangentDivergence
  have hsum : 0 ≤ ∑ i ∈ indices, logarithmicTangentGap (slope i) :=
    sum_nonneg fun i hi =>
      logarithmicTangentGap_nonnegative (slope i) (hdomain i hi)
  positivity

theorem finiteTangentDivergence_eq_zero_iff
    {ι : Type*} (indices : Finset ι) (slope : ι → ℝ)
    (hdomain : ∀ i ∈ indices, -1 < slope i) :
    finiteTangentDivergence indices slope = 0 ↔
      ∀ i ∈ indices, slope i = 0 := by
  constructor
  · intro hzero
    have hsum : ∑ i ∈ indices, logarithmicTangentGap (slope i) = 0 := by
      unfold finiteTangentDivergence at hzero
      linarith
    have hterm := (sum_eq_zero_iff_of_nonneg
      (fun i hi => logarithmicTangentGap_nonnegative (slope i) (hdomain i hi))).1 hsum
    intro i hi
    exact (logarithmicTangentGap_eq_zero_iff (slope i) (hdomain i hi)).1
      (hterm i hi)
  · intro hzero
    unfold finiteTangentDivergence
    rw [sum_eq_zero fun i hi =>
      (logarithmicTangentGap_eq_zero_iff (slope i) (hdomain i hi)).2
        (hzero i hi)]
    ring

/-- A nontrivial admissible slope has strictly positive divergence. -/
theorem singleton_nontrivial_tangent_divergence_positive :
    0 < finiteTangentDivergence ({()} : Finset Unit) (fun _ => 1) := by
  have hstrict := Real.log_lt_sub_one_of_pos (show (0 : ℝ) < 2 by norm_num)
    (show (2 : ℝ) ≠ 1 by norm_num)
  simp [finiteTangentDivergence, logarithmicTangentGap]
  linarith

section OrderedPairs

def orderedPairSlope (baseGap perturbationGap : ℝ) : ℝ :=
  perturbationGap / baseGap

/-- For a positive reference-lattice gap, strict ordering of the perturbed
pair is exactly the logarithm-domain condition on its normalized slope. -/
theorem perturbed_pair_ordered_iff_slope_gt_neg_one
    (baseGap perturbationGap : ℝ) (hbase : 0 < baseGap) :
    0 < baseGap + perturbationGap ↔
      -1 < orderedPairSlope baseGap perturbationGap := by
  unfold orderedPairSlope
  constructor
  · intro hordered
    apply (lt_div_iff₀ hbase).2
    linarith
  · intro hslope
    have := (lt_div_iff₀ hbase).1 hslope
    linarith

def AllPairDifferencesZero {ι : Type*} (perturbation : ι → ℝ) : Prop :=
  ∀ i j, perturbation j - perturbation i = 0

/-- Vanishing of every pair slope is exactly common translation of all
retained lattice coordinates. -/
theorem allPairDifferencesZero_iff_common_translation
    {ι : Type*} [Nonempty ι] (perturbation : ι → ℝ) :
    AllPairDifferencesZero perturbation ↔
      ∃ shift : ℝ, ∀ i, perturbation i = shift := by
  classical
  constructor
  · intro hzero
    let anchor : ι := Classical.choice (inferInstance : Nonempty ι)
    refine ⟨perturbation anchor, ?_⟩
    intro i
    have hpair := hzero anchor i
    linarith
  · rintro ⟨shift, hshift⟩
    intro i j
    rw [hshift i, hshift j]
    ring

end OrderedPairs

end MariciFormal
