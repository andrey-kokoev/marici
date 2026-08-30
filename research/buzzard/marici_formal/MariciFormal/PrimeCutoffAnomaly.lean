import Mathlib.Algebra.BigOperators.Group.Finset.Basic
import Mathlib.Tactic

/-!
Finite exact-cocycle core of Grothendieck's prime-cutoff adjoint anomaly.
Prime logarithms and complex exponentials are not needed for this layer.
-/

namespace MariciFormal

open Finset
open scoped BigOperators

section ExactCutoffCocycle

variable {Label R : Type*} [DecidableEq Label] [CommRing R]

def cutoffAnomaly (displacement : R) (weight : Label → R)
    (cutoff : Finset Label) : R :=
  2 * displacement * ∑ label ∈ cutoff, weight label

/-- Adding one fresh label has an increment independent of the old cutoff. -/
theorem cutoffAnomaly_insert
    (displacement : R) (weight : Label → R)
    (cutoff : Finset Label) (label : Label) (hfresh : label ∉ cutoff) :
    cutoffAnomaly displacement weight (insert label cutoff) -
        cutoffAnomaly displacement weight cutoff =
      2 * displacement * weight label := by
  simp [cutoffAnomaly, sum_insert, hfresh]
  ring

def exactCountercurrent (displacement constant : R) (weight : Label → R)
    (cutoff : Finset Label) : R :=
  constant - cutoffAnomaly displacement weight cutoff

theorem anomaly_add_countercurrent
    (displacement constant : R) (weight : Label → R)
    (cutoff : Finset Label) :
    cutoffAnomaly displacement weight cutoff +
        exactCountercurrent displacement constant weight cutoff = constant := by
  simp [exactCountercurrent]

theorem exactCountercurrent_insert
    (displacement constant : R) (weight : Label → R)
    (cutoff : Finset Label) (label : Label) (hfresh : label ∉ cutoff) :
    exactCountercurrent displacement constant weight (insert label cutoff) -
        exactCountercurrent displacement constant weight cutoff =
      -(2 * displacement * weight label) := by
  simp [exactCountercurrent, cutoffAnomaly, sum_insert, hfresh]
  ring

/-- Every path-independent scalar countercurrent with the required fresh-label
increments differs from the canonical countercurrent by its value at the empty
cutoff. -/
theorem countercurrent_unique
    (displacement : R) (weight : Label → R) (countercurrent : Finset Label → R)
    (hincrement : ∀ cutoff label, label ∉ cutoff →
      countercurrent (insert label cutoff) - countercurrent cutoff =
        -(2 * displacement * weight label)) :
    ∀ cutoff, countercurrent cutoff =
      countercurrent ∅ - cutoffAnomaly displacement weight cutoff := by
  intro cutoff
  induction cutoff using Finset.induction_on with
  | empty => simp [cutoffAnomaly]
  | @insert label cutoff hfresh ih =>
      rw [cutoffAnomaly, sum_insert hfresh]
      have hstep := hincrement cutoff label hfresh
      rw [ih] at hstep ⊢
      simp only [cutoffAnomaly] at hstep
      ring_nf at hstep ⊢
      linear_combination hstep

end ExactCutoffCocycle

section Hostile

def twoLabelWeight (_ : Fin 2) : ℤ := 1

/-- Exact cancellation can hold at a nonzero displacement, so this conserved
charge alone cannot select the seam. -/
theorem zero_total_charge_offSeam_hostile :
    let displacement : ℤ := 1
    let cutoff : Finset (Fin 2) := Finset.univ
    let anomaly := cutoffAnomaly displacement twoLabelWeight cutoff
    let countercurrent := exactCountercurrent displacement 0 twoLabelWeight cutoff
    displacement ≠ 0 ∧ anomaly + countercurrent = 0 := by
  norm_num [cutoffAnomaly, exactCountercurrent, twoLabelWeight]

end Hostile

end MariciFormal
