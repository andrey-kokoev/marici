{-# OPTIONS --safe --cubical --guardedness #-}
module ClosureAppendBothEndpointCoherence where

open import Cubical.Foundations.Prelude
open import Cubical.Foundations.Equiv
open import Cubical.Foundations.GroupoidLaws using (rUnit; cong-∙)
open import Cubical.Foundations.Path using (compPath→Square; Square→compPath)
import Cubical.HITs.Pushout.Base as PO
open import ClosureAppendEndpointCoherence using (module Coherence)
open import ClosurePushoutMovingPortCoherence using (module MovingRight)

module Both (K : Type) (Piece : K → Type) (Boundary : K → K → Type)
  (attachL : {a b : K} → Boundary a b → Piece a)
  (attachR : {a b : K} → Boundary a b → Piece b) where
  module Original = Coherence K Piece Boundary attachL attachR
  module D = Original.D
  open D.G.G.A.N

  module Words {a b c d e f : K}
    (u : Word a b) (v : Word c d) (w : Word e f) where
    module W = D.Words u v w
    module First = Original.Words u v w
    open First public using (sourceFirst; leftFirst; rightFirst)

    sourceLast : Piece f → W.Raw.Left
    sourceLast x = PO.inr (last w x)
    leftLast : (x : Piece f) → W.leftFlat (sourceLast x) ≡ last ((u ++ v) ++ w) x
    leftLast x = appendLast (u ++ v) w x
    rightBeforeLast : (x : Piece f) → W.rightFlat (W.Raw.associate (sourceLast x)) ≡ last (u ++ (v ++ w)) x
    rightBeforeLast x = cong (λ z → equivFun (appendFrame u (v ++ w)) (PO.inr z)) (appendLast v w x)
      ∙ appendLast u (v ++ w) x
    rightLast : (x : Piece f) →
      W.returnIndex (W.rightFlat (W.Raw.associate (sourceLast x))) ≡ last ((u ++ v) ++ w) x
    rightLast x = cong W.returnIndex (rightBeforeLast x)
      ∙ fromPathP {A = λ i → Normal (sym W.association i)} (λ i → last (sym W.association i) x)

    record AppendData : Type where
      constructor pointed
      field
        square : W.AppendSquare
        firstCoherence : (x : Piece a) →
          PathP (λ i → square (sourceFirst x) i ≡ first ((u ++ v) ++ w) x)
            (rightFirst x) (leftFirst x)
        lastCoherence : (x : Piece f) →
          PathP (λ i → square (sourceLast x) i ≡ last ((u ++ v) ++ w) x)
            (rightLast x) (leftLast x)

  module SingleLeft (a : K) {b c d e : K} (v : Word b c) (w : Word d e) where
    module P = Words (single a) v w
    module Base = D.SingleLeft a v w
    include : Normal (v ++ w) → Normal (cons a (v ++ w))
    include = PO.inr

    lastCoherence : (x : Piece e) →
      PathP (λ i → Base.square (P.sourceLast x) i ≡ last ((single a ++ v) ++ w) x)
        (P.rightLast x) (P.leftLast x)
    lastCoherence x = compPath→Square
      (cong (λ h → h ∙ r) (sym (rUnit start))
        ∙ sym (Square→compPath (λ i j → transportRefl (r i) j))
        ∙ cong (λ s → cong P.W.returnIndex s ∙ finish) (rUnit r)
        ∙ rUnit (P.rightLast x))
      where
      r = cong include (appendLast v w x)
      start = transportRefl (include (equivFun (appendFrame v w) (PO.inr (last w x))))
      finish = transportRefl (include (last (v ++ w) x))

    coherence : P.AppendData
    coherence = P.pointed Base.square (Original.SingleLeft.firstCoherence a v w) lastCoherence

  module Prefix (a : K) {b c d e f g : K}
    (u : Word b c) (v : Word d e) (w : Word f g) where
    module Old = Original.Prefix a u v w
    open Old public
    module L = Words u v w
    module U = Words (cons a u) v w
    module Moving = MovingRight (attachL {a} {b})

    includeRight : Normal (u ++ (v ++ w)) → Normal (cons a (u ++ (v ++ w)))
    includeRight = PO.inr
    includeLeft : Normal ((u ++ v) ++ w) → Normal (cons a ((u ++ v) ++ w))
    includeLeft = PO.inr

    lastWitnessPath : (x : Piece g) →
      PathP (λ i → equivFun (framePath i) (U.W.rightFlat (U.W.Raw.associate (U.sourceLast x)))
        ≡ last ((cons a u ++ v) ++ w) x)
        (U.rightLast x) (cong includeLeft (L.rightLast x))
    lastWitnessPath x = subst
      (λ start → PathP (λ i → equivFun (framePath i)
        (U.W.rightFlat (U.W.Raw.associate (U.sourceLast x))) ≡ last ((cons a u ++ v) ++ w) x)
        start (cong includeLeft (L.rightLast x)))
      (sym adjustStart)
      (Moving.sourcePort diagramPath (L.rightBeforeLast x) (λ i → last (sym Lower.association i) x))
      where
      indexLast = fromPathP {A = λ i → Normal (sym Upper.association i)}
        (λ i → last (sym Upper.association i) x)
      adjustStart : U.rightLast x ≡ cong Upper.returnIndex (cong includeRight (L.rightBeforeLast x)) ∙ indexLast
      adjustStart = cong (λ p → cong Upper.returnIndex p ∙ indexLast)
        (sym (cong-∙ includeRight
          (cong (λ z → equivFun (appendFrame u (v ++ w)) (PO.inr z)) (appendLast v w x))
          (appendLast u (v ++ w) x)))

-- ClosureAppendBothEndpointInduction carries both fields through the
-- non-singleton factorization paths. This module supplies its base and
-- the dependent transport correction, without postulating either.
