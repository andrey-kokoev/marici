{-# OPTIONS --safe --cubical --guardedness #-}
module ClosureSelectedHigherAdmissionRegression where

open import Cubical.Foundations.Prelude
open import Cubical.Data.Unit
open import Cubical.Data.Empty using (⊥)
open import Cubical.HITs.S1.Base using (S¹; base; loop; rotLoop)
open import ClosureSelectedHigherAdmission using (module Fiber)
open import ClosureRotationAdmission using (module Admission)
open import ClosureArbitrarySubtreeRotationAdmission using (module General)
open import ClosureGluingTreeRegression using (circleLoopNotRefl)

-- A genuine admitted identity edge on a circle-valued single-piece tree.
module A = Admission Unit (λ _ → S¹) (λ _ _ → S¹) (λ x → x) (λ x → x)
module E = A.Edges (A.N.single tt)
point : A.N.Bracket (A.N.single tt)
point = A.N.leaf tt
module P = E.Presentations point
module Cuts = P.Views.Cuts
module F = Fiber (Cuts.post point) (Cuts.target point) (Cuts.compatibleIsContr point)

identityEdge : E.Admitted point point
identityEdge = E.admitted (λ x → x) (λ x → refl)
identityPresentation : F.Presentation
identityPresentation = P.pack point identityEdge
module Same = F.Between identityPresentation identityPresentation

-- Both endpoint maps are already admitted, yet this selected homotopy
-- winds once when evaluated at base.
turn : (λ (x : S¹) → x) ≡ (λ x → x)
turn = funExt rotLoop
turnNotNull : turn ≡ refl → ⊥
turnNotNull equality = circleLoopNotRefl (cong (λ h i → h i base) equality)

noSelectedLift : F.Cells.Lift 1 Same.boundary turn → ⊥
noSelectedLift (α , equality) = turnNotNull
  (sym equality ∙ cong (cong fst)
    (isProp→isSet (isContr→isProp (Cuts.compatibleIsContr point))
      identityPresentation identityPresentation α refl))

noCoherence : Same.Coherence turn → ⊥
noCoherence coherence = noSelectedLift (Same.toLift turn coherence)

notGenerated : turn ≡ F.Cells.generated 1 Same.boundary → ⊥
notGenerated equality = noSelectedLift (F.Cells.fromGenerated 1 Same.boundary turn equality)

identityCoherence : Same.Coherence refl
identityCoherence = refl
identityLift : F.Cells.Lift 1 Same.boundary refl
identityLift = Same.toLift refl identityCoherence

-- The endpoint square matters: the SAME action with a different square
-- is also admitted. Now the SAME turn has a full compatible lift.
twistedEdge : E.Admitted point point
twistedEdge = E.admitted (λ x → x) rotLoop
twistedPresentation : F.Presentation
twistedPresentation = P.pack point twistedEdge
module Changed = F.Between twistedPresentation identityPresentation

turnCoherence : Changed.Coherence turn
turnCoherence i j x = rotLoop x (i ∨ j)
turnLift : twistedPresentation ≡ identityPresentation
turnLift = Changed.admit turn turnCoherence
retainsTurn : cong fst turnLift ≡ turn
retainsTurn = Changed.retainsSelected turn turnCoherence

-- Keeping the map stationary cannot erase that endpoint-square witness.
noStationaryComparison : Changed.Coherence refl → ⊥
noStationaryComparison coherence = turnNotNull coherence

-- Integration with the unrestricted subtree theorem, for arbitrary
-- pieces and attachments rather than just this circle instance.
module RootComparison (K : Type) (Piece : K → Type) (Boundary : K → K → Type)
  (attachL : {a b : K} → Boundary a b → Piece a)
  (attachR : {a b : K} → Boundary a b → Piece b) where
  module G = General K Piece Boundary attachL attachR
  open G.I.C.D.G.G.A.N

  module At {a b c d e f : K} {u : Word a b} {v : Word c d} {w : Word e f}
    (p : Bracket u) (q : Bracket v) (r : Bracket w) where
    module R = G.Rotation p q r
    module V = R.Presentations.Views.Cuts
    module H = Fiber (V.post R.Indexed.rightTree) (V.target R.Indexed.rightTree)
      (V.compatibleIsContr R.Indexed.rightTree)
    module B = H.Between (R.Presentations.pack R.Indexed.rightTree R.forward)
      (V.canonical R.Indexed.rightTree)

    selected : fst (R.Presentations.pack R.Indexed.rightTree R.forward) ≡
      fst (V.canonical R.Indexed.rightTree)
    selected = cong fst R.compatibleComparison

    coherence : B.Coherence selected
    coherence = B.extract R.compatibleComparison

    matchesGenerated : selected ≡ H.Cells.generated 1 B.boundary
    matchesGenerated = B.toGenerated selected coherence

    projectionRetained : cong fst (B.admit selected coherence) ≡ selected
    projectionRetained = B.retainsSelected selected coherence
