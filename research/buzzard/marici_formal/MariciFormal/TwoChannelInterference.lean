import Mathlib.Data.Matrix.Notation
import Mathlib.Tactic.FieldSimp
import Mathlib.Tactic.FinCases
import Mathlib.Tactic.NormNum
import Mathlib.Tactic.Ring

/-!
Finite scalar core of Grothendieck's two-channel interference target.
Operator-valued entries, determinant-class scalarization, and source
construction are separate interfaces.
-/

namespace MariciFormal

open Matrix

variable {K : Type*} [Field K]

def twoChannelMatrix (a b c d : K) : Matrix (Fin 2) (Fin 2) K :=
  !![a, b; c, d]

theorem twoChannelMatrix_det (a b c d : K) :
    (twoChannelMatrix a b c d).det = a * d - b * c := by
  simp [twoChannelMatrix, Matrix.det_fin_two]

def fourCycleRatio (a b c d : K) : K := a * d / (b * c)

/-- Independent nonzero row and column rescalings cancel from the four-cycle
holonomy. -/
theorem fourCycleRatio_rescaling_invariant
    (row₀ row₁ col₀ col₁ a b c d : K)
    (hrow₀ : row₀ ≠ 0) (hrow₁ : row₁ ≠ 0)
    (hcol₀ : col₀ ≠ 0) (hcol₁ : col₁ ≠ 0)
    (hb : b ≠ 0) (hc : c ≠ 0) :
    fourCycleRatio
        (row₀ * a * col₀) (row₀ * b * col₁)
        (row₁ * c * col₀) (row₁ * d * col₁) =
      fourCycleRatio a b c d := by
  unfold fourCycleRatio
  field_simp [hrow₀, hrow₁, hcol₀, hcol₁, hb, hc]
  ring

/-- At `T=1`, every source entry is nonzero while the determinant vanishes
by interference of the two matchings. -/
theorem twoChannel_nonzero_entry_interference_hostile :
    let q := twoChannelMatrix (1 : ℚ) 1 1 1
    (∀ i j, q i j ≠ 0) ∧ q.det = 0 := by
  dsimp [twoChannelMatrix]
  constructor
  · intro i j
    fin_cases i <;> fin_cases j <;> norm_num
  · norm_num [Matrix.det_fin_two]

end MariciFormal
