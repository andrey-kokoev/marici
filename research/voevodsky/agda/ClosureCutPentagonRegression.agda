{-# OPTIONS --safe --cubical --guardedness #-}
module ClosureCutPentagonRegression where

open import Cubical.Foundations.Prelude
open import Cubical.Foundations.Equiv
open import Cubical.Data.Unit
open import Cubical.Data.Bool using (Bool; false; true; not)
open import Cubical.HITs.Pushout.Base
open import Cubical.HITs.Susp.Base using (S¹≃SuspBool)
open import Cubical.HITs.S1.Base using (S¹)
open import ClosureCutPentagon

-- All four attachment domains are nonempty, all three initial arrows are
-- nonidentity, and the final cofiber is the circle rather than a set quotient.
k : Bool → Unit
k _ = tt

module Example = Pentagon not not not k

fourfoldCircle : Example.FourfoldQuotient ≃ S¹
fourfoldCircle = compEquiv Example.E0
  (compEquiv PushoutSusp≃Susp (invEquiv S¹≃SuspBool))

fourfoldAttachment : (a : Bool) (u v w t : I) →
  Example.longRoute (push (push (push (push a u) v) w) t) ≡
  Example.shortRoute (push (push (push (push a u) v) w) t)
fourfoldAttachment a u v w t =
  Example.pentagon (push (push (push (push a u) v) w) t)

-- Both endpoint assemblies retain the same specific target attachment.
leftNormalForm : (u v w t : I) →
  Example.v0 (push (push (push (push false u) v) w) t) ≡
  push true (((u ∧ v) ∧ w) ∧ t)
leftNormalForm u v w t = refl

rightNormalForm : (u v w t : I) →
  Example.v3 (push (push (push (push false u) v) w) t) ≡
  push true (u ∧ (v ∧ (w ∧ t)))
rightNormalForm u v w t = refl

circleLoop : Path (cofib k) (inl tt) (inl tt)
circleLoop = push false ∙ sym (push true)

liftedLoop : Path Example.FourfoldQuotient
  (invEq Example.E0 (inl tt)) (invEq Example.E0 (inl tt))
liftedLoop = cong (invEq Example.E0) circleLoop

pentagonAlongLoop : PathP
  (λ i → Example.longRoute (liftedLoop i) ≡ Example.shortRoute (liftedLoop i))
  (Example.pentagon (invEq Example.E0 (inl tt)))
  (Example.pentagon (invEq Example.E0 (inl tt)))
pentagonAlongLoop i = Example.pentagon (liftedLoop i)
