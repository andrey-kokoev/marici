{-# OPTIONS --safe --cubical --guardedness #-}
module RHPrimeShellResidualBoundary where

open import Cubical.Foundations.Prelude
open import RHThirdOrderRelativeEndpointPacket
open import RHReciprocalChartDeterminantCarrier
open import RHThetaBoundaryConservation
open import RHCR1PromotionBoundary
open import RHCR1WitnessAssembly
import RHSectionBoundaryReadout as SBR

-- The singleton G4 hypothesis, kept separate from the already constructed
-- CR1 support geometry.  Shell and Jet encode consecutive-prime coordinates
-- and multiplicity derivatives; commonResidual is the limiting common mode.
record PrimeShellResidualFamily {ℓ : Level}
  {R : ThirdOrderRelativeEndpoint {ℓ}}
  (C : ReciprocalChartCarrier R)
  (G : UnsewnGreenProblem {ℓ})
  (S : DistinguishedThetaSection C) : Type (ℓ-suc ℓ) where
  field
    Shell Jet : Type ℓ
    Residual : Type ℓ
    zeroResidual : Residual

    shellResidual :
      DistinguishedThetaSection.Parameter S → Shell → Jet → Residual
    commonResidual :
      DistinguishedThetaSection.Parameter S → Jet → Residual

    shellResidualVanishes :
      (s : DistinguishedThetaSection.Parameter S)
      (p : Shell) (j : Jet) →
      shellResidual s p j ≡ zeroResidual
    commonResidualVanishes :
      (s : DistinguishedThetaSection.Parameter S) (j : Jet) →
      commonResidual s j ≡ zeroResidual

    zeroLine : commonLine C
    responseReadout : commonLine C → Scalar G
    responseZero : responseReadout zeroLine ≡ zero G

    -- This is the source-normalized shell Green totalization theorem: the
    -- vector residual family, not scalar Xi symmetry, identifies Green work.
    residualTotalization :
      (s : DistinguishedThetaSection.Parameter S) →
      work G ≡ responseReadout (DistinguishedThetaSection.section S s)

open PrimeShellResidualFamily public

primeShellResidualsGiveSectionReadout : {ℓ : Level}
  {R : ThirdOrderRelativeEndpoint {ℓ}}
  (C : ReciprocalChartCarrier R)
  (G : UnsewnGreenProblem {ℓ})
  (S : DistinguishedThetaSection C) →
  PrimeShellResidualFamily C G S →
  SBR.SectionBoundaryReadout C G S
primeShellResidualsGiveSectionReadout C G S P = record
  { zeroLine = zeroLine P
  ; boundaryReadout = responseReadout P
  ; readoutPreservesZero = responseZero P
  ; workIdentification = residualTotalization P
  }

primeShellResidualsAndSupportGivePhysicalSource : {ℓ : Level}
  {R : ThirdOrderRelativeEndpoint {ℓ}}
  (C : ReciprocalChartCarrier R)
  (G : UnsewnGreenProblem {ℓ})
  (S : DistinguishedThetaSection C)
  (F : FiniteCR1Carrier {ℓ})
  (P : CR1SupportWitness C S F)
  (A : PrimeShellResidualFamily C G S)
  (zeroAgreement : physicalZeroLine P ≡ zeroLine A) →
  CR1PhysicalSourcePackage C G S F
primeShellResidualsAndSupportGivePhysicalSource C G S F P A agree = record
  { support = P
  ; sectionReadout = primeShellResidualsGiveSectionReadout C G S A
  ; zeroAgreement = agree
  }

primeShellResidualsGiveConfinement : {ℓ : Level}
  {R : ThirdOrderRelativeEndpoint {ℓ}}
  (C : ReciprocalChartCarrier R)
  (G : UnsewnGreenProblem {ℓ})
  (S : DistinguishedThetaSection C)
  (F : FiniteCR1Carrier {ℓ})
  (P : CR1SupportWitness C S F)
  (A : PrimeShellResidualFamily C G S)
  (zeroAgreement : physicalZeroLine P ≡ zeroLine A)
  (s : DistinguishedThetaSection.Parameter S) →
  DistinguishedThetaSection.section S s ≡ zeroLine A →
  transverse G ≡ zero G
primeShellResidualsGiveConfinement C G S F P A agree s vanishes =
  physicalSourcePackageThetaZeroImpliesTransverseZero C G S F
    (primeShellResidualsAndSupportGivePhysicalSource C G S F P A agree)
    s vanishes
