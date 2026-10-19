{-# OPTIONS --safe --cubical --guardedness #-}
module NativeFeedbackKeyedEndpointBinding where

open import Cubical.Foundations.Prelude
import NativeFeedbackEndpointBindingGate as Gate

module F = Gate.F
module Before = Gate.Before
module After = Gate.After

-- The context key is an explicit interface input, not selected by run.
module Keyed {ℓ : Level} (K : Type ℓ) (key : Before.Compared → K) where
  TargetPort : Type _
  TargetPort = Σ After.H.Presentation (λ _ → K)

  source : Before.Compared → Gate.RefinedPort
  source = Gate.refined-from

  target : Before.Compared → TargetPort
  target c = Gate.to c , key (F.decode (F.run c))

  key-recovered : (c : Before.Compared) → snd (target c) ≡ key c
  key-recovered c = cong key (F.decode-run c)

  -- Endpoint uniqueness comes entirely from retained source payload, so
  -- does not force singleton target fibres.
  endpoints-unique : (c d : Before.Compared)
    → source c ≡ source d → target c ≡ target d → c ≡ d
  endpoints-unique c d ps pt = sym (F.decode-run c)
    ∙ cong snd ps ∙ F.decode-run d

  target-preserves-context : (c d : Before.Compared)
    → key c ≡ key d → target c ≡ target d
  target-preserves-context c d p i = Gate.to-equal c d i ,
    (key-recovered c ∙ p ∙ sym (key-recovered d)) i

  target-reflects-context : (c d : Before.Compared)
    → target c ≡ target d → key c ≡ key d
  target-reflects-context c d p = sym (key-recovered c)
    ∙ cong snd p ∙ key-recovered d

-- The exact admissible common-target relation is therefore supplied by key.
-- Choosing a constant key, an original record-target key, or the full payload
-- changes that relation while satisfying the SAME uniqueness and retention
-- theorems. This theorem cannot select an intended T9 by itself.
