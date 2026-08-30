import Mathlib.Analysis.Normed.Group.Basic
import Mathlib.Tactic.NormNum
import Mathlib.Tactic.Nlinarith

/-!
Norm-theoretic core of Grothendieck's finite unitary-orbit no-go. Linearity
and an inner product are stronger than the norm-preservation actually used.
-/

namespace MariciFormal

section OrbitBound

variable {E : Type*} [SeminormedAddCommGroup E]

def NormPreserving (operator : E → E) : Prop :=
  ∀ x, ‖operator x‖ = ‖x‖

theorem norm_iterate_eq
    (operator : E → E) (hoperator : NormPreserving operator)
    (n : ℕ) (x : E) :
    ‖(operator^[n]) x‖ = ‖x‖ := by
  induction n with
  | zero => rfl
  | succ n ih =>
      rw [Function.iterate_succ_apply']
      exact (hoperator _).trans ih

theorem orbitCoboundary_norm_le_two
    (operator : E → E) (hoperator : NormPreserving operator)
    (n : ℕ) (x : E) :
    ‖x - (operator^[n]) x‖ ≤ 2 * ‖x‖ := by
  calc
    ‖x - (operator^[n]) x‖ ≤ ‖x‖ + ‖(operator^[n]) x‖ := norm_sub_le _ _
    _ = 2 * ‖x‖ := by rw [norm_iterate_eq operator hoperator n x]; ring

theorem orbitCoboundary_norm_sq_le_four
    (operator : E → E) (hoperator : NormPreserving operator)
    (n : ℕ) (x : E) :
    ‖x - (operator^[n]) x‖ ^ 2 ≤ 4 * ‖x‖ ^ 2 := by
  have hbound := orbitCoboundary_norm_le_two operator hoperator n x
  have hleft : 0 ≤ ‖x - (operator^[n]) x‖ := norm_nonneg _
  have hright : 0 ≤ ‖x‖ := norm_nonneg _
  nlinarith

/-- A finite-norm norm-preserving orbit cannot have unbounded coboundary
norms. -/
theorem no_unbounded_finiteOrbitCoboundary
    (operator : E → E) (hoperator : NormPreserving operator) (x : E) :
    ¬ (∀ bound : ℝ, ∃ n : ℕ, bound < ‖x - (operator^[n]) x‖) := by
  intro hunbounded
  obtain ⟨n, hn⟩ := hunbounded (2 * ‖x‖)
  exact (not_lt_of_ge (orbitCoboundary_norm_le_two operator hoperator n x)) hn

end OrbitBound

def realNegation (x : ℝ) : ℝ := -x

theorem realNegation_normPreserving : NormPreserving realNegation := by
  intro x
  simp [realNegation]

/-- The constant `2` and squared constant `4` are sharp. -/
theorem orbitCoboundary_bound_sharp :
    ‖(1 : ℝ) - (realNegation^[1]) 1‖ = 2 ∧
      ‖(1 : ℝ) - (realNegation^[1]) 1‖ ^ 2 = 4 := by
  norm_num [realNegation]

end MariciFormal
