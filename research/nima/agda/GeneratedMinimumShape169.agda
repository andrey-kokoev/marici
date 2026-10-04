{-# OPTIONS --safe --cubical --guardedness #-}
module GeneratedMinimumShape169 where
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
  holds2417 : (z0 : A1) → (mul1 (mul1 z0 z0) (mul1 z0 (mul1 (mul1 z0 z0) z0))) ≡ z0
  holds2417 m1c0 = refl
  holds2417 m1c1 = refl
  cut2417 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (var 0) (op (op (var 0) (var 0)) (var 0)))) , (var 0)) → ⊥
  cut2417  = reject1 ((op (op (var 0) (var 0)) (op (var 0) (op (op (var 0) (var 0)) (var 0)))) , (var 0)) (λ env → holds2417 (env 0))
  env0 : ℕ → Two
  env0 zero = b0
  env0 (suc zero) = b1
  env0 (suc (suc rest)) = b0
  bad2418 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop (bop b0 b0) b0))) b1 → ⊥
  bad2418  p = false≢true (cong lower p)
  cut2418 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (var 0) (op (op (var 0) (var 0)) (var 0)))) , (var 1)) → ⊥
  cut2418  adequate = bad2418  (Adequate.valid adequate Two boolean env0)
  holds2419 : (z0 z1 : A2) → (mul2 (mul2 z0 z0) (mul2 z0 (mul2 (mul2 z0 z0) z1))) ≡ z0
  holds2419 z0 z1 = refl
  cut2419 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (var 0) (op (op (var 0) (var 0)) (var 1)))) , (var 0)) → ⊥
  cut2419  = reject2 ((op (op (var 0) (var 0)) (op (var 0) (op (op (var 0) (var 0)) (var 1)))) , (var 0)) (λ env → holds2419 (env 0) (env 1))
  bad2420 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop (bop b0 b0) b1))) b1 → ⊥
  bad2420  p = false≢true (cong lower p)
  cut2420 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (var 0) (op (op (var 0) (var 0)) (var 1)))) , (var 1)) → ⊥
  cut2420  adequate = bad2420  (Adequate.valid adequate Two boolean env0)
  env1 : ℕ → Two
  env1 zero = b0
  env1 (suc zero) = b0
  env1 (suc (suc zero)) = b1
  env1 (suc (suc (suc rest))) = b0
  bad2421 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop (bop b0 b0) b0))) b1 → ⊥
  bad2421  p = false≢true (cong lower p)
  cut2421 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (var 0) (op (op (var 0) (var 0)) (var 1)))) , (var 2)) → ⊥
  cut2421  adequate = bad2421  (Adequate.valid adequate Two boolean env1)
  holds2422 : (z0 z1 : A2) → (mul2 (mul2 z0 z0) (mul2 z0 (mul2 (mul2 z0 z1) z0))) ≡ z0
  holds2422 z0 z1 = refl
  cut2422 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (var 0) (op (op (var 0) (var 1)) (var 0)))) , (var 0)) → ⊥
  cut2422  = reject2 ((op (op (var 0) (var 0)) (op (var 0) (op (op (var 0) (var 1)) (var 0)))) , (var 0)) (λ env → holds2422 (env 0) (env 1))
  bad2423 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop (bop b0 b1) b0))) b1 → ⊥
  bad2423  p = false≢true (cong lower p)
  cut2423 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (var 0) (op (op (var 0) (var 1)) (var 0)))) , (var 1)) → ⊥
  cut2423  adequate = bad2423  (Adequate.valid adequate Two boolean env0)
  bad2424 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop (bop b0 b0) b0))) b1 → ⊥
  bad2424  p = false≢true (cong lower p)
  cut2424 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (var 0) (op (op (var 0) (var 1)) (var 0)))) , (var 2)) → ⊥
  cut2424  adequate = bad2424  (Adequate.valid adequate Two boolean env1)
  holds2425 : (z0 z1 : A2) → (mul2 (mul2 z0 z0) (mul2 z0 (mul2 (mul2 z0 z1) z1))) ≡ z0
  holds2425 z0 z1 = refl
  cut2425 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (var 0) (op (op (var 0) (var 1)) (var 1)))) , (var 0)) → ⊥
  cut2425  = reject2 ((op (op (var 0) (var 0)) (op (var 0) (op (op (var 0) (var 1)) (var 1)))) , (var 0)) (λ env → holds2425 (env 0) (env 1))
  bad2426 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop (bop b0 b1) b1))) b1 → ⊥
  bad2426  p = false≢true (cong lower p)
  cut2426 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (var 0) (op (op (var 0) (var 1)) (var 1)))) , (var 1)) → ⊥
  cut2426  adequate = bad2426  (Adequate.valid adequate Two boolean env0)
  bad2427 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop (bop b0 b0) b0))) b1 → ⊥
  bad2427  p = false≢true (cong lower p)
  cut2427 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (var 0) (op (op (var 0) (var 1)) (var 1)))) , (var 2)) → ⊥
  cut2427  adequate = bad2427  (Adequate.valid adequate Two boolean env1)
  holds2428 : (z0 z1 z2 : A2) → (mul2 (mul2 z0 z0) (mul2 z0 (mul2 (mul2 z0 z1) z2))) ≡ z0
  holds2428 z0 z1 z2 = refl
  cut2428 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (var 0) (op (op (var 0) (var 1)) (var 2)))) , (var 0)) → ⊥
  cut2428  = reject2 ((op (op (var 0) (var 0)) (op (var 0) (op (op (var 0) (var 1)) (var 2)))) , (var 0)) (λ env → holds2428 (env 0) (env 1) (env 2))
  env2 : ℕ → Two
  env2 zero = b0
  env2 (suc zero) = b1
  env2 (suc (suc zero)) = b0
  env2 (suc (suc (suc rest))) = b0
  bad2429 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop (bop b0 b1) b0))) b1 → ⊥
  bad2429  p = false≢true (cong lower p)
  cut2429 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (var 0) (op (op (var 0) (var 1)) (var 2)))) , (var 1)) → ⊥
  cut2429  adequate = bad2429  (Adequate.valid adequate Two boolean env2)
  bad2430 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop (bop b0 b0) b1))) b1 → ⊥
  bad2430  p = false≢true (cong lower p)
  cut2430 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (var 0) (op (op (var 0) (var 1)) (var 2)))) , (var 2)) → ⊥
  cut2430  adequate = bad2430  (Adequate.valid adequate Two boolean env1)
  env3 : ℕ → Two
  env3 zero = b0
  env3 (suc zero) = b0
  env3 (suc (suc zero)) = b0
  env3 (suc (suc (suc zero))) = b1
  env3 (suc (suc (suc (suc rest)))) = b0
  bad2431 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop (bop b0 b0) b0))) b1 → ⊥
  bad2431  p = false≢true (cong lower p)
  cut2431 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (var 0) (op (op (var 0) (var 1)) (var 2)))) , (var 3)) → ⊥
  cut2431  adequate = bad2431  (Adequate.valid adequate Two boolean env3)
  holds2432 : (z0 z1 : A2) → (mul2 (mul2 z0 z0) (mul2 z0 (mul2 (mul2 z1 z0) z0))) ≡ z0
  holds2432 z0 z1 = refl
  cut2432 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (var 0) (op (op (var 1) (var 0)) (var 0)))) , (var 0)) → ⊥
  cut2432  = reject2 ((op (op (var 0) (var 0)) (op (var 0) (op (op (var 1) (var 0)) (var 0)))) , (var 0)) (λ env → holds2432 (env 0) (env 1))
  bad2433 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop (bop b1 b0) b0))) b1 → ⊥
  bad2433  p = false≢true (cong lower p)
  cut2433 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (var 0) (op (op (var 1) (var 0)) (var 0)))) , (var 1)) → ⊥
  cut2433  adequate = bad2433  (Adequate.valid adequate Two boolean env0)
  bad2434 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop (bop b0 b0) b0))) b1 → ⊥
  bad2434  p = false≢true (cong lower p)
  cut2434 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (var 0) (op (op (var 1) (var 0)) (var 0)))) , (var 2)) → ⊥
  cut2434  adequate = bad2434  (Adequate.valid adequate Two boolean env1)
  holds2435 : (z0 z1 : A2) → (mul2 (mul2 z0 z0) (mul2 z0 (mul2 (mul2 z1 z0) z1))) ≡ z0
  holds2435 z0 z1 = refl
  cut2435 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (var 0) (op (op (var 1) (var 0)) (var 1)))) , (var 0)) → ⊥
  cut2435  = reject2 ((op (op (var 0) (var 0)) (op (var 0) (op (op (var 1) (var 0)) (var 1)))) , (var 0)) (λ env → holds2435 (env 0) (env 1))
  bad2436 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop (bop b1 b0) b1))) b1 → ⊥
  bad2436  p = false≢true (cong lower p)
  cut2436 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (var 0) (op (op (var 1) (var 0)) (var 1)))) , (var 1)) → ⊥
  cut2436  adequate = bad2436  (Adequate.valid adequate Two boolean env0)
  bad2437 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop (bop b0 b0) b0))) b1 → ⊥
  bad2437  p = false≢true (cong lower p)
  cut2437 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (var 0) (op (op (var 1) (var 0)) (var 1)))) , (var 2)) → ⊥
  cut2437  adequate = bad2437  (Adequate.valid adequate Two boolean env1)
  holds2438 : (z0 z1 z2 : A2) → (mul2 (mul2 z0 z0) (mul2 z0 (mul2 (mul2 z1 z0) z2))) ≡ z0
  holds2438 z0 z1 z2 = refl
  cut2438 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (var 0) (op (op (var 1) (var 0)) (var 2)))) , (var 0)) → ⊥
  cut2438  = reject2 ((op (op (var 0) (var 0)) (op (var 0) (op (op (var 1) (var 0)) (var 2)))) , (var 0)) (λ env → holds2438 (env 0) (env 1) (env 2))
  bad2439 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop (bop b1 b0) b0))) b1 → ⊥
  bad2439  p = false≢true (cong lower p)
  cut2439 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (var 0) (op (op (var 1) (var 0)) (var 2)))) , (var 1)) → ⊥
  cut2439  adequate = bad2439  (Adequate.valid adequate Two boolean env2)
  bad2440 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop (bop b0 b0) b1))) b1 → ⊥
  bad2440  p = false≢true (cong lower p)
  cut2440 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (var 0) (op (op (var 1) (var 0)) (var 2)))) , (var 2)) → ⊥
  cut2440  adequate = bad2440  (Adequate.valid adequate Two boolean env1)
  bad2441 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop (bop b0 b0) b0))) b1 → ⊥
  bad2441  p = false≢true (cong lower p)
  cut2441 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (var 0) (op (op (var 1) (var 0)) (var 2)))) , (var 3)) → ⊥
  cut2441  adequate = bad2441  (Adequate.valid adequate Two boolean env3)
  holds2442 : (z0 z1 : A2) → (mul2 (mul2 z0 z0) (mul2 z0 (mul2 (mul2 z1 z1) z0))) ≡ z0
  holds2442 z0 z1 = refl
  cut2442 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (var 0) (op (op (var 1) (var 1)) (var 0)))) , (var 0)) → ⊥
  cut2442  = reject2 ((op (op (var 0) (var 0)) (op (var 0) (op (op (var 1) (var 1)) (var 0)))) , (var 0)) (λ env → holds2442 (env 0) (env 1))
  bad2443 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop (bop b1 b1) b0))) b1 → ⊥
  bad2443  p = false≢true (cong lower p)
  cut2443 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (var 0) (op (op (var 1) (var 1)) (var 0)))) , (var 1)) → ⊥
  cut2443  adequate = bad2443  (Adequate.valid adequate Two boolean env0)
  bad2444 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop (bop b0 b0) b0))) b1 → ⊥
  bad2444  p = false≢true (cong lower p)
  cut2444 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (var 0) (op (op (var 1) (var 1)) (var 0)))) , (var 2)) → ⊥
  cut2444  adequate = bad2444  (Adequate.valid adequate Two boolean env1)
  holds2445 : (z0 z1 : A2) → (mul2 (mul2 z0 z0) (mul2 z0 (mul2 (mul2 z1 z1) z1))) ≡ z0
  holds2445 z0 z1 = refl
  cut2445 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (var 0) (op (op (var 1) (var 1)) (var 1)))) , (var 0)) → ⊥
  cut2445  = reject2 ((op (op (var 0) (var 0)) (op (var 0) (op (op (var 1) (var 1)) (var 1)))) , (var 0)) (λ env → holds2445 (env 0) (env 1))
  bad2446 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop (bop b1 b1) b1))) b1 → ⊥
  bad2446  p = false≢true (cong lower p)
  cut2446 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (var 0) (op (op (var 1) (var 1)) (var 1)))) , (var 1)) → ⊥
  cut2446  adequate = bad2446  (Adequate.valid adequate Two boolean env0)
  bad2447 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop (bop b0 b0) b0))) b1 → ⊥
  bad2447  p = false≢true (cong lower p)
  cut2447 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (var 0) (op (op (var 1) (var 1)) (var 1)))) , (var 2)) → ⊥
  cut2447  adequate = bad2447  (Adequate.valid adequate Two boolean env1)
  holds2448 : (z0 z1 z2 : A2) → (mul2 (mul2 z0 z0) (mul2 z0 (mul2 (mul2 z1 z1) z2))) ≡ z0
  holds2448 z0 z1 z2 = refl
  cut2448 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (var 0) (op (op (var 1) (var 1)) (var 2)))) , (var 0)) → ⊥
  cut2448  = reject2 ((op (op (var 0) (var 0)) (op (var 0) (op (op (var 1) (var 1)) (var 2)))) , (var 0)) (λ env → holds2448 (env 0) (env 1) (env 2))
  bad2449 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop (bop b1 b1) b0))) b1 → ⊥
  bad2449  p = false≢true (cong lower p)
  cut2449 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (var 0) (op (op (var 1) (var 1)) (var 2)))) , (var 1)) → ⊥
  cut2449  adequate = bad2449  (Adequate.valid adequate Two boolean env2)
  bad2450 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop (bop b0 b0) b1))) b1 → ⊥
  bad2450  p = false≢true (cong lower p)
  cut2450 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (var 0) (op (op (var 1) (var 1)) (var 2)))) , (var 2)) → ⊥
  cut2450  adequate = bad2450  (Adequate.valid adequate Two boolean env1)
  bad2451 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop (bop b0 b0) b0))) b1 → ⊥
  bad2451  p = false≢true (cong lower p)
  cut2451 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (var 0) (op (op (var 1) (var 1)) (var 2)))) , (var 3)) → ⊥
  cut2451  adequate = bad2451  (Adequate.valid adequate Two boolean env3)
  holds2452 : (z0 z1 z2 : A2) → (mul2 (mul2 z0 z0) (mul2 z0 (mul2 (mul2 z1 z2) z0))) ≡ z0
  holds2452 z0 z1 z2 = refl
  cut2452 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (var 0) (op (op (var 1) (var 2)) (var 0)))) , (var 0)) → ⊥
  cut2452  = reject2 ((op (op (var 0) (var 0)) (op (var 0) (op (op (var 1) (var 2)) (var 0)))) , (var 0)) (λ env → holds2452 (env 0) (env 1) (env 2))
  bad2453 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop (bop b1 b0) b0))) b1 → ⊥
  bad2453  p = false≢true (cong lower p)
  cut2453 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (var 0) (op (op (var 1) (var 2)) (var 0)))) , (var 1)) → ⊥
  cut2453  adequate = bad2453  (Adequate.valid adequate Two boolean env2)
  bad2454 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop (bop b0 b1) b0))) b1 → ⊥
  bad2454  p = false≢true (cong lower p)
  cut2454 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (var 0) (op (op (var 1) (var 2)) (var 0)))) , (var 2)) → ⊥
  cut2454  adequate = bad2454  (Adequate.valid adequate Two boolean env1)
  bad2455 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop (bop b0 b0) b0))) b1 → ⊥
  bad2455  p = false≢true (cong lower p)
  cut2455 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (var 0) (op (op (var 1) (var 2)) (var 0)))) , (var 3)) → ⊥
  cut2455  adequate = bad2455  (Adequate.valid adequate Two boolean env3)
  holds2456 : (z0 z1 z2 : A2) → (mul2 (mul2 z0 z0) (mul2 z0 (mul2 (mul2 z1 z2) z1))) ≡ z0
  holds2456 z0 z1 z2 = refl
  cut2456 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (var 0) (op (op (var 1) (var 2)) (var 1)))) , (var 0)) → ⊥
  cut2456  = reject2 ((op (op (var 0) (var 0)) (op (var 0) (op (op (var 1) (var 2)) (var 1)))) , (var 0)) (λ env → holds2456 (env 0) (env 1) (env 2))
  bad2457 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop (bop b1 b0) b1))) b1 → ⊥
  bad2457  p = false≢true (cong lower p)
  cut2457 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (var 0) (op (op (var 1) (var 2)) (var 1)))) , (var 1)) → ⊥
  cut2457  adequate = bad2457  (Adequate.valid adequate Two boolean env2)
  bad2458 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop (bop b0 b1) b0))) b1 → ⊥
  bad2458  p = false≢true (cong lower p)
  cut2458 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (var 0) (op (op (var 1) (var 2)) (var 1)))) , (var 2)) → ⊥
  cut2458  adequate = bad2458  (Adequate.valid adequate Two boolean env1)
  bad2459 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop (bop b0 b0) b0))) b1 → ⊥
  bad2459  p = false≢true (cong lower p)
  cut2459 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (var 0) (op (op (var 1) (var 2)) (var 1)))) , (var 3)) → ⊥
  cut2459  adequate = bad2459  (Adequate.valid adequate Two boolean env3)
  holds2460 : (z0 z1 z2 : A2) → (mul2 (mul2 z0 z0) (mul2 z0 (mul2 (mul2 z1 z2) z2))) ≡ z0
  holds2460 z0 z1 z2 = refl
  cut2460 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (var 0) (op (op (var 1) (var 2)) (var 2)))) , (var 0)) → ⊥
  cut2460  = reject2 ((op (op (var 0) (var 0)) (op (var 0) (op (op (var 1) (var 2)) (var 2)))) , (var 0)) (λ env → holds2460 (env 0) (env 1) (env 2))
  bad2461 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop (bop b1 b0) b0))) b1 → ⊥
  bad2461  p = false≢true (cong lower p)
  cut2461 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (var 0) (op (op (var 1) (var 2)) (var 2)))) , (var 1)) → ⊥
  cut2461  adequate = bad2461  (Adequate.valid adequate Two boolean env2)
  bad2462 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop (bop b0 b1) b1))) b1 → ⊥
  bad2462  p = false≢true (cong lower p)
  cut2462 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (var 0) (op (op (var 1) (var 2)) (var 2)))) , (var 2)) → ⊥
  cut2462  adequate = bad2462  (Adequate.valid adequate Two boolean env1)
  bad2463 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop (bop b0 b0) b0))) b1 → ⊥
  bad2463  p = false≢true (cong lower p)
  cut2463 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (var 0) (op (op (var 1) (var 2)) (var 2)))) , (var 3)) → ⊥
  cut2463  adequate = bad2463  (Adequate.valid adequate Two boolean env3)
  holds2464 : (z0 z1 z2 z3 : A2) → (mul2 (mul2 z0 z0) (mul2 z0 (mul2 (mul2 z1 z2) z3))) ≡ z0
  holds2464 z0 z1 z2 z3 = refl
  cut2464 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (var 0) (op (op (var 1) (var 2)) (var 3)))) , (var 0)) → ⊥
  cut2464  = reject2 ((op (op (var 0) (var 0)) (op (var 0) (op (op (var 1) (var 2)) (var 3)))) , (var 0)) (λ env → holds2464 (env 0) (env 1) (env 2) (env 3))
  env4 : ℕ → Two
  env4 zero = b0
  env4 (suc zero) = b1
  env4 (suc (suc zero)) = b0
  env4 (suc (suc (suc zero))) = b0
  env4 (suc (suc (suc (suc rest)))) = b0
  bad2465 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop (bop b1 b0) b0))) b1 → ⊥
  bad2465  p = false≢true (cong lower p)
  cut2465 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (var 0) (op (op (var 1) (var 2)) (var 3)))) , (var 1)) → ⊥
  cut2465  adequate = bad2465  (Adequate.valid adequate Two boolean env4)
  env5 : ℕ → Two
  env5 zero = b0
  env5 (suc zero) = b0
  env5 (suc (suc zero)) = b1
  env5 (suc (suc (suc zero))) = b0
  env5 (suc (suc (suc (suc rest)))) = b0
  bad2466 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop (bop b0 b1) b0))) b1 → ⊥
  bad2466  p = false≢true (cong lower p)
  cut2466 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (var 0) (op (op (var 1) (var 2)) (var 3)))) , (var 2)) → ⊥
  cut2466  adequate = bad2466  (Adequate.valid adequate Two boolean env5)
  bad2467 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop (bop b0 b0) b1))) b1 → ⊥
  bad2467  p = false≢true (cong lower p)
  cut2467 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (var 0) (op (op (var 1) (var 2)) (var 3)))) , (var 3)) → ⊥
  cut2467  adequate = bad2467  (Adequate.valid adequate Two boolean env3)
  env6 : ℕ → Two
  env6 zero = b0
  env6 (suc zero) = b0
  env6 (suc (suc zero)) = b0
  env6 (suc (suc (suc zero))) = b0
  env6 (suc (suc (suc (suc zero)))) = b1
  env6 (suc (suc (suc (suc (suc rest))))) = b0
  bad2468 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop (bop b0 b0) b0))) b1 → ⊥
  bad2468  p = false≢true (cong lower p)
  cut2468 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (var 0) (op (op (var 1) (var 2)) (var 3)))) , (var 4)) → ⊥
  cut2468  adequate = bad2468  (Adequate.valid adequate Two boolean env6)
  bad2469 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b1 (bop (bop b0 b0) b0))) b0 → ⊥
  bad2469  p = false≢true (sym (cong lower p))
  cut2469 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (var 1) (op (op (var 0) (var 0)) (var 0)))) , (var 0)) → ⊥
  cut2469  adequate = bad2469  (Adequate.valid adequate Two boolean env0)
  env7 : ℕ → Two
  env7 zero = b1
  env7 (suc zero) = b0
  env7 (suc (suc rest)) = b0
  bad2470 : PathP (λ _ → Two) (bop (bop b1 b1) (bop b0 (bop (bop b1 b1) b1))) b0 → ⊥
  bad2470  p = false≢true (sym (cong lower p))
  cut2470 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (var 1) (op (op (var 0) (var 0)) (var 0)))) , (var 1)) → ⊥
  cut2470  adequate = bad2470  (Adequate.valid adequate Two boolean env7)
  bad2471 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop (bop b0 b0) b0))) b1 → ⊥
  bad2471  p = false≢true (cong lower p)
  cut2471 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (var 1) (op (op (var 0) (var 0)) (var 0)))) , (var 2)) → ⊥
  cut2471  adequate = bad2471  (Adequate.valid adequate Two boolean env1)
  holds2472 : (z0 z1 : A2) → (mul2 (mul2 z0 z0) (mul2 z1 (mul2 (mul2 z0 z0) z1))) ≡ z0
  holds2472 z0 z1 = refl
  cut2472 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (var 1) (op (op (var 0) (var 0)) (var 1)))) , (var 0)) → ⊥
  cut2472  = reject2 ((op (op (var 0) (var 0)) (op (var 1) (op (op (var 0) (var 0)) (var 1)))) , (var 0)) (λ env → holds2472 (env 0) (env 1))
  bad2473 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b1 (bop (bop b0 b0) b1))) b1 → ⊥
  bad2473  p = false≢true (cong lower p)
  cut2473 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (var 1) (op (op (var 0) (var 0)) (var 1)))) , (var 1)) → ⊥
  cut2473  adequate = bad2473  (Adequate.valid adequate Two boolean env0)
  bad2474 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop (bop b0 b0) b0))) b1 → ⊥
  bad2474  p = false≢true (cong lower p)
  cut2474 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (var 1) (op (op (var 0) (var 0)) (var 1)))) , (var 2)) → ⊥
  cut2474  adequate = bad2474  (Adequate.valid adequate Two boolean env1)
  bad2475 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b1 (bop (bop b0 b0) b0))) b0 → ⊥
  bad2475  p = false≢true (sym (cong lower p))
  cut2475 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (var 1) (op (op (var 0) (var 0)) (var 2)))) , (var 0)) → ⊥
  cut2475  adequate = bad2475  (Adequate.valid adequate Two boolean env2)
  env8 : ℕ → Two
  env8 zero = b0
  env8 (suc zero) = b1
  env8 (suc (suc zero)) = b1
  env8 (suc (suc (suc rest))) = b0
  bad2476 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b1 (bop (bop b0 b0) b1))) b1 → ⊥
  bad2476  p = false≢true (cong lower p)
  cut2476 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (var 1) (op (op (var 0) (var 0)) (var 2)))) , (var 1)) → ⊥
  cut2476  adequate = bad2476  (Adequate.valid adequate Two boolean env8)
  bad2477 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop (bop b0 b0) b1))) b1 → ⊥
  bad2477  p = false≢true (cong lower p)
  cut2477 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (var 1) (op (op (var 0) (var 0)) (var 2)))) , (var 2)) → ⊥
  cut2477  adequate = bad2477  (Adequate.valid adequate Two boolean env1)
  bad2478 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop (bop b0 b0) b0))) b1 → ⊥
  bad2478  p = false≢true (cong lower p)
  cut2478 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (var 1) (op (op (var 0) (var 0)) (var 2)))) , (var 3)) → ⊥
  cut2478  adequate = bad2478  (Adequate.valid adequate Two boolean env3)
  bad2479 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b1 (bop (bop b0 b1) b0))) b0 → ⊥
  bad2479  p = false≢true (sym (cong lower p))
  cut2479 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (var 1) (op (op (var 0) (var 1)) (var 0)))) , (var 0)) → ⊥
  cut2479  adequate = bad2479  (Adequate.valid adequate Two boolean env0)
  bad2480 : PathP (λ _ → Two) (bop (bop b1 b1) (bop b0 (bop (bop b1 b0) b1))) b0 → ⊥
  bad2480  p = false≢true (sym (cong lower p))
  cut2480 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (var 1) (op (op (var 0) (var 1)) (var 0)))) , (var 1)) → ⊥
  cut2480  adequate = bad2480  (Adequate.valid adequate Two boolean env7)
  bad2481 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop (bop b0 b0) b0))) b1 → ⊥
  bad2481  p = false≢true (cong lower p)
  cut2481 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (var 1) (op (op (var 0) (var 1)) (var 0)))) , (var 2)) → ⊥
  cut2481  adequate = bad2481  (Adequate.valid adequate Two boolean env1)
  holds2482 : (z0 z1 : A2) → (mul2 (mul2 z0 z0) (mul2 z1 (mul2 (mul2 z0 z1) z1))) ≡ z0
  holds2482 z0 z1 = refl
  cut2482 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (var 1) (op (op (var 0) (var 1)) (var 1)))) , (var 0)) → ⊥
  cut2482  = reject2 ((op (op (var 0) (var 0)) (op (var 1) (op (op (var 0) (var 1)) (var 1)))) , (var 0)) (λ env → holds2482 (env 0) (env 1))
  bad2483 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b1 (bop (bop b0 b1) b1))) b1 → ⊥
  bad2483  p = false≢true (cong lower p)
  cut2483 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (var 1) (op (op (var 0) (var 1)) (var 1)))) , (var 1)) → ⊥
  cut2483  adequate = bad2483  (Adequate.valid adequate Two boolean env0)
  bad2484 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop (bop b0 b0) b0))) b1 → ⊥
  bad2484  p = false≢true (cong lower p)
  cut2484 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (var 1) (op (op (var 0) (var 1)) (var 1)))) , (var 2)) → ⊥
  cut2484  adequate = bad2484  (Adequate.valid adequate Two boolean env1)
  bad2485 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b1 (bop (bop b0 b1) b0))) b0 → ⊥
  bad2485  p = false≢true (sym (cong lower p))
  cut2485 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (var 1) (op (op (var 0) (var 1)) (var 2)))) , (var 0)) → ⊥
  cut2485  adequate = bad2485  (Adequate.valid adequate Two boolean env2)
  bad2486 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b1 (bop (bop b0 b1) b1))) b1 → ⊥
  bad2486  p = false≢true (cong lower p)
  cut2486 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (var 1) (op (op (var 0) (var 1)) (var 2)))) , (var 1)) → ⊥
  cut2486  adequate = bad2486  (Adequate.valid adequate Two boolean env8)
  bad2487 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop (bop b0 b0) b1))) b1 → ⊥
  bad2487  p = false≢true (cong lower p)
  cut2487 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (var 1) (op (op (var 0) (var 1)) (var 2)))) , (var 2)) → ⊥
  cut2487  adequate = bad2487  (Adequate.valid adequate Two boolean env1)
  bad2488 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop (bop b0 b0) b0))) b1 → ⊥
  bad2488  p = false≢true (cong lower p)
  cut2488 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (var 1) (op (op (var 0) (var 1)) (var 2)))) , (var 3)) → ⊥
  cut2488  adequate = bad2488  (Adequate.valid adequate Two boolean env3)
  bad2489 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b1 (bop (bop b0 b0) b0))) b0 → ⊥
  bad2489  p = false≢true (sym (cong lower p))
  cut2489 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (var 1) (op (op (var 0) (var 2)) (var 0)))) , (var 0)) → ⊥
  cut2489  adequate = bad2489  (Adequate.valid adequate Two boolean env2)
  env9 : ℕ → Two
  env9 zero = b1
  env9 (suc zero) = b0
  env9 (suc (suc zero)) = b0
  env9 (suc (suc (suc rest))) = b0
  bad2490 : PathP (λ _ → Two) (bop (bop b1 b1) (bop b0 (bop (bop b1 b0) b1))) b0 → ⊥
  bad2490  p = false≢true (sym (cong lower p))
  cut2490 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (var 1) (op (op (var 0) (var 2)) (var 0)))) , (var 1)) → ⊥
  cut2490  adequate = bad2490  (Adequate.valid adequate Two boolean env9)
  bad2491 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop (bop b0 b1) b0))) b1 → ⊥
  bad2491  p = false≢true (cong lower p)
  cut2491 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (var 1) (op (op (var 0) (var 2)) (var 0)))) , (var 2)) → ⊥
  cut2491  adequate = bad2491  (Adequate.valid adequate Two boolean env1)
  bad2492 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop (bop b0 b0) b0))) b1 → ⊥
  bad2492  p = false≢true (cong lower p)
  cut2492 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (var 1) (op (op (var 0) (var 2)) (var 0)))) , (var 3)) → ⊥
  cut2492  adequate = bad2492  (Adequate.valid adequate Two boolean env3)
  holds2493 : (z0 z1 z2 : A2) → (mul2 (mul2 z0 z0) (mul2 z1 (mul2 (mul2 z0 z2) z1))) ≡ z0
  holds2493 z0 z1 z2 = refl
  cut2493 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (var 1) (op (op (var 0) (var 2)) (var 1)))) , (var 0)) → ⊥
  cut2493  = reject2 ((op (op (var 0) (var 0)) (op (var 1) (op (op (var 0) (var 2)) (var 1)))) , (var 0)) (λ env → holds2493 (env 0) (env 1) (env 2))
  bad2494 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b1 (bop (bop b0 b0) b1))) b1 → ⊥
  bad2494  p = false≢true (cong lower p)
  cut2494 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (var 1) (op (op (var 0) (var 2)) (var 1)))) , (var 1)) → ⊥
  cut2494  adequate = bad2494  (Adequate.valid adequate Two boolean env2)
  bad2495 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop (bop b0 b1) b0))) b1 → ⊥
  bad2495  p = false≢true (cong lower p)
  cut2495 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (var 1) (op (op (var 0) (var 2)) (var 1)))) , (var 2)) → ⊥
  cut2495  adequate = bad2495  (Adequate.valid adequate Two boolean env1)
  bad2496 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop (bop b0 b0) b0))) b1 → ⊥
  bad2496  p = false≢true (cong lower p)
  cut2496 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (var 1) (op (op (var 0) (var 2)) (var 1)))) , (var 3)) → ⊥
  cut2496  adequate = bad2496  (Adequate.valid adequate Two boolean env3)
  bad2497 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b1 (bop (bop b0 b0) b0))) b0 → ⊥
  bad2497  p = false≢true (sym (cong lower p))
  cut2497 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (var 1) (op (op (var 0) (var 2)) (var 2)))) , (var 0)) → ⊥
  cut2497  adequate = bad2497  (Adequate.valid adequate Two boolean env2)
  bad2498 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b1 (bop (bop b0 b1) b1))) b1 → ⊥
  bad2498  p = false≢true (cong lower p)
  cut2498 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (var 1) (op (op (var 0) (var 2)) (var 2)))) , (var 1)) → ⊥
  cut2498  adequate = bad2498  (Adequate.valid adequate Two boolean env8)
  bad2499 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop (bop b0 b1) b1))) b1 → ⊥
  bad2499  p = false≢true (cong lower p)
  cut2499 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (var 1) (op (op (var 0) (var 2)) (var 2)))) , (var 2)) → ⊥
  cut2499  adequate = bad2499  (Adequate.valid adequate Two boolean env1)
  bad2500 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop (bop b0 b0) b0))) b1 → ⊥
  bad2500  p = false≢true (cong lower p)
  cut2500 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (var 1) (op (op (var 0) (var 2)) (var 2)))) , (var 3)) → ⊥
  cut2500  adequate = bad2500  (Adequate.valid adequate Two boolean env3)
  bad2501 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b1 (bop (bop b0 b0) b0))) b0 → ⊥
  bad2501  p = false≢true (sym (cong lower p))
  cut2501 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (var 1) (op (op (var 0) (var 2)) (var 3)))) , (var 0)) → ⊥
  cut2501  adequate = bad2501  (Adequate.valid adequate Two boolean env4)
  env10 : ℕ → Two
  env10 zero = b0
  env10 (suc zero) = b1
  env10 (suc (suc zero)) = b0
  env10 (suc (suc (suc zero))) = b1
  env10 (suc (suc (suc (suc rest)))) = b0
  bad2502 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b1 (bop (bop b0 b0) b1))) b1 → ⊥
  bad2502  p = false≢true (cong lower p)
  cut2502 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (var 1) (op (op (var 0) (var 2)) (var 3)))) , (var 1)) → ⊥
  cut2502  adequate = bad2502  (Adequate.valid adequate Two boolean env10)
  bad2503 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop (bop b0 b1) b0))) b1 → ⊥
  bad2503  p = false≢true (cong lower p)
  cut2503 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (var 1) (op (op (var 0) (var 2)) (var 3)))) , (var 2)) → ⊥
  cut2503  adequate = bad2503  (Adequate.valid adequate Two boolean env5)
  bad2504 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop (bop b0 b0) b1))) b1 → ⊥
  bad2504  p = false≢true (cong lower p)
  cut2504 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (var 1) (op (op (var 0) (var 2)) (var 3)))) , (var 3)) → ⊥
  cut2504  adequate = bad2504  (Adequate.valid adequate Two boolean env3)
  bad2505 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop (bop b0 b0) b0))) b1 → ⊥
  bad2505  p = false≢true (cong lower p)
  cut2505 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (var 1) (op (op (var 0) (var 2)) (var 3)))) , (var 4)) → ⊥
  cut2505  adequate = bad2505  (Adequate.valid adequate Two boolean env6)
  bad2506 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b1 (bop (bop b1 b0) b0))) b0 → ⊥
  bad2506  p = false≢true (sym (cong lower p))
  cut2506 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (var 1) (op (op (var 1) (var 0)) (var 0)))) , (var 0)) → ⊥
  cut2506  adequate = bad2506  (Adequate.valid adequate Two boolean env0)
  bad2507 : PathP (λ _ → Two) (bop (bop b1 b1) (bop b0 (bop (bop b0 b1) b1))) b0 → ⊥
  bad2507  p = false≢true (sym (cong lower p))
  cut2507 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (var 1) (op (op (var 1) (var 0)) (var 0)))) , (var 1)) → ⊥
  cut2507  adequate = bad2507  (Adequate.valid adequate Two boolean env7)
  bad2508 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop (bop b0 b0) b0))) b1 → ⊥
  bad2508  p = false≢true (cong lower p)
  cut2508 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (var 1) (op (op (var 1) (var 0)) (var 0)))) , (var 2)) → ⊥
  cut2508  adequate = bad2508  (Adequate.valid adequate Two boolean env1)
  holds2509 : (z0 z1 : A2) → (mul2 (mul2 z0 z0) (mul2 z1 (mul2 (mul2 z1 z0) z1))) ≡ z0
  holds2509 z0 z1 = refl
  cut2509 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (var 1) (op (op (var 1) (var 0)) (var 1)))) , (var 0)) → ⊥
  cut2509  = reject2 ((op (op (var 0) (var 0)) (op (var 1) (op (op (var 1) (var 0)) (var 1)))) , (var 0)) (λ env → holds2509 (env 0) (env 1))
  bad2510 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b1 (bop (bop b1 b0) b1))) b1 → ⊥
  bad2510  p = false≢true (cong lower p)
  cut2510 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (var 1) (op (op (var 1) (var 0)) (var 1)))) , (var 1)) → ⊥
  cut2510  adequate = bad2510  (Adequate.valid adequate Two boolean env0)
  bad2511 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop (bop b0 b0) b0))) b1 → ⊥
  bad2511  p = false≢true (cong lower p)
  cut2511 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (var 1) (op (op (var 1) (var 0)) (var 1)))) , (var 2)) → ⊥
  cut2511  adequate = bad2511  (Adequate.valid adequate Two boolean env1)
  bad2512 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b1 (bop (bop b1 b0) b0))) b0 → ⊥
  bad2512  p = false≢true (sym (cong lower p))
  cut2512 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (var 1) (op (op (var 1) (var 0)) (var 2)))) , (var 0)) → ⊥
  cut2512  adequate = bad2512  (Adequate.valid adequate Two boolean env2)
  bad2513 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b1 (bop (bop b1 b0) b1))) b1 → ⊥
  bad2513  p = false≢true (cong lower p)
  cut2513 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (var 1) (op (op (var 1) (var 0)) (var 2)))) , (var 1)) → ⊥
  cut2513  adequate = bad2513  (Adequate.valid adequate Two boolean env8)
  bad2514 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop (bop b0 b0) b1))) b1 → ⊥
  bad2514  p = false≢true (cong lower p)
  cut2514 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (var 1) (op (op (var 1) (var 0)) (var 2)))) , (var 2)) → ⊥
  cut2514  adequate = bad2514  (Adequate.valid adequate Two boolean env1)
  bad2515 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop (bop b0 b0) b0))) b1 → ⊥
  bad2515  p = false≢true (cong lower p)
  cut2515 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (var 1) (op (op (var 1) (var 0)) (var 2)))) , (var 3)) → ⊥
  cut2515  adequate = bad2515  (Adequate.valid adequate Two boolean env3)
  bad2516 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b1 (bop (bop b1 b1) b0))) b0 → ⊥
  bad2516  p = false≢true (sym (cong lower p))
  cut2516 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (var 1) (op (op (var 1) (var 1)) (var 0)))) , (var 0)) → ⊥
  cut2516  adequate = bad2516  (Adequate.valid adequate Two boolean env0)
  bad2517 : PathP (λ _ → Two) (bop (bop b1 b1) (bop b0 (bop (bop b0 b0) b1))) b0 → ⊥
  bad2517  p = false≢true (sym (cong lower p))
  cut2517 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (var 1) (op (op (var 1) (var 1)) (var 0)))) , (var 1)) → ⊥
  cut2517  adequate = bad2517  (Adequate.valid adequate Two boolean env7)
  bad2518 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop (bop b0 b0) b0))) b1 → ⊥
  bad2518  p = false≢true (cong lower p)
  cut2518 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (var 1) (op (op (var 1) (var 1)) (var 0)))) , (var 2)) → ⊥
  cut2518  adequate = bad2518  (Adequate.valid adequate Two boolean env1)
  bad2519 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b1 (bop (bop b1 b1) b1))) b0 → ⊥
  bad2519  p = false≢true (sym (cong lower p))
  cut2519 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (var 1) (op (op (var 1) (var 1)) (var 1)))) , (var 0)) → ⊥
  cut2519  adequate = bad2519  (Adequate.valid adequate Two boolean env0)
  bad2520 : PathP (λ _ → Two) (bop (bop b1 b1) (bop b0 (bop (bop b0 b0) b0))) b0 → ⊥
  bad2520  p = false≢true (sym (cong lower p))
  cut2520 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (var 1) (op (op (var 1) (var 1)) (var 1)))) , (var 1)) → ⊥
  cut2520  adequate = bad2520  (Adequate.valid adequate Two boolean env7)
  bad2521 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop (bop b0 b0) b0))) b1 → ⊥
  bad2521  p = false≢true (cong lower p)
  cut2521 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (var 1) (op (op (var 1) (var 1)) (var 1)))) , (var 2)) → ⊥
  cut2521  adequate = bad2521  (Adequate.valid adequate Two boolean env1)
  bad2522 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b1 (bop (bop b1 b1) b0))) b0 → ⊥
  bad2522  p = false≢true (sym (cong lower p))
  cut2522 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (var 1) (op (op (var 1) (var 1)) (var 2)))) , (var 0)) → ⊥
  cut2522  adequate = bad2522  (Adequate.valid adequate Two boolean env2)
  bad2523 : PathP (λ _ → Two) (bop (bop b1 b1) (bop b0 (bop (bop b0 b0) b0))) b0 → ⊥
  bad2523  p = false≢true (sym (cong lower p))
  cut2523 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (var 1) (op (op (var 1) (var 1)) (var 2)))) , (var 1)) → ⊥
  cut2523  adequate = bad2523  (Adequate.valid adequate Two boolean env9)
  bad2524 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop (bop b0 b0) b1))) b1 → ⊥
  bad2524  p = false≢true (cong lower p)
  cut2524 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (var 1) (op (op (var 1) (var 1)) (var 2)))) , (var 2)) → ⊥
  cut2524  adequate = bad2524  (Adequate.valid adequate Two boolean env1)
  bad2525 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop (bop b0 b0) b0))) b1 → ⊥
  bad2525  p = false≢true (cong lower p)
  cut2525 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (var 1) (op (op (var 1) (var 1)) (var 2)))) , (var 3)) → ⊥
  cut2525  adequate = bad2525  (Adequate.valid adequate Two boolean env3)
  bad2526 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b1 (bop (bop b1 b0) b0))) b0 → ⊥
  bad2526  p = false≢true (sym (cong lower p))
  cut2526 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (var 1) (op (op (var 1) (var 2)) (var 0)))) , (var 0)) → ⊥
  cut2526  adequate = bad2526  (Adequate.valid adequate Two boolean env2)
  bad2527 : PathP (λ _ → Two) (bop (bop b1 b1) (bop b0 (bop (bop b0 b0) b1))) b0 → ⊥
  bad2527  p = false≢true (sym (cong lower p))
  cut2527 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (var 1) (op (op (var 1) (var 2)) (var 0)))) , (var 1)) → ⊥
  cut2527  adequate = bad2527  (Adequate.valid adequate Two boolean env9)
  bad2528 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop (bop b0 b1) b0))) b1 → ⊥
  bad2528  p = false≢true (cong lower p)
  cut2528 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (var 1) (op (op (var 1) (var 2)) (var 0)))) , (var 2)) → ⊥
  cut2528  adequate = bad2528  (Adequate.valid adequate Two boolean env1)
  bad2529 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop (bop b0 b0) b0))) b1 → ⊥
  bad2529  p = false≢true (cong lower p)
  cut2529 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (var 1) (op (op (var 1) (var 2)) (var 0)))) , (var 3)) → ⊥
  cut2529  adequate = bad2529  (Adequate.valid adequate Two boolean env3)
  bad2530 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b1 (bop (bop b1 b1) b1))) b0 → ⊥
  bad2530  p = false≢true (sym (cong lower p))
  cut2530 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (var 1) (op (op (var 1) (var 2)) (var 1)))) , (var 0)) → ⊥
  cut2530  adequate = bad2530  (Adequate.valid adequate Two boolean env8)
  bad2531 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b1 (bop (bop b1 b0) b1))) b1 → ⊥
  bad2531  p = false≢true (cong lower p)
  cut2531 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (var 1) (op (op (var 1) (var 2)) (var 1)))) , (var 1)) → ⊥
  cut2531  adequate = bad2531  (Adequate.valid adequate Two boolean env2)
  bad2532 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop (bop b0 b1) b0))) b1 → ⊥
  bad2532  p = false≢true (cong lower p)
  cut2532 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (var 1) (op (op (var 1) (var 2)) (var 1)))) , (var 2)) → ⊥
  cut2532  adequate = bad2532  (Adequate.valid adequate Two boolean env1)
  bad2533 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop (bop b0 b0) b0))) b1 → ⊥
  bad2533  p = false≢true (cong lower p)
  cut2533 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (var 1) (op (op (var 1) (var 2)) (var 1)))) , (var 3)) → ⊥
  cut2533  adequate = bad2533  (Adequate.valid adequate Two boolean env3)
  bad2534 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b1 (bop (bop b1 b0) b0))) b0 → ⊥
  bad2534  p = false≢true (sym (cong lower p))
  cut2534 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (var 1) (op (op (var 1) (var 2)) (var 2)))) , (var 0)) → ⊥
  cut2534  adequate = bad2534  (Adequate.valid adequate Two boolean env2)
  bad2535 : PathP (λ _ → Two) (bop (bop b1 b1) (bop b0 (bop (bop b0 b0) b0))) b0 → ⊥
  bad2535  p = false≢true (sym (cong lower p))
  cut2535 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (var 1) (op (op (var 1) (var 2)) (var 2)))) , (var 1)) → ⊥
  cut2535  adequate = bad2535  (Adequate.valid adequate Two boolean env9)
  bad2536 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop (bop b0 b1) b1))) b1 → ⊥
  bad2536  p = false≢true (cong lower p)
  cut2536 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (var 1) (op (op (var 1) (var 2)) (var 2)))) , (var 2)) → ⊥
  cut2536  adequate = bad2536  (Adequate.valid adequate Two boolean env1)
  bad2537 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop (bop b0 b0) b0))) b1 → ⊥
  bad2537  p = false≢true (cong lower p)
  cut2537 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (var 1) (op (op (var 1) (var 2)) (var 2)))) , (var 3)) → ⊥
  cut2537  adequate = bad2537  (Adequate.valid adequate Two boolean env3)
  bad2538 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b1 (bop (bop b1 b0) b0))) b0 → ⊥
  bad2538  p = false≢true (sym (cong lower p))
  cut2538 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (var 1) (op (op (var 1) (var 2)) (var 3)))) , (var 0)) → ⊥
  cut2538  adequate = bad2538  (Adequate.valid adequate Two boolean env4)
  bad2539 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b1 (bop (bop b1 b0) b1))) b1 → ⊥
  bad2539  p = false≢true (cong lower p)
  cut2539 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (var 1) (op (op (var 1) (var 2)) (var 3)))) , (var 1)) → ⊥
  cut2539  adequate = bad2539  (Adequate.valid adequate Two boolean env10)
  bad2540 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop (bop b0 b1) b0))) b1 → ⊥
  bad2540  p = false≢true (cong lower p)
  cut2540 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (var 1) (op (op (var 1) (var 2)) (var 3)))) , (var 2)) → ⊥
  cut2540  adequate = bad2540  (Adequate.valid adequate Two boolean env5)
  bad2541 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop (bop b0 b0) b1))) b1 → ⊥
  bad2541  p = false≢true (cong lower p)
  cut2541 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (var 1) (op (op (var 1) (var 2)) (var 3)))) , (var 3)) → ⊥
  cut2541  adequate = bad2541  (Adequate.valid adequate Two boolean env3)
  bad2542 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop (bop b0 b0) b0))) b1 → ⊥
  bad2542  p = false≢true (cong lower p)
  cut2542 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (var 1) (op (op (var 1) (var 2)) (var 3)))) , (var 4)) → ⊥
  cut2542  adequate = bad2542  (Adequate.valid adequate Two boolean env6)
  bad2543 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b1 (bop (bop b0 b0) b0))) b0 → ⊥
  bad2543  p = false≢true (sym (cong lower p))
  cut2543 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (var 1) (op (op (var 2) (var 0)) (var 0)))) , (var 0)) → ⊥
  cut2543  adequate = bad2543  (Adequate.valid adequate Two boolean env2)
  bad2544 : PathP (λ _ → Two) (bop (bop b1 b1) (bop b0 (bop (bop b0 b1) b1))) b0 → ⊥
  bad2544  p = false≢true (sym (cong lower p))
  cut2544 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (var 1) (op (op (var 2) (var 0)) (var 0)))) , (var 1)) → ⊥
  cut2544  adequate = bad2544  (Adequate.valid adequate Two boolean env9)
  bad2545 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop (bop b1 b0) b0))) b1 → ⊥
  bad2545  p = false≢true (cong lower p)
  cut2545 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (var 1) (op (op (var 2) (var 0)) (var 0)))) , (var 2)) → ⊥
  cut2545  adequate = bad2545  (Adequate.valid adequate Two boolean env1)
  bad2546 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop (bop b0 b0) b0))) b1 → ⊥
  bad2546  p = false≢true (cong lower p)
  cut2546 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (var 1) (op (op (var 2) (var 0)) (var 0)))) , (var 3)) → ⊥
  cut2546  adequate = bad2546  (Adequate.valid adequate Two boolean env3)
  holds2547 : (z0 z1 z2 : A2) → (mul2 (mul2 z0 z0) (mul2 z1 (mul2 (mul2 z2 z0) z1))) ≡ z0
  holds2547 z0 z1 z2 = refl
  cut2547 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (var 1) (op (op (var 2) (var 0)) (var 1)))) , (var 0)) → ⊥
  cut2547  = reject2 ((op (op (var 0) (var 0)) (op (var 1) (op (op (var 2) (var 0)) (var 1)))) , (var 0)) (λ env → holds2547 (env 0) (env 1) (env 2))
  bad2548 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b1 (bop (bop b0 b0) b1))) b1 → ⊥
  bad2548  p = false≢true (cong lower p)
  cut2548 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (var 1) (op (op (var 2) (var 0)) (var 1)))) , (var 1)) → ⊥
  cut2548  adequate = bad2548  (Adequate.valid adequate Two boolean env2)
  bad2549 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop (bop b1 b0) b0))) b1 → ⊥
  bad2549  p = false≢true (cong lower p)
  cut2549 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (var 1) (op (op (var 2) (var 0)) (var 1)))) , (var 2)) → ⊥
  cut2549  adequate = bad2549  (Adequate.valid adequate Two boolean env1)
  bad2550 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop (bop b0 b0) b0))) b1 → ⊥
  bad2550  p = false≢true (cong lower p)
  cut2550 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (var 1) (op (op (var 2) (var 0)) (var 1)))) , (var 3)) → ⊥
  cut2550  adequate = bad2550  (Adequate.valid adequate Two boolean env3)
  bad2551 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b1 (bop (bop b0 b0) b0))) b0 → ⊥
  bad2551  p = false≢true (sym (cong lower p))
  cut2551 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (var 1) (op (op (var 2) (var 0)) (var 2)))) , (var 0)) → ⊥
  cut2551  adequate = bad2551  (Adequate.valid adequate Two boolean env2)
  bad2552 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b1 (bop (bop b1 b0) b1))) b1 → ⊥
  bad2552  p = false≢true (cong lower p)
  cut2552 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (var 1) (op (op (var 2) (var 0)) (var 2)))) , (var 1)) → ⊥
  cut2552  adequate = bad2552  (Adequate.valid adequate Two boolean env8)
  bad2553 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop (bop b1 b0) b1))) b1 → ⊥
  bad2553  p = false≢true (cong lower p)
  cut2553 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (var 1) (op (op (var 2) (var 0)) (var 2)))) , (var 2)) → ⊥
  cut2553  adequate = bad2553  (Adequate.valid adequate Two boolean env1)
  bad2554 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop (bop b0 b0) b0))) b1 → ⊥
  bad2554  p = false≢true (cong lower p)
  cut2554 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (var 1) (op (op (var 2) (var 0)) (var 2)))) , (var 3)) → ⊥
  cut2554  adequate = bad2554  (Adequate.valid adequate Two boolean env3)
  bad2555 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b1 (bop (bop b0 b0) b0))) b0 → ⊥
  bad2555  p = false≢true (sym (cong lower p))
  cut2555 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (var 1) (op (op (var 2) (var 0)) (var 3)))) , (var 0)) → ⊥
  cut2555  adequate = bad2555  (Adequate.valid adequate Two boolean env4)
  bad2556 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b1 (bop (bop b0 b0) b1))) b1 → ⊥
  bad2556  p = false≢true (cong lower p)
  cut2556 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (var 1) (op (op (var 2) (var 0)) (var 3)))) , (var 1)) → ⊥
  cut2556  adequate = bad2556  (Adequate.valid adequate Two boolean env10)
  bad2557 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop (bop b1 b0) b0))) b1 → ⊥
  bad2557  p = false≢true (cong lower p)
  cut2557 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (var 1) (op (op (var 2) (var 0)) (var 3)))) , (var 2)) → ⊥
  cut2557  adequate = bad2557  (Adequate.valid adequate Two boolean env5)
  bad2558 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop (bop b0 b0) b1))) b1 → ⊥
  bad2558  p = false≢true (cong lower p)
  cut2558 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (var 1) (op (op (var 2) (var 0)) (var 3)))) , (var 3)) → ⊥
  cut2558  adequate = bad2558  (Adequate.valid adequate Two boolean env3)
  bad2559 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop (bop b0 b0) b0))) b1 → ⊥
  bad2559  p = false≢true (cong lower p)
  cut2559 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (var 1) (op (op (var 2) (var 0)) (var 3)))) , (var 4)) → ⊥
  cut2559  adequate = bad2559  (Adequate.valid adequate Two boolean env6)
  bad2560 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b1 (bop (bop b0 b1) b0))) b0 → ⊥
  bad2560  p = false≢true (sym (cong lower p))
  cut2560 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (var 1) (op (op (var 2) (var 1)) (var 0)))) , (var 0)) → ⊥
  cut2560  adequate = bad2560  (Adequate.valid adequate Two boolean env2)
  bad2561 : PathP (λ _ → Two) (bop (bop b1 b1) (bop b0 (bop (bop b0 b0) b1))) b0 → ⊥
  bad2561  p = false≢true (sym (cong lower p))
  cut2561 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (var 1) (op (op (var 2) (var 1)) (var 0)))) , (var 1)) → ⊥
  cut2561  adequate = bad2561  (Adequate.valid adequate Two boolean env9)
  bad2562 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop (bop b1 b0) b0))) b1 → ⊥
  bad2562  p = false≢true (cong lower p)
  cut2562 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (var 1) (op (op (var 2) (var 1)) (var 0)))) , (var 2)) → ⊥
  cut2562  adequate = bad2562  (Adequate.valid adequate Two boolean env1)
  bad2563 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop (bop b0 b0) b0))) b1 → ⊥
  bad2563  p = false≢true (cong lower p)
  cut2563 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (var 1) (op (op (var 2) (var 1)) (var 0)))) , (var 3)) → ⊥
  cut2563  adequate = bad2563  (Adequate.valid adequate Two boolean env3)
  bad2564 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b1 (bop (bop b1 b1) b1))) b0 → ⊥
  bad2564  p = false≢true (sym (cong lower p))
  cut2564 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (var 1) (op (op (var 2) (var 1)) (var 1)))) , (var 0)) → ⊥
  cut2564  adequate = bad2564  (Adequate.valid adequate Two boolean env8)
  bad2565 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b1 (bop (bop b0 b1) b1))) b1 → ⊥
  bad2565  p = false≢true (cong lower p)
  cut2565 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (var 1) (op (op (var 2) (var 1)) (var 1)))) , (var 1)) → ⊥
  cut2565  adequate = bad2565  (Adequate.valid adequate Two boolean env2)
  bad2566 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop (bop b1 b0) b0))) b1 → ⊥
  bad2566  p = false≢true (cong lower p)
  cut2566 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (var 1) (op (op (var 2) (var 1)) (var 1)))) , (var 2)) → ⊥
  cut2566  adequate = bad2566  (Adequate.valid adequate Two boolean env1)
  bad2567 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop (bop b0 b0) b0))) b1 → ⊥
  bad2567  p = false≢true (cong lower p)
  cut2567 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (var 1) (op (op (var 2) (var 1)) (var 1)))) , (var 3)) → ⊥
  cut2567  adequate = bad2567  (Adequate.valid adequate Two boolean env3)
  bad2568 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b1 (bop (bop b0 b1) b0))) b0 → ⊥
  bad2568  p = false≢true (sym (cong lower p))
  cut2568 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (var 1) (op (op (var 2) (var 1)) (var 2)))) , (var 0)) → ⊥
  cut2568  adequate = bad2568  (Adequate.valid adequate Two boolean env2)
  bad2569 : PathP (λ _ → Two) (bop (bop b1 b1) (bop b0 (bop (bop b0 b0) b0))) b0 → ⊥
  bad2569  p = false≢true (sym (cong lower p))
  cut2569 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (var 1) (op (op (var 2) (var 1)) (var 2)))) , (var 1)) → ⊥
  cut2569  adequate = bad2569  (Adequate.valid adequate Two boolean env9)
  bad2570 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop (bop b1 b0) b1))) b1 → ⊥
  bad2570  p = false≢true (cong lower p)
  cut2570 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (var 1) (op (op (var 2) (var 1)) (var 2)))) , (var 2)) → ⊥
  cut2570  adequate = bad2570  (Adequate.valid adequate Two boolean env1)
  bad2571 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop (bop b0 b0) b0))) b1 → ⊥
  bad2571  p = false≢true (cong lower p)
  cut2571 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (var 1) (op (op (var 2) (var 1)) (var 2)))) , (var 3)) → ⊥
  cut2571  adequate = bad2571  (Adequate.valid adequate Two boolean env3)
  bad2572 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b1 (bop (bop b0 b1) b0))) b0 → ⊥
  bad2572  p = false≢true (sym (cong lower p))
  cut2572 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (var 1) (op (op (var 2) (var 1)) (var 3)))) , (var 0)) → ⊥
  cut2572  adequate = bad2572  (Adequate.valid adequate Two boolean env4)
  bad2573 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b1 (bop (bop b0 b1) b1))) b1 → ⊥
  bad2573  p = false≢true (cong lower p)
  cut2573 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (var 1) (op (op (var 2) (var 1)) (var 3)))) , (var 1)) → ⊥
  cut2573  adequate = bad2573  (Adequate.valid adequate Two boolean env10)
  bad2574 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop (bop b1 b0) b0))) b1 → ⊥
  bad2574  p = false≢true (cong lower p)
  cut2574 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (var 1) (op (op (var 2) (var 1)) (var 3)))) , (var 2)) → ⊥
  cut2574  adequate = bad2574  (Adequate.valid adequate Two boolean env5)
  bad2575 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop (bop b0 b0) b1))) b1 → ⊥
  bad2575  p = false≢true (cong lower p)
  cut2575 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (var 1) (op (op (var 2) (var 1)) (var 3)))) , (var 3)) → ⊥
  cut2575  adequate = bad2575  (Adequate.valid adequate Two boolean env3)
  bad2576 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop (bop b0 b0) b0))) b1 → ⊥
  bad2576  p = false≢true (cong lower p)
  cut2576 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (var 1) (op (op (var 2) (var 1)) (var 3)))) , (var 4)) → ⊥
  cut2576  adequate = bad2576  (Adequate.valid adequate Two boolean env6)
  bad2577 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b1 (bop (bop b0 b0) b0))) b0 → ⊥
  bad2577  p = false≢true (sym (cong lower p))
  cut2577 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (var 1) (op (op (var 2) (var 2)) (var 0)))) , (var 0)) → ⊥
  cut2577  adequate = bad2577  (Adequate.valid adequate Two boolean env2)
  bad2578 : PathP (λ _ → Two) (bop (bop b1 b1) (bop b0 (bop (bop b0 b0) b1))) b0 → ⊥
  bad2578  p = false≢true (sym (cong lower p))
  cut2578 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (var 1) (op (op (var 2) (var 2)) (var 0)))) , (var 1)) → ⊥
  cut2578  adequate = bad2578  (Adequate.valid adequate Two boolean env9)
  bad2579 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop (bop b1 b1) b0))) b1 → ⊥
  bad2579  p = false≢true (cong lower p)
  cut2579 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (var 1) (op (op (var 2) (var 2)) (var 0)))) , (var 2)) → ⊥
  cut2579  adequate = bad2579  (Adequate.valid adequate Two boolean env1)
  bad2580 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop (bop b0 b0) b0))) b1 → ⊥
  bad2580  p = false≢true (cong lower p)
  cut2580 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (var 1) (op (op (var 2) (var 2)) (var 0)))) , (var 3)) → ⊥
  cut2580  adequate = bad2580  (Adequate.valid adequate Two boolean env3)
  bad2581 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b1 (bop (bop b1 b1) b1))) b0 → ⊥
  bad2581  p = false≢true (sym (cong lower p))
  cut2581 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (var 1) (op (op (var 2) (var 2)) (var 1)))) , (var 0)) → ⊥
  cut2581  adequate = bad2581  (Adequate.valid adequate Two boolean env8)
  bad2582 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b1 (bop (bop b0 b0) b1))) b1 → ⊥
  bad2582  p = false≢true (cong lower p)
  cut2582 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (var 1) (op (op (var 2) (var 2)) (var 1)))) , (var 1)) → ⊥
  cut2582  adequate = bad2582  (Adequate.valid adequate Two boolean env2)
  bad2583 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop (bop b1 b1) b0))) b1 → ⊥
  bad2583  p = false≢true (cong lower p)
  cut2583 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (var 1) (op (op (var 2) (var 2)) (var 1)))) , (var 2)) → ⊥
  cut2583  adequate = bad2583  (Adequate.valid adequate Two boolean env1)
  bad2584 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop (bop b0 b0) b0))) b1 → ⊥
  bad2584  p = false≢true (cong lower p)
  cut2584 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (var 1) (op (op (var 2) (var 2)) (var 1)))) , (var 3)) → ⊥
  cut2584  adequate = bad2584  (Adequate.valid adequate Two boolean env3)
  bad2585 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b1 (bop (bop b0 b0) b0))) b0 → ⊥
  bad2585  p = false≢true (sym (cong lower p))
  cut2585 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (var 1) (op (op (var 2) (var 2)) (var 2)))) , (var 0)) → ⊥
  cut2585  adequate = bad2585  (Adequate.valid adequate Two boolean env2)
  bad2586 : PathP (λ _ → Two) (bop (bop b1 b1) (bop b0 (bop (bop b0 b0) b0))) b0 → ⊥
  bad2586  p = false≢true (sym (cong lower p))
  cut2586 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (var 1) (op (op (var 2) (var 2)) (var 2)))) , (var 1)) → ⊥
  cut2586  adequate = bad2586  (Adequate.valid adequate Two boolean env9)
  bad2587 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop (bop b1 b1) b1))) b1 → ⊥
  bad2587  p = false≢true (cong lower p)
  cut2587 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (var 1) (op (op (var 2) (var 2)) (var 2)))) , (var 2)) → ⊥
  cut2587  adequate = bad2587  (Adequate.valid adequate Two boolean env1)
  bad2588 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop (bop b0 b0) b0))) b1 → ⊥
  bad2588  p = false≢true (cong lower p)
  cut2588 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (var 1) (op (op (var 2) (var 2)) (var 2)))) , (var 3)) → ⊥
  cut2588  adequate = bad2588  (Adequate.valid adequate Two boolean env3)
  bad2589 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b1 (bop (bop b0 b0) b0))) b0 → ⊥
  bad2589  p = false≢true (sym (cong lower p))
  cut2589 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (var 1) (op (op (var 2) (var 2)) (var 3)))) , (var 0)) → ⊥
  cut2589  adequate = bad2589  (Adequate.valid adequate Two boolean env4)
  bad2590 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b1 (bop (bop b0 b0) b1))) b1 → ⊥
  bad2590  p = false≢true (cong lower p)
  cut2590 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (var 1) (op (op (var 2) (var 2)) (var 3)))) , (var 1)) → ⊥
  cut2590  adequate = bad2590  (Adequate.valid adequate Two boolean env10)
  bad2591 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop (bop b1 b1) b0))) b1 → ⊥
  bad2591  p = false≢true (cong lower p)
  cut2591 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (var 1) (op (op (var 2) (var 2)) (var 3)))) , (var 2)) → ⊥
  cut2591  adequate = bad2591  (Adequate.valid adequate Two boolean env5)
  bad2592 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop (bop b0 b0) b1))) b1 → ⊥
  bad2592  p = false≢true (cong lower p)
  cut2592 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (var 1) (op (op (var 2) (var 2)) (var 3)))) , (var 3)) → ⊥
  cut2592  adequate = bad2592  (Adequate.valid adequate Two boolean env3)
  bad2593 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop (bop b0 b0) b0))) b1 → ⊥
  bad2593  p = false≢true (cong lower p)
  cut2593 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (var 1) (op (op (var 2) (var 2)) (var 3)))) , (var 4)) → ⊥
  cut2593  adequate = bad2593  (Adequate.valid adequate Two boolean env6)
  bad2594 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b1 (bop (bop b0 b0) b0))) b0 → ⊥
  bad2594  p = false≢true (sym (cong lower p))
  cut2594 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (var 1) (op (op (var 2) (var 3)) (var 0)))) , (var 0)) → ⊥
  cut2594  adequate = bad2594  (Adequate.valid adequate Two boolean env4)
  env11 : ℕ → Two
  env11 zero = b1
  env11 (suc zero) = b0
  env11 (suc (suc zero)) = b0
  env11 (suc (suc (suc zero))) = b0
  env11 (suc (suc (suc (suc rest)))) = b0
  bad2595 : PathP (λ _ → Two) (bop (bop b1 b1) (bop b0 (bop (bop b0 b0) b1))) b0 → ⊥
  bad2595  p = false≢true (sym (cong lower p))
  cut2595 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (var 1) (op (op (var 2) (var 3)) (var 0)))) , (var 1)) → ⊥
  cut2595  adequate = bad2595  (Adequate.valid adequate Two boolean env11)
  bad2596 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop (bop b1 b0) b0))) b1 → ⊥
  bad2596  p = false≢true (cong lower p)
  cut2596 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (var 1) (op (op (var 2) (var 3)) (var 0)))) , (var 2)) → ⊥
  cut2596  adequate = bad2596  (Adequate.valid adequate Two boolean env5)
  bad2597 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop (bop b0 b1) b0))) b1 → ⊥
  bad2597  p = false≢true (cong lower p)
  cut2597 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (var 1) (op (op (var 2) (var 3)) (var 0)))) , (var 3)) → ⊥
  cut2597  adequate = bad2597  (Adequate.valid adequate Two boolean env3)
  bad2598 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop (bop b0 b0) b0))) b1 → ⊥
  bad2598  p = false≢true (cong lower p)
  cut2598 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (var 1) (op (op (var 2) (var 3)) (var 0)))) , (var 4)) → ⊥
  cut2598  adequate = bad2598  (Adequate.valid adequate Two boolean env6)
  env12 : ℕ → Two
  env12 zero = b0
  env12 (suc zero) = b1
  env12 (suc (suc zero)) = b1
  env12 (suc (suc (suc zero))) = b1
  env12 (suc (suc (suc (suc rest)))) = b0
  bad2599 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b1 (bop (bop b1 b1) b1))) b0 → ⊥
  bad2599  p = false≢true (sym (cong lower p))
  cut2599 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (var 1) (op (op (var 2) (var 3)) (var 1)))) , (var 0)) → ⊥
  cut2599  adequate = bad2599  (Adequate.valid adequate Two boolean env12)
  bad2600 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b1 (bop (bop b0 b0) b1))) b1 → ⊥
  bad2600  p = false≢true (cong lower p)
  cut2600 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (var 1) (op (op (var 2) (var 3)) (var 1)))) , (var 1)) → ⊥
  cut2600  adequate = bad2600  (Adequate.valid adequate Two boolean env4)
  bad2601 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop (bop b1 b0) b0))) b1 → ⊥
  bad2601  p = false≢true (cong lower p)
  cut2601 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (var 1) (op (op (var 2) (var 3)) (var 1)))) , (var 2)) → ⊥
  cut2601  adequate = bad2601  (Adequate.valid adequate Two boolean env5)
  bad2602 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop (bop b0 b1) b0))) b1 → ⊥
  bad2602  p = false≢true (cong lower p)
  cut2602 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (var 1) (op (op (var 2) (var 3)) (var 1)))) , (var 3)) → ⊥
  cut2602  adequate = bad2602  (Adequate.valid adequate Two boolean env3)
  bad2603 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop (bop b0 b0) b0))) b1 → ⊥
  bad2603  p = false≢true (cong lower p)
  cut2603 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (var 1) (op (op (var 2) (var 3)) (var 1)))) , (var 4)) → ⊥
  cut2603  adequate = bad2603  (Adequate.valid adequate Two boolean env6)
  bad2604 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b1 (bop (bop b0 b0) b0))) b0 → ⊥
  bad2604  p = false≢true (sym (cong lower p))
  cut2604 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (var 1) (op (op (var 2) (var 3)) (var 2)))) , (var 0)) → ⊥
  cut2604  adequate = bad2604  (Adequate.valid adequate Two boolean env4)
  env13 : ℕ → Two
  env13 zero = b0
  env13 (suc zero) = b1
  env13 (suc (suc zero)) = b1
  env13 (suc (suc (suc zero))) = b0
  env13 (suc (suc (suc (suc rest)))) = b0
  bad2605 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b1 (bop (bop b1 b0) b1))) b1 → ⊥
  bad2605  p = false≢true (cong lower p)
  cut2605 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (var 1) (op (op (var 2) (var 3)) (var 2)))) , (var 1)) → ⊥
  cut2605  adequate = bad2605  (Adequate.valid adequate Two boolean env13)
  bad2606 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop (bop b1 b0) b1))) b1 → ⊥
  bad2606  p = false≢true (cong lower p)
  cut2606 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (var 1) (op (op (var 2) (var 3)) (var 2)))) , (var 2)) → ⊥
  cut2606  adequate = bad2606  (Adequate.valid adequate Two boolean env5)
  bad2607 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop (bop b0 b1) b0))) b1 → ⊥
  bad2607  p = false≢true (cong lower p)
  cut2607 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (var 1) (op (op (var 2) (var 3)) (var 2)))) , (var 3)) → ⊥
  cut2607  adequate = bad2607  (Adequate.valid adequate Two boolean env3)
  bad2608 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop (bop b0 b0) b0))) b1 → ⊥
  bad2608  p = false≢true (cong lower p)
  cut2608 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (var 1) (op (op (var 2) (var 3)) (var 2)))) , (var 4)) → ⊥
  cut2608  adequate = bad2608  (Adequate.valid adequate Two boolean env6)
  bad2609 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b1 (bop (bop b0 b0) b0))) b0 → ⊥
  bad2609  p = false≢true (sym (cong lower p))
  cut2609 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (var 1) (op (op (var 2) (var 3)) (var 3)))) , (var 0)) → ⊥
  cut2609  adequate = bad2609  (Adequate.valid adequate Two boolean env4)
  bad2610 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b1 (bop (bop b0 b1) b1))) b1 → ⊥
  bad2610  p = false≢true (cong lower p)
  cut2610 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (var 1) (op (op (var 2) (var 3)) (var 3)))) , (var 1)) → ⊥
  cut2610  adequate = bad2610  (Adequate.valid adequate Two boolean env10)
  bad2611 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop (bop b1 b0) b0))) b1 → ⊥
  bad2611  p = false≢true (cong lower p)
  cut2611 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (var 1) (op (op (var 2) (var 3)) (var 3)))) , (var 2)) → ⊥
  cut2611  adequate = bad2611  (Adequate.valid adequate Two boolean env5)
  bad2612 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop (bop b0 b1) b1))) b1 → ⊥
  bad2612  p = false≢true (cong lower p)
  cut2612 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (var 1) (op (op (var 2) (var 3)) (var 3)))) , (var 3)) → ⊥
  cut2612  adequate = bad2612  (Adequate.valid adequate Two boolean env3)
  bad2613 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop (bop b0 b0) b0))) b1 → ⊥
  bad2613  p = false≢true (cong lower p)
  cut2613 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (var 1) (op (op (var 2) (var 3)) (var 3)))) , (var 4)) → ⊥
  cut2613  adequate = bad2613  (Adequate.valid adequate Two boolean env6)
  env14 : ℕ → Two
  env14 zero = b0
  env14 (suc zero) = b1
  env14 (suc (suc zero)) = b0
  env14 (suc (suc (suc zero))) = b0
  env14 (suc (suc (suc (suc zero)))) = b0
  env14 (suc (suc (suc (suc (suc rest))))) = b0
  bad2614 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b1 (bop (bop b0 b0) b0))) b0 → ⊥
  bad2614  p = false≢true (sym (cong lower p))
  cut2614 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (var 1) (op (op (var 2) (var 3)) (var 4)))) , (var 0)) → ⊥
  cut2614  adequate = bad2614  (Adequate.valid adequate Two boolean env14)
  env15 : ℕ → Two
  env15 zero = b0
  env15 (suc zero) = b1
  env15 (suc (suc zero)) = b0
  env15 (suc (suc (suc zero))) = b0
  env15 (suc (suc (suc (suc zero)))) = b1
  env15 (suc (suc (suc (suc (suc rest))))) = b0
  bad2615 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b1 (bop (bop b0 b0) b1))) b1 → ⊥
  bad2615  p = false≢true (cong lower p)
  cut2615 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (var 1) (op (op (var 2) (var 3)) (var 4)))) , (var 1)) → ⊥
  cut2615  adequate = bad2615  (Adequate.valid adequate Two boolean env15)
  env16 : ℕ → Two
  env16 zero = b0
  env16 (suc zero) = b0
  env16 (suc (suc zero)) = b1
  env16 (suc (suc (suc zero))) = b0
  env16 (suc (suc (suc (suc zero)))) = b0
  env16 (suc (suc (suc (suc (suc rest))))) = b0
  bad2616 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop (bop b1 b0) b0))) b1 → ⊥
  bad2616  p = false≢true (cong lower p)
  cut2616 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (var 1) (op (op (var 2) (var 3)) (var 4)))) , (var 2)) → ⊥
  cut2616  adequate = bad2616  (Adequate.valid adequate Two boolean env16)
  env17 : ℕ → Two
  env17 zero = b0
  env17 (suc zero) = b0
  env17 (suc (suc zero)) = b0
  env17 (suc (suc (suc zero))) = b1
  env17 (suc (suc (suc (suc zero)))) = b0
  env17 (suc (suc (suc (suc (suc rest))))) = b0
  bad2617 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop (bop b0 b1) b0))) b1 → ⊥
  bad2617  p = false≢true (cong lower p)
  cut2617 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (var 1) (op (op (var 2) (var 3)) (var 4)))) , (var 3)) → ⊥
  cut2617  adequate = bad2617  (Adequate.valid adequate Two boolean env17)
  bad2618 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop (bop b0 b0) b1))) b1 → ⊥
  bad2618  p = false≢true (cong lower p)
  cut2618 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (var 1) (op (op (var 2) (var 3)) (var 4)))) , (var 4)) → ⊥
  cut2618  adequate = bad2618  (Adequate.valid adequate Two boolean env6)
  env18 : ℕ → Two
  env18 zero = b0
  env18 (suc zero) = b0
  env18 (suc (suc zero)) = b0
  env18 (suc (suc (suc zero))) = b0
  env18 (suc (suc (suc (suc zero)))) = b0
  env18 (suc (suc (suc (suc (suc zero))))) = b1
  env18 (suc (suc (suc (suc (suc (suc rest)))))) = b0
  bad2619 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop (bop b0 b0) b0))) b1 → ⊥
  bad2619  p = false≢true (cong lower p)
  cut2619 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (var 1) (op (op (var 2) (var 3)) (var 4)))) , (var 5)) → ⊥
  cut2619  adequate = bad2619  (Adequate.valid adequate Two boolean env18)
  holds2620 : (z0 z1 : A2) → (mul2 (mul2 z0 z1) (mul2 z0 (mul2 (mul2 z0 z0) z0))) ≡ z0
  holds2620 z0 z1 = refl
  cut2620 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 0) (op (op (var 0) (var 0)) (var 0)))) , (var 0)) → ⊥
  cut2620  = reject2 ((op (op (var 0) (var 1)) (op (var 0) (op (op (var 0) (var 0)) (var 0)))) , (var 0)) (λ env → holds2620 (env 0) (env 1))
  bad2621 : PathP (λ _ → Two) (bop (bop b0 b1) (bop b0 (bop (bop b0 b0) b0))) b1 → ⊥
  bad2621  p = false≢true (cong lower p)
  cut2621 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 0) (op (op (var 0) (var 0)) (var 0)))) , (var 1)) → ⊥
  cut2621  adequate = bad2621  (Adequate.valid adequate Two boolean env0)
  bad2622 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop (bop b0 b0) b0))) b1 → ⊥
  bad2622  p = false≢true (cong lower p)
  cut2622 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 0) (op (op (var 0) (var 0)) (var 0)))) , (var 2)) → ⊥
  cut2622  adequate = bad2622  (Adequate.valid adequate Two boolean env1)
  holds2623 : (z0 z1 : A2) → (mul2 (mul2 z0 z1) (mul2 z0 (mul2 (mul2 z0 z0) z1))) ≡ z0
  holds2623 z0 z1 = refl
  cut2623 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 0) (op (op (var 0) (var 0)) (var 1)))) , (var 0)) → ⊥
  cut2623  = reject2 ((op (op (var 0) (var 1)) (op (var 0) (op (op (var 0) (var 0)) (var 1)))) , (var 0)) (λ env → holds2623 (env 0) (env 1))
  bad2624 : PathP (λ _ → Two) (bop (bop b0 b1) (bop b0 (bop (bop b0 b0) b1))) b1 → ⊥
  bad2624  p = false≢true (cong lower p)
  cut2624 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 0) (op (op (var 0) (var 0)) (var 1)))) , (var 1)) → ⊥
  cut2624  adequate = bad2624  (Adequate.valid adequate Two boolean env0)
  bad2625 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop (bop b0 b0) b0))) b1 → ⊥
  bad2625  p = false≢true (cong lower p)
  cut2625 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 0) (op (op (var 0) (var 0)) (var 1)))) , (var 2)) → ⊥
  cut2625  adequate = bad2625  (Adequate.valid adequate Two boolean env1)
  holds2626 : (z0 z1 z2 : A2) → (mul2 (mul2 z0 z1) (mul2 z0 (mul2 (mul2 z0 z0) z2))) ≡ z0
  holds2626 z0 z1 z2 = refl
  cut2626 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 0) (op (op (var 0) (var 0)) (var 2)))) , (var 0)) → ⊥
  cut2626  = reject2 ((op (op (var 0) (var 1)) (op (var 0) (op (op (var 0) (var 0)) (var 2)))) , (var 0)) (λ env → holds2626 (env 0) (env 1) (env 2))
  bad2627 : PathP (λ _ → Two) (bop (bop b0 b1) (bop b0 (bop (bop b0 b0) b0))) b1 → ⊥
  bad2627  p = false≢true (cong lower p)
  cut2627 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 0) (op (op (var 0) (var 0)) (var 2)))) , (var 1)) → ⊥
  cut2627  adequate = bad2627  (Adequate.valid adequate Two boolean env2)
  bad2628 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop (bop b0 b0) b1))) b1 → ⊥
  bad2628  p = false≢true (cong lower p)
  cut2628 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 0) (op (op (var 0) (var 0)) (var 2)))) , (var 2)) → ⊥
  cut2628  adequate = bad2628  (Adequate.valid adequate Two boolean env1)
  bad2629 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop (bop b0 b0) b0))) b1 → ⊥
  bad2629  p = false≢true (cong lower p)
  cut2629 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 0) (op (op (var 0) (var 0)) (var 2)))) , (var 3)) → ⊥
  cut2629  adequate = bad2629  (Adequate.valid adequate Two boolean env3)
  bad2630 : PathP (λ _ → Two) (bop (bop b1 b0) (bop b1 (bop (bop b1 b0) b1))) b1 → ⊥
  bad2630  p = false≢true (cong lower p)
  cut2630 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 0) (op (op (var 0) (var 1)) (var 0)))) , (var 0)) → ⊥
  cut2630  adequate = bad2630  (Adequate.valid adequate Two boolean env7)
  bad2631 : PathP (λ _ → Two) (bop (bop b0 b1) (bop b0 (bop (bop b0 b1) b0))) b1 → ⊥
  bad2631  p = false≢true (cong lower p)
  cut2631 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 0) (op (op (var 0) (var 1)) (var 0)))) , (var 1)) → ⊥
  cut2631  adequate = bad2631  (Adequate.valid adequate Two boolean env0)
  bad2632 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop (bop b0 b0) b0))) b1 → ⊥
  bad2632  p = false≢true (cong lower p)
  cut2632 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 0) (op (op (var 0) (var 1)) (var 0)))) , (var 2)) → ⊥
  cut2632  adequate = bad2632  (Adequate.valid adequate Two boolean env1)
  holds2633 : (z0 z1 : A2) → (mul2 (mul2 z0 z1) (mul2 z0 (mul2 (mul2 z0 z1) z1))) ≡ z0
  holds2633 z0 z1 = refl
  cut2633 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 0) (op (op (var 0) (var 1)) (var 1)))) , (var 0)) → ⊥
  cut2633  = reject2 ((op (op (var 0) (var 1)) (op (var 0) (op (op (var 0) (var 1)) (var 1)))) , (var 0)) (λ env → holds2633 (env 0) (env 1))
  bad2634 : PathP (λ _ → Two) (bop (bop b0 b1) (bop b0 (bop (bop b0 b1) b1))) b1 → ⊥
  bad2634  p = false≢true (cong lower p)
  cut2634 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 0) (op (op (var 0) (var 1)) (var 1)))) , (var 1)) → ⊥
  cut2634  adequate = bad2634  (Adequate.valid adequate Two boolean env0)
  bad2635 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop (bop b0 b0) b0))) b1 → ⊥
  bad2635  p = false≢true (cong lower p)
  cut2635 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 0) (op (op (var 0) (var 1)) (var 1)))) , (var 2)) → ⊥
  cut2635  adequate = bad2635  (Adequate.valid adequate Two boolean env1)
  env19 : ℕ → Two
  env19 zero = b1
  env19 (suc zero) = b0
  env19 (suc (suc zero)) = b1
  env19 (suc (suc (suc rest))) = b0
  bad2636 : PathP (λ _ → Two) (bop (bop b1 b0) (bop b1 (bop (bop b1 b0) b1))) b1 → ⊥
  bad2636  p = false≢true (cong lower p)
  cut2636 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 0) (op (op (var 0) (var 1)) (var 2)))) , (var 0)) → ⊥
  cut2636  adequate = bad2636  (Adequate.valid adequate Two boolean env19)
  bad2637 : PathP (λ _ → Two) (bop (bop b0 b1) (bop b0 (bop (bop b0 b1) b0))) b1 → ⊥
  bad2637  p = false≢true (cong lower p)
  cut2637 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 0) (op (op (var 0) (var 1)) (var 2)))) , (var 1)) → ⊥
  cut2637  adequate = bad2637  (Adequate.valid adequate Two boolean env2)
  bad2638 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop (bop b0 b0) b1))) b1 → ⊥
  bad2638  p = false≢true (cong lower p)
  cut2638 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 0) (op (op (var 0) (var 1)) (var 2)))) , (var 2)) → ⊥
  cut2638  adequate = bad2638  (Adequate.valid adequate Two boolean env1)
  bad2639 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop (bop b0 b0) b0))) b1 → ⊥
  bad2639  p = false≢true (cong lower p)
  cut2639 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 0) (op (op (var 0) (var 1)) (var 2)))) , (var 3)) → ⊥
  cut2639  adequate = bad2639  (Adequate.valid adequate Two boolean env3)
  bad2640 : PathP (λ _ → Two) (bop (bop b1 b0) (bop b1 (bop (bop b1 b0) b1))) b1 → ⊥
  bad2640  p = false≢true (cong lower p)
  cut2640 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 0) (op (op (var 0) (var 2)) (var 0)))) , (var 0)) → ⊥
  cut2640  adequate = bad2640  (Adequate.valid adequate Two boolean env9)
  bad2641 : PathP (λ _ → Two) (bop (bop b0 b1) (bop b0 (bop (bop b0 b0) b0))) b1 → ⊥
  bad2641  p = false≢true (cong lower p)
  cut2641 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 0) (op (op (var 0) (var 2)) (var 0)))) , (var 1)) → ⊥
  cut2641  adequate = bad2641  (Adequate.valid adequate Two boolean env2)
  bad2642 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop (bop b0 b1) b0))) b1 → ⊥
  bad2642  p = false≢true (cong lower p)
  cut2642 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 0) (op (op (var 0) (var 2)) (var 0)))) , (var 2)) → ⊥
  cut2642  adequate = bad2642  (Adequate.valid adequate Two boolean env1)
  bad2643 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop (bop b0 b0) b0))) b1 → ⊥
  bad2643  p = false≢true (cong lower p)
  cut2643 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 0) (op (op (var 0) (var 2)) (var 0)))) , (var 3)) → ⊥
  cut2643  adequate = bad2643  (Adequate.valid adequate Two boolean env3)
  holds2644 : (z0 z1 z2 : A2) → (mul2 (mul2 z0 z1) (mul2 z0 (mul2 (mul2 z0 z2) z1))) ≡ z0
  holds2644 z0 z1 z2 = refl
  cut2644 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 0) (op (op (var 0) (var 2)) (var 1)))) , (var 0)) → ⊥
  cut2644  = reject2 ((op (op (var 0) (var 1)) (op (var 0) (op (op (var 0) (var 2)) (var 1)))) , (var 0)) (λ env → holds2644 (env 0) (env 1) (env 2))
  bad2645 : PathP (λ _ → Two) (bop (bop b0 b1) (bop b0 (bop (bop b0 b0) b1))) b1 → ⊥
  bad2645  p = false≢true (cong lower p)
  cut2645 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 0) (op (op (var 0) (var 2)) (var 1)))) , (var 1)) → ⊥
  cut2645  adequate = bad2645  (Adequate.valid adequate Two boolean env2)
  bad2646 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop (bop b0 b1) b0))) b1 → ⊥
  bad2646  p = false≢true (cong lower p)
  cut2646 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 0) (op (op (var 0) (var 2)) (var 1)))) , (var 2)) → ⊥
  cut2646  adequate = bad2646  (Adequate.valid adequate Two boolean env1)
  bad2647 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop (bop b0 b0) b0))) b1 → ⊥
  bad2647  p = false≢true (cong lower p)
  cut2647 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 0) (op (op (var 0) (var 2)) (var 1)))) , (var 3)) → ⊥
  cut2647  adequate = bad2647  (Adequate.valid adequate Two boolean env3)
  holds2648 : (z0 z1 z2 : A2) → (mul2 (mul2 z0 z1) (mul2 z0 (mul2 (mul2 z0 z2) z2))) ≡ z0
  holds2648 z0 z1 z2 = refl
  cut2648 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 0) (op (op (var 0) (var 2)) (var 2)))) , (var 0)) → ⊥
  cut2648  = reject2 ((op (op (var 0) (var 1)) (op (var 0) (op (op (var 0) (var 2)) (var 2)))) , (var 0)) (λ env → holds2648 (env 0) (env 1) (env 2))
  bad2649 : PathP (λ _ → Two) (bop (bop b0 b1) (bop b0 (bop (bop b0 b0) b0))) b1 → ⊥
  bad2649  p = false≢true (cong lower p)
  cut2649 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 0) (op (op (var 0) (var 2)) (var 2)))) , (var 1)) → ⊥
  cut2649  adequate = bad2649  (Adequate.valid adequate Two boolean env2)
  bad2650 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop (bop b0 b1) b1))) b1 → ⊥
  bad2650  p = false≢true (cong lower p)
  cut2650 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 0) (op (op (var 0) (var 2)) (var 2)))) , (var 2)) → ⊥
  cut2650  adequate = bad2650  (Adequate.valid adequate Two boolean env1)
  bad2651 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop (bop b0 b0) b0))) b1 → ⊥
  bad2651  p = false≢true (cong lower p)
  cut2651 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 0) (op (op (var 0) (var 2)) (var 2)))) , (var 3)) → ⊥
  cut2651  adequate = bad2651  (Adequate.valid adequate Two boolean env3)
  env20 : ℕ → Two
  env20 zero = b1
  env20 (suc zero) = b0
  env20 (suc (suc zero)) = b0
  env20 (suc (suc (suc zero))) = b1
  env20 (suc (suc (suc (suc rest)))) = b0
  bad2652 : PathP (λ _ → Two) (bop (bop b1 b0) (bop b1 (bop (bop b1 b0) b1))) b1 → ⊥
  bad2652  p = false≢true (cong lower p)
  cut2652 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 0) (op (op (var 0) (var 2)) (var 3)))) , (var 0)) → ⊥
  cut2652  adequate = bad2652  (Adequate.valid adequate Two boolean env20)
  bad2653 : PathP (λ _ → Two) (bop (bop b0 b1) (bop b0 (bop (bop b0 b0) b0))) b1 → ⊥
  bad2653  p = false≢true (cong lower p)
  cut2653 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 0) (op (op (var 0) (var 2)) (var 3)))) , (var 1)) → ⊥
  cut2653  adequate = bad2653  (Adequate.valid adequate Two boolean env4)
  bad2654 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop (bop b0 b1) b0))) b1 → ⊥
  bad2654  p = false≢true (cong lower p)
  cut2654 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 0) (op (op (var 0) (var 2)) (var 3)))) , (var 2)) → ⊥
  cut2654  adequate = bad2654  (Adequate.valid adequate Two boolean env5)
  bad2655 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop (bop b0 b0) b1))) b1 → ⊥
  bad2655  p = false≢true (cong lower p)
  cut2655 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 0) (op (op (var 0) (var 2)) (var 3)))) , (var 3)) → ⊥
  cut2655  adequate = bad2655  (Adequate.valid adequate Two boolean env3)
  bad2656 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop (bop b0 b0) b0))) b1 → ⊥
  bad2656  p = false≢true (cong lower p)
  cut2656 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 0) (op (op (var 0) (var 2)) (var 3)))) , (var 4)) → ⊥
  cut2656  adequate = bad2656  (Adequate.valid adequate Two boolean env6)
  bad2657 : PathP (λ _ → Two) (bop (bop b1 b0) (bop b1 (bop (bop b0 b1) b1))) b1 → ⊥
  bad2657  p = false≢true (cong lower p)
  cut2657 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 0) (op (op (var 1) (var 0)) (var 0)))) , (var 0)) → ⊥
  cut2657  adequate = bad2657  (Adequate.valid adequate Two boolean env7)
  bad2658 : PathP (λ _ → Two) (bop (bop b0 b1) (bop b0 (bop (bop b1 b0) b0))) b1 → ⊥
  bad2658  p = false≢true (cong lower p)
  cut2658 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 0) (op (op (var 1) (var 0)) (var 0)))) , (var 1)) → ⊥
  cut2658  adequate = bad2658  (Adequate.valid adequate Two boolean env0)
  bad2659 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop (bop b0 b0) b0))) b1 → ⊥
  bad2659  p = false≢true (cong lower p)
  cut2659 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 0) (op (op (var 1) (var 0)) (var 0)))) , (var 2)) → ⊥
  cut2659  adequate = bad2659  (Adequate.valid adequate Two boolean env1)
  holds2660 : (z0 z1 : A2) → (mul2 (mul2 z0 z1) (mul2 z0 (mul2 (mul2 z1 z0) z1))) ≡ z0
  holds2660 z0 z1 = refl
  cut2660 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 0) (op (op (var 1) (var 0)) (var 1)))) , (var 0)) → ⊥
  cut2660  = reject2 ((op (op (var 0) (var 1)) (op (var 0) (op (op (var 1) (var 0)) (var 1)))) , (var 0)) (λ env → holds2660 (env 0) (env 1))
  bad2661 : PathP (λ _ → Two) (bop (bop b0 b1) (bop b0 (bop (bop b1 b0) b1))) b1 → ⊥
  bad2661  p = false≢true (cong lower p)
  cut2661 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 0) (op (op (var 1) (var 0)) (var 1)))) , (var 1)) → ⊥
  cut2661  adequate = bad2661  (Adequate.valid adequate Two boolean env0)
  bad2662 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop (bop b0 b0) b0))) b1 → ⊥
  bad2662  p = false≢true (cong lower p)
  cut2662 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 0) (op (op (var 1) (var 0)) (var 1)))) , (var 2)) → ⊥
  cut2662  adequate = bad2662  (Adequate.valid adequate Two boolean env1)
  bad2663 : PathP (λ _ → Two) (bop (bop b1 b0) (bop b1 (bop (bop b0 b1) b1))) b1 → ⊥
  bad2663  p = false≢true (cong lower p)
  cut2663 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 0) (op (op (var 1) (var 0)) (var 2)))) , (var 0)) → ⊥
  cut2663  adequate = bad2663  (Adequate.valid adequate Two boolean env19)
  bad2664 : PathP (λ _ → Two) (bop (bop b0 b1) (bop b0 (bop (bop b1 b0) b0))) b1 → ⊥
  bad2664  p = false≢true (cong lower p)
  cut2664 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 0) (op (op (var 1) (var 0)) (var 2)))) , (var 1)) → ⊥
  cut2664  adequate = bad2664  (Adequate.valid adequate Two boolean env2)
  bad2665 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop (bop b0 b0) b1))) b1 → ⊥
  bad2665  p = false≢true (cong lower p)
  cut2665 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 0) (op (op (var 1) (var 0)) (var 2)))) , (var 2)) → ⊥
  cut2665  adequate = bad2665  (Adequate.valid adequate Two boolean env1)
  bad2666 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop (bop b0 b0) b0))) b1 → ⊥
  bad2666  p = false≢true (cong lower p)
  cut2666 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 0) (op (op (var 1) (var 0)) (var 2)))) , (var 3)) → ⊥
  cut2666  adequate = bad2666  (Adequate.valid adequate Two boolean env3)
  bad2667 : PathP (λ _ → Two) (bop (bop b1 b0) (bop b1 (bop (bop b0 b0) b1))) b1 → ⊥
  bad2667  p = false≢true (cong lower p)
  cut2667 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 0) (op (op (var 1) (var 1)) (var 0)))) , (var 0)) → ⊥
  cut2667  adequate = bad2667  (Adequate.valid adequate Two boolean env7)
  bad2668 : PathP (λ _ → Two) (bop (bop b0 b1) (bop b0 (bop (bop b1 b1) b0))) b1 → ⊥
  bad2668  p = false≢true (cong lower p)
  cut2668 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 0) (op (op (var 1) (var 1)) (var 0)))) , (var 1)) → ⊥
  cut2668  adequate = bad2668  (Adequate.valid adequate Two boolean env0)
  bad2669 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop (bop b0 b0) b0))) b1 → ⊥
  bad2669  p = false≢true (cong lower p)
  cut2669 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 0) (op (op (var 1) (var 1)) (var 0)))) , (var 2)) → ⊥
  cut2669  adequate = bad2669  (Adequate.valid adequate Two boolean env1)
  holds2670 : (z0 z1 : A2) → (mul2 (mul2 z0 z1) (mul2 z0 (mul2 (mul2 z1 z1) z1))) ≡ z0
  holds2670 z0 z1 = refl
  cut2670 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 0) (op (op (var 1) (var 1)) (var 1)))) , (var 0)) → ⊥
  cut2670  = reject2 ((op (op (var 0) (var 1)) (op (var 0) (op (op (var 1) (var 1)) (var 1)))) , (var 0)) (λ env → holds2670 (env 0) (env 1))
  bad2671 : PathP (λ _ → Two) (bop (bop b0 b1) (bop b0 (bop (bop b1 b1) b1))) b1 → ⊥
  bad2671  p = false≢true (cong lower p)
  cut2671 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 0) (op (op (var 1) (var 1)) (var 1)))) , (var 1)) → ⊥
  cut2671  adequate = bad2671  (Adequate.valid adequate Two boolean env0)
  bad2672 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop (bop b0 b0) b0))) b1 → ⊥
  bad2672  p = false≢true (cong lower p)
  cut2672 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 0) (op (op (var 1) (var 1)) (var 1)))) , (var 2)) → ⊥
  cut2672  adequate = bad2672  (Adequate.valid adequate Two boolean env1)
  bad2673 : PathP (λ _ → Two) (bop (bop b1 b0) (bop b1 (bop (bop b0 b0) b1))) b1 → ⊥
  bad2673  p = false≢true (cong lower p)
  cut2673 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 0) (op (op (var 1) (var 1)) (var 2)))) , (var 0)) → ⊥
  cut2673  adequate = bad2673  (Adequate.valid adequate Two boolean env19)
  bad2674 : PathP (λ _ → Two) (bop (bop b0 b1) (bop b0 (bop (bop b1 b1) b0))) b1 → ⊥
  bad2674  p = false≢true (cong lower p)
  cut2674 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 0) (op (op (var 1) (var 1)) (var 2)))) , (var 1)) → ⊥
  cut2674  adequate = bad2674  (Adequate.valid adequate Two boolean env2)
  bad2675 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop (bop b0 b0) b1))) b1 → ⊥
  bad2675  p = false≢true (cong lower p)
  cut2675 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 0) (op (op (var 1) (var 1)) (var 2)))) , (var 2)) → ⊥
  cut2675  adequate = bad2675  (Adequate.valid adequate Two boolean env1)
  bad2676 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop (bop b0 b0) b0))) b1 → ⊥
  bad2676  p = false≢true (cong lower p)
  cut2676 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 0) (op (op (var 1) (var 1)) (var 2)))) , (var 3)) → ⊥
  cut2676  adequate = bad2676  (Adequate.valid adequate Two boolean env3)
  bad2677 : PathP (λ _ → Two) (bop (bop b1 b0) (bop b1 (bop (bop b0 b0) b1))) b1 → ⊥
  bad2677  p = false≢true (cong lower p)
  cut2677 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 0) (op (op (var 1) (var 2)) (var 0)))) , (var 0)) → ⊥
  cut2677  adequate = bad2677  (Adequate.valid adequate Two boolean env9)
  bad2678 : PathP (λ _ → Two) (bop (bop b0 b1) (bop b0 (bop (bop b1 b0) b0))) b1 → ⊥
  bad2678  p = false≢true (cong lower p)
  cut2678 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 0) (op (op (var 1) (var 2)) (var 0)))) , (var 1)) → ⊥
  cut2678  adequate = bad2678  (Adequate.valid adequate Two boolean env2)
  bad2679 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop (bop b0 b1) b0))) b1 → ⊥
  bad2679  p = false≢true (cong lower p)
  cut2679 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 0) (op (op (var 1) (var 2)) (var 0)))) , (var 2)) → ⊥
  cut2679  adequate = bad2679  (Adequate.valid adequate Two boolean env1)
  bad2680 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop (bop b0 b0) b0))) b1 → ⊥
  bad2680  p = false≢true (cong lower p)
  cut2680 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 0) (op (op (var 1) (var 2)) (var 0)))) , (var 3)) → ⊥
  cut2680  adequate = bad2680  (Adequate.valid adequate Two boolean env3)
  holds2681 : (z0 z1 z2 : A2) → (mul2 (mul2 z0 z1) (mul2 z0 (mul2 (mul2 z1 z2) z1))) ≡ z0
  holds2681 z0 z1 z2 = refl
  cut2681 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 0) (op (op (var 1) (var 2)) (var 1)))) , (var 0)) → ⊥
  cut2681  = reject2 ((op (op (var 0) (var 1)) (op (var 0) (op (op (var 1) (var 2)) (var 1)))) , (var 0)) (λ env → holds2681 (env 0) (env 1) (env 2))
  bad2682 : PathP (λ _ → Two) (bop (bop b0 b1) (bop b0 (bop (bop b1 b0) b1))) b1 → ⊥
  bad2682  p = false≢true (cong lower p)
  cut2682 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 0) (op (op (var 1) (var 2)) (var 1)))) , (var 1)) → ⊥
  cut2682  adequate = bad2682  (Adequate.valid adequate Two boolean env2)
  bad2683 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop (bop b0 b1) b0))) b1 → ⊥
  bad2683  p = false≢true (cong lower p)
  cut2683 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 0) (op (op (var 1) (var 2)) (var 1)))) , (var 2)) → ⊥
  cut2683  adequate = bad2683  (Adequate.valid adequate Two boolean env1)
  bad2684 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop (bop b0 b0) b0))) b1 → ⊥
  bad2684  p = false≢true (cong lower p)
  cut2684 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 0) (op (op (var 1) (var 2)) (var 1)))) , (var 3)) → ⊥
  cut2684  adequate = bad2684  (Adequate.valid adequate Two boolean env3)
  bad2685 : PathP (λ _ → Two) (bop (bop b1 b0) (bop b1 (bop (bop b0 b1) b1))) b1 → ⊥
  bad2685  p = false≢true (cong lower p)
  cut2685 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 0) (op (op (var 1) (var 2)) (var 2)))) , (var 0)) → ⊥
  cut2685  adequate = bad2685  (Adequate.valid adequate Two boolean env19)
  bad2686 : PathP (λ _ → Two) (bop (bop b0 b1) (bop b0 (bop (bop b1 b0) b0))) b1 → ⊥
  bad2686  p = false≢true (cong lower p)
  cut2686 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 0) (op (op (var 1) (var 2)) (var 2)))) , (var 1)) → ⊥
  cut2686  adequate = bad2686  (Adequate.valid adequate Two boolean env2)
  bad2687 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop (bop b0 b1) b1))) b1 → ⊥
  bad2687  p = false≢true (cong lower p)
  cut2687 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 0) (op (op (var 1) (var 2)) (var 2)))) , (var 2)) → ⊥
  cut2687  adequate = bad2687  (Adequate.valid adequate Two boolean env1)
  bad2688 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop (bop b0 b0) b0))) b1 → ⊥
  bad2688  p = false≢true (cong lower p)
  cut2688 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 0) (op (op (var 1) (var 2)) (var 2)))) , (var 3)) → ⊥
  cut2688  adequate = bad2688  (Adequate.valid adequate Two boolean env3)
  bad2689 : PathP (λ _ → Two) (bop (bop b1 b0) (bop b1 (bop (bop b0 b0) b1))) b1 → ⊥
  bad2689  p = false≢true (cong lower p)
  cut2689 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 0) (op (op (var 1) (var 2)) (var 3)))) , (var 0)) → ⊥
  cut2689  adequate = bad2689  (Adequate.valid adequate Two boolean env20)
  bad2690 : PathP (λ _ → Two) (bop (bop b0 b1) (bop b0 (bop (bop b1 b0) b0))) b1 → ⊥
  bad2690  p = false≢true (cong lower p)
  cut2690 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 0) (op (op (var 1) (var 2)) (var 3)))) , (var 1)) → ⊥
  cut2690  adequate = bad2690  (Adequate.valid adequate Two boolean env4)
  bad2691 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop (bop b0 b1) b0))) b1 → ⊥
  bad2691  p = false≢true (cong lower p)
  cut2691 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 0) (op (op (var 1) (var 2)) (var 3)))) , (var 2)) → ⊥
  cut2691  adequate = bad2691  (Adequate.valid adequate Two boolean env5)
  bad2692 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop (bop b0 b0) b1))) b1 → ⊥
  bad2692  p = false≢true (cong lower p)
  cut2692 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 0) (op (op (var 1) (var 2)) (var 3)))) , (var 3)) → ⊥
  cut2692  adequate = bad2692  (Adequate.valid adequate Two boolean env3)
  bad2693 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop (bop b0 b0) b0))) b1 → ⊥
  bad2693  p = false≢true (cong lower p)
  cut2693 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 0) (op (op (var 1) (var 2)) (var 3)))) , (var 4)) → ⊥
  cut2693  adequate = bad2693  (Adequate.valid adequate Two boolean env6)
  bad2694 : PathP (λ _ → Two) (bop (bop b1 b0) (bop b1 (bop (bop b0 b1) b1))) b1 → ⊥
  bad2694  p = false≢true (cong lower p)
  cut2694 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 0) (op (op (var 2) (var 0)) (var 0)))) , (var 0)) → ⊥
  cut2694  adequate = bad2694  (Adequate.valid adequate Two boolean env9)
  bad2695 : PathP (λ _ → Two) (bop (bop b0 b1) (bop b0 (bop (bop b0 b0) b0))) b1 → ⊥
  bad2695  p = false≢true (cong lower p)
  cut2695 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 0) (op (op (var 2) (var 0)) (var 0)))) , (var 1)) → ⊥
  cut2695  adequate = bad2695  (Adequate.valid adequate Two boolean env2)
  bad2696 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop (bop b1 b0) b0))) b1 → ⊥
  bad2696  p = false≢true (cong lower p)
  cut2696 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 0) (op (op (var 2) (var 0)) (var 0)))) , (var 2)) → ⊥
  cut2696  adequate = bad2696  (Adequate.valid adequate Two boolean env1)
  bad2697 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop (bop b0 b0) b0))) b1 → ⊥
  bad2697  p = false≢true (cong lower p)
  cut2697 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 0) (op (op (var 2) (var 0)) (var 0)))) , (var 3)) → ⊥
  cut2697  adequate = bad2697  (Adequate.valid adequate Two boolean env3)
  holds2698 : (z0 z1 z2 : A2) → (mul2 (mul2 z0 z1) (mul2 z0 (mul2 (mul2 z2 z0) z1))) ≡ z0
  holds2698 z0 z1 z2 = refl
  cut2698 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 0) (op (op (var 2) (var 0)) (var 1)))) , (var 0)) → ⊥
  cut2698  = reject2 ((op (op (var 0) (var 1)) (op (var 0) (op (op (var 2) (var 0)) (var 1)))) , (var 0)) (λ env → holds2698 (env 0) (env 1) (env 2))
  bad2699 : PathP (λ _ → Two) (bop (bop b0 b1) (bop b0 (bop (bop b0 b0) b1))) b1 → ⊥
  bad2699  p = false≢true (cong lower p)
  cut2699 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 0) (op (op (var 2) (var 0)) (var 1)))) , (var 1)) → ⊥
  cut2699  adequate = bad2699  (Adequate.valid adequate Two boolean env2)
  bad2700 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop (bop b1 b0) b0))) b1 → ⊥
  bad2700  p = false≢true (cong lower p)
  cut2700 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 0) (op (op (var 2) (var 0)) (var 1)))) , (var 2)) → ⊥
  cut2700  adequate = bad2700  (Adequate.valid adequate Two boolean env1)
  bad2701 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop (bop b0 b0) b0))) b1 → ⊥
  bad2701  p = false≢true (cong lower p)
  cut2701 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 0) (op (op (var 2) (var 0)) (var 1)))) , (var 3)) → ⊥
  cut2701  adequate = bad2701  (Adequate.valid adequate Two boolean env3)
  holds2702 : (z0 z1 z2 : A2) → (mul2 (mul2 z0 z1) (mul2 z0 (mul2 (mul2 z2 z0) z2))) ≡ z0
  holds2702 z0 z1 z2 = refl
  cut2702 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 0) (op (op (var 2) (var 0)) (var 2)))) , (var 0)) → ⊥
  cut2702  = reject2 ((op (op (var 0) (var 1)) (op (var 0) (op (op (var 2) (var 0)) (var 2)))) , (var 0)) (λ env → holds2702 (env 0) (env 1) (env 2))
  bad2703 : PathP (λ _ → Two) (bop (bop b0 b1) (bop b0 (bop (bop b0 b0) b0))) b1 → ⊥
  bad2703  p = false≢true (cong lower p)
  cut2703 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 0) (op (op (var 2) (var 0)) (var 2)))) , (var 1)) → ⊥
  cut2703  adequate = bad2703  (Adequate.valid adequate Two boolean env2)
  bad2704 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop (bop b1 b0) b1))) b1 → ⊥
  bad2704  p = false≢true (cong lower p)
  cut2704 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 0) (op (op (var 2) (var 0)) (var 2)))) , (var 2)) → ⊥
  cut2704  adequate = bad2704  (Adequate.valid adequate Two boolean env1)
  bad2705 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop (bop b0 b0) b0))) b1 → ⊥
  bad2705  p = false≢true (cong lower p)
  cut2705 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 0) (op (op (var 2) (var 0)) (var 2)))) , (var 3)) → ⊥
  cut2705  adequate = bad2705  (Adequate.valid adequate Two boolean env3)
  bad2706 : PathP (λ _ → Two) (bop (bop b1 b0) (bop b1 (bop (bop b0 b1) b1))) b1 → ⊥
  bad2706  p = false≢true (cong lower p)
  cut2706 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 0) (op (op (var 2) (var 0)) (var 3)))) , (var 0)) → ⊥
  cut2706  adequate = bad2706  (Adequate.valid adequate Two boolean env20)
  bad2707 : PathP (λ _ → Two) (bop (bop b0 b1) (bop b0 (bop (bop b0 b0) b0))) b1 → ⊥
  bad2707  p = false≢true (cong lower p)
  cut2707 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 0) (op (op (var 2) (var 0)) (var 3)))) , (var 1)) → ⊥
  cut2707  adequate = bad2707  (Adequate.valid adequate Two boolean env4)
  bad2708 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop (bop b1 b0) b0))) b1 → ⊥
  bad2708  p = false≢true (cong lower p)
  cut2708 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 0) (op (op (var 2) (var 0)) (var 3)))) , (var 2)) → ⊥
  cut2708  adequate = bad2708  (Adequate.valid adequate Two boolean env5)
  bad2709 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop (bop b0 b0) b1))) b1 → ⊥
  bad2709  p = false≢true (cong lower p)
  cut2709 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 0) (op (op (var 2) (var 0)) (var 3)))) , (var 3)) → ⊥
  cut2709  adequate = bad2709  (Adequate.valid adequate Two boolean env3)
  bad2710 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop (bop b0 b0) b0))) b1 → ⊥
  bad2710  p = false≢true (cong lower p)
  cut2710 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 0) (op (op (var 2) (var 0)) (var 3)))) , (var 4)) → ⊥
  cut2710  adequate = bad2710  (Adequate.valid adequate Two boolean env6)
  bad2711 : PathP (λ _ → Two) (bop (bop b1 b0) (bop b1 (bop (bop b0 b0) b1))) b1 → ⊥
  bad2711  p = false≢true (cong lower p)
  cut2711 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 0) (op (op (var 2) (var 1)) (var 0)))) , (var 0)) → ⊥
  cut2711  adequate = bad2711  (Adequate.valid adequate Two boolean env9)
  bad2712 : PathP (λ _ → Two) (bop (bop b0 b1) (bop b0 (bop (bop b0 b1) b0))) b1 → ⊥
  bad2712  p = false≢true (cong lower p)
  cut2712 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 0) (op (op (var 2) (var 1)) (var 0)))) , (var 1)) → ⊥
  cut2712  adequate = bad2712  (Adequate.valid adequate Two boolean env2)
  bad2713 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop (bop b1 b0) b0))) b1 → ⊥
  bad2713  p = false≢true (cong lower p)
  cut2713 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 0) (op (op (var 2) (var 1)) (var 0)))) , (var 2)) → ⊥
  cut2713  adequate = bad2713  (Adequate.valid adequate Two boolean env1)
  bad2714 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop (bop b0 b0) b0))) b1 → ⊥
  bad2714  p = false≢true (cong lower p)
  cut2714 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 0) (op (op (var 2) (var 1)) (var 0)))) , (var 3)) → ⊥
  cut2714  adequate = bad2714  (Adequate.valid adequate Two boolean env3)
  holds2715 : (z0 z1 z2 : A2) → (mul2 (mul2 z0 z1) (mul2 z0 (mul2 (mul2 z2 z1) z1))) ≡ z0
  holds2715 z0 z1 z2 = refl
  cut2715 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 0) (op (op (var 2) (var 1)) (var 1)))) , (var 0)) → ⊥
  cut2715  = reject2 ((op (op (var 0) (var 1)) (op (var 0) (op (op (var 2) (var 1)) (var 1)))) , (var 0)) (λ env → holds2715 (env 0) (env 1) (env 2))
  bad2716 : PathP (λ _ → Two) (bop (bop b0 b1) (bop b0 (bop (bop b0 b1) b1))) b1 → ⊥
  bad2716  p = false≢true (cong lower p)
  cut2716 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 0) (op (op (var 2) (var 1)) (var 1)))) , (var 1)) → ⊥
  cut2716  adequate = bad2716  (Adequate.valid adequate Two boolean env2)
  bad2717 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop (bop b1 b0) b0))) b1 → ⊥
  bad2717  p = false≢true (cong lower p)
  cut2717 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 0) (op (op (var 2) (var 1)) (var 1)))) , (var 2)) → ⊥
  cut2717  adequate = bad2717  (Adequate.valid adequate Two boolean env1)
  bad2718 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop (bop b0 b0) b0))) b1 → ⊥
  bad2718  p = false≢true (cong lower p)
  cut2718 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 0) (op (op (var 2) (var 1)) (var 1)))) , (var 3)) → ⊥
  cut2718  adequate = bad2718  (Adequate.valid adequate Two boolean env3)
  bad2719 : PathP (λ _ → Two) (bop (bop b1 b0) (bop b1 (bop (bop b1 b0) b1))) b1 → ⊥
  bad2719  p = false≢true (cong lower p)
  cut2719 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 0) (op (op (var 2) (var 1)) (var 2)))) , (var 0)) → ⊥
  cut2719  adequate = bad2719  (Adequate.valid adequate Two boolean env19)
  bad2720 : PathP (λ _ → Two) (bop (bop b0 b1) (bop b0 (bop (bop b0 b1) b0))) b1 → ⊥
  bad2720  p = false≢true (cong lower p)
  cut2720 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 0) (op (op (var 2) (var 1)) (var 2)))) , (var 1)) → ⊥
  cut2720  adequate = bad2720  (Adequate.valid adequate Two boolean env2)
  bad2721 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop (bop b1 b0) b1))) b1 → ⊥
  bad2721  p = false≢true (cong lower p)
  cut2721 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 0) (op (op (var 2) (var 1)) (var 2)))) , (var 2)) → ⊥
  cut2721  adequate = bad2721  (Adequate.valid adequate Two boolean env1)
  bad2722 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop (bop b0 b0) b0))) b1 → ⊥
  bad2722  p = false≢true (cong lower p)
  cut2722 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 0) (op (op (var 2) (var 1)) (var 2)))) , (var 3)) → ⊥
  cut2722  adequate = bad2722  (Adequate.valid adequate Two boolean env3)
  bad2723 : PathP (λ _ → Two) (bop (bop b1 b0) (bop b1 (bop (bop b0 b0) b1))) b1 → ⊥
  bad2723  p = false≢true (cong lower p)
  cut2723 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 0) (op (op (var 2) (var 1)) (var 3)))) , (var 0)) → ⊥
  cut2723  adequate = bad2723  (Adequate.valid adequate Two boolean env20)
  bad2724 : PathP (λ _ → Two) (bop (bop b0 b1) (bop b0 (bop (bop b0 b1) b0))) b1 → ⊥
  bad2724  p = false≢true (cong lower p)
  cut2724 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 0) (op (op (var 2) (var 1)) (var 3)))) , (var 1)) → ⊥
  cut2724  adequate = bad2724  (Adequate.valid adequate Two boolean env4)
  bad2725 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop (bop b1 b0) b0))) b1 → ⊥
  bad2725  p = false≢true (cong lower p)
  cut2725 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 0) (op (op (var 2) (var 1)) (var 3)))) , (var 2)) → ⊥
  cut2725  adequate = bad2725  (Adequate.valid adequate Two boolean env5)
  bad2726 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop (bop b0 b0) b1))) b1 → ⊥
  bad2726  p = false≢true (cong lower p)
  cut2726 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 0) (op (op (var 2) (var 1)) (var 3)))) , (var 3)) → ⊥
  cut2726  adequate = bad2726  (Adequate.valid adequate Two boolean env3)
  bad2727 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop (bop b0 b0) b0))) b1 → ⊥
  bad2727  p = false≢true (cong lower p)
  cut2727 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 0) (op (op (var 2) (var 1)) (var 3)))) , (var 4)) → ⊥
  cut2727  adequate = bad2727  (Adequate.valid adequate Two boolean env6)
  bad2728 : PathP (λ _ → Two) (bop (bop b1 b0) (bop b1 (bop (bop b0 b0) b1))) b1 → ⊥
  bad2728  p = false≢true (cong lower p)
  cut2728 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 0) (op (op (var 2) (var 2)) (var 0)))) , (var 0)) → ⊥
  cut2728  adequate = bad2728  (Adequate.valid adequate Two boolean env9)
  bad2729 : PathP (λ _ → Two) (bop (bop b0 b1) (bop b0 (bop (bop b0 b0) b0))) b1 → ⊥
  bad2729  p = false≢true (cong lower p)
  cut2729 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 0) (op (op (var 2) (var 2)) (var 0)))) , (var 1)) → ⊥
  cut2729  adequate = bad2729  (Adequate.valid adequate Two boolean env2)
  bad2730 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop (bop b1 b1) b0))) b1 → ⊥
  bad2730  p = false≢true (cong lower p)
  cut2730 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 0) (op (op (var 2) (var 2)) (var 0)))) , (var 2)) → ⊥
  cut2730  adequate = bad2730  (Adequate.valid adequate Two boolean env1)
  bad2731 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop (bop b0 b0) b0))) b1 → ⊥
  bad2731  p = false≢true (cong lower p)
  cut2731 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 0) (op (op (var 2) (var 2)) (var 0)))) , (var 3)) → ⊥
  cut2731  adequate = bad2731  (Adequate.valid adequate Two boolean env3)
  holds2732 : (z0 z1 z2 : A2) → (mul2 (mul2 z0 z1) (mul2 z0 (mul2 (mul2 z2 z2) z1))) ≡ z0
  holds2732 z0 z1 z2 = refl
  cut2732 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 0) (op (op (var 2) (var 2)) (var 1)))) , (var 0)) → ⊥
  cut2732  = reject2 ((op (op (var 0) (var 1)) (op (var 0) (op (op (var 2) (var 2)) (var 1)))) , (var 0)) (λ env → holds2732 (env 0) (env 1) (env 2))
  bad2733 : PathP (λ _ → Two) (bop (bop b0 b1) (bop b0 (bop (bop b0 b0) b1))) b1 → ⊥
  bad2733  p = false≢true (cong lower p)
  cut2733 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 0) (op (op (var 2) (var 2)) (var 1)))) , (var 1)) → ⊥
  cut2733  adequate = bad2733  (Adequate.valid adequate Two boolean env2)
  bad2734 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop (bop b1 b1) b0))) b1 → ⊥
  bad2734  p = false≢true (cong lower p)
  cut2734 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 0) (op (op (var 2) (var 2)) (var 1)))) , (var 2)) → ⊥
  cut2734  adequate = bad2734  (Adequate.valid adequate Two boolean env1)
  bad2735 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop (bop b0 b0) b0))) b1 → ⊥
  bad2735  p = false≢true (cong lower p)
  cut2735 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 0) (op (op (var 2) (var 2)) (var 1)))) , (var 3)) → ⊥
  cut2735  adequate = bad2735  (Adequate.valid adequate Two boolean env3)
  holds2736 : (z0 z1 z2 : A2) → (mul2 (mul2 z0 z1) (mul2 z0 (mul2 (mul2 z2 z2) z2))) ≡ z0
  holds2736 z0 z1 z2 = refl
  cut2736 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 0) (op (op (var 2) (var 2)) (var 2)))) , (var 0)) → ⊥
  cut2736  = reject2 ((op (op (var 0) (var 1)) (op (var 0) (op (op (var 2) (var 2)) (var 2)))) , (var 0)) (λ env → holds2736 (env 0) (env 1) (env 2))
  bad2737 : PathP (λ _ → Two) (bop (bop b0 b1) (bop b0 (bop (bop b0 b0) b0))) b1 → ⊥
  bad2737  p = false≢true (cong lower p)
  cut2737 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 0) (op (op (var 2) (var 2)) (var 2)))) , (var 1)) → ⊥
  cut2737  adequate = bad2737  (Adequate.valid adequate Two boolean env2)
  bad2738 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop (bop b1 b1) b1))) b1 → ⊥
  bad2738  p = false≢true (cong lower p)
  cut2738 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 0) (op (op (var 2) (var 2)) (var 2)))) , (var 2)) → ⊥
  cut2738  adequate = bad2738  (Adequate.valid adequate Two boolean env1)
  bad2739 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop (bop b0 b0) b0))) b1 → ⊥
  bad2739  p = false≢true (cong lower p)
  cut2739 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 0) (op (op (var 2) (var 2)) (var 2)))) , (var 3)) → ⊥
  cut2739  adequate = bad2739  (Adequate.valid adequate Two boolean env3)
  bad2740 : PathP (λ _ → Two) (bop (bop b1 b0) (bop b1 (bop (bop b0 b0) b1))) b1 → ⊥
  bad2740  p = false≢true (cong lower p)
  cut2740 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 0) (op (op (var 2) (var 2)) (var 3)))) , (var 0)) → ⊥
  cut2740  adequate = bad2740  (Adequate.valid adequate Two boolean env20)
  bad2741 : PathP (λ _ → Two) (bop (bop b0 b1) (bop b0 (bop (bop b0 b0) b0))) b1 → ⊥
  bad2741  p = false≢true (cong lower p)
  cut2741 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 0) (op (op (var 2) (var 2)) (var 3)))) , (var 1)) → ⊥
  cut2741  adequate = bad2741  (Adequate.valid adequate Two boolean env4)
  bad2742 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop (bop b1 b1) b0))) b1 → ⊥
  bad2742  p = false≢true (cong lower p)
  cut2742 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 0) (op (op (var 2) (var 2)) (var 3)))) , (var 2)) → ⊥
  cut2742  adequate = bad2742  (Adequate.valid adequate Two boolean env5)
  bad2743 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop (bop b0 b0) b1))) b1 → ⊥
  bad2743  p = false≢true (cong lower p)
  cut2743 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 0) (op (op (var 2) (var 2)) (var 3)))) , (var 3)) → ⊥
  cut2743  adequate = bad2743  (Adequate.valid adequate Two boolean env3)
  bad2744 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop (bop b0 b0) b0))) b1 → ⊥
  bad2744  p = false≢true (cong lower p)
  cut2744 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 0) (op (op (var 2) (var 2)) (var 3)))) , (var 4)) → ⊥
  cut2744  adequate = bad2744  (Adequate.valid adequate Two boolean env6)
  bad2745 : PathP (λ _ → Two) (bop (bop b1 b0) (bop b1 (bop (bop b0 b0) b1))) b1 → ⊥
  bad2745  p = false≢true (cong lower p)
  cut2745 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 0) (op (op (var 2) (var 3)) (var 0)))) , (var 0)) → ⊥
  cut2745  adequate = bad2745  (Adequate.valid adequate Two boolean env11)
  bad2746 : PathP (λ _ → Two) (bop (bop b0 b1) (bop b0 (bop (bop b0 b0) b0))) b1 → ⊥
  bad2746  p = false≢true (cong lower p)
  cut2746 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 0) (op (op (var 2) (var 3)) (var 0)))) , (var 1)) → ⊥
  cut2746  adequate = bad2746  (Adequate.valid adequate Two boolean env4)
  bad2747 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop (bop b1 b0) b0))) b1 → ⊥
  bad2747  p = false≢true (cong lower p)
  cut2747 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 0) (op (op (var 2) (var 3)) (var 0)))) , (var 2)) → ⊥
  cut2747  adequate = bad2747  (Adequate.valid adequate Two boolean env5)
  bad2748 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop (bop b0 b1) b0))) b1 → ⊥
  bad2748  p = false≢true (cong lower p)
  cut2748 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 0) (op (op (var 2) (var 3)) (var 0)))) , (var 3)) → ⊥
  cut2748  adequate = bad2748  (Adequate.valid adequate Two boolean env3)
  bad2749 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop (bop b0 b0) b0))) b1 → ⊥
  bad2749  p = false≢true (cong lower p)
  cut2749 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 0) (op (op (var 2) (var 3)) (var 0)))) , (var 4)) → ⊥
  cut2749  adequate = bad2749  (Adequate.valid adequate Two boolean env6)
  holds2750 : (z0 z1 z2 z3 : A2) → (mul2 (mul2 z0 z1) (mul2 z0 (mul2 (mul2 z2 z3) z1))) ≡ z0
  holds2750 z0 z1 z2 z3 = refl
  cut2750 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 0) (op (op (var 2) (var 3)) (var 1)))) , (var 0)) → ⊥
  cut2750  = reject2 ((op (op (var 0) (var 1)) (op (var 0) (op (op (var 2) (var 3)) (var 1)))) , (var 0)) (λ env → holds2750 (env 0) (env 1) (env 2) (env 3))
  bad2751 : PathP (λ _ → Two) (bop (bop b0 b1) (bop b0 (bop (bop b0 b0) b1))) b1 → ⊥
  bad2751  p = false≢true (cong lower p)
  cut2751 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 0) (op (op (var 2) (var 3)) (var 1)))) , (var 1)) → ⊥
  cut2751  adequate = bad2751  (Adequate.valid adequate Two boolean env4)
  bad2752 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop (bop b1 b0) b0))) b1 → ⊥
  bad2752  p = false≢true (cong lower p)
  cut2752 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 0) (op (op (var 2) (var 3)) (var 1)))) , (var 2)) → ⊥
  cut2752  adequate = bad2752  (Adequate.valid adequate Two boolean env5)
  bad2753 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop (bop b0 b1) b0))) b1 → ⊥
  bad2753  p = false≢true (cong lower p)
  cut2753 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 0) (op (op (var 2) (var 3)) (var 1)))) , (var 3)) → ⊥
  cut2753  adequate = bad2753  (Adequate.valid adequate Two boolean env3)
  bad2754 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop (bop b0 b0) b0))) b1 → ⊥
  bad2754  p = false≢true (cong lower p)
  cut2754 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 0) (op (op (var 2) (var 3)) (var 1)))) , (var 4)) → ⊥
  cut2754  adequate = bad2754  (Adequate.valid adequate Two boolean env6)
  env21 : ℕ → Two
  env21 zero = b1
  env21 (suc zero) = b0
  env21 (suc (suc zero)) = b1
  env21 (suc (suc (suc zero))) = b0
  env21 (suc (suc (suc (suc rest)))) = b0
  bad2755 : PathP (λ _ → Two) (bop (bop b1 b0) (bop b1 (bop (bop b1 b0) b1))) b1 → ⊥
  bad2755  p = false≢true (cong lower p)
  cut2755 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 0) (op (op (var 2) (var 3)) (var 2)))) , (var 0)) → ⊥
  cut2755  adequate = bad2755  (Adequate.valid adequate Two boolean env21)
  bad2756 : PathP (λ _ → Two) (bop (bop b0 b1) (bop b0 (bop (bop b0 b0) b0))) b1 → ⊥
  bad2756  p = false≢true (cong lower p)
  cut2756 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 0) (op (op (var 2) (var 3)) (var 2)))) , (var 1)) → ⊥
  cut2756  adequate = bad2756  (Adequate.valid adequate Two boolean env4)
  bad2757 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop (bop b1 b0) b1))) b1 → ⊥
  bad2757  p = false≢true (cong lower p)
  cut2757 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 0) (op (op (var 2) (var 3)) (var 2)))) , (var 2)) → ⊥
  cut2757  adequate = bad2757  (Adequate.valid adequate Two boolean env5)
  bad2758 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop (bop b0 b1) b0))) b1 → ⊥
  bad2758  p = false≢true (cong lower p)
  cut2758 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 0) (op (op (var 2) (var 3)) (var 2)))) , (var 3)) → ⊥
  cut2758  adequate = bad2758  (Adequate.valid adequate Two boolean env3)
  bad2759 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop (bop b0 b0) b0))) b1 → ⊥
  bad2759  p = false≢true (cong lower p)
  cut2759 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 0) (op (op (var 2) (var 3)) (var 2)))) , (var 4)) → ⊥
  cut2759  adequate = bad2759  (Adequate.valid adequate Two boolean env6)
  bad2760 : PathP (λ _ → Two) (bop (bop b1 b0) (bop b1 (bop (bop b0 b1) b1))) b1 → ⊥
  bad2760  p = false≢true (cong lower p)
  cut2760 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 0) (op (op (var 2) (var 3)) (var 3)))) , (var 0)) → ⊥
  cut2760  adequate = bad2760  (Adequate.valid adequate Two boolean env20)
  bad2761 : PathP (λ _ → Two) (bop (bop b0 b1) (bop b0 (bop (bop b0 b0) b0))) b1 → ⊥
  bad2761  p = false≢true (cong lower p)
  cut2761 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 0) (op (op (var 2) (var 3)) (var 3)))) , (var 1)) → ⊥
  cut2761  adequate = bad2761  (Adequate.valid adequate Two boolean env4)
  bad2762 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop (bop b1 b0) b0))) b1 → ⊥
  bad2762  p = false≢true (cong lower p)
  cut2762 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 0) (op (op (var 2) (var 3)) (var 3)))) , (var 2)) → ⊥
  cut2762  adequate = bad2762  (Adequate.valid adequate Two boolean env5)
  bad2763 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop (bop b0 b1) b1))) b1 → ⊥
  bad2763  p = false≢true (cong lower p)
  cut2763 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 0) (op (op (var 2) (var 3)) (var 3)))) , (var 3)) → ⊥
  cut2763  adequate = bad2763  (Adequate.valid adequate Two boolean env3)
  bad2764 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop (bop b0 b0) b0))) b1 → ⊥
  bad2764  p = false≢true (cong lower p)
  cut2764 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 0) (op (op (var 2) (var 3)) (var 3)))) , (var 4)) → ⊥
  cut2764  adequate = bad2764  (Adequate.valid adequate Two boolean env6)
  env22 : ℕ → Two
  env22 zero = b1
  env22 (suc zero) = b0
  env22 (suc (suc zero)) = b0
  env22 (suc (suc (suc zero))) = b0
  env22 (suc (suc (suc (suc zero)))) = b1
  env22 (suc (suc (suc (suc (suc rest))))) = b0
  bad2765 : PathP (λ _ → Two) (bop (bop b1 b0) (bop b1 (bop (bop b0 b0) b1))) b1 → ⊥
  bad2765  p = false≢true (cong lower p)
  cut2765 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 0) (op (op (var 2) (var 3)) (var 4)))) , (var 0)) → ⊥
  cut2765  adequate = bad2765  (Adequate.valid adequate Two boolean env22)
  bad2766 : PathP (λ _ → Two) (bop (bop b0 b1) (bop b0 (bop (bop b0 b0) b0))) b1 → ⊥
  bad2766  p = false≢true (cong lower p)
  cut2766 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 0) (op (op (var 2) (var 3)) (var 4)))) , (var 1)) → ⊥
  cut2766  adequate = bad2766  (Adequate.valid adequate Two boolean env14)
  bad2767 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop (bop b1 b0) b0))) b1 → ⊥
  bad2767  p = false≢true (cong lower p)
  cut2767 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 0) (op (op (var 2) (var 3)) (var 4)))) , (var 2)) → ⊥
  cut2767  adequate = bad2767  (Adequate.valid adequate Two boolean env16)
  bad2768 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop (bop b0 b1) b0))) b1 → ⊥
  bad2768  p = false≢true (cong lower p)
  cut2768 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 0) (op (op (var 2) (var 3)) (var 4)))) , (var 3)) → ⊥
  cut2768  adequate = bad2768  (Adequate.valid adequate Two boolean env17)
  bad2769 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop (bop b0 b0) b1))) b1 → ⊥
  bad2769  p = false≢true (cong lower p)
  cut2769 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 0) (op (op (var 2) (var 3)) (var 4)))) , (var 4)) → ⊥
  cut2769  adequate = bad2769  (Adequate.valid adequate Two boolean env6)
  bad2770 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop (bop b0 b0) b0))) b1 → ⊥
  bad2770  p = false≢true (cong lower p)
  cut2770 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 0) (op (op (var 2) (var 3)) (var 4)))) , (var 5)) → ⊥
  cut2770  adequate = bad2770  (Adequate.valid adequate Two boolean env18)
  bad2771 : PathP (λ _ → Two) (bop (bop b0 b1) (bop b1 (bop (bop b0 b0) b0))) b0 → ⊥
  bad2771  p = false≢true (sym (cong lower p))
  cut2771 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 1) (op (op (var 0) (var 0)) (var 0)))) , (var 0)) → ⊥
  cut2771  adequate = bad2771  (Adequate.valid adequate Two boolean env0)
  holds2772 : (z0 z1 : A6) → (mul6 (mul6 z0 z1) (mul6 z1 (mul6 (mul6 z0 z0) z0))) ≡ z1
  holds2772 m6c0 m6c0 = refl
  holds2772 m6c0 m6c1 = refl
  holds2772 m6c0 m6c2 = refl
  holds2772 m6c1 m6c0 = refl
  holds2772 m6c1 m6c1 = refl
  holds2772 m6c1 m6c2 = refl
  holds2772 m6c2 m6c0 = refl
  holds2772 m6c2 m6c1 = refl
  holds2772 m6c2 m6c2 = refl
  cut2772 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 1) (op (op (var 0) (var 0)) (var 0)))) , (var 1)) → ⊥
  cut2772  = reject6 ((op (op (var 0) (var 1)) (op (var 1) (op (op (var 0) (var 0)) (var 0)))) , (var 1)) (λ env → holds2772 (env 0) (env 1))
  bad2773 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop (bop b0 b0) b0))) b1 → ⊥
  bad2773  p = false≢true (cong lower p)
  cut2773 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 1) (op (op (var 0) (var 0)) (var 0)))) , (var 2)) → ⊥
  cut2773  adequate = bad2773  (Adequate.valid adequate Two boolean env1)
  bad2774 : PathP (λ _ → Two) (bop (bop b1 b0) (bop b0 (bop (bop b1 b1) b0))) b1 → ⊥
  bad2774  p = false≢true (cong lower p)
  cut2774 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 1) (op (op (var 0) (var 0)) (var 1)))) , (var 0)) → ⊥
  cut2774  adequate = bad2774  (Adequate.valid adequate Two boolean env7)
  bad2775 : PathP (λ _ → Two) (bop (bop b0 b1) (bop b1 (bop (bop b0 b0) b1))) b1 → ⊥
  bad2775  p = false≢true (cong lower p)
  cut2775 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 1) (op (op (var 0) (var 0)) (var 1)))) , (var 1)) → ⊥
  cut2775  adequate = bad2775  (Adequate.valid adequate Two boolean env0)
  bad2776 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop (bop b0 b0) b0))) b1 → ⊥
  bad2776  p = false≢true (cong lower p)
  cut2776 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 1) (op (op (var 0) (var 0)) (var 1)))) , (var 2)) → ⊥
  cut2776  adequate = bad2776  (Adequate.valid adequate Two boolean env1)
  bad2777 : PathP (λ _ → Two) (bop (bop b0 b1) (bop b1 (bop (bop b0 b0) b0))) b0 → ⊥
  bad2777  p = false≢true (sym (cong lower p))
  cut2777 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 1) (op (op (var 0) (var 0)) (var 2)))) , (var 0)) → ⊥
  cut2777  adequate = bad2777  (Adequate.valid adequate Two boolean env2)
  bad2778 : PathP (λ _ → Two) (bop (bop b0 b1) (bop b1 (bop (bop b0 b0) b1))) b1 → ⊥
  bad2778  p = false≢true (cong lower p)
  cut2778 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 1) (op (op (var 0) (var 0)) (var 2)))) , (var 1)) → ⊥
  cut2778  adequate = bad2778  (Adequate.valid adequate Two boolean env8)
  bad2779 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop (bop b0 b0) b1))) b1 → ⊥
  bad2779  p = false≢true (cong lower p)
  cut2779 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 1) (op (op (var 0) (var 0)) (var 2)))) , (var 2)) → ⊥
  cut2779  adequate = bad2779  (Adequate.valid adequate Two boolean env1)
  bad2780 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop (bop b0 b0) b0))) b1 → ⊥
  bad2780  p = false≢true (cong lower p)
  cut2780 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 1) (op (op (var 0) (var 0)) (var 2)))) , (var 3)) → ⊥
  cut2780  adequate = bad2780  (Adequate.valid adequate Two boolean env3)
  bad2781 : PathP (λ _ → Two) (bop (bop b0 b1) (bop b1 (bop (bop b0 b1) b0))) b0 → ⊥
  bad2781  p = false≢true (sym (cong lower p))
  cut2781 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 1) (op (op (var 0) (var 1)) (var 0)))) , (var 0)) → ⊥
  cut2781  adequate = bad2781  (Adequate.valid adequate Two boolean env0)
  holds2782 : (z0 z1 : A6) → (mul6 (mul6 z0 z1) (mul6 z1 (mul6 (mul6 z0 z1) z0))) ≡ z1
  holds2782 m6c0 m6c0 = refl
  holds2782 m6c0 m6c1 = refl
  holds2782 m6c0 m6c2 = refl
  holds2782 m6c1 m6c0 = refl
  holds2782 m6c1 m6c1 = refl
  holds2782 m6c1 m6c2 = refl
  holds2782 m6c2 m6c0 = refl
  holds2782 m6c2 m6c1 = refl
  holds2782 m6c2 m6c2 = refl
  cut2782 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 1) (op (op (var 0) (var 1)) (var 0)))) , (var 1)) → ⊥
  cut2782  = reject6 ((op (op (var 0) (var 1)) (op (var 1) (op (op (var 0) (var 1)) (var 0)))) , (var 1)) (λ env → holds2782 (env 0) (env 1))
  bad2783 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop (bop b0 b0) b0))) b1 → ⊥
  bad2783  p = false≢true (cong lower p)
  cut2783 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 1) (op (op (var 0) (var 1)) (var 0)))) , (var 2)) → ⊥
  cut2783  adequate = bad2783  (Adequate.valid adequate Two boolean env1)
  bad2784 : PathP (λ _ → Two) (bop (bop b1 b0) (bop b0 (bop (bop b1 b0) b0))) b1 → ⊥
  bad2784  p = false≢true (cong lower p)
  cut2784 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 1) (op (op (var 0) (var 1)) (var 1)))) , (var 0)) → ⊥
  cut2784  adequate = bad2784  (Adequate.valid adequate Two boolean env7)
  bad2785 : PathP (λ _ → Two) (bop (bop b0 b1) (bop b1 (bop (bop b0 b1) b1))) b1 → ⊥
  bad2785  p = false≢true (cong lower p)
  cut2785 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 1) (op (op (var 0) (var 1)) (var 1)))) , (var 1)) → ⊥
  cut2785  adequate = bad2785  (Adequate.valid adequate Two boolean env0)
  bad2786 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop (bop b0 b0) b0))) b1 → ⊥
  bad2786  p = false≢true (cong lower p)
  cut2786 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 1) (op (op (var 0) (var 1)) (var 1)))) , (var 2)) → ⊥
  cut2786  adequate = bad2786  (Adequate.valid adequate Two boolean env1)
  bad2787 : PathP (λ _ → Two) (bop (bop b0 b1) (bop b1 (bop (bop b0 b1) b0))) b0 → ⊥
  bad2787  p = false≢true (sym (cong lower p))
  cut2787 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 1) (op (op (var 0) (var 1)) (var 2)))) , (var 0)) → ⊥
  cut2787  adequate = bad2787  (Adequate.valid adequate Two boolean env2)
  bad2788 : PathP (λ _ → Two) (bop (bop b0 b1) (bop b1 (bop (bop b0 b1) b1))) b1 → ⊥
  bad2788  p = false≢true (cong lower p)
  cut2788 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 1) (op (op (var 0) (var 1)) (var 2)))) , (var 1)) → ⊥
  cut2788  adequate = bad2788  (Adequate.valid adequate Two boolean env8)
  bad2789 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop (bop b0 b0) b1))) b1 → ⊥
  bad2789  p = false≢true (cong lower p)
  cut2789 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 1) (op (op (var 0) (var 1)) (var 2)))) , (var 2)) → ⊥
  cut2789  adequate = bad2789  (Adequate.valid adequate Two boolean env1)
  bad2790 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop (bop b0 b0) b0))) b1 → ⊥
  bad2790  p = false≢true (cong lower p)
  cut2790 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 1) (op (op (var 0) (var 1)) (var 2)))) , (var 3)) → ⊥
  cut2790  adequate = bad2790  (Adequate.valid adequate Two boolean env3)
  bad2791 : PathP (λ _ → Two) (bop (bop b0 b1) (bop b1 (bop (bop b0 b0) b0))) b0 → ⊥
  bad2791  p = false≢true (sym (cong lower p))
  cut2791 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 1) (op (op (var 0) (var 2)) (var 0)))) , (var 0)) → ⊥
  cut2791  adequate = bad2791  (Adequate.valid adequate Two boolean env2)
  holds2792 : (z0 z1 z2 : A13) → (mul13 (mul13 z0 z1) (mul13 z1 (mul13 (mul13 z0 z2) z0))) ≡ z1
  holds2792 m13c0 m13c0 m13c0 = refl
  holds2792 m13c0 m13c0 m13c1 = refl
  holds2792 m13c0 m13c0 m13c2 = refl
  holds2792 m13c0 m13c0 m13c3 = refl
  holds2792 m13c0 m13c1 m13c0 = refl
  holds2792 m13c0 m13c1 m13c1 = refl
  holds2792 m13c0 m13c1 m13c2 = refl
  holds2792 m13c0 m13c1 m13c3 = refl
  holds2792 m13c0 m13c2 m13c0 = refl
  holds2792 m13c0 m13c2 m13c1 = refl
  holds2792 m13c0 m13c2 m13c2 = refl
  holds2792 m13c0 m13c2 m13c3 = refl
  holds2792 m13c0 m13c3 m13c0 = refl
  holds2792 m13c0 m13c3 m13c1 = refl
  holds2792 m13c0 m13c3 m13c2 = refl
  holds2792 m13c0 m13c3 m13c3 = refl
  holds2792 m13c1 m13c0 m13c0 = refl
  holds2792 m13c1 m13c0 m13c1 = refl
  holds2792 m13c1 m13c0 m13c2 = refl
  holds2792 m13c1 m13c0 m13c3 = refl
  holds2792 m13c1 m13c1 m13c0 = refl
  holds2792 m13c1 m13c1 m13c1 = refl
  holds2792 m13c1 m13c1 m13c2 = refl
  holds2792 m13c1 m13c1 m13c3 = refl
  holds2792 m13c1 m13c2 m13c0 = refl
  holds2792 m13c1 m13c2 m13c1 = refl
  holds2792 m13c1 m13c2 m13c2 = refl
  holds2792 m13c1 m13c2 m13c3 = refl
  holds2792 m13c1 m13c3 m13c0 = refl
  holds2792 m13c1 m13c3 m13c1 = refl
  holds2792 m13c1 m13c3 m13c2 = refl
  holds2792 m13c1 m13c3 m13c3 = refl
  holds2792 m13c2 m13c0 m13c0 = refl
  holds2792 m13c2 m13c0 m13c1 = refl
  holds2792 m13c2 m13c0 m13c2 = refl
  holds2792 m13c2 m13c0 m13c3 = refl
  holds2792 m13c2 m13c1 m13c0 = refl
  holds2792 m13c2 m13c1 m13c1 = refl
  holds2792 m13c2 m13c1 m13c2 = refl
  holds2792 m13c2 m13c1 m13c3 = refl
  holds2792 m13c2 m13c2 m13c0 = refl
  holds2792 m13c2 m13c2 m13c1 = refl
  holds2792 m13c2 m13c2 m13c2 = refl
  holds2792 m13c2 m13c2 m13c3 = refl
  holds2792 m13c2 m13c3 m13c0 = refl
  holds2792 m13c2 m13c3 m13c1 = refl
  holds2792 m13c2 m13c3 m13c2 = refl
  holds2792 m13c2 m13c3 m13c3 = refl
  holds2792 m13c3 m13c0 m13c0 = refl
  holds2792 m13c3 m13c0 m13c1 = refl
  holds2792 m13c3 m13c0 m13c2 = refl
  holds2792 m13c3 m13c0 m13c3 = refl
  holds2792 m13c3 m13c1 m13c0 = refl
  holds2792 m13c3 m13c1 m13c1 = refl
  holds2792 m13c3 m13c1 m13c2 = refl
  holds2792 m13c3 m13c1 m13c3 = refl
  holds2792 m13c3 m13c2 m13c0 = refl
  holds2792 m13c3 m13c2 m13c1 = refl
  holds2792 m13c3 m13c2 m13c2 = refl
  holds2792 m13c3 m13c2 m13c3 = refl
  holds2792 m13c3 m13c3 m13c0 = refl
  holds2792 m13c3 m13c3 m13c1 = refl
  holds2792 m13c3 m13c3 m13c2 = refl
  holds2792 m13c3 m13c3 m13c3 = refl
  cut2792 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 1) (op (op (var 0) (var 2)) (var 0)))) , (var 1)) → ⊥
  cut2792  = reject13 ((op (op (var 0) (var 1)) (op (var 1) (op (op (var 0) (var 2)) (var 0)))) , (var 1)) (λ env → holds2792 (env 0) (env 1) (env 2))
  bad2793 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop (bop b0 b1) b0))) b1 → ⊥
  bad2793  p = false≢true (cong lower p)
  cut2793 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 1) (op (op (var 0) (var 2)) (var 0)))) , (var 2)) → ⊥
  cut2793  adequate = bad2793  (Adequate.valid adequate Two boolean env1)
  bad2794 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop (bop b0 b0) b0))) b1 → ⊥
  bad2794  p = false≢true (cong lower p)
  cut2794 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 1) (op (op (var 0) (var 2)) (var 0)))) , (var 3)) → ⊥
  cut2794  adequate = bad2794  (Adequate.valid adequate Two boolean env3)
  bad2795 : PathP (λ _ → Two) (bop (bop b1 b0) (bop b0 (bop (bop b1 b0) b0))) b1 → ⊥
  bad2795  p = false≢true (cong lower p)
  cut2795 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 1) (op (op (var 0) (var 2)) (var 1)))) , (var 0)) → ⊥
  cut2795  adequate = bad2795  (Adequate.valid adequate Two boolean env9)
  bad2796 : PathP (λ _ → Two) (bop (bop b0 b1) (bop b1 (bop (bop b0 b0) b1))) b1 → ⊥
  bad2796  p = false≢true (cong lower p)
  cut2796 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 1) (op (op (var 0) (var 2)) (var 1)))) , (var 1)) → ⊥
  cut2796  adequate = bad2796  (Adequate.valid adequate Two boolean env2)
  bad2797 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop (bop b0 b1) b0))) b1 → ⊥
  bad2797  p = false≢true (cong lower p)
  cut2797 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 1) (op (op (var 0) (var 2)) (var 1)))) , (var 2)) → ⊥
  cut2797  adequate = bad2797  (Adequate.valid adequate Two boolean env1)
  bad2798 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop (bop b0 b0) b0))) b1 → ⊥
  bad2798  p = false≢true (cong lower p)
  cut2798 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 1) (op (op (var 0) (var 2)) (var 1)))) , (var 3)) → ⊥
  cut2798  adequate = bad2798  (Adequate.valid adequate Two boolean env3)
  bad2799 : PathP (λ _ → Two) (bop (bop b0 b1) (bop b1 (bop (bop b0 b0) b0))) b0 → ⊥
  bad2799  p = false≢true (sym (cong lower p))
  cut2799 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 1) (op (op (var 0) (var 2)) (var 2)))) , (var 0)) → ⊥
  cut2799  adequate = bad2799  (Adequate.valid adequate Two boolean env2)
  bad2800 : PathP (λ _ → Two) (bop (bop b0 b1) (bop b1 (bop (bop b0 b1) b1))) b1 → ⊥
  bad2800  p = false≢true (cong lower p)
  cut2800 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 1) (op (op (var 0) (var 2)) (var 2)))) , (var 1)) → ⊥
  cut2800  adequate = bad2800  (Adequate.valid adequate Two boolean env8)
  bad2801 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop (bop b0 b1) b1))) b1 → ⊥
  bad2801  p = false≢true (cong lower p)
  cut2801 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 1) (op (op (var 0) (var 2)) (var 2)))) , (var 2)) → ⊥
  cut2801  adequate = bad2801  (Adequate.valid adequate Two boolean env1)
  bad2802 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop (bop b0 b0) b0))) b1 → ⊥
  bad2802  p = false≢true (cong lower p)
  cut2802 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 1) (op (op (var 0) (var 2)) (var 2)))) , (var 3)) → ⊥
  cut2802  adequate = bad2802  (Adequate.valid adequate Two boolean env3)
  bad2803 : PathP (λ _ → Two) (bop (bop b0 b1) (bop b1 (bop (bop b0 b0) b0))) b0 → ⊥
  bad2803  p = false≢true (sym (cong lower p))
  cut2803 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 1) (op (op (var 0) (var 2)) (var 3)))) , (var 0)) → ⊥
  cut2803  adequate = bad2803  (Adequate.valid adequate Two boolean env4)
  bad2804 : PathP (λ _ → Two) (bop (bop b0 b1) (bop b1 (bop (bop b0 b0) b1))) b1 → ⊥
  bad2804  p = false≢true (cong lower p)
  cut2804 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 1) (op (op (var 0) (var 2)) (var 3)))) , (var 1)) → ⊥
  cut2804  adequate = bad2804  (Adequate.valid adequate Two boolean env10)
  bad2805 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop (bop b0 b1) b0))) b1 → ⊥
  bad2805  p = false≢true (cong lower p)
  cut2805 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 1) (op (op (var 0) (var 2)) (var 3)))) , (var 2)) → ⊥
  cut2805  adequate = bad2805  (Adequate.valid adequate Two boolean env5)
  bad2806 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop (bop b0 b0) b1))) b1 → ⊥
  bad2806  p = false≢true (cong lower p)
  cut2806 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 1) (op (op (var 0) (var 2)) (var 3)))) , (var 3)) → ⊥
  cut2806  adequate = bad2806  (Adequate.valid adequate Two boolean env3)
  bad2807 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop (bop b0 b0) b0))) b1 → ⊥
  bad2807  p = false≢true (cong lower p)
  cut2807 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 1) (op (op (var 0) (var 2)) (var 3)))) , (var 4)) → ⊥
  cut2807  adequate = bad2807  (Adequate.valid adequate Two boolean env6)
  bad2808 : PathP (λ _ → Two) (bop (bop b0 b1) (bop b1 (bop (bop b1 b0) b0))) b0 → ⊥
  bad2808  p = false≢true (sym (cong lower p))
  cut2808 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 1) (op (op (var 1) (var 0)) (var 0)))) , (var 0)) → ⊥
  cut2808  adequate = bad2808  (Adequate.valid adequate Two boolean env0)
  holds2809 : (z0 z1 : A6) → (mul6 (mul6 z0 z1) (mul6 z1 (mul6 (mul6 z1 z0) z0))) ≡ z1
  holds2809 m6c0 m6c0 = refl
  holds2809 m6c0 m6c1 = refl
  holds2809 m6c0 m6c2 = refl
  holds2809 m6c1 m6c0 = refl
  holds2809 m6c1 m6c1 = refl
  holds2809 m6c1 m6c2 = refl
  holds2809 m6c2 m6c0 = refl
  holds2809 m6c2 m6c1 = refl
  holds2809 m6c2 m6c2 = refl
  cut2809 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 1) (op (op (var 1) (var 0)) (var 0)))) , (var 1)) → ⊥
  cut2809  = reject6 ((op (op (var 0) (var 1)) (op (var 1) (op (op (var 1) (var 0)) (var 0)))) , (var 1)) (λ env → holds2809 (env 0) (env 1))
  bad2810 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop (bop b0 b0) b0))) b1 → ⊥
  bad2810  p = false≢true (cong lower p)
  cut2810 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 1) (op (op (var 1) (var 0)) (var 0)))) , (var 2)) → ⊥
  cut2810  adequate = bad2810  (Adequate.valid adequate Two boolean env1)
  bad2811 : PathP (λ _ → Two) (bop (bop b1 b0) (bop b0 (bop (bop b0 b1) b0))) b1 → ⊥
  bad2811  p = false≢true (cong lower p)
  cut2811 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 1) (op (op (var 1) (var 0)) (var 1)))) , (var 0)) → ⊥
  cut2811  adequate = bad2811  (Adequate.valid adequate Two boolean env7)
  bad2812 : PathP (λ _ → Two) (bop (bop b0 b1) (bop b1 (bop (bop b1 b0) b1))) b1 → ⊥
  bad2812  p = false≢true (cong lower p)
  cut2812 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 1) (op (op (var 1) (var 0)) (var 1)))) , (var 1)) → ⊥
  cut2812  adequate = bad2812  (Adequate.valid adequate Two boolean env0)
  bad2813 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop (bop b0 b0) b0))) b1 → ⊥
  bad2813  p = false≢true (cong lower p)
  cut2813 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 1) (op (op (var 1) (var 0)) (var 1)))) , (var 2)) → ⊥
  cut2813  adequate = bad2813  (Adequate.valid adequate Two boolean env1)
  bad2814 : PathP (λ _ → Two) (bop (bop b0 b1) (bop b1 (bop (bop b1 b0) b0))) b0 → ⊥
  bad2814  p = false≢true (sym (cong lower p))
  cut2814 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 1) (op (op (var 1) (var 0)) (var 2)))) , (var 0)) → ⊥
  cut2814  adequate = bad2814  (Adequate.valid adequate Two boolean env2)
  bad2815 : PathP (λ _ → Two) (bop (bop b0 b1) (bop b1 (bop (bop b1 b0) b1))) b1 → ⊥
  bad2815  p = false≢true (cong lower p)
  cut2815 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 1) (op (op (var 1) (var 0)) (var 2)))) , (var 1)) → ⊥
  cut2815  adequate = bad2815  (Adequate.valid adequate Two boolean env8)
  bad2816 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop (bop b0 b0) b1))) b1 → ⊥
  bad2816  p = false≢true (cong lower p)
  cut2816 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 1) (op (op (var 1) (var 0)) (var 2)))) , (var 2)) → ⊥
  cut2816  adequate = bad2816  (Adequate.valid adequate Two boolean env1)
  bad2817 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop (bop b0 b0) b0))) b1 → ⊥
  bad2817  p = false≢true (cong lower p)
  cut2817 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 1) (op (op (var 1) (var 0)) (var 2)))) , (var 3)) → ⊥
  cut2817  adequate = bad2817  (Adequate.valid adequate Two boolean env3)
  bad2818 : PathP (λ _ → Two) (bop (bop b0 b1) (bop b1 (bop (bop b1 b1) b0))) b0 → ⊥
  bad2818  p = false≢true (sym (cong lower p))
  cut2818 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 1) (op (op (var 1) (var 1)) (var 0)))) , (var 0)) → ⊥
  cut2818  adequate = bad2818  (Adequate.valid adequate Two boolean env0)
  holds2819 : (z0 z1 : A5) → (mul5 (mul5 z0 z1) (mul5 z1 (mul5 (mul5 z1 z1) z0))) ≡ z1
  holds2819 m5c0 m5c0 = refl
  holds2819 m5c0 m5c1 = refl
  holds2819 m5c0 m5c2 = refl
  holds2819 m5c1 m5c0 = refl
  holds2819 m5c1 m5c1 = refl
  holds2819 m5c1 m5c2 = refl
  holds2819 m5c2 m5c0 = refl
  holds2819 m5c2 m5c1 = refl
  holds2819 m5c2 m5c2 = refl
  cut2819 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 1) (op (op (var 1) (var 1)) (var 0)))) , (var 1)) → ⊥
  cut2819  = reject5 ((op (op (var 0) (var 1)) (op (var 1) (op (op (var 1) (var 1)) (var 0)))) , (var 1)) (λ env → holds2819 (env 0) (env 1))
  bad2820 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop (bop b0 b0) b0))) b1 → ⊥
  bad2820  p = false≢true (cong lower p)
  cut2820 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 1) (op (op (var 1) (var 1)) (var 0)))) , (var 2)) → ⊥
  cut2820  adequate = bad2820  (Adequate.valid adequate Two boolean env1)
  bad2821 : PathP (λ _ → Two) (bop (bop b0 b1) (bop b1 (bop (bop b1 b1) b1))) b0 → ⊥
  bad2821  p = false≢true (sym (cong lower p))
  cut2821 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 1) (op (op (var 1) (var 1)) (var 1)))) , (var 0)) → ⊥
  cut2821  adequate = bad2821  (Adequate.valid adequate Two boolean env0)
  holds2822 : (z0 z1 : A3) → (mul3 (mul3 z0 z1) (mul3 z1 (mul3 (mul3 z1 z1) z1))) ≡ z1
  holds2822 z0 z1 = refl
  cut2822 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 1) (op (op (var 1) (var 1)) (var 1)))) , (var 1)) → ⊥
  cut2822  = reject3 ((op (op (var 0) (var 1)) (op (var 1) (op (op (var 1) (var 1)) (var 1)))) , (var 1)) (λ env → holds2822 (env 0) (env 1))
  bad2823 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop (bop b0 b0) b0))) b1 → ⊥
  bad2823  p = false≢true (cong lower p)
  cut2823 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 1) (op (op (var 1) (var 1)) (var 1)))) , (var 2)) → ⊥
  cut2823  adequate = bad2823  (Adequate.valid adequate Two boolean env1)
  bad2824 : PathP (λ _ → Two) (bop (bop b0 b1) (bop b1 (bop (bop b1 b1) b0))) b0 → ⊥
  bad2824  p = false≢true (sym (cong lower p))
  cut2824 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 1) (op (op (var 1) (var 1)) (var 2)))) , (var 0)) → ⊥
  cut2824  adequate = bad2824  (Adequate.valid adequate Two boolean env2)
  holds2825 : (z0 z1 z2 : A6) → (mul6 (mul6 z0 z1) (mul6 z1 (mul6 (mul6 z1 z1) z2))) ≡ z1
  holds2825 m6c0 m6c0 m6c0 = refl
  holds2825 m6c0 m6c0 m6c1 = refl
  holds2825 m6c0 m6c0 m6c2 = refl
  holds2825 m6c0 m6c1 m6c0 = refl
  holds2825 m6c0 m6c1 m6c1 = refl
  holds2825 m6c0 m6c1 m6c2 = refl
  holds2825 m6c0 m6c2 m6c0 = refl
  holds2825 m6c0 m6c2 m6c1 = refl
  holds2825 m6c0 m6c2 m6c2 = refl
  holds2825 m6c1 m6c0 m6c0 = refl
  holds2825 m6c1 m6c0 m6c1 = refl
  holds2825 m6c1 m6c0 m6c2 = refl
  holds2825 m6c1 m6c1 m6c0 = refl
  holds2825 m6c1 m6c1 m6c1 = refl
  holds2825 m6c1 m6c1 m6c2 = refl
  holds2825 m6c1 m6c2 m6c0 = refl
  holds2825 m6c1 m6c2 m6c1 = refl
  holds2825 m6c1 m6c2 m6c2 = refl
  holds2825 m6c2 m6c0 m6c0 = refl
  holds2825 m6c2 m6c0 m6c1 = refl
  holds2825 m6c2 m6c0 m6c2 = refl
  holds2825 m6c2 m6c1 m6c0 = refl
  holds2825 m6c2 m6c1 m6c1 = refl
  holds2825 m6c2 m6c1 m6c2 = refl
  holds2825 m6c2 m6c2 m6c0 = refl
  holds2825 m6c2 m6c2 m6c1 = refl
  holds2825 m6c2 m6c2 m6c2 = refl
  cut2825 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 1) (op (op (var 1) (var 1)) (var 2)))) , (var 1)) → ⊥
  cut2825  = reject6 ((op (op (var 0) (var 1)) (op (var 1) (op (op (var 1) (var 1)) (var 2)))) , (var 1)) (λ env → holds2825 (env 0) (env 1) (env 2))
  bad2826 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop (bop b0 b0) b1))) b1 → ⊥
  bad2826  p = false≢true (cong lower p)
  cut2826 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 1) (op (op (var 1) (var 1)) (var 2)))) , (var 2)) → ⊥
  cut2826  adequate = bad2826  (Adequate.valid adequate Two boolean env1)
  bad2827 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop (bop b0 b0) b0))) b1 → ⊥
  bad2827  p = false≢true (cong lower p)
  cut2827 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 1) (op (op (var 1) (var 1)) (var 2)))) , (var 3)) → ⊥
  cut2827  adequate = bad2827  (Adequate.valid adequate Two boolean env3)
  bad2828 : PathP (λ _ → Two) (bop (bop b0 b1) (bop b1 (bop (bop b1 b0) b0))) b0 → ⊥
  bad2828  p = false≢true (sym (cong lower p))
  cut2828 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 1) (op (op (var 1) (var 2)) (var 0)))) , (var 0)) → ⊥
  cut2828  adequate = bad2828  (Adequate.valid adequate Two boolean env2)
  holds2829 : (z0 z1 z2 : A13) → (mul13 (mul13 z0 z1) (mul13 z1 (mul13 (mul13 z1 z2) z0))) ≡ z1
  holds2829 m13c0 m13c0 m13c0 = refl
  holds2829 m13c0 m13c0 m13c1 = refl
  holds2829 m13c0 m13c0 m13c2 = refl
  holds2829 m13c0 m13c0 m13c3 = refl
  holds2829 m13c0 m13c1 m13c0 = refl
  holds2829 m13c0 m13c1 m13c1 = refl
  holds2829 m13c0 m13c1 m13c2 = refl
  holds2829 m13c0 m13c1 m13c3 = refl
  holds2829 m13c0 m13c2 m13c0 = refl
  holds2829 m13c0 m13c2 m13c1 = refl
  holds2829 m13c0 m13c2 m13c2 = refl
  holds2829 m13c0 m13c2 m13c3 = refl
  holds2829 m13c0 m13c3 m13c0 = refl
  holds2829 m13c0 m13c3 m13c1 = refl
  holds2829 m13c0 m13c3 m13c2 = refl
  holds2829 m13c0 m13c3 m13c3 = refl
  holds2829 m13c1 m13c0 m13c0 = refl
  holds2829 m13c1 m13c0 m13c1 = refl
  holds2829 m13c1 m13c0 m13c2 = refl
  holds2829 m13c1 m13c0 m13c3 = refl
  holds2829 m13c1 m13c1 m13c0 = refl
  holds2829 m13c1 m13c1 m13c1 = refl
  holds2829 m13c1 m13c1 m13c2 = refl
  holds2829 m13c1 m13c1 m13c3 = refl
  holds2829 m13c1 m13c2 m13c0 = refl
  holds2829 m13c1 m13c2 m13c1 = refl
  holds2829 m13c1 m13c2 m13c2 = refl
  holds2829 m13c1 m13c2 m13c3 = refl
  holds2829 m13c1 m13c3 m13c0 = refl
  holds2829 m13c1 m13c3 m13c1 = refl
  holds2829 m13c1 m13c3 m13c2 = refl
  holds2829 m13c1 m13c3 m13c3 = refl
  holds2829 m13c2 m13c0 m13c0 = refl
  holds2829 m13c2 m13c0 m13c1 = refl
  holds2829 m13c2 m13c0 m13c2 = refl
  holds2829 m13c2 m13c0 m13c3 = refl
  holds2829 m13c2 m13c1 m13c0 = refl
  holds2829 m13c2 m13c1 m13c1 = refl
  holds2829 m13c2 m13c1 m13c2 = refl
  holds2829 m13c2 m13c1 m13c3 = refl
  holds2829 m13c2 m13c2 m13c0 = refl
  holds2829 m13c2 m13c2 m13c1 = refl
  holds2829 m13c2 m13c2 m13c2 = refl
  holds2829 m13c2 m13c2 m13c3 = refl
  holds2829 m13c2 m13c3 m13c0 = refl
  holds2829 m13c2 m13c3 m13c1 = refl
  holds2829 m13c2 m13c3 m13c2 = refl
  holds2829 m13c2 m13c3 m13c3 = refl
  holds2829 m13c3 m13c0 m13c0 = refl
  holds2829 m13c3 m13c0 m13c1 = refl
  holds2829 m13c3 m13c0 m13c2 = refl
  holds2829 m13c3 m13c0 m13c3 = refl
  holds2829 m13c3 m13c1 m13c0 = refl
  holds2829 m13c3 m13c1 m13c1 = refl
  holds2829 m13c3 m13c1 m13c2 = refl
  holds2829 m13c3 m13c1 m13c3 = refl
  holds2829 m13c3 m13c2 m13c0 = refl
  holds2829 m13c3 m13c2 m13c1 = refl
  holds2829 m13c3 m13c2 m13c2 = refl
  holds2829 m13c3 m13c2 m13c3 = refl
  holds2829 m13c3 m13c3 m13c0 = refl
  holds2829 m13c3 m13c3 m13c1 = refl
  holds2829 m13c3 m13c3 m13c2 = refl
  holds2829 m13c3 m13c3 m13c3 = refl
  cut2829 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 1) (op (op (var 1) (var 2)) (var 0)))) , (var 1)) → ⊥
  cut2829  = reject13 ((op (op (var 0) (var 1)) (op (var 1) (op (op (var 1) (var 2)) (var 0)))) , (var 1)) (λ env → holds2829 (env 0) (env 1) (env 2))
  bad2830 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop (bop b0 b1) b0))) b1 → ⊥
  bad2830  p = false≢true (cong lower p)
  cut2830 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 1) (op (op (var 1) (var 2)) (var 0)))) , (var 2)) → ⊥
  cut2830  adequate = bad2830  (Adequate.valid adequate Two boolean env1)
  bad2831 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop (bop b0 b0) b0))) b1 → ⊥
  bad2831  p = false≢true (cong lower p)
  cut2831 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 1) (op (op (var 1) (var 2)) (var 0)))) , (var 3)) → ⊥
  cut2831  adequate = bad2831  (Adequate.valid adequate Two boolean env3)
  bad2832 : PathP (λ _ → Two) (bop (bop b0 b1) (bop b1 (bop (bop b1 b1) b1))) b0 → ⊥
  bad2832  p = false≢true (sym (cong lower p))
  cut2832 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 1) (op (op (var 1) (var 2)) (var 1)))) , (var 0)) → ⊥
  cut2832  adequate = bad2832  (Adequate.valid adequate Two boolean env8)
  bad2833 : PathP (λ _ → Two) (bop (bop b0 b1) (bop b1 (bop (bop b1 b0) b1))) b1 → ⊥
  bad2833  p = false≢true (cong lower p)
  cut2833 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 1) (op (op (var 1) (var 2)) (var 1)))) , (var 1)) → ⊥
  cut2833  adequate = bad2833  (Adequate.valid adequate Two boolean env2)
  bad2834 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop (bop b0 b1) b0))) b1 → ⊥
  bad2834  p = false≢true (cong lower p)
  cut2834 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 1) (op (op (var 1) (var 2)) (var 1)))) , (var 2)) → ⊥
  cut2834  adequate = bad2834  (Adequate.valid adequate Two boolean env1)
  bad2835 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop (bop b0 b0) b0))) b1 → ⊥
  bad2835  p = false≢true (cong lower p)
  cut2835 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 1) (op (op (var 1) (var 2)) (var 1)))) , (var 3)) → ⊥
  cut2835  adequate = bad2835  (Adequate.valid adequate Two boolean env3)
  bad2836 : PathP (λ _ → Two) (bop (bop b0 b1) (bop b1 (bop (bop b1 b0) b0))) b0 → ⊥
  bad2836  p = false≢true (sym (cong lower p))
  cut2836 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 1) (op (op (var 1) (var 2)) (var 2)))) , (var 0)) → ⊥
  cut2836  adequate = bad2836  (Adequate.valid adequate Two boolean env2)
  holds2837 : (z0 z1 z2 : A6) → (mul6 (mul6 z0 z1) (mul6 z1 (mul6 (mul6 z1 z2) z2))) ≡ z1
  holds2837 m6c0 m6c0 m6c0 = refl
  holds2837 m6c0 m6c0 m6c1 = refl
  holds2837 m6c0 m6c0 m6c2 = refl
  holds2837 m6c0 m6c1 m6c0 = refl
  holds2837 m6c0 m6c1 m6c1 = refl
  holds2837 m6c0 m6c1 m6c2 = refl
  holds2837 m6c0 m6c2 m6c0 = refl
  holds2837 m6c0 m6c2 m6c1 = refl
  holds2837 m6c0 m6c2 m6c2 = refl
  holds2837 m6c1 m6c0 m6c0 = refl
  holds2837 m6c1 m6c0 m6c1 = refl
  holds2837 m6c1 m6c0 m6c2 = refl
  holds2837 m6c1 m6c1 m6c0 = refl
  holds2837 m6c1 m6c1 m6c1 = refl
  holds2837 m6c1 m6c1 m6c2 = refl
  holds2837 m6c1 m6c2 m6c0 = refl
  holds2837 m6c1 m6c2 m6c1 = refl
  holds2837 m6c1 m6c2 m6c2 = refl
  holds2837 m6c2 m6c0 m6c0 = refl
  holds2837 m6c2 m6c0 m6c1 = refl
  holds2837 m6c2 m6c0 m6c2 = refl
  holds2837 m6c2 m6c1 m6c0 = refl
  holds2837 m6c2 m6c1 m6c1 = refl
  holds2837 m6c2 m6c1 m6c2 = refl
  holds2837 m6c2 m6c2 m6c0 = refl
  holds2837 m6c2 m6c2 m6c1 = refl
  holds2837 m6c2 m6c2 m6c2 = refl
  cut2837 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 1) (op (op (var 1) (var 2)) (var 2)))) , (var 1)) → ⊥
  cut2837  = reject6 ((op (op (var 0) (var 1)) (op (var 1) (op (op (var 1) (var 2)) (var 2)))) , (var 1)) (λ env → holds2837 (env 0) (env 1) (env 2))
  bad2838 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop (bop b0 b1) b1))) b1 → ⊥
  bad2838  p = false≢true (cong lower p)
  cut2838 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 1) (op (op (var 1) (var 2)) (var 2)))) , (var 2)) → ⊥
  cut2838  adequate = bad2838  (Adequate.valid adequate Two boolean env1)
  bad2839 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop (bop b0 b0) b0))) b1 → ⊥
  bad2839  p = false≢true (cong lower p)
  cut2839 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 1) (op (op (var 1) (var 2)) (var 2)))) , (var 3)) → ⊥
  cut2839  adequate = bad2839  (Adequate.valid adequate Two boolean env3)
  bad2840 : PathP (λ _ → Two) (bop (bop b0 b1) (bop b1 (bop (bop b1 b0) b0))) b0 → ⊥
  bad2840  p = false≢true (sym (cong lower p))
  cut2840 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 1) (op (op (var 1) (var 2)) (var 3)))) , (var 0)) → ⊥
  cut2840  adequate = bad2840  (Adequate.valid adequate Two boolean env4)
  bad2841 : PathP (λ _ → Two) (bop (bop b0 b1) (bop b1 (bop (bop b1 b0) b1))) b1 → ⊥
  bad2841  p = false≢true (cong lower p)
  cut2841 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 1) (op (op (var 1) (var 2)) (var 3)))) , (var 1)) → ⊥
  cut2841  adequate = bad2841  (Adequate.valid adequate Two boolean env10)
  bad2842 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop (bop b0 b1) b0))) b1 → ⊥
  bad2842  p = false≢true (cong lower p)
  cut2842 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 1) (op (op (var 1) (var 2)) (var 3)))) , (var 2)) → ⊥
  cut2842  adequate = bad2842  (Adequate.valid adequate Two boolean env5)
  bad2843 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop (bop b0 b0) b1))) b1 → ⊥
  bad2843  p = false≢true (cong lower p)
  cut2843 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 1) (op (op (var 1) (var 2)) (var 3)))) , (var 3)) → ⊥
  cut2843  adequate = bad2843  (Adequate.valid adequate Two boolean env3)
  bad2844 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop (bop b0 b0) b0))) b1 → ⊥
  bad2844  p = false≢true (cong lower p)
  cut2844 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 1) (op (op (var 1) (var 2)) (var 3)))) , (var 4)) → ⊥
  cut2844  adequate = bad2844  (Adequate.valid adequate Two boolean env6)
  bad2845 : PathP (λ _ → Two) (bop (bop b0 b1) (bop b1 (bop (bop b0 b0) b0))) b0 → ⊥
  bad2845  p = false≢true (sym (cong lower p))
  cut2845 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 1) (op (op (var 2) (var 0)) (var 0)))) , (var 0)) → ⊥
  cut2845  adequate = bad2845  (Adequate.valid adequate Two boolean env2)
  holds2846 : (z0 z1 z2 : A6) → (mul6 (mul6 z0 z1) (mul6 z1 (mul6 (mul6 z2 z0) z0))) ≡ z1
  holds2846 m6c0 m6c0 m6c0 = refl
  holds2846 m6c0 m6c0 m6c1 = refl
  holds2846 m6c0 m6c0 m6c2 = refl
  holds2846 m6c0 m6c1 m6c0 = refl
  holds2846 m6c0 m6c1 m6c1 = refl
  holds2846 m6c0 m6c1 m6c2 = refl
  holds2846 m6c0 m6c2 m6c0 = refl
  holds2846 m6c0 m6c2 m6c1 = refl
  holds2846 m6c0 m6c2 m6c2 = refl
  holds2846 m6c1 m6c0 m6c0 = refl
  holds2846 m6c1 m6c0 m6c1 = refl
  holds2846 m6c1 m6c0 m6c2 = refl
  holds2846 m6c1 m6c1 m6c0 = refl
  holds2846 m6c1 m6c1 m6c1 = refl
  holds2846 m6c1 m6c1 m6c2 = refl
  holds2846 m6c1 m6c2 m6c0 = refl
  holds2846 m6c1 m6c2 m6c1 = refl
  holds2846 m6c1 m6c2 m6c2 = refl
  holds2846 m6c2 m6c0 m6c0 = refl
  holds2846 m6c2 m6c0 m6c1 = refl
  holds2846 m6c2 m6c0 m6c2 = refl
  holds2846 m6c2 m6c1 m6c0 = refl
  holds2846 m6c2 m6c1 m6c1 = refl
  holds2846 m6c2 m6c1 m6c2 = refl
  holds2846 m6c2 m6c2 m6c0 = refl
  holds2846 m6c2 m6c2 m6c1 = refl
  holds2846 m6c2 m6c2 m6c2 = refl
  cut2846 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 1) (op (op (var 2) (var 0)) (var 0)))) , (var 1)) → ⊥
  cut2846  = reject6 ((op (op (var 0) (var 1)) (op (var 1) (op (op (var 2) (var 0)) (var 0)))) , (var 1)) (λ env → holds2846 (env 0) (env 1) (env 2))
  bad2847 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop (bop b1 b0) b0))) b1 → ⊥
  bad2847  p = false≢true (cong lower p)
  cut2847 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 1) (op (op (var 2) (var 0)) (var 0)))) , (var 2)) → ⊥
  cut2847  adequate = bad2847  (Adequate.valid adequate Two boolean env1)
  bad2848 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop (bop b0 b0) b0))) b1 → ⊥
  bad2848  p = false≢true (cong lower p)
  cut2848 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 1) (op (op (var 2) (var 0)) (var 0)))) , (var 3)) → ⊥
  cut2848  adequate = bad2848  (Adequate.valid adequate Two boolean env3)
  bad2849 : PathP (λ _ → Two) (bop (bop b1 b0) (bop b0 (bop (bop b0 b1) b0))) b1 → ⊥
  bad2849  p = false≢true (cong lower p)
  cut2849 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 1) (op (op (var 2) (var 0)) (var 1)))) , (var 0)) → ⊥
  cut2849  adequate = bad2849  (Adequate.valid adequate Two boolean env9)
  bad2850 : PathP (λ _ → Two) (bop (bop b0 b1) (bop b1 (bop (bop b0 b0) b1))) b1 → ⊥
  bad2850  p = false≢true (cong lower p)
  cut2850 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 1) (op (op (var 2) (var 0)) (var 1)))) , (var 1)) → ⊥
  cut2850  adequate = bad2850  (Adequate.valid adequate Two boolean env2)
  bad2851 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop (bop b1 b0) b0))) b1 → ⊥
  bad2851  p = false≢true (cong lower p)
  cut2851 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 1) (op (op (var 2) (var 0)) (var 1)))) , (var 2)) → ⊥
  cut2851  adequate = bad2851  (Adequate.valid adequate Two boolean env1)
  bad2852 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop (bop b0 b0) b0))) b1 → ⊥
  bad2852  p = false≢true (cong lower p)
  cut2852 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 1) (op (op (var 2) (var 0)) (var 1)))) , (var 3)) → ⊥
  cut2852  adequate = bad2852  (Adequate.valid adequate Two boolean env3)
  bad2853 : PathP (λ _ → Two) (bop (bop b0 b1) (bop b1 (bop (bop b0 b0) b0))) b0 → ⊥
  bad2853  p = false≢true (sym (cong lower p))
  cut2853 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 1) (op (op (var 2) (var 0)) (var 2)))) , (var 0)) → ⊥
  cut2853  adequate = bad2853  (Adequate.valid adequate Two boolean env2)
  bad2854 : PathP (λ _ → Two) (bop (bop b0 b1) (bop b1 (bop (bop b1 b0) b1))) b1 → ⊥
  bad2854  p = false≢true (cong lower p)
  cut2854 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 1) (op (op (var 2) (var 0)) (var 2)))) , (var 1)) → ⊥
  cut2854  adequate = bad2854  (Adequate.valid adequate Two boolean env8)
  bad2855 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop (bop b1 b0) b1))) b1 → ⊥
  bad2855  p = false≢true (cong lower p)
  cut2855 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 1) (op (op (var 2) (var 0)) (var 2)))) , (var 2)) → ⊥
  cut2855  adequate = bad2855  (Adequate.valid adequate Two boolean env1)
  bad2856 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop (bop b0 b0) b0))) b1 → ⊥
  bad2856  p = false≢true (cong lower p)
  cut2856 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 1) (op (op (var 2) (var 0)) (var 2)))) , (var 3)) → ⊥
  cut2856  adequate = bad2856  (Adequate.valid adequate Two boolean env3)
  bad2857 : PathP (λ _ → Two) (bop (bop b0 b1) (bop b1 (bop (bop b0 b0) b0))) b0 → ⊥
  bad2857  p = false≢true (sym (cong lower p))
  cut2857 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 1) (op (op (var 2) (var 0)) (var 3)))) , (var 0)) → ⊥
  cut2857  adequate = bad2857  (Adequate.valid adequate Two boolean env4)
  bad2858 : PathP (λ _ → Two) (bop (bop b0 b1) (bop b1 (bop (bop b0 b0) b1))) b1 → ⊥
  bad2858  p = false≢true (cong lower p)
  cut2858 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 1) (op (op (var 2) (var 0)) (var 3)))) , (var 1)) → ⊥
  cut2858  adequate = bad2858  (Adequate.valid adequate Two boolean env10)
  bad2859 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop (bop b1 b0) b0))) b1 → ⊥
  bad2859  p = false≢true (cong lower p)
  cut2859 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 1) (op (op (var 2) (var 0)) (var 3)))) , (var 2)) → ⊥
  cut2859  adequate = bad2859  (Adequate.valid adequate Two boolean env5)
  bad2860 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop (bop b0 b0) b1))) b1 → ⊥
  bad2860  p = false≢true (cong lower p)
  cut2860 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 1) (op (op (var 2) (var 0)) (var 3)))) , (var 3)) → ⊥
  cut2860  adequate = bad2860  (Adequate.valid adequate Two boolean env3)
  bad2861 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop (bop b0 b0) b0))) b1 → ⊥
  bad2861  p = false≢true (cong lower p)
  cut2861 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 1) (op (op (var 2) (var 0)) (var 3)))) , (var 4)) → ⊥
  cut2861  adequate = bad2861  (Adequate.valid adequate Two boolean env6)
  bad2862 : PathP (λ _ → Two) (bop (bop b0 b1) (bop b1 (bop (bop b0 b1) b0))) b0 → ⊥
  bad2862  p = false≢true (sym (cong lower p))
  cut2862 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 1) (op (op (var 2) (var 1)) (var 0)))) , (var 0)) → ⊥
  cut2862  adequate = bad2862  (Adequate.valid adequate Two boolean env2)
  holds2863 : (z0 z1 z2 : A6) → (mul6 (mul6 z0 z1) (mul6 z1 (mul6 (mul6 z2 z1) z0))) ≡ z1
  holds2863 m6c0 m6c0 m6c0 = refl
  holds2863 m6c0 m6c0 m6c1 = refl
  holds2863 m6c0 m6c0 m6c2 = refl
  holds2863 m6c0 m6c1 m6c0 = refl
  holds2863 m6c0 m6c1 m6c1 = refl
  holds2863 m6c0 m6c1 m6c2 = refl
  holds2863 m6c0 m6c2 m6c0 = refl
  holds2863 m6c0 m6c2 m6c1 = refl
  holds2863 m6c0 m6c2 m6c2 = refl
  holds2863 m6c1 m6c0 m6c0 = refl
  holds2863 m6c1 m6c0 m6c1 = refl
  holds2863 m6c1 m6c0 m6c2 = refl
  holds2863 m6c1 m6c1 m6c0 = refl
  holds2863 m6c1 m6c1 m6c1 = refl
  holds2863 m6c1 m6c1 m6c2 = refl
  holds2863 m6c1 m6c2 m6c0 = refl
  holds2863 m6c1 m6c2 m6c1 = refl
  holds2863 m6c1 m6c2 m6c2 = refl
  holds2863 m6c2 m6c0 m6c0 = refl
  holds2863 m6c2 m6c0 m6c1 = refl
  holds2863 m6c2 m6c0 m6c2 = refl
  holds2863 m6c2 m6c1 m6c0 = refl
  holds2863 m6c2 m6c1 m6c1 = refl
  holds2863 m6c2 m6c1 m6c2 = refl
  holds2863 m6c2 m6c2 m6c0 = refl
  holds2863 m6c2 m6c2 m6c1 = refl
  holds2863 m6c2 m6c2 m6c2 = refl
  cut2863 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 1) (op (op (var 2) (var 1)) (var 0)))) , (var 1)) → ⊥
  cut2863  = reject6 ((op (op (var 0) (var 1)) (op (var 1) (op (op (var 2) (var 1)) (var 0)))) , (var 1)) (λ env → holds2863 (env 0) (env 1) (env 2))
  bad2864 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop (bop b1 b0) b0))) b1 → ⊥
  bad2864  p = false≢true (cong lower p)
  cut2864 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 1) (op (op (var 2) (var 1)) (var 0)))) , (var 2)) → ⊥
  cut2864  adequate = bad2864  (Adequate.valid adequate Two boolean env1)
  bad2865 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop (bop b0 b0) b0))) b1 → ⊥
  bad2865  p = false≢true (cong lower p)
  cut2865 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 1) (op (op (var 2) (var 1)) (var 0)))) , (var 3)) → ⊥
  cut2865  adequate = bad2865  (Adequate.valid adequate Two boolean env3)
  bad2866 : PathP (λ _ → Two) (bop (bop b0 b1) (bop b1 (bop (bop b1 b1) b1))) b0 → ⊥
  bad2866  p = false≢true (sym (cong lower p))
  cut2866 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 1) (op (op (var 2) (var 1)) (var 1)))) , (var 0)) → ⊥
  cut2866  adequate = bad2866  (Adequate.valid adequate Two boolean env8)
  bad2867 : PathP (λ _ → Two) (bop (bop b0 b1) (bop b1 (bop (bop b0 b1) b1))) b1 → ⊥
  bad2867  p = false≢true (cong lower p)
  cut2867 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 1) (op (op (var 2) (var 1)) (var 1)))) , (var 1)) → ⊥
  cut2867  adequate = bad2867  (Adequate.valid adequate Two boolean env2)
  bad2868 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop (bop b1 b0) b0))) b1 → ⊥
  bad2868  p = false≢true (cong lower p)
  cut2868 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 1) (op (op (var 2) (var 1)) (var 1)))) , (var 2)) → ⊥
  cut2868  adequate = bad2868  (Adequate.valid adequate Two boolean env1)
  bad2869 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop (bop b0 b0) b0))) b1 → ⊥
  bad2869  p = false≢true (cong lower p)
  cut2869 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 1) (op (op (var 2) (var 1)) (var 1)))) , (var 3)) → ⊥
  cut2869  adequate = bad2869  (Adequate.valid adequate Two boolean env3)
  bad2870 : PathP (λ _ → Two) (bop (bop b0 b1) (bop b1 (bop (bop b0 b1) b0))) b0 → ⊥
  bad2870  p = false≢true (sym (cong lower p))
  cut2870 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 1) (op (op (var 2) (var 1)) (var 2)))) , (var 0)) → ⊥
  cut2870  adequate = bad2870  (Adequate.valid adequate Two boolean env2)
  holds2871 : (z0 z1 z2 : A6) → (mul6 (mul6 z0 z1) (mul6 z1 (mul6 (mul6 z2 z1) z2))) ≡ z1
  holds2871 m6c0 m6c0 m6c0 = refl
  holds2871 m6c0 m6c0 m6c1 = refl
  holds2871 m6c0 m6c0 m6c2 = refl
  holds2871 m6c0 m6c1 m6c0 = refl
  holds2871 m6c0 m6c1 m6c1 = refl
  holds2871 m6c0 m6c1 m6c2 = refl
  holds2871 m6c0 m6c2 m6c0 = refl
  holds2871 m6c0 m6c2 m6c1 = refl
  holds2871 m6c0 m6c2 m6c2 = refl
  holds2871 m6c1 m6c0 m6c0 = refl
  holds2871 m6c1 m6c0 m6c1 = refl
  holds2871 m6c1 m6c0 m6c2 = refl
  holds2871 m6c1 m6c1 m6c0 = refl
  holds2871 m6c1 m6c1 m6c1 = refl
  holds2871 m6c1 m6c1 m6c2 = refl
  holds2871 m6c1 m6c2 m6c0 = refl
  holds2871 m6c1 m6c2 m6c1 = refl
  holds2871 m6c1 m6c2 m6c2 = refl
  holds2871 m6c2 m6c0 m6c0 = refl
  holds2871 m6c2 m6c0 m6c1 = refl
  holds2871 m6c2 m6c0 m6c2 = refl
  holds2871 m6c2 m6c1 m6c0 = refl
  holds2871 m6c2 m6c1 m6c1 = refl
  holds2871 m6c2 m6c1 m6c2 = refl
  holds2871 m6c2 m6c2 m6c0 = refl
  holds2871 m6c2 m6c2 m6c1 = refl
  holds2871 m6c2 m6c2 m6c2 = refl
  cut2871 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 1) (op (op (var 2) (var 1)) (var 2)))) , (var 1)) → ⊥
  cut2871  = reject6 ((op (op (var 0) (var 1)) (op (var 1) (op (op (var 2) (var 1)) (var 2)))) , (var 1)) (λ env → holds2871 (env 0) (env 1) (env 2))
  bad2872 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop (bop b1 b0) b1))) b1 → ⊥
  bad2872  p = false≢true (cong lower p)
  cut2872 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 1) (op (op (var 2) (var 1)) (var 2)))) , (var 2)) → ⊥
  cut2872  adequate = bad2872  (Adequate.valid adequate Two boolean env1)
  bad2873 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop (bop b0 b0) b0))) b1 → ⊥
  bad2873  p = false≢true (cong lower p)
  cut2873 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 1) (op (op (var 2) (var 1)) (var 2)))) , (var 3)) → ⊥
  cut2873  adequate = bad2873  (Adequate.valid adequate Two boolean env3)
  bad2874 : PathP (λ _ → Two) (bop (bop b0 b1) (bop b1 (bop (bop b0 b1) b0))) b0 → ⊥
  bad2874  p = false≢true (sym (cong lower p))
  cut2874 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 1) (op (op (var 2) (var 1)) (var 3)))) , (var 0)) → ⊥
  cut2874  adequate = bad2874  (Adequate.valid adequate Two boolean env4)
  bad2875 : PathP (λ _ → Two) (bop (bop b0 b1) (bop b1 (bop (bop b0 b1) b1))) b1 → ⊥
  bad2875  p = false≢true (cong lower p)
  cut2875 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 1) (op (op (var 2) (var 1)) (var 3)))) , (var 1)) → ⊥
  cut2875  adequate = bad2875  (Adequate.valid adequate Two boolean env10)
  bad2876 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop (bop b1 b0) b0))) b1 → ⊥
  bad2876  p = false≢true (cong lower p)
  cut2876 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 1) (op (op (var 2) (var 1)) (var 3)))) , (var 2)) → ⊥
  cut2876  adequate = bad2876  (Adequate.valid adequate Two boolean env5)
  bad2877 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop (bop b0 b0) b1))) b1 → ⊥
  bad2877  p = false≢true (cong lower p)
  cut2877 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 1) (op (op (var 2) (var 1)) (var 3)))) , (var 3)) → ⊥
  cut2877  adequate = bad2877  (Adequate.valid adequate Two boolean env3)
  bad2878 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop (bop b0 b0) b0))) b1 → ⊥
  bad2878  p = false≢true (cong lower p)
  cut2878 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 1) (op (op (var 2) (var 1)) (var 3)))) , (var 4)) → ⊥
  cut2878  adequate = bad2878  (Adequate.valid adequate Two boolean env6)
  bad2879 : PathP (λ _ → Two) (bop (bop b0 b1) (bop b1 (bop (bop b0 b0) b0))) b0 → ⊥
  bad2879  p = false≢true (sym (cong lower p))
  cut2879 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 1) (op (op (var 2) (var 2)) (var 0)))) , (var 0)) → ⊥
  cut2879  adequate = bad2879  (Adequate.valid adequate Two boolean env2)
  holds2880 : (z0 z1 z2 : A9) → (mul9 (mul9 z0 z1) (mul9 z1 (mul9 (mul9 z2 z2) z0))) ≡ z1
  holds2880 m9c0 m9c0 m9c0 = refl
  holds2880 m9c0 m9c0 m9c1 = refl
  holds2880 m9c0 m9c0 m9c2 = refl
  holds2880 m9c0 m9c1 m9c0 = refl
  holds2880 m9c0 m9c1 m9c1 = refl
  holds2880 m9c0 m9c1 m9c2 = refl
  holds2880 m9c0 m9c2 m9c0 = refl
  holds2880 m9c0 m9c2 m9c1 = refl
  holds2880 m9c0 m9c2 m9c2 = refl
  holds2880 m9c1 m9c0 m9c0 = refl
  holds2880 m9c1 m9c0 m9c1 = refl
  holds2880 m9c1 m9c0 m9c2 = refl
  holds2880 m9c1 m9c1 m9c0 = refl
  holds2880 m9c1 m9c1 m9c1 = refl
  holds2880 m9c1 m9c1 m9c2 = refl
  holds2880 m9c1 m9c2 m9c0 = refl
  holds2880 m9c1 m9c2 m9c1 = refl
  holds2880 m9c1 m9c2 m9c2 = refl
  holds2880 m9c2 m9c0 m9c0 = refl
  holds2880 m9c2 m9c0 m9c1 = refl
  holds2880 m9c2 m9c0 m9c2 = refl
  holds2880 m9c2 m9c1 m9c0 = refl
  holds2880 m9c2 m9c1 m9c1 = refl
  holds2880 m9c2 m9c1 m9c2 = refl
  holds2880 m9c2 m9c2 m9c0 = refl
  holds2880 m9c2 m9c2 m9c1 = refl
  holds2880 m9c2 m9c2 m9c2 = refl
  cut2880 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 1) (op (op (var 2) (var 2)) (var 0)))) , (var 1)) → ⊥
  cut2880  = reject9 ((op (op (var 0) (var 1)) (op (var 1) (op (op (var 2) (var 2)) (var 0)))) , (var 1)) (λ env → holds2880 (env 0) (env 1) (env 2))
  bad2881 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop (bop b1 b1) b0))) b1 → ⊥
  bad2881  p = false≢true (cong lower p)
  cut2881 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 1) (op (op (var 2) (var 2)) (var 0)))) , (var 2)) → ⊥
  cut2881  adequate = bad2881  (Adequate.valid adequate Two boolean env1)
  bad2882 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop (bop b0 b0) b0))) b1 → ⊥
  bad2882  p = false≢true (cong lower p)
  cut2882 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 1) (op (op (var 2) (var 2)) (var 0)))) , (var 3)) → ⊥
  cut2882  adequate = bad2882  (Adequate.valid adequate Two boolean env3)
  bad2883 : PathP (λ _ → Two) (bop (bop b0 b1) (bop b1 (bop (bop b1 b1) b1))) b0 → ⊥
  bad2883  p = false≢true (sym (cong lower p))
  cut2883 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 1) (op (op (var 2) (var 2)) (var 1)))) , (var 0)) → ⊥
  cut2883  adequate = bad2883  (Adequate.valid adequate Two boolean env8)
  bad2884 : PathP (λ _ → Two) (bop (bop b0 b1) (bop b1 (bop (bop b0 b0) b1))) b1 → ⊥
  bad2884  p = false≢true (cong lower p)
  cut2884 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 1) (op (op (var 2) (var 2)) (var 1)))) , (var 1)) → ⊥
  cut2884  adequate = bad2884  (Adequate.valid adequate Two boolean env2)
  bad2885 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop (bop b1 b1) b0))) b1 → ⊥
  bad2885  p = false≢true (cong lower p)
  cut2885 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 1) (op (op (var 2) (var 2)) (var 1)))) , (var 2)) → ⊥
  cut2885  adequate = bad2885  (Adequate.valid adequate Two boolean env1)
  bad2886 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop (bop b0 b0) b0))) b1 → ⊥
  bad2886  p = false≢true (cong lower p)
  cut2886 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 1) (op (op (var 2) (var 2)) (var 1)))) , (var 3)) → ⊥
  cut2886  adequate = bad2886  (Adequate.valid adequate Two boolean env3)
  bad2887 : PathP (λ _ → Two) (bop (bop b0 b1) (bop b1 (bop (bop b0 b0) b0))) b0 → ⊥
  bad2887  p = false≢true (sym (cong lower p))
  cut2887 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 1) (op (op (var 2) (var 2)) (var 2)))) , (var 0)) → ⊥
  cut2887  adequate = bad2887  (Adequate.valid adequate Two boolean env2)
  holds2888 : (z0 z1 z2 : A6) → (mul6 (mul6 z0 z1) (mul6 z1 (mul6 (mul6 z2 z2) z2))) ≡ z1
  holds2888 m6c0 m6c0 m6c0 = refl
  holds2888 m6c0 m6c0 m6c1 = refl
  holds2888 m6c0 m6c0 m6c2 = refl
  holds2888 m6c0 m6c1 m6c0 = refl
  holds2888 m6c0 m6c1 m6c1 = refl
  holds2888 m6c0 m6c1 m6c2 = refl
  holds2888 m6c0 m6c2 m6c0 = refl
  holds2888 m6c0 m6c2 m6c1 = refl
  holds2888 m6c0 m6c2 m6c2 = refl
  holds2888 m6c1 m6c0 m6c0 = refl
  holds2888 m6c1 m6c0 m6c1 = refl
  holds2888 m6c1 m6c0 m6c2 = refl
  holds2888 m6c1 m6c1 m6c0 = refl
  holds2888 m6c1 m6c1 m6c1 = refl
  holds2888 m6c1 m6c1 m6c2 = refl
  holds2888 m6c1 m6c2 m6c0 = refl
  holds2888 m6c1 m6c2 m6c1 = refl
  holds2888 m6c1 m6c2 m6c2 = refl
  holds2888 m6c2 m6c0 m6c0 = refl
  holds2888 m6c2 m6c0 m6c1 = refl
  holds2888 m6c2 m6c0 m6c2 = refl
  holds2888 m6c2 m6c1 m6c0 = refl
  holds2888 m6c2 m6c1 m6c1 = refl
  holds2888 m6c2 m6c1 m6c2 = refl
  holds2888 m6c2 m6c2 m6c0 = refl
  holds2888 m6c2 m6c2 m6c1 = refl
  holds2888 m6c2 m6c2 m6c2 = refl
  cut2888 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 1) (op (op (var 2) (var 2)) (var 2)))) , (var 1)) → ⊥
  cut2888  = reject6 ((op (op (var 0) (var 1)) (op (var 1) (op (op (var 2) (var 2)) (var 2)))) , (var 1)) (λ env → holds2888 (env 0) (env 1) (env 2))
  bad2889 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop (bop b1 b1) b1))) b1 → ⊥
  bad2889  p = false≢true (cong lower p)
  cut2889 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 1) (op (op (var 2) (var 2)) (var 2)))) , (var 2)) → ⊥
  cut2889  adequate = bad2889  (Adequate.valid adequate Two boolean env1)
  bad2890 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop (bop b0 b0) b0))) b1 → ⊥
  bad2890  p = false≢true (cong lower p)
  cut2890 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 1) (op (op (var 2) (var 2)) (var 2)))) , (var 3)) → ⊥
  cut2890  adequate = bad2890  (Adequate.valid adequate Two boolean env3)
  bad2891 : PathP (λ _ → Two) (bop (bop b0 b1) (bop b1 (bop (bop b0 b0) b0))) b0 → ⊥
  bad2891  p = false≢true (sym (cong lower p))
  cut2891 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 1) (op (op (var 2) (var 2)) (var 3)))) , (var 0)) → ⊥
  cut2891  adequate = bad2891  (Adequate.valid adequate Two boolean env4)
  bad2892 : PathP (λ _ → Two) (bop (bop b0 b1) (bop b1 (bop (bop b0 b0) b1))) b1 → ⊥
  bad2892  p = false≢true (cong lower p)
  cut2892 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 1) (op (op (var 2) (var 2)) (var 3)))) , (var 1)) → ⊥
  cut2892  adequate = bad2892  (Adequate.valid adequate Two boolean env10)
  bad2893 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop (bop b1 b1) b0))) b1 → ⊥
  bad2893  p = false≢true (cong lower p)
  cut2893 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 1) (op (op (var 2) (var 2)) (var 3)))) , (var 2)) → ⊥
  cut2893  adequate = bad2893  (Adequate.valid adequate Two boolean env5)
  bad2894 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop (bop b0 b0) b1))) b1 → ⊥
  bad2894  p = false≢true (cong lower p)
  cut2894 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 1) (op (op (var 2) (var 2)) (var 3)))) , (var 3)) → ⊥
  cut2894  adequate = bad2894  (Adequate.valid adequate Two boolean env3)
  bad2895 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop (bop b0 b0) b0))) b1 → ⊥
  bad2895  p = false≢true (cong lower p)
  cut2895 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 1) (op (op (var 2) (var 2)) (var 3)))) , (var 4)) → ⊥
  cut2895  adequate = bad2895  (Adequate.valid adequate Two boolean env6)
  bad2896 : PathP (λ _ → Two) (bop (bop b0 b1) (bop b1 (bop (bop b0 b0) b0))) b0 → ⊥
  bad2896  p = false≢true (sym (cong lower p))
  cut2896 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 1) (op (op (var 2) (var 3)) (var 0)))) , (var 0)) → ⊥
  cut2896  adequate = bad2896  (Adequate.valid adequate Two boolean env4)
  holds2897 : (z0 z1 z2 z3 : A13) → (mul13 (mul13 z0 z1) (mul13 z1 (mul13 (mul13 z2 z3) z0))) ≡ z1
  holds2897 m13c0 m13c0 m13c0 m13c0 = refl
  holds2897 m13c0 m13c0 m13c0 m13c1 = refl
  holds2897 m13c0 m13c0 m13c0 m13c2 = refl
  holds2897 m13c0 m13c0 m13c0 m13c3 = refl
  holds2897 m13c0 m13c0 m13c1 m13c0 = refl
  holds2897 m13c0 m13c0 m13c1 m13c1 = refl
  holds2897 m13c0 m13c0 m13c1 m13c2 = refl
  holds2897 m13c0 m13c0 m13c1 m13c3 = refl
  holds2897 m13c0 m13c0 m13c2 m13c0 = refl
  holds2897 m13c0 m13c0 m13c2 m13c1 = refl
  holds2897 m13c0 m13c0 m13c2 m13c2 = refl
  holds2897 m13c0 m13c0 m13c2 m13c3 = refl
  holds2897 m13c0 m13c0 m13c3 m13c0 = refl
  holds2897 m13c0 m13c0 m13c3 m13c1 = refl
  holds2897 m13c0 m13c0 m13c3 m13c2 = refl
  holds2897 m13c0 m13c0 m13c3 m13c3 = refl
  holds2897 m13c0 m13c1 m13c0 m13c0 = refl
  holds2897 m13c0 m13c1 m13c0 m13c1 = refl
  holds2897 m13c0 m13c1 m13c0 m13c2 = refl
  holds2897 m13c0 m13c1 m13c0 m13c3 = refl
  holds2897 m13c0 m13c1 m13c1 m13c0 = refl
  holds2897 m13c0 m13c1 m13c1 m13c1 = refl
  holds2897 m13c0 m13c1 m13c1 m13c2 = refl
  holds2897 m13c0 m13c1 m13c1 m13c3 = refl
  holds2897 m13c0 m13c1 m13c2 m13c0 = refl
  holds2897 m13c0 m13c1 m13c2 m13c1 = refl
  holds2897 m13c0 m13c1 m13c2 m13c2 = refl
  holds2897 m13c0 m13c1 m13c2 m13c3 = refl
  holds2897 m13c0 m13c1 m13c3 m13c0 = refl
  holds2897 m13c0 m13c1 m13c3 m13c1 = refl
  holds2897 m13c0 m13c1 m13c3 m13c2 = refl
  holds2897 m13c0 m13c1 m13c3 m13c3 = refl
  holds2897 m13c0 m13c2 m13c0 m13c0 = refl
  holds2897 m13c0 m13c2 m13c0 m13c1 = refl
  holds2897 m13c0 m13c2 m13c0 m13c2 = refl
  holds2897 m13c0 m13c2 m13c0 m13c3 = refl
  holds2897 m13c0 m13c2 m13c1 m13c0 = refl
  holds2897 m13c0 m13c2 m13c1 m13c1 = refl
  holds2897 m13c0 m13c2 m13c1 m13c2 = refl
  holds2897 m13c0 m13c2 m13c1 m13c3 = refl
  holds2897 m13c0 m13c2 m13c2 m13c0 = refl
  holds2897 m13c0 m13c2 m13c2 m13c1 = refl
  holds2897 m13c0 m13c2 m13c2 m13c2 = refl
  holds2897 m13c0 m13c2 m13c2 m13c3 = refl
  holds2897 m13c0 m13c2 m13c3 m13c0 = refl
  holds2897 m13c0 m13c2 m13c3 m13c1 = refl
  holds2897 m13c0 m13c2 m13c3 m13c2 = refl
  holds2897 m13c0 m13c2 m13c3 m13c3 = refl
  holds2897 m13c0 m13c3 m13c0 m13c0 = refl
  holds2897 m13c0 m13c3 m13c0 m13c1 = refl
  holds2897 m13c0 m13c3 m13c0 m13c2 = refl
  holds2897 m13c0 m13c3 m13c0 m13c3 = refl
  holds2897 m13c0 m13c3 m13c1 m13c0 = refl
  holds2897 m13c0 m13c3 m13c1 m13c1 = refl
  holds2897 m13c0 m13c3 m13c1 m13c2 = refl
  holds2897 m13c0 m13c3 m13c1 m13c3 = refl
  holds2897 m13c0 m13c3 m13c2 m13c0 = refl
  holds2897 m13c0 m13c3 m13c2 m13c1 = refl
  holds2897 m13c0 m13c3 m13c2 m13c2 = refl
  holds2897 m13c0 m13c3 m13c2 m13c3 = refl
  holds2897 m13c0 m13c3 m13c3 m13c0 = refl
  holds2897 m13c0 m13c3 m13c3 m13c1 = refl
  holds2897 m13c0 m13c3 m13c3 m13c2 = refl
  holds2897 m13c0 m13c3 m13c3 m13c3 = refl
  holds2897 m13c1 m13c0 m13c0 m13c0 = refl
  holds2897 m13c1 m13c0 m13c0 m13c1 = refl
  holds2897 m13c1 m13c0 m13c0 m13c2 = refl
  holds2897 m13c1 m13c0 m13c0 m13c3 = refl
  holds2897 m13c1 m13c0 m13c1 m13c0 = refl
  holds2897 m13c1 m13c0 m13c1 m13c1 = refl
  holds2897 m13c1 m13c0 m13c1 m13c2 = refl
  holds2897 m13c1 m13c0 m13c1 m13c3 = refl
  holds2897 m13c1 m13c0 m13c2 m13c0 = refl
  holds2897 m13c1 m13c0 m13c2 m13c1 = refl
  holds2897 m13c1 m13c0 m13c2 m13c2 = refl
  holds2897 m13c1 m13c0 m13c2 m13c3 = refl
  holds2897 m13c1 m13c0 m13c3 m13c0 = refl
  holds2897 m13c1 m13c0 m13c3 m13c1 = refl
  holds2897 m13c1 m13c0 m13c3 m13c2 = refl
  holds2897 m13c1 m13c0 m13c3 m13c3 = refl
  holds2897 m13c1 m13c1 m13c0 m13c0 = refl
  holds2897 m13c1 m13c1 m13c0 m13c1 = refl
  holds2897 m13c1 m13c1 m13c0 m13c2 = refl
  holds2897 m13c1 m13c1 m13c0 m13c3 = refl
  holds2897 m13c1 m13c1 m13c1 m13c0 = refl
  holds2897 m13c1 m13c1 m13c1 m13c1 = refl
  holds2897 m13c1 m13c1 m13c1 m13c2 = refl
  holds2897 m13c1 m13c1 m13c1 m13c3 = refl
  holds2897 m13c1 m13c1 m13c2 m13c0 = refl
  holds2897 m13c1 m13c1 m13c2 m13c1 = refl
  holds2897 m13c1 m13c1 m13c2 m13c2 = refl
  holds2897 m13c1 m13c1 m13c2 m13c3 = refl
  holds2897 m13c1 m13c1 m13c3 m13c0 = refl
  holds2897 m13c1 m13c1 m13c3 m13c1 = refl
  holds2897 m13c1 m13c1 m13c3 m13c2 = refl
  holds2897 m13c1 m13c1 m13c3 m13c3 = refl
  holds2897 m13c1 m13c2 m13c0 m13c0 = refl
  holds2897 m13c1 m13c2 m13c0 m13c1 = refl
  holds2897 m13c1 m13c2 m13c0 m13c2 = refl
  holds2897 m13c1 m13c2 m13c0 m13c3 = refl
  holds2897 m13c1 m13c2 m13c1 m13c0 = refl
  holds2897 m13c1 m13c2 m13c1 m13c1 = refl
  holds2897 m13c1 m13c2 m13c1 m13c2 = refl
  holds2897 m13c1 m13c2 m13c1 m13c3 = refl
  holds2897 m13c1 m13c2 m13c2 m13c0 = refl
  holds2897 m13c1 m13c2 m13c2 m13c1 = refl
  holds2897 m13c1 m13c2 m13c2 m13c2 = refl
  holds2897 m13c1 m13c2 m13c2 m13c3 = refl
  holds2897 m13c1 m13c2 m13c3 m13c0 = refl
  holds2897 m13c1 m13c2 m13c3 m13c1 = refl
  holds2897 m13c1 m13c2 m13c3 m13c2 = refl
  holds2897 m13c1 m13c2 m13c3 m13c3 = refl
  holds2897 m13c1 m13c3 m13c0 m13c0 = refl
  holds2897 m13c1 m13c3 m13c0 m13c1 = refl
  holds2897 m13c1 m13c3 m13c0 m13c2 = refl
  holds2897 m13c1 m13c3 m13c0 m13c3 = refl
  holds2897 m13c1 m13c3 m13c1 m13c0 = refl
  holds2897 m13c1 m13c3 m13c1 m13c1 = refl
  holds2897 m13c1 m13c3 m13c1 m13c2 = refl
  holds2897 m13c1 m13c3 m13c1 m13c3 = refl
  holds2897 m13c1 m13c3 m13c2 m13c0 = refl
  holds2897 m13c1 m13c3 m13c2 m13c1 = refl
  holds2897 m13c1 m13c3 m13c2 m13c2 = refl
  holds2897 m13c1 m13c3 m13c2 m13c3 = refl
  holds2897 m13c1 m13c3 m13c3 m13c0 = refl
  holds2897 m13c1 m13c3 m13c3 m13c1 = refl
  holds2897 m13c1 m13c3 m13c3 m13c2 = refl
  holds2897 m13c1 m13c3 m13c3 m13c3 = refl
  holds2897 m13c2 m13c0 m13c0 m13c0 = refl
  holds2897 m13c2 m13c0 m13c0 m13c1 = refl
  holds2897 m13c2 m13c0 m13c0 m13c2 = refl
  holds2897 m13c2 m13c0 m13c0 m13c3 = refl
  holds2897 m13c2 m13c0 m13c1 m13c0 = refl
  holds2897 m13c2 m13c0 m13c1 m13c1 = refl
  holds2897 m13c2 m13c0 m13c1 m13c2 = refl
  holds2897 m13c2 m13c0 m13c1 m13c3 = refl
  holds2897 m13c2 m13c0 m13c2 m13c0 = refl
  holds2897 m13c2 m13c0 m13c2 m13c1 = refl
  holds2897 m13c2 m13c0 m13c2 m13c2 = refl
  holds2897 m13c2 m13c0 m13c2 m13c3 = refl
  holds2897 m13c2 m13c0 m13c3 m13c0 = refl
  holds2897 m13c2 m13c0 m13c3 m13c1 = refl
  holds2897 m13c2 m13c0 m13c3 m13c2 = refl
  holds2897 m13c2 m13c0 m13c3 m13c3 = refl
  holds2897 m13c2 m13c1 m13c0 m13c0 = refl
  holds2897 m13c2 m13c1 m13c0 m13c1 = refl
  holds2897 m13c2 m13c1 m13c0 m13c2 = refl
  holds2897 m13c2 m13c1 m13c0 m13c3 = refl
  holds2897 m13c2 m13c1 m13c1 m13c0 = refl
  holds2897 m13c2 m13c1 m13c1 m13c1 = refl
  holds2897 m13c2 m13c1 m13c1 m13c2 = refl
  holds2897 m13c2 m13c1 m13c1 m13c3 = refl
  holds2897 m13c2 m13c1 m13c2 m13c0 = refl
  holds2897 m13c2 m13c1 m13c2 m13c1 = refl
  holds2897 m13c2 m13c1 m13c2 m13c2 = refl
  holds2897 m13c2 m13c1 m13c2 m13c3 = refl
  holds2897 m13c2 m13c1 m13c3 m13c0 = refl
  holds2897 m13c2 m13c1 m13c3 m13c1 = refl
  holds2897 m13c2 m13c1 m13c3 m13c2 = refl
  holds2897 m13c2 m13c1 m13c3 m13c3 = refl
  holds2897 m13c2 m13c2 m13c0 m13c0 = refl
  holds2897 m13c2 m13c2 m13c0 m13c1 = refl
  holds2897 m13c2 m13c2 m13c0 m13c2 = refl
  holds2897 m13c2 m13c2 m13c0 m13c3 = refl
  holds2897 m13c2 m13c2 m13c1 m13c0 = refl
  holds2897 m13c2 m13c2 m13c1 m13c1 = refl
  holds2897 m13c2 m13c2 m13c1 m13c2 = refl
  holds2897 m13c2 m13c2 m13c1 m13c3 = refl
  holds2897 m13c2 m13c2 m13c2 m13c0 = refl
  holds2897 m13c2 m13c2 m13c2 m13c1 = refl
  holds2897 m13c2 m13c2 m13c2 m13c2 = refl
  holds2897 m13c2 m13c2 m13c2 m13c3 = refl
  holds2897 m13c2 m13c2 m13c3 m13c0 = refl
  holds2897 m13c2 m13c2 m13c3 m13c1 = refl
  holds2897 m13c2 m13c2 m13c3 m13c2 = refl
  holds2897 m13c2 m13c2 m13c3 m13c3 = refl
  holds2897 m13c2 m13c3 m13c0 m13c0 = refl
  holds2897 m13c2 m13c3 m13c0 m13c1 = refl
  holds2897 m13c2 m13c3 m13c0 m13c2 = refl
  holds2897 m13c2 m13c3 m13c0 m13c3 = refl
  holds2897 m13c2 m13c3 m13c1 m13c0 = refl
  holds2897 m13c2 m13c3 m13c1 m13c1 = refl
  holds2897 m13c2 m13c3 m13c1 m13c2 = refl
  holds2897 m13c2 m13c3 m13c1 m13c3 = refl
  holds2897 m13c2 m13c3 m13c2 m13c0 = refl
  holds2897 m13c2 m13c3 m13c2 m13c1 = refl
  holds2897 m13c2 m13c3 m13c2 m13c2 = refl
  holds2897 m13c2 m13c3 m13c2 m13c3 = refl
  holds2897 m13c2 m13c3 m13c3 m13c0 = refl
  holds2897 m13c2 m13c3 m13c3 m13c1 = refl
  holds2897 m13c2 m13c3 m13c3 m13c2 = refl
  holds2897 m13c2 m13c3 m13c3 m13c3 = refl
  holds2897 m13c3 m13c0 m13c0 m13c0 = refl
  holds2897 m13c3 m13c0 m13c0 m13c1 = refl
  holds2897 m13c3 m13c0 m13c0 m13c2 = refl
  holds2897 m13c3 m13c0 m13c0 m13c3 = refl
  holds2897 m13c3 m13c0 m13c1 m13c0 = refl
  holds2897 m13c3 m13c0 m13c1 m13c1 = refl
  holds2897 m13c3 m13c0 m13c1 m13c2 = refl
  holds2897 m13c3 m13c0 m13c1 m13c3 = refl
  holds2897 m13c3 m13c0 m13c2 m13c0 = refl
  holds2897 m13c3 m13c0 m13c2 m13c1 = refl
  holds2897 m13c3 m13c0 m13c2 m13c2 = refl
  holds2897 m13c3 m13c0 m13c2 m13c3 = refl
  holds2897 m13c3 m13c0 m13c3 m13c0 = refl
  holds2897 m13c3 m13c0 m13c3 m13c1 = refl
  holds2897 m13c3 m13c0 m13c3 m13c2 = refl
  holds2897 m13c3 m13c0 m13c3 m13c3 = refl
  holds2897 m13c3 m13c1 m13c0 m13c0 = refl
  holds2897 m13c3 m13c1 m13c0 m13c1 = refl
  holds2897 m13c3 m13c1 m13c0 m13c2 = refl
  holds2897 m13c3 m13c1 m13c0 m13c3 = refl
  holds2897 m13c3 m13c1 m13c1 m13c0 = refl
  holds2897 m13c3 m13c1 m13c1 m13c1 = refl
  holds2897 m13c3 m13c1 m13c1 m13c2 = refl
  holds2897 m13c3 m13c1 m13c1 m13c3 = refl
  holds2897 m13c3 m13c1 m13c2 m13c0 = refl
  holds2897 m13c3 m13c1 m13c2 m13c1 = refl
  holds2897 m13c3 m13c1 m13c2 m13c2 = refl
  holds2897 m13c3 m13c1 m13c2 m13c3 = refl
  holds2897 m13c3 m13c1 m13c3 m13c0 = refl
  holds2897 m13c3 m13c1 m13c3 m13c1 = refl
  holds2897 m13c3 m13c1 m13c3 m13c2 = refl
  holds2897 m13c3 m13c1 m13c3 m13c3 = refl
  holds2897 m13c3 m13c2 m13c0 m13c0 = refl
  holds2897 m13c3 m13c2 m13c0 m13c1 = refl
  holds2897 m13c3 m13c2 m13c0 m13c2 = refl
  holds2897 m13c3 m13c2 m13c0 m13c3 = refl
  holds2897 m13c3 m13c2 m13c1 m13c0 = refl
  holds2897 m13c3 m13c2 m13c1 m13c1 = refl
  holds2897 m13c3 m13c2 m13c1 m13c2 = refl
  holds2897 m13c3 m13c2 m13c1 m13c3 = refl
  holds2897 m13c3 m13c2 m13c2 m13c0 = refl
  holds2897 m13c3 m13c2 m13c2 m13c1 = refl
  holds2897 m13c3 m13c2 m13c2 m13c2 = refl
  holds2897 m13c3 m13c2 m13c2 m13c3 = refl
  holds2897 m13c3 m13c2 m13c3 m13c0 = refl
  holds2897 m13c3 m13c2 m13c3 m13c1 = refl
  holds2897 m13c3 m13c2 m13c3 m13c2 = refl
  holds2897 m13c3 m13c2 m13c3 m13c3 = refl
  holds2897 m13c3 m13c3 m13c0 m13c0 = refl
  holds2897 m13c3 m13c3 m13c0 m13c1 = refl
  holds2897 m13c3 m13c3 m13c0 m13c2 = refl
  holds2897 m13c3 m13c3 m13c0 m13c3 = refl
  holds2897 m13c3 m13c3 m13c1 m13c0 = refl
  holds2897 m13c3 m13c3 m13c1 m13c1 = refl
  holds2897 m13c3 m13c3 m13c1 m13c2 = refl
  holds2897 m13c3 m13c3 m13c1 m13c3 = refl
  holds2897 m13c3 m13c3 m13c2 m13c0 = refl
  holds2897 m13c3 m13c3 m13c2 m13c1 = refl
  holds2897 m13c3 m13c3 m13c2 m13c2 = refl
  holds2897 m13c3 m13c3 m13c2 m13c3 = refl
  holds2897 m13c3 m13c3 m13c3 m13c0 = refl
  holds2897 m13c3 m13c3 m13c3 m13c1 = refl
  holds2897 m13c3 m13c3 m13c3 m13c2 = refl
  holds2897 m13c3 m13c3 m13c3 m13c3 = refl
  cut2897 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 1) (op (op (var 2) (var 3)) (var 0)))) , (var 1)) → ⊥
  cut2897  = reject13 ((op (op (var 0) (var 1)) (op (var 1) (op (op (var 2) (var 3)) (var 0)))) , (var 1)) (λ env → holds2897 (env 0) (env 1) (env 2) (env 3))
  bad2898 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop (bop b1 b0) b0))) b1 → ⊥
  bad2898  p = false≢true (cong lower p)
  cut2898 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 1) (op (op (var 2) (var 3)) (var 0)))) , (var 2)) → ⊥
  cut2898  adequate = bad2898  (Adequate.valid adequate Two boolean env5)
  bad2899 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop (bop b0 b1) b0))) b1 → ⊥
  bad2899  p = false≢true (cong lower p)
  cut2899 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 1) (op (op (var 2) (var 3)) (var 0)))) , (var 3)) → ⊥
  cut2899  adequate = bad2899  (Adequate.valid adequate Two boolean env3)
  bad2900 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop (bop b0 b0) b0))) b1 → ⊥
  bad2900  p = false≢true (cong lower p)
  cut2900 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 1) (op (op (var 2) (var 3)) (var 0)))) , (var 4)) → ⊥
  cut2900  adequate = bad2900  (Adequate.valid adequate Two boolean env6)
  bad2901 : PathP (λ _ → Two) (bop (bop b0 b1) (bop b1 (bop (bop b1 b1) b1))) b0 → ⊥
  bad2901  p = false≢true (sym (cong lower p))
  cut2901 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 1) (op (op (var 2) (var 3)) (var 1)))) , (var 0)) → ⊥
  cut2901  adequate = bad2901  (Adequate.valid adequate Two boolean env12)
  bad2902 : PathP (λ _ → Two) (bop (bop b0 b1) (bop b1 (bop (bop b0 b0) b1))) b1 → ⊥
  bad2902  p = false≢true (cong lower p)
  cut2902 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 1) (op (op (var 2) (var 3)) (var 1)))) , (var 1)) → ⊥
  cut2902  adequate = bad2902  (Adequate.valid adequate Two boolean env4)
  bad2903 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop (bop b1 b0) b0))) b1 → ⊥
  bad2903  p = false≢true (cong lower p)
  cut2903 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 1) (op (op (var 2) (var 3)) (var 1)))) , (var 2)) → ⊥
  cut2903  adequate = bad2903  (Adequate.valid adequate Two boolean env5)
  bad2904 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop (bop b0 b1) b0))) b1 → ⊥
  bad2904  p = false≢true (cong lower p)
  cut2904 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 1) (op (op (var 2) (var 3)) (var 1)))) , (var 3)) → ⊥
  cut2904  adequate = bad2904  (Adequate.valid adequate Two boolean env3)
  bad2905 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop (bop b0 b0) b0))) b1 → ⊥
  bad2905  p = false≢true (cong lower p)
  cut2905 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 1) (op (op (var 2) (var 3)) (var 1)))) , (var 4)) → ⊥
  cut2905  adequate = bad2905  (Adequate.valid adequate Two boolean env6)
  bad2906 : PathP (λ _ → Two) (bop (bop b0 b1) (bop b1 (bop (bop b0 b0) b0))) b0 → ⊥
  bad2906  p = false≢true (sym (cong lower p))
  cut2906 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 1) (op (op (var 2) (var 3)) (var 2)))) , (var 0)) → ⊥
  cut2906  adequate = bad2906  (Adequate.valid adequate Two boolean env4)
  bad2907 : PathP (λ _ → Two) (bop (bop b0 b1) (bop b1 (bop (bop b1 b0) b1))) b1 → ⊥
  bad2907  p = false≢true (cong lower p)
  cut2907 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 1) (op (op (var 2) (var 3)) (var 2)))) , (var 1)) → ⊥
  cut2907  adequate = bad2907  (Adequate.valid adequate Two boolean env13)
  bad2908 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop (bop b1 b0) b1))) b1 → ⊥
  bad2908  p = false≢true (cong lower p)
  cut2908 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 1) (op (op (var 2) (var 3)) (var 2)))) , (var 2)) → ⊥
  cut2908  adequate = bad2908  (Adequate.valid adequate Two boolean env5)
  bad2909 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop (bop b0 b1) b0))) b1 → ⊥
  bad2909  p = false≢true (cong lower p)
  cut2909 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 1) (op (op (var 2) (var 3)) (var 2)))) , (var 3)) → ⊥
  cut2909  adequate = bad2909  (Adequate.valid adequate Two boolean env3)
  bad2910 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop (bop b0 b0) b0))) b1 → ⊥
  bad2910  p = false≢true (cong lower p)
  cut2910 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 1) (op (op (var 2) (var 3)) (var 2)))) , (var 4)) → ⊥
  cut2910  adequate = bad2910  (Adequate.valid adequate Two boolean env6)
  bad2911 : PathP (λ _ → Two) (bop (bop b0 b1) (bop b1 (bop (bop b0 b0) b0))) b0 → ⊥
  bad2911  p = false≢true (sym (cong lower p))
  cut2911 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 1) (op (op (var 2) (var 3)) (var 3)))) , (var 0)) → ⊥
  cut2911  adequate = bad2911  (Adequate.valid adequate Two boolean env4)
  bad2912 : PathP (λ _ → Two) (bop (bop b0 b1) (bop b1 (bop (bop b0 b1) b1))) b1 → ⊥
  bad2912  p = false≢true (cong lower p)
  cut2912 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 1) (op (op (var 2) (var 3)) (var 3)))) , (var 1)) → ⊥
  cut2912  adequate = bad2912  (Adequate.valid adequate Two boolean env10)
  bad2913 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop (bop b1 b0) b0))) b1 → ⊥
  bad2913  p = false≢true (cong lower p)
  cut2913 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 1) (op (op (var 2) (var 3)) (var 3)))) , (var 2)) → ⊥
  cut2913  adequate = bad2913  (Adequate.valid adequate Two boolean env5)
  bad2914 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop (bop b0 b1) b1))) b1 → ⊥
  bad2914  p = false≢true (cong lower p)
  cut2914 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 1) (op (op (var 2) (var 3)) (var 3)))) , (var 3)) → ⊥
  cut2914  adequate = bad2914  (Adequate.valid adequate Two boolean env3)
  bad2915 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop (bop b0 b0) b0))) b1 → ⊥
  bad2915  p = false≢true (cong lower p)
  cut2915 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 1) (op (op (var 2) (var 3)) (var 3)))) , (var 4)) → ⊥
  cut2915  adequate = bad2915  (Adequate.valid adequate Two boolean env6)
  bad2916 : PathP (λ _ → Two) (bop (bop b0 b1) (bop b1 (bop (bop b0 b0) b0))) b0 → ⊥
  bad2916  p = false≢true (sym (cong lower p))
  cut2916 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 1) (op (op (var 2) (var 3)) (var 4)))) , (var 0)) → ⊥
  cut2916  adequate = bad2916  (Adequate.valid adequate Two boolean env14)
  bad2917 : PathP (λ _ → Two) (bop (bop b0 b1) (bop b1 (bop (bop b0 b0) b1))) b1 → ⊥
  bad2917  p = false≢true (cong lower p)
  cut2917 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 1) (op (op (var 2) (var 3)) (var 4)))) , (var 1)) → ⊥
  cut2917  adequate = bad2917  (Adequate.valid adequate Two boolean env15)
  bad2918 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop (bop b1 b0) b0))) b1 → ⊥
  bad2918  p = false≢true (cong lower p)
  cut2918 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 1) (op (op (var 2) (var 3)) (var 4)))) , (var 2)) → ⊥
  cut2918  adequate = bad2918  (Adequate.valid adequate Two boolean env16)
  bad2919 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop (bop b0 b1) b0))) b1 → ⊥
  bad2919  p = false≢true (cong lower p)
  cut2919 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 1) (op (op (var 2) (var 3)) (var 4)))) , (var 3)) → ⊥
  cut2919  adequate = bad2919  (Adequate.valid adequate Two boolean env17)
  bad2920 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop (bop b0 b0) b1))) b1 → ⊥
  bad2920  p = false≢true (cong lower p)
  cut2920 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 1) (op (op (var 2) (var 3)) (var 4)))) , (var 4)) → ⊥
  cut2920  adequate = bad2920  (Adequate.valid adequate Two boolean env6)
  bad2921 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop (bop b0 b0) b0))) b1 → ⊥
  bad2921  p = false≢true (cong lower p)
  cut2921 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 1) (op (op (var 2) (var 3)) (var 4)))) , (var 5)) → ⊥
  cut2921  adequate = bad2921  (Adequate.valid adequate Two boolean env18)
  bad2922 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b1 (bop (bop b0 b0) b0))) b0 → ⊥
  bad2922  p = false≢true (sym (cong lower p))
  cut2922 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (op (var 0) (var 0)) (var 0)))) , (var 0)) → ⊥
  cut2922  adequate = bad2922  (Adequate.valid adequate Two boolean env1)
  bad2923 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b1 (bop (bop b0 b0) b0))) b0 → ⊥
  bad2923  p = false≢true (sym (cong lower p))
  cut2923 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (op (var 0) (var 0)) (var 0)))) , (var 1)) → ⊥
  cut2923  adequate = bad2923  (Adequate.valid adequate Two boolean env1)
  env23 : ℕ → Two
  env23 zero = b1
  env23 (suc zero) = b1
  env23 (suc (suc zero)) = b0
  env23 (suc (suc (suc rest))) = b0
  bad2924 : PathP (λ _ → Two) (bop (bop b1 b1) (bop b0 (bop (bop b1 b1) b1))) b0 → ⊥
  bad2924  p = false≢true (sym (cong lower p))
  cut2924 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (op (var 0) (var 0)) (var 0)))) , (var 2)) → ⊥
  cut2924  adequate = bad2924  (Adequate.valid adequate Two boolean env23)
  bad2925 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop (bop b0 b0) b0))) b1 → ⊥
  bad2925  p = false≢true (cong lower p)
  cut2925 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (op (var 0) (var 0)) (var 0)))) , (var 3)) → ⊥
  cut2925  adequate = bad2925  (Adequate.valid adequate Two boolean env3)
  bad2926 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b1 (bop (bop b0 b0) b0))) b0 → ⊥
  bad2926  p = false≢true (sym (cong lower p))
  cut2926 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (op (var 0) (var 0)) (var 1)))) , (var 0)) → ⊥
  cut2926  adequate = bad2926  (Adequate.valid adequate Two boolean env1)
  bad2927 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b1 (bop (bop b0 b0) b0))) b0 → ⊥
  bad2927  p = false≢true (sym (cong lower p))
  cut2927 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (op (var 0) (var 0)) (var 1)))) , (var 1)) → ⊥
  cut2927  adequate = bad2927  (Adequate.valid adequate Two boolean env1)
  bad2928 : PathP (λ _ → Two) (bop (bop b0 b1) (bop b1 (bop (bop b0 b0) b1))) b1 → ⊥
  bad2928  p = false≢true (cong lower p)
  cut2928 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (op (var 0) (var 0)) (var 1)))) , (var 2)) → ⊥
  cut2928  adequate = bad2928  (Adequate.valid adequate Two boolean env8)
  bad2929 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop (bop b0 b0) b0))) b1 → ⊥
  bad2929  p = false≢true (cong lower p)
  cut2929 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (op (var 0) (var 0)) (var 1)))) , (var 3)) → ⊥
  cut2929  adequate = bad2929  (Adequate.valid adequate Two boolean env3)
  bad2930 : PathP (λ _ → Two) (bop (bop b1 b0) (bop b0 (bop (bop b1 b1) b0))) b1 → ⊥
  bad2930  p = false≢true (cong lower p)
  cut2930 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (op (var 0) (var 0)) (var 2)))) , (var 0)) → ⊥
  cut2930  adequate = bad2930  (Adequate.valid adequate Two boolean env9)
  bad2931 : PathP (λ _ → Two) (bop (bop b0 b1) (bop b0 (bop (bop b0 b0) b0))) b1 → ⊥
  bad2931  p = false≢true (cong lower p)
  cut2931 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (op (var 0) (var 0)) (var 2)))) , (var 1)) → ⊥
  cut2931  adequate = bad2931  (Adequate.valid adequate Two boolean env2)
  bad2932 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b1 (bop (bop b0 b0) b1))) b1 → ⊥
  bad2932  p = false≢true (cong lower p)
  cut2932 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (op (var 0) (var 0)) (var 2)))) , (var 2)) → ⊥
  cut2932  adequate = bad2932  (Adequate.valid adequate Two boolean env1)
  bad2933 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop (bop b0 b0) b0))) b1 → ⊥
  bad2933  p = false≢true (cong lower p)
  cut2933 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (op (var 0) (var 0)) (var 2)))) , (var 3)) → ⊥
  cut2933  adequate = bad2933  (Adequate.valid adequate Two boolean env3)
  bad2934 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b1 (bop (bop b0 b0) b0))) b0 → ⊥
  bad2934  p = false≢true (sym (cong lower p))
  cut2934 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (op (var 0) (var 0)) (var 3)))) , (var 0)) → ⊥
  cut2934  adequate = bad2934  (Adequate.valid adequate Two boolean env5)
  bad2935 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b1 (bop (bop b0 b0) b0))) b0 → ⊥
  bad2935  p = false≢true (sym (cong lower p))
  cut2935 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (op (var 0) (var 0)) (var 3)))) , (var 1)) → ⊥
  cut2935  adequate = bad2935  (Adequate.valid adequate Two boolean env5)
  env24 : ℕ → Two
  env24 zero = b0
  env24 (suc zero) = b0
  env24 (suc (suc zero)) = b1
  env24 (suc (suc (suc zero))) = b1
  env24 (suc (suc (suc (suc rest)))) = b0
  bad2936 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b1 (bop (bop b0 b0) b1))) b1 → ⊥
  bad2936  p = false≢true (cong lower p)
  cut2936 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (op (var 0) (var 0)) (var 3)))) , (var 2)) → ⊥
  cut2936  adequate = bad2936  (Adequate.valid adequate Two boolean env24)
  bad2937 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop (bop b0 b0) b1))) b1 → ⊥
  bad2937  p = false≢true (cong lower p)
  cut2937 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (op (var 0) (var 0)) (var 3)))) , (var 3)) → ⊥
  cut2937  adequate = bad2937  (Adequate.valid adequate Two boolean env3)
  bad2938 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop (bop b0 b0) b0))) b1 → ⊥
  bad2938  p = false≢true (cong lower p)
  cut2938 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (op (var 0) (var 0)) (var 3)))) , (var 4)) → ⊥
  cut2938  adequate = bad2938  (Adequate.valid adequate Two boolean env6)
  bad2939 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b1 (bop (bop b0 b0) b0))) b0 → ⊥
  bad2939  p = false≢true (sym (cong lower p))
  cut2939 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (op (var 0) (var 1)) (var 0)))) , (var 0)) → ⊥
  cut2939  adequate = bad2939  (Adequate.valid adequate Two boolean env1)
  bad2940 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b1 (bop (bop b0 b0) b0))) b0 → ⊥
  bad2940  p = false≢true (sym (cong lower p))
  cut2940 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (op (var 0) (var 1)) (var 0)))) , (var 1)) → ⊥
  cut2940  adequate = bad2940  (Adequate.valid adequate Two boolean env1)
  bad2941 : PathP (λ _ → Two) (bop (bop b1 b0) (bop b1 (bop (bop b1 b0) b1))) b1 → ⊥
  bad2941  p = false≢true (cong lower p)
  cut2941 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (op (var 0) (var 1)) (var 0)))) , (var 2)) → ⊥
  cut2941  adequate = bad2941  (Adequate.valid adequate Two boolean env19)
  bad2942 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop (bop b0 b0) b0))) b1 → ⊥
  bad2942  p = false≢true (cong lower p)
  cut2942 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (op (var 0) (var 1)) (var 0)))) , (var 3)) → ⊥
  cut2942  adequate = bad2942  (Adequate.valid adequate Two boolean env3)
  bad2943 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b1 (bop (bop b0 b0) b0))) b0 → ⊥
  bad2943  p = false≢true (sym (cong lower p))
  cut2943 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (op (var 0) (var 1)) (var 1)))) , (var 0)) → ⊥
  cut2943  adequate = bad2943  (Adequate.valid adequate Two boolean env1)
  bad2944 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b1 (bop (bop b0 b0) b0))) b0 → ⊥
  bad2944  p = false≢true (sym (cong lower p))
  cut2944 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (op (var 0) (var 1)) (var 1)))) , (var 1)) → ⊥
  cut2944  adequate = bad2944  (Adequate.valid adequate Two boolean env1)
  bad2945 : PathP (λ _ → Two) (bop (bop b0 b1) (bop b1 (bop (bop b0 b1) b1))) b1 → ⊥
  bad2945  p = false≢true (cong lower p)
  cut2945 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (op (var 0) (var 1)) (var 1)))) , (var 2)) → ⊥
  cut2945  adequate = bad2945  (Adequate.valid adequate Two boolean env8)
  bad2946 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop (bop b0 b0) b0))) b1 → ⊥
  bad2946  p = false≢true (cong lower p)
  cut2946 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (op (var 0) (var 1)) (var 1)))) , (var 3)) → ⊥
  cut2946  adequate = bad2946  (Adequate.valid adequate Two boolean env3)
  bad2947 : PathP (λ _ → Two) (bop (bop b1 b0) (bop b0 (bop (bop b1 b0) b0))) b1 → ⊥
  bad2947  p = false≢true (cong lower p)
  cut2947 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (op (var 0) (var 1)) (var 2)))) , (var 0)) → ⊥
  cut2947  adequate = bad2947  (Adequate.valid adequate Two boolean env9)
  bad2948 : PathP (λ _ → Two) (bop (bop b0 b1) (bop b0 (bop (bop b0 b1) b0))) b1 → ⊥
  bad2948  p = false≢true (cong lower p)
  cut2948 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (op (var 0) (var 1)) (var 2)))) , (var 1)) → ⊥
  cut2948  adequate = bad2948  (Adequate.valid adequate Two boolean env2)
  bad2949 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b1 (bop (bop b0 b0) b1))) b1 → ⊥
  bad2949  p = false≢true (cong lower p)
  cut2949 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (op (var 0) (var 1)) (var 2)))) , (var 2)) → ⊥
  cut2949  adequate = bad2949  (Adequate.valid adequate Two boolean env1)
  bad2950 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop (bop b0 b0) b0))) b1 → ⊥
  bad2950  p = false≢true (cong lower p)
  cut2950 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (op (var 0) (var 1)) (var 2)))) , (var 3)) → ⊥
  cut2950  adequate = bad2950  (Adequate.valid adequate Two boolean env3)
  bad2951 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b1 (bop (bop b0 b0) b0))) b0 → ⊥
  bad2951  p = false≢true (sym (cong lower p))
  cut2951 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (op (var 0) (var 1)) (var 3)))) , (var 0)) → ⊥
  cut2951  adequate = bad2951  (Adequate.valid adequate Two boolean env5)
  bad2952 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b1 (bop (bop b0 b0) b0))) b0 → ⊥
  bad2952  p = false≢true (sym (cong lower p))
  cut2952 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (op (var 0) (var 1)) (var 3)))) , (var 1)) → ⊥
  cut2952  adequate = bad2952  (Adequate.valid adequate Two boolean env5)
  bad2953 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b1 (bop (bop b0 b0) b1))) b1 → ⊥
  bad2953  p = false≢true (cong lower p)
  cut2953 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (op (var 0) (var 1)) (var 3)))) , (var 2)) → ⊥
  cut2953  adequate = bad2953  (Adequate.valid adequate Two boolean env24)
  bad2954 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop (bop b0 b0) b1))) b1 → ⊥
  bad2954  p = false≢true (cong lower p)
  cut2954 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (op (var 0) (var 1)) (var 3)))) , (var 3)) → ⊥
  cut2954  adequate = bad2954  (Adequate.valid adequate Two boolean env3)
  bad2955 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop (bop b0 b0) b0))) b1 → ⊥
  bad2955  p = false≢true (cong lower p)
  cut2955 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (op (var 0) (var 1)) (var 3)))) , (var 4)) → ⊥
  cut2955  adequate = bad2955  (Adequate.valid adequate Two boolean env6)
  bad2956 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b1 (bop (bop b0 b1) b0))) b0 → ⊥
  bad2956  p = false≢true (sym (cong lower p))
  cut2956 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (op (var 0) (var 2)) (var 0)))) , (var 0)) → ⊥
  cut2956  adequate = bad2956  (Adequate.valid adequate Two boolean env1)
  bad2957 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b1 (bop (bop b0 b1) b0))) b0 → ⊥
  bad2957  p = false≢true (sym (cong lower p))
  cut2957 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (op (var 0) (var 2)) (var 0)))) , (var 1)) → ⊥
  cut2957  adequate = bad2957  (Adequate.valid adequate Two boolean env1)
  bad2958 : PathP (λ _ → Two) (bop (bop b1 b1) (bop b0 (bop (bop b1 b0) b1))) b0 → ⊥
  bad2958  p = false≢true (sym (cong lower p))
  cut2958 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (op (var 0) (var 2)) (var 0)))) , (var 2)) → ⊥
  cut2958  adequate = bad2958  (Adequate.valid adequate Two boolean env23)
  bad2959 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop (bop b0 b0) b0))) b1 → ⊥
  bad2959  p = false≢true (cong lower p)
  cut2959 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (op (var 0) (var 2)) (var 0)))) , (var 3)) → ⊥
  cut2959  adequate = bad2959  (Adequate.valid adequate Two boolean env3)
  bad2960 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b1 (bop (bop b0 b1) b0))) b0 → ⊥
  bad2960  p = false≢true (sym (cong lower p))
  cut2960 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (op (var 0) (var 2)) (var 1)))) , (var 0)) → ⊥
  cut2960  adequate = bad2960  (Adequate.valid adequate Two boolean env1)
  bad2961 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b1 (bop (bop b0 b1) b0))) b0 → ⊥
  bad2961  p = false≢true (sym (cong lower p))
  cut2961 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (op (var 0) (var 2)) (var 1)))) , (var 1)) → ⊥
  cut2961  adequate = bad2961  (Adequate.valid adequate Two boolean env1)
  bad2962 : PathP (λ _ → Two) (bop (bop b0 b1) (bop b1 (bop (bop b0 b1) b1))) b1 → ⊥
  bad2962  p = false≢true (cong lower p)
  cut2962 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (op (var 0) (var 2)) (var 1)))) , (var 2)) → ⊥
  cut2962  adequate = bad2962  (Adequate.valid adequate Two boolean env8)
  bad2963 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop (bop b0 b0) b0))) b1 → ⊥
  bad2963  p = false≢true (cong lower p)
  cut2963 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (op (var 0) (var 2)) (var 1)))) , (var 3)) → ⊥
  cut2963  adequate = bad2963  (Adequate.valid adequate Two boolean env3)
  bad2964 : PathP (λ _ → Two) (bop (bop b1 b0) (bop b0 (bop (bop b1 b0) b0))) b1 → ⊥
  bad2964  p = false≢true (cong lower p)
  cut2964 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (op (var 0) (var 2)) (var 2)))) , (var 0)) → ⊥
  cut2964  adequate = bad2964  (Adequate.valid adequate Two boolean env9)
  bad2965 : PathP (λ _ → Two) (bop (bop b0 b1) (bop b0 (bop (bop b0 b0) b0))) b1 → ⊥
  bad2965  p = false≢true (cong lower p)
  cut2965 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (op (var 0) (var 2)) (var 2)))) , (var 1)) → ⊥
  cut2965  adequate = bad2965  (Adequate.valid adequate Two boolean env2)
  bad2966 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b1 (bop (bop b0 b1) b1))) b1 → ⊥
  bad2966  p = false≢true (cong lower p)
  cut2966 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (op (var 0) (var 2)) (var 2)))) , (var 2)) → ⊥
  cut2966  adequate = bad2966  (Adequate.valid adequate Two boolean env1)
  bad2967 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop (bop b0 b0) b0))) b1 → ⊥
  bad2967  p = false≢true (cong lower p)
  cut2967 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (op (var 0) (var 2)) (var 2)))) , (var 3)) → ⊥
  cut2967  adequate = bad2967  (Adequate.valid adequate Two boolean env3)
  bad2968 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b1 (bop (bop b0 b1) b0))) b0 → ⊥
  bad2968  p = false≢true (sym (cong lower p))
  cut2968 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (op (var 0) (var 2)) (var 3)))) , (var 0)) → ⊥
  cut2968  adequate = bad2968  (Adequate.valid adequate Two boolean env5)
  bad2969 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b1 (bop (bop b0 b1) b0))) b0 → ⊥
  bad2969  p = false≢true (sym (cong lower p))
  cut2969 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (op (var 0) (var 2)) (var 3)))) , (var 1)) → ⊥
  cut2969  adequate = bad2969  (Adequate.valid adequate Two boolean env5)
  bad2970 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b1 (bop (bop b0 b1) b1))) b1 → ⊥
  bad2970  p = false≢true (cong lower p)
  cut2970 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (op (var 0) (var 2)) (var 3)))) , (var 2)) → ⊥
  cut2970  adequate = bad2970  (Adequate.valid adequate Two boolean env24)
  bad2971 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop (bop b0 b0) b1))) b1 → ⊥
  bad2971  p = false≢true (cong lower p)
  cut2971 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (op (var 0) (var 2)) (var 3)))) , (var 3)) → ⊥
  cut2971  adequate = bad2971  (Adequate.valid adequate Two boolean env3)
  bad2972 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop (bop b0 b0) b0))) b1 → ⊥
  bad2972  p = false≢true (cong lower p)
  cut2972 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (op (var 0) (var 2)) (var 3)))) , (var 4)) → ⊥
  cut2972  adequate = bad2972  (Adequate.valid adequate Two boolean env6)
  bad2973 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b1 (bop (bop b0 b0) b0))) b0 → ⊥
  bad2973  p = false≢true (sym (cong lower p))
  cut2973 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (op (var 0) (var 3)) (var 0)))) , (var 0)) → ⊥
  cut2973  adequate = bad2973  (Adequate.valid adequate Two boolean env5)
  bad2974 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b1 (bop (bop b0 b0) b0))) b0 → ⊥
  bad2974  p = false≢true (sym (cong lower p))
  cut2974 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (op (var 0) (var 3)) (var 0)))) , (var 1)) → ⊥
  cut2974  adequate = bad2974  (Adequate.valid adequate Two boolean env5)
  bad2975 : PathP (λ _ → Two) (bop (bop b1 b0) (bop b1 (bop (bop b1 b0) b1))) b1 → ⊥
  bad2975  p = false≢true (cong lower p)
  cut2975 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (op (var 0) (var 3)) (var 0)))) , (var 2)) → ⊥
  cut2975  adequate = bad2975  (Adequate.valid adequate Two boolean env21)
  bad2976 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop (bop b0 b1) b0))) b1 → ⊥
  bad2976  p = false≢true (cong lower p)
  cut2976 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (op (var 0) (var 3)) (var 0)))) , (var 3)) → ⊥
  cut2976  adequate = bad2976  (Adequate.valid adequate Two boolean env3)
  bad2977 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop (bop b0 b0) b0))) b1 → ⊥
  bad2977  p = false≢true (cong lower p)
  cut2977 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (op (var 0) (var 3)) (var 0)))) , (var 4)) → ⊥
  cut2977  adequate = bad2977  (Adequate.valid adequate Two boolean env6)
  bad2978 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b1 (bop (bop b0 b0) b0))) b0 → ⊥
  bad2978  p = false≢true (sym (cong lower p))
  cut2978 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (op (var 0) (var 3)) (var 1)))) , (var 0)) → ⊥
  cut2978  adequate = bad2978  (Adequate.valid adequate Two boolean env5)
  bad2979 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b1 (bop (bop b0 b0) b0))) b0 → ⊥
  bad2979  p = false≢true (sym (cong lower p))
  cut2979 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (op (var 0) (var 3)) (var 1)))) , (var 1)) → ⊥
  cut2979  adequate = bad2979  (Adequate.valid adequate Two boolean env5)
  bad2980 : PathP (λ _ → Two) (bop (bop b0 b1) (bop b1 (bop (bop b0 b0) b1))) b1 → ⊥
  bad2980  p = false≢true (cong lower p)
  cut2980 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (op (var 0) (var 3)) (var 1)))) , (var 2)) → ⊥
  cut2980  adequate = bad2980  (Adequate.valid adequate Two boolean env13)
  bad2981 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop (bop b0 b1) b0))) b1 → ⊥
  bad2981  p = false≢true (cong lower p)
  cut2981 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (op (var 0) (var 3)) (var 1)))) , (var 3)) → ⊥
  cut2981  adequate = bad2981  (Adequate.valid adequate Two boolean env3)
  bad2982 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop (bop b0 b0) b0))) b1 → ⊥
  bad2982  p = false≢true (cong lower p)
  cut2982 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (op (var 0) (var 3)) (var 1)))) , (var 4)) → ⊥
  cut2982  adequate = bad2982  (Adequate.valid adequate Two boolean env6)
  bad2983 : PathP (λ _ → Two) (bop (bop b1 b0) (bop b0 (bop (bop b1 b0) b0))) b1 → ⊥
  bad2983  p = false≢true (cong lower p)
  cut2983 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (op (var 0) (var 3)) (var 2)))) , (var 0)) → ⊥
  cut2983  adequate = bad2983  (Adequate.valid adequate Two boolean env11)
  bad2984 : PathP (λ _ → Two) (bop (bop b0 b1) (bop b0 (bop (bop b0 b0) b0))) b1 → ⊥
  bad2984  p = false≢true (cong lower p)
  cut2984 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (op (var 0) (var 3)) (var 2)))) , (var 1)) → ⊥
  cut2984  adequate = bad2984  (Adequate.valid adequate Two boolean env4)
  bad2985 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b1 (bop (bop b0 b0) b1))) b1 → ⊥
  bad2985  p = false≢true (cong lower p)
  cut2985 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (op (var 0) (var 3)) (var 2)))) , (var 2)) → ⊥
  cut2985  adequate = bad2985  (Adequate.valid adequate Two boolean env5)
  bad2986 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop (bop b0 b1) b0))) b1 → ⊥
  bad2986  p = false≢true (cong lower p)
  cut2986 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (op (var 0) (var 3)) (var 2)))) , (var 3)) → ⊥
  cut2986  adequate = bad2986  (Adequate.valid adequate Two boolean env3)
  bad2987 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop (bop b0 b0) b0))) b1 → ⊥
  bad2987  p = false≢true (cong lower p)
  cut2987 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (op (var 0) (var 3)) (var 2)))) , (var 4)) → ⊥
  cut2987  adequate = bad2987  (Adequate.valid adequate Two boolean env6)
  bad2988 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b1 (bop (bop b0 b0) b0))) b0 → ⊥
  bad2988  p = false≢true (sym (cong lower p))
  cut2988 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (op (var 0) (var 3)) (var 3)))) , (var 0)) → ⊥
  cut2988  adequate = bad2988  (Adequate.valid adequate Two boolean env5)
  bad2989 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b1 (bop (bop b0 b0) b0))) b0 → ⊥
  bad2989  p = false≢true (sym (cong lower p))
  cut2989 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (op (var 0) (var 3)) (var 3)))) , (var 1)) → ⊥
  cut2989  adequate = bad2989  (Adequate.valid adequate Two boolean env5)
  bad2990 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b1 (bop (bop b0 b1) b1))) b1 → ⊥
  bad2990  p = false≢true (cong lower p)
  cut2990 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (op (var 0) (var 3)) (var 3)))) , (var 2)) → ⊥
  cut2990  adequate = bad2990  (Adequate.valid adequate Two boolean env24)
  bad2991 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop (bop b0 b1) b1))) b1 → ⊥
  bad2991  p = false≢true (cong lower p)
  cut2991 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (op (var 0) (var 3)) (var 3)))) , (var 3)) → ⊥
  cut2991  adequate = bad2991  (Adequate.valid adequate Two boolean env3)
  bad2992 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop (bop b0 b0) b0))) b1 → ⊥
  bad2992  p = false≢true (cong lower p)
  cut2992 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (op (var 0) (var 3)) (var 3)))) , (var 4)) → ⊥
  cut2992  adequate = bad2992  (Adequate.valid adequate Two boolean env6)
  bad2993 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b1 (bop (bop b0 b0) b0))) b0 → ⊥
  bad2993  p = false≢true (sym (cong lower p))
  cut2993 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (op (var 0) (var 3)) (var 4)))) , (var 0)) → ⊥
  cut2993  adequate = bad2993  (Adequate.valid adequate Two boolean env16)
  bad2994 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b1 (bop (bop b0 b0) b0))) b0 → ⊥
  bad2994  p = false≢true (sym (cong lower p))
  cut2994 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (op (var 0) (var 3)) (var 4)))) , (var 1)) → ⊥
  cut2994  adequate = bad2994  (Adequate.valid adequate Two boolean env16)
  env25 : ℕ → Two
  env25 zero = b0
  env25 (suc zero) = b0
  env25 (suc (suc zero)) = b1
  env25 (suc (suc (suc zero))) = b0
  env25 (suc (suc (suc (suc zero)))) = b1
  env25 (suc (suc (suc (suc (suc rest))))) = b0
  bad2995 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b1 (bop (bop b0 b0) b1))) b1 → ⊥
  bad2995  p = false≢true (cong lower p)
  cut2995 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (op (var 0) (var 3)) (var 4)))) , (var 2)) → ⊥
  cut2995  adequate = bad2995  (Adequate.valid adequate Two boolean env25)
  bad2996 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop (bop b0 b1) b0))) b1 → ⊥
  bad2996  p = false≢true (cong lower p)
  cut2996 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (op (var 0) (var 3)) (var 4)))) , (var 3)) → ⊥
  cut2996  adequate = bad2996  (Adequate.valid adequate Two boolean env17)
  bad2997 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop (bop b0 b0) b1))) b1 → ⊥
  bad2997  p = false≢true (cong lower p)
  cut2997 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (op (var 0) (var 3)) (var 4)))) , (var 4)) → ⊥
  cut2997  adequate = bad2997  (Adequate.valid adequate Two boolean env6)
  bad2998 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop (bop b0 b0) b0))) b1 → ⊥
  bad2998  p = false≢true (cong lower p)
  cut2998 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (op (var 0) (var 3)) (var 4)))) , (var 5)) → ⊥
  cut2998  adequate = bad2998  (Adequate.valid adequate Two boolean env18)
  bad2999 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b1 (bop (bop b0 b0) b0))) b0 → ⊥
  bad2999  p = false≢true (sym (cong lower p))
  cut2999 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (op (var 1) (var 0)) (var 0)))) , (var 0)) → ⊥
  cut2999  adequate = bad2999  (Adequate.valid adequate Two boolean env1)
  bad3000 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b1 (bop (bop b0 b0) b0))) b0 → ⊥
  bad3000  p = false≢true (sym (cong lower p))
  cut3000 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (op (var 1) (var 0)) (var 0)))) , (var 1)) → ⊥
  cut3000  adequate = bad3000  (Adequate.valid adequate Two boolean env1)
  bad3001 : PathP (λ _ → Two) (bop (bop b1 b0) (bop b1 (bop (bop b0 b1) b1))) b1 → ⊥
  bad3001  p = false≢true (cong lower p)
  cut3001 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (op (var 1) (var 0)) (var 0)))) , (var 2)) → ⊥
  cut3001  adequate = bad3001  (Adequate.valid adequate Two boolean env19)
  bad3002 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop (bop b0 b0) b0))) b1 → ⊥
  bad3002  p = false≢true (cong lower p)
  cut3002 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (op (var 1) (var 0)) (var 0)))) , (var 3)) → ⊥
  cut3002  adequate = bad3002  (Adequate.valid adequate Two boolean env3)
  bad3003 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b1 (bop (bop b0 b0) b0))) b0 → ⊥
  bad3003  p = false≢true (sym (cong lower p))
  cut3003 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (op (var 1) (var 0)) (var 1)))) , (var 0)) → ⊥
  cut3003  adequate = bad3003  (Adequate.valid adequate Two boolean env1)
  bad3004 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b1 (bop (bop b0 b0) b0))) b0 → ⊥
  bad3004  p = false≢true (sym (cong lower p))
  cut3004 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (op (var 1) (var 0)) (var 1)))) , (var 1)) → ⊥
  cut3004  adequate = bad3004  (Adequate.valid adequate Two boolean env1)
  bad3005 : PathP (λ _ → Two) (bop (bop b0 b1) (bop b1 (bop (bop b1 b0) b1))) b1 → ⊥
  bad3005  p = false≢true (cong lower p)
  cut3005 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (op (var 1) (var 0)) (var 1)))) , (var 2)) → ⊥
  cut3005  adequate = bad3005  (Adequate.valid adequate Two boolean env8)
  bad3006 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop (bop b0 b0) b0))) b1 → ⊥
  bad3006  p = false≢true (cong lower p)
  cut3006 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (op (var 1) (var 0)) (var 1)))) , (var 3)) → ⊥
  cut3006  adequate = bad3006  (Adequate.valid adequate Two boolean env3)
  bad3007 : PathP (λ _ → Two) (bop (bop b1 b0) (bop b0 (bop (bop b0 b1) b0))) b1 → ⊥
  bad3007  p = false≢true (cong lower p)
  cut3007 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (op (var 1) (var 0)) (var 2)))) , (var 0)) → ⊥
  cut3007  adequate = bad3007  (Adequate.valid adequate Two boolean env9)
  bad3008 : PathP (λ _ → Two) (bop (bop b0 b1) (bop b0 (bop (bop b1 b0) b0))) b1 → ⊥
  bad3008  p = false≢true (cong lower p)
  cut3008 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (op (var 1) (var 0)) (var 2)))) , (var 1)) → ⊥
  cut3008  adequate = bad3008  (Adequate.valid adequate Two boolean env2)
  bad3009 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b1 (bop (bop b0 b0) b1))) b1 → ⊥
  bad3009  p = false≢true (cong lower p)
  cut3009 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (op (var 1) (var 0)) (var 2)))) , (var 2)) → ⊥
  cut3009  adequate = bad3009  (Adequate.valid adequate Two boolean env1)
  bad3010 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop (bop b0 b0) b0))) b1 → ⊥
  bad3010  p = false≢true (cong lower p)
  cut3010 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (op (var 1) (var 0)) (var 2)))) , (var 3)) → ⊥
  cut3010  adequate = bad3010  (Adequate.valid adequate Two boolean env3)
  bad3011 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b1 (bop (bop b0 b0) b0))) b0 → ⊥
  bad3011  p = false≢true (sym (cong lower p))
  cut3011 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (op (var 1) (var 0)) (var 3)))) , (var 0)) → ⊥
  cut3011  adequate = bad3011  (Adequate.valid adequate Two boolean env5)
  bad3012 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b1 (bop (bop b0 b0) b0))) b0 → ⊥
  bad3012  p = false≢true (sym (cong lower p))
  cut3012 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (op (var 1) (var 0)) (var 3)))) , (var 1)) → ⊥
  cut3012  adequate = bad3012  (Adequate.valid adequate Two boolean env5)
  bad3013 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b1 (bop (bop b0 b0) b1))) b1 → ⊥
  bad3013  p = false≢true (cong lower p)
  cut3013 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (op (var 1) (var 0)) (var 3)))) , (var 2)) → ⊥
  cut3013  adequate = bad3013  (Adequate.valid adequate Two boolean env24)
  bad3014 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop (bop b0 b0) b1))) b1 → ⊥
  bad3014  p = false≢true (cong lower p)
  cut3014 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (op (var 1) (var 0)) (var 3)))) , (var 3)) → ⊥
  cut3014  adequate = bad3014  (Adequate.valid adequate Two boolean env3)
  bad3015 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop (bop b0 b0) b0))) b1 → ⊥
  bad3015  p = false≢true (cong lower p)
  cut3015 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (op (var 1) (var 0)) (var 3)))) , (var 4)) → ⊥
  cut3015  adequate = bad3015  (Adequate.valid adequate Two boolean env6)
  bad3016 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b1 (bop (bop b0 b0) b0))) b0 → ⊥
  bad3016  p = false≢true (sym (cong lower p))
  cut3016 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (op (var 1) (var 1)) (var 0)))) , (var 0)) → ⊥
  cut3016  adequate = bad3016  (Adequate.valid adequate Two boolean env1)
  bad3017 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b1 (bop (bop b0 b0) b0))) b0 → ⊥
  bad3017  p = false≢true (sym (cong lower p))
  cut3017 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (op (var 1) (var 1)) (var 0)))) , (var 1)) → ⊥
  cut3017  adequate = bad3017  (Adequate.valid adequate Two boolean env1)
  bad3018 : PathP (λ _ → Two) (bop (bop b1 b0) (bop b1 (bop (bop b0 b0) b1))) b1 → ⊥
  bad3018  p = false≢true (cong lower p)
  cut3018 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (op (var 1) (var 1)) (var 0)))) , (var 2)) → ⊥
  cut3018  adequate = bad3018  (Adequate.valid adequate Two boolean env19)
  bad3019 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop (bop b0 b0) b0))) b1 → ⊥
  bad3019  p = false≢true (cong lower p)
  cut3019 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (op (var 1) (var 1)) (var 0)))) , (var 3)) → ⊥
  cut3019  adequate = bad3019  (Adequate.valid adequate Two boolean env3)
  bad3020 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b1 (bop (bop b0 b0) b0))) b0 → ⊥
  bad3020  p = false≢true (sym (cong lower p))
  cut3020 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (op (var 1) (var 1)) (var 1)))) , (var 0)) → ⊥
  cut3020  adequate = bad3020  (Adequate.valid adequate Two boolean env1)
  bad3021 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b1 (bop (bop b0 b0) b0))) b0 → ⊥
  bad3021  p = false≢true (sym (cong lower p))
  cut3021 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (op (var 1) (var 1)) (var 1)))) , (var 1)) → ⊥
  cut3021  adequate = bad3021  (Adequate.valid adequate Two boolean env1)
  bad3022 : PathP (λ _ → Two) (bop (bop b1 b1) (bop b0 (bop (bop b1 b1) b1))) b0 → ⊥
  bad3022  p = false≢true (sym (cong lower p))
  cut3022 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (op (var 1) (var 1)) (var 1)))) , (var 2)) → ⊥
  cut3022  adequate = bad3022  (Adequate.valid adequate Two boolean env23)
  bad3023 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop (bop b0 b0) b0))) b1 → ⊥
  bad3023  p = false≢true (cong lower p)
  cut3023 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (op (var 1) (var 1)) (var 1)))) , (var 3)) → ⊥
  cut3023  adequate = bad3023  (Adequate.valid adequate Two boolean env3)
  bad3024 : PathP (λ _ → Two) (bop (bop b0 b1) (bop b1 (bop (bop b1 b1) b1))) b0 → ⊥
  bad3024  p = false≢true (sym (cong lower p))
  cut3024 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (op (var 1) (var 1)) (var 2)))) , (var 0)) → ⊥
  cut3024  adequate = bad3024  (Adequate.valid adequate Two boolean env8)
  bad3025 : PathP (λ _ → Two) (bop (bop b0 b1) (bop b0 (bop (bop b1 b1) b0))) b1 → ⊥
  bad3025  p = false≢true (cong lower p)
  cut3025 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (op (var 1) (var 1)) (var 2)))) , (var 1)) → ⊥
  cut3025  adequate = bad3025  (Adequate.valid adequate Two boolean env2)
  bad3026 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b1 (bop (bop b0 b0) b1))) b1 → ⊥
  bad3026  p = false≢true (cong lower p)
  cut3026 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (op (var 1) (var 1)) (var 2)))) , (var 2)) → ⊥
  cut3026  adequate = bad3026  (Adequate.valid adequate Two boolean env1)
  bad3027 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop (bop b0 b0) b0))) b1 → ⊥
  bad3027  p = false≢true (cong lower p)
  cut3027 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (op (var 1) (var 1)) (var 2)))) , (var 3)) → ⊥
  cut3027  adequate = bad3027  (Adequate.valid adequate Two boolean env3)
  bad3028 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b1 (bop (bop b0 b0) b0))) b0 → ⊥
  bad3028  p = false≢true (sym (cong lower p))
  cut3028 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (op (var 1) (var 1)) (var 3)))) , (var 0)) → ⊥
  cut3028  adequate = bad3028  (Adequate.valid adequate Two boolean env5)
  bad3029 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b1 (bop (bop b0 b0) b0))) b0 → ⊥
  bad3029  p = false≢true (sym (cong lower p))
  cut3029 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (op (var 1) (var 1)) (var 3)))) , (var 1)) → ⊥
  cut3029  adequate = bad3029  (Adequate.valid adequate Two boolean env5)
  bad3030 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b1 (bop (bop b0 b0) b1))) b1 → ⊥
  bad3030  p = false≢true (cong lower p)
  cut3030 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (op (var 1) (var 1)) (var 3)))) , (var 2)) → ⊥
  cut3030  adequate = bad3030  (Adequate.valid adequate Two boolean env24)
  bad3031 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop (bop b0 b0) b1))) b1 → ⊥
  bad3031  p = false≢true (cong lower p)
  cut3031 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (op (var 1) (var 1)) (var 3)))) , (var 3)) → ⊥
  cut3031  adequate = bad3031  (Adequate.valid adequate Two boolean env3)
  bad3032 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop (bop b0 b0) b0))) b1 → ⊥
  bad3032  p = false≢true (cong lower p)
  cut3032 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (op (var 1) (var 1)) (var 3)))) , (var 4)) → ⊥
  cut3032  adequate = bad3032  (Adequate.valid adequate Two boolean env6)
  bad3033 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b1 (bop (bop b0 b1) b0))) b0 → ⊥
  bad3033  p = false≢true (sym (cong lower p))
  cut3033 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (op (var 1) (var 2)) (var 0)))) , (var 0)) → ⊥
  cut3033  adequate = bad3033  (Adequate.valid adequate Two boolean env1)
  bad3034 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b1 (bop (bop b0 b1) b0))) b0 → ⊥
  bad3034  p = false≢true (sym (cong lower p))
  cut3034 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (op (var 1) (var 2)) (var 0)))) , (var 1)) → ⊥
  cut3034  adequate = bad3034  (Adequate.valid adequate Two boolean env1)
  bad3035 : PathP (λ _ → Two) (bop (bop b1 b0) (bop b1 (bop (bop b0 b1) b1))) b1 → ⊥
  bad3035  p = false≢true (cong lower p)
  cut3035 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (op (var 1) (var 2)) (var 0)))) , (var 2)) → ⊥
  cut3035  adequate = bad3035  (Adequate.valid adequate Two boolean env19)
  bad3036 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop (bop b0 b0) b0))) b1 → ⊥
  bad3036  p = false≢true (cong lower p)
  cut3036 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (op (var 1) (var 2)) (var 0)))) , (var 3)) → ⊥
  cut3036  adequate = bad3036  (Adequate.valid adequate Two boolean env3)
  bad3037 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b1 (bop (bop b0 b1) b0))) b0 → ⊥
  bad3037  p = false≢true (sym (cong lower p))
  cut3037 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (op (var 1) (var 2)) (var 1)))) , (var 0)) → ⊥
  cut3037  adequate = bad3037  (Adequate.valid adequate Two boolean env1)
  bad3038 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b1 (bop (bop b0 b1) b0))) b0 → ⊥
  bad3038  p = false≢true (sym (cong lower p))
  cut3038 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (op (var 1) (var 2)) (var 1)))) , (var 1)) → ⊥
  cut3038  adequate = bad3038  (Adequate.valid adequate Two boolean env1)
  bad3039 : PathP (λ _ → Two) (bop (bop b1 b1) (bop b0 (bop (bop b1 b0) b1))) b0 → ⊥
  bad3039  p = false≢true (sym (cong lower p))
  cut3039 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (op (var 1) (var 2)) (var 1)))) , (var 2)) → ⊥
  cut3039  adequate = bad3039  (Adequate.valid adequate Two boolean env23)
  bad3040 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop (bop b0 b0) b0))) b1 → ⊥
  bad3040  p = false≢true (cong lower p)
  cut3040 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (op (var 1) (var 2)) (var 1)))) , (var 3)) → ⊥
  cut3040  adequate = bad3040  (Adequate.valid adequate Two boolean env3)
  bad3041 : PathP (λ _ → Two) (bop (bop b0 b1) (bop b1 (bop (bop b1 b1) b1))) b0 → ⊥
  bad3041  p = false≢true (sym (cong lower p))
  cut3041 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (op (var 1) (var 2)) (var 2)))) , (var 0)) → ⊥
  cut3041  adequate = bad3041  (Adequate.valid adequate Two boolean env8)
  bad3042 : PathP (λ _ → Two) (bop (bop b0 b1) (bop b0 (bop (bop b1 b0) b0))) b1 → ⊥
  bad3042  p = false≢true (cong lower p)
  cut3042 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (op (var 1) (var 2)) (var 2)))) , (var 1)) → ⊥
  cut3042  adequate = bad3042  (Adequate.valid adequate Two boolean env2)
  bad3043 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b1 (bop (bop b0 b1) b1))) b1 → ⊥
  bad3043  p = false≢true (cong lower p)
  cut3043 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (op (var 1) (var 2)) (var 2)))) , (var 2)) → ⊥
  cut3043  adequate = bad3043  (Adequate.valid adequate Two boolean env1)
  bad3044 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop (bop b0 b0) b0))) b1 → ⊥
  bad3044  p = false≢true (cong lower p)
  cut3044 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (op (var 1) (var 2)) (var 2)))) , (var 3)) → ⊥
  cut3044  adequate = bad3044  (Adequate.valid adequate Two boolean env3)
  bad3045 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b1 (bop (bop b0 b1) b0))) b0 → ⊥
  bad3045  p = false≢true (sym (cong lower p))
  cut3045 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (op (var 1) (var 2)) (var 3)))) , (var 0)) → ⊥
  cut3045  adequate = bad3045  (Adequate.valid adequate Two boolean env5)
  bad3046 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b1 (bop (bop b0 b1) b0))) b0 → ⊥
  bad3046  p = false≢true (sym (cong lower p))
  cut3046 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (op (var 1) (var 2)) (var 3)))) , (var 1)) → ⊥
  cut3046  adequate = bad3046  (Adequate.valid adequate Two boolean env5)
  bad3047 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b1 (bop (bop b0 b1) b1))) b1 → ⊥
  bad3047  p = false≢true (cong lower p)
  cut3047 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (op (var 1) (var 2)) (var 3)))) , (var 2)) → ⊥
  cut3047  adequate = bad3047  (Adequate.valid adequate Two boolean env24)
  bad3048 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop (bop b0 b0) b1))) b1 → ⊥
  bad3048  p = false≢true (cong lower p)
  cut3048 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (op (var 1) (var 2)) (var 3)))) , (var 3)) → ⊥
  cut3048  adequate = bad3048  (Adequate.valid adequate Two boolean env3)
  bad3049 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop (bop b0 b0) b0))) b1 → ⊥
  bad3049  p = false≢true (cong lower p)
  cut3049 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (op (var 1) (var 2)) (var 3)))) , (var 4)) → ⊥
  cut3049  adequate = bad3049  (Adequate.valid adequate Two boolean env6)
  bad3050 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b1 (bop (bop b0 b0) b0))) b0 → ⊥
  bad3050  p = false≢true (sym (cong lower p))
  cut3050 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (op (var 1) (var 3)) (var 0)))) , (var 0)) → ⊥
  cut3050  adequate = bad3050  (Adequate.valid adequate Two boolean env5)
  bad3051 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b1 (bop (bop b0 b0) b0))) b0 → ⊥
  bad3051  p = false≢true (sym (cong lower p))
  cut3051 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (op (var 1) (var 3)) (var 0)))) , (var 1)) → ⊥
  cut3051  adequate = bad3051  (Adequate.valid adequate Two boolean env5)
  bad3052 : PathP (λ _ → Two) (bop (bop b1 b0) (bop b1 (bop (bop b0 b0) b1))) b1 → ⊥
  bad3052  p = false≢true (cong lower p)
  cut3052 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (op (var 1) (var 3)) (var 0)))) , (var 2)) → ⊥
  cut3052  adequate = bad3052  (Adequate.valid adequate Two boolean env21)
  bad3053 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop (bop b0 b1) b0))) b1 → ⊥
  bad3053  p = false≢true (cong lower p)
  cut3053 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (op (var 1) (var 3)) (var 0)))) , (var 3)) → ⊥
  cut3053  adequate = bad3053  (Adequate.valid adequate Two boolean env3)
  bad3054 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop (bop b0 b0) b0))) b1 → ⊥
  bad3054  p = false≢true (cong lower p)
  cut3054 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (op (var 1) (var 3)) (var 0)))) , (var 4)) → ⊥
  cut3054  adequate = bad3054  (Adequate.valid adequate Two boolean env6)
  bad3055 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b1 (bop (bop b0 b0) b0))) b0 → ⊥
  bad3055  p = false≢true (sym (cong lower p))
  cut3055 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (op (var 1) (var 3)) (var 1)))) , (var 0)) → ⊥
  cut3055  adequate = bad3055  (Adequate.valid adequate Two boolean env5)
  bad3056 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b1 (bop (bop b0 b0) b0))) b0 → ⊥
  bad3056  p = false≢true (sym (cong lower p))
  cut3056 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (op (var 1) (var 3)) (var 1)))) , (var 1)) → ⊥
  cut3056  adequate = bad3056  (Adequate.valid adequate Two boolean env5)
  bad3057 : PathP (λ _ → Two) (bop (bop b0 b1) (bop b1 (bop (bop b1 b0) b1))) b1 → ⊥
  bad3057  p = false≢true (cong lower p)
  cut3057 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (op (var 1) (var 3)) (var 1)))) , (var 2)) → ⊥
  cut3057  adequate = bad3057  (Adequate.valid adequate Two boolean env13)
  bad3058 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop (bop b0 b1) b0))) b1 → ⊥
  bad3058  p = false≢true (cong lower p)
  cut3058 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (op (var 1) (var 3)) (var 1)))) , (var 3)) → ⊥
  cut3058  adequate = bad3058  (Adequate.valid adequate Two boolean env3)
  bad3059 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop (bop b0 b0) b0))) b1 → ⊥
  bad3059  p = false≢true (cong lower p)
  cut3059 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (op (var 1) (var 3)) (var 1)))) , (var 4)) → ⊥
  cut3059  adequate = bad3059  (Adequate.valid adequate Two boolean env6)
  bad3060 : PathP (λ _ → Two) (bop (bop b0 b1) (bop b1 (bop (bop b1 b1) b1))) b0 → ⊥
  bad3060  p = false≢true (sym (cong lower p))
  cut3060 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (op (var 1) (var 3)) (var 2)))) , (var 0)) → ⊥
  cut3060  adequate = bad3060  (Adequate.valid adequate Two boolean env12)
  bad3061 : PathP (λ _ → Two) (bop (bop b0 b1) (bop b0 (bop (bop b1 b0) b0))) b1 → ⊥
  bad3061  p = false≢true (cong lower p)
  cut3061 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (op (var 1) (var 3)) (var 2)))) , (var 1)) → ⊥
  cut3061  adequate = bad3061  (Adequate.valid adequate Two boolean env4)
  bad3062 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b1 (bop (bop b0 b0) b1))) b1 → ⊥
  bad3062  p = false≢true (cong lower p)
  cut3062 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (op (var 1) (var 3)) (var 2)))) , (var 2)) → ⊥
  cut3062  adequate = bad3062  (Adequate.valid adequate Two boolean env5)
  bad3063 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop (bop b0 b1) b0))) b1 → ⊥
  bad3063  p = false≢true (cong lower p)
  cut3063 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (op (var 1) (var 3)) (var 2)))) , (var 3)) → ⊥
  cut3063  adequate = bad3063  (Adequate.valid adequate Two boolean env3)
  bad3064 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop (bop b0 b0) b0))) b1 → ⊥
  bad3064  p = false≢true (cong lower p)
  cut3064 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (op (var 1) (var 3)) (var 2)))) , (var 4)) → ⊥
  cut3064  adequate = bad3064  (Adequate.valid adequate Two boolean env6)
  bad3065 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b1 (bop (bop b0 b0) b0))) b0 → ⊥
  bad3065  p = false≢true (sym (cong lower p))
  cut3065 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (op (var 1) (var 3)) (var 3)))) , (var 0)) → ⊥
  cut3065  adequate = bad3065  (Adequate.valid adequate Two boolean env5)
  bad3066 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b1 (bop (bop b0 b0) b0))) b0 → ⊥
  bad3066  p = false≢true (sym (cong lower p))
  cut3066 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (op (var 1) (var 3)) (var 3)))) , (var 1)) → ⊥
  cut3066  adequate = bad3066  (Adequate.valid adequate Two boolean env5)
  bad3067 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b1 (bop (bop b0 b1) b1))) b1 → ⊥
  bad3067  p = false≢true (cong lower p)
  cut3067 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (op (var 1) (var 3)) (var 3)))) , (var 2)) → ⊥
  cut3067  adequate = bad3067  (Adequate.valid adequate Two boolean env24)
  bad3068 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop (bop b0 b1) b1))) b1 → ⊥
  bad3068  p = false≢true (cong lower p)
  cut3068 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (op (var 1) (var 3)) (var 3)))) , (var 3)) → ⊥
  cut3068  adequate = bad3068  (Adequate.valid adequate Two boolean env3)
  bad3069 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop (bop b0 b0) b0))) b1 → ⊥
  bad3069  p = false≢true (cong lower p)
  cut3069 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (op (var 1) (var 3)) (var 3)))) , (var 4)) → ⊥
  cut3069  adequate = bad3069  (Adequate.valid adequate Two boolean env6)
  bad3070 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b1 (bop (bop b0 b0) b0))) b0 → ⊥
  bad3070  p = false≢true (sym (cong lower p))
  cut3070 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (op (var 1) (var 3)) (var 4)))) , (var 0)) → ⊥
  cut3070  adequate = bad3070  (Adequate.valid adequate Two boolean env16)
  bad3071 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b1 (bop (bop b0 b0) b0))) b0 → ⊥
  bad3071  p = false≢true (sym (cong lower p))
  cut3071 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (op (var 1) (var 3)) (var 4)))) , (var 1)) → ⊥
  cut3071  adequate = bad3071  (Adequate.valid adequate Two boolean env16)
  bad3072 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b1 (bop (bop b0 b0) b1))) b1 → ⊥
  bad3072  p = false≢true (cong lower p)
  cut3072 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (op (var 1) (var 3)) (var 4)))) , (var 2)) → ⊥
  cut3072  adequate = bad3072  (Adequate.valid adequate Two boolean env25)
  bad3073 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop (bop b0 b1) b0))) b1 → ⊥
  bad3073  p = false≢true (cong lower p)
  cut3073 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (op (var 1) (var 3)) (var 4)))) , (var 3)) → ⊥
  cut3073  adequate = bad3073  (Adequate.valid adequate Two boolean env17)
  bad3074 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop (bop b0 b0) b1))) b1 → ⊥
  bad3074  p = false≢true (cong lower p)
  cut3074 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (op (var 1) (var 3)) (var 4)))) , (var 4)) → ⊥
  cut3074  adequate = bad3074  (Adequate.valid adequate Two boolean env6)
  bad3075 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop (bop b0 b0) b0))) b1 → ⊥
  bad3075  p = false≢true (cong lower p)
  cut3075 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (op (var 1) (var 3)) (var 4)))) , (var 5)) → ⊥
  cut3075  adequate = bad3075  (Adequate.valid adequate Two boolean env18)
  bad3076 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b1 (bop (bop b1 b0) b0))) b0 → ⊥
  bad3076  p = false≢true (sym (cong lower p))
  cut3076 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (op (var 2) (var 0)) (var 0)))) , (var 0)) → ⊥
  cut3076  adequate = bad3076  (Adequate.valid adequate Two boolean env1)
  bad3077 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b1 (bop (bop b1 b0) b0))) b0 → ⊥
  bad3077  p = false≢true (sym (cong lower p))
  cut3077 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (op (var 2) (var 0)) (var 0)))) , (var 1)) → ⊥
  cut3077  adequate = bad3077  (Adequate.valid adequate Two boolean env1)
  bad3078 : PathP (λ _ → Two) (bop (bop b1 b1) (bop b0 (bop (bop b0 b1) b1))) b0 → ⊥
  bad3078  p = false≢true (sym (cong lower p))
  cut3078 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (op (var 2) (var 0)) (var 0)))) , (var 2)) → ⊥
  cut3078  adequate = bad3078  (Adequate.valid adequate Two boolean env23)
  bad3079 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop (bop b0 b0) b0))) b1 → ⊥
  bad3079  p = false≢true (cong lower p)
  cut3079 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (op (var 2) (var 0)) (var 0)))) , (var 3)) → ⊥
  cut3079  adequate = bad3079  (Adequate.valid adequate Two boolean env3)
  bad3080 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b1 (bop (bop b1 b0) b0))) b0 → ⊥
  bad3080  p = false≢true (sym (cong lower p))
  cut3080 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (op (var 2) (var 0)) (var 1)))) , (var 0)) → ⊥
  cut3080  adequate = bad3080  (Adequate.valid adequate Two boolean env1)
  bad3081 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b1 (bop (bop b1 b0) b0))) b0 → ⊥
  bad3081  p = false≢true (sym (cong lower p))
  cut3081 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (op (var 2) (var 0)) (var 1)))) , (var 1)) → ⊥
  cut3081  adequate = bad3081  (Adequate.valid adequate Two boolean env1)
  bad3082 : PathP (λ _ → Two) (bop (bop b0 b1) (bop b1 (bop (bop b1 b0) b1))) b1 → ⊥
  bad3082  p = false≢true (cong lower p)
  cut3082 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (op (var 2) (var 0)) (var 1)))) , (var 2)) → ⊥
  cut3082  adequate = bad3082  (Adequate.valid adequate Two boolean env8)
  bad3083 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop (bop b0 b0) b0))) b1 → ⊥
  bad3083  p = false≢true (cong lower p)
  cut3083 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (op (var 2) (var 0)) (var 1)))) , (var 3)) → ⊥
  cut3083  adequate = bad3083  (Adequate.valid adequate Two boolean env3)
  bad3084 : PathP (λ _ → Two) (bop (bop b1 b0) (bop b0 (bop (bop b0 b1) b0))) b1 → ⊥
  bad3084  p = false≢true (cong lower p)
  cut3084 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (op (var 2) (var 0)) (var 2)))) , (var 0)) → ⊥
  cut3084  adequate = bad3084  (Adequate.valid adequate Two boolean env9)
  bad3085 : PathP (λ _ → Two) (bop (bop b0 b1) (bop b0 (bop (bop b0 b0) b0))) b1 → ⊥
  bad3085  p = false≢true (cong lower p)
  cut3085 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (op (var 2) (var 0)) (var 2)))) , (var 1)) → ⊥
  cut3085  adequate = bad3085  (Adequate.valid adequate Two boolean env2)
  bad3086 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b1 (bop (bop b1 b0) b1))) b1 → ⊥
  bad3086  p = false≢true (cong lower p)
  cut3086 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (op (var 2) (var 0)) (var 2)))) , (var 2)) → ⊥
  cut3086  adequate = bad3086  (Adequate.valid adequate Two boolean env1)
  bad3087 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop (bop b0 b0) b0))) b1 → ⊥
  bad3087  p = false≢true (cong lower p)
  cut3087 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (op (var 2) (var 0)) (var 2)))) , (var 3)) → ⊥
  cut3087  adequate = bad3087  (Adequate.valid adequate Two boolean env3)
  bad3088 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b1 (bop (bop b1 b0) b0))) b0 → ⊥
  bad3088  p = false≢true (sym (cong lower p))
  cut3088 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (op (var 2) (var 0)) (var 3)))) , (var 0)) → ⊥
  cut3088  adequate = bad3088  (Adequate.valid adequate Two boolean env5)
  bad3089 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b1 (bop (bop b1 b0) b0))) b0 → ⊥
  bad3089  p = false≢true (sym (cong lower p))
  cut3089 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (op (var 2) (var 0)) (var 3)))) , (var 1)) → ⊥
  cut3089  adequate = bad3089  (Adequate.valid adequate Two boolean env5)
  bad3090 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b1 (bop (bop b1 b0) b1))) b1 → ⊥
  bad3090  p = false≢true (cong lower p)
  cut3090 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (op (var 2) (var 0)) (var 3)))) , (var 2)) → ⊥
  cut3090  adequate = bad3090  (Adequate.valid adequate Two boolean env24)
  bad3091 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop (bop b0 b0) b1))) b1 → ⊥
  bad3091  p = false≢true (cong lower p)
  cut3091 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (op (var 2) (var 0)) (var 3)))) , (var 3)) → ⊥
  cut3091  adequate = bad3091  (Adequate.valid adequate Two boolean env3)
  bad3092 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop (bop b0 b0) b0))) b1 → ⊥
  bad3092  p = false≢true (cong lower p)
  cut3092 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (op (var 2) (var 0)) (var 3)))) , (var 4)) → ⊥
  cut3092  adequate = bad3092  (Adequate.valid adequate Two boolean env6)
  bad3093 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b1 (bop (bop b1 b0) b0))) b0 → ⊥
  bad3093  p = false≢true (sym (cong lower p))
  cut3093 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (op (var 2) (var 1)) (var 0)))) , (var 0)) → ⊥
  cut3093  adequate = bad3093  (Adequate.valid adequate Two boolean env1)
  bad3094 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b1 (bop (bop b1 b0) b0))) b0 → ⊥
  bad3094  p = false≢true (sym (cong lower p))
  cut3094 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (op (var 2) (var 1)) (var 0)))) , (var 1)) → ⊥
  cut3094  adequate = bad3094  (Adequate.valid adequate Two boolean env1)
  bad3095 : PathP (λ _ → Two) (bop (bop b1 b0) (bop b1 (bop (bop b1 b0) b1))) b1 → ⊥
  bad3095  p = false≢true (cong lower p)
  cut3095 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (op (var 2) (var 1)) (var 0)))) , (var 2)) → ⊥
  cut3095  adequate = bad3095  (Adequate.valid adequate Two boolean env19)
  bad3096 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop (bop b0 b0) b0))) b1 → ⊥
  bad3096  p = false≢true (cong lower p)
  cut3096 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (op (var 2) (var 1)) (var 0)))) , (var 3)) → ⊥
  cut3096  adequate = bad3096  (Adequate.valid adequate Two boolean env3)
  bad3097 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b1 (bop (bop b1 b0) b0))) b0 → ⊥
  bad3097  p = false≢true (sym (cong lower p))
  cut3097 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (op (var 2) (var 1)) (var 1)))) , (var 0)) → ⊥
  cut3097  adequate = bad3097  (Adequate.valid adequate Two boolean env1)
  bad3098 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b1 (bop (bop b1 b0) b0))) b0 → ⊥
  bad3098  p = false≢true (sym (cong lower p))
  cut3098 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (op (var 2) (var 1)) (var 1)))) , (var 1)) → ⊥
  cut3098  adequate = bad3098  (Adequate.valid adequate Two boolean env1)
  bad3099 : PathP (λ _ → Two) (bop (bop b1 b1) (bop b0 (bop (bop b0 b1) b1))) b0 → ⊥
  bad3099  p = false≢true (sym (cong lower p))
  cut3099 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (op (var 2) (var 1)) (var 1)))) , (var 2)) → ⊥
  cut3099  adequate = bad3099  (Adequate.valid adequate Two boolean env23)
  bad3100 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop (bop b0 b0) b0))) b1 → ⊥
  bad3100  p = false≢true (cong lower p)
  cut3100 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (op (var 2) (var 1)) (var 1)))) , (var 3)) → ⊥
  cut3100  adequate = bad3100  (Adequate.valid adequate Two boolean env3)
  bad3101 : PathP (λ _ → Two) (bop (bop b0 b1) (bop b1 (bop (bop b1 b1) b1))) b0 → ⊥
  bad3101  p = false≢true (sym (cong lower p))
  cut3101 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (op (var 2) (var 1)) (var 2)))) , (var 0)) → ⊥
  cut3101  adequate = bad3101  (Adequate.valid adequate Two boolean env8)
  bad3102 : PathP (λ _ → Two) (bop (bop b0 b1) (bop b0 (bop (bop b0 b1) b0))) b1 → ⊥
  bad3102  p = false≢true (cong lower p)
  cut3102 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (op (var 2) (var 1)) (var 2)))) , (var 1)) → ⊥
  cut3102  adequate = bad3102  (Adequate.valid adequate Two boolean env2)
  bad3103 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b1 (bop (bop b1 b0) b1))) b1 → ⊥
  bad3103  p = false≢true (cong lower p)
  cut3103 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (op (var 2) (var 1)) (var 2)))) , (var 2)) → ⊥
  cut3103  adequate = bad3103  (Adequate.valid adequate Two boolean env1)
  bad3104 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop (bop b0 b0) b0))) b1 → ⊥
  bad3104  p = false≢true (cong lower p)
  cut3104 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (op (var 2) (var 1)) (var 2)))) , (var 3)) → ⊥
  cut3104  adequate = bad3104  (Adequate.valid adequate Two boolean env3)
  bad3105 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b1 (bop (bop b1 b0) b0))) b0 → ⊥
  bad3105  p = false≢true (sym (cong lower p))
  cut3105 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (op (var 2) (var 1)) (var 3)))) , (var 0)) → ⊥
  cut3105  adequate = bad3105  (Adequate.valid adequate Two boolean env5)
  bad3106 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b1 (bop (bop b1 b0) b0))) b0 → ⊥
  bad3106  p = false≢true (sym (cong lower p))
  cut3106 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (op (var 2) (var 1)) (var 3)))) , (var 1)) → ⊥
  cut3106  adequate = bad3106  (Adequate.valid adequate Two boolean env5)
  bad3107 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b1 (bop (bop b1 b0) b1))) b1 → ⊥
  bad3107  p = false≢true (cong lower p)
  cut3107 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (op (var 2) (var 1)) (var 3)))) , (var 2)) → ⊥
  cut3107  adequate = bad3107  (Adequate.valid adequate Two boolean env24)
  bad3108 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop (bop b0 b0) b1))) b1 → ⊥
  bad3108  p = false≢true (cong lower p)
  cut3108 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (op (var 2) (var 1)) (var 3)))) , (var 3)) → ⊥
  cut3108  adequate = bad3108  (Adequate.valid adequate Two boolean env3)
  bad3109 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop (bop b0 b0) b0))) b1 → ⊥
  bad3109  p = false≢true (cong lower p)
  cut3109 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (op (var 2) (var 1)) (var 3)))) , (var 4)) → ⊥
  cut3109  adequate = bad3109  (Adequate.valid adequate Two boolean env6)
  bad3110 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b1 (bop (bop b1 b1) b0))) b0 → ⊥
  bad3110  p = false≢true (sym (cong lower p))
  cut3110 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (op (var 2) (var 2)) (var 0)))) , (var 0)) → ⊥
  cut3110  adequate = bad3110  (Adequate.valid adequate Two boolean env1)
  bad3111 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b1 (bop (bop b1 b1) b0))) b0 → ⊥
  bad3111  p = false≢true (sym (cong lower p))
  cut3111 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (op (var 2) (var 2)) (var 0)))) , (var 1)) → ⊥
  cut3111  adequate = bad3111  (Adequate.valid adequate Two boolean env1)
  bad3112 : PathP (λ _ → Two) (bop (bop b1 b1) (bop b0 (bop (bop b0 b0) b1))) b0 → ⊥
  bad3112  p = false≢true (sym (cong lower p))
  cut3112 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (op (var 2) (var 2)) (var 0)))) , (var 2)) → ⊥
  cut3112  adequate = bad3112  (Adequate.valid adequate Two boolean env23)
  bad3113 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop (bop b0 b0) b0))) b1 → ⊥
  bad3113  p = false≢true (cong lower p)
  cut3113 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (op (var 2) (var 2)) (var 0)))) , (var 3)) → ⊥
  cut3113  adequate = bad3113  (Adequate.valid adequate Two boolean env3)
  bad3114 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b1 (bop (bop b1 b1) b0))) b0 → ⊥
  bad3114  p = false≢true (sym (cong lower p))
  cut3114 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (op (var 2) (var 2)) (var 1)))) , (var 0)) → ⊥
  cut3114  adequate = bad3114  (Adequate.valid adequate Two boolean env1)
  bad3115 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b1 (bop (bop b1 b1) b0))) b0 → ⊥
  bad3115  p = false≢true (sym (cong lower p))
  cut3115 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (op (var 2) (var 2)) (var 1)))) , (var 1)) → ⊥
  cut3115  adequate = bad3115  (Adequate.valid adequate Two boolean env1)
  bad3116 : PathP (λ _ → Two) (bop (bop b1 b1) (bop b0 (bop (bop b0 b0) b1))) b0 → ⊥
  bad3116  p = false≢true (sym (cong lower p))
  cut3116 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (op (var 2) (var 2)) (var 1)))) , (var 2)) → ⊥
  cut3116  adequate = bad3116  (Adequate.valid adequate Two boolean env23)
  bad3117 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop (bop b0 b0) b0))) b1 → ⊥
  bad3117  p = false≢true (cong lower p)
  cut3117 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (op (var 2) (var 2)) (var 1)))) , (var 3)) → ⊥
  cut3117  adequate = bad3117  (Adequate.valid adequate Two boolean env3)
  bad3118 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b1 (bop (bop b1 b1) b1))) b0 → ⊥
  bad3118  p = false≢true (sym (cong lower p))
  cut3118 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (op (var 2) (var 2)) (var 2)))) , (var 0)) → ⊥
  cut3118  adequate = bad3118  (Adequate.valid adequate Two boolean env1)
  bad3119 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b1 (bop (bop b1 b1) b1))) b0 → ⊥
  bad3119  p = false≢true (sym (cong lower p))
  cut3119 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (op (var 2) (var 2)) (var 2)))) , (var 1)) → ⊥
  cut3119  adequate = bad3119  (Adequate.valid adequate Two boolean env1)
  bad3120 : PathP (λ _ → Two) (bop (bop b1 b1) (bop b0 (bop (bop b0 b0) b0))) b0 → ⊥
  bad3120  p = false≢true (sym (cong lower p))
  cut3120 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (op (var 2) (var 2)) (var 2)))) , (var 2)) → ⊥
  cut3120  adequate = bad3120  (Adequate.valid adequate Two boolean env23)
  bad3121 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop (bop b0 b0) b0))) b1 → ⊥
  bad3121  p = false≢true (cong lower p)
  cut3121 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (op (var 2) (var 2)) (var 2)))) , (var 3)) → ⊥
  cut3121  adequate = bad3121  (Adequate.valid adequate Two boolean env3)
  bad3122 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b1 (bop (bop b1 b1) b0))) b0 → ⊥
  bad3122  p = false≢true (sym (cong lower p))
  cut3122 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (op (var 2) (var 2)) (var 3)))) , (var 0)) → ⊥
  cut3122  adequate = bad3122  (Adequate.valid adequate Two boolean env5)
  bad3123 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b1 (bop (bop b1 b1) b0))) b0 → ⊥
  bad3123  p = false≢true (sym (cong lower p))
  cut3123 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (op (var 2) (var 2)) (var 3)))) , (var 1)) → ⊥
  cut3123  adequate = bad3123  (Adequate.valid adequate Two boolean env5)
  env26 : ℕ → Two
  env26 zero = b1
  env26 (suc zero) = b1
  env26 (suc (suc zero)) = b0
  env26 (suc (suc (suc zero))) = b0
  env26 (suc (suc (suc (suc rest)))) = b0
  bad3124 : PathP (λ _ → Two) (bop (bop b1 b1) (bop b0 (bop (bop b0 b0) b0))) b0 → ⊥
  bad3124  p = false≢true (sym (cong lower p))
  cut3124 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (op (var 2) (var 2)) (var 3)))) , (var 2)) → ⊥
  cut3124  adequate = bad3124  (Adequate.valid adequate Two boolean env26)
  bad3125 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop (bop b0 b0) b1))) b1 → ⊥
  bad3125  p = false≢true (cong lower p)
  cut3125 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (op (var 2) (var 2)) (var 3)))) , (var 3)) → ⊥
  cut3125  adequate = bad3125  (Adequate.valid adequate Two boolean env3)
  bad3126 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop (bop b0 b0) b0))) b1 → ⊥
  bad3126  p = false≢true (cong lower p)
  cut3126 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (op (var 2) (var 2)) (var 3)))) , (var 4)) → ⊥
  cut3126  adequate = bad3126  (Adequate.valid adequate Two boolean env6)
  bad3127 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b1 (bop (bop b1 b0) b0))) b0 → ⊥
  bad3127  p = false≢true (sym (cong lower p))
  cut3127 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (op (var 2) (var 3)) (var 0)))) , (var 0)) → ⊥
  cut3127  adequate = bad3127  (Adequate.valid adequate Two boolean env5)
  bad3128 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b1 (bop (bop b1 b0) b0))) b0 → ⊥
  bad3128  p = false≢true (sym (cong lower p))
  cut3128 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (op (var 2) (var 3)) (var 0)))) , (var 1)) → ⊥
  cut3128  adequate = bad3128  (Adequate.valid adequate Two boolean env5)
  bad3129 : PathP (λ _ → Two) (bop (bop b1 b0) (bop b1 (bop (bop b1 b0) b1))) b1 → ⊥
  bad3129  p = false≢true (cong lower p)
  cut3129 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (op (var 2) (var 3)) (var 0)))) , (var 2)) → ⊥
  cut3129  adequate = bad3129  (Adequate.valid adequate Two boolean env21)
  bad3130 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop (bop b0 b1) b0))) b1 → ⊥
  bad3130  p = false≢true (cong lower p)
  cut3130 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (op (var 2) (var 3)) (var 0)))) , (var 3)) → ⊥
  cut3130  adequate = bad3130  (Adequate.valid adequate Two boolean env3)
  bad3131 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop (bop b0 b0) b0))) b1 → ⊥
  bad3131  p = false≢true (cong lower p)
  cut3131 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (op (var 2) (var 3)) (var 0)))) , (var 4)) → ⊥
  cut3131  adequate = bad3131  (Adequate.valid adequate Two boolean env6)
  bad3132 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b1 (bop (bop b1 b0) b0))) b0 → ⊥
  bad3132  p = false≢true (sym (cong lower p))
  cut3132 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (op (var 2) (var 3)) (var 1)))) , (var 0)) → ⊥
  cut3132  adequate = bad3132  (Adequate.valid adequate Two boolean env5)
  bad3133 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b1 (bop (bop b1 b0) b0))) b0 → ⊥
  bad3133  p = false≢true (sym (cong lower p))
  cut3133 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (op (var 2) (var 3)) (var 1)))) , (var 1)) → ⊥
  cut3133  adequate = bad3133  (Adequate.valid adequate Two boolean env5)
  bad3134 : PathP (λ _ → Two) (bop (bop b0 b1) (bop b1 (bop (bop b1 b0) b1))) b1 → ⊥
  bad3134  p = false≢true (cong lower p)
  cut3134 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (op (var 2) (var 3)) (var 1)))) , (var 2)) → ⊥
  cut3134  adequate = bad3134  (Adequate.valid adequate Two boolean env13)
  bad3135 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop (bop b0 b1) b0))) b1 → ⊥
  bad3135  p = false≢true (cong lower p)
  cut3135 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (op (var 2) (var 3)) (var 1)))) , (var 3)) → ⊥
  cut3135  adequate = bad3135  (Adequate.valid adequate Two boolean env3)
  bad3136 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop (bop b0 b0) b0))) b1 → ⊥
  bad3136  p = false≢true (cong lower p)
  cut3136 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (op (var 2) (var 3)) (var 1)))) , (var 4)) → ⊥
  cut3136  adequate = bad3136  (Adequate.valid adequate Two boolean env6)
  bad3137 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b1 (bop (bop b1 b1) b1))) b0 → ⊥
  bad3137  p = false≢true (sym (cong lower p))
  cut3137 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (op (var 2) (var 3)) (var 2)))) , (var 0)) → ⊥
  cut3137  adequate = bad3137  (Adequate.valid adequate Two boolean env24)
  bad3138 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b1 (bop (bop b1 b1) b1))) b0 → ⊥
  bad3138  p = false≢true (sym (cong lower p))
  cut3138 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (op (var 2) (var 3)) (var 2)))) , (var 1)) → ⊥
  cut3138  adequate = bad3138  (Adequate.valid adequate Two boolean env24)
  bad3139 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b1 (bop (bop b1 b0) b1))) b1 → ⊥
  bad3139  p = false≢true (cong lower p)
  cut3139 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (op (var 2) (var 3)) (var 2)))) , (var 2)) → ⊥
  cut3139  adequate = bad3139  (Adequate.valid adequate Two boolean env5)
  bad3140 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop (bop b0 b1) b0))) b1 → ⊥
  bad3140  p = false≢true (cong lower p)
  cut3140 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (op (var 2) (var 3)) (var 2)))) , (var 3)) → ⊥
  cut3140  adequate = bad3140  (Adequate.valid adequate Two boolean env3)
  bad3141 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop (bop b0 b0) b0))) b1 → ⊥
  bad3141  p = false≢true (cong lower p)
  cut3141 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (op (var 2) (var 3)) (var 2)))) , (var 4)) → ⊥
  cut3141  adequate = bad3141  (Adequate.valid adequate Two boolean env6)
  bad3142 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b1 (bop (bop b1 b0) b0))) b0 → ⊥
  bad3142  p = false≢true (sym (cong lower p))
  cut3142 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (op (var 2) (var 3)) (var 3)))) , (var 0)) → ⊥
  cut3142  adequate = bad3142  (Adequate.valid adequate Two boolean env5)
  bad3143 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b1 (bop (bop b1 b0) b0))) b0 → ⊥
  bad3143  p = false≢true (sym (cong lower p))
  cut3143 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (op (var 2) (var 3)) (var 3)))) , (var 1)) → ⊥
  cut3143  adequate = bad3143  (Adequate.valid adequate Two boolean env5)
  bad3144 : PathP (λ _ → Two) (bop (bop b1 b1) (bop b0 (bop (bop b0 b0) b0))) b0 → ⊥
  bad3144  p = false≢true (sym (cong lower p))
  cut3144 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (op (var 2) (var 3)) (var 3)))) , (var 2)) → ⊥
  cut3144  adequate = bad3144  (Adequate.valid adequate Two boolean env26)
  bad3145 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop (bop b0 b1) b1))) b1 → ⊥
  bad3145  p = false≢true (cong lower p)
  cut3145 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (op (var 2) (var 3)) (var 3)))) , (var 3)) → ⊥
  cut3145  adequate = bad3145  (Adequate.valid adequate Two boolean env3)
  bad3146 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop (bop b0 b0) b0))) b1 → ⊥
  bad3146  p = false≢true (cong lower p)
  cut3146 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (op (var 2) (var 3)) (var 3)))) , (var 4)) → ⊥
  cut3146  adequate = bad3146  (Adequate.valid adequate Two boolean env6)
  bad3147 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b1 (bop (bop b1 b0) b0))) b0 → ⊥
  bad3147  p = false≢true (sym (cong lower p))
  cut3147 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (op (var 2) (var 3)) (var 4)))) , (var 0)) → ⊥
  cut3147  adequate = bad3147  (Adequate.valid adequate Two boolean env16)
  bad3148 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b1 (bop (bop b1 b0) b0))) b0 → ⊥
  bad3148  p = false≢true (sym (cong lower p))
  cut3148 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (op (var 2) (var 3)) (var 4)))) , (var 1)) → ⊥
  cut3148  adequate = bad3148  (Adequate.valid adequate Two boolean env16)
  bad3149 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b1 (bop (bop b1 b0) b1))) b1 → ⊥
  bad3149  p = false≢true (cong lower p)
  cut3149 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (op (var 2) (var 3)) (var 4)))) , (var 2)) → ⊥
  cut3149  adequate = bad3149  (Adequate.valid adequate Two boolean env25)
  bad3150 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop (bop b0 b1) b0))) b1 → ⊥
  bad3150  p = false≢true (cong lower p)
  cut3150 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (op (var 2) (var 3)) (var 4)))) , (var 3)) → ⊥
  cut3150  adequate = bad3150  (Adequate.valid adequate Two boolean env17)
  bad3151 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop (bop b0 b0) b1))) b1 → ⊥
  bad3151  p = false≢true (cong lower p)
  cut3151 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (op (var 2) (var 3)) (var 4)))) , (var 4)) → ⊥
  cut3151  adequate = bad3151  (Adequate.valid adequate Two boolean env6)
  bad3152 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop (bop b0 b0) b0))) b1 → ⊥
  bad3152  p = false≢true (cong lower p)
  cut3152 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (op (var 2) (var 3)) (var 4)))) , (var 5)) → ⊥
  cut3152  adequate = bad3152  (Adequate.valid adequate Two boolean env18)
  bad3153 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b1 (bop (bop b0 b0) b0))) b0 → ⊥
  bad3153  p = false≢true (sym (cong lower p))
  cut3153 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (op (var 3) (var 0)) (var 0)))) , (var 0)) → ⊥
  cut3153  adequate = bad3153  (Adequate.valid adequate Two boolean env5)
  bad3154 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b1 (bop (bop b0 b0) b0))) b0 → ⊥
  bad3154  p = false≢true (sym (cong lower p))
  cut3154 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (op (var 3) (var 0)) (var 0)))) , (var 1)) → ⊥
  cut3154  adequate = bad3154  (Adequate.valid adequate Two boolean env5)
  bad3155 : PathP (λ _ → Two) (bop (bop b1 b0) (bop b1 (bop (bop b0 b1) b1))) b1 → ⊥
  bad3155  p = false≢true (cong lower p)
  cut3155 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (op (var 3) (var 0)) (var 0)))) , (var 2)) → ⊥
  cut3155  adequate = bad3155  (Adequate.valid adequate Two boolean env21)
  bad3156 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop (bop b1 b0) b0))) b1 → ⊥
  bad3156  p = false≢true (cong lower p)
  cut3156 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (op (var 3) (var 0)) (var 0)))) , (var 3)) → ⊥
  cut3156  adequate = bad3156  (Adequate.valid adequate Two boolean env3)
  bad3157 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop (bop b0 b0) b0))) b1 → ⊥
  bad3157  p = false≢true (cong lower p)
  cut3157 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (op (var 3) (var 0)) (var 0)))) , (var 4)) → ⊥
  cut3157  adequate = bad3157  (Adequate.valid adequate Two boolean env6)
  bad3158 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b1 (bop (bop b0 b0) b0))) b0 → ⊥
  bad3158  p = false≢true (sym (cong lower p))
  cut3158 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (op (var 3) (var 0)) (var 1)))) , (var 0)) → ⊥
  cut3158  adequate = bad3158  (Adequate.valid adequate Two boolean env5)
  bad3159 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b1 (bop (bop b0 b0) b0))) b0 → ⊥
  bad3159  p = false≢true (sym (cong lower p))
  cut3159 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (op (var 3) (var 0)) (var 1)))) , (var 1)) → ⊥
  cut3159  adequate = bad3159  (Adequate.valid adequate Two boolean env5)
  bad3160 : PathP (λ _ → Two) (bop (bop b0 b1) (bop b1 (bop (bop b0 b0) b1))) b1 → ⊥
  bad3160  p = false≢true (cong lower p)
  cut3160 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (op (var 3) (var 0)) (var 1)))) , (var 2)) → ⊥
  cut3160  adequate = bad3160  (Adequate.valid adequate Two boolean env13)
  bad3161 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop (bop b1 b0) b0))) b1 → ⊥
  bad3161  p = false≢true (cong lower p)
  cut3161 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (op (var 3) (var 0)) (var 1)))) , (var 3)) → ⊥
  cut3161  adequate = bad3161  (Adequate.valid adequate Two boolean env3)
  bad3162 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop (bop b0 b0) b0))) b1 → ⊥
  bad3162  p = false≢true (cong lower p)
  cut3162 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (op (var 3) (var 0)) (var 1)))) , (var 4)) → ⊥
  cut3162  adequate = bad3162  (Adequate.valid adequate Two boolean env6)
  bad3163 : PathP (λ _ → Two) (bop (bop b1 b0) (bop b0 (bop (bop b0 b1) b0))) b1 → ⊥
  bad3163  p = false≢true (cong lower p)
  cut3163 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (op (var 3) (var 0)) (var 2)))) , (var 0)) → ⊥
  cut3163  adequate = bad3163  (Adequate.valid adequate Two boolean env11)
  bad3164 : PathP (λ _ → Two) (bop (bop b0 b1) (bop b0 (bop (bop b0 b0) b0))) b1 → ⊥
  bad3164  p = false≢true (cong lower p)
  cut3164 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (op (var 3) (var 0)) (var 2)))) , (var 1)) → ⊥
  cut3164  adequate = bad3164  (Adequate.valid adequate Two boolean env4)
  bad3165 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b1 (bop (bop b0 b0) b1))) b1 → ⊥
  bad3165  p = false≢true (cong lower p)
  cut3165 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (op (var 3) (var 0)) (var 2)))) , (var 2)) → ⊥
  cut3165  adequate = bad3165  (Adequate.valid adequate Two boolean env5)
  bad3166 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop (bop b1 b0) b0))) b1 → ⊥
  bad3166  p = false≢true (cong lower p)
  cut3166 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (op (var 3) (var 0)) (var 2)))) , (var 3)) → ⊥
  cut3166  adequate = bad3166  (Adequate.valid adequate Two boolean env3)
  bad3167 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop (bop b0 b0) b0))) b1 → ⊥
  bad3167  p = false≢true (cong lower p)
  cut3167 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (op (var 3) (var 0)) (var 2)))) , (var 4)) → ⊥
  cut3167  adequate = bad3167  (Adequate.valid adequate Two boolean env6)
  bad3168 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b1 (bop (bop b0 b0) b0))) b0 → ⊥
  bad3168  p = false≢true (sym (cong lower p))
  cut3168 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (op (var 3) (var 0)) (var 3)))) , (var 0)) → ⊥
  cut3168  adequate = bad3168  (Adequate.valid adequate Two boolean env5)
  bad3169 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b1 (bop (bop b0 b0) b0))) b0 → ⊥
  bad3169  p = false≢true (sym (cong lower p))
  cut3169 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (op (var 3) (var 0)) (var 3)))) , (var 1)) → ⊥
  cut3169  adequate = bad3169  (Adequate.valid adequate Two boolean env5)
  bad3170 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b1 (bop (bop b1 b0) b1))) b1 → ⊥
  bad3170  p = false≢true (cong lower p)
  cut3170 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (op (var 3) (var 0)) (var 3)))) , (var 2)) → ⊥
  cut3170  adequate = bad3170  (Adequate.valid adequate Two boolean env24)
  bad3171 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop (bop b1 b0) b1))) b1 → ⊥
  bad3171  p = false≢true (cong lower p)
  cut3171 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (op (var 3) (var 0)) (var 3)))) , (var 3)) → ⊥
  cut3171  adequate = bad3171  (Adequate.valid adequate Two boolean env3)
  bad3172 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop (bop b0 b0) b0))) b1 → ⊥
  bad3172  p = false≢true (cong lower p)
  cut3172 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (op (var 3) (var 0)) (var 3)))) , (var 4)) → ⊥
  cut3172  adequate = bad3172  (Adequate.valid adequate Two boolean env6)
  bad3173 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b1 (bop (bop b0 b0) b0))) b0 → ⊥
  bad3173  p = false≢true (sym (cong lower p))
  cut3173 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (op (var 3) (var 0)) (var 4)))) , (var 0)) → ⊥
  cut3173  adequate = bad3173  (Adequate.valid adequate Two boolean env16)
  bad3174 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b1 (bop (bop b0 b0) b0))) b0 → ⊥
  bad3174  p = false≢true (sym (cong lower p))
  cut3174 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (op (var 3) (var 0)) (var 4)))) , (var 1)) → ⊥
  cut3174  adequate = bad3174  (Adequate.valid adequate Two boolean env16)
  bad3175 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b1 (bop (bop b0 b0) b1))) b1 → ⊥
  bad3175  p = false≢true (cong lower p)
  cut3175 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (op (var 3) (var 0)) (var 4)))) , (var 2)) → ⊥
  cut3175  adequate = bad3175  (Adequate.valid adequate Two boolean env25)
  bad3176 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop (bop b1 b0) b0))) b1 → ⊥
  bad3176  p = false≢true (cong lower p)
  cut3176 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (op (var 3) (var 0)) (var 4)))) , (var 3)) → ⊥
  cut3176  adequate = bad3176  (Adequate.valid adequate Two boolean env17)
  bad3177 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop (bop b0 b0) b1))) b1 → ⊥
  bad3177  p = false≢true (cong lower p)
  cut3177 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (op (var 3) (var 0)) (var 4)))) , (var 4)) → ⊥
  cut3177  adequate = bad3177  (Adequate.valid adequate Two boolean env6)
  bad3178 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop (bop b0 b0) b0))) b1 → ⊥
  bad3178  p = false≢true (cong lower p)
  cut3178 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (op (var 3) (var 0)) (var 4)))) , (var 5)) → ⊥
  cut3178  adequate = bad3178  (Adequate.valid adequate Two boolean env18)
  bad3179 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b1 (bop (bop b0 b0) b0))) b0 → ⊥
  bad3179  p = false≢true (sym (cong lower p))
  cut3179 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (op (var 3) (var 1)) (var 0)))) , (var 0)) → ⊥
  cut3179  adequate = bad3179  (Adequate.valid adequate Two boolean env5)
  bad3180 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b1 (bop (bop b0 b0) b0))) b0 → ⊥
  bad3180  p = false≢true (sym (cong lower p))
  cut3180 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (op (var 3) (var 1)) (var 0)))) , (var 1)) → ⊥
  cut3180  adequate = bad3180  (Adequate.valid adequate Two boolean env5)
  bad3181 : PathP (λ _ → Two) (bop (bop b1 b0) (bop b1 (bop (bop b0 b0) b1))) b1 → ⊥
  bad3181  p = false≢true (cong lower p)
  cut3181 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (op (var 3) (var 1)) (var 0)))) , (var 2)) → ⊥
  cut3181  adequate = bad3181  (Adequate.valid adequate Two boolean env21)
  bad3182 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop (bop b1 b0) b0))) b1 → ⊥
  bad3182  p = false≢true (cong lower p)
  cut3182 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (op (var 3) (var 1)) (var 0)))) , (var 3)) → ⊥
  cut3182  adequate = bad3182  (Adequate.valid adequate Two boolean env3)
  bad3183 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop (bop b0 b0) b0))) b1 → ⊥
  bad3183  p = false≢true (cong lower p)
  cut3183 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (op (var 3) (var 1)) (var 0)))) , (var 4)) → ⊥
  cut3183  adequate = bad3183  (Adequate.valid adequate Two boolean env6)
  bad3184 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b1 (bop (bop b0 b0) b0))) b0 → ⊥
  bad3184  p = false≢true (sym (cong lower p))
  cut3184 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (op (var 3) (var 1)) (var 1)))) , (var 0)) → ⊥
  cut3184  adequate = bad3184  (Adequate.valid adequate Two boolean env5)
  bad3185 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b1 (bop (bop b0 b0) b0))) b0 → ⊥
  bad3185  p = false≢true (sym (cong lower p))
  cut3185 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (op (var 3) (var 1)) (var 1)))) , (var 1)) → ⊥
  cut3185  adequate = bad3185  (Adequate.valid adequate Two boolean env5)
  bad3186 : PathP (λ _ → Two) (bop (bop b0 b1) (bop b1 (bop (bop b0 b1) b1))) b1 → ⊥
  bad3186  p = false≢true (cong lower p)
  cut3186 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (op (var 3) (var 1)) (var 1)))) , (var 2)) → ⊥
  cut3186  adequate = bad3186  (Adequate.valid adequate Two boolean env13)
  bad3187 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop (bop b1 b0) b0))) b1 → ⊥
  bad3187  p = false≢true (cong lower p)
  cut3187 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (op (var 3) (var 1)) (var 1)))) , (var 3)) → ⊥
  cut3187  adequate = bad3187  (Adequate.valid adequate Two boolean env3)
  bad3188 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop (bop b0 b0) b0))) b1 → ⊥
  bad3188  p = false≢true (cong lower p)
  cut3188 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (op (var 3) (var 1)) (var 1)))) , (var 4)) → ⊥
  cut3188  adequate = bad3188  (Adequate.valid adequate Two boolean env6)
  bad3189 : PathP (λ _ → Two) (bop (bop b0 b1) (bop b1 (bop (bop b1 b1) b1))) b0 → ⊥
  bad3189  p = false≢true (sym (cong lower p))
  cut3189 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (op (var 3) (var 1)) (var 2)))) , (var 0)) → ⊥
  cut3189  adequate = bad3189  (Adequate.valid adequate Two boolean env12)
  bad3190 : PathP (λ _ → Two) (bop (bop b0 b1) (bop b0 (bop (bop b0 b1) b0))) b1 → ⊥
  bad3190  p = false≢true (cong lower p)
  cut3190 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (op (var 3) (var 1)) (var 2)))) , (var 1)) → ⊥
  cut3190  adequate = bad3190  (Adequate.valid adequate Two boolean env4)
  bad3191 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b1 (bop (bop b0 b0) b1))) b1 → ⊥
  bad3191  p = false≢true (cong lower p)
  cut3191 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (op (var 3) (var 1)) (var 2)))) , (var 2)) → ⊥
  cut3191  adequate = bad3191  (Adequate.valid adequate Two boolean env5)
  bad3192 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop (bop b1 b0) b0))) b1 → ⊥
  bad3192  p = false≢true (cong lower p)
  cut3192 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (op (var 3) (var 1)) (var 2)))) , (var 3)) → ⊥
  cut3192  adequate = bad3192  (Adequate.valid adequate Two boolean env3)
  bad3193 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop (bop b0 b0) b0))) b1 → ⊥
  bad3193  p = false≢true (cong lower p)
  cut3193 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (op (var 3) (var 1)) (var 2)))) , (var 4)) → ⊥
  cut3193  adequate = bad3193  (Adequate.valid adequate Two boolean env6)
  bad3194 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b1 (bop (bop b0 b0) b0))) b0 → ⊥
  bad3194  p = false≢true (sym (cong lower p))
  cut3194 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (op (var 3) (var 1)) (var 3)))) , (var 0)) → ⊥
  cut3194  adequate = bad3194  (Adequate.valid adequate Two boolean env5)
  bad3195 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b1 (bop (bop b0 b0) b0))) b0 → ⊥
  bad3195  p = false≢true (sym (cong lower p))
  cut3195 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (op (var 3) (var 1)) (var 3)))) , (var 1)) → ⊥
  cut3195  adequate = bad3195  (Adequate.valid adequate Two boolean env5)
  bad3196 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b1 (bop (bop b1 b0) b1))) b1 → ⊥
  bad3196  p = false≢true (cong lower p)
  cut3196 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (op (var 3) (var 1)) (var 3)))) , (var 2)) → ⊥
  cut3196  adequate = bad3196  (Adequate.valid adequate Two boolean env24)
  bad3197 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop (bop b1 b0) b1))) b1 → ⊥
  bad3197  p = false≢true (cong lower p)
  cut3197 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (op (var 3) (var 1)) (var 3)))) , (var 3)) → ⊥
  cut3197  adequate = bad3197  (Adequate.valid adequate Two boolean env3)
  bad3198 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop (bop b0 b0) b0))) b1 → ⊥
  bad3198  p = false≢true (cong lower p)
  cut3198 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (op (var 3) (var 1)) (var 3)))) , (var 4)) → ⊥
  cut3198  adequate = bad3198  (Adequate.valid adequate Two boolean env6)
  bad3199 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b1 (bop (bop b0 b0) b0))) b0 → ⊥
  bad3199  p = false≢true (sym (cong lower p))
  cut3199 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (op (var 3) (var 1)) (var 4)))) , (var 0)) → ⊥
  cut3199  adequate = bad3199  (Adequate.valid adequate Two boolean env16)
  bad3200 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b1 (bop (bop b0 b0) b0))) b0 → ⊥
  bad3200  p = false≢true (sym (cong lower p))
  cut3200 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (op (var 3) (var 1)) (var 4)))) , (var 1)) → ⊥
  cut3200  adequate = bad3200  (Adequate.valid adequate Two boolean env16)
  bad3201 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b1 (bop (bop b0 b0) b1))) b1 → ⊥
  bad3201  p = false≢true (cong lower p)
  cut3201 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (op (var 3) (var 1)) (var 4)))) , (var 2)) → ⊥
  cut3201  adequate = bad3201  (Adequate.valid adequate Two boolean env25)
  bad3202 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop (bop b1 b0) b0))) b1 → ⊥
  bad3202  p = false≢true (cong lower p)
  cut3202 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (op (var 3) (var 1)) (var 4)))) , (var 3)) → ⊥
  cut3202  adequate = bad3202  (Adequate.valid adequate Two boolean env17)
  bad3203 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop (bop b0 b0) b1))) b1 → ⊥
  bad3203  p = false≢true (cong lower p)
  cut3203 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (op (var 3) (var 1)) (var 4)))) , (var 4)) → ⊥
  cut3203  adequate = bad3203  (Adequate.valid adequate Two boolean env6)
  bad3204 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop (bop b0 b0) b0))) b1 → ⊥
  bad3204  p = false≢true (cong lower p)
  cut3204 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (op (var 3) (var 1)) (var 4)))) , (var 5)) → ⊥
  cut3204  adequate = bad3204  (Adequate.valid adequate Two boolean env18)
  bad3205 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b1 (bop (bop b0 b1) b0))) b0 → ⊥
  bad3205  p = false≢true (sym (cong lower p))
  cut3205 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (op (var 3) (var 2)) (var 0)))) , (var 0)) → ⊥
  cut3205  adequate = bad3205  (Adequate.valid adequate Two boolean env5)
  bad3206 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b1 (bop (bop b0 b1) b0))) b0 → ⊥
  bad3206  p = false≢true (sym (cong lower p))
  cut3206 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (op (var 3) (var 2)) (var 0)))) , (var 1)) → ⊥
  cut3206  adequate = bad3206  (Adequate.valid adequate Two boolean env5)
  bad3207 : PathP (λ _ → Two) (bop (bop b1 b0) (bop b1 (bop (bop b0 b1) b1))) b1 → ⊥
  bad3207  p = false≢true (cong lower p)
  cut3207 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (op (var 3) (var 2)) (var 0)))) , (var 2)) → ⊥
  cut3207  adequate = bad3207  (Adequate.valid adequate Two boolean env21)
  bad3208 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop (bop b1 b0) b0))) b1 → ⊥
  bad3208  p = false≢true (cong lower p)
  cut3208 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (op (var 3) (var 2)) (var 0)))) , (var 3)) → ⊥
  cut3208  adequate = bad3208  (Adequate.valid adequate Two boolean env3)
  bad3209 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop (bop b0 b0) b0))) b1 → ⊥
  bad3209  p = false≢true (cong lower p)
  cut3209 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (op (var 3) (var 2)) (var 0)))) , (var 4)) → ⊥
  cut3209  adequate = bad3209  (Adequate.valid adequate Two boolean env6)
  bad3210 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b1 (bop (bop b0 b1) b0))) b0 → ⊥
  bad3210  p = false≢true (sym (cong lower p))
  cut3210 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (op (var 3) (var 2)) (var 1)))) , (var 0)) → ⊥
  cut3210  adequate = bad3210  (Adequate.valid adequate Two boolean env5)
  bad3211 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b1 (bop (bop b0 b1) b0))) b0 → ⊥
  bad3211  p = false≢true (sym (cong lower p))
  cut3211 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (op (var 3) (var 2)) (var 1)))) , (var 1)) → ⊥
  cut3211  adequate = bad3211  (Adequate.valid adequate Two boolean env5)
  bad3212 : PathP (λ _ → Two) (bop (bop b0 b1) (bop b1 (bop (bop b0 b1) b1))) b1 → ⊥
  bad3212  p = false≢true (cong lower p)
  cut3212 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (op (var 3) (var 2)) (var 1)))) , (var 2)) → ⊥
  cut3212  adequate = bad3212  (Adequate.valid adequate Two boolean env13)
  bad3213 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop (bop b1 b0) b0))) b1 → ⊥
  bad3213  p = false≢true (cong lower p)
  cut3213 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (op (var 3) (var 2)) (var 1)))) , (var 3)) → ⊥
  cut3213  adequate = bad3213  (Adequate.valid adequate Two boolean env3)
  bad3214 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop (bop b0 b0) b0))) b1 → ⊥
  bad3214  p = false≢true (cong lower p)
  cut3214 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (op (var 3) (var 2)) (var 1)))) , (var 4)) → ⊥
  cut3214  adequate = bad3214  (Adequate.valid adequate Two boolean env6)
  bad3215 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b1 (bop (bop b1 b1) b1))) b0 → ⊥
  bad3215  p = false≢true (sym (cong lower p))
  cut3215 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (op (var 3) (var 2)) (var 2)))) , (var 0)) → ⊥
  cut3215  adequate = bad3215  (Adequate.valid adequate Two boolean env24)
  bad3216 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b1 (bop (bop b1 b1) b1))) b0 → ⊥
  bad3216  p = false≢true (sym (cong lower p))
  cut3216 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (op (var 3) (var 2)) (var 2)))) , (var 1)) → ⊥
  cut3216  adequate = bad3216  (Adequate.valid adequate Two boolean env24)
  bad3217 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b1 (bop (bop b0 b1) b1))) b1 → ⊥
  bad3217  p = false≢true (cong lower p)
  cut3217 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (op (var 3) (var 2)) (var 2)))) , (var 2)) → ⊥
  cut3217  adequate = bad3217  (Adequate.valid adequate Two boolean env5)
  bad3218 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop (bop b1 b0) b0))) b1 → ⊥
  bad3218  p = false≢true (cong lower p)
  cut3218 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (op (var 3) (var 2)) (var 2)))) , (var 3)) → ⊥
  cut3218  adequate = bad3218  (Adequate.valid adequate Two boolean env3)
  bad3219 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop (bop b0 b0) b0))) b1 → ⊥
  bad3219  p = false≢true (cong lower p)
  cut3219 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (op (var 3) (var 2)) (var 2)))) , (var 4)) → ⊥
  cut3219  adequate = bad3219  (Adequate.valid adequate Two boolean env6)
  bad3220 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b1 (bop (bop b0 b1) b0))) b0 → ⊥
  bad3220  p = false≢true (sym (cong lower p))
  cut3220 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (op (var 3) (var 2)) (var 3)))) , (var 0)) → ⊥
  cut3220  adequate = bad3220  (Adequate.valid adequate Two boolean env5)
  bad3221 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b1 (bop (bop b0 b1) b0))) b0 → ⊥
  bad3221  p = false≢true (sym (cong lower p))
  cut3221 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (op (var 3) (var 2)) (var 3)))) , (var 1)) → ⊥
  cut3221  adequate = bad3221  (Adequate.valid adequate Two boolean env5)
  bad3222 : PathP (λ _ → Two) (bop (bop b1 b1) (bop b0 (bop (bop b0 b0) b0))) b0 → ⊥
  bad3222  p = false≢true (sym (cong lower p))
  cut3222 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (op (var 3) (var 2)) (var 3)))) , (var 2)) → ⊥
  cut3222  adequate = bad3222  (Adequate.valid adequate Two boolean env26)
  bad3223 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop (bop b1 b0) b1))) b1 → ⊥
  bad3223  p = false≢true (cong lower p)
  cut3223 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (op (var 3) (var 2)) (var 3)))) , (var 3)) → ⊥
  cut3223  adequate = bad3223  (Adequate.valid adequate Two boolean env3)
  bad3224 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop (bop b0 b0) b0))) b1 → ⊥
  bad3224  p = false≢true (cong lower p)
  cut3224 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (op (var 3) (var 2)) (var 3)))) , (var 4)) → ⊥
  cut3224  adequate = bad3224  (Adequate.valid adequate Two boolean env6)
  bad3225 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b1 (bop (bop b0 b1) b0))) b0 → ⊥
  bad3225  p = false≢true (sym (cong lower p))
  cut3225 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (op (var 3) (var 2)) (var 4)))) , (var 0)) → ⊥
  cut3225  adequate = bad3225  (Adequate.valid adequate Two boolean env16)
  bad3226 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b1 (bop (bop b0 b1) b0))) b0 → ⊥
  bad3226  p = false≢true (sym (cong lower p))
  cut3226 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (op (var 3) (var 2)) (var 4)))) , (var 1)) → ⊥
  cut3226  adequate = bad3226  (Adequate.valid adequate Two boolean env16)
  bad3227 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b1 (bop (bop b0 b1) b1))) b1 → ⊥
  bad3227  p = false≢true (cong lower p)
  cut3227 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (op (var 3) (var 2)) (var 4)))) , (var 2)) → ⊥
  cut3227  adequate = bad3227  (Adequate.valid adequate Two boolean env25)
  bad3228 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop (bop b1 b0) b0))) b1 → ⊥
  bad3228  p = false≢true (cong lower p)
  cut3228 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (op (var 3) (var 2)) (var 4)))) , (var 3)) → ⊥
  cut3228  adequate = bad3228  (Adequate.valid adequate Two boolean env17)
  bad3229 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop (bop b0 b0) b1))) b1 → ⊥
  bad3229  p = false≢true (cong lower p)
  cut3229 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (op (var 3) (var 2)) (var 4)))) , (var 4)) → ⊥
  cut3229  adequate = bad3229  (Adequate.valid adequate Two boolean env6)
  bad3230 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop (bop b0 b0) b0))) b1 → ⊥
  bad3230  p = false≢true (cong lower p)
  cut3230 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (op (var 3) (var 2)) (var 4)))) , (var 5)) → ⊥
  cut3230  adequate = bad3230  (Adequate.valid adequate Two boolean env18)
  bad3231 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b1 (bop (bop b0 b0) b0))) b0 → ⊥
  bad3231  p = false≢true (sym (cong lower p))
  cut3231 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (op (var 3) (var 3)) (var 0)))) , (var 0)) → ⊥
  cut3231  adequate = bad3231  (Adequate.valid adequate Two boolean env5)
  bad3232 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b1 (bop (bop b0 b0) b0))) b0 → ⊥
  bad3232  p = false≢true (sym (cong lower p))
  cut3232 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (op (var 3) (var 3)) (var 0)))) , (var 1)) → ⊥
  cut3232  adequate = bad3232  (Adequate.valid adequate Two boolean env5)
  bad3233 : PathP (λ _ → Two) (bop (bop b1 b0) (bop b1 (bop (bop b0 b0) b1))) b1 → ⊥
  bad3233  p = false≢true (cong lower p)
  cut3233 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (op (var 3) (var 3)) (var 0)))) , (var 2)) → ⊥
  cut3233  adequate = bad3233  (Adequate.valid adequate Two boolean env21)
  bad3234 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop (bop b1 b1) b0))) b1 → ⊥
  bad3234  p = false≢true (cong lower p)
  cut3234 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (op (var 3) (var 3)) (var 0)))) , (var 3)) → ⊥
  cut3234  adequate = bad3234  (Adequate.valid adequate Two boolean env3)
  bad3235 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop (bop b0 b0) b0))) b1 → ⊥
  bad3235  p = false≢true (cong lower p)
  cut3235 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (op (var 3) (var 3)) (var 0)))) , (var 4)) → ⊥
  cut3235  adequate = bad3235  (Adequate.valid adequate Two boolean env6)
  bad3236 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b1 (bop (bop b0 b0) b0))) b0 → ⊥
  bad3236  p = false≢true (sym (cong lower p))
  cut3236 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (op (var 3) (var 3)) (var 1)))) , (var 0)) → ⊥
  cut3236  adequate = bad3236  (Adequate.valid adequate Two boolean env5)
  bad3237 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b1 (bop (bop b0 b0) b0))) b0 → ⊥
  bad3237  p = false≢true (sym (cong lower p))
  cut3237 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (op (var 3) (var 3)) (var 1)))) , (var 1)) → ⊥
  cut3237  adequate = bad3237  (Adequate.valid adequate Two boolean env5)
  bad3238 : PathP (λ _ → Two) (bop (bop b0 b1) (bop b1 (bop (bop b0 b0) b1))) b1 → ⊥
  bad3238  p = false≢true (cong lower p)
  cut3238 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (op (var 3) (var 3)) (var 1)))) , (var 2)) → ⊥
  cut3238  adequate = bad3238  (Adequate.valid adequate Two boolean env13)
  bad3239 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop (bop b1 b1) b0))) b1 → ⊥
  bad3239  p = false≢true (cong lower p)
  cut3239 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (op (var 3) (var 3)) (var 1)))) , (var 3)) → ⊥
  cut3239  adequate = bad3239  (Adequate.valid adequate Two boolean env3)
  bad3240 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop (bop b0 b0) b0))) b1 → ⊥
  bad3240  p = false≢true (cong lower p)
  cut3240 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (op (var 3) (var 3)) (var 1)))) , (var 4)) → ⊥
  cut3240  adequate = bad3240  (Adequate.valid adequate Two boolean env6)
  bad3241 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b1 (bop (bop b1 b1) b1))) b0 → ⊥
  bad3241  p = false≢true (sym (cong lower p))
  cut3241 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (op (var 3) (var 3)) (var 2)))) , (var 0)) → ⊥
  cut3241  adequate = bad3241  (Adequate.valid adequate Two boolean env24)
  bad3242 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b1 (bop (bop b1 b1) b1))) b0 → ⊥
  bad3242  p = false≢true (sym (cong lower p))
  cut3242 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (op (var 3) (var 3)) (var 2)))) , (var 1)) → ⊥
  cut3242  adequate = bad3242  (Adequate.valid adequate Two boolean env24)
  bad3243 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b1 (bop (bop b0 b0) b1))) b1 → ⊥
  bad3243  p = false≢true (cong lower p)
  cut3243 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (op (var 3) (var 3)) (var 2)))) , (var 2)) → ⊥
  cut3243  adequate = bad3243  (Adequate.valid adequate Two boolean env5)
  bad3244 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop (bop b1 b1) b0))) b1 → ⊥
  bad3244  p = false≢true (cong lower p)
  cut3244 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (op (var 3) (var 3)) (var 2)))) , (var 3)) → ⊥
  cut3244  adequate = bad3244  (Adequate.valid adequate Two boolean env3)
  bad3245 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop (bop b0 b0) b0))) b1 → ⊥
  bad3245  p = false≢true (cong lower p)
  cut3245 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (op (var 3) (var 3)) (var 2)))) , (var 4)) → ⊥
  cut3245  adequate = bad3245  (Adequate.valid adequate Two boolean env6)
  bad3246 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b1 (bop (bop b0 b0) b0))) b0 → ⊥
  bad3246  p = false≢true (sym (cong lower p))
  cut3246 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (op (var 3) (var 3)) (var 3)))) , (var 0)) → ⊥
  cut3246  adequate = bad3246  (Adequate.valid adequate Two boolean env5)
  bad3247 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b1 (bop (bop b0 b0) b0))) b0 → ⊥
  bad3247  p = false≢true (sym (cong lower p))
  cut3247 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (op (var 3) (var 3)) (var 3)))) , (var 1)) → ⊥
  cut3247  adequate = bad3247  (Adequate.valid adequate Two boolean env5)
  bad3248 : PathP (λ _ → Two) (bop (bop b1 b1) (bop b0 (bop (bop b0 b0) b0))) b0 → ⊥
  bad3248  p = false≢true (sym (cong lower p))
  cut3248 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (op (var 3) (var 3)) (var 3)))) , (var 2)) → ⊥
  cut3248  adequate = bad3248  (Adequate.valid adequate Two boolean env26)
  bad3249 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop (bop b1 b1) b1))) b1 → ⊥
  bad3249  p = false≢true (cong lower p)
  cut3249 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (op (var 3) (var 3)) (var 3)))) , (var 3)) → ⊥
  cut3249  adequate = bad3249  (Adequate.valid adequate Two boolean env3)
  bad3250 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop (bop b0 b0) b0))) b1 → ⊥
  bad3250  p = false≢true (cong lower p)
  cut3250 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (op (var 3) (var 3)) (var 3)))) , (var 4)) → ⊥
  cut3250  adequate = bad3250  (Adequate.valid adequate Two boolean env6)
  bad3251 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b1 (bop (bop b0 b0) b0))) b0 → ⊥
  bad3251  p = false≢true (sym (cong lower p))
  cut3251 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (op (var 3) (var 3)) (var 4)))) , (var 0)) → ⊥
  cut3251  adequate = bad3251  (Adequate.valid adequate Two boolean env16)
  bad3252 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b1 (bop (bop b0 b0) b0))) b0 → ⊥
  bad3252  p = false≢true (sym (cong lower p))
  cut3252 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (op (var 3) (var 3)) (var 4)))) , (var 1)) → ⊥
  cut3252  adequate = bad3252  (Adequate.valid adequate Two boolean env16)
  bad3253 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b1 (bop (bop b0 b0) b1))) b1 → ⊥
  bad3253  p = false≢true (cong lower p)
  cut3253 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (op (var 3) (var 3)) (var 4)))) , (var 2)) → ⊥
  cut3253  adequate = bad3253  (Adequate.valid adequate Two boolean env25)
  bad3254 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop (bop b1 b1) b0))) b1 → ⊥
  bad3254  p = false≢true (cong lower p)
  cut3254 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (op (var 3) (var 3)) (var 4)))) , (var 3)) → ⊥
  cut3254  adequate = bad3254  (Adequate.valid adequate Two boolean env17)
  bad3255 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop (bop b0 b0) b1))) b1 → ⊥
  bad3255  p = false≢true (cong lower p)
  cut3255 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (op (var 3) (var 3)) (var 4)))) , (var 4)) → ⊥
  cut3255  adequate = bad3255  (Adequate.valid adequate Two boolean env6)
  bad3256 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop (bop b0 b0) b0))) b1 → ⊥
  bad3256  p = false≢true (cong lower p)
  cut3256 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (op (var 3) (var 3)) (var 4)))) , (var 5)) → ⊥
  cut3256  adequate = bad3256  (Adequate.valid adequate Two boolean env18)
  bad3257 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b1 (bop (bop b0 b0) b0))) b0 → ⊥
  bad3257  p = false≢true (sym (cong lower p))
  cut3257 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (op (var 3) (var 4)) (var 0)))) , (var 0)) → ⊥
  cut3257  adequate = bad3257  (Adequate.valid adequate Two boolean env16)
  bad3258 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b1 (bop (bop b0 b0) b0))) b0 → ⊥
  bad3258  p = false≢true (sym (cong lower p))
  cut3258 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (op (var 3) (var 4)) (var 0)))) , (var 1)) → ⊥
  cut3258  adequate = bad3258  (Adequate.valid adequate Two boolean env16)
  env27 : ℕ → Two
  env27 zero = b1
  env27 (suc zero) = b0
  env27 (suc (suc zero)) = b1
  env27 (suc (suc (suc zero))) = b0
  env27 (suc (suc (suc (suc zero)))) = b0
  env27 (suc (suc (suc (suc (suc rest))))) = b0
  bad3259 : PathP (λ _ → Two) (bop (bop b1 b0) (bop b1 (bop (bop b0 b0) b1))) b1 → ⊥
  bad3259  p = false≢true (cong lower p)
  cut3259 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (op (var 3) (var 4)) (var 0)))) , (var 2)) → ⊥
  cut3259  adequate = bad3259  (Adequate.valid adequate Two boolean env27)
  bad3260 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop (bop b1 b0) b0))) b1 → ⊥
  bad3260  p = false≢true (cong lower p)
  cut3260 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (op (var 3) (var 4)) (var 0)))) , (var 3)) → ⊥
  cut3260  adequate = bad3260  (Adequate.valid adequate Two boolean env17)
  bad3261 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop (bop b0 b1) b0))) b1 → ⊥
  bad3261  p = false≢true (cong lower p)
  cut3261 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (op (var 3) (var 4)) (var 0)))) , (var 4)) → ⊥
  cut3261  adequate = bad3261  (Adequate.valid adequate Two boolean env6)
  bad3262 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop (bop b0 b0) b0))) b1 → ⊥
  bad3262  p = false≢true (cong lower p)
  cut3262 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (op (var 3) (var 4)) (var 0)))) , (var 5)) → ⊥
  cut3262  adequate = bad3262  (Adequate.valid adequate Two boolean env18)
  bad3263 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b1 (bop (bop b0 b0) b0))) b0 → ⊥
  bad3263  p = false≢true (sym (cong lower p))
  cut3263 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (op (var 3) (var 4)) (var 1)))) , (var 0)) → ⊥
  cut3263  adequate = bad3263  (Adequate.valid adequate Two boolean env16)
  bad3264 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b1 (bop (bop b0 b0) b0))) b0 → ⊥
  bad3264  p = false≢true (sym (cong lower p))
  cut3264 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (op (var 3) (var 4)) (var 1)))) , (var 1)) → ⊥
  cut3264  adequate = bad3264  (Adequate.valid adequate Two boolean env16)
  env28 : ℕ → Two
  env28 zero = b0
  env28 (suc zero) = b1
  env28 (suc (suc zero)) = b1
  env28 (suc (suc (suc zero))) = b0
  env28 (suc (suc (suc (suc zero)))) = b0
  env28 (suc (suc (suc (suc (suc rest))))) = b0
  bad3265 : PathP (λ _ → Two) (bop (bop b0 b1) (bop b1 (bop (bop b0 b0) b1))) b1 → ⊥
  bad3265  p = false≢true (cong lower p)
  cut3265 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (op (var 3) (var 4)) (var 1)))) , (var 2)) → ⊥
  cut3265  adequate = bad3265  (Adequate.valid adequate Two boolean env28)
  bad3266 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop (bop b1 b0) b0))) b1 → ⊥
  bad3266  p = false≢true (cong lower p)
  cut3266 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (op (var 3) (var 4)) (var 1)))) , (var 3)) → ⊥
  cut3266  adequate = bad3266  (Adequate.valid adequate Two boolean env17)
  bad3267 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop (bop b0 b1) b0))) b1 → ⊥
  bad3267  p = false≢true (cong lower p)
  cut3267 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (op (var 3) (var 4)) (var 1)))) , (var 4)) → ⊥
  cut3267  adequate = bad3267  (Adequate.valid adequate Two boolean env6)
  bad3268 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop (bop b0 b0) b0))) b1 → ⊥
  bad3268  p = false≢true (cong lower p)
  cut3268 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (op (var 3) (var 4)) (var 1)))) , (var 5)) → ⊥
  cut3268  adequate = bad3268  (Adequate.valid adequate Two boolean env18)
  env29 : ℕ → Two
  env29 zero = b0
  env29 (suc zero) = b0
  env29 (suc (suc zero)) = b1
  env29 (suc (suc (suc zero))) = b1
  env29 (suc (suc (suc (suc zero)))) = b1
  env29 (suc (suc (suc (suc (suc rest))))) = b0
  bad3269 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b1 (bop (bop b1 b1) b1))) b0 → ⊥
  bad3269  p = false≢true (sym (cong lower p))
  cut3269 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (op (var 3) (var 4)) (var 2)))) , (var 0)) → ⊥
  cut3269  adequate = bad3269  (Adequate.valid adequate Two boolean env29)
  bad3270 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b1 (bop (bop b1 b1) b1))) b0 → ⊥
  bad3270  p = false≢true (sym (cong lower p))
  cut3270 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (op (var 3) (var 4)) (var 2)))) , (var 1)) → ⊥
  cut3270  adequate = bad3270  (Adequate.valid adequate Two boolean env29)
  bad3271 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b1 (bop (bop b0 b0) b1))) b1 → ⊥
  bad3271  p = false≢true (cong lower p)
  cut3271 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (op (var 3) (var 4)) (var 2)))) , (var 2)) → ⊥
  cut3271  adequate = bad3271  (Adequate.valid adequate Two boolean env16)
  bad3272 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop (bop b1 b0) b0))) b1 → ⊥
  bad3272  p = false≢true (cong lower p)
  cut3272 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (op (var 3) (var 4)) (var 2)))) , (var 3)) → ⊥
  cut3272  adequate = bad3272  (Adequate.valid adequate Two boolean env17)
  bad3273 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop (bop b0 b1) b0))) b1 → ⊥
  bad3273  p = false≢true (cong lower p)
  cut3273 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (op (var 3) (var 4)) (var 2)))) , (var 4)) → ⊥
  cut3273  adequate = bad3273  (Adequate.valid adequate Two boolean env6)
  bad3274 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop (bop b0 b0) b0))) b1 → ⊥
  bad3274  p = false≢true (cong lower p)
  cut3274 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (op (var 3) (var 4)) (var 2)))) , (var 5)) → ⊥
  cut3274  adequate = bad3274  (Adequate.valid adequate Two boolean env18)
  bad3275 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b1 (bop (bop b0 b0) b0))) b0 → ⊥
  bad3275  p = false≢true (sym (cong lower p))
  cut3275 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (op (var 3) (var 4)) (var 3)))) , (var 0)) → ⊥
  cut3275  adequate = bad3275  (Adequate.valid adequate Two boolean env16)
  bad3276 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b1 (bop (bop b0 b0) b0))) b0 → ⊥
  bad3276  p = false≢true (sym (cong lower p))
  cut3276 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (op (var 3) (var 4)) (var 3)))) , (var 1)) → ⊥
  cut3276  adequate = bad3276  (Adequate.valid adequate Two boolean env16)
  env30 : ℕ → Two
  env30 zero = b0
  env30 (suc zero) = b0
  env30 (suc (suc zero)) = b1
  env30 (suc (suc (suc zero))) = b1
  env30 (suc (suc (suc (suc zero)))) = b0
  env30 (suc (suc (suc (suc (suc rest))))) = b0
  bad3277 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b1 (bop (bop b1 b0) b1))) b1 → ⊥
  bad3277  p = false≢true (cong lower p)
  cut3277 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (op (var 3) (var 4)) (var 3)))) , (var 2)) → ⊥
  cut3277  adequate = bad3277  (Adequate.valid adequate Two boolean env30)
  bad3278 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop (bop b1 b0) b1))) b1 → ⊥
  bad3278  p = false≢true (cong lower p)
  cut3278 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (op (var 3) (var 4)) (var 3)))) , (var 3)) → ⊥
  cut3278  adequate = bad3278  (Adequate.valid adequate Two boolean env17)
  bad3279 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop (bop b0 b1) b0))) b1 → ⊥
  bad3279  p = false≢true (cong lower p)
  cut3279 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (op (var 3) (var 4)) (var 3)))) , (var 4)) → ⊥
  cut3279  adequate = bad3279  (Adequate.valid adequate Two boolean env6)
  bad3280 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop (bop b0 b0) b0))) b1 → ⊥
  bad3280  p = false≢true (cong lower p)
  cut3280 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (op (var 3) (var 4)) (var 3)))) , (var 5)) → ⊥
  cut3280  adequate = bad3280  (Adequate.valid adequate Two boolean env18)
  bad3281 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b1 (bop (bop b0 b0) b0))) b0 → ⊥
  bad3281  p = false≢true (sym (cong lower p))
  cut3281 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (op (var 3) (var 4)) (var 4)))) , (var 0)) → ⊥
  cut3281  adequate = bad3281  (Adequate.valid adequate Two boolean env16)
  bad3282 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b1 (bop (bop b0 b0) b0))) b0 → ⊥
  bad3282  p = false≢true (sym (cong lower p))
  cut3282 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (op (var 3) (var 4)) (var 4)))) , (var 1)) → ⊥
  cut3282  adequate = bad3282  (Adequate.valid adequate Two boolean env16)
  bad3283 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b1 (bop (bop b0 b1) b1))) b1 → ⊥
  bad3283  p = false≢true (cong lower p)
  cut3283 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (op (var 3) (var 4)) (var 4)))) , (var 2)) → ⊥
  cut3283  adequate = bad3283  (Adequate.valid adequate Two boolean env25)
  bad3284 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop (bop b1 b0) b0))) b1 → ⊥
  bad3284  p = false≢true (cong lower p)
  cut3284 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (op (var 3) (var 4)) (var 4)))) , (var 3)) → ⊥
  cut3284  adequate = bad3284  (Adequate.valid adequate Two boolean env17)
  bad3285 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop (bop b0 b1) b1))) b1 → ⊥
  bad3285  p = false≢true (cong lower p)
  cut3285 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (op (var 3) (var 4)) (var 4)))) , (var 4)) → ⊥
  cut3285  adequate = bad3285  (Adequate.valid adequate Two boolean env6)
  bad3286 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop (bop b0 b0) b0))) b1 → ⊥
  bad3286  p = false≢true (cong lower p)
  cut3286 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (op (var 3) (var 4)) (var 4)))) , (var 5)) → ⊥
  cut3286  adequate = bad3286  (Adequate.valid adequate Two boolean env18)
  env31 : ℕ → Two
  env31 zero = b0
  env31 (suc zero) = b0
  env31 (suc (suc zero)) = b1
  env31 (suc (suc (suc zero))) = b0
  env31 (suc (suc (suc (suc zero)))) = b0
  env31 (suc (suc (suc (suc (suc zero))))) = b0
  env31 (suc (suc (suc (suc (suc (suc rest)))))) = b0
  bad3287 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b1 (bop (bop b0 b0) b0))) b0 → ⊥
  bad3287  p = false≢true (sym (cong lower p))
  cut3287 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (op (var 3) (var 4)) (var 5)))) , (var 0)) → ⊥
  cut3287  adequate = bad3287  (Adequate.valid adequate Two boolean env31)
  bad3288 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b1 (bop (bop b0 b0) b0))) b0 → ⊥
  bad3288  p = false≢true (sym (cong lower p))
  cut3288 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (op (var 3) (var 4)) (var 5)))) , (var 1)) → ⊥
  cut3288  adequate = bad3288  (Adequate.valid adequate Two boolean env31)
  env32 : ℕ → Two
  env32 zero = b0
  env32 (suc zero) = b0
  env32 (suc (suc zero)) = b1
  env32 (suc (suc (suc zero))) = b0
  env32 (suc (suc (suc (suc zero)))) = b0
  env32 (suc (suc (suc (suc (suc zero))))) = b1
  env32 (suc (suc (suc (suc (suc (suc rest)))))) = b0
  bad3289 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b1 (bop (bop b0 b0) b1))) b1 → ⊥
  bad3289  p = false≢true (cong lower p)
  cut3289 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (op (var 3) (var 4)) (var 5)))) , (var 2)) → ⊥
  cut3289  adequate = bad3289  (Adequate.valid adequate Two boolean env32)
  env33 : ℕ → Two
  env33 zero = b0
  env33 (suc zero) = b0
  env33 (suc (suc zero)) = b0
  env33 (suc (suc (suc zero))) = b1
  env33 (suc (suc (suc (suc zero)))) = b0
  env33 (suc (suc (suc (suc (suc zero))))) = b0
  env33 (suc (suc (suc (suc (suc (suc rest)))))) = b0
  bad3290 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop (bop b1 b0) b0))) b1 → ⊥
  bad3290  p = false≢true (cong lower p)
  cut3290 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (op (var 3) (var 4)) (var 5)))) , (var 3)) → ⊥
  cut3290  adequate = bad3290  (Adequate.valid adequate Two boolean env33)
  env34 : ℕ → Two
  env34 zero = b0
  env34 (suc zero) = b0
  env34 (suc (suc zero)) = b0
  env34 (suc (suc (suc zero))) = b0
  env34 (suc (suc (suc (suc zero)))) = b1
  env34 (suc (suc (suc (suc (suc zero))))) = b0
  env34 (suc (suc (suc (suc (suc (suc rest)))))) = b0
  bad3291 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop (bop b0 b1) b0))) b1 → ⊥
  bad3291  p = false≢true (cong lower p)
  cut3291 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (op (var 3) (var 4)) (var 5)))) , (var 4)) → ⊥
  cut3291  adequate = bad3291  (Adequate.valid adequate Two boolean env34)
  bad3292 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop (bop b0 b0) b1))) b1 → ⊥
  bad3292  p = false≢true (cong lower p)
  cut3292 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (op (var 3) (var 4)) (var 5)))) , (var 5)) → ⊥
  cut3292  adequate = bad3292  (Adequate.valid adequate Two boolean env18)
  env35 : ℕ → Two
  env35 zero = b0
  env35 (suc zero) = b0
  env35 (suc (suc zero)) = b0
  env35 (suc (suc (suc zero))) = b0
  env35 (suc (suc (suc (suc zero)))) = b0
  env35 (suc (suc (suc (suc (suc zero))))) = b0
  env35 (suc (suc (suc (suc (suc (suc zero)))))) = b1
  env35 (suc (suc (suc (suc (suc (suc (suc rest))))))) = b0
  bad3293 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop (bop b0 b0) b0))) b1 → ⊥
  bad3293  p = false≢true (cong lower p)
  cut3293 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (op (var 3) (var 4)) (var 5)))) , (var 6)) → ⊥
  cut3293  adequate = bad3293  (Adequate.valid adequate Two boolean env35)
