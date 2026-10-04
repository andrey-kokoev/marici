{-# OPTIONS --safe --cubical --guardedness #-}
module GeneratedMinimumShape5 where
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
  holds6 : (z0 z1 z2 z3 : A0) → (mul0 z0 z1) ≡ (mul0 z2 z3)
  holds6 z0 z1 z2 z3 = refl
  cut6 : (x0 x1 x2 x3 : ℕ) → Adequate {ℓ} ((op (var x0) (var x1)) , (op (var x2) (var x3))) → ⊥
  cut6 x0 x1 x2 x3 = reject0 ((op (var x0) (var x1)) , (op (var x2) (var x3))) (λ env → holds6 (env x0) (env x1) (env x2) (env x3))
