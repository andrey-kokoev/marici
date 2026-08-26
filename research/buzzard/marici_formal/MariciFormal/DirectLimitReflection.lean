import Mathlib

/-!
The scalar reflection cell for unitary transitions, together with the repeated
dilation countermodel to uniform ambient metric comparison.
-/

namespace MariciFormal

open ComplexConjugate

/-- On the unit circle, the dual transition is exactly the conjugate transition. -/
theorem unitaryTransition_inverse_eq_conj
    (u : Complex) (unitary : ‖u‖ = 1) :
    u⁻¹ = conj u :=
  Complex.inv_eq_conj unitary

/-- Metric coefficient obtained after `n` repetitions of dilation by two. -/
noncomputable def dilatedMetric (n : Nat) : Real :=
  (1 / 4 : Real) ^ n

theorem dilatedMetric_initial : dilatedMetric 0 = 1 := by
  norm_num [dilatedMetric]

/-- Each finite dilation transports the metric by the exact factor `|2|⁻² = 1/4`. -/
theorem dilatedMetric_step (n : Nat) :
    dilatedMetric (n + 1) = dilatedMetric n / 4 := by
  simp [dilatedMetric, pow_succ]
  ring

theorem dilatedMetric_positive (n : Nat) : 0 < dilatedMetric n := by
  exact pow_pos (by norm_num) n

theorem dilatedMetric_tendsto_zero :
    Filter.Tendsto dilatedMetric Filter.atTop (nhds 0) := by
  exact tendsto_pow_atTop_nhds_zero_of_lt_one (by norm_num) (by norm_num)

/-- Exact finite metric transport does not yield a positive uniform lower comparison. -/
theorem repeatedDilation_has_no_uniform_positive_lower_bound :
    ¬ ∃ c : Real, 0 < c ∧ ∀ n, c ≤ dilatedMetric n := by
  rintro ⟨c, hc, bound⟩
  obtain ⟨n, hn⟩ := exists_pow_lt_of_lt_one hc (by norm_num : (1 / 4 : Real) < 1)
  exact (not_lt_of_ge (bound n)) hn

end MariciFormal
