{-# OPTIONS --safe --cubical --guardedness #-}
module ClosureCofiberTransportRegression where

open import Cubical.Foundations.Prelude
open import Cubical.Foundations.Function using (idfun)
open import Cubical.Foundations.Equiv
open import Cubical.Data.Unit
open import Cubical.Data.Bool using (Bool; false; true)
open import Cubical.HITs.Pushout.Base
open import Cubical.HITs.Susp.Base using (S¹≃SuspBool)
open import Cubical.HITs.S1.Base using (S¹)
open import ClosureCofiberTransportCoherence

-- This cofiber is a circle, not a hom-set or a terminal fixture.
f : Bool → Unit
f _ = tt

Circle : Type
Circle = cofib f

circleEquivalence : Circle ≃ S¹
circleEquivalence = compEquiv PushoutSusp≃Susp (invEquiv S¹≃SuspBool)

module T = Transport f (idfun Unit)
module Three = Triple f (idfun Unit) (idfun Unit)
module Four = Quadruple f (idfun Unit) (idfun Unit) (idfun Unit)

identityTransport : (x : Circle) → T.direct x ≡ x
identityTransport (inl tt) = refl
identityTransport (inr tt) = refl
identityTransport (push b i) = refl

circleLoop : Path Circle (inl tt) (inl tt)
circleLoop = push false ∙ sym (push true)

-- An equality OF paths; point-constructor tests alone would not express it.
preservesLoop : cong T.direct circleLoop ≡ circleLoop
preservesLoop i j = identityTransport (circleLoop j) i

-- Retain the path-dependent family over the whole circle, not only its base.
higherCompatibility : (x : Circle) → Four.left x ≡ Four.right x
higherCompatibility = Four.comparisonOfComparisons

-- The outstanding RejoinSquare is not assumed or instantiated by this test.
