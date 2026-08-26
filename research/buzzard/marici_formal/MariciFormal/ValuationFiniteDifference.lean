import Mathlib.Algebra.Group.Hom.End
import Mathlib.Algebra.BigOperators.Group.Finset.Basic
import Mathlib.Tactic.Abel

/-!
Finite-difference and polarization core of Grothendieck's theta valuation
routes.  All results are algebraic; no theta convergence, seam regularity, or
positivity is assumed.
-/

namespace MariciFormal

open scoped BigOperators

section OneDimensionalReconstruction

variable {A : Type*} [AddCommGroup A]

/-- The exact valuation cell is the forward difference of two nested tail
routes. -/
def valuationCell (tail : ℕ → A) (j : ℕ) : A :=
  tail j - tail (j + 1)

/-- A capped valuation chart consists of its exact interior cells and its
overflow tail. Their sum reconstructs the undecomposed source. -/
theorem valuation_cells_telescope (tail : ℕ → A) (cap : ℕ) :
    (∑ j ∈ Finset.range cap, valuationCell tail j) + tail cap = tail 0 := by
  induction cap with
  | zero => simp
  | succ cap ih =>
      rw [Finset.sum_range_succ]
      unfold valuationCell
      calc
        ((∑ j ∈ Finset.range cap, tail j - tail (j + 1)) +
              (tail cap - tail (cap + 1))) + tail (cap + 1) =
            (∑ j ∈ Finset.range cap, tail j - tail (j + 1)) + tail cap := by
              abel
        _ = tail 0 := by simpa [valuationCell] using ih

end OneDimensionalReconstruction

section BilinearReconstruction

variable {A C : Type*} [AddCommGroup A] [AddCommGroup C]

/-- A bilinear companion channel represented without analytic structure. -/
abbrev AddBilinear (A C : Type*) [AddCommGroup A] [AddCommGroup C] :=
  A →+ A →+ C

/-- Double finite difference recovers an exact valuation-pair channel from
four mixed tail-route observations. -/
theorem bilinear_valuationCell_expansion
    (B : AddBilinear A C) (left right : ℕ → A) (j k : ℕ) :
    B (valuationCell left j) (valuationCell right k) =
      B (left j) (right k) - B (left (j + 1)) (right k) -
        B (left j) (right (k + 1)) +
          B (left (j + 1)) (right (k + 1)) := by
  simp [valuationCell]
  abel

/-- Polarization exposes the two cross-label repair channels forced by
source addition. -/
theorem bilinear_polarization (B : AddBilinear A C) (F G : A) :
    B (F + G) (F + G) =
      B F F + B G G + B F G + B G F := by
  simp
  abel

end BilinearReconstruction

section DiagonalOnlyHostile

/-- Diagonal packets do not determine the companion of a sum: multiplication
on the integers has two nonzero cross terms at `(1,1)`. -/
theorem diagonal_only_loses_cross_repair :
    ((1 + 1 : ℤ) * (1 + 1)) ≠ (1 * 1 + 1 * 1 : ℤ) := by
  norm_num

end DiagonalOnlyHostile

end MariciFormal
