import Mathlib

/-!
Finite atomic core of the Hausdorff complete-monotonicity criterion.

The recursively signed forward differences retain the upper support condition:
for atoms in `[0, 1]` they are integrals of `x^k (1-x)^j`.  This file does
not invoke the infinite Hausdorff moment theorem or identify a source jet with
the completed Xi resolvent.
-/

namespace MariciFormal

section FiniteHausdorff

variable {K : Type*} [LinearOrderedField K]
variable {I : Type*} [Fintype I]

/-- The signed forward difference `(-1)^j Delta^j m_k`, defined recursively
without choosing a binomial presentation. -/
def signedMomentDifference (moment : Nat → K) (k : Nat) : Nat → K
  | 0 => moment k
  | j + 1 => signedMomentDifference moment k j -
      signedMomentDifference moment (k + 1) j

/-- The moments of a finite atomic family. -/
def finiteHausdorffMoment (weight atom : I → K) (k : Nat) : K :=
  ∑ i, weight i * atom i ^ k

/-- Signed differences of finite atomic moments are exactly the mixed
monomials that remember both endpoints of `[0, 1]`. -/
theorem signedMomentDifference_finiteAtomic
    (weight atom : I → K) (k j : Nat) :
    signedMomentDifference (finiteHausdorffMoment weight atom) k j =
      ∑ i, weight i * atom i ^ k * (1 - atom i) ^ j := by
  induction j generalizing k with
  | zero => simp [signedMomentDifference, finiteHausdorffMoment]
  | succ j ih =>
      rw [signedMomentDifference, ih, ih, ← Finset.sum_sub_distrib]
      apply Finset.sum_congr rfl
      intro i hi
      rw [pow_succ (1 - atom i)]
      ring

/-- Nonnegative atoms supported in `[0, 1]` satisfy every finite Hausdorff
complete-monotonicity inequality. -/
theorem signedMomentDifference_nonnegative
    (weight atom : I → K) (hweight : ∀ i, 0 ≤ weight i)
    (hatom0 : ∀ i, 0 ≤ atom i) (hatom1 : ∀ i, atom i ≤ 1)
    (k j : Nat) :
    0 ≤ signedMomentDifference (finiteHausdorffMoment weight atom) k j := by
  rw [signedMomentDifference_finiteAtomic]
  apply Finset.sum_nonneg
  intro i hi
  exact mul_nonneg
    (mul_nonneg (hweight i) (pow_nonneg (hatom0 i) _))
    (pow_nonneg (sub_nonneg.mpr (hatom1 i)) _)

/-- Positive weights and positive moments do not encode the upper support
bound: a unit atom at `2` violates the first Hausdorff difference. -/
theorem positiveMoments_outsideUnitInterval_failHausdorff :
    let weight : Fin 1 → Rat := fun _ => 1
    let atom : Fin 1 → Rat := fun _ => 2
    (∀ k, 0 < finiteHausdorffMoment weight atom k) ∧
      signedMomentDifference (finiteHausdorffMoment weight atom) 0 1 < 0 := by
  dsimp [finiteHausdorffMoment, signedMomentDifference]
  constructor
  · intro k
    positivity
  · norm_num

/-- The quarter-point second-order Loewner contact coefficient is exactly
sixteen times the first ordinary Hankel determinant once the displayed source
derivatives are supplied. -/
theorem quarterPointLoewnerContact_eq_Hankel
    (A0 A1 A2 : K) :
    (4 * A0) * (24 * A2) / 6 - (-8 * A1) ^ 2 / 4 =
      16 * (A0 * A2 - A1 ^ 2) := by
  ring

end FiniteHausdorff

end MariciFormal
