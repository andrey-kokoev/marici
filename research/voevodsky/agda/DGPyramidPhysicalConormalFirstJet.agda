{-# OPTIONS --safe --cubical --guardedness #-}
module DGPyramidPhysicalConormalFirstJet where

open import Cubical.Foundations.Prelude

-- Exact adapter result for all eight complete framed Gysin sources.  The
-- endpoint detector and conormal primitive use the same unique top source
-- state.  Their target lines, rather than their source degrees, remain to be
-- compared.
record PhysicalConormalFirstJetAudit {ℓ : Level} : Type (ℓ-suc ℓ) where
  field
    SourceState SourceDegree CoefficientIdeal : Type ℓ
    conormalTopState endpointPrimitiveInputState : SourceState
    sourceDegree : SourceState → SourceDegree
    commonActualDegree : SourceDegree
    sourceDegreeOfConormalTop :
      sourceDegree conormalTopState ≡ commonActualDegree
    endpointUsesSameTopSourceState :
      endpointPrimitiveInputState ≡ conormalTopState

    productCartierParameter : CoefficientIdeal
    endpointNormalParameter0 endpointNormalParameter1
      endpointNormalParameter2 : CoefficientIdeal
    conormalColumnCoefficientIsOne : Type ℓ
    noIncomingSourceStateInNextDegree : Type ℓ
    kernelFirstJetClosedEquationPasses : Type ℓ
    kernelFirstJetNormalizationEquationPasses : Type ℓ
    homotopyAmbiguityIsQuotientByCartierAndEndpointNormals : Type ℓ
    allEightFramedCasesPass : Type ℓ

open PhysicalConormalFirstJetAudit public

-- The source-column part of the endpoint-to-conormal comparison is canonical:
-- both normalized primitives evaluate the same top input state.
sharedPrimitiveInput : {ℓ : Level}
  (A : PhysicalConormalFirstJetAudit {ℓ}) →
  endpointPrimitiveInputState A ≡ conormalTopState A
sharedPrimitiveInput = endpointUsesSameTopSourceState

-- What remains is a target-line mate.  It has degree zero in the fully shifted
-- physical model; no artificial three-degree source displacement is needed.
record EndpointToConormalMateGate {ℓ : Level}
  (A : PhysicalConormalFirstJetAudit {ℓ}) : Type (ℓ-suc ℓ) where
  field
    EndpointTarget ConormalTarget : Type ℓ
    targetMate : EndpointTarget → ConormalTarget
    mateHasDegreeZeroAfterPhysicalShift : Type ℓ
    determinantAndConormalLineComparison : Type ℓ
    mateSendsFullyMarkedEndpointGeneratorToConormalGenerator : Type ℓ
    mateRespectsNativeRingAction : Type ℓ
    mateRespectsEndpointSupport : Type ℓ
    mateCarriesPrimitiveCoefficientOneToCoefficientOne : Type ℓ
    nineMixedOperationIntertwiners : Type ℓ
    reflectionTransportOfMate : Type ℓ

record PrimitiveFineFrameChainMateAudit {ℓ : Level}
  (A : PhysicalConormalFirstJetAudit {ℓ}) : Type (ℓ-suc ℓ) where
  field
    EndpointFrameComplex ConormalFrameComplex : Type ℓ
    endpointDifferential : EndpointFrameComplex → EndpointFrameComplex
    conormalDifferential : ConormalFrameComplex → ConormalFrameComplex
    endpointPrimitive : EndpointFrameComplex
    conormalPrimitive : ConormalFrameComplex
    primitiveMate : EndpointFrameComplex → ConormalFrameComplex
    primitiveMateEquation : primitiveMate endpointPrimitive ≡ conormalPrimitive
    primitiveMateIsChainMap : (x : EndpointFrameComplex) →
      primitiveMate (endpointDifferential x) ≡
      conormalDifferential (primitiveMate x)
    endpointDetectorIsIntegral : Type ℓ
    endpointDetectorAnnihilatesEveryIncomingBoundary : Type ℓ
    allEightPrimitiveFineFrameChainMatesPass : Type ℓ
    extensionBeyondPrimitiveHomogeneousFrameRemainsOpen : Type ℓ
    operationLinearMateRemainsOpen : Type ℓ
