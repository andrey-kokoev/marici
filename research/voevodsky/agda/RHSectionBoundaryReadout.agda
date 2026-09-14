{-# OPTIONS --safe --cubical --guardedness #-}
module RHSectionBoundaryReadout where

open import Cubical.Foundations.Prelude
open import RHThirdOrderRelativeEndpointPacket
open import RHReciprocalChartDeterminantCarrier
open import RHThetaBoundaryConservation

-- A source-derived readout from the distinguished section to boundary work is
-- stronger data than an implication declared only on its zero set.
record SectionBoundaryReadout {ℓ : Level}
  {R : ThirdOrderRelativeEndpoint {ℓ}}
  (C : ReciprocalChartCarrier R)
  (G : UnsewnGreenProblem {ℓ})
  (S : DistinguishedThetaSection C) : Type (ℓ-suc ℓ) where
  field
    zeroLine : commonLine C
    boundaryReadout : commonLine C → Scalar G
    readoutPreservesZero : boundaryReadout zeroLine ≡ zero G
    workIdentification :
      (s : DistinguishedThetaSection.Parameter S) →
      work G ≡ boundaryReadout (DistinguishedThetaSection.section S s)

open SectionBoundaryReadout public

-- The readout constructs the missing zero-to-work sewing law by ordinary
-- functoriality; no quotient by the zero set or fitted scalar ratio is used.
readoutZeroImpliesWorkSewing : {ℓ : Level}
  {R : ThirdOrderRelativeEndpoint {ℓ}}
  (C : ReciprocalChartCarrier R)
  (G : UnsewnGreenProblem {ℓ})
  (S : DistinguishedThetaSection C)
  (B : SectionBoundaryReadout C G S)
  (s : DistinguishedThetaSection.Parameter S) →
  DistinguishedThetaSection.section S s ≡ zeroLine B →
  work G ≡ zero G
readoutZeroImpliesWorkSewing C G S B s vanishes =
  workIdentification B s ∙
  cong (boundaryReadout B) vanishes ∙
  readoutPreservesZero B

-- Hence a readout supplies the abstract conservation interface used by the
-- confinement theorem.
readoutGivesBoundaryConservation : {ℓ : Level}
  {R : ThirdOrderRelativeEndpoint {ℓ}}
  (C : ReciprocalChartCarrier R)
  (G : UnsewnGreenProblem {ℓ})
  (S : DistinguishedThetaSection C)
  (B : SectionBoundaryReadout C G S)
  (s : DistinguishedThetaSection.Parameter S) →
  ThetaBoundaryConservation C G
readoutGivesBoundaryConservation C G S B s = record
  { thetaSection = S
  ; parameter = s
  ; sectionZero = λ x → x ≡ zeroLine B
  ; zeroImpliesWorkSewing = readoutZeroImpliesWorkSewing C G S B s
  }
