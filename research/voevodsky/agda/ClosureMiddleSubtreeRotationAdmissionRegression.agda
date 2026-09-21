{-# OPTIONS --safe --cubical --guardedness #-}
module ClosureMiddleSubtreeRotationAdmissionRegression where

open import Cubical.Foundations.Prelude
open import Cubical.Foundations.Equiv
open import Cubical.Foundations.GroupoidLaws using (cong-∙; rUnit)
open import Cubical.Data.Unit
open import Cubical.Data.Bool using (Bool; false; true)
open import Cubical.Data.Empty using (⊥)
open import Cubical.Data.Nat using (suc)
open import Cubical.Data.Nat.Properties using (max)
open import Cubical.HITs.S1.Base using (S¹; base; loop)
import Cubical.HITs.Pushout.Base as PO
open import ClosureMiddleSubtreeRotationAdmission using (module Subtrees)
open import ClosureGluingTreeRegression using (circleLoopNotRefl)
import ClosureSubtreeRotationAdmissionRegression as Fixture

module G = Subtrees Unit (λ _ → Unit) (λ _ _ → Bool) (λ _ → tt) (λ _ → tt)
module N = G.A.N

middle : N.Bracket (N.cons tt (N.single tt))
middle = N.fork (N.leaf tt) (N.leaf tt)

-- Q has two pieces and a nontrivial loop; R has nine pieces and depth eight.
-- Both are genuine subtrees of the same flattened twelve-piece word.
module R = G.LeftLeaf tt middle Fixture.tail
module E = R.E

twelvePieces : N.pieceCount R.word ≡ 12
twelvePieces = refl

leftDepth : N.depth R.leftTree ≡ 9
leftDepth = cong (λ n → suc (max 2 n)) Fixture.tailDepth

rightDepth : N.depth R.rightTree ≡ 10
rightDepth = cong (λ n → suc (suc (max 1 n))) Fixture.tailDepth

fullCompatibility : R.Presentations.pack R.rightTree R.forward ≡
  R.Presentations.Views.Cuts.canonical R.rightTree
fullCompatibility = R.compatibleComparison

reindexedCompatibility :
  R.Presentations.pack R.Indexed.rightTree R.reindexedForward ≡
  R.Presentations.Views.Cuts.canonical R.Indexed.rightTree
reindexedCompatibility = R.Presentations.agreesWithGenerated R.Indexed.rightTree R.reindexedForward

cycle : E.Route R.leftTree R.leftTree
cycle = E.step R.backward (E.step R.forward (E.stay R.leftTree))

closedTypeCycle : E.typeRoute cycle ≡ refl
closedTypeCycle = E.closedTypeRoute cycle

residualIdentity : (x : N.Realize R.leftTree) → transport (E.typeRoute cycle) x ≡ x
residualIdentity = E.residualIsIdentity cycle

includeMiddle : N.Realize middle → R.Nat.Source.Left
includeMiddle x = PO.inl (PO.inr x)

middleLoop : Path R.Nat.Source.Left (includeMiddle (PO.inl tt)) (includeMiddle (PO.inl tt))
middleLoop = cong includeMiddle (PO.push false ∙ sym (PO.push true))

middleDetector : N.Realize middle → S¹
middleDetector (PO.inl tt) = base
middleDetector (PO.inr tt) = base
middleDetector (PO.push false i) = loop i
middleDetector (PO.push true i) = base

detectMiddle : R.Nat.Source.Right → S¹
detectMiddle (PO.inl tt) = base
detectMiddle (PO.inr (PO.inl x)) = middleDetector x
detectMiddle (PO.inr (PO.inr _)) = base
detectMiddle (PO.inr (PO.push b i)) = base
detectMiddle (PO.push b i) = base

middleRetained : cong (λ x → detectMiddle (R.Nat.Source.associate x)) middleLoop ≡ loop
middleRetained = cong-∙ (λ x → detectMiddle (R.Nat.Source.associate (includeMiddle x)))
  (PO.push false) (sym (PO.push true)) ∙ sym (rUnit loop)

noMiddleCollapse : cong R.Nat.Source.associate middleLoop ≡ refl → ⊥
noMiddleCollapse h = circleLoopNotRefl (sym middleRetained ∙ cong (cong detectMiddle) h)

tailLoop : Path R.Nat.Source.Left
  (PO.inr (N.firstAt Fixture.tail tt)) (PO.inr (N.firstAt Fixture.tail tt))
tailLoop i = PO.inr (Fixture.innerLoop i)

detectTail : R.Nat.Source.Right → S¹
detectTail (PO.inl tt) = base
detectTail (PO.inr (PO.inl _)) = base
detectTail (PO.inr (PO.inr x)) = Fixture.innerDetector x
detectTail (PO.inr (PO.push b i)) = sym Fixture.innerFirst i
detectTail (PO.push b i) = base

tailRetained : PathP (λ i → Fixture.innerFirst i ≡ Fixture.innerFirst i)
  (cong (λ x → detectTail (R.Nat.Source.associate x)) tailLoop) loop
tailRetained = Fixture.innerDetected

noTailCollapse : cong R.Nat.Source.associate tailLoop ≡ refl → ⊥
noTailCollapse h = circleLoopNotRefl
  (sym (fromPathP tailRetained)
    ∙ cong (transport (λ i → Fixture.innerFirst i ≡ Fixture.innerFirst i)) (cong (cong detectTail) h)
    ∙ fromPathP (λ i → refl {x = Fixture.innerFirst i}))

-- The two detectors separate the two internal contributions.
middleInvisibleToTail : cong (λ x → detectTail (R.Nat.Source.associate x)) middleLoop ≡ refl
middleInvisibleToTail = refl

tailInvisibleToMiddle : cong (λ x → detectMiddle (R.Nat.Source.associate x)) tailLoop ≡ refl
tailInvisibleToMiddle = refl

-- The new theorem also compares with the earlier arbitrary-right-subtree
-- admission on their common specialization, including its square witness.
module Specialization = G.LeftLeaf tt (N.leaf tt) Fixture.tail

agreesWithEarlierRightCase :
  Specialization.Presentations.pack Specialization.rightTree Specialization.forward ≡
  Specialization.Presentations.pack Specialization.rightTree Fixture.R.forward
agreesWithEarlierRightCase = Specialization.Presentations.Views.Cuts.compare
  Specialization.rightTree _ _
