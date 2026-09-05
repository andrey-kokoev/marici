{-# OPTIONS --safe --cubical --no-import-sorts --guardedness #-}
module CauchyCompletionAbGroup where

open import Cubical.Foundations.Prelude
open import Cubical.Algebra.AbGroup
open import Cubical.Data.Rationals as Q
open import Cubical.HITs.SetQuotients as SQ
open import CauchyMetricEquivalence
open import CauchyAddition
open import CauchyAdditionCongruence
open import CauchyNegation
open import CauchyAdditiveLaws

zeroCompletion : MetricCompletionCandidate
zeroCompletion = embedMetricℚ 0

completion-+Assoc : (x y z : MetricCompletionCandidate) →
  x +completion (y +completion z) ≡
  (x +completion y) +completion z
completion-+Assoc = SQ.elimProp3
  (λ _ _ _ → metric-candidate-isSet _ _)
  (λ x y z → SQ.eq/ _ _
    (≈metric-sym (addRegular (addRegular x y) z)
      (addRegular x (addRegular y z)) (add-associative x y z)))

completion-+IdR : (x : MetricCompletionCandidate) →
  x +completion zeroCompletion ≡ x
completion-+IdR = SQ.elimProp
  (λ _ → metric-candidate-isSet _ _)
  (λ x → SQ.eq/ _ _ (add-zero-right x))

completion-+InvR : (x : MetricCompletionCandidate) →
  x +completion (-completion x) ≡ zeroCompletion
completion-+InvR = SQ.elimProp
  (λ _ → metric-candidate-isSet _ _)
  (λ x → SQ.eq/ _ _ (add-inverse-right x))

completion-+Comm : (x y : MetricCompletionCandidate) →
  x +completion y ≡ y +completion x
completion-+Comm = SQ.elimProp2
  (λ _ _ → metric-candidate-isSet _ _)
  (λ x y → SQ.eq/ _ _ (add-commutative x y))

CompletionAbGroup : AbGroup ℓ-zero
CompletionAbGroup =
  makeAbGroup zeroCompletion _+completion_ -completion_
    metric-candidate-isSet completion-+Assoc completion-+IdR
    completion-+InvR completion-+Comm
