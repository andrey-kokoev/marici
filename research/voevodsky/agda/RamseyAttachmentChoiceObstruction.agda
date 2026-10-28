{-# OPTIONS --safe --cubical --guardedness #-}
module RamseyAttachmentChoiceObstruction where
open import Cubical.Foundations.Prelude
open import Cubical.Foundations.Equiv
open import Cubical.Data.Unit.Base using (Unit; tt)
open import Cubical.Data.Bool.Base using (Bool; false; true)
open import Cubical.Data.Bool.Properties using (false≢true)
open import Cubical.Data.Empty.Base using (⊥)

unit-path : (x y : Unit) → x ≡ y
unit-path tt tt = refl
one-not-two-choices : Unit ≃ Bool → ⊥
one-not-two-choices e = false≢true
  (sym (secEq e false) ∙ cong (equivFun e) (unit-path (invEq e false) (invEq e true)) ∙ secEq e true)
