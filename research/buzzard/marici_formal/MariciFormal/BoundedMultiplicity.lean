import MariciFormal.CrashRestartTrace

namespace MariciFormal.TemporalAuthority.LinearConsumption

/-! Finite traces for explicitly budgeted capability multiplicity. -/

structure BudgetState where
  remaining : Nat
  successes : Nat

def attemptBudget (state : BudgetState) : BudgetState × Bool :=
  match state.remaining with
  | 0 => (state, false)
  | n + 1 => (⟨n, state.successes + 1⟩, true)

def runBudgetTrace : BudgetState → Nat → BudgetState
  | state, 0 => state
  | state, attempts + 1 => runBudgetTrace (attemptBudget state).1 attempts

/-- Attempts redistribute the fixed budget between remaining and successful uses. -/
theorem runBudgetTrace_conservation (state : BudgetState) (attempts : Nat) :
    (runBudgetTrace state attempts).remaining +
        (runBudgetTrace state attempts).successes =
      state.remaining + state.successes := by
  induction attempts generalizing state with
  | zero => rfl
  | succ attempts ih =>
      cases h : state.remaining with
      | zero => simpa [runBudgetTrace, attemptBudget, h] using ih state
      | succ n =>
          simpa [runBudgetTrace, attemptBudget, h, Nat.add_assoc,
            Nat.add_left_comm, Nat.add_comm] using
            ih ⟨n, state.successes + 1⟩

theorem fresh_budget_successes_never_exceed_declared_bound
    (bound attempts : Nat) :
    (runBudgetTrace ⟨bound, 0⟩ attempts).successes ≤ bound := by
  have h := runBudgetTrace_conservation (BudgetState.mk bound 0) attempts
  have h' : (runBudgetTrace ⟨bound, 0⟩ attempts).remaining +
      (runBudgetTrace ⟨bound, 0⟩ attempts).successes = bound := by
    simpa using h
  omega

structure BoundedMultiplicityAuthority where
  bound : Nat
  sourceAuthority : SourceAuthority

def initialBudget (authority : BoundedMultiplicityAuthority) : BudgetState :=
  ⟨authority.bound, 0⟩

theorem bounded_authority_instantiates_its_declared_budget
    (authority : BoundedMultiplicityAuthority) :
    (initialBudget authority).remaining = authority.bound := by
  rfl

def singleUseBudget : BoundedMultiplicityAuthority := ⟨1, requestAuthority⟩
def multiplicityTwoBudget : BoundedMultiplicityAuthority := ⟨2, requestAuthority⟩

theorem single_use_trace_allows_only_one_success :
    let final := runBudgetTrace (initialBudget singleUseBudget) 3
    final.remaining = 0 ∧ final.successes = 1 := by
  decide

theorem multiplicity_two_trace_allows_two_successes :
    let final := runBudgetTrace (initialBudget multiplicityTwoBudget) 3
    final.remaining = 0 ∧ final.successes = 2 := by
  decide

theorem multiplicity_two_is_semantically_not_single_use :
    (runBudgetTrace (initialBudget multiplicityTwoBudget) 2).successes = 2 ∧
      (runBudgetTrace (initialBudget singleUseBudget) 2).successes = 1 := by
  decide

/-- A Boolean availability projection forgets how many uses remain. -/
def budgetAvailable (state : BudgetState) : Bool := state.remaining > 0

theorem availability_erases_resource_multiplicity :
    budgetAvailable (initialBudget singleUseBudget) = true ∧
      budgetAvailable (initialBudget multiplicityTwoBudget) = true ∧
      (initialBudget singleUseBudget).remaining ≠
        (initialBudget multiplicityTwoBudget).remaining := by
  decide

theorem multiplicity_two_authority_supplies_its_distinct_repair :
    RepairAuthorized
      ⟨.boundedMultiplicityTwo, some multiplicityTwoBudget.sourceAuthority⟩ := by
  exact ⟨multiplicityTwoBudget.sourceAuthority, rfl⟩

end MariciFormal.TemporalAuthority.LinearConsumption
