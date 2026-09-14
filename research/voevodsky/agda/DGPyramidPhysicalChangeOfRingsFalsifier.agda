{-# OPTIONS --safe --cubical --guardedness #-}
module DGPyramidPhysicalChangeOfRingsFalsifier where

open import Cubical.Foundations.Prelude
open import Cubical.Data.Empty using (⊥)

-- Branch C's exact bar calculation separates the literal ambient A-Hom from
-- the native node-linear Hom.  The primitive survives restriction, while all
-- mixed relative-operation classes become ambient boundaries.
record PhysicalChangeOfRingsAudit {ℓ : Level} : Type (ℓ-suc ℓ) where
  field
    NativeClass AmbientClass : Type ℓ
    zeroNative : NativeClass
    zeroAmbient : AmbientClass
    primitiveNative relativeNative : NativeClass
    primitiveAmbient relativeAmbient : AmbientClass

    restrictionToAmbient : NativeClass → AmbientClass
    restrictionPreservesPrimitive :
      restrictionToAmbient primitiveNative ≡ primitiveAmbient
    restrictionKillsRelativeOperation :
      restrictionToAmbient relativeNative ≡ zeroAmbient
    ambientRelativeOperationIsBoundary : relativeAmbient ≡ zeroAmbient
    nativeRelativeOperationIsNonzero : relativeNative ≡ zeroNative → ⊥

    -- The literal computation identifies the ambient operation on the
    -- primitive with the displayed ambient-exact class.
    ambientOperationOnPrimitive : AmbientClass
    nativeOperationOnPrimitive : NativeClass
    ambientActionEquation : ambientOperationOnPrimitive ≡ relativeAmbient
    nativeActionEquation : nativeOperationOnPrimitive ≡ relativeNative

    NativeOrbitRank2 NativeOrbitRank3 NativeOrbitRank4 : Type ℓ
    nativeQuadraticOrbitHasRank9 : NativeOrbitRank2
    nativeCubicOrbitHasRank18 : NativeOrbitRank3
    nativeQuarticAndProductsOrbitHasRank96 : NativeOrbitRank4
    all123NonunitTestedOrbitColumnsBecomeAmbientBoundaries : Type ℓ

open PhysicalChangeOfRingsAudit public

-- A forward comparison with the demanded operation intertwiner would send an
-- ambient boundary to the nonzero native relative class.  This is impossible
-- already on cohomology; higher coherence cannot repair the first equation.
record ForwardPrimitiveOperationComparison {ℓ : Level}
  (A : PhysicalChangeOfRingsAudit {ℓ}) : Type (ℓ-suc ℓ) where
  field
    forward : AmbientClass A → NativeClass A
    forwardPreservesZero : forward (zeroAmbient A) ≡ zeroNative A
    forwardPreservesPrimitive :
      forward (primitiveAmbient A) ≡ primitiveNative A
    forwardIntertwinesFirstRelativeOperation :
      forward (ambientOperationOnPrimitive A) ≡
      nativeOperationOnPrimitive A

noForwardPrimitiveOperationComparison : {ℓ : Level}
  (A : PhysicalChangeOfRingsAudit {ℓ}) →
  ForwardPrimitiveOperationComparison A → ⊥
noForwardPrimitiveOperationComparison A F =
  nativeRelativeOperationIsNonzero A
    (sym (nativeActionEquation A) ∙
     sym (ForwardPrimitiveOperationComparison.forwardIntertwinesFirstRelativeOperation F) ∙
     cong (ForwardPrimitiveOperationComparison.forward F)
       (ambientActionEquation A ∙ ambientRelativeOperationIsBoundary A) ∙
     ForwardPrimitiveOperationComparison.forwardPreservesZero F)

-- The reverse restriction map is valid, but is a quotient on operation
-- cohomology rather than an equivalence of operation-bearing objects.
record ReverseRestrictionComparison {ℓ : Level}
  (A : PhysicalChangeOfRingsAudit {ℓ}) : Type (ℓ-suc ℓ) where
  field
    reverse : NativeClass A → AmbientClass A
    reverseIsCanonicalRestriction : (x : NativeClass A) →
      reverse x ≡ restrictionToAmbient A x
    reversePreservesPrimitive : reverse (primitiveNative A) ≡ primitiveAmbient A
    reverseKillsRelativeOrbit : reverse (relativeNative A) ≡ zeroAmbient A
    reverseIsNotClaimedToBeAnEquivalence : Type ℓ

-- The corrected nested coefficient is derived coinduction.  Replacing it by
-- the conductor coefficient object is precisely the invalid step exposed by
-- the bar calculation.
record CoinducedCoefficientGate {ℓ : Level} : Type (ℓ-suc ℓ) where
  field
    AmbientRing NativeRing NativeSheet : Type ℓ
    AmbientEndpointHom CoinducedCoefficient LiteralAmbientHom : Type ℓ
    nativeBarSource : Type ℓ
    coinductionUnit : AmbientEndpointHom → CoinducedCoefficient
    nestedNativeHom : Type ℓ
    tensorHomAdjunctionIdentifiesLiteralAmbientHomWithNestedHom : Type ℓ
    mixedRelationTorTermsAreRetained : Type ℓ
    conductorCoefficientCannotReplaceCoinducedCoefficient : Type ℓ
    genuinelyNativeLinearTargetWouldBeANewPhysicalProblem : Type ℓ

record CurrentPhysicalChangeOfRingsConclusion {ℓ : Level}
  : Type (ℓ-suc ℓ) where
  field
    primitiveAmbientColumnExistsWithCoefficientOne : Type ℓ
    canonicalReverseRestrictionExists : Type ℓ
    allMixedNativeOrbitClassesMapToAmbientBoundaries : Type ℓ
    prescribedForwardPrimitiveAndOperationComparisonIsFalsified : Type ℓ
    QManifoldAndCyclicLayersAreNotReachedByThisLiteralAmbientHom : Type ℓ
