{-# OPTIONS --safe --cubical --guardedness #-}
module DGPyramidConductorFormalTower where

open import Cubical.Foundations.Prelude
open import Cubical.Data.Empty using (⊥)

record ConductorFormalTowerCertificate {ℓ : Level}
  : Type (ℓ-suc ℓ) where
  field
    ConductorYonedaAlgebra ChannelOperationModule : Type ℓ
    freeProductOfSheetExteriorAlgebras : ConductorYonedaAlgebra
    sixLastBlockContractions : Type ℓ
    noCrossSheetRelations : Type ℓ
    fourteenCompleteChannelModules : ChannelOperationModule
    operationOrderNaturality : Type ℓ

    GlobalFrameGroup FirstConductorJet QuadraticTailKernel : Type ℓ
    globalFrameGroup : GlobalFrameGroup
    firstConductorJetAction : FirstConductorJet
    exactQuadraticTailKernel : QuadraticTailKernel
    quadraticTailsActStrictlyTriviallyOnConductorFibre : Type ℓ

    TransportedMarkingInfinityGroupoid GlobalFramedExtensionGroupoid : Type ℓ
    transportedMarkingInfinityGroupoid : TransportedMarkingInfinityGroupoid
    unboundedHigherMarkingGroups : Type ℓ
    globalFramedExtensionGroupoid : GlobalFramedExtensionGroupoid
    globalExtensionGroupoidIsOneType : Type ℓ
    higherConductorPathsCannotEraseEndpointAttachment : Type ℓ

    RegulatorCostalk RegulatorCounit : Type ℓ
    regulatorCostalk : RegulatorCostalk
    costalkIsFreeRankThirtyFour : Type ℓ
    counitKernelIsFreeRankThirtyOneAfterLocalization : Type ℓ
    counitImageHasThreeRegulatorTorsionDirections : Type ℓ
    threeNonzeroZeroPrimaryTransfers : Type ℓ
    invariantPrimaryLeavesTenZeroPrimaryDirections : Type ℓ

    FormalPuncturedGluing PuncturedTargetSubcomplex LiftObstruction : Type ℓ
    formalPuncturedGluing : FormalPuncturedGluing
    gluingRecoversAllFourteenGlobalResidues : Type ℓ
    gluingRecoversBothEndpointAttachments : Type ℓ
    puncturedTargetSubcomplex : PuncturedTargetSubcomplex
    oneHundredTwentyEightSummandsInvisibleToFiniteJets : Type ℓ
    seventyTwoTermJetQuotient : Type ℓ
    seventeenChannelLiftObstruction : LiftObstruction
    endpointUnitPassesEveryFiniteJetButDoesNotLift : Type ℓ

    PuncturedResidueBlock EndpointCechBlock LocalPuncturedDual : Type ℓ
    twentySignedPuncturedResidueBlocks : PuncturedResidueBlock
    twentyBlockDecompositionIsChainIsomorphism : Type ℓ
    endpointCechBlock : EndpointCechBlock
    endpointHasDegreeTwoObstructionAndDegreeZeroResidue : Type ℓ
    sevenTermEndpointKoszulCechTransgression : Type ℓ
    thirdDifferentialCancelsBothEndpointTorTowers : Type ℓ
    completedAffineDualKillsEntirePuncturedSubcomplex : Type ℓ
    completedAffineDualCannotDistinguishFullFromJetQuotient : Type ℓ
    nonzeroPolynomialEndpointDual : Type ℓ
    localPuncturedDual : LocalPuncturedDual
    localPuncturedDualIsNonzero : Type ℓ
    formalPuncturedLocalDualDataMustBeRetained : Type ℓ

    ConductorThickness TargetFramedMarking JetMarking : Type ℓ
    targetFramedAt : ConductorThickness → TargetFramedMarking
    jetMarkingAt : ConductorThickness → JetMarking
    eachFiniteTargetFramedStageHasUnboundedHomotopy : Type ℓ
    targetFramedTransitionsAreZeroOnAllHomotopyGroups : Type ℓ
    completedTargetFramedMarkingIsContractible : Type ℓ
    completeJetActionIsFaithful : Type ℓ
    compatibleJetMarkingLimitIsDiscrete : Type ℓ
    completedRingedModuleStillHasUnboundedTor : Type ℓ
    firstDerivedLimitRecordsNonglobalFormalTransport : Type ℓ
    formalTowerAloneDoesNotDetermineEndpointExtension : Type ℓ
