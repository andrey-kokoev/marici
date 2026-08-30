import Mathlib.Tactic.FieldSimp
import Mathlib.Tactic.Ring

/-!
Finite algebraic core of Grothendieck's endpoint--zeta-pole cancellation and
identity mapping-cone model. Analytic Laurent expansions and positivity of the
reduced completed kernel are not assumed.
-/

namespace MariciFormal

section PoleCancellation

variable {K : Type*} [Field K]

/-- The two polar representatives differ by a regular rational term after
their residues cancel. -/
theorem endpoint_zeta_polar_difference
    (epsilon : K)
    (hepsilon : epsilon ≠ 0)
    (hone : 1 + epsilon ≠ 0)
    (htwo : 1 + 2 * epsilon ≠ 0) :
    1 / (epsilon * (1 + epsilon)) -
        1 / (epsilon * (1 + 2 * epsilon)) =
      1 / ((1 + epsilon) * (1 + 2 * epsilon)) := by
  field_simp [hepsilon, hone, htwo]
  ring

end PoleCancellation

section IdentityCone

variable {A : Type*} [AddCommGroup A]

/-- The identity differential has trivial homology at its source. -/
theorem identity_differential_kernel_trivial (x : A) :
    (id x = 0) ↔ x = 0 := by
  rfl

/-- The identity differential is onto at its target. -/
theorem identity_differential_surjective : Function.Surjective (id : A → A) := by
  intro x
  exact ⟨x, rfl⟩

/-- Equal endpoint and pole resolvent contributions cancel in the graded
trace model. -/
theorem equal_resolvent_pair_cancels (resolvent : A) :
    resolvent - resolvent = 0 := by
  simp

end IdentityCone

end MariciFormal
