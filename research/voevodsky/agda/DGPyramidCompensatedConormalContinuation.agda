{-# OPTIONS --safe --cubical --guardedness #-}
module DGPyramidCompensatedConormalContinuation where

open import Cubical.Foundations.Prelude
open import Cubical.Data.Empty using (⊥)
open import DGPyramidHigherCoherenceHom

-- Branch A's rank-six object is an ordinary coefficient module with two
-- cancelling continuation paths.  Its cancellation is multiplication-level
-- data, not an Ext differential declaring the old mixed class a boundary.
record ReflectionClosedCompensatedContinuation {ℓ : Level}
  : Type (ℓ-suc ℓ) where
  field
    Carrier Coefficient : Type ℓ
    u v35 c35 v04 c04 w : Carrier
    zero : Carrier
    beta : Coefficient
    action35 action04 : Carrier → Carrier
    scale : Coefficient → Carrier → Carrier

    action35OnU : action35 u ≡ scale beta v35
    action04OnU : action04 u ≡ scale beta v04
    compensating35Path : Type ℓ
    compensating04Path : Type ℓ
    mixed35Then04Cancels : action04 (action35 u) ≡ zero
    mixed04Then35Cancels : action35 (action04 u) ≡ zero

    reflection : Carrier → Carrier
    reflectionSquaresToIdentity : (x : Carrier) →
      reflection (reflection x) ≡ x
    reflectionExchangesActions : (x : Carrier) →
      reflection (action35 x) ≡ action04 (reflection x)

    ordinaryModuleDifferentialIsNotAnExtTransgression : Type ℓ
    targetHasChanged : Type ℓ

-- To identify a construction with AugmentedHigherCoherenceHom one must supply
-- an actual new Ext-degree-one cochain whose differential is the included old
-- mixed cocycle.  Strict cancellation of two module-action composites does
-- not fill this field.
record CompensatedContinuationAugmentationGate {ℓ : Level}
  (H : HigherCoherenceHomComplex {ℓ})
  (Boundary : ButterflyMaurerCartanBoundary H)
  (Compensated : ReflectionClosedCompensatedContinuation {ℓ})
  : Type (ℓ-suc ℓ) where
  field
    Augmentation : AugmentedHigherCoherenceHom H Boundary
    compensatedCarrierRealizesAugmentedExtDegrees : Type ℓ
    baseNullCellIsSpecifiedInCompensatedCarrier : Type ℓ
    baseNullDifferentialIsTheOldMixedCocycle :
      AugmentedHigherCoherenceHom.augmentedDifferential Augmentation
        (AugmentedHigherCoherenceHom.baseNullTransgression Augmentation) ≡
      AugmentedHigherCoherenceHom.includeExt2 Augmentation
        (ButterflyMaurerCartanBoundary.mixedRHomCocycle Boundary)
    endpointAndGenericReadoutsAreThePhysicalOnes : Type ℓ
    operationAndReflectionActionsIntertwineTheDifferential : Type ℓ

-- The homotopy-cofiber construction has the correct formal shape, unlike the
-- ordinary rank-six module: it changes the target and supplies the canonical
-- transgression equation.  Physical readouts and actions remain gates.
record MixedProductCofiberRealization {ℓ : Level}
  (H : HigherCoherenceHomComplex {ℓ})
  (Boundary : ButterflyMaurerCartanBoundary H)
  : Type (ℓ-suc ℓ) where
  field
    Augmentation : AugmentedHigherCoherenceHom H Boundary
    canonicalConeHomotopyIsBaseNullTransgression : Type ℓ
    canonicalConeEquationIsAugmentedDifferentialEquation :
      AugmentedHigherCoherenceHom.augmentedDifferential Augmentation
        (AugmentedHigherCoherenceHom.baseNullTransgression Augmentation) ≡
      AugmentedHigherCoherenceHom.includeExt2 Augmentation
        (ButterflyMaurerCartanBoundary.mixedRHomCocycle Boundary)
    cofiberChangesTarget : Type ℓ
    noRetractionToOldRHom :
      CurrentRHomRetraction H Boundary Augmentation →
      ⊥
    physicalEndpointReadoutRemainsToBeConstructed : Type ℓ
    relativeOperationActionRemainsToBeConstructed : Type ℓ

record CurrentCompensatedContinuationAudit {ℓ : Level}
  : Type (ℓ-suc ℓ) where
  field
    reflectionClosedRankSixCalculationPasses : Type ℓ
    bothOrderedModuleProductsCancel : Type ℓ
    rankSixObjectDoesNotByItselfInstantiateAugmentedHigherHom : Type ℓ
    cofiberHasTheRequiredAugmentedDifferentialShape : Type ℓ
    BranchCPhysicalComparisonIsStillRequired : Type ℓ
