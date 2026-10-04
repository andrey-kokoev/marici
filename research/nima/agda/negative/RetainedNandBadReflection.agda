{-# OPTIONS --safe --cubical --guardedness #-}
module RetainedNandBadReflection where
open import Cubical.Foundations.Prelude
open import Cubical.Data.Bool.Base using (Bool; false; true)
import QBooleanity as Q
open import RetainedNandPhases

-- Truth reflection identifies the two Boolean answers. This proposed decoder
-- cannot recover the true answer; the positive module excludes every decoder.
recover : Q.D Bool → Bool
recover d = false
bad-recovery : recover (Q.eta true) ≡ true
bad-recovery = refl
