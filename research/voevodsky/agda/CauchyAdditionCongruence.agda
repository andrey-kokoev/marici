{-# OPTIONS --safe --cubical --no-import-sorts --guardedness #-}
module CauchyAdditionCongruence where

open import Cubical.Foundations.Prelude
open import Cubical.Data.Nat as ℕ using (ℕ; suc; max)
import Cubical.Data.Nat.Order as ℕOrder
open import Cubical.Data.Rationals as Q
open import Cubical.Data.Rationals.Order
open import Cubical.Algebra.CommRing
open import Cubical.Tactics.CommRingSolver
open import Cubical.HITs.PropositionalTruncation as PT
open import Cubical.HITs.SetQuotients.Properties using (setQuotBinOp)
open import RationalAnalyticSubstrate
open import RegularCauchyStructure
open import CauchyMetricEquivalence
open import CauchyAddition

module EqualErrorRearrangement {ℓ} (R : CommRing ℓ) where
  open CommRingStr (snd R) renaming (_+_ to _+S_)

  rearrange : (a b e : fst R) →
    (a +S e) +S (b +S e) ≡ (a +S b) +S (e +S e)
  rearrange a b e = solve! R

combine-congruence-bound : (a a′ b b′ : Q.ℚ) (k : ℕ) →
  a ≤ a′ Q.+ precision (suc k) →
  b ≤ b′ Q.+ precision (suc k) →
  a Q.+ b ≤ (a′ Q.+ b′) Q.+ precision k
combine-congruence-bound a a′ b b′ k a≤a′+e b≤b′+e =
  subst (λ z → a Q.+ b ≤ z)
    (EqualErrorRearrangement.rearrange PreferredℚCommRing
       a′ b′ (precision (suc k)) ∙
     cong ((a′ Q.+ b′) Q.+_) (precision-refines-double k))
    (≤Monotone+ a (a′ Q.+ precision (suc k))
      b (b′ Q.+ precision (suc k)) a≤a′+e b≤b′+e)

addRegular-preserves-eventual :
  (x x′ y y′ : RegularCauchy) (k : ℕ) →
  EventuallyWithin x x′ (suc k) →
  EventuallyWithin y y′ (suc k) →
  EventuallyWithin (addRegular x y) (addRegular x′ y′) k
addRegular-preserves-eventual x x′ y y′ k rx ry =
  PT.rec isPropPropTrunc
    (λ { (Nx , xb) →
      PT.rec isPropPropTrunc
        (λ { (Ny , yb) →
          ∣ (ℕ.max Nx Ny , λ n N≤n →
            let Nx≤n = ℕOrder.≤-trans ℕOrder.left-≤-max N≤n
                Ny≤n = ℕOrder.≤-trans ℕOrder.right-≤-max N≤n
                Nx≤sn = ℕOrder.≤-trans Nx≤n ℕOrder.≤-sucℕ
                Ny≤sn = ℕOrder.≤-trans Ny≤n ℕOrder.≤-sucℕ
            in combine-congruence-bound
                 (approximation x (suc n)) (approximation x′ (suc n))
                 (approximation y (suc n)) (approximation y′ (suc n)) k
                 (fst (xb (suc n) Nx≤sn)) (fst (yb (suc n) Ny≤sn)) ,
               combine-congruence-bound
                 (approximation x′ (suc n)) (approximation x (suc n))
                 (approximation y′ (suc n)) (approximation y (suc n)) k
                 (snd (xb (suc n) Nx≤sn)) (snd (yb (suc n) Ny≤sn))) ∣₁ })
        ry })
    rx

addRegular-preserves-left-eventual :
  (x x′ y : RegularCauchy) (k : ℕ) →
  EventuallyWithin x x′ (suc k) →
  EventuallyWithin (addRegular x y) (addRegular x′ y) k
addRegular-preserves-left-eventual x x′ y k relation =
  addRegular-preserves-eventual x x′ y y k relation
    (≈metric-refl y (suc k))

addRegular-preserves-right-eventual :
  (x y y′ : RegularCauchy) (k : ℕ) →
  EventuallyWithin y y′ (suc k) →
  EventuallyWithin (addRegular x y) (addRegular x y′) k
addRegular-preserves-right-eventual x y y′ k relation =
  addRegular-preserves-eventual x x y y′ k
    (≈metric-refl x (suc k)) relation

addRegular-cong :
  (x x′ y y′ : RegularCauchy) →
  x ≈metric x′ → y ≈metric y′ →
  addRegular x y ≈metric addRegular x′ y′
addRegular-cong x x′ y y′ rx ry k =
  addRegular-preserves-eventual x x′ y y′ k
    (rx (suc k)) (ry (suc k))

infixl 20 _+completion_
_+completion_ :
  MetricCompletionCandidate →
  MetricCompletionCandidate →
  MetricCompletionCandidate
_+completion_ =
  setQuotBinOp ≈metric-refl ≈metric-refl addRegular addRegular-cong
