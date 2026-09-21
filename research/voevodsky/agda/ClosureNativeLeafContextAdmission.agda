{-# OPTIONS --safe --cubical --guardedness #-}
module ClosureNativeLeafContextAdmission where

open import Cubical.Foundations.Prelude
open import Cubical.Foundations.Equiv
open import Cubical.Foundations.GroupoidLaws using (cong-∙; rUnit)
open import Cubical.Foundations.Path using (compPath→Square)
import Cubical.HITs.Pushout.Base as PO
open import ClosureGeneralRotationAdmission using (module General)
open import ClosureCoherentContextAdmission using (module Contexts)

-- Nullity here concerns selected unit paths, not arbitrary realization loops.
nullSquare : {X : Type} {x : X} (h p q : x ≡ x) →
  h ≡ refl → p ≡ refl → q ≡ refl → PathP (λ i → h i ≡ x) p q
nullSquare h p q hh hp hq = compPath→Square
  (cong₂ _∙_ hh hq ∙ sym (cong (λ r → r ∙ refl) hp))

module Native (K : Type) (Piece : K → Type) (Boundary : K → K → Type)
  (attachL : {a b : K} → Boundary a b → Piece a)
  (attachR : {a b : K} → Boundary a b → Piece b) where
  module G = General K Piece Boundary attachL attachR
  module C = Contexts K Piece Boundary attachL attachR
  open G.A.N

  module Three (a b c : K) where
    module T = G.ThreeLeaf a b c
    module Ports = C.C.Ports

    change : C.C.Change T.leftTree T.rightTree
    change = C.C.change T.Raw.reassociation (equivEq (funExt T.rotationSquare))

    firstPort : Ports.First change
    firstPort x = refl
    lastPort : Ports.Last change
    lastPort x = refl

    private
      left₁ : equivFun (normalize T.leftTree) ≡ (λ x → T.append (equivFun T.LeftId.C.equivalence x))
      left₁ = λ i x → T.append (equivFun (T.leftChildren i) x)
      left₂ : (λ x → T.append (equivFun T.LeftId.C.equivalence x)) ≡ T.append
      left₂ = funExt (λ x → cong T.append (T.LeftId.unchanged x))
      left₃ : T.append ≡ T.Raw.associate
      left₃ = funExt (λ x → T.RightId.unchanged (T.Raw.associate x))
      right₁ : equivFun (normalize T.rightTree) ≡ equivFun T.RightId.C.equivalence
      right₁ = λ i x → equivFun (T.rightChildren i) x
      right₂ : equivFun T.RightId.C.equivalence ≡ (λ x → x)
      right₂ = funExt T.RightId.unchanged
      includeBC : T.Raw.BC → T.Raw.Right
      includeBC = PO.inr

    firstLeftNull : (x : Piece a) →
      cong (λ F → F (PO.inl (PO.inl x))) T.leftToAssociate ≡ refl
    firstLeftNull x = cong-∙ (λ F → F (PO.inl (PO.inl x))) left₁ (left₂ ∙ left₃)
      ∙ cong (λ q → refl ∙ q) (cong-∙ (λ F → F (PO.inl (PO.inl x))) left₂ left₃ ∙ sym (rUnit refl))
      ∙ sym (rUnit refl)

    lastLeftNull : (x : Piece c) → cong (λ F → F (PO.inr x)) T.leftToAssociate ≡ refl
    lastLeftNull x = cong-∙ (λ F → F (PO.inr x)) left₁ (left₂ ∙ left₃)
      ∙ cong (λ q → refl ∙ q) (cong-∙ (λ F → F (PO.inr x)) left₂ left₃ ∙ sym (rUnit refl))
      ∙ sym (rUnit refl)

    firstRightNull : (x : Piece a) → cong (λ F → F (PO.inl x)) T.rightToIdentity ≡ refl
    firstRightNull x = cong-∙ (λ F → F (PO.inl x)) right₁ right₂ ∙ sym (rUnit refl)
    lastRightNull : (x : Piece c) → cong (λ F → F (PO.inr (PO.inr x))) T.rightToIdentity ≡ refl
    lastRightNull x = cong-∙ (λ F → F (PO.inr (PO.inr x))) right₁ right₂ ∙ sym (rUnit refl)

    firstActionNull : (x : Piece a) → T.rotationSquare (firstAt T.leftTree x) ≡ refl
    firstActionNull x = cong₂ _∙_ (firstRightNull x) (cong sym (firstLeftNull x)) ∙ sym (rUnit refl)
    lastActionNull : (x : Piece c) → T.rotationSquare (lastAt T.leftTree x) ≡ refl
    lastActionNull x = cong₂ _∙_ (lastRightNull x) (cong sym (lastLeftNull x)) ∙ sym (rUnit refl)

    firstSourceNull : (x : Piece a) → normalizeFirst T.leftTree x ≡ refl
    firstSourceNull x = cong (λ (p : Path T.Raw.AB (PO.inl x) (PO.inl x)) →
      cong (λ z → T.append (PO.inl z)) p ∙ refl) (sym (rUnit refl)) ∙ sym (rUnit refl)
    lastSourceNull : (x : Piece c) → normalizeLast T.leftTree x ≡ refl
    lastSourceNull x = sym (rUnit refl)
    firstTargetNull : (x : Piece a) → normalizeFirst T.rightTree x ≡ refl
    firstTargetNull x = sym (rUnit refl)
    lastTargetNull : (x : Piece c) → normalizeLast T.rightTree x ≡ refl
    lastTargetNull x = cong (λ (p : Path T.Raw.BC (PO.inr x) (PO.inr x)) →
      cong includeBC p ∙ refl) (sym (rUnit refl)) ∙ sym (rUnit refl)

    firstCoherence : Ports.FirstCoherence change firstPort
    firstCoherence x = nullSquare _ _ _ (firstActionNull x)
      (cong (λ p → refl ∙ p) (firstTargetNull x) ∙ sym (rUnit refl)) (firstSourceNull x)
    lastCoherence : Ports.LastCoherence change lastPort
    lastCoherence x = nullSquare _ _ _ (lastActionNull x)
      (cong (λ p → refl ∙ p) (lastTargetNull x) ∙ sym (rUnit refl)) (lastSourceNull x)

    coherent : C.Coherent T.leftTree T.rightTree
    coherent = C.coherent change firstPort lastPort firstCoherence lastCoherence

    module Hole = C.InHole T.word
    contextual : {d e : K} {w : Word d e} (context : Hole.Context w) →
      G.A.Edges.Admitted w (Hole.plug context T.leftTree) (Hole.plug context T.rightTree)
    contextual context = Hole.admitted context coherent

-- The hole is a native three-leaf rotation. Contexts and siblings are
-- arbitrary; the arbitrary-three-SUBTREE port package is still separate.
