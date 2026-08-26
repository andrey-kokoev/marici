import Mathlib

/-!
The exact algebraic core of Grothendieck's regular eta-jet reduction.

This file does not define the analytic eta or zeta functions and does not
certify any numerical enclosure.  It proves only that, once a nonzero value
`L` and the first five regular coefficients are supplied with the displayed
relations, the first four Laurent/Stieltjes parameters are recovered by a
triangular rational calculation.
-/

namespace MariciFormal

section EtaJet

variable {K : Type*} [Field K] [CharZero K]

/-- The five regular coefficients obtained by multiplying a simple Laurent
pole by the zero with logarithmic scale `L`. -/
def regularEtaCoefficients (L g0 g1 g2 g3 : K) : Fin 5 → K
  | 0 => L
  | 1 => L * g0 - L ^ 2 / 2
  | 2 => -L * g1 - L ^ 2 * g0 / 2 + L ^ 3 / 6
  | 3 => L * g2 / 2 + L ^ 2 * g1 / 2 + L ^ 3 * g0 / 6 - L ^ 4 / 24
  | 4 => -L * g3 / 6 - L ^ 2 * g2 / 4 - L ^ 3 * g1 / 6 -
      L ^ 4 * g0 / 24 + L ^ 5 / 120

def recoverG0 (L : K) (c : Fin 5 → K) : K :=
  (c 1 + L ^ 2 / 2) / L

def recoverG1 (L : K) (c : Fin 5 → K) : K :=
  -(c 2 + L ^ 2 * recoverG0 L c / 2 - L ^ 3 / 6) / L

def recoverG2 (L : K) (c : Fin 5 → K) : K :=
  2 * (c 3 - L ^ 2 * recoverG1 L c / 2 -
    L ^ 3 * recoverG0 L c / 6 + L ^ 4 / 24) / L

def recoverG3 (L : K) (c : Fin 5 → K) : K :=
  -6 * (c 4 + L ^ 2 * recoverG2 L c / 4 +
    L ^ 3 * recoverG1 L c / 6 + L ^ 4 * recoverG0 L c / 24 -
    L ^ 5 / 120) / L

theorem recoverG0_regularEtaCoefficients
    {L : K} (hL : L ≠ 0) (g0 g1 g2 g3 : K) :
    recoverG0 L (regularEtaCoefficients L g0 g1 g2 g3) = g0 := by
  simp [recoverG0, regularEtaCoefficients]
  field_simp
  ring

theorem recoverG1_regularEtaCoefficients
    {L : K} (hL : L ≠ 0) (g0 g1 g2 g3 : K) :
    recoverG1 L (regularEtaCoefficients L g0 g1 g2 g3) = g1 := by
  simp [recoverG1, recoverG0, regularEtaCoefficients]
  field_simp
  ring

theorem recoverG2_regularEtaCoefficients
    {L : K} (hL : L ≠ 0) (g0 g1 g2 g3 : K) :
    recoverG2 L (regularEtaCoefficients L g0 g1 g2 g3) = g2 := by
  simp [recoverG2, recoverG1, recoverG0, regularEtaCoefficients]
  field_simp
  ring

theorem recoverG3_regularEtaCoefficients
    {L : K} (hL : L ≠ 0) (g0 g1 g2 g3 : K) :
    recoverG3 L (regularEtaCoefficients L g0 g1 g2 g3) = g3 := by
  simp [recoverG3, recoverG2, recoverG1, recoverG0,
    regularEtaCoefficients]
  field_simp
  ring

/-- At fixed nonzero logarithmic scale, the regular eta coefficients retain
all four Laurent parameters. -/
theorem regularEtaCoefficients_injective
    {L : K} (hL : L ≠ 0) :
    Function.Injective (fun p : Fin 4 → K =>
      regularEtaCoefficients L (p 0) (p 1) (p 2) (p 3)) := by
  intro p q hpq
  funext i
  fin_cases i
  · simpa [recoverG0_regularEtaCoefficients hL] using
      congrArg (recoverG0 L) hpq
  · simpa [recoverG1_regularEtaCoefficients hL] using
      congrArg (recoverG1 L) hpq
  · simpa [recoverG2_regularEtaCoefficients hL] using
      congrArg (recoverG2 L) hpq
  · simpa [recoverG3_regularEtaCoefficients hL] using
      congrArg (recoverG3 L) hpq

end EtaJet

end MariciFormal
