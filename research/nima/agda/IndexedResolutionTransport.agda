{-# OPTIONS --safe --cubical --guardedness #-}
module IndexedResolutionTransport where
open import Cubical.Foundations.Prelude
open import Cubical.Foundations.Equiv
open import Cubical.Foundations.Univalence using (ua; ua→; pathToEquiv; EquivJ)

-- An independently instantiated indexed derivation datatype.
module Theory {ℓ : Level} (State Rule : Type ℓ)
  (Arity : Rule → Type ℓ) (input : (r : Rule) → Arity r → State)
  (output : Rule → State) (Seeds : State → Type ℓ) where
  data Resolve : State → Type ℓ where
    seed : {q : State} → Seeds q → Resolve q
    apply : (r : Rule) → ((i : Arity r) → Resolve (input r i)) → Resolve (output r)
  Closed : Type ℓ
  Closed = Σ State Resolve

-- Equivalence of marked signatures, including actual seed witnesses, induces
-- equivalence of their retained derivations. The endpoint square is part of
-- the result, rather than an unverified property of an arbitrary equivalence.
module Transfer {ℓ : Level} (B₁ R₁ : Type ℓ)
  (A₁ : R₁ → Type ℓ) (I₁ : (r : R₁) → A₁ r → B₁)
  (O₁ : R₁ → B₁) (S₁ : B₁ → Type ℓ) where
  module Target = Theory B₁ R₁ A₁ I₁ O₁ S₁
  Result : (B₀ : Type ℓ) (eB : B₀ ≃ B₁) (R₀ : Type ℓ)
    (A₀ : R₀ → Type ℓ) (I₀ : (r : R₀) → A₀ r → B₀)
    (O₀ : R₀ → B₀) (S₀ : B₀ → Type ℓ) → Type ℓ
  Result B₀ eB R₀ A₀ I₀ O₀ S₀ =
    Σ (Theory.Closed B₀ R₀ A₀ I₀ O₀ S₀ ≃ Target.Closed)
      (λ e → (x : Theory.Closed B₀ R₀ A₀ I₀ O₀ S₀)
        → fst (equivFun e x) ≡ equivFun eB (fst x))
  Problem : (B₀ : Type ℓ) → B₀ ≃ B₁ → (R₀ : Type ℓ) → R₀ ≃ R₁ → Type (ℓ-suc ℓ)
  Problem B₀ eB R₀ eR =
    (A₀ : R₀ → Type ℓ) (I₀ : (r : R₀) → A₀ r → B₀)
    (O₀ : R₀ → B₀) (S₀ : B₀ → Type ℓ)
    (eA : (r : R₀) → A₀ r ≃ A₁ (equivFun eR r))
    → ((r : R₀) (i : A₀ r) → equivFun eB (I₀ r i) ≡ I₁ (equivFun eR r) (equivFun (eA r) i))
    → ((r : R₀) → equivFun eB (O₀ r) ≡ O₁ (equivFun eR r))
    → ((q : B₀) → S₀ q ≃ S₁ (equivFun eB q))
    → Result B₀ eB R₀ A₀ I₀ O₀ S₀
  identity-case : Problem B₁ (idEquiv B₁) R₁ (idEquiv R₁)
  identity-case A₀ I₀ O₀ S₀ eA inputs outputs seeds =
    pathToEquiv closure-path , (λ x → sym (λ i → fst (transport-filler closure-path x i)))
    where
    closure-path : Theory.Closed B₁ R₁ A₀ I₀ O₀ S₀ ≡ Target.Closed
    closure-path i = Theory.Closed B₁ R₁ (λ r → ua (eA r) i)
      (λ r → ua→ {e = eA r} {B = λ _ → B₁} {f₀ = I₀ r} {f₁ = I₁ r} (inputs r) i)
      (λ r → outputs r i) (λ q → ua (seeds q) i)
  -- Keep the checked proof opaque at concrete applications, avoiding eager
  -- normalization of the entire univalence construction on large derivations.
  abstract
    transport-theory : {B₀ R₀ : Type ℓ} (eB : B₀ ≃ B₁) (eR : R₀ ≃ R₁) → Problem B₀ eB R₀ eR
    transport-theory {R₀ = R₀} eB eR = EquivJ
      (λ B e → (R : Type ℓ) (f : R ≃ R₁) → Problem B e R f)
      (λ R f → EquivJ (λ R f → Problem B₁ (idEquiv B₁) R f) identity-case f)
      eB R₀ eR
