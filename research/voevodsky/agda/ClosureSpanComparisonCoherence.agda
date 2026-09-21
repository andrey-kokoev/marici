{-# OPTIONS --safe --cubical --guardedness #-}
module ClosureSpanComparisonCoherence where

open import Cubical.Foundations.Prelude
open import Cubical.Foundations.Equiv
open import Cubical.Foundations.GroupoidLaws using (cong-∙; cong-∙∙; assoc; symDistr)
import Cubical.HITs.Pushout.Base as PO
open import ClosureFiniteGluingNormalization using (module LiftSpan)
open import ClosureGluingReassociation using (module Chain)

-- Associator naturality when BOTH the middle and right pieces change.
-- Attachment maps need not be invertible; the realization frames are equivalences.
module MiddleRightNaturality {A B C B′ C′ S T : Type}
  (f : S → A) (g : S → B) (h : T → B) (k : T → C)
  (g′ : S → B′) (h′ : T → B′) (k′ : T → C′)
  (eB : B ≃ B′) (eC : C ≃ C′)
  (hg : (λ s → equivFun eB (g s)) ≡ g′)
  (hh : (λ t → equivFun eB (h t)) ≡ h′)
  (hk : (λ t → equivFun eC (k t)) ≡ k′) where
  module Source = Chain A B C S T f g h k
  module Target = Chain A B′ C′ S T f g′ h′ k′
  module AB = LiftSpan f g f g′ (idEquiv S) (idEquiv A) eB refl hg
  module BC = LiftSpan h k h′ k′ (idEquiv T) eB eC hh hk
  module Left = LiftSpan Source.attachLeft k Target.attachLeft k′
    (idEquiv T) AB.equivalence eC (λ i t → PO.inr (hh i t)) hk
  module Right = LiftSpan f Source.attachRight f Target.attachRight
    (idEquiv S) (idEquiv A) BC.equivalence refl (λ i s → PO.inl (hg i s))

  include : Target.BC → Target.Right
  include = PO.inr

  naturalityAt : (x : Source.Left) →
    Target.associate (equivFun Left.equivalence x) ≡ equivFun Right.equivalence (Source.associate x)
  naturalityAt (PO.inl (PO.inl a)) = refl
  naturalityAt (PO.inl (PO.inr b)) = refl
  naturalityAt (PO.inl (PO.push s i)) j =
    cong-∙∙ (λ z → Target.associate (PO.inl z))
      refl (PO.push s) (λ z → PO.inr (hg (~ z) s)) j i
  naturalityAt (PO.inr c) = refl
  naturalityAt (PO.push t i) j =
    (cong-∙∙ Target.associate (λ z → PO.inl (PO.inr (hh z t)))
      (PO.push t) (λ z → PO.inr (hk (~ z) t))
      ∙ sym (cong-∙∙ include (λ z → PO.inl (hh z t))
        (PO.push t) (λ z → PO.inr (hk (~ z) t)))) j i

-- Composition of right-piece pushout comparisons, including the composite
-- square. This is a theorem about the actual maps used by LiftSpan.
module RightComposition {S A C C′ C″ : Type}
  (f : S → A) (g : S → C) (g′ : S → C′) (g″ : S → C″)
  (e : C ≃ C′) (d : C′ ≃ C″)
  (h₁ : (λ s → equivFun e (g s)) ≡ g′)
  (h₂ : (λ s → equivFun d (g′ s)) ≡ g″) where
  module First = LiftSpan f g f g′ (idEquiv S) (idEquiv A) e refl h₁
  module Second = LiftSpan f g′ f g″ (idEquiv S) (idEquiv A) d refl h₂

  combinedSquare : (λ s → equivFun (compEquiv e d) (g s)) ≡ g″
  combinedSquare = funExt (λ s → cong (equivFun d) (λ i → h₁ i s) ∙ (λ i → h₂ i s))

  module Combined = LiftSpan f g f g″ (idEquiv S) (idEquiv A)
    (compEquiv e d) refl combinedSquare

  include : C″ → PO.Pushout f g″
  include = PO.inr

  compositionAt : (x : PO.Pushout f g) →
    equivFun Second.equivalence (equivFun First.equivalence x) ≡ equivFun Combined.equivalence x
  compositionAt (PO.inl a) = refl
  compositionAt (PO.inr c) = refl
  compositionAt (PO.push s i) j =
    (cong-∙ (equivFun Second.equivalence) (PO.push s) (λ z → PO.inr (h₁ (~ z) s))
      ∙ sym (assoc (PO.push s) (λ z → PO.inr (h₂ (~ z) s))
        (λ z → PO.inr (equivFun d (h₁ (~ z) s))))
      ∙ cong (λ p → PO.push s ∙ p)
        (sym (cong-∙ include (λ z → h₂ (~ z) s) (λ z → equivFun d (h₁ (~ z) s)))
          ∙ cong (cong include)
            (sym (symDistr (cong (equivFun d) (λ z → h₁ z s)) (λ z → h₂ z s))))) j i

  compositionEquivalence : compEquiv First.equivalence Second.equivalence ≡ Combined.equivalence
  compositionEquivalence = equivEq (funExt compositionAt)
