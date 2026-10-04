{-# OPTIONS --safe --cubical --guardedness #-}
module GeneratedMinimumShape56 where
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
  holds384 : (z0 : A1) → (mul1 (mul1 z0 z0) (mul1 (mul1 z0 z0) z0)) ≡ z0
  holds384 m1c0 = refl
  holds384 m1c1 = refl
  cut384 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (op (var 0) (var 0)) (var 0))) , (var 0)) → ⊥
  cut384  = reject1 ((op (op (var 0) (var 0)) (op (op (var 0) (var 0)) (var 0))) , (var 0)) (λ env → holds384 (env 0))
  env0 : ℕ → Two
  env0 zero = b0
  env0 (suc zero) = b1
  env0 (suc (suc rest)) = b0
  bad385 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b0 b0) b0)) b1 → ⊥
  bad385  p = false≢true (cong lower p)
  cut385 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (op (var 0) (var 0)) (var 0))) , (var 1)) → ⊥
  cut385  adequate = bad385  (Adequate.valid adequate Two boolean env0)
  bad386 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b0 b0) b1)) b0 → ⊥
  bad386  p = false≢true (sym (cong lower p))
  cut386 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (op (var 0) (var 0)) (var 1))) , (var 0)) → ⊥
  cut386  adequate = bad386  (Adequate.valid adequate Two boolean env0)
  env1 : ℕ → Two
  env1 zero = b1
  env1 (suc zero) = b0
  env1 (suc (suc rest)) = b0
  bad387 : PathP (λ _ → Two) (bop (bop b1 b1) (bop (bop b1 b1) b0)) b0 → ⊥
  bad387  p = false≢true (sym (cong lower p))
  cut387 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (op (var 0) (var 0)) (var 1))) , (var 1)) → ⊥
  cut387  adequate = bad387  (Adequate.valid adequate Two boolean env1)
  env2 : ℕ → Two
  env2 zero = b0
  env2 (suc zero) = b0
  env2 (suc (suc zero)) = b1
  env2 (suc (suc (suc rest))) = b0
  bad388 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b0 b0) b0)) b1 → ⊥
  bad388  p = false≢true (cong lower p)
  cut388 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (op (var 0) (var 0)) (var 1))) , (var 2)) → ⊥
  cut388  adequate = bad388  (Adequate.valid adequate Two boolean env2)
  holds389 : (z0 z1 : A2) → (mul2 (mul2 z0 z0) (mul2 (mul2 z0 z1) z0)) ≡ z0
  holds389 z0 z1 = refl
  cut389 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (op (var 0) (var 1)) (var 0))) , (var 0)) → ⊥
  cut389  = reject2 ((op (op (var 0) (var 0)) (op (op (var 0) (var 1)) (var 0))) , (var 0)) (λ env → holds389 (env 0) (env 1))
  bad390 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b0 b1) b0)) b1 → ⊥
  bad390  p = false≢true (cong lower p)
  cut390 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (op (var 0) (var 1)) (var 0))) , (var 1)) → ⊥
  cut390  adequate = bad390  (Adequate.valid adequate Two boolean env0)
  bad391 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b0 b0) b0)) b1 → ⊥
  bad391  p = false≢true (cong lower p)
  cut391 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (op (var 0) (var 1)) (var 0))) , (var 2)) → ⊥
  cut391  adequate = bad391  (Adequate.valid adequate Two boolean env2)
  bad392 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b0 b1) b1)) b0 → ⊥
  bad392  p = false≢true (sym (cong lower p))
  cut392 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (op (var 0) (var 1)) (var 1))) , (var 0)) → ⊥
  cut392  adequate = bad392  (Adequate.valid adequate Two boolean env0)
  bad393 : PathP (λ _ → Two) (bop (bop b1 b1) (bop (bop b1 b0) b0)) b0 → ⊥
  bad393  p = false≢true (sym (cong lower p))
  cut393 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (op (var 0) (var 1)) (var 1))) , (var 1)) → ⊥
  cut393  adequate = bad393  (Adequate.valid adequate Two boolean env1)
  bad394 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b0 b0) b0)) b1 → ⊥
  bad394  p = false≢true (cong lower p)
  cut394 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (op (var 0) (var 1)) (var 1))) , (var 2)) → ⊥
  cut394  adequate = bad394  (Adequate.valid adequate Two boolean env2)
  bad395 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b0 b0) b1)) b0 → ⊥
  bad395  p = false≢true (sym (cong lower p))
  cut395 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (op (var 0) (var 1)) (var 2))) , (var 0)) → ⊥
  cut395  adequate = bad395  (Adequate.valid adequate Two boolean env2)
  bad396 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b0 b0) b1)) b0 → ⊥
  bad396  p = false≢true (sym (cong lower p))
  cut396 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (op (var 0) (var 1)) (var 2))) , (var 1)) → ⊥
  cut396  adequate = bad396  (Adequate.valid adequate Two boolean env2)
  env3 : ℕ → Two
  env3 zero = b1
  env3 (suc zero) = b0
  env3 (suc (suc zero)) = b0
  env3 (suc (suc (suc rest))) = b0
  bad397 : PathP (λ _ → Two) (bop (bop b1 b1) (bop (bop b1 b0) b0)) b0 → ⊥
  bad397  p = false≢true (sym (cong lower p))
  cut397 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (op (var 0) (var 1)) (var 2))) , (var 2)) → ⊥
  cut397  adequate = bad397  (Adequate.valid adequate Two boolean env3)
  env4 : ℕ → Two
  env4 zero = b0
  env4 (suc zero) = b0
  env4 (suc (suc zero)) = b0
  env4 (suc (suc (suc zero))) = b1
  env4 (suc (suc (suc (suc rest)))) = b0
  bad398 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b0 b0) b0)) b1 → ⊥
  bad398  p = false≢true (cong lower p)
  cut398 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (op (var 0) (var 1)) (var 2))) , (var 3)) → ⊥
  cut398  adequate = bad398  (Adequate.valid adequate Two boolean env4)
  holds399 : (z0 z1 : A2) → (mul2 (mul2 z0 z0) (mul2 (mul2 z1 z0) z0)) ≡ z0
  holds399 z0 z1 = refl
  cut399 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (op (var 1) (var 0)) (var 0))) , (var 0)) → ⊥
  cut399  = reject2 ((op (op (var 0) (var 0)) (op (op (var 1) (var 0)) (var 0))) , (var 0)) (λ env → holds399 (env 0) (env 1))
  bad400 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b1 b0) b0)) b1 → ⊥
  bad400  p = false≢true (cong lower p)
  cut400 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (op (var 1) (var 0)) (var 0))) , (var 1)) → ⊥
  cut400  adequate = bad400  (Adequate.valid adequate Two boolean env0)
  bad401 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b0 b0) b0)) b1 → ⊥
  bad401  p = false≢true (cong lower p)
  cut401 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (op (var 1) (var 0)) (var 0))) , (var 2)) → ⊥
  cut401  adequate = bad401  (Adequate.valid adequate Two boolean env2)
  bad402 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b1 b0) b1)) b0 → ⊥
  bad402  p = false≢true (sym (cong lower p))
  cut402 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (op (var 1) (var 0)) (var 1))) , (var 0)) → ⊥
  cut402  adequate = bad402  (Adequate.valid adequate Two boolean env0)
  bad403 : PathP (λ _ → Two) (bop (bop b1 b1) (bop (bop b0 b1) b0)) b0 → ⊥
  bad403  p = false≢true (sym (cong lower p))
  cut403 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (op (var 1) (var 0)) (var 1))) , (var 1)) → ⊥
  cut403  adequate = bad403  (Adequate.valid adequate Two boolean env1)
  bad404 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b0 b0) b0)) b1 → ⊥
  bad404  p = false≢true (cong lower p)
  cut404 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (op (var 1) (var 0)) (var 1))) , (var 2)) → ⊥
  cut404  adequate = bad404  (Adequate.valid adequate Two boolean env2)
  bad405 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b0 b0) b1)) b0 → ⊥
  bad405  p = false≢true (sym (cong lower p))
  cut405 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (op (var 1) (var 0)) (var 2))) , (var 0)) → ⊥
  cut405  adequate = bad405  (Adequate.valid adequate Two boolean env2)
  bad406 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b0 b0) b1)) b0 → ⊥
  bad406  p = false≢true (sym (cong lower p))
  cut406 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (op (var 1) (var 0)) (var 2))) , (var 1)) → ⊥
  cut406  adequate = bad406  (Adequate.valid adequate Two boolean env2)
  bad407 : PathP (λ _ → Two) (bop (bop b1 b1) (bop (bop b0 b1) b0)) b0 → ⊥
  bad407  p = false≢true (sym (cong lower p))
  cut407 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (op (var 1) (var 0)) (var 2))) , (var 2)) → ⊥
  cut407  adequate = bad407  (Adequate.valid adequate Two boolean env3)
  bad408 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b0 b0) b0)) b1 → ⊥
  bad408  p = false≢true (cong lower p)
  cut408 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (op (var 1) (var 0)) (var 2))) , (var 3)) → ⊥
  cut408  adequate = bad408  (Adequate.valid adequate Two boolean env4)
  holds409 : (z0 z1 : A2) → (mul2 (mul2 z0 z0) (mul2 (mul2 z1 z1) z0)) ≡ z0
  holds409 z0 z1 = refl
  cut409 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (op (var 1) (var 1)) (var 0))) , (var 0)) → ⊥
  cut409  = reject2 ((op (op (var 0) (var 0)) (op (op (var 1) (var 1)) (var 0))) , (var 0)) (λ env → holds409 (env 0) (env 1))
  bad410 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b1 b1) b0)) b1 → ⊥
  bad410  p = false≢true (cong lower p)
  cut410 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (op (var 1) (var 1)) (var 0))) , (var 1)) → ⊥
  cut410  adequate = bad410  (Adequate.valid adequate Two boolean env0)
  bad411 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b0 b0) b0)) b1 → ⊥
  bad411  p = false≢true (cong lower p)
  cut411 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (op (var 1) (var 1)) (var 0))) , (var 2)) → ⊥
  cut411  adequate = bad411  (Adequate.valid adequate Two boolean env2)
  holds412 : (z0 z1 : A2) → (mul2 (mul2 z0 z0) (mul2 (mul2 z1 z1) z1)) ≡ z0
  holds412 z0 z1 = refl
  cut412 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (op (var 1) (var 1)) (var 1))) , (var 0)) → ⊥
  cut412  = reject2 ((op (op (var 0) (var 0)) (op (op (var 1) (var 1)) (var 1))) , (var 0)) (λ env → holds412 (env 0) (env 1))
  bad413 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b1 b1) b1)) b1 → ⊥
  bad413  p = false≢true (cong lower p)
  cut413 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (op (var 1) (var 1)) (var 1))) , (var 1)) → ⊥
  cut413  adequate = bad413  (Adequate.valid adequate Two boolean env0)
  bad414 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b0 b0) b0)) b1 → ⊥
  bad414  p = false≢true (cong lower p)
  cut414 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (op (var 1) (var 1)) (var 1))) , (var 2)) → ⊥
  cut414  adequate = bad414  (Adequate.valid adequate Two boolean env2)
  bad415 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b0 b0) b1)) b0 → ⊥
  bad415  p = false≢true (sym (cong lower p))
  cut415 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (op (var 1) (var 1)) (var 2))) , (var 0)) → ⊥
  cut415  adequate = bad415  (Adequate.valid adequate Two boolean env2)
  bad416 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b0 b0) b1)) b0 → ⊥
  bad416  p = false≢true (sym (cong lower p))
  cut416 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (op (var 1) (var 1)) (var 2))) , (var 1)) → ⊥
  cut416  adequate = bad416  (Adequate.valid adequate Two boolean env2)
  env5 : ℕ → Two
  env5 zero = b0
  env5 (suc zero) = b1
  env5 (suc (suc zero)) = b1
  env5 (suc (suc (suc rest))) = b0
  bad417 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b1 b1) b1)) b1 → ⊥
  bad417  p = false≢true (cong lower p)
  cut417 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (op (var 1) (var 1)) (var 2))) , (var 2)) → ⊥
  cut417  adequate = bad417  (Adequate.valid adequate Two boolean env5)
  bad418 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b0 b0) b0)) b1 → ⊥
  bad418  p = false≢true (cong lower p)
  cut418 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (op (var 1) (var 1)) (var 2))) , (var 3)) → ⊥
  cut418  adequate = bad418  (Adequate.valid adequate Two boolean env4)
  holds419 : (z0 z1 z2 : A2) → (mul2 (mul2 z0 z0) (mul2 (mul2 z1 z2) z0)) ≡ z0
  holds419 z0 z1 z2 = refl
  cut419 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (op (var 1) (var 2)) (var 0))) , (var 0)) → ⊥
  cut419  = reject2 ((op (op (var 0) (var 0)) (op (op (var 1) (var 2)) (var 0))) , (var 0)) (λ env → holds419 (env 0) (env 1) (env 2))
  env6 : ℕ → Two
  env6 zero = b0
  env6 (suc zero) = b1
  env6 (suc (suc zero)) = b0
  env6 (suc (suc (suc rest))) = b0
  bad420 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b1 b0) b0)) b1 → ⊥
  bad420  p = false≢true (cong lower p)
  cut420 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (op (var 1) (var 2)) (var 0))) , (var 1)) → ⊥
  cut420  adequate = bad420  (Adequate.valid adequate Two boolean env6)
  bad421 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b0 b1) b0)) b1 → ⊥
  bad421  p = false≢true (cong lower p)
  cut421 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (op (var 1) (var 2)) (var 0))) , (var 2)) → ⊥
  cut421  adequate = bad421  (Adequate.valid adequate Two boolean env2)
  bad422 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b0 b0) b0)) b1 → ⊥
  bad422  p = false≢true (cong lower p)
  cut422 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (op (var 1) (var 2)) (var 0))) , (var 3)) → ⊥
  cut422  adequate = bad422  (Adequate.valid adequate Two boolean env4)
  bad423 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b1 b0) b1)) b0 → ⊥
  bad423  p = false≢true (sym (cong lower p))
  cut423 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (op (var 1) (var 2)) (var 1))) , (var 0)) → ⊥
  cut423  adequate = bad423  (Adequate.valid adequate Two boolean env6)
  bad424 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b1 b1) b1)) b1 → ⊥
  bad424  p = false≢true (cong lower p)
  cut424 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (op (var 1) (var 2)) (var 1))) , (var 1)) → ⊥
  cut424  adequate = bad424  (Adequate.valid adequate Two boolean env5)
  bad425 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b0 b1) b0)) b1 → ⊥
  bad425  p = false≢true (cong lower p)
  cut425 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (op (var 1) (var 2)) (var 1))) , (var 2)) → ⊥
  cut425  adequate = bad425  (Adequate.valid adequate Two boolean env2)
  bad426 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b0 b0) b0)) b1 → ⊥
  bad426  p = false≢true (cong lower p)
  cut426 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (op (var 1) (var 2)) (var 1))) , (var 3)) → ⊥
  cut426  adequate = bad426  (Adequate.valid adequate Two boolean env4)
  bad427 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b0 b1) b1)) b0 → ⊥
  bad427  p = false≢true (sym (cong lower p))
  cut427 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (op (var 1) (var 2)) (var 2))) , (var 0)) → ⊥
  cut427  adequate = bad427  (Adequate.valid adequate Two boolean env2)
  bad428 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b0 b1) b1)) b0 → ⊥
  bad428  p = false≢true (sym (cong lower p))
  cut428 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (op (var 1) (var 2)) (var 2))) , (var 1)) → ⊥
  cut428  adequate = bad428  (Adequate.valid adequate Two boolean env2)
  bad429 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b1 b1) b1)) b1 → ⊥
  bad429  p = false≢true (cong lower p)
  cut429 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (op (var 1) (var 2)) (var 2))) , (var 2)) → ⊥
  cut429  adequate = bad429  (Adequate.valid adequate Two boolean env5)
  bad430 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b0 b0) b0)) b1 → ⊥
  bad430  p = false≢true (cong lower p)
  cut430 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (op (var 1) (var 2)) (var 2))) , (var 3)) → ⊥
  cut430  adequate = bad430  (Adequate.valid adequate Two boolean env4)
  bad431 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b0 b0) b1)) b0 → ⊥
  bad431  p = false≢true (sym (cong lower p))
  cut431 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (op (var 1) (var 2)) (var 3))) , (var 0)) → ⊥
  cut431  adequate = bad431  (Adequate.valid adequate Two boolean env4)
  bad432 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b0 b0) b1)) b0 → ⊥
  bad432  p = false≢true (sym (cong lower p))
  cut432 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (op (var 1) (var 2)) (var 3))) , (var 1)) → ⊥
  cut432  adequate = bad432  (Adequate.valid adequate Two boolean env4)
  bad433 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b0 b0) b1)) b0 → ⊥
  bad433  p = false≢true (sym (cong lower p))
  cut433 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (op (var 1) (var 2)) (var 3))) , (var 2)) → ⊥
  cut433  adequate = bad433  (Adequate.valid adequate Two boolean env4)
  env7 : ℕ → Two
  env7 zero = b0
  env7 (suc zero) = b1
  env7 (suc (suc zero)) = b1
  env7 (suc (suc (suc zero))) = b1
  env7 (suc (suc (suc (suc rest)))) = b0
  bad434 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b1 b1) b1)) b1 → ⊥
  bad434  p = false≢true (cong lower p)
  cut434 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (op (var 1) (var 2)) (var 3))) , (var 3)) → ⊥
  cut434  adequate = bad434  (Adequate.valid adequate Two boolean env7)
  env8 : ℕ → Two
  env8 zero = b0
  env8 (suc zero) = b0
  env8 (suc (suc zero)) = b0
  env8 (suc (suc (suc zero))) = b0
  env8 (suc (suc (suc (suc zero)))) = b1
  env8 (suc (suc (suc (suc (suc rest))))) = b0
  bad435 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b0 b0) b0)) b1 → ⊥
  bad435  p = false≢true (cong lower p)
  cut435 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (op (var 1) (var 2)) (var 3))) , (var 4)) → ⊥
  cut435  adequate = bad435  (Adequate.valid adequate Two boolean env8)
  bad436 : PathP (λ _ → Two) (bop (bop b1 b0) (bop (bop b1 b1) b1)) b1 → ⊥
  bad436  p = false≢true (cong lower p)
  cut436 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 0) (var 0)) (var 0))) , (var 0)) → ⊥
  cut436  adequate = bad436  (Adequate.valid adequate Two boolean env1)
  bad437 : PathP (λ _ → Two) (bop (bop b0 b1) (bop (bop b0 b0) b0)) b1 → ⊥
  bad437  p = false≢true (cong lower p)
  cut437 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 0) (var 0)) (var 0))) , (var 1)) → ⊥
  cut437  adequate = bad437  (Adequate.valid adequate Two boolean env0)
  bad438 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b0 b0) b0)) b1 → ⊥
  bad438  p = false≢true (cong lower p)
  cut438 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 0) (var 0)) (var 0))) , (var 2)) → ⊥
  cut438  adequate = bad438  (Adequate.valid adequate Two boolean env2)
  bad439 : PathP (λ _ → Two) (bop (bop b0 b1) (bop (bop b0 b0) b1)) b0 → ⊥
  bad439  p = false≢true (sym (cong lower p))
  cut439 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 0) (var 0)) (var 1))) , (var 0)) → ⊥
  cut439  adequate = bad439  (Adequate.valid adequate Two boolean env0)
  holds440 : (z0 z1 : A3) → (mul3 (mul3 z0 z1) (mul3 (mul3 z0 z0) z1)) ≡ z1
  holds440 z0 z1 = refl
  cut440 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 0) (var 0)) (var 1))) , (var 1)) → ⊥
  cut440  = reject3 ((op (op (var 0) (var 1)) (op (op (var 0) (var 0)) (var 1))) , (var 1)) (λ env → holds440 (env 0) (env 1))
  bad441 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b0 b0) b0)) b1 → ⊥
  bad441  p = false≢true (cong lower p)
  cut441 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 0) (var 0)) (var 1))) , (var 2)) → ⊥
  cut441  adequate = bad441  (Adequate.valid adequate Two boolean env2)
  bad442 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b0 b0) b1)) b0 → ⊥
  bad442  p = false≢true (sym (cong lower p))
  cut442 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 0) (var 0)) (var 2))) , (var 0)) → ⊥
  cut442  adequate = bad442  (Adequate.valid adequate Two boolean env2)
  bad443 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b0 b0) b1)) b0 → ⊥
  bad443  p = false≢true (sym (cong lower p))
  cut443 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 0) (var 0)) (var 2))) , (var 1)) → ⊥
  cut443  adequate = bad443  (Adequate.valid adequate Two boolean env2)
  env9 : ℕ → Two
  env9 zero = b1
  env9 (suc zero) = b0
  env9 (suc (suc zero)) = b1
  env9 (suc (suc (suc rest))) = b0
  bad444 : PathP (λ _ → Two) (bop (bop b1 b0) (bop (bop b1 b1) b1)) b1 → ⊥
  bad444  p = false≢true (cong lower p)
  cut444 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 0) (var 0)) (var 2))) , (var 2)) → ⊥
  cut444  adequate = bad444  (Adequate.valid adequate Two boolean env9)
  bad445 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b0 b0) b0)) b1 → ⊥
  bad445  p = false≢true (cong lower p)
  cut445 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 0) (var 0)) (var 2))) , (var 3)) → ⊥
  cut445  adequate = bad445  (Adequate.valid adequate Two boolean env4)
  holds446 : (z0 z1 : A2) → (mul2 (mul2 z0 z1) (mul2 (mul2 z0 z1) z0)) ≡ z0
  holds446 z0 z1 = refl
  cut446 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 0) (var 1)) (var 0))) , (var 0)) → ⊥
  cut446  = reject2 ((op (op (var 0) (var 1)) (op (op (var 0) (var 1)) (var 0))) , (var 0)) (λ env → holds446 (env 0) (env 1))
  bad447 : PathP (λ _ → Two) (bop (bop b0 b1) (bop (bop b0 b1) b0)) b1 → ⊥
  bad447  p = false≢true (cong lower p)
  cut447 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 0) (var 1)) (var 0))) , (var 1)) → ⊥
  cut447  adequate = bad447  (Adequate.valid adequate Two boolean env0)
  bad448 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b0 b0) b0)) b1 → ⊥
  bad448  p = false≢true (cong lower p)
  cut448 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 0) (var 1)) (var 0))) , (var 2)) → ⊥
  cut448  adequate = bad448  (Adequate.valid adequate Two boolean env2)
  bad449 : PathP (λ _ → Two) (bop (bop b0 b1) (bop (bop b0 b1) b1)) b0 → ⊥
  bad449  p = false≢true (sym (cong lower p))
  cut449 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 0) (var 1)) (var 1))) , (var 0)) → ⊥
  cut449  adequate = bad449  (Adequate.valid adequate Two boolean env0)
  holds450 : (z0 z1 : A3) → (mul3 (mul3 z0 z1) (mul3 (mul3 z0 z1) z1)) ≡ z1
  holds450 z0 z1 = refl
  cut450 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 0) (var 1)) (var 1))) , (var 1)) → ⊥
  cut450  = reject3 ((op (op (var 0) (var 1)) (op (op (var 0) (var 1)) (var 1))) , (var 1)) (λ env → holds450 (env 0) (env 1))
  bad451 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b0 b0) b0)) b1 → ⊥
  bad451  p = false≢true (cong lower p)
  cut451 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 0) (var 1)) (var 1))) , (var 2)) → ⊥
  cut451  adequate = bad451  (Adequate.valid adequate Two boolean env2)
  bad452 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b0 b0) b1)) b0 → ⊥
  bad452  p = false≢true (sym (cong lower p))
  cut452 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 0) (var 1)) (var 2))) , (var 0)) → ⊥
  cut452  adequate = bad452  (Adequate.valid adequate Two boolean env2)
  bad453 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b0 b0) b1)) b0 → ⊥
  bad453  p = false≢true (sym (cong lower p))
  cut453 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 0) (var 1)) (var 2))) , (var 1)) → ⊥
  cut453  adequate = bad453  (Adequate.valid adequate Two boolean env2)
  env10 : ℕ → Two
  env10 zero = b1
  env10 (suc zero) = b1
  env10 (suc (suc zero)) = b0
  env10 (suc (suc (suc rest))) = b0
  bad454 : PathP (λ _ → Two) (bop (bop b1 b1) (bop (bop b1 b1) b0)) b0 → ⊥
  bad454  p = false≢true (sym (cong lower p))
  cut454 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 0) (var 1)) (var 2))) , (var 2)) → ⊥
  cut454  adequate = bad454  (Adequate.valid adequate Two boolean env10)
  bad455 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b0 b0) b0)) b1 → ⊥
  bad455  p = false≢true (cong lower p)
  cut455 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 0) (var 1)) (var 2))) , (var 3)) → ⊥
  cut455  adequate = bad455  (Adequate.valid adequate Two boolean env4)
  bad456 : PathP (λ _ → Two) (bop (bop b1 b0) (bop (bop b1 b1) b1)) b1 → ⊥
  bad456  p = false≢true (cong lower p)
  cut456 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 0) (var 2)) (var 0))) , (var 0)) → ⊥
  cut456  adequate = bad456  (Adequate.valid adequate Two boolean env9)
  bad457 : PathP (λ _ → Two) (bop (bop b0 b1) (bop (bop b0 b0) b0)) b1 → ⊥
  bad457  p = false≢true (cong lower p)
  cut457 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 0) (var 2)) (var 0))) , (var 1)) → ⊥
  cut457  adequate = bad457  (Adequate.valid adequate Two boolean env6)
  bad458 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b0 b1) b0)) b1 → ⊥
  bad458  p = false≢true (cong lower p)
  cut458 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 0) (var 2)) (var 0))) , (var 2)) → ⊥
  cut458  adequate = bad458  (Adequate.valid adequate Two boolean env2)
  bad459 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b0 b0) b0)) b1 → ⊥
  bad459  p = false≢true (cong lower p)
  cut459 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 0) (var 2)) (var 0))) , (var 3)) → ⊥
  cut459  adequate = bad459  (Adequate.valid adequate Two boolean env4)
  bad460 : PathP (λ _ → Two) (bop (bop b0 b1) (bop (bop b0 b0) b1)) b0 → ⊥
  bad460  p = false≢true (sym (cong lower p))
  cut460 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 0) (var 2)) (var 1))) , (var 0)) → ⊥
  cut460  adequate = bad460  (Adequate.valid adequate Two boolean env6)
  holds461 : (z0 z1 z2 : A3) → (mul3 (mul3 z0 z1) (mul3 (mul3 z0 z2) z1)) ≡ z1
  holds461 z0 z1 z2 = refl
  cut461 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 0) (var 2)) (var 1))) , (var 1)) → ⊥
  cut461  = reject3 ((op (op (var 0) (var 1)) (op (op (var 0) (var 2)) (var 1))) , (var 1)) (λ env → holds461 (env 0) (env 1) (env 2))
  bad462 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b0 b1) b0)) b1 → ⊥
  bad462  p = false≢true (cong lower p)
  cut462 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 0) (var 2)) (var 1))) , (var 2)) → ⊥
  cut462  adequate = bad462  (Adequate.valid adequate Two boolean env2)
  bad463 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b0 b0) b0)) b1 → ⊥
  bad463  p = false≢true (cong lower p)
  cut463 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 0) (var 2)) (var 1))) , (var 3)) → ⊥
  cut463  adequate = bad463  (Adequate.valid adequate Two boolean env4)
  bad464 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b0 b1) b1)) b0 → ⊥
  bad464  p = false≢true (sym (cong lower p))
  cut464 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 0) (var 2)) (var 2))) , (var 0)) → ⊥
  cut464  adequate = bad464  (Adequate.valid adequate Two boolean env2)
  bad465 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b0 b1) b1)) b0 → ⊥
  bad465  p = false≢true (sym (cong lower p))
  cut465 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 0) (var 2)) (var 2))) , (var 1)) → ⊥
  cut465  adequate = bad465  (Adequate.valid adequate Two boolean env2)
  bad466 : PathP (λ _ → Two) (bop (bop b1 b0) (bop (bop b1 b1) b1)) b1 → ⊥
  bad466  p = false≢true (cong lower p)
  cut466 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 0) (var 2)) (var 2))) , (var 2)) → ⊥
  cut466  adequate = bad466  (Adequate.valid adequate Two boolean env9)
  bad467 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b0 b0) b0)) b1 → ⊥
  bad467  p = false≢true (cong lower p)
  cut467 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 0) (var 2)) (var 2))) , (var 3)) → ⊥
  cut467  adequate = bad467  (Adequate.valid adequate Two boolean env4)
  bad468 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b0 b0) b1)) b0 → ⊥
  bad468  p = false≢true (sym (cong lower p))
  cut468 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 0) (var 2)) (var 3))) , (var 0)) → ⊥
  cut468  adequate = bad468  (Adequate.valid adequate Two boolean env4)
  bad469 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b0 b0) b1)) b0 → ⊥
  bad469  p = false≢true (sym (cong lower p))
  cut469 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 0) (var 2)) (var 3))) , (var 1)) → ⊥
  cut469  adequate = bad469  (Adequate.valid adequate Two boolean env4)
  bad470 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b0 b0) b1)) b0 → ⊥
  bad470  p = false≢true (sym (cong lower p))
  cut470 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 0) (var 2)) (var 3))) , (var 2)) → ⊥
  cut470  adequate = bad470  (Adequate.valid adequate Two boolean env4)
  env11 : ℕ → Two
  env11 zero = b1
  env11 (suc zero) = b0
  env11 (suc (suc zero)) = b1
  env11 (suc (suc (suc zero))) = b1
  env11 (suc (suc (suc (suc rest)))) = b0
  bad471 : PathP (λ _ → Two) (bop (bop b1 b0) (bop (bop b1 b1) b1)) b1 → ⊥
  bad471  p = false≢true (cong lower p)
  cut471 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 0) (var 2)) (var 3))) , (var 3)) → ⊥
  cut471  adequate = bad471  (Adequate.valid adequate Two boolean env11)
  bad472 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b0 b0) b0)) b1 → ⊥
  bad472  p = false≢true (cong lower p)
  cut472 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 0) (var 2)) (var 3))) , (var 4)) → ⊥
  cut472  adequate = bad472  (Adequate.valid adequate Two boolean env8)
  holds473 : (z0 z1 : A2) → (mul2 (mul2 z0 z1) (mul2 (mul2 z1 z0) z0)) ≡ z0
  holds473 z0 z1 = refl
  cut473 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 1) (var 0)) (var 0))) , (var 0)) → ⊥
  cut473  = reject2 ((op (op (var 0) (var 1)) (op (op (var 1) (var 0)) (var 0))) , (var 0)) (λ env → holds473 (env 0) (env 1))
  bad474 : PathP (λ _ → Two) (bop (bop b0 b1) (bop (bop b1 b0) b0)) b1 → ⊥
  bad474  p = false≢true (cong lower p)
  cut474 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 1) (var 0)) (var 0))) , (var 1)) → ⊥
  cut474  adequate = bad474  (Adequate.valid adequate Two boolean env0)
  bad475 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b0 b0) b0)) b1 → ⊥
  bad475  p = false≢true (cong lower p)
  cut475 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 1) (var 0)) (var 0))) , (var 2)) → ⊥
  cut475  adequate = bad475  (Adequate.valid adequate Two boolean env2)
  bad476 : PathP (λ _ → Two) (bop (bop b0 b1) (bop (bop b1 b0) b1)) b0 → ⊥
  bad476  p = false≢true (sym (cong lower p))
  cut476 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 1) (var 0)) (var 1))) , (var 0)) → ⊥
  cut476  adequate = bad476  (Adequate.valid adequate Two boolean env0)
  holds477 : (z0 z1 : A3) → (mul3 (mul3 z0 z1) (mul3 (mul3 z1 z0) z1)) ≡ z1
  holds477 z0 z1 = refl
  cut477 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 1) (var 0)) (var 1))) , (var 1)) → ⊥
  cut477  = reject3 ((op (op (var 0) (var 1)) (op (op (var 1) (var 0)) (var 1))) , (var 1)) (λ env → holds477 (env 0) (env 1))
  bad478 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b0 b0) b0)) b1 → ⊥
  bad478  p = false≢true (cong lower p)
  cut478 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 1) (var 0)) (var 1))) , (var 2)) → ⊥
  cut478  adequate = bad478  (Adequate.valid adequate Two boolean env2)
  bad479 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b0 b0) b1)) b0 → ⊥
  bad479  p = false≢true (sym (cong lower p))
  cut479 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 1) (var 0)) (var 2))) , (var 0)) → ⊥
  cut479  adequate = bad479  (Adequate.valid adequate Two boolean env2)
  bad480 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b0 b0) b1)) b0 → ⊥
  bad480  p = false≢true (sym (cong lower p))
  cut480 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 1) (var 0)) (var 2))) , (var 1)) → ⊥
  cut480  adequate = bad480  (Adequate.valid adequate Two boolean env2)
  bad481 : PathP (λ _ → Two) (bop (bop b1 b1) (bop (bop b1 b1) b0)) b0 → ⊥
  bad481  p = false≢true (sym (cong lower p))
  cut481 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 1) (var 0)) (var 2))) , (var 2)) → ⊥
  cut481  adequate = bad481  (Adequate.valid adequate Two boolean env10)
  bad482 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b0 b0) b0)) b1 → ⊥
  bad482  p = false≢true (cong lower p)
  cut482 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 1) (var 0)) (var 2))) , (var 3)) → ⊥
  cut482  adequate = bad482  (Adequate.valid adequate Two boolean env4)
  holds483 : (z0 z1 : A2) → (mul2 (mul2 z0 z1) (mul2 (mul2 z1 z1) z0)) ≡ z0
  holds483 z0 z1 = refl
  cut483 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 1) (var 1)) (var 0))) , (var 0)) → ⊥
  cut483  = reject2 ((op (op (var 0) (var 1)) (op (op (var 1) (var 1)) (var 0))) , (var 0)) (λ env → holds483 (env 0) (env 1))
  bad484 : PathP (λ _ → Two) (bop (bop b0 b1) (bop (bop b1 b1) b0)) b1 → ⊥
  bad484  p = false≢true (cong lower p)
  cut484 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 1) (var 1)) (var 0))) , (var 1)) → ⊥
  cut484  adequate = bad484  (Adequate.valid adequate Two boolean env0)
  bad485 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b0 b0) b0)) b1 → ⊥
  bad485  p = false≢true (cong lower p)
  cut485 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 1) (var 1)) (var 0))) , (var 2)) → ⊥
  cut485  adequate = bad485  (Adequate.valid adequate Two boolean env2)
  bad486 : PathP (λ _ → Two) (bop (bop b1 b0) (bop (bop b0 b0) b0)) b1 → ⊥
  bad486  p = false≢true (cong lower p)
  cut486 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 1) (var 1)) (var 1))) , (var 0)) → ⊥
  cut486  adequate = bad486  (Adequate.valid adequate Two boolean env1)
  bad487 : PathP (λ _ → Two) (bop (bop b0 b1) (bop (bop b1 b1) b1)) b1 → ⊥
  bad487  p = false≢true (cong lower p)
  cut487 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 1) (var 1)) (var 1))) , (var 1)) → ⊥
  cut487  adequate = bad487  (Adequate.valid adequate Two boolean env0)
  bad488 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b0 b0) b0)) b1 → ⊥
  bad488  p = false≢true (cong lower p)
  cut488 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 1) (var 1)) (var 1))) , (var 2)) → ⊥
  cut488  adequate = bad488  (Adequate.valid adequate Two boolean env2)
  bad489 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b0 b0) b1)) b0 → ⊥
  bad489  p = false≢true (sym (cong lower p))
  cut489 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 1) (var 1)) (var 2))) , (var 0)) → ⊥
  cut489  adequate = bad489  (Adequate.valid adequate Two boolean env2)
  bad490 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b0 b0) b1)) b0 → ⊥
  bad490  p = false≢true (sym (cong lower p))
  cut490 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 1) (var 1)) (var 2))) , (var 1)) → ⊥
  cut490  adequate = bad490  (Adequate.valid adequate Two boolean env2)
  bad491 : PathP (λ _ → Two) (bop (bop b0 b1) (bop (bop b1 b1) b1)) b1 → ⊥
  bad491  p = false≢true (cong lower p)
  cut491 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 1) (var 1)) (var 2))) , (var 2)) → ⊥
  cut491  adequate = bad491  (Adequate.valid adequate Two boolean env5)
  bad492 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b0 b0) b0)) b1 → ⊥
  bad492  p = false≢true (cong lower p)
  cut492 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 1) (var 1)) (var 2))) , (var 3)) → ⊥
  cut492  adequate = bad492  (Adequate.valid adequate Two boolean env4)
  holds493 : (z0 z1 z2 : A2) → (mul2 (mul2 z0 z1) (mul2 (mul2 z1 z2) z0)) ≡ z0
  holds493 z0 z1 z2 = refl
  cut493 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 1) (var 2)) (var 0))) , (var 0)) → ⊥
  cut493  = reject2 ((op (op (var 0) (var 1)) (op (op (var 1) (var 2)) (var 0))) , (var 0)) (λ env → holds493 (env 0) (env 1) (env 2))
  bad494 : PathP (λ _ → Two) (bop (bop b0 b1) (bop (bop b1 b0) b0)) b1 → ⊥
  bad494  p = false≢true (cong lower p)
  cut494 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 1) (var 2)) (var 0))) , (var 1)) → ⊥
  cut494  adequate = bad494  (Adequate.valid adequate Two boolean env6)
  bad495 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b0 b1) b0)) b1 → ⊥
  bad495  p = false≢true (cong lower p)
  cut495 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 1) (var 2)) (var 0))) , (var 2)) → ⊥
  cut495  adequate = bad495  (Adequate.valid adequate Two boolean env2)
  bad496 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b0 b0) b0)) b1 → ⊥
  bad496  p = false≢true (cong lower p)
  cut496 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 1) (var 2)) (var 0))) , (var 3)) → ⊥
  cut496  adequate = bad496  (Adequate.valid adequate Two boolean env4)
  bad497 : PathP (λ _ → Two) (bop (bop b0 b1) (bop (bop b1 b0) b1)) b0 → ⊥
  bad497  p = false≢true (sym (cong lower p))
  cut497 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 1) (var 2)) (var 1))) , (var 0)) → ⊥
  cut497  adequate = bad497  (Adequate.valid adequate Two boolean env6)
  bad498 : PathP (λ _ → Two) (bop (bop b0 b1) (bop (bop b1 b1) b1)) b1 → ⊥
  bad498  p = false≢true (cong lower p)
  cut498 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 1) (var 2)) (var 1))) , (var 1)) → ⊥
  cut498  adequate = bad498  (Adequate.valid adequate Two boolean env5)
  bad499 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b0 b1) b0)) b1 → ⊥
  bad499  p = false≢true (cong lower p)
  cut499 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 1) (var 2)) (var 1))) , (var 2)) → ⊥
  cut499  adequate = bad499  (Adequate.valid adequate Two boolean env2)
  bad500 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b0 b0) b0)) b1 → ⊥
  bad500  p = false≢true (cong lower p)
  cut500 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 1) (var 2)) (var 1))) , (var 3)) → ⊥
  cut500  adequate = bad500  (Adequate.valid adequate Two boolean env4)
  bad501 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b0 b1) b1)) b0 → ⊥
  bad501  p = false≢true (sym (cong lower p))
  cut501 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 1) (var 2)) (var 2))) , (var 0)) → ⊥
  cut501  adequate = bad501  (Adequate.valid adequate Two boolean env2)
  bad502 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b0 b1) b1)) b0 → ⊥
  bad502  p = false≢true (sym (cong lower p))
  cut502 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 1) (var 2)) (var 2))) , (var 1)) → ⊥
  cut502  adequate = bad502  (Adequate.valid adequate Two boolean env2)
  bad503 : PathP (λ _ → Two) (bop (bop b0 b1) (bop (bop b1 b1) b1)) b1 → ⊥
  bad503  p = false≢true (cong lower p)
  cut503 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 1) (var 2)) (var 2))) , (var 2)) → ⊥
  cut503  adequate = bad503  (Adequate.valid adequate Two boolean env5)
  bad504 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b0 b0) b0)) b1 → ⊥
  bad504  p = false≢true (cong lower p)
  cut504 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 1) (var 2)) (var 2))) , (var 3)) → ⊥
  cut504  adequate = bad504  (Adequate.valid adequate Two boolean env4)
  bad505 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b0 b0) b1)) b0 → ⊥
  bad505  p = false≢true (sym (cong lower p))
  cut505 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 1) (var 2)) (var 3))) , (var 0)) → ⊥
  cut505  adequate = bad505  (Adequate.valid adequate Two boolean env4)
  bad506 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b0 b0) b1)) b0 → ⊥
  bad506  p = false≢true (sym (cong lower p))
  cut506 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 1) (var 2)) (var 3))) , (var 1)) → ⊥
  cut506  adequate = bad506  (Adequate.valid adequate Two boolean env4)
  bad507 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b0 b0) b1)) b0 → ⊥
  bad507  p = false≢true (sym (cong lower p))
  cut507 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 1) (var 2)) (var 3))) , (var 2)) → ⊥
  cut507  adequate = bad507  (Adequate.valid adequate Two boolean env4)
  bad508 : PathP (λ _ → Two) (bop (bop b0 b1) (bop (bop b1 b1) b1)) b1 → ⊥
  bad508  p = false≢true (cong lower p)
  cut508 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 1) (var 2)) (var 3))) , (var 3)) → ⊥
  cut508  adequate = bad508  (Adequate.valid adequate Two boolean env7)
  bad509 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b0 b0) b0)) b1 → ⊥
  bad509  p = false≢true (cong lower p)
  cut509 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 1) (var 2)) (var 3))) , (var 4)) → ⊥
  cut509  adequate = bad509  (Adequate.valid adequate Two boolean env8)
  bad510 : PathP (λ _ → Two) (bop (bop b1 b0) (bop (bop b1 b1) b1)) b1 → ⊥
  bad510  p = false≢true (cong lower p)
  cut510 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 2) (var 0)) (var 0))) , (var 0)) → ⊥
  cut510  adequate = bad510  (Adequate.valid adequate Two boolean env9)
  bad511 : PathP (λ _ → Two) (bop (bop b0 b1) (bop (bop b0 b0) b0)) b1 → ⊥
  bad511  p = false≢true (cong lower p)
  cut511 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 2) (var 0)) (var 0))) , (var 1)) → ⊥
  cut511  adequate = bad511  (Adequate.valid adequate Two boolean env6)
  bad512 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b1 b0) b0)) b1 → ⊥
  bad512  p = false≢true (cong lower p)
  cut512 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 2) (var 0)) (var 0))) , (var 2)) → ⊥
  cut512  adequate = bad512  (Adequate.valid adequate Two boolean env2)
  bad513 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b0 b0) b0)) b1 → ⊥
  bad513  p = false≢true (cong lower p)
  cut513 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 2) (var 0)) (var 0))) , (var 3)) → ⊥
  cut513  adequate = bad513  (Adequate.valid adequate Two boolean env4)
  bad514 : PathP (λ _ → Two) (bop (bop b0 b1) (bop (bop b0 b0) b1)) b0 → ⊥
  bad514  p = false≢true (sym (cong lower p))
  cut514 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 2) (var 0)) (var 1))) , (var 0)) → ⊥
  cut514  adequate = bad514  (Adequate.valid adequate Two boolean env6)
  holds515 : (z0 z1 z2 : A3) → (mul3 (mul3 z0 z1) (mul3 (mul3 z2 z0) z1)) ≡ z1
  holds515 z0 z1 z2 = refl
  cut515 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 2) (var 0)) (var 1))) , (var 1)) → ⊥
  cut515  = reject3 ((op (op (var 0) (var 1)) (op (op (var 2) (var 0)) (var 1))) , (var 1)) (λ env → holds515 (env 0) (env 1) (env 2))
  bad516 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b1 b0) b0)) b1 → ⊥
  bad516  p = false≢true (cong lower p)
  cut516 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 2) (var 0)) (var 1))) , (var 2)) → ⊥
  cut516  adequate = bad516  (Adequate.valid adequate Two boolean env2)
  bad517 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b0 b0) b0)) b1 → ⊥
  bad517  p = false≢true (cong lower p)
  cut517 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 2) (var 0)) (var 1))) , (var 3)) → ⊥
  cut517  adequate = bad517  (Adequate.valid adequate Two boolean env4)
  bad518 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b1 b0) b1)) b0 → ⊥
  bad518  p = false≢true (sym (cong lower p))
  cut518 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 2) (var 0)) (var 2))) , (var 0)) → ⊥
  cut518  adequate = bad518  (Adequate.valid adequate Two boolean env2)
  bad519 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b1 b0) b1)) b0 → ⊥
  bad519  p = false≢true (sym (cong lower p))
  cut519 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 2) (var 0)) (var 2))) , (var 1)) → ⊥
  cut519  adequate = bad519  (Adequate.valid adequate Two boolean env2)
  bad520 : PathP (λ _ → Two) (bop (bop b1 b0) (bop (bop b1 b1) b1)) b1 → ⊥
  bad520  p = false≢true (cong lower p)
  cut520 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 2) (var 0)) (var 2))) , (var 2)) → ⊥
  cut520  adequate = bad520  (Adequate.valid adequate Two boolean env9)
  bad521 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b0 b0) b0)) b1 → ⊥
  bad521  p = false≢true (cong lower p)
  cut521 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 2) (var 0)) (var 2))) , (var 3)) → ⊥
  cut521  adequate = bad521  (Adequate.valid adequate Two boolean env4)
  bad522 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b0 b0) b1)) b0 → ⊥
  bad522  p = false≢true (sym (cong lower p))
  cut522 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 2) (var 0)) (var 3))) , (var 0)) → ⊥
  cut522  adequate = bad522  (Adequate.valid adequate Two boolean env4)
  bad523 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b0 b0) b1)) b0 → ⊥
  bad523  p = false≢true (sym (cong lower p))
  cut523 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 2) (var 0)) (var 3))) , (var 1)) → ⊥
  cut523  adequate = bad523  (Adequate.valid adequate Two boolean env4)
  bad524 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b0 b0) b1)) b0 → ⊥
  bad524  p = false≢true (sym (cong lower p))
  cut524 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 2) (var 0)) (var 3))) , (var 2)) → ⊥
  cut524  adequate = bad524  (Adequate.valid adequate Two boolean env4)
  bad525 : PathP (λ _ → Two) (bop (bop b1 b0) (bop (bop b1 b1) b1)) b1 → ⊥
  bad525  p = false≢true (cong lower p)
  cut525 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 2) (var 0)) (var 3))) , (var 3)) → ⊥
  cut525  adequate = bad525  (Adequate.valid adequate Two boolean env11)
  bad526 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b0 b0) b0)) b1 → ⊥
  bad526  p = false≢true (cong lower p)
  cut526 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 2) (var 0)) (var 3))) , (var 4)) → ⊥
  cut526  adequate = bad526  (Adequate.valid adequate Two boolean env8)
  holds527 : (z0 z1 z2 : A2) → (mul2 (mul2 z0 z1) (mul2 (mul2 z2 z1) z0)) ≡ z0
  holds527 z0 z1 z2 = refl
  cut527 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 2) (var 1)) (var 0))) , (var 0)) → ⊥
  cut527  = reject2 ((op (op (var 0) (var 1)) (op (op (var 2) (var 1)) (var 0))) , (var 0)) (λ env → holds527 (env 0) (env 1) (env 2))
  bad528 : PathP (λ _ → Two) (bop (bop b0 b1) (bop (bop b0 b1) b0)) b1 → ⊥
  bad528  p = false≢true (cong lower p)
  cut528 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 2) (var 1)) (var 0))) , (var 1)) → ⊥
  cut528  adequate = bad528  (Adequate.valid adequate Two boolean env6)
  bad529 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b1 b0) b0)) b1 → ⊥
  bad529  p = false≢true (cong lower p)
  cut529 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 2) (var 1)) (var 0))) , (var 2)) → ⊥
  cut529  adequate = bad529  (Adequate.valid adequate Two boolean env2)
  bad530 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b0 b0) b0)) b1 → ⊥
  bad530  p = false≢true (cong lower p)
  cut530 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 2) (var 1)) (var 0))) , (var 3)) → ⊥
  cut530  adequate = bad530  (Adequate.valid adequate Two boolean env4)
  bad531 : PathP (λ _ → Two) (bop (bop b0 b1) (bop (bop b0 b1) b1)) b0 → ⊥
  bad531  p = false≢true (sym (cong lower p))
  cut531 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 2) (var 1)) (var 1))) , (var 0)) → ⊥
  cut531  adequate = bad531  (Adequate.valid adequate Two boolean env6)
  bad532 : PathP (λ _ → Two) (bop (bop b0 b1) (bop (bop b1 b1) b1)) b1 → ⊥
  bad532  p = false≢true (cong lower p)
  cut532 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 2) (var 1)) (var 1))) , (var 1)) → ⊥
  cut532  adequate = bad532  (Adequate.valid adequate Two boolean env5)
  bad533 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b1 b0) b0)) b1 → ⊥
  bad533  p = false≢true (cong lower p)
  cut533 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 2) (var 1)) (var 1))) , (var 2)) → ⊥
  cut533  adequate = bad533  (Adequate.valid adequate Two boolean env2)
  bad534 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b0 b0) b0)) b1 → ⊥
  bad534  p = false≢true (cong lower p)
  cut534 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 2) (var 1)) (var 1))) , (var 3)) → ⊥
  cut534  adequate = bad534  (Adequate.valid adequate Two boolean env4)
  bad535 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b1 b0) b1)) b0 → ⊥
  bad535  p = false≢true (sym (cong lower p))
  cut535 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 2) (var 1)) (var 2))) , (var 0)) → ⊥
  cut535  adequate = bad535  (Adequate.valid adequate Two boolean env2)
  bad536 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b1 b0) b1)) b0 → ⊥
  bad536  p = false≢true (sym (cong lower p))
  cut536 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 2) (var 1)) (var 2))) , (var 1)) → ⊥
  cut536  adequate = bad536  (Adequate.valid adequate Two boolean env2)
  bad537 : PathP (λ _ → Two) (bop (bop b0 b1) (bop (bop b1 b1) b1)) b1 → ⊥
  bad537  p = false≢true (cong lower p)
  cut537 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 2) (var 1)) (var 2))) , (var 2)) → ⊥
  cut537  adequate = bad537  (Adequate.valid adequate Two boolean env5)
  bad538 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b0 b0) b0)) b1 → ⊥
  bad538  p = false≢true (cong lower p)
  cut538 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 2) (var 1)) (var 2))) , (var 3)) → ⊥
  cut538  adequate = bad538  (Adequate.valid adequate Two boolean env4)
  bad539 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b0 b0) b1)) b0 → ⊥
  bad539  p = false≢true (sym (cong lower p))
  cut539 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 2) (var 1)) (var 3))) , (var 0)) → ⊥
  cut539  adequate = bad539  (Adequate.valid adequate Two boolean env4)
  bad540 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b0 b0) b1)) b0 → ⊥
  bad540  p = false≢true (sym (cong lower p))
  cut540 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 2) (var 1)) (var 3))) , (var 1)) → ⊥
  cut540  adequate = bad540  (Adequate.valid adequate Two boolean env4)
  bad541 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b0 b0) b1)) b0 → ⊥
  bad541  p = false≢true (sym (cong lower p))
  cut541 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 2) (var 1)) (var 3))) , (var 2)) → ⊥
  cut541  adequate = bad541  (Adequate.valid adequate Two boolean env4)
  bad542 : PathP (λ _ → Two) (bop (bop b0 b1) (bop (bop b1 b1) b1)) b1 → ⊥
  bad542  p = false≢true (cong lower p)
  cut542 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 2) (var 1)) (var 3))) , (var 3)) → ⊥
  cut542  adequate = bad542  (Adequate.valid adequate Two boolean env7)
  bad543 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b0 b0) b0)) b1 → ⊥
  bad543  p = false≢true (cong lower p)
  cut543 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 2) (var 1)) (var 3))) , (var 4)) → ⊥
  cut543  adequate = bad543  (Adequate.valid adequate Two boolean env8)
  bad544 : PathP (λ _ → Two) (bop (bop b1 b0) (bop (bop b1 b1) b1)) b1 → ⊥
  bad544  p = false≢true (cong lower p)
  cut544 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 2) (var 2)) (var 0))) , (var 0)) → ⊥
  cut544  adequate = bad544  (Adequate.valid adequate Two boolean env9)
  bad545 : PathP (λ _ → Two) (bop (bop b0 b1) (bop (bop b0 b0) b0)) b1 → ⊥
  bad545  p = false≢true (cong lower p)
  cut545 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 2) (var 2)) (var 0))) , (var 1)) → ⊥
  cut545  adequate = bad545  (Adequate.valid adequate Two boolean env6)
  bad546 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b1 b1) b0)) b1 → ⊥
  bad546  p = false≢true (cong lower p)
  cut546 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 2) (var 2)) (var 0))) , (var 2)) → ⊥
  cut546  adequate = bad546  (Adequate.valid adequate Two boolean env2)
  bad547 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b0 b0) b0)) b1 → ⊥
  bad547  p = false≢true (cong lower p)
  cut547 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 2) (var 2)) (var 0))) , (var 3)) → ⊥
  cut547  adequate = bad547  (Adequate.valid adequate Two boolean env4)
  bad548 : PathP (λ _ → Two) (bop (bop b0 b1) (bop (bop b0 b0) b1)) b0 → ⊥
  bad548  p = false≢true (sym (cong lower p))
  cut548 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 2) (var 2)) (var 1))) , (var 0)) → ⊥
  cut548  adequate = bad548  (Adequate.valid adequate Two boolean env6)
  bad549 : PathP (λ _ → Two) (bop (bop b0 b1) (bop (bop b1 b1) b1)) b1 → ⊥
  bad549  p = false≢true (cong lower p)
  cut549 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 2) (var 2)) (var 1))) , (var 1)) → ⊥
  cut549  adequate = bad549  (Adequate.valid adequate Two boolean env5)
  bad550 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b1 b1) b0)) b1 → ⊥
  bad550  p = false≢true (cong lower p)
  cut550 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 2) (var 2)) (var 1))) , (var 2)) → ⊥
  cut550  adequate = bad550  (Adequate.valid adequate Two boolean env2)
  bad551 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b0 b0) b0)) b1 → ⊥
  bad551  p = false≢true (cong lower p)
  cut551 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 2) (var 2)) (var 1))) , (var 3)) → ⊥
  cut551  adequate = bad551  (Adequate.valid adequate Two boolean env4)
  bad552 : PathP (λ _ → Two) (bop (bop b1 b0) (bop (bop b0 b0) b0)) b1 → ⊥
  bad552  p = false≢true (cong lower p)
  cut552 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 2) (var 2)) (var 2))) , (var 0)) → ⊥
  cut552  adequate = bad552  (Adequate.valid adequate Two boolean env3)
  bad553 : PathP (λ _ → Two) (bop (bop b0 b1) (bop (bop b0 b0) b0)) b1 → ⊥
  bad553  p = false≢true (cong lower p)
  cut553 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 2) (var 2)) (var 2))) , (var 1)) → ⊥
  cut553  adequate = bad553  (Adequate.valid adequate Two boolean env6)
  bad554 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b1 b1) b1)) b1 → ⊥
  bad554  p = false≢true (cong lower p)
  cut554 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 2) (var 2)) (var 2))) , (var 2)) → ⊥
  cut554  adequate = bad554  (Adequate.valid adequate Two boolean env2)
  bad555 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b0 b0) b0)) b1 → ⊥
  bad555  p = false≢true (cong lower p)
  cut555 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 2) (var 2)) (var 2))) , (var 3)) → ⊥
  cut555  adequate = bad555  (Adequate.valid adequate Two boolean env4)
  bad556 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b0 b0) b1)) b0 → ⊥
  bad556  p = false≢true (sym (cong lower p))
  cut556 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 2) (var 2)) (var 3))) , (var 0)) → ⊥
  cut556  adequate = bad556  (Adequate.valid adequate Two boolean env4)
  bad557 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b0 b0) b1)) b0 → ⊥
  bad557  p = false≢true (sym (cong lower p))
  cut557 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 2) (var 2)) (var 3))) , (var 1)) → ⊥
  cut557  adequate = bad557  (Adequate.valid adequate Two boolean env4)
  bad558 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b0 b0) b1)) b0 → ⊥
  bad558  p = false≢true (sym (cong lower p))
  cut558 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 2) (var 2)) (var 3))) , (var 2)) → ⊥
  cut558  adequate = bad558  (Adequate.valid adequate Two boolean env4)
  env12 : ℕ → Two
  env12 zero = b0
  env12 (suc zero) = b0
  env12 (suc (suc zero)) = b1
  env12 (suc (suc (suc zero))) = b1
  env12 (suc (suc (suc (suc rest)))) = b0
  bad559 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b1 b1) b1)) b1 → ⊥
  bad559  p = false≢true (cong lower p)
  cut559 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 2) (var 2)) (var 3))) , (var 3)) → ⊥
  cut559  adequate = bad559  (Adequate.valid adequate Two boolean env12)
  bad560 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b0 b0) b0)) b1 → ⊥
  bad560  p = false≢true (cong lower p)
  cut560 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 2) (var 2)) (var 3))) , (var 4)) → ⊥
  cut560  adequate = bad560  (Adequate.valid adequate Two boolean env8)
  bad561 : PathP (λ _ → Two) (bop (bop b1 b0) (bop (bop b1 b1) b1)) b1 → ⊥
  bad561  p = false≢true (cong lower p)
  cut561 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 2) (var 3)) (var 0))) , (var 0)) → ⊥
  cut561  adequate = bad561  (Adequate.valid adequate Two boolean env11)
  env13 : ℕ → Two
  env13 zero = b0
  env13 (suc zero) = b1
  env13 (suc (suc zero)) = b0
  env13 (suc (suc (suc zero))) = b0
  env13 (suc (suc (suc (suc rest)))) = b0
  bad562 : PathP (λ _ → Two) (bop (bop b0 b1) (bop (bop b0 b0) b0)) b1 → ⊥
  bad562  p = false≢true (cong lower p)
  cut562 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 2) (var 3)) (var 0))) , (var 1)) → ⊥
  cut562  adequate = bad562  (Adequate.valid adequate Two boolean env13)
  env14 : ℕ → Two
  env14 zero = b0
  env14 (suc zero) = b0
  env14 (suc (suc zero)) = b1
  env14 (suc (suc (suc zero))) = b0
  env14 (suc (suc (suc (suc rest)))) = b0
  bad563 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b1 b0) b0)) b1 → ⊥
  bad563  p = false≢true (cong lower p)
  cut563 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 2) (var 3)) (var 0))) , (var 2)) → ⊥
  cut563  adequate = bad563  (Adequate.valid adequate Two boolean env14)
  bad564 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b0 b1) b0)) b1 → ⊥
  bad564  p = false≢true (cong lower p)
  cut564 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 2) (var 3)) (var 0))) , (var 3)) → ⊥
  cut564  adequate = bad564  (Adequate.valid adequate Two boolean env4)
  bad565 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b0 b0) b0)) b1 → ⊥
  bad565  p = false≢true (cong lower p)
  cut565 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 2) (var 3)) (var 0))) , (var 4)) → ⊥
  cut565  adequate = bad565  (Adequate.valid adequate Two boolean env8)
  bad566 : PathP (λ _ → Two) (bop (bop b0 b1) (bop (bop b0 b0) b1)) b0 → ⊥
  bad566  p = false≢true (sym (cong lower p))
  cut566 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 2) (var 3)) (var 1))) , (var 0)) → ⊥
  cut566  adequate = bad566  (Adequate.valid adequate Two boolean env13)
  bad567 : PathP (λ _ → Two) (bop (bop b0 b1) (bop (bop b1 b1) b1)) b1 → ⊥
  bad567  p = false≢true (cong lower p)
  cut567 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 2) (var 3)) (var 1))) , (var 1)) → ⊥
  cut567  adequate = bad567  (Adequate.valid adequate Two boolean env7)
  bad568 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b1 b0) b0)) b1 → ⊥
  bad568  p = false≢true (cong lower p)
  cut568 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 2) (var 3)) (var 1))) , (var 2)) → ⊥
  cut568  adequate = bad568  (Adequate.valid adequate Two boolean env14)
  bad569 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b0 b1) b0)) b1 → ⊥
  bad569  p = false≢true (cong lower p)
  cut569 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 2) (var 3)) (var 1))) , (var 3)) → ⊥
  cut569  adequate = bad569  (Adequate.valid adequate Two boolean env4)
  bad570 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b0 b0) b0)) b1 → ⊥
  bad570  p = false≢true (cong lower p)
  cut570 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 2) (var 3)) (var 1))) , (var 4)) → ⊥
  cut570  adequate = bad570  (Adequate.valid adequate Two boolean env8)
  bad571 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b1 b0) b1)) b0 → ⊥
  bad571  p = false≢true (sym (cong lower p))
  cut571 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 2) (var 3)) (var 2))) , (var 0)) → ⊥
  cut571  adequate = bad571  (Adequate.valid adequate Two boolean env14)
  bad572 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b1 b0) b1)) b0 → ⊥
  bad572  p = false≢true (sym (cong lower p))
  cut572 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 2) (var 3)) (var 2))) , (var 1)) → ⊥
  cut572  adequate = bad572  (Adequate.valid adequate Two boolean env14)
  bad573 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b1 b1) b1)) b1 → ⊥
  bad573  p = false≢true (cong lower p)
  cut573 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 2) (var 3)) (var 2))) , (var 2)) → ⊥
  cut573  adequate = bad573  (Adequate.valid adequate Two boolean env12)
  bad574 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b0 b1) b0)) b1 → ⊥
  bad574  p = false≢true (cong lower p)
  cut574 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 2) (var 3)) (var 2))) , (var 3)) → ⊥
  cut574  adequate = bad574  (Adequate.valid adequate Two boolean env4)
  bad575 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b0 b0) b0)) b1 → ⊥
  bad575  p = false≢true (cong lower p)
  cut575 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 2) (var 3)) (var 2))) , (var 4)) → ⊥
  cut575  adequate = bad575  (Adequate.valid adequate Two boolean env8)
  bad576 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b0 b1) b1)) b0 → ⊥
  bad576  p = false≢true (sym (cong lower p))
  cut576 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 2) (var 3)) (var 3))) , (var 0)) → ⊥
  cut576  adequate = bad576  (Adequate.valid adequate Two boolean env4)
  bad577 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b0 b1) b1)) b0 → ⊥
  bad577  p = false≢true (sym (cong lower p))
  cut577 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 2) (var 3)) (var 3))) , (var 1)) → ⊥
  cut577  adequate = bad577  (Adequate.valid adequate Two boolean env4)
  bad578 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b0 b1) b1)) b0 → ⊥
  bad578  p = false≢true (sym (cong lower p))
  cut578 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 2) (var 3)) (var 3))) , (var 2)) → ⊥
  cut578  adequate = bad578  (Adequate.valid adequate Two boolean env4)
  bad579 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b1 b1) b1)) b1 → ⊥
  bad579  p = false≢true (cong lower p)
  cut579 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 2) (var 3)) (var 3))) , (var 3)) → ⊥
  cut579  adequate = bad579  (Adequate.valid adequate Two boolean env12)
  bad580 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b0 b0) b0)) b1 → ⊥
  bad580  p = false≢true (cong lower p)
  cut580 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 2) (var 3)) (var 3))) , (var 4)) → ⊥
  cut580  adequate = bad580  (Adequate.valid adequate Two boolean env8)
  bad581 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b0 b0) b1)) b0 → ⊥
  bad581  p = false≢true (sym (cong lower p))
  cut581 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 2) (var 3)) (var 4))) , (var 0)) → ⊥
  cut581  adequate = bad581  (Adequate.valid adequate Two boolean env8)
  bad582 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b0 b0) b1)) b0 → ⊥
  bad582  p = false≢true (sym (cong lower p))
  cut582 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 2) (var 3)) (var 4))) , (var 1)) → ⊥
  cut582  adequate = bad582  (Adequate.valid adequate Two boolean env8)
  bad583 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b0 b0) b1)) b0 → ⊥
  bad583  p = false≢true (sym (cong lower p))
  cut583 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 2) (var 3)) (var 4))) , (var 2)) → ⊥
  cut583  adequate = bad583  (Adequate.valid adequate Two boolean env8)
  bad584 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b0 b0) b1)) b0 → ⊥
  bad584  p = false≢true (sym (cong lower p))
  cut584 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 2) (var 3)) (var 4))) , (var 3)) → ⊥
  cut584  adequate = bad584  (Adequate.valid adequate Two boolean env8)
  env15 : ℕ → Two
  env15 zero = b0
  env15 (suc zero) = b0
  env15 (suc (suc zero)) = b1
  env15 (suc (suc (suc zero))) = b1
  env15 (suc (suc (suc (suc zero)))) = b1
  env15 (suc (suc (suc (suc (suc rest))))) = b0
  bad585 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b1 b1) b1)) b1 → ⊥
  bad585  p = false≢true (cong lower p)
  cut585 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 2) (var 3)) (var 4))) , (var 4)) → ⊥
  cut585  adequate = bad585  (Adequate.valid adequate Two boolean env15)
  env16 : ℕ → Two
  env16 zero = b0
  env16 (suc zero) = b0
  env16 (suc (suc zero)) = b0
  env16 (suc (suc (suc zero))) = b0
  env16 (suc (suc (suc (suc zero)))) = b0
  env16 (suc (suc (suc (suc (suc zero))))) = b1
  env16 (suc (suc (suc (suc (suc (suc rest)))))) = b0
  bad586 : PathP (λ _ → Two) (bop (bop b0 b0) (bop (bop b0 b0) b0)) b1 → ⊥
  bad586  p = false≢true (cong lower p)
  cut586 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (op (var 2) (var 3)) (var 4))) , (var 5)) → ⊥
  cut586  adequate = bad586  (Adequate.valid adequate Two boolean env16)
