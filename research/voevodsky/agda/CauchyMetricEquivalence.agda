{-# OPTIONS --safe --cubical --no-import-sorts --guardedness #-}
module CauchyMetricEquivalence where

open import Cubical.Foundations.Prelude
open import Cubical.Foundations.HLevels
open import Cubical.Data.Nat as ℕ using (ℕ; suc; max)
import Cubical.Data.Nat.Order as ℕOrder
open import Cubical.Data.Rationals as Q
open import Cubical.Data.Rationals.Order
open import Cubical.Data.Sigma
open import Cubical.HITs.PropositionalTruncation as PT
open import Cubical.HITs.SetQuotients as SQ
  using ([_]; squash/)
  renaming (_/_ to _//_)
open import Cubical.Relation.Binary.Base
open BinaryRelation
open import RegularCauchyStructure

EventuallyWithin : RegularCauchy → RegularCauchy → ℕ → Type
EventuallyWithin x y k =
  ∥ Σ[ N ∈ ℕ ] ((n : ℕ) → ℕOrder._≤_ N n →
      (approximation x n ≤ approximation y n Q.+ precision k) ×
      (approximation y n ≤ approximation x n Q.+ precision k)) ∥₁

infix 4 _≈metric_
_≈metric_ : RegularCauchy → RegularCauchy → Type
x ≈metric y = (k : ℕ) → EventuallyWithin x y k

≈metric-isProp : (x y : RegularCauchy) → isProp (x ≈metric y)
≈metric-isProp x y = isPropΠ λ k → isPropPropTrunc

≈metric-refl : isRefl _≈metric_
≈metric-refl x k = ∣ (0 , λ n 0≤n →
  (≤-add-nonnegative (approximation x n) (precision k)
     (precision-nonnegative k) ,
   ≤-add-nonnegative (approximation x n) (precision k)
     (precision-nonnegative k))) ∣₁

≈metric-sym : isSym _≈metric_
≈metric-sym x y r k = PT.map
  (λ { (N , bounds) → N , λ n N≤n →
    snd (bounds n N≤n) , fst (bounds n N≤n) })
  (r k)

compose-bound : (a b c : Q.ℚ) (k : ℕ) →
  a ≤ b Q.+ precision (suc k) →
  b ≤ c Q.+ precision (suc k) →
  a ≤ c Q.+ precision k
compose-bound a b c k a≤b+e b≤c+e =
  subst (λ z → a ≤ z)
    (sym (Q.+Assoc c (precision (suc k)) (precision (suc k))) ∙
     cong (c Q.+_) (precision-refines-double k))
    (isTrans≤ a (b Q.+ precision (suc k))
      ((c Q.+ precision (suc k)) Q.+ precision (suc k))
      a≤b+e
      (≤-+o b (c Q.+ precision (suc k)) (precision (suc k)) b≤c+e))

≈metric-trans : isTrans _≈metric_
≈metric-trans x y z r s k =
  PT.rec isPropPropTrunc
    (λ { (Nr , rb) →
      PT.rec isPropPropTrunc
        (λ { (Ns , sb) →
          ∣ (ℕ.max Nr Ns , (λ n N≤n →
            let Nr≤n = ℕOrder.≤-trans ℕOrder.left-≤-max N≤n
                Ns≤n = ℕOrder.≤-trans ℕOrder.right-≤-max N≤n
            in compose-bound
                 (approximation x n) (approximation y n)
                 (approximation z n) k
                 (fst (rb n Nr≤n)) (fst (sb n Ns≤n)) ,
               compose-bound
                 (approximation z n) (approximation y n)
                 (approximation x n) k
                 (snd (sb n Ns≤n)) (snd (rb n Nr≤n))) ) ∣₁ })
        (s (suc k)) })
    (r (suc k))

regular-path→metric : (x y : RegularCauchy) → x ≡ y → x ≈metric y
regular-path→metric x y path =
  subst (x ≈metric_) path (≈metric-refl x)

regular-path←metric : (x y : RegularCauchy) → x ≡ y → y ≈metric x
regular-path←metric x y path =
  ≈metric-sym x y (regular-path→metric x y path)

≈metric-isEquivRel : isEquivRel _≈metric_
isEquivRel.reflexive ≈metric-isEquivRel = ≈metric-refl
isEquivRel.symmetric ≈metric-isEquivRel = ≈metric-sym
isEquivRel.transitive ≈metric-isEquivRel = ≈metric-trans

MetricCompletionCandidate : Type
MetricCompletionCandidate = RegularCauchy // _≈metric_

metric-candidate-isSet : isSet MetricCompletionCandidate
metric-candidate-isSet = squash/

embedMetricℚ : Q.ℚ → MetricCompletionCandidate
embedMetricℚ q = [ constantCauchy q ]
