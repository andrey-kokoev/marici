import Mathlib

/-!
Reflection invariance and positivity are independent conditions, even in one
real dimension.  A positive metric must therefore remain an explicit input.
-/

namespace MariciFormal

/-- Invariance of a scalar quadratic presentation under the reflection `x ↦ -x`. -/
def ReflectionInvariant (q : Real → Real) : Prop :=
  ∀ x, q (-x) = q x

/-- Elementary positive definiteness for a scalar quadratic presentation. -/
def PositiveDefiniteScalar (q : Real → Real) : Prop :=
  q 0 = 0 ∧ ∀ x, x ≠ 0 → 0 < q x

/-- Elementary negative definiteness, used only for the hostile fixture. -/
def NegativeDefiniteScalar (q : Real → Real) : Prop :=
  q 0 = 0 ∧ ∀ x, x ≠ 0 → q x < 0

def positiveSquare (x : Real) : Real := x ^ 2

def negativeSquare (x : Real) : Real := -(x ^ 2)

theorem positiveSquare_reflection_invariant :
    ReflectionInvariant positiveSquare := by
  intro x
  simp [positiveSquare]

theorem negativeSquare_reflection_invariant :
    ReflectionInvariant negativeSquare := by
  intro x
  simp [negativeSquare]

theorem positiveSquare_positive_definite :
    PositiveDefiniteScalar positiveSquare := by
  constructor
  · norm_num [positiveSquare]
  · intro x hx
    exact sq_pos_of_ne_zero hx

theorem negativeSquare_negative_definite :
    NegativeDefiniteScalar negativeSquare := by
  constructor
  · norm_num [negativeSquare]
  · intro x hx
    have hsquare : 0 < x ^ 2 := sq_pos_of_ne_zero hx
    simpa [negativeSquare] using neg_lt_zero.mpr hsquare

/-- The negative reflection-invariant form is a finite countermodel to inferred positivity. -/
theorem reflectionInvariant_does_not_imply_positiveDefinite :
    ∃ q : Real → Real,
      ReflectionInvariant q ∧ ¬ PositiveDefiniteScalar q := by
  refine ⟨negativeSquare, negativeSquare_reflection_invariant, ?_⟩
  intro hpositive
  have hpos := hpositive.2 1 (by norm_num)
  norm_num [negativeSquare] at hpos

/-- The two reflection-compatible presentations genuinely differ. -/
theorem positiveSquare_ne_negativeSquare :
    positiveSquare ≠ negativeSquare := by
  intro heq
  have h := congrFun heq 1
  norm_num [positiveSquare, negativeSquare] at h

/-- A source-authorized metric packet carries positivity as data, not as a symmetry consequence. -/
structure AuthorizedPositiveMetric where
  form : Real → Real
  reflectionInvariant : ReflectionInvariant form
  positiveDefinite : PositiveDefiniteScalar form

def canonicalPositiveMetric : AuthorizedPositiveMetric where
  form := positiveSquare
  reflectionInvariant := positiveSquare_reflection_invariant
  positiveDefinite := positiveSquare_positive_definite

theorem authorizedPositiveMetric_is_positive (packet : AuthorizedPositiveMetric) :
    PositiveDefiniteScalar packet.form :=
  packet.positiveDefinite

end MariciFormal
