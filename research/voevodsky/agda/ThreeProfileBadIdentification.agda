{-# OPTIONS --safe --cubical --guardedness #-}
module ThreeProfileBadIdentification where
open import Cubical.Foundations.Prelude
open import Cubical.Data.Bool.Base using (true; false)
bad : true ≡ false
bad = refl