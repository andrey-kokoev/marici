{-# OPTIONS --safe --cubical --no-import-sorts --guardedness #-}
module TaylorGeometricTail where

open import Cubical.Foundations.Prelude
open import Cubical.Data.Nat as ℕ using (ℕ; zero; suc; _+_)
open import Cubical.Data.Rationals as Q
open import Cubical.Data.Rationals.Order
open import Cubical.Algebra.CommRing
open import Cubical.Tactics.CommRingSolver
open import RationalAnalyticSubstrate
open import RegularCauchyStructure
open import CauchyProductBounds
open import CauchyProductErrorBounds
open import TaylorTermBounds
open import RationalTaylorApproximants

module PartialSumPaths {ℓ} (R : CommRing ℓ) where
  open CommRingStr (snd R)
    renaming (_+_ to _+S_; -_ to -S_)

  remove-base : (base block : fst R) →
    (base +S block) +S (-S base) ≡ block
  remove-base base block = solve! R

geometricBlock : ℕ → ℕ → Q.ℚ
geometricBlock start zero = 0
geometricBlock start (suc count) =
  precision (suc start) Q.+ geometricBlock (suc start) count

geometricBlock-nonnegative : (start count : ℕ) →
  0 ≤ geometricBlock start count
geometricBlock-nonnegative start zero = isRefl≤ 0
geometricBlock-nonnegative start (suc count) =
  ≤Monotone+ 0 (precision (suc start))
    0 (geometricBlock (suc start) count)
    (precision-nonnegative (suc start))
    (geometricBlock-nonnegative (suc start) count)

geometricBlock≤precision : (start count : ℕ) →
  geometricBlock start count ≤ precision start
geometricBlock≤precision start zero =
  precision-nonnegative start
geometricBlock≤precision start (suc count) =
  subst (geometricBlock start (suc count) ≤_)
    (precision-refines-double start)
    (≤Monotone+
      (precision (suc start)) (precision (suc start))
      (geometricBlock (suc start) count) (precision (suc start))
      (isRefl≤ (precision (suc start)))
      (geometricBlock≤precision (suc start) count))

scaledGeometricBlock≤precision : (T : Q.ℚ) (start count : ℕ) →
  0 ≤ T →
  T Q.· geometricBlock start count ≤ T Q.· precision start
scaledGeometricBlock≤precision T start count 0≤T =
  left-multiply-monotone T
    (geometricBlock start count) (precision start)
    0≤T (geometricBlock≤precision start count)

termBlock : (ℕ → Q.ℚ) → ℕ → ℕ → Q.ℚ
termBlock term start zero = 0
termBlock term start (suc count) =
  term (suc start) Q.+ termBlock term (suc start) count

termBlock-shift : (term : ℕ → Q.ℚ) (origin start count : ℕ) →
  termBlock term (origin ℕ.+ start) count ≡
  termBlock (λ j → term (origin ℕ.+ j)) start count
termBlock-shift term origin start zero = refl
termBlock-shift term origin start (suc count) =
  cong₂ Q._+_
    (cong term (sym (ℕ.+-suc origin start)))
    (cong (λ index → termBlock term index count)
       (sym (ℕ.+-suc origin start)) ∙
     termBlock-shift term origin (suc start) count)

termBlock-append : (term : ℕ → Q.ℚ) (start count : ℕ) →
  termBlock term start (suc count) ≡
  termBlock term start count Q.+ term (suc (start ℕ.+ count))
termBlock-append term start zero =
  Q.+IdR (term (suc start)) ∙
  sym (Q.+IdL (term (suc start))) ∙
  cong (λ z → 0 Q.+ z)
    (cong term (cong suc (sym (ℕ.+-zero start))))
termBlock-append term start (suc count) =
  cong (λ z → term (suc start) Q.+ z)
    (termBlock-append term (suc start) count) ∙
  Q.+Assoc
    (term (suc start))
    (termBlock term (suc start) count)
    (term (suc ((suc start) ℕ.+ count))) ∙
  cong (λ z →
      (term (suc start) Q.+ termBlock term (suc start) count) Q.+ z)
    (cong term (cong suc (sym (ℕ.+-suc start count))))

finiteSum-segment : (term : ℕ → Q.ℚ) (start count : ℕ) →
  finiteSum term (start ℕ.+ count) ≡
  finiteSum term start Q.+ termBlock term start count
finiteSum-segment term start zero =
  cong (finiteSum term) (ℕ.+-zero start) ∙
  sym (Q.+IdR (finiteSum term start))
finiteSum-segment term start (suc count) =
  cong (finiteSum term) (ℕ.+-suc start count) ∙
  cong (Q._+ term (suc (start ℕ.+ count)))
    (finiteSum-segment term start count) ∙
  sym (Q.+Assoc
    (finiteSum term start)
    (termBlock term start count)
    (term (suc (start ℕ.+ count)))) ∙
  cong (λ z → finiteSum term start Q.+ z)
    (sym (termBlock-append term start count))

termBlock-magnitude :
  (term : ℕ → Q.ℚ) (T : Q.ℚ) (start count : ℕ) →
  0 ≤ T →
  ((j : ℕ) → MagnitudeBound (term (suc j))
    (T Q.· precision (suc j))) →
  MagnitudeBound (termBlock term start count)
    (T Q.· geometricBlock start count)
termBlock-magnitude term T start zero 0≤T termBound =
  nonnegative-value-magnitude 0 (T Q.· 0)
    (isRefl≤ 0)
    (nonnegative-bound-product T 0 0≤T (isRefl≤ 0))
    (nonnegative-bound-product T 0 0≤T (isRefl≤ 0))
termBlock-magnitude term T start (suc count) 0≤T termBound =
  subst (MagnitudeBound (termBlock term start (suc count)))
    (sym (Q.·DistL+ T
      (precision (suc start)) (geometricBlock (suc start) count)))
    (add-magnitude-bounds _ _ _ _
      (termBound start)
      (termBlock-magnitude term T (suc start) count 0≤T termBound))

termBlock≤scaledPrecision :
  (term : ℕ → Q.ℚ) (T : Q.ℚ) (start count : ℕ) →
  0 ≤ T →
  ((j : ℕ) → MagnitudeBound (term (suc j))
    (T Q.· precision (suc j))) →
  MagnitudeBound (termBlock term start count)
    (T Q.· precision start)
termBlock≤scaledPrecision term T start count 0≤T termBound =
  weaken-magnitude-bound _ _ (T Q.· precision start)
    (scaledGeometricBlock≤precision T start count 0≤T)
    (termBlock-magnitude term T start count 0≤T termBound)

finiteSum-segment-difference-magnitude :
  (term : ℕ → Q.ℚ) (T : Q.ℚ) (start count : ℕ) →
  0 ≤ T →
  ((j : ℕ) → MagnitudeBound (term (suc j))
    (T Q.· precision (suc j))) →
  MagnitudeBound
    (finiteSum term (start ℕ.+ count) Q.+
      (Q.- finiteSum term start))
    (T Q.· precision start)
finiteSum-segment-difference-magnitude term T start count 0≤T termBound =
  transport-magnitude _ (termBlock term start count)
    (T Q.· precision start)
    (cong (Q._+ (Q.- finiteSum term start))
      (finiteSum-segment term start count) ∙
     PartialSumPaths.remove-base PreferredℚCommRing
       (finiteSum term start) (termBlock term start count))
    (termBlock≤scaledPrecision term T start count 0≤T termBound)
