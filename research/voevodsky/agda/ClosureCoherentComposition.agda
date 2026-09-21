{-# OPTIONS --safe --cubical --guardedness #-}
module ClosureCoherentComposition where

open import Cubical.Foundations.Prelude
open import Cubical.Foundations.Equiv
open import Cubical.Foundations.GroupoidLaws using (cong-∙; assoc)
open import Cubical.Data.Sigma.Base using (_×_)
open import ClosureCoherentContextAdmission using (module Contexts)

private
  distribute : {A B : Type} (f : A → B) {x y z : A} {t : B}
    (p : x ≡ y) (q : y ≡ z) (r : f z ≡ t) →
    cong f (p ∙ q) ∙ r ≡ cong f p ∙ (cong f q ∙ r)
  distribute f p q r = cong (λ s → s ∙ r) (cong-∙ f p q)
    ∙ sym (assoc (cong f p) (cong f q) r)

module Composition (K : Type) (Piece : K → Type) (Boundary : K → K → Type)
  (attachL : {a b : K} → Boundary a b → Piece a)
  (attachR : {a b : K} → Boundary a b → Piece b) where
  module C = Contexts K Piece Boundary attachL attachR
  open C.C.A.N

  module Compose {a b : K} {w : Word a b} {p q r : Bracket w}
    (e : C.Coherent p q) (f : C.Coherent q r) where
    private
      eFrame = C.C.frame (C.Coherent.base e)
      fFrame = C.C.frame (C.Coherent.base f)
      eNorm = C.C.normalization (C.Coherent.base e)
      fNorm = C.C.normalization (C.Coherent.base f)

    frame : Realize p ≃ Realize r
    frame = compEquiv eFrame fFrame
    firstPort : (x : Piece a) → equivFun frame (firstAt p x) ≡ firstAt r x
    firstPort x = cong (equivFun fFrame) (C.Coherent.firstPort e x) ∙ C.Coherent.firstPort f x
    lastPort : (x : Piece b) → equivFun frame (lastAt p x) ≡ lastAt r x
    lastPort x = cong (equivFun fFrame) (C.Coherent.lastPort e x) ∙ C.Coherent.lastPort f x

    private
      Pointed : Type
      Pointed = Σ[ F ∈ (Realize p → Normal w) ]
        (((x : Piece a) → F (firstAt p x) ≡ first w x) ×
         ((x : Piece b) → F (lastAt p x) ≡ last w x))
      start finish : Pointed
      start = (λ x → equivFun (normalize r) (equivFun frame x)) ,
        (λ x → cong (equivFun (normalize r)) (firstPort x) ∙ normalizeFirst r x) ,
        (λ x → cong (equivFun (normalize r)) (lastPort x) ∙ normalizeLast r x)
      finish = equivFun (normalize p) , normalizeFirst p , normalizeLast p

      abstract
        whole : start ≡ finish
        whole =
          (λ i → fst start ,
            (λ x → distribute (equivFun (normalize r))
              (cong (equivFun fFrame) (C.Coherent.firstPort e x))
              (C.Coherent.firstPort f x) (normalizeFirst r x) i) ,
            (λ x → distribute (equivFun (normalize r))
              (cong (equivFun fFrame) (C.Coherent.lastPort e x))
              (C.Coherent.lastPort f x) (normalizeLast r x) i))
          ∙ (λ i → (λ x → equivFun (fNorm i) (equivFun eFrame x)) ,
            (λ x → cong (equivFun (fNorm i)) (C.Coherent.firstPort e x) ∙ C.Coherent.firstSquare f x i) ,
            (λ x → cong (equivFun (fNorm i)) (C.Coherent.lastPort e x) ∙ C.Coherent.lastSquare f x i))
          ∙ (λ i → equivFun (eNorm i) ,
            (λ x → C.Coherent.firstSquare e x i) , (λ x → C.Coherent.lastSquare e x i))

    change : C.C.Change p r
    change = C.C.change frame (equivEq (λ i → fst (whole i)))
    firstSquare : C.C.Ports.FirstCoherence change firstPort
    firstSquare x i = fst (snd (whole i)) x
    lastSquare : C.C.Ports.LastCoherence change lastPort
    lastSquare x i = snd (snd (whole i)) x
    coherent : C.Coherent p r
    coherent = C.coherent change firstPort lastPort firstSquare lastSquare

-- Actual composite frame and composite port paths, not normal-form
-- replacements. No equality of independently selected higher cells is used.
