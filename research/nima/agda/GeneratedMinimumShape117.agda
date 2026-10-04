{-# OPTIONS --safe --cubical --guardedness #-}
module GeneratedMinimumShape117 where
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
  holds1489 : (z0 z1 z2 z3 z4 z5 z6 : A0) → (mul0 z0 z1) ≡ (mul0 (mul0 (mul0 z2 z3) (mul0 z4 z5)) z6)
  holds1489 z0 z1 z2 z3 z4 z5 z6 = refl
  cut1489 : (x0 x1 x2 x3 x4 x5 x6 : ℕ) → Adequate {ℓ} ((op (var x0) (var x1)) , (op (op (op (var x2) (var x3)) (op (var x4) (var x5))) (var x6))) → ⊥
  cut1489 x0 x1 x2 x3 x4 x5 x6 = reject0 ((op (var x0) (var x1)) , (op (op (op (var x2) (var x3)) (op (var x4) (var x5))) (var x6))) (λ env → holds1489 (env x0) (env x1) (env x2) (env x3) (env x4) (env x5) (env x6))
