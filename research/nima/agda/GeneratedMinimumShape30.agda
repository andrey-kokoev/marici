{-# OPTIONS --safe --cubical --guardedness #-}
module GeneratedMinimumShape30 where
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
  holds125 : (z0 z1 z2 z3 z4 : A2) → z0 ≡ (mul2 (mul2 (mul2 z0 z1) z2) (mul2 z3 z4))
  holds125 z0 z1 z2 z3 z4 = refl
  cut125 : (x2 x3 x4 x5 : ℕ) → Adequate {ℓ} ((var 0) , (op (op (op (var 0) (var x2)) (var x3)) (op (var x4) (var x5)))) → ⊥
  cut125 x2 x3 x4 x5 = reject2 ((var 0) , (op (op (op (var 0) (var x2)) (var x3)) (op (var x4) (var x5)))) (λ env → holds125 (env 0) (env x2) (env x3) (env x4) (env x5))
  holds126 : (z0 z1 z2 : A13) → z0 ≡ (mul13 (mul13 (mul13 z1 z0) z0) (mul13 z0 z2))
  holds126 m13c0 m13c0 m13c0 = refl
  holds126 m13c0 m13c0 m13c1 = refl
  holds126 m13c0 m13c0 m13c2 = refl
  holds126 m13c0 m13c0 m13c3 = refl
  holds126 m13c0 m13c1 m13c0 = refl
  holds126 m13c0 m13c1 m13c1 = refl
  holds126 m13c0 m13c1 m13c2 = refl
  holds126 m13c0 m13c1 m13c3 = refl
  holds126 m13c0 m13c2 m13c0 = refl
  holds126 m13c0 m13c2 m13c1 = refl
  holds126 m13c0 m13c2 m13c2 = refl
  holds126 m13c0 m13c2 m13c3 = refl
  holds126 m13c0 m13c3 m13c0 = refl
  holds126 m13c0 m13c3 m13c1 = refl
  holds126 m13c0 m13c3 m13c2 = refl
  holds126 m13c0 m13c3 m13c3 = refl
  holds126 m13c1 m13c0 m13c0 = refl
  holds126 m13c1 m13c0 m13c1 = refl
  holds126 m13c1 m13c0 m13c2 = refl
  holds126 m13c1 m13c0 m13c3 = refl
  holds126 m13c1 m13c1 m13c0 = refl
  holds126 m13c1 m13c1 m13c1 = refl
  holds126 m13c1 m13c1 m13c2 = refl
  holds126 m13c1 m13c1 m13c3 = refl
  holds126 m13c1 m13c2 m13c0 = refl
  holds126 m13c1 m13c2 m13c1 = refl
  holds126 m13c1 m13c2 m13c2 = refl
  holds126 m13c1 m13c2 m13c3 = refl
  holds126 m13c1 m13c3 m13c0 = refl
  holds126 m13c1 m13c3 m13c1 = refl
  holds126 m13c1 m13c3 m13c2 = refl
  holds126 m13c1 m13c3 m13c3 = refl
  holds126 m13c2 m13c0 m13c0 = refl
  holds126 m13c2 m13c0 m13c1 = refl
  holds126 m13c2 m13c0 m13c2 = refl
  holds126 m13c2 m13c0 m13c3 = refl
  holds126 m13c2 m13c1 m13c0 = refl
  holds126 m13c2 m13c1 m13c1 = refl
  holds126 m13c2 m13c1 m13c2 = refl
  holds126 m13c2 m13c1 m13c3 = refl
  holds126 m13c2 m13c2 m13c0 = refl
  holds126 m13c2 m13c2 m13c1 = refl
  holds126 m13c2 m13c2 m13c2 = refl
  holds126 m13c2 m13c2 m13c3 = refl
  holds126 m13c2 m13c3 m13c0 = refl
  holds126 m13c2 m13c3 m13c1 = refl
  holds126 m13c2 m13c3 m13c2 = refl
  holds126 m13c2 m13c3 m13c3 = refl
  holds126 m13c3 m13c0 m13c0 = refl
  holds126 m13c3 m13c0 m13c1 = refl
  holds126 m13c3 m13c0 m13c2 = refl
  holds126 m13c3 m13c0 m13c3 = refl
  holds126 m13c3 m13c1 m13c0 = refl
  holds126 m13c3 m13c1 m13c1 = refl
  holds126 m13c3 m13c1 m13c2 = refl
  holds126 m13c3 m13c1 m13c3 = refl
  holds126 m13c3 m13c2 m13c0 = refl
  holds126 m13c3 m13c2 m13c1 = refl
  holds126 m13c3 m13c2 m13c2 = refl
  holds126 m13c3 m13c2 m13c3 = refl
  holds126 m13c3 m13c3 m13c0 = refl
  holds126 m13c3 m13c3 m13c1 = refl
  holds126 m13c3 m13c3 m13c2 = refl
  holds126 m13c3 m13c3 m13c3 = refl
  cut126 : (x5 : ℕ) → Adequate {ℓ} ((var 0) , (op (op (op (var 1) (var 0)) (var 0)) (op (var 0) (var x5)))) → ⊥
  cut126 x5 = reject13 ((var 0) , (op (op (op (var 1) (var 0)) (var 0)) (op (var 0) (var x5)))) (λ env → holds126 (env 0) (env 1) (env x5))
  holds127 : (z0 z1 : A3) → z0 ≡ (mul3 (mul3 (mul3 z1 z0) z0) (mul3 z1 z0))
  holds127 z0 z1 = refl
  cut127 : Adequate {ℓ} ((var 0) , (op (op (op (var 1) (var 0)) (var 0)) (op (var 1) (var 0)))) → ⊥
  cut127  = reject3 ((var 0) , (op (op (op (var 1) (var 0)) (var 0)) (op (var 1) (var 0)))) (λ env → holds127 (env 0) (env 1))
  env0 : ℕ → Two
  env0 zero = b0
  env0 (suc zero) = b1
  env0 (suc (suc rest)) = b0
  bad128 : PathP (λ _ → Two) b0 (bop (bop (bop b1 b0) b0) (bop b1 b1)) → ⊥
  bad128  p = false≢true (cong lower p)
  cut128 : Adequate {ℓ} ((var 0) , (op (op (op (var 1) (var 0)) (var 0)) (op (var 1) (var 1)))) → ⊥
  cut128  adequate = bad128  (Adequate.valid adequate Two boolean env0)
  env1 : ℕ → Two
  env1 zero = b0
  env1 (suc zero) = b1
  env1 (suc (suc zero)) = b1
  env1 (suc (suc (suc rest))) = b0
  bad129 : PathP (λ _ → Two) b0 (bop (bop (bop b1 b0) b0) (bop b1 b1)) → ⊥
  bad129  p = false≢true (cong lower p)
  cut129 : Adequate {ℓ} ((var 0) , (op (op (op (var 1) (var 0)) (var 0)) (op (var 1) (var 2)))) → ⊥
  cut129  adequate = bad129  (Adequate.valid adequate Two boolean env1)
  env2 : ℕ → Two
  env2 zero = b1
  env2 (suc zero) = b1
  env2 (suc (suc zero)) = b0
  env2 (suc (suc (suc rest))) = b0
  bad130 : (z3 : Two) → PathP (λ _ → Two) b1 (bop (bop (bop b1 b1) b1) (bop b0 z3)) → ⊥
  bad130 z3 p = false≢true (sym (cong lower p))
  cut130 : (x5 : ℕ) → Adequate {ℓ} ((var 0) , (op (op (op (var 1) (var 0)) (var 0)) (op (var 2) (var x5)))) → ⊥
  cut130 x5 adequate = bad130 (env2 x5) (Adequate.valid adequate Two boolean env2)
  bad131 : (z2 z3 : Two) → PathP (λ _ → Two) b0 (bop (bop (bop b1 b0) b1) (bop z2 z3)) → ⊥
  bad131 z2 z3 p = false≢true (cong lower p)
  cut131 : (x4 x5 : ℕ) → Adequate {ℓ} ((var 0) , (op (op (op (var 1) (var 0)) (var 1)) (op (var x4) (var x5)))) → ⊥
  cut131 x4 x5 adequate = bad131 (env0 x4) (env0 x5) (Adequate.valid adequate Two boolean env0)
  env3 : ℕ → Two
  env3 zero = b0
  env3 (suc zero) = b0
  env3 (suc (suc zero)) = b1
  env3 (suc (suc (suc rest))) = b0
  bad132 : (z3 z4 : Two) → PathP (λ _ → Two) b0 (bop (bop (bop b0 b0) b1) (bop z3 z4)) → ⊥
  bad132 z3 z4 p = false≢true (cong lower p)
  cut132 : (x4 x5 : ℕ) → Adequate {ℓ} ((var 0) , (op (op (op (var 1) (var 0)) (var 2)) (op (var x4) (var x5)))) → ⊥
  cut132 x4 x5 adequate = bad132 (env3 x4) (env3 x5) (Adequate.valid adequate Two boolean env3)
  holds133 : (z0 z1 z2 : A13) → z0 ≡ (mul13 (mul13 (mul13 z1 z1) z0) (mul13 z0 z2))
  holds133 m13c0 m13c0 m13c0 = refl
  holds133 m13c0 m13c0 m13c1 = refl
  holds133 m13c0 m13c0 m13c2 = refl
  holds133 m13c0 m13c0 m13c3 = refl
  holds133 m13c0 m13c1 m13c0 = refl
  holds133 m13c0 m13c1 m13c1 = refl
  holds133 m13c0 m13c1 m13c2 = refl
  holds133 m13c0 m13c1 m13c3 = refl
  holds133 m13c0 m13c2 m13c0 = refl
  holds133 m13c0 m13c2 m13c1 = refl
  holds133 m13c0 m13c2 m13c2 = refl
  holds133 m13c0 m13c2 m13c3 = refl
  holds133 m13c0 m13c3 m13c0 = refl
  holds133 m13c0 m13c3 m13c1 = refl
  holds133 m13c0 m13c3 m13c2 = refl
  holds133 m13c0 m13c3 m13c3 = refl
  holds133 m13c1 m13c0 m13c0 = refl
  holds133 m13c1 m13c0 m13c1 = refl
  holds133 m13c1 m13c0 m13c2 = refl
  holds133 m13c1 m13c0 m13c3 = refl
  holds133 m13c1 m13c1 m13c0 = refl
  holds133 m13c1 m13c1 m13c1 = refl
  holds133 m13c1 m13c1 m13c2 = refl
  holds133 m13c1 m13c1 m13c3 = refl
  holds133 m13c1 m13c2 m13c0 = refl
  holds133 m13c1 m13c2 m13c1 = refl
  holds133 m13c1 m13c2 m13c2 = refl
  holds133 m13c1 m13c2 m13c3 = refl
  holds133 m13c1 m13c3 m13c0 = refl
  holds133 m13c1 m13c3 m13c1 = refl
  holds133 m13c1 m13c3 m13c2 = refl
  holds133 m13c1 m13c3 m13c3 = refl
  holds133 m13c2 m13c0 m13c0 = refl
  holds133 m13c2 m13c0 m13c1 = refl
  holds133 m13c2 m13c0 m13c2 = refl
  holds133 m13c2 m13c0 m13c3 = refl
  holds133 m13c2 m13c1 m13c0 = refl
  holds133 m13c2 m13c1 m13c1 = refl
  holds133 m13c2 m13c1 m13c2 = refl
  holds133 m13c2 m13c1 m13c3 = refl
  holds133 m13c2 m13c2 m13c0 = refl
  holds133 m13c2 m13c2 m13c1 = refl
  holds133 m13c2 m13c2 m13c2 = refl
  holds133 m13c2 m13c2 m13c3 = refl
  holds133 m13c2 m13c3 m13c0 = refl
  holds133 m13c2 m13c3 m13c1 = refl
  holds133 m13c2 m13c3 m13c2 = refl
  holds133 m13c2 m13c3 m13c3 = refl
  holds133 m13c3 m13c0 m13c0 = refl
  holds133 m13c3 m13c0 m13c1 = refl
  holds133 m13c3 m13c0 m13c2 = refl
  holds133 m13c3 m13c0 m13c3 = refl
  holds133 m13c3 m13c1 m13c0 = refl
  holds133 m13c3 m13c1 m13c1 = refl
  holds133 m13c3 m13c1 m13c2 = refl
  holds133 m13c3 m13c1 m13c3 = refl
  holds133 m13c3 m13c2 m13c0 = refl
  holds133 m13c3 m13c2 m13c1 = refl
  holds133 m13c3 m13c2 m13c2 = refl
  holds133 m13c3 m13c2 m13c3 = refl
  holds133 m13c3 m13c3 m13c0 = refl
  holds133 m13c3 m13c3 m13c1 = refl
  holds133 m13c3 m13c3 m13c2 = refl
  holds133 m13c3 m13c3 m13c3 = refl
  cut133 : (x5 : ℕ) → Adequate {ℓ} ((var 0) , (op (op (op (var 1) (var 1)) (var 0)) (op (var 0) (var x5)))) → ⊥
  cut133 x5 = reject13 ((var 0) , (op (op (op (var 1) (var 1)) (var 0)) (op (var 0) (var x5)))) (λ env → holds133 (env 0) (env 1) (env x5))
  holds134 : (z0 z1 : A3) → z0 ≡ (mul3 (mul3 (mul3 z1 z1) z0) (mul3 z1 z0))
  holds134 z0 z1 = refl
  cut134 : Adequate {ℓ} ((var 0) , (op (op (op (var 1) (var 1)) (var 0)) (op (var 1) (var 0)))) → ⊥
  cut134  = reject3 ((var 0) , (op (op (op (var 1) (var 1)) (var 0)) (op (var 1) (var 0)))) (λ env → holds134 (env 0) (env 1))
  bad135 : PathP (λ _ → Two) b0 (bop (bop (bop b1 b1) b0) (bop b1 b1)) → ⊥
  bad135  p = false≢true (cong lower p)
  cut135 : Adequate {ℓ} ((var 0) , (op (op (op (var 1) (var 1)) (var 0)) (op (var 1) (var 1)))) → ⊥
  cut135  adequate = bad135  (Adequate.valid adequate Two boolean env0)
  bad136 : PathP (λ _ → Two) b0 (bop (bop (bop b1 b1) b0) (bop b1 b1)) → ⊥
  bad136  p = false≢true (cong lower p)
  cut136 : Adequate {ℓ} ((var 0) , (op (op (op (var 1) (var 1)) (var 0)) (op (var 1) (var 2)))) → ⊥
  cut136  adequate = bad136  (Adequate.valid adequate Two boolean env1)
  bad137 : (z3 : Two) → PathP (λ _ → Two) b1 (bop (bop (bop b1 b1) b1) (bop b0 z3)) → ⊥
  bad137 z3 p = false≢true (sym (cong lower p))
  cut137 : (x5 : ℕ) → Adequate {ℓ} ((var 0) , (op (op (op (var 1) (var 1)) (var 0)) (op (var 2) (var x5)))) → ⊥
  cut137 x5 adequate = bad137 (env2 x5) (Adequate.valid adequate Two boolean env2)
  holds138 : (z0 z1 : A3) → z0 ≡ (mul3 (mul3 (mul3 z1 z1) z1) (mul3 z0 z0))
  holds138 z0 z1 = refl
  cut138 : Adequate {ℓ} ((var 0) , (op (op (op (var 1) (var 1)) (var 1)) (op (var 0) (var 0)))) → ⊥
  cut138  = reject3 ((var 0) , (op (op (op (var 1) (var 1)) (var 1)) (op (var 0) (var 0)))) (λ env → holds138 (env 0) (env 1))
  env4 : ℕ → Two
  env4 zero = b1
  env4 (suc zero) = b0
  env4 (suc (suc rest)) = b0
  bad139 : PathP (λ _ → Two) b1 (bop (bop (bop b0 b0) b0) (bop b1 b0)) → ⊥
  bad139  p = false≢true (sym (cong lower p))
  cut139 : Adequate {ℓ} ((var 0) , (op (op (op (var 1) (var 1)) (var 1)) (op (var 0) (var 1)))) → ⊥
  cut139  adequate = bad139  (Adequate.valid adequate Two boolean env4)
  env5 : ℕ → Two
  env5 zero = b1
  env5 (suc zero) = b0
  env5 (suc (suc zero)) = b0
  env5 (suc (suc (suc rest))) = b0
  bad140 : PathP (λ _ → Two) b1 (bop (bop (bop b0 b0) b0) (bop b1 b0)) → ⊥
  bad140  p = false≢true (sym (cong lower p))
  cut140 : Adequate {ℓ} ((var 0) , (op (op (op (var 1) (var 1)) (var 1)) (op (var 0) (var 2)))) → ⊥
  cut140  adequate = bad140  (Adequate.valid adequate Two boolean env5)
  bad141 : (z2 : Two) → PathP (λ _ → Two) b1 (bop (bop (bop b0 b0) b0) (bop b0 z2)) → ⊥
  bad141 z2 p = false≢true (sym (cong lower p))
  cut141 : (x5 : ℕ) → Adequate {ℓ} ((var 0) , (op (op (op (var 1) (var 1)) (var 1)) (op (var 1) (var x5)))) → ⊥
  cut141 x5 adequate = bad141 (env4 x5) (Adequate.valid adequate Two boolean env4)
  bad142 : (z3 : Two) → PathP (λ _ → Two) b1 (bop (bop (bop b0 b0) b0) (bop b0 z3)) → ⊥
  bad142 z3 p = false≢true (sym (cong lower p))
  cut142 : (x5 : ℕ) → Adequate {ℓ} ((var 0) , (op (op (op (var 1) (var 1)) (var 1)) (op (var 2) (var x5)))) → ⊥
  cut142 x5 adequate = bad142 (env5 x5) (Adequate.valid adequate Two boolean env5)
  bad143 : (z3 z4 : Two) → PathP (λ _ → Two) b0 (bop (bop (bop b0 b0) b1) (bop z3 z4)) → ⊥
  bad143 z3 z4 p = false≢true (cong lower p)
  cut143 : (x4 x5 : ℕ) → Adequate {ℓ} ((var 0) , (op (op (op (var 1) (var 1)) (var 2)) (op (var x4) (var x5)))) → ⊥
  cut143 x4 x5 adequate = bad143 (env3 x4) (env3 x5) (Adequate.valid adequate Two boolean env3)
  holds144 : (z0 z1 z2 z3 : A13) → z0 ≡ (mul13 (mul13 (mul13 z1 z2) z0) (mul13 z0 z3))
  holds144 m13c0 m13c0 m13c0 m13c0 = refl
  holds144 m13c0 m13c0 m13c0 m13c1 = refl
  holds144 m13c0 m13c0 m13c0 m13c2 = refl
  holds144 m13c0 m13c0 m13c0 m13c3 = refl
  holds144 m13c0 m13c0 m13c1 m13c0 = refl
  holds144 m13c0 m13c0 m13c1 m13c1 = refl
  holds144 m13c0 m13c0 m13c1 m13c2 = refl
  holds144 m13c0 m13c0 m13c1 m13c3 = refl
  holds144 m13c0 m13c0 m13c2 m13c0 = refl
  holds144 m13c0 m13c0 m13c2 m13c1 = refl
  holds144 m13c0 m13c0 m13c2 m13c2 = refl
  holds144 m13c0 m13c0 m13c2 m13c3 = refl
  holds144 m13c0 m13c0 m13c3 m13c0 = refl
  holds144 m13c0 m13c0 m13c3 m13c1 = refl
  holds144 m13c0 m13c0 m13c3 m13c2 = refl
  holds144 m13c0 m13c0 m13c3 m13c3 = refl
  holds144 m13c0 m13c1 m13c0 m13c0 = refl
  holds144 m13c0 m13c1 m13c0 m13c1 = refl
  holds144 m13c0 m13c1 m13c0 m13c2 = refl
  holds144 m13c0 m13c1 m13c0 m13c3 = refl
  holds144 m13c0 m13c1 m13c1 m13c0 = refl
  holds144 m13c0 m13c1 m13c1 m13c1 = refl
  holds144 m13c0 m13c1 m13c1 m13c2 = refl
  holds144 m13c0 m13c1 m13c1 m13c3 = refl
  holds144 m13c0 m13c1 m13c2 m13c0 = refl
  holds144 m13c0 m13c1 m13c2 m13c1 = refl
  holds144 m13c0 m13c1 m13c2 m13c2 = refl
  holds144 m13c0 m13c1 m13c2 m13c3 = refl
  holds144 m13c0 m13c1 m13c3 m13c0 = refl
  holds144 m13c0 m13c1 m13c3 m13c1 = refl
  holds144 m13c0 m13c1 m13c3 m13c2 = refl
  holds144 m13c0 m13c1 m13c3 m13c3 = refl
  holds144 m13c0 m13c2 m13c0 m13c0 = refl
  holds144 m13c0 m13c2 m13c0 m13c1 = refl
  holds144 m13c0 m13c2 m13c0 m13c2 = refl
  holds144 m13c0 m13c2 m13c0 m13c3 = refl
  holds144 m13c0 m13c2 m13c1 m13c0 = refl
  holds144 m13c0 m13c2 m13c1 m13c1 = refl
  holds144 m13c0 m13c2 m13c1 m13c2 = refl
  holds144 m13c0 m13c2 m13c1 m13c3 = refl
  holds144 m13c0 m13c2 m13c2 m13c0 = refl
  holds144 m13c0 m13c2 m13c2 m13c1 = refl
  holds144 m13c0 m13c2 m13c2 m13c2 = refl
  holds144 m13c0 m13c2 m13c2 m13c3 = refl
  holds144 m13c0 m13c2 m13c3 m13c0 = refl
  holds144 m13c0 m13c2 m13c3 m13c1 = refl
  holds144 m13c0 m13c2 m13c3 m13c2 = refl
  holds144 m13c0 m13c2 m13c3 m13c3 = refl
  holds144 m13c0 m13c3 m13c0 m13c0 = refl
  holds144 m13c0 m13c3 m13c0 m13c1 = refl
  holds144 m13c0 m13c3 m13c0 m13c2 = refl
  holds144 m13c0 m13c3 m13c0 m13c3 = refl
  holds144 m13c0 m13c3 m13c1 m13c0 = refl
  holds144 m13c0 m13c3 m13c1 m13c1 = refl
  holds144 m13c0 m13c3 m13c1 m13c2 = refl
  holds144 m13c0 m13c3 m13c1 m13c3 = refl
  holds144 m13c0 m13c3 m13c2 m13c0 = refl
  holds144 m13c0 m13c3 m13c2 m13c1 = refl
  holds144 m13c0 m13c3 m13c2 m13c2 = refl
  holds144 m13c0 m13c3 m13c2 m13c3 = refl
  holds144 m13c0 m13c3 m13c3 m13c0 = refl
  holds144 m13c0 m13c3 m13c3 m13c1 = refl
  holds144 m13c0 m13c3 m13c3 m13c2 = refl
  holds144 m13c0 m13c3 m13c3 m13c3 = refl
  holds144 m13c1 m13c0 m13c0 m13c0 = refl
  holds144 m13c1 m13c0 m13c0 m13c1 = refl
  holds144 m13c1 m13c0 m13c0 m13c2 = refl
  holds144 m13c1 m13c0 m13c0 m13c3 = refl
  holds144 m13c1 m13c0 m13c1 m13c0 = refl
  holds144 m13c1 m13c0 m13c1 m13c1 = refl
  holds144 m13c1 m13c0 m13c1 m13c2 = refl
  holds144 m13c1 m13c0 m13c1 m13c3 = refl
  holds144 m13c1 m13c0 m13c2 m13c0 = refl
  holds144 m13c1 m13c0 m13c2 m13c1 = refl
  holds144 m13c1 m13c0 m13c2 m13c2 = refl
  holds144 m13c1 m13c0 m13c2 m13c3 = refl
  holds144 m13c1 m13c0 m13c3 m13c0 = refl
  holds144 m13c1 m13c0 m13c3 m13c1 = refl
  holds144 m13c1 m13c0 m13c3 m13c2 = refl
  holds144 m13c1 m13c0 m13c3 m13c3 = refl
  holds144 m13c1 m13c1 m13c0 m13c0 = refl
  holds144 m13c1 m13c1 m13c0 m13c1 = refl
  holds144 m13c1 m13c1 m13c0 m13c2 = refl
  holds144 m13c1 m13c1 m13c0 m13c3 = refl
  holds144 m13c1 m13c1 m13c1 m13c0 = refl
  holds144 m13c1 m13c1 m13c1 m13c1 = refl
  holds144 m13c1 m13c1 m13c1 m13c2 = refl
  holds144 m13c1 m13c1 m13c1 m13c3 = refl
  holds144 m13c1 m13c1 m13c2 m13c0 = refl
  holds144 m13c1 m13c1 m13c2 m13c1 = refl
  holds144 m13c1 m13c1 m13c2 m13c2 = refl
  holds144 m13c1 m13c1 m13c2 m13c3 = refl
  holds144 m13c1 m13c1 m13c3 m13c0 = refl
  holds144 m13c1 m13c1 m13c3 m13c1 = refl
  holds144 m13c1 m13c1 m13c3 m13c2 = refl
  holds144 m13c1 m13c1 m13c3 m13c3 = refl
  holds144 m13c1 m13c2 m13c0 m13c0 = refl
  holds144 m13c1 m13c2 m13c0 m13c1 = refl
  holds144 m13c1 m13c2 m13c0 m13c2 = refl
  holds144 m13c1 m13c2 m13c0 m13c3 = refl
  holds144 m13c1 m13c2 m13c1 m13c0 = refl
  holds144 m13c1 m13c2 m13c1 m13c1 = refl
  holds144 m13c1 m13c2 m13c1 m13c2 = refl
  holds144 m13c1 m13c2 m13c1 m13c3 = refl
  holds144 m13c1 m13c2 m13c2 m13c0 = refl
  holds144 m13c1 m13c2 m13c2 m13c1 = refl
  holds144 m13c1 m13c2 m13c2 m13c2 = refl
  holds144 m13c1 m13c2 m13c2 m13c3 = refl
  holds144 m13c1 m13c2 m13c3 m13c0 = refl
  holds144 m13c1 m13c2 m13c3 m13c1 = refl
  holds144 m13c1 m13c2 m13c3 m13c2 = refl
  holds144 m13c1 m13c2 m13c3 m13c3 = refl
  holds144 m13c1 m13c3 m13c0 m13c0 = refl
  holds144 m13c1 m13c3 m13c0 m13c1 = refl
  holds144 m13c1 m13c3 m13c0 m13c2 = refl
  holds144 m13c1 m13c3 m13c0 m13c3 = refl
  holds144 m13c1 m13c3 m13c1 m13c0 = refl
  holds144 m13c1 m13c3 m13c1 m13c1 = refl
  holds144 m13c1 m13c3 m13c1 m13c2 = refl
  holds144 m13c1 m13c3 m13c1 m13c3 = refl
  holds144 m13c1 m13c3 m13c2 m13c0 = refl
  holds144 m13c1 m13c3 m13c2 m13c1 = refl
  holds144 m13c1 m13c3 m13c2 m13c2 = refl
  holds144 m13c1 m13c3 m13c2 m13c3 = refl
  holds144 m13c1 m13c3 m13c3 m13c0 = refl
  holds144 m13c1 m13c3 m13c3 m13c1 = refl
  holds144 m13c1 m13c3 m13c3 m13c2 = refl
  holds144 m13c1 m13c3 m13c3 m13c3 = refl
  holds144 m13c2 m13c0 m13c0 m13c0 = refl
  holds144 m13c2 m13c0 m13c0 m13c1 = refl
  holds144 m13c2 m13c0 m13c0 m13c2 = refl
  holds144 m13c2 m13c0 m13c0 m13c3 = refl
  holds144 m13c2 m13c0 m13c1 m13c0 = refl
  holds144 m13c2 m13c0 m13c1 m13c1 = refl
  holds144 m13c2 m13c0 m13c1 m13c2 = refl
  holds144 m13c2 m13c0 m13c1 m13c3 = refl
  holds144 m13c2 m13c0 m13c2 m13c0 = refl
  holds144 m13c2 m13c0 m13c2 m13c1 = refl
  holds144 m13c2 m13c0 m13c2 m13c2 = refl
  holds144 m13c2 m13c0 m13c2 m13c3 = refl
  holds144 m13c2 m13c0 m13c3 m13c0 = refl
  holds144 m13c2 m13c0 m13c3 m13c1 = refl
  holds144 m13c2 m13c0 m13c3 m13c2 = refl
  holds144 m13c2 m13c0 m13c3 m13c3 = refl
  holds144 m13c2 m13c1 m13c0 m13c0 = refl
  holds144 m13c2 m13c1 m13c0 m13c1 = refl
  holds144 m13c2 m13c1 m13c0 m13c2 = refl
  holds144 m13c2 m13c1 m13c0 m13c3 = refl
  holds144 m13c2 m13c1 m13c1 m13c0 = refl
  holds144 m13c2 m13c1 m13c1 m13c1 = refl
  holds144 m13c2 m13c1 m13c1 m13c2 = refl
  holds144 m13c2 m13c1 m13c1 m13c3 = refl
  holds144 m13c2 m13c1 m13c2 m13c0 = refl
  holds144 m13c2 m13c1 m13c2 m13c1 = refl
  holds144 m13c2 m13c1 m13c2 m13c2 = refl
  holds144 m13c2 m13c1 m13c2 m13c3 = refl
  holds144 m13c2 m13c1 m13c3 m13c0 = refl
  holds144 m13c2 m13c1 m13c3 m13c1 = refl
  holds144 m13c2 m13c1 m13c3 m13c2 = refl
  holds144 m13c2 m13c1 m13c3 m13c3 = refl
  holds144 m13c2 m13c2 m13c0 m13c0 = refl
  holds144 m13c2 m13c2 m13c0 m13c1 = refl
  holds144 m13c2 m13c2 m13c0 m13c2 = refl
  holds144 m13c2 m13c2 m13c0 m13c3 = refl
  holds144 m13c2 m13c2 m13c1 m13c0 = refl
  holds144 m13c2 m13c2 m13c1 m13c1 = refl
  holds144 m13c2 m13c2 m13c1 m13c2 = refl
  holds144 m13c2 m13c2 m13c1 m13c3 = refl
  holds144 m13c2 m13c2 m13c2 m13c0 = refl
  holds144 m13c2 m13c2 m13c2 m13c1 = refl
  holds144 m13c2 m13c2 m13c2 m13c2 = refl
  holds144 m13c2 m13c2 m13c2 m13c3 = refl
  holds144 m13c2 m13c2 m13c3 m13c0 = refl
  holds144 m13c2 m13c2 m13c3 m13c1 = refl
  holds144 m13c2 m13c2 m13c3 m13c2 = refl
  holds144 m13c2 m13c2 m13c3 m13c3 = refl
  holds144 m13c2 m13c3 m13c0 m13c0 = refl
  holds144 m13c2 m13c3 m13c0 m13c1 = refl
  holds144 m13c2 m13c3 m13c0 m13c2 = refl
  holds144 m13c2 m13c3 m13c0 m13c3 = refl
  holds144 m13c2 m13c3 m13c1 m13c0 = refl
  holds144 m13c2 m13c3 m13c1 m13c1 = refl
  holds144 m13c2 m13c3 m13c1 m13c2 = refl
  holds144 m13c2 m13c3 m13c1 m13c3 = refl
  holds144 m13c2 m13c3 m13c2 m13c0 = refl
  holds144 m13c2 m13c3 m13c2 m13c1 = refl
  holds144 m13c2 m13c3 m13c2 m13c2 = refl
  holds144 m13c2 m13c3 m13c2 m13c3 = refl
  holds144 m13c2 m13c3 m13c3 m13c0 = refl
  holds144 m13c2 m13c3 m13c3 m13c1 = refl
  holds144 m13c2 m13c3 m13c3 m13c2 = refl
  holds144 m13c2 m13c3 m13c3 m13c3 = refl
  holds144 m13c3 m13c0 m13c0 m13c0 = refl
  holds144 m13c3 m13c0 m13c0 m13c1 = refl
  holds144 m13c3 m13c0 m13c0 m13c2 = refl
  holds144 m13c3 m13c0 m13c0 m13c3 = refl
  holds144 m13c3 m13c0 m13c1 m13c0 = refl
  holds144 m13c3 m13c0 m13c1 m13c1 = refl
  holds144 m13c3 m13c0 m13c1 m13c2 = refl
  holds144 m13c3 m13c0 m13c1 m13c3 = refl
  holds144 m13c3 m13c0 m13c2 m13c0 = refl
  holds144 m13c3 m13c0 m13c2 m13c1 = refl
  holds144 m13c3 m13c0 m13c2 m13c2 = refl
  holds144 m13c3 m13c0 m13c2 m13c3 = refl
  holds144 m13c3 m13c0 m13c3 m13c0 = refl
  holds144 m13c3 m13c0 m13c3 m13c1 = refl
  holds144 m13c3 m13c0 m13c3 m13c2 = refl
  holds144 m13c3 m13c0 m13c3 m13c3 = refl
  holds144 m13c3 m13c1 m13c0 m13c0 = refl
  holds144 m13c3 m13c1 m13c0 m13c1 = refl
  holds144 m13c3 m13c1 m13c0 m13c2 = refl
  holds144 m13c3 m13c1 m13c0 m13c3 = refl
  holds144 m13c3 m13c1 m13c1 m13c0 = refl
  holds144 m13c3 m13c1 m13c1 m13c1 = refl
  holds144 m13c3 m13c1 m13c1 m13c2 = refl
  holds144 m13c3 m13c1 m13c1 m13c3 = refl
  holds144 m13c3 m13c1 m13c2 m13c0 = refl
  holds144 m13c3 m13c1 m13c2 m13c1 = refl
  holds144 m13c3 m13c1 m13c2 m13c2 = refl
  holds144 m13c3 m13c1 m13c2 m13c3 = refl
  holds144 m13c3 m13c1 m13c3 m13c0 = refl
  holds144 m13c3 m13c1 m13c3 m13c1 = refl
  holds144 m13c3 m13c1 m13c3 m13c2 = refl
  holds144 m13c3 m13c1 m13c3 m13c3 = refl
  holds144 m13c3 m13c2 m13c0 m13c0 = refl
  holds144 m13c3 m13c2 m13c0 m13c1 = refl
  holds144 m13c3 m13c2 m13c0 m13c2 = refl
  holds144 m13c3 m13c2 m13c0 m13c3 = refl
  holds144 m13c3 m13c2 m13c1 m13c0 = refl
  holds144 m13c3 m13c2 m13c1 m13c1 = refl
  holds144 m13c3 m13c2 m13c1 m13c2 = refl
  holds144 m13c3 m13c2 m13c1 m13c3 = refl
  holds144 m13c3 m13c2 m13c2 m13c0 = refl
  holds144 m13c3 m13c2 m13c2 m13c1 = refl
  holds144 m13c3 m13c2 m13c2 m13c2 = refl
  holds144 m13c3 m13c2 m13c2 m13c3 = refl
  holds144 m13c3 m13c2 m13c3 m13c0 = refl
  holds144 m13c3 m13c2 m13c3 m13c1 = refl
  holds144 m13c3 m13c2 m13c3 m13c2 = refl
  holds144 m13c3 m13c2 m13c3 m13c3 = refl
  holds144 m13c3 m13c3 m13c0 m13c0 = refl
  holds144 m13c3 m13c3 m13c0 m13c1 = refl
  holds144 m13c3 m13c3 m13c0 m13c2 = refl
  holds144 m13c3 m13c3 m13c0 m13c3 = refl
  holds144 m13c3 m13c3 m13c1 m13c0 = refl
  holds144 m13c3 m13c3 m13c1 m13c1 = refl
  holds144 m13c3 m13c3 m13c1 m13c2 = refl
  holds144 m13c3 m13c3 m13c1 m13c3 = refl
  holds144 m13c3 m13c3 m13c2 m13c0 = refl
  holds144 m13c3 m13c3 m13c2 m13c1 = refl
  holds144 m13c3 m13c3 m13c2 m13c2 = refl
  holds144 m13c3 m13c3 m13c2 m13c3 = refl
  holds144 m13c3 m13c3 m13c3 m13c0 = refl
  holds144 m13c3 m13c3 m13c3 m13c1 = refl
  holds144 m13c3 m13c3 m13c3 m13c2 = refl
  holds144 m13c3 m13c3 m13c3 m13c3 = refl
  cut144 : (x5 : ℕ) → Adequate {ℓ} ((var 0) , (op (op (op (var 1) (var 2)) (var 0)) (op (var 0) (var x5)))) → ⊥
  cut144 x5 = reject13 ((var 0) , (op (op (op (var 1) (var 2)) (var 0)) (op (var 0) (var x5)))) (λ env → holds144 (env 0) (env 1) (env 2) (env x5))
  holds145 : (z0 z1 z2 : A3) → z0 ≡ (mul3 (mul3 (mul3 z1 z2) z0) (mul3 z1 z0))
  holds145 z0 z1 z2 = refl
  cut145 : Adequate {ℓ} ((var 0) , (op (op (op (var 1) (var 2)) (var 0)) (op (var 1) (var 0)))) → ⊥
  cut145  = reject3 ((var 0) , (op (op (op (var 1) (var 2)) (var 0)) (op (var 1) (var 0)))) (λ env → holds145 (env 0) (env 1) (env 2))
  env6 : ℕ → Two
  env6 zero = b0
  env6 (suc zero) = b1
  env6 (suc (suc zero)) = b0
  env6 (suc (suc (suc rest))) = b0
  bad146 : PathP (λ _ → Two) b0 (bop (bop (bop b1 b0) b0) (bop b1 b1)) → ⊥
  bad146  p = false≢true (cong lower p)
  cut146 : Adequate {ℓ} ((var 0) , (op (op (op (var 1) (var 2)) (var 0)) (op (var 1) (var 1)))) → ⊥
  cut146  adequate = bad146  (Adequate.valid adequate Two boolean env6)
  bad147 : PathP (λ _ → Two) b0 (bop (bop (bop b1 b1) b0) (bop b1 b1)) → ⊥
  bad147  p = false≢true (cong lower p)
  cut147 : Adequate {ℓ} ((var 0) , (op (op (op (var 1) (var 2)) (var 0)) (op (var 1) (var 2)))) → ⊥
  cut147  adequate = bad147  (Adequate.valid adequate Two boolean env1)
  env7 : ℕ → Two
  env7 zero = b0
  env7 (suc zero) = b1
  env7 (suc (suc zero)) = b0
  env7 (suc (suc (suc zero))) = b1
  env7 (suc (suc (suc (suc rest)))) = b0
  bad148 : PathP (λ _ → Two) b0 (bop (bop (bop b1 b0) b0) (bop b1 b1)) → ⊥
  bad148  p = false≢true (cong lower p)
  cut148 : Adequate {ℓ} ((var 0) , (op (op (op (var 1) (var 2)) (var 0)) (op (var 1) (var 3)))) → ⊥
  cut148  adequate = bad148  (Adequate.valid adequate Two boolean env7)
  holds149 : (z0 z1 z2 : A3) → z0 ≡ (mul3 (mul3 (mul3 z1 z2) z0) (mul3 z2 z0))
  holds149 z0 z1 z2 = refl
  cut149 : Adequate {ℓ} ((var 0) , (op (op (op (var 1) (var 2)) (var 0)) (op (var 2) (var 0)))) → ⊥
  cut149  = reject3 ((var 0) , (op (op (op (var 1) (var 2)) (var 0)) (op (var 2) (var 0)))) (λ env → holds149 (env 0) (env 1) (env 2))
  bad150 : PathP (λ _ → Two) b0 (bop (bop (bop b1 b1) b0) (bop b1 b1)) → ⊥
  bad150  p = false≢true (cong lower p)
  cut150 : Adequate {ℓ} ((var 0) , (op (op (op (var 1) (var 2)) (var 0)) (op (var 2) (var 1)))) → ⊥
  cut150  adequate = bad150  (Adequate.valid adequate Two boolean env1)
  bad151 : PathP (λ _ → Two) b0 (bop (bop (bop b0 b1) b0) (bop b1 b1)) → ⊥
  bad151  p = false≢true (cong lower p)
  cut151 : Adequate {ℓ} ((var 0) , (op (op (op (var 1) (var 2)) (var 0)) (op (var 2) (var 2)))) → ⊥
  cut151  adequate = bad151  (Adequate.valid adequate Two boolean env3)
  env8 : ℕ → Two
  env8 zero = b0
  env8 (suc zero) = b0
  env8 (suc (suc zero)) = b1
  env8 (suc (suc (suc zero))) = b1
  env8 (suc (suc (suc (suc rest)))) = b0
  bad152 : PathP (λ _ → Two) b0 (bop (bop (bop b0 b1) b0) (bop b1 b1)) → ⊥
  bad152  p = false≢true (cong lower p)
  cut152 : Adequate {ℓ} ((var 0) , (op (op (op (var 1) (var 2)) (var 0)) (op (var 2) (var 3)))) → ⊥
  cut152  adequate = bad152  (Adequate.valid adequate Two boolean env8)
  env9 : ℕ → Two
  env9 zero = b1
  env9 (suc zero) = b1
  env9 (suc (suc zero)) = b1
  env9 (suc (suc (suc zero))) = b0
  env9 (suc (suc (suc (suc rest)))) = b0
  bad153 : (z4 : Two) → PathP (λ _ → Two) b1 (bop (bop (bop b1 b1) b1) (bop b0 z4)) → ⊥
  bad153 z4 p = false≢true (sym (cong lower p))
  cut153 : (x5 : ℕ) → Adequate {ℓ} ((var 0) , (op (op (op (var 1) (var 2)) (var 0)) (op (var 3) (var x5)))) → ⊥
  cut153 x5 adequate = bad153 (env9 x5) (Adequate.valid adequate Two boolean env9)
  bad154 : (z3 z4 : Two) → PathP (λ _ → Two) b0 (bop (bop (bop b1 b0) b1) (bop z3 z4)) → ⊥
  bad154 z3 z4 p = false≢true (cong lower p)
  cut154 : (x4 x5 : ℕ) → Adequate {ℓ} ((var 0) , (op (op (op (var 1) (var 2)) (var 1)) (op (var x4) (var x5)))) → ⊥
  cut154 x4 x5 adequate = bad154 (env6 x4) (env6 x5) (Adequate.valid adequate Two boolean env6)
  bad155 : (z3 z4 : Two) → PathP (λ _ → Two) b0 (bop (bop (bop b0 b1) b1) (bop z3 z4)) → ⊥
  bad155 z3 z4 p = false≢true (cong lower p)
  cut155 : (x4 x5 : ℕ) → Adequate {ℓ} ((var 0) , (op (op (op (var 1) (var 2)) (var 2)) (op (var x4) (var x5)))) → ⊥
  cut155 x4 x5 adequate = bad155 (env3 x4) (env3 x5) (Adequate.valid adequate Two boolean env3)
  env10 : ℕ → Two
  env10 zero = b0
  env10 (suc zero) = b0
  env10 (suc (suc zero)) = b0
  env10 (suc (suc (suc zero))) = b1
  env10 (suc (suc (suc (suc rest)))) = b0
  bad156 : (z4 z5 : Two) → PathP (λ _ → Two) b0 (bop (bop (bop b0 b0) b1) (bop z4 z5)) → ⊥
  bad156 z4 z5 p = false≢true (cong lower p)
  cut156 : (x4 x5 : ℕ) → Adequate {ℓ} ((var 0) , (op (op (op (var 1) (var 2)) (var 3)) (op (var x4) (var x5)))) → ⊥
  cut156 x4 x5 adequate = bad156 (env10 x4) (env10 x5) (Adequate.valid adequate Two boolean env10)
