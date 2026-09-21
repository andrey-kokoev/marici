{-# OPTIONS --safe --cubical --guardedness #-}
module ClosureFourPresentations where

open import Cubical.Foundations.Prelude
open import Cubical.Foundations.Equiv
open import ClosureCanonicalRejoin using (module Rejoin)
open import ClosureFiltrationMapNaturality using (module Ladder)
open import Cubical.HITs.Pushout.Base using (cofib)

module Presentations {A B C A′ B′ C′ : Type}
  (f : A → B) (g : B → C) (f′ : A′ → B′) (g′ : B′ → C′)
  (u : A → A′) (v : B → B′) (w : C → C′)
  (Hf : (a : A) → v (f a) ≡ f′ (u a))
  (Hg : (b : B) → w (g b) ≡ g′ (v b)) where

  module S = Rejoin f g
  module T = Rejoin f′ g′
  module L = Ladder f g f′ g′ u v w Hf Hg

  -- These are function types on cofibers, not claimed Pi-factorizations
  -- of the quotient objects into families and retained boundary objects.
  V1 V2 V3 V4 : Type
  V1 = cofib g → cofib g′
  V2 = cofib g → T.Quotient
  V3 = S.Quotient → cofib g′
  V4 = S.Quotient → T.Quotient

  F1 : V1
  F1 = L.mapCofiber

  F2 : V2
  F2 y = T.cut (F1 y)

  F3 : V3
  F3 x = F1 (S.rejoin x)

  -- IMPORTANT: retain the previously independently constructed map.
  -- Do not define this as T.cut composed with F1 composed with S.rejoin.
  F4 : V4
  F4 = L.mapQuotient

  outputReassembly : (y : cofib g) → T.rejoin (F2 y) ≡ F1 y
  outputReassembly y = T.rejoin-cut (F1 y)

  inputReassembly : (x : S.Quotient) → F3 x ≡ F1 (S.rejoin x)
  inputReassembly x = refl

  independentSquare : (x : S.Quotient) → T.rejoin (F4 x) ≡ F3 x
  independentSquare = L.rejoinNaturality

  -- The ambient types of operations are equivalent. This alone would not
  -- identify the chosen F4; that identification is proved separately below.
  expandOutput : V1 ≃ V2
  expandOutput = equivΠCod (λ _ → invEquiv T.rejoinEquiv)

  expandInput : V1 ≃ V3
  expandInput = equiv→ (invEquiv S.rejoinEquiv) (idEquiv (cofib g′))

  operationEquivalence : V4 ≃ V1
  operationEquivalence = equiv→ S.rejoinEquiv T.rejoinEquiv

  chosenOperationComparison : equivFun operationEquivalence F4 ≡ F1
  chosenOperationComparison = funExt (λ y →
    independentSquare (invEq S.rejoinEquiv y)
    ∙ cong F1 (secEq S.rejoinEquiv y))

  -- A compatible lift includes its square witness, not only its function.
  post : V4 → V3
  post F x = T.rejoin (F x)

  CompatibleLift : Type
  CompatibleLift = Σ[ F ∈ V4 ] (post F ≡ F3)

  abstract
    postIsEquiv : isEquiv post
    postIsEquiv = snd (equivΠCod (λ (_ : S.Quotient) → T.rejoinEquiv))

  postEquiv : V4 ≃ V3
  postEquiv = post , postIsEquiv

  -- The homotopy fiber of an equivalence is contractible. This contracts
  -- pairs (map, square); it does NOT assert that V4 is a set or contractible.
  abstract
    compatibleLiftIsContr : isContr CompatibleLift
    compatibleLiftIsContr =
      equivCtr postEquiv F3 , equivCtrPath postEquiv F3

  independentLift : CompatibleLift
  independentLift = F4 , funExt independentSquare

  transportedLift : CompatibleLift
  transportedLift = (λ x → F2 (S.rejoin x)) ,
    funExt (λ x → outputReassembly (S.rejoin x))

  -- Agreement IN THE FIBER: both the map and its commuting-square witness
  -- are compared. This is stronger than comparing endpoint values alone.
  liftIdentification : independentLift ≡ transportedLift
  liftIdentification =
    sym (snd compatibleLiftIsContr independentLift)
    ∙ snd compatibleLiftIsContr transportedLift

  functionIdentification : F4 ≡ (λ x → F2 (S.rejoin x))
  functionIdentification = cong fst liftIdentification

  F4-as-transport : (x : S.Quotient) → F4 x ≡ F2 (S.rejoin x)
  F4-as-transport x i = functionIdentification i x

  squareCoherence : PathP
    (λ i → post (functionIdentification i) ≡ F3)
    (funExt independentSquare)
    (funExt (λ x → outputReassembly (S.rejoin x)))
  squareCoherence i = snd (liftIdentification i)

-- The four labels refer to presentations through rejoin equivalences. Their
-- identification with specific unary/many analytical arities or dependent
-- product-and-boundary formulas remains additional structure, not proved here.
