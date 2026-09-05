{-# OPTIONS --safe --cubical --no-import-sorts --guardedness --lossy-unification #-}
module ExponentialSeedConstruction where

open import Cubical.Foundations.Prelude
open import Cubical.Data.Nat using (zero; suc)
open import Cubical.Data.Rationals as Q
open import Cubical.Data.Sigma
open import Cubical.HITs.PropositionalTruncation as PT
open import Cubical.HITs.SetQuotients as SQ using ([_])
open import RegularCauchyStructure
open import RationallyBoundedCauchy
open import RationalArchimedean
open import CauchyBoundPromotion
open import DyadicallyBoundedCauchy
open import CauchyProductBounds
open import CauchyProductErrorBounds
open import RationalTaylorApproximants
open import ExponentialTailSchedule
open import ExponentialSeedCoherence
open import CauchyMetricEquivalence

preferred-dyadic-dominance : (q : Q.ℚ) → DyadicDominates q
preferred-dyadic-dominance =
  truncated-ceiling-principle-gives-dyadic-dominance
    (raw-ceiling-gives-truncated-principle
      preferred-raw-rational-natural-ceiling)

presentation-value-bound : (q : Q.ℚ) →
  (presentation : BoundedPresentation (constantCauchy q)) →
  MagnitudeBound q (dyadicRadius (radius-exponent (fst presentation)))
presentation-value-bound q (bounded , sourcePath) =
  transport-magnitude q (approximation (regular bounded) zero)
    (dyadicRadius (radius-exponent bounded))
    (sym (cong (λ z → approximation z zero) sourcePath))
    (bounded-value bounded zero)

TruncatedExponentialTailSeed : Q.ℚ → Type
TruncatedExponentialTailSeed q = ∥ ExponentialTailSeed q ∥₁

truncated-exponential-tail-seed-isProp : (q : Q.ℚ) →
  isProp (TruncatedExponentialTailSeed q)
truncated-exponential-tail-seed-isProp q = isPropPropTrunc

exponential-seed-from-presentations : (q : Q.ℚ) →
  (inputPresentation : BoundedPresentation (constantCauchy q)) →
  let inputExponent = radius-exponent (fst inputPresentation)
      seedTerm = exponentialTerm q (dyadicNat (suc inputExponent))
  in
  BoundedPresentation (constantCauchy seedTerm) →
  ExponentialTailSeed q
exponential-seed-from-presentations q inputPresentation seedPresentation = record
  { inputExponent = radius-exponent (fst inputPresentation)
  ; inputBound = presentation-value-bound q inputPresentation
  ; seedExponent = radius-exponent (fst seedPresentation)
  ; seedBound = presentation-value-bound _ seedPresentation
  }

preferred-truncated-exponential-tail-seed :
  (q : Q.ℚ) → TruncatedExponentialTailSeed q
preferred-truncated-exponential-tail-seed q =
  PT.rec isPropPropTrunc
    (λ inputPresentation →
      let inputExponent = radius-exponent (fst inputPresentation)
          seedTerm = exponentialTerm q (dyadicNat (suc inputExponent))
          seedDominance = preferred-dyadic-dominance
            (canonicalRadius (constantCauchy seedTerm))
      in
      PT.rec isPropPropTrunc
        (λ seedPresentation →
          ∣ exponential-seed-from-presentations
              q inputPresentation seedPresentation ∣₁)
        (promote-regular-presentation-truncated
          (constantCauchy seedTerm) seedDominance))
    (promote-regular-presentation-truncated
      (constantCauchy q)
      (preferred-dyadic-dominance
        (canonicalRadius (constantCauchy q))))

exponentialSeedClass : {q : Q.ℚ} →
  ExponentialTailSeed q → MetricCompletionCandidate
exponentialSeedClass seed = [ absorbedExponentialRegular seed ]

exponentialSeedClass-2constant : {q : Q.ℚ} →
  (first second : ExponentialTailSeed q) →
  exponentialSeedClass first ≡ exponentialSeedClass second
exponentialSeedClass-2constant first second =
  SQ.eq/ _ _ (exponential-seeds-metric-equivalent first second)

abstract
  rationalExponentialValue : Q.ℚ → MetricCompletionCandidate
  rationalExponentialValue q =
    rec→Set metric-candidate-isSet
      exponentialSeedClass
      exponentialSeedClass-2constant
      (preferred-truncated-exponential-tail-seed q)

  exponential-class-from-truncated : {q : Q.ℚ} →
    (seeds : TruncatedExponentialTailSeed q) →
    (chosen : ExponentialTailSeed q) →
    rec→Set metric-candidate-isSet
      exponentialSeedClass exponentialSeedClass-2constant seeds ≡
    exponentialSeedClass chosen
  exponential-class-from-truncated seeds chosen =
    cong
      (rec→Set metric-candidate-isSet
        exponentialSeedClass exponentialSeedClass-2constant)
      (squash₁ seeds ∣ chosen ∣₁)

  rationalExponentialValue-from-seed : (q : Q.ℚ) →
    (chosen : ExponentialTailSeed q) →
    rationalExponentialValue q ≡ exponentialSeedClass chosen
  rationalExponentialValue-from-seed q chosen =
    exponential-class-from-truncated
      (preferred-truncated-exponential-tail-seed q) chosen

  rationalExponentialValue-from-seed-path : (q : Q.ℚ) →
    (chosen : ExponentialTailSeed q) → (target : RegularCauchy) →
    absorbedExponentialRegular chosen ≡ target →
    rationalExponentialValue q ≡ SQ.[ target ]
  rationalExponentialValue-from-seed-path q chosen target path =
    rationalExponentialValue-from-seed q chosen ∙ cong SQ.[_] path

  rationalExponentialValue-zero-from-seed-path :
    (chosen : ExponentialTailSeed 0) →
    absorbedExponentialRegular chosen ≡ constantCauchy 1 →
    rationalExponentialValue 0 ≡ SQ.[ constantCauchy 1 ]
  rationalExponentialValue-zero-from-seed-path chosen path =
    rationalExponentialValue-from-seed-path 0 chosen (constantCauchy 1) path
