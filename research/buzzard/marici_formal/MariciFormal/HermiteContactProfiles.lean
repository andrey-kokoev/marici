import Mathlib.Tactic.FieldSimp
import Mathlib.Tactic.NormNum
import Mathlib.Tactic.Omega
import Mathlib.Tactic.Ring

/-!
Quadratic and quartic finite profiles from Grothendieck's higher-contact
Hermite negative-mass audit.  General analytic asymptotics remain separate.
-/

namespace MariciFormal

def physicistsH2 (z : ℝ) : ℝ :=
  4 * z ^ 2 - 2

def physicistsH4 (z : ℝ) : ℝ :=
  16 * z ^ 4 - 48 * z ^ 2 + 12

def quadraticBackwardHeatProfile (delta x : ℝ) : ℝ :=
  x ^ 2 - 2 * delta

def quarticBackwardHeatProfile (delta x : ℝ) : ℝ :=
  x ^ 4 - 12 * delta * x ^ 2 + 12 * delta ^ 2

/-- With `delta=r²`, the quadratic profile is exactly the rescaled
physicists' Hermite polynomial. -/
theorem quadratic_profile_is_scaled_H2
    (r x : ℝ) (hr : r ≠ 0) :
    r ^ 2 * physicistsH2 (x / (2 * r)) =
      quadraticBackwardHeatProfile (r ^ 2) x := by
  field_simp [physicistsH2, quadraticBackwardHeatProfile, hr]
  ring

/-- The corresponding exact quartic backward-heat profile. -/
theorem quartic_profile_is_scaled_H4
    (r x : ℝ) (hr : r ≠ 0) :
    r ^ 4 * physicistsH4 (x / (2 * r)) =
      quarticBackwardHeatProfile (r ^ 2) x := by
  field_simp [physicistsH4, quarticBackwardHeatProfile, hr]
  ring

theorem H2_has_negative_region : physicistsH2 0 = -2 := by
  norm_num [physicistsH2]

theorem H4_has_negative_region : physicistsH4 1 = -20 := by
  norm_num [physicistsH4]

theorem H4_changes_sign :
    0 < physicistsH4 0 ∧ physicistsH4 1 < 0 := by
  norm_num [physicistsH4]

/-- Twice the onset exponent `m+1/2`; this avoids quotient conventions while
retaining exact observability of contact multiplicity. -/
def contactExponentNumerator (m : ℕ) : ℕ :=
  2 * m + 1

theorem contactExponentNumerator_injective :
    Function.Injective contactExponentNumerator := by
  intro m n h
  omega

theorem quadratic_and_quartic_exponents :
    contactExponentNumerator 1 = 3 ∧
      contactExponentNumerator 2 = 5 := by
  decide

/-- A single negative-value observation cannot distinguish the two contact
orders even though their scaling exponents differ. -/
theorem negative_sign_alone_does_not_classify_contact :
    physicistsH2 0 < 0 ∧ physicistsH4 1 < 0 ∧
      contactExponentNumerator 1 ≠ contactExponentNumerator 2 := by
  norm_num [physicistsH2, physicistsH4, contactExponentNumerator]

end MariciFormal
