{-# OPTIONS --safe --cubical --guardedness #-}
module DGPyramidTStemSideProduct where

open import Cubical.Foundations.Prelude
open import Cubical.Data.Empty using (⊥)
open import DGPyramidTCellPyramid

data SideProductKind : Type where
  crossSheet sameSheet : SideProductKind

stemProductKind : TRow → SideProductKind
stemProductKind +singleton = crossSheet
stemProductKind -singleton = crossSheet
stemProductKind +pair = sameSheet
stemProductKind -pair = sameSheet

record SideEdgePair : Type where
  constructor side-pair
  field
    left right : ShortDiagonal

stemSidePair : TRow → TColumn → SideEdgePair
stemSidePair +singleton first  = side-pair d02 d35
stemSidePair +singleton second = side-pair d04 d13
stemSidePair +singleton third  = side-pair d24 d15
stemSidePair +pair first  = side-pair d02 d04
stemSidePair +pair second = side-pair d02 d24
stemSidePair +pair third  = side-pair d04 d24
stemSidePair -singleton first  = side-pair d13 d04
stemSidePair -singleton second = side-pair d15 d24
stemSidePair -singleton third  = side-pair d35 d02
stemSidePair -pair first  = side-pair d13 d15
stemSidePair -pair second = side-pair d13 d35
stemSidePair -pair third  = side-pair d15 d35

record TStemSideProductCertificate {ℓ : Level} : Type (ℓ-suc ℓ) where
  field
    SideEdge StemCoefficient StemBoundary EndpointDiscrepancy : Type ℓ
    sideEdge : ShortDiagonal → SideEdge
    multiplySideEdges : SideEdge → SideEdge → StemCoefficient
    stemCoefficient : TRow → TColumn → StemCoefficient
    stemFactorization : (r : TRow) (c : TColumn) →
      let p = stemSidePair r c in
      stemCoefficient r c ≡
        multiplySideEdges (sideEdge (SideEdgePair.left p))
                          (sideEdge (SideEdgePair.right p))

    stemBoundary : TRow → TColumn → StemBoundary
    boundaryResidueCompatibility : (r : TRow) (c : TColumn) → Type ℓ

    MixedNormalProductGenerator : Type ℓ
    mixedGenerator : TColumn → MixedNormalProductGenerator
    singletonStemToMixedGenerator :
      (r : TRow) → stemProductKind r ≡ crossSheet →
      TColumn → MixedNormalProductGenerator

    UniformMixedIdealIdentification : Type ℓ
    noUniformMixedIdealIdentification : UniformMixedIdealIdentification → ⊥
    pairRowsUseSameSheetProducts : Type ℓ

    EighteenRelationDiscrepancies : Type ℓ
    eighteenDiscrepanciesWitness : EighteenRelationDiscrepancies
    discrepancy : EndpointDiscrepancy
    higherSyzygyCoherence : Type ℓ
    TBoundaryEqualsMultiplierDiscrepancy : Type ℓ

    FourToTwoToOneSideProductDescent : Type ℓ
    PhysicalSideEdgeComposition : Type ℓ
