import Mathlib

/-!
Finite algebra for the quarter-point coordinate change
`h = epsilon + epsilon^2`, including the Jacobian division by
`1 + 2 * epsilon`.

The source packets use `L` inconsistently: one packet states the Jacobian
division explicitly, while a later packet writes `L = S` after the coordinate
change.  The formulas formalized here are exactly the Jacobian-corrected
formulas common to their displayed moments.  No analytic Xi identity and no
positivity assertion is assumed.
-/

namespace MariciFormal

section QuarterPointJets

variable {K : Type*} [CommRing K]

/-- First four compact moments obtained from the first four source
coefficients after the quarter-point coordinate change and Jacobian division. -/
def quarterPointMoments (l : Fin 4 → K) : Fin 4 → K
  | 0 => l 0
  | 1 => 2 * l 0 - l 1
  | 2 => l 2 - 3 * l 1 + 6 * l 0
  | 3 => -l 3 + 4 * l 2 - 10 * l 1 + 20 * l 0

/-- The triangular inverse of `quarterPointMoments`. -/
def recoverQuarterPointSource (A : Fin 4 → K) : Fin 4 → K
  | 0 => A 0
  | 1 => 2 * A 0 - A 1
  | 2 => A 2 + 3 * (2 * A 0 - A 1) - 6 * A 0
  | 3 => -A 3 + 4 * (A 2 + 3 * (2 * A 0 - A 1) - 6 * A 0) -
      10 * (2 * A 0 - A 1) + 20 * A 0

theorem recoverQuarterPointSource_moments (l : Fin 4 → K) :
    recoverQuarterPointSource (quarterPointMoments l) = l := by
  funext i
  fin_cases i <;>
    simp [recoverQuarterPointSource, quarterPointMoments] <;> ring

theorem quarterPointMoments_injective :
    Function.Injective (quarterPointMoments : (Fin 4 → K) → Fin 4 → K) := by
  intro l m h
  simpa only [recoverQuarterPointSource_moments] using
    congrArg recoverQuarterPointSource h

/-- The first lower endpoint-localizer determinant. -/
def lowerQuarterPointLocalizerDet (A : Fin 4 → K) : K :=
  A 1 * A 3 - A 2 ^ 2

/-- The first upper endpoint-localizer determinant for support bound four. -/
def upperQuarterPointLocalizerDet (A : Fin 4 → K) : K :=
  (4 * A 0 - A 1) * (4 * A 2 - A 3) - (4 * A 1 - A 2) ^ 2

/-- Positive individual rational moments do not force lower-localizer
positivity; coupled positivity is an additional condition. -/
theorem positiveMoments_do_not_force_lowerLocalizer :
    let A : Fin 4 → Rat := ![1, 1, 2, 1]
    (∀ i, 0 < A i) ∧ lowerQuarterPointLocalizerDet A < 0 := by
  dsimp [lowerQuarterPointLocalizerDet]
  constructor
  · intro i
    fin_cases i <;> norm_num
  · norm_num

end QuarterPointJets

end MariciFormal
