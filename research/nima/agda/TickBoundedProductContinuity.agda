{-# OPTIONS --safe --cubical --guardedness #-}
module TickBoundedProductContinuity where

open import Cubical.Foundations.Prelude
open import Cubical.Foundations.HLevels using (isPropΠ)
open import Cubical.Data.Nat as ℕ using (ℕ; zero; suc; max; _+_)
open import Cubical.Data.Sigma using (_×_; Σ-syntax)
open import Cubical.HITs.PropositionalTruncation as PT
open import Cubical.HITs.SetQuotients using ([_])
open import RegularCauchyStructure
open import CauchyMetricEquivalence
open import RationallyBoundedCauchy using (canonicalRadius)
open import DyadicallyBoundedCauchy
open import DyadicallyBoundedCauchyMultiplication using (multiplyDyadicallyBounded)
open import DyadicBoundNormalization using (commonExponent)
open import CauchyProductRegularity using (boundedProductRegular)
open import CauchyProductCongruence using (bounded-product-preserves-eventual)
open import CauchyProductWitnessCoherence using (productClassFromDominance-from-presentations)
open import CauchyCompletionMultiplication
open import TickQuotientContinuity using (CompletionNear)

max-self : (n : ℕ) → max n n ≡ n
max-self zero = refl
max-self (suc n) = cong suc (max-self n)

-- Both representatives have a specified common magnitude exponent.
-- Keeping this condition explicit avoids claiming global uniform continuity
-- of multiplication on an unbounded scalar carrier.
BoundedNear : ℕ → ℕ → MetricCompletionCandidate → MetricCompletionCandidate → Type
BoundedNear d k u v = ∥ Σ[ x ∈ DyadicallyBoundedRegularCauchy ]
  Σ[ y ∈ DyadicallyBoundedRegularCauchy ]
  ((radius-exponent x ≡ d) × ((radius-exponent y ≡ d) ×
  (([ regular x ] ≡ u) × (([ regular y ] ≡ v) ×
  EventuallyWithin (regular x) (regular y) k)))) ∥₁

product-on-bounded : (x y : DyadicallyBoundedRegularCauchy)
  → [ boundedProductRegular x y ]
    ≡ preferredCompletionMultiplication [ regular x ] [ regular y ]
product-on-bounded x y = sym
  (productClassFromDominance-from-presentations {x = regular x} {y = regular y}
    (dominates-all preferredRationalDyadicArchimedean (canonicalRadius (regular x)))
    (dominates-all preferredRationalDyadicArchimedean (canonicalRadius (regular y)))
    (x , refl) (y , refl))

common-at : (x y : DyadicallyBoundedRegularCauchy) (d : ℕ)
  → radius-exponent x ≡ d → radius-exponent y ≡ d → commonExponent x y ≡ d
common-at x y d px py = cong₂ max px py ∙ max-self d

product-precision : ℕ → ℕ → ℕ → ℕ
product-precision d e k = suc (d + e) + suc (suc (suc k))

-- A joint, radius-dependent quantitative bound for the ACTUAL completion
-- multiplication used in TickPolynomialRealization's completion instance.
product-retains-bounded-near : (d e k : ℕ)
  (u u′ v v′ : MetricCompletionCandidate)
  → BoundedNear d (product-precision d e k) u u′
  → BoundedNear e (product-precision d e k) v v′
  → BoundedNear (d + e) k
      (preferredCompletionMultiplication u v)
      (preferredCompletionMultiplication u′ v′)
product-retains-bounded-near d e k u u′ v v′ =
  PT.rec (isPropΠ λ _ → isPropPropTrunc)
    λ { (x , x′ , dx , dx′ , px , px′ , closeX) →
      PT.map λ { (y , y′ , ey , ey′ , py , py′ , closeY) →
        multiplyDyadicallyBounded x y , multiplyDyadicallyBounded x′ y′ ,
        cong₂ _+_ dx ey , cong₂ _+_ dx′ ey′ ,
        (product-on-bounded x y ∙ cong₂ preferredCompletionMultiplication px py) ,
        (product-on-bounded x′ y′ ∙ cong₂ preferredCompletionMultiplication px′ py′) ,
        bounded-product-preserves-eventual x x′ y y′ k
          (subst (EventuallyWithin (regular x) (regular x′))
            (sym (cong (λ n → suc n + suc (suc (suc k)))
              (cong₂ _+_ (common-at x x′ d dx dx′) (common-at y y e ey ey)))) closeX)
          (subst (EventuallyWithin (regular y) (regular y′))
            (sym (cong (λ n → suc n + suc (suc (suc k)))
              (cong₂ _+_ (common-at x′ x′ d dx′ dx′) (common-at y y′ e ey ey′)))) closeY) } }

forget-bound : {d k : ℕ} {u v : MetricCompletionCandidate}
  → BoundedNear d k u v → CompletionNear k u v
forget-bound = PT.map λ { (x , y , dx , dy , px , py , close) →
  regular x , regular y , px , py , close }

product-preserves-bounded-near : (d e k : ℕ)
  (u u′ v v′ : MetricCompletionCandidate)
  → BoundedNear d (product-precision d e k) u u′
  → BoundedNear e (product-precision d e k) v v′
  → CompletionNear k (preferredCompletionMultiplication u v)
      (preferredCompletionMultiplication u′ v′)
product-preserves-bounded-near d e k u u′ v v′ hx hy =
  forget-bound {d = d + e} {k = k}
    (product-retains-bounded-near d e k u u′ v v′ hx hy)
