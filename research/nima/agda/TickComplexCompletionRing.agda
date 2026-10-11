{-# OPTIONS --safe --cubical --guardedness #-}
module TickComplexCompletionRing where

open import Cubical.Foundations.Prelude
open import Cubical.Foundations.HLevels using (isSet×)
open import Cubical.Data.Sigma.Base using (_×_; _,_; fst; snd)
open import Cubical.Algebra.CommRing
open import Cubical.Tactics.CommRingSolver
open import CauchyCompletionCommRing using (CompletionCommRing)
open import ConstructiveComplexCompletion

-- Prove symbolic component identities before instantiating the operational
-- completion; reflection never needs to normalize its Cauchy schedules.
module PairRing {ℓ} (R : CommRing ℓ) where
  open CommRingStr (snd R)
  C = fst R × fst R
  add : C → C → C
  add (a , b) (c , d) = (a + c) , (b + d)
  mul : C → C → C
  mul (a , b) (c , d) = (a · c + (- (b · d))) , (a · d + b · c)
  neg : C → C
  neg (a , b) = (- a) , (- b)
  zero one : C
  zero = 0r , 0r
  one = 1r , 0r

  abstract
    add-assoc : (x y z : C) → add x (add y z) ≡ add (add x y) z
    add-assoc (a , b) (c , d) (e , f) = cong₂ _,_ (solve! R) (solve! R)
    add-zero : (x : C) → add x zero ≡ x
    add-zero (a , b) = cong₂ _,_ (solve! R) (solve! R)
    add-inverse : (x : C) → add x (neg x) ≡ zero
    add-inverse (a , b) = cong₂ _,_ (solve! R) (solve! R)
    add-comm : (x y : C) → add x y ≡ add y x
    add-comm (a , b) (c , d) = cong₂ _,_ (solve! R) (solve! R)
    mul-assoc : (x y z : C) → mul x (mul y z) ≡ mul (mul x y) z
    mul-assoc (a , b) (c , d) (e , f) = cong₂ _,_ (solve! R) (solve! R)
    mul-one : (x : C) → mul x one ≡ x
    mul-one (a , b) = cong₂ _,_ (solve! R) (solve! R)
    mul-distrib : (x y z : C) → mul x (add y z) ≡ add (mul x y) (mul x z)
    mul-distrib (a , b) (c , d) (e , f) = cong₂ _,_ (solve! R) (solve! R)
    mul-comm : (x y : C) → mul x y ≡ mul y x
    mul-comm (a , b) (c , d) = cong₂ _,_ (solve! R) (solve! R)

  ring : CommRing ℓ
  ring = makeCommRing zero one add mul neg (isSet× is-set is-set)
    add-assoc add-zero add-inverse add-comm mul-assoc mul-one mul-distrib mul-comm

module Operational = PairRing CompletionCommRing

-- All five operations are definitionally the existing implementation.
ComplexCompletionCommRing : CommRing ℓ-zero
ComplexCompletionCommRing = Operational.ring

carrier-correspondence : fst ComplexCompletionCommRing ≡ ComplexCompletion
carrier-correspondence = refl
addition-correspondence : Operational.add ≡ _+complex_
addition-correspondence = refl
multiplication-correspondence : Operational.mul ≡ _·complex_
multiplication-correspondence = refl
negation-correspondence : Operational.neg ≡ negComplex
negation-correspondence = refl
zero-correspondence : Operational.zero ≡ zeroComplex
zero-correspondence = refl
one-correspondence : Operational.one ≡ oneComplex
one-correspondence = refl
