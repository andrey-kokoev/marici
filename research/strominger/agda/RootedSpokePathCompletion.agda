{-# OPTIONS --safe --cubical --guardedness #-}
module RootedSpokePathCompletion where

open import Cubical.Foundations.Prelude
open import Cubical.Foundations.GroupoidLaws using (assoc; rCancel; lUnit)
open import MarkedTetrahedronCoherence using (module Tetrahedra)

-- Three paths with a common origin. Reuse the existing path algebra and
-- marked-horn completion, without any metric or extra branch edge input.
module FromSpokes {ℓ : Level} {X : Type ℓ} {a b c d : X}
  (ab : a ≡ b) (ac : a ≡ c) (ad : a ≡ d) where

  module T = Tetrahedra X

  cancel-root : {y z : X} (p : a ≡ y) (q : a ≡ z)
    → p ∙ (sym p ∙ q) ≡ q
  cancel-root p q =
    assoc p (sym p) q
    ∙ cong (λ t → t ∙ q) (rCancel p)
    ∙ sym (lUnit q)

  bc : b ≡ c
  bc = sym ab ∙ ac
  bd : b ≡ d
  bd = sym ab ∙ ad
  cd : c ≡ d
  cd = sym ac ∙ ad

  edges : T.Edges a b c d
  edges = record
    { e01 = ab ; e12 = bc ; e02 = ac
    ; e23 = cd ; e13 = bd ; e03 = ad }

  module O = T.Over edges

  faceABC : O.Face012
  faceABC = cancel-root ab ac
  faceABD : O.Face013
  faceABD = cancel-root ab ad
  faceACD : O.Face023
  faceACD = cancel-root ac ad

  -- The current marked-tetrahedron rule supplies the remaining face BCD
  -- together with its coherence, keeping the original spokes fixed.
  certificate : isContr (O.Missing123 faceABC faceABD faceACD)
  certificate = O.unique123 faceABC faceABD faceACD

  faceBCD : O.Face123
  faceBCD = fst (fst certificate)
  tetrahedron : O.Tetrahedron faceABC faceBCD faceABD faceACD
  tetrahedron = snd (fst certificate)

  original-AB-retained : T.Edges.e01 edges ≡ ab
  original-AB-retained = refl
  original-AC-retained : T.Edges.e02 edges ≡ ac
  original-AC-retained = refl
  original-AD-retained : T.Edges.e03 edges ≡ ad
  original-AD-retained = refl
