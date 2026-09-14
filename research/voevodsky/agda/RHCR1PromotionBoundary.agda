{-# OPTIONS --safe --cubical --guardedness #-}
module RHCR1PromotionBoundary where

open import Cubical.Foundations.Prelude
open import Cubical.Data.Empty using (⊥; rec)
open import RHThirdOrderRelativeEndpointPacket
open import RHReciprocalChartDeterminantCarrier
open import RHThetaBoundaryConservation
open import RHPhysicalRecollementRealization

-- The finite Rees--Cech calculations provide a coherent carrier diagram.  Its
-- cells and paths are retained here without identifying them with physical
-- currents or extraordinary images.
record FiniteCR1Carrier {ℓ : Level} : Type (ℓ-suc ℓ) where
  field
    Carrier OpenFace ClosedFace Overlap : Type ℓ
    openRestriction : Carrier → OpenFace
    closedRestriction : Carrier → ClosedFace
    openToOverlap : OpenFace → Overlap
    closedToOverlap : ClosedFace → Overlap
    finiteBeckChevalley :
      (x : Carrier) →
      openToOverlap (openRestriction x) ≡
      closedToOverlap (closedRestriction x)

    rotate reflect : Carrier → Carrier
    reflectOverlap : Overlap → Overlap
    rotate³ : (x : Carrier) → rotate (rotate (rotate x)) ≡ x
    reflect² : (x : Carrier) → reflect (reflect x) ≡ x
    reflectionOpen :
      (x : Carrier) →
      openToOverlap (openRestriction (reflect x)) ≡
      reflectOverlap (openToOverlap (openRestriction x))
    reflectionClosed :
      (x : Carrier) →
      closedToOverlap (closedRestriction (reflect x)) ≡
      reflectOverlap (closedToOverlap (closedRestriction x))

open FiniteCR1Carrier public

-- The exact non-circular authority required from geometry.  It maps the
-- finite carrier into the determinant line on both supports and identifies
-- the distinguished source section and Green boundary work with those maps.
record CR1ProperBaseChangeWitness {ℓ : Level}
  {R : ThirdOrderRelativeEndpoint {ℓ}}
  (C : ReciprocalChartCarrier R)
  (G : UnsewnGreenProblem {ℓ})
  (S : DistinguishedThetaSection C)
  (F : FiniteCR1Carrier {ℓ}) : Type (ℓ-suc ℓ) where
  field
    distinguishedCarrier : DistinguishedThetaSection.Parameter S → Carrier F
    zeroCarrier : Carrier F
    openPhysical closedPhysical : Carrier F → commonLine C
    properBaseChange :
      (x : Carrier F) → openPhysical x ≡ closedPhysical x
    physicalZeroLine : commonLine C
    closedZero : closedPhysical zeroCarrier ≡ physicalZeroLine
    physicalReadout : commonLine C → Scalar G
    physicalReadoutZero : physicalReadout physicalZeroLine ≡ zero G
    sectionComparison :
      (s : DistinguishedThetaSection.Parameter S) →
      DistinguishedThetaSection.section S s ≡
      openPhysical (distinguishedCarrier s)
    workComparison :
      (s : DistinguishedThetaSection.Parameter S) →
      work G ≡ physicalReadout (closedPhysical (distinguishedCarrier s))

open CR1ProperBaseChangeWitness public

properBaseChangeWitnessGivesPhysicalRealization : {ℓ : Level}
  {R : ThirdOrderRelativeEndpoint {ℓ}}
  (C : ReciprocalChartCarrier R)
  (G : UnsewnGreenProblem {ℓ})
  (S : DistinguishedThetaSection C)
  (F : FiniteCR1Carrier {ℓ}) →
  CR1ProperBaseChangeWitness C G S F →
  PhysicalRecollementRealization C G S
properBaseChangeWitnessGivesPhysicalRealization C G S F W = record
  { PhysicalCurrent = Carrier F
  ; distinguishedCurrent = distinguishedCarrier W
  ; openImage = openPhysical W
  ; closedImage = closedPhysical W
  ; beckChevalley = properBaseChange W
  ; zeroCurrent = zeroCarrier W
  ; zeroLine = physicalZeroLine W
  ; closedZero = closedZero W
  ; boundaryReadout = physicalReadout W
  ; readoutPreservesZero = physicalReadoutZero W
  ; sectionIsOpenImage = sectionComparison W
  ; workIsClosedReadout = workComparison W
  }

-- Proper base change is an authority-bearing promotion, not a theorem of the
-- finite carrier.  In particular, this module exports no witness constructor
-- from finiteBeckChevalley alone.
record CR1ProperBaseChangePromotion {ℓ : Level}
  {R : ThirdOrderRelativeEndpoint {ℓ}}
  (C : ReciprocalChartCarrier R)
  (G : UnsewnGreenProblem {ℓ})
  (S : DistinguishedThetaSection C)
  (F : FiniteCR1Carrier {ℓ}) : Type (ℓ-suc (ℓ-suc ℓ)) where
  field
    Authority : Type (ℓ-suc ℓ)
    realize : Authority → PhysicalRecollementRealization C G S
    carrierCurrent : (authority : Authority) → Carrier F →
      PhysicalRecollementRealization.PhysicalCurrent (realize authority)

open CR1ProperBaseChangePromotion public

-- Canonical promotion once, and only once, the geometric witness is supplied.
properBaseChangePromotion : {ℓ : Level}
  {R : ThirdOrderRelativeEndpoint {ℓ}}
  (C : ReciprocalChartCarrier R)
  (G : UnsewnGreenProblem {ℓ})
  (S : DistinguishedThetaSection C)
  (F : FiniteCR1Carrier {ℓ}) →
  CR1ProperBaseChangePromotion C G S F
properBaseChangePromotion C G S F = record
  { Authority = CR1ProperBaseChangeWitness C G S F
  ; realize = properBaseChangeWitnessGivesPhysicalRealization C G S F
  ; carrierCurrent = λ authority x → x
  }

-- The current repository state can be represented without postulates: its
-- promotion authority is empty.  Ex falso clauses make the target types
-- explicit but provide no physical current.
closedCR1Promotion : {ℓ : Level}
  {R : ThirdOrderRelativeEndpoint {ℓ}}
  (C : ReciprocalChartCarrier R)
  (G : UnsewnGreenProblem {ℓ})
  (S : DistinguishedThetaSection C)
  (F : FiniteCR1Carrier {ℓ}) →
  CR1ProperBaseChangePromotion C G S F
closedCR1Promotion C G S F = record
  { Authority = Lift ⊥
  ; realize = λ impossible → rec (lower impossible)
  ; carrierCurrent = λ impossible → rec (lower impossible)
  }

closedCR1HasNoAuthority : {ℓ : Level}
  {R : ThirdOrderRelativeEndpoint {ℓ}}
  (C : ReciprocalChartCarrier R)
  (G : UnsewnGreenProblem {ℓ})
  (S : DistinguishedThetaSection C)
  (F : FiniteCR1Carrier {ℓ}) →
  Authority (closedCR1Promotion C G S F) → ⊥
closedCR1HasNoAuthority C G S F authority = lower authority

-- Once the external proper-base-change authority is supplied, the existing
-- RH theorem follows.  No finite incidence path is silently promoted.
authorizedCR1GivesBoundaryConservation : {ℓ : Level}
  {R : ThirdOrderRelativeEndpoint {ℓ}}
  (C : ReciprocalChartCarrier R)
  (G : UnsewnGreenProblem {ℓ})
  (S : DistinguishedThetaSection C)
  (F : FiniteCR1Carrier {ℓ})
  (P : CR1ProperBaseChangePromotion C G S F) →
  Authority P →
  (s : DistinguishedThetaSection.Parameter S) →
  ThetaBoundaryConservation C G
authorizedCR1GivesBoundaryConservation C G S F P authority s =
  physicalRealizationGivesBoundaryConservation C G S
    (realize P authority) s
