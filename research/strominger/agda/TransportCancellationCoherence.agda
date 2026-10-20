{-# OPTIONS --safe --cubical --guardedness #-}
module TransportCancellationCoherence where

open import Cubical.Foundations.Prelude
open import Cubical.Foundations.Transport using (transport⁻Transport; subst⁻Subst)
open import Cubical.Foundations.GroupoidLaws using (lUnit)

-- Keep the library's exact cancellation witnesses. At a constant type line,
-- varying the transp extent deforms all three transports simultaneously to
-- identity, including both candidate cancellation paths and their endpoints.
module Constant {ℓ : Level} (X : Type ℓ) (x : X) where
  T : I → X → X
  T r a = transp (λ _ → X) r a
  cancel : (r : I) (a : X) → T r (T r a) ≡ a
  cancel r a j = T (r ∨ j) (T (r ∨ j) a)
  Goal : I → Type ℓ
  Goal r = cancel r (T r x) ≡ cong (T r) (cancel r x)
  triangle : transport⁻Transport (sym (refl {x = X})) (transport refl x)
    ≡ cong (transport refl) (transport⁻Transport refl x)
  triangle = transport (λ r → Goal (~ r)) refl

roundTrip : ∀ {ℓ ℓ'} {X : Type ℓ} {a b : X} (B : X → Type ℓ')
  (p : a ≡ b) (q : b ≡ a) → q ≡ sym p → (x : B a)
  → subst B q (subst B p x) ≡ x
roundTrip B p q h x = cong (λ r → subst B r (subst B p x)) h ∙ subst⁻Subst B p x

abstract
  transport-cancellation-triangle : ∀ {ℓ} {X Y : Type ℓ} (p : X ≡ Y) (x : X)
    → transport⁻Transport (sym p) (transport p x)
      ≡ cong (transport p) (transport⁻Transport p x)
  transport-cancellation-triangle {X = X} = J
    (λ Y p → (x : X) → transport⁻Transport (sym p) (transport p x)
      ≡ cong (transport p) (transport⁻Transport p x))
    (Constant.triangle X)

  subst-cancellation-triangle : ∀ {ℓ ℓ'} {X : Type ℓ} {a b : X}
    (B : X → Type ℓ') (p : a ≡ b) (x : B a)
    → subst⁻Subst B (sym p) (subst B p x)
      ≡ cong (subst B p) (subst⁻Subst B p x)
  subst-cancellation-triangle B p x = transport-cancellation-triangle (cong B p) x

  paired-roundTrip : ∀ {ℓ ℓ'} {X : Type ℓ} {a b : X} (B : X → Type ℓ')
    (p : a ≡ b) (q : b ≡ a) (h : q ≡ sym p) (x : B a)
    → roundTrip B q p (cong sym (sym h)) (subst B p x)
      ≡ cong (subst B p) (roundTrip B p q h x)
  paired-roundTrip B p q h x = J
    (λ q k → roundTrip B q p (cong sym k) (subst B p x)
      ≡ cong (subst B p) (roundTrip B p q (sym k) x))
    (sym (lUnit (subst⁻Subst B (sym p) (subst B p x)))
      ∙ subst-cancellation-triangle B p x
      ∙ cong (cong (subst B p)) (lUnit (subst⁻Subst B p x)))
    (sym h)

  paired-with-coherence : ∀ {ℓ ℓ'} {X : Type ℓ} {a b : X} (B : X → Type ℓ')
    (p : a ≡ b) (q : b ≡ a) (h : q ≡ sym p) (h' : p ≡ sym q)
    → h' ≡ cong sym (sym h) → (x : B a)
    → roundTrip B q p h' (subst B p x)
      ≡ cong (subst B p) (roundTrip B p q h x)
  paired-with-coherence B p q h h' cube x =
    cong (λ k → roundTrip B q p k (subst B p x)) cube ∙ paired-roundTrip B p q h x
