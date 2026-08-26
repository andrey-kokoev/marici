import Mathlib.Data.Complex.Basic
import Mathlib.Tactic.Ring

/-!
Finite boundary-phase algebra from Grothendieck's real-structure no-go.
Plain conjugation restricts a unit phase to the two real signs, while
reflection-conjugation adds no condition beyond unit modulus.
-/

namespace MariciFormal

def IsUnitBoundaryPhase (phase : ℂ) : Prop :=
  phase * Complex.conj phase = 1

def PlainConjugationInvariant (phase : ℂ) : Prop :=
  Complex.conj phase = phase

def ReflectionConjugationInvariant (phase : ℂ) : Prop :=
  phase * Complex.conj phase = 1

/-- A unit phase fixed by plain conjugation is one of the two real signs. -/
theorem plainConjugation_unitPhase_eq_one_or_neg_one
    (phase : ℂ) (hunit : IsUnitBoundaryPhase phase)
    (hreal : PlainConjugationInvariant phase) :
    phase = 1 ∨ phase = -1 := by
  have hsquare : phase ^ 2 = 1 := by
    unfold IsUnitBoundaryPhase PlainConjugationInvariant at hunit hreal
    rw [hreal] at hunit
    simpa [pow_two] using hunit
  have hfactor : (phase - 1) * (phase + 1) = 0 := by
    calc
      (phase - 1) * (phase + 1) = phase ^ 2 - 1 := by ring
      _ = 0 := by rw [hsquare]; ring
  rcases mul_eq_zero.mp hfactor with hplus | hminus
  · exact Or.inl (sub_eq_zero.mp hplus)
  · exact Or.inr (eq_neg_of_add_eq_zero_left hminus)

/-- Reflection-conjugation preserves every unit phase, so it cannot select a
distinguished member of the extension family. -/
theorem every_unitPhase_is_reflectionConjugationInvariant
    (phase : ℂ) (hunit : IsUnitBoundaryPhase phase) :
    ReflectionConjugationInvariant phase := hunit

theorem reflectionConjugation_admits_distinct_phases :
    ReflectionConjugationInvariant 1 ∧
      ReflectionConjugationInvariant Complex.I ∧
      (1 : ℂ) ≠ Complex.I := by
  constructor
  · norm_num [ReflectionConjugationInvariant]
  constructor
  · norm_num [ReflectionConjugationInvariant, Complex.conj_I]
  · intro h
    have him := congrArg Complex.im h
    norm_num at him

end MariciFormal
