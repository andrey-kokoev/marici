{-# OPTIONS --safe --cubical --guardedness #-}
module RamseyNativeFieldInterpretation where
open import Cubical.Foundations.Prelude
open import Cubical.Foundations.Equiv
open import RamseyNativeDerivedComparison

module Interpretation (Root Frame View A : Type) (Valid : Root → Type)
  (view : Frame → Root → View) (root-field : Root → A)
  (Field : Frame → Type) (frame : (f : Frame) → A ≃ Field f) where
  module P = Presentations Root Frame View Valid view
  evaluate : (a : Root) (v : Valid a) (f : Frame) → N.Ty (P.display a v f) → Field f
  evaluate a v f x = equivFun (frame f) (root-field (fst (snd x)))
  transfer : (f g : Frame) → Field f → Field g
  transfer f g y = equivFun (frame g) (invEq (frame f) y)
  native-semantic-square : (a : Root) (v : Valid a) (f g : Frame) (x : N.Ty (P.display a v f))
    → transfer f g (evaluate a v f x)
      ≡ evaluate a v g (equivFun (P.equivalence a v f g) x)
  native-semantic-square a v f g x =
    cong (equivFun (frame g)) (retEq (frame f) (root-field (fst (snd x))))
  identity-cell : (f : Frame) (y : Field f) → transfer f f y ≡ y
  identity-cell f y = secEq (frame f) y
  composition-cell : (f g h : Frame) (y : Field f)
    → transfer g h (transfer f g y) ≡ transfer f h y
  composition-cell f g h y = cong (equivFun (frame h)) (retEq (frame g) (invEq (frame f) y))
  decoded-root : (a : Root) (v : Valid a) (f : Frame) (x : N.Ty (P.display a v f))
    → invEq (frame f) (evaluate a v f x) ≡ root-field (fst (snd x))
  decoded-root a v f x = retEq (frame f) (root-field (fst (snd x)))
  actual-value : (a : Root) (v : Valid a) (f : Frame)
    → evaluate a v f (N.value (P.display a v f)) ≡ equivFun (frame f) (root-field a)
  actual-value a v f = refl
