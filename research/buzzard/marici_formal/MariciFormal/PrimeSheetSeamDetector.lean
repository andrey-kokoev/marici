import Mathlib.Tactic

/-!
Algebraic log-amplitude core of Grothendieck's native prime-sheet adjoint
matching theorem. Complex exponentiation and operator adjoints are external.
-/

namespace MariciFormal

section LogAmplitude

variable {K : Type*} [Field K] [CharZero K]

def directLogAmplitude (base displacement logPrime : K) : K :=
  (base - displacement) * logPrime

def reciprocalLogAmplitude (base displacement logPrime : K) : K :=
  (base + displacement) * logPrime

def logModulusMismatch (displacement logPrime : K) : K :=
  2 * displacement * logPrime

theorem reciprocal_sub_direct_eq_mismatch
    (base displacement logPrime : K) :
    reciprocalLogAmplitude base displacement logPrime -
        directLogAmplitude base displacement logPrime =
      logModulusMismatch displacement logPrime := by
  simp [reciprocalLogAmplitude, directLogAmplitude, logModulusMismatch]
  ring

/-- When the prime logarithm is nonzero, native direct and reciprocal
log-amplitudes match exactly at zero centered displacement. -/
theorem primeSheetMatching_iff_seam
    (base displacement logPrime : K) (hlog : logPrime ≠ 0) :
    directLogAmplitude base displacement logPrime =
        reciprocalLogAmplitude base displacement logPrime ↔
      displacement = 0 := by
  constructor
  · intro hmatch
    have hproduct : (2 * displacement) * logPrime = 0 := by
      simp only [directLogAmplitude, reciprocalLogAmplitude] at hmatch
      linear_combination -hmatch
    have htwice : 2 * displacement = 0 :=
      (mul_eq_zero.mp hproduct).resolve_right hlog
    exact (mul_eq_zero.mp htwice).resolve_left (by norm_num)
  · intro hzero
    simp [directLogAmplitude, reciprocalLogAmplitude, hzero]

theorem logModulusMismatch_eq_zero_iff
    (displacement logPrime : K) (hlog : logPrime ≠ 0) :
    logModulusMismatch displacement logPrime = 0 ↔ displacement = 0 := by
  constructor
  · intro hmismatch
    change (2 * displacement) * logPrime = 0 at hmismatch
    have htwice : 2 * displacement = 0 :=
      (mul_eq_zero.mp hmismatch).resolve_right hlog
    exact (mul_eq_zero.mp htwice).resolve_left (by norm_num)
  · intro hzero
    simp [logModulusMismatch, hzero]

end LogAmplitude

section UnitaryNoRepair

/-- Multiplication by a real unit-modulus phase cannot repair unequal
amplitude moduli. -/
theorem unitModulus_transport_cannot_repair
    (phase direct reciprocal : ℝ)
    (hphase : |phase| = 1)
    (hmismatch : |direct| ≠ |reciprocal|) :
    |phase * direct| ≠ |reciprocal| := by
  rw [abs_mul, hphase, one_mul]
  exact hmismatch

end UnitaryNoRepair

section Hostile

/-- Scalar cancellation can coexist with a nonzero native sheet mismatch. -/
theorem scalarCancellation_does_not_imply_primeSheetMatching :
    let base : ℚ := -(1 / 2)
    let displacement : ℚ := 1
    let logPrime : ℚ := 2
    (1 : ℚ) + (-1) = 0 ∧
      directLogAmplitude base displacement logPrime ≠
        reciprocalLogAmplitude base displacement logPrime := by
  norm_num [directLogAmplitude, reciprocalLogAmplitude]

end Hostile

end MariciFormal
