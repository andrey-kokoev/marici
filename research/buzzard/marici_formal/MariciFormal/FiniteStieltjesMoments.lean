import Mathlib

/-!
Finite atomic core of the Stieltjes moment hierarchy.

This file proves Gram positivity for a finite nonnegative atomic measure and
keeps the ordinary and shifted Hankel forms distinct.  It does not invoke the
Stieltjes moment theorem, construct an infinite measure, establish moment
determinacy, or make an RH assertion.
-/

namespace MariciFormal

section FiniteAtomicMoments

variable {K : Type*} [LinearOrderedField K]
variable {I : Type*} [Fintype I]

/-- The `k`th moment of a finite weighted atomic family. -/
def finiteAtomicMoment (weight atom : I → K) (k : Nat) : K :=
  ∑ i, weight i * atom i ^ k

/-- A finite Hankel quadratic form is the sum of the corresponding weighted
squares. -/
theorem finiteHankelForm_eq_sum_squares
    (weight atom : I → K) {n : Nat} (c : Fin n → K) :
    (∑ a, ∑ b, c a * c b * finiteAtomicMoment weight atom (a.val + b.val)) =
      ∑ i, weight i * (∑ a, c a * atom i ^ a.val) ^ 2 := by
  simp only [finiteAtomicMoment, pow_add]
  simp_rw [Finset.mul_sum]
  rw [Finset.sum_comm]
  apply Finset.sum_congr rfl
  intro i hi
  ring

/-- Nonnegative atomic weights make every finite ordinary Hankel form
nonnegative. -/
theorem finiteHankelForm_nonnegative
    (weight atom : I → K) (hweight : ∀ i, 0 ≤ weight i)
    {n : Nat} (c : Fin n → K) :
    0 ≤ ∑ a, ∑ b, c a * c b *
      finiteAtomicMoment weight atom (a.val + b.val) := by
  rw [finiteHankelForm_eq_sum_squares]
  exact Finset.sum_nonneg fun i _ => mul_nonneg (hweight i) (sq_nonneg _)

/-- The shifted Hankel form is a different Gram form: its atomic weight is
`weight i * atom i`, so support nonnegativity is an additional premise. -/
theorem finiteShiftedHankelForm_nonnegative
    (weight atom : I → K) (hweight : ∀ i, 0 ≤ weight i)
    (hatom : ∀ i, 0 ≤ atom i) {n : Nat} (c : Fin n → K) :
    0 ≤ ∑ a, ∑ b, c a * c b *
      finiteAtomicMoment weight atom (a.val + b.val + 1) := by
  have hmoment : ∀ k,
      finiteAtomicMoment weight atom (k + 1) =
        finiteAtomicMoment (fun i => weight i * atom i) atom k := by
    intro k
    simp only [finiteAtomicMoment, pow_succ']
    apply Finset.sum_congr rfl
    intro i hi
    ring
  simp_rw [hmoment]
  apply finiteHankelForm_nonnegative (fun i => weight i * atom i) atom
  intro i
  exact mul_nonneg (hweight i) (hatom i)

/-- Componentwise nonnegative data need not be a Stieltjes moment sequence:
the first ordinary Hankel determinant can already be negative. -/
theorem nonnegativeEntries_do_not_force_HankelPositivity :
    let D : Fin 3 → Rat := ![1, 1, 1 / 2]
    (∀ i, 0 ≤ D i) ∧ D 0 * D 2 - D 1 ^ 2 < 0 := by
  dsimp
  constructor
  · intro i
    fin_cases i <;> norm_num
  · norm_num

end FiniteAtomicMoments

section OrderTwoBoundaryAtom

variable {K : Type*} [Field K] [CharZero K]

/-- The atomwise algebra behind the reverse order-two boundary transform. -/
theorem orderTwoBoundary_reverse_atom
    (x lambda : K) (hx : 4 * x - 1 ≠ 0)
    (hlambda : 1 + 4 * lambda ≠ 0) (hxlambda : x + lambda ≠ 0) :
    (4 / (1 + 4 * lambda) - 1 / (x + lambda)) / (4 * x - 1) =
      1 / ((1 + 4 * lambda) * (x + lambda)) := by
  field_simp
  ring

/-- Weight transport in the forward and reverse directions is inverse when
the boundary factor is nonzero. -/
theorem orderTwoBoundary_weight_roundtrip
    (lambda weight : K) (hlambda : 1 + 4 * lambda ≠ 0) :
    ((1 + 4 * lambda) * weight) / (1 + 4 * lambda) = weight := by
  exact mul_div_cancel_left₀ weight hlambda

end OrderTwoBoundaryAtom

end MariciFormal
