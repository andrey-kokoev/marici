import MariciFormal.AdditivePrimeEdgeBudget
import Mathlib.LinearAlgebra.Matrix.Hermitian
import Mathlib.Tactic

/-!
Finite operator and squarefree spectral core of Grothendieck's prime-power
translation adjacency packet. The completed unbounded source is not assumed.
-/

namespace MariciFormal

open scoped BigOperators

section SelfAdjointAdjacency

variable {ι n : Type*} [Fintype ι]

/-- A finite real-weighted sum of a translation channel and its adjoint. -/
def finiteTranslationAdjacency
    (weight : ι → ℝ) (shift : ι → Matrix n n ℂ) : Matrix n n ℂ :=
  ∑ i, (weight i : ℂ) • (shift i + (shift i)ᴴ)

theorem finiteTranslationAdjacency_isHermitian
    (weight : ι → ℝ) (shift : ι → Matrix n n ℂ) :
    (finiteTranslationAdjacency weight shift).IsHermitian := by
  classical
  unfold finiteTranslationAdjacency
  generalize (Finset.univ : Finset ι) = indices
  induction indices using Finset.induction_on with
  | empty => simp
  | @insert index indices hnotmem hinduction =>
      rw [Finset.sum_insert hnotmem]
      exact ((Matrix.isHermitian_add_transpose_self (shift index)).smul (by simp)).add
        hinduction

end SelfAdjointAdjacency

section SquarefreeSpectrum

variable {ι : Type*} [Fintype ι]

def primeAdjacencyWalshEigenvalue
    (weight : ι → ℝ) (polarity : ι → Bool) : ℝ :=
  ∑ i, signedEdge (weight i) (polarity i)

theorem primeAdjacency_opposite_eigenvalue (weight : ι → ℝ) :
    primeAdjacencyWalshEigenvalue weight (oppositePolarity weight) =
      -(∑ i, |weight i|) := by
  unfold primeAdjacencyWalshEigenvalue
  rw [Finset.sum_neg_distrib]
  apply Finset.sum_congr rfl
  intro i hi
  exact signedEdge_oppositePolarity weight i

/-- Adding scalar diagonal energy `D` is nonnegative on every Walsh channel
exactly when `D` dominates the shared edge budget. -/
theorem diagonal_plus_primeAdjacency_nonnegative_iff
    (diagonal : ℝ) (weight : ι → ℝ) :
    (∀ polarity : ι → Bool,
        0 ≤ diagonal + primeAdjacencyWalshEigenvalue weight polarity) ↔
      ∑ i, |weight i| ≤ diagonal := by
  constructor
  · intro hall
    have hopposite := hall (oppositePolarity weight)
    rw [primeAdjacency_opposite_eigenvalue] at hopposite
    linarith
  · intro hbudget polarity
    have hsum :
        ∑ i, -|weight i| ≤
          ∑ i, signedEdge (weight i) (polarity i) := by
      exact Finset.sum_le_sum fun i hi =>
        negative_abs_le_signedEdge (weight i) (polarity i)
    rw [Finset.sum_neg_distrib] at hsum
    unfold primeAdjacencyWalshEigenvalue
    linarith

/-- Every Walsh eigenvalue lies in the exact shared `l1` spectral interval. -/
theorem primeAdjacency_eigenvalue_abs_le
    (weight : ι → ℝ) (polarity : ι → Bool) :
    |primeAdjacencyWalshEigenvalue weight polarity| ≤
      ∑ i, |weight i| := by
  unfold primeAdjacencyWalshEigenvalue
  calc
    |∑ i, signedEdge (weight i) (polarity i)| ≤
        ∑ i, |signedEdge (weight i) (polarity i)| :=
      Finset.abs_sum_le_sum_abs _ _
    _ = ∑ i, |weight i| := by
      apply Finset.sum_congr rfl
      intro i hi
      cases polarity i <;> simp [signedEdge]

/-- The sum of absolute weights is the least uniform Walsh spectral bound. -/
theorem primeAdjacency_spectral_radius_exact
    (weight : ι → ℝ) (bound : ℝ) :
    (∀ polarity : ι → Bool,
        |primeAdjacencyWalshEigenvalue weight polarity| ≤ bound) ↔
      ∑ i, |weight i| ≤ bound := by
  constructor
  · intro hall
    have hopposite := hall (oppositePolarity weight)
    rw [primeAdjacency_opposite_eigenvalue] at hopposite
    simpa only [abs_neg, abs_of_nonneg (Finset.sum_nonneg fun i hi => abs_nonneg _)]
      using hopposite
  · intro hbound polarity
    exact (primeAdjacency_eigenvalue_abs_le weight polarity).trans hbound

end SquarefreeSpectrum

end MariciFormal
