{-# OPTIONS --safe --cubical --guardedness #-}
-- EXPECTED FAILURE: 144/600 is not 7/25.
module negative.ScalarSixBadResult where
open import Cubical.Foundations.Prelude
open import Cubical.Data.Int.Base using (pos; _·_)
open import ScalarSixCertificate using (numerator; denominator)

bad-result : numerator · pos 25 ≡ pos 7 · denominator
bad-result = refl
