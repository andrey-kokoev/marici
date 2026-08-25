import Mathlib
import MariciFormal.AuthorityAudit

namespace MariciFormal.TemporalAuthority

abbrev AuthorityKind := MariciFormal.AuthorityAudit.AuthorityKind
abbrev Variance := MariciFormal.AuthorityAudit.Variance

@[ext] structure Grant (Obj D : Type*) where
  source : Obj
  target : Obj
  kind : AuthorityKind
  domain : D
  variance : Variance
  validFrom : Nat
  validUntil : Nat
  interval_nonempty : validFrom < validUntil

def LiveAt {Obj D : Type*} (g : Grant Obj D) (t : Nat) : Prop :=
  g.validFrom ≤ t ∧ t < g.validUntil

/-- Composition is partial: typing, kind, domain, variance, and live intervals must match. -/
structure CanCompose {Obj D : Type*} (g h : Grant Obj D) where
  endpoint : g.target = h.source
  kind : g.kind = h.kind
  domain : g.domain = h.domain
  variance : g.variance = h.variance
  liveOverlap : max g.validFrom h.validFrom < min g.validUntil h.validUntil
  coherenceDefect : Nat
  coherent : coherenceDefect = 0

def compose {Obj D : Type*} (g h : Grant Obj D) (w : CanCompose g h) :
    Grant Obj D where
  source := g.source
  target := h.target
  kind := g.kind
  domain := g.domain
  variance := g.variance
  validFrom := max g.validFrom h.validFrom
  validUntil := min g.validUntil h.validUntil
  interval_nonempty := w.liveOverlap

theorem compose_kind_preserved {Obj D : Type*} (g h : Grant Obj D)
    (w : CanCompose g h) :
    (compose g h w).kind = g.kind ∧ (compose g h w).kind = h.kind := by
  exact ⟨rfl, w.kind⟩

def identity {Obj D : Type*} (x : Obj) (kind : AuthorityKind)
    (domain : D) (variance : Variance) (start stop : Nat) (h : start < stop) :
    Grant Obj D where
  source := x
  target := x
  kind := kind
  domain := domain
  variance := variance
  validFrom := start
  validUntil := stop
  interval_nonempty := h

theorem compose_left_identity {Obj D : Type*} (g : Grant Obj D)
    (w : CanCompose
      (identity g.source g.kind g.domain g.variance g.validFrom g.validUntil
        g.interval_nonempty) g) :
    compose
      (identity g.source g.kind g.domain g.variance g.validFrom g.validUntil
        g.interval_nonempty) g w = g := by
  ext <;> simp [compose, identity]

theorem compose_right_identity {Obj D : Type*} (g : Grant Obj D)
    (w : CanCompose g
      (identity g.target g.kind g.domain g.variance g.validFrom g.validUntil
        g.interval_nonempty)) :
    compose g
      (identity g.target g.kind g.domain g.variance g.validFrom g.validUntil
        g.interval_nonempty) w = g := by
  ext <;> simp [compose, identity]

/-- Associativity of the defined composites; existence remains witness-dependent. -/
theorem compose_assoc {Obj D : Type*} (f g h : Grant Obj D)
    (wfg : CanCompose f g) (wgh : CanCompose g h)
    (wl : CanCompose (compose f g wfg) h)
    (wr : CanCompose f (compose g h wgh)) :
    compose (compose f g wfg) h wl = compose f (compose g h wgh) wr := by
  ext <;> simp [compose, max_assoc, min_assoc]

structure CachedEvidence (Packet : Type*) where
  packet : Packet
  occurredAt : Nat

def PersistedAt {Packet : Type*} (e : CachedEvidence Packet) (t : Nat) : Prop :=
  e.occurredAt ≤ t

theorem evidence_persists {Packet : Type*} (e : CachedEvidence Packet) {t u : Nat}
    (ht : PersistedAt e t) (htu : t ≤ u) : PersistedAt e u :=
  le_trans ht htu

/-- Revocation preserves the old grant as history but ends its live interval. -/
def revoke {Obj D : Type*} (g : Grant Obj D) (revokedTime : Nat)
    (h : g.validFrom < revokedTime) : Grant Obj D where
  source := g.source
  target := g.target
  kind := g.kind
  domain := g.domain
  variance := g.variance
  validFrom := g.validFrom
  validUntil := revokedTime
  interval_nonempty := h

theorem revoked_not_live_at {Obj D : Type*} (g : Grant Obj D) (revokedTime : Nat)
    (h : g.validFrom < revokedTime) :
    ¬ LiveAt (revoke g revokedTime h) revokedTime := by
  simp [LiveAt, revoke]

structure Replay {Obj D Packet : Type*}
    (e : CachedEvidence Packet) (g : Grant Obj D) (t : Nat) where
  samePacket : Packet
  packet_fixed : samePacket = e.packet
  liveRoot : LiveAt g t

theorem replay_requires_live_authority {Obj D Packet : Type*}
    {e : CachedEvidence Packet} {g : Grant Obj D} {t : Nat}
    (r : Replay e g t) : LiveAt g t :=
  r.liveRoot

inductive FixtureObject where
  | frozenPacket | reviewDisposition | appealDisposition
  deriving DecidableEq, Repr

inductive FixtureDomain where
  | rivalAdmission
  deriving DecidableEq, Repr

def cachedReview : CachedEvidence String := ⟨"frozen-rival-packet", 1⟩

def reviewerPanelGrant : Grant FixtureObject FixtureDomain where
  source := .frozenPacket
  target := .reviewDisposition
  kind := .readout
  domain := .rivalAdmission
  variance := .covariant
  validFrom := 0
  validUntil := 2
  interval_nonempty := by decide

theorem cached_evidence_survives_revocation_but_authority_does_not :
    PersistedAt cachedReview 2 ∧ ¬ LiveAt reviewerPanelGrant 2 := by
  simp [PersistedAt, LiveAt, cachedReview, reviewerPanelGrant]

/-- Cached evidence cannot, in general, imply current authority. -/
theorem cached_evidence_cannot_imply_live_authority :
    ¬ (∀ (e : CachedEvidence String) (g : Grant FixtureObject FixtureDomain) (t : Nat),
      PersistedAt e t → LiveAt g t) := by
  intro h
  exact cached_evidence_survives_revocation_but_authority_does_not.2
    (h cachedReview reviewerPanelGrant 2
      cached_evidence_survives_revocation_but_authority_does_not.1)

/-- A revocation event must follow the evidenced authorized act; history is not backdated. -/
structure RevocationEvent {Obj D Packet : Type*}
    (e : CachedEvidence Packet) (g : Grant Obj D) where
  revokedAt : Nat
  evidence_was_live : LiveAt g e.occurredAt
  after_evidence : e.occurredAt < revokedAt

def reviewRevocation : RevocationEvent cachedReview reviewerPanelGrant where
  revokedAt := 2
  evidence_was_live := by
    norm_num [LiveAt, reviewerPanelGrant, cachedReview]
  after_evidence := by decide

theorem revocation_preserves_history (r : RevocationEvent cachedReview reviewerPanelGrant) :
    PersistedAt cachedReview r.revokedAt := by
  exact Nat.le_of_lt r.after_evidence

/-- Restoration is a fresh live-root replay of the identical cached packet. -/
structure Restoration {Obj D Packet : Type*}
    (old : CachedEvidence Packet) (newGrant : Grant Obj D) where
  replayedAt : Nat
  replayPacket : Packet
  packet_unchanged : replayPacket = old.packet
  evidence_available : PersistedAt old replayedAt
  live_successor_root : LiveAt newGrant replayedAt

theorem restoration_requires_live_successor {Obj D Packet : Type*}
    {old : CachedEvidence Packet} {newGrant : Grant Obj D}
    (r : Restoration old newGrant) : LiveAt newGrant r.replayedAt :=
  r.live_successor_root

theorem cached_record_alone_cannot_restore_at_revocation :
  ¬ ∃ r : Restoration cachedReview
      (revoke reviewerPanelGrant 2 (by decide)), r.replayedAt = 2 := by
  rintro ⟨r, hr⟩
  have hl : LiveAt (revoke reviewerPanelGrant 2 (by decide)) 2 := by
    simpa [hr] using r.live_successor_root
  exact (revoked_not_live_at reviewerPanelGrant 2 (by decide)) hl

structure LocalCoherenceAudit where
  overlapDefects : List Nat

def FlatLocal (a : LocalCoherenceAudit) : Prop := ∀ d ∈ a.overlapDefects, d = 0

structure DescentAudit where
  localAudit : LocalCoherenceAudit
  globalReconstruction : Bool
  ambiguityRank : Nat

def EffectiveUniqueDescent (a : DescentAudit) : Prop :=
  FlatLocal a.localAudit ∧ a.globalReconstruction = true ∧ a.ambiguityRank = 0

def flatButIneffective : DescentAudit where
  localAudit := ⟨[0, 0, 0]⟩
  globalReconstruction := false
  ambiguityRank := 1

theorem flat_local_does_not_imply_effective_unique_descent :
    FlatLocal flatButIneffective.localAudit ∧ ¬ EffectiveUniqueDescent flatButIneffective := by
  simp [FlatLocal, EffectiveUniqueDescent, flatButIneffective]

/-- Proof-relevant effective descent: restriction has a two-sided reconstruction. -/
structure DescentEquivalence (Global Local : Type*) where
  restrict : Global → Local
  reconstruct : Local → Global
  reconstruct_restrict : ∀ g, reconstruct (restrict g) = g
  restrict_reconstruct : ∀ l, restrict (reconstruct l) = l

def boolDescentEquivalence : DescentEquivalence Bool Bool where
  restrict := id
  reconstruct := id
  reconstruct_restrict := fun _ ↦ rfl
  restrict_reconstruct := fun _ ↦ rfl

/-- Flat local data can exist even when no global object can reconstruct it. -/
theorem flat_local_without_proof_relevant_descent :
    FlatLocal ⟨[0]⟩ ∧ IsEmpty (DescentEquivalence Empty Unit) := by
  constructor
  · simp [FlatLocal]
  · constructor
    intro d
    exact (d.reconstruct ()).elim

structure HolonomyAudit where
  defect : Int

def ZeroHolonomy (h : HolonomyAudit) : Prop := h.defect = 0
def NonzeroHolonomy (h : HolonomyAudit) : Prop := h.defect ≠ 0

theorem zero_holonomy_excludes_nonzero (h : HolonomyAudit) :
    ZeroHolonomy h → ¬ NonzeroHolonomy h := by
  simp [ZeroHolonomy, NonzeroHolonomy]

def flatReplayAtlas : HolonomyAudit := ⟨0⟩
def rivalReplayDisagreement : HolonomyAudit := ⟨1⟩

theorem replay_holonomy_fixtures :
    ZeroHolonomy flatReplayAtlas ∧ NonzeroHolonomy rivalReplayDisagreement := by
  simp [ZeroHolonomy, NonzeroHolonomy, flatReplayAtlas, rivalReplayDisagreement]

/-- Index for the minimal family of evidence/grant fibers. -/
structure AuthorityIndex (D : Type*) where
  time : Nat
  kind : AuthorityKind
  domain : D

/-- An evidence record and grant inhabiting the same time/kind/domain fiber. -/
structure IndexedRecord (Obj D Packet : Type*) where
  index : AuthorityIndex D
  evidence : CachedEvidence Packet
  grant : Grant Obj D
  evidence_available : PersistedAt evidence index.time
  grant_live : LiveAt grant index.time
  kind_indexed : grant.kind = index.kind
  domain_indexed : grant.domain = index.domain

/-- The three logically independent admission gates requested by the audit. -/
structure AdmissionAudit where
  effectiveDescent : Bool
  temporalValidity : Bool
  kindPreservation : Bool

def Admissible (a : AdmissionAudit) : Prop :=
  a.effectiveDescent = true ∧ a.temporalValidity = true ∧
    a.kindPreservation = true

def noEffectiveDescent : AdmissionAudit := ⟨false, true, true⟩
def noTemporalValidity : AdmissionAudit := ⟨true, false, true⟩
def noKindPreservation : AdmissionAudit := ⟨true, true, false⟩

theorem effective_descent_is_independent :
    noEffectiveDescent.temporalValidity = true ∧
    noEffectiveDescent.kindPreservation = true ∧
    ¬ Admissible noEffectiveDescent := by
  simp [Admissible, noEffectiveDescent]

theorem temporal_validity_is_independent :
    noTemporalValidity.effectiveDescent = true ∧
    noTemporalValidity.kindPreservation = true ∧
    ¬ Admissible noTemporalValidity := by
  simp [Admissible, noTemporalValidity]

theorem kind_preservation_is_independent :
    noKindPreservation.effectiveDescent = true ∧
    noKindPreservation.temporalValidity = true ∧
    ¬ Admissible noKindPreservation := by
  simp [Admissible, noKindPreservation]

/-- Every single omitted gate has a countermodel satisfying the other two. -/
theorem descent_time_kind_pairwise_independent :
    (noEffectiveDescent.temporalValidity = true ∧
      noEffectiveDescent.kindPreservation = true ∧ ¬ Admissible noEffectiveDescent) ∧
    (noTemporalValidity.effectiveDescent = true ∧
      noTemporalValidity.kindPreservation = true ∧ ¬ Admissible noTemporalValidity) ∧
    (noKindPreservation.effectiveDescent = true ∧
      noKindPreservation.temporalValidity = true ∧ ¬ Admissible noKindPreservation) := by
  exact ⟨effective_descent_is_independent,
    temporal_validity_is_independent, kind_preservation_is_independent⟩

namespace LinearConsumption

def ExactlyOne (o : Bool × Bool) : Prop := o.1 ≠ o.2

structure DisconnectedViews (State : Type*) where
  stateA : State
  stateB : State
  identicalState : stateA = stateB
  execute : State → Bool

def decisions {State : Type*} (v : DisconnectedViews State) : Bool × Bool :=
  (v.execute v.stateA, v.execute v.stateB)

theorem decisions_agree {State : Type*} (v : DisconnectedViews State) :
    (decisions v).1 = (decisions v).2 := by
  simp [decisions, v.identicalState]

theorem outcomes_are_00_or_11 {State : Type*} (v : DisconnectedViews State) :
    decisions v = (false, false) ∨ decisions v = (true, true) := by
  have h := decisions_agree v
  rcases hv : decisions v with ⟨a, b⟩
  cases a <;> cases b <;> simp_all

theorem no_unique_consumption_without_coordination {State : Type*}
    (v : DisconnectedViews State) : ¬ ExactlyOne (decisions v) := by
  intro h
  exact h (decisions_agree v)

def reportAfterCommit (o : Bool × Bool) (_lateMessage : Unit) : Bool × Bool := o

theorem delayed_coherence_cannot_undo_execution {State : Type*}
    (v : DisconnectedViews State) :
    ¬ ExactlyOne (reportAfterCommit (decisions v) ()) := by
  simpa [reportAfterCommit] using no_unique_consumption_without_coordination v

def IndependentSeeds {Seed : Type*} (_ _ : Seed) : Prop := True

def RandomizedGuarantee {State Seed : Type*} (state : State)
    (rule : State → Seed → Bool) (allowed : Seed → Seed → Prop) : Prop :=
  ∀ a b, allowed a b → ExactlyOne (rule state a, rule state b)

theorem independent_randomness_cannot_guarantee_exactly_one
    {State Seed : Type*} [Nonempty Seed] (state : State) (rule : State → Seed → Bool) :
    ¬ RandomizedGuarantee state rule IndependentSeeds := by
  intro h
  let s : Seed := Classical.choice inferInstance
  exact (h s s trivial) rfl

structure SharedCoordination (Seed : Type*) where
  allowed : Seed → Seed → Prop
  excludesDiagonal : ∀ s, ¬ allowed s s

theorem guaranteed_correlation_excludes_diagonal {State Seed : Type*}
    (state : State) (rule : State → Seed → Bool) (allowed : Seed → Seed → Prop)
    (h : RandomizedGuarantee state rule allowed) : ∀ s, ¬ allowed s s := by
  intro s hs
  exact (h s s hs) rfl

inductive ResourceKind where
  | singleUse
  | boundedMultiplicity (bound : Nat)
  deriving DecidableEq, Repr

structure KindTransport where
  before : ResourceKind
  after : ResourceKind
  preservesKind : after = before

theorem replay_cannot_turn_two_use_into_single_use (t : KindTransport)
    (h : t.before = .boundedMultiplicity 2) : t.after ≠ .singleUse := by
  rw [t.preservesKind, h]
  simp

inductive RepairKind where
  | sharedLinearization | priorPartition | boundedMultiplicityTwo
  deriving DecidableEq, Repr

structure SourceAuthority where grantId : String

/-- Shared minimal predicate for records carrying optional source authority. -/
def SourceAuthorized (authority : Option SourceAuthority) : Prop :=
  ∃ witness, authority = some witness

theorem some_source_authority_is_authorized (authority : SourceAuthority) :
    SourceAuthorized (some authority) := by
  exact ⟨authority, rfl⟩

theorem absent_source_authority_is_not_authorized :
    ¬ SourceAuthorized none := by
  simp [SourceAuthorized]

structure Repair where
  kind : RepairKind
  sourceAuthority : Option SourceAuthority

def RepairAuthorized (r : Repair) : Prop := SourceAuthorized r.sourceAuthority

theorem every_repair_requires_additional_source_authority (kind : RepairKind) :
    ¬ RepairAuthorized ⟨kind, none⟩ := by
  exact absent_source_authority_is_not_authorized

theorem repair_types_are_pairwise_distinct :
    RepairKind.sharedLinearization ≠ .priorPartition ∧
    RepairKind.sharedLinearization ≠ .boundedMultiplicityTwo ∧
    RepairKind.priorPartition ≠ .boundedMultiplicityTwo := by
  decide

def sharedLinearizationOutcome : Bool × Bool := (true, false)

theorem shared_linearization_preserves_single_use :
    ExactlyOne sharedLinearizationOutcome := by
  simp [ExactlyOne, sharedLinearizationOutcome]

inductive Locus where | siteA | siteB deriving DecidableEq, Repr

def priorPartitionOutcome : Locus → Bool × Bool
  | .siteA => (true, false)
  | .siteB => (false, true)

theorem prior_partition_preserves_linearity (site : Locus) :
    ExactlyOne (priorPartitionOutcome site) := by
  cases site <;> simp [ExactlyOne, priorPartitionOutcome]

def boundedMultiplicityTwoOutcome : Bool × Bool := (true, true)

theorem multiplicity_two_is_not_single_use :
    ¬ ExactlyOne boundedMultiplicityTwoOutcome := by
  simp [ExactlyOne, boundedMultiplicityTwoOutcome]

def duplicatedNonceLogs : DisconnectedViews Bool where
  stateA := false
  stateB := false
  identicalState := rfl
  execute := not

theorem duplicated_nonce_logs_are_not_global_linear_state :
    decisions duplicatedNonceLogs = (true, true) ∧
      ¬ ExactlyOne (decisions duplicatedNonceLogs) := by
  simp [decisions, duplicatedNonceLogs, ExactlyOne]

inductive OmittedPremise where
  | sameCapability | identicalState | identicalRule | noCommunication
  deriving DecidableEq, Repr

def omissionCountermodel : OmittedPremise → Bool × Bool
  | .sameCapability => (true, false)
  | .identicalState => (true, false)
  | .identicalRule => (true, false)
  | .noCommunication => (true, false)

theorem every_omitted_premise_has_finite_countermodel (p : OmittedPremise) :
    ExactlyOne (omissionCountermodel p) := by
  cases p <;> simp [ExactlyOne, omissionCountermodel]

/-! Atomic shared-linearization specification. -/

inductive CellState where
  | unused | consumed
  deriving DecidableEq, Repr

/-- One indivisible specification step; this does not implement atomicity. -/
def atomicStep : CellState → CellState × Bool
  | .unused => (.consumed, true)
  | .consumed => (.consumed, false)

inductive TwoSiteOrder where
  | AthenB | BthenA
  deriving DecidableEq, Repr

/-- Sequential specification outcome, returned in fixed `(A,B)` label order. -/
def executeInOrder : TwoSiteOrder → Bool × Bool
  | .AthenB =>
      let s₁ := atomicStep .unused
      let s₂ := atomicStep s₁.1
      (s₁.2, s₂.2)
  | .BthenA =>
      let s₁ := atomicStep .unused
      let s₂ := atomicStep s₁.1
      (s₂.2, s₁.2)

theorem atomic_specification_exactly_one (order : TwoSiteOrder) :
    ExactlyOne (executeInOrder order) := by
  cases order <;> simp [ExactlyOne, executeInOrder, atomicStep]

structure TwoSiteHistory where
  outcome : Bool × Bool

/-- A history is linearizable when one legal sequential order explains it. -/
structure LinearizationWitness (h : TwoSiteHistory) where
  order : TwoSiteOrder
  agrees : h.outcome = executeInOrder order

theorem linearizable_history_exactly_one (h : TwoSiteHistory)
    (w : LinearizationWitness h) : ExactlyOne h.outcome := by
  rw [w.agrees]
  exact atomic_specification_exactly_one w.order

def concurrentWinnerA : TwoSiteHistory := ⟨(true, false)⟩
def concurrentWinnerB : TwoSiteHistory := ⟨(false, true)⟩

def winnerA_linearizes : LinearizationWitness concurrentWinnerA :=
  ⟨.AthenB, rfl⟩

def winnerB_linearizes : LinearizationWitness concurrentWinnerB :=
  ⟨.BthenA, rfl⟩

/-- The duplicated-local `(true,true)` history has no atomic linearization. -/
theorem duplicated_success_has_no_linearization :
    IsEmpty (LinearizationWitness ⟨(true, true)⟩) := by
  constructor
  intro w
  rcases w with ⟨order, h⟩
  cases order <;> simp [executeInOrder, atomicStep] at h

structure AuthorizedAtomicLinearizer where
  authority : SourceAuthority
  initial : CellState
  initiallyUnused : initial = .unused

theorem authorized_linearizer_supplies_authorized_repair
    (a : AuthorizedAtomicLinearizer) :
    RepairAuthorized ⟨.sharedLinearization, some a.authority⟩ := by
  exact ⟨a.authority, rfl⟩

/-! Finite labeled histories. -/

/-- The first operation consumes the cell; all later operations fail. -/
def runAtomicOrder {Op : Type*} : List Op → List (Op × Bool)
  | [] => []
  | first :: rest => (first, true) :: rest.map (fun op ↦ (op, false))

def historySuccessCount {Op : Type*} (events : List (Op × Bool)) : Nat :=
  (events.filter (fun event ↦ event.2)).length

theorem runAtomicOrder_successCount {Op : Type*} (first : Op) (rest : List Op) :
    historySuccessCount (runAtomicOrder (first :: rest)) = 1 := by
  simp [historySuccessCount, runAtomicOrder]

structure FiniteHistory (Op : Type*) where
  invoked : List Op
  events : List (Op × Bool)

/-- A finite history linearizes when a permutation of invocations explains its events. -/
structure FiniteLinearizationWitness {Op : Type*} (h : FiniteHistory Op) where
  order : List Op
  sameOperations : order.Perm h.invoked
  agrees : h.events = runAtomicOrder order

theorem nonempty_linearizable_history_exactly_one {Op : Type*}
    (h : FiniteHistory Op) (w : FiniteLinearizationWitness h)
    (hne : h.invoked ≠ []) : historySuccessCount h.events = 1 := by
  have horder : w.order ≠ [] := by
    intro hw
    have hlen := w.sameOperations.length_eq
    rw [hw] at hlen
    apply hne
    simpa using hlen.symm
  obtain ⟨first, rest, horderEq⟩ := List.exists_cons_of_ne_nil horder
  rw [w.agrees, horderEq]
  exact runAtomicOrder_successCount first rest

def twoSuccessHistory : FiniteHistory (Fin 2) where
  invoked := [0, 1]
  events := [(0, true), (1, true)]

theorem two_success_history_has_no_finite_linearization :
    IsEmpty (FiniteLinearizationWitness twoSuccessHistory) := by
  constructor
  intro w
  have hc := nonempty_linearizable_history_exactly_one twoSuccessHistory w (by decide)
  norm_num [historySuccessCount, twoSuccessHistory] at hc

/-! Real-time precedence for two-site histories. -/

structure OperationInterval where
  invokedAt : Nat
  respondedAt : Nat
  wellFormed : invokedAt < respondedAt

def RealTimePrecedes (a b : OperationInterval) : Prop :=
  a.respondedAt ≤ b.invokedAt

structure TimedTwoSiteHistory where
  intervalA : OperationInterval
  intervalB : OperationInterval
  history : TwoSiteHistory

/-- Linearization must respect every completed-before-invoked relation. -/
structure RealTimeLinearizationWitness (h : TimedTwoSiteHistory)
    extends LinearizationWitness h.history where
  respectsAB : RealTimePrecedes h.intervalA h.intervalB → order = .AthenB
  respectsBA : RealTimePrecedes h.intervalB h.intervalA → order = .BthenA

theorem real_time_linearizable_history_exactly_one (h : TimedTwoSiteHistory)
    (w : RealTimeLinearizationWitness h) : ExactlyOne h.history.outcome := by
  exact linearizable_history_exactly_one h.history w.toLinearizationWitness

def interval (invoked responded : Nat) (h : invoked < responded) : OperationInterval :=
  ⟨invoked, responded, h⟩

/-- Overlapping operations admit either legal linearization order. -/
def overlappingWinnerA : TimedTwoSiteHistory where
  intervalA := interval 0 3 (by decide)
  intervalB := interval 1 2 (by decide)
  history := concurrentWinnerA

def overlappingWinnerA_linearizes : RealTimeLinearizationWitness overlappingWinnerA where
  order := .AthenB
  agrees := rfl
  respectsAB := by simp [RealTimePrecedes, overlappingWinnerA, interval]
  respectsBA := by simp [RealTimePrecedes, overlappingWinnerA, interval]

/-- B completes before A is invoked, but the observed output says A won. -/
def precedenceViolation : TimedTwoSiteHistory where
  intervalA := interval 2 3 (by decide)
  intervalB := interval 0 1 (by decide)
  history := concurrentWinnerA

theorem precedence_violation_has_no_real_time_linearization :
    IsEmpty (RealTimeLinearizationWitness precedenceViolation) := by
  constructor
  intro w
  have horderA : w.order = .AthenB := by
    cases horder : w.order
    · rfl
    · have ha := w.agrees
      simp [precedenceViolation, concurrentWinnerA, executeInOrder, atomicStep,
        horder] at ha
  have horderB : w.order = .BthenA := by
    apply w.respectsBA
    norm_num [RealTimePrecedes, precedenceViolation, interval]
  rw [horderA] at horderB
  contradiction

/-! Compare-and-set refinement of the atomic specification. -/

/-- `false` is unused and `true` is consumed in the concrete Boolean cell. -/
def abstractCellState : Bool → CellState
  | false => .unused
  | true => .consumed

/-- Concrete compare-and-set transition: return the new cell and success bit. -/
def compareAndSet : Bool → Bool × Bool
  | false => (true, true)
  | true => (true, false)

theorem compareAndSet_refines_atomicStep (memory : Bool) :
    (abstractCellState (compareAndSet memory).1, (compareAndSet memory).2) =
      atomicStep (abstractCellState memory) := by
  cases memory <;> rfl

def runTwoCAS : TwoSiteOrder → Bool × Bool
  | .AthenB =>
      let first := compareAndSet false
      let second := compareAndSet first.1
      (first.2, second.2)
  | .BthenA =>
      let first := compareAndSet false
      let second := compareAndSet first.1
      (second.2, first.2)

theorem two_compareAndSet_refines_atomic_order (order : TwoSiteOrder) :
    runTwoCAS order = executeInOrder order := by
  cases order <;> rfl

theorem two_compareAndSet_exactly_one (order : TwoSiteOrder) :
    ExactlyOne (runTwoCAS order) := by
  rw [two_compareAndSet_refines_atomic_order]
  exact atomic_specification_exactly_one order

/-- Hostile non-atomic implementation: both read unused before either write. -/
structure SplitReadWriteTrace where
  readA : Bool
  readB : Bool
  successA : Bool
  successB : Bool

def lostUpdateTrace : SplitReadWriteTrace where
  readA := false
  readB := false
  successA := true
  successB := true

def splitOutcome (t : SplitReadWriteTrace) : Bool × Bool :=
  (t.successA, t.successB)

theorem split_read_write_breaks_single_use :
    splitOutcome lostUpdateTrace = (true, true) ∧
      ¬ ExactlyOne (splitOutcome lostUpdateTrace) := by
  simp [splitOutcome, lostUpdateTrace, ExactlyOne]

theorem split_read_write_has_no_atomic_witness :
    IsEmpty (LinearizationWitness ⟨splitOutcome lostUpdateTrace⟩) := by
  simpa [splitOutcome, lostUpdateTrace] using duplicated_success_has_no_linearization

structure AuthorizedCompareAndSet where
  authority : SourceAuthority
  concreteInitial : Bool
  startsUnused : concreteInitial = false

theorem authorized_compareAndSet_binds_atomic_repair (a : AuthorizedCompareAndSet) :
    RepairAuthorized ⟨.sharedLinearization, some a.authority⟩ := by
  exact ⟨a.authority, rfl⟩

/-! Revocation-linearized execution leases. -/

structure ExecutionLease where
  validatedEpoch : Nat
  expiresAt : Nat
  kind : AuthorityKind

structure LeaseState where
  liveEpoch : Nat
  nonceConsumed : Bool

def LeaseExecutable (lease : ExecutionLease) (state : LeaseState)
    (now : Nat) (requestedKind : AuthorityKind) : Prop :=
  state.liveEpoch = lease.validatedEpoch ∧
  now < lease.expiresAt ∧
  state.nonceConsumed = false ∧
  requestedKind = lease.kind

/-- One atomic use validates epoch, expiry, nonce, and kind, then consumes. -/
noncomputable def attemptLease (lease : ExecutionLease) (state : LeaseState)
    (now : Nat) (requestedKind : AuthorityKind) : LeaseState × Bool := by
  classical
  exact if LeaseExecutable lease state now requestedKind then
      (⟨state.liveEpoch, true⟩, true)
    else
      (state, false)

theorem attemptLease_success_iff (lease : ExecutionLease) (state : LeaseState)
    (now : Nat) (requestedKind : AuthorityKind) :
    (attemptLease lease state now requestedKind).2 = true ↔
      LeaseExecutable lease state now requestedKind := by
  classical
  by_cases h : LeaseExecutable lease state now requestedKind <;>
    simp [attemptLease, h]

def liveLease : ExecutionLease where
  validatedEpoch := 3
  expiresAt := 10
  kind := .readout

def freshLeaseState : LeaseState := ⟨3, false⟩

theorem live_fresh_scoped_lease_succeeds :
    attemptLease liveLease freshLeaseState 5 .readout =
      (⟨3, true⟩, true) := by
  simp [attemptLease, LeaseExecutable, liveLease, freshLeaseState]

theorem consumed_nonce_replay_fails :
    (attemptLease liveLease (attemptLease liveLease freshLeaseState 5 .readout).1
      6 .readout).2 = false := by
  simp [attemptLease, LeaseExecutable, liveLease, freshLeaseState]

def revokeEpoch (state : LeaseState) : LeaseState :=
  ⟨state.liveEpoch + 1, state.nonceConsumed⟩

theorem revocation_between_check_and_use_fails :
    (attemptLease liveLease (revokeEpoch freshLeaseState) 5 .readout).2 = false := by
  simp [attemptLease, LeaseExecutable, liveLease, freshLeaseState, revokeEpoch]

theorem expired_lease_fails :
    (attemptLease liveLease freshLeaseState 10 .readout).2 = false := by
  simp [attemptLease, LeaseExecutable, liveLease, freshLeaseState]

theorem lease_cannot_widen_authority_kind :
    (attemptLease liveLease freshLeaseState 5 .selector).2 = false := by
  simp [attemptLease, LeaseExecutable, liveLease, freshLeaseState]

theorem cached_validation_does_not_override_epoch_revocation :
    liveLease.validatedEpoch = freshLeaseState.liveEpoch ∧
      (attemptLease liveLease (revokeEpoch freshLeaseState) 5 .readout).2 = false := by
  simp [attemptLease, LeaseExecutable, liveLease, freshLeaseState, revokeEpoch]

/-! Retry identity and at-most-once execution. -/

abbrev RequestId := Nat

structure RequestLedger where
  consumed : Finset RequestId

inductive DeliveryDisposition where
  | executed | replayed
  deriving DecidableEq, Repr

/-- Atomic request admission: insert a fresh ID or classify a duplicate as replay. -/
def admitRequest (ledger : RequestLedger) (id : RequestId) :
    RequestLedger × DeliveryDisposition :=
  if id ∈ ledger.consumed then
    (ledger, .replayed)
  else
    (⟨insert id ledger.consumed⟩, .executed)

def emptyRequestLedger : RequestLedger := ⟨∅⟩

theorem first_delivery_executes (id : RequestId) :
    (admitRequest emptyRequestLedger id).2 = .executed := by
  simp [admitRequest, emptyRequestLedger]

theorem same_id_retry_is_replay (ledger : RequestLedger) (id : RequestId) :
    (admitRequest (admitRequest ledger id).1 id).2 = .replayed := by
  by_cases h : id ∈ ledger.consumed <;> simp [admitRequest, h]

theorem same_id_retry_does_not_grow_ledger (ledger : RequestLedger) (id : RequestId) :
    (admitRequest (admitRequest ledger id).1 id).1.consumed =
      (admitRequest ledger id).1.consumed := by
  by_cases h : id ∈ ledger.consumed <;> simp [admitRequest, h]

theorem distinct_ids_can_both_execute (a b : RequestId) (h : a ≠ b) :
    (admitRequest emptyRequestLedger a).2 = .executed ∧
    (admitRequest (admitRequest emptyRequestLedger a).1 b).2 = .executed := by
  simp [admitRequest, emptyRequestLedger, Ne.symm h]

/-- Hostile fixture: relabeling a retry as fresh defeats duplicate suppression. -/
theorem fresh_id_retry_countermodel :
    (admitRequest emptyRequestLedger 7).2 = .executed ∧
    (admitRequest (admitRequest emptyRequestLedger 7).1 8).2 = .executed := by
  exact distinct_ids_can_both_execute 7 8 (by decide)

structure IdentifiedRequest where
  id : RequestId
  identityAuthority : SourceAuthority

theorem identified_request_carries_source_authority (r : IdentifiedRequest) :
    Nonempty SourceAuthority :=
  ⟨r.identityAuthority⟩

/-! One transaction combining request identity with lease consumption. -/

structure IdentifiedLeaseState where
  leaseState : LeaseState
  requestLedger : RequestLedger

inductive IdentifiedDisposition where
  | executed | replayed | rejected
  deriving DecidableEq, Repr

noncomputable def attemptIdentifiedLease (lease : ExecutionLease)
    (state : IdentifiedLeaseState) (request : IdentifiedRequest)
    (now : Nat) (requestedKind : AuthorityKind) :
    IdentifiedLeaseState × IdentifiedDisposition := by
  classical
  if request.id ∈ state.requestLedger.consumed then
    exact (state, .replayed)
  else
    let leaseAttempt := attemptLease lease state.leaseState now requestedKind
    if leaseAttempt.2 = true then
      exact (⟨leaseAttempt.1, ⟨insert request.id state.requestLedger.consumed⟩⟩,
        .executed)
    else
      exact (state, .rejected)

def requestAuthority : SourceAuthority := ⟨"fixture-request-authority"⟩
def request7 : IdentifiedRequest := ⟨7, requestAuthority⟩
def request8 : IdentifiedRequest := ⟨8, requestAuthority⟩

def freshIdentifiedLeaseState : IdentifiedLeaseState :=
  ⟨freshLeaseState, emptyRequestLedger⟩

theorem fresh_identified_lease_executes :
    (attemptIdentifiedLease liveLease freshIdentifiedLeaseState request7
      5 .readout).2 = .executed := by
  simp [attemptIdentifiedLease, freshIdentifiedLeaseState, request7,
    emptyRequestLedger, attemptLease, LeaseExecutable, liveLease, freshLeaseState]

theorem successful_identified_execution_consumes_both :
    let next := (attemptIdentifiedLease liveLease freshIdentifiedLeaseState request7
      5 .readout).1
    next.leaseState.nonceConsumed = true ∧ 7 ∈ next.requestLedger.consumed := by
  simp [attemptIdentifiedLease, freshIdentifiedLeaseState, request7,
    emptyRequestLedger, attemptLease, LeaseExecutable, liveLease, freshLeaseState]

theorem same_identified_request_replays :
    let next := (attemptIdentifiedLease liveLease freshIdentifiedLeaseState request7
      5 .readout).1
    (attemptIdentifiedLease liveLease next request7 6 .readout).2 = .replayed := by
  simp [attemptIdentifiedLease, freshIdentifiedLeaseState, request7,
    emptyRequestLedger, attemptLease, LeaseExecutable, liveLease, freshLeaseState]

theorem fresh_second_request_cannot_reuse_consumed_lease :
    let next := (attemptIdentifiedLease liveLease freshIdentifiedLeaseState request7
      5 .readout).1
    (attemptIdentifiedLease liveLease next request8 6 .readout).2 = .rejected := by
  simp [attemptIdentifiedLease, freshIdentifiedLeaseState, request7, request8,
    emptyRequestLedger, attemptLease, LeaseExecutable, liveLease, freshLeaseState]

theorem rejected_request_does_not_poison_identity_ledger :
    let revoked : IdentifiedLeaseState :=
      ⟨revokeEpoch freshLeaseState, emptyRequestLedger⟩
    let next := (attemptIdentifiedLease liveLease revoked request7 5 .readout).1
    7 ∉ next.requestLedger.consumed := by
  simp [attemptIdentifiedLease, request7, emptyRequestLedger, attemptLease,
    LeaseExecutable, liveLease, freshLeaseState, revokeEpoch]

/-! Cached response replay. -/

structure ResponseState (Result : Type*) where
  leaseState : LeaseState
  responses : RequestId → Option Result

inductive ResponseDisposition (Result : Type*) where
  | executed (result : Result)
  | replayed (result : Result)
  | rejected
  deriving DecidableEq, Repr

noncomputable def attemptWithResponse {Result : Type*}
    (produce : RequestId → Result) (lease : ExecutionLease)
    (state : ResponseState Result) (request : IdentifiedRequest)
    (now : Nat) (requestedKind : AuthorityKind) :
    ResponseState Result × ResponseDisposition Result := by
  classical
  match state.responses request.id with
  | some result => exact (state, .replayed result)
  | none =>
      let leaseAttempt := attemptLease lease state.leaseState now requestedKind
      if leaseAttempt.2 = true then
        let result := produce request.id
        exact (⟨leaseAttempt.1, Function.update state.responses request.id (some result)⟩,
          .executed result)
      else
        exact (state, .rejected)

def emptyResponseState : ResponseState Nat :=
  ⟨freshLeaseState, fun _ ↦ none⟩

def fixtureResult (id : RequestId) : Nat := id + 100

theorem first_response_execution_is_cached :
    let next := (attemptWithResponse fixtureResult liveLease emptyResponseState
      request7 5 .readout).1
    (attemptWithResponse fixtureResult liveLease emptyResponseState
      request7 5 .readout).2 = .executed 107 ∧
    next.responses 7 = some 107 := by
  simp [attemptWithResponse, fixtureResult, emptyResponseState, request7,
    attemptLease, LeaseExecutable, liveLease, freshLeaseState]

theorem retry_returns_identical_cached_response :
    let next := (attemptWithResponse fixtureResult liveLease emptyResponseState
      request7 5 .readout).1
    (attemptWithResponse fixtureResult liveLease next request7 6 .readout).2 =
      .replayed 107 := by
  simp [attemptWithResponse, fixtureResult, emptyResponseState, request7,
    attemptLease, LeaseExecutable, liveLease, freshLeaseState, Function.update]

theorem rejected_request_creates_no_cached_response :
    let revoked : ResponseState Nat :=
      ⟨revokeEpoch freshLeaseState, fun _ ↦ none⟩
    let next := (attemptWithResponse fixtureResult liveLease revoked request7 5 .readout).1
    next.responses 7 = none := by
  simp [attemptWithResponse, attemptLease,
    LeaseExecutable, liveLease, freshLeaseState, revokeEpoch]

/-- Crash split: consumption persisted but its response did not. -/
structure CrashSplitRecord where
  consumedPersisted : Bool
  responsePersisted : Bool

def AtMostOnceSafe (r : CrashSplitRecord) : Prop := r.consumedPersisted = true
def ReplayComplete (r : CrashSplitRecord) : Prop := r.responsePersisted = true

def consumptionWithoutResponse : CrashSplitRecord := ⟨true, false⟩

theorem at_most_once_does_not_imply_replay_complete :
    AtMostOnceSafe consumptionWithoutResponse ∧
      ¬ ReplayComplete consumptionWithoutResponse := by
  simp [AtMostOnceSafe, ReplayComplete, consumptionWithoutResponse]

/-! Crash-atomic persistence invariant. -/

structure DurableExecution (Result : Type*) where
  nonceConsumed : Bool
  response : Option Result

def CrashConsistent {Result : Type*} (d : DurableExecution Result) : Prop :=
  d.nonceConsumed = d.response.isSome

def durablePreState (Result : Type*) : DurableExecution Result :=
  ⟨false, none⟩

def durableCommit {Result : Type*} (result : Result) : DurableExecution Result :=
  ⟨true, some result⟩

theorem durable_pre_state_consistent (Result : Type*) :
    CrashConsistent (durablePreState Result) := by
  simp [CrashConsistent, durablePreState]

theorem durable_commit_consistent {Result : Type*} (result : Result) :
    CrashConsistent (durableCommit result) := by
  simp [CrashConsistent, durableCommit]

inductive AtomicPersistenceOutcome (Result : Type*) where
  | beforeCommit
  | afterCommit (result : Result)

def recoverAtomic {Result : Type*} : AtomicPersistenceOutcome Result → DurableExecution Result
  | .beforeCommit => durablePreState Result
  | .afterCommit result => durableCommit result

theorem atomic_recovery_preserves_consistency {Result : Type*}
    (outcome : AtomicPersistenceOutcome Result) :
    CrashConsistent (recoverAtomic outcome) := by
  cases outcome <;> simp [recoverAtomic, CrashConsistent, durablePreState, durableCommit]

def nonceOnlyCrash : DurableExecution Nat := ⟨true, none⟩
def responseOnlyCrash : DurableExecution Nat := ⟨false, some 107⟩

theorem nonce_only_crash_is_inconsistent : ¬ CrashConsistent nonceOnlyCrash := by
  simp [CrashConsistent, nonceOnlyCrash]

theorem response_only_crash_is_inconsistent : ¬ CrashConsistent responseOnlyCrash := by
  simp [CrashConsistent, responseOnlyCrash]

theorem crash_consistency_equates_consumption_and_replayability
    {Result : Type*} (d : DurableExecution Result) (h : CrashConsistent d) :
    (d.nonceConsumed = true ↔ ∃ result, d.response = some result) := by
  cases hr : d.response with
  | none =>
      simp [CrashConsistent, hr] at h
      simp [h]
  | some result =>
      simp [CrashConsistent, hr] at h
      simp [h]

/-! Leases requiring multiple authority roots. -/

structure MultiRootLease (n : Nat) where
  validatedEpochs : Fin n → Nat
  expiresAt : Nat
  kind : AuthorityKind
  roots_nonempty : 0 < n

structure MultiRootState (n : Nat) where
  liveEpochs : Fin n → Nat
  nonceConsumed : Bool

def MultiRootExecutable {n : Nat} (lease : MultiRootLease n)
    (state : MultiRootState n) (now : Nat) (requestedKind : AuthorityKind) : Prop :=
  (∀ i, state.liveEpochs i = lease.validatedEpochs i) ∧
  now < lease.expiresAt ∧ state.nonceConsumed = false ∧ requestedKind = lease.kind

noncomputable def attemptMultiRootLease {n : Nat} (lease : MultiRootLease n)
    (state : MultiRootState n) (now : Nat) (requestedKind : AuthorityKind) :
    MultiRootState n × Bool := by
  classical
  exact if MultiRootExecutable lease state now requestedKind then
      (⟨state.liveEpochs, true⟩, true)
    else
      (state, false)

theorem attemptMultiRootLease_success_iff {n : Nat} (lease : MultiRootLease n)
    (state : MultiRootState n) (now : Nat) (requestedKind : AuthorityKind) :
    (attemptMultiRootLease lease state now requestedKind).2 = true ↔
      MultiRootExecutable lease state now requestedKind := by
  classical
  by_cases h : MultiRootExecutable lease state now requestedKind <;>
    simp [attemptMultiRootLease, h]

def twoRootLease : MultiRootLease 2 where
  validatedEpochs := ![4, 9]
  expiresAt := 20
  kind := .readout
  roots_nonempty := by decide

def twoRootFresh : MultiRootState 2 where
  liveEpochs := ![4, 9]
  nonceConsumed := false

def secondRootRevoked : MultiRootState 2 where
  liveEpochs := ![4, 10]
  nonceConsumed := false

theorem all_live_roots_succeed :
    (attemptMultiRootLease twoRootLease twoRootFresh 10 .readout).2 = true := by
  simp [attemptMultiRootLease, MultiRootExecutable, twoRootLease, twoRootFresh]

theorem one_revoked_root_invalidates_whole_lease :
    (attemptMultiRootLease twoRootLease secondRootRevoked 10 .readout).2 = false := by
  simp [attemptMultiRootLease, MultiRootExecutable, twoRootLease, secondRootRevoked]

theorem matching_first_root_does_not_imply_multi_root_freshness :
    secondRootRevoked.liveEpochs 0 = twoRootLease.validatedEpochs 0 ∧
      ¬ MultiRootExecutable twoRootLease secondRootRevoked 10 .readout := by
  constructor
  · decide
  · intro h
    have hsecond := h.1 (1 : Fin 2)
    norm_num [secondRootRevoked, twoRootLease] at hsecond

theorem zero_root_lease_is_unrepresentable : IsEmpty (MultiRootLease 0) := by
  constructor
  intro lease
  exact (Nat.not_lt_zero 0) lease.roots_nonempty

/-! Torn multi-root snapshot hostile model. -/

abbrev TwoEpochs := Fin 2 → Nat

def EpochsMatch (snapshot live : TwoEpochs) : Prop := ∀ i, live i = snapshot i

def requiredEpochs : TwoEpochs := ![4, 9]
def earlyEpochs : TwoEpochs := ![4, 10]
def lateEpochs : TwoEpochs := ![5, 9]

/-- Non-atomic sampling reads root 0 early and root 1 late. -/
def tornEpochRead : TwoEpochs := ![earlyEpochs 0, lateEpochs 1]

theorem torn_read_matches_every_cached_epoch :
    EpochsMatch requiredEpochs tornEpochRead := by
  intro i
  fin_cases i <;> decide

theorem early_state_never_had_all_epochs :
    ¬ EpochsMatch requiredEpochs earlyEpochs := by
  intro h
  have := h (1 : Fin 2)
  norm_num [requiredEpochs, earlyEpochs] at this

theorem late_state_never_had_all_epochs :
    ¬ EpochsMatch requiredEpochs lateEpochs := by
  intro h
  have := h (0 : Fin 2)
  norm_num [requiredEpochs, lateEpochs] at this

theorem pointwise_reads_do_not_supply_atomic_snapshot :
    EpochsMatch requiredEpochs tornEpochRead ∧
      ¬ EpochsMatch requiredEpochs earlyEpochs ∧
      ¬ EpochsMatch requiredEpochs lateEpochs := by
  exact ⟨torn_read_matches_every_cached_epoch,
    early_state_never_had_all_epochs, late_state_never_had_all_epochs⟩

/-! Version-consistent snapshot certificate. -/

structure VersionedEpochState where
  version : Nat
  epochs : TwoEpochs

structure SnapshotRead where
  openedVersion : Nat
  closedVersion : Nat
  sampled : TwoEpochs

def VersionStable (r : SnapshotRead) : Prop := r.openedVersion = r.closedVersion

/-- A certificate ties a stable read to one versioned state. -/
structure SnapshotCertificate (state : VersionedEpochState) (read : SnapshotRead) : Prop where
  stable : VersionStable read
  version_matches : read.openedVersion = state.version
  sample_matches : read.sampled = state.epochs

def tornVersionedRead : SnapshotRead where
  openedVersion := 2
  closedVersion := 4
  sampled := tornEpochRead

theorem torn_read_rejected_by_version_check : ¬ VersionStable tornVersionedRead := by
  simp [VersionStable, tornVersionedRead]

def stableEpochState : VersionedEpochState := ⟨6, requiredEpochs⟩

def stableEpochRead : SnapshotRead where
  openedVersion := 6
  closedVersion := 6
  sampled := requiredEpochs

theorem stableEpochCertificate : SnapshotCertificate stableEpochState stableEpochRead where
  stable := rfl
  version_matches := rfl
  sample_matches := rfl

theorem certified_snapshot_matches_required_epochs
    (c : SnapshotCertificate stableEpochState stableEpochRead) :
    EpochsMatch requiredEpochs stableEpochRead.sampled := by
  intro i
  rw [c.sample_matches]
  rfl

theorem stable_version_without_state_binding_is_insufficient :
    let unbound : SnapshotRead := ⟨6, 6, earlyEpochs⟩
    VersionStable unbound ∧ ¬ EpochsMatch requiredEpochs unbound.sampled := by
  dsimp [VersionStable]
  exact ⟨rfl, early_state_never_had_all_epochs⟩

/-! ABA/version-reuse hostile model. -/

structure ThreeStateTrace where
  opened : VersionedEpochState
  intervening : VersionedEpochState
  closed : VersionedEpochState

def abaTrace : ThreeStateTrace where
  opened := ⟨6, requiredEpochs⟩
  intervening := ⟨7, earlyEpochs⟩
  closed := ⟨6, requiredEpochs⟩

def EndpointVersionStable (t : ThreeStateTrace) : Prop :=
  t.opened.version = t.closed.version

def InterveningChange (t : ThreeStateTrace) : Prop :=
  t.opened.epochs ≠ t.intervening.epochs ∨
    t.intervening.epochs ≠ t.closed.epochs

theorem aba_reuse_looks_stable_despite_intervening_change :
    EndpointVersionStable abaTrace ∧ InterveningChange abaTrace := by
  constructor
  · rfl
  · left
    intro h
    have hc := congrFun h (1 : Fin 2)
    norm_num [abaTrace, requiredEpochs, earlyEpochs] at hc

/-- Every state-changing transition must allocate a strictly fresher version. -/
def FreshTransition (before after : VersionedEpochState) : Prop :=
  before.epochs ≠ after.epochs → before.version < after.version

theorem fresh_transitions_exclude_stable_ABA (t : ThreeStateTrace)
    (h₁ : FreshTransition t.opened t.intervening)
    (h₂ : FreshTransition t.intervening t.closed)
    (hc₁ : t.opened.epochs ≠ t.intervening.epochs)
    (hc₂ : t.intervening.epochs ≠ t.closed.epochs) :
    ¬ EndpointVersionStable t := by
  intro stable
  have v₁ := h₁ hc₁
  have v₂ := h₂ hc₂
  exact (Nat.ne_of_lt (lt_trans v₁ v₂)) stable

theorem aba_trace_violates_fresh_version_discipline :
    ¬ (FreshTransition abaTrace.opened abaTrace.intervening ∧
      FreshTransition abaTrace.intervening abaTrace.closed) := by
  rintro ⟨h₁, h₂⟩
  apply fresh_transitions_exclude_stable_ABA abaTrace h₁ h₂
  · intro h
    have hc := congrFun h (1 : Fin 2)
    norm_num [abaTrace, requiredEpochs, earlyEpochs] at hc
  · intro h
    have hc := congrFun h (1 : Fin 2)
    norm_num [abaTrace, requiredEpochs, earlyEpochs] at hc
  · rfl

/-! Content-address alternative to monotone versions. -/

def CollisionFree {Data Digest : Type*} (digest : Data → Digest) : Prop :=
  Function.Injective digest

theorem equal_digest_identifies_state {Data Digest : Type*}
    (digest : Data → Digest) (hcf : CollisionFree digest) {a b : Data}
    (h : digest a = digest b) : a = b :=
  hcf h

structure ContentBoundSnapshot (Digest : Type*) where
  sampledEpochs : TwoEpochs
  sampledDigest : Digest

def SnapshotDigestConsistent {Digest : Type*} (digest : TwoEpochs → Digest)
    (s : ContentBoundSnapshot Digest) : Prop :=
  s.sampledDigest = digest s.sampledEpochs

theorem equal_content_address_binds_epoch_vector {Digest : Type*}
    (digest : TwoEpochs → Digest) (hcf : CollisionFree digest)
    (a b : ContentBoundSnapshot Digest)
    (ha : SnapshotDigestConsistent digest a)
    (hb : SnapshotDigestConsistent digest b)
    (heq : a.sampledDigest = b.sampledDigest) :
    a.sampledEpochs = b.sampledEpochs := by
  apply hcf
  rw [← ha, ← hb]
  exact heq

/-- Exact fixture digest; it represents content itself, not a finite hash claim. -/
def exactEpochDigest : TwoEpochs → TwoEpochs := id

theorem exact_epoch_digest_collision_free : CollisionFree exactEpochDigest := by
  intro a b h
  exact h

def constantDigest (_ : TwoEpochs) : Unit := ()

theorem constant_digest_matches_distinct_states :
    constantDigest requiredEpochs = constantDigest earlyEpochs ∧
      requiredEpochs ≠ earlyEpochs := by
  constructor
  · rfl
  · intro h
    have hc := congrFun h (1 : Fin 2)
    norm_num [requiredEpochs, earlyEpochs] at hc

theorem equal_hash_without_collision_evidence_is_insufficient :
    ¬ CollisionFree constantDigest := by
  intro h
  exact constant_digest_matches_distinct_states.2
    (h constant_digest_matches_distinct_states.1)

/-! Bounded collision audits are not mathematical collision freedom. -/

/-- The digest distinguishes inputs only inside the explicitly audited domain. -/
def CollisionFreeOn {Data Digest : Type*} (audited : Set Data)
    (digest : Data → Digest) : Prop :=
  ∀ ⦃a b⦄, a ∈ audited → b ∈ audited → digest a = digest b → a = b

def threeToBoolDigest : Fin 3 → Bool
  | 0 => false
  | _ => true

def auditedPair : Set (Fin 3) := {0, 1}

theorem threeToBool_collision_free_on_audited_pair :
    CollisionFreeOn auditedPair threeToBoolDigest := by
  intro a b ha hb hd
  simp only [auditedPair, Set.mem_insert_iff, Set.mem_singleton_iff] at ha hb
  rcases ha with rfl | rfl <;> rcases hb with rfl | rfl
  · rfl
  · simp [threeToBoolDigest] at hd
  · simp [threeToBoolDigest] at hd
  · rfl

theorem threeToBool_has_unaudited_collision :
    threeToBoolDigest (1 : Fin 3) = threeToBoolDigest (2 : Fin 3) ∧
      (1 : Fin 3) ≠ 2 := by
  decide

theorem bounded_collision_audit_does_not_imply_collision_free :
    CollisionFreeOn auditedPair threeToBoolDigest ∧
      ¬ CollisionFree threeToBoolDigest := by
  refine ⟨threeToBool_collision_free_on_audited_pair, ?_⟩
  intro h
  exact threeToBool_has_unaudited_collision.2
    (h threeToBool_has_unaudited_collision.1)

end LinearConsumption

end MariciFormal.TemporalAuthority
