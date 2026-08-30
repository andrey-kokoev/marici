import Mathlib.Data.Matrix.Basic
import Mathlib.Tactic.Abel
import Mathlib.Tactic.FieldSimp
import Mathlib.Tactic.NormNum
import Mathlib.Tactic.Ring

/-!
Finite relative-complement incidence factorization from Grothendieck's
coefficient--Betti lane.  The theorem is purely algebraic and keeps the
analytic determinant and orientation gates separate.
-/

namespace MariciFormal

open Matrix

section CoordinateSplit

variable {X Y R : Type*}
variable [Fintype X] [Fintype Y] [DecidableEq X]
variable [CommRing R]

def admittedRestriction (p : Y → Prop) [DecidablePred p]
    (U : Matrix Y X R) : Matrix Y X R :=
  fun y x => if p y then U y x else 0

def complementRestriction (p : Y → Prop) [DecidablePred p]
    (U : Matrix Y X R) : Matrix Y X R :=
  fun y x => if p y then 0 else U y x

def transposeGram (U : Matrix Y X R) : Matrix X X R :=
  Uᵀ * U

/-- An admitted coordinate subset and its relative complement split the Gram
operator exactly. -/
theorem admitted_add_complement_gram
    (p : Y → Prop) [DecidablePred p] (U : Matrix Y X R) :
    transposeGram (admittedRestriction p U) +
        transposeGram (complementRestriction p U) =
      transposeGram U := by
  ext i j
  simp only [transposeGram, Matrix.add_apply, Matrix.mul_apply,
    Matrix.transpose_apply]
  rw [← Finset.sum_add_distrib]
  apply Finset.sum_congr rfl
  intro y hy
  by_cases hp : p y <;>
    simp [admittedRestriction, complementRestriction, hp]

/-- If the full incidence is normalized, the relative complement is an
independently defined first-order factor of the admitted Gram defect. -/
theorem relative_complement_factors_defect
    (p : Y → Prop) [DecidablePred p] (U : Matrix Y X R)
    (hisometry : transposeGram U = 1) :
    1 - transposeGram (admittedRestriction p U) =
      transposeGram (complementRestriction p U) := by
  have hsplit := admitted_add_complement_gram p U
  calc
    1 - transposeGram (admittedRestriction p U) =
        (transposeGram (admittedRestriction p U) +
          transposeGram (complementRestriction p U)) -
            transposeGram (admittedRestriction p U) := by
              rw [hsplit, hisometry]
    _ = transposeGram (complementRestriction p U) := by abel

end CoordinateSplit

section RegularFiberHostile

def normalizedGramScalar (admitted degree : ℕ) : ℚ :=
  admitted / degree

/-- For a regular unweighted finite fiber, the complement defect is just the
rational omitted fraction. -/
theorem normalizedGramScalar_complement
    (admitted degree : ℕ) (h : admitted ≤ degree) (hdegree : degree ≠ 0) :
    1 - normalizedGramScalar admitted degree =
      normalizedGramScalar (degree - admitted) degree := by
  have hdq : (degree : ℚ) ≠ 0 := by exact_mod_cast hdegree
  unfold normalizedGramScalar
  rw [Nat.cast_sub h]
  field_simp [hdq] <;> ring

theorem c2_one_branch_gram : normalizedGramScalar 1 2 = 1 / 2 := by
  norm_num [normalizedGramScalar]

theorem c2_one_branch_complement :
    1 - normalizedGramScalar 1 2 = 1 / 2 := by
  norm_num [normalizedGramScalar]

/-- A fixed finite split has no dependence on an external height parameter. -/
theorem fixed_split_is_height_constant {T : Type*} (t₁ t₂ : T) :
    (fun _ : T => 1 - normalizedGramScalar 1 2) t₁ =
      (fun _ : T => 1 - normalizedGramScalar 1 2) t₂ := by
  rfl

end RegularFiberHostile

end MariciFormal
