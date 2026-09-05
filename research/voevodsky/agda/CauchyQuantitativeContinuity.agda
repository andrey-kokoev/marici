{-# OPTIONS --safe --cubical --no-import-sorts --guardedness #-}
module CauchyQuantitativeContinuity where

open import Cubical.Foundations.Prelude
open import Cubical.Data.Nat as ℕ using (ℕ; suc; max)
import Cubical.Data.Nat.Order as ℕOrder
open import Cubical.Data.Rationals as Q
open import Cubical.HITs.PropositionalTruncation as PT
open import RegularCauchyStructure
open import CauchyMetricEquivalence
open import CauchyRationalDensity
open import CauchyAddition
open import CauchyAdditionCongruence

eventuallyWithin-sym :
  (x y : RegularCauchy) (k : ℕ) →
  EventuallyWithin x y k → EventuallyWithin y x k
eventuallyWithin-sym x y k =
  PT.map λ { (N , bounds) →
    N , λ n N≤n → snd (bounds n N≤n) , fst (bounds n N≤n) }

composeEventuallyWithin :
  (x y z : RegularCauchy) (k : ℕ) →
  EventuallyWithin x y (suc k) →
  EventuallyWithin y z (suc k) →
  EventuallyWithin x z k
composeEventuallyWithin x y z k xyRelation yzRelation =
  PT.rec isPropPropTrunc (λ { (Nxy , xyBounds) →
    PT.rec isPropPropTrunc (λ { (Nyz , yzBounds) →
      ∣ (ℕ.max Nxy Nyz , λ n max≤n →
        let Nxy≤n = ℕOrder.≤-trans ℕOrder.left-≤-max max≤n
            Nyz≤n = ℕOrder.≤-trans ℕOrder.right-≤-max max≤n
            xy = xyBounds n Nxy≤n
            yz = yzBounds n Nyz≤n
        in
        compose-bound
          (approximation x n) (approximation y n) (approximation z n)
          k (fst xy) (fst yz) ,
        compose-bound
          (approximation z n) (approximation y n) (approximation x n)
          k (snd yz) (snd xy)) ∣₁ }) yzRelation }) xyRelation

record QuantitativelyContinuous
  (f : RegularCauchy → RegularCauchy) : Type where
  field
    modulus : ℕ → ℕ
    preservesEventuallyWithin :
      (x y : RegularCauchy) (k : ℕ) →
      EventuallyWithin x y (modulus k) →
      EventuallyWithin (f x) (f y) k
open QuantitativelyContinuous public

quantitative-continuity-respects-metric :
  {f : RegularCauchy → RegularCauchy} →
  QuantitativelyContinuous f →
  (x y : RegularCauchy) → x ≈metric y → f x ≈metric f y
quantitative-continuity-respects-metric continuity x y relation k =
  preservesEventuallyWithin continuity x y k
    (relation (modulus continuity k))

compose-quantitatively-continuous :
  {f g : RegularCauchy → RegularCauchy} →
  QuantitativelyContinuous f → QuantitativelyContinuous g →
  QuantitativelyContinuous (λ x → f (g x))
compose-quantitatively-continuous {f} {g} fContinuous gContinuous .modulus k =
  modulus gContinuous (modulus fContinuous k)
compose-quantitatively-continuous {f} {g} fContinuous gContinuous
    .preservesEventuallyWithin x y k relation =
  preservesEventuallyWithin fContinuous (g x) (g y) k
    (preservesEventuallyWithin gContinuous x y
      (modulus fContinuous k) relation)

add-pointwise-quantitatively-continuous :
  {f g : RegularCauchy → RegularCauchy} →
  QuantitativelyContinuous f → QuantitativelyContinuous g →
  QuantitativelyContinuous (λ x → addRegular (f x) (g x))
add-pointwise-quantitatively-continuous {f} {g} fContinuous gContinuous .modulus k =
  ℕ.max (modulus fContinuous (suc k)) (modulus gContinuous (suc k))
add-pointwise-quantitatively-continuous {f} {g} fContinuous gContinuous
    .preservesEventuallyWithin x y k relation =
  let fInput = modulus fContinuous (suc k)
      gInput = modulus gContinuous (suc k)
      common = ℕ.max fInput gInput
      fRelation = eventuallyWithin-weaken x y fInput common
        ℕOrder.left-≤-max relation
      gRelation = eventuallyWithin-weaken x y gInput common
        ℕOrder.right-≤-max relation
  in
  addRegular-preserves-eventual (f x) (f y) (g x) (g y) k
    (preservesEventuallyWithin fContinuous x y (suc k) fRelation)
    (preservesEventuallyWithin gContinuous x y (suc k) gRelation)

addRegular-left-quantitatively-continuous :
  (y : RegularCauchy) →
  QuantitativelyContinuous (λ x → addRegular x y)
addRegular-left-quantitatively-continuous y .modulus = suc
addRegular-left-quantitatively-continuous y .preservesEventuallyWithin
    x x′ k relation =
  addRegular-preserves-left-eventual x x′ y k relation

addRegular-right-quantitatively-continuous :
  (x : RegularCauchy) →
  QuantitativelyContinuous (addRegular x)
addRegular-right-quantitatively-continuous x .modulus = suc
addRegular-right-quantitatively-continuous x .preservesEventuallyWithin
    y y′ k relation =
  addRegular-preserves-right-eventual x y y′ k relation

quantitative-continuous-rationally-equal :
  (f g : RegularCauchy → RegularCauchy) →
  QuantitativelyContinuous f → QuantitativelyContinuous g →
  ((q : Q.ℚ) →
    f (constantCauchy q) ≈metric g (constantCauchy q)) →
  (x : RegularCauchy) → f x ≈metric g x
quantitative-continuous-rationally-equal f g fContinuous gContinuous
    rationalAgreement x k =
  let fInput = modulus fContinuous (suc k)
      gInput = modulus gContinuous (suc (suc k))
      tight = ℕ.max fInput gInput
      q = approximation x (suc tight)
      qCloseX = rational-approximation-dense x tight
      xCloseQAtF = eventuallyWithin-weaken x (constantCauchy q)
        fInput tight ℕOrder.left-≤-max
        (eventuallyWithin-sym (constantCauchy q) x tight qCloseX)
      qCloseXAtG = eventuallyWithin-weaken (constantCauchy q) x
        gInput tight ℕOrder.right-≤-max qCloseX
      fEdge = preservesEventuallyWithin fContinuous
        x (constantCauchy q) (suc k) xCloseQAtF
      gEdge = preservesEventuallyWithin gContinuous
        (constantCauchy q) x (suc (suc k)) qCloseXAtG
      rationalEdge = rationalAgreement q (suc (suc k))
      secondEdge = composeEventuallyWithin
        (f (constantCauchy q)) (g (constantCauchy q)) (g x)
        (suc k) rationalEdge gEdge
  in
  composeEventuallyWithin (f x) (f (constantCauchy q)) (g x)
    k fEdge secondEdge
