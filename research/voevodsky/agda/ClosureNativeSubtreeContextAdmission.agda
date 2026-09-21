{-# OPTIONS --safe --cubical --guardedness #-}
module ClosureNativeSubtreeContextAdmission where

open import Cubical.Foundations.Prelude
open import Cubical.Foundations.Equiv
open import Cubical.Foundations.GroupoidLaws using (cong-∙; assoc)
open import Cubical.Data.Sigma.Base using (_×_)
import Cubical.HITs.Pushout.Base as PO
open import ClosureAppendBothEndpointInduction using (module Induction)
open import ClosureRotationIndexPortCoherence using (module IndexPorts)
open import ClosureSubtreeAppendPortCoherence using (module SubtreePorts)
open import ClosureCoherentContextAdmission using (module Contexts)

-- Distribute a mapped composite while retaining the chosen final port.
distribute : {A B : Type} (f : A → B) {x y z : A} {t : B}
  (p : x ≡ y) (q : y ≡ z) (r : f z ≡ t) →
  cong f (p ∙ q) ∙ r ≡ cong f p ∙ (cong f q ∙ r)
distribute f p q r = cong (λ s → s ∙ r) (cong-∙ f p q)
  ∙ sym (assoc (cong f p) (cong f q) r)

module Native (K : Type) (Piece : K → Type) (Boundary : K → K → Type)
  (attachL : {a b : K} → Boundary a b → Piece a)
  (attachR : {a b : K} → Boundary a b → Piece b) where
  private
    module I = Induction K Piece Boundary attachL attachR
    module J = IndexPorts K Piece Boundary attachL attachR
    module S = SubtreePorts K Piece Boundary attachL attachR
  module C = Contexts K Piece Boundary attachL attachR
  open I.C.D.G.G.A.N

  module Trees {a b c d e f : K}
    {u : Word a b} {v : Word c d} {w : Word e f}
    (p : Bracket u) (q : Bracket v) (r : Bracket w) where
    private
      module P = J.Trees p q r
      module M = S.Trees p q r
      module T = M.T
      module W = M.W
      module Data = M.Transfer (I.coherentAppend u v w)
    module R = T.Indexed

    Pointed : Type
    Pointed = Σ[ F ∈ (Realize R.leftTree → Normal ((u ++ v) ++ w)) ]
      (((x : Piece a) → F (firstAt R.leftTree x) ≡ first ((u ++ v) ++ w) x) ×
       ((x : Piece f) → F (lastAt R.leftTree x) ≡ last ((u ++ v) ++ w) x))

    start indexed rightForm leftForm finish : Pointed
    start = (λ x → equivFun (normalize R.rightTree) (equivFun R.nativeEquivalence x)) ,
      P.First.after , P.Last.after
    indexed = (λ x → T.W.returnIndex (equivFun (normalize R.nativeRight) (R.Raw.associate x))) ,
      P.First.before , P.Last.before
    rightForm = M.rightForm , M.firstRight , M.lastRight
    leftForm = M.leftForm , M.firstLeft , M.lastLeft
    finish = equivFun (normalize R.leftTree) , normalizeFirst R.leftTree , normalizeLast R.leftTree

    reindex : start ≡ indexed
    reindex i = (λ x → P.reindexSquare x i) ,
      (λ x → P.First.coherence x i) , (λ x → P.Last.coherence x i)

    firstLeftAdjustment : (x : Piece a) → normalizeFirst R.leftTree x ≡ M.firstLeft x
    firstLeftAdjustment x = distribute
      (λ z → equivFun (appendFrame (u ++ v) w) (PO.inl z))
      (cong (λ z → equivFun (appendFrame u v) (PO.inl z)) (normalizeFirst p x))
      (appendFirst u v x) (appendFirst (u ++ v) w x)

    firstRightAdjustment : (x : Piece a) → P.First.before x ≡ M.firstRight x
    firstRightAdjustment x = distribute T.W.returnIndex
      (cong (λ z → equivFun (appendFrame u (v ++ w)) (PO.inl z)) (normalizeFirst p x))
      (appendFirst u (v ++ w) x)
      (fromPathP (λ i → first (sym R.association i) x))

    lastRightAdjustment : (x : Piece f) → P.Last.before x ≡ M.lastRight x
    lastRightAdjustment x =
      cong (λ h → cong T.W.returnIndex h ∙ fromPathP (λ i → last (sym R.association i) x))
        (distribute outer
          (cong inner (normalizeLast r x)) (appendLast v w x) (appendLast u (v ++ w) x))
      ∙ distribute T.W.returnIndex
          (cong (λ z → outer (inner z)) (normalizeLast r x))
          (cong outer (appendLast v w x) ∙ appendLast u (v ++ w) x)
          (fromPathP (λ i → last (sym R.association i) x))
      where
      inner : Normal w → Normal (v ++ w)
      inner z = equivFun (appendFrame v w) (PO.inr z)
      outer : Normal (v ++ w) → Normal (u ++ (v ++ w))
      outer z = equivFun (appendFrame u (v ++ w)) (PO.inr z)

    leftFactor : finish ≡ leftForm
    leftFactor =
      (λ i → (λ x → equivFun (appendFrame (u ++ v) w) (equivFun (T.leftChildren (~ i)) x)) ,
        normalizeFirst R.leftTree , normalizeLast R.leftTree)
      ∙ (λ i → (λ x → equivFun (appendFrame (u ++ v) w) (T.LC.compositionAt x (~ i))) ,
        normalizeFirst R.leftTree , normalizeLast R.leftTree)
      ∙ (λ i → M.leftForm , (λ x → firstLeftAdjustment x i) , M.lastLeft)

    rightFactor : indexed ≡ rightForm
    rightFactor =
      (λ i → (λ x → T.W.returnIndex (equivFun (appendFrame u (v ++ w))
        (equivFun (T.rightChildren (~ i)) (R.Raw.associate x)))) , P.First.before , P.Last.before)
      ∙ (λ i → (λ x → T.W.returnIndex (equivFun (appendFrame u (v ++ w))
        (T.RC.compositionAt (R.Raw.associate x) (~ i)))) , P.First.before , P.Last.before)
      ∙ (λ i → (λ x → T.W.returnIndex (T.W.rightFlat (T.Nat.naturalityAt x (~ i)))) ,
        P.First.before , P.Last.before)
      ∙ (λ i → M.rightForm , (λ x → firstRightAdjustment x i) , (λ x → lastRightAdjustment x i))

    wordStep : rightForm ≡ leftForm
    wordStep i = (λ x → Data.square x i) ,
      (λ x → Data.firstCoherence x i) , (λ x → Data.lastCoherence x i)

    abstract
      whole : start ≡ finish
      whole = reindex ∙ rightFactor ∙ wordStep ∙ sym leftFactor

    change : C.C.Change R.leftTree R.rightTree
    change = C.C.change R.nativeEquivalence (equivEq (λ i → fst (whole i)))

    firstPort : C.C.Ports.First change
    firstPort = P.First.port
    lastPort : C.C.Ports.Last change
    lastPort = P.Last.port
    firstCoherence : C.C.Ports.FirstCoherence change firstPort
    firstCoherence x i = fst (snd (whole i)) x
    lastCoherence : C.C.Ports.LastCoherence change lastPort
    lastCoherence x i = snd (snd (whole i)) x

    coherent : C.Coherent R.leftTree R.rightTree
    coherent = C.coherent change firstPort lastPort firstCoherence lastCoherence

    module Hole = C.InHole ((u ++ v) ++ w)
    contextual : {g h : K} {z : Word g h} (context : Hole.Context z) →
      C.C.A.Edges.Admitted z (Hole.plug context R.leftTree) (Hole.plug context R.rightTree)
    contextual context = Hole.admitted context coherent

-- The square is constructed in the full paired-port state. It is not
-- asserted equal to the earlier unpointed T.rotationSquare. Its frame and
-- both ports are the actual native reindexed rotation and its tree paths.
