import Mathlib.Tactic.NormNum
import Mathlib.Tactic.Ring

/-!
Finite algebraic core of Grothendieck's reciprocal Gaussian seam calculation.
The analytic construction of the half-Mellin amplitudes is deliberately an
input: this file proves only what reciprocal sewing does to the two channels.
-/

namespace MariciFormal

section ReciprocalSewing

variable {R : Type*} [Field R] [CharZero R]

def symmetricChannel (forward reverse : R) : R :=
  forward + reverse

def antisymmetricChannel (forward reverse : R) : R :=
  forward - reverse

def forwardNumberChannel (spectral forward seam : R) : R :=
  ((1 / 2 : R) + spectral) * forward + seam

def reverseNumberChannel (spectral reverse seam : R) : R :=
  ((1 / 2 : R) - spectral) * reverse + seam

/-- Reciprocal sewing doubles the common seam value in the symmetric number
channel.  The parameter `spectral` is the algebraic slot occupied by `i z` in
the source packet. -/
theorem numberChannel_sum_sewing
    (spectral forward reverse seam : R) :
    forwardNumberChannel spectral forward seam +
        reverseNumberChannel spectral reverse seam =
      (1 / 2 : R) * symmetricChannel forward reverse +
        spectral * antisymmetricChannel forward reverse + 2 * seam := by
  simp [forwardNumberChannel, reverseNumberChannel, symmetricChannel,
    antisymmetricChannel]
  ring

/-- The common seam value cancels from the antisymmetric number channel. -/
theorem numberChannel_difference_sewing
    (spectral forward reverse seam : R) :
    forwardNumberChannel spectral forward seam -
        reverseNumberChannel spectral reverse seam =
      (1 / 2 : R) * antisymmetricChannel forward reverse +
        spectral * symmetricChannel forward reverse := by
  simp [forwardNumberChannel, reverseNumberChannel, symmetricChannel,
    antisymmetricChannel]
  ring

theorem at_symmetric_zero_sum_retains_seam_and_route
    (spectral forward reverse seam : R)
    (hzero : symmetricChannel forward reverse = 0) :
    forwardNumberChannel spectral forward seam +
        reverseNumberChannel spectral reverse seam =
      spectral * antisymmetricChannel forward reverse + 2 * seam := by
  rw [numberChannel_sum_sewing, hzero]
  ring

theorem at_symmetric_zero_difference_retains_route
    (spectral forward reverse seam : R)
    (hzero : symmetricChannel forward reverse = 0) :
    forwardNumberChannel spectral forward seam -
        reverseNumberChannel spectral reverse seam =
      (1 / 2 : R) * antisymmetricChannel forward reverse := by
  rw [numberChannel_difference_sewing, hzero]
  ring

end ReciprocalSewing

section Hostile

/-- A zero symmetric scalar does not imply that the antisymmetric route or
the sewn number-channel difference vanishes. -/
theorem symmetric_zero_with_nonzero_transverse_route :
    symmetricChannel (R := ℚ) 1 (-1) = 0 ∧
      antisymmetricChannel (R := ℚ) 1 (-1) = 2 ∧
      forwardNumberChannel (R := ℚ) 0 1 0 -
          reverseNumberChannel (R := ℚ) 0 (-1) 0 = 1 := by
  norm_num [symmetricChannel, antisymmetricChannel, forwardNumberChannel,
    reverseNumberChannel]

end Hostile

end MariciFormal
