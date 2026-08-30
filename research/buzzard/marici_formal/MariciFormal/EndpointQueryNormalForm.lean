import Mathlib

/-!
The commutative endpoint-query normal form and a hostile noncommuting action
showing that the normal form requires an independent commutation theorem.
-/

namespace MariciFormal

/-- Finite valuation constraints plus one additive Mellin parameter. -/
@[ext] structure EndpointQueryNormalForm where
  constraints : Finset Nat
  mellin : Rat
  deriving DecidableEq

namespace EndpointQueryNormalForm

def compose (left right : EndpointQueryNormalForm) : EndpointQueryNormalForm where
  constraints := left.constraints ∪ right.constraints
  mellin := left.mellin + right.mellin

def identity : EndpointQueryNormalForm where
  constraints := ∅
  mellin := 0

theorem compose_assoc (a b c : EndpointQueryNormalForm) :
    compose (compose a b) c = compose a (compose b c) := by
  ext <;> simp [compose, Finset.union_assoc, add_assoc]

theorem identity_compose (a : EndpointQueryNormalForm) :
    compose identity a = a := by
  ext <;> simp [compose, identity]

theorem compose_identity (a : EndpointQueryNormalForm) :
    compose a identity = a := by
  ext <;> simp [compose, identity]

/-- This normal-form composition is commutative because both constructor
families have already been assumed to commute. -/
theorem compose_comm (a b : EndpointQueryNormalForm) :
    compose a b = compose b a := by
  ext <;> simp [compose, Finset.union_comm, add_comm]

end EndpointQueryNormalForm

section RepresentationGate

variable {X : Type*}

/-- An action respects the declared normal-form composition. -/
def RespectsEndpointQueryComposition
    (act : EndpointQueryNormalForm → X → X) : Prop :=
  ∀ a b, act (EndpointQueryNormalForm.compose a b) = act a ∘ act b

/-- Every action of the commutative normal form has commuting images. -/
theorem representedQueries_commute
    (act : EndpointQueryNormalForm → X → X)
    (respects : RespectsEndpointQueryComposition act)
    (a b : EndpointQueryNormalForm) :
    act a ∘ act b = act b ∘ act a := by
  rw [← respects a b, EndpointQueryNormalForm.compose_comm, respects b a]

end RepresentationGate

section NoncommutingHostile

def toggle : Bool → Bool := not

def erase : Bool → Bool := fun _ => false

theorem toggle_erase_ne_erase_toggle :
    toggle ∘ erase ≠ erase ∘ toggle := by
  intro heq
  have h := congrFun heq false
  simp [toggle, erase] at h

def projectorQuery : EndpointQueryNormalForm where
  constraints := {0}
  mellin := 0

def mellinQuery : EndpointQueryNormalForm where
  constraints := ∅
  mellin := 1

/-- Noncommuting constructors cannot be forced through the commutative normal form. -/
theorem noncommutingActions_have_no_normalFormRepresentation :
    ¬ ∃ act : EndpointQueryNormalForm → Bool → Bool,
      RespectsEndpointQueryComposition act ∧
      act projectorQuery = toggle ∧ act mellinQuery = erase := by
  rintro ⟨act, respects, hprojector, hmellin⟩
  have hcomm := representedQueries_commute act respects projectorQuery mellinQuery
  rw [hprojector, hmellin] at hcomm
  exact toggle_erase_ne_erase_toggle hcomm

end NoncommutingHostile

end MariciFormal
