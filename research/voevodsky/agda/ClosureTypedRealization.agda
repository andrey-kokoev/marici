{-# OPTIONS --safe --cubical --guardedness #-}
module ClosureTypedRealization where

open import Cubical.Foundations.Prelude
open import Cubical.Foundations.Equiv
open import Cubical.Foundations.Univalence
open import Cubical.Foundations.GroupoidLaws using (rCancel)
open import ClosureFourPresentations using (module Presentations)
open import Cubical.HITs.Pushout.Base using (cofib)

-- A type TOGETHER WITH an inhabitant. This lives one universe above the
-- individual realization types. No value is identified with its own type.
TypedRealization : Type₁
TypedRealization = Σ[ T ∈ Type ] T

module AlongEquivalence {A B : Type} (e : A ≃ B) {a : A} {b : B}
  (compatible : equivFun e a ≡ b) where
  typePath : A ≡ B
  typePath = ua e

  valuePath : PathP (λ i → typePath i) a b
  valuePath = ua-gluePath e compatible

  together : Path TypedRealization (A , a) (B , b)
  together i = typePath i , valuePath i

  -- Extracting the endpoint comparison gives back the supplied proof,
  -- including its path data. This is not merely equality of endpoint values.
  recoversCompatibility : ua-ungluePath e valuePath ≡ compatible
  recoversCompatibility = refl

  outAndBack : together ∙ sym together ≡ refl
  outAndBack = rCancel together

-- Changing a COMPATIBLE choice also transports its typed-realization path.
-- Endpoints at the source vary by the first projection of the choice path.
module ChoiceCoherence {A B : Type} (e : A ≃ B) (b : B) where
  Choice : Type
  Choice = fiber (equivFun e) b

  realize : (p : Choice) → Path TypedRealization (A , fst p) (B , b)
  realize p = AlongEquivalence.together e (snd p)

  compareChoices : (p q : Choice) → p ≡ q
  compareChoices p q = sym (equivCtrPath e b p) ∙ equivCtrPath e b q

  coherence : (p q : Choice) (h : p ≡ q) →
    PathP (λ i → Path TypedRealization (A , fst (h i)) (B , b))
      (realize p) (realize q)
  coherence p q h i = realize (h i)

module CofiberOperation {A B C A′ B′ C′ : Type}
  (f : A → B) (g : B → C) (f′ : A′ → B′) (g′ : B′ → C′)
  (u : A → A′) (v : B → B′) (w : C → C′)
  (Hf : (a : A) → v (f a) ≡ f′ (u a))
  (Hg : (b : B) → w (g b) ≡ g′ (v b)) where
  module Old = Presentations f g f′ g′ u v w Hf Hg
  module Travel = AlongEquivalence Old.operationEquivalence
    {a = Old.F4} {b = Old.F1} Old.chosenOperationComparison
  module Choices = ChoiceCoherence Old.operationEquivalence Old.F1

  -- The value at the expanded endpoint is the independently constructed
  -- ladder map, NOT a newly defined function chosen to satisfy the square.
  expanded rejoined : TypedRealization
  expanded = Old.V4 , Old.F4
  rejoined = Old.V1 , Old.F1

  realizationPath : expanded ≡ rejoined
  realizationPath = Travel.together

  operationAlongTypes : PathP (λ i → ua Old.operationEquivalence i) Old.F4 Old.F1
  operationAlongTypes = Travel.valuePath

  -- A second, explicitly arrow-shaped traversal changes domain and codomain
  -- together, so the intermediate operation can be applied to a travelling
  -- input. It is not asserted equal to the whole-function-type ua path above.
  arrowTypePath : Old.V4 ≡ Old.V1
  arrowTypePath i = ua Old.S.rejoinEquiv i → ua Old.T.rejoinEquiv i

  arrowAlongTypes : PathP (λ i → arrowTypePath i) Old.F4 Old.F1
  arrowAlongTypes = ua→ {e = Old.S.rejoinEquiv}
    {B = λ i → ua Old.T.rejoinEquiv i} {f₀ = Old.F4} {f₁ = Old.F1}
    (λ x → ua-gluePath Old.T.rejoinEquiv
      {x = Old.F4 x} {y = Old.F1 (Old.S.rejoin x)} (Old.independentSquare x))

  inputAlongTypes : (x : Old.S.Quotient) →
    PathP (λ i → ua Old.S.rejoinEquiv i) x (Old.S.rejoin x)
  inputAlongTypes x = ua-gluePath Old.S.rejoinEquiv
    {x = x} {y = Old.S.rejoin x} refl

  evaluationAlongTypes : (x : Old.S.Quotient) →
    PathP (λ i → ua Old.T.rejoinEquiv i) (Old.F4 x) (Old.F1 (Old.S.rejoin x))
  evaluationAlongTypes x i = arrowAlongTypes i (inputAlongTypes x i)

  evaluatedRealizationPath : (x : Old.S.Quotient) →
    Path TypedRealization (Old.T.Quotient , Old.F4 x)
      (cofib g′ , Old.F1 (Old.S.rejoin x))
  evaluatedRealizationPath x i = ua Old.T.rejoinEquiv i , evaluationAlongTypes x i

  preservedOriginalComparison :
    ua-ungluePath Old.operationEquivalence operationAlongTypes ≡
    Old.chosenOperationComparison
  preservedOriginalComparison = Travel.recoversCompatibility

  actualChoice : Choices.Choice
  actualChoice = Old.F4 , Old.chosenOperationComparison

  transportedChoice : Choices.Choice
  transportedChoice = equivCtr Old.operationEquivalence Old.F1

  transportedValueIsF2 : fst transportedChoice ≡ (λ x → Old.F2 (Old.S.rejoin x))
  transportedValueIsF2 = refl

  choiceComparison : actualChoice ≡ transportedChoice
  choiceComparison = Choices.compareChoices actualChoice transportedChoice

  coherentRealizationPaths :
    PathP (λ i → Path TypedRealization
      (Old.V4 , fst (choiceComparison i)) rejoined)
      realizationPath (Choices.realize transportedChoice)
  coherentRealizationPaths = Choices.coherence actualChoice transportedChoice choiceComparison

  returnLaw : realizationPath ∙ sym realizationPath ≡ refl
  returnLaw = Travel.outAndBack

-- This realizes a change of TYPE AND VALUE together. It adds no new
-- analytical equivalence or Pi-factorization. Reverse traversal here means
-- the reverse of this specific path, not an arbitrary independent transition.
