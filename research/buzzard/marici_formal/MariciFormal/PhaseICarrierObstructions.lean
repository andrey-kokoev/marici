import Mathlib.Algebra.Group.Hom.End
import Mathlib.Tactic.NormNum
import Mathlib.Tactic.Omega

/-!
Two distinctly typed Phase-I obstructions from Grothendieck: the missing
Carrier unit for connected boundary sewing, and collapse of additive maps
from an idempotent coproduct monoid into a group.
-/

namespace MariciFormal

section ConnectedSewing

/-- Boundary arity after gluing two interfaces with two endpoints. -/
def connectedSewArity (left right : ℕ) : ℕ :=
  left + right - 2

def boundaryExcess (arity : ℕ) : ℕ :=
  arity - 2

def StableEvenArity (arity : ℕ) : Prop :=
  4 ≤ arity ∧ Even arity

theorem connectedSew_profiles :
    connectedSewArity 4 4 = 6 ∧
      connectedSewArity 6 4 = 8 ∧
      connectedSewArity 4 8 = 10 ∧
      connectedSewArity 6 6 = 10 := by
  norm_num [connectedSewArity]

theorem boundaryExcess_additive
    (left right : ℕ) (hleft : 2 ≤ left) (hright : 2 ≤ right) :
    boundaryExcess (connectedSewArity left right) =
      boundaryExcess left + boundaryExcess right := by
  unfold boundaryExcess connectedSewArity
  omega

theorem connectedSew_unit_arity_eq_two
    (arity unitArity : ℕ) (harity : 2 ≤ arity)
    (hunit : connectedSewArity arity unitArity = arity) :
    unitArity = 2 := by
  unfold connectedSewArity at hunit
  omega

theorem fourPoint_coefficientUnit_is_not_carrierUnit
    (arity : ℕ) (harity : 2 ≤ arity) :
    connectedSewArity arity 4 - arity = 2 := by
  unfold connectedSewArity
  omega

theorem no_connectedSew_unit_in_stableEvenFamily :
    ¬ ∃ unitArity : ℕ,
      StableEvenArity unitArity ∧
        ∀ arity, StableEvenArity arity →
          connectedSewArity arity unitArity = arity := by
  rintro ⟨unitArity, hstable, hunit⟩
  have hfour : StableEvenArity 4 := by
    exact ⟨by norm_num, ⟨2, by norm_num⟩⟩
  have heq : unitArity = 2 :=
    connectedSew_unit_arity_eq_two 4 unitArity (by norm_num) (hunit 4 hfour)
  omega

end ConnectedSewing

section IdempotentCoproduct

variable {M G : Type*} [AddCommMonoid M] [AddCommGroup G]

/-- Any additive map from an idempotent coproduct monoid into a group is
zero. This is the universal group-completion obstruction. -/
theorem additiveHom_eq_zero_of_idempotent
    (hidempotent : ∀ x : M, x + x = x) (map : M →+ G) :
    map = 0 := by
  ext x
  have h : map x + map x = map x := by
    simpa using congrArg map (hidempotent x)
  have h' : map x + map x = map x + 0 := by
    simpa using h
  exact add_left_cancel h'

theorem idempotent_element_maps_to_zero
    (x : M) (hx : x + x = x) (map : M →+ G) :
    map x = 0 := by
  have h : map x + map x = map x := by
    simpa using congrArg map hx
  have h' : map x + map x = map x + 0 := by
    simpa using h
  exact add_left_cancel h'

end IdempotentCoproduct

section ConditionalFreeCompletion

variable {M G : Type*} [AddCommMonoid M] [AddCommGroup G]

def natGeneratedMap (generator : M) : ℕ →+ M where
  toFun n := n • generator
  map_zero' := by simp
  map_add' left right := by simp [add_nsmul]

theorem additiveMap_from_nat_determined_by_generator
    (map : ℕ →+ M) :
    map = natGeneratedMap (map 1) := by
  ext n
  calc
    map n = map (n • (1 : ℕ)) := by simp
    _ = n • map 1 := map.map_nsmul n 1
    _ = natGeneratedMap (map 1) n := rfl

def intGeneratedMap (generator : G) : ℤ →+ G where
  toFun n := n • generator
  map_zero' := by simp
  map_add' left right := by simp [add_zsmul]

theorem additiveMap_from_int_determined_by_generator
    (map : ℤ →+ G) :
    map = intGeneratedMap (map 1) := by
  ext n
  calc
    map n = map (n • (1 : ℤ)) := by simp
    _ = n • map 1 := map.map_zsmul n 1
    _ = intGeneratedMap (map 1) n := rfl

end ConditionalFreeCompletion

end MariciFormal
