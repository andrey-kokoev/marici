{-# OPTIONS --safe --cubical --guardedness #-}
module DGPyramidEndpointNormalCube where

open import Cubical.Foundations.Prelude
open import Cubical.Data.Empty using (⊥)

-- Target-side continuation through the six short-normal directions.
record EndpointNormalCubeCertificate {ℓ : Level} : Type (ℓ-suc ℓ) where
  field
    ShortSupport : Type ℓ
    emptySupport fullSupport oddBranch evenBranch : ShortSupport
    addNormal : ShortSupport → ShortSupport → ShortSupport

    RelativeComplex RemainingFaceCochains Stabilizer : ShortSupport → Type ℓ
    reduceToFaces : (P : ShortSupport) →
      RelativeComplex P → RemainingFaceCochains P
    reductionValid : (P : ShortSupport) → Type ℓ
    reductionWitness : (P : ShortSupport) → reductionValid P

    normalRestriction : (P a : ShortSupport) →
      RelativeComplex P → RelativeComplex (addNormal P a)
    faceRestriction : (P a : ShortSupport) →
      RemainingFaceCochains P → RemainingFaceCochains (addNormal P a)
    restrictionCommutes : (P a : ShortSupport) (x : RelativeComplex P) →
      reduceToFaces (addNormal P a) (normalRestriction P a x) ≡
      faceRestriction P a (reduceToFaces P x)
    CubeSquare : (P a b : ShortSupport) → Type ℓ
    allCubeSquares : (P a b : ShortSupport) → CubeSquare P a b

    -- Explicit contraction fib(E[-1] -> V + Q[-1]) ~= B[-1].
    MappingFibre ShiftedBoundary : Type ℓ
    fibreProjection : MappingFibre → ShiftedBoundary
    fibreInclusion : ShiftedBoundary → MappingFibre
    fibreHomotopy : MappingFibre → MappingFibre
    FibreContractionEquation :
      (MappingFibre → ShiftedBoundary) →
      (ShiftedBoundary → MappingFibre) →
      (MappingFibre → MappingFibre) → Type ℓ
    fibreContraction :
      FibreContractionEquation fibreProjection fibreInclusion fibreHomotopy

    OriginalComponent FullComponent : Type ℓ
    originalLeft originalRight : OriginalComponent
    originalComponentsDistinct : originalLeft ≡ originalRight → ⊥
    multiplyToFull : OriginalComponent → FullComponent
    fullFibreContractible : (x y : FullComponent) → x ≡ y

    EndpointClass : Type ℓ
    zeroEndpoint : EndpointClass
    positiveEndpointClass negativeEndpointClass : EndpointClass
    positiveEndpointNonzero : positiveEndpointClass ≡ zeroEndpoint → ⊥
    negativeEndpointNonzero : negativeEndpointClass ≡ zeroEndpoint → ⊥
    multiplyEndpointByAllNormals : EndpointClass → EndpointClass
    fullNormalsKillPositive :
      multiplyEndpointByAllNormals positiveEndpointClass ≡ zeroEndpoint
    fullNormalsKillNegative :
      multiplyEndpointByAllNormals negativeEndpointClass ≡ zeroEndpoint

    -- Reflection maps between branch degrees; it is not an endomap of either.
    OddBranchPoint EvenBranchPoint BranchLoop : Type ℓ
    oddBranchConnected : (x y : OddBranchPoint) → x ≡ y
    evenBranchConnected : (x y : EvenBranchPoint) → x ≡ y
    reflectOddToEven : OddBranchPoint → EvenBranchPoint
    reflectEvenToOdd : EvenBranchPoint → OddBranchPoint
    branchLoop : BranchLoop
    BranchLoopNontrivial : BranchLoop → Type ℓ
    branchLoopNontrivial : BranchLoopNontrivial branchLoop

open EndpointNormalCubeCertificate public

fullMultiplicationForgetsDistinction : {ℓ : Level}
  (C : EndpointNormalCubeCertificate {ℓ}) →
  Σ (originalLeft C ≡ originalRight C → ⊥) λ _ →
    multiplyToFull C (originalLeft C) ≡ multiplyToFull C (originalRight C)
fullMultiplicationForgetsDistinction C =
  originalComponentsDistinct C ,
  fullFibreContractible C
    (multiplyToFull C (originalLeft C))
    (multiplyToFull C (originalRight C))

fullMultiplicationDoesNotPreservePositiveEndpoint : {ℓ : Level}
  (C : EndpointNormalCubeCertificate {ℓ}) →
  multiplyEndpointByAllNormals C (positiveEndpointClass C)
    ≡ positiveEndpointClass C → ⊥
fullMultiplicationDoesNotPreservePositiveEndpoint C preserves =
  positiveEndpointNonzero C
    (sym preserves ∙ fullNormalsKillPositive C)

fullMultiplicationDoesNotPreserveNegativeEndpoint : {ℓ : Level}
  (C : EndpointNormalCubeCertificate {ℓ}) →
  multiplyEndpointByAllNormals C (negativeEndpointClass C)
    ≡ negativeEndpointClass C → ⊥
fullMultiplicationDoesNotPreserveNegativeEndpoint C preserves =
  negativeEndpointNonzero C
    (sym preserves ∙ fullNormalsKillNegative C)

-- No preferred original component, external-Tor placement, or physical parity
-- selector is exported from terminal contractibility.
