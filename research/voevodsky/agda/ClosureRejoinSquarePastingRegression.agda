{-# OPTIONS --safe --cubical --guardedness #-}
module ClosureRejoinSquarePastingRegression where

open import Cubical.Foundations.Prelude
open import Cubical.Foundations.Function using (idfun)
open import Cubical.Foundations.Equiv
open import Cubical.Data.Unit
open import Cubical.Data.Empty using (⊥; rec)
open import Cubical.Data.Bool using (Bool; false; true; not)
open import Cubical.HITs.Pushout.Base
open import Cubical.HITs.Susp.Base using (S¹≃SuspBool)
open import Cubical.HITs.S1.Base using (S¹)
open import ClosureRejoinSquarePasting

-- Nonempty attachment domain and TWO nonidentity target transports.
f : Bool → Unit
f _ = tt

g : Unit → Bool
g _ = false

module SwapTwice = Pasting f g not not

pointAfterTwoTransports :
  SwapTwice.K.After.rejoin
    (SwapTwice.K.upper (SwapTwice.H.upper (inr (inr true)))) ≡ inr true
pointAfterTwoTransports = refl

nestedAttachmentPasting : (a : Bool) (u v : I) →
  SwapTwice.pastedRejoin (push (push a u) v) ≡
  SwapTwice.compositeRejoin (push (push a u) v)
nestedAttachmentPasting a u v =
  SwapTwice.rejoinPasting (push (push a u) v)

inversePasting : (x : cofib g) →
  SwapTwice.pastedCut x ≡ SwapTwice.compositeCut x
inversePasting = SwapTwice.cutPasting

-- A separate fixture has a circle as rejoined output. The family of higher
-- comparisons can be traversed along its entire lifted loop.
emptyMap : ⊥ → Bool
emptyMap = rec

terminalMap : Bool → Unit
terminalMap _ = tt

module CircleCase = Pasting emptyMap terminalMap (idfun Unit) (idfun Unit)

circleQuotient : CircleCase.H.Before.Quotient ≃ S¹
circleQuotient = compEquiv CircleCase.H.Before.rejoinEquiv
  (compEquiv PushoutSusp≃Susp (invEquiv S¹≃SuspBool))

circleLoop : Path (cofib terminalMap) (inl tt) (inl tt)
circleLoop = push false ∙ sym (push true)

liftedLoop : Path CircleCase.H.Before.Quotient (inl tt) (inl tt)
liftedLoop = cong CircleCase.H.Before.cut circleLoop

pastingAlongLoop : PathP
  (λ i → CircleCase.pastedRejoin (liftedLoop i) ≡
         CircleCase.compositeRejoin (liftedLoop i))
  (CircleCase.rejoinPasting (inl tt))
  (CircleCase.rejoinPasting (inl tt))
pastingAlongLoop i = CircleCase.rejoinPasting (liftedLoop i)
