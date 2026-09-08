{-# OPTIONS --safe --cubical --guardedness #-}
module DGPyramidBetaEndpointQTransgression where

open import Cubical.Foundations.Prelude
open import Cubical.Data.Empty using (⊥)

record BetaEndpointQTransgressionCertificate {ℓ : Level}
  : Type (ℓ-suc ℓ) where
  field
    Coeff TopCycle Endpoint QClass BoundaryClass : Type ℓ
    beta betaSquared zeroCoeff : Coeff
    multiplyTop : Coeff → TopCycle → TopCycle
    multiplyBoundary : Coeff → BoundaryClass → BoundaryClass
    addTop : TopCycle → TopCycle → TopCycle

    zMinus zPlus : TopCycle
    endpointCoordinates : TopCycle → Endpoint
    qProjection : TopCycle → QClass
    zeroEndpoint : Endpoint
    zeroQ : QClass
    phiQ : QClass

    TopCoefficients : TopCycle → Type ℓ
    reconstructTop : TopCoefficients zMinus → TopCoefficients zPlus → TopCycle
    endpointCoordinatesComplete : (z w : TopCycle) →
      endpointCoordinates z ≡ endpointCoordinates w → z ≡ w
    qForcedByNegativeEndpoint : Type ℓ
    endpointQCompatibilityWitness : qForcedByNegativeEndpoint

    RecordedPrimitive : Type ℓ
    firstPrimitive secondPrimitive : RecordedPrimitive
    RequiredEndpointCorrection : RecordedPrimitive → RecordedPrimitive → TopCycle → Type ℓ
    zMinusCorrectsEndpoints :
      RequiredEndpointCorrection secondPrimitive firstPrimitive zMinus
    endpointCorrectionUnique : (z : TopCycle) →
      RequiredEndpointCorrection secondPrimitive firstPrimitive z → z ≡ zMinus
    scaleQ : Coeff → QClass → QClass
    zMinusQProjection : qProjection zMinus ≡ scaleQ betaSquared phiQ
    correctionCannotHaveZeroQ : qProjection zMinus ≡ zeroQ → ⊥

    QLift BoundaryChain : Type ℓ
    liftPhiQ : QLift
    attachingCycle : BoundaryClass
    boundaryOfQLift : QLift → BoundaryClass
    attachingDefinition : boundaryOfQLift liftPhiQ ≡ attachingCycle
    zeroBoundary : BoundaryClass
    attachingNonzero : attachingCycle ≡ zeroBoundary → ⊥
    betaAttachingNonzero :
      multiplyBoundary beta attachingCycle ≡ zeroBoundary → ⊥
    betaSquaredKillsAttaching :
      multiplyBoundary betaSquared attachingCycle ≡ zeroBoundary
    OrdinaryExactAnnihilatorBetaSquared : Type ℓ
    ordinaryAnnihilatorWitness : OrdinaryExactAnnihilatorBetaSquared

    annihilatingPrimitive : BoundaryChain
    boundaryDifferential : BoundaryChain → BoundaryClass
    annihilatingPrimitiveEquation :
      boundaryDifferential annihilatingPrimitive ≡
      multiplyBoundary betaSquared attachingCycle
    EndpointTermsPresent : BoundaryChain → Type ℓ
    primitiveRetainsEndpointTerms : EndpointTermsPresent annihilatingPrimitive
    removeEndpointTerms : BoundaryChain → BoundaryChain
    endpointTermsAreNecessary :
      boundaryDifferential (removeEndpointTerms annihilatingPrimitive) ≡
      multiplyBoundary betaSquared attachingCycle → ⊥

    SupportedMapDifference QHomotopy : Type ℓ
    supportedDifference : SupportedMapDifference
    uniqueQNullhomotopy : QHomotopy
    QNullhomotopy : SupportedMapDifference → QHomotopy → Type ℓ
    qNullhomotopyWitness : QNullhomotopy supportedDifference uniqueQNullhomotopy
    qNullhomotopyUnique : (h : QHomotopy) →
      QNullhomotopy supportedDifference h → h ≡ uniqueQNullhomotopy
    lowerLiftingDefect : BoundaryClass
    lowerDefectEquation :
      lowerLiftingDefect ≡ multiplyBoundary beta attachingCycle
    lowerDefectNonzero : lowerLiftingDefect ≡ zeroBoundary → ⊥

    StrictEndpointBoundaryClass : Type ℓ
    strictClass : StrictEndpointBoundaryClass
    zeroStrictClass : StrictEndpointBoundaryClass
    StrictPolynomialAnnihilator : Coeff → StrictEndpointBoundaryClass → Type ℓ
    strictClassNonzero : strictClass ≡ zeroStrictClass → ⊥
    strictHasNoNonzeroAnnihilator : (a : Coeff) →
      StrictPolynomialAnnihilator a strictClass → a ≡ zeroCoeff
    forgetStrictEndpoint : StrictEndpointBoundaryClass → BoundaryClass
    forgetStrictClass : forgetStrictEndpoint strictClass ≡ attachingCycle

    ExtraCentralClass FirstOrderObstruction : Type ℓ
    extraCentralClass : ExtraCentralClass
    TwelveEndpointFixedClasses : Type ℓ
    twelveEndpointFixedWitness : TwelveEndpointFixedClasses
    firstOrderObstruction : ExtraCentralClass → FirstOrderObstruction
    zeroFirstOrder : FirstOrderObstruction
    allExtraClassesObstructed : (z : ExtraCentralClass) →
      firstOrderObstruction z ≡ zeroFirstOrder → ⊥

qNullhomotopyDoesNotPreserveLowerCochain : {ℓ : Level}
  (C : BetaEndpointQTransgressionCertificate {ℓ}) →
  BetaEndpointQTransgressionCertificate.lowerLiftingDefect C ≡
  BetaEndpointQTransgressionCertificate.zeroBoundary C → ⊥
qNullhomotopyDoesNotPreserveLowerCochain C =
  BetaEndpointQTransgressionCertificate.lowerDefectNonzero C

ordinaryEndpointTorsionDoesNotExtendToStrictFrame : {ℓ : Level}
  (C : BetaEndpointQTransgressionCertificate {ℓ}) →
  BetaEndpointQTransgressionCertificate.StrictPolynomialAnnihilator C
    (BetaEndpointQTransgressionCertificate.betaSquared C)
    (BetaEndpointQTransgressionCertificate.strictClass C) →
  BetaEndpointQTransgressionCertificate.betaSquared C ≡
    BetaEndpointQTransgressionCertificate.zeroCoeff C
ordinaryEndpointTorsionDoesNotExtendToStrictFrame C h =
  BetaEndpointQTransgressionCertificate.strictHasNoNonzeroAnnihilator C
    (BetaEndpointQTransgressionCertificate.betaSquared C) h
