{-# OPTIONS --safe --cubical --guardedness #-}
module ActiveViewBadTrace where
open import Cubical.Foundations.Prelude
open import Cubical.Data.Bool.Base using (true)
open import Cubical.Data.List.Base using ([]; _∷_)
open import ActiveViewMachine
bad : trace (turn ∷ []) true ≡ (true ∷ true ∷ [])
bad = refl
