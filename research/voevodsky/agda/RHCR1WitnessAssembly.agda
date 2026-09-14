{-# OPTIONS --safe --cubical --guardedness #-}
module RHCR1WitnessAssembly where

open import Cubical.Foundations.Prelude
open import RHThirdOrderRelativeEndpointPacket
open import RHReciprocalChartDeterminantCarrier
open import RHThetaBoundaryConservation
open import RHPhysicalRecollementRealization
open import RHCR1PromotionBoundary
import RHSectionBoundaryReadout as SBR

-- Geometric proper base change supplies the support-sensitive part of the
-- physical witness.  It does not define the analytic boundary readout.
record CR1SupportWitness {ℓ : Level}
  {R : ThirdOrderRelativeEndpoint {ℓ}}
  (C : ReciprocalChartCarrier R)
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
    sectionComparison :
      (s : DistinguishedThetaSection.Parameter S) →
      DistinguishedThetaSection.section S s ≡
      openPhysical (distinguishedCarrier s)

open CR1SupportWitness public

-- The analytic/physical readout is separately sourced.  This prevents a
-- support comparison from manufacturing a scalar observable.
record CR1ReadoutWitness {ℓ : Level}
  {R : ThirdOrderRelativeEndpoint {ℓ}}
  (C : ReciprocalChartCarrier R)
  (G : UnsewnGreenProblem {ℓ}) : Type (ℓ-suc ℓ) where
  field
    boundaryReadout : commonLine C → Scalar G
    zeroLine : commonLine C
    readoutPreservesZero : boundaryReadout zeroLine ≡ zero G

open CR1ReadoutWitness public

-- The final mate identifies the independently defined Green work with the
-- readout of the closed physical image.
record CR1WorkMate {ℓ : Level}
  {R : ThirdOrderRelativeEndpoint {ℓ}}
  (C : ReciprocalChartCarrier R)
  (G : UnsewnGreenProblem {ℓ})
  (S : DistinguishedThetaSection C)
  (F : FiniteCR1Carrier {ℓ})
  (P : CR1SupportWitness C S F)
  (B : CR1ReadoutWitness C G) : Type (ℓ-suc ℓ) where
  field
    zeroLinesAgree : physicalZeroLine P ≡ zeroLine B
    workComparison :
      (s : DistinguishedThetaSection.Parameter S) →
      work G ≡ boundaryReadout B (closedPhysical P (distinguishedCarrier P s))

open CR1WorkMate public

-- The previously isolated section readout supplies both analytic CR1 pieces.
-- Only agreement of its independently chosen zero line with the support zero
-- remains explicit; the work mate then follows from section comparison and
-- proper base change rather than being postulated a second time.
sectionReadoutToCR1Readout : {ℓ : Level}
  {R : ThirdOrderRelativeEndpoint {ℓ}}
  (C : ReciprocalChartCarrier R)
  (G : UnsewnGreenProblem {ℓ})
  (S : DistinguishedThetaSection C) →
  SBR.SectionBoundaryReadout C G S →
  CR1ReadoutWitness C G
sectionReadoutToCR1Readout C G S B = record
  { boundaryReadout = SBR.boundaryReadout B
  ; zeroLine = SBR.zeroLine B
  ; readoutPreservesZero = SBR.readoutPreservesZero B
  }

sectionReadoutToCR1WorkMate : {ℓ : Level}
  {R : ThirdOrderRelativeEndpoint {ℓ}}
  (C : ReciprocalChartCarrier R)
  (G : UnsewnGreenProblem {ℓ})
  (S : DistinguishedThetaSection C)
  (F : FiniteCR1Carrier {ℓ})
  (P : CR1SupportWitness C S F)
  (B : SBR.SectionBoundaryReadout C G S)
  (zeroAgreement : physicalZeroLine P ≡ SBR.zeroLine B) →
  CR1WorkMate C G S F P (sectionReadoutToCR1Readout C G S B)
sectionReadoutToCR1WorkMate C G S F P B zeroAgreement = record
  { zeroLinesAgree = zeroAgreement
  ; workComparison = λ s →
      SBR.workIdentification B s ∙
      cong (SBR.boundaryReadout B) (sectionComparison P s) ∙
      cong (SBR.boundaryReadout B)
        (properBaseChange P (distinguishedCarrier P s))
  }

-- The reduced source package is the single concrete inhabitation target left
-- to CR1 geometry and analysis.  It records no opaque promotion token.
record CR1PhysicalSourcePackage {ℓ : Level}
  {R : ThirdOrderRelativeEndpoint {ℓ}}
  (C : ReciprocalChartCarrier R)
  (G : UnsewnGreenProblem {ℓ})
  (S : DistinguishedThetaSection C)
  (F : FiniteCR1Carrier {ℓ}) : Type (ℓ-suc ℓ) where
  field
    support : CR1SupportWitness C S F
    sectionReadout : SBR.SectionBoundaryReadout C G S
    zeroAgreement :
      physicalZeroLine support ≡ SBR.zeroLine sectionReadout

open CR1PhysicalSourcePackage public

-- The three independently auditable interfaces assemble the exact authority
-- consumed by RHCR1PromotionBoundary.
assembleCR1ProperBaseChangeWitness : {ℓ : Level}
  {R : ThirdOrderRelativeEndpoint {ℓ}}
  (C : ReciprocalChartCarrier R)
  (G : UnsewnGreenProblem {ℓ})
  (S : DistinguishedThetaSection C)
  (F : FiniteCR1Carrier {ℓ})
  (P : CR1SupportWitness C S F)
  (B : CR1ReadoutWitness C G)
  (M : CR1WorkMate C G S F P B) →
  CR1ProperBaseChangeWitness C G S F
assembleCR1ProperBaseChangeWitness C G S F P B M = record
  { distinguishedCarrier = distinguishedCarrier P
  ; zeroCarrier = zeroCarrier P
  ; openPhysical = openPhysical P
  ; closedPhysical = closedPhysical P
  ; properBaseChange = properBaseChange P
  ; physicalZeroLine = zeroLine B
  ; closedZero = closedZero P ∙ zeroLinesAgree M
  ; physicalReadout = boundaryReadout B
  ; physicalReadoutZero = readoutPreservesZero B
  ; sectionComparison = sectionComparison P
  ; workComparison = workComparison M
  }

-- End-to-end RH theorem from the three separately auditable witnesses.
assembledCR1GivesBoundaryConservation : {ℓ : Level}
  {R : ThirdOrderRelativeEndpoint {ℓ}}
  (C : ReciprocalChartCarrier R)
  (G : UnsewnGreenProblem {ℓ})
  (S : DistinguishedThetaSection C)
  (F : FiniteCR1Carrier {ℓ})
  (P : CR1SupportWitness C S F)
  (B : CR1ReadoutWitness C G)
  (M : CR1WorkMate C G S F P B)
  (s : DistinguishedThetaSection.Parameter S) →
  ThetaBoundaryConservation C G
assembledCR1GivesBoundaryConservation C G S F P B M s =
  physicalRealizationGivesBoundaryConservation C G S
    (properBaseChangeWitnessGivesPhysicalRealization C G S F
      (assembleCR1ProperBaseChangeWitness C G S F P B M)) s

assembledCR1ThetaZeroImpliesTransverseZero : {ℓ : Level}
  {R : ThirdOrderRelativeEndpoint {ℓ}}
  (C : ReciprocalChartCarrier R)
  (G : UnsewnGreenProblem {ℓ})
  (S : DistinguishedThetaSection C)
  (F : FiniteCR1Carrier {ℓ})
  (P : CR1SupportWitness C S F)
  (B : CR1ReadoutWitness C G)
  (M : CR1WorkMate C G S F P B)
  (s : DistinguishedThetaSection.Parameter S) →
  DistinguishedThetaSection.section S s ≡ zeroLine B →
  transverse G ≡ zero G
assembledCR1ThetaZeroImpliesTransverseZero C G S F P B M s vanishes =
  thetaZeroImpliesTransverseZero C G
    (assembledCR1GivesBoundaryConservation C G S F P B M s)
    vanishes

physicalSourcePackageGivesProperBaseChangeWitness : {ℓ : Level}
  {R : ThirdOrderRelativeEndpoint {ℓ}}
  (C : ReciprocalChartCarrier R)
  (G : UnsewnGreenProblem {ℓ})
  (S : DistinguishedThetaSection C)
  (F : FiniteCR1Carrier {ℓ}) →
  CR1PhysicalSourcePackage C G S F →
  CR1ProperBaseChangeWitness C G S F
physicalSourcePackageGivesProperBaseChangeWitness C G S F K =
  assembleCR1ProperBaseChangeWitness C G S F
    (support K)
    (sectionReadoutToCR1Readout C G S (sectionReadout K))
    (sectionReadoutToCR1WorkMate C G S F (support K)
      (sectionReadout K) (zeroAgreement K))

physicalSourcePackageGivesPhysicalRealization : {ℓ : Level}
  {R : ThirdOrderRelativeEndpoint {ℓ}}
  (C : ReciprocalChartCarrier R)
  (G : UnsewnGreenProblem {ℓ})
  (S : DistinguishedThetaSection C)
  (F : FiniteCR1Carrier {ℓ}) →
  CR1PhysicalSourcePackage C G S F →
  PhysicalRecollementRealization C G S
physicalSourcePackageGivesPhysicalRealization C G S F K =
  properBaseChangeWitnessGivesPhysicalRealization C G S F
    (physicalSourcePackageGivesProperBaseChangeWitness C G S F K)

physicalSourcePackageGivesBoundaryConservation : {ℓ : Level}
  {R : ThirdOrderRelativeEndpoint {ℓ}}
  (C : ReciprocalChartCarrier R)
  (G : UnsewnGreenProblem {ℓ})
  (S : DistinguishedThetaSection C)
  (F : FiniteCR1Carrier {ℓ})
  (K : CR1PhysicalSourcePackage C G S F)
  (s : DistinguishedThetaSection.Parameter S) →
  ThetaBoundaryConservation C G
physicalSourcePackageGivesBoundaryConservation C G S F K s =
  physicalRealizationGivesBoundaryConservation C G S
    (physicalSourcePackageGivesPhysicalRealization C G S F K) s

physicalSourcePackageThetaZeroImpliesTransverseZero : {ℓ : Level}
  {R : ThirdOrderRelativeEndpoint {ℓ}}
  (C : ReciprocalChartCarrier R)
  (G : UnsewnGreenProblem {ℓ})
  (S : DistinguishedThetaSection C)
  (F : FiniteCR1Carrier {ℓ})
  (K : CR1PhysicalSourcePackage C G S F)
  (s : DistinguishedThetaSection.Parameter S) →
  DistinguishedThetaSection.section S s ≡
    SBR.zeroLine (sectionReadout K) →
  transverse G ≡ zero G
physicalSourcePackageThetaZeroImpliesTransverseZero C G S F K s vanishes =
  thetaZeroImpliesTransverseZero C G
    (physicalSourcePackageGivesBoundaryConservation C G S F K s)
    vanishes

-- Reduced end-to-end interface: a source section readout already contains the
-- analytic work mate.  Thus users need not separately inhabit CR1ReadoutWitness
-- and CR1WorkMate.
sectionReadoutAndSupportGiveBoundaryConservation : {ℓ : Level}
  {R : ThirdOrderRelativeEndpoint {ℓ}}
  (C : ReciprocalChartCarrier R)
  (G : UnsewnGreenProblem {ℓ})
  (S : DistinguishedThetaSection C)
  (F : FiniteCR1Carrier {ℓ})
  (P : CR1SupportWitness C S F)
  (B : SBR.SectionBoundaryReadout C G S)
  (zeroAgreement : physicalZeroLine P ≡ SBR.zeroLine B)
  (s : DistinguishedThetaSection.Parameter S) →
  ThetaBoundaryConservation C G
sectionReadoutAndSupportGiveBoundaryConservation C G S F P B zeroAgreement s =
  assembledCR1GivesBoundaryConservation C G S F P
    (sectionReadoutToCR1Readout C G S B)
    (sectionReadoutToCR1WorkMate C G S F P B zeroAgreement)
    s

sectionReadoutAndSupportThetaZeroImpliesTransverseZero : {ℓ : Level}
  {R : ThirdOrderRelativeEndpoint {ℓ}}
  (C : ReciprocalChartCarrier R)
  (G : UnsewnGreenProblem {ℓ})
  (S : DistinguishedThetaSection C)
  (F : FiniteCR1Carrier {ℓ})
  (P : CR1SupportWitness C S F)
  (B : SBR.SectionBoundaryReadout C G S)
  (zeroAgreement : physicalZeroLine P ≡ SBR.zeroLine B)
  (s : DistinguishedThetaSection.Parameter S) →
  DistinguishedThetaSection.section S s ≡ SBR.zeroLine B →
  transverse G ≡ zero G
sectionReadoutAndSupportThetaZeroImpliesTransverseZero
  C G S F P B zeroAgreement s vanishes =
  thetaZeroImpliesTransverseZero C G
    (sectionReadoutAndSupportGiveBoundaryConservation
      C G S F P B zeroAgreement s)
    vanishes
