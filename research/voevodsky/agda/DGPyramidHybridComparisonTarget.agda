{-# OPTIONS --safe --cubical --guardedness #-}
module DGPyramidHybridComparisonTarget where

open import Cubical.Foundations.Prelude
open import Cubical.Data.Empty using (⊥)
open import DGPyramidPhysicalEndpointPullback
open import DGPyramidTetrahedralEndpointBoundary

-- The two computed comparison models retain complementary data.  Their
-- homotopy pullback is the smallest target in which endpoint and generic
-- columns can coexist without identifying the two models.
record HybridComparisonCospan {ℓ : Level} : Type (ℓ-suc ℓ) where
  field
    EndpointModel ComplementaryModel CommonShortSupport : Type ℓ
    endpointRestriction : EndpointModel → CommonShortSupport
    complementaryRestriction : ComplementaryModel → CommonShortSupport

open HybridComparisonCospan public

HybridComparisonTarget : {ℓ : Level} → HybridComparisonCospan {ℓ} → Type ℓ
HybridComparisonTarget C =
  Σ[ endpoint ∈ EndpointModel C ]
  Σ[ generic ∈ ComplementaryModel C ]
    endpointRestriction C endpoint ≡ complementaryRestriction C generic

record HybridBivariantEndpointMap {ℓ : Level}
  (C : HybridComparisonCospan {ℓ}) : Type (ℓ-suc ℓ) where
  field
    CompleteFramedSource PrimitiveEndpointColumn BareQColumn : Type ℓ
    primitiveEndpointColumn : PrimitiveEndpointColumn
    bareQColumn : BareQColumn

    endpointLeg : CompleteFramedSource → EndpointModel C
    complementaryLeg : CompleteFramedSource → ComplementaryModel C
    overlapHomotopy : (x : CompleteFramedSource) →
      endpointRestriction C (endpointLeg x) ≡
      complementaryRestriction C (complementaryLeg x)

    bivariantMap : CompleteFramedSource → HybridComparisonTarget C
    bivariantMapIsThePairedMap : (x : CompleteFramedSource) →
      bivariantMap x ≡
        (endpointLeg x , (complementaryLeg x , overlapHomotopy x))

    endpointLegRetainsPrimitiveColumn : Type ℓ
    complementaryLegRetainsPrimitiveBareQColumn : Type ℓ
    completeProductCartierSourceIsRetained : Type ℓ
    degreeZeroAndFramePreserving : Type ℓ
    determinantLineIsNotEulerEvaluated : Type ℓ

    RelativeOperationAction : Type ℓ
    operationIntertwinersForBothLegs : RelativeOperationAction
    overlapHomotopyIsOperationCoherent : Type ℓ
    dihedralTransportIsCoherent : Type ℓ

-- Exact gate exposed by the hybrid construction: the objectwise pair of maps
-- is insufficient; their restrictions must be connected in the common
-- short-support model.  This is where the diagonal obstruction is tested.
record HybridOverlapObstruction {ℓ : Level}
  (C : HybridComparisonCospan {ℓ}) : Type (ℓ-suc ℓ) where
  field
    CompleteFramedSource : Type ℓ
    endpointLeg : CompleteFramedSource → EndpointModel C
    complementaryLeg : CompleteFramedSource → ComplementaryModel C
    Obstruction : Type ℓ
    zeroObstruction oneOneObstruction : Obstruction
    compareRestrictions : (x : CompleteFramedSource) → Obstruction
    primitiveColumn : CompleteFramedSource
    primitiveComparisonIsOneOne :
      compareRestrictions primitiveColumn ≡ oneOneObstruction
    oneOneIsNonzero : oneOneObstruction ≡ zeroObstruction → ⊥

-- Current executable evidence supplies the two legs separately.  It does not
-- yet supply their common coefficient-base/frame assignment or overlap
-- homotopy, so no inhabitant of HybridBivariantEndpointMap is asserted.
record CurrentHybridComparisonAudit {ℓ : Level} : Type (ℓ-suc ℓ) where
  field
    Cospan : HybridComparisonCospan {ℓ}
    factorizedModelRetainsEndpointData : Type ℓ
    factorizedModelHasZeroPrimitiveGenericClass : Type ℓ
    complementaryModelRetainsPrimitiveGenericClass : Type ℓ
    complementaryEndpointComplexIsAcyclic : Type ℓ
    commonShortSupportRestrictionMatrixRemainsToBeConstructed : Type ℓ
    overlapHomotopyRemainsToBeConstructed : Type ℓ
    noHybridPhysicalMapClaimed : Type ℓ
