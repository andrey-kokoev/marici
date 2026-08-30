import Mathlib.LinearAlgebra.Matrix.PosDef
import Mathlib.Analysis.Complex.Order
import Mathlib.Tactic

/-!
Hermitian positive-semidefinite transport for finite Fourier spectra. This is
the linear-algebra bridge after a source kernel has actually been identified
with an invertible spectral congruence.
-/

namespace MariciFormal

open scoped ComplexOrder

variable {n : Type*} [Fintype n] [DecidableEq n]

/-- Congruence of a real spectral diagonal by a complex synthesis matrix. -/
def spectralCongruence (synthesis : Matrix n n ℂ) (spectrum : n → ℝ) :
    Matrix n n ℂ :=
  star synthesis * Matrix.diagonal (fun i => (spectrum i : ℂ)) * synthesis

/-- An invertible synthesis matrix transports positive semidefiniteness
exactly: the reconstructed Hermitian matrix is PSD iff every real spectral
coefficient is nonnegative. -/
theorem spectralCongruence_posSemidef_iff
    (synthesis : Matrix n n ℂ) (spectrum : n → ℝ)
    (hinvertible : IsUnit synthesis) :
    (spectralCongruence synthesis spectrum).PosSemidef ↔
      ∀ i, 0 ≤ spectrum i := by
  unfold spectralCongruence
  rw [hinvertible.posSemidef_star_left_conjugate_iff]
  rw [Matrix.posSemidef_diagonal_iff]
  simp only [RCLike.ofReal_nonneg]

/-- Without invertibility, congruence can erase a negative spectral channel. -/
theorem zeroSynthesis_hides_negative_spectrum :
    let synthesis : Matrix (Fin 1) (Fin 1) ℂ := 0
    let spectrum : Fin 1 → ℝ := fun _ => -1
    spectralCongruence synthesis spectrum = 0 ∧
      ¬ (∀ i, 0 ≤ spectrum i) := by
  dsimp
  constructor
  · simp [spectralCongruence]
  · intro h
    have hzero := h 0
    norm_num at hzero

end MariciFormal
