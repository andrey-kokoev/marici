import Mathlib.Analysis.Complex.Basic
import Mathlib.Analysis.SpecialFunctions.Log.Basic
import Mathlib.Tactic.NormNum

/-!
Finite complex-gap hostile from Grothendieck's Xi lattice-divergence no-go.
The real part of the holomorphic continuation loses positivity, whereas the
radial Hermitian repair is nonnegative but cannot detect phase rotation.
-/

namespace MariciFormal

/-- Twice the real part of `w - 1 - Log w`, written using
`2 Re(Log w) = log(normSq w)`. -/
def holomorphicGapDivergence (w : ℂ) : ℝ :=
  2 * (w.re - 1) - Real.log (Complex.normSq w)

theorem holomorphicGapDivergence_one_add_I :
    holomorphicGapDivergence (1 + Complex.I) = -Real.log 2 := by
  norm_num [holomorphicGapDivergence, Complex.normSq_apply]

/-- The first harmless nonreal gap already makes the holomorphic real-part
continuation strictly negative. -/
theorem holomorphicGapDivergence_negative_hostile :
    holomorphicGapDivergence (1 + Complex.I) < 0 := by
  rw [holomorphicGapDivergence_one_add_I]
  exact neg_lt_zero.mpr (Real.log_pos (by norm_num))

def radialHermitianGapDivergence (w : ℂ) : ℝ :=
  Complex.normSq w - 1 - Real.log (Complex.normSq w)

theorem radialHermitianGapDivergence_nonnegative
    (w : ℂ) (hw : w ≠ 0) :
    0 ≤ radialHermitianGapDivergence w := by
  have hnorm : 0 < Complex.normSq w := Complex.normSq_pos.mpr hw
  have hlog := Real.log_le_sub_one_of_pos hnorm
  dsimp [radialHermitianGapDivergence]
  linarith

/-- The radial repair vanishes at a nontrivial unit phase, so it cannot by
itself distinguish the reference real gap from rigid rotation. -/
theorem radialHermitianGapDivergence_phase_blind :
    radialHermitianGapDivergence Complex.I = 0 ∧ Complex.I ≠ 1 := by
  constructor
  · norm_num [radialHermitianGapDivergence, Complex.normSq_apply]
  · intro h
    have him := congrArg Complex.im h
    norm_num at him

end MariciFormal
