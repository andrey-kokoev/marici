{-# OPTIONS --safe --cubical --guardedness #-}
module DGPyramidRelativeTetrahedralQ where

open import Cubical.Foundations.Prelude
open import Cubical.Data.Empty using (⊥)
open import DGPyramidTetrahedralEndpointBoundary

-- Finite cellular proxy for the determinant-valued relative Q-manifold
-- (Pi T Delta^3, d).  Smooth realization is deliberately a separate datum.
record RelativeTetrahedralQ {ℓ : Level} : Type (ℓ-suc ℓ) where
  field
    Form BoundaryForm DeterminantLine : Type ℓ
    zeroForm : Form
    relativeQ : Form → Form
    relativeQSquared : (x : Form) → relativeQ (relativeQ x) ≡ zeroForm

    restrictToBoundary : Form → BoundaryForm
    realizationFace underdeterminationFace
      overpresentationFace coherenceFace : BoundaryForm

    tetrahedralResidue : Form
    overlapDiscrepancy : Form
    residueBoundary : relativeQ tetrahedralResidue ≡ overlapDiscrepancy
    discrepancyIsClosed : relativeQ overlapDiscrepancy ≡ zeroForm

    determinantFrame : DeterminantLine
    determinantLineIsNotEulerEvaluated : Type ℓ
    cellularToSmoothOddTangentRealization : Type ℓ

open RelativeTetrahedralQ public

-- Relative Stokes data.  On a manifold with boundary the bulk functional need
-- not be an absolute cyclic zero-cocycle: its Q-defect is the boundary
-- functional.  A physical cyclic trace must retain or cancel this term.
record RelativeCyclicTrace {ℓ : Level}
  (C : RelativeTetrahedralQ {ℓ}) : Type (ℓ-suc ℓ) where
  field
    TraceValue : Type ℓ
    zeroTrace : TraceValue
    bulkTrace : Form C → TraceValue
    boundaryTrace : BoundaryForm C → TraceValue
    stokes : (x : Form C) →
      bulkTrace (relativeQ C x) ≡ boundaryTrace (restrictToBoundary C x)

open RelativeCyclicTrace public

record PhysicalEndpointResidueReadout {ℓ : Level}
  (C : RelativeTetrahedralQ {ℓ}) : Type (ℓ-suc ℓ) where
  field
    EndpointObstruction : Type ℓ
    zeroObstruction oneOneObstruction : EndpointObstruction
    readout : Form C → EndpointObstruction
    discrepancyReadsOneOne :
      readout (overlapDiscrepancy C) ≡ oneOneObstruction
    zeroReadsZero : readout (zeroForm C) ≡ zeroObstruction
    oneOneIsNonzero : oneOneObstruction ≡ zeroObstruction → ⊥

open PhysicalEndpointResidueReadout public

-- The residue cannot already belong to the unchanged absolute Q-complex if
-- its Q-boundary has the nonzero endpoint readout.  It belongs to a relative
-- or augmented complex.
record AbsoluteResidueClaim {ℓ : Level}
  (C : RelativeTetrahedralQ {ℓ}) : Type (ℓ-suc ℓ) where
  field
    residueWouldBeQClosed :
      relativeQ C (tetrahedralResidue C) ≡ zeroForm C

noAbsoluteResidueWithOneOneBoundary : {ℓ : Level}
  (C : RelativeTetrahedralQ {ℓ})
  (R : PhysicalEndpointResidueReadout C) → AbsoluteResidueClaim C → ⊥
noAbsoluteResidueWithOneOneBoundary C R claim =
  oneOneIsNonzero R
    (sym (discrepancyReadsOneOne R) ∙
     cong (readout R)
       (sym (residueBoundary C) ∙
        AbsoluteResidueClaim.residueWouldBeQClosed claim) ∙
     zeroReadsZero R)

-- Exact realization gate connecting the cellular tetrahedron to the physical
-- hybrid comparison target.
record RelativeTetrahedralQRealization {ℓ : Level}
  (C : RelativeTetrahedralQ {ℓ}) : Type (ℓ-suc ℓ) where
  field
    PhysicalComparisonForm : Type ℓ
    cellularToPhysical : Form C → PhysicalComparisonForm
    physicalQ : PhysicalComparisonForm → PhysicalComparisonForm
    zeroPhysical : PhysicalComparisonForm
    mapPreservesQ : (x : Form C) →
      cellularToPhysical (relativeQ C x) ≡
      physicalQ (cellularToPhysical x)
    mapPreservesZero : cellularToPhysical (zeroForm C) ≡ zeroPhysical
    allFourFaceAssignmentsAreTyped : Type ℓ
    primitiveEndpointColumnIsRetained : Type ℓ
    primitiveGenericColumnIsRetained : Type ℓ
    productCartierAndDeterminantFramesAreRetained : Type ℓ
    operationAndDihedralCoherence : Type ℓ

record CurrentRelativeTetrahedralQAudit {ℓ : Level} : Type (ℓ-suc ℓ) where
  field
    cellularBoundaryModelIsAvailable : Type ℓ
    gradedDualTargetModelIsAvailable : Type ℓ
    relativeStokesInterpretationIsRequired : Type ℓ
    cellularToPhysicalMapRemainsUnconstructed : Type ℓ
    noSmoothQManifoldRealizationClaimed : Type ℓ
