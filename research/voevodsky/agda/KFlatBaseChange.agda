{-# OPTIONS --safe --cubical --guardedness #-}
module KFlatBaseChange where

open import Cubical.Foundations.Prelude
open import Cubical.Data.Nat using (ℕ; zero; suc)

-- A bounded-free complex is presented by a finite filtration. Each successor
-- adds a finite free degree and comes with the standard closure theorem for
-- K-flatness. Hence source K-flatness below is recursively constructed.
record BoundedFreeFiltration {ℓ : Level} : Type (ℓ-suc ℓ) where
  field
    Complex : Type ℓ
    zeroComplex : Complex
    stage : ℕ → Complex
    stageZero : stage zero ≡ zeroComplex
    FreeExtension : Complex → Complex → Type ℓ
    finiteFreeStep : (n : ℕ) → FreeExtension (stage n) (stage (suc n))

    KFlat : Complex → Type ℓ
    zeroKFlat : KFlat zeroComplex
    freeExtensionPreservesKFlat : {C D : Complex} →
      FreeExtension C D → KFlat C → KFlat D

    source : Complex
    bound : ℕ
    sourceAtBound : source ≡ stage bound
    transportKFlat : {C D : Complex} → C ≡ D → KFlat D → KFlat C

open BoundedFreeFiltration

stageKFlat : {ℓ : Level} (F : BoundedFreeFiltration {ℓ})
  (n : ℕ) → KFlat F (stage F n)
stageKFlat F zero = transportKFlat F (stageZero F) (zeroKFlat F)
stageKFlat F (suc n) =
  freeExtensionPreservesKFlat F (finiteFreeStep F n) (stageKFlat F n)

boundedFreeIsKFlat : {ℓ : Level} (F : BoundedFreeFiltration {ℓ}) →
  KFlat F (source F)
boundedFreeIsKFlat F =
  transportKFlat F (sourceAtBound F) (stageKFlat F (bound F))

-- The comparison theorem is parameterized by a concrete tensor setup, but its
-- authorization must be the recursively obtained K-flat witness above.
record TensorBaseChangeData {ℓ : Level}
  (F : BoundedFreeFiltration {ℓ}) : Type (ℓ-suc ℓ) where
  field
    CoefficientAlgebra : Type ℓ
    coefficients : CoefficientAlgebra
    TermwiseTensor DerivedTensor :
      Complex F → CoefficientAlgebra → Type ℓ
    compare :
      TermwiseTensor (source F) coefficients →
      DerivedTensor (source F) coefficients

    KFlatComparisonInverse :
      KFlat F (source F) →
      (DerivedTensor (source F) coefficients →
       TermwiseTensor (source F) coefficients)
    comparisonSection : (k : KFlat F (source F))
      (x : TermwiseTensor (source F) coefficients) →
      KFlatComparisonInverse k (compare x) ≡ x
    comparisonRetraction : (k : KFlat F (source F))
      (x : DerivedTensor (source F) coefficients) →
      compare (KFlatComparisonInverse k x) ≡ x

module BoundedFreeBaseChange {ℓ : Level}
  (F : BoundedFreeFiltration {ℓ}) (T : TensorBaseChangeData F) where
  open TensorBaseChangeData T

  sourceKFlat : KFlat F (source F)
  sourceKFlat = boundedFreeIsKFlat F

  derivedToTermwise :
    DerivedTensor (source F) coefficients →
    TermwiseTensor (source F) coefficients
  derivedToTermwise = KFlatComparisonInverse sourceKFlat

  termwiseDerivedSection :
    (x : TermwiseTensor (source F) coefficients) →
    derivedToTermwise (compare x) ≡ x
  termwiseDerivedSection = comparisonSection sourceKFlat

  termwiseDerivedRetraction :
    (x : DerivedTensor (source F) coefficients) →
    compare (derivedToTermwise x) ≡ x
  termwiseDerivedRetraction = comparisonRetraction sourceKFlat

record BoundedFreeBaseChangeCertificate {ℓ : Level} : Type (ℓ-suc ℓ) where
  field
    filtration : BoundedFreeFiltration {ℓ}
    tensorData : TensorBaseChangeData filtration
