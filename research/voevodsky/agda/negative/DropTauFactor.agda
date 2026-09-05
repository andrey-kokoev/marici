{-# OPTIONS --safe --cubical --no-import-sorts --guardedness #-}
module DropTauFactor where

open import Cubical.Foundations.Prelude
open import AnalyticKernelEvaluation

private variable ℓ : Level

-- Deliberate failure: the tail atom evaluates to tau multiplied by H, not H.
module Invalid (ops : AnalyticOperations ℓ) (p : KernelParameters ops) where
  open AnalyticModel ops

  drop-tau : tail-term p ≡ H p
  drop-tau i = H p
