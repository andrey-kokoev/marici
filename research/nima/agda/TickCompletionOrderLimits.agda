{-# OPTIONS --safe --cubical --guardedness #-}
module TickCompletionOrderLimits where

open import Cubical.Foundations.Prelude
open import Cubical.Foundations.HLevels
open import Cubical.Data.Nat using (ℕ; suc)
import Cubical.Data.Nat.Order as N
open import Cubical.Data.Sigma using (Σ; _×_)
open import Cubical.HITs.PropositionalTruncation as PT
import Cubical.HITs.SetQuotients as SQ
open import Cubical.Data.Rationals as Q
open import Cubical.Data.Rationals.Order
open import Cubical.Algebra.CommRing
open import Cubical.Tactics.CommRingSolver
open import RationalAnalyticSubstrate using (PreferredℚCommRing)
open import RegularCauchyStructure
open import CauchyMetricEquivalence
open import CauchyAdditionCongruence using (_+completion_)
open import CauchyNegation using (-completion_)
open import CauchyCompletionMultiplication
open import ConstructiveComplexCompletion using (complex)
open import TickCompletionMetric
open import TickCompletionDerivative
open import TickCompletionLimits
open import TickCompletionRingContinuity
open import TickRationalProductLimits

module Algebra {ℓ} (R : CommRing ℓ) where
  open CommRingStr (snd R) renaming (_+_ to _+S_; _·_ to _·S_; -_ to -S_)
  cancel-slack : (a e : fst R) → (a +S e) +S (-S e) ≡ a
  cancel-slack a e = solve! R
  negative-double : (e : fst R) → (-S e) +S (-S e) ≡ -S (e +S e)
  negative-double e = solve! R
  left-shift : (p e : fst R) → p +S ((-S p) +S (-S e)) ≡ -S e
  left-shift p e = solve! R
  right-shift : (q p e : fst R) → (q +S e) +S ((-S p) +S (-S e)) ≡ q +S (-S p)
  right-shift q p e = solve! R
module R = Algebra PreferredℚCommRing

abstract
  lower-transfer : (q a e : Q.ℚ) → Q.- e ≤ q → q ≤ a Q.+ e →
    Q.- (e Q.+ e) ≤ a
  lower-transfer q a e lower near = subst2 _≤_
    (R.negative-double e) (R.cancel-slack a e)
    (≤-+o (Q.- e) (a Q.+ e) (Q.- e) (isTrans≤ (Q.- e) q (a Q.+ e) lower near))

  slack-difference-nonnegative : (p q e : Q.ℚ) → p ≤ q Q.+ e →
    Q.- e ≤ q Q.+ (Q.- p)
  slack-difference-nonnegative p q e bound = subst2 _≤_
    (R.left-shift p e) (R.right-shift q p e)
    (≤-+o p (q Q.+ e) ((Q.- p) Q.+ (Q.- e)) bound)

  completion-nonnegative-isProp : (a : MetricCompletionCandidate) → isProp (CompletionNonnegative a)
  completion-nonnegative-isProp a = isPropΠ (λ _ → isPropPropTrunc)

  -- Closedness of the actual existential-representative cone. The two bits
  -- spent on representative comparison are additional to the one slack bit.
  rational-limit-nonnegative : (r : ℕ → Q.ℚ) (a : MetricCompletionCandidate) →
    Converges (λ n → embedMetricℚ (r n)) a →
    ((k : ℕ) → Eventually (λ n → Q.- precision k ≤ r n)) → CompletionNonnegative a
  rational-limit-nonnegative r = SQ.elimProp
    (λ a → isPropΠ (λ _ → isPropΠ (λ _ → completion-nonnegative-isProp a)))
    (λ x converges lower k → PT.rec isPropPropTrunc
      (λ { (threshold , evidence) →
        let n = threshold
            near = fst (evidence n N.≤-refl)
            nonnegative = snd (evidence n N.≤-refl)
        in PT.map (λ { (j₀ , comparison) → x , refl , ∣ j₀ , (λ j hj →
          subst (λ e → Q.- e ≤ approximation x j) (precision-refines-double k)
            (lower-transfer (r n) (approximation x j) (precision (suc k))
              nonnegative (snd (comparison j hj)))) ∣₁ })
          (within-representatives x (constantCauchy (r n)) (suc k) near) })
      (eventually-zip (λ n near positive → near , positive)
        (converges (suc (suc (suc k)))) (lower (suc k))))

  -- The bound itself may move with n. No fixed absolute budget replaces it.
  rational-limit-order : (r s : ℕ → Q.ℚ) (a b : MetricCompletionCandidate) →
    Converges (λ n → embedMetricℚ (r n)) a →
    Converges (λ n → embedMetricℚ (s n)) b →
    ((k : ℕ) → Eventually (λ n → r n ≤ s n Q.+ precision k)) → CompletionLE a b
  rational-limit-order r s a b ha hb bounds = rational-limit-nonnegative
    (λ n → s n Q.+ (Q.- r n)) (b +completion (-completion a))
    (rational-sum-sequence-converges s (λ n → Q.- r n) b (-completion a) hb
      (rational-negative-sequence-converges r a ha))
    (λ k → eventually-map (λ n → slack-difference-nonnegative (r n) (s n) (precision k)) (bounds k))

  rational-moving-product-converges : (r s : ℕ → Q.ℚ) (a b : MetricCompletionCandidate) →
    Converges (λ n → embedMetricℚ (r n)) a →
    Converges (λ n → embedMetricℚ (s n)) b →
    Converges (λ n → embedMetricℚ (r n Q.· s n)) (preferredCompletionMultiplication a b)
  rational-moving-product-converges r s a b ha hb = converges-pointwise-path
    (λ n → preferredCompletionMultiplication (embedMetricℚ (r n)) (embedMetricℚ (s n)))
    (λ n → embedMetricℚ (r n Q.· s n)) (preferredCompletionMultiplication a b)
    (λ n → preferredCompletionMultiplication-preserves-rationals (r n) (s n))
    (joint-continuous-limit preferredCompletionMultiplication multiplication-joint-continuous
      (λ n → embedMetricℚ (r n)) (λ n → embedMetricℚ (s n)) a b ha hb)

  -- Relative first-order estimates survive the limit, including at h=0.
  -- The rational estimate is still an explicit premise, not asserted here.
  rational-quadratic-bound-limit : (r s u : ℕ → Q.ℚ) (x y h : MetricCompletionCandidate) (e : Q.ℚ) →
    Converges (λ n → embedMetricℚ (r n)) x →
    Converges (λ n → embedMetricℚ (s n)) y →
    Converges (λ n → embedMetricℚ (u n)) h →
    ((k : ℕ) → Eventually (λ n →
      (r n Q.· r n) Q.+ (s n Q.· s n) ≤ (e Q.· e) Q.· (u n Q.· u n) Q.+ precision k)) →
    CompletionLE (complexNormSquared (complex x y))
      (preferredCompletionMultiplication (embedMetricℚ (e Q.· e)) (squareCompletion h))
  rational-quadratic-bound-limit r s u x y h e hr hs hu = rational-limit-order
    (λ n → (r n Q.· r n) Q.+ (s n Q.· s n))
    (λ n → (e Q.· e) Q.· (u n Q.· u n))
    (complexNormSquared (complex x y))
    (preferredCompletionMultiplication (embedMetricℚ (e Q.· e)) (squareCompletion h))
    (rational-sum-sequence-converges (λ n → r n Q.· r n) (λ n → s n Q.· s n)
      (squareCompletion x) (squareCompletion y)
      (rational-moving-product-converges r r x x hr hr)
      (rational-moving-product-converges s s y y hs hs))
    (rational-product-sequence-converges (e Q.· e) (λ n → u n Q.· u n) (squareCompletion h)
      (rational-moving-product-converges u u h h hu hu))
