{-# OPTIONS --safe --cubical --guardedness #-}
module GeneratedMinimumShape180 where
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
  holds6808 : (z0 : A1) → (mul1 (mul1 (mul1 z0 (mul1 z0 z0)) z0) (mul1 z0 z0)) ≡ z0
  holds6808 m1c0 = refl
  holds6808 m1c1 = refl
  cut6808 : Adequate {ℓ} ((op (op (op (var 0) (op (var 0) (var 0))) (var 0)) (op (var 0) (var 0))) , (var 0)) → ⊥
  cut6808  = reject1 ((op (op (op (var 0) (op (var 0) (var 0))) (var 0)) (op (var 0) (var 0))) , (var 0)) (λ env → holds6808 (env 0))
  env0 : ℕ → Two
  env0 zero = b0
  env0 (suc zero) = b1
  env0 (suc (suc rest)) = b0
  bad6809 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b0 b0)) b0) (bop b0 b0)) b1 → ⊥
  bad6809  p = false≢true (cong lower p)
  cut6809 : Adequate {ℓ} ((op (op (op (var 0) (op (var 0) (var 0))) (var 0)) (op (var 0) (var 0))) , (var 1)) → ⊥
  cut6809  adequate = bad6809  (Adequate.valid adequate Two boolean env0)
  holds6810 : (z0 z1 : A2) → (mul2 (mul2 (mul2 z0 (mul2 z0 z0)) z0) (mul2 z0 z1)) ≡ z0
  holds6810 z0 z1 = refl
  cut6810 : Adequate {ℓ} ((op (op (op (var 0) (op (var 0) (var 0))) (var 0)) (op (var 0) (var 1))) , (var 0)) → ⊥
  cut6810  = reject2 ((op (op (op (var 0) (op (var 0) (var 0))) (var 0)) (op (var 0) (var 1))) , (var 0)) (λ env → holds6810 (env 0) (env 1))
  bad6811 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b0 b0)) b0) (bop b0 b1)) b1 → ⊥
  bad6811  p = false≢true (cong lower p)
  cut6811 : Adequate {ℓ} ((op (op (op (var 0) (op (var 0) (var 0))) (var 0)) (op (var 0) (var 1))) , (var 1)) → ⊥
  cut6811  adequate = bad6811  (Adequate.valid adequate Two boolean env0)
  env1 : ℕ → Two
  env1 zero = b0
  env1 (suc zero) = b0
  env1 (suc (suc zero)) = b1
  env1 (suc (suc (suc rest))) = b0
  bad6812 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b0 b0)) b0) (bop b0 b0)) b1 → ⊥
  bad6812  p = false≢true (cong lower p)
  cut6812 : Adequate {ℓ} ((op (op (op (var 0) (op (var 0) (var 0))) (var 0)) (op (var 0) (var 1))) , (var 2)) → ⊥
  cut6812  adequate = bad6812  (Adequate.valid adequate Two boolean env1)
  holds6813 : (z0 z1 : A2) → (mul2 (mul2 (mul2 z0 (mul2 z0 z0)) z0) (mul2 z1 z0)) ≡ z0
  holds6813 z0 z1 = refl
  cut6813 : Adequate {ℓ} ((op (op (op (var 0) (op (var 0) (var 0))) (var 0)) (op (var 1) (var 0))) , (var 0)) → ⊥
  cut6813  = reject2 ((op (op (op (var 0) (op (var 0) (var 0))) (var 0)) (op (var 1) (var 0))) , (var 0)) (λ env → holds6813 (env 0) (env 1))
  bad6814 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b0 b0)) b0) (bop b1 b0)) b1 → ⊥
  bad6814  p = false≢true (cong lower p)
  cut6814 : Adequate {ℓ} ((op (op (op (var 0) (op (var 0) (var 0))) (var 0)) (op (var 1) (var 0))) , (var 1)) → ⊥
  cut6814  adequate = bad6814  (Adequate.valid adequate Two boolean env0)
  bad6815 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b0 b0)) b0) (bop b0 b0)) b1 → ⊥
  bad6815  p = false≢true (cong lower p)
  cut6815 : Adequate {ℓ} ((op (op (op (var 0) (op (var 0) (var 0))) (var 0)) (op (var 1) (var 0))) , (var 2)) → ⊥
  cut6815  adequate = bad6815  (Adequate.valid adequate Two boolean env1)
  bad6816 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b0 b0)) b0) (bop b1 b1)) b0 → ⊥
  bad6816  p = false≢true (sym (cong lower p))
  cut6816 : Adequate {ℓ} ((op (op (op (var 0) (op (var 0) (var 0))) (var 0)) (op (var 1) (var 1))) , (var 0)) → ⊥
  cut6816  adequate = bad6816  (Adequate.valid adequate Two boolean env0)
  env2 : ℕ → Two
  env2 zero = b1
  env2 (suc zero) = b0
  env2 (suc (suc rest)) = b0
  bad6817 : PathP (λ _ → Two) (bop (bop (bop b1 (bop b1 b1)) b1) (bop b0 b0)) b0 → ⊥
  bad6817  p = false≢true (sym (cong lower p))
  cut6817 : Adequate {ℓ} ((op (op (op (var 0) (op (var 0) (var 0))) (var 0)) (op (var 1) (var 1))) , (var 1)) → ⊥
  cut6817  adequate = bad6817  (Adequate.valid adequate Two boolean env2)
  bad6818 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b0 b0)) b0) (bop b0 b0)) b1 → ⊥
  bad6818  p = false≢true (cong lower p)
  cut6818 : Adequate {ℓ} ((op (op (op (var 0) (op (var 0) (var 0))) (var 0)) (op (var 1) (var 1))) , (var 2)) → ⊥
  cut6818  adequate = bad6818  (Adequate.valid adequate Two boolean env1)
  env3 : ℕ → Two
  env3 zero = b0
  env3 (suc zero) = b1
  env3 (suc (suc zero)) = b1
  env3 (suc (suc (suc rest))) = b0
  bad6819 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b0 b0)) b0) (bop b1 b1)) b0 → ⊥
  bad6819  p = false≢true (sym (cong lower p))
  cut6819 : Adequate {ℓ} ((op (op (op (var 0) (op (var 0) (var 0))) (var 0)) (op (var 1) (var 2))) , (var 0)) → ⊥
  cut6819  adequate = bad6819  (Adequate.valid adequate Two boolean env3)
  env4 : ℕ → Two
  env4 zero = b0
  env4 (suc zero) = b1
  env4 (suc (suc zero)) = b0
  env4 (suc (suc (suc rest))) = b0
  bad6820 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b0 b0)) b0) (bop b1 b0)) b1 → ⊥
  bad6820  p = false≢true (cong lower p)
  cut6820 : Adequate {ℓ} ((op (op (op (var 0) (op (var 0) (var 0))) (var 0)) (op (var 1) (var 2))) , (var 1)) → ⊥
  cut6820  adequate = bad6820  (Adequate.valid adequate Two boolean env4)
  bad6821 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b0 b0)) b0) (bop b0 b1)) b1 → ⊥
  bad6821  p = false≢true (cong lower p)
  cut6821 : Adequate {ℓ} ((op (op (op (var 0) (op (var 0) (var 0))) (var 0)) (op (var 1) (var 2))) , (var 2)) → ⊥
  cut6821  adequate = bad6821  (Adequate.valid adequate Two boolean env1)
  env5 : ℕ → Two
  env5 zero = b0
  env5 (suc zero) = b0
  env5 (suc (suc zero)) = b0
  env5 (suc (suc (suc zero))) = b1
  env5 (suc (suc (suc (suc rest)))) = b0
  bad6822 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b0 b0)) b0) (bop b0 b0)) b1 → ⊥
  bad6822  p = false≢true (cong lower p)
  cut6822 : Adequate {ℓ} ((op (op (op (var 0) (op (var 0) (var 0))) (var 0)) (op (var 1) (var 2))) , (var 3)) → ⊥
  cut6822  adequate = bad6822  (Adequate.valid adequate Two boolean env5)
  bad6823 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b0 b0)) b1) (bop b0 b0)) b0 → ⊥
  bad6823  p = false≢true (sym (cong lower p))
  cut6823 : Adequate {ℓ} ((op (op (op (var 0) (op (var 0) (var 0))) (var 1)) (op (var 0) (var 0))) , (var 0)) → ⊥
  cut6823  adequate = bad6823  (Adequate.valid adequate Two boolean env0)
  bad6824 : PathP (λ _ → Two) (bop (bop (bop b1 (bop b1 b1)) b0) (bop b1 b1)) b0 → ⊥
  bad6824  p = false≢true (sym (cong lower p))
  cut6824 : Adequate {ℓ} ((op (op (op (var 0) (op (var 0) (var 0))) (var 1)) (op (var 0) (var 0))) , (var 1)) → ⊥
  cut6824  adequate = bad6824  (Adequate.valid adequate Two boolean env2)
  bad6825 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b0 b0)) b0) (bop b0 b0)) b1 → ⊥
  bad6825  p = false≢true (cong lower p)
  cut6825 : Adequate {ℓ} ((op (op (op (var 0) (op (var 0) (var 0))) (var 1)) (op (var 0) (var 0))) , (var 2)) → ⊥
  cut6825  adequate = bad6825  (Adequate.valid adequate Two boolean env1)
  bad6826 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b0 b0)) b1) (bop b0 b1)) b0 → ⊥
  bad6826  p = false≢true (sym (cong lower p))
  cut6826 : Adequate {ℓ} ((op (op (op (var 0) (op (var 0) (var 0))) (var 1)) (op (var 0) (var 1))) , (var 0)) → ⊥
  cut6826  adequate = bad6826  (Adequate.valid adequate Two boolean env0)
  holds6827 : (z0 z1 : A3) → (mul3 (mul3 (mul3 z0 (mul3 z0 z0)) z1) (mul3 z0 z1)) ≡ z1
  holds6827 z0 z1 = refl
  cut6827 : Adequate {ℓ} ((op (op (op (var 0) (op (var 0) (var 0))) (var 1)) (op (var 0) (var 1))) , (var 1)) → ⊥
  cut6827  = reject3 ((op (op (op (var 0) (op (var 0) (var 0))) (var 1)) (op (var 0) (var 1))) , (var 1)) (λ env → holds6827 (env 0) (env 1))
  bad6828 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b0 b0)) b0) (bop b0 b0)) b1 → ⊥
  bad6828  p = false≢true (cong lower p)
  cut6828 : Adequate {ℓ} ((op (op (op (var 0) (op (var 0) (var 0))) (var 1)) (op (var 0) (var 1))) , (var 2)) → ⊥
  cut6828  adequate = bad6828  (Adequate.valid adequate Two boolean env1)
  bad6829 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b0 b0)) b1) (bop b0 b0)) b0 → ⊥
  bad6829  p = false≢true (sym (cong lower p))
  cut6829 : Adequate {ℓ} ((op (op (op (var 0) (op (var 0) (var 0))) (var 1)) (op (var 0) (var 2))) , (var 0)) → ⊥
  cut6829  adequate = bad6829  (Adequate.valid adequate Two boolean env4)
  env6 : ℕ → Two
  env6 zero = b1
  env6 (suc zero) = b0
  env6 (suc (suc zero)) = b1
  env6 (suc (suc (suc rest))) = b0
  bad6830 : PathP (λ _ → Two) (bop (bop (bop b1 (bop b1 b1)) b0) (bop b1 b1)) b0 → ⊥
  bad6830  p = false≢true (sym (cong lower p))
  cut6830 : Adequate {ℓ} ((op (op (op (var 0) (op (var 0) (var 0))) (var 1)) (op (var 0) (var 2))) , (var 1)) → ⊥
  cut6830  adequate = bad6830  (Adequate.valid adequate Two boolean env6)
  bad6831 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b0 b0)) b0) (bop b0 b1)) b1 → ⊥
  bad6831  p = false≢true (cong lower p)
  cut6831 : Adequate {ℓ} ((op (op (op (var 0) (op (var 0) (var 0))) (var 1)) (op (var 0) (var 2))) , (var 2)) → ⊥
  cut6831  adequate = bad6831  (Adequate.valid adequate Two boolean env1)
  bad6832 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b0 b0)) b0) (bop b0 b0)) b1 → ⊥
  bad6832  p = false≢true (cong lower p)
  cut6832 : Adequate {ℓ} ((op (op (op (var 0) (op (var 0) (var 0))) (var 1)) (op (var 0) (var 2))) , (var 3)) → ⊥
  cut6832  adequate = bad6832  (Adequate.valid adequate Two boolean env5)
  bad6833 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b0 b0)) b1) (bop b1 b0)) b0 → ⊥
  bad6833  p = false≢true (sym (cong lower p))
  cut6833 : Adequate {ℓ} ((op (op (op (var 0) (op (var 0) (var 0))) (var 1)) (op (var 1) (var 0))) , (var 0)) → ⊥
  cut6833  adequate = bad6833  (Adequate.valid adequate Two boolean env0)
  holds6834 : (z0 z1 : A8) → (mul8 (mul8 (mul8 z0 (mul8 z0 z0)) z1) (mul8 z1 z0)) ≡ z1
  holds6834 m8c0 m8c0 = refl
  holds6834 m8c0 m8c1 = refl
  holds6834 m8c0 m8c2 = refl
  holds6834 m8c1 m8c0 = refl
  holds6834 m8c1 m8c1 = refl
  holds6834 m8c1 m8c2 = refl
  holds6834 m8c2 m8c0 = refl
  holds6834 m8c2 m8c1 = refl
  holds6834 m8c2 m8c2 = refl
  cut6834 : Adequate {ℓ} ((op (op (op (var 0) (op (var 0) (var 0))) (var 1)) (op (var 1) (var 0))) , (var 1)) → ⊥
  cut6834  = reject8 ((op (op (op (var 0) (op (var 0) (var 0))) (var 1)) (op (var 1) (var 0))) , (var 1)) (λ env → holds6834 (env 0) (env 1))
  bad6835 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b0 b0)) b0) (bop b0 b0)) b1 → ⊥
  bad6835  p = false≢true (cong lower p)
  cut6835 : Adequate {ℓ} ((op (op (op (var 0) (op (var 0) (var 0))) (var 1)) (op (var 1) (var 0))) , (var 2)) → ⊥
  cut6835  adequate = bad6835  (Adequate.valid adequate Two boolean env1)
  bad6836 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b0 b0)) b1) (bop b1 b1)) b0 → ⊥
  bad6836  p = false≢true (sym (cong lower p))
  cut6836 : Adequate {ℓ} ((op (op (op (var 0) (op (var 0) (var 0))) (var 1)) (op (var 1) (var 1))) , (var 0)) → ⊥
  cut6836  adequate = bad6836  (Adequate.valid adequate Two boolean env0)
  holds6837 : (z0 z1 : A3) → (mul3 (mul3 (mul3 z0 (mul3 z0 z0)) z1) (mul3 z1 z1)) ≡ z1
  holds6837 z0 z1 = refl
  cut6837 : Adequate {ℓ} ((op (op (op (var 0) (op (var 0) (var 0))) (var 1)) (op (var 1) (var 1))) , (var 1)) → ⊥
  cut6837  = reject3 ((op (op (op (var 0) (op (var 0) (var 0))) (var 1)) (op (var 1) (var 1))) , (var 1)) (λ env → holds6837 (env 0) (env 1))
  bad6838 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b0 b0)) b0) (bop b0 b0)) b1 → ⊥
  bad6838  p = false≢true (cong lower p)
  cut6838 : Adequate {ℓ} ((op (op (op (var 0) (op (var 0) (var 0))) (var 1)) (op (var 1) (var 1))) , (var 2)) → ⊥
  cut6838  adequate = bad6838  (Adequate.valid adequate Two boolean env1)
  bad6839 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b0 b0)) b1) (bop b1 b0)) b0 → ⊥
  bad6839  p = false≢true (sym (cong lower p))
  cut6839 : Adequate {ℓ} ((op (op (op (var 0) (op (var 0) (var 0))) (var 1)) (op (var 1) (var 2))) , (var 0)) → ⊥
  cut6839  adequate = bad6839  (Adequate.valid adequate Two boolean env4)
  holds6840 : (z0 z1 z2 : A11) → (mul11 (mul11 (mul11 z0 (mul11 z0 z0)) z1) (mul11 z1 z2)) ≡ z1
  holds6840 m11c0 m11c0 m11c0 = refl
  holds6840 m11c0 m11c0 m11c1 = refl
  holds6840 m11c0 m11c0 m11c2 = refl
  holds6840 m11c0 m11c1 z2 = refl
  holds6840 m11c0 m11c2 z2 = refl
  holds6840 m11c1 m11c0 m11c0 = refl
  holds6840 m11c1 m11c0 m11c1 = refl
  holds6840 m11c1 m11c0 m11c2 = refl
  holds6840 m11c1 m11c1 z2 = refl
  holds6840 m11c1 m11c2 z2 = refl
  holds6840 m11c2 m11c0 m11c0 = refl
  holds6840 m11c2 m11c0 m11c1 = refl
  holds6840 m11c2 m11c0 m11c2 = refl
  holds6840 m11c2 m11c1 z2 = refl
  holds6840 m11c2 m11c2 z2 = refl
  cut6840 : Adequate {ℓ} ((op (op (op (var 0) (op (var 0) (var 0))) (var 1)) (op (var 1) (var 2))) , (var 1)) → ⊥
  cut6840  = reject11 ((op (op (op (var 0) (op (var 0) (var 0))) (var 1)) (op (var 1) (var 2))) , (var 1)) (λ env → holds6840 (env 0) (env 1) (env 2))
  bad6841 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b0 b0)) b0) (bop b0 b1)) b1 → ⊥
  bad6841  p = false≢true (cong lower p)
  cut6841 : Adequate {ℓ} ((op (op (op (var 0) (op (var 0) (var 0))) (var 1)) (op (var 1) (var 2))) , (var 2)) → ⊥
  cut6841  adequate = bad6841  (Adequate.valid adequate Two boolean env1)
  bad6842 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b0 b0)) b0) (bop b0 b0)) b1 → ⊥
  bad6842  p = false≢true (cong lower p)
  cut6842 : Adequate {ℓ} ((op (op (op (var 0) (op (var 0) (var 0))) (var 1)) (op (var 1) (var 2))) , (var 3)) → ⊥
  cut6842  adequate = bad6842  (Adequate.valid adequate Two boolean env5)
  bad6843 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b0 b0)) b1) (bop b0 b0)) b0 → ⊥
  bad6843  p = false≢true (sym (cong lower p))
  cut6843 : Adequate {ℓ} ((op (op (op (var 0) (op (var 0) (var 0))) (var 1)) (op (var 2) (var 0))) , (var 0)) → ⊥
  cut6843  adequate = bad6843  (Adequate.valid adequate Two boolean env4)
  bad6844 : PathP (λ _ → Two) (bop (bop (bop b1 (bop b1 b1)) b0) (bop b1 b1)) b0 → ⊥
  bad6844  p = false≢true (sym (cong lower p))
  cut6844 : Adequate {ℓ} ((op (op (op (var 0) (op (var 0) (var 0))) (var 1)) (op (var 2) (var 0))) , (var 1)) → ⊥
  cut6844  adequate = bad6844  (Adequate.valid adequate Two boolean env6)
  bad6845 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b0 b0)) b0) (bop b1 b0)) b1 → ⊥
  bad6845  p = false≢true (cong lower p)
  cut6845 : Adequate {ℓ} ((op (op (op (var 0) (op (var 0) (var 0))) (var 1)) (op (var 2) (var 0))) , (var 2)) → ⊥
  cut6845  adequate = bad6845  (Adequate.valid adequate Two boolean env1)
  bad6846 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b0 b0)) b0) (bop b0 b0)) b1 → ⊥
  bad6846  p = false≢true (cong lower p)
  cut6846 : Adequate {ℓ} ((op (op (op (var 0) (op (var 0) (var 0))) (var 1)) (op (var 2) (var 0))) , (var 3)) → ⊥
  cut6846  adequate = bad6846  (Adequate.valid adequate Two boolean env5)
  bad6847 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b0 b0)) b1) (bop b0 b1)) b0 → ⊥
  bad6847  p = false≢true (sym (cong lower p))
  cut6847 : Adequate {ℓ} ((op (op (op (var 0) (op (var 0) (var 0))) (var 1)) (op (var 2) (var 1))) , (var 0)) → ⊥
  cut6847  adequate = bad6847  (Adequate.valid adequate Two boolean env4)
  holds6848 : (z0 z1 z2 : A3) → (mul3 (mul3 (mul3 z0 (mul3 z0 z0)) z1) (mul3 z2 z1)) ≡ z1
  holds6848 z0 z1 z2 = refl
  cut6848 : Adequate {ℓ} ((op (op (op (var 0) (op (var 0) (var 0))) (var 1)) (op (var 2) (var 1))) , (var 1)) → ⊥
  cut6848  = reject3 ((op (op (op (var 0) (op (var 0) (var 0))) (var 1)) (op (var 2) (var 1))) , (var 1)) (λ env → holds6848 (env 0) (env 1) (env 2))
  bad6849 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b0 b0)) b0) (bop b1 b0)) b1 → ⊥
  bad6849  p = false≢true (cong lower p)
  cut6849 : Adequate {ℓ} ((op (op (op (var 0) (op (var 0) (var 0))) (var 1)) (op (var 2) (var 1))) , (var 2)) → ⊥
  cut6849  adequate = bad6849  (Adequate.valid adequate Two boolean env1)
  bad6850 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b0 b0)) b0) (bop b0 b0)) b1 → ⊥
  bad6850  p = false≢true (cong lower p)
  cut6850 : Adequate {ℓ} ((op (op (op (var 0) (op (var 0) (var 0))) (var 1)) (op (var 2) (var 1))) , (var 3)) → ⊥
  cut6850  adequate = bad6850  (Adequate.valid adequate Two boolean env5)
  bad6851 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b0 b0)) b0) (bop b1 b1)) b0 → ⊥
  bad6851  p = false≢true (sym (cong lower p))
  cut6851 : Adequate {ℓ} ((op (op (op (var 0) (op (var 0) (var 0))) (var 1)) (op (var 2) (var 2))) , (var 0)) → ⊥
  cut6851  adequate = bad6851  (Adequate.valid adequate Two boolean env1)
  bad6852 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b0 b0)) b0) (bop b1 b1)) b0 → ⊥
  bad6852  p = false≢true (sym (cong lower p))
  cut6852 : Adequate {ℓ} ((op (op (op (var 0) (op (var 0) (var 0))) (var 1)) (op (var 2) (var 2))) , (var 1)) → ⊥
  cut6852  adequate = bad6852  (Adequate.valid adequate Two boolean env1)
  bad6853 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b0 b0)) b1) (bop b0 b0)) b0 → ⊥
  bad6853  p = false≢true (sym (cong lower p))
  cut6853 : Adequate {ℓ} ((op (op (op (var 0) (op (var 0) (var 0))) (var 1)) (op (var 2) (var 2))) , (var 2)) → ⊥
  cut6853  adequate = bad6853  (Adequate.valid adequate Two boolean env4)
  bad6854 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b0 b0)) b0) (bop b0 b0)) b1 → ⊥
  bad6854  p = false≢true (cong lower p)
  cut6854 : Adequate {ℓ} ((op (op (op (var 0) (op (var 0) (var 0))) (var 1)) (op (var 2) (var 2))) , (var 3)) → ⊥
  cut6854  adequate = bad6854  (Adequate.valid adequate Two boolean env5)
  env7 : ℕ → Two
  env7 zero = b0
  env7 (suc zero) = b0
  env7 (suc (suc zero)) = b1
  env7 (suc (suc (suc zero))) = b1
  env7 (suc (suc (suc (suc rest)))) = b0
  bad6855 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b0 b0)) b0) (bop b1 b1)) b0 → ⊥
  bad6855  p = false≢true (sym (cong lower p))
  cut6855 : Adequate {ℓ} ((op (op (op (var 0) (op (var 0) (var 0))) (var 1)) (op (var 2) (var 3))) , (var 0)) → ⊥
  cut6855  adequate = bad6855  (Adequate.valid adequate Two boolean env7)
  bad6856 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b0 b0)) b0) (bop b1 b1)) b0 → ⊥
  bad6856  p = false≢true (sym (cong lower p))
  cut6856 : Adequate {ℓ} ((op (op (op (var 0) (op (var 0) (var 0))) (var 1)) (op (var 2) (var 3))) , (var 1)) → ⊥
  cut6856  adequate = bad6856  (Adequate.valid adequate Two boolean env7)
  env8 : ℕ → Two
  env8 zero = b0
  env8 (suc zero) = b0
  env8 (suc (suc zero)) = b1
  env8 (suc (suc (suc zero))) = b0
  env8 (suc (suc (suc (suc rest)))) = b0
  bad6857 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b0 b0)) b0) (bop b1 b0)) b1 → ⊥
  bad6857  p = false≢true (cong lower p)
  cut6857 : Adequate {ℓ} ((op (op (op (var 0) (op (var 0) (var 0))) (var 1)) (op (var 2) (var 3))) , (var 2)) → ⊥
  cut6857  adequate = bad6857  (Adequate.valid adequate Two boolean env8)
  bad6858 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b0 b0)) b0) (bop b0 b1)) b1 → ⊥
  bad6858  p = false≢true (cong lower p)
  cut6858 : Adequate {ℓ} ((op (op (op (var 0) (op (var 0) (var 0))) (var 1)) (op (var 2) (var 3))) , (var 3)) → ⊥
  cut6858  adequate = bad6858  (Adequate.valid adequate Two boolean env5)
  env9 : ℕ → Two
  env9 zero = b0
  env9 (suc zero) = b0
  env9 (suc (suc zero)) = b0
  env9 (suc (suc (suc zero))) = b0
  env9 (suc (suc (suc (suc zero)))) = b1
  env9 (suc (suc (suc (suc (suc rest))))) = b0
  bad6859 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b0 b0)) b0) (bop b0 b0)) b1 → ⊥
  bad6859  p = false≢true (cong lower p)
  cut6859 : Adequate {ℓ} ((op (op (op (var 0) (op (var 0) (var 0))) (var 1)) (op (var 2) (var 3))) , (var 4)) → ⊥
  cut6859  adequate = bad6859  (Adequate.valid adequate Two boolean env9)
  holds6860 : (z0 z1 : A2) → (mul2 (mul2 (mul2 z0 (mul2 z0 z1)) z0) (mul2 z0 z0)) ≡ z0
  holds6860 z0 z1 = refl
  cut6860 : Adequate {ℓ} ((op (op (op (var 0) (op (var 0) (var 1))) (var 0)) (op (var 0) (var 0))) , (var 0)) → ⊥
  cut6860  = reject2 ((op (op (op (var 0) (op (var 0) (var 1))) (var 0)) (op (var 0) (var 0))) , (var 0)) (λ env → holds6860 (env 0) (env 1))
  bad6861 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b0 b1)) b0) (bop b0 b0)) b1 → ⊥
  bad6861  p = false≢true (cong lower p)
  cut6861 : Adequate {ℓ} ((op (op (op (var 0) (op (var 0) (var 1))) (var 0)) (op (var 0) (var 0))) , (var 1)) → ⊥
  cut6861  adequate = bad6861  (Adequate.valid adequate Two boolean env0)
  bad6862 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b0 b0)) b0) (bop b0 b0)) b1 → ⊥
  bad6862  p = false≢true (cong lower p)
  cut6862 : Adequate {ℓ} ((op (op (op (var 0) (op (var 0) (var 1))) (var 0)) (op (var 0) (var 0))) , (var 2)) → ⊥
  cut6862  adequate = bad6862  (Adequate.valid adequate Two boolean env1)
  bad6863 : PathP (λ _ → Two) (bop (bop (bop b1 (bop b1 b0)) b1) (bop b1 b0)) b1 → ⊥
  bad6863  p = false≢true (cong lower p)
  cut6863 : Adequate {ℓ} ((op (op (op (var 0) (op (var 0) (var 1))) (var 0)) (op (var 0) (var 1))) , (var 0)) → ⊥
  cut6863  adequate = bad6863  (Adequate.valid adequate Two boolean env2)
  bad6864 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b0 b1)) b0) (bop b0 b1)) b1 → ⊥
  bad6864  p = false≢true (cong lower p)
  cut6864 : Adequate {ℓ} ((op (op (op (var 0) (op (var 0) (var 1))) (var 0)) (op (var 0) (var 1))) , (var 1)) → ⊥
  cut6864  adequate = bad6864  (Adequate.valid adequate Two boolean env0)
  bad6865 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b0 b0)) b0) (bop b0 b0)) b1 → ⊥
  bad6865  p = false≢true (cong lower p)
  cut6865 : Adequate {ℓ} ((op (op (op (var 0) (op (var 0) (var 1))) (var 0)) (op (var 0) (var 1))) , (var 2)) → ⊥
  cut6865  adequate = bad6865  (Adequate.valid adequate Two boolean env1)
  env10 : ℕ → Two
  env10 zero = b1
  env10 (suc zero) = b0
  env10 (suc (suc zero)) = b0
  env10 (suc (suc (suc rest))) = b0
  bad6866 : PathP (λ _ → Two) (bop (bop (bop b1 (bop b1 b0)) b1) (bop b1 b0)) b1 → ⊥
  bad6866  p = false≢true (cong lower p)
  cut6866 : Adequate {ℓ} ((op (op (op (var 0) (op (var 0) (var 1))) (var 0)) (op (var 0) (var 2))) , (var 0)) → ⊥
  cut6866  adequate = bad6866  (Adequate.valid adequate Two boolean env10)
  bad6867 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b0 b1)) b0) (bop b0 b0)) b1 → ⊥
  bad6867  p = false≢true (cong lower p)
  cut6867 : Adequate {ℓ} ((op (op (op (var 0) (op (var 0) (var 1))) (var 0)) (op (var 0) (var 2))) , (var 1)) → ⊥
  cut6867  adequate = bad6867  (Adequate.valid adequate Two boolean env4)
  bad6868 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b0 b0)) b0) (bop b0 b1)) b1 → ⊥
  bad6868  p = false≢true (cong lower p)
  cut6868 : Adequate {ℓ} ((op (op (op (var 0) (op (var 0) (var 1))) (var 0)) (op (var 0) (var 2))) , (var 2)) → ⊥
  cut6868  adequate = bad6868  (Adequate.valid adequate Two boolean env1)
  bad6869 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b0 b0)) b0) (bop b0 b0)) b1 → ⊥
  bad6869  p = false≢true (cong lower p)
  cut6869 : Adequate {ℓ} ((op (op (op (var 0) (op (var 0) (var 1))) (var 0)) (op (var 0) (var 2))) , (var 3)) → ⊥
  cut6869  adequate = bad6869  (Adequate.valid adequate Two boolean env5)
  bad6870 : PathP (λ _ → Two) (bop (bop (bop b1 (bop b1 b0)) b1) (bop b0 b1)) b1 → ⊥
  bad6870  p = false≢true (cong lower p)
  cut6870 : Adequate {ℓ} ((op (op (op (var 0) (op (var 0) (var 1))) (var 0)) (op (var 1) (var 0))) , (var 0)) → ⊥
  cut6870  adequate = bad6870  (Adequate.valid adequate Two boolean env2)
  bad6871 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b0 b1)) b0) (bop b1 b0)) b1 → ⊥
  bad6871  p = false≢true (cong lower p)
  cut6871 : Adequate {ℓ} ((op (op (op (var 0) (op (var 0) (var 1))) (var 0)) (op (var 1) (var 0))) , (var 1)) → ⊥
  cut6871  adequate = bad6871  (Adequate.valid adequate Two boolean env0)
  bad6872 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b0 b0)) b0) (bop b0 b0)) b1 → ⊥
  bad6872  p = false≢true (cong lower p)
  cut6872 : Adequate {ℓ} ((op (op (op (var 0) (op (var 0) (var 1))) (var 0)) (op (var 1) (var 0))) , (var 2)) → ⊥
  cut6872  adequate = bad6872  (Adequate.valid adequate Two boolean env1)
  bad6873 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b0 b1)) b0) (bop b1 b1)) b0 → ⊥
  bad6873  p = false≢true (sym (cong lower p))
  cut6873 : Adequate {ℓ} ((op (op (op (var 0) (op (var 0) (var 1))) (var 0)) (op (var 1) (var 1))) , (var 0)) → ⊥
  cut6873  adequate = bad6873  (Adequate.valid adequate Two boolean env0)
  holds6874 : (z0 z1 : A3) → (mul3 (mul3 (mul3 z0 (mul3 z0 z1)) z0) (mul3 z1 z1)) ≡ z1
  holds6874 z0 z1 = refl
  cut6874 : Adequate {ℓ} ((op (op (op (var 0) (op (var 0) (var 1))) (var 0)) (op (var 1) (var 1))) , (var 1)) → ⊥
  cut6874  = reject3 ((op (op (op (var 0) (op (var 0) (var 1))) (var 0)) (op (var 1) (var 1))) , (var 1)) (λ env → holds6874 (env 0) (env 1))
  bad6875 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b0 b0)) b0) (bop b0 b0)) b1 → ⊥
  bad6875  p = false≢true (cong lower p)
  cut6875 : Adequate {ℓ} ((op (op (op (var 0) (op (var 0) (var 1))) (var 0)) (op (var 1) (var 1))) , (var 2)) → ⊥
  cut6875  adequate = bad6875  (Adequate.valid adequate Two boolean env1)
  bad6876 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b0 b1)) b0) (bop b1 b1)) b0 → ⊥
  bad6876  p = false≢true (sym (cong lower p))
  cut6876 : Adequate {ℓ} ((op (op (op (var 0) (op (var 0) (var 1))) (var 0)) (op (var 1) (var 2))) , (var 0)) → ⊥
  cut6876  adequate = bad6876  (Adequate.valid adequate Two boolean env3)
  bad6877 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b0 b1)) b0) (bop b1 b0)) b1 → ⊥
  bad6877  p = false≢true (cong lower p)
  cut6877 : Adequate {ℓ} ((op (op (op (var 0) (op (var 0) (var 1))) (var 0)) (op (var 1) (var 2))) , (var 1)) → ⊥
  cut6877  adequate = bad6877  (Adequate.valid adequate Two boolean env4)
  bad6878 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b0 b0)) b0) (bop b0 b1)) b1 → ⊥
  bad6878  p = false≢true (cong lower p)
  cut6878 : Adequate {ℓ} ((op (op (op (var 0) (op (var 0) (var 1))) (var 0)) (op (var 1) (var 2))) , (var 2)) → ⊥
  cut6878  adequate = bad6878  (Adequate.valid adequate Two boolean env1)
  bad6879 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b0 b0)) b0) (bop b0 b0)) b1 → ⊥
  bad6879  p = false≢true (cong lower p)
  cut6879 : Adequate {ℓ} ((op (op (op (var 0) (op (var 0) (var 1))) (var 0)) (op (var 1) (var 2))) , (var 3)) → ⊥
  cut6879  adequate = bad6879  (Adequate.valid adequate Two boolean env5)
  bad6880 : PathP (λ _ → Two) (bop (bop (bop b1 (bop b1 b0)) b1) (bop b0 b1)) b1 → ⊥
  bad6880  p = false≢true (cong lower p)
  cut6880 : Adequate {ℓ} ((op (op (op (var 0) (op (var 0) (var 1))) (var 0)) (op (var 2) (var 0))) , (var 0)) → ⊥
  cut6880  adequate = bad6880  (Adequate.valid adequate Two boolean env10)
  bad6881 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b0 b1)) b0) (bop b0 b0)) b1 → ⊥
  bad6881  p = false≢true (cong lower p)
  cut6881 : Adequate {ℓ} ((op (op (op (var 0) (op (var 0) (var 1))) (var 0)) (op (var 2) (var 0))) , (var 1)) → ⊥
  cut6881  adequate = bad6881  (Adequate.valid adequate Two boolean env4)
  bad6882 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b0 b0)) b0) (bop b1 b0)) b1 → ⊥
  bad6882  p = false≢true (cong lower p)
  cut6882 : Adequate {ℓ} ((op (op (op (var 0) (op (var 0) (var 1))) (var 0)) (op (var 2) (var 0))) , (var 2)) → ⊥
  cut6882  adequate = bad6882  (Adequate.valid adequate Two boolean env1)
  bad6883 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b0 b0)) b0) (bop b0 b0)) b1 → ⊥
  bad6883  p = false≢true (cong lower p)
  cut6883 : Adequate {ℓ} ((op (op (op (var 0) (op (var 0) (var 1))) (var 0)) (op (var 2) (var 0))) , (var 3)) → ⊥
  cut6883  adequate = bad6883  (Adequate.valid adequate Two boolean env5)
  bad6884 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b0 b1)) b0) (bop b1 b1)) b0 → ⊥
  bad6884  p = false≢true (sym (cong lower p))
  cut6884 : Adequate {ℓ} ((op (op (op (var 0) (op (var 0) (var 1))) (var 0)) (op (var 2) (var 1))) , (var 0)) → ⊥
  cut6884  adequate = bad6884  (Adequate.valid adequate Two boolean env3)
  bad6885 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b0 b1)) b0) (bop b0 b1)) b1 → ⊥
  bad6885  p = false≢true (cong lower p)
  cut6885 : Adequate {ℓ} ((op (op (op (var 0) (op (var 0) (var 1))) (var 0)) (op (var 2) (var 1))) , (var 1)) → ⊥
  cut6885  adequate = bad6885  (Adequate.valid adequate Two boolean env4)
  bad6886 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b0 b0)) b0) (bop b1 b0)) b1 → ⊥
  bad6886  p = false≢true (cong lower p)
  cut6886 : Adequate {ℓ} ((op (op (op (var 0) (op (var 0) (var 1))) (var 0)) (op (var 2) (var 1))) , (var 2)) → ⊥
  cut6886  adequate = bad6886  (Adequate.valid adequate Two boolean env1)
  bad6887 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b0 b0)) b0) (bop b0 b0)) b1 → ⊥
  bad6887  p = false≢true (cong lower p)
  cut6887 : Adequate {ℓ} ((op (op (op (var 0) (op (var 0) (var 1))) (var 0)) (op (var 2) (var 1))) , (var 3)) → ⊥
  cut6887  adequate = bad6887  (Adequate.valid adequate Two boolean env5)
  bad6888 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b0 b0)) b0) (bop b1 b1)) b0 → ⊥
  bad6888  p = false≢true (sym (cong lower p))
  cut6888 : Adequate {ℓ} ((op (op (op (var 0) (op (var 0) (var 1))) (var 0)) (op (var 2) (var 2))) , (var 0)) → ⊥
  cut6888  adequate = bad6888  (Adequate.valid adequate Two boolean env1)
  bad6889 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b0 b0)) b0) (bop b1 b1)) b0 → ⊥
  bad6889  p = false≢true (sym (cong lower p))
  cut6889 : Adequate {ℓ} ((op (op (op (var 0) (op (var 0) (var 1))) (var 0)) (op (var 2) (var 2))) , (var 1)) → ⊥
  cut6889  adequate = bad6889  (Adequate.valid adequate Two boolean env1)
  env11 : ℕ → Two
  env11 zero = b1
  env11 (suc zero) = b1
  env11 (suc (suc zero)) = b0
  env11 (suc (suc (suc rest))) = b0
  bad6890 : PathP (λ _ → Two) (bop (bop (bop b1 (bop b1 b1)) b1) (bop b0 b0)) b0 → ⊥
  bad6890  p = false≢true (sym (cong lower p))
  cut6890 : Adequate {ℓ} ((op (op (op (var 0) (op (var 0) (var 1))) (var 0)) (op (var 2) (var 2))) , (var 2)) → ⊥
  cut6890  adequate = bad6890  (Adequate.valid adequate Two boolean env11)
  bad6891 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b0 b0)) b0) (bop b0 b0)) b1 → ⊥
  bad6891  p = false≢true (cong lower p)
  cut6891 : Adequate {ℓ} ((op (op (op (var 0) (op (var 0) (var 1))) (var 0)) (op (var 2) (var 2))) , (var 3)) → ⊥
  cut6891  adequate = bad6891  (Adequate.valid adequate Two boolean env5)
  bad6892 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b0 b0)) b0) (bop b1 b1)) b0 → ⊥
  bad6892  p = false≢true (sym (cong lower p))
  cut6892 : Adequate {ℓ} ((op (op (op (var 0) (op (var 0) (var 1))) (var 0)) (op (var 2) (var 3))) , (var 0)) → ⊥
  cut6892  adequate = bad6892  (Adequate.valid adequate Two boolean env7)
  bad6893 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b0 b0)) b0) (bop b1 b1)) b0 → ⊥
  bad6893  p = false≢true (sym (cong lower p))
  cut6893 : Adequate {ℓ} ((op (op (op (var 0) (op (var 0) (var 1))) (var 0)) (op (var 2) (var 3))) , (var 1)) → ⊥
  cut6893  adequate = bad6893  (Adequate.valid adequate Two boolean env7)
  bad6894 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b0 b0)) b0) (bop b1 b0)) b1 → ⊥
  bad6894  p = false≢true (cong lower p)
  cut6894 : Adequate {ℓ} ((op (op (op (var 0) (op (var 0) (var 1))) (var 0)) (op (var 2) (var 3))) , (var 2)) → ⊥
  cut6894  adequate = bad6894  (Adequate.valid adequate Two boolean env8)
  bad6895 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b0 b0)) b0) (bop b0 b1)) b1 → ⊥
  bad6895  p = false≢true (cong lower p)
  cut6895 : Adequate {ℓ} ((op (op (op (var 0) (op (var 0) (var 1))) (var 0)) (op (var 2) (var 3))) , (var 3)) → ⊥
  cut6895  adequate = bad6895  (Adequate.valid adequate Two boolean env5)
  bad6896 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b0 b0)) b0) (bop b0 b0)) b1 → ⊥
  bad6896  p = false≢true (cong lower p)
  cut6896 : Adequate {ℓ} ((op (op (op (var 0) (op (var 0) (var 1))) (var 0)) (op (var 2) (var 3))) , (var 4)) → ⊥
  cut6896  adequate = bad6896  (Adequate.valid adequate Two boolean env9)
  bad6897 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b0 b1)) b1) (bop b0 b0)) b0 → ⊥
  bad6897  p = false≢true (sym (cong lower p))
  cut6897 : Adequate {ℓ} ((op (op (op (var 0) (op (var 0) (var 1))) (var 1)) (op (var 0) (var 0))) , (var 0)) → ⊥
  cut6897  adequate = bad6897  (Adequate.valid adequate Two boolean env0)
  bad6898 : PathP (λ _ → Two) (bop (bop (bop b1 (bop b1 b0)) b0) (bop b1 b1)) b0 → ⊥
  bad6898  p = false≢true (sym (cong lower p))
  cut6898 : Adequate {ℓ} ((op (op (op (var 0) (op (var 0) (var 1))) (var 1)) (op (var 0) (var 0))) , (var 1)) → ⊥
  cut6898  adequate = bad6898  (Adequate.valid adequate Two boolean env2)
  bad6899 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b0 b0)) b0) (bop b0 b0)) b1 → ⊥
  bad6899  p = false≢true (cong lower p)
  cut6899 : Adequate {ℓ} ((op (op (op (var 0) (op (var 0) (var 1))) (var 1)) (op (var 0) (var 0))) , (var 2)) → ⊥
  cut6899  adequate = bad6899  (Adequate.valid adequate Two boolean env1)
  bad6900 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b0 b1)) b1) (bop b0 b1)) b0 → ⊥
  bad6900  p = false≢true (sym (cong lower p))
  cut6900 : Adequate {ℓ} ((op (op (op (var 0) (op (var 0) (var 1))) (var 1)) (op (var 0) (var 1))) , (var 0)) → ⊥
  cut6900  adequate = bad6900  (Adequate.valid adequate Two boolean env0)
  holds6901 : (z0 z1 : A3) → (mul3 (mul3 (mul3 z0 (mul3 z0 z1)) z1) (mul3 z0 z1)) ≡ z1
  holds6901 z0 z1 = refl
  cut6901 : Adequate {ℓ} ((op (op (op (var 0) (op (var 0) (var 1))) (var 1)) (op (var 0) (var 1))) , (var 1)) → ⊥
  cut6901  = reject3 ((op (op (op (var 0) (op (var 0) (var 1))) (var 1)) (op (var 0) (var 1))) , (var 1)) (λ env → holds6901 (env 0) (env 1))
  bad6902 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b0 b0)) b0) (bop b0 b0)) b1 → ⊥
  bad6902  p = false≢true (cong lower p)
  cut6902 : Adequate {ℓ} ((op (op (op (var 0) (op (var 0) (var 1))) (var 1)) (op (var 0) (var 1))) , (var 2)) → ⊥
  cut6902  adequate = bad6902  (Adequate.valid adequate Two boolean env1)
  bad6903 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b0 b1)) b1) (bop b0 b0)) b0 → ⊥
  bad6903  p = false≢true (sym (cong lower p))
  cut6903 : Adequate {ℓ} ((op (op (op (var 0) (op (var 0) (var 1))) (var 1)) (op (var 0) (var 2))) , (var 0)) → ⊥
  cut6903  adequate = bad6903  (Adequate.valid adequate Two boolean env4)
  bad6904 : PathP (λ _ → Two) (bop (bop (bop b1 (bop b1 b0)) b0) (bop b1 b1)) b0 → ⊥
  bad6904  p = false≢true (sym (cong lower p))
  cut6904 : Adequate {ℓ} ((op (op (op (var 0) (op (var 0) (var 1))) (var 1)) (op (var 0) (var 2))) , (var 1)) → ⊥
  cut6904  adequate = bad6904  (Adequate.valid adequate Two boolean env6)
  bad6905 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b0 b0)) b0) (bop b0 b1)) b1 → ⊥
  bad6905  p = false≢true (cong lower p)
  cut6905 : Adequate {ℓ} ((op (op (op (var 0) (op (var 0) (var 1))) (var 1)) (op (var 0) (var 2))) , (var 2)) → ⊥
  cut6905  adequate = bad6905  (Adequate.valid adequate Two boolean env1)
  bad6906 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b0 b0)) b0) (bop b0 b0)) b1 → ⊥
  bad6906  p = false≢true (cong lower p)
  cut6906 : Adequate {ℓ} ((op (op (op (var 0) (op (var 0) (var 1))) (var 1)) (op (var 0) (var 2))) , (var 3)) → ⊥
  cut6906  adequate = bad6906  (Adequate.valid adequate Two boolean env5)
  bad6907 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b0 b1)) b1) (bop b1 b0)) b0 → ⊥
  bad6907  p = false≢true (sym (cong lower p))
  cut6907 : Adequate {ℓ} ((op (op (op (var 0) (op (var 0) (var 1))) (var 1)) (op (var 1) (var 0))) , (var 0)) → ⊥
  cut6907  adequate = bad6907  (Adequate.valid adequate Two boolean env0)
  holds6908 : (z0 z1 : A11) → (mul11 (mul11 (mul11 z0 (mul11 z0 z1)) z1) (mul11 z1 z0)) ≡ z1
  holds6908 m11c0 m11c0 = refl
  holds6908 m11c0 m11c1 = refl
  holds6908 m11c0 m11c2 = refl
  holds6908 m11c1 m11c0 = refl
  holds6908 m11c1 m11c1 = refl
  holds6908 m11c1 m11c2 = refl
  holds6908 m11c2 m11c0 = refl
  holds6908 m11c2 m11c1 = refl
  holds6908 m11c2 m11c2 = refl
  cut6908 : Adequate {ℓ} ((op (op (op (var 0) (op (var 0) (var 1))) (var 1)) (op (var 1) (var 0))) , (var 1)) → ⊥
  cut6908  = reject11 ((op (op (op (var 0) (op (var 0) (var 1))) (var 1)) (op (var 1) (var 0))) , (var 1)) (λ env → holds6908 (env 0) (env 1))
  bad6909 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b0 b0)) b0) (bop b0 b0)) b1 → ⊥
  bad6909  p = false≢true (cong lower p)
  cut6909 : Adequate {ℓ} ((op (op (op (var 0) (op (var 0) (var 1))) (var 1)) (op (var 1) (var 0))) , (var 2)) → ⊥
  cut6909  adequate = bad6909  (Adequate.valid adequate Two boolean env1)
  bad6910 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b0 b1)) b1) (bop b1 b1)) b0 → ⊥
  bad6910  p = false≢true (sym (cong lower p))
  cut6910 : Adequate {ℓ} ((op (op (op (var 0) (op (var 0) (var 1))) (var 1)) (op (var 1) (var 1))) , (var 0)) → ⊥
  cut6910  adequate = bad6910  (Adequate.valid adequate Two boolean env0)
  holds6911 : (z0 z1 : A3) → (mul3 (mul3 (mul3 z0 (mul3 z0 z1)) z1) (mul3 z1 z1)) ≡ z1
  holds6911 z0 z1 = refl
  cut6911 : Adequate {ℓ} ((op (op (op (var 0) (op (var 0) (var 1))) (var 1)) (op (var 1) (var 1))) , (var 1)) → ⊥
  cut6911  = reject3 ((op (op (op (var 0) (op (var 0) (var 1))) (var 1)) (op (var 1) (var 1))) , (var 1)) (λ env → holds6911 (env 0) (env 1))
  bad6912 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b0 b0)) b0) (bop b0 b0)) b1 → ⊥
  bad6912  p = false≢true (cong lower p)
  cut6912 : Adequate {ℓ} ((op (op (op (var 0) (op (var 0) (var 1))) (var 1)) (op (var 1) (var 1))) , (var 2)) → ⊥
  cut6912  adequate = bad6912  (Adequate.valid adequate Two boolean env1)
  bad6913 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b0 b1)) b1) (bop b1 b0)) b0 → ⊥
  bad6913  p = false≢true (sym (cong lower p))
  cut6913 : Adequate {ℓ} ((op (op (op (var 0) (op (var 0) (var 1))) (var 1)) (op (var 1) (var 2))) , (var 0)) → ⊥
  cut6913  adequate = bad6913  (Adequate.valid adequate Two boolean env4)
  holds6914 : (z0 z1 z2 : A11) → (mul11 (mul11 (mul11 z0 (mul11 z0 z1)) z1) (mul11 z1 z2)) ≡ z1
  holds6914 m11c0 m11c0 m11c0 = refl
  holds6914 m11c0 m11c0 m11c1 = refl
  holds6914 m11c0 m11c0 m11c2 = refl
  holds6914 m11c0 m11c1 z2 = refl
  holds6914 m11c0 m11c2 z2 = refl
  holds6914 m11c1 m11c0 m11c0 = refl
  holds6914 m11c1 m11c0 m11c1 = refl
  holds6914 m11c1 m11c0 m11c2 = refl
  holds6914 m11c1 m11c1 z2 = refl
  holds6914 m11c1 m11c2 z2 = refl
  holds6914 m11c2 m11c0 m11c0 = refl
  holds6914 m11c2 m11c0 m11c1 = refl
  holds6914 m11c2 m11c0 m11c2 = refl
  holds6914 m11c2 m11c1 z2 = refl
  holds6914 m11c2 m11c2 z2 = refl
  cut6914 : Adequate {ℓ} ((op (op (op (var 0) (op (var 0) (var 1))) (var 1)) (op (var 1) (var 2))) , (var 1)) → ⊥
  cut6914  = reject11 ((op (op (op (var 0) (op (var 0) (var 1))) (var 1)) (op (var 1) (var 2))) , (var 1)) (λ env → holds6914 (env 0) (env 1) (env 2))
  bad6915 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b0 b0)) b0) (bop b0 b1)) b1 → ⊥
  bad6915  p = false≢true (cong lower p)
  cut6915 : Adequate {ℓ} ((op (op (op (var 0) (op (var 0) (var 1))) (var 1)) (op (var 1) (var 2))) , (var 2)) → ⊥
  cut6915  adequate = bad6915  (Adequate.valid adequate Two boolean env1)
  bad6916 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b0 b0)) b0) (bop b0 b0)) b1 → ⊥
  bad6916  p = false≢true (cong lower p)
  cut6916 : Adequate {ℓ} ((op (op (op (var 0) (op (var 0) (var 1))) (var 1)) (op (var 1) (var 2))) , (var 3)) → ⊥
  cut6916  adequate = bad6916  (Adequate.valid adequate Two boolean env5)
  bad6917 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b0 b1)) b1) (bop b0 b0)) b0 → ⊥
  bad6917  p = false≢true (sym (cong lower p))
  cut6917 : Adequate {ℓ} ((op (op (op (var 0) (op (var 0) (var 1))) (var 1)) (op (var 2) (var 0))) , (var 0)) → ⊥
  cut6917  adequate = bad6917  (Adequate.valid adequate Two boolean env4)
  bad6918 : PathP (λ _ → Two) (bop (bop (bop b1 (bop b1 b0)) b0) (bop b1 b1)) b0 → ⊥
  bad6918  p = false≢true (sym (cong lower p))
  cut6918 : Adequate {ℓ} ((op (op (op (var 0) (op (var 0) (var 1))) (var 1)) (op (var 2) (var 0))) , (var 1)) → ⊥
  cut6918  adequate = bad6918  (Adequate.valid adequate Two boolean env6)
  bad6919 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b0 b0)) b0) (bop b1 b0)) b1 → ⊥
  bad6919  p = false≢true (cong lower p)
  cut6919 : Adequate {ℓ} ((op (op (op (var 0) (op (var 0) (var 1))) (var 1)) (op (var 2) (var 0))) , (var 2)) → ⊥
  cut6919  adequate = bad6919  (Adequate.valid adequate Two boolean env1)
  bad6920 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b0 b0)) b0) (bop b0 b0)) b1 → ⊥
  bad6920  p = false≢true (cong lower p)
  cut6920 : Adequate {ℓ} ((op (op (op (var 0) (op (var 0) (var 1))) (var 1)) (op (var 2) (var 0))) , (var 3)) → ⊥
  cut6920  adequate = bad6920  (Adequate.valid adequate Two boolean env5)
  bad6921 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b0 b1)) b1) (bop b0 b1)) b0 → ⊥
  bad6921  p = false≢true (sym (cong lower p))
  cut6921 : Adequate {ℓ} ((op (op (op (var 0) (op (var 0) (var 1))) (var 1)) (op (var 2) (var 1))) , (var 0)) → ⊥
  cut6921  adequate = bad6921  (Adequate.valid adequate Two boolean env4)
  holds6922 : (z0 z1 z2 : A3) → (mul3 (mul3 (mul3 z0 (mul3 z0 z1)) z1) (mul3 z2 z1)) ≡ z1
  holds6922 z0 z1 z2 = refl
  cut6922 : Adequate {ℓ} ((op (op (op (var 0) (op (var 0) (var 1))) (var 1)) (op (var 2) (var 1))) , (var 1)) → ⊥
  cut6922  = reject3 ((op (op (op (var 0) (op (var 0) (var 1))) (var 1)) (op (var 2) (var 1))) , (var 1)) (λ env → holds6922 (env 0) (env 1) (env 2))
  bad6923 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b0 b0)) b0) (bop b1 b0)) b1 → ⊥
  bad6923  p = false≢true (cong lower p)
  cut6923 : Adequate {ℓ} ((op (op (op (var 0) (op (var 0) (var 1))) (var 1)) (op (var 2) (var 1))) , (var 2)) → ⊥
  cut6923  adequate = bad6923  (Adequate.valid adequate Two boolean env1)
  bad6924 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b0 b0)) b0) (bop b0 b0)) b1 → ⊥
  bad6924  p = false≢true (cong lower p)
  cut6924 : Adequate {ℓ} ((op (op (op (var 0) (op (var 0) (var 1))) (var 1)) (op (var 2) (var 1))) , (var 3)) → ⊥
  cut6924  adequate = bad6924  (Adequate.valid adequate Two boolean env5)
  bad6925 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b0 b0)) b0) (bop b1 b1)) b0 → ⊥
  bad6925  p = false≢true (sym (cong lower p))
  cut6925 : Adequate {ℓ} ((op (op (op (var 0) (op (var 0) (var 1))) (var 1)) (op (var 2) (var 2))) , (var 0)) → ⊥
  cut6925  adequate = bad6925  (Adequate.valid adequate Two boolean env1)
  bad6926 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b0 b0)) b0) (bop b1 b1)) b0 → ⊥
  bad6926  p = false≢true (sym (cong lower p))
  cut6926 : Adequate {ℓ} ((op (op (op (var 0) (op (var 0) (var 1))) (var 1)) (op (var 2) (var 2))) , (var 1)) → ⊥
  cut6926  adequate = bad6926  (Adequate.valid adequate Two boolean env1)
  bad6927 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b0 b1)) b1) (bop b0 b0)) b0 → ⊥
  bad6927  p = false≢true (sym (cong lower p))
  cut6927 : Adequate {ℓ} ((op (op (op (var 0) (op (var 0) (var 1))) (var 1)) (op (var 2) (var 2))) , (var 2)) → ⊥
  cut6927  adequate = bad6927  (Adequate.valid adequate Two boolean env4)
  bad6928 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b0 b0)) b0) (bop b0 b0)) b1 → ⊥
  bad6928  p = false≢true (cong lower p)
  cut6928 : Adequate {ℓ} ((op (op (op (var 0) (op (var 0) (var 1))) (var 1)) (op (var 2) (var 2))) , (var 3)) → ⊥
  cut6928  adequate = bad6928  (Adequate.valid adequate Two boolean env5)
  bad6929 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b0 b0)) b0) (bop b1 b1)) b0 → ⊥
  bad6929  p = false≢true (sym (cong lower p))
  cut6929 : Adequate {ℓ} ((op (op (op (var 0) (op (var 0) (var 1))) (var 1)) (op (var 2) (var 3))) , (var 0)) → ⊥
  cut6929  adequate = bad6929  (Adequate.valid adequate Two boolean env7)
  bad6930 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b0 b0)) b0) (bop b1 b1)) b0 → ⊥
  bad6930  p = false≢true (sym (cong lower p))
  cut6930 : Adequate {ℓ} ((op (op (op (var 0) (op (var 0) (var 1))) (var 1)) (op (var 2) (var 3))) , (var 1)) → ⊥
  cut6930  adequate = bad6930  (Adequate.valid adequate Two boolean env7)
  bad6931 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b0 b0)) b0) (bop b1 b0)) b1 → ⊥
  bad6931  p = false≢true (cong lower p)
  cut6931 : Adequate {ℓ} ((op (op (op (var 0) (op (var 0) (var 1))) (var 1)) (op (var 2) (var 3))) , (var 2)) → ⊥
  cut6931  adequate = bad6931  (Adequate.valid adequate Two boolean env8)
  bad6932 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b0 b0)) b0) (bop b0 b1)) b1 → ⊥
  bad6932  p = false≢true (cong lower p)
  cut6932 : Adequate {ℓ} ((op (op (op (var 0) (op (var 0) (var 1))) (var 1)) (op (var 2) (var 3))) , (var 3)) → ⊥
  cut6932  adequate = bad6932  (Adequate.valid adequate Two boolean env5)
  bad6933 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b0 b0)) b0) (bop b0 b0)) b1 → ⊥
  bad6933  p = false≢true (cong lower p)
  cut6933 : Adequate {ℓ} ((op (op (op (var 0) (op (var 0) (var 1))) (var 1)) (op (var 2) (var 3))) , (var 4)) → ⊥
  cut6933  adequate = bad6933  (Adequate.valid adequate Two boolean env9)
  bad6934 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b0 b0)) b1) (bop b0 b0)) b0 → ⊥
  bad6934  p = false≢true (sym (cong lower p))
  cut6934 : Adequate {ℓ} ((op (op (op (var 0) (op (var 0) (var 1))) (var 2)) (op (var 0) (var 0))) , (var 0)) → ⊥
  cut6934  adequate = bad6934  (Adequate.valid adequate Two boolean env1)
  bad6935 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b0 b0)) b1) (bop b0 b0)) b0 → ⊥
  bad6935  p = false≢true (sym (cong lower p))
  cut6935 : Adequate {ℓ} ((op (op (op (var 0) (op (var 0) (var 1))) (var 2)) (op (var 0) (var 0))) , (var 1)) → ⊥
  cut6935  adequate = bad6935  (Adequate.valid adequate Two boolean env1)
  bad6936 : PathP (λ _ → Two) (bop (bop (bop b1 (bop b1 b0)) b0) (bop b1 b1)) b0 → ⊥
  bad6936  p = false≢true (sym (cong lower p))
  cut6936 : Adequate {ℓ} ((op (op (op (var 0) (op (var 0) (var 1))) (var 2)) (op (var 0) (var 0))) , (var 2)) → ⊥
  cut6936  adequate = bad6936  (Adequate.valid adequate Two boolean env10)
  bad6937 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b0 b0)) b0) (bop b0 b0)) b1 → ⊥
  bad6937  p = false≢true (cong lower p)
  cut6937 : Adequate {ℓ} ((op (op (op (var 0) (op (var 0) (var 1))) (var 2)) (op (var 0) (var 0))) , (var 3)) → ⊥
  cut6937  adequate = bad6937  (Adequate.valid adequate Two boolean env5)
  bad6938 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b0 b0)) b1) (bop b0 b0)) b0 → ⊥
  bad6938  p = false≢true (sym (cong lower p))
  cut6938 : Adequate {ℓ} ((op (op (op (var 0) (op (var 0) (var 1))) (var 2)) (op (var 0) (var 1))) , (var 0)) → ⊥
  cut6938  adequate = bad6938  (Adequate.valid adequate Two boolean env1)
  bad6939 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b0 b0)) b1) (bop b0 b0)) b0 → ⊥
  bad6939  p = false≢true (sym (cong lower p))
  cut6939 : Adequate {ℓ} ((op (op (op (var 0) (op (var 0) (var 1))) (var 2)) (op (var 0) (var 1))) , (var 1)) → ⊥
  cut6939  adequate = bad6939  (Adequate.valid adequate Two boolean env1)
  bad6940 : PathP (λ _ → Two) (bop (bop (bop b1 (bop b1 b0)) b1) (bop b1 b0)) b1 → ⊥
  bad6940  p = false≢true (cong lower p)
  cut6940 : Adequate {ℓ} ((op (op (op (var 0) (op (var 0) (var 1))) (var 2)) (op (var 0) (var 1))) , (var 2)) → ⊥
  cut6940  adequate = bad6940  (Adequate.valid adequate Two boolean env6)
  bad6941 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b0 b0)) b0) (bop b0 b0)) b1 → ⊥
  bad6941  p = false≢true (cong lower p)
  cut6941 : Adequate {ℓ} ((op (op (op (var 0) (op (var 0) (var 1))) (var 2)) (op (var 0) (var 1))) , (var 3)) → ⊥
  cut6941  adequate = bad6941  (Adequate.valid adequate Two boolean env5)
  bad6942 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b0 b0)) b1) (bop b0 b1)) b0 → ⊥
  bad6942  p = false≢true (sym (cong lower p))
  cut6942 : Adequate {ℓ} ((op (op (op (var 0) (op (var 0) (var 1))) (var 2)) (op (var 0) (var 2))) , (var 0)) → ⊥
  cut6942  adequate = bad6942  (Adequate.valid adequate Two boolean env1)
  bad6943 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b0 b0)) b1) (bop b0 b1)) b0 → ⊥
  bad6943  p = false≢true (sym (cong lower p))
  cut6943 : Adequate {ℓ} ((op (op (op (var 0) (op (var 0) (var 1))) (var 2)) (op (var 0) (var 2))) , (var 1)) → ⊥
  cut6943  adequate = bad6943  (Adequate.valid adequate Two boolean env1)
  holds6944 : (z0 z1 z2 : A3) → (mul3 (mul3 (mul3 z0 (mul3 z0 z1)) z2) (mul3 z0 z2)) ≡ z2
  holds6944 z0 z1 z2 = refl
  cut6944 : Adequate {ℓ} ((op (op (op (var 0) (op (var 0) (var 1))) (var 2)) (op (var 0) (var 2))) , (var 2)) → ⊥
  cut6944  = reject3 ((op (op (op (var 0) (op (var 0) (var 1))) (var 2)) (op (var 0) (var 2))) , (var 2)) (λ env → holds6944 (env 0) (env 1) (env 2))
  bad6945 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b0 b0)) b0) (bop b0 b0)) b1 → ⊥
  bad6945  p = false≢true (cong lower p)
  cut6945 : Adequate {ℓ} ((op (op (op (var 0) (op (var 0) (var 1))) (var 2)) (op (var 0) (var 2))) , (var 3)) → ⊥
  cut6945  adequate = bad6945  (Adequate.valid adequate Two boolean env5)
  bad6946 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b0 b0)) b1) (bop b0 b0)) b0 → ⊥
  bad6946  p = false≢true (sym (cong lower p))
  cut6946 : Adequate {ℓ} ((op (op (op (var 0) (op (var 0) (var 1))) (var 2)) (op (var 0) (var 3))) , (var 0)) → ⊥
  cut6946  adequate = bad6946  (Adequate.valid adequate Two boolean env8)
  bad6947 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b0 b0)) b1) (bop b0 b0)) b0 → ⊥
  bad6947  p = false≢true (sym (cong lower p))
  cut6947 : Adequate {ℓ} ((op (op (op (var 0) (op (var 0) (var 1))) (var 2)) (op (var 0) (var 3))) , (var 1)) → ⊥
  cut6947  adequate = bad6947  (Adequate.valid adequate Two boolean env8)
  env12 : ℕ → Two
  env12 zero = b1
  env12 (suc zero) = b0
  env12 (suc (suc zero)) = b0
  env12 (suc (suc (suc zero))) = b1
  env12 (suc (suc (suc (suc rest)))) = b0
  bad6948 : PathP (λ _ → Two) (bop (bop (bop b1 (bop b1 b0)) b0) (bop b1 b1)) b0 → ⊥
  bad6948  p = false≢true (sym (cong lower p))
  cut6948 : Adequate {ℓ} ((op (op (op (var 0) (op (var 0) (var 1))) (var 2)) (op (var 0) (var 3))) , (var 2)) → ⊥
  cut6948  adequate = bad6948  (Adequate.valid adequate Two boolean env12)
  bad6949 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b0 b0)) b0) (bop b0 b1)) b1 → ⊥
  bad6949  p = false≢true (cong lower p)
  cut6949 : Adequate {ℓ} ((op (op (op (var 0) (op (var 0) (var 1))) (var 2)) (op (var 0) (var 3))) , (var 3)) → ⊥
  cut6949  adequate = bad6949  (Adequate.valid adequate Two boolean env5)
  bad6950 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b0 b0)) b0) (bop b0 b0)) b1 → ⊥
  bad6950  p = false≢true (cong lower p)
  cut6950 : Adequate {ℓ} ((op (op (op (var 0) (op (var 0) (var 1))) (var 2)) (op (var 0) (var 3))) , (var 4)) → ⊥
  cut6950  adequate = bad6950  (Adequate.valid adequate Two boolean env9)
  bad6951 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b0 b0)) b1) (bop b0 b0)) b0 → ⊥
  bad6951  p = false≢true (sym (cong lower p))
  cut6951 : Adequate {ℓ} ((op (op (op (var 0) (op (var 0) (var 1))) (var 2)) (op (var 1) (var 0))) , (var 0)) → ⊥
  cut6951  adequate = bad6951  (Adequate.valid adequate Two boolean env1)
  bad6952 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b0 b0)) b1) (bop b0 b0)) b0 → ⊥
  bad6952  p = false≢true (sym (cong lower p))
  cut6952 : Adequate {ℓ} ((op (op (op (var 0) (op (var 0) (var 1))) (var 2)) (op (var 1) (var 0))) , (var 1)) → ⊥
  cut6952  adequate = bad6952  (Adequate.valid adequate Two boolean env1)
  bad6953 : PathP (λ _ → Two) (bop (bop (bop b1 (bop b1 b0)) b1) (bop b0 b1)) b1 → ⊥
  bad6953  p = false≢true (cong lower p)
  cut6953 : Adequate {ℓ} ((op (op (op (var 0) (op (var 0) (var 1))) (var 2)) (op (var 1) (var 0))) , (var 2)) → ⊥
  cut6953  adequate = bad6953  (Adequate.valid adequate Two boolean env6)
  bad6954 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b0 b0)) b0) (bop b0 b0)) b1 → ⊥
  bad6954  p = false≢true (cong lower p)
  cut6954 : Adequate {ℓ} ((op (op (op (var 0) (op (var 0) (var 1))) (var 2)) (op (var 1) (var 0))) , (var 3)) → ⊥
  cut6954  adequate = bad6954  (Adequate.valid adequate Two boolean env5)
  bad6955 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b0 b0)) b1) (bop b0 b0)) b0 → ⊥
  bad6955  p = false≢true (sym (cong lower p))
  cut6955 : Adequate {ℓ} ((op (op (op (var 0) (op (var 0) (var 1))) (var 2)) (op (var 1) (var 1))) , (var 0)) → ⊥
  cut6955  adequate = bad6955  (Adequate.valid adequate Two boolean env1)
  bad6956 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b0 b0)) b1) (bop b0 b0)) b0 → ⊥
  bad6956  p = false≢true (sym (cong lower p))
  cut6956 : Adequate {ℓ} ((op (op (op (var 0) (op (var 0) (var 1))) (var 2)) (op (var 1) (var 1))) , (var 1)) → ⊥
  cut6956  adequate = bad6956  (Adequate.valid adequate Two boolean env1)
  bad6957 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b0 b1)) b0) (bop b1 b1)) b0 → ⊥
  bad6957  p = false≢true (sym (cong lower p))
  cut6957 : Adequate {ℓ} ((op (op (op (var 0) (op (var 0) (var 1))) (var 2)) (op (var 1) (var 1))) , (var 2)) → ⊥
  cut6957  adequate = bad6957  (Adequate.valid adequate Two boolean env4)
  bad6958 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b0 b0)) b0) (bop b0 b0)) b1 → ⊥
  bad6958  p = false≢true (cong lower p)
  cut6958 : Adequate {ℓ} ((op (op (op (var 0) (op (var 0) (var 1))) (var 2)) (op (var 1) (var 1))) , (var 3)) → ⊥
  cut6958  adequate = bad6958  (Adequate.valid adequate Two boolean env5)
  bad6959 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b0 b0)) b1) (bop b0 b1)) b0 → ⊥
  bad6959  p = false≢true (sym (cong lower p))
  cut6959 : Adequate {ℓ} ((op (op (op (var 0) (op (var 0) (var 1))) (var 2)) (op (var 1) (var 2))) , (var 0)) → ⊥
  cut6959  adequate = bad6959  (Adequate.valid adequate Two boolean env1)
  bad6960 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b0 b0)) b1) (bop b0 b1)) b0 → ⊥
  bad6960  p = false≢true (sym (cong lower p))
  cut6960 : Adequate {ℓ} ((op (op (op (var 0) (op (var 0) (var 1))) (var 2)) (op (var 1) (var 2))) , (var 1)) → ⊥
  cut6960  adequate = bad6960  (Adequate.valid adequate Two boolean env1)
  bad6961 : PathP (λ _ → Two) (bop (bop (bop b1 (bop b1 b0)) b1) (bop b0 b1)) b1 → ⊥
  bad6961  p = false≢true (cong lower p)
  cut6961 : Adequate {ℓ} ((op (op (op (var 0) (op (var 0) (var 1))) (var 2)) (op (var 1) (var 2))) , (var 2)) → ⊥
  cut6961  adequate = bad6961  (Adequate.valid adequate Two boolean env6)
  bad6962 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b0 b0)) b0) (bop b0 b0)) b1 → ⊥
  bad6962  p = false≢true (cong lower p)
  cut6962 : Adequate {ℓ} ((op (op (op (var 0) (op (var 0) (var 1))) (var 2)) (op (var 1) (var 2))) , (var 3)) → ⊥
  cut6962  adequate = bad6962  (Adequate.valid adequate Two boolean env5)
  bad6963 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b0 b0)) b1) (bop b0 b0)) b0 → ⊥
  bad6963  p = false≢true (sym (cong lower p))
  cut6963 : Adequate {ℓ} ((op (op (op (var 0) (op (var 0) (var 1))) (var 2)) (op (var 1) (var 3))) , (var 0)) → ⊥
  cut6963  adequate = bad6963  (Adequate.valid adequate Two boolean env8)
  bad6964 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b0 b0)) b1) (bop b0 b0)) b0 → ⊥
  bad6964  p = false≢true (sym (cong lower p))
  cut6964 : Adequate {ℓ} ((op (op (op (var 0) (op (var 0) (var 1))) (var 2)) (op (var 1) (var 3))) , (var 1)) → ⊥
  cut6964  adequate = bad6964  (Adequate.valid adequate Two boolean env8)
  env13 : ℕ → Two
  env13 zero = b0
  env13 (suc zero) = b1
  env13 (suc (suc zero)) = b0
  env13 (suc (suc (suc zero))) = b1
  env13 (suc (suc (suc (suc rest)))) = b0
  bad6965 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b0 b1)) b0) (bop b1 b1)) b0 → ⊥
  bad6965  p = false≢true (sym (cong lower p))
  cut6965 : Adequate {ℓ} ((op (op (op (var 0) (op (var 0) (var 1))) (var 2)) (op (var 1) (var 3))) , (var 2)) → ⊥
  cut6965  adequate = bad6965  (Adequate.valid adequate Two boolean env13)
  bad6966 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b0 b0)) b0) (bop b0 b1)) b1 → ⊥
  bad6966  p = false≢true (cong lower p)
  cut6966 : Adequate {ℓ} ((op (op (op (var 0) (op (var 0) (var 1))) (var 2)) (op (var 1) (var 3))) , (var 3)) → ⊥
  cut6966  adequate = bad6966  (Adequate.valid adequate Two boolean env5)
  bad6967 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b0 b0)) b0) (bop b0 b0)) b1 → ⊥
  bad6967  p = false≢true (cong lower p)
  cut6967 : Adequate {ℓ} ((op (op (op (var 0) (op (var 0) (var 1))) (var 2)) (op (var 1) (var 3))) , (var 4)) → ⊥
  cut6967  adequate = bad6967  (Adequate.valid adequate Two boolean env9)
  bad6968 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b0 b0)) b1) (bop b1 b0)) b0 → ⊥
  bad6968  p = false≢true (sym (cong lower p))
  cut6968 : Adequate {ℓ} ((op (op (op (var 0) (op (var 0) (var 1))) (var 2)) (op (var 2) (var 0))) , (var 0)) → ⊥
  cut6968  adequate = bad6968  (Adequate.valid adequate Two boolean env1)
  bad6969 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b0 b0)) b1) (bop b1 b0)) b0 → ⊥
  bad6969  p = false≢true (sym (cong lower p))
  cut6969 : Adequate {ℓ} ((op (op (op (var 0) (op (var 0) (var 1))) (var 2)) (op (var 2) (var 0))) , (var 1)) → ⊥
  cut6969  adequate = bad6969  (Adequate.valid adequate Two boolean env1)
  holds6970 : (z0 z1 z2 : A11) → (mul11 (mul11 (mul11 z0 (mul11 z0 z1)) z2) (mul11 z2 z0)) ≡ z2
  holds6970 m11c0 m11c0 m11c0 = refl
  holds6970 m11c0 m11c0 m11c1 = refl
  holds6970 m11c0 m11c0 m11c2 = refl
  holds6970 m11c0 m11c1 m11c0 = refl
  holds6970 m11c0 m11c1 m11c1 = refl
  holds6970 m11c0 m11c1 m11c2 = refl
  holds6970 m11c0 m11c2 m11c0 = refl
  holds6970 m11c0 m11c2 m11c1 = refl
  holds6970 m11c0 m11c2 m11c2 = refl
  holds6970 m11c1 z1 m11c0 = refl
  holds6970 m11c1 z1 m11c1 = refl
  holds6970 m11c1 z1 m11c2 = refl
  holds6970 m11c2 m11c0 m11c0 = refl
  holds6970 m11c2 m11c0 m11c1 = refl
  holds6970 m11c2 m11c0 m11c2 = refl
  holds6970 m11c2 m11c1 m11c0 = refl
  holds6970 m11c2 m11c1 m11c1 = refl
  holds6970 m11c2 m11c1 m11c2 = refl
  holds6970 m11c2 m11c2 m11c0 = refl
  holds6970 m11c2 m11c2 m11c1 = refl
  holds6970 m11c2 m11c2 m11c2 = refl
  cut6970 : Adequate {ℓ} ((op (op (op (var 0) (op (var 0) (var 1))) (var 2)) (op (var 2) (var 0))) , (var 2)) → ⊥
  cut6970  = reject11 ((op (op (op (var 0) (op (var 0) (var 1))) (var 2)) (op (var 2) (var 0))) , (var 2)) (λ env → holds6970 (env 0) (env 1) (env 2))
  bad6971 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b0 b0)) b0) (bop b0 b0)) b1 → ⊥
  bad6971  p = false≢true (cong lower p)
  cut6971 : Adequate {ℓ} ((op (op (op (var 0) (op (var 0) (var 1))) (var 2)) (op (var 2) (var 0))) , (var 3)) → ⊥
  cut6971  adequate = bad6971  (Adequate.valid adequate Two boolean env5)
  bad6972 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b0 b0)) b1) (bop b1 b0)) b0 → ⊥
  bad6972  p = false≢true (sym (cong lower p))
  cut6972 : Adequate {ℓ} ((op (op (op (var 0) (op (var 0) (var 1))) (var 2)) (op (var 2) (var 1))) , (var 0)) → ⊥
  cut6972  adequate = bad6972  (Adequate.valid adequate Two boolean env1)
  bad6973 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b0 b0)) b1) (bop b1 b0)) b0 → ⊥
  bad6973  p = false≢true (sym (cong lower p))
  cut6973 : Adequate {ℓ} ((op (op (op (var 0) (op (var 0) (var 1))) (var 2)) (op (var 2) (var 1))) , (var 1)) → ⊥
  cut6973  adequate = bad6973  (Adequate.valid adequate Two boolean env1)
  bad6974 : PathP (λ _ → Two) (bop (bop (bop b1 (bop b1 b0)) b1) (bop b1 b0)) b1 → ⊥
  bad6974  p = false≢true (cong lower p)
  cut6974 : Adequate {ℓ} ((op (op (op (var 0) (op (var 0) (var 1))) (var 2)) (op (var 2) (var 1))) , (var 2)) → ⊥
  cut6974  adequate = bad6974  (Adequate.valid adequate Two boolean env6)
  bad6975 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b0 b0)) b0) (bop b0 b0)) b1 → ⊥
  bad6975  p = false≢true (cong lower p)
  cut6975 : Adequate {ℓ} ((op (op (op (var 0) (op (var 0) (var 1))) (var 2)) (op (var 2) (var 1))) , (var 3)) → ⊥
  cut6975  adequate = bad6975  (Adequate.valid adequate Two boolean env5)
  bad6976 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b0 b0)) b1) (bop b1 b1)) b0 → ⊥
  bad6976  p = false≢true (sym (cong lower p))
  cut6976 : Adequate {ℓ} ((op (op (op (var 0) (op (var 0) (var 1))) (var 2)) (op (var 2) (var 2))) , (var 0)) → ⊥
  cut6976  adequate = bad6976  (Adequate.valid adequate Two boolean env1)
  bad6977 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b0 b0)) b1) (bop b1 b1)) b0 → ⊥
  bad6977  p = false≢true (sym (cong lower p))
  cut6977 : Adequate {ℓ} ((op (op (op (var 0) (op (var 0) (var 1))) (var 2)) (op (var 2) (var 2))) , (var 1)) → ⊥
  cut6977  adequate = bad6977  (Adequate.valid adequate Two boolean env1)
  holds6978 : (z0 z1 z2 : A3) → (mul3 (mul3 (mul3 z0 (mul3 z0 z1)) z2) (mul3 z2 z2)) ≡ z2
  holds6978 z0 z1 z2 = refl
  cut6978 : Adequate {ℓ} ((op (op (op (var 0) (op (var 0) (var 1))) (var 2)) (op (var 2) (var 2))) , (var 2)) → ⊥
  cut6978  = reject3 ((op (op (op (var 0) (op (var 0) (var 1))) (var 2)) (op (var 2) (var 2))) , (var 2)) (λ env → holds6978 (env 0) (env 1) (env 2))
  bad6979 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b0 b0)) b0) (bop b0 b0)) b1 → ⊥
  bad6979  p = false≢true (cong lower p)
  cut6979 : Adequate {ℓ} ((op (op (op (var 0) (op (var 0) (var 1))) (var 2)) (op (var 2) (var 2))) , (var 3)) → ⊥
  cut6979  adequate = bad6979  (Adequate.valid adequate Two boolean env5)
  bad6980 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b0 b0)) b1) (bop b1 b0)) b0 → ⊥
  bad6980  p = false≢true (sym (cong lower p))
  cut6980 : Adequate {ℓ} ((op (op (op (var 0) (op (var 0) (var 1))) (var 2)) (op (var 2) (var 3))) , (var 0)) → ⊥
  cut6980  adequate = bad6980  (Adequate.valid adequate Two boolean env8)
  bad6981 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b0 b0)) b1) (bop b1 b0)) b0 → ⊥
  bad6981  p = false≢true (sym (cong lower p))
  cut6981 : Adequate {ℓ} ((op (op (op (var 0) (op (var 0) (var 1))) (var 2)) (op (var 2) (var 3))) , (var 1)) → ⊥
  cut6981  adequate = bad6981  (Adequate.valid adequate Two boolean env8)
  env14 : ℕ → Two
  env14 zero = b1
  env14 (suc zero) = b0
  env14 (suc (suc zero)) = b1
  env14 (suc (suc (suc zero))) = b0
  env14 (suc (suc (suc (suc rest)))) = b0
  bad6982 : PathP (λ _ → Two) (bop (bop (bop b1 (bop b1 b0)) b1) (bop b1 b0)) b1 → ⊥
  bad6982  p = false≢true (cong lower p)
  cut6982 : Adequate {ℓ} ((op (op (op (var 0) (op (var 0) (var 1))) (var 2)) (op (var 2) (var 3))) , (var 2)) → ⊥
  cut6982  adequate = bad6982  (Adequate.valid adequate Two boolean env14)
  bad6983 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b0 b0)) b0) (bop b0 b1)) b1 → ⊥
  bad6983  p = false≢true (cong lower p)
  cut6983 : Adequate {ℓ} ((op (op (op (var 0) (op (var 0) (var 1))) (var 2)) (op (var 2) (var 3))) , (var 3)) → ⊥
  cut6983  adequate = bad6983  (Adequate.valid adequate Two boolean env5)
  bad6984 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b0 b0)) b0) (bop b0 b0)) b1 → ⊥
  bad6984  p = false≢true (cong lower p)
  cut6984 : Adequate {ℓ} ((op (op (op (var 0) (op (var 0) (var 1))) (var 2)) (op (var 2) (var 3))) , (var 4)) → ⊥
  cut6984  adequate = bad6984  (Adequate.valid adequate Two boolean env9)
  bad6985 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b0 b0)) b1) (bop b0 b0)) b0 → ⊥
  bad6985  p = false≢true (sym (cong lower p))
  cut6985 : Adequate {ℓ} ((op (op (op (var 0) (op (var 0) (var 1))) (var 2)) (op (var 3) (var 0))) , (var 0)) → ⊥
  cut6985  adequate = bad6985  (Adequate.valid adequate Two boolean env8)
  bad6986 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b0 b0)) b1) (bop b0 b0)) b0 → ⊥
  bad6986  p = false≢true (sym (cong lower p))
  cut6986 : Adequate {ℓ} ((op (op (op (var 0) (op (var 0) (var 1))) (var 2)) (op (var 3) (var 0))) , (var 1)) → ⊥
  cut6986  adequate = bad6986  (Adequate.valid adequate Two boolean env8)
  bad6987 : PathP (λ _ → Two) (bop (bop (bop b1 (bop b1 b0)) b0) (bop b1 b1)) b0 → ⊥
  bad6987  p = false≢true (sym (cong lower p))
  cut6987 : Adequate {ℓ} ((op (op (op (var 0) (op (var 0) (var 1))) (var 2)) (op (var 3) (var 0))) , (var 2)) → ⊥
  cut6987  adequate = bad6987  (Adequate.valid adequate Two boolean env12)
  bad6988 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b0 b0)) b0) (bop b1 b0)) b1 → ⊥
  bad6988  p = false≢true (cong lower p)
  cut6988 : Adequate {ℓ} ((op (op (op (var 0) (op (var 0) (var 1))) (var 2)) (op (var 3) (var 0))) , (var 3)) → ⊥
  cut6988  adequate = bad6988  (Adequate.valid adequate Two boolean env5)
  bad6989 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b0 b0)) b0) (bop b0 b0)) b1 → ⊥
  bad6989  p = false≢true (cong lower p)
  cut6989 : Adequate {ℓ} ((op (op (op (var 0) (op (var 0) (var 1))) (var 2)) (op (var 3) (var 0))) , (var 4)) → ⊥
  cut6989  adequate = bad6989  (Adequate.valid adequate Two boolean env9)
  bad6990 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b0 b0)) b1) (bop b0 b0)) b0 → ⊥
  bad6990  p = false≢true (sym (cong lower p))
  cut6990 : Adequate {ℓ} ((op (op (op (var 0) (op (var 0) (var 1))) (var 2)) (op (var 3) (var 1))) , (var 0)) → ⊥
  cut6990  adequate = bad6990  (Adequate.valid adequate Two boolean env8)
  bad6991 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b0 b0)) b1) (bop b0 b0)) b0 → ⊥
  bad6991  p = false≢true (sym (cong lower p))
  cut6991 : Adequate {ℓ} ((op (op (op (var 0) (op (var 0) (var 1))) (var 2)) (op (var 3) (var 1))) , (var 1)) → ⊥
  cut6991  adequate = bad6991  (Adequate.valid adequate Two boolean env8)
  bad6992 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b0 b1)) b0) (bop b1 b1)) b0 → ⊥
  bad6992  p = false≢true (sym (cong lower p))
  cut6992 : Adequate {ℓ} ((op (op (op (var 0) (op (var 0) (var 1))) (var 2)) (op (var 3) (var 1))) , (var 2)) → ⊥
  cut6992  adequate = bad6992  (Adequate.valid adequate Two boolean env13)
  bad6993 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b0 b0)) b0) (bop b1 b0)) b1 → ⊥
  bad6993  p = false≢true (cong lower p)
  cut6993 : Adequate {ℓ} ((op (op (op (var 0) (op (var 0) (var 1))) (var 2)) (op (var 3) (var 1))) , (var 3)) → ⊥
  cut6993  adequate = bad6993  (Adequate.valid adequate Two boolean env5)
  bad6994 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b0 b0)) b0) (bop b0 b0)) b1 → ⊥
  bad6994  p = false≢true (cong lower p)
  cut6994 : Adequate {ℓ} ((op (op (op (var 0) (op (var 0) (var 1))) (var 2)) (op (var 3) (var 1))) , (var 4)) → ⊥
  cut6994  adequate = bad6994  (Adequate.valid adequate Two boolean env9)
  bad6995 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b0 b0)) b1) (bop b0 b1)) b0 → ⊥
  bad6995  p = false≢true (sym (cong lower p))
  cut6995 : Adequate {ℓ} ((op (op (op (var 0) (op (var 0) (var 1))) (var 2)) (op (var 3) (var 2))) , (var 0)) → ⊥
  cut6995  adequate = bad6995  (Adequate.valid adequate Two boolean env8)
  bad6996 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b0 b0)) b1) (bop b0 b1)) b0 → ⊥
  bad6996  p = false≢true (sym (cong lower p))
  cut6996 : Adequate {ℓ} ((op (op (op (var 0) (op (var 0) (var 1))) (var 2)) (op (var 3) (var 2))) , (var 1)) → ⊥
  cut6996  adequate = bad6996  (Adequate.valid adequate Two boolean env8)
  bad6997 : PathP (λ _ → Two) (bop (bop (bop b1 (bop b1 b0)) b1) (bop b0 b1)) b1 → ⊥
  bad6997  p = false≢true (cong lower p)
  cut6997 : Adequate {ℓ} ((op (op (op (var 0) (op (var 0) (var 1))) (var 2)) (op (var 3) (var 2))) , (var 2)) → ⊥
  cut6997  adequate = bad6997  (Adequate.valid adequate Two boolean env14)
  bad6998 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b0 b0)) b0) (bop b1 b0)) b1 → ⊥
  bad6998  p = false≢true (cong lower p)
  cut6998 : Adequate {ℓ} ((op (op (op (var 0) (op (var 0) (var 1))) (var 2)) (op (var 3) (var 2))) , (var 3)) → ⊥
  cut6998  adequate = bad6998  (Adequate.valid adequate Two boolean env5)
  bad6999 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b0 b0)) b0) (bop b0 b0)) b1 → ⊥
  bad6999  p = false≢true (cong lower p)
  cut6999 : Adequate {ℓ} ((op (op (op (var 0) (op (var 0) (var 1))) (var 2)) (op (var 3) (var 2))) , (var 4)) → ⊥
  cut6999  adequate = bad6999  (Adequate.valid adequate Two boolean env9)
  bad7000 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b0 b0)) b0) (bop b1 b1)) b0 → ⊥
  bad7000  p = false≢true (sym (cong lower p))
  cut7000 : Adequate {ℓ} ((op (op (op (var 0) (op (var 0) (var 1))) (var 2)) (op (var 3) (var 3))) , (var 0)) → ⊥
  cut7000  adequate = bad7000  (Adequate.valid adequate Two boolean env5)
  bad7001 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b0 b0)) b0) (bop b1 b1)) b0 → ⊥
  bad7001  p = false≢true (sym (cong lower p))
  cut7001 : Adequate {ℓ} ((op (op (op (var 0) (op (var 0) (var 1))) (var 2)) (op (var 3) (var 3))) , (var 1)) → ⊥
  cut7001  adequate = bad7001  (Adequate.valid adequate Two boolean env5)
  bad7002 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b0 b0)) b0) (bop b1 b1)) b0 → ⊥
  bad7002  p = false≢true (sym (cong lower p))
  cut7002 : Adequate {ℓ} ((op (op (op (var 0) (op (var 0) (var 1))) (var 2)) (op (var 3) (var 3))) , (var 2)) → ⊥
  cut7002  adequate = bad7002  (Adequate.valid adequate Two boolean env5)
  bad7003 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b0 b0)) b1) (bop b0 b0)) b0 → ⊥
  bad7003  p = false≢true (sym (cong lower p))
  cut7003 : Adequate {ℓ} ((op (op (op (var 0) (op (var 0) (var 1))) (var 2)) (op (var 3) (var 3))) , (var 3)) → ⊥
  cut7003  adequate = bad7003  (Adequate.valid adequate Two boolean env8)
  bad7004 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b0 b0)) b0) (bop b0 b0)) b1 → ⊥
  bad7004  p = false≢true (cong lower p)
  cut7004 : Adequate {ℓ} ((op (op (op (var 0) (op (var 0) (var 1))) (var 2)) (op (var 3) (var 3))) , (var 4)) → ⊥
  cut7004  adequate = bad7004  (Adequate.valid adequate Two boolean env9)
  env15 : ℕ → Two
  env15 zero = b0
  env15 (suc zero) = b0
  env15 (suc (suc zero)) = b0
  env15 (suc (suc (suc zero))) = b1
  env15 (suc (suc (suc (suc zero)))) = b1
  env15 (suc (suc (suc (suc (suc rest))))) = b0
  bad7005 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b0 b0)) b0) (bop b1 b1)) b0 → ⊥
  bad7005  p = false≢true (sym (cong lower p))
  cut7005 : Adequate {ℓ} ((op (op (op (var 0) (op (var 0) (var 1))) (var 2)) (op (var 3) (var 4))) , (var 0)) → ⊥
  cut7005  adequate = bad7005  (Adequate.valid adequate Two boolean env15)
  bad7006 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b0 b0)) b0) (bop b1 b1)) b0 → ⊥
  bad7006  p = false≢true (sym (cong lower p))
  cut7006 : Adequate {ℓ} ((op (op (op (var 0) (op (var 0) (var 1))) (var 2)) (op (var 3) (var 4))) , (var 1)) → ⊥
  cut7006  adequate = bad7006  (Adequate.valid adequate Two boolean env15)
  bad7007 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b0 b0)) b0) (bop b1 b1)) b0 → ⊥
  bad7007  p = false≢true (sym (cong lower p))
  cut7007 : Adequate {ℓ} ((op (op (op (var 0) (op (var 0) (var 1))) (var 2)) (op (var 3) (var 4))) , (var 2)) → ⊥
  cut7007  adequate = bad7007  (Adequate.valid adequate Two boolean env15)
  env16 : ℕ → Two
  env16 zero = b0
  env16 (suc zero) = b0
  env16 (suc (suc zero)) = b0
  env16 (suc (suc (suc zero))) = b1
  env16 (suc (suc (suc (suc zero)))) = b0
  env16 (suc (suc (suc (suc (suc rest))))) = b0
  bad7008 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b0 b0)) b0) (bop b1 b0)) b1 → ⊥
  bad7008  p = false≢true (cong lower p)
  cut7008 : Adequate {ℓ} ((op (op (op (var 0) (op (var 0) (var 1))) (var 2)) (op (var 3) (var 4))) , (var 3)) → ⊥
  cut7008  adequate = bad7008  (Adequate.valid adequate Two boolean env16)
  bad7009 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b0 b0)) b0) (bop b0 b1)) b1 → ⊥
  bad7009  p = false≢true (cong lower p)
  cut7009 : Adequate {ℓ} ((op (op (op (var 0) (op (var 0) (var 1))) (var 2)) (op (var 3) (var 4))) , (var 4)) → ⊥
  cut7009  adequate = bad7009  (Adequate.valid adequate Two boolean env9)
  env17 : ℕ → Two
  env17 zero = b0
  env17 (suc zero) = b0
  env17 (suc (suc zero)) = b0
  env17 (suc (suc (suc zero))) = b0
  env17 (suc (suc (suc (suc zero)))) = b0
  env17 (suc (suc (suc (suc (suc zero))))) = b1
  env17 (suc (suc (suc (suc (suc (suc rest)))))) = b0
  bad7010 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b0 b0)) b0) (bop b0 b0)) b1 → ⊥
  bad7010  p = false≢true (cong lower p)
  cut7010 : Adequate {ℓ} ((op (op (op (var 0) (op (var 0) (var 1))) (var 2)) (op (var 3) (var 4))) , (var 5)) → ⊥
  cut7010  adequate = bad7010  (Adequate.valid adequate Two boolean env17)
  holds7011 : (z0 z1 : A2) → (mul2 (mul2 (mul2 z0 (mul2 z1 z0)) z0) (mul2 z0 z0)) ≡ z0
  holds7011 z0 z1 = refl
  cut7011 : Adequate {ℓ} ((op (op (op (var 0) (op (var 1) (var 0))) (var 0)) (op (var 0) (var 0))) , (var 0)) → ⊥
  cut7011  = reject2 ((op (op (op (var 0) (op (var 1) (var 0))) (var 0)) (op (var 0) (var 0))) , (var 0)) (λ env → holds7011 (env 0) (env 1))
  bad7012 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b1 b0)) b0) (bop b0 b0)) b1 → ⊥
  bad7012  p = false≢true (cong lower p)
  cut7012 : Adequate {ℓ} ((op (op (op (var 0) (op (var 1) (var 0))) (var 0)) (op (var 0) (var 0))) , (var 1)) → ⊥
  cut7012  adequate = bad7012  (Adequate.valid adequate Two boolean env0)
  bad7013 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b0 b0)) b0) (bop b0 b0)) b1 → ⊥
  bad7013  p = false≢true (cong lower p)
  cut7013 : Adequate {ℓ} ((op (op (op (var 0) (op (var 1) (var 0))) (var 0)) (op (var 0) (var 0))) , (var 2)) → ⊥
  cut7013  adequate = bad7013  (Adequate.valid adequate Two boolean env1)
  bad7014 : PathP (λ _ → Two) (bop (bop (bop b1 (bop b0 b1)) b1) (bop b1 b0)) b1 → ⊥
  bad7014  p = false≢true (cong lower p)
  cut7014 : Adequate {ℓ} ((op (op (op (var 0) (op (var 1) (var 0))) (var 0)) (op (var 0) (var 1))) , (var 0)) → ⊥
  cut7014  adequate = bad7014  (Adequate.valid adequate Two boolean env2)
  bad7015 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b1 b0)) b0) (bop b0 b1)) b1 → ⊥
  bad7015  p = false≢true (cong lower p)
  cut7015 : Adequate {ℓ} ((op (op (op (var 0) (op (var 1) (var 0))) (var 0)) (op (var 0) (var 1))) , (var 1)) → ⊥
  cut7015  adequate = bad7015  (Adequate.valid adequate Two boolean env0)
  bad7016 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b0 b0)) b0) (bop b0 b0)) b1 → ⊥
  bad7016  p = false≢true (cong lower p)
  cut7016 : Adequate {ℓ} ((op (op (op (var 0) (op (var 1) (var 0))) (var 0)) (op (var 0) (var 1))) , (var 2)) → ⊥
  cut7016  adequate = bad7016  (Adequate.valid adequate Two boolean env1)
  bad7017 : PathP (λ _ → Two) (bop (bop (bop b1 (bop b0 b1)) b1) (bop b1 b0)) b1 → ⊥
  bad7017  p = false≢true (cong lower p)
  cut7017 : Adequate {ℓ} ((op (op (op (var 0) (op (var 1) (var 0))) (var 0)) (op (var 0) (var 2))) , (var 0)) → ⊥
  cut7017  adequate = bad7017  (Adequate.valid adequate Two boolean env10)
  bad7018 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b1 b0)) b0) (bop b0 b0)) b1 → ⊥
  bad7018  p = false≢true (cong lower p)
  cut7018 : Adequate {ℓ} ((op (op (op (var 0) (op (var 1) (var 0))) (var 0)) (op (var 0) (var 2))) , (var 1)) → ⊥
  cut7018  adequate = bad7018  (Adequate.valid adequate Two boolean env4)
  bad7019 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b0 b0)) b0) (bop b0 b1)) b1 → ⊥
  bad7019  p = false≢true (cong lower p)
  cut7019 : Adequate {ℓ} ((op (op (op (var 0) (op (var 1) (var 0))) (var 0)) (op (var 0) (var 2))) , (var 2)) → ⊥
  cut7019  adequate = bad7019  (Adequate.valid adequate Two boolean env1)
  bad7020 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b0 b0)) b0) (bop b0 b0)) b1 → ⊥
  bad7020  p = false≢true (cong lower p)
  cut7020 : Adequate {ℓ} ((op (op (op (var 0) (op (var 1) (var 0))) (var 0)) (op (var 0) (var 2))) , (var 3)) → ⊥
  cut7020  adequate = bad7020  (Adequate.valid adequate Two boolean env5)
  bad7021 : PathP (λ _ → Two) (bop (bop (bop b1 (bop b0 b1)) b1) (bop b0 b1)) b1 → ⊥
  bad7021  p = false≢true (cong lower p)
  cut7021 : Adequate {ℓ} ((op (op (op (var 0) (op (var 1) (var 0))) (var 0)) (op (var 1) (var 0))) , (var 0)) → ⊥
  cut7021  adequate = bad7021  (Adequate.valid adequate Two boolean env2)
  bad7022 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b1 b0)) b0) (bop b1 b0)) b1 → ⊥
  bad7022  p = false≢true (cong lower p)
  cut7022 : Adequate {ℓ} ((op (op (op (var 0) (op (var 1) (var 0))) (var 0)) (op (var 1) (var 0))) , (var 1)) → ⊥
  cut7022  adequate = bad7022  (Adequate.valid adequate Two boolean env0)
  bad7023 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b0 b0)) b0) (bop b0 b0)) b1 → ⊥
  bad7023  p = false≢true (cong lower p)
  cut7023 : Adequate {ℓ} ((op (op (op (var 0) (op (var 1) (var 0))) (var 0)) (op (var 1) (var 0))) , (var 2)) → ⊥
  cut7023  adequate = bad7023  (Adequate.valid adequate Two boolean env1)
  bad7024 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b1 b0)) b0) (bop b1 b1)) b0 → ⊥
  bad7024  p = false≢true (sym (cong lower p))
  cut7024 : Adequate {ℓ} ((op (op (op (var 0) (op (var 1) (var 0))) (var 0)) (op (var 1) (var 1))) , (var 0)) → ⊥
  cut7024  adequate = bad7024  (Adequate.valid adequate Two boolean env0)
  holds7025 : (z0 z1 : A3) → (mul3 (mul3 (mul3 z0 (mul3 z1 z0)) z0) (mul3 z1 z1)) ≡ z1
  holds7025 z0 z1 = refl
  cut7025 : Adequate {ℓ} ((op (op (op (var 0) (op (var 1) (var 0))) (var 0)) (op (var 1) (var 1))) , (var 1)) → ⊥
  cut7025  = reject3 ((op (op (op (var 0) (op (var 1) (var 0))) (var 0)) (op (var 1) (var 1))) , (var 1)) (λ env → holds7025 (env 0) (env 1))
  bad7026 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b0 b0)) b0) (bop b0 b0)) b1 → ⊥
  bad7026  p = false≢true (cong lower p)
  cut7026 : Adequate {ℓ} ((op (op (op (var 0) (op (var 1) (var 0))) (var 0)) (op (var 1) (var 1))) , (var 2)) → ⊥
  cut7026  adequate = bad7026  (Adequate.valid adequate Two boolean env1)
  bad7027 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b1 b0)) b0) (bop b1 b1)) b0 → ⊥
  bad7027  p = false≢true (sym (cong lower p))
  cut7027 : Adequate {ℓ} ((op (op (op (var 0) (op (var 1) (var 0))) (var 0)) (op (var 1) (var 2))) , (var 0)) → ⊥
  cut7027  adequate = bad7027  (Adequate.valid adequate Two boolean env3)
  bad7028 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b1 b0)) b0) (bop b1 b0)) b1 → ⊥
  bad7028  p = false≢true (cong lower p)
  cut7028 : Adequate {ℓ} ((op (op (op (var 0) (op (var 1) (var 0))) (var 0)) (op (var 1) (var 2))) , (var 1)) → ⊥
  cut7028  adequate = bad7028  (Adequate.valid adequate Two boolean env4)
  bad7029 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b0 b0)) b0) (bop b0 b1)) b1 → ⊥
  bad7029  p = false≢true (cong lower p)
  cut7029 : Adequate {ℓ} ((op (op (op (var 0) (op (var 1) (var 0))) (var 0)) (op (var 1) (var 2))) , (var 2)) → ⊥
  cut7029  adequate = bad7029  (Adequate.valid adequate Two boolean env1)
  bad7030 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b0 b0)) b0) (bop b0 b0)) b1 → ⊥
  bad7030  p = false≢true (cong lower p)
  cut7030 : Adequate {ℓ} ((op (op (op (var 0) (op (var 1) (var 0))) (var 0)) (op (var 1) (var 2))) , (var 3)) → ⊥
  cut7030  adequate = bad7030  (Adequate.valid adequate Two boolean env5)
  bad7031 : PathP (λ _ → Two) (bop (bop (bop b1 (bop b0 b1)) b1) (bop b0 b1)) b1 → ⊥
  bad7031  p = false≢true (cong lower p)
  cut7031 : Adequate {ℓ} ((op (op (op (var 0) (op (var 1) (var 0))) (var 0)) (op (var 2) (var 0))) , (var 0)) → ⊥
  cut7031  adequate = bad7031  (Adequate.valid adequate Two boolean env10)
  bad7032 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b1 b0)) b0) (bop b0 b0)) b1 → ⊥
  bad7032  p = false≢true (cong lower p)
  cut7032 : Adequate {ℓ} ((op (op (op (var 0) (op (var 1) (var 0))) (var 0)) (op (var 2) (var 0))) , (var 1)) → ⊥
  cut7032  adequate = bad7032  (Adequate.valid adequate Two boolean env4)
  bad7033 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b0 b0)) b0) (bop b1 b0)) b1 → ⊥
  bad7033  p = false≢true (cong lower p)
  cut7033 : Adequate {ℓ} ((op (op (op (var 0) (op (var 1) (var 0))) (var 0)) (op (var 2) (var 0))) , (var 2)) → ⊥
  cut7033  adequate = bad7033  (Adequate.valid adequate Two boolean env1)
  bad7034 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b0 b0)) b0) (bop b0 b0)) b1 → ⊥
  bad7034  p = false≢true (cong lower p)
  cut7034 : Adequate {ℓ} ((op (op (op (var 0) (op (var 1) (var 0))) (var 0)) (op (var 2) (var 0))) , (var 3)) → ⊥
  cut7034  adequate = bad7034  (Adequate.valid adequate Two boolean env5)
  bad7035 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b1 b0)) b0) (bop b1 b1)) b0 → ⊥
  bad7035  p = false≢true (sym (cong lower p))
  cut7035 : Adequate {ℓ} ((op (op (op (var 0) (op (var 1) (var 0))) (var 0)) (op (var 2) (var 1))) , (var 0)) → ⊥
  cut7035  adequate = bad7035  (Adequate.valid adequate Two boolean env3)
  bad7036 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b1 b0)) b0) (bop b0 b1)) b1 → ⊥
  bad7036  p = false≢true (cong lower p)
  cut7036 : Adequate {ℓ} ((op (op (op (var 0) (op (var 1) (var 0))) (var 0)) (op (var 2) (var 1))) , (var 1)) → ⊥
  cut7036  adequate = bad7036  (Adequate.valid adequate Two boolean env4)
  bad7037 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b0 b0)) b0) (bop b1 b0)) b1 → ⊥
  bad7037  p = false≢true (cong lower p)
  cut7037 : Adequate {ℓ} ((op (op (op (var 0) (op (var 1) (var 0))) (var 0)) (op (var 2) (var 1))) , (var 2)) → ⊥
  cut7037  adequate = bad7037  (Adequate.valid adequate Two boolean env1)
  bad7038 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b0 b0)) b0) (bop b0 b0)) b1 → ⊥
  bad7038  p = false≢true (cong lower p)
  cut7038 : Adequate {ℓ} ((op (op (op (var 0) (op (var 1) (var 0))) (var 0)) (op (var 2) (var 1))) , (var 3)) → ⊥
  cut7038  adequate = bad7038  (Adequate.valid adequate Two boolean env5)
  bad7039 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b0 b0)) b0) (bop b1 b1)) b0 → ⊥
  bad7039  p = false≢true (sym (cong lower p))
  cut7039 : Adequate {ℓ} ((op (op (op (var 0) (op (var 1) (var 0))) (var 0)) (op (var 2) (var 2))) , (var 0)) → ⊥
  cut7039  adequate = bad7039  (Adequate.valid adequate Two boolean env1)
  bad7040 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b0 b0)) b0) (bop b1 b1)) b0 → ⊥
  bad7040  p = false≢true (sym (cong lower p))
  cut7040 : Adequate {ℓ} ((op (op (op (var 0) (op (var 1) (var 0))) (var 0)) (op (var 2) (var 2))) , (var 1)) → ⊥
  cut7040  adequate = bad7040  (Adequate.valid adequate Two boolean env1)
  bad7041 : PathP (λ _ → Two) (bop (bop (bop b1 (bop b1 b1)) b1) (bop b0 b0)) b0 → ⊥
  bad7041  p = false≢true (sym (cong lower p))
  cut7041 : Adequate {ℓ} ((op (op (op (var 0) (op (var 1) (var 0))) (var 0)) (op (var 2) (var 2))) , (var 2)) → ⊥
  cut7041  adequate = bad7041  (Adequate.valid adequate Two boolean env11)
  bad7042 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b0 b0)) b0) (bop b0 b0)) b1 → ⊥
  bad7042  p = false≢true (cong lower p)
  cut7042 : Adequate {ℓ} ((op (op (op (var 0) (op (var 1) (var 0))) (var 0)) (op (var 2) (var 2))) , (var 3)) → ⊥
  cut7042  adequate = bad7042  (Adequate.valid adequate Two boolean env5)
  bad7043 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b0 b0)) b0) (bop b1 b1)) b0 → ⊥
  bad7043  p = false≢true (sym (cong lower p))
  cut7043 : Adequate {ℓ} ((op (op (op (var 0) (op (var 1) (var 0))) (var 0)) (op (var 2) (var 3))) , (var 0)) → ⊥
  cut7043  adequate = bad7043  (Adequate.valid adequate Two boolean env7)
  bad7044 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b0 b0)) b0) (bop b1 b1)) b0 → ⊥
  bad7044  p = false≢true (sym (cong lower p))
  cut7044 : Adequate {ℓ} ((op (op (op (var 0) (op (var 1) (var 0))) (var 0)) (op (var 2) (var 3))) , (var 1)) → ⊥
  cut7044  adequate = bad7044  (Adequate.valid adequate Two boolean env7)
  bad7045 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b0 b0)) b0) (bop b1 b0)) b1 → ⊥
  bad7045  p = false≢true (cong lower p)
  cut7045 : Adequate {ℓ} ((op (op (op (var 0) (op (var 1) (var 0))) (var 0)) (op (var 2) (var 3))) , (var 2)) → ⊥
  cut7045  adequate = bad7045  (Adequate.valid adequate Two boolean env8)
  bad7046 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b0 b0)) b0) (bop b0 b1)) b1 → ⊥
  bad7046  p = false≢true (cong lower p)
  cut7046 : Adequate {ℓ} ((op (op (op (var 0) (op (var 1) (var 0))) (var 0)) (op (var 2) (var 3))) , (var 3)) → ⊥
  cut7046  adequate = bad7046  (Adequate.valid adequate Two boolean env5)
  bad7047 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b0 b0)) b0) (bop b0 b0)) b1 → ⊥
  bad7047  p = false≢true (cong lower p)
  cut7047 : Adequate {ℓ} ((op (op (op (var 0) (op (var 1) (var 0))) (var 0)) (op (var 2) (var 3))) , (var 4)) → ⊥
  cut7047  adequate = bad7047  (Adequate.valid adequate Two boolean env9)
  bad7048 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b1 b0)) b1) (bop b0 b0)) b0 → ⊥
  bad7048  p = false≢true (sym (cong lower p))
  cut7048 : Adequate {ℓ} ((op (op (op (var 0) (op (var 1) (var 0))) (var 1)) (op (var 0) (var 0))) , (var 0)) → ⊥
  cut7048  adequate = bad7048  (Adequate.valid adequate Two boolean env0)
  bad7049 : PathP (λ _ → Two) (bop (bop (bop b1 (bop b0 b1)) b0) (bop b1 b1)) b0 → ⊥
  bad7049  p = false≢true (sym (cong lower p))
  cut7049 : Adequate {ℓ} ((op (op (op (var 0) (op (var 1) (var 0))) (var 1)) (op (var 0) (var 0))) , (var 1)) → ⊥
  cut7049  adequate = bad7049  (Adequate.valid adequate Two boolean env2)
  bad7050 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b0 b0)) b0) (bop b0 b0)) b1 → ⊥
  bad7050  p = false≢true (cong lower p)
  cut7050 : Adequate {ℓ} ((op (op (op (var 0) (op (var 1) (var 0))) (var 1)) (op (var 0) (var 0))) , (var 2)) → ⊥
  cut7050  adequate = bad7050  (Adequate.valid adequate Two boolean env1)
  bad7051 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b1 b0)) b1) (bop b0 b1)) b0 → ⊥
  bad7051  p = false≢true (sym (cong lower p))
  cut7051 : Adequate {ℓ} ((op (op (op (var 0) (op (var 1) (var 0))) (var 1)) (op (var 0) (var 1))) , (var 0)) → ⊥
  cut7051  adequate = bad7051  (Adequate.valid adequate Two boolean env0)
  holds7052 : (z0 z1 : A3) → (mul3 (mul3 (mul3 z0 (mul3 z1 z0)) z1) (mul3 z0 z1)) ≡ z1
  holds7052 z0 z1 = refl
  cut7052 : Adequate {ℓ} ((op (op (op (var 0) (op (var 1) (var 0))) (var 1)) (op (var 0) (var 1))) , (var 1)) → ⊥
  cut7052  = reject3 ((op (op (op (var 0) (op (var 1) (var 0))) (var 1)) (op (var 0) (var 1))) , (var 1)) (λ env → holds7052 (env 0) (env 1))
  bad7053 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b0 b0)) b0) (bop b0 b0)) b1 → ⊥
  bad7053  p = false≢true (cong lower p)
  cut7053 : Adequate {ℓ} ((op (op (op (var 0) (op (var 1) (var 0))) (var 1)) (op (var 0) (var 1))) , (var 2)) → ⊥
  cut7053  adequate = bad7053  (Adequate.valid adequate Two boolean env1)
  bad7054 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b1 b0)) b1) (bop b0 b0)) b0 → ⊥
  bad7054  p = false≢true (sym (cong lower p))
  cut7054 : Adequate {ℓ} ((op (op (op (var 0) (op (var 1) (var 0))) (var 1)) (op (var 0) (var 2))) , (var 0)) → ⊥
  cut7054  adequate = bad7054  (Adequate.valid adequate Two boolean env4)
  bad7055 : PathP (λ _ → Two) (bop (bop (bop b1 (bop b0 b1)) b0) (bop b1 b1)) b0 → ⊥
  bad7055  p = false≢true (sym (cong lower p))
  cut7055 : Adequate {ℓ} ((op (op (op (var 0) (op (var 1) (var 0))) (var 1)) (op (var 0) (var 2))) , (var 1)) → ⊥
  cut7055  adequate = bad7055  (Adequate.valid adequate Two boolean env6)
  bad7056 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b0 b0)) b0) (bop b0 b1)) b1 → ⊥
  bad7056  p = false≢true (cong lower p)
  cut7056 : Adequate {ℓ} ((op (op (op (var 0) (op (var 1) (var 0))) (var 1)) (op (var 0) (var 2))) , (var 2)) → ⊥
  cut7056  adequate = bad7056  (Adequate.valid adequate Two boolean env1)
  bad7057 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b0 b0)) b0) (bop b0 b0)) b1 → ⊥
  bad7057  p = false≢true (cong lower p)
  cut7057 : Adequate {ℓ} ((op (op (op (var 0) (op (var 1) (var 0))) (var 1)) (op (var 0) (var 2))) , (var 3)) → ⊥
  cut7057  adequate = bad7057  (Adequate.valid adequate Two boolean env5)
  bad7058 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b1 b0)) b1) (bop b1 b0)) b0 → ⊥
  bad7058  p = false≢true (sym (cong lower p))
  cut7058 : Adequate {ℓ} ((op (op (op (var 0) (op (var 1) (var 0))) (var 1)) (op (var 1) (var 0))) , (var 0)) → ⊥
  cut7058  adequate = bad7058  (Adequate.valid adequate Two boolean env0)
  holds7059 : (z0 z1 : A11) → (mul11 (mul11 (mul11 z0 (mul11 z1 z0)) z1) (mul11 z1 z0)) ≡ z1
  holds7059 m11c0 m11c0 = refl
  holds7059 m11c0 m11c1 = refl
  holds7059 m11c0 m11c2 = refl
  holds7059 m11c1 m11c0 = refl
  holds7059 m11c1 m11c1 = refl
  holds7059 m11c1 m11c2 = refl
  holds7059 m11c2 m11c0 = refl
  holds7059 m11c2 m11c1 = refl
  holds7059 m11c2 m11c2 = refl
  cut7059 : Adequate {ℓ} ((op (op (op (var 0) (op (var 1) (var 0))) (var 1)) (op (var 1) (var 0))) , (var 1)) → ⊥
  cut7059  = reject11 ((op (op (op (var 0) (op (var 1) (var 0))) (var 1)) (op (var 1) (var 0))) , (var 1)) (λ env → holds7059 (env 0) (env 1))
  bad7060 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b0 b0)) b0) (bop b0 b0)) b1 → ⊥
  bad7060  p = false≢true (cong lower p)
  cut7060 : Adequate {ℓ} ((op (op (op (var 0) (op (var 1) (var 0))) (var 1)) (op (var 1) (var 0))) , (var 2)) → ⊥
  cut7060  adequate = bad7060  (Adequate.valid adequate Two boolean env1)
  bad7061 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b1 b0)) b1) (bop b1 b1)) b0 → ⊥
  bad7061  p = false≢true (sym (cong lower p))
  cut7061 : Adequate {ℓ} ((op (op (op (var 0) (op (var 1) (var 0))) (var 1)) (op (var 1) (var 1))) , (var 0)) → ⊥
  cut7061  adequate = bad7061  (Adequate.valid adequate Two boolean env0)
  holds7062 : (z0 z1 : A3) → (mul3 (mul3 (mul3 z0 (mul3 z1 z0)) z1) (mul3 z1 z1)) ≡ z1
  holds7062 z0 z1 = refl
  cut7062 : Adequate {ℓ} ((op (op (op (var 0) (op (var 1) (var 0))) (var 1)) (op (var 1) (var 1))) , (var 1)) → ⊥
  cut7062  = reject3 ((op (op (op (var 0) (op (var 1) (var 0))) (var 1)) (op (var 1) (var 1))) , (var 1)) (λ env → holds7062 (env 0) (env 1))
  bad7063 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b0 b0)) b0) (bop b0 b0)) b1 → ⊥
  bad7063  p = false≢true (cong lower p)
  cut7063 : Adequate {ℓ} ((op (op (op (var 0) (op (var 1) (var 0))) (var 1)) (op (var 1) (var 1))) , (var 2)) → ⊥
  cut7063  adequate = bad7063  (Adequate.valid adequate Two boolean env1)
  bad7064 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b1 b0)) b1) (bop b1 b0)) b0 → ⊥
  bad7064  p = false≢true (sym (cong lower p))
  cut7064 : Adequate {ℓ} ((op (op (op (var 0) (op (var 1) (var 0))) (var 1)) (op (var 1) (var 2))) , (var 0)) → ⊥
  cut7064  adequate = bad7064  (Adequate.valid adequate Two boolean env4)
  holds7065 : (z0 z1 z2 : A11) → (mul11 (mul11 (mul11 z0 (mul11 z1 z0)) z1) (mul11 z1 z2)) ≡ z1
  holds7065 m11c0 m11c0 m11c0 = refl
  holds7065 m11c0 m11c0 m11c1 = refl
  holds7065 m11c0 m11c0 m11c2 = refl
  holds7065 m11c0 m11c1 z2 = refl
  holds7065 m11c0 m11c2 z2 = refl
  holds7065 m11c1 m11c0 m11c0 = refl
  holds7065 m11c1 m11c0 m11c1 = refl
  holds7065 m11c1 m11c0 m11c2 = refl
  holds7065 m11c1 m11c1 z2 = refl
  holds7065 m11c1 m11c2 z2 = refl
  holds7065 m11c2 m11c0 m11c0 = refl
  holds7065 m11c2 m11c0 m11c1 = refl
  holds7065 m11c2 m11c0 m11c2 = refl
  holds7065 m11c2 m11c1 z2 = refl
  holds7065 m11c2 m11c2 z2 = refl
  cut7065 : Adequate {ℓ} ((op (op (op (var 0) (op (var 1) (var 0))) (var 1)) (op (var 1) (var 2))) , (var 1)) → ⊥
  cut7065  = reject11 ((op (op (op (var 0) (op (var 1) (var 0))) (var 1)) (op (var 1) (var 2))) , (var 1)) (λ env → holds7065 (env 0) (env 1) (env 2))
  bad7066 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b0 b0)) b0) (bop b0 b1)) b1 → ⊥
  bad7066  p = false≢true (cong lower p)
  cut7066 : Adequate {ℓ} ((op (op (op (var 0) (op (var 1) (var 0))) (var 1)) (op (var 1) (var 2))) , (var 2)) → ⊥
  cut7066  adequate = bad7066  (Adequate.valid adequate Two boolean env1)
  bad7067 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b0 b0)) b0) (bop b0 b0)) b1 → ⊥
  bad7067  p = false≢true (cong lower p)
  cut7067 : Adequate {ℓ} ((op (op (op (var 0) (op (var 1) (var 0))) (var 1)) (op (var 1) (var 2))) , (var 3)) → ⊥
  cut7067  adequate = bad7067  (Adequate.valid adequate Two boolean env5)
  bad7068 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b1 b0)) b1) (bop b0 b0)) b0 → ⊥
  bad7068  p = false≢true (sym (cong lower p))
  cut7068 : Adequate {ℓ} ((op (op (op (var 0) (op (var 1) (var 0))) (var 1)) (op (var 2) (var 0))) , (var 0)) → ⊥
  cut7068  adequate = bad7068  (Adequate.valid adequate Two boolean env4)
  bad7069 : PathP (λ _ → Two) (bop (bop (bop b1 (bop b0 b1)) b0) (bop b1 b1)) b0 → ⊥
  bad7069  p = false≢true (sym (cong lower p))
  cut7069 : Adequate {ℓ} ((op (op (op (var 0) (op (var 1) (var 0))) (var 1)) (op (var 2) (var 0))) , (var 1)) → ⊥
  cut7069  adequate = bad7069  (Adequate.valid adequate Two boolean env6)
  bad7070 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b0 b0)) b0) (bop b1 b0)) b1 → ⊥
  bad7070  p = false≢true (cong lower p)
  cut7070 : Adequate {ℓ} ((op (op (op (var 0) (op (var 1) (var 0))) (var 1)) (op (var 2) (var 0))) , (var 2)) → ⊥
  cut7070  adequate = bad7070  (Adequate.valid adequate Two boolean env1)
  bad7071 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b0 b0)) b0) (bop b0 b0)) b1 → ⊥
  bad7071  p = false≢true (cong lower p)
  cut7071 : Adequate {ℓ} ((op (op (op (var 0) (op (var 1) (var 0))) (var 1)) (op (var 2) (var 0))) , (var 3)) → ⊥
  cut7071  adequate = bad7071  (Adequate.valid adequate Two boolean env5)
  bad7072 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b1 b0)) b1) (bop b0 b1)) b0 → ⊥
  bad7072  p = false≢true (sym (cong lower p))
  cut7072 : Adequate {ℓ} ((op (op (op (var 0) (op (var 1) (var 0))) (var 1)) (op (var 2) (var 1))) , (var 0)) → ⊥
  cut7072  adequate = bad7072  (Adequate.valid adequate Two boolean env4)
  holds7073 : (z0 z1 z2 : A3) → (mul3 (mul3 (mul3 z0 (mul3 z1 z0)) z1) (mul3 z2 z1)) ≡ z1
  holds7073 z0 z1 z2 = refl
  cut7073 : Adequate {ℓ} ((op (op (op (var 0) (op (var 1) (var 0))) (var 1)) (op (var 2) (var 1))) , (var 1)) → ⊥
  cut7073  = reject3 ((op (op (op (var 0) (op (var 1) (var 0))) (var 1)) (op (var 2) (var 1))) , (var 1)) (λ env → holds7073 (env 0) (env 1) (env 2))
  bad7074 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b0 b0)) b0) (bop b1 b0)) b1 → ⊥
  bad7074  p = false≢true (cong lower p)
  cut7074 : Adequate {ℓ} ((op (op (op (var 0) (op (var 1) (var 0))) (var 1)) (op (var 2) (var 1))) , (var 2)) → ⊥
  cut7074  adequate = bad7074  (Adequate.valid adequate Two boolean env1)
  bad7075 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b0 b0)) b0) (bop b0 b0)) b1 → ⊥
  bad7075  p = false≢true (cong lower p)
  cut7075 : Adequate {ℓ} ((op (op (op (var 0) (op (var 1) (var 0))) (var 1)) (op (var 2) (var 1))) , (var 3)) → ⊥
  cut7075  adequate = bad7075  (Adequate.valid adequate Two boolean env5)
  bad7076 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b0 b0)) b0) (bop b1 b1)) b0 → ⊥
  bad7076  p = false≢true (sym (cong lower p))
  cut7076 : Adequate {ℓ} ((op (op (op (var 0) (op (var 1) (var 0))) (var 1)) (op (var 2) (var 2))) , (var 0)) → ⊥
  cut7076  adequate = bad7076  (Adequate.valid adequate Two boolean env1)
  bad7077 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b0 b0)) b0) (bop b1 b1)) b0 → ⊥
  bad7077  p = false≢true (sym (cong lower p))
  cut7077 : Adequate {ℓ} ((op (op (op (var 0) (op (var 1) (var 0))) (var 1)) (op (var 2) (var 2))) , (var 1)) → ⊥
  cut7077  adequate = bad7077  (Adequate.valid adequate Two boolean env1)
  bad7078 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b1 b0)) b1) (bop b0 b0)) b0 → ⊥
  bad7078  p = false≢true (sym (cong lower p))
  cut7078 : Adequate {ℓ} ((op (op (op (var 0) (op (var 1) (var 0))) (var 1)) (op (var 2) (var 2))) , (var 2)) → ⊥
  cut7078  adequate = bad7078  (Adequate.valid adequate Two boolean env4)
  bad7079 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b0 b0)) b0) (bop b0 b0)) b1 → ⊥
  bad7079  p = false≢true (cong lower p)
  cut7079 : Adequate {ℓ} ((op (op (op (var 0) (op (var 1) (var 0))) (var 1)) (op (var 2) (var 2))) , (var 3)) → ⊥
  cut7079  adequate = bad7079  (Adequate.valid adequate Two boolean env5)
  bad7080 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b0 b0)) b0) (bop b1 b1)) b0 → ⊥
  bad7080  p = false≢true (sym (cong lower p))
  cut7080 : Adequate {ℓ} ((op (op (op (var 0) (op (var 1) (var 0))) (var 1)) (op (var 2) (var 3))) , (var 0)) → ⊥
  cut7080  adequate = bad7080  (Adequate.valid adequate Two boolean env7)
  bad7081 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b0 b0)) b0) (bop b1 b1)) b0 → ⊥
  bad7081  p = false≢true (sym (cong lower p))
  cut7081 : Adequate {ℓ} ((op (op (op (var 0) (op (var 1) (var 0))) (var 1)) (op (var 2) (var 3))) , (var 1)) → ⊥
  cut7081  adequate = bad7081  (Adequate.valid adequate Two boolean env7)
  bad7082 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b0 b0)) b0) (bop b1 b0)) b1 → ⊥
  bad7082  p = false≢true (cong lower p)
  cut7082 : Adequate {ℓ} ((op (op (op (var 0) (op (var 1) (var 0))) (var 1)) (op (var 2) (var 3))) , (var 2)) → ⊥
  cut7082  adequate = bad7082  (Adequate.valid adequate Two boolean env8)
  bad7083 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b0 b0)) b0) (bop b0 b1)) b1 → ⊥
  bad7083  p = false≢true (cong lower p)
  cut7083 : Adequate {ℓ} ((op (op (op (var 0) (op (var 1) (var 0))) (var 1)) (op (var 2) (var 3))) , (var 3)) → ⊥
  cut7083  adequate = bad7083  (Adequate.valid adequate Two boolean env5)
  bad7084 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b0 b0)) b0) (bop b0 b0)) b1 → ⊥
  bad7084  p = false≢true (cong lower p)
  cut7084 : Adequate {ℓ} ((op (op (op (var 0) (op (var 1) (var 0))) (var 1)) (op (var 2) (var 3))) , (var 4)) → ⊥
  cut7084  adequate = bad7084  (Adequate.valid adequate Two boolean env9)
  bad7085 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b0 b0)) b1) (bop b0 b0)) b0 → ⊥
  bad7085  p = false≢true (sym (cong lower p))
  cut7085 : Adequate {ℓ} ((op (op (op (var 0) (op (var 1) (var 0))) (var 2)) (op (var 0) (var 0))) , (var 0)) → ⊥
  cut7085  adequate = bad7085  (Adequate.valid adequate Two boolean env1)
  bad7086 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b0 b0)) b1) (bop b0 b0)) b0 → ⊥
  bad7086  p = false≢true (sym (cong lower p))
  cut7086 : Adequate {ℓ} ((op (op (op (var 0) (op (var 1) (var 0))) (var 2)) (op (var 0) (var 0))) , (var 1)) → ⊥
  cut7086  adequate = bad7086  (Adequate.valid adequate Two boolean env1)
  bad7087 : PathP (λ _ → Two) (bop (bop (bop b1 (bop b0 b1)) b0) (bop b1 b1)) b0 → ⊥
  bad7087  p = false≢true (sym (cong lower p))
  cut7087 : Adequate {ℓ} ((op (op (op (var 0) (op (var 1) (var 0))) (var 2)) (op (var 0) (var 0))) , (var 2)) → ⊥
  cut7087  adequate = bad7087  (Adequate.valid adequate Two boolean env10)
  bad7088 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b0 b0)) b0) (bop b0 b0)) b1 → ⊥
  bad7088  p = false≢true (cong lower p)
  cut7088 : Adequate {ℓ} ((op (op (op (var 0) (op (var 1) (var 0))) (var 2)) (op (var 0) (var 0))) , (var 3)) → ⊥
  cut7088  adequate = bad7088  (Adequate.valid adequate Two boolean env5)
  bad7089 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b0 b0)) b1) (bop b0 b0)) b0 → ⊥
  bad7089  p = false≢true (sym (cong lower p))
  cut7089 : Adequate {ℓ} ((op (op (op (var 0) (op (var 1) (var 0))) (var 2)) (op (var 0) (var 1))) , (var 0)) → ⊥
  cut7089  adequate = bad7089  (Adequate.valid adequate Two boolean env1)
  bad7090 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b0 b0)) b1) (bop b0 b0)) b0 → ⊥
  bad7090  p = false≢true (sym (cong lower p))
  cut7090 : Adequate {ℓ} ((op (op (op (var 0) (op (var 1) (var 0))) (var 2)) (op (var 0) (var 1))) , (var 1)) → ⊥
  cut7090  adequate = bad7090  (Adequate.valid adequate Two boolean env1)
  bad7091 : PathP (λ _ → Two) (bop (bop (bop b1 (bop b0 b1)) b1) (bop b1 b0)) b1 → ⊥
  bad7091  p = false≢true (cong lower p)
  cut7091 : Adequate {ℓ} ((op (op (op (var 0) (op (var 1) (var 0))) (var 2)) (op (var 0) (var 1))) , (var 2)) → ⊥
  cut7091  adequate = bad7091  (Adequate.valid adequate Two boolean env6)
  bad7092 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b0 b0)) b0) (bop b0 b0)) b1 → ⊥
  bad7092  p = false≢true (cong lower p)
  cut7092 : Adequate {ℓ} ((op (op (op (var 0) (op (var 1) (var 0))) (var 2)) (op (var 0) (var 1))) , (var 3)) → ⊥
  cut7092  adequate = bad7092  (Adequate.valid adequate Two boolean env5)
  bad7093 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b0 b0)) b1) (bop b0 b1)) b0 → ⊥
  bad7093  p = false≢true (sym (cong lower p))
  cut7093 : Adequate {ℓ} ((op (op (op (var 0) (op (var 1) (var 0))) (var 2)) (op (var 0) (var 2))) , (var 0)) → ⊥
  cut7093  adequate = bad7093  (Adequate.valid adequate Two boolean env1)
  bad7094 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b0 b0)) b1) (bop b0 b1)) b0 → ⊥
  bad7094  p = false≢true (sym (cong lower p))
  cut7094 : Adequate {ℓ} ((op (op (op (var 0) (op (var 1) (var 0))) (var 2)) (op (var 0) (var 2))) , (var 1)) → ⊥
  cut7094  adequate = bad7094  (Adequate.valid adequate Two boolean env1)
  holds7095 : (z0 z1 z2 : A3) → (mul3 (mul3 (mul3 z0 (mul3 z1 z0)) z2) (mul3 z0 z2)) ≡ z2
  holds7095 z0 z1 z2 = refl
  cut7095 : Adequate {ℓ} ((op (op (op (var 0) (op (var 1) (var 0))) (var 2)) (op (var 0) (var 2))) , (var 2)) → ⊥
  cut7095  = reject3 ((op (op (op (var 0) (op (var 1) (var 0))) (var 2)) (op (var 0) (var 2))) , (var 2)) (λ env → holds7095 (env 0) (env 1) (env 2))
  bad7096 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b0 b0)) b0) (bop b0 b0)) b1 → ⊥
  bad7096  p = false≢true (cong lower p)
  cut7096 : Adequate {ℓ} ((op (op (op (var 0) (op (var 1) (var 0))) (var 2)) (op (var 0) (var 2))) , (var 3)) → ⊥
  cut7096  adequate = bad7096  (Adequate.valid adequate Two boolean env5)
  bad7097 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b0 b0)) b1) (bop b0 b0)) b0 → ⊥
  bad7097  p = false≢true (sym (cong lower p))
  cut7097 : Adequate {ℓ} ((op (op (op (var 0) (op (var 1) (var 0))) (var 2)) (op (var 0) (var 3))) , (var 0)) → ⊥
  cut7097  adequate = bad7097  (Adequate.valid adequate Two boolean env8)
  bad7098 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b0 b0)) b1) (bop b0 b0)) b0 → ⊥
  bad7098  p = false≢true (sym (cong lower p))
  cut7098 : Adequate {ℓ} ((op (op (op (var 0) (op (var 1) (var 0))) (var 2)) (op (var 0) (var 3))) , (var 1)) → ⊥
  cut7098  adequate = bad7098  (Adequate.valid adequate Two boolean env8)
  bad7099 : PathP (λ _ → Two) (bop (bop (bop b1 (bop b0 b1)) b0) (bop b1 b1)) b0 → ⊥
  bad7099  p = false≢true (sym (cong lower p))
  cut7099 : Adequate {ℓ} ((op (op (op (var 0) (op (var 1) (var 0))) (var 2)) (op (var 0) (var 3))) , (var 2)) → ⊥
  cut7099  adequate = bad7099  (Adequate.valid adequate Two boolean env12)
  bad7100 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b0 b0)) b0) (bop b0 b1)) b1 → ⊥
  bad7100  p = false≢true (cong lower p)
  cut7100 : Adequate {ℓ} ((op (op (op (var 0) (op (var 1) (var 0))) (var 2)) (op (var 0) (var 3))) , (var 3)) → ⊥
  cut7100  adequate = bad7100  (Adequate.valid adequate Two boolean env5)
  bad7101 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b0 b0)) b0) (bop b0 b0)) b1 → ⊥
  bad7101  p = false≢true (cong lower p)
  cut7101 : Adequate {ℓ} ((op (op (op (var 0) (op (var 1) (var 0))) (var 2)) (op (var 0) (var 3))) , (var 4)) → ⊥
  cut7101  adequate = bad7101  (Adequate.valid adequate Two boolean env9)
  bad7102 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b0 b0)) b1) (bop b0 b0)) b0 → ⊥
  bad7102  p = false≢true (sym (cong lower p))
  cut7102 : Adequate {ℓ} ((op (op (op (var 0) (op (var 1) (var 0))) (var 2)) (op (var 1) (var 0))) , (var 0)) → ⊥
  cut7102  adequate = bad7102  (Adequate.valid adequate Two boolean env1)
  bad7103 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b0 b0)) b1) (bop b0 b0)) b0 → ⊥
  bad7103  p = false≢true (sym (cong lower p))
  cut7103 : Adequate {ℓ} ((op (op (op (var 0) (op (var 1) (var 0))) (var 2)) (op (var 1) (var 0))) , (var 1)) → ⊥
  cut7103  adequate = bad7103  (Adequate.valid adequate Two boolean env1)
  bad7104 : PathP (λ _ → Two) (bop (bop (bop b1 (bop b0 b1)) b1) (bop b0 b1)) b1 → ⊥
  bad7104  p = false≢true (cong lower p)
  cut7104 : Adequate {ℓ} ((op (op (op (var 0) (op (var 1) (var 0))) (var 2)) (op (var 1) (var 0))) , (var 2)) → ⊥
  cut7104  adequate = bad7104  (Adequate.valid adequate Two boolean env6)
  bad7105 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b0 b0)) b0) (bop b0 b0)) b1 → ⊥
  bad7105  p = false≢true (cong lower p)
  cut7105 : Adequate {ℓ} ((op (op (op (var 0) (op (var 1) (var 0))) (var 2)) (op (var 1) (var 0))) , (var 3)) → ⊥
  cut7105  adequate = bad7105  (Adequate.valid adequate Two boolean env5)
  bad7106 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b0 b0)) b1) (bop b0 b0)) b0 → ⊥
  bad7106  p = false≢true (sym (cong lower p))
  cut7106 : Adequate {ℓ} ((op (op (op (var 0) (op (var 1) (var 0))) (var 2)) (op (var 1) (var 1))) , (var 0)) → ⊥
  cut7106  adequate = bad7106  (Adequate.valid adequate Two boolean env1)
  bad7107 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b0 b0)) b1) (bop b0 b0)) b0 → ⊥
  bad7107  p = false≢true (sym (cong lower p))
  cut7107 : Adequate {ℓ} ((op (op (op (var 0) (op (var 1) (var 0))) (var 2)) (op (var 1) (var 1))) , (var 1)) → ⊥
  cut7107  adequate = bad7107  (Adequate.valid adequate Two boolean env1)
  bad7108 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b1 b0)) b0) (bop b1 b1)) b0 → ⊥
  bad7108  p = false≢true (sym (cong lower p))
  cut7108 : Adequate {ℓ} ((op (op (op (var 0) (op (var 1) (var 0))) (var 2)) (op (var 1) (var 1))) , (var 2)) → ⊥
  cut7108  adequate = bad7108  (Adequate.valid adequate Two boolean env4)
  bad7109 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b0 b0)) b0) (bop b0 b0)) b1 → ⊥
  bad7109  p = false≢true (cong lower p)
  cut7109 : Adequate {ℓ} ((op (op (op (var 0) (op (var 1) (var 0))) (var 2)) (op (var 1) (var 1))) , (var 3)) → ⊥
  cut7109  adequate = bad7109  (Adequate.valid adequate Two boolean env5)
  bad7110 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b0 b0)) b1) (bop b0 b1)) b0 → ⊥
  bad7110  p = false≢true (sym (cong lower p))
  cut7110 : Adequate {ℓ} ((op (op (op (var 0) (op (var 1) (var 0))) (var 2)) (op (var 1) (var 2))) , (var 0)) → ⊥
  cut7110  adequate = bad7110  (Adequate.valid adequate Two boolean env1)
  bad7111 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b0 b0)) b1) (bop b0 b1)) b0 → ⊥
  bad7111  p = false≢true (sym (cong lower p))
  cut7111 : Adequate {ℓ} ((op (op (op (var 0) (op (var 1) (var 0))) (var 2)) (op (var 1) (var 2))) , (var 1)) → ⊥
  cut7111  adequate = bad7111  (Adequate.valid adequate Two boolean env1)
  bad7112 : PathP (λ _ → Two) (bop (bop (bop b1 (bop b0 b1)) b1) (bop b0 b1)) b1 → ⊥
  bad7112  p = false≢true (cong lower p)
  cut7112 : Adequate {ℓ} ((op (op (op (var 0) (op (var 1) (var 0))) (var 2)) (op (var 1) (var 2))) , (var 2)) → ⊥
  cut7112  adequate = bad7112  (Adequate.valid adequate Two boolean env6)
  bad7113 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b0 b0)) b0) (bop b0 b0)) b1 → ⊥
  bad7113  p = false≢true (cong lower p)
  cut7113 : Adequate {ℓ} ((op (op (op (var 0) (op (var 1) (var 0))) (var 2)) (op (var 1) (var 2))) , (var 3)) → ⊥
  cut7113  adequate = bad7113  (Adequate.valid adequate Two boolean env5)
  bad7114 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b0 b0)) b1) (bop b0 b0)) b0 → ⊥
  bad7114  p = false≢true (sym (cong lower p))
  cut7114 : Adequate {ℓ} ((op (op (op (var 0) (op (var 1) (var 0))) (var 2)) (op (var 1) (var 3))) , (var 0)) → ⊥
  cut7114  adequate = bad7114  (Adequate.valid adequate Two boolean env8)
  bad7115 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b0 b0)) b1) (bop b0 b0)) b0 → ⊥
  bad7115  p = false≢true (sym (cong lower p))
  cut7115 : Adequate {ℓ} ((op (op (op (var 0) (op (var 1) (var 0))) (var 2)) (op (var 1) (var 3))) , (var 1)) → ⊥
  cut7115  adequate = bad7115  (Adequate.valid adequate Two boolean env8)
  bad7116 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b1 b0)) b0) (bop b1 b1)) b0 → ⊥
  bad7116  p = false≢true (sym (cong lower p))
  cut7116 : Adequate {ℓ} ((op (op (op (var 0) (op (var 1) (var 0))) (var 2)) (op (var 1) (var 3))) , (var 2)) → ⊥
  cut7116  adequate = bad7116  (Adequate.valid adequate Two boolean env13)
  bad7117 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b0 b0)) b0) (bop b0 b1)) b1 → ⊥
  bad7117  p = false≢true (cong lower p)
  cut7117 : Adequate {ℓ} ((op (op (op (var 0) (op (var 1) (var 0))) (var 2)) (op (var 1) (var 3))) , (var 3)) → ⊥
  cut7117  adequate = bad7117  (Adequate.valid adequate Two boolean env5)
  bad7118 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b0 b0)) b0) (bop b0 b0)) b1 → ⊥
  bad7118  p = false≢true (cong lower p)
  cut7118 : Adequate {ℓ} ((op (op (op (var 0) (op (var 1) (var 0))) (var 2)) (op (var 1) (var 3))) , (var 4)) → ⊥
  cut7118  adequate = bad7118  (Adequate.valid adequate Two boolean env9)
  bad7119 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b0 b0)) b1) (bop b1 b0)) b0 → ⊥
  bad7119  p = false≢true (sym (cong lower p))
  cut7119 : Adequate {ℓ} ((op (op (op (var 0) (op (var 1) (var 0))) (var 2)) (op (var 2) (var 0))) , (var 0)) → ⊥
  cut7119  adequate = bad7119  (Adequate.valid adequate Two boolean env1)
  bad7120 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b0 b0)) b1) (bop b1 b0)) b0 → ⊥
  bad7120  p = false≢true (sym (cong lower p))
  cut7120 : Adequate {ℓ} ((op (op (op (var 0) (op (var 1) (var 0))) (var 2)) (op (var 2) (var 0))) , (var 1)) → ⊥
  cut7120  adequate = bad7120  (Adequate.valid adequate Two boolean env1)
  holds7121 : (z0 z1 z2 : A13) → (mul13 (mul13 (mul13 z0 (mul13 z1 z0)) z2) (mul13 z2 z0)) ≡ z2
  holds7121 m13c0 m13c0 m13c0 = refl
  holds7121 m13c0 m13c0 m13c1 = refl
  holds7121 m13c0 m13c0 m13c2 = refl
  holds7121 m13c0 m13c0 m13c3 = refl
  holds7121 m13c0 m13c1 m13c0 = refl
  holds7121 m13c0 m13c1 m13c1 = refl
  holds7121 m13c0 m13c1 m13c2 = refl
  holds7121 m13c0 m13c1 m13c3 = refl
  holds7121 m13c0 m13c2 m13c0 = refl
  holds7121 m13c0 m13c2 m13c1 = refl
  holds7121 m13c0 m13c2 m13c2 = refl
  holds7121 m13c0 m13c2 m13c3 = refl
  holds7121 m13c0 m13c3 m13c0 = refl
  holds7121 m13c0 m13c3 m13c1 = refl
  holds7121 m13c0 m13c3 m13c2 = refl
  holds7121 m13c0 m13c3 m13c3 = refl
  holds7121 m13c1 m13c0 m13c0 = refl
  holds7121 m13c1 m13c0 m13c1 = refl
  holds7121 m13c1 m13c0 m13c2 = refl
  holds7121 m13c1 m13c0 m13c3 = refl
  holds7121 m13c1 m13c1 m13c0 = refl
  holds7121 m13c1 m13c1 m13c1 = refl
  holds7121 m13c1 m13c1 m13c2 = refl
  holds7121 m13c1 m13c1 m13c3 = refl
  holds7121 m13c1 m13c2 m13c0 = refl
  holds7121 m13c1 m13c2 m13c1 = refl
  holds7121 m13c1 m13c2 m13c2 = refl
  holds7121 m13c1 m13c2 m13c3 = refl
  holds7121 m13c1 m13c3 m13c0 = refl
  holds7121 m13c1 m13c3 m13c1 = refl
  holds7121 m13c1 m13c3 m13c2 = refl
  holds7121 m13c1 m13c3 m13c3 = refl
  holds7121 m13c2 m13c0 m13c0 = refl
  holds7121 m13c2 m13c0 m13c1 = refl
  holds7121 m13c2 m13c0 m13c2 = refl
  holds7121 m13c2 m13c0 m13c3 = refl
  holds7121 m13c2 m13c1 m13c0 = refl
  holds7121 m13c2 m13c1 m13c1 = refl
  holds7121 m13c2 m13c1 m13c2 = refl
  holds7121 m13c2 m13c1 m13c3 = refl
  holds7121 m13c2 m13c2 m13c0 = refl
  holds7121 m13c2 m13c2 m13c1 = refl
  holds7121 m13c2 m13c2 m13c2 = refl
  holds7121 m13c2 m13c2 m13c3 = refl
  holds7121 m13c2 m13c3 m13c0 = refl
  holds7121 m13c2 m13c3 m13c1 = refl
  holds7121 m13c2 m13c3 m13c2 = refl
  holds7121 m13c2 m13c3 m13c3 = refl
  holds7121 m13c3 m13c0 m13c0 = refl
  holds7121 m13c3 m13c0 m13c1 = refl
  holds7121 m13c3 m13c0 m13c2 = refl
  holds7121 m13c3 m13c0 m13c3 = refl
  holds7121 m13c3 m13c1 m13c0 = refl
  holds7121 m13c3 m13c1 m13c1 = refl
  holds7121 m13c3 m13c1 m13c2 = refl
  holds7121 m13c3 m13c1 m13c3 = refl
  holds7121 m13c3 m13c2 m13c0 = refl
  holds7121 m13c3 m13c2 m13c1 = refl
  holds7121 m13c3 m13c2 m13c2 = refl
  holds7121 m13c3 m13c2 m13c3 = refl
  holds7121 m13c3 m13c3 m13c0 = refl
  holds7121 m13c3 m13c3 m13c1 = refl
  holds7121 m13c3 m13c3 m13c2 = refl
  holds7121 m13c3 m13c3 m13c3 = refl
  cut7121 : Adequate {ℓ} ((op (op (op (var 0) (op (var 1) (var 0))) (var 2)) (op (var 2) (var 0))) , (var 2)) → ⊥
  cut7121  = reject13 ((op (op (op (var 0) (op (var 1) (var 0))) (var 2)) (op (var 2) (var 0))) , (var 2)) (λ env → holds7121 (env 0) (env 1) (env 2))
  bad7122 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b0 b0)) b0) (bop b0 b0)) b1 → ⊥
  bad7122  p = false≢true (cong lower p)
  cut7122 : Adequate {ℓ} ((op (op (op (var 0) (op (var 1) (var 0))) (var 2)) (op (var 2) (var 0))) , (var 3)) → ⊥
  cut7122  adequate = bad7122  (Adequate.valid adequate Two boolean env5)
  bad7123 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b0 b0)) b1) (bop b1 b0)) b0 → ⊥
  bad7123  p = false≢true (sym (cong lower p))
  cut7123 : Adequate {ℓ} ((op (op (op (var 0) (op (var 1) (var 0))) (var 2)) (op (var 2) (var 1))) , (var 0)) → ⊥
  cut7123  adequate = bad7123  (Adequate.valid adequate Two boolean env1)
  bad7124 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b0 b0)) b1) (bop b1 b0)) b0 → ⊥
  bad7124  p = false≢true (sym (cong lower p))
  cut7124 : Adequate {ℓ} ((op (op (op (var 0) (op (var 1) (var 0))) (var 2)) (op (var 2) (var 1))) , (var 1)) → ⊥
  cut7124  adequate = bad7124  (Adequate.valid adequate Two boolean env1)
  bad7125 : PathP (λ _ → Two) (bop (bop (bop b1 (bop b0 b1)) b1) (bop b1 b0)) b1 → ⊥
  bad7125  p = false≢true (cong lower p)
  cut7125 : Adequate {ℓ} ((op (op (op (var 0) (op (var 1) (var 0))) (var 2)) (op (var 2) (var 1))) , (var 2)) → ⊥
  cut7125  adequate = bad7125  (Adequate.valid adequate Two boolean env6)
  bad7126 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b0 b0)) b0) (bop b0 b0)) b1 → ⊥
  bad7126  p = false≢true (cong lower p)
  cut7126 : Adequate {ℓ} ((op (op (op (var 0) (op (var 1) (var 0))) (var 2)) (op (var 2) (var 1))) , (var 3)) → ⊥
  cut7126  adequate = bad7126  (Adequate.valid adequate Two boolean env5)
  bad7127 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b0 b0)) b1) (bop b1 b1)) b0 → ⊥
  bad7127  p = false≢true (sym (cong lower p))
  cut7127 : Adequate {ℓ} ((op (op (op (var 0) (op (var 1) (var 0))) (var 2)) (op (var 2) (var 2))) , (var 0)) → ⊥
  cut7127  adequate = bad7127  (Adequate.valid adequate Two boolean env1)
  bad7128 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b0 b0)) b1) (bop b1 b1)) b0 → ⊥
  bad7128  p = false≢true (sym (cong lower p))
  cut7128 : Adequate {ℓ} ((op (op (op (var 0) (op (var 1) (var 0))) (var 2)) (op (var 2) (var 2))) , (var 1)) → ⊥
  cut7128  adequate = bad7128  (Adequate.valid adequate Two boolean env1)
  holds7129 : (z0 z1 z2 : A3) → (mul3 (mul3 (mul3 z0 (mul3 z1 z0)) z2) (mul3 z2 z2)) ≡ z2
  holds7129 z0 z1 z2 = refl
  cut7129 : Adequate {ℓ} ((op (op (op (var 0) (op (var 1) (var 0))) (var 2)) (op (var 2) (var 2))) , (var 2)) → ⊥
  cut7129  = reject3 ((op (op (op (var 0) (op (var 1) (var 0))) (var 2)) (op (var 2) (var 2))) , (var 2)) (λ env → holds7129 (env 0) (env 1) (env 2))
  bad7130 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b0 b0)) b0) (bop b0 b0)) b1 → ⊥
  bad7130  p = false≢true (cong lower p)
  cut7130 : Adequate {ℓ} ((op (op (op (var 0) (op (var 1) (var 0))) (var 2)) (op (var 2) (var 2))) , (var 3)) → ⊥
  cut7130  adequate = bad7130  (Adequate.valid adequate Two boolean env5)
  bad7131 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b0 b0)) b1) (bop b1 b0)) b0 → ⊥
  bad7131  p = false≢true (sym (cong lower p))
  cut7131 : Adequate {ℓ} ((op (op (op (var 0) (op (var 1) (var 0))) (var 2)) (op (var 2) (var 3))) , (var 0)) → ⊥
  cut7131  adequate = bad7131  (Adequate.valid adequate Two boolean env8)
  bad7132 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b0 b0)) b1) (bop b1 b0)) b0 → ⊥
  bad7132  p = false≢true (sym (cong lower p))
  cut7132 : Adequate {ℓ} ((op (op (op (var 0) (op (var 1) (var 0))) (var 2)) (op (var 2) (var 3))) , (var 1)) → ⊥
  cut7132  adequate = bad7132  (Adequate.valid adequate Two boolean env8)
  bad7133 : PathP (λ _ → Two) (bop (bop (bop b1 (bop b0 b1)) b1) (bop b1 b0)) b1 → ⊥
  bad7133  p = false≢true (cong lower p)
  cut7133 : Adequate {ℓ} ((op (op (op (var 0) (op (var 1) (var 0))) (var 2)) (op (var 2) (var 3))) , (var 2)) → ⊥
  cut7133  adequate = bad7133  (Adequate.valid adequate Two boolean env14)
  bad7134 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b0 b0)) b0) (bop b0 b1)) b1 → ⊥
  bad7134  p = false≢true (cong lower p)
  cut7134 : Adequate {ℓ} ((op (op (op (var 0) (op (var 1) (var 0))) (var 2)) (op (var 2) (var 3))) , (var 3)) → ⊥
  cut7134  adequate = bad7134  (Adequate.valid adequate Two boolean env5)
  bad7135 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b0 b0)) b0) (bop b0 b0)) b1 → ⊥
  bad7135  p = false≢true (cong lower p)
  cut7135 : Adequate {ℓ} ((op (op (op (var 0) (op (var 1) (var 0))) (var 2)) (op (var 2) (var 3))) , (var 4)) → ⊥
  cut7135  adequate = bad7135  (Adequate.valid adequate Two boolean env9)
  bad7136 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b0 b0)) b1) (bop b0 b0)) b0 → ⊥
  bad7136  p = false≢true (sym (cong lower p))
  cut7136 : Adequate {ℓ} ((op (op (op (var 0) (op (var 1) (var 0))) (var 2)) (op (var 3) (var 0))) , (var 0)) → ⊥
  cut7136  adequate = bad7136  (Adequate.valid adequate Two boolean env8)
  bad7137 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b0 b0)) b1) (bop b0 b0)) b0 → ⊥
  bad7137  p = false≢true (sym (cong lower p))
  cut7137 : Adequate {ℓ} ((op (op (op (var 0) (op (var 1) (var 0))) (var 2)) (op (var 3) (var 0))) , (var 1)) → ⊥
  cut7137  adequate = bad7137  (Adequate.valid adequate Two boolean env8)
  bad7138 : PathP (λ _ → Two) (bop (bop (bop b1 (bop b0 b1)) b0) (bop b1 b1)) b0 → ⊥
  bad7138  p = false≢true (sym (cong lower p))
  cut7138 : Adequate {ℓ} ((op (op (op (var 0) (op (var 1) (var 0))) (var 2)) (op (var 3) (var 0))) , (var 2)) → ⊥
  cut7138  adequate = bad7138  (Adequate.valid adequate Two boolean env12)
  bad7139 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b0 b0)) b0) (bop b1 b0)) b1 → ⊥
  bad7139  p = false≢true (cong lower p)
  cut7139 : Adequate {ℓ} ((op (op (op (var 0) (op (var 1) (var 0))) (var 2)) (op (var 3) (var 0))) , (var 3)) → ⊥
  cut7139  adequate = bad7139  (Adequate.valid adequate Two boolean env5)
  bad7140 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b0 b0)) b0) (bop b0 b0)) b1 → ⊥
  bad7140  p = false≢true (cong lower p)
  cut7140 : Adequate {ℓ} ((op (op (op (var 0) (op (var 1) (var 0))) (var 2)) (op (var 3) (var 0))) , (var 4)) → ⊥
  cut7140  adequate = bad7140  (Adequate.valid adequate Two boolean env9)
  bad7141 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b0 b0)) b1) (bop b0 b0)) b0 → ⊥
  bad7141  p = false≢true (sym (cong lower p))
  cut7141 : Adequate {ℓ} ((op (op (op (var 0) (op (var 1) (var 0))) (var 2)) (op (var 3) (var 1))) , (var 0)) → ⊥
  cut7141  adequate = bad7141  (Adequate.valid adequate Two boolean env8)
  bad7142 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b0 b0)) b1) (bop b0 b0)) b0 → ⊥
  bad7142  p = false≢true (sym (cong lower p))
  cut7142 : Adequate {ℓ} ((op (op (op (var 0) (op (var 1) (var 0))) (var 2)) (op (var 3) (var 1))) , (var 1)) → ⊥
  cut7142  adequate = bad7142  (Adequate.valid adequate Two boolean env8)
  bad7143 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b1 b0)) b0) (bop b1 b1)) b0 → ⊥
  bad7143  p = false≢true (sym (cong lower p))
  cut7143 : Adequate {ℓ} ((op (op (op (var 0) (op (var 1) (var 0))) (var 2)) (op (var 3) (var 1))) , (var 2)) → ⊥
  cut7143  adequate = bad7143  (Adequate.valid adequate Two boolean env13)
  bad7144 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b0 b0)) b0) (bop b1 b0)) b1 → ⊥
  bad7144  p = false≢true (cong lower p)
  cut7144 : Adequate {ℓ} ((op (op (op (var 0) (op (var 1) (var 0))) (var 2)) (op (var 3) (var 1))) , (var 3)) → ⊥
  cut7144  adequate = bad7144  (Adequate.valid adequate Two boolean env5)
  bad7145 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b0 b0)) b0) (bop b0 b0)) b1 → ⊥
  bad7145  p = false≢true (cong lower p)
  cut7145 : Adequate {ℓ} ((op (op (op (var 0) (op (var 1) (var 0))) (var 2)) (op (var 3) (var 1))) , (var 4)) → ⊥
  cut7145  adequate = bad7145  (Adequate.valid adequate Two boolean env9)
  bad7146 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b0 b0)) b1) (bop b0 b1)) b0 → ⊥
  bad7146  p = false≢true (sym (cong lower p))
  cut7146 : Adequate {ℓ} ((op (op (op (var 0) (op (var 1) (var 0))) (var 2)) (op (var 3) (var 2))) , (var 0)) → ⊥
  cut7146  adequate = bad7146  (Adequate.valid adequate Two boolean env8)
  bad7147 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b0 b0)) b1) (bop b0 b1)) b0 → ⊥
  bad7147  p = false≢true (sym (cong lower p))
  cut7147 : Adequate {ℓ} ((op (op (op (var 0) (op (var 1) (var 0))) (var 2)) (op (var 3) (var 2))) , (var 1)) → ⊥
  cut7147  adequate = bad7147  (Adequate.valid adequate Two boolean env8)
  bad7148 : PathP (λ _ → Two) (bop (bop (bop b1 (bop b0 b1)) b1) (bop b0 b1)) b1 → ⊥
  bad7148  p = false≢true (cong lower p)
  cut7148 : Adequate {ℓ} ((op (op (op (var 0) (op (var 1) (var 0))) (var 2)) (op (var 3) (var 2))) , (var 2)) → ⊥
  cut7148  adequate = bad7148  (Adequate.valid adequate Two boolean env14)
  bad7149 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b0 b0)) b0) (bop b1 b0)) b1 → ⊥
  bad7149  p = false≢true (cong lower p)
  cut7149 : Adequate {ℓ} ((op (op (op (var 0) (op (var 1) (var 0))) (var 2)) (op (var 3) (var 2))) , (var 3)) → ⊥
  cut7149  adequate = bad7149  (Adequate.valid adequate Two boolean env5)
  bad7150 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b0 b0)) b0) (bop b0 b0)) b1 → ⊥
  bad7150  p = false≢true (cong lower p)
  cut7150 : Adequate {ℓ} ((op (op (op (var 0) (op (var 1) (var 0))) (var 2)) (op (var 3) (var 2))) , (var 4)) → ⊥
  cut7150  adequate = bad7150  (Adequate.valid adequate Two boolean env9)
  bad7151 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b0 b0)) b0) (bop b1 b1)) b0 → ⊥
  bad7151  p = false≢true (sym (cong lower p))
  cut7151 : Adequate {ℓ} ((op (op (op (var 0) (op (var 1) (var 0))) (var 2)) (op (var 3) (var 3))) , (var 0)) → ⊥
  cut7151  adequate = bad7151  (Adequate.valid adequate Two boolean env5)
  bad7152 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b0 b0)) b0) (bop b1 b1)) b0 → ⊥
  bad7152  p = false≢true (sym (cong lower p))
  cut7152 : Adequate {ℓ} ((op (op (op (var 0) (op (var 1) (var 0))) (var 2)) (op (var 3) (var 3))) , (var 1)) → ⊥
  cut7152  adequate = bad7152  (Adequate.valid adequate Two boolean env5)
  bad7153 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b0 b0)) b0) (bop b1 b1)) b0 → ⊥
  bad7153  p = false≢true (sym (cong lower p))
  cut7153 : Adequate {ℓ} ((op (op (op (var 0) (op (var 1) (var 0))) (var 2)) (op (var 3) (var 3))) , (var 2)) → ⊥
  cut7153  adequate = bad7153  (Adequate.valid adequate Two boolean env5)
  bad7154 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b0 b0)) b1) (bop b0 b0)) b0 → ⊥
  bad7154  p = false≢true (sym (cong lower p))
  cut7154 : Adequate {ℓ} ((op (op (op (var 0) (op (var 1) (var 0))) (var 2)) (op (var 3) (var 3))) , (var 3)) → ⊥
  cut7154  adequate = bad7154  (Adequate.valid adequate Two boolean env8)
  bad7155 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b0 b0)) b0) (bop b0 b0)) b1 → ⊥
  bad7155  p = false≢true (cong lower p)
  cut7155 : Adequate {ℓ} ((op (op (op (var 0) (op (var 1) (var 0))) (var 2)) (op (var 3) (var 3))) , (var 4)) → ⊥
  cut7155  adequate = bad7155  (Adequate.valid adequate Two boolean env9)
  bad7156 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b0 b0)) b0) (bop b1 b1)) b0 → ⊥
  bad7156  p = false≢true (sym (cong lower p))
  cut7156 : Adequate {ℓ} ((op (op (op (var 0) (op (var 1) (var 0))) (var 2)) (op (var 3) (var 4))) , (var 0)) → ⊥
  cut7156  adequate = bad7156  (Adequate.valid adequate Two boolean env15)
  bad7157 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b0 b0)) b0) (bop b1 b1)) b0 → ⊥
  bad7157  p = false≢true (sym (cong lower p))
  cut7157 : Adequate {ℓ} ((op (op (op (var 0) (op (var 1) (var 0))) (var 2)) (op (var 3) (var 4))) , (var 1)) → ⊥
  cut7157  adequate = bad7157  (Adequate.valid adequate Two boolean env15)
  bad7158 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b0 b0)) b0) (bop b1 b1)) b0 → ⊥
  bad7158  p = false≢true (sym (cong lower p))
  cut7158 : Adequate {ℓ} ((op (op (op (var 0) (op (var 1) (var 0))) (var 2)) (op (var 3) (var 4))) , (var 2)) → ⊥
  cut7158  adequate = bad7158  (Adequate.valid adequate Two boolean env15)
  bad7159 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b0 b0)) b0) (bop b1 b0)) b1 → ⊥
  bad7159  p = false≢true (cong lower p)
  cut7159 : Adequate {ℓ} ((op (op (op (var 0) (op (var 1) (var 0))) (var 2)) (op (var 3) (var 4))) , (var 3)) → ⊥
  cut7159  adequate = bad7159  (Adequate.valid adequate Two boolean env16)
  bad7160 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b0 b0)) b0) (bop b0 b1)) b1 → ⊥
  bad7160  p = false≢true (cong lower p)
  cut7160 : Adequate {ℓ} ((op (op (op (var 0) (op (var 1) (var 0))) (var 2)) (op (var 3) (var 4))) , (var 4)) → ⊥
  cut7160  adequate = bad7160  (Adequate.valid adequate Two boolean env9)
  bad7161 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b0 b0)) b0) (bop b0 b0)) b1 → ⊥
  bad7161  p = false≢true (cong lower p)
  cut7161 : Adequate {ℓ} ((op (op (op (var 0) (op (var 1) (var 0))) (var 2)) (op (var 3) (var 4))) , (var 5)) → ⊥
  cut7161  adequate = bad7161  (Adequate.valid adequate Two boolean env17)
  holds7162 : (z0 z1 : A2) → (mul2 (mul2 (mul2 z0 (mul2 z1 z1)) z0) (mul2 z0 z0)) ≡ z0
  holds7162 z0 z1 = refl
  cut7162 : Adequate {ℓ} ((op (op (op (var 0) (op (var 1) (var 1))) (var 0)) (op (var 0) (var 0))) , (var 0)) → ⊥
  cut7162  = reject2 ((op (op (op (var 0) (op (var 1) (var 1))) (var 0)) (op (var 0) (var 0))) , (var 0)) (λ env → holds7162 (env 0) (env 1))
  bad7163 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b1 b1)) b0) (bop b0 b0)) b1 → ⊥
  bad7163  p = false≢true (cong lower p)
  cut7163 : Adequate {ℓ} ((op (op (op (var 0) (op (var 1) (var 1))) (var 0)) (op (var 0) (var 0))) , (var 1)) → ⊥
  cut7163  adequate = bad7163  (Adequate.valid adequate Two boolean env0)
  bad7164 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b0 b0)) b0) (bop b0 b0)) b1 → ⊥
  bad7164  p = false≢true (cong lower p)
  cut7164 : Adequate {ℓ} ((op (op (op (var 0) (op (var 1) (var 1))) (var 0)) (op (var 0) (var 0))) , (var 2)) → ⊥
  cut7164  adequate = bad7164  (Adequate.valid adequate Two boolean env1)
  bad7165 : PathP (λ _ → Two) (bop (bop (bop b1 (bop b0 b0)) b1) (bop b1 b0)) b1 → ⊥
  bad7165  p = false≢true (cong lower p)
  cut7165 : Adequate {ℓ} ((op (op (op (var 0) (op (var 1) (var 1))) (var 0)) (op (var 0) (var 1))) , (var 0)) → ⊥
  cut7165  adequate = bad7165  (Adequate.valid adequate Two boolean env2)
  bad7166 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b1 b1)) b0) (bop b0 b1)) b1 → ⊥
  bad7166  p = false≢true (cong lower p)
  cut7166 : Adequate {ℓ} ((op (op (op (var 0) (op (var 1) (var 1))) (var 0)) (op (var 0) (var 1))) , (var 1)) → ⊥
  cut7166  adequate = bad7166  (Adequate.valid adequate Two boolean env0)
  bad7167 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b0 b0)) b0) (bop b0 b0)) b1 → ⊥
  bad7167  p = false≢true (cong lower p)
  cut7167 : Adequate {ℓ} ((op (op (op (var 0) (op (var 1) (var 1))) (var 0)) (op (var 0) (var 1))) , (var 2)) → ⊥
  cut7167  adequate = bad7167  (Adequate.valid adequate Two boolean env1)
  bad7168 : PathP (λ _ → Two) (bop (bop (bop b1 (bop b0 b0)) b1) (bop b1 b0)) b1 → ⊥
  bad7168  p = false≢true (cong lower p)
  cut7168 : Adequate {ℓ} ((op (op (op (var 0) (op (var 1) (var 1))) (var 0)) (op (var 0) (var 2))) , (var 0)) → ⊥
  cut7168  adequate = bad7168  (Adequate.valid adequate Two boolean env10)
  bad7169 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b1 b1)) b0) (bop b0 b0)) b1 → ⊥
  bad7169  p = false≢true (cong lower p)
  cut7169 : Adequate {ℓ} ((op (op (op (var 0) (op (var 1) (var 1))) (var 0)) (op (var 0) (var 2))) , (var 1)) → ⊥
  cut7169  adequate = bad7169  (Adequate.valid adequate Two boolean env4)
  bad7170 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b0 b0)) b0) (bop b0 b1)) b1 → ⊥
  bad7170  p = false≢true (cong lower p)
  cut7170 : Adequate {ℓ} ((op (op (op (var 0) (op (var 1) (var 1))) (var 0)) (op (var 0) (var 2))) , (var 2)) → ⊥
  cut7170  adequate = bad7170  (Adequate.valid adequate Two boolean env1)
  bad7171 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b0 b0)) b0) (bop b0 b0)) b1 → ⊥
  bad7171  p = false≢true (cong lower p)
  cut7171 : Adequate {ℓ} ((op (op (op (var 0) (op (var 1) (var 1))) (var 0)) (op (var 0) (var 2))) , (var 3)) → ⊥
  cut7171  adequate = bad7171  (Adequate.valid adequate Two boolean env5)
  bad7172 : PathP (λ _ → Two) (bop (bop (bop b1 (bop b0 b0)) b1) (bop b0 b1)) b1 → ⊥
  bad7172  p = false≢true (cong lower p)
  cut7172 : Adequate {ℓ} ((op (op (op (var 0) (op (var 1) (var 1))) (var 0)) (op (var 1) (var 0))) , (var 0)) → ⊥
  cut7172  adequate = bad7172  (Adequate.valid adequate Two boolean env2)
  bad7173 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b1 b1)) b0) (bop b1 b0)) b1 → ⊥
  bad7173  p = false≢true (cong lower p)
  cut7173 : Adequate {ℓ} ((op (op (op (var 0) (op (var 1) (var 1))) (var 0)) (op (var 1) (var 0))) , (var 1)) → ⊥
  cut7173  adequate = bad7173  (Adequate.valid adequate Two boolean env0)
  bad7174 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b0 b0)) b0) (bop b0 b0)) b1 → ⊥
  bad7174  p = false≢true (cong lower p)
  cut7174 : Adequate {ℓ} ((op (op (op (var 0) (op (var 1) (var 1))) (var 0)) (op (var 1) (var 0))) , (var 2)) → ⊥
  cut7174  adequate = bad7174  (Adequate.valid adequate Two boolean env1)
  bad7175 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b1 b1)) b0) (bop b1 b1)) b0 → ⊥
  bad7175  p = false≢true (sym (cong lower p))
  cut7175 : Adequate {ℓ} ((op (op (op (var 0) (op (var 1) (var 1))) (var 0)) (op (var 1) (var 1))) , (var 0)) → ⊥
  cut7175  adequate = bad7175  (Adequate.valid adequate Two boolean env0)
  holds7176 : (z0 z1 : A3) → (mul3 (mul3 (mul3 z0 (mul3 z1 z1)) z0) (mul3 z1 z1)) ≡ z1
  holds7176 z0 z1 = refl
  cut7176 : Adequate {ℓ} ((op (op (op (var 0) (op (var 1) (var 1))) (var 0)) (op (var 1) (var 1))) , (var 1)) → ⊥
  cut7176  = reject3 ((op (op (op (var 0) (op (var 1) (var 1))) (var 0)) (op (var 1) (var 1))) , (var 1)) (λ env → holds7176 (env 0) (env 1))
  bad7177 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b0 b0)) b0) (bop b0 b0)) b1 → ⊥
  bad7177  p = false≢true (cong lower p)
  cut7177 : Adequate {ℓ} ((op (op (op (var 0) (op (var 1) (var 1))) (var 0)) (op (var 1) (var 1))) , (var 2)) → ⊥
  cut7177  adequate = bad7177  (Adequate.valid adequate Two boolean env1)
  bad7178 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b1 b1)) b0) (bop b1 b1)) b0 → ⊥
  bad7178  p = false≢true (sym (cong lower p))
  cut7178 : Adequate {ℓ} ((op (op (op (var 0) (op (var 1) (var 1))) (var 0)) (op (var 1) (var 2))) , (var 0)) → ⊥
  cut7178  adequate = bad7178  (Adequate.valid adequate Two boolean env3)
  bad7179 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b1 b1)) b0) (bop b1 b0)) b1 → ⊥
  bad7179  p = false≢true (cong lower p)
  cut7179 : Adequate {ℓ} ((op (op (op (var 0) (op (var 1) (var 1))) (var 0)) (op (var 1) (var 2))) , (var 1)) → ⊥
  cut7179  adequate = bad7179  (Adequate.valid adequate Two boolean env4)
  bad7180 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b0 b0)) b0) (bop b0 b1)) b1 → ⊥
  bad7180  p = false≢true (cong lower p)
  cut7180 : Adequate {ℓ} ((op (op (op (var 0) (op (var 1) (var 1))) (var 0)) (op (var 1) (var 2))) , (var 2)) → ⊥
  cut7180  adequate = bad7180  (Adequate.valid adequate Two boolean env1)
  bad7181 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b0 b0)) b0) (bop b0 b0)) b1 → ⊥
  bad7181  p = false≢true (cong lower p)
  cut7181 : Adequate {ℓ} ((op (op (op (var 0) (op (var 1) (var 1))) (var 0)) (op (var 1) (var 2))) , (var 3)) → ⊥
  cut7181  adequate = bad7181  (Adequate.valid adequate Two boolean env5)
  bad7182 : PathP (λ _ → Two) (bop (bop (bop b1 (bop b0 b0)) b1) (bop b0 b1)) b1 → ⊥
  bad7182  p = false≢true (cong lower p)
  cut7182 : Adequate {ℓ} ((op (op (op (var 0) (op (var 1) (var 1))) (var 0)) (op (var 2) (var 0))) , (var 0)) → ⊥
  cut7182  adequate = bad7182  (Adequate.valid adequate Two boolean env10)
  bad7183 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b1 b1)) b0) (bop b0 b0)) b1 → ⊥
  bad7183  p = false≢true (cong lower p)
  cut7183 : Adequate {ℓ} ((op (op (op (var 0) (op (var 1) (var 1))) (var 0)) (op (var 2) (var 0))) , (var 1)) → ⊥
  cut7183  adequate = bad7183  (Adequate.valid adequate Two boolean env4)
  bad7184 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b0 b0)) b0) (bop b1 b0)) b1 → ⊥
  bad7184  p = false≢true (cong lower p)
  cut7184 : Adequate {ℓ} ((op (op (op (var 0) (op (var 1) (var 1))) (var 0)) (op (var 2) (var 0))) , (var 2)) → ⊥
  cut7184  adequate = bad7184  (Adequate.valid adequate Two boolean env1)
  bad7185 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b0 b0)) b0) (bop b0 b0)) b1 → ⊥
  bad7185  p = false≢true (cong lower p)
  cut7185 : Adequate {ℓ} ((op (op (op (var 0) (op (var 1) (var 1))) (var 0)) (op (var 2) (var 0))) , (var 3)) → ⊥
  cut7185  adequate = bad7185  (Adequate.valid adequate Two boolean env5)
  bad7186 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b1 b1)) b0) (bop b1 b1)) b0 → ⊥
  bad7186  p = false≢true (sym (cong lower p))
  cut7186 : Adequate {ℓ} ((op (op (op (var 0) (op (var 1) (var 1))) (var 0)) (op (var 2) (var 1))) , (var 0)) → ⊥
  cut7186  adequate = bad7186  (Adequate.valid adequate Two boolean env3)
  bad7187 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b1 b1)) b0) (bop b0 b1)) b1 → ⊥
  bad7187  p = false≢true (cong lower p)
  cut7187 : Adequate {ℓ} ((op (op (op (var 0) (op (var 1) (var 1))) (var 0)) (op (var 2) (var 1))) , (var 1)) → ⊥
  cut7187  adequate = bad7187  (Adequate.valid adequate Two boolean env4)
  bad7188 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b0 b0)) b0) (bop b1 b0)) b1 → ⊥
  bad7188  p = false≢true (cong lower p)
  cut7188 : Adequate {ℓ} ((op (op (op (var 0) (op (var 1) (var 1))) (var 0)) (op (var 2) (var 1))) , (var 2)) → ⊥
  cut7188  adequate = bad7188  (Adequate.valid adequate Two boolean env1)
  bad7189 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b0 b0)) b0) (bop b0 b0)) b1 → ⊥
  bad7189  p = false≢true (cong lower p)
  cut7189 : Adequate {ℓ} ((op (op (op (var 0) (op (var 1) (var 1))) (var 0)) (op (var 2) (var 1))) , (var 3)) → ⊥
  cut7189  adequate = bad7189  (Adequate.valid adequate Two boolean env5)
  bad7190 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b0 b0)) b0) (bop b1 b1)) b0 → ⊥
  bad7190  p = false≢true (sym (cong lower p))
  cut7190 : Adequate {ℓ} ((op (op (op (var 0) (op (var 1) (var 1))) (var 0)) (op (var 2) (var 2))) , (var 0)) → ⊥
  cut7190  adequate = bad7190  (Adequate.valid adequate Two boolean env1)
  bad7191 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b0 b0)) b0) (bop b1 b1)) b0 → ⊥
  bad7191  p = false≢true (sym (cong lower p))
  cut7191 : Adequate {ℓ} ((op (op (op (var 0) (op (var 1) (var 1))) (var 0)) (op (var 2) (var 2))) , (var 1)) → ⊥
  cut7191  adequate = bad7191  (Adequate.valid adequate Two boolean env1)
  bad7192 : PathP (λ _ → Two) (bop (bop (bop b1 (bop b1 b1)) b1) (bop b0 b0)) b0 → ⊥
  bad7192  p = false≢true (sym (cong lower p))
  cut7192 : Adequate {ℓ} ((op (op (op (var 0) (op (var 1) (var 1))) (var 0)) (op (var 2) (var 2))) , (var 2)) → ⊥
  cut7192  adequate = bad7192  (Adequate.valid adequate Two boolean env11)
  bad7193 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b0 b0)) b0) (bop b0 b0)) b1 → ⊥
  bad7193  p = false≢true (cong lower p)
  cut7193 : Adequate {ℓ} ((op (op (op (var 0) (op (var 1) (var 1))) (var 0)) (op (var 2) (var 2))) , (var 3)) → ⊥
  cut7193  adequate = bad7193  (Adequate.valid adequate Two boolean env5)
  bad7194 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b0 b0)) b0) (bop b1 b1)) b0 → ⊥
  bad7194  p = false≢true (sym (cong lower p))
  cut7194 : Adequate {ℓ} ((op (op (op (var 0) (op (var 1) (var 1))) (var 0)) (op (var 2) (var 3))) , (var 0)) → ⊥
  cut7194  adequate = bad7194  (Adequate.valid adequate Two boolean env7)
  bad7195 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b0 b0)) b0) (bop b1 b1)) b0 → ⊥
  bad7195  p = false≢true (sym (cong lower p))
  cut7195 : Adequate {ℓ} ((op (op (op (var 0) (op (var 1) (var 1))) (var 0)) (op (var 2) (var 3))) , (var 1)) → ⊥
  cut7195  adequate = bad7195  (Adequate.valid adequate Two boolean env7)
  bad7196 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b0 b0)) b0) (bop b1 b0)) b1 → ⊥
  bad7196  p = false≢true (cong lower p)
  cut7196 : Adequate {ℓ} ((op (op (op (var 0) (op (var 1) (var 1))) (var 0)) (op (var 2) (var 3))) , (var 2)) → ⊥
  cut7196  adequate = bad7196  (Adequate.valid adequate Two boolean env8)
  bad7197 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b0 b0)) b0) (bop b0 b1)) b1 → ⊥
  bad7197  p = false≢true (cong lower p)
  cut7197 : Adequate {ℓ} ((op (op (op (var 0) (op (var 1) (var 1))) (var 0)) (op (var 2) (var 3))) , (var 3)) → ⊥
  cut7197  adequate = bad7197  (Adequate.valid adequate Two boolean env5)
  bad7198 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b0 b0)) b0) (bop b0 b0)) b1 → ⊥
  bad7198  p = false≢true (cong lower p)
  cut7198 : Adequate {ℓ} ((op (op (op (var 0) (op (var 1) (var 1))) (var 0)) (op (var 2) (var 3))) , (var 4)) → ⊥
  cut7198  adequate = bad7198  (Adequate.valid adequate Two boolean env9)
  bad7199 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b1 b1)) b1) (bop b0 b0)) b0 → ⊥
  bad7199  p = false≢true (sym (cong lower p))
  cut7199 : Adequate {ℓ} ((op (op (op (var 0) (op (var 1) (var 1))) (var 1)) (op (var 0) (var 0))) , (var 0)) → ⊥
  cut7199  adequate = bad7199  (Adequate.valid adequate Two boolean env0)
  bad7200 : PathP (λ _ → Two) (bop (bop (bop b1 (bop b0 b0)) b0) (bop b1 b1)) b0 → ⊥
  bad7200  p = false≢true (sym (cong lower p))
  cut7200 : Adequate {ℓ} ((op (op (op (var 0) (op (var 1) (var 1))) (var 1)) (op (var 0) (var 0))) , (var 1)) → ⊥
  cut7200  adequate = bad7200  (Adequate.valid adequate Two boolean env2)
  bad7201 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b0 b0)) b0) (bop b0 b0)) b1 → ⊥
  bad7201  p = false≢true (cong lower p)
  cut7201 : Adequate {ℓ} ((op (op (op (var 0) (op (var 1) (var 1))) (var 1)) (op (var 0) (var 0))) , (var 2)) → ⊥
  cut7201  adequate = bad7201  (Adequate.valid adequate Two boolean env1)
  bad7202 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b1 b1)) b1) (bop b0 b1)) b0 → ⊥
  bad7202  p = false≢true (sym (cong lower p))
  cut7202 : Adequate {ℓ} ((op (op (op (var 0) (op (var 1) (var 1))) (var 1)) (op (var 0) (var 1))) , (var 0)) → ⊥
  cut7202  adequate = bad7202  (Adequate.valid adequate Two boolean env0)
  holds7203 : (z0 z1 : A3) → (mul3 (mul3 (mul3 z0 (mul3 z1 z1)) z1) (mul3 z0 z1)) ≡ z1
  holds7203 z0 z1 = refl
  cut7203 : Adequate {ℓ} ((op (op (op (var 0) (op (var 1) (var 1))) (var 1)) (op (var 0) (var 1))) , (var 1)) → ⊥
  cut7203  = reject3 ((op (op (op (var 0) (op (var 1) (var 1))) (var 1)) (op (var 0) (var 1))) , (var 1)) (λ env → holds7203 (env 0) (env 1))
  bad7204 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b0 b0)) b0) (bop b0 b0)) b1 → ⊥
  bad7204  p = false≢true (cong lower p)
  cut7204 : Adequate {ℓ} ((op (op (op (var 0) (op (var 1) (var 1))) (var 1)) (op (var 0) (var 1))) , (var 2)) → ⊥
  cut7204  adequate = bad7204  (Adequate.valid adequate Two boolean env1)
  bad7205 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b1 b1)) b1) (bop b0 b0)) b0 → ⊥
  bad7205  p = false≢true (sym (cong lower p))
  cut7205 : Adequate {ℓ} ((op (op (op (var 0) (op (var 1) (var 1))) (var 1)) (op (var 0) (var 2))) , (var 0)) → ⊥
  cut7205  adequate = bad7205  (Adequate.valid adequate Two boolean env4)
  bad7206 : PathP (λ _ → Two) (bop (bop (bop b1 (bop b0 b0)) b0) (bop b1 b1)) b0 → ⊥
  bad7206  p = false≢true (sym (cong lower p))
  cut7206 : Adequate {ℓ} ((op (op (op (var 0) (op (var 1) (var 1))) (var 1)) (op (var 0) (var 2))) , (var 1)) → ⊥
  cut7206  adequate = bad7206  (Adequate.valid adequate Two boolean env6)
  bad7207 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b0 b0)) b0) (bop b0 b1)) b1 → ⊥
  bad7207  p = false≢true (cong lower p)
  cut7207 : Adequate {ℓ} ((op (op (op (var 0) (op (var 1) (var 1))) (var 1)) (op (var 0) (var 2))) , (var 2)) → ⊥
  cut7207  adequate = bad7207  (Adequate.valid adequate Two boolean env1)
  bad7208 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b0 b0)) b0) (bop b0 b0)) b1 → ⊥
  bad7208  p = false≢true (cong lower p)
  cut7208 : Adequate {ℓ} ((op (op (op (var 0) (op (var 1) (var 1))) (var 1)) (op (var 0) (var 2))) , (var 3)) → ⊥
  cut7208  adequate = bad7208  (Adequate.valid adequate Two boolean env5)
  bad7209 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b1 b1)) b1) (bop b1 b0)) b0 → ⊥
  bad7209  p = false≢true (sym (cong lower p))
  cut7209 : Adequate {ℓ} ((op (op (op (var 0) (op (var 1) (var 1))) (var 1)) (op (var 1) (var 0))) , (var 0)) → ⊥
  cut7209  adequate = bad7209  (Adequate.valid adequate Two boolean env0)
  holds7210 : (z0 z1 : A5) → (mul5 (mul5 (mul5 z0 (mul5 z1 z1)) z1) (mul5 z1 z0)) ≡ z1
  holds7210 m5c0 m5c0 = refl
  holds7210 m5c0 m5c1 = refl
  holds7210 m5c0 m5c2 = refl
  holds7210 m5c1 m5c0 = refl
  holds7210 m5c1 m5c1 = refl
  holds7210 m5c1 m5c2 = refl
  holds7210 m5c2 m5c0 = refl
  holds7210 m5c2 m5c1 = refl
  holds7210 m5c2 m5c2 = refl
  cut7210 : Adequate {ℓ} ((op (op (op (var 0) (op (var 1) (var 1))) (var 1)) (op (var 1) (var 0))) , (var 1)) → ⊥
  cut7210  = reject5 ((op (op (op (var 0) (op (var 1) (var 1))) (var 1)) (op (var 1) (var 0))) , (var 1)) (λ env → holds7210 (env 0) (env 1))
  bad7211 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b0 b0)) b0) (bop b0 b0)) b1 → ⊥
  bad7211  p = false≢true (cong lower p)
  cut7211 : Adequate {ℓ} ((op (op (op (var 0) (op (var 1) (var 1))) (var 1)) (op (var 1) (var 0))) , (var 2)) → ⊥
  cut7211  adequate = bad7211  (Adequate.valid adequate Two boolean env1)
  bad7212 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b1 b1)) b1) (bop b1 b1)) b0 → ⊥
  bad7212  p = false≢true (sym (cong lower p))
  cut7212 : Adequate {ℓ} ((op (op (op (var 0) (op (var 1) (var 1))) (var 1)) (op (var 1) (var 1))) , (var 0)) → ⊥
  cut7212  adequate = bad7212  (Adequate.valid adequate Two boolean env0)
  holds7213 : (z0 z1 : A3) → (mul3 (mul3 (mul3 z0 (mul3 z1 z1)) z1) (mul3 z1 z1)) ≡ z1
  holds7213 z0 z1 = refl
  cut7213 : Adequate {ℓ} ((op (op (op (var 0) (op (var 1) (var 1))) (var 1)) (op (var 1) (var 1))) , (var 1)) → ⊥
  cut7213  = reject3 ((op (op (op (var 0) (op (var 1) (var 1))) (var 1)) (op (var 1) (var 1))) , (var 1)) (λ env → holds7213 (env 0) (env 1))
  bad7214 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b0 b0)) b0) (bop b0 b0)) b1 → ⊥
  bad7214  p = false≢true (cong lower p)
  cut7214 : Adequate {ℓ} ((op (op (op (var 0) (op (var 1) (var 1))) (var 1)) (op (var 1) (var 1))) , (var 2)) → ⊥
  cut7214  adequate = bad7214  (Adequate.valid adequate Two boolean env1)
  bad7215 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b1 b1)) b1) (bop b1 b0)) b0 → ⊥
  bad7215  p = false≢true (sym (cong lower p))
  cut7215 : Adequate {ℓ} ((op (op (op (var 0) (op (var 1) (var 1))) (var 1)) (op (var 1) (var 2))) , (var 0)) → ⊥
  cut7215  adequate = bad7215  (Adequate.valid adequate Two boolean env4)
  holds7216 : (z0 z1 z2 : A10) → (mul10 (mul10 (mul10 z0 (mul10 z1 z1)) z1) (mul10 z1 z2)) ≡ z1
  holds7216 m10c0 m10c0 m10c0 = refl
  holds7216 m10c0 m10c0 m10c1 = refl
  holds7216 m10c0 m10c0 m10c2 = refl
  holds7216 m10c0 m10c1 z2 = refl
  holds7216 m10c0 m10c2 z2 = refl
  holds7216 m10c1 m10c0 m10c0 = refl
  holds7216 m10c1 m10c0 m10c1 = refl
  holds7216 m10c1 m10c0 m10c2 = refl
  holds7216 m10c1 m10c1 z2 = refl
  holds7216 m10c1 m10c2 z2 = refl
  holds7216 m10c2 m10c0 m10c0 = refl
  holds7216 m10c2 m10c0 m10c1 = refl
  holds7216 m10c2 m10c0 m10c2 = refl
  holds7216 m10c2 m10c1 z2 = refl
  holds7216 m10c2 m10c2 z2 = refl
  cut7216 : Adequate {ℓ} ((op (op (op (var 0) (op (var 1) (var 1))) (var 1)) (op (var 1) (var 2))) , (var 1)) → ⊥
  cut7216  = reject10 ((op (op (op (var 0) (op (var 1) (var 1))) (var 1)) (op (var 1) (var 2))) , (var 1)) (λ env → holds7216 (env 0) (env 1) (env 2))
  bad7217 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b0 b0)) b0) (bop b0 b1)) b1 → ⊥
  bad7217  p = false≢true (cong lower p)
  cut7217 : Adequate {ℓ} ((op (op (op (var 0) (op (var 1) (var 1))) (var 1)) (op (var 1) (var 2))) , (var 2)) → ⊥
  cut7217  adequate = bad7217  (Adequate.valid adequate Two boolean env1)
  bad7218 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b0 b0)) b0) (bop b0 b0)) b1 → ⊥
  bad7218  p = false≢true (cong lower p)
  cut7218 : Adequate {ℓ} ((op (op (op (var 0) (op (var 1) (var 1))) (var 1)) (op (var 1) (var 2))) , (var 3)) → ⊥
  cut7218  adequate = bad7218  (Adequate.valid adequate Two boolean env5)
  bad7219 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b1 b1)) b1) (bop b0 b0)) b0 → ⊥
  bad7219  p = false≢true (sym (cong lower p))
  cut7219 : Adequate {ℓ} ((op (op (op (var 0) (op (var 1) (var 1))) (var 1)) (op (var 2) (var 0))) , (var 0)) → ⊥
  cut7219  adequate = bad7219  (Adequate.valid adequate Two boolean env4)
  bad7220 : PathP (λ _ → Two) (bop (bop (bop b1 (bop b0 b0)) b0) (bop b1 b1)) b0 → ⊥
  bad7220  p = false≢true (sym (cong lower p))
  cut7220 : Adequate {ℓ} ((op (op (op (var 0) (op (var 1) (var 1))) (var 1)) (op (var 2) (var 0))) , (var 1)) → ⊥
  cut7220  adequate = bad7220  (Adequate.valid adequate Two boolean env6)
  bad7221 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b0 b0)) b0) (bop b1 b0)) b1 → ⊥
  bad7221  p = false≢true (cong lower p)
  cut7221 : Adequate {ℓ} ((op (op (op (var 0) (op (var 1) (var 1))) (var 1)) (op (var 2) (var 0))) , (var 2)) → ⊥
  cut7221  adequate = bad7221  (Adequate.valid adequate Two boolean env1)
  bad7222 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b0 b0)) b0) (bop b0 b0)) b1 → ⊥
  bad7222  p = false≢true (cong lower p)
  cut7222 : Adequate {ℓ} ((op (op (op (var 0) (op (var 1) (var 1))) (var 1)) (op (var 2) (var 0))) , (var 3)) → ⊥
  cut7222  adequate = bad7222  (Adequate.valid adequate Two boolean env5)
  bad7223 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b1 b1)) b1) (bop b0 b1)) b0 → ⊥
  bad7223  p = false≢true (sym (cong lower p))
  cut7223 : Adequate {ℓ} ((op (op (op (var 0) (op (var 1) (var 1))) (var 1)) (op (var 2) (var 1))) , (var 0)) → ⊥
  cut7223  adequate = bad7223  (Adequate.valid adequate Two boolean env4)
  holds7224 : (z0 z1 z2 : A3) → (mul3 (mul3 (mul3 z0 (mul3 z1 z1)) z1) (mul3 z2 z1)) ≡ z1
  holds7224 z0 z1 z2 = refl
  cut7224 : Adequate {ℓ} ((op (op (op (var 0) (op (var 1) (var 1))) (var 1)) (op (var 2) (var 1))) , (var 1)) → ⊥
  cut7224  = reject3 ((op (op (op (var 0) (op (var 1) (var 1))) (var 1)) (op (var 2) (var 1))) , (var 1)) (λ env → holds7224 (env 0) (env 1) (env 2))
  bad7225 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b0 b0)) b0) (bop b1 b0)) b1 → ⊥
  bad7225  p = false≢true (cong lower p)
  cut7225 : Adequate {ℓ} ((op (op (op (var 0) (op (var 1) (var 1))) (var 1)) (op (var 2) (var 1))) , (var 2)) → ⊥
  cut7225  adequate = bad7225  (Adequate.valid adequate Two boolean env1)
  bad7226 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b0 b0)) b0) (bop b0 b0)) b1 → ⊥
  bad7226  p = false≢true (cong lower p)
  cut7226 : Adequate {ℓ} ((op (op (op (var 0) (op (var 1) (var 1))) (var 1)) (op (var 2) (var 1))) , (var 3)) → ⊥
  cut7226  adequate = bad7226  (Adequate.valid adequate Two boolean env5)
  bad7227 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b0 b0)) b0) (bop b1 b1)) b0 → ⊥
  bad7227  p = false≢true (sym (cong lower p))
  cut7227 : Adequate {ℓ} ((op (op (op (var 0) (op (var 1) (var 1))) (var 1)) (op (var 2) (var 2))) , (var 0)) → ⊥
  cut7227  adequate = bad7227  (Adequate.valid adequate Two boolean env1)
  bad7228 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b0 b0)) b0) (bop b1 b1)) b0 → ⊥
  bad7228  p = false≢true (sym (cong lower p))
  cut7228 : Adequate {ℓ} ((op (op (op (var 0) (op (var 1) (var 1))) (var 1)) (op (var 2) (var 2))) , (var 1)) → ⊥
  cut7228  adequate = bad7228  (Adequate.valid adequate Two boolean env1)
  bad7229 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b1 b1)) b1) (bop b0 b0)) b0 → ⊥
  bad7229  p = false≢true (sym (cong lower p))
  cut7229 : Adequate {ℓ} ((op (op (op (var 0) (op (var 1) (var 1))) (var 1)) (op (var 2) (var 2))) , (var 2)) → ⊥
  cut7229  adequate = bad7229  (Adequate.valid adequate Two boolean env4)
  bad7230 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b0 b0)) b0) (bop b0 b0)) b1 → ⊥
  bad7230  p = false≢true (cong lower p)
  cut7230 : Adequate {ℓ} ((op (op (op (var 0) (op (var 1) (var 1))) (var 1)) (op (var 2) (var 2))) , (var 3)) → ⊥
  cut7230  adequate = bad7230  (Adequate.valid adequate Two boolean env5)
  bad7231 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b0 b0)) b0) (bop b1 b1)) b0 → ⊥
  bad7231  p = false≢true (sym (cong lower p))
  cut7231 : Adequate {ℓ} ((op (op (op (var 0) (op (var 1) (var 1))) (var 1)) (op (var 2) (var 3))) , (var 0)) → ⊥
  cut7231  adequate = bad7231  (Adequate.valid adequate Two boolean env7)
  bad7232 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b0 b0)) b0) (bop b1 b1)) b0 → ⊥
  bad7232  p = false≢true (sym (cong lower p))
  cut7232 : Adequate {ℓ} ((op (op (op (var 0) (op (var 1) (var 1))) (var 1)) (op (var 2) (var 3))) , (var 1)) → ⊥
  cut7232  adequate = bad7232  (Adequate.valid adequate Two boolean env7)
  bad7233 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b0 b0)) b0) (bop b1 b0)) b1 → ⊥
  bad7233  p = false≢true (cong lower p)
  cut7233 : Adequate {ℓ} ((op (op (op (var 0) (op (var 1) (var 1))) (var 1)) (op (var 2) (var 3))) , (var 2)) → ⊥
  cut7233  adequate = bad7233  (Adequate.valid adequate Two boolean env8)
  bad7234 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b0 b0)) b0) (bop b0 b1)) b1 → ⊥
  bad7234  p = false≢true (cong lower p)
  cut7234 : Adequate {ℓ} ((op (op (op (var 0) (op (var 1) (var 1))) (var 1)) (op (var 2) (var 3))) , (var 3)) → ⊥
  cut7234  adequate = bad7234  (Adequate.valid adequate Two boolean env5)
  bad7235 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b0 b0)) b0) (bop b0 b0)) b1 → ⊥
  bad7235  p = false≢true (cong lower p)
  cut7235 : Adequate {ℓ} ((op (op (op (var 0) (op (var 1) (var 1))) (var 1)) (op (var 2) (var 3))) , (var 4)) → ⊥
  cut7235  adequate = bad7235  (Adequate.valid adequate Two boolean env9)
  bad7236 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b0 b0)) b1) (bop b0 b0)) b0 → ⊥
  bad7236  p = false≢true (sym (cong lower p))
  cut7236 : Adequate {ℓ} ((op (op (op (var 0) (op (var 1) (var 1))) (var 2)) (op (var 0) (var 0))) , (var 0)) → ⊥
  cut7236  adequate = bad7236  (Adequate.valid adequate Two boolean env1)
  bad7237 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b0 b0)) b1) (bop b0 b0)) b0 → ⊥
  bad7237  p = false≢true (sym (cong lower p))
  cut7237 : Adequate {ℓ} ((op (op (op (var 0) (op (var 1) (var 1))) (var 2)) (op (var 0) (var 0))) , (var 1)) → ⊥
  cut7237  adequate = bad7237  (Adequate.valid adequate Two boolean env1)
  bad7238 : PathP (λ _ → Two) (bop (bop (bop b1 (bop b0 b0)) b0) (bop b1 b1)) b0 → ⊥
  bad7238  p = false≢true (sym (cong lower p))
  cut7238 : Adequate {ℓ} ((op (op (op (var 0) (op (var 1) (var 1))) (var 2)) (op (var 0) (var 0))) , (var 2)) → ⊥
  cut7238  adequate = bad7238  (Adequate.valid adequate Two boolean env10)
  bad7239 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b0 b0)) b0) (bop b0 b0)) b1 → ⊥
  bad7239  p = false≢true (cong lower p)
  cut7239 : Adequate {ℓ} ((op (op (op (var 0) (op (var 1) (var 1))) (var 2)) (op (var 0) (var 0))) , (var 3)) → ⊥
  cut7239  adequate = bad7239  (Adequate.valid adequate Two boolean env5)
  bad7240 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b0 b0)) b1) (bop b0 b0)) b0 → ⊥
  bad7240  p = false≢true (sym (cong lower p))
  cut7240 : Adequate {ℓ} ((op (op (op (var 0) (op (var 1) (var 1))) (var 2)) (op (var 0) (var 1))) , (var 0)) → ⊥
  cut7240  adequate = bad7240  (Adequate.valid adequate Two boolean env1)
  bad7241 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b0 b0)) b1) (bop b0 b0)) b0 → ⊥
  bad7241  p = false≢true (sym (cong lower p))
  cut7241 : Adequate {ℓ} ((op (op (op (var 0) (op (var 1) (var 1))) (var 2)) (op (var 0) (var 1))) , (var 1)) → ⊥
  cut7241  adequate = bad7241  (Adequate.valid adequate Two boolean env1)
  bad7242 : PathP (λ _ → Two) (bop (bop (bop b1 (bop b0 b0)) b1) (bop b1 b0)) b1 → ⊥
  bad7242  p = false≢true (cong lower p)
  cut7242 : Adequate {ℓ} ((op (op (op (var 0) (op (var 1) (var 1))) (var 2)) (op (var 0) (var 1))) , (var 2)) → ⊥
  cut7242  adequate = bad7242  (Adequate.valid adequate Two boolean env6)
  bad7243 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b0 b0)) b0) (bop b0 b0)) b1 → ⊥
  bad7243  p = false≢true (cong lower p)
  cut7243 : Adequate {ℓ} ((op (op (op (var 0) (op (var 1) (var 1))) (var 2)) (op (var 0) (var 1))) , (var 3)) → ⊥
  cut7243  adequate = bad7243  (Adequate.valid adequate Two boolean env5)
  bad7244 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b0 b0)) b1) (bop b0 b1)) b0 → ⊥
  bad7244  p = false≢true (sym (cong lower p))
  cut7244 : Adequate {ℓ} ((op (op (op (var 0) (op (var 1) (var 1))) (var 2)) (op (var 0) (var 2))) , (var 0)) → ⊥
  cut7244  adequate = bad7244  (Adequate.valid adequate Two boolean env1)
  bad7245 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b0 b0)) b1) (bop b0 b1)) b0 → ⊥
  bad7245  p = false≢true (sym (cong lower p))
  cut7245 : Adequate {ℓ} ((op (op (op (var 0) (op (var 1) (var 1))) (var 2)) (op (var 0) (var 2))) , (var 1)) → ⊥
  cut7245  adequate = bad7245  (Adequate.valid adequate Two boolean env1)
  holds7246 : (z0 z1 z2 : A3) → (mul3 (mul3 (mul3 z0 (mul3 z1 z1)) z2) (mul3 z0 z2)) ≡ z2
  holds7246 z0 z1 z2 = refl
  cut7246 : Adequate {ℓ} ((op (op (op (var 0) (op (var 1) (var 1))) (var 2)) (op (var 0) (var 2))) , (var 2)) → ⊥
  cut7246  = reject3 ((op (op (op (var 0) (op (var 1) (var 1))) (var 2)) (op (var 0) (var 2))) , (var 2)) (λ env → holds7246 (env 0) (env 1) (env 2))
  bad7247 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b0 b0)) b0) (bop b0 b0)) b1 → ⊥
  bad7247  p = false≢true (cong lower p)
  cut7247 : Adequate {ℓ} ((op (op (op (var 0) (op (var 1) (var 1))) (var 2)) (op (var 0) (var 2))) , (var 3)) → ⊥
  cut7247  adequate = bad7247  (Adequate.valid adequate Two boolean env5)
  bad7248 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b0 b0)) b1) (bop b0 b0)) b0 → ⊥
  bad7248  p = false≢true (sym (cong lower p))
  cut7248 : Adequate {ℓ} ((op (op (op (var 0) (op (var 1) (var 1))) (var 2)) (op (var 0) (var 3))) , (var 0)) → ⊥
  cut7248  adequate = bad7248  (Adequate.valid adequate Two boolean env8)
  bad7249 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b0 b0)) b1) (bop b0 b0)) b0 → ⊥
  bad7249  p = false≢true (sym (cong lower p))
  cut7249 : Adequate {ℓ} ((op (op (op (var 0) (op (var 1) (var 1))) (var 2)) (op (var 0) (var 3))) , (var 1)) → ⊥
  cut7249  adequate = bad7249  (Adequate.valid adequate Two boolean env8)
  bad7250 : PathP (λ _ → Two) (bop (bop (bop b1 (bop b0 b0)) b0) (bop b1 b1)) b0 → ⊥
  bad7250  p = false≢true (sym (cong lower p))
  cut7250 : Adequate {ℓ} ((op (op (op (var 0) (op (var 1) (var 1))) (var 2)) (op (var 0) (var 3))) , (var 2)) → ⊥
  cut7250  adequate = bad7250  (Adequate.valid adequate Two boolean env12)
  bad7251 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b0 b0)) b0) (bop b0 b1)) b1 → ⊥
  bad7251  p = false≢true (cong lower p)
  cut7251 : Adequate {ℓ} ((op (op (op (var 0) (op (var 1) (var 1))) (var 2)) (op (var 0) (var 3))) , (var 3)) → ⊥
  cut7251  adequate = bad7251  (Adequate.valid adequate Two boolean env5)
  bad7252 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b0 b0)) b0) (bop b0 b0)) b1 → ⊥
  bad7252  p = false≢true (cong lower p)
  cut7252 : Adequate {ℓ} ((op (op (op (var 0) (op (var 1) (var 1))) (var 2)) (op (var 0) (var 3))) , (var 4)) → ⊥
  cut7252  adequate = bad7252  (Adequate.valid adequate Two boolean env9)
  bad7253 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b0 b0)) b1) (bop b0 b0)) b0 → ⊥
  bad7253  p = false≢true (sym (cong lower p))
  cut7253 : Adequate {ℓ} ((op (op (op (var 0) (op (var 1) (var 1))) (var 2)) (op (var 1) (var 0))) , (var 0)) → ⊥
  cut7253  adequate = bad7253  (Adequate.valid adequate Two boolean env1)
  bad7254 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b0 b0)) b1) (bop b0 b0)) b0 → ⊥
  bad7254  p = false≢true (sym (cong lower p))
  cut7254 : Adequate {ℓ} ((op (op (op (var 0) (op (var 1) (var 1))) (var 2)) (op (var 1) (var 0))) , (var 1)) → ⊥
  cut7254  adequate = bad7254  (Adequate.valid adequate Two boolean env1)
  bad7255 : PathP (λ _ → Two) (bop (bop (bop b1 (bop b0 b0)) b1) (bop b0 b1)) b1 → ⊥
  bad7255  p = false≢true (cong lower p)
  cut7255 : Adequate {ℓ} ((op (op (op (var 0) (op (var 1) (var 1))) (var 2)) (op (var 1) (var 0))) , (var 2)) → ⊥
  cut7255  adequate = bad7255  (Adequate.valid adequate Two boolean env6)
  bad7256 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b0 b0)) b0) (bop b0 b0)) b1 → ⊥
  bad7256  p = false≢true (cong lower p)
  cut7256 : Adequate {ℓ} ((op (op (op (var 0) (op (var 1) (var 1))) (var 2)) (op (var 1) (var 0))) , (var 3)) → ⊥
  cut7256  adequate = bad7256  (Adequate.valid adequate Two boolean env5)
  bad7257 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b0 b0)) b1) (bop b0 b0)) b0 → ⊥
  bad7257  p = false≢true (sym (cong lower p))
  cut7257 : Adequate {ℓ} ((op (op (op (var 0) (op (var 1) (var 1))) (var 2)) (op (var 1) (var 1))) , (var 0)) → ⊥
  cut7257  adequate = bad7257  (Adequate.valid adequate Two boolean env1)
  bad7258 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b0 b0)) b1) (bop b0 b0)) b0 → ⊥
  bad7258  p = false≢true (sym (cong lower p))
  cut7258 : Adequate {ℓ} ((op (op (op (var 0) (op (var 1) (var 1))) (var 2)) (op (var 1) (var 1))) , (var 1)) → ⊥
  cut7258  adequate = bad7258  (Adequate.valid adequate Two boolean env1)
  bad7259 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b1 b1)) b0) (bop b1 b1)) b0 → ⊥
  bad7259  p = false≢true (sym (cong lower p))
  cut7259 : Adequate {ℓ} ((op (op (op (var 0) (op (var 1) (var 1))) (var 2)) (op (var 1) (var 1))) , (var 2)) → ⊥
  cut7259  adequate = bad7259  (Adequate.valid adequate Two boolean env4)
  bad7260 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b0 b0)) b0) (bop b0 b0)) b1 → ⊥
  bad7260  p = false≢true (cong lower p)
  cut7260 : Adequate {ℓ} ((op (op (op (var 0) (op (var 1) (var 1))) (var 2)) (op (var 1) (var 1))) , (var 3)) → ⊥
  cut7260  adequate = bad7260  (Adequate.valid adequate Two boolean env5)
  bad7261 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b0 b0)) b1) (bop b0 b1)) b0 → ⊥
  bad7261  p = false≢true (sym (cong lower p))
  cut7261 : Adequate {ℓ} ((op (op (op (var 0) (op (var 1) (var 1))) (var 2)) (op (var 1) (var 2))) , (var 0)) → ⊥
  cut7261  adequate = bad7261  (Adequate.valid adequate Two boolean env1)
  bad7262 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b0 b0)) b1) (bop b0 b1)) b0 → ⊥
  bad7262  p = false≢true (sym (cong lower p))
  cut7262 : Adequate {ℓ} ((op (op (op (var 0) (op (var 1) (var 1))) (var 2)) (op (var 1) (var 2))) , (var 1)) → ⊥
  cut7262  adequate = bad7262  (Adequate.valid adequate Two boolean env1)
  bad7263 : PathP (λ _ → Two) (bop (bop (bop b1 (bop b0 b0)) b1) (bop b0 b1)) b1 → ⊥
  bad7263  p = false≢true (cong lower p)
  cut7263 : Adequate {ℓ} ((op (op (op (var 0) (op (var 1) (var 1))) (var 2)) (op (var 1) (var 2))) , (var 2)) → ⊥
  cut7263  adequate = bad7263  (Adequate.valid adequate Two boolean env6)
  bad7264 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b0 b0)) b0) (bop b0 b0)) b1 → ⊥
  bad7264  p = false≢true (cong lower p)
  cut7264 : Adequate {ℓ} ((op (op (op (var 0) (op (var 1) (var 1))) (var 2)) (op (var 1) (var 2))) , (var 3)) → ⊥
  cut7264  adequate = bad7264  (Adequate.valid adequate Two boolean env5)
  bad7265 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b0 b0)) b1) (bop b0 b0)) b0 → ⊥
  bad7265  p = false≢true (sym (cong lower p))
  cut7265 : Adequate {ℓ} ((op (op (op (var 0) (op (var 1) (var 1))) (var 2)) (op (var 1) (var 3))) , (var 0)) → ⊥
  cut7265  adequate = bad7265  (Adequate.valid adequate Two boolean env8)
  bad7266 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b0 b0)) b1) (bop b0 b0)) b0 → ⊥
  bad7266  p = false≢true (sym (cong lower p))
  cut7266 : Adequate {ℓ} ((op (op (op (var 0) (op (var 1) (var 1))) (var 2)) (op (var 1) (var 3))) , (var 1)) → ⊥
  cut7266  adequate = bad7266  (Adequate.valid adequate Two boolean env8)
  bad7267 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b1 b1)) b0) (bop b1 b1)) b0 → ⊥
  bad7267  p = false≢true (sym (cong lower p))
  cut7267 : Adequate {ℓ} ((op (op (op (var 0) (op (var 1) (var 1))) (var 2)) (op (var 1) (var 3))) , (var 2)) → ⊥
  cut7267  adequate = bad7267  (Adequate.valid adequate Two boolean env13)
  bad7268 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b0 b0)) b0) (bop b0 b1)) b1 → ⊥
  bad7268  p = false≢true (cong lower p)
  cut7268 : Adequate {ℓ} ((op (op (op (var 0) (op (var 1) (var 1))) (var 2)) (op (var 1) (var 3))) , (var 3)) → ⊥
  cut7268  adequate = bad7268  (Adequate.valid adequate Two boolean env5)
  bad7269 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b0 b0)) b0) (bop b0 b0)) b1 → ⊥
  bad7269  p = false≢true (cong lower p)
  cut7269 : Adequate {ℓ} ((op (op (op (var 0) (op (var 1) (var 1))) (var 2)) (op (var 1) (var 3))) , (var 4)) → ⊥
  cut7269  adequate = bad7269  (Adequate.valid adequate Two boolean env9)
  bad7270 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b0 b0)) b1) (bop b1 b0)) b0 → ⊥
  bad7270  p = false≢true (sym (cong lower p))
  cut7270 : Adequate {ℓ} ((op (op (op (var 0) (op (var 1) (var 1))) (var 2)) (op (var 2) (var 0))) , (var 0)) → ⊥
  cut7270  adequate = bad7270  (Adequate.valid adequate Two boolean env1)
  bad7271 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b0 b0)) b1) (bop b1 b0)) b0 → ⊥
  bad7271  p = false≢true (sym (cong lower p))
  cut7271 : Adequate {ℓ} ((op (op (op (var 0) (op (var 1) (var 1))) (var 2)) (op (var 2) (var 0))) , (var 1)) → ⊥
  cut7271  adequate = bad7271  (Adequate.valid adequate Two boolean env1)
  holds7272 : (z0 z1 z2 : A8) → (mul8 (mul8 (mul8 z0 (mul8 z1 z1)) z2) (mul8 z2 z0)) ≡ z2
  holds7272 m8c0 m8c0 m8c0 = refl
  holds7272 m8c0 m8c0 m8c1 = refl
  holds7272 m8c0 m8c0 m8c2 = refl
  holds7272 m8c0 m8c1 m8c0 = refl
  holds7272 m8c0 m8c1 m8c1 = refl
  holds7272 m8c0 m8c1 m8c2 = refl
  holds7272 m8c0 m8c2 m8c0 = refl
  holds7272 m8c0 m8c2 m8c1 = refl
  holds7272 m8c0 m8c2 m8c2 = refl
  holds7272 m8c1 m8c0 m8c0 = refl
  holds7272 m8c1 m8c0 m8c1 = refl
  holds7272 m8c1 m8c0 m8c2 = refl
  holds7272 m8c1 m8c1 m8c0 = refl
  holds7272 m8c1 m8c1 m8c1 = refl
  holds7272 m8c1 m8c1 m8c2 = refl
  holds7272 m8c1 m8c2 m8c0 = refl
  holds7272 m8c1 m8c2 m8c1 = refl
  holds7272 m8c1 m8c2 m8c2 = refl
  holds7272 m8c2 m8c0 m8c0 = refl
  holds7272 m8c2 m8c0 m8c1 = refl
  holds7272 m8c2 m8c0 m8c2 = refl
  holds7272 m8c2 m8c1 m8c0 = refl
  holds7272 m8c2 m8c1 m8c1 = refl
  holds7272 m8c2 m8c1 m8c2 = refl
  holds7272 m8c2 m8c2 m8c0 = refl
  holds7272 m8c2 m8c2 m8c1 = refl
  holds7272 m8c2 m8c2 m8c2 = refl
  cut7272 : Adequate {ℓ} ((op (op (op (var 0) (op (var 1) (var 1))) (var 2)) (op (var 2) (var 0))) , (var 2)) → ⊥
  cut7272  = reject8 ((op (op (op (var 0) (op (var 1) (var 1))) (var 2)) (op (var 2) (var 0))) , (var 2)) (λ env → holds7272 (env 0) (env 1) (env 2))
  bad7273 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b0 b0)) b0) (bop b0 b0)) b1 → ⊥
  bad7273  p = false≢true (cong lower p)
  cut7273 : Adequate {ℓ} ((op (op (op (var 0) (op (var 1) (var 1))) (var 2)) (op (var 2) (var 0))) , (var 3)) → ⊥
  cut7273  adequate = bad7273  (Adequate.valid adequate Two boolean env5)
  bad7274 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b0 b0)) b1) (bop b1 b0)) b0 → ⊥
  bad7274  p = false≢true (sym (cong lower p))
  cut7274 : Adequate {ℓ} ((op (op (op (var 0) (op (var 1) (var 1))) (var 2)) (op (var 2) (var 1))) , (var 0)) → ⊥
  cut7274  adequate = bad7274  (Adequate.valid adequate Two boolean env1)
  bad7275 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b0 b0)) b1) (bop b1 b0)) b0 → ⊥
  bad7275  p = false≢true (sym (cong lower p))
  cut7275 : Adequate {ℓ} ((op (op (op (var 0) (op (var 1) (var 1))) (var 2)) (op (var 2) (var 1))) , (var 1)) → ⊥
  cut7275  adequate = bad7275  (Adequate.valid adequate Two boolean env1)
  bad7276 : PathP (λ _ → Two) (bop (bop (bop b1 (bop b0 b0)) b1) (bop b1 b0)) b1 → ⊥
  bad7276  p = false≢true (cong lower p)
  cut7276 : Adequate {ℓ} ((op (op (op (var 0) (op (var 1) (var 1))) (var 2)) (op (var 2) (var 1))) , (var 2)) → ⊥
  cut7276  adequate = bad7276  (Adequate.valid adequate Two boolean env6)
  bad7277 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b0 b0)) b0) (bop b0 b0)) b1 → ⊥
  bad7277  p = false≢true (cong lower p)
  cut7277 : Adequate {ℓ} ((op (op (op (var 0) (op (var 1) (var 1))) (var 2)) (op (var 2) (var 1))) , (var 3)) → ⊥
  cut7277  adequate = bad7277  (Adequate.valid adequate Two boolean env5)
  bad7278 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b0 b0)) b1) (bop b1 b1)) b0 → ⊥
  bad7278  p = false≢true (sym (cong lower p))
  cut7278 : Adequate {ℓ} ((op (op (op (var 0) (op (var 1) (var 1))) (var 2)) (op (var 2) (var 2))) , (var 0)) → ⊥
  cut7278  adequate = bad7278  (Adequate.valid adequate Two boolean env1)
  bad7279 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b0 b0)) b1) (bop b1 b1)) b0 → ⊥
  bad7279  p = false≢true (sym (cong lower p))
  cut7279 : Adequate {ℓ} ((op (op (op (var 0) (op (var 1) (var 1))) (var 2)) (op (var 2) (var 2))) , (var 1)) → ⊥
  cut7279  adequate = bad7279  (Adequate.valid adequate Two boolean env1)
  holds7280 : (z0 z1 z2 : A3) → (mul3 (mul3 (mul3 z0 (mul3 z1 z1)) z2) (mul3 z2 z2)) ≡ z2
  holds7280 z0 z1 z2 = refl
  cut7280 : Adequate {ℓ} ((op (op (op (var 0) (op (var 1) (var 1))) (var 2)) (op (var 2) (var 2))) , (var 2)) → ⊥
  cut7280  = reject3 ((op (op (op (var 0) (op (var 1) (var 1))) (var 2)) (op (var 2) (var 2))) , (var 2)) (λ env → holds7280 (env 0) (env 1) (env 2))
  bad7281 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b0 b0)) b0) (bop b0 b0)) b1 → ⊥
  bad7281  p = false≢true (cong lower p)
  cut7281 : Adequate {ℓ} ((op (op (op (var 0) (op (var 1) (var 1))) (var 2)) (op (var 2) (var 2))) , (var 3)) → ⊥
  cut7281  adequate = bad7281  (Adequate.valid adequate Two boolean env5)
  bad7282 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b0 b0)) b1) (bop b1 b0)) b0 → ⊥
  bad7282  p = false≢true (sym (cong lower p))
  cut7282 : Adequate {ℓ} ((op (op (op (var 0) (op (var 1) (var 1))) (var 2)) (op (var 2) (var 3))) , (var 0)) → ⊥
  cut7282  adequate = bad7282  (Adequate.valid adequate Two boolean env8)
  bad7283 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b0 b0)) b1) (bop b1 b0)) b0 → ⊥
  bad7283  p = false≢true (sym (cong lower p))
  cut7283 : Adequate {ℓ} ((op (op (op (var 0) (op (var 1) (var 1))) (var 2)) (op (var 2) (var 3))) , (var 1)) → ⊥
  cut7283  adequate = bad7283  (Adequate.valid adequate Two boolean env8)
  bad7284 : PathP (λ _ → Two) (bop (bop (bop b1 (bop b0 b0)) b1) (bop b1 b0)) b1 → ⊥
  bad7284  p = false≢true (cong lower p)
  cut7284 : Adequate {ℓ} ((op (op (op (var 0) (op (var 1) (var 1))) (var 2)) (op (var 2) (var 3))) , (var 2)) → ⊥
  cut7284  adequate = bad7284  (Adequate.valid adequate Two boolean env14)
  bad7285 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b0 b0)) b0) (bop b0 b1)) b1 → ⊥
  bad7285  p = false≢true (cong lower p)
  cut7285 : Adequate {ℓ} ((op (op (op (var 0) (op (var 1) (var 1))) (var 2)) (op (var 2) (var 3))) , (var 3)) → ⊥
  cut7285  adequate = bad7285  (Adequate.valid adequate Two boolean env5)
  bad7286 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b0 b0)) b0) (bop b0 b0)) b1 → ⊥
  bad7286  p = false≢true (cong lower p)
  cut7286 : Adequate {ℓ} ((op (op (op (var 0) (op (var 1) (var 1))) (var 2)) (op (var 2) (var 3))) , (var 4)) → ⊥
  cut7286  adequate = bad7286  (Adequate.valid adequate Two boolean env9)
  bad7287 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b0 b0)) b1) (bop b0 b0)) b0 → ⊥
  bad7287  p = false≢true (sym (cong lower p))
  cut7287 : Adequate {ℓ} ((op (op (op (var 0) (op (var 1) (var 1))) (var 2)) (op (var 3) (var 0))) , (var 0)) → ⊥
  cut7287  adequate = bad7287  (Adequate.valid adequate Two boolean env8)
  bad7288 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b0 b0)) b1) (bop b0 b0)) b0 → ⊥
  bad7288  p = false≢true (sym (cong lower p))
  cut7288 : Adequate {ℓ} ((op (op (op (var 0) (op (var 1) (var 1))) (var 2)) (op (var 3) (var 0))) , (var 1)) → ⊥
  cut7288  adequate = bad7288  (Adequate.valid adequate Two boolean env8)
  bad7289 : PathP (λ _ → Two) (bop (bop (bop b1 (bop b0 b0)) b0) (bop b1 b1)) b0 → ⊥
  bad7289  p = false≢true (sym (cong lower p))
  cut7289 : Adequate {ℓ} ((op (op (op (var 0) (op (var 1) (var 1))) (var 2)) (op (var 3) (var 0))) , (var 2)) → ⊥
  cut7289  adequate = bad7289  (Adequate.valid adequate Two boolean env12)
  bad7290 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b0 b0)) b0) (bop b1 b0)) b1 → ⊥
  bad7290  p = false≢true (cong lower p)
  cut7290 : Adequate {ℓ} ((op (op (op (var 0) (op (var 1) (var 1))) (var 2)) (op (var 3) (var 0))) , (var 3)) → ⊥
  cut7290  adequate = bad7290  (Adequate.valid adequate Two boolean env5)
  bad7291 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b0 b0)) b0) (bop b0 b0)) b1 → ⊥
  bad7291  p = false≢true (cong lower p)
  cut7291 : Adequate {ℓ} ((op (op (op (var 0) (op (var 1) (var 1))) (var 2)) (op (var 3) (var 0))) , (var 4)) → ⊥
  cut7291  adequate = bad7291  (Adequate.valid adequate Two boolean env9)
  bad7292 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b0 b0)) b1) (bop b0 b0)) b0 → ⊥
  bad7292  p = false≢true (sym (cong lower p))
  cut7292 : Adequate {ℓ} ((op (op (op (var 0) (op (var 1) (var 1))) (var 2)) (op (var 3) (var 1))) , (var 0)) → ⊥
  cut7292  adequate = bad7292  (Adequate.valid adequate Two boolean env8)
  bad7293 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b0 b0)) b1) (bop b0 b0)) b0 → ⊥
  bad7293  p = false≢true (sym (cong lower p))
  cut7293 : Adequate {ℓ} ((op (op (op (var 0) (op (var 1) (var 1))) (var 2)) (op (var 3) (var 1))) , (var 1)) → ⊥
  cut7293  adequate = bad7293  (Adequate.valid adequate Two boolean env8)
  bad7294 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b1 b1)) b0) (bop b1 b1)) b0 → ⊥
  bad7294  p = false≢true (sym (cong lower p))
  cut7294 : Adequate {ℓ} ((op (op (op (var 0) (op (var 1) (var 1))) (var 2)) (op (var 3) (var 1))) , (var 2)) → ⊥
  cut7294  adequate = bad7294  (Adequate.valid adequate Two boolean env13)
  bad7295 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b0 b0)) b0) (bop b1 b0)) b1 → ⊥
  bad7295  p = false≢true (cong lower p)
  cut7295 : Adequate {ℓ} ((op (op (op (var 0) (op (var 1) (var 1))) (var 2)) (op (var 3) (var 1))) , (var 3)) → ⊥
  cut7295  adequate = bad7295  (Adequate.valid adequate Two boolean env5)
  bad7296 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b0 b0)) b0) (bop b0 b0)) b1 → ⊥
  bad7296  p = false≢true (cong lower p)
  cut7296 : Adequate {ℓ} ((op (op (op (var 0) (op (var 1) (var 1))) (var 2)) (op (var 3) (var 1))) , (var 4)) → ⊥
  cut7296  adequate = bad7296  (Adequate.valid adequate Two boolean env9)
  bad7297 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b0 b0)) b1) (bop b0 b1)) b0 → ⊥
  bad7297  p = false≢true (sym (cong lower p))
  cut7297 : Adequate {ℓ} ((op (op (op (var 0) (op (var 1) (var 1))) (var 2)) (op (var 3) (var 2))) , (var 0)) → ⊥
  cut7297  adequate = bad7297  (Adequate.valid adequate Two boolean env8)
  bad7298 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b0 b0)) b1) (bop b0 b1)) b0 → ⊥
  bad7298  p = false≢true (sym (cong lower p))
  cut7298 : Adequate {ℓ} ((op (op (op (var 0) (op (var 1) (var 1))) (var 2)) (op (var 3) (var 2))) , (var 1)) → ⊥
  cut7298  adequate = bad7298  (Adequate.valid adequate Two boolean env8)
  bad7299 : PathP (λ _ → Two) (bop (bop (bop b1 (bop b0 b0)) b1) (bop b0 b1)) b1 → ⊥
  bad7299  p = false≢true (cong lower p)
  cut7299 : Adequate {ℓ} ((op (op (op (var 0) (op (var 1) (var 1))) (var 2)) (op (var 3) (var 2))) , (var 2)) → ⊥
  cut7299  adequate = bad7299  (Adequate.valid adequate Two boolean env14)
  bad7300 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b0 b0)) b0) (bop b1 b0)) b1 → ⊥
  bad7300  p = false≢true (cong lower p)
  cut7300 : Adequate {ℓ} ((op (op (op (var 0) (op (var 1) (var 1))) (var 2)) (op (var 3) (var 2))) , (var 3)) → ⊥
  cut7300  adequate = bad7300  (Adequate.valid adequate Two boolean env5)
  bad7301 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b0 b0)) b0) (bop b0 b0)) b1 → ⊥
  bad7301  p = false≢true (cong lower p)
  cut7301 : Adequate {ℓ} ((op (op (op (var 0) (op (var 1) (var 1))) (var 2)) (op (var 3) (var 2))) , (var 4)) → ⊥
  cut7301  adequate = bad7301  (Adequate.valid adequate Two boolean env9)
  bad7302 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b0 b0)) b0) (bop b1 b1)) b0 → ⊥
  bad7302  p = false≢true (sym (cong lower p))
  cut7302 : Adequate {ℓ} ((op (op (op (var 0) (op (var 1) (var 1))) (var 2)) (op (var 3) (var 3))) , (var 0)) → ⊥
  cut7302  adequate = bad7302  (Adequate.valid adequate Two boolean env5)
  bad7303 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b0 b0)) b0) (bop b1 b1)) b0 → ⊥
  bad7303  p = false≢true (sym (cong lower p))
  cut7303 : Adequate {ℓ} ((op (op (op (var 0) (op (var 1) (var 1))) (var 2)) (op (var 3) (var 3))) , (var 1)) → ⊥
  cut7303  adequate = bad7303  (Adequate.valid adequate Two boolean env5)
  bad7304 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b0 b0)) b0) (bop b1 b1)) b0 → ⊥
  bad7304  p = false≢true (sym (cong lower p))
  cut7304 : Adequate {ℓ} ((op (op (op (var 0) (op (var 1) (var 1))) (var 2)) (op (var 3) (var 3))) , (var 2)) → ⊥
  cut7304  adequate = bad7304  (Adequate.valid adequate Two boolean env5)
  bad7305 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b0 b0)) b1) (bop b0 b0)) b0 → ⊥
  bad7305  p = false≢true (sym (cong lower p))
  cut7305 : Adequate {ℓ} ((op (op (op (var 0) (op (var 1) (var 1))) (var 2)) (op (var 3) (var 3))) , (var 3)) → ⊥
  cut7305  adequate = bad7305  (Adequate.valid adequate Two boolean env8)
  bad7306 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b0 b0)) b0) (bop b0 b0)) b1 → ⊥
  bad7306  p = false≢true (cong lower p)
  cut7306 : Adequate {ℓ} ((op (op (op (var 0) (op (var 1) (var 1))) (var 2)) (op (var 3) (var 3))) , (var 4)) → ⊥
  cut7306  adequate = bad7306  (Adequate.valid adequate Two boolean env9)
  bad7307 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b0 b0)) b0) (bop b1 b1)) b0 → ⊥
  bad7307  p = false≢true (sym (cong lower p))
  cut7307 : Adequate {ℓ} ((op (op (op (var 0) (op (var 1) (var 1))) (var 2)) (op (var 3) (var 4))) , (var 0)) → ⊥
  cut7307  adequate = bad7307  (Adequate.valid adequate Two boolean env15)
  bad7308 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b0 b0)) b0) (bop b1 b1)) b0 → ⊥
  bad7308  p = false≢true (sym (cong lower p))
  cut7308 : Adequate {ℓ} ((op (op (op (var 0) (op (var 1) (var 1))) (var 2)) (op (var 3) (var 4))) , (var 1)) → ⊥
  cut7308  adequate = bad7308  (Adequate.valid adequate Two boolean env15)
  bad7309 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b0 b0)) b0) (bop b1 b1)) b0 → ⊥
  bad7309  p = false≢true (sym (cong lower p))
  cut7309 : Adequate {ℓ} ((op (op (op (var 0) (op (var 1) (var 1))) (var 2)) (op (var 3) (var 4))) , (var 2)) → ⊥
  cut7309  adequate = bad7309  (Adequate.valid adequate Two boolean env15)
  bad7310 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b0 b0)) b0) (bop b1 b0)) b1 → ⊥
  bad7310  p = false≢true (cong lower p)
  cut7310 : Adequate {ℓ} ((op (op (op (var 0) (op (var 1) (var 1))) (var 2)) (op (var 3) (var 4))) , (var 3)) → ⊥
  cut7310  adequate = bad7310  (Adequate.valid adequate Two boolean env16)
  bad7311 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b0 b0)) b0) (bop b0 b1)) b1 → ⊥
  bad7311  p = false≢true (cong lower p)
  cut7311 : Adequate {ℓ} ((op (op (op (var 0) (op (var 1) (var 1))) (var 2)) (op (var 3) (var 4))) , (var 4)) → ⊥
  cut7311  adequate = bad7311  (Adequate.valid adequate Two boolean env9)
  bad7312 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b0 b0)) b0) (bop b0 b0)) b1 → ⊥
  bad7312  p = false≢true (cong lower p)
  cut7312 : Adequate {ℓ} ((op (op (op (var 0) (op (var 1) (var 1))) (var 2)) (op (var 3) (var 4))) , (var 5)) → ⊥
  cut7312  adequate = bad7312  (Adequate.valid adequate Two boolean env17)
  holds7313 : (z0 z1 z2 : A2) → (mul2 (mul2 (mul2 z0 (mul2 z1 z2)) z0) (mul2 z0 z0)) ≡ z0
  holds7313 z0 z1 z2 = refl
  cut7313 : Adequate {ℓ} ((op (op (op (var 0) (op (var 1) (var 2))) (var 0)) (op (var 0) (var 0))) , (var 0)) → ⊥
  cut7313  = reject2 ((op (op (op (var 0) (op (var 1) (var 2))) (var 0)) (op (var 0) (var 0))) , (var 0)) (λ env → holds7313 (env 0) (env 1) (env 2))
  bad7314 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b1 b0)) b0) (bop b0 b0)) b1 → ⊥
  bad7314  p = false≢true (cong lower p)
  cut7314 : Adequate {ℓ} ((op (op (op (var 0) (op (var 1) (var 2))) (var 0)) (op (var 0) (var 0))) , (var 1)) → ⊥
  cut7314  adequate = bad7314  (Adequate.valid adequate Two boolean env4)
  bad7315 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b0 b1)) b0) (bop b0 b0)) b1 → ⊥
  bad7315  p = false≢true (cong lower p)
  cut7315 : Adequate {ℓ} ((op (op (op (var 0) (op (var 1) (var 2))) (var 0)) (op (var 0) (var 0))) , (var 2)) → ⊥
  cut7315  adequate = bad7315  (Adequate.valid adequate Two boolean env1)
  bad7316 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b0 b0)) b0) (bop b0 b0)) b1 → ⊥
  bad7316  p = false≢true (cong lower p)
  cut7316 : Adequate {ℓ} ((op (op (op (var 0) (op (var 1) (var 2))) (var 0)) (op (var 0) (var 0))) , (var 3)) → ⊥
  cut7316  adequate = bad7316  (Adequate.valid adequate Two boolean env5)
  bad7317 : PathP (λ _ → Two) (bop (bop (bop b1 (bop b0 b0)) b1) (bop b1 b0)) b1 → ⊥
  bad7317  p = false≢true (cong lower p)
  cut7317 : Adequate {ℓ} ((op (op (op (var 0) (op (var 1) (var 2))) (var 0)) (op (var 0) (var 1))) , (var 0)) → ⊥
  cut7317  adequate = bad7317  (Adequate.valid adequate Two boolean env10)
  bad7318 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b1 b0)) b0) (bop b0 b1)) b1 → ⊥
  bad7318  p = false≢true (cong lower p)
  cut7318 : Adequate {ℓ} ((op (op (op (var 0) (op (var 1) (var 2))) (var 0)) (op (var 0) (var 1))) , (var 1)) → ⊥
  cut7318  adequate = bad7318  (Adequate.valid adequate Two boolean env4)
  bad7319 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b0 b1)) b0) (bop b0 b0)) b1 → ⊥
  bad7319  p = false≢true (cong lower p)
  cut7319 : Adequate {ℓ} ((op (op (op (var 0) (op (var 1) (var 2))) (var 0)) (op (var 0) (var 1))) , (var 2)) → ⊥
  cut7319  adequate = bad7319  (Adequate.valid adequate Two boolean env1)
  bad7320 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b0 b0)) b0) (bop b0 b0)) b1 → ⊥
  bad7320  p = false≢true (cong lower p)
  cut7320 : Adequate {ℓ} ((op (op (op (var 0) (op (var 1) (var 2))) (var 0)) (op (var 0) (var 1))) , (var 3)) → ⊥
  cut7320  adequate = bad7320  (Adequate.valid adequate Two boolean env5)
  bad7321 : PathP (λ _ → Two) (bop (bop (bop b1 (bop b0 b0)) b1) (bop b1 b0)) b1 → ⊥
  bad7321  p = false≢true (cong lower p)
  cut7321 : Adequate {ℓ} ((op (op (op (var 0) (op (var 1) (var 2))) (var 0)) (op (var 0) (var 2))) , (var 0)) → ⊥
  cut7321  adequate = bad7321  (Adequate.valid adequate Two boolean env10)
  bad7322 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b1 b0)) b0) (bop b0 b0)) b1 → ⊥
  bad7322  p = false≢true (cong lower p)
  cut7322 : Adequate {ℓ} ((op (op (op (var 0) (op (var 1) (var 2))) (var 0)) (op (var 0) (var 2))) , (var 1)) → ⊥
  cut7322  adequate = bad7322  (Adequate.valid adequate Two boolean env4)
  bad7323 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b0 b1)) b0) (bop b0 b1)) b1 → ⊥
  bad7323  p = false≢true (cong lower p)
  cut7323 : Adequate {ℓ} ((op (op (op (var 0) (op (var 1) (var 2))) (var 0)) (op (var 0) (var 2))) , (var 2)) → ⊥
  cut7323  adequate = bad7323  (Adequate.valid adequate Two boolean env1)
  bad7324 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b0 b0)) b0) (bop b0 b0)) b1 → ⊥
  bad7324  p = false≢true (cong lower p)
  cut7324 : Adequate {ℓ} ((op (op (op (var 0) (op (var 1) (var 2))) (var 0)) (op (var 0) (var 2))) , (var 3)) → ⊥
  cut7324  adequate = bad7324  (Adequate.valid adequate Two boolean env5)
  env18 : ℕ → Two
  env18 zero = b1
  env18 (suc zero) = b0
  env18 (suc (suc zero)) = b0
  env18 (suc (suc (suc zero))) = b0
  env18 (suc (suc (suc (suc rest)))) = b0
  bad7325 : PathP (λ _ → Two) (bop (bop (bop b1 (bop b0 b0)) b1) (bop b1 b0)) b1 → ⊥
  bad7325  p = false≢true (cong lower p)
  cut7325 : Adequate {ℓ} ((op (op (op (var 0) (op (var 1) (var 2))) (var 0)) (op (var 0) (var 3))) , (var 0)) → ⊥
  cut7325  adequate = bad7325  (Adequate.valid adequate Two boolean env18)
  env19 : ℕ → Two
  env19 zero = b0
  env19 (suc zero) = b1
  env19 (suc (suc zero)) = b0
  env19 (suc (suc (suc zero))) = b0
  env19 (suc (suc (suc (suc rest)))) = b0
  bad7326 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b1 b0)) b0) (bop b0 b0)) b1 → ⊥
  bad7326  p = false≢true (cong lower p)
  cut7326 : Adequate {ℓ} ((op (op (op (var 0) (op (var 1) (var 2))) (var 0)) (op (var 0) (var 3))) , (var 1)) → ⊥
  cut7326  adequate = bad7326  (Adequate.valid adequate Two boolean env19)
  bad7327 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b0 b1)) b0) (bop b0 b0)) b1 → ⊥
  bad7327  p = false≢true (cong lower p)
  cut7327 : Adequate {ℓ} ((op (op (op (var 0) (op (var 1) (var 2))) (var 0)) (op (var 0) (var 3))) , (var 2)) → ⊥
  cut7327  adequate = bad7327  (Adequate.valid adequate Two boolean env8)
  bad7328 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b0 b0)) b0) (bop b0 b1)) b1 → ⊥
  bad7328  p = false≢true (cong lower p)
  cut7328 : Adequate {ℓ} ((op (op (op (var 0) (op (var 1) (var 2))) (var 0)) (op (var 0) (var 3))) , (var 3)) → ⊥
  cut7328  adequate = bad7328  (Adequate.valid adequate Two boolean env5)
  bad7329 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b0 b0)) b0) (bop b0 b0)) b1 → ⊥
  bad7329  p = false≢true (cong lower p)
  cut7329 : Adequate {ℓ} ((op (op (op (var 0) (op (var 1) (var 2))) (var 0)) (op (var 0) (var 3))) , (var 4)) → ⊥
  cut7329  adequate = bad7329  (Adequate.valid adequate Two boolean env9)
  bad7330 : PathP (λ _ → Two) (bop (bop (bop b1 (bop b0 b0)) b1) (bop b0 b1)) b1 → ⊥
  bad7330  p = false≢true (cong lower p)
  cut7330 : Adequate {ℓ} ((op (op (op (var 0) (op (var 1) (var 2))) (var 0)) (op (var 1) (var 0))) , (var 0)) → ⊥
  cut7330  adequate = bad7330  (Adequate.valid adequate Two boolean env10)
  bad7331 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b1 b0)) b0) (bop b1 b0)) b1 → ⊥
  bad7331  p = false≢true (cong lower p)
  cut7331 : Adequate {ℓ} ((op (op (op (var 0) (op (var 1) (var 2))) (var 0)) (op (var 1) (var 0))) , (var 1)) → ⊥
  cut7331  adequate = bad7331  (Adequate.valid adequate Two boolean env4)
  bad7332 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b0 b1)) b0) (bop b0 b0)) b1 → ⊥
  bad7332  p = false≢true (cong lower p)
  cut7332 : Adequate {ℓ} ((op (op (op (var 0) (op (var 1) (var 2))) (var 0)) (op (var 1) (var 0))) , (var 2)) → ⊥
  cut7332  adequate = bad7332  (Adequate.valid adequate Two boolean env1)
  bad7333 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b0 b0)) b0) (bop b0 b0)) b1 → ⊥
  bad7333  p = false≢true (cong lower p)
  cut7333 : Adequate {ℓ} ((op (op (op (var 0) (op (var 1) (var 2))) (var 0)) (op (var 1) (var 0))) , (var 3)) → ⊥
  cut7333  adequate = bad7333  (Adequate.valid adequate Two boolean env5)
  bad7334 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b1 b0)) b0) (bop b1 b1)) b0 → ⊥
  bad7334  p = false≢true (sym (cong lower p))
  cut7334 : Adequate {ℓ} ((op (op (op (var 0) (op (var 1) (var 2))) (var 0)) (op (var 1) (var 1))) , (var 0)) → ⊥
  cut7334  adequate = bad7334  (Adequate.valid adequate Two boolean env4)
  holds7335 : (z0 z1 z2 : A3) → (mul3 (mul3 (mul3 z0 (mul3 z1 z2)) z0) (mul3 z1 z1)) ≡ z1
  holds7335 z0 z1 z2 = refl
  cut7335 : Adequate {ℓ} ((op (op (op (var 0) (op (var 1) (var 2))) (var 0)) (op (var 1) (var 1))) , (var 1)) → ⊥
  cut7335  = reject3 ((op (op (op (var 0) (op (var 1) (var 2))) (var 0)) (op (var 1) (var 1))) , (var 1)) (λ env → holds7335 (env 0) (env 1) (env 2))
  bad7336 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b0 b1)) b0) (bop b0 b0)) b1 → ⊥
  bad7336  p = false≢true (cong lower p)
  cut7336 : Adequate {ℓ} ((op (op (op (var 0) (op (var 1) (var 2))) (var 0)) (op (var 1) (var 1))) , (var 2)) → ⊥
  cut7336  adequate = bad7336  (Adequate.valid adequate Two boolean env1)
  bad7337 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b0 b0)) b0) (bop b0 b0)) b1 → ⊥
  bad7337  p = false≢true (cong lower p)
  cut7337 : Adequate {ℓ} ((op (op (op (var 0) (op (var 1) (var 2))) (var 0)) (op (var 1) (var 1))) , (var 3)) → ⊥
  cut7337  adequate = bad7337  (Adequate.valid adequate Two boolean env5)
  bad7338 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b1 b1)) b0) (bop b1 b1)) b0 → ⊥
  bad7338  p = false≢true (sym (cong lower p))
  cut7338 : Adequate {ℓ} ((op (op (op (var 0) (op (var 1) (var 2))) (var 0)) (op (var 1) (var 2))) , (var 0)) → ⊥
  cut7338  adequate = bad7338  (Adequate.valid adequate Two boolean env3)
  bad7339 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b1 b0)) b0) (bop b1 b0)) b1 → ⊥
  bad7339  p = false≢true (cong lower p)
  cut7339 : Adequate {ℓ} ((op (op (op (var 0) (op (var 1) (var 2))) (var 0)) (op (var 1) (var 2))) , (var 1)) → ⊥
  cut7339  adequate = bad7339  (Adequate.valid adequate Two boolean env4)
  bad7340 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b0 b1)) b0) (bop b0 b1)) b1 → ⊥
  bad7340  p = false≢true (cong lower p)
  cut7340 : Adequate {ℓ} ((op (op (op (var 0) (op (var 1) (var 2))) (var 0)) (op (var 1) (var 2))) , (var 2)) → ⊥
  cut7340  adequate = bad7340  (Adequate.valid adequate Two boolean env1)
  bad7341 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b0 b0)) b0) (bop b0 b0)) b1 → ⊥
  bad7341  p = false≢true (cong lower p)
  cut7341 : Adequate {ℓ} ((op (op (op (var 0) (op (var 1) (var 2))) (var 0)) (op (var 1) (var 2))) , (var 3)) → ⊥
  cut7341  adequate = bad7341  (Adequate.valid adequate Two boolean env5)
  bad7342 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b1 b0)) b0) (bop b1 b1)) b0 → ⊥
  bad7342  p = false≢true (sym (cong lower p))
  cut7342 : Adequate {ℓ} ((op (op (op (var 0) (op (var 1) (var 2))) (var 0)) (op (var 1) (var 3))) , (var 0)) → ⊥
  cut7342  adequate = bad7342  (Adequate.valid adequate Two boolean env13)
  bad7343 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b1 b0)) b0) (bop b1 b0)) b1 → ⊥
  bad7343  p = false≢true (cong lower p)
  cut7343 : Adequate {ℓ} ((op (op (op (var 0) (op (var 1) (var 2))) (var 0)) (op (var 1) (var 3))) , (var 1)) → ⊥
  cut7343  adequate = bad7343  (Adequate.valid adequate Two boolean env19)
  bad7344 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b0 b1)) b0) (bop b0 b0)) b1 → ⊥
  bad7344  p = false≢true (cong lower p)
  cut7344 : Adequate {ℓ} ((op (op (op (var 0) (op (var 1) (var 2))) (var 0)) (op (var 1) (var 3))) , (var 2)) → ⊥
  cut7344  adequate = bad7344  (Adequate.valid adequate Two boolean env8)
  bad7345 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b0 b0)) b0) (bop b0 b1)) b1 → ⊥
  bad7345  p = false≢true (cong lower p)
  cut7345 : Adequate {ℓ} ((op (op (op (var 0) (op (var 1) (var 2))) (var 0)) (op (var 1) (var 3))) , (var 3)) → ⊥
  cut7345  adequate = bad7345  (Adequate.valid adequate Two boolean env5)
  bad7346 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b0 b0)) b0) (bop b0 b0)) b1 → ⊥
  bad7346  p = false≢true (cong lower p)
  cut7346 : Adequate {ℓ} ((op (op (op (var 0) (op (var 1) (var 2))) (var 0)) (op (var 1) (var 3))) , (var 4)) → ⊥
  cut7346  adequate = bad7346  (Adequate.valid adequate Two boolean env9)
  bad7347 : PathP (λ _ → Two) (bop (bop (bop b1 (bop b0 b0)) b1) (bop b0 b1)) b1 → ⊥
  bad7347  p = false≢true (cong lower p)
  cut7347 : Adequate {ℓ} ((op (op (op (var 0) (op (var 1) (var 2))) (var 0)) (op (var 2) (var 0))) , (var 0)) → ⊥
  cut7347  adequate = bad7347  (Adequate.valid adequate Two boolean env10)
  bad7348 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b1 b0)) b0) (bop b0 b0)) b1 → ⊥
  bad7348  p = false≢true (cong lower p)
  cut7348 : Adequate {ℓ} ((op (op (op (var 0) (op (var 1) (var 2))) (var 0)) (op (var 2) (var 0))) , (var 1)) → ⊥
  cut7348  adequate = bad7348  (Adequate.valid adequate Two boolean env4)
  bad7349 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b0 b1)) b0) (bop b1 b0)) b1 → ⊥
  bad7349  p = false≢true (cong lower p)
  cut7349 : Adequate {ℓ} ((op (op (op (var 0) (op (var 1) (var 2))) (var 0)) (op (var 2) (var 0))) , (var 2)) → ⊥
  cut7349  adequate = bad7349  (Adequate.valid adequate Two boolean env1)
  bad7350 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b0 b0)) b0) (bop b0 b0)) b1 → ⊥
  bad7350  p = false≢true (cong lower p)
  cut7350 : Adequate {ℓ} ((op (op (op (var 0) (op (var 1) (var 2))) (var 0)) (op (var 2) (var 0))) , (var 3)) → ⊥
  cut7350  adequate = bad7350  (Adequate.valid adequate Two boolean env5)
  bad7351 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b1 b1)) b0) (bop b1 b1)) b0 → ⊥
  bad7351  p = false≢true (sym (cong lower p))
  cut7351 : Adequate {ℓ} ((op (op (op (var 0) (op (var 1) (var 2))) (var 0)) (op (var 2) (var 1))) , (var 0)) → ⊥
  cut7351  adequate = bad7351  (Adequate.valid adequate Two boolean env3)
  bad7352 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b1 b0)) b0) (bop b0 b1)) b1 → ⊥
  bad7352  p = false≢true (cong lower p)
  cut7352 : Adequate {ℓ} ((op (op (op (var 0) (op (var 1) (var 2))) (var 0)) (op (var 2) (var 1))) , (var 1)) → ⊥
  cut7352  adequate = bad7352  (Adequate.valid adequate Two boolean env4)
  bad7353 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b0 b1)) b0) (bop b1 b0)) b1 → ⊥
  bad7353  p = false≢true (cong lower p)
  cut7353 : Adequate {ℓ} ((op (op (op (var 0) (op (var 1) (var 2))) (var 0)) (op (var 2) (var 1))) , (var 2)) → ⊥
  cut7353  adequate = bad7353  (Adequate.valid adequate Two boolean env1)
  bad7354 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b0 b0)) b0) (bop b0 b0)) b1 → ⊥
  bad7354  p = false≢true (cong lower p)
  cut7354 : Adequate {ℓ} ((op (op (op (var 0) (op (var 1) (var 2))) (var 0)) (op (var 2) (var 1))) , (var 3)) → ⊥
  cut7354  adequate = bad7354  (Adequate.valid adequate Two boolean env5)
  bad7355 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b0 b1)) b0) (bop b1 b1)) b0 → ⊥
  bad7355  p = false≢true (sym (cong lower p))
  cut7355 : Adequate {ℓ} ((op (op (op (var 0) (op (var 1) (var 2))) (var 0)) (op (var 2) (var 2))) , (var 0)) → ⊥
  cut7355  adequate = bad7355  (Adequate.valid adequate Two boolean env1)
  bad7356 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b0 b1)) b0) (bop b1 b1)) b0 → ⊥
  bad7356  p = false≢true (sym (cong lower p))
  cut7356 : Adequate {ℓ} ((op (op (op (var 0) (op (var 1) (var 2))) (var 0)) (op (var 2) (var 2))) , (var 1)) → ⊥
  cut7356  adequate = bad7356  (Adequate.valid adequate Two boolean env1)
  holds7357 : (z0 z1 z2 : A3) → (mul3 (mul3 (mul3 z0 (mul3 z1 z2)) z0) (mul3 z2 z2)) ≡ z2
  holds7357 z0 z1 z2 = refl
  cut7357 : Adequate {ℓ} ((op (op (op (var 0) (op (var 1) (var 2))) (var 0)) (op (var 2) (var 2))) , (var 2)) → ⊥
  cut7357  = reject3 ((op (op (op (var 0) (op (var 1) (var 2))) (var 0)) (op (var 2) (var 2))) , (var 2)) (λ env → holds7357 (env 0) (env 1) (env 2))
  bad7358 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b0 b0)) b0) (bop b0 b0)) b1 → ⊥
  bad7358  p = false≢true (cong lower p)
  cut7358 : Adequate {ℓ} ((op (op (op (var 0) (op (var 1) (var 2))) (var 0)) (op (var 2) (var 2))) , (var 3)) → ⊥
  cut7358  adequate = bad7358  (Adequate.valid adequate Two boolean env5)
  bad7359 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b0 b1)) b0) (bop b1 b1)) b0 → ⊥
  bad7359  p = false≢true (sym (cong lower p))
  cut7359 : Adequate {ℓ} ((op (op (op (var 0) (op (var 1) (var 2))) (var 0)) (op (var 2) (var 3))) , (var 0)) → ⊥
  cut7359  adequate = bad7359  (Adequate.valid adequate Two boolean env7)
  bad7360 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b0 b1)) b0) (bop b1 b1)) b0 → ⊥
  bad7360  p = false≢true (sym (cong lower p))
  cut7360 : Adequate {ℓ} ((op (op (op (var 0) (op (var 1) (var 2))) (var 0)) (op (var 2) (var 3))) , (var 1)) → ⊥
  cut7360  adequate = bad7360  (Adequate.valid adequate Two boolean env7)
  bad7361 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b0 b1)) b0) (bop b1 b0)) b1 → ⊥
  bad7361  p = false≢true (cong lower p)
  cut7361 : Adequate {ℓ} ((op (op (op (var 0) (op (var 1) (var 2))) (var 0)) (op (var 2) (var 3))) , (var 2)) → ⊥
  cut7361  adequate = bad7361  (Adequate.valid adequate Two boolean env8)
  bad7362 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b0 b0)) b0) (bop b0 b1)) b1 → ⊥
  bad7362  p = false≢true (cong lower p)
  cut7362 : Adequate {ℓ} ((op (op (op (var 0) (op (var 1) (var 2))) (var 0)) (op (var 2) (var 3))) , (var 3)) → ⊥
  cut7362  adequate = bad7362  (Adequate.valid adequate Two boolean env5)
  bad7363 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b0 b0)) b0) (bop b0 b0)) b1 → ⊥
  bad7363  p = false≢true (cong lower p)
  cut7363 : Adequate {ℓ} ((op (op (op (var 0) (op (var 1) (var 2))) (var 0)) (op (var 2) (var 3))) , (var 4)) → ⊥
  cut7363  adequate = bad7363  (Adequate.valid adequate Two boolean env9)
  bad7364 : PathP (λ _ → Two) (bop (bop (bop b1 (bop b0 b0)) b1) (bop b0 b1)) b1 → ⊥
  bad7364  p = false≢true (cong lower p)
  cut7364 : Adequate {ℓ} ((op (op (op (var 0) (op (var 1) (var 2))) (var 0)) (op (var 3) (var 0))) , (var 0)) → ⊥
  cut7364  adequate = bad7364  (Adequate.valid adequate Two boolean env18)
  bad7365 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b1 b0)) b0) (bop b0 b0)) b1 → ⊥
  bad7365  p = false≢true (cong lower p)
  cut7365 : Adequate {ℓ} ((op (op (op (var 0) (op (var 1) (var 2))) (var 0)) (op (var 3) (var 0))) , (var 1)) → ⊥
  cut7365  adequate = bad7365  (Adequate.valid adequate Two boolean env19)
  bad7366 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b0 b1)) b0) (bop b0 b0)) b1 → ⊥
  bad7366  p = false≢true (cong lower p)
  cut7366 : Adequate {ℓ} ((op (op (op (var 0) (op (var 1) (var 2))) (var 0)) (op (var 3) (var 0))) , (var 2)) → ⊥
  cut7366  adequate = bad7366  (Adequate.valid adequate Two boolean env8)
  bad7367 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b0 b0)) b0) (bop b1 b0)) b1 → ⊥
  bad7367  p = false≢true (cong lower p)
  cut7367 : Adequate {ℓ} ((op (op (op (var 0) (op (var 1) (var 2))) (var 0)) (op (var 3) (var 0))) , (var 3)) → ⊥
  cut7367  adequate = bad7367  (Adequate.valid adequate Two boolean env5)
  bad7368 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b0 b0)) b0) (bop b0 b0)) b1 → ⊥
  bad7368  p = false≢true (cong lower p)
  cut7368 : Adequate {ℓ} ((op (op (op (var 0) (op (var 1) (var 2))) (var 0)) (op (var 3) (var 0))) , (var 4)) → ⊥
  cut7368  adequate = bad7368  (Adequate.valid adequate Two boolean env9)
  bad7369 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b1 b0)) b0) (bop b1 b1)) b0 → ⊥
  bad7369  p = false≢true (sym (cong lower p))
  cut7369 : Adequate {ℓ} ((op (op (op (var 0) (op (var 1) (var 2))) (var 0)) (op (var 3) (var 1))) , (var 0)) → ⊥
  cut7369  adequate = bad7369  (Adequate.valid adequate Two boolean env13)
  bad7370 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b1 b0)) b0) (bop b0 b1)) b1 → ⊥
  bad7370  p = false≢true (cong lower p)
  cut7370 : Adequate {ℓ} ((op (op (op (var 0) (op (var 1) (var 2))) (var 0)) (op (var 3) (var 1))) , (var 1)) → ⊥
  cut7370  adequate = bad7370  (Adequate.valid adequate Two boolean env19)
  bad7371 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b0 b1)) b0) (bop b0 b0)) b1 → ⊥
  bad7371  p = false≢true (cong lower p)
  cut7371 : Adequate {ℓ} ((op (op (op (var 0) (op (var 1) (var 2))) (var 0)) (op (var 3) (var 1))) , (var 2)) → ⊥
  cut7371  adequate = bad7371  (Adequate.valid adequate Two boolean env8)
  bad7372 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b0 b0)) b0) (bop b1 b0)) b1 → ⊥
  bad7372  p = false≢true (cong lower p)
  cut7372 : Adequate {ℓ} ((op (op (op (var 0) (op (var 1) (var 2))) (var 0)) (op (var 3) (var 1))) , (var 3)) → ⊥
  cut7372  adequate = bad7372  (Adequate.valid adequate Two boolean env5)
  bad7373 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b0 b0)) b0) (bop b0 b0)) b1 → ⊥
  bad7373  p = false≢true (cong lower p)
  cut7373 : Adequate {ℓ} ((op (op (op (var 0) (op (var 1) (var 2))) (var 0)) (op (var 3) (var 1))) , (var 4)) → ⊥
  cut7373  adequate = bad7373  (Adequate.valid adequate Two boolean env9)
  bad7374 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b0 b1)) b0) (bop b1 b1)) b0 → ⊥
  bad7374  p = false≢true (sym (cong lower p))
  cut7374 : Adequate {ℓ} ((op (op (op (var 0) (op (var 1) (var 2))) (var 0)) (op (var 3) (var 2))) , (var 0)) → ⊥
  cut7374  adequate = bad7374  (Adequate.valid adequate Two boolean env7)
  bad7375 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b0 b1)) b0) (bop b1 b1)) b0 → ⊥
  bad7375  p = false≢true (sym (cong lower p))
  cut7375 : Adequate {ℓ} ((op (op (op (var 0) (op (var 1) (var 2))) (var 0)) (op (var 3) (var 2))) , (var 1)) → ⊥
  cut7375  adequate = bad7375  (Adequate.valid adequate Two boolean env7)
  bad7376 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b0 b1)) b0) (bop b0 b1)) b1 → ⊥
  bad7376  p = false≢true (cong lower p)
  cut7376 : Adequate {ℓ} ((op (op (op (var 0) (op (var 1) (var 2))) (var 0)) (op (var 3) (var 2))) , (var 2)) → ⊥
  cut7376  adequate = bad7376  (Adequate.valid adequate Two boolean env8)
  bad7377 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b0 b0)) b0) (bop b1 b0)) b1 → ⊥
  bad7377  p = false≢true (cong lower p)
  cut7377 : Adequate {ℓ} ((op (op (op (var 0) (op (var 1) (var 2))) (var 0)) (op (var 3) (var 2))) , (var 3)) → ⊥
  cut7377  adequate = bad7377  (Adequate.valid adequate Two boolean env5)
  bad7378 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b0 b0)) b0) (bop b0 b0)) b1 → ⊥
  bad7378  p = false≢true (cong lower p)
  cut7378 : Adequate {ℓ} ((op (op (op (var 0) (op (var 1) (var 2))) (var 0)) (op (var 3) (var 2))) , (var 4)) → ⊥
  cut7378  adequate = bad7378  (Adequate.valid adequate Two boolean env9)
  bad7379 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b0 b0)) b0) (bop b1 b1)) b0 → ⊥
  bad7379  p = false≢true (sym (cong lower p))
  cut7379 : Adequate {ℓ} ((op (op (op (var 0) (op (var 1) (var 2))) (var 0)) (op (var 3) (var 3))) , (var 0)) → ⊥
  cut7379  adequate = bad7379  (Adequate.valid adequate Two boolean env5)
  bad7380 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b0 b0)) b0) (bop b1 b1)) b0 → ⊥
  bad7380  p = false≢true (sym (cong lower p))
  cut7380 : Adequate {ℓ} ((op (op (op (var 0) (op (var 1) (var 2))) (var 0)) (op (var 3) (var 3))) , (var 1)) → ⊥
  cut7380  adequate = bad7380  (Adequate.valid adequate Two boolean env5)
  bad7381 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b0 b0)) b0) (bop b1 b1)) b0 → ⊥
  bad7381  p = false≢true (sym (cong lower p))
  cut7381 : Adequate {ℓ} ((op (op (op (var 0) (op (var 1) (var 2))) (var 0)) (op (var 3) (var 3))) , (var 2)) → ⊥
  cut7381  adequate = bad7381  (Adequate.valid adequate Two boolean env5)
  env20 : ℕ → Two
  env20 zero = b1
  env20 (suc zero) = b1
  env20 (suc (suc zero)) = b1
  env20 (suc (suc (suc zero))) = b0
  env20 (suc (suc (suc (suc rest)))) = b0
  bad7382 : PathP (λ _ → Two) (bop (bop (bop b1 (bop b1 b1)) b1) (bop b0 b0)) b0 → ⊥
  bad7382  p = false≢true (sym (cong lower p))
  cut7382 : Adequate {ℓ} ((op (op (op (var 0) (op (var 1) (var 2))) (var 0)) (op (var 3) (var 3))) , (var 3)) → ⊥
  cut7382  adequate = bad7382  (Adequate.valid adequate Two boolean env20)
  bad7383 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b0 b0)) b0) (bop b0 b0)) b1 → ⊥
  bad7383  p = false≢true (cong lower p)
  cut7383 : Adequate {ℓ} ((op (op (op (var 0) (op (var 1) (var 2))) (var 0)) (op (var 3) (var 3))) , (var 4)) → ⊥
  cut7383  adequate = bad7383  (Adequate.valid adequate Two boolean env9)
  bad7384 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b0 b0)) b0) (bop b1 b1)) b0 → ⊥
  bad7384  p = false≢true (sym (cong lower p))
  cut7384 : Adequate {ℓ} ((op (op (op (var 0) (op (var 1) (var 2))) (var 0)) (op (var 3) (var 4))) , (var 0)) → ⊥
  cut7384  adequate = bad7384  (Adequate.valid adequate Two boolean env15)
  bad7385 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b0 b0)) b0) (bop b1 b1)) b0 → ⊥
  bad7385  p = false≢true (sym (cong lower p))
  cut7385 : Adequate {ℓ} ((op (op (op (var 0) (op (var 1) (var 2))) (var 0)) (op (var 3) (var 4))) , (var 1)) → ⊥
  cut7385  adequate = bad7385  (Adequate.valid adequate Two boolean env15)
  bad7386 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b0 b0)) b0) (bop b1 b1)) b0 → ⊥
  bad7386  p = false≢true (sym (cong lower p))
  cut7386 : Adequate {ℓ} ((op (op (op (var 0) (op (var 1) (var 2))) (var 0)) (op (var 3) (var 4))) , (var 2)) → ⊥
  cut7386  adequate = bad7386  (Adequate.valid adequate Two boolean env15)
  bad7387 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b0 b0)) b0) (bop b1 b0)) b1 → ⊥
  bad7387  p = false≢true (cong lower p)
  cut7387 : Adequate {ℓ} ((op (op (op (var 0) (op (var 1) (var 2))) (var 0)) (op (var 3) (var 4))) , (var 3)) → ⊥
  cut7387  adequate = bad7387  (Adequate.valid adequate Two boolean env16)
  bad7388 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b0 b0)) b0) (bop b0 b1)) b1 → ⊥
  bad7388  p = false≢true (cong lower p)
  cut7388 : Adequate {ℓ} ((op (op (op (var 0) (op (var 1) (var 2))) (var 0)) (op (var 3) (var 4))) , (var 4)) → ⊥
  cut7388  adequate = bad7388  (Adequate.valid adequate Two boolean env9)
  bad7389 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b0 b0)) b0) (bop b0 b0)) b1 → ⊥
  bad7389  p = false≢true (cong lower p)
  cut7389 : Adequate {ℓ} ((op (op (op (var 0) (op (var 1) (var 2))) (var 0)) (op (var 3) (var 4))) , (var 5)) → ⊥
  cut7389  adequate = bad7389  (Adequate.valid adequate Two boolean env17)
  bad7390 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b1 b0)) b1) (bop b0 b0)) b0 → ⊥
  bad7390  p = false≢true (sym (cong lower p))
  cut7390 : Adequate {ℓ} ((op (op (op (var 0) (op (var 1) (var 2))) (var 1)) (op (var 0) (var 0))) , (var 0)) → ⊥
  cut7390  adequate = bad7390  (Adequate.valid adequate Two boolean env4)
  bad7391 : PathP (λ _ → Two) (bop (bop (bop b1 (bop b0 b0)) b0) (bop b1 b1)) b0 → ⊥
  bad7391  p = false≢true (sym (cong lower p))
  cut7391 : Adequate {ℓ} ((op (op (op (var 0) (op (var 1) (var 2))) (var 1)) (op (var 0) (var 0))) , (var 1)) → ⊥
  cut7391  adequate = bad7391  (Adequate.valid adequate Two boolean env10)
  bad7392 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b0 b1)) b0) (bop b0 b0)) b1 → ⊥
  bad7392  p = false≢true (cong lower p)
  cut7392 : Adequate {ℓ} ((op (op (op (var 0) (op (var 1) (var 2))) (var 1)) (op (var 0) (var 0))) , (var 2)) → ⊥
  cut7392  adequate = bad7392  (Adequate.valid adequate Two boolean env1)
  bad7393 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b0 b0)) b0) (bop b0 b0)) b1 → ⊥
  bad7393  p = false≢true (cong lower p)
  cut7393 : Adequate {ℓ} ((op (op (op (var 0) (op (var 1) (var 2))) (var 1)) (op (var 0) (var 0))) , (var 3)) → ⊥
  cut7393  adequate = bad7393  (Adequate.valid adequate Two boolean env5)
  bad7394 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b1 b0)) b1) (bop b0 b1)) b0 → ⊥
  bad7394  p = false≢true (sym (cong lower p))
  cut7394 : Adequate {ℓ} ((op (op (op (var 0) (op (var 1) (var 2))) (var 1)) (op (var 0) (var 1))) , (var 0)) → ⊥
  cut7394  adequate = bad7394  (Adequate.valid adequate Two boolean env4)
  holds7395 : (z0 z1 z2 : A3) → (mul3 (mul3 (mul3 z0 (mul3 z1 z2)) z1) (mul3 z0 z1)) ≡ z1
  holds7395 z0 z1 z2 = refl
  cut7395 : Adequate {ℓ} ((op (op (op (var 0) (op (var 1) (var 2))) (var 1)) (op (var 0) (var 1))) , (var 1)) → ⊥
  cut7395  = reject3 ((op (op (op (var 0) (op (var 1) (var 2))) (var 1)) (op (var 0) (var 1))) , (var 1)) (λ env → holds7395 (env 0) (env 1) (env 2))
  bad7396 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b0 b1)) b0) (bop b0 b0)) b1 → ⊥
  bad7396  p = false≢true (cong lower p)
  cut7396 : Adequate {ℓ} ((op (op (op (var 0) (op (var 1) (var 2))) (var 1)) (op (var 0) (var 1))) , (var 2)) → ⊥
  cut7396  adequate = bad7396  (Adequate.valid adequate Two boolean env1)
  bad7397 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b0 b0)) b0) (bop b0 b0)) b1 → ⊥
  bad7397  p = false≢true (cong lower p)
  cut7397 : Adequate {ℓ} ((op (op (op (var 0) (op (var 1) (var 2))) (var 1)) (op (var 0) (var 1))) , (var 3)) → ⊥
  cut7397  adequate = bad7397  (Adequate.valid adequate Two boolean env5)
  bad7398 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b1 b0)) b1) (bop b0 b0)) b0 → ⊥
  bad7398  p = false≢true (sym (cong lower p))
  cut7398 : Adequate {ℓ} ((op (op (op (var 0) (op (var 1) (var 2))) (var 1)) (op (var 0) (var 2))) , (var 0)) → ⊥
  cut7398  adequate = bad7398  (Adequate.valid adequate Two boolean env4)
  bad7399 : PathP (λ _ → Two) (bop (bop (bop b1 (bop b0 b1)) b0) (bop b1 b1)) b0 → ⊥
  bad7399  p = false≢true (sym (cong lower p))
  cut7399 : Adequate {ℓ} ((op (op (op (var 0) (op (var 1) (var 2))) (var 1)) (op (var 0) (var 2))) , (var 1)) → ⊥
  cut7399  adequate = bad7399  (Adequate.valid adequate Two boolean env6)
  bad7400 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b0 b1)) b0) (bop b0 b1)) b1 → ⊥
  bad7400  p = false≢true (cong lower p)
  cut7400 : Adequate {ℓ} ((op (op (op (var 0) (op (var 1) (var 2))) (var 1)) (op (var 0) (var 2))) , (var 2)) → ⊥
  cut7400  adequate = bad7400  (Adequate.valid adequate Two boolean env1)
  bad7401 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b0 b0)) b0) (bop b0 b0)) b1 → ⊥
  bad7401  p = false≢true (cong lower p)
  cut7401 : Adequate {ℓ} ((op (op (op (var 0) (op (var 1) (var 2))) (var 1)) (op (var 0) (var 2))) , (var 3)) → ⊥
  cut7401  adequate = bad7401  (Adequate.valid adequate Two boolean env5)
  bad7402 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b1 b0)) b1) (bop b0 b0)) b0 → ⊥
  bad7402  p = false≢true (sym (cong lower p))
  cut7402 : Adequate {ℓ} ((op (op (op (var 0) (op (var 1) (var 2))) (var 1)) (op (var 0) (var 3))) , (var 0)) → ⊥
  cut7402  adequate = bad7402  (Adequate.valid adequate Two boolean env19)
  bad7403 : PathP (λ _ → Two) (bop (bop (bop b1 (bop b0 b0)) b0) (bop b1 b1)) b0 → ⊥
  bad7403  p = false≢true (sym (cong lower p))
  cut7403 : Adequate {ℓ} ((op (op (op (var 0) (op (var 1) (var 2))) (var 1)) (op (var 0) (var 3))) , (var 1)) → ⊥
  cut7403  adequate = bad7403  (Adequate.valid adequate Two boolean env12)
  bad7404 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b0 b1)) b0) (bop b0 b0)) b1 → ⊥
  bad7404  p = false≢true (cong lower p)
  cut7404 : Adequate {ℓ} ((op (op (op (var 0) (op (var 1) (var 2))) (var 1)) (op (var 0) (var 3))) , (var 2)) → ⊥
  cut7404  adequate = bad7404  (Adequate.valid adequate Two boolean env8)
  bad7405 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b0 b0)) b0) (bop b0 b1)) b1 → ⊥
  bad7405  p = false≢true (cong lower p)
  cut7405 : Adequate {ℓ} ((op (op (op (var 0) (op (var 1) (var 2))) (var 1)) (op (var 0) (var 3))) , (var 3)) → ⊥
  cut7405  adequate = bad7405  (Adequate.valid adequate Two boolean env5)
  bad7406 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b0 b0)) b0) (bop b0 b0)) b1 → ⊥
  bad7406  p = false≢true (cong lower p)
  cut7406 : Adequate {ℓ} ((op (op (op (var 0) (op (var 1) (var 2))) (var 1)) (op (var 0) (var 3))) , (var 4)) → ⊥
  cut7406  adequate = bad7406  (Adequate.valid adequate Two boolean env9)
  bad7407 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b1 b0)) b1) (bop b1 b0)) b0 → ⊥
  bad7407  p = false≢true (sym (cong lower p))
  cut7407 : Adequate {ℓ} ((op (op (op (var 0) (op (var 1) (var 2))) (var 1)) (op (var 1) (var 0))) , (var 0)) → ⊥
  cut7407  adequate = bad7407  (Adequate.valid adequate Two boolean env4)
  holds7408 : (z0 z1 z2 : A11) → (mul11 (mul11 (mul11 z0 (mul11 z1 z2)) z1) (mul11 z1 z0)) ≡ z1
  holds7408 m11c0 m11c0 m11c0 = refl
  holds7408 m11c0 m11c0 m11c1 = refl
  holds7408 m11c0 m11c0 m11c2 = refl
  holds7408 m11c0 m11c1 z2 = refl
  holds7408 m11c0 m11c2 m11c0 = refl
  holds7408 m11c0 m11c2 m11c1 = refl
  holds7408 m11c0 m11c2 m11c2 = refl
  holds7408 m11c1 m11c0 z2 = refl
  holds7408 m11c1 m11c1 z2 = refl
  holds7408 m11c1 m11c2 z2 = refl
  holds7408 m11c2 m11c0 m11c0 = refl
  holds7408 m11c2 m11c0 m11c1 = refl
  holds7408 m11c2 m11c0 m11c2 = refl
  holds7408 m11c2 m11c1 z2 = refl
  holds7408 m11c2 m11c2 m11c0 = refl
  holds7408 m11c2 m11c2 m11c1 = refl
  holds7408 m11c2 m11c2 m11c2 = refl
  cut7408 : Adequate {ℓ} ((op (op (op (var 0) (op (var 1) (var 2))) (var 1)) (op (var 1) (var 0))) , (var 1)) → ⊥
  cut7408  = reject11 ((op (op (op (var 0) (op (var 1) (var 2))) (var 1)) (op (var 1) (var 0))) , (var 1)) (λ env → holds7408 (env 0) (env 1) (env 2))
  bad7409 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b0 b1)) b0) (bop b0 b0)) b1 → ⊥
  bad7409  p = false≢true (cong lower p)
  cut7409 : Adequate {ℓ} ((op (op (op (var 0) (op (var 1) (var 2))) (var 1)) (op (var 1) (var 0))) , (var 2)) → ⊥
  cut7409  adequate = bad7409  (Adequate.valid adequate Two boolean env1)
  bad7410 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b0 b0)) b0) (bop b0 b0)) b1 → ⊥
  bad7410  p = false≢true (cong lower p)
  cut7410 : Adequate {ℓ} ((op (op (op (var 0) (op (var 1) (var 2))) (var 1)) (op (var 1) (var 0))) , (var 3)) → ⊥
  cut7410  adequate = bad7410  (Adequate.valid adequate Two boolean env5)
  bad7411 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b1 b0)) b1) (bop b1 b1)) b0 → ⊥
  bad7411  p = false≢true (sym (cong lower p))
  cut7411 : Adequate {ℓ} ((op (op (op (var 0) (op (var 1) (var 2))) (var 1)) (op (var 1) (var 1))) , (var 0)) → ⊥
  cut7411  adequate = bad7411  (Adequate.valid adequate Two boolean env4)
  holds7412 : (z0 z1 z2 : A3) → (mul3 (mul3 (mul3 z0 (mul3 z1 z2)) z1) (mul3 z1 z1)) ≡ z1
  holds7412 z0 z1 z2 = refl
  cut7412 : Adequate {ℓ} ((op (op (op (var 0) (op (var 1) (var 2))) (var 1)) (op (var 1) (var 1))) , (var 1)) → ⊥
  cut7412  = reject3 ((op (op (op (var 0) (op (var 1) (var 2))) (var 1)) (op (var 1) (var 1))) , (var 1)) (λ env → holds7412 (env 0) (env 1) (env 2))
  bad7413 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b0 b1)) b0) (bop b0 b0)) b1 → ⊥
  bad7413  p = false≢true (cong lower p)
  cut7413 : Adequate {ℓ} ((op (op (op (var 0) (op (var 1) (var 2))) (var 1)) (op (var 1) (var 1))) , (var 2)) → ⊥
  cut7413  adequate = bad7413  (Adequate.valid adequate Two boolean env1)
  bad7414 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b0 b0)) b0) (bop b0 b0)) b1 → ⊥
  bad7414  p = false≢true (cong lower p)
  cut7414 : Adequate {ℓ} ((op (op (op (var 0) (op (var 1) (var 2))) (var 1)) (op (var 1) (var 1))) , (var 3)) → ⊥
  cut7414  adequate = bad7414  (Adequate.valid adequate Two boolean env5)
  bad7415 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b1 b0)) b1) (bop b1 b0)) b0 → ⊥
  bad7415  p = false≢true (sym (cong lower p))
  cut7415 : Adequate {ℓ} ((op (op (op (var 0) (op (var 1) (var 2))) (var 1)) (op (var 1) (var 2))) , (var 0)) → ⊥
  cut7415  adequate = bad7415  (Adequate.valid adequate Two boolean env4)
  bad7416 : PathP (λ _ → Two) (bop (bop (bop b1 (bop b1 b0)) b1) (bop b1 b0)) b1 → ⊥
  bad7416  p = false≢true (cong lower p)
  cut7416 : Adequate {ℓ} ((op (op (op (var 0) (op (var 1) (var 2))) (var 1)) (op (var 1) (var 2))) , (var 1)) → ⊥
  cut7416  adequate = bad7416  (Adequate.valid adequate Two boolean env11)
  bad7417 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b0 b1)) b0) (bop b0 b1)) b1 → ⊥
  bad7417  p = false≢true (cong lower p)
  cut7417 : Adequate {ℓ} ((op (op (op (var 0) (op (var 1) (var 2))) (var 1)) (op (var 1) (var 2))) , (var 2)) → ⊥
  cut7417  adequate = bad7417  (Adequate.valid adequate Two boolean env1)
  bad7418 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b0 b0)) b0) (bop b0 b0)) b1 → ⊥
  bad7418  p = false≢true (cong lower p)
  cut7418 : Adequate {ℓ} ((op (op (op (var 0) (op (var 1) (var 2))) (var 1)) (op (var 1) (var 2))) , (var 3)) → ⊥
  cut7418  adequate = bad7418  (Adequate.valid adequate Two boolean env5)
  bad7419 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b1 b0)) b1) (bop b1 b0)) b0 → ⊥
  bad7419  p = false≢true (sym (cong lower p))
  cut7419 : Adequate {ℓ} ((op (op (op (var 0) (op (var 1) (var 2))) (var 1)) (op (var 1) (var 3))) , (var 0)) → ⊥
  cut7419  adequate = bad7419  (Adequate.valid adequate Two boolean env19)
  env21 : ℕ → Two
  env21 zero = b1
  env21 (suc zero) = b1
  env21 (suc (suc zero)) = b0
  env21 (suc (suc (suc zero))) = b0
  env21 (suc (suc (suc (suc rest)))) = b0
  bad7420 : PathP (λ _ → Two) (bop (bop (bop b1 (bop b1 b0)) b1) (bop b1 b0)) b1 → ⊥
  bad7420  p = false≢true (cong lower p)
  cut7420 : Adequate {ℓ} ((op (op (op (var 0) (op (var 1) (var 2))) (var 1)) (op (var 1) (var 3))) , (var 1)) → ⊥
  cut7420  adequate = bad7420  (Adequate.valid adequate Two boolean env21)
  bad7421 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b0 b1)) b0) (bop b0 b0)) b1 → ⊥
  bad7421  p = false≢true (cong lower p)
  cut7421 : Adequate {ℓ} ((op (op (op (var 0) (op (var 1) (var 2))) (var 1)) (op (var 1) (var 3))) , (var 2)) → ⊥
  cut7421  adequate = bad7421  (Adequate.valid adequate Two boolean env8)
  bad7422 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b0 b0)) b0) (bop b0 b1)) b1 → ⊥
  bad7422  p = false≢true (cong lower p)
  cut7422 : Adequate {ℓ} ((op (op (op (var 0) (op (var 1) (var 2))) (var 1)) (op (var 1) (var 3))) , (var 3)) → ⊥
  cut7422  adequate = bad7422  (Adequate.valid adequate Two boolean env5)
  bad7423 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b0 b0)) b0) (bop b0 b0)) b1 → ⊥
  bad7423  p = false≢true (cong lower p)
  cut7423 : Adequate {ℓ} ((op (op (op (var 0) (op (var 1) (var 2))) (var 1)) (op (var 1) (var 3))) , (var 4)) → ⊥
  cut7423  adequate = bad7423  (Adequate.valid adequate Two boolean env9)
  bad7424 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b1 b0)) b1) (bop b0 b0)) b0 → ⊥
  bad7424  p = false≢true (sym (cong lower p))
  cut7424 : Adequate {ℓ} ((op (op (op (var 0) (op (var 1) (var 2))) (var 1)) (op (var 2) (var 0))) , (var 0)) → ⊥
  cut7424  adequate = bad7424  (Adequate.valid adequate Two boolean env4)
  bad7425 : PathP (λ _ → Two) (bop (bop (bop b1 (bop b0 b1)) b0) (bop b1 b1)) b0 → ⊥
  bad7425  p = false≢true (sym (cong lower p))
  cut7425 : Adequate {ℓ} ((op (op (op (var 0) (op (var 1) (var 2))) (var 1)) (op (var 2) (var 0))) , (var 1)) → ⊥
  cut7425  adequate = bad7425  (Adequate.valid adequate Two boolean env6)
  bad7426 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b0 b1)) b0) (bop b1 b0)) b1 → ⊥
  bad7426  p = false≢true (cong lower p)
  cut7426 : Adequate {ℓ} ((op (op (op (var 0) (op (var 1) (var 2))) (var 1)) (op (var 2) (var 0))) , (var 2)) → ⊥
  cut7426  adequate = bad7426  (Adequate.valid adequate Two boolean env1)
  bad7427 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b0 b0)) b0) (bop b0 b0)) b1 → ⊥
  bad7427  p = false≢true (cong lower p)
  cut7427 : Adequate {ℓ} ((op (op (op (var 0) (op (var 1) (var 2))) (var 1)) (op (var 2) (var 0))) , (var 3)) → ⊥
  cut7427  adequate = bad7427  (Adequate.valid adequate Two boolean env5)
  bad7428 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b1 b0)) b1) (bop b0 b1)) b0 → ⊥
  bad7428  p = false≢true (sym (cong lower p))
  cut7428 : Adequate {ℓ} ((op (op (op (var 0) (op (var 1) (var 2))) (var 1)) (op (var 2) (var 1))) , (var 0)) → ⊥
  cut7428  adequate = bad7428  (Adequate.valid adequate Two boolean env4)
  bad7429 : PathP (λ _ → Two) (bop (bop (bop b1 (bop b1 b0)) b1) (bop b0 b1)) b1 → ⊥
  bad7429  p = false≢true (cong lower p)
  cut7429 : Adequate {ℓ} ((op (op (op (var 0) (op (var 1) (var 2))) (var 1)) (op (var 2) (var 1))) , (var 1)) → ⊥
  cut7429  adequate = bad7429  (Adequate.valid adequate Two boolean env11)
  bad7430 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b0 b1)) b0) (bop b1 b0)) b1 → ⊥
  bad7430  p = false≢true (cong lower p)
  cut7430 : Adequate {ℓ} ((op (op (op (var 0) (op (var 1) (var 2))) (var 1)) (op (var 2) (var 1))) , (var 2)) → ⊥
  cut7430  adequate = bad7430  (Adequate.valid adequate Two boolean env1)
  bad7431 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b0 b0)) b0) (bop b0 b0)) b1 → ⊥
  bad7431  p = false≢true (cong lower p)
  cut7431 : Adequate {ℓ} ((op (op (op (var 0) (op (var 1) (var 2))) (var 1)) (op (var 2) (var 1))) , (var 3)) → ⊥
  cut7431  adequate = bad7431  (Adequate.valid adequate Two boolean env5)
  bad7432 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b0 b1)) b0) (bop b1 b1)) b0 → ⊥
  bad7432  p = false≢true (sym (cong lower p))
  cut7432 : Adequate {ℓ} ((op (op (op (var 0) (op (var 1) (var 2))) (var 1)) (op (var 2) (var 2))) , (var 0)) → ⊥
  cut7432  adequate = bad7432  (Adequate.valid adequate Two boolean env1)
  bad7433 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b0 b1)) b0) (bop b1 b1)) b0 → ⊥
  bad7433  p = false≢true (sym (cong lower p))
  cut7433 : Adequate {ℓ} ((op (op (op (var 0) (op (var 1) (var 2))) (var 1)) (op (var 2) (var 2))) , (var 1)) → ⊥
  cut7433  adequate = bad7433  (Adequate.valid adequate Two boolean env1)
  bad7434 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b1 b0)) b1) (bop b0 b0)) b0 → ⊥
  bad7434  p = false≢true (sym (cong lower p))
  cut7434 : Adequate {ℓ} ((op (op (op (var 0) (op (var 1) (var 2))) (var 1)) (op (var 2) (var 2))) , (var 2)) → ⊥
  cut7434  adequate = bad7434  (Adequate.valid adequate Two boolean env4)
  bad7435 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b0 b0)) b0) (bop b0 b0)) b1 → ⊥
  bad7435  p = false≢true (cong lower p)
  cut7435 : Adequate {ℓ} ((op (op (op (var 0) (op (var 1) (var 2))) (var 1)) (op (var 2) (var 2))) , (var 3)) → ⊥
  cut7435  adequate = bad7435  (Adequate.valid adequate Two boolean env5)
  bad7436 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b0 b1)) b0) (bop b1 b1)) b0 → ⊥
  bad7436  p = false≢true (sym (cong lower p))
  cut7436 : Adequate {ℓ} ((op (op (op (var 0) (op (var 1) (var 2))) (var 1)) (op (var 2) (var 3))) , (var 0)) → ⊥
  cut7436  adequate = bad7436  (Adequate.valid adequate Two boolean env7)
  bad7437 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b0 b1)) b0) (bop b1 b1)) b0 → ⊥
  bad7437  p = false≢true (sym (cong lower p))
  cut7437 : Adequate {ℓ} ((op (op (op (var 0) (op (var 1) (var 2))) (var 1)) (op (var 2) (var 3))) , (var 1)) → ⊥
  cut7437  adequate = bad7437  (Adequate.valid adequate Two boolean env7)
  bad7438 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b0 b1)) b0) (bop b1 b0)) b1 → ⊥
  bad7438  p = false≢true (cong lower p)
  cut7438 : Adequate {ℓ} ((op (op (op (var 0) (op (var 1) (var 2))) (var 1)) (op (var 2) (var 3))) , (var 2)) → ⊥
  cut7438  adequate = bad7438  (Adequate.valid adequate Two boolean env8)
  bad7439 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b0 b0)) b0) (bop b0 b1)) b1 → ⊥
  bad7439  p = false≢true (cong lower p)
  cut7439 : Adequate {ℓ} ((op (op (op (var 0) (op (var 1) (var 2))) (var 1)) (op (var 2) (var 3))) , (var 3)) → ⊥
  cut7439  adequate = bad7439  (Adequate.valid adequate Two boolean env5)
  bad7440 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b0 b0)) b0) (bop b0 b0)) b1 → ⊥
  bad7440  p = false≢true (cong lower p)
  cut7440 : Adequate {ℓ} ((op (op (op (var 0) (op (var 1) (var 2))) (var 1)) (op (var 2) (var 3))) , (var 4)) → ⊥
  cut7440  adequate = bad7440  (Adequate.valid adequate Two boolean env9)
  bad7441 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b1 b0)) b1) (bop b0 b0)) b0 → ⊥
  bad7441  p = false≢true (sym (cong lower p))
  cut7441 : Adequate {ℓ} ((op (op (op (var 0) (op (var 1) (var 2))) (var 1)) (op (var 3) (var 0))) , (var 0)) → ⊥
  cut7441  adequate = bad7441  (Adequate.valid adequate Two boolean env19)
  bad7442 : PathP (λ _ → Two) (bop (bop (bop b1 (bop b0 b0)) b0) (bop b1 b1)) b0 → ⊥
  bad7442  p = false≢true (sym (cong lower p))
  cut7442 : Adequate {ℓ} ((op (op (op (var 0) (op (var 1) (var 2))) (var 1)) (op (var 3) (var 0))) , (var 1)) → ⊥
  cut7442  adequate = bad7442  (Adequate.valid adequate Two boolean env12)
  bad7443 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b0 b1)) b0) (bop b0 b0)) b1 → ⊥
  bad7443  p = false≢true (cong lower p)
  cut7443 : Adequate {ℓ} ((op (op (op (var 0) (op (var 1) (var 2))) (var 1)) (op (var 3) (var 0))) , (var 2)) → ⊥
  cut7443  adequate = bad7443  (Adequate.valid adequate Two boolean env8)
  bad7444 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b0 b0)) b0) (bop b1 b0)) b1 → ⊥
  bad7444  p = false≢true (cong lower p)
  cut7444 : Adequate {ℓ} ((op (op (op (var 0) (op (var 1) (var 2))) (var 1)) (op (var 3) (var 0))) , (var 3)) → ⊥
  cut7444  adequate = bad7444  (Adequate.valid adequate Two boolean env5)
  bad7445 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b0 b0)) b0) (bop b0 b0)) b1 → ⊥
  bad7445  p = false≢true (cong lower p)
  cut7445 : Adequate {ℓ} ((op (op (op (var 0) (op (var 1) (var 2))) (var 1)) (op (var 3) (var 0))) , (var 4)) → ⊥
  cut7445  adequate = bad7445  (Adequate.valid adequate Two boolean env9)
  bad7446 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b1 b0)) b1) (bop b0 b1)) b0 → ⊥
  bad7446  p = false≢true (sym (cong lower p))
  cut7446 : Adequate {ℓ} ((op (op (op (var 0) (op (var 1) (var 2))) (var 1)) (op (var 3) (var 1))) , (var 0)) → ⊥
  cut7446  adequate = bad7446  (Adequate.valid adequate Two boolean env19)
  bad7447 : PathP (λ _ → Two) (bop (bop (bop b1 (bop b1 b0)) b1) (bop b0 b1)) b1 → ⊥
  bad7447  p = false≢true (cong lower p)
  cut7447 : Adequate {ℓ} ((op (op (op (var 0) (op (var 1) (var 2))) (var 1)) (op (var 3) (var 1))) , (var 1)) → ⊥
  cut7447  adequate = bad7447  (Adequate.valid adequate Two boolean env21)
  bad7448 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b0 b1)) b0) (bop b0 b0)) b1 → ⊥
  bad7448  p = false≢true (cong lower p)
  cut7448 : Adequate {ℓ} ((op (op (op (var 0) (op (var 1) (var 2))) (var 1)) (op (var 3) (var 1))) , (var 2)) → ⊥
  cut7448  adequate = bad7448  (Adequate.valid adequate Two boolean env8)
  bad7449 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b0 b0)) b0) (bop b1 b0)) b1 → ⊥
  bad7449  p = false≢true (cong lower p)
  cut7449 : Adequate {ℓ} ((op (op (op (var 0) (op (var 1) (var 2))) (var 1)) (op (var 3) (var 1))) , (var 3)) → ⊥
  cut7449  adequate = bad7449  (Adequate.valid adequate Two boolean env5)
  bad7450 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b0 b0)) b0) (bop b0 b0)) b1 → ⊥
  bad7450  p = false≢true (cong lower p)
  cut7450 : Adequate {ℓ} ((op (op (op (var 0) (op (var 1) (var 2))) (var 1)) (op (var 3) (var 1))) , (var 4)) → ⊥
  cut7450  adequate = bad7450  (Adequate.valid adequate Two boolean env9)
  bad7451 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b0 b1)) b0) (bop b1 b1)) b0 → ⊥
  bad7451  p = false≢true (sym (cong lower p))
  cut7451 : Adequate {ℓ} ((op (op (op (var 0) (op (var 1) (var 2))) (var 1)) (op (var 3) (var 2))) , (var 0)) → ⊥
  cut7451  adequate = bad7451  (Adequate.valid adequate Two boolean env7)
  bad7452 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b0 b1)) b0) (bop b1 b1)) b0 → ⊥
  bad7452  p = false≢true (sym (cong lower p))
  cut7452 : Adequate {ℓ} ((op (op (op (var 0) (op (var 1) (var 2))) (var 1)) (op (var 3) (var 2))) , (var 1)) → ⊥
  cut7452  adequate = bad7452  (Adequate.valid adequate Two boolean env7)
  bad7453 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b0 b1)) b0) (bop b0 b1)) b1 → ⊥
  bad7453  p = false≢true (cong lower p)
  cut7453 : Adequate {ℓ} ((op (op (op (var 0) (op (var 1) (var 2))) (var 1)) (op (var 3) (var 2))) , (var 2)) → ⊥
  cut7453  adequate = bad7453  (Adequate.valid adequate Two boolean env8)
  bad7454 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b0 b0)) b0) (bop b1 b0)) b1 → ⊥
  bad7454  p = false≢true (cong lower p)
  cut7454 : Adequate {ℓ} ((op (op (op (var 0) (op (var 1) (var 2))) (var 1)) (op (var 3) (var 2))) , (var 3)) → ⊥
  cut7454  adequate = bad7454  (Adequate.valid adequate Two boolean env5)
  bad7455 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b0 b0)) b0) (bop b0 b0)) b1 → ⊥
  bad7455  p = false≢true (cong lower p)
  cut7455 : Adequate {ℓ} ((op (op (op (var 0) (op (var 1) (var 2))) (var 1)) (op (var 3) (var 2))) , (var 4)) → ⊥
  cut7455  adequate = bad7455  (Adequate.valid adequate Two boolean env9)
  bad7456 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b0 b0)) b0) (bop b1 b1)) b0 → ⊥
  bad7456  p = false≢true (sym (cong lower p))
  cut7456 : Adequate {ℓ} ((op (op (op (var 0) (op (var 1) (var 2))) (var 1)) (op (var 3) (var 3))) , (var 0)) → ⊥
  cut7456  adequate = bad7456  (Adequate.valid adequate Two boolean env5)
  bad7457 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b0 b0)) b0) (bop b1 b1)) b0 → ⊥
  bad7457  p = false≢true (sym (cong lower p))
  cut7457 : Adequate {ℓ} ((op (op (op (var 0) (op (var 1) (var 2))) (var 1)) (op (var 3) (var 3))) , (var 1)) → ⊥
  cut7457  adequate = bad7457  (Adequate.valid adequate Two boolean env5)
  bad7458 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b0 b0)) b0) (bop b1 b1)) b0 → ⊥
  bad7458  p = false≢true (sym (cong lower p))
  cut7458 : Adequate {ℓ} ((op (op (op (var 0) (op (var 1) (var 2))) (var 1)) (op (var 3) (var 3))) , (var 2)) → ⊥
  cut7458  adequate = bad7458  (Adequate.valid adequate Two boolean env5)
  bad7459 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b1 b0)) b1) (bop b0 b0)) b0 → ⊥
  bad7459  p = false≢true (sym (cong lower p))
  cut7459 : Adequate {ℓ} ((op (op (op (var 0) (op (var 1) (var 2))) (var 1)) (op (var 3) (var 3))) , (var 3)) → ⊥
  cut7459  adequate = bad7459  (Adequate.valid adequate Two boolean env19)
  bad7460 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b0 b0)) b0) (bop b0 b0)) b1 → ⊥
  bad7460  p = false≢true (cong lower p)
  cut7460 : Adequate {ℓ} ((op (op (op (var 0) (op (var 1) (var 2))) (var 1)) (op (var 3) (var 3))) , (var 4)) → ⊥
  cut7460  adequate = bad7460  (Adequate.valid adequate Two boolean env9)
  bad7461 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b0 b0)) b0) (bop b1 b1)) b0 → ⊥
  bad7461  p = false≢true (sym (cong lower p))
  cut7461 : Adequate {ℓ} ((op (op (op (var 0) (op (var 1) (var 2))) (var 1)) (op (var 3) (var 4))) , (var 0)) → ⊥
  cut7461  adequate = bad7461  (Adequate.valid adequate Two boolean env15)
  bad7462 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b0 b0)) b0) (bop b1 b1)) b0 → ⊥
  bad7462  p = false≢true (sym (cong lower p))
  cut7462 : Adequate {ℓ} ((op (op (op (var 0) (op (var 1) (var 2))) (var 1)) (op (var 3) (var 4))) , (var 1)) → ⊥
  cut7462  adequate = bad7462  (Adequate.valid adequate Two boolean env15)
  bad7463 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b0 b0)) b0) (bop b1 b1)) b0 → ⊥
  bad7463  p = false≢true (sym (cong lower p))
  cut7463 : Adequate {ℓ} ((op (op (op (var 0) (op (var 1) (var 2))) (var 1)) (op (var 3) (var 4))) , (var 2)) → ⊥
  cut7463  adequate = bad7463  (Adequate.valid adequate Two boolean env15)
  bad7464 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b0 b0)) b0) (bop b1 b0)) b1 → ⊥
  bad7464  p = false≢true (cong lower p)
  cut7464 : Adequate {ℓ} ((op (op (op (var 0) (op (var 1) (var 2))) (var 1)) (op (var 3) (var 4))) , (var 3)) → ⊥
  cut7464  adequate = bad7464  (Adequate.valid adequate Two boolean env16)
  bad7465 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b0 b0)) b0) (bop b0 b1)) b1 → ⊥
  bad7465  p = false≢true (cong lower p)
  cut7465 : Adequate {ℓ} ((op (op (op (var 0) (op (var 1) (var 2))) (var 1)) (op (var 3) (var 4))) , (var 4)) → ⊥
  cut7465  adequate = bad7465  (Adequate.valid adequate Two boolean env9)
  bad7466 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b0 b0)) b0) (bop b0 b0)) b1 → ⊥
  bad7466  p = false≢true (cong lower p)
  cut7466 : Adequate {ℓ} ((op (op (op (var 0) (op (var 1) (var 2))) (var 1)) (op (var 3) (var 4))) , (var 5)) → ⊥
  cut7466  adequate = bad7466  (Adequate.valid adequate Two boolean env17)
  bad7467 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b0 b1)) b1) (bop b0 b0)) b0 → ⊥
  bad7467  p = false≢true (sym (cong lower p))
  cut7467 : Adequate {ℓ} ((op (op (op (var 0) (op (var 1) (var 2))) (var 2)) (op (var 0) (var 0))) , (var 0)) → ⊥
  cut7467  adequate = bad7467  (Adequate.valid adequate Two boolean env1)
  bad7468 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b0 b1)) b1) (bop b0 b0)) b0 → ⊥
  bad7468  p = false≢true (sym (cong lower p))
  cut7468 : Adequate {ℓ} ((op (op (op (var 0) (op (var 1) (var 2))) (var 2)) (op (var 0) (var 0))) , (var 1)) → ⊥
  cut7468  adequate = bad7468  (Adequate.valid adequate Two boolean env1)
  bad7469 : PathP (λ _ → Two) (bop (bop (bop b1 (bop b0 b0)) b0) (bop b1 b1)) b0 → ⊥
  bad7469  p = false≢true (sym (cong lower p))
  cut7469 : Adequate {ℓ} ((op (op (op (var 0) (op (var 1) (var 2))) (var 2)) (op (var 0) (var 0))) , (var 2)) → ⊥
  cut7469  adequate = bad7469  (Adequate.valid adequate Two boolean env10)
  bad7470 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b0 b0)) b0) (bop b0 b0)) b1 → ⊥
  bad7470  p = false≢true (cong lower p)
  cut7470 : Adequate {ℓ} ((op (op (op (var 0) (op (var 1) (var 2))) (var 2)) (op (var 0) (var 0))) , (var 3)) → ⊥
  cut7470  adequate = bad7470  (Adequate.valid adequate Two boolean env5)
  bad7471 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b0 b1)) b1) (bop b0 b0)) b0 → ⊥
  bad7471  p = false≢true (sym (cong lower p))
  cut7471 : Adequate {ℓ} ((op (op (op (var 0) (op (var 1) (var 2))) (var 2)) (op (var 0) (var 1))) , (var 0)) → ⊥
  cut7471  adequate = bad7471  (Adequate.valid adequate Two boolean env1)
  bad7472 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b0 b1)) b1) (bop b0 b0)) b0 → ⊥
  bad7472  p = false≢true (sym (cong lower p))
  cut7472 : Adequate {ℓ} ((op (op (op (var 0) (op (var 1) (var 2))) (var 2)) (op (var 0) (var 1))) , (var 1)) → ⊥
  cut7472  adequate = bad7472  (Adequate.valid adequate Two boolean env1)
  bad7473 : PathP (λ _ → Two) (bop (bop (bop b1 (bop b0 b1)) b1) (bop b1 b0)) b1 → ⊥
  bad7473  p = false≢true (cong lower p)
  cut7473 : Adequate {ℓ} ((op (op (op (var 0) (op (var 1) (var 2))) (var 2)) (op (var 0) (var 1))) , (var 2)) → ⊥
  cut7473  adequate = bad7473  (Adequate.valid adequate Two boolean env6)
  bad7474 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b0 b0)) b0) (bop b0 b0)) b1 → ⊥
  bad7474  p = false≢true (cong lower p)
  cut7474 : Adequate {ℓ} ((op (op (op (var 0) (op (var 1) (var 2))) (var 2)) (op (var 0) (var 1))) , (var 3)) → ⊥
  cut7474  adequate = bad7474  (Adequate.valid adequate Two boolean env5)
  bad7475 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b0 b1)) b1) (bop b0 b1)) b0 → ⊥
  bad7475  p = false≢true (sym (cong lower p))
  cut7475 : Adequate {ℓ} ((op (op (op (var 0) (op (var 1) (var 2))) (var 2)) (op (var 0) (var 2))) , (var 0)) → ⊥
  cut7475  adequate = bad7475  (Adequate.valid adequate Two boolean env1)
  bad7476 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b0 b1)) b1) (bop b0 b1)) b0 → ⊥
  bad7476  p = false≢true (sym (cong lower p))
  cut7476 : Adequate {ℓ} ((op (op (op (var 0) (op (var 1) (var 2))) (var 2)) (op (var 0) (var 2))) , (var 1)) → ⊥
  cut7476  adequate = bad7476  (Adequate.valid adequate Two boolean env1)
  holds7477 : (z0 z1 z2 : A3) → (mul3 (mul3 (mul3 z0 (mul3 z1 z2)) z2) (mul3 z0 z2)) ≡ z2
  holds7477 z0 z1 z2 = refl
  cut7477 : Adequate {ℓ} ((op (op (op (var 0) (op (var 1) (var 2))) (var 2)) (op (var 0) (var 2))) , (var 2)) → ⊥
  cut7477  = reject3 ((op (op (op (var 0) (op (var 1) (var 2))) (var 2)) (op (var 0) (var 2))) , (var 2)) (λ env → holds7477 (env 0) (env 1) (env 2))
  bad7478 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b0 b0)) b0) (bop b0 b0)) b1 → ⊥
  bad7478  p = false≢true (cong lower p)
  cut7478 : Adequate {ℓ} ((op (op (op (var 0) (op (var 1) (var 2))) (var 2)) (op (var 0) (var 2))) , (var 3)) → ⊥
  cut7478  adequate = bad7478  (Adequate.valid adequate Two boolean env5)
  bad7479 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b0 b1)) b1) (bop b0 b0)) b0 → ⊥
  bad7479  p = false≢true (sym (cong lower p))
  cut7479 : Adequate {ℓ} ((op (op (op (var 0) (op (var 1) (var 2))) (var 2)) (op (var 0) (var 3))) , (var 0)) → ⊥
  cut7479  adequate = bad7479  (Adequate.valid adequate Two boolean env8)
  bad7480 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b0 b1)) b1) (bop b0 b0)) b0 → ⊥
  bad7480  p = false≢true (sym (cong lower p))
  cut7480 : Adequate {ℓ} ((op (op (op (var 0) (op (var 1) (var 2))) (var 2)) (op (var 0) (var 3))) , (var 1)) → ⊥
  cut7480  adequate = bad7480  (Adequate.valid adequate Two boolean env8)
  bad7481 : PathP (λ _ → Two) (bop (bop (bop b1 (bop b0 b0)) b0) (bop b1 b1)) b0 → ⊥
  bad7481  p = false≢true (sym (cong lower p))
  cut7481 : Adequate {ℓ} ((op (op (op (var 0) (op (var 1) (var 2))) (var 2)) (op (var 0) (var 3))) , (var 2)) → ⊥
  cut7481  adequate = bad7481  (Adequate.valid adequate Two boolean env12)
  bad7482 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b0 b0)) b0) (bop b0 b1)) b1 → ⊥
  bad7482  p = false≢true (cong lower p)
  cut7482 : Adequate {ℓ} ((op (op (op (var 0) (op (var 1) (var 2))) (var 2)) (op (var 0) (var 3))) , (var 3)) → ⊥
  cut7482  adequate = bad7482  (Adequate.valid adequate Two boolean env5)
  bad7483 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b0 b0)) b0) (bop b0 b0)) b1 → ⊥
  bad7483  p = false≢true (cong lower p)
  cut7483 : Adequate {ℓ} ((op (op (op (var 0) (op (var 1) (var 2))) (var 2)) (op (var 0) (var 3))) , (var 4)) → ⊥
  cut7483  adequate = bad7483  (Adequate.valid adequate Two boolean env9)
  bad7484 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b0 b1)) b1) (bop b0 b0)) b0 → ⊥
  bad7484  p = false≢true (sym (cong lower p))
  cut7484 : Adequate {ℓ} ((op (op (op (var 0) (op (var 1) (var 2))) (var 2)) (op (var 1) (var 0))) , (var 0)) → ⊥
  cut7484  adequate = bad7484  (Adequate.valid adequate Two boolean env1)
  bad7485 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b0 b1)) b1) (bop b0 b0)) b0 → ⊥
  bad7485  p = false≢true (sym (cong lower p))
  cut7485 : Adequate {ℓ} ((op (op (op (var 0) (op (var 1) (var 2))) (var 2)) (op (var 1) (var 0))) , (var 1)) → ⊥
  cut7485  adequate = bad7485  (Adequate.valid adequate Two boolean env1)
  bad7486 : PathP (λ _ → Two) (bop (bop (bop b1 (bop b0 b1)) b1) (bop b0 b1)) b1 → ⊥
  bad7486  p = false≢true (cong lower p)
  cut7486 : Adequate {ℓ} ((op (op (op (var 0) (op (var 1) (var 2))) (var 2)) (op (var 1) (var 0))) , (var 2)) → ⊥
  cut7486  adequate = bad7486  (Adequate.valid adequate Two boolean env6)
  bad7487 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b0 b0)) b0) (bop b0 b0)) b1 → ⊥
  bad7487  p = false≢true (cong lower p)
  cut7487 : Adequate {ℓ} ((op (op (op (var 0) (op (var 1) (var 2))) (var 2)) (op (var 1) (var 0))) , (var 3)) → ⊥
  cut7487  adequate = bad7487  (Adequate.valid adequate Two boolean env5)
  bad7488 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b0 b1)) b1) (bop b0 b0)) b0 → ⊥
  bad7488  p = false≢true (sym (cong lower p))
  cut7488 : Adequate {ℓ} ((op (op (op (var 0) (op (var 1) (var 2))) (var 2)) (op (var 1) (var 1))) , (var 0)) → ⊥
  cut7488  adequate = bad7488  (Adequate.valid adequate Two boolean env1)
  bad7489 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b0 b1)) b1) (bop b0 b0)) b0 → ⊥
  bad7489  p = false≢true (sym (cong lower p))
  cut7489 : Adequate {ℓ} ((op (op (op (var 0) (op (var 1) (var 2))) (var 2)) (op (var 1) (var 1))) , (var 1)) → ⊥
  cut7489  adequate = bad7489  (Adequate.valid adequate Two boolean env1)
  bad7490 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b1 b0)) b0) (bop b1 b1)) b0 → ⊥
  bad7490  p = false≢true (sym (cong lower p))
  cut7490 : Adequate {ℓ} ((op (op (op (var 0) (op (var 1) (var 2))) (var 2)) (op (var 1) (var 1))) , (var 2)) → ⊥
  cut7490  adequate = bad7490  (Adequate.valid adequate Two boolean env4)
  bad7491 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b0 b0)) b0) (bop b0 b0)) b1 → ⊥
  bad7491  p = false≢true (cong lower p)
  cut7491 : Adequate {ℓ} ((op (op (op (var 0) (op (var 1) (var 2))) (var 2)) (op (var 1) (var 1))) , (var 3)) → ⊥
  cut7491  adequate = bad7491  (Adequate.valid adequate Two boolean env5)
  bad7492 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b0 b1)) b1) (bop b0 b1)) b0 → ⊥
  bad7492  p = false≢true (sym (cong lower p))
  cut7492 : Adequate {ℓ} ((op (op (op (var 0) (op (var 1) (var 2))) (var 2)) (op (var 1) (var 2))) , (var 0)) → ⊥
  cut7492  adequate = bad7492  (Adequate.valid adequate Two boolean env1)
  bad7493 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b0 b1)) b1) (bop b0 b1)) b0 → ⊥
  bad7493  p = false≢true (sym (cong lower p))
  cut7493 : Adequate {ℓ} ((op (op (op (var 0) (op (var 1) (var 2))) (var 2)) (op (var 1) (var 2))) , (var 1)) → ⊥
  cut7493  adequate = bad7493  (Adequate.valid adequate Two boolean env1)
  bad7494 : PathP (λ _ → Two) (bop (bop (bop b1 (bop b0 b1)) b1) (bop b0 b1)) b1 → ⊥
  bad7494  p = false≢true (cong lower p)
  cut7494 : Adequate {ℓ} ((op (op (op (var 0) (op (var 1) (var 2))) (var 2)) (op (var 1) (var 2))) , (var 2)) → ⊥
  cut7494  adequate = bad7494  (Adequate.valid adequate Two boolean env6)
  bad7495 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b0 b0)) b0) (bop b0 b0)) b1 → ⊥
  bad7495  p = false≢true (cong lower p)
  cut7495 : Adequate {ℓ} ((op (op (op (var 0) (op (var 1) (var 2))) (var 2)) (op (var 1) (var 2))) , (var 3)) → ⊥
  cut7495  adequate = bad7495  (Adequate.valid adequate Two boolean env5)
  bad7496 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b0 b1)) b1) (bop b0 b0)) b0 → ⊥
  bad7496  p = false≢true (sym (cong lower p))
  cut7496 : Adequate {ℓ} ((op (op (op (var 0) (op (var 1) (var 2))) (var 2)) (op (var 1) (var 3))) , (var 0)) → ⊥
  cut7496  adequate = bad7496  (Adequate.valid adequate Two boolean env8)
  bad7497 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b0 b1)) b1) (bop b0 b0)) b0 → ⊥
  bad7497  p = false≢true (sym (cong lower p))
  cut7497 : Adequate {ℓ} ((op (op (op (var 0) (op (var 1) (var 2))) (var 2)) (op (var 1) (var 3))) , (var 1)) → ⊥
  cut7497  adequate = bad7497  (Adequate.valid adequate Two boolean env8)
  bad7498 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b1 b0)) b0) (bop b1 b1)) b0 → ⊥
  bad7498  p = false≢true (sym (cong lower p))
  cut7498 : Adequate {ℓ} ((op (op (op (var 0) (op (var 1) (var 2))) (var 2)) (op (var 1) (var 3))) , (var 2)) → ⊥
  cut7498  adequate = bad7498  (Adequate.valid adequate Two boolean env13)
  bad7499 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b0 b0)) b0) (bop b0 b1)) b1 → ⊥
  bad7499  p = false≢true (cong lower p)
  cut7499 : Adequate {ℓ} ((op (op (op (var 0) (op (var 1) (var 2))) (var 2)) (op (var 1) (var 3))) , (var 3)) → ⊥
  cut7499  adequate = bad7499  (Adequate.valid adequate Two boolean env5)
  bad7500 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b0 b0)) b0) (bop b0 b0)) b1 → ⊥
  bad7500  p = false≢true (cong lower p)
  cut7500 : Adequate {ℓ} ((op (op (op (var 0) (op (var 1) (var 2))) (var 2)) (op (var 1) (var 3))) , (var 4)) → ⊥
  cut7500  adequate = bad7500  (Adequate.valid adequate Two boolean env9)
  bad7501 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b0 b1)) b1) (bop b1 b0)) b0 → ⊥
  bad7501  p = false≢true (sym (cong lower p))
  cut7501 : Adequate {ℓ} ((op (op (op (var 0) (op (var 1) (var 2))) (var 2)) (op (var 2) (var 0))) , (var 0)) → ⊥
  cut7501  adequate = bad7501  (Adequate.valid adequate Two boolean env1)
  bad7502 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b0 b1)) b1) (bop b1 b0)) b0 → ⊥
  bad7502  p = false≢true (sym (cong lower p))
  cut7502 : Adequate {ℓ} ((op (op (op (var 0) (op (var 1) (var 2))) (var 2)) (op (var 2) (var 0))) , (var 1)) → ⊥
  cut7502  adequate = bad7502  (Adequate.valid adequate Two boolean env1)
  holds7503 : (z0 z1 z2 : A13) → (mul13 (mul13 (mul13 z0 (mul13 z1 z2)) z2) (mul13 z2 z0)) ≡ z2
  holds7503 m13c0 m13c0 m13c0 = refl
  holds7503 m13c0 m13c0 m13c1 = refl
  holds7503 m13c0 m13c0 m13c2 = refl
  holds7503 m13c0 m13c0 m13c3 = refl
  holds7503 m13c0 m13c1 m13c0 = refl
  holds7503 m13c0 m13c1 m13c1 = refl
  holds7503 m13c0 m13c1 m13c2 = refl
  holds7503 m13c0 m13c1 m13c3 = refl
  holds7503 m13c0 m13c2 m13c0 = refl
  holds7503 m13c0 m13c2 m13c1 = refl
  holds7503 m13c0 m13c2 m13c2 = refl
  holds7503 m13c0 m13c2 m13c3 = refl
  holds7503 m13c0 m13c3 m13c0 = refl
  holds7503 m13c0 m13c3 m13c1 = refl
  holds7503 m13c0 m13c3 m13c2 = refl
  holds7503 m13c0 m13c3 m13c3 = refl
  holds7503 m13c1 m13c0 m13c0 = refl
  holds7503 m13c1 m13c0 m13c1 = refl
  holds7503 m13c1 m13c0 m13c2 = refl
  holds7503 m13c1 m13c0 m13c3 = refl
  holds7503 m13c1 m13c1 m13c0 = refl
  holds7503 m13c1 m13c1 m13c1 = refl
  holds7503 m13c1 m13c1 m13c2 = refl
  holds7503 m13c1 m13c1 m13c3 = refl
  holds7503 m13c1 m13c2 m13c0 = refl
  holds7503 m13c1 m13c2 m13c1 = refl
  holds7503 m13c1 m13c2 m13c2 = refl
  holds7503 m13c1 m13c2 m13c3 = refl
  holds7503 m13c1 m13c3 m13c0 = refl
  holds7503 m13c1 m13c3 m13c1 = refl
  holds7503 m13c1 m13c3 m13c2 = refl
  holds7503 m13c1 m13c3 m13c3 = refl
  holds7503 m13c2 m13c0 m13c0 = refl
  holds7503 m13c2 m13c0 m13c1 = refl
  holds7503 m13c2 m13c0 m13c2 = refl
  holds7503 m13c2 m13c0 m13c3 = refl
  holds7503 m13c2 m13c1 m13c0 = refl
  holds7503 m13c2 m13c1 m13c1 = refl
  holds7503 m13c2 m13c1 m13c2 = refl
  holds7503 m13c2 m13c1 m13c3 = refl
  holds7503 m13c2 m13c2 m13c0 = refl
  holds7503 m13c2 m13c2 m13c1 = refl
  holds7503 m13c2 m13c2 m13c2 = refl
  holds7503 m13c2 m13c2 m13c3 = refl
  holds7503 m13c2 m13c3 m13c0 = refl
  holds7503 m13c2 m13c3 m13c1 = refl
  holds7503 m13c2 m13c3 m13c2 = refl
  holds7503 m13c2 m13c3 m13c3 = refl
  holds7503 m13c3 m13c0 m13c0 = refl
  holds7503 m13c3 m13c0 m13c1 = refl
  holds7503 m13c3 m13c0 m13c2 = refl
  holds7503 m13c3 m13c0 m13c3 = refl
  holds7503 m13c3 m13c1 m13c0 = refl
  holds7503 m13c3 m13c1 m13c1 = refl
  holds7503 m13c3 m13c1 m13c2 = refl
  holds7503 m13c3 m13c1 m13c3 = refl
  holds7503 m13c3 m13c2 m13c0 = refl
  holds7503 m13c3 m13c2 m13c1 = refl
  holds7503 m13c3 m13c2 m13c2 = refl
  holds7503 m13c3 m13c2 m13c3 = refl
  holds7503 m13c3 m13c3 m13c0 = refl
  holds7503 m13c3 m13c3 m13c1 = refl
  holds7503 m13c3 m13c3 m13c2 = refl
  holds7503 m13c3 m13c3 m13c3 = refl
  cut7503 : Adequate {ℓ} ((op (op (op (var 0) (op (var 1) (var 2))) (var 2)) (op (var 2) (var 0))) , (var 2)) → ⊥
  cut7503  = reject13 ((op (op (op (var 0) (op (var 1) (var 2))) (var 2)) (op (var 2) (var 0))) , (var 2)) (λ env → holds7503 (env 0) (env 1) (env 2))
  bad7504 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b0 b0)) b0) (bop b0 b0)) b1 → ⊥
  bad7504  p = false≢true (cong lower p)
  cut7504 : Adequate {ℓ} ((op (op (op (var 0) (op (var 1) (var 2))) (var 2)) (op (var 2) (var 0))) , (var 3)) → ⊥
  cut7504  adequate = bad7504  (Adequate.valid adequate Two boolean env5)
  bad7505 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b0 b1)) b1) (bop b1 b0)) b0 → ⊥
  bad7505  p = false≢true (sym (cong lower p))
  cut7505 : Adequate {ℓ} ((op (op (op (var 0) (op (var 1) (var 2))) (var 2)) (op (var 2) (var 1))) , (var 0)) → ⊥
  cut7505  adequate = bad7505  (Adequate.valid adequate Two boolean env1)
  bad7506 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b0 b1)) b1) (bop b1 b0)) b0 → ⊥
  bad7506  p = false≢true (sym (cong lower p))
  cut7506 : Adequate {ℓ} ((op (op (op (var 0) (op (var 1) (var 2))) (var 2)) (op (var 2) (var 1))) , (var 1)) → ⊥
  cut7506  adequate = bad7506  (Adequate.valid adequate Two boolean env1)
  bad7507 : PathP (λ _ → Two) (bop (bop (bop b1 (bop b0 b1)) b1) (bop b1 b0)) b1 → ⊥
  bad7507  p = false≢true (cong lower p)
  cut7507 : Adequate {ℓ} ((op (op (op (var 0) (op (var 1) (var 2))) (var 2)) (op (var 2) (var 1))) , (var 2)) → ⊥
  cut7507  adequate = bad7507  (Adequate.valid adequate Two boolean env6)
  bad7508 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b0 b0)) b0) (bop b0 b0)) b1 → ⊥
  bad7508  p = false≢true (cong lower p)
  cut7508 : Adequate {ℓ} ((op (op (op (var 0) (op (var 1) (var 2))) (var 2)) (op (var 2) (var 1))) , (var 3)) → ⊥
  cut7508  adequate = bad7508  (Adequate.valid adequate Two boolean env5)
  bad7509 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b0 b1)) b1) (bop b1 b1)) b0 → ⊥
  bad7509  p = false≢true (sym (cong lower p))
  cut7509 : Adequate {ℓ} ((op (op (op (var 0) (op (var 1) (var 2))) (var 2)) (op (var 2) (var 2))) , (var 0)) → ⊥
  cut7509  adequate = bad7509  (Adequate.valid adequate Two boolean env1)
  bad7510 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b0 b1)) b1) (bop b1 b1)) b0 → ⊥
  bad7510  p = false≢true (sym (cong lower p))
  cut7510 : Adequate {ℓ} ((op (op (op (var 0) (op (var 1) (var 2))) (var 2)) (op (var 2) (var 2))) , (var 1)) → ⊥
  cut7510  adequate = bad7510  (Adequate.valid adequate Two boolean env1)
  holds7511 : (z0 z1 z2 : A3) → (mul3 (mul3 (mul3 z0 (mul3 z1 z2)) z2) (mul3 z2 z2)) ≡ z2
  holds7511 z0 z1 z2 = refl
  cut7511 : Adequate {ℓ} ((op (op (op (var 0) (op (var 1) (var 2))) (var 2)) (op (var 2) (var 2))) , (var 2)) → ⊥
  cut7511  = reject3 ((op (op (op (var 0) (op (var 1) (var 2))) (var 2)) (op (var 2) (var 2))) , (var 2)) (λ env → holds7511 (env 0) (env 1) (env 2))
  bad7512 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b0 b0)) b0) (bop b0 b0)) b1 → ⊥
  bad7512  p = false≢true (cong lower p)
  cut7512 : Adequate {ℓ} ((op (op (op (var 0) (op (var 1) (var 2))) (var 2)) (op (var 2) (var 2))) , (var 3)) → ⊥
  cut7512  adequate = bad7512  (Adequate.valid adequate Two boolean env5)
  bad7513 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b0 b1)) b1) (bop b1 b0)) b0 → ⊥
  bad7513  p = false≢true (sym (cong lower p))
  cut7513 : Adequate {ℓ} ((op (op (op (var 0) (op (var 1) (var 2))) (var 2)) (op (var 2) (var 3))) , (var 0)) → ⊥
  cut7513  adequate = bad7513  (Adequate.valid adequate Two boolean env8)
  bad7514 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b0 b1)) b1) (bop b1 b0)) b0 → ⊥
  bad7514  p = false≢true (sym (cong lower p))
  cut7514 : Adequate {ℓ} ((op (op (op (var 0) (op (var 1) (var 2))) (var 2)) (op (var 2) (var 3))) , (var 1)) → ⊥
  cut7514  adequate = bad7514  (Adequate.valid adequate Two boolean env8)
  bad7515 : PathP (λ _ → Two) (bop (bop (bop b1 (bop b0 b1)) b1) (bop b1 b0)) b1 → ⊥
  bad7515  p = false≢true (cong lower p)
  cut7515 : Adequate {ℓ} ((op (op (op (var 0) (op (var 1) (var 2))) (var 2)) (op (var 2) (var 3))) , (var 2)) → ⊥
  cut7515  adequate = bad7515  (Adequate.valid adequate Two boolean env14)
  bad7516 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b0 b0)) b0) (bop b0 b1)) b1 → ⊥
  bad7516  p = false≢true (cong lower p)
  cut7516 : Adequate {ℓ} ((op (op (op (var 0) (op (var 1) (var 2))) (var 2)) (op (var 2) (var 3))) , (var 3)) → ⊥
  cut7516  adequate = bad7516  (Adequate.valid adequate Two boolean env5)
  bad7517 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b0 b0)) b0) (bop b0 b0)) b1 → ⊥
  bad7517  p = false≢true (cong lower p)
  cut7517 : Adequate {ℓ} ((op (op (op (var 0) (op (var 1) (var 2))) (var 2)) (op (var 2) (var 3))) , (var 4)) → ⊥
  cut7517  adequate = bad7517  (Adequate.valid adequate Two boolean env9)
  bad7518 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b0 b1)) b1) (bop b0 b0)) b0 → ⊥
  bad7518  p = false≢true (sym (cong lower p))
  cut7518 : Adequate {ℓ} ((op (op (op (var 0) (op (var 1) (var 2))) (var 2)) (op (var 3) (var 0))) , (var 0)) → ⊥
  cut7518  adequate = bad7518  (Adequate.valid adequate Two boolean env8)
  bad7519 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b0 b1)) b1) (bop b0 b0)) b0 → ⊥
  bad7519  p = false≢true (sym (cong lower p))
  cut7519 : Adequate {ℓ} ((op (op (op (var 0) (op (var 1) (var 2))) (var 2)) (op (var 3) (var 0))) , (var 1)) → ⊥
  cut7519  adequate = bad7519  (Adequate.valid adequate Two boolean env8)
  bad7520 : PathP (λ _ → Two) (bop (bop (bop b1 (bop b0 b0)) b0) (bop b1 b1)) b0 → ⊥
  bad7520  p = false≢true (sym (cong lower p))
  cut7520 : Adequate {ℓ} ((op (op (op (var 0) (op (var 1) (var 2))) (var 2)) (op (var 3) (var 0))) , (var 2)) → ⊥
  cut7520  adequate = bad7520  (Adequate.valid adequate Two boolean env12)
  bad7521 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b0 b0)) b0) (bop b1 b0)) b1 → ⊥
  bad7521  p = false≢true (cong lower p)
  cut7521 : Adequate {ℓ} ((op (op (op (var 0) (op (var 1) (var 2))) (var 2)) (op (var 3) (var 0))) , (var 3)) → ⊥
  cut7521  adequate = bad7521  (Adequate.valid adequate Two boolean env5)
  bad7522 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b0 b0)) b0) (bop b0 b0)) b1 → ⊥
  bad7522  p = false≢true (cong lower p)
  cut7522 : Adequate {ℓ} ((op (op (op (var 0) (op (var 1) (var 2))) (var 2)) (op (var 3) (var 0))) , (var 4)) → ⊥
  cut7522  adequate = bad7522  (Adequate.valid adequate Two boolean env9)
  bad7523 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b0 b1)) b1) (bop b0 b0)) b0 → ⊥
  bad7523  p = false≢true (sym (cong lower p))
  cut7523 : Adequate {ℓ} ((op (op (op (var 0) (op (var 1) (var 2))) (var 2)) (op (var 3) (var 1))) , (var 0)) → ⊥
  cut7523  adequate = bad7523  (Adequate.valid adequate Two boolean env8)
  bad7524 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b0 b1)) b1) (bop b0 b0)) b0 → ⊥
  bad7524  p = false≢true (sym (cong lower p))
  cut7524 : Adequate {ℓ} ((op (op (op (var 0) (op (var 1) (var 2))) (var 2)) (op (var 3) (var 1))) , (var 1)) → ⊥
  cut7524  adequate = bad7524  (Adequate.valid adequate Two boolean env8)
  bad7525 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b1 b0)) b0) (bop b1 b1)) b0 → ⊥
  bad7525  p = false≢true (sym (cong lower p))
  cut7525 : Adequate {ℓ} ((op (op (op (var 0) (op (var 1) (var 2))) (var 2)) (op (var 3) (var 1))) , (var 2)) → ⊥
  cut7525  adequate = bad7525  (Adequate.valid adequate Two boolean env13)
  bad7526 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b0 b0)) b0) (bop b1 b0)) b1 → ⊥
  bad7526  p = false≢true (cong lower p)
  cut7526 : Adequate {ℓ} ((op (op (op (var 0) (op (var 1) (var 2))) (var 2)) (op (var 3) (var 1))) , (var 3)) → ⊥
  cut7526  adequate = bad7526  (Adequate.valid adequate Two boolean env5)
  bad7527 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b0 b0)) b0) (bop b0 b0)) b1 → ⊥
  bad7527  p = false≢true (cong lower p)
  cut7527 : Adequate {ℓ} ((op (op (op (var 0) (op (var 1) (var 2))) (var 2)) (op (var 3) (var 1))) , (var 4)) → ⊥
  cut7527  adequate = bad7527  (Adequate.valid adequate Two boolean env9)
  bad7528 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b0 b1)) b1) (bop b0 b1)) b0 → ⊥
  bad7528  p = false≢true (sym (cong lower p))
  cut7528 : Adequate {ℓ} ((op (op (op (var 0) (op (var 1) (var 2))) (var 2)) (op (var 3) (var 2))) , (var 0)) → ⊥
  cut7528  adequate = bad7528  (Adequate.valid adequate Two boolean env8)
  bad7529 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b0 b1)) b1) (bop b0 b1)) b0 → ⊥
  bad7529  p = false≢true (sym (cong lower p))
  cut7529 : Adequate {ℓ} ((op (op (op (var 0) (op (var 1) (var 2))) (var 2)) (op (var 3) (var 2))) , (var 1)) → ⊥
  cut7529  adequate = bad7529  (Adequate.valid adequate Two boolean env8)
  bad7530 : PathP (λ _ → Two) (bop (bop (bop b1 (bop b0 b1)) b1) (bop b0 b1)) b1 → ⊥
  bad7530  p = false≢true (cong lower p)
  cut7530 : Adequate {ℓ} ((op (op (op (var 0) (op (var 1) (var 2))) (var 2)) (op (var 3) (var 2))) , (var 2)) → ⊥
  cut7530  adequate = bad7530  (Adequate.valid adequate Two boolean env14)
  bad7531 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b0 b0)) b0) (bop b1 b0)) b1 → ⊥
  bad7531  p = false≢true (cong lower p)
  cut7531 : Adequate {ℓ} ((op (op (op (var 0) (op (var 1) (var 2))) (var 2)) (op (var 3) (var 2))) , (var 3)) → ⊥
  cut7531  adequate = bad7531  (Adequate.valid adequate Two boolean env5)
  bad7532 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b0 b0)) b0) (bop b0 b0)) b1 → ⊥
  bad7532  p = false≢true (cong lower p)
  cut7532 : Adequate {ℓ} ((op (op (op (var 0) (op (var 1) (var 2))) (var 2)) (op (var 3) (var 2))) , (var 4)) → ⊥
  cut7532  adequate = bad7532  (Adequate.valid adequate Two boolean env9)
  bad7533 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b0 b0)) b0) (bop b1 b1)) b0 → ⊥
  bad7533  p = false≢true (sym (cong lower p))
  cut7533 : Adequate {ℓ} ((op (op (op (var 0) (op (var 1) (var 2))) (var 2)) (op (var 3) (var 3))) , (var 0)) → ⊥
  cut7533  adequate = bad7533  (Adequate.valid adequate Two boolean env5)
  bad7534 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b0 b0)) b0) (bop b1 b1)) b0 → ⊥
  bad7534  p = false≢true (sym (cong lower p))
  cut7534 : Adequate {ℓ} ((op (op (op (var 0) (op (var 1) (var 2))) (var 2)) (op (var 3) (var 3))) , (var 1)) → ⊥
  cut7534  adequate = bad7534  (Adequate.valid adequate Two boolean env5)
  bad7535 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b0 b0)) b0) (bop b1 b1)) b0 → ⊥
  bad7535  p = false≢true (sym (cong lower p))
  cut7535 : Adequate {ℓ} ((op (op (op (var 0) (op (var 1) (var 2))) (var 2)) (op (var 3) (var 3))) , (var 2)) → ⊥
  cut7535  adequate = bad7535  (Adequate.valid adequate Two boolean env5)
  bad7536 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b0 b1)) b1) (bop b0 b0)) b0 → ⊥
  bad7536  p = false≢true (sym (cong lower p))
  cut7536 : Adequate {ℓ} ((op (op (op (var 0) (op (var 1) (var 2))) (var 2)) (op (var 3) (var 3))) , (var 3)) → ⊥
  cut7536  adequate = bad7536  (Adequate.valid adequate Two boolean env8)
  bad7537 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b0 b0)) b0) (bop b0 b0)) b1 → ⊥
  bad7537  p = false≢true (cong lower p)
  cut7537 : Adequate {ℓ} ((op (op (op (var 0) (op (var 1) (var 2))) (var 2)) (op (var 3) (var 3))) , (var 4)) → ⊥
  cut7537  adequate = bad7537  (Adequate.valid adequate Two boolean env9)
  bad7538 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b0 b0)) b0) (bop b1 b1)) b0 → ⊥
  bad7538  p = false≢true (sym (cong lower p))
  cut7538 : Adequate {ℓ} ((op (op (op (var 0) (op (var 1) (var 2))) (var 2)) (op (var 3) (var 4))) , (var 0)) → ⊥
  cut7538  adequate = bad7538  (Adequate.valid adequate Two boolean env15)
  bad7539 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b0 b0)) b0) (bop b1 b1)) b0 → ⊥
  bad7539  p = false≢true (sym (cong lower p))
  cut7539 : Adequate {ℓ} ((op (op (op (var 0) (op (var 1) (var 2))) (var 2)) (op (var 3) (var 4))) , (var 1)) → ⊥
  cut7539  adequate = bad7539  (Adequate.valid adequate Two boolean env15)
  bad7540 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b0 b0)) b0) (bop b1 b1)) b0 → ⊥
  bad7540  p = false≢true (sym (cong lower p))
  cut7540 : Adequate {ℓ} ((op (op (op (var 0) (op (var 1) (var 2))) (var 2)) (op (var 3) (var 4))) , (var 2)) → ⊥
  cut7540  adequate = bad7540  (Adequate.valid adequate Two boolean env15)
  bad7541 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b0 b0)) b0) (bop b1 b0)) b1 → ⊥
  bad7541  p = false≢true (cong lower p)
  cut7541 : Adequate {ℓ} ((op (op (op (var 0) (op (var 1) (var 2))) (var 2)) (op (var 3) (var 4))) , (var 3)) → ⊥
  cut7541  adequate = bad7541  (Adequate.valid adequate Two boolean env16)
  bad7542 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b0 b0)) b0) (bop b0 b1)) b1 → ⊥
  bad7542  p = false≢true (cong lower p)
  cut7542 : Adequate {ℓ} ((op (op (op (var 0) (op (var 1) (var 2))) (var 2)) (op (var 3) (var 4))) , (var 4)) → ⊥
  cut7542  adequate = bad7542  (Adequate.valid adequate Two boolean env9)
  bad7543 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b0 b0)) b0) (bop b0 b0)) b1 → ⊥
  bad7543  p = false≢true (cong lower p)
  cut7543 : Adequate {ℓ} ((op (op (op (var 0) (op (var 1) (var 2))) (var 2)) (op (var 3) (var 4))) , (var 5)) → ⊥
  cut7543  adequate = bad7543  (Adequate.valid adequate Two boolean env17)
  bad7544 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b0 b0)) b1) (bop b0 b0)) b0 → ⊥
  bad7544  p = false≢true (sym (cong lower p))
  cut7544 : Adequate {ℓ} ((op (op (op (var 0) (op (var 1) (var 2))) (var 3)) (op (var 0) (var 0))) , (var 0)) → ⊥
  cut7544  adequate = bad7544  (Adequate.valid adequate Two boolean env5)
  bad7545 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b0 b0)) b1) (bop b0 b0)) b0 → ⊥
  bad7545  p = false≢true (sym (cong lower p))
  cut7545 : Adequate {ℓ} ((op (op (op (var 0) (op (var 1) (var 2))) (var 3)) (op (var 0) (var 0))) , (var 1)) → ⊥
  cut7545  adequate = bad7545  (Adequate.valid adequate Two boolean env5)
  bad7546 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b0 b0)) b1) (bop b0 b0)) b0 → ⊥
  bad7546  p = false≢true (sym (cong lower p))
  cut7546 : Adequate {ℓ} ((op (op (op (var 0) (op (var 1) (var 2))) (var 3)) (op (var 0) (var 0))) , (var 2)) → ⊥
  cut7546  adequate = bad7546  (Adequate.valid adequate Two boolean env5)
  bad7547 : PathP (λ _ → Two) (bop (bop (bop b1 (bop b0 b0)) b0) (bop b1 b1)) b0 → ⊥
  bad7547  p = false≢true (sym (cong lower p))
  cut7547 : Adequate {ℓ} ((op (op (op (var 0) (op (var 1) (var 2))) (var 3)) (op (var 0) (var 0))) , (var 3)) → ⊥
  cut7547  adequate = bad7547  (Adequate.valid adequate Two boolean env18)
  bad7548 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b0 b0)) b0) (bop b0 b0)) b1 → ⊥
  bad7548  p = false≢true (cong lower p)
  cut7548 : Adequate {ℓ} ((op (op (op (var 0) (op (var 1) (var 2))) (var 3)) (op (var 0) (var 0))) , (var 4)) → ⊥
  cut7548  adequate = bad7548  (Adequate.valid adequate Two boolean env9)
  bad7549 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b0 b0)) b1) (bop b0 b0)) b0 → ⊥
  bad7549  p = false≢true (sym (cong lower p))
  cut7549 : Adequate {ℓ} ((op (op (op (var 0) (op (var 1) (var 2))) (var 3)) (op (var 0) (var 1))) , (var 0)) → ⊥
  cut7549  adequate = bad7549  (Adequate.valid adequate Two boolean env5)
  bad7550 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b0 b0)) b1) (bop b0 b0)) b0 → ⊥
  bad7550  p = false≢true (sym (cong lower p))
  cut7550 : Adequate {ℓ} ((op (op (op (var 0) (op (var 1) (var 2))) (var 3)) (op (var 0) (var 1))) , (var 1)) → ⊥
  cut7550  adequate = bad7550  (Adequate.valid adequate Two boolean env5)
  bad7551 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b0 b0)) b1) (bop b0 b0)) b0 → ⊥
  bad7551  p = false≢true (sym (cong lower p))
  cut7551 : Adequate {ℓ} ((op (op (op (var 0) (op (var 1) (var 2))) (var 3)) (op (var 0) (var 1))) , (var 2)) → ⊥
  cut7551  adequate = bad7551  (Adequate.valid adequate Two boolean env5)
  bad7552 : PathP (λ _ → Two) (bop (bop (bop b1 (bop b0 b0)) b1) (bop b1 b0)) b1 → ⊥
  bad7552  p = false≢true (cong lower p)
  cut7552 : Adequate {ℓ} ((op (op (op (var 0) (op (var 1) (var 2))) (var 3)) (op (var 0) (var 1))) , (var 3)) → ⊥
  cut7552  adequate = bad7552  (Adequate.valid adequate Two boolean env12)
  bad7553 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b0 b0)) b0) (bop b0 b0)) b1 → ⊥
  bad7553  p = false≢true (cong lower p)
  cut7553 : Adequate {ℓ} ((op (op (op (var 0) (op (var 1) (var 2))) (var 3)) (op (var 0) (var 1))) , (var 4)) → ⊥
  cut7553  adequate = bad7553  (Adequate.valid adequate Two boolean env9)
  bad7554 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b0 b0)) b1) (bop b0 b0)) b0 → ⊥
  bad7554  p = false≢true (sym (cong lower p))
  cut7554 : Adequate {ℓ} ((op (op (op (var 0) (op (var 1) (var 2))) (var 3)) (op (var 0) (var 2))) , (var 0)) → ⊥
  cut7554  adequate = bad7554  (Adequate.valid adequate Two boolean env5)
  bad7555 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b0 b0)) b1) (bop b0 b0)) b0 → ⊥
  bad7555  p = false≢true (sym (cong lower p))
  cut7555 : Adequate {ℓ} ((op (op (op (var 0) (op (var 1) (var 2))) (var 3)) (op (var 0) (var 2))) , (var 1)) → ⊥
  cut7555  adequate = bad7555  (Adequate.valid adequate Two boolean env5)
  bad7556 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b0 b0)) b1) (bop b0 b0)) b0 → ⊥
  bad7556  p = false≢true (sym (cong lower p))
  cut7556 : Adequate {ℓ} ((op (op (op (var 0) (op (var 1) (var 2))) (var 3)) (op (var 0) (var 2))) , (var 2)) → ⊥
  cut7556  adequate = bad7556  (Adequate.valid adequate Two boolean env5)
  bad7557 : PathP (λ _ → Two) (bop (bop (bop b1 (bop b0 b0)) b1) (bop b1 b0)) b1 → ⊥
  bad7557  p = false≢true (cong lower p)
  cut7557 : Adequate {ℓ} ((op (op (op (var 0) (op (var 1) (var 2))) (var 3)) (op (var 0) (var 2))) , (var 3)) → ⊥
  cut7557  adequate = bad7557  (Adequate.valid adequate Two boolean env12)
  bad7558 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b0 b0)) b0) (bop b0 b0)) b1 → ⊥
  bad7558  p = false≢true (cong lower p)
  cut7558 : Adequate {ℓ} ((op (op (op (var 0) (op (var 1) (var 2))) (var 3)) (op (var 0) (var 2))) , (var 4)) → ⊥
  cut7558  adequate = bad7558  (Adequate.valid adequate Two boolean env9)
  bad7559 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b0 b0)) b1) (bop b0 b1)) b0 → ⊥
  bad7559  p = false≢true (sym (cong lower p))
  cut7559 : Adequate {ℓ} ((op (op (op (var 0) (op (var 1) (var 2))) (var 3)) (op (var 0) (var 3))) , (var 0)) → ⊥
  cut7559  adequate = bad7559  (Adequate.valid adequate Two boolean env5)
  bad7560 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b0 b0)) b1) (bop b0 b1)) b0 → ⊥
  bad7560  p = false≢true (sym (cong lower p))
  cut7560 : Adequate {ℓ} ((op (op (op (var 0) (op (var 1) (var 2))) (var 3)) (op (var 0) (var 3))) , (var 1)) → ⊥
  cut7560  adequate = bad7560  (Adequate.valid adequate Two boolean env5)
  bad7561 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b0 b0)) b1) (bop b0 b1)) b0 → ⊥
  bad7561  p = false≢true (sym (cong lower p))
  cut7561 : Adequate {ℓ} ((op (op (op (var 0) (op (var 1) (var 2))) (var 3)) (op (var 0) (var 3))) , (var 2)) → ⊥
  cut7561  adequate = bad7561  (Adequate.valid adequate Two boolean env5)
  holds7562 : (z0 z1 z2 z3 : A3) → (mul3 (mul3 (mul3 z0 (mul3 z1 z2)) z3) (mul3 z0 z3)) ≡ z3
  holds7562 z0 z1 z2 z3 = refl
  cut7562 : Adequate {ℓ} ((op (op (op (var 0) (op (var 1) (var 2))) (var 3)) (op (var 0) (var 3))) , (var 3)) → ⊥
  cut7562  = reject3 ((op (op (op (var 0) (op (var 1) (var 2))) (var 3)) (op (var 0) (var 3))) , (var 3)) (λ env → holds7562 (env 0) (env 1) (env 2) (env 3))
  bad7563 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b0 b0)) b0) (bop b0 b0)) b1 → ⊥
  bad7563  p = false≢true (cong lower p)
  cut7563 : Adequate {ℓ} ((op (op (op (var 0) (op (var 1) (var 2))) (var 3)) (op (var 0) (var 3))) , (var 4)) → ⊥
  cut7563  adequate = bad7563  (Adequate.valid adequate Two boolean env9)
  bad7564 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b0 b0)) b1) (bop b0 b0)) b0 → ⊥
  bad7564  p = false≢true (sym (cong lower p))
  cut7564 : Adequate {ℓ} ((op (op (op (var 0) (op (var 1) (var 2))) (var 3)) (op (var 0) (var 4))) , (var 0)) → ⊥
  cut7564  adequate = bad7564  (Adequate.valid adequate Two boolean env16)
  bad7565 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b0 b0)) b1) (bop b0 b0)) b0 → ⊥
  bad7565  p = false≢true (sym (cong lower p))
  cut7565 : Adequate {ℓ} ((op (op (op (var 0) (op (var 1) (var 2))) (var 3)) (op (var 0) (var 4))) , (var 1)) → ⊥
  cut7565  adequate = bad7565  (Adequate.valid adequate Two boolean env16)
  bad7566 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b0 b0)) b1) (bop b0 b0)) b0 → ⊥
  bad7566  p = false≢true (sym (cong lower p))
  cut7566 : Adequate {ℓ} ((op (op (op (var 0) (op (var 1) (var 2))) (var 3)) (op (var 0) (var 4))) , (var 2)) → ⊥
  cut7566  adequate = bad7566  (Adequate.valid adequate Two boolean env16)
  env22 : ℕ → Two
  env22 zero = b1
  env22 (suc zero) = b0
  env22 (suc (suc zero)) = b0
  env22 (suc (suc (suc zero))) = b0
  env22 (suc (suc (suc (suc zero)))) = b1
  env22 (suc (suc (suc (suc (suc rest))))) = b0
  bad7567 : PathP (λ _ → Two) (bop (bop (bop b1 (bop b0 b0)) b0) (bop b1 b1)) b0 → ⊥
  bad7567  p = false≢true (sym (cong lower p))
  cut7567 : Adequate {ℓ} ((op (op (op (var 0) (op (var 1) (var 2))) (var 3)) (op (var 0) (var 4))) , (var 3)) → ⊥
  cut7567  adequate = bad7567  (Adequate.valid adequate Two boolean env22)
  bad7568 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b0 b0)) b0) (bop b0 b1)) b1 → ⊥
  bad7568  p = false≢true (cong lower p)
  cut7568 : Adequate {ℓ} ((op (op (op (var 0) (op (var 1) (var 2))) (var 3)) (op (var 0) (var 4))) , (var 4)) → ⊥
  cut7568  adequate = bad7568  (Adequate.valid adequate Two boolean env9)
  bad7569 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b0 b0)) b0) (bop b0 b0)) b1 → ⊥
  bad7569  p = false≢true (cong lower p)
  cut7569 : Adequate {ℓ} ((op (op (op (var 0) (op (var 1) (var 2))) (var 3)) (op (var 0) (var 4))) , (var 5)) → ⊥
  cut7569  adequate = bad7569  (Adequate.valid adequate Two boolean env17)
  bad7570 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b0 b0)) b1) (bop b0 b0)) b0 → ⊥
  bad7570  p = false≢true (sym (cong lower p))
  cut7570 : Adequate {ℓ} ((op (op (op (var 0) (op (var 1) (var 2))) (var 3)) (op (var 1) (var 0))) , (var 0)) → ⊥
  cut7570  adequate = bad7570  (Adequate.valid adequate Two boolean env5)
  bad7571 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b0 b0)) b1) (bop b0 b0)) b0 → ⊥
  bad7571  p = false≢true (sym (cong lower p))
  cut7571 : Adequate {ℓ} ((op (op (op (var 0) (op (var 1) (var 2))) (var 3)) (op (var 1) (var 0))) , (var 1)) → ⊥
  cut7571  adequate = bad7571  (Adequate.valid adequate Two boolean env5)
  bad7572 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b0 b0)) b1) (bop b0 b0)) b0 → ⊥
  bad7572  p = false≢true (sym (cong lower p))
  cut7572 : Adequate {ℓ} ((op (op (op (var 0) (op (var 1) (var 2))) (var 3)) (op (var 1) (var 0))) , (var 2)) → ⊥
  cut7572  adequate = bad7572  (Adequate.valid adequate Two boolean env5)
  bad7573 : PathP (λ _ → Two) (bop (bop (bop b1 (bop b0 b0)) b1) (bop b0 b1)) b1 → ⊥
  bad7573  p = false≢true (cong lower p)
  cut7573 : Adequate {ℓ} ((op (op (op (var 0) (op (var 1) (var 2))) (var 3)) (op (var 1) (var 0))) , (var 3)) → ⊥
  cut7573  adequate = bad7573  (Adequate.valid adequate Two boolean env12)
  bad7574 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b0 b0)) b0) (bop b0 b0)) b1 → ⊥
  bad7574  p = false≢true (cong lower p)
  cut7574 : Adequate {ℓ} ((op (op (op (var 0) (op (var 1) (var 2))) (var 3)) (op (var 1) (var 0))) , (var 4)) → ⊥
  cut7574  adequate = bad7574  (Adequate.valid adequate Two boolean env9)
  bad7575 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b0 b0)) b1) (bop b0 b0)) b0 → ⊥
  bad7575  p = false≢true (sym (cong lower p))
  cut7575 : Adequate {ℓ} ((op (op (op (var 0) (op (var 1) (var 2))) (var 3)) (op (var 1) (var 1))) , (var 0)) → ⊥
  cut7575  adequate = bad7575  (Adequate.valid adequate Two boolean env5)
  bad7576 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b0 b0)) b1) (bop b0 b0)) b0 → ⊥
  bad7576  p = false≢true (sym (cong lower p))
  cut7576 : Adequate {ℓ} ((op (op (op (var 0) (op (var 1) (var 2))) (var 3)) (op (var 1) (var 1))) , (var 1)) → ⊥
  cut7576  adequate = bad7576  (Adequate.valid adequate Two boolean env5)
  bad7577 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b0 b0)) b1) (bop b0 b0)) b0 → ⊥
  bad7577  p = false≢true (sym (cong lower p))
  cut7577 : Adequate {ℓ} ((op (op (op (var 0) (op (var 1) (var 2))) (var 3)) (op (var 1) (var 1))) , (var 2)) → ⊥
  cut7577  adequate = bad7577  (Adequate.valid adequate Two boolean env5)
  bad7578 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b1 b0)) b0) (bop b1 b1)) b0 → ⊥
  bad7578  p = false≢true (sym (cong lower p))
  cut7578 : Adequate {ℓ} ((op (op (op (var 0) (op (var 1) (var 2))) (var 3)) (op (var 1) (var 1))) , (var 3)) → ⊥
  cut7578  adequate = bad7578  (Adequate.valid adequate Two boolean env19)
  bad7579 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b0 b0)) b0) (bop b0 b0)) b1 → ⊥
  bad7579  p = false≢true (cong lower p)
  cut7579 : Adequate {ℓ} ((op (op (op (var 0) (op (var 1) (var 2))) (var 3)) (op (var 1) (var 1))) , (var 4)) → ⊥
  cut7579  adequate = bad7579  (Adequate.valid adequate Two boolean env9)
  bad7580 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b0 b0)) b1) (bop b0 b0)) b0 → ⊥
  bad7580  p = false≢true (sym (cong lower p))
  cut7580 : Adequate {ℓ} ((op (op (op (var 0) (op (var 1) (var 2))) (var 3)) (op (var 1) (var 2))) , (var 0)) → ⊥
  cut7580  adequate = bad7580  (Adequate.valid adequate Two boolean env5)
  bad7581 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b0 b0)) b1) (bop b0 b0)) b0 → ⊥
  bad7581  p = false≢true (sym (cong lower p))
  cut7581 : Adequate {ℓ} ((op (op (op (var 0) (op (var 1) (var 2))) (var 3)) (op (var 1) (var 2))) , (var 1)) → ⊥
  cut7581  adequate = bad7581  (Adequate.valid adequate Two boolean env5)
  bad7582 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b0 b0)) b1) (bop b0 b0)) b0 → ⊥
  bad7582  p = false≢true (sym (cong lower p))
  cut7582 : Adequate {ℓ} ((op (op (op (var 0) (op (var 1) (var 2))) (var 3)) (op (var 1) (var 2))) , (var 2)) → ⊥
  cut7582  adequate = bad7582  (Adequate.valid adequate Two boolean env5)
  env23 : ℕ → Two
  env23 zero = b0
  env23 (suc zero) = b1
  env23 (suc (suc zero)) = b1
  env23 (suc (suc (suc zero))) = b0
  env23 (suc (suc (suc (suc rest)))) = b0
  bad7583 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b1 b1)) b0) (bop b1 b1)) b0 → ⊥
  bad7583  p = false≢true (sym (cong lower p))
  cut7583 : Adequate {ℓ} ((op (op (op (var 0) (op (var 1) (var 2))) (var 3)) (op (var 1) (var 2))) , (var 3)) → ⊥
  cut7583  adequate = bad7583  (Adequate.valid adequate Two boolean env23)
  bad7584 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b0 b0)) b0) (bop b0 b0)) b1 → ⊥
  bad7584  p = false≢true (cong lower p)
  cut7584 : Adequate {ℓ} ((op (op (op (var 0) (op (var 1) (var 2))) (var 3)) (op (var 1) (var 2))) , (var 4)) → ⊥
  cut7584  adequate = bad7584  (Adequate.valid adequate Two boolean env9)
  bad7585 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b0 b0)) b1) (bop b0 b1)) b0 → ⊥
  bad7585  p = false≢true (sym (cong lower p))
  cut7585 : Adequate {ℓ} ((op (op (op (var 0) (op (var 1) (var 2))) (var 3)) (op (var 1) (var 3))) , (var 0)) → ⊥
  cut7585  adequate = bad7585  (Adequate.valid adequate Two boolean env5)
  bad7586 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b0 b0)) b1) (bop b0 b1)) b0 → ⊥
  bad7586  p = false≢true (sym (cong lower p))
  cut7586 : Adequate {ℓ} ((op (op (op (var 0) (op (var 1) (var 2))) (var 3)) (op (var 1) (var 3))) , (var 1)) → ⊥
  cut7586  adequate = bad7586  (Adequate.valid adequate Two boolean env5)
  bad7587 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b0 b0)) b1) (bop b0 b1)) b0 → ⊥
  bad7587  p = false≢true (sym (cong lower p))
  cut7587 : Adequate {ℓ} ((op (op (op (var 0) (op (var 1) (var 2))) (var 3)) (op (var 1) (var 3))) , (var 2)) → ⊥
  cut7587  adequate = bad7587  (Adequate.valid adequate Two boolean env5)
  bad7588 : PathP (λ _ → Two) (bop (bop (bop b1 (bop b0 b0)) b1) (bop b0 b1)) b1 → ⊥
  bad7588  p = false≢true (cong lower p)
  cut7588 : Adequate {ℓ} ((op (op (op (var 0) (op (var 1) (var 2))) (var 3)) (op (var 1) (var 3))) , (var 3)) → ⊥
  cut7588  adequate = bad7588  (Adequate.valid adequate Two boolean env12)
  bad7589 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b0 b0)) b0) (bop b0 b0)) b1 → ⊥
  bad7589  p = false≢true (cong lower p)
  cut7589 : Adequate {ℓ} ((op (op (op (var 0) (op (var 1) (var 2))) (var 3)) (op (var 1) (var 3))) , (var 4)) → ⊥
  cut7589  adequate = bad7589  (Adequate.valid adequate Two boolean env9)
  bad7590 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b0 b0)) b1) (bop b0 b0)) b0 → ⊥
  bad7590  p = false≢true (sym (cong lower p))
  cut7590 : Adequate {ℓ} ((op (op (op (var 0) (op (var 1) (var 2))) (var 3)) (op (var 1) (var 4))) , (var 0)) → ⊥
  cut7590  adequate = bad7590  (Adequate.valid adequate Two boolean env16)
  bad7591 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b0 b0)) b1) (bop b0 b0)) b0 → ⊥
  bad7591  p = false≢true (sym (cong lower p))
  cut7591 : Adequate {ℓ} ((op (op (op (var 0) (op (var 1) (var 2))) (var 3)) (op (var 1) (var 4))) , (var 1)) → ⊥
  cut7591  adequate = bad7591  (Adequate.valid adequate Two boolean env16)
  bad7592 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b0 b0)) b1) (bop b0 b0)) b0 → ⊥
  bad7592  p = false≢true (sym (cong lower p))
  cut7592 : Adequate {ℓ} ((op (op (op (var 0) (op (var 1) (var 2))) (var 3)) (op (var 1) (var 4))) , (var 2)) → ⊥
  cut7592  adequate = bad7592  (Adequate.valid adequate Two boolean env16)
  env24 : ℕ → Two
  env24 zero = b0
  env24 (suc zero) = b1
  env24 (suc (suc zero)) = b0
  env24 (suc (suc (suc zero))) = b0
  env24 (suc (suc (suc (suc zero)))) = b1
  env24 (suc (suc (suc (suc (suc rest))))) = b0
  bad7593 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b1 b0)) b0) (bop b1 b1)) b0 → ⊥
  bad7593  p = false≢true (sym (cong lower p))
  cut7593 : Adequate {ℓ} ((op (op (op (var 0) (op (var 1) (var 2))) (var 3)) (op (var 1) (var 4))) , (var 3)) → ⊥
  cut7593  adequate = bad7593  (Adequate.valid adequate Two boolean env24)
  bad7594 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b0 b0)) b0) (bop b0 b1)) b1 → ⊥
  bad7594  p = false≢true (cong lower p)
  cut7594 : Adequate {ℓ} ((op (op (op (var 0) (op (var 1) (var 2))) (var 3)) (op (var 1) (var 4))) , (var 4)) → ⊥
  cut7594  adequate = bad7594  (Adequate.valid adequate Two boolean env9)
  bad7595 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b0 b0)) b0) (bop b0 b0)) b1 → ⊥
  bad7595  p = false≢true (cong lower p)
  cut7595 : Adequate {ℓ} ((op (op (op (var 0) (op (var 1) (var 2))) (var 3)) (op (var 1) (var 4))) , (var 5)) → ⊥
  cut7595  adequate = bad7595  (Adequate.valid adequate Two boolean env17)
  bad7596 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b0 b0)) b1) (bop b0 b0)) b0 → ⊥
  bad7596  p = false≢true (sym (cong lower p))
  cut7596 : Adequate {ℓ} ((op (op (op (var 0) (op (var 1) (var 2))) (var 3)) (op (var 2) (var 0))) , (var 0)) → ⊥
  cut7596  adequate = bad7596  (Adequate.valid adequate Two boolean env5)
  bad7597 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b0 b0)) b1) (bop b0 b0)) b0 → ⊥
  bad7597  p = false≢true (sym (cong lower p))
  cut7597 : Adequate {ℓ} ((op (op (op (var 0) (op (var 1) (var 2))) (var 3)) (op (var 2) (var 0))) , (var 1)) → ⊥
  cut7597  adequate = bad7597  (Adequate.valid adequate Two boolean env5)
  bad7598 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b0 b0)) b1) (bop b0 b0)) b0 → ⊥
  bad7598  p = false≢true (sym (cong lower p))
  cut7598 : Adequate {ℓ} ((op (op (op (var 0) (op (var 1) (var 2))) (var 3)) (op (var 2) (var 0))) , (var 2)) → ⊥
  cut7598  adequate = bad7598  (Adequate.valid adequate Two boolean env5)
  bad7599 : PathP (λ _ → Two) (bop (bop (bop b1 (bop b0 b0)) b1) (bop b0 b1)) b1 → ⊥
  bad7599  p = false≢true (cong lower p)
  cut7599 : Adequate {ℓ} ((op (op (op (var 0) (op (var 1) (var 2))) (var 3)) (op (var 2) (var 0))) , (var 3)) → ⊥
  cut7599  adequate = bad7599  (Adequate.valid adequate Two boolean env12)
  bad7600 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b0 b0)) b0) (bop b0 b0)) b1 → ⊥
  bad7600  p = false≢true (cong lower p)
  cut7600 : Adequate {ℓ} ((op (op (op (var 0) (op (var 1) (var 2))) (var 3)) (op (var 2) (var 0))) , (var 4)) → ⊥
  cut7600  adequate = bad7600  (Adequate.valid adequate Two boolean env9)
  bad7601 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b0 b0)) b1) (bop b0 b0)) b0 → ⊥
  bad7601  p = false≢true (sym (cong lower p))
  cut7601 : Adequate {ℓ} ((op (op (op (var 0) (op (var 1) (var 2))) (var 3)) (op (var 2) (var 1))) , (var 0)) → ⊥
  cut7601  adequate = bad7601  (Adequate.valid adequate Two boolean env5)
  bad7602 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b0 b0)) b1) (bop b0 b0)) b0 → ⊥
  bad7602  p = false≢true (sym (cong lower p))
  cut7602 : Adequate {ℓ} ((op (op (op (var 0) (op (var 1) (var 2))) (var 3)) (op (var 2) (var 1))) , (var 1)) → ⊥
  cut7602  adequate = bad7602  (Adequate.valid adequate Two boolean env5)
  bad7603 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b0 b0)) b1) (bop b0 b0)) b0 → ⊥
  bad7603  p = false≢true (sym (cong lower p))
  cut7603 : Adequate {ℓ} ((op (op (op (var 0) (op (var 1) (var 2))) (var 3)) (op (var 2) (var 1))) , (var 2)) → ⊥
  cut7603  adequate = bad7603  (Adequate.valid adequate Two boolean env5)
  bad7604 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b1 b1)) b0) (bop b1 b1)) b0 → ⊥
  bad7604  p = false≢true (sym (cong lower p))
  cut7604 : Adequate {ℓ} ((op (op (op (var 0) (op (var 1) (var 2))) (var 3)) (op (var 2) (var 1))) , (var 3)) → ⊥
  cut7604  adequate = bad7604  (Adequate.valid adequate Two boolean env23)
  bad7605 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b0 b0)) b0) (bop b0 b0)) b1 → ⊥
  bad7605  p = false≢true (cong lower p)
  cut7605 : Adequate {ℓ} ((op (op (op (var 0) (op (var 1) (var 2))) (var 3)) (op (var 2) (var 1))) , (var 4)) → ⊥
  cut7605  adequate = bad7605  (Adequate.valid adequate Two boolean env9)
  bad7606 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b0 b0)) b1) (bop b0 b0)) b0 → ⊥
  bad7606  p = false≢true (sym (cong lower p))
  cut7606 : Adequate {ℓ} ((op (op (op (var 0) (op (var 1) (var 2))) (var 3)) (op (var 2) (var 2))) , (var 0)) → ⊥
  cut7606  adequate = bad7606  (Adequate.valid adequate Two boolean env5)
  bad7607 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b0 b0)) b1) (bop b0 b0)) b0 → ⊥
  bad7607  p = false≢true (sym (cong lower p))
  cut7607 : Adequate {ℓ} ((op (op (op (var 0) (op (var 1) (var 2))) (var 3)) (op (var 2) (var 2))) , (var 1)) → ⊥
  cut7607  adequate = bad7607  (Adequate.valid adequate Two boolean env5)
  bad7608 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b0 b0)) b1) (bop b0 b0)) b0 → ⊥
  bad7608  p = false≢true (sym (cong lower p))
  cut7608 : Adequate {ℓ} ((op (op (op (var 0) (op (var 1) (var 2))) (var 3)) (op (var 2) (var 2))) , (var 2)) → ⊥
  cut7608  adequate = bad7608  (Adequate.valid adequate Two boolean env5)
  bad7609 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b0 b1)) b0) (bop b1 b1)) b0 → ⊥
  bad7609  p = false≢true (sym (cong lower p))
  cut7609 : Adequate {ℓ} ((op (op (op (var 0) (op (var 1) (var 2))) (var 3)) (op (var 2) (var 2))) , (var 3)) → ⊥
  cut7609  adequate = bad7609  (Adequate.valid adequate Two boolean env8)
  bad7610 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b0 b0)) b0) (bop b0 b0)) b1 → ⊥
  bad7610  p = false≢true (cong lower p)
  cut7610 : Adequate {ℓ} ((op (op (op (var 0) (op (var 1) (var 2))) (var 3)) (op (var 2) (var 2))) , (var 4)) → ⊥
  cut7610  adequate = bad7610  (Adequate.valid adequate Two boolean env9)
  bad7611 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b0 b0)) b1) (bop b0 b1)) b0 → ⊥
  bad7611  p = false≢true (sym (cong lower p))
  cut7611 : Adequate {ℓ} ((op (op (op (var 0) (op (var 1) (var 2))) (var 3)) (op (var 2) (var 3))) , (var 0)) → ⊥
  cut7611  adequate = bad7611  (Adequate.valid adequate Two boolean env5)
  bad7612 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b0 b0)) b1) (bop b0 b1)) b0 → ⊥
  bad7612  p = false≢true (sym (cong lower p))
  cut7612 : Adequate {ℓ} ((op (op (op (var 0) (op (var 1) (var 2))) (var 3)) (op (var 2) (var 3))) , (var 1)) → ⊥
  cut7612  adequate = bad7612  (Adequate.valid adequate Two boolean env5)
  bad7613 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b0 b0)) b1) (bop b0 b1)) b0 → ⊥
  bad7613  p = false≢true (sym (cong lower p))
  cut7613 : Adequate {ℓ} ((op (op (op (var 0) (op (var 1) (var 2))) (var 3)) (op (var 2) (var 3))) , (var 2)) → ⊥
  cut7613  adequate = bad7613  (Adequate.valid adequate Two boolean env5)
  bad7614 : PathP (λ _ → Two) (bop (bop (bop b1 (bop b0 b0)) b1) (bop b0 b1)) b1 → ⊥
  bad7614  p = false≢true (cong lower p)
  cut7614 : Adequate {ℓ} ((op (op (op (var 0) (op (var 1) (var 2))) (var 3)) (op (var 2) (var 3))) , (var 3)) → ⊥
  cut7614  adequate = bad7614  (Adequate.valid adequate Two boolean env12)
  bad7615 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b0 b0)) b0) (bop b0 b0)) b1 → ⊥
  bad7615  p = false≢true (cong lower p)
  cut7615 : Adequate {ℓ} ((op (op (op (var 0) (op (var 1) (var 2))) (var 3)) (op (var 2) (var 3))) , (var 4)) → ⊥
  cut7615  adequate = bad7615  (Adequate.valid adequate Two boolean env9)
  bad7616 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b0 b0)) b1) (bop b0 b0)) b0 → ⊥
  bad7616  p = false≢true (sym (cong lower p))
  cut7616 : Adequate {ℓ} ((op (op (op (var 0) (op (var 1) (var 2))) (var 3)) (op (var 2) (var 4))) , (var 0)) → ⊥
  cut7616  adequate = bad7616  (Adequate.valid adequate Two boolean env16)
  bad7617 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b0 b0)) b1) (bop b0 b0)) b0 → ⊥
  bad7617  p = false≢true (sym (cong lower p))
  cut7617 : Adequate {ℓ} ((op (op (op (var 0) (op (var 1) (var 2))) (var 3)) (op (var 2) (var 4))) , (var 1)) → ⊥
  cut7617  adequate = bad7617  (Adequate.valid adequate Two boolean env16)
  bad7618 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b0 b0)) b1) (bop b0 b0)) b0 → ⊥
  bad7618  p = false≢true (sym (cong lower p))
  cut7618 : Adequate {ℓ} ((op (op (op (var 0) (op (var 1) (var 2))) (var 3)) (op (var 2) (var 4))) , (var 2)) → ⊥
  cut7618  adequate = bad7618  (Adequate.valid adequate Two boolean env16)
  env25 : ℕ → Two
  env25 zero = b0
  env25 (suc zero) = b0
  env25 (suc (suc zero)) = b1
  env25 (suc (suc (suc zero))) = b0
  env25 (suc (suc (suc (suc zero)))) = b1
  env25 (suc (suc (suc (suc (suc rest))))) = b0
  bad7619 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b0 b1)) b0) (bop b1 b1)) b0 → ⊥
  bad7619  p = false≢true (sym (cong lower p))
  cut7619 : Adequate {ℓ} ((op (op (op (var 0) (op (var 1) (var 2))) (var 3)) (op (var 2) (var 4))) , (var 3)) → ⊥
  cut7619  adequate = bad7619  (Adequate.valid adequate Two boolean env25)
  bad7620 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b0 b0)) b0) (bop b0 b1)) b1 → ⊥
  bad7620  p = false≢true (cong lower p)
  cut7620 : Adequate {ℓ} ((op (op (op (var 0) (op (var 1) (var 2))) (var 3)) (op (var 2) (var 4))) , (var 4)) → ⊥
  cut7620  adequate = bad7620  (Adequate.valid adequate Two boolean env9)
  bad7621 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b0 b0)) b0) (bop b0 b0)) b1 → ⊥
  bad7621  p = false≢true (cong lower p)
  cut7621 : Adequate {ℓ} ((op (op (op (var 0) (op (var 1) (var 2))) (var 3)) (op (var 2) (var 4))) , (var 5)) → ⊥
  cut7621  adequate = bad7621  (Adequate.valid adequate Two boolean env17)
  bad7622 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b0 b0)) b1) (bop b1 b0)) b0 → ⊥
  bad7622  p = false≢true (sym (cong lower p))
  cut7622 : Adequate {ℓ} ((op (op (op (var 0) (op (var 1) (var 2))) (var 3)) (op (var 3) (var 0))) , (var 0)) → ⊥
  cut7622  adequate = bad7622  (Adequate.valid adequate Two boolean env5)
  bad7623 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b0 b0)) b1) (bop b1 b0)) b0 → ⊥
  bad7623  p = false≢true (sym (cong lower p))
  cut7623 : Adequate {ℓ} ((op (op (op (var 0) (op (var 1) (var 2))) (var 3)) (op (var 3) (var 0))) , (var 1)) → ⊥
  cut7623  adequate = bad7623  (Adequate.valid adequate Two boolean env5)
  bad7624 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b0 b0)) b1) (bop b1 b0)) b0 → ⊥
  bad7624  p = false≢true (sym (cong lower p))
  cut7624 : Adequate {ℓ} ((op (op (op (var 0) (op (var 1) (var 2))) (var 3)) (op (var 3) (var 0))) , (var 2)) → ⊥
  cut7624  adequate = bad7624  (Adequate.valid adequate Two boolean env5)
  holds7625 : (z0 z1 z2 z3 : A13) → (mul13 (mul13 (mul13 z0 (mul13 z1 z2)) z3) (mul13 z3 z0)) ≡ z3
  holds7625 m13c0 m13c0 m13c0 m13c0 = refl
  holds7625 m13c0 m13c0 m13c0 m13c1 = refl
  holds7625 m13c0 m13c0 m13c0 m13c2 = refl
  holds7625 m13c0 m13c0 m13c0 m13c3 = refl
  holds7625 m13c0 m13c0 m13c1 m13c0 = refl
  holds7625 m13c0 m13c0 m13c1 m13c1 = refl
  holds7625 m13c0 m13c0 m13c1 m13c2 = refl
  holds7625 m13c0 m13c0 m13c1 m13c3 = refl
  holds7625 m13c0 m13c0 m13c2 m13c0 = refl
  holds7625 m13c0 m13c0 m13c2 m13c1 = refl
  holds7625 m13c0 m13c0 m13c2 m13c2 = refl
  holds7625 m13c0 m13c0 m13c2 m13c3 = refl
  holds7625 m13c0 m13c0 m13c3 m13c0 = refl
  holds7625 m13c0 m13c0 m13c3 m13c1 = refl
  holds7625 m13c0 m13c0 m13c3 m13c2 = refl
  holds7625 m13c0 m13c0 m13c3 m13c3 = refl
  holds7625 m13c0 m13c1 m13c0 m13c0 = refl
  holds7625 m13c0 m13c1 m13c0 m13c1 = refl
  holds7625 m13c0 m13c1 m13c0 m13c2 = refl
  holds7625 m13c0 m13c1 m13c0 m13c3 = refl
  holds7625 m13c0 m13c1 m13c1 m13c0 = refl
  holds7625 m13c0 m13c1 m13c1 m13c1 = refl
  holds7625 m13c0 m13c1 m13c1 m13c2 = refl
  holds7625 m13c0 m13c1 m13c1 m13c3 = refl
  holds7625 m13c0 m13c1 m13c2 m13c0 = refl
  holds7625 m13c0 m13c1 m13c2 m13c1 = refl
  holds7625 m13c0 m13c1 m13c2 m13c2 = refl
  holds7625 m13c0 m13c1 m13c2 m13c3 = refl
  holds7625 m13c0 m13c1 m13c3 m13c0 = refl
  holds7625 m13c0 m13c1 m13c3 m13c1 = refl
  holds7625 m13c0 m13c1 m13c3 m13c2 = refl
  holds7625 m13c0 m13c1 m13c3 m13c3 = refl
  holds7625 m13c0 m13c2 m13c0 m13c0 = refl
  holds7625 m13c0 m13c2 m13c0 m13c1 = refl
  holds7625 m13c0 m13c2 m13c0 m13c2 = refl
  holds7625 m13c0 m13c2 m13c0 m13c3 = refl
  holds7625 m13c0 m13c2 m13c1 m13c0 = refl
  holds7625 m13c0 m13c2 m13c1 m13c1 = refl
  holds7625 m13c0 m13c2 m13c1 m13c2 = refl
  holds7625 m13c0 m13c2 m13c1 m13c3 = refl
  holds7625 m13c0 m13c2 m13c2 m13c0 = refl
  holds7625 m13c0 m13c2 m13c2 m13c1 = refl
  holds7625 m13c0 m13c2 m13c2 m13c2 = refl
  holds7625 m13c0 m13c2 m13c2 m13c3 = refl
  holds7625 m13c0 m13c2 m13c3 m13c0 = refl
  holds7625 m13c0 m13c2 m13c3 m13c1 = refl
  holds7625 m13c0 m13c2 m13c3 m13c2 = refl
  holds7625 m13c0 m13c2 m13c3 m13c3 = refl
  holds7625 m13c0 m13c3 m13c0 m13c0 = refl
  holds7625 m13c0 m13c3 m13c0 m13c1 = refl
  holds7625 m13c0 m13c3 m13c0 m13c2 = refl
  holds7625 m13c0 m13c3 m13c0 m13c3 = refl
  holds7625 m13c0 m13c3 m13c1 m13c0 = refl
  holds7625 m13c0 m13c3 m13c1 m13c1 = refl
  holds7625 m13c0 m13c3 m13c1 m13c2 = refl
  holds7625 m13c0 m13c3 m13c1 m13c3 = refl
  holds7625 m13c0 m13c3 m13c2 m13c0 = refl
  holds7625 m13c0 m13c3 m13c2 m13c1 = refl
  holds7625 m13c0 m13c3 m13c2 m13c2 = refl
  holds7625 m13c0 m13c3 m13c2 m13c3 = refl
  holds7625 m13c0 m13c3 m13c3 m13c0 = refl
  holds7625 m13c0 m13c3 m13c3 m13c1 = refl
  holds7625 m13c0 m13c3 m13c3 m13c2 = refl
  holds7625 m13c0 m13c3 m13c3 m13c3 = refl
  holds7625 m13c1 m13c0 m13c0 m13c0 = refl
  holds7625 m13c1 m13c0 m13c0 m13c1 = refl
  holds7625 m13c1 m13c0 m13c0 m13c2 = refl
  holds7625 m13c1 m13c0 m13c0 m13c3 = refl
  holds7625 m13c1 m13c0 m13c1 m13c0 = refl
  holds7625 m13c1 m13c0 m13c1 m13c1 = refl
  holds7625 m13c1 m13c0 m13c1 m13c2 = refl
  holds7625 m13c1 m13c0 m13c1 m13c3 = refl
  holds7625 m13c1 m13c0 m13c2 m13c0 = refl
  holds7625 m13c1 m13c0 m13c2 m13c1 = refl
  holds7625 m13c1 m13c0 m13c2 m13c2 = refl
  holds7625 m13c1 m13c0 m13c2 m13c3 = refl
  holds7625 m13c1 m13c0 m13c3 m13c0 = refl
  holds7625 m13c1 m13c0 m13c3 m13c1 = refl
  holds7625 m13c1 m13c0 m13c3 m13c2 = refl
  holds7625 m13c1 m13c0 m13c3 m13c3 = refl
  holds7625 m13c1 m13c1 m13c0 m13c0 = refl
  holds7625 m13c1 m13c1 m13c0 m13c1 = refl
  holds7625 m13c1 m13c1 m13c0 m13c2 = refl
  holds7625 m13c1 m13c1 m13c0 m13c3 = refl
  holds7625 m13c1 m13c1 m13c1 m13c0 = refl
  holds7625 m13c1 m13c1 m13c1 m13c1 = refl
  holds7625 m13c1 m13c1 m13c1 m13c2 = refl
  holds7625 m13c1 m13c1 m13c1 m13c3 = refl
  holds7625 m13c1 m13c1 m13c2 m13c0 = refl
  holds7625 m13c1 m13c1 m13c2 m13c1 = refl
  holds7625 m13c1 m13c1 m13c2 m13c2 = refl
  holds7625 m13c1 m13c1 m13c2 m13c3 = refl
  holds7625 m13c1 m13c1 m13c3 m13c0 = refl
  holds7625 m13c1 m13c1 m13c3 m13c1 = refl
  holds7625 m13c1 m13c1 m13c3 m13c2 = refl
  holds7625 m13c1 m13c1 m13c3 m13c3 = refl
  holds7625 m13c1 m13c2 m13c0 m13c0 = refl
  holds7625 m13c1 m13c2 m13c0 m13c1 = refl
  holds7625 m13c1 m13c2 m13c0 m13c2 = refl
  holds7625 m13c1 m13c2 m13c0 m13c3 = refl
  holds7625 m13c1 m13c2 m13c1 m13c0 = refl
  holds7625 m13c1 m13c2 m13c1 m13c1 = refl
  holds7625 m13c1 m13c2 m13c1 m13c2 = refl
  holds7625 m13c1 m13c2 m13c1 m13c3 = refl
  holds7625 m13c1 m13c2 m13c2 m13c0 = refl
  holds7625 m13c1 m13c2 m13c2 m13c1 = refl
  holds7625 m13c1 m13c2 m13c2 m13c2 = refl
  holds7625 m13c1 m13c2 m13c2 m13c3 = refl
  holds7625 m13c1 m13c2 m13c3 m13c0 = refl
  holds7625 m13c1 m13c2 m13c3 m13c1 = refl
  holds7625 m13c1 m13c2 m13c3 m13c2 = refl
  holds7625 m13c1 m13c2 m13c3 m13c3 = refl
  holds7625 m13c1 m13c3 m13c0 m13c0 = refl
  holds7625 m13c1 m13c3 m13c0 m13c1 = refl
  holds7625 m13c1 m13c3 m13c0 m13c2 = refl
  holds7625 m13c1 m13c3 m13c0 m13c3 = refl
  holds7625 m13c1 m13c3 m13c1 m13c0 = refl
  holds7625 m13c1 m13c3 m13c1 m13c1 = refl
  holds7625 m13c1 m13c3 m13c1 m13c2 = refl
  holds7625 m13c1 m13c3 m13c1 m13c3 = refl
  holds7625 m13c1 m13c3 m13c2 m13c0 = refl
  holds7625 m13c1 m13c3 m13c2 m13c1 = refl
  holds7625 m13c1 m13c3 m13c2 m13c2 = refl
  holds7625 m13c1 m13c3 m13c2 m13c3 = refl
  holds7625 m13c1 m13c3 m13c3 m13c0 = refl
  holds7625 m13c1 m13c3 m13c3 m13c1 = refl
  holds7625 m13c1 m13c3 m13c3 m13c2 = refl
  holds7625 m13c1 m13c3 m13c3 m13c3 = refl
  holds7625 m13c2 m13c0 m13c0 m13c0 = refl
  holds7625 m13c2 m13c0 m13c0 m13c1 = refl
  holds7625 m13c2 m13c0 m13c0 m13c2 = refl
  holds7625 m13c2 m13c0 m13c0 m13c3 = refl
  holds7625 m13c2 m13c0 m13c1 m13c0 = refl
  holds7625 m13c2 m13c0 m13c1 m13c1 = refl
  holds7625 m13c2 m13c0 m13c1 m13c2 = refl
  holds7625 m13c2 m13c0 m13c1 m13c3 = refl
  holds7625 m13c2 m13c0 m13c2 m13c0 = refl
  holds7625 m13c2 m13c0 m13c2 m13c1 = refl
  holds7625 m13c2 m13c0 m13c2 m13c2 = refl
  holds7625 m13c2 m13c0 m13c2 m13c3 = refl
  holds7625 m13c2 m13c0 m13c3 m13c0 = refl
  holds7625 m13c2 m13c0 m13c3 m13c1 = refl
  holds7625 m13c2 m13c0 m13c3 m13c2 = refl
  holds7625 m13c2 m13c0 m13c3 m13c3 = refl
  holds7625 m13c2 m13c1 m13c0 m13c0 = refl
  holds7625 m13c2 m13c1 m13c0 m13c1 = refl
  holds7625 m13c2 m13c1 m13c0 m13c2 = refl
  holds7625 m13c2 m13c1 m13c0 m13c3 = refl
  holds7625 m13c2 m13c1 m13c1 m13c0 = refl
  holds7625 m13c2 m13c1 m13c1 m13c1 = refl
  holds7625 m13c2 m13c1 m13c1 m13c2 = refl
  holds7625 m13c2 m13c1 m13c1 m13c3 = refl
  holds7625 m13c2 m13c1 m13c2 m13c0 = refl
  holds7625 m13c2 m13c1 m13c2 m13c1 = refl
  holds7625 m13c2 m13c1 m13c2 m13c2 = refl
  holds7625 m13c2 m13c1 m13c2 m13c3 = refl
  holds7625 m13c2 m13c1 m13c3 m13c0 = refl
  holds7625 m13c2 m13c1 m13c3 m13c1 = refl
  holds7625 m13c2 m13c1 m13c3 m13c2 = refl
  holds7625 m13c2 m13c1 m13c3 m13c3 = refl
  holds7625 m13c2 m13c2 m13c0 m13c0 = refl
  holds7625 m13c2 m13c2 m13c0 m13c1 = refl
  holds7625 m13c2 m13c2 m13c0 m13c2 = refl
  holds7625 m13c2 m13c2 m13c0 m13c3 = refl
  holds7625 m13c2 m13c2 m13c1 m13c0 = refl
  holds7625 m13c2 m13c2 m13c1 m13c1 = refl
  holds7625 m13c2 m13c2 m13c1 m13c2 = refl
  holds7625 m13c2 m13c2 m13c1 m13c3 = refl
  holds7625 m13c2 m13c2 m13c2 m13c0 = refl
  holds7625 m13c2 m13c2 m13c2 m13c1 = refl
  holds7625 m13c2 m13c2 m13c2 m13c2 = refl
  holds7625 m13c2 m13c2 m13c2 m13c3 = refl
  holds7625 m13c2 m13c2 m13c3 m13c0 = refl
  holds7625 m13c2 m13c2 m13c3 m13c1 = refl
  holds7625 m13c2 m13c2 m13c3 m13c2 = refl
  holds7625 m13c2 m13c2 m13c3 m13c3 = refl
  holds7625 m13c2 m13c3 m13c0 m13c0 = refl
  holds7625 m13c2 m13c3 m13c0 m13c1 = refl
  holds7625 m13c2 m13c3 m13c0 m13c2 = refl
  holds7625 m13c2 m13c3 m13c0 m13c3 = refl
  holds7625 m13c2 m13c3 m13c1 m13c0 = refl
  holds7625 m13c2 m13c3 m13c1 m13c1 = refl
  holds7625 m13c2 m13c3 m13c1 m13c2 = refl
  holds7625 m13c2 m13c3 m13c1 m13c3 = refl
  holds7625 m13c2 m13c3 m13c2 m13c0 = refl
  holds7625 m13c2 m13c3 m13c2 m13c1 = refl
  holds7625 m13c2 m13c3 m13c2 m13c2 = refl
  holds7625 m13c2 m13c3 m13c2 m13c3 = refl
  holds7625 m13c2 m13c3 m13c3 m13c0 = refl
  holds7625 m13c2 m13c3 m13c3 m13c1 = refl
  holds7625 m13c2 m13c3 m13c3 m13c2 = refl
  holds7625 m13c2 m13c3 m13c3 m13c3 = refl
  holds7625 m13c3 m13c0 m13c0 m13c0 = refl
  holds7625 m13c3 m13c0 m13c0 m13c1 = refl
  holds7625 m13c3 m13c0 m13c0 m13c2 = refl
  holds7625 m13c3 m13c0 m13c0 m13c3 = refl
  holds7625 m13c3 m13c0 m13c1 m13c0 = refl
  holds7625 m13c3 m13c0 m13c1 m13c1 = refl
  holds7625 m13c3 m13c0 m13c1 m13c2 = refl
  holds7625 m13c3 m13c0 m13c1 m13c3 = refl
  holds7625 m13c3 m13c0 m13c2 m13c0 = refl
  holds7625 m13c3 m13c0 m13c2 m13c1 = refl
  holds7625 m13c3 m13c0 m13c2 m13c2 = refl
  holds7625 m13c3 m13c0 m13c2 m13c3 = refl
  holds7625 m13c3 m13c0 m13c3 m13c0 = refl
  holds7625 m13c3 m13c0 m13c3 m13c1 = refl
  holds7625 m13c3 m13c0 m13c3 m13c2 = refl
  holds7625 m13c3 m13c0 m13c3 m13c3 = refl
  holds7625 m13c3 m13c1 m13c0 m13c0 = refl
  holds7625 m13c3 m13c1 m13c0 m13c1 = refl
  holds7625 m13c3 m13c1 m13c0 m13c2 = refl
  holds7625 m13c3 m13c1 m13c0 m13c3 = refl
  holds7625 m13c3 m13c1 m13c1 m13c0 = refl
  holds7625 m13c3 m13c1 m13c1 m13c1 = refl
  holds7625 m13c3 m13c1 m13c1 m13c2 = refl
  holds7625 m13c3 m13c1 m13c1 m13c3 = refl
  holds7625 m13c3 m13c1 m13c2 m13c0 = refl
  holds7625 m13c3 m13c1 m13c2 m13c1 = refl
  holds7625 m13c3 m13c1 m13c2 m13c2 = refl
  holds7625 m13c3 m13c1 m13c2 m13c3 = refl
  holds7625 m13c3 m13c1 m13c3 m13c0 = refl
  holds7625 m13c3 m13c1 m13c3 m13c1 = refl
  holds7625 m13c3 m13c1 m13c3 m13c2 = refl
  holds7625 m13c3 m13c1 m13c3 m13c3 = refl
  holds7625 m13c3 m13c2 m13c0 m13c0 = refl
  holds7625 m13c3 m13c2 m13c0 m13c1 = refl
  holds7625 m13c3 m13c2 m13c0 m13c2 = refl
  holds7625 m13c3 m13c2 m13c0 m13c3 = refl
  holds7625 m13c3 m13c2 m13c1 m13c0 = refl
  holds7625 m13c3 m13c2 m13c1 m13c1 = refl
  holds7625 m13c3 m13c2 m13c1 m13c2 = refl
  holds7625 m13c3 m13c2 m13c1 m13c3 = refl
  holds7625 m13c3 m13c2 m13c2 m13c0 = refl
  holds7625 m13c3 m13c2 m13c2 m13c1 = refl
  holds7625 m13c3 m13c2 m13c2 m13c2 = refl
  holds7625 m13c3 m13c2 m13c2 m13c3 = refl
  holds7625 m13c3 m13c2 m13c3 m13c0 = refl
  holds7625 m13c3 m13c2 m13c3 m13c1 = refl
  holds7625 m13c3 m13c2 m13c3 m13c2 = refl
  holds7625 m13c3 m13c2 m13c3 m13c3 = refl
  holds7625 m13c3 m13c3 m13c0 m13c0 = refl
  holds7625 m13c3 m13c3 m13c0 m13c1 = refl
  holds7625 m13c3 m13c3 m13c0 m13c2 = refl
  holds7625 m13c3 m13c3 m13c0 m13c3 = refl
  holds7625 m13c3 m13c3 m13c1 m13c0 = refl
  holds7625 m13c3 m13c3 m13c1 m13c1 = refl
  holds7625 m13c3 m13c3 m13c1 m13c2 = refl
  holds7625 m13c3 m13c3 m13c1 m13c3 = refl
  holds7625 m13c3 m13c3 m13c2 m13c0 = refl
  holds7625 m13c3 m13c3 m13c2 m13c1 = refl
  holds7625 m13c3 m13c3 m13c2 m13c2 = refl
  holds7625 m13c3 m13c3 m13c2 m13c3 = refl
  holds7625 m13c3 m13c3 m13c3 m13c0 = refl
  holds7625 m13c3 m13c3 m13c3 m13c1 = refl
  holds7625 m13c3 m13c3 m13c3 m13c2 = refl
  holds7625 m13c3 m13c3 m13c3 m13c3 = refl
  cut7625 : Adequate {ℓ} ((op (op (op (var 0) (op (var 1) (var 2))) (var 3)) (op (var 3) (var 0))) , (var 3)) → ⊥
  cut7625  = reject13 ((op (op (op (var 0) (op (var 1) (var 2))) (var 3)) (op (var 3) (var 0))) , (var 3)) (λ env → holds7625 (env 0) (env 1) (env 2) (env 3))
  bad7626 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b0 b0)) b0) (bop b0 b0)) b1 → ⊥
  bad7626  p = false≢true (cong lower p)
  cut7626 : Adequate {ℓ} ((op (op (op (var 0) (op (var 1) (var 2))) (var 3)) (op (var 3) (var 0))) , (var 4)) → ⊥
  cut7626  adequate = bad7626  (Adequate.valid adequate Two boolean env9)
  bad7627 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b0 b0)) b1) (bop b1 b0)) b0 → ⊥
  bad7627  p = false≢true (sym (cong lower p))
  cut7627 : Adequate {ℓ} ((op (op (op (var 0) (op (var 1) (var 2))) (var 3)) (op (var 3) (var 1))) , (var 0)) → ⊥
  cut7627  adequate = bad7627  (Adequate.valid adequate Two boolean env5)
  bad7628 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b0 b0)) b1) (bop b1 b0)) b0 → ⊥
  bad7628  p = false≢true (sym (cong lower p))
  cut7628 : Adequate {ℓ} ((op (op (op (var 0) (op (var 1) (var 2))) (var 3)) (op (var 3) (var 1))) , (var 1)) → ⊥
  cut7628  adequate = bad7628  (Adequate.valid adequate Two boolean env5)
  bad7629 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b0 b0)) b1) (bop b1 b0)) b0 → ⊥
  bad7629  p = false≢true (sym (cong lower p))
  cut7629 : Adequate {ℓ} ((op (op (op (var 0) (op (var 1) (var 2))) (var 3)) (op (var 3) (var 1))) , (var 2)) → ⊥
  cut7629  adequate = bad7629  (Adequate.valid adequate Two boolean env5)
  bad7630 : PathP (λ _ → Two) (bop (bop (bop b1 (bop b0 b0)) b1) (bop b1 b0)) b1 → ⊥
  bad7630  p = false≢true (cong lower p)
  cut7630 : Adequate {ℓ} ((op (op (op (var 0) (op (var 1) (var 2))) (var 3)) (op (var 3) (var 1))) , (var 3)) → ⊥
  cut7630  adequate = bad7630  (Adequate.valid adequate Two boolean env12)
  bad7631 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b0 b0)) b0) (bop b0 b0)) b1 → ⊥
  bad7631  p = false≢true (cong lower p)
  cut7631 : Adequate {ℓ} ((op (op (op (var 0) (op (var 1) (var 2))) (var 3)) (op (var 3) (var 1))) , (var 4)) → ⊥
  cut7631  adequate = bad7631  (Adequate.valid adequate Two boolean env9)
  bad7632 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b0 b0)) b1) (bop b1 b0)) b0 → ⊥
  bad7632  p = false≢true (sym (cong lower p))
  cut7632 : Adequate {ℓ} ((op (op (op (var 0) (op (var 1) (var 2))) (var 3)) (op (var 3) (var 2))) , (var 0)) → ⊥
  cut7632  adequate = bad7632  (Adequate.valid adequate Two boolean env5)
  bad7633 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b0 b0)) b1) (bop b1 b0)) b0 → ⊥
  bad7633  p = false≢true (sym (cong lower p))
  cut7633 : Adequate {ℓ} ((op (op (op (var 0) (op (var 1) (var 2))) (var 3)) (op (var 3) (var 2))) , (var 1)) → ⊥
  cut7633  adequate = bad7633  (Adequate.valid adequate Two boolean env5)
  bad7634 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b0 b0)) b1) (bop b1 b0)) b0 → ⊥
  bad7634  p = false≢true (sym (cong lower p))
  cut7634 : Adequate {ℓ} ((op (op (op (var 0) (op (var 1) (var 2))) (var 3)) (op (var 3) (var 2))) , (var 2)) → ⊥
  cut7634  adequate = bad7634  (Adequate.valid adequate Two boolean env5)
  bad7635 : PathP (λ _ → Two) (bop (bop (bop b1 (bop b0 b0)) b1) (bop b1 b0)) b1 → ⊥
  bad7635  p = false≢true (cong lower p)
  cut7635 : Adequate {ℓ} ((op (op (op (var 0) (op (var 1) (var 2))) (var 3)) (op (var 3) (var 2))) , (var 3)) → ⊥
  cut7635  adequate = bad7635  (Adequate.valid adequate Two boolean env12)
  bad7636 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b0 b0)) b0) (bop b0 b0)) b1 → ⊥
  bad7636  p = false≢true (cong lower p)
  cut7636 : Adequate {ℓ} ((op (op (op (var 0) (op (var 1) (var 2))) (var 3)) (op (var 3) (var 2))) , (var 4)) → ⊥
  cut7636  adequate = bad7636  (Adequate.valid adequate Two boolean env9)
  bad7637 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b0 b0)) b1) (bop b1 b1)) b0 → ⊥
  bad7637  p = false≢true (sym (cong lower p))
  cut7637 : Adequate {ℓ} ((op (op (op (var 0) (op (var 1) (var 2))) (var 3)) (op (var 3) (var 3))) , (var 0)) → ⊥
  cut7637  adequate = bad7637  (Adequate.valid adequate Two boolean env5)
  bad7638 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b0 b0)) b1) (bop b1 b1)) b0 → ⊥
  bad7638  p = false≢true (sym (cong lower p))
  cut7638 : Adequate {ℓ} ((op (op (op (var 0) (op (var 1) (var 2))) (var 3)) (op (var 3) (var 3))) , (var 1)) → ⊥
  cut7638  adequate = bad7638  (Adequate.valid adequate Two boolean env5)
  bad7639 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b0 b0)) b1) (bop b1 b1)) b0 → ⊥
  bad7639  p = false≢true (sym (cong lower p))
  cut7639 : Adequate {ℓ} ((op (op (op (var 0) (op (var 1) (var 2))) (var 3)) (op (var 3) (var 3))) , (var 2)) → ⊥
  cut7639  adequate = bad7639  (Adequate.valid adequate Two boolean env5)
  holds7640 : (z0 z1 z2 z3 : A3) → (mul3 (mul3 (mul3 z0 (mul3 z1 z2)) z3) (mul3 z3 z3)) ≡ z3
  holds7640 z0 z1 z2 z3 = refl
  cut7640 : Adequate {ℓ} ((op (op (op (var 0) (op (var 1) (var 2))) (var 3)) (op (var 3) (var 3))) , (var 3)) → ⊥
  cut7640  = reject3 ((op (op (op (var 0) (op (var 1) (var 2))) (var 3)) (op (var 3) (var 3))) , (var 3)) (λ env → holds7640 (env 0) (env 1) (env 2) (env 3))
  bad7641 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b0 b0)) b0) (bop b0 b0)) b1 → ⊥
  bad7641  p = false≢true (cong lower p)
  cut7641 : Adequate {ℓ} ((op (op (op (var 0) (op (var 1) (var 2))) (var 3)) (op (var 3) (var 3))) , (var 4)) → ⊥
  cut7641  adequate = bad7641  (Adequate.valid adequate Two boolean env9)
  bad7642 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b0 b0)) b1) (bop b1 b0)) b0 → ⊥
  bad7642  p = false≢true (sym (cong lower p))
  cut7642 : Adequate {ℓ} ((op (op (op (var 0) (op (var 1) (var 2))) (var 3)) (op (var 3) (var 4))) , (var 0)) → ⊥
  cut7642  adequate = bad7642  (Adequate.valid adequate Two boolean env16)
  bad7643 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b0 b0)) b1) (bop b1 b0)) b0 → ⊥
  bad7643  p = false≢true (sym (cong lower p))
  cut7643 : Adequate {ℓ} ((op (op (op (var 0) (op (var 1) (var 2))) (var 3)) (op (var 3) (var 4))) , (var 1)) → ⊥
  cut7643  adequate = bad7643  (Adequate.valid adequate Two boolean env16)
  bad7644 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b0 b0)) b1) (bop b1 b0)) b0 → ⊥
  bad7644  p = false≢true (sym (cong lower p))
  cut7644 : Adequate {ℓ} ((op (op (op (var 0) (op (var 1) (var 2))) (var 3)) (op (var 3) (var 4))) , (var 2)) → ⊥
  cut7644  adequate = bad7644  (Adequate.valid adequate Two boolean env16)
  env26 : ℕ → Two
  env26 zero = b1
  env26 (suc zero) = b0
  env26 (suc (suc zero)) = b0
  env26 (suc (suc (suc zero))) = b1
  env26 (suc (suc (suc (suc zero)))) = b0
  env26 (suc (suc (suc (suc (suc rest))))) = b0
  bad7645 : PathP (λ _ → Two) (bop (bop (bop b1 (bop b0 b0)) b1) (bop b1 b0)) b1 → ⊥
  bad7645  p = false≢true (cong lower p)
  cut7645 : Adequate {ℓ} ((op (op (op (var 0) (op (var 1) (var 2))) (var 3)) (op (var 3) (var 4))) , (var 3)) → ⊥
  cut7645  adequate = bad7645  (Adequate.valid adequate Two boolean env26)
  bad7646 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b0 b0)) b0) (bop b0 b1)) b1 → ⊥
  bad7646  p = false≢true (cong lower p)
  cut7646 : Adequate {ℓ} ((op (op (op (var 0) (op (var 1) (var 2))) (var 3)) (op (var 3) (var 4))) , (var 4)) → ⊥
  cut7646  adequate = bad7646  (Adequate.valid adequate Two boolean env9)
  bad7647 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b0 b0)) b0) (bop b0 b0)) b1 → ⊥
  bad7647  p = false≢true (cong lower p)
  cut7647 : Adequate {ℓ} ((op (op (op (var 0) (op (var 1) (var 2))) (var 3)) (op (var 3) (var 4))) , (var 5)) → ⊥
  cut7647  adequate = bad7647  (Adequate.valid adequate Two boolean env17)
  bad7648 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b0 b0)) b1) (bop b0 b0)) b0 → ⊥
  bad7648  p = false≢true (sym (cong lower p))
  cut7648 : Adequate {ℓ} ((op (op (op (var 0) (op (var 1) (var 2))) (var 3)) (op (var 4) (var 0))) , (var 0)) → ⊥
  cut7648  adequate = bad7648  (Adequate.valid adequate Two boolean env16)
  bad7649 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b0 b0)) b1) (bop b0 b0)) b0 → ⊥
  bad7649  p = false≢true (sym (cong lower p))
  cut7649 : Adequate {ℓ} ((op (op (op (var 0) (op (var 1) (var 2))) (var 3)) (op (var 4) (var 0))) , (var 1)) → ⊥
  cut7649  adequate = bad7649  (Adequate.valid adequate Two boolean env16)
  bad7650 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b0 b0)) b1) (bop b0 b0)) b0 → ⊥
  bad7650  p = false≢true (sym (cong lower p))
  cut7650 : Adequate {ℓ} ((op (op (op (var 0) (op (var 1) (var 2))) (var 3)) (op (var 4) (var 0))) , (var 2)) → ⊥
  cut7650  adequate = bad7650  (Adequate.valid adequate Two boolean env16)
  bad7651 : PathP (λ _ → Two) (bop (bop (bop b1 (bop b0 b0)) b0) (bop b1 b1)) b0 → ⊥
  bad7651  p = false≢true (sym (cong lower p))
  cut7651 : Adequate {ℓ} ((op (op (op (var 0) (op (var 1) (var 2))) (var 3)) (op (var 4) (var 0))) , (var 3)) → ⊥
  cut7651  adequate = bad7651  (Adequate.valid adequate Two boolean env22)
  bad7652 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b0 b0)) b0) (bop b1 b0)) b1 → ⊥
  bad7652  p = false≢true (cong lower p)
  cut7652 : Adequate {ℓ} ((op (op (op (var 0) (op (var 1) (var 2))) (var 3)) (op (var 4) (var 0))) , (var 4)) → ⊥
  cut7652  adequate = bad7652  (Adequate.valid adequate Two boolean env9)
  bad7653 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b0 b0)) b0) (bop b0 b0)) b1 → ⊥
  bad7653  p = false≢true (cong lower p)
  cut7653 : Adequate {ℓ} ((op (op (op (var 0) (op (var 1) (var 2))) (var 3)) (op (var 4) (var 0))) , (var 5)) → ⊥
  cut7653  adequate = bad7653  (Adequate.valid adequate Two boolean env17)
  bad7654 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b0 b0)) b1) (bop b0 b0)) b0 → ⊥
  bad7654  p = false≢true (sym (cong lower p))
  cut7654 : Adequate {ℓ} ((op (op (op (var 0) (op (var 1) (var 2))) (var 3)) (op (var 4) (var 1))) , (var 0)) → ⊥
  cut7654  adequate = bad7654  (Adequate.valid adequate Two boolean env16)
  bad7655 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b0 b0)) b1) (bop b0 b0)) b0 → ⊥
  bad7655  p = false≢true (sym (cong lower p))
  cut7655 : Adequate {ℓ} ((op (op (op (var 0) (op (var 1) (var 2))) (var 3)) (op (var 4) (var 1))) , (var 1)) → ⊥
  cut7655  adequate = bad7655  (Adequate.valid adequate Two boolean env16)
  bad7656 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b0 b0)) b1) (bop b0 b0)) b0 → ⊥
  bad7656  p = false≢true (sym (cong lower p))
  cut7656 : Adequate {ℓ} ((op (op (op (var 0) (op (var 1) (var 2))) (var 3)) (op (var 4) (var 1))) , (var 2)) → ⊥
  cut7656  adequate = bad7656  (Adequate.valid adequate Two boolean env16)
  bad7657 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b1 b0)) b0) (bop b1 b1)) b0 → ⊥
  bad7657  p = false≢true (sym (cong lower p))
  cut7657 : Adequate {ℓ} ((op (op (op (var 0) (op (var 1) (var 2))) (var 3)) (op (var 4) (var 1))) , (var 3)) → ⊥
  cut7657  adequate = bad7657  (Adequate.valid adequate Two boolean env24)
  bad7658 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b0 b0)) b0) (bop b1 b0)) b1 → ⊥
  bad7658  p = false≢true (cong lower p)
  cut7658 : Adequate {ℓ} ((op (op (op (var 0) (op (var 1) (var 2))) (var 3)) (op (var 4) (var 1))) , (var 4)) → ⊥
  cut7658  adequate = bad7658  (Adequate.valid adequate Two boolean env9)
  bad7659 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b0 b0)) b0) (bop b0 b0)) b1 → ⊥
  bad7659  p = false≢true (cong lower p)
  cut7659 : Adequate {ℓ} ((op (op (op (var 0) (op (var 1) (var 2))) (var 3)) (op (var 4) (var 1))) , (var 5)) → ⊥
  cut7659  adequate = bad7659  (Adequate.valid adequate Two boolean env17)
  bad7660 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b0 b0)) b1) (bop b0 b0)) b0 → ⊥
  bad7660  p = false≢true (sym (cong lower p))
  cut7660 : Adequate {ℓ} ((op (op (op (var 0) (op (var 1) (var 2))) (var 3)) (op (var 4) (var 2))) , (var 0)) → ⊥
  cut7660  adequate = bad7660  (Adequate.valid adequate Two boolean env16)
  bad7661 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b0 b0)) b1) (bop b0 b0)) b0 → ⊥
  bad7661  p = false≢true (sym (cong lower p))
  cut7661 : Adequate {ℓ} ((op (op (op (var 0) (op (var 1) (var 2))) (var 3)) (op (var 4) (var 2))) , (var 1)) → ⊥
  cut7661  adequate = bad7661  (Adequate.valid adequate Two boolean env16)
  bad7662 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b0 b0)) b1) (bop b0 b0)) b0 → ⊥
  bad7662  p = false≢true (sym (cong lower p))
  cut7662 : Adequate {ℓ} ((op (op (op (var 0) (op (var 1) (var 2))) (var 3)) (op (var 4) (var 2))) , (var 2)) → ⊥
  cut7662  adequate = bad7662  (Adequate.valid adequate Two boolean env16)
  bad7663 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b0 b1)) b0) (bop b1 b1)) b0 → ⊥
  bad7663  p = false≢true (sym (cong lower p))
  cut7663 : Adequate {ℓ} ((op (op (op (var 0) (op (var 1) (var 2))) (var 3)) (op (var 4) (var 2))) , (var 3)) → ⊥
  cut7663  adequate = bad7663  (Adequate.valid adequate Two boolean env25)
  bad7664 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b0 b0)) b0) (bop b1 b0)) b1 → ⊥
  bad7664  p = false≢true (cong lower p)
  cut7664 : Adequate {ℓ} ((op (op (op (var 0) (op (var 1) (var 2))) (var 3)) (op (var 4) (var 2))) , (var 4)) → ⊥
  cut7664  adequate = bad7664  (Adequate.valid adequate Two boolean env9)
  bad7665 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b0 b0)) b0) (bop b0 b0)) b1 → ⊥
  bad7665  p = false≢true (cong lower p)
  cut7665 : Adequate {ℓ} ((op (op (op (var 0) (op (var 1) (var 2))) (var 3)) (op (var 4) (var 2))) , (var 5)) → ⊥
  cut7665  adequate = bad7665  (Adequate.valid adequate Two boolean env17)
  bad7666 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b0 b0)) b1) (bop b0 b1)) b0 → ⊥
  bad7666  p = false≢true (sym (cong lower p))
  cut7666 : Adequate {ℓ} ((op (op (op (var 0) (op (var 1) (var 2))) (var 3)) (op (var 4) (var 3))) , (var 0)) → ⊥
  cut7666  adequate = bad7666  (Adequate.valid adequate Two boolean env16)
  bad7667 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b0 b0)) b1) (bop b0 b1)) b0 → ⊥
  bad7667  p = false≢true (sym (cong lower p))
  cut7667 : Adequate {ℓ} ((op (op (op (var 0) (op (var 1) (var 2))) (var 3)) (op (var 4) (var 3))) , (var 1)) → ⊥
  cut7667  adequate = bad7667  (Adequate.valid adequate Two boolean env16)
  bad7668 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b0 b0)) b1) (bop b0 b1)) b0 → ⊥
  bad7668  p = false≢true (sym (cong lower p))
  cut7668 : Adequate {ℓ} ((op (op (op (var 0) (op (var 1) (var 2))) (var 3)) (op (var 4) (var 3))) , (var 2)) → ⊥
  cut7668  adequate = bad7668  (Adequate.valid adequate Two boolean env16)
  bad7669 : PathP (λ _ → Two) (bop (bop (bop b1 (bop b0 b0)) b1) (bop b0 b1)) b1 → ⊥
  bad7669  p = false≢true (cong lower p)
  cut7669 : Adequate {ℓ} ((op (op (op (var 0) (op (var 1) (var 2))) (var 3)) (op (var 4) (var 3))) , (var 3)) → ⊥
  cut7669  adequate = bad7669  (Adequate.valid adequate Two boolean env26)
  bad7670 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b0 b0)) b0) (bop b1 b0)) b1 → ⊥
  bad7670  p = false≢true (cong lower p)
  cut7670 : Adequate {ℓ} ((op (op (op (var 0) (op (var 1) (var 2))) (var 3)) (op (var 4) (var 3))) , (var 4)) → ⊥
  cut7670  adequate = bad7670  (Adequate.valid adequate Two boolean env9)
  bad7671 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b0 b0)) b0) (bop b0 b0)) b1 → ⊥
  bad7671  p = false≢true (cong lower p)
  cut7671 : Adequate {ℓ} ((op (op (op (var 0) (op (var 1) (var 2))) (var 3)) (op (var 4) (var 3))) , (var 5)) → ⊥
  cut7671  adequate = bad7671  (Adequate.valid adequate Two boolean env17)
  bad7672 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b0 b0)) b0) (bop b1 b1)) b0 → ⊥
  bad7672  p = false≢true (sym (cong lower p))
  cut7672 : Adequate {ℓ} ((op (op (op (var 0) (op (var 1) (var 2))) (var 3)) (op (var 4) (var 4))) , (var 0)) → ⊥
  cut7672  adequate = bad7672  (Adequate.valid adequate Two boolean env9)
  bad7673 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b0 b0)) b0) (bop b1 b1)) b0 → ⊥
  bad7673  p = false≢true (sym (cong lower p))
  cut7673 : Adequate {ℓ} ((op (op (op (var 0) (op (var 1) (var 2))) (var 3)) (op (var 4) (var 4))) , (var 1)) → ⊥
  cut7673  adequate = bad7673  (Adequate.valid adequate Two boolean env9)
  bad7674 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b0 b0)) b0) (bop b1 b1)) b0 → ⊥
  bad7674  p = false≢true (sym (cong lower p))
  cut7674 : Adequate {ℓ} ((op (op (op (var 0) (op (var 1) (var 2))) (var 3)) (op (var 4) (var 4))) , (var 2)) → ⊥
  cut7674  adequate = bad7674  (Adequate.valid adequate Two boolean env9)
  bad7675 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b0 b0)) b0) (bop b1 b1)) b0 → ⊥
  bad7675  p = false≢true (sym (cong lower p))
  cut7675 : Adequate {ℓ} ((op (op (op (var 0) (op (var 1) (var 2))) (var 3)) (op (var 4) (var 4))) , (var 3)) → ⊥
  cut7675  adequate = bad7675  (Adequate.valid adequate Two boolean env9)
  bad7676 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b0 b0)) b1) (bop b0 b0)) b0 → ⊥
  bad7676  p = false≢true (sym (cong lower p))
  cut7676 : Adequate {ℓ} ((op (op (op (var 0) (op (var 1) (var 2))) (var 3)) (op (var 4) (var 4))) , (var 4)) → ⊥
  cut7676  adequate = bad7676  (Adequate.valid adequate Two boolean env16)
  bad7677 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b0 b0)) b0) (bop b0 b0)) b1 → ⊥
  bad7677  p = false≢true (cong lower p)
  cut7677 : Adequate {ℓ} ((op (op (op (var 0) (op (var 1) (var 2))) (var 3)) (op (var 4) (var 4))) , (var 5)) → ⊥
  cut7677  adequate = bad7677  (Adequate.valid adequate Two boolean env17)
  env27 : ℕ → Two
  env27 zero = b0
  env27 (suc zero) = b0
  env27 (suc (suc zero)) = b0
  env27 (suc (suc (suc zero))) = b0
  env27 (suc (suc (suc (suc zero)))) = b1
  env27 (suc (suc (suc (suc (suc zero))))) = b1
  env27 (suc (suc (suc (suc (suc (suc rest)))))) = b0
  bad7678 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b0 b0)) b0) (bop b1 b1)) b0 → ⊥
  bad7678  p = false≢true (sym (cong lower p))
  cut7678 : Adequate {ℓ} ((op (op (op (var 0) (op (var 1) (var 2))) (var 3)) (op (var 4) (var 5))) , (var 0)) → ⊥
  cut7678  adequate = bad7678  (Adequate.valid adequate Two boolean env27)
  bad7679 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b0 b0)) b0) (bop b1 b1)) b0 → ⊥
  bad7679  p = false≢true (sym (cong lower p))
  cut7679 : Adequate {ℓ} ((op (op (op (var 0) (op (var 1) (var 2))) (var 3)) (op (var 4) (var 5))) , (var 1)) → ⊥
  cut7679  adequate = bad7679  (Adequate.valid adequate Two boolean env27)
  bad7680 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b0 b0)) b0) (bop b1 b1)) b0 → ⊥
  bad7680  p = false≢true (sym (cong lower p))
  cut7680 : Adequate {ℓ} ((op (op (op (var 0) (op (var 1) (var 2))) (var 3)) (op (var 4) (var 5))) , (var 2)) → ⊥
  cut7680  adequate = bad7680  (Adequate.valid adequate Two boolean env27)
  bad7681 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b0 b0)) b0) (bop b1 b1)) b0 → ⊥
  bad7681  p = false≢true (sym (cong lower p))
  cut7681 : Adequate {ℓ} ((op (op (op (var 0) (op (var 1) (var 2))) (var 3)) (op (var 4) (var 5))) , (var 3)) → ⊥
  cut7681  adequate = bad7681  (Adequate.valid adequate Two boolean env27)
  env28 : ℕ → Two
  env28 zero = b0
  env28 (suc zero) = b0
  env28 (suc (suc zero)) = b0
  env28 (suc (suc (suc zero))) = b0
  env28 (suc (suc (suc (suc zero)))) = b1
  env28 (suc (suc (suc (suc (suc zero))))) = b0
  env28 (suc (suc (suc (suc (suc (suc rest)))))) = b0
  bad7682 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b0 b0)) b0) (bop b1 b0)) b1 → ⊥
  bad7682  p = false≢true (cong lower p)
  cut7682 : Adequate {ℓ} ((op (op (op (var 0) (op (var 1) (var 2))) (var 3)) (op (var 4) (var 5))) , (var 4)) → ⊥
  cut7682  adequate = bad7682  (Adequate.valid adequate Two boolean env28)
  bad7683 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b0 b0)) b0) (bop b0 b1)) b1 → ⊥
  bad7683  p = false≢true (cong lower p)
  cut7683 : Adequate {ℓ} ((op (op (op (var 0) (op (var 1) (var 2))) (var 3)) (op (var 4) (var 5))) , (var 5)) → ⊥
  cut7683  adequate = bad7683  (Adequate.valid adequate Two boolean env17)
  env29 : ℕ → Two
  env29 zero = b0
  env29 (suc zero) = b0
  env29 (suc (suc zero)) = b0
  env29 (suc (suc (suc zero))) = b0
  env29 (suc (suc (suc (suc zero)))) = b0
  env29 (suc (suc (suc (suc (suc zero))))) = b0
  env29 (suc (suc (suc (suc (suc (suc zero)))))) = b1
  env29 (suc (suc (suc (suc (suc (suc (suc rest))))))) = b0
  bad7684 : PathP (λ _ → Two) (bop (bop (bop b0 (bop b0 b0)) b0) (bop b0 b0)) b1 → ⊥
  bad7684  p = false≢true (cong lower p)
  cut7684 : Adequate {ℓ} ((op (op (op (var 0) (op (var 1) (var 2))) (var 3)) (op (var 4) (var 5))) , (var 6)) → ⊥
  cut7684  adequate = bad7684  (Adequate.valid adequate Two boolean env29)
