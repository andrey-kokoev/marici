import MariciFormal.RequestNamespace

namespace MariciFormal.TemporalAuthority.LinearConsumption

/-! Finite traces for fenced execution and request identity. -/

structure FencedTraceResult where
  finalState : FencedEffectState
  successes : Nat

def runFencedTrace : FencedEffectState → List Nat → FencedTraceResult
  | state, [] => ⟨state, 0⟩
  | state, token :: rest =>
      let step := attemptFencedEffect state token
      let tail := runFencedTrace step.1 rest
      ⟨tail.finalState, (if step.2 then 1 else 0) + tail.successes⟩

/-- Every successful trace step corresponds to exactly one counted effect. -/
theorem runFencedTrace_effect_accounting (tokens : List Nat)
    (state : FencedEffectState) :
    (runFencedTrace state tokens).finalState.effectCount =
      state.effectCount + (runFencedTrace state tokens).successes := by
  induction tokens generalizing state with
  | nil => simp [runFencedTrace]
  | cons token rest ih =>
      by_cases h : state.fence.lastAccepted < token
      · simp [runFencedTrace, attemptFencedEffect, h, ih, Nat.add_assoc]
      · simp [runFencedTrace, attemptFencedEffect, h, ih]

theorem runFencedTrace_successes_bounded_by_length (tokens : List Nat)
    (state : FencedEffectState) :
    (runFencedTrace state tokens).successes ≤ tokens.length := by
  induction tokens generalizing state with
  | nil => simp [runFencedTrace]
  | cons token rest ih =>
      by_cases h : state.fence.lastAccepted < token
      · simp only [runFencedTrace, attemptFencedEffect, h, ↓reduceIte,
          List.length_cons]
        have htail := ih ⟨⟨token⟩, state.effectCount + 1⟩
        omega
      · simp [runFencedTrace, attemptFencedEffect, h]
        exact Nat.le_trans (ih state) (Nat.le_succ _)

theorem repeated_token_finite_trace_executes_once :
    let result := runFencedTrace initialFencedEffect [4, 4, 4]
    result.successes = 1 ∧ result.finalState.effectCount = 1 := by
  decide

/-- Disconnected resource histories each satisfy local accounting but total two. -/
theorem disconnected_finite_traces_duplicate_global_effect :
    let left := runFencedTrace initialFencedEffect [4]
    let right := runFencedTrace initialFencedEffect [4]
    left.successes = 1 ∧ right.successes = 1 ∧
      left.successes + right.successes = 2 := by
  decide

def qualifiedRequestTrace : List QualifiedRequestId := [idA7, idB7]

theorem qualified_finite_trace_preserves_distinct_requests :
    qualifiedRequestTrace.Nodup := by
  simp [qualifiedRequestTrace, idA7, idB7, issuerA, issuerB]

theorem erasing_authority_makes_finite_trace_ambiguous :
    ¬ (qualifiedRequestTrace.map eraseIssuer).Nodup := by
  simp [qualifiedRequestTrace, eraseIssuer, idA7, idB7]

/-- A trace is usable only when every witness passes all four scoped checks. -/
def WitnessTraceUsable (trace : List WitnessEnvelope)
    (request : IdentifiedRequest) (ctx : RecoveryContext) : Prop :=
  ∀ w ∈ trace, WitnessUsableFor w request ctx

theorem valid_witness_trace_is_usable :
    WitnessTraceUsable [validWitness, validWitness] request7 liveRecoveryContext := by
  simp [WitnessTraceUsable, valid_witness_is_usable]

theorem one_forged_entry_invalidates_witness_trace :
    ¬ WitnessTraceUsable [validWitness, forgedFreshWitness]
      request7 liveRecoveryContext := by
  intro h
  have usable := h forgedFreshWitness (by simp)
  exact freshness_and_epoch_do_not_imply_authenticity.2.2 usable.2.1

end MariciFormal.TemporalAuthority.LinearConsumption
