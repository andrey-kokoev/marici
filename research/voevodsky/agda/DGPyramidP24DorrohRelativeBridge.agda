{-# OPTIONS --safe --cubical --guardedness #-}
module DGPyramidP24DorrohRelativeBridge where

open import Cubical.Foundations.Prelude
open import DGPyramidP24TraceDeformation

-- The Dorroh extension A+ = A (+) R is unital, but is not itself the derived
-- algebra of a Q-manifold.  Its useful cyclic object is therefore the reduced
-- complex relative to the augmentation A+ -> R, not the absolute complex.
record DorrohUnitalization {ℓ : Level} : Type (ℓ-suc ℓ) where
  field
    Algebra Scalars UnitalAlgebra : Type ℓ
    zeroAlgebra : Algebra
    oneScalar : Scalars
    derivedProduct : Algebra → Algebra → Algebra
    addAlgebra : Algebra → Algebra → Algebra
    leftScale rightScale : Scalars → Algebra → Algebra
    scalarProduct : Scalars → Scalars → Scalars
    pair : Algebra → Scalars → UnitalAlgebra
    unitalProduct : UnitalAlgebra → UnitalAlgebra → UnitalAlgebra
    unit : UnitalAlgebra
    augmentation : UnitalAlgebra → Scalars
    idealInclusion : Algebra → UnitalAlgebra

    unitIsZeroOne : unit ≡ pair zeroAlgebra oneScalar
    dorrohFormula : (f g : Algebra) (a b : Scalars) →
      unitalProduct (pair f a) (pair g b) ≡
      pair
        (addAlgebra
          (addAlgebra (derivedProduct f g) (leftScale a g))
          (rightScale b f))
        (scalarProduct a b)
    augmentationSplitsUnit : augmentation unit ≡ oneScalar
    augmentationKillsIdeal : (f : Algebra) →
      augmentation (idealInclusion f) ≡ augmentation (idealInclusion zeroAlgebra)
    inclusionIsTheAugmentationIdeal : Type ℓ
    nuclearFrechetDirectSumTopologyIsRetained : Type ℓ

-- Low degrees suffice for P24's trace-deformation obstruction.  "Reduced"
-- means normalized relative to the scalar augmentation: unit-degenerate
-- arguments have been removed.
record P24DorrohReducedBridge {ℓ : Level}
  (P : P24TraceDeformationProblem {ℓ}) : Type (ℓ-suc ℓ) where
  field
    ReducedZero ReducedOne ReducedTwo : Type ℓ
    reducedB0 : ReducedZero → ReducedOne
    reducedB1 : ReducedOne → ReducedTwo

    extendZero : ZeroCochain P → ReducedZero
    extendOne : OneCochain P → ReducedOne
    extendTwo : TwoCochain P → ReducedTwo
    restrictZero : ReducedZero → ZeroCochain P
    restrictOne : ReducedOne → OneCochain P
    restrictTwo : ReducedTwo → TwoCochain P

    restrictExtendZero : (x : ZeroCochain P) → restrictZero (extendZero x) ≡ x
    extendRestrictZero : (x : ReducedZero) → extendZero (restrictZero x) ≡ x
    restrictExtendOne : (x : OneCochain P) → restrictOne (extendOne x) ≡ x
    extendRestrictOne : (x : ReducedOne) → extendOne (restrictOne x) ≡ x
    restrictExtendTwo : (x : TwoCochain P) → restrictTwo (extendTwo x) ≡ x
    extendRestrictTwo : (x : ReducedTwo) → extendTwo (restrictTwo x) ≡ x

    extendPreservesB0 : (x : ZeroCochain P) →
      extendOne (hochschildB0 P x) ≡ reducedB0 (extendZero x)
    extendPreservesB1 : (x : OneCochain P) →
      extendTwo (hochschildB1 P x) ≡ reducedB1 (extendOne x)
    restrictPreservesB0 : (x : ReducedZero) →
      restrictOne (reducedB0 x) ≡ hochschildB0 P (restrictZero x)
    restrictPreservesB1 : (x : ReducedOne) →
      restrictTwo (reducedB1 x) ≡ hochschildB1 P (restrictOne x)

    unitDegenerateArgumentsVanish : Type ℓ
    shiftedCyclicPermutationIsPreserved : Type ℓ
    mapsAreContinuousForCompletedNuclearTensorPowers : Type ℓ

open P24DorrohReducedBridge public

-- The concrete P24 obstruction cochain is transported without changing its
-- Hochschild content.
reducedDeformationCocycle : {ℓ : Level}
  {P : P24TraceDeformationProblem {ℓ}} →
  (B : P24DorrohReducedBridge P) → ReducedOne B
reducedDeformationCocycle {P = P} B = extendOne B (deformationCocycle P)

reducedDeformationCocycleIsClosed : {ℓ : Level}
  {P : P24TraceDeformationProblem {ℓ}}
  (B : P24DorrohReducedBridge P) →
  reducedB1 B (reducedDeformationCocycle B) ≡ extendTwo B (zeroTwo P)
reducedDeformationCocycleIsClosed {P = P} B =
  sym (extendPreservesB1 B (deformationCocycle P)) ∙
  cong (extendTwo B) (deformationCocycleIsClosed P)

-- A reduced Dorroh primitive restricts to P24's actual trace variation.  This
-- is the direction needed to ensure that adjoining a unit creates no false
-- solution of b sigma + phi = 0.
record ReducedDorrohTraceExtension {ℓ : Level}
  {P : P24TraceDeformationProblem {ℓ}}
  (B : P24DorrohReducedBridge P) : Type (ℓ-suc ℓ) where
  field
    reducedTraceVariation : ReducedZero B
    reducedFirstOrderEquation :
      reducedDeformationCocycle B ≡
      extendOne B (negateOne P
        (hochschildB0 P (restrictZero B reducedTraceVariation)))

reducedExtensionRestrictsToP24 : {ℓ : Level}
  {P : P24TraceDeformationProblem {ℓ}}
  (B : P24DorrohReducedBridge P) →
  ReducedDorrohTraceExtension B →
  InfinitesimalTraceExtension P
reducedExtensionRestrictsToP24 {P = P} B E =
  record
    { traceVariation = restrictZero B
        (ReducedDorrohTraceExtension.reducedTraceVariation E)
    ; firstOrderTraceEquation =
        sym (restrictExtendOne B (deformationCocycle P)) ∙
        cong (restrictOne B)
          (ReducedDorrohTraceExtension.reducedFirstOrderEquation E) ∙
        restrictExtendOne B
          (negateOne P (hochschildB0 P
            (restrictZero B
              (ReducedDorrohTraceExtension.reducedTraceVariation E))))
    }

p24ExtensionProducesReducedExtension : {ℓ : Level}
  {P : P24TraceDeformationProblem {ℓ}}
  (B : P24DorrohReducedBridge P) →
  InfinitesimalTraceExtension P →
  ReducedDorrohTraceExtension B
p24ExtensionProducesReducedExtension {P = P} B E =
  record
    { reducedTraceVariation = extendZero B (traceVariation E)
    ; reducedFirstOrderEquation =
        cong (extendOne B) (firstOrderTraceEquation E) ∙
        cong (λ x → extendOne B
          (negateOne P (hochschildB0 P x)))
          (sym (restrictExtendZero B (traceVariation E)))
    }

record DorrohBridgeBoundary {ℓ : Level} : Type (ℓ-suc ℓ) where
  field
    standardAlgebraicNormalizationTheoremStillRequired : Type ℓ
    shiftedSuperSignsMustBeChecked : Type ℓ
    continuityOfNormalizationMustBeChecked : Type ℓ
    noQManifoldStructureOnTheUnitalizationMayBeClaimed : Type ℓ
