{-# OPTIONS --safe --cubical --no-import-sorts --guardedness #-}
module CauchyCompletionCommRing where

open import Cubical.Foundations.Prelude
open import Cubical.Algebra.CommRing
open import Cubical.Data.Rationals
open import CauchyMetricEquivalence
open import CauchyAdditionCongruence
open import CauchyNegation
open import CauchyCompletionAbGroup
open import CauchyCompletionMultiplication
open import CauchyCompletionMultiplicativeLaws

oneCompletion : MetricCompletionCandidate
oneCompletion = embedMetricℚ 1

CompletionCommRing : CommRing ℓ-zero
CompletionCommRing =
  makeCommRing
    zeroCompletion oneCompletion
    _+completion_ preferredCompletionMultiplication -completion_
    metric-candidate-isSet
    completion-+Assoc
    completion-+IdR
    completion-+InvR
    completion-+Comm
    (λ x y z → sym
      (preferred-completion-multiplication-associative x y z))
    preferred-completion-multiplication-right-unit
    preferred-completion-multiplication-distributive-right
    preferred-completion-multiplication-commutative
