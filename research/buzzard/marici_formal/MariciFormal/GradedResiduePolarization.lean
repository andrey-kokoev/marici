import Mathlib.Data.Complex.Basic
import Mathlib.Data.Fin.Rev
import Mathlib.Algebra.Order.BigOperators.Group.Finset
import Mathlib.Tactic.FieldSimp
import Mathlib.Tactic.NormNum
import Mathlib.Tactic.PushNeg
import Mathlib.Tactic.Ring

/-!
Local finite-jet algebra of Grothendieck's graded residue polarization.
The global self-adjoint spectral boundary remains conditional on reality of
the source divisor.
-/

namespace MariciFormal

open scoped BigOperators

section AlgebraicJetForm

variable {K : Type*} [Field K]
variable {m : ℕ}

def degreeReverse (u : K) (y : Fin m → K) : Fin m → K :=
  fun j => u * y j.rev

def residueJetForm (uInv : K) (x y : Fin m → K) : K :=
  ∑ i, uInv * x i * y i.rev

def polarizedJetForm (u : K) (x y : Fin m → K) : K :=
  (m : K) * residueJetForm u⁻¹ x (degreeReverse u y)

/-- Degree reversal cancels the nonzero leading coefficient and diagonalizes
the residue form with scalar `m`. -/
theorem polarizedJetForm_eq_scaled_dot
    (u : K) (hu : u ≠ 0) (x y : Fin m → K) :
    polarizedJetForm u x y = (m : K) * ∑ i, x i * y i := by
  unfold polarizedJetForm residueJetForm
  congr 1
  apply Finset.sum_congr rfl
  intro i hi
  simp only [degreeReverse, Fin.rev_rev]
  field_simp [hu] <;> ring

end AlgebraicJetForm

section PositiveRealJetForm

variable {m : ℕ}

theorem polarizedJetForm_nonnegative
    (u : ℝ) (hu : u ≠ 0) (x : Fin m → ℝ) :
    0 ≤ polarizedJetForm u x x := by
  rw [polarizedJetForm_eq_scaled_dot u hu]
  exact mul_nonneg (Nat.cast_nonneg m)
    (Finset.sum_nonneg fun i hi => mul_self_nonneg (x i))

theorem polarizedJetForm_positive
    (u : ℝ) (hu : u ≠ 0) (x : Fin m → ℝ)
    (hm : 0 < m) (hx : x ≠ 0) :
    0 < polarizedJetForm u x x := by
  rw [polarizedJetForm_eq_scaled_dot u hu]
  apply mul_pos (Nat.cast_pos.mpr hm)
  apply Finset.sum_pos'
  · intro i hi
    exact mul_self_nonneg (x i)
  · have hex : ∃ i, x i ≠ 0 := by
      by_contra hall
      push_neg at hall
      apply hx
      funext i
      exact hall i
    obtain ⟨i, hi⟩ := hex
    exact ⟨i, Finset.mem_univ i, mul_self_pos.mpr hi⟩

end PositiveRealJetForm

section NonrealHostile

/-- A nonreal scalar fails the conjugation-fixed condition required of a
one-dimensional self-adjoint eigenvalue. -/
theorem imaginary_scalar_not_conjugation_fixed :
    Complex.conj Complex.I ≠ Complex.I := by
  norm_num

end NonrealHostile

end MariciFormal
