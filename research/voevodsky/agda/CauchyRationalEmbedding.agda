{-# OPTIONS --safe --cubical --no-import-sorts --guardedness #-}
module CauchyRationalEmbedding where

open import Cubical.Foundations.Prelude
open import Cubical.Data.Rationals as Q
open import Cubical.Algebra.AbGroup
open import Cubical.Algebra.Group.Morphisms
open import Cubical.Algebra.Group.MorphismProperties
open import Cubical.HITs.SetQuotients as SQ
open import RationalAnalyticSubstrate
open import RegularCauchyStructure
open import CauchyMetricEquivalence
open import CauchyAddition
open import CauchyAdditionCongruence
open import CauchyNegation
open import CauchyAdditiveLaws using (pointwise-equivalent)
open import CauchyCompletionAbGroup
open import CauchyHalving

embedℚ-preserves-sum : (q r : Q.ℚ) →
  embedMetricℚ (q Q.+ r) ≡ embedMetricℚ q +completion embedMetricℚ r
embedℚ-preserves-sum q r = SQ.eq/ _ _
  (pointwise-equivalent
    (constantCauchy (q Q.+ r))
    (addRegular (constantCauchy q) (constantCauchy r))
    (λ n → refl))

embedℚ-hom : AbGroupHom RationalAbGroup CompletionAbGroup
embedℚ-hom .fst = embedMetricℚ
embedℚ-hom .snd = makeIsGroupHom embedℚ-preserves-sum

embedℚ-preserves-negation : (q : Q.ℚ) →
  -completion (embedMetricℚ q) ≡ embedMetricℚ (Q.- q)
embedℚ-preserves-negation q = SQ.eq/ _ _
  (pointwise-equivalent
    (negateRegular (constantCauchy q))
    (constantCauchy (Q.- q))
    (λ n → refl))

embedℚ-preserves-half : (q : Q.ℚ) →
  embedMetricℚ (halfℚ q) ≡ halfCompletion (embedMetricℚ q)
embedℚ-preserves-half q = SQ.eq/ _ _
  (pointwise-equivalent
    (constantCauchy (halfℚ q))
    (halfRegular (constantCauchy q))
    (λ n → refl))
