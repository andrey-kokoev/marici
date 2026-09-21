{-# OPTIONS --safe --cubical --guardedness #-}
module ClosureSubtreeAppendPortCoherence where

open import Cubical.Foundations.Prelude
open import Cubical.Foundations.Equiv
import Cubical.HITs.Pushout.Base as PO
open import ClosureAppendBothEndpointCoherence using (module Both)

module SubtreePorts (K : Type) (Piece : K → Type) (Boundary : K → K → Type)
  (attachL : {a b : K} → Boundary a b → Piece a)
  (attachR : {a b : K} → Boundary a b → Piece b) where
  module C = Both K Piece Boundary attachL attachR
  open C.D.G.G.A.N

  module Trees {a b c d e f : K}
    {u : Word a b} {v : Word c d} {w : Word e f}
    (p : Bracket u) (q : Bracket v) (r : Bracket w) where
    module W = C.Words u v w
    module T = C.D.Trees p q r

    toWords : Realize T.Indexed.leftTree → W.W.Raw.Left
    toWords = equivFun T.Nat.Left.equivalence

    firstBridge : (x : Piece a) → toWords (firstAt T.Indexed.leftTree x) ≡ W.sourceFirst x
    firstBridge x = cong (λ z → PO.inl (PO.inl z)) (normalizeFirst p x)

    lastBridge : (x : Piece f) → toWords (lastAt T.Indexed.leftTree x) ≡ W.sourceLast x
    lastBridge x = cong PO.inr (normalizeLast r x)

    rightForm leftForm : Realize T.Indexed.leftTree → Normal ((u ++ v) ++ w)
    rightForm y = W.W.returnIndex (W.W.rightFlat (W.W.Raw.associate (toWords y)))
    leftForm y = W.W.leftFlat (toWords y)

    firstRight : (x : Piece a) → rightForm (firstAt T.Indexed.leftTree x) ≡ first ((u ++ v) ++ w) x
    firstRight x = cong (λ z → W.W.returnIndex (W.W.rightFlat (W.W.Raw.associate z))) (firstBridge x)
      ∙ W.rightFirst x
    firstLeft : (x : Piece a) → leftForm (firstAt T.Indexed.leftTree x) ≡ first ((u ++ v) ++ w) x
    firstLeft x = cong W.W.leftFlat (firstBridge x) ∙ W.leftFirst x

    lastRight : (x : Piece f) → rightForm (lastAt T.Indexed.leftTree x) ≡ last ((u ++ v) ++ w) x
    lastRight x = cong (λ z → W.W.returnIndex (W.W.rightFlat (W.W.Raw.associate z))) (lastBridge x)
      ∙ W.rightLast x
    lastLeft : (x : Piece f) → leftForm (lastAt T.Indexed.leftTree x) ≡ last ((u ++ v) ++ w) x
    lastLeft x = cong W.W.leftFlat (lastBridge x) ∙ W.leftLast x

    module Transfer (data′ : W.AppendData) where
      square : (y : Realize T.Indexed.leftTree) → rightForm y ≡ leftForm y
      square y = W.AppendData.square data′ (toWords y)

      firstCoherence : (x : Piece a) →
        PathP (λ i → square (firstAt T.Indexed.leftTree x) i ≡ first ((u ++ v) ++ w) x)
          (firstRight x) (firstLeft x)
      firstCoherence x i = cong (λ z → W.AppendData.square data′ z i) (firstBridge x)
        ∙ W.AppendData.firstCoherence data′ x i

      lastCoherence : (x : Piece f) →
        PathP (λ i → square (lastAt T.Indexed.leftTree x) i ≡ last ((u ++ v) ++ w) x)
          (lastRight x) (lastLeft x)
      lastCoherence x i = cong (λ z → W.AppendData.square data′ z i) (lastBridge x)
        ∙ W.AppendData.lastCoherence data′ x i

-- This transfers the middle, word-square segment to actual subtree ports.
-- Child normalization witnesses are retained even when nonreflexive. The
-- outer leftToForm/rightToForm factorization cells are separate obligations.
