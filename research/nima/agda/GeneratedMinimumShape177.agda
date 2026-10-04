{-# OPTIONS --safe --cubical --guardedness #-}
module GeneratedMinimumShape177 where
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
  holds5053 : (z0 : A1) → (mul1 (mul1 z0 (mul1 z0 (mul1 z0 z0))) (mul1 z0 z0)) ≡ z0
  holds5053 m1c0 = refl
  holds5053 m1c1 = refl
  cut5053 : Adequate {ℓ} ((op (op (var 0) (op (var 0) (op (var 0) (var 0)))) (op (var 0) (var 0))) , (var 0)) → ⊥
  cut5053  = reject1 ((op (op (var 0) (op (var 0) (op (var 0) (var 0)))) (op (var 0) (var 0))) , (var 0)) (λ env → holds5053 (env 0))
  env0 : ℕ → Two
  env0 zero = b0
  env0 (suc zero) = b1
  env0 (suc (suc rest)) = b0
  bad5054 : PathP (λ _ → Two) (bop (bop b0 (bop b0 (bop b0 b0))) (bop b0 b0)) b1 → ⊥
  bad5054  p = false≢true (cong lower p)
  cut5054 : Adequate {ℓ} ((op (op (var 0) (op (var 0) (op (var 0) (var 0)))) (op (var 0) (var 0))) , (var 1)) → ⊥
  cut5054  adequate = bad5054  (Adequate.valid adequate Two boolean env0)
  holds5055 : (z0 z1 : A2) → (mul2 (mul2 z0 (mul2 z0 (mul2 z0 z0))) (mul2 z0 z1)) ≡ z0
  holds5055 z0 z1 = refl
  cut5055 : Adequate {ℓ} ((op (op (var 0) (op (var 0) (op (var 0) (var 0)))) (op (var 0) (var 1))) , (var 0)) → ⊥
  cut5055  = reject2 ((op (op (var 0) (op (var 0) (op (var 0) (var 0)))) (op (var 0) (var 1))) , (var 0)) (λ env → holds5055 (env 0) (env 1))
  bad5056 : PathP (λ _ → Two) (bop (bop b0 (bop b0 (bop b0 b0))) (bop b0 b1)) b1 → ⊥
  bad5056  p = false≢true (cong lower p)
  cut5056 : Adequate {ℓ} ((op (op (var 0) (op (var 0) (op (var 0) (var 0)))) (op (var 0) (var 1))) , (var 1)) → ⊥
  cut5056  adequate = bad5056  (Adequate.valid adequate Two boolean env0)
  env1 : ℕ → Two
  env1 zero = b0
  env1 (suc zero) = b0
  env1 (suc (suc zero)) = b1
  env1 (suc (suc (suc rest))) = b0
  bad5057 : PathP (λ _ → Two) (bop (bop b0 (bop b0 (bop b0 b0))) (bop b0 b0)) b1 → ⊥
  bad5057  p = false≢true (cong lower p)
  cut5057 : Adequate {ℓ} ((op (op (var 0) (op (var 0) (op (var 0) (var 0)))) (op (var 0) (var 1))) , (var 2)) → ⊥
  cut5057  adequate = bad5057  (Adequate.valid adequate Two boolean env1)
  holds5058 : (z0 z1 : A2) → (mul2 (mul2 z0 (mul2 z0 (mul2 z0 z0))) (mul2 z1 z0)) ≡ z0
  holds5058 z0 z1 = refl
  cut5058 : Adequate {ℓ} ((op (op (var 0) (op (var 0) (op (var 0) (var 0)))) (op (var 1) (var 0))) , (var 0)) → ⊥
  cut5058  = reject2 ((op (op (var 0) (op (var 0) (op (var 0) (var 0)))) (op (var 1) (var 0))) , (var 0)) (λ env → holds5058 (env 0) (env 1))
  bad5059 : PathP (λ _ → Two) (bop (bop b0 (bop b0 (bop b0 b0))) (bop b1 b0)) b1 → ⊥
  bad5059  p = false≢true (cong lower p)
  cut5059 : Adequate {ℓ} ((op (op (var 0) (op (var 0) (op (var 0) (var 0)))) (op (var 1) (var 0))) , (var 1)) → ⊥
  cut5059  adequate = bad5059  (Adequate.valid adequate Two boolean env0)
  bad5060 : PathP (λ _ → Two) (bop (bop b0 (bop b0 (bop b0 b0))) (bop b0 b0)) b1 → ⊥
  bad5060  p = false≢true (cong lower p)
  cut5060 : Adequate {ℓ} ((op (op (var 0) (op (var 0) (op (var 0) (var 0)))) (op (var 1) (var 0))) , (var 2)) → ⊥
  cut5060  adequate = bad5060  (Adequate.valid adequate Two boolean env1)
  bad5061 : PathP (λ _ → Two) (bop (bop b0 (bop b0 (bop b0 b0))) (bop b1 b1)) b0 → ⊥
  bad5061  p = false≢true (sym (cong lower p))
  cut5061 : Adequate {ℓ} ((op (op (var 0) (op (var 0) (op (var 0) (var 0)))) (op (var 1) (var 1))) , (var 0)) → ⊥
  cut5061  adequate = bad5061  (Adequate.valid adequate Two boolean env0)
  env2 : ℕ → Two
  env2 zero = b1
  env2 (suc zero) = b0
  env2 (suc (suc rest)) = b0
  bad5062 : PathP (λ _ → Two) (bop (bop b1 (bop b1 (bop b1 b1))) (bop b0 b0)) b0 → ⊥
  bad5062  p = false≢true (sym (cong lower p))
  cut5062 : Adequate {ℓ} ((op (op (var 0) (op (var 0) (op (var 0) (var 0)))) (op (var 1) (var 1))) , (var 1)) → ⊥
  cut5062  adequate = bad5062  (Adequate.valid adequate Two boolean env2)
  bad5063 : PathP (λ _ → Two) (bop (bop b0 (bop b0 (bop b0 b0))) (bop b0 b0)) b1 → ⊥
  bad5063  p = false≢true (cong lower p)
  cut5063 : Adequate {ℓ} ((op (op (var 0) (op (var 0) (op (var 0) (var 0)))) (op (var 1) (var 1))) , (var 2)) → ⊥
  cut5063  adequate = bad5063  (Adequate.valid adequate Two boolean env1)
  env3 : ℕ → Two
  env3 zero = b0
  env3 (suc zero) = b1
  env3 (suc (suc zero)) = b1
  env3 (suc (suc (suc rest))) = b0
  bad5064 : PathP (λ _ → Two) (bop (bop b0 (bop b0 (bop b0 b0))) (bop b1 b1)) b0 → ⊥
  bad5064  p = false≢true (sym (cong lower p))
  cut5064 : Adequate {ℓ} ((op (op (var 0) (op (var 0) (op (var 0) (var 0)))) (op (var 1) (var 2))) , (var 0)) → ⊥
  cut5064  adequate = bad5064  (Adequate.valid adequate Two boolean env3)
  env4 : ℕ → Two
  env4 zero = b0
  env4 (suc zero) = b1
  env4 (suc (suc zero)) = b0
  env4 (suc (suc (suc rest))) = b0
  bad5065 : PathP (λ _ → Two) (bop (bop b0 (bop b0 (bop b0 b0))) (bop b1 b0)) b1 → ⊥
  bad5065  p = false≢true (cong lower p)
  cut5065 : Adequate {ℓ} ((op (op (var 0) (op (var 0) (op (var 0) (var 0)))) (op (var 1) (var 2))) , (var 1)) → ⊥
  cut5065  adequate = bad5065  (Adequate.valid adequate Two boolean env4)
  bad5066 : PathP (λ _ → Two) (bop (bop b0 (bop b0 (bop b0 b0))) (bop b0 b1)) b1 → ⊥
  bad5066  p = false≢true (cong lower p)
  cut5066 : Adequate {ℓ} ((op (op (var 0) (op (var 0) (op (var 0) (var 0)))) (op (var 1) (var 2))) , (var 2)) → ⊥
  cut5066  adequate = bad5066  (Adequate.valid adequate Two boolean env1)
  env5 : ℕ → Two
  env5 zero = b0
  env5 (suc zero) = b0
  env5 (suc (suc zero)) = b0
  env5 (suc (suc (suc zero))) = b1
  env5 (suc (suc (suc (suc rest)))) = b0
  bad5067 : PathP (λ _ → Two) (bop (bop b0 (bop b0 (bop b0 b0))) (bop b0 b0)) b1 → ⊥
  bad5067  p = false≢true (cong lower p)
  cut5067 : Adequate {ℓ} ((op (op (var 0) (op (var 0) (op (var 0) (var 0)))) (op (var 1) (var 2))) , (var 3)) → ⊥
  cut5067  adequate = bad5067  (Adequate.valid adequate Two boolean env5)
  holds5068 : (z0 z1 : A2) → (mul2 (mul2 z0 (mul2 z0 (mul2 z0 z1))) (mul2 z0 z0)) ≡ z0
  holds5068 z0 z1 = refl
  cut5068 : Adequate {ℓ} ((op (op (var 0) (op (var 0) (op (var 0) (var 1)))) (op (var 0) (var 0))) , (var 0)) → ⊥
  cut5068  = reject2 ((op (op (var 0) (op (var 0) (op (var 0) (var 1)))) (op (var 0) (var 0))) , (var 0)) (λ env → holds5068 (env 0) (env 1))
  bad5069 : PathP (λ _ → Two) (bop (bop b0 (bop b0 (bop b0 b1))) (bop b0 b0)) b1 → ⊥
  bad5069  p = false≢true (cong lower p)
  cut5069 : Adequate {ℓ} ((op (op (var 0) (op (var 0) (op (var 0) (var 1)))) (op (var 0) (var 0))) , (var 1)) → ⊥
  cut5069  adequate = bad5069  (Adequate.valid adequate Two boolean env0)
  bad5070 : PathP (λ _ → Two) (bop (bop b0 (bop b0 (bop b0 b0))) (bop b0 b0)) b1 → ⊥
  bad5070  p = false≢true (cong lower p)
  cut5070 : Adequate {ℓ} ((op (op (var 0) (op (var 0) (op (var 0) (var 1)))) (op (var 0) (var 0))) , (var 2)) → ⊥
  cut5070  adequate = bad5070  (Adequate.valid adequate Two boolean env1)
  bad5071 : PathP (λ _ → Two) (bop (bop b1 (bop b1 (bop b1 b0))) (bop b1 b0)) b1 → ⊥
  bad5071  p = false≢true (cong lower p)
  cut5071 : Adequate {ℓ} ((op (op (var 0) (op (var 0) (op (var 0) (var 1)))) (op (var 0) (var 1))) , (var 0)) → ⊥
  cut5071  adequate = bad5071  (Adequate.valid adequate Two boolean env2)
  bad5072 : PathP (λ _ → Two) (bop (bop b0 (bop b0 (bop b0 b1))) (bop b0 b1)) b1 → ⊥
  bad5072  p = false≢true (cong lower p)
  cut5072 : Adequate {ℓ} ((op (op (var 0) (op (var 0) (op (var 0) (var 1)))) (op (var 0) (var 1))) , (var 1)) → ⊥
  cut5072  adequate = bad5072  (Adequate.valid adequate Two boolean env0)
  bad5073 : PathP (λ _ → Two) (bop (bop b0 (bop b0 (bop b0 b0))) (bop b0 b0)) b1 → ⊥
  bad5073  p = false≢true (cong lower p)
  cut5073 : Adequate {ℓ} ((op (op (var 0) (op (var 0) (op (var 0) (var 1)))) (op (var 0) (var 1))) , (var 2)) → ⊥
  cut5073  adequate = bad5073  (Adequate.valid adequate Two boolean env1)
  env6 : ℕ → Two
  env6 zero = b1
  env6 (suc zero) = b0
  env6 (suc (suc zero)) = b0
  env6 (suc (suc (suc rest))) = b0
  bad5074 : PathP (λ _ → Two) (bop (bop b1 (bop b1 (bop b1 b0))) (bop b1 b0)) b1 → ⊥
  bad5074  p = false≢true (cong lower p)
  cut5074 : Adequate {ℓ} ((op (op (var 0) (op (var 0) (op (var 0) (var 1)))) (op (var 0) (var 2))) , (var 0)) → ⊥
  cut5074  adequate = bad5074  (Adequate.valid adequate Two boolean env6)
  bad5075 : PathP (λ _ → Two) (bop (bop b0 (bop b0 (bop b0 b1))) (bop b0 b0)) b1 → ⊥
  bad5075  p = false≢true (cong lower p)
  cut5075 : Adequate {ℓ} ((op (op (var 0) (op (var 0) (op (var 0) (var 1)))) (op (var 0) (var 2))) , (var 1)) → ⊥
  cut5075  adequate = bad5075  (Adequate.valid adequate Two boolean env4)
  bad5076 : PathP (λ _ → Two) (bop (bop b0 (bop b0 (bop b0 b0))) (bop b0 b1)) b1 → ⊥
  bad5076  p = false≢true (cong lower p)
  cut5076 : Adequate {ℓ} ((op (op (var 0) (op (var 0) (op (var 0) (var 1)))) (op (var 0) (var 2))) , (var 2)) → ⊥
  cut5076  adequate = bad5076  (Adequate.valid adequate Two boolean env1)
  bad5077 : PathP (λ _ → Two) (bop (bop b0 (bop b0 (bop b0 b0))) (bop b0 b0)) b1 → ⊥
  bad5077  p = false≢true (cong lower p)
  cut5077 : Adequate {ℓ} ((op (op (var 0) (op (var 0) (op (var 0) (var 1)))) (op (var 0) (var 2))) , (var 3)) → ⊥
  cut5077  adequate = bad5077  (Adequate.valid adequate Two boolean env5)
  bad5078 : PathP (λ _ → Two) (bop (bop b1 (bop b1 (bop b1 b0))) (bop b0 b1)) b1 → ⊥
  bad5078  p = false≢true (cong lower p)
  cut5078 : Adequate {ℓ} ((op (op (var 0) (op (var 0) (op (var 0) (var 1)))) (op (var 1) (var 0))) , (var 0)) → ⊥
  cut5078  adequate = bad5078  (Adequate.valid adequate Two boolean env2)
  bad5079 : PathP (λ _ → Two) (bop (bop b0 (bop b0 (bop b0 b1))) (bop b1 b0)) b1 → ⊥
  bad5079  p = false≢true (cong lower p)
  cut5079 : Adequate {ℓ} ((op (op (var 0) (op (var 0) (op (var 0) (var 1)))) (op (var 1) (var 0))) , (var 1)) → ⊥
  cut5079  adequate = bad5079  (Adequate.valid adequate Two boolean env0)
  bad5080 : PathP (λ _ → Two) (bop (bop b0 (bop b0 (bop b0 b0))) (bop b0 b0)) b1 → ⊥
  bad5080  p = false≢true (cong lower p)
  cut5080 : Adequate {ℓ} ((op (op (var 0) (op (var 0) (op (var 0) (var 1)))) (op (var 1) (var 0))) , (var 2)) → ⊥
  cut5080  adequate = bad5080  (Adequate.valid adequate Two boolean env1)
  bad5081 : PathP (λ _ → Two) (bop (bop b0 (bop b0 (bop b0 b1))) (bop b1 b1)) b0 → ⊥
  bad5081  p = false≢true (sym (cong lower p))
  cut5081 : Adequate {ℓ} ((op (op (var 0) (op (var 0) (op (var 0) (var 1)))) (op (var 1) (var 1))) , (var 0)) → ⊥
  cut5081  adequate = bad5081  (Adequate.valid adequate Two boolean env0)
  holds5082 : (z0 z1 : A3) → (mul3 (mul3 z0 (mul3 z0 (mul3 z0 z1))) (mul3 z1 z1)) ≡ z1
  holds5082 z0 z1 = refl
  cut5082 : Adequate {ℓ} ((op (op (var 0) (op (var 0) (op (var 0) (var 1)))) (op (var 1) (var 1))) , (var 1)) → ⊥
  cut5082  = reject3 ((op (op (var 0) (op (var 0) (op (var 0) (var 1)))) (op (var 1) (var 1))) , (var 1)) (λ env → holds5082 (env 0) (env 1))
  bad5083 : PathP (λ _ → Two) (bop (bop b0 (bop b0 (bop b0 b0))) (bop b0 b0)) b1 → ⊥
  bad5083  p = false≢true (cong lower p)
  cut5083 : Adequate {ℓ} ((op (op (var 0) (op (var 0) (op (var 0) (var 1)))) (op (var 1) (var 1))) , (var 2)) → ⊥
  cut5083  adequate = bad5083  (Adequate.valid adequate Two boolean env1)
  bad5084 : PathP (λ _ → Two) (bop (bop b0 (bop b0 (bop b0 b1))) (bop b1 b1)) b0 → ⊥
  bad5084  p = false≢true (sym (cong lower p))
  cut5084 : Adequate {ℓ} ((op (op (var 0) (op (var 0) (op (var 0) (var 1)))) (op (var 1) (var 2))) , (var 0)) → ⊥
  cut5084  adequate = bad5084  (Adequate.valid adequate Two boolean env3)
  bad5085 : PathP (λ _ → Two) (bop (bop b0 (bop b0 (bop b0 b1))) (bop b1 b0)) b1 → ⊥
  bad5085  p = false≢true (cong lower p)
  cut5085 : Adequate {ℓ} ((op (op (var 0) (op (var 0) (op (var 0) (var 1)))) (op (var 1) (var 2))) , (var 1)) → ⊥
  cut5085  adequate = bad5085  (Adequate.valid adequate Two boolean env4)
  bad5086 : PathP (λ _ → Two) (bop (bop b0 (bop b0 (bop b0 b0))) (bop b0 b1)) b1 → ⊥
  bad5086  p = false≢true (cong lower p)
  cut5086 : Adequate {ℓ} ((op (op (var 0) (op (var 0) (op (var 0) (var 1)))) (op (var 1) (var 2))) , (var 2)) → ⊥
  cut5086  adequate = bad5086  (Adequate.valid adequate Two boolean env1)
  bad5087 : PathP (λ _ → Two) (bop (bop b0 (bop b0 (bop b0 b0))) (bop b0 b0)) b1 → ⊥
  bad5087  p = false≢true (cong lower p)
  cut5087 : Adequate {ℓ} ((op (op (var 0) (op (var 0) (op (var 0) (var 1)))) (op (var 1) (var 2))) , (var 3)) → ⊥
  cut5087  adequate = bad5087  (Adequate.valid adequate Two boolean env5)
  bad5088 : PathP (λ _ → Two) (bop (bop b1 (bop b1 (bop b1 b0))) (bop b0 b1)) b1 → ⊥
  bad5088  p = false≢true (cong lower p)
  cut5088 : Adequate {ℓ} ((op (op (var 0) (op (var 0) (op (var 0) (var 1)))) (op (var 2) (var 0))) , (var 0)) → ⊥
  cut5088  adequate = bad5088  (Adequate.valid adequate Two boolean env6)
  bad5089 : PathP (λ _ → Two) (bop (bop b0 (bop b0 (bop b0 b1))) (bop b0 b0)) b1 → ⊥
  bad5089  p = false≢true (cong lower p)
  cut5089 : Adequate {ℓ} ((op (op (var 0) (op (var 0) (op (var 0) (var 1)))) (op (var 2) (var 0))) , (var 1)) → ⊥
  cut5089  adequate = bad5089  (Adequate.valid adequate Two boolean env4)
  bad5090 : PathP (λ _ → Two) (bop (bop b0 (bop b0 (bop b0 b0))) (bop b1 b0)) b1 → ⊥
  bad5090  p = false≢true (cong lower p)
  cut5090 : Adequate {ℓ} ((op (op (var 0) (op (var 0) (op (var 0) (var 1)))) (op (var 2) (var 0))) , (var 2)) → ⊥
  cut5090  adequate = bad5090  (Adequate.valid adequate Two boolean env1)
  bad5091 : PathP (λ _ → Two) (bop (bop b0 (bop b0 (bop b0 b0))) (bop b0 b0)) b1 → ⊥
  bad5091  p = false≢true (cong lower p)
  cut5091 : Adequate {ℓ} ((op (op (var 0) (op (var 0) (op (var 0) (var 1)))) (op (var 2) (var 0))) , (var 3)) → ⊥
  cut5091  adequate = bad5091  (Adequate.valid adequate Two boolean env5)
  bad5092 : PathP (λ _ → Two) (bop (bop b0 (bop b0 (bop b0 b1))) (bop b1 b1)) b0 → ⊥
  bad5092  p = false≢true (sym (cong lower p))
  cut5092 : Adequate {ℓ} ((op (op (var 0) (op (var 0) (op (var 0) (var 1)))) (op (var 2) (var 1))) , (var 0)) → ⊥
  cut5092  adequate = bad5092  (Adequate.valid adequate Two boolean env3)
  bad5093 : PathP (λ _ → Two) (bop (bop b0 (bop b0 (bop b0 b1))) (bop b0 b1)) b1 → ⊥
  bad5093  p = false≢true (cong lower p)
  cut5093 : Adequate {ℓ} ((op (op (var 0) (op (var 0) (op (var 0) (var 1)))) (op (var 2) (var 1))) , (var 1)) → ⊥
  cut5093  adequate = bad5093  (Adequate.valid adequate Two boolean env4)
  bad5094 : PathP (λ _ → Two) (bop (bop b0 (bop b0 (bop b0 b0))) (bop b1 b0)) b1 → ⊥
  bad5094  p = false≢true (cong lower p)
  cut5094 : Adequate {ℓ} ((op (op (var 0) (op (var 0) (op (var 0) (var 1)))) (op (var 2) (var 1))) , (var 2)) → ⊥
  cut5094  adequate = bad5094  (Adequate.valid adequate Two boolean env1)
  bad5095 : PathP (λ _ → Two) (bop (bop b0 (bop b0 (bop b0 b0))) (bop b0 b0)) b1 → ⊥
  bad5095  p = false≢true (cong lower p)
  cut5095 : Adequate {ℓ} ((op (op (var 0) (op (var 0) (op (var 0) (var 1)))) (op (var 2) (var 1))) , (var 3)) → ⊥
  cut5095  adequate = bad5095  (Adequate.valid adequate Two boolean env5)
  bad5096 : PathP (λ _ → Two) (bop (bop b0 (bop b0 (bop b0 b0))) (bop b1 b1)) b0 → ⊥
  bad5096  p = false≢true (sym (cong lower p))
  cut5096 : Adequate {ℓ} ((op (op (var 0) (op (var 0) (op (var 0) (var 1)))) (op (var 2) (var 2))) , (var 0)) → ⊥
  cut5096  adequate = bad5096  (Adequate.valid adequate Two boolean env1)
  bad5097 : PathP (λ _ → Two) (bop (bop b0 (bop b0 (bop b0 b0))) (bop b1 b1)) b0 → ⊥
  bad5097  p = false≢true (sym (cong lower p))
  cut5097 : Adequate {ℓ} ((op (op (var 0) (op (var 0) (op (var 0) (var 1)))) (op (var 2) (var 2))) , (var 1)) → ⊥
  cut5097  adequate = bad5097  (Adequate.valid adequate Two boolean env1)
  env7 : ℕ → Two
  env7 zero = b1
  env7 (suc zero) = b1
  env7 (suc (suc zero)) = b0
  env7 (suc (suc (suc rest))) = b0
  bad5098 : PathP (λ _ → Two) (bop (bop b1 (bop b1 (bop b1 b1))) (bop b0 b0)) b0 → ⊥
  bad5098  p = false≢true (sym (cong lower p))
  cut5098 : Adequate {ℓ} ((op (op (var 0) (op (var 0) (op (var 0) (var 1)))) (op (var 2) (var 2))) , (var 2)) → ⊥
  cut5098  adequate = bad5098  (Adequate.valid adequate Two boolean env7)
  bad5099 : PathP (λ _ → Two) (bop (bop b0 (bop b0 (bop b0 b0))) (bop b0 b0)) b1 → ⊥
  bad5099  p = false≢true (cong lower p)
  cut5099 : Adequate {ℓ} ((op (op (var 0) (op (var 0) (op (var 0) (var 1)))) (op (var 2) (var 2))) , (var 3)) → ⊥
  cut5099  adequate = bad5099  (Adequate.valid adequate Two boolean env5)
  env8 : ℕ → Two
  env8 zero = b0
  env8 (suc zero) = b0
  env8 (suc (suc zero)) = b1
  env8 (suc (suc (suc zero))) = b1
  env8 (suc (suc (suc (suc rest)))) = b0
  bad5100 : PathP (λ _ → Two) (bop (bop b0 (bop b0 (bop b0 b0))) (bop b1 b1)) b0 → ⊥
  bad5100  p = false≢true (sym (cong lower p))
  cut5100 : Adequate {ℓ} ((op (op (var 0) (op (var 0) (op (var 0) (var 1)))) (op (var 2) (var 3))) , (var 0)) → ⊥
  cut5100  adequate = bad5100  (Adequate.valid adequate Two boolean env8)
  bad5101 : PathP (λ _ → Two) (bop (bop b0 (bop b0 (bop b0 b0))) (bop b1 b1)) b0 → ⊥
  bad5101  p = false≢true (sym (cong lower p))
  cut5101 : Adequate {ℓ} ((op (op (var 0) (op (var 0) (op (var 0) (var 1)))) (op (var 2) (var 3))) , (var 1)) → ⊥
  cut5101  adequate = bad5101  (Adequate.valid adequate Two boolean env8)
  env9 : ℕ → Two
  env9 zero = b0
  env9 (suc zero) = b0
  env9 (suc (suc zero)) = b1
  env9 (suc (suc (suc zero))) = b0
  env9 (suc (suc (suc (suc rest)))) = b0
  bad5102 : PathP (λ _ → Two) (bop (bop b0 (bop b0 (bop b0 b0))) (bop b1 b0)) b1 → ⊥
  bad5102  p = false≢true (cong lower p)
  cut5102 : Adequate {ℓ} ((op (op (var 0) (op (var 0) (op (var 0) (var 1)))) (op (var 2) (var 3))) , (var 2)) → ⊥
  cut5102  adequate = bad5102  (Adequate.valid adequate Two boolean env9)
  bad5103 : PathP (λ _ → Two) (bop (bop b0 (bop b0 (bop b0 b0))) (bop b0 b1)) b1 → ⊥
  bad5103  p = false≢true (cong lower p)
  cut5103 : Adequate {ℓ} ((op (op (var 0) (op (var 0) (op (var 0) (var 1)))) (op (var 2) (var 3))) , (var 3)) → ⊥
  cut5103  adequate = bad5103  (Adequate.valid adequate Two boolean env5)
  env10 : ℕ → Two
  env10 zero = b0
  env10 (suc zero) = b0
  env10 (suc (suc zero)) = b0
  env10 (suc (suc (suc zero))) = b0
  env10 (suc (suc (suc (suc zero)))) = b1
  env10 (suc (suc (suc (suc (suc rest))))) = b0
  bad5104 : PathP (λ _ → Two) (bop (bop b0 (bop b0 (bop b0 b0))) (bop b0 b0)) b1 → ⊥
  bad5104  p = false≢true (cong lower p)
  cut5104 : Adequate {ℓ} ((op (op (var 0) (op (var 0) (op (var 0) (var 1)))) (op (var 2) (var 3))) , (var 4)) → ⊥
  cut5104  adequate = bad5104  (Adequate.valid adequate Two boolean env10)
  holds5105 : (z0 z1 : A2) → (mul2 (mul2 z0 (mul2 z0 (mul2 z1 z0))) (mul2 z0 z0)) ≡ z0
  holds5105 z0 z1 = refl
  cut5105 : Adequate {ℓ} ((op (op (var 0) (op (var 0) (op (var 1) (var 0)))) (op (var 0) (var 0))) , (var 0)) → ⊥
  cut5105  = reject2 ((op (op (var 0) (op (var 0) (op (var 1) (var 0)))) (op (var 0) (var 0))) , (var 0)) (λ env → holds5105 (env 0) (env 1))
  bad5106 : PathP (λ _ → Two) (bop (bop b0 (bop b0 (bop b1 b0))) (bop b0 b0)) b1 → ⊥
  bad5106  p = false≢true (cong lower p)
  cut5106 : Adequate {ℓ} ((op (op (var 0) (op (var 0) (op (var 1) (var 0)))) (op (var 0) (var 0))) , (var 1)) → ⊥
  cut5106  adequate = bad5106  (Adequate.valid adequate Two boolean env0)
  bad5107 : PathP (λ _ → Two) (bop (bop b0 (bop b0 (bop b0 b0))) (bop b0 b0)) b1 → ⊥
  bad5107  p = false≢true (cong lower p)
  cut5107 : Adequate {ℓ} ((op (op (var 0) (op (var 0) (op (var 1) (var 0)))) (op (var 0) (var 0))) , (var 2)) → ⊥
  cut5107  adequate = bad5107  (Adequate.valid adequate Two boolean env1)
  bad5108 : PathP (λ _ → Two) (bop (bop b1 (bop b1 (bop b0 b1))) (bop b1 b0)) b1 → ⊥
  bad5108  p = false≢true (cong lower p)
  cut5108 : Adequate {ℓ} ((op (op (var 0) (op (var 0) (op (var 1) (var 0)))) (op (var 0) (var 1))) , (var 0)) → ⊥
  cut5108  adequate = bad5108  (Adequate.valid adequate Two boolean env2)
  bad5109 : PathP (λ _ → Two) (bop (bop b0 (bop b0 (bop b1 b0))) (bop b0 b1)) b1 → ⊥
  bad5109  p = false≢true (cong lower p)
  cut5109 : Adequate {ℓ} ((op (op (var 0) (op (var 0) (op (var 1) (var 0)))) (op (var 0) (var 1))) , (var 1)) → ⊥
  cut5109  adequate = bad5109  (Adequate.valid adequate Two boolean env0)
  bad5110 : PathP (λ _ → Two) (bop (bop b0 (bop b0 (bop b0 b0))) (bop b0 b0)) b1 → ⊥
  bad5110  p = false≢true (cong lower p)
  cut5110 : Adequate {ℓ} ((op (op (var 0) (op (var 0) (op (var 1) (var 0)))) (op (var 0) (var 1))) , (var 2)) → ⊥
  cut5110  adequate = bad5110  (Adequate.valid adequate Two boolean env1)
  bad5111 : PathP (λ _ → Two) (bop (bop b1 (bop b1 (bop b0 b1))) (bop b1 b0)) b1 → ⊥
  bad5111  p = false≢true (cong lower p)
  cut5111 : Adequate {ℓ} ((op (op (var 0) (op (var 0) (op (var 1) (var 0)))) (op (var 0) (var 2))) , (var 0)) → ⊥
  cut5111  adequate = bad5111  (Adequate.valid adequate Two boolean env6)
  bad5112 : PathP (λ _ → Two) (bop (bop b0 (bop b0 (bop b1 b0))) (bop b0 b0)) b1 → ⊥
  bad5112  p = false≢true (cong lower p)
  cut5112 : Adequate {ℓ} ((op (op (var 0) (op (var 0) (op (var 1) (var 0)))) (op (var 0) (var 2))) , (var 1)) → ⊥
  cut5112  adequate = bad5112  (Adequate.valid adequate Two boolean env4)
  bad5113 : PathP (λ _ → Two) (bop (bop b0 (bop b0 (bop b0 b0))) (bop b0 b1)) b1 → ⊥
  bad5113  p = false≢true (cong lower p)
  cut5113 : Adequate {ℓ} ((op (op (var 0) (op (var 0) (op (var 1) (var 0)))) (op (var 0) (var 2))) , (var 2)) → ⊥
  cut5113  adequate = bad5113  (Adequate.valid adequate Two boolean env1)
  bad5114 : PathP (λ _ → Two) (bop (bop b0 (bop b0 (bop b0 b0))) (bop b0 b0)) b1 → ⊥
  bad5114  p = false≢true (cong lower p)
  cut5114 : Adequate {ℓ} ((op (op (var 0) (op (var 0) (op (var 1) (var 0)))) (op (var 0) (var 2))) , (var 3)) → ⊥
  cut5114  adequate = bad5114  (Adequate.valid adequate Two boolean env5)
  bad5115 : PathP (λ _ → Two) (bop (bop b1 (bop b1 (bop b0 b1))) (bop b0 b1)) b1 → ⊥
  bad5115  p = false≢true (cong lower p)
  cut5115 : Adequate {ℓ} ((op (op (var 0) (op (var 0) (op (var 1) (var 0)))) (op (var 1) (var 0))) , (var 0)) → ⊥
  cut5115  adequate = bad5115  (Adequate.valid adequate Two boolean env2)
  bad5116 : PathP (λ _ → Two) (bop (bop b0 (bop b0 (bop b1 b0))) (bop b1 b0)) b1 → ⊥
  bad5116  p = false≢true (cong lower p)
  cut5116 : Adequate {ℓ} ((op (op (var 0) (op (var 0) (op (var 1) (var 0)))) (op (var 1) (var 0))) , (var 1)) → ⊥
  cut5116  adequate = bad5116  (Adequate.valid adequate Two boolean env0)
  bad5117 : PathP (λ _ → Two) (bop (bop b0 (bop b0 (bop b0 b0))) (bop b0 b0)) b1 → ⊥
  bad5117  p = false≢true (cong lower p)
  cut5117 : Adequate {ℓ} ((op (op (var 0) (op (var 0) (op (var 1) (var 0)))) (op (var 1) (var 0))) , (var 2)) → ⊥
  cut5117  adequate = bad5117  (Adequate.valid adequate Two boolean env1)
  bad5118 : PathP (λ _ → Two) (bop (bop b0 (bop b0 (bop b1 b0))) (bop b1 b1)) b0 → ⊥
  bad5118  p = false≢true (sym (cong lower p))
  cut5118 : Adequate {ℓ} ((op (op (var 0) (op (var 0) (op (var 1) (var 0)))) (op (var 1) (var 1))) , (var 0)) → ⊥
  cut5118  adequate = bad5118  (Adequate.valid adequate Two boolean env0)
  holds5119 : (z0 z1 : A3) → (mul3 (mul3 z0 (mul3 z0 (mul3 z1 z0))) (mul3 z1 z1)) ≡ z1
  holds5119 z0 z1 = refl
  cut5119 : Adequate {ℓ} ((op (op (var 0) (op (var 0) (op (var 1) (var 0)))) (op (var 1) (var 1))) , (var 1)) → ⊥
  cut5119  = reject3 ((op (op (var 0) (op (var 0) (op (var 1) (var 0)))) (op (var 1) (var 1))) , (var 1)) (λ env → holds5119 (env 0) (env 1))
  bad5120 : PathP (λ _ → Two) (bop (bop b0 (bop b0 (bop b0 b0))) (bop b0 b0)) b1 → ⊥
  bad5120  p = false≢true (cong lower p)
  cut5120 : Adequate {ℓ} ((op (op (var 0) (op (var 0) (op (var 1) (var 0)))) (op (var 1) (var 1))) , (var 2)) → ⊥
  cut5120  adequate = bad5120  (Adequate.valid adequate Two boolean env1)
  bad5121 : PathP (λ _ → Two) (bop (bop b0 (bop b0 (bop b1 b0))) (bop b1 b1)) b0 → ⊥
  bad5121  p = false≢true (sym (cong lower p))
  cut5121 : Adequate {ℓ} ((op (op (var 0) (op (var 0) (op (var 1) (var 0)))) (op (var 1) (var 2))) , (var 0)) → ⊥
  cut5121  adequate = bad5121  (Adequate.valid adequate Two boolean env3)
  bad5122 : PathP (λ _ → Two) (bop (bop b0 (bop b0 (bop b1 b0))) (bop b1 b0)) b1 → ⊥
  bad5122  p = false≢true (cong lower p)
  cut5122 : Adequate {ℓ} ((op (op (var 0) (op (var 0) (op (var 1) (var 0)))) (op (var 1) (var 2))) , (var 1)) → ⊥
  cut5122  adequate = bad5122  (Adequate.valid adequate Two boolean env4)
  bad5123 : PathP (λ _ → Two) (bop (bop b0 (bop b0 (bop b0 b0))) (bop b0 b1)) b1 → ⊥
  bad5123  p = false≢true (cong lower p)
  cut5123 : Adequate {ℓ} ((op (op (var 0) (op (var 0) (op (var 1) (var 0)))) (op (var 1) (var 2))) , (var 2)) → ⊥
  cut5123  adequate = bad5123  (Adequate.valid adequate Two boolean env1)
  bad5124 : PathP (λ _ → Two) (bop (bop b0 (bop b0 (bop b0 b0))) (bop b0 b0)) b1 → ⊥
  bad5124  p = false≢true (cong lower p)
  cut5124 : Adequate {ℓ} ((op (op (var 0) (op (var 0) (op (var 1) (var 0)))) (op (var 1) (var 2))) , (var 3)) → ⊥
  cut5124  adequate = bad5124  (Adequate.valid adequate Two boolean env5)
  bad5125 : PathP (λ _ → Two) (bop (bop b1 (bop b1 (bop b0 b1))) (bop b0 b1)) b1 → ⊥
  bad5125  p = false≢true (cong lower p)
  cut5125 : Adequate {ℓ} ((op (op (var 0) (op (var 0) (op (var 1) (var 0)))) (op (var 2) (var 0))) , (var 0)) → ⊥
  cut5125  adequate = bad5125  (Adequate.valid adequate Two boolean env6)
  bad5126 : PathP (λ _ → Two) (bop (bop b0 (bop b0 (bop b1 b0))) (bop b0 b0)) b1 → ⊥
  bad5126  p = false≢true (cong lower p)
  cut5126 : Adequate {ℓ} ((op (op (var 0) (op (var 0) (op (var 1) (var 0)))) (op (var 2) (var 0))) , (var 1)) → ⊥
  cut5126  adequate = bad5126  (Adequate.valid adequate Two boolean env4)
  bad5127 : PathP (λ _ → Two) (bop (bop b0 (bop b0 (bop b0 b0))) (bop b1 b0)) b1 → ⊥
  bad5127  p = false≢true (cong lower p)
  cut5127 : Adequate {ℓ} ((op (op (var 0) (op (var 0) (op (var 1) (var 0)))) (op (var 2) (var 0))) , (var 2)) → ⊥
  cut5127  adequate = bad5127  (Adequate.valid adequate Two boolean env1)
  bad5128 : PathP (λ _ → Two) (bop (bop b0 (bop b0 (bop b0 b0))) (bop b0 b0)) b1 → ⊥
  bad5128  p = false≢true (cong lower p)
  cut5128 : Adequate {ℓ} ((op (op (var 0) (op (var 0) (op (var 1) (var 0)))) (op (var 2) (var 0))) , (var 3)) → ⊥
  cut5128  adequate = bad5128  (Adequate.valid adequate Two boolean env5)
  bad5129 : PathP (λ _ → Two) (bop (bop b0 (bop b0 (bop b1 b0))) (bop b1 b1)) b0 → ⊥
  bad5129  p = false≢true (sym (cong lower p))
  cut5129 : Adequate {ℓ} ((op (op (var 0) (op (var 0) (op (var 1) (var 0)))) (op (var 2) (var 1))) , (var 0)) → ⊥
  cut5129  adequate = bad5129  (Adequate.valid adequate Two boolean env3)
  bad5130 : PathP (λ _ → Two) (bop (bop b0 (bop b0 (bop b1 b0))) (bop b0 b1)) b1 → ⊥
  bad5130  p = false≢true (cong lower p)
  cut5130 : Adequate {ℓ} ((op (op (var 0) (op (var 0) (op (var 1) (var 0)))) (op (var 2) (var 1))) , (var 1)) → ⊥
  cut5130  adequate = bad5130  (Adequate.valid adequate Two boolean env4)
  bad5131 : PathP (λ _ → Two) (bop (bop b0 (bop b0 (bop b0 b0))) (bop b1 b0)) b1 → ⊥
  bad5131  p = false≢true (cong lower p)
  cut5131 : Adequate {ℓ} ((op (op (var 0) (op (var 0) (op (var 1) (var 0)))) (op (var 2) (var 1))) , (var 2)) → ⊥
  cut5131  adequate = bad5131  (Adequate.valid adequate Two boolean env1)
  bad5132 : PathP (λ _ → Two) (bop (bop b0 (bop b0 (bop b0 b0))) (bop b0 b0)) b1 → ⊥
  bad5132  p = false≢true (cong lower p)
  cut5132 : Adequate {ℓ} ((op (op (var 0) (op (var 0) (op (var 1) (var 0)))) (op (var 2) (var 1))) , (var 3)) → ⊥
  cut5132  adequate = bad5132  (Adequate.valid adequate Two boolean env5)
  bad5133 : PathP (λ _ → Two) (bop (bop b0 (bop b0 (bop b0 b0))) (bop b1 b1)) b0 → ⊥
  bad5133  p = false≢true (sym (cong lower p))
  cut5133 : Adequate {ℓ} ((op (op (var 0) (op (var 0) (op (var 1) (var 0)))) (op (var 2) (var 2))) , (var 0)) → ⊥
  cut5133  adequate = bad5133  (Adequate.valid adequate Two boolean env1)
  bad5134 : PathP (λ _ → Two) (bop (bop b0 (bop b0 (bop b0 b0))) (bop b1 b1)) b0 → ⊥
  bad5134  p = false≢true (sym (cong lower p))
  cut5134 : Adequate {ℓ} ((op (op (var 0) (op (var 0) (op (var 1) (var 0)))) (op (var 2) (var 2))) , (var 1)) → ⊥
  cut5134  adequate = bad5134  (Adequate.valid adequate Two boolean env1)
  bad5135 : PathP (λ _ → Two) (bop (bop b1 (bop b1 (bop b1 b1))) (bop b0 b0)) b0 → ⊥
  bad5135  p = false≢true (sym (cong lower p))
  cut5135 : Adequate {ℓ} ((op (op (var 0) (op (var 0) (op (var 1) (var 0)))) (op (var 2) (var 2))) , (var 2)) → ⊥
  cut5135  adequate = bad5135  (Adequate.valid adequate Two boolean env7)
  bad5136 : PathP (λ _ → Two) (bop (bop b0 (bop b0 (bop b0 b0))) (bop b0 b0)) b1 → ⊥
  bad5136  p = false≢true (cong lower p)
  cut5136 : Adequate {ℓ} ((op (op (var 0) (op (var 0) (op (var 1) (var 0)))) (op (var 2) (var 2))) , (var 3)) → ⊥
  cut5136  adequate = bad5136  (Adequate.valid adequate Two boolean env5)
  bad5137 : PathP (λ _ → Two) (bop (bop b0 (bop b0 (bop b0 b0))) (bop b1 b1)) b0 → ⊥
  bad5137  p = false≢true (sym (cong lower p))
  cut5137 : Adequate {ℓ} ((op (op (var 0) (op (var 0) (op (var 1) (var 0)))) (op (var 2) (var 3))) , (var 0)) → ⊥
  cut5137  adequate = bad5137  (Adequate.valid adequate Two boolean env8)
  bad5138 : PathP (λ _ → Two) (bop (bop b0 (bop b0 (bop b0 b0))) (bop b1 b1)) b0 → ⊥
  bad5138  p = false≢true (sym (cong lower p))
  cut5138 : Adequate {ℓ} ((op (op (var 0) (op (var 0) (op (var 1) (var 0)))) (op (var 2) (var 3))) , (var 1)) → ⊥
  cut5138  adequate = bad5138  (Adequate.valid adequate Two boolean env8)
  bad5139 : PathP (λ _ → Two) (bop (bop b0 (bop b0 (bop b0 b0))) (bop b1 b0)) b1 → ⊥
  bad5139  p = false≢true (cong lower p)
  cut5139 : Adequate {ℓ} ((op (op (var 0) (op (var 0) (op (var 1) (var 0)))) (op (var 2) (var 3))) , (var 2)) → ⊥
  cut5139  adequate = bad5139  (Adequate.valid adequate Two boolean env9)
  bad5140 : PathP (λ _ → Two) (bop (bop b0 (bop b0 (bop b0 b0))) (bop b0 b1)) b1 → ⊥
  bad5140  p = false≢true (cong lower p)
  cut5140 : Adequate {ℓ} ((op (op (var 0) (op (var 0) (op (var 1) (var 0)))) (op (var 2) (var 3))) , (var 3)) → ⊥
  cut5140  adequate = bad5140  (Adequate.valid adequate Two boolean env5)
  bad5141 : PathP (λ _ → Two) (bop (bop b0 (bop b0 (bop b0 b0))) (bop b0 b0)) b1 → ⊥
  bad5141  p = false≢true (cong lower p)
  cut5141 : Adequate {ℓ} ((op (op (var 0) (op (var 0) (op (var 1) (var 0)))) (op (var 2) (var 3))) , (var 4)) → ⊥
  cut5141  adequate = bad5141  (Adequate.valid adequate Two boolean env10)
  holds5142 : (z0 z1 : A2) → (mul2 (mul2 z0 (mul2 z0 (mul2 z1 z1))) (mul2 z0 z0)) ≡ z0
  holds5142 z0 z1 = refl
  cut5142 : Adequate {ℓ} ((op (op (var 0) (op (var 0) (op (var 1) (var 1)))) (op (var 0) (var 0))) , (var 0)) → ⊥
  cut5142  = reject2 ((op (op (var 0) (op (var 0) (op (var 1) (var 1)))) (op (var 0) (var 0))) , (var 0)) (λ env → holds5142 (env 0) (env 1))
  bad5143 : PathP (λ _ → Two) (bop (bop b0 (bop b0 (bop b1 b1))) (bop b0 b0)) b1 → ⊥
  bad5143  p = false≢true (cong lower p)
  cut5143 : Adequate {ℓ} ((op (op (var 0) (op (var 0) (op (var 1) (var 1)))) (op (var 0) (var 0))) , (var 1)) → ⊥
  cut5143  adequate = bad5143  (Adequate.valid adequate Two boolean env0)
  bad5144 : PathP (λ _ → Two) (bop (bop b0 (bop b0 (bop b0 b0))) (bop b0 b0)) b1 → ⊥
  bad5144  p = false≢true (cong lower p)
  cut5144 : Adequate {ℓ} ((op (op (var 0) (op (var 0) (op (var 1) (var 1)))) (op (var 0) (var 0))) , (var 2)) → ⊥
  cut5144  adequate = bad5144  (Adequate.valid adequate Two boolean env1)
  bad5145 : PathP (λ _ → Two) (bop (bop b1 (bop b1 (bop b0 b0))) (bop b1 b0)) b1 → ⊥
  bad5145  p = false≢true (cong lower p)
  cut5145 : Adequate {ℓ} ((op (op (var 0) (op (var 0) (op (var 1) (var 1)))) (op (var 0) (var 1))) , (var 0)) → ⊥
  cut5145  adequate = bad5145  (Adequate.valid adequate Two boolean env2)
  bad5146 : PathP (λ _ → Two) (bop (bop b0 (bop b0 (bop b1 b1))) (bop b0 b1)) b1 → ⊥
  bad5146  p = false≢true (cong lower p)
  cut5146 : Adequate {ℓ} ((op (op (var 0) (op (var 0) (op (var 1) (var 1)))) (op (var 0) (var 1))) , (var 1)) → ⊥
  cut5146  adequate = bad5146  (Adequate.valid adequate Two boolean env0)
  bad5147 : PathP (λ _ → Two) (bop (bop b0 (bop b0 (bop b0 b0))) (bop b0 b0)) b1 → ⊥
  bad5147  p = false≢true (cong lower p)
  cut5147 : Adequate {ℓ} ((op (op (var 0) (op (var 0) (op (var 1) (var 1)))) (op (var 0) (var 1))) , (var 2)) → ⊥
  cut5147  adequate = bad5147  (Adequate.valid adequate Two boolean env1)
  bad5148 : PathP (λ _ → Two) (bop (bop b1 (bop b1 (bop b0 b0))) (bop b1 b0)) b1 → ⊥
  bad5148  p = false≢true (cong lower p)
  cut5148 : Adequate {ℓ} ((op (op (var 0) (op (var 0) (op (var 1) (var 1)))) (op (var 0) (var 2))) , (var 0)) → ⊥
  cut5148  adequate = bad5148  (Adequate.valid adequate Two boolean env6)
  bad5149 : PathP (λ _ → Two) (bop (bop b0 (bop b0 (bop b1 b1))) (bop b0 b0)) b1 → ⊥
  bad5149  p = false≢true (cong lower p)
  cut5149 : Adequate {ℓ} ((op (op (var 0) (op (var 0) (op (var 1) (var 1)))) (op (var 0) (var 2))) , (var 1)) → ⊥
  cut5149  adequate = bad5149  (Adequate.valid adequate Two boolean env4)
  bad5150 : PathP (λ _ → Two) (bop (bop b0 (bop b0 (bop b0 b0))) (bop b0 b1)) b1 → ⊥
  bad5150  p = false≢true (cong lower p)
  cut5150 : Adequate {ℓ} ((op (op (var 0) (op (var 0) (op (var 1) (var 1)))) (op (var 0) (var 2))) , (var 2)) → ⊥
  cut5150  adequate = bad5150  (Adequate.valid adequate Two boolean env1)
  bad5151 : PathP (λ _ → Two) (bop (bop b0 (bop b0 (bop b0 b0))) (bop b0 b0)) b1 → ⊥
  bad5151  p = false≢true (cong lower p)
  cut5151 : Adequate {ℓ} ((op (op (var 0) (op (var 0) (op (var 1) (var 1)))) (op (var 0) (var 2))) , (var 3)) → ⊥
  cut5151  adequate = bad5151  (Adequate.valid adequate Two boolean env5)
  bad5152 : PathP (λ _ → Two) (bop (bop b1 (bop b1 (bop b0 b0))) (bop b0 b1)) b1 → ⊥
  bad5152  p = false≢true (cong lower p)
  cut5152 : Adequate {ℓ} ((op (op (var 0) (op (var 0) (op (var 1) (var 1)))) (op (var 1) (var 0))) , (var 0)) → ⊥
  cut5152  adequate = bad5152  (Adequate.valid adequate Two boolean env2)
  bad5153 : PathP (λ _ → Two) (bop (bop b0 (bop b0 (bop b1 b1))) (bop b1 b0)) b1 → ⊥
  bad5153  p = false≢true (cong lower p)
  cut5153 : Adequate {ℓ} ((op (op (var 0) (op (var 0) (op (var 1) (var 1)))) (op (var 1) (var 0))) , (var 1)) → ⊥
  cut5153  adequate = bad5153  (Adequate.valid adequate Two boolean env0)
  bad5154 : PathP (λ _ → Two) (bop (bop b0 (bop b0 (bop b0 b0))) (bop b0 b0)) b1 → ⊥
  bad5154  p = false≢true (cong lower p)
  cut5154 : Adequate {ℓ} ((op (op (var 0) (op (var 0) (op (var 1) (var 1)))) (op (var 1) (var 0))) , (var 2)) → ⊥
  cut5154  adequate = bad5154  (Adequate.valid adequate Two boolean env1)
  bad5155 : PathP (λ _ → Two) (bop (bop b0 (bop b0 (bop b1 b1))) (bop b1 b1)) b0 → ⊥
  bad5155  p = false≢true (sym (cong lower p))
  cut5155 : Adequate {ℓ} ((op (op (var 0) (op (var 0) (op (var 1) (var 1)))) (op (var 1) (var 1))) , (var 0)) → ⊥
  cut5155  adequate = bad5155  (Adequate.valid adequate Two boolean env0)
  holds5156 : (z0 z1 : A3) → (mul3 (mul3 z0 (mul3 z0 (mul3 z1 z1))) (mul3 z1 z1)) ≡ z1
  holds5156 z0 z1 = refl
  cut5156 : Adequate {ℓ} ((op (op (var 0) (op (var 0) (op (var 1) (var 1)))) (op (var 1) (var 1))) , (var 1)) → ⊥
  cut5156  = reject3 ((op (op (var 0) (op (var 0) (op (var 1) (var 1)))) (op (var 1) (var 1))) , (var 1)) (λ env → holds5156 (env 0) (env 1))
  bad5157 : PathP (λ _ → Two) (bop (bop b0 (bop b0 (bop b0 b0))) (bop b0 b0)) b1 → ⊥
  bad5157  p = false≢true (cong lower p)
  cut5157 : Adequate {ℓ} ((op (op (var 0) (op (var 0) (op (var 1) (var 1)))) (op (var 1) (var 1))) , (var 2)) → ⊥
  cut5157  adequate = bad5157  (Adequate.valid adequate Two boolean env1)
  bad5158 : PathP (λ _ → Two) (bop (bop b0 (bop b0 (bop b1 b1))) (bop b1 b1)) b0 → ⊥
  bad5158  p = false≢true (sym (cong lower p))
  cut5158 : Adequate {ℓ} ((op (op (var 0) (op (var 0) (op (var 1) (var 1)))) (op (var 1) (var 2))) , (var 0)) → ⊥
  cut5158  adequate = bad5158  (Adequate.valid adequate Two boolean env3)
  bad5159 : PathP (λ _ → Two) (bop (bop b0 (bop b0 (bop b1 b1))) (bop b1 b0)) b1 → ⊥
  bad5159  p = false≢true (cong lower p)
  cut5159 : Adequate {ℓ} ((op (op (var 0) (op (var 0) (op (var 1) (var 1)))) (op (var 1) (var 2))) , (var 1)) → ⊥
  cut5159  adequate = bad5159  (Adequate.valid adequate Two boolean env4)
  bad5160 : PathP (λ _ → Two) (bop (bop b0 (bop b0 (bop b0 b0))) (bop b0 b1)) b1 → ⊥
  bad5160  p = false≢true (cong lower p)
  cut5160 : Adequate {ℓ} ((op (op (var 0) (op (var 0) (op (var 1) (var 1)))) (op (var 1) (var 2))) , (var 2)) → ⊥
  cut5160  adequate = bad5160  (Adequate.valid adequate Two boolean env1)
  bad5161 : PathP (λ _ → Two) (bop (bop b0 (bop b0 (bop b0 b0))) (bop b0 b0)) b1 → ⊥
  bad5161  p = false≢true (cong lower p)
  cut5161 : Adequate {ℓ} ((op (op (var 0) (op (var 0) (op (var 1) (var 1)))) (op (var 1) (var 2))) , (var 3)) → ⊥
  cut5161  adequate = bad5161  (Adequate.valid adequate Two boolean env5)
  bad5162 : PathP (λ _ → Two) (bop (bop b1 (bop b1 (bop b0 b0))) (bop b0 b1)) b1 → ⊥
  bad5162  p = false≢true (cong lower p)
  cut5162 : Adequate {ℓ} ((op (op (var 0) (op (var 0) (op (var 1) (var 1)))) (op (var 2) (var 0))) , (var 0)) → ⊥
  cut5162  adequate = bad5162  (Adequate.valid adequate Two boolean env6)
  bad5163 : PathP (λ _ → Two) (bop (bop b0 (bop b0 (bop b1 b1))) (bop b0 b0)) b1 → ⊥
  bad5163  p = false≢true (cong lower p)
  cut5163 : Adequate {ℓ} ((op (op (var 0) (op (var 0) (op (var 1) (var 1)))) (op (var 2) (var 0))) , (var 1)) → ⊥
  cut5163  adequate = bad5163  (Adequate.valid adequate Two boolean env4)
  bad5164 : PathP (λ _ → Two) (bop (bop b0 (bop b0 (bop b0 b0))) (bop b1 b0)) b1 → ⊥
  bad5164  p = false≢true (cong lower p)
  cut5164 : Adequate {ℓ} ((op (op (var 0) (op (var 0) (op (var 1) (var 1)))) (op (var 2) (var 0))) , (var 2)) → ⊥
  cut5164  adequate = bad5164  (Adequate.valid adequate Two boolean env1)
  bad5165 : PathP (λ _ → Two) (bop (bop b0 (bop b0 (bop b0 b0))) (bop b0 b0)) b1 → ⊥
  bad5165  p = false≢true (cong lower p)
  cut5165 : Adequate {ℓ} ((op (op (var 0) (op (var 0) (op (var 1) (var 1)))) (op (var 2) (var 0))) , (var 3)) → ⊥
  cut5165  adequate = bad5165  (Adequate.valid adequate Two boolean env5)
  bad5166 : PathP (λ _ → Two) (bop (bop b0 (bop b0 (bop b1 b1))) (bop b1 b1)) b0 → ⊥
  bad5166  p = false≢true (sym (cong lower p))
  cut5166 : Adequate {ℓ} ((op (op (var 0) (op (var 0) (op (var 1) (var 1)))) (op (var 2) (var 1))) , (var 0)) → ⊥
  cut5166  adequate = bad5166  (Adequate.valid adequate Two boolean env3)
  bad5167 : PathP (λ _ → Two) (bop (bop b0 (bop b0 (bop b1 b1))) (bop b0 b1)) b1 → ⊥
  bad5167  p = false≢true (cong lower p)
  cut5167 : Adequate {ℓ} ((op (op (var 0) (op (var 0) (op (var 1) (var 1)))) (op (var 2) (var 1))) , (var 1)) → ⊥
  cut5167  adequate = bad5167  (Adequate.valid adequate Two boolean env4)
  bad5168 : PathP (λ _ → Two) (bop (bop b0 (bop b0 (bop b0 b0))) (bop b1 b0)) b1 → ⊥
  bad5168  p = false≢true (cong lower p)
  cut5168 : Adequate {ℓ} ((op (op (var 0) (op (var 0) (op (var 1) (var 1)))) (op (var 2) (var 1))) , (var 2)) → ⊥
  cut5168  adequate = bad5168  (Adequate.valid adequate Two boolean env1)
  bad5169 : PathP (λ _ → Two) (bop (bop b0 (bop b0 (bop b0 b0))) (bop b0 b0)) b1 → ⊥
  bad5169  p = false≢true (cong lower p)
  cut5169 : Adequate {ℓ} ((op (op (var 0) (op (var 0) (op (var 1) (var 1)))) (op (var 2) (var 1))) , (var 3)) → ⊥
  cut5169  adequate = bad5169  (Adequate.valid adequate Two boolean env5)
  bad5170 : PathP (λ _ → Two) (bop (bop b0 (bop b0 (bop b0 b0))) (bop b1 b1)) b0 → ⊥
  bad5170  p = false≢true (sym (cong lower p))
  cut5170 : Adequate {ℓ} ((op (op (var 0) (op (var 0) (op (var 1) (var 1)))) (op (var 2) (var 2))) , (var 0)) → ⊥
  cut5170  adequate = bad5170  (Adequate.valid adequate Two boolean env1)
  bad5171 : PathP (λ _ → Two) (bop (bop b0 (bop b0 (bop b0 b0))) (bop b1 b1)) b0 → ⊥
  bad5171  p = false≢true (sym (cong lower p))
  cut5171 : Adequate {ℓ} ((op (op (var 0) (op (var 0) (op (var 1) (var 1)))) (op (var 2) (var 2))) , (var 1)) → ⊥
  cut5171  adequate = bad5171  (Adequate.valid adequate Two boolean env1)
  bad5172 : PathP (λ _ → Two) (bop (bop b1 (bop b1 (bop b1 b1))) (bop b0 b0)) b0 → ⊥
  bad5172  p = false≢true (sym (cong lower p))
  cut5172 : Adequate {ℓ} ((op (op (var 0) (op (var 0) (op (var 1) (var 1)))) (op (var 2) (var 2))) , (var 2)) → ⊥
  cut5172  adequate = bad5172  (Adequate.valid adequate Two boolean env7)
  bad5173 : PathP (λ _ → Two) (bop (bop b0 (bop b0 (bop b0 b0))) (bop b0 b0)) b1 → ⊥
  bad5173  p = false≢true (cong lower p)
  cut5173 : Adequate {ℓ} ((op (op (var 0) (op (var 0) (op (var 1) (var 1)))) (op (var 2) (var 2))) , (var 3)) → ⊥
  cut5173  adequate = bad5173  (Adequate.valid adequate Two boolean env5)
  bad5174 : PathP (λ _ → Two) (bop (bop b0 (bop b0 (bop b0 b0))) (bop b1 b1)) b0 → ⊥
  bad5174  p = false≢true (sym (cong lower p))
  cut5174 : Adequate {ℓ} ((op (op (var 0) (op (var 0) (op (var 1) (var 1)))) (op (var 2) (var 3))) , (var 0)) → ⊥
  cut5174  adequate = bad5174  (Adequate.valid adequate Two boolean env8)
  bad5175 : PathP (λ _ → Two) (bop (bop b0 (bop b0 (bop b0 b0))) (bop b1 b1)) b0 → ⊥
  bad5175  p = false≢true (sym (cong lower p))
  cut5175 : Adequate {ℓ} ((op (op (var 0) (op (var 0) (op (var 1) (var 1)))) (op (var 2) (var 3))) , (var 1)) → ⊥
  cut5175  adequate = bad5175  (Adequate.valid adequate Two boolean env8)
  bad5176 : PathP (λ _ → Two) (bop (bop b0 (bop b0 (bop b0 b0))) (bop b1 b0)) b1 → ⊥
  bad5176  p = false≢true (cong lower p)
  cut5176 : Adequate {ℓ} ((op (op (var 0) (op (var 0) (op (var 1) (var 1)))) (op (var 2) (var 3))) , (var 2)) → ⊥
  cut5176  adequate = bad5176  (Adequate.valid adequate Two boolean env9)
  bad5177 : PathP (λ _ → Two) (bop (bop b0 (bop b0 (bop b0 b0))) (bop b0 b1)) b1 → ⊥
  bad5177  p = false≢true (cong lower p)
  cut5177 : Adequate {ℓ} ((op (op (var 0) (op (var 0) (op (var 1) (var 1)))) (op (var 2) (var 3))) , (var 3)) → ⊥
  cut5177  adequate = bad5177  (Adequate.valid adequate Two boolean env5)
  bad5178 : PathP (λ _ → Two) (bop (bop b0 (bop b0 (bop b0 b0))) (bop b0 b0)) b1 → ⊥
  bad5178  p = false≢true (cong lower p)
  cut5178 : Adequate {ℓ} ((op (op (var 0) (op (var 0) (op (var 1) (var 1)))) (op (var 2) (var 3))) , (var 4)) → ⊥
  cut5178  adequate = bad5178  (Adequate.valid adequate Two boolean env10)
  holds5179 : (z0 z1 z2 : A2) → (mul2 (mul2 z0 (mul2 z0 (mul2 z1 z2))) (mul2 z0 z0)) ≡ z0
  holds5179 z0 z1 z2 = refl
  cut5179 : Adequate {ℓ} ((op (op (var 0) (op (var 0) (op (var 1) (var 2)))) (op (var 0) (var 0))) , (var 0)) → ⊥
  cut5179  = reject2 ((op (op (var 0) (op (var 0) (op (var 1) (var 2)))) (op (var 0) (var 0))) , (var 0)) (λ env → holds5179 (env 0) (env 1) (env 2))
  bad5180 : PathP (λ _ → Two) (bop (bop b0 (bop b0 (bop b1 b0))) (bop b0 b0)) b1 → ⊥
  bad5180  p = false≢true (cong lower p)
  cut5180 : Adequate {ℓ} ((op (op (var 0) (op (var 0) (op (var 1) (var 2)))) (op (var 0) (var 0))) , (var 1)) → ⊥
  cut5180  adequate = bad5180  (Adequate.valid adequate Two boolean env4)
  bad5181 : PathP (λ _ → Two) (bop (bop b0 (bop b0 (bop b0 b1))) (bop b0 b0)) b1 → ⊥
  bad5181  p = false≢true (cong lower p)
  cut5181 : Adequate {ℓ} ((op (op (var 0) (op (var 0) (op (var 1) (var 2)))) (op (var 0) (var 0))) , (var 2)) → ⊥
  cut5181  adequate = bad5181  (Adequate.valid adequate Two boolean env1)
  bad5182 : PathP (λ _ → Two) (bop (bop b0 (bop b0 (bop b0 b0))) (bop b0 b0)) b1 → ⊥
  bad5182  p = false≢true (cong lower p)
  cut5182 : Adequate {ℓ} ((op (op (var 0) (op (var 0) (op (var 1) (var 2)))) (op (var 0) (var 0))) , (var 3)) → ⊥
  cut5182  adequate = bad5182  (Adequate.valid adequate Two boolean env5)
  bad5183 : PathP (λ _ → Two) (bop (bop b1 (bop b1 (bop b0 b0))) (bop b1 b0)) b1 → ⊥
  bad5183  p = false≢true (cong lower p)
  cut5183 : Adequate {ℓ} ((op (op (var 0) (op (var 0) (op (var 1) (var 2)))) (op (var 0) (var 1))) , (var 0)) → ⊥
  cut5183  adequate = bad5183  (Adequate.valid adequate Two boolean env6)
  bad5184 : PathP (λ _ → Two) (bop (bop b0 (bop b0 (bop b1 b0))) (bop b0 b1)) b1 → ⊥
  bad5184  p = false≢true (cong lower p)
  cut5184 : Adequate {ℓ} ((op (op (var 0) (op (var 0) (op (var 1) (var 2)))) (op (var 0) (var 1))) , (var 1)) → ⊥
  cut5184  adequate = bad5184  (Adequate.valid adequate Two boolean env4)
  bad5185 : PathP (λ _ → Two) (bop (bop b0 (bop b0 (bop b0 b1))) (bop b0 b0)) b1 → ⊥
  bad5185  p = false≢true (cong lower p)
  cut5185 : Adequate {ℓ} ((op (op (var 0) (op (var 0) (op (var 1) (var 2)))) (op (var 0) (var 1))) , (var 2)) → ⊥
  cut5185  adequate = bad5185  (Adequate.valid adequate Two boolean env1)
  bad5186 : PathP (λ _ → Two) (bop (bop b0 (bop b0 (bop b0 b0))) (bop b0 b0)) b1 → ⊥
  bad5186  p = false≢true (cong lower p)
  cut5186 : Adequate {ℓ} ((op (op (var 0) (op (var 0) (op (var 1) (var 2)))) (op (var 0) (var 1))) , (var 3)) → ⊥
  cut5186  adequate = bad5186  (Adequate.valid adequate Two boolean env5)
  bad5187 : PathP (λ _ → Two) (bop (bop b1 (bop b1 (bop b0 b0))) (bop b1 b0)) b1 → ⊥
  bad5187  p = false≢true (cong lower p)
  cut5187 : Adequate {ℓ} ((op (op (var 0) (op (var 0) (op (var 1) (var 2)))) (op (var 0) (var 2))) , (var 0)) → ⊥
  cut5187  adequate = bad5187  (Adequate.valid adequate Two boolean env6)
  bad5188 : PathP (λ _ → Two) (bop (bop b0 (bop b0 (bop b1 b0))) (bop b0 b0)) b1 → ⊥
  bad5188  p = false≢true (cong lower p)
  cut5188 : Adequate {ℓ} ((op (op (var 0) (op (var 0) (op (var 1) (var 2)))) (op (var 0) (var 2))) , (var 1)) → ⊥
  cut5188  adequate = bad5188  (Adequate.valid adequate Two boolean env4)
  bad5189 : PathP (λ _ → Two) (bop (bop b0 (bop b0 (bop b0 b1))) (bop b0 b1)) b1 → ⊥
  bad5189  p = false≢true (cong lower p)
  cut5189 : Adequate {ℓ} ((op (op (var 0) (op (var 0) (op (var 1) (var 2)))) (op (var 0) (var 2))) , (var 2)) → ⊥
  cut5189  adequate = bad5189  (Adequate.valid adequate Two boolean env1)
  bad5190 : PathP (λ _ → Two) (bop (bop b0 (bop b0 (bop b0 b0))) (bop b0 b0)) b1 → ⊥
  bad5190  p = false≢true (cong lower p)
  cut5190 : Adequate {ℓ} ((op (op (var 0) (op (var 0) (op (var 1) (var 2)))) (op (var 0) (var 2))) , (var 3)) → ⊥
  cut5190  adequate = bad5190  (Adequate.valid adequate Two boolean env5)
  env11 : ℕ → Two
  env11 zero = b1
  env11 (suc zero) = b0
  env11 (suc (suc zero)) = b0
  env11 (suc (suc (suc zero))) = b0
  env11 (suc (suc (suc (suc rest)))) = b0
  bad5191 : PathP (λ _ → Two) (bop (bop b1 (bop b1 (bop b0 b0))) (bop b1 b0)) b1 → ⊥
  bad5191  p = false≢true (cong lower p)
  cut5191 : Adequate {ℓ} ((op (op (var 0) (op (var 0) (op (var 1) (var 2)))) (op (var 0) (var 3))) , (var 0)) → ⊥
  cut5191  adequate = bad5191  (Adequate.valid adequate Two boolean env11)
  env12 : ℕ → Two
  env12 zero = b0
  env12 (suc zero) = b1
  env12 (suc (suc zero)) = b0
  env12 (suc (suc (suc zero))) = b0
  env12 (suc (suc (suc (suc rest)))) = b0
  bad5192 : PathP (λ _ → Two) (bop (bop b0 (bop b0 (bop b1 b0))) (bop b0 b0)) b1 → ⊥
  bad5192  p = false≢true (cong lower p)
  cut5192 : Adequate {ℓ} ((op (op (var 0) (op (var 0) (op (var 1) (var 2)))) (op (var 0) (var 3))) , (var 1)) → ⊥
  cut5192  adequate = bad5192  (Adequate.valid adequate Two boolean env12)
  bad5193 : PathP (λ _ → Two) (bop (bop b0 (bop b0 (bop b0 b1))) (bop b0 b0)) b1 → ⊥
  bad5193  p = false≢true (cong lower p)
  cut5193 : Adequate {ℓ} ((op (op (var 0) (op (var 0) (op (var 1) (var 2)))) (op (var 0) (var 3))) , (var 2)) → ⊥
  cut5193  adequate = bad5193  (Adequate.valid adequate Two boolean env9)
  bad5194 : PathP (λ _ → Two) (bop (bop b0 (bop b0 (bop b0 b0))) (bop b0 b1)) b1 → ⊥
  bad5194  p = false≢true (cong lower p)
  cut5194 : Adequate {ℓ} ((op (op (var 0) (op (var 0) (op (var 1) (var 2)))) (op (var 0) (var 3))) , (var 3)) → ⊥
  cut5194  adequate = bad5194  (Adequate.valid adequate Two boolean env5)
  bad5195 : PathP (λ _ → Two) (bop (bop b0 (bop b0 (bop b0 b0))) (bop b0 b0)) b1 → ⊥
  bad5195  p = false≢true (cong lower p)
  cut5195 : Adequate {ℓ} ((op (op (var 0) (op (var 0) (op (var 1) (var 2)))) (op (var 0) (var 3))) , (var 4)) → ⊥
  cut5195  adequate = bad5195  (Adequate.valid adequate Two boolean env10)
  bad5196 : PathP (λ _ → Two) (bop (bop b1 (bop b1 (bop b0 b0))) (bop b0 b1)) b1 → ⊥
  bad5196  p = false≢true (cong lower p)
  cut5196 : Adequate {ℓ} ((op (op (var 0) (op (var 0) (op (var 1) (var 2)))) (op (var 1) (var 0))) , (var 0)) → ⊥
  cut5196  adequate = bad5196  (Adequate.valid adequate Two boolean env6)
  bad5197 : PathP (λ _ → Two) (bop (bop b0 (bop b0 (bop b1 b0))) (bop b1 b0)) b1 → ⊥
  bad5197  p = false≢true (cong lower p)
  cut5197 : Adequate {ℓ} ((op (op (var 0) (op (var 0) (op (var 1) (var 2)))) (op (var 1) (var 0))) , (var 1)) → ⊥
  cut5197  adequate = bad5197  (Adequate.valid adequate Two boolean env4)
  bad5198 : PathP (λ _ → Two) (bop (bop b0 (bop b0 (bop b0 b1))) (bop b0 b0)) b1 → ⊥
  bad5198  p = false≢true (cong lower p)
  cut5198 : Adequate {ℓ} ((op (op (var 0) (op (var 0) (op (var 1) (var 2)))) (op (var 1) (var 0))) , (var 2)) → ⊥
  cut5198  adequate = bad5198  (Adequate.valid adequate Two boolean env1)
  bad5199 : PathP (λ _ → Two) (bop (bop b0 (bop b0 (bop b0 b0))) (bop b0 b0)) b1 → ⊥
  bad5199  p = false≢true (cong lower p)
  cut5199 : Adequate {ℓ} ((op (op (var 0) (op (var 0) (op (var 1) (var 2)))) (op (var 1) (var 0))) , (var 3)) → ⊥
  cut5199  adequate = bad5199  (Adequate.valid adequate Two boolean env5)
  bad5200 : PathP (λ _ → Two) (bop (bop b0 (bop b0 (bop b1 b0))) (bop b1 b1)) b0 → ⊥
  bad5200  p = false≢true (sym (cong lower p))
  cut5200 : Adequate {ℓ} ((op (op (var 0) (op (var 0) (op (var 1) (var 2)))) (op (var 1) (var 1))) , (var 0)) → ⊥
  cut5200  adequate = bad5200  (Adequate.valid adequate Two boolean env4)
  holds5201 : (z0 z1 z2 : A3) → (mul3 (mul3 z0 (mul3 z0 (mul3 z1 z2))) (mul3 z1 z1)) ≡ z1
  holds5201 z0 z1 z2 = refl
  cut5201 : Adequate {ℓ} ((op (op (var 0) (op (var 0) (op (var 1) (var 2)))) (op (var 1) (var 1))) , (var 1)) → ⊥
  cut5201  = reject3 ((op (op (var 0) (op (var 0) (op (var 1) (var 2)))) (op (var 1) (var 1))) , (var 1)) (λ env → holds5201 (env 0) (env 1) (env 2))
  bad5202 : PathP (λ _ → Two) (bop (bop b0 (bop b0 (bop b0 b1))) (bop b0 b0)) b1 → ⊥
  bad5202  p = false≢true (cong lower p)
  cut5202 : Adequate {ℓ} ((op (op (var 0) (op (var 0) (op (var 1) (var 2)))) (op (var 1) (var 1))) , (var 2)) → ⊥
  cut5202  adequate = bad5202  (Adequate.valid adequate Two boolean env1)
  bad5203 : PathP (λ _ → Two) (bop (bop b0 (bop b0 (bop b0 b0))) (bop b0 b0)) b1 → ⊥
  bad5203  p = false≢true (cong lower p)
  cut5203 : Adequate {ℓ} ((op (op (var 0) (op (var 0) (op (var 1) (var 2)))) (op (var 1) (var 1))) , (var 3)) → ⊥
  cut5203  adequate = bad5203  (Adequate.valid adequate Two boolean env5)
  bad5204 : PathP (λ _ → Two) (bop (bop b0 (bop b0 (bop b1 b1))) (bop b1 b1)) b0 → ⊥
  bad5204  p = false≢true (sym (cong lower p))
  cut5204 : Adequate {ℓ} ((op (op (var 0) (op (var 0) (op (var 1) (var 2)))) (op (var 1) (var 2))) , (var 0)) → ⊥
  cut5204  adequate = bad5204  (Adequate.valid adequate Two boolean env3)
  bad5205 : PathP (λ _ → Two) (bop (bop b0 (bop b0 (bop b1 b0))) (bop b1 b0)) b1 → ⊥
  bad5205  p = false≢true (cong lower p)
  cut5205 : Adequate {ℓ} ((op (op (var 0) (op (var 0) (op (var 1) (var 2)))) (op (var 1) (var 2))) , (var 1)) → ⊥
  cut5205  adequate = bad5205  (Adequate.valid adequate Two boolean env4)
  bad5206 : PathP (λ _ → Two) (bop (bop b0 (bop b0 (bop b0 b1))) (bop b0 b1)) b1 → ⊥
  bad5206  p = false≢true (cong lower p)
  cut5206 : Adequate {ℓ} ((op (op (var 0) (op (var 0) (op (var 1) (var 2)))) (op (var 1) (var 2))) , (var 2)) → ⊥
  cut5206  adequate = bad5206  (Adequate.valid adequate Two boolean env1)
  bad5207 : PathP (λ _ → Two) (bop (bop b0 (bop b0 (bop b0 b0))) (bop b0 b0)) b1 → ⊥
  bad5207  p = false≢true (cong lower p)
  cut5207 : Adequate {ℓ} ((op (op (var 0) (op (var 0) (op (var 1) (var 2)))) (op (var 1) (var 2))) , (var 3)) → ⊥
  cut5207  adequate = bad5207  (Adequate.valid adequate Two boolean env5)
  env13 : ℕ → Two
  env13 zero = b0
  env13 (suc zero) = b1
  env13 (suc (suc zero)) = b0
  env13 (suc (suc (suc zero))) = b1
  env13 (suc (suc (suc (suc rest)))) = b0
  bad5208 : PathP (λ _ → Two) (bop (bop b0 (bop b0 (bop b1 b0))) (bop b1 b1)) b0 → ⊥
  bad5208  p = false≢true (sym (cong lower p))
  cut5208 : Adequate {ℓ} ((op (op (var 0) (op (var 0) (op (var 1) (var 2)))) (op (var 1) (var 3))) , (var 0)) → ⊥
  cut5208  adequate = bad5208  (Adequate.valid adequate Two boolean env13)
  bad5209 : PathP (λ _ → Two) (bop (bop b0 (bop b0 (bop b1 b0))) (bop b1 b0)) b1 → ⊥
  bad5209  p = false≢true (cong lower p)
  cut5209 : Adequate {ℓ} ((op (op (var 0) (op (var 0) (op (var 1) (var 2)))) (op (var 1) (var 3))) , (var 1)) → ⊥
  cut5209  adequate = bad5209  (Adequate.valid adequate Two boolean env12)
  bad5210 : PathP (λ _ → Two) (bop (bop b0 (bop b0 (bop b0 b1))) (bop b0 b0)) b1 → ⊥
  bad5210  p = false≢true (cong lower p)
  cut5210 : Adequate {ℓ} ((op (op (var 0) (op (var 0) (op (var 1) (var 2)))) (op (var 1) (var 3))) , (var 2)) → ⊥
  cut5210  adequate = bad5210  (Adequate.valid adequate Two boolean env9)
  bad5211 : PathP (λ _ → Two) (bop (bop b0 (bop b0 (bop b0 b0))) (bop b0 b1)) b1 → ⊥
  bad5211  p = false≢true (cong lower p)
  cut5211 : Adequate {ℓ} ((op (op (var 0) (op (var 0) (op (var 1) (var 2)))) (op (var 1) (var 3))) , (var 3)) → ⊥
  cut5211  adequate = bad5211  (Adequate.valid adequate Two boolean env5)
  bad5212 : PathP (λ _ → Two) (bop (bop b0 (bop b0 (bop b0 b0))) (bop b0 b0)) b1 → ⊥
  bad5212  p = false≢true (cong lower p)
  cut5212 : Adequate {ℓ} ((op (op (var 0) (op (var 0) (op (var 1) (var 2)))) (op (var 1) (var 3))) , (var 4)) → ⊥
  cut5212  adequate = bad5212  (Adequate.valid adequate Two boolean env10)
  bad5213 : PathP (λ _ → Two) (bop (bop b1 (bop b1 (bop b0 b0))) (bop b0 b1)) b1 → ⊥
  bad5213  p = false≢true (cong lower p)
  cut5213 : Adequate {ℓ} ((op (op (var 0) (op (var 0) (op (var 1) (var 2)))) (op (var 2) (var 0))) , (var 0)) → ⊥
  cut5213  adequate = bad5213  (Adequate.valid adequate Two boolean env6)
  bad5214 : PathP (λ _ → Two) (bop (bop b0 (bop b0 (bop b1 b0))) (bop b0 b0)) b1 → ⊥
  bad5214  p = false≢true (cong lower p)
  cut5214 : Adequate {ℓ} ((op (op (var 0) (op (var 0) (op (var 1) (var 2)))) (op (var 2) (var 0))) , (var 1)) → ⊥
  cut5214  adequate = bad5214  (Adequate.valid adequate Two boolean env4)
  bad5215 : PathP (λ _ → Two) (bop (bop b0 (bop b0 (bop b0 b1))) (bop b1 b0)) b1 → ⊥
  bad5215  p = false≢true (cong lower p)
  cut5215 : Adequate {ℓ} ((op (op (var 0) (op (var 0) (op (var 1) (var 2)))) (op (var 2) (var 0))) , (var 2)) → ⊥
  cut5215  adequate = bad5215  (Adequate.valid adequate Two boolean env1)
  bad5216 : PathP (λ _ → Two) (bop (bop b0 (bop b0 (bop b0 b0))) (bop b0 b0)) b1 → ⊥
  bad5216  p = false≢true (cong lower p)
  cut5216 : Adequate {ℓ} ((op (op (var 0) (op (var 0) (op (var 1) (var 2)))) (op (var 2) (var 0))) , (var 3)) → ⊥
  cut5216  adequate = bad5216  (Adequate.valid adequate Two boolean env5)
  bad5217 : PathP (λ _ → Two) (bop (bop b0 (bop b0 (bop b1 b1))) (bop b1 b1)) b0 → ⊥
  bad5217  p = false≢true (sym (cong lower p))
  cut5217 : Adequate {ℓ} ((op (op (var 0) (op (var 0) (op (var 1) (var 2)))) (op (var 2) (var 1))) , (var 0)) → ⊥
  cut5217  adequate = bad5217  (Adequate.valid adequate Two boolean env3)
  bad5218 : PathP (λ _ → Two) (bop (bop b0 (bop b0 (bop b1 b0))) (bop b0 b1)) b1 → ⊥
  bad5218  p = false≢true (cong lower p)
  cut5218 : Adequate {ℓ} ((op (op (var 0) (op (var 0) (op (var 1) (var 2)))) (op (var 2) (var 1))) , (var 1)) → ⊥
  cut5218  adequate = bad5218  (Adequate.valid adequate Two boolean env4)
  bad5219 : PathP (λ _ → Two) (bop (bop b0 (bop b0 (bop b0 b1))) (bop b1 b0)) b1 → ⊥
  bad5219  p = false≢true (cong lower p)
  cut5219 : Adequate {ℓ} ((op (op (var 0) (op (var 0) (op (var 1) (var 2)))) (op (var 2) (var 1))) , (var 2)) → ⊥
  cut5219  adequate = bad5219  (Adequate.valid adequate Two boolean env1)
  bad5220 : PathP (λ _ → Two) (bop (bop b0 (bop b0 (bop b0 b0))) (bop b0 b0)) b1 → ⊥
  bad5220  p = false≢true (cong lower p)
  cut5220 : Adequate {ℓ} ((op (op (var 0) (op (var 0) (op (var 1) (var 2)))) (op (var 2) (var 1))) , (var 3)) → ⊥
  cut5220  adequate = bad5220  (Adequate.valid adequate Two boolean env5)
  bad5221 : PathP (λ _ → Two) (bop (bop b0 (bop b0 (bop b0 b1))) (bop b1 b1)) b0 → ⊥
  bad5221  p = false≢true (sym (cong lower p))
  cut5221 : Adequate {ℓ} ((op (op (var 0) (op (var 0) (op (var 1) (var 2)))) (op (var 2) (var 2))) , (var 0)) → ⊥
  cut5221  adequate = bad5221  (Adequate.valid adequate Two boolean env1)
  bad5222 : PathP (λ _ → Two) (bop (bop b0 (bop b0 (bop b0 b1))) (bop b1 b1)) b0 → ⊥
  bad5222  p = false≢true (sym (cong lower p))
  cut5222 : Adequate {ℓ} ((op (op (var 0) (op (var 0) (op (var 1) (var 2)))) (op (var 2) (var 2))) , (var 1)) → ⊥
  cut5222  adequate = bad5222  (Adequate.valid adequate Two boolean env1)
  holds5223 : (z0 z1 z2 : A3) → (mul3 (mul3 z0 (mul3 z0 (mul3 z1 z2))) (mul3 z2 z2)) ≡ z2
  holds5223 z0 z1 z2 = refl
  cut5223 : Adequate {ℓ} ((op (op (var 0) (op (var 0) (op (var 1) (var 2)))) (op (var 2) (var 2))) , (var 2)) → ⊥
  cut5223  = reject3 ((op (op (var 0) (op (var 0) (op (var 1) (var 2)))) (op (var 2) (var 2))) , (var 2)) (λ env → holds5223 (env 0) (env 1) (env 2))
  bad5224 : PathP (λ _ → Two) (bop (bop b0 (bop b0 (bop b0 b0))) (bop b0 b0)) b1 → ⊥
  bad5224  p = false≢true (cong lower p)
  cut5224 : Adequate {ℓ} ((op (op (var 0) (op (var 0) (op (var 1) (var 2)))) (op (var 2) (var 2))) , (var 3)) → ⊥
  cut5224  adequate = bad5224  (Adequate.valid adequate Two boolean env5)
  bad5225 : PathP (λ _ → Two) (bop (bop b0 (bop b0 (bop b0 b1))) (bop b1 b1)) b0 → ⊥
  bad5225  p = false≢true (sym (cong lower p))
  cut5225 : Adequate {ℓ} ((op (op (var 0) (op (var 0) (op (var 1) (var 2)))) (op (var 2) (var 3))) , (var 0)) → ⊥
  cut5225  adequate = bad5225  (Adequate.valid adequate Two boolean env8)
  bad5226 : PathP (λ _ → Two) (bop (bop b0 (bop b0 (bop b0 b1))) (bop b1 b1)) b0 → ⊥
  bad5226  p = false≢true (sym (cong lower p))
  cut5226 : Adequate {ℓ} ((op (op (var 0) (op (var 0) (op (var 1) (var 2)))) (op (var 2) (var 3))) , (var 1)) → ⊥
  cut5226  adequate = bad5226  (Adequate.valid adequate Two boolean env8)
  bad5227 : PathP (λ _ → Two) (bop (bop b0 (bop b0 (bop b0 b1))) (bop b1 b0)) b1 → ⊥
  bad5227  p = false≢true (cong lower p)
  cut5227 : Adequate {ℓ} ((op (op (var 0) (op (var 0) (op (var 1) (var 2)))) (op (var 2) (var 3))) , (var 2)) → ⊥
  cut5227  adequate = bad5227  (Adequate.valid adequate Two boolean env9)
  bad5228 : PathP (λ _ → Two) (bop (bop b0 (bop b0 (bop b0 b0))) (bop b0 b1)) b1 → ⊥
  bad5228  p = false≢true (cong lower p)
  cut5228 : Adequate {ℓ} ((op (op (var 0) (op (var 0) (op (var 1) (var 2)))) (op (var 2) (var 3))) , (var 3)) → ⊥
  cut5228  adequate = bad5228  (Adequate.valid adequate Two boolean env5)
  bad5229 : PathP (λ _ → Two) (bop (bop b0 (bop b0 (bop b0 b0))) (bop b0 b0)) b1 → ⊥
  bad5229  p = false≢true (cong lower p)
  cut5229 : Adequate {ℓ} ((op (op (var 0) (op (var 0) (op (var 1) (var 2)))) (op (var 2) (var 3))) , (var 4)) → ⊥
  cut5229  adequate = bad5229  (Adequate.valid adequate Two boolean env10)
  bad5230 : PathP (λ _ → Two) (bop (bop b1 (bop b1 (bop b0 b0))) (bop b0 b1)) b1 → ⊥
  bad5230  p = false≢true (cong lower p)
  cut5230 : Adequate {ℓ} ((op (op (var 0) (op (var 0) (op (var 1) (var 2)))) (op (var 3) (var 0))) , (var 0)) → ⊥
  cut5230  adequate = bad5230  (Adequate.valid adequate Two boolean env11)
  bad5231 : PathP (λ _ → Two) (bop (bop b0 (bop b0 (bop b1 b0))) (bop b0 b0)) b1 → ⊥
  bad5231  p = false≢true (cong lower p)
  cut5231 : Adequate {ℓ} ((op (op (var 0) (op (var 0) (op (var 1) (var 2)))) (op (var 3) (var 0))) , (var 1)) → ⊥
  cut5231  adequate = bad5231  (Adequate.valid adequate Two boolean env12)
  bad5232 : PathP (λ _ → Two) (bop (bop b0 (bop b0 (bop b0 b1))) (bop b0 b0)) b1 → ⊥
  bad5232  p = false≢true (cong lower p)
  cut5232 : Adequate {ℓ} ((op (op (var 0) (op (var 0) (op (var 1) (var 2)))) (op (var 3) (var 0))) , (var 2)) → ⊥
  cut5232  adequate = bad5232  (Adequate.valid adequate Two boolean env9)
  bad5233 : PathP (λ _ → Two) (bop (bop b0 (bop b0 (bop b0 b0))) (bop b1 b0)) b1 → ⊥
  bad5233  p = false≢true (cong lower p)
  cut5233 : Adequate {ℓ} ((op (op (var 0) (op (var 0) (op (var 1) (var 2)))) (op (var 3) (var 0))) , (var 3)) → ⊥
  cut5233  adequate = bad5233  (Adequate.valid adequate Two boolean env5)
  bad5234 : PathP (λ _ → Two) (bop (bop b0 (bop b0 (bop b0 b0))) (bop b0 b0)) b1 → ⊥
  bad5234  p = false≢true (cong lower p)
  cut5234 : Adequate {ℓ} ((op (op (var 0) (op (var 0) (op (var 1) (var 2)))) (op (var 3) (var 0))) , (var 4)) → ⊥
  cut5234  adequate = bad5234  (Adequate.valid adequate Two boolean env10)
  bad5235 : PathP (λ _ → Two) (bop (bop b0 (bop b0 (bop b1 b0))) (bop b1 b1)) b0 → ⊥
  bad5235  p = false≢true (sym (cong lower p))
  cut5235 : Adequate {ℓ} ((op (op (var 0) (op (var 0) (op (var 1) (var 2)))) (op (var 3) (var 1))) , (var 0)) → ⊥
  cut5235  adequate = bad5235  (Adequate.valid adequate Two boolean env13)
  bad5236 : PathP (λ _ → Two) (bop (bop b0 (bop b0 (bop b1 b0))) (bop b0 b1)) b1 → ⊥
  bad5236  p = false≢true (cong lower p)
  cut5236 : Adequate {ℓ} ((op (op (var 0) (op (var 0) (op (var 1) (var 2)))) (op (var 3) (var 1))) , (var 1)) → ⊥
  cut5236  adequate = bad5236  (Adequate.valid adequate Two boolean env12)
  bad5237 : PathP (λ _ → Two) (bop (bop b0 (bop b0 (bop b0 b1))) (bop b0 b0)) b1 → ⊥
  bad5237  p = false≢true (cong lower p)
  cut5237 : Adequate {ℓ} ((op (op (var 0) (op (var 0) (op (var 1) (var 2)))) (op (var 3) (var 1))) , (var 2)) → ⊥
  cut5237  adequate = bad5237  (Adequate.valid adequate Two boolean env9)
  bad5238 : PathP (λ _ → Two) (bop (bop b0 (bop b0 (bop b0 b0))) (bop b1 b0)) b1 → ⊥
  bad5238  p = false≢true (cong lower p)
  cut5238 : Adequate {ℓ} ((op (op (var 0) (op (var 0) (op (var 1) (var 2)))) (op (var 3) (var 1))) , (var 3)) → ⊥
  cut5238  adequate = bad5238  (Adequate.valid adequate Two boolean env5)
  bad5239 : PathP (λ _ → Two) (bop (bop b0 (bop b0 (bop b0 b0))) (bop b0 b0)) b1 → ⊥
  bad5239  p = false≢true (cong lower p)
  cut5239 : Adequate {ℓ} ((op (op (var 0) (op (var 0) (op (var 1) (var 2)))) (op (var 3) (var 1))) , (var 4)) → ⊥
  cut5239  adequate = bad5239  (Adequate.valid adequate Two boolean env10)
  bad5240 : PathP (λ _ → Two) (bop (bop b0 (bop b0 (bop b0 b1))) (bop b1 b1)) b0 → ⊥
  bad5240  p = false≢true (sym (cong lower p))
  cut5240 : Adequate {ℓ} ((op (op (var 0) (op (var 0) (op (var 1) (var 2)))) (op (var 3) (var 2))) , (var 0)) → ⊥
  cut5240  adequate = bad5240  (Adequate.valid adequate Two boolean env8)
  bad5241 : PathP (λ _ → Two) (bop (bop b0 (bop b0 (bop b0 b1))) (bop b1 b1)) b0 → ⊥
  bad5241  p = false≢true (sym (cong lower p))
  cut5241 : Adequate {ℓ} ((op (op (var 0) (op (var 0) (op (var 1) (var 2)))) (op (var 3) (var 2))) , (var 1)) → ⊥
  cut5241  adequate = bad5241  (Adequate.valid adequate Two boolean env8)
  bad5242 : PathP (λ _ → Two) (bop (bop b0 (bop b0 (bop b0 b1))) (bop b0 b1)) b1 → ⊥
  bad5242  p = false≢true (cong lower p)
  cut5242 : Adequate {ℓ} ((op (op (var 0) (op (var 0) (op (var 1) (var 2)))) (op (var 3) (var 2))) , (var 2)) → ⊥
  cut5242  adequate = bad5242  (Adequate.valid adequate Two boolean env9)
  bad5243 : PathP (λ _ → Two) (bop (bop b0 (bop b0 (bop b0 b0))) (bop b1 b0)) b1 → ⊥
  bad5243  p = false≢true (cong lower p)
  cut5243 : Adequate {ℓ} ((op (op (var 0) (op (var 0) (op (var 1) (var 2)))) (op (var 3) (var 2))) , (var 3)) → ⊥
  cut5243  adequate = bad5243  (Adequate.valid adequate Two boolean env5)
  bad5244 : PathP (λ _ → Two) (bop (bop b0 (bop b0 (bop b0 b0))) (bop b0 b0)) b1 → ⊥
  bad5244  p = false≢true (cong lower p)
  cut5244 : Adequate {ℓ} ((op (op (var 0) (op (var 0) (op (var 1) (var 2)))) (op (var 3) (var 2))) , (var 4)) → ⊥
  cut5244  adequate = bad5244  (Adequate.valid adequate Two boolean env10)
  bad5245 : PathP (λ _ → Two) (bop (bop b0 (bop b0 (bop b0 b0))) (bop b1 b1)) b0 → ⊥
  bad5245  p = false≢true (sym (cong lower p))
  cut5245 : Adequate {ℓ} ((op (op (var 0) (op (var 0) (op (var 1) (var 2)))) (op (var 3) (var 3))) , (var 0)) → ⊥
  cut5245  adequate = bad5245  (Adequate.valid adequate Two boolean env5)
  bad5246 : PathP (λ _ → Two) (bop (bop b0 (bop b0 (bop b0 b0))) (bop b1 b1)) b0 → ⊥
  bad5246  p = false≢true (sym (cong lower p))
  cut5246 : Adequate {ℓ} ((op (op (var 0) (op (var 0) (op (var 1) (var 2)))) (op (var 3) (var 3))) , (var 1)) → ⊥
  cut5246  adequate = bad5246  (Adequate.valid adequate Two boolean env5)
  bad5247 : PathP (λ _ → Two) (bop (bop b0 (bop b0 (bop b0 b0))) (bop b1 b1)) b0 → ⊥
  bad5247  p = false≢true (sym (cong lower p))
  cut5247 : Adequate {ℓ} ((op (op (var 0) (op (var 0) (op (var 1) (var 2)))) (op (var 3) (var 3))) , (var 2)) → ⊥
  cut5247  adequate = bad5247  (Adequate.valid adequate Two boolean env5)
  env14 : ℕ → Two
  env14 zero = b1
  env14 (suc zero) = b1
  env14 (suc (suc zero)) = b1
  env14 (suc (suc (suc zero))) = b0
  env14 (suc (suc (suc (suc rest)))) = b0
  bad5248 : PathP (λ _ → Two) (bop (bop b1 (bop b1 (bop b1 b1))) (bop b0 b0)) b0 → ⊥
  bad5248  p = false≢true (sym (cong lower p))
  cut5248 : Adequate {ℓ} ((op (op (var 0) (op (var 0) (op (var 1) (var 2)))) (op (var 3) (var 3))) , (var 3)) → ⊥
  cut5248  adequate = bad5248  (Adequate.valid adequate Two boolean env14)
  bad5249 : PathP (λ _ → Two) (bop (bop b0 (bop b0 (bop b0 b0))) (bop b0 b0)) b1 → ⊥
  bad5249  p = false≢true (cong lower p)
  cut5249 : Adequate {ℓ} ((op (op (var 0) (op (var 0) (op (var 1) (var 2)))) (op (var 3) (var 3))) , (var 4)) → ⊥
  cut5249  adequate = bad5249  (Adequate.valid adequate Two boolean env10)
  env15 : ℕ → Two
  env15 zero = b0
  env15 (suc zero) = b0
  env15 (suc (suc zero)) = b0
  env15 (suc (suc (suc zero))) = b1
  env15 (suc (suc (suc (suc zero)))) = b1
  env15 (suc (suc (suc (suc (suc rest))))) = b0
  bad5250 : PathP (λ _ → Two) (bop (bop b0 (bop b0 (bop b0 b0))) (bop b1 b1)) b0 → ⊥
  bad5250  p = false≢true (sym (cong lower p))
  cut5250 : Adequate {ℓ} ((op (op (var 0) (op (var 0) (op (var 1) (var 2)))) (op (var 3) (var 4))) , (var 0)) → ⊥
  cut5250  adequate = bad5250  (Adequate.valid adequate Two boolean env15)
  bad5251 : PathP (λ _ → Two) (bop (bop b0 (bop b0 (bop b0 b0))) (bop b1 b1)) b0 → ⊥
  bad5251  p = false≢true (sym (cong lower p))
  cut5251 : Adequate {ℓ} ((op (op (var 0) (op (var 0) (op (var 1) (var 2)))) (op (var 3) (var 4))) , (var 1)) → ⊥
  cut5251  adequate = bad5251  (Adequate.valid adequate Two boolean env15)
  bad5252 : PathP (λ _ → Two) (bop (bop b0 (bop b0 (bop b0 b0))) (bop b1 b1)) b0 → ⊥
  bad5252  p = false≢true (sym (cong lower p))
  cut5252 : Adequate {ℓ} ((op (op (var 0) (op (var 0) (op (var 1) (var 2)))) (op (var 3) (var 4))) , (var 2)) → ⊥
  cut5252  adequate = bad5252  (Adequate.valid adequate Two boolean env15)
  env16 : ℕ → Two
  env16 zero = b0
  env16 (suc zero) = b0
  env16 (suc (suc zero)) = b0
  env16 (suc (suc (suc zero))) = b1
  env16 (suc (suc (suc (suc zero)))) = b0
  env16 (suc (suc (suc (suc (suc rest))))) = b0
  bad5253 : PathP (λ _ → Two) (bop (bop b0 (bop b0 (bop b0 b0))) (bop b1 b0)) b1 → ⊥
  bad5253  p = false≢true (cong lower p)
  cut5253 : Adequate {ℓ} ((op (op (var 0) (op (var 0) (op (var 1) (var 2)))) (op (var 3) (var 4))) , (var 3)) → ⊥
  cut5253  adequate = bad5253  (Adequate.valid adequate Two boolean env16)
  bad5254 : PathP (λ _ → Two) (bop (bop b0 (bop b0 (bop b0 b0))) (bop b0 b1)) b1 → ⊥
  bad5254  p = false≢true (cong lower p)
  cut5254 : Adequate {ℓ} ((op (op (var 0) (op (var 0) (op (var 1) (var 2)))) (op (var 3) (var 4))) , (var 4)) → ⊥
  cut5254  adequate = bad5254  (Adequate.valid adequate Two boolean env10)
  env17 : ℕ → Two
  env17 zero = b0
  env17 (suc zero) = b0
  env17 (suc (suc zero)) = b0
  env17 (suc (suc (suc zero))) = b0
  env17 (suc (suc (suc (suc zero)))) = b0
  env17 (suc (suc (suc (suc (suc zero))))) = b1
  env17 (suc (suc (suc (suc (suc (suc rest)))))) = b0
  bad5255 : PathP (λ _ → Two) (bop (bop b0 (bop b0 (bop b0 b0))) (bop b0 b0)) b1 → ⊥
  bad5255  p = false≢true (cong lower p)
  cut5255 : Adequate {ℓ} ((op (op (var 0) (op (var 0) (op (var 1) (var 2)))) (op (var 3) (var 4))) , (var 5)) → ⊥
  cut5255  adequate = bad5255  (Adequate.valid adequate Two boolean env17)
  holds5256 : (z0 z1 : A2) → (mul2 (mul2 z0 (mul2 z1 (mul2 z0 z0))) (mul2 z0 z0)) ≡ z0
  holds5256 z0 z1 = refl
  cut5256 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (op (var 0) (var 0)))) (op (var 0) (var 0))) , (var 0)) → ⊥
  cut5256  = reject2 ((op (op (var 0) (op (var 1) (op (var 0) (var 0)))) (op (var 0) (var 0))) , (var 0)) (λ env → holds5256 (env 0) (env 1))
  bad5257 : PathP (λ _ → Two) (bop (bop b0 (bop b1 (bop b0 b0))) (bop b0 b0)) b1 → ⊥
  bad5257  p = false≢true (cong lower p)
  cut5257 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (op (var 0) (var 0)))) (op (var 0) (var 0))) , (var 1)) → ⊥
  cut5257  adequate = bad5257  (Adequate.valid adequate Two boolean env0)
  bad5258 : PathP (λ _ → Two) (bop (bop b0 (bop b0 (bop b0 b0))) (bop b0 b0)) b1 → ⊥
  bad5258  p = false≢true (cong lower p)
  cut5258 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (op (var 0) (var 0)))) (op (var 0) (var 0))) , (var 2)) → ⊥
  cut5258  adequate = bad5258  (Adequate.valid adequate Two boolean env1)
  holds5259 : (z0 z1 : A2) → (mul2 (mul2 z0 (mul2 z1 (mul2 z0 z0))) (mul2 z0 z1)) ≡ z0
  holds5259 z0 z1 = refl
  cut5259 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (op (var 0) (var 0)))) (op (var 0) (var 1))) , (var 0)) → ⊥
  cut5259  = reject2 ((op (op (var 0) (op (var 1) (op (var 0) (var 0)))) (op (var 0) (var 1))) , (var 0)) (λ env → holds5259 (env 0) (env 1))
  bad5260 : PathP (λ _ → Two) (bop (bop b0 (bop b1 (bop b0 b0))) (bop b0 b1)) b1 → ⊥
  bad5260  p = false≢true (cong lower p)
  cut5260 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (op (var 0) (var 0)))) (op (var 0) (var 1))) , (var 1)) → ⊥
  cut5260  adequate = bad5260  (Adequate.valid adequate Two boolean env0)
  bad5261 : PathP (λ _ → Two) (bop (bop b0 (bop b0 (bop b0 b0))) (bop b0 b0)) b1 → ⊥
  bad5261  p = false≢true (cong lower p)
  cut5261 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (op (var 0) (var 0)))) (op (var 0) (var 1))) , (var 2)) → ⊥
  cut5261  adequate = bad5261  (Adequate.valid adequate Two boolean env1)
  holds5262 : (z0 z1 z2 : A2) → (mul2 (mul2 z0 (mul2 z1 (mul2 z0 z0))) (mul2 z0 z2)) ≡ z0
  holds5262 z0 z1 z2 = refl
  cut5262 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (op (var 0) (var 0)))) (op (var 0) (var 2))) , (var 0)) → ⊥
  cut5262  = reject2 ((op (op (var 0) (op (var 1) (op (var 0) (var 0)))) (op (var 0) (var 2))) , (var 0)) (λ env → holds5262 (env 0) (env 1) (env 2))
  bad5263 : PathP (λ _ → Two) (bop (bop b0 (bop b1 (bop b0 b0))) (bop b0 b0)) b1 → ⊥
  bad5263  p = false≢true (cong lower p)
  cut5263 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (op (var 0) (var 0)))) (op (var 0) (var 2))) , (var 1)) → ⊥
  cut5263  adequate = bad5263  (Adequate.valid adequate Two boolean env4)
  bad5264 : PathP (λ _ → Two) (bop (bop b0 (bop b0 (bop b0 b0))) (bop b0 b1)) b1 → ⊥
  bad5264  p = false≢true (cong lower p)
  cut5264 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (op (var 0) (var 0)))) (op (var 0) (var 2))) , (var 2)) → ⊥
  cut5264  adequate = bad5264  (Adequate.valid adequate Two boolean env1)
  bad5265 : PathP (λ _ → Two) (bop (bop b0 (bop b0 (bop b0 b0))) (bop b0 b0)) b1 → ⊥
  bad5265  p = false≢true (cong lower p)
  cut5265 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (op (var 0) (var 0)))) (op (var 0) (var 2))) , (var 3)) → ⊥
  cut5265  adequate = bad5265  (Adequate.valid adequate Two boolean env5)
  holds5266 : (z0 z1 : A2) → (mul2 (mul2 z0 (mul2 z1 (mul2 z0 z0))) (mul2 z1 z0)) ≡ z0
  holds5266 z0 z1 = refl
  cut5266 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (op (var 0) (var 0)))) (op (var 1) (var 0))) , (var 0)) → ⊥
  cut5266  = reject2 ((op (op (var 0) (op (var 1) (op (var 0) (var 0)))) (op (var 1) (var 0))) , (var 0)) (λ env → holds5266 (env 0) (env 1))
  bad5267 : PathP (λ _ → Two) (bop (bop b0 (bop b1 (bop b0 b0))) (bop b1 b0)) b1 → ⊥
  bad5267  p = false≢true (cong lower p)
  cut5267 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (op (var 0) (var 0)))) (op (var 1) (var 0))) , (var 1)) → ⊥
  cut5267  adequate = bad5267  (Adequate.valid adequate Two boolean env0)
  bad5268 : PathP (λ _ → Two) (bop (bop b0 (bop b0 (bop b0 b0))) (bop b0 b0)) b1 → ⊥
  bad5268  p = false≢true (cong lower p)
  cut5268 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (op (var 0) (var 0)))) (op (var 1) (var 0))) , (var 2)) → ⊥
  cut5268  adequate = bad5268  (Adequate.valid adequate Two boolean env1)
  bad5269 : PathP (λ _ → Two) (bop (bop b0 (bop b1 (bop b0 b0))) (bop b1 b1)) b0 → ⊥
  bad5269  p = false≢true (sym (cong lower p))
  cut5269 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (op (var 0) (var 0)))) (op (var 1) (var 1))) , (var 0)) → ⊥
  cut5269  adequate = bad5269  (Adequate.valid adequate Two boolean env0)
  bad5270 : PathP (λ _ → Two) (bop (bop b1 (bop b0 (bop b1 b1))) (bop b0 b0)) b0 → ⊥
  bad5270  p = false≢true (sym (cong lower p))
  cut5270 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (op (var 0) (var 0)))) (op (var 1) (var 1))) , (var 1)) → ⊥
  cut5270  adequate = bad5270  (Adequate.valid adequate Two boolean env2)
  bad5271 : PathP (λ _ → Two) (bop (bop b0 (bop b0 (bop b0 b0))) (bop b0 b0)) b1 → ⊥
  bad5271  p = false≢true (cong lower p)
  cut5271 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (op (var 0) (var 0)))) (op (var 1) (var 1))) , (var 2)) → ⊥
  cut5271  adequate = bad5271  (Adequate.valid adequate Two boolean env1)
  bad5272 : PathP (λ _ → Two) (bop (bop b0 (bop b1 (bop b0 b0))) (bop b1 b1)) b0 → ⊥
  bad5272  p = false≢true (sym (cong lower p))
  cut5272 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (op (var 0) (var 0)))) (op (var 1) (var 2))) , (var 0)) → ⊥
  cut5272  adequate = bad5272  (Adequate.valid adequate Two boolean env3)
  bad5273 : PathP (λ _ → Two) (bop (bop b0 (bop b1 (bop b0 b0))) (bop b1 b0)) b1 → ⊥
  bad5273  p = false≢true (cong lower p)
  cut5273 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (op (var 0) (var 0)))) (op (var 1) (var 2))) , (var 1)) → ⊥
  cut5273  adequate = bad5273  (Adequate.valid adequate Two boolean env4)
  bad5274 : PathP (λ _ → Two) (bop (bop b0 (bop b0 (bop b0 b0))) (bop b0 b1)) b1 → ⊥
  bad5274  p = false≢true (cong lower p)
  cut5274 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (op (var 0) (var 0)))) (op (var 1) (var 2))) , (var 2)) → ⊥
  cut5274  adequate = bad5274  (Adequate.valid adequate Two boolean env1)
  bad5275 : PathP (λ _ → Two) (bop (bop b0 (bop b0 (bop b0 b0))) (bop b0 b0)) b1 → ⊥
  bad5275  p = false≢true (cong lower p)
  cut5275 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (op (var 0) (var 0)))) (op (var 1) (var 2))) , (var 3)) → ⊥
  cut5275  adequate = bad5275  (Adequate.valid adequate Two boolean env5)
  holds5276 : (z0 z1 z2 : A2) → (mul2 (mul2 z0 (mul2 z1 (mul2 z0 z0))) (mul2 z2 z0)) ≡ z0
  holds5276 z0 z1 z2 = refl
  cut5276 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (op (var 0) (var 0)))) (op (var 2) (var 0))) , (var 0)) → ⊥
  cut5276  = reject2 ((op (op (var 0) (op (var 1) (op (var 0) (var 0)))) (op (var 2) (var 0))) , (var 0)) (λ env → holds5276 (env 0) (env 1) (env 2))
  bad5277 : PathP (λ _ → Two) (bop (bop b0 (bop b1 (bop b0 b0))) (bop b0 b0)) b1 → ⊥
  bad5277  p = false≢true (cong lower p)
  cut5277 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (op (var 0) (var 0)))) (op (var 2) (var 0))) , (var 1)) → ⊥
  cut5277  adequate = bad5277  (Adequate.valid adequate Two boolean env4)
  bad5278 : PathP (λ _ → Two) (bop (bop b0 (bop b0 (bop b0 b0))) (bop b1 b0)) b1 → ⊥
  bad5278  p = false≢true (cong lower p)
  cut5278 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (op (var 0) (var 0)))) (op (var 2) (var 0))) , (var 2)) → ⊥
  cut5278  adequate = bad5278  (Adequate.valid adequate Two boolean env1)
  bad5279 : PathP (λ _ → Two) (bop (bop b0 (bop b0 (bop b0 b0))) (bop b0 b0)) b1 → ⊥
  bad5279  p = false≢true (cong lower p)
  cut5279 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (op (var 0) (var 0)))) (op (var 2) (var 0))) , (var 3)) → ⊥
  cut5279  adequate = bad5279  (Adequate.valid adequate Two boolean env5)
  bad5280 : PathP (λ _ → Two) (bop (bop b0 (bop b1 (bop b0 b0))) (bop b1 b1)) b0 → ⊥
  bad5280  p = false≢true (sym (cong lower p))
  cut5280 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (op (var 0) (var 0)))) (op (var 2) (var 1))) , (var 0)) → ⊥
  cut5280  adequate = bad5280  (Adequate.valid adequate Two boolean env3)
  bad5281 : PathP (λ _ → Two) (bop (bop b0 (bop b1 (bop b0 b0))) (bop b0 b1)) b1 → ⊥
  bad5281  p = false≢true (cong lower p)
  cut5281 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (op (var 0) (var 0)))) (op (var 2) (var 1))) , (var 1)) → ⊥
  cut5281  adequate = bad5281  (Adequate.valid adequate Two boolean env4)
  bad5282 : PathP (λ _ → Two) (bop (bop b0 (bop b0 (bop b0 b0))) (bop b1 b0)) b1 → ⊥
  bad5282  p = false≢true (cong lower p)
  cut5282 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (op (var 0) (var 0)))) (op (var 2) (var 1))) , (var 2)) → ⊥
  cut5282  adequate = bad5282  (Adequate.valid adequate Two boolean env1)
  bad5283 : PathP (λ _ → Two) (bop (bop b0 (bop b0 (bop b0 b0))) (bop b0 b0)) b1 → ⊥
  bad5283  p = false≢true (cong lower p)
  cut5283 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (op (var 0) (var 0)))) (op (var 2) (var 1))) , (var 3)) → ⊥
  cut5283  adequate = bad5283  (Adequate.valid adequate Two boolean env5)
  bad5284 : PathP (λ _ → Two) (bop (bop b0 (bop b0 (bop b0 b0))) (bop b1 b1)) b0 → ⊥
  bad5284  p = false≢true (sym (cong lower p))
  cut5284 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (op (var 0) (var 0)))) (op (var 2) (var 2))) , (var 0)) → ⊥
  cut5284  adequate = bad5284  (Adequate.valid adequate Two boolean env1)
  bad5285 : PathP (λ _ → Two) (bop (bop b0 (bop b0 (bop b0 b0))) (bop b1 b1)) b0 → ⊥
  bad5285  p = false≢true (sym (cong lower p))
  cut5285 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (op (var 0) (var 0)))) (op (var 2) (var 2))) , (var 1)) → ⊥
  cut5285  adequate = bad5285  (Adequate.valid adequate Two boolean env1)
  bad5286 : PathP (λ _ → Two) (bop (bop b1 (bop b0 (bop b1 b1))) (bop b0 b0)) b0 → ⊥
  bad5286  p = false≢true (sym (cong lower p))
  cut5286 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (op (var 0) (var 0)))) (op (var 2) (var 2))) , (var 2)) → ⊥
  cut5286  adequate = bad5286  (Adequate.valid adequate Two boolean env6)
  bad5287 : PathP (λ _ → Two) (bop (bop b0 (bop b0 (bop b0 b0))) (bop b0 b0)) b1 → ⊥
  bad5287  p = false≢true (cong lower p)
  cut5287 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (op (var 0) (var 0)))) (op (var 2) (var 2))) , (var 3)) → ⊥
  cut5287  adequate = bad5287  (Adequate.valid adequate Two boolean env5)
  bad5288 : PathP (λ _ → Two) (bop (bop b0 (bop b0 (bop b0 b0))) (bop b1 b1)) b0 → ⊥
  bad5288  p = false≢true (sym (cong lower p))
  cut5288 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (op (var 0) (var 0)))) (op (var 2) (var 3))) , (var 0)) → ⊥
  cut5288  adequate = bad5288  (Adequate.valid adequate Two boolean env8)
  bad5289 : PathP (λ _ → Two) (bop (bop b0 (bop b0 (bop b0 b0))) (bop b1 b1)) b0 → ⊥
  bad5289  p = false≢true (sym (cong lower p))
  cut5289 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (op (var 0) (var 0)))) (op (var 2) (var 3))) , (var 1)) → ⊥
  cut5289  adequate = bad5289  (Adequate.valid adequate Two boolean env8)
  bad5290 : PathP (λ _ → Two) (bop (bop b0 (bop b0 (bop b0 b0))) (bop b1 b0)) b1 → ⊥
  bad5290  p = false≢true (cong lower p)
  cut5290 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (op (var 0) (var 0)))) (op (var 2) (var 3))) , (var 2)) → ⊥
  cut5290  adequate = bad5290  (Adequate.valid adequate Two boolean env9)
  bad5291 : PathP (λ _ → Two) (bop (bop b0 (bop b0 (bop b0 b0))) (bop b0 b1)) b1 → ⊥
  bad5291  p = false≢true (cong lower p)
  cut5291 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (op (var 0) (var 0)))) (op (var 2) (var 3))) , (var 3)) → ⊥
  cut5291  adequate = bad5291  (Adequate.valid adequate Two boolean env5)
  bad5292 : PathP (λ _ → Two) (bop (bop b0 (bop b0 (bop b0 b0))) (bop b0 b0)) b1 → ⊥
  bad5292  p = false≢true (cong lower p)
  cut5292 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (op (var 0) (var 0)))) (op (var 2) (var 3))) , (var 4)) → ⊥
  cut5292  adequate = bad5292  (Adequate.valid adequate Two boolean env10)
  holds5293 : (z0 z1 : A2) → (mul2 (mul2 z0 (mul2 z1 (mul2 z0 z1))) (mul2 z0 z0)) ≡ z0
  holds5293 z0 z1 = refl
  cut5293 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (op (var 0) (var 1)))) (op (var 0) (var 0))) , (var 0)) → ⊥
  cut5293  = reject2 ((op (op (var 0) (op (var 1) (op (var 0) (var 1)))) (op (var 0) (var 0))) , (var 0)) (λ env → holds5293 (env 0) (env 1))
  bad5294 : PathP (λ _ → Two) (bop (bop b0 (bop b1 (bop b0 b1))) (bop b0 b0)) b1 → ⊥
  bad5294  p = false≢true (cong lower p)
  cut5294 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (op (var 0) (var 1)))) (op (var 0) (var 0))) , (var 1)) → ⊥
  cut5294  adequate = bad5294  (Adequate.valid adequate Two boolean env0)
  bad5295 : PathP (λ _ → Two) (bop (bop b0 (bop b0 (bop b0 b0))) (bop b0 b0)) b1 → ⊥
  bad5295  p = false≢true (cong lower p)
  cut5295 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (op (var 0) (var 1)))) (op (var 0) (var 0))) , (var 2)) → ⊥
  cut5295  adequate = bad5295  (Adequate.valid adequate Two boolean env1)
  holds5296 : (z0 z1 : A2) → (mul2 (mul2 z0 (mul2 z1 (mul2 z0 z1))) (mul2 z0 z1)) ≡ z0
  holds5296 z0 z1 = refl
  cut5296 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (op (var 0) (var 1)))) (op (var 0) (var 1))) , (var 0)) → ⊥
  cut5296  = reject2 ((op (op (var 0) (op (var 1) (op (var 0) (var 1)))) (op (var 0) (var 1))) , (var 0)) (λ env → holds5296 (env 0) (env 1))
  bad5297 : PathP (λ _ → Two) (bop (bop b0 (bop b1 (bop b0 b1))) (bop b0 b1)) b1 → ⊥
  bad5297  p = false≢true (cong lower p)
  cut5297 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (op (var 0) (var 1)))) (op (var 0) (var 1))) , (var 1)) → ⊥
  cut5297  adequate = bad5297  (Adequate.valid adequate Two boolean env0)
  bad5298 : PathP (λ _ → Two) (bop (bop b0 (bop b0 (bop b0 b0))) (bop b0 b0)) b1 → ⊥
  bad5298  p = false≢true (cong lower p)
  cut5298 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (op (var 0) (var 1)))) (op (var 0) (var 1))) , (var 2)) → ⊥
  cut5298  adequate = bad5298  (Adequate.valid adequate Two boolean env1)
  holds5299 : (z0 z1 z2 : A2) → (mul2 (mul2 z0 (mul2 z1 (mul2 z0 z1))) (mul2 z0 z2)) ≡ z0
  holds5299 z0 z1 z2 = refl
  cut5299 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (op (var 0) (var 1)))) (op (var 0) (var 2))) , (var 0)) → ⊥
  cut5299  = reject2 ((op (op (var 0) (op (var 1) (op (var 0) (var 1)))) (op (var 0) (var 2))) , (var 0)) (λ env → holds5299 (env 0) (env 1) (env 2))
  bad5300 : PathP (λ _ → Two) (bop (bop b0 (bop b1 (bop b0 b1))) (bop b0 b0)) b1 → ⊥
  bad5300  p = false≢true (cong lower p)
  cut5300 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (op (var 0) (var 1)))) (op (var 0) (var 2))) , (var 1)) → ⊥
  cut5300  adequate = bad5300  (Adequate.valid adequate Two boolean env4)
  bad5301 : PathP (λ _ → Two) (bop (bop b0 (bop b0 (bop b0 b0))) (bop b0 b1)) b1 → ⊥
  bad5301  p = false≢true (cong lower p)
  cut5301 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (op (var 0) (var 1)))) (op (var 0) (var 2))) , (var 2)) → ⊥
  cut5301  adequate = bad5301  (Adequate.valid adequate Two boolean env1)
  bad5302 : PathP (λ _ → Two) (bop (bop b0 (bop b0 (bop b0 b0))) (bop b0 b0)) b1 → ⊥
  bad5302  p = false≢true (cong lower p)
  cut5302 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (op (var 0) (var 1)))) (op (var 0) (var 2))) , (var 3)) → ⊥
  cut5302  adequate = bad5302  (Adequate.valid adequate Two boolean env5)
  holds5303 : (z0 z1 : A2) → (mul2 (mul2 z0 (mul2 z1 (mul2 z0 z1))) (mul2 z1 z0)) ≡ z0
  holds5303 z0 z1 = refl
  cut5303 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (op (var 0) (var 1)))) (op (var 1) (var 0))) , (var 0)) → ⊥
  cut5303  = reject2 ((op (op (var 0) (op (var 1) (op (var 0) (var 1)))) (op (var 1) (var 0))) , (var 0)) (λ env → holds5303 (env 0) (env 1))
  bad5304 : PathP (λ _ → Two) (bop (bop b0 (bop b1 (bop b0 b1))) (bop b1 b0)) b1 → ⊥
  bad5304  p = false≢true (cong lower p)
  cut5304 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (op (var 0) (var 1)))) (op (var 1) (var 0))) , (var 1)) → ⊥
  cut5304  adequate = bad5304  (Adequate.valid adequate Two boolean env0)
  bad5305 : PathP (λ _ → Two) (bop (bop b0 (bop b0 (bop b0 b0))) (bop b0 b0)) b1 → ⊥
  bad5305  p = false≢true (cong lower p)
  cut5305 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (op (var 0) (var 1)))) (op (var 1) (var 0))) , (var 2)) → ⊥
  cut5305  adequate = bad5305  (Adequate.valid adequate Two boolean env1)
  bad5306 : PathP (λ _ → Two) (bop (bop b0 (bop b1 (bop b0 b1))) (bop b1 b1)) b0 → ⊥
  bad5306  p = false≢true (sym (cong lower p))
  cut5306 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (op (var 0) (var 1)))) (op (var 1) (var 1))) , (var 0)) → ⊥
  cut5306  adequate = bad5306  (Adequate.valid adequate Two boolean env0)
  bad5307 : PathP (λ _ → Two) (bop (bop b1 (bop b0 (bop b1 b0))) (bop b0 b0)) b0 → ⊥
  bad5307  p = false≢true (sym (cong lower p))
  cut5307 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (op (var 0) (var 1)))) (op (var 1) (var 1))) , (var 1)) → ⊥
  cut5307  adequate = bad5307  (Adequate.valid adequate Two boolean env2)
  bad5308 : PathP (λ _ → Two) (bop (bop b0 (bop b0 (bop b0 b0))) (bop b0 b0)) b1 → ⊥
  bad5308  p = false≢true (cong lower p)
  cut5308 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (op (var 0) (var 1)))) (op (var 1) (var 1))) , (var 2)) → ⊥
  cut5308  adequate = bad5308  (Adequate.valid adequate Two boolean env1)
  bad5309 : PathP (λ _ → Two) (bop (bop b0 (bop b1 (bop b0 b1))) (bop b1 b1)) b0 → ⊥
  bad5309  p = false≢true (sym (cong lower p))
  cut5309 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (op (var 0) (var 1)))) (op (var 1) (var 2))) , (var 0)) → ⊥
  cut5309  adequate = bad5309  (Adequate.valid adequate Two boolean env3)
  bad5310 : PathP (λ _ → Two) (bop (bop b0 (bop b1 (bop b0 b1))) (bop b1 b0)) b1 → ⊥
  bad5310  p = false≢true (cong lower p)
  cut5310 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (op (var 0) (var 1)))) (op (var 1) (var 2))) , (var 1)) → ⊥
  cut5310  adequate = bad5310  (Adequate.valid adequate Two boolean env4)
  bad5311 : PathP (λ _ → Two) (bop (bop b0 (bop b0 (bop b0 b0))) (bop b0 b1)) b1 → ⊥
  bad5311  p = false≢true (cong lower p)
  cut5311 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (op (var 0) (var 1)))) (op (var 1) (var 2))) , (var 2)) → ⊥
  cut5311  adequate = bad5311  (Adequate.valid adequate Two boolean env1)
  bad5312 : PathP (λ _ → Two) (bop (bop b0 (bop b0 (bop b0 b0))) (bop b0 b0)) b1 → ⊥
  bad5312  p = false≢true (cong lower p)
  cut5312 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (op (var 0) (var 1)))) (op (var 1) (var 2))) , (var 3)) → ⊥
  cut5312  adequate = bad5312  (Adequate.valid adequate Two boolean env5)
  holds5313 : (z0 z1 z2 : A2) → (mul2 (mul2 z0 (mul2 z1 (mul2 z0 z1))) (mul2 z2 z0)) ≡ z0
  holds5313 z0 z1 z2 = refl
  cut5313 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (op (var 0) (var 1)))) (op (var 2) (var 0))) , (var 0)) → ⊥
  cut5313  = reject2 ((op (op (var 0) (op (var 1) (op (var 0) (var 1)))) (op (var 2) (var 0))) , (var 0)) (λ env → holds5313 (env 0) (env 1) (env 2))
  bad5314 : PathP (λ _ → Two) (bop (bop b0 (bop b1 (bop b0 b1))) (bop b0 b0)) b1 → ⊥
  bad5314  p = false≢true (cong lower p)
  cut5314 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (op (var 0) (var 1)))) (op (var 2) (var 0))) , (var 1)) → ⊥
  cut5314  adequate = bad5314  (Adequate.valid adequate Two boolean env4)
  bad5315 : PathP (λ _ → Two) (bop (bop b0 (bop b0 (bop b0 b0))) (bop b1 b0)) b1 → ⊥
  bad5315  p = false≢true (cong lower p)
  cut5315 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (op (var 0) (var 1)))) (op (var 2) (var 0))) , (var 2)) → ⊥
  cut5315  adequate = bad5315  (Adequate.valid adequate Two boolean env1)
  bad5316 : PathP (λ _ → Two) (bop (bop b0 (bop b0 (bop b0 b0))) (bop b0 b0)) b1 → ⊥
  bad5316  p = false≢true (cong lower p)
  cut5316 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (op (var 0) (var 1)))) (op (var 2) (var 0))) , (var 3)) → ⊥
  cut5316  adequate = bad5316  (Adequate.valid adequate Two boolean env5)
  bad5317 : PathP (λ _ → Two) (bop (bop b0 (bop b1 (bop b0 b1))) (bop b1 b1)) b0 → ⊥
  bad5317  p = false≢true (sym (cong lower p))
  cut5317 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (op (var 0) (var 1)))) (op (var 2) (var 1))) , (var 0)) → ⊥
  cut5317  adequate = bad5317  (Adequate.valid adequate Two boolean env3)
  bad5318 : PathP (λ _ → Two) (bop (bop b0 (bop b1 (bop b0 b1))) (bop b0 b1)) b1 → ⊥
  bad5318  p = false≢true (cong lower p)
  cut5318 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (op (var 0) (var 1)))) (op (var 2) (var 1))) , (var 1)) → ⊥
  cut5318  adequate = bad5318  (Adequate.valid adequate Two boolean env4)
  bad5319 : PathP (λ _ → Two) (bop (bop b0 (bop b0 (bop b0 b0))) (bop b1 b0)) b1 → ⊥
  bad5319  p = false≢true (cong lower p)
  cut5319 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (op (var 0) (var 1)))) (op (var 2) (var 1))) , (var 2)) → ⊥
  cut5319  adequate = bad5319  (Adequate.valid adequate Two boolean env1)
  bad5320 : PathP (λ _ → Two) (bop (bop b0 (bop b0 (bop b0 b0))) (bop b0 b0)) b1 → ⊥
  bad5320  p = false≢true (cong lower p)
  cut5320 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (op (var 0) (var 1)))) (op (var 2) (var 1))) , (var 3)) → ⊥
  cut5320  adequate = bad5320  (Adequate.valid adequate Two boolean env5)
  bad5321 : PathP (λ _ → Two) (bop (bop b0 (bop b0 (bop b0 b0))) (bop b1 b1)) b0 → ⊥
  bad5321  p = false≢true (sym (cong lower p))
  cut5321 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (op (var 0) (var 1)))) (op (var 2) (var 2))) , (var 0)) → ⊥
  cut5321  adequate = bad5321  (Adequate.valid adequate Two boolean env1)
  bad5322 : PathP (λ _ → Two) (bop (bop b0 (bop b0 (bop b0 b0))) (bop b1 b1)) b0 → ⊥
  bad5322  p = false≢true (sym (cong lower p))
  cut5322 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (op (var 0) (var 1)))) (op (var 2) (var 2))) , (var 1)) → ⊥
  cut5322  adequate = bad5322  (Adequate.valid adequate Two boolean env1)
  bad5323 : PathP (λ _ → Two) (bop (bop b1 (bop b0 (bop b1 b0))) (bop b0 b0)) b0 → ⊥
  bad5323  p = false≢true (sym (cong lower p))
  cut5323 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (op (var 0) (var 1)))) (op (var 2) (var 2))) , (var 2)) → ⊥
  cut5323  adequate = bad5323  (Adequate.valid adequate Two boolean env6)
  bad5324 : PathP (λ _ → Two) (bop (bop b0 (bop b0 (bop b0 b0))) (bop b0 b0)) b1 → ⊥
  bad5324  p = false≢true (cong lower p)
  cut5324 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (op (var 0) (var 1)))) (op (var 2) (var 2))) , (var 3)) → ⊥
  cut5324  adequate = bad5324  (Adequate.valid adequate Two boolean env5)
  bad5325 : PathP (λ _ → Two) (bop (bop b0 (bop b0 (bop b0 b0))) (bop b1 b1)) b0 → ⊥
  bad5325  p = false≢true (sym (cong lower p))
  cut5325 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (op (var 0) (var 1)))) (op (var 2) (var 3))) , (var 0)) → ⊥
  cut5325  adequate = bad5325  (Adequate.valid adequate Two boolean env8)
  bad5326 : PathP (λ _ → Two) (bop (bop b0 (bop b0 (bop b0 b0))) (bop b1 b1)) b0 → ⊥
  bad5326  p = false≢true (sym (cong lower p))
  cut5326 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (op (var 0) (var 1)))) (op (var 2) (var 3))) , (var 1)) → ⊥
  cut5326  adequate = bad5326  (Adequate.valid adequate Two boolean env8)
  bad5327 : PathP (λ _ → Two) (bop (bop b0 (bop b0 (bop b0 b0))) (bop b1 b0)) b1 → ⊥
  bad5327  p = false≢true (cong lower p)
  cut5327 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (op (var 0) (var 1)))) (op (var 2) (var 3))) , (var 2)) → ⊥
  cut5327  adequate = bad5327  (Adequate.valid adequate Two boolean env9)
  bad5328 : PathP (λ _ → Two) (bop (bop b0 (bop b0 (bop b0 b0))) (bop b0 b1)) b1 → ⊥
  bad5328  p = false≢true (cong lower p)
  cut5328 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (op (var 0) (var 1)))) (op (var 2) (var 3))) , (var 3)) → ⊥
  cut5328  adequate = bad5328  (Adequate.valid adequate Two boolean env5)
  bad5329 : PathP (λ _ → Two) (bop (bop b0 (bop b0 (bop b0 b0))) (bop b0 b0)) b1 → ⊥
  bad5329  p = false≢true (cong lower p)
  cut5329 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (op (var 0) (var 1)))) (op (var 2) (var 3))) , (var 4)) → ⊥
  cut5329  adequate = bad5329  (Adequate.valid adequate Two boolean env10)
  holds5330 : (z0 z1 z2 : A2) → (mul2 (mul2 z0 (mul2 z1 (mul2 z0 z2))) (mul2 z0 z0)) ≡ z0
  holds5330 z0 z1 z2 = refl
  cut5330 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (op (var 0) (var 2)))) (op (var 0) (var 0))) , (var 0)) → ⊥
  cut5330  = reject2 ((op (op (var 0) (op (var 1) (op (var 0) (var 2)))) (op (var 0) (var 0))) , (var 0)) (λ env → holds5330 (env 0) (env 1) (env 2))
  bad5331 : PathP (λ _ → Two) (bop (bop b0 (bop b1 (bop b0 b0))) (bop b0 b0)) b1 → ⊥
  bad5331  p = false≢true (cong lower p)
  cut5331 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (op (var 0) (var 2)))) (op (var 0) (var 0))) , (var 1)) → ⊥
  cut5331  adequate = bad5331  (Adequate.valid adequate Two boolean env4)
  bad5332 : PathP (λ _ → Two) (bop (bop b0 (bop b0 (bop b0 b1))) (bop b0 b0)) b1 → ⊥
  bad5332  p = false≢true (cong lower p)
  cut5332 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (op (var 0) (var 2)))) (op (var 0) (var 0))) , (var 2)) → ⊥
  cut5332  adequate = bad5332  (Adequate.valid adequate Two boolean env1)
  bad5333 : PathP (λ _ → Two) (bop (bop b0 (bop b0 (bop b0 b0))) (bop b0 b0)) b1 → ⊥
  bad5333  p = false≢true (cong lower p)
  cut5333 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (op (var 0) (var 2)))) (op (var 0) (var 0))) , (var 3)) → ⊥
  cut5333  adequate = bad5333  (Adequate.valid adequate Two boolean env5)
  holds5334 : (z0 z1 z2 : A2) → (mul2 (mul2 z0 (mul2 z1 (mul2 z0 z2))) (mul2 z0 z1)) ≡ z0
  holds5334 z0 z1 z2 = refl
  cut5334 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (op (var 0) (var 2)))) (op (var 0) (var 1))) , (var 0)) → ⊥
  cut5334  = reject2 ((op (op (var 0) (op (var 1) (op (var 0) (var 2)))) (op (var 0) (var 1))) , (var 0)) (λ env → holds5334 (env 0) (env 1) (env 2))
  bad5335 : PathP (λ _ → Two) (bop (bop b0 (bop b1 (bop b0 b0))) (bop b0 b1)) b1 → ⊥
  bad5335  p = false≢true (cong lower p)
  cut5335 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (op (var 0) (var 2)))) (op (var 0) (var 1))) , (var 1)) → ⊥
  cut5335  adequate = bad5335  (Adequate.valid adequate Two boolean env4)
  bad5336 : PathP (λ _ → Two) (bop (bop b0 (bop b0 (bop b0 b1))) (bop b0 b0)) b1 → ⊥
  bad5336  p = false≢true (cong lower p)
  cut5336 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (op (var 0) (var 2)))) (op (var 0) (var 1))) , (var 2)) → ⊥
  cut5336  adequate = bad5336  (Adequate.valid adequate Two boolean env1)
  bad5337 : PathP (λ _ → Two) (bop (bop b0 (bop b0 (bop b0 b0))) (bop b0 b0)) b1 → ⊥
  bad5337  p = false≢true (cong lower p)
  cut5337 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (op (var 0) (var 2)))) (op (var 0) (var 1))) , (var 3)) → ⊥
  cut5337  adequate = bad5337  (Adequate.valid adequate Two boolean env5)
  bad5338 : PathP (λ _ → Two) (bop (bop b1 (bop b1 (bop b1 b0))) (bop b1 b0)) b1 → ⊥
  bad5338  p = false≢true (cong lower p)
  cut5338 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (op (var 0) (var 2)))) (op (var 0) (var 2))) , (var 0)) → ⊥
  cut5338  adequate = bad5338  (Adequate.valid adequate Two boolean env7)
  bad5339 : PathP (λ _ → Two) (bop (bop b0 (bop b1 (bop b0 b0))) (bop b0 b0)) b1 → ⊥
  bad5339  p = false≢true (cong lower p)
  cut5339 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (op (var 0) (var 2)))) (op (var 0) (var 2))) , (var 1)) → ⊥
  cut5339  adequate = bad5339  (Adequate.valid adequate Two boolean env4)
  bad5340 : PathP (λ _ → Two) (bop (bop b0 (bop b0 (bop b0 b1))) (bop b0 b1)) b1 → ⊥
  bad5340  p = false≢true (cong lower p)
  cut5340 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (op (var 0) (var 2)))) (op (var 0) (var 2))) , (var 2)) → ⊥
  cut5340  adequate = bad5340  (Adequate.valid adequate Two boolean env1)
  bad5341 : PathP (λ _ → Two) (bop (bop b0 (bop b0 (bop b0 b0))) (bop b0 b0)) b1 → ⊥
  bad5341  p = false≢true (cong lower p)
  cut5341 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (op (var 0) (var 2)))) (op (var 0) (var 2))) , (var 3)) → ⊥
  cut5341  adequate = bad5341  (Adequate.valid adequate Two boolean env5)
  env18 : ℕ → Two
  env18 zero = b1
  env18 (suc zero) = b1
  env18 (suc (suc zero)) = b0
  env18 (suc (suc (suc zero))) = b0
  env18 (suc (suc (suc (suc rest)))) = b0
  bad5342 : PathP (λ _ → Two) (bop (bop b1 (bop b1 (bop b1 b0))) (bop b1 b0)) b1 → ⊥
  bad5342  p = false≢true (cong lower p)
  cut5342 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (op (var 0) (var 2)))) (op (var 0) (var 3))) , (var 0)) → ⊥
  cut5342  adequate = bad5342  (Adequate.valid adequate Two boolean env18)
  bad5343 : PathP (λ _ → Two) (bop (bop b0 (bop b1 (bop b0 b0))) (bop b0 b0)) b1 → ⊥
  bad5343  p = false≢true (cong lower p)
  cut5343 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (op (var 0) (var 2)))) (op (var 0) (var 3))) , (var 1)) → ⊥
  cut5343  adequate = bad5343  (Adequate.valid adequate Two boolean env12)
  bad5344 : PathP (λ _ → Two) (bop (bop b0 (bop b0 (bop b0 b1))) (bop b0 b0)) b1 → ⊥
  bad5344  p = false≢true (cong lower p)
  cut5344 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (op (var 0) (var 2)))) (op (var 0) (var 3))) , (var 2)) → ⊥
  cut5344  adequate = bad5344  (Adequate.valid adequate Two boolean env9)
  bad5345 : PathP (λ _ → Two) (bop (bop b0 (bop b0 (bop b0 b0))) (bop b0 b1)) b1 → ⊥
  bad5345  p = false≢true (cong lower p)
  cut5345 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (op (var 0) (var 2)))) (op (var 0) (var 3))) , (var 3)) → ⊥
  cut5345  adequate = bad5345  (Adequate.valid adequate Two boolean env5)
  bad5346 : PathP (λ _ → Two) (bop (bop b0 (bop b0 (bop b0 b0))) (bop b0 b0)) b1 → ⊥
  bad5346  p = false≢true (cong lower p)
  cut5346 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (op (var 0) (var 2)))) (op (var 0) (var 3))) , (var 4)) → ⊥
  cut5346  adequate = bad5346  (Adequate.valid adequate Two boolean env10)
  holds5347 : (z0 z1 z2 : A2) → (mul2 (mul2 z0 (mul2 z1 (mul2 z0 z2))) (mul2 z1 z0)) ≡ z0
  holds5347 z0 z1 z2 = refl
  cut5347 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (op (var 0) (var 2)))) (op (var 1) (var 0))) , (var 0)) → ⊥
  cut5347  = reject2 ((op (op (var 0) (op (var 1) (op (var 0) (var 2)))) (op (var 1) (var 0))) , (var 0)) (λ env → holds5347 (env 0) (env 1) (env 2))
  bad5348 : PathP (λ _ → Two) (bop (bop b0 (bop b1 (bop b0 b0))) (bop b1 b0)) b1 → ⊥
  bad5348  p = false≢true (cong lower p)
  cut5348 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (op (var 0) (var 2)))) (op (var 1) (var 0))) , (var 1)) → ⊥
  cut5348  adequate = bad5348  (Adequate.valid adequate Two boolean env4)
  bad5349 : PathP (λ _ → Two) (bop (bop b0 (bop b0 (bop b0 b1))) (bop b0 b0)) b1 → ⊥
  bad5349  p = false≢true (cong lower p)
  cut5349 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (op (var 0) (var 2)))) (op (var 1) (var 0))) , (var 2)) → ⊥
  cut5349  adequate = bad5349  (Adequate.valid adequate Two boolean env1)
  bad5350 : PathP (λ _ → Two) (bop (bop b0 (bop b0 (bop b0 b0))) (bop b0 b0)) b1 → ⊥
  bad5350  p = false≢true (cong lower p)
  cut5350 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (op (var 0) (var 2)))) (op (var 1) (var 0))) , (var 3)) → ⊥
  cut5350  adequate = bad5350  (Adequate.valid adequate Two boolean env5)
  bad5351 : PathP (λ _ → Two) (bop (bop b0 (bop b1 (bop b0 b0))) (bop b1 b1)) b0 → ⊥
  bad5351  p = false≢true (sym (cong lower p))
  cut5351 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (op (var 0) (var 2)))) (op (var 1) (var 1))) , (var 0)) → ⊥
  cut5351  adequate = bad5351  (Adequate.valid adequate Two boolean env4)
  bad5352 : PathP (λ _ → Two) (bop (bop b1 (bop b0 (bop b1 b0))) (bop b0 b0)) b0 → ⊥
  bad5352  p = false≢true (sym (cong lower p))
  cut5352 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (op (var 0) (var 2)))) (op (var 1) (var 1))) , (var 1)) → ⊥
  cut5352  adequate = bad5352  (Adequate.valid adequate Two boolean env6)
  bad5353 : PathP (λ _ → Two) (bop (bop b0 (bop b0 (bop b0 b1))) (bop b0 b0)) b1 → ⊥
  bad5353  p = false≢true (cong lower p)
  cut5353 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (op (var 0) (var 2)))) (op (var 1) (var 1))) , (var 2)) → ⊥
  cut5353  adequate = bad5353  (Adequate.valid adequate Two boolean env1)
  bad5354 : PathP (λ _ → Two) (bop (bop b0 (bop b0 (bop b0 b0))) (bop b0 b0)) b1 → ⊥
  bad5354  p = false≢true (cong lower p)
  cut5354 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (op (var 0) (var 2)))) (op (var 1) (var 1))) , (var 3)) → ⊥
  cut5354  adequate = bad5354  (Adequate.valid adequate Two boolean env5)
  bad5355 : PathP (λ _ → Two) (bop (bop b0 (bop b1 (bop b0 b1))) (bop b1 b1)) b0 → ⊥
  bad5355  p = false≢true (sym (cong lower p))
  cut5355 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (op (var 0) (var 2)))) (op (var 1) (var 2))) , (var 0)) → ⊥
  cut5355  adequate = bad5355  (Adequate.valid adequate Two boolean env3)
  bad5356 : PathP (λ _ → Two) (bop (bop b0 (bop b1 (bop b0 b0))) (bop b1 b0)) b1 → ⊥
  bad5356  p = false≢true (cong lower p)
  cut5356 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (op (var 0) (var 2)))) (op (var 1) (var 2))) , (var 1)) → ⊥
  cut5356  adequate = bad5356  (Adequate.valid adequate Two boolean env4)
  bad5357 : PathP (λ _ → Two) (bop (bop b0 (bop b0 (bop b0 b1))) (bop b0 b1)) b1 → ⊥
  bad5357  p = false≢true (cong lower p)
  cut5357 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (op (var 0) (var 2)))) (op (var 1) (var 2))) , (var 2)) → ⊥
  cut5357  adequate = bad5357  (Adequate.valid adequate Two boolean env1)
  bad5358 : PathP (λ _ → Two) (bop (bop b0 (bop b0 (bop b0 b0))) (bop b0 b0)) b1 → ⊥
  bad5358  p = false≢true (cong lower p)
  cut5358 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (op (var 0) (var 2)))) (op (var 1) (var 2))) , (var 3)) → ⊥
  cut5358  adequate = bad5358  (Adequate.valid adequate Two boolean env5)
  bad5359 : PathP (λ _ → Two) (bop (bop b0 (bop b1 (bop b0 b0))) (bop b1 b1)) b0 → ⊥
  bad5359  p = false≢true (sym (cong lower p))
  cut5359 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (op (var 0) (var 2)))) (op (var 1) (var 3))) , (var 0)) → ⊥
  cut5359  adequate = bad5359  (Adequate.valid adequate Two boolean env13)
  bad5360 : PathP (λ _ → Two) (bop (bop b0 (bop b1 (bop b0 b0))) (bop b1 b0)) b1 → ⊥
  bad5360  p = false≢true (cong lower p)
  cut5360 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (op (var 0) (var 2)))) (op (var 1) (var 3))) , (var 1)) → ⊥
  cut5360  adequate = bad5360  (Adequate.valid adequate Two boolean env12)
  bad5361 : PathP (λ _ → Two) (bop (bop b0 (bop b0 (bop b0 b1))) (bop b0 b0)) b1 → ⊥
  bad5361  p = false≢true (cong lower p)
  cut5361 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (op (var 0) (var 2)))) (op (var 1) (var 3))) , (var 2)) → ⊥
  cut5361  adequate = bad5361  (Adequate.valid adequate Two boolean env9)
  bad5362 : PathP (λ _ → Two) (bop (bop b0 (bop b0 (bop b0 b0))) (bop b0 b1)) b1 → ⊥
  bad5362  p = false≢true (cong lower p)
  cut5362 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (op (var 0) (var 2)))) (op (var 1) (var 3))) , (var 3)) → ⊥
  cut5362  adequate = bad5362  (Adequate.valid adequate Two boolean env5)
  bad5363 : PathP (λ _ → Two) (bop (bop b0 (bop b0 (bop b0 b0))) (bop b0 b0)) b1 → ⊥
  bad5363  p = false≢true (cong lower p)
  cut5363 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (op (var 0) (var 2)))) (op (var 1) (var 3))) , (var 4)) → ⊥
  cut5363  adequate = bad5363  (Adequate.valid adequate Two boolean env10)
  bad5364 : PathP (λ _ → Two) (bop (bop b1 (bop b1 (bop b1 b0))) (bop b0 b1)) b1 → ⊥
  bad5364  p = false≢true (cong lower p)
  cut5364 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (op (var 0) (var 2)))) (op (var 2) (var 0))) , (var 0)) → ⊥
  cut5364  adequate = bad5364  (Adequate.valid adequate Two boolean env7)
  bad5365 : PathP (λ _ → Two) (bop (bop b0 (bop b1 (bop b0 b0))) (bop b0 b0)) b1 → ⊥
  bad5365  p = false≢true (cong lower p)
  cut5365 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (op (var 0) (var 2)))) (op (var 2) (var 0))) , (var 1)) → ⊥
  cut5365  adequate = bad5365  (Adequate.valid adequate Two boolean env4)
  bad5366 : PathP (λ _ → Two) (bop (bop b0 (bop b0 (bop b0 b1))) (bop b1 b0)) b1 → ⊥
  bad5366  p = false≢true (cong lower p)
  cut5366 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (op (var 0) (var 2)))) (op (var 2) (var 0))) , (var 2)) → ⊥
  cut5366  adequate = bad5366  (Adequate.valid adequate Two boolean env1)
  bad5367 : PathP (λ _ → Two) (bop (bop b0 (bop b0 (bop b0 b0))) (bop b0 b0)) b1 → ⊥
  bad5367  p = false≢true (cong lower p)
  cut5367 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (op (var 0) (var 2)))) (op (var 2) (var 0))) , (var 3)) → ⊥
  cut5367  adequate = bad5367  (Adequate.valid adequate Two boolean env5)
  bad5368 : PathP (λ _ → Two) (bop (bop b0 (bop b1 (bop b0 b1))) (bop b1 b1)) b0 → ⊥
  bad5368  p = false≢true (sym (cong lower p))
  cut5368 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (op (var 0) (var 2)))) (op (var 2) (var 1))) , (var 0)) → ⊥
  cut5368  adequate = bad5368  (Adequate.valid adequate Two boolean env3)
  bad5369 : PathP (λ _ → Two) (bop (bop b0 (bop b1 (bop b0 b0))) (bop b0 b1)) b1 → ⊥
  bad5369  p = false≢true (cong lower p)
  cut5369 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (op (var 0) (var 2)))) (op (var 2) (var 1))) , (var 1)) → ⊥
  cut5369  adequate = bad5369  (Adequate.valid adequate Two boolean env4)
  bad5370 : PathP (λ _ → Two) (bop (bop b0 (bop b0 (bop b0 b1))) (bop b1 b0)) b1 → ⊥
  bad5370  p = false≢true (cong lower p)
  cut5370 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (op (var 0) (var 2)))) (op (var 2) (var 1))) , (var 2)) → ⊥
  cut5370  adequate = bad5370  (Adequate.valid adequate Two boolean env1)
  bad5371 : PathP (λ _ → Two) (bop (bop b0 (bop b0 (bop b0 b0))) (bop b0 b0)) b1 → ⊥
  bad5371  p = false≢true (cong lower p)
  cut5371 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (op (var 0) (var 2)))) (op (var 2) (var 1))) , (var 3)) → ⊥
  cut5371  adequate = bad5371  (Adequate.valid adequate Two boolean env5)
  bad5372 : PathP (λ _ → Two) (bop (bop b0 (bop b0 (bop b0 b1))) (bop b1 b1)) b0 → ⊥
  bad5372  p = false≢true (sym (cong lower p))
  cut5372 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (op (var 0) (var 2)))) (op (var 2) (var 2))) , (var 0)) → ⊥
  cut5372  adequate = bad5372  (Adequate.valid adequate Two boolean env1)
  bad5373 : PathP (λ _ → Two) (bop (bop b0 (bop b0 (bop b0 b1))) (bop b1 b1)) b0 → ⊥
  bad5373  p = false≢true (sym (cong lower p))
  cut5373 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (op (var 0) (var 2)))) (op (var 2) (var 2))) , (var 1)) → ⊥
  cut5373  adequate = bad5373  (Adequate.valid adequate Two boolean env1)
  bad5374 : PathP (λ _ → Two) (bop (bop b1 (bop b0 (bop b1 b0))) (bop b0 b0)) b0 → ⊥
  bad5374  p = false≢true (sym (cong lower p))
  cut5374 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (op (var 0) (var 2)))) (op (var 2) (var 2))) , (var 2)) → ⊥
  cut5374  adequate = bad5374  (Adequate.valid adequate Two boolean env6)
  bad5375 : PathP (λ _ → Two) (bop (bop b0 (bop b0 (bop b0 b0))) (bop b0 b0)) b1 → ⊥
  bad5375  p = false≢true (cong lower p)
  cut5375 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (op (var 0) (var 2)))) (op (var 2) (var 2))) , (var 3)) → ⊥
  cut5375  adequate = bad5375  (Adequate.valid adequate Two boolean env5)
  bad5376 : PathP (λ _ → Two) (bop (bop b0 (bop b0 (bop b0 b1))) (bop b1 b1)) b0 → ⊥
  bad5376  p = false≢true (sym (cong lower p))
  cut5376 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (op (var 0) (var 2)))) (op (var 2) (var 3))) , (var 0)) → ⊥
  cut5376  adequate = bad5376  (Adequate.valid adequate Two boolean env8)
  bad5377 : PathP (λ _ → Two) (bop (bop b0 (bop b0 (bop b0 b1))) (bop b1 b1)) b0 → ⊥
  bad5377  p = false≢true (sym (cong lower p))
  cut5377 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (op (var 0) (var 2)))) (op (var 2) (var 3))) , (var 1)) → ⊥
  cut5377  adequate = bad5377  (Adequate.valid adequate Two boolean env8)
  bad5378 : PathP (λ _ → Two) (bop (bop b0 (bop b0 (bop b0 b1))) (bop b1 b0)) b1 → ⊥
  bad5378  p = false≢true (cong lower p)
  cut5378 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (op (var 0) (var 2)))) (op (var 2) (var 3))) , (var 2)) → ⊥
  cut5378  adequate = bad5378  (Adequate.valid adequate Two boolean env9)
  bad5379 : PathP (λ _ → Two) (bop (bop b0 (bop b0 (bop b0 b0))) (bop b0 b1)) b1 → ⊥
  bad5379  p = false≢true (cong lower p)
  cut5379 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (op (var 0) (var 2)))) (op (var 2) (var 3))) , (var 3)) → ⊥
  cut5379  adequate = bad5379  (Adequate.valid adequate Two boolean env5)
  bad5380 : PathP (λ _ → Two) (bop (bop b0 (bop b0 (bop b0 b0))) (bop b0 b0)) b1 → ⊥
  bad5380  p = false≢true (cong lower p)
  cut5380 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (op (var 0) (var 2)))) (op (var 2) (var 3))) , (var 4)) → ⊥
  cut5380  adequate = bad5380  (Adequate.valid adequate Two boolean env10)
  bad5381 : PathP (λ _ → Two) (bop (bop b1 (bop b1 (bop b1 b0))) (bop b0 b1)) b1 → ⊥
  bad5381  p = false≢true (cong lower p)
  cut5381 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (op (var 0) (var 2)))) (op (var 3) (var 0))) , (var 0)) → ⊥
  cut5381  adequate = bad5381  (Adequate.valid adequate Two boolean env18)
  bad5382 : PathP (λ _ → Two) (bop (bop b0 (bop b1 (bop b0 b0))) (bop b0 b0)) b1 → ⊥
  bad5382  p = false≢true (cong lower p)
  cut5382 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (op (var 0) (var 2)))) (op (var 3) (var 0))) , (var 1)) → ⊥
  cut5382  adequate = bad5382  (Adequate.valid adequate Two boolean env12)
  bad5383 : PathP (λ _ → Two) (bop (bop b0 (bop b0 (bop b0 b1))) (bop b0 b0)) b1 → ⊥
  bad5383  p = false≢true (cong lower p)
  cut5383 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (op (var 0) (var 2)))) (op (var 3) (var 0))) , (var 2)) → ⊥
  cut5383  adequate = bad5383  (Adequate.valid adequate Two boolean env9)
  bad5384 : PathP (λ _ → Two) (bop (bop b0 (bop b0 (bop b0 b0))) (bop b1 b0)) b1 → ⊥
  bad5384  p = false≢true (cong lower p)
  cut5384 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (op (var 0) (var 2)))) (op (var 3) (var 0))) , (var 3)) → ⊥
  cut5384  adequate = bad5384  (Adequate.valid adequate Two boolean env5)
  bad5385 : PathP (λ _ → Two) (bop (bop b0 (bop b0 (bop b0 b0))) (bop b0 b0)) b1 → ⊥
  bad5385  p = false≢true (cong lower p)
  cut5385 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (op (var 0) (var 2)))) (op (var 3) (var 0))) , (var 4)) → ⊥
  cut5385  adequate = bad5385  (Adequate.valid adequate Two boolean env10)
  bad5386 : PathP (λ _ → Two) (bop (bop b0 (bop b1 (bop b0 b0))) (bop b1 b1)) b0 → ⊥
  bad5386  p = false≢true (sym (cong lower p))
  cut5386 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (op (var 0) (var 2)))) (op (var 3) (var 1))) , (var 0)) → ⊥
  cut5386  adequate = bad5386  (Adequate.valid adequate Two boolean env13)
  bad5387 : PathP (λ _ → Two) (bop (bop b0 (bop b1 (bop b0 b0))) (bop b0 b1)) b1 → ⊥
  bad5387  p = false≢true (cong lower p)
  cut5387 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (op (var 0) (var 2)))) (op (var 3) (var 1))) , (var 1)) → ⊥
  cut5387  adequate = bad5387  (Adequate.valid adequate Two boolean env12)
  bad5388 : PathP (λ _ → Two) (bop (bop b0 (bop b0 (bop b0 b1))) (bop b0 b0)) b1 → ⊥
  bad5388  p = false≢true (cong lower p)
  cut5388 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (op (var 0) (var 2)))) (op (var 3) (var 1))) , (var 2)) → ⊥
  cut5388  adequate = bad5388  (Adequate.valid adequate Two boolean env9)
  bad5389 : PathP (λ _ → Two) (bop (bop b0 (bop b0 (bop b0 b0))) (bop b1 b0)) b1 → ⊥
  bad5389  p = false≢true (cong lower p)
  cut5389 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (op (var 0) (var 2)))) (op (var 3) (var 1))) , (var 3)) → ⊥
  cut5389  adequate = bad5389  (Adequate.valid adequate Two boolean env5)
  bad5390 : PathP (λ _ → Two) (bop (bop b0 (bop b0 (bop b0 b0))) (bop b0 b0)) b1 → ⊥
  bad5390  p = false≢true (cong lower p)
  cut5390 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (op (var 0) (var 2)))) (op (var 3) (var 1))) , (var 4)) → ⊥
  cut5390  adequate = bad5390  (Adequate.valid adequate Two boolean env10)
  bad5391 : PathP (λ _ → Two) (bop (bop b0 (bop b0 (bop b0 b1))) (bop b1 b1)) b0 → ⊥
  bad5391  p = false≢true (sym (cong lower p))
  cut5391 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (op (var 0) (var 2)))) (op (var 3) (var 2))) , (var 0)) → ⊥
  cut5391  adequate = bad5391  (Adequate.valid adequate Two boolean env8)
  bad5392 : PathP (λ _ → Two) (bop (bop b0 (bop b0 (bop b0 b1))) (bop b1 b1)) b0 → ⊥
  bad5392  p = false≢true (sym (cong lower p))
  cut5392 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (op (var 0) (var 2)))) (op (var 3) (var 2))) , (var 1)) → ⊥
  cut5392  adequate = bad5392  (Adequate.valid adequate Two boolean env8)
  bad5393 : PathP (λ _ → Two) (bop (bop b0 (bop b0 (bop b0 b1))) (bop b0 b1)) b1 → ⊥
  bad5393  p = false≢true (cong lower p)
  cut5393 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (op (var 0) (var 2)))) (op (var 3) (var 2))) , (var 2)) → ⊥
  cut5393  adequate = bad5393  (Adequate.valid adequate Two boolean env9)
  bad5394 : PathP (λ _ → Two) (bop (bop b0 (bop b0 (bop b0 b0))) (bop b1 b0)) b1 → ⊥
  bad5394  p = false≢true (cong lower p)
  cut5394 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (op (var 0) (var 2)))) (op (var 3) (var 2))) , (var 3)) → ⊥
  cut5394  adequate = bad5394  (Adequate.valid adequate Two boolean env5)
  bad5395 : PathP (λ _ → Two) (bop (bop b0 (bop b0 (bop b0 b0))) (bop b0 b0)) b1 → ⊥
  bad5395  p = false≢true (cong lower p)
  cut5395 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (op (var 0) (var 2)))) (op (var 3) (var 2))) , (var 4)) → ⊥
  cut5395  adequate = bad5395  (Adequate.valid adequate Two boolean env10)
  bad5396 : PathP (λ _ → Two) (bop (bop b0 (bop b0 (bop b0 b0))) (bop b1 b1)) b0 → ⊥
  bad5396  p = false≢true (sym (cong lower p))
  cut5396 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (op (var 0) (var 2)))) (op (var 3) (var 3))) , (var 0)) → ⊥
  cut5396  adequate = bad5396  (Adequate.valid adequate Two boolean env5)
  bad5397 : PathP (λ _ → Two) (bop (bop b0 (bop b0 (bop b0 b0))) (bop b1 b1)) b0 → ⊥
  bad5397  p = false≢true (sym (cong lower p))
  cut5397 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (op (var 0) (var 2)))) (op (var 3) (var 3))) , (var 1)) → ⊥
  cut5397  adequate = bad5397  (Adequate.valid adequate Two boolean env5)
  bad5398 : PathP (λ _ → Two) (bop (bop b0 (bop b0 (bop b0 b0))) (bop b1 b1)) b0 → ⊥
  bad5398  p = false≢true (sym (cong lower p))
  cut5398 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (op (var 0) (var 2)))) (op (var 3) (var 3))) , (var 2)) → ⊥
  cut5398  adequate = bad5398  (Adequate.valid adequate Two boolean env5)
  bad5399 : PathP (λ _ → Two) (bop (bop b1 (bop b0 (bop b1 b0))) (bop b0 b0)) b0 → ⊥
  bad5399  p = false≢true (sym (cong lower p))
  cut5399 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (op (var 0) (var 2)))) (op (var 3) (var 3))) , (var 3)) → ⊥
  cut5399  adequate = bad5399  (Adequate.valid adequate Two boolean env11)
  bad5400 : PathP (λ _ → Two) (bop (bop b0 (bop b0 (bop b0 b0))) (bop b0 b0)) b1 → ⊥
  bad5400  p = false≢true (cong lower p)
  cut5400 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (op (var 0) (var 2)))) (op (var 3) (var 3))) , (var 4)) → ⊥
  cut5400  adequate = bad5400  (Adequate.valid adequate Two boolean env10)
  bad5401 : PathP (λ _ → Two) (bop (bop b0 (bop b0 (bop b0 b0))) (bop b1 b1)) b0 → ⊥
  bad5401  p = false≢true (sym (cong lower p))
  cut5401 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (op (var 0) (var 2)))) (op (var 3) (var 4))) , (var 0)) → ⊥
  cut5401  adequate = bad5401  (Adequate.valid adequate Two boolean env15)
  bad5402 : PathP (λ _ → Two) (bop (bop b0 (bop b0 (bop b0 b0))) (bop b1 b1)) b0 → ⊥
  bad5402  p = false≢true (sym (cong lower p))
  cut5402 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (op (var 0) (var 2)))) (op (var 3) (var 4))) , (var 1)) → ⊥
  cut5402  adequate = bad5402  (Adequate.valid adequate Two boolean env15)
  bad5403 : PathP (λ _ → Two) (bop (bop b0 (bop b0 (bop b0 b0))) (bop b1 b1)) b0 → ⊥
  bad5403  p = false≢true (sym (cong lower p))
  cut5403 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (op (var 0) (var 2)))) (op (var 3) (var 4))) , (var 2)) → ⊥
  cut5403  adequate = bad5403  (Adequate.valid adequate Two boolean env15)
  bad5404 : PathP (λ _ → Two) (bop (bop b0 (bop b0 (bop b0 b0))) (bop b1 b0)) b1 → ⊥
  bad5404  p = false≢true (cong lower p)
  cut5404 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (op (var 0) (var 2)))) (op (var 3) (var 4))) , (var 3)) → ⊥
  cut5404  adequate = bad5404  (Adequate.valid adequate Two boolean env16)
  bad5405 : PathP (λ _ → Two) (bop (bop b0 (bop b0 (bop b0 b0))) (bop b0 b1)) b1 → ⊥
  bad5405  p = false≢true (cong lower p)
  cut5405 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (op (var 0) (var 2)))) (op (var 3) (var 4))) , (var 4)) → ⊥
  cut5405  adequate = bad5405  (Adequate.valid adequate Two boolean env10)
  bad5406 : PathP (λ _ → Two) (bop (bop b0 (bop b0 (bop b0 b0))) (bop b0 b0)) b1 → ⊥
  bad5406  p = false≢true (cong lower p)
  cut5406 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (op (var 0) (var 2)))) (op (var 3) (var 4))) , (var 5)) → ⊥
  cut5406  adequate = bad5406  (Adequate.valid adequate Two boolean env17)
  holds5407 : (z0 z1 : A2) → (mul2 (mul2 z0 (mul2 z1 (mul2 z1 z0))) (mul2 z0 z0)) ≡ z0
  holds5407 z0 z1 = refl
  cut5407 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (op (var 1) (var 0)))) (op (var 0) (var 0))) , (var 0)) → ⊥
  cut5407  = reject2 ((op (op (var 0) (op (var 1) (op (var 1) (var 0)))) (op (var 0) (var 0))) , (var 0)) (λ env → holds5407 (env 0) (env 1))
  bad5408 : PathP (λ _ → Two) (bop (bop b0 (bop b1 (bop b1 b0))) (bop b0 b0)) b1 → ⊥
  bad5408  p = false≢true (cong lower p)
  cut5408 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (op (var 1) (var 0)))) (op (var 0) (var 0))) , (var 1)) → ⊥
  cut5408  adequate = bad5408  (Adequate.valid adequate Two boolean env0)
  bad5409 : PathP (λ _ → Two) (bop (bop b0 (bop b0 (bop b0 b0))) (bop b0 b0)) b1 → ⊥
  bad5409  p = false≢true (cong lower p)
  cut5409 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (op (var 1) (var 0)))) (op (var 0) (var 0))) , (var 2)) → ⊥
  cut5409  adequate = bad5409  (Adequate.valid adequate Two boolean env1)
  holds5410 : (z0 z1 : A2) → (mul2 (mul2 z0 (mul2 z1 (mul2 z1 z0))) (mul2 z0 z1)) ≡ z0
  holds5410 z0 z1 = refl
  cut5410 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (op (var 1) (var 0)))) (op (var 0) (var 1))) , (var 0)) → ⊥
  cut5410  = reject2 ((op (op (var 0) (op (var 1) (op (var 1) (var 0)))) (op (var 0) (var 1))) , (var 0)) (λ env → holds5410 (env 0) (env 1))
  bad5411 : PathP (λ _ → Two) (bop (bop b0 (bop b1 (bop b1 b0))) (bop b0 b1)) b1 → ⊥
  bad5411  p = false≢true (cong lower p)
  cut5411 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (op (var 1) (var 0)))) (op (var 0) (var 1))) , (var 1)) → ⊥
  cut5411  adequate = bad5411  (Adequate.valid adequate Two boolean env0)
  bad5412 : PathP (λ _ → Two) (bop (bop b0 (bop b0 (bop b0 b0))) (bop b0 b0)) b1 → ⊥
  bad5412  p = false≢true (cong lower p)
  cut5412 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (op (var 1) (var 0)))) (op (var 0) (var 1))) , (var 2)) → ⊥
  cut5412  adequate = bad5412  (Adequate.valid adequate Two boolean env1)
  holds5413 : (z0 z1 z2 : A2) → (mul2 (mul2 z0 (mul2 z1 (mul2 z1 z0))) (mul2 z0 z2)) ≡ z0
  holds5413 z0 z1 z2 = refl
  cut5413 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (op (var 1) (var 0)))) (op (var 0) (var 2))) , (var 0)) → ⊥
  cut5413  = reject2 ((op (op (var 0) (op (var 1) (op (var 1) (var 0)))) (op (var 0) (var 2))) , (var 0)) (λ env → holds5413 (env 0) (env 1) (env 2))
  bad5414 : PathP (λ _ → Two) (bop (bop b0 (bop b1 (bop b1 b0))) (bop b0 b0)) b1 → ⊥
  bad5414  p = false≢true (cong lower p)
  cut5414 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (op (var 1) (var 0)))) (op (var 0) (var 2))) , (var 1)) → ⊥
  cut5414  adequate = bad5414  (Adequate.valid adequate Two boolean env4)
  bad5415 : PathP (λ _ → Two) (bop (bop b0 (bop b0 (bop b0 b0))) (bop b0 b1)) b1 → ⊥
  bad5415  p = false≢true (cong lower p)
  cut5415 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (op (var 1) (var 0)))) (op (var 0) (var 2))) , (var 2)) → ⊥
  cut5415  adequate = bad5415  (Adequate.valid adequate Two boolean env1)
  bad5416 : PathP (λ _ → Two) (bop (bop b0 (bop b0 (bop b0 b0))) (bop b0 b0)) b1 → ⊥
  bad5416  p = false≢true (cong lower p)
  cut5416 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (op (var 1) (var 0)))) (op (var 0) (var 2))) , (var 3)) → ⊥
  cut5416  adequate = bad5416  (Adequate.valid adequate Two boolean env5)
  holds5417 : (z0 z1 : A2) → (mul2 (mul2 z0 (mul2 z1 (mul2 z1 z0))) (mul2 z1 z0)) ≡ z0
  holds5417 z0 z1 = refl
  cut5417 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (op (var 1) (var 0)))) (op (var 1) (var 0))) , (var 0)) → ⊥
  cut5417  = reject2 ((op (op (var 0) (op (var 1) (op (var 1) (var 0)))) (op (var 1) (var 0))) , (var 0)) (λ env → holds5417 (env 0) (env 1))
  bad5418 : PathP (λ _ → Two) (bop (bop b0 (bop b1 (bop b1 b0))) (bop b1 b0)) b1 → ⊥
  bad5418  p = false≢true (cong lower p)
  cut5418 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (op (var 1) (var 0)))) (op (var 1) (var 0))) , (var 1)) → ⊥
  cut5418  adequate = bad5418  (Adequate.valid adequate Two boolean env0)
  bad5419 : PathP (λ _ → Two) (bop (bop b0 (bop b0 (bop b0 b0))) (bop b0 b0)) b1 → ⊥
  bad5419  p = false≢true (cong lower p)
  cut5419 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (op (var 1) (var 0)))) (op (var 1) (var 0))) , (var 2)) → ⊥
  cut5419  adequate = bad5419  (Adequate.valid adequate Two boolean env1)
  bad5420 : PathP (λ _ → Two) (bop (bop b0 (bop b1 (bop b1 b0))) (bop b1 b1)) b0 → ⊥
  bad5420  p = false≢true (sym (cong lower p))
  cut5420 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (op (var 1) (var 0)))) (op (var 1) (var 1))) , (var 0)) → ⊥
  cut5420  adequate = bad5420  (Adequate.valid adequate Two boolean env0)
  bad5421 : PathP (λ _ → Two) (bop (bop b1 (bop b0 (bop b0 b1))) (bop b0 b0)) b0 → ⊥
  bad5421  p = false≢true (sym (cong lower p))
  cut5421 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (op (var 1) (var 0)))) (op (var 1) (var 1))) , (var 1)) → ⊥
  cut5421  adequate = bad5421  (Adequate.valid adequate Two boolean env2)
  bad5422 : PathP (λ _ → Two) (bop (bop b0 (bop b0 (bop b0 b0))) (bop b0 b0)) b1 → ⊥
  bad5422  p = false≢true (cong lower p)
  cut5422 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (op (var 1) (var 0)))) (op (var 1) (var 1))) , (var 2)) → ⊥
  cut5422  adequate = bad5422  (Adequate.valid adequate Two boolean env1)
  bad5423 : PathP (λ _ → Two) (bop (bop b0 (bop b1 (bop b1 b0))) (bop b1 b1)) b0 → ⊥
  bad5423  p = false≢true (sym (cong lower p))
  cut5423 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (op (var 1) (var 0)))) (op (var 1) (var 2))) , (var 0)) → ⊥
  cut5423  adequate = bad5423  (Adequate.valid adequate Two boolean env3)
  bad5424 : PathP (λ _ → Two) (bop (bop b0 (bop b1 (bop b1 b0))) (bop b1 b0)) b1 → ⊥
  bad5424  p = false≢true (cong lower p)
  cut5424 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (op (var 1) (var 0)))) (op (var 1) (var 2))) , (var 1)) → ⊥
  cut5424  adequate = bad5424  (Adequate.valid adequate Two boolean env4)
  bad5425 : PathP (λ _ → Two) (bop (bop b0 (bop b0 (bop b0 b0))) (bop b0 b1)) b1 → ⊥
  bad5425  p = false≢true (cong lower p)
  cut5425 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (op (var 1) (var 0)))) (op (var 1) (var 2))) , (var 2)) → ⊥
  cut5425  adequate = bad5425  (Adequate.valid adequate Two boolean env1)
  bad5426 : PathP (λ _ → Two) (bop (bop b0 (bop b0 (bop b0 b0))) (bop b0 b0)) b1 → ⊥
  bad5426  p = false≢true (cong lower p)
  cut5426 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (op (var 1) (var 0)))) (op (var 1) (var 2))) , (var 3)) → ⊥
  cut5426  adequate = bad5426  (Adequate.valid adequate Two boolean env5)
  holds5427 : (z0 z1 z2 : A2) → (mul2 (mul2 z0 (mul2 z1 (mul2 z1 z0))) (mul2 z2 z0)) ≡ z0
  holds5427 z0 z1 z2 = refl
  cut5427 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (op (var 1) (var 0)))) (op (var 2) (var 0))) , (var 0)) → ⊥
  cut5427  = reject2 ((op (op (var 0) (op (var 1) (op (var 1) (var 0)))) (op (var 2) (var 0))) , (var 0)) (λ env → holds5427 (env 0) (env 1) (env 2))
  bad5428 : PathP (λ _ → Two) (bop (bop b0 (bop b1 (bop b1 b0))) (bop b0 b0)) b1 → ⊥
  bad5428  p = false≢true (cong lower p)
  cut5428 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (op (var 1) (var 0)))) (op (var 2) (var 0))) , (var 1)) → ⊥
  cut5428  adequate = bad5428  (Adequate.valid adequate Two boolean env4)
  bad5429 : PathP (λ _ → Two) (bop (bop b0 (bop b0 (bop b0 b0))) (bop b1 b0)) b1 → ⊥
  bad5429  p = false≢true (cong lower p)
  cut5429 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (op (var 1) (var 0)))) (op (var 2) (var 0))) , (var 2)) → ⊥
  cut5429  adequate = bad5429  (Adequate.valid adequate Two boolean env1)
  bad5430 : PathP (λ _ → Two) (bop (bop b0 (bop b0 (bop b0 b0))) (bop b0 b0)) b1 → ⊥
  bad5430  p = false≢true (cong lower p)
  cut5430 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (op (var 1) (var 0)))) (op (var 2) (var 0))) , (var 3)) → ⊥
  cut5430  adequate = bad5430  (Adequate.valid adequate Two boolean env5)
  bad5431 : PathP (λ _ → Two) (bop (bop b0 (bop b1 (bop b1 b0))) (bop b1 b1)) b0 → ⊥
  bad5431  p = false≢true (sym (cong lower p))
  cut5431 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (op (var 1) (var 0)))) (op (var 2) (var 1))) , (var 0)) → ⊥
  cut5431  adequate = bad5431  (Adequate.valid adequate Two boolean env3)
  bad5432 : PathP (λ _ → Two) (bop (bop b0 (bop b1 (bop b1 b0))) (bop b0 b1)) b1 → ⊥
  bad5432  p = false≢true (cong lower p)
  cut5432 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (op (var 1) (var 0)))) (op (var 2) (var 1))) , (var 1)) → ⊥
  cut5432  adequate = bad5432  (Adequate.valid adequate Two boolean env4)
  bad5433 : PathP (λ _ → Two) (bop (bop b0 (bop b0 (bop b0 b0))) (bop b1 b0)) b1 → ⊥
  bad5433  p = false≢true (cong lower p)
  cut5433 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (op (var 1) (var 0)))) (op (var 2) (var 1))) , (var 2)) → ⊥
  cut5433  adequate = bad5433  (Adequate.valid adequate Two boolean env1)
  bad5434 : PathP (λ _ → Two) (bop (bop b0 (bop b0 (bop b0 b0))) (bop b0 b0)) b1 → ⊥
  bad5434  p = false≢true (cong lower p)
  cut5434 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (op (var 1) (var 0)))) (op (var 2) (var 1))) , (var 3)) → ⊥
  cut5434  adequate = bad5434  (Adequate.valid adequate Two boolean env5)
  bad5435 : PathP (λ _ → Two) (bop (bop b0 (bop b0 (bop b0 b0))) (bop b1 b1)) b0 → ⊥
  bad5435  p = false≢true (sym (cong lower p))
  cut5435 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (op (var 1) (var 0)))) (op (var 2) (var 2))) , (var 0)) → ⊥
  cut5435  adequate = bad5435  (Adequate.valid adequate Two boolean env1)
  bad5436 : PathP (λ _ → Two) (bop (bop b0 (bop b0 (bop b0 b0))) (bop b1 b1)) b0 → ⊥
  bad5436  p = false≢true (sym (cong lower p))
  cut5436 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (op (var 1) (var 0)))) (op (var 2) (var 2))) , (var 1)) → ⊥
  cut5436  adequate = bad5436  (Adequate.valid adequate Two boolean env1)
  bad5437 : PathP (λ _ → Two) (bop (bop b1 (bop b0 (bop b0 b1))) (bop b0 b0)) b0 → ⊥
  bad5437  p = false≢true (sym (cong lower p))
  cut5437 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (op (var 1) (var 0)))) (op (var 2) (var 2))) , (var 2)) → ⊥
  cut5437  adequate = bad5437  (Adequate.valid adequate Two boolean env6)
  bad5438 : PathP (λ _ → Two) (bop (bop b0 (bop b0 (bop b0 b0))) (bop b0 b0)) b1 → ⊥
  bad5438  p = false≢true (cong lower p)
  cut5438 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (op (var 1) (var 0)))) (op (var 2) (var 2))) , (var 3)) → ⊥
  cut5438  adequate = bad5438  (Adequate.valid adequate Two boolean env5)
  bad5439 : PathP (λ _ → Two) (bop (bop b0 (bop b0 (bop b0 b0))) (bop b1 b1)) b0 → ⊥
  bad5439  p = false≢true (sym (cong lower p))
  cut5439 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (op (var 1) (var 0)))) (op (var 2) (var 3))) , (var 0)) → ⊥
  cut5439  adequate = bad5439  (Adequate.valid adequate Two boolean env8)
  bad5440 : PathP (λ _ → Two) (bop (bop b0 (bop b0 (bop b0 b0))) (bop b1 b1)) b0 → ⊥
  bad5440  p = false≢true (sym (cong lower p))
  cut5440 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (op (var 1) (var 0)))) (op (var 2) (var 3))) , (var 1)) → ⊥
  cut5440  adequate = bad5440  (Adequate.valid adequate Two boolean env8)
  bad5441 : PathP (λ _ → Two) (bop (bop b0 (bop b0 (bop b0 b0))) (bop b1 b0)) b1 → ⊥
  bad5441  p = false≢true (cong lower p)
  cut5441 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (op (var 1) (var 0)))) (op (var 2) (var 3))) , (var 2)) → ⊥
  cut5441  adequate = bad5441  (Adequate.valid adequate Two boolean env9)
  bad5442 : PathP (λ _ → Two) (bop (bop b0 (bop b0 (bop b0 b0))) (bop b0 b1)) b1 → ⊥
  bad5442  p = false≢true (cong lower p)
  cut5442 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (op (var 1) (var 0)))) (op (var 2) (var 3))) , (var 3)) → ⊥
  cut5442  adequate = bad5442  (Adequate.valid adequate Two boolean env5)
  bad5443 : PathP (λ _ → Two) (bop (bop b0 (bop b0 (bop b0 b0))) (bop b0 b0)) b1 → ⊥
  bad5443  p = false≢true (cong lower p)
  cut5443 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (op (var 1) (var 0)))) (op (var 2) (var 3))) , (var 4)) → ⊥
  cut5443  adequate = bad5443  (Adequate.valid adequate Two boolean env10)
  holds5444 : (z0 z1 : A2) → (mul2 (mul2 z0 (mul2 z1 (mul2 z1 z1))) (mul2 z0 z0)) ≡ z0
  holds5444 z0 z1 = refl
  cut5444 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (op (var 1) (var 1)))) (op (var 0) (var 0))) , (var 0)) → ⊥
  cut5444  = reject2 ((op (op (var 0) (op (var 1) (op (var 1) (var 1)))) (op (var 0) (var 0))) , (var 0)) (λ env → holds5444 (env 0) (env 1))
  bad5445 : PathP (λ _ → Two) (bop (bop b0 (bop b1 (bop b1 b1))) (bop b0 b0)) b1 → ⊥
  bad5445  p = false≢true (cong lower p)
  cut5445 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (op (var 1) (var 1)))) (op (var 0) (var 0))) , (var 1)) → ⊥
  cut5445  adequate = bad5445  (Adequate.valid adequate Two boolean env0)
  bad5446 : PathP (λ _ → Two) (bop (bop b0 (bop b0 (bop b0 b0))) (bop b0 b0)) b1 → ⊥
  bad5446  p = false≢true (cong lower p)
  cut5446 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (op (var 1) (var 1)))) (op (var 0) (var 0))) , (var 2)) → ⊥
  cut5446  adequate = bad5446  (Adequate.valid adequate Two boolean env1)
  holds5447 : (z0 z1 : A2) → (mul2 (mul2 z0 (mul2 z1 (mul2 z1 z1))) (mul2 z0 z1)) ≡ z0
  holds5447 z0 z1 = refl
  cut5447 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (op (var 1) (var 1)))) (op (var 0) (var 1))) , (var 0)) → ⊥
  cut5447  = reject2 ((op (op (var 0) (op (var 1) (op (var 1) (var 1)))) (op (var 0) (var 1))) , (var 0)) (λ env → holds5447 (env 0) (env 1))
  bad5448 : PathP (λ _ → Two) (bop (bop b0 (bop b1 (bop b1 b1))) (bop b0 b1)) b1 → ⊥
  bad5448  p = false≢true (cong lower p)
  cut5448 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (op (var 1) (var 1)))) (op (var 0) (var 1))) , (var 1)) → ⊥
  cut5448  adequate = bad5448  (Adequate.valid adequate Two boolean env0)
  bad5449 : PathP (λ _ → Two) (bop (bop b0 (bop b0 (bop b0 b0))) (bop b0 b0)) b1 → ⊥
  bad5449  p = false≢true (cong lower p)
  cut5449 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (op (var 1) (var 1)))) (op (var 0) (var 1))) , (var 2)) → ⊥
  cut5449  adequate = bad5449  (Adequate.valid adequate Two boolean env1)
  holds5450 : (z0 z1 z2 : A2) → (mul2 (mul2 z0 (mul2 z1 (mul2 z1 z1))) (mul2 z0 z2)) ≡ z0
  holds5450 z0 z1 z2 = refl
  cut5450 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (op (var 1) (var 1)))) (op (var 0) (var 2))) , (var 0)) → ⊥
  cut5450  = reject2 ((op (op (var 0) (op (var 1) (op (var 1) (var 1)))) (op (var 0) (var 2))) , (var 0)) (λ env → holds5450 (env 0) (env 1) (env 2))
  bad5451 : PathP (λ _ → Two) (bop (bop b0 (bop b1 (bop b1 b1))) (bop b0 b0)) b1 → ⊥
  bad5451  p = false≢true (cong lower p)
  cut5451 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (op (var 1) (var 1)))) (op (var 0) (var 2))) , (var 1)) → ⊥
  cut5451  adequate = bad5451  (Adequate.valid adequate Two boolean env4)
  bad5452 : PathP (λ _ → Two) (bop (bop b0 (bop b0 (bop b0 b0))) (bop b0 b1)) b1 → ⊥
  bad5452  p = false≢true (cong lower p)
  cut5452 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (op (var 1) (var 1)))) (op (var 0) (var 2))) , (var 2)) → ⊥
  cut5452  adequate = bad5452  (Adequate.valid adequate Two boolean env1)
  bad5453 : PathP (λ _ → Two) (bop (bop b0 (bop b0 (bop b0 b0))) (bop b0 b0)) b1 → ⊥
  bad5453  p = false≢true (cong lower p)
  cut5453 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (op (var 1) (var 1)))) (op (var 0) (var 2))) , (var 3)) → ⊥
  cut5453  adequate = bad5453  (Adequate.valid adequate Two boolean env5)
  holds5454 : (z0 z1 : A2) → (mul2 (mul2 z0 (mul2 z1 (mul2 z1 z1))) (mul2 z1 z0)) ≡ z0
  holds5454 z0 z1 = refl
  cut5454 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (op (var 1) (var 1)))) (op (var 1) (var 0))) , (var 0)) → ⊥
  cut5454  = reject2 ((op (op (var 0) (op (var 1) (op (var 1) (var 1)))) (op (var 1) (var 0))) , (var 0)) (λ env → holds5454 (env 0) (env 1))
  bad5455 : PathP (λ _ → Two) (bop (bop b0 (bop b1 (bop b1 b1))) (bop b1 b0)) b1 → ⊥
  bad5455  p = false≢true (cong lower p)
  cut5455 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (op (var 1) (var 1)))) (op (var 1) (var 0))) , (var 1)) → ⊥
  cut5455  adequate = bad5455  (Adequate.valid adequate Two boolean env0)
  bad5456 : PathP (λ _ → Two) (bop (bop b0 (bop b0 (bop b0 b0))) (bop b0 b0)) b1 → ⊥
  bad5456  p = false≢true (cong lower p)
  cut5456 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (op (var 1) (var 1)))) (op (var 1) (var 0))) , (var 2)) → ⊥
  cut5456  adequate = bad5456  (Adequate.valid adequate Two boolean env1)
  bad5457 : PathP (λ _ → Two) (bop (bop b0 (bop b1 (bop b1 b1))) (bop b1 b1)) b0 → ⊥
  bad5457  p = false≢true (sym (cong lower p))
  cut5457 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (op (var 1) (var 1)))) (op (var 1) (var 1))) , (var 0)) → ⊥
  cut5457  adequate = bad5457  (Adequate.valid adequate Two boolean env0)
  bad5458 : PathP (λ _ → Two) (bop (bop b1 (bop b0 (bop b0 b0))) (bop b0 b0)) b0 → ⊥
  bad5458  p = false≢true (sym (cong lower p))
  cut5458 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (op (var 1) (var 1)))) (op (var 1) (var 1))) , (var 1)) → ⊥
  cut5458  adequate = bad5458  (Adequate.valid adequate Two boolean env2)
  bad5459 : PathP (λ _ → Two) (bop (bop b0 (bop b0 (bop b0 b0))) (bop b0 b0)) b1 → ⊥
  bad5459  p = false≢true (cong lower p)
  cut5459 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (op (var 1) (var 1)))) (op (var 1) (var 1))) , (var 2)) → ⊥
  cut5459  adequate = bad5459  (Adequate.valid adequate Two boolean env1)
  bad5460 : PathP (λ _ → Two) (bop (bop b0 (bop b1 (bop b1 b1))) (bop b1 b1)) b0 → ⊥
  bad5460  p = false≢true (sym (cong lower p))
  cut5460 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (op (var 1) (var 1)))) (op (var 1) (var 2))) , (var 0)) → ⊥
  cut5460  adequate = bad5460  (Adequate.valid adequate Two boolean env3)
  bad5461 : PathP (λ _ → Two) (bop (bop b0 (bop b1 (bop b1 b1))) (bop b1 b0)) b1 → ⊥
  bad5461  p = false≢true (cong lower p)
  cut5461 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (op (var 1) (var 1)))) (op (var 1) (var 2))) , (var 1)) → ⊥
  cut5461  adequate = bad5461  (Adequate.valid adequate Two boolean env4)
  bad5462 : PathP (λ _ → Two) (bop (bop b0 (bop b0 (bop b0 b0))) (bop b0 b1)) b1 → ⊥
  bad5462  p = false≢true (cong lower p)
  cut5462 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (op (var 1) (var 1)))) (op (var 1) (var 2))) , (var 2)) → ⊥
  cut5462  adequate = bad5462  (Adequate.valid adequate Two boolean env1)
  bad5463 : PathP (λ _ → Two) (bop (bop b0 (bop b0 (bop b0 b0))) (bop b0 b0)) b1 → ⊥
  bad5463  p = false≢true (cong lower p)
  cut5463 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (op (var 1) (var 1)))) (op (var 1) (var 2))) , (var 3)) → ⊥
  cut5463  adequate = bad5463  (Adequate.valid adequate Two boolean env5)
  holds5464 : (z0 z1 z2 : A2) → (mul2 (mul2 z0 (mul2 z1 (mul2 z1 z1))) (mul2 z2 z0)) ≡ z0
  holds5464 z0 z1 z2 = refl
  cut5464 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (op (var 1) (var 1)))) (op (var 2) (var 0))) , (var 0)) → ⊥
  cut5464  = reject2 ((op (op (var 0) (op (var 1) (op (var 1) (var 1)))) (op (var 2) (var 0))) , (var 0)) (λ env → holds5464 (env 0) (env 1) (env 2))
  bad5465 : PathP (λ _ → Two) (bop (bop b0 (bop b1 (bop b1 b1))) (bop b0 b0)) b1 → ⊥
  bad5465  p = false≢true (cong lower p)
  cut5465 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (op (var 1) (var 1)))) (op (var 2) (var 0))) , (var 1)) → ⊥
  cut5465  adequate = bad5465  (Adequate.valid adequate Two boolean env4)
  bad5466 : PathP (λ _ → Two) (bop (bop b0 (bop b0 (bop b0 b0))) (bop b1 b0)) b1 → ⊥
  bad5466  p = false≢true (cong lower p)
  cut5466 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (op (var 1) (var 1)))) (op (var 2) (var 0))) , (var 2)) → ⊥
  cut5466  adequate = bad5466  (Adequate.valid adequate Two boolean env1)
  bad5467 : PathP (λ _ → Two) (bop (bop b0 (bop b0 (bop b0 b0))) (bop b0 b0)) b1 → ⊥
  bad5467  p = false≢true (cong lower p)
  cut5467 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (op (var 1) (var 1)))) (op (var 2) (var 0))) , (var 3)) → ⊥
  cut5467  adequate = bad5467  (Adequate.valid adequate Two boolean env5)
  bad5468 : PathP (λ _ → Two) (bop (bop b0 (bop b1 (bop b1 b1))) (bop b1 b1)) b0 → ⊥
  bad5468  p = false≢true (sym (cong lower p))
  cut5468 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (op (var 1) (var 1)))) (op (var 2) (var 1))) , (var 0)) → ⊥
  cut5468  adequate = bad5468  (Adequate.valid adequate Two boolean env3)
  bad5469 : PathP (λ _ → Two) (bop (bop b0 (bop b1 (bop b1 b1))) (bop b0 b1)) b1 → ⊥
  bad5469  p = false≢true (cong lower p)
  cut5469 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (op (var 1) (var 1)))) (op (var 2) (var 1))) , (var 1)) → ⊥
  cut5469  adequate = bad5469  (Adequate.valid adequate Two boolean env4)
  bad5470 : PathP (λ _ → Two) (bop (bop b0 (bop b0 (bop b0 b0))) (bop b1 b0)) b1 → ⊥
  bad5470  p = false≢true (cong lower p)
  cut5470 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (op (var 1) (var 1)))) (op (var 2) (var 1))) , (var 2)) → ⊥
  cut5470  adequate = bad5470  (Adequate.valid adequate Two boolean env1)
  bad5471 : PathP (λ _ → Two) (bop (bop b0 (bop b0 (bop b0 b0))) (bop b0 b0)) b1 → ⊥
  bad5471  p = false≢true (cong lower p)
  cut5471 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (op (var 1) (var 1)))) (op (var 2) (var 1))) , (var 3)) → ⊥
  cut5471  adequate = bad5471  (Adequate.valid adequate Two boolean env5)
  bad5472 : PathP (λ _ → Two) (bop (bop b0 (bop b0 (bop b0 b0))) (bop b1 b1)) b0 → ⊥
  bad5472  p = false≢true (sym (cong lower p))
  cut5472 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (op (var 1) (var 1)))) (op (var 2) (var 2))) , (var 0)) → ⊥
  cut5472  adequate = bad5472  (Adequate.valid adequate Two boolean env1)
  bad5473 : PathP (λ _ → Two) (bop (bop b0 (bop b0 (bop b0 b0))) (bop b1 b1)) b0 → ⊥
  bad5473  p = false≢true (sym (cong lower p))
  cut5473 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (op (var 1) (var 1)))) (op (var 2) (var 2))) , (var 1)) → ⊥
  cut5473  adequate = bad5473  (Adequate.valid adequate Two boolean env1)
  bad5474 : PathP (λ _ → Two) (bop (bop b1 (bop b0 (bop b0 b0))) (bop b0 b0)) b0 → ⊥
  bad5474  p = false≢true (sym (cong lower p))
  cut5474 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (op (var 1) (var 1)))) (op (var 2) (var 2))) , (var 2)) → ⊥
  cut5474  adequate = bad5474  (Adequate.valid adequate Two boolean env6)
  bad5475 : PathP (λ _ → Two) (bop (bop b0 (bop b0 (bop b0 b0))) (bop b0 b0)) b1 → ⊥
  bad5475  p = false≢true (cong lower p)
  cut5475 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (op (var 1) (var 1)))) (op (var 2) (var 2))) , (var 3)) → ⊥
  cut5475  adequate = bad5475  (Adequate.valid adequate Two boolean env5)
  bad5476 : PathP (λ _ → Two) (bop (bop b0 (bop b0 (bop b0 b0))) (bop b1 b1)) b0 → ⊥
  bad5476  p = false≢true (sym (cong lower p))
  cut5476 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (op (var 1) (var 1)))) (op (var 2) (var 3))) , (var 0)) → ⊥
  cut5476  adequate = bad5476  (Adequate.valid adequate Two boolean env8)
  bad5477 : PathP (λ _ → Two) (bop (bop b0 (bop b0 (bop b0 b0))) (bop b1 b1)) b0 → ⊥
  bad5477  p = false≢true (sym (cong lower p))
  cut5477 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (op (var 1) (var 1)))) (op (var 2) (var 3))) , (var 1)) → ⊥
  cut5477  adequate = bad5477  (Adequate.valid adequate Two boolean env8)
  bad5478 : PathP (λ _ → Two) (bop (bop b0 (bop b0 (bop b0 b0))) (bop b1 b0)) b1 → ⊥
  bad5478  p = false≢true (cong lower p)
  cut5478 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (op (var 1) (var 1)))) (op (var 2) (var 3))) , (var 2)) → ⊥
  cut5478  adequate = bad5478  (Adequate.valid adequate Two boolean env9)
  bad5479 : PathP (λ _ → Two) (bop (bop b0 (bop b0 (bop b0 b0))) (bop b0 b1)) b1 → ⊥
  bad5479  p = false≢true (cong lower p)
  cut5479 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (op (var 1) (var 1)))) (op (var 2) (var 3))) , (var 3)) → ⊥
  cut5479  adequate = bad5479  (Adequate.valid adequate Two boolean env5)
  bad5480 : PathP (λ _ → Two) (bop (bop b0 (bop b0 (bop b0 b0))) (bop b0 b0)) b1 → ⊥
  bad5480  p = false≢true (cong lower p)
  cut5480 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (op (var 1) (var 1)))) (op (var 2) (var 3))) , (var 4)) → ⊥
  cut5480  adequate = bad5480  (Adequate.valid adequate Two boolean env10)
  holds5481 : (z0 z1 z2 : A2) → (mul2 (mul2 z0 (mul2 z1 (mul2 z1 z2))) (mul2 z0 z0)) ≡ z0
  holds5481 z0 z1 z2 = refl
  cut5481 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (op (var 1) (var 2)))) (op (var 0) (var 0))) , (var 0)) → ⊥
  cut5481  = reject2 ((op (op (var 0) (op (var 1) (op (var 1) (var 2)))) (op (var 0) (var 0))) , (var 0)) (λ env → holds5481 (env 0) (env 1) (env 2))
  bad5482 : PathP (λ _ → Two) (bop (bop b0 (bop b1 (bop b1 b0))) (bop b0 b0)) b1 → ⊥
  bad5482  p = false≢true (cong lower p)
  cut5482 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (op (var 1) (var 2)))) (op (var 0) (var 0))) , (var 1)) → ⊥
  cut5482  adequate = bad5482  (Adequate.valid adequate Two boolean env4)
  bad5483 : PathP (λ _ → Two) (bop (bop b0 (bop b0 (bop b0 b1))) (bop b0 b0)) b1 → ⊥
  bad5483  p = false≢true (cong lower p)
  cut5483 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (op (var 1) (var 2)))) (op (var 0) (var 0))) , (var 2)) → ⊥
  cut5483  adequate = bad5483  (Adequate.valid adequate Two boolean env1)
  bad5484 : PathP (λ _ → Two) (bop (bop b0 (bop b0 (bop b0 b0))) (bop b0 b0)) b1 → ⊥
  bad5484  p = false≢true (cong lower p)
  cut5484 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (op (var 1) (var 2)))) (op (var 0) (var 0))) , (var 3)) → ⊥
  cut5484  adequate = bad5484  (Adequate.valid adequate Two boolean env5)
  holds5485 : (z0 z1 z2 : A2) → (mul2 (mul2 z0 (mul2 z1 (mul2 z1 z2))) (mul2 z0 z1)) ≡ z0
  holds5485 z0 z1 z2 = refl
  cut5485 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (op (var 1) (var 2)))) (op (var 0) (var 1))) , (var 0)) → ⊥
  cut5485  = reject2 ((op (op (var 0) (op (var 1) (op (var 1) (var 2)))) (op (var 0) (var 1))) , (var 0)) (λ env → holds5485 (env 0) (env 1) (env 2))
  bad5486 : PathP (λ _ → Two) (bop (bop b0 (bop b1 (bop b1 b0))) (bop b0 b1)) b1 → ⊥
  bad5486  p = false≢true (cong lower p)
  cut5486 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (op (var 1) (var 2)))) (op (var 0) (var 1))) , (var 1)) → ⊥
  cut5486  adequate = bad5486  (Adequate.valid adequate Two boolean env4)
  bad5487 : PathP (λ _ → Two) (bop (bop b0 (bop b0 (bop b0 b1))) (bop b0 b0)) b1 → ⊥
  bad5487  p = false≢true (cong lower p)
  cut5487 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (op (var 1) (var 2)))) (op (var 0) (var 1))) , (var 2)) → ⊥
  cut5487  adequate = bad5487  (Adequate.valid adequate Two boolean env1)
  bad5488 : PathP (λ _ → Two) (bop (bop b0 (bop b0 (bop b0 b0))) (bop b0 b0)) b1 → ⊥
  bad5488  p = false≢true (cong lower p)
  cut5488 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (op (var 1) (var 2)))) (op (var 0) (var 1))) , (var 3)) → ⊥
  cut5488  adequate = bad5488  (Adequate.valid adequate Two boolean env5)
  bad5489 : PathP (λ _ → Two) (bop (bop b1 (bop b1 (bop b1 b0))) (bop b1 b0)) b1 → ⊥
  bad5489  p = false≢true (cong lower p)
  cut5489 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (op (var 1) (var 2)))) (op (var 0) (var 2))) , (var 0)) → ⊥
  cut5489  adequate = bad5489  (Adequate.valid adequate Two boolean env7)
  bad5490 : PathP (λ _ → Two) (bop (bop b0 (bop b1 (bop b1 b0))) (bop b0 b0)) b1 → ⊥
  bad5490  p = false≢true (cong lower p)
  cut5490 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (op (var 1) (var 2)))) (op (var 0) (var 2))) , (var 1)) → ⊥
  cut5490  adequate = bad5490  (Adequate.valid adequate Two boolean env4)
  bad5491 : PathP (λ _ → Two) (bop (bop b0 (bop b0 (bop b0 b1))) (bop b0 b1)) b1 → ⊥
  bad5491  p = false≢true (cong lower p)
  cut5491 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (op (var 1) (var 2)))) (op (var 0) (var 2))) , (var 2)) → ⊥
  cut5491  adequate = bad5491  (Adequate.valid adequate Two boolean env1)
  bad5492 : PathP (λ _ → Two) (bop (bop b0 (bop b0 (bop b0 b0))) (bop b0 b0)) b1 → ⊥
  bad5492  p = false≢true (cong lower p)
  cut5492 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (op (var 1) (var 2)))) (op (var 0) (var 2))) , (var 3)) → ⊥
  cut5492  adequate = bad5492  (Adequate.valid adequate Two boolean env5)
  bad5493 : PathP (λ _ → Two) (bop (bop b1 (bop b1 (bop b1 b0))) (bop b1 b0)) b1 → ⊥
  bad5493  p = false≢true (cong lower p)
  cut5493 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (op (var 1) (var 2)))) (op (var 0) (var 3))) , (var 0)) → ⊥
  cut5493  adequate = bad5493  (Adequate.valid adequate Two boolean env18)
  bad5494 : PathP (λ _ → Two) (bop (bop b0 (bop b1 (bop b1 b0))) (bop b0 b0)) b1 → ⊥
  bad5494  p = false≢true (cong lower p)
  cut5494 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (op (var 1) (var 2)))) (op (var 0) (var 3))) , (var 1)) → ⊥
  cut5494  adequate = bad5494  (Adequate.valid adequate Two boolean env12)
  bad5495 : PathP (λ _ → Two) (bop (bop b0 (bop b0 (bop b0 b1))) (bop b0 b0)) b1 → ⊥
  bad5495  p = false≢true (cong lower p)
  cut5495 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (op (var 1) (var 2)))) (op (var 0) (var 3))) , (var 2)) → ⊥
  cut5495  adequate = bad5495  (Adequate.valid adequate Two boolean env9)
  bad5496 : PathP (λ _ → Two) (bop (bop b0 (bop b0 (bop b0 b0))) (bop b0 b1)) b1 → ⊥
  bad5496  p = false≢true (cong lower p)
  cut5496 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (op (var 1) (var 2)))) (op (var 0) (var 3))) , (var 3)) → ⊥
  cut5496  adequate = bad5496  (Adequate.valid adequate Two boolean env5)
  bad5497 : PathP (λ _ → Two) (bop (bop b0 (bop b0 (bop b0 b0))) (bop b0 b0)) b1 → ⊥
  bad5497  p = false≢true (cong lower p)
  cut5497 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (op (var 1) (var 2)))) (op (var 0) (var 3))) , (var 4)) → ⊥
  cut5497  adequate = bad5497  (Adequate.valid adequate Two boolean env10)
  holds5498 : (z0 z1 z2 : A2) → (mul2 (mul2 z0 (mul2 z1 (mul2 z1 z2))) (mul2 z1 z0)) ≡ z0
  holds5498 z0 z1 z2 = refl
  cut5498 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (op (var 1) (var 2)))) (op (var 1) (var 0))) , (var 0)) → ⊥
  cut5498  = reject2 ((op (op (var 0) (op (var 1) (op (var 1) (var 2)))) (op (var 1) (var 0))) , (var 0)) (λ env → holds5498 (env 0) (env 1) (env 2))
  bad5499 : PathP (λ _ → Two) (bop (bop b0 (bop b1 (bop b1 b0))) (bop b1 b0)) b1 → ⊥
  bad5499  p = false≢true (cong lower p)
  cut5499 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (op (var 1) (var 2)))) (op (var 1) (var 0))) , (var 1)) → ⊥
  cut5499  adequate = bad5499  (Adequate.valid adequate Two boolean env4)
  bad5500 : PathP (λ _ → Two) (bop (bop b0 (bop b0 (bop b0 b1))) (bop b0 b0)) b1 → ⊥
  bad5500  p = false≢true (cong lower p)
  cut5500 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (op (var 1) (var 2)))) (op (var 1) (var 0))) , (var 2)) → ⊥
  cut5500  adequate = bad5500  (Adequate.valid adequate Two boolean env1)
  bad5501 : PathP (λ _ → Two) (bop (bop b0 (bop b0 (bop b0 b0))) (bop b0 b0)) b1 → ⊥
  bad5501  p = false≢true (cong lower p)
  cut5501 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (op (var 1) (var 2)))) (op (var 1) (var 0))) , (var 3)) → ⊥
  cut5501  adequate = bad5501  (Adequate.valid adequate Two boolean env5)
  bad5502 : PathP (λ _ → Two) (bop (bop b0 (bop b1 (bop b1 b0))) (bop b1 b1)) b0 → ⊥
  bad5502  p = false≢true (sym (cong lower p))
  cut5502 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (op (var 1) (var 2)))) (op (var 1) (var 1))) , (var 0)) → ⊥
  cut5502  adequate = bad5502  (Adequate.valid adequate Two boolean env4)
  bad5503 : PathP (λ _ → Two) (bop (bop b1 (bop b0 (bop b0 b0))) (bop b0 b0)) b0 → ⊥
  bad5503  p = false≢true (sym (cong lower p))
  cut5503 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (op (var 1) (var 2)))) (op (var 1) (var 1))) , (var 1)) → ⊥
  cut5503  adequate = bad5503  (Adequate.valid adequate Two boolean env6)
  bad5504 : PathP (λ _ → Two) (bop (bop b0 (bop b0 (bop b0 b1))) (bop b0 b0)) b1 → ⊥
  bad5504  p = false≢true (cong lower p)
  cut5504 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (op (var 1) (var 2)))) (op (var 1) (var 1))) , (var 2)) → ⊥
  cut5504  adequate = bad5504  (Adequate.valid adequate Two boolean env1)
  bad5505 : PathP (λ _ → Two) (bop (bop b0 (bop b0 (bop b0 b0))) (bop b0 b0)) b1 → ⊥
  bad5505  p = false≢true (cong lower p)
  cut5505 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (op (var 1) (var 2)))) (op (var 1) (var 1))) , (var 3)) → ⊥
  cut5505  adequate = bad5505  (Adequate.valid adequate Two boolean env5)
  bad5506 : PathP (λ _ → Two) (bop (bop b0 (bop b1 (bop b1 b1))) (bop b1 b1)) b0 → ⊥
  bad5506  p = false≢true (sym (cong lower p))
  cut5506 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (op (var 1) (var 2)))) (op (var 1) (var 2))) , (var 0)) → ⊥
  cut5506  adequate = bad5506  (Adequate.valid adequate Two boolean env3)
  bad5507 : PathP (λ _ → Two) (bop (bop b0 (bop b1 (bop b1 b0))) (bop b1 b0)) b1 → ⊥
  bad5507  p = false≢true (cong lower p)
  cut5507 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (op (var 1) (var 2)))) (op (var 1) (var 2))) , (var 1)) → ⊥
  cut5507  adequate = bad5507  (Adequate.valid adequate Two boolean env4)
  bad5508 : PathP (λ _ → Two) (bop (bop b0 (bop b0 (bop b0 b1))) (bop b0 b1)) b1 → ⊥
  bad5508  p = false≢true (cong lower p)
  cut5508 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (op (var 1) (var 2)))) (op (var 1) (var 2))) , (var 2)) → ⊥
  cut5508  adequate = bad5508  (Adequate.valid adequate Two boolean env1)
  bad5509 : PathP (λ _ → Two) (bop (bop b0 (bop b0 (bop b0 b0))) (bop b0 b0)) b1 → ⊥
  bad5509  p = false≢true (cong lower p)
  cut5509 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (op (var 1) (var 2)))) (op (var 1) (var 2))) , (var 3)) → ⊥
  cut5509  adequate = bad5509  (Adequate.valid adequate Two boolean env5)
  bad5510 : PathP (λ _ → Two) (bop (bop b0 (bop b1 (bop b1 b0))) (bop b1 b1)) b0 → ⊥
  bad5510  p = false≢true (sym (cong lower p))
  cut5510 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (op (var 1) (var 2)))) (op (var 1) (var 3))) , (var 0)) → ⊥
  cut5510  adequate = bad5510  (Adequate.valid adequate Two boolean env13)
  bad5511 : PathP (λ _ → Two) (bop (bop b0 (bop b1 (bop b1 b0))) (bop b1 b0)) b1 → ⊥
  bad5511  p = false≢true (cong lower p)
  cut5511 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (op (var 1) (var 2)))) (op (var 1) (var 3))) , (var 1)) → ⊥
  cut5511  adequate = bad5511  (Adequate.valid adequate Two boolean env12)
  bad5512 : PathP (λ _ → Two) (bop (bop b0 (bop b0 (bop b0 b1))) (bop b0 b0)) b1 → ⊥
  bad5512  p = false≢true (cong lower p)
  cut5512 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (op (var 1) (var 2)))) (op (var 1) (var 3))) , (var 2)) → ⊥
  cut5512  adequate = bad5512  (Adequate.valid adequate Two boolean env9)
  bad5513 : PathP (λ _ → Two) (bop (bop b0 (bop b0 (bop b0 b0))) (bop b0 b1)) b1 → ⊥
  bad5513  p = false≢true (cong lower p)
  cut5513 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (op (var 1) (var 2)))) (op (var 1) (var 3))) , (var 3)) → ⊥
  cut5513  adequate = bad5513  (Adequate.valid adequate Two boolean env5)
  bad5514 : PathP (λ _ → Two) (bop (bop b0 (bop b0 (bop b0 b0))) (bop b0 b0)) b1 → ⊥
  bad5514  p = false≢true (cong lower p)
  cut5514 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (op (var 1) (var 2)))) (op (var 1) (var 3))) , (var 4)) → ⊥
  cut5514  adequate = bad5514  (Adequate.valid adequate Two boolean env10)
  bad5515 : PathP (λ _ → Two) (bop (bop b1 (bop b1 (bop b1 b0))) (bop b0 b1)) b1 → ⊥
  bad5515  p = false≢true (cong lower p)
  cut5515 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (op (var 1) (var 2)))) (op (var 2) (var 0))) , (var 0)) → ⊥
  cut5515  adequate = bad5515  (Adequate.valid adequate Two boolean env7)
  bad5516 : PathP (λ _ → Two) (bop (bop b0 (bop b1 (bop b1 b0))) (bop b0 b0)) b1 → ⊥
  bad5516  p = false≢true (cong lower p)
  cut5516 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (op (var 1) (var 2)))) (op (var 2) (var 0))) , (var 1)) → ⊥
  cut5516  adequate = bad5516  (Adequate.valid adequate Two boolean env4)
  bad5517 : PathP (λ _ → Two) (bop (bop b0 (bop b0 (bop b0 b1))) (bop b1 b0)) b1 → ⊥
  bad5517  p = false≢true (cong lower p)
  cut5517 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (op (var 1) (var 2)))) (op (var 2) (var 0))) , (var 2)) → ⊥
  cut5517  adequate = bad5517  (Adequate.valid adequate Two boolean env1)
  bad5518 : PathP (λ _ → Two) (bop (bop b0 (bop b0 (bop b0 b0))) (bop b0 b0)) b1 → ⊥
  bad5518  p = false≢true (cong lower p)
  cut5518 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (op (var 1) (var 2)))) (op (var 2) (var 0))) , (var 3)) → ⊥
  cut5518  adequate = bad5518  (Adequate.valid adequate Two boolean env5)
  bad5519 : PathP (λ _ → Two) (bop (bop b0 (bop b1 (bop b1 b1))) (bop b1 b1)) b0 → ⊥
  bad5519  p = false≢true (sym (cong lower p))
  cut5519 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (op (var 1) (var 2)))) (op (var 2) (var 1))) , (var 0)) → ⊥
  cut5519  adequate = bad5519  (Adequate.valid adequate Two boolean env3)
  bad5520 : PathP (λ _ → Two) (bop (bop b0 (bop b1 (bop b1 b0))) (bop b0 b1)) b1 → ⊥
  bad5520  p = false≢true (cong lower p)
  cut5520 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (op (var 1) (var 2)))) (op (var 2) (var 1))) , (var 1)) → ⊥
  cut5520  adequate = bad5520  (Adequate.valid adequate Two boolean env4)
  bad5521 : PathP (λ _ → Two) (bop (bop b0 (bop b0 (bop b0 b1))) (bop b1 b0)) b1 → ⊥
  bad5521  p = false≢true (cong lower p)
  cut5521 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (op (var 1) (var 2)))) (op (var 2) (var 1))) , (var 2)) → ⊥
  cut5521  adequate = bad5521  (Adequate.valid adequate Two boolean env1)
  bad5522 : PathP (λ _ → Two) (bop (bop b0 (bop b0 (bop b0 b0))) (bop b0 b0)) b1 → ⊥
  bad5522  p = false≢true (cong lower p)
  cut5522 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (op (var 1) (var 2)))) (op (var 2) (var 1))) , (var 3)) → ⊥
  cut5522  adequate = bad5522  (Adequate.valid adequate Two boolean env5)
  bad5523 : PathP (λ _ → Two) (bop (bop b0 (bop b0 (bop b0 b1))) (bop b1 b1)) b0 → ⊥
  bad5523  p = false≢true (sym (cong lower p))
  cut5523 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (op (var 1) (var 2)))) (op (var 2) (var 2))) , (var 0)) → ⊥
  cut5523  adequate = bad5523  (Adequate.valid adequate Two boolean env1)
  bad5524 : PathP (λ _ → Two) (bop (bop b0 (bop b0 (bop b0 b1))) (bop b1 b1)) b0 → ⊥
  bad5524  p = false≢true (sym (cong lower p))
  cut5524 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (op (var 1) (var 2)))) (op (var 2) (var 2))) , (var 1)) → ⊥
  cut5524  adequate = bad5524  (Adequate.valid adequate Two boolean env1)
  bad5525 : PathP (λ _ → Two) (bop (bop b1 (bop b0 (bop b0 b0))) (bop b0 b0)) b0 → ⊥
  bad5525  p = false≢true (sym (cong lower p))
  cut5525 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (op (var 1) (var 2)))) (op (var 2) (var 2))) , (var 2)) → ⊥
  cut5525  adequate = bad5525  (Adequate.valid adequate Two boolean env6)
  bad5526 : PathP (λ _ → Two) (bop (bop b0 (bop b0 (bop b0 b0))) (bop b0 b0)) b1 → ⊥
  bad5526  p = false≢true (cong lower p)
  cut5526 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (op (var 1) (var 2)))) (op (var 2) (var 2))) , (var 3)) → ⊥
  cut5526  adequate = bad5526  (Adequate.valid adequate Two boolean env5)
  bad5527 : PathP (λ _ → Two) (bop (bop b0 (bop b0 (bop b0 b1))) (bop b1 b1)) b0 → ⊥
  bad5527  p = false≢true (sym (cong lower p))
  cut5527 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (op (var 1) (var 2)))) (op (var 2) (var 3))) , (var 0)) → ⊥
  cut5527  adequate = bad5527  (Adequate.valid adequate Two boolean env8)
  bad5528 : PathP (λ _ → Two) (bop (bop b0 (bop b0 (bop b0 b1))) (bop b1 b1)) b0 → ⊥
  bad5528  p = false≢true (sym (cong lower p))
  cut5528 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (op (var 1) (var 2)))) (op (var 2) (var 3))) , (var 1)) → ⊥
  cut5528  adequate = bad5528  (Adequate.valid adequate Two boolean env8)
  bad5529 : PathP (λ _ → Two) (bop (bop b0 (bop b0 (bop b0 b1))) (bop b1 b0)) b1 → ⊥
  bad5529  p = false≢true (cong lower p)
  cut5529 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (op (var 1) (var 2)))) (op (var 2) (var 3))) , (var 2)) → ⊥
  cut5529  adequate = bad5529  (Adequate.valid adequate Two boolean env9)
  bad5530 : PathP (λ _ → Two) (bop (bop b0 (bop b0 (bop b0 b0))) (bop b0 b1)) b1 → ⊥
  bad5530  p = false≢true (cong lower p)
  cut5530 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (op (var 1) (var 2)))) (op (var 2) (var 3))) , (var 3)) → ⊥
  cut5530  adequate = bad5530  (Adequate.valid adequate Two boolean env5)
  bad5531 : PathP (λ _ → Two) (bop (bop b0 (bop b0 (bop b0 b0))) (bop b0 b0)) b1 → ⊥
  bad5531  p = false≢true (cong lower p)
  cut5531 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (op (var 1) (var 2)))) (op (var 2) (var 3))) , (var 4)) → ⊥
  cut5531  adequate = bad5531  (Adequate.valid adequate Two boolean env10)
  bad5532 : PathP (λ _ → Two) (bop (bop b1 (bop b1 (bop b1 b0))) (bop b0 b1)) b1 → ⊥
  bad5532  p = false≢true (cong lower p)
  cut5532 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (op (var 1) (var 2)))) (op (var 3) (var 0))) , (var 0)) → ⊥
  cut5532  adequate = bad5532  (Adequate.valid adequate Two boolean env18)
  bad5533 : PathP (λ _ → Two) (bop (bop b0 (bop b1 (bop b1 b0))) (bop b0 b0)) b1 → ⊥
  bad5533  p = false≢true (cong lower p)
  cut5533 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (op (var 1) (var 2)))) (op (var 3) (var 0))) , (var 1)) → ⊥
  cut5533  adequate = bad5533  (Adequate.valid adequate Two boolean env12)
  bad5534 : PathP (λ _ → Two) (bop (bop b0 (bop b0 (bop b0 b1))) (bop b0 b0)) b1 → ⊥
  bad5534  p = false≢true (cong lower p)
  cut5534 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (op (var 1) (var 2)))) (op (var 3) (var 0))) , (var 2)) → ⊥
  cut5534  adequate = bad5534  (Adequate.valid adequate Two boolean env9)
  bad5535 : PathP (λ _ → Two) (bop (bop b0 (bop b0 (bop b0 b0))) (bop b1 b0)) b1 → ⊥
  bad5535  p = false≢true (cong lower p)
  cut5535 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (op (var 1) (var 2)))) (op (var 3) (var 0))) , (var 3)) → ⊥
  cut5535  adequate = bad5535  (Adequate.valid adequate Two boolean env5)
  bad5536 : PathP (λ _ → Two) (bop (bop b0 (bop b0 (bop b0 b0))) (bop b0 b0)) b1 → ⊥
  bad5536  p = false≢true (cong lower p)
  cut5536 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (op (var 1) (var 2)))) (op (var 3) (var 0))) , (var 4)) → ⊥
  cut5536  adequate = bad5536  (Adequate.valid adequate Two boolean env10)
  bad5537 : PathP (λ _ → Two) (bop (bop b0 (bop b1 (bop b1 b0))) (bop b1 b1)) b0 → ⊥
  bad5537  p = false≢true (sym (cong lower p))
  cut5537 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (op (var 1) (var 2)))) (op (var 3) (var 1))) , (var 0)) → ⊥
  cut5537  adequate = bad5537  (Adequate.valid adequate Two boolean env13)
  bad5538 : PathP (λ _ → Two) (bop (bop b0 (bop b1 (bop b1 b0))) (bop b0 b1)) b1 → ⊥
  bad5538  p = false≢true (cong lower p)
  cut5538 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (op (var 1) (var 2)))) (op (var 3) (var 1))) , (var 1)) → ⊥
  cut5538  adequate = bad5538  (Adequate.valid adequate Two boolean env12)
  bad5539 : PathP (λ _ → Two) (bop (bop b0 (bop b0 (bop b0 b1))) (bop b0 b0)) b1 → ⊥
  bad5539  p = false≢true (cong lower p)
  cut5539 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (op (var 1) (var 2)))) (op (var 3) (var 1))) , (var 2)) → ⊥
  cut5539  adequate = bad5539  (Adequate.valid adequate Two boolean env9)
  bad5540 : PathP (λ _ → Two) (bop (bop b0 (bop b0 (bop b0 b0))) (bop b1 b0)) b1 → ⊥
  bad5540  p = false≢true (cong lower p)
  cut5540 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (op (var 1) (var 2)))) (op (var 3) (var 1))) , (var 3)) → ⊥
  cut5540  adequate = bad5540  (Adequate.valid adequate Two boolean env5)
  bad5541 : PathP (λ _ → Two) (bop (bop b0 (bop b0 (bop b0 b0))) (bop b0 b0)) b1 → ⊥
  bad5541  p = false≢true (cong lower p)
  cut5541 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (op (var 1) (var 2)))) (op (var 3) (var 1))) , (var 4)) → ⊥
  cut5541  adequate = bad5541  (Adequate.valid adequate Two boolean env10)
  bad5542 : PathP (λ _ → Two) (bop (bop b0 (bop b0 (bop b0 b1))) (bop b1 b1)) b0 → ⊥
  bad5542  p = false≢true (sym (cong lower p))
  cut5542 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (op (var 1) (var 2)))) (op (var 3) (var 2))) , (var 0)) → ⊥
  cut5542  adequate = bad5542  (Adequate.valid adequate Two boolean env8)
  bad5543 : PathP (λ _ → Two) (bop (bop b0 (bop b0 (bop b0 b1))) (bop b1 b1)) b0 → ⊥
  bad5543  p = false≢true (sym (cong lower p))
  cut5543 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (op (var 1) (var 2)))) (op (var 3) (var 2))) , (var 1)) → ⊥
  cut5543  adequate = bad5543  (Adequate.valid adequate Two boolean env8)
  bad5544 : PathP (λ _ → Two) (bop (bop b0 (bop b0 (bop b0 b1))) (bop b0 b1)) b1 → ⊥
  bad5544  p = false≢true (cong lower p)
  cut5544 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (op (var 1) (var 2)))) (op (var 3) (var 2))) , (var 2)) → ⊥
  cut5544  adequate = bad5544  (Adequate.valid adequate Two boolean env9)
  bad5545 : PathP (λ _ → Two) (bop (bop b0 (bop b0 (bop b0 b0))) (bop b1 b0)) b1 → ⊥
  bad5545  p = false≢true (cong lower p)
  cut5545 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (op (var 1) (var 2)))) (op (var 3) (var 2))) , (var 3)) → ⊥
  cut5545  adequate = bad5545  (Adequate.valid adequate Two boolean env5)
  bad5546 : PathP (λ _ → Two) (bop (bop b0 (bop b0 (bop b0 b0))) (bop b0 b0)) b1 → ⊥
  bad5546  p = false≢true (cong lower p)
  cut5546 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (op (var 1) (var 2)))) (op (var 3) (var 2))) , (var 4)) → ⊥
  cut5546  adequate = bad5546  (Adequate.valid adequate Two boolean env10)
  bad5547 : PathP (λ _ → Two) (bop (bop b0 (bop b0 (bop b0 b0))) (bop b1 b1)) b0 → ⊥
  bad5547  p = false≢true (sym (cong lower p))
  cut5547 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (op (var 1) (var 2)))) (op (var 3) (var 3))) , (var 0)) → ⊥
  cut5547  adequate = bad5547  (Adequate.valid adequate Two boolean env5)
  bad5548 : PathP (λ _ → Two) (bop (bop b0 (bop b0 (bop b0 b0))) (bop b1 b1)) b0 → ⊥
  bad5548  p = false≢true (sym (cong lower p))
  cut5548 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (op (var 1) (var 2)))) (op (var 3) (var 3))) , (var 1)) → ⊥
  cut5548  adequate = bad5548  (Adequate.valid adequate Two boolean env5)
  bad5549 : PathP (λ _ → Two) (bop (bop b0 (bop b0 (bop b0 b0))) (bop b1 b1)) b0 → ⊥
  bad5549  p = false≢true (sym (cong lower p))
  cut5549 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (op (var 1) (var 2)))) (op (var 3) (var 3))) , (var 2)) → ⊥
  cut5549  adequate = bad5549  (Adequate.valid adequate Two boolean env5)
  bad5550 : PathP (λ _ → Two) (bop (bop b1 (bop b0 (bop b0 b0))) (bop b0 b0)) b0 → ⊥
  bad5550  p = false≢true (sym (cong lower p))
  cut5550 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (op (var 1) (var 2)))) (op (var 3) (var 3))) , (var 3)) → ⊥
  cut5550  adequate = bad5550  (Adequate.valid adequate Two boolean env11)
  bad5551 : PathP (λ _ → Two) (bop (bop b0 (bop b0 (bop b0 b0))) (bop b0 b0)) b1 → ⊥
  bad5551  p = false≢true (cong lower p)
  cut5551 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (op (var 1) (var 2)))) (op (var 3) (var 3))) , (var 4)) → ⊥
  cut5551  adequate = bad5551  (Adequate.valid adequate Two boolean env10)
  bad5552 : PathP (λ _ → Two) (bop (bop b0 (bop b0 (bop b0 b0))) (bop b1 b1)) b0 → ⊥
  bad5552  p = false≢true (sym (cong lower p))
  cut5552 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (op (var 1) (var 2)))) (op (var 3) (var 4))) , (var 0)) → ⊥
  cut5552  adequate = bad5552  (Adequate.valid adequate Two boolean env15)
  bad5553 : PathP (λ _ → Two) (bop (bop b0 (bop b0 (bop b0 b0))) (bop b1 b1)) b0 → ⊥
  bad5553  p = false≢true (sym (cong lower p))
  cut5553 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (op (var 1) (var 2)))) (op (var 3) (var 4))) , (var 1)) → ⊥
  cut5553  adequate = bad5553  (Adequate.valid adequate Two boolean env15)
  bad5554 : PathP (λ _ → Two) (bop (bop b0 (bop b0 (bop b0 b0))) (bop b1 b1)) b0 → ⊥
  bad5554  p = false≢true (sym (cong lower p))
  cut5554 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (op (var 1) (var 2)))) (op (var 3) (var 4))) , (var 2)) → ⊥
  cut5554  adequate = bad5554  (Adequate.valid adequate Two boolean env15)
  bad5555 : PathP (λ _ → Two) (bop (bop b0 (bop b0 (bop b0 b0))) (bop b1 b0)) b1 → ⊥
  bad5555  p = false≢true (cong lower p)
  cut5555 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (op (var 1) (var 2)))) (op (var 3) (var 4))) , (var 3)) → ⊥
  cut5555  adequate = bad5555  (Adequate.valid adequate Two boolean env16)
  bad5556 : PathP (λ _ → Two) (bop (bop b0 (bop b0 (bop b0 b0))) (bop b0 b1)) b1 → ⊥
  bad5556  p = false≢true (cong lower p)
  cut5556 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (op (var 1) (var 2)))) (op (var 3) (var 4))) , (var 4)) → ⊥
  cut5556  adequate = bad5556  (Adequate.valid adequate Two boolean env10)
  bad5557 : PathP (λ _ → Two) (bop (bop b0 (bop b0 (bop b0 b0))) (bop b0 b0)) b1 → ⊥
  bad5557  p = false≢true (cong lower p)
  cut5557 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (op (var 1) (var 2)))) (op (var 3) (var 4))) , (var 5)) → ⊥
  cut5557  adequate = bad5557  (Adequate.valid adequate Two boolean env17)
  holds5558 : (z0 z1 z2 : A2) → (mul2 (mul2 z0 (mul2 z1 (mul2 z2 z0))) (mul2 z0 z0)) ≡ z0
  holds5558 z0 z1 z2 = refl
  cut5558 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (op (var 2) (var 0)))) (op (var 0) (var 0))) , (var 0)) → ⊥
  cut5558  = reject2 ((op (op (var 0) (op (var 1) (op (var 2) (var 0)))) (op (var 0) (var 0))) , (var 0)) (λ env → holds5558 (env 0) (env 1) (env 2))
  bad5559 : PathP (λ _ → Two) (bop (bop b0 (bop b1 (bop b0 b0))) (bop b0 b0)) b1 → ⊥
  bad5559  p = false≢true (cong lower p)
  cut5559 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (op (var 2) (var 0)))) (op (var 0) (var 0))) , (var 1)) → ⊥
  cut5559  adequate = bad5559  (Adequate.valid adequate Two boolean env4)
  bad5560 : PathP (λ _ → Two) (bop (bop b0 (bop b0 (bop b1 b0))) (bop b0 b0)) b1 → ⊥
  bad5560  p = false≢true (cong lower p)
  cut5560 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (op (var 2) (var 0)))) (op (var 0) (var 0))) , (var 2)) → ⊥
  cut5560  adequate = bad5560  (Adequate.valid adequate Two boolean env1)
  bad5561 : PathP (λ _ → Two) (bop (bop b0 (bop b0 (bop b0 b0))) (bop b0 b0)) b1 → ⊥
  bad5561  p = false≢true (cong lower p)
  cut5561 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (op (var 2) (var 0)))) (op (var 0) (var 0))) , (var 3)) → ⊥
  cut5561  adequate = bad5561  (Adequate.valid adequate Two boolean env5)
  holds5562 : (z0 z1 z2 : A2) → (mul2 (mul2 z0 (mul2 z1 (mul2 z2 z0))) (mul2 z0 z1)) ≡ z0
  holds5562 z0 z1 z2 = refl
  cut5562 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (op (var 2) (var 0)))) (op (var 0) (var 1))) , (var 0)) → ⊥
  cut5562  = reject2 ((op (op (var 0) (op (var 1) (op (var 2) (var 0)))) (op (var 0) (var 1))) , (var 0)) (λ env → holds5562 (env 0) (env 1) (env 2))
  bad5563 : PathP (λ _ → Two) (bop (bop b0 (bop b1 (bop b0 b0))) (bop b0 b1)) b1 → ⊥
  bad5563  p = false≢true (cong lower p)
  cut5563 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (op (var 2) (var 0)))) (op (var 0) (var 1))) , (var 1)) → ⊥
  cut5563  adequate = bad5563  (Adequate.valid adequate Two boolean env4)
  bad5564 : PathP (λ _ → Two) (bop (bop b0 (bop b0 (bop b1 b0))) (bop b0 b0)) b1 → ⊥
  bad5564  p = false≢true (cong lower p)
  cut5564 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (op (var 2) (var 0)))) (op (var 0) (var 1))) , (var 2)) → ⊥
  cut5564  adequate = bad5564  (Adequate.valid adequate Two boolean env1)
  bad5565 : PathP (λ _ → Two) (bop (bop b0 (bop b0 (bop b0 b0))) (bop b0 b0)) b1 → ⊥
  bad5565  p = false≢true (cong lower p)
  cut5565 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (op (var 2) (var 0)))) (op (var 0) (var 1))) , (var 3)) → ⊥
  cut5565  adequate = bad5565  (Adequate.valid adequate Two boolean env5)
  bad5566 : PathP (λ _ → Two) (bop (bop b1 (bop b1 (bop b0 b1))) (bop b1 b0)) b1 → ⊥
  bad5566  p = false≢true (cong lower p)
  cut5566 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (op (var 2) (var 0)))) (op (var 0) (var 2))) , (var 0)) → ⊥
  cut5566  adequate = bad5566  (Adequate.valid adequate Two boolean env7)
  bad5567 : PathP (λ _ → Two) (bop (bop b0 (bop b1 (bop b0 b0))) (bop b0 b0)) b1 → ⊥
  bad5567  p = false≢true (cong lower p)
  cut5567 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (op (var 2) (var 0)))) (op (var 0) (var 2))) , (var 1)) → ⊥
  cut5567  adequate = bad5567  (Adequate.valid adequate Two boolean env4)
  bad5568 : PathP (λ _ → Two) (bop (bop b0 (bop b0 (bop b1 b0))) (bop b0 b1)) b1 → ⊥
  bad5568  p = false≢true (cong lower p)
  cut5568 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (op (var 2) (var 0)))) (op (var 0) (var 2))) , (var 2)) → ⊥
  cut5568  adequate = bad5568  (Adequate.valid adequate Two boolean env1)
  bad5569 : PathP (λ _ → Two) (bop (bop b0 (bop b0 (bop b0 b0))) (bop b0 b0)) b1 → ⊥
  bad5569  p = false≢true (cong lower p)
  cut5569 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (op (var 2) (var 0)))) (op (var 0) (var 2))) , (var 3)) → ⊥
  cut5569  adequate = bad5569  (Adequate.valid adequate Two boolean env5)
  bad5570 : PathP (λ _ → Two) (bop (bop b1 (bop b1 (bop b0 b1))) (bop b1 b0)) b1 → ⊥
  bad5570  p = false≢true (cong lower p)
  cut5570 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (op (var 2) (var 0)))) (op (var 0) (var 3))) , (var 0)) → ⊥
  cut5570  adequate = bad5570  (Adequate.valid adequate Two boolean env18)
  bad5571 : PathP (λ _ → Two) (bop (bop b0 (bop b1 (bop b0 b0))) (bop b0 b0)) b1 → ⊥
  bad5571  p = false≢true (cong lower p)
  cut5571 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (op (var 2) (var 0)))) (op (var 0) (var 3))) , (var 1)) → ⊥
  cut5571  adequate = bad5571  (Adequate.valid adequate Two boolean env12)
  bad5572 : PathP (λ _ → Two) (bop (bop b0 (bop b0 (bop b1 b0))) (bop b0 b0)) b1 → ⊥
  bad5572  p = false≢true (cong lower p)
  cut5572 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (op (var 2) (var 0)))) (op (var 0) (var 3))) , (var 2)) → ⊥
  cut5572  adequate = bad5572  (Adequate.valid adequate Two boolean env9)
  bad5573 : PathP (λ _ → Two) (bop (bop b0 (bop b0 (bop b0 b0))) (bop b0 b1)) b1 → ⊥
  bad5573  p = false≢true (cong lower p)
  cut5573 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (op (var 2) (var 0)))) (op (var 0) (var 3))) , (var 3)) → ⊥
  cut5573  adequate = bad5573  (Adequate.valid adequate Two boolean env5)
  bad5574 : PathP (λ _ → Two) (bop (bop b0 (bop b0 (bop b0 b0))) (bop b0 b0)) b1 → ⊥
  bad5574  p = false≢true (cong lower p)
  cut5574 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (op (var 2) (var 0)))) (op (var 0) (var 3))) , (var 4)) → ⊥
  cut5574  adequate = bad5574  (Adequate.valid adequate Two boolean env10)
  holds5575 : (z0 z1 z2 : A2) → (mul2 (mul2 z0 (mul2 z1 (mul2 z2 z0))) (mul2 z1 z0)) ≡ z0
  holds5575 z0 z1 z2 = refl
  cut5575 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (op (var 2) (var 0)))) (op (var 1) (var 0))) , (var 0)) → ⊥
  cut5575  = reject2 ((op (op (var 0) (op (var 1) (op (var 2) (var 0)))) (op (var 1) (var 0))) , (var 0)) (λ env → holds5575 (env 0) (env 1) (env 2))
  bad5576 : PathP (λ _ → Two) (bop (bop b0 (bop b1 (bop b0 b0))) (bop b1 b0)) b1 → ⊥
  bad5576  p = false≢true (cong lower p)
  cut5576 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (op (var 2) (var 0)))) (op (var 1) (var 0))) , (var 1)) → ⊥
  cut5576  adequate = bad5576  (Adequate.valid adequate Two boolean env4)
  bad5577 : PathP (λ _ → Two) (bop (bop b0 (bop b0 (bop b1 b0))) (bop b0 b0)) b1 → ⊥
  bad5577  p = false≢true (cong lower p)
  cut5577 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (op (var 2) (var 0)))) (op (var 1) (var 0))) , (var 2)) → ⊥
  cut5577  adequate = bad5577  (Adequate.valid adequate Two boolean env1)
  bad5578 : PathP (λ _ → Two) (bop (bop b0 (bop b0 (bop b0 b0))) (bop b0 b0)) b1 → ⊥
  bad5578  p = false≢true (cong lower p)
  cut5578 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (op (var 2) (var 0)))) (op (var 1) (var 0))) , (var 3)) → ⊥
  cut5578  adequate = bad5578  (Adequate.valid adequate Two boolean env5)
  bad5579 : PathP (λ _ → Two) (bop (bop b0 (bop b1 (bop b0 b0))) (bop b1 b1)) b0 → ⊥
  bad5579  p = false≢true (sym (cong lower p))
  cut5579 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (op (var 2) (var 0)))) (op (var 1) (var 1))) , (var 0)) → ⊥
  cut5579  adequate = bad5579  (Adequate.valid adequate Two boolean env4)
  bad5580 : PathP (λ _ → Two) (bop (bop b1 (bop b0 (bop b0 b1))) (bop b0 b0)) b0 → ⊥
  bad5580  p = false≢true (sym (cong lower p))
  cut5580 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (op (var 2) (var 0)))) (op (var 1) (var 1))) , (var 1)) → ⊥
  cut5580  adequate = bad5580  (Adequate.valid adequate Two boolean env6)
  bad5581 : PathP (λ _ → Two) (bop (bop b0 (bop b0 (bop b1 b0))) (bop b0 b0)) b1 → ⊥
  bad5581  p = false≢true (cong lower p)
  cut5581 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (op (var 2) (var 0)))) (op (var 1) (var 1))) , (var 2)) → ⊥
  cut5581  adequate = bad5581  (Adequate.valid adequate Two boolean env1)
  bad5582 : PathP (λ _ → Two) (bop (bop b0 (bop b0 (bop b0 b0))) (bop b0 b0)) b1 → ⊥
  bad5582  p = false≢true (cong lower p)
  cut5582 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (op (var 2) (var 0)))) (op (var 1) (var 1))) , (var 3)) → ⊥
  cut5582  adequate = bad5582  (Adequate.valid adequate Two boolean env5)
  bad5583 : PathP (λ _ → Two) (bop (bop b0 (bop b1 (bop b1 b0))) (bop b1 b1)) b0 → ⊥
  bad5583  p = false≢true (sym (cong lower p))
  cut5583 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (op (var 2) (var 0)))) (op (var 1) (var 2))) , (var 0)) → ⊥
  cut5583  adequate = bad5583  (Adequate.valid adequate Two boolean env3)
  bad5584 : PathP (λ _ → Two) (bop (bop b0 (bop b1 (bop b0 b0))) (bop b1 b0)) b1 → ⊥
  bad5584  p = false≢true (cong lower p)
  cut5584 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (op (var 2) (var 0)))) (op (var 1) (var 2))) , (var 1)) → ⊥
  cut5584  adequate = bad5584  (Adequate.valid adequate Two boolean env4)
  bad5585 : PathP (λ _ → Two) (bop (bop b0 (bop b0 (bop b1 b0))) (bop b0 b1)) b1 → ⊥
  bad5585  p = false≢true (cong lower p)
  cut5585 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (op (var 2) (var 0)))) (op (var 1) (var 2))) , (var 2)) → ⊥
  cut5585  adequate = bad5585  (Adequate.valid adequate Two boolean env1)
  bad5586 : PathP (λ _ → Two) (bop (bop b0 (bop b0 (bop b0 b0))) (bop b0 b0)) b1 → ⊥
  bad5586  p = false≢true (cong lower p)
  cut5586 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (op (var 2) (var 0)))) (op (var 1) (var 2))) , (var 3)) → ⊥
  cut5586  adequate = bad5586  (Adequate.valid adequate Two boolean env5)
  bad5587 : PathP (λ _ → Two) (bop (bop b0 (bop b1 (bop b0 b0))) (bop b1 b1)) b0 → ⊥
  bad5587  p = false≢true (sym (cong lower p))
  cut5587 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (op (var 2) (var 0)))) (op (var 1) (var 3))) , (var 0)) → ⊥
  cut5587  adequate = bad5587  (Adequate.valid adequate Two boolean env13)
  bad5588 : PathP (λ _ → Two) (bop (bop b0 (bop b1 (bop b0 b0))) (bop b1 b0)) b1 → ⊥
  bad5588  p = false≢true (cong lower p)
  cut5588 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (op (var 2) (var 0)))) (op (var 1) (var 3))) , (var 1)) → ⊥
  cut5588  adequate = bad5588  (Adequate.valid adequate Two boolean env12)
  bad5589 : PathP (λ _ → Two) (bop (bop b0 (bop b0 (bop b1 b0))) (bop b0 b0)) b1 → ⊥
  bad5589  p = false≢true (cong lower p)
  cut5589 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (op (var 2) (var 0)))) (op (var 1) (var 3))) , (var 2)) → ⊥
  cut5589  adequate = bad5589  (Adequate.valid adequate Two boolean env9)
  bad5590 : PathP (λ _ → Two) (bop (bop b0 (bop b0 (bop b0 b0))) (bop b0 b1)) b1 → ⊥
  bad5590  p = false≢true (cong lower p)
  cut5590 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (op (var 2) (var 0)))) (op (var 1) (var 3))) , (var 3)) → ⊥
  cut5590  adequate = bad5590  (Adequate.valid adequate Two boolean env5)
  bad5591 : PathP (λ _ → Two) (bop (bop b0 (bop b0 (bop b0 b0))) (bop b0 b0)) b1 → ⊥
  bad5591  p = false≢true (cong lower p)
  cut5591 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (op (var 2) (var 0)))) (op (var 1) (var 3))) , (var 4)) → ⊥
  cut5591  adequate = bad5591  (Adequate.valid adequate Two boolean env10)
  bad5592 : PathP (λ _ → Two) (bop (bop b1 (bop b1 (bop b0 b1))) (bop b0 b1)) b1 → ⊥
  bad5592  p = false≢true (cong lower p)
  cut5592 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (op (var 2) (var 0)))) (op (var 2) (var 0))) , (var 0)) → ⊥
  cut5592  adequate = bad5592  (Adequate.valid adequate Two boolean env7)
  bad5593 : PathP (λ _ → Two) (bop (bop b0 (bop b1 (bop b0 b0))) (bop b0 b0)) b1 → ⊥
  bad5593  p = false≢true (cong lower p)
  cut5593 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (op (var 2) (var 0)))) (op (var 2) (var 0))) , (var 1)) → ⊥
  cut5593  adequate = bad5593  (Adequate.valid adequate Two boolean env4)
  bad5594 : PathP (λ _ → Two) (bop (bop b0 (bop b0 (bop b1 b0))) (bop b1 b0)) b1 → ⊥
  bad5594  p = false≢true (cong lower p)
  cut5594 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (op (var 2) (var 0)))) (op (var 2) (var 0))) , (var 2)) → ⊥
  cut5594  adequate = bad5594  (Adequate.valid adequate Two boolean env1)
  bad5595 : PathP (λ _ → Two) (bop (bop b0 (bop b0 (bop b0 b0))) (bop b0 b0)) b1 → ⊥
  bad5595  p = false≢true (cong lower p)
  cut5595 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (op (var 2) (var 0)))) (op (var 2) (var 0))) , (var 3)) → ⊥
  cut5595  adequate = bad5595  (Adequate.valid adequate Two boolean env5)
  bad5596 : PathP (λ _ → Two) (bop (bop b0 (bop b1 (bop b1 b0))) (bop b1 b1)) b0 → ⊥
  bad5596  p = false≢true (sym (cong lower p))
  cut5596 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (op (var 2) (var 0)))) (op (var 2) (var 1))) , (var 0)) → ⊥
  cut5596  adequate = bad5596  (Adequate.valid adequate Two boolean env3)
  bad5597 : PathP (λ _ → Two) (bop (bop b0 (bop b1 (bop b0 b0))) (bop b0 b1)) b1 → ⊥
  bad5597  p = false≢true (cong lower p)
  cut5597 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (op (var 2) (var 0)))) (op (var 2) (var 1))) , (var 1)) → ⊥
  cut5597  adequate = bad5597  (Adequate.valid adequate Two boolean env4)
  bad5598 : PathP (λ _ → Two) (bop (bop b0 (bop b0 (bop b1 b0))) (bop b1 b0)) b1 → ⊥
  bad5598  p = false≢true (cong lower p)
  cut5598 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (op (var 2) (var 0)))) (op (var 2) (var 1))) , (var 2)) → ⊥
  cut5598  adequate = bad5598  (Adequate.valid adequate Two boolean env1)
  bad5599 : PathP (λ _ → Two) (bop (bop b0 (bop b0 (bop b0 b0))) (bop b0 b0)) b1 → ⊥
  bad5599  p = false≢true (cong lower p)
  cut5599 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (op (var 2) (var 0)))) (op (var 2) (var 1))) , (var 3)) → ⊥
  cut5599  adequate = bad5599  (Adequate.valid adequate Two boolean env5)
  bad5600 : PathP (λ _ → Two) (bop (bop b0 (bop b0 (bop b1 b0))) (bop b1 b1)) b0 → ⊥
  bad5600  p = false≢true (sym (cong lower p))
  cut5600 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (op (var 2) (var 0)))) (op (var 2) (var 2))) , (var 0)) → ⊥
  cut5600  adequate = bad5600  (Adequate.valid adequate Two boolean env1)
  bad5601 : PathP (λ _ → Two) (bop (bop b0 (bop b0 (bop b1 b0))) (bop b1 b1)) b0 → ⊥
  bad5601  p = false≢true (sym (cong lower p))
  cut5601 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (op (var 2) (var 0)))) (op (var 2) (var 2))) , (var 1)) → ⊥
  cut5601  adequate = bad5601  (Adequate.valid adequate Two boolean env1)
  bad5602 : PathP (λ _ → Two) (bop (bop b1 (bop b0 (bop b0 b1))) (bop b0 b0)) b0 → ⊥
  bad5602  p = false≢true (sym (cong lower p))
  cut5602 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (op (var 2) (var 0)))) (op (var 2) (var 2))) , (var 2)) → ⊥
  cut5602  adequate = bad5602  (Adequate.valid adequate Two boolean env6)
  bad5603 : PathP (λ _ → Two) (bop (bop b0 (bop b0 (bop b0 b0))) (bop b0 b0)) b1 → ⊥
  bad5603  p = false≢true (cong lower p)
  cut5603 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (op (var 2) (var 0)))) (op (var 2) (var 2))) , (var 3)) → ⊥
  cut5603  adequate = bad5603  (Adequate.valid adequate Two boolean env5)
  bad5604 : PathP (λ _ → Two) (bop (bop b0 (bop b0 (bop b1 b0))) (bop b1 b1)) b0 → ⊥
  bad5604  p = false≢true (sym (cong lower p))
  cut5604 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (op (var 2) (var 0)))) (op (var 2) (var 3))) , (var 0)) → ⊥
  cut5604  adequate = bad5604  (Adequate.valid adequate Two boolean env8)
  bad5605 : PathP (λ _ → Two) (bop (bop b0 (bop b0 (bop b1 b0))) (bop b1 b1)) b0 → ⊥
  bad5605  p = false≢true (sym (cong lower p))
  cut5605 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (op (var 2) (var 0)))) (op (var 2) (var 3))) , (var 1)) → ⊥
  cut5605  adequate = bad5605  (Adequate.valid adequate Two boolean env8)
  bad5606 : PathP (λ _ → Two) (bop (bop b0 (bop b0 (bop b1 b0))) (bop b1 b0)) b1 → ⊥
  bad5606  p = false≢true (cong lower p)
  cut5606 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (op (var 2) (var 0)))) (op (var 2) (var 3))) , (var 2)) → ⊥
  cut5606  adequate = bad5606  (Adequate.valid adequate Two boolean env9)
  bad5607 : PathP (λ _ → Two) (bop (bop b0 (bop b0 (bop b0 b0))) (bop b0 b1)) b1 → ⊥
  bad5607  p = false≢true (cong lower p)
  cut5607 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (op (var 2) (var 0)))) (op (var 2) (var 3))) , (var 3)) → ⊥
  cut5607  adequate = bad5607  (Adequate.valid adequate Two boolean env5)
  bad5608 : PathP (λ _ → Two) (bop (bop b0 (bop b0 (bop b0 b0))) (bop b0 b0)) b1 → ⊥
  bad5608  p = false≢true (cong lower p)
  cut5608 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (op (var 2) (var 0)))) (op (var 2) (var 3))) , (var 4)) → ⊥
  cut5608  adequate = bad5608  (Adequate.valid adequate Two boolean env10)
  bad5609 : PathP (λ _ → Two) (bop (bop b1 (bop b1 (bop b0 b1))) (bop b0 b1)) b1 → ⊥
  bad5609  p = false≢true (cong lower p)
  cut5609 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (op (var 2) (var 0)))) (op (var 3) (var 0))) , (var 0)) → ⊥
  cut5609  adequate = bad5609  (Adequate.valid adequate Two boolean env18)
  bad5610 : PathP (λ _ → Two) (bop (bop b0 (bop b1 (bop b0 b0))) (bop b0 b0)) b1 → ⊥
  bad5610  p = false≢true (cong lower p)
  cut5610 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (op (var 2) (var 0)))) (op (var 3) (var 0))) , (var 1)) → ⊥
  cut5610  adequate = bad5610  (Adequate.valid adequate Two boolean env12)
  bad5611 : PathP (λ _ → Two) (bop (bop b0 (bop b0 (bop b1 b0))) (bop b0 b0)) b1 → ⊥
  bad5611  p = false≢true (cong lower p)
  cut5611 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (op (var 2) (var 0)))) (op (var 3) (var 0))) , (var 2)) → ⊥
  cut5611  adequate = bad5611  (Adequate.valid adequate Two boolean env9)
  bad5612 : PathP (λ _ → Two) (bop (bop b0 (bop b0 (bop b0 b0))) (bop b1 b0)) b1 → ⊥
  bad5612  p = false≢true (cong lower p)
  cut5612 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (op (var 2) (var 0)))) (op (var 3) (var 0))) , (var 3)) → ⊥
  cut5612  adequate = bad5612  (Adequate.valid adequate Two boolean env5)
  bad5613 : PathP (λ _ → Two) (bop (bop b0 (bop b0 (bop b0 b0))) (bop b0 b0)) b1 → ⊥
  bad5613  p = false≢true (cong lower p)
  cut5613 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (op (var 2) (var 0)))) (op (var 3) (var 0))) , (var 4)) → ⊥
  cut5613  adequate = bad5613  (Adequate.valid adequate Two boolean env10)
  bad5614 : PathP (λ _ → Two) (bop (bop b0 (bop b1 (bop b0 b0))) (bop b1 b1)) b0 → ⊥
  bad5614  p = false≢true (sym (cong lower p))
  cut5614 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (op (var 2) (var 0)))) (op (var 3) (var 1))) , (var 0)) → ⊥
  cut5614  adequate = bad5614  (Adequate.valid adequate Two boolean env13)
  bad5615 : PathP (λ _ → Two) (bop (bop b0 (bop b1 (bop b0 b0))) (bop b0 b1)) b1 → ⊥
  bad5615  p = false≢true (cong lower p)
  cut5615 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (op (var 2) (var 0)))) (op (var 3) (var 1))) , (var 1)) → ⊥
  cut5615  adequate = bad5615  (Adequate.valid adequate Two boolean env12)
  bad5616 : PathP (λ _ → Two) (bop (bop b0 (bop b0 (bop b1 b0))) (bop b0 b0)) b1 → ⊥
  bad5616  p = false≢true (cong lower p)
  cut5616 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (op (var 2) (var 0)))) (op (var 3) (var 1))) , (var 2)) → ⊥
  cut5616  adequate = bad5616  (Adequate.valid adequate Two boolean env9)
  bad5617 : PathP (λ _ → Two) (bop (bop b0 (bop b0 (bop b0 b0))) (bop b1 b0)) b1 → ⊥
  bad5617  p = false≢true (cong lower p)
  cut5617 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (op (var 2) (var 0)))) (op (var 3) (var 1))) , (var 3)) → ⊥
  cut5617  adequate = bad5617  (Adequate.valid adequate Two boolean env5)
  bad5618 : PathP (λ _ → Two) (bop (bop b0 (bop b0 (bop b0 b0))) (bop b0 b0)) b1 → ⊥
  bad5618  p = false≢true (cong lower p)
  cut5618 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (op (var 2) (var 0)))) (op (var 3) (var 1))) , (var 4)) → ⊥
  cut5618  adequate = bad5618  (Adequate.valid adequate Two boolean env10)
  bad5619 : PathP (λ _ → Two) (bop (bop b0 (bop b0 (bop b1 b0))) (bop b1 b1)) b0 → ⊥
  bad5619  p = false≢true (sym (cong lower p))
  cut5619 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (op (var 2) (var 0)))) (op (var 3) (var 2))) , (var 0)) → ⊥
  cut5619  adequate = bad5619  (Adequate.valid adequate Two boolean env8)
  bad5620 : PathP (λ _ → Two) (bop (bop b0 (bop b0 (bop b1 b0))) (bop b1 b1)) b0 → ⊥
  bad5620  p = false≢true (sym (cong lower p))
  cut5620 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (op (var 2) (var 0)))) (op (var 3) (var 2))) , (var 1)) → ⊥
  cut5620  adequate = bad5620  (Adequate.valid adequate Two boolean env8)
  bad5621 : PathP (λ _ → Two) (bop (bop b0 (bop b0 (bop b1 b0))) (bop b0 b1)) b1 → ⊥
  bad5621  p = false≢true (cong lower p)
  cut5621 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (op (var 2) (var 0)))) (op (var 3) (var 2))) , (var 2)) → ⊥
  cut5621  adequate = bad5621  (Adequate.valid adequate Two boolean env9)
  bad5622 : PathP (λ _ → Two) (bop (bop b0 (bop b0 (bop b0 b0))) (bop b1 b0)) b1 → ⊥
  bad5622  p = false≢true (cong lower p)
  cut5622 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (op (var 2) (var 0)))) (op (var 3) (var 2))) , (var 3)) → ⊥
  cut5622  adequate = bad5622  (Adequate.valid adequate Two boolean env5)
  bad5623 : PathP (λ _ → Two) (bop (bop b0 (bop b0 (bop b0 b0))) (bop b0 b0)) b1 → ⊥
  bad5623  p = false≢true (cong lower p)
  cut5623 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (op (var 2) (var 0)))) (op (var 3) (var 2))) , (var 4)) → ⊥
  cut5623  adequate = bad5623  (Adequate.valid adequate Two boolean env10)
  bad5624 : PathP (λ _ → Two) (bop (bop b0 (bop b0 (bop b0 b0))) (bop b1 b1)) b0 → ⊥
  bad5624  p = false≢true (sym (cong lower p))
  cut5624 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (op (var 2) (var 0)))) (op (var 3) (var 3))) , (var 0)) → ⊥
  cut5624  adequate = bad5624  (Adequate.valid adequate Two boolean env5)
  bad5625 : PathP (λ _ → Two) (bop (bop b0 (bop b0 (bop b0 b0))) (bop b1 b1)) b0 → ⊥
  bad5625  p = false≢true (sym (cong lower p))
  cut5625 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (op (var 2) (var 0)))) (op (var 3) (var 3))) , (var 1)) → ⊥
  cut5625  adequate = bad5625  (Adequate.valid adequate Two boolean env5)
  bad5626 : PathP (λ _ → Two) (bop (bop b0 (bop b0 (bop b0 b0))) (bop b1 b1)) b0 → ⊥
  bad5626  p = false≢true (sym (cong lower p))
  cut5626 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (op (var 2) (var 0)))) (op (var 3) (var 3))) , (var 2)) → ⊥
  cut5626  adequate = bad5626  (Adequate.valid adequate Two boolean env5)
  bad5627 : PathP (λ _ → Two) (bop (bop b1 (bop b0 (bop b0 b1))) (bop b0 b0)) b0 → ⊥
  bad5627  p = false≢true (sym (cong lower p))
  cut5627 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (op (var 2) (var 0)))) (op (var 3) (var 3))) , (var 3)) → ⊥
  cut5627  adequate = bad5627  (Adequate.valid adequate Two boolean env11)
  bad5628 : PathP (λ _ → Two) (bop (bop b0 (bop b0 (bop b0 b0))) (bop b0 b0)) b1 → ⊥
  bad5628  p = false≢true (cong lower p)
  cut5628 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (op (var 2) (var 0)))) (op (var 3) (var 3))) , (var 4)) → ⊥
  cut5628  adequate = bad5628  (Adequate.valid adequate Two boolean env10)
  bad5629 : PathP (λ _ → Two) (bop (bop b0 (bop b0 (bop b0 b0))) (bop b1 b1)) b0 → ⊥
  bad5629  p = false≢true (sym (cong lower p))
  cut5629 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (op (var 2) (var 0)))) (op (var 3) (var 4))) , (var 0)) → ⊥
  cut5629  adequate = bad5629  (Adequate.valid adequate Two boolean env15)
  bad5630 : PathP (λ _ → Two) (bop (bop b0 (bop b0 (bop b0 b0))) (bop b1 b1)) b0 → ⊥
  bad5630  p = false≢true (sym (cong lower p))
  cut5630 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (op (var 2) (var 0)))) (op (var 3) (var 4))) , (var 1)) → ⊥
  cut5630  adequate = bad5630  (Adequate.valid adequate Two boolean env15)
  bad5631 : PathP (λ _ → Two) (bop (bop b0 (bop b0 (bop b0 b0))) (bop b1 b1)) b0 → ⊥
  bad5631  p = false≢true (sym (cong lower p))
  cut5631 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (op (var 2) (var 0)))) (op (var 3) (var 4))) , (var 2)) → ⊥
  cut5631  adequate = bad5631  (Adequate.valid adequate Two boolean env15)
  bad5632 : PathP (λ _ → Two) (bop (bop b0 (bop b0 (bop b0 b0))) (bop b1 b0)) b1 → ⊥
  bad5632  p = false≢true (cong lower p)
  cut5632 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (op (var 2) (var 0)))) (op (var 3) (var 4))) , (var 3)) → ⊥
  cut5632  adequate = bad5632  (Adequate.valid adequate Two boolean env16)
  bad5633 : PathP (λ _ → Two) (bop (bop b0 (bop b0 (bop b0 b0))) (bop b0 b1)) b1 → ⊥
  bad5633  p = false≢true (cong lower p)
  cut5633 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (op (var 2) (var 0)))) (op (var 3) (var 4))) , (var 4)) → ⊥
  cut5633  adequate = bad5633  (Adequate.valid adequate Two boolean env10)
  bad5634 : PathP (λ _ → Two) (bop (bop b0 (bop b0 (bop b0 b0))) (bop b0 b0)) b1 → ⊥
  bad5634  p = false≢true (cong lower p)
  cut5634 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (op (var 2) (var 0)))) (op (var 3) (var 4))) , (var 5)) → ⊥
  cut5634  adequate = bad5634  (Adequate.valid adequate Two boolean env17)
  holds5635 : (z0 z1 z2 : A2) → (mul2 (mul2 z0 (mul2 z1 (mul2 z2 z1))) (mul2 z0 z0)) ≡ z0
  holds5635 z0 z1 z2 = refl
  cut5635 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (op (var 2) (var 1)))) (op (var 0) (var 0))) , (var 0)) → ⊥
  cut5635  = reject2 ((op (op (var 0) (op (var 1) (op (var 2) (var 1)))) (op (var 0) (var 0))) , (var 0)) (λ env → holds5635 (env 0) (env 1) (env 2))
  bad5636 : PathP (λ _ → Two) (bop (bop b0 (bop b1 (bop b0 b1))) (bop b0 b0)) b1 → ⊥
  bad5636  p = false≢true (cong lower p)
  cut5636 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (op (var 2) (var 1)))) (op (var 0) (var 0))) , (var 1)) → ⊥
  cut5636  adequate = bad5636  (Adequate.valid adequate Two boolean env4)
  bad5637 : PathP (λ _ → Two) (bop (bop b0 (bop b0 (bop b1 b0))) (bop b0 b0)) b1 → ⊥
  bad5637  p = false≢true (cong lower p)
  cut5637 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (op (var 2) (var 1)))) (op (var 0) (var 0))) , (var 2)) → ⊥
  cut5637  adequate = bad5637  (Adequate.valid adequate Two boolean env1)
  bad5638 : PathP (λ _ → Two) (bop (bop b0 (bop b0 (bop b0 b0))) (bop b0 b0)) b1 → ⊥
  bad5638  p = false≢true (cong lower p)
  cut5638 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (op (var 2) (var 1)))) (op (var 0) (var 0))) , (var 3)) → ⊥
  cut5638  adequate = bad5638  (Adequate.valid adequate Two boolean env5)
  holds5639 : (z0 z1 z2 : A2) → (mul2 (mul2 z0 (mul2 z1 (mul2 z2 z1))) (mul2 z0 z1)) ≡ z0
  holds5639 z0 z1 z2 = refl
  cut5639 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (op (var 2) (var 1)))) (op (var 0) (var 1))) , (var 0)) → ⊥
  cut5639  = reject2 ((op (op (var 0) (op (var 1) (op (var 2) (var 1)))) (op (var 0) (var 1))) , (var 0)) (λ env → holds5639 (env 0) (env 1) (env 2))
  bad5640 : PathP (λ _ → Two) (bop (bop b0 (bop b1 (bop b0 b1))) (bop b0 b1)) b1 → ⊥
  bad5640  p = false≢true (cong lower p)
  cut5640 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (op (var 2) (var 1)))) (op (var 0) (var 1))) , (var 1)) → ⊥
  cut5640  adequate = bad5640  (Adequate.valid adequate Two boolean env4)
  bad5641 : PathP (λ _ → Two) (bop (bop b0 (bop b0 (bop b1 b0))) (bop b0 b0)) b1 → ⊥
  bad5641  p = false≢true (cong lower p)
  cut5641 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (op (var 2) (var 1)))) (op (var 0) (var 1))) , (var 2)) → ⊥
  cut5641  adequate = bad5641  (Adequate.valid adequate Two boolean env1)
  bad5642 : PathP (λ _ → Two) (bop (bop b0 (bop b0 (bop b0 b0))) (bop b0 b0)) b1 → ⊥
  bad5642  p = false≢true (cong lower p)
  cut5642 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (op (var 2) (var 1)))) (op (var 0) (var 1))) , (var 3)) → ⊥
  cut5642  adequate = bad5642  (Adequate.valid adequate Two boolean env5)
  bad5643 : PathP (λ _ → Two) (bop (bop b1 (bop b1 (bop b0 b1))) (bop b1 b0)) b1 → ⊥
  bad5643  p = false≢true (cong lower p)
  cut5643 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (op (var 2) (var 1)))) (op (var 0) (var 2))) , (var 0)) → ⊥
  cut5643  adequate = bad5643  (Adequate.valid adequate Two boolean env7)
  bad5644 : PathP (λ _ → Two) (bop (bop b0 (bop b1 (bop b0 b1))) (bop b0 b0)) b1 → ⊥
  bad5644  p = false≢true (cong lower p)
  cut5644 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (op (var 2) (var 1)))) (op (var 0) (var 2))) , (var 1)) → ⊥
  cut5644  adequate = bad5644  (Adequate.valid adequate Two boolean env4)
  bad5645 : PathP (λ _ → Two) (bop (bop b0 (bop b0 (bop b1 b0))) (bop b0 b1)) b1 → ⊥
  bad5645  p = false≢true (cong lower p)
  cut5645 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (op (var 2) (var 1)))) (op (var 0) (var 2))) , (var 2)) → ⊥
  cut5645  adequate = bad5645  (Adequate.valid adequate Two boolean env1)
  bad5646 : PathP (λ _ → Two) (bop (bop b0 (bop b0 (bop b0 b0))) (bop b0 b0)) b1 → ⊥
  bad5646  p = false≢true (cong lower p)
  cut5646 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (op (var 2) (var 1)))) (op (var 0) (var 2))) , (var 3)) → ⊥
  cut5646  adequate = bad5646  (Adequate.valid adequate Two boolean env5)
  bad5647 : PathP (λ _ → Two) (bop (bop b1 (bop b1 (bop b0 b1))) (bop b1 b0)) b1 → ⊥
  bad5647  p = false≢true (cong lower p)
  cut5647 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (op (var 2) (var 1)))) (op (var 0) (var 3))) , (var 0)) → ⊥
  cut5647  adequate = bad5647  (Adequate.valid adequate Two boolean env18)
  bad5648 : PathP (λ _ → Two) (bop (bop b0 (bop b1 (bop b0 b1))) (bop b0 b0)) b1 → ⊥
  bad5648  p = false≢true (cong lower p)
  cut5648 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (op (var 2) (var 1)))) (op (var 0) (var 3))) , (var 1)) → ⊥
  cut5648  adequate = bad5648  (Adequate.valid adequate Two boolean env12)
  bad5649 : PathP (λ _ → Two) (bop (bop b0 (bop b0 (bop b1 b0))) (bop b0 b0)) b1 → ⊥
  bad5649  p = false≢true (cong lower p)
  cut5649 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (op (var 2) (var 1)))) (op (var 0) (var 3))) , (var 2)) → ⊥
  cut5649  adequate = bad5649  (Adequate.valid adequate Two boolean env9)
  bad5650 : PathP (λ _ → Two) (bop (bop b0 (bop b0 (bop b0 b0))) (bop b0 b1)) b1 → ⊥
  bad5650  p = false≢true (cong lower p)
  cut5650 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (op (var 2) (var 1)))) (op (var 0) (var 3))) , (var 3)) → ⊥
  cut5650  adequate = bad5650  (Adequate.valid adequate Two boolean env5)
  bad5651 : PathP (λ _ → Two) (bop (bop b0 (bop b0 (bop b0 b0))) (bop b0 b0)) b1 → ⊥
  bad5651  p = false≢true (cong lower p)
  cut5651 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (op (var 2) (var 1)))) (op (var 0) (var 3))) , (var 4)) → ⊥
  cut5651  adequate = bad5651  (Adequate.valid adequate Two boolean env10)
  holds5652 : (z0 z1 z2 : A2) → (mul2 (mul2 z0 (mul2 z1 (mul2 z2 z1))) (mul2 z1 z0)) ≡ z0
  holds5652 z0 z1 z2 = refl
  cut5652 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (op (var 2) (var 1)))) (op (var 1) (var 0))) , (var 0)) → ⊥
  cut5652  = reject2 ((op (op (var 0) (op (var 1) (op (var 2) (var 1)))) (op (var 1) (var 0))) , (var 0)) (λ env → holds5652 (env 0) (env 1) (env 2))
  bad5653 : PathP (λ _ → Two) (bop (bop b0 (bop b1 (bop b0 b1))) (bop b1 b0)) b1 → ⊥
  bad5653  p = false≢true (cong lower p)
  cut5653 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (op (var 2) (var 1)))) (op (var 1) (var 0))) , (var 1)) → ⊥
  cut5653  adequate = bad5653  (Adequate.valid adequate Two boolean env4)
  bad5654 : PathP (λ _ → Two) (bop (bop b0 (bop b0 (bop b1 b0))) (bop b0 b0)) b1 → ⊥
  bad5654  p = false≢true (cong lower p)
  cut5654 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (op (var 2) (var 1)))) (op (var 1) (var 0))) , (var 2)) → ⊥
  cut5654  adequate = bad5654  (Adequate.valid adequate Two boolean env1)
  bad5655 : PathP (λ _ → Two) (bop (bop b0 (bop b0 (bop b0 b0))) (bop b0 b0)) b1 → ⊥
  bad5655  p = false≢true (cong lower p)
  cut5655 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (op (var 2) (var 1)))) (op (var 1) (var 0))) , (var 3)) → ⊥
  cut5655  adequate = bad5655  (Adequate.valid adequate Two boolean env5)
  bad5656 : PathP (λ _ → Two) (bop (bop b0 (bop b1 (bop b0 b1))) (bop b1 b1)) b0 → ⊥
  bad5656  p = false≢true (sym (cong lower p))
  cut5656 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (op (var 2) (var 1)))) (op (var 1) (var 1))) , (var 0)) → ⊥
  cut5656  adequate = bad5656  (Adequate.valid adequate Two boolean env4)
  bad5657 : PathP (λ _ → Two) (bop (bop b1 (bop b0 (bop b0 b0))) (bop b0 b0)) b0 → ⊥
  bad5657  p = false≢true (sym (cong lower p))
  cut5657 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (op (var 2) (var 1)))) (op (var 1) (var 1))) , (var 1)) → ⊥
  cut5657  adequate = bad5657  (Adequate.valid adequate Two boolean env6)
  bad5658 : PathP (λ _ → Two) (bop (bop b0 (bop b0 (bop b1 b0))) (bop b0 b0)) b1 → ⊥
  bad5658  p = false≢true (cong lower p)
  cut5658 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (op (var 2) (var 1)))) (op (var 1) (var 1))) , (var 2)) → ⊥
  cut5658  adequate = bad5658  (Adequate.valid adequate Two boolean env1)
  bad5659 : PathP (λ _ → Two) (bop (bop b0 (bop b0 (bop b0 b0))) (bop b0 b0)) b1 → ⊥
  bad5659  p = false≢true (cong lower p)
  cut5659 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (op (var 2) (var 1)))) (op (var 1) (var 1))) , (var 3)) → ⊥
  cut5659  adequate = bad5659  (Adequate.valid adequate Two boolean env5)
  bad5660 : PathP (λ _ → Two) (bop (bop b0 (bop b1 (bop b1 b1))) (bop b1 b1)) b0 → ⊥
  bad5660  p = false≢true (sym (cong lower p))
  cut5660 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (op (var 2) (var 1)))) (op (var 1) (var 2))) , (var 0)) → ⊥
  cut5660  adequate = bad5660  (Adequate.valid adequate Two boolean env3)
  bad5661 : PathP (λ _ → Two) (bop (bop b0 (bop b1 (bop b0 b1))) (bop b1 b0)) b1 → ⊥
  bad5661  p = false≢true (cong lower p)
  cut5661 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (op (var 2) (var 1)))) (op (var 1) (var 2))) , (var 1)) → ⊥
  cut5661  adequate = bad5661  (Adequate.valid adequate Two boolean env4)
  bad5662 : PathP (λ _ → Two) (bop (bop b0 (bop b0 (bop b1 b0))) (bop b0 b1)) b1 → ⊥
  bad5662  p = false≢true (cong lower p)
  cut5662 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (op (var 2) (var 1)))) (op (var 1) (var 2))) , (var 2)) → ⊥
  cut5662  adequate = bad5662  (Adequate.valid adequate Two boolean env1)
  bad5663 : PathP (λ _ → Two) (bop (bop b0 (bop b0 (bop b0 b0))) (bop b0 b0)) b1 → ⊥
  bad5663  p = false≢true (cong lower p)
  cut5663 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (op (var 2) (var 1)))) (op (var 1) (var 2))) , (var 3)) → ⊥
  cut5663  adequate = bad5663  (Adequate.valid adequate Two boolean env5)
  bad5664 : PathP (λ _ → Two) (bop (bop b0 (bop b1 (bop b0 b1))) (bop b1 b1)) b0 → ⊥
  bad5664  p = false≢true (sym (cong lower p))
  cut5664 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (op (var 2) (var 1)))) (op (var 1) (var 3))) , (var 0)) → ⊥
  cut5664  adequate = bad5664  (Adequate.valid adequate Two boolean env13)
  bad5665 : PathP (λ _ → Two) (bop (bop b0 (bop b1 (bop b0 b1))) (bop b1 b0)) b1 → ⊥
  bad5665  p = false≢true (cong lower p)
  cut5665 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (op (var 2) (var 1)))) (op (var 1) (var 3))) , (var 1)) → ⊥
  cut5665  adequate = bad5665  (Adequate.valid adequate Two boolean env12)
  bad5666 : PathP (λ _ → Two) (bop (bop b0 (bop b0 (bop b1 b0))) (bop b0 b0)) b1 → ⊥
  bad5666  p = false≢true (cong lower p)
  cut5666 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (op (var 2) (var 1)))) (op (var 1) (var 3))) , (var 2)) → ⊥
  cut5666  adequate = bad5666  (Adequate.valid adequate Two boolean env9)
  bad5667 : PathP (λ _ → Two) (bop (bop b0 (bop b0 (bop b0 b0))) (bop b0 b1)) b1 → ⊥
  bad5667  p = false≢true (cong lower p)
  cut5667 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (op (var 2) (var 1)))) (op (var 1) (var 3))) , (var 3)) → ⊥
  cut5667  adequate = bad5667  (Adequate.valid adequate Two boolean env5)
  bad5668 : PathP (λ _ → Two) (bop (bop b0 (bop b0 (bop b0 b0))) (bop b0 b0)) b1 → ⊥
  bad5668  p = false≢true (cong lower p)
  cut5668 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (op (var 2) (var 1)))) (op (var 1) (var 3))) , (var 4)) → ⊥
  cut5668  adequate = bad5668  (Adequate.valid adequate Two boolean env10)
  bad5669 : PathP (λ _ → Two) (bop (bop b1 (bop b1 (bop b0 b1))) (bop b0 b1)) b1 → ⊥
  bad5669  p = false≢true (cong lower p)
  cut5669 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (op (var 2) (var 1)))) (op (var 2) (var 0))) , (var 0)) → ⊥
  cut5669  adequate = bad5669  (Adequate.valid adequate Two boolean env7)
  bad5670 : PathP (λ _ → Two) (bop (bop b0 (bop b1 (bop b0 b1))) (bop b0 b0)) b1 → ⊥
  bad5670  p = false≢true (cong lower p)
  cut5670 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (op (var 2) (var 1)))) (op (var 2) (var 0))) , (var 1)) → ⊥
  cut5670  adequate = bad5670  (Adequate.valid adequate Two boolean env4)
  bad5671 : PathP (λ _ → Two) (bop (bop b0 (bop b0 (bop b1 b0))) (bop b1 b0)) b1 → ⊥
  bad5671  p = false≢true (cong lower p)
  cut5671 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (op (var 2) (var 1)))) (op (var 2) (var 0))) , (var 2)) → ⊥
  cut5671  adequate = bad5671  (Adequate.valid adequate Two boolean env1)
  bad5672 : PathP (λ _ → Two) (bop (bop b0 (bop b0 (bop b0 b0))) (bop b0 b0)) b1 → ⊥
  bad5672  p = false≢true (cong lower p)
  cut5672 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (op (var 2) (var 1)))) (op (var 2) (var 0))) , (var 3)) → ⊥
  cut5672  adequate = bad5672  (Adequate.valid adequate Two boolean env5)
  bad5673 : PathP (λ _ → Two) (bop (bop b0 (bop b1 (bop b1 b1))) (bop b1 b1)) b0 → ⊥
  bad5673  p = false≢true (sym (cong lower p))
  cut5673 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (op (var 2) (var 1)))) (op (var 2) (var 1))) , (var 0)) → ⊥
  cut5673  adequate = bad5673  (Adequate.valid adequate Two boolean env3)
  bad5674 : PathP (λ _ → Two) (bop (bop b0 (bop b1 (bop b0 b1))) (bop b0 b1)) b1 → ⊥
  bad5674  p = false≢true (cong lower p)
  cut5674 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (op (var 2) (var 1)))) (op (var 2) (var 1))) , (var 1)) → ⊥
  cut5674  adequate = bad5674  (Adequate.valid adequate Two boolean env4)
  bad5675 : PathP (λ _ → Two) (bop (bop b0 (bop b0 (bop b1 b0))) (bop b1 b0)) b1 → ⊥
  bad5675  p = false≢true (cong lower p)
  cut5675 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (op (var 2) (var 1)))) (op (var 2) (var 1))) , (var 2)) → ⊥
  cut5675  adequate = bad5675  (Adequate.valid adequate Two boolean env1)
  bad5676 : PathP (λ _ → Two) (bop (bop b0 (bop b0 (bop b0 b0))) (bop b0 b0)) b1 → ⊥
  bad5676  p = false≢true (cong lower p)
  cut5676 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (op (var 2) (var 1)))) (op (var 2) (var 1))) , (var 3)) → ⊥
  cut5676  adequate = bad5676  (Adequate.valid adequate Two boolean env5)
  bad5677 : PathP (λ _ → Two) (bop (bop b0 (bop b0 (bop b1 b0))) (bop b1 b1)) b0 → ⊥
  bad5677  p = false≢true (sym (cong lower p))
  cut5677 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (op (var 2) (var 1)))) (op (var 2) (var 2))) , (var 0)) → ⊥
  cut5677  adequate = bad5677  (Adequate.valid adequate Two boolean env1)
  bad5678 : PathP (λ _ → Two) (bop (bop b0 (bop b0 (bop b1 b0))) (bop b1 b1)) b0 → ⊥
  bad5678  p = false≢true (sym (cong lower p))
  cut5678 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (op (var 2) (var 1)))) (op (var 2) (var 2))) , (var 1)) → ⊥
  cut5678  adequate = bad5678  (Adequate.valid adequate Two boolean env1)
  bad5679 : PathP (λ _ → Two) (bop (bop b1 (bop b0 (bop b0 b0))) (bop b0 b0)) b0 → ⊥
  bad5679  p = false≢true (sym (cong lower p))
  cut5679 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (op (var 2) (var 1)))) (op (var 2) (var 2))) , (var 2)) → ⊥
  cut5679  adequate = bad5679  (Adequate.valid adequate Two boolean env6)
  bad5680 : PathP (λ _ → Two) (bop (bop b0 (bop b0 (bop b0 b0))) (bop b0 b0)) b1 → ⊥
  bad5680  p = false≢true (cong lower p)
  cut5680 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (op (var 2) (var 1)))) (op (var 2) (var 2))) , (var 3)) → ⊥
  cut5680  adequate = bad5680  (Adequate.valid adequate Two boolean env5)
  bad5681 : PathP (λ _ → Two) (bop (bop b0 (bop b0 (bop b1 b0))) (bop b1 b1)) b0 → ⊥
  bad5681  p = false≢true (sym (cong lower p))
  cut5681 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (op (var 2) (var 1)))) (op (var 2) (var 3))) , (var 0)) → ⊥
  cut5681  adequate = bad5681  (Adequate.valid adequate Two boolean env8)
  bad5682 : PathP (λ _ → Two) (bop (bop b0 (bop b0 (bop b1 b0))) (bop b1 b1)) b0 → ⊥
  bad5682  p = false≢true (sym (cong lower p))
  cut5682 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (op (var 2) (var 1)))) (op (var 2) (var 3))) , (var 1)) → ⊥
  cut5682  adequate = bad5682  (Adequate.valid adequate Two boolean env8)
  bad5683 : PathP (λ _ → Two) (bop (bop b0 (bop b0 (bop b1 b0))) (bop b1 b0)) b1 → ⊥
  bad5683  p = false≢true (cong lower p)
  cut5683 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (op (var 2) (var 1)))) (op (var 2) (var 3))) , (var 2)) → ⊥
  cut5683  adequate = bad5683  (Adequate.valid adequate Two boolean env9)
  bad5684 : PathP (λ _ → Two) (bop (bop b0 (bop b0 (bop b0 b0))) (bop b0 b1)) b1 → ⊥
  bad5684  p = false≢true (cong lower p)
  cut5684 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (op (var 2) (var 1)))) (op (var 2) (var 3))) , (var 3)) → ⊥
  cut5684  adequate = bad5684  (Adequate.valid adequate Two boolean env5)
  bad5685 : PathP (λ _ → Two) (bop (bop b0 (bop b0 (bop b0 b0))) (bop b0 b0)) b1 → ⊥
  bad5685  p = false≢true (cong lower p)
  cut5685 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (op (var 2) (var 1)))) (op (var 2) (var 3))) , (var 4)) → ⊥
  cut5685  adequate = bad5685  (Adequate.valid adequate Two boolean env10)
  bad5686 : PathP (λ _ → Two) (bop (bop b1 (bop b1 (bop b0 b1))) (bop b0 b1)) b1 → ⊥
  bad5686  p = false≢true (cong lower p)
  cut5686 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (op (var 2) (var 1)))) (op (var 3) (var 0))) , (var 0)) → ⊥
  cut5686  adequate = bad5686  (Adequate.valid adequate Two boolean env18)
  bad5687 : PathP (λ _ → Two) (bop (bop b0 (bop b1 (bop b0 b1))) (bop b0 b0)) b1 → ⊥
  bad5687  p = false≢true (cong lower p)
  cut5687 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (op (var 2) (var 1)))) (op (var 3) (var 0))) , (var 1)) → ⊥
  cut5687  adequate = bad5687  (Adequate.valid adequate Two boolean env12)
  bad5688 : PathP (λ _ → Two) (bop (bop b0 (bop b0 (bop b1 b0))) (bop b0 b0)) b1 → ⊥
  bad5688  p = false≢true (cong lower p)
  cut5688 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (op (var 2) (var 1)))) (op (var 3) (var 0))) , (var 2)) → ⊥
  cut5688  adequate = bad5688  (Adequate.valid adequate Two boolean env9)
  bad5689 : PathP (λ _ → Two) (bop (bop b0 (bop b0 (bop b0 b0))) (bop b1 b0)) b1 → ⊥
  bad5689  p = false≢true (cong lower p)
  cut5689 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (op (var 2) (var 1)))) (op (var 3) (var 0))) , (var 3)) → ⊥
  cut5689  adequate = bad5689  (Adequate.valid adequate Two boolean env5)
  bad5690 : PathP (λ _ → Two) (bop (bop b0 (bop b0 (bop b0 b0))) (bop b0 b0)) b1 → ⊥
  bad5690  p = false≢true (cong lower p)
  cut5690 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (op (var 2) (var 1)))) (op (var 3) (var 0))) , (var 4)) → ⊥
  cut5690  adequate = bad5690  (Adequate.valid adequate Two boolean env10)
  bad5691 : PathP (λ _ → Two) (bop (bop b0 (bop b1 (bop b0 b1))) (bop b1 b1)) b0 → ⊥
  bad5691  p = false≢true (sym (cong lower p))
  cut5691 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (op (var 2) (var 1)))) (op (var 3) (var 1))) , (var 0)) → ⊥
  cut5691  adequate = bad5691  (Adequate.valid adequate Two boolean env13)
  bad5692 : PathP (λ _ → Two) (bop (bop b0 (bop b1 (bop b0 b1))) (bop b0 b1)) b1 → ⊥
  bad5692  p = false≢true (cong lower p)
  cut5692 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (op (var 2) (var 1)))) (op (var 3) (var 1))) , (var 1)) → ⊥
  cut5692  adequate = bad5692  (Adequate.valid adequate Two boolean env12)
  bad5693 : PathP (λ _ → Two) (bop (bop b0 (bop b0 (bop b1 b0))) (bop b0 b0)) b1 → ⊥
  bad5693  p = false≢true (cong lower p)
  cut5693 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (op (var 2) (var 1)))) (op (var 3) (var 1))) , (var 2)) → ⊥
  cut5693  adequate = bad5693  (Adequate.valid adequate Two boolean env9)
  bad5694 : PathP (λ _ → Two) (bop (bop b0 (bop b0 (bop b0 b0))) (bop b1 b0)) b1 → ⊥
  bad5694  p = false≢true (cong lower p)
  cut5694 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (op (var 2) (var 1)))) (op (var 3) (var 1))) , (var 3)) → ⊥
  cut5694  adequate = bad5694  (Adequate.valid adequate Two boolean env5)
  bad5695 : PathP (λ _ → Two) (bop (bop b0 (bop b0 (bop b0 b0))) (bop b0 b0)) b1 → ⊥
  bad5695  p = false≢true (cong lower p)
  cut5695 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (op (var 2) (var 1)))) (op (var 3) (var 1))) , (var 4)) → ⊥
  cut5695  adequate = bad5695  (Adequate.valid adequate Two boolean env10)
  bad5696 : PathP (λ _ → Two) (bop (bop b0 (bop b0 (bop b1 b0))) (bop b1 b1)) b0 → ⊥
  bad5696  p = false≢true (sym (cong lower p))
  cut5696 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (op (var 2) (var 1)))) (op (var 3) (var 2))) , (var 0)) → ⊥
  cut5696  adequate = bad5696  (Adequate.valid adequate Two boolean env8)
  bad5697 : PathP (λ _ → Two) (bop (bop b0 (bop b0 (bop b1 b0))) (bop b1 b1)) b0 → ⊥
  bad5697  p = false≢true (sym (cong lower p))
  cut5697 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (op (var 2) (var 1)))) (op (var 3) (var 2))) , (var 1)) → ⊥
  cut5697  adequate = bad5697  (Adequate.valid adequate Two boolean env8)
  bad5698 : PathP (λ _ → Two) (bop (bop b0 (bop b0 (bop b1 b0))) (bop b0 b1)) b1 → ⊥
  bad5698  p = false≢true (cong lower p)
  cut5698 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (op (var 2) (var 1)))) (op (var 3) (var 2))) , (var 2)) → ⊥
  cut5698  adequate = bad5698  (Adequate.valid adequate Two boolean env9)
  bad5699 : PathP (λ _ → Two) (bop (bop b0 (bop b0 (bop b0 b0))) (bop b1 b0)) b1 → ⊥
  bad5699  p = false≢true (cong lower p)
  cut5699 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (op (var 2) (var 1)))) (op (var 3) (var 2))) , (var 3)) → ⊥
  cut5699  adequate = bad5699  (Adequate.valid adequate Two boolean env5)
  bad5700 : PathP (λ _ → Two) (bop (bop b0 (bop b0 (bop b0 b0))) (bop b0 b0)) b1 → ⊥
  bad5700  p = false≢true (cong lower p)
  cut5700 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (op (var 2) (var 1)))) (op (var 3) (var 2))) , (var 4)) → ⊥
  cut5700  adequate = bad5700  (Adequate.valid adequate Two boolean env10)
  bad5701 : PathP (λ _ → Two) (bop (bop b0 (bop b0 (bop b0 b0))) (bop b1 b1)) b0 → ⊥
  bad5701  p = false≢true (sym (cong lower p))
  cut5701 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (op (var 2) (var 1)))) (op (var 3) (var 3))) , (var 0)) → ⊥
  cut5701  adequate = bad5701  (Adequate.valid adequate Two boolean env5)
  bad5702 : PathP (λ _ → Two) (bop (bop b0 (bop b0 (bop b0 b0))) (bop b1 b1)) b0 → ⊥
  bad5702  p = false≢true (sym (cong lower p))
  cut5702 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (op (var 2) (var 1)))) (op (var 3) (var 3))) , (var 1)) → ⊥
  cut5702  adequate = bad5702  (Adequate.valid adequate Two boolean env5)
  bad5703 : PathP (λ _ → Two) (bop (bop b0 (bop b0 (bop b0 b0))) (bop b1 b1)) b0 → ⊥
  bad5703  p = false≢true (sym (cong lower p))
  cut5703 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (op (var 2) (var 1)))) (op (var 3) (var 3))) , (var 2)) → ⊥
  cut5703  adequate = bad5703  (Adequate.valid adequate Two boolean env5)
  bad5704 : PathP (λ _ → Two) (bop (bop b1 (bop b0 (bop b0 b0))) (bop b0 b0)) b0 → ⊥
  bad5704  p = false≢true (sym (cong lower p))
  cut5704 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (op (var 2) (var 1)))) (op (var 3) (var 3))) , (var 3)) → ⊥
  cut5704  adequate = bad5704  (Adequate.valid adequate Two boolean env11)
  bad5705 : PathP (λ _ → Two) (bop (bop b0 (bop b0 (bop b0 b0))) (bop b0 b0)) b1 → ⊥
  bad5705  p = false≢true (cong lower p)
  cut5705 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (op (var 2) (var 1)))) (op (var 3) (var 3))) , (var 4)) → ⊥
  cut5705  adequate = bad5705  (Adequate.valid adequate Two boolean env10)
  bad5706 : PathP (λ _ → Two) (bop (bop b0 (bop b0 (bop b0 b0))) (bop b1 b1)) b0 → ⊥
  bad5706  p = false≢true (sym (cong lower p))
  cut5706 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (op (var 2) (var 1)))) (op (var 3) (var 4))) , (var 0)) → ⊥
  cut5706  adequate = bad5706  (Adequate.valid adequate Two boolean env15)
  bad5707 : PathP (λ _ → Two) (bop (bop b0 (bop b0 (bop b0 b0))) (bop b1 b1)) b0 → ⊥
  bad5707  p = false≢true (sym (cong lower p))
  cut5707 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (op (var 2) (var 1)))) (op (var 3) (var 4))) , (var 1)) → ⊥
  cut5707  adequate = bad5707  (Adequate.valid adequate Two boolean env15)
  bad5708 : PathP (λ _ → Two) (bop (bop b0 (bop b0 (bop b0 b0))) (bop b1 b1)) b0 → ⊥
  bad5708  p = false≢true (sym (cong lower p))
  cut5708 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (op (var 2) (var 1)))) (op (var 3) (var 4))) , (var 2)) → ⊥
  cut5708  adequate = bad5708  (Adequate.valid adequate Two boolean env15)
  bad5709 : PathP (λ _ → Two) (bop (bop b0 (bop b0 (bop b0 b0))) (bop b1 b0)) b1 → ⊥
  bad5709  p = false≢true (cong lower p)
  cut5709 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (op (var 2) (var 1)))) (op (var 3) (var 4))) , (var 3)) → ⊥
  cut5709  adequate = bad5709  (Adequate.valid adequate Two boolean env16)
  bad5710 : PathP (λ _ → Two) (bop (bop b0 (bop b0 (bop b0 b0))) (bop b0 b1)) b1 → ⊥
  bad5710  p = false≢true (cong lower p)
  cut5710 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (op (var 2) (var 1)))) (op (var 3) (var 4))) , (var 4)) → ⊥
  cut5710  adequate = bad5710  (Adequate.valid adequate Two boolean env10)
  bad5711 : PathP (λ _ → Two) (bop (bop b0 (bop b0 (bop b0 b0))) (bop b0 b0)) b1 → ⊥
  bad5711  p = false≢true (cong lower p)
  cut5711 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (op (var 2) (var 1)))) (op (var 3) (var 4))) , (var 5)) → ⊥
  cut5711  adequate = bad5711  (Adequate.valid adequate Two boolean env17)
  holds5712 : (z0 z1 z2 : A2) → (mul2 (mul2 z0 (mul2 z1 (mul2 z2 z2))) (mul2 z0 z0)) ≡ z0
  holds5712 z0 z1 z2 = refl
  cut5712 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (op (var 2) (var 2)))) (op (var 0) (var 0))) , (var 0)) → ⊥
  cut5712  = reject2 ((op (op (var 0) (op (var 1) (op (var 2) (var 2)))) (op (var 0) (var 0))) , (var 0)) (λ env → holds5712 (env 0) (env 1) (env 2))
  bad5713 : PathP (λ _ → Two) (bop (bop b0 (bop b1 (bop b0 b0))) (bop b0 b0)) b1 → ⊥
  bad5713  p = false≢true (cong lower p)
  cut5713 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (op (var 2) (var 2)))) (op (var 0) (var 0))) , (var 1)) → ⊥
  cut5713  adequate = bad5713  (Adequate.valid adequate Two boolean env4)
  bad5714 : PathP (λ _ → Two) (bop (bop b0 (bop b0 (bop b1 b1))) (bop b0 b0)) b1 → ⊥
  bad5714  p = false≢true (cong lower p)
  cut5714 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (op (var 2) (var 2)))) (op (var 0) (var 0))) , (var 2)) → ⊥
  cut5714  adequate = bad5714  (Adequate.valid adequate Two boolean env1)
  bad5715 : PathP (λ _ → Two) (bop (bop b0 (bop b0 (bop b0 b0))) (bop b0 b0)) b1 → ⊥
  bad5715  p = false≢true (cong lower p)
  cut5715 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (op (var 2) (var 2)))) (op (var 0) (var 0))) , (var 3)) → ⊥
  cut5715  adequate = bad5715  (Adequate.valid adequate Two boolean env5)
  holds5716 : (z0 z1 z2 : A2) → (mul2 (mul2 z0 (mul2 z1 (mul2 z2 z2))) (mul2 z0 z1)) ≡ z0
  holds5716 z0 z1 z2 = refl
  cut5716 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (op (var 2) (var 2)))) (op (var 0) (var 1))) , (var 0)) → ⊥
  cut5716  = reject2 ((op (op (var 0) (op (var 1) (op (var 2) (var 2)))) (op (var 0) (var 1))) , (var 0)) (λ env → holds5716 (env 0) (env 1) (env 2))
  bad5717 : PathP (λ _ → Two) (bop (bop b0 (bop b1 (bop b0 b0))) (bop b0 b1)) b1 → ⊥
  bad5717  p = false≢true (cong lower p)
  cut5717 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (op (var 2) (var 2)))) (op (var 0) (var 1))) , (var 1)) → ⊥
  cut5717  adequate = bad5717  (Adequate.valid adequate Two boolean env4)
  bad5718 : PathP (λ _ → Two) (bop (bop b0 (bop b0 (bop b1 b1))) (bop b0 b0)) b1 → ⊥
  bad5718  p = false≢true (cong lower p)
  cut5718 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (op (var 2) (var 2)))) (op (var 0) (var 1))) , (var 2)) → ⊥
  cut5718  adequate = bad5718  (Adequate.valid adequate Two boolean env1)
  bad5719 : PathP (λ _ → Two) (bop (bop b0 (bop b0 (bop b0 b0))) (bop b0 b0)) b1 → ⊥
  bad5719  p = false≢true (cong lower p)
  cut5719 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (op (var 2) (var 2)))) (op (var 0) (var 1))) , (var 3)) → ⊥
  cut5719  adequate = bad5719  (Adequate.valid adequate Two boolean env5)
  bad5720 : PathP (λ _ → Two) (bop (bop b1 (bop b1 (bop b0 b0))) (bop b1 b0)) b1 → ⊥
  bad5720  p = false≢true (cong lower p)
  cut5720 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (op (var 2) (var 2)))) (op (var 0) (var 2))) , (var 0)) → ⊥
  cut5720  adequate = bad5720  (Adequate.valid adequate Two boolean env7)
  bad5721 : PathP (λ _ → Two) (bop (bop b0 (bop b1 (bop b0 b0))) (bop b0 b0)) b1 → ⊥
  bad5721  p = false≢true (cong lower p)
  cut5721 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (op (var 2) (var 2)))) (op (var 0) (var 2))) , (var 1)) → ⊥
  cut5721  adequate = bad5721  (Adequate.valid adequate Two boolean env4)
  bad5722 : PathP (λ _ → Two) (bop (bop b0 (bop b0 (bop b1 b1))) (bop b0 b1)) b1 → ⊥
  bad5722  p = false≢true (cong lower p)
  cut5722 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (op (var 2) (var 2)))) (op (var 0) (var 2))) , (var 2)) → ⊥
  cut5722  adequate = bad5722  (Adequate.valid adequate Two boolean env1)
  bad5723 : PathP (λ _ → Two) (bop (bop b0 (bop b0 (bop b0 b0))) (bop b0 b0)) b1 → ⊥
  bad5723  p = false≢true (cong lower p)
  cut5723 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (op (var 2) (var 2)))) (op (var 0) (var 2))) , (var 3)) → ⊥
  cut5723  adequate = bad5723  (Adequate.valid adequate Two boolean env5)
  bad5724 : PathP (λ _ → Two) (bop (bop b1 (bop b1 (bop b0 b0))) (bop b1 b0)) b1 → ⊥
  bad5724  p = false≢true (cong lower p)
  cut5724 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (op (var 2) (var 2)))) (op (var 0) (var 3))) , (var 0)) → ⊥
  cut5724  adequate = bad5724  (Adequate.valid adequate Two boolean env18)
  bad5725 : PathP (λ _ → Two) (bop (bop b0 (bop b1 (bop b0 b0))) (bop b0 b0)) b1 → ⊥
  bad5725  p = false≢true (cong lower p)
  cut5725 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (op (var 2) (var 2)))) (op (var 0) (var 3))) , (var 1)) → ⊥
  cut5725  adequate = bad5725  (Adequate.valid adequate Two boolean env12)
  bad5726 : PathP (λ _ → Two) (bop (bop b0 (bop b0 (bop b1 b1))) (bop b0 b0)) b1 → ⊥
  bad5726  p = false≢true (cong lower p)
  cut5726 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (op (var 2) (var 2)))) (op (var 0) (var 3))) , (var 2)) → ⊥
  cut5726  adequate = bad5726  (Adequate.valid adequate Two boolean env9)
  bad5727 : PathP (λ _ → Two) (bop (bop b0 (bop b0 (bop b0 b0))) (bop b0 b1)) b1 → ⊥
  bad5727  p = false≢true (cong lower p)
  cut5727 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (op (var 2) (var 2)))) (op (var 0) (var 3))) , (var 3)) → ⊥
  cut5727  adequate = bad5727  (Adequate.valid adequate Two boolean env5)
  bad5728 : PathP (λ _ → Two) (bop (bop b0 (bop b0 (bop b0 b0))) (bop b0 b0)) b1 → ⊥
  bad5728  p = false≢true (cong lower p)
  cut5728 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (op (var 2) (var 2)))) (op (var 0) (var 3))) , (var 4)) → ⊥
  cut5728  adequate = bad5728  (Adequate.valid adequate Two boolean env10)
  holds5729 : (z0 z1 z2 : A2) → (mul2 (mul2 z0 (mul2 z1 (mul2 z2 z2))) (mul2 z1 z0)) ≡ z0
  holds5729 z0 z1 z2 = refl
  cut5729 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (op (var 2) (var 2)))) (op (var 1) (var 0))) , (var 0)) → ⊥
  cut5729  = reject2 ((op (op (var 0) (op (var 1) (op (var 2) (var 2)))) (op (var 1) (var 0))) , (var 0)) (λ env → holds5729 (env 0) (env 1) (env 2))
  bad5730 : PathP (λ _ → Two) (bop (bop b0 (bop b1 (bop b0 b0))) (bop b1 b0)) b1 → ⊥
  bad5730  p = false≢true (cong lower p)
  cut5730 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (op (var 2) (var 2)))) (op (var 1) (var 0))) , (var 1)) → ⊥
  cut5730  adequate = bad5730  (Adequate.valid adequate Two boolean env4)
  bad5731 : PathP (λ _ → Two) (bop (bop b0 (bop b0 (bop b1 b1))) (bop b0 b0)) b1 → ⊥
  bad5731  p = false≢true (cong lower p)
  cut5731 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (op (var 2) (var 2)))) (op (var 1) (var 0))) , (var 2)) → ⊥
  cut5731  adequate = bad5731  (Adequate.valid adequate Two boolean env1)
  bad5732 : PathP (λ _ → Two) (bop (bop b0 (bop b0 (bop b0 b0))) (bop b0 b0)) b1 → ⊥
  bad5732  p = false≢true (cong lower p)
  cut5732 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (op (var 2) (var 2)))) (op (var 1) (var 0))) , (var 3)) → ⊥
  cut5732  adequate = bad5732  (Adequate.valid adequate Two boolean env5)
  bad5733 : PathP (λ _ → Two) (bop (bop b0 (bop b1 (bop b0 b0))) (bop b1 b1)) b0 → ⊥
  bad5733  p = false≢true (sym (cong lower p))
  cut5733 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (op (var 2) (var 2)))) (op (var 1) (var 1))) , (var 0)) → ⊥
  cut5733  adequate = bad5733  (Adequate.valid adequate Two boolean env4)
  bad5734 : PathP (λ _ → Two) (bop (bop b1 (bop b0 (bop b0 b0))) (bop b0 b0)) b0 → ⊥
  bad5734  p = false≢true (sym (cong lower p))
  cut5734 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (op (var 2) (var 2)))) (op (var 1) (var 1))) , (var 1)) → ⊥
  cut5734  adequate = bad5734  (Adequate.valid adequate Two boolean env6)
  bad5735 : PathP (λ _ → Two) (bop (bop b0 (bop b0 (bop b1 b1))) (bop b0 b0)) b1 → ⊥
  bad5735  p = false≢true (cong lower p)
  cut5735 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (op (var 2) (var 2)))) (op (var 1) (var 1))) , (var 2)) → ⊥
  cut5735  adequate = bad5735  (Adequate.valid adequate Two boolean env1)
  bad5736 : PathP (λ _ → Two) (bop (bop b0 (bop b0 (bop b0 b0))) (bop b0 b0)) b1 → ⊥
  bad5736  p = false≢true (cong lower p)
  cut5736 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (op (var 2) (var 2)))) (op (var 1) (var 1))) , (var 3)) → ⊥
  cut5736  adequate = bad5736  (Adequate.valid adequate Two boolean env5)
  bad5737 : PathP (λ _ → Two) (bop (bop b0 (bop b1 (bop b1 b1))) (bop b1 b1)) b0 → ⊥
  bad5737  p = false≢true (sym (cong lower p))
  cut5737 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (op (var 2) (var 2)))) (op (var 1) (var 2))) , (var 0)) → ⊥
  cut5737  adequate = bad5737  (Adequate.valid adequate Two boolean env3)
  bad5738 : PathP (λ _ → Two) (bop (bop b0 (bop b1 (bop b0 b0))) (bop b1 b0)) b1 → ⊥
  bad5738  p = false≢true (cong lower p)
  cut5738 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (op (var 2) (var 2)))) (op (var 1) (var 2))) , (var 1)) → ⊥
  cut5738  adequate = bad5738  (Adequate.valid adequate Two boolean env4)
  bad5739 : PathP (λ _ → Two) (bop (bop b0 (bop b0 (bop b1 b1))) (bop b0 b1)) b1 → ⊥
  bad5739  p = false≢true (cong lower p)
  cut5739 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (op (var 2) (var 2)))) (op (var 1) (var 2))) , (var 2)) → ⊥
  cut5739  adequate = bad5739  (Adequate.valid adequate Two boolean env1)
  bad5740 : PathP (λ _ → Two) (bop (bop b0 (bop b0 (bop b0 b0))) (bop b0 b0)) b1 → ⊥
  bad5740  p = false≢true (cong lower p)
  cut5740 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (op (var 2) (var 2)))) (op (var 1) (var 2))) , (var 3)) → ⊥
  cut5740  adequate = bad5740  (Adequate.valid adequate Two boolean env5)
  bad5741 : PathP (λ _ → Two) (bop (bop b0 (bop b1 (bop b0 b0))) (bop b1 b1)) b0 → ⊥
  bad5741  p = false≢true (sym (cong lower p))
  cut5741 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (op (var 2) (var 2)))) (op (var 1) (var 3))) , (var 0)) → ⊥
  cut5741  adequate = bad5741  (Adequate.valid adequate Two boolean env13)
  bad5742 : PathP (λ _ → Two) (bop (bop b0 (bop b1 (bop b0 b0))) (bop b1 b0)) b1 → ⊥
  bad5742  p = false≢true (cong lower p)
  cut5742 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (op (var 2) (var 2)))) (op (var 1) (var 3))) , (var 1)) → ⊥
  cut5742  adequate = bad5742  (Adequate.valid adequate Two boolean env12)
  bad5743 : PathP (λ _ → Two) (bop (bop b0 (bop b0 (bop b1 b1))) (bop b0 b0)) b1 → ⊥
  bad5743  p = false≢true (cong lower p)
  cut5743 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (op (var 2) (var 2)))) (op (var 1) (var 3))) , (var 2)) → ⊥
  cut5743  adequate = bad5743  (Adequate.valid adequate Two boolean env9)
  bad5744 : PathP (λ _ → Two) (bop (bop b0 (bop b0 (bop b0 b0))) (bop b0 b1)) b1 → ⊥
  bad5744  p = false≢true (cong lower p)
  cut5744 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (op (var 2) (var 2)))) (op (var 1) (var 3))) , (var 3)) → ⊥
  cut5744  adequate = bad5744  (Adequate.valid adequate Two boolean env5)
  bad5745 : PathP (λ _ → Two) (bop (bop b0 (bop b0 (bop b0 b0))) (bop b0 b0)) b1 → ⊥
  bad5745  p = false≢true (cong lower p)
  cut5745 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (op (var 2) (var 2)))) (op (var 1) (var 3))) , (var 4)) → ⊥
  cut5745  adequate = bad5745  (Adequate.valid adequate Two boolean env10)
  bad5746 : PathP (λ _ → Two) (bop (bop b1 (bop b1 (bop b0 b0))) (bop b0 b1)) b1 → ⊥
  bad5746  p = false≢true (cong lower p)
  cut5746 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (op (var 2) (var 2)))) (op (var 2) (var 0))) , (var 0)) → ⊥
  cut5746  adequate = bad5746  (Adequate.valid adequate Two boolean env7)
  bad5747 : PathP (λ _ → Two) (bop (bop b0 (bop b1 (bop b0 b0))) (bop b0 b0)) b1 → ⊥
  bad5747  p = false≢true (cong lower p)
  cut5747 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (op (var 2) (var 2)))) (op (var 2) (var 0))) , (var 1)) → ⊥
  cut5747  adequate = bad5747  (Adequate.valid adequate Two boolean env4)
  bad5748 : PathP (λ _ → Two) (bop (bop b0 (bop b0 (bop b1 b1))) (bop b1 b0)) b1 → ⊥
  bad5748  p = false≢true (cong lower p)
  cut5748 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (op (var 2) (var 2)))) (op (var 2) (var 0))) , (var 2)) → ⊥
  cut5748  adequate = bad5748  (Adequate.valid adequate Two boolean env1)
  bad5749 : PathP (λ _ → Two) (bop (bop b0 (bop b0 (bop b0 b0))) (bop b0 b0)) b1 → ⊥
  bad5749  p = false≢true (cong lower p)
  cut5749 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (op (var 2) (var 2)))) (op (var 2) (var 0))) , (var 3)) → ⊥
  cut5749  adequate = bad5749  (Adequate.valid adequate Two boolean env5)
  bad5750 : PathP (λ _ → Two) (bop (bop b0 (bop b1 (bop b1 b1))) (bop b1 b1)) b0 → ⊥
  bad5750  p = false≢true (sym (cong lower p))
  cut5750 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (op (var 2) (var 2)))) (op (var 2) (var 1))) , (var 0)) → ⊥
  cut5750  adequate = bad5750  (Adequate.valid adequate Two boolean env3)
  bad5751 : PathP (λ _ → Two) (bop (bop b0 (bop b1 (bop b0 b0))) (bop b0 b1)) b1 → ⊥
  bad5751  p = false≢true (cong lower p)
  cut5751 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (op (var 2) (var 2)))) (op (var 2) (var 1))) , (var 1)) → ⊥
  cut5751  adequate = bad5751  (Adequate.valid adequate Two boolean env4)
  bad5752 : PathP (λ _ → Two) (bop (bop b0 (bop b0 (bop b1 b1))) (bop b1 b0)) b1 → ⊥
  bad5752  p = false≢true (cong lower p)
  cut5752 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (op (var 2) (var 2)))) (op (var 2) (var 1))) , (var 2)) → ⊥
  cut5752  adequate = bad5752  (Adequate.valid adequate Two boolean env1)
  bad5753 : PathP (λ _ → Two) (bop (bop b0 (bop b0 (bop b0 b0))) (bop b0 b0)) b1 → ⊥
  bad5753  p = false≢true (cong lower p)
  cut5753 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (op (var 2) (var 2)))) (op (var 2) (var 1))) , (var 3)) → ⊥
  cut5753  adequate = bad5753  (Adequate.valid adequate Two boolean env5)
  bad5754 : PathP (λ _ → Two) (bop (bop b0 (bop b0 (bop b1 b1))) (bop b1 b1)) b0 → ⊥
  bad5754  p = false≢true (sym (cong lower p))
  cut5754 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (op (var 2) (var 2)))) (op (var 2) (var 2))) , (var 0)) → ⊥
  cut5754  adequate = bad5754  (Adequate.valid adequate Two boolean env1)
  bad5755 : PathP (λ _ → Two) (bop (bop b0 (bop b0 (bop b1 b1))) (bop b1 b1)) b0 → ⊥
  bad5755  p = false≢true (sym (cong lower p))
  cut5755 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (op (var 2) (var 2)))) (op (var 2) (var 2))) , (var 1)) → ⊥
  cut5755  adequate = bad5755  (Adequate.valid adequate Two boolean env1)
  bad5756 : PathP (λ _ → Two) (bop (bop b1 (bop b0 (bop b0 b0))) (bop b0 b0)) b0 → ⊥
  bad5756  p = false≢true (sym (cong lower p))
  cut5756 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (op (var 2) (var 2)))) (op (var 2) (var 2))) , (var 2)) → ⊥
  cut5756  adequate = bad5756  (Adequate.valid adequate Two boolean env6)
  bad5757 : PathP (λ _ → Two) (bop (bop b0 (bop b0 (bop b0 b0))) (bop b0 b0)) b1 → ⊥
  bad5757  p = false≢true (cong lower p)
  cut5757 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (op (var 2) (var 2)))) (op (var 2) (var 2))) , (var 3)) → ⊥
  cut5757  adequate = bad5757  (Adequate.valid adequate Two boolean env5)
  bad5758 : PathP (λ _ → Two) (bop (bop b0 (bop b0 (bop b1 b1))) (bop b1 b1)) b0 → ⊥
  bad5758  p = false≢true (sym (cong lower p))
  cut5758 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (op (var 2) (var 2)))) (op (var 2) (var 3))) , (var 0)) → ⊥
  cut5758  adequate = bad5758  (Adequate.valid adequate Two boolean env8)
  bad5759 : PathP (λ _ → Two) (bop (bop b0 (bop b0 (bop b1 b1))) (bop b1 b1)) b0 → ⊥
  bad5759  p = false≢true (sym (cong lower p))
  cut5759 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (op (var 2) (var 2)))) (op (var 2) (var 3))) , (var 1)) → ⊥
  cut5759  adequate = bad5759  (Adequate.valid adequate Two boolean env8)
  bad5760 : PathP (λ _ → Two) (bop (bop b0 (bop b0 (bop b1 b1))) (bop b1 b0)) b1 → ⊥
  bad5760  p = false≢true (cong lower p)
  cut5760 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (op (var 2) (var 2)))) (op (var 2) (var 3))) , (var 2)) → ⊥
  cut5760  adequate = bad5760  (Adequate.valid adequate Two boolean env9)
  bad5761 : PathP (λ _ → Two) (bop (bop b0 (bop b0 (bop b0 b0))) (bop b0 b1)) b1 → ⊥
  bad5761  p = false≢true (cong lower p)
  cut5761 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (op (var 2) (var 2)))) (op (var 2) (var 3))) , (var 3)) → ⊥
  cut5761  adequate = bad5761  (Adequate.valid adequate Two boolean env5)
  bad5762 : PathP (λ _ → Two) (bop (bop b0 (bop b0 (bop b0 b0))) (bop b0 b0)) b1 → ⊥
  bad5762  p = false≢true (cong lower p)
  cut5762 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (op (var 2) (var 2)))) (op (var 2) (var 3))) , (var 4)) → ⊥
  cut5762  adequate = bad5762  (Adequate.valid adequate Two boolean env10)
  bad5763 : PathP (λ _ → Two) (bop (bop b1 (bop b1 (bop b0 b0))) (bop b0 b1)) b1 → ⊥
  bad5763  p = false≢true (cong lower p)
  cut5763 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (op (var 2) (var 2)))) (op (var 3) (var 0))) , (var 0)) → ⊥
  cut5763  adequate = bad5763  (Adequate.valid adequate Two boolean env18)
  bad5764 : PathP (λ _ → Two) (bop (bop b0 (bop b1 (bop b0 b0))) (bop b0 b0)) b1 → ⊥
  bad5764  p = false≢true (cong lower p)
  cut5764 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (op (var 2) (var 2)))) (op (var 3) (var 0))) , (var 1)) → ⊥
  cut5764  adequate = bad5764  (Adequate.valid adequate Two boolean env12)
  bad5765 : PathP (λ _ → Two) (bop (bop b0 (bop b0 (bop b1 b1))) (bop b0 b0)) b1 → ⊥
  bad5765  p = false≢true (cong lower p)
  cut5765 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (op (var 2) (var 2)))) (op (var 3) (var 0))) , (var 2)) → ⊥
  cut5765  adequate = bad5765  (Adequate.valid adequate Two boolean env9)
  bad5766 : PathP (λ _ → Two) (bop (bop b0 (bop b0 (bop b0 b0))) (bop b1 b0)) b1 → ⊥
  bad5766  p = false≢true (cong lower p)
  cut5766 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (op (var 2) (var 2)))) (op (var 3) (var 0))) , (var 3)) → ⊥
  cut5766  adequate = bad5766  (Adequate.valid adequate Two boolean env5)
  bad5767 : PathP (λ _ → Two) (bop (bop b0 (bop b0 (bop b0 b0))) (bop b0 b0)) b1 → ⊥
  bad5767  p = false≢true (cong lower p)
  cut5767 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (op (var 2) (var 2)))) (op (var 3) (var 0))) , (var 4)) → ⊥
  cut5767  adequate = bad5767  (Adequate.valid adequate Two boolean env10)
  bad5768 : PathP (λ _ → Two) (bop (bop b0 (bop b1 (bop b0 b0))) (bop b1 b1)) b0 → ⊥
  bad5768  p = false≢true (sym (cong lower p))
  cut5768 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (op (var 2) (var 2)))) (op (var 3) (var 1))) , (var 0)) → ⊥
  cut5768  adequate = bad5768  (Adequate.valid adequate Two boolean env13)
  bad5769 : PathP (λ _ → Two) (bop (bop b0 (bop b1 (bop b0 b0))) (bop b0 b1)) b1 → ⊥
  bad5769  p = false≢true (cong lower p)
  cut5769 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (op (var 2) (var 2)))) (op (var 3) (var 1))) , (var 1)) → ⊥
  cut5769  adequate = bad5769  (Adequate.valid adequate Two boolean env12)
  bad5770 : PathP (λ _ → Two) (bop (bop b0 (bop b0 (bop b1 b1))) (bop b0 b0)) b1 → ⊥
  bad5770  p = false≢true (cong lower p)
  cut5770 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (op (var 2) (var 2)))) (op (var 3) (var 1))) , (var 2)) → ⊥
  cut5770  adequate = bad5770  (Adequate.valid adequate Two boolean env9)
  bad5771 : PathP (λ _ → Two) (bop (bop b0 (bop b0 (bop b0 b0))) (bop b1 b0)) b1 → ⊥
  bad5771  p = false≢true (cong lower p)
  cut5771 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (op (var 2) (var 2)))) (op (var 3) (var 1))) , (var 3)) → ⊥
  cut5771  adequate = bad5771  (Adequate.valid adequate Two boolean env5)
  bad5772 : PathP (λ _ → Two) (bop (bop b0 (bop b0 (bop b0 b0))) (bop b0 b0)) b1 → ⊥
  bad5772  p = false≢true (cong lower p)
  cut5772 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (op (var 2) (var 2)))) (op (var 3) (var 1))) , (var 4)) → ⊥
  cut5772  adequate = bad5772  (Adequate.valid adequate Two boolean env10)
  bad5773 : PathP (λ _ → Two) (bop (bop b0 (bop b0 (bop b1 b1))) (bop b1 b1)) b0 → ⊥
  bad5773  p = false≢true (sym (cong lower p))
  cut5773 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (op (var 2) (var 2)))) (op (var 3) (var 2))) , (var 0)) → ⊥
  cut5773  adequate = bad5773  (Adequate.valid adequate Two boolean env8)
  bad5774 : PathP (λ _ → Two) (bop (bop b0 (bop b0 (bop b1 b1))) (bop b1 b1)) b0 → ⊥
  bad5774  p = false≢true (sym (cong lower p))
  cut5774 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (op (var 2) (var 2)))) (op (var 3) (var 2))) , (var 1)) → ⊥
  cut5774  adequate = bad5774  (Adequate.valid adequate Two boolean env8)
  bad5775 : PathP (λ _ → Two) (bop (bop b0 (bop b0 (bop b1 b1))) (bop b0 b1)) b1 → ⊥
  bad5775  p = false≢true (cong lower p)
  cut5775 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (op (var 2) (var 2)))) (op (var 3) (var 2))) , (var 2)) → ⊥
  cut5775  adequate = bad5775  (Adequate.valid adequate Two boolean env9)
  bad5776 : PathP (λ _ → Two) (bop (bop b0 (bop b0 (bop b0 b0))) (bop b1 b0)) b1 → ⊥
  bad5776  p = false≢true (cong lower p)
  cut5776 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (op (var 2) (var 2)))) (op (var 3) (var 2))) , (var 3)) → ⊥
  cut5776  adequate = bad5776  (Adequate.valid adequate Two boolean env5)
  bad5777 : PathP (λ _ → Two) (bop (bop b0 (bop b0 (bop b0 b0))) (bop b0 b0)) b1 → ⊥
  bad5777  p = false≢true (cong lower p)
  cut5777 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (op (var 2) (var 2)))) (op (var 3) (var 2))) , (var 4)) → ⊥
  cut5777  adequate = bad5777  (Adequate.valid adequate Two boolean env10)
  bad5778 : PathP (λ _ → Two) (bop (bop b0 (bop b0 (bop b0 b0))) (bop b1 b1)) b0 → ⊥
  bad5778  p = false≢true (sym (cong lower p))
  cut5778 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (op (var 2) (var 2)))) (op (var 3) (var 3))) , (var 0)) → ⊥
  cut5778  adequate = bad5778  (Adequate.valid adequate Two boolean env5)
  bad5779 : PathP (λ _ → Two) (bop (bop b0 (bop b0 (bop b0 b0))) (bop b1 b1)) b0 → ⊥
  bad5779  p = false≢true (sym (cong lower p))
  cut5779 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (op (var 2) (var 2)))) (op (var 3) (var 3))) , (var 1)) → ⊥
  cut5779  adequate = bad5779  (Adequate.valid adequate Two boolean env5)
  bad5780 : PathP (λ _ → Two) (bop (bop b0 (bop b0 (bop b0 b0))) (bop b1 b1)) b0 → ⊥
  bad5780  p = false≢true (sym (cong lower p))
  cut5780 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (op (var 2) (var 2)))) (op (var 3) (var 3))) , (var 2)) → ⊥
  cut5780  adequate = bad5780  (Adequate.valid adequate Two boolean env5)
  bad5781 : PathP (λ _ → Two) (bop (bop b1 (bop b0 (bop b0 b0))) (bop b0 b0)) b0 → ⊥
  bad5781  p = false≢true (sym (cong lower p))
  cut5781 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (op (var 2) (var 2)))) (op (var 3) (var 3))) , (var 3)) → ⊥
  cut5781  adequate = bad5781  (Adequate.valid adequate Two boolean env11)
  bad5782 : PathP (λ _ → Two) (bop (bop b0 (bop b0 (bop b0 b0))) (bop b0 b0)) b1 → ⊥
  bad5782  p = false≢true (cong lower p)
  cut5782 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (op (var 2) (var 2)))) (op (var 3) (var 3))) , (var 4)) → ⊥
  cut5782  adequate = bad5782  (Adequate.valid adequate Two boolean env10)
  bad5783 : PathP (λ _ → Two) (bop (bop b0 (bop b0 (bop b0 b0))) (bop b1 b1)) b0 → ⊥
  bad5783  p = false≢true (sym (cong lower p))
  cut5783 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (op (var 2) (var 2)))) (op (var 3) (var 4))) , (var 0)) → ⊥
  cut5783  adequate = bad5783  (Adequate.valid adequate Two boolean env15)
  bad5784 : PathP (λ _ → Two) (bop (bop b0 (bop b0 (bop b0 b0))) (bop b1 b1)) b0 → ⊥
  bad5784  p = false≢true (sym (cong lower p))
  cut5784 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (op (var 2) (var 2)))) (op (var 3) (var 4))) , (var 1)) → ⊥
  cut5784  adequate = bad5784  (Adequate.valid adequate Two boolean env15)
  bad5785 : PathP (λ _ → Two) (bop (bop b0 (bop b0 (bop b0 b0))) (bop b1 b1)) b0 → ⊥
  bad5785  p = false≢true (sym (cong lower p))
  cut5785 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (op (var 2) (var 2)))) (op (var 3) (var 4))) , (var 2)) → ⊥
  cut5785  adequate = bad5785  (Adequate.valid adequate Two boolean env15)
  bad5786 : PathP (λ _ → Two) (bop (bop b0 (bop b0 (bop b0 b0))) (bop b1 b0)) b1 → ⊥
  bad5786  p = false≢true (cong lower p)
  cut5786 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (op (var 2) (var 2)))) (op (var 3) (var 4))) , (var 3)) → ⊥
  cut5786  adequate = bad5786  (Adequate.valid adequate Two boolean env16)
  bad5787 : PathP (λ _ → Two) (bop (bop b0 (bop b0 (bop b0 b0))) (bop b0 b1)) b1 → ⊥
  bad5787  p = false≢true (cong lower p)
  cut5787 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (op (var 2) (var 2)))) (op (var 3) (var 4))) , (var 4)) → ⊥
  cut5787  adequate = bad5787  (Adequate.valid adequate Two boolean env10)
  bad5788 : PathP (λ _ → Two) (bop (bop b0 (bop b0 (bop b0 b0))) (bop b0 b0)) b1 → ⊥
  bad5788  p = false≢true (cong lower p)
  cut5788 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (op (var 2) (var 2)))) (op (var 3) (var 4))) , (var 5)) → ⊥
  cut5788  adequate = bad5788  (Adequate.valid adequate Two boolean env17)
  holds5789 : (z0 z1 z2 z3 : A2) → (mul2 (mul2 z0 (mul2 z1 (mul2 z2 z3))) (mul2 z0 z0)) ≡ z0
  holds5789 z0 z1 z2 z3 = refl
  cut5789 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (op (var 2) (var 3)))) (op (var 0) (var 0))) , (var 0)) → ⊥
  cut5789  = reject2 ((op (op (var 0) (op (var 1) (op (var 2) (var 3)))) (op (var 0) (var 0))) , (var 0)) (λ env → holds5789 (env 0) (env 1) (env 2) (env 3))
  bad5790 : PathP (λ _ → Two) (bop (bop b0 (bop b1 (bop b0 b0))) (bop b0 b0)) b1 → ⊥
  bad5790  p = false≢true (cong lower p)
  cut5790 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (op (var 2) (var 3)))) (op (var 0) (var 0))) , (var 1)) → ⊥
  cut5790  adequate = bad5790  (Adequate.valid adequate Two boolean env12)
  bad5791 : PathP (λ _ → Two) (bop (bop b0 (bop b0 (bop b1 b0))) (bop b0 b0)) b1 → ⊥
  bad5791  p = false≢true (cong lower p)
  cut5791 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (op (var 2) (var 3)))) (op (var 0) (var 0))) , (var 2)) → ⊥
  cut5791  adequate = bad5791  (Adequate.valid adequate Two boolean env9)
  bad5792 : PathP (λ _ → Two) (bop (bop b0 (bop b0 (bop b0 b1))) (bop b0 b0)) b1 → ⊥
  bad5792  p = false≢true (cong lower p)
  cut5792 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (op (var 2) (var 3)))) (op (var 0) (var 0))) , (var 3)) → ⊥
  cut5792  adequate = bad5792  (Adequate.valid adequate Two boolean env5)
  bad5793 : PathP (λ _ → Two) (bop (bop b0 (bop b0 (bop b0 b0))) (bop b0 b0)) b1 → ⊥
  bad5793  p = false≢true (cong lower p)
  cut5793 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (op (var 2) (var 3)))) (op (var 0) (var 0))) , (var 4)) → ⊥
  cut5793  adequate = bad5793  (Adequate.valid adequate Two boolean env10)
  holds5794 : (z0 z1 z2 z3 : A2) → (mul2 (mul2 z0 (mul2 z1 (mul2 z2 z3))) (mul2 z0 z1)) ≡ z0
  holds5794 z0 z1 z2 z3 = refl
  cut5794 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (op (var 2) (var 3)))) (op (var 0) (var 1))) , (var 0)) → ⊥
  cut5794  = reject2 ((op (op (var 0) (op (var 1) (op (var 2) (var 3)))) (op (var 0) (var 1))) , (var 0)) (λ env → holds5794 (env 0) (env 1) (env 2) (env 3))
  bad5795 : PathP (λ _ → Two) (bop (bop b0 (bop b1 (bop b0 b0))) (bop b0 b1)) b1 → ⊥
  bad5795  p = false≢true (cong lower p)
  cut5795 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (op (var 2) (var 3)))) (op (var 0) (var 1))) , (var 1)) → ⊥
  cut5795  adequate = bad5795  (Adequate.valid adequate Two boolean env12)
  bad5796 : PathP (λ _ → Two) (bop (bop b0 (bop b0 (bop b1 b0))) (bop b0 b0)) b1 → ⊥
  bad5796  p = false≢true (cong lower p)
  cut5796 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (op (var 2) (var 3)))) (op (var 0) (var 1))) , (var 2)) → ⊥
  cut5796  adequate = bad5796  (Adequate.valid adequate Two boolean env9)
  bad5797 : PathP (λ _ → Two) (bop (bop b0 (bop b0 (bop b0 b1))) (bop b0 b0)) b1 → ⊥
  bad5797  p = false≢true (cong lower p)
  cut5797 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (op (var 2) (var 3)))) (op (var 0) (var 1))) , (var 3)) → ⊥
  cut5797  adequate = bad5797  (Adequate.valid adequate Two boolean env5)
  bad5798 : PathP (λ _ → Two) (bop (bop b0 (bop b0 (bop b0 b0))) (bop b0 b0)) b1 → ⊥
  bad5798  p = false≢true (cong lower p)
  cut5798 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (op (var 2) (var 3)))) (op (var 0) (var 1))) , (var 4)) → ⊥
  cut5798  adequate = bad5798  (Adequate.valid adequate Two boolean env10)
  bad5799 : PathP (λ _ → Two) (bop (bop b1 (bop b1 (bop b0 b0))) (bop b1 b0)) b1 → ⊥
  bad5799  p = false≢true (cong lower p)
  cut5799 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (op (var 2) (var 3)))) (op (var 0) (var 2))) , (var 0)) → ⊥
  cut5799  adequate = bad5799  (Adequate.valid adequate Two boolean env18)
  bad5800 : PathP (λ _ → Two) (bop (bop b0 (bop b1 (bop b0 b0))) (bop b0 b0)) b1 → ⊥
  bad5800  p = false≢true (cong lower p)
  cut5800 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (op (var 2) (var 3)))) (op (var 0) (var 2))) , (var 1)) → ⊥
  cut5800  adequate = bad5800  (Adequate.valid adequate Two boolean env12)
  bad5801 : PathP (λ _ → Two) (bop (bop b0 (bop b0 (bop b1 b0))) (bop b0 b1)) b1 → ⊥
  bad5801  p = false≢true (cong lower p)
  cut5801 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (op (var 2) (var 3)))) (op (var 0) (var 2))) , (var 2)) → ⊥
  cut5801  adequate = bad5801  (Adequate.valid adequate Two boolean env9)
  bad5802 : PathP (λ _ → Two) (bop (bop b0 (bop b0 (bop b0 b1))) (bop b0 b0)) b1 → ⊥
  bad5802  p = false≢true (cong lower p)
  cut5802 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (op (var 2) (var 3)))) (op (var 0) (var 2))) , (var 3)) → ⊥
  cut5802  adequate = bad5802  (Adequate.valid adequate Two boolean env5)
  bad5803 : PathP (λ _ → Two) (bop (bop b0 (bop b0 (bop b0 b0))) (bop b0 b0)) b1 → ⊥
  bad5803  p = false≢true (cong lower p)
  cut5803 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (op (var 2) (var 3)))) (op (var 0) (var 2))) , (var 4)) → ⊥
  cut5803  adequate = bad5803  (Adequate.valid adequate Two boolean env10)
  bad5804 : PathP (λ _ → Two) (bop (bop b1 (bop b1 (bop b0 b0))) (bop b1 b0)) b1 → ⊥
  bad5804  p = false≢true (cong lower p)
  cut5804 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (op (var 2) (var 3)))) (op (var 0) (var 3))) , (var 0)) → ⊥
  cut5804  adequate = bad5804  (Adequate.valid adequate Two boolean env18)
  bad5805 : PathP (λ _ → Two) (bop (bop b0 (bop b1 (bop b0 b0))) (bop b0 b0)) b1 → ⊥
  bad5805  p = false≢true (cong lower p)
  cut5805 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (op (var 2) (var 3)))) (op (var 0) (var 3))) , (var 1)) → ⊥
  cut5805  adequate = bad5805  (Adequate.valid adequate Two boolean env12)
  bad5806 : PathP (λ _ → Two) (bop (bop b0 (bop b0 (bop b1 b0))) (bop b0 b0)) b1 → ⊥
  bad5806  p = false≢true (cong lower p)
  cut5806 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (op (var 2) (var 3)))) (op (var 0) (var 3))) , (var 2)) → ⊥
  cut5806  adequate = bad5806  (Adequate.valid adequate Two boolean env9)
  bad5807 : PathP (λ _ → Two) (bop (bop b0 (bop b0 (bop b0 b1))) (bop b0 b1)) b1 → ⊥
  bad5807  p = false≢true (cong lower p)
  cut5807 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (op (var 2) (var 3)))) (op (var 0) (var 3))) , (var 3)) → ⊥
  cut5807  adequate = bad5807  (Adequate.valid adequate Two boolean env5)
  bad5808 : PathP (λ _ → Two) (bop (bop b0 (bop b0 (bop b0 b0))) (bop b0 b0)) b1 → ⊥
  bad5808  p = false≢true (cong lower p)
  cut5808 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (op (var 2) (var 3)))) (op (var 0) (var 3))) , (var 4)) → ⊥
  cut5808  adequate = bad5808  (Adequate.valid adequate Two boolean env10)
  env19 : ℕ → Two
  env19 zero = b1
  env19 (suc zero) = b1
  env19 (suc (suc zero)) = b0
  env19 (suc (suc (suc zero))) = b0
  env19 (suc (suc (suc (suc zero)))) = b0
  env19 (suc (suc (suc (suc (suc rest))))) = b0
  bad5809 : PathP (λ _ → Two) (bop (bop b1 (bop b1 (bop b0 b0))) (bop b1 b0)) b1 → ⊥
  bad5809  p = false≢true (cong lower p)
  cut5809 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (op (var 2) (var 3)))) (op (var 0) (var 4))) , (var 0)) → ⊥
  cut5809  adequate = bad5809  (Adequate.valid adequate Two boolean env19)
  env20 : ℕ → Two
  env20 zero = b0
  env20 (suc zero) = b1
  env20 (suc (suc zero)) = b0
  env20 (suc (suc (suc zero))) = b0
  env20 (suc (suc (suc (suc zero)))) = b0
  env20 (suc (suc (suc (suc (suc rest))))) = b0
  bad5810 : PathP (λ _ → Two) (bop (bop b0 (bop b1 (bop b0 b0))) (bop b0 b0)) b1 → ⊥
  bad5810  p = false≢true (cong lower p)
  cut5810 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (op (var 2) (var 3)))) (op (var 0) (var 4))) , (var 1)) → ⊥
  cut5810  adequate = bad5810  (Adequate.valid adequate Two boolean env20)
  env21 : ℕ → Two
  env21 zero = b0
  env21 (suc zero) = b0
  env21 (suc (suc zero)) = b1
  env21 (suc (suc (suc zero))) = b0
  env21 (suc (suc (suc (suc zero)))) = b0
  env21 (suc (suc (suc (suc (suc rest))))) = b0
  bad5811 : PathP (λ _ → Two) (bop (bop b0 (bop b0 (bop b1 b0))) (bop b0 b0)) b1 → ⊥
  bad5811  p = false≢true (cong lower p)
  cut5811 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (op (var 2) (var 3)))) (op (var 0) (var 4))) , (var 2)) → ⊥
  cut5811  adequate = bad5811  (Adequate.valid adequate Two boolean env21)
  bad5812 : PathP (λ _ → Two) (bop (bop b0 (bop b0 (bop b0 b1))) (bop b0 b0)) b1 → ⊥
  bad5812  p = false≢true (cong lower p)
  cut5812 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (op (var 2) (var 3)))) (op (var 0) (var 4))) , (var 3)) → ⊥
  cut5812  adequate = bad5812  (Adequate.valid adequate Two boolean env16)
  bad5813 : PathP (λ _ → Two) (bop (bop b0 (bop b0 (bop b0 b0))) (bop b0 b1)) b1 → ⊥
  bad5813  p = false≢true (cong lower p)
  cut5813 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (op (var 2) (var 3)))) (op (var 0) (var 4))) , (var 4)) → ⊥
  cut5813  adequate = bad5813  (Adequate.valid adequate Two boolean env10)
  bad5814 : PathP (λ _ → Two) (bop (bop b0 (bop b0 (bop b0 b0))) (bop b0 b0)) b1 → ⊥
  bad5814  p = false≢true (cong lower p)
  cut5814 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (op (var 2) (var 3)))) (op (var 0) (var 4))) , (var 5)) → ⊥
  cut5814  adequate = bad5814  (Adequate.valid adequate Two boolean env17)
  holds5815 : (z0 z1 z2 z3 : A2) → (mul2 (mul2 z0 (mul2 z1 (mul2 z2 z3))) (mul2 z1 z0)) ≡ z0
  holds5815 z0 z1 z2 z3 = refl
  cut5815 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (op (var 2) (var 3)))) (op (var 1) (var 0))) , (var 0)) → ⊥
  cut5815  = reject2 ((op (op (var 0) (op (var 1) (op (var 2) (var 3)))) (op (var 1) (var 0))) , (var 0)) (λ env → holds5815 (env 0) (env 1) (env 2) (env 3))
  bad5816 : PathP (λ _ → Two) (bop (bop b0 (bop b1 (bop b0 b0))) (bop b1 b0)) b1 → ⊥
  bad5816  p = false≢true (cong lower p)
  cut5816 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (op (var 2) (var 3)))) (op (var 1) (var 0))) , (var 1)) → ⊥
  cut5816  adequate = bad5816  (Adequate.valid adequate Two boolean env12)
  bad5817 : PathP (λ _ → Two) (bop (bop b0 (bop b0 (bop b1 b0))) (bop b0 b0)) b1 → ⊥
  bad5817  p = false≢true (cong lower p)
  cut5817 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (op (var 2) (var 3)))) (op (var 1) (var 0))) , (var 2)) → ⊥
  cut5817  adequate = bad5817  (Adequate.valid adequate Two boolean env9)
  bad5818 : PathP (λ _ → Two) (bop (bop b0 (bop b0 (bop b0 b1))) (bop b0 b0)) b1 → ⊥
  bad5818  p = false≢true (cong lower p)
  cut5818 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (op (var 2) (var 3)))) (op (var 1) (var 0))) , (var 3)) → ⊥
  cut5818  adequate = bad5818  (Adequate.valid adequate Two boolean env5)
  bad5819 : PathP (λ _ → Two) (bop (bop b0 (bop b0 (bop b0 b0))) (bop b0 b0)) b1 → ⊥
  bad5819  p = false≢true (cong lower p)
  cut5819 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (op (var 2) (var 3)))) (op (var 1) (var 0))) , (var 4)) → ⊥
  cut5819  adequate = bad5819  (Adequate.valid adequate Two boolean env10)
  bad5820 : PathP (λ _ → Two) (bop (bop b0 (bop b1 (bop b0 b0))) (bop b1 b1)) b0 → ⊥
  bad5820  p = false≢true (sym (cong lower p))
  cut5820 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (op (var 2) (var 3)))) (op (var 1) (var 1))) , (var 0)) → ⊥
  cut5820  adequate = bad5820  (Adequate.valid adequate Two boolean env12)
  bad5821 : PathP (λ _ → Two) (bop (bop b1 (bop b0 (bop b0 b0))) (bop b0 b0)) b0 → ⊥
  bad5821  p = false≢true (sym (cong lower p))
  cut5821 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (op (var 2) (var 3)))) (op (var 1) (var 1))) , (var 1)) → ⊥
  cut5821  adequate = bad5821  (Adequate.valid adequate Two boolean env11)
  bad5822 : PathP (λ _ → Two) (bop (bop b0 (bop b0 (bop b1 b0))) (bop b0 b0)) b1 → ⊥
  bad5822  p = false≢true (cong lower p)
  cut5822 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (op (var 2) (var 3)))) (op (var 1) (var 1))) , (var 2)) → ⊥
  cut5822  adequate = bad5822  (Adequate.valid adequate Two boolean env9)
  bad5823 : PathP (λ _ → Two) (bop (bop b0 (bop b0 (bop b0 b1))) (bop b0 b0)) b1 → ⊥
  bad5823  p = false≢true (cong lower p)
  cut5823 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (op (var 2) (var 3)))) (op (var 1) (var 1))) , (var 3)) → ⊥
  cut5823  adequate = bad5823  (Adequate.valid adequate Two boolean env5)
  bad5824 : PathP (λ _ → Two) (bop (bop b0 (bop b0 (bop b0 b0))) (bop b0 b0)) b1 → ⊥
  bad5824  p = false≢true (cong lower p)
  cut5824 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (op (var 2) (var 3)))) (op (var 1) (var 1))) , (var 4)) → ⊥
  cut5824  adequate = bad5824  (Adequate.valid adequate Two boolean env10)
  env22 : ℕ → Two
  env22 zero = b0
  env22 (suc zero) = b1
  env22 (suc (suc zero)) = b1
  env22 (suc (suc (suc zero))) = b0
  env22 (suc (suc (suc (suc rest)))) = b0
  bad5825 : PathP (λ _ → Two) (bop (bop b0 (bop b1 (bop b1 b0))) (bop b1 b1)) b0 → ⊥
  bad5825  p = false≢true (sym (cong lower p))
  cut5825 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (op (var 2) (var 3)))) (op (var 1) (var 2))) , (var 0)) → ⊥
  cut5825  adequate = bad5825  (Adequate.valid adequate Two boolean env22)
  bad5826 : PathP (λ _ → Two) (bop (bop b0 (bop b1 (bop b0 b0))) (bop b1 b0)) b1 → ⊥
  bad5826  p = false≢true (cong lower p)
  cut5826 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (op (var 2) (var 3)))) (op (var 1) (var 2))) , (var 1)) → ⊥
  cut5826  adequate = bad5826  (Adequate.valid adequate Two boolean env12)
  bad5827 : PathP (λ _ → Two) (bop (bop b0 (bop b0 (bop b1 b0))) (bop b0 b1)) b1 → ⊥
  bad5827  p = false≢true (cong lower p)
  cut5827 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (op (var 2) (var 3)))) (op (var 1) (var 2))) , (var 2)) → ⊥
  cut5827  adequate = bad5827  (Adequate.valid adequate Two boolean env9)
  bad5828 : PathP (λ _ → Two) (bop (bop b0 (bop b0 (bop b0 b1))) (bop b0 b0)) b1 → ⊥
  bad5828  p = false≢true (cong lower p)
  cut5828 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (op (var 2) (var 3)))) (op (var 1) (var 2))) , (var 3)) → ⊥
  cut5828  adequate = bad5828  (Adequate.valid adequate Two boolean env5)
  bad5829 : PathP (λ _ → Two) (bop (bop b0 (bop b0 (bop b0 b0))) (bop b0 b0)) b1 → ⊥
  bad5829  p = false≢true (cong lower p)
  cut5829 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (op (var 2) (var 3)))) (op (var 1) (var 2))) , (var 4)) → ⊥
  cut5829  adequate = bad5829  (Adequate.valid adequate Two boolean env10)
  bad5830 : PathP (λ _ → Two) (bop (bop b0 (bop b1 (bop b0 b1))) (bop b1 b1)) b0 → ⊥
  bad5830  p = false≢true (sym (cong lower p))
  cut5830 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (op (var 2) (var 3)))) (op (var 1) (var 3))) , (var 0)) → ⊥
  cut5830  adequate = bad5830  (Adequate.valid adequate Two boolean env13)
  bad5831 : PathP (λ _ → Two) (bop (bop b0 (bop b1 (bop b0 b0))) (bop b1 b0)) b1 → ⊥
  bad5831  p = false≢true (cong lower p)
  cut5831 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (op (var 2) (var 3)))) (op (var 1) (var 3))) , (var 1)) → ⊥
  cut5831  adequate = bad5831  (Adequate.valid adequate Two boolean env12)
  bad5832 : PathP (λ _ → Two) (bop (bop b0 (bop b0 (bop b1 b0))) (bop b0 b0)) b1 → ⊥
  bad5832  p = false≢true (cong lower p)
  cut5832 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (op (var 2) (var 3)))) (op (var 1) (var 3))) , (var 2)) → ⊥
  cut5832  adequate = bad5832  (Adequate.valid adequate Two boolean env9)
  bad5833 : PathP (λ _ → Two) (bop (bop b0 (bop b0 (bop b0 b1))) (bop b0 b1)) b1 → ⊥
  bad5833  p = false≢true (cong lower p)
  cut5833 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (op (var 2) (var 3)))) (op (var 1) (var 3))) , (var 3)) → ⊥
  cut5833  adequate = bad5833  (Adequate.valid adequate Two boolean env5)
  bad5834 : PathP (λ _ → Two) (bop (bop b0 (bop b0 (bop b0 b0))) (bop b0 b0)) b1 → ⊥
  bad5834  p = false≢true (cong lower p)
  cut5834 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (op (var 2) (var 3)))) (op (var 1) (var 3))) , (var 4)) → ⊥
  cut5834  adequate = bad5834  (Adequate.valid adequate Two boolean env10)
  env23 : ℕ → Two
  env23 zero = b0
  env23 (suc zero) = b1
  env23 (suc (suc zero)) = b0
  env23 (suc (suc (suc zero))) = b0
  env23 (suc (suc (suc (suc zero)))) = b1
  env23 (suc (suc (suc (suc (suc rest))))) = b0
  bad5835 : PathP (λ _ → Two) (bop (bop b0 (bop b1 (bop b0 b0))) (bop b1 b1)) b0 → ⊥
  bad5835  p = false≢true (sym (cong lower p))
  cut5835 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (op (var 2) (var 3)))) (op (var 1) (var 4))) , (var 0)) → ⊥
  cut5835  adequate = bad5835  (Adequate.valid adequate Two boolean env23)
  bad5836 : PathP (λ _ → Two) (bop (bop b0 (bop b1 (bop b0 b0))) (bop b1 b0)) b1 → ⊥
  bad5836  p = false≢true (cong lower p)
  cut5836 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (op (var 2) (var 3)))) (op (var 1) (var 4))) , (var 1)) → ⊥
  cut5836  adequate = bad5836  (Adequate.valid adequate Two boolean env20)
  bad5837 : PathP (λ _ → Two) (bop (bop b0 (bop b0 (bop b1 b0))) (bop b0 b0)) b1 → ⊥
  bad5837  p = false≢true (cong lower p)
  cut5837 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (op (var 2) (var 3)))) (op (var 1) (var 4))) , (var 2)) → ⊥
  cut5837  adequate = bad5837  (Adequate.valid adequate Two boolean env21)
  bad5838 : PathP (λ _ → Two) (bop (bop b0 (bop b0 (bop b0 b1))) (bop b0 b0)) b1 → ⊥
  bad5838  p = false≢true (cong lower p)
  cut5838 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (op (var 2) (var 3)))) (op (var 1) (var 4))) , (var 3)) → ⊥
  cut5838  adequate = bad5838  (Adequate.valid adequate Two boolean env16)
  bad5839 : PathP (λ _ → Two) (bop (bop b0 (bop b0 (bop b0 b0))) (bop b0 b1)) b1 → ⊥
  bad5839  p = false≢true (cong lower p)
  cut5839 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (op (var 2) (var 3)))) (op (var 1) (var 4))) , (var 4)) → ⊥
  cut5839  adequate = bad5839  (Adequate.valid adequate Two boolean env10)
  bad5840 : PathP (λ _ → Two) (bop (bop b0 (bop b0 (bop b0 b0))) (bop b0 b0)) b1 → ⊥
  bad5840  p = false≢true (cong lower p)
  cut5840 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (op (var 2) (var 3)))) (op (var 1) (var 4))) , (var 5)) → ⊥
  cut5840  adequate = bad5840  (Adequate.valid adequate Two boolean env17)
  bad5841 : PathP (λ _ → Two) (bop (bop b1 (bop b1 (bop b0 b0))) (bop b0 b1)) b1 → ⊥
  bad5841  p = false≢true (cong lower p)
  cut5841 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (op (var 2) (var 3)))) (op (var 2) (var 0))) , (var 0)) → ⊥
  cut5841  adequate = bad5841  (Adequate.valid adequate Two boolean env18)
  bad5842 : PathP (λ _ → Two) (bop (bop b0 (bop b1 (bop b0 b0))) (bop b0 b0)) b1 → ⊥
  bad5842  p = false≢true (cong lower p)
  cut5842 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (op (var 2) (var 3)))) (op (var 2) (var 0))) , (var 1)) → ⊥
  cut5842  adequate = bad5842  (Adequate.valid adequate Two boolean env12)
  bad5843 : PathP (λ _ → Two) (bop (bop b0 (bop b0 (bop b1 b0))) (bop b1 b0)) b1 → ⊥
  bad5843  p = false≢true (cong lower p)
  cut5843 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (op (var 2) (var 3)))) (op (var 2) (var 0))) , (var 2)) → ⊥
  cut5843  adequate = bad5843  (Adequate.valid adequate Two boolean env9)
  bad5844 : PathP (λ _ → Two) (bop (bop b0 (bop b0 (bop b0 b1))) (bop b0 b0)) b1 → ⊥
  bad5844  p = false≢true (cong lower p)
  cut5844 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (op (var 2) (var 3)))) (op (var 2) (var 0))) , (var 3)) → ⊥
  cut5844  adequate = bad5844  (Adequate.valid adequate Two boolean env5)
  bad5845 : PathP (λ _ → Two) (bop (bop b0 (bop b0 (bop b0 b0))) (bop b0 b0)) b1 → ⊥
  bad5845  p = false≢true (cong lower p)
  cut5845 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (op (var 2) (var 3)))) (op (var 2) (var 0))) , (var 4)) → ⊥
  cut5845  adequate = bad5845  (Adequate.valid adequate Two boolean env10)
  bad5846 : PathP (λ _ → Two) (bop (bop b0 (bop b1 (bop b1 b0))) (bop b1 b1)) b0 → ⊥
  bad5846  p = false≢true (sym (cong lower p))
  cut5846 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (op (var 2) (var 3)))) (op (var 2) (var 1))) , (var 0)) → ⊥
  cut5846  adequate = bad5846  (Adequate.valid adequate Two boolean env22)
  bad5847 : PathP (λ _ → Two) (bop (bop b0 (bop b1 (bop b0 b0))) (bop b0 b1)) b1 → ⊥
  bad5847  p = false≢true (cong lower p)
  cut5847 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (op (var 2) (var 3)))) (op (var 2) (var 1))) , (var 1)) → ⊥
  cut5847  adequate = bad5847  (Adequate.valid adequate Two boolean env12)
  bad5848 : PathP (λ _ → Two) (bop (bop b0 (bop b0 (bop b1 b0))) (bop b1 b0)) b1 → ⊥
  bad5848  p = false≢true (cong lower p)
  cut5848 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (op (var 2) (var 3)))) (op (var 2) (var 1))) , (var 2)) → ⊥
  cut5848  adequate = bad5848  (Adequate.valid adequate Two boolean env9)
  bad5849 : PathP (λ _ → Two) (bop (bop b0 (bop b0 (bop b0 b1))) (bop b0 b0)) b1 → ⊥
  bad5849  p = false≢true (cong lower p)
  cut5849 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (op (var 2) (var 3)))) (op (var 2) (var 1))) , (var 3)) → ⊥
  cut5849  adequate = bad5849  (Adequate.valid adequate Two boolean env5)
  bad5850 : PathP (λ _ → Two) (bop (bop b0 (bop b0 (bop b0 b0))) (bop b0 b0)) b1 → ⊥
  bad5850  p = false≢true (cong lower p)
  cut5850 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (op (var 2) (var 3)))) (op (var 2) (var 1))) , (var 4)) → ⊥
  cut5850  adequate = bad5850  (Adequate.valid adequate Two boolean env10)
  bad5851 : PathP (λ _ → Two) (bop (bop b0 (bop b0 (bop b1 b0))) (bop b1 b1)) b0 → ⊥
  bad5851  p = false≢true (sym (cong lower p))
  cut5851 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (op (var 2) (var 3)))) (op (var 2) (var 2))) , (var 0)) → ⊥
  cut5851  adequate = bad5851  (Adequate.valid adequate Two boolean env9)
  bad5852 : PathP (λ _ → Two) (bop (bop b0 (bop b0 (bop b1 b0))) (bop b1 b1)) b0 → ⊥
  bad5852  p = false≢true (sym (cong lower p))
  cut5852 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (op (var 2) (var 3)))) (op (var 2) (var 2))) , (var 1)) → ⊥
  cut5852  adequate = bad5852  (Adequate.valid adequate Two boolean env9)
  bad5853 : PathP (λ _ → Two) (bop (bop b1 (bop b0 (bop b0 b0))) (bop b0 b0)) b0 → ⊥
  bad5853  p = false≢true (sym (cong lower p))
  cut5853 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (op (var 2) (var 3)))) (op (var 2) (var 2))) , (var 2)) → ⊥
  cut5853  adequate = bad5853  (Adequate.valid adequate Two boolean env11)
  bad5854 : PathP (λ _ → Two) (bop (bop b0 (bop b0 (bop b0 b1))) (bop b0 b0)) b1 → ⊥
  bad5854  p = false≢true (cong lower p)
  cut5854 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (op (var 2) (var 3)))) (op (var 2) (var 2))) , (var 3)) → ⊥
  cut5854  adequate = bad5854  (Adequate.valid adequate Two boolean env5)
  bad5855 : PathP (λ _ → Two) (bop (bop b0 (bop b0 (bop b0 b0))) (bop b0 b0)) b1 → ⊥
  bad5855  p = false≢true (cong lower p)
  cut5855 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (op (var 2) (var 3)))) (op (var 2) (var 2))) , (var 4)) → ⊥
  cut5855  adequate = bad5855  (Adequate.valid adequate Two boolean env10)
  bad5856 : PathP (λ _ → Two) (bop (bop b0 (bop b0 (bop b1 b1))) (bop b1 b1)) b0 → ⊥
  bad5856  p = false≢true (sym (cong lower p))
  cut5856 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (op (var 2) (var 3)))) (op (var 2) (var 3))) , (var 0)) → ⊥
  cut5856  adequate = bad5856  (Adequate.valid adequate Two boolean env8)
  bad5857 : PathP (λ _ → Two) (bop (bop b0 (bop b0 (bop b1 b1))) (bop b1 b1)) b0 → ⊥
  bad5857  p = false≢true (sym (cong lower p))
  cut5857 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (op (var 2) (var 3)))) (op (var 2) (var 3))) , (var 1)) → ⊥
  cut5857  adequate = bad5857  (Adequate.valid adequate Two boolean env8)
  bad5858 : PathP (λ _ → Two) (bop (bop b0 (bop b0 (bop b1 b0))) (bop b1 b0)) b1 → ⊥
  bad5858  p = false≢true (cong lower p)
  cut5858 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (op (var 2) (var 3)))) (op (var 2) (var 3))) , (var 2)) → ⊥
  cut5858  adequate = bad5858  (Adequate.valid adequate Two boolean env9)
  bad5859 : PathP (λ _ → Two) (bop (bop b0 (bop b0 (bop b0 b1))) (bop b0 b1)) b1 → ⊥
  bad5859  p = false≢true (cong lower p)
  cut5859 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (op (var 2) (var 3)))) (op (var 2) (var 3))) , (var 3)) → ⊥
  cut5859  adequate = bad5859  (Adequate.valid adequate Two boolean env5)
  bad5860 : PathP (λ _ → Two) (bop (bop b0 (bop b0 (bop b0 b0))) (bop b0 b0)) b1 → ⊥
  bad5860  p = false≢true (cong lower p)
  cut5860 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (op (var 2) (var 3)))) (op (var 2) (var 3))) , (var 4)) → ⊥
  cut5860  adequate = bad5860  (Adequate.valid adequate Two boolean env10)
  env24 : ℕ → Two
  env24 zero = b0
  env24 (suc zero) = b0
  env24 (suc (suc zero)) = b1
  env24 (suc (suc (suc zero))) = b0
  env24 (suc (suc (suc (suc zero)))) = b1
  env24 (suc (suc (suc (suc (suc rest))))) = b0
  bad5861 : PathP (λ _ → Two) (bop (bop b0 (bop b0 (bop b1 b0))) (bop b1 b1)) b0 → ⊥
  bad5861  p = false≢true (sym (cong lower p))
  cut5861 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (op (var 2) (var 3)))) (op (var 2) (var 4))) , (var 0)) → ⊥
  cut5861  adequate = bad5861  (Adequate.valid adequate Two boolean env24)
  bad5862 : PathP (λ _ → Two) (bop (bop b0 (bop b0 (bop b1 b0))) (bop b1 b1)) b0 → ⊥
  bad5862  p = false≢true (sym (cong lower p))
  cut5862 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (op (var 2) (var 3)))) (op (var 2) (var 4))) , (var 1)) → ⊥
  cut5862  adequate = bad5862  (Adequate.valid adequate Two boolean env24)
  bad5863 : PathP (λ _ → Two) (bop (bop b0 (bop b0 (bop b1 b0))) (bop b1 b0)) b1 → ⊥
  bad5863  p = false≢true (cong lower p)
  cut5863 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (op (var 2) (var 3)))) (op (var 2) (var 4))) , (var 2)) → ⊥
  cut5863  adequate = bad5863  (Adequate.valid adequate Two boolean env21)
  bad5864 : PathP (λ _ → Two) (bop (bop b0 (bop b0 (bop b0 b1))) (bop b0 b0)) b1 → ⊥
  bad5864  p = false≢true (cong lower p)
  cut5864 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (op (var 2) (var 3)))) (op (var 2) (var 4))) , (var 3)) → ⊥
  cut5864  adequate = bad5864  (Adequate.valid adequate Two boolean env16)
  bad5865 : PathP (λ _ → Two) (bop (bop b0 (bop b0 (bop b0 b0))) (bop b0 b1)) b1 → ⊥
  bad5865  p = false≢true (cong lower p)
  cut5865 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (op (var 2) (var 3)))) (op (var 2) (var 4))) , (var 4)) → ⊥
  cut5865  adequate = bad5865  (Adequate.valid adequate Two boolean env10)
  bad5866 : PathP (λ _ → Two) (bop (bop b0 (bop b0 (bop b0 b0))) (bop b0 b0)) b1 → ⊥
  bad5866  p = false≢true (cong lower p)
  cut5866 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (op (var 2) (var 3)))) (op (var 2) (var 4))) , (var 5)) → ⊥
  cut5866  adequate = bad5866  (Adequate.valid adequate Two boolean env17)
  bad5867 : PathP (λ _ → Two) (bop (bop b1 (bop b1 (bop b0 b0))) (bop b0 b1)) b1 → ⊥
  bad5867  p = false≢true (cong lower p)
  cut5867 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (op (var 2) (var 3)))) (op (var 3) (var 0))) , (var 0)) → ⊥
  cut5867  adequate = bad5867  (Adequate.valid adequate Two boolean env18)
  bad5868 : PathP (λ _ → Two) (bop (bop b0 (bop b1 (bop b0 b0))) (bop b0 b0)) b1 → ⊥
  bad5868  p = false≢true (cong lower p)
  cut5868 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (op (var 2) (var 3)))) (op (var 3) (var 0))) , (var 1)) → ⊥
  cut5868  adequate = bad5868  (Adequate.valid adequate Two boolean env12)
  bad5869 : PathP (λ _ → Two) (bop (bop b0 (bop b0 (bop b1 b0))) (bop b0 b0)) b1 → ⊥
  bad5869  p = false≢true (cong lower p)
  cut5869 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (op (var 2) (var 3)))) (op (var 3) (var 0))) , (var 2)) → ⊥
  cut5869  adequate = bad5869  (Adequate.valid adequate Two boolean env9)
  bad5870 : PathP (λ _ → Two) (bop (bop b0 (bop b0 (bop b0 b1))) (bop b1 b0)) b1 → ⊥
  bad5870  p = false≢true (cong lower p)
  cut5870 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (op (var 2) (var 3)))) (op (var 3) (var 0))) , (var 3)) → ⊥
  cut5870  adequate = bad5870  (Adequate.valid adequate Two boolean env5)
  bad5871 : PathP (λ _ → Two) (bop (bop b0 (bop b0 (bop b0 b0))) (bop b0 b0)) b1 → ⊥
  bad5871  p = false≢true (cong lower p)
  cut5871 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (op (var 2) (var 3)))) (op (var 3) (var 0))) , (var 4)) → ⊥
  cut5871  adequate = bad5871  (Adequate.valid adequate Two boolean env10)
  bad5872 : PathP (λ _ → Two) (bop (bop b0 (bop b1 (bop b0 b1))) (bop b1 b1)) b0 → ⊥
  bad5872  p = false≢true (sym (cong lower p))
  cut5872 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (op (var 2) (var 3)))) (op (var 3) (var 1))) , (var 0)) → ⊥
  cut5872  adequate = bad5872  (Adequate.valid adequate Two boolean env13)
  bad5873 : PathP (λ _ → Two) (bop (bop b0 (bop b1 (bop b0 b0))) (bop b0 b1)) b1 → ⊥
  bad5873  p = false≢true (cong lower p)
  cut5873 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (op (var 2) (var 3)))) (op (var 3) (var 1))) , (var 1)) → ⊥
  cut5873  adequate = bad5873  (Adequate.valid adequate Two boolean env12)
  bad5874 : PathP (λ _ → Two) (bop (bop b0 (bop b0 (bop b1 b0))) (bop b0 b0)) b1 → ⊥
  bad5874  p = false≢true (cong lower p)
  cut5874 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (op (var 2) (var 3)))) (op (var 3) (var 1))) , (var 2)) → ⊥
  cut5874  adequate = bad5874  (Adequate.valid adequate Two boolean env9)
  bad5875 : PathP (λ _ → Two) (bop (bop b0 (bop b0 (bop b0 b1))) (bop b1 b0)) b1 → ⊥
  bad5875  p = false≢true (cong lower p)
  cut5875 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (op (var 2) (var 3)))) (op (var 3) (var 1))) , (var 3)) → ⊥
  cut5875  adequate = bad5875  (Adequate.valid adequate Two boolean env5)
  bad5876 : PathP (λ _ → Two) (bop (bop b0 (bop b0 (bop b0 b0))) (bop b0 b0)) b1 → ⊥
  bad5876  p = false≢true (cong lower p)
  cut5876 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (op (var 2) (var 3)))) (op (var 3) (var 1))) , (var 4)) → ⊥
  cut5876  adequate = bad5876  (Adequate.valid adequate Two boolean env10)
  bad5877 : PathP (λ _ → Two) (bop (bop b0 (bop b0 (bop b1 b1))) (bop b1 b1)) b0 → ⊥
  bad5877  p = false≢true (sym (cong lower p))
  cut5877 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (op (var 2) (var 3)))) (op (var 3) (var 2))) , (var 0)) → ⊥
  cut5877  adequate = bad5877  (Adequate.valid adequate Two boolean env8)
  bad5878 : PathP (λ _ → Two) (bop (bop b0 (bop b0 (bop b1 b1))) (bop b1 b1)) b0 → ⊥
  bad5878  p = false≢true (sym (cong lower p))
  cut5878 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (op (var 2) (var 3)))) (op (var 3) (var 2))) , (var 1)) → ⊥
  cut5878  adequate = bad5878  (Adequate.valid adequate Two boolean env8)
  bad5879 : PathP (λ _ → Two) (bop (bop b0 (bop b0 (bop b1 b0))) (bop b0 b1)) b1 → ⊥
  bad5879  p = false≢true (cong lower p)
  cut5879 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (op (var 2) (var 3)))) (op (var 3) (var 2))) , (var 2)) → ⊥
  cut5879  adequate = bad5879  (Adequate.valid adequate Two boolean env9)
  bad5880 : PathP (λ _ → Two) (bop (bop b0 (bop b0 (bop b0 b1))) (bop b1 b0)) b1 → ⊥
  bad5880  p = false≢true (cong lower p)
  cut5880 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (op (var 2) (var 3)))) (op (var 3) (var 2))) , (var 3)) → ⊥
  cut5880  adequate = bad5880  (Adequate.valid adequate Two boolean env5)
  bad5881 : PathP (λ _ → Two) (bop (bop b0 (bop b0 (bop b0 b0))) (bop b0 b0)) b1 → ⊥
  bad5881  p = false≢true (cong lower p)
  cut5881 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (op (var 2) (var 3)))) (op (var 3) (var 2))) , (var 4)) → ⊥
  cut5881  adequate = bad5881  (Adequate.valid adequate Two boolean env10)
  bad5882 : PathP (λ _ → Two) (bop (bop b0 (bop b0 (bop b0 b1))) (bop b1 b1)) b0 → ⊥
  bad5882  p = false≢true (sym (cong lower p))
  cut5882 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (op (var 2) (var 3)))) (op (var 3) (var 3))) , (var 0)) → ⊥
  cut5882  adequate = bad5882  (Adequate.valid adequate Two boolean env5)
  bad5883 : PathP (λ _ → Two) (bop (bop b0 (bop b0 (bop b0 b1))) (bop b1 b1)) b0 → ⊥
  bad5883  p = false≢true (sym (cong lower p))
  cut5883 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (op (var 2) (var 3)))) (op (var 3) (var 3))) , (var 1)) → ⊥
  cut5883  adequate = bad5883  (Adequate.valid adequate Two boolean env5)
  bad5884 : PathP (λ _ → Two) (bop (bop b0 (bop b0 (bop b0 b1))) (bop b1 b1)) b0 → ⊥
  bad5884  p = false≢true (sym (cong lower p))
  cut5884 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (op (var 2) (var 3)))) (op (var 3) (var 3))) , (var 2)) → ⊥
  cut5884  adequate = bad5884  (Adequate.valid adequate Two boolean env5)
  bad5885 : PathP (λ _ → Two) (bop (bop b1 (bop b0 (bop b0 b0))) (bop b0 b0)) b0 → ⊥
  bad5885  p = false≢true (sym (cong lower p))
  cut5885 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (op (var 2) (var 3)))) (op (var 3) (var 3))) , (var 3)) → ⊥
  cut5885  adequate = bad5885  (Adequate.valid adequate Two boolean env11)
  bad5886 : PathP (λ _ → Two) (bop (bop b0 (bop b0 (bop b0 b0))) (bop b0 b0)) b1 → ⊥
  bad5886  p = false≢true (cong lower p)
  cut5886 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (op (var 2) (var 3)))) (op (var 3) (var 3))) , (var 4)) → ⊥
  cut5886  adequate = bad5886  (Adequate.valid adequate Two boolean env10)
  bad5887 : PathP (λ _ → Two) (bop (bop b0 (bop b0 (bop b0 b1))) (bop b1 b1)) b0 → ⊥
  bad5887  p = false≢true (sym (cong lower p))
  cut5887 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (op (var 2) (var 3)))) (op (var 3) (var 4))) , (var 0)) → ⊥
  cut5887  adequate = bad5887  (Adequate.valid adequate Two boolean env15)
  bad5888 : PathP (λ _ → Two) (bop (bop b0 (bop b0 (bop b0 b1))) (bop b1 b1)) b0 → ⊥
  bad5888  p = false≢true (sym (cong lower p))
  cut5888 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (op (var 2) (var 3)))) (op (var 3) (var 4))) , (var 1)) → ⊥
  cut5888  adequate = bad5888  (Adequate.valid adequate Two boolean env15)
  bad5889 : PathP (λ _ → Two) (bop (bop b0 (bop b0 (bop b0 b1))) (bop b1 b1)) b0 → ⊥
  bad5889  p = false≢true (sym (cong lower p))
  cut5889 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (op (var 2) (var 3)))) (op (var 3) (var 4))) , (var 2)) → ⊥
  cut5889  adequate = bad5889  (Adequate.valid adequate Two boolean env15)
  bad5890 : PathP (λ _ → Two) (bop (bop b0 (bop b0 (bop b0 b1))) (bop b1 b0)) b1 → ⊥
  bad5890  p = false≢true (cong lower p)
  cut5890 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (op (var 2) (var 3)))) (op (var 3) (var 4))) , (var 3)) → ⊥
  cut5890  adequate = bad5890  (Adequate.valid adequate Two boolean env16)
  bad5891 : PathP (λ _ → Two) (bop (bop b0 (bop b0 (bop b0 b0))) (bop b0 b1)) b1 → ⊥
  bad5891  p = false≢true (cong lower p)
  cut5891 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (op (var 2) (var 3)))) (op (var 3) (var 4))) , (var 4)) → ⊥
  cut5891  adequate = bad5891  (Adequate.valid adequate Two boolean env10)
  bad5892 : PathP (λ _ → Two) (bop (bop b0 (bop b0 (bop b0 b0))) (bop b0 b0)) b1 → ⊥
  bad5892  p = false≢true (cong lower p)
  cut5892 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (op (var 2) (var 3)))) (op (var 3) (var 4))) , (var 5)) → ⊥
  cut5892  adequate = bad5892  (Adequate.valid adequate Two boolean env17)
  bad5893 : PathP (λ _ → Two) (bop (bop b1 (bop b1 (bop b0 b0))) (bop b0 b1)) b1 → ⊥
  bad5893  p = false≢true (cong lower p)
  cut5893 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (op (var 2) (var 3)))) (op (var 4) (var 0))) , (var 0)) → ⊥
  cut5893  adequate = bad5893  (Adequate.valid adequate Two boolean env19)
  bad5894 : PathP (λ _ → Two) (bop (bop b0 (bop b1 (bop b0 b0))) (bop b0 b0)) b1 → ⊥
  bad5894  p = false≢true (cong lower p)
  cut5894 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (op (var 2) (var 3)))) (op (var 4) (var 0))) , (var 1)) → ⊥
  cut5894  adequate = bad5894  (Adequate.valid adequate Two boolean env20)
  bad5895 : PathP (λ _ → Two) (bop (bop b0 (bop b0 (bop b1 b0))) (bop b0 b0)) b1 → ⊥
  bad5895  p = false≢true (cong lower p)
  cut5895 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (op (var 2) (var 3)))) (op (var 4) (var 0))) , (var 2)) → ⊥
  cut5895  adequate = bad5895  (Adequate.valid adequate Two boolean env21)
  bad5896 : PathP (λ _ → Two) (bop (bop b0 (bop b0 (bop b0 b1))) (bop b0 b0)) b1 → ⊥
  bad5896  p = false≢true (cong lower p)
  cut5896 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (op (var 2) (var 3)))) (op (var 4) (var 0))) , (var 3)) → ⊥
  cut5896  adequate = bad5896  (Adequate.valid adequate Two boolean env16)
  bad5897 : PathP (λ _ → Two) (bop (bop b0 (bop b0 (bop b0 b0))) (bop b1 b0)) b1 → ⊥
  bad5897  p = false≢true (cong lower p)
  cut5897 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (op (var 2) (var 3)))) (op (var 4) (var 0))) , (var 4)) → ⊥
  cut5897  adequate = bad5897  (Adequate.valid adequate Two boolean env10)
  bad5898 : PathP (λ _ → Two) (bop (bop b0 (bop b0 (bop b0 b0))) (bop b0 b0)) b1 → ⊥
  bad5898  p = false≢true (cong lower p)
  cut5898 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (op (var 2) (var 3)))) (op (var 4) (var 0))) , (var 5)) → ⊥
  cut5898  adequate = bad5898  (Adequate.valid adequate Two boolean env17)
  bad5899 : PathP (λ _ → Two) (bop (bop b0 (bop b1 (bop b0 b0))) (bop b1 b1)) b0 → ⊥
  bad5899  p = false≢true (sym (cong lower p))
  cut5899 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (op (var 2) (var 3)))) (op (var 4) (var 1))) , (var 0)) → ⊥
  cut5899  adequate = bad5899  (Adequate.valid adequate Two boolean env23)
  bad5900 : PathP (λ _ → Two) (bop (bop b0 (bop b1 (bop b0 b0))) (bop b0 b1)) b1 → ⊥
  bad5900  p = false≢true (cong lower p)
  cut5900 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (op (var 2) (var 3)))) (op (var 4) (var 1))) , (var 1)) → ⊥
  cut5900  adequate = bad5900  (Adequate.valid adequate Two boolean env20)
  bad5901 : PathP (λ _ → Two) (bop (bop b0 (bop b0 (bop b1 b0))) (bop b0 b0)) b1 → ⊥
  bad5901  p = false≢true (cong lower p)
  cut5901 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (op (var 2) (var 3)))) (op (var 4) (var 1))) , (var 2)) → ⊥
  cut5901  adequate = bad5901  (Adequate.valid adequate Two boolean env21)
  bad5902 : PathP (λ _ → Two) (bop (bop b0 (bop b0 (bop b0 b1))) (bop b0 b0)) b1 → ⊥
  bad5902  p = false≢true (cong lower p)
  cut5902 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (op (var 2) (var 3)))) (op (var 4) (var 1))) , (var 3)) → ⊥
  cut5902  adequate = bad5902  (Adequate.valid adequate Two boolean env16)
  bad5903 : PathP (λ _ → Two) (bop (bop b0 (bop b0 (bop b0 b0))) (bop b1 b0)) b1 → ⊥
  bad5903  p = false≢true (cong lower p)
  cut5903 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (op (var 2) (var 3)))) (op (var 4) (var 1))) , (var 4)) → ⊥
  cut5903  adequate = bad5903  (Adequate.valid adequate Two boolean env10)
  bad5904 : PathP (λ _ → Two) (bop (bop b0 (bop b0 (bop b0 b0))) (bop b0 b0)) b1 → ⊥
  bad5904  p = false≢true (cong lower p)
  cut5904 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (op (var 2) (var 3)))) (op (var 4) (var 1))) , (var 5)) → ⊥
  cut5904  adequate = bad5904  (Adequate.valid adequate Two boolean env17)
  bad5905 : PathP (λ _ → Two) (bop (bop b0 (bop b0 (bop b1 b0))) (bop b1 b1)) b0 → ⊥
  bad5905  p = false≢true (sym (cong lower p))
  cut5905 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (op (var 2) (var 3)))) (op (var 4) (var 2))) , (var 0)) → ⊥
  cut5905  adequate = bad5905  (Adequate.valid adequate Two boolean env24)
  bad5906 : PathP (λ _ → Two) (bop (bop b0 (bop b0 (bop b1 b0))) (bop b1 b1)) b0 → ⊥
  bad5906  p = false≢true (sym (cong lower p))
  cut5906 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (op (var 2) (var 3)))) (op (var 4) (var 2))) , (var 1)) → ⊥
  cut5906  adequate = bad5906  (Adequate.valid adequate Two boolean env24)
  bad5907 : PathP (λ _ → Two) (bop (bop b0 (bop b0 (bop b1 b0))) (bop b0 b1)) b1 → ⊥
  bad5907  p = false≢true (cong lower p)
  cut5907 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (op (var 2) (var 3)))) (op (var 4) (var 2))) , (var 2)) → ⊥
  cut5907  adequate = bad5907  (Adequate.valid adequate Two boolean env21)
  bad5908 : PathP (λ _ → Two) (bop (bop b0 (bop b0 (bop b0 b1))) (bop b0 b0)) b1 → ⊥
  bad5908  p = false≢true (cong lower p)
  cut5908 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (op (var 2) (var 3)))) (op (var 4) (var 2))) , (var 3)) → ⊥
  cut5908  adequate = bad5908  (Adequate.valid adequate Two boolean env16)
  bad5909 : PathP (λ _ → Two) (bop (bop b0 (bop b0 (bop b0 b0))) (bop b1 b0)) b1 → ⊥
  bad5909  p = false≢true (cong lower p)
  cut5909 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (op (var 2) (var 3)))) (op (var 4) (var 2))) , (var 4)) → ⊥
  cut5909  adequate = bad5909  (Adequate.valid adequate Two boolean env10)
  bad5910 : PathP (λ _ → Two) (bop (bop b0 (bop b0 (bop b0 b0))) (bop b0 b0)) b1 → ⊥
  bad5910  p = false≢true (cong lower p)
  cut5910 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (op (var 2) (var 3)))) (op (var 4) (var 2))) , (var 5)) → ⊥
  cut5910  adequate = bad5910  (Adequate.valid adequate Two boolean env17)
  bad5911 : PathP (λ _ → Two) (bop (bop b0 (bop b0 (bop b0 b1))) (bop b1 b1)) b0 → ⊥
  bad5911  p = false≢true (sym (cong lower p))
  cut5911 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (op (var 2) (var 3)))) (op (var 4) (var 3))) , (var 0)) → ⊥
  cut5911  adequate = bad5911  (Adequate.valid adequate Two boolean env15)
  bad5912 : PathP (λ _ → Two) (bop (bop b0 (bop b0 (bop b0 b1))) (bop b1 b1)) b0 → ⊥
  bad5912  p = false≢true (sym (cong lower p))
  cut5912 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (op (var 2) (var 3)))) (op (var 4) (var 3))) , (var 1)) → ⊥
  cut5912  adequate = bad5912  (Adequate.valid adequate Two boolean env15)
  bad5913 : PathP (λ _ → Two) (bop (bop b0 (bop b0 (bop b0 b1))) (bop b1 b1)) b0 → ⊥
  bad5913  p = false≢true (sym (cong lower p))
  cut5913 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (op (var 2) (var 3)))) (op (var 4) (var 3))) , (var 2)) → ⊥
  cut5913  adequate = bad5913  (Adequate.valid adequate Two boolean env15)
  bad5914 : PathP (λ _ → Two) (bop (bop b0 (bop b0 (bop b0 b1))) (bop b0 b1)) b1 → ⊥
  bad5914  p = false≢true (cong lower p)
  cut5914 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (op (var 2) (var 3)))) (op (var 4) (var 3))) , (var 3)) → ⊥
  cut5914  adequate = bad5914  (Adequate.valid adequate Two boolean env16)
  bad5915 : PathP (λ _ → Two) (bop (bop b0 (bop b0 (bop b0 b0))) (bop b1 b0)) b1 → ⊥
  bad5915  p = false≢true (cong lower p)
  cut5915 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (op (var 2) (var 3)))) (op (var 4) (var 3))) , (var 4)) → ⊥
  cut5915  adequate = bad5915  (Adequate.valid adequate Two boolean env10)
  bad5916 : PathP (λ _ → Two) (bop (bop b0 (bop b0 (bop b0 b0))) (bop b0 b0)) b1 → ⊥
  bad5916  p = false≢true (cong lower p)
  cut5916 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (op (var 2) (var 3)))) (op (var 4) (var 3))) , (var 5)) → ⊥
  cut5916  adequate = bad5916  (Adequate.valid adequate Two boolean env17)
  bad5917 : PathP (λ _ → Two) (bop (bop b0 (bop b0 (bop b0 b0))) (bop b1 b1)) b0 → ⊥
  bad5917  p = false≢true (sym (cong lower p))
  cut5917 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (op (var 2) (var 3)))) (op (var 4) (var 4))) , (var 0)) → ⊥
  cut5917  adequate = bad5917  (Adequate.valid adequate Two boolean env10)
  bad5918 : PathP (λ _ → Two) (bop (bop b0 (bop b0 (bop b0 b0))) (bop b1 b1)) b0 → ⊥
  bad5918  p = false≢true (sym (cong lower p))
  cut5918 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (op (var 2) (var 3)))) (op (var 4) (var 4))) , (var 1)) → ⊥
  cut5918  adequate = bad5918  (Adequate.valid adequate Two boolean env10)
  bad5919 : PathP (λ _ → Two) (bop (bop b0 (bop b0 (bop b0 b0))) (bop b1 b1)) b0 → ⊥
  bad5919  p = false≢true (sym (cong lower p))
  cut5919 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (op (var 2) (var 3)))) (op (var 4) (var 4))) , (var 2)) → ⊥
  cut5919  adequate = bad5919  (Adequate.valid adequate Two boolean env10)
  bad5920 : PathP (λ _ → Two) (bop (bop b0 (bop b0 (bop b0 b0))) (bop b1 b1)) b0 → ⊥
  bad5920  p = false≢true (sym (cong lower p))
  cut5920 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (op (var 2) (var 3)))) (op (var 4) (var 4))) , (var 3)) → ⊥
  cut5920  adequate = bad5920  (Adequate.valid adequate Two boolean env10)
  env25 : ℕ → Two
  env25 zero = b1
  env25 (suc zero) = b0
  env25 (suc (suc zero)) = b0
  env25 (suc (suc (suc zero))) = b0
  env25 (suc (suc (suc (suc zero)))) = b0
  env25 (suc (suc (suc (suc (suc rest))))) = b0
  bad5921 : PathP (λ _ → Two) (bop (bop b1 (bop b0 (bop b0 b0))) (bop b0 b0)) b0 → ⊥
  bad5921  p = false≢true (sym (cong lower p))
  cut5921 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (op (var 2) (var 3)))) (op (var 4) (var 4))) , (var 4)) → ⊥
  cut5921  adequate = bad5921  (Adequate.valid adequate Two boolean env25)
  bad5922 : PathP (λ _ → Two) (bop (bop b0 (bop b0 (bop b0 b0))) (bop b0 b0)) b1 → ⊥
  bad5922  p = false≢true (cong lower p)
  cut5922 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (op (var 2) (var 3)))) (op (var 4) (var 4))) , (var 5)) → ⊥
  cut5922  adequate = bad5922  (Adequate.valid adequate Two boolean env17)
  env26 : ℕ → Two
  env26 zero = b0
  env26 (suc zero) = b0
  env26 (suc (suc zero)) = b0
  env26 (suc (suc (suc zero))) = b0
  env26 (suc (suc (suc (suc zero)))) = b1
  env26 (suc (suc (suc (suc (suc zero))))) = b1
  env26 (suc (suc (suc (suc (suc (suc rest)))))) = b0
  bad5923 : PathP (λ _ → Two) (bop (bop b0 (bop b0 (bop b0 b0))) (bop b1 b1)) b0 → ⊥
  bad5923  p = false≢true (sym (cong lower p))
  cut5923 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (op (var 2) (var 3)))) (op (var 4) (var 5))) , (var 0)) → ⊥
  cut5923  adequate = bad5923  (Adequate.valid adequate Two boolean env26)
  bad5924 : PathP (λ _ → Two) (bop (bop b0 (bop b0 (bop b0 b0))) (bop b1 b1)) b0 → ⊥
  bad5924  p = false≢true (sym (cong lower p))
  cut5924 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (op (var 2) (var 3)))) (op (var 4) (var 5))) , (var 1)) → ⊥
  cut5924  adequate = bad5924  (Adequate.valid adequate Two boolean env26)
  bad5925 : PathP (λ _ → Two) (bop (bop b0 (bop b0 (bop b0 b0))) (bop b1 b1)) b0 → ⊥
  bad5925  p = false≢true (sym (cong lower p))
  cut5925 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (op (var 2) (var 3)))) (op (var 4) (var 5))) , (var 2)) → ⊥
  cut5925  adequate = bad5925  (Adequate.valid adequate Two boolean env26)
  bad5926 : PathP (λ _ → Two) (bop (bop b0 (bop b0 (bop b0 b0))) (bop b1 b1)) b0 → ⊥
  bad5926  p = false≢true (sym (cong lower p))
  cut5926 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (op (var 2) (var 3)))) (op (var 4) (var 5))) , (var 3)) → ⊥
  cut5926  adequate = bad5926  (Adequate.valid adequate Two boolean env26)
  env27 : ℕ → Two
  env27 zero = b0
  env27 (suc zero) = b0
  env27 (suc (suc zero)) = b0
  env27 (suc (suc (suc zero))) = b0
  env27 (suc (suc (suc (suc zero)))) = b1
  env27 (suc (suc (suc (suc (suc zero))))) = b0
  env27 (suc (suc (suc (suc (suc (suc rest)))))) = b0
  bad5927 : PathP (λ _ → Two) (bop (bop b0 (bop b0 (bop b0 b0))) (bop b1 b0)) b1 → ⊥
  bad5927  p = false≢true (cong lower p)
  cut5927 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (op (var 2) (var 3)))) (op (var 4) (var 5))) , (var 4)) → ⊥
  cut5927  adequate = bad5927  (Adequate.valid adequate Two boolean env27)
  bad5928 : PathP (λ _ → Two) (bop (bop b0 (bop b0 (bop b0 b0))) (bop b0 b1)) b1 → ⊥
  bad5928  p = false≢true (cong lower p)
  cut5928 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (op (var 2) (var 3)))) (op (var 4) (var 5))) , (var 5)) → ⊥
  cut5928  adequate = bad5928  (Adequate.valid adequate Two boolean env17)
  env28 : ℕ → Two
  env28 zero = b0
  env28 (suc zero) = b0
  env28 (suc (suc zero)) = b0
  env28 (suc (suc (suc zero))) = b0
  env28 (suc (suc (suc (suc zero)))) = b0
  env28 (suc (suc (suc (suc (suc zero))))) = b0
  env28 (suc (suc (suc (suc (suc (suc zero)))))) = b1
  env28 (suc (suc (suc (suc (suc (suc (suc rest))))))) = b0
  bad5929 : PathP (λ _ → Two) (bop (bop b0 (bop b0 (bop b0 b0))) (bop b0 b0)) b1 → ⊥
  bad5929  p = false≢true (cong lower p)
  cut5929 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (op (var 2) (var 3)))) (op (var 4) (var 5))) , (var 6)) → ⊥
  cut5929  adequate = bad5929  (Adequate.valid adequate Two boolean env28)
