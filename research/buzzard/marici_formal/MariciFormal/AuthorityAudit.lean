namespace MariciFormal.AuthorityAudit

/-!
A deliberately small audit vocabulary for proposed authority composition.
It does not assert a category: the available sector examples do not yet justify
one common domain-composition operation or an associativity law.
-/

inductive AuthorityKind where
  | algebraic | readout | selector | constructor | executor
  deriving DecidableEq, Repr

inductive Variance where
  | covariant | contravariant
  deriving DecidableEq, Repr

structure GrantSignature (Obj Domain : Type) where
  source : Obj
  target : Obj
  kind : AuthorityKind
  evidenceDomain : Domain
  variance : Variance

def PairwiseTyped {Obj Domain : Type} [DecidableEq Obj] [DecidableEq Domain]
    (g h : GrantSignature Obj Domain) : Prop :=
  g.target = h.source ∧
  g.kind = h.kind ∧
  g.evidenceDomain = h.evidenceDomain ∧
  g.variance = h.variance

/-- Non-strict composition is admitted only with an explicit zero-defect cell. -/
structure CompositionWitness {Obj Domain : Type} [DecidableEq Obj] [DecidableEq Domain]
    (g h : GrantSignature Obj Domain) where
  typed : PairwiseTyped g h
  coherenceDefect : Nat
  coherent : coherenceDefect = 0

theorem kind_is_preserved {Obj Domain : Type} [DecidableEq Obj] [DecidableEq Domain]
    {g h : GrantSignature Obj Domain} (w : CompositionWitness g h) :
    g.kind = h.kind :=
  w.typed.2.1

structure TripleAudit where
  leftPairAdmitted : Bool
  rightPairAdmitted : Bool
  tripleDefect : Nat

def PairwiseAdmitted (a : TripleAudit) : Prop :=
  a.leftPairAdmitted = true ∧ a.rightPairAdmitted = true

def TripleCoherent (a : TripleAudit) : Prop := a.tripleDefect = 0

/-- Strominger's hostile fixture: both adjacent pairs pass, but the triple cell fails. -/
def pairwiseValidTripleIncoherent : TripleAudit where
  leftPairAdmitted := true
  rightPairAdmitted := true
  tripleDefect := 1

theorem pairwise_does_not_supply_triple_coherence :
    PairwiseAdmitted pairwiseValidTripleIncoherent ∧
      ¬ TripleCoherent pairwiseValidTripleIncoherent := by
  simp [PairwiseAdmitted, TripleCoherent, pairwiseValidTripleIncoherent]

inductive SectorObject where
  | thetaLabels | thetaHalfLine | thetaDouble
  | kitaevLogical | kitaevFiveRail
  deriving DecidableEq, Repr

inductive SectorDomain where
  | thetaPositive | thetaDoubled
  | kitaevLogicalEvidence | kitaevPhysicalRails
  deriving DecidableEq, Repr

def thetaLabelsToHalf : GrantSignature SectorObject SectorDomain where
  source := .thetaLabels
  target := .thetaHalfLine
  kind := .readout
  evidenceDomain := .thetaPositive
  variance := .covariant

def thetaHalfToDouble : GrantSignature SectorObject SectorDomain where
  source := .thetaHalfLine
  target := .thetaDouble
  kind := .readout
  evidenceDomain := .thetaDoubled
  variance := .covariant

/-- The strict domain-equality interface rejects the real theta square.
The source says it composes only after domain extension and a moving-seam cell. -/
theorem theta_needs_domain_extension :
    ¬ PairwiseTyped thetaLabelsToHalf thetaHalfToDouble := by
  simp [PairwiseTyped, thetaLabelsToHalf, thetaHalfToDouble]

structure TransportAudit where
  endpointTyped : Bool
  authorityPreserved : Bool
  evidenceDomainMatched : Bool
  coherencePresent : Bool

def TransportAdmissible (a : TransportAudit) : Prop :=
  a.endpointTyped = true ∧ a.authorityPreserved = true ∧
  a.evidenceDomainMatched = true ∧ a.coherencePresent = true

/-- Kitaev hostile: logical capability does not authorize the five-rail lift. -/
def kitaevLogicalToFiveRail : TransportAudit where
  endpointTyped := true
  authorityPreserved := false
  evidenceDomainMatched := false
  coherencePresent := false

theorem kitaev_lift_is_not_admissible :
    ¬ TransportAdmissible kitaevLogicalToFiveRail := by
  simp [TransportAdmissible, kitaevLogicalToFiveRail]

end MariciFormal.AuthorityAudit
