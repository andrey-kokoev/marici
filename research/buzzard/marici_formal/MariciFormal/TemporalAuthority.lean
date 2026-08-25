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

end MariciFormal.TemporalAuthority
