import Mathlib.Algebra.BigOperators.Group.Finset.Basic
import Mathlib.Tactic.NormNum
import Mathlib.Tactic.Ring

/-!
Canonical coefficient--Betti quarter-turn from Grothendieck's paired
polarization packet.  The real half-rotation and metaplectic phase remain
separate analytic/representation-theoretic data.
-/

namespace MariciFormal

open scoped BigOperators

section FinitePolarization

variable {X R : Type*} [Fintype X] [CommRing R]

abbrev PolarizationDouble (X R : Type*) := (X → R) × (X → R)

/-- The first component is the coefficient polarization and the second is
the Betti polarization. -/
def polarizationQuarterTurn
    (v : PolarizationDouble X R) : PolarizationDouble X R :=
  (-v.2, v.1)

def canonicalSymplecticForm
    (v w : PolarizationDouble X R) : R :=
  ∑ x, v.1 x * w.2 x - w.1 x * v.2 x

theorem polarizationQuarterTurn_sq
    (v : PolarizationDouble X R) :
    polarizationQuarterTurn (polarizationQuarterTurn v) = -v := by
  apply Prod.ext <;> funext x <;> simp [polarizationQuarterTurn]

theorem polarizationQuarterTurn_preserves_symplectic
    (v w : PolarizationDouble X R) :
    canonicalSymplecticForm (polarizationQuarterTurn v)
        (polarizationQuarterTurn w) =
      canonicalSymplecticForm v w := by
  unfold canonicalSymplecticForm
  apply Finset.sum_congr rfl
  intro x hx
  simp [polarizationQuarterTurn]
  ring

def InCoefficientPolarization (v : PolarizationDouble X R) : Prop :=
  v.2 = 0

def InBettiPolarization (v : PolarizationDouble X R) : Prop :=
  v.1 = 0

theorem quarterTurn_coefficient_to_betti
    (v : PolarizationDouble X R) (h : InCoefficientPolarization v) :
    InBettiPolarization (polarizationQuarterTurn v) := by
  simpa [InCoefficientPolarization, InBettiPolarization,
    polarizationQuarterTurn] using congrArg (fun f => -f) h

theorem quarterTurn_betti_to_coefficient
    (v : PolarizationDouble X R) (h : InBettiPolarization v) :
    InCoefficientPolarization (polarizationQuarterTurn v) := by
  simpa [InCoefficientPolarization, InBettiPolarization,
    polarizationQuarterTurn] using h

end FinitePolarization

section SelectionHostile

def polarizationTestVector : PolarizationDouble PUnit ℤ :=
  (fun _ => 1, fun _ => 0)

/-- The canonical quarter-turn is nontrivial, while the identity also
preserves the symplectic form. Algebraic symplecticity therefore does not by
itself select a half-rotation path or one of its metaplectic lifts. -/
theorem polarizationQuarterTurn_ne_identity :
    polarizationQuarterTurn polarizationTestVector ≠
      polarizationTestVector := by
  intro h
  have hfirst := congrArg (fun v => v.1 PUnit.unit) h
  norm_num [polarizationQuarterTurn, polarizationTestVector] at hfirst

theorem identity_preserves_canonicalSymplectic
    {X R : Type*} [Fintype X] [CommRing R]
    (v w : PolarizationDouble X R) :
    canonicalSymplecticForm v w = canonicalSymplecticForm v w := by
  rfl

end SelectionHostile

end MariciFormal
