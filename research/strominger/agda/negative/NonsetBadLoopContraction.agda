{-# OPTIONS --safe --cubical --guardedness #-}
module NonsetBadLoopContraction where
open import Cubical.Foundations.Prelude
open import NonsetWitnessEnvelopes
bad : isContr (x ≡ x)
bad = refl , (λ p → refl)
