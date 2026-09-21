{-# OPTIONS --safe --cubical --guardedness #-}
module ClosureGeneralRotationAdmission where

open import Cubical.Foundations.Prelude
open import Cubical.Foundations.Equiv
open import Cubical.Foundations.GroupoidLaws using (rUnit)
import Cubical.HITs.Pushout.Base as PO
open import ClosureFiniteGluingNormalization using (module LiftSpan)
open import ClosureRotationAdmission using (module Admission)
open import ClosureGluingReassociation using (module Chain)

-- The identity span comparison has extra unit compositions on attachments.
-- Its homotopy to identity must include those paths, not only the vertices.
module IdentitySpan {S L R : Type} (f : S → L) (g : S → R) where
  module C = LiftSpan f g f g (idEquiv S) (idEquiv L) (idEquiv R) refl refl

  unchanged : (x : PO.Pushout f g) → equivFun C.equivalence x ≡ x
  unchanged (PO.inl x) = refl
  unchanged (PO.inr y) = refl
  unchanged (PO.push s i) j = sym (rUnit (PO.push s)) j i

module General (K : Type) (Piece : K → Type) (Boundary : K → K → Type)
  (attachL : {a b : K} → Boundary a b → Piece a)
  (attachR : {a b : K} → Boundary a b → Piece b) where
  module A = Admission K Piece Boundary attachL attachR
  open A.N

  module Pair (a b : K) where
    tree : Bracket (cons a (single b))
    tree = fork (leaf a) (leaf b)

    module Id = IdentitySpan (attachL {a} {b}) attachR

    framePath : normalize tree ≡ idEquiv (Realize tree)
    framePath = equivEq (funExt Id.unchanged)

    -- Contract the endpoint witnesses along WITH the frame. Omitting these
    -- two squares would not justify substituting this frame into a parent.
    firstPath : (x : Piece a) →
      PathP (λ i → equivFun (framePath i) (PO.inl x) ≡ PO.inl x)
        (normalizeFirst tree x) refl
    firstPath x = sym (rUnit refl)

    lastPath : (x : Piece b) →
      PathP (λ i → equivFun (framePath i) (PO.inr x) ≡ PO.inr x)
        (normalizeLast tree x) refl
    lastPath x = sym (rUnit refl)

  module ThreeLeaf (a b c : K) where
    module AB = Pair a b
    module BC = Pair b c
    module Raw = Chain (Piece a) (Piece b) (Piece c)
      (Boundary a b) (Boundary b c) attachL attachR attachL attachR

    word : Word a c
    word = cons a (cons b (single c))

    leftTree rightTree : Bracket word
    leftTree = fork AB.tree (leaf c)
    rightTree = fork (leaf a) BC.tree

    module E = A.Edges word
    module LeftId = IdentitySpan Raw.attachLeft (attachR {b} {c})
    module RightId = IdentitySpan (attachL {a} {b}) Raw.attachRight

    leftChildren : I → Raw.Left ≃ Raw.Left
    leftChildren i = LiftSpan.equivalence Raw.attachLeft attachR Raw.attachLeft attachR
      (idEquiv (Boundary b c)) (AB.framePath i) (idEquiv (Piece c))
      (funExt (λ t → AB.lastPath (attachL t) i)) refl

    rightChildren : I → Raw.Right ≃ Raw.Right
    rightChildren i = LiftSpan.equivalence attachL Raw.attachRight attachL Raw.attachRight
      (idEquiv (Boundary a b)) (idEquiv (Piece a)) (BC.framePath i)
      refl (funExt (λ s → BC.firstPath (attachR s) i))

    append : Raw.Left → Raw.Right
    append = equivFun (appendFrame (cons a (single b)) (single c))

    leftToAssociate : equivFun (normalize leftTree) ≡ Raw.associate
    leftToAssociate =
      (λ i x → append (equivFun (leftChildren i) x))
      ∙ funExt (λ x → cong append (LeftId.unchanged x))
      ∙ funExt (λ x → RightId.unchanged (Raw.associate x))

    rightToIdentity : equivFun (normalize rightTree) ≡ (λ x → x)
    rightToIdentity = (λ i x → equivFun (rightChildren i) x) ∙ funExt RightId.unchanged

    -- No invertibility, truncation, or emptiness hypotheses on attachments.
    rotationSquare : (x : Realize leftTree) →
      equivFun (normalize rightTree) (Raw.associate x) ≡ equivFun (normalize leftTree) x
    rotationSquare x = cong (λ F → F (Raw.associate x)) rightToIdentity
      ∙ sym (cong (λ F → F x) leftToAssociate)

    forward : E.Admitted leftTree rightTree
    forward = E.admitted Raw.associate rotationSquare

    backward : E.Admitted rightTree leftTree
    backward = E.admitted Raw.unassociate (λ y →
      sym (rotationSquare (Raw.unassociate y))
      ∙ cong (equivFun (normalize rightTree)) (Raw.associateSection y))

    nativeMatchesGenerated : Raw.associate ≡ Comparisons.change word leftTree rightTree
    nativeMatchesGenerated = funExt (E.matchesNormalForm forward)

    module Presentations = E.Presentations leftTree

    compatibleComparison : Presentations.pack rightTree forward ≡
      Presentations.Views.Cuts.canonical rightTree
    compatibleComparison = Presentations.agreesWithGenerated rightTree forward

-- This removes the invertible-leg gate for THREE LEAVES. Rotating arbitrary
-- variable subtrees additionally requires word-index reassociation and a
-- corresponding generalization of the endpoint-preserving frame homotopy.
