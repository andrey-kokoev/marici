{-# OPTIONS --safe --cubical --guardedness #-}
module ScalarSixCertificate where

open import Cubical.Foundations.Prelude
open import Cubical.Data.Sigma.Base using (_×_)
open import Cubical.Data.Int.Base using (ℤ; pos; negsuc; _·_)
open import Cubical.Data.List.Base using (List; []; _∷_; map; length)
open import ScalarSixKernel
open import ScalarSixFixture

coupling-fixed : (couplingNumerator ≡ pos 3) × (couplingDenominator ≡ pos 5)
coupling-fixed = refl , refl

-- Enumerate the ten label-preserving unordered channels, not ten supplied values.
census : length channels ≡ 10
census = refl

null-external : map (λ l → square (momenta l)) allLabels ≡
  (pos 0 ∷ pos 0 ∷ pos 0 ∷ pos 0 ∷ pos 0 ∷ pos 0 ∷ [])
null-external = refl

conserved : sumP (map momenta allLabels) ≡ p (pos 0) (pos 0) (pos 0) (pos 0)
conserved = refl

squares : denominators momenta ≡
  (pos 8 ∷ pos 8 ∷ pos 8 ∷ pos 8 ∷ negsuc 3 ∷ negsuc 5 ∷
   negsuc 5 ∷ negsuc 5 ∷ negsuc 5 ∷ negsuc 3 ∷ [])
squares = refl

-- Also proves none of the listed propagators is zero; no rational i0 used.
reciprocals : inverseChecks (denominators momenta) ≡
  (pos 24 ∷ pos 24 ∷ pos 24 ∷ pos 24 ∷ pos 24 ∷ pos 24 ∷
   pos 24 ∷ pos 24 ∷ pos 24 ∷ pos 24 ∷ [])
reciprocals = refl

numerator : ℤ
numerator = amplitudeNumerator (couplingNumerator · couplingNumerator) (denominators momenta)

denominator : ℤ
denominator = (couplingDenominator · couplingDenominator) · pos 24

computed-numerator : numerator ≡ pos 144
computed-numerator = refl

computed-denominator : denominator ≡ pos 600
computed-denominator = refl

-- The exported evaluator value is checked against arithmetic, not postulated.
export-agrees : numerator · exportedDenominator ≡ exportedNumerator · denominator
export-agrees = refl

frozen-value : (exportedNumerator ≡ pos 6) × (exportedDenominator ≡ pos 25)
frozen-value = refl , refl
