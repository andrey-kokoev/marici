{-# OPTIONS --safe --cubical --guardedness #-}
module SourceAdmissibleComparisons where

open import Cubical.Foundations.Prelude
open import BoundaryExtensionFibres

-- The caller must instantiate this predicate with actual source constraints.
-- It is not evidence that arbitrary declared constraints are physical.
AdmissibleFiller : {ℓ : Level} {A B : Type ℓ}
  (f g : A → B) → ((a : A) → f a ≡ g a → Type ℓ) → Type ℓ
AdmissibleFiller {A = A} f g allowed =
  (a : A) → Σ (f a ≡ g a) (allowed a)

forgetAdmissibility : {ℓ : Level} {A B : Type ℓ}
  {f g : A → B} {allowed : (a : A) → f a ≡ g a → Type ℓ}
  → AdmissibleFiller f g allowed → (a : A) → f a ≡ g a
forgetAdmissibility filler a = fst (filler a)

-- Replacement does not by itself identify the old and new problems.
record MapReplacement {ℓ : Level} (A B : Type ℓ) : Type ℓ where
  field
    oldMap newMap : A → B

-- Transport of extension data requires its own comparison witness.
transportExtension : {ℓ : Level} {A B : Type ℓ}
  {old new : A → B} → ((a : A) → old a ≡ new a)
  → (b : B) → Extension old b → Extension new b
transportExtension compare b (a , boundary) =
  a , sym (compare a) ∙ boundary

-- A change of marking object and readout needs a commuting readout square.
transportNormalization : {ℓ : Level} {M N R : Type ℓ}
  (change : M → N) (oldReadout : M → R) (newReadout : N → R)
  → ((m : M) → newReadout (change m) ≡ oldReadout m)
  → (r : R) → Extension oldReadout r → Extension newReadout r
transportNormalization change oldReadout newReadout square r (m , p) =
  change m , square m ∙ p

-- Nonempty admissible locus, but no point over the requested normalization.
OnlyFirst : Marking → Type
OnlyFirst m = m ≡ first

RestrictedMarking : Type
RestrictedMarking = Σ Marking OnlyFirst

restrictedReadout : RestrictedMarking → Marking
restrictedReadout = fst

forgetful-second-extension : Extension (λ (m : Marking) → m) second
forgetful-second-extension = second , refl

restricted-second-impossible : Extension restrictedReadout second → Impossible
restricted-second-impossible ((m , admitted) , p) =
  first≠second (sym admitted ∙ p)

-- Forgetting can turn an empty extension problem into an inhabited one.
no-automatic-lift :
  (Extension (λ (m : Marking) → m) second
    → Extension restrictedReadout second) → Impossible
no-automatic-lift liftExtension =
  restricted-second-impossible (liftExtension forgetful-second-extension)

-- Changing one endpoint creates a different filler problem.
constantFirst constantSecond : UnitReadout → Marking
constantFirst _ = first
constantSecond _ = second

old-filler : (u : UnitReadout) → constantFirst u ≡ constantFirst u
old-filler _ = refl

new-filler-impossible :
  ((u : UnitReadout) → constantFirst u ≡ constantSecond u) → Impossible
new-filler-impossible filler = first≠second (filler unit)

-- Even when the underlying path exists, an admissibility witness is separate.
forbidden-filler-impossible :
  AdmissibleFiller constantFirst constantFirst (λ _ _ → Impossible)
  → Impossible
forbidden-filler-impossible filler = snd (filler unit)

-- Changing markings need not preserve their old normalization.
changeToSecond : Marking → Marking
changeToSecond _ = second

normalization-square-impossible :
  ((m : Marking) → changeToSecond m ≡ m) → Impossible
normalization-square-impossible square = first≠second (sym (square first))
