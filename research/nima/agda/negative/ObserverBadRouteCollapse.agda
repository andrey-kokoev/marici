{-# OPTIONS --safe --cubical --guardedness #-}
module negative.ObserverBadRouteCollapse where
open import Cubical.Foundations.Prelude
open import Cubical.Foundations.Equiv using (idEquiv)
open import Cubical.Data.Bool.Base using (Bool)
import ObserverCoherenceCube as C
open C.Geometry Bool Bool (idEquiv Bool)
-- Equal interpreted maps do not erase the retained schedule constructors.
bad : leftFirst ≡ rightFirst
bad = refl
