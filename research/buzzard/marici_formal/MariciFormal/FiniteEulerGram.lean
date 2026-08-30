import Mathlib.Analysis.InnerProductSpace.Basic
import Mathlib.Algebra.BigOperators.Group.Finset.Basic
import Mathlib.Tactic

/-!
Finite Hilbert-Gram and polarization core shared by Grothendieck's Euler
cross-resolvent and minimal Schur-prime packets. No infinite source limit or
positive descent is assumed.
-/

namespace MariciFormal

open scoped BigOperators RealInnerProductSpace

variable {E ι : Type*} [SeminormedAddCommGroup E] [InnerProductSpace ℝ E]

/-- Determinant of the real two-vector Gram matrix. -/
def twoVectorGramDeterminant (u v : E) : ℝ :=
  ⟪u, u⟫_ℝ * ⟪v, v⟫_ℝ - ⟪u, v⟫_ℝ ^ 2

/-- Every real two-vector Gram determinant is nonnegative. This is the exact
finite positivity statement used before any Euler-source limit. -/
theorem twoVectorGramDeterminant_nonnegative (u v : E) :
    0 ≤ twoVectorGramDeterminant u v := by
  unfold twoVectorGramDeterminant
  have h := real_inner_mul_inner_self_le u v
  nlinarith

/-- A finite weighted source remains linear in the cross channel. -/
theorem inner_finset_weighted_source
    [Fintype ι] (boundary : E) (weight : ι → ℝ) (source : ι → E) :
    ⟪boundary, ∑ i, weight i • source i⟫_ℝ =
      ∑ i, weight i * ⟪boundary, source i⟫_ℝ := by
  simp [inner_sum, inner_smul_right]

/-- Polarization realizes a cross term as a signed difference of two positive
quadratic channels. The minus sign is data: this is not a positive Hilbert
Schur complement. -/
theorem real_cross_term_polarization (u v : E) :
    4 * ⟪u, v⟫_ℝ =
      ⟪u + v, u + v⟫_ℝ - ⟪u - v, u - v⟫_ℝ := by
  simp only [inner_add_left, inner_add_right, inner_sub_left, inner_sub_right]
  rw [real_inner_comm v u]
  ring

/-- A zero cross term does not force either source vector to vanish. -/
theorem orthogonal_nonzero_cross_hostile :
    let u : EuclideanSpace ℝ (Fin 2) := fun i => if i = 0 then 1 else 0
    let v : EuclideanSpace ℝ (Fin 2) := fun i => if i = 1 then 1 else 0
    u ≠ 0 ∧ v ≠ 0 ∧ ⟪u, v⟫_ℝ = 0 := by
  dsimp
  constructor
  · intro h
    have := congrFun h 0
    norm_num at this
  constructor
  · intro h
    have := congrFun h 1
    norm_num at this
  · simp [EuclideanSpace.inner_eq_star_dotProduct, dotProduct]

end MariciFormal
