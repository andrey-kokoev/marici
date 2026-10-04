{-# OPTIONS --safe --cubical --guardedness #-}
module GeneratedMinimumShape172 where
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
  holds4172 : (z0 : A1) → (mul1 (mul1 z0 z0) (mul1 (mul1 (mul1 z0 z0) z0) z0)) ≡ z0
  holds4172 m1c0 = refl
  holds4172 m1c1 = refl
  cut4172 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (op (op (var 0) (var 0)) (var 0)) (var 0))) , (var 0)) → ⊥
  cut4172  = reject1 ((op (op (var 0) (var 0)) (op (op (op (var 0) (var 0)) (var 0)) (var 0))) , (var 0)) (λ env → holds4172 (env 0))
  env0 : ℕ → Two
  env0 zero = b0
  env0 (suc zero) = b1
  env0 (suc (suc rest)) = b0
  bad4173 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop (bop b0 b0) b0) b0)) b1 → ⊥
  bad4173  p = false≢true (cong lower p)
  cut4173 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (op (op (var 0) (var 0)) (var 0)) (var 0))) , (var 1)) → ⊥
  cut4173  adequate = bad4173  (Adequate.valid adequate Two boolean env0)
  bad4174 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop (bop b0 b0) b0) b1)) b0 → ⊥
  bad4174  p = false≢true (sym (cong lower p))
  cut4174 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (op (op (var 0) (var 0)) (var 0)) (var 1))) , (var 0)) → ⊥
  cut4174  adequate = bad4174  (Adequate.valid adequate Two boolean env0)
  env1 : ℕ → Two
  env1 zero = b1
  env1 (suc zero) = b0
  env1 (suc (suc rest)) = b0
  bad4175 : PathP (λ _ → Two) (bop (bop b1 b1) (bop (bop (bop b1 b1) b1) b0)) b0 → ⊥
  bad4175  p = false≢true (sym (cong lower p))
  cut4175 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (op (op (var 0) (var 0)) (var 0)) (var 1))) , (var 1)) → ⊥
  cut4175  adequate = bad4175  (Adequate.valid adequate Two boolean env1)
  env2 : ℕ → Two
  env2 zero = b0
  env2 (suc zero) = b0
  env2 (suc (suc zero)) = b1
  env2 (suc (suc (suc rest))) = b0
  bad4176 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop (bop b0 b0) b0) b0)) b1 → ⊥
  bad4176  p = false≢true (cong lower p)
  cut4176 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (op (op (var 0) (var 0)) (var 0)) (var 1))) , (var 2)) → ⊥
  cut4176  adequate = bad4176  (Adequate.valid adequate Two boolean env2)
  holds4177 : (z0 z1 : A2) → (mul2 (mul2 z0 z0) (mul2 (mul2 (mul2 z0 z0) z1) z0)) ≡ z0
  holds4177 z0 z1 = refl
  cut4177 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (op (op (var 0) (var 0)) (var 1)) (var 0))) , (var 0)) → ⊥
  cut4177  = reject2 ((op (op (var 0) (var 0)) (op (op (op (var 0) (var 0)) (var 1)) (var 0))) , (var 0)) (λ env → holds4177 (env 0) (env 1))
  bad4178 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop (bop b0 b0) b1) b0)) b1 → ⊥
  bad4178  p = false≢true (cong lower p)
  cut4178 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (op (op (var 0) (var 0)) (var 1)) (var 0))) , (var 1)) → ⊥
  cut4178  adequate = bad4178  (Adequate.valid adequate Two boolean env0)
  bad4179 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop (bop b0 b0) b0) b0)) b1 → ⊥
  bad4179  p = false≢true (cong lower p)
  cut4179 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (op (op (var 0) (var 0)) (var 1)) (var 0))) , (var 2)) → ⊥
  cut4179  adequate = bad4179  (Adequate.valid adequate Two boolean env2)
  holds4180 : (z0 z1 : A2) → (mul2 (mul2 z0 z0) (mul2 (mul2 (mul2 z0 z0) z1) z1)) ≡ z0
  holds4180 z0 z1 = refl
  cut4180 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (op (op (var 0) (var 0)) (var 1)) (var 1))) , (var 0)) → ⊥
  cut4180  = reject2 ((op (op (var 0) (var 0)) (op (op (op (var 0) (var 0)) (var 1)) (var 1))) , (var 0)) (λ env → holds4180 (env 0) (env 1))
  bad4181 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop (bop b0 b0) b1) b1)) b1 → ⊥
  bad4181  p = false≢true (cong lower p)
  cut4181 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (op (op (var 0) (var 0)) (var 1)) (var 1))) , (var 1)) → ⊥
  cut4181  adequate = bad4181  (Adequate.valid adequate Two boolean env0)
  bad4182 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop (bop b0 b0) b0) b0)) b1 → ⊥
  bad4182  p = false≢true (cong lower p)
  cut4182 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (op (op (var 0) (var 0)) (var 1)) (var 1))) , (var 2)) → ⊥
  cut4182  adequate = bad4182  (Adequate.valid adequate Two boolean env2)
  bad4183 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop (bop b0 b0) b0) b1)) b0 → ⊥
  bad4183  p = false≢true (sym (cong lower p))
  cut4183 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (op (op (var 0) (var 0)) (var 1)) (var 2))) , (var 0)) → ⊥
  cut4183  adequate = bad4183  (Adequate.valid adequate Two boolean env2)
  bad4184 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop (bop b0 b0) b0) b1)) b0 → ⊥
  bad4184  p = false≢true (sym (cong lower p))
  cut4184 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (op (op (var 0) (var 0)) (var 1)) (var 2))) , (var 1)) → ⊥
  cut4184  adequate = bad4184  (Adequate.valid adequate Two boolean env2)
  env3 : ℕ → Two
  env3 zero = b0
  env3 (suc zero) = b1
  env3 (suc (suc zero)) = b1
  env3 (suc (suc (suc rest))) = b0
  bad4185 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop (bop b0 b0) b1) b1)) b1 → ⊥
  bad4185  p = false≢true (cong lower p)
  cut4185 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (op (op (var 0) (var 0)) (var 1)) (var 2))) , (var 2)) → ⊥
  cut4185  adequate = bad4185  (Adequate.valid adequate Two boolean env3)
  env4 : ℕ → Two
  env4 zero = b0
  env4 (suc zero) = b0
  env4 (suc (suc zero)) = b0
  env4 (suc (suc (suc zero))) = b1
  env4 (suc (suc (suc (suc rest)))) = b0
  bad4186 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop (bop b0 b0) b0) b0)) b1 → ⊥
  bad4186  p = false≢true (cong lower p)
  cut4186 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (op (op (var 0) (var 0)) (var 1)) (var 2))) , (var 3)) → ⊥
  cut4186  adequate = bad4186  (Adequate.valid adequate Two boolean env4)
  holds4187 : (z0 z1 : A2) → (mul2 (mul2 z0 z0) (mul2 (mul2 (mul2 z0 z1) z0) z0)) ≡ z0
  holds4187 z0 z1 = refl
  cut4187 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (op (op (var 0) (var 1)) (var 0)) (var 0))) , (var 0)) → ⊥
  cut4187  = reject2 ((op (op (var 0) (var 0)) (op (op (op (var 0) (var 1)) (var 0)) (var 0))) , (var 0)) (λ env → holds4187 (env 0) (env 1))
  bad4188 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop (bop b0 b1) b0) b0)) b1 → ⊥
  bad4188  p = false≢true (cong lower p)
  cut4188 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (op (op (var 0) (var 1)) (var 0)) (var 0))) , (var 1)) → ⊥
  cut4188  adequate = bad4188  (Adequate.valid adequate Two boolean env0)
  bad4189 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop (bop b0 b0) b0) b0)) b1 → ⊥
  bad4189  p = false≢true (cong lower p)
  cut4189 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (op (op (var 0) (var 1)) (var 0)) (var 0))) , (var 2)) → ⊥
  cut4189  adequate = bad4189  (Adequate.valid adequate Two boolean env2)
  bad4190 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop (bop b0 b1) b0) b1)) b0 → ⊥
  bad4190  p = false≢true (sym (cong lower p))
  cut4190 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (op (op (var 0) (var 1)) (var 0)) (var 1))) , (var 0)) → ⊥
  cut4190  adequate = bad4190  (Adequate.valid adequate Two boolean env0)
  bad4191 : PathP (λ _ → Two) (bop (bop b1 b1) (bop (bop (bop b1 b0) b1) b0)) b0 → ⊥
  bad4191  p = false≢true (sym (cong lower p))
  cut4191 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (op (op (var 0) (var 1)) (var 0)) (var 1))) , (var 1)) → ⊥
  cut4191  adequate = bad4191  (Adequate.valid adequate Two boolean env1)
  bad4192 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop (bop b0 b0) b0) b0)) b1 → ⊥
  bad4192  p = false≢true (cong lower p)
  cut4192 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (op (op (var 0) (var 1)) (var 0)) (var 1))) , (var 2)) → ⊥
  cut4192  adequate = bad4192  (Adequate.valid adequate Two boolean env2)
  bad4193 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop (bop b0 b0) b0) b1)) b0 → ⊥
  bad4193  p = false≢true (sym (cong lower p))
  cut4193 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (op (op (var 0) (var 1)) (var 0)) (var 2))) , (var 0)) → ⊥
  cut4193  adequate = bad4193  (Adequate.valid adequate Two boolean env2)
  bad4194 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop (bop b0 b0) b0) b1)) b0 → ⊥
  bad4194  p = false≢true (sym (cong lower p))
  cut4194 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (op (op (var 0) (var 1)) (var 0)) (var 2))) , (var 1)) → ⊥
  cut4194  adequate = bad4194  (Adequate.valid adequate Two boolean env2)
  env5 : ℕ → Two
  env5 zero = b1
  env5 (suc zero) = b0
  env5 (suc (suc zero)) = b0
  env5 (suc (suc (suc rest))) = b0
  bad4195 : PathP (λ _ → Two) (bop (bop b1 b1) (bop (bop (bop b1 b0) b1) b0)) b0 → ⊥
  bad4195  p = false≢true (sym (cong lower p))
  cut4195 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (op (op (var 0) (var 1)) (var 0)) (var 2))) , (var 2)) → ⊥
  cut4195  adequate = bad4195  (Adequate.valid adequate Two boolean env5)
  bad4196 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop (bop b0 b0) b0) b0)) b1 → ⊥
  bad4196  p = false≢true (cong lower p)
  cut4196 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (op (op (var 0) (var 1)) (var 0)) (var 2))) , (var 3)) → ⊥
  cut4196  adequate = bad4196  (Adequate.valid adequate Two boolean env4)
  holds4197 : (z0 z1 : A2) → (mul2 (mul2 z0 z0) (mul2 (mul2 (mul2 z0 z1) z1) z0)) ≡ z0
  holds4197 z0 z1 = refl
  cut4197 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (op (op (var 0) (var 1)) (var 1)) (var 0))) , (var 0)) → ⊥
  cut4197  = reject2 ((op (op (var 0) (var 0)) (op (op (op (var 0) (var 1)) (var 1)) (var 0))) , (var 0)) (λ env → holds4197 (env 0) (env 1))
  bad4198 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop (bop b0 b1) b1) b0)) b1 → ⊥
  bad4198  p = false≢true (cong lower p)
  cut4198 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (op (op (var 0) (var 1)) (var 1)) (var 0))) , (var 1)) → ⊥
  cut4198  adequate = bad4198  (Adequate.valid adequate Two boolean env0)
  bad4199 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop (bop b0 b0) b0) b0)) b1 → ⊥
  bad4199  p = false≢true (cong lower p)
  cut4199 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (op (op (var 0) (var 1)) (var 1)) (var 0))) , (var 2)) → ⊥
  cut4199  adequate = bad4199  (Adequate.valid adequate Two boolean env2)
  holds4200 : (z0 z1 : A2) → (mul2 (mul2 z0 z0) (mul2 (mul2 (mul2 z0 z1) z1) z1)) ≡ z0
  holds4200 z0 z1 = refl
  cut4200 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (op (op (var 0) (var 1)) (var 1)) (var 1))) , (var 0)) → ⊥
  cut4200  = reject2 ((op (op (var 0) (var 0)) (op (op (op (var 0) (var 1)) (var 1)) (var 1))) , (var 0)) (λ env → holds4200 (env 0) (env 1))
  bad4201 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop (bop b0 b1) b1) b1)) b1 → ⊥
  bad4201  p = false≢true (cong lower p)
  cut4201 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (op (op (var 0) (var 1)) (var 1)) (var 1))) , (var 1)) → ⊥
  cut4201  adequate = bad4201  (Adequate.valid adequate Two boolean env0)
  bad4202 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop (bop b0 b0) b0) b0)) b1 → ⊥
  bad4202  p = false≢true (cong lower p)
  cut4202 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (op (op (var 0) (var 1)) (var 1)) (var 1))) , (var 2)) → ⊥
  cut4202  adequate = bad4202  (Adequate.valid adequate Two boolean env2)
  bad4203 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop (bop b0 b0) b0) b1)) b0 → ⊥
  bad4203  p = false≢true (sym (cong lower p))
  cut4203 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (op (op (var 0) (var 1)) (var 1)) (var 2))) , (var 0)) → ⊥
  cut4203  adequate = bad4203  (Adequate.valid adequate Two boolean env2)
  bad4204 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop (bop b0 b0) b0) b1)) b0 → ⊥
  bad4204  p = false≢true (sym (cong lower p))
  cut4204 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (op (op (var 0) (var 1)) (var 1)) (var 2))) , (var 1)) → ⊥
  cut4204  adequate = bad4204  (Adequate.valid adequate Two boolean env2)
  bad4205 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop (bop b0 b1) b1) b1)) b1 → ⊥
  bad4205  p = false≢true (cong lower p)
  cut4205 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (op (op (var 0) (var 1)) (var 1)) (var 2))) , (var 2)) → ⊥
  cut4205  adequate = bad4205  (Adequate.valid adequate Two boolean env3)
  bad4206 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop (bop b0 b0) b0) b0)) b1 → ⊥
  bad4206  p = false≢true (cong lower p)
  cut4206 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (op (op (var 0) (var 1)) (var 1)) (var 2))) , (var 3)) → ⊥
  cut4206  adequate = bad4206  (Adequate.valid adequate Two boolean env4)
  holds4207 : (z0 z1 z2 : A2) → (mul2 (mul2 z0 z0) (mul2 (mul2 (mul2 z0 z1) z2) z0)) ≡ z0
  holds4207 z0 z1 z2 = refl
  cut4207 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (op (op (var 0) (var 1)) (var 2)) (var 0))) , (var 0)) → ⊥
  cut4207  = reject2 ((op (op (var 0) (var 0)) (op (op (op (var 0) (var 1)) (var 2)) (var 0))) , (var 0)) (λ env → holds4207 (env 0) (env 1) (env 2))
  env6 : ℕ → Two
  env6 zero = b0
  env6 (suc zero) = b1
  env6 (suc (suc zero)) = b0
  env6 (suc (suc (suc rest))) = b0
  bad4208 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop (bop b0 b1) b0) b0)) b1 → ⊥
  bad4208  p = false≢true (cong lower p)
  cut4208 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (op (op (var 0) (var 1)) (var 2)) (var 0))) , (var 1)) → ⊥
  cut4208  adequate = bad4208  (Adequate.valid adequate Two boolean env6)
  bad4209 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop (bop b0 b0) b1) b0)) b1 → ⊥
  bad4209  p = false≢true (cong lower p)
  cut4209 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (op (op (var 0) (var 1)) (var 2)) (var 0))) , (var 2)) → ⊥
  cut4209  adequate = bad4209  (Adequate.valid adequate Two boolean env2)
  bad4210 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop (bop b0 b0) b0) b0)) b1 → ⊥
  bad4210  p = false≢true (cong lower p)
  cut4210 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (op (op (var 0) (var 1)) (var 2)) (var 0))) , (var 3)) → ⊥
  cut4210  adequate = bad4210  (Adequate.valid adequate Two boolean env4)
  bad4211 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop (bop b0 b1) b0) b1)) b0 → ⊥
  bad4211  p = false≢true (sym (cong lower p))
  cut4211 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (op (op (var 0) (var 1)) (var 2)) (var 1))) , (var 0)) → ⊥
  cut4211  adequate = bad4211  (Adequate.valid adequate Two boolean env6)
  bad4212 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop (bop b0 b1) b1) b1)) b1 → ⊥
  bad4212  p = false≢true (cong lower p)
  cut4212 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (op (op (var 0) (var 1)) (var 2)) (var 1))) , (var 1)) → ⊥
  cut4212  adequate = bad4212  (Adequate.valid adequate Two boolean env3)
  bad4213 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop (bop b0 b0) b1) b0)) b1 → ⊥
  bad4213  p = false≢true (cong lower p)
  cut4213 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (op (op (var 0) (var 1)) (var 2)) (var 1))) , (var 2)) → ⊥
  cut4213  adequate = bad4213  (Adequate.valid adequate Two boolean env2)
  bad4214 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop (bop b0 b0) b0) b0)) b1 → ⊥
  bad4214  p = false≢true (cong lower p)
  cut4214 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (op (op (var 0) (var 1)) (var 2)) (var 1))) , (var 3)) → ⊥
  cut4214  adequate = bad4214  (Adequate.valid adequate Two boolean env4)
  holds4215 : (z0 z1 z2 : A2) → (mul2 (mul2 z0 z0) (mul2 (mul2 (mul2 z0 z1) z2) z2)) ≡ z0
  holds4215 z0 z1 z2 = refl
  cut4215 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (op (op (var 0) (var 1)) (var 2)) (var 2))) , (var 0)) → ⊥
  cut4215  = reject2 ((op (op (var 0) (var 0)) (op (op (op (var 0) (var 1)) (var 2)) (var 2))) , (var 0)) (λ env → holds4215 (env 0) (env 1) (env 2))
  bad4216 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop (bop b0 b1) b0) b0)) b1 → ⊥
  bad4216  p = false≢true (cong lower p)
  cut4216 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (op (op (var 0) (var 1)) (var 2)) (var 2))) , (var 1)) → ⊥
  cut4216  adequate = bad4216  (Adequate.valid adequate Two boolean env6)
  bad4217 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop (bop b0 b0) b1) b1)) b1 → ⊥
  bad4217  p = false≢true (cong lower p)
  cut4217 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (op (op (var 0) (var 1)) (var 2)) (var 2))) , (var 2)) → ⊥
  cut4217  adequate = bad4217  (Adequate.valid adequate Two boolean env2)
  bad4218 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop (bop b0 b0) b0) b0)) b1 → ⊥
  bad4218  p = false≢true (cong lower p)
  cut4218 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (op (op (var 0) (var 1)) (var 2)) (var 2))) , (var 3)) → ⊥
  cut4218  adequate = bad4218  (Adequate.valid adequate Two boolean env4)
  bad4219 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop (bop b0 b0) b0) b1)) b0 → ⊥
  bad4219  p = false≢true (sym (cong lower p))
  cut4219 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (op (op (var 0) (var 1)) (var 2)) (var 3))) , (var 0)) → ⊥
  cut4219  adequate = bad4219  (Adequate.valid adequate Two boolean env4)
  bad4220 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop (bop b0 b0) b0) b1)) b0 → ⊥
  bad4220  p = false≢true (sym (cong lower p))
  cut4220 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (op (op (var 0) (var 1)) (var 2)) (var 3))) , (var 1)) → ⊥
  cut4220  adequate = bad4220  (Adequate.valid adequate Two boolean env4)
  bad4221 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop (bop b0 b0) b0) b1)) b0 → ⊥
  bad4221  p = false≢true (sym (cong lower p))
  cut4221 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (op (op (var 0) (var 1)) (var 2)) (var 3))) , (var 2)) → ⊥
  cut4221  adequate = bad4221  (Adequate.valid adequate Two boolean env4)
  env7 : ℕ → Two
  env7 zero = b0
  env7 (suc zero) = b0
  env7 (suc (suc zero)) = b1
  env7 (suc (suc (suc zero))) = b1
  env7 (suc (suc (suc (suc rest)))) = b0
  bad4222 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop (bop b0 b0) b1) b1)) b1 → ⊥
  bad4222  p = false≢true (cong lower p)
  cut4222 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (op (op (var 0) (var 1)) (var 2)) (var 3))) , (var 3)) → ⊥
  cut4222  adequate = bad4222  (Adequate.valid adequate Two boolean env7)
  env8 : ℕ → Two
  env8 zero = b0
  env8 (suc zero) = b0
  env8 (suc (suc zero)) = b0
  env8 (suc (suc (suc zero))) = b0
  env8 (suc (suc (suc (suc zero)))) = b1
  env8 (suc (suc (suc (suc (suc rest))))) = b0
  bad4223 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop (bop b0 b0) b0) b0)) b1 → ⊥
  bad4223  p = false≢true (cong lower p)
  cut4223 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (op (op (var 0) (var 1)) (var 2)) (var 3))) , (var 4)) → ⊥
  cut4223  adequate = bad4223  (Adequate.valid adequate Two boolean env8)
  holds4224 : (z0 z1 : A2) → (mul2 (mul2 z0 z0) (mul2 (mul2 (mul2 z1 z0) z0) z0)) ≡ z0
  holds4224 z0 z1 = refl
  cut4224 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (op (op (var 1) (var 0)) (var 0)) (var 0))) , (var 0)) → ⊥
  cut4224  = reject2 ((op (op (var 0) (var 0)) (op (op (op (var 1) (var 0)) (var 0)) (var 0))) , (var 0)) (λ env → holds4224 (env 0) (env 1))
  bad4225 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop (bop b1 b0) b0) b0)) b1 → ⊥
  bad4225  p = false≢true (cong lower p)
  cut4225 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (op (op (var 1) (var 0)) (var 0)) (var 0))) , (var 1)) → ⊥
  cut4225  adequate = bad4225  (Adequate.valid adequate Two boolean env0)
  bad4226 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop (bop b0 b0) b0) b0)) b1 → ⊥
  bad4226  p = false≢true (cong lower p)
  cut4226 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (op (op (var 1) (var 0)) (var 0)) (var 0))) , (var 2)) → ⊥
  cut4226  adequate = bad4226  (Adequate.valid adequate Two boolean env2)
  bad4227 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop (bop b1 b0) b0) b1)) b0 → ⊥
  bad4227  p = false≢true (sym (cong lower p))
  cut4227 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (op (op (var 1) (var 0)) (var 0)) (var 1))) , (var 0)) → ⊥
  cut4227  adequate = bad4227  (Adequate.valid adequate Two boolean env0)
  bad4228 : PathP (λ _ → Two) (bop (bop b1 b1) (bop (bop (bop b0 b1) b1) b0)) b0 → ⊥
  bad4228  p = false≢true (sym (cong lower p))
  cut4228 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (op (op (var 1) (var 0)) (var 0)) (var 1))) , (var 1)) → ⊥
  cut4228  adequate = bad4228  (Adequate.valid adequate Two boolean env1)
  bad4229 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop (bop b0 b0) b0) b0)) b1 → ⊥
  bad4229  p = false≢true (cong lower p)
  cut4229 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (op (op (var 1) (var 0)) (var 0)) (var 1))) , (var 2)) → ⊥
  cut4229  adequate = bad4229  (Adequate.valid adequate Two boolean env2)
  bad4230 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop (bop b0 b0) b0) b1)) b0 → ⊥
  bad4230  p = false≢true (sym (cong lower p))
  cut4230 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (op (op (var 1) (var 0)) (var 0)) (var 2))) , (var 0)) → ⊥
  cut4230  adequate = bad4230  (Adequate.valid adequate Two boolean env2)
  bad4231 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop (bop b0 b0) b0) b1)) b0 → ⊥
  bad4231  p = false≢true (sym (cong lower p))
  cut4231 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (op (op (var 1) (var 0)) (var 0)) (var 2))) , (var 1)) → ⊥
  cut4231  adequate = bad4231  (Adequate.valid adequate Two boolean env2)
  bad4232 : PathP (λ _ → Two) (bop (bop b1 b1) (bop (bop (bop b0 b1) b1) b0)) b0 → ⊥
  bad4232  p = false≢true (sym (cong lower p))
  cut4232 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (op (op (var 1) (var 0)) (var 0)) (var 2))) , (var 2)) → ⊥
  cut4232  adequate = bad4232  (Adequate.valid adequate Two boolean env5)
  bad4233 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop (bop b0 b0) b0) b0)) b1 → ⊥
  bad4233  p = false≢true (cong lower p)
  cut4233 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (op (op (var 1) (var 0)) (var 0)) (var 2))) , (var 3)) → ⊥
  cut4233  adequate = bad4233  (Adequate.valid adequate Two boolean env4)
  holds4234 : (z0 z1 : A2) → (mul2 (mul2 z0 z0) (mul2 (mul2 (mul2 z1 z0) z1) z0)) ≡ z0
  holds4234 z0 z1 = refl
  cut4234 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (op (op (var 1) (var 0)) (var 1)) (var 0))) , (var 0)) → ⊥
  cut4234  = reject2 ((op (op (var 0) (var 0)) (op (op (op (var 1) (var 0)) (var 1)) (var 0))) , (var 0)) (λ env → holds4234 (env 0) (env 1))
  bad4235 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop (bop b1 b0) b1) b0)) b1 → ⊥
  bad4235  p = false≢true (cong lower p)
  cut4235 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (op (op (var 1) (var 0)) (var 1)) (var 0))) , (var 1)) → ⊥
  cut4235  adequate = bad4235  (Adequate.valid adequate Two boolean env0)
  bad4236 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop (bop b0 b0) b0) b0)) b1 → ⊥
  bad4236  p = false≢true (cong lower p)
  cut4236 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (op (op (var 1) (var 0)) (var 1)) (var 0))) , (var 2)) → ⊥
  cut4236  adequate = bad4236  (Adequate.valid adequate Two boolean env2)
  holds4237 : (z0 z1 : A2) → (mul2 (mul2 z0 z0) (mul2 (mul2 (mul2 z1 z0) z1) z1)) ≡ z0
  holds4237 z0 z1 = refl
  cut4237 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (op (op (var 1) (var 0)) (var 1)) (var 1))) , (var 0)) → ⊥
  cut4237  = reject2 ((op (op (var 0) (var 0)) (op (op (op (var 1) (var 0)) (var 1)) (var 1))) , (var 0)) (λ env → holds4237 (env 0) (env 1))
  bad4238 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop (bop b1 b0) b1) b1)) b1 → ⊥
  bad4238  p = false≢true (cong lower p)
  cut4238 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (op (op (var 1) (var 0)) (var 1)) (var 1))) , (var 1)) → ⊥
  cut4238  adequate = bad4238  (Adequate.valid adequate Two boolean env0)
  bad4239 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop (bop b0 b0) b0) b0)) b1 → ⊥
  bad4239  p = false≢true (cong lower p)
  cut4239 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (op (op (var 1) (var 0)) (var 1)) (var 1))) , (var 2)) → ⊥
  cut4239  adequate = bad4239  (Adequate.valid adequate Two boolean env2)
  bad4240 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop (bop b0 b0) b0) b1)) b0 → ⊥
  bad4240  p = false≢true (sym (cong lower p))
  cut4240 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (op (op (var 1) (var 0)) (var 1)) (var 2))) , (var 0)) → ⊥
  cut4240  adequate = bad4240  (Adequate.valid adequate Two boolean env2)
  bad4241 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop (bop b0 b0) b0) b1)) b0 → ⊥
  bad4241  p = false≢true (sym (cong lower p))
  cut4241 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (op (op (var 1) (var 0)) (var 1)) (var 2))) , (var 1)) → ⊥
  cut4241  adequate = bad4241  (Adequate.valid adequate Two boolean env2)
  bad4242 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop (bop b1 b0) b1) b1)) b1 → ⊥
  bad4242  p = false≢true (cong lower p)
  cut4242 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (op (op (var 1) (var 0)) (var 1)) (var 2))) , (var 2)) → ⊥
  cut4242  adequate = bad4242  (Adequate.valid adequate Two boolean env3)
  bad4243 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop (bop b0 b0) b0) b0)) b1 → ⊥
  bad4243  p = false≢true (cong lower p)
  cut4243 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (op (op (var 1) (var 0)) (var 1)) (var 2))) , (var 3)) → ⊥
  cut4243  adequate = bad4243  (Adequate.valid adequate Two boolean env4)
  holds4244 : (z0 z1 z2 : A2) → (mul2 (mul2 z0 z0) (mul2 (mul2 (mul2 z1 z0) z2) z0)) ≡ z0
  holds4244 z0 z1 z2 = refl
  cut4244 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (op (op (var 1) (var 0)) (var 2)) (var 0))) , (var 0)) → ⊥
  cut4244  = reject2 ((op (op (var 0) (var 0)) (op (op (op (var 1) (var 0)) (var 2)) (var 0))) , (var 0)) (λ env → holds4244 (env 0) (env 1) (env 2))
  bad4245 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop (bop b1 b0) b0) b0)) b1 → ⊥
  bad4245  p = false≢true (cong lower p)
  cut4245 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (op (op (var 1) (var 0)) (var 2)) (var 0))) , (var 1)) → ⊥
  cut4245  adequate = bad4245  (Adequate.valid adequate Two boolean env6)
  bad4246 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop (bop b0 b0) b1) b0)) b1 → ⊥
  bad4246  p = false≢true (cong lower p)
  cut4246 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (op (op (var 1) (var 0)) (var 2)) (var 0))) , (var 2)) → ⊥
  cut4246  adequate = bad4246  (Adequate.valid adequate Two boolean env2)
  bad4247 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop (bop b0 b0) b0) b0)) b1 → ⊥
  bad4247  p = false≢true (cong lower p)
  cut4247 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (op (op (var 1) (var 0)) (var 2)) (var 0))) , (var 3)) → ⊥
  cut4247  adequate = bad4247  (Adequate.valid adequate Two boolean env4)
  bad4248 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop (bop b1 b0) b0) b1)) b0 → ⊥
  bad4248  p = false≢true (sym (cong lower p))
  cut4248 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (op (op (var 1) (var 0)) (var 2)) (var 1))) , (var 0)) → ⊥
  cut4248  adequate = bad4248  (Adequate.valid adequate Two boolean env6)
  bad4249 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop (bop b1 b0) b1) b1)) b1 → ⊥
  bad4249  p = false≢true (cong lower p)
  cut4249 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (op (op (var 1) (var 0)) (var 2)) (var 1))) , (var 1)) → ⊥
  cut4249  adequate = bad4249  (Adequate.valid adequate Two boolean env3)
  bad4250 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop (bop b0 b0) b1) b0)) b1 → ⊥
  bad4250  p = false≢true (cong lower p)
  cut4250 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (op (op (var 1) (var 0)) (var 2)) (var 1))) , (var 2)) → ⊥
  cut4250  adequate = bad4250  (Adequate.valid adequate Two boolean env2)
  bad4251 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop (bop b0 b0) b0) b0)) b1 → ⊥
  bad4251  p = false≢true (cong lower p)
  cut4251 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (op (op (var 1) (var 0)) (var 2)) (var 1))) , (var 3)) → ⊥
  cut4251  adequate = bad4251  (Adequate.valid adequate Two boolean env4)
  holds4252 : (z0 z1 z2 : A2) → (mul2 (mul2 z0 z0) (mul2 (mul2 (mul2 z1 z0) z2) z2)) ≡ z0
  holds4252 z0 z1 z2 = refl
  cut4252 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (op (op (var 1) (var 0)) (var 2)) (var 2))) , (var 0)) → ⊥
  cut4252  = reject2 ((op (op (var 0) (var 0)) (op (op (op (var 1) (var 0)) (var 2)) (var 2))) , (var 0)) (λ env → holds4252 (env 0) (env 1) (env 2))
  bad4253 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop (bop b1 b0) b0) b0)) b1 → ⊥
  bad4253  p = false≢true (cong lower p)
  cut4253 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (op (op (var 1) (var 0)) (var 2)) (var 2))) , (var 1)) → ⊥
  cut4253  adequate = bad4253  (Adequate.valid adequate Two boolean env6)
  bad4254 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop (bop b0 b0) b1) b1)) b1 → ⊥
  bad4254  p = false≢true (cong lower p)
  cut4254 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (op (op (var 1) (var 0)) (var 2)) (var 2))) , (var 2)) → ⊥
  cut4254  adequate = bad4254  (Adequate.valid adequate Two boolean env2)
  bad4255 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop (bop b0 b0) b0) b0)) b1 → ⊥
  bad4255  p = false≢true (cong lower p)
  cut4255 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (op (op (var 1) (var 0)) (var 2)) (var 2))) , (var 3)) → ⊥
  cut4255  adequate = bad4255  (Adequate.valid adequate Two boolean env4)
  bad4256 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop (bop b0 b0) b0) b1)) b0 → ⊥
  bad4256  p = false≢true (sym (cong lower p))
  cut4256 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (op (op (var 1) (var 0)) (var 2)) (var 3))) , (var 0)) → ⊥
  cut4256  adequate = bad4256  (Adequate.valid adequate Two boolean env4)
  bad4257 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop (bop b0 b0) b0) b1)) b0 → ⊥
  bad4257  p = false≢true (sym (cong lower p))
  cut4257 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (op (op (var 1) (var 0)) (var 2)) (var 3))) , (var 1)) → ⊥
  cut4257  adequate = bad4257  (Adequate.valid adequate Two boolean env4)
  bad4258 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop (bop b0 b0) b0) b1)) b0 → ⊥
  bad4258  p = false≢true (sym (cong lower p))
  cut4258 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (op (op (var 1) (var 0)) (var 2)) (var 3))) , (var 2)) → ⊥
  cut4258  adequate = bad4258  (Adequate.valid adequate Two boolean env4)
  bad4259 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop (bop b0 b0) b1) b1)) b1 → ⊥
  bad4259  p = false≢true (cong lower p)
  cut4259 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (op (op (var 1) (var 0)) (var 2)) (var 3))) , (var 3)) → ⊥
  cut4259  adequate = bad4259  (Adequate.valid adequate Two boolean env7)
  bad4260 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop (bop b0 b0) b0) b0)) b1 → ⊥
  bad4260  p = false≢true (cong lower p)
  cut4260 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (op (op (var 1) (var 0)) (var 2)) (var 3))) , (var 4)) → ⊥
  cut4260  adequate = bad4260  (Adequate.valid adequate Two boolean env8)
  holds4261 : (z0 z1 : A2) → (mul2 (mul2 z0 z0) (mul2 (mul2 (mul2 z1 z1) z0) z0)) ≡ z0
  holds4261 z0 z1 = refl
  cut4261 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (op (op (var 1) (var 1)) (var 0)) (var 0))) , (var 0)) → ⊥
  cut4261  = reject2 ((op (op (var 0) (var 0)) (op (op (op (var 1) (var 1)) (var 0)) (var 0))) , (var 0)) (λ env → holds4261 (env 0) (env 1))
  bad4262 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop (bop b1 b1) b0) b0)) b1 → ⊥
  bad4262  p = false≢true (cong lower p)
  cut4262 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (op (op (var 1) (var 1)) (var 0)) (var 0))) , (var 1)) → ⊥
  cut4262  adequate = bad4262  (Adequate.valid adequate Two boolean env0)
  bad4263 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop (bop b0 b0) b0) b0)) b1 → ⊥
  bad4263  p = false≢true (cong lower p)
  cut4263 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (op (op (var 1) (var 1)) (var 0)) (var 0))) , (var 2)) → ⊥
  cut4263  adequate = bad4263  (Adequate.valid adequate Two boolean env2)
  bad4264 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop (bop b1 b1) b0) b1)) b0 → ⊥
  bad4264  p = false≢true (sym (cong lower p))
  cut4264 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (op (op (var 1) (var 1)) (var 0)) (var 1))) , (var 0)) → ⊥
  cut4264  adequate = bad4264  (Adequate.valid adequate Two boolean env0)
  bad4265 : PathP (λ _ → Two) (bop (bop b1 b1) (bop (bop (bop b0 b0) b1) b0)) b0 → ⊥
  bad4265  p = false≢true (sym (cong lower p))
  cut4265 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (op (op (var 1) (var 1)) (var 0)) (var 1))) , (var 1)) → ⊥
  cut4265  adequate = bad4265  (Adequate.valid adequate Two boolean env1)
  bad4266 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop (bop b0 b0) b0) b0)) b1 → ⊥
  bad4266  p = false≢true (cong lower p)
  cut4266 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (op (op (var 1) (var 1)) (var 0)) (var 1))) , (var 2)) → ⊥
  cut4266  adequate = bad4266  (Adequate.valid adequate Two boolean env2)
  bad4267 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop (bop b0 b0) b0) b1)) b0 → ⊥
  bad4267  p = false≢true (sym (cong lower p))
  cut4267 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (op (op (var 1) (var 1)) (var 0)) (var 2))) , (var 0)) → ⊥
  cut4267  adequate = bad4267  (Adequate.valid adequate Two boolean env2)
  bad4268 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop (bop b0 b0) b0) b1)) b0 → ⊥
  bad4268  p = false≢true (sym (cong lower p))
  cut4268 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (op (op (var 1) (var 1)) (var 0)) (var 2))) , (var 1)) → ⊥
  cut4268  adequate = bad4268  (Adequate.valid adequate Two boolean env2)
  bad4269 : PathP (λ _ → Two) (bop (bop b1 b1) (bop (bop (bop b0 b0) b1) b0)) b0 → ⊥
  bad4269  p = false≢true (sym (cong lower p))
  cut4269 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (op (op (var 1) (var 1)) (var 0)) (var 2))) , (var 2)) → ⊥
  cut4269  adequate = bad4269  (Adequate.valid adequate Two boolean env5)
  bad4270 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop (bop b0 b0) b0) b0)) b1 → ⊥
  bad4270  p = false≢true (cong lower p)
  cut4270 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (op (op (var 1) (var 1)) (var 0)) (var 2))) , (var 3)) → ⊥
  cut4270  adequate = bad4270  (Adequate.valid adequate Two boolean env4)
  holds4271 : (z0 z1 : A2) → (mul2 (mul2 z0 z0) (mul2 (mul2 (mul2 z1 z1) z1) z0)) ≡ z0
  holds4271 z0 z1 = refl
  cut4271 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (op (op (var 1) (var 1)) (var 1)) (var 0))) , (var 0)) → ⊥
  cut4271  = reject2 ((op (op (var 0) (var 0)) (op (op (op (var 1) (var 1)) (var 1)) (var 0))) , (var 0)) (λ env → holds4271 (env 0) (env 1))
  bad4272 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop (bop b1 b1) b1) b0)) b1 → ⊥
  bad4272  p = false≢true (cong lower p)
  cut4272 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (op (op (var 1) (var 1)) (var 1)) (var 0))) , (var 1)) → ⊥
  cut4272  adequate = bad4272  (Adequate.valid adequate Two boolean env0)
  bad4273 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop (bop b0 b0) b0) b0)) b1 → ⊥
  bad4273  p = false≢true (cong lower p)
  cut4273 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (op (op (var 1) (var 1)) (var 1)) (var 0))) , (var 2)) → ⊥
  cut4273  adequate = bad4273  (Adequate.valid adequate Two boolean env2)
  bad4274 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop (bop b1 b1) b1) b1)) b0 → ⊥
  bad4274  p = false≢true (sym (cong lower p))
  cut4274 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (op (op (var 1) (var 1)) (var 1)) (var 1))) , (var 0)) → ⊥
  cut4274  adequate = bad4274  (Adequate.valid adequate Two boolean env0)
  bad4275 : PathP (λ _ → Two) (bop (bop b1 b1) (bop (bop (bop b0 b0) b0) b0)) b0 → ⊥
  bad4275  p = false≢true (sym (cong lower p))
  cut4275 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (op (op (var 1) (var 1)) (var 1)) (var 1))) , (var 1)) → ⊥
  cut4275  adequate = bad4275  (Adequate.valid adequate Two boolean env1)
  bad4276 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop (bop b0 b0) b0) b0)) b1 → ⊥
  bad4276  p = false≢true (cong lower p)
  cut4276 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (op (op (var 1) (var 1)) (var 1)) (var 1))) , (var 2)) → ⊥
  cut4276  adequate = bad4276  (Adequate.valid adequate Two boolean env2)
  bad4277 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop (bop b0 b0) b0) b1)) b0 → ⊥
  bad4277  p = false≢true (sym (cong lower p))
  cut4277 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (op (op (var 1) (var 1)) (var 1)) (var 2))) , (var 0)) → ⊥
  cut4277  adequate = bad4277  (Adequate.valid adequate Two boolean env2)
  bad4278 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop (bop b0 b0) b0) b1)) b0 → ⊥
  bad4278  p = false≢true (sym (cong lower p))
  cut4278 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (op (op (var 1) (var 1)) (var 1)) (var 2))) , (var 1)) → ⊥
  cut4278  adequate = bad4278  (Adequate.valid adequate Two boolean env2)
  bad4279 : PathP (λ _ → Two) (bop (bop b1 b1) (bop (bop (bop b0 b0) b0) b0)) b0 → ⊥
  bad4279  p = false≢true (sym (cong lower p))
  cut4279 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (op (op (var 1) (var 1)) (var 1)) (var 2))) , (var 2)) → ⊥
  cut4279  adequate = bad4279  (Adequate.valid adequate Two boolean env5)
  bad4280 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop (bop b0 b0) b0) b0)) b1 → ⊥
  bad4280  p = false≢true (cong lower p)
  cut4280 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (op (op (var 1) (var 1)) (var 1)) (var 2))) , (var 3)) → ⊥
  cut4280  adequate = bad4280  (Adequate.valid adequate Two boolean env4)
  holds4281 : (z0 z1 z2 : A2) → (mul2 (mul2 z0 z0) (mul2 (mul2 (mul2 z1 z1) z2) z0)) ≡ z0
  holds4281 z0 z1 z2 = refl
  cut4281 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (op (op (var 1) (var 1)) (var 2)) (var 0))) , (var 0)) → ⊥
  cut4281  = reject2 ((op (op (var 0) (var 0)) (op (op (op (var 1) (var 1)) (var 2)) (var 0))) , (var 0)) (λ env → holds4281 (env 0) (env 1) (env 2))
  bad4282 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop (bop b1 b1) b0) b0)) b1 → ⊥
  bad4282  p = false≢true (cong lower p)
  cut4282 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (op (op (var 1) (var 1)) (var 2)) (var 0))) , (var 1)) → ⊥
  cut4282  adequate = bad4282  (Adequate.valid adequate Two boolean env6)
  bad4283 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop (bop b0 b0) b1) b0)) b1 → ⊥
  bad4283  p = false≢true (cong lower p)
  cut4283 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (op (op (var 1) (var 1)) (var 2)) (var 0))) , (var 2)) → ⊥
  cut4283  adequate = bad4283  (Adequate.valid adequate Two boolean env2)
  bad4284 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop (bop b0 b0) b0) b0)) b1 → ⊥
  bad4284  p = false≢true (cong lower p)
  cut4284 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (op (op (var 1) (var 1)) (var 2)) (var 0))) , (var 3)) → ⊥
  cut4284  adequate = bad4284  (Adequate.valid adequate Two boolean env4)
  bad4285 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop (bop b1 b1) b0) b1)) b0 → ⊥
  bad4285  p = false≢true (sym (cong lower p))
  cut4285 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (op (op (var 1) (var 1)) (var 2)) (var 1))) , (var 0)) → ⊥
  cut4285  adequate = bad4285  (Adequate.valid adequate Two boolean env6)
  bad4286 : PathP (λ _ → Two) (bop (bop b1 b1) (bop (bop (bop b0 b0) b0) b0)) b0 → ⊥
  bad4286  p = false≢true (sym (cong lower p))
  cut4286 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (op (op (var 1) (var 1)) (var 2)) (var 1))) , (var 1)) → ⊥
  cut4286  adequate = bad4286  (Adequate.valid adequate Two boolean env5)
  bad4287 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop (bop b0 b0) b1) b0)) b1 → ⊥
  bad4287  p = false≢true (cong lower p)
  cut4287 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (op (op (var 1) (var 1)) (var 2)) (var 1))) , (var 2)) → ⊥
  cut4287  adequate = bad4287  (Adequate.valid adequate Two boolean env2)
  bad4288 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop (bop b0 b0) b0) b0)) b1 → ⊥
  bad4288  p = false≢true (cong lower p)
  cut4288 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (op (op (var 1) (var 1)) (var 2)) (var 1))) , (var 3)) → ⊥
  cut4288  adequate = bad4288  (Adequate.valid adequate Two boolean env4)
  bad4289 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop (bop b1 b1) b1) b1)) b0 → ⊥
  bad4289  p = false≢true (sym (cong lower p))
  cut4289 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (op (op (var 1) (var 1)) (var 2)) (var 2))) , (var 0)) → ⊥
  cut4289  adequate = bad4289  (Adequate.valid adequate Two boolean env3)
  bad4290 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop (bop b1 b1) b0) b0)) b1 → ⊥
  bad4290  p = false≢true (cong lower p)
  cut4290 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (op (op (var 1) (var 1)) (var 2)) (var 2))) , (var 1)) → ⊥
  cut4290  adequate = bad4290  (Adequate.valid adequate Two boolean env6)
  bad4291 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop (bop b0 b0) b1) b1)) b1 → ⊥
  bad4291  p = false≢true (cong lower p)
  cut4291 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (op (op (var 1) (var 1)) (var 2)) (var 2))) , (var 2)) → ⊥
  cut4291  adequate = bad4291  (Adequate.valid adequate Two boolean env2)
  bad4292 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop (bop b0 b0) b0) b0)) b1 → ⊥
  bad4292  p = false≢true (cong lower p)
  cut4292 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (op (op (var 1) (var 1)) (var 2)) (var 2))) , (var 3)) → ⊥
  cut4292  adequate = bad4292  (Adequate.valid adequate Two boolean env4)
  bad4293 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop (bop b0 b0) b0) b1)) b0 → ⊥
  bad4293  p = false≢true (sym (cong lower p))
  cut4293 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (op (op (var 1) (var 1)) (var 2)) (var 3))) , (var 0)) → ⊥
  cut4293  adequate = bad4293  (Adequate.valid adequate Two boolean env4)
  bad4294 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop (bop b0 b0) b0) b1)) b0 → ⊥
  bad4294  p = false≢true (sym (cong lower p))
  cut4294 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (op (op (var 1) (var 1)) (var 2)) (var 3))) , (var 1)) → ⊥
  cut4294  adequate = bad4294  (Adequate.valid adequate Two boolean env4)
  bad4295 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop (bop b0 b0) b0) b1)) b0 → ⊥
  bad4295  p = false≢true (sym (cong lower p))
  cut4295 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (op (op (var 1) (var 1)) (var 2)) (var 3))) , (var 2)) → ⊥
  cut4295  adequate = bad4295  (Adequate.valid adequate Two boolean env4)
  bad4296 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop (bop b0 b0) b1) b1)) b1 → ⊥
  bad4296  p = false≢true (cong lower p)
  cut4296 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (op (op (var 1) (var 1)) (var 2)) (var 3))) , (var 3)) → ⊥
  cut4296  adequate = bad4296  (Adequate.valid adequate Two boolean env7)
  bad4297 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop (bop b0 b0) b0) b0)) b1 → ⊥
  bad4297  p = false≢true (cong lower p)
  cut4297 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (op (op (var 1) (var 1)) (var 2)) (var 3))) , (var 4)) → ⊥
  cut4297  adequate = bad4297  (Adequate.valid adequate Two boolean env8)
  holds4298 : (z0 z1 z2 : A2) → (mul2 (mul2 z0 z0) (mul2 (mul2 (mul2 z1 z2) z0) z0)) ≡ z0
  holds4298 z0 z1 z2 = refl
  cut4298 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (op (op (var 1) (var 2)) (var 0)) (var 0))) , (var 0)) → ⊥
  cut4298  = reject2 ((op (op (var 0) (var 0)) (op (op (op (var 1) (var 2)) (var 0)) (var 0))) , (var 0)) (λ env → holds4298 (env 0) (env 1) (env 2))
  bad4299 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop (bop b1 b0) b0) b0)) b1 → ⊥
  bad4299  p = false≢true (cong lower p)
  cut4299 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (op (op (var 1) (var 2)) (var 0)) (var 0))) , (var 1)) → ⊥
  cut4299  adequate = bad4299  (Adequate.valid adequate Two boolean env6)
  bad4300 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop (bop b0 b1) b0) b0)) b1 → ⊥
  bad4300  p = false≢true (cong lower p)
  cut4300 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (op (op (var 1) (var 2)) (var 0)) (var 0))) , (var 2)) → ⊥
  cut4300  adequate = bad4300  (Adequate.valid adequate Two boolean env2)
  bad4301 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop (bop b0 b0) b0) b0)) b1 → ⊥
  bad4301  p = false≢true (cong lower p)
  cut4301 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (op (op (var 1) (var 2)) (var 0)) (var 0))) , (var 3)) → ⊥
  cut4301  adequate = bad4301  (Adequate.valid adequate Two boolean env4)
  bad4302 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop (bop b1 b0) b0) b1)) b0 → ⊥
  bad4302  p = false≢true (sym (cong lower p))
  cut4302 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (op (op (var 1) (var 2)) (var 0)) (var 1))) , (var 0)) → ⊥
  cut4302  adequate = bad4302  (Adequate.valid adequate Two boolean env6)
  bad4303 : PathP (λ _ → Two) (bop (bop b1 b1) (bop (bop (bop b0 b0) b1) b0)) b0 → ⊥
  bad4303  p = false≢true (sym (cong lower p))
  cut4303 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (op (op (var 1) (var 2)) (var 0)) (var 1))) , (var 1)) → ⊥
  cut4303  adequate = bad4303  (Adequate.valid adequate Two boolean env5)
  bad4304 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop (bop b0 b1) b0) b0)) b1 → ⊥
  bad4304  p = false≢true (cong lower p)
  cut4304 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (op (op (var 1) (var 2)) (var 0)) (var 1))) , (var 2)) → ⊥
  cut4304  adequate = bad4304  (Adequate.valid adequate Two boolean env2)
  bad4305 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop (bop b0 b0) b0) b0)) b1 → ⊥
  bad4305  p = false≢true (cong lower p)
  cut4305 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (op (op (var 1) (var 2)) (var 0)) (var 1))) , (var 3)) → ⊥
  cut4305  adequate = bad4305  (Adequate.valid adequate Two boolean env4)
  bad4306 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop (bop b0 b1) b0) b1)) b0 → ⊥
  bad4306  p = false≢true (sym (cong lower p))
  cut4306 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (op (op (var 1) (var 2)) (var 0)) (var 2))) , (var 0)) → ⊥
  cut4306  adequate = bad4306  (Adequate.valid adequate Two boolean env2)
  bad4307 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop (bop b0 b1) b0) b1)) b0 → ⊥
  bad4307  p = false≢true (sym (cong lower p))
  cut4307 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (op (op (var 1) (var 2)) (var 0)) (var 2))) , (var 1)) → ⊥
  cut4307  adequate = bad4307  (Adequate.valid adequate Two boolean env2)
  bad4308 : PathP (λ _ → Two) (bop (bop b1 b1) (bop (bop (bop b0 b0) b1) b0)) b0 → ⊥
  bad4308  p = false≢true (sym (cong lower p))
  cut4308 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (op (op (var 1) (var 2)) (var 0)) (var 2))) , (var 2)) → ⊥
  cut4308  adequate = bad4308  (Adequate.valid adequate Two boolean env5)
  bad4309 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop (bop b0 b0) b0) b0)) b1 → ⊥
  bad4309  p = false≢true (cong lower p)
  cut4309 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (op (op (var 1) (var 2)) (var 0)) (var 2))) , (var 3)) → ⊥
  cut4309  adequate = bad4309  (Adequate.valid adequate Two boolean env4)
  bad4310 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop (bop b0 b0) b0) b1)) b0 → ⊥
  bad4310  p = false≢true (sym (cong lower p))
  cut4310 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (op (op (var 1) (var 2)) (var 0)) (var 3))) , (var 0)) → ⊥
  cut4310  adequate = bad4310  (Adequate.valid adequate Two boolean env4)
  bad4311 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop (bop b0 b0) b0) b1)) b0 → ⊥
  bad4311  p = false≢true (sym (cong lower p))
  cut4311 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (op (op (var 1) (var 2)) (var 0)) (var 3))) , (var 1)) → ⊥
  cut4311  adequate = bad4311  (Adequate.valid adequate Two boolean env4)
  bad4312 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop (bop b0 b0) b0) b1)) b0 → ⊥
  bad4312  p = false≢true (sym (cong lower p))
  cut4312 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (op (op (var 1) (var 2)) (var 0)) (var 3))) , (var 2)) → ⊥
  cut4312  adequate = bad4312  (Adequate.valid adequate Two boolean env4)
  env9 : ℕ → Two
  env9 zero = b1
  env9 (suc zero) = b0
  env9 (suc (suc zero)) = b0
  env9 (suc (suc (suc zero))) = b0
  env9 (suc (suc (suc (suc rest)))) = b0
  bad4313 : PathP (λ _ → Two) (bop (bop b1 b1) (bop (bop (bop b0 b0) b1) b0)) b0 → ⊥
  bad4313  p = false≢true (sym (cong lower p))
  cut4313 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (op (op (var 1) (var 2)) (var 0)) (var 3))) , (var 3)) → ⊥
  cut4313  adequate = bad4313  (Adequate.valid adequate Two boolean env9)
  bad4314 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop (bop b0 b0) b0) b0)) b1 → ⊥
  bad4314  p = false≢true (cong lower p)
  cut4314 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (op (op (var 1) (var 2)) (var 0)) (var 3))) , (var 4)) → ⊥
  cut4314  adequate = bad4314  (Adequate.valid adequate Two boolean env8)
  holds4315 : (z0 z1 z2 : A2) → (mul2 (mul2 z0 z0) (mul2 (mul2 (mul2 z1 z2) z1) z0)) ≡ z0
  holds4315 z0 z1 z2 = refl
  cut4315 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (op (op (var 1) (var 2)) (var 1)) (var 0))) , (var 0)) → ⊥
  cut4315  = reject2 ((op (op (var 0) (var 0)) (op (op (op (var 1) (var 2)) (var 1)) (var 0))) , (var 0)) (λ env → holds4315 (env 0) (env 1) (env 2))
  bad4316 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop (bop b1 b0) b1) b0)) b1 → ⊥
  bad4316  p = false≢true (cong lower p)
  cut4316 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (op (op (var 1) (var 2)) (var 1)) (var 0))) , (var 1)) → ⊥
  cut4316  adequate = bad4316  (Adequate.valid adequate Two boolean env6)
  bad4317 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop (bop b0 b1) b0) b0)) b1 → ⊥
  bad4317  p = false≢true (cong lower p)
  cut4317 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (op (op (var 1) (var 2)) (var 1)) (var 0))) , (var 2)) → ⊥
  cut4317  adequate = bad4317  (Adequate.valid adequate Two boolean env2)
  bad4318 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop (bop b0 b0) b0) b0)) b1 → ⊥
  bad4318  p = false≢true (cong lower p)
  cut4318 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (op (op (var 1) (var 2)) (var 1)) (var 0))) , (var 3)) → ⊥
  cut4318  adequate = bad4318  (Adequate.valid adequate Two boolean env4)
  bad4319 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop (bop b1 b1) b1) b1)) b0 → ⊥
  bad4319  p = false≢true (sym (cong lower p))
  cut4319 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (op (op (var 1) (var 2)) (var 1)) (var 1))) , (var 0)) → ⊥
  cut4319  adequate = bad4319  (Adequate.valid adequate Two boolean env3)
  bad4320 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop (bop b1 b0) b1) b1)) b1 → ⊥
  bad4320  p = false≢true (cong lower p)
  cut4320 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (op (op (var 1) (var 2)) (var 1)) (var 1))) , (var 1)) → ⊥
  cut4320  adequate = bad4320  (Adequate.valid adequate Two boolean env6)
  bad4321 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop (bop b0 b1) b0) b0)) b1 → ⊥
  bad4321  p = false≢true (cong lower p)
  cut4321 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (op (op (var 1) (var 2)) (var 1)) (var 1))) , (var 2)) → ⊥
  cut4321  adequate = bad4321  (Adequate.valid adequate Two boolean env2)
  bad4322 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop (bop b0 b0) b0) b0)) b1 → ⊥
  bad4322  p = false≢true (cong lower p)
  cut4322 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (op (op (var 1) (var 2)) (var 1)) (var 1))) , (var 3)) → ⊥
  cut4322  adequate = bad4322  (Adequate.valid adequate Two boolean env4)
  bad4323 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop (bop b0 b1) b0) b1)) b0 → ⊥
  bad4323  p = false≢true (sym (cong lower p))
  cut4323 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (op (op (var 1) (var 2)) (var 1)) (var 2))) , (var 0)) → ⊥
  cut4323  adequate = bad4323  (Adequate.valid adequate Two boolean env2)
  bad4324 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop (bop b0 b1) b0) b1)) b0 → ⊥
  bad4324  p = false≢true (sym (cong lower p))
  cut4324 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (op (op (var 1) (var 2)) (var 1)) (var 2))) , (var 1)) → ⊥
  cut4324  adequate = bad4324  (Adequate.valid adequate Two boolean env2)
  bad4325 : PathP (λ _ → Two) (bop (bop b1 b1) (bop (bop (bop b0 b0) b0) b0)) b0 → ⊥
  bad4325  p = false≢true (sym (cong lower p))
  cut4325 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (op (op (var 1) (var 2)) (var 1)) (var 2))) , (var 2)) → ⊥
  cut4325  adequate = bad4325  (Adequate.valid adequate Two boolean env5)
  bad4326 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop (bop b0 b0) b0) b0)) b1 → ⊥
  bad4326  p = false≢true (cong lower p)
  cut4326 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (op (op (var 1) (var 2)) (var 1)) (var 2))) , (var 3)) → ⊥
  cut4326  adequate = bad4326  (Adequate.valid adequate Two boolean env4)
  bad4327 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop (bop b0 b0) b0) b1)) b0 → ⊥
  bad4327  p = false≢true (sym (cong lower p))
  cut4327 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (op (op (var 1) (var 2)) (var 1)) (var 3))) , (var 0)) → ⊥
  cut4327  adequate = bad4327  (Adequate.valid adequate Two boolean env4)
  bad4328 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop (bop b0 b0) b0) b1)) b0 → ⊥
  bad4328  p = false≢true (sym (cong lower p))
  cut4328 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (op (op (var 1) (var 2)) (var 1)) (var 3))) , (var 1)) → ⊥
  cut4328  adequate = bad4328  (Adequate.valid adequate Two boolean env4)
  bad4329 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop (bop b0 b0) b0) b1)) b0 → ⊥
  bad4329  p = false≢true (sym (cong lower p))
  cut4329 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (op (op (var 1) (var 2)) (var 1)) (var 3))) , (var 2)) → ⊥
  cut4329  adequate = bad4329  (Adequate.valid adequate Two boolean env4)
  env10 : ℕ → Two
  env10 zero = b0
  env10 (suc zero) = b1
  env10 (suc (suc zero)) = b0
  env10 (suc (suc (suc zero))) = b1
  env10 (suc (suc (suc (suc rest)))) = b0
  bad4330 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop (bop b1 b0) b1) b1)) b1 → ⊥
  bad4330  p = false≢true (cong lower p)
  cut4330 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (op (op (var 1) (var 2)) (var 1)) (var 3))) , (var 3)) → ⊥
  cut4330  adequate = bad4330  (Adequate.valid adequate Two boolean env10)
  bad4331 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop (bop b0 b0) b0) b0)) b1 → ⊥
  bad4331  p = false≢true (cong lower p)
  cut4331 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (op (op (var 1) (var 2)) (var 1)) (var 3))) , (var 4)) → ⊥
  cut4331  adequate = bad4331  (Adequate.valid adequate Two boolean env8)
  holds4332 : (z0 z1 z2 : A2) → (mul2 (mul2 z0 z0) (mul2 (mul2 (mul2 z1 z2) z2) z0)) ≡ z0
  holds4332 z0 z1 z2 = refl
  cut4332 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (op (op (var 1) (var 2)) (var 2)) (var 0))) , (var 0)) → ⊥
  cut4332  = reject2 ((op (op (var 0) (var 0)) (op (op (op (var 1) (var 2)) (var 2)) (var 0))) , (var 0)) (λ env → holds4332 (env 0) (env 1) (env 2))
  bad4333 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop (bop b1 b0) b0) b0)) b1 → ⊥
  bad4333  p = false≢true (cong lower p)
  cut4333 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (op (op (var 1) (var 2)) (var 2)) (var 0))) , (var 1)) → ⊥
  cut4333  adequate = bad4333  (Adequate.valid adequate Two boolean env6)
  bad4334 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop (bop b0 b1) b1) b0)) b1 → ⊥
  bad4334  p = false≢true (cong lower p)
  cut4334 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (op (op (var 1) (var 2)) (var 2)) (var 0))) , (var 2)) → ⊥
  cut4334  adequate = bad4334  (Adequate.valid adequate Two boolean env2)
  bad4335 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop (bop b0 b0) b0) b0)) b1 → ⊥
  bad4335  p = false≢true (cong lower p)
  cut4335 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (op (op (var 1) (var 2)) (var 2)) (var 0))) , (var 3)) → ⊥
  cut4335  adequate = bad4335  (Adequate.valid adequate Two boolean env4)
  bad4336 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop (bop b1 b0) b0) b1)) b0 → ⊥
  bad4336  p = false≢true (sym (cong lower p))
  cut4336 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (op (op (var 1) (var 2)) (var 2)) (var 1))) , (var 0)) → ⊥
  cut4336  adequate = bad4336  (Adequate.valid adequate Two boolean env6)
  bad4337 : PathP (λ _ → Two) (bop (bop b1 b1) (bop (bop (bop b0 b0) b0) b0)) b0 → ⊥
  bad4337  p = false≢true (sym (cong lower p))
  cut4337 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (op (op (var 1) (var 2)) (var 2)) (var 1))) , (var 1)) → ⊥
  cut4337  adequate = bad4337  (Adequate.valid adequate Two boolean env5)
  bad4338 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop (bop b0 b1) b1) b0)) b1 → ⊥
  bad4338  p = false≢true (cong lower p)
  cut4338 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (op (op (var 1) (var 2)) (var 2)) (var 1))) , (var 2)) → ⊥
  cut4338  adequate = bad4338  (Adequate.valid adequate Two boolean env2)
  bad4339 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop (bop b0 b0) b0) b0)) b1 → ⊥
  bad4339  p = false≢true (cong lower p)
  cut4339 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (op (op (var 1) (var 2)) (var 2)) (var 1))) , (var 3)) → ⊥
  cut4339  adequate = bad4339  (Adequate.valid adequate Two boolean env4)
  bad4340 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop (bop b1 b1) b1) b1)) b0 → ⊥
  bad4340  p = false≢true (sym (cong lower p))
  cut4340 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (op (op (var 1) (var 2)) (var 2)) (var 2))) , (var 0)) → ⊥
  cut4340  adequate = bad4340  (Adequate.valid adequate Two boolean env3)
  bad4341 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop (bop b1 b0) b0) b0)) b1 → ⊥
  bad4341  p = false≢true (cong lower p)
  cut4341 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (op (op (var 1) (var 2)) (var 2)) (var 2))) , (var 1)) → ⊥
  cut4341  adequate = bad4341  (Adequate.valid adequate Two boolean env6)
  bad4342 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop (bop b0 b1) b1) b1)) b1 → ⊥
  bad4342  p = false≢true (cong lower p)
  cut4342 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (op (op (var 1) (var 2)) (var 2)) (var 2))) , (var 2)) → ⊥
  cut4342  adequate = bad4342  (Adequate.valid adequate Two boolean env2)
  bad4343 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop (bop b0 b0) b0) b0)) b1 → ⊥
  bad4343  p = false≢true (cong lower p)
  cut4343 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (op (op (var 1) (var 2)) (var 2)) (var 2))) , (var 3)) → ⊥
  cut4343  adequate = bad4343  (Adequate.valid adequate Two boolean env4)
  bad4344 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop (bop b0 b0) b0) b1)) b0 → ⊥
  bad4344  p = false≢true (sym (cong lower p))
  cut4344 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (op (op (var 1) (var 2)) (var 2)) (var 3))) , (var 0)) → ⊥
  cut4344  adequate = bad4344  (Adequate.valid adequate Two boolean env4)
  bad4345 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop (bop b0 b0) b0) b1)) b0 → ⊥
  bad4345  p = false≢true (sym (cong lower p))
  cut4345 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (op (op (var 1) (var 2)) (var 2)) (var 3))) , (var 1)) → ⊥
  cut4345  adequate = bad4345  (Adequate.valid adequate Two boolean env4)
  bad4346 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop (bop b0 b0) b0) b1)) b0 → ⊥
  bad4346  p = false≢true (sym (cong lower p))
  cut4346 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (op (op (var 1) (var 2)) (var 2)) (var 3))) , (var 2)) → ⊥
  cut4346  adequate = bad4346  (Adequate.valid adequate Two boolean env4)
  bad4347 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop (bop b0 b1) b1) b1)) b1 → ⊥
  bad4347  p = false≢true (cong lower p)
  cut4347 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (op (op (var 1) (var 2)) (var 2)) (var 3))) , (var 3)) → ⊥
  cut4347  adequate = bad4347  (Adequate.valid adequate Two boolean env7)
  bad4348 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop (bop b0 b0) b0) b0)) b1 → ⊥
  bad4348  p = false≢true (cong lower p)
  cut4348 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (op (op (var 1) (var 2)) (var 2)) (var 3))) , (var 4)) → ⊥
  cut4348  adequate = bad4348  (Adequate.valid adequate Two boolean env8)
  holds4349 : (z0 z1 z2 z3 : A2) → (mul2 (mul2 z0 z0) (mul2 (mul2 (mul2 z1 z2) z3) z0)) ≡ z0
  holds4349 z0 z1 z2 z3 = refl
  cut4349 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (op (op (var 1) (var 2)) (var 3)) (var 0))) , (var 0)) → ⊥
  cut4349  = reject2 ((op (op (var 0) (var 0)) (op (op (op (var 1) (var 2)) (var 3)) (var 0))) , (var 0)) (λ env → holds4349 (env 0) (env 1) (env 2) (env 3))
  env11 : ℕ → Two
  env11 zero = b0
  env11 (suc zero) = b1
  env11 (suc (suc zero)) = b0
  env11 (suc (suc (suc zero))) = b0
  env11 (suc (suc (suc (suc rest)))) = b0
  bad4350 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop (bop b1 b0) b0) b0)) b1 → ⊥
  bad4350  p = false≢true (cong lower p)
  cut4350 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (op (op (var 1) (var 2)) (var 3)) (var 0))) , (var 1)) → ⊥
  cut4350  adequate = bad4350  (Adequate.valid adequate Two boolean env11)
  env12 : ℕ → Two
  env12 zero = b0
  env12 (suc zero) = b0
  env12 (suc (suc zero)) = b1
  env12 (suc (suc (suc zero))) = b0
  env12 (suc (suc (suc (suc rest)))) = b0
  bad4351 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop (bop b0 b1) b0) b0)) b1 → ⊥
  bad4351  p = false≢true (cong lower p)
  cut4351 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (op (op (var 1) (var 2)) (var 3)) (var 0))) , (var 2)) → ⊥
  cut4351  adequate = bad4351  (Adequate.valid adequate Two boolean env12)
  bad4352 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop (bop b0 b0) b1) b0)) b1 → ⊥
  bad4352  p = false≢true (cong lower p)
  cut4352 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (op (op (var 1) (var 2)) (var 3)) (var 0))) , (var 3)) → ⊥
  cut4352  adequate = bad4352  (Adequate.valid adequate Two boolean env4)
  bad4353 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop (bop b0 b0) b0) b0)) b1 → ⊥
  bad4353  p = false≢true (cong lower p)
  cut4353 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (op (op (var 1) (var 2)) (var 3)) (var 0))) , (var 4)) → ⊥
  cut4353  adequate = bad4353  (Adequate.valid adequate Two boolean env8)
  bad4354 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop (bop b1 b0) b0) b1)) b0 → ⊥
  bad4354  p = false≢true (sym (cong lower p))
  cut4354 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (op (op (var 1) (var 2)) (var 3)) (var 1))) , (var 0)) → ⊥
  cut4354  adequate = bad4354  (Adequate.valid adequate Two boolean env11)
  bad4355 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop (bop b1 b0) b1) b1)) b1 → ⊥
  bad4355  p = false≢true (cong lower p)
  cut4355 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (op (op (var 1) (var 2)) (var 3)) (var 1))) , (var 1)) → ⊥
  cut4355  adequate = bad4355  (Adequate.valid adequate Two boolean env10)
  bad4356 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop (bop b0 b1) b0) b0)) b1 → ⊥
  bad4356  p = false≢true (cong lower p)
  cut4356 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (op (op (var 1) (var 2)) (var 3)) (var 1))) , (var 2)) → ⊥
  cut4356  adequate = bad4356  (Adequate.valid adequate Two boolean env12)
  bad4357 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop (bop b0 b0) b1) b0)) b1 → ⊥
  bad4357  p = false≢true (cong lower p)
  cut4357 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (op (op (var 1) (var 2)) (var 3)) (var 1))) , (var 3)) → ⊥
  cut4357  adequate = bad4357  (Adequate.valid adequate Two boolean env4)
  bad4358 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop (bop b0 b0) b0) b0)) b1 → ⊥
  bad4358  p = false≢true (cong lower p)
  cut4358 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (op (op (var 1) (var 2)) (var 3)) (var 1))) , (var 4)) → ⊥
  cut4358  adequate = bad4358  (Adequate.valid adequate Two boolean env8)
  bad4359 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop (bop b0 b1) b0) b1)) b0 → ⊥
  bad4359  p = false≢true (sym (cong lower p))
  cut4359 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (op (op (var 1) (var 2)) (var 3)) (var 2))) , (var 0)) → ⊥
  cut4359  adequate = bad4359  (Adequate.valid adequate Two boolean env12)
  bad4360 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop (bop b0 b1) b0) b1)) b0 → ⊥
  bad4360  p = false≢true (sym (cong lower p))
  cut4360 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (op (op (var 1) (var 2)) (var 3)) (var 2))) , (var 1)) → ⊥
  cut4360  adequate = bad4360  (Adequate.valid adequate Two boolean env12)
  bad4361 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop (bop b0 b1) b1) b1)) b1 → ⊥
  bad4361  p = false≢true (cong lower p)
  cut4361 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (op (op (var 1) (var 2)) (var 3)) (var 2))) , (var 2)) → ⊥
  cut4361  adequate = bad4361  (Adequate.valid adequate Two boolean env7)
  bad4362 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop (bop b0 b0) b1) b0)) b1 → ⊥
  bad4362  p = false≢true (cong lower p)
  cut4362 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (op (op (var 1) (var 2)) (var 3)) (var 2))) , (var 3)) → ⊥
  cut4362  adequate = bad4362  (Adequate.valid adequate Two boolean env4)
  bad4363 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop (bop b0 b0) b0) b0)) b1 → ⊥
  bad4363  p = false≢true (cong lower p)
  cut4363 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (op (op (var 1) (var 2)) (var 3)) (var 2))) , (var 4)) → ⊥
  cut4363  adequate = bad4363  (Adequate.valid adequate Two boolean env8)
  env13 : ℕ → Two
  env13 zero = b0
  env13 (suc zero) = b1
  env13 (suc (suc zero)) = b1
  env13 (suc (suc (suc zero))) = b1
  env13 (suc (suc (suc (suc rest)))) = b0
  bad4364 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop (bop b1 b1) b1) b1)) b0 → ⊥
  bad4364  p = false≢true (sym (cong lower p))
  cut4364 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (op (op (var 1) (var 2)) (var 3)) (var 3))) , (var 0)) → ⊥
  cut4364  adequate = bad4364  (Adequate.valid adequate Two boolean env13)
  bad4365 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop (bop b1 b0) b0) b0)) b1 → ⊥
  bad4365  p = false≢true (cong lower p)
  cut4365 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (op (op (var 1) (var 2)) (var 3)) (var 3))) , (var 1)) → ⊥
  cut4365  adequate = bad4365  (Adequate.valid adequate Two boolean env11)
  bad4366 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop (bop b0 b1) b0) b0)) b1 → ⊥
  bad4366  p = false≢true (cong lower p)
  cut4366 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (op (op (var 1) (var 2)) (var 3)) (var 3))) , (var 2)) → ⊥
  cut4366  adequate = bad4366  (Adequate.valid adequate Two boolean env12)
  bad4367 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop (bop b0 b0) b1) b1)) b1 → ⊥
  bad4367  p = false≢true (cong lower p)
  cut4367 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (op (op (var 1) (var 2)) (var 3)) (var 3))) , (var 3)) → ⊥
  cut4367  adequate = bad4367  (Adequate.valid adequate Two boolean env4)
  bad4368 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop (bop b0 b0) b0) b0)) b1 → ⊥
  bad4368  p = false≢true (cong lower p)
  cut4368 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (op (op (var 1) (var 2)) (var 3)) (var 3))) , (var 4)) → ⊥
  cut4368  adequate = bad4368  (Adequate.valid adequate Two boolean env8)
  bad4369 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop (bop b0 b0) b0) b1)) b0 → ⊥
  bad4369  p = false≢true (sym (cong lower p))
  cut4369 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (op (op (var 1) (var 2)) (var 3)) (var 4))) , (var 0)) → ⊥
  cut4369  adequate = bad4369  (Adequate.valid adequate Two boolean env8)
  bad4370 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop (bop b0 b0) b0) b1)) b0 → ⊥
  bad4370  p = false≢true (sym (cong lower p))
  cut4370 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (op (op (var 1) (var 2)) (var 3)) (var 4))) , (var 1)) → ⊥
  cut4370  adequate = bad4370  (Adequate.valid adequate Two boolean env8)
  bad4371 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop (bop b0 b0) b0) b1)) b0 → ⊥
  bad4371  p = false≢true (sym (cong lower p))
  cut4371 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (op (op (var 1) (var 2)) (var 3)) (var 4))) , (var 2)) → ⊥
  cut4371  adequate = bad4371  (Adequate.valid adequate Two boolean env8)
  bad4372 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop (bop b0 b0) b0) b1)) b0 → ⊥
  bad4372  p = false≢true (sym (cong lower p))
  cut4372 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (op (op (var 1) (var 2)) (var 3)) (var 4))) , (var 3)) → ⊥
  cut4372  adequate = bad4372  (Adequate.valid adequate Two boolean env8)
  env14 : ℕ → Two
  env14 zero = b0
  env14 (suc zero) = b0
  env14 (suc (suc zero)) = b0
  env14 (suc (suc (suc zero))) = b1
  env14 (suc (suc (suc (suc zero)))) = b1
  env14 (suc (suc (suc (suc (suc rest))))) = b0
  bad4373 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop (bop b0 b0) b1) b1)) b1 → ⊥
  bad4373  p = false≢true (cong lower p)
  cut4373 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (op (op (var 1) (var 2)) (var 3)) (var 4))) , (var 4)) → ⊥
  cut4373  adequate = bad4373  (Adequate.valid adequate Two boolean env14)
  env15 : ℕ → Two
  env15 zero = b0
  env15 (suc zero) = b0
  env15 (suc (suc zero)) = b0
  env15 (suc (suc (suc zero))) = b0
  env15 (suc (suc (suc (suc zero)))) = b0
  env15 (suc (suc (suc (suc (suc zero))))) = b1
  env15 (suc (suc (suc (suc (suc (suc rest)))))) = b0
  bad4374 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop (bop b0 b0) b0) b0)) b1 → ⊥
  bad4374  p = false≢true (cong lower p)
  cut4374 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (op (op (var 1) (var 2)) (var 3)) (var 4))) , (var 5)) → ⊥
  cut4374  adequate = bad4374  (Adequate.valid adequate Two boolean env15)
  holds4375 : (z0 z1 : A2) → (mul2 (mul2 z0 z1) (mul2 (mul2 (mul2 z0 z0) z0) z0)) ≡ z0
  holds4375 z0 z1 = refl
  cut4375 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (op (var 0) (var 0)) (var 0)) (var 0))) , (var 0)) → ⊥
  cut4375  = reject2 ((op (op (var 0) (var 1)) (op (op (op (var 0) (var 0)) (var 0)) (var 0))) , (var 0)) (λ env → holds4375 (env 0) (env 1))
  bad4376 : PathP (λ _ → Two) (bop (bop b0 b1) (bop (bop (bop b0 b0) b0) b0)) b1 → ⊥
  bad4376  p = false≢true (cong lower p)
  cut4376 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (op (var 0) (var 0)) (var 0)) (var 0))) , (var 1)) → ⊥
  cut4376  adequate = bad4376  (Adequate.valid adequate Two boolean env0)
  bad4377 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop (bop b0 b0) b0) b0)) b1 → ⊥
  bad4377  p = false≢true (cong lower p)
  cut4377 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (op (var 0) (var 0)) (var 0)) (var 0))) , (var 2)) → ⊥
  cut4377  adequate = bad4377  (Adequate.valid adequate Two boolean env2)
  bad4378 : PathP (λ _ → Two) (bop (bop b0 b1) (bop (bop (bop b0 b0) b0) b1)) b0 → ⊥
  bad4378  p = false≢true (sym (cong lower p))
  cut4378 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (op (var 0) (var 0)) (var 0)) (var 1))) , (var 0)) → ⊥
  cut4378  adequate = bad4378  (Adequate.valid adequate Two boolean env0)
  holds4379 : (z0 z1 : A3) → (mul3 (mul3 z0 z1) (mul3 (mul3 (mul3 z0 z0) z0) z1)) ≡ z1
  holds4379 z0 z1 = refl
  cut4379 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (op (var 0) (var 0)) (var 0)) (var 1))) , (var 1)) → ⊥
  cut4379  = reject3 ((op (op (var 0) (var 1)) (op (op (op (var 0) (var 0)) (var 0)) (var 1))) , (var 1)) (λ env → holds4379 (env 0) (env 1))
  bad4380 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop (bop b0 b0) b0) b0)) b1 → ⊥
  bad4380  p = false≢true (cong lower p)
  cut4380 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (op (var 0) (var 0)) (var 0)) (var 1))) , (var 2)) → ⊥
  cut4380  adequate = bad4380  (Adequate.valid adequate Two boolean env2)
  bad4381 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop (bop b0 b0) b0) b1)) b0 → ⊥
  bad4381  p = false≢true (sym (cong lower p))
  cut4381 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (op (var 0) (var 0)) (var 0)) (var 2))) , (var 0)) → ⊥
  cut4381  adequate = bad4381  (Adequate.valid adequate Two boolean env2)
  bad4382 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop (bop b0 b0) b0) b1)) b0 → ⊥
  bad4382  p = false≢true (sym (cong lower p))
  cut4382 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (op (var 0) (var 0)) (var 0)) (var 2))) , (var 1)) → ⊥
  cut4382  adequate = bad4382  (Adequate.valid adequate Two boolean env2)
  env16 : ℕ → Two
  env16 zero = b1
  env16 (suc zero) = b1
  env16 (suc (suc zero)) = b0
  env16 (suc (suc (suc rest))) = b0
  bad4383 : PathP (λ _ → Two) (bop (bop b1 b1) (bop (bop (bop b1 b1) b1) b0)) b0 → ⊥
  bad4383  p = false≢true (sym (cong lower p))
  cut4383 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (op (var 0) (var 0)) (var 0)) (var 2))) , (var 2)) → ⊥
  cut4383  adequate = bad4383  (Adequate.valid adequate Two boolean env16)
  bad4384 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop (bop b0 b0) b0) b0)) b1 → ⊥
  bad4384  p = false≢true (cong lower p)
  cut4384 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (op (var 0) (var 0)) (var 0)) (var 2))) , (var 3)) → ⊥
  cut4384  adequate = bad4384  (Adequate.valid adequate Two boolean env4)
  holds4385 : (z0 z1 : A2) → (mul2 (mul2 z0 z1) (mul2 (mul2 (mul2 z0 z0) z1) z0)) ≡ z0
  holds4385 z0 z1 = refl
  cut4385 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (op (var 0) (var 0)) (var 1)) (var 0))) , (var 0)) → ⊥
  cut4385  = reject2 ((op (op (var 0) (var 1)) (op (op (op (var 0) (var 0)) (var 1)) (var 0))) , (var 0)) (λ env → holds4385 (env 0) (env 1))
  bad4386 : PathP (λ _ → Two) (bop (bop b0 b1) (bop (bop (bop b0 b0) b1) b0)) b1 → ⊥
  bad4386  p = false≢true (cong lower p)
  cut4386 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (op (var 0) (var 0)) (var 1)) (var 0))) , (var 1)) → ⊥
  cut4386  adequate = bad4386  (Adequate.valid adequate Two boolean env0)
  bad4387 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop (bop b0 b0) b0) b0)) b1 → ⊥
  bad4387  p = false≢true (cong lower p)
  cut4387 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (op (var 0) (var 0)) (var 1)) (var 0))) , (var 2)) → ⊥
  cut4387  adequate = bad4387  (Adequate.valid adequate Two boolean env2)
  bad4388 : PathP (λ _ → Two) (bop (bop b1 b0) (bop (bop (bop b1 b1) b0) b0)) b1 → ⊥
  bad4388  p = false≢true (cong lower p)
  cut4388 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (op (var 0) (var 0)) (var 1)) (var 1))) , (var 0)) → ⊥
  cut4388  adequate = bad4388  (Adequate.valid adequate Two boolean env1)
  bad4389 : PathP (λ _ → Two) (bop (bop b0 b1) (bop (bop (bop b0 b0) b1) b1)) b1 → ⊥
  bad4389  p = false≢true (cong lower p)
  cut4389 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (op (var 0) (var 0)) (var 1)) (var 1))) , (var 1)) → ⊥
  cut4389  adequate = bad4389  (Adequate.valid adequate Two boolean env0)
  bad4390 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop (bop b0 b0) b0) b0)) b1 → ⊥
  bad4390  p = false≢true (cong lower p)
  cut4390 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (op (var 0) (var 0)) (var 1)) (var 1))) , (var 2)) → ⊥
  cut4390  adequate = bad4390  (Adequate.valid adequate Two boolean env2)
  bad4391 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop (bop b0 b0) b0) b1)) b0 → ⊥
  bad4391  p = false≢true (sym (cong lower p))
  cut4391 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (op (var 0) (var 0)) (var 1)) (var 2))) , (var 0)) → ⊥
  cut4391  adequate = bad4391  (Adequate.valid adequate Two boolean env2)
  bad4392 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop (bop b0 b0) b0) b1)) b0 → ⊥
  bad4392  p = false≢true (sym (cong lower p))
  cut4392 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (op (var 0) (var 0)) (var 1)) (var 2))) , (var 1)) → ⊥
  cut4392  adequate = bad4392  (Adequate.valid adequate Two boolean env2)
  bad4393 : PathP (λ _ → Two) (bop (bop b0 b1) (bop (bop (bop b0 b0) b1) b1)) b1 → ⊥
  bad4393  p = false≢true (cong lower p)
  cut4393 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (op (var 0) (var 0)) (var 1)) (var 2))) , (var 2)) → ⊥
  cut4393  adequate = bad4393  (Adequate.valid adequate Two boolean env3)
  bad4394 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop (bop b0 b0) b0) b0)) b1 → ⊥
  bad4394  p = false≢true (cong lower p)
  cut4394 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (op (var 0) (var 0)) (var 1)) (var 2))) , (var 3)) → ⊥
  cut4394  adequate = bad4394  (Adequate.valid adequate Two boolean env4)
  holds4395 : (z0 z1 z2 : A2) → (mul2 (mul2 z0 z1) (mul2 (mul2 (mul2 z0 z0) z2) z0)) ≡ z0
  holds4395 z0 z1 z2 = refl
  cut4395 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (op (var 0) (var 0)) (var 2)) (var 0))) , (var 0)) → ⊥
  cut4395  = reject2 ((op (op (var 0) (var 1)) (op (op (op (var 0) (var 0)) (var 2)) (var 0))) , (var 0)) (λ env → holds4395 (env 0) (env 1) (env 2))
  bad4396 : PathP (λ _ → Two) (bop (bop b0 b1) (bop (bop (bop b0 b0) b0) b0)) b1 → ⊥
  bad4396  p = false≢true (cong lower p)
  cut4396 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (op (var 0) (var 0)) (var 2)) (var 0))) , (var 1)) → ⊥
  cut4396  adequate = bad4396  (Adequate.valid adequate Two boolean env6)
  bad4397 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop (bop b0 b0) b1) b0)) b1 → ⊥
  bad4397  p = false≢true (cong lower p)
  cut4397 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (op (var 0) (var 0)) (var 2)) (var 0))) , (var 2)) → ⊥
  cut4397  adequate = bad4397  (Adequate.valid adequate Two boolean env2)
  bad4398 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop (bop b0 b0) b0) b0)) b1 → ⊥
  bad4398  p = false≢true (cong lower p)
  cut4398 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (op (var 0) (var 0)) (var 2)) (var 0))) , (var 3)) → ⊥
  cut4398  adequate = bad4398  (Adequate.valid adequate Two boolean env4)
  bad4399 : PathP (λ _ → Two) (bop (bop b0 b1) (bop (bop (bop b0 b0) b0) b1)) b0 → ⊥
  bad4399  p = false≢true (sym (cong lower p))
  cut4399 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (op (var 0) (var 0)) (var 2)) (var 1))) , (var 0)) → ⊥
  cut4399  adequate = bad4399  (Adequate.valid adequate Two boolean env6)
  bad4400 : PathP (λ _ → Two) (bop (bop b0 b1) (bop (bop (bop b0 b0) b1) b1)) b1 → ⊥
  bad4400  p = false≢true (cong lower p)
  cut4400 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (op (var 0) (var 0)) (var 2)) (var 1))) , (var 1)) → ⊥
  cut4400  adequate = bad4400  (Adequate.valid adequate Two boolean env3)
  bad4401 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop (bop b0 b0) b1) b0)) b1 → ⊥
  bad4401  p = false≢true (cong lower p)
  cut4401 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (op (var 0) (var 0)) (var 2)) (var 1))) , (var 2)) → ⊥
  cut4401  adequate = bad4401  (Adequate.valid adequate Two boolean env2)
  bad4402 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop (bop b0 b0) b0) b0)) b1 → ⊥
  bad4402  p = false≢true (cong lower p)
  cut4402 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (op (var 0) (var 0)) (var 2)) (var 1))) , (var 3)) → ⊥
  cut4402  adequate = bad4402  (Adequate.valid adequate Two boolean env4)
  bad4403 : PathP (λ _ → Two) (bop (bop b1 b0) (bop (bop (bop b1 b1) b0) b0)) b1 → ⊥
  bad4403  p = false≢true (cong lower p)
  cut4403 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (op (var 0) (var 0)) (var 2)) (var 2))) , (var 0)) → ⊥
  cut4403  adequate = bad4403  (Adequate.valid adequate Two boolean env5)
  bad4404 : PathP (λ _ → Two) (bop (bop b0 b1) (bop (bop (bop b0 b0) b0) b0)) b1 → ⊥
  bad4404  p = false≢true (cong lower p)
  cut4404 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (op (var 0) (var 0)) (var 2)) (var 2))) , (var 1)) → ⊥
  cut4404  adequate = bad4404  (Adequate.valid adequate Two boolean env6)
  bad4405 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop (bop b0 b0) b1) b1)) b1 → ⊥
  bad4405  p = false≢true (cong lower p)
  cut4405 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (op (var 0) (var 0)) (var 2)) (var 2))) , (var 2)) → ⊥
  cut4405  adequate = bad4405  (Adequate.valid adequate Two boolean env2)
  bad4406 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop (bop b0 b0) b0) b0)) b1 → ⊥
  bad4406  p = false≢true (cong lower p)
  cut4406 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (op (var 0) (var 0)) (var 2)) (var 2))) , (var 3)) → ⊥
  cut4406  adequate = bad4406  (Adequate.valid adequate Two boolean env4)
  bad4407 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop (bop b0 b0) b0) b1)) b0 → ⊥
  bad4407  p = false≢true (sym (cong lower p))
  cut4407 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (op (var 0) (var 0)) (var 2)) (var 3))) , (var 0)) → ⊥
  cut4407  adequate = bad4407  (Adequate.valid adequate Two boolean env4)
  bad4408 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop (bop b0 b0) b0) b1)) b0 → ⊥
  bad4408  p = false≢true (sym (cong lower p))
  cut4408 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (op (var 0) (var 0)) (var 2)) (var 3))) , (var 1)) → ⊥
  cut4408  adequate = bad4408  (Adequate.valid adequate Two boolean env4)
  bad4409 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop (bop b0 b0) b0) b1)) b0 → ⊥
  bad4409  p = false≢true (sym (cong lower p))
  cut4409 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (op (var 0) (var 0)) (var 2)) (var 3))) , (var 2)) → ⊥
  cut4409  adequate = bad4409  (Adequate.valid adequate Two boolean env4)
  bad4410 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop (bop b0 b0) b1) b1)) b1 → ⊥
  bad4410  p = false≢true (cong lower p)
  cut4410 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (op (var 0) (var 0)) (var 2)) (var 3))) , (var 3)) → ⊥
  cut4410  adequate = bad4410  (Adequate.valid adequate Two boolean env7)
  bad4411 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop (bop b0 b0) b0) b0)) b1 → ⊥
  bad4411  p = false≢true (cong lower p)
  cut4411 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (op (var 0) (var 0)) (var 2)) (var 3))) , (var 4)) → ⊥
  cut4411  adequate = bad4411  (Adequate.valid adequate Two boolean env8)
  bad4412 : PathP (λ _ → Two) (bop (bop b1 b0) (bop (bop (bop b1 b0) b1) b1)) b1 → ⊥
  bad4412  p = false≢true (cong lower p)
  cut4412 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (op (var 0) (var 1)) (var 0)) (var 0))) , (var 0)) → ⊥
  cut4412  adequate = bad4412  (Adequate.valid adequate Two boolean env1)
  bad4413 : PathP (λ _ → Two) (bop (bop b0 b1) (bop (bop (bop b0 b1) b0) b0)) b1 → ⊥
  bad4413  p = false≢true (cong lower p)
  cut4413 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (op (var 0) (var 1)) (var 0)) (var 0))) , (var 1)) → ⊥
  cut4413  adequate = bad4413  (Adequate.valid adequate Two boolean env0)
  bad4414 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop (bop b0 b0) b0) b0)) b1 → ⊥
  bad4414  p = false≢true (cong lower p)
  cut4414 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (op (var 0) (var 1)) (var 0)) (var 0))) , (var 2)) → ⊥
  cut4414  adequate = bad4414  (Adequate.valid adequate Two boolean env2)
  bad4415 : PathP (λ _ → Two) (bop (bop b0 b1) (bop (bop (bop b0 b1) b0) b1)) b0 → ⊥
  bad4415  p = false≢true (sym (cong lower p))
  cut4415 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (op (var 0) (var 1)) (var 0)) (var 1))) , (var 0)) → ⊥
  cut4415  adequate = bad4415  (Adequate.valid adequate Two boolean env0)
  holds4416 : (z0 z1 : A3) → (mul3 (mul3 z0 z1) (mul3 (mul3 (mul3 z0 z1) z0) z1)) ≡ z1
  holds4416 z0 z1 = refl
  cut4416 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (op (var 0) (var 1)) (var 0)) (var 1))) , (var 1)) → ⊥
  cut4416  = reject3 ((op (op (var 0) (var 1)) (op (op (op (var 0) (var 1)) (var 0)) (var 1))) , (var 1)) (λ env → holds4416 (env 0) (env 1))
  bad4417 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop (bop b0 b0) b0) b0)) b1 → ⊥
  bad4417  p = false≢true (cong lower p)
  cut4417 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (op (var 0) (var 1)) (var 0)) (var 1))) , (var 2)) → ⊥
  cut4417  adequate = bad4417  (Adequate.valid adequate Two boolean env2)
  bad4418 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop (bop b0 b0) b0) b1)) b0 → ⊥
  bad4418  p = false≢true (sym (cong lower p))
  cut4418 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (op (var 0) (var 1)) (var 0)) (var 2))) , (var 0)) → ⊥
  cut4418  adequate = bad4418  (Adequate.valid adequate Two boolean env2)
  bad4419 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop (bop b0 b0) b0) b1)) b0 → ⊥
  bad4419  p = false≢true (sym (cong lower p))
  cut4419 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (op (var 0) (var 1)) (var 0)) (var 2))) , (var 1)) → ⊥
  cut4419  adequate = bad4419  (Adequate.valid adequate Two boolean env2)
  env17 : ℕ → Two
  env17 zero = b1
  env17 (suc zero) = b0
  env17 (suc (suc zero)) = b1
  env17 (suc (suc (suc rest))) = b0
  bad4420 : PathP (λ _ → Two) (bop (bop b1 b0) (bop (bop (bop b1 b0) b1) b1)) b1 → ⊥
  bad4420  p = false≢true (cong lower p)
  cut4420 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (op (var 0) (var 1)) (var 0)) (var 2))) , (var 2)) → ⊥
  cut4420  adequate = bad4420  (Adequate.valid adequate Two boolean env17)
  bad4421 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop (bop b0 b0) b0) b0)) b1 → ⊥
  bad4421  p = false≢true (cong lower p)
  cut4421 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (op (var 0) (var 1)) (var 0)) (var 2))) , (var 3)) → ⊥
  cut4421  adequate = bad4421  (Adequate.valid adequate Two boolean env4)
  holds4422 : (z0 z1 : A2) → (mul2 (mul2 z0 z1) (mul2 (mul2 (mul2 z0 z1) z1) z0)) ≡ z0
  holds4422 z0 z1 = refl
  cut4422 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (op (var 0) (var 1)) (var 1)) (var 0))) , (var 0)) → ⊥
  cut4422  = reject2 ((op (op (var 0) (var 1)) (op (op (op (var 0) (var 1)) (var 1)) (var 0))) , (var 0)) (λ env → holds4422 (env 0) (env 1))
  bad4423 : PathP (λ _ → Two) (bop (bop b0 b1) (bop (bop (bop b0 b1) b1) b0)) b1 → ⊥
  bad4423  p = false≢true (cong lower p)
  cut4423 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (op (var 0) (var 1)) (var 1)) (var 0))) , (var 1)) → ⊥
  cut4423  adequate = bad4423  (Adequate.valid adequate Two boolean env0)
  bad4424 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop (bop b0 b0) b0) b0)) b1 → ⊥
  bad4424  p = false≢true (cong lower p)
  cut4424 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (op (var 0) (var 1)) (var 1)) (var 0))) , (var 2)) → ⊥
  cut4424  adequate = bad4424  (Adequate.valid adequate Two boolean env2)
  bad4425 : PathP (λ _ → Two) (bop (bop b1 b0) (bop (bop (bop b1 b0) b0) b0)) b1 → ⊥
  bad4425  p = false≢true (cong lower p)
  cut4425 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (op (var 0) (var 1)) (var 1)) (var 1))) , (var 0)) → ⊥
  cut4425  adequate = bad4425  (Adequate.valid adequate Two boolean env1)
  bad4426 : PathP (λ _ → Two) (bop (bop b0 b1) (bop (bop (bop b0 b1) b1) b1)) b1 → ⊥
  bad4426  p = false≢true (cong lower p)
  cut4426 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (op (var 0) (var 1)) (var 1)) (var 1))) , (var 1)) → ⊥
  cut4426  adequate = bad4426  (Adequate.valid adequate Two boolean env0)
  bad4427 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop (bop b0 b0) b0) b0)) b1 → ⊥
  bad4427  p = false≢true (cong lower p)
  cut4427 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (op (var 0) (var 1)) (var 1)) (var 1))) , (var 2)) → ⊥
  cut4427  adequate = bad4427  (Adequate.valid adequate Two boolean env2)
  bad4428 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop (bop b0 b0) b0) b1)) b0 → ⊥
  bad4428  p = false≢true (sym (cong lower p))
  cut4428 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (op (var 0) (var 1)) (var 1)) (var 2))) , (var 0)) → ⊥
  cut4428  adequate = bad4428  (Adequate.valid adequate Two boolean env2)
  bad4429 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop (bop b0 b0) b0) b1)) b0 → ⊥
  bad4429  p = false≢true (sym (cong lower p))
  cut4429 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (op (var 0) (var 1)) (var 1)) (var 2))) , (var 1)) → ⊥
  cut4429  adequate = bad4429  (Adequate.valid adequate Two boolean env2)
  bad4430 : PathP (λ _ → Two) (bop (bop b0 b1) (bop (bop (bop b0 b1) b1) b1)) b1 → ⊥
  bad4430  p = false≢true (cong lower p)
  cut4430 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (op (var 0) (var 1)) (var 1)) (var 2))) , (var 2)) → ⊥
  cut4430  adequate = bad4430  (Adequate.valid adequate Two boolean env3)
  bad4431 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop (bop b0 b0) b0) b0)) b1 → ⊥
  bad4431  p = false≢true (cong lower p)
  cut4431 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (op (var 0) (var 1)) (var 1)) (var 2))) , (var 3)) → ⊥
  cut4431  adequate = bad4431  (Adequate.valid adequate Two boolean env4)
  bad4432 : PathP (λ _ → Two) (bop (bop b1 b0) (bop (bop (bop b1 b0) b1) b1)) b1 → ⊥
  bad4432  p = false≢true (cong lower p)
  cut4432 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (op (var 0) (var 1)) (var 2)) (var 0))) , (var 0)) → ⊥
  cut4432  adequate = bad4432  (Adequate.valid adequate Two boolean env17)
  bad4433 : PathP (λ _ → Two) (bop (bop b0 b1) (bop (bop (bop b0 b1) b0) b0)) b1 → ⊥
  bad4433  p = false≢true (cong lower p)
  cut4433 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (op (var 0) (var 1)) (var 2)) (var 0))) , (var 1)) → ⊥
  cut4433  adequate = bad4433  (Adequate.valid adequate Two boolean env6)
  bad4434 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop (bop b0 b0) b1) b0)) b1 → ⊥
  bad4434  p = false≢true (cong lower p)
  cut4434 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (op (var 0) (var 1)) (var 2)) (var 0))) , (var 2)) → ⊥
  cut4434  adequate = bad4434  (Adequate.valid adequate Two boolean env2)
  bad4435 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop (bop b0 b0) b0) b0)) b1 → ⊥
  bad4435  p = false≢true (cong lower p)
  cut4435 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (op (var 0) (var 1)) (var 2)) (var 0))) , (var 3)) → ⊥
  cut4435  adequate = bad4435  (Adequate.valid adequate Two boolean env4)
  bad4436 : PathP (λ _ → Two) (bop (bop b0 b1) (bop (bop (bop b0 b1) b0) b1)) b0 → ⊥
  bad4436  p = false≢true (sym (cong lower p))
  cut4436 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (op (var 0) (var 1)) (var 2)) (var 1))) , (var 0)) → ⊥
  cut4436  adequate = bad4436  (Adequate.valid adequate Two boolean env6)
  bad4437 : PathP (λ _ → Two) (bop (bop b0 b1) (bop (bop (bop b0 b1) b1) b1)) b1 → ⊥
  bad4437  p = false≢true (cong lower p)
  cut4437 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (op (var 0) (var 1)) (var 2)) (var 1))) , (var 1)) → ⊥
  cut4437  adequate = bad4437  (Adequate.valid adequate Two boolean env3)
  bad4438 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop (bop b0 b0) b1) b0)) b1 → ⊥
  bad4438  p = false≢true (cong lower p)
  cut4438 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (op (var 0) (var 1)) (var 2)) (var 1))) , (var 2)) → ⊥
  cut4438  adequate = bad4438  (Adequate.valid adequate Two boolean env2)
  bad4439 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop (bop b0 b0) b0) b0)) b1 → ⊥
  bad4439  p = false≢true (cong lower p)
  cut4439 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (op (var 0) (var 1)) (var 2)) (var 1))) , (var 3)) → ⊥
  cut4439  adequate = bad4439  (Adequate.valid adequate Two boolean env4)
  bad4440 : PathP (λ _ → Two) (bop (bop b1 b0) (bop (bop (bop b1 b0) b0) b0)) b1 → ⊥
  bad4440  p = false≢true (cong lower p)
  cut4440 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (op (var 0) (var 1)) (var 2)) (var 2))) , (var 0)) → ⊥
  cut4440  adequate = bad4440  (Adequate.valid adequate Two boolean env5)
  bad4441 : PathP (λ _ → Two) (bop (bop b0 b1) (bop (bop (bop b0 b1) b0) b0)) b1 → ⊥
  bad4441  p = false≢true (cong lower p)
  cut4441 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (op (var 0) (var 1)) (var 2)) (var 2))) , (var 1)) → ⊥
  cut4441  adequate = bad4441  (Adequate.valid adequate Two boolean env6)
  bad4442 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop (bop b0 b0) b1) b1)) b1 → ⊥
  bad4442  p = false≢true (cong lower p)
  cut4442 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (op (var 0) (var 1)) (var 2)) (var 2))) , (var 2)) → ⊥
  cut4442  adequate = bad4442  (Adequate.valid adequate Two boolean env2)
  bad4443 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop (bop b0 b0) b0) b0)) b1 → ⊥
  bad4443  p = false≢true (cong lower p)
  cut4443 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (op (var 0) (var 1)) (var 2)) (var 2))) , (var 3)) → ⊥
  cut4443  adequate = bad4443  (Adequate.valid adequate Two boolean env4)
  bad4444 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop (bop b0 b0) b0) b1)) b0 → ⊥
  bad4444  p = false≢true (sym (cong lower p))
  cut4444 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (op (var 0) (var 1)) (var 2)) (var 3))) , (var 0)) → ⊥
  cut4444  adequate = bad4444  (Adequate.valid adequate Two boolean env4)
  bad4445 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop (bop b0 b0) b0) b1)) b0 → ⊥
  bad4445  p = false≢true (sym (cong lower p))
  cut4445 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (op (var 0) (var 1)) (var 2)) (var 3))) , (var 1)) → ⊥
  cut4445  adequate = bad4445  (Adequate.valid adequate Two boolean env4)
  bad4446 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop (bop b0 b0) b0) b1)) b0 → ⊥
  bad4446  p = false≢true (sym (cong lower p))
  cut4446 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (op (var 0) (var 1)) (var 2)) (var 3))) , (var 2)) → ⊥
  cut4446  adequate = bad4446  (Adequate.valid adequate Two boolean env4)
  bad4447 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop (bop b0 b0) b1) b1)) b1 → ⊥
  bad4447  p = false≢true (cong lower p)
  cut4447 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (op (var 0) (var 1)) (var 2)) (var 3))) , (var 3)) → ⊥
  cut4447  adequate = bad4447  (Adequate.valid adequate Two boolean env7)
  bad4448 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop (bop b0 b0) b0) b0)) b1 → ⊥
  bad4448  p = false≢true (cong lower p)
  cut4448 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (op (var 0) (var 1)) (var 2)) (var 3))) , (var 4)) → ⊥
  cut4448  adequate = bad4448  (Adequate.valid adequate Two boolean env8)
  bad4449 : PathP (λ _ → Two) (bop (bop b1 b0) (bop (bop (bop b1 b0) b1) b1)) b1 → ⊥
  bad4449  p = false≢true (cong lower p)
  cut4449 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (op (var 0) (var 2)) (var 0)) (var 0))) , (var 0)) → ⊥
  cut4449  adequate = bad4449  (Adequate.valid adequate Two boolean env5)
  bad4450 : PathP (λ _ → Two) (bop (bop b0 b1) (bop (bop (bop b0 b0) b0) b0)) b1 → ⊥
  bad4450  p = false≢true (cong lower p)
  cut4450 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (op (var 0) (var 2)) (var 0)) (var 0))) , (var 1)) → ⊥
  cut4450  adequate = bad4450  (Adequate.valid adequate Two boolean env6)
  bad4451 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop (bop b0 b1) b0) b0)) b1 → ⊥
  bad4451  p = false≢true (cong lower p)
  cut4451 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (op (var 0) (var 2)) (var 0)) (var 0))) , (var 2)) → ⊥
  cut4451  adequate = bad4451  (Adequate.valid adequate Two boolean env2)
  bad4452 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop (bop b0 b0) b0) b0)) b1 → ⊥
  bad4452  p = false≢true (cong lower p)
  cut4452 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (op (var 0) (var 2)) (var 0)) (var 0))) , (var 3)) → ⊥
  cut4452  adequate = bad4452  (Adequate.valid adequate Two boolean env4)
  bad4453 : PathP (λ _ → Two) (bop (bop b0 b1) (bop (bop (bop b0 b0) b0) b1)) b0 → ⊥
  bad4453  p = false≢true (sym (cong lower p))
  cut4453 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (op (var 0) (var 2)) (var 0)) (var 1))) , (var 0)) → ⊥
  cut4453  adequate = bad4453  (Adequate.valid adequate Two boolean env6)
  holds4454 : (z0 z1 z2 : A3) → (mul3 (mul3 z0 z1) (mul3 (mul3 (mul3 z0 z2) z0) z1)) ≡ z1
  holds4454 z0 z1 z2 = refl
  cut4454 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (op (var 0) (var 2)) (var 0)) (var 1))) , (var 1)) → ⊥
  cut4454  = reject3 ((op (op (var 0) (var 1)) (op (op (op (var 0) (var 2)) (var 0)) (var 1))) , (var 1)) (λ env → holds4454 (env 0) (env 1) (env 2))
  bad4455 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop (bop b0 b1) b0) b0)) b1 → ⊥
  bad4455  p = false≢true (cong lower p)
  cut4455 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (op (var 0) (var 2)) (var 0)) (var 1))) , (var 2)) → ⊥
  cut4455  adequate = bad4455  (Adequate.valid adequate Two boolean env2)
  bad4456 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop (bop b0 b0) b0) b0)) b1 → ⊥
  bad4456  p = false≢true (cong lower p)
  cut4456 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (op (var 0) (var 2)) (var 0)) (var 1))) , (var 3)) → ⊥
  cut4456  adequate = bad4456  (Adequate.valid adequate Two boolean env4)
  bad4457 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop (bop b0 b1) b0) b1)) b0 → ⊥
  bad4457  p = false≢true (sym (cong lower p))
  cut4457 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (op (var 0) (var 2)) (var 0)) (var 2))) , (var 0)) → ⊥
  cut4457  adequate = bad4457  (Adequate.valid adequate Two boolean env2)
  bad4458 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop (bop b0 b1) b0) b1)) b0 → ⊥
  bad4458  p = false≢true (sym (cong lower p))
  cut4458 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (op (var 0) (var 2)) (var 0)) (var 2))) , (var 1)) → ⊥
  cut4458  adequate = bad4458  (Adequate.valid adequate Two boolean env2)
  bad4459 : PathP (λ _ → Two) (bop (bop b1 b1) (bop (bop (bop b1 b0) b1) b0)) b0 → ⊥
  bad4459  p = false≢true (sym (cong lower p))
  cut4459 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (op (var 0) (var 2)) (var 0)) (var 2))) , (var 2)) → ⊥
  cut4459  adequate = bad4459  (Adequate.valid adequate Two boolean env16)
  bad4460 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop (bop b0 b0) b0) b0)) b1 → ⊥
  bad4460  p = false≢true (cong lower p)
  cut4460 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (op (var 0) (var 2)) (var 0)) (var 2))) , (var 3)) → ⊥
  cut4460  adequate = bad4460  (Adequate.valid adequate Two boolean env4)
  bad4461 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop (bop b0 b0) b0) b1)) b0 → ⊥
  bad4461  p = false≢true (sym (cong lower p))
  cut4461 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (op (var 0) (var 2)) (var 0)) (var 3))) , (var 0)) → ⊥
  cut4461  adequate = bad4461  (Adequate.valid adequate Two boolean env4)
  bad4462 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop (bop b0 b0) b0) b1)) b0 → ⊥
  bad4462  p = false≢true (sym (cong lower p))
  cut4462 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (op (var 0) (var 2)) (var 0)) (var 3))) , (var 1)) → ⊥
  cut4462  adequate = bad4462  (Adequate.valid adequate Two boolean env4)
  bad4463 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop (bop b0 b0) b0) b1)) b0 → ⊥
  bad4463  p = false≢true (sym (cong lower p))
  cut4463 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (op (var 0) (var 2)) (var 0)) (var 3))) , (var 2)) → ⊥
  cut4463  adequate = bad4463  (Adequate.valid adequate Two boolean env4)
  env18 : ℕ → Two
  env18 zero = b1
  env18 (suc zero) = b0
  env18 (suc (suc zero)) = b0
  env18 (suc (suc (suc zero))) = b1
  env18 (suc (suc (suc (suc rest)))) = b0
  bad4464 : PathP (λ _ → Two) (bop (bop b1 b0) (bop (bop (bop b1 b0) b1) b1)) b1 → ⊥
  bad4464  p = false≢true (cong lower p)
  cut4464 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (op (var 0) (var 2)) (var 0)) (var 3))) , (var 3)) → ⊥
  cut4464  adequate = bad4464  (Adequate.valid adequate Two boolean env18)
  bad4465 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop (bop b0 b0) b0) b0)) b1 → ⊥
  bad4465  p = false≢true (cong lower p)
  cut4465 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (op (var 0) (var 2)) (var 0)) (var 3))) , (var 4)) → ⊥
  cut4465  adequate = bad4465  (Adequate.valid adequate Two boolean env8)
  holds4466 : (z0 z1 z2 : A2) → (mul2 (mul2 z0 z1) (mul2 (mul2 (mul2 z0 z2) z1) z0)) ≡ z0
  holds4466 z0 z1 z2 = refl
  cut4466 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (op (var 0) (var 2)) (var 1)) (var 0))) , (var 0)) → ⊥
  cut4466  = reject2 ((op (op (var 0) (var 1)) (op (op (op (var 0) (var 2)) (var 1)) (var 0))) , (var 0)) (λ env → holds4466 (env 0) (env 1) (env 2))
  bad4467 : PathP (λ _ → Two) (bop (bop b0 b1) (bop (bop (bop b0 b0) b1) b0)) b1 → ⊥
  bad4467  p = false≢true (cong lower p)
  cut4467 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (op (var 0) (var 2)) (var 1)) (var 0))) , (var 1)) → ⊥
  cut4467  adequate = bad4467  (Adequate.valid adequate Two boolean env6)
  bad4468 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop (bop b0 b1) b0) b0)) b1 → ⊥
  bad4468  p = false≢true (cong lower p)
  cut4468 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (op (var 0) (var 2)) (var 1)) (var 0))) , (var 2)) → ⊥
  cut4468  adequate = bad4468  (Adequate.valid adequate Two boolean env2)
  bad4469 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop (bop b0 b0) b0) b0)) b1 → ⊥
  bad4469  p = false≢true (cong lower p)
  cut4469 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (op (var 0) (var 2)) (var 1)) (var 0))) , (var 3)) → ⊥
  cut4469  adequate = bad4469  (Adequate.valid adequate Two boolean env4)
  bad4470 : PathP (λ _ → Two) (bop (bop b1 b0) (bop (bop (bop b1 b0) b0) b0)) b1 → ⊥
  bad4470  p = false≢true (cong lower p)
  cut4470 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (op (var 0) (var 2)) (var 1)) (var 1))) , (var 0)) → ⊥
  cut4470  adequate = bad4470  (Adequate.valid adequate Two boolean env5)
  bad4471 : PathP (λ _ → Two) (bop (bop b0 b1) (bop (bop (bop b0 b0) b1) b1)) b1 → ⊥
  bad4471  p = false≢true (cong lower p)
  cut4471 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (op (var 0) (var 2)) (var 1)) (var 1))) , (var 1)) → ⊥
  cut4471  adequate = bad4471  (Adequate.valid adequate Two boolean env6)
  bad4472 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop (bop b0 b1) b0) b0)) b1 → ⊥
  bad4472  p = false≢true (cong lower p)
  cut4472 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (op (var 0) (var 2)) (var 1)) (var 1))) , (var 2)) → ⊥
  cut4472  adequate = bad4472  (Adequate.valid adequate Two boolean env2)
  bad4473 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop (bop b0 b0) b0) b0)) b1 → ⊥
  bad4473  p = false≢true (cong lower p)
  cut4473 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (op (var 0) (var 2)) (var 1)) (var 1))) , (var 3)) → ⊥
  cut4473  adequate = bad4473  (Adequate.valid adequate Two boolean env4)
  bad4474 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop (bop b0 b1) b0) b1)) b0 → ⊥
  bad4474  p = false≢true (sym (cong lower p))
  cut4474 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (op (var 0) (var 2)) (var 1)) (var 2))) , (var 0)) → ⊥
  cut4474  adequate = bad4474  (Adequate.valid adequate Two boolean env2)
  bad4475 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop (bop b0 b1) b0) b1)) b0 → ⊥
  bad4475  p = false≢true (sym (cong lower p))
  cut4475 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (op (var 0) (var 2)) (var 1)) (var 2))) , (var 1)) → ⊥
  cut4475  adequate = bad4475  (Adequate.valid adequate Two boolean env2)
  bad4476 : PathP (λ _ → Two) (bop (bop b0 b1) (bop (bop (bop b0 b1) b1) b1)) b1 → ⊥
  bad4476  p = false≢true (cong lower p)
  cut4476 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (op (var 0) (var 2)) (var 1)) (var 2))) , (var 2)) → ⊥
  cut4476  adequate = bad4476  (Adequate.valid adequate Two boolean env3)
  bad4477 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop (bop b0 b0) b0) b0)) b1 → ⊥
  bad4477  p = false≢true (cong lower p)
  cut4477 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (op (var 0) (var 2)) (var 1)) (var 2))) , (var 3)) → ⊥
  cut4477  adequate = bad4477  (Adequate.valid adequate Two boolean env4)
  bad4478 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop (bop b0 b0) b0) b1)) b0 → ⊥
  bad4478  p = false≢true (sym (cong lower p))
  cut4478 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (op (var 0) (var 2)) (var 1)) (var 3))) , (var 0)) → ⊥
  cut4478  adequate = bad4478  (Adequate.valid adequate Two boolean env4)
  bad4479 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop (bop b0 b0) b0) b1)) b0 → ⊥
  bad4479  p = false≢true (sym (cong lower p))
  cut4479 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (op (var 0) (var 2)) (var 1)) (var 3))) , (var 1)) → ⊥
  cut4479  adequate = bad4479  (Adequate.valid adequate Two boolean env4)
  bad4480 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop (bop b0 b0) b0) b1)) b0 → ⊥
  bad4480  p = false≢true (sym (cong lower p))
  cut4480 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (op (var 0) (var 2)) (var 1)) (var 3))) , (var 2)) → ⊥
  cut4480  adequate = bad4480  (Adequate.valid adequate Two boolean env4)
  bad4481 : PathP (λ _ → Two) (bop (bop b0 b1) (bop (bop (bop b0 b0) b1) b1)) b1 → ⊥
  bad4481  p = false≢true (cong lower p)
  cut4481 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (op (var 0) (var 2)) (var 1)) (var 3))) , (var 3)) → ⊥
  cut4481  adequate = bad4481  (Adequate.valid adequate Two boolean env10)
  bad4482 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop (bop b0 b0) b0) b0)) b1 → ⊥
  bad4482  p = false≢true (cong lower p)
  cut4482 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (op (var 0) (var 2)) (var 1)) (var 3))) , (var 4)) → ⊥
  cut4482  adequate = bad4482  (Adequate.valid adequate Two boolean env8)
  holds4483 : (z0 z1 z2 : A2) → (mul2 (mul2 z0 z1) (mul2 (mul2 (mul2 z0 z2) z2) z0)) ≡ z0
  holds4483 z0 z1 z2 = refl
  cut4483 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (op (var 0) (var 2)) (var 2)) (var 0))) , (var 0)) → ⊥
  cut4483  = reject2 ((op (op (var 0) (var 1)) (op (op (op (var 0) (var 2)) (var 2)) (var 0))) , (var 0)) (λ env → holds4483 (env 0) (env 1) (env 2))
  bad4484 : PathP (λ _ → Two) (bop (bop b0 b1) (bop (bop (bop b0 b0) b0) b0)) b1 → ⊥
  bad4484  p = false≢true (cong lower p)
  cut4484 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (op (var 0) (var 2)) (var 2)) (var 0))) , (var 1)) → ⊥
  cut4484  adequate = bad4484  (Adequate.valid adequate Two boolean env6)
  bad4485 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop (bop b0 b1) b1) b0)) b1 → ⊥
  bad4485  p = false≢true (cong lower p)
  cut4485 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (op (var 0) (var 2)) (var 2)) (var 0))) , (var 2)) → ⊥
  cut4485  adequate = bad4485  (Adequate.valid adequate Two boolean env2)
  bad4486 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop (bop b0 b0) b0) b0)) b1 → ⊥
  bad4486  p = false≢true (cong lower p)
  cut4486 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (op (var 0) (var 2)) (var 2)) (var 0))) , (var 3)) → ⊥
  cut4486  adequate = bad4486  (Adequate.valid adequate Two boolean env4)
  bad4487 : PathP (λ _ → Two) (bop (bop b0 b1) (bop (bop (bop b0 b0) b0) b1)) b0 → ⊥
  bad4487  p = false≢true (sym (cong lower p))
  cut4487 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (op (var 0) (var 2)) (var 2)) (var 1))) , (var 0)) → ⊥
  cut4487  adequate = bad4487  (Adequate.valid adequate Two boolean env6)
  bad4488 : PathP (λ _ → Two) (bop (bop b0 b1) (bop (bop (bop b0 b1) b1) b1)) b1 → ⊥
  bad4488  p = false≢true (cong lower p)
  cut4488 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (op (var 0) (var 2)) (var 2)) (var 1))) , (var 1)) → ⊥
  cut4488  adequate = bad4488  (Adequate.valid adequate Two boolean env3)
  bad4489 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop (bop b0 b1) b1) b0)) b1 → ⊥
  bad4489  p = false≢true (cong lower p)
  cut4489 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (op (var 0) (var 2)) (var 2)) (var 1))) , (var 2)) → ⊥
  cut4489  adequate = bad4489  (Adequate.valid adequate Two boolean env2)
  bad4490 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop (bop b0 b0) b0) b0)) b1 → ⊥
  bad4490  p = false≢true (cong lower p)
  cut4490 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (op (var 0) (var 2)) (var 2)) (var 1))) , (var 3)) → ⊥
  cut4490  adequate = bad4490  (Adequate.valid adequate Two boolean env4)
  bad4491 : PathP (λ _ → Two) (bop (bop b1 b0) (bop (bop (bop b1 b0) b0) b0)) b1 → ⊥
  bad4491  p = false≢true (cong lower p)
  cut4491 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (op (var 0) (var 2)) (var 2)) (var 2))) , (var 0)) → ⊥
  cut4491  adequate = bad4491  (Adequate.valid adequate Two boolean env5)
  bad4492 : PathP (λ _ → Two) (bop (bop b0 b1) (bop (bop (bop b0 b0) b0) b0)) b1 → ⊥
  bad4492  p = false≢true (cong lower p)
  cut4492 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (op (var 0) (var 2)) (var 2)) (var 2))) , (var 1)) → ⊥
  cut4492  adequate = bad4492  (Adequate.valid adequate Two boolean env6)
  bad4493 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop (bop b0 b1) b1) b1)) b1 → ⊥
  bad4493  p = false≢true (cong lower p)
  cut4493 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (op (var 0) (var 2)) (var 2)) (var 2))) , (var 2)) → ⊥
  cut4493  adequate = bad4493  (Adequate.valid adequate Two boolean env2)
  bad4494 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop (bop b0 b0) b0) b0)) b1 → ⊥
  bad4494  p = false≢true (cong lower p)
  cut4494 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (op (var 0) (var 2)) (var 2)) (var 2))) , (var 3)) → ⊥
  cut4494  adequate = bad4494  (Adequate.valid adequate Two boolean env4)
  bad4495 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop (bop b0 b0) b0) b1)) b0 → ⊥
  bad4495  p = false≢true (sym (cong lower p))
  cut4495 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (op (var 0) (var 2)) (var 2)) (var 3))) , (var 0)) → ⊥
  cut4495  adequate = bad4495  (Adequate.valid adequate Two boolean env4)
  bad4496 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop (bop b0 b0) b0) b1)) b0 → ⊥
  bad4496  p = false≢true (sym (cong lower p))
  cut4496 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (op (var 0) (var 2)) (var 2)) (var 3))) , (var 1)) → ⊥
  cut4496  adequate = bad4496  (Adequate.valid adequate Two boolean env4)
  bad4497 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop (bop b0 b0) b0) b1)) b0 → ⊥
  bad4497  p = false≢true (sym (cong lower p))
  cut4497 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (op (var 0) (var 2)) (var 2)) (var 3))) , (var 2)) → ⊥
  cut4497  adequate = bad4497  (Adequate.valid adequate Two boolean env4)
  bad4498 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop (bop b0 b1) b1) b1)) b1 → ⊥
  bad4498  p = false≢true (cong lower p)
  cut4498 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (op (var 0) (var 2)) (var 2)) (var 3))) , (var 3)) → ⊥
  cut4498  adequate = bad4498  (Adequate.valid adequate Two boolean env7)
  bad4499 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop (bop b0 b0) b0) b0)) b1 → ⊥
  bad4499  p = false≢true (cong lower p)
  cut4499 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (op (var 0) (var 2)) (var 2)) (var 3))) , (var 4)) → ⊥
  cut4499  adequate = bad4499  (Adequate.valid adequate Two boolean env8)
  bad4500 : PathP (λ _ → Two) (bop (bop b1 b0) (bop (bop (bop b1 b0) b1) b1)) b1 → ⊥
  bad4500  p = false≢true (cong lower p)
  cut4500 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (op (var 0) (var 2)) (var 3)) (var 0))) , (var 0)) → ⊥
  cut4500  adequate = bad4500  (Adequate.valid adequate Two boolean env18)
  bad4501 : PathP (λ _ → Two) (bop (bop b0 b1) (bop (bop (bop b0 b0) b0) b0)) b1 → ⊥
  bad4501  p = false≢true (cong lower p)
  cut4501 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (op (var 0) (var 2)) (var 3)) (var 0))) , (var 1)) → ⊥
  cut4501  adequate = bad4501  (Adequate.valid adequate Two boolean env11)
  bad4502 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop (bop b0 b1) b0) b0)) b1 → ⊥
  bad4502  p = false≢true (cong lower p)
  cut4502 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (op (var 0) (var 2)) (var 3)) (var 0))) , (var 2)) → ⊥
  cut4502  adequate = bad4502  (Adequate.valid adequate Two boolean env12)
  bad4503 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop (bop b0 b0) b1) b0)) b1 → ⊥
  bad4503  p = false≢true (cong lower p)
  cut4503 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (op (var 0) (var 2)) (var 3)) (var 0))) , (var 3)) → ⊥
  cut4503  adequate = bad4503  (Adequate.valid adequate Two boolean env4)
  bad4504 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop (bop b0 b0) b0) b0)) b1 → ⊥
  bad4504  p = false≢true (cong lower p)
  cut4504 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (op (var 0) (var 2)) (var 3)) (var 0))) , (var 4)) → ⊥
  cut4504  adequate = bad4504  (Adequate.valid adequate Two boolean env8)
  bad4505 : PathP (λ _ → Two) (bop (bop b0 b1) (bop (bop (bop b0 b0) b0) b1)) b0 → ⊥
  bad4505  p = false≢true (sym (cong lower p))
  cut4505 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (op (var 0) (var 2)) (var 3)) (var 1))) , (var 0)) → ⊥
  cut4505  adequate = bad4505  (Adequate.valid adequate Two boolean env11)
  bad4506 : PathP (λ _ → Two) (bop (bop b0 b1) (bop (bop (bop b0 b0) b1) b1)) b1 → ⊥
  bad4506  p = false≢true (cong lower p)
  cut4506 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (op (var 0) (var 2)) (var 3)) (var 1))) , (var 1)) → ⊥
  cut4506  adequate = bad4506  (Adequate.valid adequate Two boolean env10)
  bad4507 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop (bop b0 b1) b0) b0)) b1 → ⊥
  bad4507  p = false≢true (cong lower p)
  cut4507 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (op (var 0) (var 2)) (var 3)) (var 1))) , (var 2)) → ⊥
  cut4507  adequate = bad4507  (Adequate.valid adequate Two boolean env12)
  bad4508 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop (bop b0 b0) b1) b0)) b1 → ⊥
  bad4508  p = false≢true (cong lower p)
  cut4508 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (op (var 0) (var 2)) (var 3)) (var 1))) , (var 3)) → ⊥
  cut4508  adequate = bad4508  (Adequate.valid adequate Two boolean env4)
  bad4509 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop (bop b0 b0) b0) b0)) b1 → ⊥
  bad4509  p = false≢true (cong lower p)
  cut4509 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (op (var 0) (var 2)) (var 3)) (var 1))) , (var 4)) → ⊥
  cut4509  adequate = bad4509  (Adequate.valid adequate Two boolean env8)
  bad4510 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop (bop b0 b1) b0) b1)) b0 → ⊥
  bad4510  p = false≢true (sym (cong lower p))
  cut4510 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (op (var 0) (var 2)) (var 3)) (var 2))) , (var 0)) → ⊥
  cut4510  adequate = bad4510  (Adequate.valid adequate Two boolean env12)
  bad4511 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop (bop b0 b1) b0) b1)) b0 → ⊥
  bad4511  p = false≢true (sym (cong lower p))
  cut4511 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (op (var 0) (var 2)) (var 3)) (var 2))) , (var 1)) → ⊥
  cut4511  adequate = bad4511  (Adequate.valid adequate Two boolean env12)
  bad4512 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop (bop b0 b1) b1) b1)) b1 → ⊥
  bad4512  p = false≢true (cong lower p)
  cut4512 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (op (var 0) (var 2)) (var 3)) (var 2))) , (var 2)) → ⊥
  cut4512  adequate = bad4512  (Adequate.valid adequate Two boolean env7)
  bad4513 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop (bop b0 b0) b1) b0)) b1 → ⊥
  bad4513  p = false≢true (cong lower p)
  cut4513 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (op (var 0) (var 2)) (var 3)) (var 2))) , (var 3)) → ⊥
  cut4513  adequate = bad4513  (Adequate.valid adequate Two boolean env4)
  bad4514 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop (bop b0 b0) b0) b0)) b1 → ⊥
  bad4514  p = false≢true (cong lower p)
  cut4514 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (op (var 0) (var 2)) (var 3)) (var 2))) , (var 4)) → ⊥
  cut4514  adequate = bad4514  (Adequate.valid adequate Two boolean env8)
  bad4515 : PathP (λ _ → Two) (bop (bop b1 b0) (bop (bop (bop b1 b0) b0) b0)) b1 → ⊥
  bad4515  p = false≢true (cong lower p)
  cut4515 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (op (var 0) (var 2)) (var 3)) (var 3))) , (var 0)) → ⊥
  cut4515  adequate = bad4515  (Adequate.valid adequate Two boolean env9)
  bad4516 : PathP (λ _ → Two) (bop (bop b0 b1) (bop (bop (bop b0 b0) b0) b0)) b1 → ⊥
  bad4516  p = false≢true (cong lower p)
  cut4516 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (op (var 0) (var 2)) (var 3)) (var 3))) , (var 1)) → ⊥
  cut4516  adequate = bad4516  (Adequate.valid adequate Two boolean env11)
  bad4517 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop (bop b0 b1) b0) b0)) b1 → ⊥
  bad4517  p = false≢true (cong lower p)
  cut4517 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (op (var 0) (var 2)) (var 3)) (var 3))) , (var 2)) → ⊥
  cut4517  adequate = bad4517  (Adequate.valid adequate Two boolean env12)
  bad4518 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop (bop b0 b0) b1) b1)) b1 → ⊥
  bad4518  p = false≢true (cong lower p)
  cut4518 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (op (var 0) (var 2)) (var 3)) (var 3))) , (var 3)) → ⊥
  cut4518  adequate = bad4518  (Adequate.valid adequate Two boolean env4)
  bad4519 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop (bop b0 b0) b0) b0)) b1 → ⊥
  bad4519  p = false≢true (cong lower p)
  cut4519 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (op (var 0) (var 2)) (var 3)) (var 3))) , (var 4)) → ⊥
  cut4519  adequate = bad4519  (Adequate.valid adequate Two boolean env8)
  bad4520 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop (bop b0 b0) b0) b1)) b0 → ⊥
  bad4520  p = false≢true (sym (cong lower p))
  cut4520 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (op (var 0) (var 2)) (var 3)) (var 4))) , (var 0)) → ⊥
  cut4520  adequate = bad4520  (Adequate.valid adequate Two boolean env8)
  bad4521 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop (bop b0 b0) b0) b1)) b0 → ⊥
  bad4521  p = false≢true (sym (cong lower p))
  cut4521 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (op (var 0) (var 2)) (var 3)) (var 4))) , (var 1)) → ⊥
  cut4521  adequate = bad4521  (Adequate.valid adequate Two boolean env8)
  bad4522 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop (bop b0 b0) b0) b1)) b0 → ⊥
  bad4522  p = false≢true (sym (cong lower p))
  cut4522 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (op (var 0) (var 2)) (var 3)) (var 4))) , (var 2)) → ⊥
  cut4522  adequate = bad4522  (Adequate.valid adequate Two boolean env8)
  bad4523 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop (bop b0 b0) b0) b1)) b0 → ⊥
  bad4523  p = false≢true (sym (cong lower p))
  cut4523 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (op (var 0) (var 2)) (var 3)) (var 4))) , (var 3)) → ⊥
  cut4523  adequate = bad4523  (Adequate.valid adequate Two boolean env8)
  bad4524 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop (bop b0 b0) b1) b1)) b1 → ⊥
  bad4524  p = false≢true (cong lower p)
  cut4524 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (op (var 0) (var 2)) (var 3)) (var 4))) , (var 4)) → ⊥
  cut4524  adequate = bad4524  (Adequate.valid adequate Two boolean env14)
  bad4525 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop (bop b0 b0) b0) b0)) b1 → ⊥
  bad4525  p = false≢true (cong lower p)
  cut4525 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (op (var 0) (var 2)) (var 3)) (var 4))) , (var 5)) → ⊥
  cut4525  adequate = bad4525  (Adequate.valid adequate Two boolean env15)
  bad4526 : PathP (λ _ → Two) (bop (bop b1 b0) (bop (bop (bop b0 b1) b1) b1)) b1 → ⊥
  bad4526  p = false≢true (cong lower p)
  cut4526 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (op (var 1) (var 0)) (var 0)) (var 0))) , (var 0)) → ⊥
  cut4526  adequate = bad4526  (Adequate.valid adequate Two boolean env1)
  bad4527 : PathP (λ _ → Two) (bop (bop b0 b1) (bop (bop (bop b1 b0) b0) b0)) b1 → ⊥
  bad4527  p = false≢true (cong lower p)
  cut4527 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (op (var 1) (var 0)) (var 0)) (var 0))) , (var 1)) → ⊥
  cut4527  adequate = bad4527  (Adequate.valid adequate Two boolean env0)
  bad4528 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop (bop b0 b0) b0) b0)) b1 → ⊥
  bad4528  p = false≢true (cong lower p)
  cut4528 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (op (var 1) (var 0)) (var 0)) (var 0))) , (var 2)) → ⊥
  cut4528  adequate = bad4528  (Adequate.valid adequate Two boolean env2)
  bad4529 : PathP (λ _ → Two) (bop (bop b0 b1) (bop (bop (bop b1 b0) b0) b1)) b0 → ⊥
  bad4529  p = false≢true (sym (cong lower p))
  cut4529 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (op (var 1) (var 0)) (var 0)) (var 1))) , (var 0)) → ⊥
  cut4529  adequate = bad4529  (Adequate.valid adequate Two boolean env0)
  holds4530 : (z0 z1 : A3) → (mul3 (mul3 z0 z1) (mul3 (mul3 (mul3 z1 z0) z0) z1)) ≡ z1
  holds4530 z0 z1 = refl
  cut4530 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (op (var 1) (var 0)) (var 0)) (var 1))) , (var 1)) → ⊥
  cut4530  = reject3 ((op (op (var 0) (var 1)) (op (op (op (var 1) (var 0)) (var 0)) (var 1))) , (var 1)) (λ env → holds4530 (env 0) (env 1))
  bad4531 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop (bop b0 b0) b0) b0)) b1 → ⊥
  bad4531  p = false≢true (cong lower p)
  cut4531 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (op (var 1) (var 0)) (var 0)) (var 1))) , (var 2)) → ⊥
  cut4531  adequate = bad4531  (Adequate.valid adequate Two boolean env2)
  bad4532 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop (bop b0 b0) b0) b1)) b0 → ⊥
  bad4532  p = false≢true (sym (cong lower p))
  cut4532 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (op (var 1) (var 0)) (var 0)) (var 2))) , (var 0)) → ⊥
  cut4532  adequate = bad4532  (Adequate.valid adequate Two boolean env2)
  bad4533 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop (bop b0 b0) b0) b1)) b0 → ⊥
  bad4533  p = false≢true (sym (cong lower p))
  cut4533 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (op (var 1) (var 0)) (var 0)) (var 2))) , (var 1)) → ⊥
  cut4533  adequate = bad4533  (Adequate.valid adequate Two boolean env2)
  bad4534 : PathP (λ _ → Two) (bop (bop b1 b0) (bop (bop (bop b0 b1) b1) b1)) b1 → ⊥
  bad4534  p = false≢true (cong lower p)
  cut4534 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (op (var 1) (var 0)) (var 0)) (var 2))) , (var 2)) → ⊥
  cut4534  adequate = bad4534  (Adequate.valid adequate Two boolean env17)
  bad4535 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop (bop b0 b0) b0) b0)) b1 → ⊥
  bad4535  p = false≢true (cong lower p)
  cut4535 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (op (var 1) (var 0)) (var 0)) (var 2))) , (var 3)) → ⊥
  cut4535  adequate = bad4535  (Adequate.valid adequate Two boolean env4)
  holds4536 : (z0 z1 : A2) → (mul2 (mul2 z0 z1) (mul2 (mul2 (mul2 z1 z0) z1) z0)) ≡ z0
  holds4536 z0 z1 = refl
  cut4536 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (op (var 1) (var 0)) (var 1)) (var 0))) , (var 0)) → ⊥
  cut4536  = reject2 ((op (op (var 0) (var 1)) (op (op (op (var 1) (var 0)) (var 1)) (var 0))) , (var 0)) (λ env → holds4536 (env 0) (env 1))
  bad4537 : PathP (λ _ → Two) (bop (bop b0 b1) (bop (bop (bop b1 b0) b1) b0)) b1 → ⊥
  bad4537  p = false≢true (cong lower p)
  cut4537 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (op (var 1) (var 0)) (var 1)) (var 0))) , (var 1)) → ⊥
  cut4537  adequate = bad4537  (Adequate.valid adequate Two boolean env0)
  bad4538 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop (bop b0 b0) b0) b0)) b1 → ⊥
  bad4538  p = false≢true (cong lower p)
  cut4538 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (op (var 1) (var 0)) (var 1)) (var 0))) , (var 2)) → ⊥
  cut4538  adequate = bad4538  (Adequate.valid adequate Two boolean env2)
  bad4539 : PathP (λ _ → Two) (bop (bop b1 b0) (bop (bop (bop b0 b1) b0) b0)) b1 → ⊥
  bad4539  p = false≢true (cong lower p)
  cut4539 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (op (var 1) (var 0)) (var 1)) (var 1))) , (var 0)) → ⊥
  cut4539  adequate = bad4539  (Adequate.valid adequate Two boolean env1)
  bad4540 : PathP (λ _ → Two) (bop (bop b0 b1) (bop (bop (bop b1 b0) b1) b1)) b1 → ⊥
  bad4540  p = false≢true (cong lower p)
  cut4540 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (op (var 1) (var 0)) (var 1)) (var 1))) , (var 1)) → ⊥
  cut4540  adequate = bad4540  (Adequate.valid adequate Two boolean env0)
  bad4541 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop (bop b0 b0) b0) b0)) b1 → ⊥
  bad4541  p = false≢true (cong lower p)
  cut4541 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (op (var 1) (var 0)) (var 1)) (var 1))) , (var 2)) → ⊥
  cut4541  adequate = bad4541  (Adequate.valid adequate Two boolean env2)
  bad4542 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop (bop b0 b0) b0) b1)) b0 → ⊥
  bad4542  p = false≢true (sym (cong lower p))
  cut4542 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (op (var 1) (var 0)) (var 1)) (var 2))) , (var 0)) → ⊥
  cut4542  adequate = bad4542  (Adequate.valid adequate Two boolean env2)
  bad4543 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop (bop b0 b0) b0) b1)) b0 → ⊥
  bad4543  p = false≢true (sym (cong lower p))
  cut4543 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (op (var 1) (var 0)) (var 1)) (var 2))) , (var 1)) → ⊥
  cut4543  adequate = bad4543  (Adequate.valid adequate Two boolean env2)
  bad4544 : PathP (λ _ → Two) (bop (bop b0 b1) (bop (bop (bop b1 b0) b1) b1)) b1 → ⊥
  bad4544  p = false≢true (cong lower p)
  cut4544 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (op (var 1) (var 0)) (var 1)) (var 2))) , (var 2)) → ⊥
  cut4544  adequate = bad4544  (Adequate.valid adequate Two boolean env3)
  bad4545 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop (bop b0 b0) b0) b0)) b1 → ⊥
  bad4545  p = false≢true (cong lower p)
  cut4545 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (op (var 1) (var 0)) (var 1)) (var 2))) , (var 3)) → ⊥
  cut4545  adequate = bad4545  (Adequate.valid adequate Two boolean env4)
  bad4546 : PathP (λ _ → Two) (bop (bop b1 b0) (bop (bop (bop b0 b1) b1) b1)) b1 → ⊥
  bad4546  p = false≢true (cong lower p)
  cut4546 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (op (var 1) (var 0)) (var 2)) (var 0))) , (var 0)) → ⊥
  cut4546  adequate = bad4546  (Adequate.valid adequate Two boolean env17)
  bad4547 : PathP (λ _ → Two) (bop (bop b0 b1) (bop (bop (bop b1 b0) b0) b0)) b1 → ⊥
  bad4547  p = false≢true (cong lower p)
  cut4547 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (op (var 1) (var 0)) (var 2)) (var 0))) , (var 1)) → ⊥
  cut4547  adequate = bad4547  (Adequate.valid adequate Two boolean env6)
  bad4548 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop (bop b0 b0) b1) b0)) b1 → ⊥
  bad4548  p = false≢true (cong lower p)
  cut4548 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (op (var 1) (var 0)) (var 2)) (var 0))) , (var 2)) → ⊥
  cut4548  adequate = bad4548  (Adequate.valid adequate Two boolean env2)
  bad4549 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop (bop b0 b0) b0) b0)) b1 → ⊥
  bad4549  p = false≢true (cong lower p)
  cut4549 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (op (var 1) (var 0)) (var 2)) (var 0))) , (var 3)) → ⊥
  cut4549  adequate = bad4549  (Adequate.valid adequate Two boolean env4)
  bad4550 : PathP (λ _ → Two) (bop (bop b0 b1) (bop (bop (bop b1 b0) b0) b1)) b0 → ⊥
  bad4550  p = false≢true (sym (cong lower p))
  cut4550 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (op (var 1) (var 0)) (var 2)) (var 1))) , (var 0)) → ⊥
  cut4550  adequate = bad4550  (Adequate.valid adequate Two boolean env6)
  bad4551 : PathP (λ _ → Two) (bop (bop b0 b1) (bop (bop (bop b1 b0) b1) b1)) b1 → ⊥
  bad4551  p = false≢true (cong lower p)
  cut4551 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (op (var 1) (var 0)) (var 2)) (var 1))) , (var 1)) → ⊥
  cut4551  adequate = bad4551  (Adequate.valid adequate Two boolean env3)
  bad4552 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop (bop b0 b0) b1) b0)) b1 → ⊥
  bad4552  p = false≢true (cong lower p)
  cut4552 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (op (var 1) (var 0)) (var 2)) (var 1))) , (var 2)) → ⊥
  cut4552  adequate = bad4552  (Adequate.valid adequate Two boolean env2)
  bad4553 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop (bop b0 b0) b0) b0)) b1 → ⊥
  bad4553  p = false≢true (cong lower p)
  cut4553 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (op (var 1) (var 0)) (var 2)) (var 1))) , (var 3)) → ⊥
  cut4553  adequate = bad4553  (Adequate.valid adequate Two boolean env4)
  bad4554 : PathP (λ _ → Two) (bop (bop b1 b0) (bop (bop (bop b0 b1) b0) b0)) b1 → ⊥
  bad4554  p = false≢true (cong lower p)
  cut4554 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (op (var 1) (var 0)) (var 2)) (var 2))) , (var 0)) → ⊥
  cut4554  adequate = bad4554  (Adequate.valid adequate Two boolean env5)
  bad4555 : PathP (λ _ → Two) (bop (bop b0 b1) (bop (bop (bop b1 b0) b0) b0)) b1 → ⊥
  bad4555  p = false≢true (cong lower p)
  cut4555 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (op (var 1) (var 0)) (var 2)) (var 2))) , (var 1)) → ⊥
  cut4555  adequate = bad4555  (Adequate.valid adequate Two boolean env6)
  bad4556 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop (bop b0 b0) b1) b1)) b1 → ⊥
  bad4556  p = false≢true (cong lower p)
  cut4556 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (op (var 1) (var 0)) (var 2)) (var 2))) , (var 2)) → ⊥
  cut4556  adequate = bad4556  (Adequate.valid adequate Two boolean env2)
  bad4557 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop (bop b0 b0) b0) b0)) b1 → ⊥
  bad4557  p = false≢true (cong lower p)
  cut4557 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (op (var 1) (var 0)) (var 2)) (var 2))) , (var 3)) → ⊥
  cut4557  adequate = bad4557  (Adequate.valid adequate Two boolean env4)
  bad4558 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop (bop b0 b0) b0) b1)) b0 → ⊥
  bad4558  p = false≢true (sym (cong lower p))
  cut4558 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (op (var 1) (var 0)) (var 2)) (var 3))) , (var 0)) → ⊥
  cut4558  adequate = bad4558  (Adequate.valid adequate Two boolean env4)
  bad4559 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop (bop b0 b0) b0) b1)) b0 → ⊥
  bad4559  p = false≢true (sym (cong lower p))
  cut4559 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (op (var 1) (var 0)) (var 2)) (var 3))) , (var 1)) → ⊥
  cut4559  adequate = bad4559  (Adequate.valid adequate Two boolean env4)
  bad4560 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop (bop b0 b0) b0) b1)) b0 → ⊥
  bad4560  p = false≢true (sym (cong lower p))
  cut4560 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (op (var 1) (var 0)) (var 2)) (var 3))) , (var 2)) → ⊥
  cut4560  adequate = bad4560  (Adequate.valid adequate Two boolean env4)
  bad4561 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop (bop b0 b0) b1) b1)) b1 → ⊥
  bad4561  p = false≢true (cong lower p)
  cut4561 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (op (var 1) (var 0)) (var 2)) (var 3))) , (var 3)) → ⊥
  cut4561  adequate = bad4561  (Adequate.valid adequate Two boolean env7)
  bad4562 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop (bop b0 b0) b0) b0)) b1 → ⊥
  bad4562  p = false≢true (cong lower p)
  cut4562 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (op (var 1) (var 0)) (var 2)) (var 3))) , (var 4)) → ⊥
  cut4562  adequate = bad4562  (Adequate.valid adequate Two boolean env8)
  bad4563 : PathP (λ _ → Two) (bop (bop b1 b0) (bop (bop (bop b0 b0) b1) b1)) b1 → ⊥
  bad4563  p = false≢true (cong lower p)
  cut4563 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (op (var 1) (var 1)) (var 0)) (var 0))) , (var 0)) → ⊥
  cut4563  adequate = bad4563  (Adequate.valid adequate Two boolean env1)
  bad4564 : PathP (λ _ → Two) (bop (bop b0 b1) (bop (bop (bop b1 b1) b0) b0)) b1 → ⊥
  bad4564  p = false≢true (cong lower p)
  cut4564 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (op (var 1) (var 1)) (var 0)) (var 0))) , (var 1)) → ⊥
  cut4564  adequate = bad4564  (Adequate.valid adequate Two boolean env0)
  bad4565 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop (bop b0 b0) b0) b0)) b1 → ⊥
  bad4565  p = false≢true (cong lower p)
  cut4565 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (op (var 1) (var 1)) (var 0)) (var 0))) , (var 2)) → ⊥
  cut4565  adequate = bad4565  (Adequate.valid adequate Two boolean env2)
  bad4566 : PathP (λ _ → Two) (bop (bop b0 b1) (bop (bop (bop b1 b1) b0) b1)) b0 → ⊥
  bad4566  p = false≢true (sym (cong lower p))
  cut4566 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (op (var 1) (var 1)) (var 0)) (var 1))) , (var 0)) → ⊥
  cut4566  adequate = bad4566  (Adequate.valid adequate Two boolean env0)
  holds4567 : (z0 z1 : A3) → (mul3 (mul3 z0 z1) (mul3 (mul3 (mul3 z1 z1) z0) z1)) ≡ z1
  holds4567 z0 z1 = refl
  cut4567 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (op (var 1) (var 1)) (var 0)) (var 1))) , (var 1)) → ⊥
  cut4567  = reject3 ((op (op (var 0) (var 1)) (op (op (op (var 1) (var 1)) (var 0)) (var 1))) , (var 1)) (λ env → holds4567 (env 0) (env 1))
  bad4568 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop (bop b0 b0) b0) b0)) b1 → ⊥
  bad4568  p = false≢true (cong lower p)
  cut4568 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (op (var 1) (var 1)) (var 0)) (var 1))) , (var 2)) → ⊥
  cut4568  adequate = bad4568  (Adequate.valid adequate Two boolean env2)
  bad4569 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop (bop b0 b0) b0) b1)) b0 → ⊥
  bad4569  p = false≢true (sym (cong lower p))
  cut4569 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (op (var 1) (var 1)) (var 0)) (var 2))) , (var 0)) → ⊥
  cut4569  adequate = bad4569  (Adequate.valid adequate Two boolean env2)
  bad4570 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop (bop b0 b0) b0) b1)) b0 → ⊥
  bad4570  p = false≢true (sym (cong lower p))
  cut4570 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (op (var 1) (var 1)) (var 0)) (var 2))) , (var 1)) → ⊥
  cut4570  adequate = bad4570  (Adequate.valid adequate Two boolean env2)
  bad4571 : PathP (λ _ → Two) (bop (bop b1 b0) (bop (bop (bop b0 b0) b1) b1)) b1 → ⊥
  bad4571  p = false≢true (cong lower p)
  cut4571 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (op (var 1) (var 1)) (var 0)) (var 2))) , (var 2)) → ⊥
  cut4571  adequate = bad4571  (Adequate.valid adequate Two boolean env17)
  bad4572 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop (bop b0 b0) b0) b0)) b1 → ⊥
  bad4572  p = false≢true (cong lower p)
  cut4572 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (op (var 1) (var 1)) (var 0)) (var 2))) , (var 3)) → ⊥
  cut4572  adequate = bad4572  (Adequate.valid adequate Two boolean env4)
  holds4573 : (z0 z1 : A2) → (mul2 (mul2 z0 z1) (mul2 (mul2 (mul2 z1 z1) z1) z0)) ≡ z0
  holds4573 z0 z1 = refl
  cut4573 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (op (var 1) (var 1)) (var 1)) (var 0))) , (var 0)) → ⊥
  cut4573  = reject2 ((op (op (var 0) (var 1)) (op (op (op (var 1) (var 1)) (var 1)) (var 0))) , (var 0)) (λ env → holds4573 (env 0) (env 1))
  bad4574 : PathP (λ _ → Two) (bop (bop b0 b1) (bop (bop (bop b1 b1) b1) b0)) b1 → ⊥
  bad4574  p = false≢true (cong lower p)
  cut4574 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (op (var 1) (var 1)) (var 1)) (var 0))) , (var 1)) → ⊥
  cut4574  adequate = bad4574  (Adequate.valid adequate Two boolean env0)
  bad4575 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop (bop b0 b0) b0) b0)) b1 → ⊥
  bad4575  p = false≢true (cong lower p)
  cut4575 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (op (var 1) (var 1)) (var 1)) (var 0))) , (var 2)) → ⊥
  cut4575  adequate = bad4575  (Adequate.valid adequate Two boolean env2)
  bad4576 : PathP (λ _ → Two) (bop (bop b0 b1) (bop (bop (bop b1 b1) b1) b1)) b0 → ⊥
  bad4576  p = false≢true (sym (cong lower p))
  cut4576 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (op (var 1) (var 1)) (var 1)) (var 1))) , (var 0)) → ⊥
  cut4576  adequate = bad4576  (Adequate.valid adequate Two boolean env0)
  holds4577 : (z0 z1 : A3) → (mul3 (mul3 z0 z1) (mul3 (mul3 (mul3 z1 z1) z1) z1)) ≡ z1
  holds4577 z0 z1 = refl
  cut4577 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (op (var 1) (var 1)) (var 1)) (var 1))) , (var 1)) → ⊥
  cut4577  = reject3 ((op (op (var 0) (var 1)) (op (op (op (var 1) (var 1)) (var 1)) (var 1))) , (var 1)) (λ env → holds4577 (env 0) (env 1))
  bad4578 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop (bop b0 b0) b0) b0)) b1 → ⊥
  bad4578  p = false≢true (cong lower p)
  cut4578 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (op (var 1) (var 1)) (var 1)) (var 1))) , (var 2)) → ⊥
  cut4578  adequate = bad4578  (Adequate.valid adequate Two boolean env2)
  bad4579 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop (bop b0 b0) b0) b1)) b0 → ⊥
  bad4579  p = false≢true (sym (cong lower p))
  cut4579 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (op (var 1) (var 1)) (var 1)) (var 2))) , (var 0)) → ⊥
  cut4579  adequate = bad4579  (Adequate.valid adequate Two boolean env2)
  bad4580 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop (bop b0 b0) b0) b1)) b0 → ⊥
  bad4580  p = false≢true (sym (cong lower p))
  cut4580 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (op (var 1) (var 1)) (var 1)) (var 2))) , (var 1)) → ⊥
  cut4580  adequate = bad4580  (Adequate.valid adequate Two boolean env2)
  bad4581 : PathP (λ _ → Two) (bop (bop b1 b1) (bop (bop (bop b1 b1) b1) b0)) b0 → ⊥
  bad4581  p = false≢true (sym (cong lower p))
  cut4581 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (op (var 1) (var 1)) (var 1)) (var 2))) , (var 2)) → ⊥
  cut4581  adequate = bad4581  (Adequate.valid adequate Two boolean env16)
  bad4582 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop (bop b0 b0) b0) b0)) b1 → ⊥
  bad4582  p = false≢true (cong lower p)
  cut4582 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (op (var 1) (var 1)) (var 1)) (var 2))) , (var 3)) → ⊥
  cut4582  adequate = bad4582  (Adequate.valid adequate Two boolean env4)
  bad4583 : PathP (λ _ → Two) (bop (bop b1 b0) (bop (bop (bop b0 b0) b1) b1)) b1 → ⊥
  bad4583  p = false≢true (cong lower p)
  cut4583 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (op (var 1) (var 1)) (var 2)) (var 0))) , (var 0)) → ⊥
  cut4583  adequate = bad4583  (Adequate.valid adequate Two boolean env17)
  bad4584 : PathP (λ _ → Two) (bop (bop b0 b1) (bop (bop (bop b1 b1) b0) b0)) b1 → ⊥
  bad4584  p = false≢true (cong lower p)
  cut4584 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (op (var 1) (var 1)) (var 2)) (var 0))) , (var 1)) → ⊥
  cut4584  adequate = bad4584  (Adequate.valid adequate Two boolean env6)
  bad4585 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop (bop b0 b0) b1) b0)) b1 → ⊥
  bad4585  p = false≢true (cong lower p)
  cut4585 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (op (var 1) (var 1)) (var 2)) (var 0))) , (var 2)) → ⊥
  cut4585  adequate = bad4585  (Adequate.valid adequate Two boolean env2)
  bad4586 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop (bop b0 b0) b0) b0)) b1 → ⊥
  bad4586  p = false≢true (cong lower p)
  cut4586 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (op (var 1) (var 1)) (var 2)) (var 0))) , (var 3)) → ⊥
  cut4586  adequate = bad4586  (Adequate.valid adequate Two boolean env4)
  bad4587 : PathP (λ _ → Two) (bop (bop b0 b1) (bop (bop (bop b1 b1) b0) b1)) b0 → ⊥
  bad4587  p = false≢true (sym (cong lower p))
  cut4587 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (op (var 1) (var 1)) (var 2)) (var 1))) , (var 0)) → ⊥
  cut4587  adequate = bad4587  (Adequate.valid adequate Two boolean env6)
  holds4588 : (z0 z1 z2 : A3) → (mul3 (mul3 z0 z1) (mul3 (mul3 (mul3 z1 z1) z2) z1)) ≡ z1
  holds4588 z0 z1 z2 = refl
  cut4588 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (op (var 1) (var 1)) (var 2)) (var 1))) , (var 1)) → ⊥
  cut4588  = reject3 ((op (op (var 0) (var 1)) (op (op (op (var 1) (var 1)) (var 2)) (var 1))) , (var 1)) (λ env → holds4588 (env 0) (env 1) (env 2))
  bad4589 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop (bop b0 b0) b1) b0)) b1 → ⊥
  bad4589  p = false≢true (cong lower p)
  cut4589 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (op (var 1) (var 1)) (var 2)) (var 1))) , (var 2)) → ⊥
  cut4589  adequate = bad4589  (Adequate.valid adequate Two boolean env2)
  bad4590 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop (bop b0 b0) b0) b0)) b1 → ⊥
  bad4590  p = false≢true (cong lower p)
  cut4590 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (op (var 1) (var 1)) (var 2)) (var 1))) , (var 3)) → ⊥
  cut4590  adequate = bad4590  (Adequate.valid adequate Two boolean env4)
  bad4591 : PathP (λ _ → Two) (bop (bop b0 b1) (bop (bop (bop b1 b1) b1) b1)) b0 → ⊥
  bad4591  p = false≢true (sym (cong lower p))
  cut4591 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (op (var 1) (var 1)) (var 2)) (var 2))) , (var 0)) → ⊥
  cut4591  adequate = bad4591  (Adequate.valid adequate Two boolean env3)
  bad4592 : PathP (λ _ → Two) (bop (bop b0 b1) (bop (bop (bop b1 b1) b0) b0)) b1 → ⊥
  bad4592  p = false≢true (cong lower p)
  cut4592 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (op (var 1) (var 1)) (var 2)) (var 2))) , (var 1)) → ⊥
  cut4592  adequate = bad4592  (Adequate.valid adequate Two boolean env6)
  bad4593 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop (bop b0 b0) b1) b1)) b1 → ⊥
  bad4593  p = false≢true (cong lower p)
  cut4593 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (op (var 1) (var 1)) (var 2)) (var 2))) , (var 2)) → ⊥
  cut4593  adequate = bad4593  (Adequate.valid adequate Two boolean env2)
  bad4594 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop (bop b0 b0) b0) b0)) b1 → ⊥
  bad4594  p = false≢true (cong lower p)
  cut4594 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (op (var 1) (var 1)) (var 2)) (var 2))) , (var 3)) → ⊥
  cut4594  adequate = bad4594  (Adequate.valid adequate Two boolean env4)
  bad4595 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop (bop b0 b0) b0) b1)) b0 → ⊥
  bad4595  p = false≢true (sym (cong lower p))
  cut4595 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (op (var 1) (var 1)) (var 2)) (var 3))) , (var 0)) → ⊥
  cut4595  adequate = bad4595  (Adequate.valid adequate Two boolean env4)
  bad4596 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop (bop b0 b0) b0) b1)) b0 → ⊥
  bad4596  p = false≢true (sym (cong lower p))
  cut4596 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (op (var 1) (var 1)) (var 2)) (var 3))) , (var 1)) → ⊥
  cut4596  adequate = bad4596  (Adequate.valid adequate Two boolean env4)
  bad4597 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop (bop b0 b0) b0) b1)) b0 → ⊥
  bad4597  p = false≢true (sym (cong lower p))
  cut4597 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (op (var 1) (var 1)) (var 2)) (var 3))) , (var 2)) → ⊥
  cut4597  adequate = bad4597  (Adequate.valid adequate Two boolean env4)
  bad4598 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop (bop b0 b0) b1) b1)) b1 → ⊥
  bad4598  p = false≢true (cong lower p)
  cut4598 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (op (var 1) (var 1)) (var 2)) (var 3))) , (var 3)) → ⊥
  cut4598  adequate = bad4598  (Adequate.valid adequate Two boolean env7)
  bad4599 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop (bop b0 b0) b0) b0)) b1 → ⊥
  bad4599  p = false≢true (cong lower p)
  cut4599 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (op (var 1) (var 1)) (var 2)) (var 3))) , (var 4)) → ⊥
  cut4599  adequate = bad4599  (Adequate.valid adequate Two boolean env8)
  bad4600 : PathP (λ _ → Two) (bop (bop b1 b0) (bop (bop (bop b0 b0) b1) b1)) b1 → ⊥
  bad4600  p = false≢true (cong lower p)
  cut4600 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (op (var 1) (var 2)) (var 0)) (var 0))) , (var 0)) → ⊥
  cut4600  adequate = bad4600  (Adequate.valid adequate Two boolean env5)
  bad4601 : PathP (λ _ → Two) (bop (bop b0 b1) (bop (bop (bop b1 b0) b0) b0)) b1 → ⊥
  bad4601  p = false≢true (cong lower p)
  cut4601 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (op (var 1) (var 2)) (var 0)) (var 0))) , (var 1)) → ⊥
  cut4601  adequate = bad4601  (Adequate.valid adequate Two boolean env6)
  bad4602 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop (bop b0 b1) b0) b0)) b1 → ⊥
  bad4602  p = false≢true (cong lower p)
  cut4602 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (op (var 1) (var 2)) (var 0)) (var 0))) , (var 2)) → ⊥
  cut4602  adequate = bad4602  (Adequate.valid adequate Two boolean env2)
  bad4603 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop (bop b0 b0) b0) b0)) b1 → ⊥
  bad4603  p = false≢true (cong lower p)
  cut4603 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (op (var 1) (var 2)) (var 0)) (var 0))) , (var 3)) → ⊥
  cut4603  adequate = bad4603  (Adequate.valid adequate Two boolean env4)
  bad4604 : PathP (λ _ → Two) (bop (bop b0 b1) (bop (bop (bop b1 b0) b0) b1)) b0 → ⊥
  bad4604  p = false≢true (sym (cong lower p))
  cut4604 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (op (var 1) (var 2)) (var 0)) (var 1))) , (var 0)) → ⊥
  cut4604  adequate = bad4604  (Adequate.valid adequate Two boolean env6)
  holds4605 : (z0 z1 z2 : A3) → (mul3 (mul3 z0 z1) (mul3 (mul3 (mul3 z1 z2) z0) z1)) ≡ z1
  holds4605 z0 z1 z2 = refl
  cut4605 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (op (var 1) (var 2)) (var 0)) (var 1))) , (var 1)) → ⊥
  cut4605  = reject3 ((op (op (var 0) (var 1)) (op (op (op (var 1) (var 2)) (var 0)) (var 1))) , (var 1)) (λ env → holds4605 (env 0) (env 1) (env 2))
  bad4606 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop (bop b0 b1) b0) b0)) b1 → ⊥
  bad4606  p = false≢true (cong lower p)
  cut4606 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (op (var 1) (var 2)) (var 0)) (var 1))) , (var 2)) → ⊥
  cut4606  adequate = bad4606  (Adequate.valid adequate Two boolean env2)
  bad4607 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop (bop b0 b0) b0) b0)) b1 → ⊥
  bad4607  p = false≢true (cong lower p)
  cut4607 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (op (var 1) (var 2)) (var 0)) (var 1))) , (var 3)) → ⊥
  cut4607  adequate = bad4607  (Adequate.valid adequate Two boolean env4)
  bad4608 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop (bop b0 b1) b0) b1)) b0 → ⊥
  bad4608  p = false≢true (sym (cong lower p))
  cut4608 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (op (var 1) (var 2)) (var 0)) (var 2))) , (var 0)) → ⊥
  cut4608  adequate = bad4608  (Adequate.valid adequate Two boolean env2)
  bad4609 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop (bop b0 b1) b0) b1)) b0 → ⊥
  bad4609  p = false≢true (sym (cong lower p))
  cut4609 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (op (var 1) (var 2)) (var 0)) (var 2))) , (var 1)) → ⊥
  cut4609  adequate = bad4609  (Adequate.valid adequate Two boolean env2)
  bad4610 : PathP (λ _ → Two) (bop (bop b1 b0) (bop (bop (bop b0 b1) b1) b1)) b1 → ⊥
  bad4610  p = false≢true (cong lower p)
  cut4610 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (op (var 1) (var 2)) (var 0)) (var 2))) , (var 2)) → ⊥
  cut4610  adequate = bad4610  (Adequate.valid adequate Two boolean env17)
  bad4611 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop (bop b0 b0) b0) b0)) b1 → ⊥
  bad4611  p = false≢true (cong lower p)
  cut4611 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (op (var 1) (var 2)) (var 0)) (var 2))) , (var 3)) → ⊥
  cut4611  adequate = bad4611  (Adequate.valid adequate Two boolean env4)
  bad4612 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop (bop b0 b0) b0) b1)) b0 → ⊥
  bad4612  p = false≢true (sym (cong lower p))
  cut4612 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (op (var 1) (var 2)) (var 0)) (var 3))) , (var 0)) → ⊥
  cut4612  adequate = bad4612  (Adequate.valid adequate Two boolean env4)
  bad4613 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop (bop b0 b0) b0) b1)) b0 → ⊥
  bad4613  p = false≢true (sym (cong lower p))
  cut4613 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (op (var 1) (var 2)) (var 0)) (var 3))) , (var 1)) → ⊥
  cut4613  adequate = bad4613  (Adequate.valid adequate Two boolean env4)
  bad4614 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop (bop b0 b0) b0) b1)) b0 → ⊥
  bad4614  p = false≢true (sym (cong lower p))
  cut4614 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (op (var 1) (var 2)) (var 0)) (var 3))) , (var 2)) → ⊥
  cut4614  adequate = bad4614  (Adequate.valid adequate Two boolean env4)
  bad4615 : PathP (λ _ → Two) (bop (bop b1 b0) (bop (bop (bop b0 b0) b1) b1)) b1 → ⊥
  bad4615  p = false≢true (cong lower p)
  cut4615 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (op (var 1) (var 2)) (var 0)) (var 3))) , (var 3)) → ⊥
  cut4615  adequate = bad4615  (Adequate.valid adequate Two boolean env18)
  bad4616 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop (bop b0 b0) b0) b0)) b1 → ⊥
  bad4616  p = false≢true (cong lower p)
  cut4616 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (op (var 1) (var 2)) (var 0)) (var 3))) , (var 4)) → ⊥
  cut4616  adequate = bad4616  (Adequate.valid adequate Two boolean env8)
  holds4617 : (z0 z1 z2 : A2) → (mul2 (mul2 z0 z1) (mul2 (mul2 (mul2 z1 z2) z1) z0)) ≡ z0
  holds4617 z0 z1 z2 = refl
  cut4617 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (op (var 1) (var 2)) (var 1)) (var 0))) , (var 0)) → ⊥
  cut4617  = reject2 ((op (op (var 0) (var 1)) (op (op (op (var 1) (var 2)) (var 1)) (var 0))) , (var 0)) (λ env → holds4617 (env 0) (env 1) (env 2))
  bad4618 : PathP (λ _ → Two) (bop (bop b0 b1) (bop (bop (bop b1 b0) b1) b0)) b1 → ⊥
  bad4618  p = false≢true (cong lower p)
  cut4618 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (op (var 1) (var 2)) (var 1)) (var 0))) , (var 1)) → ⊥
  cut4618  adequate = bad4618  (Adequate.valid adequate Two boolean env6)
  bad4619 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop (bop b0 b1) b0) b0)) b1 → ⊥
  bad4619  p = false≢true (cong lower p)
  cut4619 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (op (var 1) (var 2)) (var 1)) (var 0))) , (var 2)) → ⊥
  cut4619  adequate = bad4619  (Adequate.valid adequate Two boolean env2)
  bad4620 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop (bop b0 b0) b0) b0)) b1 → ⊥
  bad4620  p = false≢true (cong lower p)
  cut4620 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (op (var 1) (var 2)) (var 1)) (var 0))) , (var 3)) → ⊥
  cut4620  adequate = bad4620  (Adequate.valid adequate Two boolean env4)
  bad4621 : PathP (λ _ → Two) (bop (bop b0 b1) (bop (bop (bop b1 b1) b1) b1)) b0 → ⊥
  bad4621  p = false≢true (sym (cong lower p))
  cut4621 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (op (var 1) (var 2)) (var 1)) (var 1))) , (var 0)) → ⊥
  cut4621  adequate = bad4621  (Adequate.valid adequate Two boolean env3)
  bad4622 : PathP (λ _ → Two) (bop (bop b0 b1) (bop (bop (bop b1 b0) b1) b1)) b1 → ⊥
  bad4622  p = false≢true (cong lower p)
  cut4622 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (op (var 1) (var 2)) (var 1)) (var 1))) , (var 1)) → ⊥
  cut4622  adequate = bad4622  (Adequate.valid adequate Two boolean env6)
  bad4623 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop (bop b0 b1) b0) b0)) b1 → ⊥
  bad4623  p = false≢true (cong lower p)
  cut4623 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (op (var 1) (var 2)) (var 1)) (var 1))) , (var 2)) → ⊥
  cut4623  adequate = bad4623  (Adequate.valid adequate Two boolean env2)
  bad4624 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop (bop b0 b0) b0) b0)) b1 → ⊥
  bad4624  p = false≢true (cong lower p)
  cut4624 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (op (var 1) (var 2)) (var 1)) (var 1))) , (var 3)) → ⊥
  cut4624  adequate = bad4624  (Adequate.valid adequate Two boolean env4)
  bad4625 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop (bop b0 b1) b0) b1)) b0 → ⊥
  bad4625  p = false≢true (sym (cong lower p))
  cut4625 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (op (var 1) (var 2)) (var 1)) (var 2))) , (var 0)) → ⊥
  cut4625  adequate = bad4625  (Adequate.valid adequate Two boolean env2)
  bad4626 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop (bop b0 b1) b0) b1)) b0 → ⊥
  bad4626  p = false≢true (sym (cong lower p))
  cut4626 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (op (var 1) (var 2)) (var 1)) (var 2))) , (var 1)) → ⊥
  cut4626  adequate = bad4626  (Adequate.valid adequate Two boolean env2)
  bad4627 : PathP (λ _ → Two) (bop (bop b1 b1) (bop (bop (bop b1 b0) b1) b0)) b0 → ⊥
  bad4627  p = false≢true (sym (cong lower p))
  cut4627 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (op (var 1) (var 2)) (var 1)) (var 2))) , (var 2)) → ⊥
  cut4627  adequate = bad4627  (Adequate.valid adequate Two boolean env16)
  bad4628 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop (bop b0 b0) b0) b0)) b1 → ⊥
  bad4628  p = false≢true (cong lower p)
  cut4628 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (op (var 1) (var 2)) (var 1)) (var 2))) , (var 3)) → ⊥
  cut4628  adequate = bad4628  (Adequate.valid adequate Two boolean env4)
  bad4629 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop (bop b0 b0) b0) b1)) b0 → ⊥
  bad4629  p = false≢true (sym (cong lower p))
  cut4629 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (op (var 1) (var 2)) (var 1)) (var 3))) , (var 0)) → ⊥
  cut4629  adequate = bad4629  (Adequate.valid adequate Two boolean env4)
  bad4630 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop (bop b0 b0) b0) b1)) b0 → ⊥
  bad4630  p = false≢true (sym (cong lower p))
  cut4630 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (op (var 1) (var 2)) (var 1)) (var 3))) , (var 1)) → ⊥
  cut4630  adequate = bad4630  (Adequate.valid adequate Two boolean env4)
  bad4631 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop (bop b0 b0) b0) b1)) b0 → ⊥
  bad4631  p = false≢true (sym (cong lower p))
  cut4631 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (op (var 1) (var 2)) (var 1)) (var 3))) , (var 2)) → ⊥
  cut4631  adequate = bad4631  (Adequate.valid adequate Two boolean env4)
  bad4632 : PathP (λ _ → Two) (bop (bop b0 b1) (bop (bop (bop b1 b0) b1) b1)) b1 → ⊥
  bad4632  p = false≢true (cong lower p)
  cut4632 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (op (var 1) (var 2)) (var 1)) (var 3))) , (var 3)) → ⊥
  cut4632  adequate = bad4632  (Adequate.valid adequate Two boolean env10)
  bad4633 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop (bop b0 b0) b0) b0)) b1 → ⊥
  bad4633  p = false≢true (cong lower p)
  cut4633 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (op (var 1) (var 2)) (var 1)) (var 3))) , (var 4)) → ⊥
  cut4633  adequate = bad4633  (Adequate.valid adequate Two boolean env8)
  bad4634 : PathP (λ _ → Two) (bop (bop b1 b0) (bop (bop (bop b0 b1) b1) b1)) b1 → ⊥
  bad4634  p = false≢true (cong lower p)
  cut4634 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (op (var 1) (var 2)) (var 2)) (var 0))) , (var 0)) → ⊥
  cut4634  adequate = bad4634  (Adequate.valid adequate Two boolean env17)
  bad4635 : PathP (λ _ → Two) (bop (bop b0 b1) (bop (bop (bop b1 b0) b0) b0)) b1 → ⊥
  bad4635  p = false≢true (cong lower p)
  cut4635 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (op (var 1) (var 2)) (var 2)) (var 0))) , (var 1)) → ⊥
  cut4635  adequate = bad4635  (Adequate.valid adequate Two boolean env6)
  bad4636 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop (bop b0 b1) b1) b0)) b1 → ⊥
  bad4636  p = false≢true (cong lower p)
  cut4636 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (op (var 1) (var 2)) (var 2)) (var 0))) , (var 2)) → ⊥
  cut4636  adequate = bad4636  (Adequate.valid adequate Two boolean env2)
  bad4637 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop (bop b0 b0) b0) b0)) b1 → ⊥
  bad4637  p = false≢true (cong lower p)
  cut4637 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (op (var 1) (var 2)) (var 2)) (var 0))) , (var 3)) → ⊥
  cut4637  adequate = bad4637  (Adequate.valid adequate Two boolean env4)
  bad4638 : PathP (λ _ → Two) (bop (bop b0 b1) (bop (bop (bop b1 b0) b0) b1)) b0 → ⊥
  bad4638  p = false≢true (sym (cong lower p))
  cut4638 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (op (var 1) (var 2)) (var 2)) (var 1))) , (var 0)) → ⊥
  cut4638  adequate = bad4638  (Adequate.valid adequate Two boolean env6)
  holds4639 : (z0 z1 z2 : A3) → (mul3 (mul3 z0 z1) (mul3 (mul3 (mul3 z1 z2) z2) z1)) ≡ z1
  holds4639 z0 z1 z2 = refl
  cut4639 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (op (var 1) (var 2)) (var 2)) (var 1))) , (var 1)) → ⊥
  cut4639  = reject3 ((op (op (var 0) (var 1)) (op (op (op (var 1) (var 2)) (var 2)) (var 1))) , (var 1)) (λ env → holds4639 (env 0) (env 1) (env 2))
  bad4640 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop (bop b0 b1) b1) b0)) b1 → ⊥
  bad4640  p = false≢true (cong lower p)
  cut4640 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (op (var 1) (var 2)) (var 2)) (var 1))) , (var 2)) → ⊥
  cut4640  adequate = bad4640  (Adequate.valid adequate Two boolean env2)
  bad4641 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop (bop b0 b0) b0) b0)) b1 → ⊥
  bad4641  p = false≢true (cong lower p)
  cut4641 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (op (var 1) (var 2)) (var 2)) (var 1))) , (var 3)) → ⊥
  cut4641  adequate = bad4641  (Adequate.valid adequate Two boolean env4)
  bad4642 : PathP (λ _ → Two) (bop (bop b0 b1) (bop (bop (bop b1 b1) b1) b1)) b0 → ⊥
  bad4642  p = false≢true (sym (cong lower p))
  cut4642 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (op (var 1) (var 2)) (var 2)) (var 2))) , (var 0)) → ⊥
  cut4642  adequate = bad4642  (Adequate.valid adequate Two boolean env3)
  bad4643 : PathP (λ _ → Two) (bop (bop b0 b1) (bop (bop (bop b1 b0) b0) b0)) b1 → ⊥
  bad4643  p = false≢true (cong lower p)
  cut4643 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (op (var 1) (var 2)) (var 2)) (var 2))) , (var 1)) → ⊥
  cut4643  adequate = bad4643  (Adequate.valid adequate Two boolean env6)
  bad4644 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop (bop b0 b1) b1) b1)) b1 → ⊥
  bad4644  p = false≢true (cong lower p)
  cut4644 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (op (var 1) (var 2)) (var 2)) (var 2))) , (var 2)) → ⊥
  cut4644  adequate = bad4644  (Adequate.valid adequate Two boolean env2)
  bad4645 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop (bop b0 b0) b0) b0)) b1 → ⊥
  bad4645  p = false≢true (cong lower p)
  cut4645 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (op (var 1) (var 2)) (var 2)) (var 2))) , (var 3)) → ⊥
  cut4645  adequate = bad4645  (Adequate.valid adequate Two boolean env4)
  bad4646 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop (bop b0 b0) b0) b1)) b0 → ⊥
  bad4646  p = false≢true (sym (cong lower p))
  cut4646 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (op (var 1) (var 2)) (var 2)) (var 3))) , (var 0)) → ⊥
  cut4646  adequate = bad4646  (Adequate.valid adequate Two boolean env4)
  bad4647 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop (bop b0 b0) b0) b1)) b0 → ⊥
  bad4647  p = false≢true (sym (cong lower p))
  cut4647 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (op (var 1) (var 2)) (var 2)) (var 3))) , (var 1)) → ⊥
  cut4647  adequate = bad4647  (Adequate.valid adequate Two boolean env4)
  bad4648 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop (bop b0 b0) b0) b1)) b0 → ⊥
  bad4648  p = false≢true (sym (cong lower p))
  cut4648 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (op (var 1) (var 2)) (var 2)) (var 3))) , (var 2)) → ⊥
  cut4648  adequate = bad4648  (Adequate.valid adequate Two boolean env4)
  bad4649 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop (bop b0 b1) b1) b1)) b1 → ⊥
  bad4649  p = false≢true (cong lower p)
  cut4649 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (op (var 1) (var 2)) (var 2)) (var 3))) , (var 3)) → ⊥
  cut4649  adequate = bad4649  (Adequate.valid adequate Two boolean env7)
  bad4650 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop (bop b0 b0) b0) b0)) b1 → ⊥
  bad4650  p = false≢true (cong lower p)
  cut4650 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (op (var 1) (var 2)) (var 2)) (var 3))) , (var 4)) → ⊥
  cut4650  adequate = bad4650  (Adequate.valid adequate Two boolean env8)
  bad4651 : PathP (λ _ → Two) (bop (bop b1 b0) (bop (bop (bop b0 b0) b1) b1)) b1 → ⊥
  bad4651  p = false≢true (cong lower p)
  cut4651 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (op (var 1) (var 2)) (var 3)) (var 0))) , (var 0)) → ⊥
  cut4651  adequate = bad4651  (Adequate.valid adequate Two boolean env18)
  bad4652 : PathP (λ _ → Two) (bop (bop b0 b1) (bop (bop (bop b1 b0) b0) b0)) b1 → ⊥
  bad4652  p = false≢true (cong lower p)
  cut4652 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (op (var 1) (var 2)) (var 3)) (var 0))) , (var 1)) → ⊥
  cut4652  adequate = bad4652  (Adequate.valid adequate Two boolean env11)
  bad4653 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop (bop b0 b1) b0) b0)) b1 → ⊥
  bad4653  p = false≢true (cong lower p)
  cut4653 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (op (var 1) (var 2)) (var 3)) (var 0))) , (var 2)) → ⊥
  cut4653  adequate = bad4653  (Adequate.valid adequate Two boolean env12)
  bad4654 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop (bop b0 b0) b1) b0)) b1 → ⊥
  bad4654  p = false≢true (cong lower p)
  cut4654 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (op (var 1) (var 2)) (var 3)) (var 0))) , (var 3)) → ⊥
  cut4654  adequate = bad4654  (Adequate.valid adequate Two boolean env4)
  bad4655 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop (bop b0 b0) b0) b0)) b1 → ⊥
  bad4655  p = false≢true (cong lower p)
  cut4655 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (op (var 1) (var 2)) (var 3)) (var 0))) , (var 4)) → ⊥
  cut4655  adequate = bad4655  (Adequate.valid adequate Two boolean env8)
  bad4656 : PathP (λ _ → Two) (bop (bop b0 b1) (bop (bop (bop b1 b0) b0) b1)) b0 → ⊥
  bad4656  p = false≢true (sym (cong lower p))
  cut4656 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (op (var 1) (var 2)) (var 3)) (var 1))) , (var 0)) → ⊥
  cut4656  adequate = bad4656  (Adequate.valid adequate Two boolean env11)
  bad4657 : PathP (λ _ → Two) (bop (bop b0 b1) (bop (bop (bop b1 b0) b1) b1)) b1 → ⊥
  bad4657  p = false≢true (cong lower p)
  cut4657 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (op (var 1) (var 2)) (var 3)) (var 1))) , (var 1)) → ⊥
  cut4657  adequate = bad4657  (Adequate.valid adequate Two boolean env10)
  bad4658 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop (bop b0 b1) b0) b0)) b1 → ⊥
  bad4658  p = false≢true (cong lower p)
  cut4658 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (op (var 1) (var 2)) (var 3)) (var 1))) , (var 2)) → ⊥
  cut4658  adequate = bad4658  (Adequate.valid adequate Two boolean env12)
  bad4659 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop (bop b0 b0) b1) b0)) b1 → ⊥
  bad4659  p = false≢true (cong lower p)
  cut4659 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (op (var 1) (var 2)) (var 3)) (var 1))) , (var 3)) → ⊥
  cut4659  adequate = bad4659  (Adequate.valid adequate Two boolean env4)
  bad4660 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop (bop b0 b0) b0) b0)) b1 → ⊥
  bad4660  p = false≢true (cong lower p)
  cut4660 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (op (var 1) (var 2)) (var 3)) (var 1))) , (var 4)) → ⊥
  cut4660  adequate = bad4660  (Adequate.valid adequate Two boolean env8)
  bad4661 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop (bop b0 b1) b0) b1)) b0 → ⊥
  bad4661  p = false≢true (sym (cong lower p))
  cut4661 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (op (var 1) (var 2)) (var 3)) (var 2))) , (var 0)) → ⊥
  cut4661  adequate = bad4661  (Adequate.valid adequate Two boolean env12)
  bad4662 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop (bop b0 b1) b0) b1)) b0 → ⊥
  bad4662  p = false≢true (sym (cong lower p))
  cut4662 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (op (var 1) (var 2)) (var 3)) (var 2))) , (var 1)) → ⊥
  cut4662  adequate = bad4662  (Adequate.valid adequate Two boolean env12)
  bad4663 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop (bop b0 b1) b1) b1)) b1 → ⊥
  bad4663  p = false≢true (cong lower p)
  cut4663 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (op (var 1) (var 2)) (var 3)) (var 2))) , (var 2)) → ⊥
  cut4663  adequate = bad4663  (Adequate.valid adequate Two boolean env7)
  bad4664 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop (bop b0 b0) b1) b0)) b1 → ⊥
  bad4664  p = false≢true (cong lower p)
  cut4664 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (op (var 1) (var 2)) (var 3)) (var 2))) , (var 3)) → ⊥
  cut4664  adequate = bad4664  (Adequate.valid adequate Two boolean env4)
  bad4665 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop (bop b0 b0) b0) b0)) b1 → ⊥
  bad4665  p = false≢true (cong lower p)
  cut4665 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (op (var 1) (var 2)) (var 3)) (var 2))) , (var 4)) → ⊥
  cut4665  adequate = bad4665  (Adequate.valid adequate Two boolean env8)
  bad4666 : PathP (λ _ → Two) (bop (bop b0 b1) (bop (bop (bop b1 b1) b1) b1)) b0 → ⊥
  bad4666  p = false≢true (sym (cong lower p))
  cut4666 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (op (var 1) (var 2)) (var 3)) (var 3))) , (var 0)) → ⊥
  cut4666  adequate = bad4666  (Adequate.valid adequate Two boolean env13)
  bad4667 : PathP (λ _ → Two) (bop (bop b0 b1) (bop (bop (bop b1 b0) b0) b0)) b1 → ⊥
  bad4667  p = false≢true (cong lower p)
  cut4667 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (op (var 1) (var 2)) (var 3)) (var 3))) , (var 1)) → ⊥
  cut4667  adequate = bad4667  (Adequate.valid adequate Two boolean env11)
  bad4668 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop (bop b0 b1) b0) b0)) b1 → ⊥
  bad4668  p = false≢true (cong lower p)
  cut4668 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (op (var 1) (var 2)) (var 3)) (var 3))) , (var 2)) → ⊥
  cut4668  adequate = bad4668  (Adequate.valid adequate Two boolean env12)
  bad4669 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop (bop b0 b0) b1) b1)) b1 → ⊥
  bad4669  p = false≢true (cong lower p)
  cut4669 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (op (var 1) (var 2)) (var 3)) (var 3))) , (var 3)) → ⊥
  cut4669  adequate = bad4669  (Adequate.valid adequate Two boolean env4)
  bad4670 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop (bop b0 b0) b0) b0)) b1 → ⊥
  bad4670  p = false≢true (cong lower p)
  cut4670 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (op (var 1) (var 2)) (var 3)) (var 3))) , (var 4)) → ⊥
  cut4670  adequate = bad4670  (Adequate.valid adequate Two boolean env8)
  bad4671 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop (bop b0 b0) b0) b1)) b0 → ⊥
  bad4671  p = false≢true (sym (cong lower p))
  cut4671 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (op (var 1) (var 2)) (var 3)) (var 4))) , (var 0)) → ⊥
  cut4671  adequate = bad4671  (Adequate.valid adequate Two boolean env8)
  bad4672 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop (bop b0 b0) b0) b1)) b0 → ⊥
  bad4672  p = false≢true (sym (cong lower p))
  cut4672 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (op (var 1) (var 2)) (var 3)) (var 4))) , (var 1)) → ⊥
  cut4672  adequate = bad4672  (Adequate.valid adequate Two boolean env8)
  bad4673 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop (bop b0 b0) b0) b1)) b0 → ⊥
  bad4673  p = false≢true (sym (cong lower p))
  cut4673 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (op (var 1) (var 2)) (var 3)) (var 4))) , (var 2)) → ⊥
  cut4673  adequate = bad4673  (Adequate.valid adequate Two boolean env8)
  bad4674 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop (bop b0 b0) b0) b1)) b0 → ⊥
  bad4674  p = false≢true (sym (cong lower p))
  cut4674 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (op (var 1) (var 2)) (var 3)) (var 4))) , (var 3)) → ⊥
  cut4674  adequate = bad4674  (Adequate.valid adequate Two boolean env8)
  bad4675 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop (bop b0 b0) b1) b1)) b1 → ⊥
  bad4675  p = false≢true (cong lower p)
  cut4675 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (op (var 1) (var 2)) (var 3)) (var 4))) , (var 4)) → ⊥
  cut4675  adequate = bad4675  (Adequate.valid adequate Two boolean env14)
  bad4676 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop (bop b0 b0) b0) b0)) b1 → ⊥
  bad4676  p = false≢true (cong lower p)
  cut4676 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (op (var 1) (var 2)) (var 3)) (var 4))) , (var 5)) → ⊥
  cut4676  adequate = bad4676  (Adequate.valid adequate Two boolean env15)
  bad4677 : PathP (λ _ → Two) (bop (bop b1 b0) (bop (bop (bop b0 b1) b1) b1)) b1 → ⊥
  bad4677  p = false≢true (cong lower p)
  cut4677 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (op (var 2) (var 0)) (var 0)) (var 0))) , (var 0)) → ⊥
  cut4677  adequate = bad4677  (Adequate.valid adequate Two boolean env5)
  bad4678 : PathP (λ _ → Two) (bop (bop b0 b1) (bop (bop (bop b0 b0) b0) b0)) b1 → ⊥
  bad4678  p = false≢true (cong lower p)
  cut4678 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (op (var 2) (var 0)) (var 0)) (var 0))) , (var 1)) → ⊥
  cut4678  adequate = bad4678  (Adequate.valid adequate Two boolean env6)
  bad4679 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop (bop b1 b0) b0) b0)) b1 → ⊥
  bad4679  p = false≢true (cong lower p)
  cut4679 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (op (var 2) (var 0)) (var 0)) (var 0))) , (var 2)) → ⊥
  cut4679  adequate = bad4679  (Adequate.valid adequate Two boolean env2)
  bad4680 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop (bop b0 b0) b0) b0)) b1 → ⊥
  bad4680  p = false≢true (cong lower p)
  cut4680 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (op (var 2) (var 0)) (var 0)) (var 0))) , (var 3)) → ⊥
  cut4680  adequate = bad4680  (Adequate.valid adequate Two boolean env4)
  bad4681 : PathP (λ _ → Two) (bop (bop b0 b1) (bop (bop (bop b0 b0) b0) b1)) b0 → ⊥
  bad4681  p = false≢true (sym (cong lower p))
  cut4681 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (op (var 2) (var 0)) (var 0)) (var 1))) , (var 0)) → ⊥
  cut4681  adequate = bad4681  (Adequate.valid adequate Two boolean env6)
  holds4682 : (z0 z1 z2 : A3) → (mul3 (mul3 z0 z1) (mul3 (mul3 (mul3 z2 z0) z0) z1)) ≡ z1
  holds4682 z0 z1 z2 = refl
  cut4682 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (op (var 2) (var 0)) (var 0)) (var 1))) , (var 1)) → ⊥
  cut4682  = reject3 ((op (op (var 0) (var 1)) (op (op (op (var 2) (var 0)) (var 0)) (var 1))) , (var 1)) (λ env → holds4682 (env 0) (env 1) (env 2))
  bad4683 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop (bop b1 b0) b0) b0)) b1 → ⊥
  bad4683  p = false≢true (cong lower p)
  cut4683 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (op (var 2) (var 0)) (var 0)) (var 1))) , (var 2)) → ⊥
  cut4683  adequate = bad4683  (Adequate.valid adequate Two boolean env2)
  bad4684 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop (bop b0 b0) b0) b0)) b1 → ⊥
  bad4684  p = false≢true (cong lower p)
  cut4684 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (op (var 2) (var 0)) (var 0)) (var 1))) , (var 3)) → ⊥
  cut4684  adequate = bad4684  (Adequate.valid adequate Two boolean env4)
  bad4685 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop (bop b1 b0) b0) b1)) b0 → ⊥
  bad4685  p = false≢true (sym (cong lower p))
  cut4685 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (op (var 2) (var 0)) (var 0)) (var 2))) , (var 0)) → ⊥
  cut4685  adequate = bad4685  (Adequate.valid adequate Two boolean env2)
  bad4686 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop (bop b1 b0) b0) b1)) b0 → ⊥
  bad4686  p = false≢true (sym (cong lower p))
  cut4686 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (op (var 2) (var 0)) (var 0)) (var 2))) , (var 1)) → ⊥
  cut4686  adequate = bad4686  (Adequate.valid adequate Two boolean env2)
  bad4687 : PathP (λ _ → Two) (bop (bop b1 b1) (bop (bop (bop b0 b1) b1) b0)) b0 → ⊥
  bad4687  p = false≢true (sym (cong lower p))
  cut4687 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (op (var 2) (var 0)) (var 0)) (var 2))) , (var 2)) → ⊥
  cut4687  adequate = bad4687  (Adequate.valid adequate Two boolean env16)
  bad4688 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop (bop b0 b0) b0) b0)) b1 → ⊥
  bad4688  p = false≢true (cong lower p)
  cut4688 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (op (var 2) (var 0)) (var 0)) (var 2))) , (var 3)) → ⊥
  cut4688  adequate = bad4688  (Adequate.valid adequate Two boolean env4)
  bad4689 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop (bop b0 b0) b0) b1)) b0 → ⊥
  bad4689  p = false≢true (sym (cong lower p))
  cut4689 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (op (var 2) (var 0)) (var 0)) (var 3))) , (var 0)) → ⊥
  cut4689  adequate = bad4689  (Adequate.valid adequate Two boolean env4)
  bad4690 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop (bop b0 b0) b0) b1)) b0 → ⊥
  bad4690  p = false≢true (sym (cong lower p))
  cut4690 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (op (var 2) (var 0)) (var 0)) (var 3))) , (var 1)) → ⊥
  cut4690  adequate = bad4690  (Adequate.valid adequate Two boolean env4)
  bad4691 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop (bop b0 b0) b0) b1)) b0 → ⊥
  bad4691  p = false≢true (sym (cong lower p))
  cut4691 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (op (var 2) (var 0)) (var 0)) (var 3))) , (var 2)) → ⊥
  cut4691  adequate = bad4691  (Adequate.valid adequate Two boolean env4)
  bad4692 : PathP (λ _ → Two) (bop (bop b1 b0) (bop (bop (bop b0 b1) b1) b1)) b1 → ⊥
  bad4692  p = false≢true (cong lower p)
  cut4692 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (op (var 2) (var 0)) (var 0)) (var 3))) , (var 3)) → ⊥
  cut4692  adequate = bad4692  (Adequate.valid adequate Two boolean env18)
  bad4693 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop (bop b0 b0) b0) b0)) b1 → ⊥
  bad4693  p = false≢true (cong lower p)
  cut4693 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (op (var 2) (var 0)) (var 0)) (var 3))) , (var 4)) → ⊥
  cut4693  adequate = bad4693  (Adequate.valid adequate Two boolean env8)
  holds4694 : (z0 z1 z2 : A2) → (mul2 (mul2 z0 z1) (mul2 (mul2 (mul2 z2 z0) z1) z0)) ≡ z0
  holds4694 z0 z1 z2 = refl
  cut4694 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (op (var 2) (var 0)) (var 1)) (var 0))) , (var 0)) → ⊥
  cut4694  = reject2 ((op (op (var 0) (var 1)) (op (op (op (var 2) (var 0)) (var 1)) (var 0))) , (var 0)) (λ env → holds4694 (env 0) (env 1) (env 2))
  bad4695 : PathP (λ _ → Two) (bop (bop b0 b1) (bop (bop (bop b0 b0) b1) b0)) b1 → ⊥
  bad4695  p = false≢true (cong lower p)
  cut4695 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (op (var 2) (var 0)) (var 1)) (var 0))) , (var 1)) → ⊥
  cut4695  adequate = bad4695  (Adequate.valid adequate Two boolean env6)
  bad4696 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop (bop b1 b0) b0) b0)) b1 → ⊥
  bad4696  p = false≢true (cong lower p)
  cut4696 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (op (var 2) (var 0)) (var 1)) (var 0))) , (var 2)) → ⊥
  cut4696  adequate = bad4696  (Adequate.valid adequate Two boolean env2)
  bad4697 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop (bop b0 b0) b0) b0)) b1 → ⊥
  bad4697  p = false≢true (cong lower p)
  cut4697 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (op (var 2) (var 0)) (var 1)) (var 0))) , (var 3)) → ⊥
  cut4697  adequate = bad4697  (Adequate.valid adequate Two boolean env4)
  bad4698 : PathP (λ _ → Two) (bop (bop b1 b0) (bop (bop (bop b0 b1) b0) b0)) b1 → ⊥
  bad4698  p = false≢true (cong lower p)
  cut4698 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (op (var 2) (var 0)) (var 1)) (var 1))) , (var 0)) → ⊥
  cut4698  adequate = bad4698  (Adequate.valid adequate Two boolean env5)
  bad4699 : PathP (λ _ → Two) (bop (bop b0 b1) (bop (bop (bop b0 b0) b1) b1)) b1 → ⊥
  bad4699  p = false≢true (cong lower p)
  cut4699 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (op (var 2) (var 0)) (var 1)) (var 1))) , (var 1)) → ⊥
  cut4699  adequate = bad4699  (Adequate.valid adequate Two boolean env6)
  bad4700 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop (bop b1 b0) b0) b0)) b1 → ⊥
  bad4700  p = false≢true (cong lower p)
  cut4700 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (op (var 2) (var 0)) (var 1)) (var 1))) , (var 2)) → ⊥
  cut4700  adequate = bad4700  (Adequate.valid adequate Two boolean env2)
  bad4701 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop (bop b0 b0) b0) b0)) b1 → ⊥
  bad4701  p = false≢true (cong lower p)
  cut4701 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (op (var 2) (var 0)) (var 1)) (var 1))) , (var 3)) → ⊥
  cut4701  adequate = bad4701  (Adequate.valid adequate Two boolean env4)
  bad4702 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop (bop b1 b0) b0) b1)) b0 → ⊥
  bad4702  p = false≢true (sym (cong lower p))
  cut4702 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (op (var 2) (var 0)) (var 1)) (var 2))) , (var 0)) → ⊥
  cut4702  adequate = bad4702  (Adequate.valid adequate Two boolean env2)
  bad4703 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop (bop b1 b0) b0) b1)) b0 → ⊥
  bad4703  p = false≢true (sym (cong lower p))
  cut4703 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (op (var 2) (var 0)) (var 1)) (var 2))) , (var 1)) → ⊥
  cut4703  adequate = bad4703  (Adequate.valid adequate Two boolean env2)
  bad4704 : PathP (λ _ → Two) (bop (bop b0 b1) (bop (bop (bop b1 b0) b1) b1)) b1 → ⊥
  bad4704  p = false≢true (cong lower p)
  cut4704 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (op (var 2) (var 0)) (var 1)) (var 2))) , (var 2)) → ⊥
  cut4704  adequate = bad4704  (Adequate.valid adequate Two boolean env3)
  bad4705 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop (bop b0 b0) b0) b0)) b1 → ⊥
  bad4705  p = false≢true (cong lower p)
  cut4705 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (op (var 2) (var 0)) (var 1)) (var 2))) , (var 3)) → ⊥
  cut4705  adequate = bad4705  (Adequate.valid adequate Two boolean env4)
  bad4706 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop (bop b0 b0) b0) b1)) b0 → ⊥
  bad4706  p = false≢true (sym (cong lower p))
  cut4706 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (op (var 2) (var 0)) (var 1)) (var 3))) , (var 0)) → ⊥
  cut4706  adequate = bad4706  (Adequate.valid adequate Two boolean env4)
  bad4707 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop (bop b0 b0) b0) b1)) b0 → ⊥
  bad4707  p = false≢true (sym (cong lower p))
  cut4707 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (op (var 2) (var 0)) (var 1)) (var 3))) , (var 1)) → ⊥
  cut4707  adequate = bad4707  (Adequate.valid adequate Two boolean env4)
  bad4708 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop (bop b0 b0) b0) b1)) b0 → ⊥
  bad4708  p = false≢true (sym (cong lower p))
  cut4708 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (op (var 2) (var 0)) (var 1)) (var 3))) , (var 2)) → ⊥
  cut4708  adequate = bad4708  (Adequate.valid adequate Two boolean env4)
  bad4709 : PathP (λ _ → Two) (bop (bop b0 b1) (bop (bop (bop b0 b0) b1) b1)) b1 → ⊥
  bad4709  p = false≢true (cong lower p)
  cut4709 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (op (var 2) (var 0)) (var 1)) (var 3))) , (var 3)) → ⊥
  cut4709  adequate = bad4709  (Adequate.valid adequate Two boolean env10)
  bad4710 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop (bop b0 b0) b0) b0)) b1 → ⊥
  bad4710  p = false≢true (cong lower p)
  cut4710 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (op (var 2) (var 0)) (var 1)) (var 3))) , (var 4)) → ⊥
  cut4710  adequate = bad4710  (Adequate.valid adequate Two boolean env8)
  holds4711 : (z0 z1 z2 : A2) → (mul2 (mul2 z0 z1) (mul2 (mul2 (mul2 z2 z0) z2) z0)) ≡ z0
  holds4711 z0 z1 z2 = refl
  cut4711 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (op (var 2) (var 0)) (var 2)) (var 0))) , (var 0)) → ⊥
  cut4711  = reject2 ((op (op (var 0) (var 1)) (op (op (op (var 2) (var 0)) (var 2)) (var 0))) , (var 0)) (λ env → holds4711 (env 0) (env 1) (env 2))
  bad4712 : PathP (λ _ → Two) (bop (bop b0 b1) (bop (bop (bop b0 b0) b0) b0)) b1 → ⊥
  bad4712  p = false≢true (cong lower p)
  cut4712 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (op (var 2) (var 0)) (var 2)) (var 0))) , (var 1)) → ⊥
  cut4712  adequate = bad4712  (Adequate.valid adequate Two boolean env6)
  bad4713 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop (bop b1 b0) b1) b0)) b1 → ⊥
  bad4713  p = false≢true (cong lower p)
  cut4713 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (op (var 2) (var 0)) (var 2)) (var 0))) , (var 2)) → ⊥
  cut4713  adequate = bad4713  (Adequate.valid adequate Two boolean env2)
  bad4714 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop (bop b0 b0) b0) b0)) b1 → ⊥
  bad4714  p = false≢true (cong lower p)
  cut4714 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (op (var 2) (var 0)) (var 2)) (var 0))) , (var 3)) → ⊥
  cut4714  adequate = bad4714  (Adequate.valid adequate Two boolean env4)
  bad4715 : PathP (λ _ → Two) (bop (bop b0 b1) (bop (bop (bop b0 b0) b0) b1)) b0 → ⊥
  bad4715  p = false≢true (sym (cong lower p))
  cut4715 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (op (var 2) (var 0)) (var 2)) (var 1))) , (var 0)) → ⊥
  cut4715  adequate = bad4715  (Adequate.valid adequate Two boolean env6)
  bad4716 : PathP (λ _ → Two) (bop (bop b0 b1) (bop (bop (bop b1 b0) b1) b1)) b1 → ⊥
  bad4716  p = false≢true (cong lower p)
  cut4716 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (op (var 2) (var 0)) (var 2)) (var 1))) , (var 1)) → ⊥
  cut4716  adequate = bad4716  (Adequate.valid adequate Two boolean env3)
  bad4717 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop (bop b1 b0) b1) b0)) b1 → ⊥
  bad4717  p = false≢true (cong lower p)
  cut4717 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (op (var 2) (var 0)) (var 2)) (var 1))) , (var 2)) → ⊥
  cut4717  adequate = bad4717  (Adequate.valid adequate Two boolean env2)
  bad4718 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop (bop b0 b0) b0) b0)) b1 → ⊥
  bad4718  p = false≢true (cong lower p)
  cut4718 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (op (var 2) (var 0)) (var 2)) (var 1))) , (var 3)) → ⊥
  cut4718  adequate = bad4718  (Adequate.valid adequate Two boolean env4)
  bad4719 : PathP (λ _ → Two) (bop (bop b1 b0) (bop (bop (bop b0 b1) b0) b0)) b1 → ⊥
  bad4719  p = false≢true (cong lower p)
  cut4719 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (op (var 2) (var 0)) (var 2)) (var 2))) , (var 0)) → ⊥
  cut4719  adequate = bad4719  (Adequate.valid adequate Two boolean env5)
  bad4720 : PathP (λ _ → Two) (bop (bop b0 b1) (bop (bop (bop b0 b0) b0) b0)) b1 → ⊥
  bad4720  p = false≢true (cong lower p)
  cut4720 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (op (var 2) (var 0)) (var 2)) (var 2))) , (var 1)) → ⊥
  cut4720  adequate = bad4720  (Adequate.valid adequate Two boolean env6)
  bad4721 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop (bop b1 b0) b1) b1)) b1 → ⊥
  bad4721  p = false≢true (cong lower p)
  cut4721 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (op (var 2) (var 0)) (var 2)) (var 2))) , (var 2)) → ⊥
  cut4721  adequate = bad4721  (Adequate.valid adequate Two boolean env2)
  bad4722 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop (bop b0 b0) b0) b0)) b1 → ⊥
  bad4722  p = false≢true (cong lower p)
  cut4722 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (op (var 2) (var 0)) (var 2)) (var 2))) , (var 3)) → ⊥
  cut4722  adequate = bad4722  (Adequate.valid adequate Two boolean env4)
  bad4723 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop (bop b0 b0) b0) b1)) b0 → ⊥
  bad4723  p = false≢true (sym (cong lower p))
  cut4723 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (op (var 2) (var 0)) (var 2)) (var 3))) , (var 0)) → ⊥
  cut4723  adequate = bad4723  (Adequate.valid adequate Two boolean env4)
  bad4724 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop (bop b0 b0) b0) b1)) b0 → ⊥
  bad4724  p = false≢true (sym (cong lower p))
  cut4724 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (op (var 2) (var 0)) (var 2)) (var 3))) , (var 1)) → ⊥
  cut4724  adequate = bad4724  (Adequate.valid adequate Two boolean env4)
  bad4725 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop (bop b0 b0) b0) b1)) b0 → ⊥
  bad4725  p = false≢true (sym (cong lower p))
  cut4725 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (op (var 2) (var 0)) (var 2)) (var 3))) , (var 2)) → ⊥
  cut4725  adequate = bad4725  (Adequate.valid adequate Two boolean env4)
  bad4726 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop (bop b1 b0) b1) b1)) b1 → ⊥
  bad4726  p = false≢true (cong lower p)
  cut4726 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (op (var 2) (var 0)) (var 2)) (var 3))) , (var 3)) → ⊥
  cut4726  adequate = bad4726  (Adequate.valid adequate Two boolean env7)
  bad4727 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop (bop b0 b0) b0) b0)) b1 → ⊥
  bad4727  p = false≢true (cong lower p)
  cut4727 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (op (var 2) (var 0)) (var 2)) (var 3))) , (var 4)) → ⊥
  cut4727  adequate = bad4727  (Adequate.valid adequate Two boolean env8)
  bad4728 : PathP (λ _ → Two) (bop (bop b1 b0) (bop (bop (bop b0 b1) b1) b1)) b1 → ⊥
  bad4728  p = false≢true (cong lower p)
  cut4728 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (op (var 2) (var 0)) (var 3)) (var 0))) , (var 0)) → ⊥
  cut4728  adequate = bad4728  (Adequate.valid adequate Two boolean env18)
  bad4729 : PathP (λ _ → Two) (bop (bop b0 b1) (bop (bop (bop b0 b0) b0) b0)) b1 → ⊥
  bad4729  p = false≢true (cong lower p)
  cut4729 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (op (var 2) (var 0)) (var 3)) (var 0))) , (var 1)) → ⊥
  cut4729  adequate = bad4729  (Adequate.valid adequate Two boolean env11)
  bad4730 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop (bop b1 b0) b0) b0)) b1 → ⊥
  bad4730  p = false≢true (cong lower p)
  cut4730 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (op (var 2) (var 0)) (var 3)) (var 0))) , (var 2)) → ⊥
  cut4730  adequate = bad4730  (Adequate.valid adequate Two boolean env12)
  bad4731 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop (bop b0 b0) b1) b0)) b1 → ⊥
  bad4731  p = false≢true (cong lower p)
  cut4731 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (op (var 2) (var 0)) (var 3)) (var 0))) , (var 3)) → ⊥
  cut4731  adequate = bad4731  (Adequate.valid adequate Two boolean env4)
  bad4732 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop (bop b0 b0) b0) b0)) b1 → ⊥
  bad4732  p = false≢true (cong lower p)
  cut4732 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (op (var 2) (var 0)) (var 3)) (var 0))) , (var 4)) → ⊥
  cut4732  adequate = bad4732  (Adequate.valid adequate Two boolean env8)
  bad4733 : PathP (λ _ → Two) (bop (bop b0 b1) (bop (bop (bop b0 b0) b0) b1)) b0 → ⊥
  bad4733  p = false≢true (sym (cong lower p))
  cut4733 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (op (var 2) (var 0)) (var 3)) (var 1))) , (var 0)) → ⊥
  cut4733  adequate = bad4733  (Adequate.valid adequate Two boolean env11)
  bad4734 : PathP (λ _ → Two) (bop (bop b0 b1) (bop (bop (bop b0 b0) b1) b1)) b1 → ⊥
  bad4734  p = false≢true (cong lower p)
  cut4734 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (op (var 2) (var 0)) (var 3)) (var 1))) , (var 1)) → ⊥
  cut4734  adequate = bad4734  (Adequate.valid adequate Two boolean env10)
  bad4735 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop (bop b1 b0) b0) b0)) b1 → ⊥
  bad4735  p = false≢true (cong lower p)
  cut4735 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (op (var 2) (var 0)) (var 3)) (var 1))) , (var 2)) → ⊥
  cut4735  adequate = bad4735  (Adequate.valid adequate Two boolean env12)
  bad4736 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop (bop b0 b0) b1) b0)) b1 → ⊥
  bad4736  p = false≢true (cong lower p)
  cut4736 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (op (var 2) (var 0)) (var 3)) (var 1))) , (var 3)) → ⊥
  cut4736  adequate = bad4736  (Adequate.valid adequate Two boolean env4)
  bad4737 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop (bop b0 b0) b0) b0)) b1 → ⊥
  bad4737  p = false≢true (cong lower p)
  cut4737 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (op (var 2) (var 0)) (var 3)) (var 1))) , (var 4)) → ⊥
  cut4737  adequate = bad4737  (Adequate.valid adequate Two boolean env8)
  bad4738 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop (bop b1 b0) b0) b1)) b0 → ⊥
  bad4738  p = false≢true (sym (cong lower p))
  cut4738 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (op (var 2) (var 0)) (var 3)) (var 2))) , (var 0)) → ⊥
  cut4738  adequate = bad4738  (Adequate.valid adequate Two boolean env12)
  bad4739 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop (bop b1 b0) b0) b1)) b0 → ⊥
  bad4739  p = false≢true (sym (cong lower p))
  cut4739 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (op (var 2) (var 0)) (var 3)) (var 2))) , (var 1)) → ⊥
  cut4739  adequate = bad4739  (Adequate.valid adequate Two boolean env12)
  bad4740 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop (bop b1 b0) b1) b1)) b1 → ⊥
  bad4740  p = false≢true (cong lower p)
  cut4740 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (op (var 2) (var 0)) (var 3)) (var 2))) , (var 2)) → ⊥
  cut4740  adequate = bad4740  (Adequate.valid adequate Two boolean env7)
  bad4741 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop (bop b0 b0) b1) b0)) b1 → ⊥
  bad4741  p = false≢true (cong lower p)
  cut4741 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (op (var 2) (var 0)) (var 3)) (var 2))) , (var 3)) → ⊥
  cut4741  adequate = bad4741  (Adequate.valid adequate Two boolean env4)
  bad4742 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop (bop b0 b0) b0) b0)) b1 → ⊥
  bad4742  p = false≢true (cong lower p)
  cut4742 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (op (var 2) (var 0)) (var 3)) (var 2))) , (var 4)) → ⊥
  cut4742  adequate = bad4742  (Adequate.valid adequate Two boolean env8)
  bad4743 : PathP (λ _ → Two) (bop (bop b1 b0) (bop (bop (bop b0 b1) b0) b0)) b1 → ⊥
  bad4743  p = false≢true (cong lower p)
  cut4743 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (op (var 2) (var 0)) (var 3)) (var 3))) , (var 0)) → ⊥
  cut4743  adequate = bad4743  (Adequate.valid adequate Two boolean env9)
  bad4744 : PathP (λ _ → Two) (bop (bop b0 b1) (bop (bop (bop b0 b0) b0) b0)) b1 → ⊥
  bad4744  p = false≢true (cong lower p)
  cut4744 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (op (var 2) (var 0)) (var 3)) (var 3))) , (var 1)) → ⊥
  cut4744  adequate = bad4744  (Adequate.valid adequate Two boolean env11)
  bad4745 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop (bop b1 b0) b0) b0)) b1 → ⊥
  bad4745  p = false≢true (cong lower p)
  cut4745 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (op (var 2) (var 0)) (var 3)) (var 3))) , (var 2)) → ⊥
  cut4745  adequate = bad4745  (Adequate.valid adequate Two boolean env12)
  bad4746 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop (bop b0 b0) b1) b1)) b1 → ⊥
  bad4746  p = false≢true (cong lower p)
  cut4746 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (op (var 2) (var 0)) (var 3)) (var 3))) , (var 3)) → ⊥
  cut4746  adequate = bad4746  (Adequate.valid adequate Two boolean env4)
  bad4747 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop (bop b0 b0) b0) b0)) b1 → ⊥
  bad4747  p = false≢true (cong lower p)
  cut4747 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (op (var 2) (var 0)) (var 3)) (var 3))) , (var 4)) → ⊥
  cut4747  adequate = bad4747  (Adequate.valid adequate Two boolean env8)
  bad4748 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop (bop b0 b0) b0) b1)) b0 → ⊥
  bad4748  p = false≢true (sym (cong lower p))
  cut4748 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (op (var 2) (var 0)) (var 3)) (var 4))) , (var 0)) → ⊥
  cut4748  adequate = bad4748  (Adequate.valid adequate Two boolean env8)
  bad4749 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop (bop b0 b0) b0) b1)) b0 → ⊥
  bad4749  p = false≢true (sym (cong lower p))
  cut4749 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (op (var 2) (var 0)) (var 3)) (var 4))) , (var 1)) → ⊥
  cut4749  adequate = bad4749  (Adequate.valid adequate Two boolean env8)
  bad4750 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop (bop b0 b0) b0) b1)) b0 → ⊥
  bad4750  p = false≢true (sym (cong lower p))
  cut4750 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (op (var 2) (var 0)) (var 3)) (var 4))) , (var 2)) → ⊥
  cut4750  adequate = bad4750  (Adequate.valid adequate Two boolean env8)
  bad4751 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop (bop b0 b0) b0) b1)) b0 → ⊥
  bad4751  p = false≢true (sym (cong lower p))
  cut4751 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (op (var 2) (var 0)) (var 3)) (var 4))) , (var 3)) → ⊥
  cut4751  adequate = bad4751  (Adequate.valid adequate Two boolean env8)
  bad4752 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop (bop b0 b0) b1) b1)) b1 → ⊥
  bad4752  p = false≢true (cong lower p)
  cut4752 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (op (var 2) (var 0)) (var 3)) (var 4))) , (var 4)) → ⊥
  cut4752  adequate = bad4752  (Adequate.valid adequate Two boolean env14)
  bad4753 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop (bop b0 b0) b0) b0)) b1 → ⊥
  bad4753  p = false≢true (cong lower p)
  cut4753 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (op (var 2) (var 0)) (var 3)) (var 4))) , (var 5)) → ⊥
  cut4753  adequate = bad4753  (Adequate.valid adequate Two boolean env15)
  bad4754 : PathP (λ _ → Two) (bop (bop b1 b0) (bop (bop (bop b0 b0) b1) b1)) b1 → ⊥
  bad4754  p = false≢true (cong lower p)
  cut4754 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (op (var 2) (var 1)) (var 0)) (var 0))) , (var 0)) → ⊥
  cut4754  adequate = bad4754  (Adequate.valid adequate Two boolean env5)
  bad4755 : PathP (λ _ → Two) (bop (bop b0 b1) (bop (bop (bop b0 b1) b0) b0)) b1 → ⊥
  bad4755  p = false≢true (cong lower p)
  cut4755 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (op (var 2) (var 1)) (var 0)) (var 0))) , (var 1)) → ⊥
  cut4755  adequate = bad4755  (Adequate.valid adequate Two boolean env6)
  bad4756 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop (bop b1 b0) b0) b0)) b1 → ⊥
  bad4756  p = false≢true (cong lower p)
  cut4756 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (op (var 2) (var 1)) (var 0)) (var 0))) , (var 2)) → ⊥
  cut4756  adequate = bad4756  (Adequate.valid adequate Two boolean env2)
  bad4757 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop (bop b0 b0) b0) b0)) b1 → ⊥
  bad4757  p = false≢true (cong lower p)
  cut4757 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (op (var 2) (var 1)) (var 0)) (var 0))) , (var 3)) → ⊥
  cut4757  adequate = bad4757  (Adequate.valid adequate Two boolean env4)
  bad4758 : PathP (λ _ → Two) (bop (bop b0 b1) (bop (bop (bop b0 b1) b0) b1)) b0 → ⊥
  bad4758  p = false≢true (sym (cong lower p))
  cut4758 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (op (var 2) (var 1)) (var 0)) (var 1))) , (var 0)) → ⊥
  cut4758  adequate = bad4758  (Adequate.valid adequate Two boolean env6)
  holds4759 : (z0 z1 z2 : A3) → (mul3 (mul3 z0 z1) (mul3 (mul3 (mul3 z2 z1) z0) z1)) ≡ z1
  holds4759 z0 z1 z2 = refl
  cut4759 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (op (var 2) (var 1)) (var 0)) (var 1))) , (var 1)) → ⊥
  cut4759  = reject3 ((op (op (var 0) (var 1)) (op (op (op (var 2) (var 1)) (var 0)) (var 1))) , (var 1)) (λ env → holds4759 (env 0) (env 1) (env 2))
  bad4760 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop (bop b1 b0) b0) b0)) b1 → ⊥
  bad4760  p = false≢true (cong lower p)
  cut4760 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (op (var 2) (var 1)) (var 0)) (var 1))) , (var 2)) → ⊥
  cut4760  adequate = bad4760  (Adequate.valid adequate Two boolean env2)
  bad4761 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop (bop b0 b0) b0) b0)) b1 → ⊥
  bad4761  p = false≢true (cong lower p)
  cut4761 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (op (var 2) (var 1)) (var 0)) (var 1))) , (var 3)) → ⊥
  cut4761  adequate = bad4761  (Adequate.valid adequate Two boolean env4)
  bad4762 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop (bop b1 b0) b0) b1)) b0 → ⊥
  bad4762  p = false≢true (sym (cong lower p))
  cut4762 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (op (var 2) (var 1)) (var 0)) (var 2))) , (var 0)) → ⊥
  cut4762  adequate = bad4762  (Adequate.valid adequate Two boolean env2)
  bad4763 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop (bop b1 b0) b0) b1)) b0 → ⊥
  bad4763  p = false≢true (sym (cong lower p))
  cut4763 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (op (var 2) (var 1)) (var 0)) (var 2))) , (var 1)) → ⊥
  cut4763  adequate = bad4763  (Adequate.valid adequate Two boolean env2)
  bad4764 : PathP (λ _ → Two) (bop (bop b1 b0) (bop (bop (bop b1 b0) b1) b1)) b1 → ⊥
  bad4764  p = false≢true (cong lower p)
  cut4764 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (op (var 2) (var 1)) (var 0)) (var 2))) , (var 2)) → ⊥
  cut4764  adequate = bad4764  (Adequate.valid adequate Two boolean env17)
  bad4765 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop (bop b0 b0) b0) b0)) b1 → ⊥
  bad4765  p = false≢true (cong lower p)
  cut4765 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (op (var 2) (var 1)) (var 0)) (var 2))) , (var 3)) → ⊥
  cut4765  adequate = bad4765  (Adequate.valid adequate Two boolean env4)
  bad4766 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop (bop b0 b0) b0) b1)) b0 → ⊥
  bad4766  p = false≢true (sym (cong lower p))
  cut4766 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (op (var 2) (var 1)) (var 0)) (var 3))) , (var 0)) → ⊥
  cut4766  adequate = bad4766  (Adequate.valid adequate Two boolean env4)
  bad4767 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop (bop b0 b0) b0) b1)) b0 → ⊥
  bad4767  p = false≢true (sym (cong lower p))
  cut4767 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (op (var 2) (var 1)) (var 0)) (var 3))) , (var 1)) → ⊥
  cut4767  adequate = bad4767  (Adequate.valid adequate Two boolean env4)
  bad4768 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop (bop b0 b0) b0) b1)) b0 → ⊥
  bad4768  p = false≢true (sym (cong lower p))
  cut4768 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (op (var 2) (var 1)) (var 0)) (var 3))) , (var 2)) → ⊥
  cut4768  adequate = bad4768  (Adequate.valid adequate Two boolean env4)
  bad4769 : PathP (λ _ → Two) (bop (bop b1 b0) (bop (bop (bop b0 b0) b1) b1)) b1 → ⊥
  bad4769  p = false≢true (cong lower p)
  cut4769 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (op (var 2) (var 1)) (var 0)) (var 3))) , (var 3)) → ⊥
  cut4769  adequate = bad4769  (Adequate.valid adequate Two boolean env18)
  bad4770 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop (bop b0 b0) b0) b0)) b1 → ⊥
  bad4770  p = false≢true (cong lower p)
  cut4770 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (op (var 2) (var 1)) (var 0)) (var 3))) , (var 4)) → ⊥
  cut4770  adequate = bad4770  (Adequate.valid adequate Two boolean env8)
  holds4771 : (z0 z1 z2 : A2) → (mul2 (mul2 z0 z1) (mul2 (mul2 (mul2 z2 z1) z1) z0)) ≡ z0
  holds4771 z0 z1 z2 = refl
  cut4771 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (op (var 2) (var 1)) (var 1)) (var 0))) , (var 0)) → ⊥
  cut4771  = reject2 ((op (op (var 0) (var 1)) (op (op (op (var 2) (var 1)) (var 1)) (var 0))) , (var 0)) (λ env → holds4771 (env 0) (env 1) (env 2))
  bad4772 : PathP (λ _ → Two) (bop (bop b0 b1) (bop (bop (bop b0 b1) b1) b0)) b1 → ⊥
  bad4772  p = false≢true (cong lower p)
  cut4772 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (op (var 2) (var 1)) (var 1)) (var 0))) , (var 1)) → ⊥
  cut4772  adequate = bad4772  (Adequate.valid adequate Two boolean env6)
  bad4773 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop (bop b1 b0) b0) b0)) b1 → ⊥
  bad4773  p = false≢true (cong lower p)
  cut4773 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (op (var 2) (var 1)) (var 1)) (var 0))) , (var 2)) → ⊥
  cut4773  adequate = bad4773  (Adequate.valid adequate Two boolean env2)
  bad4774 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop (bop b0 b0) b0) b0)) b1 → ⊥
  bad4774  p = false≢true (cong lower p)
  cut4774 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (op (var 2) (var 1)) (var 1)) (var 0))) , (var 3)) → ⊥
  cut4774  adequate = bad4774  (Adequate.valid adequate Two boolean env4)
  bad4775 : PathP (λ _ → Two) (bop (bop b0 b1) (bop (bop (bop b1 b1) b1) b1)) b0 → ⊥
  bad4775  p = false≢true (sym (cong lower p))
  cut4775 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (op (var 2) (var 1)) (var 1)) (var 1))) , (var 0)) → ⊥
  cut4775  adequate = bad4775  (Adequate.valid adequate Two boolean env3)
  bad4776 : PathP (λ _ → Two) (bop (bop b0 b1) (bop (bop (bop b0 b1) b1) b1)) b1 → ⊥
  bad4776  p = false≢true (cong lower p)
  cut4776 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (op (var 2) (var 1)) (var 1)) (var 1))) , (var 1)) → ⊥
  cut4776  adequate = bad4776  (Adequate.valid adequate Two boolean env6)
  bad4777 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop (bop b1 b0) b0) b0)) b1 → ⊥
  bad4777  p = false≢true (cong lower p)
  cut4777 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (op (var 2) (var 1)) (var 1)) (var 1))) , (var 2)) → ⊥
  cut4777  adequate = bad4777  (Adequate.valid adequate Two boolean env2)
  bad4778 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop (bop b0 b0) b0) b0)) b1 → ⊥
  bad4778  p = false≢true (cong lower p)
  cut4778 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (op (var 2) (var 1)) (var 1)) (var 1))) , (var 3)) → ⊥
  cut4778  adequate = bad4778  (Adequate.valid adequate Two boolean env4)
  bad4779 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop (bop b1 b0) b0) b1)) b0 → ⊥
  bad4779  p = false≢true (sym (cong lower p))
  cut4779 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (op (var 2) (var 1)) (var 1)) (var 2))) , (var 0)) → ⊥
  cut4779  adequate = bad4779  (Adequate.valid adequate Two boolean env2)
  bad4780 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop (bop b1 b0) b0) b1)) b0 → ⊥
  bad4780  p = false≢true (sym (cong lower p))
  cut4780 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (op (var 2) (var 1)) (var 1)) (var 2))) , (var 1)) → ⊥
  cut4780  adequate = bad4780  (Adequate.valid adequate Two boolean env2)
  bad4781 : PathP (λ _ → Two) (bop (bop b1 b1) (bop (bop (bop b0 b1) b1) b0)) b0 → ⊥
  bad4781  p = false≢true (sym (cong lower p))
  cut4781 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (op (var 2) (var 1)) (var 1)) (var 2))) , (var 2)) → ⊥
  cut4781  adequate = bad4781  (Adequate.valid adequate Two boolean env16)
  bad4782 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop (bop b0 b0) b0) b0)) b1 → ⊥
  bad4782  p = false≢true (cong lower p)
  cut4782 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (op (var 2) (var 1)) (var 1)) (var 2))) , (var 3)) → ⊥
  cut4782  adequate = bad4782  (Adequate.valid adequate Two boolean env4)
  bad4783 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop (bop b0 b0) b0) b1)) b0 → ⊥
  bad4783  p = false≢true (sym (cong lower p))
  cut4783 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (op (var 2) (var 1)) (var 1)) (var 3))) , (var 0)) → ⊥
  cut4783  adequate = bad4783  (Adequate.valid adequate Two boolean env4)
  bad4784 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop (bop b0 b0) b0) b1)) b0 → ⊥
  bad4784  p = false≢true (sym (cong lower p))
  cut4784 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (op (var 2) (var 1)) (var 1)) (var 3))) , (var 1)) → ⊥
  cut4784  adequate = bad4784  (Adequate.valid adequate Two boolean env4)
  bad4785 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop (bop b0 b0) b0) b1)) b0 → ⊥
  bad4785  p = false≢true (sym (cong lower p))
  cut4785 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (op (var 2) (var 1)) (var 1)) (var 3))) , (var 2)) → ⊥
  cut4785  adequate = bad4785  (Adequate.valid adequate Two boolean env4)
  bad4786 : PathP (λ _ → Two) (bop (bop b0 b1) (bop (bop (bop b0 b1) b1) b1)) b1 → ⊥
  bad4786  p = false≢true (cong lower p)
  cut4786 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (op (var 2) (var 1)) (var 1)) (var 3))) , (var 3)) → ⊥
  cut4786  adequate = bad4786  (Adequate.valid adequate Two boolean env10)
  bad4787 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop (bop b0 b0) b0) b0)) b1 → ⊥
  bad4787  p = false≢true (cong lower p)
  cut4787 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (op (var 2) (var 1)) (var 1)) (var 3))) , (var 4)) → ⊥
  cut4787  adequate = bad4787  (Adequate.valid adequate Two boolean env8)
  bad4788 : PathP (λ _ → Two) (bop (bop b1 b0) (bop (bop (bop b1 b0) b1) b1)) b1 → ⊥
  bad4788  p = false≢true (cong lower p)
  cut4788 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (op (var 2) (var 1)) (var 2)) (var 0))) , (var 0)) → ⊥
  cut4788  adequate = bad4788  (Adequate.valid adequate Two boolean env17)
  bad4789 : PathP (λ _ → Two) (bop (bop b0 b1) (bop (bop (bop b0 b1) b0) b0)) b1 → ⊥
  bad4789  p = false≢true (cong lower p)
  cut4789 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (op (var 2) (var 1)) (var 2)) (var 0))) , (var 1)) → ⊥
  cut4789  adequate = bad4789  (Adequate.valid adequate Two boolean env6)
  bad4790 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop (bop b1 b0) b1) b0)) b1 → ⊥
  bad4790  p = false≢true (cong lower p)
  cut4790 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (op (var 2) (var 1)) (var 2)) (var 0))) , (var 2)) → ⊥
  cut4790  adequate = bad4790  (Adequate.valid adequate Two boolean env2)
  bad4791 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop (bop b0 b0) b0) b0)) b1 → ⊥
  bad4791  p = false≢true (cong lower p)
  cut4791 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (op (var 2) (var 1)) (var 2)) (var 0))) , (var 3)) → ⊥
  cut4791  adequate = bad4791  (Adequate.valid adequate Two boolean env4)
  bad4792 : PathP (λ _ → Two) (bop (bop b0 b1) (bop (bop (bop b0 b1) b0) b1)) b0 → ⊥
  bad4792  p = false≢true (sym (cong lower p))
  cut4792 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (op (var 2) (var 1)) (var 2)) (var 1))) , (var 0)) → ⊥
  cut4792  adequate = bad4792  (Adequate.valid adequate Two boolean env6)
  holds4793 : (z0 z1 z2 : A3) → (mul3 (mul3 z0 z1) (mul3 (mul3 (mul3 z2 z1) z2) z1)) ≡ z1
  holds4793 z0 z1 z2 = refl
  cut4793 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (op (var 2) (var 1)) (var 2)) (var 1))) , (var 1)) → ⊥
  cut4793  = reject3 ((op (op (var 0) (var 1)) (op (op (op (var 2) (var 1)) (var 2)) (var 1))) , (var 1)) (λ env → holds4793 (env 0) (env 1) (env 2))
  bad4794 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop (bop b1 b0) b1) b0)) b1 → ⊥
  bad4794  p = false≢true (cong lower p)
  cut4794 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (op (var 2) (var 1)) (var 2)) (var 1))) , (var 2)) → ⊥
  cut4794  adequate = bad4794  (Adequate.valid adequate Two boolean env2)
  bad4795 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop (bop b0 b0) b0) b0)) b1 → ⊥
  bad4795  p = false≢true (cong lower p)
  cut4795 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (op (var 2) (var 1)) (var 2)) (var 1))) , (var 3)) → ⊥
  cut4795  adequate = bad4795  (Adequate.valid adequate Two boolean env4)
  bad4796 : PathP (λ _ → Two) (bop (bop b0 b1) (bop (bop (bop b1 b1) b1) b1)) b0 → ⊥
  bad4796  p = false≢true (sym (cong lower p))
  cut4796 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (op (var 2) (var 1)) (var 2)) (var 2))) , (var 0)) → ⊥
  cut4796  adequate = bad4796  (Adequate.valid adequate Two boolean env3)
  bad4797 : PathP (λ _ → Two) (bop (bop b0 b1) (bop (bop (bop b0 b1) b0) b0)) b1 → ⊥
  bad4797  p = false≢true (cong lower p)
  cut4797 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (op (var 2) (var 1)) (var 2)) (var 2))) , (var 1)) → ⊥
  cut4797  adequate = bad4797  (Adequate.valid adequate Two boolean env6)
  bad4798 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop (bop b1 b0) b1) b1)) b1 → ⊥
  bad4798  p = false≢true (cong lower p)
  cut4798 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (op (var 2) (var 1)) (var 2)) (var 2))) , (var 2)) → ⊥
  cut4798  adequate = bad4798  (Adequate.valid adequate Two boolean env2)
  bad4799 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop (bop b0 b0) b0) b0)) b1 → ⊥
  bad4799  p = false≢true (cong lower p)
  cut4799 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (op (var 2) (var 1)) (var 2)) (var 2))) , (var 3)) → ⊥
  cut4799  adequate = bad4799  (Adequate.valid adequate Two boolean env4)
  bad4800 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop (bop b0 b0) b0) b1)) b0 → ⊥
  bad4800  p = false≢true (sym (cong lower p))
  cut4800 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (op (var 2) (var 1)) (var 2)) (var 3))) , (var 0)) → ⊥
  cut4800  adequate = bad4800  (Adequate.valid adequate Two boolean env4)
  bad4801 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop (bop b0 b0) b0) b1)) b0 → ⊥
  bad4801  p = false≢true (sym (cong lower p))
  cut4801 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (op (var 2) (var 1)) (var 2)) (var 3))) , (var 1)) → ⊥
  cut4801  adequate = bad4801  (Adequate.valid adequate Two boolean env4)
  bad4802 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop (bop b0 b0) b0) b1)) b0 → ⊥
  bad4802  p = false≢true (sym (cong lower p))
  cut4802 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (op (var 2) (var 1)) (var 2)) (var 3))) , (var 2)) → ⊥
  cut4802  adequate = bad4802  (Adequate.valid adequate Two boolean env4)
  bad4803 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop (bop b1 b0) b1) b1)) b1 → ⊥
  bad4803  p = false≢true (cong lower p)
  cut4803 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (op (var 2) (var 1)) (var 2)) (var 3))) , (var 3)) → ⊥
  cut4803  adequate = bad4803  (Adequate.valid adequate Two boolean env7)
  bad4804 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop (bop b0 b0) b0) b0)) b1 → ⊥
  bad4804  p = false≢true (cong lower p)
  cut4804 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (op (var 2) (var 1)) (var 2)) (var 3))) , (var 4)) → ⊥
  cut4804  adequate = bad4804  (Adequate.valid adequate Two boolean env8)
  bad4805 : PathP (λ _ → Two) (bop (bop b1 b0) (bop (bop (bop b0 b0) b1) b1)) b1 → ⊥
  bad4805  p = false≢true (cong lower p)
  cut4805 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (op (var 2) (var 1)) (var 3)) (var 0))) , (var 0)) → ⊥
  cut4805  adequate = bad4805  (Adequate.valid adequate Two boolean env18)
  bad4806 : PathP (λ _ → Two) (bop (bop b0 b1) (bop (bop (bop b0 b1) b0) b0)) b1 → ⊥
  bad4806  p = false≢true (cong lower p)
  cut4806 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (op (var 2) (var 1)) (var 3)) (var 0))) , (var 1)) → ⊥
  cut4806  adequate = bad4806  (Adequate.valid adequate Two boolean env11)
  bad4807 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop (bop b1 b0) b0) b0)) b1 → ⊥
  bad4807  p = false≢true (cong lower p)
  cut4807 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (op (var 2) (var 1)) (var 3)) (var 0))) , (var 2)) → ⊥
  cut4807  adequate = bad4807  (Adequate.valid adequate Two boolean env12)
  bad4808 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop (bop b0 b0) b1) b0)) b1 → ⊥
  bad4808  p = false≢true (cong lower p)
  cut4808 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (op (var 2) (var 1)) (var 3)) (var 0))) , (var 3)) → ⊥
  cut4808  adequate = bad4808  (Adequate.valid adequate Two boolean env4)
  bad4809 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop (bop b0 b0) b0) b0)) b1 → ⊥
  bad4809  p = false≢true (cong lower p)
  cut4809 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (op (var 2) (var 1)) (var 3)) (var 0))) , (var 4)) → ⊥
  cut4809  adequate = bad4809  (Adequate.valid adequate Two boolean env8)
  bad4810 : PathP (λ _ → Two) (bop (bop b0 b1) (bop (bop (bop b0 b1) b0) b1)) b0 → ⊥
  bad4810  p = false≢true (sym (cong lower p))
  cut4810 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (op (var 2) (var 1)) (var 3)) (var 1))) , (var 0)) → ⊥
  cut4810  adequate = bad4810  (Adequate.valid adequate Two boolean env11)
  bad4811 : PathP (λ _ → Two) (bop (bop b0 b1) (bop (bop (bop b0 b1) b1) b1)) b1 → ⊥
  bad4811  p = false≢true (cong lower p)
  cut4811 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (op (var 2) (var 1)) (var 3)) (var 1))) , (var 1)) → ⊥
  cut4811  adequate = bad4811  (Adequate.valid adequate Two boolean env10)
  bad4812 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop (bop b1 b0) b0) b0)) b1 → ⊥
  bad4812  p = false≢true (cong lower p)
  cut4812 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (op (var 2) (var 1)) (var 3)) (var 1))) , (var 2)) → ⊥
  cut4812  adequate = bad4812  (Adequate.valid adequate Two boolean env12)
  bad4813 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop (bop b0 b0) b1) b0)) b1 → ⊥
  bad4813  p = false≢true (cong lower p)
  cut4813 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (op (var 2) (var 1)) (var 3)) (var 1))) , (var 3)) → ⊥
  cut4813  adequate = bad4813  (Adequate.valid adequate Two boolean env4)
  bad4814 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop (bop b0 b0) b0) b0)) b1 → ⊥
  bad4814  p = false≢true (cong lower p)
  cut4814 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (op (var 2) (var 1)) (var 3)) (var 1))) , (var 4)) → ⊥
  cut4814  adequate = bad4814  (Adequate.valid adequate Two boolean env8)
  bad4815 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop (bop b1 b0) b0) b1)) b0 → ⊥
  bad4815  p = false≢true (sym (cong lower p))
  cut4815 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (op (var 2) (var 1)) (var 3)) (var 2))) , (var 0)) → ⊥
  cut4815  adequate = bad4815  (Adequate.valid adequate Two boolean env12)
  bad4816 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop (bop b1 b0) b0) b1)) b0 → ⊥
  bad4816  p = false≢true (sym (cong lower p))
  cut4816 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (op (var 2) (var 1)) (var 3)) (var 2))) , (var 1)) → ⊥
  cut4816  adequate = bad4816  (Adequate.valid adequate Two boolean env12)
  bad4817 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop (bop b1 b0) b1) b1)) b1 → ⊥
  bad4817  p = false≢true (cong lower p)
  cut4817 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (op (var 2) (var 1)) (var 3)) (var 2))) , (var 2)) → ⊥
  cut4817  adequate = bad4817  (Adequate.valid adequate Two boolean env7)
  bad4818 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop (bop b0 b0) b1) b0)) b1 → ⊥
  bad4818  p = false≢true (cong lower p)
  cut4818 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (op (var 2) (var 1)) (var 3)) (var 2))) , (var 3)) → ⊥
  cut4818  adequate = bad4818  (Adequate.valid adequate Two boolean env4)
  bad4819 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop (bop b0 b0) b0) b0)) b1 → ⊥
  bad4819  p = false≢true (cong lower p)
  cut4819 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (op (var 2) (var 1)) (var 3)) (var 2))) , (var 4)) → ⊥
  cut4819  adequate = bad4819  (Adequate.valid adequate Two boolean env8)
  bad4820 : PathP (λ _ → Two) (bop (bop b0 b1) (bop (bop (bop b1 b1) b1) b1)) b0 → ⊥
  bad4820  p = false≢true (sym (cong lower p))
  cut4820 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (op (var 2) (var 1)) (var 3)) (var 3))) , (var 0)) → ⊥
  cut4820  adequate = bad4820  (Adequate.valid adequate Two boolean env13)
  bad4821 : PathP (λ _ → Two) (bop (bop b0 b1) (bop (bop (bop b0 b1) b0) b0)) b1 → ⊥
  bad4821  p = false≢true (cong lower p)
  cut4821 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (op (var 2) (var 1)) (var 3)) (var 3))) , (var 1)) → ⊥
  cut4821  adequate = bad4821  (Adequate.valid adequate Two boolean env11)
  bad4822 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop (bop b1 b0) b0) b0)) b1 → ⊥
  bad4822  p = false≢true (cong lower p)
  cut4822 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (op (var 2) (var 1)) (var 3)) (var 3))) , (var 2)) → ⊥
  cut4822  adequate = bad4822  (Adequate.valid adequate Two boolean env12)
  bad4823 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop (bop b0 b0) b1) b1)) b1 → ⊥
  bad4823  p = false≢true (cong lower p)
  cut4823 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (op (var 2) (var 1)) (var 3)) (var 3))) , (var 3)) → ⊥
  cut4823  adequate = bad4823  (Adequate.valid adequate Two boolean env4)
  bad4824 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop (bop b0 b0) b0) b0)) b1 → ⊥
  bad4824  p = false≢true (cong lower p)
  cut4824 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (op (var 2) (var 1)) (var 3)) (var 3))) , (var 4)) → ⊥
  cut4824  adequate = bad4824  (Adequate.valid adequate Two boolean env8)
  bad4825 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop (bop b0 b0) b0) b1)) b0 → ⊥
  bad4825  p = false≢true (sym (cong lower p))
  cut4825 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (op (var 2) (var 1)) (var 3)) (var 4))) , (var 0)) → ⊥
  cut4825  adequate = bad4825  (Adequate.valid adequate Two boolean env8)
  bad4826 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop (bop b0 b0) b0) b1)) b0 → ⊥
  bad4826  p = false≢true (sym (cong lower p))
  cut4826 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (op (var 2) (var 1)) (var 3)) (var 4))) , (var 1)) → ⊥
  cut4826  adequate = bad4826  (Adequate.valid adequate Two boolean env8)
  bad4827 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop (bop b0 b0) b0) b1)) b0 → ⊥
  bad4827  p = false≢true (sym (cong lower p))
  cut4827 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (op (var 2) (var 1)) (var 3)) (var 4))) , (var 2)) → ⊥
  cut4827  adequate = bad4827  (Adequate.valid adequate Two boolean env8)
  bad4828 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop (bop b0 b0) b0) b1)) b0 → ⊥
  bad4828  p = false≢true (sym (cong lower p))
  cut4828 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (op (var 2) (var 1)) (var 3)) (var 4))) , (var 3)) → ⊥
  cut4828  adequate = bad4828  (Adequate.valid adequate Two boolean env8)
  bad4829 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop (bop b0 b0) b1) b1)) b1 → ⊥
  bad4829  p = false≢true (cong lower p)
  cut4829 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (op (var 2) (var 1)) (var 3)) (var 4))) , (var 4)) → ⊥
  cut4829  adequate = bad4829  (Adequate.valid adequate Two boolean env14)
  bad4830 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop (bop b0 b0) b0) b0)) b1 → ⊥
  bad4830  p = false≢true (cong lower p)
  cut4830 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (op (var 2) (var 1)) (var 3)) (var 4))) , (var 5)) → ⊥
  cut4830  adequate = bad4830  (Adequate.valid adequate Two boolean env15)
  bad4831 : PathP (λ _ → Two) (bop (bop b1 b0) (bop (bop (bop b0 b0) b1) b1)) b1 → ⊥
  bad4831  p = false≢true (cong lower p)
  cut4831 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (op (var 2) (var 2)) (var 0)) (var 0))) , (var 0)) → ⊥
  cut4831  adequate = bad4831  (Adequate.valid adequate Two boolean env5)
  bad4832 : PathP (λ _ → Two) (bop (bop b0 b1) (bop (bop (bop b0 b0) b0) b0)) b1 → ⊥
  bad4832  p = false≢true (cong lower p)
  cut4832 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (op (var 2) (var 2)) (var 0)) (var 0))) , (var 1)) → ⊥
  cut4832  adequate = bad4832  (Adequate.valid adequate Two boolean env6)
  bad4833 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop (bop b1 b1) b0) b0)) b1 → ⊥
  bad4833  p = false≢true (cong lower p)
  cut4833 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (op (var 2) (var 2)) (var 0)) (var 0))) , (var 2)) → ⊥
  cut4833  adequate = bad4833  (Adequate.valid adequate Two boolean env2)
  bad4834 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop (bop b0 b0) b0) b0)) b1 → ⊥
  bad4834  p = false≢true (cong lower p)
  cut4834 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (op (var 2) (var 2)) (var 0)) (var 0))) , (var 3)) → ⊥
  cut4834  adequate = bad4834  (Adequate.valid adequate Two boolean env4)
  bad4835 : PathP (λ _ → Two) (bop (bop b0 b1) (bop (bop (bop b0 b0) b0) b1)) b0 → ⊥
  bad4835  p = false≢true (sym (cong lower p))
  cut4835 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (op (var 2) (var 2)) (var 0)) (var 1))) , (var 0)) → ⊥
  cut4835  adequate = bad4835  (Adequate.valid adequate Two boolean env6)
  holds4836 : (z0 z1 z2 : A3) → (mul3 (mul3 z0 z1) (mul3 (mul3 (mul3 z2 z2) z0) z1)) ≡ z1
  holds4836 z0 z1 z2 = refl
  cut4836 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (op (var 2) (var 2)) (var 0)) (var 1))) , (var 1)) → ⊥
  cut4836  = reject3 ((op (op (var 0) (var 1)) (op (op (op (var 2) (var 2)) (var 0)) (var 1))) , (var 1)) (λ env → holds4836 (env 0) (env 1) (env 2))
  bad4837 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop (bop b1 b1) b0) b0)) b1 → ⊥
  bad4837  p = false≢true (cong lower p)
  cut4837 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (op (var 2) (var 2)) (var 0)) (var 1))) , (var 2)) → ⊥
  cut4837  adequate = bad4837  (Adequate.valid adequate Two boolean env2)
  bad4838 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop (bop b0 b0) b0) b0)) b1 → ⊥
  bad4838  p = false≢true (cong lower p)
  cut4838 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (op (var 2) (var 2)) (var 0)) (var 1))) , (var 3)) → ⊥
  cut4838  adequate = bad4838  (Adequate.valid adequate Two boolean env4)
  bad4839 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop (bop b1 b1) b0) b1)) b0 → ⊥
  bad4839  p = false≢true (sym (cong lower p))
  cut4839 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (op (var 2) (var 2)) (var 0)) (var 2))) , (var 0)) → ⊥
  cut4839  adequate = bad4839  (Adequate.valid adequate Two boolean env2)
  bad4840 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop (bop b1 b1) b0) b1)) b0 → ⊥
  bad4840  p = false≢true (sym (cong lower p))
  cut4840 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (op (var 2) (var 2)) (var 0)) (var 2))) , (var 1)) → ⊥
  cut4840  adequate = bad4840  (Adequate.valid adequate Two boolean env2)
  bad4841 : PathP (λ _ → Two) (bop (bop b1 b1) (bop (bop (bop b0 b0) b1) b0)) b0 → ⊥
  bad4841  p = false≢true (sym (cong lower p))
  cut4841 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (op (var 2) (var 2)) (var 0)) (var 2))) , (var 2)) → ⊥
  cut4841  adequate = bad4841  (Adequate.valid adequate Two boolean env16)
  bad4842 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop (bop b0 b0) b0) b0)) b1 → ⊥
  bad4842  p = false≢true (cong lower p)
  cut4842 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (op (var 2) (var 2)) (var 0)) (var 2))) , (var 3)) → ⊥
  cut4842  adequate = bad4842  (Adequate.valid adequate Two boolean env4)
  bad4843 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop (bop b0 b0) b0) b1)) b0 → ⊥
  bad4843  p = false≢true (sym (cong lower p))
  cut4843 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (op (var 2) (var 2)) (var 0)) (var 3))) , (var 0)) → ⊥
  cut4843  adequate = bad4843  (Adequate.valid adequate Two boolean env4)
  bad4844 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop (bop b0 b0) b0) b1)) b0 → ⊥
  bad4844  p = false≢true (sym (cong lower p))
  cut4844 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (op (var 2) (var 2)) (var 0)) (var 3))) , (var 1)) → ⊥
  cut4844  adequate = bad4844  (Adequate.valid adequate Two boolean env4)
  bad4845 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop (bop b0 b0) b0) b1)) b0 → ⊥
  bad4845  p = false≢true (sym (cong lower p))
  cut4845 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (op (var 2) (var 2)) (var 0)) (var 3))) , (var 2)) → ⊥
  cut4845  adequate = bad4845  (Adequate.valid adequate Two boolean env4)
  bad4846 : PathP (λ _ → Two) (bop (bop b1 b0) (bop (bop (bop b0 b0) b1) b1)) b1 → ⊥
  bad4846  p = false≢true (cong lower p)
  cut4846 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (op (var 2) (var 2)) (var 0)) (var 3))) , (var 3)) → ⊥
  cut4846  adequate = bad4846  (Adequate.valid adequate Two boolean env18)
  bad4847 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop (bop b0 b0) b0) b0)) b1 → ⊥
  bad4847  p = false≢true (cong lower p)
  cut4847 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (op (var 2) (var 2)) (var 0)) (var 3))) , (var 4)) → ⊥
  cut4847  adequate = bad4847  (Adequate.valid adequate Two boolean env8)
  holds4848 : (z0 z1 z2 : A2) → (mul2 (mul2 z0 z1) (mul2 (mul2 (mul2 z2 z2) z1) z0)) ≡ z0
  holds4848 z0 z1 z2 = refl
  cut4848 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (op (var 2) (var 2)) (var 1)) (var 0))) , (var 0)) → ⊥
  cut4848  = reject2 ((op (op (var 0) (var 1)) (op (op (op (var 2) (var 2)) (var 1)) (var 0))) , (var 0)) (λ env → holds4848 (env 0) (env 1) (env 2))
  bad4849 : PathP (λ _ → Two) (bop (bop b0 b1) (bop (bop (bop b0 b0) b1) b0)) b1 → ⊥
  bad4849  p = false≢true (cong lower p)
  cut4849 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (op (var 2) (var 2)) (var 1)) (var 0))) , (var 1)) → ⊥
  cut4849  adequate = bad4849  (Adequate.valid adequate Two boolean env6)
  bad4850 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop (bop b1 b1) b0) b0)) b1 → ⊥
  bad4850  p = false≢true (cong lower p)
  cut4850 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (op (var 2) (var 2)) (var 1)) (var 0))) , (var 2)) → ⊥
  cut4850  adequate = bad4850  (Adequate.valid adequate Two boolean env2)
  bad4851 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop (bop b0 b0) b0) b0)) b1 → ⊥
  bad4851  p = false≢true (cong lower p)
  cut4851 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (op (var 2) (var 2)) (var 1)) (var 0))) , (var 3)) → ⊥
  cut4851  adequate = bad4851  (Adequate.valid adequate Two boolean env4)
  bad4852 : PathP (λ _ → Two) (bop (bop b0 b1) (bop (bop (bop b1 b1) b1) b1)) b0 → ⊥
  bad4852  p = false≢true (sym (cong lower p))
  cut4852 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (op (var 2) (var 2)) (var 1)) (var 1))) , (var 0)) → ⊥
  cut4852  adequate = bad4852  (Adequate.valid adequate Two boolean env3)
  bad4853 : PathP (λ _ → Two) (bop (bop b0 b1) (bop (bop (bop b0 b0) b1) b1)) b1 → ⊥
  bad4853  p = false≢true (cong lower p)
  cut4853 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (op (var 2) (var 2)) (var 1)) (var 1))) , (var 1)) → ⊥
  cut4853  adequate = bad4853  (Adequate.valid adequate Two boolean env6)
  bad4854 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop (bop b1 b1) b0) b0)) b1 → ⊥
  bad4854  p = false≢true (cong lower p)
  cut4854 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (op (var 2) (var 2)) (var 1)) (var 1))) , (var 2)) → ⊥
  cut4854  adequate = bad4854  (Adequate.valid adequate Two boolean env2)
  bad4855 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop (bop b0 b0) b0) b0)) b1 → ⊥
  bad4855  p = false≢true (cong lower p)
  cut4855 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (op (var 2) (var 2)) (var 1)) (var 1))) , (var 3)) → ⊥
  cut4855  adequate = bad4855  (Adequate.valid adequate Two boolean env4)
  bad4856 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop (bop b1 b1) b0) b1)) b0 → ⊥
  bad4856  p = false≢true (sym (cong lower p))
  cut4856 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (op (var 2) (var 2)) (var 1)) (var 2))) , (var 0)) → ⊥
  cut4856  adequate = bad4856  (Adequate.valid adequate Two boolean env2)
  bad4857 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop (bop b1 b1) b0) b1)) b0 → ⊥
  bad4857  p = false≢true (sym (cong lower p))
  cut4857 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (op (var 2) (var 2)) (var 1)) (var 2))) , (var 1)) → ⊥
  cut4857  adequate = bad4857  (Adequate.valid adequate Two boolean env2)
  bad4858 : PathP (λ _ → Two) (bop (bop b1 b1) (bop (bop (bop b0 b0) b1) b0)) b0 → ⊥
  bad4858  p = false≢true (sym (cong lower p))
  cut4858 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (op (var 2) (var 2)) (var 1)) (var 2))) , (var 2)) → ⊥
  cut4858  adequate = bad4858  (Adequate.valid adequate Two boolean env16)
  bad4859 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop (bop b0 b0) b0) b0)) b1 → ⊥
  bad4859  p = false≢true (cong lower p)
  cut4859 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (op (var 2) (var 2)) (var 1)) (var 2))) , (var 3)) → ⊥
  cut4859  adequate = bad4859  (Adequate.valid adequate Two boolean env4)
  bad4860 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop (bop b0 b0) b0) b1)) b0 → ⊥
  bad4860  p = false≢true (sym (cong lower p))
  cut4860 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (op (var 2) (var 2)) (var 1)) (var 3))) , (var 0)) → ⊥
  cut4860  adequate = bad4860  (Adequate.valid adequate Two boolean env4)
  bad4861 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop (bop b0 b0) b0) b1)) b0 → ⊥
  bad4861  p = false≢true (sym (cong lower p))
  cut4861 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (op (var 2) (var 2)) (var 1)) (var 3))) , (var 1)) → ⊥
  cut4861  adequate = bad4861  (Adequate.valid adequate Two boolean env4)
  bad4862 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop (bop b0 b0) b0) b1)) b0 → ⊥
  bad4862  p = false≢true (sym (cong lower p))
  cut4862 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (op (var 2) (var 2)) (var 1)) (var 3))) , (var 2)) → ⊥
  cut4862  adequate = bad4862  (Adequate.valid adequate Two boolean env4)
  bad4863 : PathP (λ _ → Two) (bop (bop b0 b1) (bop (bop (bop b0 b0) b1) b1)) b1 → ⊥
  bad4863  p = false≢true (cong lower p)
  cut4863 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (op (var 2) (var 2)) (var 1)) (var 3))) , (var 3)) → ⊥
  cut4863  adequate = bad4863  (Adequate.valid adequate Two boolean env10)
  bad4864 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop (bop b0 b0) b0) b0)) b1 → ⊥
  bad4864  p = false≢true (cong lower p)
  cut4864 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (op (var 2) (var 2)) (var 1)) (var 3))) , (var 4)) → ⊥
  cut4864  adequate = bad4864  (Adequate.valid adequate Two boolean env8)
  holds4865 : (z0 z1 z2 : A2) → (mul2 (mul2 z0 z1) (mul2 (mul2 (mul2 z2 z2) z2) z0)) ≡ z0
  holds4865 z0 z1 z2 = refl
  cut4865 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (op (var 2) (var 2)) (var 2)) (var 0))) , (var 0)) → ⊥
  cut4865  = reject2 ((op (op (var 0) (var 1)) (op (op (op (var 2) (var 2)) (var 2)) (var 0))) , (var 0)) (λ env → holds4865 (env 0) (env 1) (env 2))
  bad4866 : PathP (λ _ → Two) (bop (bop b0 b1) (bop (bop (bop b0 b0) b0) b0)) b1 → ⊥
  bad4866  p = false≢true (cong lower p)
  cut4866 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (op (var 2) (var 2)) (var 2)) (var 0))) , (var 1)) → ⊥
  cut4866  adequate = bad4866  (Adequate.valid adequate Two boolean env6)
  bad4867 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop (bop b1 b1) b1) b0)) b1 → ⊥
  bad4867  p = false≢true (cong lower p)
  cut4867 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (op (var 2) (var 2)) (var 2)) (var 0))) , (var 2)) → ⊥
  cut4867  adequate = bad4867  (Adequate.valid adequate Two boolean env2)
  bad4868 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop (bop b0 b0) b0) b0)) b1 → ⊥
  bad4868  p = false≢true (cong lower p)
  cut4868 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (op (var 2) (var 2)) (var 2)) (var 0))) , (var 3)) → ⊥
  cut4868  adequate = bad4868  (Adequate.valid adequate Two boolean env4)
  bad4869 : PathP (λ _ → Two) (bop (bop b0 b1) (bop (bop (bop b0 b0) b0) b1)) b0 → ⊥
  bad4869  p = false≢true (sym (cong lower p))
  cut4869 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (op (var 2) (var 2)) (var 2)) (var 1))) , (var 0)) → ⊥
  cut4869  adequate = bad4869  (Adequate.valid adequate Two boolean env6)
  holds4870 : (z0 z1 z2 : A3) → (mul3 (mul3 z0 z1) (mul3 (mul3 (mul3 z2 z2) z2) z1)) ≡ z1
  holds4870 z0 z1 z2 = refl
  cut4870 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (op (var 2) (var 2)) (var 2)) (var 1))) , (var 1)) → ⊥
  cut4870  = reject3 ((op (op (var 0) (var 1)) (op (op (op (var 2) (var 2)) (var 2)) (var 1))) , (var 1)) (λ env → holds4870 (env 0) (env 1) (env 2))
  bad4871 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop (bop b1 b1) b1) b0)) b1 → ⊥
  bad4871  p = false≢true (cong lower p)
  cut4871 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (op (var 2) (var 2)) (var 2)) (var 1))) , (var 2)) → ⊥
  cut4871  adequate = bad4871  (Adequate.valid adequate Two boolean env2)
  bad4872 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop (bop b0 b0) b0) b0)) b1 → ⊥
  bad4872  p = false≢true (cong lower p)
  cut4872 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (op (var 2) (var 2)) (var 2)) (var 1))) , (var 3)) → ⊥
  cut4872  adequate = bad4872  (Adequate.valid adequate Two boolean env4)
  bad4873 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop (bop b1 b1) b1) b1)) b0 → ⊥
  bad4873  p = false≢true (sym (cong lower p))
  cut4873 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (op (var 2) (var 2)) (var 2)) (var 2))) , (var 0)) → ⊥
  cut4873  adequate = bad4873  (Adequate.valid adequate Two boolean env2)
  bad4874 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop (bop b1 b1) b1) b1)) b0 → ⊥
  bad4874  p = false≢true (sym (cong lower p))
  cut4874 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (op (var 2) (var 2)) (var 2)) (var 2))) , (var 1)) → ⊥
  cut4874  adequate = bad4874  (Adequate.valid adequate Two boolean env2)
  bad4875 : PathP (λ _ → Two) (bop (bop b1 b1) (bop (bop (bop b0 b0) b0) b0)) b0 → ⊥
  bad4875  p = false≢true (sym (cong lower p))
  cut4875 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (op (var 2) (var 2)) (var 2)) (var 2))) , (var 2)) → ⊥
  cut4875  adequate = bad4875  (Adequate.valid adequate Two boolean env16)
  bad4876 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop (bop b0 b0) b0) b0)) b1 → ⊥
  bad4876  p = false≢true (cong lower p)
  cut4876 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (op (var 2) (var 2)) (var 2)) (var 2))) , (var 3)) → ⊥
  cut4876  adequate = bad4876  (Adequate.valid adequate Two boolean env4)
  bad4877 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop (bop b0 b0) b0) b1)) b0 → ⊥
  bad4877  p = false≢true (sym (cong lower p))
  cut4877 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (op (var 2) (var 2)) (var 2)) (var 3))) , (var 0)) → ⊥
  cut4877  adequate = bad4877  (Adequate.valid adequate Two boolean env4)
  bad4878 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop (bop b0 b0) b0) b1)) b0 → ⊥
  bad4878  p = false≢true (sym (cong lower p))
  cut4878 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (op (var 2) (var 2)) (var 2)) (var 3))) , (var 1)) → ⊥
  cut4878  adequate = bad4878  (Adequate.valid adequate Two boolean env4)
  bad4879 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop (bop b0 b0) b0) b1)) b0 → ⊥
  bad4879  p = false≢true (sym (cong lower p))
  cut4879 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (op (var 2) (var 2)) (var 2)) (var 3))) , (var 2)) → ⊥
  cut4879  adequate = bad4879  (Adequate.valid adequate Two boolean env4)
  env19 : ℕ → Two
  env19 zero = b1
  env19 (suc zero) = b1
  env19 (suc (suc zero)) = b0
  env19 (suc (suc (suc zero))) = b0
  env19 (suc (suc (suc (suc rest)))) = b0
  bad4880 : PathP (λ _ → Two) (bop (bop b1 b1) (bop (bop (bop b0 b0) b0) b0)) b0 → ⊥
  bad4880  p = false≢true (sym (cong lower p))
  cut4880 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (op (var 2) (var 2)) (var 2)) (var 3))) , (var 3)) → ⊥
  cut4880  adequate = bad4880  (Adequate.valid adequate Two boolean env19)
  bad4881 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop (bop b0 b0) b0) b0)) b1 → ⊥
  bad4881  p = false≢true (cong lower p)
  cut4881 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (op (var 2) (var 2)) (var 2)) (var 3))) , (var 4)) → ⊥
  cut4881  adequate = bad4881  (Adequate.valid adequate Two boolean env8)
  bad4882 : PathP (λ _ → Two) (bop (bop b1 b0) (bop (bop (bop b0 b0) b1) b1)) b1 → ⊥
  bad4882  p = false≢true (cong lower p)
  cut4882 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (op (var 2) (var 2)) (var 3)) (var 0))) , (var 0)) → ⊥
  cut4882  adequate = bad4882  (Adequate.valid adequate Two boolean env18)
  bad4883 : PathP (λ _ → Two) (bop (bop b0 b1) (bop (bop (bop b0 b0) b0) b0)) b1 → ⊥
  bad4883  p = false≢true (cong lower p)
  cut4883 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (op (var 2) (var 2)) (var 3)) (var 0))) , (var 1)) → ⊥
  cut4883  adequate = bad4883  (Adequate.valid adequate Two boolean env11)
  bad4884 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop (bop b1 b1) b0) b0)) b1 → ⊥
  bad4884  p = false≢true (cong lower p)
  cut4884 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (op (var 2) (var 2)) (var 3)) (var 0))) , (var 2)) → ⊥
  cut4884  adequate = bad4884  (Adequate.valid adequate Two boolean env12)
  bad4885 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop (bop b0 b0) b1) b0)) b1 → ⊥
  bad4885  p = false≢true (cong lower p)
  cut4885 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (op (var 2) (var 2)) (var 3)) (var 0))) , (var 3)) → ⊥
  cut4885  adequate = bad4885  (Adequate.valid adequate Two boolean env4)
  bad4886 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop (bop b0 b0) b0) b0)) b1 → ⊥
  bad4886  p = false≢true (cong lower p)
  cut4886 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (op (var 2) (var 2)) (var 3)) (var 0))) , (var 4)) → ⊥
  cut4886  adequate = bad4886  (Adequate.valid adequate Two boolean env8)
  bad4887 : PathP (λ _ → Two) (bop (bop b0 b1) (bop (bop (bop b0 b0) b0) b1)) b0 → ⊥
  bad4887  p = false≢true (sym (cong lower p))
  cut4887 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (op (var 2) (var 2)) (var 3)) (var 1))) , (var 0)) → ⊥
  cut4887  adequate = bad4887  (Adequate.valid adequate Two boolean env11)
  bad4888 : PathP (λ _ → Two) (bop (bop b0 b1) (bop (bop (bop b0 b0) b1) b1)) b1 → ⊥
  bad4888  p = false≢true (cong lower p)
  cut4888 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (op (var 2) (var 2)) (var 3)) (var 1))) , (var 1)) → ⊥
  cut4888  adequate = bad4888  (Adequate.valid adequate Two boolean env10)
  bad4889 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop (bop b1 b1) b0) b0)) b1 → ⊥
  bad4889  p = false≢true (cong lower p)
  cut4889 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (op (var 2) (var 2)) (var 3)) (var 1))) , (var 2)) → ⊥
  cut4889  adequate = bad4889  (Adequate.valid adequate Two boolean env12)
  bad4890 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop (bop b0 b0) b1) b0)) b1 → ⊥
  bad4890  p = false≢true (cong lower p)
  cut4890 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (op (var 2) (var 2)) (var 3)) (var 1))) , (var 3)) → ⊥
  cut4890  adequate = bad4890  (Adequate.valid adequate Two boolean env4)
  bad4891 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop (bop b0 b0) b0) b0)) b1 → ⊥
  bad4891  p = false≢true (cong lower p)
  cut4891 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (op (var 2) (var 2)) (var 3)) (var 1))) , (var 4)) → ⊥
  cut4891  adequate = bad4891  (Adequate.valid adequate Two boolean env8)
  bad4892 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop (bop b1 b1) b0) b1)) b0 → ⊥
  bad4892  p = false≢true (sym (cong lower p))
  cut4892 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (op (var 2) (var 2)) (var 3)) (var 2))) , (var 0)) → ⊥
  cut4892  adequate = bad4892  (Adequate.valid adequate Two boolean env12)
  bad4893 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop (bop b1 b1) b0) b1)) b0 → ⊥
  bad4893  p = false≢true (sym (cong lower p))
  cut4893 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (op (var 2) (var 2)) (var 3)) (var 2))) , (var 1)) → ⊥
  cut4893  adequate = bad4893  (Adequate.valid adequate Two boolean env12)
  bad4894 : PathP (λ _ → Two) (bop (bop b1 b1) (bop (bop (bop b0 b0) b0) b0)) b0 → ⊥
  bad4894  p = false≢true (sym (cong lower p))
  cut4894 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (op (var 2) (var 2)) (var 3)) (var 2))) , (var 2)) → ⊥
  cut4894  adequate = bad4894  (Adequate.valid adequate Two boolean env19)
  bad4895 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop (bop b0 b0) b1) b0)) b1 → ⊥
  bad4895  p = false≢true (cong lower p)
  cut4895 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (op (var 2) (var 2)) (var 3)) (var 2))) , (var 3)) → ⊥
  cut4895  adequate = bad4895  (Adequate.valid adequate Two boolean env4)
  bad4896 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop (bop b0 b0) b0) b0)) b1 → ⊥
  bad4896  p = false≢true (cong lower p)
  cut4896 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (op (var 2) (var 2)) (var 3)) (var 2))) , (var 4)) → ⊥
  cut4896  adequate = bad4896  (Adequate.valid adequate Two boolean env8)
  bad4897 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop (bop b1 b1) b1) b1)) b0 → ⊥
  bad4897  p = false≢true (sym (cong lower p))
  cut4897 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (op (var 2) (var 2)) (var 3)) (var 3))) , (var 0)) → ⊥
  cut4897  adequate = bad4897  (Adequate.valid adequate Two boolean env7)
  bad4898 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop (bop b1 b1) b1) b1)) b0 → ⊥
  bad4898  p = false≢true (sym (cong lower p))
  cut4898 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (op (var 2) (var 2)) (var 3)) (var 3))) , (var 1)) → ⊥
  cut4898  adequate = bad4898  (Adequate.valid adequate Two boolean env7)
  bad4899 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop (bop b1 b1) b0) b0)) b1 → ⊥
  bad4899  p = false≢true (cong lower p)
  cut4899 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (op (var 2) (var 2)) (var 3)) (var 3))) , (var 2)) → ⊥
  cut4899  adequate = bad4899  (Adequate.valid adequate Two boolean env12)
  bad4900 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop (bop b0 b0) b1) b1)) b1 → ⊥
  bad4900  p = false≢true (cong lower p)
  cut4900 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (op (var 2) (var 2)) (var 3)) (var 3))) , (var 3)) → ⊥
  cut4900  adequate = bad4900  (Adequate.valid adequate Two boolean env4)
  bad4901 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop (bop b0 b0) b0) b0)) b1 → ⊥
  bad4901  p = false≢true (cong lower p)
  cut4901 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (op (var 2) (var 2)) (var 3)) (var 3))) , (var 4)) → ⊥
  cut4901  adequate = bad4901  (Adequate.valid adequate Two boolean env8)
  bad4902 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop (bop b0 b0) b0) b1)) b0 → ⊥
  bad4902  p = false≢true (sym (cong lower p))
  cut4902 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (op (var 2) (var 2)) (var 3)) (var 4))) , (var 0)) → ⊥
  cut4902  adequate = bad4902  (Adequate.valid adequate Two boolean env8)
  bad4903 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop (bop b0 b0) b0) b1)) b0 → ⊥
  bad4903  p = false≢true (sym (cong lower p))
  cut4903 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (op (var 2) (var 2)) (var 3)) (var 4))) , (var 1)) → ⊥
  cut4903  adequate = bad4903  (Adequate.valid adequate Two boolean env8)
  bad4904 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop (bop b0 b0) b0) b1)) b0 → ⊥
  bad4904  p = false≢true (sym (cong lower p))
  cut4904 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (op (var 2) (var 2)) (var 3)) (var 4))) , (var 2)) → ⊥
  cut4904  adequate = bad4904  (Adequate.valid adequate Two boolean env8)
  bad4905 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop (bop b0 b0) b0) b1)) b0 → ⊥
  bad4905  p = false≢true (sym (cong lower p))
  cut4905 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (op (var 2) (var 2)) (var 3)) (var 4))) , (var 3)) → ⊥
  cut4905  adequate = bad4905  (Adequate.valid adequate Two boolean env8)
  bad4906 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop (bop b0 b0) b1) b1)) b1 → ⊥
  bad4906  p = false≢true (cong lower p)
  cut4906 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (op (var 2) (var 2)) (var 3)) (var 4))) , (var 4)) → ⊥
  cut4906  adequate = bad4906  (Adequate.valid adequate Two boolean env14)
  bad4907 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop (bop b0 b0) b0) b0)) b1 → ⊥
  bad4907  p = false≢true (cong lower p)
  cut4907 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (op (var 2) (var 2)) (var 3)) (var 4))) , (var 5)) → ⊥
  cut4907  adequate = bad4907  (Adequate.valid adequate Two boolean env15)
  bad4908 : PathP (λ _ → Two) (bop (bop b1 b0) (bop (bop (bop b0 b0) b1) b1)) b1 → ⊥
  bad4908  p = false≢true (cong lower p)
  cut4908 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (op (var 2) (var 3)) (var 0)) (var 0))) , (var 0)) → ⊥
  cut4908  adequate = bad4908  (Adequate.valid adequate Two boolean env9)
  bad4909 : PathP (λ _ → Two) (bop (bop b0 b1) (bop (bop (bop b0 b0) b0) b0)) b1 → ⊥
  bad4909  p = false≢true (cong lower p)
  cut4909 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (op (var 2) (var 3)) (var 0)) (var 0))) , (var 1)) → ⊥
  cut4909  adequate = bad4909  (Adequate.valid adequate Two boolean env11)
  bad4910 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop (bop b1 b0) b0) b0)) b1 → ⊥
  bad4910  p = false≢true (cong lower p)
  cut4910 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (op (var 2) (var 3)) (var 0)) (var 0))) , (var 2)) → ⊥
  cut4910  adequate = bad4910  (Adequate.valid adequate Two boolean env12)
  bad4911 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop (bop b0 b1) b0) b0)) b1 → ⊥
  bad4911  p = false≢true (cong lower p)
  cut4911 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (op (var 2) (var 3)) (var 0)) (var 0))) , (var 3)) → ⊥
  cut4911  adequate = bad4911  (Adequate.valid adequate Two boolean env4)
  bad4912 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop (bop b0 b0) b0) b0)) b1 → ⊥
  bad4912  p = false≢true (cong lower p)
  cut4912 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (op (var 2) (var 3)) (var 0)) (var 0))) , (var 4)) → ⊥
  cut4912  adequate = bad4912  (Adequate.valid adequate Two boolean env8)
  bad4913 : PathP (λ _ → Two) (bop (bop b0 b1) (bop (bop (bop b0 b0) b0) b1)) b0 → ⊥
  bad4913  p = false≢true (sym (cong lower p))
  cut4913 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (op (var 2) (var 3)) (var 0)) (var 1))) , (var 0)) → ⊥
  cut4913  adequate = bad4913  (Adequate.valid adequate Two boolean env11)
  holds4914 : (z0 z1 z2 z3 : A3) → (mul3 (mul3 z0 z1) (mul3 (mul3 (mul3 z2 z3) z0) z1)) ≡ z1
  holds4914 z0 z1 z2 z3 = refl
  cut4914 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (op (var 2) (var 3)) (var 0)) (var 1))) , (var 1)) → ⊥
  cut4914  = reject3 ((op (op (var 0) (var 1)) (op (op (op (var 2) (var 3)) (var 0)) (var 1))) , (var 1)) (λ env → holds4914 (env 0) (env 1) (env 2) (env 3))
  bad4915 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop (bop b1 b0) b0) b0)) b1 → ⊥
  bad4915  p = false≢true (cong lower p)
  cut4915 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (op (var 2) (var 3)) (var 0)) (var 1))) , (var 2)) → ⊥
  cut4915  adequate = bad4915  (Adequate.valid adequate Two boolean env12)
  bad4916 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop (bop b0 b1) b0) b0)) b1 → ⊥
  bad4916  p = false≢true (cong lower p)
  cut4916 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (op (var 2) (var 3)) (var 0)) (var 1))) , (var 3)) → ⊥
  cut4916  adequate = bad4916  (Adequate.valid adequate Two boolean env4)
  bad4917 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop (bop b0 b0) b0) b0)) b1 → ⊥
  bad4917  p = false≢true (cong lower p)
  cut4917 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (op (var 2) (var 3)) (var 0)) (var 1))) , (var 4)) → ⊥
  cut4917  adequate = bad4917  (Adequate.valid adequate Two boolean env8)
  bad4918 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop (bop b1 b0) b0) b1)) b0 → ⊥
  bad4918  p = false≢true (sym (cong lower p))
  cut4918 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (op (var 2) (var 3)) (var 0)) (var 2))) , (var 0)) → ⊥
  cut4918  adequate = bad4918  (Adequate.valid adequate Two boolean env12)
  bad4919 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop (bop b1 b0) b0) b1)) b0 → ⊥
  bad4919  p = false≢true (sym (cong lower p))
  cut4919 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (op (var 2) (var 3)) (var 0)) (var 2))) , (var 1)) → ⊥
  cut4919  adequate = bad4919  (Adequate.valid adequate Two boolean env12)
  env20 : ℕ → Two
  env20 zero = b1
  env20 (suc zero) = b0
  env20 (suc (suc zero)) = b1
  env20 (suc (suc (suc zero))) = b0
  env20 (suc (suc (suc (suc rest)))) = b0
  bad4920 : PathP (λ _ → Two) (bop (bop b1 b0) (bop (bop (bop b1 b0) b1) b1)) b1 → ⊥
  bad4920  p = false≢true (cong lower p)
  cut4920 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (op (var 2) (var 3)) (var 0)) (var 2))) , (var 2)) → ⊥
  cut4920  adequate = bad4920  (Adequate.valid adequate Two boolean env20)
  bad4921 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop (bop b0 b1) b0) b0)) b1 → ⊥
  bad4921  p = false≢true (cong lower p)
  cut4921 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (op (var 2) (var 3)) (var 0)) (var 2))) , (var 3)) → ⊥
  cut4921  adequate = bad4921  (Adequate.valid adequate Two boolean env4)
  bad4922 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop (bop b0 b0) b0) b0)) b1 → ⊥
  bad4922  p = false≢true (cong lower p)
  cut4922 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (op (var 2) (var 3)) (var 0)) (var 2))) , (var 4)) → ⊥
  cut4922  adequate = bad4922  (Adequate.valid adequate Two boolean env8)
  bad4923 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop (bop b0 b1) b0) b1)) b0 → ⊥
  bad4923  p = false≢true (sym (cong lower p))
  cut4923 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (op (var 2) (var 3)) (var 0)) (var 3))) , (var 0)) → ⊥
  cut4923  adequate = bad4923  (Adequate.valid adequate Two boolean env4)
  bad4924 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop (bop b0 b1) b0) b1)) b0 → ⊥
  bad4924  p = false≢true (sym (cong lower p))
  cut4924 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (op (var 2) (var 3)) (var 0)) (var 3))) , (var 1)) → ⊥
  cut4924  adequate = bad4924  (Adequate.valid adequate Two boolean env4)
  bad4925 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop (bop b0 b1) b0) b1)) b0 → ⊥
  bad4925  p = false≢true (sym (cong lower p))
  cut4925 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (op (var 2) (var 3)) (var 0)) (var 3))) , (var 2)) → ⊥
  cut4925  adequate = bad4925  (Adequate.valid adequate Two boolean env4)
  bad4926 : PathP (λ _ → Two) (bop (bop b1 b0) (bop (bop (bop b0 b1) b1) b1)) b1 → ⊥
  bad4926  p = false≢true (cong lower p)
  cut4926 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (op (var 2) (var 3)) (var 0)) (var 3))) , (var 3)) → ⊥
  cut4926  adequate = bad4926  (Adequate.valid adequate Two boolean env18)
  bad4927 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop (bop b0 b0) b0) b0)) b1 → ⊥
  bad4927  p = false≢true (cong lower p)
  cut4927 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (op (var 2) (var 3)) (var 0)) (var 3))) , (var 4)) → ⊥
  cut4927  adequate = bad4927  (Adequate.valid adequate Two boolean env8)
  bad4928 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop (bop b0 b0) b0) b1)) b0 → ⊥
  bad4928  p = false≢true (sym (cong lower p))
  cut4928 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (op (var 2) (var 3)) (var 0)) (var 4))) , (var 0)) → ⊥
  cut4928  adequate = bad4928  (Adequate.valid adequate Two boolean env8)
  bad4929 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop (bop b0 b0) b0) b1)) b0 → ⊥
  bad4929  p = false≢true (sym (cong lower p))
  cut4929 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (op (var 2) (var 3)) (var 0)) (var 4))) , (var 1)) → ⊥
  cut4929  adequate = bad4929  (Adequate.valid adequate Two boolean env8)
  bad4930 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop (bop b0 b0) b0) b1)) b0 → ⊥
  bad4930  p = false≢true (sym (cong lower p))
  cut4930 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (op (var 2) (var 3)) (var 0)) (var 4))) , (var 2)) → ⊥
  cut4930  adequate = bad4930  (Adequate.valid adequate Two boolean env8)
  bad4931 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop (bop b0 b0) b0) b1)) b0 → ⊥
  bad4931  p = false≢true (sym (cong lower p))
  cut4931 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (op (var 2) (var 3)) (var 0)) (var 4))) , (var 3)) → ⊥
  cut4931  adequate = bad4931  (Adequate.valid adequate Two boolean env8)
  env21 : ℕ → Two
  env21 zero = b1
  env21 (suc zero) = b0
  env21 (suc (suc zero)) = b0
  env21 (suc (suc (suc zero))) = b0
  env21 (suc (suc (suc (suc zero)))) = b1
  env21 (suc (suc (suc (suc (suc rest))))) = b0
  bad4932 : PathP (λ _ → Two) (bop (bop b1 b0) (bop (bop (bop b0 b0) b1) b1)) b1 → ⊥
  bad4932  p = false≢true (cong lower p)
  cut4932 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (op (var 2) (var 3)) (var 0)) (var 4))) , (var 4)) → ⊥
  cut4932  adequate = bad4932  (Adequate.valid adequate Two boolean env21)
  bad4933 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop (bop b0 b0) b0) b0)) b1 → ⊥
  bad4933  p = false≢true (cong lower p)
  cut4933 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (op (var 2) (var 3)) (var 0)) (var 4))) , (var 5)) → ⊥
  cut4933  adequate = bad4933  (Adequate.valid adequate Two boolean env15)
  holds4934 : (z0 z1 z2 z3 : A2) → (mul2 (mul2 z0 z1) (mul2 (mul2 (mul2 z2 z3) z1) z0)) ≡ z0
  holds4934 z0 z1 z2 z3 = refl
  cut4934 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (op (var 2) (var 3)) (var 1)) (var 0))) , (var 0)) → ⊥
  cut4934  = reject2 ((op (op (var 0) (var 1)) (op (op (op (var 2) (var 3)) (var 1)) (var 0))) , (var 0)) (λ env → holds4934 (env 0) (env 1) (env 2) (env 3))
  bad4935 : PathP (λ _ → Two) (bop (bop b0 b1) (bop (bop (bop b0 b0) b1) b0)) b1 → ⊥
  bad4935  p = false≢true (cong lower p)
  cut4935 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (op (var 2) (var 3)) (var 1)) (var 0))) , (var 1)) → ⊥
  cut4935  adequate = bad4935  (Adequate.valid adequate Two boolean env11)
  bad4936 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop (bop b1 b0) b0) b0)) b1 → ⊥
  bad4936  p = false≢true (cong lower p)
  cut4936 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (op (var 2) (var 3)) (var 1)) (var 0))) , (var 2)) → ⊥
  cut4936  adequate = bad4936  (Adequate.valid adequate Two boolean env12)
  bad4937 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop (bop b0 b1) b0) b0)) b1 → ⊥
  bad4937  p = false≢true (cong lower p)
  cut4937 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (op (var 2) (var 3)) (var 1)) (var 0))) , (var 3)) → ⊥
  cut4937  adequate = bad4937  (Adequate.valid adequate Two boolean env4)
  bad4938 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop (bop b0 b0) b0) b0)) b1 → ⊥
  bad4938  p = false≢true (cong lower p)
  cut4938 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (op (var 2) (var 3)) (var 1)) (var 0))) , (var 4)) → ⊥
  cut4938  adequate = bad4938  (Adequate.valid adequate Two boolean env8)
  bad4939 : PathP (λ _ → Two) (bop (bop b0 b1) (bop (bop (bop b1 b1) b1) b1)) b0 → ⊥
  bad4939  p = false≢true (sym (cong lower p))
  cut4939 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (op (var 2) (var 3)) (var 1)) (var 1))) , (var 0)) → ⊥
  cut4939  adequate = bad4939  (Adequate.valid adequate Two boolean env13)
  bad4940 : PathP (λ _ → Two) (bop (bop b0 b1) (bop (bop (bop b0 b0) b1) b1)) b1 → ⊥
  bad4940  p = false≢true (cong lower p)
  cut4940 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (op (var 2) (var 3)) (var 1)) (var 1))) , (var 1)) → ⊥
  cut4940  adequate = bad4940  (Adequate.valid adequate Two boolean env11)
  bad4941 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop (bop b1 b0) b0) b0)) b1 → ⊥
  bad4941  p = false≢true (cong lower p)
  cut4941 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (op (var 2) (var 3)) (var 1)) (var 1))) , (var 2)) → ⊥
  cut4941  adequate = bad4941  (Adequate.valid adequate Two boolean env12)
  bad4942 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop (bop b0 b1) b0) b0)) b1 → ⊥
  bad4942  p = false≢true (cong lower p)
  cut4942 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (op (var 2) (var 3)) (var 1)) (var 1))) , (var 3)) → ⊥
  cut4942  adequate = bad4942  (Adequate.valid adequate Two boolean env4)
  bad4943 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop (bop b0 b0) b0) b0)) b1 → ⊥
  bad4943  p = false≢true (cong lower p)
  cut4943 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (op (var 2) (var 3)) (var 1)) (var 1))) , (var 4)) → ⊥
  cut4943  adequate = bad4943  (Adequate.valid adequate Two boolean env8)
  bad4944 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop (bop b1 b0) b0) b1)) b0 → ⊥
  bad4944  p = false≢true (sym (cong lower p))
  cut4944 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (op (var 2) (var 3)) (var 1)) (var 2))) , (var 0)) → ⊥
  cut4944  adequate = bad4944  (Adequate.valid adequate Two boolean env12)
  bad4945 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop (bop b1 b0) b0) b1)) b0 → ⊥
  bad4945  p = false≢true (sym (cong lower p))
  cut4945 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (op (var 2) (var 3)) (var 1)) (var 2))) , (var 1)) → ⊥
  cut4945  adequate = bad4945  (Adequate.valid adequate Two boolean env12)
  env22 : ℕ → Two
  env22 zero = b0
  env22 (suc zero) = b1
  env22 (suc (suc zero)) = b1
  env22 (suc (suc (suc zero))) = b0
  env22 (suc (suc (suc (suc rest)))) = b0
  bad4946 : PathP (λ _ → Two) (bop (bop b0 b1) (bop (bop (bop b1 b0) b1) b1)) b1 → ⊥
  bad4946  p = false≢true (cong lower p)
  cut4946 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (op (var 2) (var 3)) (var 1)) (var 2))) , (var 2)) → ⊥
  cut4946  adequate = bad4946  (Adequate.valid adequate Two boolean env22)
  bad4947 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop (bop b0 b1) b0) b0)) b1 → ⊥
  bad4947  p = false≢true (cong lower p)
  cut4947 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (op (var 2) (var 3)) (var 1)) (var 2))) , (var 3)) → ⊥
  cut4947  adequate = bad4947  (Adequate.valid adequate Two boolean env4)
  bad4948 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop (bop b0 b0) b0) b0)) b1 → ⊥
  bad4948  p = false≢true (cong lower p)
  cut4948 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (op (var 2) (var 3)) (var 1)) (var 2))) , (var 4)) → ⊥
  cut4948  adequate = bad4948  (Adequate.valid adequate Two boolean env8)
  bad4949 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop (bop b0 b1) b0) b1)) b0 → ⊥
  bad4949  p = false≢true (sym (cong lower p))
  cut4949 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (op (var 2) (var 3)) (var 1)) (var 3))) , (var 0)) → ⊥
  cut4949  adequate = bad4949  (Adequate.valid adequate Two boolean env4)
  bad4950 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop (bop b0 b1) b0) b1)) b0 → ⊥
  bad4950  p = false≢true (sym (cong lower p))
  cut4950 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (op (var 2) (var 3)) (var 1)) (var 3))) , (var 1)) → ⊥
  cut4950  adequate = bad4950  (Adequate.valid adequate Two boolean env4)
  bad4951 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop (bop b0 b1) b0) b1)) b0 → ⊥
  bad4951  p = false≢true (sym (cong lower p))
  cut4951 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (op (var 2) (var 3)) (var 1)) (var 3))) , (var 2)) → ⊥
  cut4951  adequate = bad4951  (Adequate.valid adequate Two boolean env4)
  bad4952 : PathP (λ _ → Two) (bop (bop b0 b1) (bop (bop (bop b0 b1) b1) b1)) b1 → ⊥
  bad4952  p = false≢true (cong lower p)
  cut4952 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (op (var 2) (var 3)) (var 1)) (var 3))) , (var 3)) → ⊥
  cut4952  adequate = bad4952  (Adequate.valid adequate Two boolean env10)
  bad4953 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop (bop b0 b0) b0) b0)) b1 → ⊥
  bad4953  p = false≢true (cong lower p)
  cut4953 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (op (var 2) (var 3)) (var 1)) (var 3))) , (var 4)) → ⊥
  cut4953  adequate = bad4953  (Adequate.valid adequate Two boolean env8)
  bad4954 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop (bop b0 b0) b0) b1)) b0 → ⊥
  bad4954  p = false≢true (sym (cong lower p))
  cut4954 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (op (var 2) (var 3)) (var 1)) (var 4))) , (var 0)) → ⊥
  cut4954  adequate = bad4954  (Adequate.valid adequate Two boolean env8)
  bad4955 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop (bop b0 b0) b0) b1)) b0 → ⊥
  bad4955  p = false≢true (sym (cong lower p))
  cut4955 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (op (var 2) (var 3)) (var 1)) (var 4))) , (var 1)) → ⊥
  cut4955  adequate = bad4955  (Adequate.valid adequate Two boolean env8)
  bad4956 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop (bop b0 b0) b0) b1)) b0 → ⊥
  bad4956  p = false≢true (sym (cong lower p))
  cut4956 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (op (var 2) (var 3)) (var 1)) (var 4))) , (var 2)) → ⊥
  cut4956  adequate = bad4956  (Adequate.valid adequate Two boolean env8)
  bad4957 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop (bop b0 b0) b0) b1)) b0 → ⊥
  bad4957  p = false≢true (sym (cong lower p))
  cut4957 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (op (var 2) (var 3)) (var 1)) (var 4))) , (var 3)) → ⊥
  cut4957  adequate = bad4957  (Adequate.valid adequate Two boolean env8)
  env23 : ℕ → Two
  env23 zero = b0
  env23 (suc zero) = b1
  env23 (suc (suc zero)) = b0
  env23 (suc (suc (suc zero))) = b0
  env23 (suc (suc (suc (suc zero)))) = b1
  env23 (suc (suc (suc (suc (suc rest))))) = b0
  bad4958 : PathP (λ _ → Two) (bop (bop b0 b1) (bop (bop (bop b0 b0) b1) b1)) b1 → ⊥
  bad4958  p = false≢true (cong lower p)
  cut4958 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (op (var 2) (var 3)) (var 1)) (var 4))) , (var 4)) → ⊥
  cut4958  adequate = bad4958  (Adequate.valid adequate Two boolean env23)
  bad4959 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop (bop b0 b0) b0) b0)) b1 → ⊥
  bad4959  p = false≢true (cong lower p)
  cut4959 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (op (var 2) (var 3)) (var 1)) (var 4))) , (var 5)) → ⊥
  cut4959  adequate = bad4959  (Adequate.valid adequate Two boolean env15)
  bad4960 : PathP (λ _ → Two) (bop (bop b1 b0) (bop (bop (bop b1 b0) b1) b1)) b1 → ⊥
  bad4960  p = false≢true (cong lower p)
  cut4960 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (op (var 2) (var 3)) (var 2)) (var 0))) , (var 0)) → ⊥
  cut4960  adequate = bad4960  (Adequate.valid adequate Two boolean env20)
  bad4961 : PathP (λ _ → Two) (bop (bop b0 b1) (bop (bop (bop b0 b0) b0) b0)) b1 → ⊥
  bad4961  p = false≢true (cong lower p)
  cut4961 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (op (var 2) (var 3)) (var 2)) (var 0))) , (var 1)) → ⊥
  cut4961  adequate = bad4961  (Adequate.valid adequate Two boolean env11)
  bad4962 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop (bop b1 b0) b1) b0)) b1 → ⊥
  bad4962  p = false≢true (cong lower p)
  cut4962 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (op (var 2) (var 3)) (var 2)) (var 0))) , (var 2)) → ⊥
  cut4962  adequate = bad4962  (Adequate.valid adequate Two boolean env12)
  bad4963 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop (bop b0 b1) b0) b0)) b1 → ⊥
  bad4963  p = false≢true (cong lower p)
  cut4963 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (op (var 2) (var 3)) (var 2)) (var 0))) , (var 3)) → ⊥
  cut4963  adequate = bad4963  (Adequate.valid adequate Two boolean env4)
  bad4964 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop (bop b0 b0) b0) b0)) b1 → ⊥
  bad4964  p = false≢true (cong lower p)
  cut4964 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (op (var 2) (var 3)) (var 2)) (var 0))) , (var 4)) → ⊥
  cut4964  adequate = bad4964  (Adequate.valid adequate Two boolean env8)
  bad4965 : PathP (λ _ → Two) (bop (bop b0 b1) (bop (bop (bop b0 b0) b0) b1)) b0 → ⊥
  bad4965  p = false≢true (sym (cong lower p))
  cut4965 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (op (var 2) (var 3)) (var 2)) (var 1))) , (var 0)) → ⊥
  cut4965  adequate = bad4965  (Adequate.valid adequate Two boolean env11)
  bad4966 : PathP (λ _ → Two) (bop (bop b0 b1) (bop (bop (bop b1 b0) b1) b1)) b1 → ⊥
  bad4966  p = false≢true (cong lower p)
  cut4966 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (op (var 2) (var 3)) (var 2)) (var 1))) , (var 1)) → ⊥
  cut4966  adequate = bad4966  (Adequate.valid adequate Two boolean env22)
  bad4967 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop (bop b1 b0) b1) b0)) b1 → ⊥
  bad4967  p = false≢true (cong lower p)
  cut4967 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (op (var 2) (var 3)) (var 2)) (var 1))) , (var 2)) → ⊥
  cut4967  adequate = bad4967  (Adequate.valid adequate Two boolean env12)
  bad4968 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop (bop b0 b1) b0) b0)) b1 → ⊥
  bad4968  p = false≢true (cong lower p)
  cut4968 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (op (var 2) (var 3)) (var 2)) (var 1))) , (var 3)) → ⊥
  cut4968  adequate = bad4968  (Adequate.valid adequate Two boolean env4)
  bad4969 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop (bop b0 b0) b0) b0)) b1 → ⊥
  bad4969  p = false≢true (cong lower p)
  cut4969 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (op (var 2) (var 3)) (var 2)) (var 1))) , (var 4)) → ⊥
  cut4969  adequate = bad4969  (Adequate.valid adequate Two boolean env8)
  bad4970 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop (bop b1 b1) b1) b1)) b0 → ⊥
  bad4970  p = false≢true (sym (cong lower p))
  cut4970 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (op (var 2) (var 3)) (var 2)) (var 2))) , (var 0)) → ⊥
  cut4970  adequate = bad4970  (Adequate.valid adequate Two boolean env7)
  bad4971 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop (bop b1 b1) b1) b1)) b0 → ⊥
  bad4971  p = false≢true (sym (cong lower p))
  cut4971 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (op (var 2) (var 3)) (var 2)) (var 2))) , (var 1)) → ⊥
  cut4971  adequate = bad4971  (Adequate.valid adequate Two boolean env7)
  bad4972 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop (bop b1 b0) b1) b1)) b1 → ⊥
  bad4972  p = false≢true (cong lower p)
  cut4972 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (op (var 2) (var 3)) (var 2)) (var 2))) , (var 2)) → ⊥
  cut4972  adequate = bad4972  (Adequate.valid adequate Two boolean env12)
  bad4973 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop (bop b0 b1) b0) b0)) b1 → ⊥
  bad4973  p = false≢true (cong lower p)
  cut4973 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (op (var 2) (var 3)) (var 2)) (var 2))) , (var 3)) → ⊥
  cut4973  adequate = bad4973  (Adequate.valid adequate Two boolean env4)
  bad4974 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop (bop b0 b0) b0) b0)) b1 → ⊥
  bad4974  p = false≢true (cong lower p)
  cut4974 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (op (var 2) (var 3)) (var 2)) (var 2))) , (var 4)) → ⊥
  cut4974  adequate = bad4974  (Adequate.valid adequate Two boolean env8)
  bad4975 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop (bop b0 b1) b0) b1)) b0 → ⊥
  bad4975  p = false≢true (sym (cong lower p))
  cut4975 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (op (var 2) (var 3)) (var 2)) (var 3))) , (var 0)) → ⊥
  cut4975  adequate = bad4975  (Adequate.valid adequate Two boolean env4)
  bad4976 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop (bop b0 b1) b0) b1)) b0 → ⊥
  bad4976  p = false≢true (sym (cong lower p))
  cut4976 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (op (var 2) (var 3)) (var 2)) (var 3))) , (var 1)) → ⊥
  cut4976  adequate = bad4976  (Adequate.valid adequate Two boolean env4)
  bad4977 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop (bop b0 b1) b0) b1)) b0 → ⊥
  bad4977  p = false≢true (sym (cong lower p))
  cut4977 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (op (var 2) (var 3)) (var 2)) (var 3))) , (var 2)) → ⊥
  cut4977  adequate = bad4977  (Adequate.valid adequate Two boolean env4)
  bad4978 : PathP (λ _ → Two) (bop (bop b1 b1) (bop (bop (bop b0 b0) b0) b0)) b0 → ⊥
  bad4978  p = false≢true (sym (cong lower p))
  cut4978 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (op (var 2) (var 3)) (var 2)) (var 3))) , (var 3)) → ⊥
  cut4978  adequate = bad4978  (Adequate.valid adequate Two boolean env19)
  bad4979 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop (bop b0 b0) b0) b0)) b1 → ⊥
  bad4979  p = false≢true (cong lower p)
  cut4979 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (op (var 2) (var 3)) (var 2)) (var 3))) , (var 4)) → ⊥
  cut4979  adequate = bad4979  (Adequate.valid adequate Two boolean env8)
  bad4980 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop (bop b0 b0) b0) b1)) b0 → ⊥
  bad4980  p = false≢true (sym (cong lower p))
  cut4980 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (op (var 2) (var 3)) (var 2)) (var 4))) , (var 0)) → ⊥
  cut4980  adequate = bad4980  (Adequate.valid adequate Two boolean env8)
  bad4981 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop (bop b0 b0) b0) b1)) b0 → ⊥
  bad4981  p = false≢true (sym (cong lower p))
  cut4981 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (op (var 2) (var 3)) (var 2)) (var 4))) , (var 1)) → ⊥
  cut4981  adequate = bad4981  (Adequate.valid adequate Two boolean env8)
  bad4982 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop (bop b0 b0) b0) b1)) b0 → ⊥
  bad4982  p = false≢true (sym (cong lower p))
  cut4982 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (op (var 2) (var 3)) (var 2)) (var 4))) , (var 2)) → ⊥
  cut4982  adequate = bad4982  (Adequate.valid adequate Two boolean env8)
  bad4983 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop (bop b0 b0) b0) b1)) b0 → ⊥
  bad4983  p = false≢true (sym (cong lower p))
  cut4983 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (op (var 2) (var 3)) (var 2)) (var 4))) , (var 3)) → ⊥
  cut4983  adequate = bad4983  (Adequate.valid adequate Two boolean env8)
  env24 : ℕ → Two
  env24 zero = b0
  env24 (suc zero) = b0
  env24 (suc (suc zero)) = b1
  env24 (suc (suc (suc zero))) = b0
  env24 (suc (suc (suc (suc zero)))) = b1
  env24 (suc (suc (suc (suc (suc rest))))) = b0
  bad4984 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop (bop b1 b0) b1) b1)) b1 → ⊥
  bad4984  p = false≢true (cong lower p)
  cut4984 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (op (var 2) (var 3)) (var 2)) (var 4))) , (var 4)) → ⊥
  cut4984  adequate = bad4984  (Adequate.valid adequate Two boolean env24)
  bad4985 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop (bop b0 b0) b0) b0)) b1 → ⊥
  bad4985  p = false≢true (cong lower p)
  cut4985 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (op (var 2) (var 3)) (var 2)) (var 4))) , (var 5)) → ⊥
  cut4985  adequate = bad4985  (Adequate.valid adequate Two boolean env15)
  bad4986 : PathP (λ _ → Two) (bop (bop b1 b0) (bop (bop (bop b0 b1) b1) b1)) b1 → ⊥
  bad4986  p = false≢true (cong lower p)
  cut4986 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (op (var 2) (var 3)) (var 3)) (var 0))) , (var 0)) → ⊥
  cut4986  adequate = bad4986  (Adequate.valid adequate Two boolean env18)
  bad4987 : PathP (λ _ → Two) (bop (bop b0 b1) (bop (bop (bop b0 b0) b0) b0)) b1 → ⊥
  bad4987  p = false≢true (cong lower p)
  cut4987 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (op (var 2) (var 3)) (var 3)) (var 0))) , (var 1)) → ⊥
  cut4987  adequate = bad4987  (Adequate.valid adequate Two boolean env11)
  bad4988 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop (bop b1 b0) b0) b0)) b1 → ⊥
  bad4988  p = false≢true (cong lower p)
  cut4988 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (op (var 2) (var 3)) (var 3)) (var 0))) , (var 2)) → ⊥
  cut4988  adequate = bad4988  (Adequate.valid adequate Two boolean env12)
  bad4989 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop (bop b0 b1) b1) b0)) b1 → ⊥
  bad4989  p = false≢true (cong lower p)
  cut4989 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (op (var 2) (var 3)) (var 3)) (var 0))) , (var 3)) → ⊥
  cut4989  adequate = bad4989  (Adequate.valid adequate Two boolean env4)
  bad4990 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop (bop b0 b0) b0) b0)) b1 → ⊥
  bad4990  p = false≢true (cong lower p)
  cut4990 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (op (var 2) (var 3)) (var 3)) (var 0))) , (var 4)) → ⊥
  cut4990  adequate = bad4990  (Adequate.valid adequate Two boolean env8)
  bad4991 : PathP (λ _ → Two) (bop (bop b0 b1) (bop (bop (bop b0 b0) b0) b1)) b0 → ⊥
  bad4991  p = false≢true (sym (cong lower p))
  cut4991 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (op (var 2) (var 3)) (var 3)) (var 1))) , (var 0)) → ⊥
  cut4991  adequate = bad4991  (Adequate.valid adequate Two boolean env11)
  bad4992 : PathP (λ _ → Two) (bop (bop b0 b1) (bop (bop (bop b0 b1) b1) b1)) b1 → ⊥
  bad4992  p = false≢true (cong lower p)
  cut4992 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (op (var 2) (var 3)) (var 3)) (var 1))) , (var 1)) → ⊥
  cut4992  adequate = bad4992  (Adequate.valid adequate Two boolean env10)
  bad4993 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop (bop b1 b0) b0) b0)) b1 → ⊥
  bad4993  p = false≢true (cong lower p)
  cut4993 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (op (var 2) (var 3)) (var 3)) (var 1))) , (var 2)) → ⊥
  cut4993  adequate = bad4993  (Adequate.valid adequate Two boolean env12)
  bad4994 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop (bop b0 b1) b1) b0)) b1 → ⊥
  bad4994  p = false≢true (cong lower p)
  cut4994 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (op (var 2) (var 3)) (var 3)) (var 1))) , (var 3)) → ⊥
  cut4994  adequate = bad4994  (Adequate.valid adequate Two boolean env4)
  bad4995 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop (bop b0 b0) b0) b0)) b1 → ⊥
  bad4995  p = false≢true (cong lower p)
  cut4995 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (op (var 2) (var 3)) (var 3)) (var 1))) , (var 4)) → ⊥
  cut4995  adequate = bad4995  (Adequate.valid adequate Two boolean env8)
  bad4996 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop (bop b1 b0) b0) b1)) b0 → ⊥
  bad4996  p = false≢true (sym (cong lower p))
  cut4996 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (op (var 2) (var 3)) (var 3)) (var 2))) , (var 0)) → ⊥
  cut4996  adequate = bad4996  (Adequate.valid adequate Two boolean env12)
  bad4997 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop (bop b1 b0) b0) b1)) b0 → ⊥
  bad4997  p = false≢true (sym (cong lower p))
  cut4997 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (op (var 2) (var 3)) (var 3)) (var 2))) , (var 1)) → ⊥
  cut4997  adequate = bad4997  (Adequate.valid adequate Two boolean env12)
  bad4998 : PathP (λ _ → Two) (bop (bop b1 b1) (bop (bop (bop b0 b0) b0) b0)) b0 → ⊥
  bad4998  p = false≢true (sym (cong lower p))
  cut4998 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (op (var 2) (var 3)) (var 3)) (var 2))) , (var 2)) → ⊥
  cut4998  adequate = bad4998  (Adequate.valid adequate Two boolean env19)
  bad4999 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop (bop b0 b1) b1) b0)) b1 → ⊥
  bad4999  p = false≢true (cong lower p)
  cut4999 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (op (var 2) (var 3)) (var 3)) (var 2))) , (var 3)) → ⊥
  cut4999  adequate = bad4999  (Adequate.valid adequate Two boolean env4)
  bad5000 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop (bop b0 b0) b0) b0)) b1 → ⊥
  bad5000  p = false≢true (cong lower p)
  cut5000 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (op (var 2) (var 3)) (var 3)) (var 2))) , (var 4)) → ⊥
  cut5000  adequate = bad5000  (Adequate.valid adequate Two boolean env8)
  bad5001 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop (bop b1 b1) b1) b1)) b0 → ⊥
  bad5001  p = false≢true (sym (cong lower p))
  cut5001 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (op (var 2) (var 3)) (var 3)) (var 3))) , (var 0)) → ⊥
  cut5001  adequate = bad5001  (Adequate.valid adequate Two boolean env7)
  bad5002 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop (bop b1 b1) b1) b1)) b0 → ⊥
  bad5002  p = false≢true (sym (cong lower p))
  cut5002 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (op (var 2) (var 3)) (var 3)) (var 3))) , (var 1)) → ⊥
  cut5002  adequate = bad5002  (Adequate.valid adequate Two boolean env7)
  bad5003 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop (bop b1 b0) b0) b0)) b1 → ⊥
  bad5003  p = false≢true (cong lower p)
  cut5003 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (op (var 2) (var 3)) (var 3)) (var 3))) , (var 2)) → ⊥
  cut5003  adequate = bad5003  (Adequate.valid adequate Two boolean env12)
  bad5004 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop (bop b0 b1) b1) b1)) b1 → ⊥
  bad5004  p = false≢true (cong lower p)
  cut5004 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (op (var 2) (var 3)) (var 3)) (var 3))) , (var 3)) → ⊥
  cut5004  adequate = bad5004  (Adequate.valid adequate Two boolean env4)
  bad5005 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop (bop b0 b0) b0) b0)) b1 → ⊥
  bad5005  p = false≢true (cong lower p)
  cut5005 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (op (var 2) (var 3)) (var 3)) (var 3))) , (var 4)) → ⊥
  cut5005  adequate = bad5005  (Adequate.valid adequate Two boolean env8)
  bad5006 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop (bop b0 b0) b0) b1)) b0 → ⊥
  bad5006  p = false≢true (sym (cong lower p))
  cut5006 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (op (var 2) (var 3)) (var 3)) (var 4))) , (var 0)) → ⊥
  cut5006  adequate = bad5006  (Adequate.valid adequate Two boolean env8)
  bad5007 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop (bop b0 b0) b0) b1)) b0 → ⊥
  bad5007  p = false≢true (sym (cong lower p))
  cut5007 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (op (var 2) (var 3)) (var 3)) (var 4))) , (var 1)) → ⊥
  cut5007  adequate = bad5007  (Adequate.valid adequate Two boolean env8)
  bad5008 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop (bop b0 b0) b0) b1)) b0 → ⊥
  bad5008  p = false≢true (sym (cong lower p))
  cut5008 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (op (var 2) (var 3)) (var 3)) (var 4))) , (var 2)) → ⊥
  cut5008  adequate = bad5008  (Adequate.valid adequate Two boolean env8)
  bad5009 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop (bop b0 b0) b0) b1)) b0 → ⊥
  bad5009  p = false≢true (sym (cong lower p))
  cut5009 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (op (var 2) (var 3)) (var 3)) (var 4))) , (var 3)) → ⊥
  cut5009  adequate = bad5009  (Adequate.valid adequate Two boolean env8)
  bad5010 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop (bop b0 b1) b1) b1)) b1 → ⊥
  bad5010  p = false≢true (cong lower p)
  cut5010 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (op (var 2) (var 3)) (var 3)) (var 4))) , (var 4)) → ⊥
  cut5010  adequate = bad5010  (Adequate.valid adequate Two boolean env14)
  bad5011 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop (bop b0 b0) b0) b0)) b1 → ⊥
  bad5011  p = false≢true (cong lower p)
  cut5011 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (op (var 2) (var 3)) (var 3)) (var 4))) , (var 5)) → ⊥
  cut5011  adequate = bad5011  (Adequate.valid adequate Two boolean env15)
  bad5012 : PathP (λ _ → Two) (bop (bop b1 b0) (bop (bop (bop b0 b0) b1) b1)) b1 → ⊥
  bad5012  p = false≢true (cong lower p)
  cut5012 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (op (var 2) (var 3)) (var 4)) (var 0))) , (var 0)) → ⊥
  cut5012  adequate = bad5012  (Adequate.valid adequate Two boolean env21)
  env25 : ℕ → Two
  env25 zero = b0
  env25 (suc zero) = b1
  env25 (suc (suc zero)) = b0
  env25 (suc (suc (suc zero))) = b0
  env25 (suc (suc (suc (suc zero)))) = b0
  env25 (suc (suc (suc (suc (suc rest))))) = b0
  bad5013 : PathP (λ _ → Two) (bop (bop b0 b1) (bop (bop (bop b0 b0) b0) b0)) b1 → ⊥
  bad5013  p = false≢true (cong lower p)
  cut5013 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (op (var 2) (var 3)) (var 4)) (var 0))) , (var 1)) → ⊥
  cut5013  adequate = bad5013  (Adequate.valid adequate Two boolean env25)
  env26 : ℕ → Two
  env26 zero = b0
  env26 (suc zero) = b0
  env26 (suc (suc zero)) = b1
  env26 (suc (suc (suc zero))) = b0
  env26 (suc (suc (suc (suc zero)))) = b0
  env26 (suc (suc (suc (suc (suc rest))))) = b0
  bad5014 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop (bop b1 b0) b0) b0)) b1 → ⊥
  bad5014  p = false≢true (cong lower p)
  cut5014 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (op (var 2) (var 3)) (var 4)) (var 0))) , (var 2)) → ⊥
  cut5014  adequate = bad5014  (Adequate.valid adequate Two boolean env26)
  env27 : ℕ → Two
  env27 zero = b0
  env27 (suc zero) = b0
  env27 (suc (suc zero)) = b0
  env27 (suc (suc (suc zero))) = b1
  env27 (suc (suc (suc (suc zero)))) = b0
  env27 (suc (suc (suc (suc (suc rest))))) = b0
  bad5015 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop (bop b0 b1) b0) b0)) b1 → ⊥
  bad5015  p = false≢true (cong lower p)
  cut5015 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (op (var 2) (var 3)) (var 4)) (var 0))) , (var 3)) → ⊥
  cut5015  adequate = bad5015  (Adequate.valid adequate Two boolean env27)
  bad5016 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop (bop b0 b0) b1) b0)) b1 → ⊥
  bad5016  p = false≢true (cong lower p)
  cut5016 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (op (var 2) (var 3)) (var 4)) (var 0))) , (var 4)) → ⊥
  cut5016  adequate = bad5016  (Adequate.valid adequate Two boolean env8)
  bad5017 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop (bop b0 b0) b0) b0)) b1 → ⊥
  bad5017  p = false≢true (cong lower p)
  cut5017 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (op (var 2) (var 3)) (var 4)) (var 0))) , (var 5)) → ⊥
  cut5017  adequate = bad5017  (Adequate.valid adequate Two boolean env15)
  bad5018 : PathP (λ _ → Two) (bop (bop b0 b1) (bop (bop (bop b0 b0) b0) b1)) b0 → ⊥
  bad5018  p = false≢true (sym (cong lower p))
  cut5018 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (op (var 2) (var 3)) (var 4)) (var 1))) , (var 0)) → ⊥
  cut5018  adequate = bad5018  (Adequate.valid adequate Two boolean env25)
  bad5019 : PathP (λ _ → Two) (bop (bop b0 b1) (bop (bop (bop b0 b0) b1) b1)) b1 → ⊥
  bad5019  p = false≢true (cong lower p)
  cut5019 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (op (var 2) (var 3)) (var 4)) (var 1))) , (var 1)) → ⊥
  cut5019  adequate = bad5019  (Adequate.valid adequate Two boolean env23)
  bad5020 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop (bop b1 b0) b0) b0)) b1 → ⊥
  bad5020  p = false≢true (cong lower p)
  cut5020 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (op (var 2) (var 3)) (var 4)) (var 1))) , (var 2)) → ⊥
  cut5020  adequate = bad5020  (Adequate.valid adequate Two boolean env26)
  bad5021 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop (bop b0 b1) b0) b0)) b1 → ⊥
  bad5021  p = false≢true (cong lower p)
  cut5021 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (op (var 2) (var 3)) (var 4)) (var 1))) , (var 3)) → ⊥
  cut5021  adequate = bad5021  (Adequate.valid adequate Two boolean env27)
  bad5022 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop (bop b0 b0) b1) b0)) b1 → ⊥
  bad5022  p = false≢true (cong lower p)
  cut5022 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (op (var 2) (var 3)) (var 4)) (var 1))) , (var 4)) → ⊥
  cut5022  adequate = bad5022  (Adequate.valid adequate Two boolean env8)
  bad5023 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop (bop b0 b0) b0) b0)) b1 → ⊥
  bad5023  p = false≢true (cong lower p)
  cut5023 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (op (var 2) (var 3)) (var 4)) (var 1))) , (var 5)) → ⊥
  cut5023  adequate = bad5023  (Adequate.valid adequate Two boolean env15)
  bad5024 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop (bop b1 b0) b0) b1)) b0 → ⊥
  bad5024  p = false≢true (sym (cong lower p))
  cut5024 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (op (var 2) (var 3)) (var 4)) (var 2))) , (var 0)) → ⊥
  cut5024  adequate = bad5024  (Adequate.valid adequate Two boolean env26)
  bad5025 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop (bop b1 b0) b0) b1)) b0 → ⊥
  bad5025  p = false≢true (sym (cong lower p))
  cut5025 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (op (var 2) (var 3)) (var 4)) (var 2))) , (var 1)) → ⊥
  cut5025  adequate = bad5025  (Adequate.valid adequate Two boolean env26)
  bad5026 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop (bop b1 b0) b1) b1)) b1 → ⊥
  bad5026  p = false≢true (cong lower p)
  cut5026 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (op (var 2) (var 3)) (var 4)) (var 2))) , (var 2)) → ⊥
  cut5026  adequate = bad5026  (Adequate.valid adequate Two boolean env24)
  bad5027 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop (bop b0 b1) b0) b0)) b1 → ⊥
  bad5027  p = false≢true (cong lower p)
  cut5027 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (op (var 2) (var 3)) (var 4)) (var 2))) , (var 3)) → ⊥
  cut5027  adequate = bad5027  (Adequate.valid adequate Two boolean env27)
  bad5028 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop (bop b0 b0) b1) b0)) b1 → ⊥
  bad5028  p = false≢true (cong lower p)
  cut5028 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (op (var 2) (var 3)) (var 4)) (var 2))) , (var 4)) → ⊥
  cut5028  adequate = bad5028  (Adequate.valid adequate Two boolean env8)
  bad5029 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop (bop b0 b0) b0) b0)) b1 → ⊥
  bad5029  p = false≢true (cong lower p)
  cut5029 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (op (var 2) (var 3)) (var 4)) (var 2))) , (var 5)) → ⊥
  cut5029  adequate = bad5029  (Adequate.valid adequate Two boolean env15)
  bad5030 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop (bop b0 b1) b0) b1)) b0 → ⊥
  bad5030  p = false≢true (sym (cong lower p))
  cut5030 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (op (var 2) (var 3)) (var 4)) (var 3))) , (var 0)) → ⊥
  cut5030  adequate = bad5030  (Adequate.valid adequate Two boolean env27)
  bad5031 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop (bop b0 b1) b0) b1)) b0 → ⊥
  bad5031  p = false≢true (sym (cong lower p))
  cut5031 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (op (var 2) (var 3)) (var 4)) (var 3))) , (var 1)) → ⊥
  cut5031  adequate = bad5031  (Adequate.valid adequate Two boolean env27)
  bad5032 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop (bop b0 b1) b0) b1)) b0 → ⊥
  bad5032  p = false≢true (sym (cong lower p))
  cut5032 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (op (var 2) (var 3)) (var 4)) (var 3))) , (var 2)) → ⊥
  cut5032  adequate = bad5032  (Adequate.valid adequate Two boolean env27)
  bad5033 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop (bop b0 b1) b1) b1)) b1 → ⊥
  bad5033  p = false≢true (cong lower p)
  cut5033 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (op (var 2) (var 3)) (var 4)) (var 3))) , (var 3)) → ⊥
  cut5033  adequate = bad5033  (Adequate.valid adequate Two boolean env14)
  bad5034 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop (bop b0 b0) b1) b0)) b1 → ⊥
  bad5034  p = false≢true (cong lower p)
  cut5034 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (op (var 2) (var 3)) (var 4)) (var 3))) , (var 4)) → ⊥
  cut5034  adequate = bad5034  (Adequate.valid adequate Two boolean env8)
  bad5035 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop (bop b0 b0) b0) b0)) b1 → ⊥
  bad5035  p = false≢true (cong lower p)
  cut5035 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (op (var 2) (var 3)) (var 4)) (var 3))) , (var 5)) → ⊥
  cut5035  adequate = bad5035  (Adequate.valid adequate Two boolean env15)
  env28 : ℕ → Two
  env28 zero = b0
  env28 (suc zero) = b0
  env28 (suc (suc zero)) = b1
  env28 (suc (suc (suc zero))) = b1
  env28 (suc (suc (suc (suc zero)))) = b1
  env28 (suc (suc (suc (suc (suc rest))))) = b0
  bad5036 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop (bop b1 b1) b1) b1)) b0 → ⊥
  bad5036  p = false≢true (sym (cong lower p))
  cut5036 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (op (var 2) (var 3)) (var 4)) (var 4))) , (var 0)) → ⊥
  cut5036  adequate = bad5036  (Adequate.valid adequate Two boolean env28)
  bad5037 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop (bop b1 b1) b1) b1)) b0 → ⊥
  bad5037  p = false≢true (sym (cong lower p))
  cut5037 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (op (var 2) (var 3)) (var 4)) (var 4))) , (var 1)) → ⊥
  cut5037  adequate = bad5037  (Adequate.valid adequate Two boolean env28)
  bad5038 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop (bop b1 b0) b0) b0)) b1 → ⊥
  bad5038  p = false≢true (cong lower p)
  cut5038 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (op (var 2) (var 3)) (var 4)) (var 4))) , (var 2)) → ⊥
  cut5038  adequate = bad5038  (Adequate.valid adequate Two boolean env26)
  bad5039 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop (bop b0 b1) b0) b0)) b1 → ⊥
  bad5039  p = false≢true (cong lower p)
  cut5039 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (op (var 2) (var 3)) (var 4)) (var 4))) , (var 3)) → ⊥
  cut5039  adequate = bad5039  (Adequate.valid adequate Two boolean env27)
  bad5040 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop (bop b0 b0) b1) b1)) b1 → ⊥
  bad5040  p = false≢true (cong lower p)
  cut5040 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (op (var 2) (var 3)) (var 4)) (var 4))) , (var 4)) → ⊥
  cut5040  adequate = bad5040  (Adequate.valid adequate Two boolean env8)
  bad5041 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop (bop b0 b0) b0) b0)) b1 → ⊥
  bad5041  p = false≢true (cong lower p)
  cut5041 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (op (var 2) (var 3)) (var 4)) (var 4))) , (var 5)) → ⊥
  cut5041  adequate = bad5041  (Adequate.valid adequate Two boolean env15)
  bad5042 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop (bop b0 b0) b0) b1)) b0 → ⊥
  bad5042  p = false≢true (sym (cong lower p))
  cut5042 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (op (var 2) (var 3)) (var 4)) (var 5))) , (var 0)) → ⊥
  cut5042  adequate = bad5042  (Adequate.valid adequate Two boolean env15)
  bad5043 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop (bop b0 b0) b0) b1)) b0 → ⊥
  bad5043  p = false≢true (sym (cong lower p))
  cut5043 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (op (var 2) (var 3)) (var 4)) (var 5))) , (var 1)) → ⊥
  cut5043  adequate = bad5043  (Adequate.valid adequate Two boolean env15)
  bad5044 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop (bop b0 b0) b0) b1)) b0 → ⊥
  bad5044  p = false≢true (sym (cong lower p))
  cut5044 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (op (var 2) (var 3)) (var 4)) (var 5))) , (var 2)) → ⊥
  cut5044  adequate = bad5044  (Adequate.valid adequate Two boolean env15)
  bad5045 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop (bop b0 b0) b0) b1)) b0 → ⊥
  bad5045  p = false≢true (sym (cong lower p))
  cut5045 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (op (var 2) (var 3)) (var 4)) (var 5))) , (var 3)) → ⊥
  cut5045  adequate = bad5045  (Adequate.valid adequate Two boolean env15)
  bad5046 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop (bop b0 b0) b0) b1)) b0 → ⊥
  bad5046  p = false≢true (sym (cong lower p))
  cut5046 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (op (var 2) (var 3)) (var 4)) (var 5))) , (var 4)) → ⊥
  cut5046  adequate = bad5046  (Adequate.valid adequate Two boolean env15)
  env29 : ℕ → Two
  env29 zero = b0
  env29 (suc zero) = b0
  env29 (suc (suc zero)) = b0
  env29 (suc (suc (suc zero))) = b0
  env29 (suc (suc (suc (suc zero)))) = b1
  env29 (suc (suc (suc (suc (suc zero))))) = b1
  env29 (suc (suc (suc (suc (suc (suc rest)))))) = b0
  bad5047 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop (bop b0 b0) b1) b1)) b1 → ⊥
  bad5047  p = false≢true (cong lower p)
  cut5047 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (op (var 2) (var 3)) (var 4)) (var 5))) , (var 5)) → ⊥
  cut5047  adequate = bad5047  (Adequate.valid adequate Two boolean env29)
  env30 : ℕ → Two
  env30 zero = b0
  env30 (suc zero) = b0
  env30 (suc (suc zero)) = b0
  env30 (suc (suc (suc zero))) = b0
  env30 (suc (suc (suc (suc zero)))) = b0
  env30 (suc (suc (suc (suc (suc zero))))) = b0
  env30 (suc (suc (suc (suc (suc (suc zero)))))) = b1
  env30 (suc (suc (suc (suc (suc (suc (suc rest))))))) = b0
  bad5048 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop (bop b0 b0) b0) b0)) b1 → ⊥
  bad5048  p = false≢true (cong lower p)
  cut5048 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (op (var 2) (var 3)) (var 4)) (var 5))) , (var 6)) → ⊥
  cut5048  adequate = bad5048  (Adequate.valid adequate Two boolean env30)
