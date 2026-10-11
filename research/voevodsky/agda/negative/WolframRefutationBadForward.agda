{-# OPTIONS --safe --cubical --guardedness #-}
module WolframRefutationBadForward where
open import Cubical.Foundations.Prelude
import GeneratedWolframRefutations as G
module Bad {ℓ : Level} (A B C : Type ℓ) where
  open G.Construct A B C
  -- Mutation: omit the application that must produce the empty result.
  broken-forward : W → D
  broken-forward w nc = w
