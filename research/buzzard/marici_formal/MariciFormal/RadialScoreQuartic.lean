import Mathlib.Tactic.FieldSimp
import Mathlib.Tactic.Ring

/-!
Denominator-clearing algebra from Grothendieck's theta radial-score quartic
packet. The cleared obstruction is homogeneous of source degree four; no sign
of that quartic expression is assumed.
-/

namespace MariciFormal

variable {K : Type*} [Field K]

def radialPotentialScore (f a : K) : K := -a / f

def radialPotentialScoreDerivative (f a b : K) : K :=
  (a ^ 2 - f * b) / f ^ 2

def radialPotentialScoreSecondDerivative (f a b c : K) : K :=
  (3 * f * a * b - 2 * a ^ 3 - f ^ 2 * c) / f ^ 3

def radialScoreCurvatureNumerator
    (u f a b c : K) : K :=
  u ^ 2 *
      (radialPotentialScoreDerivative f a b ^ 2 -
        radialPotentialScore f a *
          radialPotentialScoreSecondDerivative f a b c) +
    u * radialPotentialScore f a * radialPotentialScoreDerivative f a b -
    2 * radialPotentialScore f a ^ 2

def radialScoreQuartic (u f a b c : K) : K :=
  u ^ 2 * (-a ^ 4 + f * a ^ 2 * b + f ^ 2 * (b ^ 2 - a * c)) +
    u * (-f * a ^ 3 + f ^ 2 * a * b) - 2 * f ^ 2 * a ^ 2

/-- Clearing the four powers of the source denominator produces the exact
quartic polynomial in the source and its first three derivatives. -/
theorem radialScore_denominator_clearing
    (u f a b c : K) (hf : f ≠ 0) :
    f ^ 4 * radialScoreCurvatureNumerator u f a b c =
      radialScoreQuartic u f a b c := by
  unfold radialScoreCurvatureNumerator radialPotentialScore
    radialPotentialScoreDerivative radialPotentialScoreSecondDerivative
    radialScoreQuartic
  field_simp [hf]
  ring

end MariciFormal
