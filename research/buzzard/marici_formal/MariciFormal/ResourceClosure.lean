import Mathlib

namespace MariciFormal.ResourceClosure

variable {α : Type*}

/-- Descendant closure of resource roots under a directed derivation relation. -/
def descendantClosure (edge : α → α → Prop) (roots : Set α) : Set α :=
  {y | ∃ x ∈ roots, Relation.ReflTransGen edge x y}

/-- A removal set is counterfactually sound only when it removes descendants. -/
def RemovalClosed (edge : α → α → Prop) (removed : Set α) : Prop :=
  ∀ ⦃x y⦄, x ∈ removed → Relation.ReflTransGen edge x y → y ∈ removed

theorem roots_subset_descendantClosure (edge : α → α → Prop) (roots : Set α) :
    roots ⊆ descendantClosure edge roots := by
  intro x hx
  exact ⟨x, hx, .refl⟩

theorem descendantClosure_removalClosed (edge : α → α → Prop) (roots : Set α) :
    RemovalClosed edge (descendantClosure edge roots) := by
  rintro _ y ⟨x, hx, hxy⟩ hyz
  exact ⟨x, hx, hxy.trans hyz⟩

inductive HostileResource where
  | sourceLabel | derivedState | compiledCapability
  deriving DecidableEq, Repr

inductive HostileDerives : HostileResource → HostileResource → Prop where
  | state : HostileDerives .sourceLabel .derivedState
  | capability : HostileDerives .derivedState .compiledCapability

def labelOnlyRemoval : Set HostileResource := {.sourceLabel}

/-- Deleting only the source label leaves its derived state behind. -/
theorem label_only_removal_is_not_closed :
    ¬ RemovalClosed HostileDerives labelOnlyRemoval := by
  intro h
  have hs : HostileResource.sourceLabel ∈ labelOnlyRemoval := by simp [labelOnlyRemoval]
  have hd := h hs (Relation.ReflTransGen.single HostileDerives.state)
  simp [labelOnlyRemoval] at hd

theorem closed_removal_contains_compiledCapability :
    HostileResource.compiledCapability ∈
      descendantClosure HostileDerives labelOnlyRemoval := by
  refine ⟨.sourceLabel, by simp [labelOnlyRemoval], ?_⟩
  exact (Relation.ReflTransGen.single HostileDerives.state).trans
    (Relation.ReflTransGen.single HostileDerives.capability)

/-! Sector instances remain distinct: sharing closure does not identify resources. -/

inductive KitaevResource where
  | factory | distilledState | compiledGate
  deriving DecidableEq, Repr

inductive KitaevDerives : KitaevResource → KitaevResource → Prop where
  | distill : KitaevDerives .factory .distilledState
  | compile : KitaevDerives .distilledState .compiledGate

theorem kitaev_counterfactual_removes_compiledGate :
    KitaevResource.compiledGate ∈
      descendantClosure KitaevDerives ({.factory} : Set KitaevResource) := by
  refine ⟨.factory, by simp, ?_⟩
  exact (Relation.ReflTransGen.single KitaevDerives.distill).trans
    (Relation.ReflTransGen.single KitaevDerives.compile)

inductive FlavorResource where
  | uvSource | fittedCoefficient | downstreamReadout
  deriving DecidableEq, Repr

inductive FlavorDerives : FlavorResource → FlavorResource → Prop where
  | fit : FlavorDerives .uvSource .fittedCoefficient
  | readout : FlavorDerives .fittedCoefficient .downstreamReadout

theorem flavor_counterfactual_removes_downstreamReadout :
    FlavorResource.downstreamReadout ∈
      descendantClosure FlavorDerives ({.uvSource} : Set FlavorResource) := by
  refine ⟨.uvSource, by simp, ?_⟩
  exact (Relation.ReflTransGen.single FlavorDerives.fit).trans
    (Relation.ReflTransGen.single FlavorDerives.readout)

end MariciFormal.ResourceClosure
