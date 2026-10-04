{-# OPTIONS --safe --cubical --guardedness #-}
module GeneratedMinimumShape0 where
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
  holds0 : (z0 : A0) → z0 ≡ z0
  holds0 z0 = refl
  cut0 : Adequate {ℓ} ((var 0) , (var 0)) → ⊥
  cut0  = reject0 ((var 0) , (var 0)) (λ env → holds0 (env 0))
  env0 : ℕ → Two
  env0 zero = b0
  env0 (suc zero) = b1
  env0 (suc (suc rest)) = b0
  bad1 : PathP (λ _ → Two) b0 b1 → ⊥
  bad1  p = false≢true (cong lower p)
  cut1 : Adequate {ℓ} ((var 0) , (var 1)) → ⊥
  cut1  adequate = bad1  (Adequate.valid adequate Two boolean env0)
