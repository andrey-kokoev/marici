{-# OPTIONS --safe --cubical --guardedness #-}
module ClosureArbitrarySubtreeRotationAdmission where

open import Cubical.Foundations.Prelude
open import Cubical.Foundations.Equiv
open import ClosureAppendInduction using (module Induction)

module General (K : Type) (Piece : K → Type) (Boundary : K → K → Type)
  (attachL : {a b : K} → Boundary a b → Piece a)
  (attachR : {a b : K} → Boundary a b → Piece b) where
  module I = Induction K Piece Boundary attachL attachR
  open I.C.D.G.G.A.N

  module Rotation {a b c d e f : K}
    {u : Word a b} {v : Word c d} {w : Word e f}
    (p : Bracket u) (q : Bracket v) (r : Bracket w) where
    module T = I.C.D.Trees p q r
    module W = I.C.Words u v w
    module Indexed = T.Indexed
    module E = Indexed.E

    word : Word a f
    word = (u ++ v) ++ w

    -- No attachment equivalence, endpoint equivalence, truncation, or
    -- externally supplied compatibility square is required.
    abstract
      appendSquare : T.W.AppendSquare
      appendSquare = W.AppendData.square (I.coherentAppend u v w)

      rotationSquare : Indexed.NormalizationSquare
      rotationSquare = T.rotationSquare appendSquare

    forward : E.Admitted Indexed.leftTree Indexed.rightTree
    forward = Indexed.admit rotationSquare

    backward : E.Admitted Indexed.rightTree Indexed.leftTree
    backward = E.admitted (invEq Indexed.nativeEquivalence) (λ y →
      sym (rotationSquare (invEq Indexed.nativeEquivalence y))
      ∙ cong (equivFun (normalize Indexed.rightTree)) (secEq Indexed.nativeEquivalence y))

    nativeMatchesGenerated : equivFun Indexed.nativeEquivalence ≡
      Comparisons.change word Indexed.leftTree Indexed.rightTree
    nativeMatchesGenerated = funExt (E.matchesNormalForm forward)

    nativeEquivalenceRetained : E.actionEquiv forward ≡ Indexed.nativeEquivalence
    nativeEquivalenceRetained = equivEq refl

    module Presentations = E.Presentations Indexed.leftTree
    compatibleComparison : Presentations.pack Indexed.rightTree forward ≡
      Presentations.Views.Cuts.canonical Indexed.rightTree
    compatibleComparison = Presentations.agreesWithGenerated Indexed.rightTree forward

-- This proves root rotations of THREE ARBITRARY finite subtrees, with
-- word reindexing. Contextual whiskering and arbitrary higher witnesses
-- are separate statements, not silently added to the theorem's scope.
