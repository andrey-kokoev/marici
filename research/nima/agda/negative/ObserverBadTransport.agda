{-# OPTIONS --safe --cubical --guardedness #-}
module negative.ObserverBadTransport where
open import Cubical.Foundations.Prelude
open import Cubical.Data.Bool.Base using (Bool; true)
open import Cubical.Data.Bool.Properties using (notEquiv)
import ObserverCoherenceCube as C
open C.Geometry Bool Bool notEquiv
-- The specified equivalence transports true to false, not to itself.
bad : expand true ≡ true
bad = refl
