{-# OPTIONS --safe --cubical --guardedness #-}
module ClosurePushoutRefinement where

open import Cubical.Foundations.Prelude
open import Cubical.Foundations.Equiv
import Cubical.HITs.Pushout.Base as PO
open import Cubical.HITs.Pushout.Properties using (pushoutEquiv)

-- Refine the left piece, shared boundary, and right piece independently.
-- Both attachment maps are reconstructed through their realization frames.
module Span {L M R L′ M′ R′ : Type}
  (f : M → L) (g : M → R)
  (middle : M′ ≃ M) (left : L′ ≃ L) (right : R′ ≃ R) where

  leftMap : M′ → L′
  leftMap x = invEq left (f (equivFun middle x))

  rightMap : M′ → R′
  rightMap x = invEq right (g (equivFun middle x))

  Space : Type
  Space = PO.Pushout leftMap rightMap

  leftSquare : (x : M′) → equivFun left (leftMap x) ≡ f (equivFun middle x)
  leftSquare x = secEq left (f (equivFun middle x))

  rightSquare : (x : M′) → equivFun right (rightMap x) ≡ g (equivFun middle x)
  rightSquare x = secEq right (g (equivFun middle x))

  private
    rawEquiv : Space ≃ PO.Pushout f g
    rawEquiv = pushoutEquiv leftMap rightMap f g middle left right
      (funExt leftSquare) (funExt rightSquare)

  -- Keep the certified inverse proof opaque while preserving all forward
  -- constructor equations. Specializations should not unfold a large proof.
  abstract
    comparisonIsEquiv : isEquiv (equivFun rawEquiv)
    comparisonIsEquiv = snd rawEquiv

  comparison : Space ≃ PO.Pushout f g
  comparison = equivFun rawEquiv , comparisonIsEquiv

  onLeft : (x : L′) → equivFun comparison (PO.inl x) ≡ PO.inl (equivFun left x)
  onLeft x = refl

  onRight : (x : R′) → equivFun comparison (PO.inr x) ≡ PO.inr (equivFun right x)
  onRight x = refl

  -- Full action on the gluing path, including its two boundary adjustments.
  -- Dropping these adjustments would give the wrong endpoints in general.
  onAttachment : (x : M′) → cong (equivFun comparison) (PO.push x) ≡
    ((λ i → PO.inl (leftSquare x i))
      ∙∙ PO.push (equivFun middle x)
      ∙∙ (λ i → PO.inr (rightSquare x (~ i))))
  onAttachment x = refl
