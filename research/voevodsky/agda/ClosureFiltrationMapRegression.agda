{-# OPTIONS --safe --cubical --guardedness #-}
module ClosureFiltrationMapRegression where

open import Cubical.Foundations.Prelude
open import Cubical.Foundations.Function using (idfun)
open import Cubical.Foundations.Equiv
open import Cubical.Data.Unit
open import Cubical.Data.Empty using (⊥)
open import Cubical.Data.Bool using (Bool; false; true)
open import Cubical.Data.Bool.Properties using (false≢true)
open import Cubical.HITs.Pushout.Base
open import Cubical.HITs.S1.Base using (S¹; base; loop)
open import ClosureCanonicalRejoin using (module Rejoin)
open import ClosureFiltrationMapNaturality

module Noninvertible where
  -- Every object changes from Bool to Unit, and every vertical map merges
  -- the two points. The theorem must not require vertical equivalences.
  u : Bool → Unit
  u _ = tt

  module L = Ladder (idfun Bool) (idfun Bool) (idfun Unit) (idfun Unit)
    u u u (λ _ → refl) (λ _ → refl)

  notAnEquivalence : isEquiv u → ⊥
  notAnEquivalence e = false≢true
    (sym (retEq (u , e) false) ∙ retEq (u , e) true)

  entireSquare : (x : Rejoin.Quotient (idfun Bool) (idfun Bool)) →
    Rejoin.rejoin (idfun Unit) (idfun Unit) (L.mapQuotient x) ≡
    L.mapCofiber (Rejoin.rejoin (idfun Bool) (idfun Bool) x)
  entireSquare = L.rejoinNaturality

module LoopSquares where
  -- Both given commuting-square witnesses are circle loops, not refl.
  -- This exercises the dependent transport stages of the constructed map.
  f : Bool → S¹
  f _ = base

  f′ : Unit → S¹
  f′ _ = base

  g : S¹ → S¹
  g _ = base

  u : Bool → Unit
  u _ = tt

  module L = Ladder f g f′ g u (idfun S¹) (idfun S¹)
    (λ _ → loop) (λ _ → loop)

  nestedAttachmentSquare : (a : Bool) (i j : I) →
    Rejoin.rejoin f′ g (L.mapQuotient (push (push a i) j)) ≡
    L.mapCofiber (Rejoin.rejoin f g (push (push a i) j))
  nestedAttachmentSquare a i j = L.rejoinNaturality (push (push a i) j)

  -- The output has a circle retract. It is not replaced with a terminal or
  -- set-valued fixture merely to make all square homotopies disappear.
  project : cofib g → S¹
  project (inl tt) = base
  project (inr x) = x
  project (push b i) = base

  retractCircle : (x : S¹) → project (inr x) ≡ x
  retractCircle x = refl

  loopInCofiber : Path (cofib g) (inr base) (inr base)
  loopInCofiber i = inr (loop i)

  cutSquareAlongLoop : PathP
    (λ i → L.mapQuotient (Rejoin.cut f g (loopInCofiber i)) ≡
           Rejoin.cut f′ g (L.mapCofiber (loopInCofiber i)))
    (L.cutNaturality (inr base)) (L.cutNaturality (inr base))
  cutSquareAlongLoop i = L.cutNaturality (loopInCofiber i)
