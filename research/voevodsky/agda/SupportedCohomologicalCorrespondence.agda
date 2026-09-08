{-# OPTIONS --safe --cubical --guardedness #-}
module SupportedCohomologicalCorrespondence where

open import Cubical.Foundations.Prelude
open import Cubical.Data.Empty using (⊥)

-- A cohomological correspondence is extraordinary at the target leg. Its
-- generic value is obtained from supported data through the localization
-- connector, not by dualizing an ordinary generic carrier map afterward.
record SupportedCohomologicalCorrespondence {ℓ : Level}
  : Type (ℓ-suc ℓ) where
  field
    Source Ambient Supported OpenGeneric : Type ℓ
    OrdinaryPullback ExtraordinaryPullback : Type ℓ
    ordinaryPullback : Source → OrdinaryPullback
    extraordinaryPullback : Ambient → ExtraordinaryPullback

    SupportInclusion AmbientProjection : Type ℓ
    supportInclusion : Supported → Ambient
    genericProjection : Ambient → OpenGeneric
    LocalizationTriangle : Type ℓ
    localizationTriangle : LocalizationTriangle

    SupportedClass GenericClass : Type ℓ
    supportedClass : SupportedClass
    zeroSupportedClass : SupportedClass
    genericClass : GenericClass
    zeroGenericClass : GenericClass
    localizationConnecting : SupportedClass → GenericClass
    genericFromSupport : localizationConnecting supportedClass ≡ genericClass
    supportedClassNonzero : supportedClass ≡ zeroSupportedClass → ⊥
    genericClassNonzero : genericClass ≡ zeroGenericClass → ⊥

    OrdinaryGenericMorphism : Type ℓ
    ordinaryGeneric : OrdinaryGenericMorphism
    zeroOrdinaryGeneric : OrdinaryGenericMorphism
    ordinaryGenericNull : ordinaryGeneric ≡ zeroOrdinaryGeneric

    CapTraceValue : Type ℓ
    capTrace : ExtraordinaryPullback → SupportedClass → CapTraceValue
    extraordinaryKernel : ExtraordinaryPullback
    capValue : CapTraceValue
    zeroCapValue : CapTraceValue
    capEquation : capTrace extraordinaryKernel supportedClass ≡ capValue
    capValueNonzero : capValue ≡ zeroCapValue → ⊥

    DualNormalLine Shift : Type ℓ
    dualNormalLine : DualNormalLine
    supportShift : Shift
    determinantShiftRetained : Type ℓ
    determinantShiftWitness : determinantShiftRetained

    PlusEndpoint MinusEndpoint EndpointCell : Type ℓ
    plusEndpoint : PlusEndpoint
    minusEndpoint : MinusEndpoint
    plusConnector minusConnector : EndpointCell
    CoupledEndpointConeLaw : Type ℓ
    coupledEndpointConeWitness : CoupledEndpointConeLaw

    FilteredObject FirstSymbol : Type ℓ
    filteredSource : FilteredObject
    firstSymbol : FilteredObject → FirstSymbol
    fixedFirstSymbol : FirstSymbol
    filteredSymbolCompatibility : firstSymbol filteredSource ≡ fixedFirstSymbol

    BetaFamily ExcessSpecialFibre : Type ℓ
    betaFamily : BetaFamily
    excessSpecialFibre : ExcessSpecialFibre
    ExcessBaseChangeCompatibility : Type ℓ
    excessBaseChangeWitness : ExcessBaseChangeCompatibility

    -- Any realization through the tested ordinary generic map would identify
    -- the nonzero connector value with zero.
    OrdinaryFactorization : Type ℓ
    ordinaryFactorizationForcesZero : OrdinaryFactorization →
      genericClass ≡ zeroGenericClass

extraordinaryGenericValueDoesNotFactorOrdinarily : {ℓ : Level}
  (C : SupportedCohomologicalCorrespondence {ℓ}) →
  SupportedCohomologicalCorrespondence.OrdinaryFactorization C → ⊥
extraordinaryGenericValueDoesNotFactorOrdinarily C factors =
  SupportedCohomologicalCorrespondence.genericClassNonzero C
    (SupportedCohomologicalCorrespondence.ordinaryFactorizationForcesZero C factors)

-- Nested support functors carry their own transitivity law. This is separate
-- from merely composing scalar values of already evaluated residues.
record NestedSupportTransitivity {ℓ : Level} : Type (ℓ-suc ℓ) where
  field
    Object SmallSupport LargeSupport : Type ℓ
    supportSmall : Object → SmallSupport
    supportLarge : Object → LargeSupport
    enlargeSupport : SmallSupport → LargeSupport
    transitivity : (x : Object) →
      enlargeSupport (supportSmall x) ≡ supportLarge x

    SmallDualLine LargeDualLine QuotientDualLine : Type ℓ
    composeDualLines : SmallDualLine → QuotientDualLine → LargeDualLine
    smallLine : SmallDualLine
    quotientLine : QuotientDualLine
    largeLine : LargeDualLine
    determinantTransitivity :
      composeDualLines smallLine quotientLine ≡ largeLine

record SupportedCorrespondenceCertificate {ℓ : Level} : Type (ℓ-suc ℓ) where
  field
    correspondence : SupportedCohomologicalCorrespondence {ℓ}
    nestedSupports : NestedSupportTransitivity {ℓ}
