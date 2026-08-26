import Mathlib.Algebra.BigOperators.Group.Finset.Basic
import Mathlib.Data.Fin.Basic
import Mathlib.Tactic.FinCases

/-!
Finite pull--push core of Grothendieck's capped valuation refinements.

This file only formalizes the coefficient correspondence. It does not assert
that a refinement is a physical decomposition, that a seam-compatible packet
is positive, or that the scalar companion satisfies the cubic inequality.
-/

namespace MariciFormal

open scoped BigOperators

section PullPush

variable {Fine Coarse R : Type*}
variable [Fintype Fine] [Fintype Coarse] [DecidableEq Coarse]
variable [AddCommMonoid R]

def coefficientPullback (q : Fine → Coarse) (c : Coarse → R) : Fine → R :=
  fun i => c (q i)

def packetPushforward (q : Fine → Coarse) (v : Fine → R) : Coarse → R :=
  fun a => ∑ i ∈ Finset.univ.filter (fun i => q i = a), v i

def fiberNorm (q : Fine → Coarse) (c : Coarse → R) : Coarse → R :=
  fun a => (Finset.univ.filter (fun i => q i = a)).card • c a

/-- Pull followed by push is the diagonal fiber norm. -/
theorem packetPushforward_coefficientPullback
    (q : Fine → Coarse) (c : Coarse → R) :
    packetPushforward q (coefficientPullback q c) = fiberNorm q c := by
  funext a
  simp [packetPushforward, coefficientPullback, fiberNorm]

end PullPush

section SeamKernel

variable {Fine Coarse R : Type*}
variable [Fintype Fine] [Fintype Coarse]
variable [CommSemiring R]

def seamCompatible (b c : Fine → R) : Prop :=
  ∑ i, c i * b i = 0

/-- This is the exact coefficient interface
`(b_fine)^* q^* = (b_coarse)^*`. -/
def SeamCovariant (q : Fine → Coarse)
    (bFine : Fine → R) (bCoarse : Coarse → R) : Prop :=
  ∀ c, (∑ i, coefficientPullback q c i * bFine i) =
    ∑ a, c a * bCoarse a

theorem seamCompatible_pullback
    (q : Fine → Coarse) (bFine : Fine → R) (bCoarse c : Coarse → R)
    (hcovariant : SeamCovariant q bFine bCoarse)
    (hseam : seamCompatible bCoarse c) :
    seamCompatible bFine (coefficientPullback q c) := by
  unfold seamCompatible
  rw [hcovariant c]
  exact hseam

/-- A refinement map alone does not create nonzero source data. -/
theorem zero_seam_covector_is_covariant
    (q : Fine → Coarse) :
    SeamCovariant q (fun _ => (0 : R)) (fun _ => 0) := by
  intro c
  simp [coefficientPullback]

end SeamKernel

section NonuniformHostile

def nonuniformRefinement : Fin 3 → Fin 2
  | 0 => 0
  | 1 => 0
  | 2 => 1

def unitCoarsePacket : Fin 2 → ℕ := fun _ => 1

/-- Nonuniform refinement yields a diagonal norm, not one scalar norm. -/
theorem nonuniform_fiber_norm_is_not_uniform :
    packetPushforward nonuniformRefinement
        (coefficientPullback nonuniformRefinement unitCoarsePacket) 0 = 2 ∧
      packetPushforward nonuniformRefinement
        (coefficientPullback nonuniformRefinement unitCoarsePacket) 1 = 1 := by
  decide

end NonuniformHostile

end MariciFormal
