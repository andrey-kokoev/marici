{-# OPTIONS --safe --cubical --guardedness #-}
module GeneratedMinimumShape178 where
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
  holds5930 : (z0 : A1) → (mul1 (mul1 z0 (mul1 (mul1 z0 z0) z0)) (mul1 z0 z0)) ≡ z0
  holds5930 m1c0 = refl
  holds5930 m1c1 = refl
  cut5930 : Adequate {ℓ} ((op (op (var 0) (op (op (var 0) (var 0)) (var 0))) (op (var 0) (var 0))) , (var 0)) → ⊥
  cut5930  = reject1 ((op (op (var 0) (op (op (var 0) (var 0)) (var 0))) (op (var 0) (var 0))) , (var 0)) (λ env → holds5930 (env 0))
  env0 : ℕ → Two
  env0 zero = b0
  env0 (suc zero) = b1
  env0 (suc (suc rest)) = b0
  bad5931 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b0 b0) b0)) (bop b0 b0)) b1 → ⊥
  bad5931  p = false≢true (cong lower p)
  cut5931 : Adequate {ℓ} ((op (op (var 0) (op (op (var 0) (var 0)) (var 0))) (op (var 0) (var 0))) , (var 1)) → ⊥
  cut5931  adequate = bad5931  (Adequate.valid adequate Two boolean env0)
  holds5932 : (z0 z1 : A2) → (mul2 (mul2 z0 (mul2 (mul2 z0 z0) z0)) (mul2 z0 z1)) ≡ z0
  holds5932 z0 z1 = refl
  cut5932 : Adequate {ℓ} ((op (op (var 0) (op (op (var 0) (var 0)) (var 0))) (op (var 0) (var 1))) , (var 0)) → ⊥
  cut5932  = reject2 ((op (op (var 0) (op (op (var 0) (var 0)) (var 0))) (op (var 0) (var 1))) , (var 0)) (λ env → holds5932 (env 0) (env 1))
  bad5933 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b0 b0) b0)) (bop b0 b1)) b1 → ⊥
  bad5933  p = false≢true (cong lower p)
  cut5933 : Adequate {ℓ} ((op (op (var 0) (op (op (var 0) (var 0)) (var 0))) (op (var 0) (var 1))) , (var 1)) → ⊥
  cut5933  adequate = bad5933  (Adequate.valid adequate Two boolean env0)
  env1 : ℕ → Two
  env1 zero = b0
  env1 (suc zero) = b0
  env1 (suc (suc zero)) = b1
  env1 (suc (suc (suc rest))) = b0
  bad5934 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b0 b0) b0)) (bop b0 b0)) b1 → ⊥
  bad5934  p = false≢true (cong lower p)
  cut5934 : Adequate {ℓ} ((op (op (var 0) (op (op (var 0) (var 0)) (var 0))) (op (var 0) (var 1))) , (var 2)) → ⊥
  cut5934  adequate = bad5934  (Adequate.valid adequate Two boolean env1)
  holds5935 : (z0 z1 : A2) → (mul2 (mul2 z0 (mul2 (mul2 z0 z0) z0)) (mul2 z1 z0)) ≡ z0
  holds5935 z0 z1 = refl
  cut5935 : Adequate {ℓ} ((op (op (var 0) (op (op (var 0) (var 0)) (var 0))) (op (var 1) (var 0))) , (var 0)) → ⊥
  cut5935  = reject2 ((op (op (var 0) (op (op (var 0) (var 0)) (var 0))) (op (var 1) (var 0))) , (var 0)) (λ env → holds5935 (env 0) (env 1))
  bad5936 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b0 b0) b0)) (bop b1 b0)) b1 → ⊥
  bad5936  p = false≢true (cong lower p)
  cut5936 : Adequate {ℓ} ((op (op (var 0) (op (op (var 0) (var 0)) (var 0))) (op (var 1) (var 0))) , (var 1)) → ⊥
  cut5936  adequate = bad5936  (Adequate.valid adequate Two boolean env0)
  bad5937 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b0 b0) b0)) (bop b0 b0)) b1 → ⊥
  bad5937  p = false≢true (cong lower p)
  cut5937 : Adequate {ℓ} ((op (op (var 0) (op (op (var 0) (var 0)) (var 0))) (op (var 1) (var 0))) , (var 2)) → ⊥
  cut5937  adequate = bad5937  (Adequate.valid adequate Two boolean env1)
  bad5938 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b0 b0) b0)) (bop b1 b1)) b0 → ⊥
  bad5938  p = false≢true (sym (cong lower p))
  cut5938 : Adequate {ℓ} ((op (op (var 0) (op (op (var 0) (var 0)) (var 0))) (op (var 1) (var 1))) , (var 0)) → ⊥
  cut5938  adequate = bad5938  (Adequate.valid adequate Two boolean env0)
  env2 : ℕ → Two
  env2 zero = b1
  env2 (suc zero) = b0
  env2 (suc (suc rest)) = b0
  bad5939 : PathP (λ _ → Two) (bop (bop b1 (bop (bop b1 b1) b1)) (bop b0 b0)) b0 → ⊥
  bad5939  p = false≢true (sym (cong lower p))
  cut5939 : Adequate {ℓ} ((op (op (var 0) (op (op (var 0) (var 0)) (var 0))) (op (var 1) (var 1))) , (var 1)) → ⊥
  cut5939  adequate = bad5939  (Adequate.valid adequate Two boolean env2)
  bad5940 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b0 b0) b0)) (bop b0 b0)) b1 → ⊥
  bad5940  p = false≢true (cong lower p)
  cut5940 : Adequate {ℓ} ((op (op (var 0) (op (op (var 0) (var 0)) (var 0))) (op (var 1) (var 1))) , (var 2)) → ⊥
  cut5940  adequate = bad5940  (Adequate.valid adequate Two boolean env1)
  env3 : ℕ → Two
  env3 zero = b0
  env3 (suc zero) = b1
  env3 (suc (suc zero)) = b1
  env3 (suc (suc (suc rest))) = b0
  bad5941 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b0 b0) b0)) (bop b1 b1)) b0 → ⊥
  bad5941  p = false≢true (sym (cong lower p))
  cut5941 : Adequate {ℓ} ((op (op (var 0) (op (op (var 0) (var 0)) (var 0))) (op (var 1) (var 2))) , (var 0)) → ⊥
  cut5941  adequate = bad5941  (Adequate.valid adequate Two boolean env3)
  env4 : ℕ → Two
  env4 zero = b0
  env4 (suc zero) = b1
  env4 (suc (suc zero)) = b0
  env4 (suc (suc (suc rest))) = b0
  bad5942 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b0 b0) b0)) (bop b1 b0)) b1 → ⊥
  bad5942  p = false≢true (cong lower p)
  cut5942 : Adequate {ℓ} ((op (op (var 0) (op (op (var 0) (var 0)) (var 0))) (op (var 1) (var 2))) , (var 1)) → ⊥
  cut5942  adequate = bad5942  (Adequate.valid adequate Two boolean env4)
  bad5943 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b0 b0) b0)) (bop b0 b1)) b1 → ⊥
  bad5943  p = false≢true (cong lower p)
  cut5943 : Adequate {ℓ} ((op (op (var 0) (op (op (var 0) (var 0)) (var 0))) (op (var 1) (var 2))) , (var 2)) → ⊥
  cut5943  adequate = bad5943  (Adequate.valid adequate Two boolean env1)
  env5 : ℕ → Two
  env5 zero = b0
  env5 (suc zero) = b0
  env5 (suc (suc zero)) = b0
  env5 (suc (suc (suc zero))) = b1
  env5 (suc (suc (suc (suc rest)))) = b0
  bad5944 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b0 b0) b0)) (bop b0 b0)) b1 → ⊥
  bad5944  p = false≢true (cong lower p)
  cut5944 : Adequate {ℓ} ((op (op (var 0) (op (op (var 0) (var 0)) (var 0))) (op (var 1) (var 2))) , (var 3)) → ⊥
  cut5944  adequate = bad5944  (Adequate.valid adequate Two boolean env5)
  holds5945 : (z0 z1 : A2) → (mul2 (mul2 z0 (mul2 (mul2 z0 z0) z1)) (mul2 z0 z0)) ≡ z0
  holds5945 z0 z1 = refl
  cut5945 : Adequate {ℓ} ((op (op (var 0) (op (op (var 0) (var 0)) (var 1))) (op (var 0) (var 0))) , (var 0)) → ⊥
  cut5945  = reject2 ((op (op (var 0) (op (op (var 0) (var 0)) (var 1))) (op (var 0) (var 0))) , (var 0)) (λ env → holds5945 (env 0) (env 1))
  bad5946 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b0 b0) b1)) (bop b0 b0)) b1 → ⊥
  bad5946  p = false≢true (cong lower p)
  cut5946 : Adequate {ℓ} ((op (op (var 0) (op (op (var 0) (var 0)) (var 1))) (op (var 0) (var 0))) , (var 1)) → ⊥
  cut5946  adequate = bad5946  (Adequate.valid adequate Two boolean env0)
  bad5947 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b0 b0) b0)) (bop b0 b0)) b1 → ⊥
  bad5947  p = false≢true (cong lower p)
  cut5947 : Adequate {ℓ} ((op (op (var 0) (op (op (var 0) (var 0)) (var 1))) (op (var 0) (var 0))) , (var 2)) → ⊥
  cut5947  adequate = bad5947  (Adequate.valid adequate Two boolean env1)
  holds5948 : (z0 z1 : A2) → (mul2 (mul2 z0 (mul2 (mul2 z0 z0) z1)) (mul2 z0 z1)) ≡ z0
  holds5948 z0 z1 = refl
  cut5948 : Adequate {ℓ} ((op (op (var 0) (op (op (var 0) (var 0)) (var 1))) (op (var 0) (var 1))) , (var 0)) → ⊥
  cut5948  = reject2 ((op (op (var 0) (op (op (var 0) (var 0)) (var 1))) (op (var 0) (var 1))) , (var 0)) (λ env → holds5948 (env 0) (env 1))
  bad5949 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b0 b0) b1)) (bop b0 b1)) b1 → ⊥
  bad5949  p = false≢true (cong lower p)
  cut5949 : Adequate {ℓ} ((op (op (var 0) (op (op (var 0) (var 0)) (var 1))) (op (var 0) (var 1))) , (var 1)) → ⊥
  cut5949  adequate = bad5949  (Adequate.valid adequate Two boolean env0)
  bad5950 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b0 b0) b0)) (bop b0 b0)) b1 → ⊥
  bad5950  p = false≢true (cong lower p)
  cut5950 : Adequate {ℓ} ((op (op (var 0) (op (op (var 0) (var 0)) (var 1))) (op (var 0) (var 1))) , (var 2)) → ⊥
  cut5950  adequate = bad5950  (Adequate.valid adequate Two boolean env1)
  holds5951 : (z0 z1 z2 : A2) → (mul2 (mul2 z0 (mul2 (mul2 z0 z0) z1)) (mul2 z0 z2)) ≡ z0
  holds5951 z0 z1 z2 = refl
  cut5951 : Adequate {ℓ} ((op (op (var 0) (op (op (var 0) (var 0)) (var 1))) (op (var 0) (var 2))) , (var 0)) → ⊥
  cut5951  = reject2 ((op (op (var 0) (op (op (var 0) (var 0)) (var 1))) (op (var 0) (var 2))) , (var 0)) (λ env → holds5951 (env 0) (env 1) (env 2))
  bad5952 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b0 b0) b1)) (bop b0 b0)) b1 → ⊥
  bad5952  p = false≢true (cong lower p)
  cut5952 : Adequate {ℓ} ((op (op (var 0) (op (op (var 0) (var 0)) (var 1))) (op (var 0) (var 2))) , (var 1)) → ⊥
  cut5952  adequate = bad5952  (Adequate.valid adequate Two boolean env4)
  bad5953 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b0 b0) b0)) (bop b0 b1)) b1 → ⊥
  bad5953  p = false≢true (cong lower p)
  cut5953 : Adequate {ℓ} ((op (op (var 0) (op (op (var 0) (var 0)) (var 1))) (op (var 0) (var 2))) , (var 2)) → ⊥
  cut5953  adequate = bad5953  (Adequate.valid adequate Two boolean env1)
  bad5954 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b0 b0) b0)) (bop b0 b0)) b1 → ⊥
  bad5954  p = false≢true (cong lower p)
  cut5954 : Adequate {ℓ} ((op (op (var 0) (op (op (var 0) (var 0)) (var 1))) (op (var 0) (var 2))) , (var 3)) → ⊥
  cut5954  adequate = bad5954  (Adequate.valid adequate Two boolean env5)
  holds5955 : (z0 z1 : A2) → (mul2 (mul2 z0 (mul2 (mul2 z0 z0) z1)) (mul2 z1 z0)) ≡ z0
  holds5955 z0 z1 = refl
  cut5955 : Adequate {ℓ} ((op (op (var 0) (op (op (var 0) (var 0)) (var 1))) (op (var 1) (var 0))) , (var 0)) → ⊥
  cut5955  = reject2 ((op (op (var 0) (op (op (var 0) (var 0)) (var 1))) (op (var 1) (var 0))) , (var 0)) (λ env → holds5955 (env 0) (env 1))
  bad5956 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b0 b0) b1)) (bop b1 b0)) b1 → ⊥
  bad5956  p = false≢true (cong lower p)
  cut5956 : Adequate {ℓ} ((op (op (var 0) (op (op (var 0) (var 0)) (var 1))) (op (var 1) (var 0))) , (var 1)) → ⊥
  cut5956  adequate = bad5956  (Adequate.valid adequate Two boolean env0)
  bad5957 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b0 b0) b0)) (bop b0 b0)) b1 → ⊥
  bad5957  p = false≢true (cong lower p)
  cut5957 : Adequate {ℓ} ((op (op (var 0) (op (op (var 0) (var 0)) (var 1))) (op (var 1) (var 0))) , (var 2)) → ⊥
  cut5957  adequate = bad5957  (Adequate.valid adequate Two boolean env1)
  bad5958 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b0 b0) b1)) (bop b1 b1)) b0 → ⊥
  bad5958  p = false≢true (sym (cong lower p))
  cut5958 : Adequate {ℓ} ((op (op (var 0) (op (op (var 0) (var 0)) (var 1))) (op (var 1) (var 1))) , (var 0)) → ⊥
  cut5958  adequate = bad5958  (Adequate.valid adequate Two boolean env0)
  bad5959 : PathP (λ _ → Two) (bop (bop b1 (bop (bop b1 b1) b0)) (bop b0 b0)) b0 → ⊥
  bad5959  p = false≢true (sym (cong lower p))
  cut5959 : Adequate {ℓ} ((op (op (var 0) (op (op (var 0) (var 0)) (var 1))) (op (var 1) (var 1))) , (var 1)) → ⊥
  cut5959  adequate = bad5959  (Adequate.valid adequate Two boolean env2)
  bad5960 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b0 b0) b0)) (bop b0 b0)) b1 → ⊥
  bad5960  p = false≢true (cong lower p)
  cut5960 : Adequate {ℓ} ((op (op (var 0) (op (op (var 0) (var 0)) (var 1))) (op (var 1) (var 1))) , (var 2)) → ⊥
  cut5960  adequate = bad5960  (Adequate.valid adequate Two boolean env1)
  bad5961 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b0 b0) b1)) (bop b1 b1)) b0 → ⊥
  bad5961  p = false≢true (sym (cong lower p))
  cut5961 : Adequate {ℓ} ((op (op (var 0) (op (op (var 0) (var 0)) (var 1))) (op (var 1) (var 2))) , (var 0)) → ⊥
  cut5961  adequate = bad5961  (Adequate.valid adequate Two boolean env3)
  bad5962 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b0 b0) b1)) (bop b1 b0)) b1 → ⊥
  bad5962  p = false≢true (cong lower p)
  cut5962 : Adequate {ℓ} ((op (op (var 0) (op (op (var 0) (var 0)) (var 1))) (op (var 1) (var 2))) , (var 1)) → ⊥
  cut5962  adequate = bad5962  (Adequate.valid adequate Two boolean env4)
  bad5963 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b0 b0) b0)) (bop b0 b1)) b1 → ⊥
  bad5963  p = false≢true (cong lower p)
  cut5963 : Adequate {ℓ} ((op (op (var 0) (op (op (var 0) (var 0)) (var 1))) (op (var 1) (var 2))) , (var 2)) → ⊥
  cut5963  adequate = bad5963  (Adequate.valid adequate Two boolean env1)
  bad5964 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b0 b0) b0)) (bop b0 b0)) b1 → ⊥
  bad5964  p = false≢true (cong lower p)
  cut5964 : Adequate {ℓ} ((op (op (var 0) (op (op (var 0) (var 0)) (var 1))) (op (var 1) (var 2))) , (var 3)) → ⊥
  cut5964  adequate = bad5964  (Adequate.valid adequate Two boolean env5)
  holds5965 : (z0 z1 z2 : A2) → (mul2 (mul2 z0 (mul2 (mul2 z0 z0) z1)) (mul2 z2 z0)) ≡ z0
  holds5965 z0 z1 z2 = refl
  cut5965 : Adequate {ℓ} ((op (op (var 0) (op (op (var 0) (var 0)) (var 1))) (op (var 2) (var 0))) , (var 0)) → ⊥
  cut5965  = reject2 ((op (op (var 0) (op (op (var 0) (var 0)) (var 1))) (op (var 2) (var 0))) , (var 0)) (λ env → holds5965 (env 0) (env 1) (env 2))
  bad5966 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b0 b0) b1)) (bop b0 b0)) b1 → ⊥
  bad5966  p = false≢true (cong lower p)
  cut5966 : Adequate {ℓ} ((op (op (var 0) (op (op (var 0) (var 0)) (var 1))) (op (var 2) (var 0))) , (var 1)) → ⊥
  cut5966  adequate = bad5966  (Adequate.valid adequate Two boolean env4)
  bad5967 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b0 b0) b0)) (bop b1 b0)) b1 → ⊥
  bad5967  p = false≢true (cong lower p)
  cut5967 : Adequate {ℓ} ((op (op (var 0) (op (op (var 0) (var 0)) (var 1))) (op (var 2) (var 0))) , (var 2)) → ⊥
  cut5967  adequate = bad5967  (Adequate.valid adequate Two boolean env1)
  bad5968 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b0 b0) b0)) (bop b0 b0)) b1 → ⊥
  bad5968  p = false≢true (cong lower p)
  cut5968 : Adequate {ℓ} ((op (op (var 0) (op (op (var 0) (var 0)) (var 1))) (op (var 2) (var 0))) , (var 3)) → ⊥
  cut5968  adequate = bad5968  (Adequate.valid adequate Two boolean env5)
  bad5969 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b0 b0) b1)) (bop b1 b1)) b0 → ⊥
  bad5969  p = false≢true (sym (cong lower p))
  cut5969 : Adequate {ℓ} ((op (op (var 0) (op (op (var 0) (var 0)) (var 1))) (op (var 2) (var 1))) , (var 0)) → ⊥
  cut5969  adequate = bad5969  (Adequate.valid adequate Two boolean env3)
  bad5970 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b0 b0) b1)) (bop b0 b1)) b1 → ⊥
  bad5970  p = false≢true (cong lower p)
  cut5970 : Adequate {ℓ} ((op (op (var 0) (op (op (var 0) (var 0)) (var 1))) (op (var 2) (var 1))) , (var 1)) → ⊥
  cut5970  adequate = bad5970  (Adequate.valid adequate Two boolean env4)
  bad5971 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b0 b0) b0)) (bop b1 b0)) b1 → ⊥
  bad5971  p = false≢true (cong lower p)
  cut5971 : Adequate {ℓ} ((op (op (var 0) (op (op (var 0) (var 0)) (var 1))) (op (var 2) (var 1))) , (var 2)) → ⊥
  cut5971  adequate = bad5971  (Adequate.valid adequate Two boolean env1)
  bad5972 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b0 b0) b0)) (bop b0 b0)) b1 → ⊥
  bad5972  p = false≢true (cong lower p)
  cut5972 : Adequate {ℓ} ((op (op (var 0) (op (op (var 0) (var 0)) (var 1))) (op (var 2) (var 1))) , (var 3)) → ⊥
  cut5972  adequate = bad5972  (Adequate.valid adequate Two boolean env5)
  bad5973 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b0 b0) b0)) (bop b1 b1)) b0 → ⊥
  bad5973  p = false≢true (sym (cong lower p))
  cut5973 : Adequate {ℓ} ((op (op (var 0) (op (op (var 0) (var 0)) (var 1))) (op (var 2) (var 2))) , (var 0)) → ⊥
  cut5973  adequate = bad5973  (Adequate.valid adequate Two boolean env1)
  bad5974 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b0 b0) b0)) (bop b1 b1)) b0 → ⊥
  bad5974  p = false≢true (sym (cong lower p))
  cut5974 : Adequate {ℓ} ((op (op (var 0) (op (op (var 0) (var 0)) (var 1))) (op (var 2) (var 2))) , (var 1)) → ⊥
  cut5974  adequate = bad5974  (Adequate.valid adequate Two boolean env1)
  env6 : ℕ → Two
  env6 zero = b1
  env6 (suc zero) = b0
  env6 (suc (suc zero)) = b0
  env6 (suc (suc (suc rest))) = b0
  bad5975 : PathP (λ _ → Two) (bop (bop b1 (bop (bop b1 b1) b0)) (bop b0 b0)) b0 → ⊥
  bad5975  p = false≢true (sym (cong lower p))
  cut5975 : Adequate {ℓ} ((op (op (var 0) (op (op (var 0) (var 0)) (var 1))) (op (var 2) (var 2))) , (var 2)) → ⊥
  cut5975  adequate = bad5975  (Adequate.valid adequate Two boolean env6)
  bad5976 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b0 b0) b0)) (bop b0 b0)) b1 → ⊥
  bad5976  p = false≢true (cong lower p)
  cut5976 : Adequate {ℓ} ((op (op (var 0) (op (op (var 0) (var 0)) (var 1))) (op (var 2) (var 2))) , (var 3)) → ⊥
  cut5976  adequate = bad5976  (Adequate.valid adequate Two boolean env5)
  env7 : ℕ → Two
  env7 zero = b0
  env7 (suc zero) = b0
  env7 (suc (suc zero)) = b1
  env7 (suc (suc (suc zero))) = b1
  env7 (suc (suc (suc (suc rest)))) = b0
  bad5977 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b0 b0) b0)) (bop b1 b1)) b0 → ⊥
  bad5977  p = false≢true (sym (cong lower p))
  cut5977 : Adequate {ℓ} ((op (op (var 0) (op (op (var 0) (var 0)) (var 1))) (op (var 2) (var 3))) , (var 0)) → ⊥
  cut5977  adequate = bad5977  (Adequate.valid adequate Two boolean env7)
  bad5978 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b0 b0) b0)) (bop b1 b1)) b0 → ⊥
  bad5978  p = false≢true (sym (cong lower p))
  cut5978 : Adequate {ℓ} ((op (op (var 0) (op (op (var 0) (var 0)) (var 1))) (op (var 2) (var 3))) , (var 1)) → ⊥
  cut5978  adequate = bad5978  (Adequate.valid adequate Two boolean env7)
  env8 : ℕ → Two
  env8 zero = b0
  env8 (suc zero) = b0
  env8 (suc (suc zero)) = b1
  env8 (suc (suc (suc zero))) = b0
  env8 (suc (suc (suc (suc rest)))) = b0
  bad5979 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b0 b0) b0)) (bop b1 b0)) b1 → ⊥
  bad5979  p = false≢true (cong lower p)
  cut5979 : Adequate {ℓ} ((op (op (var 0) (op (op (var 0) (var 0)) (var 1))) (op (var 2) (var 3))) , (var 2)) → ⊥
  cut5979  adequate = bad5979  (Adequate.valid adequate Two boolean env8)
  bad5980 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b0 b0) b0)) (bop b0 b1)) b1 → ⊥
  bad5980  p = false≢true (cong lower p)
  cut5980 : Adequate {ℓ} ((op (op (var 0) (op (op (var 0) (var 0)) (var 1))) (op (var 2) (var 3))) , (var 3)) → ⊥
  cut5980  adequate = bad5980  (Adequate.valid adequate Two boolean env5)
  env9 : ℕ → Two
  env9 zero = b0
  env9 (suc zero) = b0
  env9 (suc (suc zero)) = b0
  env9 (suc (suc (suc zero))) = b0
  env9 (suc (suc (suc (suc zero)))) = b1
  env9 (suc (suc (suc (suc (suc rest))))) = b0
  bad5981 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b0 b0) b0)) (bop b0 b0)) b1 → ⊥
  bad5981  p = false≢true (cong lower p)
  cut5981 : Adequate {ℓ} ((op (op (var 0) (op (op (var 0) (var 0)) (var 1))) (op (var 2) (var 3))) , (var 4)) → ⊥
  cut5981  adequate = bad5981  (Adequate.valid adequate Two boolean env9)
  holds5982 : (z0 z1 : A2) → (mul2 (mul2 z0 (mul2 (mul2 z0 z1) z0)) (mul2 z0 z0)) ≡ z0
  holds5982 z0 z1 = refl
  cut5982 : Adequate {ℓ} ((op (op (var 0) (op (op (var 0) (var 1)) (var 0))) (op (var 0) (var 0))) , (var 0)) → ⊥
  cut5982  = reject2 ((op (op (var 0) (op (op (var 0) (var 1)) (var 0))) (op (var 0) (var 0))) , (var 0)) (λ env → holds5982 (env 0) (env 1))
  bad5983 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b0 b1) b0)) (bop b0 b0)) b1 → ⊥
  bad5983  p = false≢true (cong lower p)
  cut5983 : Adequate {ℓ} ((op (op (var 0) (op (op (var 0) (var 1)) (var 0))) (op (var 0) (var 0))) , (var 1)) → ⊥
  cut5983  adequate = bad5983  (Adequate.valid adequate Two boolean env0)
  bad5984 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b0 b0) b0)) (bop b0 b0)) b1 → ⊥
  bad5984  p = false≢true (cong lower p)
  cut5984 : Adequate {ℓ} ((op (op (var 0) (op (op (var 0) (var 1)) (var 0))) (op (var 0) (var 0))) , (var 2)) → ⊥
  cut5984  adequate = bad5984  (Adequate.valid adequate Two boolean env1)
  bad5985 : PathP (λ _ → Two) (bop (bop b1 (bop (bop b1 b0) b1)) (bop b1 b0)) b1 → ⊥
  bad5985  p = false≢true (cong lower p)
  cut5985 : Adequate {ℓ} ((op (op (var 0) (op (op (var 0) (var 1)) (var 0))) (op (var 0) (var 1))) , (var 0)) → ⊥
  cut5985  adequate = bad5985  (Adequate.valid adequate Two boolean env2)
  bad5986 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b0 b1) b0)) (bop b0 b1)) b1 → ⊥
  bad5986  p = false≢true (cong lower p)
  cut5986 : Adequate {ℓ} ((op (op (var 0) (op (op (var 0) (var 1)) (var 0))) (op (var 0) (var 1))) , (var 1)) → ⊥
  cut5986  adequate = bad5986  (Adequate.valid adequate Two boolean env0)
  bad5987 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b0 b0) b0)) (bop b0 b0)) b1 → ⊥
  bad5987  p = false≢true (cong lower p)
  cut5987 : Adequate {ℓ} ((op (op (var 0) (op (op (var 0) (var 1)) (var 0))) (op (var 0) (var 1))) , (var 2)) → ⊥
  cut5987  adequate = bad5987  (Adequate.valid adequate Two boolean env1)
  bad5988 : PathP (λ _ → Two) (bop (bop b1 (bop (bop b1 b0) b1)) (bop b1 b0)) b1 → ⊥
  bad5988  p = false≢true (cong lower p)
  cut5988 : Adequate {ℓ} ((op (op (var 0) (op (op (var 0) (var 1)) (var 0))) (op (var 0) (var 2))) , (var 0)) → ⊥
  cut5988  adequate = bad5988  (Adequate.valid adequate Two boolean env6)
  bad5989 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b0 b1) b0)) (bop b0 b0)) b1 → ⊥
  bad5989  p = false≢true (cong lower p)
  cut5989 : Adequate {ℓ} ((op (op (var 0) (op (op (var 0) (var 1)) (var 0))) (op (var 0) (var 2))) , (var 1)) → ⊥
  cut5989  adequate = bad5989  (Adequate.valid adequate Two boolean env4)
  bad5990 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b0 b0) b0)) (bop b0 b1)) b1 → ⊥
  bad5990  p = false≢true (cong lower p)
  cut5990 : Adequate {ℓ} ((op (op (var 0) (op (op (var 0) (var 1)) (var 0))) (op (var 0) (var 2))) , (var 2)) → ⊥
  cut5990  adequate = bad5990  (Adequate.valid adequate Two boolean env1)
  bad5991 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b0 b0) b0)) (bop b0 b0)) b1 → ⊥
  bad5991  p = false≢true (cong lower p)
  cut5991 : Adequate {ℓ} ((op (op (var 0) (op (op (var 0) (var 1)) (var 0))) (op (var 0) (var 2))) , (var 3)) → ⊥
  cut5991  adequate = bad5991  (Adequate.valid adequate Two boolean env5)
  bad5992 : PathP (λ _ → Two) (bop (bop b1 (bop (bop b1 b0) b1)) (bop b0 b1)) b1 → ⊥
  bad5992  p = false≢true (cong lower p)
  cut5992 : Adequate {ℓ} ((op (op (var 0) (op (op (var 0) (var 1)) (var 0))) (op (var 1) (var 0))) , (var 0)) → ⊥
  cut5992  adequate = bad5992  (Adequate.valid adequate Two boolean env2)
  bad5993 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b0 b1) b0)) (bop b1 b0)) b1 → ⊥
  bad5993  p = false≢true (cong lower p)
  cut5993 : Adequate {ℓ} ((op (op (var 0) (op (op (var 0) (var 1)) (var 0))) (op (var 1) (var 0))) , (var 1)) → ⊥
  cut5993  adequate = bad5993  (Adequate.valid adequate Two boolean env0)
  bad5994 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b0 b0) b0)) (bop b0 b0)) b1 → ⊥
  bad5994  p = false≢true (cong lower p)
  cut5994 : Adequate {ℓ} ((op (op (var 0) (op (op (var 0) (var 1)) (var 0))) (op (var 1) (var 0))) , (var 2)) → ⊥
  cut5994  adequate = bad5994  (Adequate.valid adequate Two boolean env1)
  bad5995 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b0 b1) b0)) (bop b1 b1)) b0 → ⊥
  bad5995  p = false≢true (sym (cong lower p))
  cut5995 : Adequate {ℓ} ((op (op (var 0) (op (op (var 0) (var 1)) (var 0))) (op (var 1) (var 1))) , (var 0)) → ⊥
  cut5995  adequate = bad5995  (Adequate.valid adequate Two boolean env0)
  holds5996 : (z0 z1 : A3) → (mul3 (mul3 z0 (mul3 (mul3 z0 z1) z0)) (mul3 z1 z1)) ≡ z1
  holds5996 z0 z1 = refl
  cut5996 : Adequate {ℓ} ((op (op (var 0) (op (op (var 0) (var 1)) (var 0))) (op (var 1) (var 1))) , (var 1)) → ⊥
  cut5996  = reject3 ((op (op (var 0) (op (op (var 0) (var 1)) (var 0))) (op (var 1) (var 1))) , (var 1)) (λ env → holds5996 (env 0) (env 1))
  bad5997 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b0 b0) b0)) (bop b0 b0)) b1 → ⊥
  bad5997  p = false≢true (cong lower p)
  cut5997 : Adequate {ℓ} ((op (op (var 0) (op (op (var 0) (var 1)) (var 0))) (op (var 1) (var 1))) , (var 2)) → ⊥
  cut5997  adequate = bad5997  (Adequate.valid adequate Two boolean env1)
  bad5998 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b0 b1) b0)) (bop b1 b1)) b0 → ⊥
  bad5998  p = false≢true (sym (cong lower p))
  cut5998 : Adequate {ℓ} ((op (op (var 0) (op (op (var 0) (var 1)) (var 0))) (op (var 1) (var 2))) , (var 0)) → ⊥
  cut5998  adequate = bad5998  (Adequate.valid adequate Two boolean env3)
  bad5999 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b0 b1) b0)) (bop b1 b0)) b1 → ⊥
  bad5999  p = false≢true (cong lower p)
  cut5999 : Adequate {ℓ} ((op (op (var 0) (op (op (var 0) (var 1)) (var 0))) (op (var 1) (var 2))) , (var 1)) → ⊥
  cut5999  adequate = bad5999  (Adequate.valid adequate Two boolean env4)
  bad6000 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b0 b0) b0)) (bop b0 b1)) b1 → ⊥
  bad6000  p = false≢true (cong lower p)
  cut6000 : Adequate {ℓ} ((op (op (var 0) (op (op (var 0) (var 1)) (var 0))) (op (var 1) (var 2))) , (var 2)) → ⊥
  cut6000  adequate = bad6000  (Adequate.valid adequate Two boolean env1)
  bad6001 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b0 b0) b0)) (bop b0 b0)) b1 → ⊥
  bad6001  p = false≢true (cong lower p)
  cut6001 : Adequate {ℓ} ((op (op (var 0) (op (op (var 0) (var 1)) (var 0))) (op (var 1) (var 2))) , (var 3)) → ⊥
  cut6001  adequate = bad6001  (Adequate.valid adequate Two boolean env5)
  bad6002 : PathP (λ _ → Two) (bop (bop b1 (bop (bop b1 b0) b1)) (bop b0 b1)) b1 → ⊥
  bad6002  p = false≢true (cong lower p)
  cut6002 : Adequate {ℓ} ((op (op (var 0) (op (op (var 0) (var 1)) (var 0))) (op (var 2) (var 0))) , (var 0)) → ⊥
  cut6002  adequate = bad6002  (Adequate.valid adequate Two boolean env6)
  bad6003 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b0 b1) b0)) (bop b0 b0)) b1 → ⊥
  bad6003  p = false≢true (cong lower p)
  cut6003 : Adequate {ℓ} ((op (op (var 0) (op (op (var 0) (var 1)) (var 0))) (op (var 2) (var 0))) , (var 1)) → ⊥
  cut6003  adequate = bad6003  (Adequate.valid adequate Two boolean env4)
  bad6004 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b0 b0) b0)) (bop b1 b0)) b1 → ⊥
  bad6004  p = false≢true (cong lower p)
  cut6004 : Adequate {ℓ} ((op (op (var 0) (op (op (var 0) (var 1)) (var 0))) (op (var 2) (var 0))) , (var 2)) → ⊥
  cut6004  adequate = bad6004  (Adequate.valid adequate Two boolean env1)
  bad6005 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b0 b0) b0)) (bop b0 b0)) b1 → ⊥
  bad6005  p = false≢true (cong lower p)
  cut6005 : Adequate {ℓ} ((op (op (var 0) (op (op (var 0) (var 1)) (var 0))) (op (var 2) (var 0))) , (var 3)) → ⊥
  cut6005  adequate = bad6005  (Adequate.valid adequate Two boolean env5)
  bad6006 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b0 b1) b0)) (bop b1 b1)) b0 → ⊥
  bad6006  p = false≢true (sym (cong lower p))
  cut6006 : Adequate {ℓ} ((op (op (var 0) (op (op (var 0) (var 1)) (var 0))) (op (var 2) (var 1))) , (var 0)) → ⊥
  cut6006  adequate = bad6006  (Adequate.valid adequate Two boolean env3)
  bad6007 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b0 b1) b0)) (bop b0 b1)) b1 → ⊥
  bad6007  p = false≢true (cong lower p)
  cut6007 : Adequate {ℓ} ((op (op (var 0) (op (op (var 0) (var 1)) (var 0))) (op (var 2) (var 1))) , (var 1)) → ⊥
  cut6007  adequate = bad6007  (Adequate.valid adequate Two boolean env4)
  bad6008 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b0 b0) b0)) (bop b1 b0)) b1 → ⊥
  bad6008  p = false≢true (cong lower p)
  cut6008 : Adequate {ℓ} ((op (op (var 0) (op (op (var 0) (var 1)) (var 0))) (op (var 2) (var 1))) , (var 2)) → ⊥
  cut6008  adequate = bad6008  (Adequate.valid adequate Two boolean env1)
  bad6009 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b0 b0) b0)) (bop b0 b0)) b1 → ⊥
  bad6009  p = false≢true (cong lower p)
  cut6009 : Adequate {ℓ} ((op (op (var 0) (op (op (var 0) (var 1)) (var 0))) (op (var 2) (var 1))) , (var 3)) → ⊥
  cut6009  adequate = bad6009  (Adequate.valid adequate Two boolean env5)
  bad6010 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b0 b0) b0)) (bop b1 b1)) b0 → ⊥
  bad6010  p = false≢true (sym (cong lower p))
  cut6010 : Adequate {ℓ} ((op (op (var 0) (op (op (var 0) (var 1)) (var 0))) (op (var 2) (var 2))) , (var 0)) → ⊥
  cut6010  adequate = bad6010  (Adequate.valid adequate Two boolean env1)
  bad6011 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b0 b0) b0)) (bop b1 b1)) b0 → ⊥
  bad6011  p = false≢true (sym (cong lower p))
  cut6011 : Adequate {ℓ} ((op (op (var 0) (op (op (var 0) (var 1)) (var 0))) (op (var 2) (var 2))) , (var 1)) → ⊥
  cut6011  adequate = bad6011  (Adequate.valid adequate Two boolean env1)
  env10 : ℕ → Two
  env10 zero = b1
  env10 (suc zero) = b1
  env10 (suc (suc zero)) = b0
  env10 (suc (suc (suc rest))) = b0
  bad6012 : PathP (λ _ → Two) (bop (bop b1 (bop (bop b1 b1) b1)) (bop b0 b0)) b0 → ⊥
  bad6012  p = false≢true (sym (cong lower p))
  cut6012 : Adequate {ℓ} ((op (op (var 0) (op (op (var 0) (var 1)) (var 0))) (op (var 2) (var 2))) , (var 2)) → ⊥
  cut6012  adequate = bad6012  (Adequate.valid adequate Two boolean env10)
  bad6013 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b0 b0) b0)) (bop b0 b0)) b1 → ⊥
  bad6013  p = false≢true (cong lower p)
  cut6013 : Adequate {ℓ} ((op (op (var 0) (op (op (var 0) (var 1)) (var 0))) (op (var 2) (var 2))) , (var 3)) → ⊥
  cut6013  adequate = bad6013  (Adequate.valid adequate Two boolean env5)
  bad6014 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b0 b0) b0)) (bop b1 b1)) b0 → ⊥
  bad6014  p = false≢true (sym (cong lower p))
  cut6014 : Adequate {ℓ} ((op (op (var 0) (op (op (var 0) (var 1)) (var 0))) (op (var 2) (var 3))) , (var 0)) → ⊥
  cut6014  adequate = bad6014  (Adequate.valid adequate Two boolean env7)
  bad6015 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b0 b0) b0)) (bop b1 b1)) b0 → ⊥
  bad6015  p = false≢true (sym (cong lower p))
  cut6015 : Adequate {ℓ} ((op (op (var 0) (op (op (var 0) (var 1)) (var 0))) (op (var 2) (var 3))) , (var 1)) → ⊥
  cut6015  adequate = bad6015  (Adequate.valid adequate Two boolean env7)
  bad6016 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b0 b0) b0)) (bop b1 b0)) b1 → ⊥
  bad6016  p = false≢true (cong lower p)
  cut6016 : Adequate {ℓ} ((op (op (var 0) (op (op (var 0) (var 1)) (var 0))) (op (var 2) (var 3))) , (var 2)) → ⊥
  cut6016  adequate = bad6016  (Adequate.valid adequate Two boolean env8)
  bad6017 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b0 b0) b0)) (bop b0 b1)) b1 → ⊥
  bad6017  p = false≢true (cong lower p)
  cut6017 : Adequate {ℓ} ((op (op (var 0) (op (op (var 0) (var 1)) (var 0))) (op (var 2) (var 3))) , (var 3)) → ⊥
  cut6017  adequate = bad6017  (Adequate.valid adequate Two boolean env5)
  bad6018 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b0 b0) b0)) (bop b0 b0)) b1 → ⊥
  bad6018  p = false≢true (cong lower p)
  cut6018 : Adequate {ℓ} ((op (op (var 0) (op (op (var 0) (var 1)) (var 0))) (op (var 2) (var 3))) , (var 4)) → ⊥
  cut6018  adequate = bad6018  (Adequate.valid adequate Two boolean env9)
  holds6019 : (z0 z1 : A2) → (mul2 (mul2 z0 (mul2 (mul2 z0 z1) z1)) (mul2 z0 z0)) ≡ z0
  holds6019 z0 z1 = refl
  cut6019 : Adequate {ℓ} ((op (op (var 0) (op (op (var 0) (var 1)) (var 1))) (op (var 0) (var 0))) , (var 0)) → ⊥
  cut6019  = reject2 ((op (op (var 0) (op (op (var 0) (var 1)) (var 1))) (op (var 0) (var 0))) , (var 0)) (λ env → holds6019 (env 0) (env 1))
  bad6020 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b0 b1) b1)) (bop b0 b0)) b1 → ⊥
  bad6020  p = false≢true (cong lower p)
  cut6020 : Adequate {ℓ} ((op (op (var 0) (op (op (var 0) (var 1)) (var 1))) (op (var 0) (var 0))) , (var 1)) → ⊥
  cut6020  adequate = bad6020  (Adequate.valid adequate Two boolean env0)
  bad6021 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b0 b0) b0)) (bop b0 b0)) b1 → ⊥
  bad6021  p = false≢true (cong lower p)
  cut6021 : Adequate {ℓ} ((op (op (var 0) (op (op (var 0) (var 1)) (var 1))) (op (var 0) (var 0))) , (var 2)) → ⊥
  cut6021  adequate = bad6021  (Adequate.valid adequate Two boolean env1)
  holds6022 : (z0 z1 : A2) → (mul2 (mul2 z0 (mul2 (mul2 z0 z1) z1)) (mul2 z0 z1)) ≡ z0
  holds6022 z0 z1 = refl
  cut6022 : Adequate {ℓ} ((op (op (var 0) (op (op (var 0) (var 1)) (var 1))) (op (var 0) (var 1))) , (var 0)) → ⊥
  cut6022  = reject2 ((op (op (var 0) (op (op (var 0) (var 1)) (var 1))) (op (var 0) (var 1))) , (var 0)) (λ env → holds6022 (env 0) (env 1))
  bad6023 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b0 b1) b1)) (bop b0 b1)) b1 → ⊥
  bad6023  p = false≢true (cong lower p)
  cut6023 : Adequate {ℓ} ((op (op (var 0) (op (op (var 0) (var 1)) (var 1))) (op (var 0) (var 1))) , (var 1)) → ⊥
  cut6023  adequate = bad6023  (Adequate.valid adequate Two boolean env0)
  bad6024 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b0 b0) b0)) (bop b0 b0)) b1 → ⊥
  bad6024  p = false≢true (cong lower p)
  cut6024 : Adequate {ℓ} ((op (op (var 0) (op (op (var 0) (var 1)) (var 1))) (op (var 0) (var 1))) , (var 2)) → ⊥
  cut6024  adequate = bad6024  (Adequate.valid adequate Two boolean env1)
  holds6025 : (z0 z1 z2 : A2) → (mul2 (mul2 z0 (mul2 (mul2 z0 z1) z1)) (mul2 z0 z2)) ≡ z0
  holds6025 z0 z1 z2 = refl
  cut6025 : Adequate {ℓ} ((op (op (var 0) (op (op (var 0) (var 1)) (var 1))) (op (var 0) (var 2))) , (var 0)) → ⊥
  cut6025  = reject2 ((op (op (var 0) (op (op (var 0) (var 1)) (var 1))) (op (var 0) (var 2))) , (var 0)) (λ env → holds6025 (env 0) (env 1) (env 2))
  bad6026 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b0 b1) b1)) (bop b0 b0)) b1 → ⊥
  bad6026  p = false≢true (cong lower p)
  cut6026 : Adequate {ℓ} ((op (op (var 0) (op (op (var 0) (var 1)) (var 1))) (op (var 0) (var 2))) , (var 1)) → ⊥
  cut6026  adequate = bad6026  (Adequate.valid adequate Two boolean env4)
  bad6027 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b0 b0) b0)) (bop b0 b1)) b1 → ⊥
  bad6027  p = false≢true (cong lower p)
  cut6027 : Adequate {ℓ} ((op (op (var 0) (op (op (var 0) (var 1)) (var 1))) (op (var 0) (var 2))) , (var 2)) → ⊥
  cut6027  adequate = bad6027  (Adequate.valid adequate Two boolean env1)
  bad6028 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b0 b0) b0)) (bop b0 b0)) b1 → ⊥
  bad6028  p = false≢true (cong lower p)
  cut6028 : Adequate {ℓ} ((op (op (var 0) (op (op (var 0) (var 1)) (var 1))) (op (var 0) (var 2))) , (var 3)) → ⊥
  cut6028  adequate = bad6028  (Adequate.valid adequate Two boolean env5)
  holds6029 : (z0 z1 : A2) → (mul2 (mul2 z0 (mul2 (mul2 z0 z1) z1)) (mul2 z1 z0)) ≡ z0
  holds6029 z0 z1 = refl
  cut6029 : Adequate {ℓ} ((op (op (var 0) (op (op (var 0) (var 1)) (var 1))) (op (var 1) (var 0))) , (var 0)) → ⊥
  cut6029  = reject2 ((op (op (var 0) (op (op (var 0) (var 1)) (var 1))) (op (var 1) (var 0))) , (var 0)) (λ env → holds6029 (env 0) (env 1))
  bad6030 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b0 b1) b1)) (bop b1 b0)) b1 → ⊥
  bad6030  p = false≢true (cong lower p)
  cut6030 : Adequate {ℓ} ((op (op (var 0) (op (op (var 0) (var 1)) (var 1))) (op (var 1) (var 0))) , (var 1)) → ⊥
  cut6030  adequate = bad6030  (Adequate.valid adequate Two boolean env0)
  bad6031 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b0 b0) b0)) (bop b0 b0)) b1 → ⊥
  bad6031  p = false≢true (cong lower p)
  cut6031 : Adequate {ℓ} ((op (op (var 0) (op (op (var 0) (var 1)) (var 1))) (op (var 1) (var 0))) , (var 2)) → ⊥
  cut6031  adequate = bad6031  (Adequate.valid adequate Two boolean env1)
  bad6032 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b0 b1) b1)) (bop b1 b1)) b0 → ⊥
  bad6032  p = false≢true (sym (cong lower p))
  cut6032 : Adequate {ℓ} ((op (op (var 0) (op (op (var 0) (var 1)) (var 1))) (op (var 1) (var 1))) , (var 0)) → ⊥
  cut6032  adequate = bad6032  (Adequate.valid adequate Two boolean env0)
  bad6033 : PathP (λ _ → Two) (bop (bop b1 (bop (bop b1 b0) b0)) (bop b0 b0)) b0 → ⊥
  bad6033  p = false≢true (sym (cong lower p))
  cut6033 : Adequate {ℓ} ((op (op (var 0) (op (op (var 0) (var 1)) (var 1))) (op (var 1) (var 1))) , (var 1)) → ⊥
  cut6033  adequate = bad6033  (Adequate.valid adequate Two boolean env2)
  bad6034 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b0 b0) b0)) (bop b0 b0)) b1 → ⊥
  bad6034  p = false≢true (cong lower p)
  cut6034 : Adequate {ℓ} ((op (op (var 0) (op (op (var 0) (var 1)) (var 1))) (op (var 1) (var 1))) , (var 2)) → ⊥
  cut6034  adequate = bad6034  (Adequate.valid adequate Two boolean env1)
  bad6035 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b0 b1) b1)) (bop b1 b1)) b0 → ⊥
  bad6035  p = false≢true (sym (cong lower p))
  cut6035 : Adequate {ℓ} ((op (op (var 0) (op (op (var 0) (var 1)) (var 1))) (op (var 1) (var 2))) , (var 0)) → ⊥
  cut6035  adequate = bad6035  (Adequate.valid adequate Two boolean env3)
  bad6036 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b0 b1) b1)) (bop b1 b0)) b1 → ⊥
  bad6036  p = false≢true (cong lower p)
  cut6036 : Adequate {ℓ} ((op (op (var 0) (op (op (var 0) (var 1)) (var 1))) (op (var 1) (var 2))) , (var 1)) → ⊥
  cut6036  adequate = bad6036  (Adequate.valid adequate Two boolean env4)
  bad6037 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b0 b0) b0)) (bop b0 b1)) b1 → ⊥
  bad6037  p = false≢true (cong lower p)
  cut6037 : Adequate {ℓ} ((op (op (var 0) (op (op (var 0) (var 1)) (var 1))) (op (var 1) (var 2))) , (var 2)) → ⊥
  cut6037  adequate = bad6037  (Adequate.valid adequate Two boolean env1)
  bad6038 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b0 b0) b0)) (bop b0 b0)) b1 → ⊥
  bad6038  p = false≢true (cong lower p)
  cut6038 : Adequate {ℓ} ((op (op (var 0) (op (op (var 0) (var 1)) (var 1))) (op (var 1) (var 2))) , (var 3)) → ⊥
  cut6038  adequate = bad6038  (Adequate.valid adequate Two boolean env5)
  holds6039 : (z0 z1 z2 : A2) → (mul2 (mul2 z0 (mul2 (mul2 z0 z1) z1)) (mul2 z2 z0)) ≡ z0
  holds6039 z0 z1 z2 = refl
  cut6039 : Adequate {ℓ} ((op (op (var 0) (op (op (var 0) (var 1)) (var 1))) (op (var 2) (var 0))) , (var 0)) → ⊥
  cut6039  = reject2 ((op (op (var 0) (op (op (var 0) (var 1)) (var 1))) (op (var 2) (var 0))) , (var 0)) (λ env → holds6039 (env 0) (env 1) (env 2))
  bad6040 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b0 b1) b1)) (bop b0 b0)) b1 → ⊥
  bad6040  p = false≢true (cong lower p)
  cut6040 : Adequate {ℓ} ((op (op (var 0) (op (op (var 0) (var 1)) (var 1))) (op (var 2) (var 0))) , (var 1)) → ⊥
  cut6040  adequate = bad6040  (Adequate.valid adequate Two boolean env4)
  bad6041 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b0 b0) b0)) (bop b1 b0)) b1 → ⊥
  bad6041  p = false≢true (cong lower p)
  cut6041 : Adequate {ℓ} ((op (op (var 0) (op (op (var 0) (var 1)) (var 1))) (op (var 2) (var 0))) , (var 2)) → ⊥
  cut6041  adequate = bad6041  (Adequate.valid adequate Two boolean env1)
  bad6042 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b0 b0) b0)) (bop b0 b0)) b1 → ⊥
  bad6042  p = false≢true (cong lower p)
  cut6042 : Adequate {ℓ} ((op (op (var 0) (op (op (var 0) (var 1)) (var 1))) (op (var 2) (var 0))) , (var 3)) → ⊥
  cut6042  adequate = bad6042  (Adequate.valid adequate Two boolean env5)
  bad6043 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b0 b1) b1)) (bop b1 b1)) b0 → ⊥
  bad6043  p = false≢true (sym (cong lower p))
  cut6043 : Adequate {ℓ} ((op (op (var 0) (op (op (var 0) (var 1)) (var 1))) (op (var 2) (var 1))) , (var 0)) → ⊥
  cut6043  adequate = bad6043  (Adequate.valid adequate Two boolean env3)
  bad6044 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b0 b1) b1)) (bop b0 b1)) b1 → ⊥
  bad6044  p = false≢true (cong lower p)
  cut6044 : Adequate {ℓ} ((op (op (var 0) (op (op (var 0) (var 1)) (var 1))) (op (var 2) (var 1))) , (var 1)) → ⊥
  cut6044  adequate = bad6044  (Adequate.valid adequate Two boolean env4)
  bad6045 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b0 b0) b0)) (bop b1 b0)) b1 → ⊥
  bad6045  p = false≢true (cong lower p)
  cut6045 : Adequate {ℓ} ((op (op (var 0) (op (op (var 0) (var 1)) (var 1))) (op (var 2) (var 1))) , (var 2)) → ⊥
  cut6045  adequate = bad6045  (Adequate.valid adequate Two boolean env1)
  bad6046 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b0 b0) b0)) (bop b0 b0)) b1 → ⊥
  bad6046  p = false≢true (cong lower p)
  cut6046 : Adequate {ℓ} ((op (op (var 0) (op (op (var 0) (var 1)) (var 1))) (op (var 2) (var 1))) , (var 3)) → ⊥
  cut6046  adequate = bad6046  (Adequate.valid adequate Two boolean env5)
  bad6047 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b0 b0) b0)) (bop b1 b1)) b0 → ⊥
  bad6047  p = false≢true (sym (cong lower p))
  cut6047 : Adequate {ℓ} ((op (op (var 0) (op (op (var 0) (var 1)) (var 1))) (op (var 2) (var 2))) , (var 0)) → ⊥
  cut6047  adequate = bad6047  (Adequate.valid adequate Two boolean env1)
  bad6048 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b0 b0) b0)) (bop b1 b1)) b0 → ⊥
  bad6048  p = false≢true (sym (cong lower p))
  cut6048 : Adequate {ℓ} ((op (op (var 0) (op (op (var 0) (var 1)) (var 1))) (op (var 2) (var 2))) , (var 1)) → ⊥
  cut6048  adequate = bad6048  (Adequate.valid adequate Two boolean env1)
  bad6049 : PathP (λ _ → Two) (bop (bop b1 (bop (bop b1 b0) b0)) (bop b0 b0)) b0 → ⊥
  bad6049  p = false≢true (sym (cong lower p))
  cut6049 : Adequate {ℓ} ((op (op (var 0) (op (op (var 0) (var 1)) (var 1))) (op (var 2) (var 2))) , (var 2)) → ⊥
  cut6049  adequate = bad6049  (Adequate.valid adequate Two boolean env6)
  bad6050 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b0 b0) b0)) (bop b0 b0)) b1 → ⊥
  bad6050  p = false≢true (cong lower p)
  cut6050 : Adequate {ℓ} ((op (op (var 0) (op (op (var 0) (var 1)) (var 1))) (op (var 2) (var 2))) , (var 3)) → ⊥
  cut6050  adequate = bad6050  (Adequate.valid adequate Two boolean env5)
  bad6051 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b0 b0) b0)) (bop b1 b1)) b0 → ⊥
  bad6051  p = false≢true (sym (cong lower p))
  cut6051 : Adequate {ℓ} ((op (op (var 0) (op (op (var 0) (var 1)) (var 1))) (op (var 2) (var 3))) , (var 0)) → ⊥
  cut6051  adequate = bad6051  (Adequate.valid adequate Two boolean env7)
  bad6052 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b0 b0) b0)) (bop b1 b1)) b0 → ⊥
  bad6052  p = false≢true (sym (cong lower p))
  cut6052 : Adequate {ℓ} ((op (op (var 0) (op (op (var 0) (var 1)) (var 1))) (op (var 2) (var 3))) , (var 1)) → ⊥
  cut6052  adequate = bad6052  (Adequate.valid adequate Two boolean env7)
  bad6053 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b0 b0) b0)) (bop b1 b0)) b1 → ⊥
  bad6053  p = false≢true (cong lower p)
  cut6053 : Adequate {ℓ} ((op (op (var 0) (op (op (var 0) (var 1)) (var 1))) (op (var 2) (var 3))) , (var 2)) → ⊥
  cut6053  adequate = bad6053  (Adequate.valid adequate Two boolean env8)
  bad6054 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b0 b0) b0)) (bop b0 b1)) b1 → ⊥
  bad6054  p = false≢true (cong lower p)
  cut6054 : Adequate {ℓ} ((op (op (var 0) (op (op (var 0) (var 1)) (var 1))) (op (var 2) (var 3))) , (var 3)) → ⊥
  cut6054  adequate = bad6054  (Adequate.valid adequate Two boolean env5)
  bad6055 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b0 b0) b0)) (bop b0 b0)) b1 → ⊥
  bad6055  p = false≢true (cong lower p)
  cut6055 : Adequate {ℓ} ((op (op (var 0) (op (op (var 0) (var 1)) (var 1))) (op (var 2) (var 3))) , (var 4)) → ⊥
  cut6055  adequate = bad6055  (Adequate.valid adequate Two boolean env9)
  holds6056 : (z0 z1 z2 : A2) → (mul2 (mul2 z0 (mul2 (mul2 z0 z1) z2)) (mul2 z0 z0)) ≡ z0
  holds6056 z0 z1 z2 = refl
  cut6056 : Adequate {ℓ} ((op (op (var 0) (op (op (var 0) (var 1)) (var 2))) (op (var 0) (var 0))) , (var 0)) → ⊥
  cut6056  = reject2 ((op (op (var 0) (op (op (var 0) (var 1)) (var 2))) (op (var 0) (var 0))) , (var 0)) (λ env → holds6056 (env 0) (env 1) (env 2))
  bad6057 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b0 b1) b0)) (bop b0 b0)) b1 → ⊥
  bad6057  p = false≢true (cong lower p)
  cut6057 : Adequate {ℓ} ((op (op (var 0) (op (op (var 0) (var 1)) (var 2))) (op (var 0) (var 0))) , (var 1)) → ⊥
  cut6057  adequate = bad6057  (Adequate.valid adequate Two boolean env4)
  bad6058 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b0 b0) b1)) (bop b0 b0)) b1 → ⊥
  bad6058  p = false≢true (cong lower p)
  cut6058 : Adequate {ℓ} ((op (op (var 0) (op (op (var 0) (var 1)) (var 2))) (op (var 0) (var 0))) , (var 2)) → ⊥
  cut6058  adequate = bad6058  (Adequate.valid adequate Two boolean env1)
  bad6059 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b0 b0) b0)) (bop b0 b0)) b1 → ⊥
  bad6059  p = false≢true (cong lower p)
  cut6059 : Adequate {ℓ} ((op (op (var 0) (op (op (var 0) (var 1)) (var 2))) (op (var 0) (var 0))) , (var 3)) → ⊥
  cut6059  adequate = bad6059  (Adequate.valid adequate Two boolean env5)
  env11 : ℕ → Two
  env11 zero = b1
  env11 (suc zero) = b0
  env11 (suc (suc zero)) = b1
  env11 (suc (suc (suc rest))) = b0
  bad6060 : PathP (λ _ → Two) (bop (bop b1 (bop (bop b1 b0) b1)) (bop b1 b0)) b1 → ⊥
  bad6060  p = false≢true (cong lower p)
  cut6060 : Adequate {ℓ} ((op (op (var 0) (op (op (var 0) (var 1)) (var 2))) (op (var 0) (var 1))) , (var 0)) → ⊥
  cut6060  adequate = bad6060  (Adequate.valid adequate Two boolean env11)
  bad6061 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b0 b1) b0)) (bop b0 b1)) b1 → ⊥
  bad6061  p = false≢true (cong lower p)
  cut6061 : Adequate {ℓ} ((op (op (var 0) (op (op (var 0) (var 1)) (var 2))) (op (var 0) (var 1))) , (var 1)) → ⊥
  cut6061  adequate = bad6061  (Adequate.valid adequate Two boolean env4)
  bad6062 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b0 b0) b1)) (bop b0 b0)) b1 → ⊥
  bad6062  p = false≢true (cong lower p)
  cut6062 : Adequate {ℓ} ((op (op (var 0) (op (op (var 0) (var 1)) (var 2))) (op (var 0) (var 1))) , (var 2)) → ⊥
  cut6062  adequate = bad6062  (Adequate.valid adequate Two boolean env1)
  bad6063 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b0 b0) b0)) (bop b0 b0)) b1 → ⊥
  bad6063  p = false≢true (cong lower p)
  cut6063 : Adequate {ℓ} ((op (op (var 0) (op (op (var 0) (var 1)) (var 2))) (op (var 0) (var 1))) , (var 3)) → ⊥
  cut6063  adequate = bad6063  (Adequate.valid adequate Two boolean env5)
  holds6064 : (z0 z1 z2 : A2) → (mul2 (mul2 z0 (mul2 (mul2 z0 z1) z2)) (mul2 z0 z2)) ≡ z0
  holds6064 z0 z1 z2 = refl
  cut6064 : Adequate {ℓ} ((op (op (var 0) (op (op (var 0) (var 1)) (var 2))) (op (var 0) (var 2))) , (var 0)) → ⊥
  cut6064  = reject2 ((op (op (var 0) (op (op (var 0) (var 1)) (var 2))) (op (var 0) (var 2))) , (var 0)) (λ env → holds6064 (env 0) (env 1) (env 2))
  bad6065 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b0 b1) b0)) (bop b0 b0)) b1 → ⊥
  bad6065  p = false≢true (cong lower p)
  cut6065 : Adequate {ℓ} ((op (op (var 0) (op (op (var 0) (var 1)) (var 2))) (op (var 0) (var 2))) , (var 1)) → ⊥
  cut6065  adequate = bad6065  (Adequate.valid adequate Two boolean env4)
  bad6066 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b0 b0) b1)) (bop b0 b1)) b1 → ⊥
  bad6066  p = false≢true (cong lower p)
  cut6066 : Adequate {ℓ} ((op (op (var 0) (op (op (var 0) (var 1)) (var 2))) (op (var 0) (var 2))) , (var 2)) → ⊥
  cut6066  adequate = bad6066  (Adequate.valid adequate Two boolean env1)
  bad6067 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b0 b0) b0)) (bop b0 b0)) b1 → ⊥
  bad6067  p = false≢true (cong lower p)
  cut6067 : Adequate {ℓ} ((op (op (var 0) (op (op (var 0) (var 1)) (var 2))) (op (var 0) (var 2))) , (var 3)) → ⊥
  cut6067  adequate = bad6067  (Adequate.valid adequate Two boolean env5)
  env12 : ℕ → Two
  env12 zero = b1
  env12 (suc zero) = b0
  env12 (suc (suc zero)) = b1
  env12 (suc (suc (suc zero))) = b0
  env12 (suc (suc (suc (suc rest)))) = b0
  bad6068 : PathP (λ _ → Two) (bop (bop b1 (bop (bop b1 b0) b1)) (bop b1 b0)) b1 → ⊥
  bad6068  p = false≢true (cong lower p)
  cut6068 : Adequate {ℓ} ((op (op (var 0) (op (op (var 0) (var 1)) (var 2))) (op (var 0) (var 3))) , (var 0)) → ⊥
  cut6068  adequate = bad6068  (Adequate.valid adequate Two boolean env12)
  env13 : ℕ → Two
  env13 zero = b0
  env13 (suc zero) = b1
  env13 (suc (suc zero)) = b0
  env13 (suc (suc (suc zero))) = b0
  env13 (suc (suc (suc (suc rest)))) = b0
  bad6069 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b0 b1) b0)) (bop b0 b0)) b1 → ⊥
  bad6069  p = false≢true (cong lower p)
  cut6069 : Adequate {ℓ} ((op (op (var 0) (op (op (var 0) (var 1)) (var 2))) (op (var 0) (var 3))) , (var 1)) → ⊥
  cut6069  adequate = bad6069  (Adequate.valid adequate Two boolean env13)
  bad6070 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b0 b0) b1)) (bop b0 b0)) b1 → ⊥
  bad6070  p = false≢true (cong lower p)
  cut6070 : Adequate {ℓ} ((op (op (var 0) (op (op (var 0) (var 1)) (var 2))) (op (var 0) (var 3))) , (var 2)) → ⊥
  cut6070  adequate = bad6070  (Adequate.valid adequate Two boolean env8)
  bad6071 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b0 b0) b0)) (bop b0 b1)) b1 → ⊥
  bad6071  p = false≢true (cong lower p)
  cut6071 : Adequate {ℓ} ((op (op (var 0) (op (op (var 0) (var 1)) (var 2))) (op (var 0) (var 3))) , (var 3)) → ⊥
  cut6071  adequate = bad6071  (Adequate.valid adequate Two boolean env5)
  bad6072 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b0 b0) b0)) (bop b0 b0)) b1 → ⊥
  bad6072  p = false≢true (cong lower p)
  cut6072 : Adequate {ℓ} ((op (op (var 0) (op (op (var 0) (var 1)) (var 2))) (op (var 0) (var 3))) , (var 4)) → ⊥
  cut6072  adequate = bad6072  (Adequate.valid adequate Two boolean env9)
  bad6073 : PathP (λ _ → Two) (bop (bop b1 (bop (bop b1 b0) b1)) (bop b0 b1)) b1 → ⊥
  bad6073  p = false≢true (cong lower p)
  cut6073 : Adequate {ℓ} ((op (op (var 0) (op (op (var 0) (var 1)) (var 2))) (op (var 1) (var 0))) , (var 0)) → ⊥
  cut6073  adequate = bad6073  (Adequate.valid adequate Two boolean env11)
  bad6074 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b0 b1) b0)) (bop b1 b0)) b1 → ⊥
  bad6074  p = false≢true (cong lower p)
  cut6074 : Adequate {ℓ} ((op (op (var 0) (op (op (var 0) (var 1)) (var 2))) (op (var 1) (var 0))) , (var 1)) → ⊥
  cut6074  adequate = bad6074  (Adequate.valid adequate Two boolean env4)
  bad6075 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b0 b0) b1)) (bop b0 b0)) b1 → ⊥
  bad6075  p = false≢true (cong lower p)
  cut6075 : Adequate {ℓ} ((op (op (var 0) (op (op (var 0) (var 1)) (var 2))) (op (var 1) (var 0))) , (var 2)) → ⊥
  cut6075  adequate = bad6075  (Adequate.valid adequate Two boolean env1)
  bad6076 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b0 b0) b0)) (bop b0 b0)) b1 → ⊥
  bad6076  p = false≢true (cong lower p)
  cut6076 : Adequate {ℓ} ((op (op (var 0) (op (op (var 0) (var 1)) (var 2))) (op (var 1) (var 0))) , (var 3)) → ⊥
  cut6076  adequate = bad6076  (Adequate.valid adequate Two boolean env5)
  bad6077 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b0 b1) b0)) (bop b1 b1)) b0 → ⊥
  bad6077  p = false≢true (sym (cong lower p))
  cut6077 : Adequate {ℓ} ((op (op (var 0) (op (op (var 0) (var 1)) (var 2))) (op (var 1) (var 1))) , (var 0)) → ⊥
  cut6077  adequate = bad6077  (Adequate.valid adequate Two boolean env4)
  bad6078 : PathP (λ _ → Two) (bop (bop b1 (bop (bop b1 b0) b0)) (bop b0 b0)) b0 → ⊥
  bad6078  p = false≢true (sym (cong lower p))
  cut6078 : Adequate {ℓ} ((op (op (var 0) (op (op (var 0) (var 1)) (var 2))) (op (var 1) (var 1))) , (var 1)) → ⊥
  cut6078  adequate = bad6078  (Adequate.valid adequate Two boolean env6)
  bad6079 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b0 b0) b1)) (bop b0 b0)) b1 → ⊥
  bad6079  p = false≢true (cong lower p)
  cut6079 : Adequate {ℓ} ((op (op (var 0) (op (op (var 0) (var 1)) (var 2))) (op (var 1) (var 1))) , (var 2)) → ⊥
  cut6079  adequate = bad6079  (Adequate.valid adequate Two boolean env1)
  bad6080 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b0 b0) b0)) (bop b0 b0)) b1 → ⊥
  bad6080  p = false≢true (cong lower p)
  cut6080 : Adequate {ℓ} ((op (op (var 0) (op (op (var 0) (var 1)) (var 2))) (op (var 1) (var 1))) , (var 3)) → ⊥
  cut6080  adequate = bad6080  (Adequate.valid adequate Two boolean env5)
  bad6081 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b0 b1) b1)) (bop b1 b1)) b0 → ⊥
  bad6081  p = false≢true (sym (cong lower p))
  cut6081 : Adequate {ℓ} ((op (op (var 0) (op (op (var 0) (var 1)) (var 2))) (op (var 1) (var 2))) , (var 0)) → ⊥
  cut6081  adequate = bad6081  (Adequate.valid adequate Two boolean env3)
  bad6082 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b0 b1) b0)) (bop b1 b0)) b1 → ⊥
  bad6082  p = false≢true (cong lower p)
  cut6082 : Adequate {ℓ} ((op (op (var 0) (op (op (var 0) (var 1)) (var 2))) (op (var 1) (var 2))) , (var 1)) → ⊥
  cut6082  adequate = bad6082  (Adequate.valid adequate Two boolean env4)
  bad6083 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b0 b0) b1)) (bop b0 b1)) b1 → ⊥
  bad6083  p = false≢true (cong lower p)
  cut6083 : Adequate {ℓ} ((op (op (var 0) (op (op (var 0) (var 1)) (var 2))) (op (var 1) (var 2))) , (var 2)) → ⊥
  cut6083  adequate = bad6083  (Adequate.valid adequate Two boolean env1)
  bad6084 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b0 b0) b0)) (bop b0 b0)) b1 → ⊥
  bad6084  p = false≢true (cong lower p)
  cut6084 : Adequate {ℓ} ((op (op (var 0) (op (op (var 0) (var 1)) (var 2))) (op (var 1) (var 2))) , (var 3)) → ⊥
  cut6084  adequate = bad6084  (Adequate.valid adequate Two boolean env5)
  env14 : ℕ → Two
  env14 zero = b0
  env14 (suc zero) = b1
  env14 (suc (suc zero)) = b0
  env14 (suc (suc (suc zero))) = b1
  env14 (suc (suc (suc (suc rest)))) = b0
  bad6085 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b0 b1) b0)) (bop b1 b1)) b0 → ⊥
  bad6085  p = false≢true (sym (cong lower p))
  cut6085 : Adequate {ℓ} ((op (op (var 0) (op (op (var 0) (var 1)) (var 2))) (op (var 1) (var 3))) , (var 0)) → ⊥
  cut6085  adequate = bad6085  (Adequate.valid adequate Two boolean env14)
  bad6086 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b0 b1) b0)) (bop b1 b0)) b1 → ⊥
  bad6086  p = false≢true (cong lower p)
  cut6086 : Adequate {ℓ} ((op (op (var 0) (op (op (var 0) (var 1)) (var 2))) (op (var 1) (var 3))) , (var 1)) → ⊥
  cut6086  adequate = bad6086  (Adequate.valid adequate Two boolean env13)
  bad6087 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b0 b0) b1)) (bop b0 b0)) b1 → ⊥
  bad6087  p = false≢true (cong lower p)
  cut6087 : Adequate {ℓ} ((op (op (var 0) (op (op (var 0) (var 1)) (var 2))) (op (var 1) (var 3))) , (var 2)) → ⊥
  cut6087  adequate = bad6087  (Adequate.valid adequate Two boolean env8)
  bad6088 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b0 b0) b0)) (bop b0 b1)) b1 → ⊥
  bad6088  p = false≢true (cong lower p)
  cut6088 : Adequate {ℓ} ((op (op (var 0) (op (op (var 0) (var 1)) (var 2))) (op (var 1) (var 3))) , (var 3)) → ⊥
  cut6088  adequate = bad6088  (Adequate.valid adequate Two boolean env5)
  bad6089 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b0 b0) b0)) (bop b0 b0)) b1 → ⊥
  bad6089  p = false≢true (cong lower p)
  cut6089 : Adequate {ℓ} ((op (op (var 0) (op (op (var 0) (var 1)) (var 2))) (op (var 1) (var 3))) , (var 4)) → ⊥
  cut6089  adequate = bad6089  (Adequate.valid adequate Two boolean env9)
  holds6090 : (z0 z1 z2 : A2) → (mul2 (mul2 z0 (mul2 (mul2 z0 z1) z2)) (mul2 z2 z0)) ≡ z0
  holds6090 z0 z1 z2 = refl
  cut6090 : Adequate {ℓ} ((op (op (var 0) (op (op (var 0) (var 1)) (var 2))) (op (var 2) (var 0))) , (var 0)) → ⊥
  cut6090  = reject2 ((op (op (var 0) (op (op (var 0) (var 1)) (var 2))) (op (var 2) (var 0))) , (var 0)) (λ env → holds6090 (env 0) (env 1) (env 2))
  bad6091 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b0 b1) b0)) (bop b0 b0)) b1 → ⊥
  bad6091  p = false≢true (cong lower p)
  cut6091 : Adequate {ℓ} ((op (op (var 0) (op (op (var 0) (var 1)) (var 2))) (op (var 2) (var 0))) , (var 1)) → ⊥
  cut6091  adequate = bad6091  (Adequate.valid adequate Two boolean env4)
  bad6092 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b0 b0) b1)) (bop b1 b0)) b1 → ⊥
  bad6092  p = false≢true (cong lower p)
  cut6092 : Adequate {ℓ} ((op (op (var 0) (op (op (var 0) (var 1)) (var 2))) (op (var 2) (var 0))) , (var 2)) → ⊥
  cut6092  adequate = bad6092  (Adequate.valid adequate Two boolean env1)
  bad6093 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b0 b0) b0)) (bop b0 b0)) b1 → ⊥
  bad6093  p = false≢true (cong lower p)
  cut6093 : Adequate {ℓ} ((op (op (var 0) (op (op (var 0) (var 1)) (var 2))) (op (var 2) (var 0))) , (var 3)) → ⊥
  cut6093  adequate = bad6093  (Adequate.valid adequate Two boolean env5)
  bad6094 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b0 b1) b1)) (bop b1 b1)) b0 → ⊥
  bad6094  p = false≢true (sym (cong lower p))
  cut6094 : Adequate {ℓ} ((op (op (var 0) (op (op (var 0) (var 1)) (var 2))) (op (var 2) (var 1))) , (var 0)) → ⊥
  cut6094  adequate = bad6094  (Adequate.valid adequate Two boolean env3)
  bad6095 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b0 b1) b0)) (bop b0 b1)) b1 → ⊥
  bad6095  p = false≢true (cong lower p)
  cut6095 : Adequate {ℓ} ((op (op (var 0) (op (op (var 0) (var 1)) (var 2))) (op (var 2) (var 1))) , (var 1)) → ⊥
  cut6095  adequate = bad6095  (Adequate.valid adequate Two boolean env4)
  bad6096 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b0 b0) b1)) (bop b1 b0)) b1 → ⊥
  bad6096  p = false≢true (cong lower p)
  cut6096 : Adequate {ℓ} ((op (op (var 0) (op (op (var 0) (var 1)) (var 2))) (op (var 2) (var 1))) , (var 2)) → ⊥
  cut6096  adequate = bad6096  (Adequate.valid adequate Two boolean env1)
  bad6097 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b0 b0) b0)) (bop b0 b0)) b1 → ⊥
  bad6097  p = false≢true (cong lower p)
  cut6097 : Adequate {ℓ} ((op (op (var 0) (op (op (var 0) (var 1)) (var 2))) (op (var 2) (var 1))) , (var 3)) → ⊥
  cut6097  adequate = bad6097  (Adequate.valid adequate Two boolean env5)
  bad6098 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b0 b0) b1)) (bop b1 b1)) b0 → ⊥
  bad6098  p = false≢true (sym (cong lower p))
  cut6098 : Adequate {ℓ} ((op (op (var 0) (op (op (var 0) (var 1)) (var 2))) (op (var 2) (var 2))) , (var 0)) → ⊥
  cut6098  adequate = bad6098  (Adequate.valid adequate Two boolean env1)
  bad6099 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b0 b0) b1)) (bop b1 b1)) b0 → ⊥
  bad6099  p = false≢true (sym (cong lower p))
  cut6099 : Adequate {ℓ} ((op (op (var 0) (op (op (var 0) (var 1)) (var 2))) (op (var 2) (var 2))) , (var 1)) → ⊥
  cut6099  adequate = bad6099  (Adequate.valid adequate Two boolean env1)
  bad6100 : PathP (λ _ → Two) (bop (bop b1 (bop (bop b1 b0) b0)) (bop b0 b0)) b0 → ⊥
  bad6100  p = false≢true (sym (cong lower p))
  cut6100 : Adequate {ℓ} ((op (op (var 0) (op (op (var 0) (var 1)) (var 2))) (op (var 2) (var 2))) , (var 2)) → ⊥
  cut6100  adequate = bad6100  (Adequate.valid adequate Two boolean env6)
  bad6101 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b0 b0) b0)) (bop b0 b0)) b1 → ⊥
  bad6101  p = false≢true (cong lower p)
  cut6101 : Adequate {ℓ} ((op (op (var 0) (op (op (var 0) (var 1)) (var 2))) (op (var 2) (var 2))) , (var 3)) → ⊥
  cut6101  adequate = bad6101  (Adequate.valid adequate Two boolean env5)
  bad6102 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b0 b0) b1)) (bop b1 b1)) b0 → ⊥
  bad6102  p = false≢true (sym (cong lower p))
  cut6102 : Adequate {ℓ} ((op (op (var 0) (op (op (var 0) (var 1)) (var 2))) (op (var 2) (var 3))) , (var 0)) → ⊥
  cut6102  adequate = bad6102  (Adequate.valid adequate Two boolean env7)
  bad6103 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b0 b0) b1)) (bop b1 b1)) b0 → ⊥
  bad6103  p = false≢true (sym (cong lower p))
  cut6103 : Adequate {ℓ} ((op (op (var 0) (op (op (var 0) (var 1)) (var 2))) (op (var 2) (var 3))) , (var 1)) → ⊥
  cut6103  adequate = bad6103  (Adequate.valid adequate Two boolean env7)
  bad6104 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b0 b0) b1)) (bop b1 b0)) b1 → ⊥
  bad6104  p = false≢true (cong lower p)
  cut6104 : Adequate {ℓ} ((op (op (var 0) (op (op (var 0) (var 1)) (var 2))) (op (var 2) (var 3))) , (var 2)) → ⊥
  cut6104  adequate = bad6104  (Adequate.valid adequate Two boolean env8)
  bad6105 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b0 b0) b0)) (bop b0 b1)) b1 → ⊥
  bad6105  p = false≢true (cong lower p)
  cut6105 : Adequate {ℓ} ((op (op (var 0) (op (op (var 0) (var 1)) (var 2))) (op (var 2) (var 3))) , (var 3)) → ⊥
  cut6105  adequate = bad6105  (Adequate.valid adequate Two boolean env5)
  bad6106 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b0 b0) b0)) (bop b0 b0)) b1 → ⊥
  bad6106  p = false≢true (cong lower p)
  cut6106 : Adequate {ℓ} ((op (op (var 0) (op (op (var 0) (var 1)) (var 2))) (op (var 2) (var 3))) , (var 4)) → ⊥
  cut6106  adequate = bad6106  (Adequate.valid adequate Two boolean env9)
  bad6107 : PathP (λ _ → Two) (bop (bop b1 (bop (bop b1 b0) b1)) (bop b0 b1)) b1 → ⊥
  bad6107  p = false≢true (cong lower p)
  cut6107 : Adequate {ℓ} ((op (op (var 0) (op (op (var 0) (var 1)) (var 2))) (op (var 3) (var 0))) , (var 0)) → ⊥
  cut6107  adequate = bad6107  (Adequate.valid adequate Two boolean env12)
  bad6108 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b0 b1) b0)) (bop b0 b0)) b1 → ⊥
  bad6108  p = false≢true (cong lower p)
  cut6108 : Adequate {ℓ} ((op (op (var 0) (op (op (var 0) (var 1)) (var 2))) (op (var 3) (var 0))) , (var 1)) → ⊥
  cut6108  adequate = bad6108  (Adequate.valid adequate Two boolean env13)
  bad6109 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b0 b0) b1)) (bop b0 b0)) b1 → ⊥
  bad6109  p = false≢true (cong lower p)
  cut6109 : Adequate {ℓ} ((op (op (var 0) (op (op (var 0) (var 1)) (var 2))) (op (var 3) (var 0))) , (var 2)) → ⊥
  cut6109  adequate = bad6109  (Adequate.valid adequate Two boolean env8)
  bad6110 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b0 b0) b0)) (bop b1 b0)) b1 → ⊥
  bad6110  p = false≢true (cong lower p)
  cut6110 : Adequate {ℓ} ((op (op (var 0) (op (op (var 0) (var 1)) (var 2))) (op (var 3) (var 0))) , (var 3)) → ⊥
  cut6110  adequate = bad6110  (Adequate.valid adequate Two boolean env5)
  bad6111 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b0 b0) b0)) (bop b0 b0)) b1 → ⊥
  bad6111  p = false≢true (cong lower p)
  cut6111 : Adequate {ℓ} ((op (op (var 0) (op (op (var 0) (var 1)) (var 2))) (op (var 3) (var 0))) , (var 4)) → ⊥
  cut6111  adequate = bad6111  (Adequate.valid adequate Two boolean env9)
  bad6112 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b0 b1) b0)) (bop b1 b1)) b0 → ⊥
  bad6112  p = false≢true (sym (cong lower p))
  cut6112 : Adequate {ℓ} ((op (op (var 0) (op (op (var 0) (var 1)) (var 2))) (op (var 3) (var 1))) , (var 0)) → ⊥
  cut6112  adequate = bad6112  (Adequate.valid adequate Two boolean env14)
  bad6113 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b0 b1) b0)) (bop b0 b1)) b1 → ⊥
  bad6113  p = false≢true (cong lower p)
  cut6113 : Adequate {ℓ} ((op (op (var 0) (op (op (var 0) (var 1)) (var 2))) (op (var 3) (var 1))) , (var 1)) → ⊥
  cut6113  adequate = bad6113  (Adequate.valid adequate Two boolean env13)
  bad6114 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b0 b0) b1)) (bop b0 b0)) b1 → ⊥
  bad6114  p = false≢true (cong lower p)
  cut6114 : Adequate {ℓ} ((op (op (var 0) (op (op (var 0) (var 1)) (var 2))) (op (var 3) (var 1))) , (var 2)) → ⊥
  cut6114  adequate = bad6114  (Adequate.valid adequate Two boolean env8)
  bad6115 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b0 b0) b0)) (bop b1 b0)) b1 → ⊥
  bad6115  p = false≢true (cong lower p)
  cut6115 : Adequate {ℓ} ((op (op (var 0) (op (op (var 0) (var 1)) (var 2))) (op (var 3) (var 1))) , (var 3)) → ⊥
  cut6115  adequate = bad6115  (Adequate.valid adequate Two boolean env5)
  bad6116 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b0 b0) b0)) (bop b0 b0)) b1 → ⊥
  bad6116  p = false≢true (cong lower p)
  cut6116 : Adequate {ℓ} ((op (op (var 0) (op (op (var 0) (var 1)) (var 2))) (op (var 3) (var 1))) , (var 4)) → ⊥
  cut6116  adequate = bad6116  (Adequate.valid adequate Two boolean env9)
  bad6117 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b0 b0) b1)) (bop b1 b1)) b0 → ⊥
  bad6117  p = false≢true (sym (cong lower p))
  cut6117 : Adequate {ℓ} ((op (op (var 0) (op (op (var 0) (var 1)) (var 2))) (op (var 3) (var 2))) , (var 0)) → ⊥
  cut6117  adequate = bad6117  (Adequate.valid adequate Two boolean env7)
  bad6118 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b0 b0) b1)) (bop b1 b1)) b0 → ⊥
  bad6118  p = false≢true (sym (cong lower p))
  cut6118 : Adequate {ℓ} ((op (op (var 0) (op (op (var 0) (var 1)) (var 2))) (op (var 3) (var 2))) , (var 1)) → ⊥
  cut6118  adequate = bad6118  (Adequate.valid adequate Two boolean env7)
  bad6119 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b0 b0) b1)) (bop b0 b1)) b1 → ⊥
  bad6119  p = false≢true (cong lower p)
  cut6119 : Adequate {ℓ} ((op (op (var 0) (op (op (var 0) (var 1)) (var 2))) (op (var 3) (var 2))) , (var 2)) → ⊥
  cut6119  adequate = bad6119  (Adequate.valid adequate Two boolean env8)
  bad6120 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b0 b0) b0)) (bop b1 b0)) b1 → ⊥
  bad6120  p = false≢true (cong lower p)
  cut6120 : Adequate {ℓ} ((op (op (var 0) (op (op (var 0) (var 1)) (var 2))) (op (var 3) (var 2))) , (var 3)) → ⊥
  cut6120  adequate = bad6120  (Adequate.valid adequate Two boolean env5)
  bad6121 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b0 b0) b0)) (bop b0 b0)) b1 → ⊥
  bad6121  p = false≢true (cong lower p)
  cut6121 : Adequate {ℓ} ((op (op (var 0) (op (op (var 0) (var 1)) (var 2))) (op (var 3) (var 2))) , (var 4)) → ⊥
  cut6121  adequate = bad6121  (Adequate.valid adequate Two boolean env9)
  bad6122 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b0 b0) b0)) (bop b1 b1)) b0 → ⊥
  bad6122  p = false≢true (sym (cong lower p))
  cut6122 : Adequate {ℓ} ((op (op (var 0) (op (op (var 0) (var 1)) (var 2))) (op (var 3) (var 3))) , (var 0)) → ⊥
  cut6122  adequate = bad6122  (Adequate.valid adequate Two boolean env5)
  bad6123 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b0 b0) b0)) (bop b1 b1)) b0 → ⊥
  bad6123  p = false≢true (sym (cong lower p))
  cut6123 : Adequate {ℓ} ((op (op (var 0) (op (op (var 0) (var 1)) (var 2))) (op (var 3) (var 3))) , (var 1)) → ⊥
  cut6123  adequate = bad6123  (Adequate.valid adequate Two boolean env5)
  bad6124 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b0 b0) b0)) (bop b1 b1)) b0 → ⊥
  bad6124  p = false≢true (sym (cong lower p))
  cut6124 : Adequate {ℓ} ((op (op (var 0) (op (op (var 0) (var 1)) (var 2))) (op (var 3) (var 3))) , (var 2)) → ⊥
  cut6124  adequate = bad6124  (Adequate.valid adequate Two boolean env5)
  env15 : ℕ → Two
  env15 zero = b1
  env15 (suc zero) = b0
  env15 (suc (suc zero)) = b0
  env15 (suc (suc (suc zero))) = b0
  env15 (suc (suc (suc (suc rest)))) = b0
  bad6125 : PathP (λ _ → Two) (bop (bop b1 (bop (bop b1 b0) b0)) (bop b0 b0)) b0 → ⊥
  bad6125  p = false≢true (sym (cong lower p))
  cut6125 : Adequate {ℓ} ((op (op (var 0) (op (op (var 0) (var 1)) (var 2))) (op (var 3) (var 3))) , (var 3)) → ⊥
  cut6125  adequate = bad6125  (Adequate.valid adequate Two boolean env15)
  bad6126 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b0 b0) b0)) (bop b0 b0)) b1 → ⊥
  bad6126  p = false≢true (cong lower p)
  cut6126 : Adequate {ℓ} ((op (op (var 0) (op (op (var 0) (var 1)) (var 2))) (op (var 3) (var 3))) , (var 4)) → ⊥
  cut6126  adequate = bad6126  (Adequate.valid adequate Two boolean env9)
  env16 : ℕ → Two
  env16 zero = b0
  env16 (suc zero) = b0
  env16 (suc (suc zero)) = b0
  env16 (suc (suc (suc zero))) = b1
  env16 (suc (suc (suc (suc zero)))) = b1
  env16 (suc (suc (suc (suc (suc rest))))) = b0
  bad6127 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b0 b0) b0)) (bop b1 b1)) b0 → ⊥
  bad6127  p = false≢true (sym (cong lower p))
  cut6127 : Adequate {ℓ} ((op (op (var 0) (op (op (var 0) (var 1)) (var 2))) (op (var 3) (var 4))) , (var 0)) → ⊥
  cut6127  adequate = bad6127  (Adequate.valid adequate Two boolean env16)
  bad6128 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b0 b0) b0)) (bop b1 b1)) b0 → ⊥
  bad6128  p = false≢true (sym (cong lower p))
  cut6128 : Adequate {ℓ} ((op (op (var 0) (op (op (var 0) (var 1)) (var 2))) (op (var 3) (var 4))) , (var 1)) → ⊥
  cut6128  adequate = bad6128  (Adequate.valid adequate Two boolean env16)
  bad6129 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b0 b0) b0)) (bop b1 b1)) b0 → ⊥
  bad6129  p = false≢true (sym (cong lower p))
  cut6129 : Adequate {ℓ} ((op (op (var 0) (op (op (var 0) (var 1)) (var 2))) (op (var 3) (var 4))) , (var 2)) → ⊥
  cut6129  adequate = bad6129  (Adequate.valid adequate Two boolean env16)
  env17 : ℕ → Two
  env17 zero = b0
  env17 (suc zero) = b0
  env17 (suc (suc zero)) = b0
  env17 (suc (suc (suc zero))) = b1
  env17 (suc (suc (suc (suc zero)))) = b0
  env17 (suc (suc (suc (suc (suc rest))))) = b0
  bad6130 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b0 b0) b0)) (bop b1 b0)) b1 → ⊥
  bad6130  p = false≢true (cong lower p)
  cut6130 : Adequate {ℓ} ((op (op (var 0) (op (op (var 0) (var 1)) (var 2))) (op (var 3) (var 4))) , (var 3)) → ⊥
  cut6130  adequate = bad6130  (Adequate.valid adequate Two boolean env17)
  bad6131 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b0 b0) b0)) (bop b0 b1)) b1 → ⊥
  bad6131  p = false≢true (cong lower p)
  cut6131 : Adequate {ℓ} ((op (op (var 0) (op (op (var 0) (var 1)) (var 2))) (op (var 3) (var 4))) , (var 4)) → ⊥
  cut6131  adequate = bad6131  (Adequate.valid adequate Two boolean env9)
  env18 : ℕ → Two
  env18 zero = b0
  env18 (suc zero) = b0
  env18 (suc (suc zero)) = b0
  env18 (suc (suc (suc zero))) = b0
  env18 (suc (suc (suc (suc zero)))) = b0
  env18 (suc (suc (suc (suc (suc zero))))) = b1
  env18 (suc (suc (suc (suc (suc (suc rest)))))) = b0
  bad6132 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b0 b0) b0)) (bop b0 b0)) b1 → ⊥
  bad6132  p = false≢true (cong lower p)
  cut6132 : Adequate {ℓ} ((op (op (var 0) (op (op (var 0) (var 1)) (var 2))) (op (var 3) (var 4))) , (var 5)) → ⊥
  cut6132  adequate = bad6132  (Adequate.valid adequate Two boolean env18)
  holds6133 : (z0 z1 : A2) → (mul2 (mul2 z0 (mul2 (mul2 z1 z0) z0)) (mul2 z0 z0)) ≡ z0
  holds6133 z0 z1 = refl
  cut6133 : Adequate {ℓ} ((op (op (var 0) (op (op (var 1) (var 0)) (var 0))) (op (var 0) (var 0))) , (var 0)) → ⊥
  cut6133  = reject2 ((op (op (var 0) (op (op (var 1) (var 0)) (var 0))) (op (var 0) (var 0))) , (var 0)) (λ env → holds6133 (env 0) (env 1))
  bad6134 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b1 b0) b0)) (bop b0 b0)) b1 → ⊥
  bad6134  p = false≢true (cong lower p)
  cut6134 : Adequate {ℓ} ((op (op (var 0) (op (op (var 1) (var 0)) (var 0))) (op (var 0) (var 0))) , (var 1)) → ⊥
  cut6134  adequate = bad6134  (Adequate.valid adequate Two boolean env0)
  bad6135 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b0 b0) b0)) (bop b0 b0)) b1 → ⊥
  bad6135  p = false≢true (cong lower p)
  cut6135 : Adequate {ℓ} ((op (op (var 0) (op (op (var 1) (var 0)) (var 0))) (op (var 0) (var 0))) , (var 2)) → ⊥
  cut6135  adequate = bad6135  (Adequate.valid adequate Two boolean env1)
  bad6136 : PathP (λ _ → Two) (bop (bop b1 (bop (bop b0 b1) b1)) (bop b1 b0)) b1 → ⊥
  bad6136  p = false≢true (cong lower p)
  cut6136 : Adequate {ℓ} ((op (op (var 0) (op (op (var 1) (var 0)) (var 0))) (op (var 0) (var 1))) , (var 0)) → ⊥
  cut6136  adequate = bad6136  (Adequate.valid adequate Two boolean env2)
  bad6137 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b1 b0) b0)) (bop b0 b1)) b1 → ⊥
  bad6137  p = false≢true (cong lower p)
  cut6137 : Adequate {ℓ} ((op (op (var 0) (op (op (var 1) (var 0)) (var 0))) (op (var 0) (var 1))) , (var 1)) → ⊥
  cut6137  adequate = bad6137  (Adequate.valid adequate Two boolean env0)
  bad6138 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b0 b0) b0)) (bop b0 b0)) b1 → ⊥
  bad6138  p = false≢true (cong lower p)
  cut6138 : Adequate {ℓ} ((op (op (var 0) (op (op (var 1) (var 0)) (var 0))) (op (var 0) (var 1))) , (var 2)) → ⊥
  cut6138  adequate = bad6138  (Adequate.valid adequate Two boolean env1)
  bad6139 : PathP (λ _ → Two) (bop (bop b1 (bop (bop b0 b1) b1)) (bop b1 b0)) b1 → ⊥
  bad6139  p = false≢true (cong lower p)
  cut6139 : Adequate {ℓ} ((op (op (var 0) (op (op (var 1) (var 0)) (var 0))) (op (var 0) (var 2))) , (var 0)) → ⊥
  cut6139  adequate = bad6139  (Adequate.valid adequate Two boolean env6)
  bad6140 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b1 b0) b0)) (bop b0 b0)) b1 → ⊥
  bad6140  p = false≢true (cong lower p)
  cut6140 : Adequate {ℓ} ((op (op (var 0) (op (op (var 1) (var 0)) (var 0))) (op (var 0) (var 2))) , (var 1)) → ⊥
  cut6140  adequate = bad6140  (Adequate.valid adequate Two boolean env4)
  bad6141 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b0 b0) b0)) (bop b0 b1)) b1 → ⊥
  bad6141  p = false≢true (cong lower p)
  cut6141 : Adequate {ℓ} ((op (op (var 0) (op (op (var 1) (var 0)) (var 0))) (op (var 0) (var 2))) , (var 2)) → ⊥
  cut6141  adequate = bad6141  (Adequate.valid adequate Two boolean env1)
  bad6142 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b0 b0) b0)) (bop b0 b0)) b1 → ⊥
  bad6142  p = false≢true (cong lower p)
  cut6142 : Adequate {ℓ} ((op (op (var 0) (op (op (var 1) (var 0)) (var 0))) (op (var 0) (var 2))) , (var 3)) → ⊥
  cut6142  adequate = bad6142  (Adequate.valid adequate Two boolean env5)
  bad6143 : PathP (λ _ → Two) (bop (bop b1 (bop (bop b0 b1) b1)) (bop b0 b1)) b1 → ⊥
  bad6143  p = false≢true (cong lower p)
  cut6143 : Adequate {ℓ} ((op (op (var 0) (op (op (var 1) (var 0)) (var 0))) (op (var 1) (var 0))) , (var 0)) → ⊥
  cut6143  adequate = bad6143  (Adequate.valid adequate Two boolean env2)
  bad6144 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b1 b0) b0)) (bop b1 b0)) b1 → ⊥
  bad6144  p = false≢true (cong lower p)
  cut6144 : Adequate {ℓ} ((op (op (var 0) (op (op (var 1) (var 0)) (var 0))) (op (var 1) (var 0))) , (var 1)) → ⊥
  cut6144  adequate = bad6144  (Adequate.valid adequate Two boolean env0)
  bad6145 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b0 b0) b0)) (bop b0 b0)) b1 → ⊥
  bad6145  p = false≢true (cong lower p)
  cut6145 : Adequate {ℓ} ((op (op (var 0) (op (op (var 1) (var 0)) (var 0))) (op (var 1) (var 0))) , (var 2)) → ⊥
  cut6145  adequate = bad6145  (Adequate.valid adequate Two boolean env1)
  bad6146 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b1 b0) b0)) (bop b1 b1)) b0 → ⊥
  bad6146  p = false≢true (sym (cong lower p))
  cut6146 : Adequate {ℓ} ((op (op (var 0) (op (op (var 1) (var 0)) (var 0))) (op (var 1) (var 1))) , (var 0)) → ⊥
  cut6146  adequate = bad6146  (Adequate.valid adequate Two boolean env0)
  holds6147 : (z0 z1 : A3) → (mul3 (mul3 z0 (mul3 (mul3 z1 z0) z0)) (mul3 z1 z1)) ≡ z1
  holds6147 z0 z1 = refl
  cut6147 : Adequate {ℓ} ((op (op (var 0) (op (op (var 1) (var 0)) (var 0))) (op (var 1) (var 1))) , (var 1)) → ⊥
  cut6147  = reject3 ((op (op (var 0) (op (op (var 1) (var 0)) (var 0))) (op (var 1) (var 1))) , (var 1)) (λ env → holds6147 (env 0) (env 1))
  bad6148 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b0 b0) b0)) (bop b0 b0)) b1 → ⊥
  bad6148  p = false≢true (cong lower p)
  cut6148 : Adequate {ℓ} ((op (op (var 0) (op (op (var 1) (var 0)) (var 0))) (op (var 1) (var 1))) , (var 2)) → ⊥
  cut6148  adequate = bad6148  (Adequate.valid adequate Two boolean env1)
  bad6149 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b1 b0) b0)) (bop b1 b1)) b0 → ⊥
  bad6149  p = false≢true (sym (cong lower p))
  cut6149 : Adequate {ℓ} ((op (op (var 0) (op (op (var 1) (var 0)) (var 0))) (op (var 1) (var 2))) , (var 0)) → ⊥
  cut6149  adequate = bad6149  (Adequate.valid adequate Two boolean env3)
  bad6150 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b1 b0) b0)) (bop b1 b0)) b1 → ⊥
  bad6150  p = false≢true (cong lower p)
  cut6150 : Adequate {ℓ} ((op (op (var 0) (op (op (var 1) (var 0)) (var 0))) (op (var 1) (var 2))) , (var 1)) → ⊥
  cut6150  adequate = bad6150  (Adequate.valid adequate Two boolean env4)
  bad6151 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b0 b0) b0)) (bop b0 b1)) b1 → ⊥
  bad6151  p = false≢true (cong lower p)
  cut6151 : Adequate {ℓ} ((op (op (var 0) (op (op (var 1) (var 0)) (var 0))) (op (var 1) (var 2))) , (var 2)) → ⊥
  cut6151  adequate = bad6151  (Adequate.valid adequate Two boolean env1)
  bad6152 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b0 b0) b0)) (bop b0 b0)) b1 → ⊥
  bad6152  p = false≢true (cong lower p)
  cut6152 : Adequate {ℓ} ((op (op (var 0) (op (op (var 1) (var 0)) (var 0))) (op (var 1) (var 2))) , (var 3)) → ⊥
  cut6152  adequate = bad6152  (Adequate.valid adequate Two boolean env5)
  bad6153 : PathP (λ _ → Two) (bop (bop b1 (bop (bop b0 b1) b1)) (bop b0 b1)) b1 → ⊥
  bad6153  p = false≢true (cong lower p)
  cut6153 : Adequate {ℓ} ((op (op (var 0) (op (op (var 1) (var 0)) (var 0))) (op (var 2) (var 0))) , (var 0)) → ⊥
  cut6153  adequate = bad6153  (Adequate.valid adequate Two boolean env6)
  bad6154 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b1 b0) b0)) (bop b0 b0)) b1 → ⊥
  bad6154  p = false≢true (cong lower p)
  cut6154 : Adequate {ℓ} ((op (op (var 0) (op (op (var 1) (var 0)) (var 0))) (op (var 2) (var 0))) , (var 1)) → ⊥
  cut6154  adequate = bad6154  (Adequate.valid adequate Two boolean env4)
  bad6155 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b0 b0) b0)) (bop b1 b0)) b1 → ⊥
  bad6155  p = false≢true (cong lower p)
  cut6155 : Adequate {ℓ} ((op (op (var 0) (op (op (var 1) (var 0)) (var 0))) (op (var 2) (var 0))) , (var 2)) → ⊥
  cut6155  adequate = bad6155  (Adequate.valid adequate Two boolean env1)
  bad6156 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b0 b0) b0)) (bop b0 b0)) b1 → ⊥
  bad6156  p = false≢true (cong lower p)
  cut6156 : Adequate {ℓ} ((op (op (var 0) (op (op (var 1) (var 0)) (var 0))) (op (var 2) (var 0))) , (var 3)) → ⊥
  cut6156  adequate = bad6156  (Adequate.valid adequate Two boolean env5)
  bad6157 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b1 b0) b0)) (bop b1 b1)) b0 → ⊥
  bad6157  p = false≢true (sym (cong lower p))
  cut6157 : Adequate {ℓ} ((op (op (var 0) (op (op (var 1) (var 0)) (var 0))) (op (var 2) (var 1))) , (var 0)) → ⊥
  cut6157  adequate = bad6157  (Adequate.valid adequate Two boolean env3)
  bad6158 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b1 b0) b0)) (bop b0 b1)) b1 → ⊥
  bad6158  p = false≢true (cong lower p)
  cut6158 : Adequate {ℓ} ((op (op (var 0) (op (op (var 1) (var 0)) (var 0))) (op (var 2) (var 1))) , (var 1)) → ⊥
  cut6158  adequate = bad6158  (Adequate.valid adequate Two boolean env4)
  bad6159 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b0 b0) b0)) (bop b1 b0)) b1 → ⊥
  bad6159  p = false≢true (cong lower p)
  cut6159 : Adequate {ℓ} ((op (op (var 0) (op (op (var 1) (var 0)) (var 0))) (op (var 2) (var 1))) , (var 2)) → ⊥
  cut6159  adequate = bad6159  (Adequate.valid adequate Two boolean env1)
  bad6160 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b0 b0) b0)) (bop b0 b0)) b1 → ⊥
  bad6160  p = false≢true (cong lower p)
  cut6160 : Adequate {ℓ} ((op (op (var 0) (op (op (var 1) (var 0)) (var 0))) (op (var 2) (var 1))) , (var 3)) → ⊥
  cut6160  adequate = bad6160  (Adequate.valid adequate Two boolean env5)
  bad6161 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b0 b0) b0)) (bop b1 b1)) b0 → ⊥
  bad6161  p = false≢true (sym (cong lower p))
  cut6161 : Adequate {ℓ} ((op (op (var 0) (op (op (var 1) (var 0)) (var 0))) (op (var 2) (var 2))) , (var 0)) → ⊥
  cut6161  adequate = bad6161  (Adequate.valid adequate Two boolean env1)
  bad6162 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b0 b0) b0)) (bop b1 b1)) b0 → ⊥
  bad6162  p = false≢true (sym (cong lower p))
  cut6162 : Adequate {ℓ} ((op (op (var 0) (op (op (var 1) (var 0)) (var 0))) (op (var 2) (var 2))) , (var 1)) → ⊥
  cut6162  adequate = bad6162  (Adequate.valid adequate Two boolean env1)
  bad6163 : PathP (λ _ → Two) (bop (bop b1 (bop (bop b1 b1) b1)) (bop b0 b0)) b0 → ⊥
  bad6163  p = false≢true (sym (cong lower p))
  cut6163 : Adequate {ℓ} ((op (op (var 0) (op (op (var 1) (var 0)) (var 0))) (op (var 2) (var 2))) , (var 2)) → ⊥
  cut6163  adequate = bad6163  (Adequate.valid adequate Two boolean env10)
  bad6164 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b0 b0) b0)) (bop b0 b0)) b1 → ⊥
  bad6164  p = false≢true (cong lower p)
  cut6164 : Adequate {ℓ} ((op (op (var 0) (op (op (var 1) (var 0)) (var 0))) (op (var 2) (var 2))) , (var 3)) → ⊥
  cut6164  adequate = bad6164  (Adequate.valid adequate Two boolean env5)
  bad6165 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b0 b0) b0)) (bop b1 b1)) b0 → ⊥
  bad6165  p = false≢true (sym (cong lower p))
  cut6165 : Adequate {ℓ} ((op (op (var 0) (op (op (var 1) (var 0)) (var 0))) (op (var 2) (var 3))) , (var 0)) → ⊥
  cut6165  adequate = bad6165  (Adequate.valid adequate Two boolean env7)
  bad6166 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b0 b0) b0)) (bop b1 b1)) b0 → ⊥
  bad6166  p = false≢true (sym (cong lower p))
  cut6166 : Adequate {ℓ} ((op (op (var 0) (op (op (var 1) (var 0)) (var 0))) (op (var 2) (var 3))) , (var 1)) → ⊥
  cut6166  adequate = bad6166  (Adequate.valid adequate Two boolean env7)
  bad6167 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b0 b0) b0)) (bop b1 b0)) b1 → ⊥
  bad6167  p = false≢true (cong lower p)
  cut6167 : Adequate {ℓ} ((op (op (var 0) (op (op (var 1) (var 0)) (var 0))) (op (var 2) (var 3))) , (var 2)) → ⊥
  cut6167  adequate = bad6167  (Adequate.valid adequate Two boolean env8)
  bad6168 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b0 b0) b0)) (bop b0 b1)) b1 → ⊥
  bad6168  p = false≢true (cong lower p)
  cut6168 : Adequate {ℓ} ((op (op (var 0) (op (op (var 1) (var 0)) (var 0))) (op (var 2) (var 3))) , (var 3)) → ⊥
  cut6168  adequate = bad6168  (Adequate.valid adequate Two boolean env5)
  bad6169 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b0 b0) b0)) (bop b0 b0)) b1 → ⊥
  bad6169  p = false≢true (cong lower p)
  cut6169 : Adequate {ℓ} ((op (op (var 0) (op (op (var 1) (var 0)) (var 0))) (op (var 2) (var 3))) , (var 4)) → ⊥
  cut6169  adequate = bad6169  (Adequate.valid adequate Two boolean env9)
  holds6170 : (z0 z1 : A2) → (mul2 (mul2 z0 (mul2 (mul2 z1 z0) z1)) (mul2 z0 z0)) ≡ z0
  holds6170 z0 z1 = refl
  cut6170 : Adequate {ℓ} ((op (op (var 0) (op (op (var 1) (var 0)) (var 1))) (op (var 0) (var 0))) , (var 0)) → ⊥
  cut6170  = reject2 ((op (op (var 0) (op (op (var 1) (var 0)) (var 1))) (op (var 0) (var 0))) , (var 0)) (λ env → holds6170 (env 0) (env 1))
  bad6171 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b1 b0) b1)) (bop b0 b0)) b1 → ⊥
  bad6171  p = false≢true (cong lower p)
  cut6171 : Adequate {ℓ} ((op (op (var 0) (op (op (var 1) (var 0)) (var 1))) (op (var 0) (var 0))) , (var 1)) → ⊥
  cut6171  adequate = bad6171  (Adequate.valid adequate Two boolean env0)
  bad6172 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b0 b0) b0)) (bop b0 b0)) b1 → ⊥
  bad6172  p = false≢true (cong lower p)
  cut6172 : Adequate {ℓ} ((op (op (var 0) (op (op (var 1) (var 0)) (var 1))) (op (var 0) (var 0))) , (var 2)) → ⊥
  cut6172  adequate = bad6172  (Adequate.valid adequate Two boolean env1)
  holds6173 : (z0 z1 : A2) → (mul2 (mul2 z0 (mul2 (mul2 z1 z0) z1)) (mul2 z0 z1)) ≡ z0
  holds6173 z0 z1 = refl
  cut6173 : Adequate {ℓ} ((op (op (var 0) (op (op (var 1) (var 0)) (var 1))) (op (var 0) (var 1))) , (var 0)) → ⊥
  cut6173  = reject2 ((op (op (var 0) (op (op (var 1) (var 0)) (var 1))) (op (var 0) (var 1))) , (var 0)) (λ env → holds6173 (env 0) (env 1))
  bad6174 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b1 b0) b1)) (bop b0 b1)) b1 → ⊥
  bad6174  p = false≢true (cong lower p)
  cut6174 : Adequate {ℓ} ((op (op (var 0) (op (op (var 1) (var 0)) (var 1))) (op (var 0) (var 1))) , (var 1)) → ⊥
  cut6174  adequate = bad6174  (Adequate.valid adequate Two boolean env0)
  bad6175 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b0 b0) b0)) (bop b0 b0)) b1 → ⊥
  bad6175  p = false≢true (cong lower p)
  cut6175 : Adequate {ℓ} ((op (op (var 0) (op (op (var 1) (var 0)) (var 1))) (op (var 0) (var 1))) , (var 2)) → ⊥
  cut6175  adequate = bad6175  (Adequate.valid adequate Two boolean env1)
  holds6176 : (z0 z1 z2 : A2) → (mul2 (mul2 z0 (mul2 (mul2 z1 z0) z1)) (mul2 z0 z2)) ≡ z0
  holds6176 z0 z1 z2 = refl
  cut6176 : Adequate {ℓ} ((op (op (var 0) (op (op (var 1) (var 0)) (var 1))) (op (var 0) (var 2))) , (var 0)) → ⊥
  cut6176  = reject2 ((op (op (var 0) (op (op (var 1) (var 0)) (var 1))) (op (var 0) (var 2))) , (var 0)) (λ env → holds6176 (env 0) (env 1) (env 2))
  bad6177 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b1 b0) b1)) (bop b0 b0)) b1 → ⊥
  bad6177  p = false≢true (cong lower p)
  cut6177 : Adequate {ℓ} ((op (op (var 0) (op (op (var 1) (var 0)) (var 1))) (op (var 0) (var 2))) , (var 1)) → ⊥
  cut6177  adequate = bad6177  (Adequate.valid adequate Two boolean env4)
  bad6178 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b0 b0) b0)) (bop b0 b1)) b1 → ⊥
  bad6178  p = false≢true (cong lower p)
  cut6178 : Adequate {ℓ} ((op (op (var 0) (op (op (var 1) (var 0)) (var 1))) (op (var 0) (var 2))) , (var 2)) → ⊥
  cut6178  adequate = bad6178  (Adequate.valid adequate Two boolean env1)
  bad6179 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b0 b0) b0)) (bop b0 b0)) b1 → ⊥
  bad6179  p = false≢true (cong lower p)
  cut6179 : Adequate {ℓ} ((op (op (var 0) (op (op (var 1) (var 0)) (var 1))) (op (var 0) (var 2))) , (var 3)) → ⊥
  cut6179  adequate = bad6179  (Adequate.valid adequate Two boolean env5)
  holds6180 : (z0 z1 : A2) → (mul2 (mul2 z0 (mul2 (mul2 z1 z0) z1)) (mul2 z1 z0)) ≡ z0
  holds6180 z0 z1 = refl
  cut6180 : Adequate {ℓ} ((op (op (var 0) (op (op (var 1) (var 0)) (var 1))) (op (var 1) (var 0))) , (var 0)) → ⊥
  cut6180  = reject2 ((op (op (var 0) (op (op (var 1) (var 0)) (var 1))) (op (var 1) (var 0))) , (var 0)) (λ env → holds6180 (env 0) (env 1))
  bad6181 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b1 b0) b1)) (bop b1 b0)) b1 → ⊥
  bad6181  p = false≢true (cong lower p)
  cut6181 : Adequate {ℓ} ((op (op (var 0) (op (op (var 1) (var 0)) (var 1))) (op (var 1) (var 0))) , (var 1)) → ⊥
  cut6181  adequate = bad6181  (Adequate.valid adequate Two boolean env0)
  bad6182 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b0 b0) b0)) (bop b0 b0)) b1 → ⊥
  bad6182  p = false≢true (cong lower p)
  cut6182 : Adequate {ℓ} ((op (op (var 0) (op (op (var 1) (var 0)) (var 1))) (op (var 1) (var 0))) , (var 2)) → ⊥
  cut6182  adequate = bad6182  (Adequate.valid adequate Two boolean env1)
  bad6183 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b1 b0) b1)) (bop b1 b1)) b0 → ⊥
  bad6183  p = false≢true (sym (cong lower p))
  cut6183 : Adequate {ℓ} ((op (op (var 0) (op (op (var 1) (var 0)) (var 1))) (op (var 1) (var 1))) , (var 0)) → ⊥
  cut6183  adequate = bad6183  (Adequate.valid adequate Two boolean env0)
  bad6184 : PathP (λ _ → Two) (bop (bop b1 (bop (bop b0 b1) b0)) (bop b0 b0)) b0 → ⊥
  bad6184  p = false≢true (sym (cong lower p))
  cut6184 : Adequate {ℓ} ((op (op (var 0) (op (op (var 1) (var 0)) (var 1))) (op (var 1) (var 1))) , (var 1)) → ⊥
  cut6184  adequate = bad6184  (Adequate.valid adequate Two boolean env2)
  bad6185 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b0 b0) b0)) (bop b0 b0)) b1 → ⊥
  bad6185  p = false≢true (cong lower p)
  cut6185 : Adequate {ℓ} ((op (op (var 0) (op (op (var 1) (var 0)) (var 1))) (op (var 1) (var 1))) , (var 2)) → ⊥
  cut6185  adequate = bad6185  (Adequate.valid adequate Two boolean env1)
  bad6186 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b1 b0) b1)) (bop b1 b1)) b0 → ⊥
  bad6186  p = false≢true (sym (cong lower p))
  cut6186 : Adequate {ℓ} ((op (op (var 0) (op (op (var 1) (var 0)) (var 1))) (op (var 1) (var 2))) , (var 0)) → ⊥
  cut6186  adequate = bad6186  (Adequate.valid adequate Two boolean env3)
  bad6187 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b1 b0) b1)) (bop b1 b0)) b1 → ⊥
  bad6187  p = false≢true (cong lower p)
  cut6187 : Adequate {ℓ} ((op (op (var 0) (op (op (var 1) (var 0)) (var 1))) (op (var 1) (var 2))) , (var 1)) → ⊥
  cut6187  adequate = bad6187  (Adequate.valid adequate Two boolean env4)
  bad6188 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b0 b0) b0)) (bop b0 b1)) b1 → ⊥
  bad6188  p = false≢true (cong lower p)
  cut6188 : Adequate {ℓ} ((op (op (var 0) (op (op (var 1) (var 0)) (var 1))) (op (var 1) (var 2))) , (var 2)) → ⊥
  cut6188  adequate = bad6188  (Adequate.valid adequate Two boolean env1)
  bad6189 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b0 b0) b0)) (bop b0 b0)) b1 → ⊥
  bad6189  p = false≢true (cong lower p)
  cut6189 : Adequate {ℓ} ((op (op (var 0) (op (op (var 1) (var 0)) (var 1))) (op (var 1) (var 2))) , (var 3)) → ⊥
  cut6189  adequate = bad6189  (Adequate.valid adequate Two boolean env5)
  holds6190 : (z0 z1 z2 : A2) → (mul2 (mul2 z0 (mul2 (mul2 z1 z0) z1)) (mul2 z2 z0)) ≡ z0
  holds6190 z0 z1 z2 = refl
  cut6190 : Adequate {ℓ} ((op (op (var 0) (op (op (var 1) (var 0)) (var 1))) (op (var 2) (var 0))) , (var 0)) → ⊥
  cut6190  = reject2 ((op (op (var 0) (op (op (var 1) (var 0)) (var 1))) (op (var 2) (var 0))) , (var 0)) (λ env → holds6190 (env 0) (env 1) (env 2))
  bad6191 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b1 b0) b1)) (bop b0 b0)) b1 → ⊥
  bad6191  p = false≢true (cong lower p)
  cut6191 : Adequate {ℓ} ((op (op (var 0) (op (op (var 1) (var 0)) (var 1))) (op (var 2) (var 0))) , (var 1)) → ⊥
  cut6191  adequate = bad6191  (Adequate.valid adequate Two boolean env4)
  bad6192 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b0 b0) b0)) (bop b1 b0)) b1 → ⊥
  bad6192  p = false≢true (cong lower p)
  cut6192 : Adequate {ℓ} ((op (op (var 0) (op (op (var 1) (var 0)) (var 1))) (op (var 2) (var 0))) , (var 2)) → ⊥
  cut6192  adequate = bad6192  (Adequate.valid adequate Two boolean env1)
  bad6193 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b0 b0) b0)) (bop b0 b0)) b1 → ⊥
  bad6193  p = false≢true (cong lower p)
  cut6193 : Adequate {ℓ} ((op (op (var 0) (op (op (var 1) (var 0)) (var 1))) (op (var 2) (var 0))) , (var 3)) → ⊥
  cut6193  adequate = bad6193  (Adequate.valid adequate Two boolean env5)
  bad6194 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b1 b0) b1)) (bop b1 b1)) b0 → ⊥
  bad6194  p = false≢true (sym (cong lower p))
  cut6194 : Adequate {ℓ} ((op (op (var 0) (op (op (var 1) (var 0)) (var 1))) (op (var 2) (var 1))) , (var 0)) → ⊥
  cut6194  adequate = bad6194  (Adequate.valid adequate Two boolean env3)
  bad6195 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b1 b0) b1)) (bop b0 b1)) b1 → ⊥
  bad6195  p = false≢true (cong lower p)
  cut6195 : Adequate {ℓ} ((op (op (var 0) (op (op (var 1) (var 0)) (var 1))) (op (var 2) (var 1))) , (var 1)) → ⊥
  cut6195  adequate = bad6195  (Adequate.valid adequate Two boolean env4)
  bad6196 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b0 b0) b0)) (bop b1 b0)) b1 → ⊥
  bad6196  p = false≢true (cong lower p)
  cut6196 : Adequate {ℓ} ((op (op (var 0) (op (op (var 1) (var 0)) (var 1))) (op (var 2) (var 1))) , (var 2)) → ⊥
  cut6196  adequate = bad6196  (Adequate.valid adequate Two boolean env1)
  bad6197 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b0 b0) b0)) (bop b0 b0)) b1 → ⊥
  bad6197  p = false≢true (cong lower p)
  cut6197 : Adequate {ℓ} ((op (op (var 0) (op (op (var 1) (var 0)) (var 1))) (op (var 2) (var 1))) , (var 3)) → ⊥
  cut6197  adequate = bad6197  (Adequate.valid adequate Two boolean env5)
  bad6198 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b0 b0) b0)) (bop b1 b1)) b0 → ⊥
  bad6198  p = false≢true (sym (cong lower p))
  cut6198 : Adequate {ℓ} ((op (op (var 0) (op (op (var 1) (var 0)) (var 1))) (op (var 2) (var 2))) , (var 0)) → ⊥
  cut6198  adequate = bad6198  (Adequate.valid adequate Two boolean env1)
  bad6199 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b0 b0) b0)) (bop b1 b1)) b0 → ⊥
  bad6199  p = false≢true (sym (cong lower p))
  cut6199 : Adequate {ℓ} ((op (op (var 0) (op (op (var 1) (var 0)) (var 1))) (op (var 2) (var 2))) , (var 1)) → ⊥
  cut6199  adequate = bad6199  (Adequate.valid adequate Two boolean env1)
  bad6200 : PathP (λ _ → Two) (bop (bop b1 (bop (bop b0 b1) b0)) (bop b0 b0)) b0 → ⊥
  bad6200  p = false≢true (sym (cong lower p))
  cut6200 : Adequate {ℓ} ((op (op (var 0) (op (op (var 1) (var 0)) (var 1))) (op (var 2) (var 2))) , (var 2)) → ⊥
  cut6200  adequate = bad6200  (Adequate.valid adequate Two boolean env6)
  bad6201 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b0 b0) b0)) (bop b0 b0)) b1 → ⊥
  bad6201  p = false≢true (cong lower p)
  cut6201 : Adequate {ℓ} ((op (op (var 0) (op (op (var 1) (var 0)) (var 1))) (op (var 2) (var 2))) , (var 3)) → ⊥
  cut6201  adequate = bad6201  (Adequate.valid adequate Two boolean env5)
  bad6202 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b0 b0) b0)) (bop b1 b1)) b0 → ⊥
  bad6202  p = false≢true (sym (cong lower p))
  cut6202 : Adequate {ℓ} ((op (op (var 0) (op (op (var 1) (var 0)) (var 1))) (op (var 2) (var 3))) , (var 0)) → ⊥
  cut6202  adequate = bad6202  (Adequate.valid adequate Two boolean env7)
  bad6203 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b0 b0) b0)) (bop b1 b1)) b0 → ⊥
  bad6203  p = false≢true (sym (cong lower p))
  cut6203 : Adequate {ℓ} ((op (op (var 0) (op (op (var 1) (var 0)) (var 1))) (op (var 2) (var 3))) , (var 1)) → ⊥
  cut6203  adequate = bad6203  (Adequate.valid adequate Two boolean env7)
  bad6204 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b0 b0) b0)) (bop b1 b0)) b1 → ⊥
  bad6204  p = false≢true (cong lower p)
  cut6204 : Adequate {ℓ} ((op (op (var 0) (op (op (var 1) (var 0)) (var 1))) (op (var 2) (var 3))) , (var 2)) → ⊥
  cut6204  adequate = bad6204  (Adequate.valid adequate Two boolean env8)
  bad6205 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b0 b0) b0)) (bop b0 b1)) b1 → ⊥
  bad6205  p = false≢true (cong lower p)
  cut6205 : Adequate {ℓ} ((op (op (var 0) (op (op (var 1) (var 0)) (var 1))) (op (var 2) (var 3))) , (var 3)) → ⊥
  cut6205  adequate = bad6205  (Adequate.valid adequate Two boolean env5)
  bad6206 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b0 b0) b0)) (bop b0 b0)) b1 → ⊥
  bad6206  p = false≢true (cong lower p)
  cut6206 : Adequate {ℓ} ((op (op (var 0) (op (op (var 1) (var 0)) (var 1))) (op (var 2) (var 3))) , (var 4)) → ⊥
  cut6206  adequate = bad6206  (Adequate.valid adequate Two boolean env9)
  holds6207 : (z0 z1 z2 : A2) → (mul2 (mul2 z0 (mul2 (mul2 z1 z0) z2)) (mul2 z0 z0)) ≡ z0
  holds6207 z0 z1 z2 = refl
  cut6207 : Adequate {ℓ} ((op (op (var 0) (op (op (var 1) (var 0)) (var 2))) (op (var 0) (var 0))) , (var 0)) → ⊥
  cut6207  = reject2 ((op (op (var 0) (op (op (var 1) (var 0)) (var 2))) (op (var 0) (var 0))) , (var 0)) (λ env → holds6207 (env 0) (env 1) (env 2))
  bad6208 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b1 b0) b0)) (bop b0 b0)) b1 → ⊥
  bad6208  p = false≢true (cong lower p)
  cut6208 : Adequate {ℓ} ((op (op (var 0) (op (op (var 1) (var 0)) (var 2))) (op (var 0) (var 0))) , (var 1)) → ⊥
  cut6208  adequate = bad6208  (Adequate.valid adequate Two boolean env4)
  bad6209 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b0 b0) b1)) (bop b0 b0)) b1 → ⊥
  bad6209  p = false≢true (cong lower p)
  cut6209 : Adequate {ℓ} ((op (op (var 0) (op (op (var 1) (var 0)) (var 2))) (op (var 0) (var 0))) , (var 2)) → ⊥
  cut6209  adequate = bad6209  (Adequate.valid adequate Two boolean env1)
  bad6210 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b0 b0) b0)) (bop b0 b0)) b1 → ⊥
  bad6210  p = false≢true (cong lower p)
  cut6210 : Adequate {ℓ} ((op (op (var 0) (op (op (var 1) (var 0)) (var 2))) (op (var 0) (var 0))) , (var 3)) → ⊥
  cut6210  adequate = bad6210  (Adequate.valid adequate Two boolean env5)
  bad6211 : PathP (λ _ → Two) (bop (bop b1 (bop (bop b0 b1) b1)) (bop b1 b0)) b1 → ⊥
  bad6211  p = false≢true (cong lower p)
  cut6211 : Adequate {ℓ} ((op (op (var 0) (op (op (var 1) (var 0)) (var 2))) (op (var 0) (var 1))) , (var 0)) → ⊥
  cut6211  adequate = bad6211  (Adequate.valid adequate Two boolean env11)
  bad6212 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b1 b0) b0)) (bop b0 b1)) b1 → ⊥
  bad6212  p = false≢true (cong lower p)
  cut6212 : Adequate {ℓ} ((op (op (var 0) (op (op (var 1) (var 0)) (var 2))) (op (var 0) (var 1))) , (var 1)) → ⊥
  cut6212  adequate = bad6212  (Adequate.valid adequate Two boolean env4)
  bad6213 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b0 b0) b1)) (bop b0 b0)) b1 → ⊥
  bad6213  p = false≢true (cong lower p)
  cut6213 : Adequate {ℓ} ((op (op (var 0) (op (op (var 1) (var 0)) (var 2))) (op (var 0) (var 1))) , (var 2)) → ⊥
  cut6213  adequate = bad6213  (Adequate.valid adequate Two boolean env1)
  bad6214 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b0 b0) b0)) (bop b0 b0)) b1 → ⊥
  bad6214  p = false≢true (cong lower p)
  cut6214 : Adequate {ℓ} ((op (op (var 0) (op (op (var 1) (var 0)) (var 2))) (op (var 0) (var 1))) , (var 3)) → ⊥
  cut6214  adequate = bad6214  (Adequate.valid adequate Two boolean env5)
  holds6215 : (z0 z1 z2 : A2) → (mul2 (mul2 z0 (mul2 (mul2 z1 z0) z2)) (mul2 z0 z2)) ≡ z0
  holds6215 z0 z1 z2 = refl
  cut6215 : Adequate {ℓ} ((op (op (var 0) (op (op (var 1) (var 0)) (var 2))) (op (var 0) (var 2))) , (var 0)) → ⊥
  cut6215  = reject2 ((op (op (var 0) (op (op (var 1) (var 0)) (var 2))) (op (var 0) (var 2))) , (var 0)) (λ env → holds6215 (env 0) (env 1) (env 2))
  bad6216 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b1 b0) b0)) (bop b0 b0)) b1 → ⊥
  bad6216  p = false≢true (cong lower p)
  cut6216 : Adequate {ℓ} ((op (op (var 0) (op (op (var 1) (var 0)) (var 2))) (op (var 0) (var 2))) , (var 1)) → ⊥
  cut6216  adequate = bad6216  (Adequate.valid adequate Two boolean env4)
  bad6217 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b0 b0) b1)) (bop b0 b1)) b1 → ⊥
  bad6217  p = false≢true (cong lower p)
  cut6217 : Adequate {ℓ} ((op (op (var 0) (op (op (var 1) (var 0)) (var 2))) (op (var 0) (var 2))) , (var 2)) → ⊥
  cut6217  adequate = bad6217  (Adequate.valid adequate Two boolean env1)
  bad6218 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b0 b0) b0)) (bop b0 b0)) b1 → ⊥
  bad6218  p = false≢true (cong lower p)
  cut6218 : Adequate {ℓ} ((op (op (var 0) (op (op (var 1) (var 0)) (var 2))) (op (var 0) (var 2))) , (var 3)) → ⊥
  cut6218  adequate = bad6218  (Adequate.valid adequate Two boolean env5)
  bad6219 : PathP (λ _ → Two) (bop (bop b1 (bop (bop b0 b1) b1)) (bop b1 b0)) b1 → ⊥
  bad6219  p = false≢true (cong lower p)
  cut6219 : Adequate {ℓ} ((op (op (var 0) (op (op (var 1) (var 0)) (var 2))) (op (var 0) (var 3))) , (var 0)) → ⊥
  cut6219  adequate = bad6219  (Adequate.valid adequate Two boolean env12)
  bad6220 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b1 b0) b0)) (bop b0 b0)) b1 → ⊥
  bad6220  p = false≢true (cong lower p)
  cut6220 : Adequate {ℓ} ((op (op (var 0) (op (op (var 1) (var 0)) (var 2))) (op (var 0) (var 3))) , (var 1)) → ⊥
  cut6220  adequate = bad6220  (Adequate.valid adequate Two boolean env13)
  bad6221 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b0 b0) b1)) (bop b0 b0)) b1 → ⊥
  bad6221  p = false≢true (cong lower p)
  cut6221 : Adequate {ℓ} ((op (op (var 0) (op (op (var 1) (var 0)) (var 2))) (op (var 0) (var 3))) , (var 2)) → ⊥
  cut6221  adequate = bad6221  (Adequate.valid adequate Two boolean env8)
  bad6222 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b0 b0) b0)) (bop b0 b1)) b1 → ⊥
  bad6222  p = false≢true (cong lower p)
  cut6222 : Adequate {ℓ} ((op (op (var 0) (op (op (var 1) (var 0)) (var 2))) (op (var 0) (var 3))) , (var 3)) → ⊥
  cut6222  adequate = bad6222  (Adequate.valid adequate Two boolean env5)
  bad6223 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b0 b0) b0)) (bop b0 b0)) b1 → ⊥
  bad6223  p = false≢true (cong lower p)
  cut6223 : Adequate {ℓ} ((op (op (var 0) (op (op (var 1) (var 0)) (var 2))) (op (var 0) (var 3))) , (var 4)) → ⊥
  cut6223  adequate = bad6223  (Adequate.valid adequate Two boolean env9)
  bad6224 : PathP (λ _ → Two) (bop (bop b1 (bop (bop b0 b1) b1)) (bop b0 b1)) b1 → ⊥
  bad6224  p = false≢true (cong lower p)
  cut6224 : Adequate {ℓ} ((op (op (var 0) (op (op (var 1) (var 0)) (var 2))) (op (var 1) (var 0))) , (var 0)) → ⊥
  cut6224  adequate = bad6224  (Adequate.valid adequate Two boolean env11)
  bad6225 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b1 b0) b0)) (bop b1 b0)) b1 → ⊥
  bad6225  p = false≢true (cong lower p)
  cut6225 : Adequate {ℓ} ((op (op (var 0) (op (op (var 1) (var 0)) (var 2))) (op (var 1) (var 0))) , (var 1)) → ⊥
  cut6225  adequate = bad6225  (Adequate.valid adequate Two boolean env4)
  bad6226 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b0 b0) b1)) (bop b0 b0)) b1 → ⊥
  bad6226  p = false≢true (cong lower p)
  cut6226 : Adequate {ℓ} ((op (op (var 0) (op (op (var 1) (var 0)) (var 2))) (op (var 1) (var 0))) , (var 2)) → ⊥
  cut6226  adequate = bad6226  (Adequate.valid adequate Two boolean env1)
  bad6227 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b0 b0) b0)) (bop b0 b0)) b1 → ⊥
  bad6227  p = false≢true (cong lower p)
  cut6227 : Adequate {ℓ} ((op (op (var 0) (op (op (var 1) (var 0)) (var 2))) (op (var 1) (var 0))) , (var 3)) → ⊥
  cut6227  adequate = bad6227  (Adequate.valid adequate Two boolean env5)
  bad6228 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b1 b0) b0)) (bop b1 b1)) b0 → ⊥
  bad6228  p = false≢true (sym (cong lower p))
  cut6228 : Adequate {ℓ} ((op (op (var 0) (op (op (var 1) (var 0)) (var 2))) (op (var 1) (var 1))) , (var 0)) → ⊥
  cut6228  adequate = bad6228  (Adequate.valid adequate Two boolean env4)
  bad6229 : PathP (λ _ → Two) (bop (bop b1 (bop (bop b0 b1) b0)) (bop b0 b0)) b0 → ⊥
  bad6229  p = false≢true (sym (cong lower p))
  cut6229 : Adequate {ℓ} ((op (op (var 0) (op (op (var 1) (var 0)) (var 2))) (op (var 1) (var 1))) , (var 1)) → ⊥
  cut6229  adequate = bad6229  (Adequate.valid adequate Two boolean env6)
  bad6230 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b0 b0) b1)) (bop b0 b0)) b1 → ⊥
  bad6230  p = false≢true (cong lower p)
  cut6230 : Adequate {ℓ} ((op (op (var 0) (op (op (var 1) (var 0)) (var 2))) (op (var 1) (var 1))) , (var 2)) → ⊥
  cut6230  adequate = bad6230  (Adequate.valid adequate Two boolean env1)
  bad6231 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b0 b0) b0)) (bop b0 b0)) b1 → ⊥
  bad6231  p = false≢true (cong lower p)
  cut6231 : Adequate {ℓ} ((op (op (var 0) (op (op (var 1) (var 0)) (var 2))) (op (var 1) (var 1))) , (var 3)) → ⊥
  cut6231  adequate = bad6231  (Adequate.valid adequate Two boolean env5)
  bad6232 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b1 b0) b1)) (bop b1 b1)) b0 → ⊥
  bad6232  p = false≢true (sym (cong lower p))
  cut6232 : Adequate {ℓ} ((op (op (var 0) (op (op (var 1) (var 0)) (var 2))) (op (var 1) (var 2))) , (var 0)) → ⊥
  cut6232  adequate = bad6232  (Adequate.valid adequate Two boolean env3)
  bad6233 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b1 b0) b0)) (bop b1 b0)) b1 → ⊥
  bad6233  p = false≢true (cong lower p)
  cut6233 : Adequate {ℓ} ((op (op (var 0) (op (op (var 1) (var 0)) (var 2))) (op (var 1) (var 2))) , (var 1)) → ⊥
  cut6233  adequate = bad6233  (Adequate.valid adequate Two boolean env4)
  bad6234 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b0 b0) b1)) (bop b0 b1)) b1 → ⊥
  bad6234  p = false≢true (cong lower p)
  cut6234 : Adequate {ℓ} ((op (op (var 0) (op (op (var 1) (var 0)) (var 2))) (op (var 1) (var 2))) , (var 2)) → ⊥
  cut6234  adequate = bad6234  (Adequate.valid adequate Two boolean env1)
  bad6235 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b0 b0) b0)) (bop b0 b0)) b1 → ⊥
  bad6235  p = false≢true (cong lower p)
  cut6235 : Adequate {ℓ} ((op (op (var 0) (op (op (var 1) (var 0)) (var 2))) (op (var 1) (var 2))) , (var 3)) → ⊥
  cut6235  adequate = bad6235  (Adequate.valid adequate Two boolean env5)
  bad6236 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b1 b0) b0)) (bop b1 b1)) b0 → ⊥
  bad6236  p = false≢true (sym (cong lower p))
  cut6236 : Adequate {ℓ} ((op (op (var 0) (op (op (var 1) (var 0)) (var 2))) (op (var 1) (var 3))) , (var 0)) → ⊥
  cut6236  adequate = bad6236  (Adequate.valid adequate Two boolean env14)
  bad6237 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b1 b0) b0)) (bop b1 b0)) b1 → ⊥
  bad6237  p = false≢true (cong lower p)
  cut6237 : Adequate {ℓ} ((op (op (var 0) (op (op (var 1) (var 0)) (var 2))) (op (var 1) (var 3))) , (var 1)) → ⊥
  cut6237  adequate = bad6237  (Adequate.valid adequate Two boolean env13)
  bad6238 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b0 b0) b1)) (bop b0 b0)) b1 → ⊥
  bad6238  p = false≢true (cong lower p)
  cut6238 : Adequate {ℓ} ((op (op (var 0) (op (op (var 1) (var 0)) (var 2))) (op (var 1) (var 3))) , (var 2)) → ⊥
  cut6238  adequate = bad6238  (Adequate.valid adequate Two boolean env8)
  bad6239 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b0 b0) b0)) (bop b0 b1)) b1 → ⊥
  bad6239  p = false≢true (cong lower p)
  cut6239 : Adequate {ℓ} ((op (op (var 0) (op (op (var 1) (var 0)) (var 2))) (op (var 1) (var 3))) , (var 3)) → ⊥
  cut6239  adequate = bad6239  (Adequate.valid adequate Two boolean env5)
  bad6240 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b0 b0) b0)) (bop b0 b0)) b1 → ⊥
  bad6240  p = false≢true (cong lower p)
  cut6240 : Adequate {ℓ} ((op (op (var 0) (op (op (var 1) (var 0)) (var 2))) (op (var 1) (var 3))) , (var 4)) → ⊥
  cut6240  adequate = bad6240  (Adequate.valid adequate Two boolean env9)
  holds6241 : (z0 z1 z2 : A2) → (mul2 (mul2 z0 (mul2 (mul2 z1 z0) z2)) (mul2 z2 z0)) ≡ z0
  holds6241 z0 z1 z2 = refl
  cut6241 : Adequate {ℓ} ((op (op (var 0) (op (op (var 1) (var 0)) (var 2))) (op (var 2) (var 0))) , (var 0)) → ⊥
  cut6241  = reject2 ((op (op (var 0) (op (op (var 1) (var 0)) (var 2))) (op (var 2) (var 0))) , (var 0)) (λ env → holds6241 (env 0) (env 1) (env 2))
  bad6242 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b1 b0) b0)) (bop b0 b0)) b1 → ⊥
  bad6242  p = false≢true (cong lower p)
  cut6242 : Adequate {ℓ} ((op (op (var 0) (op (op (var 1) (var 0)) (var 2))) (op (var 2) (var 0))) , (var 1)) → ⊥
  cut6242  adequate = bad6242  (Adequate.valid adequate Two boolean env4)
  bad6243 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b0 b0) b1)) (bop b1 b0)) b1 → ⊥
  bad6243  p = false≢true (cong lower p)
  cut6243 : Adequate {ℓ} ((op (op (var 0) (op (op (var 1) (var 0)) (var 2))) (op (var 2) (var 0))) , (var 2)) → ⊥
  cut6243  adequate = bad6243  (Adequate.valid adequate Two boolean env1)
  bad6244 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b0 b0) b0)) (bop b0 b0)) b1 → ⊥
  bad6244  p = false≢true (cong lower p)
  cut6244 : Adequate {ℓ} ((op (op (var 0) (op (op (var 1) (var 0)) (var 2))) (op (var 2) (var 0))) , (var 3)) → ⊥
  cut6244  adequate = bad6244  (Adequate.valid adequate Two boolean env5)
  bad6245 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b1 b0) b1)) (bop b1 b1)) b0 → ⊥
  bad6245  p = false≢true (sym (cong lower p))
  cut6245 : Adequate {ℓ} ((op (op (var 0) (op (op (var 1) (var 0)) (var 2))) (op (var 2) (var 1))) , (var 0)) → ⊥
  cut6245  adequate = bad6245  (Adequate.valid adequate Two boolean env3)
  bad6246 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b1 b0) b0)) (bop b0 b1)) b1 → ⊥
  bad6246  p = false≢true (cong lower p)
  cut6246 : Adequate {ℓ} ((op (op (var 0) (op (op (var 1) (var 0)) (var 2))) (op (var 2) (var 1))) , (var 1)) → ⊥
  cut6246  adequate = bad6246  (Adequate.valid adequate Two boolean env4)
  bad6247 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b0 b0) b1)) (bop b1 b0)) b1 → ⊥
  bad6247  p = false≢true (cong lower p)
  cut6247 : Adequate {ℓ} ((op (op (var 0) (op (op (var 1) (var 0)) (var 2))) (op (var 2) (var 1))) , (var 2)) → ⊥
  cut6247  adequate = bad6247  (Adequate.valid adequate Two boolean env1)
  bad6248 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b0 b0) b0)) (bop b0 b0)) b1 → ⊥
  bad6248  p = false≢true (cong lower p)
  cut6248 : Adequate {ℓ} ((op (op (var 0) (op (op (var 1) (var 0)) (var 2))) (op (var 2) (var 1))) , (var 3)) → ⊥
  cut6248  adequate = bad6248  (Adequate.valid adequate Two boolean env5)
  bad6249 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b0 b0) b1)) (bop b1 b1)) b0 → ⊥
  bad6249  p = false≢true (sym (cong lower p))
  cut6249 : Adequate {ℓ} ((op (op (var 0) (op (op (var 1) (var 0)) (var 2))) (op (var 2) (var 2))) , (var 0)) → ⊥
  cut6249  adequate = bad6249  (Adequate.valid adequate Two boolean env1)
  bad6250 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b0 b0) b1)) (bop b1 b1)) b0 → ⊥
  bad6250  p = false≢true (sym (cong lower p))
  cut6250 : Adequate {ℓ} ((op (op (var 0) (op (op (var 1) (var 0)) (var 2))) (op (var 2) (var 2))) , (var 1)) → ⊥
  cut6250  adequate = bad6250  (Adequate.valid adequate Two boolean env1)
  bad6251 : PathP (λ _ → Two) (bop (bop b1 (bop (bop b0 b1) b0)) (bop b0 b0)) b0 → ⊥
  bad6251  p = false≢true (sym (cong lower p))
  cut6251 : Adequate {ℓ} ((op (op (var 0) (op (op (var 1) (var 0)) (var 2))) (op (var 2) (var 2))) , (var 2)) → ⊥
  cut6251  adequate = bad6251  (Adequate.valid adequate Two boolean env6)
  bad6252 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b0 b0) b0)) (bop b0 b0)) b1 → ⊥
  bad6252  p = false≢true (cong lower p)
  cut6252 : Adequate {ℓ} ((op (op (var 0) (op (op (var 1) (var 0)) (var 2))) (op (var 2) (var 2))) , (var 3)) → ⊥
  cut6252  adequate = bad6252  (Adequate.valid adequate Two boolean env5)
  bad6253 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b0 b0) b1)) (bop b1 b1)) b0 → ⊥
  bad6253  p = false≢true (sym (cong lower p))
  cut6253 : Adequate {ℓ} ((op (op (var 0) (op (op (var 1) (var 0)) (var 2))) (op (var 2) (var 3))) , (var 0)) → ⊥
  cut6253  adequate = bad6253  (Adequate.valid adequate Two boolean env7)
  bad6254 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b0 b0) b1)) (bop b1 b1)) b0 → ⊥
  bad6254  p = false≢true (sym (cong lower p))
  cut6254 : Adequate {ℓ} ((op (op (var 0) (op (op (var 1) (var 0)) (var 2))) (op (var 2) (var 3))) , (var 1)) → ⊥
  cut6254  adequate = bad6254  (Adequate.valid adequate Two boolean env7)
  bad6255 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b0 b0) b1)) (bop b1 b0)) b1 → ⊥
  bad6255  p = false≢true (cong lower p)
  cut6255 : Adequate {ℓ} ((op (op (var 0) (op (op (var 1) (var 0)) (var 2))) (op (var 2) (var 3))) , (var 2)) → ⊥
  cut6255  adequate = bad6255  (Adequate.valid adequate Two boolean env8)
  bad6256 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b0 b0) b0)) (bop b0 b1)) b1 → ⊥
  bad6256  p = false≢true (cong lower p)
  cut6256 : Adequate {ℓ} ((op (op (var 0) (op (op (var 1) (var 0)) (var 2))) (op (var 2) (var 3))) , (var 3)) → ⊥
  cut6256  adequate = bad6256  (Adequate.valid adequate Two boolean env5)
  bad6257 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b0 b0) b0)) (bop b0 b0)) b1 → ⊥
  bad6257  p = false≢true (cong lower p)
  cut6257 : Adequate {ℓ} ((op (op (var 0) (op (op (var 1) (var 0)) (var 2))) (op (var 2) (var 3))) , (var 4)) → ⊥
  cut6257  adequate = bad6257  (Adequate.valid adequate Two boolean env9)
  bad6258 : PathP (λ _ → Two) (bop (bop b1 (bop (bop b0 b1) b1)) (bop b0 b1)) b1 → ⊥
  bad6258  p = false≢true (cong lower p)
  cut6258 : Adequate {ℓ} ((op (op (var 0) (op (op (var 1) (var 0)) (var 2))) (op (var 3) (var 0))) , (var 0)) → ⊥
  cut6258  adequate = bad6258  (Adequate.valid adequate Two boolean env12)
  bad6259 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b1 b0) b0)) (bop b0 b0)) b1 → ⊥
  bad6259  p = false≢true (cong lower p)
  cut6259 : Adequate {ℓ} ((op (op (var 0) (op (op (var 1) (var 0)) (var 2))) (op (var 3) (var 0))) , (var 1)) → ⊥
  cut6259  adequate = bad6259  (Adequate.valid adequate Two boolean env13)
  bad6260 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b0 b0) b1)) (bop b0 b0)) b1 → ⊥
  bad6260  p = false≢true (cong lower p)
  cut6260 : Adequate {ℓ} ((op (op (var 0) (op (op (var 1) (var 0)) (var 2))) (op (var 3) (var 0))) , (var 2)) → ⊥
  cut6260  adequate = bad6260  (Adequate.valid adequate Two boolean env8)
  bad6261 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b0 b0) b0)) (bop b1 b0)) b1 → ⊥
  bad6261  p = false≢true (cong lower p)
  cut6261 : Adequate {ℓ} ((op (op (var 0) (op (op (var 1) (var 0)) (var 2))) (op (var 3) (var 0))) , (var 3)) → ⊥
  cut6261  adequate = bad6261  (Adequate.valid adequate Two boolean env5)
  bad6262 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b0 b0) b0)) (bop b0 b0)) b1 → ⊥
  bad6262  p = false≢true (cong lower p)
  cut6262 : Adequate {ℓ} ((op (op (var 0) (op (op (var 1) (var 0)) (var 2))) (op (var 3) (var 0))) , (var 4)) → ⊥
  cut6262  adequate = bad6262  (Adequate.valid adequate Two boolean env9)
  bad6263 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b1 b0) b0)) (bop b1 b1)) b0 → ⊥
  bad6263  p = false≢true (sym (cong lower p))
  cut6263 : Adequate {ℓ} ((op (op (var 0) (op (op (var 1) (var 0)) (var 2))) (op (var 3) (var 1))) , (var 0)) → ⊥
  cut6263  adequate = bad6263  (Adequate.valid adequate Two boolean env14)
  bad6264 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b1 b0) b0)) (bop b0 b1)) b1 → ⊥
  bad6264  p = false≢true (cong lower p)
  cut6264 : Adequate {ℓ} ((op (op (var 0) (op (op (var 1) (var 0)) (var 2))) (op (var 3) (var 1))) , (var 1)) → ⊥
  cut6264  adequate = bad6264  (Adequate.valid adequate Two boolean env13)
  bad6265 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b0 b0) b1)) (bop b0 b0)) b1 → ⊥
  bad6265  p = false≢true (cong lower p)
  cut6265 : Adequate {ℓ} ((op (op (var 0) (op (op (var 1) (var 0)) (var 2))) (op (var 3) (var 1))) , (var 2)) → ⊥
  cut6265  adequate = bad6265  (Adequate.valid adequate Two boolean env8)
  bad6266 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b0 b0) b0)) (bop b1 b0)) b1 → ⊥
  bad6266  p = false≢true (cong lower p)
  cut6266 : Adequate {ℓ} ((op (op (var 0) (op (op (var 1) (var 0)) (var 2))) (op (var 3) (var 1))) , (var 3)) → ⊥
  cut6266  adequate = bad6266  (Adequate.valid adequate Two boolean env5)
  bad6267 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b0 b0) b0)) (bop b0 b0)) b1 → ⊥
  bad6267  p = false≢true (cong lower p)
  cut6267 : Adequate {ℓ} ((op (op (var 0) (op (op (var 1) (var 0)) (var 2))) (op (var 3) (var 1))) , (var 4)) → ⊥
  cut6267  adequate = bad6267  (Adequate.valid adequate Two boolean env9)
  bad6268 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b0 b0) b1)) (bop b1 b1)) b0 → ⊥
  bad6268  p = false≢true (sym (cong lower p))
  cut6268 : Adequate {ℓ} ((op (op (var 0) (op (op (var 1) (var 0)) (var 2))) (op (var 3) (var 2))) , (var 0)) → ⊥
  cut6268  adequate = bad6268  (Adequate.valid adequate Two boolean env7)
  bad6269 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b0 b0) b1)) (bop b1 b1)) b0 → ⊥
  bad6269  p = false≢true (sym (cong lower p))
  cut6269 : Adequate {ℓ} ((op (op (var 0) (op (op (var 1) (var 0)) (var 2))) (op (var 3) (var 2))) , (var 1)) → ⊥
  cut6269  adequate = bad6269  (Adequate.valid adequate Two boolean env7)
  bad6270 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b0 b0) b1)) (bop b0 b1)) b1 → ⊥
  bad6270  p = false≢true (cong lower p)
  cut6270 : Adequate {ℓ} ((op (op (var 0) (op (op (var 1) (var 0)) (var 2))) (op (var 3) (var 2))) , (var 2)) → ⊥
  cut6270  adequate = bad6270  (Adequate.valid adequate Two boolean env8)
  bad6271 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b0 b0) b0)) (bop b1 b0)) b1 → ⊥
  bad6271  p = false≢true (cong lower p)
  cut6271 : Adequate {ℓ} ((op (op (var 0) (op (op (var 1) (var 0)) (var 2))) (op (var 3) (var 2))) , (var 3)) → ⊥
  cut6271  adequate = bad6271  (Adequate.valid adequate Two boolean env5)
  bad6272 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b0 b0) b0)) (bop b0 b0)) b1 → ⊥
  bad6272  p = false≢true (cong lower p)
  cut6272 : Adequate {ℓ} ((op (op (var 0) (op (op (var 1) (var 0)) (var 2))) (op (var 3) (var 2))) , (var 4)) → ⊥
  cut6272  adequate = bad6272  (Adequate.valid adequate Two boolean env9)
  bad6273 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b0 b0) b0)) (bop b1 b1)) b0 → ⊥
  bad6273  p = false≢true (sym (cong lower p))
  cut6273 : Adequate {ℓ} ((op (op (var 0) (op (op (var 1) (var 0)) (var 2))) (op (var 3) (var 3))) , (var 0)) → ⊥
  cut6273  adequate = bad6273  (Adequate.valid adequate Two boolean env5)
  bad6274 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b0 b0) b0)) (bop b1 b1)) b0 → ⊥
  bad6274  p = false≢true (sym (cong lower p))
  cut6274 : Adequate {ℓ} ((op (op (var 0) (op (op (var 1) (var 0)) (var 2))) (op (var 3) (var 3))) , (var 1)) → ⊥
  cut6274  adequate = bad6274  (Adequate.valid adequate Two boolean env5)
  bad6275 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b0 b0) b0)) (bop b1 b1)) b0 → ⊥
  bad6275  p = false≢true (sym (cong lower p))
  cut6275 : Adequate {ℓ} ((op (op (var 0) (op (op (var 1) (var 0)) (var 2))) (op (var 3) (var 3))) , (var 2)) → ⊥
  cut6275  adequate = bad6275  (Adequate.valid adequate Two boolean env5)
  bad6276 : PathP (λ _ → Two) (bop (bop b1 (bop (bop b0 b1) b0)) (bop b0 b0)) b0 → ⊥
  bad6276  p = false≢true (sym (cong lower p))
  cut6276 : Adequate {ℓ} ((op (op (var 0) (op (op (var 1) (var 0)) (var 2))) (op (var 3) (var 3))) , (var 3)) → ⊥
  cut6276  adequate = bad6276  (Adequate.valid adequate Two boolean env15)
  bad6277 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b0 b0) b0)) (bop b0 b0)) b1 → ⊥
  bad6277  p = false≢true (cong lower p)
  cut6277 : Adequate {ℓ} ((op (op (var 0) (op (op (var 1) (var 0)) (var 2))) (op (var 3) (var 3))) , (var 4)) → ⊥
  cut6277  adequate = bad6277  (Adequate.valid adequate Two boolean env9)
  bad6278 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b0 b0) b0)) (bop b1 b1)) b0 → ⊥
  bad6278  p = false≢true (sym (cong lower p))
  cut6278 : Adequate {ℓ} ((op (op (var 0) (op (op (var 1) (var 0)) (var 2))) (op (var 3) (var 4))) , (var 0)) → ⊥
  cut6278  adequate = bad6278  (Adequate.valid adequate Two boolean env16)
  bad6279 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b0 b0) b0)) (bop b1 b1)) b0 → ⊥
  bad6279  p = false≢true (sym (cong lower p))
  cut6279 : Adequate {ℓ} ((op (op (var 0) (op (op (var 1) (var 0)) (var 2))) (op (var 3) (var 4))) , (var 1)) → ⊥
  cut6279  adequate = bad6279  (Adequate.valid adequate Two boolean env16)
  bad6280 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b0 b0) b0)) (bop b1 b1)) b0 → ⊥
  bad6280  p = false≢true (sym (cong lower p))
  cut6280 : Adequate {ℓ} ((op (op (var 0) (op (op (var 1) (var 0)) (var 2))) (op (var 3) (var 4))) , (var 2)) → ⊥
  cut6280  adequate = bad6280  (Adequate.valid adequate Two boolean env16)
  bad6281 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b0 b0) b0)) (bop b1 b0)) b1 → ⊥
  bad6281  p = false≢true (cong lower p)
  cut6281 : Adequate {ℓ} ((op (op (var 0) (op (op (var 1) (var 0)) (var 2))) (op (var 3) (var 4))) , (var 3)) → ⊥
  cut6281  adequate = bad6281  (Adequate.valid adequate Two boolean env17)
  bad6282 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b0 b0) b0)) (bop b0 b1)) b1 → ⊥
  bad6282  p = false≢true (cong lower p)
  cut6282 : Adequate {ℓ} ((op (op (var 0) (op (op (var 1) (var 0)) (var 2))) (op (var 3) (var 4))) , (var 4)) → ⊥
  cut6282  adequate = bad6282  (Adequate.valid adequate Two boolean env9)
  bad6283 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b0 b0) b0)) (bop b0 b0)) b1 → ⊥
  bad6283  p = false≢true (cong lower p)
  cut6283 : Adequate {ℓ} ((op (op (var 0) (op (op (var 1) (var 0)) (var 2))) (op (var 3) (var 4))) , (var 5)) → ⊥
  cut6283  adequate = bad6283  (Adequate.valid adequate Two boolean env18)
  holds6284 : (z0 z1 : A2) → (mul2 (mul2 z0 (mul2 (mul2 z1 z1) z0)) (mul2 z0 z0)) ≡ z0
  holds6284 z0 z1 = refl
  cut6284 : Adequate {ℓ} ((op (op (var 0) (op (op (var 1) (var 1)) (var 0))) (op (var 0) (var 0))) , (var 0)) → ⊥
  cut6284  = reject2 ((op (op (var 0) (op (op (var 1) (var 1)) (var 0))) (op (var 0) (var 0))) , (var 0)) (λ env → holds6284 (env 0) (env 1))
  bad6285 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b1 b1) b0)) (bop b0 b0)) b1 → ⊥
  bad6285  p = false≢true (cong lower p)
  cut6285 : Adequate {ℓ} ((op (op (var 0) (op (op (var 1) (var 1)) (var 0))) (op (var 0) (var 0))) , (var 1)) → ⊥
  cut6285  adequate = bad6285  (Adequate.valid adequate Two boolean env0)
  bad6286 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b0 b0) b0)) (bop b0 b0)) b1 → ⊥
  bad6286  p = false≢true (cong lower p)
  cut6286 : Adequate {ℓ} ((op (op (var 0) (op (op (var 1) (var 1)) (var 0))) (op (var 0) (var 0))) , (var 2)) → ⊥
  cut6286  adequate = bad6286  (Adequate.valid adequate Two boolean env1)
  bad6287 : PathP (λ _ → Two) (bop (bop b1 (bop (bop b0 b0) b1)) (bop b1 b0)) b1 → ⊥
  bad6287  p = false≢true (cong lower p)
  cut6287 : Adequate {ℓ} ((op (op (var 0) (op (op (var 1) (var 1)) (var 0))) (op (var 0) (var 1))) , (var 0)) → ⊥
  cut6287  adequate = bad6287  (Adequate.valid adequate Two boolean env2)
  bad6288 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b1 b1) b0)) (bop b0 b1)) b1 → ⊥
  bad6288  p = false≢true (cong lower p)
  cut6288 : Adequate {ℓ} ((op (op (var 0) (op (op (var 1) (var 1)) (var 0))) (op (var 0) (var 1))) , (var 1)) → ⊥
  cut6288  adequate = bad6288  (Adequate.valid adequate Two boolean env0)
  bad6289 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b0 b0) b0)) (bop b0 b0)) b1 → ⊥
  bad6289  p = false≢true (cong lower p)
  cut6289 : Adequate {ℓ} ((op (op (var 0) (op (op (var 1) (var 1)) (var 0))) (op (var 0) (var 1))) , (var 2)) → ⊥
  cut6289  adequate = bad6289  (Adequate.valid adequate Two boolean env1)
  bad6290 : PathP (λ _ → Two) (bop (bop b1 (bop (bop b0 b0) b1)) (bop b1 b0)) b1 → ⊥
  bad6290  p = false≢true (cong lower p)
  cut6290 : Adequate {ℓ} ((op (op (var 0) (op (op (var 1) (var 1)) (var 0))) (op (var 0) (var 2))) , (var 0)) → ⊥
  cut6290  adequate = bad6290  (Adequate.valid adequate Two boolean env6)
  bad6291 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b1 b1) b0)) (bop b0 b0)) b1 → ⊥
  bad6291  p = false≢true (cong lower p)
  cut6291 : Adequate {ℓ} ((op (op (var 0) (op (op (var 1) (var 1)) (var 0))) (op (var 0) (var 2))) , (var 1)) → ⊥
  cut6291  adequate = bad6291  (Adequate.valid adequate Two boolean env4)
  bad6292 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b0 b0) b0)) (bop b0 b1)) b1 → ⊥
  bad6292  p = false≢true (cong lower p)
  cut6292 : Adequate {ℓ} ((op (op (var 0) (op (op (var 1) (var 1)) (var 0))) (op (var 0) (var 2))) , (var 2)) → ⊥
  cut6292  adequate = bad6292  (Adequate.valid adequate Two boolean env1)
  bad6293 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b0 b0) b0)) (bop b0 b0)) b1 → ⊥
  bad6293  p = false≢true (cong lower p)
  cut6293 : Adequate {ℓ} ((op (op (var 0) (op (op (var 1) (var 1)) (var 0))) (op (var 0) (var 2))) , (var 3)) → ⊥
  cut6293  adequate = bad6293  (Adequate.valid adequate Two boolean env5)
  bad6294 : PathP (λ _ → Two) (bop (bop b1 (bop (bop b0 b0) b1)) (bop b0 b1)) b1 → ⊥
  bad6294  p = false≢true (cong lower p)
  cut6294 : Adequate {ℓ} ((op (op (var 0) (op (op (var 1) (var 1)) (var 0))) (op (var 1) (var 0))) , (var 0)) → ⊥
  cut6294  adequate = bad6294  (Adequate.valid adequate Two boolean env2)
  bad6295 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b1 b1) b0)) (bop b1 b0)) b1 → ⊥
  bad6295  p = false≢true (cong lower p)
  cut6295 : Adequate {ℓ} ((op (op (var 0) (op (op (var 1) (var 1)) (var 0))) (op (var 1) (var 0))) , (var 1)) → ⊥
  cut6295  adequate = bad6295  (Adequate.valid adequate Two boolean env0)
  bad6296 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b0 b0) b0)) (bop b0 b0)) b1 → ⊥
  bad6296  p = false≢true (cong lower p)
  cut6296 : Adequate {ℓ} ((op (op (var 0) (op (op (var 1) (var 1)) (var 0))) (op (var 1) (var 0))) , (var 2)) → ⊥
  cut6296  adequate = bad6296  (Adequate.valid adequate Two boolean env1)
  bad6297 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b1 b1) b0)) (bop b1 b1)) b0 → ⊥
  bad6297  p = false≢true (sym (cong lower p))
  cut6297 : Adequate {ℓ} ((op (op (var 0) (op (op (var 1) (var 1)) (var 0))) (op (var 1) (var 1))) , (var 0)) → ⊥
  cut6297  adequate = bad6297  (Adequate.valid adequate Two boolean env0)
  holds6298 : (z0 z1 : A3) → (mul3 (mul3 z0 (mul3 (mul3 z1 z1) z0)) (mul3 z1 z1)) ≡ z1
  holds6298 z0 z1 = refl
  cut6298 : Adequate {ℓ} ((op (op (var 0) (op (op (var 1) (var 1)) (var 0))) (op (var 1) (var 1))) , (var 1)) → ⊥
  cut6298  = reject3 ((op (op (var 0) (op (op (var 1) (var 1)) (var 0))) (op (var 1) (var 1))) , (var 1)) (λ env → holds6298 (env 0) (env 1))
  bad6299 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b0 b0) b0)) (bop b0 b0)) b1 → ⊥
  bad6299  p = false≢true (cong lower p)
  cut6299 : Adequate {ℓ} ((op (op (var 0) (op (op (var 1) (var 1)) (var 0))) (op (var 1) (var 1))) , (var 2)) → ⊥
  cut6299  adequate = bad6299  (Adequate.valid adequate Two boolean env1)
  bad6300 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b1 b1) b0)) (bop b1 b1)) b0 → ⊥
  bad6300  p = false≢true (sym (cong lower p))
  cut6300 : Adequate {ℓ} ((op (op (var 0) (op (op (var 1) (var 1)) (var 0))) (op (var 1) (var 2))) , (var 0)) → ⊥
  cut6300  adequate = bad6300  (Adequate.valid adequate Two boolean env3)
  bad6301 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b1 b1) b0)) (bop b1 b0)) b1 → ⊥
  bad6301  p = false≢true (cong lower p)
  cut6301 : Adequate {ℓ} ((op (op (var 0) (op (op (var 1) (var 1)) (var 0))) (op (var 1) (var 2))) , (var 1)) → ⊥
  cut6301  adequate = bad6301  (Adequate.valid adequate Two boolean env4)
  bad6302 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b0 b0) b0)) (bop b0 b1)) b1 → ⊥
  bad6302  p = false≢true (cong lower p)
  cut6302 : Adequate {ℓ} ((op (op (var 0) (op (op (var 1) (var 1)) (var 0))) (op (var 1) (var 2))) , (var 2)) → ⊥
  cut6302  adequate = bad6302  (Adequate.valid adequate Two boolean env1)
  bad6303 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b0 b0) b0)) (bop b0 b0)) b1 → ⊥
  bad6303  p = false≢true (cong lower p)
  cut6303 : Adequate {ℓ} ((op (op (var 0) (op (op (var 1) (var 1)) (var 0))) (op (var 1) (var 2))) , (var 3)) → ⊥
  cut6303  adequate = bad6303  (Adequate.valid adequate Two boolean env5)
  bad6304 : PathP (λ _ → Two) (bop (bop b1 (bop (bop b0 b0) b1)) (bop b0 b1)) b1 → ⊥
  bad6304  p = false≢true (cong lower p)
  cut6304 : Adequate {ℓ} ((op (op (var 0) (op (op (var 1) (var 1)) (var 0))) (op (var 2) (var 0))) , (var 0)) → ⊥
  cut6304  adequate = bad6304  (Adequate.valid adequate Two boolean env6)
  bad6305 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b1 b1) b0)) (bop b0 b0)) b1 → ⊥
  bad6305  p = false≢true (cong lower p)
  cut6305 : Adequate {ℓ} ((op (op (var 0) (op (op (var 1) (var 1)) (var 0))) (op (var 2) (var 0))) , (var 1)) → ⊥
  cut6305  adequate = bad6305  (Adequate.valid adequate Two boolean env4)
  bad6306 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b0 b0) b0)) (bop b1 b0)) b1 → ⊥
  bad6306  p = false≢true (cong lower p)
  cut6306 : Adequate {ℓ} ((op (op (var 0) (op (op (var 1) (var 1)) (var 0))) (op (var 2) (var 0))) , (var 2)) → ⊥
  cut6306  adequate = bad6306  (Adequate.valid adequate Two boolean env1)
  bad6307 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b0 b0) b0)) (bop b0 b0)) b1 → ⊥
  bad6307  p = false≢true (cong lower p)
  cut6307 : Adequate {ℓ} ((op (op (var 0) (op (op (var 1) (var 1)) (var 0))) (op (var 2) (var 0))) , (var 3)) → ⊥
  cut6307  adequate = bad6307  (Adequate.valid adequate Two boolean env5)
  bad6308 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b1 b1) b0)) (bop b1 b1)) b0 → ⊥
  bad6308  p = false≢true (sym (cong lower p))
  cut6308 : Adequate {ℓ} ((op (op (var 0) (op (op (var 1) (var 1)) (var 0))) (op (var 2) (var 1))) , (var 0)) → ⊥
  cut6308  adequate = bad6308  (Adequate.valid adequate Two boolean env3)
  bad6309 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b1 b1) b0)) (bop b0 b1)) b1 → ⊥
  bad6309  p = false≢true (cong lower p)
  cut6309 : Adequate {ℓ} ((op (op (var 0) (op (op (var 1) (var 1)) (var 0))) (op (var 2) (var 1))) , (var 1)) → ⊥
  cut6309  adequate = bad6309  (Adequate.valid adequate Two boolean env4)
  bad6310 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b0 b0) b0)) (bop b1 b0)) b1 → ⊥
  bad6310  p = false≢true (cong lower p)
  cut6310 : Adequate {ℓ} ((op (op (var 0) (op (op (var 1) (var 1)) (var 0))) (op (var 2) (var 1))) , (var 2)) → ⊥
  cut6310  adequate = bad6310  (Adequate.valid adequate Two boolean env1)
  bad6311 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b0 b0) b0)) (bop b0 b0)) b1 → ⊥
  bad6311  p = false≢true (cong lower p)
  cut6311 : Adequate {ℓ} ((op (op (var 0) (op (op (var 1) (var 1)) (var 0))) (op (var 2) (var 1))) , (var 3)) → ⊥
  cut6311  adequate = bad6311  (Adequate.valid adequate Two boolean env5)
  bad6312 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b0 b0) b0)) (bop b1 b1)) b0 → ⊥
  bad6312  p = false≢true (sym (cong lower p))
  cut6312 : Adequate {ℓ} ((op (op (var 0) (op (op (var 1) (var 1)) (var 0))) (op (var 2) (var 2))) , (var 0)) → ⊥
  cut6312  adequate = bad6312  (Adequate.valid adequate Two boolean env1)
  bad6313 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b0 b0) b0)) (bop b1 b1)) b0 → ⊥
  bad6313  p = false≢true (sym (cong lower p))
  cut6313 : Adequate {ℓ} ((op (op (var 0) (op (op (var 1) (var 1)) (var 0))) (op (var 2) (var 2))) , (var 1)) → ⊥
  cut6313  adequate = bad6313  (Adequate.valid adequate Two boolean env1)
  bad6314 : PathP (λ _ → Two) (bop (bop b1 (bop (bop b1 b1) b1)) (bop b0 b0)) b0 → ⊥
  bad6314  p = false≢true (sym (cong lower p))
  cut6314 : Adequate {ℓ} ((op (op (var 0) (op (op (var 1) (var 1)) (var 0))) (op (var 2) (var 2))) , (var 2)) → ⊥
  cut6314  adequate = bad6314  (Adequate.valid adequate Two boolean env10)
  bad6315 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b0 b0) b0)) (bop b0 b0)) b1 → ⊥
  bad6315  p = false≢true (cong lower p)
  cut6315 : Adequate {ℓ} ((op (op (var 0) (op (op (var 1) (var 1)) (var 0))) (op (var 2) (var 2))) , (var 3)) → ⊥
  cut6315  adequate = bad6315  (Adequate.valid adequate Two boolean env5)
  bad6316 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b0 b0) b0)) (bop b1 b1)) b0 → ⊥
  bad6316  p = false≢true (sym (cong lower p))
  cut6316 : Adequate {ℓ} ((op (op (var 0) (op (op (var 1) (var 1)) (var 0))) (op (var 2) (var 3))) , (var 0)) → ⊥
  cut6316  adequate = bad6316  (Adequate.valid adequate Two boolean env7)
  bad6317 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b0 b0) b0)) (bop b1 b1)) b0 → ⊥
  bad6317  p = false≢true (sym (cong lower p))
  cut6317 : Adequate {ℓ} ((op (op (var 0) (op (op (var 1) (var 1)) (var 0))) (op (var 2) (var 3))) , (var 1)) → ⊥
  cut6317  adequate = bad6317  (Adequate.valid adequate Two boolean env7)
  bad6318 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b0 b0) b0)) (bop b1 b0)) b1 → ⊥
  bad6318  p = false≢true (cong lower p)
  cut6318 : Adequate {ℓ} ((op (op (var 0) (op (op (var 1) (var 1)) (var 0))) (op (var 2) (var 3))) , (var 2)) → ⊥
  cut6318  adequate = bad6318  (Adequate.valid adequate Two boolean env8)
  bad6319 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b0 b0) b0)) (bop b0 b1)) b1 → ⊥
  bad6319  p = false≢true (cong lower p)
  cut6319 : Adequate {ℓ} ((op (op (var 0) (op (op (var 1) (var 1)) (var 0))) (op (var 2) (var 3))) , (var 3)) → ⊥
  cut6319  adequate = bad6319  (Adequate.valid adequate Two boolean env5)
  bad6320 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b0 b0) b0)) (bop b0 b0)) b1 → ⊥
  bad6320  p = false≢true (cong lower p)
  cut6320 : Adequate {ℓ} ((op (op (var 0) (op (op (var 1) (var 1)) (var 0))) (op (var 2) (var 3))) , (var 4)) → ⊥
  cut6320  adequate = bad6320  (Adequate.valid adequate Two boolean env9)
  holds6321 : (z0 z1 : A2) → (mul2 (mul2 z0 (mul2 (mul2 z1 z1) z1)) (mul2 z0 z0)) ≡ z0
  holds6321 z0 z1 = refl
  cut6321 : Adequate {ℓ} ((op (op (var 0) (op (op (var 1) (var 1)) (var 1))) (op (var 0) (var 0))) , (var 0)) → ⊥
  cut6321  = reject2 ((op (op (var 0) (op (op (var 1) (var 1)) (var 1))) (op (var 0) (var 0))) , (var 0)) (λ env → holds6321 (env 0) (env 1))
  bad6322 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b1 b1) b1)) (bop b0 b0)) b1 → ⊥
  bad6322  p = false≢true (cong lower p)
  cut6322 : Adequate {ℓ} ((op (op (var 0) (op (op (var 1) (var 1)) (var 1))) (op (var 0) (var 0))) , (var 1)) → ⊥
  cut6322  adequate = bad6322  (Adequate.valid adequate Two boolean env0)
  bad6323 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b0 b0) b0)) (bop b0 b0)) b1 → ⊥
  bad6323  p = false≢true (cong lower p)
  cut6323 : Adequate {ℓ} ((op (op (var 0) (op (op (var 1) (var 1)) (var 1))) (op (var 0) (var 0))) , (var 2)) → ⊥
  cut6323  adequate = bad6323  (Adequate.valid adequate Two boolean env1)
  holds6324 : (z0 z1 : A2) → (mul2 (mul2 z0 (mul2 (mul2 z1 z1) z1)) (mul2 z0 z1)) ≡ z0
  holds6324 z0 z1 = refl
  cut6324 : Adequate {ℓ} ((op (op (var 0) (op (op (var 1) (var 1)) (var 1))) (op (var 0) (var 1))) , (var 0)) → ⊥
  cut6324  = reject2 ((op (op (var 0) (op (op (var 1) (var 1)) (var 1))) (op (var 0) (var 1))) , (var 0)) (λ env → holds6324 (env 0) (env 1))
  bad6325 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b1 b1) b1)) (bop b0 b1)) b1 → ⊥
  bad6325  p = false≢true (cong lower p)
  cut6325 : Adequate {ℓ} ((op (op (var 0) (op (op (var 1) (var 1)) (var 1))) (op (var 0) (var 1))) , (var 1)) → ⊥
  cut6325  adequate = bad6325  (Adequate.valid adequate Two boolean env0)
  bad6326 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b0 b0) b0)) (bop b0 b0)) b1 → ⊥
  bad6326  p = false≢true (cong lower p)
  cut6326 : Adequate {ℓ} ((op (op (var 0) (op (op (var 1) (var 1)) (var 1))) (op (var 0) (var 1))) , (var 2)) → ⊥
  cut6326  adequate = bad6326  (Adequate.valid adequate Two boolean env1)
  holds6327 : (z0 z1 z2 : A2) → (mul2 (mul2 z0 (mul2 (mul2 z1 z1) z1)) (mul2 z0 z2)) ≡ z0
  holds6327 z0 z1 z2 = refl
  cut6327 : Adequate {ℓ} ((op (op (var 0) (op (op (var 1) (var 1)) (var 1))) (op (var 0) (var 2))) , (var 0)) → ⊥
  cut6327  = reject2 ((op (op (var 0) (op (op (var 1) (var 1)) (var 1))) (op (var 0) (var 2))) , (var 0)) (λ env → holds6327 (env 0) (env 1) (env 2))
  bad6328 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b1 b1) b1)) (bop b0 b0)) b1 → ⊥
  bad6328  p = false≢true (cong lower p)
  cut6328 : Adequate {ℓ} ((op (op (var 0) (op (op (var 1) (var 1)) (var 1))) (op (var 0) (var 2))) , (var 1)) → ⊥
  cut6328  adequate = bad6328  (Adequate.valid adequate Two boolean env4)
  bad6329 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b0 b0) b0)) (bop b0 b1)) b1 → ⊥
  bad6329  p = false≢true (cong lower p)
  cut6329 : Adequate {ℓ} ((op (op (var 0) (op (op (var 1) (var 1)) (var 1))) (op (var 0) (var 2))) , (var 2)) → ⊥
  cut6329  adequate = bad6329  (Adequate.valid adequate Two boolean env1)
  bad6330 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b0 b0) b0)) (bop b0 b0)) b1 → ⊥
  bad6330  p = false≢true (cong lower p)
  cut6330 : Adequate {ℓ} ((op (op (var 0) (op (op (var 1) (var 1)) (var 1))) (op (var 0) (var 2))) , (var 3)) → ⊥
  cut6330  adequate = bad6330  (Adequate.valid adequate Two boolean env5)
  holds6331 : (z0 z1 : A2) → (mul2 (mul2 z0 (mul2 (mul2 z1 z1) z1)) (mul2 z1 z0)) ≡ z0
  holds6331 z0 z1 = refl
  cut6331 : Adequate {ℓ} ((op (op (var 0) (op (op (var 1) (var 1)) (var 1))) (op (var 1) (var 0))) , (var 0)) → ⊥
  cut6331  = reject2 ((op (op (var 0) (op (op (var 1) (var 1)) (var 1))) (op (var 1) (var 0))) , (var 0)) (λ env → holds6331 (env 0) (env 1))
  bad6332 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b1 b1) b1)) (bop b1 b0)) b1 → ⊥
  bad6332  p = false≢true (cong lower p)
  cut6332 : Adequate {ℓ} ((op (op (var 0) (op (op (var 1) (var 1)) (var 1))) (op (var 1) (var 0))) , (var 1)) → ⊥
  cut6332  adequate = bad6332  (Adequate.valid adequate Two boolean env0)
  bad6333 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b0 b0) b0)) (bop b0 b0)) b1 → ⊥
  bad6333  p = false≢true (cong lower p)
  cut6333 : Adequate {ℓ} ((op (op (var 0) (op (op (var 1) (var 1)) (var 1))) (op (var 1) (var 0))) , (var 2)) → ⊥
  cut6333  adequate = bad6333  (Adequate.valid adequate Two boolean env1)
  bad6334 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b1 b1) b1)) (bop b1 b1)) b0 → ⊥
  bad6334  p = false≢true (sym (cong lower p))
  cut6334 : Adequate {ℓ} ((op (op (var 0) (op (op (var 1) (var 1)) (var 1))) (op (var 1) (var 1))) , (var 0)) → ⊥
  cut6334  adequate = bad6334  (Adequate.valid adequate Two boolean env0)
  bad6335 : PathP (λ _ → Two) (bop (bop b1 (bop (bop b0 b0) b0)) (bop b0 b0)) b0 → ⊥
  bad6335  p = false≢true (sym (cong lower p))
  cut6335 : Adequate {ℓ} ((op (op (var 0) (op (op (var 1) (var 1)) (var 1))) (op (var 1) (var 1))) , (var 1)) → ⊥
  cut6335  adequate = bad6335  (Adequate.valid adequate Two boolean env2)
  bad6336 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b0 b0) b0)) (bop b0 b0)) b1 → ⊥
  bad6336  p = false≢true (cong lower p)
  cut6336 : Adequate {ℓ} ((op (op (var 0) (op (op (var 1) (var 1)) (var 1))) (op (var 1) (var 1))) , (var 2)) → ⊥
  cut6336  adequate = bad6336  (Adequate.valid adequate Two boolean env1)
  bad6337 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b1 b1) b1)) (bop b1 b1)) b0 → ⊥
  bad6337  p = false≢true (sym (cong lower p))
  cut6337 : Adequate {ℓ} ((op (op (var 0) (op (op (var 1) (var 1)) (var 1))) (op (var 1) (var 2))) , (var 0)) → ⊥
  cut6337  adequate = bad6337  (Adequate.valid adequate Two boolean env3)
  bad6338 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b1 b1) b1)) (bop b1 b0)) b1 → ⊥
  bad6338  p = false≢true (cong lower p)
  cut6338 : Adequate {ℓ} ((op (op (var 0) (op (op (var 1) (var 1)) (var 1))) (op (var 1) (var 2))) , (var 1)) → ⊥
  cut6338  adequate = bad6338  (Adequate.valid adequate Two boolean env4)
  bad6339 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b0 b0) b0)) (bop b0 b1)) b1 → ⊥
  bad6339  p = false≢true (cong lower p)
  cut6339 : Adequate {ℓ} ((op (op (var 0) (op (op (var 1) (var 1)) (var 1))) (op (var 1) (var 2))) , (var 2)) → ⊥
  cut6339  adequate = bad6339  (Adequate.valid adequate Two boolean env1)
  bad6340 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b0 b0) b0)) (bop b0 b0)) b1 → ⊥
  bad6340  p = false≢true (cong lower p)
  cut6340 : Adequate {ℓ} ((op (op (var 0) (op (op (var 1) (var 1)) (var 1))) (op (var 1) (var 2))) , (var 3)) → ⊥
  cut6340  adequate = bad6340  (Adequate.valid adequate Two boolean env5)
  holds6341 : (z0 z1 z2 : A2) → (mul2 (mul2 z0 (mul2 (mul2 z1 z1) z1)) (mul2 z2 z0)) ≡ z0
  holds6341 z0 z1 z2 = refl
  cut6341 : Adequate {ℓ} ((op (op (var 0) (op (op (var 1) (var 1)) (var 1))) (op (var 2) (var 0))) , (var 0)) → ⊥
  cut6341  = reject2 ((op (op (var 0) (op (op (var 1) (var 1)) (var 1))) (op (var 2) (var 0))) , (var 0)) (λ env → holds6341 (env 0) (env 1) (env 2))
  bad6342 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b1 b1) b1)) (bop b0 b0)) b1 → ⊥
  bad6342  p = false≢true (cong lower p)
  cut6342 : Adequate {ℓ} ((op (op (var 0) (op (op (var 1) (var 1)) (var 1))) (op (var 2) (var 0))) , (var 1)) → ⊥
  cut6342  adequate = bad6342  (Adequate.valid adequate Two boolean env4)
  bad6343 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b0 b0) b0)) (bop b1 b0)) b1 → ⊥
  bad6343  p = false≢true (cong lower p)
  cut6343 : Adequate {ℓ} ((op (op (var 0) (op (op (var 1) (var 1)) (var 1))) (op (var 2) (var 0))) , (var 2)) → ⊥
  cut6343  adequate = bad6343  (Adequate.valid adequate Two boolean env1)
  bad6344 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b0 b0) b0)) (bop b0 b0)) b1 → ⊥
  bad6344  p = false≢true (cong lower p)
  cut6344 : Adequate {ℓ} ((op (op (var 0) (op (op (var 1) (var 1)) (var 1))) (op (var 2) (var 0))) , (var 3)) → ⊥
  cut6344  adequate = bad6344  (Adequate.valid adequate Two boolean env5)
  bad6345 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b1 b1) b1)) (bop b1 b1)) b0 → ⊥
  bad6345  p = false≢true (sym (cong lower p))
  cut6345 : Adequate {ℓ} ((op (op (var 0) (op (op (var 1) (var 1)) (var 1))) (op (var 2) (var 1))) , (var 0)) → ⊥
  cut6345  adequate = bad6345  (Adequate.valid adequate Two boolean env3)
  bad6346 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b1 b1) b1)) (bop b0 b1)) b1 → ⊥
  bad6346  p = false≢true (cong lower p)
  cut6346 : Adequate {ℓ} ((op (op (var 0) (op (op (var 1) (var 1)) (var 1))) (op (var 2) (var 1))) , (var 1)) → ⊥
  cut6346  adequate = bad6346  (Adequate.valid adequate Two boolean env4)
  bad6347 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b0 b0) b0)) (bop b1 b0)) b1 → ⊥
  bad6347  p = false≢true (cong lower p)
  cut6347 : Adequate {ℓ} ((op (op (var 0) (op (op (var 1) (var 1)) (var 1))) (op (var 2) (var 1))) , (var 2)) → ⊥
  cut6347  adequate = bad6347  (Adequate.valid adequate Two boolean env1)
  bad6348 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b0 b0) b0)) (bop b0 b0)) b1 → ⊥
  bad6348  p = false≢true (cong lower p)
  cut6348 : Adequate {ℓ} ((op (op (var 0) (op (op (var 1) (var 1)) (var 1))) (op (var 2) (var 1))) , (var 3)) → ⊥
  cut6348  adequate = bad6348  (Adequate.valid adequate Two boolean env5)
  bad6349 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b0 b0) b0)) (bop b1 b1)) b0 → ⊥
  bad6349  p = false≢true (sym (cong lower p))
  cut6349 : Adequate {ℓ} ((op (op (var 0) (op (op (var 1) (var 1)) (var 1))) (op (var 2) (var 2))) , (var 0)) → ⊥
  cut6349  adequate = bad6349  (Adequate.valid adequate Two boolean env1)
  bad6350 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b0 b0) b0)) (bop b1 b1)) b0 → ⊥
  bad6350  p = false≢true (sym (cong lower p))
  cut6350 : Adequate {ℓ} ((op (op (var 0) (op (op (var 1) (var 1)) (var 1))) (op (var 2) (var 2))) , (var 1)) → ⊥
  cut6350  adequate = bad6350  (Adequate.valid adequate Two boolean env1)
  bad6351 : PathP (λ _ → Two) (bop (bop b1 (bop (bop b0 b0) b0)) (bop b0 b0)) b0 → ⊥
  bad6351  p = false≢true (sym (cong lower p))
  cut6351 : Adequate {ℓ} ((op (op (var 0) (op (op (var 1) (var 1)) (var 1))) (op (var 2) (var 2))) , (var 2)) → ⊥
  cut6351  adequate = bad6351  (Adequate.valid adequate Two boolean env6)
  bad6352 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b0 b0) b0)) (bop b0 b0)) b1 → ⊥
  bad6352  p = false≢true (cong lower p)
  cut6352 : Adequate {ℓ} ((op (op (var 0) (op (op (var 1) (var 1)) (var 1))) (op (var 2) (var 2))) , (var 3)) → ⊥
  cut6352  adequate = bad6352  (Adequate.valid adequate Two boolean env5)
  bad6353 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b0 b0) b0)) (bop b1 b1)) b0 → ⊥
  bad6353  p = false≢true (sym (cong lower p))
  cut6353 : Adequate {ℓ} ((op (op (var 0) (op (op (var 1) (var 1)) (var 1))) (op (var 2) (var 3))) , (var 0)) → ⊥
  cut6353  adequate = bad6353  (Adequate.valid adequate Two boolean env7)
  bad6354 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b0 b0) b0)) (bop b1 b1)) b0 → ⊥
  bad6354  p = false≢true (sym (cong lower p))
  cut6354 : Adequate {ℓ} ((op (op (var 0) (op (op (var 1) (var 1)) (var 1))) (op (var 2) (var 3))) , (var 1)) → ⊥
  cut6354  adequate = bad6354  (Adequate.valid adequate Two boolean env7)
  bad6355 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b0 b0) b0)) (bop b1 b0)) b1 → ⊥
  bad6355  p = false≢true (cong lower p)
  cut6355 : Adequate {ℓ} ((op (op (var 0) (op (op (var 1) (var 1)) (var 1))) (op (var 2) (var 3))) , (var 2)) → ⊥
  cut6355  adequate = bad6355  (Adequate.valid adequate Two boolean env8)
  bad6356 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b0 b0) b0)) (bop b0 b1)) b1 → ⊥
  bad6356  p = false≢true (cong lower p)
  cut6356 : Adequate {ℓ} ((op (op (var 0) (op (op (var 1) (var 1)) (var 1))) (op (var 2) (var 3))) , (var 3)) → ⊥
  cut6356  adequate = bad6356  (Adequate.valid adequate Two boolean env5)
  bad6357 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b0 b0) b0)) (bop b0 b0)) b1 → ⊥
  bad6357  p = false≢true (cong lower p)
  cut6357 : Adequate {ℓ} ((op (op (var 0) (op (op (var 1) (var 1)) (var 1))) (op (var 2) (var 3))) , (var 4)) → ⊥
  cut6357  adequate = bad6357  (Adequate.valid adequate Two boolean env9)
  holds6358 : (z0 z1 z2 : A2) → (mul2 (mul2 z0 (mul2 (mul2 z1 z1) z2)) (mul2 z0 z0)) ≡ z0
  holds6358 z0 z1 z2 = refl
  cut6358 : Adequate {ℓ} ((op (op (var 0) (op (op (var 1) (var 1)) (var 2))) (op (var 0) (var 0))) , (var 0)) → ⊥
  cut6358  = reject2 ((op (op (var 0) (op (op (var 1) (var 1)) (var 2))) (op (var 0) (var 0))) , (var 0)) (λ env → holds6358 (env 0) (env 1) (env 2))
  bad6359 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b1 b1) b0)) (bop b0 b0)) b1 → ⊥
  bad6359  p = false≢true (cong lower p)
  cut6359 : Adequate {ℓ} ((op (op (var 0) (op (op (var 1) (var 1)) (var 2))) (op (var 0) (var 0))) , (var 1)) → ⊥
  cut6359  adequate = bad6359  (Adequate.valid adequate Two boolean env4)
  bad6360 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b0 b0) b1)) (bop b0 b0)) b1 → ⊥
  bad6360  p = false≢true (cong lower p)
  cut6360 : Adequate {ℓ} ((op (op (var 0) (op (op (var 1) (var 1)) (var 2))) (op (var 0) (var 0))) , (var 2)) → ⊥
  cut6360  adequate = bad6360  (Adequate.valid adequate Two boolean env1)
  bad6361 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b0 b0) b0)) (bop b0 b0)) b1 → ⊥
  bad6361  p = false≢true (cong lower p)
  cut6361 : Adequate {ℓ} ((op (op (var 0) (op (op (var 1) (var 1)) (var 2))) (op (var 0) (var 0))) , (var 3)) → ⊥
  cut6361  adequate = bad6361  (Adequate.valid adequate Two boolean env5)
  bad6362 : PathP (λ _ → Two) (bop (bop b1 (bop (bop b0 b0) b1)) (bop b1 b0)) b1 → ⊥
  bad6362  p = false≢true (cong lower p)
  cut6362 : Adequate {ℓ} ((op (op (var 0) (op (op (var 1) (var 1)) (var 2))) (op (var 0) (var 1))) , (var 0)) → ⊥
  cut6362  adequate = bad6362  (Adequate.valid adequate Two boolean env11)
  bad6363 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b1 b1) b0)) (bop b0 b1)) b1 → ⊥
  bad6363  p = false≢true (cong lower p)
  cut6363 : Adequate {ℓ} ((op (op (var 0) (op (op (var 1) (var 1)) (var 2))) (op (var 0) (var 1))) , (var 1)) → ⊥
  cut6363  adequate = bad6363  (Adequate.valid adequate Two boolean env4)
  bad6364 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b0 b0) b1)) (bop b0 b0)) b1 → ⊥
  bad6364  p = false≢true (cong lower p)
  cut6364 : Adequate {ℓ} ((op (op (var 0) (op (op (var 1) (var 1)) (var 2))) (op (var 0) (var 1))) , (var 2)) → ⊥
  cut6364  adequate = bad6364  (Adequate.valid adequate Two boolean env1)
  bad6365 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b0 b0) b0)) (bop b0 b0)) b1 → ⊥
  bad6365  p = false≢true (cong lower p)
  cut6365 : Adequate {ℓ} ((op (op (var 0) (op (op (var 1) (var 1)) (var 2))) (op (var 0) (var 1))) , (var 3)) → ⊥
  cut6365  adequate = bad6365  (Adequate.valid adequate Two boolean env5)
  holds6366 : (z0 z1 z2 : A2) → (mul2 (mul2 z0 (mul2 (mul2 z1 z1) z2)) (mul2 z0 z2)) ≡ z0
  holds6366 z0 z1 z2 = refl
  cut6366 : Adequate {ℓ} ((op (op (var 0) (op (op (var 1) (var 1)) (var 2))) (op (var 0) (var 2))) , (var 0)) → ⊥
  cut6366  = reject2 ((op (op (var 0) (op (op (var 1) (var 1)) (var 2))) (op (var 0) (var 2))) , (var 0)) (λ env → holds6366 (env 0) (env 1) (env 2))
  bad6367 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b1 b1) b0)) (bop b0 b0)) b1 → ⊥
  bad6367  p = false≢true (cong lower p)
  cut6367 : Adequate {ℓ} ((op (op (var 0) (op (op (var 1) (var 1)) (var 2))) (op (var 0) (var 2))) , (var 1)) → ⊥
  cut6367  adequate = bad6367  (Adequate.valid adequate Two boolean env4)
  bad6368 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b0 b0) b1)) (bop b0 b1)) b1 → ⊥
  bad6368  p = false≢true (cong lower p)
  cut6368 : Adequate {ℓ} ((op (op (var 0) (op (op (var 1) (var 1)) (var 2))) (op (var 0) (var 2))) , (var 2)) → ⊥
  cut6368  adequate = bad6368  (Adequate.valid adequate Two boolean env1)
  bad6369 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b0 b0) b0)) (bop b0 b0)) b1 → ⊥
  bad6369  p = false≢true (cong lower p)
  cut6369 : Adequate {ℓ} ((op (op (var 0) (op (op (var 1) (var 1)) (var 2))) (op (var 0) (var 2))) , (var 3)) → ⊥
  cut6369  adequate = bad6369  (Adequate.valid adequate Two boolean env5)
  bad6370 : PathP (λ _ → Two) (bop (bop b1 (bop (bop b0 b0) b1)) (bop b1 b0)) b1 → ⊥
  bad6370  p = false≢true (cong lower p)
  cut6370 : Adequate {ℓ} ((op (op (var 0) (op (op (var 1) (var 1)) (var 2))) (op (var 0) (var 3))) , (var 0)) → ⊥
  cut6370  adequate = bad6370  (Adequate.valid adequate Two boolean env12)
  bad6371 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b1 b1) b0)) (bop b0 b0)) b1 → ⊥
  bad6371  p = false≢true (cong lower p)
  cut6371 : Adequate {ℓ} ((op (op (var 0) (op (op (var 1) (var 1)) (var 2))) (op (var 0) (var 3))) , (var 1)) → ⊥
  cut6371  adequate = bad6371  (Adequate.valid adequate Two boolean env13)
  bad6372 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b0 b0) b1)) (bop b0 b0)) b1 → ⊥
  bad6372  p = false≢true (cong lower p)
  cut6372 : Adequate {ℓ} ((op (op (var 0) (op (op (var 1) (var 1)) (var 2))) (op (var 0) (var 3))) , (var 2)) → ⊥
  cut6372  adequate = bad6372  (Adequate.valid adequate Two boolean env8)
  bad6373 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b0 b0) b0)) (bop b0 b1)) b1 → ⊥
  bad6373  p = false≢true (cong lower p)
  cut6373 : Adequate {ℓ} ((op (op (var 0) (op (op (var 1) (var 1)) (var 2))) (op (var 0) (var 3))) , (var 3)) → ⊥
  cut6373  adequate = bad6373  (Adequate.valid adequate Two boolean env5)
  bad6374 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b0 b0) b0)) (bop b0 b0)) b1 → ⊥
  bad6374  p = false≢true (cong lower p)
  cut6374 : Adequate {ℓ} ((op (op (var 0) (op (op (var 1) (var 1)) (var 2))) (op (var 0) (var 3))) , (var 4)) → ⊥
  cut6374  adequate = bad6374  (Adequate.valid adequate Two boolean env9)
  bad6375 : PathP (λ _ → Two) (bop (bop b1 (bop (bop b0 b0) b1)) (bop b0 b1)) b1 → ⊥
  bad6375  p = false≢true (cong lower p)
  cut6375 : Adequate {ℓ} ((op (op (var 0) (op (op (var 1) (var 1)) (var 2))) (op (var 1) (var 0))) , (var 0)) → ⊥
  cut6375  adequate = bad6375  (Adequate.valid adequate Two boolean env11)
  bad6376 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b1 b1) b0)) (bop b1 b0)) b1 → ⊥
  bad6376  p = false≢true (cong lower p)
  cut6376 : Adequate {ℓ} ((op (op (var 0) (op (op (var 1) (var 1)) (var 2))) (op (var 1) (var 0))) , (var 1)) → ⊥
  cut6376  adequate = bad6376  (Adequate.valid adequate Two boolean env4)
  bad6377 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b0 b0) b1)) (bop b0 b0)) b1 → ⊥
  bad6377  p = false≢true (cong lower p)
  cut6377 : Adequate {ℓ} ((op (op (var 0) (op (op (var 1) (var 1)) (var 2))) (op (var 1) (var 0))) , (var 2)) → ⊥
  cut6377  adequate = bad6377  (Adequate.valid adequate Two boolean env1)
  bad6378 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b0 b0) b0)) (bop b0 b0)) b1 → ⊥
  bad6378  p = false≢true (cong lower p)
  cut6378 : Adequate {ℓ} ((op (op (var 0) (op (op (var 1) (var 1)) (var 2))) (op (var 1) (var 0))) , (var 3)) → ⊥
  cut6378  adequate = bad6378  (Adequate.valid adequate Two boolean env5)
  bad6379 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b1 b1) b0)) (bop b1 b1)) b0 → ⊥
  bad6379  p = false≢true (sym (cong lower p))
  cut6379 : Adequate {ℓ} ((op (op (var 0) (op (op (var 1) (var 1)) (var 2))) (op (var 1) (var 1))) , (var 0)) → ⊥
  cut6379  adequate = bad6379  (Adequate.valid adequate Two boolean env4)
  bad6380 : PathP (λ _ → Two) (bop (bop b1 (bop (bop b0 b0) b0)) (bop b0 b0)) b0 → ⊥
  bad6380  p = false≢true (sym (cong lower p))
  cut6380 : Adequate {ℓ} ((op (op (var 0) (op (op (var 1) (var 1)) (var 2))) (op (var 1) (var 1))) , (var 1)) → ⊥
  cut6380  adequate = bad6380  (Adequate.valid adequate Two boolean env6)
  bad6381 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b0 b0) b1)) (bop b0 b0)) b1 → ⊥
  bad6381  p = false≢true (cong lower p)
  cut6381 : Adequate {ℓ} ((op (op (var 0) (op (op (var 1) (var 1)) (var 2))) (op (var 1) (var 1))) , (var 2)) → ⊥
  cut6381  adequate = bad6381  (Adequate.valid adequate Two boolean env1)
  bad6382 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b0 b0) b0)) (bop b0 b0)) b1 → ⊥
  bad6382  p = false≢true (cong lower p)
  cut6382 : Adequate {ℓ} ((op (op (var 0) (op (op (var 1) (var 1)) (var 2))) (op (var 1) (var 1))) , (var 3)) → ⊥
  cut6382  adequate = bad6382  (Adequate.valid adequate Two boolean env5)
  bad6383 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b1 b1) b1)) (bop b1 b1)) b0 → ⊥
  bad6383  p = false≢true (sym (cong lower p))
  cut6383 : Adequate {ℓ} ((op (op (var 0) (op (op (var 1) (var 1)) (var 2))) (op (var 1) (var 2))) , (var 0)) → ⊥
  cut6383  adequate = bad6383  (Adequate.valid adequate Two boolean env3)
  bad6384 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b1 b1) b0)) (bop b1 b0)) b1 → ⊥
  bad6384  p = false≢true (cong lower p)
  cut6384 : Adequate {ℓ} ((op (op (var 0) (op (op (var 1) (var 1)) (var 2))) (op (var 1) (var 2))) , (var 1)) → ⊥
  cut6384  adequate = bad6384  (Adequate.valid adequate Two boolean env4)
  bad6385 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b0 b0) b1)) (bop b0 b1)) b1 → ⊥
  bad6385  p = false≢true (cong lower p)
  cut6385 : Adequate {ℓ} ((op (op (var 0) (op (op (var 1) (var 1)) (var 2))) (op (var 1) (var 2))) , (var 2)) → ⊥
  cut6385  adequate = bad6385  (Adequate.valid adequate Two boolean env1)
  bad6386 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b0 b0) b0)) (bop b0 b0)) b1 → ⊥
  bad6386  p = false≢true (cong lower p)
  cut6386 : Adequate {ℓ} ((op (op (var 0) (op (op (var 1) (var 1)) (var 2))) (op (var 1) (var 2))) , (var 3)) → ⊥
  cut6386  adequate = bad6386  (Adequate.valid adequate Two boolean env5)
  bad6387 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b1 b1) b0)) (bop b1 b1)) b0 → ⊥
  bad6387  p = false≢true (sym (cong lower p))
  cut6387 : Adequate {ℓ} ((op (op (var 0) (op (op (var 1) (var 1)) (var 2))) (op (var 1) (var 3))) , (var 0)) → ⊥
  cut6387  adequate = bad6387  (Adequate.valid adequate Two boolean env14)
  bad6388 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b1 b1) b0)) (bop b1 b0)) b1 → ⊥
  bad6388  p = false≢true (cong lower p)
  cut6388 : Adequate {ℓ} ((op (op (var 0) (op (op (var 1) (var 1)) (var 2))) (op (var 1) (var 3))) , (var 1)) → ⊥
  cut6388  adequate = bad6388  (Adequate.valid adequate Two boolean env13)
  bad6389 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b0 b0) b1)) (bop b0 b0)) b1 → ⊥
  bad6389  p = false≢true (cong lower p)
  cut6389 : Adequate {ℓ} ((op (op (var 0) (op (op (var 1) (var 1)) (var 2))) (op (var 1) (var 3))) , (var 2)) → ⊥
  cut6389  adequate = bad6389  (Adequate.valid adequate Two boolean env8)
  bad6390 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b0 b0) b0)) (bop b0 b1)) b1 → ⊥
  bad6390  p = false≢true (cong lower p)
  cut6390 : Adequate {ℓ} ((op (op (var 0) (op (op (var 1) (var 1)) (var 2))) (op (var 1) (var 3))) , (var 3)) → ⊥
  cut6390  adequate = bad6390  (Adequate.valid adequate Two boolean env5)
  bad6391 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b0 b0) b0)) (bop b0 b0)) b1 → ⊥
  bad6391  p = false≢true (cong lower p)
  cut6391 : Adequate {ℓ} ((op (op (var 0) (op (op (var 1) (var 1)) (var 2))) (op (var 1) (var 3))) , (var 4)) → ⊥
  cut6391  adequate = bad6391  (Adequate.valid adequate Two boolean env9)
  holds6392 : (z0 z1 z2 : A2) → (mul2 (mul2 z0 (mul2 (mul2 z1 z1) z2)) (mul2 z2 z0)) ≡ z0
  holds6392 z0 z1 z2 = refl
  cut6392 : Adequate {ℓ} ((op (op (var 0) (op (op (var 1) (var 1)) (var 2))) (op (var 2) (var 0))) , (var 0)) → ⊥
  cut6392  = reject2 ((op (op (var 0) (op (op (var 1) (var 1)) (var 2))) (op (var 2) (var 0))) , (var 0)) (λ env → holds6392 (env 0) (env 1) (env 2))
  bad6393 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b1 b1) b0)) (bop b0 b0)) b1 → ⊥
  bad6393  p = false≢true (cong lower p)
  cut6393 : Adequate {ℓ} ((op (op (var 0) (op (op (var 1) (var 1)) (var 2))) (op (var 2) (var 0))) , (var 1)) → ⊥
  cut6393  adequate = bad6393  (Adequate.valid adequate Two boolean env4)
  bad6394 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b0 b0) b1)) (bop b1 b0)) b1 → ⊥
  bad6394  p = false≢true (cong lower p)
  cut6394 : Adequate {ℓ} ((op (op (var 0) (op (op (var 1) (var 1)) (var 2))) (op (var 2) (var 0))) , (var 2)) → ⊥
  cut6394  adequate = bad6394  (Adequate.valid adequate Two boolean env1)
  bad6395 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b0 b0) b0)) (bop b0 b0)) b1 → ⊥
  bad6395  p = false≢true (cong lower p)
  cut6395 : Adequate {ℓ} ((op (op (var 0) (op (op (var 1) (var 1)) (var 2))) (op (var 2) (var 0))) , (var 3)) → ⊥
  cut6395  adequate = bad6395  (Adequate.valid adequate Two boolean env5)
  bad6396 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b1 b1) b1)) (bop b1 b1)) b0 → ⊥
  bad6396  p = false≢true (sym (cong lower p))
  cut6396 : Adequate {ℓ} ((op (op (var 0) (op (op (var 1) (var 1)) (var 2))) (op (var 2) (var 1))) , (var 0)) → ⊥
  cut6396  adequate = bad6396  (Adequate.valid adequate Two boolean env3)
  bad6397 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b1 b1) b0)) (bop b0 b1)) b1 → ⊥
  bad6397  p = false≢true (cong lower p)
  cut6397 : Adequate {ℓ} ((op (op (var 0) (op (op (var 1) (var 1)) (var 2))) (op (var 2) (var 1))) , (var 1)) → ⊥
  cut6397  adequate = bad6397  (Adequate.valid adequate Two boolean env4)
  bad6398 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b0 b0) b1)) (bop b1 b0)) b1 → ⊥
  bad6398  p = false≢true (cong lower p)
  cut6398 : Adequate {ℓ} ((op (op (var 0) (op (op (var 1) (var 1)) (var 2))) (op (var 2) (var 1))) , (var 2)) → ⊥
  cut6398  adequate = bad6398  (Adequate.valid adequate Two boolean env1)
  bad6399 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b0 b0) b0)) (bop b0 b0)) b1 → ⊥
  bad6399  p = false≢true (cong lower p)
  cut6399 : Adequate {ℓ} ((op (op (var 0) (op (op (var 1) (var 1)) (var 2))) (op (var 2) (var 1))) , (var 3)) → ⊥
  cut6399  adequate = bad6399  (Adequate.valid adequate Two boolean env5)
  bad6400 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b0 b0) b1)) (bop b1 b1)) b0 → ⊥
  bad6400  p = false≢true (sym (cong lower p))
  cut6400 : Adequate {ℓ} ((op (op (var 0) (op (op (var 1) (var 1)) (var 2))) (op (var 2) (var 2))) , (var 0)) → ⊥
  cut6400  adequate = bad6400  (Adequate.valid adequate Two boolean env1)
  bad6401 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b0 b0) b1)) (bop b1 b1)) b0 → ⊥
  bad6401  p = false≢true (sym (cong lower p))
  cut6401 : Adequate {ℓ} ((op (op (var 0) (op (op (var 1) (var 1)) (var 2))) (op (var 2) (var 2))) , (var 1)) → ⊥
  cut6401  adequate = bad6401  (Adequate.valid adequate Two boolean env1)
  bad6402 : PathP (λ _ → Two) (bop (bop b1 (bop (bop b0 b0) b0)) (bop b0 b0)) b0 → ⊥
  bad6402  p = false≢true (sym (cong lower p))
  cut6402 : Adequate {ℓ} ((op (op (var 0) (op (op (var 1) (var 1)) (var 2))) (op (var 2) (var 2))) , (var 2)) → ⊥
  cut6402  adequate = bad6402  (Adequate.valid adequate Two boolean env6)
  bad6403 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b0 b0) b0)) (bop b0 b0)) b1 → ⊥
  bad6403  p = false≢true (cong lower p)
  cut6403 : Adequate {ℓ} ((op (op (var 0) (op (op (var 1) (var 1)) (var 2))) (op (var 2) (var 2))) , (var 3)) → ⊥
  cut6403  adequate = bad6403  (Adequate.valid adequate Two boolean env5)
  bad6404 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b0 b0) b1)) (bop b1 b1)) b0 → ⊥
  bad6404  p = false≢true (sym (cong lower p))
  cut6404 : Adequate {ℓ} ((op (op (var 0) (op (op (var 1) (var 1)) (var 2))) (op (var 2) (var 3))) , (var 0)) → ⊥
  cut6404  adequate = bad6404  (Adequate.valid adequate Two boolean env7)
  bad6405 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b0 b0) b1)) (bop b1 b1)) b0 → ⊥
  bad6405  p = false≢true (sym (cong lower p))
  cut6405 : Adequate {ℓ} ((op (op (var 0) (op (op (var 1) (var 1)) (var 2))) (op (var 2) (var 3))) , (var 1)) → ⊥
  cut6405  adequate = bad6405  (Adequate.valid adequate Two boolean env7)
  bad6406 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b0 b0) b1)) (bop b1 b0)) b1 → ⊥
  bad6406  p = false≢true (cong lower p)
  cut6406 : Adequate {ℓ} ((op (op (var 0) (op (op (var 1) (var 1)) (var 2))) (op (var 2) (var 3))) , (var 2)) → ⊥
  cut6406  adequate = bad6406  (Adequate.valid adequate Two boolean env8)
  bad6407 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b0 b0) b0)) (bop b0 b1)) b1 → ⊥
  bad6407  p = false≢true (cong lower p)
  cut6407 : Adequate {ℓ} ((op (op (var 0) (op (op (var 1) (var 1)) (var 2))) (op (var 2) (var 3))) , (var 3)) → ⊥
  cut6407  adequate = bad6407  (Adequate.valid adequate Two boolean env5)
  bad6408 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b0 b0) b0)) (bop b0 b0)) b1 → ⊥
  bad6408  p = false≢true (cong lower p)
  cut6408 : Adequate {ℓ} ((op (op (var 0) (op (op (var 1) (var 1)) (var 2))) (op (var 2) (var 3))) , (var 4)) → ⊥
  cut6408  adequate = bad6408  (Adequate.valid adequate Two boolean env9)
  bad6409 : PathP (λ _ → Two) (bop (bop b1 (bop (bop b0 b0) b1)) (bop b0 b1)) b1 → ⊥
  bad6409  p = false≢true (cong lower p)
  cut6409 : Adequate {ℓ} ((op (op (var 0) (op (op (var 1) (var 1)) (var 2))) (op (var 3) (var 0))) , (var 0)) → ⊥
  cut6409  adequate = bad6409  (Adequate.valid adequate Two boolean env12)
  bad6410 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b1 b1) b0)) (bop b0 b0)) b1 → ⊥
  bad6410  p = false≢true (cong lower p)
  cut6410 : Adequate {ℓ} ((op (op (var 0) (op (op (var 1) (var 1)) (var 2))) (op (var 3) (var 0))) , (var 1)) → ⊥
  cut6410  adequate = bad6410  (Adequate.valid adequate Two boolean env13)
  bad6411 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b0 b0) b1)) (bop b0 b0)) b1 → ⊥
  bad6411  p = false≢true (cong lower p)
  cut6411 : Adequate {ℓ} ((op (op (var 0) (op (op (var 1) (var 1)) (var 2))) (op (var 3) (var 0))) , (var 2)) → ⊥
  cut6411  adequate = bad6411  (Adequate.valid adequate Two boolean env8)
  bad6412 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b0 b0) b0)) (bop b1 b0)) b1 → ⊥
  bad6412  p = false≢true (cong lower p)
  cut6412 : Adequate {ℓ} ((op (op (var 0) (op (op (var 1) (var 1)) (var 2))) (op (var 3) (var 0))) , (var 3)) → ⊥
  cut6412  adequate = bad6412  (Adequate.valid adequate Two boolean env5)
  bad6413 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b0 b0) b0)) (bop b0 b0)) b1 → ⊥
  bad6413  p = false≢true (cong lower p)
  cut6413 : Adequate {ℓ} ((op (op (var 0) (op (op (var 1) (var 1)) (var 2))) (op (var 3) (var 0))) , (var 4)) → ⊥
  cut6413  adequate = bad6413  (Adequate.valid adequate Two boolean env9)
  bad6414 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b1 b1) b0)) (bop b1 b1)) b0 → ⊥
  bad6414  p = false≢true (sym (cong lower p))
  cut6414 : Adequate {ℓ} ((op (op (var 0) (op (op (var 1) (var 1)) (var 2))) (op (var 3) (var 1))) , (var 0)) → ⊥
  cut6414  adequate = bad6414  (Adequate.valid adequate Two boolean env14)
  bad6415 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b1 b1) b0)) (bop b0 b1)) b1 → ⊥
  bad6415  p = false≢true (cong lower p)
  cut6415 : Adequate {ℓ} ((op (op (var 0) (op (op (var 1) (var 1)) (var 2))) (op (var 3) (var 1))) , (var 1)) → ⊥
  cut6415  adequate = bad6415  (Adequate.valid adequate Two boolean env13)
  bad6416 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b0 b0) b1)) (bop b0 b0)) b1 → ⊥
  bad6416  p = false≢true (cong lower p)
  cut6416 : Adequate {ℓ} ((op (op (var 0) (op (op (var 1) (var 1)) (var 2))) (op (var 3) (var 1))) , (var 2)) → ⊥
  cut6416  adequate = bad6416  (Adequate.valid adequate Two boolean env8)
  bad6417 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b0 b0) b0)) (bop b1 b0)) b1 → ⊥
  bad6417  p = false≢true (cong lower p)
  cut6417 : Adequate {ℓ} ((op (op (var 0) (op (op (var 1) (var 1)) (var 2))) (op (var 3) (var 1))) , (var 3)) → ⊥
  cut6417  adequate = bad6417  (Adequate.valid adequate Two boolean env5)
  bad6418 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b0 b0) b0)) (bop b0 b0)) b1 → ⊥
  bad6418  p = false≢true (cong lower p)
  cut6418 : Adequate {ℓ} ((op (op (var 0) (op (op (var 1) (var 1)) (var 2))) (op (var 3) (var 1))) , (var 4)) → ⊥
  cut6418  adequate = bad6418  (Adequate.valid adequate Two boolean env9)
  bad6419 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b0 b0) b1)) (bop b1 b1)) b0 → ⊥
  bad6419  p = false≢true (sym (cong lower p))
  cut6419 : Adequate {ℓ} ((op (op (var 0) (op (op (var 1) (var 1)) (var 2))) (op (var 3) (var 2))) , (var 0)) → ⊥
  cut6419  adequate = bad6419  (Adequate.valid adequate Two boolean env7)
  bad6420 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b0 b0) b1)) (bop b1 b1)) b0 → ⊥
  bad6420  p = false≢true (sym (cong lower p))
  cut6420 : Adequate {ℓ} ((op (op (var 0) (op (op (var 1) (var 1)) (var 2))) (op (var 3) (var 2))) , (var 1)) → ⊥
  cut6420  adequate = bad6420  (Adequate.valid adequate Two boolean env7)
  bad6421 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b0 b0) b1)) (bop b0 b1)) b1 → ⊥
  bad6421  p = false≢true (cong lower p)
  cut6421 : Adequate {ℓ} ((op (op (var 0) (op (op (var 1) (var 1)) (var 2))) (op (var 3) (var 2))) , (var 2)) → ⊥
  cut6421  adequate = bad6421  (Adequate.valid adequate Two boolean env8)
  bad6422 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b0 b0) b0)) (bop b1 b0)) b1 → ⊥
  bad6422  p = false≢true (cong lower p)
  cut6422 : Adequate {ℓ} ((op (op (var 0) (op (op (var 1) (var 1)) (var 2))) (op (var 3) (var 2))) , (var 3)) → ⊥
  cut6422  adequate = bad6422  (Adequate.valid adequate Two boolean env5)
  bad6423 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b0 b0) b0)) (bop b0 b0)) b1 → ⊥
  bad6423  p = false≢true (cong lower p)
  cut6423 : Adequate {ℓ} ((op (op (var 0) (op (op (var 1) (var 1)) (var 2))) (op (var 3) (var 2))) , (var 4)) → ⊥
  cut6423  adequate = bad6423  (Adequate.valid adequate Two boolean env9)
  bad6424 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b0 b0) b0)) (bop b1 b1)) b0 → ⊥
  bad6424  p = false≢true (sym (cong lower p))
  cut6424 : Adequate {ℓ} ((op (op (var 0) (op (op (var 1) (var 1)) (var 2))) (op (var 3) (var 3))) , (var 0)) → ⊥
  cut6424  adequate = bad6424  (Adequate.valid adequate Two boolean env5)
  bad6425 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b0 b0) b0)) (bop b1 b1)) b0 → ⊥
  bad6425  p = false≢true (sym (cong lower p))
  cut6425 : Adequate {ℓ} ((op (op (var 0) (op (op (var 1) (var 1)) (var 2))) (op (var 3) (var 3))) , (var 1)) → ⊥
  cut6425  adequate = bad6425  (Adequate.valid adequate Two boolean env5)
  bad6426 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b0 b0) b0)) (bop b1 b1)) b0 → ⊥
  bad6426  p = false≢true (sym (cong lower p))
  cut6426 : Adequate {ℓ} ((op (op (var 0) (op (op (var 1) (var 1)) (var 2))) (op (var 3) (var 3))) , (var 2)) → ⊥
  cut6426  adequate = bad6426  (Adequate.valid adequate Two boolean env5)
  bad6427 : PathP (λ _ → Two) (bop (bop b1 (bop (bop b0 b0) b0)) (bop b0 b0)) b0 → ⊥
  bad6427  p = false≢true (sym (cong lower p))
  cut6427 : Adequate {ℓ} ((op (op (var 0) (op (op (var 1) (var 1)) (var 2))) (op (var 3) (var 3))) , (var 3)) → ⊥
  cut6427  adequate = bad6427  (Adequate.valid adequate Two boolean env15)
  bad6428 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b0 b0) b0)) (bop b0 b0)) b1 → ⊥
  bad6428  p = false≢true (cong lower p)
  cut6428 : Adequate {ℓ} ((op (op (var 0) (op (op (var 1) (var 1)) (var 2))) (op (var 3) (var 3))) , (var 4)) → ⊥
  cut6428  adequate = bad6428  (Adequate.valid adequate Two boolean env9)
  bad6429 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b0 b0) b0)) (bop b1 b1)) b0 → ⊥
  bad6429  p = false≢true (sym (cong lower p))
  cut6429 : Adequate {ℓ} ((op (op (var 0) (op (op (var 1) (var 1)) (var 2))) (op (var 3) (var 4))) , (var 0)) → ⊥
  cut6429  adequate = bad6429  (Adequate.valid adequate Two boolean env16)
  bad6430 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b0 b0) b0)) (bop b1 b1)) b0 → ⊥
  bad6430  p = false≢true (sym (cong lower p))
  cut6430 : Adequate {ℓ} ((op (op (var 0) (op (op (var 1) (var 1)) (var 2))) (op (var 3) (var 4))) , (var 1)) → ⊥
  cut6430  adequate = bad6430  (Adequate.valid adequate Two boolean env16)
  bad6431 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b0 b0) b0)) (bop b1 b1)) b0 → ⊥
  bad6431  p = false≢true (sym (cong lower p))
  cut6431 : Adequate {ℓ} ((op (op (var 0) (op (op (var 1) (var 1)) (var 2))) (op (var 3) (var 4))) , (var 2)) → ⊥
  cut6431  adequate = bad6431  (Adequate.valid adequate Two boolean env16)
  bad6432 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b0 b0) b0)) (bop b1 b0)) b1 → ⊥
  bad6432  p = false≢true (cong lower p)
  cut6432 : Adequate {ℓ} ((op (op (var 0) (op (op (var 1) (var 1)) (var 2))) (op (var 3) (var 4))) , (var 3)) → ⊥
  cut6432  adequate = bad6432  (Adequate.valid adequate Two boolean env17)
  bad6433 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b0 b0) b0)) (bop b0 b1)) b1 → ⊥
  bad6433  p = false≢true (cong lower p)
  cut6433 : Adequate {ℓ} ((op (op (var 0) (op (op (var 1) (var 1)) (var 2))) (op (var 3) (var 4))) , (var 4)) → ⊥
  cut6433  adequate = bad6433  (Adequate.valid adequate Two boolean env9)
  bad6434 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b0 b0) b0)) (bop b0 b0)) b1 → ⊥
  bad6434  p = false≢true (cong lower p)
  cut6434 : Adequate {ℓ} ((op (op (var 0) (op (op (var 1) (var 1)) (var 2))) (op (var 3) (var 4))) , (var 5)) → ⊥
  cut6434  adequate = bad6434  (Adequate.valid adequate Two boolean env18)
  holds6435 : (z0 z1 z2 : A2) → (mul2 (mul2 z0 (mul2 (mul2 z1 z2) z0)) (mul2 z0 z0)) ≡ z0
  holds6435 z0 z1 z2 = refl
  cut6435 : Adequate {ℓ} ((op (op (var 0) (op (op (var 1) (var 2)) (var 0))) (op (var 0) (var 0))) , (var 0)) → ⊥
  cut6435  = reject2 ((op (op (var 0) (op (op (var 1) (var 2)) (var 0))) (op (var 0) (var 0))) , (var 0)) (λ env → holds6435 (env 0) (env 1) (env 2))
  bad6436 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b1 b0) b0)) (bop b0 b0)) b1 → ⊥
  bad6436  p = false≢true (cong lower p)
  cut6436 : Adequate {ℓ} ((op (op (var 0) (op (op (var 1) (var 2)) (var 0))) (op (var 0) (var 0))) , (var 1)) → ⊥
  cut6436  adequate = bad6436  (Adequate.valid adequate Two boolean env4)
  bad6437 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b0 b1) b0)) (bop b0 b0)) b1 → ⊥
  bad6437  p = false≢true (cong lower p)
  cut6437 : Adequate {ℓ} ((op (op (var 0) (op (op (var 1) (var 2)) (var 0))) (op (var 0) (var 0))) , (var 2)) → ⊥
  cut6437  adequate = bad6437  (Adequate.valid adequate Two boolean env1)
  bad6438 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b0 b0) b0)) (bop b0 b0)) b1 → ⊥
  bad6438  p = false≢true (cong lower p)
  cut6438 : Adequate {ℓ} ((op (op (var 0) (op (op (var 1) (var 2)) (var 0))) (op (var 0) (var 0))) , (var 3)) → ⊥
  cut6438  adequate = bad6438  (Adequate.valid adequate Two boolean env5)
  bad6439 : PathP (λ _ → Two) (bop (bop b1 (bop (bop b0 b0) b1)) (bop b1 b0)) b1 → ⊥
  bad6439  p = false≢true (cong lower p)
  cut6439 : Adequate {ℓ} ((op (op (var 0) (op (op (var 1) (var 2)) (var 0))) (op (var 0) (var 1))) , (var 0)) → ⊥
  cut6439  adequate = bad6439  (Adequate.valid adequate Two boolean env6)
  bad6440 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b1 b0) b0)) (bop b0 b1)) b1 → ⊥
  bad6440  p = false≢true (cong lower p)
  cut6440 : Adequate {ℓ} ((op (op (var 0) (op (op (var 1) (var 2)) (var 0))) (op (var 0) (var 1))) , (var 1)) → ⊥
  cut6440  adequate = bad6440  (Adequate.valid adequate Two boolean env4)
  bad6441 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b0 b1) b0)) (bop b0 b0)) b1 → ⊥
  bad6441  p = false≢true (cong lower p)
  cut6441 : Adequate {ℓ} ((op (op (var 0) (op (op (var 1) (var 2)) (var 0))) (op (var 0) (var 1))) , (var 2)) → ⊥
  cut6441  adequate = bad6441  (Adequate.valid adequate Two boolean env1)
  bad6442 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b0 b0) b0)) (bop b0 b0)) b1 → ⊥
  bad6442  p = false≢true (cong lower p)
  cut6442 : Adequate {ℓ} ((op (op (var 0) (op (op (var 1) (var 2)) (var 0))) (op (var 0) (var 1))) , (var 3)) → ⊥
  cut6442  adequate = bad6442  (Adequate.valid adequate Two boolean env5)
  bad6443 : PathP (λ _ → Two) (bop (bop b1 (bop (bop b0 b0) b1)) (bop b1 b0)) b1 → ⊥
  bad6443  p = false≢true (cong lower p)
  cut6443 : Adequate {ℓ} ((op (op (var 0) (op (op (var 1) (var 2)) (var 0))) (op (var 0) (var 2))) , (var 0)) → ⊥
  cut6443  adequate = bad6443  (Adequate.valid adequate Two boolean env6)
  bad6444 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b1 b0) b0)) (bop b0 b0)) b1 → ⊥
  bad6444  p = false≢true (cong lower p)
  cut6444 : Adequate {ℓ} ((op (op (var 0) (op (op (var 1) (var 2)) (var 0))) (op (var 0) (var 2))) , (var 1)) → ⊥
  cut6444  adequate = bad6444  (Adequate.valid adequate Two boolean env4)
  bad6445 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b0 b1) b0)) (bop b0 b1)) b1 → ⊥
  bad6445  p = false≢true (cong lower p)
  cut6445 : Adequate {ℓ} ((op (op (var 0) (op (op (var 1) (var 2)) (var 0))) (op (var 0) (var 2))) , (var 2)) → ⊥
  cut6445  adequate = bad6445  (Adequate.valid adequate Two boolean env1)
  bad6446 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b0 b0) b0)) (bop b0 b0)) b1 → ⊥
  bad6446  p = false≢true (cong lower p)
  cut6446 : Adequate {ℓ} ((op (op (var 0) (op (op (var 1) (var 2)) (var 0))) (op (var 0) (var 2))) , (var 3)) → ⊥
  cut6446  adequate = bad6446  (Adequate.valid adequate Two boolean env5)
  bad6447 : PathP (λ _ → Two) (bop (bop b1 (bop (bop b0 b0) b1)) (bop b1 b0)) b1 → ⊥
  bad6447  p = false≢true (cong lower p)
  cut6447 : Adequate {ℓ} ((op (op (var 0) (op (op (var 1) (var 2)) (var 0))) (op (var 0) (var 3))) , (var 0)) → ⊥
  cut6447  adequate = bad6447  (Adequate.valid adequate Two boolean env15)
  bad6448 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b1 b0) b0)) (bop b0 b0)) b1 → ⊥
  bad6448  p = false≢true (cong lower p)
  cut6448 : Adequate {ℓ} ((op (op (var 0) (op (op (var 1) (var 2)) (var 0))) (op (var 0) (var 3))) , (var 1)) → ⊥
  cut6448  adequate = bad6448  (Adequate.valid adequate Two boolean env13)
  bad6449 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b0 b1) b0)) (bop b0 b0)) b1 → ⊥
  bad6449  p = false≢true (cong lower p)
  cut6449 : Adequate {ℓ} ((op (op (var 0) (op (op (var 1) (var 2)) (var 0))) (op (var 0) (var 3))) , (var 2)) → ⊥
  cut6449  adequate = bad6449  (Adequate.valid adequate Two boolean env8)
  bad6450 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b0 b0) b0)) (bop b0 b1)) b1 → ⊥
  bad6450  p = false≢true (cong lower p)
  cut6450 : Adequate {ℓ} ((op (op (var 0) (op (op (var 1) (var 2)) (var 0))) (op (var 0) (var 3))) , (var 3)) → ⊥
  cut6450  adequate = bad6450  (Adequate.valid adequate Two boolean env5)
  bad6451 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b0 b0) b0)) (bop b0 b0)) b1 → ⊥
  bad6451  p = false≢true (cong lower p)
  cut6451 : Adequate {ℓ} ((op (op (var 0) (op (op (var 1) (var 2)) (var 0))) (op (var 0) (var 3))) , (var 4)) → ⊥
  cut6451  adequate = bad6451  (Adequate.valid adequate Two boolean env9)
  bad6452 : PathP (λ _ → Two) (bop (bop b1 (bop (bop b0 b0) b1)) (bop b0 b1)) b1 → ⊥
  bad6452  p = false≢true (cong lower p)
  cut6452 : Adequate {ℓ} ((op (op (var 0) (op (op (var 1) (var 2)) (var 0))) (op (var 1) (var 0))) , (var 0)) → ⊥
  cut6452  adequate = bad6452  (Adequate.valid adequate Two boolean env6)
  bad6453 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b1 b0) b0)) (bop b1 b0)) b1 → ⊥
  bad6453  p = false≢true (cong lower p)
  cut6453 : Adequate {ℓ} ((op (op (var 0) (op (op (var 1) (var 2)) (var 0))) (op (var 1) (var 0))) , (var 1)) → ⊥
  cut6453  adequate = bad6453  (Adequate.valid adequate Two boolean env4)
  bad6454 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b0 b1) b0)) (bop b0 b0)) b1 → ⊥
  bad6454  p = false≢true (cong lower p)
  cut6454 : Adequate {ℓ} ((op (op (var 0) (op (op (var 1) (var 2)) (var 0))) (op (var 1) (var 0))) , (var 2)) → ⊥
  cut6454  adequate = bad6454  (Adequate.valid adequate Two boolean env1)
  bad6455 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b0 b0) b0)) (bop b0 b0)) b1 → ⊥
  bad6455  p = false≢true (cong lower p)
  cut6455 : Adequate {ℓ} ((op (op (var 0) (op (op (var 1) (var 2)) (var 0))) (op (var 1) (var 0))) , (var 3)) → ⊥
  cut6455  adequate = bad6455  (Adequate.valid adequate Two boolean env5)
  bad6456 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b1 b0) b0)) (bop b1 b1)) b0 → ⊥
  bad6456  p = false≢true (sym (cong lower p))
  cut6456 : Adequate {ℓ} ((op (op (var 0) (op (op (var 1) (var 2)) (var 0))) (op (var 1) (var 1))) , (var 0)) → ⊥
  cut6456  adequate = bad6456  (Adequate.valid adequate Two boolean env4)
  holds6457 : (z0 z1 z2 : A3) → (mul3 (mul3 z0 (mul3 (mul3 z1 z2) z0)) (mul3 z1 z1)) ≡ z1
  holds6457 z0 z1 z2 = refl
  cut6457 : Adequate {ℓ} ((op (op (var 0) (op (op (var 1) (var 2)) (var 0))) (op (var 1) (var 1))) , (var 1)) → ⊥
  cut6457  = reject3 ((op (op (var 0) (op (op (var 1) (var 2)) (var 0))) (op (var 1) (var 1))) , (var 1)) (λ env → holds6457 (env 0) (env 1) (env 2))
  bad6458 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b0 b1) b0)) (bop b0 b0)) b1 → ⊥
  bad6458  p = false≢true (cong lower p)
  cut6458 : Adequate {ℓ} ((op (op (var 0) (op (op (var 1) (var 2)) (var 0))) (op (var 1) (var 1))) , (var 2)) → ⊥
  cut6458  adequate = bad6458  (Adequate.valid adequate Two boolean env1)
  bad6459 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b0 b0) b0)) (bop b0 b0)) b1 → ⊥
  bad6459  p = false≢true (cong lower p)
  cut6459 : Adequate {ℓ} ((op (op (var 0) (op (op (var 1) (var 2)) (var 0))) (op (var 1) (var 1))) , (var 3)) → ⊥
  cut6459  adequate = bad6459  (Adequate.valid adequate Two boolean env5)
  bad6460 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b1 b1) b0)) (bop b1 b1)) b0 → ⊥
  bad6460  p = false≢true (sym (cong lower p))
  cut6460 : Adequate {ℓ} ((op (op (var 0) (op (op (var 1) (var 2)) (var 0))) (op (var 1) (var 2))) , (var 0)) → ⊥
  cut6460  adequate = bad6460  (Adequate.valid adequate Two boolean env3)
  bad6461 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b1 b0) b0)) (bop b1 b0)) b1 → ⊥
  bad6461  p = false≢true (cong lower p)
  cut6461 : Adequate {ℓ} ((op (op (var 0) (op (op (var 1) (var 2)) (var 0))) (op (var 1) (var 2))) , (var 1)) → ⊥
  cut6461  adequate = bad6461  (Adequate.valid adequate Two boolean env4)
  bad6462 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b0 b1) b0)) (bop b0 b1)) b1 → ⊥
  bad6462  p = false≢true (cong lower p)
  cut6462 : Adequate {ℓ} ((op (op (var 0) (op (op (var 1) (var 2)) (var 0))) (op (var 1) (var 2))) , (var 2)) → ⊥
  cut6462  adequate = bad6462  (Adequate.valid adequate Two boolean env1)
  bad6463 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b0 b0) b0)) (bop b0 b0)) b1 → ⊥
  bad6463  p = false≢true (cong lower p)
  cut6463 : Adequate {ℓ} ((op (op (var 0) (op (op (var 1) (var 2)) (var 0))) (op (var 1) (var 2))) , (var 3)) → ⊥
  cut6463  adequate = bad6463  (Adequate.valid adequate Two boolean env5)
  bad6464 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b1 b0) b0)) (bop b1 b1)) b0 → ⊥
  bad6464  p = false≢true (sym (cong lower p))
  cut6464 : Adequate {ℓ} ((op (op (var 0) (op (op (var 1) (var 2)) (var 0))) (op (var 1) (var 3))) , (var 0)) → ⊥
  cut6464  adequate = bad6464  (Adequate.valid adequate Two boolean env14)
  bad6465 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b1 b0) b0)) (bop b1 b0)) b1 → ⊥
  bad6465  p = false≢true (cong lower p)
  cut6465 : Adequate {ℓ} ((op (op (var 0) (op (op (var 1) (var 2)) (var 0))) (op (var 1) (var 3))) , (var 1)) → ⊥
  cut6465  adequate = bad6465  (Adequate.valid adequate Two boolean env13)
  bad6466 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b0 b1) b0)) (bop b0 b0)) b1 → ⊥
  bad6466  p = false≢true (cong lower p)
  cut6466 : Adequate {ℓ} ((op (op (var 0) (op (op (var 1) (var 2)) (var 0))) (op (var 1) (var 3))) , (var 2)) → ⊥
  cut6466  adequate = bad6466  (Adequate.valid adequate Two boolean env8)
  bad6467 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b0 b0) b0)) (bop b0 b1)) b1 → ⊥
  bad6467  p = false≢true (cong lower p)
  cut6467 : Adequate {ℓ} ((op (op (var 0) (op (op (var 1) (var 2)) (var 0))) (op (var 1) (var 3))) , (var 3)) → ⊥
  cut6467  adequate = bad6467  (Adequate.valid adequate Two boolean env5)
  bad6468 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b0 b0) b0)) (bop b0 b0)) b1 → ⊥
  bad6468  p = false≢true (cong lower p)
  cut6468 : Adequate {ℓ} ((op (op (var 0) (op (op (var 1) (var 2)) (var 0))) (op (var 1) (var 3))) , (var 4)) → ⊥
  cut6468  adequate = bad6468  (Adequate.valid adequate Two boolean env9)
  bad6469 : PathP (λ _ → Two) (bop (bop b1 (bop (bop b0 b0) b1)) (bop b0 b1)) b1 → ⊥
  bad6469  p = false≢true (cong lower p)
  cut6469 : Adequate {ℓ} ((op (op (var 0) (op (op (var 1) (var 2)) (var 0))) (op (var 2) (var 0))) , (var 0)) → ⊥
  cut6469  adequate = bad6469  (Adequate.valid adequate Two boolean env6)
  bad6470 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b1 b0) b0)) (bop b0 b0)) b1 → ⊥
  bad6470  p = false≢true (cong lower p)
  cut6470 : Adequate {ℓ} ((op (op (var 0) (op (op (var 1) (var 2)) (var 0))) (op (var 2) (var 0))) , (var 1)) → ⊥
  cut6470  adequate = bad6470  (Adequate.valid adequate Two boolean env4)
  bad6471 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b0 b1) b0)) (bop b1 b0)) b1 → ⊥
  bad6471  p = false≢true (cong lower p)
  cut6471 : Adequate {ℓ} ((op (op (var 0) (op (op (var 1) (var 2)) (var 0))) (op (var 2) (var 0))) , (var 2)) → ⊥
  cut6471  adequate = bad6471  (Adequate.valid adequate Two boolean env1)
  bad6472 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b0 b0) b0)) (bop b0 b0)) b1 → ⊥
  bad6472  p = false≢true (cong lower p)
  cut6472 : Adequate {ℓ} ((op (op (var 0) (op (op (var 1) (var 2)) (var 0))) (op (var 2) (var 0))) , (var 3)) → ⊥
  cut6472  adequate = bad6472  (Adequate.valid adequate Two boolean env5)
  bad6473 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b1 b1) b0)) (bop b1 b1)) b0 → ⊥
  bad6473  p = false≢true (sym (cong lower p))
  cut6473 : Adequate {ℓ} ((op (op (var 0) (op (op (var 1) (var 2)) (var 0))) (op (var 2) (var 1))) , (var 0)) → ⊥
  cut6473  adequate = bad6473  (Adequate.valid adequate Two boolean env3)
  bad6474 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b1 b0) b0)) (bop b0 b1)) b1 → ⊥
  bad6474  p = false≢true (cong lower p)
  cut6474 : Adequate {ℓ} ((op (op (var 0) (op (op (var 1) (var 2)) (var 0))) (op (var 2) (var 1))) , (var 1)) → ⊥
  cut6474  adequate = bad6474  (Adequate.valid adequate Two boolean env4)
  bad6475 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b0 b1) b0)) (bop b1 b0)) b1 → ⊥
  bad6475  p = false≢true (cong lower p)
  cut6475 : Adequate {ℓ} ((op (op (var 0) (op (op (var 1) (var 2)) (var 0))) (op (var 2) (var 1))) , (var 2)) → ⊥
  cut6475  adequate = bad6475  (Adequate.valid adequate Two boolean env1)
  bad6476 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b0 b0) b0)) (bop b0 b0)) b1 → ⊥
  bad6476  p = false≢true (cong lower p)
  cut6476 : Adequate {ℓ} ((op (op (var 0) (op (op (var 1) (var 2)) (var 0))) (op (var 2) (var 1))) , (var 3)) → ⊥
  cut6476  adequate = bad6476  (Adequate.valid adequate Two boolean env5)
  bad6477 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b0 b1) b0)) (bop b1 b1)) b0 → ⊥
  bad6477  p = false≢true (sym (cong lower p))
  cut6477 : Adequate {ℓ} ((op (op (var 0) (op (op (var 1) (var 2)) (var 0))) (op (var 2) (var 2))) , (var 0)) → ⊥
  cut6477  adequate = bad6477  (Adequate.valid adequate Two boolean env1)
  bad6478 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b0 b1) b0)) (bop b1 b1)) b0 → ⊥
  bad6478  p = false≢true (sym (cong lower p))
  cut6478 : Adequate {ℓ} ((op (op (var 0) (op (op (var 1) (var 2)) (var 0))) (op (var 2) (var 2))) , (var 1)) → ⊥
  cut6478  adequate = bad6478  (Adequate.valid adequate Two boolean env1)
  holds6479 : (z0 z1 z2 : A3) → (mul3 (mul3 z0 (mul3 (mul3 z1 z2) z0)) (mul3 z2 z2)) ≡ z2
  holds6479 z0 z1 z2 = refl
  cut6479 : Adequate {ℓ} ((op (op (var 0) (op (op (var 1) (var 2)) (var 0))) (op (var 2) (var 2))) , (var 2)) → ⊥
  cut6479  = reject3 ((op (op (var 0) (op (op (var 1) (var 2)) (var 0))) (op (var 2) (var 2))) , (var 2)) (λ env → holds6479 (env 0) (env 1) (env 2))
  bad6480 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b0 b0) b0)) (bop b0 b0)) b1 → ⊥
  bad6480  p = false≢true (cong lower p)
  cut6480 : Adequate {ℓ} ((op (op (var 0) (op (op (var 1) (var 2)) (var 0))) (op (var 2) (var 2))) , (var 3)) → ⊥
  cut6480  adequate = bad6480  (Adequate.valid adequate Two boolean env5)
  bad6481 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b0 b1) b0)) (bop b1 b1)) b0 → ⊥
  bad6481  p = false≢true (sym (cong lower p))
  cut6481 : Adequate {ℓ} ((op (op (var 0) (op (op (var 1) (var 2)) (var 0))) (op (var 2) (var 3))) , (var 0)) → ⊥
  cut6481  adequate = bad6481  (Adequate.valid adequate Two boolean env7)
  bad6482 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b0 b1) b0)) (bop b1 b1)) b0 → ⊥
  bad6482  p = false≢true (sym (cong lower p))
  cut6482 : Adequate {ℓ} ((op (op (var 0) (op (op (var 1) (var 2)) (var 0))) (op (var 2) (var 3))) , (var 1)) → ⊥
  cut6482  adequate = bad6482  (Adequate.valid adequate Two boolean env7)
  bad6483 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b0 b1) b0)) (bop b1 b0)) b1 → ⊥
  bad6483  p = false≢true (cong lower p)
  cut6483 : Adequate {ℓ} ((op (op (var 0) (op (op (var 1) (var 2)) (var 0))) (op (var 2) (var 3))) , (var 2)) → ⊥
  cut6483  adequate = bad6483  (Adequate.valid adequate Two boolean env8)
  bad6484 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b0 b0) b0)) (bop b0 b1)) b1 → ⊥
  bad6484  p = false≢true (cong lower p)
  cut6484 : Adequate {ℓ} ((op (op (var 0) (op (op (var 1) (var 2)) (var 0))) (op (var 2) (var 3))) , (var 3)) → ⊥
  cut6484  adequate = bad6484  (Adequate.valid adequate Two boolean env5)
  bad6485 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b0 b0) b0)) (bop b0 b0)) b1 → ⊥
  bad6485  p = false≢true (cong lower p)
  cut6485 : Adequate {ℓ} ((op (op (var 0) (op (op (var 1) (var 2)) (var 0))) (op (var 2) (var 3))) , (var 4)) → ⊥
  cut6485  adequate = bad6485  (Adequate.valid adequate Two boolean env9)
  bad6486 : PathP (λ _ → Two) (bop (bop b1 (bop (bop b0 b0) b1)) (bop b0 b1)) b1 → ⊥
  bad6486  p = false≢true (cong lower p)
  cut6486 : Adequate {ℓ} ((op (op (var 0) (op (op (var 1) (var 2)) (var 0))) (op (var 3) (var 0))) , (var 0)) → ⊥
  cut6486  adequate = bad6486  (Adequate.valid adequate Two boolean env15)
  bad6487 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b1 b0) b0)) (bop b0 b0)) b1 → ⊥
  bad6487  p = false≢true (cong lower p)
  cut6487 : Adequate {ℓ} ((op (op (var 0) (op (op (var 1) (var 2)) (var 0))) (op (var 3) (var 0))) , (var 1)) → ⊥
  cut6487  adequate = bad6487  (Adequate.valid adequate Two boolean env13)
  bad6488 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b0 b1) b0)) (bop b0 b0)) b1 → ⊥
  bad6488  p = false≢true (cong lower p)
  cut6488 : Adequate {ℓ} ((op (op (var 0) (op (op (var 1) (var 2)) (var 0))) (op (var 3) (var 0))) , (var 2)) → ⊥
  cut6488  adequate = bad6488  (Adequate.valid adequate Two boolean env8)
  bad6489 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b0 b0) b0)) (bop b1 b0)) b1 → ⊥
  bad6489  p = false≢true (cong lower p)
  cut6489 : Adequate {ℓ} ((op (op (var 0) (op (op (var 1) (var 2)) (var 0))) (op (var 3) (var 0))) , (var 3)) → ⊥
  cut6489  adequate = bad6489  (Adequate.valid adequate Two boolean env5)
  bad6490 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b0 b0) b0)) (bop b0 b0)) b1 → ⊥
  bad6490  p = false≢true (cong lower p)
  cut6490 : Adequate {ℓ} ((op (op (var 0) (op (op (var 1) (var 2)) (var 0))) (op (var 3) (var 0))) , (var 4)) → ⊥
  cut6490  adequate = bad6490  (Adequate.valid adequate Two boolean env9)
  bad6491 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b1 b0) b0)) (bop b1 b1)) b0 → ⊥
  bad6491  p = false≢true (sym (cong lower p))
  cut6491 : Adequate {ℓ} ((op (op (var 0) (op (op (var 1) (var 2)) (var 0))) (op (var 3) (var 1))) , (var 0)) → ⊥
  cut6491  adequate = bad6491  (Adequate.valid adequate Two boolean env14)
  bad6492 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b1 b0) b0)) (bop b0 b1)) b1 → ⊥
  bad6492  p = false≢true (cong lower p)
  cut6492 : Adequate {ℓ} ((op (op (var 0) (op (op (var 1) (var 2)) (var 0))) (op (var 3) (var 1))) , (var 1)) → ⊥
  cut6492  adequate = bad6492  (Adequate.valid adequate Two boolean env13)
  bad6493 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b0 b1) b0)) (bop b0 b0)) b1 → ⊥
  bad6493  p = false≢true (cong lower p)
  cut6493 : Adequate {ℓ} ((op (op (var 0) (op (op (var 1) (var 2)) (var 0))) (op (var 3) (var 1))) , (var 2)) → ⊥
  cut6493  adequate = bad6493  (Adequate.valid adequate Two boolean env8)
  bad6494 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b0 b0) b0)) (bop b1 b0)) b1 → ⊥
  bad6494  p = false≢true (cong lower p)
  cut6494 : Adequate {ℓ} ((op (op (var 0) (op (op (var 1) (var 2)) (var 0))) (op (var 3) (var 1))) , (var 3)) → ⊥
  cut6494  adequate = bad6494  (Adequate.valid adequate Two boolean env5)
  bad6495 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b0 b0) b0)) (bop b0 b0)) b1 → ⊥
  bad6495  p = false≢true (cong lower p)
  cut6495 : Adequate {ℓ} ((op (op (var 0) (op (op (var 1) (var 2)) (var 0))) (op (var 3) (var 1))) , (var 4)) → ⊥
  cut6495  adequate = bad6495  (Adequate.valid adequate Two boolean env9)
  bad6496 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b0 b1) b0)) (bop b1 b1)) b0 → ⊥
  bad6496  p = false≢true (sym (cong lower p))
  cut6496 : Adequate {ℓ} ((op (op (var 0) (op (op (var 1) (var 2)) (var 0))) (op (var 3) (var 2))) , (var 0)) → ⊥
  cut6496  adequate = bad6496  (Adequate.valid adequate Two boolean env7)
  bad6497 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b0 b1) b0)) (bop b1 b1)) b0 → ⊥
  bad6497  p = false≢true (sym (cong lower p))
  cut6497 : Adequate {ℓ} ((op (op (var 0) (op (op (var 1) (var 2)) (var 0))) (op (var 3) (var 2))) , (var 1)) → ⊥
  cut6497  adequate = bad6497  (Adequate.valid adequate Two boolean env7)
  bad6498 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b0 b1) b0)) (bop b0 b1)) b1 → ⊥
  bad6498  p = false≢true (cong lower p)
  cut6498 : Adequate {ℓ} ((op (op (var 0) (op (op (var 1) (var 2)) (var 0))) (op (var 3) (var 2))) , (var 2)) → ⊥
  cut6498  adequate = bad6498  (Adequate.valid adequate Two boolean env8)
  bad6499 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b0 b0) b0)) (bop b1 b0)) b1 → ⊥
  bad6499  p = false≢true (cong lower p)
  cut6499 : Adequate {ℓ} ((op (op (var 0) (op (op (var 1) (var 2)) (var 0))) (op (var 3) (var 2))) , (var 3)) → ⊥
  cut6499  adequate = bad6499  (Adequate.valid adequate Two boolean env5)
  bad6500 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b0 b0) b0)) (bop b0 b0)) b1 → ⊥
  bad6500  p = false≢true (cong lower p)
  cut6500 : Adequate {ℓ} ((op (op (var 0) (op (op (var 1) (var 2)) (var 0))) (op (var 3) (var 2))) , (var 4)) → ⊥
  cut6500  adequate = bad6500  (Adequate.valid adequate Two boolean env9)
  bad6501 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b0 b0) b0)) (bop b1 b1)) b0 → ⊥
  bad6501  p = false≢true (sym (cong lower p))
  cut6501 : Adequate {ℓ} ((op (op (var 0) (op (op (var 1) (var 2)) (var 0))) (op (var 3) (var 3))) , (var 0)) → ⊥
  cut6501  adequate = bad6501  (Adequate.valid adequate Two boolean env5)
  bad6502 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b0 b0) b0)) (bop b1 b1)) b0 → ⊥
  bad6502  p = false≢true (sym (cong lower p))
  cut6502 : Adequate {ℓ} ((op (op (var 0) (op (op (var 1) (var 2)) (var 0))) (op (var 3) (var 3))) , (var 1)) → ⊥
  cut6502  adequate = bad6502  (Adequate.valid adequate Two boolean env5)
  bad6503 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b0 b0) b0)) (bop b1 b1)) b0 → ⊥
  bad6503  p = false≢true (sym (cong lower p))
  cut6503 : Adequate {ℓ} ((op (op (var 0) (op (op (var 1) (var 2)) (var 0))) (op (var 3) (var 3))) , (var 2)) → ⊥
  cut6503  adequate = bad6503  (Adequate.valid adequate Two boolean env5)
  env19 : ℕ → Two
  env19 zero = b1
  env19 (suc zero) = b1
  env19 (suc (suc zero)) = b1
  env19 (suc (suc (suc zero))) = b0
  env19 (suc (suc (suc (suc rest)))) = b0
  bad6504 : PathP (λ _ → Two) (bop (bop b1 (bop (bop b1 b1) b1)) (bop b0 b0)) b0 → ⊥
  bad6504  p = false≢true (sym (cong lower p))
  cut6504 : Adequate {ℓ} ((op (op (var 0) (op (op (var 1) (var 2)) (var 0))) (op (var 3) (var 3))) , (var 3)) → ⊥
  cut6504  adequate = bad6504  (Adequate.valid adequate Two boolean env19)
  bad6505 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b0 b0) b0)) (bop b0 b0)) b1 → ⊥
  bad6505  p = false≢true (cong lower p)
  cut6505 : Adequate {ℓ} ((op (op (var 0) (op (op (var 1) (var 2)) (var 0))) (op (var 3) (var 3))) , (var 4)) → ⊥
  cut6505  adequate = bad6505  (Adequate.valid adequate Two boolean env9)
  bad6506 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b0 b0) b0)) (bop b1 b1)) b0 → ⊥
  bad6506  p = false≢true (sym (cong lower p))
  cut6506 : Adequate {ℓ} ((op (op (var 0) (op (op (var 1) (var 2)) (var 0))) (op (var 3) (var 4))) , (var 0)) → ⊥
  cut6506  adequate = bad6506  (Adequate.valid adequate Two boolean env16)
  bad6507 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b0 b0) b0)) (bop b1 b1)) b0 → ⊥
  bad6507  p = false≢true (sym (cong lower p))
  cut6507 : Adequate {ℓ} ((op (op (var 0) (op (op (var 1) (var 2)) (var 0))) (op (var 3) (var 4))) , (var 1)) → ⊥
  cut6507  adequate = bad6507  (Adequate.valid adequate Two boolean env16)
  bad6508 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b0 b0) b0)) (bop b1 b1)) b0 → ⊥
  bad6508  p = false≢true (sym (cong lower p))
  cut6508 : Adequate {ℓ} ((op (op (var 0) (op (op (var 1) (var 2)) (var 0))) (op (var 3) (var 4))) , (var 2)) → ⊥
  cut6508  adequate = bad6508  (Adequate.valid adequate Two boolean env16)
  bad6509 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b0 b0) b0)) (bop b1 b0)) b1 → ⊥
  bad6509  p = false≢true (cong lower p)
  cut6509 : Adequate {ℓ} ((op (op (var 0) (op (op (var 1) (var 2)) (var 0))) (op (var 3) (var 4))) , (var 3)) → ⊥
  cut6509  adequate = bad6509  (Adequate.valid adequate Two boolean env17)
  bad6510 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b0 b0) b0)) (bop b0 b1)) b1 → ⊥
  bad6510  p = false≢true (cong lower p)
  cut6510 : Adequate {ℓ} ((op (op (var 0) (op (op (var 1) (var 2)) (var 0))) (op (var 3) (var 4))) , (var 4)) → ⊥
  cut6510  adequate = bad6510  (Adequate.valid adequate Two boolean env9)
  bad6511 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b0 b0) b0)) (bop b0 b0)) b1 → ⊥
  bad6511  p = false≢true (cong lower p)
  cut6511 : Adequate {ℓ} ((op (op (var 0) (op (op (var 1) (var 2)) (var 0))) (op (var 3) (var 4))) , (var 5)) → ⊥
  cut6511  adequate = bad6511  (Adequate.valid adequate Two boolean env18)
  holds6512 : (z0 z1 z2 : A2) → (mul2 (mul2 z0 (mul2 (mul2 z1 z2) z1)) (mul2 z0 z0)) ≡ z0
  holds6512 z0 z1 z2 = refl
  cut6512 : Adequate {ℓ} ((op (op (var 0) (op (op (var 1) (var 2)) (var 1))) (op (var 0) (var 0))) , (var 0)) → ⊥
  cut6512  = reject2 ((op (op (var 0) (op (op (var 1) (var 2)) (var 1))) (op (var 0) (var 0))) , (var 0)) (λ env → holds6512 (env 0) (env 1) (env 2))
  bad6513 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b1 b0) b1)) (bop b0 b0)) b1 → ⊥
  bad6513  p = false≢true (cong lower p)
  cut6513 : Adequate {ℓ} ((op (op (var 0) (op (op (var 1) (var 2)) (var 1))) (op (var 0) (var 0))) , (var 1)) → ⊥
  cut6513  adequate = bad6513  (Adequate.valid adequate Two boolean env4)
  bad6514 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b0 b1) b0)) (bop b0 b0)) b1 → ⊥
  bad6514  p = false≢true (cong lower p)
  cut6514 : Adequate {ℓ} ((op (op (var 0) (op (op (var 1) (var 2)) (var 1))) (op (var 0) (var 0))) , (var 2)) → ⊥
  cut6514  adequate = bad6514  (Adequate.valid adequate Two boolean env1)
  bad6515 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b0 b0) b0)) (bop b0 b0)) b1 → ⊥
  bad6515  p = false≢true (cong lower p)
  cut6515 : Adequate {ℓ} ((op (op (var 0) (op (op (var 1) (var 2)) (var 1))) (op (var 0) (var 0))) , (var 3)) → ⊥
  cut6515  adequate = bad6515  (Adequate.valid adequate Two boolean env5)
  holds6516 : (z0 z1 z2 : A2) → (mul2 (mul2 z0 (mul2 (mul2 z1 z2) z1)) (mul2 z0 z1)) ≡ z0
  holds6516 z0 z1 z2 = refl
  cut6516 : Adequate {ℓ} ((op (op (var 0) (op (op (var 1) (var 2)) (var 1))) (op (var 0) (var 1))) , (var 0)) → ⊥
  cut6516  = reject2 ((op (op (var 0) (op (op (var 1) (var 2)) (var 1))) (op (var 0) (var 1))) , (var 0)) (λ env → holds6516 (env 0) (env 1) (env 2))
  bad6517 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b1 b0) b1)) (bop b0 b1)) b1 → ⊥
  bad6517  p = false≢true (cong lower p)
  cut6517 : Adequate {ℓ} ((op (op (var 0) (op (op (var 1) (var 2)) (var 1))) (op (var 0) (var 1))) , (var 1)) → ⊥
  cut6517  adequate = bad6517  (Adequate.valid adequate Two boolean env4)
  bad6518 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b0 b1) b0)) (bop b0 b0)) b1 → ⊥
  bad6518  p = false≢true (cong lower p)
  cut6518 : Adequate {ℓ} ((op (op (var 0) (op (op (var 1) (var 2)) (var 1))) (op (var 0) (var 1))) , (var 2)) → ⊥
  cut6518  adequate = bad6518  (Adequate.valid adequate Two boolean env1)
  bad6519 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b0 b0) b0)) (bop b0 b0)) b1 → ⊥
  bad6519  p = false≢true (cong lower p)
  cut6519 : Adequate {ℓ} ((op (op (var 0) (op (op (var 1) (var 2)) (var 1))) (op (var 0) (var 1))) , (var 3)) → ⊥
  cut6519  adequate = bad6519  (Adequate.valid adequate Two boolean env5)
  bad6520 : PathP (λ _ → Two) (bop (bop b1 (bop (bop b1 b0) b1)) (bop b1 b0)) b1 → ⊥
  bad6520  p = false≢true (cong lower p)
  cut6520 : Adequate {ℓ} ((op (op (var 0) (op (op (var 1) (var 2)) (var 1))) (op (var 0) (var 2))) , (var 0)) → ⊥
  cut6520  adequate = bad6520  (Adequate.valid adequate Two boolean env10)
  bad6521 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b1 b0) b1)) (bop b0 b0)) b1 → ⊥
  bad6521  p = false≢true (cong lower p)
  cut6521 : Adequate {ℓ} ((op (op (var 0) (op (op (var 1) (var 2)) (var 1))) (op (var 0) (var 2))) , (var 1)) → ⊥
  cut6521  adequate = bad6521  (Adequate.valid adequate Two boolean env4)
  bad6522 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b0 b1) b0)) (bop b0 b1)) b1 → ⊥
  bad6522  p = false≢true (cong lower p)
  cut6522 : Adequate {ℓ} ((op (op (var 0) (op (op (var 1) (var 2)) (var 1))) (op (var 0) (var 2))) , (var 2)) → ⊥
  cut6522  adequate = bad6522  (Adequate.valid adequate Two boolean env1)
  bad6523 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b0 b0) b0)) (bop b0 b0)) b1 → ⊥
  bad6523  p = false≢true (cong lower p)
  cut6523 : Adequate {ℓ} ((op (op (var 0) (op (op (var 1) (var 2)) (var 1))) (op (var 0) (var 2))) , (var 3)) → ⊥
  cut6523  adequate = bad6523  (Adequate.valid adequate Two boolean env5)
  env20 : ℕ → Two
  env20 zero = b1
  env20 (suc zero) = b1
  env20 (suc (suc zero)) = b0
  env20 (suc (suc (suc zero))) = b0
  env20 (suc (suc (suc (suc rest)))) = b0
  bad6524 : PathP (λ _ → Two) (bop (bop b1 (bop (bop b1 b0) b1)) (bop b1 b0)) b1 → ⊥
  bad6524  p = false≢true (cong lower p)
  cut6524 : Adequate {ℓ} ((op (op (var 0) (op (op (var 1) (var 2)) (var 1))) (op (var 0) (var 3))) , (var 0)) → ⊥
  cut6524  adequate = bad6524  (Adequate.valid adequate Two boolean env20)
  bad6525 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b1 b0) b1)) (bop b0 b0)) b1 → ⊥
  bad6525  p = false≢true (cong lower p)
  cut6525 : Adequate {ℓ} ((op (op (var 0) (op (op (var 1) (var 2)) (var 1))) (op (var 0) (var 3))) , (var 1)) → ⊥
  cut6525  adequate = bad6525  (Adequate.valid adequate Two boolean env13)
  bad6526 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b0 b1) b0)) (bop b0 b0)) b1 → ⊥
  bad6526  p = false≢true (cong lower p)
  cut6526 : Adequate {ℓ} ((op (op (var 0) (op (op (var 1) (var 2)) (var 1))) (op (var 0) (var 3))) , (var 2)) → ⊥
  cut6526  adequate = bad6526  (Adequate.valid adequate Two boolean env8)
  bad6527 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b0 b0) b0)) (bop b0 b1)) b1 → ⊥
  bad6527  p = false≢true (cong lower p)
  cut6527 : Adequate {ℓ} ((op (op (var 0) (op (op (var 1) (var 2)) (var 1))) (op (var 0) (var 3))) , (var 3)) → ⊥
  cut6527  adequate = bad6527  (Adequate.valid adequate Two boolean env5)
  bad6528 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b0 b0) b0)) (bop b0 b0)) b1 → ⊥
  bad6528  p = false≢true (cong lower p)
  cut6528 : Adequate {ℓ} ((op (op (var 0) (op (op (var 1) (var 2)) (var 1))) (op (var 0) (var 3))) , (var 4)) → ⊥
  cut6528  adequate = bad6528  (Adequate.valid adequate Two boolean env9)
  holds6529 : (z0 z1 z2 : A2) → (mul2 (mul2 z0 (mul2 (mul2 z1 z2) z1)) (mul2 z1 z0)) ≡ z0
  holds6529 z0 z1 z2 = refl
  cut6529 : Adequate {ℓ} ((op (op (var 0) (op (op (var 1) (var 2)) (var 1))) (op (var 1) (var 0))) , (var 0)) → ⊥
  cut6529  = reject2 ((op (op (var 0) (op (op (var 1) (var 2)) (var 1))) (op (var 1) (var 0))) , (var 0)) (λ env → holds6529 (env 0) (env 1) (env 2))
  bad6530 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b1 b0) b1)) (bop b1 b0)) b1 → ⊥
  bad6530  p = false≢true (cong lower p)
  cut6530 : Adequate {ℓ} ((op (op (var 0) (op (op (var 1) (var 2)) (var 1))) (op (var 1) (var 0))) , (var 1)) → ⊥
  cut6530  adequate = bad6530  (Adequate.valid adequate Two boolean env4)
  bad6531 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b0 b1) b0)) (bop b0 b0)) b1 → ⊥
  bad6531  p = false≢true (cong lower p)
  cut6531 : Adequate {ℓ} ((op (op (var 0) (op (op (var 1) (var 2)) (var 1))) (op (var 1) (var 0))) , (var 2)) → ⊥
  cut6531  adequate = bad6531  (Adequate.valid adequate Two boolean env1)
  bad6532 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b0 b0) b0)) (bop b0 b0)) b1 → ⊥
  bad6532  p = false≢true (cong lower p)
  cut6532 : Adequate {ℓ} ((op (op (var 0) (op (op (var 1) (var 2)) (var 1))) (op (var 1) (var 0))) , (var 3)) → ⊥
  cut6532  adequate = bad6532  (Adequate.valid adequate Two boolean env5)
  bad6533 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b1 b0) b1)) (bop b1 b1)) b0 → ⊥
  bad6533  p = false≢true (sym (cong lower p))
  cut6533 : Adequate {ℓ} ((op (op (var 0) (op (op (var 1) (var 2)) (var 1))) (op (var 1) (var 1))) , (var 0)) → ⊥
  cut6533  adequate = bad6533  (Adequate.valid adequate Two boolean env4)
  bad6534 : PathP (λ _ → Two) (bop (bop b1 (bop (bop b0 b0) b0)) (bop b0 b0)) b0 → ⊥
  bad6534  p = false≢true (sym (cong lower p))
  cut6534 : Adequate {ℓ} ((op (op (var 0) (op (op (var 1) (var 2)) (var 1))) (op (var 1) (var 1))) , (var 1)) → ⊥
  cut6534  adequate = bad6534  (Adequate.valid adequate Two boolean env6)
  bad6535 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b0 b1) b0)) (bop b0 b0)) b1 → ⊥
  bad6535  p = false≢true (cong lower p)
  cut6535 : Adequate {ℓ} ((op (op (var 0) (op (op (var 1) (var 2)) (var 1))) (op (var 1) (var 1))) , (var 2)) → ⊥
  cut6535  adequate = bad6535  (Adequate.valid adequate Two boolean env1)
  bad6536 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b0 b0) b0)) (bop b0 b0)) b1 → ⊥
  bad6536  p = false≢true (cong lower p)
  cut6536 : Adequate {ℓ} ((op (op (var 0) (op (op (var 1) (var 2)) (var 1))) (op (var 1) (var 1))) , (var 3)) → ⊥
  cut6536  adequate = bad6536  (Adequate.valid adequate Two boolean env5)
  bad6537 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b1 b1) b1)) (bop b1 b1)) b0 → ⊥
  bad6537  p = false≢true (sym (cong lower p))
  cut6537 : Adequate {ℓ} ((op (op (var 0) (op (op (var 1) (var 2)) (var 1))) (op (var 1) (var 2))) , (var 0)) → ⊥
  cut6537  adequate = bad6537  (Adequate.valid adequate Two boolean env3)
  bad6538 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b1 b0) b1)) (bop b1 b0)) b1 → ⊥
  bad6538  p = false≢true (cong lower p)
  cut6538 : Adequate {ℓ} ((op (op (var 0) (op (op (var 1) (var 2)) (var 1))) (op (var 1) (var 2))) , (var 1)) → ⊥
  cut6538  adequate = bad6538  (Adequate.valid adequate Two boolean env4)
  bad6539 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b0 b1) b0)) (bop b0 b1)) b1 → ⊥
  bad6539  p = false≢true (cong lower p)
  cut6539 : Adequate {ℓ} ((op (op (var 0) (op (op (var 1) (var 2)) (var 1))) (op (var 1) (var 2))) , (var 2)) → ⊥
  cut6539  adequate = bad6539  (Adequate.valid adequate Two boolean env1)
  bad6540 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b0 b0) b0)) (bop b0 b0)) b1 → ⊥
  bad6540  p = false≢true (cong lower p)
  cut6540 : Adequate {ℓ} ((op (op (var 0) (op (op (var 1) (var 2)) (var 1))) (op (var 1) (var 2))) , (var 3)) → ⊥
  cut6540  adequate = bad6540  (Adequate.valid adequate Two boolean env5)
  bad6541 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b1 b0) b1)) (bop b1 b1)) b0 → ⊥
  bad6541  p = false≢true (sym (cong lower p))
  cut6541 : Adequate {ℓ} ((op (op (var 0) (op (op (var 1) (var 2)) (var 1))) (op (var 1) (var 3))) , (var 0)) → ⊥
  cut6541  adequate = bad6541  (Adequate.valid adequate Two boolean env14)
  bad6542 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b1 b0) b1)) (bop b1 b0)) b1 → ⊥
  bad6542  p = false≢true (cong lower p)
  cut6542 : Adequate {ℓ} ((op (op (var 0) (op (op (var 1) (var 2)) (var 1))) (op (var 1) (var 3))) , (var 1)) → ⊥
  cut6542  adequate = bad6542  (Adequate.valid adequate Two boolean env13)
  bad6543 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b0 b1) b0)) (bop b0 b0)) b1 → ⊥
  bad6543  p = false≢true (cong lower p)
  cut6543 : Adequate {ℓ} ((op (op (var 0) (op (op (var 1) (var 2)) (var 1))) (op (var 1) (var 3))) , (var 2)) → ⊥
  cut6543  adequate = bad6543  (Adequate.valid adequate Two boolean env8)
  bad6544 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b0 b0) b0)) (bop b0 b1)) b1 → ⊥
  bad6544  p = false≢true (cong lower p)
  cut6544 : Adequate {ℓ} ((op (op (var 0) (op (op (var 1) (var 2)) (var 1))) (op (var 1) (var 3))) , (var 3)) → ⊥
  cut6544  adequate = bad6544  (Adequate.valid adequate Two boolean env5)
  bad6545 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b0 b0) b0)) (bop b0 b0)) b1 → ⊥
  bad6545  p = false≢true (cong lower p)
  cut6545 : Adequate {ℓ} ((op (op (var 0) (op (op (var 1) (var 2)) (var 1))) (op (var 1) (var 3))) , (var 4)) → ⊥
  cut6545  adequate = bad6545  (Adequate.valid adequate Two boolean env9)
  bad6546 : PathP (λ _ → Two) (bop (bop b1 (bop (bop b1 b0) b1)) (bop b0 b1)) b1 → ⊥
  bad6546  p = false≢true (cong lower p)
  cut6546 : Adequate {ℓ} ((op (op (var 0) (op (op (var 1) (var 2)) (var 1))) (op (var 2) (var 0))) , (var 0)) → ⊥
  cut6546  adequate = bad6546  (Adequate.valid adequate Two boolean env10)
  bad6547 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b1 b0) b1)) (bop b0 b0)) b1 → ⊥
  bad6547  p = false≢true (cong lower p)
  cut6547 : Adequate {ℓ} ((op (op (var 0) (op (op (var 1) (var 2)) (var 1))) (op (var 2) (var 0))) , (var 1)) → ⊥
  cut6547  adequate = bad6547  (Adequate.valid adequate Two boolean env4)
  bad6548 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b0 b1) b0)) (bop b1 b0)) b1 → ⊥
  bad6548  p = false≢true (cong lower p)
  cut6548 : Adequate {ℓ} ((op (op (var 0) (op (op (var 1) (var 2)) (var 1))) (op (var 2) (var 0))) , (var 2)) → ⊥
  cut6548  adequate = bad6548  (Adequate.valid adequate Two boolean env1)
  bad6549 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b0 b0) b0)) (bop b0 b0)) b1 → ⊥
  bad6549  p = false≢true (cong lower p)
  cut6549 : Adequate {ℓ} ((op (op (var 0) (op (op (var 1) (var 2)) (var 1))) (op (var 2) (var 0))) , (var 3)) → ⊥
  cut6549  adequate = bad6549  (Adequate.valid adequate Two boolean env5)
  bad6550 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b1 b1) b1)) (bop b1 b1)) b0 → ⊥
  bad6550  p = false≢true (sym (cong lower p))
  cut6550 : Adequate {ℓ} ((op (op (var 0) (op (op (var 1) (var 2)) (var 1))) (op (var 2) (var 1))) , (var 0)) → ⊥
  cut6550  adequate = bad6550  (Adequate.valid adequate Two boolean env3)
  bad6551 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b1 b0) b1)) (bop b0 b1)) b1 → ⊥
  bad6551  p = false≢true (cong lower p)
  cut6551 : Adequate {ℓ} ((op (op (var 0) (op (op (var 1) (var 2)) (var 1))) (op (var 2) (var 1))) , (var 1)) → ⊥
  cut6551  adequate = bad6551  (Adequate.valid adequate Two boolean env4)
  bad6552 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b0 b1) b0)) (bop b1 b0)) b1 → ⊥
  bad6552  p = false≢true (cong lower p)
  cut6552 : Adequate {ℓ} ((op (op (var 0) (op (op (var 1) (var 2)) (var 1))) (op (var 2) (var 1))) , (var 2)) → ⊥
  cut6552  adequate = bad6552  (Adequate.valid adequate Two boolean env1)
  bad6553 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b0 b0) b0)) (bop b0 b0)) b1 → ⊥
  bad6553  p = false≢true (cong lower p)
  cut6553 : Adequate {ℓ} ((op (op (var 0) (op (op (var 1) (var 2)) (var 1))) (op (var 2) (var 1))) , (var 3)) → ⊥
  cut6553  adequate = bad6553  (Adequate.valid adequate Two boolean env5)
  bad6554 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b0 b1) b0)) (bop b1 b1)) b0 → ⊥
  bad6554  p = false≢true (sym (cong lower p))
  cut6554 : Adequate {ℓ} ((op (op (var 0) (op (op (var 1) (var 2)) (var 1))) (op (var 2) (var 2))) , (var 0)) → ⊥
  cut6554  adequate = bad6554  (Adequate.valid adequate Two boolean env1)
  bad6555 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b0 b1) b0)) (bop b1 b1)) b0 → ⊥
  bad6555  p = false≢true (sym (cong lower p))
  cut6555 : Adequate {ℓ} ((op (op (var 0) (op (op (var 1) (var 2)) (var 1))) (op (var 2) (var 2))) , (var 1)) → ⊥
  cut6555  adequate = bad6555  (Adequate.valid adequate Two boolean env1)
  bad6556 : PathP (λ _ → Two) (bop (bop b1 (bop (bop b0 b0) b0)) (bop b0 b0)) b0 → ⊥
  bad6556  p = false≢true (sym (cong lower p))
  cut6556 : Adequate {ℓ} ((op (op (var 0) (op (op (var 1) (var 2)) (var 1))) (op (var 2) (var 2))) , (var 2)) → ⊥
  cut6556  adequate = bad6556  (Adequate.valid adequate Two boolean env6)
  bad6557 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b0 b0) b0)) (bop b0 b0)) b1 → ⊥
  bad6557  p = false≢true (cong lower p)
  cut6557 : Adequate {ℓ} ((op (op (var 0) (op (op (var 1) (var 2)) (var 1))) (op (var 2) (var 2))) , (var 3)) → ⊥
  cut6557  adequate = bad6557  (Adequate.valid adequate Two boolean env5)
  bad6558 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b0 b1) b0)) (bop b1 b1)) b0 → ⊥
  bad6558  p = false≢true (sym (cong lower p))
  cut6558 : Adequate {ℓ} ((op (op (var 0) (op (op (var 1) (var 2)) (var 1))) (op (var 2) (var 3))) , (var 0)) → ⊥
  cut6558  adequate = bad6558  (Adequate.valid adequate Two boolean env7)
  bad6559 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b0 b1) b0)) (bop b1 b1)) b0 → ⊥
  bad6559  p = false≢true (sym (cong lower p))
  cut6559 : Adequate {ℓ} ((op (op (var 0) (op (op (var 1) (var 2)) (var 1))) (op (var 2) (var 3))) , (var 1)) → ⊥
  cut6559  adequate = bad6559  (Adequate.valid adequate Two boolean env7)
  bad6560 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b0 b1) b0)) (bop b1 b0)) b1 → ⊥
  bad6560  p = false≢true (cong lower p)
  cut6560 : Adequate {ℓ} ((op (op (var 0) (op (op (var 1) (var 2)) (var 1))) (op (var 2) (var 3))) , (var 2)) → ⊥
  cut6560  adequate = bad6560  (Adequate.valid adequate Two boolean env8)
  bad6561 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b0 b0) b0)) (bop b0 b1)) b1 → ⊥
  bad6561  p = false≢true (cong lower p)
  cut6561 : Adequate {ℓ} ((op (op (var 0) (op (op (var 1) (var 2)) (var 1))) (op (var 2) (var 3))) , (var 3)) → ⊥
  cut6561  adequate = bad6561  (Adequate.valid adequate Two boolean env5)
  bad6562 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b0 b0) b0)) (bop b0 b0)) b1 → ⊥
  bad6562  p = false≢true (cong lower p)
  cut6562 : Adequate {ℓ} ((op (op (var 0) (op (op (var 1) (var 2)) (var 1))) (op (var 2) (var 3))) , (var 4)) → ⊥
  cut6562  adequate = bad6562  (Adequate.valid adequate Two boolean env9)
  bad6563 : PathP (λ _ → Two) (bop (bop b1 (bop (bop b1 b0) b1)) (bop b0 b1)) b1 → ⊥
  bad6563  p = false≢true (cong lower p)
  cut6563 : Adequate {ℓ} ((op (op (var 0) (op (op (var 1) (var 2)) (var 1))) (op (var 3) (var 0))) , (var 0)) → ⊥
  cut6563  adequate = bad6563  (Adequate.valid adequate Two boolean env20)
  bad6564 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b1 b0) b1)) (bop b0 b0)) b1 → ⊥
  bad6564  p = false≢true (cong lower p)
  cut6564 : Adequate {ℓ} ((op (op (var 0) (op (op (var 1) (var 2)) (var 1))) (op (var 3) (var 0))) , (var 1)) → ⊥
  cut6564  adequate = bad6564  (Adequate.valid adequate Two boolean env13)
  bad6565 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b0 b1) b0)) (bop b0 b0)) b1 → ⊥
  bad6565  p = false≢true (cong lower p)
  cut6565 : Adequate {ℓ} ((op (op (var 0) (op (op (var 1) (var 2)) (var 1))) (op (var 3) (var 0))) , (var 2)) → ⊥
  cut6565  adequate = bad6565  (Adequate.valid adequate Two boolean env8)
  bad6566 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b0 b0) b0)) (bop b1 b0)) b1 → ⊥
  bad6566  p = false≢true (cong lower p)
  cut6566 : Adequate {ℓ} ((op (op (var 0) (op (op (var 1) (var 2)) (var 1))) (op (var 3) (var 0))) , (var 3)) → ⊥
  cut6566  adequate = bad6566  (Adequate.valid adequate Two boolean env5)
  bad6567 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b0 b0) b0)) (bop b0 b0)) b1 → ⊥
  bad6567  p = false≢true (cong lower p)
  cut6567 : Adequate {ℓ} ((op (op (var 0) (op (op (var 1) (var 2)) (var 1))) (op (var 3) (var 0))) , (var 4)) → ⊥
  cut6567  adequate = bad6567  (Adequate.valid adequate Two boolean env9)
  bad6568 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b1 b0) b1)) (bop b1 b1)) b0 → ⊥
  bad6568  p = false≢true (sym (cong lower p))
  cut6568 : Adequate {ℓ} ((op (op (var 0) (op (op (var 1) (var 2)) (var 1))) (op (var 3) (var 1))) , (var 0)) → ⊥
  cut6568  adequate = bad6568  (Adequate.valid adequate Two boolean env14)
  bad6569 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b1 b0) b1)) (bop b0 b1)) b1 → ⊥
  bad6569  p = false≢true (cong lower p)
  cut6569 : Adequate {ℓ} ((op (op (var 0) (op (op (var 1) (var 2)) (var 1))) (op (var 3) (var 1))) , (var 1)) → ⊥
  cut6569  adequate = bad6569  (Adequate.valid adequate Two boolean env13)
  bad6570 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b0 b1) b0)) (bop b0 b0)) b1 → ⊥
  bad6570  p = false≢true (cong lower p)
  cut6570 : Adequate {ℓ} ((op (op (var 0) (op (op (var 1) (var 2)) (var 1))) (op (var 3) (var 1))) , (var 2)) → ⊥
  cut6570  adequate = bad6570  (Adequate.valid adequate Two boolean env8)
  bad6571 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b0 b0) b0)) (bop b1 b0)) b1 → ⊥
  bad6571  p = false≢true (cong lower p)
  cut6571 : Adequate {ℓ} ((op (op (var 0) (op (op (var 1) (var 2)) (var 1))) (op (var 3) (var 1))) , (var 3)) → ⊥
  cut6571  adequate = bad6571  (Adequate.valid adequate Two boolean env5)
  bad6572 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b0 b0) b0)) (bop b0 b0)) b1 → ⊥
  bad6572  p = false≢true (cong lower p)
  cut6572 : Adequate {ℓ} ((op (op (var 0) (op (op (var 1) (var 2)) (var 1))) (op (var 3) (var 1))) , (var 4)) → ⊥
  cut6572  adequate = bad6572  (Adequate.valid adequate Two boolean env9)
  bad6573 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b0 b1) b0)) (bop b1 b1)) b0 → ⊥
  bad6573  p = false≢true (sym (cong lower p))
  cut6573 : Adequate {ℓ} ((op (op (var 0) (op (op (var 1) (var 2)) (var 1))) (op (var 3) (var 2))) , (var 0)) → ⊥
  cut6573  adequate = bad6573  (Adequate.valid adequate Two boolean env7)
  bad6574 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b0 b1) b0)) (bop b1 b1)) b0 → ⊥
  bad6574  p = false≢true (sym (cong lower p))
  cut6574 : Adequate {ℓ} ((op (op (var 0) (op (op (var 1) (var 2)) (var 1))) (op (var 3) (var 2))) , (var 1)) → ⊥
  cut6574  adequate = bad6574  (Adequate.valid adequate Two boolean env7)
  bad6575 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b0 b1) b0)) (bop b0 b1)) b1 → ⊥
  bad6575  p = false≢true (cong lower p)
  cut6575 : Adequate {ℓ} ((op (op (var 0) (op (op (var 1) (var 2)) (var 1))) (op (var 3) (var 2))) , (var 2)) → ⊥
  cut6575  adequate = bad6575  (Adequate.valid adequate Two boolean env8)
  bad6576 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b0 b0) b0)) (bop b1 b0)) b1 → ⊥
  bad6576  p = false≢true (cong lower p)
  cut6576 : Adequate {ℓ} ((op (op (var 0) (op (op (var 1) (var 2)) (var 1))) (op (var 3) (var 2))) , (var 3)) → ⊥
  cut6576  adequate = bad6576  (Adequate.valid adequate Two boolean env5)
  bad6577 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b0 b0) b0)) (bop b0 b0)) b1 → ⊥
  bad6577  p = false≢true (cong lower p)
  cut6577 : Adequate {ℓ} ((op (op (var 0) (op (op (var 1) (var 2)) (var 1))) (op (var 3) (var 2))) , (var 4)) → ⊥
  cut6577  adequate = bad6577  (Adequate.valid adequate Two boolean env9)
  bad6578 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b0 b0) b0)) (bop b1 b1)) b0 → ⊥
  bad6578  p = false≢true (sym (cong lower p))
  cut6578 : Adequate {ℓ} ((op (op (var 0) (op (op (var 1) (var 2)) (var 1))) (op (var 3) (var 3))) , (var 0)) → ⊥
  cut6578  adequate = bad6578  (Adequate.valid adequate Two boolean env5)
  bad6579 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b0 b0) b0)) (bop b1 b1)) b0 → ⊥
  bad6579  p = false≢true (sym (cong lower p))
  cut6579 : Adequate {ℓ} ((op (op (var 0) (op (op (var 1) (var 2)) (var 1))) (op (var 3) (var 3))) , (var 1)) → ⊥
  cut6579  adequate = bad6579  (Adequate.valid adequate Two boolean env5)
  bad6580 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b0 b0) b0)) (bop b1 b1)) b0 → ⊥
  bad6580  p = false≢true (sym (cong lower p))
  cut6580 : Adequate {ℓ} ((op (op (var 0) (op (op (var 1) (var 2)) (var 1))) (op (var 3) (var 3))) , (var 2)) → ⊥
  cut6580  adequate = bad6580  (Adequate.valid adequate Two boolean env5)
  bad6581 : PathP (λ _ → Two) (bop (bop b1 (bop (bop b0 b0) b0)) (bop b0 b0)) b0 → ⊥
  bad6581  p = false≢true (sym (cong lower p))
  cut6581 : Adequate {ℓ} ((op (op (var 0) (op (op (var 1) (var 2)) (var 1))) (op (var 3) (var 3))) , (var 3)) → ⊥
  cut6581  adequate = bad6581  (Adequate.valid adequate Two boolean env15)
  bad6582 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b0 b0) b0)) (bop b0 b0)) b1 → ⊥
  bad6582  p = false≢true (cong lower p)
  cut6582 : Adequate {ℓ} ((op (op (var 0) (op (op (var 1) (var 2)) (var 1))) (op (var 3) (var 3))) , (var 4)) → ⊥
  cut6582  adequate = bad6582  (Adequate.valid adequate Two boolean env9)
  bad6583 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b0 b0) b0)) (bop b1 b1)) b0 → ⊥
  bad6583  p = false≢true (sym (cong lower p))
  cut6583 : Adequate {ℓ} ((op (op (var 0) (op (op (var 1) (var 2)) (var 1))) (op (var 3) (var 4))) , (var 0)) → ⊥
  cut6583  adequate = bad6583  (Adequate.valid adequate Two boolean env16)
  bad6584 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b0 b0) b0)) (bop b1 b1)) b0 → ⊥
  bad6584  p = false≢true (sym (cong lower p))
  cut6584 : Adequate {ℓ} ((op (op (var 0) (op (op (var 1) (var 2)) (var 1))) (op (var 3) (var 4))) , (var 1)) → ⊥
  cut6584  adequate = bad6584  (Adequate.valid adequate Two boolean env16)
  bad6585 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b0 b0) b0)) (bop b1 b1)) b0 → ⊥
  bad6585  p = false≢true (sym (cong lower p))
  cut6585 : Adequate {ℓ} ((op (op (var 0) (op (op (var 1) (var 2)) (var 1))) (op (var 3) (var 4))) , (var 2)) → ⊥
  cut6585  adequate = bad6585  (Adequate.valid adequate Two boolean env16)
  bad6586 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b0 b0) b0)) (bop b1 b0)) b1 → ⊥
  bad6586  p = false≢true (cong lower p)
  cut6586 : Adequate {ℓ} ((op (op (var 0) (op (op (var 1) (var 2)) (var 1))) (op (var 3) (var 4))) , (var 3)) → ⊥
  cut6586  adequate = bad6586  (Adequate.valid adequate Two boolean env17)
  bad6587 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b0 b0) b0)) (bop b0 b1)) b1 → ⊥
  bad6587  p = false≢true (cong lower p)
  cut6587 : Adequate {ℓ} ((op (op (var 0) (op (op (var 1) (var 2)) (var 1))) (op (var 3) (var 4))) , (var 4)) → ⊥
  cut6587  adequate = bad6587  (Adequate.valid adequate Two boolean env9)
  bad6588 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b0 b0) b0)) (bop b0 b0)) b1 → ⊥
  bad6588  p = false≢true (cong lower p)
  cut6588 : Adequate {ℓ} ((op (op (var 0) (op (op (var 1) (var 2)) (var 1))) (op (var 3) (var 4))) , (var 5)) → ⊥
  cut6588  adequate = bad6588  (Adequate.valid adequate Two boolean env18)
  holds6589 : (z0 z1 z2 : A2) → (mul2 (mul2 z0 (mul2 (mul2 z1 z2) z2)) (mul2 z0 z0)) ≡ z0
  holds6589 z0 z1 z2 = refl
  cut6589 : Adequate {ℓ} ((op (op (var 0) (op (op (var 1) (var 2)) (var 2))) (op (var 0) (var 0))) , (var 0)) → ⊥
  cut6589  = reject2 ((op (op (var 0) (op (op (var 1) (var 2)) (var 2))) (op (var 0) (var 0))) , (var 0)) (λ env → holds6589 (env 0) (env 1) (env 2))
  bad6590 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b1 b0) b0)) (bop b0 b0)) b1 → ⊥
  bad6590  p = false≢true (cong lower p)
  cut6590 : Adequate {ℓ} ((op (op (var 0) (op (op (var 1) (var 2)) (var 2))) (op (var 0) (var 0))) , (var 1)) → ⊥
  cut6590  adequate = bad6590  (Adequate.valid adequate Two boolean env4)
  bad6591 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b0 b1) b1)) (bop b0 b0)) b1 → ⊥
  bad6591  p = false≢true (cong lower p)
  cut6591 : Adequate {ℓ} ((op (op (var 0) (op (op (var 1) (var 2)) (var 2))) (op (var 0) (var 0))) , (var 2)) → ⊥
  cut6591  adequate = bad6591  (Adequate.valid adequate Two boolean env1)
  bad6592 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b0 b0) b0)) (bop b0 b0)) b1 → ⊥
  bad6592  p = false≢true (cong lower p)
  cut6592 : Adequate {ℓ} ((op (op (var 0) (op (op (var 1) (var 2)) (var 2))) (op (var 0) (var 0))) , (var 3)) → ⊥
  cut6592  adequate = bad6592  (Adequate.valid adequate Two boolean env5)
  bad6593 : PathP (λ _ → Two) (bop (bop b1 (bop (bop b0 b1) b1)) (bop b1 b0)) b1 → ⊥
  bad6593  p = false≢true (cong lower p)
  cut6593 : Adequate {ℓ} ((op (op (var 0) (op (op (var 1) (var 2)) (var 2))) (op (var 0) (var 1))) , (var 0)) → ⊥
  cut6593  adequate = bad6593  (Adequate.valid adequate Two boolean env11)
  bad6594 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b1 b0) b0)) (bop b0 b1)) b1 → ⊥
  bad6594  p = false≢true (cong lower p)
  cut6594 : Adequate {ℓ} ((op (op (var 0) (op (op (var 1) (var 2)) (var 2))) (op (var 0) (var 1))) , (var 1)) → ⊥
  cut6594  adequate = bad6594  (Adequate.valid adequate Two boolean env4)
  bad6595 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b0 b1) b1)) (bop b0 b0)) b1 → ⊥
  bad6595  p = false≢true (cong lower p)
  cut6595 : Adequate {ℓ} ((op (op (var 0) (op (op (var 1) (var 2)) (var 2))) (op (var 0) (var 1))) , (var 2)) → ⊥
  cut6595  adequate = bad6595  (Adequate.valid adequate Two boolean env1)
  bad6596 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b0 b0) b0)) (bop b0 b0)) b1 → ⊥
  bad6596  p = false≢true (cong lower p)
  cut6596 : Adequate {ℓ} ((op (op (var 0) (op (op (var 1) (var 2)) (var 2))) (op (var 0) (var 1))) , (var 3)) → ⊥
  cut6596  adequate = bad6596  (Adequate.valid adequate Two boolean env5)
  holds6597 : (z0 z1 z2 : A2) → (mul2 (mul2 z0 (mul2 (mul2 z1 z2) z2)) (mul2 z0 z2)) ≡ z0
  holds6597 z0 z1 z2 = refl
  cut6597 : Adequate {ℓ} ((op (op (var 0) (op (op (var 1) (var 2)) (var 2))) (op (var 0) (var 2))) , (var 0)) → ⊥
  cut6597  = reject2 ((op (op (var 0) (op (op (var 1) (var 2)) (var 2))) (op (var 0) (var 2))) , (var 0)) (λ env → holds6597 (env 0) (env 1) (env 2))
  bad6598 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b1 b0) b0)) (bop b0 b0)) b1 → ⊥
  bad6598  p = false≢true (cong lower p)
  cut6598 : Adequate {ℓ} ((op (op (var 0) (op (op (var 1) (var 2)) (var 2))) (op (var 0) (var 2))) , (var 1)) → ⊥
  cut6598  adequate = bad6598  (Adequate.valid adequate Two boolean env4)
  bad6599 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b0 b1) b1)) (bop b0 b1)) b1 → ⊥
  bad6599  p = false≢true (cong lower p)
  cut6599 : Adequate {ℓ} ((op (op (var 0) (op (op (var 1) (var 2)) (var 2))) (op (var 0) (var 2))) , (var 2)) → ⊥
  cut6599  adequate = bad6599  (Adequate.valid adequate Two boolean env1)
  bad6600 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b0 b0) b0)) (bop b0 b0)) b1 → ⊥
  bad6600  p = false≢true (cong lower p)
  cut6600 : Adequate {ℓ} ((op (op (var 0) (op (op (var 1) (var 2)) (var 2))) (op (var 0) (var 2))) , (var 3)) → ⊥
  cut6600  adequate = bad6600  (Adequate.valid adequate Two boolean env5)
  bad6601 : PathP (λ _ → Two) (bop (bop b1 (bop (bop b0 b1) b1)) (bop b1 b0)) b1 → ⊥
  bad6601  p = false≢true (cong lower p)
  cut6601 : Adequate {ℓ} ((op (op (var 0) (op (op (var 1) (var 2)) (var 2))) (op (var 0) (var 3))) , (var 0)) → ⊥
  cut6601  adequate = bad6601  (Adequate.valid adequate Two boolean env12)
  bad6602 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b1 b0) b0)) (bop b0 b0)) b1 → ⊥
  bad6602  p = false≢true (cong lower p)
  cut6602 : Adequate {ℓ} ((op (op (var 0) (op (op (var 1) (var 2)) (var 2))) (op (var 0) (var 3))) , (var 1)) → ⊥
  cut6602  adequate = bad6602  (Adequate.valid adequate Two boolean env13)
  bad6603 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b0 b1) b1)) (bop b0 b0)) b1 → ⊥
  bad6603  p = false≢true (cong lower p)
  cut6603 : Adequate {ℓ} ((op (op (var 0) (op (op (var 1) (var 2)) (var 2))) (op (var 0) (var 3))) , (var 2)) → ⊥
  cut6603  adequate = bad6603  (Adequate.valid adequate Two boolean env8)
  bad6604 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b0 b0) b0)) (bop b0 b1)) b1 → ⊥
  bad6604  p = false≢true (cong lower p)
  cut6604 : Adequate {ℓ} ((op (op (var 0) (op (op (var 1) (var 2)) (var 2))) (op (var 0) (var 3))) , (var 3)) → ⊥
  cut6604  adequate = bad6604  (Adequate.valid adequate Two boolean env5)
  bad6605 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b0 b0) b0)) (bop b0 b0)) b1 → ⊥
  bad6605  p = false≢true (cong lower p)
  cut6605 : Adequate {ℓ} ((op (op (var 0) (op (op (var 1) (var 2)) (var 2))) (op (var 0) (var 3))) , (var 4)) → ⊥
  cut6605  adequate = bad6605  (Adequate.valid adequate Two boolean env9)
  bad6606 : PathP (λ _ → Two) (bop (bop b1 (bop (bop b0 b1) b1)) (bop b0 b1)) b1 → ⊥
  bad6606  p = false≢true (cong lower p)
  cut6606 : Adequate {ℓ} ((op (op (var 0) (op (op (var 1) (var 2)) (var 2))) (op (var 1) (var 0))) , (var 0)) → ⊥
  cut6606  adequate = bad6606  (Adequate.valid adequate Two boolean env11)
  bad6607 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b1 b0) b0)) (bop b1 b0)) b1 → ⊥
  bad6607  p = false≢true (cong lower p)
  cut6607 : Adequate {ℓ} ((op (op (var 0) (op (op (var 1) (var 2)) (var 2))) (op (var 1) (var 0))) , (var 1)) → ⊥
  cut6607  adequate = bad6607  (Adequate.valid adequate Two boolean env4)
  bad6608 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b0 b1) b1)) (bop b0 b0)) b1 → ⊥
  bad6608  p = false≢true (cong lower p)
  cut6608 : Adequate {ℓ} ((op (op (var 0) (op (op (var 1) (var 2)) (var 2))) (op (var 1) (var 0))) , (var 2)) → ⊥
  cut6608  adequate = bad6608  (Adequate.valid adequate Two boolean env1)
  bad6609 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b0 b0) b0)) (bop b0 b0)) b1 → ⊥
  bad6609  p = false≢true (cong lower p)
  cut6609 : Adequate {ℓ} ((op (op (var 0) (op (op (var 1) (var 2)) (var 2))) (op (var 1) (var 0))) , (var 3)) → ⊥
  cut6609  adequate = bad6609  (Adequate.valid adequate Two boolean env5)
  bad6610 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b1 b0) b0)) (bop b1 b1)) b0 → ⊥
  bad6610  p = false≢true (sym (cong lower p))
  cut6610 : Adequate {ℓ} ((op (op (var 0) (op (op (var 1) (var 2)) (var 2))) (op (var 1) (var 1))) , (var 0)) → ⊥
  cut6610  adequate = bad6610  (Adequate.valid adequate Two boolean env4)
  bad6611 : PathP (λ _ → Two) (bop (bop b1 (bop (bop b0 b0) b0)) (bop b0 b0)) b0 → ⊥
  bad6611  p = false≢true (sym (cong lower p))
  cut6611 : Adequate {ℓ} ((op (op (var 0) (op (op (var 1) (var 2)) (var 2))) (op (var 1) (var 1))) , (var 1)) → ⊥
  cut6611  adequate = bad6611  (Adequate.valid adequate Two boolean env6)
  bad6612 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b0 b1) b1)) (bop b0 b0)) b1 → ⊥
  bad6612  p = false≢true (cong lower p)
  cut6612 : Adequate {ℓ} ((op (op (var 0) (op (op (var 1) (var 2)) (var 2))) (op (var 1) (var 1))) , (var 2)) → ⊥
  cut6612  adequate = bad6612  (Adequate.valid adequate Two boolean env1)
  bad6613 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b0 b0) b0)) (bop b0 b0)) b1 → ⊥
  bad6613  p = false≢true (cong lower p)
  cut6613 : Adequate {ℓ} ((op (op (var 0) (op (op (var 1) (var 2)) (var 2))) (op (var 1) (var 1))) , (var 3)) → ⊥
  cut6613  adequate = bad6613  (Adequate.valid adequate Two boolean env5)
  bad6614 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b1 b1) b1)) (bop b1 b1)) b0 → ⊥
  bad6614  p = false≢true (sym (cong lower p))
  cut6614 : Adequate {ℓ} ((op (op (var 0) (op (op (var 1) (var 2)) (var 2))) (op (var 1) (var 2))) , (var 0)) → ⊥
  cut6614  adequate = bad6614  (Adequate.valid adequate Two boolean env3)
  bad6615 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b1 b0) b0)) (bop b1 b0)) b1 → ⊥
  bad6615  p = false≢true (cong lower p)
  cut6615 : Adequate {ℓ} ((op (op (var 0) (op (op (var 1) (var 2)) (var 2))) (op (var 1) (var 2))) , (var 1)) → ⊥
  cut6615  adequate = bad6615  (Adequate.valid adequate Two boolean env4)
  bad6616 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b0 b1) b1)) (bop b0 b1)) b1 → ⊥
  bad6616  p = false≢true (cong lower p)
  cut6616 : Adequate {ℓ} ((op (op (var 0) (op (op (var 1) (var 2)) (var 2))) (op (var 1) (var 2))) , (var 2)) → ⊥
  cut6616  adequate = bad6616  (Adequate.valid adequate Two boolean env1)
  bad6617 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b0 b0) b0)) (bop b0 b0)) b1 → ⊥
  bad6617  p = false≢true (cong lower p)
  cut6617 : Adequate {ℓ} ((op (op (var 0) (op (op (var 1) (var 2)) (var 2))) (op (var 1) (var 2))) , (var 3)) → ⊥
  cut6617  adequate = bad6617  (Adequate.valid adequate Two boolean env5)
  bad6618 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b1 b0) b0)) (bop b1 b1)) b0 → ⊥
  bad6618  p = false≢true (sym (cong lower p))
  cut6618 : Adequate {ℓ} ((op (op (var 0) (op (op (var 1) (var 2)) (var 2))) (op (var 1) (var 3))) , (var 0)) → ⊥
  cut6618  adequate = bad6618  (Adequate.valid adequate Two boolean env14)
  bad6619 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b1 b0) b0)) (bop b1 b0)) b1 → ⊥
  bad6619  p = false≢true (cong lower p)
  cut6619 : Adequate {ℓ} ((op (op (var 0) (op (op (var 1) (var 2)) (var 2))) (op (var 1) (var 3))) , (var 1)) → ⊥
  cut6619  adequate = bad6619  (Adequate.valid adequate Two boolean env13)
  bad6620 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b0 b1) b1)) (bop b0 b0)) b1 → ⊥
  bad6620  p = false≢true (cong lower p)
  cut6620 : Adequate {ℓ} ((op (op (var 0) (op (op (var 1) (var 2)) (var 2))) (op (var 1) (var 3))) , (var 2)) → ⊥
  cut6620  adequate = bad6620  (Adequate.valid adequate Two boolean env8)
  bad6621 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b0 b0) b0)) (bop b0 b1)) b1 → ⊥
  bad6621  p = false≢true (cong lower p)
  cut6621 : Adequate {ℓ} ((op (op (var 0) (op (op (var 1) (var 2)) (var 2))) (op (var 1) (var 3))) , (var 3)) → ⊥
  cut6621  adequate = bad6621  (Adequate.valid adequate Two boolean env5)
  bad6622 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b0 b0) b0)) (bop b0 b0)) b1 → ⊥
  bad6622  p = false≢true (cong lower p)
  cut6622 : Adequate {ℓ} ((op (op (var 0) (op (op (var 1) (var 2)) (var 2))) (op (var 1) (var 3))) , (var 4)) → ⊥
  cut6622  adequate = bad6622  (Adequate.valid adequate Two boolean env9)
  holds6623 : (z0 z1 z2 : A2) → (mul2 (mul2 z0 (mul2 (mul2 z1 z2) z2)) (mul2 z2 z0)) ≡ z0
  holds6623 z0 z1 z2 = refl
  cut6623 : Adequate {ℓ} ((op (op (var 0) (op (op (var 1) (var 2)) (var 2))) (op (var 2) (var 0))) , (var 0)) → ⊥
  cut6623  = reject2 ((op (op (var 0) (op (op (var 1) (var 2)) (var 2))) (op (var 2) (var 0))) , (var 0)) (λ env → holds6623 (env 0) (env 1) (env 2))
  bad6624 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b1 b0) b0)) (bop b0 b0)) b1 → ⊥
  bad6624  p = false≢true (cong lower p)
  cut6624 : Adequate {ℓ} ((op (op (var 0) (op (op (var 1) (var 2)) (var 2))) (op (var 2) (var 0))) , (var 1)) → ⊥
  cut6624  adequate = bad6624  (Adequate.valid adequate Two boolean env4)
  bad6625 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b0 b1) b1)) (bop b1 b0)) b1 → ⊥
  bad6625  p = false≢true (cong lower p)
  cut6625 : Adequate {ℓ} ((op (op (var 0) (op (op (var 1) (var 2)) (var 2))) (op (var 2) (var 0))) , (var 2)) → ⊥
  cut6625  adequate = bad6625  (Adequate.valid adequate Two boolean env1)
  bad6626 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b0 b0) b0)) (bop b0 b0)) b1 → ⊥
  bad6626  p = false≢true (cong lower p)
  cut6626 : Adequate {ℓ} ((op (op (var 0) (op (op (var 1) (var 2)) (var 2))) (op (var 2) (var 0))) , (var 3)) → ⊥
  cut6626  adequate = bad6626  (Adequate.valid adequate Two boolean env5)
  bad6627 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b1 b1) b1)) (bop b1 b1)) b0 → ⊥
  bad6627  p = false≢true (sym (cong lower p))
  cut6627 : Adequate {ℓ} ((op (op (var 0) (op (op (var 1) (var 2)) (var 2))) (op (var 2) (var 1))) , (var 0)) → ⊥
  cut6627  adequate = bad6627  (Adequate.valid adequate Two boolean env3)
  bad6628 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b1 b0) b0)) (bop b0 b1)) b1 → ⊥
  bad6628  p = false≢true (cong lower p)
  cut6628 : Adequate {ℓ} ((op (op (var 0) (op (op (var 1) (var 2)) (var 2))) (op (var 2) (var 1))) , (var 1)) → ⊥
  cut6628  adequate = bad6628  (Adequate.valid adequate Two boolean env4)
  bad6629 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b0 b1) b1)) (bop b1 b0)) b1 → ⊥
  bad6629  p = false≢true (cong lower p)
  cut6629 : Adequate {ℓ} ((op (op (var 0) (op (op (var 1) (var 2)) (var 2))) (op (var 2) (var 1))) , (var 2)) → ⊥
  cut6629  adequate = bad6629  (Adequate.valid adequate Two boolean env1)
  bad6630 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b0 b0) b0)) (bop b0 b0)) b1 → ⊥
  bad6630  p = false≢true (cong lower p)
  cut6630 : Adequate {ℓ} ((op (op (var 0) (op (op (var 1) (var 2)) (var 2))) (op (var 2) (var 1))) , (var 3)) → ⊥
  cut6630  adequate = bad6630  (Adequate.valid adequate Two boolean env5)
  bad6631 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b0 b1) b1)) (bop b1 b1)) b0 → ⊥
  bad6631  p = false≢true (sym (cong lower p))
  cut6631 : Adequate {ℓ} ((op (op (var 0) (op (op (var 1) (var 2)) (var 2))) (op (var 2) (var 2))) , (var 0)) → ⊥
  cut6631  adequate = bad6631  (Adequate.valid adequate Two boolean env1)
  bad6632 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b0 b1) b1)) (bop b1 b1)) b0 → ⊥
  bad6632  p = false≢true (sym (cong lower p))
  cut6632 : Adequate {ℓ} ((op (op (var 0) (op (op (var 1) (var 2)) (var 2))) (op (var 2) (var 2))) , (var 1)) → ⊥
  cut6632  adequate = bad6632  (Adequate.valid adequate Two boolean env1)
  bad6633 : PathP (λ _ → Two) (bop (bop b1 (bop (bop b0 b0) b0)) (bop b0 b0)) b0 → ⊥
  bad6633  p = false≢true (sym (cong lower p))
  cut6633 : Adequate {ℓ} ((op (op (var 0) (op (op (var 1) (var 2)) (var 2))) (op (var 2) (var 2))) , (var 2)) → ⊥
  cut6633  adequate = bad6633  (Adequate.valid adequate Two boolean env6)
  bad6634 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b0 b0) b0)) (bop b0 b0)) b1 → ⊥
  bad6634  p = false≢true (cong lower p)
  cut6634 : Adequate {ℓ} ((op (op (var 0) (op (op (var 1) (var 2)) (var 2))) (op (var 2) (var 2))) , (var 3)) → ⊥
  cut6634  adequate = bad6634  (Adequate.valid adequate Two boolean env5)
  bad6635 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b0 b1) b1)) (bop b1 b1)) b0 → ⊥
  bad6635  p = false≢true (sym (cong lower p))
  cut6635 : Adequate {ℓ} ((op (op (var 0) (op (op (var 1) (var 2)) (var 2))) (op (var 2) (var 3))) , (var 0)) → ⊥
  cut6635  adequate = bad6635  (Adequate.valid adequate Two boolean env7)
  bad6636 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b0 b1) b1)) (bop b1 b1)) b0 → ⊥
  bad6636  p = false≢true (sym (cong lower p))
  cut6636 : Adequate {ℓ} ((op (op (var 0) (op (op (var 1) (var 2)) (var 2))) (op (var 2) (var 3))) , (var 1)) → ⊥
  cut6636  adequate = bad6636  (Adequate.valid adequate Two boolean env7)
  bad6637 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b0 b1) b1)) (bop b1 b0)) b1 → ⊥
  bad6637  p = false≢true (cong lower p)
  cut6637 : Adequate {ℓ} ((op (op (var 0) (op (op (var 1) (var 2)) (var 2))) (op (var 2) (var 3))) , (var 2)) → ⊥
  cut6637  adequate = bad6637  (Adequate.valid adequate Two boolean env8)
  bad6638 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b0 b0) b0)) (bop b0 b1)) b1 → ⊥
  bad6638  p = false≢true (cong lower p)
  cut6638 : Adequate {ℓ} ((op (op (var 0) (op (op (var 1) (var 2)) (var 2))) (op (var 2) (var 3))) , (var 3)) → ⊥
  cut6638  adequate = bad6638  (Adequate.valid adequate Two boolean env5)
  bad6639 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b0 b0) b0)) (bop b0 b0)) b1 → ⊥
  bad6639  p = false≢true (cong lower p)
  cut6639 : Adequate {ℓ} ((op (op (var 0) (op (op (var 1) (var 2)) (var 2))) (op (var 2) (var 3))) , (var 4)) → ⊥
  cut6639  adequate = bad6639  (Adequate.valid adequate Two boolean env9)
  bad6640 : PathP (λ _ → Two) (bop (bop b1 (bop (bop b0 b1) b1)) (bop b0 b1)) b1 → ⊥
  bad6640  p = false≢true (cong lower p)
  cut6640 : Adequate {ℓ} ((op (op (var 0) (op (op (var 1) (var 2)) (var 2))) (op (var 3) (var 0))) , (var 0)) → ⊥
  cut6640  adequate = bad6640  (Adequate.valid adequate Two boolean env12)
  bad6641 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b1 b0) b0)) (bop b0 b0)) b1 → ⊥
  bad6641  p = false≢true (cong lower p)
  cut6641 : Adequate {ℓ} ((op (op (var 0) (op (op (var 1) (var 2)) (var 2))) (op (var 3) (var 0))) , (var 1)) → ⊥
  cut6641  adequate = bad6641  (Adequate.valid adequate Two boolean env13)
  bad6642 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b0 b1) b1)) (bop b0 b0)) b1 → ⊥
  bad6642  p = false≢true (cong lower p)
  cut6642 : Adequate {ℓ} ((op (op (var 0) (op (op (var 1) (var 2)) (var 2))) (op (var 3) (var 0))) , (var 2)) → ⊥
  cut6642  adequate = bad6642  (Adequate.valid adequate Two boolean env8)
  bad6643 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b0 b0) b0)) (bop b1 b0)) b1 → ⊥
  bad6643  p = false≢true (cong lower p)
  cut6643 : Adequate {ℓ} ((op (op (var 0) (op (op (var 1) (var 2)) (var 2))) (op (var 3) (var 0))) , (var 3)) → ⊥
  cut6643  adequate = bad6643  (Adequate.valid adequate Two boolean env5)
  bad6644 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b0 b0) b0)) (bop b0 b0)) b1 → ⊥
  bad6644  p = false≢true (cong lower p)
  cut6644 : Adequate {ℓ} ((op (op (var 0) (op (op (var 1) (var 2)) (var 2))) (op (var 3) (var 0))) , (var 4)) → ⊥
  cut6644  adequate = bad6644  (Adequate.valid adequate Two boolean env9)
  bad6645 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b1 b0) b0)) (bop b1 b1)) b0 → ⊥
  bad6645  p = false≢true (sym (cong lower p))
  cut6645 : Adequate {ℓ} ((op (op (var 0) (op (op (var 1) (var 2)) (var 2))) (op (var 3) (var 1))) , (var 0)) → ⊥
  cut6645  adequate = bad6645  (Adequate.valid adequate Two boolean env14)
  bad6646 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b1 b0) b0)) (bop b0 b1)) b1 → ⊥
  bad6646  p = false≢true (cong lower p)
  cut6646 : Adequate {ℓ} ((op (op (var 0) (op (op (var 1) (var 2)) (var 2))) (op (var 3) (var 1))) , (var 1)) → ⊥
  cut6646  adequate = bad6646  (Adequate.valid adequate Two boolean env13)
  bad6647 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b0 b1) b1)) (bop b0 b0)) b1 → ⊥
  bad6647  p = false≢true (cong lower p)
  cut6647 : Adequate {ℓ} ((op (op (var 0) (op (op (var 1) (var 2)) (var 2))) (op (var 3) (var 1))) , (var 2)) → ⊥
  cut6647  adequate = bad6647  (Adequate.valid adequate Two boolean env8)
  bad6648 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b0 b0) b0)) (bop b1 b0)) b1 → ⊥
  bad6648  p = false≢true (cong lower p)
  cut6648 : Adequate {ℓ} ((op (op (var 0) (op (op (var 1) (var 2)) (var 2))) (op (var 3) (var 1))) , (var 3)) → ⊥
  cut6648  adequate = bad6648  (Adequate.valid adequate Two boolean env5)
  bad6649 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b0 b0) b0)) (bop b0 b0)) b1 → ⊥
  bad6649  p = false≢true (cong lower p)
  cut6649 : Adequate {ℓ} ((op (op (var 0) (op (op (var 1) (var 2)) (var 2))) (op (var 3) (var 1))) , (var 4)) → ⊥
  cut6649  adequate = bad6649  (Adequate.valid adequate Two boolean env9)
  bad6650 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b0 b1) b1)) (bop b1 b1)) b0 → ⊥
  bad6650  p = false≢true (sym (cong lower p))
  cut6650 : Adequate {ℓ} ((op (op (var 0) (op (op (var 1) (var 2)) (var 2))) (op (var 3) (var 2))) , (var 0)) → ⊥
  cut6650  adequate = bad6650  (Adequate.valid adequate Two boolean env7)
  bad6651 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b0 b1) b1)) (bop b1 b1)) b0 → ⊥
  bad6651  p = false≢true (sym (cong lower p))
  cut6651 : Adequate {ℓ} ((op (op (var 0) (op (op (var 1) (var 2)) (var 2))) (op (var 3) (var 2))) , (var 1)) → ⊥
  cut6651  adequate = bad6651  (Adequate.valid adequate Two boolean env7)
  bad6652 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b0 b1) b1)) (bop b0 b1)) b1 → ⊥
  bad6652  p = false≢true (cong lower p)
  cut6652 : Adequate {ℓ} ((op (op (var 0) (op (op (var 1) (var 2)) (var 2))) (op (var 3) (var 2))) , (var 2)) → ⊥
  cut6652  adequate = bad6652  (Adequate.valid adequate Two boolean env8)
  bad6653 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b0 b0) b0)) (bop b1 b0)) b1 → ⊥
  bad6653  p = false≢true (cong lower p)
  cut6653 : Adequate {ℓ} ((op (op (var 0) (op (op (var 1) (var 2)) (var 2))) (op (var 3) (var 2))) , (var 3)) → ⊥
  cut6653  adequate = bad6653  (Adequate.valid adequate Two boolean env5)
  bad6654 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b0 b0) b0)) (bop b0 b0)) b1 → ⊥
  bad6654  p = false≢true (cong lower p)
  cut6654 : Adequate {ℓ} ((op (op (var 0) (op (op (var 1) (var 2)) (var 2))) (op (var 3) (var 2))) , (var 4)) → ⊥
  cut6654  adequate = bad6654  (Adequate.valid adequate Two boolean env9)
  bad6655 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b0 b0) b0)) (bop b1 b1)) b0 → ⊥
  bad6655  p = false≢true (sym (cong lower p))
  cut6655 : Adequate {ℓ} ((op (op (var 0) (op (op (var 1) (var 2)) (var 2))) (op (var 3) (var 3))) , (var 0)) → ⊥
  cut6655  adequate = bad6655  (Adequate.valid adequate Two boolean env5)
  bad6656 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b0 b0) b0)) (bop b1 b1)) b0 → ⊥
  bad6656  p = false≢true (sym (cong lower p))
  cut6656 : Adequate {ℓ} ((op (op (var 0) (op (op (var 1) (var 2)) (var 2))) (op (var 3) (var 3))) , (var 1)) → ⊥
  cut6656  adequate = bad6656  (Adequate.valid adequate Two boolean env5)
  bad6657 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b0 b0) b0)) (bop b1 b1)) b0 → ⊥
  bad6657  p = false≢true (sym (cong lower p))
  cut6657 : Adequate {ℓ} ((op (op (var 0) (op (op (var 1) (var 2)) (var 2))) (op (var 3) (var 3))) , (var 2)) → ⊥
  cut6657  adequate = bad6657  (Adequate.valid adequate Two boolean env5)
  bad6658 : PathP (λ _ → Two) (bop (bop b1 (bop (bop b0 b0) b0)) (bop b0 b0)) b0 → ⊥
  bad6658  p = false≢true (sym (cong lower p))
  cut6658 : Adequate {ℓ} ((op (op (var 0) (op (op (var 1) (var 2)) (var 2))) (op (var 3) (var 3))) , (var 3)) → ⊥
  cut6658  adequate = bad6658  (Adequate.valid adequate Two boolean env15)
  bad6659 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b0 b0) b0)) (bop b0 b0)) b1 → ⊥
  bad6659  p = false≢true (cong lower p)
  cut6659 : Adequate {ℓ} ((op (op (var 0) (op (op (var 1) (var 2)) (var 2))) (op (var 3) (var 3))) , (var 4)) → ⊥
  cut6659  adequate = bad6659  (Adequate.valid adequate Two boolean env9)
  bad6660 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b0 b0) b0)) (bop b1 b1)) b0 → ⊥
  bad6660  p = false≢true (sym (cong lower p))
  cut6660 : Adequate {ℓ} ((op (op (var 0) (op (op (var 1) (var 2)) (var 2))) (op (var 3) (var 4))) , (var 0)) → ⊥
  cut6660  adequate = bad6660  (Adequate.valid adequate Two boolean env16)
  bad6661 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b0 b0) b0)) (bop b1 b1)) b0 → ⊥
  bad6661  p = false≢true (sym (cong lower p))
  cut6661 : Adequate {ℓ} ((op (op (var 0) (op (op (var 1) (var 2)) (var 2))) (op (var 3) (var 4))) , (var 1)) → ⊥
  cut6661  adequate = bad6661  (Adequate.valid adequate Two boolean env16)
  bad6662 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b0 b0) b0)) (bop b1 b1)) b0 → ⊥
  bad6662  p = false≢true (sym (cong lower p))
  cut6662 : Adequate {ℓ} ((op (op (var 0) (op (op (var 1) (var 2)) (var 2))) (op (var 3) (var 4))) , (var 2)) → ⊥
  cut6662  adequate = bad6662  (Adequate.valid adequate Two boolean env16)
  bad6663 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b0 b0) b0)) (bop b1 b0)) b1 → ⊥
  bad6663  p = false≢true (cong lower p)
  cut6663 : Adequate {ℓ} ((op (op (var 0) (op (op (var 1) (var 2)) (var 2))) (op (var 3) (var 4))) , (var 3)) → ⊥
  cut6663  adequate = bad6663  (Adequate.valid adequate Two boolean env17)
  bad6664 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b0 b0) b0)) (bop b0 b1)) b1 → ⊥
  bad6664  p = false≢true (cong lower p)
  cut6664 : Adequate {ℓ} ((op (op (var 0) (op (op (var 1) (var 2)) (var 2))) (op (var 3) (var 4))) , (var 4)) → ⊥
  cut6664  adequate = bad6664  (Adequate.valid adequate Two boolean env9)
  bad6665 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b0 b0) b0)) (bop b0 b0)) b1 → ⊥
  bad6665  p = false≢true (cong lower p)
  cut6665 : Adequate {ℓ} ((op (op (var 0) (op (op (var 1) (var 2)) (var 2))) (op (var 3) (var 4))) , (var 5)) → ⊥
  cut6665  adequate = bad6665  (Adequate.valid adequate Two boolean env18)
  holds6666 : (z0 z1 z2 z3 : A2) → (mul2 (mul2 z0 (mul2 (mul2 z1 z2) z3)) (mul2 z0 z0)) ≡ z0
  holds6666 z0 z1 z2 z3 = refl
  cut6666 : Adequate {ℓ} ((op (op (var 0) (op (op (var 1) (var 2)) (var 3))) (op (var 0) (var 0))) , (var 0)) → ⊥
  cut6666  = reject2 ((op (op (var 0) (op (op (var 1) (var 2)) (var 3))) (op (var 0) (var 0))) , (var 0)) (λ env → holds6666 (env 0) (env 1) (env 2) (env 3))
  bad6667 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b1 b0) b0)) (bop b0 b0)) b1 → ⊥
  bad6667  p = false≢true (cong lower p)
  cut6667 : Adequate {ℓ} ((op (op (var 0) (op (op (var 1) (var 2)) (var 3))) (op (var 0) (var 0))) , (var 1)) → ⊥
  cut6667  adequate = bad6667  (Adequate.valid adequate Two boolean env13)
  bad6668 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b0 b1) b0)) (bop b0 b0)) b1 → ⊥
  bad6668  p = false≢true (cong lower p)
  cut6668 : Adequate {ℓ} ((op (op (var 0) (op (op (var 1) (var 2)) (var 3))) (op (var 0) (var 0))) , (var 2)) → ⊥
  cut6668  adequate = bad6668  (Adequate.valid adequate Two boolean env8)
  bad6669 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b0 b0) b1)) (bop b0 b0)) b1 → ⊥
  bad6669  p = false≢true (cong lower p)
  cut6669 : Adequate {ℓ} ((op (op (var 0) (op (op (var 1) (var 2)) (var 3))) (op (var 0) (var 0))) , (var 3)) → ⊥
  cut6669  adequate = bad6669  (Adequate.valid adequate Two boolean env5)
  bad6670 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b0 b0) b0)) (bop b0 b0)) b1 → ⊥
  bad6670  p = false≢true (cong lower p)
  cut6670 : Adequate {ℓ} ((op (op (var 0) (op (op (var 1) (var 2)) (var 3))) (op (var 0) (var 0))) , (var 4)) → ⊥
  cut6670  adequate = bad6670  (Adequate.valid adequate Two boolean env9)
  env21 : ℕ → Two
  env21 zero = b1
  env21 (suc zero) = b0
  env21 (suc (suc zero)) = b0
  env21 (suc (suc (suc zero))) = b1
  env21 (suc (suc (suc (suc rest)))) = b0
  bad6671 : PathP (λ _ → Two) (bop (bop b1 (bop (bop b0 b0) b1)) (bop b1 b0)) b1 → ⊥
  bad6671  p = false≢true (cong lower p)
  cut6671 : Adequate {ℓ} ((op (op (var 0) (op (op (var 1) (var 2)) (var 3))) (op (var 0) (var 1))) , (var 0)) → ⊥
  cut6671  adequate = bad6671  (Adequate.valid adequate Two boolean env21)
  bad6672 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b1 b0) b0)) (bop b0 b1)) b1 → ⊥
  bad6672  p = false≢true (cong lower p)
  cut6672 : Adequate {ℓ} ((op (op (var 0) (op (op (var 1) (var 2)) (var 3))) (op (var 0) (var 1))) , (var 1)) → ⊥
  cut6672  adequate = bad6672  (Adequate.valid adequate Two boolean env13)
  bad6673 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b0 b1) b0)) (bop b0 b0)) b1 → ⊥
  bad6673  p = false≢true (cong lower p)
  cut6673 : Adequate {ℓ} ((op (op (var 0) (op (op (var 1) (var 2)) (var 3))) (op (var 0) (var 1))) , (var 2)) → ⊥
  cut6673  adequate = bad6673  (Adequate.valid adequate Two boolean env8)
  bad6674 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b0 b0) b1)) (bop b0 b0)) b1 → ⊥
  bad6674  p = false≢true (cong lower p)
  cut6674 : Adequate {ℓ} ((op (op (var 0) (op (op (var 1) (var 2)) (var 3))) (op (var 0) (var 1))) , (var 3)) → ⊥
  cut6674  adequate = bad6674  (Adequate.valid adequate Two boolean env5)
  bad6675 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b0 b0) b0)) (bop b0 b0)) b1 → ⊥
  bad6675  p = false≢true (cong lower p)
  cut6675 : Adequate {ℓ} ((op (op (var 0) (op (op (var 1) (var 2)) (var 3))) (op (var 0) (var 1))) , (var 4)) → ⊥
  cut6675  adequate = bad6675  (Adequate.valid adequate Two boolean env9)
  bad6676 : PathP (λ _ → Two) (bop (bop b1 (bop (bop b0 b0) b1)) (bop b1 b0)) b1 → ⊥
  bad6676  p = false≢true (cong lower p)
  cut6676 : Adequate {ℓ} ((op (op (var 0) (op (op (var 1) (var 2)) (var 3))) (op (var 0) (var 2))) , (var 0)) → ⊥
  cut6676  adequate = bad6676  (Adequate.valid adequate Two boolean env21)
  bad6677 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b1 b0) b0)) (bop b0 b0)) b1 → ⊥
  bad6677  p = false≢true (cong lower p)
  cut6677 : Adequate {ℓ} ((op (op (var 0) (op (op (var 1) (var 2)) (var 3))) (op (var 0) (var 2))) , (var 1)) → ⊥
  cut6677  adequate = bad6677  (Adequate.valid adequate Two boolean env13)
  bad6678 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b0 b1) b0)) (bop b0 b1)) b1 → ⊥
  bad6678  p = false≢true (cong lower p)
  cut6678 : Adequate {ℓ} ((op (op (var 0) (op (op (var 1) (var 2)) (var 3))) (op (var 0) (var 2))) , (var 2)) → ⊥
  cut6678  adequate = bad6678  (Adequate.valid adequate Two boolean env8)
  bad6679 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b0 b0) b1)) (bop b0 b0)) b1 → ⊥
  bad6679  p = false≢true (cong lower p)
  cut6679 : Adequate {ℓ} ((op (op (var 0) (op (op (var 1) (var 2)) (var 3))) (op (var 0) (var 2))) , (var 3)) → ⊥
  cut6679  adequate = bad6679  (Adequate.valid adequate Two boolean env5)
  bad6680 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b0 b0) b0)) (bop b0 b0)) b1 → ⊥
  bad6680  p = false≢true (cong lower p)
  cut6680 : Adequate {ℓ} ((op (op (var 0) (op (op (var 1) (var 2)) (var 3))) (op (var 0) (var 2))) , (var 4)) → ⊥
  cut6680  adequate = bad6680  (Adequate.valid adequate Two boolean env9)
  holds6681 : (z0 z1 z2 z3 : A2) → (mul2 (mul2 z0 (mul2 (mul2 z1 z2) z3)) (mul2 z0 z3)) ≡ z0
  holds6681 z0 z1 z2 z3 = refl
  cut6681 : Adequate {ℓ} ((op (op (var 0) (op (op (var 1) (var 2)) (var 3))) (op (var 0) (var 3))) , (var 0)) → ⊥
  cut6681  = reject2 ((op (op (var 0) (op (op (var 1) (var 2)) (var 3))) (op (var 0) (var 3))) , (var 0)) (λ env → holds6681 (env 0) (env 1) (env 2) (env 3))
  bad6682 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b1 b0) b0)) (bop b0 b0)) b1 → ⊥
  bad6682  p = false≢true (cong lower p)
  cut6682 : Adequate {ℓ} ((op (op (var 0) (op (op (var 1) (var 2)) (var 3))) (op (var 0) (var 3))) , (var 1)) → ⊥
  cut6682  adequate = bad6682  (Adequate.valid adequate Two boolean env13)
  bad6683 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b0 b1) b0)) (bop b0 b0)) b1 → ⊥
  bad6683  p = false≢true (cong lower p)
  cut6683 : Adequate {ℓ} ((op (op (var 0) (op (op (var 1) (var 2)) (var 3))) (op (var 0) (var 3))) , (var 2)) → ⊥
  cut6683  adequate = bad6683  (Adequate.valid adequate Two boolean env8)
  bad6684 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b0 b0) b1)) (bop b0 b1)) b1 → ⊥
  bad6684  p = false≢true (cong lower p)
  cut6684 : Adequate {ℓ} ((op (op (var 0) (op (op (var 1) (var 2)) (var 3))) (op (var 0) (var 3))) , (var 3)) → ⊥
  cut6684  adequate = bad6684  (Adequate.valid adequate Two boolean env5)
  bad6685 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b0 b0) b0)) (bop b0 b0)) b1 → ⊥
  bad6685  p = false≢true (cong lower p)
  cut6685 : Adequate {ℓ} ((op (op (var 0) (op (op (var 1) (var 2)) (var 3))) (op (var 0) (var 3))) , (var 4)) → ⊥
  cut6685  adequate = bad6685  (Adequate.valid adequate Two boolean env9)
  env22 : ℕ → Two
  env22 zero = b1
  env22 (suc zero) = b0
  env22 (suc (suc zero)) = b0
  env22 (suc (suc (suc zero))) = b1
  env22 (suc (suc (suc (suc zero)))) = b0
  env22 (suc (suc (suc (suc (suc rest))))) = b0
  bad6686 : PathP (λ _ → Two) (bop (bop b1 (bop (bop b0 b0) b1)) (bop b1 b0)) b1 → ⊥
  bad6686  p = false≢true (cong lower p)
  cut6686 : Adequate {ℓ} ((op (op (var 0) (op (op (var 1) (var 2)) (var 3))) (op (var 0) (var 4))) , (var 0)) → ⊥
  cut6686  adequate = bad6686  (Adequate.valid adequate Two boolean env22)
  env23 : ℕ → Two
  env23 zero = b0
  env23 (suc zero) = b1
  env23 (suc (suc zero)) = b0
  env23 (suc (suc (suc zero))) = b0
  env23 (suc (suc (suc (suc zero)))) = b0
  env23 (suc (suc (suc (suc (suc rest))))) = b0
  bad6687 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b1 b0) b0)) (bop b0 b0)) b1 → ⊥
  bad6687  p = false≢true (cong lower p)
  cut6687 : Adequate {ℓ} ((op (op (var 0) (op (op (var 1) (var 2)) (var 3))) (op (var 0) (var 4))) , (var 1)) → ⊥
  cut6687  adequate = bad6687  (Adequate.valid adequate Two boolean env23)
  env24 : ℕ → Two
  env24 zero = b0
  env24 (suc zero) = b0
  env24 (suc (suc zero)) = b1
  env24 (suc (suc (suc zero))) = b0
  env24 (suc (suc (suc (suc zero)))) = b0
  env24 (suc (suc (suc (suc (suc rest))))) = b0
  bad6688 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b0 b1) b0)) (bop b0 b0)) b1 → ⊥
  bad6688  p = false≢true (cong lower p)
  cut6688 : Adequate {ℓ} ((op (op (var 0) (op (op (var 1) (var 2)) (var 3))) (op (var 0) (var 4))) , (var 2)) → ⊥
  cut6688  adequate = bad6688  (Adequate.valid adequate Two boolean env24)
  bad6689 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b0 b0) b1)) (bop b0 b0)) b1 → ⊥
  bad6689  p = false≢true (cong lower p)
  cut6689 : Adequate {ℓ} ((op (op (var 0) (op (op (var 1) (var 2)) (var 3))) (op (var 0) (var 4))) , (var 3)) → ⊥
  cut6689  adequate = bad6689  (Adequate.valid adequate Two boolean env17)
  bad6690 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b0 b0) b0)) (bop b0 b1)) b1 → ⊥
  bad6690  p = false≢true (cong lower p)
  cut6690 : Adequate {ℓ} ((op (op (var 0) (op (op (var 1) (var 2)) (var 3))) (op (var 0) (var 4))) , (var 4)) → ⊥
  cut6690  adequate = bad6690  (Adequate.valid adequate Two boolean env9)
  bad6691 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b0 b0) b0)) (bop b0 b0)) b1 → ⊥
  bad6691  p = false≢true (cong lower p)
  cut6691 : Adequate {ℓ} ((op (op (var 0) (op (op (var 1) (var 2)) (var 3))) (op (var 0) (var 4))) , (var 5)) → ⊥
  cut6691  adequate = bad6691  (Adequate.valid adequate Two boolean env18)
  bad6692 : PathP (λ _ → Two) (bop (bop b1 (bop (bop b0 b0) b1)) (bop b0 b1)) b1 → ⊥
  bad6692  p = false≢true (cong lower p)
  cut6692 : Adequate {ℓ} ((op (op (var 0) (op (op (var 1) (var 2)) (var 3))) (op (var 1) (var 0))) , (var 0)) → ⊥
  cut6692  adequate = bad6692  (Adequate.valid adequate Two boolean env21)
  bad6693 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b1 b0) b0)) (bop b1 b0)) b1 → ⊥
  bad6693  p = false≢true (cong lower p)
  cut6693 : Adequate {ℓ} ((op (op (var 0) (op (op (var 1) (var 2)) (var 3))) (op (var 1) (var 0))) , (var 1)) → ⊥
  cut6693  adequate = bad6693  (Adequate.valid adequate Two boolean env13)
  bad6694 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b0 b1) b0)) (bop b0 b0)) b1 → ⊥
  bad6694  p = false≢true (cong lower p)
  cut6694 : Adequate {ℓ} ((op (op (var 0) (op (op (var 1) (var 2)) (var 3))) (op (var 1) (var 0))) , (var 2)) → ⊥
  cut6694  adequate = bad6694  (Adequate.valid adequate Two boolean env8)
  bad6695 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b0 b0) b1)) (bop b0 b0)) b1 → ⊥
  bad6695  p = false≢true (cong lower p)
  cut6695 : Adequate {ℓ} ((op (op (var 0) (op (op (var 1) (var 2)) (var 3))) (op (var 1) (var 0))) , (var 3)) → ⊥
  cut6695  adequate = bad6695  (Adequate.valid adequate Two boolean env5)
  bad6696 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b0 b0) b0)) (bop b0 b0)) b1 → ⊥
  bad6696  p = false≢true (cong lower p)
  cut6696 : Adequate {ℓ} ((op (op (var 0) (op (op (var 1) (var 2)) (var 3))) (op (var 1) (var 0))) , (var 4)) → ⊥
  cut6696  adequate = bad6696  (Adequate.valid adequate Two boolean env9)
  bad6697 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b1 b0) b0)) (bop b1 b1)) b0 → ⊥
  bad6697  p = false≢true (sym (cong lower p))
  cut6697 : Adequate {ℓ} ((op (op (var 0) (op (op (var 1) (var 2)) (var 3))) (op (var 1) (var 1))) , (var 0)) → ⊥
  cut6697  adequate = bad6697  (Adequate.valid adequate Two boolean env13)
  bad6698 : PathP (λ _ → Two) (bop (bop b1 (bop (bop b0 b0) b0)) (bop b0 b0)) b0 → ⊥
  bad6698  p = false≢true (sym (cong lower p))
  cut6698 : Adequate {ℓ} ((op (op (var 0) (op (op (var 1) (var 2)) (var 3))) (op (var 1) (var 1))) , (var 1)) → ⊥
  cut6698  adequate = bad6698  (Adequate.valid adequate Two boolean env15)
  bad6699 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b0 b1) b0)) (bop b0 b0)) b1 → ⊥
  bad6699  p = false≢true (cong lower p)
  cut6699 : Adequate {ℓ} ((op (op (var 0) (op (op (var 1) (var 2)) (var 3))) (op (var 1) (var 1))) , (var 2)) → ⊥
  cut6699  adequate = bad6699  (Adequate.valid adequate Two boolean env8)
  bad6700 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b0 b0) b1)) (bop b0 b0)) b1 → ⊥
  bad6700  p = false≢true (cong lower p)
  cut6700 : Adequate {ℓ} ((op (op (var 0) (op (op (var 1) (var 2)) (var 3))) (op (var 1) (var 1))) , (var 3)) → ⊥
  cut6700  adequate = bad6700  (Adequate.valid adequate Two boolean env5)
  bad6701 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b0 b0) b0)) (bop b0 b0)) b1 → ⊥
  bad6701  p = false≢true (cong lower p)
  cut6701 : Adequate {ℓ} ((op (op (var 0) (op (op (var 1) (var 2)) (var 3))) (op (var 1) (var 1))) , (var 4)) → ⊥
  cut6701  adequate = bad6701  (Adequate.valid adequate Two boolean env9)
  env25 : ℕ → Two
  env25 zero = b0
  env25 (suc zero) = b1
  env25 (suc (suc zero)) = b1
  env25 (suc (suc (suc zero))) = b0
  env25 (suc (suc (suc (suc rest)))) = b0
  bad6702 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b1 b1) b0)) (bop b1 b1)) b0 → ⊥
  bad6702  p = false≢true (sym (cong lower p))
  cut6702 : Adequate {ℓ} ((op (op (var 0) (op (op (var 1) (var 2)) (var 3))) (op (var 1) (var 2))) , (var 0)) → ⊥
  cut6702  adequate = bad6702  (Adequate.valid adequate Two boolean env25)
  bad6703 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b1 b0) b0)) (bop b1 b0)) b1 → ⊥
  bad6703  p = false≢true (cong lower p)
  cut6703 : Adequate {ℓ} ((op (op (var 0) (op (op (var 1) (var 2)) (var 3))) (op (var 1) (var 2))) , (var 1)) → ⊥
  cut6703  adequate = bad6703  (Adequate.valid adequate Two boolean env13)
  bad6704 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b0 b1) b0)) (bop b0 b1)) b1 → ⊥
  bad6704  p = false≢true (cong lower p)
  cut6704 : Adequate {ℓ} ((op (op (var 0) (op (op (var 1) (var 2)) (var 3))) (op (var 1) (var 2))) , (var 2)) → ⊥
  cut6704  adequate = bad6704  (Adequate.valid adequate Two boolean env8)
  bad6705 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b0 b0) b1)) (bop b0 b0)) b1 → ⊥
  bad6705  p = false≢true (cong lower p)
  cut6705 : Adequate {ℓ} ((op (op (var 0) (op (op (var 1) (var 2)) (var 3))) (op (var 1) (var 2))) , (var 3)) → ⊥
  cut6705  adequate = bad6705  (Adequate.valid adequate Two boolean env5)
  bad6706 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b0 b0) b0)) (bop b0 b0)) b1 → ⊥
  bad6706  p = false≢true (cong lower p)
  cut6706 : Adequate {ℓ} ((op (op (var 0) (op (op (var 1) (var 2)) (var 3))) (op (var 1) (var 2))) , (var 4)) → ⊥
  cut6706  adequate = bad6706  (Adequate.valid adequate Two boolean env9)
  bad6707 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b1 b0) b1)) (bop b1 b1)) b0 → ⊥
  bad6707  p = false≢true (sym (cong lower p))
  cut6707 : Adequate {ℓ} ((op (op (var 0) (op (op (var 1) (var 2)) (var 3))) (op (var 1) (var 3))) , (var 0)) → ⊥
  cut6707  adequate = bad6707  (Adequate.valid adequate Two boolean env14)
  bad6708 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b1 b0) b0)) (bop b1 b0)) b1 → ⊥
  bad6708  p = false≢true (cong lower p)
  cut6708 : Adequate {ℓ} ((op (op (var 0) (op (op (var 1) (var 2)) (var 3))) (op (var 1) (var 3))) , (var 1)) → ⊥
  cut6708  adequate = bad6708  (Adequate.valid adequate Two boolean env13)
  bad6709 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b0 b1) b0)) (bop b0 b0)) b1 → ⊥
  bad6709  p = false≢true (cong lower p)
  cut6709 : Adequate {ℓ} ((op (op (var 0) (op (op (var 1) (var 2)) (var 3))) (op (var 1) (var 3))) , (var 2)) → ⊥
  cut6709  adequate = bad6709  (Adequate.valid adequate Two boolean env8)
  bad6710 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b0 b0) b1)) (bop b0 b1)) b1 → ⊥
  bad6710  p = false≢true (cong lower p)
  cut6710 : Adequate {ℓ} ((op (op (var 0) (op (op (var 1) (var 2)) (var 3))) (op (var 1) (var 3))) , (var 3)) → ⊥
  cut6710  adequate = bad6710  (Adequate.valid adequate Two boolean env5)
  bad6711 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b0 b0) b0)) (bop b0 b0)) b1 → ⊥
  bad6711  p = false≢true (cong lower p)
  cut6711 : Adequate {ℓ} ((op (op (var 0) (op (op (var 1) (var 2)) (var 3))) (op (var 1) (var 3))) , (var 4)) → ⊥
  cut6711  adequate = bad6711  (Adequate.valid adequate Two boolean env9)
  env26 : ℕ → Two
  env26 zero = b0
  env26 (suc zero) = b1
  env26 (suc (suc zero)) = b0
  env26 (suc (suc (suc zero))) = b0
  env26 (suc (suc (suc (suc zero)))) = b1
  env26 (suc (suc (suc (suc (suc rest))))) = b0
  bad6712 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b1 b0) b0)) (bop b1 b1)) b0 → ⊥
  bad6712  p = false≢true (sym (cong lower p))
  cut6712 : Adequate {ℓ} ((op (op (var 0) (op (op (var 1) (var 2)) (var 3))) (op (var 1) (var 4))) , (var 0)) → ⊥
  cut6712  adequate = bad6712  (Adequate.valid adequate Two boolean env26)
  bad6713 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b1 b0) b0)) (bop b1 b0)) b1 → ⊥
  bad6713  p = false≢true (cong lower p)
  cut6713 : Adequate {ℓ} ((op (op (var 0) (op (op (var 1) (var 2)) (var 3))) (op (var 1) (var 4))) , (var 1)) → ⊥
  cut6713  adequate = bad6713  (Adequate.valid adequate Two boolean env23)
  bad6714 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b0 b1) b0)) (bop b0 b0)) b1 → ⊥
  bad6714  p = false≢true (cong lower p)
  cut6714 : Adequate {ℓ} ((op (op (var 0) (op (op (var 1) (var 2)) (var 3))) (op (var 1) (var 4))) , (var 2)) → ⊥
  cut6714  adequate = bad6714  (Adequate.valid adequate Two boolean env24)
  bad6715 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b0 b0) b1)) (bop b0 b0)) b1 → ⊥
  bad6715  p = false≢true (cong lower p)
  cut6715 : Adequate {ℓ} ((op (op (var 0) (op (op (var 1) (var 2)) (var 3))) (op (var 1) (var 4))) , (var 3)) → ⊥
  cut6715  adequate = bad6715  (Adequate.valid adequate Two boolean env17)
  bad6716 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b0 b0) b0)) (bop b0 b1)) b1 → ⊥
  bad6716  p = false≢true (cong lower p)
  cut6716 : Adequate {ℓ} ((op (op (var 0) (op (op (var 1) (var 2)) (var 3))) (op (var 1) (var 4))) , (var 4)) → ⊥
  cut6716  adequate = bad6716  (Adequate.valid adequate Two boolean env9)
  bad6717 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b0 b0) b0)) (bop b0 b0)) b1 → ⊥
  bad6717  p = false≢true (cong lower p)
  cut6717 : Adequate {ℓ} ((op (op (var 0) (op (op (var 1) (var 2)) (var 3))) (op (var 1) (var 4))) , (var 5)) → ⊥
  cut6717  adequate = bad6717  (Adequate.valid adequate Two boolean env18)
  bad6718 : PathP (λ _ → Two) (bop (bop b1 (bop (bop b0 b0) b1)) (bop b0 b1)) b1 → ⊥
  bad6718  p = false≢true (cong lower p)
  cut6718 : Adequate {ℓ} ((op (op (var 0) (op (op (var 1) (var 2)) (var 3))) (op (var 2) (var 0))) , (var 0)) → ⊥
  cut6718  adequate = bad6718  (Adequate.valid adequate Two boolean env21)
  bad6719 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b1 b0) b0)) (bop b0 b0)) b1 → ⊥
  bad6719  p = false≢true (cong lower p)
  cut6719 : Adequate {ℓ} ((op (op (var 0) (op (op (var 1) (var 2)) (var 3))) (op (var 2) (var 0))) , (var 1)) → ⊥
  cut6719  adequate = bad6719  (Adequate.valid adequate Two boolean env13)
  bad6720 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b0 b1) b0)) (bop b1 b0)) b1 → ⊥
  bad6720  p = false≢true (cong lower p)
  cut6720 : Adequate {ℓ} ((op (op (var 0) (op (op (var 1) (var 2)) (var 3))) (op (var 2) (var 0))) , (var 2)) → ⊥
  cut6720  adequate = bad6720  (Adequate.valid adequate Two boolean env8)
  bad6721 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b0 b0) b1)) (bop b0 b0)) b1 → ⊥
  bad6721  p = false≢true (cong lower p)
  cut6721 : Adequate {ℓ} ((op (op (var 0) (op (op (var 1) (var 2)) (var 3))) (op (var 2) (var 0))) , (var 3)) → ⊥
  cut6721  adequate = bad6721  (Adequate.valid adequate Two boolean env5)
  bad6722 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b0 b0) b0)) (bop b0 b0)) b1 → ⊥
  bad6722  p = false≢true (cong lower p)
  cut6722 : Adequate {ℓ} ((op (op (var 0) (op (op (var 1) (var 2)) (var 3))) (op (var 2) (var 0))) , (var 4)) → ⊥
  cut6722  adequate = bad6722  (Adequate.valid adequate Two boolean env9)
  bad6723 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b1 b1) b0)) (bop b1 b1)) b0 → ⊥
  bad6723  p = false≢true (sym (cong lower p))
  cut6723 : Adequate {ℓ} ((op (op (var 0) (op (op (var 1) (var 2)) (var 3))) (op (var 2) (var 1))) , (var 0)) → ⊥
  cut6723  adequate = bad6723  (Adequate.valid adequate Two boolean env25)
  bad6724 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b1 b0) b0)) (bop b0 b1)) b1 → ⊥
  bad6724  p = false≢true (cong lower p)
  cut6724 : Adequate {ℓ} ((op (op (var 0) (op (op (var 1) (var 2)) (var 3))) (op (var 2) (var 1))) , (var 1)) → ⊥
  cut6724  adequate = bad6724  (Adequate.valid adequate Two boolean env13)
  bad6725 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b0 b1) b0)) (bop b1 b0)) b1 → ⊥
  bad6725  p = false≢true (cong lower p)
  cut6725 : Adequate {ℓ} ((op (op (var 0) (op (op (var 1) (var 2)) (var 3))) (op (var 2) (var 1))) , (var 2)) → ⊥
  cut6725  adequate = bad6725  (Adequate.valid adequate Two boolean env8)
  bad6726 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b0 b0) b1)) (bop b0 b0)) b1 → ⊥
  bad6726  p = false≢true (cong lower p)
  cut6726 : Adequate {ℓ} ((op (op (var 0) (op (op (var 1) (var 2)) (var 3))) (op (var 2) (var 1))) , (var 3)) → ⊥
  cut6726  adequate = bad6726  (Adequate.valid adequate Two boolean env5)
  bad6727 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b0 b0) b0)) (bop b0 b0)) b1 → ⊥
  bad6727  p = false≢true (cong lower p)
  cut6727 : Adequate {ℓ} ((op (op (var 0) (op (op (var 1) (var 2)) (var 3))) (op (var 2) (var 1))) , (var 4)) → ⊥
  cut6727  adequate = bad6727  (Adequate.valid adequate Two boolean env9)
  bad6728 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b0 b1) b0)) (bop b1 b1)) b0 → ⊥
  bad6728  p = false≢true (sym (cong lower p))
  cut6728 : Adequate {ℓ} ((op (op (var 0) (op (op (var 1) (var 2)) (var 3))) (op (var 2) (var 2))) , (var 0)) → ⊥
  cut6728  adequate = bad6728  (Adequate.valid adequate Two boolean env8)
  bad6729 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b0 b1) b0)) (bop b1 b1)) b0 → ⊥
  bad6729  p = false≢true (sym (cong lower p))
  cut6729 : Adequate {ℓ} ((op (op (var 0) (op (op (var 1) (var 2)) (var 3))) (op (var 2) (var 2))) , (var 1)) → ⊥
  cut6729  adequate = bad6729  (Adequate.valid adequate Two boolean env8)
  bad6730 : PathP (λ _ → Two) (bop (bop b1 (bop (bop b0 b0) b0)) (bop b0 b0)) b0 → ⊥
  bad6730  p = false≢true (sym (cong lower p))
  cut6730 : Adequate {ℓ} ((op (op (var 0) (op (op (var 1) (var 2)) (var 3))) (op (var 2) (var 2))) , (var 2)) → ⊥
  cut6730  adequate = bad6730  (Adequate.valid adequate Two boolean env15)
  bad6731 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b0 b0) b1)) (bop b0 b0)) b1 → ⊥
  bad6731  p = false≢true (cong lower p)
  cut6731 : Adequate {ℓ} ((op (op (var 0) (op (op (var 1) (var 2)) (var 3))) (op (var 2) (var 2))) , (var 3)) → ⊥
  cut6731  adequate = bad6731  (Adequate.valid adequate Two boolean env5)
  bad6732 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b0 b0) b0)) (bop b0 b0)) b1 → ⊥
  bad6732  p = false≢true (cong lower p)
  cut6732 : Adequate {ℓ} ((op (op (var 0) (op (op (var 1) (var 2)) (var 3))) (op (var 2) (var 2))) , (var 4)) → ⊥
  cut6732  adequate = bad6732  (Adequate.valid adequate Two boolean env9)
  bad6733 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b0 b1) b1)) (bop b1 b1)) b0 → ⊥
  bad6733  p = false≢true (sym (cong lower p))
  cut6733 : Adequate {ℓ} ((op (op (var 0) (op (op (var 1) (var 2)) (var 3))) (op (var 2) (var 3))) , (var 0)) → ⊥
  cut6733  adequate = bad6733  (Adequate.valid adequate Two boolean env7)
  bad6734 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b0 b1) b1)) (bop b1 b1)) b0 → ⊥
  bad6734  p = false≢true (sym (cong lower p))
  cut6734 : Adequate {ℓ} ((op (op (var 0) (op (op (var 1) (var 2)) (var 3))) (op (var 2) (var 3))) , (var 1)) → ⊥
  cut6734  adequate = bad6734  (Adequate.valid adequate Two boolean env7)
  bad6735 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b0 b1) b0)) (bop b1 b0)) b1 → ⊥
  bad6735  p = false≢true (cong lower p)
  cut6735 : Adequate {ℓ} ((op (op (var 0) (op (op (var 1) (var 2)) (var 3))) (op (var 2) (var 3))) , (var 2)) → ⊥
  cut6735  adequate = bad6735  (Adequate.valid adequate Two boolean env8)
  bad6736 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b0 b0) b1)) (bop b0 b1)) b1 → ⊥
  bad6736  p = false≢true (cong lower p)
  cut6736 : Adequate {ℓ} ((op (op (var 0) (op (op (var 1) (var 2)) (var 3))) (op (var 2) (var 3))) , (var 3)) → ⊥
  cut6736  adequate = bad6736  (Adequate.valid adequate Two boolean env5)
  bad6737 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b0 b0) b0)) (bop b0 b0)) b1 → ⊥
  bad6737  p = false≢true (cong lower p)
  cut6737 : Adequate {ℓ} ((op (op (var 0) (op (op (var 1) (var 2)) (var 3))) (op (var 2) (var 3))) , (var 4)) → ⊥
  cut6737  adequate = bad6737  (Adequate.valid adequate Two boolean env9)
  env27 : ℕ → Two
  env27 zero = b0
  env27 (suc zero) = b0
  env27 (suc (suc zero)) = b1
  env27 (suc (suc (suc zero))) = b0
  env27 (suc (suc (suc (suc zero)))) = b1
  env27 (suc (suc (suc (suc (suc rest))))) = b0
  bad6738 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b0 b1) b0)) (bop b1 b1)) b0 → ⊥
  bad6738  p = false≢true (sym (cong lower p))
  cut6738 : Adequate {ℓ} ((op (op (var 0) (op (op (var 1) (var 2)) (var 3))) (op (var 2) (var 4))) , (var 0)) → ⊥
  cut6738  adequate = bad6738  (Adequate.valid adequate Two boolean env27)
  bad6739 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b0 b1) b0)) (bop b1 b1)) b0 → ⊥
  bad6739  p = false≢true (sym (cong lower p))
  cut6739 : Adequate {ℓ} ((op (op (var 0) (op (op (var 1) (var 2)) (var 3))) (op (var 2) (var 4))) , (var 1)) → ⊥
  cut6739  adequate = bad6739  (Adequate.valid adequate Two boolean env27)
  bad6740 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b0 b1) b0)) (bop b1 b0)) b1 → ⊥
  bad6740  p = false≢true (cong lower p)
  cut6740 : Adequate {ℓ} ((op (op (var 0) (op (op (var 1) (var 2)) (var 3))) (op (var 2) (var 4))) , (var 2)) → ⊥
  cut6740  adequate = bad6740  (Adequate.valid adequate Two boolean env24)
  bad6741 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b0 b0) b1)) (bop b0 b0)) b1 → ⊥
  bad6741  p = false≢true (cong lower p)
  cut6741 : Adequate {ℓ} ((op (op (var 0) (op (op (var 1) (var 2)) (var 3))) (op (var 2) (var 4))) , (var 3)) → ⊥
  cut6741  adequate = bad6741  (Adequate.valid adequate Two boolean env17)
  bad6742 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b0 b0) b0)) (bop b0 b1)) b1 → ⊥
  bad6742  p = false≢true (cong lower p)
  cut6742 : Adequate {ℓ} ((op (op (var 0) (op (op (var 1) (var 2)) (var 3))) (op (var 2) (var 4))) , (var 4)) → ⊥
  cut6742  adequate = bad6742  (Adequate.valid adequate Two boolean env9)
  bad6743 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b0 b0) b0)) (bop b0 b0)) b1 → ⊥
  bad6743  p = false≢true (cong lower p)
  cut6743 : Adequate {ℓ} ((op (op (var 0) (op (op (var 1) (var 2)) (var 3))) (op (var 2) (var 4))) , (var 5)) → ⊥
  cut6743  adequate = bad6743  (Adequate.valid adequate Two boolean env18)
  holds6744 : (z0 z1 z2 z3 : A2) → (mul2 (mul2 z0 (mul2 (mul2 z1 z2) z3)) (mul2 z3 z0)) ≡ z0
  holds6744 z0 z1 z2 z3 = refl
  cut6744 : Adequate {ℓ} ((op (op (var 0) (op (op (var 1) (var 2)) (var 3))) (op (var 3) (var 0))) , (var 0)) → ⊥
  cut6744  = reject2 ((op (op (var 0) (op (op (var 1) (var 2)) (var 3))) (op (var 3) (var 0))) , (var 0)) (λ env → holds6744 (env 0) (env 1) (env 2) (env 3))
  bad6745 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b1 b0) b0)) (bop b0 b0)) b1 → ⊥
  bad6745  p = false≢true (cong lower p)
  cut6745 : Adequate {ℓ} ((op (op (var 0) (op (op (var 1) (var 2)) (var 3))) (op (var 3) (var 0))) , (var 1)) → ⊥
  cut6745  adequate = bad6745  (Adequate.valid adequate Two boolean env13)
  bad6746 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b0 b1) b0)) (bop b0 b0)) b1 → ⊥
  bad6746  p = false≢true (cong lower p)
  cut6746 : Adequate {ℓ} ((op (op (var 0) (op (op (var 1) (var 2)) (var 3))) (op (var 3) (var 0))) , (var 2)) → ⊥
  cut6746  adequate = bad6746  (Adequate.valid adequate Two boolean env8)
  bad6747 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b0 b0) b1)) (bop b1 b0)) b1 → ⊥
  bad6747  p = false≢true (cong lower p)
  cut6747 : Adequate {ℓ} ((op (op (var 0) (op (op (var 1) (var 2)) (var 3))) (op (var 3) (var 0))) , (var 3)) → ⊥
  cut6747  adequate = bad6747  (Adequate.valid adequate Two boolean env5)
  bad6748 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b0 b0) b0)) (bop b0 b0)) b1 → ⊥
  bad6748  p = false≢true (cong lower p)
  cut6748 : Adequate {ℓ} ((op (op (var 0) (op (op (var 1) (var 2)) (var 3))) (op (var 3) (var 0))) , (var 4)) → ⊥
  cut6748  adequate = bad6748  (Adequate.valid adequate Two boolean env9)
  bad6749 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b1 b0) b1)) (bop b1 b1)) b0 → ⊥
  bad6749  p = false≢true (sym (cong lower p))
  cut6749 : Adequate {ℓ} ((op (op (var 0) (op (op (var 1) (var 2)) (var 3))) (op (var 3) (var 1))) , (var 0)) → ⊥
  cut6749  adequate = bad6749  (Adequate.valid adequate Two boolean env14)
  bad6750 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b1 b0) b0)) (bop b0 b1)) b1 → ⊥
  bad6750  p = false≢true (cong lower p)
  cut6750 : Adequate {ℓ} ((op (op (var 0) (op (op (var 1) (var 2)) (var 3))) (op (var 3) (var 1))) , (var 1)) → ⊥
  cut6750  adequate = bad6750  (Adequate.valid adequate Two boolean env13)
  bad6751 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b0 b1) b0)) (bop b0 b0)) b1 → ⊥
  bad6751  p = false≢true (cong lower p)
  cut6751 : Adequate {ℓ} ((op (op (var 0) (op (op (var 1) (var 2)) (var 3))) (op (var 3) (var 1))) , (var 2)) → ⊥
  cut6751  adequate = bad6751  (Adequate.valid adequate Two boolean env8)
  bad6752 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b0 b0) b1)) (bop b1 b0)) b1 → ⊥
  bad6752  p = false≢true (cong lower p)
  cut6752 : Adequate {ℓ} ((op (op (var 0) (op (op (var 1) (var 2)) (var 3))) (op (var 3) (var 1))) , (var 3)) → ⊥
  cut6752  adequate = bad6752  (Adequate.valid adequate Two boolean env5)
  bad6753 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b0 b0) b0)) (bop b0 b0)) b1 → ⊥
  bad6753  p = false≢true (cong lower p)
  cut6753 : Adequate {ℓ} ((op (op (var 0) (op (op (var 1) (var 2)) (var 3))) (op (var 3) (var 1))) , (var 4)) → ⊥
  cut6753  adequate = bad6753  (Adequate.valid adequate Two boolean env9)
  bad6754 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b0 b1) b1)) (bop b1 b1)) b0 → ⊥
  bad6754  p = false≢true (sym (cong lower p))
  cut6754 : Adequate {ℓ} ((op (op (var 0) (op (op (var 1) (var 2)) (var 3))) (op (var 3) (var 2))) , (var 0)) → ⊥
  cut6754  adequate = bad6754  (Adequate.valid adequate Two boolean env7)
  bad6755 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b0 b1) b1)) (bop b1 b1)) b0 → ⊥
  bad6755  p = false≢true (sym (cong lower p))
  cut6755 : Adequate {ℓ} ((op (op (var 0) (op (op (var 1) (var 2)) (var 3))) (op (var 3) (var 2))) , (var 1)) → ⊥
  cut6755  adequate = bad6755  (Adequate.valid adequate Two boolean env7)
  bad6756 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b0 b1) b0)) (bop b0 b1)) b1 → ⊥
  bad6756  p = false≢true (cong lower p)
  cut6756 : Adequate {ℓ} ((op (op (var 0) (op (op (var 1) (var 2)) (var 3))) (op (var 3) (var 2))) , (var 2)) → ⊥
  cut6756  adequate = bad6756  (Adequate.valid adequate Two boolean env8)
  bad6757 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b0 b0) b1)) (bop b1 b0)) b1 → ⊥
  bad6757  p = false≢true (cong lower p)
  cut6757 : Adequate {ℓ} ((op (op (var 0) (op (op (var 1) (var 2)) (var 3))) (op (var 3) (var 2))) , (var 3)) → ⊥
  cut6757  adequate = bad6757  (Adequate.valid adequate Two boolean env5)
  bad6758 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b0 b0) b0)) (bop b0 b0)) b1 → ⊥
  bad6758  p = false≢true (cong lower p)
  cut6758 : Adequate {ℓ} ((op (op (var 0) (op (op (var 1) (var 2)) (var 3))) (op (var 3) (var 2))) , (var 4)) → ⊥
  cut6758  adequate = bad6758  (Adequate.valid adequate Two boolean env9)
  bad6759 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b0 b0) b1)) (bop b1 b1)) b0 → ⊥
  bad6759  p = false≢true (sym (cong lower p))
  cut6759 : Adequate {ℓ} ((op (op (var 0) (op (op (var 1) (var 2)) (var 3))) (op (var 3) (var 3))) , (var 0)) → ⊥
  cut6759  adequate = bad6759  (Adequate.valid adequate Two boolean env5)
  bad6760 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b0 b0) b1)) (bop b1 b1)) b0 → ⊥
  bad6760  p = false≢true (sym (cong lower p))
  cut6760 : Adequate {ℓ} ((op (op (var 0) (op (op (var 1) (var 2)) (var 3))) (op (var 3) (var 3))) , (var 1)) → ⊥
  cut6760  adequate = bad6760  (Adequate.valid adequate Two boolean env5)
  bad6761 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b0 b0) b1)) (bop b1 b1)) b0 → ⊥
  bad6761  p = false≢true (sym (cong lower p))
  cut6761 : Adequate {ℓ} ((op (op (var 0) (op (op (var 1) (var 2)) (var 3))) (op (var 3) (var 3))) , (var 2)) → ⊥
  cut6761  adequate = bad6761  (Adequate.valid adequate Two boolean env5)
  bad6762 : PathP (λ _ → Two) (bop (bop b1 (bop (bop b0 b0) b0)) (bop b0 b0)) b0 → ⊥
  bad6762  p = false≢true (sym (cong lower p))
  cut6762 : Adequate {ℓ} ((op (op (var 0) (op (op (var 1) (var 2)) (var 3))) (op (var 3) (var 3))) , (var 3)) → ⊥
  cut6762  adequate = bad6762  (Adequate.valid adequate Two boolean env15)
  bad6763 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b0 b0) b0)) (bop b0 b0)) b1 → ⊥
  bad6763  p = false≢true (cong lower p)
  cut6763 : Adequate {ℓ} ((op (op (var 0) (op (op (var 1) (var 2)) (var 3))) (op (var 3) (var 3))) , (var 4)) → ⊥
  cut6763  adequate = bad6763  (Adequate.valid adequate Two boolean env9)
  bad6764 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b0 b0) b1)) (bop b1 b1)) b0 → ⊥
  bad6764  p = false≢true (sym (cong lower p))
  cut6764 : Adequate {ℓ} ((op (op (var 0) (op (op (var 1) (var 2)) (var 3))) (op (var 3) (var 4))) , (var 0)) → ⊥
  cut6764  adequate = bad6764  (Adequate.valid adequate Two boolean env16)
  bad6765 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b0 b0) b1)) (bop b1 b1)) b0 → ⊥
  bad6765  p = false≢true (sym (cong lower p))
  cut6765 : Adequate {ℓ} ((op (op (var 0) (op (op (var 1) (var 2)) (var 3))) (op (var 3) (var 4))) , (var 1)) → ⊥
  cut6765  adequate = bad6765  (Adequate.valid adequate Two boolean env16)
  bad6766 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b0 b0) b1)) (bop b1 b1)) b0 → ⊥
  bad6766  p = false≢true (sym (cong lower p))
  cut6766 : Adequate {ℓ} ((op (op (var 0) (op (op (var 1) (var 2)) (var 3))) (op (var 3) (var 4))) , (var 2)) → ⊥
  cut6766  adequate = bad6766  (Adequate.valid adequate Two boolean env16)
  bad6767 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b0 b0) b1)) (bop b1 b0)) b1 → ⊥
  bad6767  p = false≢true (cong lower p)
  cut6767 : Adequate {ℓ} ((op (op (var 0) (op (op (var 1) (var 2)) (var 3))) (op (var 3) (var 4))) , (var 3)) → ⊥
  cut6767  adequate = bad6767  (Adequate.valid adequate Two boolean env17)
  bad6768 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b0 b0) b0)) (bop b0 b1)) b1 → ⊥
  bad6768  p = false≢true (cong lower p)
  cut6768 : Adequate {ℓ} ((op (op (var 0) (op (op (var 1) (var 2)) (var 3))) (op (var 3) (var 4))) , (var 4)) → ⊥
  cut6768  adequate = bad6768  (Adequate.valid adequate Two boolean env9)
  bad6769 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b0 b0) b0)) (bop b0 b0)) b1 → ⊥
  bad6769  p = false≢true (cong lower p)
  cut6769 : Adequate {ℓ} ((op (op (var 0) (op (op (var 1) (var 2)) (var 3))) (op (var 3) (var 4))) , (var 5)) → ⊥
  cut6769  adequate = bad6769  (Adequate.valid adequate Two boolean env18)
  bad6770 : PathP (λ _ → Two) (bop (bop b1 (bop (bop b0 b0) b1)) (bop b0 b1)) b1 → ⊥
  bad6770  p = false≢true (cong lower p)
  cut6770 : Adequate {ℓ} ((op (op (var 0) (op (op (var 1) (var 2)) (var 3))) (op (var 4) (var 0))) , (var 0)) → ⊥
  cut6770  adequate = bad6770  (Adequate.valid adequate Two boolean env22)
  bad6771 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b1 b0) b0)) (bop b0 b0)) b1 → ⊥
  bad6771  p = false≢true (cong lower p)
  cut6771 : Adequate {ℓ} ((op (op (var 0) (op (op (var 1) (var 2)) (var 3))) (op (var 4) (var 0))) , (var 1)) → ⊥
  cut6771  adequate = bad6771  (Adequate.valid adequate Two boolean env23)
  bad6772 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b0 b1) b0)) (bop b0 b0)) b1 → ⊥
  bad6772  p = false≢true (cong lower p)
  cut6772 : Adequate {ℓ} ((op (op (var 0) (op (op (var 1) (var 2)) (var 3))) (op (var 4) (var 0))) , (var 2)) → ⊥
  cut6772  adequate = bad6772  (Adequate.valid adequate Two boolean env24)
  bad6773 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b0 b0) b1)) (bop b0 b0)) b1 → ⊥
  bad6773  p = false≢true (cong lower p)
  cut6773 : Adequate {ℓ} ((op (op (var 0) (op (op (var 1) (var 2)) (var 3))) (op (var 4) (var 0))) , (var 3)) → ⊥
  cut6773  adequate = bad6773  (Adequate.valid adequate Two boolean env17)
  bad6774 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b0 b0) b0)) (bop b1 b0)) b1 → ⊥
  bad6774  p = false≢true (cong lower p)
  cut6774 : Adequate {ℓ} ((op (op (var 0) (op (op (var 1) (var 2)) (var 3))) (op (var 4) (var 0))) , (var 4)) → ⊥
  cut6774  adequate = bad6774  (Adequate.valid adequate Two boolean env9)
  bad6775 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b0 b0) b0)) (bop b0 b0)) b1 → ⊥
  bad6775  p = false≢true (cong lower p)
  cut6775 : Adequate {ℓ} ((op (op (var 0) (op (op (var 1) (var 2)) (var 3))) (op (var 4) (var 0))) , (var 5)) → ⊥
  cut6775  adequate = bad6775  (Adequate.valid adequate Two boolean env18)
  bad6776 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b1 b0) b0)) (bop b1 b1)) b0 → ⊥
  bad6776  p = false≢true (sym (cong lower p))
  cut6776 : Adequate {ℓ} ((op (op (var 0) (op (op (var 1) (var 2)) (var 3))) (op (var 4) (var 1))) , (var 0)) → ⊥
  cut6776  adequate = bad6776  (Adequate.valid adequate Two boolean env26)
  bad6777 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b1 b0) b0)) (bop b0 b1)) b1 → ⊥
  bad6777  p = false≢true (cong lower p)
  cut6777 : Adequate {ℓ} ((op (op (var 0) (op (op (var 1) (var 2)) (var 3))) (op (var 4) (var 1))) , (var 1)) → ⊥
  cut6777  adequate = bad6777  (Adequate.valid adequate Two boolean env23)
  bad6778 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b0 b1) b0)) (bop b0 b0)) b1 → ⊥
  bad6778  p = false≢true (cong lower p)
  cut6778 : Adequate {ℓ} ((op (op (var 0) (op (op (var 1) (var 2)) (var 3))) (op (var 4) (var 1))) , (var 2)) → ⊥
  cut6778  adequate = bad6778  (Adequate.valid adequate Two boolean env24)
  bad6779 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b0 b0) b1)) (bop b0 b0)) b1 → ⊥
  bad6779  p = false≢true (cong lower p)
  cut6779 : Adequate {ℓ} ((op (op (var 0) (op (op (var 1) (var 2)) (var 3))) (op (var 4) (var 1))) , (var 3)) → ⊥
  cut6779  adequate = bad6779  (Adequate.valid adequate Two boolean env17)
  bad6780 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b0 b0) b0)) (bop b1 b0)) b1 → ⊥
  bad6780  p = false≢true (cong lower p)
  cut6780 : Adequate {ℓ} ((op (op (var 0) (op (op (var 1) (var 2)) (var 3))) (op (var 4) (var 1))) , (var 4)) → ⊥
  cut6780  adequate = bad6780  (Adequate.valid adequate Two boolean env9)
  bad6781 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b0 b0) b0)) (bop b0 b0)) b1 → ⊥
  bad6781  p = false≢true (cong lower p)
  cut6781 : Adequate {ℓ} ((op (op (var 0) (op (op (var 1) (var 2)) (var 3))) (op (var 4) (var 1))) , (var 5)) → ⊥
  cut6781  adequate = bad6781  (Adequate.valid adequate Two boolean env18)
  bad6782 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b0 b1) b0)) (bop b1 b1)) b0 → ⊥
  bad6782  p = false≢true (sym (cong lower p))
  cut6782 : Adequate {ℓ} ((op (op (var 0) (op (op (var 1) (var 2)) (var 3))) (op (var 4) (var 2))) , (var 0)) → ⊥
  cut6782  adequate = bad6782  (Adequate.valid adequate Two boolean env27)
  bad6783 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b0 b1) b0)) (bop b1 b1)) b0 → ⊥
  bad6783  p = false≢true (sym (cong lower p))
  cut6783 : Adequate {ℓ} ((op (op (var 0) (op (op (var 1) (var 2)) (var 3))) (op (var 4) (var 2))) , (var 1)) → ⊥
  cut6783  adequate = bad6783  (Adequate.valid adequate Two boolean env27)
  bad6784 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b0 b1) b0)) (bop b0 b1)) b1 → ⊥
  bad6784  p = false≢true (cong lower p)
  cut6784 : Adequate {ℓ} ((op (op (var 0) (op (op (var 1) (var 2)) (var 3))) (op (var 4) (var 2))) , (var 2)) → ⊥
  cut6784  adequate = bad6784  (Adequate.valid adequate Two boolean env24)
  bad6785 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b0 b0) b1)) (bop b0 b0)) b1 → ⊥
  bad6785  p = false≢true (cong lower p)
  cut6785 : Adequate {ℓ} ((op (op (var 0) (op (op (var 1) (var 2)) (var 3))) (op (var 4) (var 2))) , (var 3)) → ⊥
  cut6785  adequate = bad6785  (Adequate.valid adequate Two boolean env17)
  bad6786 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b0 b0) b0)) (bop b1 b0)) b1 → ⊥
  bad6786  p = false≢true (cong lower p)
  cut6786 : Adequate {ℓ} ((op (op (var 0) (op (op (var 1) (var 2)) (var 3))) (op (var 4) (var 2))) , (var 4)) → ⊥
  cut6786  adequate = bad6786  (Adequate.valid adequate Two boolean env9)
  bad6787 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b0 b0) b0)) (bop b0 b0)) b1 → ⊥
  bad6787  p = false≢true (cong lower p)
  cut6787 : Adequate {ℓ} ((op (op (var 0) (op (op (var 1) (var 2)) (var 3))) (op (var 4) (var 2))) , (var 5)) → ⊥
  cut6787  adequate = bad6787  (Adequate.valid adequate Two boolean env18)
  bad6788 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b0 b0) b1)) (bop b1 b1)) b0 → ⊥
  bad6788  p = false≢true (sym (cong lower p))
  cut6788 : Adequate {ℓ} ((op (op (var 0) (op (op (var 1) (var 2)) (var 3))) (op (var 4) (var 3))) , (var 0)) → ⊥
  cut6788  adequate = bad6788  (Adequate.valid adequate Two boolean env16)
  bad6789 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b0 b0) b1)) (bop b1 b1)) b0 → ⊥
  bad6789  p = false≢true (sym (cong lower p))
  cut6789 : Adequate {ℓ} ((op (op (var 0) (op (op (var 1) (var 2)) (var 3))) (op (var 4) (var 3))) , (var 1)) → ⊥
  cut6789  adequate = bad6789  (Adequate.valid adequate Two boolean env16)
  bad6790 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b0 b0) b1)) (bop b1 b1)) b0 → ⊥
  bad6790  p = false≢true (sym (cong lower p))
  cut6790 : Adequate {ℓ} ((op (op (var 0) (op (op (var 1) (var 2)) (var 3))) (op (var 4) (var 3))) , (var 2)) → ⊥
  cut6790  adequate = bad6790  (Adequate.valid adequate Two boolean env16)
  bad6791 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b0 b0) b1)) (bop b0 b1)) b1 → ⊥
  bad6791  p = false≢true (cong lower p)
  cut6791 : Adequate {ℓ} ((op (op (var 0) (op (op (var 1) (var 2)) (var 3))) (op (var 4) (var 3))) , (var 3)) → ⊥
  cut6791  adequate = bad6791  (Adequate.valid adequate Two boolean env17)
  bad6792 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b0 b0) b0)) (bop b1 b0)) b1 → ⊥
  bad6792  p = false≢true (cong lower p)
  cut6792 : Adequate {ℓ} ((op (op (var 0) (op (op (var 1) (var 2)) (var 3))) (op (var 4) (var 3))) , (var 4)) → ⊥
  cut6792  adequate = bad6792  (Adequate.valid adequate Two boolean env9)
  bad6793 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b0 b0) b0)) (bop b0 b0)) b1 → ⊥
  bad6793  p = false≢true (cong lower p)
  cut6793 : Adequate {ℓ} ((op (op (var 0) (op (op (var 1) (var 2)) (var 3))) (op (var 4) (var 3))) , (var 5)) → ⊥
  cut6793  adequate = bad6793  (Adequate.valid adequate Two boolean env18)
  bad6794 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b0 b0) b0)) (bop b1 b1)) b0 → ⊥
  bad6794  p = false≢true (sym (cong lower p))
  cut6794 : Adequate {ℓ} ((op (op (var 0) (op (op (var 1) (var 2)) (var 3))) (op (var 4) (var 4))) , (var 0)) → ⊥
  cut6794  adequate = bad6794  (Adequate.valid adequate Two boolean env9)
  bad6795 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b0 b0) b0)) (bop b1 b1)) b0 → ⊥
  bad6795  p = false≢true (sym (cong lower p))
  cut6795 : Adequate {ℓ} ((op (op (var 0) (op (op (var 1) (var 2)) (var 3))) (op (var 4) (var 4))) , (var 1)) → ⊥
  cut6795  adequate = bad6795  (Adequate.valid adequate Two boolean env9)
  bad6796 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b0 b0) b0)) (bop b1 b1)) b0 → ⊥
  bad6796  p = false≢true (sym (cong lower p))
  cut6796 : Adequate {ℓ} ((op (op (var 0) (op (op (var 1) (var 2)) (var 3))) (op (var 4) (var 4))) , (var 2)) → ⊥
  cut6796  adequate = bad6796  (Adequate.valid adequate Two boolean env9)
  bad6797 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b0 b0) b0)) (bop b1 b1)) b0 → ⊥
  bad6797  p = false≢true (sym (cong lower p))
  cut6797 : Adequate {ℓ} ((op (op (var 0) (op (op (var 1) (var 2)) (var 3))) (op (var 4) (var 4))) , (var 3)) → ⊥
  cut6797  adequate = bad6797  (Adequate.valid adequate Two boolean env9)
  env28 : ℕ → Two
  env28 zero = b1
  env28 (suc zero) = b0
  env28 (suc (suc zero)) = b0
  env28 (suc (suc (suc zero))) = b0
  env28 (suc (suc (suc (suc zero)))) = b0
  env28 (suc (suc (suc (suc (suc rest))))) = b0
  bad6798 : PathP (λ _ → Two) (bop (bop b1 (bop (bop b0 b0) b0)) (bop b0 b0)) b0 → ⊥
  bad6798  p = false≢true (sym (cong lower p))
  cut6798 : Adequate {ℓ} ((op (op (var 0) (op (op (var 1) (var 2)) (var 3))) (op (var 4) (var 4))) , (var 4)) → ⊥
  cut6798  adequate = bad6798  (Adequate.valid adequate Two boolean env28)
  bad6799 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b0 b0) b0)) (bop b0 b0)) b1 → ⊥
  bad6799  p = false≢true (cong lower p)
  cut6799 : Adequate {ℓ} ((op (op (var 0) (op (op (var 1) (var 2)) (var 3))) (op (var 4) (var 4))) , (var 5)) → ⊥
  cut6799  adequate = bad6799  (Adequate.valid adequate Two boolean env18)
  env29 : ℕ → Two
  env29 zero = b0
  env29 (suc zero) = b0
  env29 (suc (suc zero)) = b0
  env29 (suc (suc (suc zero))) = b0
  env29 (suc (suc (suc (suc zero)))) = b1
  env29 (suc (suc (suc (suc (suc zero))))) = b1
  env29 (suc (suc (suc (suc (suc (suc rest)))))) = b0
  bad6800 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b0 b0) b0)) (bop b1 b1)) b0 → ⊥
  bad6800  p = false≢true (sym (cong lower p))
  cut6800 : Adequate {ℓ} ((op (op (var 0) (op (op (var 1) (var 2)) (var 3))) (op (var 4) (var 5))) , (var 0)) → ⊥
  cut6800  adequate = bad6800  (Adequate.valid adequate Two boolean env29)
  bad6801 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b0 b0) b0)) (bop b1 b1)) b0 → ⊥
  bad6801  p = false≢true (sym (cong lower p))
  cut6801 : Adequate {ℓ} ((op (op (var 0) (op (op (var 1) (var 2)) (var 3))) (op (var 4) (var 5))) , (var 1)) → ⊥
  cut6801  adequate = bad6801  (Adequate.valid adequate Two boolean env29)
  bad6802 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b0 b0) b0)) (bop b1 b1)) b0 → ⊥
  bad6802  p = false≢true (sym (cong lower p))
  cut6802 : Adequate {ℓ} ((op (op (var 0) (op (op (var 1) (var 2)) (var 3))) (op (var 4) (var 5))) , (var 2)) → ⊥
  cut6802  adequate = bad6802  (Adequate.valid adequate Two boolean env29)
  bad6803 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b0 b0) b0)) (bop b1 b1)) b0 → ⊥
  bad6803  p = false≢true (sym (cong lower p))
  cut6803 : Adequate {ℓ} ((op (op (var 0) (op (op (var 1) (var 2)) (var 3))) (op (var 4) (var 5))) , (var 3)) → ⊥
  cut6803  adequate = bad6803  (Adequate.valid adequate Two boolean env29)
  env30 : ℕ → Two
  env30 zero = b0
  env30 (suc zero) = b0
  env30 (suc (suc zero)) = b0
  env30 (suc (suc (suc zero))) = b0
  env30 (suc (suc (suc (suc zero)))) = b1
  env30 (suc (suc (suc (suc (suc zero))))) = b0
  env30 (suc (suc (suc (suc (suc (suc rest)))))) = b0
  bad6804 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b0 b0) b0)) (bop b1 b0)) b1 → ⊥
  bad6804  p = false≢true (cong lower p)
  cut6804 : Adequate {ℓ} ((op (op (var 0) (op (op (var 1) (var 2)) (var 3))) (op (var 4) (var 5))) , (var 4)) → ⊥
  cut6804  adequate = bad6804  (Adequate.valid adequate Two boolean env30)
  bad6805 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b0 b0) b0)) (bop b0 b1)) b1 → ⊥
  bad6805  p = false≢true (cong lower p)
  cut6805 : Adequate {ℓ} ((op (op (var 0) (op (op (var 1) (var 2)) (var 3))) (op (var 4) (var 5))) , (var 5)) → ⊥
  cut6805  adequate = bad6805  (Adequate.valid adequate Two boolean env18)
  env31 : ℕ → Two
  env31 zero = b0
  env31 (suc zero) = b0
  env31 (suc (suc zero)) = b0
  env31 (suc (suc (suc zero))) = b0
  env31 (suc (suc (suc (suc zero)))) = b0
  env31 (suc (suc (suc (suc (suc zero))))) = b0
  env31 (suc (suc (suc (suc (suc (suc zero)))))) = b1
  env31 (suc (suc (suc (suc (suc (suc (suc rest))))))) = b0
  bad6806 : PathP (λ _ → Two) (bop (bop b0 (bop (bop b0 b0) b0)) (bop b0 b0)) b1 → ⊥
  bad6806  p = false≢true (cong lower p)
  cut6806 : Adequate {ℓ} ((op (op (var 0) (op (op (var 1) (var 2)) (var 3))) (op (var 4) (var 5))) , (var 6)) → ⊥
  cut6806  adequate = bad6806  (Adequate.valid adequate Two boolean env31)
