import Mathlib

/-!
The first-nonzero-jet covariance theorem as finite lower-triangular algebra.
This does not assume an analytic section or a uniform multiplicity bound.
-/

namespace MariciFormal

section TriangularGauge

variable {K : Type*} [Field K]

/-- The `m`th transformed jet: contragredient leading term plus lower corrections. -/
def transformedJet
    (correction : Nat → Nat → K) (r : K) (jet : Nat → K) (m : Nat) : K :=
  jet m / r + ∑ k ∈ Finset.range m, correction m k * jet k

/-- `m` is the first index carrying a nonzero jet. -/
def FirstNonzeroAt (jet : Nat → K) (m : Nat) : Prop :=
  (∀ k < m, jet k = 0) ∧ jet m ≠ 0

/-- Lower-triangular corrections vanish at the first nonzero jet. -/
theorem transformedJet_eq_div_at_first_nonzero
    (correction : Nat → Nat → K) (r : K) (jet : Nat → K) (m : Nat)
    (first : FirstNonzeroAt jet m) :
    transformedJet correction r jet m = jet m / r := by
  unfold transformedJet
  rw [Finset.sum_eq_zero]
  · simp
  · intro k hk
    have hkm : k < m := Finset.mem_range.mp hk
    rw [first.1 k hkm, mul_zero]

/-- A nonzero gauge preserves the first-nonzero order for every triangular correction. -/
theorem firstNonzeroAt_transformedJet
    (correction : Nat → Nat → K) {r : K} (jet : Nat → K) (m : Nat)
    (hr : r ≠ 0) (first : FirstNonzeroAt jet m) :
    FirstNonzeroAt (transformedJet correction r jet) m := by
  constructor
  · intro k hkm
    unfold transformedJet
    rw [first.1 k hkm, zero_div, zero_add]
    apply Finset.sum_eq_zero
    intro l hl
    rw [first.1 l (lt_trans (Finset.mem_range.mp hl) hkm), mul_zero]
  · rw [transformedJet_eq_div_at_first_nonzero correction r jet m first]
    exact div_ne_zero first.2 hr

end TriangularGauge

section FiniteDepthHostile

/-- A section whose first nonzero formal coefficient lies just beyond depth `d`. -/
def beyondDepthJet (d : Nat) : Nat → Rat := fun n =>
  if n = d + 1 then 1 else 0

theorem beyondDepthJet_vanishes_through (d : Nat) :
    ∀ n ≤ d, beyondDepthJet d n = 0 := by
  intro n hn
  have hne : n ≠ d + 1 := by omega
  simp [beyondDepthJet, hne]

theorem beyondDepthJet_first_nonzero (d : Nat) :
    FirstNonzeroAt (beyondDepthJet d) (d + 1) := by
  constructor
  · intro n hn
    have hne : n ≠ d + 1 := by omega
    simp [beyondDepthJet, hne]
  · simp [beyondDepthJet]

/-- No fixed finite inspection depth detects every nonzero formal jet family. -/
theorem everyFiniteJetDepthHasAHostileSection :
    ∀ d : Nat, ∃ jet : Nat → Rat,
      (∀ n ≤ d, jet n = 0) ∧ jet (d + 1) ≠ 0 := by
  intro d
  exact ⟨beyondDepthJet d, beyondDepthJet_vanishes_through d,
    (beyondDepthJet_first_nonzero d).2⟩

end FiniteDepthHostile

end MariciFormal
