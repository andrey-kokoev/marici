{-# OPTIONS --safe --cubical --guardedness #-}
module DGPyramidTetrahedralEndpointBoundary where

open import Cubical.Foundations.Prelude
open import Cubical.Data.Empty using (⊥)
open import DGPyramidNextEvaluationShiftTest

-- Four vertices organize the four comparison modes.  The six edges and four
-- triangular faces are actual paths; no tetrahedral filler is assumed.
record TetrahedralEndpointBoundary {ℓ : Level} : Type (ℓ-suc ℓ) where
  field
    ComparisonSpace : Type ℓ
    realization underdetermination overpresentation coherence : ComparisonSpace

    realization-underdetermination : realization ≡ underdetermination
    realization-overpresentation : realization ≡ overpresentation
    realization-coherence : realization ≡ coherence
    underdetermination-overpresentation : underdetermination ≡ overpresentation
    underdetermination-coherence : underdetermination ≡ coherence
    overpresentation-coherence : overpresentation ≡ coherence

    realization-underdetermination-overpresentation :
      realization-underdetermination ∙ underdetermination-overpresentation
        ≡ realization-overpresentation
    realization-underdetermination-coherence :
      realization-underdetermination ∙ underdetermination-coherence
        ≡ realization-coherence
    realization-overpresentation-coherence :
      realization-overpresentation ∙ overpresentation-coherence
        ≡ realization-coherence
    underdetermination-overpresentation-coherence :
      underdetermination-overpresentation ∙ overpresentation-coherence
        ≡ underdetermination-coherence

open TetrahedralEndpointBoundary public

-- The two routes across the tetrahedral boundary give a based loop.  A closed
-- tetrahedron requires a higher equality between the induced face coherences,
-- not merely agreement of their endpoint coordinates.
tetrahedralBoundaryLoop : {ℓ : Level} →
  (T : TetrahedralEndpointBoundary {ℓ}) →
  realization T ≡ realization T
tetrahedralBoundaryLoop T =
  realization-underdetermination T ∙
  underdetermination-overpresentation T ∙
  overpresentation-coherence T ∙
  sym (realization-coherence T)

record TetrahedralEndpointReadout {ℓ : Level}
  (T : TetrahedralEndpointBoundary {ℓ}) : Type (ℓ-suc ℓ) where
  field
    PhysicalEndpointObstruction : Type ℓ
    zeroObstruction oneOneObstruction : PhysicalEndpointObstruction
    boundaryReadout : realization T ≡ realization T → PhysicalEndpointObstruction
    tetrahedralBoundaryIsOneOne :
      boundaryReadout (tetrahedralBoundaryLoop T) ≡ oneOneObstruction
    constantBoundaryIsZero : boundaryReadout refl ≡ zeroObstruction
    oneOneIsNonzero : oneOneObstruction ≡ zeroObstruction → ⊥

open TetrahedralEndpointReadout public

TetrahedralFiller : {ℓ : Level} →
  (T : TetrahedralEndpointBoundary {ℓ}) → Type ℓ
TetrahedralFiller T = tetrahedralBoundaryLoop T ≡ refl

-- The visible diagonal obstruction excludes a filler in the unchanged
-- comparison space.
noCurrentTetrahedralFiller : {ℓ : Level}
  (T : TetrahedralEndpointBoundary {ℓ})
  (R : TetrahedralEndpointReadout T) → TetrahedralFiller T → ⊥
noCurrentTetrahedralFiller T R filler =
  oneOneIsNonzero R
    (sym (tetrahedralBoundaryIsOneOne R) ∙
     cong (boundaryReadout R) filler ∙
     constantBoundaryIsZero R)

-- A marked-normal cell is a candidate filler only after an actual typed map
-- carries its boundary into this comparison space and matches all structures.
record MarkedNormalTetrahedralFiller {ℓ : Level}
  (T : TetrahedralEndpointBoundary {ℓ})
  (R : TetrahedralEndpointReadout T)
  (Shift : NextEvaluationShiftData {ℓ}) : Type (ℓ-suc ℓ) where
  field
    markedNormalBoundaryToComparisonLoop :
      TargetEndpointBoundary Shift → realization T ≡ realization T
    boundaryMapSendsCandidateToTetrahedralBoundary :
      markedNormalBoundaryToComparisonLoop
        (targetEndpointBoundary Shift (nextMarkedNormalClass Shift))
        ≡ tetrahedralBoundaryLoop T
    physicalObstructionBridge :
      NextEvaluationShiftData.PhysicalEndpointObstruction Shift →
      TetrahedralEndpointReadout.PhysicalEndpointObstruction R
    physicalReadoutsAgree :
      boundaryReadout R
        (markedNormalBoundaryToComparisonLoop
          (targetEndpointBoundary Shift (nextMarkedNormalClass Shift)))
        ≡ physicalObstructionBridge
          (physicalComparison Shift
            (targetEndpointBoundary Shift (nextMarkedNormalClass Shift)))
    degreeWeightSupportAndDeterminantsMatch : Type ℓ
    operationBarCoherenceCloses : Type ℓ
    dihedralCoherenceCloses : Type ℓ

-- This audit records exactly how far the current coefficient calculations go.
-- It does not turn coordinate agreement into a geometric edge map.
record CurrentTetrahedralAudit {ℓ : Level} : Type (ℓ-suc ℓ) where
  field
    Boundary : TetrahedralEndpointBoundary {ℓ}
    Readout : TetrahedralEndpointReadout Boundary
    Shift : NextEvaluationShiftData {ℓ}
    coefficientFacesAndTheirHomotopiesAreAvailable : Type ℓ
    markedNormalBoundaryHasPrimitiveDiagonalCoordinates : Type ℓ
    physicalRealizationEdgeRemainsUnconstructed : Type ℓ
    noMarkedNormalFillerClaimed : Type ℓ

-- The only presently constructed comparison from the independently framed
-- endpoint source evaluates its conormal line by the Euler section.  Its
-- induced obstruction map is null.  Therefore that canonical comparison
-- cannot be the missing physical edge.
record EulerEvaluatedBridgeAudit {ℓ : Level}
  (T : TetrahedralEndpointBoundary {ℓ})
  (R : TetrahedralEndpointReadout T) : Type (ℓ-suc ℓ) where
  field
    EulerBridgeInput : Type ℓ
    markedNormalBoundaryInput : EulerBridgeInput
    eulerBridge : EulerBridgeInput →
      TetrahedralEndpointReadout.PhysicalEndpointObstruction R
    eulerBridgeIsNull : (x : EulerBridgeInput) → eulerBridge x ≡ zeroObstruction R

open EulerEvaluatedBridgeAudit public

EulerBridgeHitsOneOne : {ℓ : Level}
  {T : TetrahedralEndpointBoundary {ℓ}}
  (R : TetrahedralEndpointReadout T)
  (E : EulerEvaluatedBridgeAudit T R) → Type ℓ
EulerBridgeHitsOneOne R E =
  eulerBridge E (markedNormalBoundaryInput E) ≡ oneOneObstruction R

-- Decisive narrow falsification of the currently available bridge.  It does
-- not exclude an extraordinary or mixed-variance physical comparison.
noEulerEvaluatedTetrahedralBridge : {ℓ : Level}
  {T : TetrahedralEndpointBoundary {ℓ}}
  (R : TetrahedralEndpointReadout T)
  (E : EulerEvaluatedBridgeAudit T R) → EulerBridgeHitsOneOne R E → ⊥
noEulerEvaluatedTetrahedralBridge R E hits =
  oneOneIsNonzero R
    (sym hits ∙ eulerBridgeIsNull E (markedNormalBoundaryInput E))
