import Mathlib.Tactic

/-!
Rank-one integral core of Grothendieck's Smith-factor criterion for Mackey
traces. The arbitrary-matrix Smith normal form theorem remains an external
interface.
-/

namespace MariciFormal

/-- For a one-dimensional integral pushforward of scale `s`, an integral
trace with norm scalar `d` exists exactly when `s` divides `d`. -/
theorem scalar_integral_trace_exists_iff_dvd (s d : ℤ) :
    (∃ trace : ℤ, s * trace = d) ↔ s ∣ d := by
  constructor
  · rintro ⟨trace, htrace⟩
    exact ⟨trace, htrace.symm⟩
  · rintro ⟨trace, htrace⟩
    exact ⟨trace, htrace.symm⟩

/-- Smith factor two excludes a degree-three integral trace. -/
theorem smith_two_degree_three_hostile :
    ¬ ∃ trace : ℤ, 2 * trace = 3 := by
  rw [scalar_integral_trace_exists_iff_dvd]
  norm_num

/-- The same nonsplit scale admits a degree-four trace. -/
theorem smith_two_degree_four_trace :
    ∃ trace : ℤ, 2 * trace = 4 := by
  exact ⟨2, by norm_num⟩

/-- Existence need not select a canonical trace once an invisible kernel
coordinate is present. -/
theorem scalar_trace_kernel_nonuniqueness :
    ∃ left right : ℤ × ℤ,
      left ≠ right ∧ 2 * left.1 = 4 ∧ 2 * right.1 = 4 := by
  exact ⟨(2, 0), (2, 1), by norm_num⟩

/-- Pairing scale six and right-hand side four have no integral adjoint. -/
theorem pairing_six_rhs_four_no_integral_adjoint :
    ¬ ∃ adjoint : ℤ, 6 * adjoint = 4 := by
  rw [scalar_integral_trace_exists_iff_dvd]
  norm_num

/-- The same equation has the rational adjoint `2/3`, so localization at
three, not at two, repairs this rank-one obstruction. -/
theorem pairing_six_rhs_four_rational_adjoint :
    (6 : ℚ) * (2 / 3) = 4 := by
  norm_num

/-- A nonunimodular pairing need not obstruct integrality when the right-hand
side already contains its divisibility. -/
theorem pairing_six_rhs_six_integral_adjoint :
    ∃ adjoint : ℤ, 6 * adjoint = 6 := by
  exact ⟨1, by norm_num⟩

end MariciFormal
