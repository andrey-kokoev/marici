{-# OPTIONS --safe --cubical --guardedness #-}
module WitnessedRouteBadErasure where

open import Cubical.Foundations.Prelude
open import Cubical.Data.Bool.Base using (false)
import DependentTransportMachine as M
open import WitnessedRouteContinuation

-- DELIBERATE NEGATIVE TEST. Endpoint/return equality cannot justify this.
bad-erasure : probe (triangle M.stay) false ≡ probe (triangle M.turn) false
bad-erasure = refl
