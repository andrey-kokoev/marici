import MariciFormal.Fencing

namespace MariciFormal.TemporalAuthority.LinearConsumption

/-! In-doubt recovery needs authoritative completion evidence. -/

/-- `true` means recovery retries the protected effect. -/
def RecoveryCorrect (effectAlreadyHappened retry : Bool) : Prop :=
  retry = !effectAlreadyHappened

theorem no_recovery_decision_handles_both_indistinguishable_worlds
    (retry : Bool) :
    ¬ (RecoveryCorrect false retry ∧ RecoveryCorrect true retry) := by
  cases retry <;> simp [RecoveryCorrect]

structure InDoubtObservation where
  durableFence : Nat

def ambiguousObservation : InDoubtObservation := ⟨3⟩

theorem deterministic_recovery_cannot_guarantee_exactly_once
    (recover : InDoubtObservation → Bool) :
    ¬ (RecoveryCorrect false (recover ambiguousObservation) ∧
      RecoveryCorrect true (recover ambiguousObservation)) :=
  no_recovery_decision_handles_both_indistinguishable_worlds _

structure CompletionWitness where
  effectAlreadyHappened : Bool

def recoverFromWitness (w : CompletionWitness) : Bool :=
  !w.effectAlreadyHappened

theorem authoritative_completion_witness_selects_correct_recovery
    (w : CompletionWitness) :
    RecoveryCorrect w.effectAlreadyHappened (recoverFromWitness w) := by
  simp [RecoveryCorrect, recoverFromWitness]

structure AuthorizedRecovery where
  sourceAuthorized : Bool
  completion : CompletionWitness

def MayRecover (r : AuthorizedRecovery) : Prop := r.sourceAuthorized = true

theorem completion_evidence_does_not_supply_recovery_authority :
    let r : AuthorizedRecovery := ⟨false, ⟨false⟩⟩
    RecoveryCorrect r.completion.effectAlreadyHappened
        (recoverFromWitness r.completion) ∧ ¬ MayRecover r := by
  simp [RecoveryCorrect, recoverFromWitness, MayRecover]

theorem recovery_authority_without_completion_evidence_cannot_choose_safely :
    ∀ retry : Bool,
      ¬ (RecoveryCorrect false retry ∧ RecoveryCorrect true retry) :=
  no_recovery_decision_handles_both_indistinguishable_worlds

structure ScopedCompletionWitness where
  requestId : RequestId
  effectAlreadyHappened : Bool

def WitnessAppliesTo (w : ScopedCompletionWitness) (request : IdentifiedRequest) :
    Prop :=
  w.requestId = request.id

def recoverScoped (w : ScopedCompletionWitness) (request : IdentifiedRequest) :
    Option Bool :=
  if w.requestId = request.id then some (!w.effectAlreadyHappened) else none

theorem applicable_scoped_witness_selects_correct_recovery
    (w : ScopedCompletionWitness) (request : IdentifiedRequest)
    (h : WitnessAppliesTo w request) :
    recoverScoped w request = some (!w.effectAlreadyHappened) := by
  simp [recoverScoped, WitnessAppliesTo] at h ⊢
  exact h

def request7Completed : ScopedCompletionWitness := ⟨7, true⟩

theorem scoped_witness_rejects_cross_request_replay :
    recoverScoped request7Completed request8 = none := by
  simp [recoverScoped, request7Completed, request8]

theorem unscoped_completion_replay_can_choose_wrong_recovery :
    let unscoped : CompletionWitness := ⟨true⟩
    ¬ RecoveryCorrect false (recoverFromWitness unscoped) := by
  simp [RecoveryCorrect, recoverFromWitness]

theorem truthful_completion_is_not_transferable_evidence :
    request7Completed.effectAlreadyHappened = true ∧
      ¬ WitnessAppliesTo request7Completed request8 ∧
      recoverScoped request7Completed request8 = none := by
  simp [request7Completed, WitnessAppliesTo, request8, recoverScoped]

/-! Authenticity, freshness, and epoch currency are independent. -/

structure WitnessEnvelope where
  completion : ScopedCompletionWitness
  issuer : String
  issuedAt : Nat
  expiresAt : Nat
  authorityEpoch : Nat

structure RecoveryContext where
  trustedIssuer : String
  now : Nat
  liveAuthorityEpoch : Nat

def WitnessAuthentic (w : WitnessEnvelope) (ctx : RecoveryContext) : Prop :=
  w.issuer = ctx.trustedIssuer

def WitnessFresh (w : WitnessEnvelope) (ctx : RecoveryContext) : Prop :=
  w.issuedAt ≤ ctx.now ∧ ctx.now < w.expiresAt

def WitnessEpochCurrent (w : WitnessEnvelope) (ctx : RecoveryContext) : Prop :=
  w.authorityEpoch = ctx.liveAuthorityEpoch

def WitnessUsableFor (w : WitnessEnvelope) (request : IdentifiedRequest)
    (ctx : RecoveryContext) : Prop :=
  WitnessAppliesTo w.completion request ∧ WitnessAuthentic w ctx ∧
    WitnessFresh w ctx ∧ WitnessEpochCurrent w ctx

def liveRecoveryContext : RecoveryContext := ⟨"effect-owner", 5, 3⟩

def validWitness : WitnessEnvelope :=
  ⟨⟨7, true⟩, "effect-owner", 2, 8, 3⟩

theorem valid_witness_is_usable :
    WitnessUsableFor validWitness request7 liveRecoveryContext := by
  simp [WitnessUsableFor, WitnessAppliesTo, WitnessAuthentic, WitnessFresh,
    WitnessEpochCurrent, validWitness, request7, liveRecoveryContext]

def forgedFreshWitness : WitnessEnvelope :=
  { validWitness with issuer := "untrusted-replica" }

theorem freshness_and_epoch_do_not_imply_authenticity :
    WitnessFresh forgedFreshWitness liveRecoveryContext ∧
      WitnessEpochCurrent forgedFreshWitness liveRecoveryContext ∧
      ¬ WitnessAuthentic forgedFreshWitness liveRecoveryContext := by
  simp [WitnessFresh, WitnessEpochCurrent, WitnessAuthentic,
    forgedFreshWitness, validWitness, liveRecoveryContext]

def authenticStaleWitness : WitnessEnvelope :=
  { validWitness with expiresAt := 5 }

theorem authenticity_and_epoch_do_not_imply_freshness :
    WitnessAuthentic authenticStaleWitness liveRecoveryContext ∧
      WitnessEpochCurrent authenticStaleWitness liveRecoveryContext ∧
      ¬ WitnessFresh authenticStaleWitness liveRecoveryContext := by
  simp [WitnessFresh, WitnessEpochCurrent, WitnessAuthentic,
    authenticStaleWitness, validWitness, liveRecoveryContext]

def authenticFreshRevokedWitness : WitnessEnvelope :=
  { validWitness with authorityEpoch := 2 }

theorem authenticity_and_freshness_do_not_imply_epoch_currency :
    WitnessAuthentic authenticFreshRevokedWitness liveRecoveryContext ∧
      WitnessFresh authenticFreshRevokedWitness liveRecoveryContext ∧
      ¬ WitnessEpochCurrent authenticFreshRevokedWitness liveRecoveryContext := by
  simp [WitnessFresh, WitnessEpochCurrent, WitnessAuthentic,
    authenticFreshRevokedWitness, validWitness, liveRecoveryContext]

theorem usable_witness_supplies_all_validation_interfaces
    (w : WitnessEnvelope) (request : IdentifiedRequest) (ctx : RecoveryContext)
    (h : WitnessUsableFor w request ctx) :
    WitnessAppliesTo w.completion request ∧ WitnessAuthentic w ctx ∧
      WitnessFresh w ctx ∧ WitnessEpochCurrent w ctx :=
  h

end MariciFormal.TemporalAuthority.LinearConsumption
