{-# OPTIONS --safe --cubical --guardedness #-}
module GeneratedMinimumShape171 where
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
  holds3295 : (z0 : A1) → (mul1 (mul1 z0 z0) (mul1 (mul1 z0 (mul1 z0 z0)) z0)) ≡ z0
  holds3295 m1c0 = refl
  holds3295 m1c1 = refl
  cut3295 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (op (var 0) (op (var 0) (var 0))) (var 0))) , (var 0)) → ⊥
  cut3295  = reject1 ((op (op (var 0) (var 0)) (op (op (var 0) (op (var 0) (var 0))) (var 0))) , (var 0)) (λ env → holds3295 (env 0))
  env0 : ℕ → Two
  env0 zero = b0
  env0 (suc zero) = b1
  env0 (suc (suc rest)) = b0
  bad3296 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b0 (bop b0 b0)) b0)) b1 → ⊥
  bad3296  p = false≢true (cong lower p)
  cut3296 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (op (var 0) (op (var 0) (var 0))) (var 0))) , (var 1)) → ⊥
  cut3296  adequate = bad3296  (Adequate.valid adequate Two boolean env0)
  bad3297 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b0 (bop b0 b0)) b1)) b0 → ⊥
  bad3297  p = false≢true (sym (cong lower p))
  cut3297 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (op (var 0) (op (var 0) (var 0))) (var 1))) , (var 0)) → ⊥
  cut3297  adequate = bad3297  (Adequate.valid adequate Two boolean env0)
  env1 : ℕ → Two
  env1 zero = b1
  env1 (suc zero) = b0
  env1 (suc (suc rest)) = b0
  bad3298 : PathP (λ _ → Two) (bop (bop b1 b1) (bop (bop b1 (bop b1 b1)) b0)) b0 → ⊥
  bad3298  p = false≢true (sym (cong lower p))
  cut3298 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (op (var 0) (op (var 0) (var 0))) (var 1))) , (var 1)) → ⊥
  cut3298  adequate = bad3298  (Adequate.valid adequate Two boolean env1)
  env2 : ℕ → Two
  env2 zero = b0
  env2 (suc zero) = b0
  env2 (suc (suc zero)) = b1
  env2 (suc (suc (suc rest))) = b0
  bad3299 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b0 (bop b0 b0)) b0)) b1 → ⊥
  bad3299  p = false≢true (cong lower p)
  cut3299 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (op (var 0) (op (var 0) (var 0))) (var 1))) , (var 2)) → ⊥
  cut3299  adequate = bad3299  (Adequate.valid adequate Two boolean env2)
  holds3300 : (z0 z1 : A2) → (mul2 (mul2 z0 z0) (mul2 (mul2 z0 (mul2 z0 z1)) z0)) ≡ z0
  holds3300 z0 z1 = refl
  cut3300 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (op (var 0) (op (var 0) (var 1))) (var 0))) , (var 0)) → ⊥
  cut3300  = reject2 ((op (op (var 0) (var 0)) (op (op (var 0) (op (var 0) (var 1))) (var 0))) , (var 0)) (λ env → holds3300 (env 0) (env 1))
  bad3301 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b0 (bop b0 b1)) b0)) b1 → ⊥
  bad3301  p = false≢true (cong lower p)
  cut3301 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (op (var 0) (op (var 0) (var 1))) (var 0))) , (var 1)) → ⊥
  cut3301  adequate = bad3301  (Adequate.valid adequate Two boolean env0)
  bad3302 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b0 (bop b0 b0)) b0)) b1 → ⊥
  bad3302  p = false≢true (cong lower p)
  cut3302 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (op (var 0) (op (var 0) (var 1))) (var 0))) , (var 2)) → ⊥
  cut3302  adequate = bad3302  (Adequate.valid adequate Two boolean env2)
  bad3303 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b0 (bop b0 b1)) b1)) b0 → ⊥
  bad3303  p = false≢true (sym (cong lower p))
  cut3303 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (op (var 0) (op (var 0) (var 1))) (var 1))) , (var 0)) → ⊥
  cut3303  adequate = bad3303  (Adequate.valid adequate Two boolean env0)
  bad3304 : PathP (λ _ → Two) (bop (bop b1 b1) (bop (bop b1 (bop b1 b0)) b0)) b0 → ⊥
  bad3304  p = false≢true (sym (cong lower p))
  cut3304 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (op (var 0) (op (var 0) (var 1))) (var 1))) , (var 1)) → ⊥
  cut3304  adequate = bad3304  (Adequate.valid adequate Two boolean env1)
  bad3305 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b0 (bop b0 b0)) b0)) b1 → ⊥
  bad3305  p = false≢true (cong lower p)
  cut3305 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (op (var 0) (op (var 0) (var 1))) (var 1))) , (var 2)) → ⊥
  cut3305  adequate = bad3305  (Adequate.valid adequate Two boolean env2)
  bad3306 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b0 (bop b0 b0)) b1)) b0 → ⊥
  bad3306  p = false≢true (sym (cong lower p))
  cut3306 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (op (var 0) (op (var 0) (var 1))) (var 2))) , (var 0)) → ⊥
  cut3306  adequate = bad3306  (Adequate.valid adequate Two boolean env2)
  bad3307 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b0 (bop b0 b0)) b1)) b0 → ⊥
  bad3307  p = false≢true (sym (cong lower p))
  cut3307 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (op (var 0) (op (var 0) (var 1))) (var 2))) , (var 1)) → ⊥
  cut3307  adequate = bad3307  (Adequate.valid adequate Two boolean env2)
  env3 : ℕ → Two
  env3 zero = b1
  env3 (suc zero) = b0
  env3 (suc (suc zero)) = b0
  env3 (suc (suc (suc rest))) = b0
  bad3308 : PathP (λ _ → Two) (bop (bop b1 b1) (bop (bop b1 (bop b1 b0)) b0)) b0 → ⊥
  bad3308  p = false≢true (sym (cong lower p))
  cut3308 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (op (var 0) (op (var 0) (var 1))) (var 2))) , (var 2)) → ⊥
  cut3308  adequate = bad3308  (Adequate.valid adequate Two boolean env3)
  env4 : ℕ → Two
  env4 zero = b0
  env4 (suc zero) = b0
  env4 (suc (suc zero)) = b0
  env4 (suc (suc (suc zero))) = b1
  env4 (suc (suc (suc (suc rest)))) = b0
  bad3309 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b0 (bop b0 b0)) b0)) b1 → ⊥
  bad3309  p = false≢true (cong lower p)
  cut3309 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (op (var 0) (op (var 0) (var 1))) (var 2))) , (var 3)) → ⊥
  cut3309  adequate = bad3309  (Adequate.valid adequate Two boolean env4)
  holds3310 : (z0 z1 : A2) → (mul2 (mul2 z0 z0) (mul2 (mul2 z0 (mul2 z1 z0)) z0)) ≡ z0
  holds3310 z0 z1 = refl
  cut3310 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (op (var 0) (op (var 1) (var 0))) (var 0))) , (var 0)) → ⊥
  cut3310  = reject2 ((op (op (var 0) (var 0)) (op (op (var 0) (op (var 1) (var 0))) (var 0))) , (var 0)) (λ env → holds3310 (env 0) (env 1))
  bad3311 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b0 (bop b1 b0)) b0)) b1 → ⊥
  bad3311  p = false≢true (cong lower p)
  cut3311 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (op (var 0) (op (var 1) (var 0))) (var 0))) , (var 1)) → ⊥
  cut3311  adequate = bad3311  (Adequate.valid adequate Two boolean env0)
  bad3312 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b0 (bop b0 b0)) b0)) b1 → ⊥
  bad3312  p = false≢true (cong lower p)
  cut3312 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (op (var 0) (op (var 1) (var 0))) (var 0))) , (var 2)) → ⊥
  cut3312  adequate = bad3312  (Adequate.valid adequate Two boolean env2)
  bad3313 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b0 (bop b1 b0)) b1)) b0 → ⊥
  bad3313  p = false≢true (sym (cong lower p))
  cut3313 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (op (var 0) (op (var 1) (var 0))) (var 1))) , (var 0)) → ⊥
  cut3313  adequate = bad3313  (Adequate.valid adequate Two boolean env0)
  bad3314 : PathP (λ _ → Two) (bop (bop b1 b1) (bop (bop b1 (bop b0 b1)) b0)) b0 → ⊥
  bad3314  p = false≢true (sym (cong lower p))
  cut3314 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (op (var 0) (op (var 1) (var 0))) (var 1))) , (var 1)) → ⊥
  cut3314  adequate = bad3314  (Adequate.valid adequate Two boolean env1)
  bad3315 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b0 (bop b0 b0)) b0)) b1 → ⊥
  bad3315  p = false≢true (cong lower p)
  cut3315 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (op (var 0) (op (var 1) (var 0))) (var 1))) , (var 2)) → ⊥
  cut3315  adequate = bad3315  (Adequate.valid adequate Two boolean env2)
  bad3316 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b0 (bop b0 b0)) b1)) b0 → ⊥
  bad3316  p = false≢true (sym (cong lower p))
  cut3316 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (op (var 0) (op (var 1) (var 0))) (var 2))) , (var 0)) → ⊥
  cut3316  adequate = bad3316  (Adequate.valid adequate Two boolean env2)
  bad3317 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b0 (bop b0 b0)) b1)) b0 → ⊥
  bad3317  p = false≢true (sym (cong lower p))
  cut3317 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (op (var 0) (op (var 1) (var 0))) (var 2))) , (var 1)) → ⊥
  cut3317  adequate = bad3317  (Adequate.valid adequate Two boolean env2)
  bad3318 : PathP (λ _ → Two) (bop (bop b1 b1) (bop (bop b1 (bop b0 b1)) b0)) b0 → ⊥
  bad3318  p = false≢true (sym (cong lower p))
  cut3318 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (op (var 0) (op (var 1) (var 0))) (var 2))) , (var 2)) → ⊥
  cut3318  adequate = bad3318  (Adequate.valid adequate Two boolean env3)
  bad3319 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b0 (bop b0 b0)) b0)) b1 → ⊥
  bad3319  p = false≢true (cong lower p)
  cut3319 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (op (var 0) (op (var 1) (var 0))) (var 2))) , (var 3)) → ⊥
  cut3319  adequate = bad3319  (Adequate.valid adequate Two boolean env4)
  holds3320 : (z0 z1 : A2) → (mul2 (mul2 z0 z0) (mul2 (mul2 z0 (mul2 z1 z1)) z0)) ≡ z0
  holds3320 z0 z1 = refl
  cut3320 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (op (var 0) (op (var 1) (var 1))) (var 0))) , (var 0)) → ⊥
  cut3320  = reject2 ((op (op (var 0) (var 0)) (op (op (var 0) (op (var 1) (var 1))) (var 0))) , (var 0)) (λ env → holds3320 (env 0) (env 1))
  bad3321 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b0 (bop b1 b1)) b0)) b1 → ⊥
  bad3321  p = false≢true (cong lower p)
  cut3321 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (op (var 0) (op (var 1) (var 1))) (var 0))) , (var 1)) → ⊥
  cut3321  adequate = bad3321  (Adequate.valid adequate Two boolean env0)
  bad3322 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b0 (bop b0 b0)) b0)) b1 → ⊥
  bad3322  p = false≢true (cong lower p)
  cut3322 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (op (var 0) (op (var 1) (var 1))) (var 0))) , (var 2)) → ⊥
  cut3322  adequate = bad3322  (Adequate.valid adequate Two boolean env2)
  bad3323 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b0 (bop b1 b1)) b1)) b0 → ⊥
  bad3323  p = false≢true (sym (cong lower p))
  cut3323 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (op (var 0) (op (var 1) (var 1))) (var 1))) , (var 0)) → ⊥
  cut3323  adequate = bad3323  (Adequate.valid adequate Two boolean env0)
  bad3324 : PathP (λ _ → Two) (bop (bop b1 b1) (bop (bop b1 (bop b0 b0)) b0)) b0 → ⊥
  bad3324  p = false≢true (sym (cong lower p))
  cut3324 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (op (var 0) (op (var 1) (var 1))) (var 1))) , (var 1)) → ⊥
  cut3324  adequate = bad3324  (Adequate.valid adequate Two boolean env1)
  bad3325 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b0 (bop b0 b0)) b0)) b1 → ⊥
  bad3325  p = false≢true (cong lower p)
  cut3325 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (op (var 0) (op (var 1) (var 1))) (var 1))) , (var 2)) → ⊥
  cut3325  adequate = bad3325  (Adequate.valid adequate Two boolean env2)
  bad3326 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b0 (bop b0 b0)) b1)) b0 → ⊥
  bad3326  p = false≢true (sym (cong lower p))
  cut3326 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (op (var 0) (op (var 1) (var 1))) (var 2))) , (var 0)) → ⊥
  cut3326  adequate = bad3326  (Adequate.valid adequate Two boolean env2)
  bad3327 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b0 (bop b0 b0)) b1)) b0 → ⊥
  bad3327  p = false≢true (sym (cong lower p))
  cut3327 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (op (var 0) (op (var 1) (var 1))) (var 2))) , (var 1)) → ⊥
  cut3327  adequate = bad3327  (Adequate.valid adequate Two boolean env2)
  bad3328 : PathP (λ _ → Two) (bop (bop b1 b1) (bop (bop b1 (bop b0 b0)) b0)) b0 → ⊥
  bad3328  p = false≢true (sym (cong lower p))
  cut3328 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (op (var 0) (op (var 1) (var 1))) (var 2))) , (var 2)) → ⊥
  cut3328  adequate = bad3328  (Adequate.valid adequate Two boolean env3)
  bad3329 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b0 (bop b0 b0)) b0)) b1 → ⊥
  bad3329  p = false≢true (cong lower p)
  cut3329 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (op (var 0) (op (var 1) (var 1))) (var 2))) , (var 3)) → ⊥
  cut3329  adequate = bad3329  (Adequate.valid adequate Two boolean env4)
  holds3330 : (z0 z1 z2 : A2) → (mul2 (mul2 z0 z0) (mul2 (mul2 z0 (mul2 z1 z2)) z0)) ≡ z0
  holds3330 z0 z1 z2 = refl
  cut3330 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (op (var 0) (op (var 1) (var 2))) (var 0))) , (var 0)) → ⊥
  cut3330  = reject2 ((op (op (var 0) (var 0)) (op (op (var 0) (op (var 1) (var 2))) (var 0))) , (var 0)) (λ env → holds3330 (env 0) (env 1) (env 2))
  env5 : ℕ → Two
  env5 zero = b0
  env5 (suc zero) = b1
  env5 (suc (suc zero)) = b0
  env5 (suc (suc (suc rest))) = b0
  bad3331 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b0 (bop b1 b0)) b0)) b1 → ⊥
  bad3331  p = false≢true (cong lower p)
  cut3331 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (op (var 0) (op (var 1) (var 2))) (var 0))) , (var 1)) → ⊥
  cut3331  adequate = bad3331  (Adequate.valid adequate Two boolean env5)
  bad3332 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b0 (bop b0 b1)) b0)) b1 → ⊥
  bad3332  p = false≢true (cong lower p)
  cut3332 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (op (var 0) (op (var 1) (var 2))) (var 0))) , (var 2)) → ⊥
  cut3332  adequate = bad3332  (Adequate.valid adequate Two boolean env2)
  bad3333 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b0 (bop b0 b0)) b0)) b1 → ⊥
  bad3333  p = false≢true (cong lower p)
  cut3333 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (op (var 0) (op (var 1) (var 2))) (var 0))) , (var 3)) → ⊥
  cut3333  adequate = bad3333  (Adequate.valid adequate Two boolean env4)
  bad3334 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b0 (bop b1 b0)) b1)) b0 → ⊥
  bad3334  p = false≢true (sym (cong lower p))
  cut3334 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (op (var 0) (op (var 1) (var 2))) (var 1))) , (var 0)) → ⊥
  cut3334  adequate = bad3334  (Adequate.valid adequate Two boolean env5)
  bad3335 : PathP (λ _ → Two) (bop (bop b1 b1) (bop (bop b1 (bop b0 b0)) b0)) b0 → ⊥
  bad3335  p = false≢true (sym (cong lower p))
  cut3335 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (op (var 0) (op (var 1) (var 2))) (var 1))) , (var 1)) → ⊥
  cut3335  adequate = bad3335  (Adequate.valid adequate Two boolean env3)
  bad3336 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b0 (bop b0 b1)) b0)) b1 → ⊥
  bad3336  p = false≢true (cong lower p)
  cut3336 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (op (var 0) (op (var 1) (var 2))) (var 1))) , (var 2)) → ⊥
  cut3336  adequate = bad3336  (Adequate.valid adequate Two boolean env2)
  bad3337 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b0 (bop b0 b0)) b0)) b1 → ⊥
  bad3337  p = false≢true (cong lower p)
  cut3337 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (op (var 0) (op (var 1) (var 2))) (var 1))) , (var 3)) → ⊥
  cut3337  adequate = bad3337  (Adequate.valid adequate Two boolean env4)
  bad3338 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b0 (bop b0 b1)) b1)) b0 → ⊥
  bad3338  p = false≢true (sym (cong lower p))
  cut3338 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (op (var 0) (op (var 1) (var 2))) (var 2))) , (var 0)) → ⊥
  cut3338  adequate = bad3338  (Adequate.valid adequate Two boolean env2)
  bad3339 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b0 (bop b0 b1)) b1)) b0 → ⊥
  bad3339  p = false≢true (sym (cong lower p))
  cut3339 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (op (var 0) (op (var 1) (var 2))) (var 2))) , (var 1)) → ⊥
  cut3339  adequate = bad3339  (Adequate.valid adequate Two boolean env2)
  bad3340 : PathP (λ _ → Two) (bop (bop b1 b1) (bop (bop b1 (bop b0 b0)) b0)) b0 → ⊥
  bad3340  p = false≢true (sym (cong lower p))
  cut3340 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (op (var 0) (op (var 1) (var 2))) (var 2))) , (var 2)) → ⊥
  cut3340  adequate = bad3340  (Adequate.valid adequate Two boolean env3)
  bad3341 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b0 (bop b0 b0)) b0)) b1 → ⊥
  bad3341  p = false≢true (cong lower p)
  cut3341 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (op (var 0) (op (var 1) (var 2))) (var 2))) , (var 3)) → ⊥
  cut3341  adequate = bad3341  (Adequate.valid adequate Two boolean env4)
  bad3342 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b0 (bop b0 b0)) b1)) b0 → ⊥
  bad3342  p = false≢true (sym (cong lower p))
  cut3342 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (op (var 0) (op (var 1) (var 2))) (var 3))) , (var 0)) → ⊥
  cut3342  adequate = bad3342  (Adequate.valid adequate Two boolean env4)
  bad3343 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b0 (bop b0 b0)) b1)) b0 → ⊥
  bad3343  p = false≢true (sym (cong lower p))
  cut3343 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (op (var 0) (op (var 1) (var 2))) (var 3))) , (var 1)) → ⊥
  cut3343  adequate = bad3343  (Adequate.valid adequate Two boolean env4)
  bad3344 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b0 (bop b0 b0)) b1)) b0 → ⊥
  bad3344  p = false≢true (sym (cong lower p))
  cut3344 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (op (var 0) (op (var 1) (var 2))) (var 3))) , (var 2)) → ⊥
  cut3344  adequate = bad3344  (Adequate.valid adequate Two boolean env4)
  env6 : ℕ → Two
  env6 zero = b1
  env6 (suc zero) = b0
  env6 (suc (suc zero)) = b0
  env6 (suc (suc (suc zero))) = b0
  env6 (suc (suc (suc (suc rest)))) = b0
  bad3345 : PathP (λ _ → Two) (bop (bop b1 b1) (bop (bop b1 (bop b0 b0)) b0)) b0 → ⊥
  bad3345  p = false≢true (sym (cong lower p))
  cut3345 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (op (var 0) (op (var 1) (var 2))) (var 3))) , (var 3)) → ⊥
  cut3345  adequate = bad3345  (Adequate.valid adequate Two boolean env6)
  env7 : ℕ → Two
  env7 zero = b0
  env7 (suc zero) = b0
  env7 (suc (suc zero)) = b0
  env7 (suc (suc (suc zero))) = b0
  env7 (suc (suc (suc (suc zero)))) = b1
  env7 (suc (suc (suc (suc (suc rest))))) = b0
  bad3346 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b0 (bop b0 b0)) b0)) b1 → ⊥
  bad3346  p = false≢true (cong lower p)
  cut3346 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (op (var 0) (op (var 1) (var 2))) (var 3))) , (var 4)) → ⊥
  cut3346  adequate = bad3346  (Adequate.valid adequate Two boolean env7)
  holds3347 : (z0 z1 : A2) → (mul2 (mul2 z0 z0) (mul2 (mul2 z1 (mul2 z0 z0)) z0)) ≡ z0
  holds3347 z0 z1 = refl
  cut3347 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (op (var 1) (op (var 0) (var 0))) (var 0))) , (var 0)) → ⊥
  cut3347  = reject2 ((op (op (var 0) (var 0)) (op (op (var 1) (op (var 0) (var 0))) (var 0))) , (var 0)) (λ env → holds3347 (env 0) (env 1))
  bad3348 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b1 (bop b0 b0)) b0)) b1 → ⊥
  bad3348  p = false≢true (cong lower p)
  cut3348 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (op (var 1) (op (var 0) (var 0))) (var 0))) , (var 1)) → ⊥
  cut3348  adequate = bad3348  (Adequate.valid adequate Two boolean env0)
  bad3349 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b0 (bop b0 b0)) b0)) b1 → ⊥
  bad3349  p = false≢true (cong lower p)
  cut3349 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (op (var 1) (op (var 0) (var 0))) (var 0))) , (var 2)) → ⊥
  cut3349  adequate = bad3349  (Adequate.valid adequate Two boolean env2)
  holds3350 : (z0 z1 : A2) → (mul2 (mul2 z0 z0) (mul2 (mul2 z1 (mul2 z0 z0)) z1)) ≡ z0
  holds3350 z0 z1 = refl
  cut3350 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (op (var 1) (op (var 0) (var 0))) (var 1))) , (var 0)) → ⊥
  cut3350  = reject2 ((op (op (var 0) (var 0)) (op (op (var 1) (op (var 0) (var 0))) (var 1))) , (var 0)) (λ env → holds3350 (env 0) (env 1))
  bad3351 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b1 (bop b0 b0)) b1)) b1 → ⊥
  bad3351  p = false≢true (cong lower p)
  cut3351 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (op (var 1) (op (var 0) (var 0))) (var 1))) , (var 1)) → ⊥
  cut3351  adequate = bad3351  (Adequate.valid adequate Two boolean env0)
  bad3352 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b0 (bop b0 b0)) b0)) b1 → ⊥
  bad3352  p = false≢true (cong lower p)
  cut3352 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (op (var 1) (op (var 0) (var 0))) (var 1))) , (var 2)) → ⊥
  cut3352  adequate = bad3352  (Adequate.valid adequate Two boolean env2)
  bad3353 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b0 (bop b0 b0)) b1)) b0 → ⊥
  bad3353  p = false≢true (sym (cong lower p))
  cut3353 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (op (var 1) (op (var 0) (var 0))) (var 2))) , (var 0)) → ⊥
  cut3353  adequate = bad3353  (Adequate.valid adequate Two boolean env2)
  bad3354 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b0 (bop b0 b0)) b1)) b0 → ⊥
  bad3354  p = false≢true (sym (cong lower p))
  cut3354 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (op (var 1) (op (var 0) (var 0))) (var 2))) , (var 1)) → ⊥
  cut3354  adequate = bad3354  (Adequate.valid adequate Two boolean env2)
  env8 : ℕ → Two
  env8 zero = b0
  env8 (suc zero) = b1
  env8 (suc (suc zero)) = b1
  env8 (suc (suc (suc rest))) = b0
  bad3355 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b1 (bop b0 b0)) b1)) b1 → ⊥
  bad3355  p = false≢true (cong lower p)
  cut3355 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (op (var 1) (op (var 0) (var 0))) (var 2))) , (var 2)) → ⊥
  cut3355  adequate = bad3355  (Adequate.valid adequate Two boolean env8)
  bad3356 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b0 (bop b0 b0)) b0)) b1 → ⊥
  bad3356  p = false≢true (cong lower p)
  cut3356 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (op (var 1) (op (var 0) (var 0))) (var 2))) , (var 3)) → ⊥
  cut3356  adequate = bad3356  (Adequate.valid adequate Two boolean env4)
  holds3357 : (z0 z1 : A2) → (mul2 (mul2 z0 z0) (mul2 (mul2 z1 (mul2 z0 z1)) z0)) ≡ z0
  holds3357 z0 z1 = refl
  cut3357 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (op (var 1) (op (var 0) (var 1))) (var 0))) , (var 0)) → ⊥
  cut3357  = reject2 ((op (op (var 0) (var 0)) (op (op (var 1) (op (var 0) (var 1))) (var 0))) , (var 0)) (λ env → holds3357 (env 0) (env 1))
  bad3358 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b1 (bop b0 b1)) b0)) b1 → ⊥
  bad3358  p = false≢true (cong lower p)
  cut3358 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (op (var 1) (op (var 0) (var 1))) (var 0))) , (var 1)) → ⊥
  cut3358  adequate = bad3358  (Adequate.valid adequate Two boolean env0)
  bad3359 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b0 (bop b0 b0)) b0)) b1 → ⊥
  bad3359  p = false≢true (cong lower p)
  cut3359 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (op (var 1) (op (var 0) (var 1))) (var 0))) , (var 2)) → ⊥
  cut3359  adequate = bad3359  (Adequate.valid adequate Two boolean env2)
  holds3360 : (z0 z1 : A2) → (mul2 (mul2 z0 z0) (mul2 (mul2 z1 (mul2 z0 z1)) z1)) ≡ z0
  holds3360 z0 z1 = refl
  cut3360 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (op (var 1) (op (var 0) (var 1))) (var 1))) , (var 0)) → ⊥
  cut3360  = reject2 ((op (op (var 0) (var 0)) (op (op (var 1) (op (var 0) (var 1))) (var 1))) , (var 0)) (λ env → holds3360 (env 0) (env 1))
  bad3361 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b1 (bop b0 b1)) b1)) b1 → ⊥
  bad3361  p = false≢true (cong lower p)
  cut3361 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (op (var 1) (op (var 0) (var 1))) (var 1))) , (var 1)) → ⊥
  cut3361  adequate = bad3361  (Adequate.valid adequate Two boolean env0)
  bad3362 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b0 (bop b0 b0)) b0)) b1 → ⊥
  bad3362  p = false≢true (cong lower p)
  cut3362 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (op (var 1) (op (var 0) (var 1))) (var 1))) , (var 2)) → ⊥
  cut3362  adequate = bad3362  (Adequate.valid adequate Two boolean env2)
  bad3363 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b0 (bop b0 b0)) b1)) b0 → ⊥
  bad3363  p = false≢true (sym (cong lower p))
  cut3363 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (op (var 1) (op (var 0) (var 1))) (var 2))) , (var 0)) → ⊥
  cut3363  adequate = bad3363  (Adequate.valid adequate Two boolean env2)
  bad3364 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b0 (bop b0 b0)) b1)) b0 → ⊥
  bad3364  p = false≢true (sym (cong lower p))
  cut3364 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (op (var 1) (op (var 0) (var 1))) (var 2))) , (var 1)) → ⊥
  cut3364  adequate = bad3364  (Adequate.valid adequate Two boolean env2)
  bad3365 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b1 (bop b0 b1)) b1)) b1 → ⊥
  bad3365  p = false≢true (cong lower p)
  cut3365 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (op (var 1) (op (var 0) (var 1))) (var 2))) , (var 2)) → ⊥
  cut3365  adequate = bad3365  (Adequate.valid adequate Two boolean env8)
  bad3366 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b0 (bop b0 b0)) b0)) b1 → ⊥
  bad3366  p = false≢true (cong lower p)
  cut3366 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (op (var 1) (op (var 0) (var 1))) (var 2))) , (var 3)) → ⊥
  cut3366  adequate = bad3366  (Adequate.valid adequate Two boolean env4)
  holds3367 : (z0 z1 z2 : A2) → (mul2 (mul2 z0 z0) (mul2 (mul2 z1 (mul2 z0 z2)) z0)) ≡ z0
  holds3367 z0 z1 z2 = refl
  cut3367 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (op (var 1) (op (var 0) (var 2))) (var 0))) , (var 0)) → ⊥
  cut3367  = reject2 ((op (op (var 0) (var 0)) (op (op (var 1) (op (var 0) (var 2))) (var 0))) , (var 0)) (λ env → holds3367 (env 0) (env 1) (env 2))
  bad3368 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b1 (bop b0 b0)) b0)) b1 → ⊥
  bad3368  p = false≢true (cong lower p)
  cut3368 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (op (var 1) (op (var 0) (var 2))) (var 0))) , (var 1)) → ⊥
  cut3368  adequate = bad3368  (Adequate.valid adequate Two boolean env5)
  bad3369 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b0 (bop b0 b1)) b0)) b1 → ⊥
  bad3369  p = false≢true (cong lower p)
  cut3369 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (op (var 1) (op (var 0) (var 2))) (var 0))) , (var 2)) → ⊥
  cut3369  adequate = bad3369  (Adequate.valid adequate Two boolean env2)
  bad3370 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b0 (bop b0 b0)) b0)) b1 → ⊥
  bad3370  p = false≢true (cong lower p)
  cut3370 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (op (var 1) (op (var 0) (var 2))) (var 0))) , (var 3)) → ⊥
  cut3370  adequate = bad3370  (Adequate.valid adequate Two boolean env4)
  holds3371 : (z0 z1 z2 : A2) → (mul2 (mul2 z0 z0) (mul2 (mul2 z1 (mul2 z0 z2)) z1)) ≡ z0
  holds3371 z0 z1 z2 = refl
  cut3371 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (op (var 1) (op (var 0) (var 2))) (var 1))) , (var 0)) → ⊥
  cut3371  = reject2 ((op (op (var 0) (var 0)) (op (op (var 1) (op (var 0) (var 2))) (var 1))) , (var 0)) (λ env → holds3371 (env 0) (env 1) (env 2))
  bad3372 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b1 (bop b0 b0)) b1)) b1 → ⊥
  bad3372  p = false≢true (cong lower p)
  cut3372 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (op (var 1) (op (var 0) (var 2))) (var 1))) , (var 1)) → ⊥
  cut3372  adequate = bad3372  (Adequate.valid adequate Two boolean env5)
  bad3373 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b0 (bop b0 b1)) b0)) b1 → ⊥
  bad3373  p = false≢true (cong lower p)
  cut3373 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (op (var 1) (op (var 0) (var 2))) (var 1))) , (var 2)) → ⊥
  cut3373  adequate = bad3373  (Adequate.valid adequate Two boolean env2)
  bad3374 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b0 (bop b0 b0)) b0)) b1 → ⊥
  bad3374  p = false≢true (cong lower p)
  cut3374 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (op (var 1) (op (var 0) (var 2))) (var 1))) , (var 3)) → ⊥
  cut3374  adequate = bad3374  (Adequate.valid adequate Two boolean env4)
  bad3375 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b0 (bop b0 b1)) b1)) b0 → ⊥
  bad3375  p = false≢true (sym (cong lower p))
  cut3375 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (op (var 1) (op (var 0) (var 2))) (var 2))) , (var 0)) → ⊥
  cut3375  adequate = bad3375  (Adequate.valid adequate Two boolean env2)
  bad3376 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b0 (bop b0 b1)) b1)) b0 → ⊥
  bad3376  p = false≢true (sym (cong lower p))
  cut3376 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (op (var 1) (op (var 0) (var 2))) (var 2))) , (var 1)) → ⊥
  cut3376  adequate = bad3376  (Adequate.valid adequate Two boolean env2)
  bad3377 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b1 (bop b0 b1)) b1)) b1 → ⊥
  bad3377  p = false≢true (cong lower p)
  cut3377 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (op (var 1) (op (var 0) (var 2))) (var 2))) , (var 2)) → ⊥
  cut3377  adequate = bad3377  (Adequate.valid adequate Two boolean env8)
  bad3378 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b0 (bop b0 b0)) b0)) b1 → ⊥
  bad3378  p = false≢true (cong lower p)
  cut3378 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (op (var 1) (op (var 0) (var 2))) (var 2))) , (var 3)) → ⊥
  cut3378  adequate = bad3378  (Adequate.valid adequate Two boolean env4)
  bad3379 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b0 (bop b0 b0)) b1)) b0 → ⊥
  bad3379  p = false≢true (sym (cong lower p))
  cut3379 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (op (var 1) (op (var 0) (var 2))) (var 3))) , (var 0)) → ⊥
  cut3379  adequate = bad3379  (Adequate.valid adequate Two boolean env4)
  bad3380 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b0 (bop b0 b0)) b1)) b0 → ⊥
  bad3380  p = false≢true (sym (cong lower p))
  cut3380 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (op (var 1) (op (var 0) (var 2))) (var 3))) , (var 1)) → ⊥
  cut3380  adequate = bad3380  (Adequate.valid adequate Two boolean env4)
  bad3381 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b0 (bop b0 b0)) b1)) b0 → ⊥
  bad3381  p = false≢true (sym (cong lower p))
  cut3381 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (op (var 1) (op (var 0) (var 2))) (var 3))) , (var 2)) → ⊥
  cut3381  adequate = bad3381  (Adequate.valid adequate Two boolean env4)
  env9 : ℕ → Two
  env9 zero = b0
  env9 (suc zero) = b1
  env9 (suc (suc zero)) = b0
  env9 (suc (suc (suc zero))) = b1
  env9 (suc (suc (suc (suc rest)))) = b0
  bad3382 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b1 (bop b0 b0)) b1)) b1 → ⊥
  bad3382  p = false≢true (cong lower p)
  cut3382 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (op (var 1) (op (var 0) (var 2))) (var 3))) , (var 3)) → ⊥
  cut3382  adequate = bad3382  (Adequate.valid adequate Two boolean env9)
  bad3383 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b0 (bop b0 b0)) b0)) b1 → ⊥
  bad3383  p = false≢true (cong lower p)
  cut3383 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (op (var 1) (op (var 0) (var 2))) (var 3))) , (var 4)) → ⊥
  cut3383  adequate = bad3383  (Adequate.valid adequate Two boolean env7)
  holds3384 : (z0 z1 : A2) → (mul2 (mul2 z0 z0) (mul2 (mul2 z1 (mul2 z1 z0)) z0)) ≡ z0
  holds3384 z0 z1 = refl
  cut3384 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (op (var 1) (op (var 1) (var 0))) (var 0))) , (var 0)) → ⊥
  cut3384  = reject2 ((op (op (var 0) (var 0)) (op (op (var 1) (op (var 1) (var 0))) (var 0))) , (var 0)) (λ env → holds3384 (env 0) (env 1))
  bad3385 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b1 (bop b1 b0)) b0)) b1 → ⊥
  bad3385  p = false≢true (cong lower p)
  cut3385 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (op (var 1) (op (var 1) (var 0))) (var 0))) , (var 1)) → ⊥
  cut3385  adequate = bad3385  (Adequate.valid adequate Two boolean env0)
  bad3386 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b0 (bop b0 b0)) b0)) b1 → ⊥
  bad3386  p = false≢true (cong lower p)
  cut3386 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (op (var 1) (op (var 1) (var 0))) (var 0))) , (var 2)) → ⊥
  cut3386  adequate = bad3386  (Adequate.valid adequate Two boolean env2)
  holds3387 : (z0 z1 : A2) → (mul2 (mul2 z0 z0) (mul2 (mul2 z1 (mul2 z1 z0)) z1)) ≡ z0
  holds3387 z0 z1 = refl
  cut3387 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (op (var 1) (op (var 1) (var 0))) (var 1))) , (var 0)) → ⊥
  cut3387  = reject2 ((op (op (var 0) (var 0)) (op (op (var 1) (op (var 1) (var 0))) (var 1))) , (var 0)) (λ env → holds3387 (env 0) (env 1))
  bad3388 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b1 (bop b1 b0)) b1)) b1 → ⊥
  bad3388  p = false≢true (cong lower p)
  cut3388 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (op (var 1) (op (var 1) (var 0))) (var 1))) , (var 1)) → ⊥
  cut3388  adequate = bad3388  (Adequate.valid adequate Two boolean env0)
  bad3389 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b0 (bop b0 b0)) b0)) b1 → ⊥
  bad3389  p = false≢true (cong lower p)
  cut3389 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (op (var 1) (op (var 1) (var 0))) (var 1))) , (var 2)) → ⊥
  cut3389  adequate = bad3389  (Adequate.valid adequate Two boolean env2)
  bad3390 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b0 (bop b0 b0)) b1)) b0 → ⊥
  bad3390  p = false≢true (sym (cong lower p))
  cut3390 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (op (var 1) (op (var 1) (var 0))) (var 2))) , (var 0)) → ⊥
  cut3390  adequate = bad3390  (Adequate.valid adequate Two boolean env2)
  bad3391 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b0 (bop b0 b0)) b1)) b0 → ⊥
  bad3391  p = false≢true (sym (cong lower p))
  cut3391 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (op (var 1) (op (var 1) (var 0))) (var 2))) , (var 1)) → ⊥
  cut3391  adequate = bad3391  (Adequate.valid adequate Two boolean env2)
  bad3392 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b1 (bop b1 b0)) b1)) b1 → ⊥
  bad3392  p = false≢true (cong lower p)
  cut3392 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (op (var 1) (op (var 1) (var 0))) (var 2))) , (var 2)) → ⊥
  cut3392  adequate = bad3392  (Adequate.valid adequate Two boolean env8)
  bad3393 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b0 (bop b0 b0)) b0)) b1 → ⊥
  bad3393  p = false≢true (cong lower p)
  cut3393 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (op (var 1) (op (var 1) (var 0))) (var 2))) , (var 3)) → ⊥
  cut3393  adequate = bad3393  (Adequate.valid adequate Two boolean env4)
  holds3394 : (z0 z1 : A2) → (mul2 (mul2 z0 z0) (mul2 (mul2 z1 (mul2 z1 z1)) z0)) ≡ z0
  holds3394 z0 z1 = refl
  cut3394 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (op (var 1) (op (var 1) (var 1))) (var 0))) , (var 0)) → ⊥
  cut3394  = reject2 ((op (op (var 0) (var 0)) (op (op (var 1) (op (var 1) (var 1))) (var 0))) , (var 0)) (λ env → holds3394 (env 0) (env 1))
  bad3395 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b1 (bop b1 b1)) b0)) b1 → ⊥
  bad3395  p = false≢true (cong lower p)
  cut3395 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (op (var 1) (op (var 1) (var 1))) (var 0))) , (var 1)) → ⊥
  cut3395  adequate = bad3395  (Adequate.valid adequate Two boolean env0)
  bad3396 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b0 (bop b0 b0)) b0)) b1 → ⊥
  bad3396  p = false≢true (cong lower p)
  cut3396 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (op (var 1) (op (var 1) (var 1))) (var 0))) , (var 2)) → ⊥
  cut3396  adequate = bad3396  (Adequate.valid adequate Two boolean env2)
  bad3397 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b1 (bop b1 b1)) b1)) b0 → ⊥
  bad3397  p = false≢true (sym (cong lower p))
  cut3397 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (op (var 1) (op (var 1) (var 1))) (var 1))) , (var 0)) → ⊥
  cut3397  adequate = bad3397  (Adequate.valid adequate Two boolean env0)
  bad3398 : PathP (λ _ → Two) (bop (bop b1 b1) (bop (bop b0 (bop b0 b0)) b0)) b0 → ⊥
  bad3398  p = false≢true (sym (cong lower p))
  cut3398 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (op (var 1) (op (var 1) (var 1))) (var 1))) , (var 1)) → ⊥
  cut3398  adequate = bad3398  (Adequate.valid adequate Two boolean env1)
  bad3399 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b0 (bop b0 b0)) b0)) b1 → ⊥
  bad3399  p = false≢true (cong lower p)
  cut3399 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (op (var 1) (op (var 1) (var 1))) (var 1))) , (var 2)) → ⊥
  cut3399  adequate = bad3399  (Adequate.valid adequate Two boolean env2)
  bad3400 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b0 (bop b0 b0)) b1)) b0 → ⊥
  bad3400  p = false≢true (sym (cong lower p))
  cut3400 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (op (var 1) (op (var 1) (var 1))) (var 2))) , (var 0)) → ⊥
  cut3400  adequate = bad3400  (Adequate.valid adequate Two boolean env2)
  bad3401 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b0 (bop b0 b0)) b1)) b0 → ⊥
  bad3401  p = false≢true (sym (cong lower p))
  cut3401 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (op (var 1) (op (var 1) (var 1))) (var 2))) , (var 1)) → ⊥
  cut3401  adequate = bad3401  (Adequate.valid adequate Two boolean env2)
  bad3402 : PathP (λ _ → Two) (bop (bop b1 b1) (bop (bop b0 (bop b0 b0)) b0)) b0 → ⊥
  bad3402  p = false≢true (sym (cong lower p))
  cut3402 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (op (var 1) (op (var 1) (var 1))) (var 2))) , (var 2)) → ⊥
  cut3402  adequate = bad3402  (Adequate.valid adequate Two boolean env3)
  bad3403 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b0 (bop b0 b0)) b0)) b1 → ⊥
  bad3403  p = false≢true (cong lower p)
  cut3403 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (op (var 1) (op (var 1) (var 1))) (var 2))) , (var 3)) → ⊥
  cut3403  adequate = bad3403  (Adequate.valid adequate Two boolean env4)
  holds3404 : (z0 z1 z2 : A2) → (mul2 (mul2 z0 z0) (mul2 (mul2 z1 (mul2 z1 z2)) z0)) ≡ z0
  holds3404 z0 z1 z2 = refl
  cut3404 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (op (var 1) (op (var 1) (var 2))) (var 0))) , (var 0)) → ⊥
  cut3404  = reject2 ((op (op (var 0) (var 0)) (op (op (var 1) (op (var 1) (var 2))) (var 0))) , (var 0)) (λ env → holds3404 (env 0) (env 1) (env 2))
  bad3405 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b1 (bop b1 b0)) b0)) b1 → ⊥
  bad3405  p = false≢true (cong lower p)
  cut3405 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (op (var 1) (op (var 1) (var 2))) (var 0))) , (var 1)) → ⊥
  cut3405  adequate = bad3405  (Adequate.valid adequate Two boolean env5)
  bad3406 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b0 (bop b0 b1)) b0)) b1 → ⊥
  bad3406  p = false≢true (cong lower p)
  cut3406 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (op (var 1) (op (var 1) (var 2))) (var 0))) , (var 2)) → ⊥
  cut3406  adequate = bad3406  (Adequate.valid adequate Two boolean env2)
  bad3407 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b0 (bop b0 b0)) b0)) b1 → ⊥
  bad3407  p = false≢true (cong lower p)
  cut3407 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (op (var 1) (op (var 1) (var 2))) (var 0))) , (var 3)) → ⊥
  cut3407  adequate = bad3407  (Adequate.valid adequate Two boolean env4)
  bad3408 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b1 (bop b1 b1)) b1)) b0 → ⊥
  bad3408  p = false≢true (sym (cong lower p))
  cut3408 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (op (var 1) (op (var 1) (var 2))) (var 1))) , (var 0)) → ⊥
  cut3408  adequate = bad3408  (Adequate.valid adequate Two boolean env8)
  bad3409 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b1 (bop b1 b0)) b1)) b1 → ⊥
  bad3409  p = false≢true (cong lower p)
  cut3409 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (op (var 1) (op (var 1) (var 2))) (var 1))) , (var 1)) → ⊥
  cut3409  adequate = bad3409  (Adequate.valid adequate Two boolean env5)
  bad3410 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b0 (bop b0 b1)) b0)) b1 → ⊥
  bad3410  p = false≢true (cong lower p)
  cut3410 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (op (var 1) (op (var 1) (var 2))) (var 1))) , (var 2)) → ⊥
  cut3410  adequate = bad3410  (Adequate.valid adequate Two boolean env2)
  bad3411 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b0 (bop b0 b0)) b0)) b1 → ⊥
  bad3411  p = false≢true (cong lower p)
  cut3411 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (op (var 1) (op (var 1) (var 2))) (var 1))) , (var 3)) → ⊥
  cut3411  adequate = bad3411  (Adequate.valid adequate Two boolean env4)
  bad3412 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b0 (bop b0 b1)) b1)) b0 → ⊥
  bad3412  p = false≢true (sym (cong lower p))
  cut3412 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (op (var 1) (op (var 1) (var 2))) (var 2))) , (var 0)) → ⊥
  cut3412  adequate = bad3412  (Adequate.valid adequate Two boolean env2)
  bad3413 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b0 (bop b0 b1)) b1)) b0 → ⊥
  bad3413  p = false≢true (sym (cong lower p))
  cut3413 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (op (var 1) (op (var 1) (var 2))) (var 2))) , (var 1)) → ⊥
  cut3413  adequate = bad3413  (Adequate.valid adequate Two boolean env2)
  bad3414 : PathP (λ _ → Two) (bop (bop b1 b1) (bop (bop b0 (bop b0 b0)) b0)) b0 → ⊥
  bad3414  p = false≢true (sym (cong lower p))
  cut3414 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (op (var 1) (op (var 1) (var 2))) (var 2))) , (var 2)) → ⊥
  cut3414  adequate = bad3414  (Adequate.valid adequate Two boolean env3)
  bad3415 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b0 (bop b0 b0)) b0)) b1 → ⊥
  bad3415  p = false≢true (cong lower p)
  cut3415 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (op (var 1) (op (var 1) (var 2))) (var 2))) , (var 3)) → ⊥
  cut3415  adequate = bad3415  (Adequate.valid adequate Two boolean env4)
  bad3416 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b0 (bop b0 b0)) b1)) b0 → ⊥
  bad3416  p = false≢true (sym (cong lower p))
  cut3416 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (op (var 1) (op (var 1) (var 2))) (var 3))) , (var 0)) → ⊥
  cut3416  adequate = bad3416  (Adequate.valid adequate Two boolean env4)
  bad3417 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b0 (bop b0 b0)) b1)) b0 → ⊥
  bad3417  p = false≢true (sym (cong lower p))
  cut3417 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (op (var 1) (op (var 1) (var 2))) (var 3))) , (var 1)) → ⊥
  cut3417  adequate = bad3417  (Adequate.valid adequate Two boolean env4)
  bad3418 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b0 (bop b0 b0)) b1)) b0 → ⊥
  bad3418  p = false≢true (sym (cong lower p))
  cut3418 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (op (var 1) (op (var 1) (var 2))) (var 3))) , (var 2)) → ⊥
  cut3418  adequate = bad3418  (Adequate.valid adequate Two boolean env4)
  bad3419 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b1 (bop b1 b0)) b1)) b1 → ⊥
  bad3419  p = false≢true (cong lower p)
  cut3419 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (op (var 1) (op (var 1) (var 2))) (var 3))) , (var 3)) → ⊥
  cut3419  adequate = bad3419  (Adequate.valid adequate Two boolean env9)
  bad3420 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b0 (bop b0 b0)) b0)) b1 → ⊥
  bad3420  p = false≢true (cong lower p)
  cut3420 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (op (var 1) (op (var 1) (var 2))) (var 3))) , (var 4)) → ⊥
  cut3420  adequate = bad3420  (Adequate.valid adequate Two boolean env7)
  holds3421 : (z0 z1 z2 : A2) → (mul2 (mul2 z0 z0) (mul2 (mul2 z1 (mul2 z2 z0)) z0)) ≡ z0
  holds3421 z0 z1 z2 = refl
  cut3421 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (op (var 1) (op (var 2) (var 0))) (var 0))) , (var 0)) → ⊥
  cut3421  = reject2 ((op (op (var 0) (var 0)) (op (op (var 1) (op (var 2) (var 0))) (var 0))) , (var 0)) (λ env → holds3421 (env 0) (env 1) (env 2))
  bad3422 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b1 (bop b0 b0)) b0)) b1 → ⊥
  bad3422  p = false≢true (cong lower p)
  cut3422 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (op (var 1) (op (var 2) (var 0))) (var 0))) , (var 1)) → ⊥
  cut3422  adequate = bad3422  (Adequate.valid adequate Two boolean env5)
  bad3423 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b0 (bop b1 b0)) b0)) b1 → ⊥
  bad3423  p = false≢true (cong lower p)
  cut3423 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (op (var 1) (op (var 2) (var 0))) (var 0))) , (var 2)) → ⊥
  cut3423  adequate = bad3423  (Adequate.valid adequate Two boolean env2)
  bad3424 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b0 (bop b0 b0)) b0)) b1 → ⊥
  bad3424  p = false≢true (cong lower p)
  cut3424 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (op (var 1) (op (var 2) (var 0))) (var 0))) , (var 3)) → ⊥
  cut3424  adequate = bad3424  (Adequate.valid adequate Two boolean env4)
  holds3425 : (z0 z1 z2 : A2) → (mul2 (mul2 z0 z0) (mul2 (mul2 z1 (mul2 z2 z0)) z1)) ≡ z0
  holds3425 z0 z1 z2 = refl
  cut3425 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (op (var 1) (op (var 2) (var 0))) (var 1))) , (var 0)) → ⊥
  cut3425  = reject2 ((op (op (var 0) (var 0)) (op (op (var 1) (op (var 2) (var 0))) (var 1))) , (var 0)) (λ env → holds3425 (env 0) (env 1) (env 2))
  bad3426 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b1 (bop b0 b0)) b1)) b1 → ⊥
  bad3426  p = false≢true (cong lower p)
  cut3426 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (op (var 1) (op (var 2) (var 0))) (var 1))) , (var 1)) → ⊥
  cut3426  adequate = bad3426  (Adequate.valid adequate Two boolean env5)
  bad3427 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b0 (bop b1 b0)) b0)) b1 → ⊥
  bad3427  p = false≢true (cong lower p)
  cut3427 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (op (var 1) (op (var 2) (var 0))) (var 1))) , (var 2)) → ⊥
  cut3427  adequate = bad3427  (Adequate.valid adequate Two boolean env2)
  bad3428 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b0 (bop b0 b0)) b0)) b1 → ⊥
  bad3428  p = false≢true (cong lower p)
  cut3428 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (op (var 1) (op (var 2) (var 0))) (var 1))) , (var 3)) → ⊥
  cut3428  adequate = bad3428  (Adequate.valid adequate Two boolean env4)
  bad3429 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b0 (bop b1 b0)) b1)) b0 → ⊥
  bad3429  p = false≢true (sym (cong lower p))
  cut3429 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (op (var 1) (op (var 2) (var 0))) (var 2))) , (var 0)) → ⊥
  cut3429  adequate = bad3429  (Adequate.valid adequate Two boolean env2)
  bad3430 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b0 (bop b1 b0)) b1)) b0 → ⊥
  bad3430  p = false≢true (sym (cong lower p))
  cut3430 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (op (var 1) (op (var 2) (var 0))) (var 2))) , (var 1)) → ⊥
  cut3430  adequate = bad3430  (Adequate.valid adequate Two boolean env2)
  bad3431 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b1 (bop b1 b0)) b1)) b1 → ⊥
  bad3431  p = false≢true (cong lower p)
  cut3431 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (op (var 1) (op (var 2) (var 0))) (var 2))) , (var 2)) → ⊥
  cut3431  adequate = bad3431  (Adequate.valid adequate Two boolean env8)
  bad3432 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b0 (bop b0 b0)) b0)) b1 → ⊥
  bad3432  p = false≢true (cong lower p)
  cut3432 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (op (var 1) (op (var 2) (var 0))) (var 2))) , (var 3)) → ⊥
  cut3432  adequate = bad3432  (Adequate.valid adequate Two boolean env4)
  bad3433 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b0 (bop b0 b0)) b1)) b0 → ⊥
  bad3433  p = false≢true (sym (cong lower p))
  cut3433 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (op (var 1) (op (var 2) (var 0))) (var 3))) , (var 0)) → ⊥
  cut3433  adequate = bad3433  (Adequate.valid adequate Two boolean env4)
  bad3434 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b0 (bop b0 b0)) b1)) b0 → ⊥
  bad3434  p = false≢true (sym (cong lower p))
  cut3434 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (op (var 1) (op (var 2) (var 0))) (var 3))) , (var 1)) → ⊥
  cut3434  adequate = bad3434  (Adequate.valid adequate Two boolean env4)
  bad3435 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b0 (bop b0 b0)) b1)) b0 → ⊥
  bad3435  p = false≢true (sym (cong lower p))
  cut3435 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (op (var 1) (op (var 2) (var 0))) (var 3))) , (var 2)) → ⊥
  cut3435  adequate = bad3435  (Adequate.valid adequate Two boolean env4)
  bad3436 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b1 (bop b0 b0)) b1)) b1 → ⊥
  bad3436  p = false≢true (cong lower p)
  cut3436 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (op (var 1) (op (var 2) (var 0))) (var 3))) , (var 3)) → ⊥
  cut3436  adequate = bad3436  (Adequate.valid adequate Two boolean env9)
  bad3437 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b0 (bop b0 b0)) b0)) b1 → ⊥
  bad3437  p = false≢true (cong lower p)
  cut3437 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (op (var 1) (op (var 2) (var 0))) (var 3))) , (var 4)) → ⊥
  cut3437  adequate = bad3437  (Adequate.valid adequate Two boolean env7)
  holds3438 : (z0 z1 z2 : A2) → (mul2 (mul2 z0 z0) (mul2 (mul2 z1 (mul2 z2 z1)) z0)) ≡ z0
  holds3438 z0 z1 z2 = refl
  cut3438 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (op (var 1) (op (var 2) (var 1))) (var 0))) , (var 0)) → ⊥
  cut3438  = reject2 ((op (op (var 0) (var 0)) (op (op (var 1) (op (var 2) (var 1))) (var 0))) , (var 0)) (λ env → holds3438 (env 0) (env 1) (env 2))
  bad3439 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b1 (bop b0 b1)) b0)) b1 → ⊥
  bad3439  p = false≢true (cong lower p)
  cut3439 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (op (var 1) (op (var 2) (var 1))) (var 0))) , (var 1)) → ⊥
  cut3439  adequate = bad3439  (Adequate.valid adequate Two boolean env5)
  bad3440 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b0 (bop b1 b0)) b0)) b1 → ⊥
  bad3440  p = false≢true (cong lower p)
  cut3440 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (op (var 1) (op (var 2) (var 1))) (var 0))) , (var 2)) → ⊥
  cut3440  adequate = bad3440  (Adequate.valid adequate Two boolean env2)
  bad3441 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b0 (bop b0 b0)) b0)) b1 → ⊥
  bad3441  p = false≢true (cong lower p)
  cut3441 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (op (var 1) (op (var 2) (var 1))) (var 0))) , (var 3)) → ⊥
  cut3441  adequate = bad3441  (Adequate.valid adequate Two boolean env4)
  bad3442 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b1 (bop b1 b1)) b1)) b0 → ⊥
  bad3442  p = false≢true (sym (cong lower p))
  cut3442 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (op (var 1) (op (var 2) (var 1))) (var 1))) , (var 0)) → ⊥
  cut3442  adequate = bad3442  (Adequate.valid adequate Two boolean env8)
  bad3443 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b1 (bop b0 b1)) b1)) b1 → ⊥
  bad3443  p = false≢true (cong lower p)
  cut3443 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (op (var 1) (op (var 2) (var 1))) (var 1))) , (var 1)) → ⊥
  cut3443  adequate = bad3443  (Adequate.valid adequate Two boolean env5)
  bad3444 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b0 (bop b1 b0)) b0)) b1 → ⊥
  bad3444  p = false≢true (cong lower p)
  cut3444 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (op (var 1) (op (var 2) (var 1))) (var 1))) , (var 2)) → ⊥
  cut3444  adequate = bad3444  (Adequate.valid adequate Two boolean env2)
  bad3445 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b0 (bop b0 b0)) b0)) b1 → ⊥
  bad3445  p = false≢true (cong lower p)
  cut3445 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (op (var 1) (op (var 2) (var 1))) (var 1))) , (var 3)) → ⊥
  cut3445  adequate = bad3445  (Adequate.valid adequate Two boolean env4)
  bad3446 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b0 (bop b1 b0)) b1)) b0 → ⊥
  bad3446  p = false≢true (sym (cong lower p))
  cut3446 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (op (var 1) (op (var 2) (var 1))) (var 2))) , (var 0)) → ⊥
  cut3446  adequate = bad3446  (Adequate.valid adequate Two boolean env2)
  bad3447 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b0 (bop b1 b0)) b1)) b0 → ⊥
  bad3447  p = false≢true (sym (cong lower p))
  cut3447 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (op (var 1) (op (var 2) (var 1))) (var 2))) , (var 1)) → ⊥
  cut3447  adequate = bad3447  (Adequate.valid adequate Two boolean env2)
  bad3448 : PathP (λ _ → Two) (bop (bop b1 b1) (bop (bop b0 (bop b0 b0)) b0)) b0 → ⊥
  bad3448  p = false≢true (sym (cong lower p))
  cut3448 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (op (var 1) (op (var 2) (var 1))) (var 2))) , (var 2)) → ⊥
  cut3448  adequate = bad3448  (Adequate.valid adequate Two boolean env3)
  bad3449 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b0 (bop b0 b0)) b0)) b1 → ⊥
  bad3449  p = false≢true (cong lower p)
  cut3449 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (op (var 1) (op (var 2) (var 1))) (var 2))) , (var 3)) → ⊥
  cut3449  adequate = bad3449  (Adequate.valid adequate Two boolean env4)
  bad3450 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b0 (bop b0 b0)) b1)) b0 → ⊥
  bad3450  p = false≢true (sym (cong lower p))
  cut3450 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (op (var 1) (op (var 2) (var 1))) (var 3))) , (var 0)) → ⊥
  cut3450  adequate = bad3450  (Adequate.valid adequate Two boolean env4)
  bad3451 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b0 (bop b0 b0)) b1)) b0 → ⊥
  bad3451  p = false≢true (sym (cong lower p))
  cut3451 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (op (var 1) (op (var 2) (var 1))) (var 3))) , (var 1)) → ⊥
  cut3451  adequate = bad3451  (Adequate.valid adequate Two boolean env4)
  bad3452 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b0 (bop b0 b0)) b1)) b0 → ⊥
  bad3452  p = false≢true (sym (cong lower p))
  cut3452 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (op (var 1) (op (var 2) (var 1))) (var 3))) , (var 2)) → ⊥
  cut3452  adequate = bad3452  (Adequate.valid adequate Two boolean env4)
  bad3453 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b1 (bop b0 b1)) b1)) b1 → ⊥
  bad3453  p = false≢true (cong lower p)
  cut3453 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (op (var 1) (op (var 2) (var 1))) (var 3))) , (var 3)) → ⊥
  cut3453  adequate = bad3453  (Adequate.valid adequate Two boolean env9)
  bad3454 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b0 (bop b0 b0)) b0)) b1 → ⊥
  bad3454  p = false≢true (cong lower p)
  cut3454 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (op (var 1) (op (var 2) (var 1))) (var 3))) , (var 4)) → ⊥
  cut3454  adequate = bad3454  (Adequate.valid adequate Two boolean env7)
  holds3455 : (z0 z1 z2 : A2) → (mul2 (mul2 z0 z0) (mul2 (mul2 z1 (mul2 z2 z2)) z0)) ≡ z0
  holds3455 z0 z1 z2 = refl
  cut3455 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (op (var 1) (op (var 2) (var 2))) (var 0))) , (var 0)) → ⊥
  cut3455  = reject2 ((op (op (var 0) (var 0)) (op (op (var 1) (op (var 2) (var 2))) (var 0))) , (var 0)) (λ env → holds3455 (env 0) (env 1) (env 2))
  bad3456 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b1 (bop b0 b0)) b0)) b1 → ⊥
  bad3456  p = false≢true (cong lower p)
  cut3456 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (op (var 1) (op (var 2) (var 2))) (var 0))) , (var 1)) → ⊥
  cut3456  adequate = bad3456  (Adequate.valid adequate Two boolean env5)
  bad3457 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b0 (bop b1 b1)) b0)) b1 → ⊥
  bad3457  p = false≢true (cong lower p)
  cut3457 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (op (var 1) (op (var 2) (var 2))) (var 0))) , (var 2)) → ⊥
  cut3457  adequate = bad3457  (Adequate.valid adequate Two boolean env2)
  bad3458 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b0 (bop b0 b0)) b0)) b1 → ⊥
  bad3458  p = false≢true (cong lower p)
  cut3458 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (op (var 1) (op (var 2) (var 2))) (var 0))) , (var 3)) → ⊥
  cut3458  adequate = bad3458  (Adequate.valid adequate Two boolean env4)
  bad3459 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b1 (bop b1 b1)) b1)) b0 → ⊥
  bad3459  p = false≢true (sym (cong lower p))
  cut3459 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (op (var 1) (op (var 2) (var 2))) (var 1))) , (var 0)) → ⊥
  cut3459  adequate = bad3459  (Adequate.valid adequate Two boolean env8)
  bad3460 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b1 (bop b0 b0)) b1)) b1 → ⊥
  bad3460  p = false≢true (cong lower p)
  cut3460 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (op (var 1) (op (var 2) (var 2))) (var 1))) , (var 1)) → ⊥
  cut3460  adequate = bad3460  (Adequate.valid adequate Two boolean env5)
  bad3461 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b0 (bop b1 b1)) b0)) b1 → ⊥
  bad3461  p = false≢true (cong lower p)
  cut3461 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (op (var 1) (op (var 2) (var 2))) (var 1))) , (var 2)) → ⊥
  cut3461  adequate = bad3461  (Adequate.valid adequate Two boolean env2)
  bad3462 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b0 (bop b0 b0)) b0)) b1 → ⊥
  bad3462  p = false≢true (cong lower p)
  cut3462 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (op (var 1) (op (var 2) (var 2))) (var 1))) , (var 3)) → ⊥
  cut3462  adequate = bad3462  (Adequate.valid adequate Two boolean env4)
  bad3463 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b0 (bop b1 b1)) b1)) b0 → ⊥
  bad3463  p = false≢true (sym (cong lower p))
  cut3463 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (op (var 1) (op (var 2) (var 2))) (var 2))) , (var 0)) → ⊥
  cut3463  adequate = bad3463  (Adequate.valid adequate Two boolean env2)
  bad3464 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b0 (bop b1 b1)) b1)) b0 → ⊥
  bad3464  p = false≢true (sym (cong lower p))
  cut3464 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (op (var 1) (op (var 2) (var 2))) (var 2))) , (var 1)) → ⊥
  cut3464  adequate = bad3464  (Adequate.valid adequate Two boolean env2)
  bad3465 : PathP (λ _ → Two) (bop (bop b1 b1) (bop (bop b0 (bop b0 b0)) b0)) b0 → ⊥
  bad3465  p = false≢true (sym (cong lower p))
  cut3465 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (op (var 1) (op (var 2) (var 2))) (var 2))) , (var 2)) → ⊥
  cut3465  adequate = bad3465  (Adequate.valid adequate Two boolean env3)
  bad3466 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b0 (bop b0 b0)) b0)) b1 → ⊥
  bad3466  p = false≢true (cong lower p)
  cut3466 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (op (var 1) (op (var 2) (var 2))) (var 2))) , (var 3)) → ⊥
  cut3466  adequate = bad3466  (Adequate.valid adequate Two boolean env4)
  bad3467 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b0 (bop b0 b0)) b1)) b0 → ⊥
  bad3467  p = false≢true (sym (cong lower p))
  cut3467 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (op (var 1) (op (var 2) (var 2))) (var 3))) , (var 0)) → ⊥
  cut3467  adequate = bad3467  (Adequate.valid adequate Two boolean env4)
  bad3468 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b0 (bop b0 b0)) b1)) b0 → ⊥
  bad3468  p = false≢true (sym (cong lower p))
  cut3468 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (op (var 1) (op (var 2) (var 2))) (var 3))) , (var 1)) → ⊥
  cut3468  adequate = bad3468  (Adequate.valid adequate Two boolean env4)
  bad3469 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b0 (bop b0 b0)) b1)) b0 → ⊥
  bad3469  p = false≢true (sym (cong lower p))
  cut3469 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (op (var 1) (op (var 2) (var 2))) (var 3))) , (var 2)) → ⊥
  cut3469  adequate = bad3469  (Adequate.valid adequate Two boolean env4)
  bad3470 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b1 (bop b0 b0)) b1)) b1 → ⊥
  bad3470  p = false≢true (cong lower p)
  cut3470 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (op (var 1) (op (var 2) (var 2))) (var 3))) , (var 3)) → ⊥
  cut3470  adequate = bad3470  (Adequate.valid adequate Two boolean env9)
  bad3471 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b0 (bop b0 b0)) b0)) b1 → ⊥
  bad3471  p = false≢true (cong lower p)
  cut3471 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (op (var 1) (op (var 2) (var 2))) (var 3))) , (var 4)) → ⊥
  cut3471  adequate = bad3471  (Adequate.valid adequate Two boolean env7)
  holds3472 : (z0 z1 z2 z3 : A2) → (mul2 (mul2 z0 z0) (mul2 (mul2 z1 (mul2 z2 z3)) z0)) ≡ z0
  holds3472 z0 z1 z2 z3 = refl
  cut3472 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (op (var 1) (op (var 2) (var 3))) (var 0))) , (var 0)) → ⊥
  cut3472  = reject2 ((op (op (var 0) (var 0)) (op (op (var 1) (op (var 2) (var 3))) (var 0))) , (var 0)) (λ env → holds3472 (env 0) (env 1) (env 2) (env 3))
  env10 : ℕ → Two
  env10 zero = b0
  env10 (suc zero) = b1
  env10 (suc (suc zero)) = b0
  env10 (suc (suc (suc zero))) = b0
  env10 (suc (suc (suc (suc rest)))) = b0
  bad3473 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b1 (bop b0 b0)) b0)) b1 → ⊥
  bad3473  p = false≢true (cong lower p)
  cut3473 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (op (var 1) (op (var 2) (var 3))) (var 0))) , (var 1)) → ⊥
  cut3473  adequate = bad3473  (Adequate.valid adequate Two boolean env10)
  env11 : ℕ → Two
  env11 zero = b0
  env11 (suc zero) = b0
  env11 (suc (suc zero)) = b1
  env11 (suc (suc (suc zero))) = b0
  env11 (suc (suc (suc (suc rest)))) = b0
  bad3474 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b0 (bop b1 b0)) b0)) b1 → ⊥
  bad3474  p = false≢true (cong lower p)
  cut3474 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (op (var 1) (op (var 2) (var 3))) (var 0))) , (var 2)) → ⊥
  cut3474  adequate = bad3474  (Adequate.valid adequate Two boolean env11)
  bad3475 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b0 (bop b0 b1)) b0)) b1 → ⊥
  bad3475  p = false≢true (cong lower p)
  cut3475 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (op (var 1) (op (var 2) (var 3))) (var 0))) , (var 3)) → ⊥
  cut3475  adequate = bad3475  (Adequate.valid adequate Two boolean env4)
  bad3476 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b0 (bop b0 b0)) b0)) b1 → ⊥
  bad3476  p = false≢true (cong lower p)
  cut3476 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (op (var 1) (op (var 2) (var 3))) (var 0))) , (var 4)) → ⊥
  cut3476  adequate = bad3476  (Adequate.valid adequate Two boolean env7)
  env12 : ℕ → Two
  env12 zero = b0
  env12 (suc zero) = b1
  env12 (suc (suc zero)) = b1
  env12 (suc (suc (suc zero))) = b1
  env12 (suc (suc (suc (suc rest)))) = b0
  bad3477 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b1 (bop b1 b1)) b1)) b0 → ⊥
  bad3477  p = false≢true (sym (cong lower p))
  cut3477 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (op (var 1) (op (var 2) (var 3))) (var 1))) , (var 0)) → ⊥
  cut3477  adequate = bad3477  (Adequate.valid adequate Two boolean env12)
  bad3478 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b1 (bop b0 b0)) b1)) b1 → ⊥
  bad3478  p = false≢true (cong lower p)
  cut3478 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (op (var 1) (op (var 2) (var 3))) (var 1))) , (var 1)) → ⊥
  cut3478  adequate = bad3478  (Adequate.valid adequate Two boolean env10)
  bad3479 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b0 (bop b1 b0)) b0)) b1 → ⊥
  bad3479  p = false≢true (cong lower p)
  cut3479 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (op (var 1) (op (var 2) (var 3))) (var 1))) , (var 2)) → ⊥
  cut3479  adequate = bad3479  (Adequate.valid adequate Two boolean env11)
  bad3480 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b0 (bop b0 b1)) b0)) b1 → ⊥
  bad3480  p = false≢true (cong lower p)
  cut3480 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (op (var 1) (op (var 2) (var 3))) (var 1))) , (var 3)) → ⊥
  cut3480  adequate = bad3480  (Adequate.valid adequate Two boolean env4)
  bad3481 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b0 (bop b0 b0)) b0)) b1 → ⊥
  bad3481  p = false≢true (cong lower p)
  cut3481 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (op (var 1) (op (var 2) (var 3))) (var 1))) , (var 4)) → ⊥
  cut3481  adequate = bad3481  (Adequate.valid adequate Two boolean env7)
  bad3482 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b0 (bop b1 b0)) b1)) b0 → ⊥
  bad3482  p = false≢true (sym (cong lower p))
  cut3482 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (op (var 1) (op (var 2) (var 3))) (var 2))) , (var 0)) → ⊥
  cut3482  adequate = bad3482  (Adequate.valid adequate Two boolean env11)
  bad3483 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b0 (bop b1 b0)) b1)) b0 → ⊥
  bad3483  p = false≢true (sym (cong lower p))
  cut3483 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (op (var 1) (op (var 2) (var 3))) (var 2))) , (var 1)) → ⊥
  cut3483  adequate = bad3483  (Adequate.valid adequate Two boolean env11)
  env13 : ℕ → Two
  env13 zero = b0
  env13 (suc zero) = b1
  env13 (suc (suc zero)) = b1
  env13 (suc (suc (suc zero))) = b0
  env13 (suc (suc (suc (suc rest)))) = b0
  bad3484 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b1 (bop b1 b0)) b1)) b1 → ⊥
  bad3484  p = false≢true (cong lower p)
  cut3484 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (op (var 1) (op (var 2) (var 3))) (var 2))) , (var 2)) → ⊥
  cut3484  adequate = bad3484  (Adequate.valid adequate Two boolean env13)
  bad3485 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b0 (bop b0 b1)) b0)) b1 → ⊥
  bad3485  p = false≢true (cong lower p)
  cut3485 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (op (var 1) (op (var 2) (var 3))) (var 2))) , (var 3)) → ⊥
  cut3485  adequate = bad3485  (Adequate.valid adequate Two boolean env4)
  bad3486 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b0 (bop b0 b0)) b0)) b1 → ⊥
  bad3486  p = false≢true (cong lower p)
  cut3486 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (op (var 1) (op (var 2) (var 3))) (var 2))) , (var 4)) → ⊥
  cut3486  adequate = bad3486  (Adequate.valid adequate Two boolean env7)
  bad3487 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b0 (bop b0 b1)) b1)) b0 → ⊥
  bad3487  p = false≢true (sym (cong lower p))
  cut3487 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (op (var 1) (op (var 2) (var 3))) (var 3))) , (var 0)) → ⊥
  cut3487  adequate = bad3487  (Adequate.valid adequate Two boolean env4)
  bad3488 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b0 (bop b0 b1)) b1)) b0 → ⊥
  bad3488  p = false≢true (sym (cong lower p))
  cut3488 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (op (var 1) (op (var 2) (var 3))) (var 3))) , (var 1)) → ⊥
  cut3488  adequate = bad3488  (Adequate.valid adequate Two boolean env4)
  bad3489 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b0 (bop b0 b1)) b1)) b0 → ⊥
  bad3489  p = false≢true (sym (cong lower p))
  cut3489 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (op (var 1) (op (var 2) (var 3))) (var 3))) , (var 2)) → ⊥
  cut3489  adequate = bad3489  (Adequate.valid adequate Two boolean env4)
  bad3490 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b1 (bop b0 b1)) b1)) b1 → ⊥
  bad3490  p = false≢true (cong lower p)
  cut3490 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (op (var 1) (op (var 2) (var 3))) (var 3))) , (var 3)) → ⊥
  cut3490  adequate = bad3490  (Adequate.valid adequate Two boolean env9)
  bad3491 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b0 (bop b0 b0)) b0)) b1 → ⊥
  bad3491  p = false≢true (cong lower p)
  cut3491 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (op (var 1) (op (var 2) (var 3))) (var 3))) , (var 4)) → ⊥
  cut3491  adequate = bad3491  (Adequate.valid adequate Two boolean env7)
  bad3492 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b0 (bop b0 b0)) b1)) b0 → ⊥
  bad3492  p = false≢true (sym (cong lower p))
  cut3492 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (op (var 1) (op (var 2) (var 3))) (var 4))) , (var 0)) → ⊥
  cut3492  adequate = bad3492  (Adequate.valid adequate Two boolean env7)
  bad3493 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b0 (bop b0 b0)) b1)) b0 → ⊥
  bad3493  p = false≢true (sym (cong lower p))
  cut3493 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (op (var 1) (op (var 2) (var 3))) (var 4))) , (var 1)) → ⊥
  cut3493  adequate = bad3493  (Adequate.valid adequate Two boolean env7)
  bad3494 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b0 (bop b0 b0)) b1)) b0 → ⊥
  bad3494  p = false≢true (sym (cong lower p))
  cut3494 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (op (var 1) (op (var 2) (var 3))) (var 4))) , (var 2)) → ⊥
  cut3494  adequate = bad3494  (Adequate.valid adequate Two boolean env7)
  bad3495 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b0 (bop b0 b0)) b1)) b0 → ⊥
  bad3495  p = false≢true (sym (cong lower p))
  cut3495 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (op (var 1) (op (var 2) (var 3))) (var 4))) , (var 3)) → ⊥
  cut3495  adequate = bad3495  (Adequate.valid adequate Two boolean env7)
  env14 : ℕ → Two
  env14 zero = b0
  env14 (suc zero) = b1
  env14 (suc (suc zero)) = b0
  env14 (suc (suc (suc zero))) = b0
  env14 (suc (suc (suc (suc zero)))) = b1
  env14 (suc (suc (suc (suc (suc rest))))) = b0
  bad3496 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b1 (bop b0 b0)) b1)) b1 → ⊥
  bad3496  p = false≢true (cong lower p)
  cut3496 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (op (var 1) (op (var 2) (var 3))) (var 4))) , (var 4)) → ⊥
  cut3496  adequate = bad3496  (Adequate.valid adequate Two boolean env14)
  env15 : ℕ → Two
  env15 zero = b0
  env15 (suc zero) = b0
  env15 (suc (suc zero)) = b0
  env15 (suc (suc (suc zero))) = b0
  env15 (suc (suc (suc (suc zero)))) = b0
  env15 (suc (suc (suc (suc (suc zero))))) = b1
  env15 (suc (suc (suc (suc (suc (suc rest)))))) = b0
  bad3497 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b0 (bop b0 b0)) b0)) b1 → ⊥
  bad3497  p = false≢true (cong lower p)
  cut3497 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (op (var 1) (op (var 2) (var 3))) (var 4))) , (var 5)) → ⊥
  cut3497  adequate = bad3497  (Adequate.valid adequate Two boolean env15)
  holds3498 : (z0 z1 : A2) → (mul2 (mul2 z0 z1) (mul2 (mul2 z0 (mul2 z0 z0)) z0)) ≡ z0
  holds3498 z0 z1 = refl
  cut3498 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 0) (op (var 0) (var 0))) (var 0))) , (var 0)) → ⊥
  cut3498  = reject2 ((op (op (var 0) (var 1)) (op (op (var 0) (op (var 0) (var 0))) (var 0))) , (var 0)) (λ env → holds3498 (env 0) (env 1))
  bad3499 : PathP (λ _ → Two) (bop (bop b0 b1) (bop (bop b0 (bop b0 b0)) b0)) b1 → ⊥
  bad3499  p = false≢true (cong lower p)
  cut3499 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 0) (op (var 0) (var 0))) (var 0))) , (var 1)) → ⊥
  cut3499  adequate = bad3499  (Adequate.valid adequate Two boolean env0)
  bad3500 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b0 (bop b0 b0)) b0)) b1 → ⊥
  bad3500  p = false≢true (cong lower p)
  cut3500 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 0) (op (var 0) (var 0))) (var 0))) , (var 2)) → ⊥
  cut3500  adequate = bad3500  (Adequate.valid adequate Two boolean env2)
  bad3501 : PathP (λ _ → Two) (bop (bop b0 b1) (bop (bop b0 (bop b0 b0)) b1)) b0 → ⊥
  bad3501  p = false≢true (sym (cong lower p))
  cut3501 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 0) (op (var 0) (var 0))) (var 1))) , (var 0)) → ⊥
  cut3501  adequate = bad3501  (Adequate.valid adequate Two boolean env0)
  holds3502 : (z0 z1 : A3) → (mul3 (mul3 z0 z1) (mul3 (mul3 z0 (mul3 z0 z0)) z1)) ≡ z1
  holds3502 z0 z1 = refl
  cut3502 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 0) (op (var 0) (var 0))) (var 1))) , (var 1)) → ⊥
  cut3502  = reject3 ((op (op (var 0) (var 1)) (op (op (var 0) (op (var 0) (var 0))) (var 1))) , (var 1)) (λ env → holds3502 (env 0) (env 1))
  bad3503 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b0 (bop b0 b0)) b0)) b1 → ⊥
  bad3503  p = false≢true (cong lower p)
  cut3503 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 0) (op (var 0) (var 0))) (var 1))) , (var 2)) → ⊥
  cut3503  adequate = bad3503  (Adequate.valid adequate Two boolean env2)
  bad3504 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b0 (bop b0 b0)) b1)) b0 → ⊥
  bad3504  p = false≢true (sym (cong lower p))
  cut3504 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 0) (op (var 0) (var 0))) (var 2))) , (var 0)) → ⊥
  cut3504  adequate = bad3504  (Adequate.valid adequate Two boolean env2)
  bad3505 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b0 (bop b0 b0)) b1)) b0 → ⊥
  bad3505  p = false≢true (sym (cong lower p))
  cut3505 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 0) (op (var 0) (var 0))) (var 2))) , (var 1)) → ⊥
  cut3505  adequate = bad3505  (Adequate.valid adequate Two boolean env2)
  env16 : ℕ → Two
  env16 zero = b1
  env16 (suc zero) = b1
  env16 (suc (suc zero)) = b0
  env16 (suc (suc (suc rest))) = b0
  bad3506 : PathP (λ _ → Two) (bop (bop b1 b1) (bop (bop b1 (bop b1 b1)) b0)) b0 → ⊥
  bad3506  p = false≢true (sym (cong lower p))
  cut3506 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 0) (op (var 0) (var 0))) (var 2))) , (var 2)) → ⊥
  cut3506  adequate = bad3506  (Adequate.valid adequate Two boolean env16)
  bad3507 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b0 (bop b0 b0)) b0)) b1 → ⊥
  bad3507  p = false≢true (cong lower p)
  cut3507 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 0) (op (var 0) (var 0))) (var 2))) , (var 3)) → ⊥
  cut3507  adequate = bad3507  (Adequate.valid adequate Two boolean env4)
  bad3508 : PathP (λ _ → Two) (bop (bop b1 b0) (bop (bop b1 (bop b1 b0)) b1)) b1 → ⊥
  bad3508  p = false≢true (cong lower p)
  cut3508 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 0) (op (var 0) (var 1))) (var 0))) , (var 0)) → ⊥
  cut3508  adequate = bad3508  (Adequate.valid adequate Two boolean env1)
  bad3509 : PathP (λ _ → Two) (bop (bop b0 b1) (bop (bop b0 (bop b0 b1)) b0)) b1 → ⊥
  bad3509  p = false≢true (cong lower p)
  cut3509 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 0) (op (var 0) (var 1))) (var 0))) , (var 1)) → ⊥
  cut3509  adequate = bad3509  (Adequate.valid adequate Two boolean env0)
  bad3510 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b0 (bop b0 b0)) b0)) b1 → ⊥
  bad3510  p = false≢true (cong lower p)
  cut3510 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 0) (op (var 0) (var 1))) (var 0))) , (var 2)) → ⊥
  cut3510  adequate = bad3510  (Adequate.valid adequate Two boolean env2)
  bad3511 : PathP (λ _ → Two) (bop (bop b0 b1) (bop (bop b0 (bop b0 b1)) b1)) b0 → ⊥
  bad3511  p = false≢true (sym (cong lower p))
  cut3511 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 0) (op (var 0) (var 1))) (var 1))) , (var 0)) → ⊥
  cut3511  adequate = bad3511  (Adequate.valid adequate Two boolean env0)
  holds3512 : (z0 z1 : A3) → (mul3 (mul3 z0 z1) (mul3 (mul3 z0 (mul3 z0 z1)) z1)) ≡ z1
  holds3512 z0 z1 = refl
  cut3512 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 0) (op (var 0) (var 1))) (var 1))) , (var 1)) → ⊥
  cut3512  = reject3 ((op (op (var 0) (var 1)) (op (op (var 0) (op (var 0) (var 1))) (var 1))) , (var 1)) (λ env → holds3512 (env 0) (env 1))
  bad3513 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b0 (bop b0 b0)) b0)) b1 → ⊥
  bad3513  p = false≢true (cong lower p)
  cut3513 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 0) (op (var 0) (var 1))) (var 1))) , (var 2)) → ⊥
  cut3513  adequate = bad3513  (Adequate.valid adequate Two boolean env2)
  bad3514 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b0 (bop b0 b0)) b1)) b0 → ⊥
  bad3514  p = false≢true (sym (cong lower p))
  cut3514 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 0) (op (var 0) (var 1))) (var 2))) , (var 0)) → ⊥
  cut3514  adequate = bad3514  (Adequate.valid adequate Two boolean env2)
  bad3515 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b0 (bop b0 b0)) b1)) b0 → ⊥
  bad3515  p = false≢true (sym (cong lower p))
  cut3515 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 0) (op (var 0) (var 1))) (var 2))) , (var 1)) → ⊥
  cut3515  adequate = bad3515  (Adequate.valid adequate Two boolean env2)
  env17 : ℕ → Two
  env17 zero = b1
  env17 (suc zero) = b0
  env17 (suc (suc zero)) = b1
  env17 (suc (suc (suc rest))) = b0
  bad3516 : PathP (λ _ → Two) (bop (bop b1 b0) (bop (bop b1 (bop b1 b0)) b1)) b1 → ⊥
  bad3516  p = false≢true (cong lower p)
  cut3516 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 0) (op (var 0) (var 1))) (var 2))) , (var 2)) → ⊥
  cut3516  adequate = bad3516  (Adequate.valid adequate Two boolean env17)
  bad3517 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b0 (bop b0 b0)) b0)) b1 → ⊥
  bad3517  p = false≢true (cong lower p)
  cut3517 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 0) (op (var 0) (var 1))) (var 2))) , (var 3)) → ⊥
  cut3517  adequate = bad3517  (Adequate.valid adequate Two boolean env4)
  bad3518 : PathP (λ _ → Two) (bop (bop b1 b0) (bop (bop b1 (bop b1 b0)) b1)) b1 → ⊥
  bad3518  p = false≢true (cong lower p)
  cut3518 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 0) (op (var 0) (var 2))) (var 0))) , (var 0)) → ⊥
  cut3518  adequate = bad3518  (Adequate.valid adequate Two boolean env3)
  bad3519 : PathP (λ _ → Two) (bop (bop b0 b1) (bop (bop b0 (bop b0 b0)) b0)) b1 → ⊥
  bad3519  p = false≢true (cong lower p)
  cut3519 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 0) (op (var 0) (var 2))) (var 0))) , (var 1)) → ⊥
  cut3519  adequate = bad3519  (Adequate.valid adequate Two boolean env5)
  bad3520 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b0 (bop b0 b1)) b0)) b1 → ⊥
  bad3520  p = false≢true (cong lower p)
  cut3520 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 0) (op (var 0) (var 2))) (var 0))) , (var 2)) → ⊥
  cut3520  adequate = bad3520  (Adequate.valid adequate Two boolean env2)
  bad3521 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b0 (bop b0 b0)) b0)) b1 → ⊥
  bad3521  p = false≢true (cong lower p)
  cut3521 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 0) (op (var 0) (var 2))) (var 0))) , (var 3)) → ⊥
  cut3521  adequate = bad3521  (Adequate.valid adequate Two boolean env4)
  bad3522 : PathP (λ _ → Two) (bop (bop b0 b1) (bop (bop b0 (bop b0 b0)) b1)) b0 → ⊥
  bad3522  p = false≢true (sym (cong lower p))
  cut3522 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 0) (op (var 0) (var 2))) (var 1))) , (var 0)) → ⊥
  cut3522  adequate = bad3522  (Adequate.valid adequate Two boolean env5)
  holds3523 : (z0 z1 z2 : A3) → (mul3 (mul3 z0 z1) (mul3 (mul3 z0 (mul3 z0 z2)) z1)) ≡ z1
  holds3523 z0 z1 z2 = refl
  cut3523 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 0) (op (var 0) (var 2))) (var 1))) , (var 1)) → ⊥
  cut3523  = reject3 ((op (op (var 0) (var 1)) (op (op (var 0) (op (var 0) (var 2))) (var 1))) , (var 1)) (λ env → holds3523 (env 0) (env 1) (env 2))
  bad3524 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b0 (bop b0 b1)) b0)) b1 → ⊥
  bad3524  p = false≢true (cong lower p)
  cut3524 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 0) (op (var 0) (var 2))) (var 1))) , (var 2)) → ⊥
  cut3524  adequate = bad3524  (Adequate.valid adequate Two boolean env2)
  bad3525 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b0 (bop b0 b0)) b0)) b1 → ⊥
  bad3525  p = false≢true (cong lower p)
  cut3525 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 0) (op (var 0) (var 2))) (var 1))) , (var 3)) → ⊥
  cut3525  adequate = bad3525  (Adequate.valid adequate Two boolean env4)
  bad3526 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b0 (bop b0 b1)) b1)) b0 → ⊥
  bad3526  p = false≢true (sym (cong lower p))
  cut3526 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 0) (op (var 0) (var 2))) (var 2))) , (var 0)) → ⊥
  cut3526  adequate = bad3526  (Adequate.valid adequate Two boolean env2)
  bad3527 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b0 (bop b0 b1)) b1)) b0 → ⊥
  bad3527  p = false≢true (sym (cong lower p))
  cut3527 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 0) (op (var 0) (var 2))) (var 2))) , (var 1)) → ⊥
  cut3527  adequate = bad3527  (Adequate.valid adequate Two boolean env2)
  bad3528 : PathP (λ _ → Two) (bop (bop b1 b1) (bop (bop b1 (bop b1 b0)) b0)) b0 → ⊥
  bad3528  p = false≢true (sym (cong lower p))
  cut3528 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 0) (op (var 0) (var 2))) (var 2))) , (var 2)) → ⊥
  cut3528  adequate = bad3528  (Adequate.valid adequate Two boolean env16)
  bad3529 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b0 (bop b0 b0)) b0)) b1 → ⊥
  bad3529  p = false≢true (cong lower p)
  cut3529 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 0) (op (var 0) (var 2))) (var 2))) , (var 3)) → ⊥
  cut3529  adequate = bad3529  (Adequate.valid adequate Two boolean env4)
  bad3530 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b0 (bop b0 b0)) b1)) b0 → ⊥
  bad3530  p = false≢true (sym (cong lower p))
  cut3530 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 0) (op (var 0) (var 2))) (var 3))) , (var 0)) → ⊥
  cut3530  adequate = bad3530  (Adequate.valid adequate Two boolean env4)
  bad3531 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b0 (bop b0 b0)) b1)) b0 → ⊥
  bad3531  p = false≢true (sym (cong lower p))
  cut3531 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 0) (op (var 0) (var 2))) (var 3))) , (var 1)) → ⊥
  cut3531  adequate = bad3531  (Adequate.valid adequate Two boolean env4)
  bad3532 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b0 (bop b0 b0)) b1)) b0 → ⊥
  bad3532  p = false≢true (sym (cong lower p))
  cut3532 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 0) (op (var 0) (var 2))) (var 3))) , (var 2)) → ⊥
  cut3532  adequate = bad3532  (Adequate.valid adequate Two boolean env4)
  env18 : ℕ → Two
  env18 zero = b1
  env18 (suc zero) = b0
  env18 (suc (suc zero)) = b0
  env18 (suc (suc (suc zero))) = b1
  env18 (suc (suc (suc (suc rest)))) = b0
  bad3533 : PathP (λ _ → Two) (bop (bop b1 b0) (bop (bop b1 (bop b1 b0)) b1)) b1 → ⊥
  bad3533  p = false≢true (cong lower p)
  cut3533 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 0) (op (var 0) (var 2))) (var 3))) , (var 3)) → ⊥
  cut3533  adequate = bad3533  (Adequate.valid adequate Two boolean env18)
  bad3534 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b0 (bop b0 b0)) b0)) b1 → ⊥
  bad3534  p = false≢true (cong lower p)
  cut3534 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 0) (op (var 0) (var 2))) (var 3))) , (var 4)) → ⊥
  cut3534  adequate = bad3534  (Adequate.valid adequate Two boolean env7)
  bad3535 : PathP (λ _ → Two) (bop (bop b1 b0) (bop (bop b1 (bop b0 b1)) b1)) b1 → ⊥
  bad3535  p = false≢true (cong lower p)
  cut3535 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 0) (op (var 1) (var 0))) (var 0))) , (var 0)) → ⊥
  cut3535  adequate = bad3535  (Adequate.valid adequate Two boolean env1)
  bad3536 : PathP (λ _ → Two) (bop (bop b0 b1) (bop (bop b0 (bop b1 b0)) b0)) b1 → ⊥
  bad3536  p = false≢true (cong lower p)
  cut3536 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 0) (op (var 1) (var 0))) (var 0))) , (var 1)) → ⊥
  cut3536  adequate = bad3536  (Adequate.valid adequate Two boolean env0)
  bad3537 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b0 (bop b0 b0)) b0)) b1 → ⊥
  bad3537  p = false≢true (cong lower p)
  cut3537 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 0) (op (var 1) (var 0))) (var 0))) , (var 2)) → ⊥
  cut3537  adequate = bad3537  (Adequate.valid adequate Two boolean env2)
  bad3538 : PathP (λ _ → Two) (bop (bop b0 b1) (bop (bop b0 (bop b1 b0)) b1)) b0 → ⊥
  bad3538  p = false≢true (sym (cong lower p))
  cut3538 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 0) (op (var 1) (var 0))) (var 1))) , (var 0)) → ⊥
  cut3538  adequate = bad3538  (Adequate.valid adequate Two boolean env0)
  holds3539 : (z0 z1 : A3) → (mul3 (mul3 z0 z1) (mul3 (mul3 z0 (mul3 z1 z0)) z1)) ≡ z1
  holds3539 z0 z1 = refl
  cut3539 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 0) (op (var 1) (var 0))) (var 1))) , (var 1)) → ⊥
  cut3539  = reject3 ((op (op (var 0) (var 1)) (op (op (var 0) (op (var 1) (var 0))) (var 1))) , (var 1)) (λ env → holds3539 (env 0) (env 1))
  bad3540 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b0 (bop b0 b0)) b0)) b1 → ⊥
  bad3540  p = false≢true (cong lower p)
  cut3540 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 0) (op (var 1) (var 0))) (var 1))) , (var 2)) → ⊥
  cut3540  adequate = bad3540  (Adequate.valid adequate Two boolean env2)
  bad3541 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b0 (bop b0 b0)) b1)) b0 → ⊥
  bad3541  p = false≢true (sym (cong lower p))
  cut3541 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 0) (op (var 1) (var 0))) (var 2))) , (var 0)) → ⊥
  cut3541  adequate = bad3541  (Adequate.valid adequate Two boolean env2)
  bad3542 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b0 (bop b0 b0)) b1)) b0 → ⊥
  bad3542  p = false≢true (sym (cong lower p))
  cut3542 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 0) (op (var 1) (var 0))) (var 2))) , (var 1)) → ⊥
  cut3542  adequate = bad3542  (Adequate.valid adequate Two boolean env2)
  bad3543 : PathP (λ _ → Two) (bop (bop b1 b0) (bop (bop b1 (bop b0 b1)) b1)) b1 → ⊥
  bad3543  p = false≢true (cong lower p)
  cut3543 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 0) (op (var 1) (var 0))) (var 2))) , (var 2)) → ⊥
  cut3543  adequate = bad3543  (Adequate.valid adequate Two boolean env17)
  bad3544 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b0 (bop b0 b0)) b0)) b1 → ⊥
  bad3544  p = false≢true (cong lower p)
  cut3544 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 0) (op (var 1) (var 0))) (var 2))) , (var 3)) → ⊥
  cut3544  adequate = bad3544  (Adequate.valid adequate Two boolean env4)
  bad3545 : PathP (λ _ → Two) (bop (bop b1 b0) (bop (bop b1 (bop b0 b0)) b1)) b1 → ⊥
  bad3545  p = false≢true (cong lower p)
  cut3545 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 0) (op (var 1) (var 1))) (var 0))) , (var 0)) → ⊥
  cut3545  adequate = bad3545  (Adequate.valid adequate Two boolean env1)
  bad3546 : PathP (λ _ → Two) (bop (bop b0 b1) (bop (bop b0 (bop b1 b1)) b0)) b1 → ⊥
  bad3546  p = false≢true (cong lower p)
  cut3546 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 0) (op (var 1) (var 1))) (var 0))) , (var 1)) → ⊥
  cut3546  adequate = bad3546  (Adequate.valid adequate Two boolean env0)
  bad3547 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b0 (bop b0 b0)) b0)) b1 → ⊥
  bad3547  p = false≢true (cong lower p)
  cut3547 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 0) (op (var 1) (var 1))) (var 0))) , (var 2)) → ⊥
  cut3547  adequate = bad3547  (Adequate.valid adequate Two boolean env2)
  bad3548 : PathP (λ _ → Two) (bop (bop b0 b1) (bop (bop b0 (bop b1 b1)) b1)) b0 → ⊥
  bad3548  p = false≢true (sym (cong lower p))
  cut3548 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 0) (op (var 1) (var 1))) (var 1))) , (var 0)) → ⊥
  cut3548  adequate = bad3548  (Adequate.valid adequate Two boolean env0)
  holds3549 : (z0 z1 : A3) → (mul3 (mul3 z0 z1) (mul3 (mul3 z0 (mul3 z1 z1)) z1)) ≡ z1
  holds3549 z0 z1 = refl
  cut3549 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 0) (op (var 1) (var 1))) (var 1))) , (var 1)) → ⊥
  cut3549  = reject3 ((op (op (var 0) (var 1)) (op (op (var 0) (op (var 1) (var 1))) (var 1))) , (var 1)) (λ env → holds3549 (env 0) (env 1))
  bad3550 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b0 (bop b0 b0)) b0)) b1 → ⊥
  bad3550  p = false≢true (cong lower p)
  cut3550 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 0) (op (var 1) (var 1))) (var 1))) , (var 2)) → ⊥
  cut3550  adequate = bad3550  (Adequate.valid adequate Two boolean env2)
  bad3551 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b0 (bop b0 b0)) b1)) b0 → ⊥
  bad3551  p = false≢true (sym (cong lower p))
  cut3551 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 0) (op (var 1) (var 1))) (var 2))) , (var 0)) → ⊥
  cut3551  adequate = bad3551  (Adequate.valid adequate Two boolean env2)
  bad3552 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b0 (bop b0 b0)) b1)) b0 → ⊥
  bad3552  p = false≢true (sym (cong lower p))
  cut3552 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 0) (op (var 1) (var 1))) (var 2))) , (var 1)) → ⊥
  cut3552  adequate = bad3552  (Adequate.valid adequate Two boolean env2)
  bad3553 : PathP (λ _ → Two) (bop (bop b1 b0) (bop (bop b1 (bop b0 b0)) b1)) b1 → ⊥
  bad3553  p = false≢true (cong lower p)
  cut3553 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 0) (op (var 1) (var 1))) (var 2))) , (var 2)) → ⊥
  cut3553  adequate = bad3553  (Adequate.valid adequate Two boolean env17)
  bad3554 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b0 (bop b0 b0)) b0)) b1 → ⊥
  bad3554  p = false≢true (cong lower p)
  cut3554 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 0) (op (var 1) (var 1))) (var 2))) , (var 3)) → ⊥
  cut3554  adequate = bad3554  (Adequate.valid adequate Two boolean env4)
  bad3555 : PathP (λ _ → Two) (bop (bop b1 b0) (bop (bop b1 (bop b0 b0)) b1)) b1 → ⊥
  bad3555  p = false≢true (cong lower p)
  cut3555 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 0) (op (var 1) (var 2))) (var 0))) , (var 0)) → ⊥
  cut3555  adequate = bad3555  (Adequate.valid adequate Two boolean env3)
  bad3556 : PathP (λ _ → Two) (bop (bop b0 b1) (bop (bop b0 (bop b1 b0)) b0)) b1 → ⊥
  bad3556  p = false≢true (cong lower p)
  cut3556 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 0) (op (var 1) (var 2))) (var 0))) , (var 1)) → ⊥
  cut3556  adequate = bad3556  (Adequate.valid adequate Two boolean env5)
  bad3557 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b0 (bop b0 b1)) b0)) b1 → ⊥
  bad3557  p = false≢true (cong lower p)
  cut3557 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 0) (op (var 1) (var 2))) (var 0))) , (var 2)) → ⊥
  cut3557  adequate = bad3557  (Adequate.valid adequate Two boolean env2)
  bad3558 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b0 (bop b0 b0)) b0)) b1 → ⊥
  bad3558  p = false≢true (cong lower p)
  cut3558 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 0) (op (var 1) (var 2))) (var 0))) , (var 3)) → ⊥
  cut3558  adequate = bad3558  (Adequate.valid adequate Two boolean env4)
  bad3559 : PathP (λ _ → Two) (bop (bop b0 b1) (bop (bop b0 (bop b1 b0)) b1)) b0 → ⊥
  bad3559  p = false≢true (sym (cong lower p))
  cut3559 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 0) (op (var 1) (var 2))) (var 1))) , (var 0)) → ⊥
  cut3559  adequate = bad3559  (Adequate.valid adequate Two boolean env5)
  holds3560 : (z0 z1 z2 : A3) → (mul3 (mul3 z0 z1) (mul3 (mul3 z0 (mul3 z1 z2)) z1)) ≡ z1
  holds3560 z0 z1 z2 = refl
  cut3560 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 0) (op (var 1) (var 2))) (var 1))) , (var 1)) → ⊥
  cut3560  = reject3 ((op (op (var 0) (var 1)) (op (op (var 0) (op (var 1) (var 2))) (var 1))) , (var 1)) (λ env → holds3560 (env 0) (env 1) (env 2))
  bad3561 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b0 (bop b0 b1)) b0)) b1 → ⊥
  bad3561  p = false≢true (cong lower p)
  cut3561 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 0) (op (var 1) (var 2))) (var 1))) , (var 2)) → ⊥
  cut3561  adequate = bad3561  (Adequate.valid adequate Two boolean env2)
  bad3562 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b0 (bop b0 b0)) b0)) b1 → ⊥
  bad3562  p = false≢true (cong lower p)
  cut3562 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 0) (op (var 1) (var 2))) (var 1))) , (var 3)) → ⊥
  cut3562  adequate = bad3562  (Adequate.valid adequate Two boolean env4)
  bad3563 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b0 (bop b0 b1)) b1)) b0 → ⊥
  bad3563  p = false≢true (sym (cong lower p))
  cut3563 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 0) (op (var 1) (var 2))) (var 2))) , (var 0)) → ⊥
  cut3563  adequate = bad3563  (Adequate.valid adequate Two boolean env2)
  bad3564 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b0 (bop b0 b1)) b1)) b0 → ⊥
  bad3564  p = false≢true (sym (cong lower p))
  cut3564 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 0) (op (var 1) (var 2))) (var 2))) , (var 1)) → ⊥
  cut3564  adequate = bad3564  (Adequate.valid adequate Two boolean env2)
  bad3565 : PathP (λ _ → Two) (bop (bop b1 b0) (bop (bop b1 (bop b0 b1)) b1)) b1 → ⊥
  bad3565  p = false≢true (cong lower p)
  cut3565 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 0) (op (var 1) (var 2))) (var 2))) , (var 2)) → ⊥
  cut3565  adequate = bad3565  (Adequate.valid adequate Two boolean env17)
  bad3566 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b0 (bop b0 b0)) b0)) b1 → ⊥
  bad3566  p = false≢true (cong lower p)
  cut3566 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 0) (op (var 1) (var 2))) (var 2))) , (var 3)) → ⊥
  cut3566  adequate = bad3566  (Adequate.valid adequate Two boolean env4)
  bad3567 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b0 (bop b0 b0)) b1)) b0 → ⊥
  bad3567  p = false≢true (sym (cong lower p))
  cut3567 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 0) (op (var 1) (var 2))) (var 3))) , (var 0)) → ⊥
  cut3567  adequate = bad3567  (Adequate.valid adequate Two boolean env4)
  bad3568 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b0 (bop b0 b0)) b1)) b0 → ⊥
  bad3568  p = false≢true (sym (cong lower p))
  cut3568 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 0) (op (var 1) (var 2))) (var 3))) , (var 1)) → ⊥
  cut3568  adequate = bad3568  (Adequate.valid adequate Two boolean env4)
  bad3569 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b0 (bop b0 b0)) b1)) b0 → ⊥
  bad3569  p = false≢true (sym (cong lower p))
  cut3569 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 0) (op (var 1) (var 2))) (var 3))) , (var 2)) → ⊥
  cut3569  adequate = bad3569  (Adequate.valid adequate Two boolean env4)
  bad3570 : PathP (λ _ → Two) (bop (bop b1 b0) (bop (bop b1 (bop b0 b0)) b1)) b1 → ⊥
  bad3570  p = false≢true (cong lower p)
  cut3570 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 0) (op (var 1) (var 2))) (var 3))) , (var 3)) → ⊥
  cut3570  adequate = bad3570  (Adequate.valid adequate Two boolean env18)
  bad3571 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b0 (bop b0 b0)) b0)) b1 → ⊥
  bad3571  p = false≢true (cong lower p)
  cut3571 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 0) (op (var 1) (var 2))) (var 3))) , (var 4)) → ⊥
  cut3571  adequate = bad3571  (Adequate.valid adequate Two boolean env7)
  bad3572 : PathP (λ _ → Two) (bop (bop b1 b0) (bop (bop b1 (bop b0 b1)) b1)) b1 → ⊥
  bad3572  p = false≢true (cong lower p)
  cut3572 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 0) (op (var 2) (var 0))) (var 0))) , (var 0)) → ⊥
  cut3572  adequate = bad3572  (Adequate.valid adequate Two boolean env3)
  bad3573 : PathP (λ _ → Two) (bop (bop b0 b1) (bop (bop b0 (bop b0 b0)) b0)) b1 → ⊥
  bad3573  p = false≢true (cong lower p)
  cut3573 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 0) (op (var 2) (var 0))) (var 0))) , (var 1)) → ⊥
  cut3573  adequate = bad3573  (Adequate.valid adequate Two boolean env5)
  bad3574 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b0 (bop b1 b0)) b0)) b1 → ⊥
  bad3574  p = false≢true (cong lower p)
  cut3574 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 0) (op (var 2) (var 0))) (var 0))) , (var 2)) → ⊥
  cut3574  adequate = bad3574  (Adequate.valid adequate Two boolean env2)
  bad3575 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b0 (bop b0 b0)) b0)) b1 → ⊥
  bad3575  p = false≢true (cong lower p)
  cut3575 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 0) (op (var 2) (var 0))) (var 0))) , (var 3)) → ⊥
  cut3575  adequate = bad3575  (Adequate.valid adequate Two boolean env4)
  bad3576 : PathP (λ _ → Two) (bop (bop b0 b1) (bop (bop b0 (bop b0 b0)) b1)) b0 → ⊥
  bad3576  p = false≢true (sym (cong lower p))
  cut3576 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 0) (op (var 2) (var 0))) (var 1))) , (var 0)) → ⊥
  cut3576  adequate = bad3576  (Adequate.valid adequate Two boolean env5)
  holds3577 : (z0 z1 z2 : A3) → (mul3 (mul3 z0 z1) (mul3 (mul3 z0 (mul3 z2 z0)) z1)) ≡ z1
  holds3577 z0 z1 z2 = refl
  cut3577 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 0) (op (var 2) (var 0))) (var 1))) , (var 1)) → ⊥
  cut3577  = reject3 ((op (op (var 0) (var 1)) (op (op (var 0) (op (var 2) (var 0))) (var 1))) , (var 1)) (λ env → holds3577 (env 0) (env 1) (env 2))
  bad3578 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b0 (bop b1 b0)) b0)) b1 → ⊥
  bad3578  p = false≢true (cong lower p)
  cut3578 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 0) (op (var 2) (var 0))) (var 1))) , (var 2)) → ⊥
  cut3578  adequate = bad3578  (Adequate.valid adequate Two boolean env2)
  bad3579 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b0 (bop b0 b0)) b0)) b1 → ⊥
  bad3579  p = false≢true (cong lower p)
  cut3579 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 0) (op (var 2) (var 0))) (var 1))) , (var 3)) → ⊥
  cut3579  adequate = bad3579  (Adequate.valid adequate Two boolean env4)
  bad3580 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b0 (bop b1 b0)) b1)) b0 → ⊥
  bad3580  p = false≢true (sym (cong lower p))
  cut3580 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 0) (op (var 2) (var 0))) (var 2))) , (var 0)) → ⊥
  cut3580  adequate = bad3580  (Adequate.valid adequate Two boolean env2)
  bad3581 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b0 (bop b1 b0)) b1)) b0 → ⊥
  bad3581  p = false≢true (sym (cong lower p))
  cut3581 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 0) (op (var 2) (var 0))) (var 2))) , (var 1)) → ⊥
  cut3581  adequate = bad3581  (Adequate.valid adequate Two boolean env2)
  bad3582 : PathP (λ _ → Two) (bop (bop b1 b1) (bop (bop b1 (bop b0 b1)) b0)) b0 → ⊥
  bad3582  p = false≢true (sym (cong lower p))
  cut3582 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 0) (op (var 2) (var 0))) (var 2))) , (var 2)) → ⊥
  cut3582  adequate = bad3582  (Adequate.valid adequate Two boolean env16)
  bad3583 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b0 (bop b0 b0)) b0)) b1 → ⊥
  bad3583  p = false≢true (cong lower p)
  cut3583 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 0) (op (var 2) (var 0))) (var 2))) , (var 3)) → ⊥
  cut3583  adequate = bad3583  (Adequate.valid adequate Two boolean env4)
  bad3584 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b0 (bop b0 b0)) b1)) b0 → ⊥
  bad3584  p = false≢true (sym (cong lower p))
  cut3584 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 0) (op (var 2) (var 0))) (var 3))) , (var 0)) → ⊥
  cut3584  adequate = bad3584  (Adequate.valid adequate Two boolean env4)
  bad3585 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b0 (bop b0 b0)) b1)) b0 → ⊥
  bad3585  p = false≢true (sym (cong lower p))
  cut3585 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 0) (op (var 2) (var 0))) (var 3))) , (var 1)) → ⊥
  cut3585  adequate = bad3585  (Adequate.valid adequate Two boolean env4)
  bad3586 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b0 (bop b0 b0)) b1)) b0 → ⊥
  bad3586  p = false≢true (sym (cong lower p))
  cut3586 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 0) (op (var 2) (var 0))) (var 3))) , (var 2)) → ⊥
  cut3586  adequate = bad3586  (Adequate.valid adequate Two boolean env4)
  bad3587 : PathP (λ _ → Two) (bop (bop b1 b0) (bop (bop b1 (bop b0 b1)) b1)) b1 → ⊥
  bad3587  p = false≢true (cong lower p)
  cut3587 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 0) (op (var 2) (var 0))) (var 3))) , (var 3)) → ⊥
  cut3587  adequate = bad3587  (Adequate.valid adequate Two boolean env18)
  bad3588 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b0 (bop b0 b0)) b0)) b1 → ⊥
  bad3588  p = false≢true (cong lower p)
  cut3588 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 0) (op (var 2) (var 0))) (var 3))) , (var 4)) → ⊥
  cut3588  adequate = bad3588  (Adequate.valid adequate Two boolean env7)
  bad3589 : PathP (λ _ → Two) (bop (bop b1 b0) (bop (bop b1 (bop b0 b0)) b1)) b1 → ⊥
  bad3589  p = false≢true (cong lower p)
  cut3589 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 0) (op (var 2) (var 1))) (var 0))) , (var 0)) → ⊥
  cut3589  adequate = bad3589  (Adequate.valid adequate Two boolean env3)
  bad3590 : PathP (λ _ → Two) (bop (bop b0 b1) (bop (bop b0 (bop b0 b1)) b0)) b1 → ⊥
  bad3590  p = false≢true (cong lower p)
  cut3590 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 0) (op (var 2) (var 1))) (var 0))) , (var 1)) → ⊥
  cut3590  adequate = bad3590  (Adequate.valid adequate Two boolean env5)
  bad3591 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b0 (bop b1 b0)) b0)) b1 → ⊥
  bad3591  p = false≢true (cong lower p)
  cut3591 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 0) (op (var 2) (var 1))) (var 0))) , (var 2)) → ⊥
  cut3591  adequate = bad3591  (Adequate.valid adequate Two boolean env2)
  bad3592 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b0 (bop b0 b0)) b0)) b1 → ⊥
  bad3592  p = false≢true (cong lower p)
  cut3592 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 0) (op (var 2) (var 1))) (var 0))) , (var 3)) → ⊥
  cut3592  adequate = bad3592  (Adequate.valid adequate Two boolean env4)
  bad3593 : PathP (λ _ → Two) (bop (bop b0 b1) (bop (bop b0 (bop b0 b1)) b1)) b0 → ⊥
  bad3593  p = false≢true (sym (cong lower p))
  cut3593 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 0) (op (var 2) (var 1))) (var 1))) , (var 0)) → ⊥
  cut3593  adequate = bad3593  (Adequate.valid adequate Two boolean env5)
  holds3594 : (z0 z1 z2 : A3) → (mul3 (mul3 z0 z1) (mul3 (mul3 z0 (mul3 z2 z1)) z1)) ≡ z1
  holds3594 z0 z1 z2 = refl
  cut3594 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 0) (op (var 2) (var 1))) (var 1))) , (var 1)) → ⊥
  cut3594  = reject3 ((op (op (var 0) (var 1)) (op (op (var 0) (op (var 2) (var 1))) (var 1))) , (var 1)) (λ env → holds3594 (env 0) (env 1) (env 2))
  bad3595 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b0 (bop b1 b0)) b0)) b1 → ⊥
  bad3595  p = false≢true (cong lower p)
  cut3595 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 0) (op (var 2) (var 1))) (var 1))) , (var 2)) → ⊥
  cut3595  adequate = bad3595  (Adequate.valid adequate Two boolean env2)
  bad3596 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b0 (bop b0 b0)) b0)) b1 → ⊥
  bad3596  p = false≢true (cong lower p)
  cut3596 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 0) (op (var 2) (var 1))) (var 1))) , (var 3)) → ⊥
  cut3596  adequate = bad3596  (Adequate.valid adequate Two boolean env4)
  bad3597 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b0 (bop b1 b0)) b1)) b0 → ⊥
  bad3597  p = false≢true (sym (cong lower p))
  cut3597 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 0) (op (var 2) (var 1))) (var 2))) , (var 0)) → ⊥
  cut3597  adequate = bad3597  (Adequate.valid adequate Two boolean env2)
  bad3598 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b0 (bop b1 b0)) b1)) b0 → ⊥
  bad3598  p = false≢true (sym (cong lower p))
  cut3598 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 0) (op (var 2) (var 1))) (var 2))) , (var 1)) → ⊥
  cut3598  adequate = bad3598  (Adequate.valid adequate Two boolean env2)
  bad3599 : PathP (λ _ → Two) (bop (bop b1 b0) (bop (bop b1 (bop b1 b0)) b1)) b1 → ⊥
  bad3599  p = false≢true (cong lower p)
  cut3599 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 0) (op (var 2) (var 1))) (var 2))) , (var 2)) → ⊥
  cut3599  adequate = bad3599  (Adequate.valid adequate Two boolean env17)
  bad3600 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b0 (bop b0 b0)) b0)) b1 → ⊥
  bad3600  p = false≢true (cong lower p)
  cut3600 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 0) (op (var 2) (var 1))) (var 2))) , (var 3)) → ⊥
  cut3600  adequate = bad3600  (Adequate.valid adequate Two boolean env4)
  bad3601 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b0 (bop b0 b0)) b1)) b0 → ⊥
  bad3601  p = false≢true (sym (cong lower p))
  cut3601 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 0) (op (var 2) (var 1))) (var 3))) , (var 0)) → ⊥
  cut3601  adequate = bad3601  (Adequate.valid adequate Two boolean env4)
  bad3602 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b0 (bop b0 b0)) b1)) b0 → ⊥
  bad3602  p = false≢true (sym (cong lower p))
  cut3602 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 0) (op (var 2) (var 1))) (var 3))) , (var 1)) → ⊥
  cut3602  adequate = bad3602  (Adequate.valid adequate Two boolean env4)
  bad3603 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b0 (bop b0 b0)) b1)) b0 → ⊥
  bad3603  p = false≢true (sym (cong lower p))
  cut3603 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 0) (op (var 2) (var 1))) (var 3))) , (var 2)) → ⊥
  cut3603  adequate = bad3603  (Adequate.valid adequate Two boolean env4)
  bad3604 : PathP (λ _ → Two) (bop (bop b1 b0) (bop (bop b1 (bop b0 b0)) b1)) b1 → ⊥
  bad3604  p = false≢true (cong lower p)
  cut3604 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 0) (op (var 2) (var 1))) (var 3))) , (var 3)) → ⊥
  cut3604  adequate = bad3604  (Adequate.valid adequate Two boolean env18)
  bad3605 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b0 (bop b0 b0)) b0)) b1 → ⊥
  bad3605  p = false≢true (cong lower p)
  cut3605 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 0) (op (var 2) (var 1))) (var 3))) , (var 4)) → ⊥
  cut3605  adequate = bad3605  (Adequate.valid adequate Two boolean env7)
  bad3606 : PathP (λ _ → Two) (bop (bop b1 b0) (bop (bop b1 (bop b0 b0)) b1)) b1 → ⊥
  bad3606  p = false≢true (cong lower p)
  cut3606 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 0) (op (var 2) (var 2))) (var 0))) , (var 0)) → ⊥
  cut3606  adequate = bad3606  (Adequate.valid adequate Two boolean env3)
  bad3607 : PathP (λ _ → Two) (bop (bop b0 b1) (bop (bop b0 (bop b0 b0)) b0)) b1 → ⊥
  bad3607  p = false≢true (cong lower p)
  cut3607 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 0) (op (var 2) (var 2))) (var 0))) , (var 1)) → ⊥
  cut3607  adequate = bad3607  (Adequate.valid adequate Two boolean env5)
  bad3608 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b0 (bop b1 b1)) b0)) b1 → ⊥
  bad3608  p = false≢true (cong lower p)
  cut3608 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 0) (op (var 2) (var 2))) (var 0))) , (var 2)) → ⊥
  cut3608  adequate = bad3608  (Adequate.valid adequate Two boolean env2)
  bad3609 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b0 (bop b0 b0)) b0)) b1 → ⊥
  bad3609  p = false≢true (cong lower p)
  cut3609 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 0) (op (var 2) (var 2))) (var 0))) , (var 3)) → ⊥
  cut3609  adequate = bad3609  (Adequate.valid adequate Two boolean env4)
  bad3610 : PathP (λ _ → Two) (bop (bop b0 b1) (bop (bop b0 (bop b0 b0)) b1)) b0 → ⊥
  bad3610  p = false≢true (sym (cong lower p))
  cut3610 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 0) (op (var 2) (var 2))) (var 1))) , (var 0)) → ⊥
  cut3610  adequate = bad3610  (Adequate.valid adequate Two boolean env5)
  holds3611 : (z0 z1 z2 : A3) → (mul3 (mul3 z0 z1) (mul3 (mul3 z0 (mul3 z2 z2)) z1)) ≡ z1
  holds3611 z0 z1 z2 = refl
  cut3611 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 0) (op (var 2) (var 2))) (var 1))) , (var 1)) → ⊥
  cut3611  = reject3 ((op (op (var 0) (var 1)) (op (op (var 0) (op (var 2) (var 2))) (var 1))) , (var 1)) (λ env → holds3611 (env 0) (env 1) (env 2))
  bad3612 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b0 (bop b1 b1)) b0)) b1 → ⊥
  bad3612  p = false≢true (cong lower p)
  cut3612 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 0) (op (var 2) (var 2))) (var 1))) , (var 2)) → ⊥
  cut3612  adequate = bad3612  (Adequate.valid adequate Two boolean env2)
  bad3613 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b0 (bop b0 b0)) b0)) b1 → ⊥
  bad3613  p = false≢true (cong lower p)
  cut3613 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 0) (op (var 2) (var 2))) (var 1))) , (var 3)) → ⊥
  cut3613  adequate = bad3613  (Adequate.valid adequate Two boolean env4)
  bad3614 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b0 (bop b1 b1)) b1)) b0 → ⊥
  bad3614  p = false≢true (sym (cong lower p))
  cut3614 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 0) (op (var 2) (var 2))) (var 2))) , (var 0)) → ⊥
  cut3614  adequate = bad3614  (Adequate.valid adequate Two boolean env2)
  bad3615 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b0 (bop b1 b1)) b1)) b0 → ⊥
  bad3615  p = false≢true (sym (cong lower p))
  cut3615 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 0) (op (var 2) (var 2))) (var 2))) , (var 1)) → ⊥
  cut3615  adequate = bad3615  (Adequate.valid adequate Two boolean env2)
  bad3616 : PathP (λ _ → Two) (bop (bop b1 b1) (bop (bop b1 (bop b0 b0)) b0)) b0 → ⊥
  bad3616  p = false≢true (sym (cong lower p))
  cut3616 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 0) (op (var 2) (var 2))) (var 2))) , (var 2)) → ⊥
  cut3616  adequate = bad3616  (Adequate.valid adequate Two boolean env16)
  bad3617 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b0 (bop b0 b0)) b0)) b1 → ⊥
  bad3617  p = false≢true (cong lower p)
  cut3617 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 0) (op (var 2) (var 2))) (var 2))) , (var 3)) → ⊥
  cut3617  adequate = bad3617  (Adequate.valid adequate Two boolean env4)
  bad3618 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b0 (bop b0 b0)) b1)) b0 → ⊥
  bad3618  p = false≢true (sym (cong lower p))
  cut3618 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 0) (op (var 2) (var 2))) (var 3))) , (var 0)) → ⊥
  cut3618  adequate = bad3618  (Adequate.valid adequate Two boolean env4)
  bad3619 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b0 (bop b0 b0)) b1)) b0 → ⊥
  bad3619  p = false≢true (sym (cong lower p))
  cut3619 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 0) (op (var 2) (var 2))) (var 3))) , (var 1)) → ⊥
  cut3619  adequate = bad3619  (Adequate.valid adequate Two boolean env4)
  bad3620 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b0 (bop b0 b0)) b1)) b0 → ⊥
  bad3620  p = false≢true (sym (cong lower p))
  cut3620 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 0) (op (var 2) (var 2))) (var 3))) , (var 2)) → ⊥
  cut3620  adequate = bad3620  (Adequate.valid adequate Two boolean env4)
  bad3621 : PathP (λ _ → Two) (bop (bop b1 b0) (bop (bop b1 (bop b0 b0)) b1)) b1 → ⊥
  bad3621  p = false≢true (cong lower p)
  cut3621 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 0) (op (var 2) (var 2))) (var 3))) , (var 3)) → ⊥
  cut3621  adequate = bad3621  (Adequate.valid adequate Two boolean env18)
  bad3622 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b0 (bop b0 b0)) b0)) b1 → ⊥
  bad3622  p = false≢true (cong lower p)
  cut3622 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 0) (op (var 2) (var 2))) (var 3))) , (var 4)) → ⊥
  cut3622  adequate = bad3622  (Adequate.valid adequate Two boolean env7)
  bad3623 : PathP (λ _ → Two) (bop (bop b1 b0) (bop (bop b1 (bop b0 b0)) b1)) b1 → ⊥
  bad3623  p = false≢true (cong lower p)
  cut3623 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 0) (op (var 2) (var 3))) (var 0))) , (var 0)) → ⊥
  cut3623  adequate = bad3623  (Adequate.valid adequate Two boolean env6)
  bad3624 : PathP (λ _ → Two) (bop (bop b0 b1) (bop (bop b0 (bop b0 b0)) b0)) b1 → ⊥
  bad3624  p = false≢true (cong lower p)
  cut3624 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 0) (op (var 2) (var 3))) (var 0))) , (var 1)) → ⊥
  cut3624  adequate = bad3624  (Adequate.valid adequate Two boolean env10)
  bad3625 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b0 (bop b1 b0)) b0)) b1 → ⊥
  bad3625  p = false≢true (cong lower p)
  cut3625 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 0) (op (var 2) (var 3))) (var 0))) , (var 2)) → ⊥
  cut3625  adequate = bad3625  (Adequate.valid adequate Two boolean env11)
  bad3626 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b0 (bop b0 b1)) b0)) b1 → ⊥
  bad3626  p = false≢true (cong lower p)
  cut3626 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 0) (op (var 2) (var 3))) (var 0))) , (var 3)) → ⊥
  cut3626  adequate = bad3626  (Adequate.valid adequate Two boolean env4)
  bad3627 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b0 (bop b0 b0)) b0)) b1 → ⊥
  bad3627  p = false≢true (cong lower p)
  cut3627 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 0) (op (var 2) (var 3))) (var 0))) , (var 4)) → ⊥
  cut3627  adequate = bad3627  (Adequate.valid adequate Two boolean env7)
  bad3628 : PathP (λ _ → Two) (bop (bop b0 b1) (bop (bop b0 (bop b0 b0)) b1)) b0 → ⊥
  bad3628  p = false≢true (sym (cong lower p))
  cut3628 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 0) (op (var 2) (var 3))) (var 1))) , (var 0)) → ⊥
  cut3628  adequate = bad3628  (Adequate.valid adequate Two boolean env10)
  holds3629 : (z0 z1 z2 z3 : A3) → (mul3 (mul3 z0 z1) (mul3 (mul3 z0 (mul3 z2 z3)) z1)) ≡ z1
  holds3629 z0 z1 z2 z3 = refl
  cut3629 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 0) (op (var 2) (var 3))) (var 1))) , (var 1)) → ⊥
  cut3629  = reject3 ((op (op (var 0) (var 1)) (op (op (var 0) (op (var 2) (var 3))) (var 1))) , (var 1)) (λ env → holds3629 (env 0) (env 1) (env 2) (env 3))
  bad3630 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b0 (bop b1 b0)) b0)) b1 → ⊥
  bad3630  p = false≢true (cong lower p)
  cut3630 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 0) (op (var 2) (var 3))) (var 1))) , (var 2)) → ⊥
  cut3630  adequate = bad3630  (Adequate.valid adequate Two boolean env11)
  bad3631 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b0 (bop b0 b1)) b0)) b1 → ⊥
  bad3631  p = false≢true (cong lower p)
  cut3631 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 0) (op (var 2) (var 3))) (var 1))) , (var 3)) → ⊥
  cut3631  adequate = bad3631  (Adequate.valid adequate Two boolean env4)
  bad3632 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b0 (bop b0 b0)) b0)) b1 → ⊥
  bad3632  p = false≢true (cong lower p)
  cut3632 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 0) (op (var 2) (var 3))) (var 1))) , (var 4)) → ⊥
  cut3632  adequate = bad3632  (Adequate.valid adequate Two boolean env7)
  bad3633 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b0 (bop b1 b0)) b1)) b0 → ⊥
  bad3633  p = false≢true (sym (cong lower p))
  cut3633 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 0) (op (var 2) (var 3))) (var 2))) , (var 0)) → ⊥
  cut3633  adequate = bad3633  (Adequate.valid adequate Two boolean env11)
  bad3634 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b0 (bop b1 b0)) b1)) b0 → ⊥
  bad3634  p = false≢true (sym (cong lower p))
  cut3634 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 0) (op (var 2) (var 3))) (var 2))) , (var 1)) → ⊥
  cut3634  adequate = bad3634  (Adequate.valid adequate Two boolean env11)
  env19 : ℕ → Two
  env19 zero = b1
  env19 (suc zero) = b0
  env19 (suc (suc zero)) = b1
  env19 (suc (suc (suc zero))) = b0
  env19 (suc (suc (suc (suc rest)))) = b0
  bad3635 : PathP (λ _ → Two) (bop (bop b1 b0) (bop (bop b1 (bop b1 b0)) b1)) b1 → ⊥
  bad3635  p = false≢true (cong lower p)
  cut3635 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 0) (op (var 2) (var 3))) (var 2))) , (var 2)) → ⊥
  cut3635  adequate = bad3635  (Adequate.valid adequate Two boolean env19)
  bad3636 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b0 (bop b0 b1)) b0)) b1 → ⊥
  bad3636  p = false≢true (cong lower p)
  cut3636 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 0) (op (var 2) (var 3))) (var 2))) , (var 3)) → ⊥
  cut3636  adequate = bad3636  (Adequate.valid adequate Two boolean env4)
  bad3637 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b0 (bop b0 b0)) b0)) b1 → ⊥
  bad3637  p = false≢true (cong lower p)
  cut3637 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 0) (op (var 2) (var 3))) (var 2))) , (var 4)) → ⊥
  cut3637  adequate = bad3637  (Adequate.valid adequate Two boolean env7)
  bad3638 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b0 (bop b0 b1)) b1)) b0 → ⊥
  bad3638  p = false≢true (sym (cong lower p))
  cut3638 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 0) (op (var 2) (var 3))) (var 3))) , (var 0)) → ⊥
  cut3638  adequate = bad3638  (Adequate.valid adequate Two boolean env4)
  bad3639 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b0 (bop b0 b1)) b1)) b0 → ⊥
  bad3639  p = false≢true (sym (cong lower p))
  cut3639 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 0) (op (var 2) (var 3))) (var 3))) , (var 1)) → ⊥
  cut3639  adequate = bad3639  (Adequate.valid adequate Two boolean env4)
  bad3640 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b0 (bop b0 b1)) b1)) b0 → ⊥
  bad3640  p = false≢true (sym (cong lower p))
  cut3640 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 0) (op (var 2) (var 3))) (var 3))) , (var 2)) → ⊥
  cut3640  adequate = bad3640  (Adequate.valid adequate Two boolean env4)
  bad3641 : PathP (λ _ → Two) (bop (bop b1 b0) (bop (bop b1 (bop b0 b1)) b1)) b1 → ⊥
  bad3641  p = false≢true (cong lower p)
  cut3641 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 0) (op (var 2) (var 3))) (var 3))) , (var 3)) → ⊥
  cut3641  adequate = bad3641  (Adequate.valid adequate Two boolean env18)
  bad3642 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b0 (bop b0 b0)) b0)) b1 → ⊥
  bad3642  p = false≢true (cong lower p)
  cut3642 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 0) (op (var 2) (var 3))) (var 3))) , (var 4)) → ⊥
  cut3642  adequate = bad3642  (Adequate.valid adequate Two boolean env7)
  bad3643 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b0 (bop b0 b0)) b1)) b0 → ⊥
  bad3643  p = false≢true (sym (cong lower p))
  cut3643 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 0) (op (var 2) (var 3))) (var 4))) , (var 0)) → ⊥
  cut3643  adequate = bad3643  (Adequate.valid adequate Two boolean env7)
  bad3644 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b0 (bop b0 b0)) b1)) b0 → ⊥
  bad3644  p = false≢true (sym (cong lower p))
  cut3644 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 0) (op (var 2) (var 3))) (var 4))) , (var 1)) → ⊥
  cut3644  adequate = bad3644  (Adequate.valid adequate Two boolean env7)
  bad3645 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b0 (bop b0 b0)) b1)) b0 → ⊥
  bad3645  p = false≢true (sym (cong lower p))
  cut3645 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 0) (op (var 2) (var 3))) (var 4))) , (var 2)) → ⊥
  cut3645  adequate = bad3645  (Adequate.valid adequate Two boolean env7)
  bad3646 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b0 (bop b0 b0)) b1)) b0 → ⊥
  bad3646  p = false≢true (sym (cong lower p))
  cut3646 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 0) (op (var 2) (var 3))) (var 4))) , (var 3)) → ⊥
  cut3646  adequate = bad3646  (Adequate.valid adequate Two boolean env7)
  env20 : ℕ → Two
  env20 zero = b1
  env20 (suc zero) = b0
  env20 (suc (suc zero)) = b0
  env20 (suc (suc (suc zero))) = b0
  env20 (suc (suc (suc (suc zero)))) = b1
  env20 (suc (suc (suc (suc (suc rest))))) = b0
  bad3647 : PathP (λ _ → Two) (bop (bop b1 b0) (bop (bop b1 (bop b0 b0)) b1)) b1 → ⊥
  bad3647  p = false≢true (cong lower p)
  cut3647 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 0) (op (var 2) (var 3))) (var 4))) , (var 4)) → ⊥
  cut3647  adequate = bad3647  (Adequate.valid adequate Two boolean env20)
  bad3648 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b0 (bop b0 b0)) b0)) b1 → ⊥
  bad3648  p = false≢true (cong lower p)
  cut3648 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 0) (op (var 2) (var 3))) (var 4))) , (var 5)) → ⊥
  cut3648  adequate = bad3648  (Adequate.valid adequate Two boolean env15)
  holds3649 : (z0 z1 : A2) → (mul2 (mul2 z0 z1) (mul2 (mul2 z1 (mul2 z0 z0)) z0)) ≡ z0
  holds3649 z0 z1 = refl
  cut3649 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 1) (op (var 0) (var 0))) (var 0))) , (var 0)) → ⊥
  cut3649  = reject2 ((op (op (var 0) (var 1)) (op (op (var 1) (op (var 0) (var 0))) (var 0))) , (var 0)) (λ env → holds3649 (env 0) (env 1))
  bad3650 : PathP (λ _ → Two) (bop (bop b0 b1) (bop (bop b1 (bop b0 b0)) b0)) b1 → ⊥
  bad3650  p = false≢true (cong lower p)
  cut3650 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 1) (op (var 0) (var 0))) (var 0))) , (var 1)) → ⊥
  cut3650  adequate = bad3650  (Adequate.valid adequate Two boolean env0)
  bad3651 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b0 (bop b0 b0)) b0)) b1 → ⊥
  bad3651  p = false≢true (cong lower p)
  cut3651 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 1) (op (var 0) (var 0))) (var 0))) , (var 2)) → ⊥
  cut3651  adequate = bad3651  (Adequate.valid adequate Two boolean env2)
  bad3652 : PathP (λ _ → Two) (bop (bop b1 b0) (bop (bop b0 (bop b1 b1)) b0)) b1 → ⊥
  bad3652  p = false≢true (cong lower p)
  cut3652 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 1) (op (var 0) (var 0))) (var 1))) , (var 0)) → ⊥
  cut3652  adequate = bad3652  (Adequate.valid adequate Two boolean env1)
  bad3653 : PathP (λ _ → Two) (bop (bop b0 b1) (bop (bop b1 (bop b0 b0)) b1)) b1 → ⊥
  bad3653  p = false≢true (cong lower p)
  cut3653 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 1) (op (var 0) (var 0))) (var 1))) , (var 1)) → ⊥
  cut3653  adequate = bad3653  (Adequate.valid adequate Two boolean env0)
  bad3654 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b0 (bop b0 b0)) b0)) b1 → ⊥
  bad3654  p = false≢true (cong lower p)
  cut3654 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 1) (op (var 0) (var 0))) (var 1))) , (var 2)) → ⊥
  cut3654  adequate = bad3654  (Adequate.valid adequate Two boolean env2)
  bad3655 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b0 (bop b0 b0)) b1)) b0 → ⊥
  bad3655  p = false≢true (sym (cong lower p))
  cut3655 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 1) (op (var 0) (var 0))) (var 2))) , (var 0)) → ⊥
  cut3655  adequate = bad3655  (Adequate.valid adequate Two boolean env2)
  bad3656 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b0 (bop b0 b0)) b1)) b0 → ⊥
  bad3656  p = false≢true (sym (cong lower p))
  cut3656 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 1) (op (var 0) (var 0))) (var 2))) , (var 1)) → ⊥
  cut3656  adequate = bad3656  (Adequate.valid adequate Two boolean env2)
  bad3657 : PathP (λ _ → Two) (bop (bop b0 b1) (bop (bop b1 (bop b0 b0)) b1)) b1 → ⊥
  bad3657  p = false≢true (cong lower p)
  cut3657 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 1) (op (var 0) (var 0))) (var 2))) , (var 2)) → ⊥
  cut3657  adequate = bad3657  (Adequate.valid adequate Two boolean env8)
  bad3658 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b0 (bop b0 b0)) b0)) b1 → ⊥
  bad3658  p = false≢true (cong lower p)
  cut3658 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 1) (op (var 0) (var 0))) (var 2))) , (var 3)) → ⊥
  cut3658  adequate = bad3658  (Adequate.valid adequate Two boolean env4)
  holds3659 : (z0 z1 : A2) → (mul2 (mul2 z0 z1) (mul2 (mul2 z1 (mul2 z0 z1)) z0)) ≡ z0
  holds3659 z0 z1 = refl
  cut3659 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 1) (op (var 0) (var 1))) (var 0))) , (var 0)) → ⊥
  cut3659  = reject2 ((op (op (var 0) (var 1)) (op (op (var 1) (op (var 0) (var 1))) (var 0))) , (var 0)) (λ env → holds3659 (env 0) (env 1))
  bad3660 : PathP (λ _ → Two) (bop (bop b0 b1) (bop (bop b1 (bop b0 b1)) b0)) b1 → ⊥
  bad3660  p = false≢true (cong lower p)
  cut3660 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 1) (op (var 0) (var 1))) (var 0))) , (var 1)) → ⊥
  cut3660  adequate = bad3660  (Adequate.valid adequate Two boolean env0)
  bad3661 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b0 (bop b0 b0)) b0)) b1 → ⊥
  bad3661  p = false≢true (cong lower p)
  cut3661 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 1) (op (var 0) (var 1))) (var 0))) , (var 2)) → ⊥
  cut3661  adequate = bad3661  (Adequate.valid adequate Two boolean env2)
  bad3662 : PathP (λ _ → Two) (bop (bop b1 b0) (bop (bop b0 (bop b1 b0)) b0)) b1 → ⊥
  bad3662  p = false≢true (cong lower p)
  cut3662 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 1) (op (var 0) (var 1))) (var 1))) , (var 0)) → ⊥
  cut3662  adequate = bad3662  (Adequate.valid adequate Two boolean env1)
  bad3663 : PathP (λ _ → Two) (bop (bop b0 b1) (bop (bop b1 (bop b0 b1)) b1)) b1 → ⊥
  bad3663  p = false≢true (cong lower p)
  cut3663 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 1) (op (var 0) (var 1))) (var 1))) , (var 1)) → ⊥
  cut3663  adequate = bad3663  (Adequate.valid adequate Two boolean env0)
  bad3664 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b0 (bop b0 b0)) b0)) b1 → ⊥
  bad3664  p = false≢true (cong lower p)
  cut3664 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 1) (op (var 0) (var 1))) (var 1))) , (var 2)) → ⊥
  cut3664  adequate = bad3664  (Adequate.valid adequate Two boolean env2)
  bad3665 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b0 (bop b0 b0)) b1)) b0 → ⊥
  bad3665  p = false≢true (sym (cong lower p))
  cut3665 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 1) (op (var 0) (var 1))) (var 2))) , (var 0)) → ⊥
  cut3665  adequate = bad3665  (Adequate.valid adequate Two boolean env2)
  bad3666 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b0 (bop b0 b0)) b1)) b0 → ⊥
  bad3666  p = false≢true (sym (cong lower p))
  cut3666 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 1) (op (var 0) (var 1))) (var 2))) , (var 1)) → ⊥
  cut3666  adequate = bad3666  (Adequate.valid adequate Two boolean env2)
  bad3667 : PathP (λ _ → Two) (bop (bop b0 b1) (bop (bop b1 (bop b0 b1)) b1)) b1 → ⊥
  bad3667  p = false≢true (cong lower p)
  cut3667 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 1) (op (var 0) (var 1))) (var 2))) , (var 2)) → ⊥
  cut3667  adequate = bad3667  (Adequate.valid adequate Two boolean env8)
  bad3668 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b0 (bop b0 b0)) b0)) b1 → ⊥
  bad3668  p = false≢true (cong lower p)
  cut3668 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 1) (op (var 0) (var 1))) (var 2))) , (var 3)) → ⊥
  cut3668  adequate = bad3668  (Adequate.valid adequate Two boolean env4)
  holds3669 : (z0 z1 z2 : A2) → (mul2 (mul2 z0 z1) (mul2 (mul2 z1 (mul2 z0 z2)) z0)) ≡ z0
  holds3669 z0 z1 z2 = refl
  cut3669 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 1) (op (var 0) (var 2))) (var 0))) , (var 0)) → ⊥
  cut3669  = reject2 ((op (op (var 0) (var 1)) (op (op (var 1) (op (var 0) (var 2))) (var 0))) , (var 0)) (λ env → holds3669 (env 0) (env 1) (env 2))
  bad3670 : PathP (λ _ → Two) (bop (bop b0 b1) (bop (bop b1 (bop b0 b0)) b0)) b1 → ⊥
  bad3670  p = false≢true (cong lower p)
  cut3670 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 1) (op (var 0) (var 2))) (var 0))) , (var 1)) → ⊥
  cut3670  adequate = bad3670  (Adequate.valid adequate Two boolean env5)
  bad3671 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b0 (bop b0 b1)) b0)) b1 → ⊥
  bad3671  p = false≢true (cong lower p)
  cut3671 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 1) (op (var 0) (var 2))) (var 0))) , (var 2)) → ⊥
  cut3671  adequate = bad3671  (Adequate.valid adequate Two boolean env2)
  bad3672 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b0 (bop b0 b0)) b0)) b1 → ⊥
  bad3672  p = false≢true (cong lower p)
  cut3672 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 1) (op (var 0) (var 2))) (var 0))) , (var 3)) → ⊥
  cut3672  adequate = bad3672  (Adequate.valid adequate Two boolean env4)
  bad3673 : PathP (λ _ → Two) (bop (bop b1 b0) (bop (bop b0 (bop b1 b0)) b0)) b1 → ⊥
  bad3673  p = false≢true (cong lower p)
  cut3673 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 1) (op (var 0) (var 2))) (var 1))) , (var 0)) → ⊥
  cut3673  adequate = bad3673  (Adequate.valid adequate Two boolean env3)
  bad3674 : PathP (λ _ → Two) (bop (bop b0 b1) (bop (bop b1 (bop b0 b0)) b1)) b1 → ⊥
  bad3674  p = false≢true (cong lower p)
  cut3674 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 1) (op (var 0) (var 2))) (var 1))) , (var 1)) → ⊥
  cut3674  adequate = bad3674  (Adequate.valid adequate Two boolean env5)
  bad3675 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b0 (bop b0 b1)) b0)) b1 → ⊥
  bad3675  p = false≢true (cong lower p)
  cut3675 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 1) (op (var 0) (var 2))) (var 1))) , (var 2)) → ⊥
  cut3675  adequate = bad3675  (Adequate.valid adequate Two boolean env2)
  bad3676 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b0 (bop b0 b0)) b0)) b1 → ⊥
  bad3676  p = false≢true (cong lower p)
  cut3676 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 1) (op (var 0) (var 2))) (var 1))) , (var 3)) → ⊥
  cut3676  adequate = bad3676  (Adequate.valid adequate Two boolean env4)
  bad3677 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b0 (bop b0 b1)) b1)) b0 → ⊥
  bad3677  p = false≢true (sym (cong lower p))
  cut3677 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 1) (op (var 0) (var 2))) (var 2))) , (var 0)) → ⊥
  cut3677  adequate = bad3677  (Adequate.valid adequate Two boolean env2)
  bad3678 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b0 (bop b0 b1)) b1)) b0 → ⊥
  bad3678  p = false≢true (sym (cong lower p))
  cut3678 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 1) (op (var 0) (var 2))) (var 2))) , (var 1)) → ⊥
  cut3678  adequate = bad3678  (Adequate.valid adequate Two boolean env2)
  bad3679 : PathP (λ _ → Two) (bop (bop b0 b1) (bop (bop b1 (bop b0 b1)) b1)) b1 → ⊥
  bad3679  p = false≢true (cong lower p)
  cut3679 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 1) (op (var 0) (var 2))) (var 2))) , (var 2)) → ⊥
  cut3679  adequate = bad3679  (Adequate.valid adequate Two boolean env8)
  bad3680 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b0 (bop b0 b0)) b0)) b1 → ⊥
  bad3680  p = false≢true (cong lower p)
  cut3680 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 1) (op (var 0) (var 2))) (var 2))) , (var 3)) → ⊥
  cut3680  adequate = bad3680  (Adequate.valid adequate Two boolean env4)
  bad3681 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b0 (bop b0 b0)) b1)) b0 → ⊥
  bad3681  p = false≢true (sym (cong lower p))
  cut3681 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 1) (op (var 0) (var 2))) (var 3))) , (var 0)) → ⊥
  cut3681  adequate = bad3681  (Adequate.valid adequate Two boolean env4)
  bad3682 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b0 (bop b0 b0)) b1)) b0 → ⊥
  bad3682  p = false≢true (sym (cong lower p))
  cut3682 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 1) (op (var 0) (var 2))) (var 3))) , (var 1)) → ⊥
  cut3682  adequate = bad3682  (Adequate.valid adequate Two boolean env4)
  bad3683 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b0 (bop b0 b0)) b1)) b0 → ⊥
  bad3683  p = false≢true (sym (cong lower p))
  cut3683 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 1) (op (var 0) (var 2))) (var 3))) , (var 2)) → ⊥
  cut3683  adequate = bad3683  (Adequate.valid adequate Two boolean env4)
  bad3684 : PathP (λ _ → Two) (bop (bop b0 b1) (bop (bop b1 (bop b0 b0)) b1)) b1 → ⊥
  bad3684  p = false≢true (cong lower p)
  cut3684 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 1) (op (var 0) (var 2))) (var 3))) , (var 3)) → ⊥
  cut3684  adequate = bad3684  (Adequate.valid adequate Two boolean env9)
  bad3685 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b0 (bop b0 b0)) b0)) b1 → ⊥
  bad3685  p = false≢true (cong lower p)
  cut3685 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 1) (op (var 0) (var 2))) (var 3))) , (var 4)) → ⊥
  cut3685  adequate = bad3685  (Adequate.valid adequate Two boolean env7)
  holds3686 : (z0 z1 : A2) → (mul2 (mul2 z0 z1) (mul2 (mul2 z1 (mul2 z1 z0)) z0)) ≡ z0
  holds3686 z0 z1 = refl
  cut3686 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 1) (op (var 1) (var 0))) (var 0))) , (var 0)) → ⊥
  cut3686  = reject2 ((op (op (var 0) (var 1)) (op (op (var 1) (op (var 1) (var 0))) (var 0))) , (var 0)) (λ env → holds3686 (env 0) (env 1))
  bad3687 : PathP (λ _ → Two) (bop (bop b0 b1) (bop (bop b1 (bop b1 b0)) b0)) b1 → ⊥
  bad3687  p = false≢true (cong lower p)
  cut3687 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 1) (op (var 1) (var 0))) (var 0))) , (var 1)) → ⊥
  cut3687  adequate = bad3687  (Adequate.valid adequate Two boolean env0)
  bad3688 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b0 (bop b0 b0)) b0)) b1 → ⊥
  bad3688  p = false≢true (cong lower p)
  cut3688 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 1) (op (var 1) (var 0))) (var 0))) , (var 2)) → ⊥
  cut3688  adequate = bad3688  (Adequate.valid adequate Two boolean env2)
  bad3689 : PathP (λ _ → Two) (bop (bop b1 b0) (bop (bop b0 (bop b0 b1)) b0)) b1 → ⊥
  bad3689  p = false≢true (cong lower p)
  cut3689 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 1) (op (var 1) (var 0))) (var 1))) , (var 0)) → ⊥
  cut3689  adequate = bad3689  (Adequate.valid adequate Two boolean env1)
  bad3690 : PathP (λ _ → Two) (bop (bop b0 b1) (bop (bop b1 (bop b1 b0)) b1)) b1 → ⊥
  bad3690  p = false≢true (cong lower p)
  cut3690 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 1) (op (var 1) (var 0))) (var 1))) , (var 1)) → ⊥
  cut3690  adequate = bad3690  (Adequate.valid adequate Two boolean env0)
  bad3691 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b0 (bop b0 b0)) b0)) b1 → ⊥
  bad3691  p = false≢true (cong lower p)
  cut3691 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 1) (op (var 1) (var 0))) (var 1))) , (var 2)) → ⊥
  cut3691  adequate = bad3691  (Adequate.valid adequate Two boolean env2)
  bad3692 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b0 (bop b0 b0)) b1)) b0 → ⊥
  bad3692  p = false≢true (sym (cong lower p))
  cut3692 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 1) (op (var 1) (var 0))) (var 2))) , (var 0)) → ⊥
  cut3692  adequate = bad3692  (Adequate.valid adequate Two boolean env2)
  bad3693 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b0 (bop b0 b0)) b1)) b0 → ⊥
  bad3693  p = false≢true (sym (cong lower p))
  cut3693 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 1) (op (var 1) (var 0))) (var 2))) , (var 1)) → ⊥
  cut3693  adequate = bad3693  (Adequate.valid adequate Two boolean env2)
  bad3694 : PathP (λ _ → Two) (bop (bop b0 b1) (bop (bop b1 (bop b1 b0)) b1)) b1 → ⊥
  bad3694  p = false≢true (cong lower p)
  cut3694 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 1) (op (var 1) (var 0))) (var 2))) , (var 2)) → ⊥
  cut3694  adequate = bad3694  (Adequate.valid adequate Two boolean env8)
  bad3695 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b0 (bop b0 b0)) b0)) b1 → ⊥
  bad3695  p = false≢true (cong lower p)
  cut3695 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 1) (op (var 1) (var 0))) (var 2))) , (var 3)) → ⊥
  cut3695  adequate = bad3695  (Adequate.valid adequate Two boolean env4)
  holds3696 : (z0 z1 : A2) → (mul2 (mul2 z0 z1) (mul2 (mul2 z1 (mul2 z1 z1)) z0)) ≡ z0
  holds3696 z0 z1 = refl
  cut3696 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 1) (op (var 1) (var 1))) (var 0))) , (var 0)) → ⊥
  cut3696  = reject2 ((op (op (var 0) (var 1)) (op (op (var 1) (op (var 1) (var 1))) (var 0))) , (var 0)) (λ env → holds3696 (env 0) (env 1))
  bad3697 : PathP (λ _ → Two) (bop (bop b0 b1) (bop (bop b1 (bop b1 b1)) b0)) b1 → ⊥
  bad3697  p = false≢true (cong lower p)
  cut3697 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 1) (op (var 1) (var 1))) (var 0))) , (var 1)) → ⊥
  cut3697  adequate = bad3697  (Adequate.valid adequate Two boolean env0)
  bad3698 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b0 (bop b0 b0)) b0)) b1 → ⊥
  bad3698  p = false≢true (cong lower p)
  cut3698 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 1) (op (var 1) (var 1))) (var 0))) , (var 2)) → ⊥
  cut3698  adequate = bad3698  (Adequate.valid adequate Two boolean env2)
  bad3699 : PathP (λ _ → Two) (bop (bop b0 b1) (bop (bop b1 (bop b1 b1)) b1)) b0 → ⊥
  bad3699  p = false≢true (sym (cong lower p))
  cut3699 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 1) (op (var 1) (var 1))) (var 1))) , (var 0)) → ⊥
  cut3699  adequate = bad3699  (Adequate.valid adequate Two boolean env0)
  holds3700 : (z0 z1 : A3) → (mul3 (mul3 z0 z1) (mul3 (mul3 z1 (mul3 z1 z1)) z1)) ≡ z1
  holds3700 z0 z1 = refl
  cut3700 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 1) (op (var 1) (var 1))) (var 1))) , (var 1)) → ⊥
  cut3700  = reject3 ((op (op (var 0) (var 1)) (op (op (var 1) (op (var 1) (var 1))) (var 1))) , (var 1)) (λ env → holds3700 (env 0) (env 1))
  bad3701 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b0 (bop b0 b0)) b0)) b1 → ⊥
  bad3701  p = false≢true (cong lower p)
  cut3701 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 1) (op (var 1) (var 1))) (var 1))) , (var 2)) → ⊥
  cut3701  adequate = bad3701  (Adequate.valid adequate Two boolean env2)
  bad3702 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b0 (bop b0 b0)) b1)) b0 → ⊥
  bad3702  p = false≢true (sym (cong lower p))
  cut3702 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 1) (op (var 1) (var 1))) (var 2))) , (var 0)) → ⊥
  cut3702  adequate = bad3702  (Adequate.valid adequate Two boolean env2)
  bad3703 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b0 (bop b0 b0)) b1)) b0 → ⊥
  bad3703  p = false≢true (sym (cong lower p))
  cut3703 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 1) (op (var 1) (var 1))) (var 2))) , (var 1)) → ⊥
  cut3703  adequate = bad3703  (Adequate.valid adequate Two boolean env2)
  bad3704 : PathP (λ _ → Two) (bop (bop b1 b1) (bop (bop b1 (bop b1 b1)) b0)) b0 → ⊥
  bad3704  p = false≢true (sym (cong lower p))
  cut3704 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 1) (op (var 1) (var 1))) (var 2))) , (var 2)) → ⊥
  cut3704  adequate = bad3704  (Adequate.valid adequate Two boolean env16)
  bad3705 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b0 (bop b0 b0)) b0)) b1 → ⊥
  bad3705  p = false≢true (cong lower p)
  cut3705 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 1) (op (var 1) (var 1))) (var 2))) , (var 3)) → ⊥
  cut3705  adequate = bad3705  (Adequate.valid adequate Two boolean env4)
  holds3706 : (z0 z1 z2 : A2) → (mul2 (mul2 z0 z1) (mul2 (mul2 z1 (mul2 z1 z2)) z0)) ≡ z0
  holds3706 z0 z1 z2 = refl
  cut3706 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 1) (op (var 1) (var 2))) (var 0))) , (var 0)) → ⊥
  cut3706  = reject2 ((op (op (var 0) (var 1)) (op (op (var 1) (op (var 1) (var 2))) (var 0))) , (var 0)) (λ env → holds3706 (env 0) (env 1) (env 2))
  bad3707 : PathP (λ _ → Two) (bop (bop b0 b1) (bop (bop b1 (bop b1 b0)) b0)) b1 → ⊥
  bad3707  p = false≢true (cong lower p)
  cut3707 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 1) (op (var 1) (var 2))) (var 0))) , (var 1)) → ⊥
  cut3707  adequate = bad3707  (Adequate.valid adequate Two boolean env5)
  bad3708 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b0 (bop b0 b1)) b0)) b1 → ⊥
  bad3708  p = false≢true (cong lower p)
  cut3708 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 1) (op (var 1) (var 2))) (var 0))) , (var 2)) → ⊥
  cut3708  adequate = bad3708  (Adequate.valid adequate Two boolean env2)
  bad3709 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b0 (bop b0 b0)) b0)) b1 → ⊥
  bad3709  p = false≢true (cong lower p)
  cut3709 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 1) (op (var 1) (var 2))) (var 0))) , (var 3)) → ⊥
  cut3709  adequate = bad3709  (Adequate.valid adequate Two boolean env4)
  bad3710 : PathP (λ _ → Two) (bop (bop b0 b1) (bop (bop b1 (bop b1 b1)) b1)) b0 → ⊥
  bad3710  p = false≢true (sym (cong lower p))
  cut3710 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 1) (op (var 1) (var 2))) (var 1))) , (var 0)) → ⊥
  cut3710  adequate = bad3710  (Adequate.valid adequate Two boolean env8)
  bad3711 : PathP (λ _ → Two) (bop (bop b0 b1) (bop (bop b1 (bop b1 b0)) b1)) b1 → ⊥
  bad3711  p = false≢true (cong lower p)
  cut3711 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 1) (op (var 1) (var 2))) (var 1))) , (var 1)) → ⊥
  cut3711  adequate = bad3711  (Adequate.valid adequate Two boolean env5)
  bad3712 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b0 (bop b0 b1)) b0)) b1 → ⊥
  bad3712  p = false≢true (cong lower p)
  cut3712 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 1) (op (var 1) (var 2))) (var 1))) , (var 2)) → ⊥
  cut3712  adequate = bad3712  (Adequate.valid adequate Two boolean env2)
  bad3713 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b0 (bop b0 b0)) b0)) b1 → ⊥
  bad3713  p = false≢true (cong lower p)
  cut3713 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 1) (op (var 1) (var 2))) (var 1))) , (var 3)) → ⊥
  cut3713  adequate = bad3713  (Adequate.valid adequate Two boolean env4)
  bad3714 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b0 (bop b0 b1)) b1)) b0 → ⊥
  bad3714  p = false≢true (sym (cong lower p))
  cut3714 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 1) (op (var 1) (var 2))) (var 2))) , (var 0)) → ⊥
  cut3714  adequate = bad3714  (Adequate.valid adequate Two boolean env2)
  bad3715 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b0 (bop b0 b1)) b1)) b0 → ⊥
  bad3715  p = false≢true (sym (cong lower p))
  cut3715 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 1) (op (var 1) (var 2))) (var 2))) , (var 1)) → ⊥
  cut3715  adequate = bad3715  (Adequate.valid adequate Two boolean env2)
  bad3716 : PathP (λ _ → Two) (bop (bop b1 b1) (bop (bop b1 (bop b1 b0)) b0)) b0 → ⊥
  bad3716  p = false≢true (sym (cong lower p))
  cut3716 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 1) (op (var 1) (var 2))) (var 2))) , (var 2)) → ⊥
  cut3716  adequate = bad3716  (Adequate.valid adequate Two boolean env16)
  bad3717 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b0 (bop b0 b0)) b0)) b1 → ⊥
  bad3717  p = false≢true (cong lower p)
  cut3717 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 1) (op (var 1) (var 2))) (var 2))) , (var 3)) → ⊥
  cut3717  adequate = bad3717  (Adequate.valid adequate Two boolean env4)
  bad3718 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b0 (bop b0 b0)) b1)) b0 → ⊥
  bad3718  p = false≢true (sym (cong lower p))
  cut3718 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 1) (op (var 1) (var 2))) (var 3))) , (var 0)) → ⊥
  cut3718  adequate = bad3718  (Adequate.valid adequate Two boolean env4)
  bad3719 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b0 (bop b0 b0)) b1)) b0 → ⊥
  bad3719  p = false≢true (sym (cong lower p))
  cut3719 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 1) (op (var 1) (var 2))) (var 3))) , (var 1)) → ⊥
  cut3719  adequate = bad3719  (Adequate.valid adequate Two boolean env4)
  bad3720 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b0 (bop b0 b0)) b1)) b0 → ⊥
  bad3720  p = false≢true (sym (cong lower p))
  cut3720 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 1) (op (var 1) (var 2))) (var 3))) , (var 2)) → ⊥
  cut3720  adequate = bad3720  (Adequate.valid adequate Two boolean env4)
  bad3721 : PathP (λ _ → Two) (bop (bop b0 b1) (bop (bop b1 (bop b1 b0)) b1)) b1 → ⊥
  bad3721  p = false≢true (cong lower p)
  cut3721 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 1) (op (var 1) (var 2))) (var 3))) , (var 3)) → ⊥
  cut3721  adequate = bad3721  (Adequate.valid adequate Two boolean env9)
  bad3722 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b0 (bop b0 b0)) b0)) b1 → ⊥
  bad3722  p = false≢true (cong lower p)
  cut3722 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 1) (op (var 1) (var 2))) (var 3))) , (var 4)) → ⊥
  cut3722  adequate = bad3722  (Adequate.valid adequate Two boolean env7)
  holds3723 : (z0 z1 z2 : A2) → (mul2 (mul2 z0 z1) (mul2 (mul2 z1 (mul2 z2 z0)) z0)) ≡ z0
  holds3723 z0 z1 z2 = refl
  cut3723 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 1) (op (var 2) (var 0))) (var 0))) , (var 0)) → ⊥
  cut3723  = reject2 ((op (op (var 0) (var 1)) (op (op (var 1) (op (var 2) (var 0))) (var 0))) , (var 0)) (λ env → holds3723 (env 0) (env 1) (env 2))
  bad3724 : PathP (λ _ → Two) (bop (bop b0 b1) (bop (bop b1 (bop b0 b0)) b0)) b1 → ⊥
  bad3724  p = false≢true (cong lower p)
  cut3724 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 1) (op (var 2) (var 0))) (var 0))) , (var 1)) → ⊥
  cut3724  adequate = bad3724  (Adequate.valid adequate Two boolean env5)
  bad3725 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b0 (bop b1 b0)) b0)) b1 → ⊥
  bad3725  p = false≢true (cong lower p)
  cut3725 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 1) (op (var 2) (var 0))) (var 0))) , (var 2)) → ⊥
  cut3725  adequate = bad3725  (Adequate.valid adequate Two boolean env2)
  bad3726 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b0 (bop b0 b0)) b0)) b1 → ⊥
  bad3726  p = false≢true (cong lower p)
  cut3726 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 1) (op (var 2) (var 0))) (var 0))) , (var 3)) → ⊥
  cut3726  adequate = bad3726  (Adequate.valid adequate Two boolean env4)
  bad3727 : PathP (λ _ → Two) (bop (bop b1 b0) (bop (bop b0 (bop b0 b1)) b0)) b1 → ⊥
  bad3727  p = false≢true (cong lower p)
  cut3727 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 1) (op (var 2) (var 0))) (var 1))) , (var 0)) → ⊥
  cut3727  adequate = bad3727  (Adequate.valid adequate Two boolean env3)
  bad3728 : PathP (λ _ → Two) (bop (bop b0 b1) (bop (bop b1 (bop b0 b0)) b1)) b1 → ⊥
  bad3728  p = false≢true (cong lower p)
  cut3728 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 1) (op (var 2) (var 0))) (var 1))) , (var 1)) → ⊥
  cut3728  adequate = bad3728  (Adequate.valid adequate Two boolean env5)
  bad3729 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b0 (bop b1 b0)) b0)) b1 → ⊥
  bad3729  p = false≢true (cong lower p)
  cut3729 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 1) (op (var 2) (var 0))) (var 1))) , (var 2)) → ⊥
  cut3729  adequate = bad3729  (Adequate.valid adequate Two boolean env2)
  bad3730 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b0 (bop b0 b0)) b0)) b1 → ⊥
  bad3730  p = false≢true (cong lower p)
  cut3730 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 1) (op (var 2) (var 0))) (var 1))) , (var 3)) → ⊥
  cut3730  adequate = bad3730  (Adequate.valid adequate Two boolean env4)
  bad3731 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b0 (bop b1 b0)) b1)) b0 → ⊥
  bad3731  p = false≢true (sym (cong lower p))
  cut3731 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 1) (op (var 2) (var 0))) (var 2))) , (var 0)) → ⊥
  cut3731  adequate = bad3731  (Adequate.valid adequate Two boolean env2)
  bad3732 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b0 (bop b1 b0)) b1)) b0 → ⊥
  bad3732  p = false≢true (sym (cong lower p))
  cut3732 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 1) (op (var 2) (var 0))) (var 2))) , (var 1)) → ⊥
  cut3732  adequate = bad3732  (Adequate.valid adequate Two boolean env2)
  bad3733 : PathP (λ _ → Two) (bop (bop b0 b1) (bop (bop b1 (bop b1 b0)) b1)) b1 → ⊥
  bad3733  p = false≢true (cong lower p)
  cut3733 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 1) (op (var 2) (var 0))) (var 2))) , (var 2)) → ⊥
  cut3733  adequate = bad3733  (Adequate.valid adequate Two boolean env8)
  bad3734 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b0 (bop b0 b0)) b0)) b1 → ⊥
  bad3734  p = false≢true (cong lower p)
  cut3734 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 1) (op (var 2) (var 0))) (var 2))) , (var 3)) → ⊥
  cut3734  adequate = bad3734  (Adequate.valid adequate Two boolean env4)
  bad3735 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b0 (bop b0 b0)) b1)) b0 → ⊥
  bad3735  p = false≢true (sym (cong lower p))
  cut3735 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 1) (op (var 2) (var 0))) (var 3))) , (var 0)) → ⊥
  cut3735  adequate = bad3735  (Adequate.valid adequate Two boolean env4)
  bad3736 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b0 (bop b0 b0)) b1)) b0 → ⊥
  bad3736  p = false≢true (sym (cong lower p))
  cut3736 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 1) (op (var 2) (var 0))) (var 3))) , (var 1)) → ⊥
  cut3736  adequate = bad3736  (Adequate.valid adequate Two boolean env4)
  bad3737 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b0 (bop b0 b0)) b1)) b0 → ⊥
  bad3737  p = false≢true (sym (cong lower p))
  cut3737 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 1) (op (var 2) (var 0))) (var 3))) , (var 2)) → ⊥
  cut3737  adequate = bad3737  (Adequate.valid adequate Two boolean env4)
  bad3738 : PathP (λ _ → Two) (bop (bop b0 b1) (bop (bop b1 (bop b0 b0)) b1)) b1 → ⊥
  bad3738  p = false≢true (cong lower p)
  cut3738 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 1) (op (var 2) (var 0))) (var 3))) , (var 3)) → ⊥
  cut3738  adequate = bad3738  (Adequate.valid adequate Two boolean env9)
  bad3739 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b0 (bop b0 b0)) b0)) b1 → ⊥
  bad3739  p = false≢true (cong lower p)
  cut3739 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 1) (op (var 2) (var 0))) (var 3))) , (var 4)) → ⊥
  cut3739  adequate = bad3739  (Adequate.valid adequate Two boolean env7)
  holds3740 : (z0 z1 z2 : A2) → (mul2 (mul2 z0 z1) (mul2 (mul2 z1 (mul2 z2 z1)) z0)) ≡ z0
  holds3740 z0 z1 z2 = refl
  cut3740 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 1) (op (var 2) (var 1))) (var 0))) , (var 0)) → ⊥
  cut3740  = reject2 ((op (op (var 0) (var 1)) (op (op (var 1) (op (var 2) (var 1))) (var 0))) , (var 0)) (λ env → holds3740 (env 0) (env 1) (env 2))
  bad3741 : PathP (λ _ → Two) (bop (bop b0 b1) (bop (bop b1 (bop b0 b1)) b0)) b1 → ⊥
  bad3741  p = false≢true (cong lower p)
  cut3741 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 1) (op (var 2) (var 1))) (var 0))) , (var 1)) → ⊥
  cut3741  adequate = bad3741  (Adequate.valid adequate Two boolean env5)
  bad3742 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b0 (bop b1 b0)) b0)) b1 → ⊥
  bad3742  p = false≢true (cong lower p)
  cut3742 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 1) (op (var 2) (var 1))) (var 0))) , (var 2)) → ⊥
  cut3742  adequate = bad3742  (Adequate.valid adequate Two boolean env2)
  bad3743 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b0 (bop b0 b0)) b0)) b1 → ⊥
  bad3743  p = false≢true (cong lower p)
  cut3743 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 1) (op (var 2) (var 1))) (var 0))) , (var 3)) → ⊥
  cut3743  adequate = bad3743  (Adequate.valid adequate Two boolean env4)
  bad3744 : PathP (λ _ → Two) (bop (bop b0 b1) (bop (bop b1 (bop b1 b1)) b1)) b0 → ⊥
  bad3744  p = false≢true (sym (cong lower p))
  cut3744 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 1) (op (var 2) (var 1))) (var 1))) , (var 0)) → ⊥
  cut3744  adequate = bad3744  (Adequate.valid adequate Two boolean env8)
  bad3745 : PathP (λ _ → Two) (bop (bop b0 b1) (bop (bop b1 (bop b0 b1)) b1)) b1 → ⊥
  bad3745  p = false≢true (cong lower p)
  cut3745 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 1) (op (var 2) (var 1))) (var 1))) , (var 1)) → ⊥
  cut3745  adequate = bad3745  (Adequate.valid adequate Two boolean env5)
  bad3746 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b0 (bop b1 b0)) b0)) b1 → ⊥
  bad3746  p = false≢true (cong lower p)
  cut3746 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 1) (op (var 2) (var 1))) (var 1))) , (var 2)) → ⊥
  cut3746  adequate = bad3746  (Adequate.valid adequate Two boolean env2)
  bad3747 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b0 (bop b0 b0)) b0)) b1 → ⊥
  bad3747  p = false≢true (cong lower p)
  cut3747 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 1) (op (var 2) (var 1))) (var 1))) , (var 3)) → ⊥
  cut3747  adequate = bad3747  (Adequate.valid adequate Two boolean env4)
  bad3748 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b0 (bop b1 b0)) b1)) b0 → ⊥
  bad3748  p = false≢true (sym (cong lower p))
  cut3748 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 1) (op (var 2) (var 1))) (var 2))) , (var 0)) → ⊥
  cut3748  adequate = bad3748  (Adequate.valid adequate Two boolean env2)
  bad3749 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b0 (bop b1 b0)) b1)) b0 → ⊥
  bad3749  p = false≢true (sym (cong lower p))
  cut3749 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 1) (op (var 2) (var 1))) (var 2))) , (var 1)) → ⊥
  cut3749  adequate = bad3749  (Adequate.valid adequate Two boolean env2)
  bad3750 : PathP (λ _ → Two) (bop (bop b1 b1) (bop (bop b1 (bop b0 b1)) b0)) b0 → ⊥
  bad3750  p = false≢true (sym (cong lower p))
  cut3750 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 1) (op (var 2) (var 1))) (var 2))) , (var 2)) → ⊥
  cut3750  adequate = bad3750  (Adequate.valid adequate Two boolean env16)
  bad3751 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b0 (bop b0 b0)) b0)) b1 → ⊥
  bad3751  p = false≢true (cong lower p)
  cut3751 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 1) (op (var 2) (var 1))) (var 2))) , (var 3)) → ⊥
  cut3751  adequate = bad3751  (Adequate.valid adequate Two boolean env4)
  bad3752 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b0 (bop b0 b0)) b1)) b0 → ⊥
  bad3752  p = false≢true (sym (cong lower p))
  cut3752 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 1) (op (var 2) (var 1))) (var 3))) , (var 0)) → ⊥
  cut3752  adequate = bad3752  (Adequate.valid adequate Two boolean env4)
  bad3753 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b0 (bop b0 b0)) b1)) b0 → ⊥
  bad3753  p = false≢true (sym (cong lower p))
  cut3753 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 1) (op (var 2) (var 1))) (var 3))) , (var 1)) → ⊥
  cut3753  adequate = bad3753  (Adequate.valid adequate Two boolean env4)
  bad3754 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b0 (bop b0 b0)) b1)) b0 → ⊥
  bad3754  p = false≢true (sym (cong lower p))
  cut3754 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 1) (op (var 2) (var 1))) (var 3))) , (var 2)) → ⊥
  cut3754  adequate = bad3754  (Adequate.valid adequate Two boolean env4)
  bad3755 : PathP (λ _ → Two) (bop (bop b0 b1) (bop (bop b1 (bop b0 b1)) b1)) b1 → ⊥
  bad3755  p = false≢true (cong lower p)
  cut3755 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 1) (op (var 2) (var 1))) (var 3))) , (var 3)) → ⊥
  cut3755  adequate = bad3755  (Adequate.valid adequate Two boolean env9)
  bad3756 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b0 (bop b0 b0)) b0)) b1 → ⊥
  bad3756  p = false≢true (cong lower p)
  cut3756 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 1) (op (var 2) (var 1))) (var 3))) , (var 4)) → ⊥
  cut3756  adequate = bad3756  (Adequate.valid adequate Two boolean env7)
  holds3757 : (z0 z1 z2 : A2) → (mul2 (mul2 z0 z1) (mul2 (mul2 z1 (mul2 z2 z2)) z0)) ≡ z0
  holds3757 z0 z1 z2 = refl
  cut3757 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 1) (op (var 2) (var 2))) (var 0))) , (var 0)) → ⊥
  cut3757  = reject2 ((op (op (var 0) (var 1)) (op (op (var 1) (op (var 2) (var 2))) (var 0))) , (var 0)) (λ env → holds3757 (env 0) (env 1) (env 2))
  bad3758 : PathP (λ _ → Two) (bop (bop b0 b1) (bop (bop b1 (bop b0 b0)) b0)) b1 → ⊥
  bad3758  p = false≢true (cong lower p)
  cut3758 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 1) (op (var 2) (var 2))) (var 0))) , (var 1)) → ⊥
  cut3758  adequate = bad3758  (Adequate.valid adequate Two boolean env5)
  bad3759 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b0 (bop b1 b1)) b0)) b1 → ⊥
  bad3759  p = false≢true (cong lower p)
  cut3759 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 1) (op (var 2) (var 2))) (var 0))) , (var 2)) → ⊥
  cut3759  adequate = bad3759  (Adequate.valid adequate Two boolean env2)
  bad3760 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b0 (bop b0 b0)) b0)) b1 → ⊥
  bad3760  p = false≢true (cong lower p)
  cut3760 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 1) (op (var 2) (var 2))) (var 0))) , (var 3)) → ⊥
  cut3760  adequate = bad3760  (Adequate.valid adequate Two boolean env4)
  bad3761 : PathP (λ _ → Two) (bop (bop b0 b1) (bop (bop b1 (bop b1 b1)) b1)) b0 → ⊥
  bad3761  p = false≢true (sym (cong lower p))
  cut3761 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 1) (op (var 2) (var 2))) (var 1))) , (var 0)) → ⊥
  cut3761  adequate = bad3761  (Adequate.valid adequate Two boolean env8)
  bad3762 : PathP (λ _ → Two) (bop (bop b0 b1) (bop (bop b1 (bop b0 b0)) b1)) b1 → ⊥
  bad3762  p = false≢true (cong lower p)
  cut3762 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 1) (op (var 2) (var 2))) (var 1))) , (var 1)) → ⊥
  cut3762  adequate = bad3762  (Adequate.valid adequate Two boolean env5)
  bad3763 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b0 (bop b1 b1)) b0)) b1 → ⊥
  bad3763  p = false≢true (cong lower p)
  cut3763 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 1) (op (var 2) (var 2))) (var 1))) , (var 2)) → ⊥
  cut3763  adequate = bad3763  (Adequate.valid adequate Two boolean env2)
  bad3764 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b0 (bop b0 b0)) b0)) b1 → ⊥
  bad3764  p = false≢true (cong lower p)
  cut3764 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 1) (op (var 2) (var 2))) (var 1))) , (var 3)) → ⊥
  cut3764  adequate = bad3764  (Adequate.valid adequate Two boolean env4)
  bad3765 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b0 (bop b1 b1)) b1)) b0 → ⊥
  bad3765  p = false≢true (sym (cong lower p))
  cut3765 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 1) (op (var 2) (var 2))) (var 2))) , (var 0)) → ⊥
  cut3765  adequate = bad3765  (Adequate.valid adequate Two boolean env2)
  bad3766 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b0 (bop b1 b1)) b1)) b0 → ⊥
  bad3766  p = false≢true (sym (cong lower p))
  cut3766 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 1) (op (var 2) (var 2))) (var 2))) , (var 1)) → ⊥
  cut3766  adequate = bad3766  (Adequate.valid adequate Two boolean env2)
  bad3767 : PathP (λ _ → Two) (bop (bop b1 b1) (bop (bop b1 (bop b0 b0)) b0)) b0 → ⊥
  bad3767  p = false≢true (sym (cong lower p))
  cut3767 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 1) (op (var 2) (var 2))) (var 2))) , (var 2)) → ⊥
  cut3767  adequate = bad3767  (Adequate.valid adequate Two boolean env16)
  bad3768 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b0 (bop b0 b0)) b0)) b1 → ⊥
  bad3768  p = false≢true (cong lower p)
  cut3768 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 1) (op (var 2) (var 2))) (var 2))) , (var 3)) → ⊥
  cut3768  adequate = bad3768  (Adequate.valid adequate Two boolean env4)
  bad3769 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b0 (bop b0 b0)) b1)) b0 → ⊥
  bad3769  p = false≢true (sym (cong lower p))
  cut3769 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 1) (op (var 2) (var 2))) (var 3))) , (var 0)) → ⊥
  cut3769  adequate = bad3769  (Adequate.valid adequate Two boolean env4)
  bad3770 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b0 (bop b0 b0)) b1)) b0 → ⊥
  bad3770  p = false≢true (sym (cong lower p))
  cut3770 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 1) (op (var 2) (var 2))) (var 3))) , (var 1)) → ⊥
  cut3770  adequate = bad3770  (Adequate.valid adequate Two boolean env4)
  bad3771 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b0 (bop b0 b0)) b1)) b0 → ⊥
  bad3771  p = false≢true (sym (cong lower p))
  cut3771 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 1) (op (var 2) (var 2))) (var 3))) , (var 2)) → ⊥
  cut3771  adequate = bad3771  (Adequate.valid adequate Two boolean env4)
  bad3772 : PathP (λ _ → Two) (bop (bop b0 b1) (bop (bop b1 (bop b0 b0)) b1)) b1 → ⊥
  bad3772  p = false≢true (cong lower p)
  cut3772 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 1) (op (var 2) (var 2))) (var 3))) , (var 3)) → ⊥
  cut3772  adequate = bad3772  (Adequate.valid adequate Two boolean env9)
  bad3773 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b0 (bop b0 b0)) b0)) b1 → ⊥
  bad3773  p = false≢true (cong lower p)
  cut3773 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 1) (op (var 2) (var 2))) (var 3))) , (var 4)) → ⊥
  cut3773  adequate = bad3773  (Adequate.valid adequate Two boolean env7)
  holds3774 : (z0 z1 z2 z3 : A2) → (mul2 (mul2 z0 z1) (mul2 (mul2 z1 (mul2 z2 z3)) z0)) ≡ z0
  holds3774 z0 z1 z2 z3 = refl
  cut3774 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 1) (op (var 2) (var 3))) (var 0))) , (var 0)) → ⊥
  cut3774  = reject2 ((op (op (var 0) (var 1)) (op (op (var 1) (op (var 2) (var 3))) (var 0))) , (var 0)) (λ env → holds3774 (env 0) (env 1) (env 2) (env 3))
  bad3775 : PathP (λ _ → Two) (bop (bop b0 b1) (bop (bop b1 (bop b0 b0)) b0)) b1 → ⊥
  bad3775  p = false≢true (cong lower p)
  cut3775 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 1) (op (var 2) (var 3))) (var 0))) , (var 1)) → ⊥
  cut3775  adequate = bad3775  (Adequate.valid adequate Two boolean env10)
  bad3776 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b0 (bop b1 b0)) b0)) b1 → ⊥
  bad3776  p = false≢true (cong lower p)
  cut3776 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 1) (op (var 2) (var 3))) (var 0))) , (var 2)) → ⊥
  cut3776  adequate = bad3776  (Adequate.valid adequate Two boolean env11)
  bad3777 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b0 (bop b0 b1)) b0)) b1 → ⊥
  bad3777  p = false≢true (cong lower p)
  cut3777 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 1) (op (var 2) (var 3))) (var 0))) , (var 3)) → ⊥
  cut3777  adequate = bad3777  (Adequate.valid adequate Two boolean env4)
  bad3778 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b0 (bop b0 b0)) b0)) b1 → ⊥
  bad3778  p = false≢true (cong lower p)
  cut3778 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 1) (op (var 2) (var 3))) (var 0))) , (var 4)) → ⊥
  cut3778  adequate = bad3778  (Adequate.valid adequate Two boolean env7)
  bad3779 : PathP (λ _ → Two) (bop (bop b0 b1) (bop (bop b1 (bop b1 b1)) b1)) b0 → ⊥
  bad3779  p = false≢true (sym (cong lower p))
  cut3779 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 1) (op (var 2) (var 3))) (var 1))) , (var 0)) → ⊥
  cut3779  adequate = bad3779  (Adequate.valid adequate Two boolean env12)
  bad3780 : PathP (λ _ → Two) (bop (bop b0 b1) (bop (bop b1 (bop b0 b0)) b1)) b1 → ⊥
  bad3780  p = false≢true (cong lower p)
  cut3780 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 1) (op (var 2) (var 3))) (var 1))) , (var 1)) → ⊥
  cut3780  adequate = bad3780  (Adequate.valid adequate Two boolean env10)
  bad3781 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b0 (bop b1 b0)) b0)) b1 → ⊥
  bad3781  p = false≢true (cong lower p)
  cut3781 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 1) (op (var 2) (var 3))) (var 1))) , (var 2)) → ⊥
  cut3781  adequate = bad3781  (Adequate.valid adequate Two boolean env11)
  bad3782 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b0 (bop b0 b1)) b0)) b1 → ⊥
  bad3782  p = false≢true (cong lower p)
  cut3782 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 1) (op (var 2) (var 3))) (var 1))) , (var 3)) → ⊥
  cut3782  adequate = bad3782  (Adequate.valid adequate Two boolean env4)
  bad3783 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b0 (bop b0 b0)) b0)) b1 → ⊥
  bad3783  p = false≢true (cong lower p)
  cut3783 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 1) (op (var 2) (var 3))) (var 1))) , (var 4)) → ⊥
  cut3783  adequate = bad3783  (Adequate.valid adequate Two boolean env7)
  bad3784 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b0 (bop b1 b0)) b1)) b0 → ⊥
  bad3784  p = false≢true (sym (cong lower p))
  cut3784 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 1) (op (var 2) (var 3))) (var 2))) , (var 0)) → ⊥
  cut3784  adequate = bad3784  (Adequate.valid adequate Two boolean env11)
  bad3785 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b0 (bop b1 b0)) b1)) b0 → ⊥
  bad3785  p = false≢true (sym (cong lower p))
  cut3785 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 1) (op (var 2) (var 3))) (var 2))) , (var 1)) → ⊥
  cut3785  adequate = bad3785  (Adequate.valid adequate Two boolean env11)
  bad3786 : PathP (λ _ → Two) (bop (bop b0 b1) (bop (bop b1 (bop b1 b0)) b1)) b1 → ⊥
  bad3786  p = false≢true (cong lower p)
  cut3786 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 1) (op (var 2) (var 3))) (var 2))) , (var 2)) → ⊥
  cut3786  adequate = bad3786  (Adequate.valid adequate Two boolean env13)
  bad3787 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b0 (bop b0 b1)) b0)) b1 → ⊥
  bad3787  p = false≢true (cong lower p)
  cut3787 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 1) (op (var 2) (var 3))) (var 2))) , (var 3)) → ⊥
  cut3787  adequate = bad3787  (Adequate.valid adequate Two boolean env4)
  bad3788 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b0 (bop b0 b0)) b0)) b1 → ⊥
  bad3788  p = false≢true (cong lower p)
  cut3788 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 1) (op (var 2) (var 3))) (var 2))) , (var 4)) → ⊥
  cut3788  adequate = bad3788  (Adequate.valid adequate Two boolean env7)
  bad3789 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b0 (bop b0 b1)) b1)) b0 → ⊥
  bad3789  p = false≢true (sym (cong lower p))
  cut3789 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 1) (op (var 2) (var 3))) (var 3))) , (var 0)) → ⊥
  cut3789  adequate = bad3789  (Adequate.valid adequate Two boolean env4)
  bad3790 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b0 (bop b0 b1)) b1)) b0 → ⊥
  bad3790  p = false≢true (sym (cong lower p))
  cut3790 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 1) (op (var 2) (var 3))) (var 3))) , (var 1)) → ⊥
  cut3790  adequate = bad3790  (Adequate.valid adequate Two boolean env4)
  bad3791 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b0 (bop b0 b1)) b1)) b0 → ⊥
  bad3791  p = false≢true (sym (cong lower p))
  cut3791 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 1) (op (var 2) (var 3))) (var 3))) , (var 2)) → ⊥
  cut3791  adequate = bad3791  (Adequate.valid adequate Two boolean env4)
  bad3792 : PathP (λ _ → Two) (bop (bop b0 b1) (bop (bop b1 (bop b0 b1)) b1)) b1 → ⊥
  bad3792  p = false≢true (cong lower p)
  cut3792 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 1) (op (var 2) (var 3))) (var 3))) , (var 3)) → ⊥
  cut3792  adequate = bad3792  (Adequate.valid adequate Two boolean env9)
  bad3793 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b0 (bop b0 b0)) b0)) b1 → ⊥
  bad3793  p = false≢true (cong lower p)
  cut3793 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 1) (op (var 2) (var 3))) (var 3))) , (var 4)) → ⊥
  cut3793  adequate = bad3793  (Adequate.valid adequate Two boolean env7)
  bad3794 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b0 (bop b0 b0)) b1)) b0 → ⊥
  bad3794  p = false≢true (sym (cong lower p))
  cut3794 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 1) (op (var 2) (var 3))) (var 4))) , (var 0)) → ⊥
  cut3794  adequate = bad3794  (Adequate.valid adequate Two boolean env7)
  bad3795 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b0 (bop b0 b0)) b1)) b0 → ⊥
  bad3795  p = false≢true (sym (cong lower p))
  cut3795 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 1) (op (var 2) (var 3))) (var 4))) , (var 1)) → ⊥
  cut3795  adequate = bad3795  (Adequate.valid adequate Two boolean env7)
  bad3796 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b0 (bop b0 b0)) b1)) b0 → ⊥
  bad3796  p = false≢true (sym (cong lower p))
  cut3796 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 1) (op (var 2) (var 3))) (var 4))) , (var 2)) → ⊥
  cut3796  adequate = bad3796  (Adequate.valid adequate Two boolean env7)
  bad3797 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b0 (bop b0 b0)) b1)) b0 → ⊥
  bad3797  p = false≢true (sym (cong lower p))
  cut3797 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 1) (op (var 2) (var 3))) (var 4))) , (var 3)) → ⊥
  cut3797  adequate = bad3797  (Adequate.valid adequate Two boolean env7)
  bad3798 : PathP (λ _ → Two) (bop (bop b0 b1) (bop (bop b1 (bop b0 b0)) b1)) b1 → ⊥
  bad3798  p = false≢true (cong lower p)
  cut3798 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 1) (op (var 2) (var 3))) (var 4))) , (var 4)) → ⊥
  cut3798  adequate = bad3798  (Adequate.valid adequate Two boolean env14)
  bad3799 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b0 (bop b0 b0)) b0)) b1 → ⊥
  bad3799  p = false≢true (cong lower p)
  cut3799 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 1) (op (var 2) (var 3))) (var 4))) , (var 5)) → ⊥
  cut3799  adequate = bad3799  (Adequate.valid adequate Two boolean env15)
  holds3800 : (z0 z1 z2 : A2) → (mul2 (mul2 z0 z1) (mul2 (mul2 z2 (mul2 z0 z0)) z0)) ≡ z0
  holds3800 z0 z1 z2 = refl
  cut3800 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 2) (op (var 0) (var 0))) (var 0))) , (var 0)) → ⊥
  cut3800  = reject2 ((op (op (var 0) (var 1)) (op (op (var 2) (op (var 0) (var 0))) (var 0))) , (var 0)) (λ env → holds3800 (env 0) (env 1) (env 2))
  bad3801 : PathP (λ _ → Two) (bop (bop b0 b1) (bop (bop b0 (bop b0 b0)) b0)) b1 → ⊥
  bad3801  p = false≢true (cong lower p)
  cut3801 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 2) (op (var 0) (var 0))) (var 0))) , (var 1)) → ⊥
  cut3801  adequate = bad3801  (Adequate.valid adequate Two boolean env5)
  bad3802 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b1 (bop b0 b0)) b0)) b1 → ⊥
  bad3802  p = false≢true (cong lower p)
  cut3802 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 2) (op (var 0) (var 0))) (var 0))) , (var 2)) → ⊥
  cut3802  adequate = bad3802  (Adequate.valid adequate Two boolean env2)
  bad3803 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b0 (bop b0 b0)) b0)) b1 → ⊥
  bad3803  p = false≢true (cong lower p)
  cut3803 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 2) (op (var 0) (var 0))) (var 0))) , (var 3)) → ⊥
  cut3803  adequate = bad3803  (Adequate.valid adequate Two boolean env4)
  bad3804 : PathP (λ _ → Two) (bop (bop b0 b1) (bop (bop b0 (bop b0 b0)) b1)) b0 → ⊥
  bad3804  p = false≢true (sym (cong lower p))
  cut3804 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 2) (op (var 0) (var 0))) (var 1))) , (var 0)) → ⊥
  cut3804  adequate = bad3804  (Adequate.valid adequate Two boolean env5)
  bad3805 : PathP (λ _ → Two) (bop (bop b0 b1) (bop (bop b1 (bop b0 b0)) b1)) b1 → ⊥
  bad3805  p = false≢true (cong lower p)
  cut3805 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 2) (op (var 0) (var 0))) (var 1))) , (var 1)) → ⊥
  cut3805  adequate = bad3805  (Adequate.valid adequate Two boolean env8)
  bad3806 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b1 (bop b0 b0)) b0)) b1 → ⊥
  bad3806  p = false≢true (cong lower p)
  cut3806 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 2) (op (var 0) (var 0))) (var 1))) , (var 2)) → ⊥
  cut3806  adequate = bad3806  (Adequate.valid adequate Two boolean env2)
  bad3807 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b0 (bop b0 b0)) b0)) b1 → ⊥
  bad3807  p = false≢true (cong lower p)
  cut3807 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 2) (op (var 0) (var 0))) (var 1))) , (var 3)) → ⊥
  cut3807  adequate = bad3807  (Adequate.valid adequate Two boolean env4)
  bad3808 : PathP (λ _ → Two) (bop (bop b1 b0) (bop (bop b0 (bop b1 b1)) b0)) b1 → ⊥
  bad3808  p = false≢true (cong lower p)
  cut3808 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 2) (op (var 0) (var 0))) (var 2))) , (var 0)) → ⊥
  cut3808  adequate = bad3808  (Adequate.valid adequate Two boolean env3)
  bad3809 : PathP (λ _ → Two) (bop (bop b0 b1) (bop (bop b0 (bop b0 b0)) b0)) b1 → ⊥
  bad3809  p = false≢true (cong lower p)
  cut3809 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 2) (op (var 0) (var 0))) (var 2))) , (var 1)) → ⊥
  cut3809  adequate = bad3809  (Adequate.valid adequate Two boolean env5)
  bad3810 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b1 (bop b0 b0)) b1)) b1 → ⊥
  bad3810  p = false≢true (cong lower p)
  cut3810 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 2) (op (var 0) (var 0))) (var 2))) , (var 2)) → ⊥
  cut3810  adequate = bad3810  (Adequate.valid adequate Two boolean env2)
  bad3811 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b0 (bop b0 b0)) b0)) b1 → ⊥
  bad3811  p = false≢true (cong lower p)
  cut3811 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 2) (op (var 0) (var 0))) (var 2))) , (var 3)) → ⊥
  cut3811  adequate = bad3811  (Adequate.valid adequate Two boolean env4)
  bad3812 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b0 (bop b0 b0)) b1)) b0 → ⊥
  bad3812  p = false≢true (sym (cong lower p))
  cut3812 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 2) (op (var 0) (var 0))) (var 3))) , (var 0)) → ⊥
  cut3812  adequate = bad3812  (Adequate.valid adequate Two boolean env4)
  bad3813 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b0 (bop b0 b0)) b1)) b0 → ⊥
  bad3813  p = false≢true (sym (cong lower p))
  cut3813 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 2) (op (var 0) (var 0))) (var 3))) , (var 1)) → ⊥
  cut3813  adequate = bad3813  (Adequate.valid adequate Two boolean env4)
  bad3814 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b0 (bop b0 b0)) b1)) b0 → ⊥
  bad3814  p = false≢true (sym (cong lower p))
  cut3814 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 2) (op (var 0) (var 0))) (var 3))) , (var 2)) → ⊥
  cut3814  adequate = bad3814  (Adequate.valid adequate Two boolean env4)
  env21 : ℕ → Two
  env21 zero = b0
  env21 (suc zero) = b0
  env21 (suc (suc zero)) = b1
  env21 (suc (suc (suc zero))) = b1
  env21 (suc (suc (suc (suc rest)))) = b0
  bad3815 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b1 (bop b0 b0)) b1)) b1 → ⊥
  bad3815  p = false≢true (cong lower p)
  cut3815 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 2) (op (var 0) (var 0))) (var 3))) , (var 3)) → ⊥
  cut3815  adequate = bad3815  (Adequate.valid adequate Two boolean env21)
  bad3816 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b0 (bop b0 b0)) b0)) b1 → ⊥
  bad3816  p = false≢true (cong lower p)
  cut3816 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 2) (op (var 0) (var 0))) (var 3))) , (var 4)) → ⊥
  cut3816  adequate = bad3816  (Adequate.valid adequate Two boolean env7)
  bad3817 : PathP (λ _ → Two) (bop (bop b1 b0) (bop (bop b1 (bop b1 b0)) b1)) b1 → ⊥
  bad3817  p = false≢true (cong lower p)
  cut3817 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 2) (op (var 0) (var 1))) (var 0))) , (var 0)) → ⊥
  cut3817  adequate = bad3817  (Adequate.valid adequate Two boolean env17)
  bad3818 : PathP (λ _ → Two) (bop (bop b0 b1) (bop (bop b0 (bop b0 b1)) b0)) b1 → ⊥
  bad3818  p = false≢true (cong lower p)
  cut3818 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 2) (op (var 0) (var 1))) (var 0))) , (var 1)) → ⊥
  cut3818  adequate = bad3818  (Adequate.valid adequate Two boolean env5)
  bad3819 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b1 (bop b0 b0)) b0)) b1 → ⊥
  bad3819  p = false≢true (cong lower p)
  cut3819 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 2) (op (var 0) (var 1))) (var 0))) , (var 2)) → ⊥
  cut3819  adequate = bad3819  (Adequate.valid adequate Two boolean env2)
  bad3820 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b0 (bop b0 b0)) b0)) b1 → ⊥
  bad3820  p = false≢true (cong lower p)
  cut3820 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 2) (op (var 0) (var 1))) (var 0))) , (var 3)) → ⊥
  cut3820  adequate = bad3820  (Adequate.valid adequate Two boolean env4)
  bad3821 : PathP (λ _ → Two) (bop (bop b0 b1) (bop (bop b0 (bop b0 b1)) b1)) b0 → ⊥
  bad3821  p = false≢true (sym (cong lower p))
  cut3821 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 2) (op (var 0) (var 1))) (var 1))) , (var 0)) → ⊥
  cut3821  adequate = bad3821  (Adequate.valid adequate Two boolean env5)
  bad3822 : PathP (λ _ → Two) (bop (bop b0 b1) (bop (bop b1 (bop b0 b1)) b1)) b1 → ⊥
  bad3822  p = false≢true (cong lower p)
  cut3822 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 2) (op (var 0) (var 1))) (var 1))) , (var 1)) → ⊥
  cut3822  adequate = bad3822  (Adequate.valid adequate Two boolean env8)
  bad3823 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b1 (bop b0 b0)) b0)) b1 → ⊥
  bad3823  p = false≢true (cong lower p)
  cut3823 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 2) (op (var 0) (var 1))) (var 1))) , (var 2)) → ⊥
  cut3823  adequate = bad3823  (Adequate.valid adequate Two boolean env2)
  bad3824 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b0 (bop b0 b0)) b0)) b1 → ⊥
  bad3824  p = false≢true (cong lower p)
  cut3824 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 2) (op (var 0) (var 1))) (var 1))) , (var 3)) → ⊥
  cut3824  adequate = bad3824  (Adequate.valid adequate Two boolean env4)
  bad3825 : PathP (λ _ → Two) (bop (bop b1 b0) (bop (bop b0 (bop b1 b0)) b0)) b1 → ⊥
  bad3825  p = false≢true (cong lower p)
  cut3825 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 2) (op (var 0) (var 1))) (var 2))) , (var 0)) → ⊥
  cut3825  adequate = bad3825  (Adequate.valid adequate Two boolean env3)
  bad3826 : PathP (λ _ → Two) (bop (bop b0 b1) (bop (bop b0 (bop b0 b1)) b0)) b1 → ⊥
  bad3826  p = false≢true (cong lower p)
  cut3826 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 2) (op (var 0) (var 1))) (var 2))) , (var 1)) → ⊥
  cut3826  adequate = bad3826  (Adequate.valid adequate Two boolean env5)
  bad3827 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b1 (bop b0 b0)) b1)) b1 → ⊥
  bad3827  p = false≢true (cong lower p)
  cut3827 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 2) (op (var 0) (var 1))) (var 2))) , (var 2)) → ⊥
  cut3827  adequate = bad3827  (Adequate.valid adequate Two boolean env2)
  bad3828 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b0 (bop b0 b0)) b0)) b1 → ⊥
  bad3828  p = false≢true (cong lower p)
  cut3828 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 2) (op (var 0) (var 1))) (var 2))) , (var 3)) → ⊥
  cut3828  adequate = bad3828  (Adequate.valid adequate Two boolean env4)
  bad3829 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b0 (bop b0 b0)) b1)) b0 → ⊥
  bad3829  p = false≢true (sym (cong lower p))
  cut3829 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 2) (op (var 0) (var 1))) (var 3))) , (var 0)) → ⊥
  cut3829  adequate = bad3829  (Adequate.valid adequate Two boolean env4)
  bad3830 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b0 (bop b0 b0)) b1)) b0 → ⊥
  bad3830  p = false≢true (sym (cong lower p))
  cut3830 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 2) (op (var 0) (var 1))) (var 3))) , (var 1)) → ⊥
  cut3830  adequate = bad3830  (Adequate.valid adequate Two boolean env4)
  bad3831 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b0 (bop b0 b0)) b1)) b0 → ⊥
  bad3831  p = false≢true (sym (cong lower p))
  cut3831 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 2) (op (var 0) (var 1))) (var 3))) , (var 2)) → ⊥
  cut3831  adequate = bad3831  (Adequate.valid adequate Two boolean env4)
  bad3832 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b1 (bop b0 b0)) b1)) b1 → ⊥
  bad3832  p = false≢true (cong lower p)
  cut3832 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 2) (op (var 0) (var 1))) (var 3))) , (var 3)) → ⊥
  cut3832  adequate = bad3832  (Adequate.valid adequate Two boolean env21)
  bad3833 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b0 (bop b0 b0)) b0)) b1 → ⊥
  bad3833  p = false≢true (cong lower p)
  cut3833 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 2) (op (var 0) (var 1))) (var 3))) , (var 4)) → ⊥
  cut3833  adequate = bad3833  (Adequate.valid adequate Two boolean env7)
  holds3834 : (z0 z1 z2 : A2) → (mul2 (mul2 z0 z1) (mul2 (mul2 z2 (mul2 z0 z2)) z0)) ≡ z0
  holds3834 z0 z1 z2 = refl
  cut3834 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 2) (op (var 0) (var 2))) (var 0))) , (var 0)) → ⊥
  cut3834  = reject2 ((op (op (var 0) (var 1)) (op (op (var 2) (op (var 0) (var 2))) (var 0))) , (var 0)) (λ env → holds3834 (env 0) (env 1) (env 2))
  bad3835 : PathP (λ _ → Two) (bop (bop b0 b1) (bop (bop b0 (bop b0 b0)) b0)) b1 → ⊥
  bad3835  p = false≢true (cong lower p)
  cut3835 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 2) (op (var 0) (var 2))) (var 0))) , (var 1)) → ⊥
  cut3835  adequate = bad3835  (Adequate.valid adequate Two boolean env5)
  bad3836 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b1 (bop b0 b1)) b0)) b1 → ⊥
  bad3836  p = false≢true (cong lower p)
  cut3836 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 2) (op (var 0) (var 2))) (var 0))) , (var 2)) → ⊥
  cut3836  adequate = bad3836  (Adequate.valid adequate Two boolean env2)
  bad3837 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b0 (bop b0 b0)) b0)) b1 → ⊥
  bad3837  p = false≢true (cong lower p)
  cut3837 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 2) (op (var 0) (var 2))) (var 0))) , (var 3)) → ⊥
  cut3837  adequate = bad3837  (Adequate.valid adequate Two boolean env4)
  bad3838 : PathP (λ _ → Two) (bop (bop b0 b1) (bop (bop b0 (bop b0 b0)) b1)) b0 → ⊥
  bad3838  p = false≢true (sym (cong lower p))
  cut3838 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 2) (op (var 0) (var 2))) (var 1))) , (var 0)) → ⊥
  cut3838  adequate = bad3838  (Adequate.valid adequate Two boolean env5)
  bad3839 : PathP (λ _ → Two) (bop (bop b0 b1) (bop (bop b1 (bop b0 b1)) b1)) b1 → ⊥
  bad3839  p = false≢true (cong lower p)
  cut3839 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 2) (op (var 0) (var 2))) (var 1))) , (var 1)) → ⊥
  cut3839  adequate = bad3839  (Adequate.valid adequate Two boolean env8)
  bad3840 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b1 (bop b0 b1)) b0)) b1 → ⊥
  bad3840  p = false≢true (cong lower p)
  cut3840 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 2) (op (var 0) (var 2))) (var 1))) , (var 2)) → ⊥
  cut3840  adequate = bad3840  (Adequate.valid adequate Two boolean env2)
  bad3841 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b0 (bop b0 b0)) b0)) b1 → ⊥
  bad3841  p = false≢true (cong lower p)
  cut3841 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 2) (op (var 0) (var 2))) (var 1))) , (var 3)) → ⊥
  cut3841  adequate = bad3841  (Adequate.valid adequate Two boolean env4)
  bad3842 : PathP (λ _ → Two) (bop (bop b1 b0) (bop (bop b0 (bop b1 b0)) b0)) b1 → ⊥
  bad3842  p = false≢true (cong lower p)
  cut3842 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 2) (op (var 0) (var 2))) (var 2))) , (var 0)) → ⊥
  cut3842  adequate = bad3842  (Adequate.valid adequate Two boolean env3)
  bad3843 : PathP (λ _ → Two) (bop (bop b0 b1) (bop (bop b0 (bop b0 b0)) b0)) b1 → ⊥
  bad3843  p = false≢true (cong lower p)
  cut3843 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 2) (op (var 0) (var 2))) (var 2))) , (var 1)) → ⊥
  cut3843  adequate = bad3843  (Adequate.valid adequate Two boolean env5)
  bad3844 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b1 (bop b0 b1)) b1)) b1 → ⊥
  bad3844  p = false≢true (cong lower p)
  cut3844 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 2) (op (var 0) (var 2))) (var 2))) , (var 2)) → ⊥
  cut3844  adequate = bad3844  (Adequate.valid adequate Two boolean env2)
  bad3845 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b0 (bop b0 b0)) b0)) b1 → ⊥
  bad3845  p = false≢true (cong lower p)
  cut3845 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 2) (op (var 0) (var 2))) (var 2))) , (var 3)) → ⊥
  cut3845  adequate = bad3845  (Adequate.valid adequate Two boolean env4)
  bad3846 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b0 (bop b0 b0)) b1)) b0 → ⊥
  bad3846  p = false≢true (sym (cong lower p))
  cut3846 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 2) (op (var 0) (var 2))) (var 3))) , (var 0)) → ⊥
  cut3846  adequate = bad3846  (Adequate.valid adequate Two boolean env4)
  bad3847 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b0 (bop b0 b0)) b1)) b0 → ⊥
  bad3847  p = false≢true (sym (cong lower p))
  cut3847 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 2) (op (var 0) (var 2))) (var 3))) , (var 1)) → ⊥
  cut3847  adequate = bad3847  (Adequate.valid adequate Two boolean env4)
  bad3848 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b0 (bop b0 b0)) b1)) b0 → ⊥
  bad3848  p = false≢true (sym (cong lower p))
  cut3848 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 2) (op (var 0) (var 2))) (var 3))) , (var 2)) → ⊥
  cut3848  adequate = bad3848  (Adequate.valid adequate Two boolean env4)
  bad3849 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b1 (bop b0 b1)) b1)) b1 → ⊥
  bad3849  p = false≢true (cong lower p)
  cut3849 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 2) (op (var 0) (var 2))) (var 3))) , (var 3)) → ⊥
  cut3849  adequate = bad3849  (Adequate.valid adequate Two boolean env21)
  bad3850 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b0 (bop b0 b0)) b0)) b1 → ⊥
  bad3850  p = false≢true (cong lower p)
  cut3850 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 2) (op (var 0) (var 2))) (var 3))) , (var 4)) → ⊥
  cut3850  adequate = bad3850  (Adequate.valid adequate Two boolean env7)
  bad3851 : PathP (λ _ → Two) (bop (bop b1 b0) (bop (bop b1 (bop b1 b0)) b1)) b1 → ⊥
  bad3851  p = false≢true (cong lower p)
  cut3851 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 2) (op (var 0) (var 3))) (var 0))) , (var 0)) → ⊥
  cut3851  adequate = bad3851  (Adequate.valid adequate Two boolean env19)
  bad3852 : PathP (λ _ → Two) (bop (bop b0 b1) (bop (bop b0 (bop b0 b0)) b0)) b1 → ⊥
  bad3852  p = false≢true (cong lower p)
  cut3852 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 2) (op (var 0) (var 3))) (var 0))) , (var 1)) → ⊥
  cut3852  adequate = bad3852  (Adequate.valid adequate Two boolean env10)
  bad3853 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b1 (bop b0 b0)) b0)) b1 → ⊥
  bad3853  p = false≢true (cong lower p)
  cut3853 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 2) (op (var 0) (var 3))) (var 0))) , (var 2)) → ⊥
  cut3853  adequate = bad3853  (Adequate.valid adequate Two boolean env11)
  bad3854 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b0 (bop b0 b1)) b0)) b1 → ⊥
  bad3854  p = false≢true (cong lower p)
  cut3854 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 2) (op (var 0) (var 3))) (var 0))) , (var 3)) → ⊥
  cut3854  adequate = bad3854  (Adequate.valid adequate Two boolean env4)
  bad3855 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b0 (bop b0 b0)) b0)) b1 → ⊥
  bad3855  p = false≢true (cong lower p)
  cut3855 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 2) (op (var 0) (var 3))) (var 0))) , (var 4)) → ⊥
  cut3855  adequate = bad3855  (Adequate.valid adequate Two boolean env7)
  bad3856 : PathP (λ _ → Two) (bop (bop b0 b1) (bop (bop b0 (bop b0 b0)) b1)) b0 → ⊥
  bad3856  p = false≢true (sym (cong lower p))
  cut3856 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 2) (op (var 0) (var 3))) (var 1))) , (var 0)) → ⊥
  cut3856  adequate = bad3856  (Adequate.valid adequate Two boolean env10)
  bad3857 : PathP (λ _ → Two) (bop (bop b0 b1) (bop (bop b1 (bop b0 b0)) b1)) b1 → ⊥
  bad3857  p = false≢true (cong lower p)
  cut3857 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 2) (op (var 0) (var 3))) (var 1))) , (var 1)) → ⊥
  cut3857  adequate = bad3857  (Adequate.valid adequate Two boolean env13)
  bad3858 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b1 (bop b0 b0)) b0)) b1 → ⊥
  bad3858  p = false≢true (cong lower p)
  cut3858 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 2) (op (var 0) (var 3))) (var 1))) , (var 2)) → ⊥
  cut3858  adequate = bad3858  (Adequate.valid adequate Two boolean env11)
  bad3859 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b0 (bop b0 b1)) b0)) b1 → ⊥
  bad3859  p = false≢true (cong lower p)
  cut3859 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 2) (op (var 0) (var 3))) (var 1))) , (var 3)) → ⊥
  cut3859  adequate = bad3859  (Adequate.valid adequate Two boolean env4)
  bad3860 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b0 (bop b0 b0)) b0)) b1 → ⊥
  bad3860  p = false≢true (cong lower p)
  cut3860 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 2) (op (var 0) (var 3))) (var 1))) , (var 4)) → ⊥
  cut3860  adequate = bad3860  (Adequate.valid adequate Two boolean env7)
  bad3861 : PathP (λ _ → Two) (bop (bop b1 b0) (bop (bop b0 (bop b1 b0)) b0)) b1 → ⊥
  bad3861  p = false≢true (cong lower p)
  cut3861 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 2) (op (var 0) (var 3))) (var 2))) , (var 0)) → ⊥
  cut3861  adequate = bad3861  (Adequate.valid adequate Two boolean env6)
  bad3862 : PathP (λ _ → Two) (bop (bop b0 b1) (bop (bop b0 (bop b0 b0)) b0)) b1 → ⊥
  bad3862  p = false≢true (cong lower p)
  cut3862 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 2) (op (var 0) (var 3))) (var 2))) , (var 1)) → ⊥
  cut3862  adequate = bad3862  (Adequate.valid adequate Two boolean env10)
  bad3863 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b1 (bop b0 b0)) b1)) b1 → ⊥
  bad3863  p = false≢true (cong lower p)
  cut3863 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 2) (op (var 0) (var 3))) (var 2))) , (var 2)) → ⊥
  cut3863  adequate = bad3863  (Adequate.valid adequate Two boolean env11)
  bad3864 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b0 (bop b0 b1)) b0)) b1 → ⊥
  bad3864  p = false≢true (cong lower p)
  cut3864 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 2) (op (var 0) (var 3))) (var 2))) , (var 3)) → ⊥
  cut3864  adequate = bad3864  (Adequate.valid adequate Two boolean env4)
  bad3865 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b0 (bop b0 b0)) b0)) b1 → ⊥
  bad3865  p = false≢true (cong lower p)
  cut3865 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 2) (op (var 0) (var 3))) (var 2))) , (var 4)) → ⊥
  cut3865  adequate = bad3865  (Adequate.valid adequate Two boolean env7)
  bad3866 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b0 (bop b0 b1)) b1)) b0 → ⊥
  bad3866  p = false≢true (sym (cong lower p))
  cut3866 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 2) (op (var 0) (var 3))) (var 3))) , (var 0)) → ⊥
  cut3866  adequate = bad3866  (Adequate.valid adequate Two boolean env4)
  bad3867 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b0 (bop b0 b1)) b1)) b0 → ⊥
  bad3867  p = false≢true (sym (cong lower p))
  cut3867 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 2) (op (var 0) (var 3))) (var 3))) , (var 1)) → ⊥
  cut3867  adequate = bad3867  (Adequate.valid adequate Two boolean env4)
  bad3868 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b0 (bop b0 b1)) b1)) b0 → ⊥
  bad3868  p = false≢true (sym (cong lower p))
  cut3868 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 2) (op (var 0) (var 3))) (var 3))) , (var 2)) → ⊥
  cut3868  adequate = bad3868  (Adequate.valid adequate Two boolean env4)
  bad3869 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b1 (bop b0 b1)) b1)) b1 → ⊥
  bad3869  p = false≢true (cong lower p)
  cut3869 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 2) (op (var 0) (var 3))) (var 3))) , (var 3)) → ⊥
  cut3869  adequate = bad3869  (Adequate.valid adequate Two boolean env21)
  bad3870 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b0 (bop b0 b0)) b0)) b1 → ⊥
  bad3870  p = false≢true (cong lower p)
  cut3870 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 2) (op (var 0) (var 3))) (var 3))) , (var 4)) → ⊥
  cut3870  adequate = bad3870  (Adequate.valid adequate Two boolean env7)
  bad3871 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b0 (bop b0 b0)) b1)) b0 → ⊥
  bad3871  p = false≢true (sym (cong lower p))
  cut3871 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 2) (op (var 0) (var 3))) (var 4))) , (var 0)) → ⊥
  cut3871  adequate = bad3871  (Adequate.valid adequate Two boolean env7)
  bad3872 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b0 (bop b0 b0)) b1)) b0 → ⊥
  bad3872  p = false≢true (sym (cong lower p))
  cut3872 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 2) (op (var 0) (var 3))) (var 4))) , (var 1)) → ⊥
  cut3872  adequate = bad3872  (Adequate.valid adequate Two boolean env7)
  bad3873 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b0 (bop b0 b0)) b1)) b0 → ⊥
  bad3873  p = false≢true (sym (cong lower p))
  cut3873 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 2) (op (var 0) (var 3))) (var 4))) , (var 2)) → ⊥
  cut3873  adequate = bad3873  (Adequate.valid adequate Two boolean env7)
  bad3874 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b0 (bop b0 b0)) b1)) b0 → ⊥
  bad3874  p = false≢true (sym (cong lower p))
  cut3874 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 2) (op (var 0) (var 3))) (var 4))) , (var 3)) → ⊥
  cut3874  adequate = bad3874  (Adequate.valid adequate Two boolean env7)
  env22 : ℕ → Two
  env22 zero = b0
  env22 (suc zero) = b0
  env22 (suc (suc zero)) = b1
  env22 (suc (suc (suc zero))) = b0
  env22 (suc (suc (suc (suc zero)))) = b1
  env22 (suc (suc (suc (suc (suc rest))))) = b0
  bad3875 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b1 (bop b0 b0)) b1)) b1 → ⊥
  bad3875  p = false≢true (cong lower p)
  cut3875 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 2) (op (var 0) (var 3))) (var 4))) , (var 4)) → ⊥
  cut3875  adequate = bad3875  (Adequate.valid adequate Two boolean env22)
  bad3876 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b0 (bop b0 b0)) b0)) b1 → ⊥
  bad3876  p = false≢true (cong lower p)
  cut3876 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 2) (op (var 0) (var 3))) (var 4))) , (var 5)) → ⊥
  cut3876  adequate = bad3876  (Adequate.valid adequate Two boolean env15)
  bad3877 : PathP (λ _ → Two) (bop (bop b1 b0) (bop (bop b1 (bop b0 b1)) b1)) b1 → ⊥
  bad3877  p = false≢true (cong lower p)
  cut3877 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 2) (op (var 1) (var 0))) (var 0))) , (var 0)) → ⊥
  cut3877  adequate = bad3877  (Adequate.valid adequate Two boolean env17)
  bad3878 : PathP (λ _ → Two) (bop (bop b0 b1) (bop (bop b0 (bop b1 b0)) b0)) b1 → ⊥
  bad3878  p = false≢true (cong lower p)
  cut3878 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 2) (op (var 1) (var 0))) (var 0))) , (var 1)) → ⊥
  cut3878  adequate = bad3878  (Adequate.valid adequate Two boolean env5)
  bad3879 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b1 (bop b0 b0)) b0)) b1 → ⊥
  bad3879  p = false≢true (cong lower p)
  cut3879 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 2) (op (var 1) (var 0))) (var 0))) , (var 2)) → ⊥
  cut3879  adequate = bad3879  (Adequate.valid adequate Two boolean env2)
  bad3880 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b0 (bop b0 b0)) b0)) b1 → ⊥
  bad3880  p = false≢true (cong lower p)
  cut3880 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 2) (op (var 1) (var 0))) (var 0))) , (var 3)) → ⊥
  cut3880  adequate = bad3880  (Adequate.valid adequate Two boolean env4)
  bad3881 : PathP (λ _ → Two) (bop (bop b0 b1) (bop (bop b0 (bop b1 b0)) b1)) b0 → ⊥
  bad3881  p = false≢true (sym (cong lower p))
  cut3881 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 2) (op (var 1) (var 0))) (var 1))) , (var 0)) → ⊥
  cut3881  adequate = bad3881  (Adequate.valid adequate Two boolean env5)
  bad3882 : PathP (λ _ → Two) (bop (bop b0 b1) (bop (bop b1 (bop b1 b0)) b1)) b1 → ⊥
  bad3882  p = false≢true (cong lower p)
  cut3882 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 2) (op (var 1) (var 0))) (var 1))) , (var 1)) → ⊥
  cut3882  adequate = bad3882  (Adequate.valid adequate Two boolean env8)
  bad3883 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b1 (bop b0 b0)) b0)) b1 → ⊥
  bad3883  p = false≢true (cong lower p)
  cut3883 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 2) (op (var 1) (var 0))) (var 1))) , (var 2)) → ⊥
  cut3883  adequate = bad3883  (Adequate.valid adequate Two boolean env2)
  bad3884 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b0 (bop b0 b0)) b0)) b1 → ⊥
  bad3884  p = false≢true (cong lower p)
  cut3884 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 2) (op (var 1) (var 0))) (var 1))) , (var 3)) → ⊥
  cut3884  adequate = bad3884  (Adequate.valid adequate Two boolean env4)
  bad3885 : PathP (λ _ → Two) (bop (bop b1 b0) (bop (bop b0 (bop b0 b1)) b0)) b1 → ⊥
  bad3885  p = false≢true (cong lower p)
  cut3885 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 2) (op (var 1) (var 0))) (var 2))) , (var 0)) → ⊥
  cut3885  adequate = bad3885  (Adequate.valid adequate Two boolean env3)
  bad3886 : PathP (λ _ → Two) (bop (bop b0 b1) (bop (bop b0 (bop b1 b0)) b0)) b1 → ⊥
  bad3886  p = false≢true (cong lower p)
  cut3886 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 2) (op (var 1) (var 0))) (var 2))) , (var 1)) → ⊥
  cut3886  adequate = bad3886  (Adequate.valid adequate Two boolean env5)
  bad3887 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b1 (bop b0 b0)) b1)) b1 → ⊥
  bad3887  p = false≢true (cong lower p)
  cut3887 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 2) (op (var 1) (var 0))) (var 2))) , (var 2)) → ⊥
  cut3887  adequate = bad3887  (Adequate.valid adequate Two boolean env2)
  bad3888 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b0 (bop b0 b0)) b0)) b1 → ⊥
  bad3888  p = false≢true (cong lower p)
  cut3888 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 2) (op (var 1) (var 0))) (var 2))) , (var 3)) → ⊥
  cut3888  adequate = bad3888  (Adequate.valid adequate Two boolean env4)
  bad3889 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b0 (bop b0 b0)) b1)) b0 → ⊥
  bad3889  p = false≢true (sym (cong lower p))
  cut3889 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 2) (op (var 1) (var 0))) (var 3))) , (var 0)) → ⊥
  cut3889  adequate = bad3889  (Adequate.valid adequate Two boolean env4)
  bad3890 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b0 (bop b0 b0)) b1)) b0 → ⊥
  bad3890  p = false≢true (sym (cong lower p))
  cut3890 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 2) (op (var 1) (var 0))) (var 3))) , (var 1)) → ⊥
  cut3890  adequate = bad3890  (Adequate.valid adequate Two boolean env4)
  bad3891 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b0 (bop b0 b0)) b1)) b0 → ⊥
  bad3891  p = false≢true (sym (cong lower p))
  cut3891 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 2) (op (var 1) (var 0))) (var 3))) , (var 2)) → ⊥
  cut3891  adequate = bad3891  (Adequate.valid adequate Two boolean env4)
  bad3892 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b1 (bop b0 b0)) b1)) b1 → ⊥
  bad3892  p = false≢true (cong lower p)
  cut3892 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 2) (op (var 1) (var 0))) (var 3))) , (var 3)) → ⊥
  cut3892  adequate = bad3892  (Adequate.valid adequate Two boolean env21)
  bad3893 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b0 (bop b0 b0)) b0)) b1 → ⊥
  bad3893  p = false≢true (cong lower p)
  cut3893 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 2) (op (var 1) (var 0))) (var 3))) , (var 4)) → ⊥
  cut3893  adequate = bad3893  (Adequate.valid adequate Two boolean env7)
  bad3894 : PathP (λ _ → Two) (bop (bop b1 b0) (bop (bop b1 (bop b0 b0)) b1)) b1 → ⊥
  bad3894  p = false≢true (cong lower p)
  cut3894 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 2) (op (var 1) (var 1))) (var 0))) , (var 0)) → ⊥
  cut3894  adequate = bad3894  (Adequate.valid adequate Two boolean env17)
  bad3895 : PathP (λ _ → Two) (bop (bop b0 b1) (bop (bop b0 (bop b1 b1)) b0)) b1 → ⊥
  bad3895  p = false≢true (cong lower p)
  cut3895 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 2) (op (var 1) (var 1))) (var 0))) , (var 1)) → ⊥
  cut3895  adequate = bad3895  (Adequate.valid adequate Two boolean env5)
  bad3896 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b1 (bop b0 b0)) b0)) b1 → ⊥
  bad3896  p = false≢true (cong lower p)
  cut3896 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 2) (op (var 1) (var 1))) (var 0))) , (var 2)) → ⊥
  cut3896  adequate = bad3896  (Adequate.valid adequate Two boolean env2)
  bad3897 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b0 (bop b0 b0)) b0)) b1 → ⊥
  bad3897  p = false≢true (cong lower p)
  cut3897 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 2) (op (var 1) (var 1))) (var 0))) , (var 3)) → ⊥
  cut3897  adequate = bad3897  (Adequate.valid adequate Two boolean env4)
  bad3898 : PathP (λ _ → Two) (bop (bop b0 b1) (bop (bop b0 (bop b1 b1)) b1)) b0 → ⊥
  bad3898  p = false≢true (sym (cong lower p))
  cut3898 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 2) (op (var 1) (var 1))) (var 1))) , (var 0)) → ⊥
  cut3898  adequate = bad3898  (Adequate.valid adequate Two boolean env5)
  holds3899 : (z0 z1 z2 : A3) → (mul3 (mul3 z0 z1) (mul3 (mul3 z2 (mul3 z1 z1)) z1)) ≡ z1
  holds3899 z0 z1 z2 = refl
  cut3899 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 2) (op (var 1) (var 1))) (var 1))) , (var 1)) → ⊥
  cut3899  = reject3 ((op (op (var 0) (var 1)) (op (op (var 2) (op (var 1) (var 1))) (var 1))) , (var 1)) (λ env → holds3899 (env 0) (env 1) (env 2))
  bad3900 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b1 (bop b0 b0)) b0)) b1 → ⊥
  bad3900  p = false≢true (cong lower p)
  cut3900 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 2) (op (var 1) (var 1))) (var 1))) , (var 2)) → ⊥
  cut3900  adequate = bad3900  (Adequate.valid adequate Two boolean env2)
  bad3901 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b0 (bop b0 b0)) b0)) b1 → ⊥
  bad3901  p = false≢true (cong lower p)
  cut3901 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 2) (op (var 1) (var 1))) (var 1))) , (var 3)) → ⊥
  cut3901  adequate = bad3901  (Adequate.valid adequate Two boolean env4)
  bad3902 : PathP (λ _ → Two) (bop (bop b0 b1) (bop (bop b1 (bop b1 b1)) b1)) b0 → ⊥
  bad3902  p = false≢true (sym (cong lower p))
  cut3902 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 2) (op (var 1) (var 1))) (var 2))) , (var 0)) → ⊥
  cut3902  adequate = bad3902  (Adequate.valid adequate Two boolean env8)
  bad3903 : PathP (λ _ → Two) (bop (bop b0 b1) (bop (bop b0 (bop b1 b1)) b0)) b1 → ⊥
  bad3903  p = false≢true (cong lower p)
  cut3903 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 2) (op (var 1) (var 1))) (var 2))) , (var 1)) → ⊥
  cut3903  adequate = bad3903  (Adequate.valid adequate Two boolean env5)
  bad3904 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b1 (bop b0 b0)) b1)) b1 → ⊥
  bad3904  p = false≢true (cong lower p)
  cut3904 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 2) (op (var 1) (var 1))) (var 2))) , (var 2)) → ⊥
  cut3904  adequate = bad3904  (Adequate.valid adequate Two boolean env2)
  bad3905 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b0 (bop b0 b0)) b0)) b1 → ⊥
  bad3905  p = false≢true (cong lower p)
  cut3905 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 2) (op (var 1) (var 1))) (var 2))) , (var 3)) → ⊥
  cut3905  adequate = bad3905  (Adequate.valid adequate Two boolean env4)
  bad3906 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b0 (bop b0 b0)) b1)) b0 → ⊥
  bad3906  p = false≢true (sym (cong lower p))
  cut3906 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 2) (op (var 1) (var 1))) (var 3))) , (var 0)) → ⊥
  cut3906  adequate = bad3906  (Adequate.valid adequate Two boolean env4)
  bad3907 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b0 (bop b0 b0)) b1)) b0 → ⊥
  bad3907  p = false≢true (sym (cong lower p))
  cut3907 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 2) (op (var 1) (var 1))) (var 3))) , (var 1)) → ⊥
  cut3907  adequate = bad3907  (Adequate.valid adequate Two boolean env4)
  bad3908 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b0 (bop b0 b0)) b1)) b0 → ⊥
  bad3908  p = false≢true (sym (cong lower p))
  cut3908 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 2) (op (var 1) (var 1))) (var 3))) , (var 2)) → ⊥
  cut3908  adequate = bad3908  (Adequate.valid adequate Two boolean env4)
  bad3909 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b1 (bop b0 b0)) b1)) b1 → ⊥
  bad3909  p = false≢true (cong lower p)
  cut3909 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 2) (op (var 1) (var 1))) (var 3))) , (var 3)) → ⊥
  cut3909  adequate = bad3909  (Adequate.valid adequate Two boolean env21)
  bad3910 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b0 (bop b0 b0)) b0)) b1 → ⊥
  bad3910  p = false≢true (cong lower p)
  cut3910 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 2) (op (var 1) (var 1))) (var 3))) , (var 4)) → ⊥
  cut3910  adequate = bad3910  (Adequate.valid adequate Two boolean env7)
  bad3911 : PathP (λ _ → Two) (bop (bop b1 b0) (bop (bop b1 (bop b0 b1)) b1)) b1 → ⊥
  bad3911  p = false≢true (cong lower p)
  cut3911 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 2) (op (var 1) (var 2))) (var 0))) , (var 0)) → ⊥
  cut3911  adequate = bad3911  (Adequate.valid adequate Two boolean env17)
  bad3912 : PathP (λ _ → Two) (bop (bop b0 b1) (bop (bop b0 (bop b1 b0)) b0)) b1 → ⊥
  bad3912  p = false≢true (cong lower p)
  cut3912 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 2) (op (var 1) (var 2))) (var 0))) , (var 1)) → ⊥
  cut3912  adequate = bad3912  (Adequate.valid adequate Two boolean env5)
  bad3913 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b1 (bop b0 b1)) b0)) b1 → ⊥
  bad3913  p = false≢true (cong lower p)
  cut3913 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 2) (op (var 1) (var 2))) (var 0))) , (var 2)) → ⊥
  cut3913  adequate = bad3913  (Adequate.valid adequate Two boolean env2)
  bad3914 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b0 (bop b0 b0)) b0)) b1 → ⊥
  bad3914  p = false≢true (cong lower p)
  cut3914 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 2) (op (var 1) (var 2))) (var 0))) , (var 3)) → ⊥
  cut3914  adequate = bad3914  (Adequate.valid adequate Two boolean env4)
  bad3915 : PathP (λ _ → Two) (bop (bop b0 b1) (bop (bop b0 (bop b1 b0)) b1)) b0 → ⊥
  bad3915  p = false≢true (sym (cong lower p))
  cut3915 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 2) (op (var 1) (var 2))) (var 1))) , (var 0)) → ⊥
  cut3915  adequate = bad3915  (Adequate.valid adequate Two boolean env5)
  holds3916 : (z0 z1 z2 : A3) → (mul3 (mul3 z0 z1) (mul3 (mul3 z2 (mul3 z1 z2)) z1)) ≡ z1
  holds3916 z0 z1 z2 = refl
  cut3916 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 2) (op (var 1) (var 2))) (var 1))) , (var 1)) → ⊥
  cut3916  = reject3 ((op (op (var 0) (var 1)) (op (op (var 2) (op (var 1) (var 2))) (var 1))) , (var 1)) (λ env → holds3916 (env 0) (env 1) (env 2))
  bad3917 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b1 (bop b0 b1)) b0)) b1 → ⊥
  bad3917  p = false≢true (cong lower p)
  cut3917 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 2) (op (var 1) (var 2))) (var 1))) , (var 2)) → ⊥
  cut3917  adequate = bad3917  (Adequate.valid adequate Two boolean env2)
  bad3918 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b0 (bop b0 b0)) b0)) b1 → ⊥
  bad3918  p = false≢true (cong lower p)
  cut3918 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 2) (op (var 1) (var 2))) (var 1))) , (var 3)) → ⊥
  cut3918  adequate = bad3918  (Adequate.valid adequate Two boolean env4)
  bad3919 : PathP (λ _ → Two) (bop (bop b0 b1) (bop (bop b1 (bop b1 b1)) b1)) b0 → ⊥
  bad3919  p = false≢true (sym (cong lower p))
  cut3919 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 2) (op (var 1) (var 2))) (var 2))) , (var 0)) → ⊥
  cut3919  adequate = bad3919  (Adequate.valid adequate Two boolean env8)
  bad3920 : PathP (λ _ → Two) (bop (bop b0 b1) (bop (bop b0 (bop b1 b0)) b0)) b1 → ⊥
  bad3920  p = false≢true (cong lower p)
  cut3920 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 2) (op (var 1) (var 2))) (var 2))) , (var 1)) → ⊥
  cut3920  adequate = bad3920  (Adequate.valid adequate Two boolean env5)
  bad3921 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b1 (bop b0 b1)) b1)) b1 → ⊥
  bad3921  p = false≢true (cong lower p)
  cut3921 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 2) (op (var 1) (var 2))) (var 2))) , (var 2)) → ⊥
  cut3921  adequate = bad3921  (Adequate.valid adequate Two boolean env2)
  bad3922 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b0 (bop b0 b0)) b0)) b1 → ⊥
  bad3922  p = false≢true (cong lower p)
  cut3922 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 2) (op (var 1) (var 2))) (var 2))) , (var 3)) → ⊥
  cut3922  adequate = bad3922  (Adequate.valid adequate Two boolean env4)
  bad3923 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b0 (bop b0 b0)) b1)) b0 → ⊥
  bad3923  p = false≢true (sym (cong lower p))
  cut3923 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 2) (op (var 1) (var 2))) (var 3))) , (var 0)) → ⊥
  cut3923  adequate = bad3923  (Adequate.valid adequate Two boolean env4)
  bad3924 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b0 (bop b0 b0)) b1)) b0 → ⊥
  bad3924  p = false≢true (sym (cong lower p))
  cut3924 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 2) (op (var 1) (var 2))) (var 3))) , (var 1)) → ⊥
  cut3924  adequate = bad3924  (Adequate.valid adequate Two boolean env4)
  bad3925 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b0 (bop b0 b0)) b1)) b0 → ⊥
  bad3925  p = false≢true (sym (cong lower p))
  cut3925 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 2) (op (var 1) (var 2))) (var 3))) , (var 2)) → ⊥
  cut3925  adequate = bad3925  (Adequate.valid adequate Two boolean env4)
  bad3926 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b1 (bop b0 b1)) b1)) b1 → ⊥
  bad3926  p = false≢true (cong lower p)
  cut3926 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 2) (op (var 1) (var 2))) (var 3))) , (var 3)) → ⊥
  cut3926  adequate = bad3926  (Adequate.valid adequate Two boolean env21)
  bad3927 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b0 (bop b0 b0)) b0)) b1 → ⊥
  bad3927  p = false≢true (cong lower p)
  cut3927 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 2) (op (var 1) (var 2))) (var 3))) , (var 4)) → ⊥
  cut3927  adequate = bad3927  (Adequate.valid adequate Two boolean env7)
  bad3928 : PathP (λ _ → Two) (bop (bop b1 b0) (bop (bop b1 (bop b0 b0)) b1)) b1 → ⊥
  bad3928  p = false≢true (cong lower p)
  cut3928 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 2) (op (var 1) (var 3))) (var 0))) , (var 0)) → ⊥
  cut3928  adequate = bad3928  (Adequate.valid adequate Two boolean env19)
  bad3929 : PathP (λ _ → Two) (bop (bop b0 b1) (bop (bop b0 (bop b1 b0)) b0)) b1 → ⊥
  bad3929  p = false≢true (cong lower p)
  cut3929 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 2) (op (var 1) (var 3))) (var 0))) , (var 1)) → ⊥
  cut3929  adequate = bad3929  (Adequate.valid adequate Two boolean env10)
  bad3930 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b1 (bop b0 b0)) b0)) b1 → ⊥
  bad3930  p = false≢true (cong lower p)
  cut3930 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 2) (op (var 1) (var 3))) (var 0))) , (var 2)) → ⊥
  cut3930  adequate = bad3930  (Adequate.valid adequate Two boolean env11)
  bad3931 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b0 (bop b0 b1)) b0)) b1 → ⊥
  bad3931  p = false≢true (cong lower p)
  cut3931 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 2) (op (var 1) (var 3))) (var 0))) , (var 3)) → ⊥
  cut3931  adequate = bad3931  (Adequate.valid adequate Two boolean env4)
  bad3932 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b0 (bop b0 b0)) b0)) b1 → ⊥
  bad3932  p = false≢true (cong lower p)
  cut3932 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 2) (op (var 1) (var 3))) (var 0))) , (var 4)) → ⊥
  cut3932  adequate = bad3932  (Adequate.valid adequate Two boolean env7)
  bad3933 : PathP (λ _ → Two) (bop (bop b0 b1) (bop (bop b0 (bop b1 b0)) b1)) b0 → ⊥
  bad3933  p = false≢true (sym (cong lower p))
  cut3933 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 2) (op (var 1) (var 3))) (var 1))) , (var 0)) → ⊥
  cut3933  adequate = bad3933  (Adequate.valid adequate Two boolean env10)
  bad3934 : PathP (λ _ → Two) (bop (bop b0 b1) (bop (bop b1 (bop b1 b0)) b1)) b1 → ⊥
  bad3934  p = false≢true (cong lower p)
  cut3934 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 2) (op (var 1) (var 3))) (var 1))) , (var 1)) → ⊥
  cut3934  adequate = bad3934  (Adequate.valid adequate Two boolean env13)
  bad3935 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b1 (bop b0 b0)) b0)) b1 → ⊥
  bad3935  p = false≢true (cong lower p)
  cut3935 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 2) (op (var 1) (var 3))) (var 1))) , (var 2)) → ⊥
  cut3935  adequate = bad3935  (Adequate.valid adequate Two boolean env11)
  bad3936 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b0 (bop b0 b1)) b0)) b1 → ⊥
  bad3936  p = false≢true (cong lower p)
  cut3936 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 2) (op (var 1) (var 3))) (var 1))) , (var 3)) → ⊥
  cut3936  adequate = bad3936  (Adequate.valid adequate Two boolean env4)
  bad3937 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b0 (bop b0 b0)) b0)) b1 → ⊥
  bad3937  p = false≢true (cong lower p)
  cut3937 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 2) (op (var 1) (var 3))) (var 1))) , (var 4)) → ⊥
  cut3937  adequate = bad3937  (Adequate.valid adequate Two boolean env7)
  bad3938 : PathP (λ _ → Two) (bop (bop b0 b1) (bop (bop b1 (bop b1 b1)) b1)) b0 → ⊥
  bad3938  p = false≢true (sym (cong lower p))
  cut3938 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 2) (op (var 1) (var 3))) (var 2))) , (var 0)) → ⊥
  cut3938  adequate = bad3938  (Adequate.valid adequate Two boolean env12)
  bad3939 : PathP (λ _ → Two) (bop (bop b0 b1) (bop (bop b0 (bop b1 b0)) b0)) b1 → ⊥
  bad3939  p = false≢true (cong lower p)
  cut3939 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 2) (op (var 1) (var 3))) (var 2))) , (var 1)) → ⊥
  cut3939  adequate = bad3939  (Adequate.valid adequate Two boolean env10)
  bad3940 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b1 (bop b0 b0)) b1)) b1 → ⊥
  bad3940  p = false≢true (cong lower p)
  cut3940 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 2) (op (var 1) (var 3))) (var 2))) , (var 2)) → ⊥
  cut3940  adequate = bad3940  (Adequate.valid adequate Two boolean env11)
  bad3941 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b0 (bop b0 b1)) b0)) b1 → ⊥
  bad3941  p = false≢true (cong lower p)
  cut3941 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 2) (op (var 1) (var 3))) (var 2))) , (var 3)) → ⊥
  cut3941  adequate = bad3941  (Adequate.valid adequate Two boolean env4)
  bad3942 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b0 (bop b0 b0)) b0)) b1 → ⊥
  bad3942  p = false≢true (cong lower p)
  cut3942 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 2) (op (var 1) (var 3))) (var 2))) , (var 4)) → ⊥
  cut3942  adequate = bad3942  (Adequate.valid adequate Two boolean env7)
  bad3943 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b0 (bop b0 b1)) b1)) b0 → ⊥
  bad3943  p = false≢true (sym (cong lower p))
  cut3943 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 2) (op (var 1) (var 3))) (var 3))) , (var 0)) → ⊥
  cut3943  adequate = bad3943  (Adequate.valid adequate Two boolean env4)
  bad3944 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b0 (bop b0 b1)) b1)) b0 → ⊥
  bad3944  p = false≢true (sym (cong lower p))
  cut3944 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 2) (op (var 1) (var 3))) (var 3))) , (var 1)) → ⊥
  cut3944  adequate = bad3944  (Adequate.valid adequate Two boolean env4)
  bad3945 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b0 (bop b0 b1)) b1)) b0 → ⊥
  bad3945  p = false≢true (sym (cong lower p))
  cut3945 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 2) (op (var 1) (var 3))) (var 3))) , (var 2)) → ⊥
  cut3945  adequate = bad3945  (Adequate.valid adequate Two boolean env4)
  bad3946 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b1 (bop b0 b1)) b1)) b1 → ⊥
  bad3946  p = false≢true (cong lower p)
  cut3946 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 2) (op (var 1) (var 3))) (var 3))) , (var 3)) → ⊥
  cut3946  adequate = bad3946  (Adequate.valid adequate Two boolean env21)
  bad3947 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b0 (bop b0 b0)) b0)) b1 → ⊥
  bad3947  p = false≢true (cong lower p)
  cut3947 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 2) (op (var 1) (var 3))) (var 3))) , (var 4)) → ⊥
  cut3947  adequate = bad3947  (Adequate.valid adequate Two boolean env7)
  bad3948 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b0 (bop b0 b0)) b1)) b0 → ⊥
  bad3948  p = false≢true (sym (cong lower p))
  cut3948 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 2) (op (var 1) (var 3))) (var 4))) , (var 0)) → ⊥
  cut3948  adequate = bad3948  (Adequate.valid adequate Two boolean env7)
  bad3949 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b0 (bop b0 b0)) b1)) b0 → ⊥
  bad3949  p = false≢true (sym (cong lower p))
  cut3949 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 2) (op (var 1) (var 3))) (var 4))) , (var 1)) → ⊥
  cut3949  adequate = bad3949  (Adequate.valid adequate Two boolean env7)
  bad3950 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b0 (bop b0 b0)) b1)) b0 → ⊥
  bad3950  p = false≢true (sym (cong lower p))
  cut3950 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 2) (op (var 1) (var 3))) (var 4))) , (var 2)) → ⊥
  cut3950  adequate = bad3950  (Adequate.valid adequate Two boolean env7)
  bad3951 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b0 (bop b0 b0)) b1)) b0 → ⊥
  bad3951  p = false≢true (sym (cong lower p))
  cut3951 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 2) (op (var 1) (var 3))) (var 4))) , (var 3)) → ⊥
  cut3951  adequate = bad3951  (Adequate.valid adequate Two boolean env7)
  bad3952 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b1 (bop b0 b0)) b1)) b1 → ⊥
  bad3952  p = false≢true (cong lower p)
  cut3952 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 2) (op (var 1) (var 3))) (var 4))) , (var 4)) → ⊥
  cut3952  adequate = bad3952  (Adequate.valid adequate Two boolean env22)
  bad3953 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b0 (bop b0 b0)) b0)) b1 → ⊥
  bad3953  p = false≢true (cong lower p)
  cut3953 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 2) (op (var 1) (var 3))) (var 4))) , (var 5)) → ⊥
  cut3953  adequate = bad3953  (Adequate.valid adequate Two boolean env15)
  holds3954 : (z0 z1 z2 : A2) → (mul2 (mul2 z0 z1) (mul2 (mul2 z2 (mul2 z2 z0)) z0)) ≡ z0
  holds3954 z0 z1 z2 = refl
  cut3954 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 2) (op (var 2) (var 0))) (var 0))) , (var 0)) → ⊥
  cut3954  = reject2 ((op (op (var 0) (var 1)) (op (op (var 2) (op (var 2) (var 0))) (var 0))) , (var 0)) (λ env → holds3954 (env 0) (env 1) (env 2))
  bad3955 : PathP (λ _ → Two) (bop (bop b0 b1) (bop (bop b0 (bop b0 b0)) b0)) b1 → ⊥
  bad3955  p = false≢true (cong lower p)
  cut3955 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 2) (op (var 2) (var 0))) (var 0))) , (var 1)) → ⊥
  cut3955  adequate = bad3955  (Adequate.valid adequate Two boolean env5)
  bad3956 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b1 (bop b1 b0)) b0)) b1 → ⊥
  bad3956  p = false≢true (cong lower p)
  cut3956 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 2) (op (var 2) (var 0))) (var 0))) , (var 2)) → ⊥
  cut3956  adequate = bad3956  (Adequate.valid adequate Two boolean env2)
  bad3957 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b0 (bop b0 b0)) b0)) b1 → ⊥
  bad3957  p = false≢true (cong lower p)
  cut3957 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 2) (op (var 2) (var 0))) (var 0))) , (var 3)) → ⊥
  cut3957  adequate = bad3957  (Adequate.valid adequate Two boolean env4)
  bad3958 : PathP (λ _ → Two) (bop (bop b0 b1) (bop (bop b0 (bop b0 b0)) b1)) b0 → ⊥
  bad3958  p = false≢true (sym (cong lower p))
  cut3958 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 2) (op (var 2) (var 0))) (var 1))) , (var 0)) → ⊥
  cut3958  adequate = bad3958  (Adequate.valid adequate Two boolean env5)
  bad3959 : PathP (λ _ → Two) (bop (bop b0 b1) (bop (bop b1 (bop b1 b0)) b1)) b1 → ⊥
  bad3959  p = false≢true (cong lower p)
  cut3959 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 2) (op (var 2) (var 0))) (var 1))) , (var 1)) → ⊥
  cut3959  adequate = bad3959  (Adequate.valid adequate Two boolean env8)
  bad3960 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b1 (bop b1 b0)) b0)) b1 → ⊥
  bad3960  p = false≢true (cong lower p)
  cut3960 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 2) (op (var 2) (var 0))) (var 1))) , (var 2)) → ⊥
  cut3960  adequate = bad3960  (Adequate.valid adequate Two boolean env2)
  bad3961 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b0 (bop b0 b0)) b0)) b1 → ⊥
  bad3961  p = false≢true (cong lower p)
  cut3961 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 2) (op (var 2) (var 0))) (var 1))) , (var 3)) → ⊥
  cut3961  adequate = bad3961  (Adequate.valid adequate Two boolean env4)
  bad3962 : PathP (λ _ → Two) (bop (bop b1 b0) (bop (bop b0 (bop b0 b1)) b0)) b1 → ⊥
  bad3962  p = false≢true (cong lower p)
  cut3962 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 2) (op (var 2) (var 0))) (var 2))) , (var 0)) → ⊥
  cut3962  adequate = bad3962  (Adequate.valid adequate Two boolean env3)
  bad3963 : PathP (λ _ → Two) (bop (bop b0 b1) (bop (bop b0 (bop b0 b0)) b0)) b1 → ⊥
  bad3963  p = false≢true (cong lower p)
  cut3963 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 2) (op (var 2) (var 0))) (var 2))) , (var 1)) → ⊥
  cut3963  adequate = bad3963  (Adequate.valid adequate Two boolean env5)
  bad3964 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b1 (bop b1 b0)) b1)) b1 → ⊥
  bad3964  p = false≢true (cong lower p)
  cut3964 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 2) (op (var 2) (var 0))) (var 2))) , (var 2)) → ⊥
  cut3964  adequate = bad3964  (Adequate.valid adequate Two boolean env2)
  bad3965 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b0 (bop b0 b0)) b0)) b1 → ⊥
  bad3965  p = false≢true (cong lower p)
  cut3965 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 2) (op (var 2) (var 0))) (var 2))) , (var 3)) → ⊥
  cut3965  adequate = bad3965  (Adequate.valid adequate Two boolean env4)
  bad3966 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b0 (bop b0 b0)) b1)) b0 → ⊥
  bad3966  p = false≢true (sym (cong lower p))
  cut3966 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 2) (op (var 2) (var 0))) (var 3))) , (var 0)) → ⊥
  cut3966  adequate = bad3966  (Adequate.valid adequate Two boolean env4)
  bad3967 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b0 (bop b0 b0)) b1)) b0 → ⊥
  bad3967  p = false≢true (sym (cong lower p))
  cut3967 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 2) (op (var 2) (var 0))) (var 3))) , (var 1)) → ⊥
  cut3967  adequate = bad3967  (Adequate.valid adequate Two boolean env4)
  bad3968 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b0 (bop b0 b0)) b1)) b0 → ⊥
  bad3968  p = false≢true (sym (cong lower p))
  cut3968 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 2) (op (var 2) (var 0))) (var 3))) , (var 2)) → ⊥
  cut3968  adequate = bad3968  (Adequate.valid adequate Two boolean env4)
  bad3969 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b1 (bop b1 b0)) b1)) b1 → ⊥
  bad3969  p = false≢true (cong lower p)
  cut3969 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 2) (op (var 2) (var 0))) (var 3))) , (var 3)) → ⊥
  cut3969  adequate = bad3969  (Adequate.valid adequate Two boolean env21)
  bad3970 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b0 (bop b0 b0)) b0)) b1 → ⊥
  bad3970  p = false≢true (cong lower p)
  cut3970 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 2) (op (var 2) (var 0))) (var 3))) , (var 4)) → ⊥
  cut3970  adequate = bad3970  (Adequate.valid adequate Two boolean env7)
  bad3971 : PathP (λ _ → Two) (bop (bop b1 b0) (bop (bop b1 (bop b1 b0)) b1)) b1 → ⊥
  bad3971  p = false≢true (cong lower p)
  cut3971 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 2) (op (var 2) (var 1))) (var 0))) , (var 0)) → ⊥
  cut3971  adequate = bad3971  (Adequate.valid adequate Two boolean env17)
  bad3972 : PathP (λ _ → Two) (bop (bop b0 b1) (bop (bop b0 (bop b0 b1)) b0)) b1 → ⊥
  bad3972  p = false≢true (cong lower p)
  cut3972 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 2) (op (var 2) (var 1))) (var 0))) , (var 1)) → ⊥
  cut3972  adequate = bad3972  (Adequate.valid adequate Two boolean env5)
  bad3973 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b1 (bop b1 b0)) b0)) b1 → ⊥
  bad3973  p = false≢true (cong lower p)
  cut3973 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 2) (op (var 2) (var 1))) (var 0))) , (var 2)) → ⊥
  cut3973  adequate = bad3973  (Adequate.valid adequate Two boolean env2)
  bad3974 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b0 (bop b0 b0)) b0)) b1 → ⊥
  bad3974  p = false≢true (cong lower p)
  cut3974 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 2) (op (var 2) (var 1))) (var 0))) , (var 3)) → ⊥
  cut3974  adequate = bad3974  (Adequate.valid adequate Two boolean env4)
  bad3975 : PathP (λ _ → Two) (bop (bop b0 b1) (bop (bop b0 (bop b0 b1)) b1)) b0 → ⊥
  bad3975  p = false≢true (sym (cong lower p))
  cut3975 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 2) (op (var 2) (var 1))) (var 1))) , (var 0)) → ⊥
  cut3975  adequate = bad3975  (Adequate.valid adequate Two boolean env5)
  holds3976 : (z0 z1 z2 : A3) → (mul3 (mul3 z0 z1) (mul3 (mul3 z2 (mul3 z2 z1)) z1)) ≡ z1
  holds3976 z0 z1 z2 = refl
  cut3976 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 2) (op (var 2) (var 1))) (var 1))) , (var 1)) → ⊥
  cut3976  = reject3 ((op (op (var 0) (var 1)) (op (op (var 2) (op (var 2) (var 1))) (var 1))) , (var 1)) (λ env → holds3976 (env 0) (env 1) (env 2))
  bad3977 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b1 (bop b1 b0)) b0)) b1 → ⊥
  bad3977  p = false≢true (cong lower p)
  cut3977 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 2) (op (var 2) (var 1))) (var 1))) , (var 2)) → ⊥
  cut3977  adequate = bad3977  (Adequate.valid adequate Two boolean env2)
  bad3978 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b0 (bop b0 b0)) b0)) b1 → ⊥
  bad3978  p = false≢true (cong lower p)
  cut3978 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 2) (op (var 2) (var 1))) (var 1))) , (var 3)) → ⊥
  cut3978  adequate = bad3978  (Adequate.valid adequate Two boolean env4)
  bad3979 : PathP (λ _ → Two) (bop (bop b0 b1) (bop (bop b1 (bop b1 b1)) b1)) b0 → ⊥
  bad3979  p = false≢true (sym (cong lower p))
  cut3979 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 2) (op (var 2) (var 1))) (var 2))) , (var 0)) → ⊥
  cut3979  adequate = bad3979  (Adequate.valid adequate Two boolean env8)
  bad3980 : PathP (λ _ → Two) (bop (bop b0 b1) (bop (bop b0 (bop b0 b1)) b0)) b1 → ⊥
  bad3980  p = false≢true (cong lower p)
  cut3980 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 2) (op (var 2) (var 1))) (var 2))) , (var 1)) → ⊥
  cut3980  adequate = bad3980  (Adequate.valid adequate Two boolean env5)
  bad3981 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b1 (bop b1 b0)) b1)) b1 → ⊥
  bad3981  p = false≢true (cong lower p)
  cut3981 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 2) (op (var 2) (var 1))) (var 2))) , (var 2)) → ⊥
  cut3981  adequate = bad3981  (Adequate.valid adequate Two boolean env2)
  bad3982 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b0 (bop b0 b0)) b0)) b1 → ⊥
  bad3982  p = false≢true (cong lower p)
  cut3982 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 2) (op (var 2) (var 1))) (var 2))) , (var 3)) → ⊥
  cut3982  adequate = bad3982  (Adequate.valid adequate Two boolean env4)
  bad3983 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b0 (bop b0 b0)) b1)) b0 → ⊥
  bad3983  p = false≢true (sym (cong lower p))
  cut3983 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 2) (op (var 2) (var 1))) (var 3))) , (var 0)) → ⊥
  cut3983  adequate = bad3983  (Adequate.valid adequate Two boolean env4)
  bad3984 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b0 (bop b0 b0)) b1)) b0 → ⊥
  bad3984  p = false≢true (sym (cong lower p))
  cut3984 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 2) (op (var 2) (var 1))) (var 3))) , (var 1)) → ⊥
  cut3984  adequate = bad3984  (Adequate.valid adequate Two boolean env4)
  bad3985 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b0 (bop b0 b0)) b1)) b0 → ⊥
  bad3985  p = false≢true (sym (cong lower p))
  cut3985 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 2) (op (var 2) (var 1))) (var 3))) , (var 2)) → ⊥
  cut3985  adequate = bad3985  (Adequate.valid adequate Two boolean env4)
  bad3986 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b1 (bop b1 b0)) b1)) b1 → ⊥
  bad3986  p = false≢true (cong lower p)
  cut3986 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 2) (op (var 2) (var 1))) (var 3))) , (var 3)) → ⊥
  cut3986  adequate = bad3986  (Adequate.valid adequate Two boolean env21)
  bad3987 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b0 (bop b0 b0)) b0)) b1 → ⊥
  bad3987  p = false≢true (cong lower p)
  cut3987 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 2) (op (var 2) (var 1))) (var 3))) , (var 4)) → ⊥
  cut3987  adequate = bad3987  (Adequate.valid adequate Two boolean env7)
  holds3988 : (z0 z1 z2 : A2) → (mul2 (mul2 z0 z1) (mul2 (mul2 z2 (mul2 z2 z2)) z0)) ≡ z0
  holds3988 z0 z1 z2 = refl
  cut3988 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 2) (op (var 2) (var 2))) (var 0))) , (var 0)) → ⊥
  cut3988  = reject2 ((op (op (var 0) (var 1)) (op (op (var 2) (op (var 2) (var 2))) (var 0))) , (var 0)) (λ env → holds3988 (env 0) (env 1) (env 2))
  bad3989 : PathP (λ _ → Two) (bop (bop b0 b1) (bop (bop b0 (bop b0 b0)) b0)) b1 → ⊥
  bad3989  p = false≢true (cong lower p)
  cut3989 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 2) (op (var 2) (var 2))) (var 0))) , (var 1)) → ⊥
  cut3989  adequate = bad3989  (Adequate.valid adequate Two boolean env5)
  bad3990 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b1 (bop b1 b1)) b0)) b1 → ⊥
  bad3990  p = false≢true (cong lower p)
  cut3990 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 2) (op (var 2) (var 2))) (var 0))) , (var 2)) → ⊥
  cut3990  adequate = bad3990  (Adequate.valid adequate Two boolean env2)
  bad3991 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b0 (bop b0 b0)) b0)) b1 → ⊥
  bad3991  p = false≢true (cong lower p)
  cut3991 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 2) (op (var 2) (var 2))) (var 0))) , (var 3)) → ⊥
  cut3991  adequate = bad3991  (Adequate.valid adequate Two boolean env4)
  bad3992 : PathP (λ _ → Two) (bop (bop b0 b1) (bop (bop b0 (bop b0 b0)) b1)) b0 → ⊥
  bad3992  p = false≢true (sym (cong lower p))
  cut3992 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 2) (op (var 2) (var 2))) (var 1))) , (var 0)) → ⊥
  cut3992  adequate = bad3992  (Adequate.valid adequate Two boolean env5)
  holds3993 : (z0 z1 z2 : A3) → (mul3 (mul3 z0 z1) (mul3 (mul3 z2 (mul3 z2 z2)) z1)) ≡ z1
  holds3993 z0 z1 z2 = refl
  cut3993 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 2) (op (var 2) (var 2))) (var 1))) , (var 1)) → ⊥
  cut3993  = reject3 ((op (op (var 0) (var 1)) (op (op (var 2) (op (var 2) (var 2))) (var 1))) , (var 1)) (λ env → holds3993 (env 0) (env 1) (env 2))
  bad3994 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b1 (bop b1 b1)) b0)) b1 → ⊥
  bad3994  p = false≢true (cong lower p)
  cut3994 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 2) (op (var 2) (var 2))) (var 1))) , (var 2)) → ⊥
  cut3994  adequate = bad3994  (Adequate.valid adequate Two boolean env2)
  bad3995 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b0 (bop b0 b0)) b0)) b1 → ⊥
  bad3995  p = false≢true (cong lower p)
  cut3995 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 2) (op (var 2) (var 2))) (var 1))) , (var 3)) → ⊥
  cut3995  adequate = bad3995  (Adequate.valid adequate Two boolean env4)
  bad3996 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b1 (bop b1 b1)) b1)) b0 → ⊥
  bad3996  p = false≢true (sym (cong lower p))
  cut3996 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 2) (op (var 2) (var 2))) (var 2))) , (var 0)) → ⊥
  cut3996  adequate = bad3996  (Adequate.valid adequate Two boolean env2)
  bad3997 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b1 (bop b1 b1)) b1)) b0 → ⊥
  bad3997  p = false≢true (sym (cong lower p))
  cut3997 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 2) (op (var 2) (var 2))) (var 2))) , (var 1)) → ⊥
  cut3997  adequate = bad3997  (Adequate.valid adequate Two boolean env2)
  bad3998 : PathP (λ _ → Two) (bop (bop b1 b1) (bop (bop b0 (bop b0 b0)) b0)) b0 → ⊥
  bad3998  p = false≢true (sym (cong lower p))
  cut3998 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 2) (op (var 2) (var 2))) (var 2))) , (var 2)) → ⊥
  cut3998  adequate = bad3998  (Adequate.valid adequate Two boolean env16)
  bad3999 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b0 (bop b0 b0)) b0)) b1 → ⊥
  bad3999  p = false≢true (cong lower p)
  cut3999 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 2) (op (var 2) (var 2))) (var 2))) , (var 3)) → ⊥
  cut3999  adequate = bad3999  (Adequate.valid adequate Two boolean env4)
  bad4000 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b0 (bop b0 b0)) b1)) b0 → ⊥
  bad4000  p = false≢true (sym (cong lower p))
  cut4000 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 2) (op (var 2) (var 2))) (var 3))) , (var 0)) → ⊥
  cut4000  adequate = bad4000  (Adequate.valid adequate Two boolean env4)
  bad4001 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b0 (bop b0 b0)) b1)) b0 → ⊥
  bad4001  p = false≢true (sym (cong lower p))
  cut4001 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 2) (op (var 2) (var 2))) (var 3))) , (var 1)) → ⊥
  cut4001  adequate = bad4001  (Adequate.valid adequate Two boolean env4)
  bad4002 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b0 (bop b0 b0)) b1)) b0 → ⊥
  bad4002  p = false≢true (sym (cong lower p))
  cut4002 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 2) (op (var 2) (var 2))) (var 3))) , (var 2)) → ⊥
  cut4002  adequate = bad4002  (Adequate.valid adequate Two boolean env4)
  env23 : ℕ → Two
  env23 zero = b1
  env23 (suc zero) = b1
  env23 (suc (suc zero)) = b0
  env23 (suc (suc (suc zero))) = b0
  env23 (suc (suc (suc (suc rest)))) = b0
  bad4003 : PathP (λ _ → Two) (bop (bop b1 b1) (bop (bop b0 (bop b0 b0)) b0)) b0 → ⊥
  bad4003  p = false≢true (sym (cong lower p))
  cut4003 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 2) (op (var 2) (var 2))) (var 3))) , (var 3)) → ⊥
  cut4003  adequate = bad4003  (Adequate.valid adequate Two boolean env23)
  bad4004 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b0 (bop b0 b0)) b0)) b1 → ⊥
  bad4004  p = false≢true (cong lower p)
  cut4004 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 2) (op (var 2) (var 2))) (var 3))) , (var 4)) → ⊥
  cut4004  adequate = bad4004  (Adequate.valid adequate Two boolean env7)
  bad4005 : PathP (λ _ → Two) (bop (bop b1 b0) (bop (bop b1 (bop b1 b0)) b1)) b1 → ⊥
  bad4005  p = false≢true (cong lower p)
  cut4005 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 2) (op (var 2) (var 3))) (var 0))) , (var 0)) → ⊥
  cut4005  adequate = bad4005  (Adequate.valid adequate Two boolean env19)
  bad4006 : PathP (λ _ → Two) (bop (bop b0 b1) (bop (bop b0 (bop b0 b0)) b0)) b1 → ⊥
  bad4006  p = false≢true (cong lower p)
  cut4006 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 2) (op (var 2) (var 3))) (var 0))) , (var 1)) → ⊥
  cut4006  adequate = bad4006  (Adequate.valid adequate Two boolean env10)
  bad4007 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b1 (bop b1 b0)) b0)) b1 → ⊥
  bad4007  p = false≢true (cong lower p)
  cut4007 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 2) (op (var 2) (var 3))) (var 0))) , (var 2)) → ⊥
  cut4007  adequate = bad4007  (Adequate.valid adequate Two boolean env11)
  bad4008 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b0 (bop b0 b1)) b0)) b1 → ⊥
  bad4008  p = false≢true (cong lower p)
  cut4008 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 2) (op (var 2) (var 3))) (var 0))) , (var 3)) → ⊥
  cut4008  adequate = bad4008  (Adequate.valid adequate Two boolean env4)
  bad4009 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b0 (bop b0 b0)) b0)) b1 → ⊥
  bad4009  p = false≢true (cong lower p)
  cut4009 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 2) (op (var 2) (var 3))) (var 0))) , (var 4)) → ⊥
  cut4009  adequate = bad4009  (Adequate.valid adequate Two boolean env7)
  bad4010 : PathP (λ _ → Two) (bop (bop b0 b1) (bop (bop b0 (bop b0 b0)) b1)) b0 → ⊥
  bad4010  p = false≢true (sym (cong lower p))
  cut4010 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 2) (op (var 2) (var 3))) (var 1))) , (var 0)) → ⊥
  cut4010  adequate = bad4010  (Adequate.valid adequate Two boolean env10)
  bad4011 : PathP (λ _ → Two) (bop (bop b0 b1) (bop (bop b1 (bop b1 b0)) b1)) b1 → ⊥
  bad4011  p = false≢true (cong lower p)
  cut4011 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 2) (op (var 2) (var 3))) (var 1))) , (var 1)) → ⊥
  cut4011  adequate = bad4011  (Adequate.valid adequate Two boolean env13)
  bad4012 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b1 (bop b1 b0)) b0)) b1 → ⊥
  bad4012  p = false≢true (cong lower p)
  cut4012 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 2) (op (var 2) (var 3))) (var 1))) , (var 2)) → ⊥
  cut4012  adequate = bad4012  (Adequate.valid adequate Two boolean env11)
  bad4013 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b0 (bop b0 b1)) b0)) b1 → ⊥
  bad4013  p = false≢true (cong lower p)
  cut4013 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 2) (op (var 2) (var 3))) (var 1))) , (var 3)) → ⊥
  cut4013  adequate = bad4013  (Adequate.valid adequate Two boolean env4)
  bad4014 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b0 (bop b0 b0)) b0)) b1 → ⊥
  bad4014  p = false≢true (cong lower p)
  cut4014 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 2) (op (var 2) (var 3))) (var 1))) , (var 4)) → ⊥
  cut4014  adequate = bad4014  (Adequate.valid adequate Two boolean env7)
  bad4015 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b1 (bop b1 b1)) b1)) b0 → ⊥
  bad4015  p = false≢true (sym (cong lower p))
  cut4015 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 2) (op (var 2) (var 3))) (var 2))) , (var 0)) → ⊥
  cut4015  adequate = bad4015  (Adequate.valid adequate Two boolean env21)
  bad4016 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b1 (bop b1 b1)) b1)) b0 → ⊥
  bad4016  p = false≢true (sym (cong lower p))
  cut4016 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 2) (op (var 2) (var 3))) (var 2))) , (var 1)) → ⊥
  cut4016  adequate = bad4016  (Adequate.valid adequate Two boolean env21)
  bad4017 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b1 (bop b1 b0)) b1)) b1 → ⊥
  bad4017  p = false≢true (cong lower p)
  cut4017 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 2) (op (var 2) (var 3))) (var 2))) , (var 2)) → ⊥
  cut4017  adequate = bad4017  (Adequate.valid adequate Two boolean env11)
  bad4018 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b0 (bop b0 b1)) b0)) b1 → ⊥
  bad4018  p = false≢true (cong lower p)
  cut4018 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 2) (op (var 2) (var 3))) (var 2))) , (var 3)) → ⊥
  cut4018  adequate = bad4018  (Adequate.valid adequate Two boolean env4)
  bad4019 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b0 (bop b0 b0)) b0)) b1 → ⊥
  bad4019  p = false≢true (cong lower p)
  cut4019 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 2) (op (var 2) (var 3))) (var 2))) , (var 4)) → ⊥
  cut4019  adequate = bad4019  (Adequate.valid adequate Two boolean env7)
  bad4020 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b0 (bop b0 b1)) b1)) b0 → ⊥
  bad4020  p = false≢true (sym (cong lower p))
  cut4020 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 2) (op (var 2) (var 3))) (var 3))) , (var 0)) → ⊥
  cut4020  adequate = bad4020  (Adequate.valid adequate Two boolean env4)
  bad4021 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b0 (bop b0 b1)) b1)) b0 → ⊥
  bad4021  p = false≢true (sym (cong lower p))
  cut4021 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 2) (op (var 2) (var 3))) (var 3))) , (var 1)) → ⊥
  cut4021  adequate = bad4021  (Adequate.valid adequate Two boolean env4)
  bad4022 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b0 (bop b0 b1)) b1)) b0 → ⊥
  bad4022  p = false≢true (sym (cong lower p))
  cut4022 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 2) (op (var 2) (var 3))) (var 3))) , (var 2)) → ⊥
  cut4022  adequate = bad4022  (Adequate.valid adequate Two boolean env4)
  bad4023 : PathP (λ _ → Two) (bop (bop b1 b1) (bop (bop b0 (bop b0 b0)) b0)) b0 → ⊥
  bad4023  p = false≢true (sym (cong lower p))
  cut4023 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 2) (op (var 2) (var 3))) (var 3))) , (var 3)) → ⊥
  cut4023  adequate = bad4023  (Adequate.valid adequate Two boolean env23)
  bad4024 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b0 (bop b0 b0)) b0)) b1 → ⊥
  bad4024  p = false≢true (cong lower p)
  cut4024 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 2) (op (var 2) (var 3))) (var 3))) , (var 4)) → ⊥
  cut4024  adequate = bad4024  (Adequate.valid adequate Two boolean env7)
  bad4025 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b0 (bop b0 b0)) b1)) b0 → ⊥
  bad4025  p = false≢true (sym (cong lower p))
  cut4025 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 2) (op (var 2) (var 3))) (var 4))) , (var 0)) → ⊥
  cut4025  adequate = bad4025  (Adequate.valid adequate Two boolean env7)
  bad4026 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b0 (bop b0 b0)) b1)) b0 → ⊥
  bad4026  p = false≢true (sym (cong lower p))
  cut4026 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 2) (op (var 2) (var 3))) (var 4))) , (var 1)) → ⊥
  cut4026  adequate = bad4026  (Adequate.valid adequate Two boolean env7)
  bad4027 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b0 (bop b0 b0)) b1)) b0 → ⊥
  bad4027  p = false≢true (sym (cong lower p))
  cut4027 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 2) (op (var 2) (var 3))) (var 4))) , (var 2)) → ⊥
  cut4027  adequate = bad4027  (Adequate.valid adequate Two boolean env7)
  bad4028 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b0 (bop b0 b0)) b1)) b0 → ⊥
  bad4028  p = false≢true (sym (cong lower p))
  cut4028 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 2) (op (var 2) (var 3))) (var 4))) , (var 3)) → ⊥
  cut4028  adequate = bad4028  (Adequate.valid adequate Two boolean env7)
  bad4029 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b1 (bop b1 b0)) b1)) b1 → ⊥
  bad4029  p = false≢true (cong lower p)
  cut4029 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 2) (op (var 2) (var 3))) (var 4))) , (var 4)) → ⊥
  cut4029  adequate = bad4029  (Adequate.valid adequate Two boolean env22)
  bad4030 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b0 (bop b0 b0)) b0)) b1 → ⊥
  bad4030  p = false≢true (cong lower p)
  cut4030 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 2) (op (var 2) (var 3))) (var 4))) , (var 5)) → ⊥
  cut4030  adequate = bad4030  (Adequate.valid adequate Two boolean env15)
  bad4031 : PathP (λ _ → Two) (bop (bop b1 b0) (bop (bop b1 (bop b0 b1)) b1)) b1 → ⊥
  bad4031  p = false≢true (cong lower p)
  cut4031 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 2) (op (var 3) (var 0))) (var 0))) , (var 0)) → ⊥
  cut4031  adequate = bad4031  (Adequate.valid adequate Two boolean env19)
  bad4032 : PathP (λ _ → Two) (bop (bop b0 b1) (bop (bop b0 (bop b0 b0)) b0)) b1 → ⊥
  bad4032  p = false≢true (cong lower p)
  cut4032 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 2) (op (var 3) (var 0))) (var 0))) , (var 1)) → ⊥
  cut4032  adequate = bad4032  (Adequate.valid adequate Two boolean env10)
  bad4033 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b1 (bop b0 b0)) b0)) b1 → ⊥
  bad4033  p = false≢true (cong lower p)
  cut4033 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 2) (op (var 3) (var 0))) (var 0))) , (var 2)) → ⊥
  cut4033  adequate = bad4033  (Adequate.valid adequate Two boolean env11)
  bad4034 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b0 (bop b1 b0)) b0)) b1 → ⊥
  bad4034  p = false≢true (cong lower p)
  cut4034 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 2) (op (var 3) (var 0))) (var 0))) , (var 3)) → ⊥
  cut4034  adequate = bad4034  (Adequate.valid adequate Two boolean env4)
  bad4035 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b0 (bop b0 b0)) b0)) b1 → ⊥
  bad4035  p = false≢true (cong lower p)
  cut4035 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 2) (op (var 3) (var 0))) (var 0))) , (var 4)) → ⊥
  cut4035  adequate = bad4035  (Adequate.valid adequate Two boolean env7)
  bad4036 : PathP (λ _ → Two) (bop (bop b0 b1) (bop (bop b0 (bop b0 b0)) b1)) b0 → ⊥
  bad4036  p = false≢true (sym (cong lower p))
  cut4036 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 2) (op (var 3) (var 0))) (var 1))) , (var 0)) → ⊥
  cut4036  adequate = bad4036  (Adequate.valid adequate Two boolean env10)
  bad4037 : PathP (λ _ → Two) (bop (bop b0 b1) (bop (bop b1 (bop b0 b0)) b1)) b1 → ⊥
  bad4037  p = false≢true (cong lower p)
  cut4037 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 2) (op (var 3) (var 0))) (var 1))) , (var 1)) → ⊥
  cut4037  adequate = bad4037  (Adequate.valid adequate Two boolean env13)
  bad4038 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b1 (bop b0 b0)) b0)) b1 → ⊥
  bad4038  p = false≢true (cong lower p)
  cut4038 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 2) (op (var 3) (var 0))) (var 1))) , (var 2)) → ⊥
  cut4038  adequate = bad4038  (Adequate.valid adequate Two boolean env11)
  bad4039 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b0 (bop b1 b0)) b0)) b1 → ⊥
  bad4039  p = false≢true (cong lower p)
  cut4039 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 2) (op (var 3) (var 0))) (var 1))) , (var 3)) → ⊥
  cut4039  adequate = bad4039  (Adequate.valid adequate Two boolean env4)
  bad4040 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b0 (bop b0 b0)) b0)) b1 → ⊥
  bad4040  p = false≢true (cong lower p)
  cut4040 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 2) (op (var 3) (var 0))) (var 1))) , (var 4)) → ⊥
  cut4040  adequate = bad4040  (Adequate.valid adequate Two boolean env7)
  bad4041 : PathP (λ _ → Two) (bop (bop b1 b0) (bop (bop b0 (bop b0 b1)) b0)) b1 → ⊥
  bad4041  p = false≢true (cong lower p)
  cut4041 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 2) (op (var 3) (var 0))) (var 2))) , (var 0)) → ⊥
  cut4041  adequate = bad4041  (Adequate.valid adequate Two boolean env6)
  bad4042 : PathP (λ _ → Two) (bop (bop b0 b1) (bop (bop b0 (bop b0 b0)) b0)) b1 → ⊥
  bad4042  p = false≢true (cong lower p)
  cut4042 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 2) (op (var 3) (var 0))) (var 2))) , (var 1)) → ⊥
  cut4042  adequate = bad4042  (Adequate.valid adequate Two boolean env10)
  bad4043 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b1 (bop b0 b0)) b1)) b1 → ⊥
  bad4043  p = false≢true (cong lower p)
  cut4043 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 2) (op (var 3) (var 0))) (var 2))) , (var 2)) → ⊥
  cut4043  adequate = bad4043  (Adequate.valid adequate Two boolean env11)
  bad4044 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b0 (bop b1 b0)) b0)) b1 → ⊥
  bad4044  p = false≢true (cong lower p)
  cut4044 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 2) (op (var 3) (var 0))) (var 2))) , (var 3)) → ⊥
  cut4044  adequate = bad4044  (Adequate.valid adequate Two boolean env4)
  bad4045 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b0 (bop b0 b0)) b0)) b1 → ⊥
  bad4045  p = false≢true (cong lower p)
  cut4045 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 2) (op (var 3) (var 0))) (var 2))) , (var 4)) → ⊥
  cut4045  adequate = bad4045  (Adequate.valid adequate Two boolean env7)
  bad4046 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b0 (bop b1 b0)) b1)) b0 → ⊥
  bad4046  p = false≢true (sym (cong lower p))
  cut4046 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 2) (op (var 3) (var 0))) (var 3))) , (var 0)) → ⊥
  cut4046  adequate = bad4046  (Adequate.valid adequate Two boolean env4)
  bad4047 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b0 (bop b1 b0)) b1)) b0 → ⊥
  bad4047  p = false≢true (sym (cong lower p))
  cut4047 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 2) (op (var 3) (var 0))) (var 3))) , (var 1)) → ⊥
  cut4047  adequate = bad4047  (Adequate.valid adequate Two boolean env4)
  bad4048 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b0 (bop b1 b0)) b1)) b0 → ⊥
  bad4048  p = false≢true (sym (cong lower p))
  cut4048 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 2) (op (var 3) (var 0))) (var 3))) , (var 2)) → ⊥
  cut4048  adequate = bad4048  (Adequate.valid adequate Two boolean env4)
  bad4049 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b1 (bop b1 b0)) b1)) b1 → ⊥
  bad4049  p = false≢true (cong lower p)
  cut4049 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 2) (op (var 3) (var 0))) (var 3))) , (var 3)) → ⊥
  cut4049  adequate = bad4049  (Adequate.valid adequate Two boolean env21)
  bad4050 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b0 (bop b0 b0)) b0)) b1 → ⊥
  bad4050  p = false≢true (cong lower p)
  cut4050 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 2) (op (var 3) (var 0))) (var 3))) , (var 4)) → ⊥
  cut4050  adequate = bad4050  (Adequate.valid adequate Two boolean env7)
  bad4051 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b0 (bop b0 b0)) b1)) b0 → ⊥
  bad4051  p = false≢true (sym (cong lower p))
  cut4051 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 2) (op (var 3) (var 0))) (var 4))) , (var 0)) → ⊥
  cut4051  adequate = bad4051  (Adequate.valid adequate Two boolean env7)
  bad4052 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b0 (bop b0 b0)) b1)) b0 → ⊥
  bad4052  p = false≢true (sym (cong lower p))
  cut4052 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 2) (op (var 3) (var 0))) (var 4))) , (var 1)) → ⊥
  cut4052  adequate = bad4052  (Adequate.valid adequate Two boolean env7)
  bad4053 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b0 (bop b0 b0)) b1)) b0 → ⊥
  bad4053  p = false≢true (sym (cong lower p))
  cut4053 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 2) (op (var 3) (var 0))) (var 4))) , (var 2)) → ⊥
  cut4053  adequate = bad4053  (Adequate.valid adequate Two boolean env7)
  bad4054 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b0 (bop b0 b0)) b1)) b0 → ⊥
  bad4054  p = false≢true (sym (cong lower p))
  cut4054 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 2) (op (var 3) (var 0))) (var 4))) , (var 3)) → ⊥
  cut4054  adequate = bad4054  (Adequate.valid adequate Two boolean env7)
  bad4055 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b1 (bop b0 b0)) b1)) b1 → ⊥
  bad4055  p = false≢true (cong lower p)
  cut4055 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 2) (op (var 3) (var 0))) (var 4))) , (var 4)) → ⊥
  cut4055  adequate = bad4055  (Adequate.valid adequate Two boolean env22)
  bad4056 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b0 (bop b0 b0)) b0)) b1 → ⊥
  bad4056  p = false≢true (cong lower p)
  cut4056 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 2) (op (var 3) (var 0))) (var 4))) , (var 5)) → ⊥
  cut4056  adequate = bad4056  (Adequate.valid adequate Two boolean env15)
  bad4057 : PathP (λ _ → Two) (bop (bop b1 b0) (bop (bop b1 (bop b0 b0)) b1)) b1 → ⊥
  bad4057  p = false≢true (cong lower p)
  cut4057 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 2) (op (var 3) (var 1))) (var 0))) , (var 0)) → ⊥
  cut4057  adequate = bad4057  (Adequate.valid adequate Two boolean env19)
  bad4058 : PathP (λ _ → Two) (bop (bop b0 b1) (bop (bop b0 (bop b0 b1)) b0)) b1 → ⊥
  bad4058  p = false≢true (cong lower p)
  cut4058 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 2) (op (var 3) (var 1))) (var 0))) , (var 1)) → ⊥
  cut4058  adequate = bad4058  (Adequate.valid adequate Two boolean env10)
  bad4059 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b1 (bop b0 b0)) b0)) b1 → ⊥
  bad4059  p = false≢true (cong lower p)
  cut4059 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 2) (op (var 3) (var 1))) (var 0))) , (var 2)) → ⊥
  cut4059  adequate = bad4059  (Adequate.valid adequate Two boolean env11)
  bad4060 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b0 (bop b1 b0)) b0)) b1 → ⊥
  bad4060  p = false≢true (cong lower p)
  cut4060 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 2) (op (var 3) (var 1))) (var 0))) , (var 3)) → ⊥
  cut4060  adequate = bad4060  (Adequate.valid adequate Two boolean env4)
  bad4061 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b0 (bop b0 b0)) b0)) b1 → ⊥
  bad4061  p = false≢true (cong lower p)
  cut4061 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 2) (op (var 3) (var 1))) (var 0))) , (var 4)) → ⊥
  cut4061  adequate = bad4061  (Adequate.valid adequate Two boolean env7)
  bad4062 : PathP (λ _ → Two) (bop (bop b0 b1) (bop (bop b0 (bop b0 b1)) b1)) b0 → ⊥
  bad4062  p = false≢true (sym (cong lower p))
  cut4062 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 2) (op (var 3) (var 1))) (var 1))) , (var 0)) → ⊥
  cut4062  adequate = bad4062  (Adequate.valid adequate Two boolean env10)
  bad4063 : PathP (λ _ → Two) (bop (bop b0 b1) (bop (bop b1 (bop b0 b1)) b1)) b1 → ⊥
  bad4063  p = false≢true (cong lower p)
  cut4063 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 2) (op (var 3) (var 1))) (var 1))) , (var 1)) → ⊥
  cut4063  adequate = bad4063  (Adequate.valid adequate Two boolean env13)
  bad4064 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b1 (bop b0 b0)) b0)) b1 → ⊥
  bad4064  p = false≢true (cong lower p)
  cut4064 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 2) (op (var 3) (var 1))) (var 1))) , (var 2)) → ⊥
  cut4064  adequate = bad4064  (Adequate.valid adequate Two boolean env11)
  bad4065 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b0 (bop b1 b0)) b0)) b1 → ⊥
  bad4065  p = false≢true (cong lower p)
  cut4065 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 2) (op (var 3) (var 1))) (var 1))) , (var 3)) → ⊥
  cut4065  adequate = bad4065  (Adequate.valid adequate Two boolean env4)
  bad4066 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b0 (bop b0 b0)) b0)) b1 → ⊥
  bad4066  p = false≢true (cong lower p)
  cut4066 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 2) (op (var 3) (var 1))) (var 1))) , (var 4)) → ⊥
  cut4066  adequate = bad4066  (Adequate.valid adequate Two boolean env7)
  bad4067 : PathP (λ _ → Two) (bop (bop b0 b1) (bop (bop b1 (bop b1 b1)) b1)) b0 → ⊥
  bad4067  p = false≢true (sym (cong lower p))
  cut4067 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 2) (op (var 3) (var 1))) (var 2))) , (var 0)) → ⊥
  cut4067  adequate = bad4067  (Adequate.valid adequate Two boolean env12)
  bad4068 : PathP (λ _ → Two) (bop (bop b0 b1) (bop (bop b0 (bop b0 b1)) b0)) b1 → ⊥
  bad4068  p = false≢true (cong lower p)
  cut4068 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 2) (op (var 3) (var 1))) (var 2))) , (var 1)) → ⊥
  cut4068  adequate = bad4068  (Adequate.valid adequate Two boolean env10)
  bad4069 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b1 (bop b0 b0)) b1)) b1 → ⊥
  bad4069  p = false≢true (cong lower p)
  cut4069 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 2) (op (var 3) (var 1))) (var 2))) , (var 2)) → ⊥
  cut4069  adequate = bad4069  (Adequate.valid adequate Two boolean env11)
  bad4070 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b0 (bop b1 b0)) b0)) b1 → ⊥
  bad4070  p = false≢true (cong lower p)
  cut4070 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 2) (op (var 3) (var 1))) (var 2))) , (var 3)) → ⊥
  cut4070  adequate = bad4070  (Adequate.valid adequate Two boolean env4)
  bad4071 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b0 (bop b0 b0)) b0)) b1 → ⊥
  bad4071  p = false≢true (cong lower p)
  cut4071 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 2) (op (var 3) (var 1))) (var 2))) , (var 4)) → ⊥
  cut4071  adequate = bad4071  (Adequate.valid adequate Two boolean env7)
  bad4072 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b0 (bop b1 b0)) b1)) b0 → ⊥
  bad4072  p = false≢true (sym (cong lower p))
  cut4072 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 2) (op (var 3) (var 1))) (var 3))) , (var 0)) → ⊥
  cut4072  adequate = bad4072  (Adequate.valid adequate Two boolean env4)
  bad4073 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b0 (bop b1 b0)) b1)) b0 → ⊥
  bad4073  p = false≢true (sym (cong lower p))
  cut4073 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 2) (op (var 3) (var 1))) (var 3))) , (var 1)) → ⊥
  cut4073  adequate = bad4073  (Adequate.valid adequate Two boolean env4)
  bad4074 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b0 (bop b1 b0)) b1)) b0 → ⊥
  bad4074  p = false≢true (sym (cong lower p))
  cut4074 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 2) (op (var 3) (var 1))) (var 3))) , (var 2)) → ⊥
  cut4074  adequate = bad4074  (Adequate.valid adequate Two boolean env4)
  bad4075 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b1 (bop b1 b0)) b1)) b1 → ⊥
  bad4075  p = false≢true (cong lower p)
  cut4075 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 2) (op (var 3) (var 1))) (var 3))) , (var 3)) → ⊥
  cut4075  adequate = bad4075  (Adequate.valid adequate Two boolean env21)
  bad4076 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b0 (bop b0 b0)) b0)) b1 → ⊥
  bad4076  p = false≢true (cong lower p)
  cut4076 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 2) (op (var 3) (var 1))) (var 3))) , (var 4)) → ⊥
  cut4076  adequate = bad4076  (Adequate.valid adequate Two boolean env7)
  bad4077 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b0 (bop b0 b0)) b1)) b0 → ⊥
  bad4077  p = false≢true (sym (cong lower p))
  cut4077 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 2) (op (var 3) (var 1))) (var 4))) , (var 0)) → ⊥
  cut4077  adequate = bad4077  (Adequate.valid adequate Two boolean env7)
  bad4078 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b0 (bop b0 b0)) b1)) b0 → ⊥
  bad4078  p = false≢true (sym (cong lower p))
  cut4078 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 2) (op (var 3) (var 1))) (var 4))) , (var 1)) → ⊥
  cut4078  adequate = bad4078  (Adequate.valid adequate Two boolean env7)
  bad4079 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b0 (bop b0 b0)) b1)) b0 → ⊥
  bad4079  p = false≢true (sym (cong lower p))
  cut4079 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 2) (op (var 3) (var 1))) (var 4))) , (var 2)) → ⊥
  cut4079  adequate = bad4079  (Adequate.valid adequate Two boolean env7)
  bad4080 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b0 (bop b0 b0)) b1)) b0 → ⊥
  bad4080  p = false≢true (sym (cong lower p))
  cut4080 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 2) (op (var 3) (var 1))) (var 4))) , (var 3)) → ⊥
  cut4080  adequate = bad4080  (Adequate.valid adequate Two boolean env7)
  bad4081 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b1 (bop b0 b0)) b1)) b1 → ⊥
  bad4081  p = false≢true (cong lower p)
  cut4081 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 2) (op (var 3) (var 1))) (var 4))) , (var 4)) → ⊥
  cut4081  adequate = bad4081  (Adequate.valid adequate Two boolean env22)
  bad4082 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b0 (bop b0 b0)) b0)) b1 → ⊥
  bad4082  p = false≢true (cong lower p)
  cut4082 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 2) (op (var 3) (var 1))) (var 4))) , (var 5)) → ⊥
  cut4082  adequate = bad4082  (Adequate.valid adequate Two boolean env15)
  bad4083 : PathP (λ _ → Two) (bop (bop b1 b0) (bop (bop b1 (bop b0 b1)) b1)) b1 → ⊥
  bad4083  p = false≢true (cong lower p)
  cut4083 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 2) (op (var 3) (var 2))) (var 0))) , (var 0)) → ⊥
  cut4083  adequate = bad4083  (Adequate.valid adequate Two boolean env19)
  bad4084 : PathP (λ _ → Two) (bop (bop b0 b1) (bop (bop b0 (bop b0 b0)) b0)) b1 → ⊥
  bad4084  p = false≢true (cong lower p)
  cut4084 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 2) (op (var 3) (var 2))) (var 0))) , (var 1)) → ⊥
  cut4084  adequate = bad4084  (Adequate.valid adequate Two boolean env10)
  bad4085 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b1 (bop b0 b1)) b0)) b1 → ⊥
  bad4085  p = false≢true (cong lower p)
  cut4085 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 2) (op (var 3) (var 2))) (var 0))) , (var 2)) → ⊥
  cut4085  adequate = bad4085  (Adequate.valid adequate Two boolean env11)
  bad4086 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b0 (bop b1 b0)) b0)) b1 → ⊥
  bad4086  p = false≢true (cong lower p)
  cut4086 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 2) (op (var 3) (var 2))) (var 0))) , (var 3)) → ⊥
  cut4086  adequate = bad4086  (Adequate.valid adequate Two boolean env4)
  bad4087 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b0 (bop b0 b0)) b0)) b1 → ⊥
  bad4087  p = false≢true (cong lower p)
  cut4087 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 2) (op (var 3) (var 2))) (var 0))) , (var 4)) → ⊥
  cut4087  adequate = bad4087  (Adequate.valid adequate Two boolean env7)
  bad4088 : PathP (λ _ → Two) (bop (bop b0 b1) (bop (bop b0 (bop b0 b0)) b1)) b0 → ⊥
  bad4088  p = false≢true (sym (cong lower p))
  cut4088 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 2) (op (var 3) (var 2))) (var 1))) , (var 0)) → ⊥
  cut4088  adequate = bad4088  (Adequate.valid adequate Two boolean env10)
  bad4089 : PathP (λ _ → Two) (bop (bop b0 b1) (bop (bop b1 (bop b0 b1)) b1)) b1 → ⊥
  bad4089  p = false≢true (cong lower p)
  cut4089 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 2) (op (var 3) (var 2))) (var 1))) , (var 1)) → ⊥
  cut4089  adequate = bad4089  (Adequate.valid adequate Two boolean env13)
  bad4090 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b1 (bop b0 b1)) b0)) b1 → ⊥
  bad4090  p = false≢true (cong lower p)
  cut4090 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 2) (op (var 3) (var 2))) (var 1))) , (var 2)) → ⊥
  cut4090  adequate = bad4090  (Adequate.valid adequate Two boolean env11)
  bad4091 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b0 (bop b1 b0)) b0)) b1 → ⊥
  bad4091  p = false≢true (cong lower p)
  cut4091 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 2) (op (var 3) (var 2))) (var 1))) , (var 3)) → ⊥
  cut4091  adequate = bad4091  (Adequate.valid adequate Two boolean env4)
  bad4092 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b0 (bop b0 b0)) b0)) b1 → ⊥
  bad4092  p = false≢true (cong lower p)
  cut4092 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 2) (op (var 3) (var 2))) (var 1))) , (var 4)) → ⊥
  cut4092  adequate = bad4092  (Adequate.valid adequate Two boolean env7)
  bad4093 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b1 (bop b1 b1)) b1)) b0 → ⊥
  bad4093  p = false≢true (sym (cong lower p))
  cut4093 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 2) (op (var 3) (var 2))) (var 2))) , (var 0)) → ⊥
  cut4093  adequate = bad4093  (Adequate.valid adequate Two boolean env21)
  bad4094 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b1 (bop b1 b1)) b1)) b0 → ⊥
  bad4094  p = false≢true (sym (cong lower p))
  cut4094 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 2) (op (var 3) (var 2))) (var 2))) , (var 1)) → ⊥
  cut4094  adequate = bad4094  (Adequate.valid adequate Two boolean env21)
  bad4095 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b1 (bop b0 b1)) b1)) b1 → ⊥
  bad4095  p = false≢true (cong lower p)
  cut4095 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 2) (op (var 3) (var 2))) (var 2))) , (var 2)) → ⊥
  cut4095  adequate = bad4095  (Adequate.valid adequate Two boolean env11)
  bad4096 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b0 (bop b1 b0)) b0)) b1 → ⊥
  bad4096  p = false≢true (cong lower p)
  cut4096 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 2) (op (var 3) (var 2))) (var 2))) , (var 3)) → ⊥
  cut4096  adequate = bad4096  (Adequate.valid adequate Two boolean env4)
  bad4097 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b0 (bop b0 b0)) b0)) b1 → ⊥
  bad4097  p = false≢true (cong lower p)
  cut4097 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 2) (op (var 3) (var 2))) (var 2))) , (var 4)) → ⊥
  cut4097  adequate = bad4097  (Adequate.valid adequate Two boolean env7)
  bad4098 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b0 (bop b1 b0)) b1)) b0 → ⊥
  bad4098  p = false≢true (sym (cong lower p))
  cut4098 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 2) (op (var 3) (var 2))) (var 3))) , (var 0)) → ⊥
  cut4098  adequate = bad4098  (Adequate.valid adequate Two boolean env4)
  bad4099 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b0 (bop b1 b0)) b1)) b0 → ⊥
  bad4099  p = false≢true (sym (cong lower p))
  cut4099 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 2) (op (var 3) (var 2))) (var 3))) , (var 1)) → ⊥
  cut4099  adequate = bad4099  (Adequate.valid adequate Two boolean env4)
  bad4100 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b0 (bop b1 b0)) b1)) b0 → ⊥
  bad4100  p = false≢true (sym (cong lower p))
  cut4100 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 2) (op (var 3) (var 2))) (var 3))) , (var 2)) → ⊥
  cut4100  adequate = bad4100  (Adequate.valid adequate Two boolean env4)
  bad4101 : PathP (λ _ → Two) (bop (bop b1 b1) (bop (bop b0 (bop b0 b0)) b0)) b0 → ⊥
  bad4101  p = false≢true (sym (cong lower p))
  cut4101 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 2) (op (var 3) (var 2))) (var 3))) , (var 3)) → ⊥
  cut4101  adequate = bad4101  (Adequate.valid adequate Two boolean env23)
  bad4102 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b0 (bop b0 b0)) b0)) b1 → ⊥
  bad4102  p = false≢true (cong lower p)
  cut4102 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 2) (op (var 3) (var 2))) (var 3))) , (var 4)) → ⊥
  cut4102  adequate = bad4102  (Adequate.valid adequate Two boolean env7)
  bad4103 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b0 (bop b0 b0)) b1)) b0 → ⊥
  bad4103  p = false≢true (sym (cong lower p))
  cut4103 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 2) (op (var 3) (var 2))) (var 4))) , (var 0)) → ⊥
  cut4103  adequate = bad4103  (Adequate.valid adequate Two boolean env7)
  bad4104 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b0 (bop b0 b0)) b1)) b0 → ⊥
  bad4104  p = false≢true (sym (cong lower p))
  cut4104 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 2) (op (var 3) (var 2))) (var 4))) , (var 1)) → ⊥
  cut4104  adequate = bad4104  (Adequate.valid adequate Two boolean env7)
  bad4105 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b0 (bop b0 b0)) b1)) b0 → ⊥
  bad4105  p = false≢true (sym (cong lower p))
  cut4105 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 2) (op (var 3) (var 2))) (var 4))) , (var 2)) → ⊥
  cut4105  adequate = bad4105  (Adequate.valid adequate Two boolean env7)
  bad4106 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b0 (bop b0 b0)) b1)) b0 → ⊥
  bad4106  p = false≢true (sym (cong lower p))
  cut4106 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 2) (op (var 3) (var 2))) (var 4))) , (var 3)) → ⊥
  cut4106  adequate = bad4106  (Adequate.valid adequate Two boolean env7)
  bad4107 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b1 (bop b0 b1)) b1)) b1 → ⊥
  bad4107  p = false≢true (cong lower p)
  cut4107 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 2) (op (var 3) (var 2))) (var 4))) , (var 4)) → ⊥
  cut4107  adequate = bad4107  (Adequate.valid adequate Two boolean env22)
  bad4108 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b0 (bop b0 b0)) b0)) b1 → ⊥
  bad4108  p = false≢true (cong lower p)
  cut4108 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 2) (op (var 3) (var 2))) (var 4))) , (var 5)) → ⊥
  cut4108  adequate = bad4108  (Adequate.valid adequate Two boolean env15)
  bad4109 : PathP (λ _ → Two) (bop (bop b1 b0) (bop (bop b1 (bop b0 b0)) b1)) b1 → ⊥
  bad4109  p = false≢true (cong lower p)
  cut4109 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 2) (op (var 3) (var 3))) (var 0))) , (var 0)) → ⊥
  cut4109  adequate = bad4109  (Adequate.valid adequate Two boolean env19)
  bad4110 : PathP (λ _ → Two) (bop (bop b0 b1) (bop (bop b0 (bop b0 b0)) b0)) b1 → ⊥
  bad4110  p = false≢true (cong lower p)
  cut4110 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 2) (op (var 3) (var 3))) (var 0))) , (var 1)) → ⊥
  cut4110  adequate = bad4110  (Adequate.valid adequate Two boolean env10)
  bad4111 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b1 (bop b0 b0)) b0)) b1 → ⊥
  bad4111  p = false≢true (cong lower p)
  cut4111 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 2) (op (var 3) (var 3))) (var 0))) , (var 2)) → ⊥
  cut4111  adequate = bad4111  (Adequate.valid adequate Two boolean env11)
  bad4112 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b0 (bop b1 b1)) b0)) b1 → ⊥
  bad4112  p = false≢true (cong lower p)
  cut4112 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 2) (op (var 3) (var 3))) (var 0))) , (var 3)) → ⊥
  cut4112  adequate = bad4112  (Adequate.valid adequate Two boolean env4)
  bad4113 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b0 (bop b0 b0)) b0)) b1 → ⊥
  bad4113  p = false≢true (cong lower p)
  cut4113 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 2) (op (var 3) (var 3))) (var 0))) , (var 4)) → ⊥
  cut4113  adequate = bad4113  (Adequate.valid adequate Two boolean env7)
  bad4114 : PathP (λ _ → Two) (bop (bop b0 b1) (bop (bop b0 (bop b0 b0)) b1)) b0 → ⊥
  bad4114  p = false≢true (sym (cong lower p))
  cut4114 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 2) (op (var 3) (var 3))) (var 1))) , (var 0)) → ⊥
  cut4114  adequate = bad4114  (Adequate.valid adequate Two boolean env10)
  bad4115 : PathP (λ _ → Two) (bop (bop b0 b1) (bop (bop b1 (bop b0 b0)) b1)) b1 → ⊥
  bad4115  p = false≢true (cong lower p)
  cut4115 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 2) (op (var 3) (var 3))) (var 1))) , (var 1)) → ⊥
  cut4115  adequate = bad4115  (Adequate.valid adequate Two boolean env13)
  bad4116 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b1 (bop b0 b0)) b0)) b1 → ⊥
  bad4116  p = false≢true (cong lower p)
  cut4116 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 2) (op (var 3) (var 3))) (var 1))) , (var 2)) → ⊥
  cut4116  adequate = bad4116  (Adequate.valid adequate Two boolean env11)
  bad4117 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b0 (bop b1 b1)) b0)) b1 → ⊥
  bad4117  p = false≢true (cong lower p)
  cut4117 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 2) (op (var 3) (var 3))) (var 1))) , (var 3)) → ⊥
  cut4117  adequate = bad4117  (Adequate.valid adequate Two boolean env4)
  bad4118 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b0 (bop b0 b0)) b0)) b1 → ⊥
  bad4118  p = false≢true (cong lower p)
  cut4118 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 2) (op (var 3) (var 3))) (var 1))) , (var 4)) → ⊥
  cut4118  adequate = bad4118  (Adequate.valid adequate Two boolean env7)
  bad4119 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b1 (bop b1 b1)) b1)) b0 → ⊥
  bad4119  p = false≢true (sym (cong lower p))
  cut4119 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 2) (op (var 3) (var 3))) (var 2))) , (var 0)) → ⊥
  cut4119  adequate = bad4119  (Adequate.valid adequate Two boolean env21)
  bad4120 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b1 (bop b1 b1)) b1)) b0 → ⊥
  bad4120  p = false≢true (sym (cong lower p))
  cut4120 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 2) (op (var 3) (var 3))) (var 2))) , (var 1)) → ⊥
  cut4120  adequate = bad4120  (Adequate.valid adequate Two boolean env21)
  bad4121 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b1 (bop b0 b0)) b1)) b1 → ⊥
  bad4121  p = false≢true (cong lower p)
  cut4121 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 2) (op (var 3) (var 3))) (var 2))) , (var 2)) → ⊥
  cut4121  adequate = bad4121  (Adequate.valid adequate Two boolean env11)
  bad4122 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b0 (bop b1 b1)) b0)) b1 → ⊥
  bad4122  p = false≢true (cong lower p)
  cut4122 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 2) (op (var 3) (var 3))) (var 2))) , (var 3)) → ⊥
  cut4122  adequate = bad4122  (Adequate.valid adequate Two boolean env4)
  bad4123 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b0 (bop b0 b0)) b0)) b1 → ⊥
  bad4123  p = false≢true (cong lower p)
  cut4123 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 2) (op (var 3) (var 3))) (var 2))) , (var 4)) → ⊥
  cut4123  adequate = bad4123  (Adequate.valid adequate Two boolean env7)
  bad4124 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b0 (bop b1 b1)) b1)) b0 → ⊥
  bad4124  p = false≢true (sym (cong lower p))
  cut4124 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 2) (op (var 3) (var 3))) (var 3))) , (var 0)) → ⊥
  cut4124  adequate = bad4124  (Adequate.valid adequate Two boolean env4)
  bad4125 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b0 (bop b1 b1)) b1)) b0 → ⊥
  bad4125  p = false≢true (sym (cong lower p))
  cut4125 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 2) (op (var 3) (var 3))) (var 3))) , (var 1)) → ⊥
  cut4125  adequate = bad4125  (Adequate.valid adequate Two boolean env4)
  bad4126 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b0 (bop b1 b1)) b1)) b0 → ⊥
  bad4126  p = false≢true (sym (cong lower p))
  cut4126 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 2) (op (var 3) (var 3))) (var 3))) , (var 2)) → ⊥
  cut4126  adequate = bad4126  (Adequate.valid adequate Two boolean env4)
  bad4127 : PathP (λ _ → Two) (bop (bop b1 b1) (bop (bop b0 (bop b0 b0)) b0)) b0 → ⊥
  bad4127  p = false≢true (sym (cong lower p))
  cut4127 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 2) (op (var 3) (var 3))) (var 3))) , (var 3)) → ⊥
  cut4127  adequate = bad4127  (Adequate.valid adequate Two boolean env23)
  bad4128 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b0 (bop b0 b0)) b0)) b1 → ⊥
  bad4128  p = false≢true (cong lower p)
  cut4128 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 2) (op (var 3) (var 3))) (var 3))) , (var 4)) → ⊥
  cut4128  adequate = bad4128  (Adequate.valid adequate Two boolean env7)
  bad4129 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b0 (bop b0 b0)) b1)) b0 → ⊥
  bad4129  p = false≢true (sym (cong lower p))
  cut4129 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 2) (op (var 3) (var 3))) (var 4))) , (var 0)) → ⊥
  cut4129  adequate = bad4129  (Adequate.valid adequate Two boolean env7)
  bad4130 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b0 (bop b0 b0)) b1)) b0 → ⊥
  bad4130  p = false≢true (sym (cong lower p))
  cut4130 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 2) (op (var 3) (var 3))) (var 4))) , (var 1)) → ⊥
  cut4130  adequate = bad4130  (Adequate.valid adequate Two boolean env7)
  bad4131 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b0 (bop b0 b0)) b1)) b0 → ⊥
  bad4131  p = false≢true (sym (cong lower p))
  cut4131 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 2) (op (var 3) (var 3))) (var 4))) , (var 2)) → ⊥
  cut4131  adequate = bad4131  (Adequate.valid adequate Two boolean env7)
  bad4132 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b0 (bop b0 b0)) b1)) b0 → ⊥
  bad4132  p = false≢true (sym (cong lower p))
  cut4132 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 2) (op (var 3) (var 3))) (var 4))) , (var 3)) → ⊥
  cut4132  adequate = bad4132  (Adequate.valid adequate Two boolean env7)
  bad4133 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b1 (bop b0 b0)) b1)) b1 → ⊥
  bad4133  p = false≢true (cong lower p)
  cut4133 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 2) (op (var 3) (var 3))) (var 4))) , (var 4)) → ⊥
  cut4133  adequate = bad4133  (Adequate.valid adequate Two boolean env22)
  bad4134 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b0 (bop b0 b0)) b0)) b1 → ⊥
  bad4134  p = false≢true (cong lower p)
  cut4134 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 2) (op (var 3) (var 3))) (var 4))) , (var 5)) → ⊥
  cut4134  adequate = bad4134  (Adequate.valid adequate Two boolean env15)
  env24 : ℕ → Two
  env24 zero = b1
  env24 (suc zero) = b0
  env24 (suc (suc zero)) = b1
  env24 (suc (suc (suc zero))) = b0
  env24 (suc (suc (suc (suc zero)))) = b0
  env24 (suc (suc (suc (suc (suc rest))))) = b0
  bad4135 : PathP (λ _ → Two) (bop (bop b1 b0) (bop (bop b1 (bop b0 b0)) b1)) b1 → ⊥
  bad4135  p = false≢true (cong lower p)
  cut4135 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 2) (op (var 3) (var 4))) (var 0))) , (var 0)) → ⊥
  cut4135  adequate = bad4135  (Adequate.valid adequate Two boolean env24)
  env25 : ℕ → Two
  env25 zero = b0
  env25 (suc zero) = b1
  env25 (suc (suc zero)) = b0
  env25 (suc (suc (suc zero))) = b0
  env25 (suc (suc (suc (suc zero)))) = b0
  env25 (suc (suc (suc (suc (suc rest))))) = b0
  bad4136 : PathP (λ _ → Two) (bop (bop b0 b1) (bop (bop b0 (bop b0 b0)) b0)) b1 → ⊥
  bad4136  p = false≢true (cong lower p)
  cut4136 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 2) (op (var 3) (var 4))) (var 0))) , (var 1)) → ⊥
  cut4136  adequate = bad4136  (Adequate.valid adequate Two boolean env25)
  env26 : ℕ → Two
  env26 zero = b0
  env26 (suc zero) = b0
  env26 (suc (suc zero)) = b1
  env26 (suc (suc (suc zero))) = b0
  env26 (suc (suc (suc (suc zero)))) = b0
  env26 (suc (suc (suc (suc (suc rest))))) = b0
  bad4137 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b1 (bop b0 b0)) b0)) b1 → ⊥
  bad4137  p = false≢true (cong lower p)
  cut4137 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 2) (op (var 3) (var 4))) (var 0))) , (var 2)) → ⊥
  cut4137  adequate = bad4137  (Adequate.valid adequate Two boolean env26)
  env27 : ℕ → Two
  env27 zero = b0
  env27 (suc zero) = b0
  env27 (suc (suc zero)) = b0
  env27 (suc (suc (suc zero))) = b1
  env27 (suc (suc (suc (suc zero)))) = b0
  env27 (suc (suc (suc (suc (suc rest))))) = b0
  bad4138 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b0 (bop b1 b0)) b0)) b1 → ⊥
  bad4138  p = false≢true (cong lower p)
  cut4138 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 2) (op (var 3) (var 4))) (var 0))) , (var 3)) → ⊥
  cut4138  adequate = bad4138  (Adequate.valid adequate Two boolean env27)
  bad4139 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b0 (bop b0 b1)) b0)) b1 → ⊥
  bad4139  p = false≢true (cong lower p)
  cut4139 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 2) (op (var 3) (var 4))) (var 0))) , (var 4)) → ⊥
  cut4139  adequate = bad4139  (Adequate.valid adequate Two boolean env7)
  bad4140 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b0 (bop b0 b0)) b0)) b1 → ⊥
  bad4140  p = false≢true (cong lower p)
  cut4140 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 2) (op (var 3) (var 4))) (var 0))) , (var 5)) → ⊥
  cut4140  adequate = bad4140  (Adequate.valid adequate Two boolean env15)
  bad4141 : PathP (λ _ → Two) (bop (bop b0 b1) (bop (bop b0 (bop b0 b0)) b1)) b0 → ⊥
  bad4141  p = false≢true (sym (cong lower p))
  cut4141 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 2) (op (var 3) (var 4))) (var 1))) , (var 0)) → ⊥
  cut4141  adequate = bad4141  (Adequate.valid adequate Two boolean env25)
  env28 : ℕ → Two
  env28 zero = b0
  env28 (suc zero) = b1
  env28 (suc (suc zero)) = b1
  env28 (suc (suc (suc zero))) = b0
  env28 (suc (suc (suc (suc zero)))) = b0
  env28 (suc (suc (suc (suc (suc rest))))) = b0
  bad4142 : PathP (λ _ → Two) (bop (bop b0 b1) (bop (bop b1 (bop b0 b0)) b1)) b1 → ⊥
  bad4142  p = false≢true (cong lower p)
  cut4142 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 2) (op (var 3) (var 4))) (var 1))) , (var 1)) → ⊥
  cut4142  adequate = bad4142  (Adequate.valid adequate Two boolean env28)
  bad4143 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b1 (bop b0 b0)) b0)) b1 → ⊥
  bad4143  p = false≢true (cong lower p)
  cut4143 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 2) (op (var 3) (var 4))) (var 1))) , (var 2)) → ⊥
  cut4143  adequate = bad4143  (Adequate.valid adequate Two boolean env26)
  bad4144 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b0 (bop b1 b0)) b0)) b1 → ⊥
  bad4144  p = false≢true (cong lower p)
  cut4144 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 2) (op (var 3) (var 4))) (var 1))) , (var 3)) → ⊥
  cut4144  adequate = bad4144  (Adequate.valid adequate Two boolean env27)
  bad4145 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b0 (bop b0 b1)) b0)) b1 → ⊥
  bad4145  p = false≢true (cong lower p)
  cut4145 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 2) (op (var 3) (var 4))) (var 1))) , (var 4)) → ⊥
  cut4145  adequate = bad4145  (Adequate.valid adequate Two boolean env7)
  bad4146 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b0 (bop b0 b0)) b0)) b1 → ⊥
  bad4146  p = false≢true (cong lower p)
  cut4146 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 2) (op (var 3) (var 4))) (var 1))) , (var 5)) → ⊥
  cut4146  adequate = bad4146  (Adequate.valid adequate Two boolean env15)
  env29 : ℕ → Two
  env29 zero = b0
  env29 (suc zero) = b0
  env29 (suc (suc zero)) = b1
  env29 (suc (suc (suc zero))) = b1
  env29 (suc (suc (suc (suc zero)))) = b1
  env29 (suc (suc (suc (suc (suc rest))))) = b0
  bad4147 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b1 (bop b1 b1)) b1)) b0 → ⊥
  bad4147  p = false≢true (sym (cong lower p))
  cut4147 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 2) (op (var 3) (var 4))) (var 2))) , (var 0)) → ⊥
  cut4147  adequate = bad4147  (Adequate.valid adequate Two boolean env29)
  bad4148 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b1 (bop b1 b1)) b1)) b0 → ⊥
  bad4148  p = false≢true (sym (cong lower p))
  cut4148 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 2) (op (var 3) (var 4))) (var 2))) , (var 1)) → ⊥
  cut4148  adequate = bad4148  (Adequate.valid adequate Two boolean env29)
  bad4149 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b1 (bop b0 b0)) b1)) b1 → ⊥
  bad4149  p = false≢true (cong lower p)
  cut4149 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 2) (op (var 3) (var 4))) (var 2))) , (var 2)) → ⊥
  cut4149  adequate = bad4149  (Adequate.valid adequate Two boolean env26)
  bad4150 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b0 (bop b1 b0)) b0)) b1 → ⊥
  bad4150  p = false≢true (cong lower p)
  cut4150 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 2) (op (var 3) (var 4))) (var 2))) , (var 3)) → ⊥
  cut4150  adequate = bad4150  (Adequate.valid adequate Two boolean env27)
  bad4151 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b0 (bop b0 b1)) b0)) b1 → ⊥
  bad4151  p = false≢true (cong lower p)
  cut4151 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 2) (op (var 3) (var 4))) (var 2))) , (var 4)) → ⊥
  cut4151  adequate = bad4151  (Adequate.valid adequate Two boolean env7)
  bad4152 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b0 (bop b0 b0)) b0)) b1 → ⊥
  bad4152  p = false≢true (cong lower p)
  cut4152 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 2) (op (var 3) (var 4))) (var 2))) , (var 5)) → ⊥
  cut4152  adequate = bad4152  (Adequate.valid adequate Two boolean env15)
  bad4153 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b0 (bop b1 b0)) b1)) b0 → ⊥
  bad4153  p = false≢true (sym (cong lower p))
  cut4153 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 2) (op (var 3) (var 4))) (var 3))) , (var 0)) → ⊥
  cut4153  adequate = bad4153  (Adequate.valid adequate Two boolean env27)
  bad4154 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b0 (bop b1 b0)) b1)) b0 → ⊥
  bad4154  p = false≢true (sym (cong lower p))
  cut4154 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 2) (op (var 3) (var 4))) (var 3))) , (var 1)) → ⊥
  cut4154  adequate = bad4154  (Adequate.valid adequate Two boolean env27)
  bad4155 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b0 (bop b1 b0)) b1)) b0 → ⊥
  bad4155  p = false≢true (sym (cong lower p))
  cut4155 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 2) (op (var 3) (var 4))) (var 3))) , (var 2)) → ⊥
  cut4155  adequate = bad4155  (Adequate.valid adequate Two boolean env27)
  env30 : ℕ → Two
  env30 zero = b0
  env30 (suc zero) = b0
  env30 (suc (suc zero)) = b1
  env30 (suc (suc (suc zero))) = b1
  env30 (suc (suc (suc (suc zero)))) = b0
  env30 (suc (suc (suc (suc (suc rest))))) = b0
  bad4156 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b1 (bop b1 b0)) b1)) b1 → ⊥
  bad4156  p = false≢true (cong lower p)
  cut4156 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 2) (op (var 3) (var 4))) (var 3))) , (var 3)) → ⊥
  cut4156  adequate = bad4156  (Adequate.valid adequate Two boolean env30)
  bad4157 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b0 (bop b0 b1)) b0)) b1 → ⊥
  bad4157  p = false≢true (cong lower p)
  cut4157 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 2) (op (var 3) (var 4))) (var 3))) , (var 4)) → ⊥
  cut4157  adequate = bad4157  (Adequate.valid adequate Two boolean env7)
  bad4158 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b0 (bop b0 b0)) b0)) b1 → ⊥
  bad4158  p = false≢true (cong lower p)
  cut4158 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 2) (op (var 3) (var 4))) (var 3))) , (var 5)) → ⊥
  cut4158  adequate = bad4158  (Adequate.valid adequate Two boolean env15)
  bad4159 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b0 (bop b0 b1)) b1)) b0 → ⊥
  bad4159  p = false≢true (sym (cong lower p))
  cut4159 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 2) (op (var 3) (var 4))) (var 4))) , (var 0)) → ⊥
  cut4159  adequate = bad4159  (Adequate.valid adequate Two boolean env7)
  bad4160 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b0 (bop b0 b1)) b1)) b0 → ⊥
  bad4160  p = false≢true (sym (cong lower p))
  cut4160 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 2) (op (var 3) (var 4))) (var 4))) , (var 1)) → ⊥
  cut4160  adequate = bad4160  (Adequate.valid adequate Two boolean env7)
  bad4161 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b0 (bop b0 b1)) b1)) b0 → ⊥
  bad4161  p = false≢true (sym (cong lower p))
  cut4161 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 2) (op (var 3) (var 4))) (var 4))) , (var 2)) → ⊥
  cut4161  adequate = bad4161  (Adequate.valid adequate Two boolean env7)
  bad4162 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b0 (bop b0 b1)) b1)) b0 → ⊥
  bad4162  p = false≢true (sym (cong lower p))
  cut4162 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 2) (op (var 3) (var 4))) (var 4))) , (var 3)) → ⊥
  cut4162  adequate = bad4162  (Adequate.valid adequate Two boolean env7)
  bad4163 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b1 (bop b0 b1)) b1)) b1 → ⊥
  bad4163  p = false≢true (cong lower p)
  cut4163 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 2) (op (var 3) (var 4))) (var 4))) , (var 4)) → ⊥
  cut4163  adequate = bad4163  (Adequate.valid adequate Two boolean env22)
  bad4164 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b0 (bop b0 b0)) b0)) b1 → ⊥
  bad4164  p = false≢true (cong lower p)
  cut4164 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 2) (op (var 3) (var 4))) (var 4))) , (var 5)) → ⊥
  cut4164  adequate = bad4164  (Adequate.valid adequate Two boolean env15)
  bad4165 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b0 (bop b0 b0)) b1)) b0 → ⊥
  bad4165  p = false≢true (sym (cong lower p))
  cut4165 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 2) (op (var 3) (var 4))) (var 5))) , (var 0)) → ⊥
  cut4165  adequate = bad4165  (Adequate.valid adequate Two boolean env15)
  bad4166 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b0 (bop b0 b0)) b1)) b0 → ⊥
  bad4166  p = false≢true (sym (cong lower p))
  cut4166 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 2) (op (var 3) (var 4))) (var 5))) , (var 1)) → ⊥
  cut4166  adequate = bad4166  (Adequate.valid adequate Two boolean env15)
  bad4167 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b0 (bop b0 b0)) b1)) b0 → ⊥
  bad4167  p = false≢true (sym (cong lower p))
  cut4167 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 2) (op (var 3) (var 4))) (var 5))) , (var 2)) → ⊥
  cut4167  adequate = bad4167  (Adequate.valid adequate Two boolean env15)
  bad4168 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b0 (bop b0 b0)) b1)) b0 → ⊥
  bad4168  p = false≢true (sym (cong lower p))
  cut4168 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 2) (op (var 3) (var 4))) (var 5))) , (var 3)) → ⊥
  cut4168  adequate = bad4168  (Adequate.valid adequate Two boolean env15)
  bad4169 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b0 (bop b0 b0)) b1)) b0 → ⊥
  bad4169  p = false≢true (sym (cong lower p))
  cut4169 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 2) (op (var 3) (var 4))) (var 5))) , (var 4)) → ⊥
  cut4169  adequate = bad4169  (Adequate.valid adequate Two boolean env15)
  env31 : ℕ → Two
  env31 zero = b0
  env31 (suc zero) = b0
  env31 (suc (suc zero)) = b1
  env31 (suc (suc (suc zero))) = b0
  env31 (suc (suc (suc (suc zero)))) = b0
  env31 (suc (suc (suc (suc (suc zero))))) = b1
  env31 (suc (suc (suc (suc (suc (suc rest)))))) = b0
  bad4170 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b1 (bop b0 b0)) b1)) b1 → ⊥
  bad4170  p = false≢true (cong lower p)
  cut4170 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 2) (op (var 3) (var 4))) (var 5))) , (var 5)) → ⊥
  cut4170  adequate = bad4170  (Adequate.valid adequate Two boolean env31)
  env32 : ℕ → Two
  env32 zero = b0
  env32 (suc zero) = b0
  env32 (suc (suc zero)) = b0
  env32 (suc (suc (suc zero))) = b0
  env32 (suc (suc (suc (suc zero)))) = b0
  env32 (suc (suc (suc (suc (suc zero))))) = b0
  env32 (suc (suc (suc (suc (suc (suc zero)))))) = b1
  env32 (suc (suc (suc (suc (suc (suc (suc rest))))))) = b0
  bad4171 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b0 (bop b0 b0)) b0)) b1 → ⊥
  bad4171  p = false≢true (cong lower p)
  cut4171 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 2) (op (var 3) (var 4))) (var 5))) , (var 6)) → ⊥
  cut4171  adequate = bad4171  (Adequate.valid adequate Two boolean env32)
