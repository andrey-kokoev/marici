{-# OPTIONS --safe --cubical --guardedness #-}
module GeneratedMinimumShape29 where
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
  holds115 : (z0 z1 z2 z3 z4 : A2) → z0 ≡ (mul2 (mul2 z0 (mul2 z1 z2)) (mul2 z3 z4))
  holds115 z0 z1 z2 z3 z4 = refl
  cut115 : (x2 x3 x4 x5 : ℕ) → Adequate {ℓ} ((var 0) , (op (op (var 0) (op (var x2) (var x3))) (op (var x4) (var x5)))) → ⊥
  cut115 x2 x3 x4 x5 = reject2 ((var 0) , (op (op (var 0) (op (var x2) (var x3))) (op (var x4) (var x5)))) (λ env → holds115 (env 0) (env x2) (env x3) (env x4) (env x5))
  env0 : ℕ → Two
  env0 zero = b0
  env0 (suc zero) = b1
  env0 (suc (suc rest)) = b0
  bad116 : (z2 z3 z4 : Two) → PathP (λ _ → Two) b0 (bop (bop b1 (bop b0 z2)) (bop z3 z4)) → ⊥
  bad116 z2 z3 z4 p = false≢true (cong lower p)
  cut116 : (x3 x4 x5 : ℕ) → Adequate {ℓ} ((var 0) , (op (op (var 1) (op (var 0) (var x3))) (op (var x4) (var x5)))) → ⊥
  cut116 x3 x4 x5 adequate = bad116 (env0 x3) (env0 x4) (env0 x5) (Adequate.valid adequate Two boolean env0)
  bad117 : (z2 z3 : Two) → PathP (λ _ → Two) b0 (bop (bop b1 (bop b1 b0)) (bop z2 z3)) → ⊥
  bad117 z2 z3 p = false≢true (cong lower p)
  cut117 : (x4 x5 : ℕ) → Adequate {ℓ} ((var 0) , (op (op (var 1) (op (var 1) (var 0))) (op (var x4) (var x5)))) → ⊥
  cut117 x4 x5 adequate = bad117 (env0 x4) (env0 x5) (Adequate.valid adequate Two boolean env0)
  holds118 : (z0 z1 : A3) → z0 ≡ (mul3 (mul3 z1 (mul3 z1 z1)) (mul3 z0 z0))
  holds118 z0 z1 = refl
  cut118 : Adequate {ℓ} ((var 0) , (op (op (var 1) (op (var 1) (var 1))) (op (var 0) (var 0)))) → ⊥
  cut118  = reject3 ((var 0) , (op (op (var 1) (op (var 1) (var 1))) (op (var 0) (var 0)))) (λ env → holds118 (env 0) (env 1))
  env1 : ℕ → Two
  env1 zero = b1
  env1 (suc zero) = b0
  env1 (suc (suc rest)) = b0
  bad119 : PathP (λ _ → Two) b1 (bop (bop b0 (bop b0 b0)) (bop b1 b0)) → ⊥
  bad119  p = false≢true (sym (cong lower p))
  cut119 : Adequate {ℓ} ((var 0) , (op (op (var 1) (op (var 1) (var 1))) (op (var 0) (var 1)))) → ⊥
  cut119  adequate = bad119  (Adequate.valid adequate Two boolean env1)
  env2 : ℕ → Two
  env2 zero = b1
  env2 (suc zero) = b0
  env2 (suc (suc zero)) = b0
  env2 (suc (suc (suc rest))) = b0
  bad120 : PathP (λ _ → Two) b1 (bop (bop b0 (bop b0 b0)) (bop b1 b0)) → ⊥
  bad120  p = false≢true (sym (cong lower p))
  cut120 : Adequate {ℓ} ((var 0) , (op (op (var 1) (op (var 1) (var 1))) (op (var 0) (var 2)))) → ⊥
  cut120  adequate = bad120  (Adequate.valid adequate Two boolean env2)
  bad121 : (z2 : Two) → PathP (λ _ → Two) b1 (bop (bop b0 (bop b0 b0)) (bop b0 z2)) → ⊥
  bad121 z2 p = false≢true (sym (cong lower p))
  cut121 : (x5 : ℕ) → Adequate {ℓ} ((var 0) , (op (op (var 1) (op (var 1) (var 1))) (op (var 1) (var x5)))) → ⊥
  cut121 x5 adequate = bad121 (env1 x5) (Adequate.valid adequate Two boolean env1)
  bad122 : (z3 : Two) → PathP (λ _ → Two) b1 (bop (bop b0 (bop b0 b0)) (bop b0 z3)) → ⊥
  bad122 z3 p = false≢true (sym (cong lower p))
  cut122 : (x5 : ℕ) → Adequate {ℓ} ((var 0) , (op (op (var 1) (op (var 1) (var 1))) (op (var 2) (var x5)))) → ⊥
  cut122 x5 adequate = bad122 (env2 x5) (Adequate.valid adequate Two boolean env2)
  env3 : ℕ → Two
  env3 zero = b0
  env3 (suc zero) = b1
  env3 (suc (suc zero)) = b0
  env3 (suc (suc (suc rest))) = b0
  bad123 : (z3 z4 : Two) → PathP (λ _ → Two) b0 (bop (bop b1 (bop b1 b0)) (bop z3 z4)) → ⊥
  bad123 z3 z4 p = false≢true (cong lower p)
  cut123 : (x4 x5 : ℕ) → Adequate {ℓ} ((var 0) , (op (op (var 1) (op (var 1) (var 2))) (op (var x4) (var x5)))) → ⊥
  cut123 x4 x5 adequate = bad123 (env3 x4) (env3 x5) (Adequate.valid adequate Two boolean env3)
  bad124 : (z3 z4 z5 : Two) → PathP (λ _ → Two) b0 (bop (bop b1 (bop b0 z3)) (bop z4 z5)) → ⊥
  bad124 z3 z4 z5 p = false≢true (cong lower p)
  cut124 : (x3 x4 x5 : ℕ) → Adequate {ℓ} ((var 0) , (op (op (var 1) (op (var 2) (var x3))) (op (var x4) (var x5)))) → ⊥
  cut124 x3 x4 x5 adequate = bad124 (env3 x3) (env3 x4) (env3 x5) (Adequate.valid adequate Two boolean env3)
