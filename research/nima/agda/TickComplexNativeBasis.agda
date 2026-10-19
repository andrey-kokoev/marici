{-# OPTIONS --safe --cubical --guardedness #-}
module TickComplexNativeBasis where

open import Cubical.Foundations.Prelude
open import Cubical.Data.Bool.Base using (Bool; false; true)
open import Cubical.Data.Sigma.Base using (_,_)
open import Cubical.Data.Empty using (⊥)
open import Cubical.Algebra.CommRing
open import Cubical.Tactics.CommRingSolver
open import CauchyCompletionCommRing using (CompletionCommRing; oneCompletion)
open import ConstructiveComplexCompletion
import TickComplexCompletionRing as Ring
import TickComplexConjugation as Conj
import TickComplexNativeOperators as Native
import TickSpectralProjectorLaws as P
import TickSpectralLocalNorm as Norm
open import TickLocalReturnSection using (zero-not-one)

module Basis (R : CommRing ℓ-zero) where
  open CommRingStr (snd R)
  module V = Native.Native (fst R) _+_ _·_
  delta : Bool → Bool → fst R
  delta false false = 1r
  delta false true = 0r
  delta true false = 0r
  delta true true = 1r
  basis : V.Label → V.Vector
  basis (a , b) (c , d) = delta a c · delta b d
  delta-self : (a : Bool) → delta a a ≡ 1r
  delta-self false = refl
  delta-self true = refl
  delta-other : (a : Bool) → delta a (V.flip a) ≡ 0r
  delta-other false = refl
  delta-other true = refl
  delta-flipped : (a : Bool) → delta (V.flip a) a ≡ 0r
  delta-flipped false = refl
  delta-flipped true = refl
  delta-flip : (a b : Bool) → delta a (V.flip b) ≡ delta (V.flip a) b
  delta-flip false false = refl
  delta-flip false true = refl
  delta-flip true false = refl
  delta-flip true true = refl
  abstract
    basis-self : (s : V.Label) → basis s s ≡ 1r
    basis-self (a , b) = cong₂ _·_ (delta-self a) (delta-self b) ∙ ·IdR 1r
    basis-left : (s : V.Label) → V.left (basis s) ≡ basis (P.leftIndex s)
    basis-left (a , b) = funExt λ { (c , d) → cong (_· delta b d) (delta-flip a c) }
    basis-right : (s : V.Label) → V.right (basis s) ≡ basis (P.rightIndex s)
    basis-right (a , b) = funExt λ { (c , d) → cong (delta a c ·_) (delta-flip b d) }
    zero-product : 0r · 0r ≡ 0r
    zero-product = solve! R
    right-at-left : (s : V.Label) → basis (P.rightIndex s) (P.leftIndex s) ≡ 0r
    right-at-left (a , b) = cong₂ _·_ (delta-other a) (delta-flipped b) ∙ zero-product

module Operational = Basis Ring.ComplexCompletionCommRing
open Operational public using (basis)

module NormIdentity (R : CommRing ℓ-zero) where
  open CommRingStr (snd R)
  module C = Ring.PairRing R
  module B = Basis C.ring
  module N = Conj.Laws R
  norm : B.V.Vector → fst R
  norm v = (N.normSquared (v (false , false)) + N.normSquared (v (false , true))) +
    (N.normSquared (v (true , false)) + N.normSquared (v (true , true)))
  abstract
    basis-unit-norm : (s : B.V.Label) → norm (B.basis s) ≡ 1r
    basis-unit-norm (false , false) = solve! R
    basis-unit-norm (false , true) = solve! R
    basis-unit-norm (true , false) = solve! R
    basis-unit-norm (true , true) = solve! R
module N = NormIdentity CompletionCommRing

abstract
  basis-unit-norm : (s : Operational.V.Label) → Norm.vectorNormSquared (basis s) ≡ oneCompletion
  basis-unit-norm = N.basis-unit-norm
  distinct-native-seams : (s : Operational.V.Label) → basis (P.leftIndex s) ≡ basis (P.rightIndex s) → ⊥
  distinct-native-seams s equal = zero-not-one (sym (cong realPart
    (sym (Operational.basis-self (P.leftIndex s))
      ∙ cong (λ v → v (P.leftIndex s)) equal ∙ Operational.right-at-left s)))
