{-# OPTIONS --safe --cubical --no-import-sorts --guardedness #-}
module CompletedKernelEvaluation where

open import Cubical.Foundations.Prelude
open import Cubical.Algebra.AbGroup
open import AnalyticKernelEvaluation
open import SymbolicKernelCoefficients
open import CauchyMetricEquivalence
open import CauchyCompletionAbGroup
open import CauchyHalving

-- The completion carrier, additive group, and halving operation are now
-- constructed. Only the genuinely multiplicative/transcendental operations
-- remain parameters.
record RemainingAnalyticOperations : Type₁ where
  field
    multiply : MetricCompletionCandidate →
               MetricCompletionCandidate → MetricCompletionCandidate
    exponential : MetricCompletionCandidate → MetricCompletionCandidate
    cosine : MetricCompletionCandidate → MetricCompletionCandidate
open RemainingAnalyticOperations public

completed-operations : RemainingAnalyticOperations → AnalyticOperations ℓ-zero
completed-operations remaining = record
  { ValueGroup = CompletionAbGroup
  ; multiply = RemainingAnalyticOperations.multiply remaining
  ; exponential = RemainingAnalyticOperations.exponential remaining
  ; cosine = RemainingAnalyticOperations.cosine remaining
  ; half = halfCompletion
  }

module CompletedModel (remaining : RemainingAnalyticOperations) where
  ops : AnalyticOperations ℓ-zero
  ops = completed-operations remaining

  module Model = AnalyticModel ops
  open Model public

  Parameters : Type
  Parameters = KernelParameters ops

  module Syntax = SymbolicKernel Parameters

  completed-kernel-evaluation :
    AbGroupHom Syntax.KernelCoefficientGroup CompletionAbGroup
  completed-kernel-evaluation = analytic-evaluation

  completed-tail-evaluates-to-tau-H :
    (p : Parameters) →
    Model.E.evaluate (Syntax.tail p) ≡
    RemainingAnalyticOperations.multiply remaining (tau p) (H p)
  completed-tail-evaluates-to-tau-H = tail-evaluates-to-tau-H
