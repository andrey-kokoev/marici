{-# OPTIONS --safe --cubical --guardedness #-}
module negative.ETreeBadS where
open import Cubical.Foundations.Prelude
open import ETreeSubstitution
bad-template : Tree Slot
bad-template = node (node (leaf f-slot) (leaf x-slot)) (leaf g-slot)
-- EXPECTED FAILURE: the second occurrence of x cannot be omitted.
bad : {A : Type} (f g x : Tree A)
  → instantiate3 bad-template f g x ≡ node (node f x) (node g x)
bad f g x = refl
