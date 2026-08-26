import Mathlib

/-!
Finite quadratic-form positivity under diagonal congruence.

This is the algebraic core of the denominator-cleared Loewner kernel.  The
reverse implication requires every diagonal factor to be nonzero.  Positivity
at zeros therefore needs a separate continuity theorem and cannot be inferred
from congruence alone.
-/

namespace MariciFormal

section DiagonalCongruence

variable {K : Type*} [LinearOrderedField K]
variable {I : Type*} [Fintype I]

def finiteQuadraticForm (A : I → I → K) (v : I → K) : K :=
  ∑ i, ∑ j, v i * A i j * v j

def PositiveSemidefiniteForm (A : I → I → K) : Prop :=
  ∀ v, 0 ≤ finiteQuadraticForm A v

def diagonalCongruence (d : I → K) (A : I → I → K) : I → I → K :=
  fun i j => d i * A i j * d j

theorem quadraticForm_diagonalCongruence
    (d : I → K) (A : I → I → K) (v : I → K) :
    finiteQuadraticForm (diagonalCongruence d A) v =
      finiteQuadraticForm A (fun i => d i * v i) := by
  unfold finiteQuadraticForm diagonalCongruence
  apply Finset.sum_congr rfl
  intro i hi
  apply Finset.sum_congr rfl
  intro j hj
  ring

theorem diagonalCongruence_preserves_psd
    (d : I → K) (A : I → I → K)
    (hA : PositiveSemidefiniteForm A) :
    PositiveSemidefiniteForm (diagonalCongruence d A) := by
  intro v
  rw [quadraticForm_diagonalCongruence]
  exact hA _

theorem diagonalCongruence_reflects_psd
    (d : I → K) (A : I → I → K) (hd : ∀ i, d i ≠ 0)
    (hcongruent : PositiveSemidefiniteForm (diagonalCongruence d A)) :
    PositiveSemidefiniteForm A := by
  intro v
  have h := hcongruent (fun i => v i / d i)
  rw [quadraticForm_diagonalCongruence] at h
  simpa [hd] using h

theorem diagonalCongruence_psd_iff
    (d : I → K) (A : I → I → K) (hd : ∀ i, d i ≠ 0) :
    PositiveSemidefiniteForm (diagonalCongruence d A) ↔
      PositiveSemidefiniteForm A :=
  ⟨diagonalCongruence_reflects_psd d A hd,
    diagonalCongruence_preserves_psd d A⟩

/-- If a denominator-clearing factor vanishes, congruence can erase a
negative direction; reflection of positivity is then false. -/
theorem zeroDiagonalFactor_can_erase_negativity :
    let A : Fin 1 → Fin 1 → Rat := fun _ _ => -1
    let d : Fin 1 → Rat := fun _ => 0
    PositiveSemidefiniteForm (diagonalCongruence d A) ∧
      ¬ PositiveSemidefiniteForm A := by
  dsimp [PositiveSemidefiniteForm, finiteQuadraticForm, diagonalCongruence]
  constructor
  · intro v
    norm_num
  · intro h
    have := h (fun _ => 1)
    norm_num at this

end DiagonalCongruence

end MariciFormal
