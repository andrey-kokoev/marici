{-# OPTIONS --safe --cubical --guardedness #-}
module RootedSpokeAssemblyBadErasure where

open import Cubical.Foundations.Prelude
open import Cubical.Data.Bool.Base using (false)
import RootedSpokeSharedAssembly as Assembly

-- Deliberate rejection: the shared assembly retained the nontrivial AB
-- action. It cannot be replaced by an identity just because the outer
-- tetrahedral incidence shape is unchanged.
bad : transport Assembly.Twisted.first-edge false ≡ false
bad = refl
