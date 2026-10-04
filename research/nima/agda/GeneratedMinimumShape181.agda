{-# OPTIONS --safe --cubical --guardedness #-}
module GeneratedMinimumShape181 where
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
  holds7685 : (z0 : A1) → (mul1 (mul1 (mul1 (mul1 z0 z0) z0) z0) (mul1 z0 z0)) ≡ z0
  holds7685 m1c0 = refl
  holds7685 m1c1 = refl
  cut7685 : Adequate {ℓ} ((op (op (op (op (var 0) (var 0)) (var 0)) (var 0)) (op (var 0) (var 0))) , (var 0)) → ⊥
  cut7685  = reject1 ((op (op (op (op (var 0) (var 0)) (var 0)) (var 0)) (op (var 0) (var 0))) , (var 0)) (λ env → holds7685 (env 0))
  env0 : ℕ → Two
  env0 zero = b0
  env0 (suc zero) = b1
  env0 (suc (suc rest)) = b0
  bad7686 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b0) b0) b0) (bop b0 b0)) b1 → ⊥
  bad7686  p = false≢true (cong lower p)
  cut7686 : Adequate {ℓ} ((op (op (op (op (var 0) (var 0)) (var 0)) (var 0)) (op (var 0) (var 0))) , (var 1)) → ⊥
  cut7686  adequate = bad7686  (Adequate.valid adequate Two boolean env0)
  holds7687 : (z0 z1 : A2) → (mul2 (mul2 (mul2 (mul2 z0 z0) z0) z0) (mul2 z0 z1)) ≡ z0
  holds7687 z0 z1 = refl
  cut7687 : Adequate {ℓ} ((op (op (op (op (var 0) (var 0)) (var 0)) (var 0)) (op (var 0) (var 1))) , (var 0)) → ⊥
  cut7687  = reject2 ((op (op (op (op (var 0) (var 0)) (var 0)) (var 0)) (op (var 0) (var 1))) , (var 0)) (λ env → holds7687 (env 0) (env 1))
  bad7688 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b0) b0) b0) (bop b0 b1)) b1 → ⊥
  bad7688  p = false≢true (cong lower p)
  cut7688 : Adequate {ℓ} ((op (op (op (op (var 0) (var 0)) (var 0)) (var 0)) (op (var 0) (var 1))) , (var 1)) → ⊥
  cut7688  adequate = bad7688  (Adequate.valid adequate Two boolean env0)
  env1 : ℕ → Two
  env1 zero = b0
  env1 (suc zero) = b0
  env1 (suc (suc zero)) = b1
  env1 (suc (suc (suc rest))) = b0
  bad7689 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b0) b0) b0) (bop b0 b0)) b1 → ⊥
  bad7689  p = false≢true (cong lower p)
  cut7689 : Adequate {ℓ} ((op (op (op (op (var 0) (var 0)) (var 0)) (var 0)) (op (var 0) (var 1))) , (var 2)) → ⊥
  cut7689  adequate = bad7689  (Adequate.valid adequate Two boolean env1)
  holds7690 : (z0 z1 : A2) → (mul2 (mul2 (mul2 (mul2 z0 z0) z0) z0) (mul2 z1 z0)) ≡ z0
  holds7690 z0 z1 = refl
  cut7690 : Adequate {ℓ} ((op (op (op (op (var 0) (var 0)) (var 0)) (var 0)) (op (var 1) (var 0))) , (var 0)) → ⊥
  cut7690  = reject2 ((op (op (op (op (var 0) (var 0)) (var 0)) (var 0)) (op (var 1) (var 0))) , (var 0)) (λ env → holds7690 (env 0) (env 1))
  bad7691 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b0) b0) b0) (bop b1 b0)) b1 → ⊥
  bad7691  p = false≢true (cong lower p)
  cut7691 : Adequate {ℓ} ((op (op (op (op (var 0) (var 0)) (var 0)) (var 0)) (op (var 1) (var 0))) , (var 1)) → ⊥
  cut7691  adequate = bad7691  (Adequate.valid adequate Two boolean env0)
  bad7692 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b0) b0) b0) (bop b0 b0)) b1 → ⊥
  bad7692  p = false≢true (cong lower p)
  cut7692 : Adequate {ℓ} ((op (op (op (op (var 0) (var 0)) (var 0)) (var 0)) (op (var 1) (var 0))) , (var 2)) → ⊥
  cut7692  adequate = bad7692  (Adequate.valid adequate Two boolean env1)
  bad7693 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b0) b0) b0) (bop b1 b1)) b0 → ⊥
  bad7693  p = false≢true (sym (cong lower p))
  cut7693 : Adequate {ℓ} ((op (op (op (op (var 0) (var 0)) (var 0)) (var 0)) (op (var 1) (var 1))) , (var 0)) → ⊥
  cut7693  adequate = bad7693  (Adequate.valid adequate Two boolean env0)
  env2 : ℕ → Two
  env2 zero = b1
  env2 (suc zero) = b0
  env2 (suc (suc rest)) = b0
  bad7694 : PathP (λ _ → Two) (bop (bop (bop (bop b1 b1) b1) b1) (bop b0 b0)) b0 → ⊥
  bad7694  p = false≢true (sym (cong lower p))
  cut7694 : Adequate {ℓ} ((op (op (op (op (var 0) (var 0)) (var 0)) (var 0)) (op (var 1) (var 1))) , (var 1)) → ⊥
  cut7694  adequate = bad7694  (Adequate.valid adequate Two boolean env2)
  bad7695 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b0) b0) b0) (bop b0 b0)) b1 → ⊥
  bad7695  p = false≢true (cong lower p)
  cut7695 : Adequate {ℓ} ((op (op (op (op (var 0) (var 0)) (var 0)) (var 0)) (op (var 1) (var 1))) , (var 2)) → ⊥
  cut7695  adequate = bad7695  (Adequate.valid adequate Two boolean env1)
  env3 : ℕ → Two
  env3 zero = b0
  env3 (suc zero) = b1
  env3 (suc (suc zero)) = b1
  env3 (suc (suc (suc rest))) = b0
  bad7696 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b0) b0) b0) (bop b1 b1)) b0 → ⊥
  bad7696  p = false≢true (sym (cong lower p))
  cut7696 : Adequate {ℓ} ((op (op (op (op (var 0) (var 0)) (var 0)) (var 0)) (op (var 1) (var 2))) , (var 0)) → ⊥
  cut7696  adequate = bad7696  (Adequate.valid adequate Two boolean env3)
  env4 : ℕ → Two
  env4 zero = b0
  env4 (suc zero) = b1
  env4 (suc (suc zero)) = b0
  env4 (suc (suc (suc rest))) = b0
  bad7697 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b0) b0) b0) (bop b1 b0)) b1 → ⊥
  bad7697  p = false≢true (cong lower p)
  cut7697 : Adequate {ℓ} ((op (op (op (op (var 0) (var 0)) (var 0)) (var 0)) (op (var 1) (var 2))) , (var 1)) → ⊥
  cut7697  adequate = bad7697  (Adequate.valid adequate Two boolean env4)
  bad7698 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b0) b0) b0) (bop b0 b1)) b1 → ⊥
  bad7698  p = false≢true (cong lower p)
  cut7698 : Adequate {ℓ} ((op (op (op (op (var 0) (var 0)) (var 0)) (var 0)) (op (var 1) (var 2))) , (var 2)) → ⊥
  cut7698  adequate = bad7698  (Adequate.valid adequate Two boolean env1)
  env5 : ℕ → Two
  env5 zero = b0
  env5 (suc zero) = b0
  env5 (suc (suc zero)) = b0
  env5 (suc (suc (suc zero))) = b1
  env5 (suc (suc (suc (suc rest)))) = b0
  bad7699 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b0) b0) b0) (bop b0 b0)) b1 → ⊥
  bad7699  p = false≢true (cong lower p)
  cut7699 : Adequate {ℓ} ((op (op (op (op (var 0) (var 0)) (var 0)) (var 0)) (op (var 1) (var 2))) , (var 3)) → ⊥
  cut7699  adequate = bad7699  (Adequate.valid adequate Two boolean env5)
  bad7700 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b0) b0) b1) (bop b0 b0)) b0 → ⊥
  bad7700  p = false≢true (sym (cong lower p))
  cut7700 : Adequate {ℓ} ((op (op (op (op (var 0) (var 0)) (var 0)) (var 1)) (op (var 0) (var 0))) , (var 0)) → ⊥
  cut7700  adequate = bad7700  (Adequate.valid adequate Two boolean env0)
  bad7701 : PathP (λ _ → Two) (bop (bop (bop (bop b1 b1) b1) b0) (bop b1 b1)) b0 → ⊥
  bad7701  p = false≢true (sym (cong lower p))
  cut7701 : Adequate {ℓ} ((op (op (op (op (var 0) (var 0)) (var 0)) (var 1)) (op (var 0) (var 0))) , (var 1)) → ⊥
  cut7701  adequate = bad7701  (Adequate.valid adequate Two boolean env2)
  bad7702 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b0) b0) b0) (bop b0 b0)) b1 → ⊥
  bad7702  p = false≢true (cong lower p)
  cut7702 : Adequate {ℓ} ((op (op (op (op (var 0) (var 0)) (var 0)) (var 1)) (op (var 0) (var 0))) , (var 2)) → ⊥
  cut7702  adequate = bad7702  (Adequate.valid adequate Two boolean env1)
  bad7703 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b0) b0) b1) (bop b0 b1)) b0 → ⊥
  bad7703  p = false≢true (sym (cong lower p))
  cut7703 : Adequate {ℓ} ((op (op (op (op (var 0) (var 0)) (var 0)) (var 1)) (op (var 0) (var 1))) , (var 0)) → ⊥
  cut7703  adequate = bad7703  (Adequate.valid adequate Two boolean env0)
  holds7704 : (z0 z1 : A3) → (mul3 (mul3 (mul3 (mul3 z0 z0) z0) z1) (mul3 z0 z1)) ≡ z1
  holds7704 z0 z1 = refl
  cut7704 : Adequate {ℓ} ((op (op (op (op (var 0) (var 0)) (var 0)) (var 1)) (op (var 0) (var 1))) , (var 1)) → ⊥
  cut7704  = reject3 ((op (op (op (op (var 0) (var 0)) (var 0)) (var 1)) (op (var 0) (var 1))) , (var 1)) (λ env → holds7704 (env 0) (env 1))
  bad7705 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b0) b0) b0) (bop b0 b0)) b1 → ⊥
  bad7705  p = false≢true (cong lower p)
  cut7705 : Adequate {ℓ} ((op (op (op (op (var 0) (var 0)) (var 0)) (var 1)) (op (var 0) (var 1))) , (var 2)) → ⊥
  cut7705  adequate = bad7705  (Adequate.valid adequate Two boolean env1)
  bad7706 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b0) b0) b1) (bop b0 b0)) b0 → ⊥
  bad7706  p = false≢true (sym (cong lower p))
  cut7706 : Adequate {ℓ} ((op (op (op (op (var 0) (var 0)) (var 0)) (var 1)) (op (var 0) (var 2))) , (var 0)) → ⊥
  cut7706  adequate = bad7706  (Adequate.valid adequate Two boolean env4)
  env6 : ℕ → Two
  env6 zero = b1
  env6 (suc zero) = b0
  env6 (suc (suc zero)) = b1
  env6 (suc (suc (suc rest))) = b0
  bad7707 : PathP (λ _ → Two) (bop (bop (bop (bop b1 b1) b1) b0) (bop b1 b1)) b0 → ⊥
  bad7707  p = false≢true (sym (cong lower p))
  cut7707 : Adequate {ℓ} ((op (op (op (op (var 0) (var 0)) (var 0)) (var 1)) (op (var 0) (var 2))) , (var 1)) → ⊥
  cut7707  adequate = bad7707  (Adequate.valid adequate Two boolean env6)
  bad7708 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b0) b0) b0) (bop b0 b1)) b1 → ⊥
  bad7708  p = false≢true (cong lower p)
  cut7708 : Adequate {ℓ} ((op (op (op (op (var 0) (var 0)) (var 0)) (var 1)) (op (var 0) (var 2))) , (var 2)) → ⊥
  cut7708  adequate = bad7708  (Adequate.valid adequate Two boolean env1)
  bad7709 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b0) b0) b0) (bop b0 b0)) b1 → ⊥
  bad7709  p = false≢true (cong lower p)
  cut7709 : Adequate {ℓ} ((op (op (op (op (var 0) (var 0)) (var 0)) (var 1)) (op (var 0) (var 2))) , (var 3)) → ⊥
  cut7709  adequate = bad7709  (Adequate.valid adequate Two boolean env5)
  bad7710 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b0) b0) b1) (bop b1 b0)) b0 → ⊥
  bad7710  p = false≢true (sym (cong lower p))
  cut7710 : Adequate {ℓ} ((op (op (op (op (var 0) (var 0)) (var 0)) (var 1)) (op (var 1) (var 0))) , (var 0)) → ⊥
  cut7710  adequate = bad7710  (Adequate.valid adequate Two boolean env0)
  holds7711 : (z0 z1 : A9) → (mul9 (mul9 (mul9 (mul9 z0 z0) z0) z1) (mul9 z1 z0)) ≡ z1
  holds7711 m9c0 m9c0 = refl
  holds7711 m9c0 m9c1 = refl
  holds7711 m9c0 m9c2 = refl
  holds7711 m9c1 m9c0 = refl
  holds7711 m9c1 m9c1 = refl
  holds7711 m9c1 m9c2 = refl
  holds7711 m9c2 m9c0 = refl
  holds7711 m9c2 m9c1 = refl
  holds7711 m9c2 m9c2 = refl
  cut7711 : Adequate {ℓ} ((op (op (op (op (var 0) (var 0)) (var 0)) (var 1)) (op (var 1) (var 0))) , (var 1)) → ⊥
  cut7711  = reject9 ((op (op (op (op (var 0) (var 0)) (var 0)) (var 1)) (op (var 1) (var 0))) , (var 1)) (λ env → holds7711 (env 0) (env 1))
  bad7712 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b0) b0) b0) (bop b0 b0)) b1 → ⊥
  bad7712  p = false≢true (cong lower p)
  cut7712 : Adequate {ℓ} ((op (op (op (op (var 0) (var 0)) (var 0)) (var 1)) (op (var 1) (var 0))) , (var 2)) → ⊥
  cut7712  adequate = bad7712  (Adequate.valid adequate Two boolean env1)
  bad7713 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b0) b0) b1) (bop b1 b1)) b0 → ⊥
  bad7713  p = false≢true (sym (cong lower p))
  cut7713 : Adequate {ℓ} ((op (op (op (op (var 0) (var 0)) (var 0)) (var 1)) (op (var 1) (var 1))) , (var 0)) → ⊥
  cut7713  adequate = bad7713  (Adequate.valid adequate Two boolean env0)
  holds7714 : (z0 z1 : A3) → (mul3 (mul3 (mul3 (mul3 z0 z0) z0) z1) (mul3 z1 z1)) ≡ z1
  holds7714 z0 z1 = refl
  cut7714 : Adequate {ℓ} ((op (op (op (op (var 0) (var 0)) (var 0)) (var 1)) (op (var 1) (var 1))) , (var 1)) → ⊥
  cut7714  = reject3 ((op (op (op (op (var 0) (var 0)) (var 0)) (var 1)) (op (var 1) (var 1))) , (var 1)) (λ env → holds7714 (env 0) (env 1))
  bad7715 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b0) b0) b0) (bop b0 b0)) b1 → ⊥
  bad7715  p = false≢true (cong lower p)
  cut7715 : Adequate {ℓ} ((op (op (op (op (var 0) (var 0)) (var 0)) (var 1)) (op (var 1) (var 1))) , (var 2)) → ⊥
  cut7715  adequate = bad7715  (Adequate.valid adequate Two boolean env1)
  bad7716 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b0) b0) b1) (bop b1 b0)) b0 → ⊥
  bad7716  p = false≢true (sym (cong lower p))
  cut7716 : Adequate {ℓ} ((op (op (op (op (var 0) (var 0)) (var 0)) (var 1)) (op (var 1) (var 2))) , (var 0)) → ⊥
  cut7716  adequate = bad7716  (Adequate.valid adequate Two boolean env4)
  holds7717 : (z0 z1 z2 : A11) → (mul11 (mul11 (mul11 (mul11 z0 z0) z0) z1) (mul11 z1 z2)) ≡ z1
  holds7717 m11c0 m11c0 m11c0 = refl
  holds7717 m11c0 m11c0 m11c1 = refl
  holds7717 m11c0 m11c0 m11c2 = refl
  holds7717 m11c0 m11c1 z2 = refl
  holds7717 m11c0 m11c2 z2 = refl
  holds7717 m11c1 m11c0 m11c0 = refl
  holds7717 m11c1 m11c0 m11c1 = refl
  holds7717 m11c1 m11c0 m11c2 = refl
  holds7717 m11c1 m11c1 z2 = refl
  holds7717 m11c1 m11c2 z2 = refl
  holds7717 m11c2 m11c0 m11c0 = refl
  holds7717 m11c2 m11c0 m11c1 = refl
  holds7717 m11c2 m11c0 m11c2 = refl
  holds7717 m11c2 m11c1 z2 = refl
  holds7717 m11c2 m11c2 z2 = refl
  cut7717 : Adequate {ℓ} ((op (op (op (op (var 0) (var 0)) (var 0)) (var 1)) (op (var 1) (var 2))) , (var 1)) → ⊥
  cut7717  = reject11 ((op (op (op (op (var 0) (var 0)) (var 0)) (var 1)) (op (var 1) (var 2))) , (var 1)) (λ env → holds7717 (env 0) (env 1) (env 2))
  bad7718 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b0) b0) b0) (bop b0 b1)) b1 → ⊥
  bad7718  p = false≢true (cong lower p)
  cut7718 : Adequate {ℓ} ((op (op (op (op (var 0) (var 0)) (var 0)) (var 1)) (op (var 1) (var 2))) , (var 2)) → ⊥
  cut7718  adequate = bad7718  (Adequate.valid adequate Two boolean env1)
  bad7719 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b0) b0) b0) (bop b0 b0)) b1 → ⊥
  bad7719  p = false≢true (cong lower p)
  cut7719 : Adequate {ℓ} ((op (op (op (op (var 0) (var 0)) (var 0)) (var 1)) (op (var 1) (var 2))) , (var 3)) → ⊥
  cut7719  adequate = bad7719  (Adequate.valid adequate Two boolean env5)
  bad7720 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b0) b0) b1) (bop b0 b0)) b0 → ⊥
  bad7720  p = false≢true (sym (cong lower p))
  cut7720 : Adequate {ℓ} ((op (op (op (op (var 0) (var 0)) (var 0)) (var 1)) (op (var 2) (var 0))) , (var 0)) → ⊥
  cut7720  adequate = bad7720  (Adequate.valid adequate Two boolean env4)
  bad7721 : PathP (λ _ → Two) (bop (bop (bop (bop b1 b1) b1) b0) (bop b1 b1)) b0 → ⊥
  bad7721  p = false≢true (sym (cong lower p))
  cut7721 : Adequate {ℓ} ((op (op (op (op (var 0) (var 0)) (var 0)) (var 1)) (op (var 2) (var 0))) , (var 1)) → ⊥
  cut7721  adequate = bad7721  (Adequate.valid adequate Two boolean env6)
  bad7722 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b0) b0) b0) (bop b1 b0)) b1 → ⊥
  bad7722  p = false≢true (cong lower p)
  cut7722 : Adequate {ℓ} ((op (op (op (op (var 0) (var 0)) (var 0)) (var 1)) (op (var 2) (var 0))) , (var 2)) → ⊥
  cut7722  adequate = bad7722  (Adequate.valid adequate Two boolean env1)
  bad7723 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b0) b0) b0) (bop b0 b0)) b1 → ⊥
  bad7723  p = false≢true (cong lower p)
  cut7723 : Adequate {ℓ} ((op (op (op (op (var 0) (var 0)) (var 0)) (var 1)) (op (var 2) (var 0))) , (var 3)) → ⊥
  cut7723  adequate = bad7723  (Adequate.valid adequate Two boolean env5)
  bad7724 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b0) b0) b1) (bop b0 b1)) b0 → ⊥
  bad7724  p = false≢true (sym (cong lower p))
  cut7724 : Adequate {ℓ} ((op (op (op (op (var 0) (var 0)) (var 0)) (var 1)) (op (var 2) (var 1))) , (var 0)) → ⊥
  cut7724  adequate = bad7724  (Adequate.valid adequate Two boolean env4)
  holds7725 : (z0 z1 z2 : A3) → (mul3 (mul3 (mul3 (mul3 z0 z0) z0) z1) (mul3 z2 z1)) ≡ z1
  holds7725 z0 z1 z2 = refl
  cut7725 : Adequate {ℓ} ((op (op (op (op (var 0) (var 0)) (var 0)) (var 1)) (op (var 2) (var 1))) , (var 1)) → ⊥
  cut7725  = reject3 ((op (op (op (op (var 0) (var 0)) (var 0)) (var 1)) (op (var 2) (var 1))) , (var 1)) (λ env → holds7725 (env 0) (env 1) (env 2))
  bad7726 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b0) b0) b0) (bop b1 b0)) b1 → ⊥
  bad7726  p = false≢true (cong lower p)
  cut7726 : Adequate {ℓ} ((op (op (op (op (var 0) (var 0)) (var 0)) (var 1)) (op (var 2) (var 1))) , (var 2)) → ⊥
  cut7726  adequate = bad7726  (Adequate.valid adequate Two boolean env1)
  bad7727 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b0) b0) b0) (bop b0 b0)) b1 → ⊥
  bad7727  p = false≢true (cong lower p)
  cut7727 : Adequate {ℓ} ((op (op (op (op (var 0) (var 0)) (var 0)) (var 1)) (op (var 2) (var 1))) , (var 3)) → ⊥
  cut7727  adequate = bad7727  (Adequate.valid adequate Two boolean env5)
  bad7728 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b0) b0) b0) (bop b1 b1)) b0 → ⊥
  bad7728  p = false≢true (sym (cong lower p))
  cut7728 : Adequate {ℓ} ((op (op (op (op (var 0) (var 0)) (var 0)) (var 1)) (op (var 2) (var 2))) , (var 0)) → ⊥
  cut7728  adequate = bad7728  (Adequate.valid adequate Two boolean env1)
  bad7729 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b0) b0) b0) (bop b1 b1)) b0 → ⊥
  bad7729  p = false≢true (sym (cong lower p))
  cut7729 : Adequate {ℓ} ((op (op (op (op (var 0) (var 0)) (var 0)) (var 1)) (op (var 2) (var 2))) , (var 1)) → ⊥
  cut7729  adequate = bad7729  (Adequate.valid adequate Two boolean env1)
  bad7730 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b0) b0) b1) (bop b0 b0)) b0 → ⊥
  bad7730  p = false≢true (sym (cong lower p))
  cut7730 : Adequate {ℓ} ((op (op (op (op (var 0) (var 0)) (var 0)) (var 1)) (op (var 2) (var 2))) , (var 2)) → ⊥
  cut7730  adequate = bad7730  (Adequate.valid adequate Two boolean env4)
  bad7731 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b0) b0) b0) (bop b0 b0)) b1 → ⊥
  bad7731  p = false≢true (cong lower p)
  cut7731 : Adequate {ℓ} ((op (op (op (op (var 0) (var 0)) (var 0)) (var 1)) (op (var 2) (var 2))) , (var 3)) → ⊥
  cut7731  adequate = bad7731  (Adequate.valid adequate Two boolean env5)
  env7 : ℕ → Two
  env7 zero = b0
  env7 (suc zero) = b0
  env7 (suc (suc zero)) = b1
  env7 (suc (suc (suc zero))) = b1
  env7 (suc (suc (suc (suc rest)))) = b0
  bad7732 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b0) b0) b0) (bop b1 b1)) b0 → ⊥
  bad7732  p = false≢true (sym (cong lower p))
  cut7732 : Adequate {ℓ} ((op (op (op (op (var 0) (var 0)) (var 0)) (var 1)) (op (var 2) (var 3))) , (var 0)) → ⊥
  cut7732  adequate = bad7732  (Adequate.valid adequate Two boolean env7)
  bad7733 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b0) b0) b0) (bop b1 b1)) b0 → ⊥
  bad7733  p = false≢true (sym (cong lower p))
  cut7733 : Adequate {ℓ} ((op (op (op (op (var 0) (var 0)) (var 0)) (var 1)) (op (var 2) (var 3))) , (var 1)) → ⊥
  cut7733  adequate = bad7733  (Adequate.valid adequate Two boolean env7)
  env8 : ℕ → Two
  env8 zero = b0
  env8 (suc zero) = b0
  env8 (suc (suc zero)) = b1
  env8 (suc (suc (suc zero))) = b0
  env8 (suc (suc (suc (suc rest)))) = b0
  bad7734 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b0) b0) b0) (bop b1 b0)) b1 → ⊥
  bad7734  p = false≢true (cong lower p)
  cut7734 : Adequate {ℓ} ((op (op (op (op (var 0) (var 0)) (var 0)) (var 1)) (op (var 2) (var 3))) , (var 2)) → ⊥
  cut7734  adequate = bad7734  (Adequate.valid adequate Two boolean env8)
  bad7735 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b0) b0) b0) (bop b0 b1)) b1 → ⊥
  bad7735  p = false≢true (cong lower p)
  cut7735 : Adequate {ℓ} ((op (op (op (op (var 0) (var 0)) (var 0)) (var 1)) (op (var 2) (var 3))) , (var 3)) → ⊥
  cut7735  adequate = bad7735  (Adequate.valid adequate Two boolean env5)
  env9 : ℕ → Two
  env9 zero = b0
  env9 (suc zero) = b0
  env9 (suc (suc zero)) = b0
  env9 (suc (suc (suc zero))) = b0
  env9 (suc (suc (suc (suc zero)))) = b1
  env9 (suc (suc (suc (suc (suc rest))))) = b0
  bad7736 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b0) b0) b0) (bop b0 b0)) b1 → ⊥
  bad7736  p = false≢true (cong lower p)
  cut7736 : Adequate {ℓ} ((op (op (op (op (var 0) (var 0)) (var 0)) (var 1)) (op (var 2) (var 3))) , (var 4)) → ⊥
  cut7736  adequate = bad7736  (Adequate.valid adequate Two boolean env9)
  holds7737 : (z0 z1 : A2) → (mul2 (mul2 (mul2 (mul2 z0 z0) z1) z0) (mul2 z0 z0)) ≡ z0
  holds7737 z0 z1 = refl
  cut7737 : Adequate {ℓ} ((op (op (op (op (var 0) (var 0)) (var 1)) (var 0)) (op (var 0) (var 0))) , (var 0)) → ⊥
  cut7737  = reject2 ((op (op (op (op (var 0) (var 0)) (var 1)) (var 0)) (op (var 0) (var 0))) , (var 0)) (λ env → holds7737 (env 0) (env 1))
  bad7738 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b0) b1) b0) (bop b0 b0)) b1 → ⊥
  bad7738  p = false≢true (cong lower p)
  cut7738 : Adequate {ℓ} ((op (op (op (op (var 0) (var 0)) (var 1)) (var 0)) (op (var 0) (var 0))) , (var 1)) → ⊥
  cut7738  adequate = bad7738  (Adequate.valid adequate Two boolean env0)
  bad7739 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b0) b0) b0) (bop b0 b0)) b1 → ⊥
  bad7739  p = false≢true (cong lower p)
  cut7739 : Adequate {ℓ} ((op (op (op (op (var 0) (var 0)) (var 1)) (var 0)) (op (var 0) (var 0))) , (var 2)) → ⊥
  cut7739  adequate = bad7739  (Adequate.valid adequate Two boolean env1)
  holds7740 : (z0 z1 : A2) → (mul2 (mul2 (mul2 (mul2 z0 z0) z1) z0) (mul2 z0 z1)) ≡ z0
  holds7740 z0 z1 = refl
  cut7740 : Adequate {ℓ} ((op (op (op (op (var 0) (var 0)) (var 1)) (var 0)) (op (var 0) (var 1))) , (var 0)) → ⊥
  cut7740  = reject2 ((op (op (op (op (var 0) (var 0)) (var 1)) (var 0)) (op (var 0) (var 1))) , (var 0)) (λ env → holds7740 (env 0) (env 1))
  bad7741 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b0) b1) b0) (bop b0 b1)) b1 → ⊥
  bad7741  p = false≢true (cong lower p)
  cut7741 : Adequate {ℓ} ((op (op (op (op (var 0) (var 0)) (var 1)) (var 0)) (op (var 0) (var 1))) , (var 1)) → ⊥
  cut7741  adequate = bad7741  (Adequate.valid adequate Two boolean env0)
  bad7742 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b0) b0) b0) (bop b0 b0)) b1 → ⊥
  bad7742  p = false≢true (cong lower p)
  cut7742 : Adequate {ℓ} ((op (op (op (op (var 0) (var 0)) (var 1)) (var 0)) (op (var 0) (var 1))) , (var 2)) → ⊥
  cut7742  adequate = bad7742  (Adequate.valid adequate Two boolean env1)
  holds7743 : (z0 z1 z2 : A2) → (mul2 (mul2 (mul2 (mul2 z0 z0) z1) z0) (mul2 z0 z2)) ≡ z0
  holds7743 z0 z1 z2 = refl
  cut7743 : Adequate {ℓ} ((op (op (op (op (var 0) (var 0)) (var 1)) (var 0)) (op (var 0) (var 2))) , (var 0)) → ⊥
  cut7743  = reject2 ((op (op (op (op (var 0) (var 0)) (var 1)) (var 0)) (op (var 0) (var 2))) , (var 0)) (λ env → holds7743 (env 0) (env 1) (env 2))
  bad7744 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b0) b1) b0) (bop b0 b0)) b1 → ⊥
  bad7744  p = false≢true (cong lower p)
  cut7744 : Adequate {ℓ} ((op (op (op (op (var 0) (var 0)) (var 1)) (var 0)) (op (var 0) (var 2))) , (var 1)) → ⊥
  cut7744  adequate = bad7744  (Adequate.valid adequate Two boolean env4)
  bad7745 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b0) b0) b0) (bop b0 b1)) b1 → ⊥
  bad7745  p = false≢true (cong lower p)
  cut7745 : Adequate {ℓ} ((op (op (op (op (var 0) (var 0)) (var 1)) (var 0)) (op (var 0) (var 2))) , (var 2)) → ⊥
  cut7745  adequate = bad7745  (Adequate.valid adequate Two boolean env1)
  bad7746 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b0) b0) b0) (bop b0 b0)) b1 → ⊥
  bad7746  p = false≢true (cong lower p)
  cut7746 : Adequate {ℓ} ((op (op (op (op (var 0) (var 0)) (var 1)) (var 0)) (op (var 0) (var 2))) , (var 3)) → ⊥
  cut7746  adequate = bad7746  (Adequate.valid adequate Two boolean env5)
  holds7747 : (z0 z1 : A2) → (mul2 (mul2 (mul2 (mul2 z0 z0) z1) z0) (mul2 z1 z0)) ≡ z0
  holds7747 z0 z1 = refl
  cut7747 : Adequate {ℓ} ((op (op (op (op (var 0) (var 0)) (var 1)) (var 0)) (op (var 1) (var 0))) , (var 0)) → ⊥
  cut7747  = reject2 ((op (op (op (op (var 0) (var 0)) (var 1)) (var 0)) (op (var 1) (var 0))) , (var 0)) (λ env → holds7747 (env 0) (env 1))
  bad7748 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b0) b1) b0) (bop b1 b0)) b1 → ⊥
  bad7748  p = false≢true (cong lower p)
  cut7748 : Adequate {ℓ} ((op (op (op (op (var 0) (var 0)) (var 1)) (var 0)) (op (var 1) (var 0))) , (var 1)) → ⊥
  cut7748  adequate = bad7748  (Adequate.valid adequate Two boolean env0)
  bad7749 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b0) b0) b0) (bop b0 b0)) b1 → ⊥
  bad7749  p = false≢true (cong lower p)
  cut7749 : Adequate {ℓ} ((op (op (op (op (var 0) (var 0)) (var 1)) (var 0)) (op (var 1) (var 0))) , (var 2)) → ⊥
  cut7749  adequate = bad7749  (Adequate.valid adequate Two boolean env1)
  bad7750 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b0) b1) b0) (bop b1 b1)) b0 → ⊥
  bad7750  p = false≢true (sym (cong lower p))
  cut7750 : Adequate {ℓ} ((op (op (op (op (var 0) (var 0)) (var 1)) (var 0)) (op (var 1) (var 1))) , (var 0)) → ⊥
  cut7750  adequate = bad7750  (Adequate.valid adequate Two boolean env0)
  bad7751 : PathP (λ _ → Two) (bop (bop (bop (bop b1 b1) b0) b1) (bop b0 b0)) b0 → ⊥
  bad7751  p = false≢true (sym (cong lower p))
  cut7751 : Adequate {ℓ} ((op (op (op (op (var 0) (var 0)) (var 1)) (var 0)) (op (var 1) (var 1))) , (var 1)) → ⊥
  cut7751  adequate = bad7751  (Adequate.valid adequate Two boolean env2)
  bad7752 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b0) b0) b0) (bop b0 b0)) b1 → ⊥
  bad7752  p = false≢true (cong lower p)
  cut7752 : Adequate {ℓ} ((op (op (op (op (var 0) (var 0)) (var 1)) (var 0)) (op (var 1) (var 1))) , (var 2)) → ⊥
  cut7752  adequate = bad7752  (Adequate.valid adequate Two boolean env1)
  bad7753 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b0) b1) b0) (bop b1 b1)) b0 → ⊥
  bad7753  p = false≢true (sym (cong lower p))
  cut7753 : Adequate {ℓ} ((op (op (op (op (var 0) (var 0)) (var 1)) (var 0)) (op (var 1) (var 2))) , (var 0)) → ⊥
  cut7753  adequate = bad7753  (Adequate.valid adequate Two boolean env3)
  bad7754 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b0) b1) b0) (bop b1 b0)) b1 → ⊥
  bad7754  p = false≢true (cong lower p)
  cut7754 : Adequate {ℓ} ((op (op (op (op (var 0) (var 0)) (var 1)) (var 0)) (op (var 1) (var 2))) , (var 1)) → ⊥
  cut7754  adequate = bad7754  (Adequate.valid adequate Two boolean env4)
  bad7755 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b0) b0) b0) (bop b0 b1)) b1 → ⊥
  bad7755  p = false≢true (cong lower p)
  cut7755 : Adequate {ℓ} ((op (op (op (op (var 0) (var 0)) (var 1)) (var 0)) (op (var 1) (var 2))) , (var 2)) → ⊥
  cut7755  adequate = bad7755  (Adequate.valid adequate Two boolean env1)
  bad7756 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b0) b0) b0) (bop b0 b0)) b1 → ⊥
  bad7756  p = false≢true (cong lower p)
  cut7756 : Adequate {ℓ} ((op (op (op (op (var 0) (var 0)) (var 1)) (var 0)) (op (var 1) (var 2))) , (var 3)) → ⊥
  cut7756  adequate = bad7756  (Adequate.valid adequate Two boolean env5)
  holds7757 : (z0 z1 z2 : A2) → (mul2 (mul2 (mul2 (mul2 z0 z0) z1) z0) (mul2 z2 z0)) ≡ z0
  holds7757 z0 z1 z2 = refl
  cut7757 : Adequate {ℓ} ((op (op (op (op (var 0) (var 0)) (var 1)) (var 0)) (op (var 2) (var 0))) , (var 0)) → ⊥
  cut7757  = reject2 ((op (op (op (op (var 0) (var 0)) (var 1)) (var 0)) (op (var 2) (var 0))) , (var 0)) (λ env → holds7757 (env 0) (env 1) (env 2))
  bad7758 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b0) b1) b0) (bop b0 b0)) b1 → ⊥
  bad7758  p = false≢true (cong lower p)
  cut7758 : Adequate {ℓ} ((op (op (op (op (var 0) (var 0)) (var 1)) (var 0)) (op (var 2) (var 0))) , (var 1)) → ⊥
  cut7758  adequate = bad7758  (Adequate.valid adequate Two boolean env4)
  bad7759 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b0) b0) b0) (bop b1 b0)) b1 → ⊥
  bad7759  p = false≢true (cong lower p)
  cut7759 : Adequate {ℓ} ((op (op (op (op (var 0) (var 0)) (var 1)) (var 0)) (op (var 2) (var 0))) , (var 2)) → ⊥
  cut7759  adequate = bad7759  (Adequate.valid adequate Two boolean env1)
  bad7760 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b0) b0) b0) (bop b0 b0)) b1 → ⊥
  bad7760  p = false≢true (cong lower p)
  cut7760 : Adequate {ℓ} ((op (op (op (op (var 0) (var 0)) (var 1)) (var 0)) (op (var 2) (var 0))) , (var 3)) → ⊥
  cut7760  adequate = bad7760  (Adequate.valid adequate Two boolean env5)
  bad7761 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b0) b1) b0) (bop b1 b1)) b0 → ⊥
  bad7761  p = false≢true (sym (cong lower p))
  cut7761 : Adequate {ℓ} ((op (op (op (op (var 0) (var 0)) (var 1)) (var 0)) (op (var 2) (var 1))) , (var 0)) → ⊥
  cut7761  adequate = bad7761  (Adequate.valid adequate Two boolean env3)
  bad7762 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b0) b1) b0) (bop b0 b1)) b1 → ⊥
  bad7762  p = false≢true (cong lower p)
  cut7762 : Adequate {ℓ} ((op (op (op (op (var 0) (var 0)) (var 1)) (var 0)) (op (var 2) (var 1))) , (var 1)) → ⊥
  cut7762  adequate = bad7762  (Adequate.valid adequate Two boolean env4)
  bad7763 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b0) b0) b0) (bop b1 b0)) b1 → ⊥
  bad7763  p = false≢true (cong lower p)
  cut7763 : Adequate {ℓ} ((op (op (op (op (var 0) (var 0)) (var 1)) (var 0)) (op (var 2) (var 1))) , (var 2)) → ⊥
  cut7763  adequate = bad7763  (Adequate.valid adequate Two boolean env1)
  bad7764 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b0) b0) b0) (bop b0 b0)) b1 → ⊥
  bad7764  p = false≢true (cong lower p)
  cut7764 : Adequate {ℓ} ((op (op (op (op (var 0) (var 0)) (var 1)) (var 0)) (op (var 2) (var 1))) , (var 3)) → ⊥
  cut7764  adequate = bad7764  (Adequate.valid adequate Two boolean env5)
  bad7765 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b0) b0) b0) (bop b1 b1)) b0 → ⊥
  bad7765  p = false≢true (sym (cong lower p))
  cut7765 : Adequate {ℓ} ((op (op (op (op (var 0) (var 0)) (var 1)) (var 0)) (op (var 2) (var 2))) , (var 0)) → ⊥
  cut7765  adequate = bad7765  (Adequate.valid adequate Two boolean env1)
  bad7766 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b0) b0) b0) (bop b1 b1)) b0 → ⊥
  bad7766  p = false≢true (sym (cong lower p))
  cut7766 : Adequate {ℓ} ((op (op (op (op (var 0) (var 0)) (var 1)) (var 0)) (op (var 2) (var 2))) , (var 1)) → ⊥
  cut7766  adequate = bad7766  (Adequate.valid adequate Two boolean env1)
  env10 : ℕ → Two
  env10 zero = b1
  env10 (suc zero) = b0
  env10 (suc (suc zero)) = b0
  env10 (suc (suc (suc rest))) = b0
  bad7767 : PathP (λ _ → Two) (bop (bop (bop (bop b1 b1) b0) b1) (bop b0 b0)) b0 → ⊥
  bad7767  p = false≢true (sym (cong lower p))
  cut7767 : Adequate {ℓ} ((op (op (op (op (var 0) (var 0)) (var 1)) (var 0)) (op (var 2) (var 2))) , (var 2)) → ⊥
  cut7767  adequate = bad7767  (Adequate.valid adequate Two boolean env10)
  bad7768 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b0) b0) b0) (bop b0 b0)) b1 → ⊥
  bad7768  p = false≢true (cong lower p)
  cut7768 : Adequate {ℓ} ((op (op (op (op (var 0) (var 0)) (var 1)) (var 0)) (op (var 2) (var 2))) , (var 3)) → ⊥
  cut7768  adequate = bad7768  (Adequate.valid adequate Two boolean env5)
  bad7769 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b0) b0) b0) (bop b1 b1)) b0 → ⊥
  bad7769  p = false≢true (sym (cong lower p))
  cut7769 : Adequate {ℓ} ((op (op (op (op (var 0) (var 0)) (var 1)) (var 0)) (op (var 2) (var 3))) , (var 0)) → ⊥
  cut7769  adequate = bad7769  (Adequate.valid adequate Two boolean env7)
  bad7770 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b0) b0) b0) (bop b1 b1)) b0 → ⊥
  bad7770  p = false≢true (sym (cong lower p))
  cut7770 : Adequate {ℓ} ((op (op (op (op (var 0) (var 0)) (var 1)) (var 0)) (op (var 2) (var 3))) , (var 1)) → ⊥
  cut7770  adequate = bad7770  (Adequate.valid adequate Two boolean env7)
  bad7771 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b0) b0) b0) (bop b1 b0)) b1 → ⊥
  bad7771  p = false≢true (cong lower p)
  cut7771 : Adequate {ℓ} ((op (op (op (op (var 0) (var 0)) (var 1)) (var 0)) (op (var 2) (var 3))) , (var 2)) → ⊥
  cut7771  adequate = bad7771  (Adequate.valid adequate Two boolean env8)
  bad7772 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b0) b0) b0) (bop b0 b1)) b1 → ⊥
  bad7772  p = false≢true (cong lower p)
  cut7772 : Adequate {ℓ} ((op (op (op (op (var 0) (var 0)) (var 1)) (var 0)) (op (var 2) (var 3))) , (var 3)) → ⊥
  cut7772  adequate = bad7772  (Adequate.valid adequate Two boolean env5)
  bad7773 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b0) b0) b0) (bop b0 b0)) b1 → ⊥
  bad7773  p = false≢true (cong lower p)
  cut7773 : Adequate {ℓ} ((op (op (op (op (var 0) (var 0)) (var 1)) (var 0)) (op (var 2) (var 3))) , (var 4)) → ⊥
  cut7773  adequate = bad7773  (Adequate.valid adequate Two boolean env9)
  holds7774 : (z0 z1 : A2) → (mul2 (mul2 (mul2 (mul2 z0 z0) z1) z1) (mul2 z0 z0)) ≡ z0
  holds7774 z0 z1 = refl
  cut7774 : Adequate {ℓ} ((op (op (op (op (var 0) (var 0)) (var 1)) (var 1)) (op (var 0) (var 0))) , (var 0)) → ⊥
  cut7774  = reject2 ((op (op (op (op (var 0) (var 0)) (var 1)) (var 1)) (op (var 0) (var 0))) , (var 0)) (λ env → holds7774 (env 0) (env 1))
  bad7775 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b0) b1) b1) (bop b0 b0)) b1 → ⊥
  bad7775  p = false≢true (cong lower p)
  cut7775 : Adequate {ℓ} ((op (op (op (op (var 0) (var 0)) (var 1)) (var 1)) (op (var 0) (var 0))) , (var 1)) → ⊥
  cut7775  adequate = bad7775  (Adequate.valid adequate Two boolean env0)
  bad7776 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b0) b0) b0) (bop b0 b0)) b1 → ⊥
  bad7776  p = false≢true (cong lower p)
  cut7776 : Adequate {ℓ} ((op (op (op (op (var 0) (var 0)) (var 1)) (var 1)) (op (var 0) (var 0))) , (var 2)) → ⊥
  cut7776  adequate = bad7776  (Adequate.valid adequate Two boolean env1)
  bad7777 : PathP (λ _ → Two) (bop (bop (bop (bop b1 b1) b0) b0) (bop b1 b0)) b1 → ⊥
  bad7777  p = false≢true (cong lower p)
  cut7777 : Adequate {ℓ} ((op (op (op (op (var 0) (var 0)) (var 1)) (var 1)) (op (var 0) (var 1))) , (var 0)) → ⊥
  cut7777  adequate = bad7777  (Adequate.valid adequate Two boolean env2)
  bad7778 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b0) b1) b1) (bop b0 b1)) b1 → ⊥
  bad7778  p = false≢true (cong lower p)
  cut7778 : Adequate {ℓ} ((op (op (op (op (var 0) (var 0)) (var 1)) (var 1)) (op (var 0) (var 1))) , (var 1)) → ⊥
  cut7778  adequate = bad7778  (Adequate.valid adequate Two boolean env0)
  bad7779 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b0) b0) b0) (bop b0 b0)) b1 → ⊥
  bad7779  p = false≢true (cong lower p)
  cut7779 : Adequate {ℓ} ((op (op (op (op (var 0) (var 0)) (var 1)) (var 1)) (op (var 0) (var 1))) , (var 2)) → ⊥
  cut7779  adequate = bad7779  (Adequate.valid adequate Two boolean env1)
  bad7780 : PathP (λ _ → Two) (bop (bop (bop (bop b1 b1) b0) b0) (bop b1 b0)) b1 → ⊥
  bad7780  p = false≢true (cong lower p)
  cut7780 : Adequate {ℓ} ((op (op (op (op (var 0) (var 0)) (var 1)) (var 1)) (op (var 0) (var 2))) , (var 0)) → ⊥
  cut7780  adequate = bad7780  (Adequate.valid adequate Two boolean env10)
  bad7781 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b0) b1) b1) (bop b0 b0)) b1 → ⊥
  bad7781  p = false≢true (cong lower p)
  cut7781 : Adequate {ℓ} ((op (op (op (op (var 0) (var 0)) (var 1)) (var 1)) (op (var 0) (var 2))) , (var 1)) → ⊥
  cut7781  adequate = bad7781  (Adequate.valid adequate Two boolean env4)
  bad7782 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b0) b0) b0) (bop b0 b1)) b1 → ⊥
  bad7782  p = false≢true (cong lower p)
  cut7782 : Adequate {ℓ} ((op (op (op (op (var 0) (var 0)) (var 1)) (var 1)) (op (var 0) (var 2))) , (var 2)) → ⊥
  cut7782  adequate = bad7782  (Adequate.valid adequate Two boolean env1)
  bad7783 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b0) b0) b0) (bop b0 b0)) b1 → ⊥
  bad7783  p = false≢true (cong lower p)
  cut7783 : Adequate {ℓ} ((op (op (op (op (var 0) (var 0)) (var 1)) (var 1)) (op (var 0) (var 2))) , (var 3)) → ⊥
  cut7783  adequate = bad7783  (Adequate.valid adequate Two boolean env5)
  bad7784 : PathP (λ _ → Two) (bop (bop (bop (bop b1 b1) b0) b0) (bop b0 b1)) b1 → ⊥
  bad7784  p = false≢true (cong lower p)
  cut7784 : Adequate {ℓ} ((op (op (op (op (var 0) (var 0)) (var 1)) (var 1)) (op (var 1) (var 0))) , (var 0)) → ⊥
  cut7784  adequate = bad7784  (Adequate.valid adequate Two boolean env2)
  bad7785 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b0) b1) b1) (bop b1 b0)) b1 → ⊥
  bad7785  p = false≢true (cong lower p)
  cut7785 : Adequate {ℓ} ((op (op (op (op (var 0) (var 0)) (var 1)) (var 1)) (op (var 1) (var 0))) , (var 1)) → ⊥
  cut7785  adequate = bad7785  (Adequate.valid adequate Two boolean env0)
  bad7786 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b0) b0) b0) (bop b0 b0)) b1 → ⊥
  bad7786  p = false≢true (cong lower p)
  cut7786 : Adequate {ℓ} ((op (op (op (op (var 0) (var 0)) (var 1)) (var 1)) (op (var 1) (var 0))) , (var 2)) → ⊥
  cut7786  adequate = bad7786  (Adequate.valid adequate Two boolean env1)
  bad7787 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b0) b1) b1) (bop b1 b1)) b0 → ⊥
  bad7787  p = false≢true (sym (cong lower p))
  cut7787 : Adequate {ℓ} ((op (op (op (op (var 0) (var 0)) (var 1)) (var 1)) (op (var 1) (var 1))) , (var 0)) → ⊥
  cut7787  adequate = bad7787  (Adequate.valid adequate Two boolean env0)
  holds7788 : (z0 z1 : A3) → (mul3 (mul3 (mul3 (mul3 z0 z0) z1) z1) (mul3 z1 z1)) ≡ z1
  holds7788 z0 z1 = refl
  cut7788 : Adequate {ℓ} ((op (op (op (op (var 0) (var 0)) (var 1)) (var 1)) (op (var 1) (var 1))) , (var 1)) → ⊥
  cut7788  = reject3 ((op (op (op (op (var 0) (var 0)) (var 1)) (var 1)) (op (var 1) (var 1))) , (var 1)) (λ env → holds7788 (env 0) (env 1))
  bad7789 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b0) b0) b0) (bop b0 b0)) b1 → ⊥
  bad7789  p = false≢true (cong lower p)
  cut7789 : Adequate {ℓ} ((op (op (op (op (var 0) (var 0)) (var 1)) (var 1)) (op (var 1) (var 1))) , (var 2)) → ⊥
  cut7789  adequate = bad7789  (Adequate.valid adequate Two boolean env1)
  bad7790 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b0) b1) b1) (bop b1 b1)) b0 → ⊥
  bad7790  p = false≢true (sym (cong lower p))
  cut7790 : Adequate {ℓ} ((op (op (op (op (var 0) (var 0)) (var 1)) (var 1)) (op (var 1) (var 2))) , (var 0)) → ⊥
  cut7790  adequate = bad7790  (Adequate.valid adequate Two boolean env3)
  bad7791 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b0) b1) b1) (bop b1 b0)) b1 → ⊥
  bad7791  p = false≢true (cong lower p)
  cut7791 : Adequate {ℓ} ((op (op (op (op (var 0) (var 0)) (var 1)) (var 1)) (op (var 1) (var 2))) , (var 1)) → ⊥
  cut7791  adequate = bad7791  (Adequate.valid adequate Two boolean env4)
  bad7792 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b0) b0) b0) (bop b0 b1)) b1 → ⊥
  bad7792  p = false≢true (cong lower p)
  cut7792 : Adequate {ℓ} ((op (op (op (op (var 0) (var 0)) (var 1)) (var 1)) (op (var 1) (var 2))) , (var 2)) → ⊥
  cut7792  adequate = bad7792  (Adequate.valid adequate Two boolean env1)
  bad7793 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b0) b0) b0) (bop b0 b0)) b1 → ⊥
  bad7793  p = false≢true (cong lower p)
  cut7793 : Adequate {ℓ} ((op (op (op (op (var 0) (var 0)) (var 1)) (var 1)) (op (var 1) (var 2))) , (var 3)) → ⊥
  cut7793  adequate = bad7793  (Adequate.valid adequate Two boolean env5)
  bad7794 : PathP (λ _ → Two) (bop (bop (bop (bop b1 b1) b0) b0) (bop b0 b1)) b1 → ⊥
  bad7794  p = false≢true (cong lower p)
  cut7794 : Adequate {ℓ} ((op (op (op (op (var 0) (var 0)) (var 1)) (var 1)) (op (var 2) (var 0))) , (var 0)) → ⊥
  cut7794  adequate = bad7794  (Adequate.valid adequate Two boolean env10)
  bad7795 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b0) b1) b1) (bop b0 b0)) b1 → ⊥
  bad7795  p = false≢true (cong lower p)
  cut7795 : Adequate {ℓ} ((op (op (op (op (var 0) (var 0)) (var 1)) (var 1)) (op (var 2) (var 0))) , (var 1)) → ⊥
  cut7795  adequate = bad7795  (Adequate.valid adequate Two boolean env4)
  bad7796 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b0) b0) b0) (bop b1 b0)) b1 → ⊥
  bad7796  p = false≢true (cong lower p)
  cut7796 : Adequate {ℓ} ((op (op (op (op (var 0) (var 0)) (var 1)) (var 1)) (op (var 2) (var 0))) , (var 2)) → ⊥
  cut7796  adequate = bad7796  (Adequate.valid adequate Two boolean env1)
  bad7797 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b0) b0) b0) (bop b0 b0)) b1 → ⊥
  bad7797  p = false≢true (cong lower p)
  cut7797 : Adequate {ℓ} ((op (op (op (op (var 0) (var 0)) (var 1)) (var 1)) (op (var 2) (var 0))) , (var 3)) → ⊥
  cut7797  adequate = bad7797  (Adequate.valid adequate Two boolean env5)
  bad7798 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b0) b1) b1) (bop b1 b1)) b0 → ⊥
  bad7798  p = false≢true (sym (cong lower p))
  cut7798 : Adequate {ℓ} ((op (op (op (op (var 0) (var 0)) (var 1)) (var 1)) (op (var 2) (var 1))) , (var 0)) → ⊥
  cut7798  adequate = bad7798  (Adequate.valid adequate Two boolean env3)
  bad7799 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b0) b1) b1) (bop b0 b1)) b1 → ⊥
  bad7799  p = false≢true (cong lower p)
  cut7799 : Adequate {ℓ} ((op (op (op (op (var 0) (var 0)) (var 1)) (var 1)) (op (var 2) (var 1))) , (var 1)) → ⊥
  cut7799  adequate = bad7799  (Adequate.valid adequate Two boolean env4)
  bad7800 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b0) b0) b0) (bop b1 b0)) b1 → ⊥
  bad7800  p = false≢true (cong lower p)
  cut7800 : Adequate {ℓ} ((op (op (op (op (var 0) (var 0)) (var 1)) (var 1)) (op (var 2) (var 1))) , (var 2)) → ⊥
  cut7800  adequate = bad7800  (Adequate.valid adequate Two boolean env1)
  bad7801 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b0) b0) b0) (bop b0 b0)) b1 → ⊥
  bad7801  p = false≢true (cong lower p)
  cut7801 : Adequate {ℓ} ((op (op (op (op (var 0) (var 0)) (var 1)) (var 1)) (op (var 2) (var 1))) , (var 3)) → ⊥
  cut7801  adequate = bad7801  (Adequate.valid adequate Two boolean env5)
  bad7802 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b0) b0) b0) (bop b1 b1)) b0 → ⊥
  bad7802  p = false≢true (sym (cong lower p))
  cut7802 : Adequate {ℓ} ((op (op (op (op (var 0) (var 0)) (var 1)) (var 1)) (op (var 2) (var 2))) , (var 0)) → ⊥
  cut7802  adequate = bad7802  (Adequate.valid adequate Two boolean env1)
  bad7803 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b0) b0) b0) (bop b1 b1)) b0 → ⊥
  bad7803  p = false≢true (sym (cong lower p))
  cut7803 : Adequate {ℓ} ((op (op (op (op (var 0) (var 0)) (var 1)) (var 1)) (op (var 2) (var 2))) , (var 1)) → ⊥
  cut7803  adequate = bad7803  (Adequate.valid adequate Two boolean env1)
  env11 : ℕ → Two
  env11 zero = b1
  env11 (suc zero) = b1
  env11 (suc (suc zero)) = b0
  env11 (suc (suc (suc rest))) = b0
  bad7804 : PathP (λ _ → Two) (bop (bop (bop (bop b1 b1) b1) b1) (bop b0 b0)) b0 → ⊥
  bad7804  p = false≢true (sym (cong lower p))
  cut7804 : Adequate {ℓ} ((op (op (op (op (var 0) (var 0)) (var 1)) (var 1)) (op (var 2) (var 2))) , (var 2)) → ⊥
  cut7804  adequate = bad7804  (Adequate.valid adequate Two boolean env11)
  bad7805 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b0) b0) b0) (bop b0 b0)) b1 → ⊥
  bad7805  p = false≢true (cong lower p)
  cut7805 : Adequate {ℓ} ((op (op (op (op (var 0) (var 0)) (var 1)) (var 1)) (op (var 2) (var 2))) , (var 3)) → ⊥
  cut7805  adequate = bad7805  (Adequate.valid adequate Two boolean env5)
  bad7806 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b0) b0) b0) (bop b1 b1)) b0 → ⊥
  bad7806  p = false≢true (sym (cong lower p))
  cut7806 : Adequate {ℓ} ((op (op (op (op (var 0) (var 0)) (var 1)) (var 1)) (op (var 2) (var 3))) , (var 0)) → ⊥
  cut7806  adequate = bad7806  (Adequate.valid adequate Two boolean env7)
  bad7807 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b0) b0) b0) (bop b1 b1)) b0 → ⊥
  bad7807  p = false≢true (sym (cong lower p))
  cut7807 : Adequate {ℓ} ((op (op (op (op (var 0) (var 0)) (var 1)) (var 1)) (op (var 2) (var 3))) , (var 1)) → ⊥
  cut7807  adequate = bad7807  (Adequate.valid adequate Two boolean env7)
  bad7808 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b0) b0) b0) (bop b1 b0)) b1 → ⊥
  bad7808  p = false≢true (cong lower p)
  cut7808 : Adequate {ℓ} ((op (op (op (op (var 0) (var 0)) (var 1)) (var 1)) (op (var 2) (var 3))) , (var 2)) → ⊥
  cut7808  adequate = bad7808  (Adequate.valid adequate Two boolean env8)
  bad7809 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b0) b0) b0) (bop b0 b1)) b1 → ⊥
  bad7809  p = false≢true (cong lower p)
  cut7809 : Adequate {ℓ} ((op (op (op (op (var 0) (var 0)) (var 1)) (var 1)) (op (var 2) (var 3))) , (var 3)) → ⊥
  cut7809  adequate = bad7809  (Adequate.valid adequate Two boolean env5)
  bad7810 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b0) b0) b0) (bop b0 b0)) b1 → ⊥
  bad7810  p = false≢true (cong lower p)
  cut7810 : Adequate {ℓ} ((op (op (op (op (var 0) (var 0)) (var 1)) (var 1)) (op (var 2) (var 3))) , (var 4)) → ⊥
  cut7810  adequate = bad7810  (Adequate.valid adequate Two boolean env9)
  bad7811 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b0) b0) b1) (bop b0 b0)) b0 → ⊥
  bad7811  p = false≢true (sym (cong lower p))
  cut7811 : Adequate {ℓ} ((op (op (op (op (var 0) (var 0)) (var 1)) (var 2)) (op (var 0) (var 0))) , (var 0)) → ⊥
  cut7811  adequate = bad7811  (Adequate.valid adequate Two boolean env1)
  bad7812 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b0) b0) b1) (bop b0 b0)) b0 → ⊥
  bad7812  p = false≢true (sym (cong lower p))
  cut7812 : Adequate {ℓ} ((op (op (op (op (var 0) (var 0)) (var 1)) (var 2)) (op (var 0) (var 0))) , (var 1)) → ⊥
  cut7812  adequate = bad7812  (Adequate.valid adequate Two boolean env1)
  bad7813 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b0) b1) b1) (bop b0 b0)) b1 → ⊥
  bad7813  p = false≢true (cong lower p)
  cut7813 : Adequate {ℓ} ((op (op (op (op (var 0) (var 0)) (var 1)) (var 2)) (op (var 0) (var 0))) , (var 2)) → ⊥
  cut7813  adequate = bad7813  (Adequate.valid adequate Two boolean env3)
  bad7814 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b0) b0) b0) (bop b0 b0)) b1 → ⊥
  bad7814  p = false≢true (cong lower p)
  cut7814 : Adequate {ℓ} ((op (op (op (op (var 0) (var 0)) (var 1)) (var 2)) (op (var 0) (var 0))) , (var 3)) → ⊥
  cut7814  adequate = bad7814  (Adequate.valid adequate Two boolean env5)
  bad7815 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b0) b0) b1) (bop b0 b0)) b0 → ⊥
  bad7815  p = false≢true (sym (cong lower p))
  cut7815 : Adequate {ℓ} ((op (op (op (op (var 0) (var 0)) (var 1)) (var 2)) (op (var 0) (var 1))) , (var 0)) → ⊥
  cut7815  adequate = bad7815  (Adequate.valid adequate Two boolean env1)
  bad7816 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b0) b0) b1) (bop b0 b0)) b0 → ⊥
  bad7816  p = false≢true (sym (cong lower p))
  cut7816 : Adequate {ℓ} ((op (op (op (op (var 0) (var 0)) (var 1)) (var 2)) (op (var 0) (var 1))) , (var 1)) → ⊥
  cut7816  adequate = bad7816  (Adequate.valid adequate Two boolean env1)
  bad7817 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b0) b1) b1) (bop b0 b1)) b1 → ⊥
  bad7817  p = false≢true (cong lower p)
  cut7817 : Adequate {ℓ} ((op (op (op (op (var 0) (var 0)) (var 1)) (var 2)) (op (var 0) (var 1))) , (var 2)) → ⊥
  cut7817  adequate = bad7817  (Adequate.valid adequate Two boolean env3)
  bad7818 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b0) b0) b0) (bop b0 b0)) b1 → ⊥
  bad7818  p = false≢true (cong lower p)
  cut7818 : Adequate {ℓ} ((op (op (op (op (var 0) (var 0)) (var 1)) (var 2)) (op (var 0) (var 1))) , (var 3)) → ⊥
  cut7818  adequate = bad7818  (Adequate.valid adequate Two boolean env5)
  bad7819 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b0) b0) b1) (bop b0 b1)) b0 → ⊥
  bad7819  p = false≢true (sym (cong lower p))
  cut7819 : Adequate {ℓ} ((op (op (op (op (var 0) (var 0)) (var 1)) (var 2)) (op (var 0) (var 2))) , (var 0)) → ⊥
  cut7819  adequate = bad7819  (Adequate.valid adequate Two boolean env1)
  bad7820 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b0) b0) b1) (bop b0 b1)) b0 → ⊥
  bad7820  p = false≢true (sym (cong lower p))
  cut7820 : Adequate {ℓ} ((op (op (op (op (var 0) (var 0)) (var 1)) (var 2)) (op (var 0) (var 2))) , (var 1)) → ⊥
  cut7820  adequate = bad7820  (Adequate.valid adequate Two boolean env1)
  bad7821 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b0) b1) b1) (bop b0 b1)) b1 → ⊥
  bad7821  p = false≢true (cong lower p)
  cut7821 : Adequate {ℓ} ((op (op (op (op (var 0) (var 0)) (var 1)) (var 2)) (op (var 0) (var 2))) , (var 2)) → ⊥
  cut7821  adequate = bad7821  (Adequate.valid adequate Two boolean env3)
  bad7822 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b0) b0) b0) (bop b0 b0)) b1 → ⊥
  bad7822  p = false≢true (cong lower p)
  cut7822 : Adequate {ℓ} ((op (op (op (op (var 0) (var 0)) (var 1)) (var 2)) (op (var 0) (var 2))) , (var 3)) → ⊥
  cut7822  adequate = bad7822  (Adequate.valid adequate Two boolean env5)
  bad7823 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b0) b0) b1) (bop b0 b0)) b0 → ⊥
  bad7823  p = false≢true (sym (cong lower p))
  cut7823 : Adequate {ℓ} ((op (op (op (op (var 0) (var 0)) (var 1)) (var 2)) (op (var 0) (var 3))) , (var 0)) → ⊥
  cut7823  adequate = bad7823  (Adequate.valid adequate Two boolean env8)
  bad7824 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b0) b0) b1) (bop b0 b0)) b0 → ⊥
  bad7824  p = false≢true (sym (cong lower p))
  cut7824 : Adequate {ℓ} ((op (op (op (op (var 0) (var 0)) (var 1)) (var 2)) (op (var 0) (var 3))) , (var 1)) → ⊥
  cut7824  adequate = bad7824  (Adequate.valid adequate Two boolean env8)
  env12 : ℕ → Two
  env12 zero = b0
  env12 (suc zero) = b1
  env12 (suc (suc zero)) = b1
  env12 (suc (suc (suc zero))) = b0
  env12 (suc (suc (suc (suc rest)))) = b0
  bad7825 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b0) b1) b1) (bop b0 b0)) b1 → ⊥
  bad7825  p = false≢true (cong lower p)
  cut7825 : Adequate {ℓ} ((op (op (op (op (var 0) (var 0)) (var 1)) (var 2)) (op (var 0) (var 3))) , (var 2)) → ⊥
  cut7825  adequate = bad7825  (Adequate.valid adequate Two boolean env12)
  bad7826 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b0) b0) b0) (bop b0 b1)) b1 → ⊥
  bad7826  p = false≢true (cong lower p)
  cut7826 : Adequate {ℓ} ((op (op (op (op (var 0) (var 0)) (var 1)) (var 2)) (op (var 0) (var 3))) , (var 3)) → ⊥
  cut7826  adequate = bad7826  (Adequate.valid adequate Two boolean env5)
  bad7827 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b0) b0) b0) (bop b0 b0)) b1 → ⊥
  bad7827  p = false≢true (cong lower p)
  cut7827 : Adequate {ℓ} ((op (op (op (op (var 0) (var 0)) (var 1)) (var 2)) (op (var 0) (var 3))) , (var 4)) → ⊥
  cut7827  adequate = bad7827  (Adequate.valid adequate Two boolean env9)
  bad7828 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b0) b0) b1) (bop b0 b0)) b0 → ⊥
  bad7828  p = false≢true (sym (cong lower p))
  cut7828 : Adequate {ℓ} ((op (op (op (op (var 0) (var 0)) (var 1)) (var 2)) (op (var 1) (var 0))) , (var 0)) → ⊥
  cut7828  adequate = bad7828  (Adequate.valid adequate Two boolean env1)
  bad7829 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b0) b0) b1) (bop b0 b0)) b0 → ⊥
  bad7829  p = false≢true (sym (cong lower p))
  cut7829 : Adequate {ℓ} ((op (op (op (op (var 0) (var 0)) (var 1)) (var 2)) (op (var 1) (var 0))) , (var 1)) → ⊥
  cut7829  adequate = bad7829  (Adequate.valid adequate Two boolean env1)
  bad7830 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b0) b1) b1) (bop b1 b0)) b1 → ⊥
  bad7830  p = false≢true (cong lower p)
  cut7830 : Adequate {ℓ} ((op (op (op (op (var 0) (var 0)) (var 1)) (var 2)) (op (var 1) (var 0))) , (var 2)) → ⊥
  cut7830  adequate = bad7830  (Adequate.valid adequate Two boolean env3)
  bad7831 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b0) b0) b0) (bop b0 b0)) b1 → ⊥
  bad7831  p = false≢true (cong lower p)
  cut7831 : Adequate {ℓ} ((op (op (op (op (var 0) (var 0)) (var 1)) (var 2)) (op (var 1) (var 0))) , (var 3)) → ⊥
  cut7831  adequate = bad7831  (Adequate.valid adequate Two boolean env5)
  bad7832 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b0) b0) b1) (bop b0 b0)) b0 → ⊥
  bad7832  p = false≢true (sym (cong lower p))
  cut7832 : Adequate {ℓ} ((op (op (op (op (var 0) (var 0)) (var 1)) (var 2)) (op (var 1) (var 1))) , (var 0)) → ⊥
  cut7832  adequate = bad7832  (Adequate.valid adequate Two boolean env1)
  bad7833 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b0) b0) b1) (bop b0 b0)) b0 → ⊥
  bad7833  p = false≢true (sym (cong lower p))
  cut7833 : Adequate {ℓ} ((op (op (op (op (var 0) (var 0)) (var 1)) (var 2)) (op (var 1) (var 1))) , (var 1)) → ⊥
  cut7833  adequate = bad7833  (Adequate.valid adequate Two boolean env1)
  bad7834 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b0) b1) b0) (bop b1 b1)) b0 → ⊥
  bad7834  p = false≢true (sym (cong lower p))
  cut7834 : Adequate {ℓ} ((op (op (op (op (var 0) (var 0)) (var 1)) (var 2)) (op (var 1) (var 1))) , (var 2)) → ⊥
  cut7834  adequate = bad7834  (Adequate.valid adequate Two boolean env4)
  bad7835 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b0) b0) b0) (bop b0 b0)) b1 → ⊥
  bad7835  p = false≢true (cong lower p)
  cut7835 : Adequate {ℓ} ((op (op (op (op (var 0) (var 0)) (var 1)) (var 2)) (op (var 1) (var 1))) , (var 3)) → ⊥
  cut7835  adequate = bad7835  (Adequate.valid adequate Two boolean env5)
  bad7836 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b0) b0) b1) (bop b0 b1)) b0 → ⊥
  bad7836  p = false≢true (sym (cong lower p))
  cut7836 : Adequate {ℓ} ((op (op (op (op (var 0) (var 0)) (var 1)) (var 2)) (op (var 1) (var 2))) , (var 0)) → ⊥
  cut7836  adequate = bad7836  (Adequate.valid adequate Two boolean env1)
  bad7837 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b0) b0) b1) (bop b0 b1)) b0 → ⊥
  bad7837  p = false≢true (sym (cong lower p))
  cut7837 : Adequate {ℓ} ((op (op (op (op (var 0) (var 0)) (var 1)) (var 2)) (op (var 1) (var 2))) , (var 1)) → ⊥
  cut7837  adequate = bad7837  (Adequate.valid adequate Two boolean env1)
  holds7838 : (z0 z1 z2 : A3) → (mul3 (mul3 (mul3 (mul3 z0 z0) z1) z2) (mul3 z1 z2)) ≡ z2
  holds7838 z0 z1 z2 = refl
  cut7838 : Adequate {ℓ} ((op (op (op (op (var 0) (var 0)) (var 1)) (var 2)) (op (var 1) (var 2))) , (var 2)) → ⊥
  cut7838  = reject3 ((op (op (op (op (var 0) (var 0)) (var 1)) (var 2)) (op (var 1) (var 2))) , (var 2)) (λ env → holds7838 (env 0) (env 1) (env 2))
  bad7839 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b0) b0) b0) (bop b0 b0)) b1 → ⊥
  bad7839  p = false≢true (cong lower p)
  cut7839 : Adequate {ℓ} ((op (op (op (op (var 0) (var 0)) (var 1)) (var 2)) (op (var 1) (var 2))) , (var 3)) → ⊥
  cut7839  adequate = bad7839  (Adequate.valid adequate Two boolean env5)
  bad7840 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b0) b0) b1) (bop b0 b0)) b0 → ⊥
  bad7840  p = false≢true (sym (cong lower p))
  cut7840 : Adequate {ℓ} ((op (op (op (op (var 0) (var 0)) (var 1)) (var 2)) (op (var 1) (var 3))) , (var 0)) → ⊥
  cut7840  adequate = bad7840  (Adequate.valid adequate Two boolean env8)
  bad7841 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b0) b0) b1) (bop b0 b0)) b0 → ⊥
  bad7841  p = false≢true (sym (cong lower p))
  cut7841 : Adequate {ℓ} ((op (op (op (op (var 0) (var 0)) (var 1)) (var 2)) (op (var 1) (var 3))) , (var 1)) → ⊥
  cut7841  adequate = bad7841  (Adequate.valid adequate Two boolean env8)
  env13 : ℕ → Two
  env13 zero = b0
  env13 (suc zero) = b1
  env13 (suc (suc zero)) = b0
  env13 (suc (suc (suc zero))) = b1
  env13 (suc (suc (suc (suc rest)))) = b0
  bad7842 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b0) b1) b0) (bop b1 b1)) b0 → ⊥
  bad7842  p = false≢true (sym (cong lower p))
  cut7842 : Adequate {ℓ} ((op (op (op (op (var 0) (var 0)) (var 1)) (var 2)) (op (var 1) (var 3))) , (var 2)) → ⊥
  cut7842  adequate = bad7842  (Adequate.valid adequate Two boolean env13)
  bad7843 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b0) b0) b0) (bop b0 b1)) b1 → ⊥
  bad7843  p = false≢true (cong lower p)
  cut7843 : Adequate {ℓ} ((op (op (op (op (var 0) (var 0)) (var 1)) (var 2)) (op (var 1) (var 3))) , (var 3)) → ⊥
  cut7843  adequate = bad7843  (Adequate.valid adequate Two boolean env5)
  bad7844 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b0) b0) b0) (bop b0 b0)) b1 → ⊥
  bad7844  p = false≢true (cong lower p)
  cut7844 : Adequate {ℓ} ((op (op (op (op (var 0) (var 0)) (var 1)) (var 2)) (op (var 1) (var 3))) , (var 4)) → ⊥
  cut7844  adequate = bad7844  (Adequate.valid adequate Two boolean env9)
  bad7845 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b0) b0) b1) (bop b1 b0)) b0 → ⊥
  bad7845  p = false≢true (sym (cong lower p))
  cut7845 : Adequate {ℓ} ((op (op (op (op (var 0) (var 0)) (var 1)) (var 2)) (op (var 2) (var 0))) , (var 0)) → ⊥
  cut7845  adequate = bad7845  (Adequate.valid adequate Two boolean env1)
  bad7846 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b0) b0) b1) (bop b1 b0)) b0 → ⊥
  bad7846  p = false≢true (sym (cong lower p))
  cut7846 : Adequate {ℓ} ((op (op (op (op (var 0) (var 0)) (var 1)) (var 2)) (op (var 2) (var 0))) , (var 1)) → ⊥
  cut7846  adequate = bad7846  (Adequate.valid adequate Two boolean env1)
  bad7847 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b0) b1) b1) (bop b1 b0)) b1 → ⊥
  bad7847  p = false≢true (cong lower p)
  cut7847 : Adequate {ℓ} ((op (op (op (op (var 0) (var 0)) (var 1)) (var 2)) (op (var 2) (var 0))) , (var 2)) → ⊥
  cut7847  adequate = bad7847  (Adequate.valid adequate Two boolean env3)
  bad7848 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b0) b0) b0) (bop b0 b0)) b1 → ⊥
  bad7848  p = false≢true (cong lower p)
  cut7848 : Adequate {ℓ} ((op (op (op (op (var 0) (var 0)) (var 1)) (var 2)) (op (var 2) (var 0))) , (var 3)) → ⊥
  cut7848  adequate = bad7848  (Adequate.valid adequate Two boolean env5)
  bad7849 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b0) b0) b1) (bop b1 b0)) b0 → ⊥
  bad7849  p = false≢true (sym (cong lower p))
  cut7849 : Adequate {ℓ} ((op (op (op (op (var 0) (var 0)) (var 1)) (var 2)) (op (var 2) (var 1))) , (var 0)) → ⊥
  cut7849  adequate = bad7849  (Adequate.valid adequate Two boolean env1)
  bad7850 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b0) b0) b1) (bop b1 b0)) b0 → ⊥
  bad7850  p = false≢true (sym (cong lower p))
  cut7850 : Adequate {ℓ} ((op (op (op (op (var 0) (var 0)) (var 1)) (var 2)) (op (var 2) (var 1))) , (var 1)) → ⊥
  cut7850  adequate = bad7850  (Adequate.valid adequate Two boolean env1)
  holds7851 : (z0 z1 z2 : A9) → (mul9 (mul9 (mul9 (mul9 z0 z0) z1) z2) (mul9 z2 z1)) ≡ z2
  holds7851 m9c0 m9c0 m9c0 = refl
  holds7851 m9c0 m9c0 m9c1 = refl
  holds7851 m9c0 m9c0 m9c2 = refl
  holds7851 m9c0 m9c1 m9c0 = refl
  holds7851 m9c0 m9c1 m9c1 = refl
  holds7851 m9c0 m9c1 m9c2 = refl
  holds7851 m9c0 m9c2 m9c0 = refl
  holds7851 m9c0 m9c2 m9c1 = refl
  holds7851 m9c0 m9c2 m9c2 = refl
  holds7851 m9c1 m9c0 m9c0 = refl
  holds7851 m9c1 m9c0 m9c1 = refl
  holds7851 m9c1 m9c0 m9c2 = refl
  holds7851 m9c1 m9c1 m9c0 = refl
  holds7851 m9c1 m9c1 m9c1 = refl
  holds7851 m9c1 m9c1 m9c2 = refl
  holds7851 m9c1 m9c2 m9c0 = refl
  holds7851 m9c1 m9c2 m9c1 = refl
  holds7851 m9c1 m9c2 m9c2 = refl
  holds7851 m9c2 m9c0 m9c0 = refl
  holds7851 m9c2 m9c0 m9c1 = refl
  holds7851 m9c2 m9c0 m9c2 = refl
  holds7851 m9c2 m9c1 m9c0 = refl
  holds7851 m9c2 m9c1 m9c1 = refl
  holds7851 m9c2 m9c1 m9c2 = refl
  holds7851 m9c2 m9c2 m9c0 = refl
  holds7851 m9c2 m9c2 m9c1 = refl
  holds7851 m9c2 m9c2 m9c2 = refl
  cut7851 : Adequate {ℓ} ((op (op (op (op (var 0) (var 0)) (var 1)) (var 2)) (op (var 2) (var 1))) , (var 2)) → ⊥
  cut7851  = reject9 ((op (op (op (op (var 0) (var 0)) (var 1)) (var 2)) (op (var 2) (var 1))) , (var 2)) (λ env → holds7851 (env 0) (env 1) (env 2))
  bad7852 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b0) b0) b0) (bop b0 b0)) b1 → ⊥
  bad7852  p = false≢true (cong lower p)
  cut7852 : Adequate {ℓ} ((op (op (op (op (var 0) (var 0)) (var 1)) (var 2)) (op (var 2) (var 1))) , (var 3)) → ⊥
  cut7852  adequate = bad7852  (Adequate.valid adequate Two boolean env5)
  bad7853 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b0) b0) b1) (bop b1 b1)) b0 → ⊥
  bad7853  p = false≢true (sym (cong lower p))
  cut7853 : Adequate {ℓ} ((op (op (op (op (var 0) (var 0)) (var 1)) (var 2)) (op (var 2) (var 2))) , (var 0)) → ⊥
  cut7853  adequate = bad7853  (Adequate.valid adequate Two boolean env1)
  bad7854 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b0) b0) b1) (bop b1 b1)) b0 → ⊥
  bad7854  p = false≢true (sym (cong lower p))
  cut7854 : Adequate {ℓ} ((op (op (op (op (var 0) (var 0)) (var 1)) (var 2)) (op (var 2) (var 2))) , (var 1)) → ⊥
  cut7854  adequate = bad7854  (Adequate.valid adequate Two boolean env1)
  holds7855 : (z0 z1 z2 : A3) → (mul3 (mul3 (mul3 (mul3 z0 z0) z1) z2) (mul3 z2 z2)) ≡ z2
  holds7855 z0 z1 z2 = refl
  cut7855 : Adequate {ℓ} ((op (op (op (op (var 0) (var 0)) (var 1)) (var 2)) (op (var 2) (var 2))) , (var 2)) → ⊥
  cut7855  = reject3 ((op (op (op (op (var 0) (var 0)) (var 1)) (var 2)) (op (var 2) (var 2))) , (var 2)) (λ env → holds7855 (env 0) (env 1) (env 2))
  bad7856 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b0) b0) b0) (bop b0 b0)) b1 → ⊥
  bad7856  p = false≢true (cong lower p)
  cut7856 : Adequate {ℓ} ((op (op (op (op (var 0) (var 0)) (var 1)) (var 2)) (op (var 2) (var 2))) , (var 3)) → ⊥
  cut7856  adequate = bad7856  (Adequate.valid adequate Two boolean env5)
  bad7857 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b0) b0) b1) (bop b1 b0)) b0 → ⊥
  bad7857  p = false≢true (sym (cong lower p))
  cut7857 : Adequate {ℓ} ((op (op (op (op (var 0) (var 0)) (var 1)) (var 2)) (op (var 2) (var 3))) , (var 0)) → ⊥
  cut7857  adequate = bad7857  (Adequate.valid adequate Two boolean env8)
  bad7858 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b0) b0) b1) (bop b1 b0)) b0 → ⊥
  bad7858  p = false≢true (sym (cong lower p))
  cut7858 : Adequate {ℓ} ((op (op (op (op (var 0) (var 0)) (var 1)) (var 2)) (op (var 2) (var 3))) , (var 1)) → ⊥
  cut7858  adequate = bad7858  (Adequate.valid adequate Two boolean env8)
  bad7859 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b0) b1) b1) (bop b1 b0)) b1 → ⊥
  bad7859  p = false≢true (cong lower p)
  cut7859 : Adequate {ℓ} ((op (op (op (op (var 0) (var 0)) (var 1)) (var 2)) (op (var 2) (var 3))) , (var 2)) → ⊥
  cut7859  adequate = bad7859  (Adequate.valid adequate Two boolean env12)
  bad7860 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b0) b0) b0) (bop b0 b1)) b1 → ⊥
  bad7860  p = false≢true (cong lower p)
  cut7860 : Adequate {ℓ} ((op (op (op (op (var 0) (var 0)) (var 1)) (var 2)) (op (var 2) (var 3))) , (var 3)) → ⊥
  cut7860  adequate = bad7860  (Adequate.valid adequate Two boolean env5)
  bad7861 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b0) b0) b0) (bop b0 b0)) b1 → ⊥
  bad7861  p = false≢true (cong lower p)
  cut7861 : Adequate {ℓ} ((op (op (op (op (var 0) (var 0)) (var 1)) (var 2)) (op (var 2) (var 3))) , (var 4)) → ⊥
  cut7861  adequate = bad7861  (Adequate.valid adequate Two boolean env9)
  bad7862 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b0) b0) b1) (bop b0 b0)) b0 → ⊥
  bad7862  p = false≢true (sym (cong lower p))
  cut7862 : Adequate {ℓ} ((op (op (op (op (var 0) (var 0)) (var 1)) (var 2)) (op (var 3) (var 0))) , (var 0)) → ⊥
  cut7862  adequate = bad7862  (Adequate.valid adequate Two boolean env8)
  bad7863 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b0) b0) b1) (bop b0 b0)) b0 → ⊥
  bad7863  p = false≢true (sym (cong lower p))
  cut7863 : Adequate {ℓ} ((op (op (op (op (var 0) (var 0)) (var 1)) (var 2)) (op (var 3) (var 0))) , (var 1)) → ⊥
  cut7863  adequate = bad7863  (Adequate.valid adequate Two boolean env8)
  bad7864 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b0) b1) b1) (bop b0 b0)) b1 → ⊥
  bad7864  p = false≢true (cong lower p)
  cut7864 : Adequate {ℓ} ((op (op (op (op (var 0) (var 0)) (var 1)) (var 2)) (op (var 3) (var 0))) , (var 2)) → ⊥
  cut7864  adequate = bad7864  (Adequate.valid adequate Two boolean env12)
  bad7865 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b0) b0) b0) (bop b1 b0)) b1 → ⊥
  bad7865  p = false≢true (cong lower p)
  cut7865 : Adequate {ℓ} ((op (op (op (op (var 0) (var 0)) (var 1)) (var 2)) (op (var 3) (var 0))) , (var 3)) → ⊥
  cut7865  adequate = bad7865  (Adequate.valid adequate Two boolean env5)
  bad7866 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b0) b0) b0) (bop b0 b0)) b1 → ⊥
  bad7866  p = false≢true (cong lower p)
  cut7866 : Adequate {ℓ} ((op (op (op (op (var 0) (var 0)) (var 1)) (var 2)) (op (var 3) (var 0))) , (var 4)) → ⊥
  cut7866  adequate = bad7866  (Adequate.valid adequate Two boolean env9)
  bad7867 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b0) b0) b1) (bop b0 b0)) b0 → ⊥
  bad7867  p = false≢true (sym (cong lower p))
  cut7867 : Adequate {ℓ} ((op (op (op (op (var 0) (var 0)) (var 1)) (var 2)) (op (var 3) (var 1))) , (var 0)) → ⊥
  cut7867  adequate = bad7867  (Adequate.valid adequate Two boolean env8)
  bad7868 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b0) b0) b1) (bop b0 b0)) b0 → ⊥
  bad7868  p = false≢true (sym (cong lower p))
  cut7868 : Adequate {ℓ} ((op (op (op (op (var 0) (var 0)) (var 1)) (var 2)) (op (var 3) (var 1))) , (var 1)) → ⊥
  cut7868  adequate = bad7868  (Adequate.valid adequate Two boolean env8)
  bad7869 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b0) b1) b0) (bop b1 b1)) b0 → ⊥
  bad7869  p = false≢true (sym (cong lower p))
  cut7869 : Adequate {ℓ} ((op (op (op (op (var 0) (var 0)) (var 1)) (var 2)) (op (var 3) (var 1))) , (var 2)) → ⊥
  cut7869  adequate = bad7869  (Adequate.valid adequate Two boolean env13)
  bad7870 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b0) b0) b0) (bop b1 b0)) b1 → ⊥
  bad7870  p = false≢true (cong lower p)
  cut7870 : Adequate {ℓ} ((op (op (op (op (var 0) (var 0)) (var 1)) (var 2)) (op (var 3) (var 1))) , (var 3)) → ⊥
  cut7870  adequate = bad7870  (Adequate.valid adequate Two boolean env5)
  bad7871 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b0) b0) b0) (bop b0 b0)) b1 → ⊥
  bad7871  p = false≢true (cong lower p)
  cut7871 : Adequate {ℓ} ((op (op (op (op (var 0) (var 0)) (var 1)) (var 2)) (op (var 3) (var 1))) , (var 4)) → ⊥
  cut7871  adequate = bad7871  (Adequate.valid adequate Two boolean env9)
  bad7872 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b0) b0) b1) (bop b0 b1)) b0 → ⊥
  bad7872  p = false≢true (sym (cong lower p))
  cut7872 : Adequate {ℓ} ((op (op (op (op (var 0) (var 0)) (var 1)) (var 2)) (op (var 3) (var 2))) , (var 0)) → ⊥
  cut7872  adequate = bad7872  (Adequate.valid adequate Two boolean env8)
  bad7873 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b0) b0) b1) (bop b0 b1)) b0 → ⊥
  bad7873  p = false≢true (sym (cong lower p))
  cut7873 : Adequate {ℓ} ((op (op (op (op (var 0) (var 0)) (var 1)) (var 2)) (op (var 3) (var 2))) , (var 1)) → ⊥
  cut7873  adequate = bad7873  (Adequate.valid adequate Two boolean env8)
  bad7874 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b0) b1) b1) (bop b0 b1)) b1 → ⊥
  bad7874  p = false≢true (cong lower p)
  cut7874 : Adequate {ℓ} ((op (op (op (op (var 0) (var 0)) (var 1)) (var 2)) (op (var 3) (var 2))) , (var 2)) → ⊥
  cut7874  adequate = bad7874  (Adequate.valid adequate Two boolean env12)
  bad7875 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b0) b0) b0) (bop b1 b0)) b1 → ⊥
  bad7875  p = false≢true (cong lower p)
  cut7875 : Adequate {ℓ} ((op (op (op (op (var 0) (var 0)) (var 1)) (var 2)) (op (var 3) (var 2))) , (var 3)) → ⊥
  cut7875  adequate = bad7875  (Adequate.valid adequate Two boolean env5)
  bad7876 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b0) b0) b0) (bop b0 b0)) b1 → ⊥
  bad7876  p = false≢true (cong lower p)
  cut7876 : Adequate {ℓ} ((op (op (op (op (var 0) (var 0)) (var 1)) (var 2)) (op (var 3) (var 2))) , (var 4)) → ⊥
  cut7876  adequate = bad7876  (Adequate.valid adequate Two boolean env9)
  bad7877 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b0) b0) b0) (bop b1 b1)) b0 → ⊥
  bad7877  p = false≢true (sym (cong lower p))
  cut7877 : Adequate {ℓ} ((op (op (op (op (var 0) (var 0)) (var 1)) (var 2)) (op (var 3) (var 3))) , (var 0)) → ⊥
  cut7877  adequate = bad7877  (Adequate.valid adequate Two boolean env5)
  bad7878 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b0) b0) b0) (bop b1 b1)) b0 → ⊥
  bad7878  p = false≢true (sym (cong lower p))
  cut7878 : Adequate {ℓ} ((op (op (op (op (var 0) (var 0)) (var 1)) (var 2)) (op (var 3) (var 3))) , (var 1)) → ⊥
  cut7878  adequate = bad7878  (Adequate.valid adequate Two boolean env5)
  bad7879 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b0) b0) b0) (bop b1 b1)) b0 → ⊥
  bad7879  p = false≢true (sym (cong lower p))
  cut7879 : Adequate {ℓ} ((op (op (op (op (var 0) (var 0)) (var 1)) (var 2)) (op (var 3) (var 3))) , (var 2)) → ⊥
  cut7879  adequate = bad7879  (Adequate.valid adequate Two boolean env5)
  bad7880 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b0) b0) b1) (bop b0 b0)) b0 → ⊥
  bad7880  p = false≢true (sym (cong lower p))
  cut7880 : Adequate {ℓ} ((op (op (op (op (var 0) (var 0)) (var 1)) (var 2)) (op (var 3) (var 3))) , (var 3)) → ⊥
  cut7880  adequate = bad7880  (Adequate.valid adequate Two boolean env8)
  bad7881 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b0) b0) b0) (bop b0 b0)) b1 → ⊥
  bad7881  p = false≢true (cong lower p)
  cut7881 : Adequate {ℓ} ((op (op (op (op (var 0) (var 0)) (var 1)) (var 2)) (op (var 3) (var 3))) , (var 4)) → ⊥
  cut7881  adequate = bad7881  (Adequate.valid adequate Two boolean env9)
  env14 : ℕ → Two
  env14 zero = b0
  env14 (suc zero) = b0
  env14 (suc (suc zero)) = b0
  env14 (suc (suc (suc zero))) = b1
  env14 (suc (suc (suc (suc zero)))) = b1
  env14 (suc (suc (suc (suc (suc rest))))) = b0
  bad7882 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b0) b0) b0) (bop b1 b1)) b0 → ⊥
  bad7882  p = false≢true (sym (cong lower p))
  cut7882 : Adequate {ℓ} ((op (op (op (op (var 0) (var 0)) (var 1)) (var 2)) (op (var 3) (var 4))) , (var 0)) → ⊥
  cut7882  adequate = bad7882  (Adequate.valid adequate Two boolean env14)
  bad7883 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b0) b0) b0) (bop b1 b1)) b0 → ⊥
  bad7883  p = false≢true (sym (cong lower p))
  cut7883 : Adequate {ℓ} ((op (op (op (op (var 0) (var 0)) (var 1)) (var 2)) (op (var 3) (var 4))) , (var 1)) → ⊥
  cut7883  adequate = bad7883  (Adequate.valid adequate Two boolean env14)
  bad7884 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b0) b0) b0) (bop b1 b1)) b0 → ⊥
  bad7884  p = false≢true (sym (cong lower p))
  cut7884 : Adequate {ℓ} ((op (op (op (op (var 0) (var 0)) (var 1)) (var 2)) (op (var 3) (var 4))) , (var 2)) → ⊥
  cut7884  adequate = bad7884  (Adequate.valid adequate Two boolean env14)
  env15 : ℕ → Two
  env15 zero = b0
  env15 (suc zero) = b0
  env15 (suc (suc zero)) = b0
  env15 (suc (suc (suc zero))) = b1
  env15 (suc (suc (suc (suc zero)))) = b0
  env15 (suc (suc (suc (suc (suc rest))))) = b0
  bad7885 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b0) b0) b0) (bop b1 b0)) b1 → ⊥
  bad7885  p = false≢true (cong lower p)
  cut7885 : Adequate {ℓ} ((op (op (op (op (var 0) (var 0)) (var 1)) (var 2)) (op (var 3) (var 4))) , (var 3)) → ⊥
  cut7885  adequate = bad7885  (Adequate.valid adequate Two boolean env15)
  bad7886 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b0) b0) b0) (bop b0 b1)) b1 → ⊥
  bad7886  p = false≢true (cong lower p)
  cut7886 : Adequate {ℓ} ((op (op (op (op (var 0) (var 0)) (var 1)) (var 2)) (op (var 3) (var 4))) , (var 4)) → ⊥
  cut7886  adequate = bad7886  (Adequate.valid adequate Two boolean env9)
  env16 : ℕ → Two
  env16 zero = b0
  env16 (suc zero) = b0
  env16 (suc (suc zero)) = b0
  env16 (suc (suc (suc zero))) = b0
  env16 (suc (suc (suc (suc zero)))) = b0
  env16 (suc (suc (suc (suc (suc zero))))) = b1
  env16 (suc (suc (suc (suc (suc (suc rest)))))) = b0
  bad7887 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b0) b0) b0) (bop b0 b0)) b1 → ⊥
  bad7887  p = false≢true (cong lower p)
  cut7887 : Adequate {ℓ} ((op (op (op (op (var 0) (var 0)) (var 1)) (var 2)) (op (var 3) (var 4))) , (var 5)) → ⊥
  cut7887  adequate = bad7887  (Adequate.valid adequate Two boolean env16)
  holds7888 : (z0 z1 : A2) → (mul2 (mul2 (mul2 (mul2 z0 z1) z0) z0) (mul2 z0 z0)) ≡ z0
  holds7888 z0 z1 = refl
  cut7888 : Adequate {ℓ} ((op (op (op (op (var 0) (var 1)) (var 0)) (var 0)) (op (var 0) (var 0))) , (var 0)) → ⊥
  cut7888  = reject2 ((op (op (op (op (var 0) (var 1)) (var 0)) (var 0)) (op (var 0) (var 0))) , (var 0)) (λ env → holds7888 (env 0) (env 1))
  bad7889 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b1) b0) b0) (bop b0 b0)) b1 → ⊥
  bad7889  p = false≢true (cong lower p)
  cut7889 : Adequate {ℓ} ((op (op (op (op (var 0) (var 1)) (var 0)) (var 0)) (op (var 0) (var 0))) , (var 1)) → ⊥
  cut7889  adequate = bad7889  (Adequate.valid adequate Two boolean env0)
  bad7890 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b0) b0) b0) (bop b0 b0)) b1 → ⊥
  bad7890  p = false≢true (cong lower p)
  cut7890 : Adequate {ℓ} ((op (op (op (op (var 0) (var 1)) (var 0)) (var 0)) (op (var 0) (var 0))) , (var 2)) → ⊥
  cut7890  adequate = bad7890  (Adequate.valid adequate Two boolean env1)
  bad7891 : PathP (λ _ → Two) (bop (bop (bop (bop b1 b0) b1) b1) (bop b1 b0)) b1 → ⊥
  bad7891  p = false≢true (cong lower p)
  cut7891 : Adequate {ℓ} ((op (op (op (op (var 0) (var 1)) (var 0)) (var 0)) (op (var 0) (var 1))) , (var 0)) → ⊥
  cut7891  adequate = bad7891  (Adequate.valid adequate Two boolean env2)
  bad7892 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b1) b0) b0) (bop b0 b1)) b1 → ⊥
  bad7892  p = false≢true (cong lower p)
  cut7892 : Adequate {ℓ} ((op (op (op (op (var 0) (var 1)) (var 0)) (var 0)) (op (var 0) (var 1))) , (var 1)) → ⊥
  cut7892  adequate = bad7892  (Adequate.valid adequate Two boolean env0)
  bad7893 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b0) b0) b0) (bop b0 b0)) b1 → ⊥
  bad7893  p = false≢true (cong lower p)
  cut7893 : Adequate {ℓ} ((op (op (op (op (var 0) (var 1)) (var 0)) (var 0)) (op (var 0) (var 1))) , (var 2)) → ⊥
  cut7893  adequate = bad7893  (Adequate.valid adequate Two boolean env1)
  bad7894 : PathP (λ _ → Two) (bop (bop (bop (bop b1 b0) b1) b1) (bop b1 b0)) b1 → ⊥
  bad7894  p = false≢true (cong lower p)
  cut7894 : Adequate {ℓ} ((op (op (op (op (var 0) (var 1)) (var 0)) (var 0)) (op (var 0) (var 2))) , (var 0)) → ⊥
  cut7894  adequate = bad7894  (Adequate.valid adequate Two boolean env10)
  bad7895 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b1) b0) b0) (bop b0 b0)) b1 → ⊥
  bad7895  p = false≢true (cong lower p)
  cut7895 : Adequate {ℓ} ((op (op (op (op (var 0) (var 1)) (var 0)) (var 0)) (op (var 0) (var 2))) , (var 1)) → ⊥
  cut7895  adequate = bad7895  (Adequate.valid adequate Two boolean env4)
  bad7896 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b0) b0) b0) (bop b0 b1)) b1 → ⊥
  bad7896  p = false≢true (cong lower p)
  cut7896 : Adequate {ℓ} ((op (op (op (op (var 0) (var 1)) (var 0)) (var 0)) (op (var 0) (var 2))) , (var 2)) → ⊥
  cut7896  adequate = bad7896  (Adequate.valid adequate Two boolean env1)
  bad7897 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b0) b0) b0) (bop b0 b0)) b1 → ⊥
  bad7897  p = false≢true (cong lower p)
  cut7897 : Adequate {ℓ} ((op (op (op (op (var 0) (var 1)) (var 0)) (var 0)) (op (var 0) (var 2))) , (var 3)) → ⊥
  cut7897  adequate = bad7897  (Adequate.valid adequate Two boolean env5)
  bad7898 : PathP (λ _ → Two) (bop (bop (bop (bop b1 b0) b1) b1) (bop b0 b1)) b1 → ⊥
  bad7898  p = false≢true (cong lower p)
  cut7898 : Adequate {ℓ} ((op (op (op (op (var 0) (var 1)) (var 0)) (var 0)) (op (var 1) (var 0))) , (var 0)) → ⊥
  cut7898  adequate = bad7898  (Adequate.valid adequate Two boolean env2)
  bad7899 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b1) b0) b0) (bop b1 b0)) b1 → ⊥
  bad7899  p = false≢true (cong lower p)
  cut7899 : Adequate {ℓ} ((op (op (op (op (var 0) (var 1)) (var 0)) (var 0)) (op (var 1) (var 0))) , (var 1)) → ⊥
  cut7899  adequate = bad7899  (Adequate.valid adequate Two boolean env0)
  bad7900 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b0) b0) b0) (bop b0 b0)) b1 → ⊥
  bad7900  p = false≢true (cong lower p)
  cut7900 : Adequate {ℓ} ((op (op (op (op (var 0) (var 1)) (var 0)) (var 0)) (op (var 1) (var 0))) , (var 2)) → ⊥
  cut7900  adequate = bad7900  (Adequate.valid adequate Two boolean env1)
  bad7901 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b1) b0) b0) (bop b1 b1)) b0 → ⊥
  bad7901  p = false≢true (sym (cong lower p))
  cut7901 : Adequate {ℓ} ((op (op (op (op (var 0) (var 1)) (var 0)) (var 0)) (op (var 1) (var 1))) , (var 0)) → ⊥
  cut7901  adequate = bad7901  (Adequate.valid adequate Two boolean env0)
  holds7902 : (z0 z1 : A3) → (mul3 (mul3 (mul3 (mul3 z0 z1) z0) z0) (mul3 z1 z1)) ≡ z1
  holds7902 z0 z1 = refl
  cut7902 : Adequate {ℓ} ((op (op (op (op (var 0) (var 1)) (var 0)) (var 0)) (op (var 1) (var 1))) , (var 1)) → ⊥
  cut7902  = reject3 ((op (op (op (op (var 0) (var 1)) (var 0)) (var 0)) (op (var 1) (var 1))) , (var 1)) (λ env → holds7902 (env 0) (env 1))
  bad7903 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b0) b0) b0) (bop b0 b0)) b1 → ⊥
  bad7903  p = false≢true (cong lower p)
  cut7903 : Adequate {ℓ} ((op (op (op (op (var 0) (var 1)) (var 0)) (var 0)) (op (var 1) (var 1))) , (var 2)) → ⊥
  cut7903  adequate = bad7903  (Adequate.valid adequate Two boolean env1)
  bad7904 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b1) b0) b0) (bop b1 b1)) b0 → ⊥
  bad7904  p = false≢true (sym (cong lower p))
  cut7904 : Adequate {ℓ} ((op (op (op (op (var 0) (var 1)) (var 0)) (var 0)) (op (var 1) (var 2))) , (var 0)) → ⊥
  cut7904  adequate = bad7904  (Adequate.valid adequate Two boolean env3)
  bad7905 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b1) b0) b0) (bop b1 b0)) b1 → ⊥
  bad7905  p = false≢true (cong lower p)
  cut7905 : Adequate {ℓ} ((op (op (op (op (var 0) (var 1)) (var 0)) (var 0)) (op (var 1) (var 2))) , (var 1)) → ⊥
  cut7905  adequate = bad7905  (Adequate.valid adequate Two boolean env4)
  bad7906 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b0) b0) b0) (bop b0 b1)) b1 → ⊥
  bad7906  p = false≢true (cong lower p)
  cut7906 : Adequate {ℓ} ((op (op (op (op (var 0) (var 1)) (var 0)) (var 0)) (op (var 1) (var 2))) , (var 2)) → ⊥
  cut7906  adequate = bad7906  (Adequate.valid adequate Two boolean env1)
  bad7907 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b0) b0) b0) (bop b0 b0)) b1 → ⊥
  bad7907  p = false≢true (cong lower p)
  cut7907 : Adequate {ℓ} ((op (op (op (op (var 0) (var 1)) (var 0)) (var 0)) (op (var 1) (var 2))) , (var 3)) → ⊥
  cut7907  adequate = bad7907  (Adequate.valid adequate Two boolean env5)
  bad7908 : PathP (λ _ → Two) (bop (bop (bop (bop b1 b0) b1) b1) (bop b0 b1)) b1 → ⊥
  bad7908  p = false≢true (cong lower p)
  cut7908 : Adequate {ℓ} ((op (op (op (op (var 0) (var 1)) (var 0)) (var 0)) (op (var 2) (var 0))) , (var 0)) → ⊥
  cut7908  adequate = bad7908  (Adequate.valid adequate Two boolean env10)
  bad7909 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b1) b0) b0) (bop b0 b0)) b1 → ⊥
  bad7909  p = false≢true (cong lower p)
  cut7909 : Adequate {ℓ} ((op (op (op (op (var 0) (var 1)) (var 0)) (var 0)) (op (var 2) (var 0))) , (var 1)) → ⊥
  cut7909  adequate = bad7909  (Adequate.valid adequate Two boolean env4)
  bad7910 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b0) b0) b0) (bop b1 b0)) b1 → ⊥
  bad7910  p = false≢true (cong lower p)
  cut7910 : Adequate {ℓ} ((op (op (op (op (var 0) (var 1)) (var 0)) (var 0)) (op (var 2) (var 0))) , (var 2)) → ⊥
  cut7910  adequate = bad7910  (Adequate.valid adequate Two boolean env1)
  bad7911 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b0) b0) b0) (bop b0 b0)) b1 → ⊥
  bad7911  p = false≢true (cong lower p)
  cut7911 : Adequate {ℓ} ((op (op (op (op (var 0) (var 1)) (var 0)) (var 0)) (op (var 2) (var 0))) , (var 3)) → ⊥
  cut7911  adequate = bad7911  (Adequate.valid adequate Two boolean env5)
  bad7912 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b1) b0) b0) (bop b1 b1)) b0 → ⊥
  bad7912  p = false≢true (sym (cong lower p))
  cut7912 : Adequate {ℓ} ((op (op (op (op (var 0) (var 1)) (var 0)) (var 0)) (op (var 2) (var 1))) , (var 0)) → ⊥
  cut7912  adequate = bad7912  (Adequate.valid adequate Two boolean env3)
  bad7913 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b1) b0) b0) (bop b0 b1)) b1 → ⊥
  bad7913  p = false≢true (cong lower p)
  cut7913 : Adequate {ℓ} ((op (op (op (op (var 0) (var 1)) (var 0)) (var 0)) (op (var 2) (var 1))) , (var 1)) → ⊥
  cut7913  adequate = bad7913  (Adequate.valid adequate Two boolean env4)
  bad7914 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b0) b0) b0) (bop b1 b0)) b1 → ⊥
  bad7914  p = false≢true (cong lower p)
  cut7914 : Adequate {ℓ} ((op (op (op (op (var 0) (var 1)) (var 0)) (var 0)) (op (var 2) (var 1))) , (var 2)) → ⊥
  cut7914  adequate = bad7914  (Adequate.valid adequate Two boolean env1)
  bad7915 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b0) b0) b0) (bop b0 b0)) b1 → ⊥
  bad7915  p = false≢true (cong lower p)
  cut7915 : Adequate {ℓ} ((op (op (op (op (var 0) (var 1)) (var 0)) (var 0)) (op (var 2) (var 1))) , (var 3)) → ⊥
  cut7915  adequate = bad7915  (Adequate.valid adequate Two boolean env5)
  bad7916 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b0) b0) b0) (bop b1 b1)) b0 → ⊥
  bad7916  p = false≢true (sym (cong lower p))
  cut7916 : Adequate {ℓ} ((op (op (op (op (var 0) (var 1)) (var 0)) (var 0)) (op (var 2) (var 2))) , (var 0)) → ⊥
  cut7916  adequate = bad7916  (Adequate.valid adequate Two boolean env1)
  bad7917 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b0) b0) b0) (bop b1 b1)) b0 → ⊥
  bad7917  p = false≢true (sym (cong lower p))
  cut7917 : Adequate {ℓ} ((op (op (op (op (var 0) (var 1)) (var 0)) (var 0)) (op (var 2) (var 2))) , (var 1)) → ⊥
  cut7917  adequate = bad7917  (Adequate.valid adequate Two boolean env1)
  bad7918 : PathP (λ _ → Two) (bop (bop (bop (bop b1 b1) b1) b1) (bop b0 b0)) b0 → ⊥
  bad7918  p = false≢true (sym (cong lower p))
  cut7918 : Adequate {ℓ} ((op (op (op (op (var 0) (var 1)) (var 0)) (var 0)) (op (var 2) (var 2))) , (var 2)) → ⊥
  cut7918  adequate = bad7918  (Adequate.valid adequate Two boolean env11)
  bad7919 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b0) b0) b0) (bop b0 b0)) b1 → ⊥
  bad7919  p = false≢true (cong lower p)
  cut7919 : Adequate {ℓ} ((op (op (op (op (var 0) (var 1)) (var 0)) (var 0)) (op (var 2) (var 2))) , (var 3)) → ⊥
  cut7919  adequate = bad7919  (Adequate.valid adequate Two boolean env5)
  bad7920 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b0) b0) b0) (bop b1 b1)) b0 → ⊥
  bad7920  p = false≢true (sym (cong lower p))
  cut7920 : Adequate {ℓ} ((op (op (op (op (var 0) (var 1)) (var 0)) (var 0)) (op (var 2) (var 3))) , (var 0)) → ⊥
  cut7920  adequate = bad7920  (Adequate.valid adequate Two boolean env7)
  bad7921 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b0) b0) b0) (bop b1 b1)) b0 → ⊥
  bad7921  p = false≢true (sym (cong lower p))
  cut7921 : Adequate {ℓ} ((op (op (op (op (var 0) (var 1)) (var 0)) (var 0)) (op (var 2) (var 3))) , (var 1)) → ⊥
  cut7921  adequate = bad7921  (Adequate.valid adequate Two boolean env7)
  bad7922 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b0) b0) b0) (bop b1 b0)) b1 → ⊥
  bad7922  p = false≢true (cong lower p)
  cut7922 : Adequate {ℓ} ((op (op (op (op (var 0) (var 1)) (var 0)) (var 0)) (op (var 2) (var 3))) , (var 2)) → ⊥
  cut7922  adequate = bad7922  (Adequate.valid adequate Two boolean env8)
  bad7923 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b0) b0) b0) (bop b0 b1)) b1 → ⊥
  bad7923  p = false≢true (cong lower p)
  cut7923 : Adequate {ℓ} ((op (op (op (op (var 0) (var 1)) (var 0)) (var 0)) (op (var 2) (var 3))) , (var 3)) → ⊥
  cut7923  adequate = bad7923  (Adequate.valid adequate Two boolean env5)
  bad7924 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b0) b0) b0) (bop b0 b0)) b1 → ⊥
  bad7924  p = false≢true (cong lower p)
  cut7924 : Adequate {ℓ} ((op (op (op (op (var 0) (var 1)) (var 0)) (var 0)) (op (var 2) (var 3))) , (var 4)) → ⊥
  cut7924  adequate = bad7924  (Adequate.valid adequate Two boolean env9)
  bad7925 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b1) b0) b1) (bop b0 b0)) b0 → ⊥
  bad7925  p = false≢true (sym (cong lower p))
  cut7925 : Adequate {ℓ} ((op (op (op (op (var 0) (var 1)) (var 0)) (var 1)) (op (var 0) (var 0))) , (var 0)) → ⊥
  cut7925  adequate = bad7925  (Adequate.valid adequate Two boolean env0)
  bad7926 : PathP (λ _ → Two) (bop (bop (bop (bop b1 b0) b1) b0) (bop b1 b1)) b0 → ⊥
  bad7926  p = false≢true (sym (cong lower p))
  cut7926 : Adequate {ℓ} ((op (op (op (op (var 0) (var 1)) (var 0)) (var 1)) (op (var 0) (var 0))) , (var 1)) → ⊥
  cut7926  adequate = bad7926  (Adequate.valid adequate Two boolean env2)
  bad7927 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b0) b0) b0) (bop b0 b0)) b1 → ⊥
  bad7927  p = false≢true (cong lower p)
  cut7927 : Adequate {ℓ} ((op (op (op (op (var 0) (var 1)) (var 0)) (var 1)) (op (var 0) (var 0))) , (var 2)) → ⊥
  cut7927  adequate = bad7927  (Adequate.valid adequate Two boolean env1)
  bad7928 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b1) b0) b1) (bop b0 b1)) b0 → ⊥
  bad7928  p = false≢true (sym (cong lower p))
  cut7928 : Adequate {ℓ} ((op (op (op (op (var 0) (var 1)) (var 0)) (var 1)) (op (var 0) (var 1))) , (var 0)) → ⊥
  cut7928  adequate = bad7928  (Adequate.valid adequate Two boolean env0)
  holds7929 : (z0 z1 : A3) → (mul3 (mul3 (mul3 (mul3 z0 z1) z0) z1) (mul3 z0 z1)) ≡ z1
  holds7929 z0 z1 = refl
  cut7929 : Adequate {ℓ} ((op (op (op (op (var 0) (var 1)) (var 0)) (var 1)) (op (var 0) (var 1))) , (var 1)) → ⊥
  cut7929  = reject3 ((op (op (op (op (var 0) (var 1)) (var 0)) (var 1)) (op (var 0) (var 1))) , (var 1)) (λ env → holds7929 (env 0) (env 1))
  bad7930 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b0) b0) b0) (bop b0 b0)) b1 → ⊥
  bad7930  p = false≢true (cong lower p)
  cut7930 : Adequate {ℓ} ((op (op (op (op (var 0) (var 1)) (var 0)) (var 1)) (op (var 0) (var 1))) , (var 2)) → ⊥
  cut7930  adequate = bad7930  (Adequate.valid adequate Two boolean env1)
  bad7931 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b1) b0) b1) (bop b0 b0)) b0 → ⊥
  bad7931  p = false≢true (sym (cong lower p))
  cut7931 : Adequate {ℓ} ((op (op (op (op (var 0) (var 1)) (var 0)) (var 1)) (op (var 0) (var 2))) , (var 0)) → ⊥
  cut7931  adequate = bad7931  (Adequate.valid adequate Two boolean env4)
  bad7932 : PathP (λ _ → Two) (bop (bop (bop (bop b1 b0) b1) b0) (bop b1 b1)) b0 → ⊥
  bad7932  p = false≢true (sym (cong lower p))
  cut7932 : Adequate {ℓ} ((op (op (op (op (var 0) (var 1)) (var 0)) (var 1)) (op (var 0) (var 2))) , (var 1)) → ⊥
  cut7932  adequate = bad7932  (Adequate.valid adequate Two boolean env6)
  bad7933 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b0) b0) b0) (bop b0 b1)) b1 → ⊥
  bad7933  p = false≢true (cong lower p)
  cut7933 : Adequate {ℓ} ((op (op (op (op (var 0) (var 1)) (var 0)) (var 1)) (op (var 0) (var 2))) , (var 2)) → ⊥
  cut7933  adequate = bad7933  (Adequate.valid adequate Two boolean env1)
  bad7934 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b0) b0) b0) (bop b0 b0)) b1 → ⊥
  bad7934  p = false≢true (cong lower p)
  cut7934 : Adequate {ℓ} ((op (op (op (op (var 0) (var 1)) (var 0)) (var 1)) (op (var 0) (var 2))) , (var 3)) → ⊥
  cut7934  adequate = bad7934  (Adequate.valid adequate Two boolean env5)
  bad7935 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b1) b0) b1) (bop b1 b0)) b0 → ⊥
  bad7935  p = false≢true (sym (cong lower p))
  cut7935 : Adequate {ℓ} ((op (op (op (op (var 0) (var 1)) (var 0)) (var 1)) (op (var 1) (var 0))) , (var 0)) → ⊥
  cut7935  adequate = bad7935  (Adequate.valid adequate Two boolean env0)
  holds7936 : (z0 z1 : A11) → (mul11 (mul11 (mul11 (mul11 z0 z1) z0) z1) (mul11 z1 z0)) ≡ z1
  holds7936 m11c0 m11c0 = refl
  holds7936 m11c0 m11c1 = refl
  holds7936 m11c0 m11c2 = refl
  holds7936 m11c1 m11c0 = refl
  holds7936 m11c1 m11c1 = refl
  holds7936 m11c1 m11c2 = refl
  holds7936 m11c2 m11c0 = refl
  holds7936 m11c2 m11c1 = refl
  holds7936 m11c2 m11c2 = refl
  cut7936 : Adequate {ℓ} ((op (op (op (op (var 0) (var 1)) (var 0)) (var 1)) (op (var 1) (var 0))) , (var 1)) → ⊥
  cut7936  = reject11 ((op (op (op (op (var 0) (var 1)) (var 0)) (var 1)) (op (var 1) (var 0))) , (var 1)) (λ env → holds7936 (env 0) (env 1))
  bad7937 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b0) b0) b0) (bop b0 b0)) b1 → ⊥
  bad7937  p = false≢true (cong lower p)
  cut7937 : Adequate {ℓ} ((op (op (op (op (var 0) (var 1)) (var 0)) (var 1)) (op (var 1) (var 0))) , (var 2)) → ⊥
  cut7937  adequate = bad7937  (Adequate.valid adequate Two boolean env1)
  bad7938 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b1) b0) b1) (bop b1 b1)) b0 → ⊥
  bad7938  p = false≢true (sym (cong lower p))
  cut7938 : Adequate {ℓ} ((op (op (op (op (var 0) (var 1)) (var 0)) (var 1)) (op (var 1) (var 1))) , (var 0)) → ⊥
  cut7938  adequate = bad7938  (Adequate.valid adequate Two boolean env0)
  holds7939 : (z0 z1 : A3) → (mul3 (mul3 (mul3 (mul3 z0 z1) z0) z1) (mul3 z1 z1)) ≡ z1
  holds7939 z0 z1 = refl
  cut7939 : Adequate {ℓ} ((op (op (op (op (var 0) (var 1)) (var 0)) (var 1)) (op (var 1) (var 1))) , (var 1)) → ⊥
  cut7939  = reject3 ((op (op (op (op (var 0) (var 1)) (var 0)) (var 1)) (op (var 1) (var 1))) , (var 1)) (λ env → holds7939 (env 0) (env 1))
  bad7940 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b0) b0) b0) (bop b0 b0)) b1 → ⊥
  bad7940  p = false≢true (cong lower p)
  cut7940 : Adequate {ℓ} ((op (op (op (op (var 0) (var 1)) (var 0)) (var 1)) (op (var 1) (var 1))) , (var 2)) → ⊥
  cut7940  adequate = bad7940  (Adequate.valid adequate Two boolean env1)
  bad7941 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b1) b0) b1) (bop b1 b0)) b0 → ⊥
  bad7941  p = false≢true (sym (cong lower p))
  cut7941 : Adequate {ℓ} ((op (op (op (op (var 0) (var 1)) (var 0)) (var 1)) (op (var 1) (var 2))) , (var 0)) → ⊥
  cut7941  adequate = bad7941  (Adequate.valid adequate Two boolean env4)
  holds7942 : (z0 z1 z2 : A11) → (mul11 (mul11 (mul11 (mul11 z0 z1) z0) z1) (mul11 z1 z2)) ≡ z1
  holds7942 m11c0 m11c0 m11c0 = refl
  holds7942 m11c0 m11c0 m11c1 = refl
  holds7942 m11c0 m11c0 m11c2 = refl
  holds7942 m11c0 m11c1 z2 = refl
  holds7942 m11c0 m11c2 z2 = refl
  holds7942 m11c1 m11c0 m11c0 = refl
  holds7942 m11c1 m11c0 m11c1 = refl
  holds7942 m11c1 m11c0 m11c2 = refl
  holds7942 m11c1 m11c1 z2 = refl
  holds7942 m11c1 m11c2 z2 = refl
  holds7942 m11c2 m11c0 m11c0 = refl
  holds7942 m11c2 m11c0 m11c1 = refl
  holds7942 m11c2 m11c0 m11c2 = refl
  holds7942 m11c2 m11c1 z2 = refl
  holds7942 m11c2 m11c2 z2 = refl
  cut7942 : Adequate {ℓ} ((op (op (op (op (var 0) (var 1)) (var 0)) (var 1)) (op (var 1) (var 2))) , (var 1)) → ⊥
  cut7942  = reject11 ((op (op (op (op (var 0) (var 1)) (var 0)) (var 1)) (op (var 1) (var 2))) , (var 1)) (λ env → holds7942 (env 0) (env 1) (env 2))
  bad7943 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b0) b0) b0) (bop b0 b1)) b1 → ⊥
  bad7943  p = false≢true (cong lower p)
  cut7943 : Adequate {ℓ} ((op (op (op (op (var 0) (var 1)) (var 0)) (var 1)) (op (var 1) (var 2))) , (var 2)) → ⊥
  cut7943  adequate = bad7943  (Adequate.valid adequate Two boolean env1)
  bad7944 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b0) b0) b0) (bop b0 b0)) b1 → ⊥
  bad7944  p = false≢true (cong lower p)
  cut7944 : Adequate {ℓ} ((op (op (op (op (var 0) (var 1)) (var 0)) (var 1)) (op (var 1) (var 2))) , (var 3)) → ⊥
  cut7944  adequate = bad7944  (Adequate.valid adequate Two boolean env5)
  bad7945 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b1) b0) b1) (bop b0 b0)) b0 → ⊥
  bad7945  p = false≢true (sym (cong lower p))
  cut7945 : Adequate {ℓ} ((op (op (op (op (var 0) (var 1)) (var 0)) (var 1)) (op (var 2) (var 0))) , (var 0)) → ⊥
  cut7945  adequate = bad7945  (Adequate.valid adequate Two boolean env4)
  bad7946 : PathP (λ _ → Two) (bop (bop (bop (bop b1 b0) b1) b0) (bop b1 b1)) b0 → ⊥
  bad7946  p = false≢true (sym (cong lower p))
  cut7946 : Adequate {ℓ} ((op (op (op (op (var 0) (var 1)) (var 0)) (var 1)) (op (var 2) (var 0))) , (var 1)) → ⊥
  cut7946  adequate = bad7946  (Adequate.valid adequate Two boolean env6)
  bad7947 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b0) b0) b0) (bop b1 b0)) b1 → ⊥
  bad7947  p = false≢true (cong lower p)
  cut7947 : Adequate {ℓ} ((op (op (op (op (var 0) (var 1)) (var 0)) (var 1)) (op (var 2) (var 0))) , (var 2)) → ⊥
  cut7947  adequate = bad7947  (Adequate.valid adequate Two boolean env1)
  bad7948 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b0) b0) b0) (bop b0 b0)) b1 → ⊥
  bad7948  p = false≢true (cong lower p)
  cut7948 : Adequate {ℓ} ((op (op (op (op (var 0) (var 1)) (var 0)) (var 1)) (op (var 2) (var 0))) , (var 3)) → ⊥
  cut7948  adequate = bad7948  (Adequate.valid adequate Two boolean env5)
  bad7949 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b1) b0) b1) (bop b0 b1)) b0 → ⊥
  bad7949  p = false≢true (sym (cong lower p))
  cut7949 : Adequate {ℓ} ((op (op (op (op (var 0) (var 1)) (var 0)) (var 1)) (op (var 2) (var 1))) , (var 0)) → ⊥
  cut7949  adequate = bad7949  (Adequate.valid adequate Two boolean env4)
  holds7950 : (z0 z1 z2 : A3) → (mul3 (mul3 (mul3 (mul3 z0 z1) z0) z1) (mul3 z2 z1)) ≡ z1
  holds7950 z0 z1 z2 = refl
  cut7950 : Adequate {ℓ} ((op (op (op (op (var 0) (var 1)) (var 0)) (var 1)) (op (var 2) (var 1))) , (var 1)) → ⊥
  cut7950  = reject3 ((op (op (op (op (var 0) (var 1)) (var 0)) (var 1)) (op (var 2) (var 1))) , (var 1)) (λ env → holds7950 (env 0) (env 1) (env 2))
  bad7951 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b0) b0) b0) (bop b1 b0)) b1 → ⊥
  bad7951  p = false≢true (cong lower p)
  cut7951 : Adequate {ℓ} ((op (op (op (op (var 0) (var 1)) (var 0)) (var 1)) (op (var 2) (var 1))) , (var 2)) → ⊥
  cut7951  adequate = bad7951  (Adequate.valid adequate Two boolean env1)
  bad7952 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b0) b0) b0) (bop b0 b0)) b1 → ⊥
  bad7952  p = false≢true (cong lower p)
  cut7952 : Adequate {ℓ} ((op (op (op (op (var 0) (var 1)) (var 0)) (var 1)) (op (var 2) (var 1))) , (var 3)) → ⊥
  cut7952  adequate = bad7952  (Adequate.valid adequate Two boolean env5)
  bad7953 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b0) b0) b0) (bop b1 b1)) b0 → ⊥
  bad7953  p = false≢true (sym (cong lower p))
  cut7953 : Adequate {ℓ} ((op (op (op (op (var 0) (var 1)) (var 0)) (var 1)) (op (var 2) (var 2))) , (var 0)) → ⊥
  cut7953  adequate = bad7953  (Adequate.valid adequate Two boolean env1)
  bad7954 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b0) b0) b0) (bop b1 b1)) b0 → ⊥
  bad7954  p = false≢true (sym (cong lower p))
  cut7954 : Adequate {ℓ} ((op (op (op (op (var 0) (var 1)) (var 0)) (var 1)) (op (var 2) (var 2))) , (var 1)) → ⊥
  cut7954  adequate = bad7954  (Adequate.valid adequate Two boolean env1)
  bad7955 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b1) b0) b1) (bop b0 b0)) b0 → ⊥
  bad7955  p = false≢true (sym (cong lower p))
  cut7955 : Adequate {ℓ} ((op (op (op (op (var 0) (var 1)) (var 0)) (var 1)) (op (var 2) (var 2))) , (var 2)) → ⊥
  cut7955  adequate = bad7955  (Adequate.valid adequate Two boolean env4)
  bad7956 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b0) b0) b0) (bop b0 b0)) b1 → ⊥
  bad7956  p = false≢true (cong lower p)
  cut7956 : Adequate {ℓ} ((op (op (op (op (var 0) (var 1)) (var 0)) (var 1)) (op (var 2) (var 2))) , (var 3)) → ⊥
  cut7956  adequate = bad7956  (Adequate.valid adequate Two boolean env5)
  bad7957 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b0) b0) b0) (bop b1 b1)) b0 → ⊥
  bad7957  p = false≢true (sym (cong lower p))
  cut7957 : Adequate {ℓ} ((op (op (op (op (var 0) (var 1)) (var 0)) (var 1)) (op (var 2) (var 3))) , (var 0)) → ⊥
  cut7957  adequate = bad7957  (Adequate.valid adequate Two boolean env7)
  bad7958 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b0) b0) b0) (bop b1 b1)) b0 → ⊥
  bad7958  p = false≢true (sym (cong lower p))
  cut7958 : Adequate {ℓ} ((op (op (op (op (var 0) (var 1)) (var 0)) (var 1)) (op (var 2) (var 3))) , (var 1)) → ⊥
  cut7958  adequate = bad7958  (Adequate.valid adequate Two boolean env7)
  bad7959 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b0) b0) b0) (bop b1 b0)) b1 → ⊥
  bad7959  p = false≢true (cong lower p)
  cut7959 : Adequate {ℓ} ((op (op (op (op (var 0) (var 1)) (var 0)) (var 1)) (op (var 2) (var 3))) , (var 2)) → ⊥
  cut7959  adequate = bad7959  (Adequate.valid adequate Two boolean env8)
  bad7960 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b0) b0) b0) (bop b0 b1)) b1 → ⊥
  bad7960  p = false≢true (cong lower p)
  cut7960 : Adequate {ℓ} ((op (op (op (op (var 0) (var 1)) (var 0)) (var 1)) (op (var 2) (var 3))) , (var 3)) → ⊥
  cut7960  adequate = bad7960  (Adequate.valid adequate Two boolean env5)
  bad7961 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b0) b0) b0) (bop b0 b0)) b1 → ⊥
  bad7961  p = false≢true (cong lower p)
  cut7961 : Adequate {ℓ} ((op (op (op (op (var 0) (var 1)) (var 0)) (var 1)) (op (var 2) (var 3))) , (var 4)) → ⊥
  cut7961  adequate = bad7961  (Adequate.valid adequate Two boolean env9)
  bad7962 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b0) b0) b1) (bop b0 b0)) b0 → ⊥
  bad7962  p = false≢true (sym (cong lower p))
  cut7962 : Adequate {ℓ} ((op (op (op (op (var 0) (var 1)) (var 0)) (var 2)) (op (var 0) (var 0))) , (var 0)) → ⊥
  cut7962  adequate = bad7962  (Adequate.valid adequate Two boolean env1)
  bad7963 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b0) b0) b1) (bop b0 b0)) b0 → ⊥
  bad7963  p = false≢true (sym (cong lower p))
  cut7963 : Adequate {ℓ} ((op (op (op (op (var 0) (var 1)) (var 0)) (var 2)) (op (var 0) (var 0))) , (var 1)) → ⊥
  cut7963  adequate = bad7963  (Adequate.valid adequate Two boolean env1)
  bad7964 : PathP (λ _ → Two) (bop (bop (bop (bop b1 b0) b1) b0) (bop b1 b1)) b0 → ⊥
  bad7964  p = false≢true (sym (cong lower p))
  cut7964 : Adequate {ℓ} ((op (op (op (op (var 0) (var 1)) (var 0)) (var 2)) (op (var 0) (var 0))) , (var 2)) → ⊥
  cut7964  adequate = bad7964  (Adequate.valid adequate Two boolean env10)
  bad7965 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b0) b0) b0) (bop b0 b0)) b1 → ⊥
  bad7965  p = false≢true (cong lower p)
  cut7965 : Adequate {ℓ} ((op (op (op (op (var 0) (var 1)) (var 0)) (var 2)) (op (var 0) (var 0))) , (var 3)) → ⊥
  cut7965  adequate = bad7965  (Adequate.valid adequate Two boolean env5)
  bad7966 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b0) b0) b1) (bop b0 b0)) b0 → ⊥
  bad7966  p = false≢true (sym (cong lower p))
  cut7966 : Adequate {ℓ} ((op (op (op (op (var 0) (var 1)) (var 0)) (var 2)) (op (var 0) (var 1))) , (var 0)) → ⊥
  cut7966  adequate = bad7966  (Adequate.valid adequate Two boolean env1)
  bad7967 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b0) b0) b1) (bop b0 b0)) b0 → ⊥
  bad7967  p = false≢true (sym (cong lower p))
  cut7967 : Adequate {ℓ} ((op (op (op (op (var 0) (var 1)) (var 0)) (var 2)) (op (var 0) (var 1))) , (var 1)) → ⊥
  cut7967  adequate = bad7967  (Adequate.valid adequate Two boolean env1)
  bad7968 : PathP (λ _ → Two) (bop (bop (bop (bop b1 b0) b1) b1) (bop b1 b0)) b1 → ⊥
  bad7968  p = false≢true (cong lower p)
  cut7968 : Adequate {ℓ} ((op (op (op (op (var 0) (var 1)) (var 0)) (var 2)) (op (var 0) (var 1))) , (var 2)) → ⊥
  cut7968  adequate = bad7968  (Adequate.valid adequate Two boolean env6)
  bad7969 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b0) b0) b0) (bop b0 b0)) b1 → ⊥
  bad7969  p = false≢true (cong lower p)
  cut7969 : Adequate {ℓ} ((op (op (op (op (var 0) (var 1)) (var 0)) (var 2)) (op (var 0) (var 1))) , (var 3)) → ⊥
  cut7969  adequate = bad7969  (Adequate.valid adequate Two boolean env5)
  bad7970 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b0) b0) b1) (bop b0 b1)) b0 → ⊥
  bad7970  p = false≢true (sym (cong lower p))
  cut7970 : Adequate {ℓ} ((op (op (op (op (var 0) (var 1)) (var 0)) (var 2)) (op (var 0) (var 2))) , (var 0)) → ⊥
  cut7970  adequate = bad7970  (Adequate.valid adequate Two boolean env1)
  bad7971 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b0) b0) b1) (bop b0 b1)) b0 → ⊥
  bad7971  p = false≢true (sym (cong lower p))
  cut7971 : Adequate {ℓ} ((op (op (op (op (var 0) (var 1)) (var 0)) (var 2)) (op (var 0) (var 2))) , (var 1)) → ⊥
  cut7971  adequate = bad7971  (Adequate.valid adequate Two boolean env1)
  holds7972 : (z0 z1 z2 : A3) → (mul3 (mul3 (mul3 (mul3 z0 z1) z0) z2) (mul3 z0 z2)) ≡ z2
  holds7972 z0 z1 z2 = refl
  cut7972 : Adequate {ℓ} ((op (op (op (op (var 0) (var 1)) (var 0)) (var 2)) (op (var 0) (var 2))) , (var 2)) → ⊥
  cut7972  = reject3 ((op (op (op (op (var 0) (var 1)) (var 0)) (var 2)) (op (var 0) (var 2))) , (var 2)) (λ env → holds7972 (env 0) (env 1) (env 2))
  bad7973 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b0) b0) b0) (bop b0 b0)) b1 → ⊥
  bad7973  p = false≢true (cong lower p)
  cut7973 : Adequate {ℓ} ((op (op (op (op (var 0) (var 1)) (var 0)) (var 2)) (op (var 0) (var 2))) , (var 3)) → ⊥
  cut7973  adequate = bad7973  (Adequate.valid adequate Two boolean env5)
  bad7974 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b0) b0) b1) (bop b0 b0)) b0 → ⊥
  bad7974  p = false≢true (sym (cong lower p))
  cut7974 : Adequate {ℓ} ((op (op (op (op (var 0) (var 1)) (var 0)) (var 2)) (op (var 0) (var 3))) , (var 0)) → ⊥
  cut7974  adequate = bad7974  (Adequate.valid adequate Two boolean env8)
  bad7975 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b0) b0) b1) (bop b0 b0)) b0 → ⊥
  bad7975  p = false≢true (sym (cong lower p))
  cut7975 : Adequate {ℓ} ((op (op (op (op (var 0) (var 1)) (var 0)) (var 2)) (op (var 0) (var 3))) , (var 1)) → ⊥
  cut7975  adequate = bad7975  (Adequate.valid adequate Two boolean env8)
  env17 : ℕ → Two
  env17 zero = b1
  env17 (suc zero) = b0
  env17 (suc (suc zero)) = b0
  env17 (suc (suc (suc zero))) = b1
  env17 (suc (suc (suc (suc rest)))) = b0
  bad7976 : PathP (λ _ → Two) (bop (bop (bop (bop b1 b0) b1) b0) (bop b1 b1)) b0 → ⊥
  bad7976  p = false≢true (sym (cong lower p))
  cut7976 : Adequate {ℓ} ((op (op (op (op (var 0) (var 1)) (var 0)) (var 2)) (op (var 0) (var 3))) , (var 2)) → ⊥
  cut7976  adequate = bad7976  (Adequate.valid adequate Two boolean env17)
  bad7977 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b0) b0) b0) (bop b0 b1)) b1 → ⊥
  bad7977  p = false≢true (cong lower p)
  cut7977 : Adequate {ℓ} ((op (op (op (op (var 0) (var 1)) (var 0)) (var 2)) (op (var 0) (var 3))) , (var 3)) → ⊥
  cut7977  adequate = bad7977  (Adequate.valid adequate Two boolean env5)
  bad7978 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b0) b0) b0) (bop b0 b0)) b1 → ⊥
  bad7978  p = false≢true (cong lower p)
  cut7978 : Adequate {ℓ} ((op (op (op (op (var 0) (var 1)) (var 0)) (var 2)) (op (var 0) (var 3))) , (var 4)) → ⊥
  cut7978  adequate = bad7978  (Adequate.valid adequate Two boolean env9)
  bad7979 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b0) b0) b1) (bop b0 b0)) b0 → ⊥
  bad7979  p = false≢true (sym (cong lower p))
  cut7979 : Adequate {ℓ} ((op (op (op (op (var 0) (var 1)) (var 0)) (var 2)) (op (var 1) (var 0))) , (var 0)) → ⊥
  cut7979  adequate = bad7979  (Adequate.valid adequate Two boolean env1)
  bad7980 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b0) b0) b1) (bop b0 b0)) b0 → ⊥
  bad7980  p = false≢true (sym (cong lower p))
  cut7980 : Adequate {ℓ} ((op (op (op (op (var 0) (var 1)) (var 0)) (var 2)) (op (var 1) (var 0))) , (var 1)) → ⊥
  cut7980  adequate = bad7980  (Adequate.valid adequate Two boolean env1)
  bad7981 : PathP (λ _ → Two) (bop (bop (bop (bop b1 b0) b1) b1) (bop b0 b1)) b1 → ⊥
  bad7981  p = false≢true (cong lower p)
  cut7981 : Adequate {ℓ} ((op (op (op (op (var 0) (var 1)) (var 0)) (var 2)) (op (var 1) (var 0))) , (var 2)) → ⊥
  cut7981  adequate = bad7981  (Adequate.valid adequate Two boolean env6)
  bad7982 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b0) b0) b0) (bop b0 b0)) b1 → ⊥
  bad7982  p = false≢true (cong lower p)
  cut7982 : Adequate {ℓ} ((op (op (op (op (var 0) (var 1)) (var 0)) (var 2)) (op (var 1) (var 0))) , (var 3)) → ⊥
  cut7982  adequate = bad7982  (Adequate.valid adequate Two boolean env5)
  bad7983 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b0) b0) b1) (bop b0 b0)) b0 → ⊥
  bad7983  p = false≢true (sym (cong lower p))
  cut7983 : Adequate {ℓ} ((op (op (op (op (var 0) (var 1)) (var 0)) (var 2)) (op (var 1) (var 1))) , (var 0)) → ⊥
  cut7983  adequate = bad7983  (Adequate.valid adequate Two boolean env1)
  bad7984 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b0) b0) b1) (bop b0 b0)) b0 → ⊥
  bad7984  p = false≢true (sym (cong lower p))
  cut7984 : Adequate {ℓ} ((op (op (op (op (var 0) (var 1)) (var 0)) (var 2)) (op (var 1) (var 1))) , (var 1)) → ⊥
  cut7984  adequate = bad7984  (Adequate.valid adequate Two boolean env1)
  bad7985 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b1) b0) b0) (bop b1 b1)) b0 → ⊥
  bad7985  p = false≢true (sym (cong lower p))
  cut7985 : Adequate {ℓ} ((op (op (op (op (var 0) (var 1)) (var 0)) (var 2)) (op (var 1) (var 1))) , (var 2)) → ⊥
  cut7985  adequate = bad7985  (Adequate.valid adequate Two boolean env4)
  bad7986 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b0) b0) b0) (bop b0 b0)) b1 → ⊥
  bad7986  p = false≢true (cong lower p)
  cut7986 : Adequate {ℓ} ((op (op (op (op (var 0) (var 1)) (var 0)) (var 2)) (op (var 1) (var 1))) , (var 3)) → ⊥
  cut7986  adequate = bad7986  (Adequate.valid adequate Two boolean env5)
  bad7987 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b0) b0) b1) (bop b0 b1)) b0 → ⊥
  bad7987  p = false≢true (sym (cong lower p))
  cut7987 : Adequate {ℓ} ((op (op (op (op (var 0) (var 1)) (var 0)) (var 2)) (op (var 1) (var 2))) , (var 0)) → ⊥
  cut7987  adequate = bad7987  (Adequate.valid adequate Two boolean env1)
  bad7988 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b0) b0) b1) (bop b0 b1)) b0 → ⊥
  bad7988  p = false≢true (sym (cong lower p))
  cut7988 : Adequate {ℓ} ((op (op (op (op (var 0) (var 1)) (var 0)) (var 2)) (op (var 1) (var 2))) , (var 1)) → ⊥
  cut7988  adequate = bad7988  (Adequate.valid adequate Two boolean env1)
  bad7989 : PathP (λ _ → Two) (bop (bop (bop (bop b1 b0) b1) b1) (bop b0 b1)) b1 → ⊥
  bad7989  p = false≢true (cong lower p)
  cut7989 : Adequate {ℓ} ((op (op (op (op (var 0) (var 1)) (var 0)) (var 2)) (op (var 1) (var 2))) , (var 2)) → ⊥
  cut7989  adequate = bad7989  (Adequate.valid adequate Two boolean env6)
  bad7990 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b0) b0) b0) (bop b0 b0)) b1 → ⊥
  bad7990  p = false≢true (cong lower p)
  cut7990 : Adequate {ℓ} ((op (op (op (op (var 0) (var 1)) (var 0)) (var 2)) (op (var 1) (var 2))) , (var 3)) → ⊥
  cut7990  adequate = bad7990  (Adequate.valid adequate Two boolean env5)
  bad7991 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b0) b0) b1) (bop b0 b0)) b0 → ⊥
  bad7991  p = false≢true (sym (cong lower p))
  cut7991 : Adequate {ℓ} ((op (op (op (op (var 0) (var 1)) (var 0)) (var 2)) (op (var 1) (var 3))) , (var 0)) → ⊥
  cut7991  adequate = bad7991  (Adequate.valid adequate Two boolean env8)
  bad7992 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b0) b0) b1) (bop b0 b0)) b0 → ⊥
  bad7992  p = false≢true (sym (cong lower p))
  cut7992 : Adequate {ℓ} ((op (op (op (op (var 0) (var 1)) (var 0)) (var 2)) (op (var 1) (var 3))) , (var 1)) → ⊥
  cut7992  adequate = bad7992  (Adequate.valid adequate Two boolean env8)
  bad7993 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b1) b0) b0) (bop b1 b1)) b0 → ⊥
  bad7993  p = false≢true (sym (cong lower p))
  cut7993 : Adequate {ℓ} ((op (op (op (op (var 0) (var 1)) (var 0)) (var 2)) (op (var 1) (var 3))) , (var 2)) → ⊥
  cut7993  adequate = bad7993  (Adequate.valid adequate Two boolean env13)
  bad7994 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b0) b0) b0) (bop b0 b1)) b1 → ⊥
  bad7994  p = false≢true (cong lower p)
  cut7994 : Adequate {ℓ} ((op (op (op (op (var 0) (var 1)) (var 0)) (var 2)) (op (var 1) (var 3))) , (var 3)) → ⊥
  cut7994  adequate = bad7994  (Adequate.valid adequate Two boolean env5)
  bad7995 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b0) b0) b0) (bop b0 b0)) b1 → ⊥
  bad7995  p = false≢true (cong lower p)
  cut7995 : Adequate {ℓ} ((op (op (op (op (var 0) (var 1)) (var 0)) (var 2)) (op (var 1) (var 3))) , (var 4)) → ⊥
  cut7995  adequate = bad7995  (Adequate.valid adequate Two boolean env9)
  bad7996 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b0) b0) b1) (bop b1 b0)) b0 → ⊥
  bad7996  p = false≢true (sym (cong lower p))
  cut7996 : Adequate {ℓ} ((op (op (op (op (var 0) (var 1)) (var 0)) (var 2)) (op (var 2) (var 0))) , (var 0)) → ⊥
  cut7996  adequate = bad7996  (Adequate.valid adequate Two boolean env1)
  bad7997 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b0) b0) b1) (bop b1 b0)) b0 → ⊥
  bad7997  p = false≢true (sym (cong lower p))
  cut7997 : Adequate {ℓ} ((op (op (op (op (var 0) (var 1)) (var 0)) (var 2)) (op (var 2) (var 0))) , (var 1)) → ⊥
  cut7997  adequate = bad7997  (Adequate.valid adequate Two boolean env1)
  holds7998 : (z0 z1 z2 : A13) → (mul13 (mul13 (mul13 (mul13 z0 z1) z0) z2) (mul13 z2 z0)) ≡ z2
  holds7998 m13c0 m13c0 m13c0 = refl
  holds7998 m13c0 m13c0 m13c1 = refl
  holds7998 m13c0 m13c0 m13c2 = refl
  holds7998 m13c0 m13c0 m13c3 = refl
  holds7998 m13c0 m13c1 m13c0 = refl
  holds7998 m13c0 m13c1 m13c1 = refl
  holds7998 m13c0 m13c1 m13c2 = refl
  holds7998 m13c0 m13c1 m13c3 = refl
  holds7998 m13c0 m13c2 m13c0 = refl
  holds7998 m13c0 m13c2 m13c1 = refl
  holds7998 m13c0 m13c2 m13c2 = refl
  holds7998 m13c0 m13c2 m13c3 = refl
  holds7998 m13c0 m13c3 m13c0 = refl
  holds7998 m13c0 m13c3 m13c1 = refl
  holds7998 m13c0 m13c3 m13c2 = refl
  holds7998 m13c0 m13c3 m13c3 = refl
  holds7998 m13c1 m13c0 m13c0 = refl
  holds7998 m13c1 m13c0 m13c1 = refl
  holds7998 m13c1 m13c0 m13c2 = refl
  holds7998 m13c1 m13c0 m13c3 = refl
  holds7998 m13c1 m13c1 m13c0 = refl
  holds7998 m13c1 m13c1 m13c1 = refl
  holds7998 m13c1 m13c1 m13c2 = refl
  holds7998 m13c1 m13c1 m13c3 = refl
  holds7998 m13c1 m13c2 m13c0 = refl
  holds7998 m13c1 m13c2 m13c1 = refl
  holds7998 m13c1 m13c2 m13c2 = refl
  holds7998 m13c1 m13c2 m13c3 = refl
  holds7998 m13c1 m13c3 m13c0 = refl
  holds7998 m13c1 m13c3 m13c1 = refl
  holds7998 m13c1 m13c3 m13c2 = refl
  holds7998 m13c1 m13c3 m13c3 = refl
  holds7998 m13c2 m13c0 m13c0 = refl
  holds7998 m13c2 m13c0 m13c1 = refl
  holds7998 m13c2 m13c0 m13c2 = refl
  holds7998 m13c2 m13c0 m13c3 = refl
  holds7998 m13c2 m13c1 m13c0 = refl
  holds7998 m13c2 m13c1 m13c1 = refl
  holds7998 m13c2 m13c1 m13c2 = refl
  holds7998 m13c2 m13c1 m13c3 = refl
  holds7998 m13c2 m13c2 m13c0 = refl
  holds7998 m13c2 m13c2 m13c1 = refl
  holds7998 m13c2 m13c2 m13c2 = refl
  holds7998 m13c2 m13c2 m13c3 = refl
  holds7998 m13c2 m13c3 m13c0 = refl
  holds7998 m13c2 m13c3 m13c1 = refl
  holds7998 m13c2 m13c3 m13c2 = refl
  holds7998 m13c2 m13c3 m13c3 = refl
  holds7998 m13c3 m13c0 m13c0 = refl
  holds7998 m13c3 m13c0 m13c1 = refl
  holds7998 m13c3 m13c0 m13c2 = refl
  holds7998 m13c3 m13c0 m13c3 = refl
  holds7998 m13c3 m13c1 m13c0 = refl
  holds7998 m13c3 m13c1 m13c1 = refl
  holds7998 m13c3 m13c1 m13c2 = refl
  holds7998 m13c3 m13c1 m13c3 = refl
  holds7998 m13c3 m13c2 m13c0 = refl
  holds7998 m13c3 m13c2 m13c1 = refl
  holds7998 m13c3 m13c2 m13c2 = refl
  holds7998 m13c3 m13c2 m13c3 = refl
  holds7998 m13c3 m13c3 m13c0 = refl
  holds7998 m13c3 m13c3 m13c1 = refl
  holds7998 m13c3 m13c3 m13c2 = refl
  holds7998 m13c3 m13c3 m13c3 = refl
  cut7998 : Adequate {ℓ} ((op (op (op (op (var 0) (var 1)) (var 0)) (var 2)) (op (var 2) (var 0))) , (var 2)) → ⊥
  cut7998  = reject13 ((op (op (op (op (var 0) (var 1)) (var 0)) (var 2)) (op (var 2) (var 0))) , (var 2)) (λ env → holds7998 (env 0) (env 1) (env 2))
  bad7999 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b0) b0) b0) (bop b0 b0)) b1 → ⊥
  bad7999  p = false≢true (cong lower p)
  cut7999 : Adequate {ℓ} ((op (op (op (op (var 0) (var 1)) (var 0)) (var 2)) (op (var 2) (var 0))) , (var 3)) → ⊥
  cut7999  adequate = bad7999  (Adequate.valid adequate Two boolean env5)
  bad8000 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b0) b0) b1) (bop b1 b0)) b0 → ⊥
  bad8000  p = false≢true (sym (cong lower p))
  cut8000 : Adequate {ℓ} ((op (op (op (op (var 0) (var 1)) (var 0)) (var 2)) (op (var 2) (var 1))) , (var 0)) → ⊥
  cut8000  adequate = bad8000  (Adequate.valid adequate Two boolean env1)
  bad8001 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b0) b0) b1) (bop b1 b0)) b0 → ⊥
  bad8001  p = false≢true (sym (cong lower p))
  cut8001 : Adequate {ℓ} ((op (op (op (op (var 0) (var 1)) (var 0)) (var 2)) (op (var 2) (var 1))) , (var 1)) → ⊥
  cut8001  adequate = bad8001  (Adequate.valid adequate Two boolean env1)
  bad8002 : PathP (λ _ → Two) (bop (bop (bop (bop b1 b0) b1) b1) (bop b1 b0)) b1 → ⊥
  bad8002  p = false≢true (cong lower p)
  cut8002 : Adequate {ℓ} ((op (op (op (op (var 0) (var 1)) (var 0)) (var 2)) (op (var 2) (var 1))) , (var 2)) → ⊥
  cut8002  adequate = bad8002  (Adequate.valid adequate Two boolean env6)
  bad8003 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b0) b0) b0) (bop b0 b0)) b1 → ⊥
  bad8003  p = false≢true (cong lower p)
  cut8003 : Adequate {ℓ} ((op (op (op (op (var 0) (var 1)) (var 0)) (var 2)) (op (var 2) (var 1))) , (var 3)) → ⊥
  cut8003  adequate = bad8003  (Adequate.valid adequate Two boolean env5)
  bad8004 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b0) b0) b1) (bop b1 b1)) b0 → ⊥
  bad8004  p = false≢true (sym (cong lower p))
  cut8004 : Adequate {ℓ} ((op (op (op (op (var 0) (var 1)) (var 0)) (var 2)) (op (var 2) (var 2))) , (var 0)) → ⊥
  cut8004  adequate = bad8004  (Adequate.valid adequate Two boolean env1)
  bad8005 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b0) b0) b1) (bop b1 b1)) b0 → ⊥
  bad8005  p = false≢true (sym (cong lower p))
  cut8005 : Adequate {ℓ} ((op (op (op (op (var 0) (var 1)) (var 0)) (var 2)) (op (var 2) (var 2))) , (var 1)) → ⊥
  cut8005  adequate = bad8005  (Adequate.valid adequate Two boolean env1)
  holds8006 : (z0 z1 z2 : A3) → (mul3 (mul3 (mul3 (mul3 z0 z1) z0) z2) (mul3 z2 z2)) ≡ z2
  holds8006 z0 z1 z2 = refl
  cut8006 : Adequate {ℓ} ((op (op (op (op (var 0) (var 1)) (var 0)) (var 2)) (op (var 2) (var 2))) , (var 2)) → ⊥
  cut8006  = reject3 ((op (op (op (op (var 0) (var 1)) (var 0)) (var 2)) (op (var 2) (var 2))) , (var 2)) (λ env → holds8006 (env 0) (env 1) (env 2))
  bad8007 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b0) b0) b0) (bop b0 b0)) b1 → ⊥
  bad8007  p = false≢true (cong lower p)
  cut8007 : Adequate {ℓ} ((op (op (op (op (var 0) (var 1)) (var 0)) (var 2)) (op (var 2) (var 2))) , (var 3)) → ⊥
  cut8007  adequate = bad8007  (Adequate.valid adequate Two boolean env5)
  bad8008 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b0) b0) b1) (bop b1 b0)) b0 → ⊥
  bad8008  p = false≢true (sym (cong lower p))
  cut8008 : Adequate {ℓ} ((op (op (op (op (var 0) (var 1)) (var 0)) (var 2)) (op (var 2) (var 3))) , (var 0)) → ⊥
  cut8008  adequate = bad8008  (Adequate.valid adequate Two boolean env8)
  bad8009 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b0) b0) b1) (bop b1 b0)) b0 → ⊥
  bad8009  p = false≢true (sym (cong lower p))
  cut8009 : Adequate {ℓ} ((op (op (op (op (var 0) (var 1)) (var 0)) (var 2)) (op (var 2) (var 3))) , (var 1)) → ⊥
  cut8009  adequate = bad8009  (Adequate.valid adequate Two boolean env8)
  env18 : ℕ → Two
  env18 zero = b1
  env18 (suc zero) = b0
  env18 (suc (suc zero)) = b1
  env18 (suc (suc (suc zero))) = b0
  env18 (suc (suc (suc (suc rest)))) = b0
  bad8010 : PathP (λ _ → Two) (bop (bop (bop (bop b1 b0) b1) b1) (bop b1 b0)) b1 → ⊥
  bad8010  p = false≢true (cong lower p)
  cut8010 : Adequate {ℓ} ((op (op (op (op (var 0) (var 1)) (var 0)) (var 2)) (op (var 2) (var 3))) , (var 2)) → ⊥
  cut8010  adequate = bad8010  (Adequate.valid adequate Two boolean env18)
  bad8011 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b0) b0) b0) (bop b0 b1)) b1 → ⊥
  bad8011  p = false≢true (cong lower p)
  cut8011 : Adequate {ℓ} ((op (op (op (op (var 0) (var 1)) (var 0)) (var 2)) (op (var 2) (var 3))) , (var 3)) → ⊥
  cut8011  adequate = bad8011  (Adequate.valid adequate Two boolean env5)
  bad8012 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b0) b0) b0) (bop b0 b0)) b1 → ⊥
  bad8012  p = false≢true (cong lower p)
  cut8012 : Adequate {ℓ} ((op (op (op (op (var 0) (var 1)) (var 0)) (var 2)) (op (var 2) (var 3))) , (var 4)) → ⊥
  cut8012  adequate = bad8012  (Adequate.valid adequate Two boolean env9)
  bad8013 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b0) b0) b1) (bop b0 b0)) b0 → ⊥
  bad8013  p = false≢true (sym (cong lower p))
  cut8013 : Adequate {ℓ} ((op (op (op (op (var 0) (var 1)) (var 0)) (var 2)) (op (var 3) (var 0))) , (var 0)) → ⊥
  cut8013  adequate = bad8013  (Adequate.valid adequate Two boolean env8)
  bad8014 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b0) b0) b1) (bop b0 b0)) b0 → ⊥
  bad8014  p = false≢true (sym (cong lower p))
  cut8014 : Adequate {ℓ} ((op (op (op (op (var 0) (var 1)) (var 0)) (var 2)) (op (var 3) (var 0))) , (var 1)) → ⊥
  cut8014  adequate = bad8014  (Adequate.valid adequate Two boolean env8)
  bad8015 : PathP (λ _ → Two) (bop (bop (bop (bop b1 b0) b1) b0) (bop b1 b1)) b0 → ⊥
  bad8015  p = false≢true (sym (cong lower p))
  cut8015 : Adequate {ℓ} ((op (op (op (op (var 0) (var 1)) (var 0)) (var 2)) (op (var 3) (var 0))) , (var 2)) → ⊥
  cut8015  adequate = bad8015  (Adequate.valid adequate Two boolean env17)
  bad8016 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b0) b0) b0) (bop b1 b0)) b1 → ⊥
  bad8016  p = false≢true (cong lower p)
  cut8016 : Adequate {ℓ} ((op (op (op (op (var 0) (var 1)) (var 0)) (var 2)) (op (var 3) (var 0))) , (var 3)) → ⊥
  cut8016  adequate = bad8016  (Adequate.valid adequate Two boolean env5)
  bad8017 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b0) b0) b0) (bop b0 b0)) b1 → ⊥
  bad8017  p = false≢true (cong lower p)
  cut8017 : Adequate {ℓ} ((op (op (op (op (var 0) (var 1)) (var 0)) (var 2)) (op (var 3) (var 0))) , (var 4)) → ⊥
  cut8017  adequate = bad8017  (Adequate.valid adequate Two boolean env9)
  bad8018 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b0) b0) b1) (bop b0 b0)) b0 → ⊥
  bad8018  p = false≢true (sym (cong lower p))
  cut8018 : Adequate {ℓ} ((op (op (op (op (var 0) (var 1)) (var 0)) (var 2)) (op (var 3) (var 1))) , (var 0)) → ⊥
  cut8018  adequate = bad8018  (Adequate.valid adequate Two boolean env8)
  bad8019 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b0) b0) b1) (bop b0 b0)) b0 → ⊥
  bad8019  p = false≢true (sym (cong lower p))
  cut8019 : Adequate {ℓ} ((op (op (op (op (var 0) (var 1)) (var 0)) (var 2)) (op (var 3) (var 1))) , (var 1)) → ⊥
  cut8019  adequate = bad8019  (Adequate.valid adequate Two boolean env8)
  bad8020 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b1) b0) b0) (bop b1 b1)) b0 → ⊥
  bad8020  p = false≢true (sym (cong lower p))
  cut8020 : Adequate {ℓ} ((op (op (op (op (var 0) (var 1)) (var 0)) (var 2)) (op (var 3) (var 1))) , (var 2)) → ⊥
  cut8020  adequate = bad8020  (Adequate.valid adequate Two boolean env13)
  bad8021 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b0) b0) b0) (bop b1 b0)) b1 → ⊥
  bad8021  p = false≢true (cong lower p)
  cut8021 : Adequate {ℓ} ((op (op (op (op (var 0) (var 1)) (var 0)) (var 2)) (op (var 3) (var 1))) , (var 3)) → ⊥
  cut8021  adequate = bad8021  (Adequate.valid adequate Two boolean env5)
  bad8022 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b0) b0) b0) (bop b0 b0)) b1 → ⊥
  bad8022  p = false≢true (cong lower p)
  cut8022 : Adequate {ℓ} ((op (op (op (op (var 0) (var 1)) (var 0)) (var 2)) (op (var 3) (var 1))) , (var 4)) → ⊥
  cut8022  adequate = bad8022  (Adequate.valid adequate Two boolean env9)
  bad8023 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b0) b0) b1) (bop b0 b1)) b0 → ⊥
  bad8023  p = false≢true (sym (cong lower p))
  cut8023 : Adequate {ℓ} ((op (op (op (op (var 0) (var 1)) (var 0)) (var 2)) (op (var 3) (var 2))) , (var 0)) → ⊥
  cut8023  adequate = bad8023  (Adequate.valid adequate Two boolean env8)
  bad8024 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b0) b0) b1) (bop b0 b1)) b0 → ⊥
  bad8024  p = false≢true (sym (cong lower p))
  cut8024 : Adequate {ℓ} ((op (op (op (op (var 0) (var 1)) (var 0)) (var 2)) (op (var 3) (var 2))) , (var 1)) → ⊥
  cut8024  adequate = bad8024  (Adequate.valid adequate Two boolean env8)
  bad8025 : PathP (λ _ → Two) (bop (bop (bop (bop b1 b0) b1) b1) (bop b0 b1)) b1 → ⊥
  bad8025  p = false≢true (cong lower p)
  cut8025 : Adequate {ℓ} ((op (op (op (op (var 0) (var 1)) (var 0)) (var 2)) (op (var 3) (var 2))) , (var 2)) → ⊥
  cut8025  adequate = bad8025  (Adequate.valid adequate Two boolean env18)
  bad8026 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b0) b0) b0) (bop b1 b0)) b1 → ⊥
  bad8026  p = false≢true (cong lower p)
  cut8026 : Adequate {ℓ} ((op (op (op (op (var 0) (var 1)) (var 0)) (var 2)) (op (var 3) (var 2))) , (var 3)) → ⊥
  cut8026  adequate = bad8026  (Adequate.valid adequate Two boolean env5)
  bad8027 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b0) b0) b0) (bop b0 b0)) b1 → ⊥
  bad8027  p = false≢true (cong lower p)
  cut8027 : Adequate {ℓ} ((op (op (op (op (var 0) (var 1)) (var 0)) (var 2)) (op (var 3) (var 2))) , (var 4)) → ⊥
  cut8027  adequate = bad8027  (Adequate.valid adequate Two boolean env9)
  bad8028 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b0) b0) b0) (bop b1 b1)) b0 → ⊥
  bad8028  p = false≢true (sym (cong lower p))
  cut8028 : Adequate {ℓ} ((op (op (op (op (var 0) (var 1)) (var 0)) (var 2)) (op (var 3) (var 3))) , (var 0)) → ⊥
  cut8028  adequate = bad8028  (Adequate.valid adequate Two boolean env5)
  bad8029 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b0) b0) b0) (bop b1 b1)) b0 → ⊥
  bad8029  p = false≢true (sym (cong lower p))
  cut8029 : Adequate {ℓ} ((op (op (op (op (var 0) (var 1)) (var 0)) (var 2)) (op (var 3) (var 3))) , (var 1)) → ⊥
  cut8029  adequate = bad8029  (Adequate.valid adequate Two boolean env5)
  bad8030 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b0) b0) b0) (bop b1 b1)) b0 → ⊥
  bad8030  p = false≢true (sym (cong lower p))
  cut8030 : Adequate {ℓ} ((op (op (op (op (var 0) (var 1)) (var 0)) (var 2)) (op (var 3) (var 3))) , (var 2)) → ⊥
  cut8030  adequate = bad8030  (Adequate.valid adequate Two boolean env5)
  bad8031 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b0) b0) b1) (bop b0 b0)) b0 → ⊥
  bad8031  p = false≢true (sym (cong lower p))
  cut8031 : Adequate {ℓ} ((op (op (op (op (var 0) (var 1)) (var 0)) (var 2)) (op (var 3) (var 3))) , (var 3)) → ⊥
  cut8031  adequate = bad8031  (Adequate.valid adequate Two boolean env8)
  bad8032 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b0) b0) b0) (bop b0 b0)) b1 → ⊥
  bad8032  p = false≢true (cong lower p)
  cut8032 : Adequate {ℓ} ((op (op (op (op (var 0) (var 1)) (var 0)) (var 2)) (op (var 3) (var 3))) , (var 4)) → ⊥
  cut8032  adequate = bad8032  (Adequate.valid adequate Two boolean env9)
  bad8033 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b0) b0) b0) (bop b1 b1)) b0 → ⊥
  bad8033  p = false≢true (sym (cong lower p))
  cut8033 : Adequate {ℓ} ((op (op (op (op (var 0) (var 1)) (var 0)) (var 2)) (op (var 3) (var 4))) , (var 0)) → ⊥
  cut8033  adequate = bad8033  (Adequate.valid adequate Two boolean env14)
  bad8034 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b0) b0) b0) (bop b1 b1)) b0 → ⊥
  bad8034  p = false≢true (sym (cong lower p))
  cut8034 : Adequate {ℓ} ((op (op (op (op (var 0) (var 1)) (var 0)) (var 2)) (op (var 3) (var 4))) , (var 1)) → ⊥
  cut8034  adequate = bad8034  (Adequate.valid adequate Two boolean env14)
  bad8035 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b0) b0) b0) (bop b1 b1)) b0 → ⊥
  bad8035  p = false≢true (sym (cong lower p))
  cut8035 : Adequate {ℓ} ((op (op (op (op (var 0) (var 1)) (var 0)) (var 2)) (op (var 3) (var 4))) , (var 2)) → ⊥
  cut8035  adequate = bad8035  (Adequate.valid adequate Two boolean env14)
  bad8036 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b0) b0) b0) (bop b1 b0)) b1 → ⊥
  bad8036  p = false≢true (cong lower p)
  cut8036 : Adequate {ℓ} ((op (op (op (op (var 0) (var 1)) (var 0)) (var 2)) (op (var 3) (var 4))) , (var 3)) → ⊥
  cut8036  adequate = bad8036  (Adequate.valid adequate Two boolean env15)
  bad8037 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b0) b0) b0) (bop b0 b1)) b1 → ⊥
  bad8037  p = false≢true (cong lower p)
  cut8037 : Adequate {ℓ} ((op (op (op (op (var 0) (var 1)) (var 0)) (var 2)) (op (var 3) (var 4))) , (var 4)) → ⊥
  cut8037  adequate = bad8037  (Adequate.valid adequate Two boolean env9)
  bad8038 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b0) b0) b0) (bop b0 b0)) b1 → ⊥
  bad8038  p = false≢true (cong lower p)
  cut8038 : Adequate {ℓ} ((op (op (op (op (var 0) (var 1)) (var 0)) (var 2)) (op (var 3) (var 4))) , (var 5)) → ⊥
  cut8038  adequate = bad8038  (Adequate.valid adequate Two boolean env16)
  holds8039 : (z0 z1 : A2) → (mul2 (mul2 (mul2 (mul2 z0 z1) z1) z0) (mul2 z0 z0)) ≡ z0
  holds8039 z0 z1 = refl
  cut8039 : Adequate {ℓ} ((op (op (op (op (var 0) (var 1)) (var 1)) (var 0)) (op (var 0) (var 0))) , (var 0)) → ⊥
  cut8039  = reject2 ((op (op (op (op (var 0) (var 1)) (var 1)) (var 0)) (op (var 0) (var 0))) , (var 0)) (λ env → holds8039 (env 0) (env 1))
  bad8040 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b1) b1) b0) (bop b0 b0)) b1 → ⊥
  bad8040  p = false≢true (cong lower p)
  cut8040 : Adequate {ℓ} ((op (op (op (op (var 0) (var 1)) (var 1)) (var 0)) (op (var 0) (var 0))) , (var 1)) → ⊥
  cut8040  adequate = bad8040  (Adequate.valid adequate Two boolean env0)
  bad8041 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b0) b0) b0) (bop b0 b0)) b1 → ⊥
  bad8041  p = false≢true (cong lower p)
  cut8041 : Adequate {ℓ} ((op (op (op (op (var 0) (var 1)) (var 1)) (var 0)) (op (var 0) (var 0))) , (var 2)) → ⊥
  cut8041  adequate = bad8041  (Adequate.valid adequate Two boolean env1)
  holds8042 : (z0 z1 : A2) → (mul2 (mul2 (mul2 (mul2 z0 z1) z1) z0) (mul2 z0 z1)) ≡ z0
  holds8042 z0 z1 = refl
  cut8042 : Adequate {ℓ} ((op (op (op (op (var 0) (var 1)) (var 1)) (var 0)) (op (var 0) (var 1))) , (var 0)) → ⊥
  cut8042  = reject2 ((op (op (op (op (var 0) (var 1)) (var 1)) (var 0)) (op (var 0) (var 1))) , (var 0)) (λ env → holds8042 (env 0) (env 1))
  bad8043 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b1) b1) b0) (bop b0 b1)) b1 → ⊥
  bad8043  p = false≢true (cong lower p)
  cut8043 : Adequate {ℓ} ((op (op (op (op (var 0) (var 1)) (var 1)) (var 0)) (op (var 0) (var 1))) , (var 1)) → ⊥
  cut8043  adequate = bad8043  (Adequate.valid adequate Two boolean env0)
  bad8044 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b0) b0) b0) (bop b0 b0)) b1 → ⊥
  bad8044  p = false≢true (cong lower p)
  cut8044 : Adequate {ℓ} ((op (op (op (op (var 0) (var 1)) (var 1)) (var 0)) (op (var 0) (var 1))) , (var 2)) → ⊥
  cut8044  adequate = bad8044  (Adequate.valid adequate Two boolean env1)
  holds8045 : (z0 z1 z2 : A2) → (mul2 (mul2 (mul2 (mul2 z0 z1) z1) z0) (mul2 z0 z2)) ≡ z0
  holds8045 z0 z1 z2 = refl
  cut8045 : Adequate {ℓ} ((op (op (op (op (var 0) (var 1)) (var 1)) (var 0)) (op (var 0) (var 2))) , (var 0)) → ⊥
  cut8045  = reject2 ((op (op (op (op (var 0) (var 1)) (var 1)) (var 0)) (op (var 0) (var 2))) , (var 0)) (λ env → holds8045 (env 0) (env 1) (env 2))
  bad8046 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b1) b1) b0) (bop b0 b0)) b1 → ⊥
  bad8046  p = false≢true (cong lower p)
  cut8046 : Adequate {ℓ} ((op (op (op (op (var 0) (var 1)) (var 1)) (var 0)) (op (var 0) (var 2))) , (var 1)) → ⊥
  cut8046  adequate = bad8046  (Adequate.valid adequate Two boolean env4)
  bad8047 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b0) b0) b0) (bop b0 b1)) b1 → ⊥
  bad8047  p = false≢true (cong lower p)
  cut8047 : Adequate {ℓ} ((op (op (op (op (var 0) (var 1)) (var 1)) (var 0)) (op (var 0) (var 2))) , (var 2)) → ⊥
  cut8047  adequate = bad8047  (Adequate.valid adequate Two boolean env1)
  bad8048 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b0) b0) b0) (bop b0 b0)) b1 → ⊥
  bad8048  p = false≢true (cong lower p)
  cut8048 : Adequate {ℓ} ((op (op (op (op (var 0) (var 1)) (var 1)) (var 0)) (op (var 0) (var 2))) , (var 3)) → ⊥
  cut8048  adequate = bad8048  (Adequate.valid adequate Two boolean env5)
  holds8049 : (z0 z1 : A2) → (mul2 (mul2 (mul2 (mul2 z0 z1) z1) z0) (mul2 z1 z0)) ≡ z0
  holds8049 z0 z1 = refl
  cut8049 : Adequate {ℓ} ((op (op (op (op (var 0) (var 1)) (var 1)) (var 0)) (op (var 1) (var 0))) , (var 0)) → ⊥
  cut8049  = reject2 ((op (op (op (op (var 0) (var 1)) (var 1)) (var 0)) (op (var 1) (var 0))) , (var 0)) (λ env → holds8049 (env 0) (env 1))
  bad8050 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b1) b1) b0) (bop b1 b0)) b1 → ⊥
  bad8050  p = false≢true (cong lower p)
  cut8050 : Adequate {ℓ} ((op (op (op (op (var 0) (var 1)) (var 1)) (var 0)) (op (var 1) (var 0))) , (var 1)) → ⊥
  cut8050  adequate = bad8050  (Adequate.valid adequate Two boolean env0)
  bad8051 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b0) b0) b0) (bop b0 b0)) b1 → ⊥
  bad8051  p = false≢true (cong lower p)
  cut8051 : Adequate {ℓ} ((op (op (op (op (var 0) (var 1)) (var 1)) (var 0)) (op (var 1) (var 0))) , (var 2)) → ⊥
  cut8051  adequate = bad8051  (Adequate.valid adequate Two boolean env1)
  bad8052 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b1) b1) b0) (bop b1 b1)) b0 → ⊥
  bad8052  p = false≢true (sym (cong lower p))
  cut8052 : Adequate {ℓ} ((op (op (op (op (var 0) (var 1)) (var 1)) (var 0)) (op (var 1) (var 1))) , (var 0)) → ⊥
  cut8052  adequate = bad8052  (Adequate.valid adequate Two boolean env0)
  bad8053 : PathP (λ _ → Two) (bop (bop (bop (bop b1 b0) b0) b1) (bop b0 b0)) b0 → ⊥
  bad8053  p = false≢true (sym (cong lower p))
  cut8053 : Adequate {ℓ} ((op (op (op (op (var 0) (var 1)) (var 1)) (var 0)) (op (var 1) (var 1))) , (var 1)) → ⊥
  cut8053  adequate = bad8053  (Adequate.valid adequate Two boolean env2)
  bad8054 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b0) b0) b0) (bop b0 b0)) b1 → ⊥
  bad8054  p = false≢true (cong lower p)
  cut8054 : Adequate {ℓ} ((op (op (op (op (var 0) (var 1)) (var 1)) (var 0)) (op (var 1) (var 1))) , (var 2)) → ⊥
  cut8054  adequate = bad8054  (Adequate.valid adequate Two boolean env1)
  bad8055 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b1) b1) b0) (bop b1 b1)) b0 → ⊥
  bad8055  p = false≢true (sym (cong lower p))
  cut8055 : Adequate {ℓ} ((op (op (op (op (var 0) (var 1)) (var 1)) (var 0)) (op (var 1) (var 2))) , (var 0)) → ⊥
  cut8055  adequate = bad8055  (Adequate.valid adequate Two boolean env3)
  bad8056 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b1) b1) b0) (bop b1 b0)) b1 → ⊥
  bad8056  p = false≢true (cong lower p)
  cut8056 : Adequate {ℓ} ((op (op (op (op (var 0) (var 1)) (var 1)) (var 0)) (op (var 1) (var 2))) , (var 1)) → ⊥
  cut8056  adequate = bad8056  (Adequate.valid adequate Two boolean env4)
  bad8057 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b0) b0) b0) (bop b0 b1)) b1 → ⊥
  bad8057  p = false≢true (cong lower p)
  cut8057 : Adequate {ℓ} ((op (op (op (op (var 0) (var 1)) (var 1)) (var 0)) (op (var 1) (var 2))) , (var 2)) → ⊥
  cut8057  adequate = bad8057  (Adequate.valid adequate Two boolean env1)
  bad8058 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b0) b0) b0) (bop b0 b0)) b1 → ⊥
  bad8058  p = false≢true (cong lower p)
  cut8058 : Adequate {ℓ} ((op (op (op (op (var 0) (var 1)) (var 1)) (var 0)) (op (var 1) (var 2))) , (var 3)) → ⊥
  cut8058  adequate = bad8058  (Adequate.valid adequate Two boolean env5)
  holds8059 : (z0 z1 z2 : A2) → (mul2 (mul2 (mul2 (mul2 z0 z1) z1) z0) (mul2 z2 z0)) ≡ z0
  holds8059 z0 z1 z2 = refl
  cut8059 : Adequate {ℓ} ((op (op (op (op (var 0) (var 1)) (var 1)) (var 0)) (op (var 2) (var 0))) , (var 0)) → ⊥
  cut8059  = reject2 ((op (op (op (op (var 0) (var 1)) (var 1)) (var 0)) (op (var 2) (var 0))) , (var 0)) (λ env → holds8059 (env 0) (env 1) (env 2))
  bad8060 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b1) b1) b0) (bop b0 b0)) b1 → ⊥
  bad8060  p = false≢true (cong lower p)
  cut8060 : Adequate {ℓ} ((op (op (op (op (var 0) (var 1)) (var 1)) (var 0)) (op (var 2) (var 0))) , (var 1)) → ⊥
  cut8060  adequate = bad8060  (Adequate.valid adequate Two boolean env4)
  bad8061 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b0) b0) b0) (bop b1 b0)) b1 → ⊥
  bad8061  p = false≢true (cong lower p)
  cut8061 : Adequate {ℓ} ((op (op (op (op (var 0) (var 1)) (var 1)) (var 0)) (op (var 2) (var 0))) , (var 2)) → ⊥
  cut8061  adequate = bad8061  (Adequate.valid adequate Two boolean env1)
  bad8062 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b0) b0) b0) (bop b0 b0)) b1 → ⊥
  bad8062  p = false≢true (cong lower p)
  cut8062 : Adequate {ℓ} ((op (op (op (op (var 0) (var 1)) (var 1)) (var 0)) (op (var 2) (var 0))) , (var 3)) → ⊥
  cut8062  adequate = bad8062  (Adequate.valid adequate Two boolean env5)
  bad8063 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b1) b1) b0) (bop b1 b1)) b0 → ⊥
  bad8063  p = false≢true (sym (cong lower p))
  cut8063 : Adequate {ℓ} ((op (op (op (op (var 0) (var 1)) (var 1)) (var 0)) (op (var 2) (var 1))) , (var 0)) → ⊥
  cut8063  adequate = bad8063  (Adequate.valid adequate Two boolean env3)
  bad8064 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b1) b1) b0) (bop b0 b1)) b1 → ⊥
  bad8064  p = false≢true (cong lower p)
  cut8064 : Adequate {ℓ} ((op (op (op (op (var 0) (var 1)) (var 1)) (var 0)) (op (var 2) (var 1))) , (var 1)) → ⊥
  cut8064  adequate = bad8064  (Adequate.valid adequate Two boolean env4)
  bad8065 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b0) b0) b0) (bop b1 b0)) b1 → ⊥
  bad8065  p = false≢true (cong lower p)
  cut8065 : Adequate {ℓ} ((op (op (op (op (var 0) (var 1)) (var 1)) (var 0)) (op (var 2) (var 1))) , (var 2)) → ⊥
  cut8065  adequate = bad8065  (Adequate.valid adequate Two boolean env1)
  bad8066 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b0) b0) b0) (bop b0 b0)) b1 → ⊥
  bad8066  p = false≢true (cong lower p)
  cut8066 : Adequate {ℓ} ((op (op (op (op (var 0) (var 1)) (var 1)) (var 0)) (op (var 2) (var 1))) , (var 3)) → ⊥
  cut8066  adequate = bad8066  (Adequate.valid adequate Two boolean env5)
  bad8067 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b0) b0) b0) (bop b1 b1)) b0 → ⊥
  bad8067  p = false≢true (sym (cong lower p))
  cut8067 : Adequate {ℓ} ((op (op (op (op (var 0) (var 1)) (var 1)) (var 0)) (op (var 2) (var 2))) , (var 0)) → ⊥
  cut8067  adequate = bad8067  (Adequate.valid adequate Two boolean env1)
  bad8068 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b0) b0) b0) (bop b1 b1)) b0 → ⊥
  bad8068  p = false≢true (sym (cong lower p))
  cut8068 : Adequate {ℓ} ((op (op (op (op (var 0) (var 1)) (var 1)) (var 0)) (op (var 2) (var 2))) , (var 1)) → ⊥
  cut8068  adequate = bad8068  (Adequate.valid adequate Two boolean env1)
  bad8069 : PathP (λ _ → Two) (bop (bop (bop (bop b1 b0) b0) b1) (bop b0 b0)) b0 → ⊥
  bad8069  p = false≢true (sym (cong lower p))
  cut8069 : Adequate {ℓ} ((op (op (op (op (var 0) (var 1)) (var 1)) (var 0)) (op (var 2) (var 2))) , (var 2)) → ⊥
  cut8069  adequate = bad8069  (Adequate.valid adequate Two boolean env10)
  bad8070 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b0) b0) b0) (bop b0 b0)) b1 → ⊥
  bad8070  p = false≢true (cong lower p)
  cut8070 : Adequate {ℓ} ((op (op (op (op (var 0) (var 1)) (var 1)) (var 0)) (op (var 2) (var 2))) , (var 3)) → ⊥
  cut8070  adequate = bad8070  (Adequate.valid adequate Two boolean env5)
  bad8071 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b0) b0) b0) (bop b1 b1)) b0 → ⊥
  bad8071  p = false≢true (sym (cong lower p))
  cut8071 : Adequate {ℓ} ((op (op (op (op (var 0) (var 1)) (var 1)) (var 0)) (op (var 2) (var 3))) , (var 0)) → ⊥
  cut8071  adequate = bad8071  (Adequate.valid adequate Two boolean env7)
  bad8072 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b0) b0) b0) (bop b1 b1)) b0 → ⊥
  bad8072  p = false≢true (sym (cong lower p))
  cut8072 : Adequate {ℓ} ((op (op (op (op (var 0) (var 1)) (var 1)) (var 0)) (op (var 2) (var 3))) , (var 1)) → ⊥
  cut8072  adequate = bad8072  (Adequate.valid adequate Two boolean env7)
  bad8073 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b0) b0) b0) (bop b1 b0)) b1 → ⊥
  bad8073  p = false≢true (cong lower p)
  cut8073 : Adequate {ℓ} ((op (op (op (op (var 0) (var 1)) (var 1)) (var 0)) (op (var 2) (var 3))) , (var 2)) → ⊥
  cut8073  adequate = bad8073  (Adequate.valid adequate Two boolean env8)
  bad8074 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b0) b0) b0) (bop b0 b1)) b1 → ⊥
  bad8074  p = false≢true (cong lower p)
  cut8074 : Adequate {ℓ} ((op (op (op (op (var 0) (var 1)) (var 1)) (var 0)) (op (var 2) (var 3))) , (var 3)) → ⊥
  cut8074  adequate = bad8074  (Adequate.valid adequate Two boolean env5)
  bad8075 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b0) b0) b0) (bop b0 b0)) b1 → ⊥
  bad8075  p = false≢true (cong lower p)
  cut8075 : Adequate {ℓ} ((op (op (op (op (var 0) (var 1)) (var 1)) (var 0)) (op (var 2) (var 3))) , (var 4)) → ⊥
  cut8075  adequate = bad8075  (Adequate.valid adequate Two boolean env9)
  holds8076 : (z0 z1 : A2) → (mul2 (mul2 (mul2 (mul2 z0 z1) z1) z1) (mul2 z0 z0)) ≡ z0
  holds8076 z0 z1 = refl
  cut8076 : Adequate {ℓ} ((op (op (op (op (var 0) (var 1)) (var 1)) (var 1)) (op (var 0) (var 0))) , (var 0)) → ⊥
  cut8076  = reject2 ((op (op (op (op (var 0) (var 1)) (var 1)) (var 1)) (op (var 0) (var 0))) , (var 0)) (λ env → holds8076 (env 0) (env 1))
  bad8077 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b1) b1) b1) (bop b0 b0)) b1 → ⊥
  bad8077  p = false≢true (cong lower p)
  cut8077 : Adequate {ℓ} ((op (op (op (op (var 0) (var 1)) (var 1)) (var 1)) (op (var 0) (var 0))) , (var 1)) → ⊥
  cut8077  adequate = bad8077  (Adequate.valid adequate Two boolean env0)
  bad8078 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b0) b0) b0) (bop b0 b0)) b1 → ⊥
  bad8078  p = false≢true (cong lower p)
  cut8078 : Adequate {ℓ} ((op (op (op (op (var 0) (var 1)) (var 1)) (var 1)) (op (var 0) (var 0))) , (var 2)) → ⊥
  cut8078  adequate = bad8078  (Adequate.valid adequate Two boolean env1)
  bad8079 : PathP (λ _ → Two) (bop (bop (bop (bop b1 b0) b0) b0) (bop b1 b0)) b1 → ⊥
  bad8079  p = false≢true (cong lower p)
  cut8079 : Adequate {ℓ} ((op (op (op (op (var 0) (var 1)) (var 1)) (var 1)) (op (var 0) (var 1))) , (var 0)) → ⊥
  cut8079  adequate = bad8079  (Adequate.valid adequate Two boolean env2)
  bad8080 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b1) b1) b1) (bop b0 b1)) b1 → ⊥
  bad8080  p = false≢true (cong lower p)
  cut8080 : Adequate {ℓ} ((op (op (op (op (var 0) (var 1)) (var 1)) (var 1)) (op (var 0) (var 1))) , (var 1)) → ⊥
  cut8080  adequate = bad8080  (Adequate.valid adequate Two boolean env0)
  bad8081 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b0) b0) b0) (bop b0 b0)) b1 → ⊥
  bad8081  p = false≢true (cong lower p)
  cut8081 : Adequate {ℓ} ((op (op (op (op (var 0) (var 1)) (var 1)) (var 1)) (op (var 0) (var 1))) , (var 2)) → ⊥
  cut8081  adequate = bad8081  (Adequate.valid adequate Two boolean env1)
  bad8082 : PathP (λ _ → Two) (bop (bop (bop (bop b1 b0) b0) b0) (bop b1 b0)) b1 → ⊥
  bad8082  p = false≢true (cong lower p)
  cut8082 : Adequate {ℓ} ((op (op (op (op (var 0) (var 1)) (var 1)) (var 1)) (op (var 0) (var 2))) , (var 0)) → ⊥
  cut8082  adequate = bad8082  (Adequate.valid adequate Two boolean env10)
  bad8083 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b1) b1) b1) (bop b0 b0)) b1 → ⊥
  bad8083  p = false≢true (cong lower p)
  cut8083 : Adequate {ℓ} ((op (op (op (op (var 0) (var 1)) (var 1)) (var 1)) (op (var 0) (var 2))) , (var 1)) → ⊥
  cut8083  adequate = bad8083  (Adequate.valid adequate Two boolean env4)
  bad8084 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b0) b0) b0) (bop b0 b1)) b1 → ⊥
  bad8084  p = false≢true (cong lower p)
  cut8084 : Adequate {ℓ} ((op (op (op (op (var 0) (var 1)) (var 1)) (var 1)) (op (var 0) (var 2))) , (var 2)) → ⊥
  cut8084  adequate = bad8084  (Adequate.valid adequate Two boolean env1)
  bad8085 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b0) b0) b0) (bop b0 b0)) b1 → ⊥
  bad8085  p = false≢true (cong lower p)
  cut8085 : Adequate {ℓ} ((op (op (op (op (var 0) (var 1)) (var 1)) (var 1)) (op (var 0) (var 2))) , (var 3)) → ⊥
  cut8085  adequate = bad8085  (Adequate.valid adequate Two boolean env5)
  bad8086 : PathP (λ _ → Two) (bop (bop (bop (bop b1 b0) b0) b0) (bop b0 b1)) b1 → ⊥
  bad8086  p = false≢true (cong lower p)
  cut8086 : Adequate {ℓ} ((op (op (op (op (var 0) (var 1)) (var 1)) (var 1)) (op (var 1) (var 0))) , (var 0)) → ⊥
  cut8086  adequate = bad8086  (Adequate.valid adequate Two boolean env2)
  bad8087 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b1) b1) b1) (bop b1 b0)) b1 → ⊥
  bad8087  p = false≢true (cong lower p)
  cut8087 : Adequate {ℓ} ((op (op (op (op (var 0) (var 1)) (var 1)) (var 1)) (op (var 1) (var 0))) , (var 1)) → ⊥
  cut8087  adequate = bad8087  (Adequate.valid adequate Two boolean env0)
  bad8088 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b0) b0) b0) (bop b0 b0)) b1 → ⊥
  bad8088  p = false≢true (cong lower p)
  cut8088 : Adequate {ℓ} ((op (op (op (op (var 0) (var 1)) (var 1)) (var 1)) (op (var 1) (var 0))) , (var 2)) → ⊥
  cut8088  adequate = bad8088  (Adequate.valid adequate Two boolean env1)
  bad8089 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b1) b1) b1) (bop b1 b1)) b0 → ⊥
  bad8089  p = false≢true (sym (cong lower p))
  cut8089 : Adequate {ℓ} ((op (op (op (op (var 0) (var 1)) (var 1)) (var 1)) (op (var 1) (var 1))) , (var 0)) → ⊥
  cut8089  adequate = bad8089  (Adequate.valid adequate Two boolean env0)
  holds8090 : (z0 z1 : A3) → (mul3 (mul3 (mul3 (mul3 z0 z1) z1) z1) (mul3 z1 z1)) ≡ z1
  holds8090 z0 z1 = refl
  cut8090 : Adequate {ℓ} ((op (op (op (op (var 0) (var 1)) (var 1)) (var 1)) (op (var 1) (var 1))) , (var 1)) → ⊥
  cut8090  = reject3 ((op (op (op (op (var 0) (var 1)) (var 1)) (var 1)) (op (var 1) (var 1))) , (var 1)) (λ env → holds8090 (env 0) (env 1))
  bad8091 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b0) b0) b0) (bop b0 b0)) b1 → ⊥
  bad8091  p = false≢true (cong lower p)
  cut8091 : Adequate {ℓ} ((op (op (op (op (var 0) (var 1)) (var 1)) (var 1)) (op (var 1) (var 1))) , (var 2)) → ⊥
  cut8091  adequate = bad8091  (Adequate.valid adequate Two boolean env1)
  bad8092 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b1) b1) b1) (bop b1 b1)) b0 → ⊥
  bad8092  p = false≢true (sym (cong lower p))
  cut8092 : Adequate {ℓ} ((op (op (op (op (var 0) (var 1)) (var 1)) (var 1)) (op (var 1) (var 2))) , (var 0)) → ⊥
  cut8092  adequate = bad8092  (Adequate.valid adequate Two boolean env3)
  bad8093 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b1) b1) b1) (bop b1 b0)) b1 → ⊥
  bad8093  p = false≢true (cong lower p)
  cut8093 : Adequate {ℓ} ((op (op (op (op (var 0) (var 1)) (var 1)) (var 1)) (op (var 1) (var 2))) , (var 1)) → ⊥
  cut8093  adequate = bad8093  (Adequate.valid adequate Two boolean env4)
  bad8094 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b0) b0) b0) (bop b0 b1)) b1 → ⊥
  bad8094  p = false≢true (cong lower p)
  cut8094 : Adequate {ℓ} ((op (op (op (op (var 0) (var 1)) (var 1)) (var 1)) (op (var 1) (var 2))) , (var 2)) → ⊥
  cut8094  adequate = bad8094  (Adequate.valid adequate Two boolean env1)
  bad8095 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b0) b0) b0) (bop b0 b0)) b1 → ⊥
  bad8095  p = false≢true (cong lower p)
  cut8095 : Adequate {ℓ} ((op (op (op (op (var 0) (var 1)) (var 1)) (var 1)) (op (var 1) (var 2))) , (var 3)) → ⊥
  cut8095  adequate = bad8095  (Adequate.valid adequate Two boolean env5)
  bad8096 : PathP (λ _ → Two) (bop (bop (bop (bop b1 b0) b0) b0) (bop b0 b1)) b1 → ⊥
  bad8096  p = false≢true (cong lower p)
  cut8096 : Adequate {ℓ} ((op (op (op (op (var 0) (var 1)) (var 1)) (var 1)) (op (var 2) (var 0))) , (var 0)) → ⊥
  cut8096  adequate = bad8096  (Adequate.valid adequate Two boolean env10)
  bad8097 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b1) b1) b1) (bop b0 b0)) b1 → ⊥
  bad8097  p = false≢true (cong lower p)
  cut8097 : Adequate {ℓ} ((op (op (op (op (var 0) (var 1)) (var 1)) (var 1)) (op (var 2) (var 0))) , (var 1)) → ⊥
  cut8097  adequate = bad8097  (Adequate.valid adequate Two boolean env4)
  bad8098 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b0) b0) b0) (bop b1 b0)) b1 → ⊥
  bad8098  p = false≢true (cong lower p)
  cut8098 : Adequate {ℓ} ((op (op (op (op (var 0) (var 1)) (var 1)) (var 1)) (op (var 2) (var 0))) , (var 2)) → ⊥
  cut8098  adequate = bad8098  (Adequate.valid adequate Two boolean env1)
  bad8099 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b0) b0) b0) (bop b0 b0)) b1 → ⊥
  bad8099  p = false≢true (cong lower p)
  cut8099 : Adequate {ℓ} ((op (op (op (op (var 0) (var 1)) (var 1)) (var 1)) (op (var 2) (var 0))) , (var 3)) → ⊥
  cut8099  adequate = bad8099  (Adequate.valid adequate Two boolean env5)
  bad8100 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b1) b1) b1) (bop b1 b1)) b0 → ⊥
  bad8100  p = false≢true (sym (cong lower p))
  cut8100 : Adequate {ℓ} ((op (op (op (op (var 0) (var 1)) (var 1)) (var 1)) (op (var 2) (var 1))) , (var 0)) → ⊥
  cut8100  adequate = bad8100  (Adequate.valid adequate Two boolean env3)
  bad8101 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b1) b1) b1) (bop b0 b1)) b1 → ⊥
  bad8101  p = false≢true (cong lower p)
  cut8101 : Adequate {ℓ} ((op (op (op (op (var 0) (var 1)) (var 1)) (var 1)) (op (var 2) (var 1))) , (var 1)) → ⊥
  cut8101  adequate = bad8101  (Adequate.valid adequate Two boolean env4)
  bad8102 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b0) b0) b0) (bop b1 b0)) b1 → ⊥
  bad8102  p = false≢true (cong lower p)
  cut8102 : Adequate {ℓ} ((op (op (op (op (var 0) (var 1)) (var 1)) (var 1)) (op (var 2) (var 1))) , (var 2)) → ⊥
  cut8102  adequate = bad8102  (Adequate.valid adequate Two boolean env1)
  bad8103 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b0) b0) b0) (bop b0 b0)) b1 → ⊥
  bad8103  p = false≢true (cong lower p)
  cut8103 : Adequate {ℓ} ((op (op (op (op (var 0) (var 1)) (var 1)) (var 1)) (op (var 2) (var 1))) , (var 3)) → ⊥
  cut8103  adequate = bad8103  (Adequate.valid adequate Two boolean env5)
  bad8104 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b0) b0) b0) (bop b1 b1)) b0 → ⊥
  bad8104  p = false≢true (sym (cong lower p))
  cut8104 : Adequate {ℓ} ((op (op (op (op (var 0) (var 1)) (var 1)) (var 1)) (op (var 2) (var 2))) , (var 0)) → ⊥
  cut8104  adequate = bad8104  (Adequate.valid adequate Two boolean env1)
  bad8105 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b0) b0) b0) (bop b1 b1)) b0 → ⊥
  bad8105  p = false≢true (sym (cong lower p))
  cut8105 : Adequate {ℓ} ((op (op (op (op (var 0) (var 1)) (var 1)) (var 1)) (op (var 2) (var 2))) , (var 1)) → ⊥
  cut8105  adequate = bad8105  (Adequate.valid adequate Two boolean env1)
  bad8106 : PathP (λ _ → Two) (bop (bop (bop (bop b1 b1) b1) b1) (bop b0 b0)) b0 → ⊥
  bad8106  p = false≢true (sym (cong lower p))
  cut8106 : Adequate {ℓ} ((op (op (op (op (var 0) (var 1)) (var 1)) (var 1)) (op (var 2) (var 2))) , (var 2)) → ⊥
  cut8106  adequate = bad8106  (Adequate.valid adequate Two boolean env11)
  bad8107 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b0) b0) b0) (bop b0 b0)) b1 → ⊥
  bad8107  p = false≢true (cong lower p)
  cut8107 : Adequate {ℓ} ((op (op (op (op (var 0) (var 1)) (var 1)) (var 1)) (op (var 2) (var 2))) , (var 3)) → ⊥
  cut8107  adequate = bad8107  (Adequate.valid adequate Two boolean env5)
  bad8108 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b0) b0) b0) (bop b1 b1)) b0 → ⊥
  bad8108  p = false≢true (sym (cong lower p))
  cut8108 : Adequate {ℓ} ((op (op (op (op (var 0) (var 1)) (var 1)) (var 1)) (op (var 2) (var 3))) , (var 0)) → ⊥
  cut8108  adequate = bad8108  (Adequate.valid adequate Two boolean env7)
  bad8109 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b0) b0) b0) (bop b1 b1)) b0 → ⊥
  bad8109  p = false≢true (sym (cong lower p))
  cut8109 : Adequate {ℓ} ((op (op (op (op (var 0) (var 1)) (var 1)) (var 1)) (op (var 2) (var 3))) , (var 1)) → ⊥
  cut8109  adequate = bad8109  (Adequate.valid adequate Two boolean env7)
  bad8110 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b0) b0) b0) (bop b1 b0)) b1 → ⊥
  bad8110  p = false≢true (cong lower p)
  cut8110 : Adequate {ℓ} ((op (op (op (op (var 0) (var 1)) (var 1)) (var 1)) (op (var 2) (var 3))) , (var 2)) → ⊥
  cut8110  adequate = bad8110  (Adequate.valid adequate Two boolean env8)
  bad8111 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b0) b0) b0) (bop b0 b1)) b1 → ⊥
  bad8111  p = false≢true (cong lower p)
  cut8111 : Adequate {ℓ} ((op (op (op (op (var 0) (var 1)) (var 1)) (var 1)) (op (var 2) (var 3))) , (var 3)) → ⊥
  cut8111  adequate = bad8111  (Adequate.valid adequate Two boolean env5)
  bad8112 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b0) b0) b0) (bop b0 b0)) b1 → ⊥
  bad8112  p = false≢true (cong lower p)
  cut8112 : Adequate {ℓ} ((op (op (op (op (var 0) (var 1)) (var 1)) (var 1)) (op (var 2) (var 3))) , (var 4)) → ⊥
  cut8112  adequate = bad8112  (Adequate.valid adequate Two boolean env9)
  bad8113 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b0) b0) b1) (bop b0 b0)) b0 → ⊥
  bad8113  p = false≢true (sym (cong lower p))
  cut8113 : Adequate {ℓ} ((op (op (op (op (var 0) (var 1)) (var 1)) (var 2)) (op (var 0) (var 0))) , (var 0)) → ⊥
  cut8113  adequate = bad8113  (Adequate.valid adequate Two boolean env1)
  bad8114 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b0) b0) b1) (bop b0 b0)) b0 → ⊥
  bad8114  p = false≢true (sym (cong lower p))
  cut8114 : Adequate {ℓ} ((op (op (op (op (var 0) (var 1)) (var 1)) (var 2)) (op (var 0) (var 0))) , (var 1)) → ⊥
  cut8114  adequate = bad8114  (Adequate.valid adequate Two boolean env1)
  bad8115 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b1) b1) b1) (bop b0 b0)) b1 → ⊥
  bad8115  p = false≢true (cong lower p)
  cut8115 : Adequate {ℓ} ((op (op (op (op (var 0) (var 1)) (var 1)) (var 2)) (op (var 0) (var 0))) , (var 2)) → ⊥
  cut8115  adequate = bad8115  (Adequate.valid adequate Two boolean env3)
  bad8116 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b0) b0) b0) (bop b0 b0)) b1 → ⊥
  bad8116  p = false≢true (cong lower p)
  cut8116 : Adequate {ℓ} ((op (op (op (op (var 0) (var 1)) (var 1)) (var 2)) (op (var 0) (var 0))) , (var 3)) → ⊥
  cut8116  adequate = bad8116  (Adequate.valid adequate Two boolean env5)
  bad8117 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b0) b0) b1) (bop b0 b0)) b0 → ⊥
  bad8117  p = false≢true (sym (cong lower p))
  cut8117 : Adequate {ℓ} ((op (op (op (op (var 0) (var 1)) (var 1)) (var 2)) (op (var 0) (var 1))) , (var 0)) → ⊥
  cut8117  adequate = bad8117  (Adequate.valid adequate Two boolean env1)
  bad8118 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b0) b0) b1) (bop b0 b0)) b0 → ⊥
  bad8118  p = false≢true (sym (cong lower p))
  cut8118 : Adequate {ℓ} ((op (op (op (op (var 0) (var 1)) (var 1)) (var 2)) (op (var 0) (var 1))) , (var 1)) → ⊥
  cut8118  adequate = bad8118  (Adequate.valid adequate Two boolean env1)
  bad8119 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b1) b1) b1) (bop b0 b1)) b1 → ⊥
  bad8119  p = false≢true (cong lower p)
  cut8119 : Adequate {ℓ} ((op (op (op (op (var 0) (var 1)) (var 1)) (var 2)) (op (var 0) (var 1))) , (var 2)) → ⊥
  cut8119  adequate = bad8119  (Adequate.valid adequate Two boolean env3)
  bad8120 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b0) b0) b0) (bop b0 b0)) b1 → ⊥
  bad8120  p = false≢true (cong lower p)
  cut8120 : Adequate {ℓ} ((op (op (op (op (var 0) (var 1)) (var 1)) (var 2)) (op (var 0) (var 1))) , (var 3)) → ⊥
  cut8120  adequate = bad8120  (Adequate.valid adequate Two boolean env5)
  bad8121 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b0) b0) b1) (bop b0 b1)) b0 → ⊥
  bad8121  p = false≢true (sym (cong lower p))
  cut8121 : Adequate {ℓ} ((op (op (op (op (var 0) (var 1)) (var 1)) (var 2)) (op (var 0) (var 2))) , (var 0)) → ⊥
  cut8121  adequate = bad8121  (Adequate.valid adequate Two boolean env1)
  bad8122 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b0) b0) b1) (bop b0 b1)) b0 → ⊥
  bad8122  p = false≢true (sym (cong lower p))
  cut8122 : Adequate {ℓ} ((op (op (op (op (var 0) (var 1)) (var 1)) (var 2)) (op (var 0) (var 2))) , (var 1)) → ⊥
  cut8122  adequate = bad8122  (Adequate.valid adequate Two boolean env1)
  bad8123 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b1) b1) b1) (bop b0 b1)) b1 → ⊥
  bad8123  p = false≢true (cong lower p)
  cut8123 : Adequate {ℓ} ((op (op (op (op (var 0) (var 1)) (var 1)) (var 2)) (op (var 0) (var 2))) , (var 2)) → ⊥
  cut8123  adequate = bad8123  (Adequate.valid adequate Two boolean env3)
  bad8124 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b0) b0) b0) (bop b0 b0)) b1 → ⊥
  bad8124  p = false≢true (cong lower p)
  cut8124 : Adequate {ℓ} ((op (op (op (op (var 0) (var 1)) (var 1)) (var 2)) (op (var 0) (var 2))) , (var 3)) → ⊥
  cut8124  adequate = bad8124  (Adequate.valid adequate Two boolean env5)
  bad8125 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b0) b0) b1) (bop b0 b0)) b0 → ⊥
  bad8125  p = false≢true (sym (cong lower p))
  cut8125 : Adequate {ℓ} ((op (op (op (op (var 0) (var 1)) (var 1)) (var 2)) (op (var 0) (var 3))) , (var 0)) → ⊥
  cut8125  adequate = bad8125  (Adequate.valid adequate Two boolean env8)
  bad8126 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b0) b0) b1) (bop b0 b0)) b0 → ⊥
  bad8126  p = false≢true (sym (cong lower p))
  cut8126 : Adequate {ℓ} ((op (op (op (op (var 0) (var 1)) (var 1)) (var 2)) (op (var 0) (var 3))) , (var 1)) → ⊥
  cut8126  adequate = bad8126  (Adequate.valid adequate Two boolean env8)
  bad8127 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b1) b1) b1) (bop b0 b0)) b1 → ⊥
  bad8127  p = false≢true (cong lower p)
  cut8127 : Adequate {ℓ} ((op (op (op (op (var 0) (var 1)) (var 1)) (var 2)) (op (var 0) (var 3))) , (var 2)) → ⊥
  cut8127  adequate = bad8127  (Adequate.valid adequate Two boolean env12)
  bad8128 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b0) b0) b0) (bop b0 b1)) b1 → ⊥
  bad8128  p = false≢true (cong lower p)
  cut8128 : Adequate {ℓ} ((op (op (op (op (var 0) (var 1)) (var 1)) (var 2)) (op (var 0) (var 3))) , (var 3)) → ⊥
  cut8128  adequate = bad8128  (Adequate.valid adequate Two boolean env5)
  bad8129 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b0) b0) b0) (bop b0 b0)) b1 → ⊥
  bad8129  p = false≢true (cong lower p)
  cut8129 : Adequate {ℓ} ((op (op (op (op (var 0) (var 1)) (var 1)) (var 2)) (op (var 0) (var 3))) , (var 4)) → ⊥
  cut8129  adequate = bad8129  (Adequate.valid adequate Two boolean env9)
  bad8130 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b0) b0) b1) (bop b0 b0)) b0 → ⊥
  bad8130  p = false≢true (sym (cong lower p))
  cut8130 : Adequate {ℓ} ((op (op (op (op (var 0) (var 1)) (var 1)) (var 2)) (op (var 1) (var 0))) , (var 0)) → ⊥
  cut8130  adequate = bad8130  (Adequate.valid adequate Two boolean env1)
  bad8131 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b0) b0) b1) (bop b0 b0)) b0 → ⊥
  bad8131  p = false≢true (sym (cong lower p))
  cut8131 : Adequate {ℓ} ((op (op (op (op (var 0) (var 1)) (var 1)) (var 2)) (op (var 1) (var 0))) , (var 1)) → ⊥
  cut8131  adequate = bad8131  (Adequate.valid adequate Two boolean env1)
  bad8132 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b1) b1) b1) (bop b1 b0)) b1 → ⊥
  bad8132  p = false≢true (cong lower p)
  cut8132 : Adequate {ℓ} ((op (op (op (op (var 0) (var 1)) (var 1)) (var 2)) (op (var 1) (var 0))) , (var 2)) → ⊥
  cut8132  adequate = bad8132  (Adequate.valid adequate Two boolean env3)
  bad8133 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b0) b0) b0) (bop b0 b0)) b1 → ⊥
  bad8133  p = false≢true (cong lower p)
  cut8133 : Adequate {ℓ} ((op (op (op (op (var 0) (var 1)) (var 1)) (var 2)) (op (var 1) (var 0))) , (var 3)) → ⊥
  cut8133  adequate = bad8133  (Adequate.valid adequate Two boolean env5)
  bad8134 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b0) b0) b1) (bop b0 b0)) b0 → ⊥
  bad8134  p = false≢true (sym (cong lower p))
  cut8134 : Adequate {ℓ} ((op (op (op (op (var 0) (var 1)) (var 1)) (var 2)) (op (var 1) (var 1))) , (var 0)) → ⊥
  cut8134  adequate = bad8134  (Adequate.valid adequate Two boolean env1)
  bad8135 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b0) b0) b1) (bop b0 b0)) b0 → ⊥
  bad8135  p = false≢true (sym (cong lower p))
  cut8135 : Adequate {ℓ} ((op (op (op (op (var 0) (var 1)) (var 1)) (var 2)) (op (var 1) (var 1))) , (var 1)) → ⊥
  cut8135  adequate = bad8135  (Adequate.valid adequate Two boolean env1)
  bad8136 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b1) b1) b0) (bop b1 b1)) b0 → ⊥
  bad8136  p = false≢true (sym (cong lower p))
  cut8136 : Adequate {ℓ} ((op (op (op (op (var 0) (var 1)) (var 1)) (var 2)) (op (var 1) (var 1))) , (var 2)) → ⊥
  cut8136  adequate = bad8136  (Adequate.valid adequate Two boolean env4)
  bad8137 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b0) b0) b0) (bop b0 b0)) b1 → ⊥
  bad8137  p = false≢true (cong lower p)
  cut8137 : Adequate {ℓ} ((op (op (op (op (var 0) (var 1)) (var 1)) (var 2)) (op (var 1) (var 1))) , (var 3)) → ⊥
  cut8137  adequate = bad8137  (Adequate.valid adequate Two boolean env5)
  bad8138 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b0) b0) b1) (bop b0 b1)) b0 → ⊥
  bad8138  p = false≢true (sym (cong lower p))
  cut8138 : Adequate {ℓ} ((op (op (op (op (var 0) (var 1)) (var 1)) (var 2)) (op (var 1) (var 2))) , (var 0)) → ⊥
  cut8138  adequate = bad8138  (Adequate.valid adequate Two boolean env1)
  bad8139 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b0) b0) b1) (bop b0 b1)) b0 → ⊥
  bad8139  p = false≢true (sym (cong lower p))
  cut8139 : Adequate {ℓ} ((op (op (op (op (var 0) (var 1)) (var 1)) (var 2)) (op (var 1) (var 2))) , (var 1)) → ⊥
  cut8139  adequate = bad8139  (Adequate.valid adequate Two boolean env1)
  holds8140 : (z0 z1 z2 : A3) → (mul3 (mul3 (mul3 (mul3 z0 z1) z1) z2) (mul3 z1 z2)) ≡ z2
  holds8140 z0 z1 z2 = refl
  cut8140 : Adequate {ℓ} ((op (op (op (op (var 0) (var 1)) (var 1)) (var 2)) (op (var 1) (var 2))) , (var 2)) → ⊥
  cut8140  = reject3 ((op (op (op (op (var 0) (var 1)) (var 1)) (var 2)) (op (var 1) (var 2))) , (var 2)) (λ env → holds8140 (env 0) (env 1) (env 2))
  bad8141 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b0) b0) b0) (bop b0 b0)) b1 → ⊥
  bad8141  p = false≢true (cong lower p)
  cut8141 : Adequate {ℓ} ((op (op (op (op (var 0) (var 1)) (var 1)) (var 2)) (op (var 1) (var 2))) , (var 3)) → ⊥
  cut8141  adequate = bad8141  (Adequate.valid adequate Two boolean env5)
  bad8142 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b0) b0) b1) (bop b0 b0)) b0 → ⊥
  bad8142  p = false≢true (sym (cong lower p))
  cut8142 : Adequate {ℓ} ((op (op (op (op (var 0) (var 1)) (var 1)) (var 2)) (op (var 1) (var 3))) , (var 0)) → ⊥
  cut8142  adequate = bad8142  (Adequate.valid adequate Two boolean env8)
  bad8143 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b0) b0) b1) (bop b0 b0)) b0 → ⊥
  bad8143  p = false≢true (sym (cong lower p))
  cut8143 : Adequate {ℓ} ((op (op (op (op (var 0) (var 1)) (var 1)) (var 2)) (op (var 1) (var 3))) , (var 1)) → ⊥
  cut8143  adequate = bad8143  (Adequate.valid adequate Two boolean env8)
  bad8144 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b1) b1) b0) (bop b1 b1)) b0 → ⊥
  bad8144  p = false≢true (sym (cong lower p))
  cut8144 : Adequate {ℓ} ((op (op (op (op (var 0) (var 1)) (var 1)) (var 2)) (op (var 1) (var 3))) , (var 2)) → ⊥
  cut8144  adequate = bad8144  (Adequate.valid adequate Two boolean env13)
  bad8145 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b0) b0) b0) (bop b0 b1)) b1 → ⊥
  bad8145  p = false≢true (cong lower p)
  cut8145 : Adequate {ℓ} ((op (op (op (op (var 0) (var 1)) (var 1)) (var 2)) (op (var 1) (var 3))) , (var 3)) → ⊥
  cut8145  adequate = bad8145  (Adequate.valid adequate Two boolean env5)
  bad8146 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b0) b0) b0) (bop b0 b0)) b1 → ⊥
  bad8146  p = false≢true (cong lower p)
  cut8146 : Adequate {ℓ} ((op (op (op (op (var 0) (var 1)) (var 1)) (var 2)) (op (var 1) (var 3))) , (var 4)) → ⊥
  cut8146  adequate = bad8146  (Adequate.valid adequate Two boolean env9)
  bad8147 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b0) b0) b1) (bop b1 b0)) b0 → ⊥
  bad8147  p = false≢true (sym (cong lower p))
  cut8147 : Adequate {ℓ} ((op (op (op (op (var 0) (var 1)) (var 1)) (var 2)) (op (var 2) (var 0))) , (var 0)) → ⊥
  cut8147  adequate = bad8147  (Adequate.valid adequate Two boolean env1)
  bad8148 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b0) b0) b1) (bop b1 b0)) b0 → ⊥
  bad8148  p = false≢true (sym (cong lower p))
  cut8148 : Adequate {ℓ} ((op (op (op (op (var 0) (var 1)) (var 1)) (var 2)) (op (var 2) (var 0))) , (var 1)) → ⊥
  cut8148  adequate = bad8148  (Adequate.valid adequate Two boolean env1)
  bad8149 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b1) b1) b1) (bop b1 b0)) b1 → ⊥
  bad8149  p = false≢true (cong lower p)
  cut8149 : Adequate {ℓ} ((op (op (op (op (var 0) (var 1)) (var 1)) (var 2)) (op (var 2) (var 0))) , (var 2)) → ⊥
  cut8149  adequate = bad8149  (Adequate.valid adequate Two boolean env3)
  bad8150 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b0) b0) b0) (bop b0 b0)) b1 → ⊥
  bad8150  p = false≢true (cong lower p)
  cut8150 : Adequate {ℓ} ((op (op (op (op (var 0) (var 1)) (var 1)) (var 2)) (op (var 2) (var 0))) , (var 3)) → ⊥
  cut8150  adequate = bad8150  (Adequate.valid adequate Two boolean env5)
  bad8151 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b0) b0) b1) (bop b1 b0)) b0 → ⊥
  bad8151  p = false≢true (sym (cong lower p))
  cut8151 : Adequate {ℓ} ((op (op (op (op (var 0) (var 1)) (var 1)) (var 2)) (op (var 2) (var 1))) , (var 0)) → ⊥
  cut8151  adequate = bad8151  (Adequate.valid adequate Two boolean env1)
  bad8152 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b0) b0) b1) (bop b1 b0)) b0 → ⊥
  bad8152  p = false≢true (sym (cong lower p))
  cut8152 : Adequate {ℓ} ((op (op (op (op (var 0) (var 1)) (var 1)) (var 2)) (op (var 2) (var 1))) , (var 1)) → ⊥
  cut8152  adequate = bad8152  (Adequate.valid adequate Two boolean env1)
  holds8153 : (z0 z1 z2 : A12) → (mul12 (mul12 (mul12 (mul12 z0 z1) z1) z2) (mul12 z2 z1)) ≡ z2
  holds8153 m12c0 m12c0 m12c0 = refl
  holds8153 m12c0 m12c0 m12c1 = refl
  holds8153 m12c0 m12c0 m12c2 = refl
  holds8153 m12c0 m12c1 m12c0 = refl
  holds8153 m12c0 m12c1 m12c1 = refl
  holds8153 m12c0 m12c1 m12c2 = refl
  holds8153 m12c0 m12c2 m12c0 = refl
  holds8153 m12c0 m12c2 m12c1 = refl
  holds8153 m12c0 m12c2 m12c2 = refl
  holds8153 m12c1 m12c0 m12c0 = refl
  holds8153 m12c1 m12c0 m12c1 = refl
  holds8153 m12c1 m12c0 m12c2 = refl
  holds8153 m12c1 m12c1 m12c0 = refl
  holds8153 m12c1 m12c1 m12c1 = refl
  holds8153 m12c1 m12c1 m12c2 = refl
  holds8153 m12c1 m12c2 m12c0 = refl
  holds8153 m12c1 m12c2 m12c1 = refl
  holds8153 m12c1 m12c2 m12c2 = refl
  holds8153 m12c2 m12c0 m12c0 = refl
  holds8153 m12c2 m12c0 m12c1 = refl
  holds8153 m12c2 m12c0 m12c2 = refl
  holds8153 m12c2 m12c1 m12c0 = refl
  holds8153 m12c2 m12c1 m12c1 = refl
  holds8153 m12c2 m12c1 m12c2 = refl
  holds8153 m12c2 m12c2 m12c0 = refl
  holds8153 m12c2 m12c2 m12c1 = refl
  holds8153 m12c2 m12c2 m12c2 = refl
  cut8153 : Adequate {ℓ} ((op (op (op (op (var 0) (var 1)) (var 1)) (var 2)) (op (var 2) (var 1))) , (var 2)) → ⊥
  cut8153  = reject12 ((op (op (op (op (var 0) (var 1)) (var 1)) (var 2)) (op (var 2) (var 1))) , (var 2)) (λ env → holds8153 (env 0) (env 1) (env 2))
  bad8154 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b0) b0) b0) (bop b0 b0)) b1 → ⊥
  bad8154  p = false≢true (cong lower p)
  cut8154 : Adequate {ℓ} ((op (op (op (op (var 0) (var 1)) (var 1)) (var 2)) (op (var 2) (var 1))) , (var 3)) → ⊥
  cut8154  adequate = bad8154  (Adequate.valid adequate Two boolean env5)
  bad8155 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b0) b0) b1) (bop b1 b1)) b0 → ⊥
  bad8155  p = false≢true (sym (cong lower p))
  cut8155 : Adequate {ℓ} ((op (op (op (op (var 0) (var 1)) (var 1)) (var 2)) (op (var 2) (var 2))) , (var 0)) → ⊥
  cut8155  adequate = bad8155  (Adequate.valid adequate Two boolean env1)
  bad8156 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b0) b0) b1) (bop b1 b1)) b0 → ⊥
  bad8156  p = false≢true (sym (cong lower p))
  cut8156 : Adequate {ℓ} ((op (op (op (op (var 0) (var 1)) (var 1)) (var 2)) (op (var 2) (var 2))) , (var 1)) → ⊥
  cut8156  adequate = bad8156  (Adequate.valid adequate Two boolean env1)
  holds8157 : (z0 z1 z2 : A3) → (mul3 (mul3 (mul3 (mul3 z0 z1) z1) z2) (mul3 z2 z2)) ≡ z2
  holds8157 z0 z1 z2 = refl
  cut8157 : Adequate {ℓ} ((op (op (op (op (var 0) (var 1)) (var 1)) (var 2)) (op (var 2) (var 2))) , (var 2)) → ⊥
  cut8157  = reject3 ((op (op (op (op (var 0) (var 1)) (var 1)) (var 2)) (op (var 2) (var 2))) , (var 2)) (λ env → holds8157 (env 0) (env 1) (env 2))
  bad8158 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b0) b0) b0) (bop b0 b0)) b1 → ⊥
  bad8158  p = false≢true (cong lower p)
  cut8158 : Adequate {ℓ} ((op (op (op (op (var 0) (var 1)) (var 1)) (var 2)) (op (var 2) (var 2))) , (var 3)) → ⊥
  cut8158  adequate = bad8158  (Adequate.valid adequate Two boolean env5)
  bad8159 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b0) b0) b1) (bop b1 b0)) b0 → ⊥
  bad8159  p = false≢true (sym (cong lower p))
  cut8159 : Adequate {ℓ} ((op (op (op (op (var 0) (var 1)) (var 1)) (var 2)) (op (var 2) (var 3))) , (var 0)) → ⊥
  cut8159  adequate = bad8159  (Adequate.valid adequate Two boolean env8)
  bad8160 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b0) b0) b1) (bop b1 b0)) b0 → ⊥
  bad8160  p = false≢true (sym (cong lower p))
  cut8160 : Adequate {ℓ} ((op (op (op (op (var 0) (var 1)) (var 1)) (var 2)) (op (var 2) (var 3))) , (var 1)) → ⊥
  cut8160  adequate = bad8160  (Adequate.valid adequate Two boolean env8)
  bad8161 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b1) b1) b1) (bop b1 b0)) b1 → ⊥
  bad8161  p = false≢true (cong lower p)
  cut8161 : Adequate {ℓ} ((op (op (op (op (var 0) (var 1)) (var 1)) (var 2)) (op (var 2) (var 3))) , (var 2)) → ⊥
  cut8161  adequate = bad8161  (Adequate.valid adequate Two boolean env12)
  bad8162 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b0) b0) b0) (bop b0 b1)) b1 → ⊥
  bad8162  p = false≢true (cong lower p)
  cut8162 : Adequate {ℓ} ((op (op (op (op (var 0) (var 1)) (var 1)) (var 2)) (op (var 2) (var 3))) , (var 3)) → ⊥
  cut8162  adequate = bad8162  (Adequate.valid adequate Two boolean env5)
  bad8163 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b0) b0) b0) (bop b0 b0)) b1 → ⊥
  bad8163  p = false≢true (cong lower p)
  cut8163 : Adequate {ℓ} ((op (op (op (op (var 0) (var 1)) (var 1)) (var 2)) (op (var 2) (var 3))) , (var 4)) → ⊥
  cut8163  adequate = bad8163  (Adequate.valid adequate Two boolean env9)
  bad8164 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b0) b0) b1) (bop b0 b0)) b0 → ⊥
  bad8164  p = false≢true (sym (cong lower p))
  cut8164 : Adequate {ℓ} ((op (op (op (op (var 0) (var 1)) (var 1)) (var 2)) (op (var 3) (var 0))) , (var 0)) → ⊥
  cut8164  adequate = bad8164  (Adequate.valid adequate Two boolean env8)
  bad8165 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b0) b0) b1) (bop b0 b0)) b0 → ⊥
  bad8165  p = false≢true (sym (cong lower p))
  cut8165 : Adequate {ℓ} ((op (op (op (op (var 0) (var 1)) (var 1)) (var 2)) (op (var 3) (var 0))) , (var 1)) → ⊥
  cut8165  adequate = bad8165  (Adequate.valid adequate Two boolean env8)
  bad8166 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b1) b1) b1) (bop b0 b0)) b1 → ⊥
  bad8166  p = false≢true (cong lower p)
  cut8166 : Adequate {ℓ} ((op (op (op (op (var 0) (var 1)) (var 1)) (var 2)) (op (var 3) (var 0))) , (var 2)) → ⊥
  cut8166  adequate = bad8166  (Adequate.valid adequate Two boolean env12)
  bad8167 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b0) b0) b0) (bop b1 b0)) b1 → ⊥
  bad8167  p = false≢true (cong lower p)
  cut8167 : Adequate {ℓ} ((op (op (op (op (var 0) (var 1)) (var 1)) (var 2)) (op (var 3) (var 0))) , (var 3)) → ⊥
  cut8167  adequate = bad8167  (Adequate.valid adequate Two boolean env5)
  bad8168 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b0) b0) b0) (bop b0 b0)) b1 → ⊥
  bad8168  p = false≢true (cong lower p)
  cut8168 : Adequate {ℓ} ((op (op (op (op (var 0) (var 1)) (var 1)) (var 2)) (op (var 3) (var 0))) , (var 4)) → ⊥
  cut8168  adequate = bad8168  (Adequate.valid adequate Two boolean env9)
  bad8169 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b0) b0) b1) (bop b0 b0)) b0 → ⊥
  bad8169  p = false≢true (sym (cong lower p))
  cut8169 : Adequate {ℓ} ((op (op (op (op (var 0) (var 1)) (var 1)) (var 2)) (op (var 3) (var 1))) , (var 0)) → ⊥
  cut8169  adequate = bad8169  (Adequate.valid adequate Two boolean env8)
  bad8170 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b0) b0) b1) (bop b0 b0)) b0 → ⊥
  bad8170  p = false≢true (sym (cong lower p))
  cut8170 : Adequate {ℓ} ((op (op (op (op (var 0) (var 1)) (var 1)) (var 2)) (op (var 3) (var 1))) , (var 1)) → ⊥
  cut8170  adequate = bad8170  (Adequate.valid adequate Two boolean env8)
  bad8171 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b1) b1) b0) (bop b1 b1)) b0 → ⊥
  bad8171  p = false≢true (sym (cong lower p))
  cut8171 : Adequate {ℓ} ((op (op (op (op (var 0) (var 1)) (var 1)) (var 2)) (op (var 3) (var 1))) , (var 2)) → ⊥
  cut8171  adequate = bad8171  (Adequate.valid adequate Two boolean env13)
  bad8172 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b0) b0) b0) (bop b1 b0)) b1 → ⊥
  bad8172  p = false≢true (cong lower p)
  cut8172 : Adequate {ℓ} ((op (op (op (op (var 0) (var 1)) (var 1)) (var 2)) (op (var 3) (var 1))) , (var 3)) → ⊥
  cut8172  adequate = bad8172  (Adequate.valid adequate Two boolean env5)
  bad8173 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b0) b0) b0) (bop b0 b0)) b1 → ⊥
  bad8173  p = false≢true (cong lower p)
  cut8173 : Adequate {ℓ} ((op (op (op (op (var 0) (var 1)) (var 1)) (var 2)) (op (var 3) (var 1))) , (var 4)) → ⊥
  cut8173  adequate = bad8173  (Adequate.valid adequate Two boolean env9)
  bad8174 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b0) b0) b1) (bop b0 b1)) b0 → ⊥
  bad8174  p = false≢true (sym (cong lower p))
  cut8174 : Adequate {ℓ} ((op (op (op (op (var 0) (var 1)) (var 1)) (var 2)) (op (var 3) (var 2))) , (var 0)) → ⊥
  cut8174  adequate = bad8174  (Adequate.valid adequate Two boolean env8)
  bad8175 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b0) b0) b1) (bop b0 b1)) b0 → ⊥
  bad8175  p = false≢true (sym (cong lower p))
  cut8175 : Adequate {ℓ} ((op (op (op (op (var 0) (var 1)) (var 1)) (var 2)) (op (var 3) (var 2))) , (var 1)) → ⊥
  cut8175  adequate = bad8175  (Adequate.valid adequate Two boolean env8)
  bad8176 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b1) b1) b1) (bop b0 b1)) b1 → ⊥
  bad8176  p = false≢true (cong lower p)
  cut8176 : Adequate {ℓ} ((op (op (op (op (var 0) (var 1)) (var 1)) (var 2)) (op (var 3) (var 2))) , (var 2)) → ⊥
  cut8176  adequate = bad8176  (Adequate.valid adequate Two boolean env12)
  bad8177 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b0) b0) b0) (bop b1 b0)) b1 → ⊥
  bad8177  p = false≢true (cong lower p)
  cut8177 : Adequate {ℓ} ((op (op (op (op (var 0) (var 1)) (var 1)) (var 2)) (op (var 3) (var 2))) , (var 3)) → ⊥
  cut8177  adequate = bad8177  (Adequate.valid adequate Two boolean env5)
  bad8178 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b0) b0) b0) (bop b0 b0)) b1 → ⊥
  bad8178  p = false≢true (cong lower p)
  cut8178 : Adequate {ℓ} ((op (op (op (op (var 0) (var 1)) (var 1)) (var 2)) (op (var 3) (var 2))) , (var 4)) → ⊥
  cut8178  adequate = bad8178  (Adequate.valid adequate Two boolean env9)
  bad8179 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b0) b0) b0) (bop b1 b1)) b0 → ⊥
  bad8179  p = false≢true (sym (cong lower p))
  cut8179 : Adequate {ℓ} ((op (op (op (op (var 0) (var 1)) (var 1)) (var 2)) (op (var 3) (var 3))) , (var 0)) → ⊥
  cut8179  adequate = bad8179  (Adequate.valid adequate Two boolean env5)
  bad8180 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b0) b0) b0) (bop b1 b1)) b0 → ⊥
  bad8180  p = false≢true (sym (cong lower p))
  cut8180 : Adequate {ℓ} ((op (op (op (op (var 0) (var 1)) (var 1)) (var 2)) (op (var 3) (var 3))) , (var 1)) → ⊥
  cut8180  adequate = bad8180  (Adequate.valid adequate Two boolean env5)
  bad8181 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b0) b0) b0) (bop b1 b1)) b0 → ⊥
  bad8181  p = false≢true (sym (cong lower p))
  cut8181 : Adequate {ℓ} ((op (op (op (op (var 0) (var 1)) (var 1)) (var 2)) (op (var 3) (var 3))) , (var 2)) → ⊥
  cut8181  adequate = bad8181  (Adequate.valid adequate Two boolean env5)
  bad8182 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b0) b0) b1) (bop b0 b0)) b0 → ⊥
  bad8182  p = false≢true (sym (cong lower p))
  cut8182 : Adequate {ℓ} ((op (op (op (op (var 0) (var 1)) (var 1)) (var 2)) (op (var 3) (var 3))) , (var 3)) → ⊥
  cut8182  adequate = bad8182  (Adequate.valid adequate Two boolean env8)
  bad8183 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b0) b0) b0) (bop b0 b0)) b1 → ⊥
  bad8183  p = false≢true (cong lower p)
  cut8183 : Adequate {ℓ} ((op (op (op (op (var 0) (var 1)) (var 1)) (var 2)) (op (var 3) (var 3))) , (var 4)) → ⊥
  cut8183  adequate = bad8183  (Adequate.valid adequate Two boolean env9)
  bad8184 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b0) b0) b0) (bop b1 b1)) b0 → ⊥
  bad8184  p = false≢true (sym (cong lower p))
  cut8184 : Adequate {ℓ} ((op (op (op (op (var 0) (var 1)) (var 1)) (var 2)) (op (var 3) (var 4))) , (var 0)) → ⊥
  cut8184  adequate = bad8184  (Adequate.valid adequate Two boolean env14)
  bad8185 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b0) b0) b0) (bop b1 b1)) b0 → ⊥
  bad8185  p = false≢true (sym (cong lower p))
  cut8185 : Adequate {ℓ} ((op (op (op (op (var 0) (var 1)) (var 1)) (var 2)) (op (var 3) (var 4))) , (var 1)) → ⊥
  cut8185  adequate = bad8185  (Adequate.valid adequate Two boolean env14)
  bad8186 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b0) b0) b0) (bop b1 b1)) b0 → ⊥
  bad8186  p = false≢true (sym (cong lower p))
  cut8186 : Adequate {ℓ} ((op (op (op (op (var 0) (var 1)) (var 1)) (var 2)) (op (var 3) (var 4))) , (var 2)) → ⊥
  cut8186  adequate = bad8186  (Adequate.valid adequate Two boolean env14)
  bad8187 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b0) b0) b0) (bop b1 b0)) b1 → ⊥
  bad8187  p = false≢true (cong lower p)
  cut8187 : Adequate {ℓ} ((op (op (op (op (var 0) (var 1)) (var 1)) (var 2)) (op (var 3) (var 4))) , (var 3)) → ⊥
  cut8187  adequate = bad8187  (Adequate.valid adequate Two boolean env15)
  bad8188 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b0) b0) b0) (bop b0 b1)) b1 → ⊥
  bad8188  p = false≢true (cong lower p)
  cut8188 : Adequate {ℓ} ((op (op (op (op (var 0) (var 1)) (var 1)) (var 2)) (op (var 3) (var 4))) , (var 4)) → ⊥
  cut8188  adequate = bad8188  (Adequate.valid adequate Two boolean env9)
  bad8189 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b0) b0) b0) (bop b0 b0)) b1 → ⊥
  bad8189  p = false≢true (cong lower p)
  cut8189 : Adequate {ℓ} ((op (op (op (op (var 0) (var 1)) (var 1)) (var 2)) (op (var 3) (var 4))) , (var 5)) → ⊥
  cut8189  adequate = bad8189  (Adequate.valid adequate Two boolean env16)
  holds8190 : (z0 z1 z2 : A2) → (mul2 (mul2 (mul2 (mul2 z0 z1) z2) z0) (mul2 z0 z0)) ≡ z0
  holds8190 z0 z1 z2 = refl
  cut8190 : Adequate {ℓ} ((op (op (op (op (var 0) (var 1)) (var 2)) (var 0)) (op (var 0) (var 0))) , (var 0)) → ⊥
  cut8190  = reject2 ((op (op (op (op (var 0) (var 1)) (var 2)) (var 0)) (op (var 0) (var 0))) , (var 0)) (λ env → holds8190 (env 0) (env 1) (env 2))
  bad8191 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b1) b0) b0) (bop b0 b0)) b1 → ⊥
  bad8191  p = false≢true (cong lower p)
  cut8191 : Adequate {ℓ} ((op (op (op (op (var 0) (var 1)) (var 2)) (var 0)) (op (var 0) (var 0))) , (var 1)) → ⊥
  cut8191  adequate = bad8191  (Adequate.valid adequate Two boolean env4)
  bad8192 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b0) b1) b0) (bop b0 b0)) b1 → ⊥
  bad8192  p = false≢true (cong lower p)
  cut8192 : Adequate {ℓ} ((op (op (op (op (var 0) (var 1)) (var 2)) (var 0)) (op (var 0) (var 0))) , (var 2)) → ⊥
  cut8192  adequate = bad8192  (Adequate.valid adequate Two boolean env1)
  bad8193 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b0) b0) b0) (bop b0 b0)) b1 → ⊥
  bad8193  p = false≢true (cong lower p)
  cut8193 : Adequate {ℓ} ((op (op (op (op (var 0) (var 1)) (var 2)) (var 0)) (op (var 0) (var 0))) , (var 3)) → ⊥
  cut8193  adequate = bad8193  (Adequate.valid adequate Two boolean env5)
  bad8194 : PathP (λ _ → Two) (bop (bop (bop (bop b1 b0) b1) b1) (bop b1 b0)) b1 → ⊥
  bad8194  p = false≢true (cong lower p)
  cut8194 : Adequate {ℓ} ((op (op (op (op (var 0) (var 1)) (var 2)) (var 0)) (op (var 0) (var 1))) , (var 0)) → ⊥
  cut8194  adequate = bad8194  (Adequate.valid adequate Two boolean env6)
  bad8195 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b1) b0) b0) (bop b0 b1)) b1 → ⊥
  bad8195  p = false≢true (cong lower p)
  cut8195 : Adequate {ℓ} ((op (op (op (op (var 0) (var 1)) (var 2)) (var 0)) (op (var 0) (var 1))) , (var 1)) → ⊥
  cut8195  adequate = bad8195  (Adequate.valid adequate Two boolean env4)
  bad8196 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b0) b1) b0) (bop b0 b0)) b1 → ⊥
  bad8196  p = false≢true (cong lower p)
  cut8196 : Adequate {ℓ} ((op (op (op (op (var 0) (var 1)) (var 2)) (var 0)) (op (var 0) (var 1))) , (var 2)) → ⊥
  cut8196  adequate = bad8196  (Adequate.valid adequate Two boolean env1)
  bad8197 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b0) b0) b0) (bop b0 b0)) b1 → ⊥
  bad8197  p = false≢true (cong lower p)
  cut8197 : Adequate {ℓ} ((op (op (op (op (var 0) (var 1)) (var 2)) (var 0)) (op (var 0) (var 1))) , (var 3)) → ⊥
  cut8197  adequate = bad8197  (Adequate.valid adequate Two boolean env5)
  holds8198 : (z0 z1 z2 : A2) → (mul2 (mul2 (mul2 (mul2 z0 z1) z2) z0) (mul2 z0 z2)) ≡ z0
  holds8198 z0 z1 z2 = refl
  cut8198 : Adequate {ℓ} ((op (op (op (op (var 0) (var 1)) (var 2)) (var 0)) (op (var 0) (var 2))) , (var 0)) → ⊥
  cut8198  = reject2 ((op (op (op (op (var 0) (var 1)) (var 2)) (var 0)) (op (var 0) (var 2))) , (var 0)) (λ env → holds8198 (env 0) (env 1) (env 2))
  bad8199 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b1) b0) b0) (bop b0 b0)) b1 → ⊥
  bad8199  p = false≢true (cong lower p)
  cut8199 : Adequate {ℓ} ((op (op (op (op (var 0) (var 1)) (var 2)) (var 0)) (op (var 0) (var 2))) , (var 1)) → ⊥
  cut8199  adequate = bad8199  (Adequate.valid adequate Two boolean env4)
  bad8200 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b0) b1) b0) (bop b0 b1)) b1 → ⊥
  bad8200  p = false≢true (cong lower p)
  cut8200 : Adequate {ℓ} ((op (op (op (op (var 0) (var 1)) (var 2)) (var 0)) (op (var 0) (var 2))) , (var 2)) → ⊥
  cut8200  adequate = bad8200  (Adequate.valid adequate Two boolean env1)
  bad8201 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b0) b0) b0) (bop b0 b0)) b1 → ⊥
  bad8201  p = false≢true (cong lower p)
  cut8201 : Adequate {ℓ} ((op (op (op (op (var 0) (var 1)) (var 2)) (var 0)) (op (var 0) (var 2))) , (var 3)) → ⊥
  cut8201  adequate = bad8201  (Adequate.valid adequate Two boolean env5)
  bad8202 : PathP (λ _ → Two) (bop (bop (bop (bop b1 b0) b1) b1) (bop b1 b0)) b1 → ⊥
  bad8202  p = false≢true (cong lower p)
  cut8202 : Adequate {ℓ} ((op (op (op (op (var 0) (var 1)) (var 2)) (var 0)) (op (var 0) (var 3))) , (var 0)) → ⊥
  cut8202  adequate = bad8202  (Adequate.valid adequate Two boolean env18)
  env19 : ℕ → Two
  env19 zero = b0
  env19 (suc zero) = b1
  env19 (suc (suc zero)) = b0
  env19 (suc (suc (suc zero))) = b0
  env19 (suc (suc (suc (suc rest)))) = b0
  bad8203 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b1) b0) b0) (bop b0 b0)) b1 → ⊥
  bad8203  p = false≢true (cong lower p)
  cut8203 : Adequate {ℓ} ((op (op (op (op (var 0) (var 1)) (var 2)) (var 0)) (op (var 0) (var 3))) , (var 1)) → ⊥
  cut8203  adequate = bad8203  (Adequate.valid adequate Two boolean env19)
  bad8204 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b0) b1) b0) (bop b0 b0)) b1 → ⊥
  bad8204  p = false≢true (cong lower p)
  cut8204 : Adequate {ℓ} ((op (op (op (op (var 0) (var 1)) (var 2)) (var 0)) (op (var 0) (var 3))) , (var 2)) → ⊥
  cut8204  adequate = bad8204  (Adequate.valid adequate Two boolean env8)
  bad8205 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b0) b0) b0) (bop b0 b1)) b1 → ⊥
  bad8205  p = false≢true (cong lower p)
  cut8205 : Adequate {ℓ} ((op (op (op (op (var 0) (var 1)) (var 2)) (var 0)) (op (var 0) (var 3))) , (var 3)) → ⊥
  cut8205  adequate = bad8205  (Adequate.valid adequate Two boolean env5)
  bad8206 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b0) b0) b0) (bop b0 b0)) b1 → ⊥
  bad8206  p = false≢true (cong lower p)
  cut8206 : Adequate {ℓ} ((op (op (op (op (var 0) (var 1)) (var 2)) (var 0)) (op (var 0) (var 3))) , (var 4)) → ⊥
  cut8206  adequate = bad8206  (Adequate.valid adequate Two boolean env9)
  bad8207 : PathP (λ _ → Two) (bop (bop (bop (bop b1 b0) b1) b1) (bop b0 b1)) b1 → ⊥
  bad8207  p = false≢true (cong lower p)
  cut8207 : Adequate {ℓ} ((op (op (op (op (var 0) (var 1)) (var 2)) (var 0)) (op (var 1) (var 0))) , (var 0)) → ⊥
  cut8207  adequate = bad8207  (Adequate.valid adequate Two boolean env6)
  bad8208 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b1) b0) b0) (bop b1 b0)) b1 → ⊥
  bad8208  p = false≢true (cong lower p)
  cut8208 : Adequate {ℓ} ((op (op (op (op (var 0) (var 1)) (var 2)) (var 0)) (op (var 1) (var 0))) , (var 1)) → ⊥
  cut8208  adequate = bad8208  (Adequate.valid adequate Two boolean env4)
  bad8209 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b0) b1) b0) (bop b0 b0)) b1 → ⊥
  bad8209  p = false≢true (cong lower p)
  cut8209 : Adequate {ℓ} ((op (op (op (op (var 0) (var 1)) (var 2)) (var 0)) (op (var 1) (var 0))) , (var 2)) → ⊥
  cut8209  adequate = bad8209  (Adequate.valid adequate Two boolean env1)
  bad8210 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b0) b0) b0) (bop b0 b0)) b1 → ⊥
  bad8210  p = false≢true (cong lower p)
  cut8210 : Adequate {ℓ} ((op (op (op (op (var 0) (var 1)) (var 2)) (var 0)) (op (var 1) (var 0))) , (var 3)) → ⊥
  cut8210  adequate = bad8210  (Adequate.valid adequate Two boolean env5)
  bad8211 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b1) b0) b0) (bop b1 b1)) b0 → ⊥
  bad8211  p = false≢true (sym (cong lower p))
  cut8211 : Adequate {ℓ} ((op (op (op (op (var 0) (var 1)) (var 2)) (var 0)) (op (var 1) (var 1))) , (var 0)) → ⊥
  cut8211  adequate = bad8211  (Adequate.valid adequate Two boolean env4)
  bad8212 : PathP (λ _ → Two) (bop (bop (bop (bop b1 b0) b0) b1) (bop b0 b0)) b0 → ⊥
  bad8212  p = false≢true (sym (cong lower p))
  cut8212 : Adequate {ℓ} ((op (op (op (op (var 0) (var 1)) (var 2)) (var 0)) (op (var 1) (var 1))) , (var 1)) → ⊥
  cut8212  adequate = bad8212  (Adequate.valid adequate Two boolean env10)
  bad8213 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b0) b1) b0) (bop b0 b0)) b1 → ⊥
  bad8213  p = false≢true (cong lower p)
  cut8213 : Adequate {ℓ} ((op (op (op (op (var 0) (var 1)) (var 2)) (var 0)) (op (var 1) (var 1))) , (var 2)) → ⊥
  cut8213  adequate = bad8213  (Adequate.valid adequate Two boolean env1)
  bad8214 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b0) b0) b0) (bop b0 b0)) b1 → ⊥
  bad8214  p = false≢true (cong lower p)
  cut8214 : Adequate {ℓ} ((op (op (op (op (var 0) (var 1)) (var 2)) (var 0)) (op (var 1) (var 1))) , (var 3)) → ⊥
  cut8214  adequate = bad8214  (Adequate.valid adequate Two boolean env5)
  bad8215 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b1) b1) b0) (bop b1 b1)) b0 → ⊥
  bad8215  p = false≢true (sym (cong lower p))
  cut8215 : Adequate {ℓ} ((op (op (op (op (var 0) (var 1)) (var 2)) (var 0)) (op (var 1) (var 2))) , (var 0)) → ⊥
  cut8215  adequate = bad8215  (Adequate.valid adequate Two boolean env3)
  bad8216 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b1) b0) b0) (bop b1 b0)) b1 → ⊥
  bad8216  p = false≢true (cong lower p)
  cut8216 : Adequate {ℓ} ((op (op (op (op (var 0) (var 1)) (var 2)) (var 0)) (op (var 1) (var 2))) , (var 1)) → ⊥
  cut8216  adequate = bad8216  (Adequate.valid adequate Two boolean env4)
  bad8217 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b0) b1) b0) (bop b0 b1)) b1 → ⊥
  bad8217  p = false≢true (cong lower p)
  cut8217 : Adequate {ℓ} ((op (op (op (op (var 0) (var 1)) (var 2)) (var 0)) (op (var 1) (var 2))) , (var 2)) → ⊥
  cut8217  adequate = bad8217  (Adequate.valid adequate Two boolean env1)
  bad8218 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b0) b0) b0) (bop b0 b0)) b1 → ⊥
  bad8218  p = false≢true (cong lower p)
  cut8218 : Adequate {ℓ} ((op (op (op (op (var 0) (var 1)) (var 2)) (var 0)) (op (var 1) (var 2))) , (var 3)) → ⊥
  cut8218  adequate = bad8218  (Adequate.valid adequate Two boolean env5)
  bad8219 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b1) b0) b0) (bop b1 b1)) b0 → ⊥
  bad8219  p = false≢true (sym (cong lower p))
  cut8219 : Adequate {ℓ} ((op (op (op (op (var 0) (var 1)) (var 2)) (var 0)) (op (var 1) (var 3))) , (var 0)) → ⊥
  cut8219  adequate = bad8219  (Adequate.valid adequate Two boolean env13)
  bad8220 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b1) b0) b0) (bop b1 b0)) b1 → ⊥
  bad8220  p = false≢true (cong lower p)
  cut8220 : Adequate {ℓ} ((op (op (op (op (var 0) (var 1)) (var 2)) (var 0)) (op (var 1) (var 3))) , (var 1)) → ⊥
  cut8220  adequate = bad8220  (Adequate.valid adequate Two boolean env19)
  bad8221 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b0) b1) b0) (bop b0 b0)) b1 → ⊥
  bad8221  p = false≢true (cong lower p)
  cut8221 : Adequate {ℓ} ((op (op (op (op (var 0) (var 1)) (var 2)) (var 0)) (op (var 1) (var 3))) , (var 2)) → ⊥
  cut8221  adequate = bad8221  (Adequate.valid adequate Two boolean env8)
  bad8222 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b0) b0) b0) (bop b0 b1)) b1 → ⊥
  bad8222  p = false≢true (cong lower p)
  cut8222 : Adequate {ℓ} ((op (op (op (op (var 0) (var 1)) (var 2)) (var 0)) (op (var 1) (var 3))) , (var 3)) → ⊥
  cut8222  adequate = bad8222  (Adequate.valid adequate Two boolean env5)
  bad8223 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b0) b0) b0) (bop b0 b0)) b1 → ⊥
  bad8223  p = false≢true (cong lower p)
  cut8223 : Adequate {ℓ} ((op (op (op (op (var 0) (var 1)) (var 2)) (var 0)) (op (var 1) (var 3))) , (var 4)) → ⊥
  cut8223  adequate = bad8223  (Adequate.valid adequate Two boolean env9)
  holds8224 : (z0 z1 z2 : A2) → (mul2 (mul2 (mul2 (mul2 z0 z1) z2) z0) (mul2 z2 z0)) ≡ z0
  holds8224 z0 z1 z2 = refl
  cut8224 : Adequate {ℓ} ((op (op (op (op (var 0) (var 1)) (var 2)) (var 0)) (op (var 2) (var 0))) , (var 0)) → ⊥
  cut8224  = reject2 ((op (op (op (op (var 0) (var 1)) (var 2)) (var 0)) (op (var 2) (var 0))) , (var 0)) (λ env → holds8224 (env 0) (env 1) (env 2))
  bad8225 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b1) b0) b0) (bop b0 b0)) b1 → ⊥
  bad8225  p = false≢true (cong lower p)
  cut8225 : Adequate {ℓ} ((op (op (op (op (var 0) (var 1)) (var 2)) (var 0)) (op (var 2) (var 0))) , (var 1)) → ⊥
  cut8225  adequate = bad8225  (Adequate.valid adequate Two boolean env4)
  bad8226 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b0) b1) b0) (bop b1 b0)) b1 → ⊥
  bad8226  p = false≢true (cong lower p)
  cut8226 : Adequate {ℓ} ((op (op (op (op (var 0) (var 1)) (var 2)) (var 0)) (op (var 2) (var 0))) , (var 2)) → ⊥
  cut8226  adequate = bad8226  (Adequate.valid adequate Two boolean env1)
  bad8227 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b0) b0) b0) (bop b0 b0)) b1 → ⊥
  bad8227  p = false≢true (cong lower p)
  cut8227 : Adequate {ℓ} ((op (op (op (op (var 0) (var 1)) (var 2)) (var 0)) (op (var 2) (var 0))) , (var 3)) → ⊥
  cut8227  adequate = bad8227  (Adequate.valid adequate Two boolean env5)
  bad8228 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b1) b1) b0) (bop b1 b1)) b0 → ⊥
  bad8228  p = false≢true (sym (cong lower p))
  cut8228 : Adequate {ℓ} ((op (op (op (op (var 0) (var 1)) (var 2)) (var 0)) (op (var 2) (var 1))) , (var 0)) → ⊥
  cut8228  adequate = bad8228  (Adequate.valid adequate Two boolean env3)
  bad8229 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b1) b0) b0) (bop b0 b1)) b1 → ⊥
  bad8229  p = false≢true (cong lower p)
  cut8229 : Adequate {ℓ} ((op (op (op (op (var 0) (var 1)) (var 2)) (var 0)) (op (var 2) (var 1))) , (var 1)) → ⊥
  cut8229  adequate = bad8229  (Adequate.valid adequate Two boolean env4)
  bad8230 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b0) b1) b0) (bop b1 b0)) b1 → ⊥
  bad8230  p = false≢true (cong lower p)
  cut8230 : Adequate {ℓ} ((op (op (op (op (var 0) (var 1)) (var 2)) (var 0)) (op (var 2) (var 1))) , (var 2)) → ⊥
  cut8230  adequate = bad8230  (Adequate.valid adequate Two boolean env1)
  bad8231 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b0) b0) b0) (bop b0 b0)) b1 → ⊥
  bad8231  p = false≢true (cong lower p)
  cut8231 : Adequate {ℓ} ((op (op (op (op (var 0) (var 1)) (var 2)) (var 0)) (op (var 2) (var 1))) , (var 3)) → ⊥
  cut8231  adequate = bad8231  (Adequate.valid adequate Two boolean env5)
  bad8232 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b0) b1) b0) (bop b1 b1)) b0 → ⊥
  bad8232  p = false≢true (sym (cong lower p))
  cut8232 : Adequate {ℓ} ((op (op (op (op (var 0) (var 1)) (var 2)) (var 0)) (op (var 2) (var 2))) , (var 0)) → ⊥
  cut8232  adequate = bad8232  (Adequate.valid adequate Two boolean env1)
  bad8233 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b0) b1) b0) (bop b1 b1)) b0 → ⊥
  bad8233  p = false≢true (sym (cong lower p))
  cut8233 : Adequate {ℓ} ((op (op (op (op (var 0) (var 1)) (var 2)) (var 0)) (op (var 2) (var 2))) , (var 1)) → ⊥
  cut8233  adequate = bad8233  (Adequate.valid adequate Two boolean env1)
  bad8234 : PathP (λ _ → Two) (bop (bop (bop (bop b1 b0) b0) b1) (bop b0 b0)) b0 → ⊥
  bad8234  p = false≢true (sym (cong lower p))
  cut8234 : Adequate {ℓ} ((op (op (op (op (var 0) (var 1)) (var 2)) (var 0)) (op (var 2) (var 2))) , (var 2)) → ⊥
  cut8234  adequate = bad8234  (Adequate.valid adequate Two boolean env10)
  bad8235 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b0) b0) b0) (bop b0 b0)) b1 → ⊥
  bad8235  p = false≢true (cong lower p)
  cut8235 : Adequate {ℓ} ((op (op (op (op (var 0) (var 1)) (var 2)) (var 0)) (op (var 2) (var 2))) , (var 3)) → ⊥
  cut8235  adequate = bad8235  (Adequate.valid adequate Two boolean env5)
  bad8236 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b0) b1) b0) (bop b1 b1)) b0 → ⊥
  bad8236  p = false≢true (sym (cong lower p))
  cut8236 : Adequate {ℓ} ((op (op (op (op (var 0) (var 1)) (var 2)) (var 0)) (op (var 2) (var 3))) , (var 0)) → ⊥
  cut8236  adequate = bad8236  (Adequate.valid adequate Two boolean env7)
  bad8237 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b0) b1) b0) (bop b1 b1)) b0 → ⊥
  bad8237  p = false≢true (sym (cong lower p))
  cut8237 : Adequate {ℓ} ((op (op (op (op (var 0) (var 1)) (var 2)) (var 0)) (op (var 2) (var 3))) , (var 1)) → ⊥
  cut8237  adequate = bad8237  (Adequate.valid adequate Two boolean env7)
  bad8238 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b0) b1) b0) (bop b1 b0)) b1 → ⊥
  bad8238  p = false≢true (cong lower p)
  cut8238 : Adequate {ℓ} ((op (op (op (op (var 0) (var 1)) (var 2)) (var 0)) (op (var 2) (var 3))) , (var 2)) → ⊥
  cut8238  adequate = bad8238  (Adequate.valid adequate Two boolean env8)
  bad8239 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b0) b0) b0) (bop b0 b1)) b1 → ⊥
  bad8239  p = false≢true (cong lower p)
  cut8239 : Adequate {ℓ} ((op (op (op (op (var 0) (var 1)) (var 2)) (var 0)) (op (var 2) (var 3))) , (var 3)) → ⊥
  cut8239  adequate = bad8239  (Adequate.valid adequate Two boolean env5)
  bad8240 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b0) b0) b0) (bop b0 b0)) b1 → ⊥
  bad8240  p = false≢true (cong lower p)
  cut8240 : Adequate {ℓ} ((op (op (op (op (var 0) (var 1)) (var 2)) (var 0)) (op (var 2) (var 3))) , (var 4)) → ⊥
  cut8240  adequate = bad8240  (Adequate.valid adequate Two boolean env9)
  bad8241 : PathP (λ _ → Two) (bop (bop (bop (bop b1 b0) b1) b1) (bop b0 b1)) b1 → ⊥
  bad8241  p = false≢true (cong lower p)
  cut8241 : Adequate {ℓ} ((op (op (op (op (var 0) (var 1)) (var 2)) (var 0)) (op (var 3) (var 0))) , (var 0)) → ⊥
  cut8241  adequate = bad8241  (Adequate.valid adequate Two boolean env18)
  bad8242 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b1) b0) b0) (bop b0 b0)) b1 → ⊥
  bad8242  p = false≢true (cong lower p)
  cut8242 : Adequate {ℓ} ((op (op (op (op (var 0) (var 1)) (var 2)) (var 0)) (op (var 3) (var 0))) , (var 1)) → ⊥
  cut8242  adequate = bad8242  (Adequate.valid adequate Two boolean env19)
  bad8243 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b0) b1) b0) (bop b0 b0)) b1 → ⊥
  bad8243  p = false≢true (cong lower p)
  cut8243 : Adequate {ℓ} ((op (op (op (op (var 0) (var 1)) (var 2)) (var 0)) (op (var 3) (var 0))) , (var 2)) → ⊥
  cut8243  adequate = bad8243  (Adequate.valid adequate Two boolean env8)
  bad8244 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b0) b0) b0) (bop b1 b0)) b1 → ⊥
  bad8244  p = false≢true (cong lower p)
  cut8244 : Adequate {ℓ} ((op (op (op (op (var 0) (var 1)) (var 2)) (var 0)) (op (var 3) (var 0))) , (var 3)) → ⊥
  cut8244  adequate = bad8244  (Adequate.valid adequate Two boolean env5)
  bad8245 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b0) b0) b0) (bop b0 b0)) b1 → ⊥
  bad8245  p = false≢true (cong lower p)
  cut8245 : Adequate {ℓ} ((op (op (op (op (var 0) (var 1)) (var 2)) (var 0)) (op (var 3) (var 0))) , (var 4)) → ⊥
  cut8245  adequate = bad8245  (Adequate.valid adequate Two boolean env9)
  bad8246 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b1) b0) b0) (bop b1 b1)) b0 → ⊥
  bad8246  p = false≢true (sym (cong lower p))
  cut8246 : Adequate {ℓ} ((op (op (op (op (var 0) (var 1)) (var 2)) (var 0)) (op (var 3) (var 1))) , (var 0)) → ⊥
  cut8246  adequate = bad8246  (Adequate.valid adequate Two boolean env13)
  bad8247 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b1) b0) b0) (bop b0 b1)) b1 → ⊥
  bad8247  p = false≢true (cong lower p)
  cut8247 : Adequate {ℓ} ((op (op (op (op (var 0) (var 1)) (var 2)) (var 0)) (op (var 3) (var 1))) , (var 1)) → ⊥
  cut8247  adequate = bad8247  (Adequate.valid adequate Two boolean env19)
  bad8248 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b0) b1) b0) (bop b0 b0)) b1 → ⊥
  bad8248  p = false≢true (cong lower p)
  cut8248 : Adequate {ℓ} ((op (op (op (op (var 0) (var 1)) (var 2)) (var 0)) (op (var 3) (var 1))) , (var 2)) → ⊥
  cut8248  adequate = bad8248  (Adequate.valid adequate Two boolean env8)
  bad8249 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b0) b0) b0) (bop b1 b0)) b1 → ⊥
  bad8249  p = false≢true (cong lower p)
  cut8249 : Adequate {ℓ} ((op (op (op (op (var 0) (var 1)) (var 2)) (var 0)) (op (var 3) (var 1))) , (var 3)) → ⊥
  cut8249  adequate = bad8249  (Adequate.valid adequate Two boolean env5)
  bad8250 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b0) b0) b0) (bop b0 b0)) b1 → ⊥
  bad8250  p = false≢true (cong lower p)
  cut8250 : Adequate {ℓ} ((op (op (op (op (var 0) (var 1)) (var 2)) (var 0)) (op (var 3) (var 1))) , (var 4)) → ⊥
  cut8250  adequate = bad8250  (Adequate.valid adequate Two boolean env9)
  bad8251 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b0) b1) b0) (bop b1 b1)) b0 → ⊥
  bad8251  p = false≢true (sym (cong lower p))
  cut8251 : Adequate {ℓ} ((op (op (op (op (var 0) (var 1)) (var 2)) (var 0)) (op (var 3) (var 2))) , (var 0)) → ⊥
  cut8251  adequate = bad8251  (Adequate.valid adequate Two boolean env7)
  bad8252 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b0) b1) b0) (bop b1 b1)) b0 → ⊥
  bad8252  p = false≢true (sym (cong lower p))
  cut8252 : Adequate {ℓ} ((op (op (op (op (var 0) (var 1)) (var 2)) (var 0)) (op (var 3) (var 2))) , (var 1)) → ⊥
  cut8252  adequate = bad8252  (Adequate.valid adequate Two boolean env7)
  bad8253 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b0) b1) b0) (bop b0 b1)) b1 → ⊥
  bad8253  p = false≢true (cong lower p)
  cut8253 : Adequate {ℓ} ((op (op (op (op (var 0) (var 1)) (var 2)) (var 0)) (op (var 3) (var 2))) , (var 2)) → ⊥
  cut8253  adequate = bad8253  (Adequate.valid adequate Two boolean env8)
  bad8254 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b0) b0) b0) (bop b1 b0)) b1 → ⊥
  bad8254  p = false≢true (cong lower p)
  cut8254 : Adequate {ℓ} ((op (op (op (op (var 0) (var 1)) (var 2)) (var 0)) (op (var 3) (var 2))) , (var 3)) → ⊥
  cut8254  adequate = bad8254  (Adequate.valid adequate Two boolean env5)
  bad8255 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b0) b0) b0) (bop b0 b0)) b1 → ⊥
  bad8255  p = false≢true (cong lower p)
  cut8255 : Adequate {ℓ} ((op (op (op (op (var 0) (var 1)) (var 2)) (var 0)) (op (var 3) (var 2))) , (var 4)) → ⊥
  cut8255  adequate = bad8255  (Adequate.valid adequate Two boolean env9)
  bad8256 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b0) b0) b0) (bop b1 b1)) b0 → ⊥
  bad8256  p = false≢true (sym (cong lower p))
  cut8256 : Adequate {ℓ} ((op (op (op (op (var 0) (var 1)) (var 2)) (var 0)) (op (var 3) (var 3))) , (var 0)) → ⊥
  cut8256  adequate = bad8256  (Adequate.valid adequate Two boolean env5)
  bad8257 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b0) b0) b0) (bop b1 b1)) b0 → ⊥
  bad8257  p = false≢true (sym (cong lower p))
  cut8257 : Adequate {ℓ} ((op (op (op (op (var 0) (var 1)) (var 2)) (var 0)) (op (var 3) (var 3))) , (var 1)) → ⊥
  cut8257  adequate = bad8257  (Adequate.valid adequate Two boolean env5)
  bad8258 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b0) b0) b0) (bop b1 b1)) b0 → ⊥
  bad8258  p = false≢true (sym (cong lower p))
  cut8258 : Adequate {ℓ} ((op (op (op (op (var 0) (var 1)) (var 2)) (var 0)) (op (var 3) (var 3))) , (var 2)) → ⊥
  cut8258  adequate = bad8258  (Adequate.valid adequate Two boolean env5)
  env20 : ℕ → Two
  env20 zero = b1
  env20 (suc zero) = b0
  env20 (suc (suc zero)) = b0
  env20 (suc (suc (suc zero))) = b0
  env20 (suc (suc (suc (suc rest)))) = b0
  bad8259 : PathP (λ _ → Two) (bop (bop (bop (bop b1 b0) b0) b1) (bop b0 b0)) b0 → ⊥
  bad8259  p = false≢true (sym (cong lower p))
  cut8259 : Adequate {ℓ} ((op (op (op (op (var 0) (var 1)) (var 2)) (var 0)) (op (var 3) (var 3))) , (var 3)) → ⊥
  cut8259  adequate = bad8259  (Adequate.valid adequate Two boolean env20)
  bad8260 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b0) b0) b0) (bop b0 b0)) b1 → ⊥
  bad8260  p = false≢true (cong lower p)
  cut8260 : Adequate {ℓ} ((op (op (op (op (var 0) (var 1)) (var 2)) (var 0)) (op (var 3) (var 3))) , (var 4)) → ⊥
  cut8260  adequate = bad8260  (Adequate.valid adequate Two boolean env9)
  bad8261 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b0) b0) b0) (bop b1 b1)) b0 → ⊥
  bad8261  p = false≢true (sym (cong lower p))
  cut8261 : Adequate {ℓ} ((op (op (op (op (var 0) (var 1)) (var 2)) (var 0)) (op (var 3) (var 4))) , (var 0)) → ⊥
  cut8261  adequate = bad8261  (Adequate.valid adequate Two boolean env14)
  bad8262 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b0) b0) b0) (bop b1 b1)) b0 → ⊥
  bad8262  p = false≢true (sym (cong lower p))
  cut8262 : Adequate {ℓ} ((op (op (op (op (var 0) (var 1)) (var 2)) (var 0)) (op (var 3) (var 4))) , (var 1)) → ⊥
  cut8262  adequate = bad8262  (Adequate.valid adequate Two boolean env14)
  bad8263 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b0) b0) b0) (bop b1 b1)) b0 → ⊥
  bad8263  p = false≢true (sym (cong lower p))
  cut8263 : Adequate {ℓ} ((op (op (op (op (var 0) (var 1)) (var 2)) (var 0)) (op (var 3) (var 4))) , (var 2)) → ⊥
  cut8263  adequate = bad8263  (Adequate.valid adequate Two boolean env14)
  bad8264 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b0) b0) b0) (bop b1 b0)) b1 → ⊥
  bad8264  p = false≢true (cong lower p)
  cut8264 : Adequate {ℓ} ((op (op (op (op (var 0) (var 1)) (var 2)) (var 0)) (op (var 3) (var 4))) , (var 3)) → ⊥
  cut8264  adequate = bad8264  (Adequate.valid adequate Two boolean env15)
  bad8265 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b0) b0) b0) (bop b0 b1)) b1 → ⊥
  bad8265  p = false≢true (cong lower p)
  cut8265 : Adequate {ℓ} ((op (op (op (op (var 0) (var 1)) (var 2)) (var 0)) (op (var 3) (var 4))) , (var 4)) → ⊥
  cut8265  adequate = bad8265  (Adequate.valid adequate Two boolean env9)
  bad8266 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b0) b0) b0) (bop b0 b0)) b1 → ⊥
  bad8266  p = false≢true (cong lower p)
  cut8266 : Adequate {ℓ} ((op (op (op (op (var 0) (var 1)) (var 2)) (var 0)) (op (var 3) (var 4))) , (var 5)) → ⊥
  cut8266  adequate = bad8266  (Adequate.valid adequate Two boolean env16)
  bad8267 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b1) b0) b1) (bop b0 b0)) b0 → ⊥
  bad8267  p = false≢true (sym (cong lower p))
  cut8267 : Adequate {ℓ} ((op (op (op (op (var 0) (var 1)) (var 2)) (var 1)) (op (var 0) (var 0))) , (var 0)) → ⊥
  cut8267  adequate = bad8267  (Adequate.valid adequate Two boolean env4)
  bad8268 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b1) b1) b1) (bop b0 b0)) b1 → ⊥
  bad8268  p = false≢true (cong lower p)
  cut8268 : Adequate {ℓ} ((op (op (op (op (var 0) (var 1)) (var 2)) (var 1)) (op (var 0) (var 0))) , (var 1)) → ⊥
  cut8268  adequate = bad8268  (Adequate.valid adequate Two boolean env3)
  bad8269 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b0) b1) b0) (bop b0 b0)) b1 → ⊥
  bad8269  p = false≢true (cong lower p)
  cut8269 : Adequate {ℓ} ((op (op (op (op (var 0) (var 1)) (var 2)) (var 1)) (op (var 0) (var 0))) , (var 2)) → ⊥
  cut8269  adequate = bad8269  (Adequate.valid adequate Two boolean env1)
  bad8270 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b0) b0) b0) (bop b0 b0)) b1 → ⊥
  bad8270  p = false≢true (cong lower p)
  cut8270 : Adequate {ℓ} ((op (op (op (op (var 0) (var 1)) (var 2)) (var 1)) (op (var 0) (var 0))) , (var 3)) → ⊥
  cut8270  adequate = bad8270  (Adequate.valid adequate Two boolean env5)
  bad8271 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b1) b0) b1) (bop b0 b1)) b0 → ⊥
  bad8271  p = false≢true (sym (cong lower p))
  cut8271 : Adequate {ℓ} ((op (op (op (op (var 0) (var 1)) (var 2)) (var 1)) (op (var 0) (var 1))) , (var 0)) → ⊥
  cut8271  adequate = bad8271  (Adequate.valid adequate Two boolean env4)
  bad8272 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b1) b1) b1) (bop b0 b1)) b1 → ⊥
  bad8272  p = false≢true (cong lower p)
  cut8272 : Adequate {ℓ} ((op (op (op (op (var 0) (var 1)) (var 2)) (var 1)) (op (var 0) (var 1))) , (var 1)) → ⊥
  cut8272  adequate = bad8272  (Adequate.valid adequate Two boolean env3)
  bad8273 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b0) b1) b0) (bop b0 b0)) b1 → ⊥
  bad8273  p = false≢true (cong lower p)
  cut8273 : Adequate {ℓ} ((op (op (op (op (var 0) (var 1)) (var 2)) (var 1)) (op (var 0) (var 1))) , (var 2)) → ⊥
  cut8273  adequate = bad8273  (Adequate.valid adequate Two boolean env1)
  bad8274 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b0) b0) b0) (bop b0 b0)) b1 → ⊥
  bad8274  p = false≢true (cong lower p)
  cut8274 : Adequate {ℓ} ((op (op (op (op (var 0) (var 1)) (var 2)) (var 1)) (op (var 0) (var 1))) , (var 3)) → ⊥
  cut8274  adequate = bad8274  (Adequate.valid adequate Two boolean env5)
  bad8275 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b1) b0) b1) (bop b0 b0)) b0 → ⊥
  bad8275  p = false≢true (sym (cong lower p))
  cut8275 : Adequate {ℓ} ((op (op (op (op (var 0) (var 1)) (var 2)) (var 1)) (op (var 0) (var 2))) , (var 0)) → ⊥
  cut8275  adequate = bad8275  (Adequate.valid adequate Two boolean env4)
  bad8276 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b1) b1) b1) (bop b0 b1)) b1 → ⊥
  bad8276  p = false≢true (cong lower p)
  cut8276 : Adequate {ℓ} ((op (op (op (op (var 0) (var 1)) (var 2)) (var 1)) (op (var 0) (var 2))) , (var 1)) → ⊥
  cut8276  adequate = bad8276  (Adequate.valid adequate Two boolean env3)
  bad8277 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b0) b1) b0) (bop b0 b1)) b1 → ⊥
  bad8277  p = false≢true (cong lower p)
  cut8277 : Adequate {ℓ} ((op (op (op (op (var 0) (var 1)) (var 2)) (var 1)) (op (var 0) (var 2))) , (var 2)) → ⊥
  cut8277  adequate = bad8277  (Adequate.valid adequate Two boolean env1)
  bad8278 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b0) b0) b0) (bop b0 b0)) b1 → ⊥
  bad8278  p = false≢true (cong lower p)
  cut8278 : Adequate {ℓ} ((op (op (op (op (var 0) (var 1)) (var 2)) (var 1)) (op (var 0) (var 2))) , (var 3)) → ⊥
  cut8278  adequate = bad8278  (Adequate.valid adequate Two boolean env5)
  bad8279 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b1) b0) b1) (bop b0 b0)) b0 → ⊥
  bad8279  p = false≢true (sym (cong lower p))
  cut8279 : Adequate {ℓ} ((op (op (op (op (var 0) (var 1)) (var 2)) (var 1)) (op (var 0) (var 3))) , (var 0)) → ⊥
  cut8279  adequate = bad8279  (Adequate.valid adequate Two boolean env19)
  bad8280 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b1) b1) b1) (bop b0 b0)) b1 → ⊥
  bad8280  p = false≢true (cong lower p)
  cut8280 : Adequate {ℓ} ((op (op (op (op (var 0) (var 1)) (var 2)) (var 1)) (op (var 0) (var 3))) , (var 1)) → ⊥
  cut8280  adequate = bad8280  (Adequate.valid adequate Two boolean env12)
  bad8281 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b0) b1) b0) (bop b0 b0)) b1 → ⊥
  bad8281  p = false≢true (cong lower p)
  cut8281 : Adequate {ℓ} ((op (op (op (op (var 0) (var 1)) (var 2)) (var 1)) (op (var 0) (var 3))) , (var 2)) → ⊥
  cut8281  adequate = bad8281  (Adequate.valid adequate Two boolean env8)
  bad8282 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b0) b0) b0) (bop b0 b1)) b1 → ⊥
  bad8282  p = false≢true (cong lower p)
  cut8282 : Adequate {ℓ} ((op (op (op (op (var 0) (var 1)) (var 2)) (var 1)) (op (var 0) (var 3))) , (var 3)) → ⊥
  cut8282  adequate = bad8282  (Adequate.valid adequate Two boolean env5)
  bad8283 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b0) b0) b0) (bop b0 b0)) b1 → ⊥
  bad8283  p = false≢true (cong lower p)
  cut8283 : Adequate {ℓ} ((op (op (op (op (var 0) (var 1)) (var 2)) (var 1)) (op (var 0) (var 3))) , (var 4)) → ⊥
  cut8283  adequate = bad8283  (Adequate.valid adequate Two boolean env9)
  bad8284 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b1) b0) b1) (bop b1 b0)) b0 → ⊥
  bad8284  p = false≢true (sym (cong lower p))
  cut8284 : Adequate {ℓ} ((op (op (op (op (var 0) (var 1)) (var 2)) (var 1)) (op (var 1) (var 0))) , (var 0)) → ⊥
  cut8284  adequate = bad8284  (Adequate.valid adequate Two boolean env4)
  bad8285 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b1) b1) b1) (bop b1 b0)) b1 → ⊥
  bad8285  p = false≢true (cong lower p)
  cut8285 : Adequate {ℓ} ((op (op (op (op (var 0) (var 1)) (var 2)) (var 1)) (op (var 1) (var 0))) , (var 1)) → ⊥
  cut8285  adequate = bad8285  (Adequate.valid adequate Two boolean env3)
  bad8286 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b0) b1) b0) (bop b0 b0)) b1 → ⊥
  bad8286  p = false≢true (cong lower p)
  cut8286 : Adequate {ℓ} ((op (op (op (op (var 0) (var 1)) (var 2)) (var 1)) (op (var 1) (var 0))) , (var 2)) → ⊥
  cut8286  adequate = bad8286  (Adequate.valid adequate Two boolean env1)
  bad8287 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b0) b0) b0) (bop b0 b0)) b1 → ⊥
  bad8287  p = false≢true (cong lower p)
  cut8287 : Adequate {ℓ} ((op (op (op (op (var 0) (var 1)) (var 2)) (var 1)) (op (var 1) (var 0))) , (var 3)) → ⊥
  cut8287  adequate = bad8287  (Adequate.valid adequate Two boolean env5)
  bad8288 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b1) b0) b1) (bop b1 b1)) b0 → ⊥
  bad8288  p = false≢true (sym (cong lower p))
  cut8288 : Adequate {ℓ} ((op (op (op (op (var 0) (var 1)) (var 2)) (var 1)) (op (var 1) (var 1))) , (var 0)) → ⊥
  cut8288  adequate = bad8288  (Adequate.valid adequate Two boolean env4)
  holds8289 : (z0 z1 z2 : A3) → (mul3 (mul3 (mul3 (mul3 z0 z1) z2) z1) (mul3 z1 z1)) ≡ z1
  holds8289 z0 z1 z2 = refl
  cut8289 : Adequate {ℓ} ((op (op (op (op (var 0) (var 1)) (var 2)) (var 1)) (op (var 1) (var 1))) , (var 1)) → ⊥
  cut8289  = reject3 ((op (op (op (op (var 0) (var 1)) (var 2)) (var 1)) (op (var 1) (var 1))) , (var 1)) (λ env → holds8289 (env 0) (env 1) (env 2))
  bad8290 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b0) b1) b0) (bop b0 b0)) b1 → ⊥
  bad8290  p = false≢true (cong lower p)
  cut8290 : Adequate {ℓ} ((op (op (op (op (var 0) (var 1)) (var 2)) (var 1)) (op (var 1) (var 1))) , (var 2)) → ⊥
  cut8290  adequate = bad8290  (Adequate.valid adequate Two boolean env1)
  bad8291 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b0) b0) b0) (bop b0 b0)) b1 → ⊥
  bad8291  p = false≢true (cong lower p)
  cut8291 : Adequate {ℓ} ((op (op (op (op (var 0) (var 1)) (var 2)) (var 1)) (op (var 1) (var 1))) , (var 3)) → ⊥
  cut8291  adequate = bad8291  (Adequate.valid adequate Two boolean env5)
  bad8292 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b1) b0) b1) (bop b1 b0)) b0 → ⊥
  bad8292  p = false≢true (sym (cong lower p))
  cut8292 : Adequate {ℓ} ((op (op (op (op (var 0) (var 1)) (var 2)) (var 1)) (op (var 1) (var 2))) , (var 0)) → ⊥
  cut8292  adequate = bad8292  (Adequate.valid adequate Two boolean env4)
  holds8293 : (z0 z1 z2 : A13) → (mul13 (mul13 (mul13 (mul13 z0 z1) z2) z1) (mul13 z1 z2)) ≡ z1
  holds8293 m13c0 m13c0 m13c0 = refl
  holds8293 m13c0 m13c0 m13c1 = refl
  holds8293 m13c0 m13c0 m13c2 = refl
  holds8293 m13c0 m13c0 m13c3 = refl
  holds8293 m13c0 m13c1 m13c0 = refl
  holds8293 m13c0 m13c1 m13c1 = refl
  holds8293 m13c0 m13c1 m13c2 = refl
  holds8293 m13c0 m13c1 m13c3 = refl
  holds8293 m13c0 m13c2 m13c0 = refl
  holds8293 m13c0 m13c2 m13c1 = refl
  holds8293 m13c0 m13c2 m13c2 = refl
  holds8293 m13c0 m13c2 m13c3 = refl
  holds8293 m13c0 m13c3 m13c0 = refl
  holds8293 m13c0 m13c3 m13c1 = refl
  holds8293 m13c0 m13c3 m13c2 = refl
  holds8293 m13c0 m13c3 m13c3 = refl
  holds8293 m13c1 m13c0 m13c0 = refl
  holds8293 m13c1 m13c0 m13c1 = refl
  holds8293 m13c1 m13c0 m13c2 = refl
  holds8293 m13c1 m13c0 m13c3 = refl
  holds8293 m13c1 m13c1 m13c0 = refl
  holds8293 m13c1 m13c1 m13c1 = refl
  holds8293 m13c1 m13c1 m13c2 = refl
  holds8293 m13c1 m13c1 m13c3 = refl
  holds8293 m13c1 m13c2 m13c0 = refl
  holds8293 m13c1 m13c2 m13c1 = refl
  holds8293 m13c1 m13c2 m13c2 = refl
  holds8293 m13c1 m13c2 m13c3 = refl
  holds8293 m13c1 m13c3 m13c0 = refl
  holds8293 m13c1 m13c3 m13c1 = refl
  holds8293 m13c1 m13c3 m13c2 = refl
  holds8293 m13c1 m13c3 m13c3 = refl
  holds8293 m13c2 m13c0 m13c0 = refl
  holds8293 m13c2 m13c0 m13c1 = refl
  holds8293 m13c2 m13c0 m13c2 = refl
  holds8293 m13c2 m13c0 m13c3 = refl
  holds8293 m13c2 m13c1 m13c0 = refl
  holds8293 m13c2 m13c1 m13c1 = refl
  holds8293 m13c2 m13c1 m13c2 = refl
  holds8293 m13c2 m13c1 m13c3 = refl
  holds8293 m13c2 m13c2 m13c0 = refl
  holds8293 m13c2 m13c2 m13c1 = refl
  holds8293 m13c2 m13c2 m13c2 = refl
  holds8293 m13c2 m13c2 m13c3 = refl
  holds8293 m13c2 m13c3 m13c0 = refl
  holds8293 m13c2 m13c3 m13c1 = refl
  holds8293 m13c2 m13c3 m13c2 = refl
  holds8293 m13c2 m13c3 m13c3 = refl
  holds8293 m13c3 m13c0 m13c0 = refl
  holds8293 m13c3 m13c0 m13c1 = refl
  holds8293 m13c3 m13c0 m13c2 = refl
  holds8293 m13c3 m13c0 m13c3 = refl
  holds8293 m13c3 m13c1 m13c0 = refl
  holds8293 m13c3 m13c1 m13c1 = refl
  holds8293 m13c3 m13c1 m13c2 = refl
  holds8293 m13c3 m13c1 m13c3 = refl
  holds8293 m13c3 m13c2 m13c0 = refl
  holds8293 m13c3 m13c2 m13c1 = refl
  holds8293 m13c3 m13c2 m13c2 = refl
  holds8293 m13c3 m13c2 m13c3 = refl
  holds8293 m13c3 m13c3 m13c0 = refl
  holds8293 m13c3 m13c3 m13c1 = refl
  holds8293 m13c3 m13c3 m13c2 = refl
  holds8293 m13c3 m13c3 m13c3 = refl
  cut8293 : Adequate {ℓ} ((op (op (op (op (var 0) (var 1)) (var 2)) (var 1)) (op (var 1) (var 2))) , (var 1)) → ⊥
  cut8293  = reject13 ((op (op (op (op (var 0) (var 1)) (var 2)) (var 1)) (op (var 1) (var 2))) , (var 1)) (λ env → holds8293 (env 0) (env 1) (env 2))
  bad8294 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b0) b1) b0) (bop b0 b1)) b1 → ⊥
  bad8294  p = false≢true (cong lower p)
  cut8294 : Adequate {ℓ} ((op (op (op (op (var 0) (var 1)) (var 2)) (var 1)) (op (var 1) (var 2))) , (var 2)) → ⊥
  cut8294  adequate = bad8294  (Adequate.valid adequate Two boolean env1)
  bad8295 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b0) b0) b0) (bop b0 b0)) b1 → ⊥
  bad8295  p = false≢true (cong lower p)
  cut8295 : Adequate {ℓ} ((op (op (op (op (var 0) (var 1)) (var 2)) (var 1)) (op (var 1) (var 2))) , (var 3)) → ⊥
  cut8295  adequate = bad8295  (Adequate.valid adequate Two boolean env5)
  bad8296 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b1) b0) b1) (bop b1 b0)) b0 → ⊥
  bad8296  p = false≢true (sym (cong lower p))
  cut8296 : Adequate {ℓ} ((op (op (op (op (var 0) (var 1)) (var 2)) (var 1)) (op (var 1) (var 3))) , (var 0)) → ⊥
  cut8296  adequate = bad8296  (Adequate.valid adequate Two boolean env19)
  bad8297 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b1) b1) b1) (bop b1 b0)) b1 → ⊥
  bad8297  p = false≢true (cong lower p)
  cut8297 : Adequate {ℓ} ((op (op (op (op (var 0) (var 1)) (var 2)) (var 1)) (op (var 1) (var 3))) , (var 1)) → ⊥
  cut8297  adequate = bad8297  (Adequate.valid adequate Two boolean env12)
  bad8298 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b0) b1) b0) (bop b0 b0)) b1 → ⊥
  bad8298  p = false≢true (cong lower p)
  cut8298 : Adequate {ℓ} ((op (op (op (op (var 0) (var 1)) (var 2)) (var 1)) (op (var 1) (var 3))) , (var 2)) → ⊥
  cut8298  adequate = bad8298  (Adequate.valid adequate Two boolean env8)
  bad8299 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b0) b0) b0) (bop b0 b1)) b1 → ⊥
  bad8299  p = false≢true (cong lower p)
  cut8299 : Adequate {ℓ} ((op (op (op (op (var 0) (var 1)) (var 2)) (var 1)) (op (var 1) (var 3))) , (var 3)) → ⊥
  cut8299  adequate = bad8299  (Adequate.valid adequate Two boolean env5)
  bad8300 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b0) b0) b0) (bop b0 b0)) b1 → ⊥
  bad8300  p = false≢true (cong lower p)
  cut8300 : Adequate {ℓ} ((op (op (op (op (var 0) (var 1)) (var 2)) (var 1)) (op (var 1) (var 3))) , (var 4)) → ⊥
  cut8300  adequate = bad8300  (Adequate.valid adequate Two boolean env9)
  bad8301 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b1) b0) b1) (bop b0 b0)) b0 → ⊥
  bad8301  p = false≢true (sym (cong lower p))
  cut8301 : Adequate {ℓ} ((op (op (op (op (var 0) (var 1)) (var 2)) (var 1)) (op (var 2) (var 0))) , (var 0)) → ⊥
  cut8301  adequate = bad8301  (Adequate.valid adequate Two boolean env4)
  bad8302 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b1) b1) b1) (bop b1 b0)) b1 → ⊥
  bad8302  p = false≢true (cong lower p)
  cut8302 : Adequate {ℓ} ((op (op (op (op (var 0) (var 1)) (var 2)) (var 1)) (op (var 2) (var 0))) , (var 1)) → ⊥
  cut8302  adequate = bad8302  (Adequate.valid adequate Two boolean env3)
  bad8303 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b0) b1) b0) (bop b1 b0)) b1 → ⊥
  bad8303  p = false≢true (cong lower p)
  cut8303 : Adequate {ℓ} ((op (op (op (op (var 0) (var 1)) (var 2)) (var 1)) (op (var 2) (var 0))) , (var 2)) → ⊥
  cut8303  adequate = bad8303  (Adequate.valid adequate Two boolean env1)
  bad8304 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b0) b0) b0) (bop b0 b0)) b1 → ⊥
  bad8304  p = false≢true (cong lower p)
  cut8304 : Adequate {ℓ} ((op (op (op (op (var 0) (var 1)) (var 2)) (var 1)) (op (var 2) (var 0))) , (var 3)) → ⊥
  cut8304  adequate = bad8304  (Adequate.valid adequate Two boolean env5)
  bad8305 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b1) b0) b1) (bop b0 b1)) b0 → ⊥
  bad8305  p = false≢true (sym (cong lower p))
  cut8305 : Adequate {ℓ} ((op (op (op (op (var 0) (var 1)) (var 2)) (var 1)) (op (var 2) (var 1))) , (var 0)) → ⊥
  cut8305  adequate = bad8305  (Adequate.valid adequate Two boolean env4)
  holds8306 : (z0 z1 z2 : A3) → (mul3 (mul3 (mul3 (mul3 z0 z1) z2) z1) (mul3 z2 z1)) ≡ z1
  holds8306 z0 z1 z2 = refl
  cut8306 : Adequate {ℓ} ((op (op (op (op (var 0) (var 1)) (var 2)) (var 1)) (op (var 2) (var 1))) , (var 1)) → ⊥
  cut8306  = reject3 ((op (op (op (op (var 0) (var 1)) (var 2)) (var 1)) (op (var 2) (var 1))) , (var 1)) (λ env → holds8306 (env 0) (env 1) (env 2))
  bad8307 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b0) b1) b0) (bop b1 b0)) b1 → ⊥
  bad8307  p = false≢true (cong lower p)
  cut8307 : Adequate {ℓ} ((op (op (op (op (var 0) (var 1)) (var 2)) (var 1)) (op (var 2) (var 1))) , (var 2)) → ⊥
  cut8307  adequate = bad8307  (Adequate.valid adequate Two boolean env1)
  bad8308 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b0) b0) b0) (bop b0 b0)) b1 → ⊥
  bad8308  p = false≢true (cong lower p)
  cut8308 : Adequate {ℓ} ((op (op (op (op (var 0) (var 1)) (var 2)) (var 1)) (op (var 2) (var 1))) , (var 3)) → ⊥
  cut8308  adequate = bad8308  (Adequate.valid adequate Two boolean env5)
  bad8309 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b0) b1) b0) (bop b1 b1)) b0 → ⊥
  bad8309  p = false≢true (sym (cong lower p))
  cut8309 : Adequate {ℓ} ((op (op (op (op (var 0) (var 1)) (var 2)) (var 1)) (op (var 2) (var 2))) , (var 0)) → ⊥
  cut8309  adequate = bad8309  (Adequate.valid adequate Two boolean env1)
  bad8310 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b0) b1) b0) (bop b1 b1)) b0 → ⊥
  bad8310  p = false≢true (sym (cong lower p))
  cut8310 : Adequate {ℓ} ((op (op (op (op (var 0) (var 1)) (var 2)) (var 1)) (op (var 2) (var 2))) , (var 1)) → ⊥
  cut8310  adequate = bad8310  (Adequate.valid adequate Two boolean env1)
  bad8311 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b1) b0) b1) (bop b0 b0)) b0 → ⊥
  bad8311  p = false≢true (sym (cong lower p))
  cut8311 : Adequate {ℓ} ((op (op (op (op (var 0) (var 1)) (var 2)) (var 1)) (op (var 2) (var 2))) , (var 2)) → ⊥
  cut8311  adequate = bad8311  (Adequate.valid adequate Two boolean env4)
  bad8312 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b0) b0) b0) (bop b0 b0)) b1 → ⊥
  bad8312  p = false≢true (cong lower p)
  cut8312 : Adequate {ℓ} ((op (op (op (op (var 0) (var 1)) (var 2)) (var 1)) (op (var 2) (var 2))) , (var 3)) → ⊥
  cut8312  adequate = bad8312  (Adequate.valid adequate Two boolean env5)
  bad8313 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b0) b1) b0) (bop b1 b1)) b0 → ⊥
  bad8313  p = false≢true (sym (cong lower p))
  cut8313 : Adequate {ℓ} ((op (op (op (op (var 0) (var 1)) (var 2)) (var 1)) (op (var 2) (var 3))) , (var 0)) → ⊥
  cut8313  adequate = bad8313  (Adequate.valid adequate Two boolean env7)
  bad8314 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b0) b1) b0) (bop b1 b1)) b0 → ⊥
  bad8314  p = false≢true (sym (cong lower p))
  cut8314 : Adequate {ℓ} ((op (op (op (op (var 0) (var 1)) (var 2)) (var 1)) (op (var 2) (var 3))) , (var 1)) → ⊥
  cut8314  adequate = bad8314  (Adequate.valid adequate Two boolean env7)
  bad8315 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b0) b1) b0) (bop b1 b0)) b1 → ⊥
  bad8315  p = false≢true (cong lower p)
  cut8315 : Adequate {ℓ} ((op (op (op (op (var 0) (var 1)) (var 2)) (var 1)) (op (var 2) (var 3))) , (var 2)) → ⊥
  cut8315  adequate = bad8315  (Adequate.valid adequate Two boolean env8)
  bad8316 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b0) b0) b0) (bop b0 b1)) b1 → ⊥
  bad8316  p = false≢true (cong lower p)
  cut8316 : Adequate {ℓ} ((op (op (op (op (var 0) (var 1)) (var 2)) (var 1)) (op (var 2) (var 3))) , (var 3)) → ⊥
  cut8316  adequate = bad8316  (Adequate.valid adequate Two boolean env5)
  bad8317 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b0) b0) b0) (bop b0 b0)) b1 → ⊥
  bad8317  p = false≢true (cong lower p)
  cut8317 : Adequate {ℓ} ((op (op (op (op (var 0) (var 1)) (var 2)) (var 1)) (op (var 2) (var 3))) , (var 4)) → ⊥
  cut8317  adequate = bad8317  (Adequate.valid adequate Two boolean env9)
  bad8318 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b1) b0) b1) (bop b0 b0)) b0 → ⊥
  bad8318  p = false≢true (sym (cong lower p))
  cut8318 : Adequate {ℓ} ((op (op (op (op (var 0) (var 1)) (var 2)) (var 1)) (op (var 3) (var 0))) , (var 0)) → ⊥
  cut8318  adequate = bad8318  (Adequate.valid adequate Two boolean env19)
  bad8319 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b1) b1) b1) (bop b0 b0)) b1 → ⊥
  bad8319  p = false≢true (cong lower p)
  cut8319 : Adequate {ℓ} ((op (op (op (op (var 0) (var 1)) (var 2)) (var 1)) (op (var 3) (var 0))) , (var 1)) → ⊥
  cut8319  adequate = bad8319  (Adequate.valid adequate Two boolean env12)
  bad8320 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b0) b1) b0) (bop b0 b0)) b1 → ⊥
  bad8320  p = false≢true (cong lower p)
  cut8320 : Adequate {ℓ} ((op (op (op (op (var 0) (var 1)) (var 2)) (var 1)) (op (var 3) (var 0))) , (var 2)) → ⊥
  cut8320  adequate = bad8320  (Adequate.valid adequate Two boolean env8)
  bad8321 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b0) b0) b0) (bop b1 b0)) b1 → ⊥
  bad8321  p = false≢true (cong lower p)
  cut8321 : Adequate {ℓ} ((op (op (op (op (var 0) (var 1)) (var 2)) (var 1)) (op (var 3) (var 0))) , (var 3)) → ⊥
  cut8321  adequate = bad8321  (Adequate.valid adequate Two boolean env5)
  bad8322 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b0) b0) b0) (bop b0 b0)) b1 → ⊥
  bad8322  p = false≢true (cong lower p)
  cut8322 : Adequate {ℓ} ((op (op (op (op (var 0) (var 1)) (var 2)) (var 1)) (op (var 3) (var 0))) , (var 4)) → ⊥
  cut8322  adequate = bad8322  (Adequate.valid adequate Two boolean env9)
  bad8323 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b1) b0) b1) (bop b0 b1)) b0 → ⊥
  bad8323  p = false≢true (sym (cong lower p))
  cut8323 : Adequate {ℓ} ((op (op (op (op (var 0) (var 1)) (var 2)) (var 1)) (op (var 3) (var 1))) , (var 0)) → ⊥
  cut8323  adequate = bad8323  (Adequate.valid adequate Two boolean env19)
  bad8324 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b1) b1) b1) (bop b0 b1)) b1 → ⊥
  bad8324  p = false≢true (cong lower p)
  cut8324 : Adequate {ℓ} ((op (op (op (op (var 0) (var 1)) (var 2)) (var 1)) (op (var 3) (var 1))) , (var 1)) → ⊥
  cut8324  adequate = bad8324  (Adequate.valid adequate Two boolean env12)
  bad8325 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b0) b1) b0) (bop b0 b0)) b1 → ⊥
  bad8325  p = false≢true (cong lower p)
  cut8325 : Adequate {ℓ} ((op (op (op (op (var 0) (var 1)) (var 2)) (var 1)) (op (var 3) (var 1))) , (var 2)) → ⊥
  cut8325  adequate = bad8325  (Adequate.valid adequate Two boolean env8)
  bad8326 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b0) b0) b0) (bop b1 b0)) b1 → ⊥
  bad8326  p = false≢true (cong lower p)
  cut8326 : Adequate {ℓ} ((op (op (op (op (var 0) (var 1)) (var 2)) (var 1)) (op (var 3) (var 1))) , (var 3)) → ⊥
  cut8326  adequate = bad8326  (Adequate.valid adequate Two boolean env5)
  bad8327 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b0) b0) b0) (bop b0 b0)) b1 → ⊥
  bad8327  p = false≢true (cong lower p)
  cut8327 : Adequate {ℓ} ((op (op (op (op (var 0) (var 1)) (var 2)) (var 1)) (op (var 3) (var 1))) , (var 4)) → ⊥
  cut8327  adequate = bad8327  (Adequate.valid adequate Two boolean env9)
  bad8328 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b0) b1) b0) (bop b1 b1)) b0 → ⊥
  bad8328  p = false≢true (sym (cong lower p))
  cut8328 : Adequate {ℓ} ((op (op (op (op (var 0) (var 1)) (var 2)) (var 1)) (op (var 3) (var 2))) , (var 0)) → ⊥
  cut8328  adequate = bad8328  (Adequate.valid adequate Two boolean env7)
  bad8329 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b0) b1) b0) (bop b1 b1)) b0 → ⊥
  bad8329  p = false≢true (sym (cong lower p))
  cut8329 : Adequate {ℓ} ((op (op (op (op (var 0) (var 1)) (var 2)) (var 1)) (op (var 3) (var 2))) , (var 1)) → ⊥
  cut8329  adequate = bad8329  (Adequate.valid adequate Two boolean env7)
  bad8330 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b0) b1) b0) (bop b0 b1)) b1 → ⊥
  bad8330  p = false≢true (cong lower p)
  cut8330 : Adequate {ℓ} ((op (op (op (op (var 0) (var 1)) (var 2)) (var 1)) (op (var 3) (var 2))) , (var 2)) → ⊥
  cut8330  adequate = bad8330  (Adequate.valid adequate Two boolean env8)
  bad8331 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b0) b0) b0) (bop b1 b0)) b1 → ⊥
  bad8331  p = false≢true (cong lower p)
  cut8331 : Adequate {ℓ} ((op (op (op (op (var 0) (var 1)) (var 2)) (var 1)) (op (var 3) (var 2))) , (var 3)) → ⊥
  cut8331  adequate = bad8331  (Adequate.valid adequate Two boolean env5)
  bad8332 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b0) b0) b0) (bop b0 b0)) b1 → ⊥
  bad8332  p = false≢true (cong lower p)
  cut8332 : Adequate {ℓ} ((op (op (op (op (var 0) (var 1)) (var 2)) (var 1)) (op (var 3) (var 2))) , (var 4)) → ⊥
  cut8332  adequate = bad8332  (Adequate.valid adequate Two boolean env9)
  bad8333 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b0) b0) b0) (bop b1 b1)) b0 → ⊥
  bad8333  p = false≢true (sym (cong lower p))
  cut8333 : Adequate {ℓ} ((op (op (op (op (var 0) (var 1)) (var 2)) (var 1)) (op (var 3) (var 3))) , (var 0)) → ⊥
  cut8333  adequate = bad8333  (Adequate.valid adequate Two boolean env5)
  bad8334 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b0) b0) b0) (bop b1 b1)) b0 → ⊥
  bad8334  p = false≢true (sym (cong lower p))
  cut8334 : Adequate {ℓ} ((op (op (op (op (var 0) (var 1)) (var 2)) (var 1)) (op (var 3) (var 3))) , (var 1)) → ⊥
  cut8334  adequate = bad8334  (Adequate.valid adequate Two boolean env5)
  bad8335 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b0) b0) b0) (bop b1 b1)) b0 → ⊥
  bad8335  p = false≢true (sym (cong lower p))
  cut8335 : Adequate {ℓ} ((op (op (op (op (var 0) (var 1)) (var 2)) (var 1)) (op (var 3) (var 3))) , (var 2)) → ⊥
  cut8335  adequate = bad8335  (Adequate.valid adequate Two boolean env5)
  bad8336 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b1) b0) b1) (bop b0 b0)) b0 → ⊥
  bad8336  p = false≢true (sym (cong lower p))
  cut8336 : Adequate {ℓ} ((op (op (op (op (var 0) (var 1)) (var 2)) (var 1)) (op (var 3) (var 3))) , (var 3)) → ⊥
  cut8336  adequate = bad8336  (Adequate.valid adequate Two boolean env19)
  bad8337 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b0) b0) b0) (bop b0 b0)) b1 → ⊥
  bad8337  p = false≢true (cong lower p)
  cut8337 : Adequate {ℓ} ((op (op (op (op (var 0) (var 1)) (var 2)) (var 1)) (op (var 3) (var 3))) , (var 4)) → ⊥
  cut8337  adequate = bad8337  (Adequate.valid adequate Two boolean env9)
  bad8338 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b0) b0) b0) (bop b1 b1)) b0 → ⊥
  bad8338  p = false≢true (sym (cong lower p))
  cut8338 : Adequate {ℓ} ((op (op (op (op (var 0) (var 1)) (var 2)) (var 1)) (op (var 3) (var 4))) , (var 0)) → ⊥
  cut8338  adequate = bad8338  (Adequate.valid adequate Two boolean env14)
  bad8339 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b0) b0) b0) (bop b1 b1)) b0 → ⊥
  bad8339  p = false≢true (sym (cong lower p))
  cut8339 : Adequate {ℓ} ((op (op (op (op (var 0) (var 1)) (var 2)) (var 1)) (op (var 3) (var 4))) , (var 1)) → ⊥
  cut8339  adequate = bad8339  (Adequate.valid adequate Two boolean env14)
  bad8340 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b0) b0) b0) (bop b1 b1)) b0 → ⊥
  bad8340  p = false≢true (sym (cong lower p))
  cut8340 : Adequate {ℓ} ((op (op (op (op (var 0) (var 1)) (var 2)) (var 1)) (op (var 3) (var 4))) , (var 2)) → ⊥
  cut8340  adequate = bad8340  (Adequate.valid adequate Two boolean env14)
  bad8341 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b0) b0) b0) (bop b1 b0)) b1 → ⊥
  bad8341  p = false≢true (cong lower p)
  cut8341 : Adequate {ℓ} ((op (op (op (op (var 0) (var 1)) (var 2)) (var 1)) (op (var 3) (var 4))) , (var 3)) → ⊥
  cut8341  adequate = bad8341  (Adequate.valid adequate Two boolean env15)
  bad8342 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b0) b0) b0) (bop b0 b1)) b1 → ⊥
  bad8342  p = false≢true (cong lower p)
  cut8342 : Adequate {ℓ} ((op (op (op (op (var 0) (var 1)) (var 2)) (var 1)) (op (var 3) (var 4))) , (var 4)) → ⊥
  cut8342  adequate = bad8342  (Adequate.valid adequate Two boolean env9)
  bad8343 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b0) b0) b0) (bop b0 b0)) b1 → ⊥
  bad8343  p = false≢true (cong lower p)
  cut8343 : Adequate {ℓ} ((op (op (op (op (var 0) (var 1)) (var 2)) (var 1)) (op (var 3) (var 4))) , (var 5)) → ⊥
  cut8343  adequate = bad8343  (Adequate.valid adequate Two boolean env16)
  holds8344 : (z0 z1 z2 : A2) → (mul2 (mul2 (mul2 (mul2 z0 z1) z2) z2) (mul2 z0 z0)) ≡ z0
  holds8344 z0 z1 z2 = refl
  cut8344 : Adequate {ℓ} ((op (op (op (op (var 0) (var 1)) (var 2)) (var 2)) (op (var 0) (var 0))) , (var 0)) → ⊥
  cut8344  = reject2 ((op (op (op (op (var 0) (var 1)) (var 2)) (var 2)) (op (var 0) (var 0))) , (var 0)) (λ env → holds8344 (env 0) (env 1) (env 2))
  bad8345 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b1) b0) b0) (bop b0 b0)) b1 → ⊥
  bad8345  p = false≢true (cong lower p)
  cut8345 : Adequate {ℓ} ((op (op (op (op (var 0) (var 1)) (var 2)) (var 2)) (op (var 0) (var 0))) , (var 1)) → ⊥
  cut8345  adequate = bad8345  (Adequate.valid adequate Two boolean env4)
  bad8346 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b0) b1) b1) (bop b0 b0)) b1 → ⊥
  bad8346  p = false≢true (cong lower p)
  cut8346 : Adequate {ℓ} ((op (op (op (op (var 0) (var 1)) (var 2)) (var 2)) (op (var 0) (var 0))) , (var 2)) → ⊥
  cut8346  adequate = bad8346  (Adequate.valid adequate Two boolean env1)
  bad8347 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b0) b0) b0) (bop b0 b0)) b1 → ⊥
  bad8347  p = false≢true (cong lower p)
  cut8347 : Adequate {ℓ} ((op (op (op (op (var 0) (var 1)) (var 2)) (var 2)) (op (var 0) (var 0))) , (var 3)) → ⊥
  cut8347  adequate = bad8347  (Adequate.valid adequate Two boolean env5)
  bad8348 : PathP (λ _ → Two) (bop (bop (bop (bop b1 b0) b0) b0) (bop b1 b0)) b1 → ⊥
  bad8348  p = false≢true (cong lower p)
  cut8348 : Adequate {ℓ} ((op (op (op (op (var 0) (var 1)) (var 2)) (var 2)) (op (var 0) (var 1))) , (var 0)) → ⊥
  cut8348  adequate = bad8348  (Adequate.valid adequate Two boolean env10)
  bad8349 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b1) b0) b0) (bop b0 b1)) b1 → ⊥
  bad8349  p = false≢true (cong lower p)
  cut8349 : Adequate {ℓ} ((op (op (op (op (var 0) (var 1)) (var 2)) (var 2)) (op (var 0) (var 1))) , (var 1)) → ⊥
  cut8349  adequate = bad8349  (Adequate.valid adequate Two boolean env4)
  bad8350 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b0) b1) b1) (bop b0 b0)) b1 → ⊥
  bad8350  p = false≢true (cong lower p)
  cut8350 : Adequate {ℓ} ((op (op (op (op (var 0) (var 1)) (var 2)) (var 2)) (op (var 0) (var 1))) , (var 2)) → ⊥
  cut8350  adequate = bad8350  (Adequate.valid adequate Two boolean env1)
  bad8351 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b0) b0) b0) (bop b0 b0)) b1 → ⊥
  bad8351  p = false≢true (cong lower p)
  cut8351 : Adequate {ℓ} ((op (op (op (op (var 0) (var 1)) (var 2)) (var 2)) (op (var 0) (var 1))) , (var 3)) → ⊥
  cut8351  adequate = bad8351  (Adequate.valid adequate Two boolean env5)
  bad8352 : PathP (λ _ → Two) (bop (bop (bop (bop b1 b0) b0) b0) (bop b1 b0)) b1 → ⊥
  bad8352  p = false≢true (cong lower p)
  cut8352 : Adequate {ℓ} ((op (op (op (op (var 0) (var 1)) (var 2)) (var 2)) (op (var 0) (var 2))) , (var 0)) → ⊥
  cut8352  adequate = bad8352  (Adequate.valid adequate Two boolean env10)
  bad8353 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b1) b0) b0) (bop b0 b0)) b1 → ⊥
  bad8353  p = false≢true (cong lower p)
  cut8353 : Adequate {ℓ} ((op (op (op (op (var 0) (var 1)) (var 2)) (var 2)) (op (var 0) (var 2))) , (var 1)) → ⊥
  cut8353  adequate = bad8353  (Adequate.valid adequate Two boolean env4)
  bad8354 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b0) b1) b1) (bop b0 b1)) b1 → ⊥
  bad8354  p = false≢true (cong lower p)
  cut8354 : Adequate {ℓ} ((op (op (op (op (var 0) (var 1)) (var 2)) (var 2)) (op (var 0) (var 2))) , (var 2)) → ⊥
  cut8354  adequate = bad8354  (Adequate.valid adequate Two boolean env1)
  bad8355 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b0) b0) b0) (bop b0 b0)) b1 → ⊥
  bad8355  p = false≢true (cong lower p)
  cut8355 : Adequate {ℓ} ((op (op (op (op (var 0) (var 1)) (var 2)) (var 2)) (op (var 0) (var 2))) , (var 3)) → ⊥
  cut8355  adequate = bad8355  (Adequate.valid adequate Two boolean env5)
  bad8356 : PathP (λ _ → Two) (bop (bop (bop (bop b1 b0) b0) b0) (bop b1 b0)) b1 → ⊥
  bad8356  p = false≢true (cong lower p)
  cut8356 : Adequate {ℓ} ((op (op (op (op (var 0) (var 1)) (var 2)) (var 2)) (op (var 0) (var 3))) , (var 0)) → ⊥
  cut8356  adequate = bad8356  (Adequate.valid adequate Two boolean env20)
  bad8357 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b1) b0) b0) (bop b0 b0)) b1 → ⊥
  bad8357  p = false≢true (cong lower p)
  cut8357 : Adequate {ℓ} ((op (op (op (op (var 0) (var 1)) (var 2)) (var 2)) (op (var 0) (var 3))) , (var 1)) → ⊥
  cut8357  adequate = bad8357  (Adequate.valid adequate Two boolean env19)
  bad8358 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b0) b1) b1) (bop b0 b0)) b1 → ⊥
  bad8358  p = false≢true (cong lower p)
  cut8358 : Adequate {ℓ} ((op (op (op (op (var 0) (var 1)) (var 2)) (var 2)) (op (var 0) (var 3))) , (var 2)) → ⊥
  cut8358  adequate = bad8358  (Adequate.valid adequate Two boolean env8)
  bad8359 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b0) b0) b0) (bop b0 b1)) b1 → ⊥
  bad8359  p = false≢true (cong lower p)
  cut8359 : Adequate {ℓ} ((op (op (op (op (var 0) (var 1)) (var 2)) (var 2)) (op (var 0) (var 3))) , (var 3)) → ⊥
  cut8359  adequate = bad8359  (Adequate.valid adequate Two boolean env5)
  bad8360 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b0) b0) b0) (bop b0 b0)) b1 → ⊥
  bad8360  p = false≢true (cong lower p)
  cut8360 : Adequate {ℓ} ((op (op (op (op (var 0) (var 1)) (var 2)) (var 2)) (op (var 0) (var 3))) , (var 4)) → ⊥
  cut8360  adequate = bad8360  (Adequate.valid adequate Two boolean env9)
  bad8361 : PathP (λ _ → Two) (bop (bop (bop (bop b1 b0) b0) b0) (bop b0 b1)) b1 → ⊥
  bad8361  p = false≢true (cong lower p)
  cut8361 : Adequate {ℓ} ((op (op (op (op (var 0) (var 1)) (var 2)) (var 2)) (op (var 1) (var 0))) , (var 0)) → ⊥
  cut8361  adequate = bad8361  (Adequate.valid adequate Two boolean env10)
  bad8362 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b1) b0) b0) (bop b1 b0)) b1 → ⊥
  bad8362  p = false≢true (cong lower p)
  cut8362 : Adequate {ℓ} ((op (op (op (op (var 0) (var 1)) (var 2)) (var 2)) (op (var 1) (var 0))) , (var 1)) → ⊥
  cut8362  adequate = bad8362  (Adequate.valid adequate Two boolean env4)
  bad8363 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b0) b1) b1) (bop b0 b0)) b1 → ⊥
  bad8363  p = false≢true (cong lower p)
  cut8363 : Adequate {ℓ} ((op (op (op (op (var 0) (var 1)) (var 2)) (var 2)) (op (var 1) (var 0))) , (var 2)) → ⊥
  cut8363  adequate = bad8363  (Adequate.valid adequate Two boolean env1)
  bad8364 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b0) b0) b0) (bop b0 b0)) b1 → ⊥
  bad8364  p = false≢true (cong lower p)
  cut8364 : Adequate {ℓ} ((op (op (op (op (var 0) (var 1)) (var 2)) (var 2)) (op (var 1) (var 0))) , (var 3)) → ⊥
  cut8364  adequate = bad8364  (Adequate.valid adequate Two boolean env5)
  bad8365 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b1) b0) b0) (bop b1 b1)) b0 → ⊥
  bad8365  p = false≢true (sym (cong lower p))
  cut8365 : Adequate {ℓ} ((op (op (op (op (var 0) (var 1)) (var 2)) (var 2)) (op (var 1) (var 1))) , (var 0)) → ⊥
  cut8365  adequate = bad8365  (Adequate.valid adequate Two boolean env4)
  holds8366 : (z0 z1 z2 : A3) → (mul3 (mul3 (mul3 (mul3 z0 z1) z2) z2) (mul3 z1 z1)) ≡ z1
  holds8366 z0 z1 z2 = refl
  cut8366 : Adequate {ℓ} ((op (op (op (op (var 0) (var 1)) (var 2)) (var 2)) (op (var 1) (var 1))) , (var 1)) → ⊥
  cut8366  = reject3 ((op (op (op (op (var 0) (var 1)) (var 2)) (var 2)) (op (var 1) (var 1))) , (var 1)) (λ env → holds8366 (env 0) (env 1) (env 2))
  bad8367 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b0) b1) b1) (bop b0 b0)) b1 → ⊥
  bad8367  p = false≢true (cong lower p)
  cut8367 : Adequate {ℓ} ((op (op (op (op (var 0) (var 1)) (var 2)) (var 2)) (op (var 1) (var 1))) , (var 2)) → ⊥
  cut8367  adequate = bad8367  (Adequate.valid adequate Two boolean env1)
  bad8368 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b0) b0) b0) (bop b0 b0)) b1 → ⊥
  bad8368  p = false≢true (cong lower p)
  cut8368 : Adequate {ℓ} ((op (op (op (op (var 0) (var 1)) (var 2)) (var 2)) (op (var 1) (var 1))) , (var 3)) → ⊥
  cut8368  adequate = bad8368  (Adequate.valid adequate Two boolean env5)
  bad8369 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b1) b1) b1) (bop b1 b1)) b0 → ⊥
  bad8369  p = false≢true (sym (cong lower p))
  cut8369 : Adequate {ℓ} ((op (op (op (op (var 0) (var 1)) (var 2)) (var 2)) (op (var 1) (var 2))) , (var 0)) → ⊥
  cut8369  adequate = bad8369  (Adequate.valid adequate Two boolean env3)
  bad8370 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b1) b0) b0) (bop b1 b0)) b1 → ⊥
  bad8370  p = false≢true (cong lower p)
  cut8370 : Adequate {ℓ} ((op (op (op (op (var 0) (var 1)) (var 2)) (var 2)) (op (var 1) (var 2))) , (var 1)) → ⊥
  cut8370  adequate = bad8370  (Adequate.valid adequate Two boolean env4)
  bad8371 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b0) b1) b1) (bop b0 b1)) b1 → ⊥
  bad8371  p = false≢true (cong lower p)
  cut8371 : Adequate {ℓ} ((op (op (op (op (var 0) (var 1)) (var 2)) (var 2)) (op (var 1) (var 2))) , (var 2)) → ⊥
  cut8371  adequate = bad8371  (Adequate.valid adequate Two boolean env1)
  bad8372 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b0) b0) b0) (bop b0 b0)) b1 → ⊥
  bad8372  p = false≢true (cong lower p)
  cut8372 : Adequate {ℓ} ((op (op (op (op (var 0) (var 1)) (var 2)) (var 2)) (op (var 1) (var 2))) , (var 3)) → ⊥
  cut8372  adequate = bad8372  (Adequate.valid adequate Two boolean env5)
  bad8373 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b1) b0) b0) (bop b1 b1)) b0 → ⊥
  bad8373  p = false≢true (sym (cong lower p))
  cut8373 : Adequate {ℓ} ((op (op (op (op (var 0) (var 1)) (var 2)) (var 2)) (op (var 1) (var 3))) , (var 0)) → ⊥
  cut8373  adequate = bad8373  (Adequate.valid adequate Two boolean env13)
  bad8374 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b1) b0) b0) (bop b1 b0)) b1 → ⊥
  bad8374  p = false≢true (cong lower p)
  cut8374 : Adequate {ℓ} ((op (op (op (op (var 0) (var 1)) (var 2)) (var 2)) (op (var 1) (var 3))) , (var 1)) → ⊥
  cut8374  adequate = bad8374  (Adequate.valid adequate Two boolean env19)
  bad8375 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b0) b1) b1) (bop b0 b0)) b1 → ⊥
  bad8375  p = false≢true (cong lower p)
  cut8375 : Adequate {ℓ} ((op (op (op (op (var 0) (var 1)) (var 2)) (var 2)) (op (var 1) (var 3))) , (var 2)) → ⊥
  cut8375  adequate = bad8375  (Adequate.valid adequate Two boolean env8)
  bad8376 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b0) b0) b0) (bop b0 b1)) b1 → ⊥
  bad8376  p = false≢true (cong lower p)
  cut8376 : Adequate {ℓ} ((op (op (op (op (var 0) (var 1)) (var 2)) (var 2)) (op (var 1) (var 3))) , (var 3)) → ⊥
  cut8376  adequate = bad8376  (Adequate.valid adequate Two boolean env5)
  bad8377 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b0) b0) b0) (bop b0 b0)) b1 → ⊥
  bad8377  p = false≢true (cong lower p)
  cut8377 : Adequate {ℓ} ((op (op (op (op (var 0) (var 1)) (var 2)) (var 2)) (op (var 1) (var 3))) , (var 4)) → ⊥
  cut8377  adequate = bad8377  (Adequate.valid adequate Two boolean env9)
  bad8378 : PathP (λ _ → Two) (bop (bop (bop (bop b1 b0) b0) b0) (bop b0 b1)) b1 → ⊥
  bad8378  p = false≢true (cong lower p)
  cut8378 : Adequate {ℓ} ((op (op (op (op (var 0) (var 1)) (var 2)) (var 2)) (op (var 2) (var 0))) , (var 0)) → ⊥
  cut8378  adequate = bad8378  (Adequate.valid adequate Two boolean env10)
  bad8379 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b1) b0) b0) (bop b0 b0)) b1 → ⊥
  bad8379  p = false≢true (cong lower p)
  cut8379 : Adequate {ℓ} ((op (op (op (op (var 0) (var 1)) (var 2)) (var 2)) (op (var 2) (var 0))) , (var 1)) → ⊥
  cut8379  adequate = bad8379  (Adequate.valid adequate Two boolean env4)
  bad8380 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b0) b1) b1) (bop b1 b0)) b1 → ⊥
  bad8380  p = false≢true (cong lower p)
  cut8380 : Adequate {ℓ} ((op (op (op (op (var 0) (var 1)) (var 2)) (var 2)) (op (var 2) (var 0))) , (var 2)) → ⊥
  cut8380  adequate = bad8380  (Adequate.valid adequate Two boolean env1)
  bad8381 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b0) b0) b0) (bop b0 b0)) b1 → ⊥
  bad8381  p = false≢true (cong lower p)
  cut8381 : Adequate {ℓ} ((op (op (op (op (var 0) (var 1)) (var 2)) (var 2)) (op (var 2) (var 0))) , (var 3)) → ⊥
  cut8381  adequate = bad8381  (Adequate.valid adequate Two boolean env5)
  bad8382 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b1) b1) b1) (bop b1 b1)) b0 → ⊥
  bad8382  p = false≢true (sym (cong lower p))
  cut8382 : Adequate {ℓ} ((op (op (op (op (var 0) (var 1)) (var 2)) (var 2)) (op (var 2) (var 1))) , (var 0)) → ⊥
  cut8382  adequate = bad8382  (Adequate.valid adequate Two boolean env3)
  bad8383 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b1) b0) b0) (bop b0 b1)) b1 → ⊥
  bad8383  p = false≢true (cong lower p)
  cut8383 : Adequate {ℓ} ((op (op (op (op (var 0) (var 1)) (var 2)) (var 2)) (op (var 2) (var 1))) , (var 1)) → ⊥
  cut8383  adequate = bad8383  (Adequate.valid adequate Two boolean env4)
  bad8384 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b0) b1) b1) (bop b1 b0)) b1 → ⊥
  bad8384  p = false≢true (cong lower p)
  cut8384 : Adequate {ℓ} ((op (op (op (op (var 0) (var 1)) (var 2)) (var 2)) (op (var 2) (var 1))) , (var 2)) → ⊥
  cut8384  adequate = bad8384  (Adequate.valid adequate Two boolean env1)
  bad8385 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b0) b0) b0) (bop b0 b0)) b1 → ⊥
  bad8385  p = false≢true (cong lower p)
  cut8385 : Adequate {ℓ} ((op (op (op (op (var 0) (var 1)) (var 2)) (var 2)) (op (var 2) (var 1))) , (var 3)) → ⊥
  cut8385  adequate = bad8385  (Adequate.valid adequate Two boolean env5)
  bad8386 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b0) b1) b1) (bop b1 b1)) b0 → ⊥
  bad8386  p = false≢true (sym (cong lower p))
  cut8386 : Adequate {ℓ} ((op (op (op (op (var 0) (var 1)) (var 2)) (var 2)) (op (var 2) (var 2))) , (var 0)) → ⊥
  cut8386  adequate = bad8386  (Adequate.valid adequate Two boolean env1)
  bad8387 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b0) b1) b1) (bop b1 b1)) b0 → ⊥
  bad8387  p = false≢true (sym (cong lower p))
  cut8387 : Adequate {ℓ} ((op (op (op (op (var 0) (var 1)) (var 2)) (var 2)) (op (var 2) (var 2))) , (var 1)) → ⊥
  cut8387  adequate = bad8387  (Adequate.valid adequate Two boolean env1)
  holds8388 : (z0 z1 z2 : A3) → (mul3 (mul3 (mul3 (mul3 z0 z1) z2) z2) (mul3 z2 z2)) ≡ z2
  holds8388 z0 z1 z2 = refl
  cut8388 : Adequate {ℓ} ((op (op (op (op (var 0) (var 1)) (var 2)) (var 2)) (op (var 2) (var 2))) , (var 2)) → ⊥
  cut8388  = reject3 ((op (op (op (op (var 0) (var 1)) (var 2)) (var 2)) (op (var 2) (var 2))) , (var 2)) (λ env → holds8388 (env 0) (env 1) (env 2))
  bad8389 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b0) b0) b0) (bop b0 b0)) b1 → ⊥
  bad8389  p = false≢true (cong lower p)
  cut8389 : Adequate {ℓ} ((op (op (op (op (var 0) (var 1)) (var 2)) (var 2)) (op (var 2) (var 2))) , (var 3)) → ⊥
  cut8389  adequate = bad8389  (Adequate.valid adequate Two boolean env5)
  bad8390 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b0) b1) b1) (bop b1 b1)) b0 → ⊥
  bad8390  p = false≢true (sym (cong lower p))
  cut8390 : Adequate {ℓ} ((op (op (op (op (var 0) (var 1)) (var 2)) (var 2)) (op (var 2) (var 3))) , (var 0)) → ⊥
  cut8390  adequate = bad8390  (Adequate.valid adequate Two boolean env7)
  bad8391 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b0) b1) b1) (bop b1 b1)) b0 → ⊥
  bad8391  p = false≢true (sym (cong lower p))
  cut8391 : Adequate {ℓ} ((op (op (op (op (var 0) (var 1)) (var 2)) (var 2)) (op (var 2) (var 3))) , (var 1)) → ⊥
  cut8391  adequate = bad8391  (Adequate.valid adequate Two boolean env7)
  bad8392 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b0) b1) b1) (bop b1 b0)) b1 → ⊥
  bad8392  p = false≢true (cong lower p)
  cut8392 : Adequate {ℓ} ((op (op (op (op (var 0) (var 1)) (var 2)) (var 2)) (op (var 2) (var 3))) , (var 2)) → ⊥
  cut8392  adequate = bad8392  (Adequate.valid adequate Two boolean env8)
  bad8393 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b0) b0) b0) (bop b0 b1)) b1 → ⊥
  bad8393  p = false≢true (cong lower p)
  cut8393 : Adequate {ℓ} ((op (op (op (op (var 0) (var 1)) (var 2)) (var 2)) (op (var 2) (var 3))) , (var 3)) → ⊥
  cut8393  adequate = bad8393  (Adequate.valid adequate Two boolean env5)
  bad8394 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b0) b0) b0) (bop b0 b0)) b1 → ⊥
  bad8394  p = false≢true (cong lower p)
  cut8394 : Adequate {ℓ} ((op (op (op (op (var 0) (var 1)) (var 2)) (var 2)) (op (var 2) (var 3))) , (var 4)) → ⊥
  cut8394  adequate = bad8394  (Adequate.valid adequate Two boolean env9)
  bad8395 : PathP (λ _ → Two) (bop (bop (bop (bop b1 b0) b0) b0) (bop b0 b1)) b1 → ⊥
  bad8395  p = false≢true (cong lower p)
  cut8395 : Adequate {ℓ} ((op (op (op (op (var 0) (var 1)) (var 2)) (var 2)) (op (var 3) (var 0))) , (var 0)) → ⊥
  cut8395  adequate = bad8395  (Adequate.valid adequate Two boolean env20)
  bad8396 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b1) b0) b0) (bop b0 b0)) b1 → ⊥
  bad8396  p = false≢true (cong lower p)
  cut8396 : Adequate {ℓ} ((op (op (op (op (var 0) (var 1)) (var 2)) (var 2)) (op (var 3) (var 0))) , (var 1)) → ⊥
  cut8396  adequate = bad8396  (Adequate.valid adequate Two boolean env19)
  bad8397 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b0) b1) b1) (bop b0 b0)) b1 → ⊥
  bad8397  p = false≢true (cong lower p)
  cut8397 : Adequate {ℓ} ((op (op (op (op (var 0) (var 1)) (var 2)) (var 2)) (op (var 3) (var 0))) , (var 2)) → ⊥
  cut8397  adequate = bad8397  (Adequate.valid adequate Two boolean env8)
  bad8398 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b0) b0) b0) (bop b1 b0)) b1 → ⊥
  bad8398  p = false≢true (cong lower p)
  cut8398 : Adequate {ℓ} ((op (op (op (op (var 0) (var 1)) (var 2)) (var 2)) (op (var 3) (var 0))) , (var 3)) → ⊥
  cut8398  adequate = bad8398  (Adequate.valid adequate Two boolean env5)
  bad8399 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b0) b0) b0) (bop b0 b0)) b1 → ⊥
  bad8399  p = false≢true (cong lower p)
  cut8399 : Adequate {ℓ} ((op (op (op (op (var 0) (var 1)) (var 2)) (var 2)) (op (var 3) (var 0))) , (var 4)) → ⊥
  cut8399  adequate = bad8399  (Adequate.valid adequate Two boolean env9)
  bad8400 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b1) b0) b0) (bop b1 b1)) b0 → ⊥
  bad8400  p = false≢true (sym (cong lower p))
  cut8400 : Adequate {ℓ} ((op (op (op (op (var 0) (var 1)) (var 2)) (var 2)) (op (var 3) (var 1))) , (var 0)) → ⊥
  cut8400  adequate = bad8400  (Adequate.valid adequate Two boolean env13)
  bad8401 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b1) b0) b0) (bop b0 b1)) b1 → ⊥
  bad8401  p = false≢true (cong lower p)
  cut8401 : Adequate {ℓ} ((op (op (op (op (var 0) (var 1)) (var 2)) (var 2)) (op (var 3) (var 1))) , (var 1)) → ⊥
  cut8401  adequate = bad8401  (Adequate.valid adequate Two boolean env19)
  bad8402 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b0) b1) b1) (bop b0 b0)) b1 → ⊥
  bad8402  p = false≢true (cong lower p)
  cut8402 : Adequate {ℓ} ((op (op (op (op (var 0) (var 1)) (var 2)) (var 2)) (op (var 3) (var 1))) , (var 2)) → ⊥
  cut8402  adequate = bad8402  (Adequate.valid adequate Two boolean env8)
  bad8403 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b0) b0) b0) (bop b1 b0)) b1 → ⊥
  bad8403  p = false≢true (cong lower p)
  cut8403 : Adequate {ℓ} ((op (op (op (op (var 0) (var 1)) (var 2)) (var 2)) (op (var 3) (var 1))) , (var 3)) → ⊥
  cut8403  adequate = bad8403  (Adequate.valid adequate Two boolean env5)
  bad8404 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b0) b0) b0) (bop b0 b0)) b1 → ⊥
  bad8404  p = false≢true (cong lower p)
  cut8404 : Adequate {ℓ} ((op (op (op (op (var 0) (var 1)) (var 2)) (var 2)) (op (var 3) (var 1))) , (var 4)) → ⊥
  cut8404  adequate = bad8404  (Adequate.valid adequate Two boolean env9)
  bad8405 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b0) b1) b1) (bop b1 b1)) b0 → ⊥
  bad8405  p = false≢true (sym (cong lower p))
  cut8405 : Adequate {ℓ} ((op (op (op (op (var 0) (var 1)) (var 2)) (var 2)) (op (var 3) (var 2))) , (var 0)) → ⊥
  cut8405  adequate = bad8405  (Adequate.valid adequate Two boolean env7)
  bad8406 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b0) b1) b1) (bop b1 b1)) b0 → ⊥
  bad8406  p = false≢true (sym (cong lower p))
  cut8406 : Adequate {ℓ} ((op (op (op (op (var 0) (var 1)) (var 2)) (var 2)) (op (var 3) (var 2))) , (var 1)) → ⊥
  cut8406  adequate = bad8406  (Adequate.valid adequate Two boolean env7)
  bad8407 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b0) b1) b1) (bop b0 b1)) b1 → ⊥
  bad8407  p = false≢true (cong lower p)
  cut8407 : Adequate {ℓ} ((op (op (op (op (var 0) (var 1)) (var 2)) (var 2)) (op (var 3) (var 2))) , (var 2)) → ⊥
  cut8407  adequate = bad8407  (Adequate.valid adequate Two boolean env8)
  bad8408 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b0) b0) b0) (bop b1 b0)) b1 → ⊥
  bad8408  p = false≢true (cong lower p)
  cut8408 : Adequate {ℓ} ((op (op (op (op (var 0) (var 1)) (var 2)) (var 2)) (op (var 3) (var 2))) , (var 3)) → ⊥
  cut8408  adequate = bad8408  (Adequate.valid adequate Two boolean env5)
  bad8409 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b0) b0) b0) (bop b0 b0)) b1 → ⊥
  bad8409  p = false≢true (cong lower p)
  cut8409 : Adequate {ℓ} ((op (op (op (op (var 0) (var 1)) (var 2)) (var 2)) (op (var 3) (var 2))) , (var 4)) → ⊥
  cut8409  adequate = bad8409  (Adequate.valid adequate Two boolean env9)
  bad8410 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b0) b0) b0) (bop b1 b1)) b0 → ⊥
  bad8410  p = false≢true (sym (cong lower p))
  cut8410 : Adequate {ℓ} ((op (op (op (op (var 0) (var 1)) (var 2)) (var 2)) (op (var 3) (var 3))) , (var 0)) → ⊥
  cut8410  adequate = bad8410  (Adequate.valid adequate Two boolean env5)
  bad8411 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b0) b0) b0) (bop b1 b1)) b0 → ⊥
  bad8411  p = false≢true (sym (cong lower p))
  cut8411 : Adequate {ℓ} ((op (op (op (op (var 0) (var 1)) (var 2)) (var 2)) (op (var 3) (var 3))) , (var 1)) → ⊥
  cut8411  adequate = bad8411  (Adequate.valid adequate Two boolean env5)
  bad8412 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b0) b0) b0) (bop b1 b1)) b0 → ⊥
  bad8412  p = false≢true (sym (cong lower p))
  cut8412 : Adequate {ℓ} ((op (op (op (op (var 0) (var 1)) (var 2)) (var 2)) (op (var 3) (var 3))) , (var 2)) → ⊥
  cut8412  adequate = bad8412  (Adequate.valid adequate Two boolean env5)
  env21 : ℕ → Two
  env21 zero = b1
  env21 (suc zero) = b1
  env21 (suc (suc zero)) = b1
  env21 (suc (suc (suc zero))) = b0
  env21 (suc (suc (suc (suc rest)))) = b0
  bad8413 : PathP (λ _ → Two) (bop (bop (bop (bop b1 b1) b1) b1) (bop b0 b0)) b0 → ⊥
  bad8413  p = false≢true (sym (cong lower p))
  cut8413 : Adequate {ℓ} ((op (op (op (op (var 0) (var 1)) (var 2)) (var 2)) (op (var 3) (var 3))) , (var 3)) → ⊥
  cut8413  adequate = bad8413  (Adequate.valid adequate Two boolean env21)
  bad8414 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b0) b0) b0) (bop b0 b0)) b1 → ⊥
  bad8414  p = false≢true (cong lower p)
  cut8414 : Adequate {ℓ} ((op (op (op (op (var 0) (var 1)) (var 2)) (var 2)) (op (var 3) (var 3))) , (var 4)) → ⊥
  cut8414  adequate = bad8414  (Adequate.valid adequate Two boolean env9)
  bad8415 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b0) b0) b0) (bop b1 b1)) b0 → ⊥
  bad8415  p = false≢true (sym (cong lower p))
  cut8415 : Adequate {ℓ} ((op (op (op (op (var 0) (var 1)) (var 2)) (var 2)) (op (var 3) (var 4))) , (var 0)) → ⊥
  cut8415  adequate = bad8415  (Adequate.valid adequate Two boolean env14)
  bad8416 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b0) b0) b0) (bop b1 b1)) b0 → ⊥
  bad8416  p = false≢true (sym (cong lower p))
  cut8416 : Adequate {ℓ} ((op (op (op (op (var 0) (var 1)) (var 2)) (var 2)) (op (var 3) (var 4))) , (var 1)) → ⊥
  cut8416  adequate = bad8416  (Adequate.valid adequate Two boolean env14)
  bad8417 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b0) b0) b0) (bop b1 b1)) b0 → ⊥
  bad8417  p = false≢true (sym (cong lower p))
  cut8417 : Adequate {ℓ} ((op (op (op (op (var 0) (var 1)) (var 2)) (var 2)) (op (var 3) (var 4))) , (var 2)) → ⊥
  cut8417  adequate = bad8417  (Adequate.valid adequate Two boolean env14)
  bad8418 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b0) b0) b0) (bop b1 b0)) b1 → ⊥
  bad8418  p = false≢true (cong lower p)
  cut8418 : Adequate {ℓ} ((op (op (op (op (var 0) (var 1)) (var 2)) (var 2)) (op (var 3) (var 4))) , (var 3)) → ⊥
  cut8418  adequate = bad8418  (Adequate.valid adequate Two boolean env15)
  bad8419 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b0) b0) b0) (bop b0 b1)) b1 → ⊥
  bad8419  p = false≢true (cong lower p)
  cut8419 : Adequate {ℓ} ((op (op (op (op (var 0) (var 1)) (var 2)) (var 2)) (op (var 3) (var 4))) , (var 4)) → ⊥
  cut8419  adequate = bad8419  (Adequate.valid adequate Two boolean env9)
  bad8420 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b0) b0) b0) (bop b0 b0)) b1 → ⊥
  bad8420  p = false≢true (cong lower p)
  cut8420 : Adequate {ℓ} ((op (op (op (op (var 0) (var 1)) (var 2)) (var 2)) (op (var 3) (var 4))) , (var 5)) → ⊥
  cut8420  adequate = bad8420  (Adequate.valid adequate Two boolean env16)
  bad8421 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b0) b0) b1) (bop b0 b0)) b0 → ⊥
  bad8421  p = false≢true (sym (cong lower p))
  cut8421 : Adequate {ℓ} ((op (op (op (op (var 0) (var 1)) (var 2)) (var 3)) (op (var 0) (var 0))) , (var 0)) → ⊥
  cut8421  adequate = bad8421  (Adequate.valid adequate Two boolean env5)
  bad8422 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b0) b0) b1) (bop b0 b0)) b0 → ⊥
  bad8422  p = false≢true (sym (cong lower p))
  cut8422 : Adequate {ℓ} ((op (op (op (op (var 0) (var 1)) (var 2)) (var 3)) (op (var 0) (var 0))) , (var 1)) → ⊥
  cut8422  adequate = bad8422  (Adequate.valid adequate Two boolean env5)
  bad8423 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b0) b0) b1) (bop b0 b0)) b0 → ⊥
  bad8423  p = false≢true (sym (cong lower p))
  cut8423 : Adequate {ℓ} ((op (op (op (op (var 0) (var 1)) (var 2)) (var 3)) (op (var 0) (var 0))) , (var 2)) → ⊥
  cut8423  adequate = bad8423  (Adequate.valid adequate Two boolean env5)
  bad8424 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b0) b1) b1) (bop b0 b0)) b1 → ⊥
  bad8424  p = false≢true (cong lower p)
  cut8424 : Adequate {ℓ} ((op (op (op (op (var 0) (var 1)) (var 2)) (var 3)) (op (var 0) (var 0))) , (var 3)) → ⊥
  cut8424  adequate = bad8424  (Adequate.valid adequate Two boolean env7)
  bad8425 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b0) b0) b0) (bop b0 b0)) b1 → ⊥
  bad8425  p = false≢true (cong lower p)
  cut8425 : Adequate {ℓ} ((op (op (op (op (var 0) (var 1)) (var 2)) (var 3)) (op (var 0) (var 0))) , (var 4)) → ⊥
  cut8425  adequate = bad8425  (Adequate.valid adequate Two boolean env9)
  bad8426 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b0) b0) b1) (bop b0 b0)) b0 → ⊥
  bad8426  p = false≢true (sym (cong lower p))
  cut8426 : Adequate {ℓ} ((op (op (op (op (var 0) (var 1)) (var 2)) (var 3)) (op (var 0) (var 1))) , (var 0)) → ⊥
  cut8426  adequate = bad8426  (Adequate.valid adequate Two boolean env5)
  bad8427 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b0) b0) b1) (bop b0 b0)) b0 → ⊥
  bad8427  p = false≢true (sym (cong lower p))
  cut8427 : Adequate {ℓ} ((op (op (op (op (var 0) (var 1)) (var 2)) (var 3)) (op (var 0) (var 1))) , (var 1)) → ⊥
  cut8427  adequate = bad8427  (Adequate.valid adequate Two boolean env5)
  bad8428 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b0) b0) b1) (bop b0 b0)) b0 → ⊥
  bad8428  p = false≢true (sym (cong lower p))
  cut8428 : Adequate {ℓ} ((op (op (op (op (var 0) (var 1)) (var 2)) (var 3)) (op (var 0) (var 1))) , (var 2)) → ⊥
  cut8428  adequate = bad8428  (Adequate.valid adequate Two boolean env5)
  bad8429 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b0) b1) b1) (bop b0 b0)) b1 → ⊥
  bad8429  p = false≢true (cong lower p)
  cut8429 : Adequate {ℓ} ((op (op (op (op (var 0) (var 1)) (var 2)) (var 3)) (op (var 0) (var 1))) , (var 3)) → ⊥
  cut8429  adequate = bad8429  (Adequate.valid adequate Two boolean env7)
  bad8430 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b0) b0) b0) (bop b0 b0)) b1 → ⊥
  bad8430  p = false≢true (cong lower p)
  cut8430 : Adequate {ℓ} ((op (op (op (op (var 0) (var 1)) (var 2)) (var 3)) (op (var 0) (var 1))) , (var 4)) → ⊥
  cut8430  adequate = bad8430  (Adequate.valid adequate Two boolean env9)
  bad8431 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b0) b0) b1) (bop b0 b0)) b0 → ⊥
  bad8431  p = false≢true (sym (cong lower p))
  cut8431 : Adequate {ℓ} ((op (op (op (op (var 0) (var 1)) (var 2)) (var 3)) (op (var 0) (var 2))) , (var 0)) → ⊥
  cut8431  adequate = bad8431  (Adequate.valid adequate Two boolean env5)
  bad8432 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b0) b0) b1) (bop b0 b0)) b0 → ⊥
  bad8432  p = false≢true (sym (cong lower p))
  cut8432 : Adequate {ℓ} ((op (op (op (op (var 0) (var 1)) (var 2)) (var 3)) (op (var 0) (var 2))) , (var 1)) → ⊥
  cut8432  adequate = bad8432  (Adequate.valid adequate Two boolean env5)
  bad8433 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b0) b0) b1) (bop b0 b0)) b0 → ⊥
  bad8433  p = false≢true (sym (cong lower p))
  cut8433 : Adequate {ℓ} ((op (op (op (op (var 0) (var 1)) (var 2)) (var 3)) (op (var 0) (var 2))) , (var 2)) → ⊥
  cut8433  adequate = bad8433  (Adequate.valid adequate Two boolean env5)
  bad8434 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b0) b1) b1) (bop b0 b1)) b1 → ⊥
  bad8434  p = false≢true (cong lower p)
  cut8434 : Adequate {ℓ} ((op (op (op (op (var 0) (var 1)) (var 2)) (var 3)) (op (var 0) (var 2))) , (var 3)) → ⊥
  cut8434  adequate = bad8434  (Adequate.valid adequate Two boolean env7)
  bad8435 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b0) b0) b0) (bop b0 b0)) b1 → ⊥
  bad8435  p = false≢true (cong lower p)
  cut8435 : Adequate {ℓ} ((op (op (op (op (var 0) (var 1)) (var 2)) (var 3)) (op (var 0) (var 2))) , (var 4)) → ⊥
  cut8435  adequate = bad8435  (Adequate.valid adequate Two boolean env9)
  bad8436 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b0) b0) b1) (bop b0 b1)) b0 → ⊥
  bad8436  p = false≢true (sym (cong lower p))
  cut8436 : Adequate {ℓ} ((op (op (op (op (var 0) (var 1)) (var 2)) (var 3)) (op (var 0) (var 3))) , (var 0)) → ⊥
  cut8436  adequate = bad8436  (Adequate.valid adequate Two boolean env5)
  bad8437 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b0) b0) b1) (bop b0 b1)) b0 → ⊥
  bad8437  p = false≢true (sym (cong lower p))
  cut8437 : Adequate {ℓ} ((op (op (op (op (var 0) (var 1)) (var 2)) (var 3)) (op (var 0) (var 3))) , (var 1)) → ⊥
  cut8437  adequate = bad8437  (Adequate.valid adequate Two boolean env5)
  bad8438 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b0) b0) b1) (bop b0 b1)) b0 → ⊥
  bad8438  p = false≢true (sym (cong lower p))
  cut8438 : Adequate {ℓ} ((op (op (op (op (var 0) (var 1)) (var 2)) (var 3)) (op (var 0) (var 3))) , (var 2)) → ⊥
  cut8438  adequate = bad8438  (Adequate.valid adequate Two boolean env5)
  bad8439 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b0) b1) b1) (bop b0 b1)) b1 → ⊥
  bad8439  p = false≢true (cong lower p)
  cut8439 : Adequate {ℓ} ((op (op (op (op (var 0) (var 1)) (var 2)) (var 3)) (op (var 0) (var 3))) , (var 3)) → ⊥
  cut8439  adequate = bad8439  (Adequate.valid adequate Two boolean env7)
  bad8440 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b0) b0) b0) (bop b0 b0)) b1 → ⊥
  bad8440  p = false≢true (cong lower p)
  cut8440 : Adequate {ℓ} ((op (op (op (op (var 0) (var 1)) (var 2)) (var 3)) (op (var 0) (var 3))) , (var 4)) → ⊥
  cut8440  adequate = bad8440  (Adequate.valid adequate Two boolean env9)
  bad8441 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b0) b0) b1) (bop b0 b0)) b0 → ⊥
  bad8441  p = false≢true (sym (cong lower p))
  cut8441 : Adequate {ℓ} ((op (op (op (op (var 0) (var 1)) (var 2)) (var 3)) (op (var 0) (var 4))) , (var 0)) → ⊥
  cut8441  adequate = bad8441  (Adequate.valid adequate Two boolean env15)
  bad8442 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b0) b0) b1) (bop b0 b0)) b0 → ⊥
  bad8442  p = false≢true (sym (cong lower p))
  cut8442 : Adequate {ℓ} ((op (op (op (op (var 0) (var 1)) (var 2)) (var 3)) (op (var 0) (var 4))) , (var 1)) → ⊥
  cut8442  adequate = bad8442  (Adequate.valid adequate Two boolean env15)
  bad8443 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b0) b0) b1) (bop b0 b0)) b0 → ⊥
  bad8443  p = false≢true (sym (cong lower p))
  cut8443 : Adequate {ℓ} ((op (op (op (op (var 0) (var 1)) (var 2)) (var 3)) (op (var 0) (var 4))) , (var 2)) → ⊥
  cut8443  adequate = bad8443  (Adequate.valid adequate Two boolean env15)
  env22 : ℕ → Two
  env22 zero = b0
  env22 (suc zero) = b0
  env22 (suc (suc zero)) = b1
  env22 (suc (suc (suc zero))) = b1
  env22 (suc (suc (suc (suc zero)))) = b0
  env22 (suc (suc (suc (suc (suc rest))))) = b0
  bad8444 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b0) b1) b1) (bop b0 b0)) b1 → ⊥
  bad8444  p = false≢true (cong lower p)
  cut8444 : Adequate {ℓ} ((op (op (op (op (var 0) (var 1)) (var 2)) (var 3)) (op (var 0) (var 4))) , (var 3)) → ⊥
  cut8444  adequate = bad8444  (Adequate.valid adequate Two boolean env22)
  bad8445 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b0) b0) b0) (bop b0 b1)) b1 → ⊥
  bad8445  p = false≢true (cong lower p)
  cut8445 : Adequate {ℓ} ((op (op (op (op (var 0) (var 1)) (var 2)) (var 3)) (op (var 0) (var 4))) , (var 4)) → ⊥
  cut8445  adequate = bad8445  (Adequate.valid adequate Two boolean env9)
  bad8446 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b0) b0) b0) (bop b0 b0)) b1 → ⊥
  bad8446  p = false≢true (cong lower p)
  cut8446 : Adequate {ℓ} ((op (op (op (op (var 0) (var 1)) (var 2)) (var 3)) (op (var 0) (var 4))) , (var 5)) → ⊥
  cut8446  adequate = bad8446  (Adequate.valid adequate Two boolean env16)
  bad8447 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b0) b0) b1) (bop b0 b0)) b0 → ⊥
  bad8447  p = false≢true (sym (cong lower p))
  cut8447 : Adequate {ℓ} ((op (op (op (op (var 0) (var 1)) (var 2)) (var 3)) (op (var 1) (var 0))) , (var 0)) → ⊥
  cut8447  adequate = bad8447  (Adequate.valid adequate Two boolean env5)
  bad8448 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b0) b0) b1) (bop b0 b0)) b0 → ⊥
  bad8448  p = false≢true (sym (cong lower p))
  cut8448 : Adequate {ℓ} ((op (op (op (op (var 0) (var 1)) (var 2)) (var 3)) (op (var 1) (var 0))) , (var 1)) → ⊥
  cut8448  adequate = bad8448  (Adequate.valid adequate Two boolean env5)
  bad8449 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b0) b0) b1) (bop b0 b0)) b0 → ⊥
  bad8449  p = false≢true (sym (cong lower p))
  cut8449 : Adequate {ℓ} ((op (op (op (op (var 0) (var 1)) (var 2)) (var 3)) (op (var 1) (var 0))) , (var 2)) → ⊥
  cut8449  adequate = bad8449  (Adequate.valid adequate Two boolean env5)
  bad8450 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b0) b1) b1) (bop b0 b0)) b1 → ⊥
  bad8450  p = false≢true (cong lower p)
  cut8450 : Adequate {ℓ} ((op (op (op (op (var 0) (var 1)) (var 2)) (var 3)) (op (var 1) (var 0))) , (var 3)) → ⊥
  cut8450  adequate = bad8450  (Adequate.valid adequate Two boolean env7)
  bad8451 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b0) b0) b0) (bop b0 b0)) b1 → ⊥
  bad8451  p = false≢true (cong lower p)
  cut8451 : Adequate {ℓ} ((op (op (op (op (var 0) (var 1)) (var 2)) (var 3)) (op (var 1) (var 0))) , (var 4)) → ⊥
  cut8451  adequate = bad8451  (Adequate.valid adequate Two boolean env9)
  bad8452 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b0) b0) b1) (bop b0 b0)) b0 → ⊥
  bad8452  p = false≢true (sym (cong lower p))
  cut8452 : Adequate {ℓ} ((op (op (op (op (var 0) (var 1)) (var 2)) (var 3)) (op (var 1) (var 1))) , (var 0)) → ⊥
  cut8452  adequate = bad8452  (Adequate.valid adequate Two boolean env5)
  bad8453 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b0) b0) b1) (bop b0 b0)) b0 → ⊥
  bad8453  p = false≢true (sym (cong lower p))
  cut8453 : Adequate {ℓ} ((op (op (op (op (var 0) (var 1)) (var 2)) (var 3)) (op (var 1) (var 1))) , (var 1)) → ⊥
  cut8453  adequate = bad8453  (Adequate.valid adequate Two boolean env5)
  bad8454 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b0) b0) b1) (bop b0 b0)) b0 → ⊥
  bad8454  p = false≢true (sym (cong lower p))
  cut8454 : Adequate {ℓ} ((op (op (op (op (var 0) (var 1)) (var 2)) (var 3)) (op (var 1) (var 1))) , (var 2)) → ⊥
  cut8454  adequate = bad8454  (Adequate.valid adequate Two boolean env5)
  bad8455 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b0) b1) b1) (bop b0 b0)) b1 → ⊥
  bad8455  p = false≢true (cong lower p)
  cut8455 : Adequate {ℓ} ((op (op (op (op (var 0) (var 1)) (var 2)) (var 3)) (op (var 1) (var 1))) , (var 3)) → ⊥
  cut8455  adequate = bad8455  (Adequate.valid adequate Two boolean env7)
  bad8456 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b0) b0) b0) (bop b0 b0)) b1 → ⊥
  bad8456  p = false≢true (cong lower p)
  cut8456 : Adequate {ℓ} ((op (op (op (op (var 0) (var 1)) (var 2)) (var 3)) (op (var 1) (var 1))) , (var 4)) → ⊥
  cut8456  adequate = bad8456  (Adequate.valid adequate Two boolean env9)
  bad8457 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b0) b0) b1) (bop b0 b0)) b0 → ⊥
  bad8457  p = false≢true (sym (cong lower p))
  cut8457 : Adequate {ℓ} ((op (op (op (op (var 0) (var 1)) (var 2)) (var 3)) (op (var 1) (var 2))) , (var 0)) → ⊥
  cut8457  adequate = bad8457  (Adequate.valid adequate Two boolean env5)
  bad8458 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b0) b0) b1) (bop b0 b0)) b0 → ⊥
  bad8458  p = false≢true (sym (cong lower p))
  cut8458 : Adequate {ℓ} ((op (op (op (op (var 0) (var 1)) (var 2)) (var 3)) (op (var 1) (var 2))) , (var 1)) → ⊥
  cut8458  adequate = bad8458  (Adequate.valid adequate Two boolean env5)
  bad8459 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b0) b0) b1) (bop b0 b0)) b0 → ⊥
  bad8459  p = false≢true (sym (cong lower p))
  cut8459 : Adequate {ℓ} ((op (op (op (op (var 0) (var 1)) (var 2)) (var 3)) (op (var 1) (var 2))) , (var 2)) → ⊥
  cut8459  adequate = bad8459  (Adequate.valid adequate Two boolean env5)
  bad8460 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b0) b1) b1) (bop b0 b1)) b1 → ⊥
  bad8460  p = false≢true (cong lower p)
  cut8460 : Adequate {ℓ} ((op (op (op (op (var 0) (var 1)) (var 2)) (var 3)) (op (var 1) (var 2))) , (var 3)) → ⊥
  cut8460  adequate = bad8460  (Adequate.valid adequate Two boolean env7)
  bad8461 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b0) b0) b0) (bop b0 b0)) b1 → ⊥
  bad8461  p = false≢true (cong lower p)
  cut8461 : Adequate {ℓ} ((op (op (op (op (var 0) (var 1)) (var 2)) (var 3)) (op (var 1) (var 2))) , (var 4)) → ⊥
  cut8461  adequate = bad8461  (Adequate.valid adequate Two boolean env9)
  bad8462 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b0) b0) b1) (bop b0 b1)) b0 → ⊥
  bad8462  p = false≢true (sym (cong lower p))
  cut8462 : Adequate {ℓ} ((op (op (op (op (var 0) (var 1)) (var 2)) (var 3)) (op (var 1) (var 3))) , (var 0)) → ⊥
  cut8462  adequate = bad8462  (Adequate.valid adequate Two boolean env5)
  bad8463 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b0) b0) b1) (bop b0 b1)) b0 → ⊥
  bad8463  p = false≢true (sym (cong lower p))
  cut8463 : Adequate {ℓ} ((op (op (op (op (var 0) (var 1)) (var 2)) (var 3)) (op (var 1) (var 3))) , (var 1)) → ⊥
  cut8463  adequate = bad8463  (Adequate.valid adequate Two boolean env5)
  bad8464 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b0) b0) b1) (bop b0 b1)) b0 → ⊥
  bad8464  p = false≢true (sym (cong lower p))
  cut8464 : Adequate {ℓ} ((op (op (op (op (var 0) (var 1)) (var 2)) (var 3)) (op (var 1) (var 3))) , (var 2)) → ⊥
  cut8464  adequate = bad8464  (Adequate.valid adequate Two boolean env5)
  bad8465 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b0) b1) b1) (bop b0 b1)) b1 → ⊥
  bad8465  p = false≢true (cong lower p)
  cut8465 : Adequate {ℓ} ((op (op (op (op (var 0) (var 1)) (var 2)) (var 3)) (op (var 1) (var 3))) , (var 3)) → ⊥
  cut8465  adequate = bad8465  (Adequate.valid adequate Two boolean env7)
  bad8466 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b0) b0) b0) (bop b0 b0)) b1 → ⊥
  bad8466  p = false≢true (cong lower p)
  cut8466 : Adequate {ℓ} ((op (op (op (op (var 0) (var 1)) (var 2)) (var 3)) (op (var 1) (var 3))) , (var 4)) → ⊥
  cut8466  adequate = bad8466  (Adequate.valid adequate Two boolean env9)
  bad8467 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b0) b0) b1) (bop b0 b0)) b0 → ⊥
  bad8467  p = false≢true (sym (cong lower p))
  cut8467 : Adequate {ℓ} ((op (op (op (op (var 0) (var 1)) (var 2)) (var 3)) (op (var 1) (var 4))) , (var 0)) → ⊥
  cut8467  adequate = bad8467  (Adequate.valid adequate Two boolean env15)
  bad8468 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b0) b0) b1) (bop b0 b0)) b0 → ⊥
  bad8468  p = false≢true (sym (cong lower p))
  cut8468 : Adequate {ℓ} ((op (op (op (op (var 0) (var 1)) (var 2)) (var 3)) (op (var 1) (var 4))) , (var 1)) → ⊥
  cut8468  adequate = bad8468  (Adequate.valid adequate Two boolean env15)
  bad8469 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b0) b0) b1) (bop b0 b0)) b0 → ⊥
  bad8469  p = false≢true (sym (cong lower p))
  cut8469 : Adequate {ℓ} ((op (op (op (op (var 0) (var 1)) (var 2)) (var 3)) (op (var 1) (var 4))) , (var 2)) → ⊥
  cut8469  adequate = bad8469  (Adequate.valid adequate Two boolean env15)
  bad8470 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b0) b1) b1) (bop b0 b0)) b1 → ⊥
  bad8470  p = false≢true (cong lower p)
  cut8470 : Adequate {ℓ} ((op (op (op (op (var 0) (var 1)) (var 2)) (var 3)) (op (var 1) (var 4))) , (var 3)) → ⊥
  cut8470  adequate = bad8470  (Adequate.valid adequate Two boolean env22)
  bad8471 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b0) b0) b0) (bop b0 b1)) b1 → ⊥
  bad8471  p = false≢true (cong lower p)
  cut8471 : Adequate {ℓ} ((op (op (op (op (var 0) (var 1)) (var 2)) (var 3)) (op (var 1) (var 4))) , (var 4)) → ⊥
  cut8471  adequate = bad8471  (Adequate.valid adequate Two boolean env9)
  bad8472 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b0) b0) b0) (bop b0 b0)) b1 → ⊥
  bad8472  p = false≢true (cong lower p)
  cut8472 : Adequate {ℓ} ((op (op (op (op (var 0) (var 1)) (var 2)) (var 3)) (op (var 1) (var 4))) , (var 5)) → ⊥
  cut8472  adequate = bad8472  (Adequate.valid adequate Two boolean env16)
  bad8473 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b0) b0) b1) (bop b0 b0)) b0 → ⊥
  bad8473  p = false≢true (sym (cong lower p))
  cut8473 : Adequate {ℓ} ((op (op (op (op (var 0) (var 1)) (var 2)) (var 3)) (op (var 2) (var 0))) , (var 0)) → ⊥
  cut8473  adequate = bad8473  (Adequate.valid adequate Two boolean env5)
  bad8474 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b0) b0) b1) (bop b0 b0)) b0 → ⊥
  bad8474  p = false≢true (sym (cong lower p))
  cut8474 : Adequate {ℓ} ((op (op (op (op (var 0) (var 1)) (var 2)) (var 3)) (op (var 2) (var 0))) , (var 1)) → ⊥
  cut8474  adequate = bad8474  (Adequate.valid adequate Two boolean env5)
  bad8475 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b0) b0) b1) (bop b0 b0)) b0 → ⊥
  bad8475  p = false≢true (sym (cong lower p))
  cut8475 : Adequate {ℓ} ((op (op (op (op (var 0) (var 1)) (var 2)) (var 3)) (op (var 2) (var 0))) , (var 2)) → ⊥
  cut8475  adequate = bad8475  (Adequate.valid adequate Two boolean env5)
  bad8476 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b0) b1) b1) (bop b1 b0)) b1 → ⊥
  bad8476  p = false≢true (cong lower p)
  cut8476 : Adequate {ℓ} ((op (op (op (op (var 0) (var 1)) (var 2)) (var 3)) (op (var 2) (var 0))) , (var 3)) → ⊥
  cut8476  adequate = bad8476  (Adequate.valid adequate Two boolean env7)
  bad8477 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b0) b0) b0) (bop b0 b0)) b1 → ⊥
  bad8477  p = false≢true (cong lower p)
  cut8477 : Adequate {ℓ} ((op (op (op (op (var 0) (var 1)) (var 2)) (var 3)) (op (var 2) (var 0))) , (var 4)) → ⊥
  cut8477  adequate = bad8477  (Adequate.valid adequate Two boolean env9)
  bad8478 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b0) b0) b1) (bop b0 b0)) b0 → ⊥
  bad8478  p = false≢true (sym (cong lower p))
  cut8478 : Adequate {ℓ} ((op (op (op (op (var 0) (var 1)) (var 2)) (var 3)) (op (var 2) (var 1))) , (var 0)) → ⊥
  cut8478  adequate = bad8478  (Adequate.valid adequate Two boolean env5)
  bad8479 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b0) b0) b1) (bop b0 b0)) b0 → ⊥
  bad8479  p = false≢true (sym (cong lower p))
  cut8479 : Adequate {ℓ} ((op (op (op (op (var 0) (var 1)) (var 2)) (var 3)) (op (var 2) (var 1))) , (var 1)) → ⊥
  cut8479  adequate = bad8479  (Adequate.valid adequate Two boolean env5)
  bad8480 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b0) b0) b1) (bop b0 b0)) b0 → ⊥
  bad8480  p = false≢true (sym (cong lower p))
  cut8480 : Adequate {ℓ} ((op (op (op (op (var 0) (var 1)) (var 2)) (var 3)) (op (var 2) (var 1))) , (var 2)) → ⊥
  cut8480  adequate = bad8480  (Adequate.valid adequate Two boolean env5)
  bad8481 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b0) b1) b1) (bop b1 b0)) b1 → ⊥
  bad8481  p = false≢true (cong lower p)
  cut8481 : Adequate {ℓ} ((op (op (op (op (var 0) (var 1)) (var 2)) (var 3)) (op (var 2) (var 1))) , (var 3)) → ⊥
  cut8481  adequate = bad8481  (Adequate.valid adequate Two boolean env7)
  bad8482 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b0) b0) b0) (bop b0 b0)) b1 → ⊥
  bad8482  p = false≢true (cong lower p)
  cut8482 : Adequate {ℓ} ((op (op (op (op (var 0) (var 1)) (var 2)) (var 3)) (op (var 2) (var 1))) , (var 4)) → ⊥
  cut8482  adequate = bad8482  (Adequate.valid adequate Two boolean env9)
  bad8483 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b0) b0) b1) (bop b0 b0)) b0 → ⊥
  bad8483  p = false≢true (sym (cong lower p))
  cut8483 : Adequate {ℓ} ((op (op (op (op (var 0) (var 1)) (var 2)) (var 3)) (op (var 2) (var 2))) , (var 0)) → ⊥
  cut8483  adequate = bad8483  (Adequate.valid adequate Two boolean env5)
  bad8484 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b0) b0) b1) (bop b0 b0)) b0 → ⊥
  bad8484  p = false≢true (sym (cong lower p))
  cut8484 : Adequate {ℓ} ((op (op (op (op (var 0) (var 1)) (var 2)) (var 3)) (op (var 2) (var 2))) , (var 1)) → ⊥
  cut8484  adequate = bad8484  (Adequate.valid adequate Two boolean env5)
  bad8485 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b0) b0) b1) (bop b0 b0)) b0 → ⊥
  bad8485  p = false≢true (sym (cong lower p))
  cut8485 : Adequate {ℓ} ((op (op (op (op (var 0) (var 1)) (var 2)) (var 3)) (op (var 2) (var 2))) , (var 2)) → ⊥
  cut8485  adequate = bad8485  (Adequate.valid adequate Two boolean env5)
  bad8486 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b0) b1) b0) (bop b1 b1)) b0 → ⊥
  bad8486  p = false≢true (sym (cong lower p))
  cut8486 : Adequate {ℓ} ((op (op (op (op (var 0) (var 1)) (var 2)) (var 3)) (op (var 2) (var 2))) , (var 3)) → ⊥
  cut8486  adequate = bad8486  (Adequate.valid adequate Two boolean env8)
  bad8487 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b0) b0) b0) (bop b0 b0)) b1 → ⊥
  bad8487  p = false≢true (cong lower p)
  cut8487 : Adequate {ℓ} ((op (op (op (op (var 0) (var 1)) (var 2)) (var 3)) (op (var 2) (var 2))) , (var 4)) → ⊥
  cut8487  adequate = bad8487  (Adequate.valid adequate Two boolean env9)
  bad8488 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b0) b0) b1) (bop b0 b1)) b0 → ⊥
  bad8488  p = false≢true (sym (cong lower p))
  cut8488 : Adequate {ℓ} ((op (op (op (op (var 0) (var 1)) (var 2)) (var 3)) (op (var 2) (var 3))) , (var 0)) → ⊥
  cut8488  adequate = bad8488  (Adequate.valid adequate Two boolean env5)
  bad8489 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b0) b0) b1) (bop b0 b1)) b0 → ⊥
  bad8489  p = false≢true (sym (cong lower p))
  cut8489 : Adequate {ℓ} ((op (op (op (op (var 0) (var 1)) (var 2)) (var 3)) (op (var 2) (var 3))) , (var 1)) → ⊥
  cut8489  adequate = bad8489  (Adequate.valid adequate Two boolean env5)
  bad8490 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b0) b0) b1) (bop b0 b1)) b0 → ⊥
  bad8490  p = false≢true (sym (cong lower p))
  cut8490 : Adequate {ℓ} ((op (op (op (op (var 0) (var 1)) (var 2)) (var 3)) (op (var 2) (var 3))) , (var 2)) → ⊥
  cut8490  adequate = bad8490  (Adequate.valid adequate Two boolean env5)
  holds8491 : (z0 z1 z2 z3 : A3) → (mul3 (mul3 (mul3 (mul3 z0 z1) z2) z3) (mul3 z2 z3)) ≡ z3
  holds8491 z0 z1 z2 z3 = refl
  cut8491 : Adequate {ℓ} ((op (op (op (op (var 0) (var 1)) (var 2)) (var 3)) (op (var 2) (var 3))) , (var 3)) → ⊥
  cut8491  = reject3 ((op (op (op (op (var 0) (var 1)) (var 2)) (var 3)) (op (var 2) (var 3))) , (var 3)) (λ env → holds8491 (env 0) (env 1) (env 2) (env 3))
  bad8492 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b0) b0) b0) (bop b0 b0)) b1 → ⊥
  bad8492  p = false≢true (cong lower p)
  cut8492 : Adequate {ℓ} ((op (op (op (op (var 0) (var 1)) (var 2)) (var 3)) (op (var 2) (var 3))) , (var 4)) → ⊥
  cut8492  adequate = bad8492  (Adequate.valid adequate Two boolean env9)
  bad8493 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b0) b0) b1) (bop b0 b0)) b0 → ⊥
  bad8493  p = false≢true (sym (cong lower p))
  cut8493 : Adequate {ℓ} ((op (op (op (op (var 0) (var 1)) (var 2)) (var 3)) (op (var 2) (var 4))) , (var 0)) → ⊥
  cut8493  adequate = bad8493  (Adequate.valid adequate Two boolean env15)
  bad8494 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b0) b0) b1) (bop b0 b0)) b0 → ⊥
  bad8494  p = false≢true (sym (cong lower p))
  cut8494 : Adequate {ℓ} ((op (op (op (op (var 0) (var 1)) (var 2)) (var 3)) (op (var 2) (var 4))) , (var 1)) → ⊥
  cut8494  adequate = bad8494  (Adequate.valid adequate Two boolean env15)
  bad8495 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b0) b0) b1) (bop b0 b0)) b0 → ⊥
  bad8495  p = false≢true (sym (cong lower p))
  cut8495 : Adequate {ℓ} ((op (op (op (op (var 0) (var 1)) (var 2)) (var 3)) (op (var 2) (var 4))) , (var 2)) → ⊥
  cut8495  adequate = bad8495  (Adequate.valid adequate Two boolean env15)
  env23 : ℕ → Two
  env23 zero = b0
  env23 (suc zero) = b0
  env23 (suc (suc zero)) = b1
  env23 (suc (suc (suc zero))) = b0
  env23 (suc (suc (suc (suc zero)))) = b1
  env23 (suc (suc (suc (suc (suc rest))))) = b0
  bad8496 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b0) b1) b0) (bop b1 b1)) b0 → ⊥
  bad8496  p = false≢true (sym (cong lower p))
  cut8496 : Adequate {ℓ} ((op (op (op (op (var 0) (var 1)) (var 2)) (var 3)) (op (var 2) (var 4))) , (var 3)) → ⊥
  cut8496  adequate = bad8496  (Adequate.valid adequate Two boolean env23)
  bad8497 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b0) b0) b0) (bop b0 b1)) b1 → ⊥
  bad8497  p = false≢true (cong lower p)
  cut8497 : Adequate {ℓ} ((op (op (op (op (var 0) (var 1)) (var 2)) (var 3)) (op (var 2) (var 4))) , (var 4)) → ⊥
  cut8497  adequate = bad8497  (Adequate.valid adequate Two boolean env9)
  bad8498 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b0) b0) b0) (bop b0 b0)) b1 → ⊥
  bad8498  p = false≢true (cong lower p)
  cut8498 : Adequate {ℓ} ((op (op (op (op (var 0) (var 1)) (var 2)) (var 3)) (op (var 2) (var 4))) , (var 5)) → ⊥
  cut8498  adequate = bad8498  (Adequate.valid adequate Two boolean env16)
  bad8499 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b0) b0) b1) (bop b1 b0)) b0 → ⊥
  bad8499  p = false≢true (sym (cong lower p))
  cut8499 : Adequate {ℓ} ((op (op (op (op (var 0) (var 1)) (var 2)) (var 3)) (op (var 3) (var 0))) , (var 0)) → ⊥
  cut8499  adequate = bad8499  (Adequate.valid adequate Two boolean env5)
  bad8500 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b0) b0) b1) (bop b1 b0)) b0 → ⊥
  bad8500  p = false≢true (sym (cong lower p))
  cut8500 : Adequate {ℓ} ((op (op (op (op (var 0) (var 1)) (var 2)) (var 3)) (op (var 3) (var 0))) , (var 1)) → ⊥
  cut8500  adequate = bad8500  (Adequate.valid adequate Two boolean env5)
  bad8501 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b0) b0) b1) (bop b1 b0)) b0 → ⊥
  bad8501  p = false≢true (sym (cong lower p))
  cut8501 : Adequate {ℓ} ((op (op (op (op (var 0) (var 1)) (var 2)) (var 3)) (op (var 3) (var 0))) , (var 2)) → ⊥
  cut8501  adequate = bad8501  (Adequate.valid adequate Two boolean env5)
  bad8502 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b0) b1) b1) (bop b1 b0)) b1 → ⊥
  bad8502  p = false≢true (cong lower p)
  cut8502 : Adequate {ℓ} ((op (op (op (op (var 0) (var 1)) (var 2)) (var 3)) (op (var 3) (var 0))) , (var 3)) → ⊥
  cut8502  adequate = bad8502  (Adequate.valid adequate Two boolean env7)
  bad8503 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b0) b0) b0) (bop b0 b0)) b1 → ⊥
  bad8503  p = false≢true (cong lower p)
  cut8503 : Adequate {ℓ} ((op (op (op (op (var 0) (var 1)) (var 2)) (var 3)) (op (var 3) (var 0))) , (var 4)) → ⊥
  cut8503  adequate = bad8503  (Adequate.valid adequate Two boolean env9)
  bad8504 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b0) b0) b1) (bop b1 b0)) b0 → ⊥
  bad8504  p = false≢true (sym (cong lower p))
  cut8504 : Adequate {ℓ} ((op (op (op (op (var 0) (var 1)) (var 2)) (var 3)) (op (var 3) (var 1))) , (var 0)) → ⊥
  cut8504  adequate = bad8504  (Adequate.valid adequate Two boolean env5)
  bad8505 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b0) b0) b1) (bop b1 b0)) b0 → ⊥
  bad8505  p = false≢true (sym (cong lower p))
  cut8505 : Adequate {ℓ} ((op (op (op (op (var 0) (var 1)) (var 2)) (var 3)) (op (var 3) (var 1))) , (var 1)) → ⊥
  cut8505  adequate = bad8505  (Adequate.valid adequate Two boolean env5)
  bad8506 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b0) b0) b1) (bop b1 b0)) b0 → ⊥
  bad8506  p = false≢true (sym (cong lower p))
  cut8506 : Adequate {ℓ} ((op (op (op (op (var 0) (var 1)) (var 2)) (var 3)) (op (var 3) (var 1))) , (var 2)) → ⊥
  cut8506  adequate = bad8506  (Adequate.valid adequate Two boolean env5)
  bad8507 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b0) b1) b1) (bop b1 b0)) b1 → ⊥
  bad8507  p = false≢true (cong lower p)
  cut8507 : Adequate {ℓ} ((op (op (op (op (var 0) (var 1)) (var 2)) (var 3)) (op (var 3) (var 1))) , (var 3)) → ⊥
  cut8507  adequate = bad8507  (Adequate.valid adequate Two boolean env7)
  bad8508 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b0) b0) b0) (bop b0 b0)) b1 → ⊥
  bad8508  p = false≢true (cong lower p)
  cut8508 : Adequate {ℓ} ((op (op (op (op (var 0) (var 1)) (var 2)) (var 3)) (op (var 3) (var 1))) , (var 4)) → ⊥
  cut8508  adequate = bad8508  (Adequate.valid adequate Two boolean env9)
  bad8509 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b0) b0) b1) (bop b1 b0)) b0 → ⊥
  bad8509  p = false≢true (sym (cong lower p))
  cut8509 : Adequate {ℓ} ((op (op (op (op (var 0) (var 1)) (var 2)) (var 3)) (op (var 3) (var 2))) , (var 0)) → ⊥
  cut8509  adequate = bad8509  (Adequate.valid adequate Two boolean env5)
  bad8510 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b0) b0) b1) (bop b1 b0)) b0 → ⊥
  bad8510  p = false≢true (sym (cong lower p))
  cut8510 : Adequate {ℓ} ((op (op (op (op (var 0) (var 1)) (var 2)) (var 3)) (op (var 3) (var 2))) , (var 1)) → ⊥
  cut8510  adequate = bad8510  (Adequate.valid adequate Two boolean env5)
  bad8511 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b0) b0) b1) (bop b1 b0)) b0 → ⊥
  bad8511  p = false≢true (sym (cong lower p))
  cut8511 : Adequate {ℓ} ((op (op (op (op (var 0) (var 1)) (var 2)) (var 3)) (op (var 3) (var 2))) , (var 2)) → ⊥
  cut8511  adequate = bad8511  (Adequate.valid adequate Two boolean env5)
  holds8512 : (z0 z1 z2 z3 : A13) → (mul13 (mul13 (mul13 (mul13 z0 z1) z2) z3) (mul13 z3 z2)) ≡ z3
  holds8512 m13c0 m13c0 m13c0 m13c0 = refl
  holds8512 m13c0 m13c0 m13c0 m13c1 = refl
  holds8512 m13c0 m13c0 m13c0 m13c2 = refl
  holds8512 m13c0 m13c0 m13c0 m13c3 = refl
  holds8512 m13c0 m13c0 m13c1 m13c0 = refl
  holds8512 m13c0 m13c0 m13c1 m13c1 = refl
  holds8512 m13c0 m13c0 m13c1 m13c2 = refl
  holds8512 m13c0 m13c0 m13c1 m13c3 = refl
  holds8512 m13c0 m13c0 m13c2 m13c0 = refl
  holds8512 m13c0 m13c0 m13c2 m13c1 = refl
  holds8512 m13c0 m13c0 m13c2 m13c2 = refl
  holds8512 m13c0 m13c0 m13c2 m13c3 = refl
  holds8512 m13c0 m13c0 m13c3 m13c0 = refl
  holds8512 m13c0 m13c0 m13c3 m13c1 = refl
  holds8512 m13c0 m13c0 m13c3 m13c2 = refl
  holds8512 m13c0 m13c0 m13c3 m13c3 = refl
  holds8512 m13c0 m13c1 m13c0 m13c0 = refl
  holds8512 m13c0 m13c1 m13c0 m13c1 = refl
  holds8512 m13c0 m13c1 m13c0 m13c2 = refl
  holds8512 m13c0 m13c1 m13c0 m13c3 = refl
  holds8512 m13c0 m13c1 m13c1 m13c0 = refl
  holds8512 m13c0 m13c1 m13c1 m13c1 = refl
  holds8512 m13c0 m13c1 m13c1 m13c2 = refl
  holds8512 m13c0 m13c1 m13c1 m13c3 = refl
  holds8512 m13c0 m13c1 m13c2 m13c0 = refl
  holds8512 m13c0 m13c1 m13c2 m13c1 = refl
  holds8512 m13c0 m13c1 m13c2 m13c2 = refl
  holds8512 m13c0 m13c1 m13c2 m13c3 = refl
  holds8512 m13c0 m13c1 m13c3 m13c0 = refl
  holds8512 m13c0 m13c1 m13c3 m13c1 = refl
  holds8512 m13c0 m13c1 m13c3 m13c2 = refl
  holds8512 m13c0 m13c1 m13c3 m13c3 = refl
  holds8512 m13c0 m13c2 m13c0 m13c0 = refl
  holds8512 m13c0 m13c2 m13c0 m13c1 = refl
  holds8512 m13c0 m13c2 m13c0 m13c2 = refl
  holds8512 m13c0 m13c2 m13c0 m13c3 = refl
  holds8512 m13c0 m13c2 m13c1 m13c0 = refl
  holds8512 m13c0 m13c2 m13c1 m13c1 = refl
  holds8512 m13c0 m13c2 m13c1 m13c2 = refl
  holds8512 m13c0 m13c2 m13c1 m13c3 = refl
  holds8512 m13c0 m13c2 m13c2 m13c0 = refl
  holds8512 m13c0 m13c2 m13c2 m13c1 = refl
  holds8512 m13c0 m13c2 m13c2 m13c2 = refl
  holds8512 m13c0 m13c2 m13c2 m13c3 = refl
  holds8512 m13c0 m13c2 m13c3 m13c0 = refl
  holds8512 m13c0 m13c2 m13c3 m13c1 = refl
  holds8512 m13c0 m13c2 m13c3 m13c2 = refl
  holds8512 m13c0 m13c2 m13c3 m13c3 = refl
  holds8512 m13c0 m13c3 m13c0 m13c0 = refl
  holds8512 m13c0 m13c3 m13c0 m13c1 = refl
  holds8512 m13c0 m13c3 m13c0 m13c2 = refl
  holds8512 m13c0 m13c3 m13c0 m13c3 = refl
  holds8512 m13c0 m13c3 m13c1 m13c0 = refl
  holds8512 m13c0 m13c3 m13c1 m13c1 = refl
  holds8512 m13c0 m13c3 m13c1 m13c2 = refl
  holds8512 m13c0 m13c3 m13c1 m13c3 = refl
  holds8512 m13c0 m13c3 m13c2 m13c0 = refl
  holds8512 m13c0 m13c3 m13c2 m13c1 = refl
  holds8512 m13c0 m13c3 m13c2 m13c2 = refl
  holds8512 m13c0 m13c3 m13c2 m13c3 = refl
  holds8512 m13c0 m13c3 m13c3 m13c0 = refl
  holds8512 m13c0 m13c3 m13c3 m13c1 = refl
  holds8512 m13c0 m13c3 m13c3 m13c2 = refl
  holds8512 m13c0 m13c3 m13c3 m13c3 = refl
  holds8512 m13c1 m13c0 m13c0 m13c0 = refl
  holds8512 m13c1 m13c0 m13c0 m13c1 = refl
  holds8512 m13c1 m13c0 m13c0 m13c2 = refl
  holds8512 m13c1 m13c0 m13c0 m13c3 = refl
  holds8512 m13c1 m13c0 m13c1 m13c0 = refl
  holds8512 m13c1 m13c0 m13c1 m13c1 = refl
  holds8512 m13c1 m13c0 m13c1 m13c2 = refl
  holds8512 m13c1 m13c0 m13c1 m13c3 = refl
  holds8512 m13c1 m13c0 m13c2 m13c0 = refl
  holds8512 m13c1 m13c0 m13c2 m13c1 = refl
  holds8512 m13c1 m13c0 m13c2 m13c2 = refl
  holds8512 m13c1 m13c0 m13c2 m13c3 = refl
  holds8512 m13c1 m13c0 m13c3 m13c0 = refl
  holds8512 m13c1 m13c0 m13c3 m13c1 = refl
  holds8512 m13c1 m13c0 m13c3 m13c2 = refl
  holds8512 m13c1 m13c0 m13c3 m13c3 = refl
  holds8512 m13c1 m13c1 m13c0 m13c0 = refl
  holds8512 m13c1 m13c1 m13c0 m13c1 = refl
  holds8512 m13c1 m13c1 m13c0 m13c2 = refl
  holds8512 m13c1 m13c1 m13c0 m13c3 = refl
  holds8512 m13c1 m13c1 m13c1 m13c0 = refl
  holds8512 m13c1 m13c1 m13c1 m13c1 = refl
  holds8512 m13c1 m13c1 m13c1 m13c2 = refl
  holds8512 m13c1 m13c1 m13c1 m13c3 = refl
  holds8512 m13c1 m13c1 m13c2 m13c0 = refl
  holds8512 m13c1 m13c1 m13c2 m13c1 = refl
  holds8512 m13c1 m13c1 m13c2 m13c2 = refl
  holds8512 m13c1 m13c1 m13c2 m13c3 = refl
  holds8512 m13c1 m13c1 m13c3 m13c0 = refl
  holds8512 m13c1 m13c1 m13c3 m13c1 = refl
  holds8512 m13c1 m13c1 m13c3 m13c2 = refl
  holds8512 m13c1 m13c1 m13c3 m13c3 = refl
  holds8512 m13c1 m13c2 m13c0 m13c0 = refl
  holds8512 m13c1 m13c2 m13c0 m13c1 = refl
  holds8512 m13c1 m13c2 m13c0 m13c2 = refl
  holds8512 m13c1 m13c2 m13c0 m13c3 = refl
  holds8512 m13c1 m13c2 m13c1 m13c0 = refl
  holds8512 m13c1 m13c2 m13c1 m13c1 = refl
  holds8512 m13c1 m13c2 m13c1 m13c2 = refl
  holds8512 m13c1 m13c2 m13c1 m13c3 = refl
  holds8512 m13c1 m13c2 m13c2 m13c0 = refl
  holds8512 m13c1 m13c2 m13c2 m13c1 = refl
  holds8512 m13c1 m13c2 m13c2 m13c2 = refl
  holds8512 m13c1 m13c2 m13c2 m13c3 = refl
  holds8512 m13c1 m13c2 m13c3 m13c0 = refl
  holds8512 m13c1 m13c2 m13c3 m13c1 = refl
  holds8512 m13c1 m13c2 m13c3 m13c2 = refl
  holds8512 m13c1 m13c2 m13c3 m13c3 = refl
  holds8512 m13c1 m13c3 m13c0 m13c0 = refl
  holds8512 m13c1 m13c3 m13c0 m13c1 = refl
  holds8512 m13c1 m13c3 m13c0 m13c2 = refl
  holds8512 m13c1 m13c3 m13c0 m13c3 = refl
  holds8512 m13c1 m13c3 m13c1 m13c0 = refl
  holds8512 m13c1 m13c3 m13c1 m13c1 = refl
  holds8512 m13c1 m13c3 m13c1 m13c2 = refl
  holds8512 m13c1 m13c3 m13c1 m13c3 = refl
  holds8512 m13c1 m13c3 m13c2 m13c0 = refl
  holds8512 m13c1 m13c3 m13c2 m13c1 = refl
  holds8512 m13c1 m13c3 m13c2 m13c2 = refl
  holds8512 m13c1 m13c3 m13c2 m13c3 = refl
  holds8512 m13c1 m13c3 m13c3 m13c0 = refl
  holds8512 m13c1 m13c3 m13c3 m13c1 = refl
  holds8512 m13c1 m13c3 m13c3 m13c2 = refl
  holds8512 m13c1 m13c3 m13c3 m13c3 = refl
  holds8512 m13c2 m13c0 m13c0 m13c0 = refl
  holds8512 m13c2 m13c0 m13c0 m13c1 = refl
  holds8512 m13c2 m13c0 m13c0 m13c2 = refl
  holds8512 m13c2 m13c0 m13c0 m13c3 = refl
  holds8512 m13c2 m13c0 m13c1 m13c0 = refl
  holds8512 m13c2 m13c0 m13c1 m13c1 = refl
  holds8512 m13c2 m13c0 m13c1 m13c2 = refl
  holds8512 m13c2 m13c0 m13c1 m13c3 = refl
  holds8512 m13c2 m13c0 m13c2 m13c0 = refl
  holds8512 m13c2 m13c0 m13c2 m13c1 = refl
  holds8512 m13c2 m13c0 m13c2 m13c2 = refl
  holds8512 m13c2 m13c0 m13c2 m13c3 = refl
  holds8512 m13c2 m13c0 m13c3 m13c0 = refl
  holds8512 m13c2 m13c0 m13c3 m13c1 = refl
  holds8512 m13c2 m13c0 m13c3 m13c2 = refl
  holds8512 m13c2 m13c0 m13c3 m13c3 = refl
  holds8512 m13c2 m13c1 m13c0 m13c0 = refl
  holds8512 m13c2 m13c1 m13c0 m13c1 = refl
  holds8512 m13c2 m13c1 m13c0 m13c2 = refl
  holds8512 m13c2 m13c1 m13c0 m13c3 = refl
  holds8512 m13c2 m13c1 m13c1 m13c0 = refl
  holds8512 m13c2 m13c1 m13c1 m13c1 = refl
  holds8512 m13c2 m13c1 m13c1 m13c2 = refl
  holds8512 m13c2 m13c1 m13c1 m13c3 = refl
  holds8512 m13c2 m13c1 m13c2 m13c0 = refl
  holds8512 m13c2 m13c1 m13c2 m13c1 = refl
  holds8512 m13c2 m13c1 m13c2 m13c2 = refl
  holds8512 m13c2 m13c1 m13c2 m13c3 = refl
  holds8512 m13c2 m13c1 m13c3 m13c0 = refl
  holds8512 m13c2 m13c1 m13c3 m13c1 = refl
  holds8512 m13c2 m13c1 m13c3 m13c2 = refl
  holds8512 m13c2 m13c1 m13c3 m13c3 = refl
  holds8512 m13c2 m13c2 m13c0 m13c0 = refl
  holds8512 m13c2 m13c2 m13c0 m13c1 = refl
  holds8512 m13c2 m13c2 m13c0 m13c2 = refl
  holds8512 m13c2 m13c2 m13c0 m13c3 = refl
  holds8512 m13c2 m13c2 m13c1 m13c0 = refl
  holds8512 m13c2 m13c2 m13c1 m13c1 = refl
  holds8512 m13c2 m13c2 m13c1 m13c2 = refl
  holds8512 m13c2 m13c2 m13c1 m13c3 = refl
  holds8512 m13c2 m13c2 m13c2 m13c0 = refl
  holds8512 m13c2 m13c2 m13c2 m13c1 = refl
  holds8512 m13c2 m13c2 m13c2 m13c2 = refl
  holds8512 m13c2 m13c2 m13c2 m13c3 = refl
  holds8512 m13c2 m13c2 m13c3 m13c0 = refl
  holds8512 m13c2 m13c2 m13c3 m13c1 = refl
  holds8512 m13c2 m13c2 m13c3 m13c2 = refl
  holds8512 m13c2 m13c2 m13c3 m13c3 = refl
  holds8512 m13c2 m13c3 m13c0 m13c0 = refl
  holds8512 m13c2 m13c3 m13c0 m13c1 = refl
  holds8512 m13c2 m13c3 m13c0 m13c2 = refl
  holds8512 m13c2 m13c3 m13c0 m13c3 = refl
  holds8512 m13c2 m13c3 m13c1 m13c0 = refl
  holds8512 m13c2 m13c3 m13c1 m13c1 = refl
  holds8512 m13c2 m13c3 m13c1 m13c2 = refl
  holds8512 m13c2 m13c3 m13c1 m13c3 = refl
  holds8512 m13c2 m13c3 m13c2 m13c0 = refl
  holds8512 m13c2 m13c3 m13c2 m13c1 = refl
  holds8512 m13c2 m13c3 m13c2 m13c2 = refl
  holds8512 m13c2 m13c3 m13c2 m13c3 = refl
  holds8512 m13c2 m13c3 m13c3 m13c0 = refl
  holds8512 m13c2 m13c3 m13c3 m13c1 = refl
  holds8512 m13c2 m13c3 m13c3 m13c2 = refl
  holds8512 m13c2 m13c3 m13c3 m13c3 = refl
  holds8512 m13c3 m13c0 m13c0 m13c0 = refl
  holds8512 m13c3 m13c0 m13c0 m13c1 = refl
  holds8512 m13c3 m13c0 m13c0 m13c2 = refl
  holds8512 m13c3 m13c0 m13c0 m13c3 = refl
  holds8512 m13c3 m13c0 m13c1 m13c0 = refl
  holds8512 m13c3 m13c0 m13c1 m13c1 = refl
  holds8512 m13c3 m13c0 m13c1 m13c2 = refl
  holds8512 m13c3 m13c0 m13c1 m13c3 = refl
  holds8512 m13c3 m13c0 m13c2 m13c0 = refl
  holds8512 m13c3 m13c0 m13c2 m13c1 = refl
  holds8512 m13c3 m13c0 m13c2 m13c2 = refl
  holds8512 m13c3 m13c0 m13c2 m13c3 = refl
  holds8512 m13c3 m13c0 m13c3 m13c0 = refl
  holds8512 m13c3 m13c0 m13c3 m13c1 = refl
  holds8512 m13c3 m13c0 m13c3 m13c2 = refl
  holds8512 m13c3 m13c0 m13c3 m13c3 = refl
  holds8512 m13c3 m13c1 m13c0 m13c0 = refl
  holds8512 m13c3 m13c1 m13c0 m13c1 = refl
  holds8512 m13c3 m13c1 m13c0 m13c2 = refl
  holds8512 m13c3 m13c1 m13c0 m13c3 = refl
  holds8512 m13c3 m13c1 m13c1 m13c0 = refl
  holds8512 m13c3 m13c1 m13c1 m13c1 = refl
  holds8512 m13c3 m13c1 m13c1 m13c2 = refl
  holds8512 m13c3 m13c1 m13c1 m13c3 = refl
  holds8512 m13c3 m13c1 m13c2 m13c0 = refl
  holds8512 m13c3 m13c1 m13c2 m13c1 = refl
  holds8512 m13c3 m13c1 m13c2 m13c2 = refl
  holds8512 m13c3 m13c1 m13c2 m13c3 = refl
  holds8512 m13c3 m13c1 m13c3 m13c0 = refl
  holds8512 m13c3 m13c1 m13c3 m13c1 = refl
  holds8512 m13c3 m13c1 m13c3 m13c2 = refl
  holds8512 m13c3 m13c1 m13c3 m13c3 = refl
  holds8512 m13c3 m13c2 m13c0 m13c0 = refl
  holds8512 m13c3 m13c2 m13c0 m13c1 = refl
  holds8512 m13c3 m13c2 m13c0 m13c2 = refl
  holds8512 m13c3 m13c2 m13c0 m13c3 = refl
  holds8512 m13c3 m13c2 m13c1 m13c0 = refl
  holds8512 m13c3 m13c2 m13c1 m13c1 = refl
  holds8512 m13c3 m13c2 m13c1 m13c2 = refl
  holds8512 m13c3 m13c2 m13c1 m13c3 = refl
  holds8512 m13c3 m13c2 m13c2 m13c0 = refl
  holds8512 m13c3 m13c2 m13c2 m13c1 = refl
  holds8512 m13c3 m13c2 m13c2 m13c2 = refl
  holds8512 m13c3 m13c2 m13c2 m13c3 = refl
  holds8512 m13c3 m13c2 m13c3 m13c0 = refl
  holds8512 m13c3 m13c2 m13c3 m13c1 = refl
  holds8512 m13c3 m13c2 m13c3 m13c2 = refl
  holds8512 m13c3 m13c2 m13c3 m13c3 = refl
  holds8512 m13c3 m13c3 m13c0 m13c0 = refl
  holds8512 m13c3 m13c3 m13c0 m13c1 = refl
  holds8512 m13c3 m13c3 m13c0 m13c2 = refl
  holds8512 m13c3 m13c3 m13c0 m13c3 = refl
  holds8512 m13c3 m13c3 m13c1 m13c0 = refl
  holds8512 m13c3 m13c3 m13c1 m13c1 = refl
  holds8512 m13c3 m13c3 m13c1 m13c2 = refl
  holds8512 m13c3 m13c3 m13c1 m13c3 = refl
  holds8512 m13c3 m13c3 m13c2 m13c0 = refl
  holds8512 m13c3 m13c3 m13c2 m13c1 = refl
  holds8512 m13c3 m13c3 m13c2 m13c2 = refl
  holds8512 m13c3 m13c3 m13c2 m13c3 = refl
  holds8512 m13c3 m13c3 m13c3 m13c0 = refl
  holds8512 m13c3 m13c3 m13c3 m13c1 = refl
  holds8512 m13c3 m13c3 m13c3 m13c2 = refl
  holds8512 m13c3 m13c3 m13c3 m13c3 = refl
  cut8512 : Adequate {ℓ} ((op (op (op (op (var 0) (var 1)) (var 2)) (var 3)) (op (var 3) (var 2))) , (var 3)) → ⊥
  cut8512  = reject13 ((op (op (op (op (var 0) (var 1)) (var 2)) (var 3)) (op (var 3) (var 2))) , (var 3)) (λ env → holds8512 (env 0) (env 1) (env 2) (env 3))
  bad8513 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b0) b0) b0) (bop b0 b0)) b1 → ⊥
  bad8513  p = false≢true (cong lower p)
  cut8513 : Adequate {ℓ} ((op (op (op (op (var 0) (var 1)) (var 2)) (var 3)) (op (var 3) (var 2))) , (var 4)) → ⊥
  cut8513  adequate = bad8513  (Adequate.valid adequate Two boolean env9)
  bad8514 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b0) b0) b1) (bop b1 b1)) b0 → ⊥
  bad8514  p = false≢true (sym (cong lower p))
  cut8514 : Adequate {ℓ} ((op (op (op (op (var 0) (var 1)) (var 2)) (var 3)) (op (var 3) (var 3))) , (var 0)) → ⊥
  cut8514  adequate = bad8514  (Adequate.valid adequate Two boolean env5)
  bad8515 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b0) b0) b1) (bop b1 b1)) b0 → ⊥
  bad8515  p = false≢true (sym (cong lower p))
  cut8515 : Adequate {ℓ} ((op (op (op (op (var 0) (var 1)) (var 2)) (var 3)) (op (var 3) (var 3))) , (var 1)) → ⊥
  cut8515  adequate = bad8515  (Adequate.valid adequate Two boolean env5)
  bad8516 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b0) b0) b1) (bop b1 b1)) b0 → ⊥
  bad8516  p = false≢true (sym (cong lower p))
  cut8516 : Adequate {ℓ} ((op (op (op (op (var 0) (var 1)) (var 2)) (var 3)) (op (var 3) (var 3))) , (var 2)) → ⊥
  cut8516  adequate = bad8516  (Adequate.valid adequate Two boolean env5)
  holds8517 : (z0 z1 z2 z3 : A3) → (mul3 (mul3 (mul3 (mul3 z0 z1) z2) z3) (mul3 z3 z3)) ≡ z3
  holds8517 z0 z1 z2 z3 = refl
  cut8517 : Adequate {ℓ} ((op (op (op (op (var 0) (var 1)) (var 2)) (var 3)) (op (var 3) (var 3))) , (var 3)) → ⊥
  cut8517  = reject3 ((op (op (op (op (var 0) (var 1)) (var 2)) (var 3)) (op (var 3) (var 3))) , (var 3)) (λ env → holds8517 (env 0) (env 1) (env 2) (env 3))
  bad8518 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b0) b0) b0) (bop b0 b0)) b1 → ⊥
  bad8518  p = false≢true (cong lower p)
  cut8518 : Adequate {ℓ} ((op (op (op (op (var 0) (var 1)) (var 2)) (var 3)) (op (var 3) (var 3))) , (var 4)) → ⊥
  cut8518  adequate = bad8518  (Adequate.valid adequate Two boolean env9)
  bad8519 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b0) b0) b1) (bop b1 b0)) b0 → ⊥
  bad8519  p = false≢true (sym (cong lower p))
  cut8519 : Adequate {ℓ} ((op (op (op (op (var 0) (var 1)) (var 2)) (var 3)) (op (var 3) (var 4))) , (var 0)) → ⊥
  cut8519  adequate = bad8519  (Adequate.valid adequate Two boolean env15)
  bad8520 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b0) b0) b1) (bop b1 b0)) b0 → ⊥
  bad8520  p = false≢true (sym (cong lower p))
  cut8520 : Adequate {ℓ} ((op (op (op (op (var 0) (var 1)) (var 2)) (var 3)) (op (var 3) (var 4))) , (var 1)) → ⊥
  cut8520  adequate = bad8520  (Adequate.valid adequate Two boolean env15)
  bad8521 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b0) b0) b1) (bop b1 b0)) b0 → ⊥
  bad8521  p = false≢true (sym (cong lower p))
  cut8521 : Adequate {ℓ} ((op (op (op (op (var 0) (var 1)) (var 2)) (var 3)) (op (var 3) (var 4))) , (var 2)) → ⊥
  cut8521  adequate = bad8521  (Adequate.valid adequate Two boolean env15)
  bad8522 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b0) b1) b1) (bop b1 b0)) b1 → ⊥
  bad8522  p = false≢true (cong lower p)
  cut8522 : Adequate {ℓ} ((op (op (op (op (var 0) (var 1)) (var 2)) (var 3)) (op (var 3) (var 4))) , (var 3)) → ⊥
  cut8522  adequate = bad8522  (Adequate.valid adequate Two boolean env22)
  bad8523 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b0) b0) b0) (bop b0 b1)) b1 → ⊥
  bad8523  p = false≢true (cong lower p)
  cut8523 : Adequate {ℓ} ((op (op (op (op (var 0) (var 1)) (var 2)) (var 3)) (op (var 3) (var 4))) , (var 4)) → ⊥
  cut8523  adequate = bad8523  (Adequate.valid adequate Two boolean env9)
  bad8524 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b0) b0) b0) (bop b0 b0)) b1 → ⊥
  bad8524  p = false≢true (cong lower p)
  cut8524 : Adequate {ℓ} ((op (op (op (op (var 0) (var 1)) (var 2)) (var 3)) (op (var 3) (var 4))) , (var 5)) → ⊥
  cut8524  adequate = bad8524  (Adequate.valid adequate Two boolean env16)
  bad8525 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b0) b0) b1) (bop b0 b0)) b0 → ⊥
  bad8525  p = false≢true (sym (cong lower p))
  cut8525 : Adequate {ℓ} ((op (op (op (op (var 0) (var 1)) (var 2)) (var 3)) (op (var 4) (var 0))) , (var 0)) → ⊥
  cut8525  adequate = bad8525  (Adequate.valid adequate Two boolean env15)
  bad8526 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b0) b0) b1) (bop b0 b0)) b0 → ⊥
  bad8526  p = false≢true (sym (cong lower p))
  cut8526 : Adequate {ℓ} ((op (op (op (op (var 0) (var 1)) (var 2)) (var 3)) (op (var 4) (var 0))) , (var 1)) → ⊥
  cut8526  adequate = bad8526  (Adequate.valid adequate Two boolean env15)
  bad8527 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b0) b0) b1) (bop b0 b0)) b0 → ⊥
  bad8527  p = false≢true (sym (cong lower p))
  cut8527 : Adequate {ℓ} ((op (op (op (op (var 0) (var 1)) (var 2)) (var 3)) (op (var 4) (var 0))) , (var 2)) → ⊥
  cut8527  adequate = bad8527  (Adequate.valid adequate Two boolean env15)
  bad8528 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b0) b1) b1) (bop b0 b0)) b1 → ⊥
  bad8528  p = false≢true (cong lower p)
  cut8528 : Adequate {ℓ} ((op (op (op (op (var 0) (var 1)) (var 2)) (var 3)) (op (var 4) (var 0))) , (var 3)) → ⊥
  cut8528  adequate = bad8528  (Adequate.valid adequate Two boolean env22)
  bad8529 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b0) b0) b0) (bop b1 b0)) b1 → ⊥
  bad8529  p = false≢true (cong lower p)
  cut8529 : Adequate {ℓ} ((op (op (op (op (var 0) (var 1)) (var 2)) (var 3)) (op (var 4) (var 0))) , (var 4)) → ⊥
  cut8529  adequate = bad8529  (Adequate.valid adequate Two boolean env9)
  bad8530 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b0) b0) b0) (bop b0 b0)) b1 → ⊥
  bad8530  p = false≢true (cong lower p)
  cut8530 : Adequate {ℓ} ((op (op (op (op (var 0) (var 1)) (var 2)) (var 3)) (op (var 4) (var 0))) , (var 5)) → ⊥
  cut8530  adequate = bad8530  (Adequate.valid adequate Two boolean env16)
  bad8531 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b0) b0) b1) (bop b0 b0)) b0 → ⊥
  bad8531  p = false≢true (sym (cong lower p))
  cut8531 : Adequate {ℓ} ((op (op (op (op (var 0) (var 1)) (var 2)) (var 3)) (op (var 4) (var 1))) , (var 0)) → ⊥
  cut8531  adequate = bad8531  (Adequate.valid adequate Two boolean env15)
  bad8532 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b0) b0) b1) (bop b0 b0)) b0 → ⊥
  bad8532  p = false≢true (sym (cong lower p))
  cut8532 : Adequate {ℓ} ((op (op (op (op (var 0) (var 1)) (var 2)) (var 3)) (op (var 4) (var 1))) , (var 1)) → ⊥
  cut8532  adequate = bad8532  (Adequate.valid adequate Two boolean env15)
  bad8533 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b0) b0) b1) (bop b0 b0)) b0 → ⊥
  bad8533  p = false≢true (sym (cong lower p))
  cut8533 : Adequate {ℓ} ((op (op (op (op (var 0) (var 1)) (var 2)) (var 3)) (op (var 4) (var 1))) , (var 2)) → ⊥
  cut8533  adequate = bad8533  (Adequate.valid adequate Two boolean env15)
  bad8534 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b0) b1) b1) (bop b0 b0)) b1 → ⊥
  bad8534  p = false≢true (cong lower p)
  cut8534 : Adequate {ℓ} ((op (op (op (op (var 0) (var 1)) (var 2)) (var 3)) (op (var 4) (var 1))) , (var 3)) → ⊥
  cut8534  adequate = bad8534  (Adequate.valid adequate Two boolean env22)
  bad8535 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b0) b0) b0) (bop b1 b0)) b1 → ⊥
  bad8535  p = false≢true (cong lower p)
  cut8535 : Adequate {ℓ} ((op (op (op (op (var 0) (var 1)) (var 2)) (var 3)) (op (var 4) (var 1))) , (var 4)) → ⊥
  cut8535  adequate = bad8535  (Adequate.valid adequate Two boolean env9)
  bad8536 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b0) b0) b0) (bop b0 b0)) b1 → ⊥
  bad8536  p = false≢true (cong lower p)
  cut8536 : Adequate {ℓ} ((op (op (op (op (var 0) (var 1)) (var 2)) (var 3)) (op (var 4) (var 1))) , (var 5)) → ⊥
  cut8536  adequate = bad8536  (Adequate.valid adequate Two boolean env16)
  bad8537 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b0) b0) b1) (bop b0 b0)) b0 → ⊥
  bad8537  p = false≢true (sym (cong lower p))
  cut8537 : Adequate {ℓ} ((op (op (op (op (var 0) (var 1)) (var 2)) (var 3)) (op (var 4) (var 2))) , (var 0)) → ⊥
  cut8537  adequate = bad8537  (Adequate.valid adequate Two boolean env15)
  bad8538 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b0) b0) b1) (bop b0 b0)) b0 → ⊥
  bad8538  p = false≢true (sym (cong lower p))
  cut8538 : Adequate {ℓ} ((op (op (op (op (var 0) (var 1)) (var 2)) (var 3)) (op (var 4) (var 2))) , (var 1)) → ⊥
  cut8538  adequate = bad8538  (Adequate.valid adequate Two boolean env15)
  bad8539 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b0) b0) b1) (bop b0 b0)) b0 → ⊥
  bad8539  p = false≢true (sym (cong lower p))
  cut8539 : Adequate {ℓ} ((op (op (op (op (var 0) (var 1)) (var 2)) (var 3)) (op (var 4) (var 2))) , (var 2)) → ⊥
  cut8539  adequate = bad8539  (Adequate.valid adequate Two boolean env15)
  bad8540 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b0) b1) b0) (bop b1 b1)) b0 → ⊥
  bad8540  p = false≢true (sym (cong lower p))
  cut8540 : Adequate {ℓ} ((op (op (op (op (var 0) (var 1)) (var 2)) (var 3)) (op (var 4) (var 2))) , (var 3)) → ⊥
  cut8540  adequate = bad8540  (Adequate.valid adequate Two boolean env23)
  bad8541 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b0) b0) b0) (bop b1 b0)) b1 → ⊥
  bad8541  p = false≢true (cong lower p)
  cut8541 : Adequate {ℓ} ((op (op (op (op (var 0) (var 1)) (var 2)) (var 3)) (op (var 4) (var 2))) , (var 4)) → ⊥
  cut8541  adequate = bad8541  (Adequate.valid adequate Two boolean env9)
  bad8542 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b0) b0) b0) (bop b0 b0)) b1 → ⊥
  bad8542  p = false≢true (cong lower p)
  cut8542 : Adequate {ℓ} ((op (op (op (op (var 0) (var 1)) (var 2)) (var 3)) (op (var 4) (var 2))) , (var 5)) → ⊥
  cut8542  adequate = bad8542  (Adequate.valid adequate Two boolean env16)
  bad8543 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b0) b0) b1) (bop b0 b1)) b0 → ⊥
  bad8543  p = false≢true (sym (cong lower p))
  cut8543 : Adequate {ℓ} ((op (op (op (op (var 0) (var 1)) (var 2)) (var 3)) (op (var 4) (var 3))) , (var 0)) → ⊥
  cut8543  adequate = bad8543  (Adequate.valid adequate Two boolean env15)
  bad8544 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b0) b0) b1) (bop b0 b1)) b0 → ⊥
  bad8544  p = false≢true (sym (cong lower p))
  cut8544 : Adequate {ℓ} ((op (op (op (op (var 0) (var 1)) (var 2)) (var 3)) (op (var 4) (var 3))) , (var 1)) → ⊥
  cut8544  adequate = bad8544  (Adequate.valid adequate Two boolean env15)
  bad8545 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b0) b0) b1) (bop b0 b1)) b0 → ⊥
  bad8545  p = false≢true (sym (cong lower p))
  cut8545 : Adequate {ℓ} ((op (op (op (op (var 0) (var 1)) (var 2)) (var 3)) (op (var 4) (var 3))) , (var 2)) → ⊥
  cut8545  adequate = bad8545  (Adequate.valid adequate Two boolean env15)
  bad8546 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b0) b1) b1) (bop b0 b1)) b1 → ⊥
  bad8546  p = false≢true (cong lower p)
  cut8546 : Adequate {ℓ} ((op (op (op (op (var 0) (var 1)) (var 2)) (var 3)) (op (var 4) (var 3))) , (var 3)) → ⊥
  cut8546  adequate = bad8546  (Adequate.valid adequate Two boolean env22)
  bad8547 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b0) b0) b0) (bop b1 b0)) b1 → ⊥
  bad8547  p = false≢true (cong lower p)
  cut8547 : Adequate {ℓ} ((op (op (op (op (var 0) (var 1)) (var 2)) (var 3)) (op (var 4) (var 3))) , (var 4)) → ⊥
  cut8547  adequate = bad8547  (Adequate.valid adequate Two boolean env9)
  bad8548 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b0) b0) b0) (bop b0 b0)) b1 → ⊥
  bad8548  p = false≢true (cong lower p)
  cut8548 : Adequate {ℓ} ((op (op (op (op (var 0) (var 1)) (var 2)) (var 3)) (op (var 4) (var 3))) , (var 5)) → ⊥
  cut8548  adequate = bad8548  (Adequate.valid adequate Two boolean env16)
  bad8549 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b0) b0) b0) (bop b1 b1)) b0 → ⊥
  bad8549  p = false≢true (sym (cong lower p))
  cut8549 : Adequate {ℓ} ((op (op (op (op (var 0) (var 1)) (var 2)) (var 3)) (op (var 4) (var 4))) , (var 0)) → ⊥
  cut8549  adequate = bad8549  (Adequate.valid adequate Two boolean env9)
  bad8550 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b0) b0) b0) (bop b1 b1)) b0 → ⊥
  bad8550  p = false≢true (sym (cong lower p))
  cut8550 : Adequate {ℓ} ((op (op (op (op (var 0) (var 1)) (var 2)) (var 3)) (op (var 4) (var 4))) , (var 1)) → ⊥
  cut8550  adequate = bad8550  (Adequate.valid adequate Two boolean env9)
  bad8551 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b0) b0) b0) (bop b1 b1)) b0 → ⊥
  bad8551  p = false≢true (sym (cong lower p))
  cut8551 : Adequate {ℓ} ((op (op (op (op (var 0) (var 1)) (var 2)) (var 3)) (op (var 4) (var 4))) , (var 2)) → ⊥
  cut8551  adequate = bad8551  (Adequate.valid adequate Two boolean env9)
  bad8552 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b0) b0) b0) (bop b1 b1)) b0 → ⊥
  bad8552  p = false≢true (sym (cong lower p))
  cut8552 : Adequate {ℓ} ((op (op (op (op (var 0) (var 1)) (var 2)) (var 3)) (op (var 4) (var 4))) , (var 3)) → ⊥
  cut8552  adequate = bad8552  (Adequate.valid adequate Two boolean env9)
  bad8553 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b0) b0) b1) (bop b0 b0)) b0 → ⊥
  bad8553  p = false≢true (sym (cong lower p))
  cut8553 : Adequate {ℓ} ((op (op (op (op (var 0) (var 1)) (var 2)) (var 3)) (op (var 4) (var 4))) , (var 4)) → ⊥
  cut8553  adequate = bad8553  (Adequate.valid adequate Two boolean env15)
  bad8554 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b0) b0) b0) (bop b0 b0)) b1 → ⊥
  bad8554  p = false≢true (cong lower p)
  cut8554 : Adequate {ℓ} ((op (op (op (op (var 0) (var 1)) (var 2)) (var 3)) (op (var 4) (var 4))) , (var 5)) → ⊥
  cut8554  adequate = bad8554  (Adequate.valid adequate Two boolean env16)
  env24 : ℕ → Two
  env24 zero = b0
  env24 (suc zero) = b0
  env24 (suc (suc zero)) = b0
  env24 (suc (suc (suc zero))) = b0
  env24 (suc (suc (suc (suc zero)))) = b1
  env24 (suc (suc (suc (suc (suc zero))))) = b1
  env24 (suc (suc (suc (suc (suc (suc rest)))))) = b0
  bad8555 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b0) b0) b0) (bop b1 b1)) b0 → ⊥
  bad8555  p = false≢true (sym (cong lower p))
  cut8555 : Adequate {ℓ} ((op (op (op (op (var 0) (var 1)) (var 2)) (var 3)) (op (var 4) (var 5))) , (var 0)) → ⊥
  cut8555  adequate = bad8555  (Adequate.valid adequate Two boolean env24)
  bad8556 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b0) b0) b0) (bop b1 b1)) b0 → ⊥
  bad8556  p = false≢true (sym (cong lower p))
  cut8556 : Adequate {ℓ} ((op (op (op (op (var 0) (var 1)) (var 2)) (var 3)) (op (var 4) (var 5))) , (var 1)) → ⊥
  cut8556  adequate = bad8556  (Adequate.valid adequate Two boolean env24)
  bad8557 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b0) b0) b0) (bop b1 b1)) b0 → ⊥
  bad8557  p = false≢true (sym (cong lower p))
  cut8557 : Adequate {ℓ} ((op (op (op (op (var 0) (var 1)) (var 2)) (var 3)) (op (var 4) (var 5))) , (var 2)) → ⊥
  cut8557  adequate = bad8557  (Adequate.valid adequate Two boolean env24)
  bad8558 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b0) b0) b0) (bop b1 b1)) b0 → ⊥
  bad8558  p = false≢true (sym (cong lower p))
  cut8558 : Adequate {ℓ} ((op (op (op (op (var 0) (var 1)) (var 2)) (var 3)) (op (var 4) (var 5))) , (var 3)) → ⊥
  cut8558  adequate = bad8558  (Adequate.valid adequate Two boolean env24)
  env25 : ℕ → Two
  env25 zero = b0
  env25 (suc zero) = b0
  env25 (suc (suc zero)) = b0
  env25 (suc (suc (suc zero))) = b0
  env25 (suc (suc (suc (suc zero)))) = b1
  env25 (suc (suc (suc (suc (suc zero))))) = b0
  env25 (suc (suc (suc (suc (suc (suc rest)))))) = b0
  bad8559 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b0) b0) b0) (bop b1 b0)) b1 → ⊥
  bad8559  p = false≢true (cong lower p)
  cut8559 : Adequate {ℓ} ((op (op (op (op (var 0) (var 1)) (var 2)) (var 3)) (op (var 4) (var 5))) , (var 4)) → ⊥
  cut8559  adequate = bad8559  (Adequate.valid adequate Two boolean env25)
  bad8560 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b0) b0) b0) (bop b0 b1)) b1 → ⊥
  bad8560  p = false≢true (cong lower p)
  cut8560 : Adequate {ℓ} ((op (op (op (op (var 0) (var 1)) (var 2)) (var 3)) (op (var 4) (var 5))) , (var 5)) → ⊥
  cut8560  adequate = bad8560  (Adequate.valid adequate Two boolean env16)
  env26 : ℕ → Two
  env26 zero = b0
  env26 (suc zero) = b0
  env26 (suc (suc zero)) = b0
  env26 (suc (suc (suc zero))) = b0
  env26 (suc (suc (suc (suc zero)))) = b0
  env26 (suc (suc (suc (suc (suc zero))))) = b0
  env26 (suc (suc (suc (suc (suc (suc zero)))))) = b1
  env26 (suc (suc (suc (suc (suc (suc (suc rest))))))) = b0
  bad8561 : PathP (λ _ → Two) (bop (bop (bop (bop b0 b0) b0) b0) (bop b0 b0)) b1 → ⊥
  bad8561  p = false≢true (cong lower p)
  cut8561 : Adequate {ℓ} ((op (op (op (op (var 0) (var 1)) (var 2)) (var 3)) (op (var 4) (var 5))) , (var 6)) → ⊥
  cut8561  adequate = bad8561  (Adequate.valid adequate Two boolean env26)
