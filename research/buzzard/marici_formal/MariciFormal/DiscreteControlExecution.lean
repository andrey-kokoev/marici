import Mathlib

/-!
Minimal deterministic discrete-time control execution.  Composition means
temporal concatenation of finite control words; it does not mean series
interconnection, feedback composition, stability, or controller synthesis.
-/

namespace MariciFormal.DiscreteControlExecution

/-- A deterministic discrete-time control system with state `State`, control
alphabet `Control`, and no hidden admissibility or authority field. -/
structure DeterministicControlSystem (State Control : Type*) where
  step : State → Control → State

namespace DeterministicControlSystem

variable {State Control : Type*}

/-- Execute a finite control word from an initial state. -/
def run (system : DeterministicControlSystem State Control) :
    State → List Control → State
  | initial, [] => initial
  | initial, control :: rest => system.run (system.step initial control) rest

theorem run_nil (system : DeterministicControlSystem State Control)
    (initial : State) : system.run initial [] = initial := rfl

/-- Temporal composition theorem: concatenating control words is sequential
execution in the declared order. -/
theorem run_append (system : DeterministicControlSystem State Control)
    (initial : State) (first second : List Control) :
    system.run initial (first ++ second) =
      system.run (system.run initial first) second := by
  induction first generalizing initial with
  | nil => rfl
  | cons control rest ih =>
      simp only [List.cons_append, run]
      exact ih (system.step initial control)

def Reachable (system : DeterministicControlSystem State Control)
    (initial target : State) : Prop :=
  ∃ controls, system.run initial controls = target

/-- A precise strong feedback objective: one state-feedback control must send
every state to the declared target in one step. -/
def OneStepFeedbackReachable
    (system : DeterministicControlSystem State Control) (target : State) : Prop :=
  ∃ feedback : State → Control,
    ∀ state, system.step state (feedback state) = target

/-- Authorization is additional typed data on a successful control word. -/
structure AuthorizedPlan
    (system : DeterministicControlSystem State Control)
    (authorized : List Control → Prop) (initial target : State) where
  controls : List Control
  reaches : system.run initial controls = target
  authority : authorized controls

end DeterministicControlSystem

/-- Exact rational integrator `xₙ₊₁ = xₙ + uₙ`. -/
def rationalIntegrator : DeterministicControlSystem ℚ ℚ where
  step state control := state + control

theorem rationalIntegrator_run (initial : ℚ) (controls : List ℚ) :
    rationalIntegrator.run initial controls = initial + controls.sum := by
  induction controls generalizing initial with
  | nil => simp [DeterministicControlSystem.run]
  | cons control rest ih =>
      simp only [DeterministicControlSystem.run, List.sum_cons]
      rw [ih]
      change (initial + control) + rest.sum = initial + (control + rest.sum)
      ring

theorem rationalIntegrator_reachable (initial target : ℚ) :
    rationalIntegrator.Reachable initial target := by
  refine ⟨[target - initial], ?_⟩
  simp [rationalIntegrator_run]

/-- Frozen Boolean system: temporal composition still holds, but `false`
cannot reach `true`. -/
def frozenBooleanSystem : DeterministicControlSystem Bool Unit where
  step state _ := state

theorem frozenBooleanSystem_run (initial : Bool) (controls : List Unit) :
    frozenBooleanSystem.run initial controls = initial := by
  induction controls generalizing initial with
  | nil => rfl
  | cons control rest ih =>
      simp only [DeterministicControlSystem.run, frozenBooleanSystem]
      exact ih initial

theorem execution_composition_does_not_imply_controllability :
    (∀ initial first second,
      frozenBooleanSystem.run initial (first ++ second) =
        frozenBooleanSystem.run
          (frozenBooleanSystem.run initial first) second) ∧
      ¬ frozenBooleanSystem.Reachable false true := by
  constructor
  · exact fun initial first second =>
      DeterministicControlSystem.run_append
        frozenBooleanSystem initial first second
  · rintro ⟨controls, reaches⟩
    rw [frozenBooleanSystem_run] at reaches
    exact Bool.noConfusion reaches

/-- Autonomous drift has lawful temporal composition but does not preserve
the proposed equilibrium zero. -/
def driftingSystem : DeterministicControlSystem ℤ Unit where
  step state _ := state + 1

theorem execution_composition_does_not_imply_equilibrium :
    (∀ initial first second,
      driftingSystem.run initial (first ++ second) =
        driftingSystem.run (driftingSystem.run initial first) second) ∧
      driftingSystem.step 0 () ≠ 0 := by
  constructor
  · exact fun initial first second =>
      DeterministicControlSystem.run_append driftingSystem initial first second
  · norm_num [driftingSystem]

theorem execution_composition_does_not_imply_feedback_objective :
    ¬ frozenBooleanSystem.OneStepFeedbackReachable true := by
  rintro ⟨feedback, reaches⟩
  have := reaches false
  simp [frozenBooleanSystem] at this

/-- Capability is not synthesis authority: the rational integrator can reach
one from zero, but an authority predicate withholding every word yields no
authorized plan. -/
theorem reachability_does_not_manufacture_synthesis_authority :
    rationalIntegrator.Reachable 0 1 ∧
      ¬ Nonempty (DeterministicControlSystem.AuthorizedPlan
        rationalIntegrator (fun _ => False) 0 1) := by
  constructor
  · exact rationalIntegrator_reachable 0 1
  · rintro ⟨plan⟩
    exact plan.authority

end MariciFormal.DiscreteControlExecution
