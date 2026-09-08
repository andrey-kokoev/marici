{-# OPTIONS --safe --cubical --guardedness #-}
module DGPyramidUnionRecollement where

open import Cubical.Foundations.Prelude
open import Cubical.Data.Empty using (⊥)

record UnionRecollementCertificate {ℓ : Level} : Type (ℓ-suc ℓ) where
  field
    Thickness FiniteDual LocalCohomology OpenComplement Object : Type ℓ
    zeroThickness : Thickness
    successorThickness : Thickness → Thickness
    dualAt : Thickness → FiniteDual
    transition : (n : Thickness) →
      FiniteDual → FiniteDual
    transitionChainMap : (n : Thickness) → Type ℓ
    supportColimit : LocalCohomology
    colimitIsLocalCohomology : Type ℓ
    colimitWitness : colimitIsLocalCohomology

    extendedCechSupport : LocalCohomology
    cechIdentification : supportColimit ≡ extendedCechSupport
    localizationCounit : LocalCohomology → Object
    openObject : OpenComplement
    LocalizationTriangle : Type ℓ
    localizationTriangleWitness : LocalizationTriangle

    tensorSupport : LocalCohomology → LocalCohomology → LocalCohomology
    tensorOpen : OpenComplement → OpenComplement → OpenComplement
    zeroMixed : Type ℓ
    supportIdempotent openIdempotent supportOpenOrthogonal : Type ℓ
    supportIdempotentWitness : supportIdempotent
    openIdempotentWitness : openIdempotent
    supportOpenWitness : supportOpenOrthogonal

    HigherPoleClass FirstPoleClass : Type ℓ
    higherPole : HigherPoleClass
    firstPole : FirstPoleClass
    multiplyNormal : HigherPoleClass → FirstPoleClass
    higherPoleSurvives : multiplyNormal higherPole ≡ firstPole

    FiniteCounitCone : Type ℓ
    finiteCone : FiniteCounitCone
    FiniteOpenIdentification : Type ℓ
    finiteConeIsNotOpenComplement : FiniteOpenIdentification → ⊥

    PrimaryObstruction SecondaryObstruction : Type ℓ
    primaryObstruction : PrimaryObstruction
    secondaryObstruction : SecondaryObstruction
    zeroPrimary : PrimaryObstruction
    zeroSecondary : SecondaryObstruction
    restrictPrimaryToOpen : PrimaryObstruction → PrimaryObstruction
    restrictSecondaryToOpen : SecondaryObstruction → SecondaryObstruction
    primaryPersists : restrictPrimaryToOpen primaryObstruction ≡ zeroPrimary → ⊥
    secondaryPersists : restrictSecondaryToOpen secondaryObstruction ≡ zeroSecondary → ⊥

    TopLiftingModule OpenTopLiftingModule : Type ℓ
    topLiftingModule : TopLiftingModule
    openTopLiftingModule : OpenTopLiftingModule
    recoverTopFromOpen : Type ℓ
    recoverTopWitness : recoverTopFromOpen
    GenericUnitLift : Type ℓ
    noGenericUnitLiftOnOpen : GenericUnitLift → ⊥
