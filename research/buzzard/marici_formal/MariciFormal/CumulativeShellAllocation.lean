import Mathlib.Algebra.BigOperators.Group.Finset.Basic
import Mathlib.Tactic.NormNum
import Mathlib.Tactic.Ring

/-!
Integer telescoping core of Grothendieck's cumulative Weyl shell allocation.
The continuous counting law and its constant term are deliberately inputs.
-/

namespace MariciFormal

open Finset
open scoped BigOperators

def cumulativeShellRank (count : ℕ → ℤ) (k : ℕ) : ℤ :=
  count (k + 1) - count k

theorem cumulativeShellRank_nonnegative
    (count : ℕ → ℤ) (hcount : Monotone count) (k : ℕ) :
    0 ≤ cumulativeShellRank count k := by
  exact sub_nonneg.mpr (hcount (Nat.le_succ k))

/-- Cumulative increments preserve the global count exactly up to the two
declared endpoints. -/
theorem cumulativeShellRank_telescopes
    (count : ℕ → ℤ) (n : ℕ) :
    ∑ k ∈ range n, cumulativeShellRank count k = count n - count 0 := by
  induction n with
  | zero => simp
  | succ n ih =>
      simp only [sum_range_succ, cumulativeShellRank]
      rw [ih]
      ring

/-- The same endpoint law holds on a shifted finite window. -/
theorem cumulativeShellRank_window
    (count : ℕ → ℤ) (start length : ℕ) :
    ∑ k ∈ range length, cumulativeShellRank count (start + k) =
      count (start + length) - count start := by
  induction length with
  | zero => simp
  | succ length ih =>
      simp only [sum_range_succ, cumulativeShellRank]
      rw [ih]
      ring

/-- A locally assigned rank schedule carries no automatic endpoint authority:
the constant-zero schedule can disagree with a declared growing count. -/
theorem local_zero_ranks_do_not_reconstruct_growth :
    (∑ _k ∈ range 3, (0 : ℤ)) ≠ (3 : ℤ) - 0 := by
  norm_num

end MariciFormal
