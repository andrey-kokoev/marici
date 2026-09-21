{-# OPTIONS --safe --cubical --guardedness #-}
module ClosureEndpointRotationAdmissionRegression where

open import Cubical.Foundations.Prelude
open import Cubical.Foundations.Equiv
open import Cubical.Foundations.Equiv.Properties using (congEquiv)
open import Cubical.Data.Unit
open import Cubical.Data.Empty using (⊥)
open import Cubical.HITs.S1.Base using (S¹; base; loop)
open import ClosureGluingTreeRegression using (circleLoopNotRefl)
open import ClosureEndpointRotationAdmission using (module Endpoint)
import ClosureRotationAppendReductionRegression
import ClosureMiddleSubtreeRotationAdmissionRegression as Previous

-- Circle-valued identity spans, not contractible point pieces.
module G = Endpoint Unit (λ _ → S¹) (λ _ _ → S¹) (λ x → x) (λ x → x)
module N = G.G.G.A.N
module Legs = G.InvertibleLeft (idIsEquiv S¹)

pair : N.Bracket (N.cons tt (N.single tt))
pair = N.fork (N.leaf tt) (N.leaf tt)
quad : N.Bracket (N.cons tt (N.cons tt (N.cons tt (N.single tt))))
quad = N.fork pair pair

-- Four pieces on the left, two in the middle, four on the right.
module R = G.Rotation quad pair quad
module Admitted = R.WithLastEquivalence (Legs.lastIsEquiv R.Indexed.leftTree)
module E = R.E
module P = E.Presentations R.Indexed.leftTree

fullCompatibility : P.pack R.Indexed.rightTree Admitted.forward ≡
  P.Views.Cuts.canonical R.Indexed.rightTree
fullCompatibility = P.agreesWithGenerated R.Indexed.rightTree Admitted.forward

nativeEquivalenceRetained : E.actionEquiv Admitted.forward ≡ R.Indexed.nativeEquivalence
nativeEquivalenceRetained = equivEq refl

cycle : E.Route R.Indexed.leftTree R.Indexed.leftTree
cycle = E.step Admitted.backward (E.step Admitted.forward (E.stay R.Indexed.leftTree))

closedTypeCycle : E.typeRoute cycle ≡ refl
closedTypeCycle = E.closedTypeRoute cycle

residualIdentity : (x : N.Realize R.Indexed.leftTree) → transport (E.typeRoute cycle) x ≡ x
residualIdentity = E.residualIsIdentity cycle

-- The final-piece circle loop remains nontrivial after native reindexing.
loopFrame : S¹ ≃ N.Realize R.Indexed.rightTree
loopFrame = compEquiv Admitted.lastFrame R.Indexed.nativeEquivalence

noLoopCollapse : cong (equivFun loopFrame) loop ≡ refl → ⊥
noLoopCollapse h = circleLoopNotRefl
  (sym (retEq (congEquiv loopFrame) loop)
    ∙ cong (invEq (congEquiv loopFrame)) h ∙ retEq (congEquiv loopFrame) refl)

-- The restricted endpoint criterion cannot be used to smuggle admission
-- into the earlier noninvertible Bool->Unit example.
noLastEquivalence : isEquiv (Previous.N.lastAt Previous.R.leftTree) → ⊥
noLastEquivalence proof = Previous.noMiddleCollapse
  (cong (cong Previous.R.Nat.Source.associate)
    (isProp→isSet (isContr→isProp contracted) _ _ Previous.middleLoop refl))
  where
  lastFrame : Unit ≃ Previous.N.Realize Previous.R.leftTree
  lastFrame = Previous.N.lastAt Previous.R.leftTree , proof

  contracted : isContr (Previous.N.Realize Previous.R.leftTree)
  contracted = equivFun lastFrame tt , λ x →
    cong (equivFun lastFrame) (snd isContrUnit (invEq lastFrame x)) ∙ secEq lastFrame x
