{-# OPTIONS --safe --cubical --guardedness #-}
module RamseyEndpointFamilyBadCollapse where
open import Cubical.Foundations.Prelude
open import Cubical.Data.Bool.Base using (false; true)
open import RamseyEndpointPolicy using (base; complement)
open import RamseyCommonSelection using (witness)
open import RamseyEndpointFamily
bad : family base complement witness false ≡ family base complement witness true
bad = refl
