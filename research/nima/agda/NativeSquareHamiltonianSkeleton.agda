{-# OPTIONS --safe --cubical --guardedness #-}
module NativeSquareHamiltonianSkeleton where

open import Cubical.Foundations.Prelude
open import Cubical.Data.Bool.Base using (Bool; false; true)
open import Cubical.Data.Bool.Properties using (notEquiv)
open import Cubical.Data.Sigma.Base using (_×_)
import ObserverCoherenceCube as Source

-- Identify the finite source operations used by the matrix checker. No
-- complex coefficients, exponential or physical Hamiltonian are asserted here.
module G = Source.Geometry Bool Bool notEquiv
State = Bool × Bool

left right : State → State
left = G.expandLeft
right = G.expandRight

left00 : left (false , false) ≡ (true , false)
left00 = refl
left01 : left (false , true) ≡ (true , true)
left01 = refl
left10 : left (true , false) ≡ (false , false)
left10 = refl
left11 : left (true , true) ≡ (false , true)
left11 = refl
right00 : right (false , false) ≡ (false , true)
right00 = refl
right01 : right (false , true) ≡ (false , false)
right01 = refl
right10 : right (true , false) ≡ (true , true)
right10 = refl
right11 : right (true , true) ≡ (true , false)
right11 = refl

left-twice : (s : State) → left (left s) ≡ s
left-twice (false , false) = refl
left-twice (false , true) = refl
left-twice (true , false) = refl
left-twice (true , true) = refl
right-twice : (s : State) → right (right s) ≡ s
right-twice (false , false) = refl
right-twice (false , true) = refl
right-twice (true , false) = refl
right-twice (true , true) = refl

same-forward-map : (λ s → right (left s)) ≡ (λ s → left (right s))
same-forward-map = G.route-homotopy
