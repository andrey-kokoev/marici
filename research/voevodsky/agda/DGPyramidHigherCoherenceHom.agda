{-# OPTIONS --safe --cubical --guardedness #-}
module DGPyramidHigherCoherenceHom where

open import Cubical.Foundations.Prelude
open import Cubical.Data.Empty using (⊥)

-- Two gradings must not be conflated.  Negative coherence degree records
-- homotopies between degree-zero maps.  Positive RHom degree records Ext and
-- the conductor operations acting on those maps.
record HigherCoherenceHomComplex {ℓ : Level} : Type (ℓ-suc ℓ) where
  field
    Map0 MapHomotopyMinus1 MapHigherHomotopyMinus2 : Type ℓ
    ExtCochain1 ExtCocycle2 : Type ℓ
    SourceEnd1 SourceEnd2 : Type ℓ

    zeroMap : Map0
    zeroMapHomotopy : MapHomotopyMinus1
    zeroExt2 : ExtCocycle2
    coherenceDifferential1 : MapHomotopyMinus1 → Map0
    coherenceDifferential2 : MapHigherHomotopyMinus2 → MapHomotopyMinus1
    coherenceDifferentialSquaresToZero :
      (h : MapHigherHomotopyMinus2) →
      coherenceDifferential1 (coherenceDifferential2 h) ≡ zeroMap

    extDifferential : ExtCochain1 → ExtCocycle2
    composeSourceOperations : SourceEnd1 → SourceEnd1 → SourceEnd2
    realizeSourceOperation : Map0 → SourceEnd2 → ExtCocycle2

    Source Target : Type ℓ
    sourceIsKProjectiveOrTargetIsKInjective : Type ℓ
    ordinaryHomComplexComputesDerivedHom : Type ℓ
    homCohomologyComputesDerivedExt : Type ℓ
    sourceEndomorphismsFormDifferentialGradedAlgebra : Type ℓ
    sourceActionMakesHomARightDGModule : Type ℓ
    oppositeAlgebraAndKoszulSignsAreRetained : Type ℓ
    compositionIsAMapOfComplexes : Type ℓ
    tensorHomTotalizationCompatibility : Type ℓ
    mappingConeCompatibility : Type ℓ

open HigherCoherenceHomComplex public

record ButterflyMaurerCartanBoundary {ℓ : Level}
  (H : HigherCoherenceHomComplex {ℓ}) : Type (ℓ-suc ℓ) where
  field
    scalarMap : Map0 H
    eta35 reflectedEta04 : SourceEnd1 H
    mixedSourceOperation : SourceEnd2 H
    mixedSourceOperationIsComposition :
      mixedSourceOperation ≡
      composeSourceOperations H eta35 reflectedEta04

    plusEndpointHomotopy minusEndpointHomotopy : MapHomotopyMinus1 H
    plusEndpointHomotopyHasRequiredBoundary : Type ℓ
    minusEndpointHomotopyHasRequiredBoundary : Type ℓ

    mixedRHomCocycle : ExtCocycle2 H
    mixedCocycleIsSourceAction :
      mixedRHomCocycle ≡
      realizeSourceOperation H scalarMap mixedSourceOperation

    MixedObstructionClass : Type ℓ
    mixedObstructionClass zeroMixedObstructionClass : MixedObstructionClass
    classOfExt2Cocycle : ExtCocycle2 H → MixedObstructionClass
    classOfExtBoundaryIsZero : (c : ExtCochain1 H) →
      classOfExt2Cocycle (extDifferential H c) ≡ zeroMixedObstructionClass
    mixedClassIsBetaSquaredEta04Eta35 :
      classOfExt2Cocycle mixedRHomCocycle ≡ mixedObstructionClass
    mixedClassNonzero :
      mixedObstructionClass ≡ zeroMixedObstructionClass → ⊥

-- Killing the mixed Ext^2 class requires an Ext-degree-one cochain.  This is
-- distinct from both a target state and a degree-minus-two endpoint coherence.
record HigherCoherenceLiftProblem {ℓ : Level}
  (H : HigherCoherenceHomComplex {ℓ})
  (Boundary : ButterflyMaurerCartanBoundary H)
  : Type (ℓ-suc ℓ) where
  open ButterflyMaurerCartanBoundary Boundary
  field
    CandidateExt1Lift : Type ℓ
    liftCochain : CandidateExt1Lift → ExtCochain1 H
    liftEquation : CandidateExt1Lift → Type ℓ
    liftEquationMeansDifferentialIsMixedCocycle :
      (c : CandidateExt1Lift) →
      liftEquation c → extDifferential H (liftCochain c) ≡ mixedRHomCocycle
    liftMustRespectEndpointSupport : CandidateExt1Lift → Type ℓ
    liftMustHaveZeroGenericQProjection : CandidateExt1Lift → Type ℓ
    liftMustRespectReflectionWithDecomposableCorrection :
      CandidateExt1Lift → Type ℓ
    currentRHomClassMayObstructLift : Type ℓ

noCurrentRHomLift : {ℓ : Level} (H : HigherCoherenceHomComplex {ℓ})
  (Boundary : ButterflyMaurerCartanBoundary H)
  (Problem : HigherCoherenceLiftProblem H Boundary)
  (c : HigherCoherenceLiftProblem.CandidateExt1Lift Problem) →
  HigherCoherenceLiftProblem.liftEquation Problem c → ⊥
noCurrentRHomLift H Boundary Problem c equation =
  ButterflyMaurerCartanBoundary.mixedClassNonzero Boundary
    (sym (ButterflyMaurerCartanBoundary.mixedClassIsBetaSquaredEta04Eta35 Boundary) ∙
     cong (ButterflyMaurerCartanBoundary.classOfExt2Cocycle Boundary)
       (sym (HigherCoherenceLiftProblem.liftEquationMeansDifferentialIsMixedCocycle
         Problem c equation)) ∙
     ButterflyMaurerCartanBoundary.classOfExtBoundaryIsZero Boundary
       (HigherCoherenceLiftProblem.liftCochain Problem c))

-- Minimal enlargement of RHom in which the mixed Ext^2 class transgresses
-- from one new Ext-degree-one cochain.  Endpoint and generic projections are
-- imposed on the enlarged Hom complex, not on the visible target states.
record AugmentedHigherCoherenceHom {ℓ : Level}
  (H : HigherCoherenceHomComplex {ℓ})
  (Boundary : ButterflyMaurerCartanBoundary H)
  : Type (ℓ-suc ℓ) where
  open ButterflyMaurerCartanBoundary Boundary
  field
    AugmentedExt1 AugmentedExt2 : Type ℓ
    augmentedDifferential : AugmentedExt1 → AugmentedExt2
    includeExt1 : ExtCochain1 H → AugmentedExt1
    includeExt2 : ExtCocycle2 H → AugmentedExt2
    inclusionCommutesWithDifferential : (c : ExtCochain1 H) →
      augmentedDifferential (includeExt1 c) ≡
      includeExt2 (extDifferential H c)

    baseNullTransgression : AugmentedExt1
    baseNullTransgressionEquation :
      augmentedDifferential baseNullTransgression ≡
      includeExt2 mixedRHomCocycle

    EndpointReadout GenericQReadout : Type ℓ
    zeroEndpointReadout : EndpointReadout
    zeroGenericQReadout : GenericQReadout
    endpointReadout : AugmentedExt1 → EndpointReadout
    genericQReadout : AugmentedExt1 → GenericQReadout
    baseNullHasZeroEndpointReadout :
      endpointReadout baseNullTransgression ≡ zeroEndpointReadout
    baseNullHasZeroGenericQReadout :
      genericQReadout baseNullTransgression ≡ zeroGenericQReadout

    RelativeCone ConnectingTarget : Type ℓ
    relativeConeClass : RelativeCone
    connectingMorphism : RelativeCone → ConnectingTarget
    connectedBaseNullClass : ConnectingTarget
    connectingEquation :
      connectingMorphism relativeConeClass ≡ connectedBaseNullClass
    augmentationIsMappingConeCompatible : Type ℓ
    augmentationPreservesDerivedHomComposition : Type ℓ

record CurrentRHomRetraction {ℓ : Level}
  (H : HigherCoherenceHomComplex {ℓ})
  (Boundary : ButterflyMaurerCartanBoundary H)
  (Augmented : AugmentedHigherCoherenceHom H Boundary)
  : Type (ℓ-suc ℓ) where
  field
    retractExt1 : AugmentedHigherCoherenceHom.AugmentedExt1 Augmented →
      ExtCochain1 H
    retractExt2 : AugmentedHigherCoherenceHom.AugmentedExt2 Augmented →
      ExtCocycle2 H
    retractExt2OnIncludedMixed :
      retractExt2
        (AugmentedHigherCoherenceHom.includeExt2 Augmented
          (ButterflyMaurerCartanBoundary.mixedRHomCocycle Boundary)) ≡
      ButterflyMaurerCartanBoundary.mixedRHomCocycle Boundary
    retractionCommutesWithDifferential :
      (c : AugmentedHigherCoherenceHom.AugmentedExt1 Augmented) →
      retractExt2
        (AugmentedHigherCoherenceHom.augmentedDifferential Augmented c) ≡
      extDifferential H (retractExt1 c)

-- The augmentation is necessarily genuine: a chain retraction back to the
-- old RHom complex would turn its nonzero mixed Ext class into a boundary.
noCurrentRHomRetraction : {ℓ : Level}
  (H : HigherCoherenceHomComplex {ℓ})
  (Boundary : ButterflyMaurerCartanBoundary H)
  (Augmented : AugmentedHigherCoherenceHom H Boundary) →
  CurrentRHomRetraction H Boundary Augmented → ⊥
noCurrentRHomRetraction H Boundary Augmented Retraction =
  ButterflyMaurerCartanBoundary.mixedClassNonzero Boundary
    (sym (ButterflyMaurerCartanBoundary.mixedClassIsBetaSquaredEta04Eta35 Boundary) ∙
     cong (ButterflyMaurerCartanBoundary.classOfExt2Cocycle Boundary)
       (sym (CurrentRHomRetraction.retractExt2OnIncludedMixed Retraction) ∙
        cong (CurrentRHomRetraction.retractExt2 Retraction)
          (sym (AugmentedHigherCoherenceHom.baseNullTransgressionEquation Augmented)) ∙
        CurrentRHomRetraction.retractionCommutesWithDifferential Retraction
          (AugmentedHigherCoherenceHom.baseNullTransgression Augmented)) ∙
     ButterflyMaurerCartanBoundary.classOfExtBoundaryIsZero Boundary
       (CurrentRHomRetraction.retractExt1 Retraction
         (AugmentedHigherCoherenceHom.baseNullTransgression Augmented)))
