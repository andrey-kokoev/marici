{-# OPTIONS --safe --cubical --guardedness #-}
module ClosureFiniteGluingNormalizationRegression where

open import Cubical.Foundations.Prelude
open import Cubical.Foundations.Equiv
open import Cubical.Foundations.GroupoidLaws using (cong-∙; rUnit)
open import Cubical.Data.Nat using (ℕ; zero; suc)
open import Cubical.Data.Unit
open import Cubical.Data.Bool using (Bool; false; true)
open import Cubical.Data.Empty using (⊥)
open import Cubical.HITs.S1.Base using (S¹; base; loop)
import Cubical.HITs.Pushout.Base as PO
open import ClosureFiniteGluingNormalization using (module System)
open import ClosureGluingTreeRegression using (circleLoopNotRefl)
-- Keep the explicit pentagon and earlier regressions in the checked closure.
import ClosureGluingPentagonRegression

module N = System Unit (λ _ → Unit) (λ _ _ → Bool) (λ _ → tt) (λ _ → tt)

word : ℕ → N.Word tt tt
word zero = N.single tt
word (suc n) = N._++_ (word n) (N.single tt)

leftChain : (n : ℕ) → N.Bracket (word n)
leftChain zero = N.leaf tt
leftChain (suc n) = N.fork (leftChain n) (N.leaf tt)

quad : N.Bracket (word 3)
quad = N.fork (N.fork (N.leaf tt) (N.leaf tt)) (N.fork (N.leaf tt) (N.leaf tt))

left right balanced : N.Bracket (word 8)
left = leftChain 8
right = N.rightBracket (word 8)
balanced = N.fork (N.fork quad quad) (N.leaf tt)

ninePieces : N.pieceCount (word 8) ≡ 9
ninePieces = refl

leftDepth : N.depth left ≡ 8
leftDepth = refl
rightDepth : N.depth right ≡ 8
rightDepth = refl
balancedDepth : N.depth balanced ≡ 4
balancedDepth = refl

-- Nine pieces, eight attachment boundaries: three genuinely different
-- bracketings share a DERIVED common normal frame.
module C = N.Comparisons (word 8)

cycle : C.Views.Cuts.Route left left
cycle = C.Views.Cuts.step left (C.Views.Cuts.step balanced
  (C.Views.Cuts.step right (C.Views.Cuts.stay left)))

allValuesReturn : (x : N.Realize left) → C.run cycle x ≡ x
allValuesReturn = C.cycleReturns cycle

typedOperationCycle : C.Views.closedCycle cycle (C.Views.Cuts.canonical left) ≡ refl
typedOperationCycle = C.Views.closedCycleIsTrivial cycle (C.Views.Cuts.canonical left)

-- Detect a real loop at the first boundary of the nine-piece normal form.
normalLoop : Path (N.Normal (word 8)) (PO.inl tt) (PO.inl tt)
normalLoop = PO.push false ∙ sym (PO.push true)

detect : N.Normal (word 8) → S¹
detect (PO.inl tt) = base
detect (PO.inr _) = base
detect (PO.push false i) = loop i
detect (PO.push true i) = base

normalLoopDetected : cong detect normalLoop ≡ loop
normalLoopDetected = cong-∙ detect (PO.push false) (sym (PO.push true)) ∙ sym (rUnit loop)

normalLoopNontrivial : normalLoop ≡ refl → ⊥
normalLoopNontrivial h = circleLoopNotRefl
  (sym normalLoopDetected ∙ cong (cong detect) h)

leftPoint : N.Realize left
leftPoint = N.firstAt left tt

-- Pull the detected loop back through the proved equivalence on path spaces.
-- This is explicitly a pulled-back loop, not a claimed computation of an
-- independently chosen source attachment expression.
leftLoop : leftPoint ≡ leftPoint
leftLoop = invEq (N.normalizedPaths left) normalLoop

leftLoopImage : cong (equivFun (N.normalize left)) leftLoop ≡ normalLoop
leftLoopImage = secEq (N.normalizedPaths left) normalLoop

leftLoopNontrivial : leftLoop ≡ refl → ⊥
leftLoopNontrivial h = normalLoopNontrivial
  (sym leftLoopImage ∙ cong (cong (equivFun (N.normalize left))) h)

-- The generated cycle returns the loop coherently, allowing its basepoint
-- to follow the already proved return path instead of assuming strict return.
loopReturns : PathP (λ i → allValuesReturn leftPoint i ≡ allValuesReturn leftPoint i)
  (cong (C.run cycle) leftLoop) leftLoop
loopReturns i j = allValuesReturn (leftLoop j) i

-- An actual operation between chains of DIFFERENT lengths, not just a
-- rebracketing identity: retain the first attachment pair, collapse the rest.
collapse : N.Normal (word 8) → N.Normal (word 1)
collapse (PO.inl tt) = PO.inl tt
collapse (PO.inr _) = PO.inr tt
collapse (PO.push b i) = PO.push b i

module Operation = N.Operations (word 8) (word 1) collapse

outputTree : N.Bracket (word 1)
outputTree = N.rightBracket (word 1)

operationSquare : (x : N.Realize left) →
  equivFun (N.normalize outputTree) (Operation.Views.view (left , outputTree) x) ≡
  collapse (equivFun (N.normalize left) x)
operationSquare x = secEq (N.normalize outputTree)
  (collapse (equivFun (N.normalize left) x))
