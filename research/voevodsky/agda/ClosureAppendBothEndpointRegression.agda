{-# OPTIONS --safe --cubical --guardedness #-}
module ClosureAppendBothEndpointRegression where

open import Cubical.Foundations.Prelude
open import Cubical.Foundations.Equiv
open import Cubical.Data.Unit
open import Cubical.Data.Empty using (⊥)
open import Cubical.HITs.S1.Base using (S¹; base; loop)
import Cubical.HITs.Pushout.Base as PO
open import ClosureAppendEndpointErasure using (module Erasure)
open import ClosurePushoutMovingPortCoherence using (module MovingRight)
open import ClosureGluingTreeRegression using (circleLoopNotRefl)

module G = Erasure Unit (λ _ → S¹) (λ _ _ → Unit) (λ _ → base) (λ _ → base)
open G.Old.C.D.G.G.A.N

pairWord : Word tt tt
pairWord = cons tt (single tt)
pair : Bracket pairWord
pair = fork (leaf tt) (leaf tt)
module W = G.New.C.Words pairWord (single tt) (single tt)
module T = G.New.C.D.Trees pair (leaf tt) (leaf tt)

abstract
  both : W.AppendData
  both = G.New.coherentAppend pairWord (single tt) (single tt)

firstEndpoint : (x : S¹) →
  PathP (λ i → W.AppendData.square both (W.sourceFirst x) i ≡ first ((pairWord ++ single tt) ++ single tt) x)
    (W.rightFirst x) (W.leftFirst x)
firstEndpoint = W.AppendData.firstCoherence both
lastEndpoint : (x : S¹) →
  PathP (λ i → W.AppendData.square both (W.sourceLast x) i ≡ last ((pairWord ++ single tt) ++ single tt) x)
    (W.rightLast x) (W.leftLast x)
lastEndpoint = W.AppendData.lastCoherence both

fourPieces : pieceCount ((pairWord ++ single tt) ++ single tt) ≡ 4
fourPieces = refl

-- The stronger word proof still admits the ACTUAL reindexed tree rotation.
module E = T.Indexed.E
edge : E.Admitted T.Indexed.leftTree T.Indexed.rightTree
edge = T.admit (W.AppendData.square both)
retainsNative : E.actionEquiv edge ≡ T.Indexed.nativeEquivalence
retainsNative = equivEq refl
module P = E.Presentations T.Indexed.leftTree
fullComparison : P.pack T.Indexed.rightTree edge ≡ P.Views.Cuts.canonical T.Indexed.rightTree
fullComparison = P.agreesWithGenerated T.Indexed.rightTree edge

attachmentNotEquivalence : isEquiv (λ (_ : Unit) → base) → ⊥
attachmentNotEquivalence proof = circleLoopNotRefl
  (isProp→isSet (isContr→isProp (base , secEq ((λ _ → base) , proof))) base base loop refl)

-- Simultaneously move the attachment family, the endpoint, and its
-- source-side port path. Neither loop is silently replaced by reflexivity.
constant : Unit → S¹
constant _ = base
module M = MovingRight constant

diagramLoop : Path M.T.Diagram (S¹ , constant) (S¹ , constant)
diagramLoop i = S¹ , (λ _ → loop i)
endpointLoop : PathP (λ i → fst (diagramLoop i)) base base
endpointLoop = loop

movingEndpoint : M.MovingSquare diagramLoop endpointLoop
movingEndpoint = M.movingSquare diagramLoop endpointLoop
movingSourcePort : M.PortSquare diagramLoop loop endpointLoop
movingSourcePort = M.sourcePort diagramLoop loop endpointLoop
endpointNotNull : endpointLoop ≡ refl → ⊥
endpointNotNull = circleLoopNotRefl

-- Abstracting a completed proof does not erase or supply either field.
-- No transfer of these port cells to arbitrary tree ports is asserted here.
