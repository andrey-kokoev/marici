{-# OPTIONS --safe --cubical --guardedness #-}
module ClosureIntermediateCutRegression where

open import Cubical.Foundations.Prelude
open import Cubical.Foundations.Equiv
open import Cubical.Data.Unit
open import Cubical.Data.Bool using (Bool; false; true; not)
open import Cubical.HITs.Pushout.Base
open import Cubical.HITs.Susp.Base using (S¹≃SuspBool)
open import Cubical.HITs.S1.Base using (S¹)
open import ClosureIntermediateCutComparison

-- Every attachment domain is nonempty, both early maps are nonidentity, and
-- the final cofiber is a circle rather than a terminal type.
h : Bool → Unit
h _ = tt

module Example = CutComparison not not h

tripleQuotientCircle : Example.TripleQuotient ≃ S¹
tripleQuotientCircle = compEquiv Example.removeAFirstEquiv
  (compEquiv PushoutSusp≃Susp (invEquiv S¹≃SuspBool))

-- The two orders agree on the full three-dimensional attachment.
tripleAttachmentComparison : (a : Bool) (u v w : I) →
  Example.removeAFirst (push (push (push a u) v) w) ≡
  Example.removeMiddleFirst (push (push (push a u) v) w)
tripleAttachmentComparison a u v w =
  Example.cutComparison (push (push (push a u) v) w)

-- A concrete normal form verifies which target attachment is retained.
tripleAttachmentNormalForm : (u v w : I) →
  Example.removeAFirst (push (push (push false u) v) w) ≡
  push false (u ∧ v ∧ w)
tripleAttachmentNormalForm u v w = refl

circleLoop : Path (cofib h) (inl tt) (inl tt)
circleLoop = push false ∙ sym (push true)

-- The inverse-comparison family also travels along the whole circle loop.
inverseComparisonAlongLoop : PathP
  (λ i → invEq Example.removeAFirstEquiv (circleLoop i) ≡
         invEq Example.removeMiddleFirstEquiv (circleLoop i))
  (Example.inverseComparison (inl tt))
  (Example.inverseComparison (inl tt))
inverseComparisonAlongLoop i = Example.inverseComparison (circleLoop i)
