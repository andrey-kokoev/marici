{-# OPTIONS --safe --cubical --guardedness #-}
module GeneratedMinimumShape82 where
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
  holds1072 : (z0 z1 z2 z3 z4 z5 : A2) → z0 ≡ (mul2 (mul2 z0 z1) (mul2 (mul2 (mul2 z2 z3) z4) z5))
  holds1072 z0 z1 z2 z3 z4 z5 = refl
  cut1072 : (x2 x3 x4 x5 x6 : ℕ) → Adequate {ℓ} ((var 0) , (op (op (var 0) (var x2)) (op (op (op (var x3) (var x4)) (var x5)) (var x6)))) → ⊥
  cut1072 x2 x3 x4 x5 x6 = reject2 ((var 0) , (op (op (var 0) (var x2)) (op (op (op (var x3) (var x4)) (var x5)) (var x6)))) (λ env → holds1072 (env 0) (env x2) (env x3) (env x4) (env x5) (env x6))
  holds1073 : (z0 z1 : A3) → z0 ≡ (mul3 (mul3 z1 z0) (mul3 (mul3 (mul3 z0 z0) z0) z0))
  holds1073 z0 z1 = refl
  cut1073 : Adequate {ℓ} ((var 0) , (op (op (var 1) (var 0)) (op (op (op (var 0) (var 0)) (var 0)) (var 0)))) → ⊥
  cut1073  = reject3 ((var 0) , (op (op (var 1) (var 0)) (op (op (op (var 0) (var 0)) (var 0)) (var 0)))) (λ env → holds1073 (env 0) (env 1))
  env0 : ℕ → Two
  env0 zero = b0
  env0 (suc zero) = b1
  env0 (suc (suc rest)) = b0
  bad1074 : PathP (λ _ → Two) b0 (bop (bop b1 b0) (bop (bop (bop b0 b0) b0) b1)) → ⊥
  bad1074  p = false≢true (cong lower p)
  cut1074 : Adequate {ℓ} ((var 0) , (op (op (var 1) (var 0)) (op (op (op (var 0) (var 0)) (var 0)) (var 1)))) → ⊥
  cut1074  adequate = bad1074  (Adequate.valid adequate Two boolean env0)
  env1 : ℕ → Two
  env1 zero = b0
  env1 (suc zero) = b0
  env1 (suc (suc zero)) = b1
  env1 (suc (suc (suc rest))) = b0
  bad1075 : PathP (λ _ → Two) b0 (bop (bop b0 b0) (bop (bop (bop b0 b0) b0) b1)) → ⊥
  bad1075  p = false≢true (cong lower p)
  cut1075 : Adequate {ℓ} ((var 0) , (op (op (var 1) (var 0)) (op (op (op (var 0) (var 0)) (var 0)) (var 2)))) → ⊥
  cut1075  adequate = bad1075  (Adequate.valid adequate Two boolean env1)
  holds1076 : (z0 z1 : A3) → z0 ≡ (mul3 (mul3 z1 z0) (mul3 (mul3 (mul3 z0 z0) z1) z0))
  holds1076 z0 z1 = refl
  cut1076 : Adequate {ℓ} ((var 0) , (op (op (var 1) (var 0)) (op (op (op (var 0) (var 0)) (var 1)) (var 0)))) → ⊥
  cut1076  = reject3 ((var 0) , (op (op (var 1) (var 0)) (op (op (op (var 0) (var 0)) (var 1)) (var 0)))) (λ env → holds1076 (env 0) (env 1))
  env2 : ℕ → Two
  env2 zero = b1
  env2 (suc zero) = b0
  env2 (suc (suc rest)) = b0
  bad1077 : PathP (λ _ → Two) b1 (bop (bop b0 b1) (bop (bop (bop b1 b1) b0) b0)) → ⊥
  bad1077  p = false≢true (sym (cong lower p))
  cut1077 : Adequate {ℓ} ((var 0) , (op (op (var 1) (var 0)) (op (op (op (var 0) (var 0)) (var 1)) (var 1)))) → ⊥
  cut1077  adequate = bad1077  (Adequate.valid adequate Two boolean env2)
  bad1078 : PathP (λ _ → Two) b0 (bop (bop b0 b0) (bop (bop (bop b0 b0) b0) b1)) → ⊥
  bad1078  p = false≢true (cong lower p)
  cut1078 : Adequate {ℓ} ((var 0) , (op (op (var 1) (var 0)) (op (op (op (var 0) (var 0)) (var 1)) (var 2)))) → ⊥
  cut1078  adequate = bad1078  (Adequate.valid adequate Two boolean env1)
  holds1079 : (z0 z1 z2 : A3) → z0 ≡ (mul3 (mul3 z1 z0) (mul3 (mul3 (mul3 z0 z0) z2) z0))
  holds1079 z0 z1 z2 = refl
  cut1079 : Adequate {ℓ} ((var 0) , (op (op (var 1) (var 0)) (op (op (op (var 0) (var 0)) (var 2)) (var 0)))) → ⊥
  cut1079  = reject3 ((var 0) , (op (op (var 1) (var 0)) (op (op (op (var 0) (var 0)) (var 2)) (var 0)))) (λ env → holds1079 (env 0) (env 1) (env 2))
  env3 : ℕ → Two
  env3 zero = b0
  env3 (suc zero) = b1
  env3 (suc (suc zero)) = b0
  env3 (suc (suc (suc rest))) = b0
  bad1080 : PathP (λ _ → Two) b0 (bop (bop b1 b0) (bop (bop (bop b0 b0) b0) b1)) → ⊥
  bad1080  p = false≢true (cong lower p)
  cut1080 : Adequate {ℓ} ((var 0) , (op (op (var 1) (var 0)) (op (op (op (var 0) (var 0)) (var 2)) (var 1)))) → ⊥
  cut1080  adequate = bad1080  (Adequate.valid adequate Two boolean env3)
  env4 : ℕ → Two
  env4 zero = b1
  env4 (suc zero) = b0
  env4 (suc (suc zero)) = b0
  env4 (suc (suc (suc rest))) = b0
  bad1081 : PathP (λ _ → Two) b1 (bop (bop b0 b1) (bop (bop (bop b1 b1) b0) b0)) → ⊥
  bad1081  p = false≢true (sym (cong lower p))
  cut1081 : Adequate {ℓ} ((var 0) , (op (op (var 1) (var 0)) (op (op (op (var 0) (var 0)) (var 2)) (var 2)))) → ⊥
  cut1081  adequate = bad1081  (Adequate.valid adequate Two boolean env4)
  env5 : ℕ → Two
  env5 zero = b0
  env5 (suc zero) = b0
  env5 (suc (suc zero)) = b0
  env5 (suc (suc (suc zero))) = b1
  env5 (suc (suc (suc (suc rest)))) = b0
  bad1082 : PathP (λ _ → Two) b0 (bop (bop b0 b0) (bop (bop (bop b0 b0) b0) b1)) → ⊥
  bad1082  p = false≢true (cong lower p)
  cut1082 : Adequate {ℓ} ((var 0) , (op (op (var 1) (var 0)) (op (op (op (var 0) (var 0)) (var 2)) (var 3)))) → ⊥
  cut1082  adequate = bad1082  (Adequate.valid adequate Two boolean env5)
  bad1083 : (z2 : Two) → PathP (λ _ → Two) b1 (bop (bop b0 b1) (bop (bop (bop b1 b0) b1) z2)) → ⊥
  bad1083 z2 p = false≢true (sym (cong lower p))
  cut1083 : (x6 : ℕ) → Adequate {ℓ} ((var 0) , (op (op (var 1) (var 0)) (op (op (op (var 0) (var 1)) (var 0)) (var x6)))) → ⊥
  cut1083 x6 adequate = bad1083 (env2 x6) (Adequate.valid adequate Two boolean env2)
  holds1084 : (z0 z1 : A3) → z0 ≡ (mul3 (mul3 z1 z0) (mul3 (mul3 (mul3 z0 z1) z1) z0))
  holds1084 z0 z1 = refl
  cut1084 : Adequate {ℓ} ((var 0) , (op (op (var 1) (var 0)) (op (op (op (var 0) (var 1)) (var 1)) (var 0)))) → ⊥
  cut1084  = reject3 ((var 0) , (op (op (var 1) (var 0)) (op (op (op (var 0) (var 1)) (var 1)) (var 0)))) (λ env → holds1084 (env 0) (env 1))
  bad1085 : PathP (λ _ → Two) b1 (bop (bop b0 b1) (bop (bop (bop b1 b0) b0) b0)) → ⊥
  bad1085  p = false≢true (sym (cong lower p))
  cut1085 : Adequate {ℓ} ((var 0) , (op (op (var 1) (var 0)) (op (op (op (var 0) (var 1)) (var 1)) (var 1)))) → ⊥
  cut1085  adequate = bad1085  (Adequate.valid adequate Two boolean env2)
  bad1086 : PathP (λ _ → Two) b0 (bop (bop b0 b0) (bop (bop (bop b0 b0) b0) b1)) → ⊥
  bad1086  p = false≢true (cong lower p)
  cut1086 : Adequate {ℓ} ((var 0) , (op (op (var 1) (var 0)) (op (op (op (var 0) (var 1)) (var 1)) (var 2)))) → ⊥
  cut1086  adequate = bad1086  (Adequate.valid adequate Two boolean env1)
  env6 : ℕ → Two
  env6 zero = b1
  env6 (suc zero) = b0
  env6 (suc (suc zero)) = b1
  env6 (suc (suc (suc rest))) = b0
  bad1087 : (z3 : Two) → PathP (λ _ → Two) b1 (bop (bop b0 b1) (bop (bop (bop b1 b0) b1) z3)) → ⊥
  bad1087 z3 p = false≢true (sym (cong lower p))
  cut1087 : (x6 : ℕ) → Adequate {ℓ} ((var 0) , (op (op (var 1) (var 0)) (op (op (op (var 0) (var 1)) (var 2)) (var x6)))) → ⊥
  cut1087 x6 adequate = bad1087 (env6 x6) (Adequate.valid adequate Two boolean env6)
  bad1088 : (z3 : Two) → PathP (λ _ → Two) b1 (bop (bop b0 b1) (bop (bop (bop b1 b0) b1) z3)) → ⊥
  bad1088 z3 p = false≢true (sym (cong lower p))
  cut1088 : (x6 : ℕ) → Adequate {ℓ} ((var 0) , (op (op (var 1) (var 0)) (op (op (op (var 0) (var 2)) (var 0)) (var x6)))) → ⊥
  cut1088 x6 adequate = bad1088 (env4 x6) (Adequate.valid adequate Two boolean env4)
  holds1089 : (z0 z1 z2 : A3) → z0 ≡ (mul3 (mul3 z1 z0) (mul3 (mul3 (mul3 z0 z2) z1) z0))
  holds1089 z0 z1 z2 = refl
  cut1089 : Adequate {ℓ} ((var 0) , (op (op (var 1) (var 0)) (op (op (op (var 0) (var 2)) (var 1)) (var 0)))) → ⊥
  cut1089  = reject3 ((var 0) , (op (op (var 1) (var 0)) (op (op (op (var 0) (var 2)) (var 1)) (var 0)))) (λ env → holds1089 (env 0) (env 1) (env 2))
  bad1090 : PathP (λ _ → Two) b1 (bop (bop b0 b1) (bop (bop (bop b1 b0) b0) b0)) → ⊥
  bad1090  p = false≢true (sym (cong lower p))
  cut1090 : Adequate {ℓ} ((var 0) , (op (op (var 1) (var 0)) (op (op (op (var 0) (var 2)) (var 1)) (var 1)))) → ⊥
  cut1090  adequate = bad1090  (Adequate.valid adequate Two boolean env4)
  bad1091 : PathP (λ _ → Two) b0 (bop (bop b0 b0) (bop (bop (bop b0 b1) b0) b1)) → ⊥
  bad1091  p = false≢true (cong lower p)
  cut1091 : Adequate {ℓ} ((var 0) , (op (op (var 1) (var 0)) (op (op (op (var 0) (var 2)) (var 1)) (var 2)))) → ⊥
  cut1091  adequate = bad1091  (Adequate.valid adequate Two boolean env1)
  bad1092 : PathP (λ _ → Two) b0 (bop (bop b0 b0) (bop (bop (bop b0 b0) b0) b1)) → ⊥
  bad1092  p = false≢true (cong lower p)
  cut1092 : Adequate {ℓ} ((var 0) , (op (op (var 1) (var 0)) (op (op (op (var 0) (var 2)) (var 1)) (var 3)))) → ⊥
  cut1092  adequate = bad1092  (Adequate.valid adequate Two boolean env5)
  holds1093 : (z0 z1 z2 : A3) → z0 ≡ (mul3 (mul3 z1 z0) (mul3 (mul3 (mul3 z0 z2) z2) z0))
  holds1093 z0 z1 z2 = refl
  cut1093 : Adequate {ℓ} ((var 0) , (op (op (var 1) (var 0)) (op (op (op (var 0) (var 2)) (var 2)) (var 0)))) → ⊥
  cut1093  = reject3 ((var 0) , (op (op (var 1) (var 0)) (op (op (op (var 0) (var 2)) (var 2)) (var 0)))) (λ env → holds1093 (env 0) (env 1) (env 2))
  bad1094 : PathP (λ _ → Two) b0 (bop (bop b1 b0) (bop (bop (bop b0 b0) b0) b1)) → ⊥
  bad1094  p = false≢true (cong lower p)
  cut1094 : Adequate {ℓ} ((var 0) , (op (op (var 1) (var 0)) (op (op (op (var 0) (var 2)) (var 2)) (var 1)))) → ⊥
  cut1094  adequate = bad1094  (Adequate.valid adequate Two boolean env3)
  bad1095 : PathP (λ _ → Two) b1 (bop (bop b0 b1) (bop (bop (bop b1 b0) b0) b0)) → ⊥
  bad1095  p = false≢true (sym (cong lower p))
  cut1095 : Adequate {ℓ} ((var 0) , (op (op (var 1) (var 0)) (op (op (op (var 0) (var 2)) (var 2)) (var 2)))) → ⊥
  cut1095  adequate = bad1095  (Adequate.valid adequate Two boolean env4)
  bad1096 : PathP (λ _ → Two) b0 (bop (bop b0 b0) (bop (bop (bop b0 b0) b0) b1)) → ⊥
  bad1096  p = false≢true (cong lower p)
  cut1096 : Adequate {ℓ} ((var 0) , (op (op (var 1) (var 0)) (op (op (op (var 0) (var 2)) (var 2)) (var 3)))) → ⊥
  cut1096  adequate = bad1096  (Adequate.valid adequate Two boolean env5)
  env7 : ℕ → Two
  env7 zero = b1
  env7 (suc zero) = b0
  env7 (suc (suc zero)) = b0
  env7 (suc (suc (suc zero))) = b1
  env7 (suc (suc (suc (suc rest)))) = b0
  bad1097 : (z4 : Two) → PathP (λ _ → Two) b1 (bop (bop b0 b1) (bop (bop (bop b1 b0) b1) z4)) → ⊥
  bad1097 z4 p = false≢true (sym (cong lower p))
  cut1097 : (x6 : ℕ) → Adequate {ℓ} ((var 0) , (op (op (var 1) (var 0)) (op (op (op (var 0) (var 2)) (var 3)) (var x6)))) → ⊥
  cut1097 x6 adequate = bad1097 (env7 x6) (Adequate.valid adequate Two boolean env7)
  bad1098 : (z2 : Two) → PathP (λ _ → Two) b1 (bop (bop b0 b1) (bop (bop (bop b0 b1) b1) z2)) → ⊥
  bad1098 z2 p = false≢true (sym (cong lower p))
  cut1098 : (x6 : ℕ) → Adequate {ℓ} ((var 0) , (op (op (var 1) (var 0)) (op (op (op (var 1) (var 0)) (var 0)) (var x6)))) → ⊥
  cut1098 x6 adequate = bad1098 (env2 x6) (Adequate.valid adequate Two boolean env2)
  holds1099 : (z0 z1 : A3) → z0 ≡ (mul3 (mul3 z1 z0) (mul3 (mul3 (mul3 z1 z0) z1) z0))
  holds1099 z0 z1 = refl
  cut1099 : Adequate {ℓ} ((var 0) , (op (op (var 1) (var 0)) (op (op (op (var 1) (var 0)) (var 1)) (var 0)))) → ⊥
  cut1099  = reject3 ((var 0) , (op (op (var 1) (var 0)) (op (op (op (var 1) (var 0)) (var 1)) (var 0)))) (λ env → holds1099 (env 0) (env 1))
  bad1100 : PathP (λ _ → Two) b1 (bop (bop b0 b1) (bop (bop (bop b0 b1) b0) b0)) → ⊥
  bad1100  p = false≢true (sym (cong lower p))
  cut1100 : Adequate {ℓ} ((var 0) , (op (op (var 1) (var 0)) (op (op (op (var 1) (var 0)) (var 1)) (var 1)))) → ⊥
  cut1100  adequate = bad1100  (Adequate.valid adequate Two boolean env2)
  bad1101 : PathP (λ _ → Two) b0 (bop (bop b0 b0) (bop (bop (bop b0 b0) b0) b1)) → ⊥
  bad1101  p = false≢true (cong lower p)
  cut1101 : Adequate {ℓ} ((var 0) , (op (op (var 1) (var 0)) (op (op (op (var 1) (var 0)) (var 1)) (var 2)))) → ⊥
  cut1101  adequate = bad1101  (Adequate.valid adequate Two boolean env1)
  bad1102 : (z3 : Two) → PathP (λ _ → Two) b1 (bop (bop b0 b1) (bop (bop (bop b0 b1) b1) z3)) → ⊥
  bad1102 z3 p = false≢true (sym (cong lower p))
  cut1102 : (x6 : ℕ) → Adequate {ℓ} ((var 0) , (op (op (var 1) (var 0)) (op (op (op (var 1) (var 0)) (var 2)) (var x6)))) → ⊥
  cut1102 x6 adequate = bad1102 (env6 x6) (Adequate.valid adequate Two boolean env6)
  bad1103 : (z2 : Two) → PathP (λ _ → Two) b1 (bop (bop b0 b1) (bop (bop (bop b0 b0) b1) z2)) → ⊥
  bad1103 z2 p = false≢true (sym (cong lower p))
  cut1103 : (x6 : ℕ) → Adequate {ℓ} ((var 0) , (op (op (var 1) (var 0)) (op (op (op (var 1) (var 1)) (var 0)) (var x6)))) → ⊥
  cut1103 x6 adequate = bad1103 (env2 x6) (Adequate.valid adequate Two boolean env2)
  holds1104 : (z0 z1 : A3) → z0 ≡ (mul3 (mul3 z1 z0) (mul3 (mul3 (mul3 z1 z1) z1) z0))
  holds1104 z0 z1 = refl
  cut1104 : Adequate {ℓ} ((var 0) , (op (op (var 1) (var 0)) (op (op (op (var 1) (var 1)) (var 1)) (var 0)))) → ⊥
  cut1104  = reject3 ((var 0) , (op (op (var 1) (var 0)) (op (op (op (var 1) (var 1)) (var 1)) (var 0)))) (λ env → holds1104 (env 0) (env 1))
  bad1105 : PathP (λ _ → Two) b0 (bop (bop b1 b0) (bop (bop (bop b1 b1) b1) b1)) → ⊥
  bad1105  p = false≢true (cong lower p)
  cut1105 : Adequate {ℓ} ((var 0) , (op (op (var 1) (var 0)) (op (op (op (var 1) (var 1)) (var 1)) (var 1)))) → ⊥
  cut1105  adequate = bad1105  (Adequate.valid adequate Two boolean env0)
  bad1106 : PathP (λ _ → Two) b0 (bop (bop b0 b0) (bop (bop (bop b0 b0) b0) b1)) → ⊥
  bad1106  p = false≢true (cong lower p)
  cut1106 : Adequate {ℓ} ((var 0) , (op (op (var 1) (var 0)) (op (op (op (var 1) (var 1)) (var 1)) (var 2)))) → ⊥
  cut1106  adequate = bad1106  (Adequate.valid adequate Two boolean env1)
  bad1107 : (z3 : Two) → PathP (λ _ → Two) b1 (bop (bop b0 b1) (bop (bop (bop b0 b0) b1) z3)) → ⊥
  bad1107 z3 p = false≢true (sym (cong lower p))
  cut1107 : (x6 : ℕ) → Adequate {ℓ} ((var 0) , (op (op (var 1) (var 0)) (op (op (op (var 1) (var 1)) (var 2)) (var x6)))) → ⊥
  cut1107 x6 adequate = bad1107 (env6 x6) (Adequate.valid adequate Two boolean env6)
  bad1108 : (z3 : Two) → PathP (λ _ → Two) b1 (bop (bop b0 b1) (bop (bop (bop b0 b0) b1) z3)) → ⊥
  bad1108 z3 p = false≢true (sym (cong lower p))
  cut1108 : (x6 : ℕ) → Adequate {ℓ} ((var 0) , (op (op (var 1) (var 0)) (op (op (op (var 1) (var 2)) (var 0)) (var x6)))) → ⊥
  cut1108 x6 adequate = bad1108 (env4 x6) (Adequate.valid adequate Two boolean env4)
  holds1109 : (z0 z1 z2 : A3) → z0 ≡ (mul3 (mul3 z1 z0) (mul3 (mul3 (mul3 z1 z2) z1) z0))
  holds1109 z0 z1 z2 = refl
  cut1109 : Adequate {ℓ} ((var 0) , (op (op (var 1) (var 0)) (op (op (op (var 1) (var 2)) (var 1)) (var 0)))) → ⊥
  cut1109  = reject3 ((var 0) , (op (op (var 1) (var 0)) (op (op (op (var 1) (var 2)) (var 1)) (var 0)))) (λ env → holds1109 (env 0) (env 1) (env 2))
  env8 : ℕ → Two
  env8 zero = b0
  env8 (suc zero) = b1
  env8 (suc (suc zero)) = b1
  env8 (suc (suc (suc rest))) = b0
  bad1110 : PathP (λ _ → Two) b0 (bop (bop b1 b0) (bop (bop (bop b1 b1) b1) b1)) → ⊥
  bad1110  p = false≢true (cong lower p)
  cut1110 : Adequate {ℓ} ((var 0) , (op (op (var 1) (var 0)) (op (op (op (var 1) (var 2)) (var 1)) (var 1)))) → ⊥
  cut1110  adequate = bad1110  (Adequate.valid adequate Two boolean env8)
  bad1111 : PathP (λ _ → Two) b0 (bop (bop b0 b0) (bop (bop (bop b0 b1) b0) b1)) → ⊥
  bad1111  p = false≢true (cong lower p)
  cut1111 : Adequate {ℓ} ((var 0) , (op (op (var 1) (var 0)) (op (op (op (var 1) (var 2)) (var 1)) (var 2)))) → ⊥
  cut1111  adequate = bad1111  (Adequate.valid adequate Two boolean env1)
  bad1112 : PathP (λ _ → Two) b0 (bop (bop b0 b0) (bop (bop (bop b0 b0) b0) b1)) → ⊥
  bad1112  p = false≢true (cong lower p)
  cut1112 : Adequate {ℓ} ((var 0) , (op (op (var 1) (var 0)) (op (op (op (var 1) (var 2)) (var 1)) (var 3)))) → ⊥
  cut1112  adequate = bad1112  (Adequate.valid adequate Two boolean env5)
  bad1113 : (z3 : Two) → PathP (λ _ → Two) b1 (bop (bop b0 b1) (bop (bop (bop b0 b1) b1) z3)) → ⊥
  bad1113 z3 p = false≢true (sym (cong lower p))
  cut1113 : (x6 : ℕ) → Adequate {ℓ} ((var 0) , (op (op (var 1) (var 0)) (op (op (op (var 1) (var 2)) (var 2)) (var x6)))) → ⊥
  cut1113 x6 adequate = bad1113 (env6 x6) (Adequate.valid adequate Two boolean env6)
  bad1114 : (z4 : Two) → PathP (λ _ → Two) b1 (bop (bop b0 b1) (bop (bop (bop b0 b0) b1) z4)) → ⊥
  bad1114 z4 p = false≢true (sym (cong lower p))
  cut1114 : (x6 : ℕ) → Adequate {ℓ} ((var 0) , (op (op (var 1) (var 0)) (op (op (op (var 1) (var 2)) (var 3)) (var x6)))) → ⊥
  cut1114 x6 adequate = bad1114 (env7 x6) (Adequate.valid adequate Two boolean env7)
  bad1115 : (z3 : Two) → PathP (λ _ → Two) b1 (bop (bop b0 b1) (bop (bop (bop b0 b1) b1) z3)) → ⊥
  bad1115 z3 p = false≢true (sym (cong lower p))
  cut1115 : (x6 : ℕ) → Adequate {ℓ} ((var 0) , (op (op (var 1) (var 0)) (op (op (op (var 2) (var 0)) (var 0)) (var x6)))) → ⊥
  cut1115 x6 adequate = bad1115 (env4 x6) (Adequate.valid adequate Two boolean env4)
  holds1116 : (z0 z1 z2 : A3) → z0 ≡ (mul3 (mul3 z1 z0) (mul3 (mul3 (mul3 z2 z0) z1) z0))
  holds1116 z0 z1 z2 = refl
  cut1116 : Adequate {ℓ} ((var 0) , (op (op (var 1) (var 0)) (op (op (op (var 2) (var 0)) (var 1)) (var 0)))) → ⊥
  cut1116  = reject3 ((var 0) , (op (op (var 1) (var 0)) (op (op (op (var 2) (var 0)) (var 1)) (var 0)))) (λ env → holds1116 (env 0) (env 1) (env 2))
  bad1117 : PathP (λ _ → Two) b1 (bop (bop b0 b1) (bop (bop (bop b0 b1) b0) b0)) → ⊥
  bad1117  p = false≢true (sym (cong lower p))
  cut1117 : Adequate {ℓ} ((var 0) , (op (op (var 1) (var 0)) (op (op (op (var 2) (var 0)) (var 1)) (var 1)))) → ⊥
  cut1117  adequate = bad1117  (Adequate.valid adequate Two boolean env4)
  bad1118 : PathP (λ _ → Two) b0 (bop (bop b0 b0) (bop (bop (bop b1 b0) b0) b1)) → ⊥
  bad1118  p = false≢true (cong lower p)
  cut1118 : Adequate {ℓ} ((var 0) , (op (op (var 1) (var 0)) (op (op (op (var 2) (var 0)) (var 1)) (var 2)))) → ⊥
  cut1118  adequate = bad1118  (Adequate.valid adequate Two boolean env1)
  bad1119 : PathP (λ _ → Two) b0 (bop (bop b0 b0) (bop (bop (bop b0 b0) b0) b1)) → ⊥
  bad1119  p = false≢true (cong lower p)
  cut1119 : Adequate {ℓ} ((var 0) , (op (op (var 1) (var 0)) (op (op (op (var 2) (var 0)) (var 1)) (var 3)))) → ⊥
  cut1119  adequate = bad1119  (Adequate.valid adequate Two boolean env5)
  holds1120 : (z0 z1 z2 : A3) → z0 ≡ (mul3 (mul3 z1 z0) (mul3 (mul3 (mul3 z2 z0) z2) z0))
  holds1120 z0 z1 z2 = refl
  cut1120 : Adequate {ℓ} ((var 0) , (op (op (var 1) (var 0)) (op (op (op (var 2) (var 0)) (var 2)) (var 0)))) → ⊥
  cut1120  = reject3 ((var 0) , (op (op (var 1) (var 0)) (op (op (op (var 2) (var 0)) (var 2)) (var 0)))) (λ env → holds1120 (env 0) (env 1) (env 2))
  bad1121 : PathP (λ _ → Two) b0 (bop (bop b1 b0) (bop (bop (bop b0 b0) b0) b1)) → ⊥
  bad1121  p = false≢true (cong lower p)
  cut1121 : Adequate {ℓ} ((var 0) , (op (op (var 1) (var 0)) (op (op (op (var 2) (var 0)) (var 2)) (var 1)))) → ⊥
  cut1121  adequate = bad1121  (Adequate.valid adequate Two boolean env3)
  bad1122 : PathP (λ _ → Two) b1 (bop (bop b0 b1) (bop (bop (bop b0 b1) b0) b0)) → ⊥
  bad1122  p = false≢true (sym (cong lower p))
  cut1122 : Adequate {ℓ} ((var 0) , (op (op (var 1) (var 0)) (op (op (op (var 2) (var 0)) (var 2)) (var 2)))) → ⊥
  cut1122  adequate = bad1122  (Adequate.valid adequate Two boolean env4)
  bad1123 : PathP (λ _ → Two) b0 (bop (bop b0 b0) (bop (bop (bop b0 b0) b0) b1)) → ⊥
  bad1123  p = false≢true (cong lower p)
  cut1123 : Adequate {ℓ} ((var 0) , (op (op (var 1) (var 0)) (op (op (op (var 2) (var 0)) (var 2)) (var 3)))) → ⊥
  cut1123  adequate = bad1123  (Adequate.valid adequate Two boolean env5)
  bad1124 : (z4 : Two) → PathP (λ _ → Two) b1 (bop (bop b0 b1) (bop (bop (bop b0 b1) b1) z4)) → ⊥
  bad1124 z4 p = false≢true (sym (cong lower p))
  cut1124 : (x6 : ℕ) → Adequate {ℓ} ((var 0) , (op (op (var 1) (var 0)) (op (op (op (var 2) (var 0)) (var 3)) (var x6)))) → ⊥
  cut1124 x6 adequate = bad1124 (env7 x6) (Adequate.valid adequate Two boolean env7)
  bad1125 : (z3 : Two) → PathP (λ _ → Two) b1 (bop (bop b0 b1) (bop (bop (bop b0 b0) b1) z3)) → ⊥
  bad1125 z3 p = false≢true (sym (cong lower p))
  cut1125 : (x6 : ℕ) → Adequate {ℓ} ((var 0) , (op (op (var 1) (var 0)) (op (op (op (var 2) (var 1)) (var 0)) (var x6)))) → ⊥
  cut1125 x6 adequate = bad1125 (env4 x6) (Adequate.valid adequate Two boolean env4)
  holds1126 : (z0 z1 z2 : A3) → z0 ≡ (mul3 (mul3 z1 z0) (mul3 (mul3 (mul3 z2 z1) z1) z0))
  holds1126 z0 z1 z2 = refl
  cut1126 : Adequate {ℓ} ((var 0) , (op (op (var 1) (var 0)) (op (op (op (var 2) (var 1)) (var 1)) (var 0)))) → ⊥
  cut1126  = reject3 ((var 0) , (op (op (var 1) (var 0)) (op (op (op (var 2) (var 1)) (var 1)) (var 0)))) (λ env → holds1126 (env 0) (env 1) (env 2))
  bad1127 : PathP (λ _ → Two) b0 (bop (bop b1 b0) (bop (bop (bop b1 b1) b1) b1)) → ⊥
  bad1127  p = false≢true (cong lower p)
  cut1127 : Adequate {ℓ} ((var 0) , (op (op (var 1) (var 0)) (op (op (op (var 2) (var 1)) (var 1)) (var 1)))) → ⊥
  cut1127  adequate = bad1127  (Adequate.valid adequate Two boolean env8)
  bad1128 : PathP (λ _ → Two) b0 (bop (bop b0 b0) (bop (bop (bop b1 b0) b0) b1)) → ⊥
  bad1128  p = false≢true (cong lower p)
  cut1128 : Adequate {ℓ} ((var 0) , (op (op (var 1) (var 0)) (op (op (op (var 2) (var 1)) (var 1)) (var 2)))) → ⊥
  cut1128  adequate = bad1128  (Adequate.valid adequate Two boolean env1)
  bad1129 : PathP (λ _ → Two) b0 (bop (bop b0 b0) (bop (bop (bop b0 b0) b0) b1)) → ⊥
  bad1129  p = false≢true (cong lower p)
  cut1129 : Adequate {ℓ} ((var 0) , (op (op (var 1) (var 0)) (op (op (op (var 2) (var 1)) (var 1)) (var 3)))) → ⊥
  cut1129  adequate = bad1129  (Adequate.valid adequate Two boolean env5)
  bad1130 : (z3 : Two) → PathP (λ _ → Two) b1 (bop (bop b0 b1) (bop (bop (bop b1 b0) b1) z3)) → ⊥
  bad1130 z3 p = false≢true (sym (cong lower p))
  cut1130 : (x6 : ℕ) → Adequate {ℓ} ((var 0) , (op (op (var 1) (var 0)) (op (op (op (var 2) (var 1)) (var 2)) (var x6)))) → ⊥
  cut1130 x6 adequate = bad1130 (env6 x6) (Adequate.valid adequate Two boolean env6)
  bad1131 : (z4 : Two) → PathP (λ _ → Two) b1 (bop (bop b0 b1) (bop (bop (bop b0 b0) b1) z4)) → ⊥
  bad1131 z4 p = false≢true (sym (cong lower p))
  cut1131 : (x6 : ℕ) → Adequate {ℓ} ((var 0) , (op (op (var 1) (var 0)) (op (op (op (var 2) (var 1)) (var 3)) (var x6)))) → ⊥
  cut1131 x6 adequate = bad1131 (env7 x6) (Adequate.valid adequate Two boolean env7)
  bad1132 : (z3 : Two) → PathP (λ _ → Two) b1 (bop (bop b0 b1) (bop (bop (bop b0 b0) b1) z3)) → ⊥
  bad1132 z3 p = false≢true (sym (cong lower p))
  cut1132 : (x6 : ℕ) → Adequate {ℓ} ((var 0) , (op (op (var 1) (var 0)) (op (op (op (var 2) (var 2)) (var 0)) (var x6)))) → ⊥
  cut1132 x6 adequate = bad1132 (env4 x6) (Adequate.valid adequate Two boolean env4)
  holds1133 : (z0 z1 z2 : A3) → z0 ≡ (mul3 (mul3 z1 z0) (mul3 (mul3 (mul3 z2 z2) z1) z0))
  holds1133 z0 z1 z2 = refl
  cut1133 : Adequate {ℓ} ((var 0) , (op (op (var 1) (var 0)) (op (op (op (var 2) (var 2)) (var 1)) (var 0)))) → ⊥
  cut1133  = reject3 ((var 0) , (op (op (var 1) (var 0)) (op (op (op (var 2) (var 2)) (var 1)) (var 0)))) (λ env → holds1133 (env 0) (env 1) (env 2))
  bad1134 : PathP (λ _ → Two) b0 (bop (bop b1 b0) (bop (bop (bop b1 b1) b1) b1)) → ⊥
  bad1134  p = false≢true (cong lower p)
  cut1134 : Adequate {ℓ} ((var 0) , (op (op (var 1) (var 0)) (op (op (op (var 2) (var 2)) (var 1)) (var 1)))) → ⊥
  cut1134  adequate = bad1134  (Adequate.valid adequate Two boolean env8)
  bad1135 : PathP (λ _ → Two) b0 (bop (bop b0 b0) (bop (bop (bop b1 b1) b0) b1)) → ⊥
  bad1135  p = false≢true (cong lower p)
  cut1135 : Adequate {ℓ} ((var 0) , (op (op (var 1) (var 0)) (op (op (op (var 2) (var 2)) (var 1)) (var 2)))) → ⊥
  cut1135  adequate = bad1135  (Adequate.valid adequate Two boolean env1)
  bad1136 : PathP (λ _ → Two) b0 (bop (bop b0 b0) (bop (bop (bop b0 b0) b0) b1)) → ⊥
  bad1136  p = false≢true (cong lower p)
  cut1136 : Adequate {ℓ} ((var 0) , (op (op (var 1) (var 0)) (op (op (op (var 2) (var 2)) (var 1)) (var 3)))) → ⊥
  cut1136  adequate = bad1136  (Adequate.valid adequate Two boolean env5)
  holds1137 : (z0 z1 z2 : A3) → z0 ≡ (mul3 (mul3 z1 z0) (mul3 (mul3 (mul3 z2 z2) z2) z0))
  holds1137 z0 z1 z2 = refl
  cut1137 : Adequate {ℓ} ((var 0) , (op (op (var 1) (var 0)) (op (op (op (var 2) (var 2)) (var 2)) (var 0)))) → ⊥
  cut1137  = reject3 ((var 0) , (op (op (var 1) (var 0)) (op (op (op (var 2) (var 2)) (var 2)) (var 0)))) (λ env → holds1137 (env 0) (env 1) (env 2))
  bad1138 : PathP (λ _ → Two) b0 (bop (bop b1 b0) (bop (bop (bop b0 b0) b0) b1)) → ⊥
  bad1138  p = false≢true (cong lower p)
  cut1138 : Adequate {ℓ} ((var 0) , (op (op (var 1) (var 0)) (op (op (op (var 2) (var 2)) (var 2)) (var 1)))) → ⊥
  cut1138  adequate = bad1138  (Adequate.valid adequate Two boolean env3)
  bad1139 : PathP (λ _ → Two) b0 (bop (bop b0 b0) (bop (bop (bop b1 b1) b1) b1)) → ⊥
  bad1139  p = false≢true (cong lower p)
  cut1139 : Adequate {ℓ} ((var 0) , (op (op (var 1) (var 0)) (op (op (op (var 2) (var 2)) (var 2)) (var 2)))) → ⊥
  cut1139  adequate = bad1139  (Adequate.valid adequate Two boolean env1)
  bad1140 : PathP (λ _ → Two) b0 (bop (bop b0 b0) (bop (bop (bop b0 b0) b0) b1)) → ⊥
  bad1140  p = false≢true (cong lower p)
  cut1140 : Adequate {ℓ} ((var 0) , (op (op (var 1) (var 0)) (op (op (op (var 2) (var 2)) (var 2)) (var 3)))) → ⊥
  cut1140  adequate = bad1140  (Adequate.valid adequate Two boolean env5)
  bad1141 : (z4 : Two) → PathP (λ _ → Two) b1 (bop (bop b0 b1) (bop (bop (bop b0 b0) b1) z4)) → ⊥
  bad1141 z4 p = false≢true (sym (cong lower p))
  cut1141 : (x6 : ℕ) → Adequate {ℓ} ((var 0) , (op (op (var 1) (var 0)) (op (op (op (var 2) (var 2)) (var 3)) (var x6)))) → ⊥
  cut1141 x6 adequate = bad1141 (env7 x6) (Adequate.valid adequate Two boolean env7)
  env9 : ℕ → Two
  env9 zero = b1
  env9 (suc zero) = b0
  env9 (suc (suc zero)) = b0
  env9 (suc (suc (suc zero))) = b0
  env9 (suc (suc (suc (suc rest)))) = b0
  bad1142 : (z4 : Two) → PathP (λ _ → Two) b1 (bop (bop b0 b1) (bop (bop (bop b0 b0) b1) z4)) → ⊥
  bad1142 z4 p = false≢true (sym (cong lower p))
  cut1142 : (x6 : ℕ) → Adequate {ℓ} ((var 0) , (op (op (var 1) (var 0)) (op (op (op (var 2) (var 3)) (var 0)) (var x6)))) → ⊥
  cut1142 x6 adequate = bad1142 (env9 x6) (Adequate.valid adequate Two boolean env9)
  holds1143 : (z0 z1 z2 z3 : A3) → z0 ≡ (mul3 (mul3 z1 z0) (mul3 (mul3 (mul3 z2 z3) z1) z0))
  holds1143 z0 z1 z2 z3 = refl
  cut1143 : Adequate {ℓ} ((var 0) , (op (op (var 1) (var 0)) (op (op (op (var 2) (var 3)) (var 1)) (var 0)))) → ⊥
  cut1143  = reject3 ((var 0) , (op (op (var 1) (var 0)) (op (op (op (var 2) (var 3)) (var 1)) (var 0)))) (λ env → holds1143 (env 0) (env 1) (env 2) (env 3))
  env10 : ℕ → Two
  env10 zero = b0
  env10 (suc zero) = b1
  env10 (suc (suc zero)) = b1
  env10 (suc (suc (suc zero))) = b1
  env10 (suc (suc (suc (suc rest)))) = b0
  bad1144 : PathP (λ _ → Two) b0 (bop (bop b1 b0) (bop (bop (bop b1 b1) b1) b1)) → ⊥
  bad1144  p = false≢true (cong lower p)
  cut1144 : Adequate {ℓ} ((var 0) , (op (op (var 1) (var 0)) (op (op (op (var 2) (var 3)) (var 1)) (var 1)))) → ⊥
  cut1144  adequate = bad1144  (Adequate.valid adequate Two boolean env10)
  env11 : ℕ → Two
  env11 zero = b0
  env11 (suc zero) = b0
  env11 (suc (suc zero)) = b1
  env11 (suc (suc (suc zero))) = b0
  env11 (suc (suc (suc (suc rest)))) = b0
  bad1145 : PathP (λ _ → Two) b0 (bop (bop b0 b0) (bop (bop (bop b1 b0) b0) b1)) → ⊥
  bad1145  p = false≢true (cong lower p)
  cut1145 : Adequate {ℓ} ((var 0) , (op (op (var 1) (var 0)) (op (op (op (var 2) (var 3)) (var 1)) (var 2)))) → ⊥
  cut1145  adequate = bad1145  (Adequate.valid adequate Two boolean env11)
  bad1146 : PathP (λ _ → Two) b0 (bop (bop b0 b0) (bop (bop (bop b0 b1) b0) b1)) → ⊥
  bad1146  p = false≢true (cong lower p)
  cut1146 : Adequate {ℓ} ((var 0) , (op (op (var 1) (var 0)) (op (op (op (var 2) (var 3)) (var 1)) (var 3)))) → ⊥
  cut1146  adequate = bad1146  (Adequate.valid adequate Two boolean env5)
  env12 : ℕ → Two
  env12 zero = b0
  env12 (suc zero) = b0
  env12 (suc (suc zero)) = b0
  env12 (suc (suc (suc zero))) = b0
  env12 (suc (suc (suc (suc zero)))) = b1
  env12 (suc (suc (suc (suc (suc rest))))) = b0
  bad1147 : PathP (λ _ → Two) b0 (bop (bop b0 b0) (bop (bop (bop b0 b0) b0) b1)) → ⊥
  bad1147  p = false≢true (cong lower p)
  cut1147 : Adequate {ℓ} ((var 0) , (op (op (var 1) (var 0)) (op (op (op (var 2) (var 3)) (var 1)) (var 4)))) → ⊥
  cut1147  adequate = bad1147  (Adequate.valid adequate Two boolean env12)
  env13 : ℕ → Two
  env13 zero = b1
  env13 (suc zero) = b0
  env13 (suc (suc zero)) = b1
  env13 (suc (suc (suc zero))) = b0
  env13 (suc (suc (suc (suc rest)))) = b0
  bad1148 : (z4 : Two) → PathP (λ _ → Two) b1 (bop (bop b0 b1) (bop (bop (bop b1 b0) b1) z4)) → ⊥
  bad1148 z4 p = false≢true (sym (cong lower p))
  cut1148 : (x6 : ℕ) → Adequate {ℓ} ((var 0) , (op (op (var 1) (var 0)) (op (op (op (var 2) (var 3)) (var 2)) (var x6)))) → ⊥
  cut1148 x6 adequate = bad1148 (env13 x6) (Adequate.valid adequate Two boolean env13)
  bad1149 : (z4 : Two) → PathP (λ _ → Two) b1 (bop (bop b0 b1) (bop (bop (bop b0 b1) b1) z4)) → ⊥
  bad1149 z4 p = false≢true (sym (cong lower p))
  cut1149 : (x6 : ℕ) → Adequate {ℓ} ((var 0) , (op (op (var 1) (var 0)) (op (op (op (var 2) (var 3)) (var 3)) (var x6)))) → ⊥
  cut1149 x6 adequate = bad1149 (env7 x6) (Adequate.valid adequate Two boolean env7)
  env14 : ℕ → Two
  env14 zero = b1
  env14 (suc zero) = b0
  env14 (suc (suc zero)) = b0
  env14 (suc (suc (suc zero))) = b0
  env14 (suc (suc (suc (suc zero)))) = b1
  env14 (suc (suc (suc (suc (suc rest))))) = b0
  bad1150 : (z5 : Two) → PathP (λ _ → Two) b1 (bop (bop b0 b1) (bop (bop (bop b0 b0) b1) z5)) → ⊥
  bad1150 z5 p = false≢true (sym (cong lower p))
  cut1150 : (x6 : ℕ) → Adequate {ℓ} ((var 0) , (op (op (var 1) (var 0)) (op (op (op (var 2) (var 3)) (var 4)) (var x6)))) → ⊥
  cut1150 x6 adequate = bad1150 (env14 x6) (Adequate.valid adequate Two boolean env14)
  bad1151 : (z2 z3 z4 z5 : Two) → PathP (λ _ → Two) b0 (bop (bop b1 b1) (bop (bop (bop z2 z3) z4) z5)) → ⊥
  bad1151 z2 z3 z4 z5 p = false≢true (cong lower p)
  cut1151 : (x3 x4 x5 x6 : ℕ) → Adequate {ℓ} ((var 0) , (op (op (var 1) (var 1)) (op (op (op (var x3) (var x4)) (var x5)) (var x6)))) → ⊥
  cut1151 x3 x4 x5 x6 adequate = bad1151 (env0 x3) (env0 x4) (env0 x5) (env0 x6) (Adequate.valid adequate Two boolean env0)
  bad1152 : (z3 z4 z5 z6 : Two) → PathP (λ _ → Two) b0 (bop (bop b1 b1) (bop (bop (bop z3 z4) z5) z6)) → ⊥
  bad1152 z3 z4 z5 z6 p = false≢true (cong lower p)
  cut1152 : (x3 x4 x5 x6 : ℕ) → Adequate {ℓ} ((var 0) , (op (op (var 1) (var 2)) (op (op (op (var x3) (var x4)) (var x5)) (var x6)))) → ⊥
  cut1152 x3 x4 x5 x6 adequate = bad1152 (env8 x3) (env8 x4) (env8 x5) (env8 x6) (Adequate.valid adequate Two boolean env8)
