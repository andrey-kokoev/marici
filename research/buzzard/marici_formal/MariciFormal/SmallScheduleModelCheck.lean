import MariciFormal.CASFencingRefinement

namespace MariciFormal.TemporalAuthority.LinearConsumption

/-! Exhaustive two-site split read/write schedules. -/

inductive SplitAction where
  | readA | writeA | readB | writeB
  deriving DecidableEq, Repr

structure SplitMachineState where
  memory : Bool
  readA : Option Bool
  readB : Option Bool
  successA : Bool
  successB : Bool
  deriving DecidableEq, Repr

def initialSplitMachine : SplitMachineState :=
  ⟨false, none, none, false, false⟩

def applySplitAction (state : SplitMachineState) : SplitAction → SplitMachineState
  | .readA => { state with readA := some state.memory }
  | .readB => { state with readB := some state.memory }
  | .writeA =>
      match state.readA with
      | some false => { state with memory := true, successA := true }
      | _ => state
  | .writeB =>
      match state.readB with
      | some false => { state with memory := true, successB := true }
      | _ => state

def runSplitActions (actions : List SplitAction) : SplitMachineState :=
  actions.foldl applySplitAction initialSplitMachine

/-- The six interleavings preserving read-before-write at each site. -/
inductive LegalSplitSchedule where
  | AABB | ABAB | ABBA | BAAB | BABA | BBAA
  deriving DecidableEq, Repr

def scheduleActions : LegalSplitSchedule → List SplitAction
  | .AABB => [.readA, .writeA, .readB, .writeB]
  | .ABAB => [.readA, .readB, .writeA, .writeB]
  | .ABBA => [.readA, .readB, .writeB, .writeA]
  | .BAAB => [.readB, .readA, .writeA, .writeB]
  | .BABA => [.readB, .readA, .writeB, .writeA]
  | .BBAA => [.readB, .writeB, .readA, .writeA]

def splitScheduleOutcome (schedule : LegalSplitSchedule) : Bool × Bool :=
  let final := runSplitActions (scheduleActions schedule)
  (final.successA, final.successB)

def SplitScheduleSafe (schedule : LegalSplitSchedule) : Bool :=
  let outcome := splitScheduleOutcome schedule
  outcome.1 != outcome.2

theorem splitScheduleSafe_iff_exactlyOne (schedule : LegalSplitSchedule) :
    SplitScheduleSafe schedule = true ↔
      ExactlyOne (splitScheduleOutcome schedule) := by
  cases schedule <;>
    simp [SplitScheduleSafe, ExactlyOne, splitScheduleOutcome, runSplitActions,
      scheduleActions, applySplitAction, initialSplitMachine]

theorem serialized_A_schedule_is_safe : SplitScheduleSafe .AABB = true := by
  decide

theorem serialized_B_schedule_is_safe : SplitScheduleSafe .BBAA = true := by
  decide

theorem all_read_read_write_write_schedules_duplicate :
    splitScheduleOutcome .ABAB = (true, true) ∧
      splitScheduleOutcome .ABBA = (true, true) ∧
      splitScheduleOutcome .BAAB = (true, true) ∧
      splitScheduleOutcome .BABA = (true, true) := by
  decide

theorem exhaustive_split_schedule_classification
    (schedule : LegalSplitSchedule) :
    SplitScheduleSafe schedule = true ↔
      schedule = .AABB ∨ schedule = .BBAA := by
  cases schedule <;> decide

def allSplitSchedules : List LegalSplitSchedule :=
  [.AABB, .ABAB, .ABBA, .BAAB, .BABA, .BBAA]

theorem allSplitSchedules_is_exhaustive :
    allSplitSchedules.Nodup ∧ ∀ schedule, schedule ∈ allSplitSchedules := by
  constructor
  · decide
  · intro schedule
    cases schedule <;> decide

def safeSplitScheduleCount : Nat :=
  (allSplitSchedules.filter SplitScheduleSafe).length

theorem exactly_two_of_six_split_schedules_are_safe :
    safeSplitScheduleCount = 2 := by
  decide

theorem four_of_six_split_schedules_violate_single_use :
    (allSplitSchedules.filter fun schedule =>
      !SplitScheduleSafe schedule).length = 4 := by
  decide

theorem schedule_model_check_recovers_lost_update_fixture :
    splitScheduleOutcome .ABAB = splitOutcome lostUpdateTrace := by
  rfl

end MariciFormal.TemporalAuthority.LinearConsumption
