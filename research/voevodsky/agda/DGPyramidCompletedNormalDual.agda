{-# OPTIONS --safe --cubical --guardedness #-}
module DGPyramidCompletedNormalDual where

open import Cubical.Foundations.Prelude
open import Cubical.Data.Empty using (⊥)

record CompletedNormalDualComparisonCertificate {ℓ : Level}
  : Type (ℓ-suc ℓ) where
  field
    NormalOrder FiniteFreeTarget LocalizedTarget TransitionMap : Type ℓ
    targetAtOrder : NormalOrder → FiniteFreeTarget
    transition : NormalOrder → NormalOrder → TransitionMap
    localizationComparison : NormalOrder → FiniteFreeTarget → LocalizedTarget
    transitionCompatibility : Type ℓ
    ColimitIsOriginalTarget : Type ℓ
    colimitWitness : ColimitIsOriginalTarget
    supportFiltrationPreservedAtEveryOrder : Type ℓ

    NativeSource LiftedComparison EndpointComposite : Type ℓ
    nativeSource : NativeSource
    liftedComparison : NormalOrder → LiftedComparison
    plusEndpoint minusEndpoint : NormalOrder → EndpointComposite
    comparisonTowerCompatibility : Type ℓ
    endpointEquationAtEveryOrder : Type ℓ

    FiniteDual DerivedInverseLimitDual CompletedGenericDual : Type ℓ
    finiteDual : NormalOrder → FiniteDual
    derivedInverseLimitDual : DerivedInverseLimitDual
    completedGenericDual : CompletedGenericDual
    inverseLimitComputesLocalizedDual : Type ℓ
    noFirstDerivedLimitCorrectionInGenericDegree : Type ℓ

    TraceImageIdeal UnitValue : Type ℓ
    exactTraceImageIdeal : TraceImageIdeal
    traceImageHasFourGenerators : Type ℓ
    unitValue : UnitValue
    TraceAttainsUnit : Type ℓ
    completionDoesNotAttainUnit : TraceAttainsUnit → ⊥
    completionDirectionsLieInTraceKernel : Type ℓ

    ReesPairProductIdeal ThreeAxisSupportDefect : Type ℓ
    reesPairProductIdeal : ReesPairProductIdeal
    threeAxisSupportDefect : ThreeAxisSupportDefect
    exactReesIdealResolution : Type ℓ
    reesImageIsPairProductIdeal : Type ℓ

    QuadraticPart CubicPart CubicEndpointPart : Type ℓ
    quadraticGenericPart : QuadraticPart
    cubicCorrectionPart : CubicPart
    cubicEndpointPart : CubicEndpointPart
    TwentySevenQuadraticTerms SixteenCubicTerms SixEndpointTerms : Type ℓ
    quadraticCountWitness : TwentySevenQuadraticTerms
    cubicCountWitness : SixteenCubicTerms
    endpointCountWitness : SixEndpointTerms
    quadraticToCubicEndpointEquation : Type ℓ

    ReesFace : Type ℓ
    comparisonOnFace : ReesFace → Type ℓ
    endpointOnFace : ReesFace → Type ℓ
    oneVanishingParameterLeavesNineGenericTerms : Type ℓ
    oneVanishingParameterKillsEndpoints : Type ℓ
    twoVanishingParametersKillEntireOrdinaryComparison : Type ℓ

    IndependentExcess : Type ℓ
    independentExcess : IndependentExcess
    excessClosed : Type ℓ
    excessTensorCompatibility : Type ℓ
    excessNotYetIdentifiedWithTargetMark : Type ℓ

    PhysicalSupportedReesGysinLift : Type ℓ
