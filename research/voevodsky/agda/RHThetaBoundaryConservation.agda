{-# OPTIONS --safe --cubical --guardedness #-}
module RHThetaBoundaryConservation where

open import Cubical.Foundations.Prelude
open import RHThirdOrderRelativeEndpointPacket
open import RHReciprocalChartDeterminantCarrier

-- Green data before the missing boundary sewing law is imposed.
record UnsewnGreenProblem {ℓ : Level} : Type (ℓ-suc ℓ) where
  field
    Scalar : Type ℓ
    zero : Scalar
    _+_ _*_ : Scalar → Scalar → Scalar
    addZeroRight : (x : Scalar) → x + zero ≡ x
    transverse bulk work : Scalar
    greenIdentity : _+_ (_*_ transverse bulk) work ≡ zero
    positiveBulkCancels : _*_ transverse bulk ≡ zero → transverse ≡ zero

open UnsewnGreenProblem public

-- The distinguished section and its zero predicate remain separate from the
-- nowhere-zero carrier.  The sole RH-bearing field is zeroImpliesWorkSewing.
record ThetaBoundaryConservation {ℓ : Level}
  {R : ThirdOrderRelativeEndpoint {ℓ}}
  (C : ReciprocalChartCarrier R)
  (G : UnsewnGreenProblem {ℓ}) : Type (ℓ-suc ℓ) where
  field
    thetaSection : DistinguishedThetaSection C
    parameter : DistinguishedThetaSection.Parameter thetaSection
    sectionZero :
      commonLine C → Type ℓ
    zeroImpliesWorkSewing :
      sectionZero (DistinguishedThetaSection.section thetaSection parameter) →
      work G ≡ zero G

open ThetaBoundaryConservation public

-- Once the independent boundary law is supplied, the existing Green identity
-- and positive-bulk cancellation force the transverse coordinate to vanish.
thetaZeroImpliesTransverseZero : {ℓ : Level}
  {R : ThirdOrderRelativeEndpoint {ℓ}}
  (C : ReciprocalChartCarrier R)
  (G : UnsewnGreenProblem {ℓ})
  (B : ThetaBoundaryConservation C G) →
  sectionZero B (DistinguishedThetaSection.section (thetaSection B) (parameter B)) →
  transverse G ≡ zero G
thetaZeroImpliesTransverseZero C G B vanishes =
  positiveBulkCancels G productZero
  where
  sewing : work G ≡ zero G
  sewing = zeroImpliesWorkSewing B vanishes

  productZero : _*_ G (transverse G) (bulk G) ≡ zero G
  productZero =
    sym (addZeroRight G (_*_ G (transverse G) (bulk G))) ∙
    cong (λ w → _+_ G (_*_ G (transverse G) (bulk G)) w)
      (sym sewing) ∙
    greenIdentity G
