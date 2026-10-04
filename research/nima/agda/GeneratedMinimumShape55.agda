{-# OPTIONS --safe --cubical --guardedness #-}
module GeneratedMinimumShape55 where
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
  holds181 : (z0 : A1) → (mul1 (mul1 z0 z0) (mul1 z0 (mul1 z0 z0))) ≡ z0
  holds181 m1c0 = refl
  holds181 m1c1 = refl
  cut181 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (var 0) (op (var 0) (var 0)))) , (var 0)) → ⊥
  cut181  = reject1 ((op (op (var 0) (var 0)) (op (var 0) (op (var 0) (var 0)))) , (var 0)) (λ env → holds181 (env 0))
  env0 : ℕ → Two
  env0 zero = b0
  env0 (suc zero) = b1
  env0 (suc (suc rest)) = b0
  bad182 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop b0 b0))) b1 → ⊥
  bad182  p = false≢true (cong lower p)
  cut182 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (var 0) (op (var 0) (var 0)))) , (var 1)) → ⊥
  cut182  adequate = bad182  (Adequate.valid adequate Two boolean env0)
  holds183 : (z0 z1 : A2) → (mul2 (mul2 z0 z0) (mul2 z0 (mul2 z0 z1))) ≡ z0
  holds183 z0 z1 = refl
  cut183 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (var 0) (op (var 0) (var 1)))) , (var 0)) → ⊥
  cut183  = reject2 ((op (op (var 0) (var 0)) (op (var 0) (op (var 0) (var 1)))) , (var 0)) (λ env → holds183 (env 0) (env 1))
  bad184 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop b0 b1))) b1 → ⊥
  bad184  p = false≢true (cong lower p)
  cut184 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (var 0) (op (var 0) (var 1)))) , (var 1)) → ⊥
  cut184  adequate = bad184  (Adequate.valid adequate Two boolean env0)
  env1 : ℕ → Two
  env1 zero = b0
  env1 (suc zero) = b0
  env1 (suc (suc zero)) = b1
  env1 (suc (suc (suc rest))) = b0
  bad185 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop b0 b0))) b1 → ⊥
  bad185  p = false≢true (cong lower p)
  cut185 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (var 0) (op (var 0) (var 1)))) , (var 2)) → ⊥
  cut185  adequate = bad185  (Adequate.valid adequate Two boolean env1)
  holds186 : (z0 z1 : A2) → (mul2 (mul2 z0 z0) (mul2 z0 (mul2 z1 z0))) ≡ z0
  holds186 z0 z1 = refl
  cut186 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (var 0) (op (var 1) (var 0)))) , (var 0)) → ⊥
  cut186  = reject2 ((op (op (var 0) (var 0)) (op (var 0) (op (var 1) (var 0)))) , (var 0)) (λ env → holds186 (env 0) (env 1))
  bad187 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop b1 b0))) b1 → ⊥
  bad187  p = false≢true (cong lower p)
  cut187 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (var 0) (op (var 1) (var 0)))) , (var 1)) → ⊥
  cut187  adequate = bad187  (Adequate.valid adequate Two boolean env0)
  bad188 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop b0 b0))) b1 → ⊥
  bad188  p = false≢true (cong lower p)
  cut188 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (var 0) (op (var 1) (var 0)))) , (var 2)) → ⊥
  cut188  adequate = bad188  (Adequate.valid adequate Two boolean env1)
  holds189 : (z0 z1 : A2) → (mul2 (mul2 z0 z0) (mul2 z0 (mul2 z1 z1))) ≡ z0
  holds189 z0 z1 = refl
  cut189 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (var 0) (op (var 1) (var 1)))) , (var 0)) → ⊥
  cut189  = reject2 ((op (op (var 0) (var 0)) (op (var 0) (op (var 1) (var 1)))) , (var 0)) (λ env → holds189 (env 0) (env 1))
  bad190 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop b1 b1))) b1 → ⊥
  bad190  p = false≢true (cong lower p)
  cut190 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (var 0) (op (var 1) (var 1)))) , (var 1)) → ⊥
  cut190  adequate = bad190  (Adequate.valid adequate Two boolean env0)
  bad191 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop b0 b0))) b1 → ⊥
  bad191  p = false≢true (cong lower p)
  cut191 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (var 0) (op (var 1) (var 1)))) , (var 2)) → ⊥
  cut191  adequate = bad191  (Adequate.valid adequate Two boolean env1)
  holds192 : (z0 z1 z2 : A2) → (mul2 (mul2 z0 z0) (mul2 z0 (mul2 z1 z2))) ≡ z0
  holds192 z0 z1 z2 = refl
  cut192 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (var 0) (op (var 1) (var 2)))) , (var 0)) → ⊥
  cut192  = reject2 ((op (op (var 0) (var 0)) (op (var 0) (op (var 1) (var 2)))) , (var 0)) (λ env → holds192 (env 0) (env 1) (env 2))
  env2 : ℕ → Two
  env2 zero = b0
  env2 (suc zero) = b1
  env2 (suc (suc zero)) = b0
  env2 (suc (suc (suc rest))) = b0
  bad193 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop b1 b0))) b1 → ⊥
  bad193  p = false≢true (cong lower p)
  cut193 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (var 0) (op (var 1) (var 2)))) , (var 1)) → ⊥
  cut193  adequate = bad193  (Adequate.valid adequate Two boolean env2)
  bad194 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop b0 b1))) b1 → ⊥
  bad194  p = false≢true (cong lower p)
  cut194 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (var 0) (op (var 1) (var 2)))) , (var 2)) → ⊥
  cut194  adequate = bad194  (Adequate.valid adequate Two boolean env1)
  env3 : ℕ → Two
  env3 zero = b0
  env3 (suc zero) = b0
  env3 (suc (suc zero)) = b0
  env3 (suc (suc (suc zero))) = b1
  env3 (suc (suc (suc (suc rest)))) = b0
  bad195 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop b0 b0))) b1 → ⊥
  bad195  p = false≢true (cong lower p)
  cut195 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (var 0) (op (var 1) (var 2)))) , (var 3)) → ⊥
  cut195  adequate = bad195  (Adequate.valid adequate Two boolean env3)
  bad196 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b1 (bop b0 b0))) b0 → ⊥
  bad196  p = false≢true (sym (cong lower p))
  cut196 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (var 1) (op (var 0) (var 0)))) , (var 0)) → ⊥
  cut196  adequate = bad196  (Adequate.valid adequate Two boolean env0)
  env4 : ℕ → Two
  env4 zero = b1
  env4 (suc zero) = b0
  env4 (suc (suc rest)) = b0
  bad197 : PathP (λ _ → Two) (bop (bop b1 b1) (bop b0 (bop b1 b1))) b0 → ⊥
  bad197  p = false≢true (sym (cong lower p))
  cut197 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (var 1) (op (var 0) (var 0)))) , (var 1)) → ⊥
  cut197  adequate = bad197  (Adequate.valid adequate Two boolean env4)
  bad198 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop b0 b0))) b1 → ⊥
  bad198  p = false≢true (cong lower p)
  cut198 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (var 1) (op (var 0) (var 0)))) , (var 2)) → ⊥
  cut198  adequate = bad198  (Adequate.valid adequate Two boolean env1)
  bad199 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b1 (bop b0 b1))) b0 → ⊥
  bad199  p = false≢true (sym (cong lower p))
  cut199 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (var 1) (op (var 0) (var 1)))) , (var 0)) → ⊥
  cut199  adequate = bad199  (Adequate.valid adequate Two boolean env0)
  bad200 : PathP (λ _ → Two) (bop (bop b1 b1) (bop b0 (bop b1 b0))) b0 → ⊥
  bad200  p = false≢true (sym (cong lower p))
  cut200 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (var 1) (op (var 0) (var 1)))) , (var 1)) → ⊥
  cut200  adequate = bad200  (Adequate.valid adequate Two boolean env4)
  bad201 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop b0 b0))) b1 → ⊥
  bad201  p = false≢true (cong lower p)
  cut201 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (var 1) (op (var 0) (var 1)))) , (var 2)) → ⊥
  cut201  adequate = bad201  (Adequate.valid adequate Two boolean env1)
  bad202 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b1 (bop b0 b0))) b0 → ⊥
  bad202  p = false≢true (sym (cong lower p))
  cut202 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (var 1) (op (var 0) (var 2)))) , (var 0)) → ⊥
  cut202  adequate = bad202  (Adequate.valid adequate Two boolean env2)
  env5 : ℕ → Two
  env5 zero = b1
  env5 (suc zero) = b0
  env5 (suc (suc zero)) = b0
  env5 (suc (suc (suc rest))) = b0
  bad203 : PathP (λ _ → Two) (bop (bop b1 b1) (bop b0 (bop b1 b0))) b0 → ⊥
  bad203  p = false≢true (sym (cong lower p))
  cut203 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (var 1) (op (var 0) (var 2)))) , (var 1)) → ⊥
  cut203  adequate = bad203  (Adequate.valid adequate Two boolean env5)
  bad204 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop b0 b1))) b1 → ⊥
  bad204  p = false≢true (cong lower p)
  cut204 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (var 1) (op (var 0) (var 2)))) , (var 2)) → ⊥
  cut204  adequate = bad204  (Adequate.valid adequate Two boolean env1)
  bad205 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop b0 b0))) b1 → ⊥
  bad205  p = false≢true (cong lower p)
  cut205 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (var 1) (op (var 0) (var 2)))) , (var 3)) → ⊥
  cut205  adequate = bad205  (Adequate.valid adequate Two boolean env3)
  bad206 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b1 (bop b1 b0))) b0 → ⊥
  bad206  p = false≢true (sym (cong lower p))
  cut206 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (var 1) (op (var 1) (var 0)))) , (var 0)) → ⊥
  cut206  adequate = bad206  (Adequate.valid adequate Two boolean env0)
  bad207 : PathP (λ _ → Two) (bop (bop b1 b1) (bop b0 (bop b0 b1))) b0 → ⊥
  bad207  p = false≢true (sym (cong lower p))
  cut207 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (var 1) (op (var 1) (var 0)))) , (var 1)) → ⊥
  cut207  adequate = bad207  (Adequate.valid adequate Two boolean env4)
  bad208 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop b0 b0))) b1 → ⊥
  bad208  p = false≢true (cong lower p)
  cut208 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (var 1) (op (var 1) (var 0)))) , (var 2)) → ⊥
  cut208  adequate = bad208  (Adequate.valid adequate Two boolean env1)
  holds209 : (z0 z1 : A2) → (mul2 (mul2 z0 z0) (mul2 z1 (mul2 z1 z1))) ≡ z0
  holds209 z0 z1 = refl
  cut209 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (var 1) (op (var 1) (var 1)))) , (var 0)) → ⊥
  cut209  = reject2 ((op (op (var 0) (var 0)) (op (var 1) (op (var 1) (var 1)))) , (var 0)) (λ env → holds209 (env 0) (env 1))
  bad210 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b1 (bop b1 b1))) b1 → ⊥
  bad210  p = false≢true (cong lower p)
  cut210 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (var 1) (op (var 1) (var 1)))) , (var 1)) → ⊥
  cut210  adequate = bad210  (Adequate.valid adequate Two boolean env0)
  bad211 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop b0 b0))) b1 → ⊥
  bad211  p = false≢true (cong lower p)
  cut211 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (var 1) (op (var 1) (var 1)))) , (var 2)) → ⊥
  cut211  adequate = bad211  (Adequate.valid adequate Two boolean env1)
  bad212 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b1 (bop b1 b0))) b0 → ⊥
  bad212  p = false≢true (sym (cong lower p))
  cut212 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (var 1) (op (var 1) (var 2)))) , (var 0)) → ⊥
  cut212  adequate = bad212  (Adequate.valid adequate Two boolean env2)
  env6 : ℕ → Two
  env6 zero = b0
  env6 (suc zero) = b1
  env6 (suc (suc zero)) = b1
  env6 (suc (suc (suc rest))) = b0
  bad213 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b1 (bop b1 b1))) b1 → ⊥
  bad213  p = false≢true (cong lower p)
  cut213 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (var 1) (op (var 1) (var 2)))) , (var 1)) → ⊥
  cut213  adequate = bad213  (Adequate.valid adequate Two boolean env6)
  bad214 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop b0 b1))) b1 → ⊥
  bad214  p = false≢true (cong lower p)
  cut214 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (var 1) (op (var 1) (var 2)))) , (var 2)) → ⊥
  cut214  adequate = bad214  (Adequate.valid adequate Two boolean env1)
  bad215 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop b0 b0))) b1 → ⊥
  bad215  p = false≢true (cong lower p)
  cut215 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (var 1) (op (var 1) (var 2)))) , (var 3)) → ⊥
  cut215  adequate = bad215  (Adequate.valid adequate Two boolean env3)
  bad216 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b1 (bop b0 b0))) b0 → ⊥
  bad216  p = false≢true (sym (cong lower p))
  cut216 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (var 1) (op (var 2) (var 0)))) , (var 0)) → ⊥
  cut216  adequate = bad216  (Adequate.valid adequate Two boolean env2)
  bad217 : PathP (λ _ → Two) (bop (bop b1 b1) (bop b0 (bop b0 b1))) b0 → ⊥
  bad217  p = false≢true (sym (cong lower p))
  cut217 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (var 1) (op (var 2) (var 0)))) , (var 1)) → ⊥
  cut217  adequate = bad217  (Adequate.valid adequate Two boolean env5)
  bad218 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop b1 b0))) b1 → ⊥
  bad218  p = false≢true (cong lower p)
  cut218 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (var 1) (op (var 2) (var 0)))) , (var 2)) → ⊥
  cut218  adequate = bad218  (Adequate.valid adequate Two boolean env1)
  bad219 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop b0 b0))) b1 → ⊥
  bad219  p = false≢true (cong lower p)
  cut219 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (var 1) (op (var 2) (var 0)))) , (var 3)) → ⊥
  cut219  adequate = bad219  (Adequate.valid adequate Two boolean env3)
  bad220 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b1 (bop b0 b1))) b0 → ⊥
  bad220  p = false≢true (sym (cong lower p))
  cut220 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (var 1) (op (var 2) (var 1)))) , (var 0)) → ⊥
  cut220  adequate = bad220  (Adequate.valid adequate Two boolean env2)
  bad221 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b1 (bop b1 b1))) b1 → ⊥
  bad221  p = false≢true (cong lower p)
  cut221 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (var 1) (op (var 2) (var 1)))) , (var 1)) → ⊥
  cut221  adequate = bad221  (Adequate.valid adequate Two boolean env6)
  bad222 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop b1 b0))) b1 → ⊥
  bad222  p = false≢true (cong lower p)
  cut222 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (var 1) (op (var 2) (var 1)))) , (var 2)) → ⊥
  cut222  adequate = bad222  (Adequate.valid adequate Two boolean env1)
  bad223 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop b0 b0))) b1 → ⊥
  bad223  p = false≢true (cong lower p)
  cut223 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (var 1) (op (var 2) (var 1)))) , (var 3)) → ⊥
  cut223  adequate = bad223  (Adequate.valid adequate Two boolean env3)
  bad224 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b1 (bop b0 b0))) b0 → ⊥
  bad224  p = false≢true (sym (cong lower p))
  cut224 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (var 1) (op (var 2) (var 2)))) , (var 0)) → ⊥
  cut224  adequate = bad224  (Adequate.valid adequate Two boolean env2)
  bad225 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b1 (bop b1 b1))) b1 → ⊥
  bad225  p = false≢true (cong lower p)
  cut225 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (var 1) (op (var 2) (var 2)))) , (var 1)) → ⊥
  cut225  adequate = bad225  (Adequate.valid adequate Two boolean env6)
  bad226 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop b1 b1))) b1 → ⊥
  bad226  p = false≢true (cong lower p)
  cut226 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (var 1) (op (var 2) (var 2)))) , (var 2)) → ⊥
  cut226  adequate = bad226  (Adequate.valid adequate Two boolean env1)
  bad227 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop b0 b0))) b1 → ⊥
  bad227  p = false≢true (cong lower p)
  cut227 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (var 1) (op (var 2) (var 2)))) , (var 3)) → ⊥
  cut227  adequate = bad227  (Adequate.valid adequate Two boolean env3)
  env7 : ℕ → Two
  env7 zero = b0
  env7 (suc zero) = b1
  env7 (suc (suc zero)) = b0
  env7 (suc (suc (suc zero))) = b0
  env7 (suc (suc (suc (suc rest)))) = b0
  bad228 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b1 (bop b0 b0))) b0 → ⊥
  bad228  p = false≢true (sym (cong lower p))
  cut228 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (var 1) (op (var 2) (var 3)))) , (var 0)) → ⊥
  cut228  adequate = bad228  (Adequate.valid adequate Two boolean env7)
  env8 : ℕ → Two
  env8 zero = b0
  env8 (suc zero) = b1
  env8 (suc (suc zero)) = b1
  env8 (suc (suc (suc zero))) = b1
  env8 (suc (suc (suc (suc rest)))) = b0
  bad229 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b1 (bop b1 b1))) b1 → ⊥
  bad229  p = false≢true (cong lower p)
  cut229 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (var 1) (op (var 2) (var 3)))) , (var 1)) → ⊥
  cut229  adequate = bad229  (Adequate.valid adequate Two boolean env8)
  env9 : ℕ → Two
  env9 zero = b0
  env9 (suc zero) = b0
  env9 (suc (suc zero)) = b1
  env9 (suc (suc (suc zero))) = b0
  env9 (suc (suc (suc (suc rest)))) = b0
  bad230 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop b1 b0))) b1 → ⊥
  bad230  p = false≢true (cong lower p)
  cut230 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (var 1) (op (var 2) (var 3)))) , (var 2)) → ⊥
  cut230  adequate = bad230  (Adequate.valid adequate Two boolean env9)
  bad231 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop b0 b1))) b1 → ⊥
  bad231  p = false≢true (cong lower p)
  cut231 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (var 1) (op (var 2) (var 3)))) , (var 3)) → ⊥
  cut231  adequate = bad231  (Adequate.valid adequate Two boolean env3)
  env10 : ℕ → Two
  env10 zero = b0
  env10 (suc zero) = b0
  env10 (suc (suc zero)) = b0
  env10 (suc (suc (suc zero))) = b0
  env10 (suc (suc (suc (suc zero)))) = b1
  env10 (suc (suc (suc (suc (suc rest))))) = b0
  bad232 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop b0 b0))) b1 → ⊥
  bad232  p = false≢true (cong lower p)
  cut232 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (var 1) (op (var 2) (var 3)))) , (var 4)) → ⊥
  cut232  adequate = bad232  (Adequate.valid adequate Two boolean env10)
  bad233 : PathP (λ _ → Two) (bop (bop b1 b0) (bop b1 (bop b1 b1))) b1 → ⊥
  bad233  p = false≢true (cong lower p)
  cut233 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 0) (op (var 0) (var 0)))) , (var 0)) → ⊥
  cut233  adequate = bad233  (Adequate.valid adequate Two boolean env4)
  bad234 : PathP (λ _ → Two) (bop (bop b0 b1) (bop b0 (bop b0 b0))) b1 → ⊥
  bad234  p = false≢true (cong lower p)
  cut234 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 0) (op (var 0) (var 0)))) , (var 1)) → ⊥
  cut234  adequate = bad234  (Adequate.valid adequate Two boolean env0)
  bad235 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop b0 b0))) b1 → ⊥
  bad235  p = false≢true (cong lower p)
  cut235 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 0) (op (var 0) (var 0)))) , (var 2)) → ⊥
  cut235  adequate = bad235  (Adequate.valid adequate Two boolean env1)
  holds236 : (z0 z1 : A2) → (mul2 (mul2 z0 z1) (mul2 z0 (mul2 z0 z1))) ≡ z0
  holds236 z0 z1 = refl
  cut236 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 0) (op (var 0) (var 1)))) , (var 0)) → ⊥
  cut236  = reject2 ((op (op (var 0) (var 1)) (op (var 0) (op (var 0) (var 1)))) , (var 0)) (λ env → holds236 (env 0) (env 1))
  bad237 : PathP (λ _ → Two) (bop (bop b0 b1) (bop b0 (bop b0 b1))) b1 → ⊥
  bad237  p = false≢true (cong lower p)
  cut237 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 0) (op (var 0) (var 1)))) , (var 1)) → ⊥
  cut237  adequate = bad237  (Adequate.valid adequate Two boolean env0)
  bad238 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop b0 b0))) b1 → ⊥
  bad238  p = false≢true (cong lower p)
  cut238 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 0) (op (var 0) (var 1)))) , (var 2)) → ⊥
  cut238  adequate = bad238  (Adequate.valid adequate Two boolean env1)
  env11 : ℕ → Two
  env11 zero = b1
  env11 (suc zero) = b0
  env11 (suc (suc zero)) = b1
  env11 (suc (suc (suc rest))) = b0
  bad239 : PathP (λ _ → Two) (bop (bop b1 b0) (bop b1 (bop b1 b1))) b1 → ⊥
  bad239  p = false≢true (cong lower p)
  cut239 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 0) (op (var 0) (var 2)))) , (var 0)) → ⊥
  cut239  adequate = bad239  (Adequate.valid adequate Two boolean env11)
  bad240 : PathP (λ _ → Two) (bop (bop b0 b1) (bop b0 (bop b0 b0))) b1 → ⊥
  bad240  p = false≢true (cong lower p)
  cut240 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 0) (op (var 0) (var 2)))) , (var 1)) → ⊥
  cut240  adequate = bad240  (Adequate.valid adequate Two boolean env2)
  bad241 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop b0 b1))) b1 → ⊥
  bad241  p = false≢true (cong lower p)
  cut241 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 0) (op (var 0) (var 2)))) , (var 2)) → ⊥
  cut241  adequate = bad241  (Adequate.valid adequate Two boolean env1)
  bad242 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop b0 b0))) b1 → ⊥
  bad242  p = false≢true (cong lower p)
  cut242 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 0) (op (var 0) (var 2)))) , (var 3)) → ⊥
  cut242  adequate = bad242  (Adequate.valid adequate Two boolean env3)
  holds243 : (z0 z1 : A2) → (mul2 (mul2 z0 z1) (mul2 z0 (mul2 z1 z0))) ≡ z0
  holds243 z0 z1 = refl
  cut243 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 0) (op (var 1) (var 0)))) , (var 0)) → ⊥
  cut243  = reject2 ((op (op (var 0) (var 1)) (op (var 0) (op (var 1) (var 0)))) , (var 0)) (λ env → holds243 (env 0) (env 1))
  bad244 : PathP (λ _ → Two) (bop (bop b0 b1) (bop b0 (bop b1 b0))) b1 → ⊥
  bad244  p = false≢true (cong lower p)
  cut244 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 0) (op (var 1) (var 0)))) , (var 1)) → ⊥
  cut244  adequate = bad244  (Adequate.valid adequate Two boolean env0)
  bad245 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop b0 b0))) b1 → ⊥
  bad245  p = false≢true (cong lower p)
  cut245 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 0) (op (var 1) (var 0)))) , (var 2)) → ⊥
  cut245  adequate = bad245  (Adequate.valid adequate Two boolean env1)
  holds246 : (z0 z1 : A2) → (mul2 (mul2 z0 z1) (mul2 z0 (mul2 z1 z1))) ≡ z0
  holds246 z0 z1 = refl
  cut246 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 0) (op (var 1) (var 1)))) , (var 0)) → ⊥
  cut246  = reject2 ((op (op (var 0) (var 1)) (op (var 0) (op (var 1) (var 1)))) , (var 0)) (λ env → holds246 (env 0) (env 1))
  bad247 : PathP (λ _ → Two) (bop (bop b0 b1) (bop b0 (bop b1 b1))) b1 → ⊥
  bad247  p = false≢true (cong lower p)
  cut247 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 0) (op (var 1) (var 1)))) , (var 1)) → ⊥
  cut247  adequate = bad247  (Adequate.valid adequate Two boolean env0)
  bad248 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop b0 b0))) b1 → ⊥
  bad248  p = false≢true (cong lower p)
  cut248 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 0) (op (var 1) (var 1)))) , (var 2)) → ⊥
  cut248  adequate = bad248  (Adequate.valid adequate Two boolean env1)
  holds249 : (z0 z1 z2 : A2) → (mul2 (mul2 z0 z1) (mul2 z0 (mul2 z1 z2))) ≡ z0
  holds249 z0 z1 z2 = refl
  cut249 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 0) (op (var 1) (var 2)))) , (var 0)) → ⊥
  cut249  = reject2 ((op (op (var 0) (var 1)) (op (var 0) (op (var 1) (var 2)))) , (var 0)) (λ env → holds249 (env 0) (env 1) (env 2))
  bad250 : PathP (λ _ → Two) (bop (bop b0 b1) (bop b0 (bop b1 b0))) b1 → ⊥
  bad250  p = false≢true (cong lower p)
  cut250 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 0) (op (var 1) (var 2)))) , (var 1)) → ⊥
  cut250  adequate = bad250  (Adequate.valid adequate Two boolean env2)
  bad251 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop b0 b1))) b1 → ⊥
  bad251  p = false≢true (cong lower p)
  cut251 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 0) (op (var 1) (var 2)))) , (var 2)) → ⊥
  cut251  adequate = bad251  (Adequate.valid adequate Two boolean env1)
  bad252 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop b0 b0))) b1 → ⊥
  bad252  p = false≢true (cong lower p)
  cut252 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 0) (op (var 1) (var 2)))) , (var 3)) → ⊥
  cut252  adequate = bad252  (Adequate.valid adequate Two boolean env3)
  bad253 : PathP (λ _ → Two) (bop (bop b1 b0) (bop b1 (bop b1 b1))) b1 → ⊥
  bad253  p = false≢true (cong lower p)
  cut253 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 0) (op (var 2) (var 0)))) , (var 0)) → ⊥
  cut253  adequate = bad253  (Adequate.valid adequate Two boolean env11)
  bad254 : PathP (λ _ → Two) (bop (bop b0 b1) (bop b0 (bop b0 b0))) b1 → ⊥
  bad254  p = false≢true (cong lower p)
  cut254 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 0) (op (var 2) (var 0)))) , (var 1)) → ⊥
  cut254  adequate = bad254  (Adequate.valid adequate Two boolean env2)
  bad255 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop b1 b0))) b1 → ⊥
  bad255  p = false≢true (cong lower p)
  cut255 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 0) (op (var 2) (var 0)))) , (var 2)) → ⊥
  cut255  adequate = bad255  (Adequate.valid adequate Two boolean env1)
  bad256 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop b0 b0))) b1 → ⊥
  bad256  p = false≢true (cong lower p)
  cut256 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 0) (op (var 2) (var 0)))) , (var 3)) → ⊥
  cut256  adequate = bad256  (Adequate.valid adequate Two boolean env3)
  holds257 : (z0 z1 z2 : A2) → (mul2 (mul2 z0 z1) (mul2 z0 (mul2 z2 z1))) ≡ z0
  holds257 z0 z1 z2 = refl
  cut257 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 0) (op (var 2) (var 1)))) , (var 0)) → ⊥
  cut257  = reject2 ((op (op (var 0) (var 1)) (op (var 0) (op (var 2) (var 1)))) , (var 0)) (λ env → holds257 (env 0) (env 1) (env 2))
  bad258 : PathP (λ _ → Two) (bop (bop b0 b1) (bop b0 (bop b0 b1))) b1 → ⊥
  bad258  p = false≢true (cong lower p)
  cut258 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 0) (op (var 2) (var 1)))) , (var 1)) → ⊥
  cut258  adequate = bad258  (Adequate.valid adequate Two boolean env2)
  bad259 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop b1 b0))) b1 → ⊥
  bad259  p = false≢true (cong lower p)
  cut259 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 0) (op (var 2) (var 1)))) , (var 2)) → ⊥
  cut259  adequate = bad259  (Adequate.valid adequate Two boolean env1)
  bad260 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop b0 b0))) b1 → ⊥
  bad260  p = false≢true (cong lower p)
  cut260 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 0) (op (var 2) (var 1)))) , (var 3)) → ⊥
  cut260  adequate = bad260  (Adequate.valid adequate Two boolean env3)
  bad261 : PathP (λ _ → Two) (bop (bop b1 b0) (bop b1 (bop b1 b1))) b1 → ⊥
  bad261  p = false≢true (cong lower p)
  cut261 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 0) (op (var 2) (var 2)))) , (var 0)) → ⊥
  cut261  adequate = bad261  (Adequate.valid adequate Two boolean env11)
  bad262 : PathP (λ _ → Two) (bop (bop b0 b1) (bop b0 (bop b0 b0))) b1 → ⊥
  bad262  p = false≢true (cong lower p)
  cut262 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 0) (op (var 2) (var 2)))) , (var 1)) → ⊥
  cut262  adequate = bad262  (Adequate.valid adequate Two boolean env2)
  bad263 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop b1 b1))) b1 → ⊥
  bad263  p = false≢true (cong lower p)
  cut263 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 0) (op (var 2) (var 2)))) , (var 2)) → ⊥
  cut263  adequate = bad263  (Adequate.valid adequate Two boolean env1)
  bad264 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop b0 b0))) b1 → ⊥
  bad264  p = false≢true (cong lower p)
  cut264 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 0) (op (var 2) (var 2)))) , (var 3)) → ⊥
  cut264  adequate = bad264  (Adequate.valid adequate Two boolean env3)
  env12 : ℕ → Two
  env12 zero = b1
  env12 (suc zero) = b0
  env12 (suc (suc zero)) = b1
  env12 (suc (suc (suc zero))) = b1
  env12 (suc (suc (suc (suc rest)))) = b0
  bad265 : PathP (λ _ → Two) (bop (bop b1 b0) (bop b1 (bop b1 b1))) b1 → ⊥
  bad265  p = false≢true (cong lower p)
  cut265 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 0) (op (var 2) (var 3)))) , (var 0)) → ⊥
  cut265  adequate = bad265  (Adequate.valid adequate Two boolean env12)
  bad266 : PathP (λ _ → Two) (bop (bop b0 b1) (bop b0 (bop b0 b0))) b1 → ⊥
  bad266  p = false≢true (cong lower p)
  cut266 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 0) (op (var 2) (var 3)))) , (var 1)) → ⊥
  cut266  adequate = bad266  (Adequate.valid adequate Two boolean env7)
  bad267 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop b1 b0))) b1 → ⊥
  bad267  p = false≢true (cong lower p)
  cut267 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 0) (op (var 2) (var 3)))) , (var 2)) → ⊥
  cut267  adequate = bad267  (Adequate.valid adequate Two boolean env9)
  bad268 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop b0 b1))) b1 → ⊥
  bad268  p = false≢true (cong lower p)
  cut268 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 0) (op (var 2) (var 3)))) , (var 3)) → ⊥
  cut268  adequate = bad268  (Adequate.valid adequate Two boolean env3)
  bad269 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop b0 b0))) b1 → ⊥
  bad269  p = false≢true (cong lower p)
  cut269 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 0) (op (var 2) (var 3)))) , (var 4)) → ⊥
  cut269  adequate = bad269  (Adequate.valid adequate Two boolean env10)
  bad270 : PathP (λ _ → Two) (bop (bop b0 b1) (bop b1 (bop b0 b0))) b0 → ⊥
  bad270  p = false≢true (sym (cong lower p))
  cut270 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 1) (op (var 0) (var 0)))) , (var 0)) → ⊥
  cut270  adequate = bad270  (Adequate.valid adequate Two boolean env0)
  holds271 : (z0 z1 : A5) → (mul5 (mul5 z0 z1) (mul5 z1 (mul5 z0 z0))) ≡ z1
  holds271 m5c0 m5c0 = refl
  holds271 m5c0 m5c1 = refl
  holds271 m5c0 m5c2 = refl
  holds271 m5c1 m5c0 = refl
  holds271 m5c1 m5c1 = refl
  holds271 m5c1 m5c2 = refl
  holds271 m5c2 m5c0 = refl
  holds271 m5c2 m5c1 = refl
  holds271 m5c2 m5c2 = refl
  cut271 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 1) (op (var 0) (var 0)))) , (var 1)) → ⊥
  cut271  = reject5 ((op (op (var 0) (var 1)) (op (var 1) (op (var 0) (var 0)))) , (var 1)) (λ env → holds271 (env 0) (env 1))
  bad272 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop b0 b0))) b1 → ⊥
  bad272  p = false≢true (cong lower p)
  cut272 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 1) (op (var 0) (var 0)))) , (var 2)) → ⊥
  cut272  adequate = bad272  (Adequate.valid adequate Two boolean env1)
  bad273 : PathP (λ _ → Two) (bop (bop b0 b1) (bop b1 (bop b0 b1))) b0 → ⊥
  bad273  p = false≢true (sym (cong lower p))
  cut273 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 1) (op (var 0) (var 1)))) , (var 0)) → ⊥
  cut273  adequate = bad273  (Adequate.valid adequate Two boolean env0)
  holds274 : (z0 z1 : A3) → (mul3 (mul3 z0 z1) (mul3 z1 (mul3 z0 z1))) ≡ z1
  holds274 z0 z1 = refl
  cut274 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 1) (op (var 0) (var 1)))) , (var 1)) → ⊥
  cut274  = reject3 ((op (op (var 0) (var 1)) (op (var 1) (op (var 0) (var 1)))) , (var 1)) (λ env → holds274 (env 0) (env 1))
  bad275 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop b0 b0))) b1 → ⊥
  bad275  p = false≢true (cong lower p)
  cut275 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 1) (op (var 0) (var 1)))) , (var 2)) → ⊥
  cut275  adequate = bad275  (Adequate.valid adequate Two boolean env1)
  bad276 : PathP (λ _ → Two) (bop (bop b0 b1) (bop b1 (bop b0 b0))) b0 → ⊥
  bad276  p = false≢true (sym (cong lower p))
  cut276 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 1) (op (var 0) (var 2)))) , (var 0)) → ⊥
  cut276  adequate = bad276  (Adequate.valid adequate Two boolean env2)
  holds277 : (z0 z1 z2 : A13) → (mul13 (mul13 z0 z1) (mul13 z1 (mul13 z0 z2))) ≡ z1
  holds277 m13c0 m13c0 m13c0 = refl
  holds277 m13c0 m13c0 m13c1 = refl
  holds277 m13c0 m13c0 m13c2 = refl
  holds277 m13c0 m13c0 m13c3 = refl
  holds277 m13c0 m13c1 m13c0 = refl
  holds277 m13c0 m13c1 m13c1 = refl
  holds277 m13c0 m13c1 m13c2 = refl
  holds277 m13c0 m13c1 m13c3 = refl
  holds277 m13c0 m13c2 m13c0 = refl
  holds277 m13c0 m13c2 m13c1 = refl
  holds277 m13c0 m13c2 m13c2 = refl
  holds277 m13c0 m13c2 m13c3 = refl
  holds277 m13c0 m13c3 m13c0 = refl
  holds277 m13c0 m13c3 m13c1 = refl
  holds277 m13c0 m13c3 m13c2 = refl
  holds277 m13c0 m13c3 m13c3 = refl
  holds277 m13c1 m13c0 m13c0 = refl
  holds277 m13c1 m13c0 m13c1 = refl
  holds277 m13c1 m13c0 m13c2 = refl
  holds277 m13c1 m13c0 m13c3 = refl
  holds277 m13c1 m13c1 m13c0 = refl
  holds277 m13c1 m13c1 m13c1 = refl
  holds277 m13c1 m13c1 m13c2 = refl
  holds277 m13c1 m13c1 m13c3 = refl
  holds277 m13c1 m13c2 m13c0 = refl
  holds277 m13c1 m13c2 m13c1 = refl
  holds277 m13c1 m13c2 m13c2 = refl
  holds277 m13c1 m13c2 m13c3 = refl
  holds277 m13c1 m13c3 m13c0 = refl
  holds277 m13c1 m13c3 m13c1 = refl
  holds277 m13c1 m13c3 m13c2 = refl
  holds277 m13c1 m13c3 m13c3 = refl
  holds277 m13c2 m13c0 m13c0 = refl
  holds277 m13c2 m13c0 m13c1 = refl
  holds277 m13c2 m13c0 m13c2 = refl
  holds277 m13c2 m13c0 m13c3 = refl
  holds277 m13c2 m13c1 m13c0 = refl
  holds277 m13c2 m13c1 m13c1 = refl
  holds277 m13c2 m13c1 m13c2 = refl
  holds277 m13c2 m13c1 m13c3 = refl
  holds277 m13c2 m13c2 m13c0 = refl
  holds277 m13c2 m13c2 m13c1 = refl
  holds277 m13c2 m13c2 m13c2 = refl
  holds277 m13c2 m13c2 m13c3 = refl
  holds277 m13c2 m13c3 m13c0 = refl
  holds277 m13c2 m13c3 m13c1 = refl
  holds277 m13c2 m13c3 m13c2 = refl
  holds277 m13c2 m13c3 m13c3 = refl
  holds277 m13c3 m13c0 m13c0 = refl
  holds277 m13c3 m13c0 m13c1 = refl
  holds277 m13c3 m13c0 m13c2 = refl
  holds277 m13c3 m13c0 m13c3 = refl
  holds277 m13c3 m13c1 m13c0 = refl
  holds277 m13c3 m13c1 m13c1 = refl
  holds277 m13c3 m13c1 m13c2 = refl
  holds277 m13c3 m13c1 m13c3 = refl
  holds277 m13c3 m13c2 m13c0 = refl
  holds277 m13c3 m13c2 m13c1 = refl
  holds277 m13c3 m13c2 m13c2 = refl
  holds277 m13c3 m13c2 m13c3 = refl
  holds277 m13c3 m13c3 m13c0 = refl
  holds277 m13c3 m13c3 m13c1 = refl
  holds277 m13c3 m13c3 m13c2 = refl
  holds277 m13c3 m13c3 m13c3 = refl
  cut277 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 1) (op (var 0) (var 2)))) , (var 1)) → ⊥
  cut277  = reject13 ((op (op (var 0) (var 1)) (op (var 1) (op (var 0) (var 2)))) , (var 1)) (λ env → holds277 (env 0) (env 1) (env 2))
  bad278 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop b0 b1))) b1 → ⊥
  bad278  p = false≢true (cong lower p)
  cut278 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 1) (op (var 0) (var 2)))) , (var 2)) → ⊥
  cut278  adequate = bad278  (Adequate.valid adequate Two boolean env1)
  bad279 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop b0 b0))) b1 → ⊥
  bad279  p = false≢true (cong lower p)
  cut279 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 1) (op (var 0) (var 2)))) , (var 3)) → ⊥
  cut279  adequate = bad279  (Adequate.valid adequate Two boolean env3)
  bad280 : PathP (λ _ → Two) (bop (bop b0 b1) (bop b1 (bop b1 b0))) b0 → ⊥
  bad280  p = false≢true (sym (cong lower p))
  cut280 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 1) (op (var 1) (var 0)))) , (var 0)) → ⊥
  cut280  adequate = bad280  (Adequate.valid adequate Two boolean env0)
  holds281 : (z0 z1 : A4) → (mul4 (mul4 z0 z1) (mul4 z1 (mul4 z1 z0))) ≡ z1
  holds281 m4c0 m4c0 = refl
  holds281 m4c0 m4c1 = refl
  holds281 m4c1 m4c0 = refl
  holds281 m4c1 m4c1 = refl
  cut281 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 1) (op (var 1) (var 0)))) , (var 1)) → ⊥
  cut281  = reject4 ((op (op (var 0) (var 1)) (op (var 1) (op (var 1) (var 0)))) , (var 1)) (λ env → holds281 (env 0) (env 1))
  bad282 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop b0 b0))) b1 → ⊥
  bad282  p = false≢true (cong lower p)
  cut282 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 1) (op (var 1) (var 0)))) , (var 2)) → ⊥
  cut282  adequate = bad282  (Adequate.valid adequate Two boolean env1)
  bad283 : PathP (λ _ → Two) (bop (bop b1 b0) (bop b0 (bop b0 b0))) b1 → ⊥
  bad283  p = false≢true (cong lower p)
  cut283 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 1) (op (var 1) (var 1)))) , (var 0)) → ⊥
  cut283  adequate = bad283  (Adequate.valid adequate Two boolean env4)
  bad284 : PathP (λ _ → Two) (bop (bop b0 b1) (bop b1 (bop b1 b1))) b1 → ⊥
  bad284  p = false≢true (cong lower p)
  cut284 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 1) (op (var 1) (var 1)))) , (var 1)) → ⊥
  cut284  adequate = bad284  (Adequate.valid adequate Two boolean env0)
  bad285 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop b0 b0))) b1 → ⊥
  bad285  p = false≢true (cong lower p)
  cut285 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 1) (op (var 1) (var 1)))) , (var 2)) → ⊥
  cut285  adequate = bad285  (Adequate.valid adequate Two boolean env1)
  bad286 : PathP (λ _ → Two) (bop (bop b0 b1) (bop b1 (bop b1 b0))) b0 → ⊥
  bad286  p = false≢true (sym (cong lower p))
  cut286 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 1) (op (var 1) (var 2)))) , (var 0)) → ⊥
  cut286  adequate = bad286  (Adequate.valid adequate Two boolean env2)
  bad287 : PathP (λ _ → Two) (bop (bop b0 b1) (bop b1 (bop b1 b1))) b1 → ⊥
  bad287  p = false≢true (cong lower p)
  cut287 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 1) (op (var 1) (var 2)))) , (var 1)) → ⊥
  cut287  adequate = bad287  (Adequate.valid adequate Two boolean env6)
  bad288 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop b0 b1))) b1 → ⊥
  bad288  p = false≢true (cong lower p)
  cut288 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 1) (op (var 1) (var 2)))) , (var 2)) → ⊥
  cut288  adequate = bad288  (Adequate.valid adequate Two boolean env1)
  bad289 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop b0 b0))) b1 → ⊥
  bad289  p = false≢true (cong lower p)
  cut289 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 1) (op (var 1) (var 2)))) , (var 3)) → ⊥
  cut289  adequate = bad289  (Adequate.valid adequate Two boolean env3)
  bad290 : PathP (λ _ → Two) (bop (bop b0 b1) (bop b1 (bop b0 b0))) b0 → ⊥
  bad290  p = false≢true (sym (cong lower p))
  cut290 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 1) (op (var 2) (var 0)))) , (var 0)) → ⊥
  cut290  adequate = bad290  (Adequate.valid adequate Two boolean env2)
  holds291 : (z0 z1 z2 : A13) → (mul13 (mul13 z0 z1) (mul13 z1 (mul13 z2 z0))) ≡ z1
  holds291 m13c0 m13c0 m13c0 = refl
  holds291 m13c0 m13c0 m13c1 = refl
  holds291 m13c0 m13c0 m13c2 = refl
  holds291 m13c0 m13c0 m13c3 = refl
  holds291 m13c0 m13c1 m13c0 = refl
  holds291 m13c0 m13c1 m13c1 = refl
  holds291 m13c0 m13c1 m13c2 = refl
  holds291 m13c0 m13c1 m13c3 = refl
  holds291 m13c0 m13c2 m13c0 = refl
  holds291 m13c0 m13c2 m13c1 = refl
  holds291 m13c0 m13c2 m13c2 = refl
  holds291 m13c0 m13c2 m13c3 = refl
  holds291 m13c0 m13c3 m13c0 = refl
  holds291 m13c0 m13c3 m13c1 = refl
  holds291 m13c0 m13c3 m13c2 = refl
  holds291 m13c0 m13c3 m13c3 = refl
  holds291 m13c1 m13c0 m13c0 = refl
  holds291 m13c1 m13c0 m13c1 = refl
  holds291 m13c1 m13c0 m13c2 = refl
  holds291 m13c1 m13c0 m13c3 = refl
  holds291 m13c1 m13c1 m13c0 = refl
  holds291 m13c1 m13c1 m13c1 = refl
  holds291 m13c1 m13c1 m13c2 = refl
  holds291 m13c1 m13c1 m13c3 = refl
  holds291 m13c1 m13c2 m13c0 = refl
  holds291 m13c1 m13c2 m13c1 = refl
  holds291 m13c1 m13c2 m13c2 = refl
  holds291 m13c1 m13c2 m13c3 = refl
  holds291 m13c1 m13c3 m13c0 = refl
  holds291 m13c1 m13c3 m13c1 = refl
  holds291 m13c1 m13c3 m13c2 = refl
  holds291 m13c1 m13c3 m13c3 = refl
  holds291 m13c2 m13c0 m13c0 = refl
  holds291 m13c2 m13c0 m13c1 = refl
  holds291 m13c2 m13c0 m13c2 = refl
  holds291 m13c2 m13c0 m13c3 = refl
  holds291 m13c2 m13c1 m13c0 = refl
  holds291 m13c2 m13c1 m13c1 = refl
  holds291 m13c2 m13c1 m13c2 = refl
  holds291 m13c2 m13c1 m13c3 = refl
  holds291 m13c2 m13c2 m13c0 = refl
  holds291 m13c2 m13c2 m13c1 = refl
  holds291 m13c2 m13c2 m13c2 = refl
  holds291 m13c2 m13c2 m13c3 = refl
  holds291 m13c2 m13c3 m13c0 = refl
  holds291 m13c2 m13c3 m13c1 = refl
  holds291 m13c2 m13c3 m13c2 = refl
  holds291 m13c2 m13c3 m13c3 = refl
  holds291 m13c3 m13c0 m13c0 = refl
  holds291 m13c3 m13c0 m13c1 = refl
  holds291 m13c3 m13c0 m13c2 = refl
  holds291 m13c3 m13c0 m13c3 = refl
  holds291 m13c3 m13c1 m13c0 = refl
  holds291 m13c3 m13c1 m13c1 = refl
  holds291 m13c3 m13c1 m13c2 = refl
  holds291 m13c3 m13c1 m13c3 = refl
  holds291 m13c3 m13c2 m13c0 = refl
  holds291 m13c3 m13c2 m13c1 = refl
  holds291 m13c3 m13c2 m13c2 = refl
  holds291 m13c3 m13c2 m13c3 = refl
  holds291 m13c3 m13c3 m13c0 = refl
  holds291 m13c3 m13c3 m13c1 = refl
  holds291 m13c3 m13c3 m13c2 = refl
  holds291 m13c3 m13c3 m13c3 = refl
  cut291 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 1) (op (var 2) (var 0)))) , (var 1)) → ⊥
  cut291  = reject13 ((op (op (var 0) (var 1)) (op (var 1) (op (var 2) (var 0)))) , (var 1)) (λ env → holds291 (env 0) (env 1) (env 2))
  bad292 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop b1 b0))) b1 → ⊥
  bad292  p = false≢true (cong lower p)
  cut292 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 1) (op (var 2) (var 0)))) , (var 2)) → ⊥
  cut292  adequate = bad292  (Adequate.valid adequate Two boolean env1)
  bad293 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop b0 b0))) b1 → ⊥
  bad293  p = false≢true (cong lower p)
  cut293 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 1) (op (var 2) (var 0)))) , (var 3)) → ⊥
  cut293  adequate = bad293  (Adequate.valid adequate Two boolean env3)
  bad294 : PathP (λ _ → Two) (bop (bop b0 b1) (bop b1 (bop b0 b1))) b0 → ⊥
  bad294  p = false≢true (sym (cong lower p))
  cut294 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 1) (op (var 2) (var 1)))) , (var 0)) → ⊥
  cut294  adequate = bad294  (Adequate.valid adequate Two boolean env2)
  bad295 : PathP (λ _ → Two) (bop (bop b0 b1) (bop b1 (bop b1 b1))) b1 → ⊥
  bad295  p = false≢true (cong lower p)
  cut295 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 1) (op (var 2) (var 1)))) , (var 1)) → ⊥
  cut295  adequate = bad295  (Adequate.valid adequate Two boolean env6)
  bad296 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop b1 b0))) b1 → ⊥
  bad296  p = false≢true (cong lower p)
  cut296 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 1) (op (var 2) (var 1)))) , (var 2)) → ⊥
  cut296  adequate = bad296  (Adequate.valid adequate Two boolean env1)
  bad297 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop b0 b0))) b1 → ⊥
  bad297  p = false≢true (cong lower p)
  cut297 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 1) (op (var 2) (var 1)))) , (var 3)) → ⊥
  cut297  adequate = bad297  (Adequate.valid adequate Two boolean env3)
  bad298 : PathP (λ _ → Two) (bop (bop b0 b1) (bop b1 (bop b0 b0))) b0 → ⊥
  bad298  p = false≢true (sym (cong lower p))
  cut298 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 1) (op (var 2) (var 2)))) , (var 0)) → ⊥
  cut298  adequate = bad298  (Adequate.valid adequate Two boolean env2)
  bad299 : PathP (λ _ → Two) (bop (bop b0 b1) (bop b1 (bop b1 b1))) b1 → ⊥
  bad299  p = false≢true (cong lower p)
  cut299 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 1) (op (var 2) (var 2)))) , (var 1)) → ⊥
  cut299  adequate = bad299  (Adequate.valid adequate Two boolean env6)
  bad300 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop b1 b1))) b1 → ⊥
  bad300  p = false≢true (cong lower p)
  cut300 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 1) (op (var 2) (var 2)))) , (var 2)) → ⊥
  cut300  adequate = bad300  (Adequate.valid adequate Two boolean env1)
  bad301 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop b0 b0))) b1 → ⊥
  bad301  p = false≢true (cong lower p)
  cut301 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 1) (op (var 2) (var 2)))) , (var 3)) → ⊥
  cut301  adequate = bad301  (Adequate.valid adequate Two boolean env3)
  bad302 : PathP (λ _ → Two) (bop (bop b0 b1) (bop b1 (bop b0 b0))) b0 → ⊥
  bad302  p = false≢true (sym (cong lower p))
  cut302 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 1) (op (var 2) (var 3)))) , (var 0)) → ⊥
  cut302  adequate = bad302  (Adequate.valid adequate Two boolean env7)
  bad303 : PathP (λ _ → Two) (bop (bop b0 b1) (bop b1 (bop b1 b1))) b1 → ⊥
  bad303  p = false≢true (cong lower p)
  cut303 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 1) (op (var 2) (var 3)))) , (var 1)) → ⊥
  cut303  adequate = bad303  (Adequate.valid adequate Two boolean env8)
  bad304 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop b1 b0))) b1 → ⊥
  bad304  p = false≢true (cong lower p)
  cut304 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 1) (op (var 2) (var 3)))) , (var 2)) → ⊥
  cut304  adequate = bad304  (Adequate.valid adequate Two boolean env9)
  bad305 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop b0 b1))) b1 → ⊥
  bad305  p = false≢true (cong lower p)
  cut305 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 1) (op (var 2) (var 3)))) , (var 3)) → ⊥
  cut305  adequate = bad305  (Adequate.valid adequate Two boolean env3)
  bad306 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop b0 b0))) b1 → ⊥
  bad306  p = false≢true (cong lower p)
  cut306 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 1) (op (var 2) (var 3)))) , (var 4)) → ⊥
  cut306  adequate = bad306  (Adequate.valid adequate Two boolean env10)
  bad307 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b1 (bop b0 b0))) b0 → ⊥
  bad307  p = false≢true (sym (cong lower p))
  cut307 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (var 0) (var 0)))) , (var 0)) → ⊥
  cut307  adequate = bad307  (Adequate.valid adequate Two boolean env1)
  bad308 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b1 (bop b0 b0))) b0 → ⊥
  bad308  p = false≢true (sym (cong lower p))
  cut308 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (var 0) (var 0)))) , (var 1)) → ⊥
  cut308  adequate = bad308  (Adequate.valid adequate Two boolean env1)
  bad309 : PathP (λ _ → Two) (bop (bop b1 b0) (bop b1 (bop b1 b1))) b1 → ⊥
  bad309  p = false≢true (cong lower p)
  cut309 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (var 0) (var 0)))) , (var 2)) → ⊥
  cut309  adequate = bad309  (Adequate.valid adequate Two boolean env11)
  bad310 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop b0 b0))) b1 → ⊥
  bad310  p = false≢true (cong lower p)
  cut310 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (var 0) (var 0)))) , (var 3)) → ⊥
  cut310  adequate = bad310  (Adequate.valid adequate Two boolean env3)
  bad311 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b1 (bop b0 b0))) b0 → ⊥
  bad311  p = false≢true (sym (cong lower p))
  cut311 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (var 0) (var 1)))) , (var 0)) → ⊥
  cut311  adequate = bad311  (Adequate.valid adequate Two boolean env1)
  bad312 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b1 (bop b0 b0))) b0 → ⊥
  bad312  p = false≢true (sym (cong lower p))
  cut312 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (var 0) (var 1)))) , (var 1)) → ⊥
  cut312  adequate = bad312  (Adequate.valid adequate Two boolean env1)
  env13 : ℕ → Two
  env13 zero = b1
  env13 (suc zero) = b1
  env13 (suc (suc zero)) = b0
  env13 (suc (suc (suc rest))) = b0
  bad313 : PathP (λ _ → Two) (bop (bop b1 b1) (bop b0 (bop b1 b1))) b0 → ⊥
  bad313  p = false≢true (sym (cong lower p))
  cut313 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (var 0) (var 1)))) , (var 2)) → ⊥
  cut313  adequate = bad313  (Adequate.valid adequate Two boolean env13)
  bad314 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop b0 b0))) b1 → ⊥
  bad314  p = false≢true (cong lower p)
  cut314 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (var 0) (var 1)))) , (var 3)) → ⊥
  cut314  adequate = bad314  (Adequate.valid adequate Two boolean env3)
  bad315 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b1 (bop b0 b1))) b0 → ⊥
  bad315  p = false≢true (sym (cong lower p))
  cut315 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (var 0) (var 2)))) , (var 0)) → ⊥
  cut315  adequate = bad315  (Adequate.valid adequate Two boolean env1)
  bad316 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b1 (bop b0 b1))) b0 → ⊥
  bad316  p = false≢true (sym (cong lower p))
  cut316 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (var 0) (var 2)))) , (var 1)) → ⊥
  cut316  adequate = bad316  (Adequate.valid adequate Two boolean env1)
  bad317 : PathP (λ _ → Two) (bop (bop b1 b0) (bop b1 (bop b1 b1))) b1 → ⊥
  bad317  p = false≢true (cong lower p)
  cut317 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (var 0) (var 2)))) , (var 2)) → ⊥
  cut317  adequate = bad317  (Adequate.valid adequate Two boolean env11)
  bad318 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop b0 b0))) b1 → ⊥
  bad318  p = false≢true (cong lower p)
  cut318 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (var 0) (var 2)))) , (var 3)) → ⊥
  cut318  adequate = bad318  (Adequate.valid adequate Two boolean env3)
  bad319 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b1 (bop b0 b0))) b0 → ⊥
  bad319  p = false≢true (sym (cong lower p))
  cut319 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (var 0) (var 3)))) , (var 0)) → ⊥
  cut319  adequate = bad319  (Adequate.valid adequate Two boolean env9)
  bad320 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b1 (bop b0 b0))) b0 → ⊥
  bad320  p = false≢true (sym (cong lower p))
  cut320 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (var 0) (var 3)))) , (var 1)) → ⊥
  cut320  adequate = bad320  (Adequate.valid adequate Two boolean env9)
  bad321 : PathP (λ _ → Two) (bop (bop b1 b0) (bop b1 (bop b1 b1))) b1 → ⊥
  bad321  p = false≢true (cong lower p)
  cut321 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (var 0) (var 3)))) , (var 2)) → ⊥
  cut321  adequate = bad321  (Adequate.valid adequate Two boolean env12)
  bad322 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop b0 b1))) b1 → ⊥
  bad322  p = false≢true (cong lower p)
  cut322 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (var 0) (var 3)))) , (var 3)) → ⊥
  cut322  adequate = bad322  (Adequate.valid adequate Two boolean env3)
  bad323 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop b0 b0))) b1 → ⊥
  bad323  p = false≢true (cong lower p)
  cut323 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (var 0) (var 3)))) , (var 4)) → ⊥
  cut323  adequate = bad323  (Adequate.valid adequate Two boolean env10)
  bad324 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b1 (bop b0 b0))) b0 → ⊥
  bad324  p = false≢true (sym (cong lower p))
  cut324 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (var 1) (var 0)))) , (var 0)) → ⊥
  cut324  adequate = bad324  (Adequate.valid adequate Two boolean env1)
  bad325 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b1 (bop b0 b0))) b0 → ⊥
  bad325  p = false≢true (sym (cong lower p))
  cut325 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (var 1) (var 0)))) , (var 1)) → ⊥
  cut325  adequate = bad325  (Adequate.valid adequate Two boolean env1)
  bad326 : PathP (λ _ → Two) (bop (bop b1 b1) (bop b0 (bop b1 b1))) b0 → ⊥
  bad326  p = false≢true (sym (cong lower p))
  cut326 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (var 1) (var 0)))) , (var 2)) → ⊥
  cut326  adequate = bad326  (Adequate.valid adequate Two boolean env13)
  bad327 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop b0 b0))) b1 → ⊥
  bad327  p = false≢true (cong lower p)
  cut327 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (var 1) (var 0)))) , (var 3)) → ⊥
  cut327  adequate = bad327  (Adequate.valid adequate Two boolean env3)
  bad328 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b1 (bop b0 b0))) b0 → ⊥
  bad328  p = false≢true (sym (cong lower p))
  cut328 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (var 1) (var 1)))) , (var 0)) → ⊥
  cut328  adequate = bad328  (Adequate.valid adequate Two boolean env1)
  bad329 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b1 (bop b0 b0))) b0 → ⊥
  bad329  p = false≢true (sym (cong lower p))
  cut329 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (var 1) (var 1)))) , (var 1)) → ⊥
  cut329  adequate = bad329  (Adequate.valid adequate Two boolean env1)
  bad330 : PathP (λ _ → Two) (bop (bop b0 b1) (bop b1 (bop b1 b1))) b1 → ⊥
  bad330  p = false≢true (cong lower p)
  cut330 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (var 1) (var 1)))) , (var 2)) → ⊥
  cut330  adequate = bad330  (Adequate.valid adequate Two boolean env6)
  bad331 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop b0 b0))) b1 → ⊥
  bad331  p = false≢true (cong lower p)
  cut331 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (var 1) (var 1)))) , (var 3)) → ⊥
  cut331  adequate = bad331  (Adequate.valid adequate Two boolean env3)
  bad332 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b1 (bop b0 b1))) b0 → ⊥
  bad332  p = false≢true (sym (cong lower p))
  cut332 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (var 1) (var 2)))) , (var 0)) → ⊥
  cut332  adequate = bad332  (Adequate.valid adequate Two boolean env1)
  bad333 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b1 (bop b0 b1))) b0 → ⊥
  bad333  p = false≢true (sym (cong lower p))
  cut333 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (var 1) (var 2)))) , (var 1)) → ⊥
  cut333  adequate = bad333  (Adequate.valid adequate Two boolean env1)
  bad334 : PathP (λ _ → Two) (bop (bop b0 b1) (bop b1 (bop b1 b1))) b1 → ⊥
  bad334  p = false≢true (cong lower p)
  cut334 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (var 1) (var 2)))) , (var 2)) → ⊥
  cut334  adequate = bad334  (Adequate.valid adequate Two boolean env6)
  bad335 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop b0 b0))) b1 → ⊥
  bad335  p = false≢true (cong lower p)
  cut335 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (var 1) (var 2)))) , (var 3)) → ⊥
  cut335  adequate = bad335  (Adequate.valid adequate Two boolean env3)
  bad336 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b1 (bop b0 b0))) b0 → ⊥
  bad336  p = false≢true (sym (cong lower p))
  cut336 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (var 1) (var 3)))) , (var 0)) → ⊥
  cut336  adequate = bad336  (Adequate.valid adequate Two boolean env9)
  bad337 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b1 (bop b0 b0))) b0 → ⊥
  bad337  p = false≢true (sym (cong lower p))
  cut337 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (var 1) (var 3)))) , (var 1)) → ⊥
  cut337  adequate = bad337  (Adequate.valid adequate Two boolean env9)
  bad338 : PathP (λ _ → Two) (bop (bop b0 b1) (bop b1 (bop b1 b1))) b1 → ⊥
  bad338  p = false≢true (cong lower p)
  cut338 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (var 1) (var 3)))) , (var 2)) → ⊥
  cut338  adequate = bad338  (Adequate.valid adequate Two boolean env8)
  bad339 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop b0 b1))) b1 → ⊥
  bad339  p = false≢true (cong lower p)
  cut339 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (var 1) (var 3)))) , (var 3)) → ⊥
  cut339  adequate = bad339  (Adequate.valid adequate Two boolean env3)
  bad340 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop b0 b0))) b1 → ⊥
  bad340  p = false≢true (cong lower p)
  cut340 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (var 1) (var 3)))) , (var 4)) → ⊥
  cut340  adequate = bad340  (Adequate.valid adequate Two boolean env10)
  bad341 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b1 (bop b1 b0))) b0 → ⊥
  bad341  p = false≢true (sym (cong lower p))
  cut341 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (var 2) (var 0)))) , (var 0)) → ⊥
  cut341  adequate = bad341  (Adequate.valid adequate Two boolean env1)
  bad342 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b1 (bop b1 b0))) b0 → ⊥
  bad342  p = false≢true (sym (cong lower p))
  cut342 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (var 2) (var 0)))) , (var 1)) → ⊥
  cut342  adequate = bad342  (Adequate.valid adequate Two boolean env1)
  bad343 : PathP (λ _ → Two) (bop (bop b1 b0) (bop b1 (bop b1 b1))) b1 → ⊥
  bad343  p = false≢true (cong lower p)
  cut343 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (var 2) (var 0)))) , (var 2)) → ⊥
  cut343  adequate = bad343  (Adequate.valid adequate Two boolean env11)
  bad344 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop b0 b0))) b1 → ⊥
  bad344  p = false≢true (cong lower p)
  cut344 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (var 2) (var 0)))) , (var 3)) → ⊥
  cut344  adequate = bad344  (Adequate.valid adequate Two boolean env3)
  bad345 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b1 (bop b1 b0))) b0 → ⊥
  bad345  p = false≢true (sym (cong lower p))
  cut345 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (var 2) (var 1)))) , (var 0)) → ⊥
  cut345  adequate = bad345  (Adequate.valid adequate Two boolean env1)
  bad346 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b1 (bop b1 b0))) b0 → ⊥
  bad346  p = false≢true (sym (cong lower p))
  cut346 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (var 2) (var 1)))) , (var 1)) → ⊥
  cut346  adequate = bad346  (Adequate.valid adequate Two boolean env1)
  bad347 : PathP (λ _ → Two) (bop (bop b0 b1) (bop b1 (bop b1 b1))) b1 → ⊥
  bad347  p = false≢true (cong lower p)
  cut347 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (var 2) (var 1)))) , (var 2)) → ⊥
  cut347  adequate = bad347  (Adequate.valid adequate Two boolean env6)
  bad348 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop b0 b0))) b1 → ⊥
  bad348  p = false≢true (cong lower p)
  cut348 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (var 2) (var 1)))) , (var 3)) → ⊥
  cut348  adequate = bad348  (Adequate.valid adequate Two boolean env3)
  bad349 : PathP (λ _ → Two) (bop (bop b1 b0) (bop b0 (bop b0 b0))) b1 → ⊥
  bad349  p = false≢true (cong lower p)
  cut349 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (var 2) (var 2)))) , (var 0)) → ⊥
  cut349  adequate = bad349  (Adequate.valid adequate Two boolean env5)
  bad350 : PathP (λ _ → Two) (bop (bop b0 b1) (bop b0 (bop b0 b0))) b1 → ⊥
  bad350  p = false≢true (cong lower p)
  cut350 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (var 2) (var 2)))) , (var 1)) → ⊥
  cut350  adequate = bad350  (Adequate.valid adequate Two boolean env2)
  bad351 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b1 (bop b1 b1))) b1 → ⊥
  bad351  p = false≢true (cong lower p)
  cut351 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (var 2) (var 2)))) , (var 2)) → ⊥
  cut351  adequate = bad351  (Adequate.valid adequate Two boolean env1)
  bad352 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop b0 b0))) b1 → ⊥
  bad352  p = false≢true (cong lower p)
  cut352 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (var 2) (var 2)))) , (var 3)) → ⊥
  cut352  adequate = bad352  (Adequate.valid adequate Two boolean env3)
  bad353 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b1 (bop b1 b0))) b0 → ⊥
  bad353  p = false≢true (sym (cong lower p))
  cut353 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (var 2) (var 3)))) , (var 0)) → ⊥
  cut353  adequate = bad353  (Adequate.valid adequate Two boolean env9)
  bad354 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b1 (bop b1 b0))) b0 → ⊥
  bad354  p = false≢true (sym (cong lower p))
  cut354 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (var 2) (var 3)))) , (var 1)) → ⊥
  cut354  adequate = bad354  (Adequate.valid adequate Two boolean env9)
  env14 : ℕ → Two
  env14 zero = b0
  env14 (suc zero) = b0
  env14 (suc (suc zero)) = b1
  env14 (suc (suc (suc zero))) = b1
  env14 (suc (suc (suc (suc rest)))) = b0
  bad355 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b1 (bop b1 b1))) b1 → ⊥
  bad355  p = false≢true (cong lower p)
  cut355 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (var 2) (var 3)))) , (var 2)) → ⊥
  cut355  adequate = bad355  (Adequate.valid adequate Two boolean env14)
  bad356 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop b0 b1))) b1 → ⊥
  bad356  p = false≢true (cong lower p)
  cut356 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (var 2) (var 3)))) , (var 3)) → ⊥
  cut356  adequate = bad356  (Adequate.valid adequate Two boolean env3)
  bad357 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop b0 b0))) b1 → ⊥
  bad357  p = false≢true (cong lower p)
  cut357 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (var 2) (var 3)))) , (var 4)) → ⊥
  cut357  adequate = bad357  (Adequate.valid adequate Two boolean env10)
  bad358 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b1 (bop b0 b0))) b0 → ⊥
  bad358  p = false≢true (sym (cong lower p))
  cut358 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (var 3) (var 0)))) , (var 0)) → ⊥
  cut358  adequate = bad358  (Adequate.valid adequate Two boolean env9)
  bad359 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b1 (bop b0 b0))) b0 → ⊥
  bad359  p = false≢true (sym (cong lower p))
  cut359 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (var 3) (var 0)))) , (var 1)) → ⊥
  cut359  adequate = bad359  (Adequate.valid adequate Two boolean env9)
  bad360 : PathP (λ _ → Two) (bop (bop b1 b0) (bop b1 (bop b1 b1))) b1 → ⊥
  bad360  p = false≢true (cong lower p)
  cut360 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (var 3) (var 0)))) , (var 2)) → ⊥
  cut360  adequate = bad360  (Adequate.valid adequate Two boolean env12)
  bad361 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop b1 b0))) b1 → ⊥
  bad361  p = false≢true (cong lower p)
  cut361 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (var 3) (var 0)))) , (var 3)) → ⊥
  cut361  adequate = bad361  (Adequate.valid adequate Two boolean env3)
  bad362 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop b0 b0))) b1 → ⊥
  bad362  p = false≢true (cong lower p)
  cut362 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (var 3) (var 0)))) , (var 4)) → ⊥
  cut362  adequate = bad362  (Adequate.valid adequate Two boolean env10)
  bad363 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b1 (bop b0 b0))) b0 → ⊥
  bad363  p = false≢true (sym (cong lower p))
  cut363 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (var 3) (var 1)))) , (var 0)) → ⊥
  cut363  adequate = bad363  (Adequate.valid adequate Two boolean env9)
  bad364 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b1 (bop b0 b0))) b0 → ⊥
  bad364  p = false≢true (sym (cong lower p))
  cut364 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (var 3) (var 1)))) , (var 1)) → ⊥
  cut364  adequate = bad364  (Adequate.valid adequate Two boolean env9)
  bad365 : PathP (λ _ → Two) (bop (bop b0 b1) (bop b1 (bop b1 b1))) b1 → ⊥
  bad365  p = false≢true (cong lower p)
  cut365 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (var 3) (var 1)))) , (var 2)) → ⊥
  cut365  adequate = bad365  (Adequate.valid adequate Two boolean env8)
  bad366 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop b1 b0))) b1 → ⊥
  bad366  p = false≢true (cong lower p)
  cut366 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (var 3) (var 1)))) , (var 3)) → ⊥
  cut366  adequate = bad366  (Adequate.valid adequate Two boolean env3)
  bad367 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop b0 b0))) b1 → ⊥
  bad367  p = false≢true (cong lower p)
  cut367 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (var 3) (var 1)))) , (var 4)) → ⊥
  cut367  adequate = bad367  (Adequate.valid adequate Two boolean env10)
  bad368 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b1 (bop b0 b1))) b0 → ⊥
  bad368  p = false≢true (sym (cong lower p))
  cut368 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (var 3) (var 2)))) , (var 0)) → ⊥
  cut368  adequate = bad368  (Adequate.valid adequate Two boolean env9)
  bad369 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b1 (bop b0 b1))) b0 → ⊥
  bad369  p = false≢true (sym (cong lower p))
  cut369 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (var 3) (var 2)))) , (var 1)) → ⊥
  cut369  adequate = bad369  (Adequate.valid adequate Two boolean env9)
  bad370 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b1 (bop b1 b1))) b1 → ⊥
  bad370  p = false≢true (cong lower p)
  cut370 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (var 3) (var 2)))) , (var 2)) → ⊥
  cut370  adequate = bad370  (Adequate.valid adequate Two boolean env14)
  bad371 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop b1 b0))) b1 → ⊥
  bad371  p = false≢true (cong lower p)
  cut371 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (var 3) (var 2)))) , (var 3)) → ⊥
  cut371  adequate = bad371  (Adequate.valid adequate Two boolean env3)
  bad372 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop b0 b0))) b1 → ⊥
  bad372  p = false≢true (cong lower p)
  cut372 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (var 3) (var 2)))) , (var 4)) → ⊥
  cut372  adequate = bad372  (Adequate.valid adequate Two boolean env10)
  bad373 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b1 (bop b0 b0))) b0 → ⊥
  bad373  p = false≢true (sym (cong lower p))
  cut373 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (var 3) (var 3)))) , (var 0)) → ⊥
  cut373  adequate = bad373  (Adequate.valid adequate Two boolean env9)
  bad374 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b1 (bop b0 b0))) b0 → ⊥
  bad374  p = false≢true (sym (cong lower p))
  cut374 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (var 3) (var 3)))) , (var 1)) → ⊥
  cut374  adequate = bad374  (Adequate.valid adequate Two boolean env9)
  bad375 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b1 (bop b1 b1))) b1 → ⊥
  bad375  p = false≢true (cong lower p)
  cut375 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (var 3) (var 3)))) , (var 2)) → ⊥
  cut375  adequate = bad375  (Adequate.valid adequate Two boolean env14)
  bad376 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop b1 b1))) b1 → ⊥
  bad376  p = false≢true (cong lower p)
  cut376 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (var 3) (var 3)))) , (var 3)) → ⊥
  cut376  adequate = bad376  (Adequate.valid adequate Two boolean env3)
  bad377 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop b0 b0))) b1 → ⊥
  bad377  p = false≢true (cong lower p)
  cut377 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (var 3) (var 3)))) , (var 4)) → ⊥
  cut377  adequate = bad377  (Adequate.valid adequate Two boolean env10)
  env15 : ℕ → Two
  env15 zero = b0
  env15 (suc zero) = b0
  env15 (suc (suc zero)) = b1
  env15 (suc (suc (suc zero))) = b0
  env15 (suc (suc (suc (suc zero)))) = b0
  env15 (suc (suc (suc (suc (suc rest))))) = b0
  bad378 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b1 (bop b0 b0))) b0 → ⊥
  bad378  p = false≢true (sym (cong lower p))
  cut378 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (var 3) (var 4)))) , (var 0)) → ⊥
  cut378  adequate = bad378  (Adequate.valid adequate Two boolean env15)
  bad379 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b1 (bop b0 b0))) b0 → ⊥
  bad379  p = false≢true (sym (cong lower p))
  cut379 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (var 3) (var 4)))) , (var 1)) → ⊥
  cut379  adequate = bad379  (Adequate.valid adequate Two boolean env15)
  env16 : ℕ → Two
  env16 zero = b0
  env16 (suc zero) = b0
  env16 (suc (suc zero)) = b1
  env16 (suc (suc (suc zero))) = b1
  env16 (suc (suc (suc (suc zero)))) = b1
  env16 (suc (suc (suc (suc (suc rest))))) = b0
  bad380 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b1 (bop b1 b1))) b1 → ⊥
  bad380  p = false≢true (cong lower p)
  cut380 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (var 3) (var 4)))) , (var 2)) → ⊥
  cut380  adequate = bad380  (Adequate.valid adequate Two boolean env16)
  env17 : ℕ → Two
  env17 zero = b0
  env17 (suc zero) = b0
  env17 (suc (suc zero)) = b0
  env17 (suc (suc (suc zero))) = b1
  env17 (suc (suc (suc (suc zero)))) = b0
  env17 (suc (suc (suc (suc (suc rest))))) = b0
  bad381 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop b1 b0))) b1 → ⊥
  bad381  p = false≢true (cong lower p)
  cut381 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (var 3) (var 4)))) , (var 3)) → ⊥
  cut381  adequate = bad381  (Adequate.valid adequate Two boolean env17)
  bad382 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop b0 b1))) b1 → ⊥
  bad382  p = false≢true (cong lower p)
  cut382 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (var 3) (var 4)))) , (var 4)) → ⊥
  cut382  adequate = bad382  (Adequate.valid adequate Two boolean env10)
  env18 : ℕ → Two
  env18 zero = b0
  env18 (suc zero) = b0
  env18 (suc (suc zero)) = b0
  env18 (suc (suc (suc zero))) = b0
  env18 (suc (suc (suc (suc zero)))) = b0
  env18 (suc (suc (suc (suc (suc zero))))) = b1
  env18 (suc (suc (suc (suc (suc (suc rest)))))) = b0
  bad383 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop b0 b0))) b1 → ⊥
  bad383  p = false≢true (cong lower p)
  cut383 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (var 3) (var 4)))) , (var 5)) → ⊥
  cut383  adequate = bad383  (Adequate.valid adequate Two boolean env18)
