{-# OPTIONS --safe --cubical --guardedness #-}
module ObserverTransportRegression where

open import Cubical.Foundations.Prelude
open import Cubical.Data.Bool.Base using (true; false)
import ObserverNonuniqueHistory as H
import ObserverInternalInterface as O

-- Definitional computation tests, not proofs obtained by rewriting
-- transport away using transportRefl.
transported-red : O.readout O.rule (transport (λ _ → H.History) H.red-history) ≡ true
transported-red = refl

transported-blue : O.readout O.rule (transport (λ _ → H.History) H.blue-history) ≡ false
transported-blue = refl

-- Preserve the original witness-bearing Run type and general recovery.
transported-recovery : (h : H.History)
  → H.replay (O.readout O.rule (transport (λ _ → H.History) h))
    ≡ transport (λ _ → H.History) h
transported-recovery h = H.replay-rule (transport (λ _ → H.History) h)
