{-# OPTIONS --safe --cubical --guardedness #-}
module ClosureAppendEndpointCoherence where

open import Cubical.Foundations.Prelude
open import Cubical.Foundations.Equiv
open import Cubical.Foundations.Univalence using (pathToEquiv)
open import Cubical.Foundations.GroupoidLaws using (rUnit; lUnit)
open import Cubical.Foundations.Path using (compPath→Square)
import Cubical.HITs.Pushout.Base as PO
open import ClosurePushoutTransportCoherence using (module FixedLeft)
open import ClosureRotationAppendReduction using (module Reduction)

module Coherence (K : Type) (Piece : K → Type) (Boundary : K → K → Type)
  (attachL : {a b : K} → Boundary a b → Piece a)
  (attachR : {a b : K} → Boundary a b → Piece b) where
  module D = Reduction K Piece Boundary attachL attachR
  open D.G.G.A.N

  -- The recursive word step needs a square WITH first-endpoint coherence.
  -- Its projection is the earlier word-only obligation, not a new axiom.
  module Words {a b c d e f : K}
    (u : Word a b) (v : Word c d) (w : Word e f) where
    module W = D.Words u v w

    sourceFirst : Piece a → W.Raw.Left
    sourceFirst x = PO.inl (PO.inl (first u x))

    leftFirst : (x : Piece a) → W.leftFlat (sourceFirst x) ≡ first ((u ++ v) ++ w) x
    leftFirst x = cong (λ z → equivFun (appendFrame (u ++ v) w) (PO.inl z)) (appendFirst u v x)
      ∙ appendFirst (u ++ v) w x

    rightFirst : (x : Piece a) →
      W.returnIndex (W.rightFlat (W.Raw.associate (sourceFirst x))) ≡ first ((u ++ v) ++ w) x
    rightFirst x = cong W.returnIndex (appendFirst u (v ++ w) x)
      ∙ fromPathP (λ i → first (sym W.association i) x)

    record AppendData : Type where
      constructor pointed
      field
        square : W.AppendSquare
        firstCoherence : (x : Piece a) →
          PathP (λ i → square (sourceFirst x) i ≡ first ((u ++ v) ++ w) x)
            (rightFirst x) (leftFirst x)

  -- The strengthened singleton base is proved, including the higher cell.
  module SingleLeft (a : K) {b c d e : K} (v : Word b c) (w : Word d e) where
    module P = Words (single a) v w
    module B = D.SingleLeft a v w

    pointTransport : (x : Piece a) → P.W.returnIndex (PO.inl x) ≡ PO.inl x
    pointTransport x = transportRefl (PO.inl x)

    firstCoherence : (x : Piece a) →
      PathP (λ i → B.square (P.sourceFirst x) i ≡ first ((single a ++ v) ++ w) x)
        (P.rightFirst x) (P.leftFirst x)
    firstCoherence x = compPath→Square
      (cong₂ _∙_ (sym (rUnit (pointTransport x))) (sym (rUnit refl))
        ∙ sym (rUnit (pointTransport x))
        ∙ lUnit (pointTransport x) ∙ rUnit (refl ∙ pointTransport x))

    coherence : P.AppendData
    coherence = P.pointed B.square firstCoherence

  -- Exact transport/comparison bridge for the non-singleton word step.
  -- This does not assume the missing append coherence for its tail.
  module Prefix (a : K) {b c d e f g : K}
    (u : Word b c) (v : Word d e) (w : Word f g) where
    module Lower = D.Words u v w
    module Upper = D.Words (cons a u) v w
    module Transport = FixedLeft (attachL {a} {b})

    diagramPath : Path Transport.Diagram
      (Normal (u ++ (v ++ w)) , λ s → first (u ++ (v ++ w)) (attachR s))
      (Normal ((u ++ v) ++ w) , λ s → first ((u ++ v) ++ w) (attachR s))
    diagramPath i = Normal (sym Lower.association i) , λ s → first (sym Lower.association i) (attachR s)

    comparison : Normal (cons a (u ++ (v ++ w))) ≃ Normal (cons a ((u ++ v) ++ w))
    comparison = Transport.replacement diagramPath

    agreesWithReturn : (x : Normal (cons a (u ++ (v ++ w)))) →
      Upper.returnIndex x ≡ equivFun comparison x
    agreesWithReturn = Transport.agreesWithTransport diagramPath

    framePath : pathToEquiv (λ i → Normal (sym Upper.association i)) ≡ comparison
    framePath = Transport.framePath diagramPath

    firstWitness : (x : Piece a) → Upper.returnIndex (PO.inl x) ≡ PO.inl x
    firstWitness x = fromPathP (λ i → first (sym Upper.association i) x)

    firstWitnessPath : (x : Piece a) →
      PathP (λ i → equivFun (framePath i) (PO.inl x) ≡ PO.inl x)
        (firstWitness x) refl
    firstWitnessPath = Transport.leftWitnessPath diagramPath

-- ClosureAppendInduction constructs the non-singleton step using this
-- endpoint-aware state, the transport bridge, and the native pentagon.
