{-# OPTIONS --safe --cubical --guardedness #-}
module RamseyComparisonForgetting where
open import Cubical.Foundations.Prelude
open import Cubical.Data.Sigma.Base using (_×_)
open import Cubical.Data.Empty as Empty using (⊥)
open import Cubical.Data.Bool.Base using (Bool; false; true)
open import Cubical.Data.Bool.Properties using (false≢true)

Factors : {X S T : Type} → (X → S) → (X → T) → Type
Factors {S = S} {T = T} forget target = Σ (S → T) (λ h → ∀ x → h (forget x) ≡ target x)

fiber-necessary : {X S T : Type} (forget : X → S) (target : X → T)
  → Factors forget target → (x y : X) → forget x ≡ forget y → target x ≡ target y
fiber-necessary forget target (h , law) x y same = sym (law x) ∙ cong h same ∙ law y

-- A fixed canonical admission has no variable completion to separate.
canonical-factor : {Root S T : Type} (actual : Root) (forget : Root → S) (target : Root → T)
  → Factors {X = Σ Root (λ a → a ≡ actual)} (λ x → forget (fst x)) (λ x → target (fst x))
canonical-factor actual forget target = (λ _ → target actual) , (λ x → sym (cong target (snd x)))

-- For independently admitted pairs, source-only target recovery requires
-- every allowed target to be equal. This is a different admission policy.
product-factor-to-constant : {S T : Type} → S
  → Factors {X = S × T} fst snd → Σ T (λ t₀ → (t : T) → t₀ ≡ t)
product-factor-to-constant s (h , law) = h s , (λ t → law (s , t))
constant-to-product-factor : {S T : Type}
  → Σ T (λ t₀ → (t : T) → t₀ ≡ t) → Factors {X = S × T} fst snd
constant-to-product-factor (t₀ , equal) = (λ _ → t₀) , (λ x → equal (snd x))

independent-boolean-obstruction : {S : Type} → S → Factors {X = S × Bool} fst snd → ⊥
independent-boolean-obstruction s factor =
  false≢true (fiber-necessary fst snd factor (s , false) (s , true) refl)
