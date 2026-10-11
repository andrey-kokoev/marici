{-# OPTIONS --safe --cubical --guardedness #-}
module TickComplexConjugation where

open import Cubical.Foundations.Prelude
open import Cubical.Data.Sigma.Base using (_,_; fst; snd)
open import Cubical.Algebra.CommRing
open import Cubical.Tactics.CommRingSolver
open import CauchyCompletionCommRing using (CompletionCommRing)
open import ConstructiveComplexCompletion
import TickComplexCompletionRing as C
import TickPhaseNormTransfer as N

module Laws {ℓ} (R : CommRing ℓ) where
  open CommRingStr (snd R)
  module P = C.PairRing R
  conjugate : P.C → P.C
  conjugate (a , b) = a , (- b)
  normSquared : P.C → fst R
  normSquared (a , b) = a · a + b · b
  real : fst R → P.C
  real a = a , 0r

  abstract
    involutive : (z : P.C) → conjugate (conjugate z) ≡ z
    involutive (a , b) = cong₂ _,_ refl (solve! R)
    additive : (z w : P.C) → conjugate (P.add z w) ≡ P.add (conjugate z) (conjugate w)
    additive (a , b) (c , d) = cong₂ _,_ refl (solve! R)
    multiplicative : (z w : P.C) → conjugate (P.mul z w) ≡ P.mul (conjugate z) (conjugate w)
    multiplicative (a , b) (c , d) = cong₂ _,_ (solve! R) (solve! R)
    conjugate-product : (z : P.C) → P.mul z (conjugate z) ≡ real (normSquared z)
    conjugate-product (a , b) = cong₂ _,_ (solve! R) (solve! R)
    norm-conjugate : (z : P.C) → normSquared (conjugate z) ≡ normSquared z
    norm-conjugate (a , b) = solve! R
    norm-product : (z w : P.C) → normSquared (P.mul z w) ≡ normSquared z · normSquared w
    norm-product (a , b) (c , d) = solve! R

module Operational = Laws CompletionCommRing

conjugation-correspondence : Operational.conjugate ≡ conjugateComplex
conjugation-correspondence = refl
norm-correspondence : Operational.normSquared ≡ N.normSquared
norm-correspondence = refl
