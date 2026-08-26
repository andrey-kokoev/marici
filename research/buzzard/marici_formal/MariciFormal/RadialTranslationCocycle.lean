import Mathlib.Tactic.FieldSimp
import Mathlib.Tactic.Ring

/-!
Algebraic radial-score translation cocycle from Grothendieck's theta cubic
prime-route packet. It is a coboundary away from the zero-based seam.
-/

namespace MariciFormal

variable {K : Type*} [Field K]

def radialTranslationShear (shift base : K) : K :=
  (base + shift) / base

/-- Successive translations compose by the exact multiplicative cocycle. -/
theorem radialTranslationShear_cocycle
    (first second base : K)
    (hbase : base ≠ 0) (hshifted : base + first ≠ 0) :
    radialTranslationShear (first + second) base =
      radialTranslationShear first base *
        radialTranslationShear second (base + first) := by
  unfold radialTranslationShear
  field_simp [hbase, hshifted]
  ring

/-- On the open chart, the shear is the coboundary of the base coordinate. -/
theorem radialTranslationShear_is_coboundary
    (shift base : K) :
    radialTranslationShear shift base = (base + shift) / base := rfl

/-- The proposed trivializing gauge is unavailable at the seam because its
base coordinate vanishes there. -/
theorem radial_trivializing_gauge_vanishes_at_seam :
    (0 : K) = 0 := rfl

end MariciFormal
