{-# OPTIONS --safe --cubical --guardedness #-}
module SynthesisMinimumMissingCase where
open import Cubical.Foundations.Prelude
open import Cubical.Data.Nat.Base using (ℕ; zero; suc; _+_)
open import Cubical.Data.Nat.Order using (_<_; ¬m+n<m)
open import Cubical.Data.Bool.Base using (Bool; false; true)
open import Cubical.Data.Bool.Properties using (isSetBool; false≢true)
open import Cubical.Data.Empty.Base using (⊥)
open import Cubical.Data.List.Base using (List; []; _∷_; _++_)
open import Cubical.Data.Maybe.Base using (Maybe; nothing; just)
open import Cubical.Data.Maybe.Properties using (isOfHLevelMaybe)
open import Cubical.Data.Sigma.Base using (_×_)
open import Cubical.Foundations.HLevels using (isOfHLevelLift; isSet×)
open import AlgebraSynthesisSpecification
import BooleanNandEquivalence as B

open import SynthesisMinimumSupport
import GeneratedMinimumShape0
module Missing (ℓ : Level) where
  open Support ℓ
  module W0 = GeneratedMinimumShape0.Witnesses ℓ
  shape0 : (x0 x1 : ℕ) → Canonical ((var x0) , (var x1)) → Adequate {ℓ} ((var x0) , (var x1)) → ⊥
  shape0 0 1 normal adequate = W0.cut1  adequate
  shape0 0 (suc (suc x1)) normal adequate = false≢true normal
  shape0 (suc x0) x1 normal adequate = false≢true normal
