{-# OPTIONS --safe --cubical --no-import-sorts --guardedness #-}
module CauchyProductAlgebra where

open import Cubical.Foundations.Prelude
open import Cubical.Data.Nat as ℕ using (ℕ; _+_)
open import Cubical.Data.Rationals as Q
open import Cubical.Algebra.CommRing
open import Cubical.Tactics.CommRingSolver
open import RationalAnalyticSubstrate
open import RegularCauchyStructure
open import DyadicallyBoundedCauchy

module ProductDifference {ℓ} (R : CommRing ℓ) where
  open CommRingStr (snd R)
    renaming (_+_ to _+S_; _·_ to _·S_; -_ to -S_)

  difference-decomposition : (a b c d : fst R) →
    (a ·S b) +S (-S (c ·S d)) ≡
    (a ·S (b +S (-S d))) +S (d ·S (a +S (-S c)))
  difference-decomposition a b c d = solve! R

product-difference-decomposition : (a b c d : Q.ℚ) →
  (a Q.· b) Q.+ (Q.- (c Q.· d)) ≡
  (a Q.· (b Q.+ (Q.- d))) Q.+
  (d Q.· (a Q.+ (Q.- c)))
product-difference-decomposition =
  ProductDifference.difference-decomposition PreferredℚCommRing

rawProductApproximation :
  RegularCauchy → RegularCauchy → ℕ → Q.ℚ
rawProductApproximation x y n =
  approximation x n Q.· approximation y n

refinedProductApproximation :
  ℕ → RegularCauchy → RegularCauchy → ℕ → Q.ℚ
refinedProductApproximation shift x y n =
  approximation x (shift ℕ.+ n) Q.·
  approximation y (shift ℕ.+ n)

refined-product-difference :
  (shift m n : ℕ) (x y : RegularCauchy) →
  refinedProductApproximation shift x y m Q.+
    (Q.- refinedProductApproximation shift x y n) ≡
  (approximation x (shift ℕ.+ m) Q.·
    (approximation y (shift ℕ.+ m) Q.+
      (Q.- approximation y (shift ℕ.+ n)))) Q.+
  (approximation y (shift ℕ.+ n) Q.·
    (approximation x (shift ℕ.+ m) Q.+
      (Q.- approximation x (shift ℕ.+ n))))
refined-product-difference shift m n x y =
  product-difference-decomposition
    (approximation x (shift ℕ.+ m))
    (approximation y (shift ℕ.+ m))
    (approximation x (shift ℕ.+ n))
    (approximation y (shift ℕ.+ n))

record ProductConstructionData
  (x y : DyadicallyBoundedRegularCauchy) : Type where
  field
    refinement-depth : ℕ
    approximation-function : ℕ → Q.ℚ
    approximation-is-refined-product : (n : ℕ) →
      approximation-function n ≡
      refinedProductApproximation refinement-depth (regular x) (regular y) n
open ProductConstructionData public

canonicalProductData :
  (x y : DyadicallyBoundedRegularCauchy) →
  ProductConstructionData x y
canonicalProductData x y .refinement-depth =
  ℕ.suc (radius-exponent x ℕ.+ radius-exponent y)
canonicalProductData x y .approximation-function =
  refinedProductApproximation
    (ℕ.suc (radius-exponent x ℕ.+ radius-exponent y))
    (regular x) (regular y)
canonicalProductData x y .approximation-is-refined-product n = refl
