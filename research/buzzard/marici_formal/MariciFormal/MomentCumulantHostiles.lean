import Mathlib

/-!
Finite rational hostiles separating positive even source measures from the
nonlinear cumulant and Loewner conditions used in Grothendieck's Xi packets.

These examples do not model the Riemann theta density.  They refute only the
proposed universal implications from positivity and evenness alone.
-/

namespace MariciFormal

/-- Three-point symmetric probability fixture with mass `3/4` at zero and
mass `1/8` at each of `-1` and `1`. -/
def sparseEvenWeight : Fin 3 → Rat := ![1 / 8, 3 / 4, 1 / 8]

def sparseEvenAtom : Fin 3 → Rat := ![-1, 0, 1]

def finiteMoment {n : Nat} (weight atom : Fin n → Rat) (k : Nat) : Rat :=
  ∑ i, weight i * atom i ^ k

theorem sparseEvenWeight_nonnegative :
    ∀ i, 0 ≤ sparseEvenWeight i := by
  intro i
  fin_cases i <;> norm_num [sparseEvenWeight]

theorem sparseEvenWeight_total :
    ∑ i, sparseEvenWeight i = 1 := by
  decide

theorem sparseEvenFixture_is_symmetric :
    sparseEvenWeight 0 = sparseEvenWeight 2 ∧
      sparseEvenAtom 0 = -sparseEvenAtom 2 := by
  norm_num [sparseEvenWeight, sparseEvenAtom]

/-- The first nonlinear Stieltjes cumulant condition fails despite positivity
and reflection symmetry of the source probability measure. -/
theorem sparseEvenFixture_fails_firstCumulantGate :
    let m2 := finiteMoment sparseEvenWeight sparseEvenAtom 2
    let m4 := finiteMoment sparseEvenWeight sparseEvenAtom 4
    m2 = 1 / 4 ∧ m4 = 1 / 4 ∧ 3 * m2 ^ 2 - m4 < 0 := by
  norm_num [finiteMoment, sparseEvenWeight, sparseEvenAtom]

/-- Exact derivative data from the symmetric four-atom Loewner hostile. -/
def fourAtomF1 : Rat := 821 / 150
def fourAtomF2 : Rat := -854 / 375
def fourAtomF3 : Rat := 14261 / 13125

theorem fourAtom_firstDerivative_positive : 0 < fourAtomF1 := by
  norm_num [fourAtomF1]

/-- Positive first derivative does not force the first diagonal Loewner
curvature condition, even for the positive even four-atom source fixture. -/
theorem fourAtom_fails_LoewnerCurvature :
    2 * fourAtomF1 * fourAtomF3 - 3 * fourAtomF2 ^ 2 =
      -721471 / 196875 ∧
    fourAtomF1 * fourAtomF3 / 6 - fourAtomF2 ^ 2 / 4 < 0 := by
  norm_num [fourAtomF1, fourAtomF2, fourAtomF3]

end MariciFormal
