import Mathlib.Algebra.Group.Translate
import Mathlib.Tactic

/-!
Finite-volume theorem and growing diagonal hostile from Grothendieck's
difference-correspondence normalization audit.
-/

namespace MariciFormal

open Finset
open scoped BigOperators

section FiniteAdditiveGroup

variable {G : Type*} [AddCommGroup G] [Fintype G]

def finiteFunctionNormSq (f : G → ℝ) : ℝ :=
  ∑ x, f x ^ 2

def differencePullbackNormSq (f : G → ℝ) : ℝ :=
  ∑ a, ∑ b, f (a - b) ^ 2

theorem sum_sq_sub_left_eq (f : G → ℝ) (a : G) :
    (∑ b, f (a - b) ^ 2) = ∑ x, f x ^ 2 := by
  exact Equiv.sum_comp (Equiv.subLeft a) (fun x => f x ^ 2)

/-- The finite difference pullback has squared norm multiplied by the group
cardinality. -/
theorem differencePullback_normSq_eq_card_mul
    (f : G → ℝ) :
    differencePullbackNormSq f =
      (Fintype.card G : ℝ) * finiteFunctionNormSq f := by
  unfold differencePullbackNormSq finiteFunctionNormSq
  simp_rw [sum_sq_sub_left_eq]
  simp

theorem normalized_differencePullback_isometric
    (f : G → ℝ) (hcard : Fintype.card G ≠ 0) :
    differencePullbackNormSq f / (Fintype.card G : ℝ) =
      finiteFunctionNormSq f := by
  rw [differencePullback_normSq_eq_card_mul]
  have hcardReal : (Fintype.card G : ℝ) ≠ 0 := by
    exact_mod_cast hcard
  field_simp [hcardReal]

end FiniteAdditiveGroup

section DiagonalWindow

def diagonalIndicator {n : ℕ} (left right : Fin n) : ℝ :=
  if left = right then 1 else 0

/-- A finite square window with `n` sites has exactly `n` unit diagonal
contributions. -/
theorem diagonalIndicator_window_normSq (n : ℕ) :
    (∑ left : Fin n, ∑ right : Fin n,
      diagonalIndicator left right ^ 2) = n := by
  simp [diagonalIndicator]

/-- The diagonal-window squared norms have no uniform natural bound. -/
theorem diagonalWindow_normSq_unbounded :
    ∀ bound : ℕ, ∃ n : ℕ,
      bound < ∑ left : Fin n, ∑ right : Fin n,
        diagonalIndicator left right ^ 2 := by
  intro bound
  refine ⟨bound + 1, ?_⟩
  rw [diagonalIndicator_window_normSq]
  exact_mod_cast Nat.lt_succ_self bound

end DiagonalWindow

end MariciFormal
