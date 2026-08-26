import Mathlib.Data.Matrix.Notation
import Mathlib.Tactic.NormNum
import Mathlib.Tactic.Ring

/-!
Finite two-port algebra behind Grothendieck's Euler cross-resolvent packet.
The free Green kernel and prime-source limit are not assumed.
-/

namespace MariciFormal

open Matrix

def crossResolventGram (scale decay : ℝ) : Matrix (Fin 2) (Fin 2) ℝ :=
  !![scale, scale * decay;
     scale * decay, scale]

theorem crossResolventGram_det (scale decay : ℝ) :
    (crossResolventGram scale decay).det = scale ^ 2 * (1 - decay ^ 2) := by
  simp [crossResolventGram, Matrix.det_fin_two]
  ring

/-- Positive scale and a cross-decay of modulus below one give positive
diagonal and determinant data for the symmetric two-port matrix. -/
theorem crossResolventGram_positive_principal_data
    (scale decay : ℝ) (hscale : 0 < scale) (hdecay : |decay| < 1) :
    0 < crossResolventGram scale decay 0 0 ∧
      0 < (crossResolventGram scale decay).det := by
  constructor
  · simpa [crossResolventGram] using hscale
  · rw [crossResolventGram_det]
    rcases abs_lt.mp hdecay with ⟨hleft, hright⟩
    have hsquare : 0 < scale ^ 2 := by positivity
    have hgap : 0 < 1 - decay ^ 2 := by nlinarith
    positivity

/-- Reversing one boundary orientation changes the cross-entry sign but not
the determinant. -/
theorem cross_orientation_flip_preserves_det (scale decay : ℝ) :
    (crossResolventGram scale (-decay)).det =
      (crossResolventGram scale decay).det := by
  simp [crossResolventGram_det]

/-- A negative cross propagator is compatible with positive principal data. -/
theorem negative_cross_entry_positive_gram_hostile :
    crossResolventGram 1 (-1 / 2) 0 1 = (-1 / 2 : ℝ) ∧
      crossResolventGram 1 (-1 / 2) 0 0 = 1 ∧
      (crossResolventGram 1 (-1 / 2)).det = 3 / 4 := by
  norm_num [crossResolventGram, Matrix.det_fin_two]

end MariciFormal
