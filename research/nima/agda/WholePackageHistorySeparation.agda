{-# OPTIONS --safe --cubical --guardedness #-}
module WholePackageHistorySeparation where

open import Cubical.Foundations.Prelude
open import Cubical.Foundations.Equiv
open import Cubical.Data.Unit.Base using (Unit; tt)
open import Cubical.Data.Empty.Base using (⊥)
open import Cubical.Data.Bool.Base using (true; false)
import WholePackageSigmaPi as Whole
import WholePackageResolution as Resolution

module Separation (ℓ : Level) (a : Whole.Universe.Complete ℓ) where
  open Whole.Universe ℓ
  open Resolution.Generators ℓ

  Seed : Complete → Type (ℓ-suc ℓ)
  Seed q = q ≡ a

  -- Same original package, same resulting complete comparison package.
  by-identity : Resolve Seed (identity-comparison a)
  by-identity = apply (identity-rule a) (λ _ → seed refl)

  by-general-comparison : Resolve Seed (identity-comparison a)
  by-general-comparison = apply (compare-rule a a (idEquiv _) refl)
    (λ { (lift true) → seed refl ; (lift false) → seed refl })

  IdentityRoot : {q : Complete} → Resolve Seed q → Type₀
  IdentityRoot (apply (identity-rule _) _) = Unit
  IdentityRoot _ = ⊥

  -- Equal endpoints do not erase distinct generating histories. This
  -- rules out raw identity as the universal comparison of resolutions.
  histories-distinct : by-identity ≡ by-general-comparison → ⊥
  histories-distinct p = subst IdentityRoot p tt
