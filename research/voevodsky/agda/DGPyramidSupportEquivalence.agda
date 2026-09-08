{-# OPTIONS --safe --cubical --guardedness #-}
module DGPyramidSupportEquivalence where

open import Cubical.Foundations.Prelude

-- Bounded interface for the computed pulled-back-normal/cellular equivalence.
-- Concrete packet types may contain all degreewise matrices and gradings.
record SupportPreservingEquivalenceCertificate {ℓ : Level}
  : Type (ℓ-suc ℓ) where
  field
    SourceComplex CellularComplex : Type ℓ
    SourceEndpoint SourceBoundary SourceQ : Type ℓ
    CellularEndpoint CellularBoundary CellularQ : Type ℓ

    sourceEndpointInclusion : SourceEndpoint → SourceComplex
    sourceBoundaryInclusion : SourceBoundary → SourceComplex
    cellularEndpointInclusion : CellularEndpoint → CellularComplex
    cellularBoundaryInclusion : CellularBoundary → CellularComplex
    sourceQProjection : SourceComplex → SourceQ
    cellularQProjection : CellularComplex → CellularQ

    comparison : SourceComplex → CellularComplex
    inverse : CellularComplex → SourceComplex
    sourceHomotopy : SourceComplex → SourceComplex

    -- Exact matrix equations are packet-defined because their component form
    -- depends on the concrete bounded complex representation.
    ComparisonIsChainMap : (SourceComplex → CellularComplex) → Type ℓ
    InverseIsChainMap : (CellularComplex → SourceComplex) → Type ℓ
    IsContraction :
      (SourceComplex → CellularComplex) →
      (CellularComplex → SourceComplex) →
      (SourceComplex → SourceComplex) → Type ℓ
    comparisonChainWitness : ComparisonIsChainMap comparison
    inverseChainWitness : InverseIsChainMap inverse
    contractionWitness : IsContraction comparison inverse sourceHomotopy

    endpointComparison : SourceEndpoint → CellularEndpoint
    boundaryComparison : SourceBoundary → CellularBoundary
    qComparison : SourceQ → CellularQ
    preservesEndpoint : (x : SourceEndpoint) →
      comparison (sourceEndpointInclusion x) ≡
      cellularEndpointInclusion (endpointComparison x)
    preservesBoundary : (x : SourceBoundary) →
      comparison (sourceBoundaryInclusion x) ≡
      cellularBoundaryInclusion (boundaryComparison x)
    inducesQComparison : (x : SourceComplex) →
      cellularQProjection (comparison x) ≡
      qComparison (sourceQProjection x)

    CorrectedHM CorrectedQ CellularHM CellularQChain : Type ℓ
    correctedHM : CorrectedHM
    correctedQ : CorrectedQ
    cellularHM : CellularHM
    cellularQChain : CellularQChain
    MorseEvaluation :
      CorrectedHM → CorrectedQ → CellularHM → CellularQChain → Type ℓ
    morseEvaluationWitness :
      MorseEvaluation correctedHM correctedQ cellularHM cellularQChain

    PreservesOccurrenceNormalReesGrading :
      (SourceComplex → CellularComplex) → Type ℓ
    gradingWitness : PreservesOccurrenceNormalReesGrading comparison

open SupportPreservingEquivalenceCertificate public

-- This certificate names the pulled-back-normal ordinary model only. No field
-- identifies it with the native-normal model or a physical supported dual.
