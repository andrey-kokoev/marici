{-# OPTIONS --safe --cubical --guardedness #-}
module DGPyramidRegulatorVertexDecomposition where

open import Cubical.Foundations.Prelude
open import Cubical.Data.Empty using (⊥)

record RegulatorVertexDecompositionCertificate {ℓ : Level}
  : Type (ℓ-suc ℓ) where
  field
    Vertex SupportedMap Primary Chain EndpointPair BocksteinClass : Type ℓ
    beta x35 : Type ℓ
    vertices : Type ℓ
    FourteenVertices : Type ℓ
    fourteenVerticesWitness : FourteenVertices
    vertexMap : Vertex → SupportedMap

    MapClass : Type ℓ
    classOfMap : SupportedMap → MapClass
    zeroMapClass : MapClass
    BetaX35Annihilator : MapClass → Type ℓ
    everyVertexExactAnnihilator : (F : Vertex) →
      BetaX35Annihilator (classOfMap (vertexMap F))

    ComparisonGroup : Type ℓ
    vertexCoordinates : ComparisonGroup → (Vertex → MapClass)
    vertexCoordinatesComplete : Type ℓ
    vertexCoordinatesWitness : vertexCoordinatesComplete

    originalDifference : SupportedMap
    No35Vertex : Vertex → Type ℓ
    sumNo35Vertices : SupportedMap
    nineVertexDecomposition :
      classOfMap originalDifference ≡ classOfMap sumNo35Vertices

    fixedPrimaryCycles : Type ℓ
    psiCycle zCycle : fixedPrimaryCycles
    PolynomialPair : Type ℓ
    fixedPrimaryRankTwo : PolynomialPair
    endpointDetector : fixedPrimaryCycles → EndpointPair
    endpointDetectorUnimodular : Type ℓ
    endpointDetectorWitness : endpointDetectorUnimodular
    endpointRigidity : (z : fixedPrimaryCycles) →
      endpointDetector z ≡ endpointDetector psiCycle → z ≡ psiCycle

    CentralCycle : Type ℓ
    firstBockstein : CentralCycle → BocksteinClass
    no35Component has35Component : CentralCycle
    zeroBockstein : BocksteinClass
    no35InKernel : firstBockstein no35Component ≡ zeroBockstein
    has35InKernel : firstBockstein has35Component ≡ zeroBockstein
    BocksteinKernelExhausted : Type ℓ
    bocksteinKernelWitness : BocksteinKernelExhausted

    EndpointQuotientMapClass : Type ℓ
    quotientDifference : EndpointQuotientMapClass
    zeroEndpointQuotient : EndpointQuotientMapClass
    quotientDifferenceNonzero : quotientDifference ≡ zeroEndpointQuotient → ⊥
    EightInteriorDetectors : Type ℓ
    eightInteriorWitness : EightInteriorDetectors

    TwoNormalExtension : Type ℓ
    proposedTwoNormalExtension : TwoNormalExtension
    extensionEquationSolvable : TwoNormalExtension → Type ℓ
    interiorTwoNormalObstruction :
      extensionEquationSolvable proposedTwoNormalExtension → ⊥

endpointQuotientDoesNotSolveTwoNormalProblem : {ℓ : Level}
  (C : RegulatorVertexDecompositionCertificate {ℓ}) →
  RegulatorVertexDecompositionCertificate.extensionEquationSolvable C
    (RegulatorVertexDecompositionCertificate.proposedTwoNormalExtension C) → ⊥
endpointQuotientDoesNotSolveTwoNormalProblem C =
  RegulatorVertexDecompositionCertificate.interiorTwoNormalObstruction C
