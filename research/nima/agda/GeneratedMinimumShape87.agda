{-# OPTIONS --safe --cubical --guardedness #-}
module GeneratedMinimumShape87 where
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
  holds1157 : (z0 z1 z2 z3 z4 z5 : A2) → z0 ≡ (mul2 (mul2 z0 (mul2 z1 (mul2 z2 z3))) (mul2 z4 z5))
  holds1157 z0 z1 z2 z3 z4 z5 = refl
  cut1157 : (x2 x3 x4 x5 x6 : ℕ) → Adequate {ℓ} ((var 0) , (op (op (var 0) (op (var x2) (op (var x3) (var x4)))) (op (var x5) (var x6)))) → ⊥
  cut1157 x2 x3 x4 x5 x6 = reject2 ((var 0) , (op (op (var 0) (op (var x2) (op (var x3) (var x4)))) (op (var x5) (var x6)))) (λ env → holds1157 (env 0) (env x2) (env x3) (env x4) (env x5) (env x6))
  env0 : ℕ → Two
  env0 zero = b0
  env0 (suc zero) = b1
  env0 (suc (suc rest)) = b0
  bad1158 : (z2 z3 z4 z5 : Two) → PathP (λ _ → Two) b0 (bop (bop b1 (bop b0 (bop z2 z3))) (bop z4 z5)) → ⊥
  bad1158 z2 z3 z4 z5 p = false≢true (cong lower p)
  cut1158 : (x3 x4 x5 x6 : ℕ) → Adequate {ℓ} ((var 0) , (op (op (var 1) (op (var 0) (op (var x3) (var x4)))) (op (var x5) (var x6)))) → ⊥
  cut1158 x3 x4 x5 x6 adequate = bad1158 (env0 x3) (env0 x4) (env0 x5) (env0 x6) (Adequate.valid adequate Two boolean env0)
  holds1159 : (z0 z1 : A3) → z0 ≡ (mul3 (mul3 z1 (mul3 z1 (mul3 z0 z0))) (mul3 z0 z0))
  holds1159 z0 z1 = refl
  cut1159 : Adequate {ℓ} ((var 0) , (op (op (var 1) (op (var 1) (op (var 0) (var 0)))) (op (var 0) (var 0)))) → ⊥
  cut1159  = reject3 ((var 0) , (op (op (var 1) (op (var 1) (op (var 0) (var 0)))) (op (var 0) (var 0)))) (λ env → holds1159 (env 0) (env 1))
  env1 : ℕ → Two
  env1 zero = b1
  env1 (suc zero) = b0
  env1 (suc (suc rest)) = b0
  bad1160 : PathP (λ _ → Two) b1 (bop (bop b0 (bop b0 (bop b1 b1))) (bop b1 b0)) → ⊥
  bad1160  p = false≢true (sym (cong lower p))
  cut1160 : Adequate {ℓ} ((var 0) , (op (op (var 1) (op (var 1) (op (var 0) (var 0)))) (op (var 0) (var 1)))) → ⊥
  cut1160  adequate = bad1160  (Adequate.valid adequate Two boolean env1)
  env2 : ℕ → Two
  env2 zero = b1
  env2 (suc zero) = b0
  env2 (suc (suc zero)) = b0
  env2 (suc (suc (suc rest))) = b0
  bad1161 : PathP (λ _ → Two) b1 (bop (bop b0 (bop b0 (bop b1 b1))) (bop b1 b0)) → ⊥
  bad1161  p = false≢true (sym (cong lower p))
  cut1161 : Adequate {ℓ} ((var 0) , (op (op (var 1) (op (var 1) (op (var 0) (var 0)))) (op (var 0) (var 2)))) → ⊥
  cut1161  adequate = bad1161  (Adequate.valid adequate Two boolean env2)
  bad1162 : (z2 : Two) → PathP (λ _ → Two) b1 (bop (bop b0 (bop b0 (bop b1 b1))) (bop b0 z2)) → ⊥
  bad1162 z2 p = false≢true (sym (cong lower p))
  cut1162 : (x6 : ℕ) → Adequate {ℓ} ((var 0) , (op (op (var 1) (op (var 1) (op (var 0) (var 0)))) (op (var 1) (var x6)))) → ⊥
  cut1162 x6 adequate = bad1162 (env1 x6) (Adequate.valid adequate Two boolean env1)
  bad1163 : (z3 : Two) → PathP (λ _ → Two) b1 (bop (bop b0 (bop b0 (bop b1 b1))) (bop b0 z3)) → ⊥
  bad1163 z3 p = false≢true (sym (cong lower p))
  cut1163 : (x6 : ℕ) → Adequate {ℓ} ((var 0) , (op (op (var 1) (op (var 1) (op (var 0) (var 0)))) (op (var 2) (var x6)))) → ⊥
  cut1163 x6 adequate = bad1163 (env2 x6) (Adequate.valid adequate Two boolean env2)
  holds1164 : (z0 z1 : A3) → z0 ≡ (mul3 (mul3 z1 (mul3 z1 (mul3 z0 z1))) (mul3 z0 z0))
  holds1164 z0 z1 = refl
  cut1164 : Adequate {ℓ} ((var 0) , (op (op (var 1) (op (var 1) (op (var 0) (var 1)))) (op (var 0) (var 0)))) → ⊥
  cut1164  = reject3 ((var 0) , (op (op (var 1) (op (var 1) (op (var 0) (var 1)))) (op (var 0) (var 0)))) (λ env → holds1164 (env 0) (env 1))
  bad1165 : PathP (λ _ → Two) b1 (bop (bop b0 (bop b0 (bop b1 b0))) (bop b1 b0)) → ⊥
  bad1165  p = false≢true (sym (cong lower p))
  cut1165 : Adequate {ℓ} ((var 0) , (op (op (var 1) (op (var 1) (op (var 0) (var 1)))) (op (var 0) (var 1)))) → ⊥
  cut1165  adequate = bad1165  (Adequate.valid adequate Two boolean env1)
  bad1166 : PathP (λ _ → Two) b1 (bop (bop b0 (bop b0 (bop b1 b0))) (bop b1 b0)) → ⊥
  bad1166  p = false≢true (sym (cong lower p))
  cut1166 : Adequate {ℓ} ((var 0) , (op (op (var 1) (op (var 1) (op (var 0) (var 1)))) (op (var 0) (var 2)))) → ⊥
  cut1166  adequate = bad1166  (Adequate.valid adequate Two boolean env2)
  bad1167 : (z2 : Two) → PathP (λ _ → Two) b1 (bop (bop b0 (bop b0 (bop b1 b0))) (bop b0 z2)) → ⊥
  bad1167 z2 p = false≢true (sym (cong lower p))
  cut1167 : (x6 : ℕ) → Adequate {ℓ} ((var 0) , (op (op (var 1) (op (var 1) (op (var 0) (var 1)))) (op (var 1) (var x6)))) → ⊥
  cut1167 x6 adequate = bad1167 (env1 x6) (Adequate.valid adequate Two boolean env1)
  bad1168 : (z3 : Two) → PathP (λ _ → Two) b1 (bop (bop b0 (bop b0 (bop b1 b0))) (bop b0 z3)) → ⊥
  bad1168 z3 p = false≢true (sym (cong lower p))
  cut1168 : (x6 : ℕ) → Adequate {ℓ} ((var 0) , (op (op (var 1) (op (var 1) (op (var 0) (var 1)))) (op (var 2) (var x6)))) → ⊥
  cut1168 x6 adequate = bad1168 (env2 x6) (Adequate.valid adequate Two boolean env2)
  holds1169 : (z0 z1 z2 : A3) → z0 ≡ (mul3 (mul3 z1 (mul3 z1 (mul3 z0 z2))) (mul3 z0 z0))
  holds1169 z0 z1 z2 = refl
  cut1169 : Adequate {ℓ} ((var 0) , (op (op (var 1) (op (var 1) (op (var 0) (var 2)))) (op (var 0) (var 0)))) → ⊥
  cut1169  = reject3 ((var 0) , (op (op (var 1) (op (var 1) (op (var 0) (var 2)))) (op (var 0) (var 0)))) (λ env → holds1169 (env 0) (env 1) (env 2))
  bad1170 : PathP (λ _ → Two) b1 (bop (bop b0 (bop b0 (bop b1 b0))) (bop b1 b0)) → ⊥
  bad1170  p = false≢true (sym (cong lower p))
  cut1170 : Adequate {ℓ} ((var 0) , (op (op (var 1) (op (var 1) (op (var 0) (var 2)))) (op (var 0) (var 1)))) → ⊥
  cut1170  adequate = bad1170  (Adequate.valid adequate Two boolean env2)
  bad1171 : PathP (λ _ → Two) b1 (bop (bop b0 (bop b0 (bop b1 b0))) (bop b1 b0)) → ⊥
  bad1171  p = false≢true (sym (cong lower p))
  cut1171 : Adequate {ℓ} ((var 0) , (op (op (var 1) (op (var 1) (op (var 0) (var 2)))) (op (var 0) (var 2)))) → ⊥
  cut1171  adequate = bad1171  (Adequate.valid adequate Two boolean env2)
  env3 : ℕ → Two
  env3 zero = b1
  env3 (suc zero) = b0
  env3 (suc (suc zero)) = b0
  env3 (suc (suc (suc zero))) = b0
  env3 (suc (suc (suc (suc rest)))) = b0
  bad1172 : PathP (λ _ → Two) b1 (bop (bop b0 (bop b0 (bop b1 b0))) (bop b1 b0)) → ⊥
  bad1172  p = false≢true (sym (cong lower p))
  cut1172 : Adequate {ℓ} ((var 0) , (op (op (var 1) (op (var 1) (op (var 0) (var 2)))) (op (var 0) (var 3)))) → ⊥
  cut1172  adequate = bad1172  (Adequate.valid adequate Two boolean env3)
  bad1173 : (z3 : Two) → PathP (λ _ → Two) b1 (bop (bop b0 (bop b0 (bop b1 b0))) (bop b0 z3)) → ⊥
  bad1173 z3 p = false≢true (sym (cong lower p))
  cut1173 : (x6 : ℕ) → Adequate {ℓ} ((var 0) , (op (op (var 1) (op (var 1) (op (var 0) (var 2)))) (op (var 1) (var x6)))) → ⊥
  cut1173 x6 adequate = bad1173 (env2 x6) (Adequate.valid adequate Two boolean env2)
  bad1174 : (z3 : Two) → PathP (λ _ → Two) b1 (bop (bop b0 (bop b0 (bop b1 b0))) (bop b0 z3)) → ⊥
  bad1174 z3 p = false≢true (sym (cong lower p))
  cut1174 : (x6 : ℕ) → Adequate {ℓ} ((var 0) , (op (op (var 1) (op (var 1) (op (var 0) (var 2)))) (op (var 2) (var x6)))) → ⊥
  cut1174 x6 adequate = bad1174 (env2 x6) (Adequate.valid adequate Two boolean env2)
  bad1175 : (z4 : Two) → PathP (λ _ → Two) b1 (bop (bop b0 (bop b0 (bop b1 b0))) (bop b0 z4)) → ⊥
  bad1175 z4 p = false≢true (sym (cong lower p))
  cut1175 : (x6 : ℕ) → Adequate {ℓ} ((var 0) , (op (op (var 1) (op (var 1) (op (var 0) (var 2)))) (op (var 3) (var x6)))) → ⊥
  cut1175 x6 adequate = bad1175 (env3 x6) (Adequate.valid adequate Two boolean env3)
  holds1176 : (z0 z1 : A3) → z0 ≡ (mul3 (mul3 z1 (mul3 z1 (mul3 z1 z0))) (mul3 z0 z0))
  holds1176 z0 z1 = refl
  cut1176 : Adequate {ℓ} ((var 0) , (op (op (var 1) (op (var 1) (op (var 1) (var 0)))) (op (var 0) (var 0)))) → ⊥
  cut1176  = reject3 ((var 0) , (op (op (var 1) (op (var 1) (op (var 1) (var 0)))) (op (var 0) (var 0)))) (λ env → holds1176 (env 0) (env 1))
  bad1177 : PathP (λ _ → Two) b1 (bop (bop b0 (bop b0 (bop b0 b1))) (bop b1 b0)) → ⊥
  bad1177  p = false≢true (sym (cong lower p))
  cut1177 : Adequate {ℓ} ((var 0) , (op (op (var 1) (op (var 1) (op (var 1) (var 0)))) (op (var 0) (var 1)))) → ⊥
  cut1177  adequate = bad1177  (Adequate.valid adequate Two boolean env1)
  bad1178 : PathP (λ _ → Two) b1 (bop (bop b0 (bop b0 (bop b0 b1))) (bop b1 b0)) → ⊥
  bad1178  p = false≢true (sym (cong lower p))
  cut1178 : Adequate {ℓ} ((var 0) , (op (op (var 1) (op (var 1) (op (var 1) (var 0)))) (op (var 0) (var 2)))) → ⊥
  cut1178  adequate = bad1178  (Adequate.valid adequate Two boolean env2)
  bad1179 : (z2 : Two) → PathP (λ _ → Two) b1 (bop (bop b0 (bop b0 (bop b0 b1))) (bop b0 z2)) → ⊥
  bad1179 z2 p = false≢true (sym (cong lower p))
  cut1179 : (x6 : ℕ) → Adequate {ℓ} ((var 0) , (op (op (var 1) (op (var 1) (op (var 1) (var 0)))) (op (var 1) (var x6)))) → ⊥
  cut1179 x6 adequate = bad1179 (env1 x6) (Adequate.valid adequate Two boolean env1)
  bad1180 : (z3 : Two) → PathP (λ _ → Two) b1 (bop (bop b0 (bop b0 (bop b0 b1))) (bop b0 z3)) → ⊥
  bad1180 z3 p = false≢true (sym (cong lower p))
  cut1180 : (x6 : ℕ) → Adequate {ℓ} ((var 0) , (op (op (var 1) (op (var 1) (op (var 1) (var 0)))) (op (var 2) (var x6)))) → ⊥
  cut1180 x6 adequate = bad1180 (env2 x6) (Adequate.valid adequate Two boolean env2)
  bad1181 : (z2 z3 : Two) → PathP (λ _ → Two) b0 (bop (bop b1 (bop b1 (bop b1 b1))) (bop z2 z3)) → ⊥
  bad1181 z2 z3 p = false≢true (cong lower p)
  cut1181 : (x5 x6 : ℕ) → Adequate {ℓ} ((var 0) , (op (op (var 1) (op (var 1) (op (var 1) (var 1)))) (op (var x5) (var x6)))) → ⊥
  cut1181 x5 x6 adequate = bad1181 (env0 x5) (env0 x6) (Adequate.valid adequate Two boolean env0)
  env4 : ℕ → Two
  env4 zero = b0
  env4 (suc zero) = b1
  env4 (suc (suc zero)) = b1
  env4 (suc (suc (suc rest))) = b0
  bad1182 : (z3 z4 : Two) → PathP (λ _ → Two) b0 (bop (bop b1 (bop b1 (bop b1 b1))) (bop z3 z4)) → ⊥
  bad1182 z3 z4 p = false≢true (cong lower p)
  cut1182 : (x5 x6 : ℕ) → Adequate {ℓ} ((var 0) , (op (op (var 1) (op (var 1) (op (var 1) (var 2)))) (op (var x5) (var x6)))) → ⊥
  cut1182 x5 x6 adequate = bad1182 (env4 x5) (env4 x6) (Adequate.valid adequate Two boolean env4)
  holds1183 : (z0 z1 z2 : A3) → z0 ≡ (mul3 (mul3 z1 (mul3 z1 (mul3 z2 z0))) (mul3 z0 z0))
  holds1183 z0 z1 z2 = refl
  cut1183 : Adequate {ℓ} ((var 0) , (op (op (var 1) (op (var 1) (op (var 2) (var 0)))) (op (var 0) (var 0)))) → ⊥
  cut1183  = reject3 ((var 0) , (op (op (var 1) (op (var 1) (op (var 2) (var 0)))) (op (var 0) (var 0)))) (λ env → holds1183 (env 0) (env 1) (env 2))
  bad1184 : PathP (λ _ → Two) b1 (bop (bop b0 (bop b0 (bop b0 b1))) (bop b1 b0)) → ⊥
  bad1184  p = false≢true (sym (cong lower p))
  cut1184 : Adequate {ℓ} ((var 0) , (op (op (var 1) (op (var 1) (op (var 2) (var 0)))) (op (var 0) (var 1)))) → ⊥
  cut1184  adequate = bad1184  (Adequate.valid adequate Two boolean env2)
  bad1185 : PathP (λ _ → Two) b1 (bop (bop b0 (bop b0 (bop b0 b1))) (bop b1 b0)) → ⊥
  bad1185  p = false≢true (sym (cong lower p))
  cut1185 : Adequate {ℓ} ((var 0) , (op (op (var 1) (op (var 1) (op (var 2) (var 0)))) (op (var 0) (var 2)))) → ⊥
  cut1185  adequate = bad1185  (Adequate.valid adequate Two boolean env2)
  bad1186 : PathP (λ _ → Two) b1 (bop (bop b0 (bop b0 (bop b0 b1))) (bop b1 b0)) → ⊥
  bad1186  p = false≢true (sym (cong lower p))
  cut1186 : Adequate {ℓ} ((var 0) , (op (op (var 1) (op (var 1) (op (var 2) (var 0)))) (op (var 0) (var 3)))) → ⊥
  cut1186  adequate = bad1186  (Adequate.valid adequate Two boolean env3)
  bad1187 : (z3 : Two) → PathP (λ _ → Two) b1 (bop (bop b0 (bop b0 (bop b0 b1))) (bop b0 z3)) → ⊥
  bad1187 z3 p = false≢true (sym (cong lower p))
  cut1187 : (x6 : ℕ) → Adequate {ℓ} ((var 0) , (op (op (var 1) (op (var 1) (op (var 2) (var 0)))) (op (var 1) (var x6)))) → ⊥
  cut1187 x6 adequate = bad1187 (env2 x6) (Adequate.valid adequate Two boolean env2)
  bad1188 : (z3 : Two) → PathP (λ _ → Two) b1 (bop (bop b0 (bop b0 (bop b0 b1))) (bop b0 z3)) → ⊥
  bad1188 z3 p = false≢true (sym (cong lower p))
  cut1188 : (x6 : ℕ) → Adequate {ℓ} ((var 0) , (op (op (var 1) (op (var 1) (op (var 2) (var 0)))) (op (var 2) (var x6)))) → ⊥
  cut1188 x6 adequate = bad1188 (env2 x6) (Adequate.valid adequate Two boolean env2)
  bad1189 : (z4 : Two) → PathP (λ _ → Two) b1 (bop (bop b0 (bop b0 (bop b0 b1))) (bop b0 z4)) → ⊥
  bad1189 z4 p = false≢true (sym (cong lower p))
  cut1189 : (x6 : ℕ) → Adequate {ℓ} ((var 0) , (op (op (var 1) (op (var 1) (op (var 2) (var 0)))) (op (var 3) (var x6)))) → ⊥
  cut1189 x6 adequate = bad1189 (env3 x6) (Adequate.valid adequate Two boolean env3)
  bad1190 : (z3 z4 : Two) → PathP (λ _ → Two) b0 (bop (bop b1 (bop b1 (bop b1 b1))) (bop z3 z4)) → ⊥
  bad1190 z3 z4 p = false≢true (cong lower p)
  cut1190 : (x5 x6 : ℕ) → Adequate {ℓ} ((var 0) , (op (op (var 1) (op (var 1) (op (var 2) (var 1)))) (op (var x5) (var x6)))) → ⊥
  cut1190 x5 x6 adequate = bad1190 (env4 x5) (env4 x6) (Adequate.valid adequate Two boolean env4)
  bad1191 : (z3 z4 : Two) → PathP (λ _ → Two) b0 (bop (bop b1 (bop b1 (bop b1 b1))) (bop z3 z4)) → ⊥
  bad1191 z3 z4 p = false≢true (cong lower p)
  cut1191 : (x5 x6 : ℕ) → Adequate {ℓ} ((var 0) , (op (op (var 1) (op (var 1) (op (var 2) (var 2)))) (op (var x5) (var x6)))) → ⊥
  cut1191 x5 x6 adequate = bad1191 (env4 x5) (env4 x6) (Adequate.valid adequate Two boolean env4)
  env5 : ℕ → Two
  env5 zero = b0
  env5 (suc zero) = b1
  env5 (suc (suc zero)) = b1
  env5 (suc (suc (suc zero))) = b1
  env5 (suc (suc (suc (suc rest)))) = b0
  bad1192 : (z4 z5 : Two) → PathP (λ _ → Two) b0 (bop (bop b1 (bop b1 (bop b1 b1))) (bop z4 z5)) → ⊥
  bad1192 z4 z5 p = false≢true (cong lower p)
  cut1192 : (x5 x6 : ℕ) → Adequate {ℓ} ((var 0) , (op (op (var 1) (op (var 1) (op (var 2) (var 3)))) (op (var x5) (var x6)))) → ⊥
  cut1192 x5 x6 adequate = bad1192 (env5 x5) (env5 x6) (Adequate.valid adequate Two boolean env5)
  env6 : ℕ → Two
  env6 zero = b0
  env6 (suc zero) = b1
  env6 (suc (suc zero)) = b0
  env6 (suc (suc (suc rest))) = b0
  bad1193 : (z3 z4 z5 z6 : Two) → PathP (λ _ → Two) b0 (bop (bop b1 (bop b0 (bop z3 z4))) (bop z5 z6)) → ⊥
  bad1193 z3 z4 z5 z6 p = false≢true (cong lower p)
  cut1193 : (x3 x4 x5 x6 : ℕ) → Adequate {ℓ} ((var 0) , (op (op (var 1) (op (var 2) (op (var x3) (var x4)))) (op (var x5) (var x6)))) → ⊥
  cut1193 x3 x4 x5 x6 adequate = bad1193 (env6 x3) (env6 x4) (env6 x5) (env6 x6) (Adequate.valid adequate Two boolean env6)
