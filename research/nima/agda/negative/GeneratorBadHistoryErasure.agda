{-# OPTIONS --safe --cubical --guardedness #-}
module GeneratorBadHistoryErasure where
open import Cubical.Foundations.Prelude
open import Cubical.Data.Bool.Base using (false; true)
open import TypedGeneratorLayers
-- Returning to the same state does not make the retained history empty.
bad : is-empty (IH.generated 2 false) ≡ true
bad = refl
