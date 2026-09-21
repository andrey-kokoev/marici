{-# OPTIONS --safe --cubical --guardedness #-}
module ClosureFiltrationMapNaturality where

open import Cubical.Foundations.Prelude
open import Cubical.Data.Unit
open import Cubical.HITs.Pushout.Base
open import ClosureCanonicalRejoin using (module Rejoin; module Naturality)

-- This packages proved squares so that concrete constructions can be pasted.
-- The final ladder theorem below constructs every field; it does not take
-- an inhabitant of this record as a hypothesis.
record Comparison {A B C A′ B′ C′ : Type}
  (f : A → B) (g : B → C) (f′ : A′ → B′) (g′ : B′ → C′) : Type where
  field
    upper : Rejoin.Quotient f g → Rejoin.Quotient f′ g′
    lower : cofib g → cofib g′
    rejoinSquare : (x : Rejoin.Quotient f g) →
      Rejoin.rejoin f′ g′ (upper x) ≡ lower (Rejoin.rejoin f g x)
    cutSquare : (y : cofib g) →
      upper (Rejoin.cut f g y) ≡ Rejoin.cut f′ g′ (lower y)

compose : {A B C A′ B′ C′ A″ B″ C″ : Type}
  {f : A → B} {g : B → C}
  {f′ : A′ → B′} {g′ : B′ → C′}
  {f″ : A″ → B″} {g″ : B″ → C″} →
  Comparison f g f′ g′ → Comparison f′ g′ f″ g″ → Comparison f g f″ g″
Comparison.upper (compose p q) x = Comparison.upper q (Comparison.upper p x)
Comparison.lower (compose p q) y = Comparison.lower q (Comparison.lower p y)
Comparison.rejoinSquare (compose p q) x =
  Comparison.rejoinSquare q (Comparison.upper p x)
  ∙ cong (Comparison.lower q) (Comparison.rejoinSquare p x)
Comparison.cutSquare (compose p q) y =
  cong (Comparison.upper q) (Comparison.cutSquare p y)
  ∙ Comparison.cutSquare q (Comparison.lower p y)

-- Changing the source of an arrow acts on its cone attachments, without
-- changing its target points. This map need not be an equivalence.
precompose : {A A′ B : Type} (u : A → A′) (f : A′ → B) →
  cofib (λ a → f (u a)) → cofib f
precompose u f (inl tt) = inl tt
precompose u f (inr b) = inr b
precompose u f (push a i) = push (u a) i

module Source {A A′ B C : Type}
  (u : A → A′) (f : A′ → B) (g : B → C) where
  module Before = Rejoin (λ a → f (u a)) g
  module After = Rejoin f g

  upper : Before.Quotient → After.Quotient
  upper (inl tt) = inl tt
  upper (inr x) = inr (precompose u (λ a → g (f a)) x)
  upper (push (inl tt) i) = push (inl tt) i
  upper (push (inr b) i) = push (inr b) i
  upper (push (push a j) i) = push (push (u a) j) i

  square : (x : Before.Quotient) → After.rejoin (upper x) ≡ Before.rejoin x
  square (inl tt) = refl
  square (inr (inl tt)) = refl
  square (inr (inr c)) = refl
  square (inr (push a i)) = refl
  square (push (inl tt) i) = refl
  square (push (inr b) i) = refl
  square (push (push a j) i) = refl

  inverseSquare : (y : cofib g) → upper (Before.cut y) ≡ After.cut y
  inverseSquare (inl tt) = refl
  inverseSquare (inr c) = refl
  inverseSquare (push b i) = refl

  comparison : Comparison (λ a → f (u a)) g f g
  Comparison.upper comparison = upper
  Comparison.lower comparison y = y
  Comparison.rejoinSquare comparison = square
  Comparison.cutSquare comparison = inverseSquare

module Middle {A B B′ C : Type}
  (f : A → B) (v : B → B′) (g : B′ → C) where
  module Before = Rejoin f (λ b → g (v b))
  module After = Rejoin (λ a → v (f a)) g

  upper : Before.Quotient → After.Quotient
  upper (inl tt) = inl tt
  upper (inr x) = inr x
  upper (push (inl tt) i) = push (inl tt) i
  upper (push (inr b) i) = push (inr (v b)) i
  upper (push (push a j) i) = push (push a j) i

  square : (x : Before.Quotient) →
    After.rejoin (upper x) ≡ precompose v g (Before.rejoin x)
  square (inl tt) = refl
  square (inr (inl tt)) = refl
  square (inr (inr c)) = refl
  square (inr (push a i)) = refl
  square (push (inl tt) i) = refl
  square (push (inr b) i) = refl
  square (push (push a j) i) = refl

  inverseSquare : (y : cofib (λ b → g (v b))) →
    upper (Before.cut y) ≡ After.cut (precompose v g y)
  inverseSquare (inl tt) = refl
  inverseSquare (inr c) = refl
  inverseSquare (push b i) = refl

  comparison : Comparison f (λ b → g (v b)) (λ a → v (f a)) g
  Comparison.upper comparison = upper
  Comparison.lower comparison = precompose v g
  Comparison.rejoinSquare comparison = square
  Comparison.cutSquare comparison = inverseSquare

-- Reuse the checked target-postcomposition squares.
postcompose : {A B C C′ : Type} (f : A → B) (g : B → C) (w : C → C′) →
  Comparison f g f (λ b → w (g b))
Comparison.upper (postcompose f g w) = Naturality.upper f g w
Comparison.lower (postcompose f g w) = Naturality.Lower.direct f g w
Comparison.rejoinSquare (postcompose f g w) = Naturality.rejoinSquare f g w
Comparison.cutSquare (postcompose f g w) = Naturality.cutSquare f g w

-- A path of arrows yields a DEPENDENT family of the previously constructed
-- maps. Transport-filler keeps the boundary witnesses when arrows commute
-- only up to homotopy. No judgmental commutativity is required by the ladder.
module ArrowPaths {A B C : Type}
  {f₀ f₁ : A → B} {g₀ g₁ : B → C}
  (p : f₀ ≡ f₁) (q : g₀ ≡ g₁) where
  upperTypes : Rejoin.Quotient f₀ g₀ ≡ Rejoin.Quotient f₁ g₁
  upperTypes i = Rejoin.Quotient (p i) (q i)

  lowerTypes : cofib g₀ ≡ cofib g₁
  lowerTypes i = cofib (q i)

  comparison : Comparison f₀ g₀ f₁ g₁
  Comparison.upper comparison = transport upperTypes
  Comparison.lower comparison = transport lowerTypes
  Comparison.rejoinSquare comparison x = sym (fromPathP
    (λ i → Rejoin.rejoin (p i) (q i) (transport-filler upperTypes x i)))
  Comparison.cutSquare comparison y = fromPathP
    (λ i → Rejoin.cut (p i) (q i) (transport-filler lowerTypes y i))

module Ladder {A B C A′ B′ C′ : Type}
  (f : A → B) (g : B → C) (f′ : A′ → B′) (g′ : B′ → C′)
  (u : A → A′) (v : B → B′) (w : C → C′)
  (Hf : (a : A) → v (f a) ≡ f′ (u a))
  (Hg : (b : B) → w (g b) ≡ g′ (v b)) where

  -- Factor the actual ladder into target change, second-square adjustment,
  -- middle change, first-square adjustment, and source change. Every stage
  -- has a constructed rejoin square AND a constructed inverse-cut square.
  targetStep : Comparison f g f (λ b → w (g b))
  targetStep = postcompose f g w

  secondSquareStep : Comparison f (λ b → w (g b)) f (λ b → g′ (v b))
  secondSquareStep = ArrowPaths.comparison refl (funExt Hg)

  middleStep : Comparison f (λ b → g′ (v b)) (λ a → v (f a)) g′
  middleStep = Middle.comparison f v g′

  firstSquareStep : Comparison (λ a → v (f a)) g′ (λ a → f′ (u a)) g′
  firstSquareStep = ArrowPaths.comparison (funExt Hf) refl

  sourceStep : Comparison (λ a → f′ (u a)) g′ f′ g′
  sourceStep = Source.comparison u f′ g′

  comparison : Comparison f g f′ g′
  comparison = compose targetStep
    (compose secondSquareStep
      (compose middleStep (compose firstSquareStep sourceStep)))

  mapQuotient : Rejoin.Quotient f g → Rejoin.Quotient f′ g′
  mapQuotient = Comparison.upper comparison

  mapCofiber : cofib g → cofib g′
  mapCofiber = Comparison.lower comparison

  rejoinNaturality : (x : Rejoin.Quotient f g) →
    Rejoin.rejoin f′ g′ (mapQuotient x) ≡ mapCofiber (Rejoin.rejoin f g x)
  rejoinNaturality = Comparison.rejoinSquare comparison

  cutNaturality : (y : cofib g) →
    mapQuotient (Rejoin.cut f g y) ≡ Rejoin.cut f′ g′ (mapCofiber y)
  cutNaturality = Comparison.cutSquare comparison

-- Arbitrary vertical maps are allowed; no isEquiv hypotheses are imposed.
-- These are constructed maps for three-object ladders with chosen square
-- homotopies. Their composition coherence for arbitrary ladders, naturality
-- of the five-object pentagon, and agreement with other cofiber-map choices
-- are separate theorems, not asserted here.
