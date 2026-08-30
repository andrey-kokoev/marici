import MariciFormal.BoundedModelCheckAudit
import MariciFormal.CASFencingRefinement

/-!
Coverage and semantic fidelity are separate obligations for finite checking.

This is a minimal audit interface instantiated by two already proved execution
fixtures.  It is not asserted to be a universal semantics ontology.
-/

namespace MariciFormal

/-- A finite check performed on model semantics, with source semantics retained. -/
structure SemanticModelCheck (X Y : Type*) where
  domain : CheckedDomain X
  sourceSemantics : X → Y
  modelSemantics : X → Y
  predicate : X → Y → Prop
  modelChecked : ∀ x ∈ domain.members, predicate x (modelSemantics x)

def SemanticModelCheck.Faithful {X Y : Type*} (check : SemanticModelCheck X Y) : Prop :=
  ∀ x, check.modelSemantics x = check.sourceSemantics x

def SemanticModelCheck.SourceUniversal {X Y : Type*}
    (check : SemanticModelCheck X Y) : Prop :=
  ∀ x, check.predicate x (check.sourceSemantics x)

/-- Coverage plus pointwise semantic fidelity transfers the checked property. -/
theorem SemanticModelCheck.source_universal_of_coverage_and_fidelity
    {X Y : Type*} (check : SemanticModelCheck X Y)
    (coverage : check.domain.Covers) (fidelity : check.Faithful) :
    check.SourceUniversal := by
  intro x
  rw [← fidelity x]
  exact check.modelChecked x (coverage x)

namespace SemanticFidelityHostile

def boolDomain : CheckedDomain Bool where
  members := [false, true]
  nodup := by decide

theorem boolDomain_covers : boolDomain.Covers := by
  intro x
  cases x <;> decide

/-- Exhaustive checking of a constant-false model disagrees with the source identity. -/
def exhaustiveWrongModel : SemanticModelCheck Bool Bool where
  domain := boolDomain
  sourceSemantics := id
  modelSemantics := fun _ => false
  predicate := fun _ y => y = false
  modelChecked := by simp [boolDomain]

theorem coverage_without_fidelity :
    exhaustiveWrongModel.domain.Covers ∧
      ¬ exhaustiveWrongModel.Faithful ∧
      ¬ exhaustiveWrongModel.SourceUniversal := by
  refine ⟨boolDomain_covers, ?_, ?_⟩
  · intro h
    have := h true
    contradiction
  · intro h
    have := h true
    contradiction

def falseOnlyDomain : CheckedDomain Bool where
  members := [false]
  nodup := by decide

/-- An exactly faithful model can still omit an input required by the source claim. -/
def faithfulPartialModel : SemanticModelCheck Bool Bool where
  domain := falseOnlyDomain
  sourceSemantics := id
  modelSemantics := id
  predicate := fun _ y => y = false
  modelChecked := by simp [falseOnlyDomain]

theorem fidelity_without_coverage :
    faithfulPartialModel.Faithful ∧
      ¬ faithfulPartialModel.domain.Covers ∧
      ¬ faithfulPartialModel.SourceUniversal := by
  refine ⟨fun _ => rfl, ?_, ?_⟩
  · intro h
    have := h true
    contradiction
  · intro h
    have := h true
    contradiction

end SemanticFidelityHostile

namespace TemporalAuthority.LinearConsumption

/-- Independent reference table for the six frozen split schedules. -/
def referenceSplitSemantics : LegalSplitSchedule → Bool × Bool
  | .AABB => (true, false)
  | .ABAB | .ABBA | .BAAB | .BABA => (true, true)
  | .BBAA => (false, true)

def splitSemanticCheck : SemanticModelCheck LegalSplitSchedule (Bool × Bool) where
  domain := legalSplitDomain
  sourceSemantics := referenceSplitSemantics
  modelSemantics := splitScheduleOutcome
  predicate := fun schedule result =>
    (result.1 != result.2) = true ↔
      schedule = .AABB ∨ schedule = .BBAA
  modelChecked := by
    intro schedule _
    simpa [SplitScheduleSafe, splitScheduleOutcome] using
      exhaustive_split_schedule_classification schedule

theorem split_semantics_faithful : splitSemanticCheck.Faithful := by
  intro schedule
  cases schedule <;> decide

theorem split_source_classification_certified :
    splitSemanticCheck.SourceUniversal :=
  splitSemanticCheck.source_universal_of_coverage_and_fidelity
    legalSplitDomain_covers split_semantics_faithful

def twoOrderDomain : CheckedDomain TwoSiteOrder where
  members := [.AthenB, .BthenA]
  nodup := by decide

theorem twoOrderDomain_covers : twoOrderDomain.Covers := by
  intro order
  cases order <;> decide

/-- CAS implementation compared with the independently declared fenced specification. -/
def casFencedSemanticCheck : SemanticModelCheck TwoSiteOrder (Bool × Bool) where
  domain := twoOrderDomain
  sourceSemantics := executeConcurrentFenceOrder overlappingSameToken
  modelSemantics := runTwoCAS
  predicate := fun _ result => ExactlyOne result
  modelChecked := by
    intro order _
    exact two_compareAndSet_exactly_one order

theorem cas_fenced_semantics_faithful : casFencedSemanticCheck.Faithful := by
  intro order
  exact two_compareAndSet_operations_refine_fenced_order order

theorem cas_fenced_source_property_certified :
    casFencedSemanticCheck.SourceUniversal :=
  casFencedSemanticCheck.source_universal_of_coverage_and_fidelity
    twoOrderDomain_covers cas_fenced_semantics_faithful

/-- Even faithful finite semantics does not supply persistence or source authority. -/
theorem semantic_fidelity_does_not_supply_persistence_or_authority :
    casFencedSemanticCheck.Faithful ∧
      fenceOnlyCrash.effectCount = 0 ∧
      ¬ RepairAuthorized ⟨.sharedLinearization, none⟩ := by
  exact ⟨cas_fenced_semantics_faithful, rfl,
    every_repair_requires_additional_source_authority .sharedLinearization⟩

end TemporalAuthority.LinearConsumption
end MariciFormal
