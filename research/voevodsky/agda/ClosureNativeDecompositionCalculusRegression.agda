{-# OPTIONS --safe --cubical --guardedness #-}
module ClosureNativeDecompositionCalculusRegression where

open import Cubical.Foundations.Prelude
open import Cubical.Foundations.Equiv
open import Cubical.Data.Unit
open import Cubical.Data.Bool.Base using (Bool; false; true)
open import Cubical.Data.Empty using (⊥)
open import Cubical.HITs.S1.Base using (S¹; base; loop)
import Cubical.HITs.Pushout.Base as PO
open import ClosureNativeDecompositionCalculus using (module Calculus)
open import ClosureNativeSubtreeContextAdmission using (module Native)
open import ClosureTreeBoundarySemantics using (module Semantics)
open import ClosureTreePolarizedSemantics using (module Polarized)
open import ClosureGluingTreeRegression using (circleLoopNotRefl)

module G = Calculus Unit (λ _ → S¹) (λ _ _ → Unit) (λ _ → base) (λ _ → base)
  using (module C; module O; Move; rotate; onLeft; onRight; Route; done; step;
    append; evaluate; run; run-append; observe; observe-compose; normal-naturality; admit)
open G.C.C.A.N
private
  module NativeModel = Native Unit (λ _ → S¹) (λ _ _ → Unit) (λ _ → base) (λ _ → base)
    using (module Trees)
module Root = NativeModel.Trees (leaf tt) (leaf tt) (leaf tt) using (module R)

triple : Word tt tt
triple = cons tt (cons tt (single tt))
leftRoot rightRoot : Bracket triple
leftRoot = Root.R.leftTree
rightRoot = Root.R.rightTree
source middle target : Bracket (triple ++ triple)
source = fork leftRoot leftRoot
middle = fork rightRoot leftRoot
target = fork rightRoot rightRoot

leftMove : G.Move source middle
leftMove = G.onLeft (G.rotate (leaf tt) (leaf tt) (leaf tt)) leftRoot
rightMove : G.Move middle target
rightMove = G.onRight rightRoot (G.rotate (leaf tt) (leaf tt) (leaf tt))
firstRoute : G.Route source middle
firstRoute = G.step leftMove (G.done source)
secondRoute : G.Route middle target
secondRoute = G.step rightMove (G.done middle)
route : G.Route source target
route = G.append firstRoute secondRoute

sixPieces : pieceCount (triple ++ triple) ≡ 6
sixPieces = refl
leftAction : (x : Realize leftRoot) → G.run route (PO.inl x) ≡
  PO.inl (equivFun Root.R.nativeEquivalence x)
leftAction x = refl
rightAction : (x : Realize leftRoot) → G.run route (PO.inr x) ≡
  PO.inr (equivFun Root.R.nativeEquivalence x)
rightAction x = refl

-- BOTH higher endpoint fields survive sequential contextual moves.
firstCell : G.C.C.Ports.FirstCoherence (G.C.Coherent.base (G.evaluate route))
  (G.C.Coherent.firstPort (G.evaluate route))
firstCell = G.C.Coherent.firstSquare (G.evaluate route)
lastCell : G.C.C.Ports.LastCoherence (G.C.Coherent.base (G.evaluate route))
  (G.C.Coherent.lastPort (G.evaluate route))
lastCell = G.C.Coherent.lastSquare (G.evaluate route)

observationsCompose : (d : G.O.Local target S¹) →
  G.observe firstRoute (G.observe secondRoute d) ≡ G.observe route d
observationsCompose = G.observe-compose firstRoute secondRoute

module E = G.C.C.A.Edges (triple ++ triple)
module P = E.Presentations source
fullComparison : P.pack target (G.admit route) ≡ P.Views.Cuts.canonical target
fullComparison = P.agreesWithGenerated target (G.admit route)

-- A two-attachment seam probe. Leaf readouts agree, but one of the
-- attachment paths is the circle generator. Assembly must retain it.
module B = Semantics Unit (λ _ → Unit) (λ _ _ → Bool) (λ _ → tt) (λ _ → tt)
  using (module N; Local; assemble; restrict; assemble-restrict; restrict-assemble; localPaths)
seamTree : B.N.Bracket (B.N.cons tt (B.N.single tt))
seamTree = B.N.fork (B.N.leaf tt) (B.N.leaf tt)
seam : (s : Bool) → base ≡ base
seam false = refl
seam true = loop
packet : B.Local seamTree S¹
packet = (λ _ → base) , (λ _ → base) , seam
seamRetained : cong (B.assemble seamTree packet) (PO.push true) ≡ loop
seamRetained = refl
seamNotErased : cong (B.assemble seamTree packet) (PO.push true) ≡ refl → ⊥
seamNotErased h = circleLoopNotRefl (sym seamRetained ∙ h)
packetRoundtrip : B.restrict seamTree (B.assemble seamTree packet) ≡ packet
packetRoundtrip = B.restrict-assemble seamTree packet

module Q = Polarized Unit (λ _ → Unit) (λ _ _ → Bool) (λ _ → tt) (λ _ → tt)
  using (module At)
module TwoSlots = Q.At seamTree S¹
polarizedRoundtrip : (F : B.N.Realize seamTree → B.N.Realize seamTree → S¹) →
  TwoSlots.assemble (TwoSlots.restrict F) ≡ F
polarizedRoundtrip = TwoSlots.assemble-restrict
