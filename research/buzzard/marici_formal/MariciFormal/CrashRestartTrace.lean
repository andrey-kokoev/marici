import MariciFormal.ConcurrentRefinement

namespace MariciFormal.TemporalAuthority.LinearConsumption

/-! Finite crash/restart histories for a fenced protected effect. -/

inductive CrashTraceEvent where
  | atomicAttempt (token : Nat)
  | persistFenceOnly (token : Nat)
  | persistEffectOnly (token : Nat)
  | restart
  deriving DecidableEq, Repr

def applyCrashTraceEvent (state : FencedEffectState) :
    CrashTraceEvent → FencedEffectState
  | .atomicAttempt token => (attemptFencedEffect state token).1
  | .persistFenceOnly token =>
      if state.fence.lastAccepted < token then
        ⟨⟨token⟩, state.effectCount⟩
      else state
  | .persistEffectOnly token =>
      if state.fence.lastAccepted < token then
        ⟨state.fence, state.effectCount + 1⟩
      else state
  | .restart => state

def runCrashTrace (initial : FencedEffectState) (events : List CrashTraceEvent) :
    FencedEffectState :=
  events.foldl applyCrashTraceEvent initial

theorem restart_preserves_all_durable_state (state : FencedEffectState) :
    applyCrashTraceEvent state .restart = state := by
  rfl

theorem delayed_restart_cannot_undo_completed_effect
    (state : FencedEffectState) :
    (applyCrashTraceEvent state .restart).effectCount = state.effectCount ∧
      (applyCrashTraceEvent state .restart).fence = state.fence := by
  exact ⟨rfl, rfl⟩

def atomicRestartRetry : List CrashTraceEvent :=
  [.atomicAttempt 4, .restart, .atomicAttempt 4]

theorem atomic_persistence_survives_restart_and_rejects_retry :
    let final := runCrashTrace initialFencedEffect atomicRestartRetry
    final.fence.lastAccepted = 4 ∧ final.effectCount = 1 := by
  decide

def fenceOnlyRestartRetry : List CrashTraceEvent :=
  [.persistFenceOnly 4, .restart, .atomicAttempt 4]

theorem fence_only_persistence_loses_effect_across_restart :
    let final := runCrashTrace initialFencedEffect fenceOnlyRestartRetry
    final.fence.lastAccepted = 4 ∧ final.effectCount = 0 := by
  decide

def effectOnlyRestartRetry : List CrashTraceEvent :=
  [.persistEffectOnly 4, .restart, .atomicAttempt 4]

theorem effect_only_persistence_duplicates_effect_after_restart :
    let final := runCrashTrace initialFencedEffect effectOnlyRestartRetry
    final.fence.lastAccepted = 4 ∧ final.effectCount = 2 := by
  decide

theorem identical_retry_policy_has_three_distinct_crash_outcomes :
    (runCrashTrace initialFencedEffect atomicRestartRetry).effectCount = 1 ∧
      (runCrashTrace initialFencedEffect fenceOnlyRestartRetry).effectCount = 0 ∧
      (runCrashTrace initialFencedEffect effectOnlyRestartRetry).effectCount = 2 := by
  decide

/-- Restart transport preserves an unsafe split; it is not recovery authority. -/
theorem restart_transport_does_not_repair_split_state :
    runCrashTrace fenceOnlyCrash [.restart] = fenceOnlyCrash ∧
      runCrashTrace effectOnlyCrash [.restart] = effectOnlyCrash := by
  exact ⟨rfl, rfl⟩

end MariciFormal.TemporalAuthority.LinearConsumption
