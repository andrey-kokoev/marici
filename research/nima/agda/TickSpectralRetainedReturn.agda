{-# OPTIONS --safe --cubical --guardedness #-}
module TickSpectralRetainedReturn where

open import Cubical.Foundations.Prelude
open import Cubical.Data.Sigma.Base using (_×_; _,_)
open import Cubical.Data.Bool.Base using (false; true)
open import Cubical.Data.Empty as Empty using (⊥)
open import CauchyCompletionCommRing using (oneCompletion)
open import TickCompletionOrderArithmetic using (completion-order-refl)
import TickRetainedStructure as S
import TickCompletionMetricInterval as I
import TickSpectralLocalOperators as L
import TickSpectralProjectorLaws as P
import TickSpectralGlobalPath as Path
import TickSpectralLocalNorm as Norm
import TickComplexNativeBasis as B
module G = S.G
module V = L.V

nativeTarget : V.Label → V.Vector
nativeTarget s = V.right (V.left (B.basis s))

-- The tags name the forward schedule. Return traverses its reversed order,
-- but continues with the positive operational phase on both legs.
returnPath : G.Schedule → V.Label → I.ReturnInterval → V.Vector
returnPath G.leftFirst s = Path.intervalPath P.rightIndex P.leftIndex (nativeTarget s)
returnPath G.rightFirst s = Path.intervalPath P.leftIndex P.rightIndex (nativeTarget s)

native-label-target : (s : V.Label) → G.run G.leftFirst s ≡ P.rightIndex (P.leftIndex s)
native-label-target (false , false) = refl
native-label-target (false , true) = refl
native-label-target (true , false) = refl
native-label-target (true , true) = refl

abstract
  native-target-correspondence : (s : V.Label) → nativeTarget s ≡ B.basis (G.run G.leftFirst s)
  native-target-correspondence s = cong V.right (B.Operational.basis-left s)
    ∙ B.Operational.basis-right (P.leftIndex s) ∙ cong B.basis (sym (native-label-target s))

  return-start : (r : G.Schedule) (s : V.Label) → returnPath r s I.start ≡ nativeTarget s
  return-start G.leftFirst s = Path.interval-start P.rightIndex P.leftIndex (nativeTarget s)
  return-start G.rightFirst s = Path.interval-start P.leftIndex P.rightIndex (nativeTarget s)

  return-finish : (r : G.Schedule) (s : V.Label) → returnPath r s I.finish ≡ B.basis s
  return-finish G.leftFirst s = Path.interval-finish P.rightIndex P.leftIndex (nativeTarget s)
    ∙ cong V.left (V.right-involutive (V.left (B.basis s))) ∙ V.left-involutive (B.basis s)
  return-finish G.rightFirst s = Path.interval-finish P.leftIndex P.rightIndex (nativeTarget s)
    ∙ cong V.right (V.flips-commute (V.left (B.basis s)))
    ∙ cong (λ v → V.right (V.right v)) (V.left-involutive (B.basis s)) ∙ V.right-involutive (B.basis s)

  return-continuous : (r : G.Schedule) (s : V.Label) → Path.IntervalPathContinuous (returnPath r s)
  return-continuous G.leftFirst s = Path.interval-path-continuous P.rightIndex P.leftIndex (nativeTarget s)
  return-continuous G.rightFirst s = Path.interval-path-continuous P.leftIndex P.rightIndex (nativeTarget s)

  target-unit-norm : (s : V.Label) → Norm.vectorNormSquared (nativeTarget s) ≡ oneCompletion
  target-unit-norm s = cong Norm.vectorNormSquared
    (cong V.right (B.Operational.basis-left s) ∙ B.Operational.basis-right (P.leftIndex s))
    ∙ B.basis-unit-norm (P.rightIndex (P.leftIndex s))

  return-unit-norm : (r : G.Schedule) (s : V.Label) (t : I.ReturnInterval) →
    Norm.vectorNormSquared (returnPath r s t) ≡ oneCompletion
  return-unit-norm G.leftFirst s t = Path.right-then-left-norm (fst t) (nativeTarget s) ∙ target-unit-norm s
  return-unit-norm G.rightFirst s t = Path.left-then-right-norm (fst t) (nativeTarget s) ∙ target-unit-norm s

  leftFirst-seam : (s : V.Label) → returnPath G.leftFirst s I.seam ≡ B.basis (P.leftIndex s)
  leftFirst-seam s = Path.glued-on-left P.rightIndex P.leftIndex oneCompletion (nativeTarget s) (completion-order-refl oneCompletion)
    ∙ L.right-finish (nativeTarget s) ∙ V.right-involutive (V.left (B.basis s)) ∙ B.Operational.basis-left s
  rightFirst-seam : (s : V.Label) → returnPath G.rightFirst s I.seam ≡ B.basis (P.rightIndex s)
  rightFirst-seam s = Path.glued-on-left P.leftIndex P.rightIndex oneCompletion (nativeTarget s) (completion-order-refl oneCompletion)
    ∙ L.left-finish (nativeTarget s) ∙ V.flips-commute (V.left (B.basis s))
    ∙ cong V.right (V.left-involutive (B.basis s)) ∙ B.Operational.basis-right s

  seam-separation : (s : V.Label) → returnPath G.leftFirst s I.seam ≡ returnPath G.rightFirst s I.seam → ⊥
  seam-separation s equal = B.distinct-native-seams s (sym (leftFirst-seam s) ∙ equal ∙ rightFirst-seam s)

  schedule-faithful : (s : V.Label) (r q : G.Schedule) → returnPath r s ≡ returnPath q s → r ≡ q
  schedule-faithful s G.leftFirst G.leftFirst equal = refl
  schedule-faithful s G.rightFirst G.rightFirst equal = refl
  schedule-faithful s G.leftFirst G.rightFirst equal = Empty.rec (seam-separation s (cong (λ f → f I.seam) equal))
  schedule-faithful s G.rightFirst G.leftFirst equal = Empty.rec (seam-separation s (sym (cong (λ f → f I.seam) equal)))

module AtSource (s : V.Label) where
  module T = S.AtSource s
  Paths : Type
  Paths = (I.ReturnInterval → V.Vector) × (I.ReturnInterval → V.Vector)
  realize-tags : G.Schedule × G.Schedule → Paths
  realize-tags (r , q) = returnPath r s , returnPath q s
  realize : T.A.Tick → Paths
  realize t = realize-tags (T.tags t)
  swap : Paths → Paths
  swap (p , q) = q , p

  abstract
    reconstruction-coherence : (t : T.A.Tick) → realize t ≡ realize (T.rebuild (T.tags t))
    reconstruction-coherence = T.observation-factors realize
    schedule-swap : (r q : G.Schedule) → realize (T.rebuild (q , r)) ≡ swap (realize (T.rebuild (r , q)))
    schedule-swap r q = refl
    fixed-source-faithful : (t u : T.A.Tick) → realize t ≡ realize u → t ≡ u
    fixed-source-faithful t u equal = T.tags-injective t u (cong₂ _,_
      (schedule-faithful s (fst (T.tags t)) (fst (T.tags u)) (cong fst equal))
      (schedule-faithful s (snd (T.tags t)) (snd (T.tags u)) (cong snd equal)))
