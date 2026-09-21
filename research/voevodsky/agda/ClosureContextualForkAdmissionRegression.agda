{-# OPTIONS --safe --cubical --guardedness #-}
module ClosureContextualForkAdmissionRegression where

open import Cubical.Foundations.Prelude
open import Cubical.Foundations.Equiv
open import Cubical.Foundations.GroupoidLaws using (rUnit; lUnit; cong-∙)
open import Cubical.Foundations.Path using (compPath→Square; Square→compPath)
open import Cubical.Data.Unit
open import Cubical.Data.Empty using (⊥)
open import Cubical.HITs.S1.Base using (S¹; base; loop; rotLoop)
import Cubical.HITs.Pushout.Base as PO
open import ClosureContextualForkAdmission using (module Contextual)
open import ClosureGluingTreeRegression using (circleLoopNotRefl)

module C = Contextual Unit (λ _ → S¹) (λ _ _ → Unit) (λ _ → base) (λ _ → base)
open C.A.N

point : Bracket (single tt)
point = leaf tt

-- An actual identity equivalence with a nontrivial normalization path.
-- Its attachment witness must move with that path.
turn : C.Change point point
turn = C.change (idEquiv S¹) (equivEq (funExt rotLoop))

port : C.Ports.Last turn
port = rotLoop
coherence : C.Ports.LastCoherence turn port
coherence x = compPath→Square (rUnit (rotLoop x ∙ refl))
firstCoherence : C.Ports.FirstCoherence turn port
firstCoherence = coherence

module Left = C.UnderLeft point turn port coherence
module Right = C.UnderRight point turn port firstCoherence

attachmentNotEquivalence : isEquiv (λ (_ : Unit) → base) → ⊥
attachmentNotEquivalence proof = circleLoopNotRefl
  (isProp→isSet (isContr→isProp (base , secEq ((λ _ → base) , proof))) base base loop refl)

-- Dropping the port witness while keeping the normalization path is invalid.
noReflexivePort : C.Ports.LastCoherence turn (λ x → refl) → ⊥
noReflexivePort claimed = circleLoopNotRefl
  (rUnit loop ∙ Square→compPath (claimed base)
    ∙ sym (rUnit (refl ∙ refl)) ∙ sym (rUnit refl))

leftDetector rightDetector : Normal (cons tt (single tt)) → S¹
leftDetector (PO.inl x) = x
leftDetector (PO.inr _) = base
leftDetector (PO.push tt i) = base
rightDetector (PO.inl _) = base
rightDetector (PO.inr x) = x
rightDetector (PO.push tt i) = base

-- The parent normalization squares retain the nontrivial chosen data.
leftSquareDetected : cong leftDetector (Left.square (PO.inl base)) ≡ loop
leftSquareDetected = cong-∙ leftDetector refl (λ i → PO.inl (loop i)) ∙ sym (lUnit loop)
rightSquareDetected : cong rightDetector (Right.square (PO.inr base)) ≡ loop
rightSquareDetected = cong-∙ rightDetector refl (λ i → PO.inr (loop i)) ∙ sym (lUnit loop)

leftSquareNotNull : Left.square (PO.inl base) ≡ refl → ⊥
leftSquareNotNull h = circleLoopNotRefl (sym leftSquareDetected ∙ cong (cong leftDetector) h)
rightSquareNotNull : Right.square (PO.inr base) ≡ refl → ⊥
rightSquareNotNull h = circleLoopNotRefl (sym rightSquareDetected ∙ cong (cong rightDetector) h)

-- Neither direction requires the unchanged sibling to be a leaf.
module AnySibling {a b : Unit} {w : Word a b} (sibling : Bracket w) where
  module L = C.UnderLeft sibling turn port coherence
  module R = C.UnderRight sibling turn port firstCoherence

  leftAdmission : C.A.Edges.Admitted (single tt ++ w) (fork point sibling) (fork point sibling)
  leftAdmission = L.admitted
  rightAdmission : C.A.Edges.Admitted (w ++ single tt) (fork sibling point) (fork sibling point)
  rightAdmission = R.admitted

  leftRetained : C.A.Edges.actionEquiv (single tt ++ w) leftAdmission ≡ L.C.First.equivalence
  leftRetained = L.retainsComparison
  rightRetained : C.A.Edges.actionEquiv (w ++ single tt) rightAdmission ≡ R.C.First.equivalence
  rightRetained = R.retainsComparison
