{-# OPTIONS --safe --cubical --guardedness #-}
module DGPyramidRelativeOperationOrbitMate where

open import Cubical.Foundations.Prelude

-- Once the physical endpoint orbit has actual operation coordinates, the
-- primitive mate extends canonically to the whole relative-operation orbit.
-- This avoids choosing 49 unrelated columns.
record RelativeOperationOrbitData {ℓ : Level} : Type (ℓ-suc ℓ) where
  field
    Operation SourceOrbitCarrier TargetOrbitCarrier : Type ℓ
    operationUnit : Operation
    composeOperation : Operation → Operation → Operation
    sourceAction : Operation → SourceOrbitCarrier → SourceOrbitCarrier
    targetAction : Operation → TargetOrbitCarrier → TargetOrbitCarrier
    sourcePrimitive : SourceOrbitCarrier
    targetPrimitive : TargetOrbitCarrier

    sourceActionAssociative :
      (r q : Operation) (x : SourceOrbitCarrier) →
      sourceAction (composeOperation r q) x ≡
      sourceAction r (sourceAction q x)
    targetActionAssociative :
      (r q : Operation) (x : TargetOrbitCarrier) →
      targetAction (composeOperation r q) x ≡
      targetAction r (targetAction q x)
    sourceUnitAction : (x : SourceOrbitCarrier) →
      sourceAction operationUnit x ≡ x
    targetUnitAction : (x : TargetOrbitCarrier) →
      targetAction operationUnit x ≡ x

open RelativeOperationOrbitData public

-- The missing physical datum is a coordinate in the native operation orbit,
-- not another target construction.  Branch A/B provide target freeness; the
-- physical endpoint checker has not yet supplied this source coordinate map.
record PhysicalOrbitCoordinates {ℓ : Level}
  (D : RelativeOperationOrbitData {ℓ}) : Type (ℓ-suc ℓ) where
  field
    operationCoordinate : SourceOrbitCarrier D → Operation D
    primitiveCoordinate :
      operationCoordinate (sourcePrimitive D) ≡ operationUnit D
    coordinateIntertwinesAction :
      (r : Operation D) (x : SourceOrbitCarrier D) →
      operationCoordinate (sourceAction D r x) ≡
      composeOperation D r (operationCoordinate x)
    coordinateReconstructsOrbit : (x : SourceOrbitCarrier D) →
      sourceAction D (operationCoordinate x) (sourcePrimitive D) ≡ x

open PhysicalOrbitCoordinates public

orbitMate : {ℓ : Level}
  (D : RelativeOperationOrbitData {ℓ}) →
  PhysicalOrbitCoordinates D →
  SourceOrbitCarrier D → TargetOrbitCarrier D
orbitMate D C x =
  targetAction D (operationCoordinate C x) (targetPrimitive D)

orbitMatePreservesPrimitive : {ℓ : Level}
  (D : RelativeOperationOrbitData {ℓ})
  (C : PhysicalOrbitCoordinates D) →
  orbitMate D C (sourcePrimitive D) ≡ targetPrimitive D
orbitMatePreservesPrimitive D C =
  cong (λ r → targetAction D r (targetPrimitive D))
    (primitiveCoordinate C) ∙
  targetUnitAction D (targetPrimitive D)

orbitMateIsOperationLinear : {ℓ : Level}
  (D : RelativeOperationOrbitData {ℓ})
  (C : PhysicalOrbitCoordinates D) →
  (r : Operation D) (x : SourceOrbitCarrier D) →
  orbitMate D C (sourceAction D r x) ≡
  targetAction D r (orbitMate D C x)
orbitMateIsOperationLinear D C r x =
  cong (λ q → targetAction D q (targetPrimitive D))
    (coordinateIntertwinesAction C r x) ∙
  targetActionAssociative D r (operationCoordinate C x)
    (targetPrimitive D)

-- The native reduced bar now supplies the first nine chain actions by cup
-- composition.  This is a construction on the genuinely native-linear model,
-- not on the literal ambient A-Hom or on the spatial target by fiat.
record NativeQuadraticChainAction {ℓ : Level} : Type (ℓ-suc ℓ) where
  field
    NativeEndpointComplex QuadraticOperation : Type ℓ
    nativeDifferential : NativeEndpointComplex → NativeEndpointComplex
    quadraticAction : QuadraticOperation →
      NativeEndpointComplex → NativeEndpointComplex
    quadraticActionsAreChainMaps :
      (r : QuadraticOperation) (x : NativeEndpointComplex) →
      quadraticAction r (nativeDifferential x) ≡
      nativeDifferential (quadraticAction r x)
    nineQuadraticOperationsArePresent : Type ℓ
    bothEndpointModelsAreCovered : Type ℓ
    primitiveImagesAreIndependent : Type ℓ
    actionIsNativeCupComposition : Type ℓ
    ambientMixedWeightsRemainAcyclic : Type ℓ

-- Contravariance is resolved by the Hopf antipode.  A primitive operation r
-- satisfies S(r)=-r, so the first nine endpoint columns acquire a mandatory
-- minus sign on the conormal right-precomposition side.
record GradedAntipodeVarianceMate {ℓ : Level} : Type (ℓ-suc ℓ) where
  field
    Operation EndpointOrbit ConormalOrbit Degree : Type ℓ
    operationUnit : Operation
    composeOperation : Operation → Operation → Operation
    operationDegree : Operation → Degree
    antipode : Operation → Operation
    endpointPrimitive : EndpointOrbit
    conormalPrimitive : ConormalOrbit
    leftCupAction : Operation → EndpointOrbit → EndpointOrbit
    rightPrecomposition : ConormalOrbit → Operation → ConormalOrbit
    koszulTwist : Degree → Degree → ConormalOrbit → ConormalOrbit
    operationCoordinate : EndpointOrbit → Operation

    mate : EndpointOrbit → ConormalOrbit
    mateFormula : (x : EndpointOrbit) →
      mate x ≡ rightPrecomposition conormalPrimitive
        (antipode (operationCoordinate x))
    antipodeIsGradedAntiMultiplicative : Type ℓ
    mateVarianceEquation : (q : Operation) (x : EndpointOrbit) →
      mate (leftCupAction q x) ≡
      koszulTwist (operationDegree q)
        (operationDegree (operationCoordinate x))
        (rightPrecomposition (mate x) (antipode q))
    all49PrimitiveAntipodesAreMinusIdentity : Type ℓ
    allNineQuadraticPrimitiveColumnsHaveMinusSign : Type ℓ
    boundedVerificationThroughOperationDegreeSix : Type ℓ
    allDegreeExtensionUsesAntipodeLawAndOrbitInjectivity : Type ℓ

record CurrentRelativeOrbitMateAudit {ℓ : Level} : Type (ℓ-suc ℓ) where
  field
    PrimitiveFineFrameMate : Type ℓ
    primitiveFineFrameMateExists : PrimitiveFineFrameMate
    nativeQuadraticChainAction : NativeQuadraticChainAction {ℓ}
    antipodeVarianceMate : GradedAntipodeVarianceMate {ℓ}
    targetRelativeOrbitIsInjectiveThroughDegreeSix : Type ℓ
    targetAllDegreeInjectivityUsesHopfFactorization : Type ℓ
    spatialEndpointToNativeBarIdentification : Type ℓ
    determinantLineAndSupportTransport : Type ℓ
    nineQuadraticSpatialMateHomotopiesAreNextRequiredColumns : Type ℓ
    noPhysicalOperationLinearMateClaimedWithoutSpatialTransport : Type ℓ
