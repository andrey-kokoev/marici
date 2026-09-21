{-# OPTIONS --safe --cubical --guardedness #-}
module ClosureReferenceNormalForm where

open import Cubical.Foundations.Prelude
open import Cubical.Foundations.Equiv
open import Cubical.Foundations.GroupoidLaws using (rCancel; lCancel; rUnit; lUnit; assoc)
open import ClosureAllDimensionalCutCoherence using (module FramedCuts)
open import ClosureTypedRealization using (TypedRealization; module AlongEquivalence)
open import ClosureProductBoundary using (module Observation)
open import ClosureRealizationHolonomy using (residualAction)

private
  -- All intermediate reference paths cancel, retaining explicit associativity
  -- and unit witnesses. This applies in the higher universe of typed values.
  telescope : ∀ {ℓ} {T : Type ℓ} {x y z o : T}
    (p : x ≡ o) (q : y ≡ o) (r : z ≡ o) →
    (p ∙ sym q) ∙ (q ∙ sym r) ≡ p ∙ sym r
  telescope p q r =
    sym (assoc p (sym q) (q ∙ sym r))
    ∙ cong (λ h → p ∙ h) (assoc (sym q) q (sym r))
    ∙ cong (λ h → p ∙ (h ∙ sym r)) (lCancel q)
    ∙ cong (λ h → p ∙ h) (sym (lUnit (sym r)))

module Model (K : Type) (X Y : K → Type) (A B : Type)
  (inputFrame : (k : K) → X k ≃ A)
  (outputFrame : (k : K) → Y k ≃ B)
  (operation : A → B) where
  module Cuts = FramedCuts K X Y A B inputFrame outputFrame operation

  -- Store one reference operation; derive its views rather than duplicating
  -- independent definitions. Independent maps enter through Compatible.
  view : (k : K) → X k → Y k
  view k = fst (Cuts.canonical k)

  normalize : (k : K) (p : Cuts.Compatible k) → p ≡ Cuts.canonical k
  normalize k p = Cuts.compare k p (Cuts.canonical k)

  reference : TypedRealization
  reference = (A → B) , operation

  typed : (k : K) → Cuts.Compatible k → TypedRealization
  typed k p = Cuts.Map k , fst p

  frame : (k : K) → Cuts.Map k ≃ (A → B)
  frame k = equiv→ (inputFrame k) (outputFrame k)

  operationCompatibility : (k : K) (p : Cuts.Compatible k) →
    equivFun (frame k) (fst p) ≡ operation
  operationCompatibility k p = funExt λ a →
    cong (λ F → F (invEq (inputFrame k) a)) (snd p)
    ∙ cong operation (secEq (inputFrame k) a)

  toReference : (k : K) (p : Cuts.Compatible k) → typed k p ≡ reference
  toReference k p = AlongEquivalence.together (frame k)
    {a = fst p} {b = operation} (operationCompatibility k p)

  between : (i j : K) (p : Cuts.Compatible i) (q : Cuts.Compatible j) →
    typed i p ≡ typed j q
  between i j p q = toReference i p ∙ sym (toReference j q)

  -- Reuse the previously checked finite-route semantics; only the explicit
  -- type-and-value path through the common reference is new here.
  routePath : {i j : K} (r : Cuts.Route i j) (p : Cuts.Compatible i) →
    typed i p ≡ typed j (Cuts.run r p)
  routePath (Cuts.stay k) p = refl
  routePath (Cuts.step {j = j} k r) p = routePath r p
    ∙ between j k (Cuts.run r p) (Cuts.change j k (Cuts.run r p))

  routeNormalForm : {i j : K} (r : Cuts.Route i j) (p : Cuts.Compatible i) →
    routePath r p ≡ between i j p (Cuts.run r p)
  routeNormalForm (Cuts.stay k) p = sym (rCancel (toReference k p))
  routeNormalForm (Cuts.step {i = i} {j = j} k r) p =
    cong (λ h → h ∙ between j k (Cuts.run r p) (Cuts.change j k (Cuts.run r p)))
      (routeNormalForm r p)
    ∙ telescope (toReference i p) (toReference j (Cuts.run r p))
        (toReference k (Cuts.change j k (Cuts.run r p)))

  presentationPathNormalForm : (k : K) {p q : Cuts.Compatible k} (h : p ≡ q) →
    cong (typed k) h ≡ between k k p q
  presentationPathNormalForm k {p = p} h =
    J (λ q h → cong (typed k) h ≡ between k k p q)
      (sym (rCancel (toReference k p))) h

  -- Closing the VALUE endpoint uses the checked compatible-presentation
  -- cycle law. Returning to the same type label alone is not sufficient.
  closedCycle : {k : K} (r : Cuts.Route k k) (p : Cuts.Compatible k) →
    typed k p ≡ typed k p
  closedCycle {k = k} r p = routePath r p
    ∙ cong (typed k) (Cuts.cycleLaw r p)

  -- Stronger than endpoint closure: these particular reference-based cycles
  -- are homotopic to the stationary path as TYPE-AND-VALUE realizations.
  closedCycleIsTrivial : {k : K} (r : Cuts.Route k k) (p : Cuts.Compatible k) →
    closedCycle r p ≡ refl
  closedCycleIsTrivial {k = k} r p =
    cong₂ _∙_ (routeNormalForm r p)
      (presentationPathNormalForm k (Cuts.cycleLaw r p))
    ∙ telescope (toReference k p) (toReference k (Cuts.run r p)) (toReference k p)
    ∙ rCancel (toReference k p)

  -- The residual is identity on EVERY inhabitant of the presentation's
  -- function type, not merely on the selected operation tracked by p.
  residualIsIdentity : {k : K} (r : Cuts.Route k k) (p : Cuts.Compatible k)
    (G : Cuts.Map k) → residualAction (closedCycle r p) G ≡ G
  residualIsIdentity r p G =
    cong (λ loop → residualAction loop G) (closedCycleIsTrivial r p)
    ∙ transportRefl G

  -- Boundary data has one general dependent form. A product is an optional
  -- specialization through Observation.productFromFibers, not a new default.
  module OutputBoundary (k : K) (P : Type) (observe : Y k → P) = Observation observe

-- This is an additive facade over checked modules, not a destructive rewrite.
-- It proves normal forms for the paths defined HERE through a common frame;
-- it does not erase residual actions of arbitrary independently chosen loops.
