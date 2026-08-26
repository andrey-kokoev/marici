import Mathlib.Tactic.FieldSimp
import Mathlib.Tactic.Ring

/-!
Algebraic core of Grothendieck's Li Möbius-coordinate rigidity theorem.

The endpoint pole and normalization at infinity reduce the coordinate to
`(a*s+b)/(a*s)`.  Reflection as inversion then forces `b = -a`, provided the
coordinate is nonconstant.  The excluded constant case is retained as a
hostile countermodel.
-/

namespace MariciFormal

section Rigidity

variable {K : Type*} [Field K]

def endpointNormalizedMobius (a b s : K) : K :=
  (a * s + b) / (a * s)

/-- Cross-multiplied reflection-to-inversion, which remains meaningful at
the endpoint where the rational coordinate itself has a pole. -/
def ReflectionInverts (a b : K) : Prop :=
  ∀ s,
    (a * (1 - s) + b) * (a * s + b) =
      (a * (1 - s)) * (a * s)

/-- Pole at zero and normalization at infinity leave one coefficient `b`;
reflection rigidity forces it to be `-a`. -/
theorem liMobius_coefficient_rigidity
    (a b : K) (hb : b ≠ 0) (hreflection : ReflectionInverts a b) :
    b = -a := by
  have hzero := hreflection 0
  have hfactor : (a + b) * b = 0 := by
    simpa using hzero
  rcases mul_eq_zero.mp hfactor with hab | hbzero
  · exact eq_neg_of_add_eq_zero_left hab
  · exact (hb hbzero).elim

/-- The normalized rational coordinate is therefore exactly `1 - 1/s`. -/
theorem liMobius_coordinate_rigidity
    (a b s : K) (ha : a ≠ 0) (hb : b ≠ 0)
    (hs : s ≠ 0) (hreflection : ReflectionInverts a b) :
    endpointNormalizedMobius a b s = 1 - 1 / s := by
  rw [liMobius_coefficient_rigidity a b hb hreflection]
  field_simp [endpointNormalizedMobius, ha, hs] <;> ring

theorem liMobius_reflection_law (a : K) :
    ReflectionInverts a (-a) := by
  intro s
  ring

end Rigidity

section NonconstantHostile

variable {K : Type*} [Field K]

/-- If nonconstancy is omitted, `b = 0` gives the constant coordinate `1`
and satisfies the same cross-multiplied reflection law. -/
theorem constant_coordinate_satisfies_reflection (a : K) :
    ReflectionInverts a 0 := by
  intro s
  ring

theorem constant_coordinate_is_one
    (a s : K) (ha : a ≠ 0) (hs : s ≠ 0) :
    endpointNormalizedMobius a 0 s = 1 := by
  simp [endpointNormalizedMobius, ha, hs]

end NonconstantHostile

end MariciFormal
