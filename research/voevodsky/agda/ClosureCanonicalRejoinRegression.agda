{-# OPTIONS --safe --cubical --guardedness #-}
module ClosureCanonicalRejoinRegression where

open import Cubical.Foundations.Prelude
open import Cubical.Foundations.Equiv
open import Cubical.Data.Unit
open import Cubical.Data.Empty using (⊥; rec)
open import Cubical.Data.Bool using (Bool; false; true; not)
open import Cubical.HITs.Pushout.Base
open import Cubical.HITs.Susp.Base using (S¹≃SuspBool)
open import Cubical.HITs.S1.Base using (S¹)
open import ClosureCanonicalRejoin

-- The explicit rejoin still preserves a genuinely higher output.
module CircleCase = Rejoin {A = ⊥} {B = Bool} {C = Unit} rec (λ _ → tt)

circleQuotient : CircleCase.Quotient ≃ S¹
circleQuotient = compEquiv CircleCase.rejoinEquiv
  (compEquiv PushoutSusp≃Susp (invEquiv S¹≃SuspBool))

-- A nonempty A exercises the nested attachment constructor; a nonidentity
-- postcomposition exchanges the two target points. This is not an all-Unit
-- or all-identity square.
f : Bool → Unit
f _ = tt

g : Unit → Bool
g _ = false

module Swap = Naturality f g not

nontrivialPoint :
  Swap.transportThenRejoin (inr (inr true)) ≡ inr false
nontrivialPoint = refl

-- The square is a family over all points AND paths of the double cofiber.
wholeSquare : (x : Swap.Before.Quotient) →
  Swap.transportThenRejoin x ≡ Swap.rejoinThenTransport x
wholeSquare = Swap.rejoinSquare

wholeInverseSquare : (x : cofib g) →
  Swap.upper (Swap.Before.cut x) ≡ Swap.After.cut (Swap.Lower.direct x)
wholeInverseSquare = Swap.cutSquare

-- Explicitly request the inverse law on the two-dimensional attachment.
attachmentInverse : (a : Bool) (u v : I) →
  Swap.Before.cut (Swap.Before.rejoin (push (push a u) v))
    ≡ push (push a u) v
attachmentInverse a u v = Swap.Before.cut-rejoin (push (push a u) v)
