{-# OPTIONS --safe --cubical --guardedness #-}
module GeneratedMinimumShape88 where
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
  holds1194 : (z0 z1 z2 z3 z4 z5 : A2) → z0 ≡ (mul2 (mul2 z0 (mul2 (mul2 z1 z2) z3)) (mul2 z4 z5))
  holds1194 z0 z1 z2 z3 z4 z5 = refl
  cut1194 : (x2 x3 x4 x5 x6 : ℕ) → Adequate {ℓ} ((var 0) , (op (op (var 0) (op (op (var x2) (var x3)) (var x4))) (op (var x5) (var x6)))) → ⊥
  cut1194 x2 x3 x4 x5 x6 = reject2 ((var 0) , (op (op (var 0) (op (op (var x2) (var x3)) (var x4))) (op (var x5) (var x6)))) (λ env → holds1194 (env 0) (env x2) (env x3) (env x4) (env x5) (env x6))
  env0 : ℕ → Two
  env0 zero = b0
  env0 (suc zero) = b1
  env0 (suc (suc rest)) = b0
  bad1195 : (z2 z3 : Two) → PathP (λ _ → Two) b0 (bop (bop b1 (bop (bop b0 b0) b0)) (bop z2 z3)) → ⊥
  bad1195 z2 z3 p = false≢true (cong lower p)
  cut1195 : (x5 x6 : ℕ) → Adequate {ℓ} ((var 0) , (op (op (var 1) (op (op (var 0) (var 0)) (var 0))) (op (var x5) (var x6)))) → ⊥
  cut1195 x5 x6 adequate = bad1195 (env0 x5) (env0 x6) (Adequate.valid adequate Two boolean env0)
  holds1196 : (z0 z1 z2 : A13) → z0 ≡ (mul13 (mul13 z1 (mul13 (mul13 z0 z0) z1)) (mul13 z0 z2))
  holds1196 m13c0 m13c0 m13c0 = refl
  holds1196 m13c0 m13c0 m13c1 = refl
  holds1196 m13c0 m13c0 m13c2 = refl
  holds1196 m13c0 m13c0 m13c3 = refl
  holds1196 m13c0 m13c1 m13c0 = refl
  holds1196 m13c0 m13c1 m13c1 = refl
  holds1196 m13c0 m13c1 m13c2 = refl
  holds1196 m13c0 m13c1 m13c3 = refl
  holds1196 m13c0 m13c2 m13c0 = refl
  holds1196 m13c0 m13c2 m13c1 = refl
  holds1196 m13c0 m13c2 m13c2 = refl
  holds1196 m13c0 m13c2 m13c3 = refl
  holds1196 m13c0 m13c3 m13c0 = refl
  holds1196 m13c0 m13c3 m13c1 = refl
  holds1196 m13c0 m13c3 m13c2 = refl
  holds1196 m13c0 m13c3 m13c3 = refl
  holds1196 m13c1 m13c0 m13c0 = refl
  holds1196 m13c1 m13c0 m13c1 = refl
  holds1196 m13c1 m13c0 m13c2 = refl
  holds1196 m13c1 m13c0 m13c3 = refl
  holds1196 m13c1 m13c1 m13c0 = refl
  holds1196 m13c1 m13c1 m13c1 = refl
  holds1196 m13c1 m13c1 m13c2 = refl
  holds1196 m13c1 m13c1 m13c3 = refl
  holds1196 m13c1 m13c2 m13c0 = refl
  holds1196 m13c1 m13c2 m13c1 = refl
  holds1196 m13c1 m13c2 m13c2 = refl
  holds1196 m13c1 m13c2 m13c3 = refl
  holds1196 m13c1 m13c3 m13c0 = refl
  holds1196 m13c1 m13c3 m13c1 = refl
  holds1196 m13c1 m13c3 m13c2 = refl
  holds1196 m13c1 m13c3 m13c3 = refl
  holds1196 m13c2 m13c0 m13c0 = refl
  holds1196 m13c2 m13c0 m13c1 = refl
  holds1196 m13c2 m13c0 m13c2 = refl
  holds1196 m13c2 m13c0 m13c3 = refl
  holds1196 m13c2 m13c1 m13c0 = refl
  holds1196 m13c2 m13c1 m13c1 = refl
  holds1196 m13c2 m13c1 m13c2 = refl
  holds1196 m13c2 m13c1 m13c3 = refl
  holds1196 m13c2 m13c2 m13c0 = refl
  holds1196 m13c2 m13c2 m13c1 = refl
  holds1196 m13c2 m13c2 m13c2 = refl
  holds1196 m13c2 m13c2 m13c3 = refl
  holds1196 m13c2 m13c3 m13c0 = refl
  holds1196 m13c2 m13c3 m13c1 = refl
  holds1196 m13c2 m13c3 m13c2 = refl
  holds1196 m13c2 m13c3 m13c3 = refl
  holds1196 m13c3 m13c0 m13c0 = refl
  holds1196 m13c3 m13c0 m13c1 = refl
  holds1196 m13c3 m13c0 m13c2 = refl
  holds1196 m13c3 m13c0 m13c3 = refl
  holds1196 m13c3 m13c1 m13c0 = refl
  holds1196 m13c3 m13c1 m13c1 = refl
  holds1196 m13c3 m13c1 m13c2 = refl
  holds1196 m13c3 m13c1 m13c3 = refl
  holds1196 m13c3 m13c2 m13c0 = refl
  holds1196 m13c3 m13c2 m13c1 = refl
  holds1196 m13c3 m13c2 m13c2 = refl
  holds1196 m13c3 m13c2 m13c3 = refl
  holds1196 m13c3 m13c3 m13c0 = refl
  holds1196 m13c3 m13c3 m13c1 = refl
  holds1196 m13c3 m13c3 m13c2 = refl
  holds1196 m13c3 m13c3 m13c3 = refl
  cut1196 : (x6 : ℕ) → Adequate {ℓ} ((var 0) , (op (op (var 1) (op (op (var 0) (var 0)) (var 1))) (op (var 0) (var x6)))) → ⊥
  cut1196 x6 = reject13 ((var 0) , (op (op (var 1) (op (op (var 0) (var 0)) (var 1))) (op (var 0) (var x6)))) (λ env → holds1196 (env 0) (env 1) (env x6))
  env1 : ℕ → Two
  env1 zero = b1
  env1 (suc zero) = b0
  env1 (suc (suc rest)) = b0
  bad1197 : (z2 : Two) → PathP (λ _ → Two) b1 (bop (bop b0 (bop (bop b1 b1) b0)) (bop b0 z2)) → ⊥
  bad1197 z2 p = false≢true (sym (cong lower p))
  cut1197 : (x6 : ℕ) → Adequate {ℓ} ((var 0) , (op (op (var 1) (op (op (var 0) (var 0)) (var 1))) (op (var 1) (var x6)))) → ⊥
  cut1197 x6 adequate = bad1197 (env1 x6) (Adequate.valid adequate Two boolean env1)
  env2 : ℕ → Two
  env2 zero = b1
  env2 (suc zero) = b0
  env2 (suc (suc zero)) = b0
  env2 (suc (suc (suc rest))) = b0
  bad1198 : (z3 : Two) → PathP (λ _ → Two) b1 (bop (bop b0 (bop (bop b1 b1) b0)) (bop b0 z3)) → ⊥
  bad1198 z3 p = false≢true (sym (cong lower p))
  cut1198 : (x6 : ℕ) → Adequate {ℓ} ((var 0) , (op (op (var 1) (op (op (var 0) (var 0)) (var 1))) (op (var 2) (var x6)))) → ⊥
  cut1198 x6 adequate = bad1198 (env2 x6) (Adequate.valid adequate Two boolean env2)
  env3 : ℕ → Two
  env3 zero = b0
  env3 (suc zero) = b1
  env3 (suc (suc zero)) = b0
  env3 (suc (suc (suc rest))) = b0
  bad1199 : (z3 z4 : Two) → PathP (λ _ → Two) b0 (bop (bop b1 (bop (bop b0 b0) b0)) (bop z3 z4)) → ⊥
  bad1199 z3 z4 p = false≢true (cong lower p)
  cut1199 : (x5 x6 : ℕ) → Adequate {ℓ} ((var 0) , (op (op (var 1) (op (op (var 0) (var 0)) (var 2))) (op (var x5) (var x6)))) → ⊥
  cut1199 x5 x6 adequate = bad1199 (env3 x5) (env3 x6) (Adequate.valid adequate Two boolean env3)
  bad1200 : (z2 z3 : Two) → PathP (λ _ → Two) b0 (bop (bop b1 (bop (bop b0 b1) b0)) (bop z2 z3)) → ⊥
  bad1200 z2 z3 p = false≢true (cong lower p)
  cut1200 : (x5 x6 : ℕ) → Adequate {ℓ} ((var 0) , (op (op (var 1) (op (op (var 0) (var 1)) (var 0))) (op (var x5) (var x6)))) → ⊥
  cut1200 x5 x6 adequate = bad1200 (env0 x5) (env0 x6) (Adequate.valid adequate Two boolean env0)
  holds1201 : (z0 z1 : A3) → z0 ≡ (mul3 (mul3 z1 (mul3 (mul3 z0 z1) z1)) (mul3 z0 z0))
  holds1201 z0 z1 = refl
  cut1201 : Adequate {ℓ} ((var 0) , (op (op (var 1) (op (op (var 0) (var 1)) (var 1))) (op (var 0) (var 0)))) → ⊥
  cut1201  = reject3 ((var 0) , (op (op (var 1) (op (op (var 0) (var 1)) (var 1))) (op (var 0) (var 0)))) (λ env → holds1201 (env 0) (env 1))
  bad1202 : PathP (λ _ → Two) b1 (bop (bop b0 (bop (bop b1 b0) b0)) (bop b1 b0)) → ⊥
  bad1202  p = false≢true (sym (cong lower p))
  cut1202 : Adequate {ℓ} ((var 0) , (op (op (var 1) (op (op (var 0) (var 1)) (var 1))) (op (var 0) (var 1)))) → ⊥
  cut1202  adequate = bad1202  (Adequate.valid adequate Two boolean env1)
  bad1203 : PathP (λ _ → Two) b1 (bop (bop b0 (bop (bop b1 b0) b0)) (bop b1 b0)) → ⊥
  bad1203  p = false≢true (sym (cong lower p))
  cut1203 : Adequate {ℓ} ((var 0) , (op (op (var 1) (op (op (var 0) (var 1)) (var 1))) (op (var 0) (var 2)))) → ⊥
  cut1203  adequate = bad1203  (Adequate.valid adequate Two boolean env2)
  bad1204 : (z2 : Two) → PathP (λ _ → Two) b1 (bop (bop b0 (bop (bop b1 b0) b0)) (bop b0 z2)) → ⊥
  bad1204 z2 p = false≢true (sym (cong lower p))
  cut1204 : (x6 : ℕ) → Adequate {ℓ} ((var 0) , (op (op (var 1) (op (op (var 0) (var 1)) (var 1))) (op (var 1) (var x6)))) → ⊥
  cut1204 x6 adequate = bad1204 (env1 x6) (Adequate.valid adequate Two boolean env1)
  bad1205 : (z3 : Two) → PathP (λ _ → Two) b1 (bop (bop b0 (bop (bop b1 b0) b0)) (bop b0 z3)) → ⊥
  bad1205 z3 p = false≢true (sym (cong lower p))
  cut1205 : (x6 : ℕ) → Adequate {ℓ} ((var 0) , (op (op (var 1) (op (op (var 0) (var 1)) (var 1))) (op (var 2) (var x6)))) → ⊥
  cut1205 x6 adequate = bad1205 (env2 x6) (Adequate.valid adequate Two boolean env2)
  bad1206 : (z3 z4 : Two) → PathP (λ _ → Two) b0 (bop (bop b1 (bop (bop b0 b1) b0)) (bop z3 z4)) → ⊥
  bad1206 z3 z4 p = false≢true (cong lower p)
  cut1206 : (x5 x6 : ℕ) → Adequate {ℓ} ((var 0) , (op (op (var 1) (op (op (var 0) (var 1)) (var 2))) (op (var x5) (var x6)))) → ⊥
  cut1206 x5 x6 adequate = bad1206 (env3 x5) (env3 x6) (Adequate.valid adequate Two boolean env3)
  bad1207 : (z3 z4 : Two) → PathP (λ _ → Two) b0 (bop (bop b1 (bop (bop b0 b0) b0)) (bop z3 z4)) → ⊥
  bad1207 z3 z4 p = false≢true (cong lower p)
  cut1207 : (x5 x6 : ℕ) → Adequate {ℓ} ((var 0) , (op (op (var 1) (op (op (var 0) (var 2)) (var 0))) (op (var x5) (var x6)))) → ⊥
  cut1207 x5 x6 adequate = bad1207 (env3 x5) (env3 x6) (Adequate.valid adequate Two boolean env3)
  holds1208 : (z0 z1 z2 : A3) → z0 ≡ (mul3 (mul3 z1 (mul3 (mul3 z0 z2) z1)) (mul3 z0 z0))
  holds1208 z0 z1 z2 = refl
  cut1208 : Adequate {ℓ} ((var 0) , (op (op (var 1) (op (op (var 0) (var 2)) (var 1))) (op (var 0) (var 0)))) → ⊥
  cut1208  = reject3 ((var 0) , (op (op (var 1) (op (op (var 0) (var 2)) (var 1))) (op (var 0) (var 0)))) (λ env → holds1208 (env 0) (env 1) (env 2))
  bad1209 : PathP (λ _ → Two) b1 (bop (bop b0 (bop (bop b1 b0) b0)) (bop b1 b0)) → ⊥
  bad1209  p = false≢true (sym (cong lower p))
  cut1209 : Adequate {ℓ} ((var 0) , (op (op (var 1) (op (op (var 0) (var 2)) (var 1))) (op (var 0) (var 1)))) → ⊥
  cut1209  adequate = bad1209  (Adequate.valid adequate Two boolean env2)
  bad1210 : PathP (λ _ → Two) b1 (bop (bop b0 (bop (bop b1 b0) b0)) (bop b1 b0)) → ⊥
  bad1210  p = false≢true (sym (cong lower p))
  cut1210 : Adequate {ℓ} ((var 0) , (op (op (var 1) (op (op (var 0) (var 2)) (var 1))) (op (var 0) (var 2)))) → ⊥
  cut1210  adequate = bad1210  (Adequate.valid adequate Two boolean env2)
  env4 : ℕ → Two
  env4 zero = b1
  env4 (suc zero) = b0
  env4 (suc (suc zero)) = b0
  env4 (suc (suc (suc zero))) = b0
  env4 (suc (suc (suc (suc rest)))) = b0
  bad1211 : PathP (λ _ → Two) b1 (bop (bop b0 (bop (bop b1 b0) b0)) (bop b1 b0)) → ⊥
  bad1211  p = false≢true (sym (cong lower p))
  cut1211 : Adequate {ℓ} ((var 0) , (op (op (var 1) (op (op (var 0) (var 2)) (var 1))) (op (var 0) (var 3)))) → ⊥
  cut1211  adequate = bad1211  (Adequate.valid adequate Two boolean env4)
  bad1212 : (z3 : Two) → PathP (λ _ → Two) b1 (bop (bop b0 (bop (bop b1 b0) b0)) (bop b0 z3)) → ⊥
  bad1212 z3 p = false≢true (sym (cong lower p))
  cut1212 : (x6 : ℕ) → Adequate {ℓ} ((var 0) , (op (op (var 1) (op (op (var 0) (var 2)) (var 1))) (op (var 1) (var x6)))) → ⊥
  cut1212 x6 adequate = bad1212 (env2 x6) (Adequate.valid adequate Two boolean env2)
  bad1213 : (z3 : Two) → PathP (λ _ → Two) b1 (bop (bop b0 (bop (bop b1 b0) b0)) (bop b0 z3)) → ⊥
  bad1213 z3 p = false≢true (sym (cong lower p))
  cut1213 : (x6 : ℕ) → Adequate {ℓ} ((var 0) , (op (op (var 1) (op (op (var 0) (var 2)) (var 1))) (op (var 2) (var x6)))) → ⊥
  cut1213 x6 adequate = bad1213 (env2 x6) (Adequate.valid adequate Two boolean env2)
  bad1214 : (z4 : Two) → PathP (λ _ → Two) b1 (bop (bop b0 (bop (bop b1 b0) b0)) (bop b0 z4)) → ⊥
  bad1214 z4 p = false≢true (sym (cong lower p))
  cut1214 : (x6 : ℕ) → Adequate {ℓ} ((var 0) , (op (op (var 1) (op (op (var 0) (var 2)) (var 1))) (op (var 3) (var x6)))) → ⊥
  cut1214 x6 adequate = bad1214 (env4 x6) (Adequate.valid adequate Two boolean env4)
  bad1215 : (z3 z4 : Two) → PathP (λ _ → Two) b0 (bop (bop b1 (bop (bop b0 b0) b0)) (bop z3 z4)) → ⊥
  bad1215 z3 z4 p = false≢true (cong lower p)
  cut1215 : (x5 x6 : ℕ) → Adequate {ℓ} ((var 0) , (op (op (var 1) (op (op (var 0) (var 2)) (var 2))) (op (var x5) (var x6)))) → ⊥
  cut1215 x5 x6 adequate = bad1215 (env3 x5) (env3 x6) (Adequate.valid adequate Two boolean env3)
  env5 : ℕ → Two
  env5 zero = b0
  env5 (suc zero) = b1
  env5 (suc (suc zero)) = b0
  env5 (suc (suc (suc zero))) = b0
  env5 (suc (suc (suc (suc rest)))) = b0
  bad1216 : (z4 z5 : Two) → PathP (λ _ → Two) b0 (bop (bop b1 (bop (bop b0 b0) b0)) (bop z4 z5)) → ⊥
  bad1216 z4 z5 p = false≢true (cong lower p)
  cut1216 : (x5 x6 : ℕ) → Adequate {ℓ} ((var 0) , (op (op (var 1) (op (op (var 0) (var 2)) (var 3))) (op (var x5) (var x6)))) → ⊥
  cut1216 x5 x6 adequate = bad1216 (env5 x5) (env5 x6) (Adequate.valid adequate Two boolean env5)
  bad1217 : (z2 z3 : Two) → PathP (λ _ → Two) b0 (bop (bop b1 (bop (bop b1 b0) b0)) (bop z2 z3)) → ⊥
  bad1217 z2 z3 p = false≢true (cong lower p)
  cut1217 : (x5 x6 : ℕ) → Adequate {ℓ} ((var 0) , (op (op (var 1) (op (op (var 1) (var 0)) (var 0))) (op (var x5) (var x6)))) → ⊥
  cut1217 x5 x6 adequate = bad1217 (env0 x5) (env0 x6) (Adequate.valid adequate Two boolean env0)
  holds1218 : (z0 z1 z2 : A13) → z0 ≡ (mul13 (mul13 z1 (mul13 (mul13 z1 z0) z1)) (mul13 z0 z2))
  holds1218 m13c0 m13c0 m13c0 = refl
  holds1218 m13c0 m13c0 m13c1 = refl
  holds1218 m13c0 m13c0 m13c2 = refl
  holds1218 m13c0 m13c0 m13c3 = refl
  holds1218 m13c0 m13c1 m13c0 = refl
  holds1218 m13c0 m13c1 m13c1 = refl
  holds1218 m13c0 m13c1 m13c2 = refl
  holds1218 m13c0 m13c1 m13c3 = refl
  holds1218 m13c0 m13c2 m13c0 = refl
  holds1218 m13c0 m13c2 m13c1 = refl
  holds1218 m13c0 m13c2 m13c2 = refl
  holds1218 m13c0 m13c2 m13c3 = refl
  holds1218 m13c0 m13c3 m13c0 = refl
  holds1218 m13c0 m13c3 m13c1 = refl
  holds1218 m13c0 m13c3 m13c2 = refl
  holds1218 m13c0 m13c3 m13c3 = refl
  holds1218 m13c1 m13c0 m13c0 = refl
  holds1218 m13c1 m13c0 m13c1 = refl
  holds1218 m13c1 m13c0 m13c2 = refl
  holds1218 m13c1 m13c0 m13c3 = refl
  holds1218 m13c1 m13c1 m13c0 = refl
  holds1218 m13c1 m13c1 m13c1 = refl
  holds1218 m13c1 m13c1 m13c2 = refl
  holds1218 m13c1 m13c1 m13c3 = refl
  holds1218 m13c1 m13c2 m13c0 = refl
  holds1218 m13c1 m13c2 m13c1 = refl
  holds1218 m13c1 m13c2 m13c2 = refl
  holds1218 m13c1 m13c2 m13c3 = refl
  holds1218 m13c1 m13c3 m13c0 = refl
  holds1218 m13c1 m13c3 m13c1 = refl
  holds1218 m13c1 m13c3 m13c2 = refl
  holds1218 m13c1 m13c3 m13c3 = refl
  holds1218 m13c2 m13c0 m13c0 = refl
  holds1218 m13c2 m13c0 m13c1 = refl
  holds1218 m13c2 m13c0 m13c2 = refl
  holds1218 m13c2 m13c0 m13c3 = refl
  holds1218 m13c2 m13c1 m13c0 = refl
  holds1218 m13c2 m13c1 m13c1 = refl
  holds1218 m13c2 m13c1 m13c2 = refl
  holds1218 m13c2 m13c1 m13c3 = refl
  holds1218 m13c2 m13c2 m13c0 = refl
  holds1218 m13c2 m13c2 m13c1 = refl
  holds1218 m13c2 m13c2 m13c2 = refl
  holds1218 m13c2 m13c2 m13c3 = refl
  holds1218 m13c2 m13c3 m13c0 = refl
  holds1218 m13c2 m13c3 m13c1 = refl
  holds1218 m13c2 m13c3 m13c2 = refl
  holds1218 m13c2 m13c3 m13c3 = refl
  holds1218 m13c3 m13c0 m13c0 = refl
  holds1218 m13c3 m13c0 m13c1 = refl
  holds1218 m13c3 m13c0 m13c2 = refl
  holds1218 m13c3 m13c0 m13c3 = refl
  holds1218 m13c3 m13c1 m13c0 = refl
  holds1218 m13c3 m13c1 m13c1 = refl
  holds1218 m13c3 m13c1 m13c2 = refl
  holds1218 m13c3 m13c1 m13c3 = refl
  holds1218 m13c3 m13c2 m13c0 = refl
  holds1218 m13c3 m13c2 m13c1 = refl
  holds1218 m13c3 m13c2 m13c2 = refl
  holds1218 m13c3 m13c2 m13c3 = refl
  holds1218 m13c3 m13c3 m13c0 = refl
  holds1218 m13c3 m13c3 m13c1 = refl
  holds1218 m13c3 m13c3 m13c2 = refl
  holds1218 m13c3 m13c3 m13c3 = refl
  cut1218 : (x6 : ℕ) → Adequate {ℓ} ((var 0) , (op (op (var 1) (op (op (var 1) (var 0)) (var 1))) (op (var 0) (var x6)))) → ⊥
  cut1218 x6 = reject13 ((var 0) , (op (op (var 1) (op (op (var 1) (var 0)) (var 1))) (op (var 0) (var x6)))) (λ env → holds1218 (env 0) (env 1) (env x6))
  bad1219 : (z2 : Two) → PathP (λ _ → Two) b1 (bop (bop b0 (bop (bop b0 b1) b0)) (bop b0 z2)) → ⊥
  bad1219 z2 p = false≢true (sym (cong lower p))
  cut1219 : (x6 : ℕ) → Adequate {ℓ} ((var 0) , (op (op (var 1) (op (op (var 1) (var 0)) (var 1))) (op (var 1) (var x6)))) → ⊥
  cut1219 x6 adequate = bad1219 (env1 x6) (Adequate.valid adequate Two boolean env1)
  bad1220 : (z3 : Two) → PathP (λ _ → Two) b1 (bop (bop b0 (bop (bop b0 b1) b0)) (bop b0 z3)) → ⊥
  bad1220 z3 p = false≢true (sym (cong lower p))
  cut1220 : (x6 : ℕ) → Adequate {ℓ} ((var 0) , (op (op (var 1) (op (op (var 1) (var 0)) (var 1))) (op (var 2) (var x6)))) → ⊥
  cut1220 x6 adequate = bad1220 (env2 x6) (Adequate.valid adequate Two boolean env2)
  bad1221 : (z3 z4 : Two) → PathP (λ _ → Two) b0 (bop (bop b1 (bop (bop b1 b0) b0)) (bop z3 z4)) → ⊥
  bad1221 z3 z4 p = false≢true (cong lower p)
  cut1221 : (x5 x6 : ℕ) → Adequate {ℓ} ((var 0) , (op (op (var 1) (op (op (var 1) (var 0)) (var 2))) (op (var x5) (var x6)))) → ⊥
  cut1221 x5 x6 adequate = bad1221 (env3 x5) (env3 x6) (Adequate.valid adequate Two boolean env3)
  bad1222 : (z2 z3 z4 : Two) → PathP (λ _ → Two) b0 (bop (bop b1 (bop (bop b1 b1) z2)) (bop z3 z4)) → ⊥
  bad1222 z2 z3 z4 p = false≢true (cong lower p)
  cut1222 : (x4 x5 x6 : ℕ) → Adequate {ℓ} ((var 0) , (op (op (var 1) (op (op (var 1) (var 1)) (var x4))) (op (var x5) (var x6)))) → ⊥
  cut1222 x4 x5 x6 adequate = bad1222 (env0 x4) (env0 x5) (env0 x6) (Adequate.valid adequate Two boolean env0)
  env6 : ℕ → Two
  env6 zero = b0
  env6 (suc zero) = b1
  env6 (suc (suc zero)) = b1
  env6 (suc (suc (suc rest))) = b0
  bad1223 : (z3 z4 z5 : Two) → PathP (λ _ → Two) b0 (bop (bop b1 (bop (bop b1 b1) z3)) (bop z4 z5)) → ⊥
  bad1223 z3 z4 z5 p = false≢true (cong lower p)
  cut1223 : (x4 x5 x6 : ℕ) → Adequate {ℓ} ((var 0) , (op (op (var 1) (op (op (var 1) (var 2)) (var x4))) (op (var x5) (var x6)))) → ⊥
  cut1223 x4 x5 x6 adequate = bad1223 (env6 x4) (env6 x5) (env6 x6) (Adequate.valid adequate Two boolean env6)
  bad1224 : (z3 z4 : Two) → PathP (λ _ → Two) b0 (bop (bop b1 (bop (bop b0 b0) b0)) (bop z3 z4)) → ⊥
  bad1224 z3 z4 p = false≢true (cong lower p)
  cut1224 : (x5 x6 : ℕ) → Adequate {ℓ} ((var 0) , (op (op (var 1) (op (op (var 2) (var 0)) (var 0))) (op (var x5) (var x6)))) → ⊥
  cut1224 x5 x6 adequate = bad1224 (env3 x5) (env3 x6) (Adequate.valid adequate Two boolean env3)
  holds1225 : (z0 z1 z2 z3 : A13) → z0 ≡ (mul13 (mul13 z1 (mul13 (mul13 z2 z0) z1)) (mul13 z0 z3))
  holds1225 m13c0 m13c0 m13c0 m13c0 = refl
  holds1225 m13c0 m13c0 m13c0 m13c1 = refl
  holds1225 m13c0 m13c0 m13c0 m13c2 = refl
  holds1225 m13c0 m13c0 m13c0 m13c3 = refl
  holds1225 m13c0 m13c0 m13c1 m13c0 = refl
  holds1225 m13c0 m13c0 m13c1 m13c1 = refl
  holds1225 m13c0 m13c0 m13c1 m13c2 = refl
  holds1225 m13c0 m13c0 m13c1 m13c3 = refl
  holds1225 m13c0 m13c0 m13c2 m13c0 = refl
  holds1225 m13c0 m13c0 m13c2 m13c1 = refl
  holds1225 m13c0 m13c0 m13c2 m13c2 = refl
  holds1225 m13c0 m13c0 m13c2 m13c3 = refl
  holds1225 m13c0 m13c0 m13c3 m13c0 = refl
  holds1225 m13c0 m13c0 m13c3 m13c1 = refl
  holds1225 m13c0 m13c0 m13c3 m13c2 = refl
  holds1225 m13c0 m13c0 m13c3 m13c3 = refl
  holds1225 m13c0 m13c1 m13c0 m13c0 = refl
  holds1225 m13c0 m13c1 m13c0 m13c1 = refl
  holds1225 m13c0 m13c1 m13c0 m13c2 = refl
  holds1225 m13c0 m13c1 m13c0 m13c3 = refl
  holds1225 m13c0 m13c1 m13c1 m13c0 = refl
  holds1225 m13c0 m13c1 m13c1 m13c1 = refl
  holds1225 m13c0 m13c1 m13c1 m13c2 = refl
  holds1225 m13c0 m13c1 m13c1 m13c3 = refl
  holds1225 m13c0 m13c1 m13c2 m13c0 = refl
  holds1225 m13c0 m13c1 m13c2 m13c1 = refl
  holds1225 m13c0 m13c1 m13c2 m13c2 = refl
  holds1225 m13c0 m13c1 m13c2 m13c3 = refl
  holds1225 m13c0 m13c1 m13c3 m13c0 = refl
  holds1225 m13c0 m13c1 m13c3 m13c1 = refl
  holds1225 m13c0 m13c1 m13c3 m13c2 = refl
  holds1225 m13c0 m13c1 m13c3 m13c3 = refl
  holds1225 m13c0 m13c2 m13c0 m13c0 = refl
  holds1225 m13c0 m13c2 m13c0 m13c1 = refl
  holds1225 m13c0 m13c2 m13c0 m13c2 = refl
  holds1225 m13c0 m13c2 m13c0 m13c3 = refl
  holds1225 m13c0 m13c2 m13c1 m13c0 = refl
  holds1225 m13c0 m13c2 m13c1 m13c1 = refl
  holds1225 m13c0 m13c2 m13c1 m13c2 = refl
  holds1225 m13c0 m13c2 m13c1 m13c3 = refl
  holds1225 m13c0 m13c2 m13c2 m13c0 = refl
  holds1225 m13c0 m13c2 m13c2 m13c1 = refl
  holds1225 m13c0 m13c2 m13c2 m13c2 = refl
  holds1225 m13c0 m13c2 m13c2 m13c3 = refl
  holds1225 m13c0 m13c2 m13c3 m13c0 = refl
  holds1225 m13c0 m13c2 m13c3 m13c1 = refl
  holds1225 m13c0 m13c2 m13c3 m13c2 = refl
  holds1225 m13c0 m13c2 m13c3 m13c3 = refl
  holds1225 m13c0 m13c3 m13c0 m13c0 = refl
  holds1225 m13c0 m13c3 m13c0 m13c1 = refl
  holds1225 m13c0 m13c3 m13c0 m13c2 = refl
  holds1225 m13c0 m13c3 m13c0 m13c3 = refl
  holds1225 m13c0 m13c3 m13c1 m13c0 = refl
  holds1225 m13c0 m13c3 m13c1 m13c1 = refl
  holds1225 m13c0 m13c3 m13c1 m13c2 = refl
  holds1225 m13c0 m13c3 m13c1 m13c3 = refl
  holds1225 m13c0 m13c3 m13c2 m13c0 = refl
  holds1225 m13c0 m13c3 m13c2 m13c1 = refl
  holds1225 m13c0 m13c3 m13c2 m13c2 = refl
  holds1225 m13c0 m13c3 m13c2 m13c3 = refl
  holds1225 m13c0 m13c3 m13c3 m13c0 = refl
  holds1225 m13c0 m13c3 m13c3 m13c1 = refl
  holds1225 m13c0 m13c3 m13c3 m13c2 = refl
  holds1225 m13c0 m13c3 m13c3 m13c3 = refl
  holds1225 m13c1 m13c0 m13c0 m13c0 = refl
  holds1225 m13c1 m13c0 m13c0 m13c1 = refl
  holds1225 m13c1 m13c0 m13c0 m13c2 = refl
  holds1225 m13c1 m13c0 m13c0 m13c3 = refl
  holds1225 m13c1 m13c0 m13c1 m13c0 = refl
  holds1225 m13c1 m13c0 m13c1 m13c1 = refl
  holds1225 m13c1 m13c0 m13c1 m13c2 = refl
  holds1225 m13c1 m13c0 m13c1 m13c3 = refl
  holds1225 m13c1 m13c0 m13c2 m13c0 = refl
  holds1225 m13c1 m13c0 m13c2 m13c1 = refl
  holds1225 m13c1 m13c0 m13c2 m13c2 = refl
  holds1225 m13c1 m13c0 m13c2 m13c3 = refl
  holds1225 m13c1 m13c0 m13c3 m13c0 = refl
  holds1225 m13c1 m13c0 m13c3 m13c1 = refl
  holds1225 m13c1 m13c0 m13c3 m13c2 = refl
  holds1225 m13c1 m13c0 m13c3 m13c3 = refl
  holds1225 m13c1 m13c1 m13c0 m13c0 = refl
  holds1225 m13c1 m13c1 m13c0 m13c1 = refl
  holds1225 m13c1 m13c1 m13c0 m13c2 = refl
  holds1225 m13c1 m13c1 m13c0 m13c3 = refl
  holds1225 m13c1 m13c1 m13c1 m13c0 = refl
  holds1225 m13c1 m13c1 m13c1 m13c1 = refl
  holds1225 m13c1 m13c1 m13c1 m13c2 = refl
  holds1225 m13c1 m13c1 m13c1 m13c3 = refl
  holds1225 m13c1 m13c1 m13c2 m13c0 = refl
  holds1225 m13c1 m13c1 m13c2 m13c1 = refl
  holds1225 m13c1 m13c1 m13c2 m13c2 = refl
  holds1225 m13c1 m13c1 m13c2 m13c3 = refl
  holds1225 m13c1 m13c1 m13c3 m13c0 = refl
  holds1225 m13c1 m13c1 m13c3 m13c1 = refl
  holds1225 m13c1 m13c1 m13c3 m13c2 = refl
  holds1225 m13c1 m13c1 m13c3 m13c3 = refl
  holds1225 m13c1 m13c2 m13c0 m13c0 = refl
  holds1225 m13c1 m13c2 m13c0 m13c1 = refl
  holds1225 m13c1 m13c2 m13c0 m13c2 = refl
  holds1225 m13c1 m13c2 m13c0 m13c3 = refl
  holds1225 m13c1 m13c2 m13c1 m13c0 = refl
  holds1225 m13c1 m13c2 m13c1 m13c1 = refl
  holds1225 m13c1 m13c2 m13c1 m13c2 = refl
  holds1225 m13c1 m13c2 m13c1 m13c3 = refl
  holds1225 m13c1 m13c2 m13c2 m13c0 = refl
  holds1225 m13c1 m13c2 m13c2 m13c1 = refl
  holds1225 m13c1 m13c2 m13c2 m13c2 = refl
  holds1225 m13c1 m13c2 m13c2 m13c3 = refl
  holds1225 m13c1 m13c2 m13c3 m13c0 = refl
  holds1225 m13c1 m13c2 m13c3 m13c1 = refl
  holds1225 m13c1 m13c2 m13c3 m13c2 = refl
  holds1225 m13c1 m13c2 m13c3 m13c3 = refl
  holds1225 m13c1 m13c3 m13c0 m13c0 = refl
  holds1225 m13c1 m13c3 m13c0 m13c1 = refl
  holds1225 m13c1 m13c3 m13c0 m13c2 = refl
  holds1225 m13c1 m13c3 m13c0 m13c3 = refl
  holds1225 m13c1 m13c3 m13c1 m13c0 = refl
  holds1225 m13c1 m13c3 m13c1 m13c1 = refl
  holds1225 m13c1 m13c3 m13c1 m13c2 = refl
  holds1225 m13c1 m13c3 m13c1 m13c3 = refl
  holds1225 m13c1 m13c3 m13c2 m13c0 = refl
  holds1225 m13c1 m13c3 m13c2 m13c1 = refl
  holds1225 m13c1 m13c3 m13c2 m13c2 = refl
  holds1225 m13c1 m13c3 m13c2 m13c3 = refl
  holds1225 m13c1 m13c3 m13c3 m13c0 = refl
  holds1225 m13c1 m13c3 m13c3 m13c1 = refl
  holds1225 m13c1 m13c3 m13c3 m13c2 = refl
  holds1225 m13c1 m13c3 m13c3 m13c3 = refl
  holds1225 m13c2 m13c0 m13c0 m13c0 = refl
  holds1225 m13c2 m13c0 m13c0 m13c1 = refl
  holds1225 m13c2 m13c0 m13c0 m13c2 = refl
  holds1225 m13c2 m13c0 m13c0 m13c3 = refl
  holds1225 m13c2 m13c0 m13c1 m13c0 = refl
  holds1225 m13c2 m13c0 m13c1 m13c1 = refl
  holds1225 m13c2 m13c0 m13c1 m13c2 = refl
  holds1225 m13c2 m13c0 m13c1 m13c3 = refl
  holds1225 m13c2 m13c0 m13c2 m13c0 = refl
  holds1225 m13c2 m13c0 m13c2 m13c1 = refl
  holds1225 m13c2 m13c0 m13c2 m13c2 = refl
  holds1225 m13c2 m13c0 m13c2 m13c3 = refl
  holds1225 m13c2 m13c0 m13c3 m13c0 = refl
  holds1225 m13c2 m13c0 m13c3 m13c1 = refl
  holds1225 m13c2 m13c0 m13c3 m13c2 = refl
  holds1225 m13c2 m13c0 m13c3 m13c3 = refl
  holds1225 m13c2 m13c1 m13c0 m13c0 = refl
  holds1225 m13c2 m13c1 m13c0 m13c1 = refl
  holds1225 m13c2 m13c1 m13c0 m13c2 = refl
  holds1225 m13c2 m13c1 m13c0 m13c3 = refl
  holds1225 m13c2 m13c1 m13c1 m13c0 = refl
  holds1225 m13c2 m13c1 m13c1 m13c1 = refl
  holds1225 m13c2 m13c1 m13c1 m13c2 = refl
  holds1225 m13c2 m13c1 m13c1 m13c3 = refl
  holds1225 m13c2 m13c1 m13c2 m13c0 = refl
  holds1225 m13c2 m13c1 m13c2 m13c1 = refl
  holds1225 m13c2 m13c1 m13c2 m13c2 = refl
  holds1225 m13c2 m13c1 m13c2 m13c3 = refl
  holds1225 m13c2 m13c1 m13c3 m13c0 = refl
  holds1225 m13c2 m13c1 m13c3 m13c1 = refl
  holds1225 m13c2 m13c1 m13c3 m13c2 = refl
  holds1225 m13c2 m13c1 m13c3 m13c3 = refl
  holds1225 m13c2 m13c2 m13c0 m13c0 = refl
  holds1225 m13c2 m13c2 m13c0 m13c1 = refl
  holds1225 m13c2 m13c2 m13c0 m13c2 = refl
  holds1225 m13c2 m13c2 m13c0 m13c3 = refl
  holds1225 m13c2 m13c2 m13c1 m13c0 = refl
  holds1225 m13c2 m13c2 m13c1 m13c1 = refl
  holds1225 m13c2 m13c2 m13c1 m13c2 = refl
  holds1225 m13c2 m13c2 m13c1 m13c3 = refl
  holds1225 m13c2 m13c2 m13c2 m13c0 = refl
  holds1225 m13c2 m13c2 m13c2 m13c1 = refl
  holds1225 m13c2 m13c2 m13c2 m13c2 = refl
  holds1225 m13c2 m13c2 m13c2 m13c3 = refl
  holds1225 m13c2 m13c2 m13c3 m13c0 = refl
  holds1225 m13c2 m13c2 m13c3 m13c1 = refl
  holds1225 m13c2 m13c2 m13c3 m13c2 = refl
  holds1225 m13c2 m13c2 m13c3 m13c3 = refl
  holds1225 m13c2 m13c3 m13c0 m13c0 = refl
  holds1225 m13c2 m13c3 m13c0 m13c1 = refl
  holds1225 m13c2 m13c3 m13c0 m13c2 = refl
  holds1225 m13c2 m13c3 m13c0 m13c3 = refl
  holds1225 m13c2 m13c3 m13c1 m13c0 = refl
  holds1225 m13c2 m13c3 m13c1 m13c1 = refl
  holds1225 m13c2 m13c3 m13c1 m13c2 = refl
  holds1225 m13c2 m13c3 m13c1 m13c3 = refl
  holds1225 m13c2 m13c3 m13c2 m13c0 = refl
  holds1225 m13c2 m13c3 m13c2 m13c1 = refl
  holds1225 m13c2 m13c3 m13c2 m13c2 = refl
  holds1225 m13c2 m13c3 m13c2 m13c3 = refl
  holds1225 m13c2 m13c3 m13c3 m13c0 = refl
  holds1225 m13c2 m13c3 m13c3 m13c1 = refl
  holds1225 m13c2 m13c3 m13c3 m13c2 = refl
  holds1225 m13c2 m13c3 m13c3 m13c3 = refl
  holds1225 m13c3 m13c0 m13c0 m13c0 = refl
  holds1225 m13c3 m13c0 m13c0 m13c1 = refl
  holds1225 m13c3 m13c0 m13c0 m13c2 = refl
  holds1225 m13c3 m13c0 m13c0 m13c3 = refl
  holds1225 m13c3 m13c0 m13c1 m13c0 = refl
  holds1225 m13c3 m13c0 m13c1 m13c1 = refl
  holds1225 m13c3 m13c0 m13c1 m13c2 = refl
  holds1225 m13c3 m13c0 m13c1 m13c3 = refl
  holds1225 m13c3 m13c0 m13c2 m13c0 = refl
  holds1225 m13c3 m13c0 m13c2 m13c1 = refl
  holds1225 m13c3 m13c0 m13c2 m13c2 = refl
  holds1225 m13c3 m13c0 m13c2 m13c3 = refl
  holds1225 m13c3 m13c0 m13c3 m13c0 = refl
  holds1225 m13c3 m13c0 m13c3 m13c1 = refl
  holds1225 m13c3 m13c0 m13c3 m13c2 = refl
  holds1225 m13c3 m13c0 m13c3 m13c3 = refl
  holds1225 m13c3 m13c1 m13c0 m13c0 = refl
  holds1225 m13c3 m13c1 m13c0 m13c1 = refl
  holds1225 m13c3 m13c1 m13c0 m13c2 = refl
  holds1225 m13c3 m13c1 m13c0 m13c3 = refl
  holds1225 m13c3 m13c1 m13c1 m13c0 = refl
  holds1225 m13c3 m13c1 m13c1 m13c1 = refl
  holds1225 m13c3 m13c1 m13c1 m13c2 = refl
  holds1225 m13c3 m13c1 m13c1 m13c3 = refl
  holds1225 m13c3 m13c1 m13c2 m13c0 = refl
  holds1225 m13c3 m13c1 m13c2 m13c1 = refl
  holds1225 m13c3 m13c1 m13c2 m13c2 = refl
  holds1225 m13c3 m13c1 m13c2 m13c3 = refl
  holds1225 m13c3 m13c1 m13c3 m13c0 = refl
  holds1225 m13c3 m13c1 m13c3 m13c1 = refl
  holds1225 m13c3 m13c1 m13c3 m13c2 = refl
  holds1225 m13c3 m13c1 m13c3 m13c3 = refl
  holds1225 m13c3 m13c2 m13c0 m13c0 = refl
  holds1225 m13c3 m13c2 m13c0 m13c1 = refl
  holds1225 m13c3 m13c2 m13c0 m13c2 = refl
  holds1225 m13c3 m13c2 m13c0 m13c3 = refl
  holds1225 m13c3 m13c2 m13c1 m13c0 = refl
  holds1225 m13c3 m13c2 m13c1 m13c1 = refl
  holds1225 m13c3 m13c2 m13c1 m13c2 = refl
  holds1225 m13c3 m13c2 m13c1 m13c3 = refl
  holds1225 m13c3 m13c2 m13c2 m13c0 = refl
  holds1225 m13c3 m13c2 m13c2 m13c1 = refl
  holds1225 m13c3 m13c2 m13c2 m13c2 = refl
  holds1225 m13c3 m13c2 m13c2 m13c3 = refl
  holds1225 m13c3 m13c2 m13c3 m13c0 = refl
  holds1225 m13c3 m13c2 m13c3 m13c1 = refl
  holds1225 m13c3 m13c2 m13c3 m13c2 = refl
  holds1225 m13c3 m13c2 m13c3 m13c3 = refl
  holds1225 m13c3 m13c3 m13c0 m13c0 = refl
  holds1225 m13c3 m13c3 m13c0 m13c1 = refl
  holds1225 m13c3 m13c3 m13c0 m13c2 = refl
  holds1225 m13c3 m13c3 m13c0 m13c3 = refl
  holds1225 m13c3 m13c3 m13c1 m13c0 = refl
  holds1225 m13c3 m13c3 m13c1 m13c1 = refl
  holds1225 m13c3 m13c3 m13c1 m13c2 = refl
  holds1225 m13c3 m13c3 m13c1 m13c3 = refl
  holds1225 m13c3 m13c3 m13c2 m13c0 = refl
  holds1225 m13c3 m13c3 m13c2 m13c1 = refl
  holds1225 m13c3 m13c3 m13c2 m13c2 = refl
  holds1225 m13c3 m13c3 m13c2 m13c3 = refl
  holds1225 m13c3 m13c3 m13c3 m13c0 = refl
  holds1225 m13c3 m13c3 m13c3 m13c1 = refl
  holds1225 m13c3 m13c3 m13c3 m13c2 = refl
  holds1225 m13c3 m13c3 m13c3 m13c3 = refl
  cut1225 : (x6 : ℕ) → Adequate {ℓ} ((var 0) , (op (op (var 1) (op (op (var 2) (var 0)) (var 1))) (op (var 0) (var x6)))) → ⊥
  cut1225 x6 = reject13 ((var 0) , (op (op (var 1) (op (op (var 2) (var 0)) (var 1))) (op (var 0) (var x6)))) (λ env → holds1225 (env 0) (env 1) (env 2) (env x6))
  bad1226 : (z3 : Two) → PathP (λ _ → Two) b1 (bop (bop b0 (bop (bop b0 b1) b0)) (bop b0 z3)) → ⊥
  bad1226 z3 p = false≢true (sym (cong lower p))
  cut1226 : (x6 : ℕ) → Adequate {ℓ} ((var 0) , (op (op (var 1) (op (op (var 2) (var 0)) (var 1))) (op (var 1) (var x6)))) → ⊥
  cut1226 x6 adequate = bad1226 (env2 x6) (Adequate.valid adequate Two boolean env2)
  bad1227 : (z3 : Two) → PathP (λ _ → Two) b1 (bop (bop b0 (bop (bop b0 b1) b0)) (bop b0 z3)) → ⊥
  bad1227 z3 p = false≢true (sym (cong lower p))
  cut1227 : (x6 : ℕ) → Adequate {ℓ} ((var 0) , (op (op (var 1) (op (op (var 2) (var 0)) (var 1))) (op (var 2) (var x6)))) → ⊥
  cut1227 x6 adequate = bad1227 (env2 x6) (Adequate.valid adequate Two boolean env2)
  bad1228 : (z4 : Two) → PathP (λ _ → Two) b1 (bop (bop b0 (bop (bop b0 b1) b0)) (bop b0 z4)) → ⊥
  bad1228 z4 p = false≢true (sym (cong lower p))
  cut1228 : (x6 : ℕ) → Adequate {ℓ} ((var 0) , (op (op (var 1) (op (op (var 2) (var 0)) (var 1))) (op (var 3) (var x6)))) → ⊥
  cut1228 x6 adequate = bad1228 (env4 x6) (Adequate.valid adequate Two boolean env4)
  bad1229 : (z3 z4 : Two) → PathP (λ _ → Two) b0 (bop (bop b1 (bop (bop b0 b0) b0)) (bop z3 z4)) → ⊥
  bad1229 z3 z4 p = false≢true (cong lower p)
  cut1229 : (x5 x6 : ℕ) → Adequate {ℓ} ((var 0) , (op (op (var 1) (op (op (var 2) (var 0)) (var 2))) (op (var x5) (var x6)))) → ⊥
  cut1229 x5 x6 adequate = bad1229 (env3 x5) (env3 x6) (Adequate.valid adequate Two boolean env3)
  bad1230 : (z4 z5 : Two) → PathP (λ _ → Two) b0 (bop (bop b1 (bop (bop b0 b0) b0)) (bop z4 z5)) → ⊥
  bad1230 z4 z5 p = false≢true (cong lower p)
  cut1230 : (x5 x6 : ℕ) → Adequate {ℓ} ((var 0) , (op (op (var 1) (op (op (var 2) (var 0)) (var 3))) (op (var x5) (var x6)))) → ⊥
  cut1230 x5 x6 adequate = bad1230 (env5 x5) (env5 x6) (Adequate.valid adequate Two boolean env5)
  bad1231 : (z3 z4 z5 : Two) → PathP (λ _ → Two) b0 (bop (bop b1 (bop (bop b1 b1) z3)) (bop z4 z5)) → ⊥
  bad1231 z3 z4 z5 p = false≢true (cong lower p)
  cut1231 : (x4 x5 x6 : ℕ) → Adequate {ℓ} ((var 0) , (op (op (var 1) (op (op (var 2) (var 1)) (var x4))) (op (var x5) (var x6)))) → ⊥
  cut1231 x4 x5 x6 adequate = bad1231 (env6 x4) (env6 x5) (env6 x6) (Adequate.valid adequate Two boolean env6)
  bad1232 : (z3 z4 z5 : Two) → PathP (λ _ → Two) b0 (bop (bop b1 (bop (bop b1 b1) z3)) (bop z4 z5)) → ⊥
  bad1232 z3 z4 z5 p = false≢true (cong lower p)
  cut1232 : (x4 x5 x6 : ℕ) → Adequate {ℓ} ((var 0) , (op (op (var 1) (op (op (var 2) (var 2)) (var x4))) (op (var x5) (var x6)))) → ⊥
  cut1232 x4 x5 x6 adequate = bad1232 (env6 x4) (env6 x5) (env6 x6) (Adequate.valid adequate Two boolean env6)
  env7 : ℕ → Two
  env7 zero = b0
  env7 (suc zero) = b1
  env7 (suc (suc zero)) = b1
  env7 (suc (suc (suc zero))) = b1
  env7 (suc (suc (suc (suc rest)))) = b0
  bad1233 : (z4 z5 z6 : Two) → PathP (λ _ → Two) b0 (bop (bop b1 (bop (bop b1 b1) z4)) (bop z5 z6)) → ⊥
  bad1233 z4 z5 z6 p = false≢true (cong lower p)
  cut1233 : (x4 x5 x6 : ℕ) → Adequate {ℓ} ((var 0) , (op (op (var 1) (op (op (var 2) (var 3)) (var x4))) (op (var x5) (var x6)))) → ⊥
  cut1233 x4 x5 x6 adequate = bad1233 (env7 x4) (env7 x5) (env7 x6) (Adequate.valid adequate Two boolean env7)
