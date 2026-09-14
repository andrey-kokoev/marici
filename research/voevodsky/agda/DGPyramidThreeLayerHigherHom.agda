{-# OPTIONS --safe --cubical --guardedness #-}
module DGPyramidThreeLayerHigherHom where

open import Cubical.Foundations.Prelude

-- Three nested categorical levels.  The maps and the nullhomotopy are data;
-- they are not generated from the names of the levels.
record ThreeLayerHigherHom {ℓ : Level} : Type (ℓ-suc ℓ) where
  field
    PhysicalHom ControlHom CyclicCochains : Type ℓ
    zeroPhysical : PhysicalHom
    zeroControl : ControlHom
    zeroCyclic : CyclicCochains

    physicalDifferential : PhysicalHom → PhysicalHom
    controlDifferential : ControlHom → ControlHom
    cyclicDifferential : CyclicCochains → CyclicCochains

    physicalDifferentialSquared : (x : PhysicalHom) →
      physicalDifferential (physicalDifferential x) ≡ zeroPhysical
    controlDifferentialSquared : (x : ControlHom) →
      controlDifferential (controlDifferential x) ≡ zeroControl
    cyclicDifferentialSquared : (x : CyclicCochains) →
      cyclicDifferential (cyclicDifferential x) ≡ zeroCyclic

    realizationToControl : PhysicalHom → ControlHom
    controlToTraceDeformation : ControlHom → CyclicCochains
    firstMapIsChainMap : (x : PhysicalHom) →
      controlDifferential (realizationToControl x) ≡
      realizationToControl (physicalDifferential x)
    secondMapIsChainMap : (x : ControlHom) →
      cyclicDifferential (controlToTraceDeformation x) ≡
      controlToTraceDeformation (controlDifferential x)

    CompositeHomotopy : Type ℓ
    zeroCompositeHomotopy : CompositeHomotopy
    compositeHomotopyBoundary : CompositeHomotopy →
      PhysicalHom → CyclicCochains
    traceCompatibilityHomotopy : CompositeHomotopy
    compositeIsItsBoundary : (x : PhysicalHom) →
      compositeHomotopyBoundary traceCompatibilityHomotopy x ≡
      controlToTraceDeformation (realizationToControl x)

    TotalCarrier : Type ℓ
    totalDifferential : TotalCarrier → TotalCarrier
    zeroTotal : TotalCarrier
    totalDifferentialSquared : (x : TotalCarrier) →
      totalDifferential (totalDifferential x) ≡ zeroTotal
    totalDifferentialUsesBothMapsAndCompositeHomotopy : Type ℓ

open ThreeLayerHigherHom public

-- The vertical three-level differential must commute, with totalization signs,
-- with each of the four transverse directions.  This is the actual 3 x 4 gate.
record ThreeLayerFourModeCompatibility {ℓ : Level}
  (H : ThreeLayerHigherHom {ℓ}) : Type (ℓ-suc ℓ) where
  field
    RealizationDirection UnderdeterminationDirection
      OverpresentationDirection CoherenceDirection : Type ℓ
    physicalRowHasFourActions : Type ℓ
    controlRowHasFourActions : Type ℓ
    cyclicRowHasFourActions : Type ℓ
    realizationToControlIntertwinesAllFour : Type ℓ
    controlToTraceIntertwinesAllFour : Type ℓ
    compositeHomotopyIsFourModeCoherent : Type ℓ
    allVerticalHorizontalMixedSquaresClose : Type ℓ

-- P24 uses real nuclear Frechet spaces, while the physical coefficient problem
-- is integral and detects torsion.  This comparison must be explicit.
record CyclicCoefficientChangeGate {ℓ : Level} : Type (ℓ-suc ℓ) where
  field
    IntegralControl RealCompletedControl : Type ℓ
    baseChangeAndCompletion : IntegralControl → RealCompletedControl
    determinantLineSurvivesBaseChange : Type ℓ
    primitiveOneOneClassSurvivesBaseChange : Type ℓ
    IntegralTorsion : Type ℓ
    torsionInformationLostOverReals : Type ℓ
    noIntegralClassificationInferredFromRealCyclicCohomology : Type ℓ

record CurrentThreeLayerHigherHomAudit {ℓ : Level} : Type (ℓ-suc ℓ) where
  field
    physicalHomRowIsSpecified : Type ℓ
    controlHomRowIsSpecifiedForCoefficientCandidate : Type ℓ
    cyclicRowFormulaIsSpecifiedByDerivedCyclicTheory : Type ℓ
    firstVerticalMapAwaitsPhysicalChiAndTau : Type ℓ
    secondVerticalMapAwaitsPhysicalQAndTraceDeformation : Type ℓ
    compositeNullhomotopyRemainsUnconstructed : Type ℓ
    noThreeLayerTotalComplexInhabitantClaimed : Type ℓ
