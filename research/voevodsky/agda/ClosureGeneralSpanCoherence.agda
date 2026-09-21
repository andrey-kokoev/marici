{-# OPTIONS --safe --cubical --guardedness #-}
module ClosureGeneralSpanCoherence where

open import Cubical.Foundations.Prelude
open import Cubical.Foundations.Equiv
open import Cubical.Foundations.GroupoidLaws using
  (cong-∙; cong-∙∙; assoc; symDistr; doubleCompPath-elim; doubleCompPath-elim')
import Cubical.HITs.Pushout.Base as PO
open import ClosureFiniteGluingNormalization using (module LiftSpan)
open import ClosureGluingReassociation using (module Chain)

-- All three realization frames can change. Attachment maps are arbitrary.
module Naturality {A B C A′ B′ C′ S T : Type}
  (f : S → A) (g : S → B) (h : T → B) (k : T → C)
  (f′ : S → A′) (g′ : S → B′) (h′ : T → B′) (k′ : T → C′)
  (eA : A ≃ A′) (eB : B ≃ B′) (eC : C ≃ C′)
  (hf : (λ s → equivFun eA (f s)) ≡ f′)
  (hg : (λ s → equivFun eB (g s)) ≡ g′)
  (hh : (λ t → equivFun eB (h t)) ≡ h′)
  (hk : (λ t → equivFun eC (k t)) ≡ k′) where
  module Source = Chain A B C S T f g h k
  module Target = Chain A′ B′ C′ S T f′ g′ h′ k′
  module AB = LiftSpan f g f′ g′ (idEquiv S) eA eB hf hg
  module BC = LiftSpan h k h′ k′ (idEquiv T) eB eC hh hk
  module Left = LiftSpan Source.attachLeft k Target.attachLeft k′
    (idEquiv T) AB.equivalence eC (λ i t → PO.inr (hh i t)) hk
  module Right = LiftSpan f Source.attachRight f′ Target.attachRight
    (idEquiv S) eA BC.equivalence hf (λ i s → PO.inl (hg i s))

  include : Target.BC → Target.Right
  include = PO.inr

  naturalityAt : (x : Source.Left) →
    Target.associate (equivFun Left.equivalence x) ≡ equivFun Right.equivalence (Source.associate x)
  naturalityAt (PO.inl (PO.inl a)) = refl
  naturalityAt (PO.inl (PO.inr b)) = refl
  naturalityAt (PO.inl (PO.push s i)) j =
    cong-∙∙ (λ z → Target.associate (PO.inl z))
      (λ z → PO.inl (hf z s)) (PO.push s) (λ z → PO.inr (hg (~ z) s)) j i
  naturalityAt (PO.inr c) = refl
  naturalityAt (PO.push t i) j =
    (cong-∙∙ Target.associate (λ z → PO.inl (PO.inr (hh z t)))
      (PO.push t) (λ z → PO.inr (hk (~ z) t))
      ∙ sym (cong-∙∙ include (λ z → PO.inl (hh z t))
        (PO.push t) (λ z → PO.inr (hk (~ z) t)))) j i

-- The five paths need not be loops or trivial paths.
fivePaths : {X : Type} {a b c d e f : X}
  (p : a ≡ b) (q : b ≡ c) (r : c ≡ d) (s : d ≡ e) (t : e ≡ f) →
  (p ∙∙ (q ∙∙ r ∙∙ s) ∙∙ t) ≡ ((p ∙ q) ∙∙ r ∙∙ (s ∙ t))
fivePaths p q r s t = doubleCompPath-elim p (q ∙∙ r ∙∙ s) t
  ∙ cong (λ z → (p ∙ z) ∙ t) (doubleCompPath-elim' q r s)
  ∙ cong (λ z → z ∙ t) (assoc p q (r ∙ s))
  ∙ cong (λ z → z ∙ t) (assoc (p ∙ q) r s)
  ∙ sym (assoc ((p ∙ q) ∙ r) s t)
  ∙ sym (doubleCompPath-elim (p ∙ q) r (s ∙ t))

-- Both legs of each comparison may change. Boundary indexing is fixed.
module Composition {S L R L′ R′ L″ R″ : Type}
  (f : S → L) (g : S → R) (f′ : S → L′) (g′ : S → R′)
  (f″ : S → L″) (g″ : S → R″)
  (eL : L ≃ L′) (eR : R ≃ R′) (dL : L′ ≃ L″) (dR : R′ ≃ R″)
  (hf : (λ s → equivFun eL (f s)) ≡ f′)
  (hg : (λ s → equivFun eR (g s)) ≡ g′)
  (hf′ : (λ s → equivFun dL (f′ s)) ≡ f″)
  (hg′ : (λ s → equivFun dR (g′ s)) ≡ g″) where
  module First = LiftSpan f g f′ g′ (idEquiv S) eL eR hf hg
  module Second = LiftSpan f′ g′ f″ g″ (idEquiv S) dL dR hf′ hg′

  leftSquare : (λ s → equivFun (compEquiv eL dL) (f s)) ≡ f″
  leftSquare = funExt (λ s → cong (equivFun dL) (λ i → hf i s) ∙ (λ i → hf′ i s))
  rightSquare : (λ s → equivFun (compEquiv eR dR) (g s)) ≡ g″
  rightSquare = funExt (λ s → cong (equivFun dR) (λ i → hg i s) ∙ (λ i → hg′ i s))

  module Combined = LiftSpan f g f″ g″ (idEquiv S)
    (compEquiv eL dL) (compEquiv eR dR) leftSquare rightSquare

  includeLeft : L″ → PO.Pushout f″ g″
  includeLeft = PO.inl
  includeRight : R″ → PO.Pushout f″ g″
  includeRight = PO.inr

  compositionAt : (x : PO.Pushout f g) →
    equivFun Second.equivalence (equivFun First.equivalence x) ≡ equivFun Combined.equivalence x
  compositionAt (PO.inl x) = refl
  compositionAt (PO.inr y) = refl
  compositionAt (PO.push s i) j =
    (cong-∙∙ (equivFun Second.equivalence) (λ z → PO.inl (hf z s))
      (PO.push s) (λ z → PO.inr (hg (~ z) s))
      ∙ fivePaths (λ z → PO.inl (equivFun dL (hf z s))) (λ z → PO.inl (hf′ z s))
        (PO.push s) (λ z → PO.inr (hg′ (~ z) s)) (λ z → PO.inr (equivFun dR (hg (~ z) s)))
      ∙ (λ z → leftPath s z ∙∙ PO.push s ∙∙ rightPath s z)) j i
    where
    leftPath : (s : S) →
      (cong includeLeft (cong (equivFun dL) (λ z → hf z s)) ∙ cong includeLeft (λ z → hf′ z s)) ≡
      cong includeLeft (λ z → leftSquare z s)
    leftPath s = sym (cong-∙ includeLeft (cong (equivFun dL) (λ z → hf z s)) (λ z → hf′ z s))

    rightPath : (s : S) →
      (cong includeRight (λ z → hg′ (~ z) s) ∙ cong includeRight (λ z → equivFun dR (hg (~ z) s))) ≡
      cong includeRight (λ z → rightSquare (~ z) s)
    rightPath s = sym (cong-∙ includeRight (λ z → hg′ (~ z) s) (λ z → equivFun dR (hg (~ z) s)))
      ∙ cong (cong includeRight)
        (sym (symDistr (cong (equivFun dR) (λ z → hg z s)) (λ z → hg′ z s)))

  compositionEquivalence : compEquiv First.equivalence Second.equivalence ≡ Combined.equivalence
  compositionEquivalence = equivEq (funExt compositionAt)
