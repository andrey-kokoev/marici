{-# OPTIONS --safe --cubical --guardedness #-}
module DGPyramidNextEvaluationShiftTest where

open import Cubical.Foundations.Prelude
open import Cubical.Data.Empty using (⊥)

-- The target-side marked-normal calculation and the physical endpoint
-- obstruction live in separately typed groups.  Equality of their coordinate
-- vectors is deliberately insufficient.
record NextEvaluationShiftData {ℓ : Level} : Type (ℓ-suc ℓ) where
  field
    MarkedNormalClass PhysicalEndpointObstruction : Type ℓ
    TargetEndpointBoundary PhysicalComparison : Type ℓ

    nextMarkedNormalClass : MarkedNormalClass
    physicalOneOneObstruction : PhysicalEndpointObstruction
    targetEndpointBoundary : MarkedNormalClass → TargetEndpointBoundary
    physicalComparison : TargetEndpointBoundary → PhysicalEndpointObstruction

    targetBoundaryIsPrimitiveDiagonal : Type ℓ
    targetBoundaryIsDihedrallyInvariant : Type ℓ
    targetBoundaryHasEighteenTermRepresentative : Type ℓ

open NextEvaluationShiftData public

-- This is the decisive typed test.  It cannot be inhabited merely from the
-- two independently computed coordinate vectors (1,1).
record NextEvaluationShiftWitness {ℓ : Level}
  (D : NextEvaluationShiftData {ℓ}) : Type (ℓ-suc ℓ) where
  field
    comparisonSendsBoundaryToPhysicalObstruction :
      physicalComparison D (targetEndpointBoundary D (nextMarkedNormalClass D))
        ≡ physicalOneOneObstruction D
    degreeAndInternalWeightMatch : Type ℓ
    supportAndDeterminantLinesMatch : Type ℓ
    relativeOperationBarActionMatches : Type ℓ
    dihedralTransportMatches : Type ℓ

-- A mismatch after the actual comparison is constructed decisively falsifies
-- the proposed next-evaluation interpretation.
record NextEvaluationShiftFalsification {ℓ : Level}
  (D : NextEvaluationShiftData {ℓ}) : Type (ℓ-suc ℓ) where
  field
    comparedBoundaryMismatch :
      physicalComparison D (targetEndpointBoundary D (nextMarkedNormalClass D))
        ≡ physicalOneOneObstruction D → ⊥

witnessExcludesBoundaryMismatch : {ℓ : Level}
  (D : NextEvaluationShiftData {ℓ}) →
  NextEvaluationShiftWitness D → NextEvaluationShiftFalsification D → ⊥
witnessExcludesBoundaryMismatch D witness falsification =
  NextEvaluationShiftFalsification.comparedBoundaryMismatch falsification
    (NextEvaluationShiftWitness.comparisonSendsBoundaryToPhysicalObstruction witness)

-- Current audit: the target-side diagonal test passes, while the comparison
-- from the long marked-normal boundary to the independently framed physical
-- endpoint mapping complex remains an explicit missing datum.
record CurrentNextEvaluationAudit {ℓ : Level} : Type (ℓ-suc ℓ) where
  field
    Data : NextEvaluationShiftData {ℓ}
    targetSideDiagonalTestPassed : Type ℓ
    targetSideTestDoesNotConstructPhysicalComparison : Type ℓ
    longNormalAndEndpointConormalFramesRemainDistinct : Type ℓ
    productCartierSourceMustBeRetained : Type ℓ
    noWitnessOrFalsificationBeforeTypedComparison : Type ℓ
