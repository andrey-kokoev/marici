{-# OPTIONS --safe --cubical --guardedness #-}
module DGPyramidTCellPyramid where

open import Cubical.Foundations.Prelude
open import Cubical.Data.Empty using (⊥)

-- The four rows are sheet × cardinality of the proper nonempty inactive face.
data TRow : Type where
  +singleton +pair -singleton -pair : TRow

data TColumn : Type where
  first second third : TColumn

data ShortDiagonal : Type where
  d02 d04 d13 d15 d24 d35 : ShortDiagonal

data LongDiagonal : Type where
  d03 d14 d25 : LongDiagonal

data InactiveFace : Type where
  singleton : ShortDiagonal → InactiveFace
  pair : ShortDiagonal → ShortDiagonal → InactiveFace

data ResidueMonomial : Type where
  residue₁ : LongDiagonal → ShortDiagonal → ShortDiagonal → ResidueMonomial
  residue₂ : LongDiagonal → LongDiagonal → ShortDiagonal → ShortDiagonal → ResidueMonomial

inactiveFace : TRow → TColumn → InactiveFace
inactiveFace +singleton first  = singleton d02
inactiveFace +singleton second = singleton d04
inactiveFace +singleton third  = singleton d24
inactiveFace +pair first  = pair d02 d04
inactiveFace +pair second = pair d02 d24
inactiveFace +pair third  = pair d04 d24
inactiveFace -singleton first  = singleton d13
inactiveFace -singleton second = singleton d15
inactiveFace -singleton third  = singleton d35
inactiveFace -pair first  = pair d13 d15
inactiveFace -pair second = pair d13 d35
inactiveFace -pair third  = pair d15 d35

-- Exact numerator and denominator labels from the twelve-residue table.
residueCoordinate : TRow → TColumn → ResidueMonomial
residueCoordinate +singleton first  = residue₁ d14 d02 d35
residueCoordinate +singleton second = residue₁ d25 d04 d13
residueCoordinate +singleton third  = residue₁ d03 d24 d15
residueCoordinate +pair first  = residue₂ d14 d25 d02 d04
residueCoordinate +pair second = residue₂ d03 d14 d02 d24
residueCoordinate +pair third  = residue₂ d03 d25 d04 d24
residueCoordinate -singleton first  = residue₁ d25 d13 d04
residueCoordinate -singleton second = residue₁ d03 d15 d24
residueCoordinate -singleton third  = residue₁ d14 d35 d02
residueCoordinate -pair first  = residue₂ d03 d25 d13 d15
residueCoordinate -pair second = residue₂ d14 d25 d13 d35
residueCoordinate -pair third  = residue₂ d03 d14 d15 d35

record TypedTCell {ℓ : Level} : Type (ℓ-suc ℓ) where
  field
    EdgeSource EdgeTarget : Type ℓ
    edge : EdgeSource → EdgeTarget
    HomotopyClass : Type ℓ
    homotopyClass : HomotopyClass
    HomotopyDegree : Type ℓ
    homotopyDegree : HomotopyDegree
    Support : Type ℓ
    support : Support
    ResidueQuotient : Type ℓ
    residueClass : ResidueQuotient

record TCellPyramidCertificate {ℓ : Level} : Type (ℓ-suc ℓ) where
  field
    cell : TRow → TColumn → TypedTCell {ℓ}
    transitionBoundary : TRow → TColumn → Type ℓ
    boundaryWitness : (r : TRow) (c : TColumn) → transitionBoundary r c

    CechCocycle DescentClass : Type ℓ
    assembleTwelveBoundaries :
      ((r : TRow) (c : TColumn) → transitionBoundary r c) → CechCocycle
    descentClass : DescentClass
    classOfCocycle : CechCocycle → DescentClass
    assembledClassEquation :
      classOfCocycle (assembleTwelveBoundaries boundaryWitness) ≡ descentClass

    zeroDescent : DescentClass
    descentNonzero : descentClass ≡ zeroDescent → ⊥
    LabelledQuotientsRemainDistinct : Type ℓ
    labelledQuotientsWitness : LabelledQuotientsRemainDistinct

    -- This is the still-open geometric gate: algebraic residues must be the
    -- boundaries of the proposed physical edge/homotopy cells.
    PhysicalTCellCorrespondence : Type ℓ
