{-# OPTIONS --safe --cubical --guardedness #-}
module ClosureRotationAppendReductionRegression where

open import Cubical.Foundations.Prelude
open import Cubical.Foundations.Equiv
open import Cubical.Data.Unit
open import Cubical.Data.Bool using (Bool)
open import Cubical.Data.Empty using (⊥)
open import Cubical.HITs.S1.Base using (S¹; base; loop)
open import ClosureGluingTreeRegression using (circleLoopNotRefl)
open import ClosureGeneralSpanCoherence using (module Composition)
open import ClosureRotationAppendReduction using (module Reduction)
import ClosureMiddleSubtreeRotationAdmissionRegression as Previous
import ClosureSubtreeRotationAdmissionRegression as Fixture

module G = Reduction Unit (λ _ → Unit) (λ _ _ → Bool) (λ _ → tt) (λ _ → tt)
module N = G.G.G.A.N
module Rebuilt = G.LeftLeaf tt Previous.middle Fixture.tail
module T = Rebuilt.T
module P = T.Indexed.E.Presentations T.Indexed.leftTree

-- An independent derivation: the reduction's singleton word base does not
-- use the earlier middle-subtree theorem.
agreesWithPrevious : P.pack T.Indexed.rightTree Rebuilt.forward ≡
  P.pack T.Indexed.rightTree Previous.R.reindexedForward
agreesWithPrevious = P.Views.Cuts.compare T.Indexed.rightTree _ _

-- Also exercise the converse transfer of square data, without asserting
-- that square witnesses for a fixed function are proof-irrelevant.
recoveredWordSquare : T.W.AppendSquare
recoveredWordSquare = T.recoverAppendSquare Previous.R.reindexedSquare

recoveredAdmission : T.Indexed.E.Admitted T.Indexed.leftTree T.Indexed.rightTree
recoveredAdmission = T.admit recoveredWordSquare

recoveredCompatibility : P.pack T.Indexed.rightTree recoveredAdmission ≡
  P.Views.Cuts.canonical T.Indexed.rightTree
recoveredCompatibility = P.agreesWithGenerated T.Indexed.rightTree recoveredAdmission

-- All three subtrees here are non-leaves. Only the factorization is tested:
-- the missing word-induction step is NOT assumed to supply an admission.
module Unrestricted = G.Trees Previous.middle Previous.middle Fixture.tail

leftFactored : equivFun (N.normalize Unrestricted.Indexed.leftTree) ≡
  (λ x → Unrestricted.W.leftFlat (equivFun Unrestricted.Nat.Left.equivalence x))
leftFactored = Unrestricted.leftToForm

rightFactored : equivFun (N.normalize Unrestricted.Indexed.nativeRight) ≡
  (λ x → Unrestricted.W.rightFlat (equivFun Unrestricted.Nat.Right.equivalence x))
rightFactored = Unrestricted.rightToForm

-- The general composition law also works with nontrivial attachment-square
-- witnesses, not just the unit-valued fixture's endpoint corrections.
constant : Unit → S¹
constant _ = base

twist : constant ≡ constant
twist i _ = loop i

twistNotRefl : twist ≡ refl → ⊥
twistNotRefl h = circleLoopNotRefl (cong (λ p i → p i tt) h)

module Twisted = Composition constant constant constant constant constant constant
  (idEquiv S¹) (idEquiv S¹) (idEquiv S¹) (idEquiv S¹)
  twist refl refl twist

twistedComposition : compEquiv Twisted.First.equivalence Twisted.Second.equivalence ≡
  Twisted.Combined.equivalence
twistedComposition = Twisted.compositionEquivalence
