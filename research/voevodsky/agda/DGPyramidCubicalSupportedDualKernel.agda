{-# OPTIONS --safe --cubical --guardedness #-}
module DGPyramidCubicalSupportedDualKernel where

open import Cubical.Foundations.Prelude
open import Cubical.Data.Empty using (⊥)

record CubicalSupportedDualKernelCertificate {ℓ : Level}
  : Type (ℓ-suc ℓ) where
  field
    Face MarkedState CubeCell TargetDual Sign : Type ℓ
    lower upper : CubeCell → Face
    cellOf : MarkedState → CubeCell
    orientationSign : MarkedState → Sign
    signedCell : Sign → CubeCell → CubeCell
    spatialRealization : TargetDual → CubeCell

    targetDualDifferential : TargetDual → TargetDual
    cubicalBoundary : CubeCell → CubeCell
    signedDualIdentification : MarkedState → TargetDual
    boundaryCompatibility : (s : MarkedState) →
      cubicalBoundary
        (signedCell (orientationSign s) (cellOf s)) ≡
      spatialRealization
        (targetDualDifferential (signedDualIdentification s))

    CubicalCellCount215 FlagTriangulation : Type ℓ
    cellCountWitness : CubicalCellCount215
    triangulation : CubeCell → FlagTriangulation
    CubicalDimension TargetDegree : Type ℓ
    cubicalDimension : CubeCell → CubicalDimension
    targetDegree : MarkedState → TargetDegree
    degreeReversal : Type ℓ
    degreeReversalWitness : degreeReversal

    W WQ WE : Type ℓ
    includeQInE : WQ → WE
    includeEInW : WE → W
    supportsStrictlyNested : Type ℓ
    nestedSupportWitness : supportsStrictlyNested

    KDual QDual BDual EDual VDual BoundaryModuloVDual : Type ℓ
    chainsW : KDual
    chainsWQ : QDual
    relativeWWQ : BDual
    chainsWE : EDual
    relativeWWE : VDual
    relativeWEWQ : BoundaryModuloVDual
    ReversedSupportIdentification : Type ℓ
    reversedSupportWitness : ReversedSupportIdentification

    FineDegree ForbiddenFaces RelativeCubeComplex : Type ℓ
    forbiddenFaces : FineDegree → ForbiddenFaces
    relativeAtDegree : FineDegree → RelativeCubeComplex
    coefficientDomainIdentification : FineDegree → Type ℓ
    coefficientDomainWitness : (α : FineDegree) →
      coefficientDomainIdentification α
    NormalMultiplicationArrow : Type ℓ
    normalMultiplicationAsRelativeQuotient : NormalMultiplicationArrow

    TensorCell : Type ℓ
    diagonal : CubeCell → TensorCell
    tensorBoundary : TensorCell → TensorCell
    diagonalChainMap : (c : CubeCell) →
      tensorBoundary (diagonal c) ≡ diagonal (cubicalBoundary c)
    tripleTensorCell : Type ℓ
    diagonalLeft diagonalRight : CubeCell → tripleTensorCell
    diagonalStrictlyCoassociative : (c : CubeCell) →
      diagonalLeft c ≡ diagonalRight c

    AlexanderWhitneyTarget : Type ℓ
    cubicalToAW simplicialAW : CubeCell → AlexanderWhitneyTarget
    strictAWCompatibility : (c : CubeCell) → cubicalToAW c ≡ simplicialAW c

    ResidualNormal ExcessCell GenericVertex RelativeEdge : Type ℓ
    residualNormal : ResidualNormal
    excessCell : ExcessCell
    genericVertex : GenericVertex
    relativeEdge : RelativeEdge
    ProductRelativeCell : Type ℓ
    xiBoundary xiGeneric : ProductRelativeCell
    productBoundary : ProductRelativeCell → ProductRelativeCell
    relativeEdgeTransgression : productBoundary xiBoundary ≡ xiGeneric

    SupportObstruction GenericObstruction Scalar : Type ℓ
    betaPlus : SupportObstruction
    genericPlus : GenericObstruction
    one zeroScalar : Scalar
    evaluateSupport : ProductRelativeCell → SupportObstruction → Scalar
    evaluateGeneric : ProductRelativeCell → GenericObstruction → Scalar
    primitiveSupportEvaluation : evaluateSupport xiBoundary betaPlus ≡ one
    primitiveGenericEvaluation : evaluateGeneric xiGeneric genericPlus ≡ one
    oneNonzero : one ≡ zeroScalar → ⊥

    PlusCollar MinusCollar MorseOperator : Type ℓ
    plusCollar : PlusCollar
    minusCollar : MinusCollar
    EndpointOperatorEquations : Type ℓ
    endpointOperatorWitness : EndpointOperatorEquations
    morseOperator : MorseOperator
    MorseComparisonEquation : Type ℓ
    morseComparisonWitness : MorseComparisonEquation

    SupportedResidue TensorKernel : Type ℓ
    supportedResidue : SupportedResidue
    tensorWithResidue : SupportedResidue → ProductRelativeCell → TensorKernel
    SupportedResidueChainCompatibility : Type ℓ
    supportedResidueChainWitness : SupportedResidueChainCompatibility
    GysinValue : Type ℓ
    gysinValue : GysinValue
    zeroGysin : GysinValue
    gysinEvaluationNonzero : gysinValue ≡ zeroGysin → ⊥

    -- These are the remaining external realization types; this certificate
    -- constructs no inhabitants of them.
    NormalizationSheet : Type ℓ
    NormalizationSheetToKernel : NormalizationSheet → Type ℓ
    RingedVerdierIdentification : Type ℓ
    CrossFrameEndpointComparison : Type ℓ
    PhysicalReflectionParity : Type ℓ

reversePairingIsSpatiallyNonzero : {ℓ : Level}
  (C : CubicalSupportedDualKernelCertificate {ℓ}) →
  CubicalSupportedDualKernelCertificate.evaluateGeneric C
    (CubicalSupportedDualKernelCertificate.xiGeneric C)
    (CubicalSupportedDualKernelCertificate.genericPlus C) ≡
  CubicalSupportedDualKernelCertificate.zeroScalar C → ⊥
reversePairingIsSpatiallyNonzero C zeroEvaluation =
  CubicalSupportedDualKernelCertificate.oneNonzero C
    (sym (CubicalSupportedDualKernelCertificate.primitiveGenericEvaluation C)
    ∙ zeroEvaluation)
