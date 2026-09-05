{-# OPTIONS --safe --cubical --no-import-sorts --guardedness --lossy-unification #-}
module CosineSeedConstruction where

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
open import CosineTailSchedule
open import CosineSeedCoherence
open import CauchyMetricEquivalence

preferred-cosine-dyadic-dominance : (q : Q.ℚ) → DyadicDominates q
preferred-cosine-dyadic-dominance =
  truncated-ceiling-principle-gives-dyadic-dominance
    (raw-ceiling-gives-truncated-principle
      preferred-raw-rational-natural-ceiling)

constant-presentation-value-bound : (q : Q.ℚ) →
  (presentation : BoundedPresentation (constantCauchy q)) →
  MagnitudeBound q (dyadicRadius (radius-exponent (fst presentation)))
constant-presentation-value-bound q (bounded , sourcePath) =
  transport-magnitude q (approximation (regular bounded) zero)
    (dyadicRadius (radius-exponent bounded))
    (sym (cong (λ z → approximation z zero) sourcePath))
    (bounded-value bounded zero)

TruncatedCosineTailSeed : Q.ℚ → Type
TruncatedCosineTailSeed q = ∥ CosineTailSeed q ∥₁

cosine-seed-from-presentations : (q : Q.ℚ) →
  (inputPresentation : BoundedPresentation (constantCauchy q)) →
  let inputExponent = radius-exponent (fst inputPresentation)
      seedTerm = cosineTerm q (dyadicNat (suc inputExponent))
  in
  BoundedPresentation (constantCauchy seedTerm) → CosineTailSeed q
cosine-seed-from-presentations q inputPresentation seedPresentation = record
  { inputExponent = radius-exponent (fst inputPresentation)
  ; inputBound = constant-presentation-value-bound q inputPresentation
  ; seedExponent = radius-exponent (fst seedPresentation)
  ; seedBound = constant-presentation-value-bound _ seedPresentation
  }

preferred-truncated-cosine-tail-seed :
  (q : Q.ℚ) → TruncatedCosineTailSeed q
preferred-truncated-cosine-tail-seed q =
  PT.rec isPropPropTrunc
    (λ inputPresentation →
      let inputExponent = radius-exponent (fst inputPresentation)
          seedTerm = cosineTerm q (dyadicNat (suc inputExponent))
          seedDominance = preferred-cosine-dyadic-dominance
            (canonicalRadius (constantCauchy seedTerm))
      in
      PT.rec isPropPropTrunc
        (λ seedPresentation →
          ∣ cosine-seed-from-presentations
              q inputPresentation seedPresentation ∣₁)
        (promote-regular-presentation-truncated
          (constantCauchy seedTerm) seedDominance))
    (promote-regular-presentation-truncated
      (constantCauchy q)
      (preferred-cosine-dyadic-dominance
        (canonicalRadius (constantCauchy q))))

cosineSeedClass : {q : Q.ℚ} →
  CosineTailSeed q → MetricCompletionCandidate
cosineSeedClass seed = [ absorbedCosineRegular seed ]

cosineSeedClass-2constant : {q : Q.ℚ} →
  (first second : CosineTailSeed q) →
  cosineSeedClass first ≡ cosineSeedClass second
cosineSeedClass-2constant first second =
  SQ.eq/ _ _ (cosine-seeds-metric-equivalent first second)

abstract
  rationalCosineValue : Q.ℚ → MetricCompletionCandidate
  rationalCosineValue q =
    rec→Set metric-candidate-isSet
      cosineSeedClass
      cosineSeedClass-2constant
      (preferred-truncated-cosine-tail-seed q)

  cosine-class-from-truncated : {q : Q.ℚ} →
    (seeds : TruncatedCosineTailSeed q) →
    (chosen : CosineTailSeed q) →
    rec→Set metric-candidate-isSet
      cosineSeedClass cosineSeedClass-2constant seeds ≡
    cosineSeedClass chosen
  cosine-class-from-truncated seeds chosen =
    cong
      (rec→Set metric-candidate-isSet
        cosineSeedClass cosineSeedClass-2constant)
      (squash₁ seeds ∣ chosen ∣₁)

  rationalCosineValue-from-seed : (q : Q.ℚ) →
    (chosen : CosineTailSeed q) →
    rationalCosineValue q ≡ cosineSeedClass chosen
  rationalCosineValue-from-seed q chosen =
    cosine-class-from-truncated
      (preferred-truncated-cosine-tail-seed q) chosen

  rationalCosineValue-from-seed-path : (q : Q.ℚ) →
    (chosen : CosineTailSeed q) → (target : RegularCauchy) →
    absorbedCosineRegular chosen ≡ target →
    rationalCosineValue q ≡ SQ.[ target ]
  rationalCosineValue-from-seed-path q chosen target path =
    rationalCosineValue-from-seed q chosen ∙ cong SQ.[_] path

  rationalCosineValue-zero-from-seed-path :
    (chosen : CosineTailSeed 0) →
    absorbedCosineRegular chosen ≡ constantCauchy 1 →
    rationalCosineValue 0 ≡ SQ.[ constantCauchy 1 ]
  rationalCosineValue-zero-from-seed-path chosen path =
    rationalCosineValue-from-seed-path 0 chosen (constantCauchy 1) path
