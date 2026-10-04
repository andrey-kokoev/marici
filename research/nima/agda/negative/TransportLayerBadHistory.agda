{-# OPTIONS --safe --cubical --guardedness #-}
module TransportLayerBadHistory where
open import Cubical.Foundations.Prelude
open import Cubical.Data.Bool.Base using (true)
open import TypedGeneratorTransport
import DependentTransportMachine as M
-- Restoring the Boolean does not erase the two retained turns.
bad : MachineBridge.is-empty (MachineBridge.history (M.follow M.turn M.turn)) ≡ true
bad = refl
