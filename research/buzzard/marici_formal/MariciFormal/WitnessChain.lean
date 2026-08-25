import MariciFormal.CompletionAvailability

namespace MariciFormal.TemporalAuthority.LinearConsumption

/-! Typed delegation chains for completion-witness authority. -/

structure ChainGrant where
  issuer : String
  subject : String
  requestId : RequestId
  kind : AuthorityKind
  epoch : Nat
  validFrom : Nat
  validUntil : Nat
  intervalNonempty : validFrom < validUntil

def ChainLiveAt (grant : ChainGrant) (time : Nat) : Prop :=
  grant.validFrom ≤ time ∧ time < grant.validUntil

structure DelegationLink where
  parent : ChainGrant
  child : ChainGrant
  signatureValid : Bool

def LinkLocallyValid (link : DelegationLink) : Prop :=
  link.signatureValid = true ∧
    link.parent.subject = link.child.issuer ∧
    link.parent.requestId = link.child.requestId ∧
    link.parent.kind = link.child.kind ∧
    link.parent.epoch ≤ link.child.epoch ∧
    max link.parent.validFrom link.child.validFrom <
      min link.parent.validUntil link.child.validUntil

theorem locally_valid_link_preserves_authority_kind
    (link : DelegationLink) (h : LinkLocallyValid link) :
    link.parent.kind = link.child.kind :=
  h.2.2.2.1

structure RootCharter where
  issuer : String
  trusted : Bool
  allowedRequests : Finset RequestId

def EndToEndScope (charter : RootCharter) (root : ChainGrant) : Prop :=
  charter.trusted = true ∧ charter.issuer = root.issuer ∧
    root.requestId ∈ charter.allowedRequests

def CommonLiveTime (root middle leaf : ChainGrant) : Prop :=
  ∃ time, ChainLiveAt root time ∧ ChainLiveAt middle time ∧ ChainLiveAt leaf time

def EndToEndChainValid (charter : RootCharter)
    (first second : DelegationLink) : Prop :=
  LinkLocallyValid first ∧ LinkLocallyValid second ∧
    first.child = second.parent ∧ EndToEndScope charter first.parent ∧
    CommonLiveTime first.parent first.child second.child

def rootGrant : ChainGrant :=
  ⟨"root", "middle", 7, .readout, 1, 0, 4, by decide⟩

def middleGrant : ChainGrant :=
  ⟨"middle", "leaf", 7, .readout, 2, 3, 7, by decide⟩

def leafGrant : ChainGrant :=
  ⟨"leaf", "resource", 7, .readout, 3, 6, 10, by decide⟩

def firstLink : DelegationLink := ⟨rootGrant, middleGrant, true⟩
def secondLink : DelegationLink := ⟨middleGrant, leafGrant, true⟩

theorem both_links_are_locally_valid :
    LinkLocallyValid firstLink ∧ LinkLocallyValid secondLink := by
  norm_num [LinkLocallyValid, firstLink, secondLink, rootGrant,
    middleGrant, leafGrant]

theorem pairwise_live_overlap_does_not_supply_common_chain_time :
    ¬ CommonLiveTime rootGrant middleGrant leafGrant := by
  rintro ⟨time, hroot, hmiddle, hleaf⟩
  simp [ChainLiveAt, rootGrant, middleGrant, leafGrant] at hroot hmiddle hleaf
  omega

def scopeExcludingCharter : RootCharter :=
  ⟨"root", true, {8}⟩

theorem locally_valid_links_do_not_supply_root_scope :
    LinkLocallyValid firstLink ∧ LinkLocallyValid secondLink ∧
      ¬ EndToEndScope scopeExcludingCharter rootGrant := by
  refine ⟨both_links_are_locally_valid.1, both_links_are_locally_valid.2, ?_⟩
  simp [EndToEndScope, scopeExcludingCharter, rootGrant]

def scopeIncludingCharter : RootCharter :=
  ⟨"root", true, {7}⟩

theorem local_validity_and_root_scope_do_not_supply_temporal_coherence :
    LinkLocallyValid firstLink ∧ LinkLocallyValid secondLink ∧
      EndToEndScope scopeIncludingCharter rootGrant ∧
      ¬ EndToEndChainValid scopeIncludingCharter firstLink secondLink := by
  refine ⟨both_links_are_locally_valid.1, both_links_are_locally_valid.2,
    by simp [EndToEndScope, scopeIncludingCharter, rootGrant], ?_⟩
  intro h
  exact pairwise_live_overlap_does_not_supply_common_chain_time h.2.2.2.2

/-- A transported link retains its original kind, scope, epoch, and issuer data. -/
def transportDelegationLink (link : DelegationLink) : DelegationLink := link

theorem transport_does_not_repair_end_to_end_chain :
    ¬ EndToEndChainValid scopeIncludingCharter
      (transportDelegationLink firstLink) (transportDelegationLink secondLink) := by
  simpa [transportDelegationLink] using
    local_validity_and_root_scope_do_not_supply_temporal_coherence.2.2.2

end MariciFormal.TemporalAuthority.LinearConsumption
