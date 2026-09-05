{-# OPTIONS --safe --cubical --no-import-sorts --guardedness #-}
module CauchyBoundPromotion where

open import Cubical.Foundations.Prelude
open import Cubical.Data.Nat using (ℕ)
open import Cubical.Data.Rationals as Q
open import Cubical.Data.Rationals.Order
open import Cubical.Data.Sigma
open import Cubical.HITs.PropositionalTruncation as PT
open import RegularCauchyStructure
open import RationallyBoundedCauchy
open import DyadicallyBoundedCauchy
open import RationalArchimedean
import CauchyNegation

promote-rational-bound :
  (x : RationallyBoundedRegularCauchy) →
  ArchimedeanExponent (radius x) →
  DyadicallyBoundedRegularCauchy
promote-rational-bound x witness .regular = regular x
promote-rational-bound x witness .radius-exponent = exponent witness
promote-rational-bound x witness .lower-bound n =
  isTrans≤
    (Q.- dyadicRadius (exponent witness))
    (Q.- radius x)
    (approximation (regular x) n)
    (subst (Q.- dyadicRadius (exponent witness) ≤_)
      (Q.+IdR (Q.- radius x))
      (CauchyNegation.negate-one-error-bound
        (radius x) (dyadicRadius (exponent witness)) 0
        (subst (radius x ≤_)
          (sym (Q.+IdR (dyadicRadius (exponent witness))))
          (dominates witness))))
    (lower-bound-from-negative-upper x n)
  where
  lower-bound-from-negative-upper :
    (y : RationallyBoundedRegularCauchy) (m : ℕ) →
    Q.- radius y ≤ approximation (regular y) m
  lower-bound-from-negative-upper y m =
    subst (Q.- radius y ≤_)
      (Q.+IdR (Q.- Q.- approximation (regular y) m) ∙
       Q.-Invol (approximation (regular y) m))
      (CauchyNegation.negate-one-error-bound
        (Q.- approximation (regular y) m)
        (radius y) 0
        (subst (Q.- approximation (regular y) m ≤_)
          (sym (Q.+IdR (radius y)))
          (negative-upper y m)))
promote-rational-bound x witness .upper-bound n =
  isTrans≤ (approximation (regular x) n) (radius x)
    (dyadicRadius (exponent witness))
    (positive-upper x n) (dominates witness)

promote-regular-with-witness :
  (x : RegularCauchy) →
  ArchimedeanExponent (canonicalRadius x) →
  DyadicallyBoundedRegularCauchy
promote-regular-with-witness x =
  promote-rational-bound (regular-is-rationally-bounded x)

promote-regular-truncated :
  (x : RegularCauchy) →
  DyadicDominates (canonicalRadius x) →
  ∥ DyadicallyBoundedRegularCauchy ∥₁
promote-regular-truncated x = PT.map λ { (d , bound) →
  promote-regular-with-witness x record
    { exponent = d ; dominates = bound } }

BoundedPresentation : RegularCauchy → Type
BoundedPresentation x =
  Σ[ bounded ∈ DyadicallyBoundedRegularCauchy ] regular bounded ≡ x

promote-regular-presentation-with-witness :
  (x : RegularCauchy) →
  ArchimedeanExponent (canonicalRadius x) →
  BoundedPresentation x
promote-regular-presentation-with-witness x witness =
  promote-regular-with-witness x witness , refl

promote-regular-presentation-truncated :
  (x : RegularCauchy) →
  DyadicDominates (canonicalRadius x) →
  ∥ BoundedPresentation x ∥₁
promote-regular-presentation-truncated x = PT.map λ { (d , bound) →
  promote-regular-presentation-with-witness x record
    { exponent = d ; dominates = bound } }
