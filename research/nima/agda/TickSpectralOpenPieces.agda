{-# OPTIONS --safe --cubical --guardedness #-}
module TickSpectralOpenPieces where

open import Cubical.Foundations.Prelude
open import Cubical.Foundations.HLevels
open import Cubical.Data.Nat using (ℕ; suc)
import Cubical.Data.Nat.Order as NO
open import Cubical.Data.Sigma using (Σ; _×_)
open import Cubical.HITs.PropositionalTruncation as PT
import Cubical.HITs.SetQuotients as SQ
open import Cubical.Data.Rationals as Q hiding (_+_; _·_; -_)
open import Cubical.Data.Rationals.Order
open import Cubical.Algebra.CommRing
open import Cubical.Tactics.CommRingSolver
open import RegularCauchyStructure
open import CauchyMetricEquivalence
open import CauchyAdditionCongruence using (_+completion_)
open import CauchyNegation using (-completion_)
open import CauchyCompletionAbGroup using (zeroCompletion)
open import CauchyCompletionCommRing using (CompletionCommRing; oneCompletion)
open import TickCompletionMetric
open import TickCompletionDerivative using (CompletionLE; CompletionNonnegative)
open import TickCompletionRingContinuity using (within-negate)
open import TickCompletionLimits
open import TickCompletionOrderLimits using (rational-limit-order; completion-nonnegative-isProp)
open import TickCompletionOrderArithmetic using (completion-order-trans)
open import TickCompletionCoefficientBound using (embedded-order)
import TickCompletionMetricInterval as I
import TickSpectralPiecewiseDerivative as D
import TickSpectralLocalDynamics as Local
import TickSpectralHamiltonian as H
import TickSpectralGlobalPath as Path
module V = D.V
module G = D.G

module Algebra (R : CommRing ℓ-zero) where
  open CommRingStr (snd R)
  abstract
    commute : (a b : fst R) → a + b ≡ b + a
    commute a b = solve! R
    add-zero : (a : fst R) → a + 0r ≡ a
    add-zero a = solve! R
    negate-zero : - 0r ≡ 0r
    negate-zero = solve! R
    cancel-right : (a h : fst R) → (a + (- h)) + h ≡ a
    cancel-right a h = solve! R
module A = Algebra CompletionCommRing

-- Constructive strict order: an explicit positive dyadic gap, truncated.
CompletionLT : MetricCompletionCandidate → MetricCompletionCandidate → Type
CompletionLT a b = ∥ Σ ℕ (λ k → CompletionLE (a +completion embedMetricℚ (precision k)) b) ∥₁

abstract
  ball-upper : (h : MetricCompletionCandidate) (k : ℕ) →
    CompletionWithin zeroCompletion h (suc (suc k)) → CompletionLE h (embedMetricℚ (precision k))
  ball-upper = SQ.elimProp
    (λ h → isPropΠ λ k → isPropΠ λ _ → completion-nonnegative-isProp ((embedMetricℚ (precision k)) +completion (-completion h)))
    (λ x k near → rational-limit-order (λ n → approximation x (suc n)) (λ _ → precision k)
      SQ.[ x ] (embedMetricℚ (precision k)) (rational-approximants-converge x) (constant-converges (embedMetricℚ (precision k)))
      (λ j → PT.map (λ { (threshold , bounds) → threshold , λ n hn →
        isTrans≤ (approximation x (suc n)) (precision k) (precision k Q.+ precision j)
          (subst (approximation x (suc n) ≤_) (Q.+IdL (precision k))
            (snd (bounds (suc n) (NO.≤-trans hn NO.≤-sucℕ))))
          (≤-add-nonnegative (precision k) (precision j) (precision-nonnegative j)) })
        (within-representatives (constantCauchy 0) x k near)))

  ball-negative-upper : (h : MetricCompletionCandidate) (k : ℕ) →
    CompletionWithin zeroCompletion h (suc (suc k)) → CompletionLE (-completion h) (embedMetricℚ (precision k))
  ball-negative-upper h k near = ball-upper (-completion h) k
    (subst (λ a → CompletionWithin a (-completion h) (suc (suc k))) A.negate-zero
      (within-negate zeroCompletion h (suc (suc k)) near))

  order-add-left : (c a b : MetricCompletionCandidate) → CompletionLE a b → CompletionLE (c +completion a) (c +completion b)
  order-add-left c a b bound = subst2 CompletionLE (A.commute a c) (A.commute b c) (I.order-translate a b c bound)

  margin-above-center : (t : MetricCompletionCandidate) (k : ℕ) → CompletionLE t (t +completion embedMetricℚ (precision k))
  margin-above-center t k = subst (λ a → CompletionLE a (t +completion embedMetricℚ (precision k))) (A.add-zero t)
    (order-add-left t zeroCompletion (embedMetricℚ (precision k)) (embedded-order 0 (precision k) (precision-nonnegative k)))

  strict-before-neighborhood : (t : MetricCompletionCandidate) → CompletionLT t oneCompletion → D.BeforeSeam t
  strict-before-neighborhood t = PT.rec
    (isProp× (completion-nonnegative-isProp (oneCompletion +completion (-completion t))) isPropPropTrunc)
    (λ { (k , margin) →
      completion-order-trans t (t +completion embedMetricℚ (precision k)) oneCompletion (margin-above-center t k) margin ,
      ∣ suc (suc k) , (λ h near → completion-order-trans (t +completion h)
        (t +completion embedMetricℚ (precision k)) oneCompletion
        (order-add-left t h (embedMetricℚ (precision k)) (ball-upper h k near)) margin) ∣₁ })

  strict-after-neighborhood : (t : MetricCompletionCandidate) → CompletionLT oneCompletion t → D.AfterSeam t
  strict-after-neighborhood t = PT.rec
    (isProp× (completion-nonnegative-isProp (t +completion (-completion oneCompletion))) isPropPropTrunc)
    (λ { (k , margin) →
      completion-order-trans oneCompletion (oneCompletion +completion embedMetricℚ (precision k)) t (margin-above-center oneCompletion k) margin ,
      ∣ suc (suc k) , (λ h near → subst (λ a → CompletionLE a (t +completion h)) (A.cancel-right oneCompletion h)
        (I.order-translate (oneCompletion +completion (-completion h)) t h
          (completion-order-trans (oneCompletion +completion (-completion h))
            (oneCompletion +completion embedMetricℚ (precision k)) t
            (order-add-left oneCompletion (-completion h) (embedMetricℚ (precision k)) (ball-negative-upper h k near)) margin))) ∣₁ })

FirstOpenPiece SecondOpenPiece : Type
FirstOpenPiece = Σ I.ReturnInterval (λ t → CompletionLT zeroCompletion (fst t) × CompletionLT (fst t) oneCompletion)
SecondOpenPiece = Σ I.ReturnInterval (λ t → CompletionLT oneCompletion (fst t) × CompletionLT (fst t) I.twoCompletion)

abstract
  return-first-open-generator : (r : G.Schedule) (s : V.Label) (u : FirstOpenPiece) →
    Local.HasVectorMetricDerivative (D.returnCurve r s) (fst (fst u))
      (V.scale H.minusI (H.hamiltonian (Path.permute (D.firstIndex r)) (D.returnCurve r s (fst (fst u)))))
  return-first-open-generator r s (t , lower , upper) = D.return-first-hamiltonian r s (fst t)
    (strict-before-neighborhood (fst t) upper)

  return-second-open-generator : (r : G.Schedule) (s : V.Label) (u : SecondOpenPiece) →
    Local.HasVectorMetricDerivative (D.returnCurve r s) (fst (fst u))
      (V.scale H.minusI (H.hamiltonian (Path.permute (D.secondIndex r)) (D.returnCurve r s (fst (fst u)))))
  return-second-open-generator r s (t , lower , upper) = D.return-second-hamiltonian r s (fst t)
    (strict-after-neighborhood (fst t) lower)
