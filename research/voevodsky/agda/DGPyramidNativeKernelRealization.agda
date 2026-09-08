{-# OPTIONS --safe --cubical --guardedness #-}
module DGPyramidNativeKernelRealization where

open import Cubical.Foundations.Prelude

-- Exact source-side contract left after construction of the finite graded
-- cubical supported-dual kernel. Predicates are fixed before a realization is
-- chosen, so validity cannot be defined post hoc by the candidate map.
record NativeKernelRealizationSpecification {ℓ : Level}
  : Type (ℓ-suc ℓ) where
  field
    NativeChain KernelChain : Type ℓ
    nativeDifferential : NativeChain → NativeChain
    kernelDifferential : KernelChain → KernelChain

    ConductorDegree PrimaryFrame : Type ℓ
    selectedConductorDegree : ConductorDegree
    selectedPrimaryFrame : PrimaryFrame

    PlusEndpoint MinusEndpoint GenericClass : Type ℓ
    plusEndpoint : PlusEndpoint
    minusEndpoint : MinusEndpoint
    genericClass : GenericClass

    NativeToKernel : Type ℓ
    underlyingMap : NativeToKernel → NativeChain → KernelChain
    ChainCompatible : NativeToKernel → Type ℓ
    SupportCompatible : NativeToKernel → Type ℓ
    ConductorDegreeCompatible : NativeToKernel → ConductorDegree → Type ℓ
    PrimaryFrameCompatible : NativeToKernel → PrimaryFrame → Type ℓ
    PlusEndpointCompatible : NativeToKernel → PlusEndpoint → Type ℓ
    MinusEndpointCompatible : NativeToKernel → MinusEndpoint → Type ℓ
    GenericCompatible : NativeToKernel → GenericClass → Type ℓ
    ReesCrossFrameCompatible : NativeToKernel → Type ℓ
    ExcessCompatible : NativeToKernel → Type ℓ
    LocalizationConnectingCompatible : NativeToKernel → Type ℓ
    Nonfactorizing : NativeToKernel → Type ℓ
    RingedVerdierCompatible : NativeToKernel → Type ℓ
    ReflectionParityCompatible : NativeToKernel → Type ℓ
    ResidualOccurrenceSupportCompatible : NativeToKernel → Type ℓ
    OccurrenceGysinCompatible : NativeToKernel → Type ℓ
    CoefficientSystemCapCompatible : NativeToKernel → Type ℓ
    DescentTorsorCompatible : NativeToKernel → Type ℓ
    TwelveResidueCoordinatesCompatible : NativeToKernel → Type ℓ
    FirstConductorPrimaryHomotopySelected : NativeToKernel → Type ℓ

    chainEquation : (f : NativeToKernel) → ChainCompatible f →
      (x : NativeChain) →
      kernelDifferential (underlyingMap f x) ≡
      underlyingMap f (nativeDifferential x)

record NativeKernelRealization {ℓ : Level}
  (Spec : NativeKernelRealizationSpecification {ℓ}) : Type (ℓ-suc ℓ) where
  open NativeKernelRealizationSpecification Spec
  field
    realization : NativeToKernel
    chainWitness : ChainCompatible realization
    supportWitness : SupportCompatible realization
    conductorDegreeWitness :
      ConductorDegreeCompatible realization selectedConductorDegree
    primaryFrameWitness :
      PrimaryFrameCompatible realization selectedPrimaryFrame
    plusEndpointWitness : PlusEndpointCompatible realization plusEndpoint
    minusEndpointWitness : MinusEndpointCompatible realization minusEndpoint
    genericWitness : GenericCompatible realization genericClass
    reesCrossFrameWitness : ReesCrossFrameCompatible realization
    excessWitness : ExcessCompatible realization
    localizationConnectingWitness :
      LocalizationConnectingCompatible realization
    nonfactorizingWitness : Nonfactorizing realization
    ringedVerdierWitness : RingedVerdierCompatible realization
    reflectionParityWitness : ReflectionParityCompatible realization
    residualOccurrenceSupportWitness :
      ResidualOccurrenceSupportCompatible realization
    occurrenceGysinWitness : OccurrenceGysinCompatible realization
    coefficientSystemCapWitness : CoefficientSystemCapCompatible realization
    descentTorsorWitness : DescentTorsorCompatible realization
    twelveResidueCoordinatesWitness :
      TwelveResidueCoordinatesCompatible realization
    firstConductorPrimaryHomotopyWitness :
      FirstConductorPrimaryHomotopySelected realization

-- No NativeKernelRealization is constructed in the current architecture.
