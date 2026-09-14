{-# OPTIONS --safe --cubical --guardedness #-}
module RHPhysicalRecollementRealization where

open import Cubical.Foundations.Prelude
open import RHThirdOrderRelativeEndpointPacket
open import RHReciprocalChartDeterminantCarrier
open import RHThetaBoundaryConservation
open import RHSectionBoundaryReadout

-- Physical realization is stronger than an abstract cubical filler.  It
-- supplies a source current, independently typed open and closed images, and
-- the Beck--Chevalley path identifying them in the common determinant line.
record PhysicalRecollementRealization {ℓ : Level}
  {R : ThirdOrderRelativeEndpoint {ℓ}}
  (C : ReciprocalChartCarrier R)
  (G : UnsewnGreenProblem {ℓ})
  (S : DistinguishedThetaSection C) : Type (ℓ-suc ℓ) where
  field
    PhysicalCurrent : Type ℓ
    distinguishedCurrent : DistinguishedThetaSection.Parameter S → PhysicalCurrent

    openImage closedImage : PhysicalCurrent → commonLine C
    beckChevalley : (j : PhysicalCurrent) → openImage j ≡ closedImage j

    zeroCurrent : PhysicalCurrent
    zeroLine : commonLine C
    closedZero : closedImage zeroCurrent ≡ zeroLine

    boundaryReadout : commonLine C → Scalar G
    readoutPreservesZero : boundaryReadout zeroLine ≡ zero G

    sectionIsOpenImage :
      (s : DistinguishedThetaSection.Parameter S) →
      DistinguishedThetaSection.section S s ≡
      openImage (distinguishedCurrent s)

    workIsClosedReadout :
      (s : DistinguishedThetaSection.Parameter S) →
      work G ≡ boundaryReadout (closedImage (distinguishedCurrent s))

open PhysicalRecollementRealization public

-- The source-derived recollement square supplies exactly the independent
-- readout interface required by the existing RH conservation theorem.
physicalRealizationGivesReadout : {ℓ : Level}
  {R : ThirdOrderRelativeEndpoint {ℓ}}
  (C : ReciprocalChartCarrier R)
  (G : UnsewnGreenProblem {ℓ})
  (S : DistinguishedThetaSection C) →
  PhysicalRecollementRealization C G S →
  SectionBoundaryReadout C G S
physicalRealizationGivesReadout C G S P = record
  { zeroLine = zeroLine P
  ; boundaryReadout = boundaryReadout P
  ; readoutPreservesZero = readoutPreservesZero P
  ; workIdentification = λ s →
      workIsClosedReadout P s ∙
      cong (boundaryReadout P) (sym (beckChevalley P (distinguishedCurrent P s))) ∙
      cong (boundaryReadout P) (sym (sectionIsOpenImage P s))
  }

-- Consequently a physical recollement realization discharges the sole
-- RH-bearing boundary-conservation field without identifying a path with a
-- propagator or assuming that a formal filler is physical.
physicalRealizationGivesBoundaryConservation : {ℓ : Level}
  {R : ThirdOrderRelativeEndpoint {ℓ}}
  (C : ReciprocalChartCarrier R)
  (G : UnsewnGreenProblem {ℓ})
  (S : DistinguishedThetaSection C)
  (P : PhysicalRecollementRealization C G S)
  (s : DistinguishedThetaSection.Parameter S) →
  ThetaBoundaryConservation C G
physicalRealizationGivesBoundaryConservation C G S P s =
  readoutGivesBoundaryConservation C G S
    (physicalRealizationGivesReadout C G S P) s

physicalRealizationThetaZeroImpliesTransverseZero : {ℓ : Level}
  {R : ThirdOrderRelativeEndpoint {ℓ}}
  (C : ReciprocalChartCarrier R)
  (G : UnsewnGreenProblem {ℓ})
  (S : DistinguishedThetaSection C)
  (P : PhysicalRecollementRealization C G S)
  (s : DistinguishedThetaSection.Parameter S) →
  DistinguishedThetaSection.section S s ≡ zeroLine P →
  transverse G ≡ zero G
physicalRealizationThetaZeroImpliesTransverseZero C G S P s vanishes =
  thetaZeroImpliesTransverseZero C G
    (physicalRealizationGivesBoundaryConservation C G S P s)
    vanishes
