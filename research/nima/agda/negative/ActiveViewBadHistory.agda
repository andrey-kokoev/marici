{-# OPTIONS --safe --cubical --guardedness #-}
module ActiveViewBadHistory where
open import Cubical.Foundations.Prelude
open import Cubical.Data.Bool.Base using (Bool; true; false)
open import Cubical.Data.Unit.Base using (tt)
open import Cubical.Data.List.Base using ([]; _∷_)
open import ActiveViewMachine
is-empty : Request → Bool
is-empty ([] , b) = true
is-empty (a ∷ h , b) = false
idle twice : View compact
idle = ([] , true) , tt
twice = (turn ∷ turn ∷ [] , true) , tt
bad : is-empty (fst idle) ≡ is-empty (fst twice)
bad = refl
