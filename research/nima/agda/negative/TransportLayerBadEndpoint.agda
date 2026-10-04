{-# OPTIONS --safe --cubical --guardedness #-}
module TransportLayerBadEndpoint where
open import Cubical.Foundations.Prelude
open import Cubical.Data.Bool.Base using (true)
open import TypedGeneratorTransport
import DependentTransportMachine as M
-- One turn at the same base index changes the payload.
bad : MachineBridge.run-compiled (M.carry M.turn (M.bit true)) ≡ true
bad = refl
