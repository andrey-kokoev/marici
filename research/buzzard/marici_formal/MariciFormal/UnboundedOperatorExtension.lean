import Mathlib.Data.Set.Basic
import Mathlib.Tactic.FinCases

/-!
Domain-bearing completion-operator interface required by Grothendieck's theta
Friedrichs contract.  A closed densely defined generator is not represented as
a total uniformly continuous self-map.
-/

namespace MariciFormal

structure DomainOperator (Y : Type*) where
  domain : Set Y
  toFun : domain → Y

namespace DomainOperator

variable {X Y : Type*} [Zero X] [Zero Y]

def EverywhereDefined (operator : DomainOperator Y) : Prop :=
  operator.domain = Set.univ

structure CoreCompatibility
    (embed : X → Y) (sourceOperator : X → X)
    (completedOperator : DomainOperator Y) where
  core_mem : ∀ x, embed x ∈ completedOperator.domain
  commutes : ∀ x,
    completedOperator.toFun ⟨embed x, core_mem x⟩ = embed (sourceOperator x)

/-- Kernel descent for a domain-bearing completed operator.  The source core
must be explicitly contained in the completed operator domain. -/
theorem kernel_descends_on_core
    (embed : X → Y) (sourceOperator : X → X)
    (completedOperator : DomainOperator Y)
    (hembedZero : embed 0 = 0)
    (hembedInjective : Function.Injective embed)
    (compatibility : CoreCompatibility embed sourceOperator completedOperator)
    {x : X}
    (hkernel : completedOperator.toFun
      ⟨embed x, compatibility.core_mem x⟩ = 0) :
    sourceOperator x = 0 := by
  apply hembedInjective
  rw [hembedZero, ← hkernel]
  exact compatibility.commutes x

end DomainOperator

section ProperDomainHostile

def properDomainOperator : DomainOperator (Fin 2) where
  domain := {0}
  toFun := fun _ => 0

/-- A valid domain-bearing operator need not be a total operator. -/
theorem properDomainOperator_not_everywhereDefined :
    ¬ properDomainOperator.EverywhereDefined := by
  intro heverywhere
  have hone : (1 : Fin 2) ∈ properDomainOperator.domain := by
    rw [heverywhere]
    exact Set.mem_univ 1
  simp [properDomainOperator] at hone

end ProperDomainHostile

end MariciFormal
