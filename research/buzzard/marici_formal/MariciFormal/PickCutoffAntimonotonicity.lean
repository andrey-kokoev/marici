import Mathlib.Analysis.SpecialFunctions.Exp
import Mathlib.Tactic.Positivity

/-!
One-mode diagonal obstruction from Grothendieck's prime Pick-cutoff packet.
Every positive Euler mode adds a strictly negative Pick-kernel direction on
the positive imaginary axis.
-/

namespace MariciFormal

def pickModeDiagonalIncrement (amplitude length height : ℝ) : ℝ :=
  -(amplitude * Real.exp (-height * length)) / height

/-- A positive mode at positive height has strictly negative diagonal Pick
increment. -/
theorem pickModeDiagonalIncrement_negative
    (amplitude length height : ℝ)
    (hamplitude : 0 < amplitude) (hheight : 0 < height) :
    pickModeDiagonalIncrement amplitude length height < 0 := by
  unfold pickModeDiagonalIncrement
  have hexp : 0 < Real.exp (-height * length) := Real.exp_pos _
  positivity

/-- Therefore this increment cannot be the squared norm of an added positive
Hilbert-space feature. -/
theorem pickModeIncrement_not_nonnegative_feature
    (amplitude length height : ℝ)
    (hamplitude : 0 < amplitude) (hheight : 0 < height) :
    ¬ 0 ≤ pickModeDiagonalIncrement amplitude length height := by
  exact not_le.mpr
    (pickModeDiagonalIncrement_negative amplitude length height
      hamplitude hheight)

end MariciFormal
