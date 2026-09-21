{-# OPTIONS --safe --cubical --guardedness #-}
module ClosureMiddleSubtreeRotationAdmission where

open import Cubical.Foundations.Prelude
open import Cubical.Foundations.Equiv
open import Cubical.Foundations.GroupoidLaws using (rUnit)
import Cubical.HITs.Pushout.Base as PO
open import ClosureFiniteGluingNormalization using (module LiftSpan)
open import ClosureRotationAdmission using (module Admission)
open import ClosureSpanComparisonCoherence using
  (module MiddleRightNaturality; module RightComposition)

module Subtrees (K : Type) (Piece : K → Type) (Boundary : K → K → Type)
  (attachL : {a b : K} → Boundary a b → Piece a)
  (attachR : {a b : K} → Boundary a b → Piece b) where
  module A = Admission K Piece Boundary attachL attachR
  open A.N

  -- Both Q and R are arbitrary finite subtrees. A alone is a leaf.
  module LeftLeaf (a : K) {b c d e : K}
    {v : Word b c} {w : Word d e} (q : Bracket v) (r : Bracket w) where

    word : Word a e
    word = cons a (v ++ w)

    leftTree rightTree : Bracket word
    leftTree = fork (fork (leaf a) q) r
    rightTree = fork (leaf a) (fork q r)

    module Nat = MiddleRightNaturality (attachL {a} {b})
      (λ s → firstAt q (attachR s)) (λ t → lastAt q (attachL t))
      (λ t → firstAt r (attachR t))
      (λ s → first v (attachR s)) (λ t → last v (attachL t))
      (λ t → first w (attachR t))
      (normalize q) (normalize r)
      (funExt (λ s → normalizeFirst q (attachR s)))
      (funExt (λ t → normalizeLast q (attachL t)))
      (funExt (λ t → normalizeFirst r (attachR t)))

    subframePath : normalize (fork (leaf a) q) ≡ Nat.AB.equivalence
    subframePath = equivEq refl

    subLastPath : (x : Piece c) →
      PathP (λ i → equivFun (subframePath i) (PO.inr (lastAt q x)) ≡ PO.inr (last v x))
        (normalizeLast (fork (leaf a) q) x) (cong PO.inr (normalizeLast q x))
    subLastPath x = sym (rUnit (cong PO.inr (normalizeLast q x)))

    leftChildren : I → Nat.Source.Left ≃ Nat.Target.Left
    leftChildren i = LiftSpan.equivalence Nat.Source.attachLeft
      (λ t → firstAt r (attachR t)) Nat.Target.attachLeft (λ t → first w (attachR t))
      (idEquiv (Boundary c d)) (subframePath i) (normalize r)
      (funExt (λ t → subLastPath (attachL t) i))
      (funExt (λ t → normalizeFirst r (attachR t)))

    module Compose = RightComposition (attachL {a} {b})
      Nat.Source.attachRight Nat.Target.attachRight (λ s → first (v ++ w) (attachR s))
      Nat.BC.equivalence (appendFrame v w)
      (λ i s → PO.inl (normalizeFirst q (attachR s) i))
      (funExt (λ s → appendFirst v w (attachR s)))

    leftToForm : equivFun (normalize leftTree) ≡
      (λ x → equivFun Compose.Second.equivalence
        (Nat.Target.associate (equivFun Nat.Left.equivalence x)))
    leftToForm i x = equivFun (appendFrame (cons a v) w) (equivFun (leftChildren i) x)

    rightIsCombined : equivFun (normalize rightTree) ≡ equivFun Compose.Combined.equivalence
    rightIsCombined = refl

    -- Composition of the two span comparisons is proved, not assumed.
    -- This is where the middle subtree's endpoint-square data matters.
    abstract
      rotationSquare : (x : Realize leftTree) →
        equivFun (normalize rightTree) (Nat.Source.associate x) ≡ equivFun (normalize leftTree) x
      rotationSquare x = cong (λ F → F (Nat.Source.associate x)) rightIsCombined
        ∙ sym (Compose.compositionAt (Nat.Source.associate x))
        ∙ cong (equivFun Compose.Second.equivalence) (sym (Nat.naturalityAt x))
        ∙ sym (cong (λ F → F x) leftToForm)

    module E = A.Edges word

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

-- Variable left subtrees still require the reindexed append-associativity
-- normalization square. This theorem does not silently assume that square.
