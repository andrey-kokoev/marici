{-# OPTIONS --safe --cubical --guardedness #-}
module ClosureAppendBothEndpointInduction where

open import Cubical.Foundations.Prelude
open import Cubical.Foundations.Equiv
open import Cubical.Foundations.Univalence using (pathToEquiv)
open import Cubical.Foundations.GroupoidLaws using (rUnit; lUnit)
import Cubical.HITs.Pushout.Base as PO
open import ClosureFiniteGluingNormalization using (module LiftSpan)
open import ClosureSpanComparisonCoherence using (module MiddleRightNaturality; module RightComposition)
open import ClosureGeneralSpanCoherence using (module Composition)
open import ClosureSubtreeRotationAdmission using (module RightNaturality)
open import ClosureGluingPentagon using (module FourPieces)
open import ClosureAppendBothEndpointCoherence using (module Both)
open import Cubical.Data.Sigma.Base using (_×_)
import ClosureAppendInduction as FirstOnly

module Induction (K : Type) (Piece : K → Type) (Boundary : K → K → Type)
  (attachL : {a b : K} → Boundary a b → Piece a)
  (attachR : {a b : K} → Boundary a b → Piece b) where
  module C = Both K Piece Boundary attachL attachR
  module Old = FirstOnly.Induction K Piece Boundary attachL attachR
  open C.D.G.G.A.N

  module Step (a : K) {b c d e f g : K}
    (u : Word b c) (v : Word d e) (w : Word f g) where
    module L = C.Words u v w
    module U = C.Words (cons a u) v w
    module Index = C.Prefix a u v w
    module P = FourPieces (Piece a) (Normal u) (Normal v) (Normal w)
      (Boundary a b) (Boundary c d) (Boundary e f)
      attachL (λ s → first u (attachR s)) (λ t → last u (attachL t))
      (λ t → first v (attachR t)) (λ z → last v (attachL z)) (λ z → first w (attachR z))

    leftE : L.W.Raw.Left ≃ Normal ((u ++ v) ++ w)
    leftE = compEquiv L.W.Left.equivalence (appendFrame (u ++ v) w)
    innerRightE : L.W.Raw.Right ≃ Normal (u ++ (v ++ w))
    innerRightE = compEquiv L.W.Right.equivalence (appendFrame u (v ++ w))
    returnE : Normal (u ++ (v ++ w)) ≃ Normal ((u ++ v) ++ w)
    returnE = pathToEquiv (λ i → Normal (sym L.W.association i))
    finalRightE : L.W.Raw.Right ≃ Normal ((u ++ v) ++ w)
    finalRightE = compEquiv innerRightE returnE
    rightE : L.W.Raw.Left ≃ Normal ((u ++ v) ++ w)
    rightE = compEquiv L.W.Raw.reassociation finalRightE

    module LL = LiftSpan attachL (λ s → L.sourceFirst (attachR s))
      attachL (λ s → first ((u ++ v) ++ w) (attachR s))
      (idEquiv (Boundary a b)) (idEquiv (Piece a)) leftE
      refl (funExt (λ s → L.leftFirst (attachR s)))
    module RR = LiftSpan attachL (λ s → L.sourceFirst (attachR s))
      attachL (λ s → first ((u ++ v) ++ w) (attachR s))
      (idEquiv (Boundary a b)) (idEquiv (Piece a)) rightE
      refl (funExt (λ s → L.rightFirst (attachR s)))

    pre : P.Start → P.Middle₂
    pre x = P.A-BC-D.associate (P.rotateLeft x)

    includeNormal : Normal ((u ++ v) ++ w) → Normal (cons a ((u ++ v) ++ w))
    includeNormal = PO.inr
    leftPort : (x : Piece g) → includeNormal (L.W.leftFlat (L.sourceLast x)) ≡ includeNormal (last ((u ++ v) ++ w) x)
    leftPort x = cong includeNormal (L.leftLast x)
    rightPort : (x : Piece g) → includeNormal (L.W.returnIndex (L.W.rightFlat (L.W.Raw.associate (L.sourceLast x)))) ≡ includeNormal (last ((u ++ v) ++ w) x)
    rightPort x = cong includeNormal (L.rightLast x)

    Pointed : Type
    Pointed = Σ[ state ∈ Old.Step.Pointed a u v w ]
      ((x : Piece g) → fst state (U.sourceLast x) ≡ includeNormal (last ((u ++ v) ++ w) x))

    pack : (F : P.Start → Normal (cons a ((u ++ v) ++ w))) →
      ((x : Piece a) → F (U.sourceFirst x) ≡ PO.inl x) →
      ((x : Piece g) → F (U.sourceLast x) ≡ includeNormal (last ((u ++ v) ++ w) x)) → Pointed
    pack F firstPort lastPort = (F , firstPort) , lastPort

    leftStart leftEnd rightStart rightEnd : Pointed
    leftStart = pack U.W.leftFlat (λ x → refl) leftPort
    leftEnd = pack (λ x → equivFun LL.equivalence (pre x)) (λ x → refl) leftPort
    rightStart = pack (λ x → U.W.returnIndex (U.W.rightFlat (U.W.Raw.associate x))) U.rightFirst U.rightLast
    rightEnd = pack (λ x → equivFun RR.equivalence (pre x)) (λ x → refl) rightPort

    -- Left factorization: normalize the BC block, reassociate, then append D.
    module LN = MiddleRightNaturality (attachL {a} {b}) P.ABC.attachRight
      (λ z → PO.inr (last v (attachL z))) (λ z → first w (attachR z))
      (λ s → first (u ++ v) (attachR s)) (λ z → last (u ++ v) (attachL z))
      (λ z → first w (attachR z)) (appendFrame u v) (idEquiv (Normal w))
      (funExt (λ s → appendFirst u v (attachR s)))
      (funExt (λ z → appendLast u v (attachL z))) refl

    module LC = Composition P.AB-C-D.attachLeft (λ z → first w (attachR z))
      P.A-BC-D.attachLeft (λ z → first w (attachR z))
      (λ z → last ((cons a u) ++ v) (attachL z)) (λ z → first w (attachR z))
      P.ABC.reassociation (idEquiv (Normal w)) LN.AB.equivalence (idEquiv (Normal w))
      refl refl (λ i z → PO.inr (appendLast u v (attachL z) i)) refl

    idFrame : compEquiv (idEquiv (Normal w)) (idEquiv (Normal w)) ≡ idEquiv (Normal w)
    idFrame = equivEq refl

    leftChildren : I → P.Start ≃ Join ((cons a u) ++ v) w
    leftChildren i = LiftSpan.equivalence P.AB-C-D.attachLeft (λ z → first w (attachR z))
      (λ z → last ((cons a u) ++ v) (attachL z)) (λ z → first w (attachR z))
      (idEquiv (Boundary e f)) (appendFrame (cons a u) v) (idFrame i)
      (funExt (λ z → sym (lUnit (cong PO.inr (appendLast u v (attachL z)))) i))
      (funExt (λ z → sym (rUnit refl) i))

    leftWhisker : (x : P.Start) → equivFun LC.First.equivalence x ≡ P.rotateLeft x
    leftWhisker = Old.Step.leftWhisker a u v w

    module LCompose = RightComposition (attachL {a} {b})
      (λ s → L.sourceFirst (attachR s))
      (λ s → PO.inl (first (u ++ v) (attachR s)))
      (λ s → first ((u ++ v) ++ w) (attachR s))
      L.W.Left.equivalence (appendFrame (u ++ v) w)
      (λ i s → PO.inl (appendFirst u v (attachR s) i))
      (funExt (λ s → appendFirst (u ++ v) w (attachR s)))

    leftFactor : leftStart ≡ leftEnd
    leftFactor =
      (λ i → pack (λ x → equivFun (appendFrame ((cons a u) ++ v) w)
        (equivFun (leftChildren (~ i)) x)) (λ x → refl) leftPort)
      ∙ (λ i → pack (λ x → equivFun (appendFrame ((cons a u) ++ v) w)
        (LC.compositionAt x (~ i))) (λ x → refl) leftPort)
      ∙ (λ i → pack (λ x → equivFun LCompose.Second.equivalence
        (LN.naturalityAt (equivFun LC.First.equivalence x) i)) (λ x → refl) leftPort)
      ∙ (λ i → pack (λ x → LCompose.compositionAt
        (P.A-BC-D.associate (equivFun LC.First.equivalence x)) i) (λ x → refl) leftPort)
      ∙ (λ i → pack (λ x → equivFun LL.equivalence
        (P.A-BC-D.associate (leftWhisker x i))) (λ x → refl) leftPort)

    -- Right factorization: append CD, reassociate, return the word index,
    -- and use the ACTUAL pentagon to reach the same source of the lower lift.
    module RN = RightNaturality (attachL {a} {b}) (λ s → first u (attachR s))
      (λ t → last u (attachL t)) P.BCD.attachRight
      (λ t → first (v ++ w) (attachR t)) (appendFrame v w)
      (funExt (λ t → appendFirst v w (attachR t)))

    module RCompose = RightComposition (attachL {a} {b})
      P.A-B-CD.attachRight (λ s → PO.inl (first u (attachR s)))
      (λ s → first (u ++ (v ++ w)) (attachR s))
      L.W.Right.equivalence (appendFrame u (v ++ w))
      refl (funExt (λ s → appendFirst u (v ++ w) (attachR s)))

    module Outside = RightComposition (attachL {a} {b}) P.A-B-CD.attachRight
      (λ s → first (u ++ (v ++ w)) (attachR s))
      (λ s → first ((u ++ v) ++ w) (attachR s)) innerRightE returnE
      (funExt (λ s → appendFirst u (v ++ w) (attachR s)))
      (funExt (λ s → fromPathP (λ i → first (sym L.W.association i) (attachR s))))

    rightChildren : I → P.Finish ≃ Normal (cons a (u ++ (v ++ w)))
    rightChildren i = LiftSpan.equivalence attachL P.A-B-CD.attachRight
      attachL (λ s → first (u ++ (v ++ w)) (attachR s))
      (idEquiv (Boundary a b)) (idEquiv (Piece a)) innerRightE refl
      (funExt (λ s → sym (lUnit (appendFirst u (v ++ w) (attachR s))) i))

    module LastCompose = RightComposition (attachL {a} {b})
      (λ s → L.sourceFirst (attachR s)) P.A-B-CD.attachRight
      (λ s → first ((u ++ v) ++ w) (attachR s))
      L.W.Raw.reassociation finalRightE refl (funExt (λ s → L.rightFirst (attachR s)))

    rightWhisker : (x : P.Middle₂) → equivFun LastCompose.First.equivalence x ≡ P.rotateRight x
    rightWhisker = Old.Step.rightWhisker a u v w

    lastChildren : I → P.Middle₂ ≃ Normal (cons a ((u ++ v) ++ w))
    lastChildren i = LiftSpan.equivalence attachL (λ s → L.sourceFirst (attachR s))
      attachL (λ s → first ((u ++ v) ++ w) (attachR s))
      (idEquiv (Boundary a b)) (idEquiv (Piece a)) rightE refl
      (funExt (λ s → sym (lUnit (L.rightFirst (attachR s))) i))

    rightFactor : rightStart ≡ rightEnd
    rightFactor =
      (λ i → pack (λ x → U.W.returnIndex (U.W.rightFlat (U.W.Raw.associate x)))
        (λ x → sym (lUnit (Index.firstWitness x)) i) U.rightLast)
      ∙ (λ i → pack (λ x → equivFun (Index.framePath i) (U.W.rightFlat (U.W.Raw.associate x)))
        (λ x → Index.firstWitnessPath x i) (λ x → Index.lastWitnessPath x i))
      ∙ (λ i → pack (λ x → equivFun Index.comparison (equivFun RCompose.Second.equivalence
        (RN.naturalityAt (P.AB-C-D.associate x) i))) (λ x → refl) rightPort)
      ∙ (λ i → pack (λ x → equivFun Index.comparison
        (RCompose.compositionAt (P.shortRoute x) i)) (λ x → refl) rightPort)
      ∙ (λ i → pack (λ x → equivFun Index.comparison
        (equivFun (rightChildren i) (P.shortRoute x))) (λ x → refl) rightPort)
      ∙ (λ i → pack (λ x → Outside.compositionAt (P.shortRoute x) i) (λ x → refl) rightPort)
      ∙ (λ i → pack (λ x → equivFun Outside.Combined.equivalence (P.pentagonAt x (~ i))) (λ x → refl) rightPort)
      ∙ (λ i → pack (λ x → equivFun Outside.Combined.equivalence (rightWhisker (pre x) (~ i))) (λ x → refl) rightPort)
      ∙ (λ i → pack (λ x → LastCompose.compositionAt (pre x) i) (λ x → refl) rightPort)
      ∙ (λ i → pack (λ x → equivFun (lastChildren i) (pre x)) (λ x → refl) rightPort)

    step : L.AppendData → U.AppendData
    step ih = U.pointed (λ x i → fst (fst (whole i)) x)
      (λ x i → snd (fst (whole i)) x) (λ x i → snd (whole i) x)
      where
      lowerPath : rightE ≡ leftE
      lowerPath = equivEq (funExt (L.AppendData.square ih))

      lifted : I → P.Middle₂ ≃ Normal (cons a ((u ++ v) ++ w))
      lifted i = LiftSpan.equivalence attachL (λ s → L.sourceFirst (attachR s))
        attachL (λ s → first ((u ++ v) ++ w) (attachR s))
        (idEquiv (Boundary a b)) (idEquiv (Piece a)) (lowerPath i) refl
        (funExt (λ s → L.AppendData.firstCoherence ih (attachR s) i))

      whole : rightStart ≡ pack U.W.leftFlat U.leftFirst U.leftLast
      whole = rightFactor
        ∙ (λ i → pack (λ x → equivFun (lifted i) (pre x)) (λ x → refl)
          (λ x → cong includeNormal (L.AppendData.lastCoherence ih x i)))
        ∙ sym leftFactor
        ∙ (λ i → pack U.W.leftFlat (λ x → rUnit refl i) leftPort)

  coherentAppend : {a b c d e f : K} (u : Word a b) (v : Word c d) (w : Word e f) →
    C.Words.AppendData u v w
  coherentAppend (single a) v w = C.SingleLeft.coherence a v w
  coherentAppend (cons a u) v w = Step.step a u v w (coherentAppend u v w)
