{-# OPTIONS --safe --cubical --guardedness #-}
module GeneratedMinimumShape27 where
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
  holds84 : (z0 z1 z2 z3 z4 : A2) → z0 ≡ (mul2 (mul2 z0 z1) (mul2 z2 (mul2 z3 z4)))
  holds84 z0 z1 z2 z3 z4 = refl
  cut84 : (x2 x3 x4 x5 : ℕ) → Adequate {ℓ} ((var 0) , (op (op (var 0) (var x2)) (op (var x3) (op (var x4) (var x5))))) → ⊥
  cut84 x2 x3 x4 x5 = reject2 ((var 0) , (op (op (var 0) (var x2)) (op (var x3) (op (var x4) (var x5))))) (λ env → holds84 (env 0) (env x2) (env x3) (env x4) (env x5))
  holds85 : (z0 z1 z2 z3 : A13) → z0 ≡ (mul13 (mul13 z1 z0) (mul13 z0 (mul13 z2 z3)))
  holds85 m13c0 m13c0 m13c0 m13c0 = refl
  holds85 m13c0 m13c0 m13c0 m13c1 = refl
  holds85 m13c0 m13c0 m13c0 m13c2 = refl
  holds85 m13c0 m13c0 m13c0 m13c3 = refl
  holds85 m13c0 m13c0 m13c1 m13c0 = refl
  holds85 m13c0 m13c0 m13c1 m13c1 = refl
  holds85 m13c0 m13c0 m13c1 m13c2 = refl
  holds85 m13c0 m13c0 m13c1 m13c3 = refl
  holds85 m13c0 m13c0 m13c2 m13c0 = refl
  holds85 m13c0 m13c0 m13c2 m13c1 = refl
  holds85 m13c0 m13c0 m13c2 m13c2 = refl
  holds85 m13c0 m13c0 m13c2 m13c3 = refl
  holds85 m13c0 m13c0 m13c3 m13c0 = refl
  holds85 m13c0 m13c0 m13c3 m13c1 = refl
  holds85 m13c0 m13c0 m13c3 m13c2 = refl
  holds85 m13c0 m13c0 m13c3 m13c3 = refl
  holds85 m13c0 m13c1 m13c0 m13c0 = refl
  holds85 m13c0 m13c1 m13c0 m13c1 = refl
  holds85 m13c0 m13c1 m13c0 m13c2 = refl
  holds85 m13c0 m13c1 m13c0 m13c3 = refl
  holds85 m13c0 m13c1 m13c1 m13c0 = refl
  holds85 m13c0 m13c1 m13c1 m13c1 = refl
  holds85 m13c0 m13c1 m13c1 m13c2 = refl
  holds85 m13c0 m13c1 m13c1 m13c3 = refl
  holds85 m13c0 m13c1 m13c2 m13c0 = refl
  holds85 m13c0 m13c1 m13c2 m13c1 = refl
  holds85 m13c0 m13c1 m13c2 m13c2 = refl
  holds85 m13c0 m13c1 m13c2 m13c3 = refl
  holds85 m13c0 m13c1 m13c3 m13c0 = refl
  holds85 m13c0 m13c1 m13c3 m13c1 = refl
  holds85 m13c0 m13c1 m13c3 m13c2 = refl
  holds85 m13c0 m13c1 m13c3 m13c3 = refl
  holds85 m13c0 m13c2 m13c0 m13c0 = refl
  holds85 m13c0 m13c2 m13c0 m13c1 = refl
  holds85 m13c0 m13c2 m13c0 m13c2 = refl
  holds85 m13c0 m13c2 m13c0 m13c3 = refl
  holds85 m13c0 m13c2 m13c1 m13c0 = refl
  holds85 m13c0 m13c2 m13c1 m13c1 = refl
  holds85 m13c0 m13c2 m13c1 m13c2 = refl
  holds85 m13c0 m13c2 m13c1 m13c3 = refl
  holds85 m13c0 m13c2 m13c2 m13c0 = refl
  holds85 m13c0 m13c2 m13c2 m13c1 = refl
  holds85 m13c0 m13c2 m13c2 m13c2 = refl
  holds85 m13c0 m13c2 m13c2 m13c3 = refl
  holds85 m13c0 m13c2 m13c3 m13c0 = refl
  holds85 m13c0 m13c2 m13c3 m13c1 = refl
  holds85 m13c0 m13c2 m13c3 m13c2 = refl
  holds85 m13c0 m13c2 m13c3 m13c3 = refl
  holds85 m13c0 m13c3 m13c0 m13c0 = refl
  holds85 m13c0 m13c3 m13c0 m13c1 = refl
  holds85 m13c0 m13c3 m13c0 m13c2 = refl
  holds85 m13c0 m13c3 m13c0 m13c3 = refl
  holds85 m13c0 m13c3 m13c1 m13c0 = refl
  holds85 m13c0 m13c3 m13c1 m13c1 = refl
  holds85 m13c0 m13c3 m13c1 m13c2 = refl
  holds85 m13c0 m13c3 m13c1 m13c3 = refl
  holds85 m13c0 m13c3 m13c2 m13c0 = refl
  holds85 m13c0 m13c3 m13c2 m13c1 = refl
  holds85 m13c0 m13c3 m13c2 m13c2 = refl
  holds85 m13c0 m13c3 m13c2 m13c3 = refl
  holds85 m13c0 m13c3 m13c3 m13c0 = refl
  holds85 m13c0 m13c3 m13c3 m13c1 = refl
  holds85 m13c0 m13c3 m13c3 m13c2 = refl
  holds85 m13c0 m13c3 m13c3 m13c3 = refl
  holds85 m13c1 m13c0 m13c0 m13c0 = refl
  holds85 m13c1 m13c0 m13c0 m13c1 = refl
  holds85 m13c1 m13c0 m13c0 m13c2 = refl
  holds85 m13c1 m13c0 m13c0 m13c3 = refl
  holds85 m13c1 m13c0 m13c1 m13c0 = refl
  holds85 m13c1 m13c0 m13c1 m13c1 = refl
  holds85 m13c1 m13c0 m13c1 m13c2 = refl
  holds85 m13c1 m13c0 m13c1 m13c3 = refl
  holds85 m13c1 m13c0 m13c2 m13c0 = refl
  holds85 m13c1 m13c0 m13c2 m13c1 = refl
  holds85 m13c1 m13c0 m13c2 m13c2 = refl
  holds85 m13c1 m13c0 m13c2 m13c3 = refl
  holds85 m13c1 m13c0 m13c3 m13c0 = refl
  holds85 m13c1 m13c0 m13c3 m13c1 = refl
  holds85 m13c1 m13c0 m13c3 m13c2 = refl
  holds85 m13c1 m13c0 m13c3 m13c3 = refl
  holds85 m13c1 m13c1 m13c0 m13c0 = refl
  holds85 m13c1 m13c1 m13c0 m13c1 = refl
  holds85 m13c1 m13c1 m13c0 m13c2 = refl
  holds85 m13c1 m13c1 m13c0 m13c3 = refl
  holds85 m13c1 m13c1 m13c1 m13c0 = refl
  holds85 m13c1 m13c1 m13c1 m13c1 = refl
  holds85 m13c1 m13c1 m13c1 m13c2 = refl
  holds85 m13c1 m13c1 m13c1 m13c3 = refl
  holds85 m13c1 m13c1 m13c2 m13c0 = refl
  holds85 m13c1 m13c1 m13c2 m13c1 = refl
  holds85 m13c1 m13c1 m13c2 m13c2 = refl
  holds85 m13c1 m13c1 m13c2 m13c3 = refl
  holds85 m13c1 m13c1 m13c3 m13c0 = refl
  holds85 m13c1 m13c1 m13c3 m13c1 = refl
  holds85 m13c1 m13c1 m13c3 m13c2 = refl
  holds85 m13c1 m13c1 m13c3 m13c3 = refl
  holds85 m13c1 m13c2 m13c0 m13c0 = refl
  holds85 m13c1 m13c2 m13c0 m13c1 = refl
  holds85 m13c1 m13c2 m13c0 m13c2 = refl
  holds85 m13c1 m13c2 m13c0 m13c3 = refl
  holds85 m13c1 m13c2 m13c1 m13c0 = refl
  holds85 m13c1 m13c2 m13c1 m13c1 = refl
  holds85 m13c1 m13c2 m13c1 m13c2 = refl
  holds85 m13c1 m13c2 m13c1 m13c3 = refl
  holds85 m13c1 m13c2 m13c2 m13c0 = refl
  holds85 m13c1 m13c2 m13c2 m13c1 = refl
  holds85 m13c1 m13c2 m13c2 m13c2 = refl
  holds85 m13c1 m13c2 m13c2 m13c3 = refl
  holds85 m13c1 m13c2 m13c3 m13c0 = refl
  holds85 m13c1 m13c2 m13c3 m13c1 = refl
  holds85 m13c1 m13c2 m13c3 m13c2 = refl
  holds85 m13c1 m13c2 m13c3 m13c3 = refl
  holds85 m13c1 m13c3 m13c0 m13c0 = refl
  holds85 m13c1 m13c3 m13c0 m13c1 = refl
  holds85 m13c1 m13c3 m13c0 m13c2 = refl
  holds85 m13c1 m13c3 m13c0 m13c3 = refl
  holds85 m13c1 m13c3 m13c1 m13c0 = refl
  holds85 m13c1 m13c3 m13c1 m13c1 = refl
  holds85 m13c1 m13c3 m13c1 m13c2 = refl
  holds85 m13c1 m13c3 m13c1 m13c3 = refl
  holds85 m13c1 m13c3 m13c2 m13c0 = refl
  holds85 m13c1 m13c3 m13c2 m13c1 = refl
  holds85 m13c1 m13c3 m13c2 m13c2 = refl
  holds85 m13c1 m13c3 m13c2 m13c3 = refl
  holds85 m13c1 m13c3 m13c3 m13c0 = refl
  holds85 m13c1 m13c3 m13c3 m13c1 = refl
  holds85 m13c1 m13c3 m13c3 m13c2 = refl
  holds85 m13c1 m13c3 m13c3 m13c3 = refl
  holds85 m13c2 m13c0 m13c0 m13c0 = refl
  holds85 m13c2 m13c0 m13c0 m13c1 = refl
  holds85 m13c2 m13c0 m13c0 m13c2 = refl
  holds85 m13c2 m13c0 m13c0 m13c3 = refl
  holds85 m13c2 m13c0 m13c1 m13c0 = refl
  holds85 m13c2 m13c0 m13c1 m13c1 = refl
  holds85 m13c2 m13c0 m13c1 m13c2 = refl
  holds85 m13c2 m13c0 m13c1 m13c3 = refl
  holds85 m13c2 m13c0 m13c2 m13c0 = refl
  holds85 m13c2 m13c0 m13c2 m13c1 = refl
  holds85 m13c2 m13c0 m13c2 m13c2 = refl
  holds85 m13c2 m13c0 m13c2 m13c3 = refl
  holds85 m13c2 m13c0 m13c3 m13c0 = refl
  holds85 m13c2 m13c0 m13c3 m13c1 = refl
  holds85 m13c2 m13c0 m13c3 m13c2 = refl
  holds85 m13c2 m13c0 m13c3 m13c3 = refl
  holds85 m13c2 m13c1 m13c0 m13c0 = refl
  holds85 m13c2 m13c1 m13c0 m13c1 = refl
  holds85 m13c2 m13c1 m13c0 m13c2 = refl
  holds85 m13c2 m13c1 m13c0 m13c3 = refl
  holds85 m13c2 m13c1 m13c1 m13c0 = refl
  holds85 m13c2 m13c1 m13c1 m13c1 = refl
  holds85 m13c2 m13c1 m13c1 m13c2 = refl
  holds85 m13c2 m13c1 m13c1 m13c3 = refl
  holds85 m13c2 m13c1 m13c2 m13c0 = refl
  holds85 m13c2 m13c1 m13c2 m13c1 = refl
  holds85 m13c2 m13c1 m13c2 m13c2 = refl
  holds85 m13c2 m13c1 m13c2 m13c3 = refl
  holds85 m13c2 m13c1 m13c3 m13c0 = refl
  holds85 m13c2 m13c1 m13c3 m13c1 = refl
  holds85 m13c2 m13c1 m13c3 m13c2 = refl
  holds85 m13c2 m13c1 m13c3 m13c3 = refl
  holds85 m13c2 m13c2 m13c0 m13c0 = refl
  holds85 m13c2 m13c2 m13c0 m13c1 = refl
  holds85 m13c2 m13c2 m13c0 m13c2 = refl
  holds85 m13c2 m13c2 m13c0 m13c3 = refl
  holds85 m13c2 m13c2 m13c1 m13c0 = refl
  holds85 m13c2 m13c2 m13c1 m13c1 = refl
  holds85 m13c2 m13c2 m13c1 m13c2 = refl
  holds85 m13c2 m13c2 m13c1 m13c3 = refl
  holds85 m13c2 m13c2 m13c2 m13c0 = refl
  holds85 m13c2 m13c2 m13c2 m13c1 = refl
  holds85 m13c2 m13c2 m13c2 m13c2 = refl
  holds85 m13c2 m13c2 m13c2 m13c3 = refl
  holds85 m13c2 m13c2 m13c3 m13c0 = refl
  holds85 m13c2 m13c2 m13c3 m13c1 = refl
  holds85 m13c2 m13c2 m13c3 m13c2 = refl
  holds85 m13c2 m13c2 m13c3 m13c3 = refl
  holds85 m13c2 m13c3 m13c0 m13c0 = refl
  holds85 m13c2 m13c3 m13c0 m13c1 = refl
  holds85 m13c2 m13c3 m13c0 m13c2 = refl
  holds85 m13c2 m13c3 m13c0 m13c3 = refl
  holds85 m13c2 m13c3 m13c1 m13c0 = refl
  holds85 m13c2 m13c3 m13c1 m13c1 = refl
  holds85 m13c2 m13c3 m13c1 m13c2 = refl
  holds85 m13c2 m13c3 m13c1 m13c3 = refl
  holds85 m13c2 m13c3 m13c2 m13c0 = refl
  holds85 m13c2 m13c3 m13c2 m13c1 = refl
  holds85 m13c2 m13c3 m13c2 m13c2 = refl
  holds85 m13c2 m13c3 m13c2 m13c3 = refl
  holds85 m13c2 m13c3 m13c3 m13c0 = refl
  holds85 m13c2 m13c3 m13c3 m13c1 = refl
  holds85 m13c2 m13c3 m13c3 m13c2 = refl
  holds85 m13c2 m13c3 m13c3 m13c3 = refl
  holds85 m13c3 m13c0 m13c0 m13c0 = refl
  holds85 m13c3 m13c0 m13c0 m13c1 = refl
  holds85 m13c3 m13c0 m13c0 m13c2 = refl
  holds85 m13c3 m13c0 m13c0 m13c3 = refl
  holds85 m13c3 m13c0 m13c1 m13c0 = refl
  holds85 m13c3 m13c0 m13c1 m13c1 = refl
  holds85 m13c3 m13c0 m13c1 m13c2 = refl
  holds85 m13c3 m13c0 m13c1 m13c3 = refl
  holds85 m13c3 m13c0 m13c2 m13c0 = refl
  holds85 m13c3 m13c0 m13c2 m13c1 = refl
  holds85 m13c3 m13c0 m13c2 m13c2 = refl
  holds85 m13c3 m13c0 m13c2 m13c3 = refl
  holds85 m13c3 m13c0 m13c3 m13c0 = refl
  holds85 m13c3 m13c0 m13c3 m13c1 = refl
  holds85 m13c3 m13c0 m13c3 m13c2 = refl
  holds85 m13c3 m13c0 m13c3 m13c3 = refl
  holds85 m13c3 m13c1 m13c0 m13c0 = refl
  holds85 m13c3 m13c1 m13c0 m13c1 = refl
  holds85 m13c3 m13c1 m13c0 m13c2 = refl
  holds85 m13c3 m13c1 m13c0 m13c3 = refl
  holds85 m13c3 m13c1 m13c1 m13c0 = refl
  holds85 m13c3 m13c1 m13c1 m13c1 = refl
  holds85 m13c3 m13c1 m13c1 m13c2 = refl
  holds85 m13c3 m13c1 m13c1 m13c3 = refl
  holds85 m13c3 m13c1 m13c2 m13c0 = refl
  holds85 m13c3 m13c1 m13c2 m13c1 = refl
  holds85 m13c3 m13c1 m13c2 m13c2 = refl
  holds85 m13c3 m13c1 m13c2 m13c3 = refl
  holds85 m13c3 m13c1 m13c3 m13c0 = refl
  holds85 m13c3 m13c1 m13c3 m13c1 = refl
  holds85 m13c3 m13c1 m13c3 m13c2 = refl
  holds85 m13c3 m13c1 m13c3 m13c3 = refl
  holds85 m13c3 m13c2 m13c0 m13c0 = refl
  holds85 m13c3 m13c2 m13c0 m13c1 = refl
  holds85 m13c3 m13c2 m13c0 m13c2 = refl
  holds85 m13c3 m13c2 m13c0 m13c3 = refl
  holds85 m13c3 m13c2 m13c1 m13c0 = refl
  holds85 m13c3 m13c2 m13c1 m13c1 = refl
  holds85 m13c3 m13c2 m13c1 m13c2 = refl
  holds85 m13c3 m13c2 m13c1 m13c3 = refl
  holds85 m13c3 m13c2 m13c2 m13c0 = refl
  holds85 m13c3 m13c2 m13c2 m13c1 = refl
  holds85 m13c3 m13c2 m13c2 m13c2 = refl
  holds85 m13c3 m13c2 m13c2 m13c3 = refl
  holds85 m13c3 m13c2 m13c3 m13c0 = refl
  holds85 m13c3 m13c2 m13c3 m13c1 = refl
  holds85 m13c3 m13c2 m13c3 m13c2 = refl
  holds85 m13c3 m13c2 m13c3 m13c3 = refl
  holds85 m13c3 m13c3 m13c0 m13c0 = refl
  holds85 m13c3 m13c3 m13c0 m13c1 = refl
  holds85 m13c3 m13c3 m13c0 m13c2 = refl
  holds85 m13c3 m13c3 m13c0 m13c3 = refl
  holds85 m13c3 m13c3 m13c1 m13c0 = refl
  holds85 m13c3 m13c3 m13c1 m13c1 = refl
  holds85 m13c3 m13c3 m13c1 m13c2 = refl
  holds85 m13c3 m13c3 m13c1 m13c3 = refl
  holds85 m13c3 m13c3 m13c2 m13c0 = refl
  holds85 m13c3 m13c3 m13c2 m13c1 = refl
  holds85 m13c3 m13c3 m13c2 m13c2 = refl
  holds85 m13c3 m13c3 m13c2 m13c3 = refl
  holds85 m13c3 m13c3 m13c3 m13c0 = refl
  holds85 m13c3 m13c3 m13c3 m13c1 = refl
  holds85 m13c3 m13c3 m13c3 m13c2 = refl
  holds85 m13c3 m13c3 m13c3 m13c3 = refl
  cut85 : (x4 x5 : ℕ) → Adequate {ℓ} ((var 0) , (op (op (var 1) (var 0)) (op (var 0) (op (var x4) (var x5))))) → ⊥
  cut85 x4 x5 = reject13 ((var 0) , (op (op (var 1) (var 0)) (op (var 0) (op (var x4) (var x5))))) (λ env → holds85 (env 0) (env 1) (env x4) (env x5))
  env0 : ℕ → Two
  env0 zero = b1
  env0 (suc zero) = b0
  env0 (suc (suc rest)) = b0
  bad86 : (z2 z3 : Two) → PathP (λ _ → Two) b1 (bop (bop b0 b1) (bop b0 (bop z2 z3))) → ⊥
  bad86 z2 z3 p = false≢true (sym (cong lower p))
  cut86 : (x4 x5 : ℕ) → Adequate {ℓ} ((var 0) , (op (op (var 1) (var 0)) (op (var 1) (op (var x4) (var x5))))) → ⊥
  cut86 x4 x5 adequate = bad86 (env0 x4) (env0 x5) (Adequate.valid adequate Two boolean env0)
  env1 : ℕ → Two
  env1 zero = b1
  env1 (suc zero) = b0
  env1 (suc (suc zero)) = b0
  env1 (suc (suc (suc rest))) = b0
  bad87 : (z3 z4 : Two) → PathP (λ _ → Two) b1 (bop (bop b0 b1) (bop b0 (bop z3 z4))) → ⊥
  bad87 z3 z4 p = false≢true (sym (cong lower p))
  cut87 : (x4 x5 : ℕ) → Adequate {ℓ} ((var 0) , (op (op (var 1) (var 0)) (op (var 2) (op (var x4) (var x5))))) → ⊥
  cut87 x4 x5 adequate = bad87 (env1 x4) (env1 x5) (Adequate.valid adequate Two boolean env1)
  env2 : ℕ → Two
  env2 zero = b0
  env2 (suc zero) = b1
  env2 (suc (suc rest)) = b0
  bad88 : (z2 z3 z4 : Two) → PathP (λ _ → Two) b0 (bop (bop b1 b1) (bop z2 (bop z3 z4))) → ⊥
  bad88 z2 z3 z4 p = false≢true (cong lower p)
  cut88 : (x3 x4 x5 : ℕ) → Adequate {ℓ} ((var 0) , (op (op (var 1) (var 1)) (op (var x3) (op (var x4) (var x5))))) → ⊥
  cut88 x3 x4 x5 adequate = bad88 (env2 x3) (env2 x4) (env2 x5) (Adequate.valid adequate Two boolean env2)
  env3 : ℕ → Two
  env3 zero = b0
  env3 (suc zero) = b1
  env3 (suc (suc zero)) = b1
  env3 (suc (suc (suc rest))) = b0
  bad89 : (z3 z4 z5 : Two) → PathP (λ _ → Two) b0 (bop (bop b1 b1) (bop z3 (bop z4 z5))) → ⊥
  bad89 z3 z4 z5 p = false≢true (cong lower p)
  cut89 : (x3 x4 x5 : ℕ) → Adequate {ℓ} ((var 0) , (op (op (var 1) (var 2)) (op (var x3) (op (var x4) (var x5))))) → ⊥
  cut89 x3 x4 x5 adequate = bad89 (env3 x3) (env3 x4) (env3 x5) (Adequate.valid adequate Two boolean env3)
