{-# OPTIONS --safe --cubical --guardedness #-}
module DGPyramidAugmentedResidueCandidateAudit where

open import Cubical.Foundations.Prelude
open import DGPyramidBetaEndpointQTransgression
open import DGPyramidJointConductorCone
open import DGPyramidUnionRecollement
open import DGPyramidReflectedConormalButterfly

-- Audit of already constructed cones.  It prevents choosing an object merely
-- because its name contains "cone" or "augmentation".
record ExistingBaseNullCandidateAudit {ℓ : Level}
  (BetaQ : BetaEndpointQTransgressionCertificate {ℓ})
  (Reverse : EndpointCompleteReverseConeCertificate {ℓ})
  (Union : UnionRecollementCertificate {ℓ})
  : Type (ℓ-suc ℓ) where
  field
    betaQPrimitiveHasNecessaryEndpointTerms : Type ℓ
    betaQPrimitiveHasNonzeroGenericProjection : Type ℓ
    betaQPrimitiveIsNotBaseNullResidue : Type ℓ

    reverseConeRetainsNonsplitEndpointAttachment : Type ℓ
    reverseConeHasNoConstructedBaseAugmentation : Type ℓ
    reverseConeHasNoConstructedNextCycleMap : Type ℓ

    finiteUnionCounitConeRetainsGenericData : Type ℓ
    finiteUnionCounitConeIsNotOpenComplement : Type ℓ
    unionConeHasNoMixedBoundaryIdentification : Type ℓ

    current215TargetHasNoOrdinaryPrimitiveCenterLift : Type ℓ
    noExistingCandidateYetInstantiatesAugmentedResidue : Type ℓ

-- The reduced endpoint-road augmentation is the closest structural candidate:
-- it already has a primitive base line, but the ringed normalization/PC map
-- and the next connecting morphism are still separate missing data.
record ReducedRoadBaseNullCandidate {ℓ : Level} : Type (ℓ-suc ℓ) where
  field
    EndpointRoadQTotal RoadOrientationLine BaseNullLine : Type ℓ
    NextCycleTarget : Type ℓ
    totalToRoadOrientation : EndpointRoadQTotal → RoadOrientationLine
    roadToBaseNull : RoadOrientationLine → BaseNullLine
    baseNullToNextCycle : BaseNullLine → NextCycleTarget

    EntirePyramidCycle : Type ℓ
    entirePyramidCycle : EntirePyramidCycle
    realizeTotalCycle : EntirePyramidCycle → EndpointRoadQTotal
    primitiveBaseResidue : BaseNullLine
    entireCycleHasPrimitiveBaseResidue :
      roadToBaseNull
        (totalToRoadOrientation (realizeTotalCycle entirePyramidCycle)) ≡
      primitiveBaseResidue

    PlusEndpoint MinusEndpoint GenericQ : Type ℓ
    zeroPlus : PlusEndpoint
    zeroMinus : MinusEndpoint
    zeroGenericQ : GenericQ
    restrictBasePlus : BaseNullLine → PlusEndpoint
    restrictBaseMinus : BaseNullLine → MinusEndpoint
    restrictBaseGenericQ : BaseNullLine → GenericQ
    primitiveResidueIsEndpointNull :
      restrictBasePlus primitiveBaseResidue ≡ zeroPlus
    primitiveResidueIsReflectedEndpointNull :
      restrictBaseMinus primitiveBaseResidue ≡ zeroMinus
    primitiveResidueIsGenericNull :
      restrictBaseGenericQ primitiveBaseResidue ≡ zeroGenericQ

    MixedBoundary NextEvaluation : Type ℓ
    betaSquaredEta04Eta35 : MixedBoundary
    nextEvaluation : NextEvaluation
    BaseBoundary : BaseNullLine → MixedBoundary → Type ℓ
    primitiveResidueHasMixedBoundary :
      BaseBoundary primitiveBaseResidue betaSquaredEta04Eta35
    NextCycleValue : NextCycleTarget → NextEvaluation → Type ℓ
    primitiveResidueFeedsNextCycle :
      NextCycleValue (baseNullToNextCycle primitiveBaseResidue) nextEvaluation

    missingRingedNormalizationToRoadMap : Type ℓ
    missingPhysicalEndpointGysinComparison : Type ℓ
    missingDerivationOfMixedBoundaryEquation : Type ℓ
    missingCanonicalNextCycleConnectingMorphsim : Type ℓ
    candidateIsNotYetAnAugmentedResidueConstruction : Type ℓ

record AugmentedResidueSelectionGate {ℓ : Level}
  (Candidate : ReducedRoadBaseNullCandidate {ℓ})
  : Type (ℓ-suc ℓ) where
  field
    RingedNormalizationPromotion : Type ℓ
    PhysicalEndpointComparison : Type ℓ
    MixedBoundaryDerivation : Type ℓ
    CanonicalNextConnectingMap : Type ℓ
    selectionRequiresAllFourMissingMaps : Type ℓ
    noSelectionFromPrimitiveRoadAugmentationAlone : Type ℓ
