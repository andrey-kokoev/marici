{-# OPTIONS --safe --cubical --guardedness #-}
module GeneratedMinimumShape90 where
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
  holds1235 : (z0 z1 z2 z3 z4 z5 : A2) → z0 ≡ (mul2 (mul2 (mul2 z0 (mul2 z1 z2)) z3) (mul2 z4 z5))
  holds1235 z0 z1 z2 z3 z4 z5 = refl
  cut1235 : (x2 x3 x4 x5 x6 : ℕ) → Adequate {ℓ} ((var 0) , (op (op (op (var 0) (op (var x2) (var x3))) (var x4)) (op (var x5) (var x6)))) → ⊥
  cut1235 x2 x3 x4 x5 x6 = reject2 ((var 0) , (op (op (op (var 0) (op (var x2) (var x3))) (var x4)) (op (var x5) (var x6)))) (λ env → holds1235 (env 0) (env x2) (env x3) (env x4) (env x5) (env x6))
  holds1236 : (z0 z1 z2 : A10) → z0 ≡ (mul10 (mul10 (mul10 z1 (mul10 z0 z0)) z0) (mul10 z0 z2))
  holds1236 m10c0 m10c0 m10c0 = refl
  holds1236 m10c0 m10c0 m10c1 = refl
  holds1236 m10c0 m10c0 m10c2 = refl
  holds1236 m10c0 m10c1 m10c0 = refl
  holds1236 m10c0 m10c1 m10c1 = refl
  holds1236 m10c0 m10c1 m10c2 = refl
  holds1236 m10c0 m10c2 m10c0 = refl
  holds1236 m10c0 m10c2 m10c1 = refl
  holds1236 m10c0 m10c2 m10c2 = refl
  holds1236 m10c1 m10c0 z2 = refl
  holds1236 m10c1 m10c1 z2 = refl
  holds1236 m10c1 m10c2 z2 = refl
  holds1236 m10c2 m10c0 z2 = refl
  holds1236 m10c2 m10c1 z2 = refl
  holds1236 m10c2 m10c2 z2 = refl
  cut1236 : (x6 : ℕ) → Adequate {ℓ} ((var 0) , (op (op (op (var 1) (op (var 0) (var 0))) (var 0)) (op (var 0) (var x6)))) → ⊥
  cut1236 x6 = reject10 ((var 0) , (op (op (op (var 1) (op (var 0) (var 0))) (var 0)) (op (var 0) (var x6)))) (λ env → holds1236 (env 0) (env 1) (env x6))
  holds1237 : (z0 z1 : A3) → z0 ≡ (mul3 (mul3 (mul3 z1 (mul3 z0 z0)) z0) (mul3 z1 z0))
  holds1237 z0 z1 = refl
  cut1237 : Adequate {ℓ} ((var 0) , (op (op (op (var 1) (op (var 0) (var 0))) (var 0)) (op (var 1) (var 0)))) → ⊥
  cut1237  = reject3 ((var 0) , (op (op (op (var 1) (op (var 0) (var 0))) (var 0)) (op (var 1) (var 0)))) (λ env → holds1237 (env 0) (env 1))
  env0 : ℕ → Two
  env0 zero = b0
  env0 (suc zero) = b1
  env0 (suc (suc rest)) = b0
  bad1238 : PathP (λ _ → Two) b0 (bop (bop (bop b1 (bop b0 b0)) b0) (bop b1 b1)) → ⊥
  bad1238  p = false≢true (cong lower p)
  cut1238 : Adequate {ℓ} ((var 0) , (op (op (op (var 1) (op (var 0) (var 0))) (var 0)) (op (var 1) (var 1)))) → ⊥
  cut1238  adequate = bad1238  (Adequate.valid adequate Two boolean env0)
  env1 : ℕ → Two
  env1 zero = b0
  env1 (suc zero) = b1
  env1 (suc (suc zero)) = b1
  env1 (suc (suc (suc rest))) = b0
  bad1239 : PathP (λ _ → Two) b0 (bop (bop (bop b1 (bop b0 b0)) b0) (bop b1 b1)) → ⊥
  bad1239  p = false≢true (cong lower p)
  cut1239 : Adequate {ℓ} ((var 0) , (op (op (op (var 1) (op (var 0) (var 0))) (var 0)) (op (var 1) (var 2)))) → ⊥
  cut1239  adequate = bad1239  (Adequate.valid adequate Two boolean env1)
  holds1240 : (z0 z1 z2 : A3) → z0 ≡ (mul3 (mul3 (mul3 z1 (mul3 z0 z0)) z0) (mul3 z2 z0))
  holds1240 z0 z1 z2 = refl
  cut1240 : Adequate {ℓ} ((var 0) , (op (op (op (var 1) (op (var 0) (var 0))) (var 0)) (op (var 2) (var 0)))) → ⊥
  cut1240  = reject3 ((var 0) , (op (op (op (var 1) (op (var 0) (var 0))) (var 0)) (op (var 2) (var 0)))) (λ env → holds1240 (env 0) (env 1) (env 2))
  bad1241 : PathP (λ _ → Two) b0 (bop (bop (bop b1 (bop b0 b0)) b0) (bop b1 b1)) → ⊥
  bad1241  p = false≢true (cong lower p)
  cut1241 : Adequate {ℓ} ((var 0) , (op (op (op (var 1) (op (var 0) (var 0))) (var 0)) (op (var 2) (var 1)))) → ⊥
  cut1241  adequate = bad1241  (Adequate.valid adequate Two boolean env1)
  env2 : ℕ → Two
  env2 zero = b0
  env2 (suc zero) = b0
  env2 (suc (suc zero)) = b1
  env2 (suc (suc (suc rest))) = b0
  bad1242 : PathP (λ _ → Two) b0 (bop (bop (bop b0 (bop b0 b0)) b0) (bop b1 b1)) → ⊥
  bad1242  p = false≢true (cong lower p)
  cut1242 : Adequate {ℓ} ((var 0) , (op (op (op (var 1) (op (var 0) (var 0))) (var 0)) (op (var 2) (var 2)))) → ⊥
  cut1242  adequate = bad1242  (Adequate.valid adequate Two boolean env2)
  env3 : ℕ → Two
  env3 zero = b0
  env3 (suc zero) = b0
  env3 (suc (suc zero)) = b1
  env3 (suc (suc (suc zero))) = b1
  env3 (suc (suc (suc (suc rest)))) = b0
  bad1243 : PathP (λ _ → Two) b0 (bop (bop (bop b0 (bop b0 b0)) b0) (bop b1 b1)) → ⊥
  bad1243  p = false≢true (cong lower p)
  cut1243 : Adequate {ℓ} ((var 0) , (op (op (op (var 1) (op (var 0) (var 0))) (var 0)) (op (var 2) (var 3)))) → ⊥
  cut1243  adequate = bad1243  (Adequate.valid adequate Two boolean env3)
  holds1244 : (z0 z1 : A3) → z0 ≡ (mul3 (mul3 (mul3 z1 (mul3 z0 z0)) z1) (mul3 z0 z0))
  holds1244 z0 z1 = refl
  cut1244 : Adequate {ℓ} ((var 0) , (op (op (op (var 1) (op (var 0) (var 0))) (var 1)) (op (var 0) (var 0)))) → ⊥
  cut1244  = reject3 ((var 0) , (op (op (op (var 1) (op (var 0) (var 0))) (var 1)) (op (var 0) (var 0)))) (λ env → holds1244 (env 0) (env 1))
  env4 : ℕ → Two
  env4 zero = b1
  env4 (suc zero) = b0
  env4 (suc (suc rest)) = b0
  bad1245 : PathP (λ _ → Two) b1 (bop (bop (bop b0 (bop b1 b1)) b0) (bop b1 b0)) → ⊥
  bad1245  p = false≢true (sym (cong lower p))
  cut1245 : Adequate {ℓ} ((var 0) , (op (op (op (var 1) (op (var 0) (var 0))) (var 1)) (op (var 0) (var 1)))) → ⊥
  cut1245  adequate = bad1245  (Adequate.valid adequate Two boolean env4)
  env5 : ℕ → Two
  env5 zero = b1
  env5 (suc zero) = b0
  env5 (suc (suc zero)) = b0
  env5 (suc (suc (suc rest))) = b0
  bad1246 : PathP (λ _ → Two) b1 (bop (bop (bop b0 (bop b1 b1)) b0) (bop b1 b0)) → ⊥
  bad1246  p = false≢true (sym (cong lower p))
  cut1246 : Adequate {ℓ} ((var 0) , (op (op (op (var 1) (op (var 0) (var 0))) (var 1)) (op (var 0) (var 2)))) → ⊥
  cut1246  adequate = bad1246  (Adequate.valid adequate Two boolean env5)
  bad1247 : (z2 : Two) → PathP (λ _ → Two) b1 (bop (bop (bop b0 (bop b1 b1)) b0) (bop b0 z2)) → ⊥
  bad1247 z2 p = false≢true (sym (cong lower p))
  cut1247 : (x6 : ℕ) → Adequate {ℓ} ((var 0) , (op (op (op (var 1) (op (var 0) (var 0))) (var 1)) (op (var 1) (var x6)))) → ⊥
  cut1247 x6 adequate = bad1247 (env4 x6) (Adequate.valid adequate Two boolean env4)
  bad1248 : (z3 : Two) → PathP (λ _ → Two) b1 (bop (bop (bop b0 (bop b1 b1)) b0) (bop b0 z3)) → ⊥
  bad1248 z3 p = false≢true (sym (cong lower p))
  cut1248 : (x6 : ℕ) → Adequate {ℓ} ((var 0) , (op (op (op (var 1) (op (var 0) (var 0))) (var 1)) (op (var 2) (var x6)))) → ⊥
  cut1248 x6 adequate = bad1248 (env5 x6) (Adequate.valid adequate Two boolean env5)
  bad1249 : (z3 z4 : Two) → PathP (λ _ → Two) b0 (bop (bop (bop b0 (bop b0 b0)) b1) (bop z3 z4)) → ⊥
  bad1249 z3 z4 p = false≢true (cong lower p)
  cut1249 : (x5 x6 : ℕ) → Adequate {ℓ} ((var 0) , (op (op (op (var 1) (op (var 0) (var 0))) (var 2)) (op (var x5) (var x6)))) → ⊥
  cut1249 x5 x6 adequate = bad1249 (env2 x5) (env2 x6) (Adequate.valid adequate Two boolean env2)
  holds1250 : (z0 z1 z2 : A11) → z0 ≡ (mul11 (mul11 (mul11 z1 (mul11 z0 z1)) z0) (mul11 z0 z2))
  holds1250 m11c0 m11c0 m11c0 = refl
  holds1250 m11c0 m11c0 m11c1 = refl
  holds1250 m11c0 m11c0 m11c2 = refl
  holds1250 m11c0 m11c1 m11c0 = refl
  holds1250 m11c0 m11c1 m11c1 = refl
  holds1250 m11c0 m11c1 m11c2 = refl
  holds1250 m11c0 m11c2 m11c0 = refl
  holds1250 m11c0 m11c2 m11c1 = refl
  holds1250 m11c0 m11c2 m11c2 = refl
  holds1250 m11c1 m11c0 z2 = refl
  holds1250 m11c1 m11c1 z2 = refl
  holds1250 m11c1 m11c2 z2 = refl
  holds1250 m11c2 m11c0 z2 = refl
  holds1250 m11c2 m11c1 z2 = refl
  holds1250 m11c2 m11c2 z2 = refl
  cut1250 : (x6 : ℕ) → Adequate {ℓ} ((var 0) , (op (op (op (var 1) (op (var 0) (var 1))) (var 0)) (op (var 0) (var x6)))) → ⊥
  cut1250 x6 = reject11 ((var 0) , (op (op (op (var 1) (op (var 0) (var 1))) (var 0)) (op (var 0) (var x6)))) (λ env → holds1250 (env 0) (env 1) (env x6))
  holds1251 : (z0 z1 : A3) → z0 ≡ (mul3 (mul3 (mul3 z1 (mul3 z0 z1)) z0) (mul3 z1 z0))
  holds1251 z0 z1 = refl
  cut1251 : Adequate {ℓ} ((var 0) , (op (op (op (var 1) (op (var 0) (var 1))) (var 0)) (op (var 1) (var 0)))) → ⊥
  cut1251  = reject3 ((var 0) , (op (op (op (var 1) (op (var 0) (var 1))) (var 0)) (op (var 1) (var 0)))) (λ env → holds1251 (env 0) (env 1))
  bad1252 : PathP (λ _ → Two) b0 (bop (bop (bop b1 (bop b0 b1)) b0) (bop b1 b1)) → ⊥
  bad1252  p = false≢true (cong lower p)
  cut1252 : Adequate {ℓ} ((var 0) , (op (op (op (var 1) (op (var 0) (var 1))) (var 0)) (op (var 1) (var 1)))) → ⊥
  cut1252  adequate = bad1252  (Adequate.valid adequate Two boolean env0)
  bad1253 : PathP (λ _ → Two) b0 (bop (bop (bop b1 (bop b0 b1)) b0) (bop b1 b1)) → ⊥
  bad1253  p = false≢true (cong lower p)
  cut1253 : Adequate {ℓ} ((var 0) , (op (op (op (var 1) (op (var 0) (var 1))) (var 0)) (op (var 1) (var 2)))) → ⊥
  cut1253  adequate = bad1253  (Adequate.valid adequate Two boolean env1)
  holds1254 : (z0 z1 z2 : A3) → z0 ≡ (mul3 (mul3 (mul3 z1 (mul3 z0 z1)) z0) (mul3 z2 z0))
  holds1254 z0 z1 z2 = refl
  cut1254 : Adequate {ℓ} ((var 0) , (op (op (op (var 1) (op (var 0) (var 1))) (var 0)) (op (var 2) (var 0)))) → ⊥
  cut1254  = reject3 ((var 0) , (op (op (op (var 1) (op (var 0) (var 1))) (var 0)) (op (var 2) (var 0)))) (λ env → holds1254 (env 0) (env 1) (env 2))
  bad1255 : PathP (λ _ → Two) b0 (bop (bop (bop b1 (bop b0 b1)) b0) (bop b1 b1)) → ⊥
  bad1255  p = false≢true (cong lower p)
  cut1255 : Adequate {ℓ} ((var 0) , (op (op (op (var 1) (op (var 0) (var 1))) (var 0)) (op (var 2) (var 1)))) → ⊥
  cut1255  adequate = bad1255  (Adequate.valid adequate Two boolean env1)
  bad1256 : PathP (λ _ → Two) b0 (bop (bop (bop b0 (bop b0 b0)) b0) (bop b1 b1)) → ⊥
  bad1256  p = false≢true (cong lower p)
  cut1256 : Adequate {ℓ} ((var 0) , (op (op (op (var 1) (op (var 0) (var 1))) (var 0)) (op (var 2) (var 2)))) → ⊥
  cut1256  adequate = bad1256  (Adequate.valid adequate Two boolean env2)
  bad1257 : PathP (λ _ → Two) b0 (bop (bop (bop b0 (bop b0 b0)) b0) (bop b1 b1)) → ⊥
  bad1257  p = false≢true (cong lower p)
  cut1257 : Adequate {ℓ} ((var 0) , (op (op (op (var 1) (op (var 0) (var 1))) (var 0)) (op (var 2) (var 3)))) → ⊥
  cut1257  adequate = bad1257  (Adequate.valid adequate Two boolean env3)
  holds1258 : (z0 z1 : A3) → z0 ≡ (mul3 (mul3 (mul3 z1 (mul3 z0 z1)) z1) (mul3 z0 z0))
  holds1258 z0 z1 = refl
  cut1258 : Adequate {ℓ} ((var 0) , (op (op (op (var 1) (op (var 0) (var 1))) (var 1)) (op (var 0) (var 0)))) → ⊥
  cut1258  = reject3 ((var 0) , (op (op (op (var 1) (op (var 0) (var 1))) (var 1)) (op (var 0) (var 0)))) (λ env → holds1258 (env 0) (env 1))
  bad1259 : PathP (λ _ → Two) b1 (bop (bop (bop b0 (bop b1 b0)) b0) (bop b1 b0)) → ⊥
  bad1259  p = false≢true (sym (cong lower p))
  cut1259 : Adequate {ℓ} ((var 0) , (op (op (op (var 1) (op (var 0) (var 1))) (var 1)) (op (var 0) (var 1)))) → ⊥
  cut1259  adequate = bad1259  (Adequate.valid adequate Two boolean env4)
  bad1260 : PathP (λ _ → Two) b1 (bop (bop (bop b0 (bop b1 b0)) b0) (bop b1 b0)) → ⊥
  bad1260  p = false≢true (sym (cong lower p))
  cut1260 : Adequate {ℓ} ((var 0) , (op (op (op (var 1) (op (var 0) (var 1))) (var 1)) (op (var 0) (var 2)))) → ⊥
  cut1260  adequate = bad1260  (Adequate.valid adequate Two boolean env5)
  bad1261 : (z2 : Two) → PathP (λ _ → Two) b1 (bop (bop (bop b0 (bop b1 b0)) b0) (bop b0 z2)) → ⊥
  bad1261 z2 p = false≢true (sym (cong lower p))
  cut1261 : (x6 : ℕ) → Adequate {ℓ} ((var 0) , (op (op (op (var 1) (op (var 0) (var 1))) (var 1)) (op (var 1) (var x6)))) → ⊥
  cut1261 x6 adequate = bad1261 (env4 x6) (Adequate.valid adequate Two boolean env4)
  bad1262 : (z3 : Two) → PathP (λ _ → Two) b1 (bop (bop (bop b0 (bop b1 b0)) b0) (bop b0 z3)) → ⊥
  bad1262 z3 p = false≢true (sym (cong lower p))
  cut1262 : (x6 : ℕ) → Adequate {ℓ} ((var 0) , (op (op (op (var 1) (op (var 0) (var 1))) (var 1)) (op (var 2) (var x6)))) → ⊥
  cut1262 x6 adequate = bad1262 (env5 x6) (Adequate.valid adequate Two boolean env5)
  bad1263 : (z3 z4 : Two) → PathP (λ _ → Two) b0 (bop (bop (bop b0 (bop b0 b0)) b1) (bop z3 z4)) → ⊥
  bad1263 z3 z4 p = false≢true (cong lower p)
  cut1263 : (x5 x6 : ℕ) → Adequate {ℓ} ((var 0) , (op (op (op (var 1) (op (var 0) (var 1))) (var 2)) (op (var x5) (var x6)))) → ⊥
  cut1263 x5 x6 adequate = bad1263 (env2 x5) (env2 x6) (Adequate.valid adequate Two boolean env2)
  holds1264 : (z0 z1 z2 z3 : A11) → z0 ≡ (mul11 (mul11 (mul11 z1 (mul11 z0 z2)) z0) (mul11 z0 z3))
  holds1264 m11c0 m11c0 m11c0 m11c0 = refl
  holds1264 m11c0 m11c0 m11c0 m11c1 = refl
  holds1264 m11c0 m11c0 m11c0 m11c2 = refl
  holds1264 m11c0 m11c0 m11c1 m11c0 = refl
  holds1264 m11c0 m11c0 m11c1 m11c1 = refl
  holds1264 m11c0 m11c0 m11c1 m11c2 = refl
  holds1264 m11c0 m11c0 m11c2 m11c0 = refl
  holds1264 m11c0 m11c0 m11c2 m11c1 = refl
  holds1264 m11c0 m11c0 m11c2 m11c2 = refl
  holds1264 m11c0 m11c1 z2 m11c0 = refl
  holds1264 m11c0 m11c1 z2 m11c1 = refl
  holds1264 m11c0 m11c1 z2 m11c2 = refl
  holds1264 m11c0 m11c2 m11c0 m11c0 = refl
  holds1264 m11c0 m11c2 m11c0 m11c1 = refl
  holds1264 m11c0 m11c2 m11c0 m11c2 = refl
  holds1264 m11c0 m11c2 m11c1 m11c0 = refl
  holds1264 m11c0 m11c2 m11c1 m11c1 = refl
  holds1264 m11c0 m11c2 m11c1 m11c2 = refl
  holds1264 m11c0 m11c2 m11c2 m11c0 = refl
  holds1264 m11c0 m11c2 m11c2 m11c1 = refl
  holds1264 m11c0 m11c2 m11c2 m11c2 = refl
  holds1264 m11c1 m11c0 z2 z3 = refl
  holds1264 m11c1 m11c1 z2 z3 = refl
  holds1264 m11c1 m11c2 z2 z3 = refl
  holds1264 m11c2 m11c0 m11c0 z3 = refl
  holds1264 m11c2 m11c0 m11c1 z3 = refl
  holds1264 m11c2 m11c0 m11c2 z3 = refl
  holds1264 m11c2 m11c1 z2 z3 = refl
  holds1264 m11c2 m11c2 m11c0 z3 = refl
  holds1264 m11c2 m11c2 m11c1 z3 = refl
  holds1264 m11c2 m11c2 m11c2 z3 = refl
  cut1264 : (x6 : ℕ) → Adequate {ℓ} ((var 0) , (op (op (op (var 1) (op (var 0) (var 2))) (var 0)) (op (var 0) (var x6)))) → ⊥
  cut1264 x6 = reject11 ((var 0) , (op (op (op (var 1) (op (var 0) (var 2))) (var 0)) (op (var 0) (var x6)))) (λ env → holds1264 (env 0) (env 1) (env 2) (env x6))
  holds1265 : (z0 z1 z2 : A3) → z0 ≡ (mul3 (mul3 (mul3 z1 (mul3 z0 z2)) z0) (mul3 z1 z0))
  holds1265 z0 z1 z2 = refl
  cut1265 : Adequate {ℓ} ((var 0) , (op (op (op (var 1) (op (var 0) (var 2))) (var 0)) (op (var 1) (var 0)))) → ⊥
  cut1265  = reject3 ((var 0) , (op (op (op (var 1) (op (var 0) (var 2))) (var 0)) (op (var 1) (var 0)))) (λ env → holds1265 (env 0) (env 1) (env 2))
  env6 : ℕ → Two
  env6 zero = b0
  env6 (suc zero) = b1
  env6 (suc (suc zero)) = b0
  env6 (suc (suc (suc rest))) = b0
  bad1266 : PathP (λ _ → Two) b0 (bop (bop (bop b1 (bop b0 b0)) b0) (bop b1 b1)) → ⊥
  bad1266  p = false≢true (cong lower p)
  cut1266 : Adequate {ℓ} ((var 0) , (op (op (op (var 1) (op (var 0) (var 2))) (var 0)) (op (var 1) (var 1)))) → ⊥
  cut1266  adequate = bad1266  (Adequate.valid adequate Two boolean env6)
  bad1267 : PathP (λ _ → Two) b0 (bop (bop (bop b1 (bop b0 b1)) b0) (bop b1 b1)) → ⊥
  bad1267  p = false≢true (cong lower p)
  cut1267 : Adequate {ℓ} ((var 0) , (op (op (op (var 1) (op (var 0) (var 2))) (var 0)) (op (var 1) (var 2)))) → ⊥
  cut1267  adequate = bad1267  (Adequate.valid adequate Two boolean env1)
  env7 : ℕ → Two
  env7 zero = b0
  env7 (suc zero) = b1
  env7 (suc (suc zero)) = b0
  env7 (suc (suc (suc zero))) = b1
  env7 (suc (suc (suc (suc rest)))) = b0
  bad1268 : PathP (λ _ → Two) b0 (bop (bop (bop b1 (bop b0 b0)) b0) (bop b1 b1)) → ⊥
  bad1268  p = false≢true (cong lower p)
  cut1268 : Adequate {ℓ} ((var 0) , (op (op (op (var 1) (op (var 0) (var 2))) (var 0)) (op (var 1) (var 3)))) → ⊥
  cut1268  adequate = bad1268  (Adequate.valid adequate Two boolean env7)
  env8 : ℕ → Two
  env8 zero = b1
  env8 (suc zero) = b1
  env8 (suc (suc zero)) = b0
  env8 (suc (suc (suc rest))) = b0
  bad1269 : (z3 : Two) → PathP (λ _ → Two) b1 (bop (bop (bop b1 (bop b1 b0)) b1) (bop b0 z3)) → ⊥
  bad1269 z3 p = false≢true (sym (cong lower p))
  cut1269 : (x6 : ℕ) → Adequate {ℓ} ((var 0) , (op (op (op (var 1) (op (var 0) (var 2))) (var 0)) (op (var 2) (var x6)))) → ⊥
  cut1269 x6 adequate = bad1269 (env8 x6) (Adequate.valid adequate Two boolean env8)
  env9 : ℕ → Two
  env9 zero = b1
  env9 (suc zero) = b1
  env9 (suc (suc zero)) = b0
  env9 (suc (suc (suc zero))) = b0
  env9 (suc (suc (suc (suc rest)))) = b0
  bad1270 : (z4 : Two) → PathP (λ _ → Two) b1 (bop (bop (bop b1 (bop b1 b0)) b1) (bop b0 z4)) → ⊥
  bad1270 z4 p = false≢true (sym (cong lower p))
  cut1270 : (x6 : ℕ) → Adequate {ℓ} ((var 0) , (op (op (op (var 1) (op (var 0) (var 2))) (var 0)) (op (var 3) (var x6)))) → ⊥
  cut1270 x6 adequate = bad1270 (env9 x6) (Adequate.valid adequate Two boolean env9)
  holds1271 : (z0 z1 z2 : A3) → z0 ≡ (mul3 (mul3 (mul3 z1 (mul3 z0 z2)) z1) (mul3 z0 z0))
  holds1271 z0 z1 z2 = refl
  cut1271 : Adequate {ℓ} ((var 0) , (op (op (op (var 1) (op (var 0) (var 2))) (var 1)) (op (var 0) (var 0)))) → ⊥
  cut1271  = reject3 ((var 0) , (op (op (op (var 1) (op (var 0) (var 2))) (var 1)) (op (var 0) (var 0)))) (λ env → holds1271 (env 0) (env 1) (env 2))
  bad1272 : PathP (λ _ → Two) b1 (bop (bop (bop b0 (bop b1 b0)) b0) (bop b1 b0)) → ⊥
  bad1272  p = false≢true (sym (cong lower p))
  cut1272 : Adequate {ℓ} ((var 0) , (op (op (op (var 1) (op (var 0) (var 2))) (var 1)) (op (var 0) (var 1)))) → ⊥
  cut1272  adequate = bad1272  (Adequate.valid adequate Two boolean env5)
  bad1273 : PathP (λ _ → Two) b1 (bop (bop (bop b0 (bop b1 b0)) b0) (bop b1 b0)) → ⊥
  bad1273  p = false≢true (sym (cong lower p))
  cut1273 : Adequate {ℓ} ((var 0) , (op (op (op (var 1) (op (var 0) (var 2))) (var 1)) (op (var 0) (var 2)))) → ⊥
  cut1273  adequate = bad1273  (Adequate.valid adequate Two boolean env5)
  env10 : ℕ → Two
  env10 zero = b1
  env10 (suc zero) = b0
  env10 (suc (suc zero)) = b0
  env10 (suc (suc (suc zero))) = b0
  env10 (suc (suc (suc (suc rest)))) = b0
  bad1274 : PathP (λ _ → Two) b1 (bop (bop (bop b0 (bop b1 b0)) b0) (bop b1 b0)) → ⊥
  bad1274  p = false≢true (sym (cong lower p))
  cut1274 : Adequate {ℓ} ((var 0) , (op (op (op (var 1) (op (var 0) (var 2))) (var 1)) (op (var 0) (var 3)))) → ⊥
  cut1274  adequate = bad1274  (Adequate.valid adequate Two boolean env10)
  bad1275 : (z3 : Two) → PathP (λ _ → Two) b1 (bop (bop (bop b0 (bop b1 b0)) b0) (bop b0 z3)) → ⊥
  bad1275 z3 p = false≢true (sym (cong lower p))
  cut1275 : (x6 : ℕ) → Adequate {ℓ} ((var 0) , (op (op (op (var 1) (op (var 0) (var 2))) (var 1)) (op (var 1) (var x6)))) → ⊥
  cut1275 x6 adequate = bad1275 (env5 x6) (Adequate.valid adequate Two boolean env5)
  bad1276 : (z3 : Two) → PathP (λ _ → Two) b1 (bop (bop (bop b0 (bop b1 b0)) b0) (bop b0 z3)) → ⊥
  bad1276 z3 p = false≢true (sym (cong lower p))
  cut1276 : (x6 : ℕ) → Adequate {ℓ} ((var 0) , (op (op (op (var 1) (op (var 0) (var 2))) (var 1)) (op (var 2) (var x6)))) → ⊥
  cut1276 x6 adequate = bad1276 (env5 x6) (Adequate.valid adequate Two boolean env5)
  bad1277 : (z4 : Two) → PathP (λ _ → Two) b1 (bop (bop (bop b0 (bop b1 b0)) b0) (bop b0 z4)) → ⊥
  bad1277 z4 p = false≢true (sym (cong lower p))
  cut1277 : (x6 : ℕ) → Adequate {ℓ} ((var 0) , (op (op (op (var 1) (op (var 0) (var 2))) (var 1)) (op (var 3) (var x6)))) → ⊥
  cut1277 x6 adequate = bad1277 (env10 x6) (Adequate.valid adequate Two boolean env10)
  bad1278 : (z3 z4 : Two) → PathP (λ _ → Two) b0 (bop (bop (bop b0 (bop b0 b1)) b1) (bop z3 z4)) → ⊥
  bad1278 z3 z4 p = false≢true (cong lower p)
  cut1278 : (x5 x6 : ℕ) → Adequate {ℓ} ((var 0) , (op (op (op (var 1) (op (var 0) (var 2))) (var 2)) (op (var x5) (var x6)))) → ⊥
  cut1278 x5 x6 adequate = bad1278 (env2 x5) (env2 x6) (Adequate.valid adequate Two boolean env2)
  env11 : ℕ → Two
  env11 zero = b0
  env11 (suc zero) = b0
  env11 (suc (suc zero)) = b0
  env11 (suc (suc (suc zero))) = b1
  env11 (suc (suc (suc (suc rest)))) = b0
  bad1279 : (z4 z5 : Two) → PathP (λ _ → Two) b0 (bop (bop (bop b0 (bop b0 b0)) b1) (bop z4 z5)) → ⊥
  bad1279 z4 z5 p = false≢true (cong lower p)
  cut1279 : (x5 x6 : ℕ) → Adequate {ℓ} ((var 0) , (op (op (op (var 1) (op (var 0) (var 2))) (var 3)) (op (var x5) (var x6)))) → ⊥
  cut1279 x5 x6 adequate = bad1279 (env11 x5) (env11 x6) (Adequate.valid adequate Two boolean env11)
  holds1280 : (z0 z1 z2 : A11) → z0 ≡ (mul11 (mul11 (mul11 z1 (mul11 z1 z0)) z0) (mul11 z0 z2))
  holds1280 m11c0 m11c0 m11c0 = refl
  holds1280 m11c0 m11c0 m11c1 = refl
  holds1280 m11c0 m11c0 m11c2 = refl
  holds1280 m11c0 m11c1 m11c0 = refl
  holds1280 m11c0 m11c1 m11c1 = refl
  holds1280 m11c0 m11c1 m11c2 = refl
  holds1280 m11c0 m11c2 m11c0 = refl
  holds1280 m11c0 m11c2 m11c1 = refl
  holds1280 m11c0 m11c2 m11c2 = refl
  holds1280 m11c1 m11c0 z2 = refl
  holds1280 m11c1 m11c1 z2 = refl
  holds1280 m11c1 m11c2 z2 = refl
  holds1280 m11c2 m11c0 z2 = refl
  holds1280 m11c2 m11c1 z2 = refl
  holds1280 m11c2 m11c2 z2 = refl
  cut1280 : (x6 : ℕ) → Adequate {ℓ} ((var 0) , (op (op (op (var 1) (op (var 1) (var 0))) (var 0)) (op (var 0) (var x6)))) → ⊥
  cut1280 x6 = reject11 ((var 0) , (op (op (op (var 1) (op (var 1) (var 0))) (var 0)) (op (var 0) (var x6)))) (λ env → holds1280 (env 0) (env 1) (env x6))
  holds1281 : (z0 z1 : A3) → z0 ≡ (mul3 (mul3 (mul3 z1 (mul3 z1 z0)) z0) (mul3 z1 z0))
  holds1281 z0 z1 = refl
  cut1281 : Adequate {ℓ} ((var 0) , (op (op (op (var 1) (op (var 1) (var 0))) (var 0)) (op (var 1) (var 0)))) → ⊥
  cut1281  = reject3 ((var 0) , (op (op (op (var 1) (op (var 1) (var 0))) (var 0)) (op (var 1) (var 0)))) (λ env → holds1281 (env 0) (env 1))
  bad1282 : PathP (λ _ → Two) b0 (bop (bop (bop b1 (bop b1 b0)) b0) (bop b1 b1)) → ⊥
  bad1282  p = false≢true (cong lower p)
  cut1282 : Adequate {ℓ} ((var 0) , (op (op (op (var 1) (op (var 1) (var 0))) (var 0)) (op (var 1) (var 1)))) → ⊥
  cut1282  adequate = bad1282  (Adequate.valid adequate Two boolean env0)
  bad1283 : PathP (λ _ → Two) b0 (bop (bop (bop b1 (bop b1 b0)) b0) (bop b1 b1)) → ⊥
  bad1283  p = false≢true (cong lower p)
  cut1283 : Adequate {ℓ} ((var 0) , (op (op (op (var 1) (op (var 1) (var 0))) (var 0)) (op (var 1) (var 2)))) → ⊥
  cut1283  adequate = bad1283  (Adequate.valid adequate Two boolean env1)
  holds1284 : (z0 z1 z2 : A3) → z0 ≡ (mul3 (mul3 (mul3 z1 (mul3 z1 z0)) z0) (mul3 z2 z0))
  holds1284 z0 z1 z2 = refl
  cut1284 : Adequate {ℓ} ((var 0) , (op (op (op (var 1) (op (var 1) (var 0))) (var 0)) (op (var 2) (var 0)))) → ⊥
  cut1284  = reject3 ((var 0) , (op (op (op (var 1) (op (var 1) (var 0))) (var 0)) (op (var 2) (var 0)))) (λ env → holds1284 (env 0) (env 1) (env 2))
  bad1285 : PathP (λ _ → Two) b0 (bop (bop (bop b1 (bop b1 b0)) b0) (bop b1 b1)) → ⊥
  bad1285  p = false≢true (cong lower p)
  cut1285 : Adequate {ℓ} ((var 0) , (op (op (op (var 1) (op (var 1) (var 0))) (var 0)) (op (var 2) (var 1)))) → ⊥
  cut1285  adequate = bad1285  (Adequate.valid adequate Two boolean env1)
  bad1286 : PathP (λ _ → Two) b0 (bop (bop (bop b0 (bop b0 b0)) b0) (bop b1 b1)) → ⊥
  bad1286  p = false≢true (cong lower p)
  cut1286 : Adequate {ℓ} ((var 0) , (op (op (op (var 1) (op (var 1) (var 0))) (var 0)) (op (var 2) (var 2)))) → ⊥
  cut1286  adequate = bad1286  (Adequate.valid adequate Two boolean env2)
  bad1287 : PathP (λ _ → Two) b0 (bop (bop (bop b0 (bop b0 b0)) b0) (bop b1 b1)) → ⊥
  bad1287  p = false≢true (cong lower p)
  cut1287 : Adequate {ℓ} ((var 0) , (op (op (op (var 1) (op (var 1) (var 0))) (var 0)) (op (var 2) (var 3)))) → ⊥
  cut1287  adequate = bad1287  (Adequate.valid adequate Two boolean env3)
  holds1288 : (z0 z1 : A3) → z0 ≡ (mul3 (mul3 (mul3 z1 (mul3 z1 z0)) z1) (mul3 z0 z0))
  holds1288 z0 z1 = refl
  cut1288 : Adequate {ℓ} ((var 0) , (op (op (op (var 1) (op (var 1) (var 0))) (var 1)) (op (var 0) (var 0)))) → ⊥
  cut1288  = reject3 ((var 0) , (op (op (op (var 1) (op (var 1) (var 0))) (var 1)) (op (var 0) (var 0)))) (λ env → holds1288 (env 0) (env 1))
  bad1289 : PathP (λ _ → Two) b1 (bop (bop (bop b0 (bop b0 b1)) b0) (bop b1 b0)) → ⊥
  bad1289  p = false≢true (sym (cong lower p))
  cut1289 : Adequate {ℓ} ((var 0) , (op (op (op (var 1) (op (var 1) (var 0))) (var 1)) (op (var 0) (var 1)))) → ⊥
  cut1289  adequate = bad1289  (Adequate.valid adequate Two boolean env4)
  bad1290 : PathP (λ _ → Two) b1 (bop (bop (bop b0 (bop b0 b1)) b0) (bop b1 b0)) → ⊥
  bad1290  p = false≢true (sym (cong lower p))
  cut1290 : Adequate {ℓ} ((var 0) , (op (op (op (var 1) (op (var 1) (var 0))) (var 1)) (op (var 0) (var 2)))) → ⊥
  cut1290  adequate = bad1290  (Adequate.valid adequate Two boolean env5)
  bad1291 : (z2 : Two) → PathP (λ _ → Two) b1 (bop (bop (bop b0 (bop b0 b1)) b0) (bop b0 z2)) → ⊥
  bad1291 z2 p = false≢true (sym (cong lower p))
  cut1291 : (x6 : ℕ) → Adequate {ℓ} ((var 0) , (op (op (op (var 1) (op (var 1) (var 0))) (var 1)) (op (var 1) (var x6)))) → ⊥
  cut1291 x6 adequate = bad1291 (env4 x6) (Adequate.valid adequate Two boolean env4)
  bad1292 : (z3 : Two) → PathP (λ _ → Two) b1 (bop (bop (bop b0 (bop b0 b1)) b0) (bop b0 z3)) → ⊥
  bad1292 z3 p = false≢true (sym (cong lower p))
  cut1292 : (x6 : ℕ) → Adequate {ℓ} ((var 0) , (op (op (op (var 1) (op (var 1) (var 0))) (var 1)) (op (var 2) (var x6)))) → ⊥
  cut1292 x6 adequate = bad1292 (env5 x6) (Adequate.valid adequate Two boolean env5)
  bad1293 : (z3 z4 : Two) → PathP (λ _ → Two) b0 (bop (bop (bop b0 (bop b0 b0)) b1) (bop z3 z4)) → ⊥
  bad1293 z3 z4 p = false≢true (cong lower p)
  cut1293 : (x5 x6 : ℕ) → Adequate {ℓ} ((var 0) , (op (op (op (var 1) (op (var 1) (var 0))) (var 2)) (op (var x5) (var x6)))) → ⊥
  cut1293 x5 x6 adequate = bad1293 (env2 x5) (env2 x6) (Adequate.valid adequate Two boolean env2)
  holds1294 : (z0 z1 z2 : A11) → z0 ≡ (mul11 (mul11 (mul11 z1 (mul11 z1 z1)) z0) (mul11 z0 z2))
  holds1294 m11c0 m11c0 m11c0 = refl
  holds1294 m11c0 m11c0 m11c1 = refl
  holds1294 m11c0 m11c0 m11c2 = refl
  holds1294 m11c0 m11c1 m11c0 = refl
  holds1294 m11c0 m11c1 m11c1 = refl
  holds1294 m11c0 m11c1 m11c2 = refl
  holds1294 m11c0 m11c2 m11c0 = refl
  holds1294 m11c0 m11c2 m11c1 = refl
  holds1294 m11c0 m11c2 m11c2 = refl
  holds1294 m11c1 m11c0 z2 = refl
  holds1294 m11c1 m11c1 z2 = refl
  holds1294 m11c1 m11c2 z2 = refl
  holds1294 m11c2 m11c0 z2 = refl
  holds1294 m11c2 m11c1 z2 = refl
  holds1294 m11c2 m11c2 z2 = refl
  cut1294 : (x6 : ℕ) → Adequate {ℓ} ((var 0) , (op (op (op (var 1) (op (var 1) (var 1))) (var 0)) (op (var 0) (var x6)))) → ⊥
  cut1294 x6 = reject11 ((var 0) , (op (op (op (var 1) (op (var 1) (var 1))) (var 0)) (op (var 0) (var x6)))) (λ env → holds1294 (env 0) (env 1) (env x6))
  holds1295 : (z0 z1 : A3) → z0 ≡ (mul3 (mul3 (mul3 z1 (mul3 z1 z1)) z0) (mul3 z1 z0))
  holds1295 z0 z1 = refl
  cut1295 : Adequate {ℓ} ((var 0) , (op (op (op (var 1) (op (var 1) (var 1))) (var 0)) (op (var 1) (var 0)))) → ⊥
  cut1295  = reject3 ((var 0) , (op (op (op (var 1) (op (var 1) (var 1))) (var 0)) (op (var 1) (var 0)))) (λ env → holds1295 (env 0) (env 1))
  bad1296 : PathP (λ _ → Two) b0 (bop (bop (bop b1 (bop b1 b1)) b0) (bop b1 b1)) → ⊥
  bad1296  p = false≢true (cong lower p)
  cut1296 : Adequate {ℓ} ((var 0) , (op (op (op (var 1) (op (var 1) (var 1))) (var 0)) (op (var 1) (var 1)))) → ⊥
  cut1296  adequate = bad1296  (Adequate.valid adequate Two boolean env0)
  bad1297 : PathP (λ _ → Two) b0 (bop (bop (bop b1 (bop b1 b1)) b0) (bop b1 b1)) → ⊥
  bad1297  p = false≢true (cong lower p)
  cut1297 : Adequate {ℓ} ((var 0) , (op (op (op (var 1) (op (var 1) (var 1))) (var 0)) (op (var 1) (var 2)))) → ⊥
  cut1297  adequate = bad1297  (Adequate.valid adequate Two boolean env1)
  holds1298 : (z0 z1 z2 : A3) → z0 ≡ (mul3 (mul3 (mul3 z1 (mul3 z1 z1)) z0) (mul3 z2 z0))
  holds1298 z0 z1 z2 = refl
  cut1298 : Adequate {ℓ} ((var 0) , (op (op (op (var 1) (op (var 1) (var 1))) (var 0)) (op (var 2) (var 0)))) → ⊥
  cut1298  = reject3 ((var 0) , (op (op (op (var 1) (op (var 1) (var 1))) (var 0)) (op (var 2) (var 0)))) (λ env → holds1298 (env 0) (env 1) (env 2))
  bad1299 : PathP (λ _ → Two) b0 (bop (bop (bop b1 (bop b1 b1)) b0) (bop b1 b1)) → ⊥
  bad1299  p = false≢true (cong lower p)
  cut1299 : Adequate {ℓ} ((var 0) , (op (op (op (var 1) (op (var 1) (var 1))) (var 0)) (op (var 2) (var 1)))) → ⊥
  cut1299  adequate = bad1299  (Adequate.valid adequate Two boolean env1)
  bad1300 : PathP (λ _ → Two) b0 (bop (bop (bop b0 (bop b0 b0)) b0) (bop b1 b1)) → ⊥
  bad1300  p = false≢true (cong lower p)
  cut1300 : Adequate {ℓ} ((var 0) , (op (op (op (var 1) (op (var 1) (var 1))) (var 0)) (op (var 2) (var 2)))) → ⊥
  cut1300  adequate = bad1300  (Adequate.valid adequate Two boolean env2)
  bad1301 : PathP (λ _ → Two) b0 (bop (bop (bop b0 (bop b0 b0)) b0) (bop b1 b1)) → ⊥
  bad1301  p = false≢true (cong lower p)
  cut1301 : Adequate {ℓ} ((var 0) , (op (op (op (var 1) (op (var 1) (var 1))) (var 0)) (op (var 2) (var 3)))) → ⊥
  cut1301  adequate = bad1301  (Adequate.valid adequate Two boolean env3)
  bad1302 : (z2 z3 : Two) → PathP (λ _ → Two) b0 (bop (bop (bop b1 (bop b1 b1)) b1) (bop z2 z3)) → ⊥
  bad1302 z2 z3 p = false≢true (cong lower p)
  cut1302 : (x5 x6 : ℕ) → Adequate {ℓ} ((var 0) , (op (op (op (var 1) (op (var 1) (var 1))) (var 1)) (op (var x5) (var x6)))) → ⊥
  cut1302 x5 x6 adequate = bad1302 (env0 x5) (env0 x6) (Adequate.valid adequate Two boolean env0)
  bad1303 : (z3 z4 : Two) → PathP (λ _ → Two) b0 (bop (bop (bop b0 (bop b0 b0)) b1) (bop z3 z4)) → ⊥
  bad1303 z3 z4 p = false≢true (cong lower p)
  cut1303 : (x5 x6 : ℕ) → Adequate {ℓ} ((var 0) , (op (op (op (var 1) (op (var 1) (var 1))) (var 2)) (op (var x5) (var x6)))) → ⊥
  cut1303 x5 x6 adequate = bad1303 (env2 x5) (env2 x6) (Adequate.valid adequate Two boolean env2)
  holds1304 : (z0 z1 z2 z3 : A11) → z0 ≡ (mul11 (mul11 (mul11 z1 (mul11 z1 z2)) z0) (mul11 z0 z3))
  holds1304 m11c0 m11c0 m11c0 m11c0 = refl
  holds1304 m11c0 m11c0 m11c0 m11c1 = refl
  holds1304 m11c0 m11c0 m11c0 m11c2 = refl
  holds1304 m11c0 m11c0 m11c1 m11c0 = refl
  holds1304 m11c0 m11c0 m11c1 m11c1 = refl
  holds1304 m11c0 m11c0 m11c1 m11c2 = refl
  holds1304 m11c0 m11c0 m11c2 m11c0 = refl
  holds1304 m11c0 m11c0 m11c2 m11c1 = refl
  holds1304 m11c0 m11c0 m11c2 m11c2 = refl
  holds1304 m11c0 m11c1 z2 m11c0 = refl
  holds1304 m11c0 m11c1 z2 m11c1 = refl
  holds1304 m11c0 m11c1 z2 m11c2 = refl
  holds1304 m11c0 m11c2 m11c0 m11c0 = refl
  holds1304 m11c0 m11c2 m11c0 m11c1 = refl
  holds1304 m11c0 m11c2 m11c0 m11c2 = refl
  holds1304 m11c0 m11c2 m11c1 m11c0 = refl
  holds1304 m11c0 m11c2 m11c1 m11c1 = refl
  holds1304 m11c0 m11c2 m11c1 m11c2 = refl
  holds1304 m11c0 m11c2 m11c2 m11c0 = refl
  holds1304 m11c0 m11c2 m11c2 m11c1 = refl
  holds1304 m11c0 m11c2 m11c2 m11c2 = refl
  holds1304 m11c1 m11c0 m11c0 z3 = refl
  holds1304 m11c1 m11c0 m11c1 z3 = refl
  holds1304 m11c1 m11c0 m11c2 z3 = refl
  holds1304 m11c1 m11c1 z2 z3 = refl
  holds1304 m11c1 m11c2 m11c0 z3 = refl
  holds1304 m11c1 m11c2 m11c1 z3 = refl
  holds1304 m11c1 m11c2 m11c2 z3 = refl
  holds1304 m11c2 m11c0 m11c0 z3 = refl
  holds1304 m11c2 m11c0 m11c1 z3 = refl
  holds1304 m11c2 m11c0 m11c2 z3 = refl
  holds1304 m11c2 m11c1 z2 z3 = refl
  holds1304 m11c2 m11c2 m11c0 z3 = refl
  holds1304 m11c2 m11c2 m11c1 z3 = refl
  holds1304 m11c2 m11c2 m11c2 z3 = refl
  cut1304 : (x6 : ℕ) → Adequate {ℓ} ((var 0) , (op (op (op (var 1) (op (var 1) (var 2))) (var 0)) (op (var 0) (var x6)))) → ⊥
  cut1304 x6 = reject11 ((var 0) , (op (op (op (var 1) (op (var 1) (var 2))) (var 0)) (op (var 0) (var x6)))) (λ env → holds1304 (env 0) (env 1) (env 2) (env x6))
  holds1305 : (z0 z1 z2 : A3) → z0 ≡ (mul3 (mul3 (mul3 z1 (mul3 z1 z2)) z0) (mul3 z1 z0))
  holds1305 z0 z1 z2 = refl
  cut1305 : Adequate {ℓ} ((var 0) , (op (op (op (var 1) (op (var 1) (var 2))) (var 0)) (op (var 1) (var 0)))) → ⊥
  cut1305  = reject3 ((var 0) , (op (op (op (var 1) (op (var 1) (var 2))) (var 0)) (op (var 1) (var 0)))) (λ env → holds1305 (env 0) (env 1) (env 2))
  bad1306 : PathP (λ _ → Two) b0 (bop (bop (bop b1 (bop b1 b0)) b0) (bop b1 b1)) → ⊥
  bad1306  p = false≢true (cong lower p)
  cut1306 : Adequate {ℓ} ((var 0) , (op (op (op (var 1) (op (var 1) (var 2))) (var 0)) (op (var 1) (var 1)))) → ⊥
  cut1306  adequate = bad1306  (Adequate.valid adequate Two boolean env6)
  bad1307 : PathP (λ _ → Two) b0 (bop (bop (bop b1 (bop b1 b1)) b0) (bop b1 b1)) → ⊥
  bad1307  p = false≢true (cong lower p)
  cut1307 : Adequate {ℓ} ((var 0) , (op (op (op (var 1) (op (var 1) (var 2))) (var 0)) (op (var 1) (var 2)))) → ⊥
  cut1307  adequate = bad1307  (Adequate.valid adequate Two boolean env1)
  bad1308 : PathP (λ _ → Two) b0 (bop (bop (bop b1 (bop b1 b0)) b0) (bop b1 b1)) → ⊥
  bad1308  p = false≢true (cong lower p)
  cut1308 : Adequate {ℓ} ((var 0) , (op (op (op (var 1) (op (var 1) (var 2))) (var 0)) (op (var 1) (var 3)))) → ⊥
  cut1308  adequate = bad1308  (Adequate.valid adequate Two boolean env7)
  bad1309 : (z3 : Two) → PathP (λ _ → Two) b1 (bop (bop (bop b1 (bop b1 b0)) b1) (bop b0 z3)) → ⊥
  bad1309 z3 p = false≢true (sym (cong lower p))
  cut1309 : (x6 : ℕ) → Adequate {ℓ} ((var 0) , (op (op (op (var 1) (op (var 1) (var 2))) (var 0)) (op (var 2) (var x6)))) → ⊥
  cut1309 x6 adequate = bad1309 (env8 x6) (Adequate.valid adequate Two boolean env8)
  bad1310 : (z4 : Two) → PathP (λ _ → Two) b1 (bop (bop (bop b1 (bop b1 b0)) b1) (bop b0 z4)) → ⊥
  bad1310 z4 p = false≢true (sym (cong lower p))
  cut1310 : (x6 : ℕ) → Adequate {ℓ} ((var 0) , (op (op (op (var 1) (op (var 1) (var 2))) (var 0)) (op (var 3) (var x6)))) → ⊥
  cut1310 x6 adequate = bad1310 (env9 x6) (Adequate.valid adequate Two boolean env9)
  bad1311 : (z3 z4 : Two) → PathP (λ _ → Two) b0 (bop (bop (bop b1 (bop b1 b1)) b1) (bop z3 z4)) → ⊥
  bad1311 z3 z4 p = false≢true (cong lower p)
  cut1311 : (x5 x6 : ℕ) → Adequate {ℓ} ((var 0) , (op (op (op (var 1) (op (var 1) (var 2))) (var 1)) (op (var x5) (var x6)))) → ⊥
  cut1311 x5 x6 adequate = bad1311 (env1 x5) (env1 x6) (Adequate.valid adequate Two boolean env1)
  bad1312 : (z3 z4 : Two) → PathP (λ _ → Two) b0 (bop (bop (bop b0 (bop b0 b1)) b1) (bop z3 z4)) → ⊥
  bad1312 z3 z4 p = false≢true (cong lower p)
  cut1312 : (x5 x6 : ℕ) → Adequate {ℓ} ((var 0) , (op (op (op (var 1) (op (var 1) (var 2))) (var 2)) (op (var x5) (var x6)))) → ⊥
  cut1312 x5 x6 adequate = bad1312 (env2 x5) (env2 x6) (Adequate.valid adequate Two boolean env2)
  bad1313 : (z4 z5 : Two) → PathP (λ _ → Two) b0 (bop (bop (bop b0 (bop b0 b0)) b1) (bop z4 z5)) → ⊥
  bad1313 z4 z5 p = false≢true (cong lower p)
  cut1313 : (x5 x6 : ℕ) → Adequate {ℓ} ((var 0) , (op (op (op (var 1) (op (var 1) (var 2))) (var 3)) (op (var x5) (var x6)))) → ⊥
  cut1313 x5 x6 adequate = bad1313 (env11 x5) (env11 x6) (Adequate.valid adequate Two boolean env11)
  holds1314 : (z0 z1 z2 z3 : A13) → z0 ≡ (mul13 (mul13 (mul13 z1 (mul13 z2 z0)) z0) (mul13 z0 z3))
  holds1314 m13c0 m13c0 m13c0 m13c0 = refl
  holds1314 m13c0 m13c0 m13c0 m13c1 = refl
  holds1314 m13c0 m13c0 m13c0 m13c2 = refl
  holds1314 m13c0 m13c0 m13c0 m13c3 = refl
  holds1314 m13c0 m13c0 m13c1 m13c0 = refl
  holds1314 m13c0 m13c0 m13c1 m13c1 = refl
  holds1314 m13c0 m13c0 m13c1 m13c2 = refl
  holds1314 m13c0 m13c0 m13c1 m13c3 = refl
  holds1314 m13c0 m13c0 m13c2 m13c0 = refl
  holds1314 m13c0 m13c0 m13c2 m13c1 = refl
  holds1314 m13c0 m13c0 m13c2 m13c2 = refl
  holds1314 m13c0 m13c0 m13c2 m13c3 = refl
  holds1314 m13c0 m13c0 m13c3 m13c0 = refl
  holds1314 m13c0 m13c0 m13c3 m13c1 = refl
  holds1314 m13c0 m13c0 m13c3 m13c2 = refl
  holds1314 m13c0 m13c0 m13c3 m13c3 = refl
  holds1314 m13c0 m13c1 m13c0 m13c0 = refl
  holds1314 m13c0 m13c1 m13c0 m13c1 = refl
  holds1314 m13c0 m13c1 m13c0 m13c2 = refl
  holds1314 m13c0 m13c1 m13c0 m13c3 = refl
  holds1314 m13c0 m13c1 m13c1 m13c0 = refl
  holds1314 m13c0 m13c1 m13c1 m13c1 = refl
  holds1314 m13c0 m13c1 m13c1 m13c2 = refl
  holds1314 m13c0 m13c1 m13c1 m13c3 = refl
  holds1314 m13c0 m13c1 m13c2 m13c0 = refl
  holds1314 m13c0 m13c1 m13c2 m13c1 = refl
  holds1314 m13c0 m13c1 m13c2 m13c2 = refl
  holds1314 m13c0 m13c1 m13c2 m13c3 = refl
  holds1314 m13c0 m13c1 m13c3 m13c0 = refl
  holds1314 m13c0 m13c1 m13c3 m13c1 = refl
  holds1314 m13c0 m13c1 m13c3 m13c2 = refl
  holds1314 m13c0 m13c1 m13c3 m13c3 = refl
  holds1314 m13c0 m13c2 m13c0 m13c0 = refl
  holds1314 m13c0 m13c2 m13c0 m13c1 = refl
  holds1314 m13c0 m13c2 m13c0 m13c2 = refl
  holds1314 m13c0 m13c2 m13c0 m13c3 = refl
  holds1314 m13c0 m13c2 m13c1 m13c0 = refl
  holds1314 m13c0 m13c2 m13c1 m13c1 = refl
  holds1314 m13c0 m13c2 m13c1 m13c2 = refl
  holds1314 m13c0 m13c2 m13c1 m13c3 = refl
  holds1314 m13c0 m13c2 m13c2 m13c0 = refl
  holds1314 m13c0 m13c2 m13c2 m13c1 = refl
  holds1314 m13c0 m13c2 m13c2 m13c2 = refl
  holds1314 m13c0 m13c2 m13c2 m13c3 = refl
  holds1314 m13c0 m13c2 m13c3 m13c0 = refl
  holds1314 m13c0 m13c2 m13c3 m13c1 = refl
  holds1314 m13c0 m13c2 m13c3 m13c2 = refl
  holds1314 m13c0 m13c2 m13c3 m13c3 = refl
  holds1314 m13c0 m13c3 m13c0 m13c0 = refl
  holds1314 m13c0 m13c3 m13c0 m13c1 = refl
  holds1314 m13c0 m13c3 m13c0 m13c2 = refl
  holds1314 m13c0 m13c3 m13c0 m13c3 = refl
  holds1314 m13c0 m13c3 m13c1 m13c0 = refl
  holds1314 m13c0 m13c3 m13c1 m13c1 = refl
  holds1314 m13c0 m13c3 m13c1 m13c2 = refl
  holds1314 m13c0 m13c3 m13c1 m13c3 = refl
  holds1314 m13c0 m13c3 m13c2 m13c0 = refl
  holds1314 m13c0 m13c3 m13c2 m13c1 = refl
  holds1314 m13c0 m13c3 m13c2 m13c2 = refl
  holds1314 m13c0 m13c3 m13c2 m13c3 = refl
  holds1314 m13c0 m13c3 m13c3 m13c0 = refl
  holds1314 m13c0 m13c3 m13c3 m13c1 = refl
  holds1314 m13c0 m13c3 m13c3 m13c2 = refl
  holds1314 m13c0 m13c3 m13c3 m13c3 = refl
  holds1314 m13c1 m13c0 m13c0 m13c0 = refl
  holds1314 m13c1 m13c0 m13c0 m13c1 = refl
  holds1314 m13c1 m13c0 m13c0 m13c2 = refl
  holds1314 m13c1 m13c0 m13c0 m13c3 = refl
  holds1314 m13c1 m13c0 m13c1 m13c0 = refl
  holds1314 m13c1 m13c0 m13c1 m13c1 = refl
  holds1314 m13c1 m13c0 m13c1 m13c2 = refl
  holds1314 m13c1 m13c0 m13c1 m13c3 = refl
  holds1314 m13c1 m13c0 m13c2 m13c0 = refl
  holds1314 m13c1 m13c0 m13c2 m13c1 = refl
  holds1314 m13c1 m13c0 m13c2 m13c2 = refl
  holds1314 m13c1 m13c0 m13c2 m13c3 = refl
  holds1314 m13c1 m13c0 m13c3 m13c0 = refl
  holds1314 m13c1 m13c0 m13c3 m13c1 = refl
  holds1314 m13c1 m13c0 m13c3 m13c2 = refl
  holds1314 m13c1 m13c0 m13c3 m13c3 = refl
  holds1314 m13c1 m13c1 m13c0 m13c0 = refl
  holds1314 m13c1 m13c1 m13c0 m13c1 = refl
  holds1314 m13c1 m13c1 m13c0 m13c2 = refl
  holds1314 m13c1 m13c1 m13c0 m13c3 = refl
  holds1314 m13c1 m13c1 m13c1 m13c0 = refl
  holds1314 m13c1 m13c1 m13c1 m13c1 = refl
  holds1314 m13c1 m13c1 m13c1 m13c2 = refl
  holds1314 m13c1 m13c1 m13c1 m13c3 = refl
  holds1314 m13c1 m13c1 m13c2 m13c0 = refl
  holds1314 m13c1 m13c1 m13c2 m13c1 = refl
  holds1314 m13c1 m13c1 m13c2 m13c2 = refl
  holds1314 m13c1 m13c1 m13c2 m13c3 = refl
  holds1314 m13c1 m13c1 m13c3 m13c0 = refl
  holds1314 m13c1 m13c1 m13c3 m13c1 = refl
  holds1314 m13c1 m13c1 m13c3 m13c2 = refl
  holds1314 m13c1 m13c1 m13c3 m13c3 = refl
  holds1314 m13c1 m13c2 m13c0 m13c0 = refl
  holds1314 m13c1 m13c2 m13c0 m13c1 = refl
  holds1314 m13c1 m13c2 m13c0 m13c2 = refl
  holds1314 m13c1 m13c2 m13c0 m13c3 = refl
  holds1314 m13c1 m13c2 m13c1 m13c0 = refl
  holds1314 m13c1 m13c2 m13c1 m13c1 = refl
  holds1314 m13c1 m13c2 m13c1 m13c2 = refl
  holds1314 m13c1 m13c2 m13c1 m13c3 = refl
  holds1314 m13c1 m13c2 m13c2 m13c0 = refl
  holds1314 m13c1 m13c2 m13c2 m13c1 = refl
  holds1314 m13c1 m13c2 m13c2 m13c2 = refl
  holds1314 m13c1 m13c2 m13c2 m13c3 = refl
  holds1314 m13c1 m13c2 m13c3 m13c0 = refl
  holds1314 m13c1 m13c2 m13c3 m13c1 = refl
  holds1314 m13c1 m13c2 m13c3 m13c2 = refl
  holds1314 m13c1 m13c2 m13c3 m13c3 = refl
  holds1314 m13c1 m13c3 m13c0 m13c0 = refl
  holds1314 m13c1 m13c3 m13c0 m13c1 = refl
  holds1314 m13c1 m13c3 m13c0 m13c2 = refl
  holds1314 m13c1 m13c3 m13c0 m13c3 = refl
  holds1314 m13c1 m13c3 m13c1 m13c0 = refl
  holds1314 m13c1 m13c3 m13c1 m13c1 = refl
  holds1314 m13c1 m13c3 m13c1 m13c2 = refl
  holds1314 m13c1 m13c3 m13c1 m13c3 = refl
  holds1314 m13c1 m13c3 m13c2 m13c0 = refl
  holds1314 m13c1 m13c3 m13c2 m13c1 = refl
  holds1314 m13c1 m13c3 m13c2 m13c2 = refl
  holds1314 m13c1 m13c3 m13c2 m13c3 = refl
  holds1314 m13c1 m13c3 m13c3 m13c0 = refl
  holds1314 m13c1 m13c3 m13c3 m13c1 = refl
  holds1314 m13c1 m13c3 m13c3 m13c2 = refl
  holds1314 m13c1 m13c3 m13c3 m13c3 = refl
  holds1314 m13c2 m13c0 m13c0 m13c0 = refl
  holds1314 m13c2 m13c0 m13c0 m13c1 = refl
  holds1314 m13c2 m13c0 m13c0 m13c2 = refl
  holds1314 m13c2 m13c0 m13c0 m13c3 = refl
  holds1314 m13c2 m13c0 m13c1 m13c0 = refl
  holds1314 m13c2 m13c0 m13c1 m13c1 = refl
  holds1314 m13c2 m13c0 m13c1 m13c2 = refl
  holds1314 m13c2 m13c0 m13c1 m13c3 = refl
  holds1314 m13c2 m13c0 m13c2 m13c0 = refl
  holds1314 m13c2 m13c0 m13c2 m13c1 = refl
  holds1314 m13c2 m13c0 m13c2 m13c2 = refl
  holds1314 m13c2 m13c0 m13c2 m13c3 = refl
  holds1314 m13c2 m13c0 m13c3 m13c0 = refl
  holds1314 m13c2 m13c0 m13c3 m13c1 = refl
  holds1314 m13c2 m13c0 m13c3 m13c2 = refl
  holds1314 m13c2 m13c0 m13c3 m13c3 = refl
  holds1314 m13c2 m13c1 m13c0 m13c0 = refl
  holds1314 m13c2 m13c1 m13c0 m13c1 = refl
  holds1314 m13c2 m13c1 m13c0 m13c2 = refl
  holds1314 m13c2 m13c1 m13c0 m13c3 = refl
  holds1314 m13c2 m13c1 m13c1 m13c0 = refl
  holds1314 m13c2 m13c1 m13c1 m13c1 = refl
  holds1314 m13c2 m13c1 m13c1 m13c2 = refl
  holds1314 m13c2 m13c1 m13c1 m13c3 = refl
  holds1314 m13c2 m13c1 m13c2 m13c0 = refl
  holds1314 m13c2 m13c1 m13c2 m13c1 = refl
  holds1314 m13c2 m13c1 m13c2 m13c2 = refl
  holds1314 m13c2 m13c1 m13c2 m13c3 = refl
  holds1314 m13c2 m13c1 m13c3 m13c0 = refl
  holds1314 m13c2 m13c1 m13c3 m13c1 = refl
  holds1314 m13c2 m13c1 m13c3 m13c2 = refl
  holds1314 m13c2 m13c1 m13c3 m13c3 = refl
  holds1314 m13c2 m13c2 m13c0 m13c0 = refl
  holds1314 m13c2 m13c2 m13c0 m13c1 = refl
  holds1314 m13c2 m13c2 m13c0 m13c2 = refl
  holds1314 m13c2 m13c2 m13c0 m13c3 = refl
  holds1314 m13c2 m13c2 m13c1 m13c0 = refl
  holds1314 m13c2 m13c2 m13c1 m13c1 = refl
  holds1314 m13c2 m13c2 m13c1 m13c2 = refl
  holds1314 m13c2 m13c2 m13c1 m13c3 = refl
  holds1314 m13c2 m13c2 m13c2 m13c0 = refl
  holds1314 m13c2 m13c2 m13c2 m13c1 = refl
  holds1314 m13c2 m13c2 m13c2 m13c2 = refl
  holds1314 m13c2 m13c2 m13c2 m13c3 = refl
  holds1314 m13c2 m13c2 m13c3 m13c0 = refl
  holds1314 m13c2 m13c2 m13c3 m13c1 = refl
  holds1314 m13c2 m13c2 m13c3 m13c2 = refl
  holds1314 m13c2 m13c2 m13c3 m13c3 = refl
  holds1314 m13c2 m13c3 m13c0 m13c0 = refl
  holds1314 m13c2 m13c3 m13c0 m13c1 = refl
  holds1314 m13c2 m13c3 m13c0 m13c2 = refl
  holds1314 m13c2 m13c3 m13c0 m13c3 = refl
  holds1314 m13c2 m13c3 m13c1 m13c0 = refl
  holds1314 m13c2 m13c3 m13c1 m13c1 = refl
  holds1314 m13c2 m13c3 m13c1 m13c2 = refl
  holds1314 m13c2 m13c3 m13c1 m13c3 = refl
  holds1314 m13c2 m13c3 m13c2 m13c0 = refl
  holds1314 m13c2 m13c3 m13c2 m13c1 = refl
  holds1314 m13c2 m13c3 m13c2 m13c2 = refl
  holds1314 m13c2 m13c3 m13c2 m13c3 = refl
  holds1314 m13c2 m13c3 m13c3 m13c0 = refl
  holds1314 m13c2 m13c3 m13c3 m13c1 = refl
  holds1314 m13c2 m13c3 m13c3 m13c2 = refl
  holds1314 m13c2 m13c3 m13c3 m13c3 = refl
  holds1314 m13c3 m13c0 m13c0 m13c0 = refl
  holds1314 m13c3 m13c0 m13c0 m13c1 = refl
  holds1314 m13c3 m13c0 m13c0 m13c2 = refl
  holds1314 m13c3 m13c0 m13c0 m13c3 = refl
  holds1314 m13c3 m13c0 m13c1 m13c0 = refl
  holds1314 m13c3 m13c0 m13c1 m13c1 = refl
  holds1314 m13c3 m13c0 m13c1 m13c2 = refl
  holds1314 m13c3 m13c0 m13c1 m13c3 = refl
  holds1314 m13c3 m13c0 m13c2 m13c0 = refl
  holds1314 m13c3 m13c0 m13c2 m13c1 = refl
  holds1314 m13c3 m13c0 m13c2 m13c2 = refl
  holds1314 m13c3 m13c0 m13c2 m13c3 = refl
  holds1314 m13c3 m13c0 m13c3 m13c0 = refl
  holds1314 m13c3 m13c0 m13c3 m13c1 = refl
  holds1314 m13c3 m13c0 m13c3 m13c2 = refl
  holds1314 m13c3 m13c0 m13c3 m13c3 = refl
  holds1314 m13c3 m13c1 m13c0 m13c0 = refl
  holds1314 m13c3 m13c1 m13c0 m13c1 = refl
  holds1314 m13c3 m13c1 m13c0 m13c2 = refl
  holds1314 m13c3 m13c1 m13c0 m13c3 = refl
  holds1314 m13c3 m13c1 m13c1 m13c0 = refl
  holds1314 m13c3 m13c1 m13c1 m13c1 = refl
  holds1314 m13c3 m13c1 m13c1 m13c2 = refl
  holds1314 m13c3 m13c1 m13c1 m13c3 = refl
  holds1314 m13c3 m13c1 m13c2 m13c0 = refl
  holds1314 m13c3 m13c1 m13c2 m13c1 = refl
  holds1314 m13c3 m13c1 m13c2 m13c2 = refl
  holds1314 m13c3 m13c1 m13c2 m13c3 = refl
  holds1314 m13c3 m13c1 m13c3 m13c0 = refl
  holds1314 m13c3 m13c1 m13c3 m13c1 = refl
  holds1314 m13c3 m13c1 m13c3 m13c2 = refl
  holds1314 m13c3 m13c1 m13c3 m13c3 = refl
  holds1314 m13c3 m13c2 m13c0 m13c0 = refl
  holds1314 m13c3 m13c2 m13c0 m13c1 = refl
  holds1314 m13c3 m13c2 m13c0 m13c2 = refl
  holds1314 m13c3 m13c2 m13c0 m13c3 = refl
  holds1314 m13c3 m13c2 m13c1 m13c0 = refl
  holds1314 m13c3 m13c2 m13c1 m13c1 = refl
  holds1314 m13c3 m13c2 m13c1 m13c2 = refl
  holds1314 m13c3 m13c2 m13c1 m13c3 = refl
  holds1314 m13c3 m13c2 m13c2 m13c0 = refl
  holds1314 m13c3 m13c2 m13c2 m13c1 = refl
  holds1314 m13c3 m13c2 m13c2 m13c2 = refl
  holds1314 m13c3 m13c2 m13c2 m13c3 = refl
  holds1314 m13c3 m13c2 m13c3 m13c0 = refl
  holds1314 m13c3 m13c2 m13c3 m13c1 = refl
  holds1314 m13c3 m13c2 m13c3 m13c2 = refl
  holds1314 m13c3 m13c2 m13c3 m13c3 = refl
  holds1314 m13c3 m13c3 m13c0 m13c0 = refl
  holds1314 m13c3 m13c3 m13c0 m13c1 = refl
  holds1314 m13c3 m13c3 m13c0 m13c2 = refl
  holds1314 m13c3 m13c3 m13c0 m13c3 = refl
  holds1314 m13c3 m13c3 m13c1 m13c0 = refl
  holds1314 m13c3 m13c3 m13c1 m13c1 = refl
  holds1314 m13c3 m13c3 m13c1 m13c2 = refl
  holds1314 m13c3 m13c3 m13c1 m13c3 = refl
  holds1314 m13c3 m13c3 m13c2 m13c0 = refl
  holds1314 m13c3 m13c3 m13c2 m13c1 = refl
  holds1314 m13c3 m13c3 m13c2 m13c2 = refl
  holds1314 m13c3 m13c3 m13c2 m13c3 = refl
  holds1314 m13c3 m13c3 m13c3 m13c0 = refl
  holds1314 m13c3 m13c3 m13c3 m13c1 = refl
  holds1314 m13c3 m13c3 m13c3 m13c2 = refl
  holds1314 m13c3 m13c3 m13c3 m13c3 = refl
  cut1314 : (x6 : ℕ) → Adequate {ℓ} ((var 0) , (op (op (op (var 1) (op (var 2) (var 0))) (var 0)) (op (var 0) (var x6)))) → ⊥
  cut1314 x6 = reject13 ((var 0) , (op (op (op (var 1) (op (var 2) (var 0))) (var 0)) (op (var 0) (var x6)))) (λ env → holds1314 (env 0) (env 1) (env 2) (env x6))
  holds1315 : (z0 z1 z2 : A3) → z0 ≡ (mul3 (mul3 (mul3 z1 (mul3 z2 z0)) z0) (mul3 z1 z0))
  holds1315 z0 z1 z2 = refl
  cut1315 : Adequate {ℓ} ((var 0) , (op (op (op (var 1) (op (var 2) (var 0))) (var 0)) (op (var 1) (var 0)))) → ⊥
  cut1315  = reject3 ((var 0) , (op (op (op (var 1) (op (var 2) (var 0))) (var 0)) (op (var 1) (var 0)))) (λ env → holds1315 (env 0) (env 1) (env 2))
  bad1316 : PathP (λ _ → Two) b0 (bop (bop (bop b1 (bop b0 b0)) b0) (bop b1 b1)) → ⊥
  bad1316  p = false≢true (cong lower p)
  cut1316 : Adequate {ℓ} ((var 0) , (op (op (op (var 1) (op (var 2) (var 0))) (var 0)) (op (var 1) (var 1)))) → ⊥
  cut1316  adequate = bad1316  (Adequate.valid adequate Two boolean env6)
  bad1317 : PathP (λ _ → Two) b0 (bop (bop (bop b1 (bop b1 b0)) b0) (bop b1 b1)) → ⊥
  bad1317  p = false≢true (cong lower p)
  cut1317 : Adequate {ℓ} ((var 0) , (op (op (op (var 1) (op (var 2) (var 0))) (var 0)) (op (var 1) (var 2)))) → ⊥
  cut1317  adequate = bad1317  (Adequate.valid adequate Two boolean env1)
  bad1318 : PathP (λ _ → Two) b0 (bop (bop (bop b1 (bop b0 b0)) b0) (bop b1 b1)) → ⊥
  bad1318  p = false≢true (cong lower p)
  cut1318 : Adequate {ℓ} ((var 0) , (op (op (op (var 1) (op (var 2) (var 0))) (var 0)) (op (var 1) (var 3)))) → ⊥
  cut1318  adequate = bad1318  (Adequate.valid adequate Two boolean env7)
  bad1319 : (z3 : Two) → PathP (λ _ → Two) b1 (bop (bop (bop b1 (bop b0 b1)) b1) (bop b0 z3)) → ⊥
  bad1319 z3 p = false≢true (sym (cong lower p))
  cut1319 : (x6 : ℕ) → Adequate {ℓ} ((var 0) , (op (op (op (var 1) (op (var 2) (var 0))) (var 0)) (op (var 2) (var x6)))) → ⊥
  cut1319 x6 adequate = bad1319 (env8 x6) (Adequate.valid adequate Two boolean env8)
  bad1320 : (z4 : Two) → PathP (λ _ → Two) b1 (bop (bop (bop b1 (bop b0 b1)) b1) (bop b0 z4)) → ⊥
  bad1320 z4 p = false≢true (sym (cong lower p))
  cut1320 : (x6 : ℕ) → Adequate {ℓ} ((var 0) , (op (op (op (var 1) (op (var 2) (var 0))) (var 0)) (op (var 3) (var x6)))) → ⊥
  cut1320 x6 adequate = bad1320 (env9 x6) (Adequate.valid adequate Two boolean env9)
  holds1321 : (z0 z1 z2 : A3) → z0 ≡ (mul3 (mul3 (mul3 z1 (mul3 z2 z0)) z1) (mul3 z0 z0))
  holds1321 z0 z1 z2 = refl
  cut1321 : Adequate {ℓ} ((var 0) , (op (op (op (var 1) (op (var 2) (var 0))) (var 1)) (op (var 0) (var 0)))) → ⊥
  cut1321  = reject3 ((var 0) , (op (op (op (var 1) (op (var 2) (var 0))) (var 1)) (op (var 0) (var 0)))) (λ env → holds1321 (env 0) (env 1) (env 2))
  bad1322 : PathP (λ _ → Two) b1 (bop (bop (bop b0 (bop b0 b1)) b0) (bop b1 b0)) → ⊥
  bad1322  p = false≢true (sym (cong lower p))
  cut1322 : Adequate {ℓ} ((var 0) , (op (op (op (var 1) (op (var 2) (var 0))) (var 1)) (op (var 0) (var 1)))) → ⊥
  cut1322  adequate = bad1322  (Adequate.valid adequate Two boolean env5)
  bad1323 : PathP (λ _ → Two) b1 (bop (bop (bop b0 (bop b0 b1)) b0) (bop b1 b0)) → ⊥
  bad1323  p = false≢true (sym (cong lower p))
  cut1323 : Adequate {ℓ} ((var 0) , (op (op (op (var 1) (op (var 2) (var 0))) (var 1)) (op (var 0) (var 2)))) → ⊥
  cut1323  adequate = bad1323  (Adequate.valid adequate Two boolean env5)
  bad1324 : PathP (λ _ → Two) b1 (bop (bop (bop b0 (bop b0 b1)) b0) (bop b1 b0)) → ⊥
  bad1324  p = false≢true (sym (cong lower p))
  cut1324 : Adequate {ℓ} ((var 0) , (op (op (op (var 1) (op (var 2) (var 0))) (var 1)) (op (var 0) (var 3)))) → ⊥
  cut1324  adequate = bad1324  (Adequate.valid adequate Two boolean env10)
  bad1325 : (z3 : Two) → PathP (λ _ → Two) b1 (bop (bop (bop b0 (bop b0 b1)) b0) (bop b0 z3)) → ⊥
  bad1325 z3 p = false≢true (sym (cong lower p))
  cut1325 : (x6 : ℕ) → Adequate {ℓ} ((var 0) , (op (op (op (var 1) (op (var 2) (var 0))) (var 1)) (op (var 1) (var x6)))) → ⊥
  cut1325 x6 adequate = bad1325 (env5 x6) (Adequate.valid adequate Two boolean env5)
  bad1326 : (z3 : Two) → PathP (λ _ → Two) b1 (bop (bop (bop b0 (bop b0 b1)) b0) (bop b0 z3)) → ⊥
  bad1326 z3 p = false≢true (sym (cong lower p))
  cut1326 : (x6 : ℕ) → Adequate {ℓ} ((var 0) , (op (op (op (var 1) (op (var 2) (var 0))) (var 1)) (op (var 2) (var x6)))) → ⊥
  cut1326 x6 adequate = bad1326 (env5 x6) (Adequate.valid adequate Two boolean env5)
  bad1327 : (z4 : Two) → PathP (λ _ → Two) b1 (bop (bop (bop b0 (bop b0 b1)) b0) (bop b0 z4)) → ⊥
  bad1327 z4 p = false≢true (sym (cong lower p))
  cut1327 : (x6 : ℕ) → Adequate {ℓ} ((var 0) , (op (op (op (var 1) (op (var 2) (var 0))) (var 1)) (op (var 3) (var x6)))) → ⊥
  cut1327 x6 adequate = bad1327 (env10 x6) (Adequate.valid adequate Two boolean env10)
  bad1328 : (z3 z4 : Two) → PathP (λ _ → Two) b0 (bop (bop (bop b0 (bop b1 b0)) b1) (bop z3 z4)) → ⊥
  bad1328 z3 z4 p = false≢true (cong lower p)
  cut1328 : (x5 x6 : ℕ) → Adequate {ℓ} ((var 0) , (op (op (op (var 1) (op (var 2) (var 0))) (var 2)) (op (var x5) (var x6)))) → ⊥
  cut1328 x5 x6 adequate = bad1328 (env2 x5) (env2 x6) (Adequate.valid adequate Two boolean env2)
  bad1329 : (z4 z5 : Two) → PathP (λ _ → Two) b0 (bop (bop (bop b0 (bop b0 b0)) b1) (bop z4 z5)) → ⊥
  bad1329 z4 z5 p = false≢true (cong lower p)
  cut1329 : (x5 x6 : ℕ) → Adequate {ℓ} ((var 0) , (op (op (op (var 1) (op (var 2) (var 0))) (var 3)) (op (var x5) (var x6)))) → ⊥
  cut1329 x5 x6 adequate = bad1329 (env11 x5) (env11 x6) (Adequate.valid adequate Two boolean env11)
  holds1330 : (z0 z1 z2 z3 : A13) → z0 ≡ (mul13 (mul13 (mul13 z1 (mul13 z2 z1)) z0) (mul13 z0 z3))
  holds1330 m13c0 m13c0 m13c0 m13c0 = refl
  holds1330 m13c0 m13c0 m13c0 m13c1 = refl
  holds1330 m13c0 m13c0 m13c0 m13c2 = refl
  holds1330 m13c0 m13c0 m13c0 m13c3 = refl
  holds1330 m13c0 m13c0 m13c1 m13c0 = refl
  holds1330 m13c0 m13c0 m13c1 m13c1 = refl
  holds1330 m13c0 m13c0 m13c1 m13c2 = refl
  holds1330 m13c0 m13c0 m13c1 m13c3 = refl
  holds1330 m13c0 m13c0 m13c2 m13c0 = refl
  holds1330 m13c0 m13c0 m13c2 m13c1 = refl
  holds1330 m13c0 m13c0 m13c2 m13c2 = refl
  holds1330 m13c0 m13c0 m13c2 m13c3 = refl
  holds1330 m13c0 m13c0 m13c3 m13c0 = refl
  holds1330 m13c0 m13c0 m13c3 m13c1 = refl
  holds1330 m13c0 m13c0 m13c3 m13c2 = refl
  holds1330 m13c0 m13c0 m13c3 m13c3 = refl
  holds1330 m13c0 m13c1 m13c0 m13c0 = refl
  holds1330 m13c0 m13c1 m13c0 m13c1 = refl
  holds1330 m13c0 m13c1 m13c0 m13c2 = refl
  holds1330 m13c0 m13c1 m13c0 m13c3 = refl
  holds1330 m13c0 m13c1 m13c1 m13c0 = refl
  holds1330 m13c0 m13c1 m13c1 m13c1 = refl
  holds1330 m13c0 m13c1 m13c1 m13c2 = refl
  holds1330 m13c0 m13c1 m13c1 m13c3 = refl
  holds1330 m13c0 m13c1 m13c2 m13c0 = refl
  holds1330 m13c0 m13c1 m13c2 m13c1 = refl
  holds1330 m13c0 m13c1 m13c2 m13c2 = refl
  holds1330 m13c0 m13c1 m13c2 m13c3 = refl
  holds1330 m13c0 m13c1 m13c3 m13c0 = refl
  holds1330 m13c0 m13c1 m13c3 m13c1 = refl
  holds1330 m13c0 m13c1 m13c3 m13c2 = refl
  holds1330 m13c0 m13c1 m13c3 m13c3 = refl
  holds1330 m13c0 m13c2 m13c0 m13c0 = refl
  holds1330 m13c0 m13c2 m13c0 m13c1 = refl
  holds1330 m13c0 m13c2 m13c0 m13c2 = refl
  holds1330 m13c0 m13c2 m13c0 m13c3 = refl
  holds1330 m13c0 m13c2 m13c1 m13c0 = refl
  holds1330 m13c0 m13c2 m13c1 m13c1 = refl
  holds1330 m13c0 m13c2 m13c1 m13c2 = refl
  holds1330 m13c0 m13c2 m13c1 m13c3 = refl
  holds1330 m13c0 m13c2 m13c2 m13c0 = refl
  holds1330 m13c0 m13c2 m13c2 m13c1 = refl
  holds1330 m13c0 m13c2 m13c2 m13c2 = refl
  holds1330 m13c0 m13c2 m13c2 m13c3 = refl
  holds1330 m13c0 m13c2 m13c3 m13c0 = refl
  holds1330 m13c0 m13c2 m13c3 m13c1 = refl
  holds1330 m13c0 m13c2 m13c3 m13c2 = refl
  holds1330 m13c0 m13c2 m13c3 m13c3 = refl
  holds1330 m13c0 m13c3 m13c0 m13c0 = refl
  holds1330 m13c0 m13c3 m13c0 m13c1 = refl
  holds1330 m13c0 m13c3 m13c0 m13c2 = refl
  holds1330 m13c0 m13c3 m13c0 m13c3 = refl
  holds1330 m13c0 m13c3 m13c1 m13c0 = refl
  holds1330 m13c0 m13c3 m13c1 m13c1 = refl
  holds1330 m13c0 m13c3 m13c1 m13c2 = refl
  holds1330 m13c0 m13c3 m13c1 m13c3 = refl
  holds1330 m13c0 m13c3 m13c2 m13c0 = refl
  holds1330 m13c0 m13c3 m13c2 m13c1 = refl
  holds1330 m13c0 m13c3 m13c2 m13c2 = refl
  holds1330 m13c0 m13c3 m13c2 m13c3 = refl
  holds1330 m13c0 m13c3 m13c3 m13c0 = refl
  holds1330 m13c0 m13c3 m13c3 m13c1 = refl
  holds1330 m13c0 m13c3 m13c3 m13c2 = refl
  holds1330 m13c0 m13c3 m13c3 m13c3 = refl
  holds1330 m13c1 m13c0 m13c0 m13c0 = refl
  holds1330 m13c1 m13c0 m13c0 m13c1 = refl
  holds1330 m13c1 m13c0 m13c0 m13c2 = refl
  holds1330 m13c1 m13c0 m13c0 m13c3 = refl
  holds1330 m13c1 m13c0 m13c1 m13c0 = refl
  holds1330 m13c1 m13c0 m13c1 m13c1 = refl
  holds1330 m13c1 m13c0 m13c1 m13c2 = refl
  holds1330 m13c1 m13c0 m13c1 m13c3 = refl
  holds1330 m13c1 m13c0 m13c2 m13c0 = refl
  holds1330 m13c1 m13c0 m13c2 m13c1 = refl
  holds1330 m13c1 m13c0 m13c2 m13c2 = refl
  holds1330 m13c1 m13c0 m13c2 m13c3 = refl
  holds1330 m13c1 m13c0 m13c3 m13c0 = refl
  holds1330 m13c1 m13c0 m13c3 m13c1 = refl
  holds1330 m13c1 m13c0 m13c3 m13c2 = refl
  holds1330 m13c1 m13c0 m13c3 m13c3 = refl
  holds1330 m13c1 m13c1 m13c0 m13c0 = refl
  holds1330 m13c1 m13c1 m13c0 m13c1 = refl
  holds1330 m13c1 m13c1 m13c0 m13c2 = refl
  holds1330 m13c1 m13c1 m13c0 m13c3 = refl
  holds1330 m13c1 m13c1 m13c1 m13c0 = refl
  holds1330 m13c1 m13c1 m13c1 m13c1 = refl
  holds1330 m13c1 m13c1 m13c1 m13c2 = refl
  holds1330 m13c1 m13c1 m13c1 m13c3 = refl
  holds1330 m13c1 m13c1 m13c2 m13c0 = refl
  holds1330 m13c1 m13c1 m13c2 m13c1 = refl
  holds1330 m13c1 m13c1 m13c2 m13c2 = refl
  holds1330 m13c1 m13c1 m13c2 m13c3 = refl
  holds1330 m13c1 m13c1 m13c3 m13c0 = refl
  holds1330 m13c1 m13c1 m13c3 m13c1 = refl
  holds1330 m13c1 m13c1 m13c3 m13c2 = refl
  holds1330 m13c1 m13c1 m13c3 m13c3 = refl
  holds1330 m13c1 m13c2 m13c0 m13c0 = refl
  holds1330 m13c1 m13c2 m13c0 m13c1 = refl
  holds1330 m13c1 m13c2 m13c0 m13c2 = refl
  holds1330 m13c1 m13c2 m13c0 m13c3 = refl
  holds1330 m13c1 m13c2 m13c1 m13c0 = refl
  holds1330 m13c1 m13c2 m13c1 m13c1 = refl
  holds1330 m13c1 m13c2 m13c1 m13c2 = refl
  holds1330 m13c1 m13c2 m13c1 m13c3 = refl
  holds1330 m13c1 m13c2 m13c2 m13c0 = refl
  holds1330 m13c1 m13c2 m13c2 m13c1 = refl
  holds1330 m13c1 m13c2 m13c2 m13c2 = refl
  holds1330 m13c1 m13c2 m13c2 m13c3 = refl
  holds1330 m13c1 m13c2 m13c3 m13c0 = refl
  holds1330 m13c1 m13c2 m13c3 m13c1 = refl
  holds1330 m13c1 m13c2 m13c3 m13c2 = refl
  holds1330 m13c1 m13c2 m13c3 m13c3 = refl
  holds1330 m13c1 m13c3 m13c0 m13c0 = refl
  holds1330 m13c1 m13c3 m13c0 m13c1 = refl
  holds1330 m13c1 m13c3 m13c0 m13c2 = refl
  holds1330 m13c1 m13c3 m13c0 m13c3 = refl
  holds1330 m13c1 m13c3 m13c1 m13c0 = refl
  holds1330 m13c1 m13c3 m13c1 m13c1 = refl
  holds1330 m13c1 m13c3 m13c1 m13c2 = refl
  holds1330 m13c1 m13c3 m13c1 m13c3 = refl
  holds1330 m13c1 m13c3 m13c2 m13c0 = refl
  holds1330 m13c1 m13c3 m13c2 m13c1 = refl
  holds1330 m13c1 m13c3 m13c2 m13c2 = refl
  holds1330 m13c1 m13c3 m13c2 m13c3 = refl
  holds1330 m13c1 m13c3 m13c3 m13c0 = refl
  holds1330 m13c1 m13c3 m13c3 m13c1 = refl
  holds1330 m13c1 m13c3 m13c3 m13c2 = refl
  holds1330 m13c1 m13c3 m13c3 m13c3 = refl
  holds1330 m13c2 m13c0 m13c0 m13c0 = refl
  holds1330 m13c2 m13c0 m13c0 m13c1 = refl
  holds1330 m13c2 m13c0 m13c0 m13c2 = refl
  holds1330 m13c2 m13c0 m13c0 m13c3 = refl
  holds1330 m13c2 m13c0 m13c1 m13c0 = refl
  holds1330 m13c2 m13c0 m13c1 m13c1 = refl
  holds1330 m13c2 m13c0 m13c1 m13c2 = refl
  holds1330 m13c2 m13c0 m13c1 m13c3 = refl
  holds1330 m13c2 m13c0 m13c2 m13c0 = refl
  holds1330 m13c2 m13c0 m13c2 m13c1 = refl
  holds1330 m13c2 m13c0 m13c2 m13c2 = refl
  holds1330 m13c2 m13c0 m13c2 m13c3 = refl
  holds1330 m13c2 m13c0 m13c3 m13c0 = refl
  holds1330 m13c2 m13c0 m13c3 m13c1 = refl
  holds1330 m13c2 m13c0 m13c3 m13c2 = refl
  holds1330 m13c2 m13c0 m13c3 m13c3 = refl
  holds1330 m13c2 m13c1 m13c0 m13c0 = refl
  holds1330 m13c2 m13c1 m13c0 m13c1 = refl
  holds1330 m13c2 m13c1 m13c0 m13c2 = refl
  holds1330 m13c2 m13c1 m13c0 m13c3 = refl
  holds1330 m13c2 m13c1 m13c1 m13c0 = refl
  holds1330 m13c2 m13c1 m13c1 m13c1 = refl
  holds1330 m13c2 m13c1 m13c1 m13c2 = refl
  holds1330 m13c2 m13c1 m13c1 m13c3 = refl
  holds1330 m13c2 m13c1 m13c2 m13c0 = refl
  holds1330 m13c2 m13c1 m13c2 m13c1 = refl
  holds1330 m13c2 m13c1 m13c2 m13c2 = refl
  holds1330 m13c2 m13c1 m13c2 m13c3 = refl
  holds1330 m13c2 m13c1 m13c3 m13c0 = refl
  holds1330 m13c2 m13c1 m13c3 m13c1 = refl
  holds1330 m13c2 m13c1 m13c3 m13c2 = refl
  holds1330 m13c2 m13c1 m13c3 m13c3 = refl
  holds1330 m13c2 m13c2 m13c0 m13c0 = refl
  holds1330 m13c2 m13c2 m13c0 m13c1 = refl
  holds1330 m13c2 m13c2 m13c0 m13c2 = refl
  holds1330 m13c2 m13c2 m13c0 m13c3 = refl
  holds1330 m13c2 m13c2 m13c1 m13c0 = refl
  holds1330 m13c2 m13c2 m13c1 m13c1 = refl
  holds1330 m13c2 m13c2 m13c1 m13c2 = refl
  holds1330 m13c2 m13c2 m13c1 m13c3 = refl
  holds1330 m13c2 m13c2 m13c2 m13c0 = refl
  holds1330 m13c2 m13c2 m13c2 m13c1 = refl
  holds1330 m13c2 m13c2 m13c2 m13c2 = refl
  holds1330 m13c2 m13c2 m13c2 m13c3 = refl
  holds1330 m13c2 m13c2 m13c3 m13c0 = refl
  holds1330 m13c2 m13c2 m13c3 m13c1 = refl
  holds1330 m13c2 m13c2 m13c3 m13c2 = refl
  holds1330 m13c2 m13c2 m13c3 m13c3 = refl
  holds1330 m13c2 m13c3 m13c0 m13c0 = refl
  holds1330 m13c2 m13c3 m13c0 m13c1 = refl
  holds1330 m13c2 m13c3 m13c0 m13c2 = refl
  holds1330 m13c2 m13c3 m13c0 m13c3 = refl
  holds1330 m13c2 m13c3 m13c1 m13c0 = refl
  holds1330 m13c2 m13c3 m13c1 m13c1 = refl
  holds1330 m13c2 m13c3 m13c1 m13c2 = refl
  holds1330 m13c2 m13c3 m13c1 m13c3 = refl
  holds1330 m13c2 m13c3 m13c2 m13c0 = refl
  holds1330 m13c2 m13c3 m13c2 m13c1 = refl
  holds1330 m13c2 m13c3 m13c2 m13c2 = refl
  holds1330 m13c2 m13c3 m13c2 m13c3 = refl
  holds1330 m13c2 m13c3 m13c3 m13c0 = refl
  holds1330 m13c2 m13c3 m13c3 m13c1 = refl
  holds1330 m13c2 m13c3 m13c3 m13c2 = refl
  holds1330 m13c2 m13c3 m13c3 m13c3 = refl
  holds1330 m13c3 m13c0 m13c0 m13c0 = refl
  holds1330 m13c3 m13c0 m13c0 m13c1 = refl
  holds1330 m13c3 m13c0 m13c0 m13c2 = refl
  holds1330 m13c3 m13c0 m13c0 m13c3 = refl
  holds1330 m13c3 m13c0 m13c1 m13c0 = refl
  holds1330 m13c3 m13c0 m13c1 m13c1 = refl
  holds1330 m13c3 m13c0 m13c1 m13c2 = refl
  holds1330 m13c3 m13c0 m13c1 m13c3 = refl
  holds1330 m13c3 m13c0 m13c2 m13c0 = refl
  holds1330 m13c3 m13c0 m13c2 m13c1 = refl
  holds1330 m13c3 m13c0 m13c2 m13c2 = refl
  holds1330 m13c3 m13c0 m13c2 m13c3 = refl
  holds1330 m13c3 m13c0 m13c3 m13c0 = refl
  holds1330 m13c3 m13c0 m13c3 m13c1 = refl
  holds1330 m13c3 m13c0 m13c3 m13c2 = refl
  holds1330 m13c3 m13c0 m13c3 m13c3 = refl
  holds1330 m13c3 m13c1 m13c0 m13c0 = refl
  holds1330 m13c3 m13c1 m13c0 m13c1 = refl
  holds1330 m13c3 m13c1 m13c0 m13c2 = refl
  holds1330 m13c3 m13c1 m13c0 m13c3 = refl
  holds1330 m13c3 m13c1 m13c1 m13c0 = refl
  holds1330 m13c3 m13c1 m13c1 m13c1 = refl
  holds1330 m13c3 m13c1 m13c1 m13c2 = refl
  holds1330 m13c3 m13c1 m13c1 m13c3 = refl
  holds1330 m13c3 m13c1 m13c2 m13c0 = refl
  holds1330 m13c3 m13c1 m13c2 m13c1 = refl
  holds1330 m13c3 m13c1 m13c2 m13c2 = refl
  holds1330 m13c3 m13c1 m13c2 m13c3 = refl
  holds1330 m13c3 m13c1 m13c3 m13c0 = refl
  holds1330 m13c3 m13c1 m13c3 m13c1 = refl
  holds1330 m13c3 m13c1 m13c3 m13c2 = refl
  holds1330 m13c3 m13c1 m13c3 m13c3 = refl
  holds1330 m13c3 m13c2 m13c0 m13c0 = refl
  holds1330 m13c3 m13c2 m13c0 m13c1 = refl
  holds1330 m13c3 m13c2 m13c0 m13c2 = refl
  holds1330 m13c3 m13c2 m13c0 m13c3 = refl
  holds1330 m13c3 m13c2 m13c1 m13c0 = refl
  holds1330 m13c3 m13c2 m13c1 m13c1 = refl
  holds1330 m13c3 m13c2 m13c1 m13c2 = refl
  holds1330 m13c3 m13c2 m13c1 m13c3 = refl
  holds1330 m13c3 m13c2 m13c2 m13c0 = refl
  holds1330 m13c3 m13c2 m13c2 m13c1 = refl
  holds1330 m13c3 m13c2 m13c2 m13c2 = refl
  holds1330 m13c3 m13c2 m13c2 m13c3 = refl
  holds1330 m13c3 m13c2 m13c3 m13c0 = refl
  holds1330 m13c3 m13c2 m13c3 m13c1 = refl
  holds1330 m13c3 m13c2 m13c3 m13c2 = refl
  holds1330 m13c3 m13c2 m13c3 m13c3 = refl
  holds1330 m13c3 m13c3 m13c0 m13c0 = refl
  holds1330 m13c3 m13c3 m13c0 m13c1 = refl
  holds1330 m13c3 m13c3 m13c0 m13c2 = refl
  holds1330 m13c3 m13c3 m13c0 m13c3 = refl
  holds1330 m13c3 m13c3 m13c1 m13c0 = refl
  holds1330 m13c3 m13c3 m13c1 m13c1 = refl
  holds1330 m13c3 m13c3 m13c1 m13c2 = refl
  holds1330 m13c3 m13c3 m13c1 m13c3 = refl
  holds1330 m13c3 m13c3 m13c2 m13c0 = refl
  holds1330 m13c3 m13c3 m13c2 m13c1 = refl
  holds1330 m13c3 m13c3 m13c2 m13c2 = refl
  holds1330 m13c3 m13c3 m13c2 m13c3 = refl
  holds1330 m13c3 m13c3 m13c3 m13c0 = refl
  holds1330 m13c3 m13c3 m13c3 m13c1 = refl
  holds1330 m13c3 m13c3 m13c3 m13c2 = refl
  holds1330 m13c3 m13c3 m13c3 m13c3 = refl
  cut1330 : (x6 : ℕ) → Adequate {ℓ} ((var 0) , (op (op (op (var 1) (op (var 2) (var 1))) (var 0)) (op (var 0) (var x6)))) → ⊥
  cut1330 x6 = reject13 ((var 0) , (op (op (op (var 1) (op (var 2) (var 1))) (var 0)) (op (var 0) (var x6)))) (λ env → holds1330 (env 0) (env 1) (env 2) (env x6))
  holds1331 : (z0 z1 z2 : A3) → z0 ≡ (mul3 (mul3 (mul3 z1 (mul3 z2 z1)) z0) (mul3 z1 z0))
  holds1331 z0 z1 z2 = refl
  cut1331 : Adequate {ℓ} ((var 0) , (op (op (op (var 1) (op (var 2) (var 1))) (var 0)) (op (var 1) (var 0)))) → ⊥
  cut1331  = reject3 ((var 0) , (op (op (op (var 1) (op (var 2) (var 1))) (var 0)) (op (var 1) (var 0)))) (λ env → holds1331 (env 0) (env 1) (env 2))
  bad1332 : PathP (λ _ → Two) b0 (bop (bop (bop b1 (bop b0 b1)) b0) (bop b1 b1)) → ⊥
  bad1332  p = false≢true (cong lower p)
  cut1332 : Adequate {ℓ} ((var 0) , (op (op (op (var 1) (op (var 2) (var 1))) (var 0)) (op (var 1) (var 1)))) → ⊥
  cut1332  adequate = bad1332  (Adequate.valid adequate Two boolean env6)
  bad1333 : PathP (λ _ → Two) b0 (bop (bop (bop b1 (bop b1 b1)) b0) (bop b1 b1)) → ⊥
  bad1333  p = false≢true (cong lower p)
  cut1333 : Adequate {ℓ} ((var 0) , (op (op (op (var 1) (op (var 2) (var 1))) (var 0)) (op (var 1) (var 2)))) → ⊥
  cut1333  adequate = bad1333  (Adequate.valid adequate Two boolean env1)
  bad1334 : PathP (λ _ → Two) b0 (bop (bop (bop b1 (bop b0 b1)) b0) (bop b1 b1)) → ⊥
  bad1334  p = false≢true (cong lower p)
  cut1334 : Adequate {ℓ} ((var 0) , (op (op (op (var 1) (op (var 2) (var 1))) (var 0)) (op (var 1) (var 3)))) → ⊥
  cut1334  adequate = bad1334  (Adequate.valid adequate Two boolean env7)
  bad1335 : (z3 : Two) → PathP (λ _ → Two) b1 (bop (bop (bop b1 (bop b0 b1)) b1) (bop b0 z3)) → ⊥
  bad1335 z3 p = false≢true (sym (cong lower p))
  cut1335 : (x6 : ℕ) → Adequate {ℓ} ((var 0) , (op (op (op (var 1) (op (var 2) (var 1))) (var 0)) (op (var 2) (var x6)))) → ⊥
  cut1335 x6 adequate = bad1335 (env8 x6) (Adequate.valid adequate Two boolean env8)
  bad1336 : (z4 : Two) → PathP (λ _ → Two) b1 (bop (bop (bop b1 (bop b0 b1)) b1) (bop b0 z4)) → ⊥
  bad1336 z4 p = false≢true (sym (cong lower p))
  cut1336 : (x6 : ℕ) → Adequate {ℓ} ((var 0) , (op (op (op (var 1) (op (var 2) (var 1))) (var 0)) (op (var 3) (var x6)))) → ⊥
  cut1336 x6 adequate = bad1336 (env9 x6) (Adequate.valid adequate Two boolean env9)
  bad1337 : (z3 z4 : Two) → PathP (λ _ → Two) b0 (bop (bop (bop b1 (bop b1 b1)) b1) (bop z3 z4)) → ⊥
  bad1337 z3 z4 p = false≢true (cong lower p)
  cut1337 : (x5 x6 : ℕ) → Adequate {ℓ} ((var 0) , (op (op (op (var 1) (op (var 2) (var 1))) (var 1)) (op (var x5) (var x6)))) → ⊥
  cut1337 x5 x6 adequate = bad1337 (env1 x5) (env1 x6) (Adequate.valid adequate Two boolean env1)
  bad1338 : (z3 z4 : Two) → PathP (λ _ → Two) b0 (bop (bop (bop b0 (bop b1 b0)) b1) (bop z3 z4)) → ⊥
  bad1338 z3 z4 p = false≢true (cong lower p)
  cut1338 : (x5 x6 : ℕ) → Adequate {ℓ} ((var 0) , (op (op (op (var 1) (op (var 2) (var 1))) (var 2)) (op (var x5) (var x6)))) → ⊥
  cut1338 x5 x6 adequate = bad1338 (env2 x5) (env2 x6) (Adequate.valid adequate Two boolean env2)
  bad1339 : (z4 z5 : Two) → PathP (λ _ → Two) b0 (bop (bop (bop b0 (bop b0 b0)) b1) (bop z4 z5)) → ⊥
  bad1339 z4 z5 p = false≢true (cong lower p)
  cut1339 : (x5 x6 : ℕ) → Adequate {ℓ} ((var 0) , (op (op (op (var 1) (op (var 2) (var 1))) (var 3)) (op (var x5) (var x6)))) → ⊥
  cut1339 x5 x6 adequate = bad1339 (env11 x5) (env11 x6) (Adequate.valid adequate Two boolean env11)
  holds1340 : (z0 z1 z2 z3 : A13) → z0 ≡ (mul13 (mul13 (mul13 z1 (mul13 z2 z2)) z0) (mul13 z0 z3))
  holds1340 m13c0 m13c0 m13c0 m13c0 = refl
  holds1340 m13c0 m13c0 m13c0 m13c1 = refl
  holds1340 m13c0 m13c0 m13c0 m13c2 = refl
  holds1340 m13c0 m13c0 m13c0 m13c3 = refl
  holds1340 m13c0 m13c0 m13c1 m13c0 = refl
  holds1340 m13c0 m13c0 m13c1 m13c1 = refl
  holds1340 m13c0 m13c0 m13c1 m13c2 = refl
  holds1340 m13c0 m13c0 m13c1 m13c3 = refl
  holds1340 m13c0 m13c0 m13c2 m13c0 = refl
  holds1340 m13c0 m13c0 m13c2 m13c1 = refl
  holds1340 m13c0 m13c0 m13c2 m13c2 = refl
  holds1340 m13c0 m13c0 m13c2 m13c3 = refl
  holds1340 m13c0 m13c0 m13c3 m13c0 = refl
  holds1340 m13c0 m13c0 m13c3 m13c1 = refl
  holds1340 m13c0 m13c0 m13c3 m13c2 = refl
  holds1340 m13c0 m13c0 m13c3 m13c3 = refl
  holds1340 m13c0 m13c1 m13c0 m13c0 = refl
  holds1340 m13c0 m13c1 m13c0 m13c1 = refl
  holds1340 m13c0 m13c1 m13c0 m13c2 = refl
  holds1340 m13c0 m13c1 m13c0 m13c3 = refl
  holds1340 m13c0 m13c1 m13c1 m13c0 = refl
  holds1340 m13c0 m13c1 m13c1 m13c1 = refl
  holds1340 m13c0 m13c1 m13c1 m13c2 = refl
  holds1340 m13c0 m13c1 m13c1 m13c3 = refl
  holds1340 m13c0 m13c1 m13c2 m13c0 = refl
  holds1340 m13c0 m13c1 m13c2 m13c1 = refl
  holds1340 m13c0 m13c1 m13c2 m13c2 = refl
  holds1340 m13c0 m13c1 m13c2 m13c3 = refl
  holds1340 m13c0 m13c1 m13c3 m13c0 = refl
  holds1340 m13c0 m13c1 m13c3 m13c1 = refl
  holds1340 m13c0 m13c1 m13c3 m13c2 = refl
  holds1340 m13c0 m13c1 m13c3 m13c3 = refl
  holds1340 m13c0 m13c2 m13c0 m13c0 = refl
  holds1340 m13c0 m13c2 m13c0 m13c1 = refl
  holds1340 m13c0 m13c2 m13c0 m13c2 = refl
  holds1340 m13c0 m13c2 m13c0 m13c3 = refl
  holds1340 m13c0 m13c2 m13c1 m13c0 = refl
  holds1340 m13c0 m13c2 m13c1 m13c1 = refl
  holds1340 m13c0 m13c2 m13c1 m13c2 = refl
  holds1340 m13c0 m13c2 m13c1 m13c3 = refl
  holds1340 m13c0 m13c2 m13c2 m13c0 = refl
  holds1340 m13c0 m13c2 m13c2 m13c1 = refl
  holds1340 m13c0 m13c2 m13c2 m13c2 = refl
  holds1340 m13c0 m13c2 m13c2 m13c3 = refl
  holds1340 m13c0 m13c2 m13c3 m13c0 = refl
  holds1340 m13c0 m13c2 m13c3 m13c1 = refl
  holds1340 m13c0 m13c2 m13c3 m13c2 = refl
  holds1340 m13c0 m13c2 m13c3 m13c3 = refl
  holds1340 m13c0 m13c3 m13c0 m13c0 = refl
  holds1340 m13c0 m13c3 m13c0 m13c1 = refl
  holds1340 m13c0 m13c3 m13c0 m13c2 = refl
  holds1340 m13c0 m13c3 m13c0 m13c3 = refl
  holds1340 m13c0 m13c3 m13c1 m13c0 = refl
  holds1340 m13c0 m13c3 m13c1 m13c1 = refl
  holds1340 m13c0 m13c3 m13c1 m13c2 = refl
  holds1340 m13c0 m13c3 m13c1 m13c3 = refl
  holds1340 m13c0 m13c3 m13c2 m13c0 = refl
  holds1340 m13c0 m13c3 m13c2 m13c1 = refl
  holds1340 m13c0 m13c3 m13c2 m13c2 = refl
  holds1340 m13c0 m13c3 m13c2 m13c3 = refl
  holds1340 m13c0 m13c3 m13c3 m13c0 = refl
  holds1340 m13c0 m13c3 m13c3 m13c1 = refl
  holds1340 m13c0 m13c3 m13c3 m13c2 = refl
  holds1340 m13c0 m13c3 m13c3 m13c3 = refl
  holds1340 m13c1 m13c0 m13c0 m13c0 = refl
  holds1340 m13c1 m13c0 m13c0 m13c1 = refl
  holds1340 m13c1 m13c0 m13c0 m13c2 = refl
  holds1340 m13c1 m13c0 m13c0 m13c3 = refl
  holds1340 m13c1 m13c0 m13c1 m13c0 = refl
  holds1340 m13c1 m13c0 m13c1 m13c1 = refl
  holds1340 m13c1 m13c0 m13c1 m13c2 = refl
  holds1340 m13c1 m13c0 m13c1 m13c3 = refl
  holds1340 m13c1 m13c0 m13c2 m13c0 = refl
  holds1340 m13c1 m13c0 m13c2 m13c1 = refl
  holds1340 m13c1 m13c0 m13c2 m13c2 = refl
  holds1340 m13c1 m13c0 m13c2 m13c3 = refl
  holds1340 m13c1 m13c0 m13c3 m13c0 = refl
  holds1340 m13c1 m13c0 m13c3 m13c1 = refl
  holds1340 m13c1 m13c0 m13c3 m13c2 = refl
  holds1340 m13c1 m13c0 m13c3 m13c3 = refl
  holds1340 m13c1 m13c1 m13c0 m13c0 = refl
  holds1340 m13c1 m13c1 m13c0 m13c1 = refl
  holds1340 m13c1 m13c1 m13c0 m13c2 = refl
  holds1340 m13c1 m13c1 m13c0 m13c3 = refl
  holds1340 m13c1 m13c1 m13c1 m13c0 = refl
  holds1340 m13c1 m13c1 m13c1 m13c1 = refl
  holds1340 m13c1 m13c1 m13c1 m13c2 = refl
  holds1340 m13c1 m13c1 m13c1 m13c3 = refl
  holds1340 m13c1 m13c1 m13c2 m13c0 = refl
  holds1340 m13c1 m13c1 m13c2 m13c1 = refl
  holds1340 m13c1 m13c1 m13c2 m13c2 = refl
  holds1340 m13c1 m13c1 m13c2 m13c3 = refl
  holds1340 m13c1 m13c1 m13c3 m13c0 = refl
  holds1340 m13c1 m13c1 m13c3 m13c1 = refl
  holds1340 m13c1 m13c1 m13c3 m13c2 = refl
  holds1340 m13c1 m13c1 m13c3 m13c3 = refl
  holds1340 m13c1 m13c2 m13c0 m13c0 = refl
  holds1340 m13c1 m13c2 m13c0 m13c1 = refl
  holds1340 m13c1 m13c2 m13c0 m13c2 = refl
  holds1340 m13c1 m13c2 m13c0 m13c3 = refl
  holds1340 m13c1 m13c2 m13c1 m13c0 = refl
  holds1340 m13c1 m13c2 m13c1 m13c1 = refl
  holds1340 m13c1 m13c2 m13c1 m13c2 = refl
  holds1340 m13c1 m13c2 m13c1 m13c3 = refl
  holds1340 m13c1 m13c2 m13c2 m13c0 = refl
  holds1340 m13c1 m13c2 m13c2 m13c1 = refl
  holds1340 m13c1 m13c2 m13c2 m13c2 = refl
  holds1340 m13c1 m13c2 m13c2 m13c3 = refl
  holds1340 m13c1 m13c2 m13c3 m13c0 = refl
  holds1340 m13c1 m13c2 m13c3 m13c1 = refl
  holds1340 m13c1 m13c2 m13c3 m13c2 = refl
  holds1340 m13c1 m13c2 m13c3 m13c3 = refl
  holds1340 m13c1 m13c3 m13c0 m13c0 = refl
  holds1340 m13c1 m13c3 m13c0 m13c1 = refl
  holds1340 m13c1 m13c3 m13c0 m13c2 = refl
  holds1340 m13c1 m13c3 m13c0 m13c3 = refl
  holds1340 m13c1 m13c3 m13c1 m13c0 = refl
  holds1340 m13c1 m13c3 m13c1 m13c1 = refl
  holds1340 m13c1 m13c3 m13c1 m13c2 = refl
  holds1340 m13c1 m13c3 m13c1 m13c3 = refl
  holds1340 m13c1 m13c3 m13c2 m13c0 = refl
  holds1340 m13c1 m13c3 m13c2 m13c1 = refl
  holds1340 m13c1 m13c3 m13c2 m13c2 = refl
  holds1340 m13c1 m13c3 m13c2 m13c3 = refl
  holds1340 m13c1 m13c3 m13c3 m13c0 = refl
  holds1340 m13c1 m13c3 m13c3 m13c1 = refl
  holds1340 m13c1 m13c3 m13c3 m13c2 = refl
  holds1340 m13c1 m13c3 m13c3 m13c3 = refl
  holds1340 m13c2 m13c0 m13c0 m13c0 = refl
  holds1340 m13c2 m13c0 m13c0 m13c1 = refl
  holds1340 m13c2 m13c0 m13c0 m13c2 = refl
  holds1340 m13c2 m13c0 m13c0 m13c3 = refl
  holds1340 m13c2 m13c0 m13c1 m13c0 = refl
  holds1340 m13c2 m13c0 m13c1 m13c1 = refl
  holds1340 m13c2 m13c0 m13c1 m13c2 = refl
  holds1340 m13c2 m13c0 m13c1 m13c3 = refl
  holds1340 m13c2 m13c0 m13c2 m13c0 = refl
  holds1340 m13c2 m13c0 m13c2 m13c1 = refl
  holds1340 m13c2 m13c0 m13c2 m13c2 = refl
  holds1340 m13c2 m13c0 m13c2 m13c3 = refl
  holds1340 m13c2 m13c0 m13c3 m13c0 = refl
  holds1340 m13c2 m13c0 m13c3 m13c1 = refl
  holds1340 m13c2 m13c0 m13c3 m13c2 = refl
  holds1340 m13c2 m13c0 m13c3 m13c3 = refl
  holds1340 m13c2 m13c1 m13c0 m13c0 = refl
  holds1340 m13c2 m13c1 m13c0 m13c1 = refl
  holds1340 m13c2 m13c1 m13c0 m13c2 = refl
  holds1340 m13c2 m13c1 m13c0 m13c3 = refl
  holds1340 m13c2 m13c1 m13c1 m13c0 = refl
  holds1340 m13c2 m13c1 m13c1 m13c1 = refl
  holds1340 m13c2 m13c1 m13c1 m13c2 = refl
  holds1340 m13c2 m13c1 m13c1 m13c3 = refl
  holds1340 m13c2 m13c1 m13c2 m13c0 = refl
  holds1340 m13c2 m13c1 m13c2 m13c1 = refl
  holds1340 m13c2 m13c1 m13c2 m13c2 = refl
  holds1340 m13c2 m13c1 m13c2 m13c3 = refl
  holds1340 m13c2 m13c1 m13c3 m13c0 = refl
  holds1340 m13c2 m13c1 m13c3 m13c1 = refl
  holds1340 m13c2 m13c1 m13c3 m13c2 = refl
  holds1340 m13c2 m13c1 m13c3 m13c3 = refl
  holds1340 m13c2 m13c2 m13c0 m13c0 = refl
  holds1340 m13c2 m13c2 m13c0 m13c1 = refl
  holds1340 m13c2 m13c2 m13c0 m13c2 = refl
  holds1340 m13c2 m13c2 m13c0 m13c3 = refl
  holds1340 m13c2 m13c2 m13c1 m13c0 = refl
  holds1340 m13c2 m13c2 m13c1 m13c1 = refl
  holds1340 m13c2 m13c2 m13c1 m13c2 = refl
  holds1340 m13c2 m13c2 m13c1 m13c3 = refl
  holds1340 m13c2 m13c2 m13c2 m13c0 = refl
  holds1340 m13c2 m13c2 m13c2 m13c1 = refl
  holds1340 m13c2 m13c2 m13c2 m13c2 = refl
  holds1340 m13c2 m13c2 m13c2 m13c3 = refl
  holds1340 m13c2 m13c2 m13c3 m13c0 = refl
  holds1340 m13c2 m13c2 m13c3 m13c1 = refl
  holds1340 m13c2 m13c2 m13c3 m13c2 = refl
  holds1340 m13c2 m13c2 m13c3 m13c3 = refl
  holds1340 m13c2 m13c3 m13c0 m13c0 = refl
  holds1340 m13c2 m13c3 m13c0 m13c1 = refl
  holds1340 m13c2 m13c3 m13c0 m13c2 = refl
  holds1340 m13c2 m13c3 m13c0 m13c3 = refl
  holds1340 m13c2 m13c3 m13c1 m13c0 = refl
  holds1340 m13c2 m13c3 m13c1 m13c1 = refl
  holds1340 m13c2 m13c3 m13c1 m13c2 = refl
  holds1340 m13c2 m13c3 m13c1 m13c3 = refl
  holds1340 m13c2 m13c3 m13c2 m13c0 = refl
  holds1340 m13c2 m13c3 m13c2 m13c1 = refl
  holds1340 m13c2 m13c3 m13c2 m13c2 = refl
  holds1340 m13c2 m13c3 m13c2 m13c3 = refl
  holds1340 m13c2 m13c3 m13c3 m13c0 = refl
  holds1340 m13c2 m13c3 m13c3 m13c1 = refl
  holds1340 m13c2 m13c3 m13c3 m13c2 = refl
  holds1340 m13c2 m13c3 m13c3 m13c3 = refl
  holds1340 m13c3 m13c0 m13c0 m13c0 = refl
  holds1340 m13c3 m13c0 m13c0 m13c1 = refl
  holds1340 m13c3 m13c0 m13c0 m13c2 = refl
  holds1340 m13c3 m13c0 m13c0 m13c3 = refl
  holds1340 m13c3 m13c0 m13c1 m13c0 = refl
  holds1340 m13c3 m13c0 m13c1 m13c1 = refl
  holds1340 m13c3 m13c0 m13c1 m13c2 = refl
  holds1340 m13c3 m13c0 m13c1 m13c3 = refl
  holds1340 m13c3 m13c0 m13c2 m13c0 = refl
  holds1340 m13c3 m13c0 m13c2 m13c1 = refl
  holds1340 m13c3 m13c0 m13c2 m13c2 = refl
  holds1340 m13c3 m13c0 m13c2 m13c3 = refl
  holds1340 m13c3 m13c0 m13c3 m13c0 = refl
  holds1340 m13c3 m13c0 m13c3 m13c1 = refl
  holds1340 m13c3 m13c0 m13c3 m13c2 = refl
  holds1340 m13c3 m13c0 m13c3 m13c3 = refl
  holds1340 m13c3 m13c1 m13c0 m13c0 = refl
  holds1340 m13c3 m13c1 m13c0 m13c1 = refl
  holds1340 m13c3 m13c1 m13c0 m13c2 = refl
  holds1340 m13c3 m13c1 m13c0 m13c3 = refl
  holds1340 m13c3 m13c1 m13c1 m13c0 = refl
  holds1340 m13c3 m13c1 m13c1 m13c1 = refl
  holds1340 m13c3 m13c1 m13c1 m13c2 = refl
  holds1340 m13c3 m13c1 m13c1 m13c3 = refl
  holds1340 m13c3 m13c1 m13c2 m13c0 = refl
  holds1340 m13c3 m13c1 m13c2 m13c1 = refl
  holds1340 m13c3 m13c1 m13c2 m13c2 = refl
  holds1340 m13c3 m13c1 m13c2 m13c3 = refl
  holds1340 m13c3 m13c1 m13c3 m13c0 = refl
  holds1340 m13c3 m13c1 m13c3 m13c1 = refl
  holds1340 m13c3 m13c1 m13c3 m13c2 = refl
  holds1340 m13c3 m13c1 m13c3 m13c3 = refl
  holds1340 m13c3 m13c2 m13c0 m13c0 = refl
  holds1340 m13c3 m13c2 m13c0 m13c1 = refl
  holds1340 m13c3 m13c2 m13c0 m13c2 = refl
  holds1340 m13c3 m13c2 m13c0 m13c3 = refl
  holds1340 m13c3 m13c2 m13c1 m13c0 = refl
  holds1340 m13c3 m13c2 m13c1 m13c1 = refl
  holds1340 m13c3 m13c2 m13c1 m13c2 = refl
  holds1340 m13c3 m13c2 m13c1 m13c3 = refl
  holds1340 m13c3 m13c2 m13c2 m13c0 = refl
  holds1340 m13c3 m13c2 m13c2 m13c1 = refl
  holds1340 m13c3 m13c2 m13c2 m13c2 = refl
  holds1340 m13c3 m13c2 m13c2 m13c3 = refl
  holds1340 m13c3 m13c2 m13c3 m13c0 = refl
  holds1340 m13c3 m13c2 m13c3 m13c1 = refl
  holds1340 m13c3 m13c2 m13c3 m13c2 = refl
  holds1340 m13c3 m13c2 m13c3 m13c3 = refl
  holds1340 m13c3 m13c3 m13c0 m13c0 = refl
  holds1340 m13c3 m13c3 m13c0 m13c1 = refl
  holds1340 m13c3 m13c3 m13c0 m13c2 = refl
  holds1340 m13c3 m13c3 m13c0 m13c3 = refl
  holds1340 m13c3 m13c3 m13c1 m13c0 = refl
  holds1340 m13c3 m13c3 m13c1 m13c1 = refl
  holds1340 m13c3 m13c3 m13c1 m13c2 = refl
  holds1340 m13c3 m13c3 m13c1 m13c3 = refl
  holds1340 m13c3 m13c3 m13c2 m13c0 = refl
  holds1340 m13c3 m13c3 m13c2 m13c1 = refl
  holds1340 m13c3 m13c3 m13c2 m13c2 = refl
  holds1340 m13c3 m13c3 m13c2 m13c3 = refl
  holds1340 m13c3 m13c3 m13c3 m13c0 = refl
  holds1340 m13c3 m13c3 m13c3 m13c1 = refl
  holds1340 m13c3 m13c3 m13c3 m13c2 = refl
  holds1340 m13c3 m13c3 m13c3 m13c3 = refl
  cut1340 : (x6 : ℕ) → Adequate {ℓ} ((var 0) , (op (op (op (var 1) (op (var 2) (var 2))) (var 0)) (op (var 0) (var x6)))) → ⊥
  cut1340 x6 = reject13 ((var 0) , (op (op (op (var 1) (op (var 2) (var 2))) (var 0)) (op (var 0) (var x6)))) (λ env → holds1340 (env 0) (env 1) (env 2) (env x6))
  holds1341 : (z0 z1 z2 : A3) → z0 ≡ (mul3 (mul3 (mul3 z1 (mul3 z2 z2)) z0) (mul3 z1 z0))
  holds1341 z0 z1 z2 = refl
  cut1341 : Adequate {ℓ} ((var 0) , (op (op (op (var 1) (op (var 2) (var 2))) (var 0)) (op (var 1) (var 0)))) → ⊥
  cut1341  = reject3 ((var 0) , (op (op (op (var 1) (op (var 2) (var 2))) (var 0)) (op (var 1) (var 0)))) (λ env → holds1341 (env 0) (env 1) (env 2))
  bad1342 : PathP (λ _ → Two) b0 (bop (bop (bop b1 (bop b0 b0)) b0) (bop b1 b1)) → ⊥
  bad1342  p = false≢true (cong lower p)
  cut1342 : Adequate {ℓ} ((var 0) , (op (op (op (var 1) (op (var 2) (var 2))) (var 0)) (op (var 1) (var 1)))) → ⊥
  cut1342  adequate = bad1342  (Adequate.valid adequate Two boolean env6)
  bad1343 : PathP (λ _ → Two) b0 (bop (bop (bop b1 (bop b1 b1)) b0) (bop b1 b1)) → ⊥
  bad1343  p = false≢true (cong lower p)
  cut1343 : Adequate {ℓ} ((var 0) , (op (op (op (var 1) (op (var 2) (var 2))) (var 0)) (op (var 1) (var 2)))) → ⊥
  cut1343  adequate = bad1343  (Adequate.valid adequate Two boolean env1)
  bad1344 : PathP (λ _ → Two) b0 (bop (bop (bop b1 (bop b0 b0)) b0) (bop b1 b1)) → ⊥
  bad1344  p = false≢true (cong lower p)
  cut1344 : Adequate {ℓ} ((var 0) , (op (op (op (var 1) (op (var 2) (var 2))) (var 0)) (op (var 1) (var 3)))) → ⊥
  cut1344  adequate = bad1344  (Adequate.valid adequate Two boolean env7)
  bad1345 : (z3 : Two) → PathP (λ _ → Two) b1 (bop (bop (bop b1 (bop b0 b0)) b1) (bop b0 z3)) → ⊥
  bad1345 z3 p = false≢true (sym (cong lower p))
  cut1345 : (x6 : ℕ) → Adequate {ℓ} ((var 0) , (op (op (op (var 1) (op (var 2) (var 2))) (var 0)) (op (var 2) (var x6)))) → ⊥
  cut1345 x6 adequate = bad1345 (env8 x6) (Adequate.valid adequate Two boolean env8)
  bad1346 : (z4 : Two) → PathP (λ _ → Two) b1 (bop (bop (bop b1 (bop b0 b0)) b1) (bop b0 z4)) → ⊥
  bad1346 z4 p = false≢true (sym (cong lower p))
  cut1346 : (x6 : ℕ) → Adequate {ℓ} ((var 0) , (op (op (op (var 1) (op (var 2) (var 2))) (var 0)) (op (var 3) (var x6)))) → ⊥
  cut1346 x6 adequate = bad1346 (env9 x6) (Adequate.valid adequate Two boolean env9)
  bad1347 : (z3 z4 : Two) → PathP (λ _ → Two) b0 (bop (bop (bop b1 (bop b1 b1)) b1) (bop z3 z4)) → ⊥
  bad1347 z3 z4 p = false≢true (cong lower p)
  cut1347 : (x5 x6 : ℕ) → Adequate {ℓ} ((var 0) , (op (op (op (var 1) (op (var 2) (var 2))) (var 1)) (op (var x5) (var x6)))) → ⊥
  cut1347 x5 x6 adequate = bad1347 (env1 x5) (env1 x6) (Adequate.valid adequate Two boolean env1)
  bad1348 : (z3 z4 : Two) → PathP (λ _ → Two) b0 (bop (bop (bop b0 (bop b1 b1)) b1) (bop z3 z4)) → ⊥
  bad1348 z3 z4 p = false≢true (cong lower p)
  cut1348 : (x5 x6 : ℕ) → Adequate {ℓ} ((var 0) , (op (op (op (var 1) (op (var 2) (var 2))) (var 2)) (op (var x5) (var x6)))) → ⊥
  cut1348 x5 x6 adequate = bad1348 (env2 x5) (env2 x6) (Adequate.valid adequate Two boolean env2)
  bad1349 : (z4 z5 : Two) → PathP (λ _ → Two) b0 (bop (bop (bop b0 (bop b0 b0)) b1) (bop z4 z5)) → ⊥
  bad1349 z4 z5 p = false≢true (cong lower p)
  cut1349 : (x5 x6 : ℕ) → Adequate {ℓ} ((var 0) , (op (op (op (var 1) (op (var 2) (var 2))) (var 3)) (op (var x5) (var x6)))) → ⊥
  cut1349 x5 x6 adequate = bad1349 (env11 x5) (env11 x6) (Adequate.valid adequate Two boolean env11)
  holds1350 : (z0 z1 z2 z3 z4 : A13) → z0 ≡ (mul13 (mul13 (mul13 z1 (mul13 z2 z3)) z0) (mul13 z0 z4))
  holds1350 m13c0 m13c0 m13c0 m13c0 m13c0 = refl
  holds1350 m13c0 m13c0 m13c0 m13c0 m13c1 = refl
  holds1350 m13c0 m13c0 m13c0 m13c0 m13c2 = refl
  holds1350 m13c0 m13c0 m13c0 m13c0 m13c3 = refl
  holds1350 m13c0 m13c0 m13c0 m13c1 m13c0 = refl
  holds1350 m13c0 m13c0 m13c0 m13c1 m13c1 = refl
  holds1350 m13c0 m13c0 m13c0 m13c1 m13c2 = refl
  holds1350 m13c0 m13c0 m13c0 m13c1 m13c3 = refl
  holds1350 m13c0 m13c0 m13c0 m13c2 m13c0 = refl
  holds1350 m13c0 m13c0 m13c0 m13c2 m13c1 = refl
  holds1350 m13c0 m13c0 m13c0 m13c2 m13c2 = refl
  holds1350 m13c0 m13c0 m13c0 m13c2 m13c3 = refl
  holds1350 m13c0 m13c0 m13c0 m13c3 m13c0 = refl
  holds1350 m13c0 m13c0 m13c0 m13c3 m13c1 = refl
  holds1350 m13c0 m13c0 m13c0 m13c3 m13c2 = refl
  holds1350 m13c0 m13c0 m13c0 m13c3 m13c3 = refl
  holds1350 m13c0 m13c0 m13c1 m13c0 m13c0 = refl
  holds1350 m13c0 m13c0 m13c1 m13c0 m13c1 = refl
  holds1350 m13c0 m13c0 m13c1 m13c0 m13c2 = refl
  holds1350 m13c0 m13c0 m13c1 m13c0 m13c3 = refl
  holds1350 m13c0 m13c0 m13c1 m13c1 m13c0 = refl
  holds1350 m13c0 m13c0 m13c1 m13c1 m13c1 = refl
  holds1350 m13c0 m13c0 m13c1 m13c1 m13c2 = refl
  holds1350 m13c0 m13c0 m13c1 m13c1 m13c3 = refl
  holds1350 m13c0 m13c0 m13c1 m13c2 m13c0 = refl
  holds1350 m13c0 m13c0 m13c1 m13c2 m13c1 = refl
  holds1350 m13c0 m13c0 m13c1 m13c2 m13c2 = refl
  holds1350 m13c0 m13c0 m13c1 m13c2 m13c3 = refl
  holds1350 m13c0 m13c0 m13c1 m13c3 m13c0 = refl
  holds1350 m13c0 m13c0 m13c1 m13c3 m13c1 = refl
  holds1350 m13c0 m13c0 m13c1 m13c3 m13c2 = refl
  holds1350 m13c0 m13c0 m13c1 m13c3 m13c3 = refl
  holds1350 m13c0 m13c0 m13c2 m13c0 m13c0 = refl
  holds1350 m13c0 m13c0 m13c2 m13c0 m13c1 = refl
  holds1350 m13c0 m13c0 m13c2 m13c0 m13c2 = refl
  holds1350 m13c0 m13c0 m13c2 m13c0 m13c3 = refl
  holds1350 m13c0 m13c0 m13c2 m13c1 m13c0 = refl
  holds1350 m13c0 m13c0 m13c2 m13c1 m13c1 = refl
  holds1350 m13c0 m13c0 m13c2 m13c1 m13c2 = refl
  holds1350 m13c0 m13c0 m13c2 m13c1 m13c3 = refl
  holds1350 m13c0 m13c0 m13c2 m13c2 m13c0 = refl
  holds1350 m13c0 m13c0 m13c2 m13c2 m13c1 = refl
  holds1350 m13c0 m13c0 m13c2 m13c2 m13c2 = refl
  holds1350 m13c0 m13c0 m13c2 m13c2 m13c3 = refl
  holds1350 m13c0 m13c0 m13c2 m13c3 m13c0 = refl
  holds1350 m13c0 m13c0 m13c2 m13c3 m13c1 = refl
  holds1350 m13c0 m13c0 m13c2 m13c3 m13c2 = refl
  holds1350 m13c0 m13c0 m13c2 m13c3 m13c3 = refl
  holds1350 m13c0 m13c0 m13c3 m13c0 m13c0 = refl
  holds1350 m13c0 m13c0 m13c3 m13c0 m13c1 = refl
  holds1350 m13c0 m13c0 m13c3 m13c0 m13c2 = refl
  holds1350 m13c0 m13c0 m13c3 m13c0 m13c3 = refl
  holds1350 m13c0 m13c0 m13c3 m13c1 m13c0 = refl
  holds1350 m13c0 m13c0 m13c3 m13c1 m13c1 = refl
  holds1350 m13c0 m13c0 m13c3 m13c1 m13c2 = refl
  holds1350 m13c0 m13c0 m13c3 m13c1 m13c3 = refl
  holds1350 m13c0 m13c0 m13c3 m13c2 m13c0 = refl
  holds1350 m13c0 m13c0 m13c3 m13c2 m13c1 = refl
  holds1350 m13c0 m13c0 m13c3 m13c2 m13c2 = refl
  holds1350 m13c0 m13c0 m13c3 m13c2 m13c3 = refl
  holds1350 m13c0 m13c0 m13c3 m13c3 m13c0 = refl
  holds1350 m13c0 m13c0 m13c3 m13c3 m13c1 = refl
  holds1350 m13c0 m13c0 m13c3 m13c3 m13c2 = refl
  holds1350 m13c0 m13c0 m13c3 m13c3 m13c3 = refl
  holds1350 m13c0 m13c1 m13c0 m13c0 m13c0 = refl
  holds1350 m13c0 m13c1 m13c0 m13c0 m13c1 = refl
  holds1350 m13c0 m13c1 m13c0 m13c0 m13c2 = refl
  holds1350 m13c0 m13c1 m13c0 m13c0 m13c3 = refl
  holds1350 m13c0 m13c1 m13c0 m13c1 m13c0 = refl
  holds1350 m13c0 m13c1 m13c0 m13c1 m13c1 = refl
  holds1350 m13c0 m13c1 m13c0 m13c1 m13c2 = refl
  holds1350 m13c0 m13c1 m13c0 m13c1 m13c3 = refl
  holds1350 m13c0 m13c1 m13c0 m13c2 m13c0 = refl
  holds1350 m13c0 m13c1 m13c0 m13c2 m13c1 = refl
  holds1350 m13c0 m13c1 m13c0 m13c2 m13c2 = refl
  holds1350 m13c0 m13c1 m13c0 m13c2 m13c3 = refl
  holds1350 m13c0 m13c1 m13c0 m13c3 m13c0 = refl
  holds1350 m13c0 m13c1 m13c0 m13c3 m13c1 = refl
  holds1350 m13c0 m13c1 m13c0 m13c3 m13c2 = refl
  holds1350 m13c0 m13c1 m13c0 m13c3 m13c3 = refl
  holds1350 m13c0 m13c1 m13c1 m13c0 m13c0 = refl
  holds1350 m13c0 m13c1 m13c1 m13c0 m13c1 = refl
  holds1350 m13c0 m13c1 m13c1 m13c0 m13c2 = refl
  holds1350 m13c0 m13c1 m13c1 m13c0 m13c3 = refl
  holds1350 m13c0 m13c1 m13c1 m13c1 m13c0 = refl
  holds1350 m13c0 m13c1 m13c1 m13c1 m13c1 = refl
  holds1350 m13c0 m13c1 m13c1 m13c1 m13c2 = refl
  holds1350 m13c0 m13c1 m13c1 m13c1 m13c3 = refl
  holds1350 m13c0 m13c1 m13c1 m13c2 m13c0 = refl
  holds1350 m13c0 m13c1 m13c1 m13c2 m13c1 = refl
  holds1350 m13c0 m13c1 m13c1 m13c2 m13c2 = refl
  holds1350 m13c0 m13c1 m13c1 m13c2 m13c3 = refl
  holds1350 m13c0 m13c1 m13c1 m13c3 m13c0 = refl
  holds1350 m13c0 m13c1 m13c1 m13c3 m13c1 = refl
  holds1350 m13c0 m13c1 m13c1 m13c3 m13c2 = refl
  holds1350 m13c0 m13c1 m13c1 m13c3 m13c3 = refl
  holds1350 m13c0 m13c1 m13c2 m13c0 m13c0 = refl
  holds1350 m13c0 m13c1 m13c2 m13c0 m13c1 = refl
  holds1350 m13c0 m13c1 m13c2 m13c0 m13c2 = refl
  holds1350 m13c0 m13c1 m13c2 m13c0 m13c3 = refl
  holds1350 m13c0 m13c1 m13c2 m13c1 m13c0 = refl
  holds1350 m13c0 m13c1 m13c2 m13c1 m13c1 = refl
  holds1350 m13c0 m13c1 m13c2 m13c1 m13c2 = refl
  holds1350 m13c0 m13c1 m13c2 m13c1 m13c3 = refl
  holds1350 m13c0 m13c1 m13c2 m13c2 m13c0 = refl
  holds1350 m13c0 m13c1 m13c2 m13c2 m13c1 = refl
  holds1350 m13c0 m13c1 m13c2 m13c2 m13c2 = refl
  holds1350 m13c0 m13c1 m13c2 m13c2 m13c3 = refl
  holds1350 m13c0 m13c1 m13c2 m13c3 m13c0 = refl
  holds1350 m13c0 m13c1 m13c2 m13c3 m13c1 = refl
  holds1350 m13c0 m13c1 m13c2 m13c3 m13c2 = refl
  holds1350 m13c0 m13c1 m13c2 m13c3 m13c3 = refl
  holds1350 m13c0 m13c1 m13c3 m13c0 m13c0 = refl
  holds1350 m13c0 m13c1 m13c3 m13c0 m13c1 = refl
  holds1350 m13c0 m13c1 m13c3 m13c0 m13c2 = refl
  holds1350 m13c0 m13c1 m13c3 m13c0 m13c3 = refl
  holds1350 m13c0 m13c1 m13c3 m13c1 m13c0 = refl
  holds1350 m13c0 m13c1 m13c3 m13c1 m13c1 = refl
  holds1350 m13c0 m13c1 m13c3 m13c1 m13c2 = refl
  holds1350 m13c0 m13c1 m13c3 m13c1 m13c3 = refl
  holds1350 m13c0 m13c1 m13c3 m13c2 m13c0 = refl
  holds1350 m13c0 m13c1 m13c3 m13c2 m13c1 = refl
  holds1350 m13c0 m13c1 m13c3 m13c2 m13c2 = refl
  holds1350 m13c0 m13c1 m13c3 m13c2 m13c3 = refl
  holds1350 m13c0 m13c1 m13c3 m13c3 m13c0 = refl
  holds1350 m13c0 m13c1 m13c3 m13c3 m13c1 = refl
  holds1350 m13c0 m13c1 m13c3 m13c3 m13c2 = refl
  holds1350 m13c0 m13c1 m13c3 m13c3 m13c3 = refl
  holds1350 m13c0 m13c2 m13c0 m13c0 m13c0 = refl
  holds1350 m13c0 m13c2 m13c0 m13c0 m13c1 = refl
  holds1350 m13c0 m13c2 m13c0 m13c0 m13c2 = refl
  holds1350 m13c0 m13c2 m13c0 m13c0 m13c3 = refl
  holds1350 m13c0 m13c2 m13c0 m13c1 m13c0 = refl
  holds1350 m13c0 m13c2 m13c0 m13c1 m13c1 = refl
  holds1350 m13c0 m13c2 m13c0 m13c1 m13c2 = refl
  holds1350 m13c0 m13c2 m13c0 m13c1 m13c3 = refl
  holds1350 m13c0 m13c2 m13c0 m13c2 m13c0 = refl
  holds1350 m13c0 m13c2 m13c0 m13c2 m13c1 = refl
  holds1350 m13c0 m13c2 m13c0 m13c2 m13c2 = refl
  holds1350 m13c0 m13c2 m13c0 m13c2 m13c3 = refl
  holds1350 m13c0 m13c2 m13c0 m13c3 m13c0 = refl
  holds1350 m13c0 m13c2 m13c0 m13c3 m13c1 = refl
  holds1350 m13c0 m13c2 m13c0 m13c3 m13c2 = refl
  holds1350 m13c0 m13c2 m13c0 m13c3 m13c3 = refl
  holds1350 m13c0 m13c2 m13c1 m13c0 m13c0 = refl
  holds1350 m13c0 m13c2 m13c1 m13c0 m13c1 = refl
  holds1350 m13c0 m13c2 m13c1 m13c0 m13c2 = refl
  holds1350 m13c0 m13c2 m13c1 m13c0 m13c3 = refl
  holds1350 m13c0 m13c2 m13c1 m13c1 m13c0 = refl
  holds1350 m13c0 m13c2 m13c1 m13c1 m13c1 = refl
  holds1350 m13c0 m13c2 m13c1 m13c1 m13c2 = refl
  holds1350 m13c0 m13c2 m13c1 m13c1 m13c3 = refl
  holds1350 m13c0 m13c2 m13c1 m13c2 m13c0 = refl
  holds1350 m13c0 m13c2 m13c1 m13c2 m13c1 = refl
  holds1350 m13c0 m13c2 m13c1 m13c2 m13c2 = refl
  holds1350 m13c0 m13c2 m13c1 m13c2 m13c3 = refl
  holds1350 m13c0 m13c2 m13c1 m13c3 m13c0 = refl
  holds1350 m13c0 m13c2 m13c1 m13c3 m13c1 = refl
  holds1350 m13c0 m13c2 m13c1 m13c3 m13c2 = refl
  holds1350 m13c0 m13c2 m13c1 m13c3 m13c3 = refl
  holds1350 m13c0 m13c2 m13c2 m13c0 m13c0 = refl
  holds1350 m13c0 m13c2 m13c2 m13c0 m13c1 = refl
  holds1350 m13c0 m13c2 m13c2 m13c0 m13c2 = refl
  holds1350 m13c0 m13c2 m13c2 m13c0 m13c3 = refl
  holds1350 m13c0 m13c2 m13c2 m13c1 m13c0 = refl
  holds1350 m13c0 m13c2 m13c2 m13c1 m13c1 = refl
  holds1350 m13c0 m13c2 m13c2 m13c1 m13c2 = refl
  holds1350 m13c0 m13c2 m13c2 m13c1 m13c3 = refl
  holds1350 m13c0 m13c2 m13c2 m13c2 m13c0 = refl
  holds1350 m13c0 m13c2 m13c2 m13c2 m13c1 = refl
  holds1350 m13c0 m13c2 m13c2 m13c2 m13c2 = refl
  holds1350 m13c0 m13c2 m13c2 m13c2 m13c3 = refl
  holds1350 m13c0 m13c2 m13c2 m13c3 m13c0 = refl
  holds1350 m13c0 m13c2 m13c2 m13c3 m13c1 = refl
  holds1350 m13c0 m13c2 m13c2 m13c3 m13c2 = refl
  holds1350 m13c0 m13c2 m13c2 m13c3 m13c3 = refl
  holds1350 m13c0 m13c2 m13c3 m13c0 m13c0 = refl
  holds1350 m13c0 m13c2 m13c3 m13c0 m13c1 = refl
  holds1350 m13c0 m13c2 m13c3 m13c0 m13c2 = refl
  holds1350 m13c0 m13c2 m13c3 m13c0 m13c3 = refl
  holds1350 m13c0 m13c2 m13c3 m13c1 m13c0 = refl
  holds1350 m13c0 m13c2 m13c3 m13c1 m13c1 = refl
  holds1350 m13c0 m13c2 m13c3 m13c1 m13c2 = refl
  holds1350 m13c0 m13c2 m13c3 m13c1 m13c3 = refl
  holds1350 m13c0 m13c2 m13c3 m13c2 m13c0 = refl
  holds1350 m13c0 m13c2 m13c3 m13c2 m13c1 = refl
  holds1350 m13c0 m13c2 m13c3 m13c2 m13c2 = refl
  holds1350 m13c0 m13c2 m13c3 m13c2 m13c3 = refl
  holds1350 m13c0 m13c2 m13c3 m13c3 m13c0 = refl
  holds1350 m13c0 m13c2 m13c3 m13c3 m13c1 = refl
  holds1350 m13c0 m13c2 m13c3 m13c3 m13c2 = refl
  holds1350 m13c0 m13c2 m13c3 m13c3 m13c3 = refl
  holds1350 m13c0 m13c3 m13c0 m13c0 m13c0 = refl
  holds1350 m13c0 m13c3 m13c0 m13c0 m13c1 = refl
  holds1350 m13c0 m13c3 m13c0 m13c0 m13c2 = refl
  holds1350 m13c0 m13c3 m13c0 m13c0 m13c3 = refl
  holds1350 m13c0 m13c3 m13c0 m13c1 m13c0 = refl
  holds1350 m13c0 m13c3 m13c0 m13c1 m13c1 = refl
  holds1350 m13c0 m13c3 m13c0 m13c1 m13c2 = refl
  holds1350 m13c0 m13c3 m13c0 m13c1 m13c3 = refl
  holds1350 m13c0 m13c3 m13c0 m13c2 m13c0 = refl
  holds1350 m13c0 m13c3 m13c0 m13c2 m13c1 = refl
  holds1350 m13c0 m13c3 m13c0 m13c2 m13c2 = refl
  holds1350 m13c0 m13c3 m13c0 m13c2 m13c3 = refl
  holds1350 m13c0 m13c3 m13c0 m13c3 m13c0 = refl
  holds1350 m13c0 m13c3 m13c0 m13c3 m13c1 = refl
  holds1350 m13c0 m13c3 m13c0 m13c3 m13c2 = refl
  holds1350 m13c0 m13c3 m13c0 m13c3 m13c3 = refl
  holds1350 m13c0 m13c3 m13c1 m13c0 m13c0 = refl
  holds1350 m13c0 m13c3 m13c1 m13c0 m13c1 = refl
  holds1350 m13c0 m13c3 m13c1 m13c0 m13c2 = refl
  holds1350 m13c0 m13c3 m13c1 m13c0 m13c3 = refl
  holds1350 m13c0 m13c3 m13c1 m13c1 m13c0 = refl
  holds1350 m13c0 m13c3 m13c1 m13c1 m13c1 = refl
  holds1350 m13c0 m13c3 m13c1 m13c1 m13c2 = refl
  holds1350 m13c0 m13c3 m13c1 m13c1 m13c3 = refl
  holds1350 m13c0 m13c3 m13c1 m13c2 m13c0 = refl
  holds1350 m13c0 m13c3 m13c1 m13c2 m13c1 = refl
  holds1350 m13c0 m13c3 m13c1 m13c2 m13c2 = refl
  holds1350 m13c0 m13c3 m13c1 m13c2 m13c3 = refl
  holds1350 m13c0 m13c3 m13c1 m13c3 m13c0 = refl
  holds1350 m13c0 m13c3 m13c1 m13c3 m13c1 = refl
  holds1350 m13c0 m13c3 m13c1 m13c3 m13c2 = refl
  holds1350 m13c0 m13c3 m13c1 m13c3 m13c3 = refl
  holds1350 m13c0 m13c3 m13c2 m13c0 m13c0 = refl
  holds1350 m13c0 m13c3 m13c2 m13c0 m13c1 = refl
  holds1350 m13c0 m13c3 m13c2 m13c0 m13c2 = refl
  holds1350 m13c0 m13c3 m13c2 m13c0 m13c3 = refl
  holds1350 m13c0 m13c3 m13c2 m13c1 m13c0 = refl
  holds1350 m13c0 m13c3 m13c2 m13c1 m13c1 = refl
  holds1350 m13c0 m13c3 m13c2 m13c1 m13c2 = refl
  holds1350 m13c0 m13c3 m13c2 m13c1 m13c3 = refl
  holds1350 m13c0 m13c3 m13c2 m13c2 m13c0 = refl
  holds1350 m13c0 m13c3 m13c2 m13c2 m13c1 = refl
  holds1350 m13c0 m13c3 m13c2 m13c2 m13c2 = refl
  holds1350 m13c0 m13c3 m13c2 m13c2 m13c3 = refl
  holds1350 m13c0 m13c3 m13c2 m13c3 m13c0 = refl
  holds1350 m13c0 m13c3 m13c2 m13c3 m13c1 = refl
  holds1350 m13c0 m13c3 m13c2 m13c3 m13c2 = refl
  holds1350 m13c0 m13c3 m13c2 m13c3 m13c3 = refl
  holds1350 m13c0 m13c3 m13c3 m13c0 m13c0 = refl
  holds1350 m13c0 m13c3 m13c3 m13c0 m13c1 = refl
  holds1350 m13c0 m13c3 m13c3 m13c0 m13c2 = refl
  holds1350 m13c0 m13c3 m13c3 m13c0 m13c3 = refl
  holds1350 m13c0 m13c3 m13c3 m13c1 m13c0 = refl
  holds1350 m13c0 m13c3 m13c3 m13c1 m13c1 = refl
  holds1350 m13c0 m13c3 m13c3 m13c1 m13c2 = refl
  holds1350 m13c0 m13c3 m13c3 m13c1 m13c3 = refl
  holds1350 m13c0 m13c3 m13c3 m13c2 m13c0 = refl
  holds1350 m13c0 m13c3 m13c3 m13c2 m13c1 = refl
  holds1350 m13c0 m13c3 m13c3 m13c2 m13c2 = refl
  holds1350 m13c0 m13c3 m13c3 m13c2 m13c3 = refl
  holds1350 m13c0 m13c3 m13c3 m13c3 m13c0 = refl
  holds1350 m13c0 m13c3 m13c3 m13c3 m13c1 = refl
  holds1350 m13c0 m13c3 m13c3 m13c3 m13c2 = refl
  holds1350 m13c0 m13c3 m13c3 m13c3 m13c3 = refl
  holds1350 m13c1 m13c0 m13c0 m13c0 m13c0 = refl
  holds1350 m13c1 m13c0 m13c0 m13c0 m13c1 = refl
  holds1350 m13c1 m13c0 m13c0 m13c0 m13c2 = refl
  holds1350 m13c1 m13c0 m13c0 m13c0 m13c3 = refl
  holds1350 m13c1 m13c0 m13c0 m13c1 m13c0 = refl
  holds1350 m13c1 m13c0 m13c0 m13c1 m13c1 = refl
  holds1350 m13c1 m13c0 m13c0 m13c1 m13c2 = refl
  holds1350 m13c1 m13c0 m13c0 m13c1 m13c3 = refl
  holds1350 m13c1 m13c0 m13c0 m13c2 m13c0 = refl
  holds1350 m13c1 m13c0 m13c0 m13c2 m13c1 = refl
  holds1350 m13c1 m13c0 m13c0 m13c2 m13c2 = refl
  holds1350 m13c1 m13c0 m13c0 m13c2 m13c3 = refl
  holds1350 m13c1 m13c0 m13c0 m13c3 m13c0 = refl
  holds1350 m13c1 m13c0 m13c0 m13c3 m13c1 = refl
  holds1350 m13c1 m13c0 m13c0 m13c3 m13c2 = refl
  holds1350 m13c1 m13c0 m13c0 m13c3 m13c3 = refl
  holds1350 m13c1 m13c0 m13c1 m13c0 m13c0 = refl
  holds1350 m13c1 m13c0 m13c1 m13c0 m13c1 = refl
  holds1350 m13c1 m13c0 m13c1 m13c0 m13c2 = refl
  holds1350 m13c1 m13c0 m13c1 m13c0 m13c3 = refl
  holds1350 m13c1 m13c0 m13c1 m13c1 m13c0 = refl
  holds1350 m13c1 m13c0 m13c1 m13c1 m13c1 = refl
  holds1350 m13c1 m13c0 m13c1 m13c1 m13c2 = refl
  holds1350 m13c1 m13c0 m13c1 m13c1 m13c3 = refl
  holds1350 m13c1 m13c0 m13c1 m13c2 m13c0 = refl
  holds1350 m13c1 m13c0 m13c1 m13c2 m13c1 = refl
  holds1350 m13c1 m13c0 m13c1 m13c2 m13c2 = refl
  holds1350 m13c1 m13c0 m13c1 m13c2 m13c3 = refl
  holds1350 m13c1 m13c0 m13c1 m13c3 m13c0 = refl
  holds1350 m13c1 m13c0 m13c1 m13c3 m13c1 = refl
  holds1350 m13c1 m13c0 m13c1 m13c3 m13c2 = refl
  holds1350 m13c1 m13c0 m13c1 m13c3 m13c3 = refl
  holds1350 m13c1 m13c0 m13c2 m13c0 m13c0 = refl
  holds1350 m13c1 m13c0 m13c2 m13c0 m13c1 = refl
  holds1350 m13c1 m13c0 m13c2 m13c0 m13c2 = refl
  holds1350 m13c1 m13c0 m13c2 m13c0 m13c3 = refl
  holds1350 m13c1 m13c0 m13c2 m13c1 m13c0 = refl
  holds1350 m13c1 m13c0 m13c2 m13c1 m13c1 = refl
  holds1350 m13c1 m13c0 m13c2 m13c1 m13c2 = refl
  holds1350 m13c1 m13c0 m13c2 m13c1 m13c3 = refl
  holds1350 m13c1 m13c0 m13c2 m13c2 m13c0 = refl
  holds1350 m13c1 m13c0 m13c2 m13c2 m13c1 = refl
  holds1350 m13c1 m13c0 m13c2 m13c2 m13c2 = refl
  holds1350 m13c1 m13c0 m13c2 m13c2 m13c3 = refl
  holds1350 m13c1 m13c0 m13c2 m13c3 m13c0 = refl
  holds1350 m13c1 m13c0 m13c2 m13c3 m13c1 = refl
  holds1350 m13c1 m13c0 m13c2 m13c3 m13c2 = refl
  holds1350 m13c1 m13c0 m13c2 m13c3 m13c3 = refl
  holds1350 m13c1 m13c0 m13c3 m13c0 m13c0 = refl
  holds1350 m13c1 m13c0 m13c3 m13c0 m13c1 = refl
  holds1350 m13c1 m13c0 m13c3 m13c0 m13c2 = refl
  holds1350 m13c1 m13c0 m13c3 m13c0 m13c3 = refl
  holds1350 m13c1 m13c0 m13c3 m13c1 m13c0 = refl
  holds1350 m13c1 m13c0 m13c3 m13c1 m13c1 = refl
  holds1350 m13c1 m13c0 m13c3 m13c1 m13c2 = refl
  holds1350 m13c1 m13c0 m13c3 m13c1 m13c3 = refl
  holds1350 m13c1 m13c0 m13c3 m13c2 m13c0 = refl
  holds1350 m13c1 m13c0 m13c3 m13c2 m13c1 = refl
  holds1350 m13c1 m13c0 m13c3 m13c2 m13c2 = refl
  holds1350 m13c1 m13c0 m13c3 m13c2 m13c3 = refl
  holds1350 m13c1 m13c0 m13c3 m13c3 m13c0 = refl
  holds1350 m13c1 m13c0 m13c3 m13c3 m13c1 = refl
  holds1350 m13c1 m13c0 m13c3 m13c3 m13c2 = refl
  holds1350 m13c1 m13c0 m13c3 m13c3 m13c3 = refl
  holds1350 m13c1 m13c1 m13c0 m13c0 m13c0 = refl
  holds1350 m13c1 m13c1 m13c0 m13c0 m13c1 = refl
  holds1350 m13c1 m13c1 m13c0 m13c0 m13c2 = refl
  holds1350 m13c1 m13c1 m13c0 m13c0 m13c3 = refl
  holds1350 m13c1 m13c1 m13c0 m13c1 m13c0 = refl
  holds1350 m13c1 m13c1 m13c0 m13c1 m13c1 = refl
  holds1350 m13c1 m13c1 m13c0 m13c1 m13c2 = refl
  holds1350 m13c1 m13c1 m13c0 m13c1 m13c3 = refl
  holds1350 m13c1 m13c1 m13c0 m13c2 m13c0 = refl
  holds1350 m13c1 m13c1 m13c0 m13c2 m13c1 = refl
  holds1350 m13c1 m13c1 m13c0 m13c2 m13c2 = refl
  holds1350 m13c1 m13c1 m13c0 m13c2 m13c3 = refl
  holds1350 m13c1 m13c1 m13c0 m13c3 m13c0 = refl
  holds1350 m13c1 m13c1 m13c0 m13c3 m13c1 = refl
  holds1350 m13c1 m13c1 m13c0 m13c3 m13c2 = refl
  holds1350 m13c1 m13c1 m13c0 m13c3 m13c3 = refl
  holds1350 m13c1 m13c1 m13c1 m13c0 m13c0 = refl
  holds1350 m13c1 m13c1 m13c1 m13c0 m13c1 = refl
  holds1350 m13c1 m13c1 m13c1 m13c0 m13c2 = refl
  holds1350 m13c1 m13c1 m13c1 m13c0 m13c3 = refl
  holds1350 m13c1 m13c1 m13c1 m13c1 m13c0 = refl
  holds1350 m13c1 m13c1 m13c1 m13c1 m13c1 = refl
  holds1350 m13c1 m13c1 m13c1 m13c1 m13c2 = refl
  holds1350 m13c1 m13c1 m13c1 m13c1 m13c3 = refl
  holds1350 m13c1 m13c1 m13c1 m13c2 m13c0 = refl
  holds1350 m13c1 m13c1 m13c1 m13c2 m13c1 = refl
  holds1350 m13c1 m13c1 m13c1 m13c2 m13c2 = refl
  holds1350 m13c1 m13c1 m13c1 m13c2 m13c3 = refl
  holds1350 m13c1 m13c1 m13c1 m13c3 m13c0 = refl
  holds1350 m13c1 m13c1 m13c1 m13c3 m13c1 = refl
  holds1350 m13c1 m13c1 m13c1 m13c3 m13c2 = refl
  holds1350 m13c1 m13c1 m13c1 m13c3 m13c3 = refl
  holds1350 m13c1 m13c1 m13c2 m13c0 m13c0 = refl
  holds1350 m13c1 m13c1 m13c2 m13c0 m13c1 = refl
  holds1350 m13c1 m13c1 m13c2 m13c0 m13c2 = refl
  holds1350 m13c1 m13c1 m13c2 m13c0 m13c3 = refl
  holds1350 m13c1 m13c1 m13c2 m13c1 m13c0 = refl
  holds1350 m13c1 m13c1 m13c2 m13c1 m13c1 = refl
  holds1350 m13c1 m13c1 m13c2 m13c1 m13c2 = refl
  holds1350 m13c1 m13c1 m13c2 m13c1 m13c3 = refl
  holds1350 m13c1 m13c1 m13c2 m13c2 m13c0 = refl
  holds1350 m13c1 m13c1 m13c2 m13c2 m13c1 = refl
  holds1350 m13c1 m13c1 m13c2 m13c2 m13c2 = refl
  holds1350 m13c1 m13c1 m13c2 m13c2 m13c3 = refl
  holds1350 m13c1 m13c1 m13c2 m13c3 m13c0 = refl
  holds1350 m13c1 m13c1 m13c2 m13c3 m13c1 = refl
  holds1350 m13c1 m13c1 m13c2 m13c3 m13c2 = refl
  holds1350 m13c1 m13c1 m13c2 m13c3 m13c3 = refl
  holds1350 m13c1 m13c1 m13c3 m13c0 m13c0 = refl
  holds1350 m13c1 m13c1 m13c3 m13c0 m13c1 = refl
  holds1350 m13c1 m13c1 m13c3 m13c0 m13c2 = refl
  holds1350 m13c1 m13c1 m13c3 m13c0 m13c3 = refl
  holds1350 m13c1 m13c1 m13c3 m13c1 m13c0 = refl
  holds1350 m13c1 m13c1 m13c3 m13c1 m13c1 = refl
  holds1350 m13c1 m13c1 m13c3 m13c1 m13c2 = refl
  holds1350 m13c1 m13c1 m13c3 m13c1 m13c3 = refl
  holds1350 m13c1 m13c1 m13c3 m13c2 m13c0 = refl
  holds1350 m13c1 m13c1 m13c3 m13c2 m13c1 = refl
  holds1350 m13c1 m13c1 m13c3 m13c2 m13c2 = refl
  holds1350 m13c1 m13c1 m13c3 m13c2 m13c3 = refl
  holds1350 m13c1 m13c1 m13c3 m13c3 m13c0 = refl
  holds1350 m13c1 m13c1 m13c3 m13c3 m13c1 = refl
  holds1350 m13c1 m13c1 m13c3 m13c3 m13c2 = refl
  holds1350 m13c1 m13c1 m13c3 m13c3 m13c3 = refl
  holds1350 m13c1 m13c2 m13c0 m13c0 m13c0 = refl
  holds1350 m13c1 m13c2 m13c0 m13c0 m13c1 = refl
  holds1350 m13c1 m13c2 m13c0 m13c0 m13c2 = refl
  holds1350 m13c1 m13c2 m13c0 m13c0 m13c3 = refl
  holds1350 m13c1 m13c2 m13c0 m13c1 m13c0 = refl
  holds1350 m13c1 m13c2 m13c0 m13c1 m13c1 = refl
  holds1350 m13c1 m13c2 m13c0 m13c1 m13c2 = refl
  holds1350 m13c1 m13c2 m13c0 m13c1 m13c3 = refl
  holds1350 m13c1 m13c2 m13c0 m13c2 m13c0 = refl
  holds1350 m13c1 m13c2 m13c0 m13c2 m13c1 = refl
  holds1350 m13c1 m13c2 m13c0 m13c2 m13c2 = refl
  holds1350 m13c1 m13c2 m13c0 m13c2 m13c3 = refl
  holds1350 m13c1 m13c2 m13c0 m13c3 m13c0 = refl
  holds1350 m13c1 m13c2 m13c0 m13c3 m13c1 = refl
  holds1350 m13c1 m13c2 m13c0 m13c3 m13c2 = refl
  holds1350 m13c1 m13c2 m13c0 m13c3 m13c3 = refl
  holds1350 m13c1 m13c2 m13c1 m13c0 m13c0 = refl
  holds1350 m13c1 m13c2 m13c1 m13c0 m13c1 = refl
  holds1350 m13c1 m13c2 m13c1 m13c0 m13c2 = refl
  holds1350 m13c1 m13c2 m13c1 m13c0 m13c3 = refl
  holds1350 m13c1 m13c2 m13c1 m13c1 m13c0 = refl
  holds1350 m13c1 m13c2 m13c1 m13c1 m13c1 = refl
  holds1350 m13c1 m13c2 m13c1 m13c1 m13c2 = refl
  holds1350 m13c1 m13c2 m13c1 m13c1 m13c3 = refl
  holds1350 m13c1 m13c2 m13c1 m13c2 m13c0 = refl
  holds1350 m13c1 m13c2 m13c1 m13c2 m13c1 = refl
  holds1350 m13c1 m13c2 m13c1 m13c2 m13c2 = refl
  holds1350 m13c1 m13c2 m13c1 m13c2 m13c3 = refl
  holds1350 m13c1 m13c2 m13c1 m13c3 m13c0 = refl
  holds1350 m13c1 m13c2 m13c1 m13c3 m13c1 = refl
  holds1350 m13c1 m13c2 m13c1 m13c3 m13c2 = refl
  holds1350 m13c1 m13c2 m13c1 m13c3 m13c3 = refl
  holds1350 m13c1 m13c2 m13c2 m13c0 m13c0 = refl
  holds1350 m13c1 m13c2 m13c2 m13c0 m13c1 = refl
  holds1350 m13c1 m13c2 m13c2 m13c0 m13c2 = refl
  holds1350 m13c1 m13c2 m13c2 m13c0 m13c3 = refl
  holds1350 m13c1 m13c2 m13c2 m13c1 m13c0 = refl
  holds1350 m13c1 m13c2 m13c2 m13c1 m13c1 = refl
  holds1350 m13c1 m13c2 m13c2 m13c1 m13c2 = refl
  holds1350 m13c1 m13c2 m13c2 m13c1 m13c3 = refl
  holds1350 m13c1 m13c2 m13c2 m13c2 m13c0 = refl
  holds1350 m13c1 m13c2 m13c2 m13c2 m13c1 = refl
  holds1350 m13c1 m13c2 m13c2 m13c2 m13c2 = refl
  holds1350 m13c1 m13c2 m13c2 m13c2 m13c3 = refl
  holds1350 m13c1 m13c2 m13c2 m13c3 m13c0 = refl
  holds1350 m13c1 m13c2 m13c2 m13c3 m13c1 = refl
  holds1350 m13c1 m13c2 m13c2 m13c3 m13c2 = refl
  holds1350 m13c1 m13c2 m13c2 m13c3 m13c3 = refl
  holds1350 m13c1 m13c2 m13c3 m13c0 m13c0 = refl
  holds1350 m13c1 m13c2 m13c3 m13c0 m13c1 = refl
  holds1350 m13c1 m13c2 m13c3 m13c0 m13c2 = refl
  holds1350 m13c1 m13c2 m13c3 m13c0 m13c3 = refl
  holds1350 m13c1 m13c2 m13c3 m13c1 m13c0 = refl
  holds1350 m13c1 m13c2 m13c3 m13c1 m13c1 = refl
  holds1350 m13c1 m13c2 m13c3 m13c1 m13c2 = refl
  holds1350 m13c1 m13c2 m13c3 m13c1 m13c3 = refl
  holds1350 m13c1 m13c2 m13c3 m13c2 m13c0 = refl
  holds1350 m13c1 m13c2 m13c3 m13c2 m13c1 = refl
  holds1350 m13c1 m13c2 m13c3 m13c2 m13c2 = refl
  holds1350 m13c1 m13c2 m13c3 m13c2 m13c3 = refl
  holds1350 m13c1 m13c2 m13c3 m13c3 m13c0 = refl
  holds1350 m13c1 m13c2 m13c3 m13c3 m13c1 = refl
  holds1350 m13c1 m13c2 m13c3 m13c3 m13c2 = refl
  holds1350 m13c1 m13c2 m13c3 m13c3 m13c3 = refl
  holds1350 m13c1 m13c3 m13c0 m13c0 m13c0 = refl
  holds1350 m13c1 m13c3 m13c0 m13c0 m13c1 = refl
  holds1350 m13c1 m13c3 m13c0 m13c0 m13c2 = refl
  holds1350 m13c1 m13c3 m13c0 m13c0 m13c3 = refl
  holds1350 m13c1 m13c3 m13c0 m13c1 m13c0 = refl
  holds1350 m13c1 m13c3 m13c0 m13c1 m13c1 = refl
  holds1350 m13c1 m13c3 m13c0 m13c1 m13c2 = refl
  holds1350 m13c1 m13c3 m13c0 m13c1 m13c3 = refl
  holds1350 m13c1 m13c3 m13c0 m13c2 m13c0 = refl
  holds1350 m13c1 m13c3 m13c0 m13c2 m13c1 = refl
  holds1350 m13c1 m13c3 m13c0 m13c2 m13c2 = refl
  holds1350 m13c1 m13c3 m13c0 m13c2 m13c3 = refl
  holds1350 m13c1 m13c3 m13c0 m13c3 m13c0 = refl
  holds1350 m13c1 m13c3 m13c0 m13c3 m13c1 = refl
  holds1350 m13c1 m13c3 m13c0 m13c3 m13c2 = refl
  holds1350 m13c1 m13c3 m13c0 m13c3 m13c3 = refl
  holds1350 m13c1 m13c3 m13c1 m13c0 m13c0 = refl
  holds1350 m13c1 m13c3 m13c1 m13c0 m13c1 = refl
  holds1350 m13c1 m13c3 m13c1 m13c0 m13c2 = refl
  holds1350 m13c1 m13c3 m13c1 m13c0 m13c3 = refl
  holds1350 m13c1 m13c3 m13c1 m13c1 m13c0 = refl
  holds1350 m13c1 m13c3 m13c1 m13c1 m13c1 = refl
  holds1350 m13c1 m13c3 m13c1 m13c1 m13c2 = refl
  holds1350 m13c1 m13c3 m13c1 m13c1 m13c3 = refl
  holds1350 m13c1 m13c3 m13c1 m13c2 m13c0 = refl
  holds1350 m13c1 m13c3 m13c1 m13c2 m13c1 = refl
  holds1350 m13c1 m13c3 m13c1 m13c2 m13c2 = refl
  holds1350 m13c1 m13c3 m13c1 m13c2 m13c3 = refl
  holds1350 m13c1 m13c3 m13c1 m13c3 m13c0 = refl
  holds1350 m13c1 m13c3 m13c1 m13c3 m13c1 = refl
  holds1350 m13c1 m13c3 m13c1 m13c3 m13c2 = refl
  holds1350 m13c1 m13c3 m13c1 m13c3 m13c3 = refl
  holds1350 m13c1 m13c3 m13c2 m13c0 m13c0 = refl
  holds1350 m13c1 m13c3 m13c2 m13c0 m13c1 = refl
  holds1350 m13c1 m13c3 m13c2 m13c0 m13c2 = refl
  holds1350 m13c1 m13c3 m13c2 m13c0 m13c3 = refl
  holds1350 m13c1 m13c3 m13c2 m13c1 m13c0 = refl
  holds1350 m13c1 m13c3 m13c2 m13c1 m13c1 = refl
  holds1350 m13c1 m13c3 m13c2 m13c1 m13c2 = refl
  holds1350 m13c1 m13c3 m13c2 m13c1 m13c3 = refl
  holds1350 m13c1 m13c3 m13c2 m13c2 m13c0 = refl
  holds1350 m13c1 m13c3 m13c2 m13c2 m13c1 = refl
  holds1350 m13c1 m13c3 m13c2 m13c2 m13c2 = refl
  holds1350 m13c1 m13c3 m13c2 m13c2 m13c3 = refl
  holds1350 m13c1 m13c3 m13c2 m13c3 m13c0 = refl
  holds1350 m13c1 m13c3 m13c2 m13c3 m13c1 = refl
  holds1350 m13c1 m13c3 m13c2 m13c3 m13c2 = refl
  holds1350 m13c1 m13c3 m13c2 m13c3 m13c3 = refl
  holds1350 m13c1 m13c3 m13c3 m13c0 m13c0 = refl
  holds1350 m13c1 m13c3 m13c3 m13c0 m13c1 = refl
  holds1350 m13c1 m13c3 m13c3 m13c0 m13c2 = refl
  holds1350 m13c1 m13c3 m13c3 m13c0 m13c3 = refl
  holds1350 m13c1 m13c3 m13c3 m13c1 m13c0 = refl
  holds1350 m13c1 m13c3 m13c3 m13c1 m13c1 = refl
  holds1350 m13c1 m13c3 m13c3 m13c1 m13c2 = refl
  holds1350 m13c1 m13c3 m13c3 m13c1 m13c3 = refl
  holds1350 m13c1 m13c3 m13c3 m13c2 m13c0 = refl
  holds1350 m13c1 m13c3 m13c3 m13c2 m13c1 = refl
  holds1350 m13c1 m13c3 m13c3 m13c2 m13c2 = refl
  holds1350 m13c1 m13c3 m13c3 m13c2 m13c3 = refl
  holds1350 m13c1 m13c3 m13c3 m13c3 m13c0 = refl
  holds1350 m13c1 m13c3 m13c3 m13c3 m13c1 = refl
  holds1350 m13c1 m13c3 m13c3 m13c3 m13c2 = refl
  holds1350 m13c1 m13c3 m13c3 m13c3 m13c3 = refl
  holds1350 m13c2 m13c0 m13c0 m13c0 m13c0 = refl
  holds1350 m13c2 m13c0 m13c0 m13c0 m13c1 = refl
  holds1350 m13c2 m13c0 m13c0 m13c0 m13c2 = refl
  holds1350 m13c2 m13c0 m13c0 m13c0 m13c3 = refl
  holds1350 m13c2 m13c0 m13c0 m13c1 m13c0 = refl
  holds1350 m13c2 m13c0 m13c0 m13c1 m13c1 = refl
  holds1350 m13c2 m13c0 m13c0 m13c1 m13c2 = refl
  holds1350 m13c2 m13c0 m13c0 m13c1 m13c3 = refl
  holds1350 m13c2 m13c0 m13c0 m13c2 m13c0 = refl
  holds1350 m13c2 m13c0 m13c0 m13c2 m13c1 = refl
  holds1350 m13c2 m13c0 m13c0 m13c2 m13c2 = refl
  holds1350 m13c2 m13c0 m13c0 m13c2 m13c3 = refl
  holds1350 m13c2 m13c0 m13c0 m13c3 m13c0 = refl
  holds1350 m13c2 m13c0 m13c0 m13c3 m13c1 = refl
  holds1350 m13c2 m13c0 m13c0 m13c3 m13c2 = refl
  holds1350 m13c2 m13c0 m13c0 m13c3 m13c3 = refl
  holds1350 m13c2 m13c0 m13c1 m13c0 m13c0 = refl
  holds1350 m13c2 m13c0 m13c1 m13c0 m13c1 = refl
  holds1350 m13c2 m13c0 m13c1 m13c0 m13c2 = refl
  holds1350 m13c2 m13c0 m13c1 m13c0 m13c3 = refl
  holds1350 m13c2 m13c0 m13c1 m13c1 m13c0 = refl
  holds1350 m13c2 m13c0 m13c1 m13c1 m13c1 = refl
  holds1350 m13c2 m13c0 m13c1 m13c1 m13c2 = refl
  holds1350 m13c2 m13c0 m13c1 m13c1 m13c3 = refl
  holds1350 m13c2 m13c0 m13c1 m13c2 m13c0 = refl
  holds1350 m13c2 m13c0 m13c1 m13c2 m13c1 = refl
  holds1350 m13c2 m13c0 m13c1 m13c2 m13c2 = refl
  holds1350 m13c2 m13c0 m13c1 m13c2 m13c3 = refl
  holds1350 m13c2 m13c0 m13c1 m13c3 m13c0 = refl
  holds1350 m13c2 m13c0 m13c1 m13c3 m13c1 = refl
  holds1350 m13c2 m13c0 m13c1 m13c3 m13c2 = refl
  holds1350 m13c2 m13c0 m13c1 m13c3 m13c3 = refl
  holds1350 m13c2 m13c0 m13c2 m13c0 m13c0 = refl
  holds1350 m13c2 m13c0 m13c2 m13c0 m13c1 = refl
  holds1350 m13c2 m13c0 m13c2 m13c0 m13c2 = refl
  holds1350 m13c2 m13c0 m13c2 m13c0 m13c3 = refl
  holds1350 m13c2 m13c0 m13c2 m13c1 m13c0 = refl
  holds1350 m13c2 m13c0 m13c2 m13c1 m13c1 = refl
  holds1350 m13c2 m13c0 m13c2 m13c1 m13c2 = refl
  holds1350 m13c2 m13c0 m13c2 m13c1 m13c3 = refl
  holds1350 m13c2 m13c0 m13c2 m13c2 m13c0 = refl
  holds1350 m13c2 m13c0 m13c2 m13c2 m13c1 = refl
  holds1350 m13c2 m13c0 m13c2 m13c2 m13c2 = refl
  holds1350 m13c2 m13c0 m13c2 m13c2 m13c3 = refl
  holds1350 m13c2 m13c0 m13c2 m13c3 m13c0 = refl
  holds1350 m13c2 m13c0 m13c2 m13c3 m13c1 = refl
  holds1350 m13c2 m13c0 m13c2 m13c3 m13c2 = refl
  holds1350 m13c2 m13c0 m13c2 m13c3 m13c3 = refl
  holds1350 m13c2 m13c0 m13c3 m13c0 m13c0 = refl
  holds1350 m13c2 m13c0 m13c3 m13c0 m13c1 = refl
  holds1350 m13c2 m13c0 m13c3 m13c0 m13c2 = refl
  holds1350 m13c2 m13c0 m13c3 m13c0 m13c3 = refl
  holds1350 m13c2 m13c0 m13c3 m13c1 m13c0 = refl
  holds1350 m13c2 m13c0 m13c3 m13c1 m13c1 = refl
  holds1350 m13c2 m13c0 m13c3 m13c1 m13c2 = refl
  holds1350 m13c2 m13c0 m13c3 m13c1 m13c3 = refl
  holds1350 m13c2 m13c0 m13c3 m13c2 m13c0 = refl
  holds1350 m13c2 m13c0 m13c3 m13c2 m13c1 = refl
  holds1350 m13c2 m13c0 m13c3 m13c2 m13c2 = refl
  holds1350 m13c2 m13c0 m13c3 m13c2 m13c3 = refl
  holds1350 m13c2 m13c0 m13c3 m13c3 m13c0 = refl
  holds1350 m13c2 m13c0 m13c3 m13c3 m13c1 = refl
  holds1350 m13c2 m13c0 m13c3 m13c3 m13c2 = refl
  holds1350 m13c2 m13c0 m13c3 m13c3 m13c3 = refl
  holds1350 m13c2 m13c1 m13c0 m13c0 m13c0 = refl
  holds1350 m13c2 m13c1 m13c0 m13c0 m13c1 = refl
  holds1350 m13c2 m13c1 m13c0 m13c0 m13c2 = refl
  holds1350 m13c2 m13c1 m13c0 m13c0 m13c3 = refl
  holds1350 m13c2 m13c1 m13c0 m13c1 m13c0 = refl
  holds1350 m13c2 m13c1 m13c0 m13c1 m13c1 = refl
  holds1350 m13c2 m13c1 m13c0 m13c1 m13c2 = refl
  holds1350 m13c2 m13c1 m13c0 m13c1 m13c3 = refl
  holds1350 m13c2 m13c1 m13c0 m13c2 m13c0 = refl
  holds1350 m13c2 m13c1 m13c0 m13c2 m13c1 = refl
  holds1350 m13c2 m13c1 m13c0 m13c2 m13c2 = refl
  holds1350 m13c2 m13c1 m13c0 m13c2 m13c3 = refl
  holds1350 m13c2 m13c1 m13c0 m13c3 m13c0 = refl
  holds1350 m13c2 m13c1 m13c0 m13c3 m13c1 = refl
  holds1350 m13c2 m13c1 m13c0 m13c3 m13c2 = refl
  holds1350 m13c2 m13c1 m13c0 m13c3 m13c3 = refl
  holds1350 m13c2 m13c1 m13c1 m13c0 m13c0 = refl
  holds1350 m13c2 m13c1 m13c1 m13c0 m13c1 = refl
  holds1350 m13c2 m13c1 m13c1 m13c0 m13c2 = refl
  holds1350 m13c2 m13c1 m13c1 m13c0 m13c3 = refl
  holds1350 m13c2 m13c1 m13c1 m13c1 m13c0 = refl
  holds1350 m13c2 m13c1 m13c1 m13c1 m13c1 = refl
  holds1350 m13c2 m13c1 m13c1 m13c1 m13c2 = refl
  holds1350 m13c2 m13c1 m13c1 m13c1 m13c3 = refl
  holds1350 m13c2 m13c1 m13c1 m13c2 m13c0 = refl
  holds1350 m13c2 m13c1 m13c1 m13c2 m13c1 = refl
  holds1350 m13c2 m13c1 m13c1 m13c2 m13c2 = refl
  holds1350 m13c2 m13c1 m13c1 m13c2 m13c3 = refl
  holds1350 m13c2 m13c1 m13c1 m13c3 m13c0 = refl
  holds1350 m13c2 m13c1 m13c1 m13c3 m13c1 = refl
  holds1350 m13c2 m13c1 m13c1 m13c3 m13c2 = refl
  holds1350 m13c2 m13c1 m13c1 m13c3 m13c3 = refl
  holds1350 m13c2 m13c1 m13c2 m13c0 m13c0 = refl
  holds1350 m13c2 m13c1 m13c2 m13c0 m13c1 = refl
  holds1350 m13c2 m13c1 m13c2 m13c0 m13c2 = refl
  holds1350 m13c2 m13c1 m13c2 m13c0 m13c3 = refl
  holds1350 m13c2 m13c1 m13c2 m13c1 m13c0 = refl
  holds1350 m13c2 m13c1 m13c2 m13c1 m13c1 = refl
  holds1350 m13c2 m13c1 m13c2 m13c1 m13c2 = refl
  holds1350 m13c2 m13c1 m13c2 m13c1 m13c3 = refl
  holds1350 m13c2 m13c1 m13c2 m13c2 m13c0 = refl
  holds1350 m13c2 m13c1 m13c2 m13c2 m13c1 = refl
  holds1350 m13c2 m13c1 m13c2 m13c2 m13c2 = refl
  holds1350 m13c2 m13c1 m13c2 m13c2 m13c3 = refl
  holds1350 m13c2 m13c1 m13c2 m13c3 m13c0 = refl
  holds1350 m13c2 m13c1 m13c2 m13c3 m13c1 = refl
  holds1350 m13c2 m13c1 m13c2 m13c3 m13c2 = refl
  holds1350 m13c2 m13c1 m13c2 m13c3 m13c3 = refl
  holds1350 m13c2 m13c1 m13c3 m13c0 m13c0 = refl
  holds1350 m13c2 m13c1 m13c3 m13c0 m13c1 = refl
  holds1350 m13c2 m13c1 m13c3 m13c0 m13c2 = refl
  holds1350 m13c2 m13c1 m13c3 m13c0 m13c3 = refl
  holds1350 m13c2 m13c1 m13c3 m13c1 m13c0 = refl
  holds1350 m13c2 m13c1 m13c3 m13c1 m13c1 = refl
  holds1350 m13c2 m13c1 m13c3 m13c1 m13c2 = refl
  holds1350 m13c2 m13c1 m13c3 m13c1 m13c3 = refl
  holds1350 m13c2 m13c1 m13c3 m13c2 m13c0 = refl
  holds1350 m13c2 m13c1 m13c3 m13c2 m13c1 = refl
  holds1350 m13c2 m13c1 m13c3 m13c2 m13c2 = refl
  holds1350 m13c2 m13c1 m13c3 m13c2 m13c3 = refl
  holds1350 m13c2 m13c1 m13c3 m13c3 m13c0 = refl
  holds1350 m13c2 m13c1 m13c3 m13c3 m13c1 = refl
  holds1350 m13c2 m13c1 m13c3 m13c3 m13c2 = refl
  holds1350 m13c2 m13c1 m13c3 m13c3 m13c3 = refl
  holds1350 m13c2 m13c2 m13c0 m13c0 m13c0 = refl
  holds1350 m13c2 m13c2 m13c0 m13c0 m13c1 = refl
  holds1350 m13c2 m13c2 m13c0 m13c0 m13c2 = refl
  holds1350 m13c2 m13c2 m13c0 m13c0 m13c3 = refl
  holds1350 m13c2 m13c2 m13c0 m13c1 m13c0 = refl
  holds1350 m13c2 m13c2 m13c0 m13c1 m13c1 = refl
  holds1350 m13c2 m13c2 m13c0 m13c1 m13c2 = refl
  holds1350 m13c2 m13c2 m13c0 m13c1 m13c3 = refl
  holds1350 m13c2 m13c2 m13c0 m13c2 m13c0 = refl
  holds1350 m13c2 m13c2 m13c0 m13c2 m13c1 = refl
  holds1350 m13c2 m13c2 m13c0 m13c2 m13c2 = refl
  holds1350 m13c2 m13c2 m13c0 m13c2 m13c3 = refl
  holds1350 m13c2 m13c2 m13c0 m13c3 m13c0 = refl
  holds1350 m13c2 m13c2 m13c0 m13c3 m13c1 = refl
  holds1350 m13c2 m13c2 m13c0 m13c3 m13c2 = refl
  holds1350 m13c2 m13c2 m13c0 m13c3 m13c3 = refl
  holds1350 m13c2 m13c2 m13c1 m13c0 m13c0 = refl
  holds1350 m13c2 m13c2 m13c1 m13c0 m13c1 = refl
  holds1350 m13c2 m13c2 m13c1 m13c0 m13c2 = refl
  holds1350 m13c2 m13c2 m13c1 m13c0 m13c3 = refl
  holds1350 m13c2 m13c2 m13c1 m13c1 m13c0 = refl
  holds1350 m13c2 m13c2 m13c1 m13c1 m13c1 = refl
  holds1350 m13c2 m13c2 m13c1 m13c1 m13c2 = refl
  holds1350 m13c2 m13c2 m13c1 m13c1 m13c3 = refl
  holds1350 m13c2 m13c2 m13c1 m13c2 m13c0 = refl
  holds1350 m13c2 m13c2 m13c1 m13c2 m13c1 = refl
  holds1350 m13c2 m13c2 m13c1 m13c2 m13c2 = refl
  holds1350 m13c2 m13c2 m13c1 m13c2 m13c3 = refl
  holds1350 m13c2 m13c2 m13c1 m13c3 m13c0 = refl
  holds1350 m13c2 m13c2 m13c1 m13c3 m13c1 = refl
  holds1350 m13c2 m13c2 m13c1 m13c3 m13c2 = refl
  holds1350 m13c2 m13c2 m13c1 m13c3 m13c3 = refl
  holds1350 m13c2 m13c2 m13c2 m13c0 m13c0 = refl
  holds1350 m13c2 m13c2 m13c2 m13c0 m13c1 = refl
  holds1350 m13c2 m13c2 m13c2 m13c0 m13c2 = refl
  holds1350 m13c2 m13c2 m13c2 m13c0 m13c3 = refl
  holds1350 m13c2 m13c2 m13c2 m13c1 m13c0 = refl
  holds1350 m13c2 m13c2 m13c2 m13c1 m13c1 = refl
  holds1350 m13c2 m13c2 m13c2 m13c1 m13c2 = refl
  holds1350 m13c2 m13c2 m13c2 m13c1 m13c3 = refl
  holds1350 m13c2 m13c2 m13c2 m13c2 m13c0 = refl
  holds1350 m13c2 m13c2 m13c2 m13c2 m13c1 = refl
  holds1350 m13c2 m13c2 m13c2 m13c2 m13c2 = refl
  holds1350 m13c2 m13c2 m13c2 m13c2 m13c3 = refl
  holds1350 m13c2 m13c2 m13c2 m13c3 m13c0 = refl
  holds1350 m13c2 m13c2 m13c2 m13c3 m13c1 = refl
  holds1350 m13c2 m13c2 m13c2 m13c3 m13c2 = refl
  holds1350 m13c2 m13c2 m13c2 m13c3 m13c3 = refl
  holds1350 m13c2 m13c2 m13c3 m13c0 m13c0 = refl
  holds1350 m13c2 m13c2 m13c3 m13c0 m13c1 = refl
  holds1350 m13c2 m13c2 m13c3 m13c0 m13c2 = refl
  holds1350 m13c2 m13c2 m13c3 m13c0 m13c3 = refl
  holds1350 m13c2 m13c2 m13c3 m13c1 m13c0 = refl
  holds1350 m13c2 m13c2 m13c3 m13c1 m13c1 = refl
  holds1350 m13c2 m13c2 m13c3 m13c1 m13c2 = refl
  holds1350 m13c2 m13c2 m13c3 m13c1 m13c3 = refl
  holds1350 m13c2 m13c2 m13c3 m13c2 m13c0 = refl
  holds1350 m13c2 m13c2 m13c3 m13c2 m13c1 = refl
  holds1350 m13c2 m13c2 m13c3 m13c2 m13c2 = refl
  holds1350 m13c2 m13c2 m13c3 m13c2 m13c3 = refl
  holds1350 m13c2 m13c2 m13c3 m13c3 m13c0 = refl
  holds1350 m13c2 m13c2 m13c3 m13c3 m13c1 = refl
  holds1350 m13c2 m13c2 m13c3 m13c3 m13c2 = refl
  holds1350 m13c2 m13c2 m13c3 m13c3 m13c3 = refl
  holds1350 m13c2 m13c3 m13c0 m13c0 m13c0 = refl
  holds1350 m13c2 m13c3 m13c0 m13c0 m13c1 = refl
  holds1350 m13c2 m13c3 m13c0 m13c0 m13c2 = refl
  holds1350 m13c2 m13c3 m13c0 m13c0 m13c3 = refl
  holds1350 m13c2 m13c3 m13c0 m13c1 m13c0 = refl
  holds1350 m13c2 m13c3 m13c0 m13c1 m13c1 = refl
  holds1350 m13c2 m13c3 m13c0 m13c1 m13c2 = refl
  holds1350 m13c2 m13c3 m13c0 m13c1 m13c3 = refl
  holds1350 m13c2 m13c3 m13c0 m13c2 m13c0 = refl
  holds1350 m13c2 m13c3 m13c0 m13c2 m13c1 = refl
  holds1350 m13c2 m13c3 m13c0 m13c2 m13c2 = refl
  holds1350 m13c2 m13c3 m13c0 m13c2 m13c3 = refl
  holds1350 m13c2 m13c3 m13c0 m13c3 m13c0 = refl
  holds1350 m13c2 m13c3 m13c0 m13c3 m13c1 = refl
  holds1350 m13c2 m13c3 m13c0 m13c3 m13c2 = refl
  holds1350 m13c2 m13c3 m13c0 m13c3 m13c3 = refl
  holds1350 m13c2 m13c3 m13c1 m13c0 m13c0 = refl
  holds1350 m13c2 m13c3 m13c1 m13c0 m13c1 = refl
  holds1350 m13c2 m13c3 m13c1 m13c0 m13c2 = refl
  holds1350 m13c2 m13c3 m13c1 m13c0 m13c3 = refl
  holds1350 m13c2 m13c3 m13c1 m13c1 m13c0 = refl
  holds1350 m13c2 m13c3 m13c1 m13c1 m13c1 = refl
  holds1350 m13c2 m13c3 m13c1 m13c1 m13c2 = refl
  holds1350 m13c2 m13c3 m13c1 m13c1 m13c3 = refl
  holds1350 m13c2 m13c3 m13c1 m13c2 m13c0 = refl
  holds1350 m13c2 m13c3 m13c1 m13c2 m13c1 = refl
  holds1350 m13c2 m13c3 m13c1 m13c2 m13c2 = refl
  holds1350 m13c2 m13c3 m13c1 m13c2 m13c3 = refl
  holds1350 m13c2 m13c3 m13c1 m13c3 m13c0 = refl
  holds1350 m13c2 m13c3 m13c1 m13c3 m13c1 = refl
  holds1350 m13c2 m13c3 m13c1 m13c3 m13c2 = refl
  holds1350 m13c2 m13c3 m13c1 m13c3 m13c3 = refl
  holds1350 m13c2 m13c3 m13c2 m13c0 m13c0 = refl
  holds1350 m13c2 m13c3 m13c2 m13c0 m13c1 = refl
  holds1350 m13c2 m13c3 m13c2 m13c0 m13c2 = refl
  holds1350 m13c2 m13c3 m13c2 m13c0 m13c3 = refl
  holds1350 m13c2 m13c3 m13c2 m13c1 m13c0 = refl
  holds1350 m13c2 m13c3 m13c2 m13c1 m13c1 = refl
  holds1350 m13c2 m13c3 m13c2 m13c1 m13c2 = refl
  holds1350 m13c2 m13c3 m13c2 m13c1 m13c3 = refl
  holds1350 m13c2 m13c3 m13c2 m13c2 m13c0 = refl
  holds1350 m13c2 m13c3 m13c2 m13c2 m13c1 = refl
  holds1350 m13c2 m13c3 m13c2 m13c2 m13c2 = refl
  holds1350 m13c2 m13c3 m13c2 m13c2 m13c3 = refl
  holds1350 m13c2 m13c3 m13c2 m13c3 m13c0 = refl
  holds1350 m13c2 m13c3 m13c2 m13c3 m13c1 = refl
  holds1350 m13c2 m13c3 m13c2 m13c3 m13c2 = refl
  holds1350 m13c2 m13c3 m13c2 m13c3 m13c3 = refl
  holds1350 m13c2 m13c3 m13c3 m13c0 m13c0 = refl
  holds1350 m13c2 m13c3 m13c3 m13c0 m13c1 = refl
  holds1350 m13c2 m13c3 m13c3 m13c0 m13c2 = refl
  holds1350 m13c2 m13c3 m13c3 m13c0 m13c3 = refl
  holds1350 m13c2 m13c3 m13c3 m13c1 m13c0 = refl
  holds1350 m13c2 m13c3 m13c3 m13c1 m13c1 = refl
  holds1350 m13c2 m13c3 m13c3 m13c1 m13c2 = refl
  holds1350 m13c2 m13c3 m13c3 m13c1 m13c3 = refl
  holds1350 m13c2 m13c3 m13c3 m13c2 m13c0 = refl
  holds1350 m13c2 m13c3 m13c3 m13c2 m13c1 = refl
  holds1350 m13c2 m13c3 m13c3 m13c2 m13c2 = refl
  holds1350 m13c2 m13c3 m13c3 m13c2 m13c3 = refl
  holds1350 m13c2 m13c3 m13c3 m13c3 m13c0 = refl
  holds1350 m13c2 m13c3 m13c3 m13c3 m13c1 = refl
  holds1350 m13c2 m13c3 m13c3 m13c3 m13c2 = refl
  holds1350 m13c2 m13c3 m13c3 m13c3 m13c3 = refl
  holds1350 m13c3 m13c0 m13c0 m13c0 m13c0 = refl
  holds1350 m13c3 m13c0 m13c0 m13c0 m13c1 = refl
  holds1350 m13c3 m13c0 m13c0 m13c0 m13c2 = refl
  holds1350 m13c3 m13c0 m13c0 m13c0 m13c3 = refl
  holds1350 m13c3 m13c0 m13c0 m13c1 m13c0 = refl
  holds1350 m13c3 m13c0 m13c0 m13c1 m13c1 = refl
  holds1350 m13c3 m13c0 m13c0 m13c1 m13c2 = refl
  holds1350 m13c3 m13c0 m13c0 m13c1 m13c3 = refl
  holds1350 m13c3 m13c0 m13c0 m13c2 m13c0 = refl
  holds1350 m13c3 m13c0 m13c0 m13c2 m13c1 = refl
  holds1350 m13c3 m13c0 m13c0 m13c2 m13c2 = refl
  holds1350 m13c3 m13c0 m13c0 m13c2 m13c3 = refl
  holds1350 m13c3 m13c0 m13c0 m13c3 m13c0 = refl
  holds1350 m13c3 m13c0 m13c0 m13c3 m13c1 = refl
  holds1350 m13c3 m13c0 m13c0 m13c3 m13c2 = refl
  holds1350 m13c3 m13c0 m13c0 m13c3 m13c3 = refl
  holds1350 m13c3 m13c0 m13c1 m13c0 m13c0 = refl
  holds1350 m13c3 m13c0 m13c1 m13c0 m13c1 = refl
  holds1350 m13c3 m13c0 m13c1 m13c0 m13c2 = refl
  holds1350 m13c3 m13c0 m13c1 m13c0 m13c3 = refl
  holds1350 m13c3 m13c0 m13c1 m13c1 m13c0 = refl
  holds1350 m13c3 m13c0 m13c1 m13c1 m13c1 = refl
  holds1350 m13c3 m13c0 m13c1 m13c1 m13c2 = refl
  holds1350 m13c3 m13c0 m13c1 m13c1 m13c3 = refl
  holds1350 m13c3 m13c0 m13c1 m13c2 m13c0 = refl
  holds1350 m13c3 m13c0 m13c1 m13c2 m13c1 = refl
  holds1350 m13c3 m13c0 m13c1 m13c2 m13c2 = refl
  holds1350 m13c3 m13c0 m13c1 m13c2 m13c3 = refl
  holds1350 m13c3 m13c0 m13c1 m13c3 m13c0 = refl
  holds1350 m13c3 m13c0 m13c1 m13c3 m13c1 = refl
  holds1350 m13c3 m13c0 m13c1 m13c3 m13c2 = refl
  holds1350 m13c3 m13c0 m13c1 m13c3 m13c3 = refl
  holds1350 m13c3 m13c0 m13c2 m13c0 m13c0 = refl
  holds1350 m13c3 m13c0 m13c2 m13c0 m13c1 = refl
  holds1350 m13c3 m13c0 m13c2 m13c0 m13c2 = refl
  holds1350 m13c3 m13c0 m13c2 m13c0 m13c3 = refl
  holds1350 m13c3 m13c0 m13c2 m13c1 m13c0 = refl
  holds1350 m13c3 m13c0 m13c2 m13c1 m13c1 = refl
  holds1350 m13c3 m13c0 m13c2 m13c1 m13c2 = refl
  holds1350 m13c3 m13c0 m13c2 m13c1 m13c3 = refl
  holds1350 m13c3 m13c0 m13c2 m13c2 m13c0 = refl
  holds1350 m13c3 m13c0 m13c2 m13c2 m13c1 = refl
  holds1350 m13c3 m13c0 m13c2 m13c2 m13c2 = refl
  holds1350 m13c3 m13c0 m13c2 m13c2 m13c3 = refl
  holds1350 m13c3 m13c0 m13c2 m13c3 m13c0 = refl
  holds1350 m13c3 m13c0 m13c2 m13c3 m13c1 = refl
  holds1350 m13c3 m13c0 m13c2 m13c3 m13c2 = refl
  holds1350 m13c3 m13c0 m13c2 m13c3 m13c3 = refl
  holds1350 m13c3 m13c0 m13c3 m13c0 m13c0 = refl
  holds1350 m13c3 m13c0 m13c3 m13c0 m13c1 = refl
  holds1350 m13c3 m13c0 m13c3 m13c0 m13c2 = refl
  holds1350 m13c3 m13c0 m13c3 m13c0 m13c3 = refl
  holds1350 m13c3 m13c0 m13c3 m13c1 m13c0 = refl
  holds1350 m13c3 m13c0 m13c3 m13c1 m13c1 = refl
  holds1350 m13c3 m13c0 m13c3 m13c1 m13c2 = refl
  holds1350 m13c3 m13c0 m13c3 m13c1 m13c3 = refl
  holds1350 m13c3 m13c0 m13c3 m13c2 m13c0 = refl
  holds1350 m13c3 m13c0 m13c3 m13c2 m13c1 = refl
  holds1350 m13c3 m13c0 m13c3 m13c2 m13c2 = refl
  holds1350 m13c3 m13c0 m13c3 m13c2 m13c3 = refl
  holds1350 m13c3 m13c0 m13c3 m13c3 m13c0 = refl
  holds1350 m13c3 m13c0 m13c3 m13c3 m13c1 = refl
  holds1350 m13c3 m13c0 m13c3 m13c3 m13c2 = refl
  holds1350 m13c3 m13c0 m13c3 m13c3 m13c3 = refl
  holds1350 m13c3 m13c1 m13c0 m13c0 m13c0 = refl
  holds1350 m13c3 m13c1 m13c0 m13c0 m13c1 = refl
  holds1350 m13c3 m13c1 m13c0 m13c0 m13c2 = refl
  holds1350 m13c3 m13c1 m13c0 m13c0 m13c3 = refl
  holds1350 m13c3 m13c1 m13c0 m13c1 m13c0 = refl
  holds1350 m13c3 m13c1 m13c0 m13c1 m13c1 = refl
  holds1350 m13c3 m13c1 m13c0 m13c1 m13c2 = refl
  holds1350 m13c3 m13c1 m13c0 m13c1 m13c3 = refl
  holds1350 m13c3 m13c1 m13c0 m13c2 m13c0 = refl
  holds1350 m13c3 m13c1 m13c0 m13c2 m13c1 = refl
  holds1350 m13c3 m13c1 m13c0 m13c2 m13c2 = refl
  holds1350 m13c3 m13c1 m13c0 m13c2 m13c3 = refl
  holds1350 m13c3 m13c1 m13c0 m13c3 m13c0 = refl
  holds1350 m13c3 m13c1 m13c0 m13c3 m13c1 = refl
  holds1350 m13c3 m13c1 m13c0 m13c3 m13c2 = refl
  holds1350 m13c3 m13c1 m13c0 m13c3 m13c3 = refl
  holds1350 m13c3 m13c1 m13c1 m13c0 m13c0 = refl
  holds1350 m13c3 m13c1 m13c1 m13c0 m13c1 = refl
  holds1350 m13c3 m13c1 m13c1 m13c0 m13c2 = refl
  holds1350 m13c3 m13c1 m13c1 m13c0 m13c3 = refl
  holds1350 m13c3 m13c1 m13c1 m13c1 m13c0 = refl
  holds1350 m13c3 m13c1 m13c1 m13c1 m13c1 = refl
  holds1350 m13c3 m13c1 m13c1 m13c1 m13c2 = refl
  holds1350 m13c3 m13c1 m13c1 m13c1 m13c3 = refl
  holds1350 m13c3 m13c1 m13c1 m13c2 m13c0 = refl
  holds1350 m13c3 m13c1 m13c1 m13c2 m13c1 = refl
  holds1350 m13c3 m13c1 m13c1 m13c2 m13c2 = refl
  holds1350 m13c3 m13c1 m13c1 m13c2 m13c3 = refl
  holds1350 m13c3 m13c1 m13c1 m13c3 m13c0 = refl
  holds1350 m13c3 m13c1 m13c1 m13c3 m13c1 = refl
  holds1350 m13c3 m13c1 m13c1 m13c3 m13c2 = refl
  holds1350 m13c3 m13c1 m13c1 m13c3 m13c3 = refl
  holds1350 m13c3 m13c1 m13c2 m13c0 m13c0 = refl
  holds1350 m13c3 m13c1 m13c2 m13c0 m13c1 = refl
  holds1350 m13c3 m13c1 m13c2 m13c0 m13c2 = refl
  holds1350 m13c3 m13c1 m13c2 m13c0 m13c3 = refl
  holds1350 m13c3 m13c1 m13c2 m13c1 m13c0 = refl
  holds1350 m13c3 m13c1 m13c2 m13c1 m13c1 = refl
  holds1350 m13c3 m13c1 m13c2 m13c1 m13c2 = refl
  holds1350 m13c3 m13c1 m13c2 m13c1 m13c3 = refl
  holds1350 m13c3 m13c1 m13c2 m13c2 m13c0 = refl
  holds1350 m13c3 m13c1 m13c2 m13c2 m13c1 = refl
  holds1350 m13c3 m13c1 m13c2 m13c2 m13c2 = refl
  holds1350 m13c3 m13c1 m13c2 m13c2 m13c3 = refl
  holds1350 m13c3 m13c1 m13c2 m13c3 m13c0 = refl
  holds1350 m13c3 m13c1 m13c2 m13c3 m13c1 = refl
  holds1350 m13c3 m13c1 m13c2 m13c3 m13c2 = refl
  holds1350 m13c3 m13c1 m13c2 m13c3 m13c3 = refl
  holds1350 m13c3 m13c1 m13c3 m13c0 m13c0 = refl
  holds1350 m13c3 m13c1 m13c3 m13c0 m13c1 = refl
  holds1350 m13c3 m13c1 m13c3 m13c0 m13c2 = refl
  holds1350 m13c3 m13c1 m13c3 m13c0 m13c3 = refl
  holds1350 m13c3 m13c1 m13c3 m13c1 m13c0 = refl
  holds1350 m13c3 m13c1 m13c3 m13c1 m13c1 = refl
  holds1350 m13c3 m13c1 m13c3 m13c1 m13c2 = refl
  holds1350 m13c3 m13c1 m13c3 m13c1 m13c3 = refl
  holds1350 m13c3 m13c1 m13c3 m13c2 m13c0 = refl
  holds1350 m13c3 m13c1 m13c3 m13c2 m13c1 = refl
  holds1350 m13c3 m13c1 m13c3 m13c2 m13c2 = refl
  holds1350 m13c3 m13c1 m13c3 m13c2 m13c3 = refl
  holds1350 m13c3 m13c1 m13c3 m13c3 m13c0 = refl
  holds1350 m13c3 m13c1 m13c3 m13c3 m13c1 = refl
  holds1350 m13c3 m13c1 m13c3 m13c3 m13c2 = refl
  holds1350 m13c3 m13c1 m13c3 m13c3 m13c3 = refl
  holds1350 m13c3 m13c2 m13c0 m13c0 m13c0 = refl
  holds1350 m13c3 m13c2 m13c0 m13c0 m13c1 = refl
  holds1350 m13c3 m13c2 m13c0 m13c0 m13c2 = refl
  holds1350 m13c3 m13c2 m13c0 m13c0 m13c3 = refl
  holds1350 m13c3 m13c2 m13c0 m13c1 m13c0 = refl
  holds1350 m13c3 m13c2 m13c0 m13c1 m13c1 = refl
  holds1350 m13c3 m13c2 m13c0 m13c1 m13c2 = refl
  holds1350 m13c3 m13c2 m13c0 m13c1 m13c3 = refl
  holds1350 m13c3 m13c2 m13c0 m13c2 m13c0 = refl
  holds1350 m13c3 m13c2 m13c0 m13c2 m13c1 = refl
  holds1350 m13c3 m13c2 m13c0 m13c2 m13c2 = refl
  holds1350 m13c3 m13c2 m13c0 m13c2 m13c3 = refl
  holds1350 m13c3 m13c2 m13c0 m13c3 m13c0 = refl
  holds1350 m13c3 m13c2 m13c0 m13c3 m13c1 = refl
  holds1350 m13c3 m13c2 m13c0 m13c3 m13c2 = refl
  holds1350 m13c3 m13c2 m13c0 m13c3 m13c3 = refl
  holds1350 m13c3 m13c2 m13c1 m13c0 m13c0 = refl
  holds1350 m13c3 m13c2 m13c1 m13c0 m13c1 = refl
  holds1350 m13c3 m13c2 m13c1 m13c0 m13c2 = refl
  holds1350 m13c3 m13c2 m13c1 m13c0 m13c3 = refl
  holds1350 m13c3 m13c2 m13c1 m13c1 m13c0 = refl
  holds1350 m13c3 m13c2 m13c1 m13c1 m13c1 = refl
  holds1350 m13c3 m13c2 m13c1 m13c1 m13c2 = refl
  holds1350 m13c3 m13c2 m13c1 m13c1 m13c3 = refl
  holds1350 m13c3 m13c2 m13c1 m13c2 m13c0 = refl
  holds1350 m13c3 m13c2 m13c1 m13c2 m13c1 = refl
  holds1350 m13c3 m13c2 m13c1 m13c2 m13c2 = refl
  holds1350 m13c3 m13c2 m13c1 m13c2 m13c3 = refl
  holds1350 m13c3 m13c2 m13c1 m13c3 m13c0 = refl
  holds1350 m13c3 m13c2 m13c1 m13c3 m13c1 = refl
  holds1350 m13c3 m13c2 m13c1 m13c3 m13c2 = refl
  holds1350 m13c3 m13c2 m13c1 m13c3 m13c3 = refl
  holds1350 m13c3 m13c2 m13c2 m13c0 m13c0 = refl
  holds1350 m13c3 m13c2 m13c2 m13c0 m13c1 = refl
  holds1350 m13c3 m13c2 m13c2 m13c0 m13c2 = refl
  holds1350 m13c3 m13c2 m13c2 m13c0 m13c3 = refl
  holds1350 m13c3 m13c2 m13c2 m13c1 m13c0 = refl
  holds1350 m13c3 m13c2 m13c2 m13c1 m13c1 = refl
  holds1350 m13c3 m13c2 m13c2 m13c1 m13c2 = refl
  holds1350 m13c3 m13c2 m13c2 m13c1 m13c3 = refl
  holds1350 m13c3 m13c2 m13c2 m13c2 m13c0 = refl
  holds1350 m13c3 m13c2 m13c2 m13c2 m13c1 = refl
  holds1350 m13c3 m13c2 m13c2 m13c2 m13c2 = refl
  holds1350 m13c3 m13c2 m13c2 m13c2 m13c3 = refl
  holds1350 m13c3 m13c2 m13c2 m13c3 m13c0 = refl
  holds1350 m13c3 m13c2 m13c2 m13c3 m13c1 = refl
  holds1350 m13c3 m13c2 m13c2 m13c3 m13c2 = refl
  holds1350 m13c3 m13c2 m13c2 m13c3 m13c3 = refl
  holds1350 m13c3 m13c2 m13c3 m13c0 m13c0 = refl
  holds1350 m13c3 m13c2 m13c3 m13c0 m13c1 = refl
  holds1350 m13c3 m13c2 m13c3 m13c0 m13c2 = refl
  holds1350 m13c3 m13c2 m13c3 m13c0 m13c3 = refl
  holds1350 m13c3 m13c2 m13c3 m13c1 m13c0 = refl
  holds1350 m13c3 m13c2 m13c3 m13c1 m13c1 = refl
  holds1350 m13c3 m13c2 m13c3 m13c1 m13c2 = refl
  holds1350 m13c3 m13c2 m13c3 m13c1 m13c3 = refl
  holds1350 m13c3 m13c2 m13c3 m13c2 m13c0 = refl
  holds1350 m13c3 m13c2 m13c3 m13c2 m13c1 = refl
  holds1350 m13c3 m13c2 m13c3 m13c2 m13c2 = refl
  holds1350 m13c3 m13c2 m13c3 m13c2 m13c3 = refl
  holds1350 m13c3 m13c2 m13c3 m13c3 m13c0 = refl
  holds1350 m13c3 m13c2 m13c3 m13c3 m13c1 = refl
  holds1350 m13c3 m13c2 m13c3 m13c3 m13c2 = refl
  holds1350 m13c3 m13c2 m13c3 m13c3 m13c3 = refl
  holds1350 m13c3 m13c3 m13c0 m13c0 m13c0 = refl
  holds1350 m13c3 m13c3 m13c0 m13c0 m13c1 = refl
  holds1350 m13c3 m13c3 m13c0 m13c0 m13c2 = refl
  holds1350 m13c3 m13c3 m13c0 m13c0 m13c3 = refl
  holds1350 m13c3 m13c3 m13c0 m13c1 m13c0 = refl
  holds1350 m13c3 m13c3 m13c0 m13c1 m13c1 = refl
  holds1350 m13c3 m13c3 m13c0 m13c1 m13c2 = refl
  holds1350 m13c3 m13c3 m13c0 m13c1 m13c3 = refl
  holds1350 m13c3 m13c3 m13c0 m13c2 m13c0 = refl
  holds1350 m13c3 m13c3 m13c0 m13c2 m13c1 = refl
  holds1350 m13c3 m13c3 m13c0 m13c2 m13c2 = refl
  holds1350 m13c3 m13c3 m13c0 m13c2 m13c3 = refl
  holds1350 m13c3 m13c3 m13c0 m13c3 m13c0 = refl
  holds1350 m13c3 m13c3 m13c0 m13c3 m13c1 = refl
  holds1350 m13c3 m13c3 m13c0 m13c3 m13c2 = refl
  holds1350 m13c3 m13c3 m13c0 m13c3 m13c3 = refl
  holds1350 m13c3 m13c3 m13c1 m13c0 m13c0 = refl
  holds1350 m13c3 m13c3 m13c1 m13c0 m13c1 = refl
  holds1350 m13c3 m13c3 m13c1 m13c0 m13c2 = refl
  holds1350 m13c3 m13c3 m13c1 m13c0 m13c3 = refl
  holds1350 m13c3 m13c3 m13c1 m13c1 m13c0 = refl
  holds1350 m13c3 m13c3 m13c1 m13c1 m13c1 = refl
  holds1350 m13c3 m13c3 m13c1 m13c1 m13c2 = refl
  holds1350 m13c3 m13c3 m13c1 m13c1 m13c3 = refl
  holds1350 m13c3 m13c3 m13c1 m13c2 m13c0 = refl
  holds1350 m13c3 m13c3 m13c1 m13c2 m13c1 = refl
  holds1350 m13c3 m13c3 m13c1 m13c2 m13c2 = refl
  holds1350 m13c3 m13c3 m13c1 m13c2 m13c3 = refl
  holds1350 m13c3 m13c3 m13c1 m13c3 m13c0 = refl
  holds1350 m13c3 m13c3 m13c1 m13c3 m13c1 = refl
  holds1350 m13c3 m13c3 m13c1 m13c3 m13c2 = refl
  holds1350 m13c3 m13c3 m13c1 m13c3 m13c3 = refl
  holds1350 m13c3 m13c3 m13c2 m13c0 m13c0 = refl
  holds1350 m13c3 m13c3 m13c2 m13c0 m13c1 = refl
  holds1350 m13c3 m13c3 m13c2 m13c0 m13c2 = refl
  holds1350 m13c3 m13c3 m13c2 m13c0 m13c3 = refl
  holds1350 m13c3 m13c3 m13c2 m13c1 m13c0 = refl
  holds1350 m13c3 m13c3 m13c2 m13c1 m13c1 = refl
  holds1350 m13c3 m13c3 m13c2 m13c1 m13c2 = refl
  holds1350 m13c3 m13c3 m13c2 m13c1 m13c3 = refl
  holds1350 m13c3 m13c3 m13c2 m13c2 m13c0 = refl
  holds1350 m13c3 m13c3 m13c2 m13c2 m13c1 = refl
  holds1350 m13c3 m13c3 m13c2 m13c2 m13c2 = refl
  holds1350 m13c3 m13c3 m13c2 m13c2 m13c3 = refl
  holds1350 m13c3 m13c3 m13c2 m13c3 m13c0 = refl
  holds1350 m13c3 m13c3 m13c2 m13c3 m13c1 = refl
  holds1350 m13c3 m13c3 m13c2 m13c3 m13c2 = refl
  holds1350 m13c3 m13c3 m13c2 m13c3 m13c3 = refl
  holds1350 m13c3 m13c3 m13c3 m13c0 m13c0 = refl
  holds1350 m13c3 m13c3 m13c3 m13c0 m13c1 = refl
  holds1350 m13c3 m13c3 m13c3 m13c0 m13c2 = refl
  holds1350 m13c3 m13c3 m13c3 m13c0 m13c3 = refl
  holds1350 m13c3 m13c3 m13c3 m13c1 m13c0 = refl
  holds1350 m13c3 m13c3 m13c3 m13c1 m13c1 = refl
  holds1350 m13c3 m13c3 m13c3 m13c1 m13c2 = refl
  holds1350 m13c3 m13c3 m13c3 m13c1 m13c3 = refl
  holds1350 m13c3 m13c3 m13c3 m13c2 m13c0 = refl
  holds1350 m13c3 m13c3 m13c3 m13c2 m13c1 = refl
  holds1350 m13c3 m13c3 m13c3 m13c2 m13c2 = refl
  holds1350 m13c3 m13c3 m13c3 m13c2 m13c3 = refl
  holds1350 m13c3 m13c3 m13c3 m13c3 m13c0 = refl
  holds1350 m13c3 m13c3 m13c3 m13c3 m13c1 = refl
  holds1350 m13c3 m13c3 m13c3 m13c3 m13c2 = refl
  holds1350 m13c3 m13c3 m13c3 m13c3 m13c3 = refl
  cut1350 : (x6 : ℕ) → Adequate {ℓ} ((var 0) , (op (op (op (var 1) (op (var 2) (var 3))) (var 0)) (op (var 0) (var x6)))) → ⊥
  cut1350 x6 = reject13 ((var 0) , (op (op (op (var 1) (op (var 2) (var 3))) (var 0)) (op (var 0) (var x6)))) (λ env → holds1350 (env 0) (env 1) (env 2) (env 3) (env x6))
  holds1351 : (z0 z1 z2 z3 : A3) → z0 ≡ (mul3 (mul3 (mul3 z1 (mul3 z2 z3)) z0) (mul3 z1 z0))
  holds1351 z0 z1 z2 z3 = refl
  cut1351 : Adequate {ℓ} ((var 0) , (op (op (op (var 1) (op (var 2) (var 3))) (var 0)) (op (var 1) (var 0)))) → ⊥
  cut1351  = reject3 ((var 0) , (op (op (op (var 1) (op (var 2) (var 3))) (var 0)) (op (var 1) (var 0)))) (λ env → holds1351 (env 0) (env 1) (env 2) (env 3))
  env12 : ℕ → Two
  env12 zero = b0
  env12 (suc zero) = b1
  env12 (suc (suc zero)) = b0
  env12 (suc (suc (suc zero))) = b0
  env12 (suc (suc (suc (suc rest)))) = b0
  bad1352 : PathP (λ _ → Two) b0 (bop (bop (bop b1 (bop b0 b0)) b0) (bop b1 b1)) → ⊥
  bad1352  p = false≢true (cong lower p)
  cut1352 : Adequate {ℓ} ((var 0) , (op (op (op (var 1) (op (var 2) (var 3))) (var 0)) (op (var 1) (var 1)))) → ⊥
  cut1352  adequate = bad1352  (Adequate.valid adequate Two boolean env12)
  env13 : ℕ → Two
  env13 zero = b0
  env13 (suc zero) = b1
  env13 (suc (suc zero)) = b1
  env13 (suc (suc (suc zero))) = b0
  env13 (suc (suc (suc (suc rest)))) = b0
  bad1353 : PathP (λ _ → Two) b0 (bop (bop (bop b1 (bop b1 b0)) b0) (bop b1 b1)) → ⊥
  bad1353  p = false≢true (cong lower p)
  cut1353 : Adequate {ℓ} ((var 0) , (op (op (op (var 1) (op (var 2) (var 3))) (var 0)) (op (var 1) (var 2)))) → ⊥
  cut1353  adequate = bad1353  (Adequate.valid adequate Two boolean env13)
  bad1354 : PathP (λ _ → Two) b0 (bop (bop (bop b1 (bop b0 b1)) b0) (bop b1 b1)) → ⊥
  bad1354  p = false≢true (cong lower p)
  cut1354 : Adequate {ℓ} ((var 0) , (op (op (op (var 1) (op (var 2) (var 3))) (var 0)) (op (var 1) (var 3)))) → ⊥
  cut1354  adequate = bad1354  (Adequate.valid adequate Two boolean env7)
  env14 : ℕ → Two
  env14 zero = b0
  env14 (suc zero) = b1
  env14 (suc (suc zero)) = b0
  env14 (suc (suc (suc zero))) = b0
  env14 (suc (suc (suc (suc zero)))) = b1
  env14 (suc (suc (suc (suc (suc rest))))) = b0
  bad1355 : PathP (λ _ → Two) b0 (bop (bop (bop b1 (bop b0 b0)) b0) (bop b1 b1)) → ⊥
  bad1355  p = false≢true (cong lower p)
  cut1355 : Adequate {ℓ} ((var 0) , (op (op (op (var 1) (op (var 2) (var 3))) (var 0)) (op (var 1) (var 4)))) → ⊥
  cut1355  adequate = bad1355  (Adequate.valid adequate Two boolean env14)
  bad1356 : (z4 : Two) → PathP (λ _ → Two) b1 (bop (bop (bop b1 (bop b0 b0)) b1) (bop b0 z4)) → ⊥
  bad1356 z4 p = false≢true (sym (cong lower p))
  cut1356 : (x6 : ℕ) → Adequate {ℓ} ((var 0) , (op (op (op (var 1) (op (var 2) (var 3))) (var 0)) (op (var 2) (var x6)))) → ⊥
  cut1356 x6 adequate = bad1356 (env9 x6) (Adequate.valid adequate Two boolean env9)
  bad1357 : (z4 : Two) → PathP (λ _ → Two) b1 (bop (bop (bop b1 (bop b0 b0)) b1) (bop b0 z4)) → ⊥
  bad1357 z4 p = false≢true (sym (cong lower p))
  cut1357 : (x6 : ℕ) → Adequate {ℓ} ((var 0) , (op (op (op (var 1) (op (var 2) (var 3))) (var 0)) (op (var 3) (var x6)))) → ⊥
  cut1357 x6 adequate = bad1357 (env9 x6) (Adequate.valid adequate Two boolean env9)
  env15 : ℕ → Two
  env15 zero = b1
  env15 (suc zero) = b1
  env15 (suc (suc zero)) = b0
  env15 (suc (suc (suc zero))) = b0
  env15 (suc (suc (suc (suc zero)))) = b0
  env15 (suc (suc (suc (suc (suc rest))))) = b0
  bad1358 : (z5 : Two) → PathP (λ _ → Two) b1 (bop (bop (bop b1 (bop b0 b0)) b1) (bop b0 z5)) → ⊥
  bad1358 z5 p = false≢true (sym (cong lower p))
  cut1358 : (x6 : ℕ) → Adequate {ℓ} ((var 0) , (op (op (op (var 1) (op (var 2) (var 3))) (var 0)) (op (var 4) (var x6)))) → ⊥
  cut1358 x6 adequate = bad1358 (env15 x6) (Adequate.valid adequate Two boolean env15)
  env16 : ℕ → Two
  env16 zero = b0
  env16 (suc zero) = b1
  env16 (suc (suc zero)) = b1
  env16 (suc (suc (suc zero))) = b1
  env16 (suc (suc (suc (suc rest)))) = b0
  bad1359 : (z4 z5 : Two) → PathP (λ _ → Two) b0 (bop (bop (bop b1 (bop b1 b1)) b1) (bop z4 z5)) → ⊥
  bad1359 z4 z5 p = false≢true (cong lower p)
  cut1359 : (x5 x6 : ℕ) → Adequate {ℓ} ((var 0) , (op (op (op (var 1) (op (var 2) (var 3))) (var 1)) (op (var x5) (var x6)))) → ⊥
  cut1359 x5 x6 adequate = bad1359 (env16 x5) (env16 x6) (Adequate.valid adequate Two boolean env16)
  env17 : ℕ → Two
  env17 zero = b0
  env17 (suc zero) = b0
  env17 (suc (suc zero)) = b1
  env17 (suc (suc (suc zero))) = b0
  env17 (suc (suc (suc (suc rest)))) = b0
  bad1360 : (z4 z5 : Two) → PathP (λ _ → Two) b0 (bop (bop (bop b0 (bop b1 b0)) b1) (bop z4 z5)) → ⊥
  bad1360 z4 z5 p = false≢true (cong lower p)
  cut1360 : (x5 x6 : ℕ) → Adequate {ℓ} ((var 0) , (op (op (op (var 1) (op (var 2) (var 3))) (var 2)) (op (var x5) (var x6)))) → ⊥
  cut1360 x5 x6 adequate = bad1360 (env17 x5) (env17 x6) (Adequate.valid adequate Two boolean env17)
  bad1361 : (z4 z5 : Two) → PathP (λ _ → Two) b0 (bop (bop (bop b0 (bop b0 b1)) b1) (bop z4 z5)) → ⊥
  bad1361 z4 z5 p = false≢true (cong lower p)
  cut1361 : (x5 x6 : ℕ) → Adequate {ℓ} ((var 0) , (op (op (op (var 1) (op (var 2) (var 3))) (var 3)) (op (var x5) (var x6)))) → ⊥
  cut1361 x5 x6 adequate = bad1361 (env11 x5) (env11 x6) (Adequate.valid adequate Two boolean env11)
  env18 : ℕ → Two
  env18 zero = b0
  env18 (suc zero) = b0
  env18 (suc (suc zero)) = b0
  env18 (suc (suc (suc zero))) = b0
  env18 (suc (suc (suc (suc zero)))) = b1
  env18 (suc (suc (suc (suc (suc rest))))) = b0
  bad1362 : (z5 z6 : Two) → PathP (λ _ → Two) b0 (bop (bop (bop b0 (bop b0 b0)) b1) (bop z5 z6)) → ⊥
  bad1362 z5 z6 p = false≢true (cong lower p)
  cut1362 : (x5 x6 : ℕ) → Adequate {ℓ} ((var 0) , (op (op (op (var 1) (op (var 2) (var 3))) (var 4)) (op (var x5) (var x6)))) → ⊥
  cut1362 x5 x6 adequate = bad1362 (env18 x5) (env18 x6) (Adequate.valid adequate Two boolean env18)
