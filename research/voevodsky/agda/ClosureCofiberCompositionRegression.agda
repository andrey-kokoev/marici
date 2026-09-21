{-# OPTIONS --safe --cubical --guardedness #-}
module ClosureCofiberCompositionRegression where

open import Cubical.Foundations.Prelude
open import Cubical.Foundations.Function using (idfun)
open import Cubical.Foundations.Equiv
open import Cubical.Data.Unit
open import Cubical.Data.Empty using (⊥; rec)
open import Cubical.Data.Bool using (Bool)
open import Cubical.HITs.Pushout.Base
open import Cubical.HITs.Susp.Base using (S¹≃SuspBool)
open import Cubical.HITs.S1.Base using (S¹)
open import ClosureCofiberComposition

-- A genuine nontruncated output: A is empty, B has two points, C has one.
-- C/B is the suspension of Bool, hence the circle. Cut/rejoin must NOT
-- collapse the complete attachment data to a terminal set.
module CircleCase = Composition ⊥ Bool Unit rec (λ _ → tt)

circleQuotient : CircleCase.iteratedQuotient ≃ S¹
circleQuotient = compEquiv CircleCase.cofiberComposition
  (compEquiv PushoutSusp≃Susp (invEquiv S¹≃SuspBool))

-- If the second map is identity, its cofiber really is contractible.
-- This also tests the other outcome without assuming any special f.
module IdentityCase (A B : Type) (f : A → B) where
  module Q = Composition A B B f (idfun B)

  terminalQuotient : Q.iteratedQuotient ≃ Unit
  terminalQuotient = compEquiv Q.cofiberComposition
    (compEquiv (symPushout (λ _ → tt) (idfun B))
      (Collapse.collapseEquiv B))

-- Both general round trips, including all higher-inductive path constructors,
-- are checked in ClosureCofiberComposition, not sampled on point constructors.
