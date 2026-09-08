{-# OPTIONS --safe --cubical --guardedness #-}
module DGPyramidPolarityStarSelection where

open import Cubical.Foundations.Prelude
open import Cubical.Data.Empty using (⊥)
open import DGPyramidTCellPyramid
open import DGPyramidTCellLongStarComparison

data RotationOrbitChoice : Type where
  firstOrbitChoice secondOrbitChoice : RotationOrbitChoice

data SingletonPolarity : Type where
  positiveSingleton negativeSingleton : SingletonPolarity

record PolarityStarSelectionCertificate {ℓ : Level} : Type (ℓ-suc ℓ) where
  field
    MixedEdge IncidentStar SignedSingletonCell : Type ℓ
    signedSingletonEdge : SignedSingletonCell → MixedEdge
    firstIncidentStar secondIncidentStar : MixedEdge → IncidentStar

    rotationChoice : RotationOrbitChoice
    selectedStar : SignedSingletonCell → IncidentStar
    positiveSelectionRotationEquivariant : Type ℓ
    negativeSelectsOppositeIncidentStar : Type ℓ
    allSixSingletonTrianglesDetermined : Type ℓ

    RotationEquivariantSelection : Type ℓ
    firstRotationChoice secondRotationChoice : RotationEquivariantSelection
    exactlyTwoRotationEquivariantChoices : Type ℓ

    ReflectionActionOnLongStars : Type ℓ
    reflectionAction : ReflectionActionOnLongStars
    ReflectionCoherent : RotationEquivariantSelection → Type ℓ
    reflectionIsDecidingGate : Type ℓ

    PairCellTriangle SingletonCellTriangle : Type ℓ
    sixPairTriangles : PairCellTriangle
    sixSingletonTriangles : SingletonCellTriangle
    LabelledTwelveByTwelveBijection : Type ℓ
    bijectionAfterReflectionChoice :
      (c : RotationEquivariantSelection) → ReflectionCoherent c →
      LabelledTwelveByTwelveBijection

    RowDifferential StarDifferential : Type ℓ
    Anticommute : LabelledTwelveByTwelveBijection → Type ℓ
    FourteenTriangleTotalCycle : LabelledTwelveByTwelveBijection → Type ℓ

    PhysicalPolarityStarChoice : Type ℓ
