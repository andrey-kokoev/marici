{-# OPTIONS --safe --cubical --guardedness #-}
module ClosureArbitrarySubtreeRotationAdmissionRegression where

open import Cubical.Foundations.Prelude
open import Cubical.Foundations.Equiv
open import Cubical.Foundations.Equiv.Properties using (congEquiv)
open import Cubical.Foundations.Univalence using (pathToEquiv)
open import Cubical.Foundations.GroupoidLaws using (cong-∙; rUnit)
open import Cubical.Data.Unit
open import Cubical.Data.Bool using (Bool; false; true)
open import Cubical.Data.Bool.Properties using (false≢true)
open import Cubical.Data.Empty using (⊥)
open import Cubical.Data.Nat using (suc)
open import Cubical.Data.Nat.Properties using (max)
open import Cubical.HITs.S1.Base using (S¹; base; loop)
import Cubical.HITs.Pushout.Base as PO
open import ClosureGluingTreeRegression using (circleLoopNotRefl)
open import ClosureArbitrarySubtreeRotationAdmission using (module General)
open import ClosurePushoutTransportCoherence using (module FixedLeft)
import ClosureSubtreeRotationAdmissionRegression as Fixture
import ClosureEndpointRotationAdmissionRegression as Circle

module G = General Unit (λ _ → Unit) (λ _ _ → Bool) (λ _ → tt) (λ _ → tt)
module N = G.I.C.D.G.G.A.N

pair : N.Bracket (N.cons tt (N.single tt))
pair = N.fork (N.leaf tt) (N.leaf tt)
quad : N.Bracket (N.cons tt (N.cons tt (N.cons tt (N.single tt))))
quad = N.fork pair pair

-- Every slot is a genuine subtree: four, two, and nine pieces.
module R = G.Rotation quad pair Fixture.tail
module Raw = R.Indexed.Raw
module E = R.E

fifteenPieces : N.pieceCount R.word ≡ 15
fifteenPieces = refl
leftDepth : N.depth R.Indexed.leftTree ≡ 9
leftDepth = cong (λ n → suc (max 3 n)) Fixture.tailDepth
nativeRightDepth : N.depth R.Indexed.nativeRight ≡ 10
nativeRightDepth = cong (λ n → suc (max 2 (suc (max 1 n)))) Fixture.tailDepth
rightDepth : N.depth R.Indexed.rightTree ≡ 10
rightDepth = sym (λ i → N.depth (R.Indexed.treePath i)) ∙ nativeRightDepth

attachmentNotEquivalence : isEquiv (λ (_ : Bool) → tt) → ⊥
attachmentNotEquivalence proof = false≢true
  (invEq (congEquiv {x = false} {y = true} ((λ _ → tt) , proof)) refl)

fullCompatibility : R.Presentations.pack R.Indexed.rightTree R.forward ≡
  R.Presentations.Views.Cuts.canonical R.Indexed.rightTree
fullCompatibility = R.compatibleComparison

cycle : E.Route R.Indexed.leftTree R.Indexed.leftTree
cycle = E.step R.backward (E.step R.forward (E.stay R.Indexed.leftTree))
closedTypeCycle : E.typeRoute cycle ≡ refl
closedTypeCycle = E.closedTypeRoute cycle
residualIdentity : (x : N.Realize R.Indexed.leftTree) → transport (E.typeRoute cycle) x ≡ x
residualIdentity = E.residualIsIdentity cycle

pairDetector : N.Realize pair → S¹
pairDetector (PO.inl tt) = base
pairDetector (PO.inr tt) = base
pairDetector (PO.push false i) = loop i
pairDetector (PO.push true i) = base

quadDetector : N.Realize quad → S¹
quadDetector (PO.inl x) = pairDetector x
quadDetector (PO.inr _) = base
quadDetector (PO.push b i) = base

includeLeft includeMiddle : N.Realize pair → Raw.Left
includeLeft x = PO.inl (PO.inl (PO.inl x))
includeMiddle x = PO.inl (PO.inr x)

leftLoop : Path Raw.Left (includeLeft (PO.inl tt)) (includeLeft (PO.inl tt))
leftLoop = cong includeLeft (PO.push false ∙ sym (PO.push true))
middleLoop : Path Raw.Left (includeMiddle (PO.inl tt)) (includeMiddle (PO.inl tt))
middleLoop = cong includeMiddle (PO.push false ∙ sym (PO.push true))
tailLoop : Path Raw.Left (PO.inr (N.firstAt Fixture.tail tt)) (PO.inr (N.firstAt Fixture.tail tt))
tailLoop i = PO.inr (Fixture.innerLoop i)

detectLeft : Raw.Right → S¹
detectLeft (PO.inl x) = quadDetector x
detectLeft (PO.inr _) = base
detectLeft (PO.push b i) = base

detectMiddle : Raw.Right → S¹
detectMiddle (PO.inl _) = base
detectMiddle (PO.inr (PO.inl x)) = pairDetector x
detectMiddle (PO.inr (PO.inr _)) = base
detectMiddle (PO.inr (PO.push b i)) = base
detectMiddle (PO.push b i) = base

detectTail : Raw.Right → S¹
detectTail (PO.inl _) = base
detectTail (PO.inr (PO.inl _)) = base
detectTail (PO.inr (PO.inr x)) = Fixture.innerDetector x
detectTail (PO.inr (PO.push b i)) = sym Fixture.innerFirst i
detectTail (PO.push b i) = base

leftDetected : cong (λ x → detectLeft (Raw.associate x)) leftLoop ≡ loop
leftDetected = cong-∙ (λ x → detectLeft (Raw.associate (includeLeft x)))
  (PO.push false) (sym (PO.push true)) ∙ sym (rUnit loop)
middleDetected : cong (λ x → detectMiddle (Raw.associate x)) middleLoop ≡ loop
middleDetected = cong-∙ (λ x → detectMiddle (Raw.associate (includeMiddle x)))
  (PO.push false) (sym (PO.push true)) ∙ sym (rUnit loop)
tailDetected : PathP (λ i → Fixture.innerFirst i ≡ Fixture.innerFirst i)
  (cong (λ x → detectTail (Raw.associate x)) tailLoop) loop
tailDetected = Fixture.innerDetected

-- Reflection through the actual realization reindexing, not its omission.
indexFrame : Raw.Right ≃ N.Realize R.Indexed.rightTree
indexFrame = pathToEquiv R.Indexed.realizationPath
reflectRaw : {x : Raw.Left} (p : x ≡ x) →
  cong (equivFun R.Indexed.nativeEquivalence) p ≡ refl → cong Raw.associate p ≡ refl
reflectRaw p h = sym (retEq (congEquiv indexFrame) (cong Raw.associate p))
  ∙ cong (invEq (congEquiv indexFrame)) h ∙ retEq (congEquiv indexFrame) refl

noLeftCollapse : cong (equivFun R.Indexed.nativeEquivalence) leftLoop ≡ refl → ⊥
noLeftCollapse h = circleLoopNotRefl (sym leftDetected ∙ cong (cong detectLeft) (reflectRaw leftLoop h))
noMiddleCollapse : cong (equivFun R.Indexed.nativeEquivalence) middleLoop ≡ refl → ⊥
noMiddleCollapse h = circleLoopNotRefl (sym middleDetected ∙ cong (cong detectMiddle) (reflectRaw middleLoop h))
noTailCollapse : cong (equivFun R.Indexed.nativeEquivalence) tailLoop ≡ refl → ⊥
noTailCollapse h = circleLoopNotRefl
  (sym (fromPathP tailDetected)
    ∙ cong (transport (λ i → Fixture.innerFirst i ≡ Fixture.innerFirst i))
      (cong (cong detectTail) (reflectRaw tailLoop h))
    ∙ fromPathP (λ i → refl {x = Fixture.innerFirst i}))

leftIgnoresMiddle : cong (λ x → detectLeft (Raw.associate x)) middleLoop ≡ refl
leftIgnoresMiddle = refl
leftIgnoresTail : cong (λ x → detectLeft (Raw.associate x)) tailLoop ≡ refl
leftIgnoresTail = refl
middleIgnoresLeft : cong (λ x → detectMiddle (Raw.associate x)) leftLoop ≡ refl
middleIgnoresLeft = refl
middleIgnoresTail : cong (λ x → detectMiddle (Raw.associate x)) tailLoop ≡ refl
middleIgnoresTail = refl
tailIgnoresLeft : cong (λ x → detectTail (Raw.associate x)) leftLoop ≡ refl
tailIgnoresLeft = refl
tailIgnoresMiddle : cong (λ x → detectTail (Raw.associate x)) middleLoop ≡ refl
tailIgnoresMiddle = refl

-- Compare complete presentations with the older endpoint-restricted
-- admission on circle-valued spans. The new admission needs no such input.
module CircleG = General Unit (λ _ → S¹) (λ _ _ → S¹) (λ x → x) (λ x → x)
module CircleR = CircleG.Rotation Circle.quad Circle.pair Circle.quad

agreesWithEndpointAdmission :
  CircleR.Presentations.pack CircleR.Indexed.rightTree CircleR.forward ≡
  CircleR.Presentations.pack CircleR.Indexed.rightTree Circle.Admitted.forward
agreesWithEndpointAdmission = CircleR.Presentations.Views.Cuts.compare
  CircleR.Indexed.rightTree _ _

-- The transport lemma also sees a genuinely varying attachment family.
constant : Unit → S¹
constant _ = base
twist : constant ≡ constant
twist i _ = loop i
twistNotRefl : twist ≡ refl → ⊥
twistNotRefl h = circleLoopNotRefl (cong (λ p i → p i tt) h)
module Transport = FixedLeft constant

diagramLoop : Path Transport.Diagram (S¹ , constant) (S¹ , constant)
diagramLoop i = S¹ , twist i

transportComparison : pathToEquiv (cong Transport.Realize diagramLoop) ≡ Transport.replacement diagramLoop
transportComparison = Transport.framePath diagramLoop
transportEndpoint : PathP
  (λ i → equivFun (transportComparison i) (PO.inl base) ≡ PO.inl base)
  (Transport.leftWitness diagramLoop base) refl
transportEndpoint = Transport.leftWitnessPath diagramLoop base
