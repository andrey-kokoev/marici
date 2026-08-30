import Mathlib.Tactic

/-!
Finite type-theoretic core of Grothendieck's selector-descent gate. Algebraic
power compatibility is intentionally absent: it is an independent premise,
not a constructor for selector descent.
-/

namespace MariciFormal

def DescendsAlong {Source Target Value : Type*}
    (quotient : Source → Target) (selector : Source → Value) : Prop :=
  ∃ descended : Target → Value, selector = descended ∘ quotient

/-- A selector that separates two points in one quotient fiber cannot
descend. -/
theorem selector_not_descend_of_same_fiber_distinguished
    {Source Target Value : Type*}
    (quotient : Source → Target) (selector : Source → Value)
    {left right : Source}
    (hsame : quotient left = quotient right)
    (hdifferent : selector left ≠ selector right) :
    ¬ DescendsAlong quotient selector := by
  rintro ⟨descended, hdescended⟩
  have hleft := congrFun hdescended left
  have hright := congrFun hdescended right
  apply hdifferent
  rw [hleft, hright, Function.comp_apply, Function.comp_apply, hsame]

def collapseBool (_ : Bool) : PUnit := PUnit.unit

def identitySelector : Bool → Bool
  | false => true
  | true => false

/-- The selected identity point and the other kernel point coalesce under
the nontrivial one-bit quotient, so the frozen selector does not descend. -/
theorem one_bit_identity_selector_not_descend :
    ¬ DescendsAlong collapseBool identitySelector := by
  apply selector_not_descend_of_same_fiber_distinguished
    collapseBool identitySelector (left := false) (right := true)
  · rfl
  · decide

/-- Descent and any algebraic compatibility predicate are logically
independent conjuncts of a joint physical gate. -/
theorem joint_gate_fails_when_selector_does_not_descend
    (algebraicallyCompatible : Prop)
    (quotient : Bool → PUnit) (selector : Bool → Bool)
    (hdescends : ¬ DescendsAlong quotient selector) :
    ¬ (algebraicallyCompatible ∧ DescendsAlong quotient selector) := by
  exact fun hjoint ↦ hdescends hjoint.2

end MariciFormal
