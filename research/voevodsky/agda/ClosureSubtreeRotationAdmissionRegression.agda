{-# OPTIONS --safe --cubical --guardedness #-}
module ClosureSubtreeRotationAdmissionRegression where

open import Cubical.Foundations.Prelude
open import Cubical.Foundations.Equiv
open import Cubical.Foundations.GroupoidLaws using (cong-∙; rUnit)
open import Cubical.Data.Unit
open import Cubical.Data.Nat using (suc)
open import Cubical.Data.Nat.Properties using (max)
open import Cubical.Data.Bool using (Bool; false; true)
open import Cubical.Data.Empty using (⊥)
open import Cubical.HITs.S1.Base using (S¹; base; loop)
import Cubical.HITs.Pushout.Base as PO
open import ClosureSubtreeRotationAdmission using (module Subtrees)
open import ClosureGluingTreeRegression using (circleLoopNotRefl)
import ClosureFiniteGluingNormalizationRegression as Previous
import ClosureGeneralRotationAdmissionRegression

module G = Subtrees Unit (λ _ → Unit) (λ _ _ → Bool) (λ _ → tt) (λ _ → tt)
module N = G.G.A.N

-- Keep the checked large fixture opaque to avoid re-expanding its inverse
-- certificates at every specialization. Its word, depth, and loop data stay
-- explicit. The generic theorem still uses the flattened word normalizer.
abstract
  tail : N.Bracket (Previous.word 8)
  tail = Previous.left

  tailDepth : N.depth tail ≡ 8
  tailDepth = Previous.leftDepth

  innerLoop : N.firstAt tail tt ≡ N.firstAt tail tt
  innerLoop = Previous.leftLoop

  innerDetector : N.Realize tail → S¹
  innerDetector x = Previous.detect (equivFun (N.normalize tail) x)

  innerFirst : innerDetector (N.firstAt tail tt) ≡ base
  innerFirst = refl

  innerDetected : PathP (λ i → innerFirst i ≡ innerFirst i)
    (cong innerDetector innerLoop) loop
  innerDetected = cong (cong Previous.detect) Previous.leftLoopImage ∙ Previous.normalLoopDetected

module R = G.RightSubtree tt tt tail
module E = R.E

elevenPieces : N.pieceCount R.word ≡ 11
elevenPieces = refl
leftDepth : N.depth R.leftTree ≡ 9
leftDepth = cong (λ n → suc (max 1 n)) tailDepth
rightDepth : N.depth R.rightTree ≡ 10
rightDepth = cong (λ n → suc (suc n)) tailDepth

fullCompatibility : R.Presentations.pack R.rightTree R.forward ≡
  R.Presentations.Views.Cuts.canonical R.rightTree
fullCompatibility = R.compatibleComparison

cycle : E.Route R.leftTree R.leftTree
cycle = E.step R.backward (E.step R.forward (E.stay R.leftTree))

closedTypeCycle : E.typeRoute cycle ≡ refl
closedTypeCycle = E.closedTypeRoute cycle

residualIdentity : (x : N.Realize R.leftTree) → transport (E.typeRoute cycle) x ≡ x
residualIdentity = E.residualIsIdentity cycle

includeAB : R.Nat.Source.AB → R.Nat.Source.Left
includeAB = PO.inl

firstLoop : Path R.Nat.Source.Left (PO.inl (PO.inl tt)) (PO.inl (PO.inl tt))
firstLoop = cong includeAB (PO.push false ∙ sym (PO.push true))

secondLoop : Path R.Nat.Source.Left (PO.inl (PO.inr tt)) (PO.inl (PO.inr tt))
secondLoop = PO.push false ∙ sym (PO.push true)

detectFirst : R.Nat.Source.Right → S¹
detectFirst (PO.inl tt) = base
detectFirst (PO.inr _) = base
detectFirst (PO.push false i) = loop i
detectFirst (PO.push true i) = base

detectSecond : R.Nat.Source.Right → S¹
detectSecond (PO.inl tt) = base
detectSecond (PO.inr (PO.inl tt)) = base
detectSecond (PO.inr (PO.inr _)) = base
detectSecond (PO.inr (PO.push false i)) = loop i
detectSecond (PO.inr (PO.push true i)) = base
detectSecond (PO.push s i) = base

firstRetained : cong (λ x → detectFirst (R.Nat.Source.associate x)) firstLoop ≡ loop
firstRetained = cong-∙ (λ x → detectFirst (R.Nat.Source.associate (includeAB x)))
  (PO.push false) (sym (PO.push true)) ∙ sym (rUnit loop)

secondRetained : cong (λ x → detectSecond (R.Nat.Source.associate x)) secondLoop ≡ loop
secondRetained = cong-∙ (λ x → detectSecond (R.Nat.Source.associate x))
  (PO.push false) (sym (PO.push true)) ∙ sym (rUnit loop)

-- A third detected loop lives INSIDE the large right subtree.
tailLoop : Path R.Nat.Source.Left (PO.inr (N.firstAt tail tt)) (PO.inr (N.firstAt tail tt))
tailLoop i = PO.inr (innerLoop i)

detectTail : R.Nat.Source.Right → S¹
detectTail (PO.inl tt) = base
detectTail (PO.inr (PO.inl tt)) = base
detectTail (PO.inr (PO.inr x)) = innerDetector x
detectTail (PO.inr (PO.push b i)) = sym innerFirst i
detectTail (PO.push b i) = base

tailRetained : PathP (λ i → innerFirst i ≡ innerFirst i)
  (cong (λ x → detectTail (R.Nat.Source.associate x)) tailLoop) loop
tailRetained = innerDetected

noTailCollapse : cong R.Nat.Source.associate tailLoop ≡ refl → ⊥
noTailCollapse h = circleLoopNotRefl
  (sym (fromPathP tailRetained)
    ∙ cong (transport (λ i → innerFirst i ≡ innerFirst i)) (cong (cong detectTail) h)
    ∙ fromPathP (λ i → refl {x = innerFirst i}))

-- General three-subtree syntax/reindexing is also instantiated. No call to
-- Indexed.admit is made: its general normalization square is still open.
module Indexed = G.ReindexRotation Previous.quad Previous.quad tail

indexedNativeEquivalence : N.Realize Indexed.leftTree ≃ N.Realize Indexed.rightTree
indexedNativeEquivalence = Indexed.nativeEquivalence
