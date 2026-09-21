{-# OPTIONS --safe --cubical --guardedness #-}
module ClosureRejoinSquarePasting where

open import Cubical.Foundations.Prelude
open import Cubical.Foundations.Function using (idfun)
open import Cubical.Foundations.GroupoidLaws using (rUnit)
open import Cubical.Data.Unit
open import Cubical.HITs.Pushout.Base
open import ClosureCofiberTransportCoherence using (module Triple)
open import ClosureCanonicalRejoin using (module Naturality)

private
  -- Do not silently treat concatenation of reflexivity paths as strict.
  reflexivePasting : {X : Type} {x : X} →
    Path (x ≡ x) (refl ∙ refl) (refl ∙ refl ∙ sym refl)
  reflexivePasting = cong (λ p → refl ∙ p) (rUnit refl)

module Pasting {A B C D E : Type}
  (f : A → B) (g : B → C) (h : C → D) (k : D → E) where
  module H = Naturality f g h
  module K = Naturality f (λ b → h (g b)) k
  module HK = Naturality f g (λ c → k (h c))

  -- First align the upper boundaries: two independently defined maps between
  -- double cofibers versus the map for the composite target transport.
  upperComposition : (x : H.Before.Quotient) →
    K.upper (H.upper x) ≡ HK.upper x
  upperComposition (inl tt) = refl
  upperComposition (inr (inl tt)) = refl
  upperComposition (inr (inr c)) = refl
  upperComposition (inr (push a i)) = refl
  upperComposition (push (inl tt) i) = refl
  upperComposition (push (inr b) i) = refl
  upperComposition (push (push a j) i) = refl

  -- Align the lower boundaries using the previously constructed cofiber
  -- transport-composition homotopy, rather than assuming functoriality.
  lowerComposition : (x : cofib g) →
    K.Lower.direct (H.Lower.direct x) ≡ HK.Lower.direct x
  lowerComposition = Triple.directComposition g h k

  -- Pasting of the two actual rejoin squares, whiskering the first by k.
  pastedRejoin : (x : H.Before.Quotient) →
    K.After.rejoin (K.upper (H.upper x)) ≡
    K.Lower.direct (H.Lower.direct (H.Before.rejoin x))
  pastedRejoin x =
    K.rejoinSquare (H.upper x)
    ∙ cong K.Lower.direct (H.rejoinSquare x)

  -- Independently constructed single square. The boundary comparisons are
  -- part of this path, with the lower comparison reversed at its far end.
  compositeRejoin : (x : H.Before.Quotient) →
    K.After.rejoin (K.upper (H.upper x)) ≡
    K.Lower.direct (H.Lower.direct (H.Before.rejoin x))
  compositeRejoin x =
    cong K.After.rejoin (upperComposition x)
    ∙ HK.rejoinSquare x
    ∙ sym (lowerComposition (H.Before.rejoin x))

  -- A path BETWEEN the two path witnesses, checked on the nested attachment
  -- square as well as on the lower-dimensional constructors.
  rejoinPasting : (x : H.Before.Quotient) →
    pastedRejoin x ≡ compositeRejoin x
  rejoinPasting (inl tt) = reflexivePasting
  rejoinPasting (inr (inl tt)) = reflexivePasting
  rejoinPasting (inr (inr c)) = reflexivePasting
  rejoinPasting (inr (push a i)) = reflexivePasting
  rejoinPasting (push (inl tt) i) = reflexivePasting
  rejoinPasting (push (inr b) i) = reflexivePasting
  rejoinPasting (push (push a j) i) = reflexivePasting

  pastedCut : (x : cofib g) →
    K.upper (H.upper (H.Before.cut x)) ≡
    K.After.cut (K.Lower.direct (H.Lower.direct x))
  pastedCut x =
    cong K.upper (H.cutSquare x)
    ∙ K.cutSquare (H.Lower.direct x)

  compositeCut : (x : cofib g) →
    K.upper (H.upper (H.Before.cut x)) ≡
    K.After.cut (K.Lower.direct (H.Lower.direct x))
  compositeCut x =
    upperComposition (H.Before.cut x)
    ∙ HK.cutSquare x
    ∙ cong K.After.cut (sym (lowerComposition x))

  cutPasting : (x : cofib g) → pastedCut x ≡ compositeCut x
  cutPasting (inl tt) = reflexivePasting
  cutPasting (inr c) = reflexivePasting
  cutPasting (push b i) = reflexivePasting

-- These theorems concern postcomposition of the canonical naturality squares.
-- They do not assert a pentagon for arbitrary filtration rebracketings, nor
-- identify the canonical rejoin with the earlier 3x3-transported choice.
