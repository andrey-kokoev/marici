import Mathlib.Algebra.BigOperators.Group.Finset.Basic
import Mathlib.Tactic.NormNum
import Mathlib.Tactic.Ring

/-!
Finite weighted-prefix core of Grothendieck's prime-translation boundary
cocycle. Prime asymptotics and restricted-product completion are not inputs.
-/

namespace MariciFormal

open Finset
open scoped BigOperators

section WeightedPrefix

variable {R : Type*} [CommRing R]

def weightedBoundaryPrefix (phase : R) (source : ℕ → R) (length : ℕ) : R :=
  ∑ k ∈ range length, phase ^ k * source k

def shiftedBoundarySource (source : ℕ → R) (offset : ℕ) : ℕ → R :=
  fun k => source (offset + k)

/-- The discrete exact analogue of boundary-interval concatenation. -/
theorem weightedBoundaryPrefix_add
    (phase : R) (source : ℕ → R) (first second : ℕ) :
    weightedBoundaryPrefix phase source (first + second) =
      weightedBoundaryPrefix phase source first +
        phase ^ first *
          weightedBoundaryPrefix phase (shiftedBoundarySource source first) second := by
  simp only [weightedBoundaryPrefix, shiftedBoundarySource, sum_range_add,
    mul_sum]
  apply congrArg (weightedBoundaryPrefix phase source first + ·)
  apply sum_congr rfl
  intro k hk
  rw [pow_add]
  ring

/-- Two staged cuts have no finite cocycle anomaly: both reconstruct the same
full prefix. -/
theorem two_stage_boundary_paths_agree
    (phase : R) (source : ℕ → R) (first second : ℕ) :
    weightedBoundaryPrefix phase source first +
        phase ^ first *
          weightedBoundaryPrefix phase (shiftedBoundarySource source first) second =
      weightedBoundaryPrefix phase source (first + second) := by
  symm
  exact weightedBoundaryPrefix_add phase source first second

end WeightedPrefix

section Hostile

def cancellingBoundarySource : ℕ → ℤ
  | 0 => 1
  | 1 => -1
  | _ => 0

/-- Vanishing of the aggregated boundary packet does not erase its proper
prefix, hence it does not imply termwise or intervalwise vanishing. -/
theorem zero_total_with_nonzero_boundary_prefix :
    weightedBoundaryPrefix (R := ℤ) 1 cancellingBoundarySource 2 = 0 ∧
      weightedBoundaryPrefix (R := ℤ) 1 cancellingBoundarySource 1 = 1 := by
  norm_num [weightedBoundaryPrefix, cancellingBoundarySource, Finset.sum_range_succ]

end Hostile

end MariciFormal
