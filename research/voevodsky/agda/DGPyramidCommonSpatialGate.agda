{-# OPTIONS --safe --cubical --guardedness #-}
module DGPyramidCommonSpatialGate where

open import Cubical.Foundations.Prelude
open import Cubical.Data.Empty using (⊥)

record CommonSpatialCorrespondenceGateCertificate {ℓ : Level}
  : Type (ℓ-suc ℓ) where
  field
    SourceCone TargetCone MiddleCarrier GenericRelative : Type ℓ
    NormalKoszul SupportedCech Excess : Type ℓ
    sourceDifferential : SourceCone → SourceCone
    targetDifferential : TargetCone → TargetCone
    genericDifferential : GenericRelative → GenericRelative
    zeroGeneric : GenericRelative

    spatialConeMap : SourceCone → TargetCone
    spatialConeMapChainEquation : (z : SourceCone) →
      targetDifferential (spatialConeMap z) ≡
      spatialConeMap (sourceDifferential z)

    PlusEndpoint MinusEndpoint EndpointHomotopy : Type ℓ
    plusEndpoint : PlusEndpoint
    minusEndpoint : MinusEndpoint
    plusHomotopy minusHomotopy : EndpointHomotopy
    CoupledEndpointEquation : Type ℓ
    coupledEndpointWitness : CoupledEndpointEquation

    Roof MorseHomotopy : Type ℓ
    correctedRoof : Roof
    morseHomotopy : MorseHomotopy
    roofEnhancedMap : SourceCone → TargetCone
    roofPreservesEndpoints : Type ℓ
    roofEndpointWitness : roofPreservesEndpoints

    genericProjection : TargetCone → GenericRelative
    genericAdd : GenericRelative → GenericRelative → GenericRelative
    genericNullhomotopy : SourceCone → GenericRelative
    genericNullhomotopyEquation : (z : SourceCone) →
      genericProjection (roofEnhancedMap z) ≡
      genericAdd (genericDifferential (genericNullhomotopy z))
        (genericNullhomotopy (sourceDifferential z))

    supportedResidue : NormalKoszul → SupportedCech
    independentExcess : Excess
    TensorSource TensorTarget TensorGeneric : Type ℓ
    tensorCandidate : TensorSource → TensorTarget
    tensorGenericProjection : TensorTarget → TensorGeneric
    zeroTensorGeneric : TensorGeneric
    tensorDifferentialSource : TensorSource → TensorSource
    tensorDifferentialGeneric : TensorGeneric → TensorGeneric
    tensorAdd : TensorGeneric → TensorGeneric → TensorGeneric
    tensorNullhomotopy : TensorSource → TensorGeneric
    tensorGenericNullhomotopyEquation : (z : TensorSource) →
      tensorGenericProjection (tensorCandidate z) ≡
      tensorAdd (tensorDifferentialGeneric (tensorNullhomotopy z))
        (tensorNullhomotopy (tensorDifferentialSource z))

    GysinExtension : Type ℓ
    centralGysin : GysinExtension
    zeroGysin : GysinExtension
    centralGysinNonzero : centralGysin ≡ zeroGysin → ⊥

    GenericDerivedClass : Type ℓ
    classOfTensorGeneric : TensorGeneric → GenericDerivedClass
    zeroGenericClass : GenericDerivedClass
    candidateGenericClass : GenericDerivedClass
    candidateClassDefinition :
      candidateGenericClass ≡ classOfTensorGeneric zeroTensorGeneric
    zeroTensorClass : classOfTensorGeneric zeroTensorGeneric ≡ zeroGenericClass

    reverseGenericClass : GenericDerivedClass
    reverseGenericNonzero : reverseGenericClass ≡ zeroGenericClass → ⊥

    -- The tempting chamber/long-facet projection discards mixed flags and is
    -- not a chain map for the genuine relative quotient.
    SmallerGeneric : Type ℓ
    temptingProjection : GenericRelative → SmallerGeneric
    ChainMap : (GenericRelative → SmallerGeneric) → Type ℓ
    temptingProjectionNotChainMap : ChainMap temptingProjection → ⊥
    mixedFlagDefect : GenericRelative
    mixedFlagDefectNonzero : mixedFlagDefect ≡ zeroGeneric → ⊥

-- A factorization identifying the candidate generic class with the primitive
-- reverse class is impossible because the candidate is null.
record FactorizesReversePairing {ℓ : Level}
  (C : CommonSpatialCorrespondenceGateCertificate {ℓ}) : Type (ℓ-suc ℓ) where
  field
    identifiesGenericClasses :
      CommonSpatialCorrespondenceGateCertificate.reverseGenericClass C ≡
      CommonSpatialCorrespondenceGateCertificate.candidateGenericClass C

factorizedCandidateCannotRealizeReversePairing : {ℓ : Level}
  (C : CommonSpatialCorrespondenceGateCertificate {ℓ}) →
  FactorizesReversePairing C → ⊥
factorizedCandidateCannotRealizeReversePairing C F =
  CommonSpatialCorrespondenceGateCertificate.reverseGenericNonzero C
    (FactorizesReversePairing.identifiesGenericClasses F
    ∙ CommonSpatialCorrespondenceGateCertificate.candidateClassDefinition C
    ∙ CommonSpatialCorrespondenceGateCertificate.zeroTensorClass C)
