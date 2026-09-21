{-# OPTIONS --safe --cubical --guardedness #-}
module ClosureSubtreeRotationAdmission where

open import Cubical.Foundations.Prelude
open import Cubical.Foundations.Equiv
open import Cubical.Foundations.Univalence using (pathToEquiv)
open import Cubical.Foundations.GroupoidLaws using (rUnit; cong-∙∙)
import Cubical.HITs.Pushout.Base as PO
open import ClosureFiniteGluingNormalization using (module LiftSpan)
open import ClosureGeneralRotationAdmission using (module General; module IdentitySpan)
open import ClosureGluingReassociation using (module Chain)

-- Naturality of the native associator when the right piece is replaced by
-- an equivalent realization. The attachment square hk is retained on paths.
module RightNaturality {A B C C′ S T : Type}
  (f : S → A) (g : S → B) (h : T → B) (k : T → C) (k′ : T → C′)
  (e : C ≃ C′) (hk : (λ t → equivFun e (k t)) ≡ k′) where
  module Source = Chain A B C S T f g h k
  module Target = Chain A B C′ S T f g h k′
  module Left = LiftSpan Source.attachLeft k Target.attachLeft k′
    (idEquiv T) (idEquiv Source.AB) e refl hk
  module Inner = LiftSpan h k h k′ (idEquiv T) (idEquiv B) e refl hk
  module Right = LiftSpan f Source.attachRight f Target.attachRight
    (idEquiv S) (idEquiv A) Inner.equivalence refl refl

  include : Target.BC → Target.Right
  include = PO.inr

  naturalityAt : (x : Source.Left) →
    Target.associate (equivFun Left.equivalence x) ≡ equivFun Right.equivalence (Source.associate x)
  naturalityAt (PO.inl (PO.inl a)) = refl
  naturalityAt (PO.inl (PO.inr b)) = refl
  naturalityAt (PO.inl (PO.push s i)) j = rUnit (PO.push s) j i
  naturalityAt (PO.inr c) = refl
  naturalityAt (PO.push t i) j =
    (cong-∙∙ Target.associate refl (PO.push t) (λ z → PO.inr (hk (~ z) t))
      ∙ sym (cong-∙∙ include refl (PO.push t) (λ z → PO.inr (hk (~ z) t)))) j i

module Subtrees (K : Type) (Piece : K → Type) (Boundary : K → K → Type)
  (attachL : {a b : K} → Boundary a b → Piece a)
  (attachR : {a b : K} → Boundary a b → Piece b) where
  module G = General K Piece Boundary attachL attachR
  open G.A.N

  appendAssociative : {a b c d e f : K}
    (u : Word a b) (v : Word c d) (w : Word e f) → (u ++ v) ++ w ≡ u ++ (v ++ w)
  appendAssociative (single a) v w = refl
  appendAssociative (cons a u) v w = cong (cons a) (appendAssociative u v w)

  -- General syntax and native equivalence, including the word-index change.
  -- This module deliberately exposes, rather than assumes, the remaining
  -- normalization-square obligation for three arbitrary subtrees.
  module ReindexRotation {a b c d e f : K}
    {u : Word a b} {v : Word c d} {w : Word e f}
    (p : Bracket u) (q : Bracket v) (r : Bracket w) where
    association : (u ++ v) ++ w ≡ u ++ (v ++ w)
    association = appendAssociative u v w

    leftTree : Bracket ((u ++ v) ++ w)
    leftTree = fork (fork p q) r

    nativeRight : Bracket (u ++ (v ++ w))
    nativeRight = fork p (fork q r)

    -- Hide indexed-data transport before applying the recursive semantic
    -- interpreters; its endpoint laws remain available through treePath.
    abstract
      rightTree : Bracket ((u ++ v) ++ w)
      rightTree = subst Bracket (sym association) nativeRight

      treePath : PathP (λ i → Bracket (sym association i)) nativeRight rightTree
      treePath = subst-filler Bracket (sym association) nativeRight

    realizationPath : Realize nativeRight ≡ Realize rightTree
    realizationPath i = Realize (treePath i)

    normalizationPath : PathP
      (λ i → Realize (treePath i) ≃ Normal (sym association i))
      (normalize nativeRight) (normalize rightTree)
    normalizationPath i = normalize (treePath i)

    module Raw = Chain (Realize p) (Realize q) (Realize r)
      (Boundary b c) (Boundary d e)
      (λ s → lastAt p (attachL s)) (λ s → firstAt q (attachR s))
      (λ t → lastAt q (attachL t)) (λ t → firstAt r (attachR t))

    nativeEquivalence : Realize leftTree ≃ Realize rightTree
    nativeEquivalence = compEquiv Raw.reassociation (pathToEquiv realizationPath)

    module E = G.A.Edges ((u ++ v) ++ w)

    NormalizationSquare : Type
    NormalizationSquare = (x : Realize leftTree) →
      equivFun (normalize rightTree) (equivFun nativeEquivalence x) ≡
      equivFun (normalize leftTree) x

    admit : NormalizationSquare → E.Admitted leftTree rightTree
    admit proof = E.admitted (equivFun nativeEquivalence) proof

  module RightSubtree (a b : K) {c d : K} {u : Word c d} (r : Bracket u) where
    module AB = G.Pair a b

    word : Word a d
    word = cons a (cons b u)

    leftTree rightTree : Bracket word
    leftTree = fork AB.tree r
    rightTree = fork (leaf a) (fork (leaf b) r)

    -- The target is the normalizer of the FLATTENED word, not a separately
    -- postulated common frame for three opaque blocks.
    module Nat = RightNaturality (attachL {a} {b}) attachR (attachL {b} {c})
      (λ t → firstAt r (attachR t)) (λ t → first u (attachR t))
      (normalize r) (funExt (λ t → normalizeFirst r (attachR t)))
    module E = G.A.Edges word
    module RightId = IdentitySpan (attachL {a} {b}) Nat.Target.attachRight

    leftChildren : I → Nat.Source.Left ≃ Nat.Target.Left
    leftChildren i = LiftSpan.equivalence
      Nat.Source.attachLeft (λ t → firstAt r (attachR t))
      Nat.Target.attachLeft (λ t → first u (attachR t))
      (idEquiv (Boundary b c)) (AB.framePath i) (normalize r)
      (funExt (λ t → AB.lastPath (attachL t) i))
      (funExt (λ t → normalizeFirst r (attachR t)))

    subframePath : normalize (fork (leaf b) r) ≡ Nat.Inner.equivalence
    subframePath = equivEq refl

    subFirstPath : (x : Piece b) →
      PathP (λ i → equivFun (subframePath i) (PO.inl x) ≡ PO.inl x)
        (normalizeFirst (fork (leaf b) r) x) refl
    subFirstPath x = sym (rUnit refl)

    rightChildren : I → Nat.Source.Right ≃ Nat.Target.Right
    rightChildren i = LiftSpan.equivalence
      attachL Nat.Source.attachRight attachL Nat.Target.attachRight
      (idEquiv (Boundary a b)) (idEquiv (Piece a)) (subframePath i)
      refl (funExt (λ s → subFirstPath (attachR s) i))

    append : Nat.Target.Left → Nat.Target.Right
    append = equivFun (appendFrame (cons a (single b)) u)

    leftToForm : equivFun (normalize leftTree) ≡
      (λ x → Nat.Target.associate (equivFun Nat.Left.equivalence x))
    leftToForm = (λ i x → append (equivFun (leftChildren i) x))
      ∙ funExt (λ x → RightId.unchanged (Nat.Target.associate (equivFun Nat.Left.equivalence x)))

    rightToForm : equivFun (normalize rightTree) ≡ equivFun Nat.Right.equivalence
    rightToForm = λ i x → equivFun (rightChildren i) x

    abstract
      rotationSquare : (x : Realize leftTree) →
        equivFun (normalize rightTree) (Nat.Source.associate x) ≡ equivFun (normalize leftTree) x
      rotationSquare x = cong (λ F → F (Nat.Source.associate x)) rightToForm
        ∙ sym (Nat.naturalityAt x) ∙ sym (cong (λ F → F x) leftToForm)

    forward : E.Admitted leftTree rightTree
    forward = E.admitted Nat.Source.associate rotationSquare

    backward : E.Admitted rightTree leftTree
    backward = E.admitted Nat.Source.unassociate (λ y →
      sym (rotationSquare (Nat.Source.unassociate y))
      ∙ cong (equivFun (normalize rightTree)) (Nat.Source.associateSection y))

    nativeMatchesGenerated : Nat.Source.associate ≡ Comparisons.change word leftTree rightTree
    nativeMatchesGenerated = funExt (E.matchesNormalForm forward)

    module Presentations = E.Presentations leftTree
    compatibleComparison : Presentations.pack rightTree forward ≡
      Presentations.Views.Cuts.canonical rightTree
    compatibleComparison = Presentations.agreesWithGenerated rightTree forward

-- The right subtree is arbitrary; A and B are leaves. General word
-- reindexing is constructed above, but the normalization square for
-- variable left/middle subtrees still requires an endpoint-coherence proof.
