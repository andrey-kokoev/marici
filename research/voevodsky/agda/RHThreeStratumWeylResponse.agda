{-# OPTIONS --safe --cubical --guardedness #-}
module RHThreeStratumWeylResponse where

open import Cubical.Foundations.Prelude
open import RHThirdOrderRelativeEndpointPacket
open import RHReciprocalChartDeterminantCarrier
open import RHThetaBoundaryConservation
open import RHSectionBoundaryReadout

-- Boundary-triplet factorization of the missing readout.  The three response
-- strata remain distinct; BoundaryState is their source-authorized
-- totalization, not an untyped scalar direct sum.
record ThreeStratumWeylResponse {ℓ : Level}
  {R : ThirdOrderRelativeEndpoint {ℓ}}
  (C : ReciprocalChartCarrier R)
  (G : UnsewnGreenProblem {ℓ})
  (S : DistinguishedThetaSection C) : Type (ℓ-suc ℓ) where
  field
    PrimitiveBoundary SquareBoundary ConnectedBoundary : Type ℓ
    BoundaryState BulkSolution : Type ℓ

    primitiveTrace : PrimitiveBoundary → BoundaryState
    squareTrace : SquareBoundary → BoundaryState
    connectedTrace : ConnectedBoundary → BoundaryState

    zeroCommonLine : commonLine C
    zeroBoundaryState : BoundaryState
    zeroBulkSolution : BulkSolution

    gammaField : BoundaryState → BulkSolution
    sourceBoundaryTrace : commonLine C → BoundaryState
    neumannResponse : BulkSolution → Scalar G

    tracePreservesZero :
      sourceBoundaryTrace zeroCommonLine ≡ zeroBoundaryState
    gammaPreservesZero :
      gammaField zeroBoundaryState ≡ zeroBulkSolution
    responsePreservesZero :
      neumannResponse zeroBulkSolution ≡ zero G

    -- The source theorem still to be constructed: the full theta trace is in
    -- the gamma-field domain and its Weyl response is the Green work term.
    workIsWeylResponse :
      (s : DistinguishedThetaSection.Parameter S) →
      work G ≡
      neumannResponse
        (gammaField
          (sourceBoundaryTrace
            (DistinguishedThetaSection.section S s)))

open ThreeStratumWeylResponse public

threeStratumWeylGivesSectionReadout : {ℓ : Level}
  {R : ThirdOrderRelativeEndpoint {ℓ}}
  (C : ReciprocalChartCarrier R)
  (G : UnsewnGreenProblem {ℓ})
  (S : DistinguishedThetaSection C) →
  ThreeStratumWeylResponse C G S →
  SectionBoundaryReadout C G S
threeStratumWeylGivesSectionReadout C G S W = record
  { zeroLine = zeroCommonLine W
  ; boundaryReadout = λ x →
      neumannResponse W (gammaField W (sourceBoundaryTrace W x))
  ; readoutPreservesZero =
      cong (λ b → neumannResponse W (gammaField W b))
        (tracePreservesZero W) ∙
      cong (neumannResponse W) (gammaPreservesZero W) ∙
      responsePreservesZero W
  ; workIdentification = workIsWeylResponse W
  }
