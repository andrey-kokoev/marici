{-# OPTIONS --safe --cubical --no-import-sorts --guardedness #-}
module RationalAnalyticSubstrate where

open import Cubical.Foundations.Prelude
open import Cubical.Data.Rationals as Q
open import Cubical.Data.Int using (pos)
open import Cubical.Data.NatPlusOne
open import Cubical.Algebra.AbGroup
open import Cubical.Algebra.CommRing
open import GenericPastingComplex

-- The library's packaged rational CommRing uses the legacy QuoQ carrier,
-- while its preferred ordered rationals use Q. Repackage the proved preferred
-- operations so algebra and order share one carrier.
PreferredℚCommRing : CommRing ℓ-zero
PreferredℚCommRing =
  makeCommRing 0 1 Q._+_ Q._·_ Q.-_
    Q.isSetℚ Q.+Assoc Q.+IdR Q.+InvR Q.+Comm
    Q.·Assoc Q.·IdR Q.·DistL+ Q.·Comm

RationalAbGroup : AbGroup ℓ-zero
RationalAbGroup = CommRing→AbGroup PreferredℚCommRing

one-half : Q.ℚ
one-half = Q.[ pos 1 / 2 ]

halfℚ : Q.ℚ → Q.ℚ
halfℚ q = q Q.· one-half

one-half-double : one-half Q.+ one-half ≡ 1
one-half-double = Q.eq/ _ _ refl

half-double : (q : Q.ℚ) → halfℚ q Q.+ halfℚ q ≡ q
half-double q =
  sym (Q.·DistL+ q one-half one-half) ∙
  cong (q Q.·_) one-half-double ∙ Q.·IdR q

module RationalPasting = Triangle RationalAbGroup

rational-chain :
  (v : RationalPasting.M³) →
  RationalPasting.∂₂ (RationalPasting.∂₁ v) ≡ 0
rational-chain = RationalPasting.chain

rational-middle-exact :
  (v : RationalPasting.M³) →
  RationalPasting.∂₂ v ≡ 0 →
  Σ[ u ∈ RationalPasting.M³ ] RationalPasting.∂₁ u ≡ v
rational-middle-exact = RationalPasting.middle-exact
