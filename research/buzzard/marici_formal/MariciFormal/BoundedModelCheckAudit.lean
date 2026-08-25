import MariciFormal.AuditRecord
import MariciFormal.SmallScheduleModelCheck

/-!
Typed coverage evidence for bounded exhaustive model checks.

Exhaustiveness is always relative to the declared input type.  A proof that a
list covers one finite type does not become coverage of a larger type merely
because the smaller type embeds in it.
-/

namespace MariciFormal

/-- A finite checked domain, without any implicit claim that it is exhaustive. -/
structure CheckedDomain (X : Type*) where
  members : List X
  nodup : members.Nodup

def CheckedDomain.Covers {X : Type*} (d : CheckedDomain X) : Prop :=
  ∀ x, x ∈ d.members

/-- Executable evidence for a predicate on exactly the listed inputs. -/
structure FiniteModelCheck (X : Type*) where
  domain : CheckedDomain X
  predicate : X → Prop
  checked : ∀ x ∈ domain.members, predicate x

def FiniteModelCheck.toBoundedClaim {X : Type*} (check : FiniteModelCheck X) :
    BoundedClaim X where
  domain := {x | x ∈ check.domain.members}
  predicate := check.predicate
  certified := check.checked

theorem FiniteModelCheck.universal_of_coverage {X : Type*}
    (check : FiniteModelCheck X) (coverage : check.domain.Covers) :
    check.toBoundedClaim.Universal := by
  intro x
  exact check.checked x (coverage x)

namespace TemporalAuthority.LinearConsumption

def legalSplitDomain : CheckedDomain LegalSplitSchedule where
  members := allSplitSchedules
  nodup := allSplitSchedules_is_exhaustive.1

theorem legalSplitDomain_covers : legalSplitDomain.Covers :=
  allSplitSchedules_is_exhaustive.2

/-- The checked statement classifies, rather than falsely declaring safe, all schedules. -/
def CorrectSplitClassification (schedule : LegalSplitSchedule) : Prop :=
  SplitScheduleSafe schedule = true ↔
    schedule = .AABB ∨ schedule = .BBAA

def splitClassificationCheck : FiniteModelCheck LegalSplitSchedule where
  domain := legalSplitDomain
  predicate := CorrectSplitClassification
  checked := by
    intro schedule _
    exact exhaustive_split_schedule_classification schedule

theorem checked_split_classification_is_universal_on_declared_type :
    splitClassificationCheck.toBoundedClaim.Universal :=
  splitClassificationCheck.universal_of_coverage legalSplitDomain_covers

/-- A strictly larger schedule type with one behavior outside the six-case contract. -/
inductive ExtendedSchedule where
  | legal (schedule : LegalSplitSchedule)
  | retryAfterCrash
  deriving DecidableEq, Repr

def embedLegalSchedule : LegalSplitSchedule → ExtendedSchedule := .legal

def extendedSplitDomain : CheckedDomain ExtendedSchedule where
  members := allSplitSchedules.map embedLegalSchedule
  nodup := allSplitSchedules_is_exhaustive.1.map (by
    intro a b h
    cases h
    rfl)

/-- The larger-domain claim agrees on old cases and fails on the new case. -/
def ExtendedClassification : ExtendedSchedule → Prop
  | .legal schedule => CorrectSplitClassification schedule
  | .retryAfterCrash => False

def liftedSplitClassificationCheck : FiniteModelCheck ExtendedSchedule where
  domain := extendedSplitDomain
  predicate := ExtendedClassification
  checked := by
    intro schedule hs
    simp [extendedSplitDomain, allSplitSchedules, embedLegalSchedule] at hs
    rcases hs with rfl | rfl | rfl | rfl | rfl | rfl <;>
      simp [ExtendedClassification, CorrectSplitClassification,
        SplitScheduleSafe, splitScheduleOutcome, runSplitActions,
        scheduleActions, applySplitAction, initialSplitMachine]

theorem old_cases_are_covered_in_larger_type
    (schedule : LegalSplitSchedule) :
    embedLegalSchedule schedule ∈ extendedSplitDomain.members := by
  cases schedule <;> decide

/-- Hostile case: embedding every old case does not cover the enlarged type. -/
theorem extended_domain_not_covered : ¬ extendedSplitDomain.Covers := by
  intro h
  have := h ExtendedSchedule.retryAfterCrash
  simp only [extendedSplitDomain, List.mem_map] at this
  rcases this with ⟨schedule, _, impossible⟩
  cases impossible

/-- The bounded evidence cannot certify the larger-domain universal claim. -/
theorem lifted_check_not_universal :
    ¬ liftedSplitClassificationCheck.toBoundedClaim.Universal := by
  intro h
  exact h ExtendedSchedule.retryAfterCrash

/--
Source-relative audit fixture for the exhaustive six-schedule classification.
The bound `6` is data, not an authority to enlarge the schedule type.
-/
abbrev SplitScheduleAudit := SourceRelativeAuditRecord
  String String (Nat × Nat) (BoundedClaim LegalSplitSchedule)
  (FiniteModelCheck LegalSplitSchedule) String String Nat AuditActor AuditActor

def splitScheduleAudit : SplitScheduleAudit where
  source := "Strominger distributed linear-consumption finite fixture"
  model := "all read-before-write interleavings of two split read/write sites"
  result := (safeSplitScheduleCount,
    (allSplitSchedules.filter fun schedule => !SplitScheduleSafe schedule).length)
  claim := splitClassificationCheck.toBoundedClaim
  verification := splitClassificationCheck
  evidence := "six explicit schedules; two safe and four duplicating"
  tests := "coverage, classification, counts, and larger-domain hostile case"
  bound := 6
  producer := .sectorProducer
  verifier := .independentVerifier

theorem splitScheduleAudit_result :
    splitScheduleAudit.result = (2, 4) ∧
    splitScheduleAudit.bound = 6 ∧
    splitScheduleAudit.producer ≠ splitScheduleAudit.verifier := by
  decide

end TemporalAuthority.LinearConsumption
end MariciFormal
