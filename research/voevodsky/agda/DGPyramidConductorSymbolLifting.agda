{-# OPTIONS --safe --cubical --guardedness #-}
module DGPyramidConductorSymbolLifting where

open import Cubical.Foundations.Prelude
open import Cubical.Data.Empty using (⊥)

record ConductorSymbolLiftingCertificate {ℓ : Level}
  : Type (ℓ-suc ℓ) where
  field
    FirstSymbol QuadraticObstruction FullLift : Type ℓ
    includeLiftSymbol : FullLift → FirstSymbol
    quadraticDefect : FirstSymbol → QuadraticObstruction
    zeroObstruction : QuadraticObstruction
    liftHasZeroDefect : (l : FullLift) →
      quadraticDefect (includeLiftSymbol l) ≡ zeroObstruction

    Compatible : FirstSymbol → Type ℓ
    compatibleMeansZero : (j : FirstSymbol) →
      Compatible j → quadraticDefect j ≡ zeroObstruction
    liftCompatible : (j : FirstSymbol) → Compatible j → FullLift
    liftHasRequestedSymbol : (j : FirstSymbol) (p : Compatible j) →
      includeLiftSymbol (liftCompatible j p) ≡ j
    liftUnique : (j : FirstSymbol) (p : Compatible j) (l : FullLift) →
      includeLiftSymbol l ≡ j → l ≡ liftCompatible j p

    Rank134FirstSymbols Rank74Obstructions Rank60FullLifts : Type ℓ
    rank134Witness : Rank134FirstSymbols
    rank74Witness : Rank74Obstructions
    rank60Witness : Rank60FullLifts
    SaturatedExact6013474 : Type ℓ
    saturatedExactWitness : SaturatedExact6013474
    noHigherConductorCorrectionInGrade : Type ℓ
    noDegreeFourIdentification : Type ℓ

    DihedralFamily ReflectionInvariant : Type ℓ
    transportOccurrenceOrbit : FullLift → DihedralFamily
    invariantFirstSymbols invariantFullLifts invariantObstructions : Type ℓ
    Rank59InvariantSymbols Rank25EquivariantLifts Rank34InvariantObstructions : Type ℓ
    rank59Witness : Rank59InvariantSymbols
    rank25Witness : Rank25EquivariantLifts
    rank34Witness : Rank34InvariantObstructions

    OrdinaryVisible PrimaryHomotopyOnly : Type ℓ
    SixteenOrdinaryVisible NinePrimaryHomotopyOnly : Type ℓ
    sixteenWitness : SixteenOrdinaryVisible
    nineWitness : NinePrimaryHomotopyOnly

    InvariantDefect OrdinaryPreimage DoubledInvariantPreimage : Type ℓ
    invariantDefect : InvariantDefect
    ordinaryPreimage : OrdinaryPreimage
    doubledInvariantPreimage : DoubledInvariantPreimage
    InvariantPreimage : InvariantDefect → Type ℓ
    noInvariantIntegralPreimage : InvariantPreimage invariantDefect → ⊥
    IndexTwoInvariantCokernel : Type ℓ
    indexTwoWitness : IndexTwoInvariantCokernel
    reflectionDefectIsPrimaryHomotopyOnly : Type ℓ

    ScalarConormalSymbol ChainValuedSymbol : Type ℓ
    scalarConormalSymbol : ScalarConormalSymbol
    CompleteChainPlacement : ScalarConormalSymbol → ChainValuedSymbol → Type ℓ
    scalarSymbolDoesNotSelectChainPlacement : Type ℓ

    PhysicalChainValuedConductorSymbol : Type ℓ
    PhysicalQuadraticCompatibility : PhysicalChainValuedConductorSymbol → Type ℓ
    PhysicalDihedralTransportCompatibility :
      PhysicalChainValuedConductorSymbol → Type ℓ
    PhysicalIntegralInvariantChoice :
      PhysicalChainValuedConductorSymbol → Type ℓ
