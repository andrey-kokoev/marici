import Mathlib

/-!
Finite algebraic core of a channel family with one common scalar factor.
This applies to Grothendieck's Eisenstein Fourier-mode denominator audit and
Aspect's common calibration factors.  No meromorphic divisor or resonance
claim is made here.
-/

namespace MariciFormal.CommonScalarModeFactor

variable {F ι : Type*} [Field F]

def scaledModes (scalar : F) (profile : ι → F) : ι → F :=
  fun channel => scalar * profile channel

/-- A nonzero profile channel makes the whole family detect exactly the
common scalar's zero locus.  The family repeats that scalar information. -/
theorem all_scaledModes_zero_iff
    (scalar : F) (profile : ι → F)
    (nonzeroChannel : ∃ channel, profile channel ≠ 0) :
    (∀ channel, scaledModes scalar profile channel = 0) ↔ scalar = 0 := by
  constructor
  · intro allZero
    obtain ⟨channel, nonzero⟩ := nonzeroChannel
    exact (mul_eq_zero.mp (allZero channel)).resolve_right nonzero
  · rintro rfl channel
    simp [scaledModes]

/-- If one declared profile coefficient is one, its channel is exactly the
common scalar. -/
theorem unit_profile_channel_recovers_scalar
    (scalar : F) (profile : ι → F) (channel : ι)
    (unitProfile : profile channel = 1) :
    scaledModes scalar profile channel = scalar := by
  simp [scaledModes, unitProfile]

/-- Normalizing by a nonzero anchor cancels the common scalar and therefore
forgets it. -/
theorem normalized_mode_ratio_cancels_common_scalar
    (scalar : F) (profile : ι → F) (channel anchor : ι)
    (scalarNonzero : scalar ≠ 0) (anchorNonzero : profile anchor ≠ 0) :
    scaledModes scalar profile channel /
        scaledModes scalar profile anchor =
      profile channel / profile anchor := by
  simp only [scaledModes]
  field_simp

/-- Hostile omitted premise: if every profile channel vanishes, the family
cannot detect even the nonzero scalar one. -/
theorem zero_profile_does_not_detect_common_scalar [Nonempty ι] :
    let profile : ι → F := fun _ => 0
    (∀ channel, scaledModes (1 : F) profile channel = 0) ∧
      (1 : F) ≠ 0 := by
  dsimp [scaledModes]
  simp

end MariciFormal.CommonScalarModeFactor
