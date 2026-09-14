{-# OPTIONS --safe --cubical --guardedness #-}
module DGPyramidDerivedCyclicBridgeTest where

open import Cubical.Foundations.Prelude
open import Cubical.Data.Empty using (⊥)
open import DGPyramidTetrahedralEndpointBoundary
open import DGPyramidReflectedConormalButterfly using (ChainTarget)
import DGPyramidReflectedConormalButterfly as Butterfly

-- Minimal interface for testing a Q/derived-cyclic route.  This does not claim
-- that the physical collar already carries a Q-manifold structure.
record CollarQComplex {ℓ : Level} : Type (ℓ-suc ℓ) where
  field
    Carrier : Type ℓ
    zero : Carrier
    homologicalVectorField : Carrier → Carrier
    homologicalVectorFieldSquared : (x : Carrier) →
      homologicalVectorField (homologicalVectorField x) ≡ zero

open CollarQComplex public

-- Section 2.4/3.4 of Bruce requires separate compatible homological vector
-- fields to anticommute.  For a cyclic zero-cocycle, closure of the pencil is
-- equivalent to closure in each direction separately.
record DoubleCollarQComplex {ℓ : Level} : Type (ℓ-suc ℓ) where
  field
    Carrier : Type ℓ
    zero : Carrier
    negate : Carrier → Carrier
    firstQ secondQ : Carrier → Carrier
    firstQSquared : (x : Carrier) → firstQ (firstQ x) ≡ zero
    secondQSquared : (x : Carrier) → secondQ (secondQ x) ≡ zero
    -- For odd Q-fields, [Q1,Q2]=0 means Q1 Q2 = -(Q2 Q1).
    QsAnticommute : (x : Carrier) →
      firstQ (secondQ x) ≡ negate (secondQ (firstQ x))

record DoubleQClosedTrace {ℓ : Level}
  (C : DoubleCollarQComplex {ℓ}) : Type (ℓ-suc ℓ) where
  field
    TraceValue : Type ℓ
    zeroTrace : TraceValue
    trace : DoubleCollarQComplex.Carrier C → TraceValue
    firstClosure : (x : DoubleCollarQComplex.Carrier C) →
      trace (DoubleCollarQComplex.firstQ C x) ≡ zeroTrace
    secondClosure : (x : DoubleCollarQComplex.Carrier C) →
      trace (DoubleCollarQComplex.secondQ C x) ≡ zeroTrace

-- Every already constructed total chain target supplies a coefficient-side
-- Q-complex: its chain differential is the homological vector field.
chainTargetAsQComplex : {ℓ : Level} → ChainTarget {ℓ} → CollarQComplex {ℓ}
chainTargetAsQComplex C = record
  { Carrier = Butterfly.ChainTarget.Carrier C
  ; zero = Butterfly.ChainTarget.zeroCarrier C
  ; homologicalVectorField = Butterfly.ChainTarget.differential C
  ; homologicalVectorFieldSquared =
      Butterfly.ChainTarget.differentialSquaresToZero C
  }

record DerivedCyclicTraceCandidate {ℓ : Level}
  (C : CollarQComplex {ℓ}) : Type (ℓ-suc ℓ) where
  field
    TraceValue DeformationParameter CyclicObstruction : Type ℓ
    zeroTrace : TraceValue
    trace : Carrier C → TraceValue
    traceIsQClosed : (x : Carrier C) →
      trace (homologicalVectorField C x) ≡ zeroTrace
    deformationObstruction : DeformationParameter → CyclicObstruction

open DerivedCyclicTraceCandidate public

-- A useful P24-style route must produce a covariant, determinant-retaining map
-- from its cyclic obstruction to the already typed endpoint obstruction.
record DerivedCyclicPhysicalBridge {ℓ : Level}
  {T : TetrahedralEndpointBoundary {ℓ}}
  (R : TetrahedralEndpointReadout T)
  (C : CollarQComplex {ℓ})
  (Trace : DerivedCyclicTraceCandidate C) : Type (ℓ-suc ℓ) where
  field
    physicalDeformation : DeformationParameter Trace
    cyclicToPhysical : CyclicObstruction Trace →
      TetrahedralEndpointReadout.PhysicalEndpointObstruction R
    obstructionHitsOneOne :
      cyclicToPhysical (deformationObstruction Trace physicalDeformation)
        ≡ oneOneObstruction R
    covarianceIsNotContravariantRHomSubstitution : Type ℓ
    endpointDeterminantLineIsRetained : Type ℓ
    productCartierSourceIsRetained : Type ℓ
    relativeOperationBarCompatibility : Type ℓ
    decomposableDihedralCompatibility : Type ℓ

-- Any cyclic construction whose physical readout factors through the existing
-- null Euler comparison fails before operation or symmetry tests are needed.
record EulerFactoringCyclicRoute {ℓ : Level}
  {T : TetrahedralEndpointBoundary {ℓ}}
  (R : TetrahedralEndpointReadout T)
  (C : CollarQComplex {ℓ})
  (Trace : DerivedCyclicTraceCandidate C) : Type (ℓ-suc ℓ) where
  field
    physicalDeformation : DeformationParameter Trace
    cyclicReadout : CyclicObstruction Trace →
      TetrahedralEndpointReadout.PhysicalEndpointObstruction R
    cyclicReadoutIsNull : (x : CyclicObstruction Trace) →
      cyclicReadout x ≡ zeroObstruction R

open EulerFactoringCyclicRoute public

EulerFactoringRouteHitsOneOne : {ℓ : Level}
  {T : TetrahedralEndpointBoundary {ℓ}}
  (R : TetrahedralEndpointReadout T)
  (C : CollarQComplex {ℓ})
  (Trace : DerivedCyclicTraceCandidate C)
  (Route : EulerFactoringCyclicRoute R C Trace) → Type ℓ
EulerFactoringRouteHitsOneOne R C Trace Route =
  cyclicReadout Route
    (deformationObstruction Trace (physicalDeformation Route))
      ≡ oneOneObstruction R

noEulerFactoringDerivedCyclicBridge : {ℓ : Level}
  {T : TetrahedralEndpointBoundary {ℓ}}
  (R : TetrahedralEndpointReadout T)
  (C : CollarQComplex {ℓ})
  (Trace : DerivedCyclicTraceCandidate C)
  (Route : EulerFactoringCyclicRoute R C Trace) →
  EulerFactoringRouteHitsOneOne R C Trace Route → ⊥
noEulerFactoringDerivedCyclicBridge R C Trace Route hits =
  oneOneIsNonzero R
    (sym hits ∙ cyclicReadoutIsNull Route
      (deformationObstruction Trace (physicalDeformation Route)))

-- Current outcome of the narrow test: the known two-grade trace suggests the
-- trace slot, but no Q on the complete collar and no cyclic-to-physical map are
-- presently constructed.  P24 therefore supplies a testable route, not yet an
-- inhabitant of the bridge.
record CurrentDerivedCyclicAudit {ℓ : Level} : Type (ℓ-suc ℓ) where
  field
    coefficientTotalDifferentialSuppliesPartialQStructure : Type ℓ
    twoGradeTraceIsClosedForResolvedChainAndNormalizationDifferential : Type ℓ
    completePhysicalCollarQStructureRemainsUnconstructed : Type ℓ
    rawDualityTargetRelativeOperationActionRemainsUnconstructed : Type ℓ
    operationBarClosureOfTwoGradeTraceRemainsUntested : Type ℓ
    compatibleMultiQAnticommutationMustBeChecked : Type ℓ
    derivedProductIsNonunitalAndMustNotBeIdentifiedWithRelativeAlgebra : Type ℓ
    cyclicDeformationClassMustBeComputed : Type ℓ
    cyclicToPhysicalMapRemainsUnconstructed : Type ℓ
    EulerFactoringRouteIsExcluded : Type ℓ
