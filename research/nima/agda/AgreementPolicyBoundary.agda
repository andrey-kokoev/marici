{-# OPTIONS --safe --cubical --guardedness #-}
module AgreementPolicyBoundary where

open import Cubical.Foundations.Prelude
open import Cubical.Data.Empty.Base using (⊥)
open import Cubical.Data.Sum.Base using (inr)
import RetainedTetrahedralPackage as Retained
import TetrahedralComparisonFeedback as Existing

-- Actual existing typed-value tetrahedron and its existing feedback adapter.
module F = Existing.Fixture.F
module N = F.N
module C = Retained.TypedFixture

input = Existing.Fixture.input
comparison : N.Compared
comparison = F.initial input

EffectAgreement : N.Compared → Type₁
EffectAgreement c = N.execute (N.Compared.first c) (N.Compared.input-value c)
                 ≡ N.execute (N.Compared.second c) (N.Compared.input-value c)

-- Agreement is already part of this actual comparison, not an added claim.
effects-agree : EffectAgreement comparison
effects-agree = N.Compared.effect-witness comparison

-- Yet the already implemented exchange changes the retained route order.
record-changes : F.F.exchange comparison ≡ comparison → ⊥
record-changes = F.exchange-changes-record input

-- The decoded full tetrahedral payload stays the same.
decoded-payload-fixed : F.decode-initial (F.F.exchange comparison)
                     ≡ F.decode-initial comparison
decoded-payload-fixed = refl

-- Thus equality of route effects cannot justify blanket record stasis.
no-effect-only-stasis :
  ((c : N.Compared) → EffectAgreement c → F.F.exchange c ≡ c) → ⊥
no-effect-only-stasis policy = record-changes (policy comparison effects-agree)

-- A DIFFERENT source operation explicitly retains an already full package.
-- This is a constructor clause, not a consequence of effects-agree above.
completed-generator-fixed : fst (C.C.C.generate (inr input)) ≡ inr input
completed-generator-fixed = refl
