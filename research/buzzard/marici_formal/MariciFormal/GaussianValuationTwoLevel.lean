import Mathlib.Algebra.Order.Field.Basic
import Mathlib.Tactic.FieldSimp
import Mathlib.Tactic.NormNum
import Mathlib.Tactic.Omega

/-!
Finite local core of Grothendieck's Gaussian-weighted valuation chain.
This file does not identify the algebraic spectral parameter with `p^(1/2-s)`.
-/

namespace MariciFormal

section QuantumPlaneWeights

variable {R : Type*} [CommMonoid R]

def quadraticValuationWeight (p : R) (k : ℕ) : R :=
  p ^ (2 * k)

/-- Scalar form of `Q S = p^2 S Q` on the valuation basis. -/
theorem quadraticValuationWeight_succ (p : R) (k : ℕ) :
    quadraticValuationWeight p (k + 1) =
      p ^ 2 * quadraticValuationWeight p k := by
  simp only [quadraticValuationWeight]
  rw [show 2 * (k + 1) = 2 + 2 * k by omega, pow_add]

end QuantumPlaneWeights

section TwoLevelPacket

variable {R : Type*} [LinearOrderedField R]

def twoLevelOccupationReadout (inner outer spectral : R) : R :=
  inner + outer * spectral

def twoLevelRoot (inner outer : R) : R :=
  -inner / outer

theorem twoLevelRoot_vanishes
    (inner outer : R) (houter : outer ≠ 0) :
    twoLevelOccupationReadout inner outer (twoLevelRoot inner outer) = 0 := by
  simp [twoLevelOccupationReadout, twoLevelRoot, houter]

theorem twoLevel_zero_iff
    (inner outer spectral : R) (houter : outer ≠ 0) :
    twoLevelOccupationReadout inner outer spectral = 0 ↔
      spectral = twoLevelRoot inner outer := by
  constructor
  · intro h
    simp only [twoLevelOccupationReadout, twoLevelRoot] at h ⊢
    apply (eq_div_iff houter).2
    linarith
  · rintro rfl
    exact twoLevelRoot_vanishes inner outer houter

/-- Equal positive occupation weights put the two-level root on the unit
modulus locus. -/
theorem equalWeight_twoLevel_root_abs
    (weight : R) (hweight : 0 < weight) :
    |twoLevelRoot weight weight| = 1 := by
  have hne : weight ≠ 0 := ne_of_gt hweight
  simp [twoLevelRoot, hne]

/-- If the inner Gaussian sample is larger than the outer sample, the unique
two-level root has modulus strictly larger than one. -/
theorem decreasingWeight_twoLevel_root_abs_gt_one
    (inner outer : R) (houter : 0 < outer) (hdecrease : outer < inner) :
    |twoLevelRoot inner outer| > 1 := by
  rw [twoLevelRoot, abs_div, abs_neg, abs_of_pos (houter.trans hdecrease),
    abs_of_pos houter]
  exact (one_lt_div houter).2 hdecrease

end TwoLevelPacket

section Hostile

/-- A positive decreasing two-level packet can vanish only at an off-unit
spectral parameter. -/
theorem positive_decreasing_packet_off_unit_hostile :
    twoLevelOccupationReadout (R := ℚ) 2 1 (-2) = 0 ∧
      |(-2 : ℚ)| > 1 := by
  norm_num [twoLevelOccupationReadout]

end Hostile

end MariciFormal
