import Mathlib

/-!
Exact determinant-ratio algebra for a finite monic Jacobi recurrence.

The determinants are supplied inputs.  This file does not construct a moment
measure, replay interval determinant certificates, or identify a finite Ritz
edge with a Riemann ordinate.
-/

namespace MariciFormal

section JacobiRatio

variable {K : Type*} [LinearOrderedField K]

def jacobiOffDiagonalSquare
    (deltaCurrent deltaPrevious deltaTwoBack : K) : K :=
  deltaCurrent * deltaTwoBack / deltaPrevious ^ 2

theorem jacobiOffDiagonalSquare_positive
    {deltaCurrent deltaPrevious deltaTwoBack : K}
    (hcurrent : 0 < deltaCurrent) (hprevious : 0 < deltaPrevious)
    (htwoBack : 0 < deltaTwoBack) :
    0 < jacobiOffDiagonalSquare deltaCurrent deltaPrevious deltaTwoBack := by
  unfold jacobiOffDiagonalSquare
  positivity

/-- For the first nontrivial three-, two-, and one-dimensional determinant
triple, a common moment-functional scale cancels from the Jacobi ratio. -/
theorem jacobiOffDiagonalSquare_threeTwoOneMomentScale
    (scale deltaCurrent deltaPrevious deltaTwoBack : K)
    (hscale : scale ≠ 0) :
    jacobiOffDiagonalSquare
        (scale ^ 3 * deltaCurrent)
        (scale ^ 2 * deltaPrevious)
        (scale * deltaTwoBack) =
      jacobiOffDiagonalSquare deltaCurrent deltaPrevious deltaTwoBack := by
  unfold jacobiOffDiagonalSquare
  field_simp
  ring

/-- Positivity of a determinant ratio is a nonbreakdown statement only; it
does not determine the diagonal coefficient or an infinite continuation. -/
theorem positiveRatio_has_many_diagonal_extensions
    (b : K) (hb : 0 < b) :
    (0, b) ≠ (1, b) ∧ 0 < (0, b).2 ∧ 0 < (1, b).2 := by
  exact ⟨by simp, hb, hb⟩

end JacobiRatio

end MariciFormal
