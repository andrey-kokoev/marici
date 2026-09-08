{-# OPTIONS --safe --cubical --guardedness #-}
module DGPyramidTCellLongStarComparison where

open import Cubical.Foundations.Prelude
open import Cubical.Data.Empty using (⊥)
open import DGPyramidTCellPyramid
open import DGPyramidTStemSideProduct

data LongStar : Type where
  star03 star14 star25 : LongStar

data StarPosition : Type where
  position1 position2 position3 position4 : StarPosition

record LongStarTriangle : Type where
  constructor star-triangle
  field
    star : LongStar
    firstShort secondShort : ShortDiagonal

longStarTriangle : LongStar → StarPosition → LongStarTriangle
longStarTriangle star03 position1 = star-triangle star03 d02 d04
longStarTriangle star03 position2 = star-triangle star03 d02 d35
longStarTriangle star03 position3 = star-triangle star03 d04 d13
longStarTriangle star03 position4 = star-triangle star03 d13 d35
longStarTriangle star14 position1 = star-triangle star14 d04 d13
longStarTriangle star14 position2 = star-triangle star14 d04 d24
longStarTriangle star14 position3 = star-triangle star14 d13 d15
longStarTriangle star14 position4 = star-triangle star14 d15 d24
longStarTriangle star25 position1 = star-triangle star25 d02 d24
longStarTriangle star25 position2 = star-triangle star25 d02 d35
longStarTriangle star25 position3 = star-triangle star25 d15 d24
longStarTriangle star25 position4 = star-triangle star25 d15 d35

record TCellLongStarComparisonCertificate {ℓ : Level} : Type (ℓ-suc ℓ) where
  field
    PairCell UniqueIncidentTriangle : Type ℓ
    pairCellToUniqueTriangle : PairCell → UniqueIncidentTriangle
    sixPairCellsMatchUniquely : Type ℓ

    SingletonCell MixedEdge TwoIncidentStars : Type ℓ
    singletonToMixedEdge : SingletonCell → MixedEdge
    incidentStars : MixedEdge → TwoIncidentStars
    sixSignedSingletonsRetainEdgeOrientation : Type ℓ
    singletonResidueNamesIncompatibleLong : Type ℓ

    CanonicalTwelveCellBijection : Type ℓ
    noCanonicalBijectionFromCurrentLabels : CanonicalTwelveCellBijection → ⊥
    IncidentStarChoice : Type ℓ
    chooseIncidentStar : IncidentStarChoice → SingletonCell → LongStar

    RowDifferential StarDifferential TotalDifferential : Type ℓ
    rowDifferential : RowDifferential
    starDifferential : StarDifferential
    totalDifferential : TotalDifferential
    AnticommutationAfterChoice : IncidentStarChoice → Type ℓ
    FourteenTriangleTotalCycleAfterChoice : IncidentStarChoice → Type ℓ

    PhysicalIncidentStarSelection : Type ℓ
