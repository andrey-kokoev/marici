{-# OPTIONS --safe --cubical --guardedness #-}
module GeneratedMinimumShape28 where
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
  holds90 : (z0 z1 z2 z3 z4 : A2) → z0 ≡ (mul2 (mul2 z0 z1) (mul2 (mul2 z2 z3) z4))
  holds90 z0 z1 z2 z3 z4 = refl
  cut90 : (x2 x3 x4 x5 : ℕ) → Adequate {ℓ} ((var 0) , (op (op (var 0) (var x2)) (op (op (var x3) (var x4)) (var x5)))) → ⊥
  cut90 x2 x3 x4 x5 = reject2 ((var 0) , (op (op (var 0) (var x2)) (op (op (var x3) (var x4)) (var x5)))) (λ env → holds90 (env 0) (env x2) (env x3) (env x4) (env x5))
  env0 : ℕ → Two
  env0 zero = b1
  env0 (suc zero) = b0
  env0 (suc (suc rest)) = b0
  bad91 : (z2 : Two) → PathP (λ _ → Two) b1 (bop (bop b0 b1) (bop (bop b1 b1) z2)) → ⊥
  bad91 z2 p = false≢true (sym (cong lower p))
  cut91 : (x5 : ℕ) → Adequate {ℓ} ((var 0) , (op (op (var 1) (var 0)) (op (op (var 0) (var 0)) (var x5)))) → ⊥
  cut91 x5 adequate = bad91 (env0 x5) (Adequate.valid adequate Two boolean env0)
  holds92 : (z0 z1 : A3) → z0 ≡ (mul3 (mul3 z1 z0) (mul3 (mul3 z0 z1) z0))
  holds92 z0 z1 = refl
  cut92 : Adequate {ℓ} ((var 0) , (op (op (var 1) (var 0)) (op (op (var 0) (var 1)) (var 0)))) → ⊥
  cut92  = reject3 ((var 0) , (op (op (var 1) (var 0)) (op (op (var 0) (var 1)) (var 0)))) (λ env → holds92 (env 0) (env 1))
  env1 : ℕ → Two
  env1 zero = b0
  env1 (suc zero) = b1
  env1 (suc (suc rest)) = b0
  bad93 : PathP (λ _ → Two) b0 (bop (bop b1 b0) (bop (bop b0 b1) b1)) → ⊥
  bad93  p = false≢true (cong lower p)
  cut93 : Adequate {ℓ} ((var 0) , (op (op (var 1) (var 0)) (op (op (var 0) (var 1)) (var 1)))) → ⊥
  cut93  adequate = bad93  (Adequate.valid adequate Two boolean env1)
  env2 : ℕ → Two
  env2 zero = b0
  env2 (suc zero) = b0
  env2 (suc (suc zero)) = b1
  env2 (suc (suc (suc rest))) = b0
  bad94 : PathP (λ _ → Two) b0 (bop (bop b0 b0) (bop (bop b0 b0) b1)) → ⊥
  bad94  p = false≢true (cong lower p)
  cut94 : Adequate {ℓ} ((var 0) , (op (op (var 1) (var 0)) (op (op (var 0) (var 1)) (var 2)))) → ⊥
  cut94  adequate = bad94  (Adequate.valid adequate Two boolean env2)
  env3 : ℕ → Two
  env3 zero = b1
  env3 (suc zero) = b0
  env3 (suc (suc zero)) = b1
  env3 (suc (suc (suc rest))) = b0
  bad95 : (z3 : Two) → PathP (λ _ → Two) b1 (bop (bop b0 b1) (bop (bop b1 b1) z3)) → ⊥
  bad95 z3 p = false≢true (sym (cong lower p))
  cut95 : (x5 : ℕ) → Adequate {ℓ} ((var 0) , (op (op (var 1) (var 0)) (op (op (var 0) (var 2)) (var x5)))) → ⊥
  cut95 x5 adequate = bad95 (env3 x5) (Adequate.valid adequate Two boolean env3)
  holds96 : (z0 z1 : A3) → z0 ≡ (mul3 (mul3 z1 z0) (mul3 (mul3 z1 z0) z0))
  holds96 z0 z1 = refl
  cut96 : Adequate {ℓ} ((var 0) , (op (op (var 1) (var 0)) (op (op (var 1) (var 0)) (var 0)))) → ⊥
  cut96  = reject3 ((var 0) , (op (op (var 1) (var 0)) (op (op (var 1) (var 0)) (var 0)))) (λ env → holds96 (env 0) (env 1))
  bad97 : PathP (λ _ → Two) b0 (bop (bop b1 b0) (bop (bop b1 b0) b1)) → ⊥
  bad97  p = false≢true (cong lower p)
  cut97 : Adequate {ℓ} ((var 0) , (op (op (var 1) (var 0)) (op (op (var 1) (var 0)) (var 1)))) → ⊥
  cut97  adequate = bad97  (Adequate.valid adequate Two boolean env1)
  bad98 : PathP (λ _ → Two) b0 (bop (bop b0 b0) (bop (bop b0 b0) b1)) → ⊥
  bad98  p = false≢true (cong lower p)
  cut98 : Adequate {ℓ} ((var 0) , (op (op (var 1) (var 0)) (op (op (var 1) (var 0)) (var 2)))) → ⊥
  cut98  adequate = bad98  (Adequate.valid adequate Two boolean env2)
  holds99 : (z0 z1 : A3) → z0 ≡ (mul3 (mul3 z1 z0) (mul3 (mul3 z1 z1) z0))
  holds99 z0 z1 = refl
  cut99 : Adequate {ℓ} ((var 0) , (op (op (var 1) (var 0)) (op (op (var 1) (var 1)) (var 0)))) → ⊥
  cut99  = reject3 ((var 0) , (op (op (var 1) (var 0)) (op (op (var 1) (var 1)) (var 0)))) (λ env → holds99 (env 0) (env 1))
  bad100 : PathP (λ _ → Two) b1 (bop (bop b0 b1) (bop (bop b0 b0) b0)) → ⊥
  bad100  p = false≢true (sym (cong lower p))
  cut100 : Adequate {ℓ} ((var 0) , (op (op (var 1) (var 0)) (op (op (var 1) (var 1)) (var 1)))) → ⊥
  cut100  adequate = bad100  (Adequate.valid adequate Two boolean env0)
  bad101 : PathP (λ _ → Two) b0 (bop (bop b0 b0) (bop (bop b0 b0) b1)) → ⊥
  bad101  p = false≢true (cong lower p)
  cut101 : Adequate {ℓ} ((var 0) , (op (op (var 1) (var 0)) (op (op (var 1) (var 1)) (var 2)))) → ⊥
  cut101  adequate = bad101  (Adequate.valid adequate Two boolean env2)
  holds102 : (z0 z1 z2 : A3) → z0 ≡ (mul3 (mul3 z1 z0) (mul3 (mul3 z1 z2) z0))
  holds102 z0 z1 z2 = refl
  cut102 : Adequate {ℓ} ((var 0) , (op (op (var 1) (var 0)) (op (op (var 1) (var 2)) (var 0)))) → ⊥
  cut102  = reject3 ((var 0) , (op (op (var 1) (var 0)) (op (op (var 1) (var 2)) (var 0)))) (λ env → holds102 (env 0) (env 1) (env 2))
  env4 : ℕ → Two
  env4 zero = b0
  env4 (suc zero) = b1
  env4 (suc (suc zero)) = b0
  env4 (suc (suc (suc rest))) = b0
  bad103 : PathP (λ _ → Two) b0 (bop (bop b1 b0) (bop (bop b1 b0) b1)) → ⊥
  bad103  p = false≢true (cong lower p)
  cut103 : Adequate {ℓ} ((var 0) , (op (op (var 1) (var 0)) (op (op (var 1) (var 2)) (var 1)))) → ⊥
  cut103  adequate = bad103  (Adequate.valid adequate Two boolean env4)
  bad104 : PathP (λ _ → Two) b0 (bop (bop b0 b0) (bop (bop b0 b1) b1)) → ⊥
  bad104  p = false≢true (cong lower p)
  cut104 : Adequate {ℓ} ((var 0) , (op (op (var 1) (var 0)) (op (op (var 1) (var 2)) (var 2)))) → ⊥
  cut104  adequate = bad104  (Adequate.valid adequate Two boolean env2)
  env5 : ℕ → Two
  env5 zero = b0
  env5 (suc zero) = b0
  env5 (suc (suc zero)) = b0
  env5 (suc (suc (suc zero))) = b1
  env5 (suc (suc (suc (suc rest)))) = b0
  bad105 : PathP (λ _ → Two) b0 (bop (bop b0 b0) (bop (bop b0 b0) b1)) → ⊥
  bad105  p = false≢true (cong lower p)
  cut105 : Adequate {ℓ} ((var 0) , (op (op (var 1) (var 0)) (op (op (var 1) (var 2)) (var 3)))) → ⊥
  cut105  adequate = bad105  (Adequate.valid adequate Two boolean env5)
  bad106 : (z3 : Two) → PathP (λ _ → Two) b1 (bop (bop b0 b1) (bop (bop b1 b1) z3)) → ⊥
  bad106 z3 p = false≢true (sym (cong lower p))
  cut106 : (x5 : ℕ) → Adequate {ℓ} ((var 0) , (op (op (var 1) (var 0)) (op (op (var 2) (var 0)) (var x5)))) → ⊥
  cut106 x5 adequate = bad106 (env3 x5) (Adequate.valid adequate Two boolean env3)
  holds107 : (z0 z1 z2 : A3) → z0 ≡ (mul3 (mul3 z1 z0) (mul3 (mul3 z2 z1) z0))
  holds107 z0 z1 z2 = refl
  cut107 : Adequate {ℓ} ((var 0) , (op (op (var 1) (var 0)) (op (op (var 2) (var 1)) (var 0)))) → ⊥
  cut107  = reject3 ((var 0) , (op (op (var 1) (var 0)) (op (op (var 2) (var 1)) (var 0)))) (λ env → holds107 (env 0) (env 1) (env 2))
  bad108 : PathP (λ _ → Two) b0 (bop (bop b1 b0) (bop (bop b0 b1) b1)) → ⊥
  bad108  p = false≢true (cong lower p)
  cut108 : Adequate {ℓ} ((var 0) , (op (op (var 1) (var 0)) (op (op (var 2) (var 1)) (var 1)))) → ⊥
  cut108  adequate = bad108  (Adequate.valid adequate Two boolean env4)
  bad109 : PathP (λ _ → Two) b0 (bop (bop b0 b0) (bop (bop b1 b0) b1)) → ⊥
  bad109  p = false≢true (cong lower p)
  cut109 : Adequate {ℓ} ((var 0) , (op (op (var 1) (var 0)) (op (op (var 2) (var 1)) (var 2)))) → ⊥
  cut109  adequate = bad109  (Adequate.valid adequate Two boolean env2)
  bad110 : PathP (λ _ → Two) b0 (bop (bop b0 b0) (bop (bop b0 b0) b1)) → ⊥
  bad110  p = false≢true (cong lower p)
  cut110 : Adequate {ℓ} ((var 0) , (op (op (var 1) (var 0)) (op (op (var 2) (var 1)) (var 3)))) → ⊥
  cut110  adequate = bad110  (Adequate.valid adequate Two boolean env5)
  bad111 : (z3 : Two) → PathP (λ _ → Two) b1 (bop (bop b0 b1) (bop (bop b1 b1) z3)) → ⊥
  bad111 z3 p = false≢true (sym (cong lower p))
  cut111 : (x5 : ℕ) → Adequate {ℓ} ((var 0) , (op (op (var 1) (var 0)) (op (op (var 2) (var 2)) (var x5)))) → ⊥
  cut111 x5 adequate = bad111 (env3 x5) (Adequate.valid adequate Two boolean env3)
  env6 : ℕ → Two
  env6 zero = b1
  env6 (suc zero) = b0
  env6 (suc (suc zero)) = b1
  env6 (suc (suc (suc zero))) = b1
  env6 (suc (suc (suc (suc rest)))) = b0
  bad112 : (z4 : Two) → PathP (λ _ → Two) b1 (bop (bop b0 b1) (bop (bop b1 b1) z4)) → ⊥
  bad112 z4 p = false≢true (sym (cong lower p))
  cut112 : (x5 : ℕ) → Adequate {ℓ} ((var 0) , (op (op (var 1) (var 0)) (op (op (var 2) (var 3)) (var x5)))) → ⊥
  cut112 x5 adequate = bad112 (env6 x5) (Adequate.valid adequate Two boolean env6)
  bad113 : (z2 z3 z4 : Two) → PathP (λ _ → Two) b0 (bop (bop b1 b1) (bop (bop z2 z3) z4)) → ⊥
  bad113 z2 z3 z4 p = false≢true (cong lower p)
  cut113 : (x3 x4 x5 : ℕ) → Adequate {ℓ} ((var 0) , (op (op (var 1) (var 1)) (op (op (var x3) (var x4)) (var x5)))) → ⊥
  cut113 x3 x4 x5 adequate = bad113 (env1 x3) (env1 x4) (env1 x5) (Adequate.valid adequate Two boolean env1)
  env7 : ℕ → Two
  env7 zero = b0
  env7 (suc zero) = b1
  env7 (suc (suc zero)) = b1
  env7 (suc (suc (suc rest))) = b0
  bad114 : (z3 z4 z5 : Two) → PathP (λ _ → Two) b0 (bop (bop b1 b1) (bop (bop z3 z4) z5)) → ⊥
  bad114 z3 z4 z5 p = false≢true (cong lower p)
  cut114 : (x3 x4 x5 : ℕ) → Adequate {ℓ} ((var 0) , (op (op (var 1) (var 2)) (op (op (var x3) (var x4)) (var x5)))) → ⊥
  cut114 x3 x4 x5 adequate = bad114 (env7 x3) (env7 x4) (env7 x5) (Adequate.valid adequate Two boolean env7)
