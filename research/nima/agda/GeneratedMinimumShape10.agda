{-# OPTIONS --safe --cubical --guardedness #-}
module GeneratedMinimumShape10 where
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
  holds11 : (z0 z1 z2 z3 : A2) → z0 ≡ (mul2 (mul2 z0 z1) (mul2 z2 z3))
  holds11 z0 z1 z2 z3 = refl
  cut11 : (x2 x3 x4 : ℕ) → Adequate {ℓ} ((var 0) , (op (op (var 0) (var x2)) (op (var x3) (var x4)))) → ⊥
  cut11 x2 x3 x4 = reject2 ((var 0) , (op (op (var 0) (var x2)) (op (var x3) (var x4)))) (λ env → holds11 (env 0) (env x2) (env x3) (env x4))
  holds12 : (z0 z1 z2 : A13) → z0 ≡ (mul13 (mul13 z1 z0) (mul13 z0 z2))
  holds12 m13c0 m13c0 m13c0 = refl
  holds12 m13c0 m13c0 m13c1 = refl
  holds12 m13c0 m13c0 m13c2 = refl
  holds12 m13c0 m13c0 m13c3 = refl
  holds12 m13c0 m13c1 m13c0 = refl
  holds12 m13c0 m13c1 m13c1 = refl
  holds12 m13c0 m13c1 m13c2 = refl
  holds12 m13c0 m13c1 m13c3 = refl
  holds12 m13c0 m13c2 m13c0 = refl
  holds12 m13c0 m13c2 m13c1 = refl
  holds12 m13c0 m13c2 m13c2 = refl
  holds12 m13c0 m13c2 m13c3 = refl
  holds12 m13c0 m13c3 m13c0 = refl
  holds12 m13c0 m13c3 m13c1 = refl
  holds12 m13c0 m13c3 m13c2 = refl
  holds12 m13c0 m13c3 m13c3 = refl
  holds12 m13c1 m13c0 m13c0 = refl
  holds12 m13c1 m13c0 m13c1 = refl
  holds12 m13c1 m13c0 m13c2 = refl
  holds12 m13c1 m13c0 m13c3 = refl
  holds12 m13c1 m13c1 m13c0 = refl
  holds12 m13c1 m13c1 m13c1 = refl
  holds12 m13c1 m13c1 m13c2 = refl
  holds12 m13c1 m13c1 m13c3 = refl
  holds12 m13c1 m13c2 m13c0 = refl
  holds12 m13c1 m13c2 m13c1 = refl
  holds12 m13c1 m13c2 m13c2 = refl
  holds12 m13c1 m13c2 m13c3 = refl
  holds12 m13c1 m13c3 m13c0 = refl
  holds12 m13c1 m13c3 m13c1 = refl
  holds12 m13c1 m13c3 m13c2 = refl
  holds12 m13c1 m13c3 m13c3 = refl
  holds12 m13c2 m13c0 m13c0 = refl
  holds12 m13c2 m13c0 m13c1 = refl
  holds12 m13c2 m13c0 m13c2 = refl
  holds12 m13c2 m13c0 m13c3 = refl
  holds12 m13c2 m13c1 m13c0 = refl
  holds12 m13c2 m13c1 m13c1 = refl
  holds12 m13c2 m13c1 m13c2 = refl
  holds12 m13c2 m13c1 m13c3 = refl
  holds12 m13c2 m13c2 m13c0 = refl
  holds12 m13c2 m13c2 m13c1 = refl
  holds12 m13c2 m13c2 m13c2 = refl
  holds12 m13c2 m13c2 m13c3 = refl
  holds12 m13c2 m13c3 m13c0 = refl
  holds12 m13c2 m13c3 m13c1 = refl
  holds12 m13c2 m13c3 m13c2 = refl
  holds12 m13c2 m13c3 m13c3 = refl
  holds12 m13c3 m13c0 m13c0 = refl
  holds12 m13c3 m13c0 m13c1 = refl
  holds12 m13c3 m13c0 m13c2 = refl
  holds12 m13c3 m13c0 m13c3 = refl
  holds12 m13c3 m13c1 m13c0 = refl
  holds12 m13c3 m13c1 m13c1 = refl
  holds12 m13c3 m13c1 m13c2 = refl
  holds12 m13c3 m13c1 m13c3 = refl
  holds12 m13c3 m13c2 m13c0 = refl
  holds12 m13c3 m13c2 m13c1 = refl
  holds12 m13c3 m13c2 m13c2 = refl
  holds12 m13c3 m13c2 m13c3 = refl
  holds12 m13c3 m13c3 m13c0 = refl
  holds12 m13c3 m13c3 m13c1 = refl
  holds12 m13c3 m13c3 m13c2 = refl
  holds12 m13c3 m13c3 m13c3 = refl
  cut12 : (x4 : ℕ) → Adequate {ℓ} ((var 0) , (op (op (var 1) (var 0)) (op (var 0) (var x4)))) → ⊥
  cut12 x4 = reject13 ((var 0) , (op (op (var 1) (var 0)) (op (var 0) (var x4)))) (λ env → holds12 (env 0) (env 1) (env x4))
  env0 : ℕ → Two
  env0 zero = b1
  env0 (suc zero) = b0
  env0 (suc (suc rest)) = b0
  bad13 : (z2 : Two) → PathP (λ _ → Two) b1 (bop (bop b0 b1) (bop b0 z2)) → ⊥
  bad13 z2 p = false≢true (sym (cong lower p))
  cut13 : (x4 : ℕ) → Adequate {ℓ} ((var 0) , (op (op (var 1) (var 0)) (op (var 1) (var x4)))) → ⊥
  cut13 x4 adequate = bad13 (env0 x4) (Adequate.valid adequate Two boolean env0)
  env1 : ℕ → Two
  env1 zero = b1
  env1 (suc zero) = b0
  env1 (suc (suc zero)) = b0
  env1 (suc (suc (suc rest))) = b0
  bad14 : (z3 : Two) → PathP (λ _ → Two) b1 (bop (bop b0 b1) (bop b0 z3)) → ⊥
  bad14 z3 p = false≢true (sym (cong lower p))
  cut14 : (x4 : ℕ) → Adequate {ℓ} ((var 0) , (op (op (var 1) (var 0)) (op (var 2) (var x4)))) → ⊥
  cut14 x4 adequate = bad14 (env1 x4) (Adequate.valid adequate Two boolean env1)
  env2 : ℕ → Two
  env2 zero = b0
  env2 (suc zero) = b1
  env2 (suc (suc rest)) = b0
  bad15 : (z2 z3 : Two) → PathP (λ _ → Two) b0 (bop (bop b1 b1) (bop z2 z3)) → ⊥
  bad15 z2 z3 p = false≢true (cong lower p)
  cut15 : (x3 x4 : ℕ) → Adequate {ℓ} ((var 0) , (op (op (var 1) (var 1)) (op (var x3) (var x4)))) → ⊥
  cut15 x3 x4 adequate = bad15 (env2 x3) (env2 x4) (Adequate.valid adequate Two boolean env2)
  env3 : ℕ → Two
  env3 zero = b0
  env3 (suc zero) = b1
  env3 (suc (suc zero)) = b1
  env3 (suc (suc (suc rest))) = b0
  bad16 : (z3 z4 : Two) → PathP (λ _ → Two) b0 (bop (bop b1 b1) (bop z3 z4)) → ⊥
  bad16 z3 z4 p = false≢true (cong lower p)
  cut16 : (x3 x4 : ℕ) → Adequate {ℓ} ((var 0) , (op (op (var 1) (var 2)) (op (var x3) (var x4)))) → ⊥
  cut16 x3 x4 adequate = bad16 (env3 x3) (env3 x4) (Adequate.valid adequate Two boolean env3)
