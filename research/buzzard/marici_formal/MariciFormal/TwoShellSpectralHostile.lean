import Mathlib.Analysis.SpecialFunctions.Hyperbolic.Basic
import Mathlib.Tactic.NormNum

/-!
Finite algebraic and real-velocity core of Grothendieck's reciprocal shell
hostiles. The complex `cosh` quotient lift is deliberately not inferred.
-/

namespace MariciFormal

section QuotientPolynomial

variable {R : Type*} [CommRing R]

def twoShellQuotient (outerWeight quotient : R) : R :=
  2 * outerWeight * quotient ^ 2 + quotient - outerWeight

end QuotientPolynomial

/-- Positive decreasing shell weights can already produce a quotient root
strictly below `-1`. The rational choice avoids importing a square-root
formula. -/
theorem positive_twoShell_offSeam_quotient_hostile :
    (0 : ℚ) < 2 / 7 ∧ (2 / 7 : ℚ) < 1 ∧ (-2 : ℚ) < -1 ∧
      twoShellQuotient (2 / 7 : ℚ) (-2) = 0 := by
  norm_num [twoShellQuotient]

section TransportedShellVelocity

def shellValueAtOddPhase (k : ℕ) (horizontal : ℝ) : ℝ :=
  (-1 : ℝ) ^ k * Real.cosh ((k : ℝ) * horizontal)

def simpleZeroVelocity
    (shellValue baseDerivative : ℝ) : ℝ :=
  -shellValue / baseDerivative

/-- At the hostile phase, a positive third shell has negative transported
value and hence positive horizontal velocity when the base derivative is
positive. -/
theorem third_positive_shell_moves_outward
    (horizontal baseDerivative : ℝ) (hbase : 0 < baseDerivative) :
    0 < simpleZeroVelocity (shellValueAtOddPhase 3 horizontal) baseDerivative := by
  simp only [simpleZeroVelocity, shellValueAtOddPhase]
  norm_num
  exact div_pos (Real.cosh_pos _) hbase

def oddEvenBlockAtOddPhase
    (innerOdd outerEven : ℝ) (m : ℕ) (horizontal : ℝ) : ℝ :=
  -innerOdd * Real.cosh (((2 * m + 1 : ℕ) : ℝ) * horizontal) +
    outerEven * Real.cosh (((2 * m + 2 : ℕ) : ℝ) * horizontal)

/-- Outer-even dominance is already necessary at the seam endpoint: if the
outer coefficient is smaller, the paired transported value has the wrong
sign at horizontal displacement zero. -/
theorem oddEvenBlock_wrong_sign_at_seam_of_outer_lt
    (innerOdd outerEven : ℝ) (m : ℕ) (hdom : outerEven < innerOdd) :
    oddEvenBlockAtOddPhase innerOdd outerEven m 0 < 0 := by
  simp [oddEvenBlockAtOddPhase]
  linarith

end TransportedShellVelocity

end MariciFormal
