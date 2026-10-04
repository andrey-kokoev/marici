{-# OPTIONS --safe --cubical --guardedness #-}
module GeneratedMinimumShape124 where
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
module Witnesses (ℓ : Level) where
  open Support ℓ
  cut1496 : (x0 x1 x2 x3 x4 x5 x6 : ℕ) → Adequate {ℓ} ((op (var x0) (op (var x1) (var x2))) , (op (op (op (var x3) (var x4)) (var x5)) (var x6))) → ⊥
  cut1496 x0 x1 x2 x3 x4 x5 x6 adequate = false≢true (sym (cong lower (Adequate.valid adequate Two boolean all1)))
