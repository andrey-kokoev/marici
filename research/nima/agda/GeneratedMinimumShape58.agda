{-# OPTIONS --safe --cubical --guardedness #-}
module GeneratedMinimumShape58 where
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
  holds790 : (z0 : A1) → (mul1 (mul1 (mul1 z0 z0) z0) (mul1 z0 z0)) ≡ z0
  holds790 m1c0 = refl
  holds790 m1c1 = refl
  cut790 : Adequate {ℓ} ((op (op (op (var 0) (var 0)) (var 0)) (op (var 0) (var 0))) , (var 0)) → ⊥
  cut790  = reject1 ((op (op (op (var 0) (var 0)) (var 0)) (op (var 0) (var 0))) , (var 0)) (λ env → holds790 (env 0))
  env0 : ℕ → Two
  env0 zero = b0
  env0 (suc zero) = b1
  env0 (suc (suc rest)) = b0
  bad791 : PathP (λ _ → Two) (bop (bop (bop b0 b0) b0) (bop b0 b0)) b1 → ⊥
  bad791  p = false≢true (cong lower p)
  cut791 : Adequate {ℓ} ((op (op (op (var 0) (var 0)) (var 0)) (op (var 0) (var 0))) , (var 1)) → ⊥
  cut791  adequate = bad791  (Adequate.valid adequate Two boolean env0)
  env1 : ℕ → Two
  env1 zero = b1
  env1 (suc zero) = b0
  env1 (suc (suc rest)) = b0
  bad792 : PathP (λ _ → Two) (bop (bop (bop b1 b1) b1) (bop b1 b0)) b1 → ⊥
  bad792  p = false≢true (cong lower p)
  cut792 : Adequate {ℓ} ((op (op (op (var 0) (var 0)) (var 0)) (op (var 0) (var 1))) , (var 0)) → ⊥
  cut792  adequate = bad792  (Adequate.valid adequate Two boolean env1)
  bad793 : PathP (λ _ → Two) (bop (bop (bop b0 b0) b0) (bop b0 b1)) b1 → ⊥
  bad793  p = false≢true (cong lower p)
  cut793 : Adequate {ℓ} ((op (op (op (var 0) (var 0)) (var 0)) (op (var 0) (var 1))) , (var 1)) → ⊥
  cut793  adequate = bad793  (Adequate.valid adequate Two boolean env0)
  env2 : ℕ → Two
  env2 zero = b0
  env2 (suc zero) = b0
  env2 (suc (suc zero)) = b1
  env2 (suc (suc (suc rest))) = b0
  bad794 : PathP (λ _ → Two) (bop (bop (bop b0 b0) b0) (bop b0 b0)) b1 → ⊥
  bad794  p = false≢true (cong lower p)
  cut794 : Adequate {ℓ} ((op (op (op (var 0) (var 0)) (var 0)) (op (var 0) (var 1))) , (var 2)) → ⊥
  cut794  adequate = bad794  (Adequate.valid adequate Two boolean env2)
  bad795 : PathP (λ _ → Two) (bop (bop (bop b1 b1) b1) (bop b0 b1)) b1 → ⊥
  bad795  p = false≢true (cong lower p)
  cut795 : Adequate {ℓ} ((op (op (op (var 0) (var 0)) (var 0)) (op (var 1) (var 0))) , (var 0)) → ⊥
  cut795  adequate = bad795  (Adequate.valid adequate Two boolean env1)
  bad796 : PathP (λ _ → Two) (bop (bop (bop b0 b0) b0) (bop b1 b0)) b1 → ⊥
  bad796  p = false≢true (cong lower p)
  cut796 : Adequate {ℓ} ((op (op (op (var 0) (var 0)) (var 0)) (op (var 1) (var 0))) , (var 1)) → ⊥
  cut796  adequate = bad796  (Adequate.valid adequate Two boolean env0)
  bad797 : PathP (λ _ → Two) (bop (bop (bop b0 b0) b0) (bop b0 b0)) b1 → ⊥
  bad797  p = false≢true (cong lower p)
  cut797 : Adequate {ℓ} ((op (op (op (var 0) (var 0)) (var 0)) (op (var 1) (var 0))) , (var 2)) → ⊥
  cut797  adequate = bad797  (Adequate.valid adequate Two boolean env2)
  bad798 : PathP (λ _ → Two) (bop (bop (bop b0 b0) b0) (bop b1 b1)) b0 → ⊥
  bad798  p = false≢true (sym (cong lower p))
  cut798 : Adequate {ℓ} ((op (op (op (var 0) (var 0)) (var 0)) (op (var 1) (var 1))) , (var 0)) → ⊥
  cut798  adequate = bad798  (Adequate.valid adequate Two boolean env0)
  holds799 : (z0 z1 : A3) → (mul3 (mul3 (mul3 z0 z0) z0) (mul3 z1 z1)) ≡ z1
  holds799 z0 z1 = refl
  cut799 : Adequate {ℓ} ((op (op (op (var 0) (var 0)) (var 0)) (op (var 1) (var 1))) , (var 1)) → ⊥
  cut799  = reject3 ((op (op (op (var 0) (var 0)) (var 0)) (op (var 1) (var 1))) , (var 1)) (λ env → holds799 (env 0) (env 1))
  bad800 : PathP (λ _ → Two) (bop (bop (bop b0 b0) b0) (bop b0 b0)) b1 → ⊥
  bad800  p = false≢true (cong lower p)
  cut800 : Adequate {ℓ} ((op (op (op (var 0) (var 0)) (var 0)) (op (var 1) (var 1))) , (var 2)) → ⊥
  cut800  adequate = bad800  (Adequate.valid adequate Two boolean env2)
  env3 : ℕ → Two
  env3 zero = b0
  env3 (suc zero) = b1
  env3 (suc (suc zero)) = b1
  env3 (suc (suc (suc rest))) = b0
  bad801 : PathP (λ _ → Two) (bop (bop (bop b0 b0) b0) (bop b1 b1)) b0 → ⊥
  bad801  p = false≢true (sym (cong lower p))
  cut801 : Adequate {ℓ} ((op (op (op (var 0) (var 0)) (var 0)) (op (var 1) (var 2))) , (var 0)) → ⊥
  cut801  adequate = bad801  (Adequate.valid adequate Two boolean env3)
  env4 : ℕ → Two
  env4 zero = b0
  env4 (suc zero) = b1
  env4 (suc (suc zero)) = b0
  env4 (suc (suc (suc rest))) = b0
  bad802 : PathP (λ _ → Two) (bop (bop (bop b0 b0) b0) (bop b1 b0)) b1 → ⊥
  bad802  p = false≢true (cong lower p)
  cut802 : Adequate {ℓ} ((op (op (op (var 0) (var 0)) (var 0)) (op (var 1) (var 2))) , (var 1)) → ⊥
  cut802  adequate = bad802  (Adequate.valid adequate Two boolean env4)
  bad803 : PathP (λ _ → Two) (bop (bop (bop b0 b0) b0) (bop b0 b1)) b1 → ⊥
  bad803  p = false≢true (cong lower p)
  cut803 : Adequate {ℓ} ((op (op (op (var 0) (var 0)) (var 0)) (op (var 1) (var 2))) , (var 2)) → ⊥
  cut803  adequate = bad803  (Adequate.valid adequate Two boolean env2)
  env5 : ℕ → Two
  env5 zero = b0
  env5 (suc zero) = b0
  env5 (suc (suc zero)) = b0
  env5 (suc (suc (suc zero))) = b1
  env5 (suc (suc (suc (suc rest)))) = b0
  bad804 : PathP (λ _ → Two) (bop (bop (bop b0 b0) b0) (bop b0 b0)) b1 → ⊥
  bad804  p = false≢true (cong lower p)
  cut804 : Adequate {ℓ} ((op (op (op (var 0) (var 0)) (var 0)) (op (var 1) (var 2))) , (var 3)) → ⊥
  cut804  adequate = bad804  (Adequate.valid adequate Two boolean env5)
  bad805 : PathP (λ _ → Two) (bop (bop (bop b0 b0) b1) (bop b0 b0)) b0 → ⊥
  bad805  p = false≢true (sym (cong lower p))
  cut805 : Adequate {ℓ} ((op (op (op (var 0) (var 0)) (var 1)) (op (var 0) (var 0))) , (var 0)) → ⊥
  cut805  adequate = bad805  (Adequate.valid adequate Two boolean env0)
  bad806 : PathP (λ _ → Two) (bop (bop (bop b1 b1) b0) (bop b1 b1)) b0 → ⊥
  bad806  p = false≢true (sym (cong lower p))
  cut806 : Adequate {ℓ} ((op (op (op (var 0) (var 0)) (var 1)) (op (var 0) (var 0))) , (var 1)) → ⊥
  cut806  adequate = bad806  (Adequate.valid adequate Two boolean env1)
  bad807 : PathP (λ _ → Two) (bop (bop (bop b0 b0) b0) (bop b0 b0)) b1 → ⊥
  bad807  p = false≢true (cong lower p)
  cut807 : Adequate {ℓ} ((op (op (op (var 0) (var 0)) (var 1)) (op (var 0) (var 0))) , (var 2)) → ⊥
  cut807  adequate = bad807  (Adequate.valid adequate Two boolean env2)
  bad808 : PathP (λ _ → Two) (bop (bop (bop b0 b0) b1) (bop b0 b1)) b0 → ⊥
  bad808  p = false≢true (sym (cong lower p))
  cut808 : Adequate {ℓ} ((op (op (op (var 0) (var 0)) (var 1)) (op (var 0) (var 1))) , (var 0)) → ⊥
  cut808  adequate = bad808  (Adequate.valid adequate Two boolean env0)
  holds809 : (z0 z1 : A3) → (mul3 (mul3 (mul3 z0 z0) z1) (mul3 z0 z1)) ≡ z1
  holds809 z0 z1 = refl
  cut809 : Adequate {ℓ} ((op (op (op (var 0) (var 0)) (var 1)) (op (var 0) (var 1))) , (var 1)) → ⊥
  cut809  = reject3 ((op (op (op (var 0) (var 0)) (var 1)) (op (var 0) (var 1))) , (var 1)) (λ env → holds809 (env 0) (env 1))
  bad810 : PathP (λ _ → Two) (bop (bop (bop b0 b0) b0) (bop b0 b0)) b1 → ⊥
  bad810  p = false≢true (cong lower p)
  cut810 : Adequate {ℓ} ((op (op (op (var 0) (var 0)) (var 1)) (op (var 0) (var 1))) , (var 2)) → ⊥
  cut810  adequate = bad810  (Adequate.valid adequate Two boolean env2)
  bad811 : PathP (λ _ → Two) (bop (bop (bop b0 b0) b1) (bop b0 b0)) b0 → ⊥
  bad811  p = false≢true (sym (cong lower p))
  cut811 : Adequate {ℓ} ((op (op (op (var 0) (var 0)) (var 1)) (op (var 0) (var 2))) , (var 0)) → ⊥
  cut811  adequate = bad811  (Adequate.valid adequate Two boolean env4)
  env6 : ℕ → Two
  env6 zero = b1
  env6 (suc zero) = b0
  env6 (suc (suc zero)) = b1
  env6 (suc (suc (suc rest))) = b0
  bad812 : PathP (λ _ → Two) (bop (bop (bop b1 b1) b0) (bop b1 b1)) b0 → ⊥
  bad812  p = false≢true (sym (cong lower p))
  cut812 : Adequate {ℓ} ((op (op (op (var 0) (var 0)) (var 1)) (op (var 0) (var 2))) , (var 1)) → ⊥
  cut812  adequate = bad812  (Adequate.valid adequate Two boolean env6)
  bad813 : PathP (λ _ → Two) (bop (bop (bop b0 b0) b0) (bop b0 b1)) b1 → ⊥
  bad813  p = false≢true (cong lower p)
  cut813 : Adequate {ℓ} ((op (op (op (var 0) (var 0)) (var 1)) (op (var 0) (var 2))) , (var 2)) → ⊥
  cut813  adequate = bad813  (Adequate.valid adequate Two boolean env2)
  bad814 : PathP (λ _ → Two) (bop (bop (bop b0 b0) b0) (bop b0 b0)) b1 → ⊥
  bad814  p = false≢true (cong lower p)
  cut814 : Adequate {ℓ} ((op (op (op (var 0) (var 0)) (var 1)) (op (var 0) (var 2))) , (var 3)) → ⊥
  cut814  adequate = bad814  (Adequate.valid adequate Two boolean env5)
  bad815 : PathP (λ _ → Two) (bop (bop (bop b0 b0) b1) (bop b1 b0)) b0 → ⊥
  bad815  p = false≢true (sym (cong lower p))
  cut815 : Adequate {ℓ} ((op (op (op (var 0) (var 0)) (var 1)) (op (var 1) (var 0))) , (var 0)) → ⊥
  cut815  adequate = bad815  (Adequate.valid adequate Two boolean env0)
  holds816 : (z0 z1 : A5) → (mul5 (mul5 (mul5 z0 z0) z1) (mul5 z1 z0)) ≡ z1
  holds816 m5c0 m5c0 = refl
  holds816 m5c0 m5c1 = refl
  holds816 m5c0 m5c2 = refl
  holds816 m5c1 m5c0 = refl
  holds816 m5c1 m5c1 = refl
  holds816 m5c1 m5c2 = refl
  holds816 m5c2 m5c0 = refl
  holds816 m5c2 m5c1 = refl
  holds816 m5c2 m5c2 = refl
  cut816 : Adequate {ℓ} ((op (op (op (var 0) (var 0)) (var 1)) (op (var 1) (var 0))) , (var 1)) → ⊥
  cut816  = reject5 ((op (op (op (var 0) (var 0)) (var 1)) (op (var 1) (var 0))) , (var 1)) (λ env → holds816 (env 0) (env 1))
  bad817 : PathP (λ _ → Two) (bop (bop (bop b0 b0) b0) (bop b0 b0)) b1 → ⊥
  bad817  p = false≢true (cong lower p)
  cut817 : Adequate {ℓ} ((op (op (op (var 0) (var 0)) (var 1)) (op (var 1) (var 0))) , (var 2)) → ⊥
  cut817  adequate = bad817  (Adequate.valid adequate Two boolean env2)
  bad818 : PathP (λ _ → Two) (bop (bop (bop b0 b0) b1) (bop b1 b1)) b0 → ⊥
  bad818  p = false≢true (sym (cong lower p))
  cut818 : Adequate {ℓ} ((op (op (op (var 0) (var 0)) (var 1)) (op (var 1) (var 1))) , (var 0)) → ⊥
  cut818  adequate = bad818  (Adequate.valid adequate Two boolean env0)
  holds819 : (z0 z1 : A3) → (mul3 (mul3 (mul3 z0 z0) z1) (mul3 z1 z1)) ≡ z1
  holds819 z0 z1 = refl
  cut819 : Adequate {ℓ} ((op (op (op (var 0) (var 0)) (var 1)) (op (var 1) (var 1))) , (var 1)) → ⊥
  cut819  = reject3 ((op (op (op (var 0) (var 0)) (var 1)) (op (var 1) (var 1))) , (var 1)) (λ env → holds819 (env 0) (env 1))
  bad820 : PathP (λ _ → Two) (bop (bop (bop b0 b0) b0) (bop b0 b0)) b1 → ⊥
  bad820  p = false≢true (cong lower p)
  cut820 : Adequate {ℓ} ((op (op (op (var 0) (var 0)) (var 1)) (op (var 1) (var 1))) , (var 2)) → ⊥
  cut820  adequate = bad820  (Adequate.valid adequate Two boolean env2)
  bad821 : PathP (λ _ → Two) (bop (bop (bop b0 b0) b1) (bop b1 b0)) b0 → ⊥
  bad821  p = false≢true (sym (cong lower p))
  cut821 : Adequate {ℓ} ((op (op (op (var 0) (var 0)) (var 1)) (op (var 1) (var 2))) , (var 0)) → ⊥
  cut821  adequate = bad821  (Adequate.valid adequate Two boolean env4)
  env7 : ℕ → Two
  env7 zero = b1
  env7 (suc zero) = b1
  env7 (suc (suc zero)) = b0
  env7 (suc (suc (suc rest))) = b0
  bad822 : PathP (λ _ → Two) (bop (bop (bop b1 b1) b1) (bop b1 b0)) b1 → ⊥
  bad822  p = false≢true (cong lower p)
  cut822 : Adequate {ℓ} ((op (op (op (var 0) (var 0)) (var 1)) (op (var 1) (var 2))) , (var 1)) → ⊥
  cut822  adequate = bad822  (Adequate.valid adequate Two boolean env7)
  bad823 : PathP (λ _ → Two) (bop (bop (bop b0 b0) b0) (bop b0 b1)) b1 → ⊥
  bad823  p = false≢true (cong lower p)
  cut823 : Adequate {ℓ} ((op (op (op (var 0) (var 0)) (var 1)) (op (var 1) (var 2))) , (var 2)) → ⊥
  cut823  adequate = bad823  (Adequate.valid adequate Two boolean env2)
  bad824 : PathP (λ _ → Two) (bop (bop (bop b0 b0) b0) (bop b0 b0)) b1 → ⊥
  bad824  p = false≢true (cong lower p)
  cut824 : Adequate {ℓ} ((op (op (op (var 0) (var 0)) (var 1)) (op (var 1) (var 2))) , (var 3)) → ⊥
  cut824  adequate = bad824  (Adequate.valid adequate Two boolean env5)
  bad825 : PathP (λ _ → Two) (bop (bop (bop b0 b0) b1) (bop b0 b0)) b0 → ⊥
  bad825  p = false≢true (sym (cong lower p))
  cut825 : Adequate {ℓ} ((op (op (op (var 0) (var 0)) (var 1)) (op (var 2) (var 0))) , (var 0)) → ⊥
  cut825  adequate = bad825  (Adequate.valid adequate Two boolean env4)
  bad826 : PathP (λ _ → Two) (bop (bop (bop b1 b1) b0) (bop b1 b1)) b0 → ⊥
  bad826  p = false≢true (sym (cong lower p))
  cut826 : Adequate {ℓ} ((op (op (op (var 0) (var 0)) (var 1)) (op (var 2) (var 0))) , (var 1)) → ⊥
  cut826  adequate = bad826  (Adequate.valid adequate Two boolean env6)
  bad827 : PathP (λ _ → Two) (bop (bop (bop b0 b0) b0) (bop b1 b0)) b1 → ⊥
  bad827  p = false≢true (cong lower p)
  cut827 : Adequate {ℓ} ((op (op (op (var 0) (var 0)) (var 1)) (op (var 2) (var 0))) , (var 2)) → ⊥
  cut827  adequate = bad827  (Adequate.valid adequate Two boolean env2)
  bad828 : PathP (λ _ → Two) (bop (bop (bop b0 b0) b0) (bop b0 b0)) b1 → ⊥
  bad828  p = false≢true (cong lower p)
  cut828 : Adequate {ℓ} ((op (op (op (var 0) (var 0)) (var 1)) (op (var 2) (var 0))) , (var 3)) → ⊥
  cut828  adequate = bad828  (Adequate.valid adequate Two boolean env5)
  bad829 : PathP (λ _ → Two) (bop (bop (bop b0 b0) b1) (bop b0 b1)) b0 → ⊥
  bad829  p = false≢true (sym (cong lower p))
  cut829 : Adequate {ℓ} ((op (op (op (var 0) (var 0)) (var 1)) (op (var 2) (var 1))) , (var 0)) → ⊥
  cut829  adequate = bad829  (Adequate.valid adequate Two boolean env4)
  bad830 : PathP (λ _ → Two) (bop (bop (bop b1 b1) b1) (bop b0 b1)) b1 → ⊥
  bad830  p = false≢true (cong lower p)
  cut830 : Adequate {ℓ} ((op (op (op (var 0) (var 0)) (var 1)) (op (var 2) (var 1))) , (var 1)) → ⊥
  cut830  adequate = bad830  (Adequate.valid adequate Two boolean env7)
  bad831 : PathP (λ _ → Two) (bop (bop (bop b0 b0) b0) (bop b1 b0)) b1 → ⊥
  bad831  p = false≢true (cong lower p)
  cut831 : Adequate {ℓ} ((op (op (op (var 0) (var 0)) (var 1)) (op (var 2) (var 1))) , (var 2)) → ⊥
  cut831  adequate = bad831  (Adequate.valid adequate Two boolean env2)
  bad832 : PathP (λ _ → Two) (bop (bop (bop b0 b0) b0) (bop b0 b0)) b1 → ⊥
  bad832  p = false≢true (cong lower p)
  cut832 : Adequate {ℓ} ((op (op (op (var 0) (var 0)) (var 1)) (op (var 2) (var 1))) , (var 3)) → ⊥
  cut832  adequate = bad832  (Adequate.valid adequate Two boolean env5)
  bad833 : PathP (λ _ → Two) (bop (bop (bop b0 b0) b0) (bop b1 b1)) b0 → ⊥
  bad833  p = false≢true (sym (cong lower p))
  cut833 : Adequate {ℓ} ((op (op (op (var 0) (var 0)) (var 1)) (op (var 2) (var 2))) , (var 0)) → ⊥
  cut833  adequate = bad833  (Adequate.valid adequate Two boolean env2)
  bad834 : PathP (λ _ → Two) (bop (bop (bop b0 b0) b0) (bop b1 b1)) b0 → ⊥
  bad834  p = false≢true (sym (cong lower p))
  cut834 : Adequate {ℓ} ((op (op (op (var 0) (var 0)) (var 1)) (op (var 2) (var 2))) , (var 1)) → ⊥
  cut834  adequate = bad834  (Adequate.valid adequate Two boolean env2)
  bad835 : PathP (λ _ → Two) (bop (bop (bop b0 b0) b1) (bop b0 b0)) b0 → ⊥
  bad835  p = false≢true (sym (cong lower p))
  cut835 : Adequate {ℓ} ((op (op (op (var 0) (var 0)) (var 1)) (op (var 2) (var 2))) , (var 2)) → ⊥
  cut835  adequate = bad835  (Adequate.valid adequate Two boolean env4)
  bad836 : PathP (λ _ → Two) (bop (bop (bop b0 b0) b0) (bop b0 b0)) b1 → ⊥
  bad836  p = false≢true (cong lower p)
  cut836 : Adequate {ℓ} ((op (op (op (var 0) (var 0)) (var 1)) (op (var 2) (var 2))) , (var 3)) → ⊥
  cut836  adequate = bad836  (Adequate.valid adequate Two boolean env5)
  env8 : ℕ → Two
  env8 zero = b0
  env8 (suc zero) = b0
  env8 (suc (suc zero)) = b1
  env8 (suc (suc (suc zero))) = b1
  env8 (suc (suc (suc (suc rest)))) = b0
  bad837 : PathP (λ _ → Two) (bop (bop (bop b0 b0) b0) (bop b1 b1)) b0 → ⊥
  bad837  p = false≢true (sym (cong lower p))
  cut837 : Adequate {ℓ} ((op (op (op (var 0) (var 0)) (var 1)) (op (var 2) (var 3))) , (var 0)) → ⊥
  cut837  adequate = bad837  (Adequate.valid adequate Two boolean env8)
  bad838 : PathP (λ _ → Two) (bop (bop (bop b0 b0) b0) (bop b1 b1)) b0 → ⊥
  bad838  p = false≢true (sym (cong lower p))
  cut838 : Adequate {ℓ} ((op (op (op (var 0) (var 0)) (var 1)) (op (var 2) (var 3))) , (var 1)) → ⊥
  cut838  adequate = bad838  (Adequate.valid adequate Two boolean env8)
  env9 : ℕ → Two
  env9 zero = b0
  env9 (suc zero) = b0
  env9 (suc (suc zero)) = b1
  env9 (suc (suc (suc zero))) = b0
  env9 (suc (suc (suc (suc rest)))) = b0
  bad839 : PathP (λ _ → Two) (bop (bop (bop b0 b0) b0) (bop b1 b0)) b1 → ⊥
  bad839  p = false≢true (cong lower p)
  cut839 : Adequate {ℓ} ((op (op (op (var 0) (var 0)) (var 1)) (op (var 2) (var 3))) , (var 2)) → ⊥
  cut839  adequate = bad839  (Adequate.valid adequate Two boolean env9)
  bad840 : PathP (λ _ → Two) (bop (bop (bop b0 b0) b0) (bop b0 b1)) b1 → ⊥
  bad840  p = false≢true (cong lower p)
  cut840 : Adequate {ℓ} ((op (op (op (var 0) (var 0)) (var 1)) (op (var 2) (var 3))) , (var 3)) → ⊥
  cut840  adequate = bad840  (Adequate.valid adequate Two boolean env5)
  env10 : ℕ → Two
  env10 zero = b0
  env10 (suc zero) = b0
  env10 (suc (suc zero)) = b0
  env10 (suc (suc (suc zero))) = b0
  env10 (suc (suc (suc (suc zero)))) = b1
  env10 (suc (suc (suc (suc (suc rest))))) = b0
  bad841 : PathP (λ _ → Two) (bop (bop (bop b0 b0) b0) (bop b0 b0)) b1 → ⊥
  bad841  p = false≢true (cong lower p)
  cut841 : Adequate {ℓ} ((op (op (op (var 0) (var 0)) (var 1)) (op (var 2) (var 3))) , (var 4)) → ⊥
  cut841  adequate = bad841  (Adequate.valid adequate Two boolean env10)
  holds842 : (z0 z1 : A2) → (mul2 (mul2 (mul2 z0 z1) z0) (mul2 z0 z0)) ≡ z0
  holds842 z0 z1 = refl
  cut842 : Adequate {ℓ} ((op (op (op (var 0) (var 1)) (var 0)) (op (var 0) (var 0))) , (var 0)) → ⊥
  cut842  = reject2 ((op (op (op (var 0) (var 1)) (var 0)) (op (var 0) (var 0))) , (var 0)) (λ env → holds842 (env 0) (env 1))
  bad843 : PathP (λ _ → Two) (bop (bop (bop b0 b1) b0) (bop b0 b0)) b1 → ⊥
  bad843  p = false≢true (cong lower p)
  cut843 : Adequate {ℓ} ((op (op (op (var 0) (var 1)) (var 0)) (op (var 0) (var 0))) , (var 1)) → ⊥
  cut843  adequate = bad843  (Adequate.valid adequate Two boolean env0)
  bad844 : PathP (λ _ → Two) (bop (bop (bop b0 b0) b0) (bop b0 b0)) b1 → ⊥
  bad844  p = false≢true (cong lower p)
  cut844 : Adequate {ℓ} ((op (op (op (var 0) (var 1)) (var 0)) (op (var 0) (var 0))) , (var 2)) → ⊥
  cut844  adequate = bad844  (Adequate.valid adequate Two boolean env2)
  holds845 : (z0 z1 : A2) → (mul2 (mul2 (mul2 z0 z1) z0) (mul2 z0 z1)) ≡ z0
  holds845 z0 z1 = refl
  cut845 : Adequate {ℓ} ((op (op (op (var 0) (var 1)) (var 0)) (op (var 0) (var 1))) , (var 0)) → ⊥
  cut845  = reject2 ((op (op (op (var 0) (var 1)) (var 0)) (op (var 0) (var 1))) , (var 0)) (λ env → holds845 (env 0) (env 1))
  bad846 : PathP (λ _ → Two) (bop (bop (bop b0 b1) b0) (bop b0 b1)) b1 → ⊥
  bad846  p = false≢true (cong lower p)
  cut846 : Adequate {ℓ} ((op (op (op (var 0) (var 1)) (var 0)) (op (var 0) (var 1))) , (var 1)) → ⊥
  cut846  adequate = bad846  (Adequate.valid adequate Two boolean env0)
  bad847 : PathP (λ _ → Two) (bop (bop (bop b0 b0) b0) (bop b0 b0)) b1 → ⊥
  bad847  p = false≢true (cong lower p)
  cut847 : Adequate {ℓ} ((op (op (op (var 0) (var 1)) (var 0)) (op (var 0) (var 1))) , (var 2)) → ⊥
  cut847  adequate = bad847  (Adequate.valid adequate Two boolean env2)
  bad848 : PathP (λ _ → Two) (bop (bop (bop b1 b1) b1) (bop b1 b0)) b1 → ⊥
  bad848  p = false≢true (cong lower p)
  cut848 : Adequate {ℓ} ((op (op (op (var 0) (var 1)) (var 0)) (op (var 0) (var 2))) , (var 0)) → ⊥
  cut848  adequate = bad848  (Adequate.valid adequate Two boolean env7)
  bad849 : PathP (λ _ → Two) (bop (bop (bop b0 b1) b0) (bop b0 b0)) b1 → ⊥
  bad849  p = false≢true (cong lower p)
  cut849 : Adequate {ℓ} ((op (op (op (var 0) (var 1)) (var 0)) (op (var 0) (var 2))) , (var 1)) → ⊥
  cut849  adequate = bad849  (Adequate.valid adequate Two boolean env4)
  bad850 : PathP (λ _ → Two) (bop (bop (bop b0 b0) b0) (bop b0 b1)) b1 → ⊥
  bad850  p = false≢true (cong lower p)
  cut850 : Adequate {ℓ} ((op (op (op (var 0) (var 1)) (var 0)) (op (var 0) (var 2))) , (var 2)) → ⊥
  cut850  adequate = bad850  (Adequate.valid adequate Two boolean env2)
  bad851 : PathP (λ _ → Two) (bop (bop (bop b0 b0) b0) (bop b0 b0)) b1 → ⊥
  bad851  p = false≢true (cong lower p)
  cut851 : Adequate {ℓ} ((op (op (op (var 0) (var 1)) (var 0)) (op (var 0) (var 2))) , (var 3)) → ⊥
  cut851  adequate = bad851  (Adequate.valid adequate Two boolean env5)
  holds852 : (z0 z1 : A2) → (mul2 (mul2 (mul2 z0 z1) z0) (mul2 z1 z0)) ≡ z0
  holds852 z0 z1 = refl
  cut852 : Adequate {ℓ} ((op (op (op (var 0) (var 1)) (var 0)) (op (var 1) (var 0))) , (var 0)) → ⊥
  cut852  = reject2 ((op (op (op (var 0) (var 1)) (var 0)) (op (var 1) (var 0))) , (var 0)) (λ env → holds852 (env 0) (env 1))
  bad853 : PathP (λ _ → Two) (bop (bop (bop b0 b1) b0) (bop b1 b0)) b1 → ⊥
  bad853  p = false≢true (cong lower p)
  cut853 : Adequate {ℓ} ((op (op (op (var 0) (var 1)) (var 0)) (op (var 1) (var 0))) , (var 1)) → ⊥
  cut853  adequate = bad853  (Adequate.valid adequate Two boolean env0)
  bad854 : PathP (λ _ → Two) (bop (bop (bop b0 b0) b0) (bop b0 b0)) b1 → ⊥
  bad854  p = false≢true (cong lower p)
  cut854 : Adequate {ℓ} ((op (op (op (var 0) (var 1)) (var 0)) (op (var 1) (var 0))) , (var 2)) → ⊥
  cut854  adequate = bad854  (Adequate.valid adequate Two boolean env2)
  bad855 : PathP (λ _ → Two) (bop (bop (bop b0 b1) b0) (bop b1 b1)) b0 → ⊥
  bad855  p = false≢true (sym (cong lower p))
  cut855 : Adequate {ℓ} ((op (op (op (var 0) (var 1)) (var 0)) (op (var 1) (var 1))) , (var 0)) → ⊥
  cut855  adequate = bad855  (Adequate.valid adequate Two boolean env0)
  bad856 : PathP (λ _ → Two) (bop (bop (bop b1 b0) b1) (bop b0 b0)) b0 → ⊥
  bad856  p = false≢true (sym (cong lower p))
  cut856 : Adequate {ℓ} ((op (op (op (var 0) (var 1)) (var 0)) (op (var 1) (var 1))) , (var 1)) → ⊥
  cut856  adequate = bad856  (Adequate.valid adequate Two boolean env1)
  bad857 : PathP (λ _ → Two) (bop (bop (bop b0 b0) b0) (bop b0 b0)) b1 → ⊥
  bad857  p = false≢true (cong lower p)
  cut857 : Adequate {ℓ} ((op (op (op (var 0) (var 1)) (var 0)) (op (var 1) (var 1))) , (var 2)) → ⊥
  cut857  adequate = bad857  (Adequate.valid adequate Two boolean env2)
  bad858 : PathP (λ _ → Two) (bop (bop (bop b0 b1) b0) (bop b1 b1)) b0 → ⊥
  bad858  p = false≢true (sym (cong lower p))
  cut858 : Adequate {ℓ} ((op (op (op (var 0) (var 1)) (var 0)) (op (var 1) (var 2))) , (var 0)) → ⊥
  cut858  adequate = bad858  (Adequate.valid adequate Two boolean env3)
  bad859 : PathP (λ _ → Two) (bop (bop (bop b0 b1) b0) (bop b1 b0)) b1 → ⊥
  bad859  p = false≢true (cong lower p)
  cut859 : Adequate {ℓ} ((op (op (op (var 0) (var 1)) (var 0)) (op (var 1) (var 2))) , (var 1)) → ⊥
  cut859  adequate = bad859  (Adequate.valid adequate Two boolean env4)
  bad860 : PathP (λ _ → Two) (bop (bop (bop b0 b0) b0) (bop b0 b1)) b1 → ⊥
  bad860  p = false≢true (cong lower p)
  cut860 : Adequate {ℓ} ((op (op (op (var 0) (var 1)) (var 0)) (op (var 1) (var 2))) , (var 2)) → ⊥
  cut860  adequate = bad860  (Adequate.valid adequate Two boolean env2)
  bad861 : PathP (λ _ → Two) (bop (bop (bop b0 b0) b0) (bop b0 b0)) b1 → ⊥
  bad861  p = false≢true (cong lower p)
  cut861 : Adequate {ℓ} ((op (op (op (var 0) (var 1)) (var 0)) (op (var 1) (var 2))) , (var 3)) → ⊥
  cut861  adequate = bad861  (Adequate.valid adequate Two boolean env5)
  bad862 : PathP (λ _ → Two) (bop (bop (bop b1 b1) b1) (bop b0 b1)) b1 → ⊥
  bad862  p = false≢true (cong lower p)
  cut862 : Adequate {ℓ} ((op (op (op (var 0) (var 1)) (var 0)) (op (var 2) (var 0))) , (var 0)) → ⊥
  cut862  adequate = bad862  (Adequate.valid adequate Two boolean env7)
  bad863 : PathP (λ _ → Two) (bop (bop (bop b0 b1) b0) (bop b0 b0)) b1 → ⊥
  bad863  p = false≢true (cong lower p)
  cut863 : Adequate {ℓ} ((op (op (op (var 0) (var 1)) (var 0)) (op (var 2) (var 0))) , (var 1)) → ⊥
  cut863  adequate = bad863  (Adequate.valid adequate Two boolean env4)
  bad864 : PathP (λ _ → Two) (bop (bop (bop b0 b0) b0) (bop b1 b0)) b1 → ⊥
  bad864  p = false≢true (cong lower p)
  cut864 : Adequate {ℓ} ((op (op (op (var 0) (var 1)) (var 0)) (op (var 2) (var 0))) , (var 2)) → ⊥
  cut864  adequate = bad864  (Adequate.valid adequate Two boolean env2)
  bad865 : PathP (λ _ → Two) (bop (bop (bop b0 b0) b0) (bop b0 b0)) b1 → ⊥
  bad865  p = false≢true (cong lower p)
  cut865 : Adequate {ℓ} ((op (op (op (var 0) (var 1)) (var 0)) (op (var 2) (var 0))) , (var 3)) → ⊥
  cut865  adequate = bad865  (Adequate.valid adequate Two boolean env5)
  bad866 : PathP (λ _ → Two) (bop (bop (bop b0 b1) b0) (bop b1 b1)) b0 → ⊥
  bad866  p = false≢true (sym (cong lower p))
  cut866 : Adequate {ℓ} ((op (op (op (var 0) (var 1)) (var 0)) (op (var 2) (var 1))) , (var 0)) → ⊥
  cut866  adequate = bad866  (Adequate.valid adequate Two boolean env3)
  bad867 : PathP (λ _ → Two) (bop (bop (bop b0 b1) b0) (bop b0 b1)) b1 → ⊥
  bad867  p = false≢true (cong lower p)
  cut867 : Adequate {ℓ} ((op (op (op (var 0) (var 1)) (var 0)) (op (var 2) (var 1))) , (var 1)) → ⊥
  cut867  adequate = bad867  (Adequate.valid adequate Two boolean env4)
  bad868 : PathP (λ _ → Two) (bop (bop (bop b0 b0) b0) (bop b1 b0)) b1 → ⊥
  bad868  p = false≢true (cong lower p)
  cut868 : Adequate {ℓ} ((op (op (op (var 0) (var 1)) (var 0)) (op (var 2) (var 1))) , (var 2)) → ⊥
  cut868  adequate = bad868  (Adequate.valid adequate Two boolean env2)
  bad869 : PathP (λ _ → Two) (bop (bop (bop b0 b0) b0) (bop b0 b0)) b1 → ⊥
  bad869  p = false≢true (cong lower p)
  cut869 : Adequate {ℓ} ((op (op (op (var 0) (var 1)) (var 0)) (op (var 2) (var 1))) , (var 3)) → ⊥
  cut869  adequate = bad869  (Adequate.valid adequate Two boolean env5)
  bad870 : PathP (λ _ → Two) (bop (bop (bop b0 b0) b0) (bop b1 b1)) b0 → ⊥
  bad870  p = false≢true (sym (cong lower p))
  cut870 : Adequate {ℓ} ((op (op (op (var 0) (var 1)) (var 0)) (op (var 2) (var 2))) , (var 0)) → ⊥
  cut870  adequate = bad870  (Adequate.valid adequate Two boolean env2)
  bad871 : PathP (λ _ → Two) (bop (bop (bop b0 b0) b0) (bop b1 b1)) b0 → ⊥
  bad871  p = false≢true (sym (cong lower p))
  cut871 : Adequate {ℓ} ((op (op (op (var 0) (var 1)) (var 0)) (op (var 2) (var 2))) , (var 1)) → ⊥
  cut871  adequate = bad871  (Adequate.valid adequate Two boolean env2)
  env11 : ℕ → Two
  env11 zero = b1
  env11 (suc zero) = b0
  env11 (suc (suc zero)) = b0
  env11 (suc (suc (suc rest))) = b0
  bad872 : PathP (λ _ → Two) (bop (bop (bop b1 b0) b1) (bop b0 b0)) b0 → ⊥
  bad872  p = false≢true (sym (cong lower p))
  cut872 : Adequate {ℓ} ((op (op (op (var 0) (var 1)) (var 0)) (op (var 2) (var 2))) , (var 2)) → ⊥
  cut872  adequate = bad872  (Adequate.valid adequate Two boolean env11)
  bad873 : PathP (λ _ → Two) (bop (bop (bop b0 b0) b0) (bop b0 b0)) b1 → ⊥
  bad873  p = false≢true (cong lower p)
  cut873 : Adequate {ℓ} ((op (op (op (var 0) (var 1)) (var 0)) (op (var 2) (var 2))) , (var 3)) → ⊥
  cut873  adequate = bad873  (Adequate.valid adequate Two boolean env5)
  bad874 : PathP (λ _ → Two) (bop (bop (bop b0 b0) b0) (bop b1 b1)) b0 → ⊥
  bad874  p = false≢true (sym (cong lower p))
  cut874 : Adequate {ℓ} ((op (op (op (var 0) (var 1)) (var 0)) (op (var 2) (var 3))) , (var 0)) → ⊥
  cut874  adequate = bad874  (Adequate.valid adequate Two boolean env8)
  bad875 : PathP (λ _ → Two) (bop (bop (bop b0 b0) b0) (bop b1 b1)) b0 → ⊥
  bad875  p = false≢true (sym (cong lower p))
  cut875 : Adequate {ℓ} ((op (op (op (var 0) (var 1)) (var 0)) (op (var 2) (var 3))) , (var 1)) → ⊥
  cut875  adequate = bad875  (Adequate.valid adequate Two boolean env8)
  bad876 : PathP (λ _ → Two) (bop (bop (bop b0 b0) b0) (bop b1 b0)) b1 → ⊥
  bad876  p = false≢true (cong lower p)
  cut876 : Adequate {ℓ} ((op (op (op (var 0) (var 1)) (var 0)) (op (var 2) (var 3))) , (var 2)) → ⊥
  cut876  adequate = bad876  (Adequate.valid adequate Two boolean env9)
  bad877 : PathP (λ _ → Two) (bop (bop (bop b0 b0) b0) (bop b0 b1)) b1 → ⊥
  bad877  p = false≢true (cong lower p)
  cut877 : Adequate {ℓ} ((op (op (op (var 0) (var 1)) (var 0)) (op (var 2) (var 3))) , (var 3)) → ⊥
  cut877  adequate = bad877  (Adequate.valid adequate Two boolean env5)
  bad878 : PathP (λ _ → Two) (bop (bop (bop b0 b0) b0) (bop b0 b0)) b1 → ⊥
  bad878  p = false≢true (cong lower p)
  cut878 : Adequate {ℓ} ((op (op (op (var 0) (var 1)) (var 0)) (op (var 2) (var 3))) , (var 4)) → ⊥
  cut878  adequate = bad878  (Adequate.valid adequate Two boolean env10)
  bad879 : PathP (λ _ → Two) (bop (bop (bop b0 b1) b1) (bop b0 b0)) b0 → ⊥
  bad879  p = false≢true (sym (cong lower p))
  cut879 : Adequate {ℓ} ((op (op (op (var 0) (var 1)) (var 1)) (op (var 0) (var 0))) , (var 0)) → ⊥
  cut879  adequate = bad879  (Adequate.valid adequate Two boolean env0)
  bad880 : PathP (λ _ → Two) (bop (bop (bop b1 b0) b0) (bop b1 b1)) b0 → ⊥
  bad880  p = false≢true (sym (cong lower p))
  cut880 : Adequate {ℓ} ((op (op (op (var 0) (var 1)) (var 1)) (op (var 0) (var 0))) , (var 1)) → ⊥
  cut880  adequate = bad880  (Adequate.valid adequate Two boolean env1)
  bad881 : PathP (λ _ → Two) (bop (bop (bop b0 b0) b0) (bop b0 b0)) b1 → ⊥
  bad881  p = false≢true (cong lower p)
  cut881 : Adequate {ℓ} ((op (op (op (var 0) (var 1)) (var 1)) (op (var 0) (var 0))) , (var 2)) → ⊥
  cut881  adequate = bad881  (Adequate.valid adequate Two boolean env2)
  bad882 : PathP (λ _ → Two) (bop (bop (bop b0 b1) b1) (bop b0 b1)) b0 → ⊥
  bad882  p = false≢true (sym (cong lower p))
  cut882 : Adequate {ℓ} ((op (op (op (var 0) (var 1)) (var 1)) (op (var 0) (var 1))) , (var 0)) → ⊥
  cut882  adequate = bad882  (Adequate.valid adequate Two boolean env0)
  holds883 : (z0 z1 : A3) → (mul3 (mul3 (mul3 z0 z1) z1) (mul3 z0 z1)) ≡ z1
  holds883 z0 z1 = refl
  cut883 : Adequate {ℓ} ((op (op (op (var 0) (var 1)) (var 1)) (op (var 0) (var 1))) , (var 1)) → ⊥
  cut883  = reject3 ((op (op (op (var 0) (var 1)) (var 1)) (op (var 0) (var 1))) , (var 1)) (λ env → holds883 (env 0) (env 1))
  bad884 : PathP (λ _ → Two) (bop (bop (bop b0 b0) b0) (bop b0 b0)) b1 → ⊥
  bad884  p = false≢true (cong lower p)
  cut884 : Adequate {ℓ} ((op (op (op (var 0) (var 1)) (var 1)) (op (var 0) (var 1))) , (var 2)) → ⊥
  cut884  adequate = bad884  (Adequate.valid adequate Two boolean env2)
  bad885 : PathP (λ _ → Two) (bop (bop (bop b0 b1) b1) (bop b0 b0)) b0 → ⊥
  bad885  p = false≢true (sym (cong lower p))
  cut885 : Adequate {ℓ} ((op (op (op (var 0) (var 1)) (var 1)) (op (var 0) (var 2))) , (var 0)) → ⊥
  cut885  adequate = bad885  (Adequate.valid adequate Two boolean env4)
  bad886 : PathP (λ _ → Two) (bop (bop (bop b1 b0) b0) (bop b1 b1)) b0 → ⊥
  bad886  p = false≢true (sym (cong lower p))
  cut886 : Adequate {ℓ} ((op (op (op (var 0) (var 1)) (var 1)) (op (var 0) (var 2))) , (var 1)) → ⊥
  cut886  adequate = bad886  (Adequate.valid adequate Two boolean env6)
  bad887 : PathP (λ _ → Two) (bop (bop (bop b0 b0) b0) (bop b0 b1)) b1 → ⊥
  bad887  p = false≢true (cong lower p)
  cut887 : Adequate {ℓ} ((op (op (op (var 0) (var 1)) (var 1)) (op (var 0) (var 2))) , (var 2)) → ⊥
  cut887  adequate = bad887  (Adequate.valid adequate Two boolean env2)
  bad888 : PathP (λ _ → Two) (bop (bop (bop b0 b0) b0) (bop b0 b0)) b1 → ⊥
  bad888  p = false≢true (cong lower p)
  cut888 : Adequate {ℓ} ((op (op (op (var 0) (var 1)) (var 1)) (op (var 0) (var 2))) , (var 3)) → ⊥
  cut888  adequate = bad888  (Adequate.valid adequate Two boolean env5)
  bad889 : PathP (λ _ → Two) (bop (bop (bop b0 b1) b1) (bop b1 b0)) b0 → ⊥
  bad889  p = false≢true (sym (cong lower p))
  cut889 : Adequate {ℓ} ((op (op (op (var 0) (var 1)) (var 1)) (op (var 1) (var 0))) , (var 0)) → ⊥
  cut889  adequate = bad889  (Adequate.valid adequate Two boolean env0)
  holds890 : (z0 z1 : A4) → (mul4 (mul4 (mul4 z0 z1) z1) (mul4 z1 z0)) ≡ z1
  holds890 m4c0 m4c0 = refl
  holds890 m4c0 m4c1 = refl
  holds890 m4c1 m4c0 = refl
  holds890 m4c1 m4c1 = refl
  cut890 : Adequate {ℓ} ((op (op (op (var 0) (var 1)) (var 1)) (op (var 1) (var 0))) , (var 1)) → ⊥
  cut890  = reject4 ((op (op (op (var 0) (var 1)) (var 1)) (op (var 1) (var 0))) , (var 1)) (λ env → holds890 (env 0) (env 1))
  bad891 : PathP (λ _ → Two) (bop (bop (bop b0 b0) b0) (bop b0 b0)) b1 → ⊥
  bad891  p = false≢true (cong lower p)
  cut891 : Adequate {ℓ} ((op (op (op (var 0) (var 1)) (var 1)) (op (var 1) (var 0))) , (var 2)) → ⊥
  cut891  adequate = bad891  (Adequate.valid adequate Two boolean env2)
  bad892 : PathP (λ _ → Two) (bop (bop (bop b0 b1) b1) (bop b1 b1)) b0 → ⊥
  bad892  p = false≢true (sym (cong lower p))
  cut892 : Adequate {ℓ} ((op (op (op (var 0) (var 1)) (var 1)) (op (var 1) (var 1))) , (var 0)) → ⊥
  cut892  adequate = bad892  (Adequate.valid adequate Two boolean env0)
  holds893 : (z0 z1 : A3) → (mul3 (mul3 (mul3 z0 z1) z1) (mul3 z1 z1)) ≡ z1
  holds893 z0 z1 = refl
  cut893 : Adequate {ℓ} ((op (op (op (var 0) (var 1)) (var 1)) (op (var 1) (var 1))) , (var 1)) → ⊥
  cut893  = reject3 ((op (op (op (var 0) (var 1)) (var 1)) (op (var 1) (var 1))) , (var 1)) (λ env → holds893 (env 0) (env 1))
  bad894 : PathP (λ _ → Two) (bop (bop (bop b0 b0) b0) (bop b0 b0)) b1 → ⊥
  bad894  p = false≢true (cong lower p)
  cut894 : Adequate {ℓ} ((op (op (op (var 0) (var 1)) (var 1)) (op (var 1) (var 1))) , (var 2)) → ⊥
  cut894  adequate = bad894  (Adequate.valid adequate Two boolean env2)
  bad895 : PathP (λ _ → Two) (bop (bop (bop b0 b1) b1) (bop b1 b0)) b0 → ⊥
  bad895  p = false≢true (sym (cong lower p))
  cut895 : Adequate {ℓ} ((op (op (op (var 0) (var 1)) (var 1)) (op (var 1) (var 2))) , (var 0)) → ⊥
  cut895  adequate = bad895  (Adequate.valid adequate Two boolean env4)
  bad896 : PathP (λ _ → Two) (bop (bop (bop b1 b1) b1) (bop b1 b0)) b1 → ⊥
  bad896  p = false≢true (cong lower p)
  cut896 : Adequate {ℓ} ((op (op (op (var 0) (var 1)) (var 1)) (op (var 1) (var 2))) , (var 1)) → ⊥
  cut896  adequate = bad896  (Adequate.valid adequate Two boolean env7)
  bad897 : PathP (λ _ → Two) (bop (bop (bop b0 b0) b0) (bop b0 b1)) b1 → ⊥
  bad897  p = false≢true (cong lower p)
  cut897 : Adequate {ℓ} ((op (op (op (var 0) (var 1)) (var 1)) (op (var 1) (var 2))) , (var 2)) → ⊥
  cut897  adequate = bad897  (Adequate.valid adequate Two boolean env2)
  bad898 : PathP (λ _ → Two) (bop (bop (bop b0 b0) b0) (bop b0 b0)) b1 → ⊥
  bad898  p = false≢true (cong lower p)
  cut898 : Adequate {ℓ} ((op (op (op (var 0) (var 1)) (var 1)) (op (var 1) (var 2))) , (var 3)) → ⊥
  cut898  adequate = bad898  (Adequate.valid adequate Two boolean env5)
  bad899 : PathP (λ _ → Two) (bop (bop (bop b0 b1) b1) (bop b0 b0)) b0 → ⊥
  bad899  p = false≢true (sym (cong lower p))
  cut899 : Adequate {ℓ} ((op (op (op (var 0) (var 1)) (var 1)) (op (var 2) (var 0))) , (var 0)) → ⊥
  cut899  adequate = bad899  (Adequate.valid adequate Two boolean env4)
  bad900 : PathP (λ _ → Two) (bop (bop (bop b1 b0) b0) (bop b1 b1)) b0 → ⊥
  bad900  p = false≢true (sym (cong lower p))
  cut900 : Adequate {ℓ} ((op (op (op (var 0) (var 1)) (var 1)) (op (var 2) (var 0))) , (var 1)) → ⊥
  cut900  adequate = bad900  (Adequate.valid adequate Two boolean env6)
  bad901 : PathP (λ _ → Two) (bop (bop (bop b0 b0) b0) (bop b1 b0)) b1 → ⊥
  bad901  p = false≢true (cong lower p)
  cut901 : Adequate {ℓ} ((op (op (op (var 0) (var 1)) (var 1)) (op (var 2) (var 0))) , (var 2)) → ⊥
  cut901  adequate = bad901  (Adequate.valid adequate Two boolean env2)
  bad902 : PathP (λ _ → Two) (bop (bop (bop b0 b0) b0) (bop b0 b0)) b1 → ⊥
  bad902  p = false≢true (cong lower p)
  cut902 : Adequate {ℓ} ((op (op (op (var 0) (var 1)) (var 1)) (op (var 2) (var 0))) , (var 3)) → ⊥
  cut902  adequate = bad902  (Adequate.valid adequate Two boolean env5)
  bad903 : PathP (λ _ → Two) (bop (bop (bop b0 b1) b1) (bop b0 b1)) b0 → ⊥
  bad903  p = false≢true (sym (cong lower p))
  cut903 : Adequate {ℓ} ((op (op (op (var 0) (var 1)) (var 1)) (op (var 2) (var 1))) , (var 0)) → ⊥
  cut903  adequate = bad903  (Adequate.valid adequate Two boolean env4)
  bad904 : PathP (λ _ → Two) (bop (bop (bop b1 b1) b1) (bop b0 b1)) b1 → ⊥
  bad904  p = false≢true (cong lower p)
  cut904 : Adequate {ℓ} ((op (op (op (var 0) (var 1)) (var 1)) (op (var 2) (var 1))) , (var 1)) → ⊥
  cut904  adequate = bad904  (Adequate.valid adequate Two boolean env7)
  bad905 : PathP (λ _ → Two) (bop (bop (bop b0 b0) b0) (bop b1 b0)) b1 → ⊥
  bad905  p = false≢true (cong lower p)
  cut905 : Adequate {ℓ} ((op (op (op (var 0) (var 1)) (var 1)) (op (var 2) (var 1))) , (var 2)) → ⊥
  cut905  adequate = bad905  (Adequate.valid adequate Two boolean env2)
  bad906 : PathP (λ _ → Two) (bop (bop (bop b0 b0) b0) (bop b0 b0)) b1 → ⊥
  bad906  p = false≢true (cong lower p)
  cut906 : Adequate {ℓ} ((op (op (op (var 0) (var 1)) (var 1)) (op (var 2) (var 1))) , (var 3)) → ⊥
  cut906  adequate = bad906  (Adequate.valid adequate Two boolean env5)
  bad907 : PathP (λ _ → Two) (bop (bop (bop b0 b0) b0) (bop b1 b1)) b0 → ⊥
  bad907  p = false≢true (sym (cong lower p))
  cut907 : Adequate {ℓ} ((op (op (op (var 0) (var 1)) (var 1)) (op (var 2) (var 2))) , (var 0)) → ⊥
  cut907  adequate = bad907  (Adequate.valid adequate Two boolean env2)
  bad908 : PathP (λ _ → Two) (bop (bop (bop b0 b0) b0) (bop b1 b1)) b0 → ⊥
  bad908  p = false≢true (sym (cong lower p))
  cut908 : Adequate {ℓ} ((op (op (op (var 0) (var 1)) (var 1)) (op (var 2) (var 2))) , (var 1)) → ⊥
  cut908  adequate = bad908  (Adequate.valid adequate Two boolean env2)
  bad909 : PathP (λ _ → Two) (bop (bop (bop b0 b1) b1) (bop b0 b0)) b0 → ⊥
  bad909  p = false≢true (sym (cong lower p))
  cut909 : Adequate {ℓ} ((op (op (op (var 0) (var 1)) (var 1)) (op (var 2) (var 2))) , (var 2)) → ⊥
  cut909  adequate = bad909  (Adequate.valid adequate Two boolean env4)
  bad910 : PathP (λ _ → Two) (bop (bop (bop b0 b0) b0) (bop b0 b0)) b1 → ⊥
  bad910  p = false≢true (cong lower p)
  cut910 : Adequate {ℓ} ((op (op (op (var 0) (var 1)) (var 1)) (op (var 2) (var 2))) , (var 3)) → ⊥
  cut910  adequate = bad910  (Adequate.valid adequate Two boolean env5)
  bad911 : PathP (λ _ → Two) (bop (bop (bop b0 b0) b0) (bop b1 b1)) b0 → ⊥
  bad911  p = false≢true (sym (cong lower p))
  cut911 : Adequate {ℓ} ((op (op (op (var 0) (var 1)) (var 1)) (op (var 2) (var 3))) , (var 0)) → ⊥
  cut911  adequate = bad911  (Adequate.valid adequate Two boolean env8)
  bad912 : PathP (λ _ → Two) (bop (bop (bop b0 b0) b0) (bop b1 b1)) b0 → ⊥
  bad912  p = false≢true (sym (cong lower p))
  cut912 : Adequate {ℓ} ((op (op (op (var 0) (var 1)) (var 1)) (op (var 2) (var 3))) , (var 1)) → ⊥
  cut912  adequate = bad912  (Adequate.valid adequate Two boolean env8)
  bad913 : PathP (λ _ → Two) (bop (bop (bop b0 b0) b0) (bop b1 b0)) b1 → ⊥
  bad913  p = false≢true (cong lower p)
  cut913 : Adequate {ℓ} ((op (op (op (var 0) (var 1)) (var 1)) (op (var 2) (var 3))) , (var 2)) → ⊥
  cut913  adequate = bad913  (Adequate.valid adequate Two boolean env9)
  bad914 : PathP (λ _ → Two) (bop (bop (bop b0 b0) b0) (bop b0 b1)) b1 → ⊥
  bad914  p = false≢true (cong lower p)
  cut914 : Adequate {ℓ} ((op (op (op (var 0) (var 1)) (var 1)) (op (var 2) (var 3))) , (var 3)) → ⊥
  cut914  adequate = bad914  (Adequate.valid adequate Two boolean env5)
  bad915 : PathP (λ _ → Two) (bop (bop (bop b0 b0) b0) (bop b0 b0)) b1 → ⊥
  bad915  p = false≢true (cong lower p)
  cut915 : Adequate {ℓ} ((op (op (op (var 0) (var 1)) (var 1)) (op (var 2) (var 3))) , (var 4)) → ⊥
  cut915  adequate = bad915  (Adequate.valid adequate Two boolean env10)
  bad916 : PathP (λ _ → Two) (bop (bop (bop b0 b0) b1) (bop b0 b0)) b0 → ⊥
  bad916  p = false≢true (sym (cong lower p))
  cut916 : Adequate {ℓ} ((op (op (op (var 0) (var 1)) (var 2)) (op (var 0) (var 0))) , (var 0)) → ⊥
  cut916  adequate = bad916  (Adequate.valid adequate Two boolean env2)
  bad917 : PathP (λ _ → Two) (bop (bop (bop b0 b0) b1) (bop b0 b0)) b0 → ⊥
  bad917  p = false≢true (sym (cong lower p))
  cut917 : Adequate {ℓ} ((op (op (op (var 0) (var 1)) (var 2)) (op (var 0) (var 0))) , (var 1)) → ⊥
  cut917  adequate = bad917  (Adequate.valid adequate Two boolean env2)
  bad918 : PathP (λ _ → Two) (bop (bop (bop b1 b0) b0) (bop b1 b1)) b0 → ⊥
  bad918  p = false≢true (sym (cong lower p))
  cut918 : Adequate {ℓ} ((op (op (op (var 0) (var 1)) (var 2)) (op (var 0) (var 0))) , (var 2)) → ⊥
  cut918  adequate = bad918  (Adequate.valid adequate Two boolean env11)
  bad919 : PathP (λ _ → Two) (bop (bop (bop b0 b0) b0) (bop b0 b0)) b1 → ⊥
  bad919  p = false≢true (cong lower p)
  cut919 : Adequate {ℓ} ((op (op (op (var 0) (var 1)) (var 2)) (op (var 0) (var 0))) , (var 3)) → ⊥
  cut919  adequate = bad919  (Adequate.valid adequate Two boolean env5)
  bad920 : PathP (λ _ → Two) (bop (bop (bop b0 b0) b1) (bop b0 b0)) b0 → ⊥
  bad920  p = false≢true (sym (cong lower p))
  cut920 : Adequate {ℓ} ((op (op (op (var 0) (var 1)) (var 2)) (op (var 0) (var 1))) , (var 0)) → ⊥
  cut920  adequate = bad920  (Adequate.valid adequate Two boolean env2)
  bad921 : PathP (λ _ → Two) (bop (bop (bop b0 b0) b1) (bop b0 b0)) b0 → ⊥
  bad921  p = false≢true (sym (cong lower p))
  cut921 : Adequate {ℓ} ((op (op (op (var 0) (var 1)) (var 2)) (op (var 0) (var 1))) , (var 1)) → ⊥
  cut921  adequate = bad921  (Adequate.valid adequate Two boolean env2)
  bad922 : PathP (λ _ → Two) (bop (bop (bop b1 b1) b0) (bop b1 b1)) b0 → ⊥
  bad922  p = false≢true (sym (cong lower p))
  cut922 : Adequate {ℓ} ((op (op (op (var 0) (var 1)) (var 2)) (op (var 0) (var 1))) , (var 2)) → ⊥
  cut922  adequate = bad922  (Adequate.valid adequate Two boolean env7)
  bad923 : PathP (λ _ → Two) (bop (bop (bop b0 b0) b0) (bop b0 b0)) b1 → ⊥
  bad923  p = false≢true (cong lower p)
  cut923 : Adequate {ℓ} ((op (op (op (var 0) (var 1)) (var 2)) (op (var 0) (var 1))) , (var 3)) → ⊥
  cut923  adequate = bad923  (Adequate.valid adequate Two boolean env5)
  bad924 : PathP (λ _ → Two) (bop (bop (bop b0 b0) b1) (bop b0 b1)) b0 → ⊥
  bad924  p = false≢true (sym (cong lower p))
  cut924 : Adequate {ℓ} ((op (op (op (var 0) (var 1)) (var 2)) (op (var 0) (var 2))) , (var 0)) → ⊥
  cut924  adequate = bad924  (Adequate.valid adequate Two boolean env2)
  bad925 : PathP (λ _ → Two) (bop (bop (bop b0 b0) b1) (bop b0 b1)) b0 → ⊥
  bad925  p = false≢true (sym (cong lower p))
  cut925 : Adequate {ℓ} ((op (op (op (var 0) (var 1)) (var 2)) (op (var 0) (var 2))) , (var 1)) → ⊥
  cut925  adequate = bad925  (Adequate.valid adequate Two boolean env2)
  holds926 : (z0 z1 z2 : A3) → (mul3 (mul3 (mul3 z0 z1) z2) (mul3 z0 z2)) ≡ z2
  holds926 z0 z1 z2 = refl
  cut926 : Adequate {ℓ} ((op (op (op (var 0) (var 1)) (var 2)) (op (var 0) (var 2))) , (var 2)) → ⊥
  cut926  = reject3 ((op (op (op (var 0) (var 1)) (var 2)) (op (var 0) (var 2))) , (var 2)) (λ env → holds926 (env 0) (env 1) (env 2))
  bad927 : PathP (λ _ → Two) (bop (bop (bop b0 b0) b0) (bop b0 b0)) b1 → ⊥
  bad927  p = false≢true (cong lower p)
  cut927 : Adequate {ℓ} ((op (op (op (var 0) (var 1)) (var 2)) (op (var 0) (var 2))) , (var 3)) → ⊥
  cut927  adequate = bad927  (Adequate.valid adequate Two boolean env5)
  bad928 : PathP (λ _ → Two) (bop (bop (bop b0 b0) b1) (bop b0 b0)) b0 → ⊥
  bad928  p = false≢true (sym (cong lower p))
  cut928 : Adequate {ℓ} ((op (op (op (var 0) (var 1)) (var 2)) (op (var 0) (var 3))) , (var 0)) → ⊥
  cut928  adequate = bad928  (Adequate.valid adequate Two boolean env9)
  bad929 : PathP (λ _ → Two) (bop (bop (bop b0 b0) b1) (bop b0 b0)) b0 → ⊥
  bad929  p = false≢true (sym (cong lower p))
  cut929 : Adequate {ℓ} ((op (op (op (var 0) (var 1)) (var 2)) (op (var 0) (var 3))) , (var 1)) → ⊥
  cut929  adequate = bad929  (Adequate.valid adequate Two boolean env9)
  env12 : ℕ → Two
  env12 zero = b1
  env12 (suc zero) = b0
  env12 (suc (suc zero)) = b0
  env12 (suc (suc (suc zero))) = b1
  env12 (suc (suc (suc (suc rest)))) = b0
  bad930 : PathP (λ _ → Two) (bop (bop (bop b1 b0) b0) (bop b1 b1)) b0 → ⊥
  bad930  p = false≢true (sym (cong lower p))
  cut930 : Adequate {ℓ} ((op (op (op (var 0) (var 1)) (var 2)) (op (var 0) (var 3))) , (var 2)) → ⊥
  cut930  adequate = bad930  (Adequate.valid adequate Two boolean env12)
  bad931 : PathP (λ _ → Two) (bop (bop (bop b0 b0) b0) (bop b0 b1)) b1 → ⊥
  bad931  p = false≢true (cong lower p)
  cut931 : Adequate {ℓ} ((op (op (op (var 0) (var 1)) (var 2)) (op (var 0) (var 3))) , (var 3)) → ⊥
  cut931  adequate = bad931  (Adequate.valid adequate Two boolean env5)
  bad932 : PathP (λ _ → Two) (bop (bop (bop b0 b0) b0) (bop b0 b0)) b1 → ⊥
  bad932  p = false≢true (cong lower p)
  cut932 : Adequate {ℓ} ((op (op (op (var 0) (var 1)) (var 2)) (op (var 0) (var 3))) , (var 4)) → ⊥
  cut932  adequate = bad932  (Adequate.valid adequate Two boolean env10)
  bad933 : PathP (λ _ → Two) (bop (bop (bop b0 b0) b1) (bop b0 b0)) b0 → ⊥
  bad933  p = false≢true (sym (cong lower p))
  cut933 : Adequate {ℓ} ((op (op (op (var 0) (var 1)) (var 2)) (op (var 1) (var 0))) , (var 0)) → ⊥
  cut933  adequate = bad933  (Adequate.valid adequate Two boolean env2)
  bad934 : PathP (λ _ → Two) (bop (bop (bop b0 b0) b1) (bop b0 b0)) b0 → ⊥
  bad934  p = false≢true (sym (cong lower p))
  cut934 : Adequate {ℓ} ((op (op (op (var 0) (var 1)) (var 2)) (op (var 1) (var 0))) , (var 1)) → ⊥
  cut934  adequate = bad934  (Adequate.valid adequate Two boolean env2)
  bad935 : PathP (λ _ → Two) (bop (bop (bop b1 b1) b0) (bop b1 b1)) b0 → ⊥
  bad935  p = false≢true (sym (cong lower p))
  cut935 : Adequate {ℓ} ((op (op (op (var 0) (var 1)) (var 2)) (op (var 1) (var 0))) , (var 2)) → ⊥
  cut935  adequate = bad935  (Adequate.valid adequate Two boolean env7)
  bad936 : PathP (λ _ → Two) (bop (bop (bop b0 b0) b0) (bop b0 b0)) b1 → ⊥
  bad936  p = false≢true (cong lower p)
  cut936 : Adequate {ℓ} ((op (op (op (var 0) (var 1)) (var 2)) (op (var 1) (var 0))) , (var 3)) → ⊥
  cut936  adequate = bad936  (Adequate.valid adequate Two boolean env5)
  bad937 : PathP (λ _ → Two) (bop (bop (bop b0 b0) b1) (bop b0 b0)) b0 → ⊥
  bad937  p = false≢true (sym (cong lower p))
  cut937 : Adequate {ℓ} ((op (op (op (var 0) (var 1)) (var 2)) (op (var 1) (var 1))) , (var 0)) → ⊥
  cut937  adequate = bad937  (Adequate.valid adequate Two boolean env2)
  bad938 : PathP (λ _ → Two) (bop (bop (bop b0 b0) b1) (bop b0 b0)) b0 → ⊥
  bad938  p = false≢true (sym (cong lower p))
  cut938 : Adequate {ℓ} ((op (op (op (var 0) (var 1)) (var 2)) (op (var 1) (var 1))) , (var 1)) → ⊥
  cut938  adequate = bad938  (Adequate.valid adequate Two boolean env2)
  bad939 : PathP (λ _ → Two) (bop (bop (bop b0 b1) b0) (bop b1 b1)) b0 → ⊥
  bad939  p = false≢true (sym (cong lower p))
  cut939 : Adequate {ℓ} ((op (op (op (var 0) (var 1)) (var 2)) (op (var 1) (var 1))) , (var 2)) → ⊥
  cut939  adequate = bad939  (Adequate.valid adequate Two boolean env4)
  bad940 : PathP (λ _ → Two) (bop (bop (bop b0 b0) b0) (bop b0 b0)) b1 → ⊥
  bad940  p = false≢true (cong lower p)
  cut940 : Adequate {ℓ} ((op (op (op (var 0) (var 1)) (var 2)) (op (var 1) (var 1))) , (var 3)) → ⊥
  cut940  adequate = bad940  (Adequate.valid adequate Two boolean env5)
  bad941 : PathP (λ _ → Two) (bop (bop (bop b0 b0) b1) (bop b0 b1)) b0 → ⊥
  bad941  p = false≢true (sym (cong lower p))
  cut941 : Adequate {ℓ} ((op (op (op (var 0) (var 1)) (var 2)) (op (var 1) (var 2))) , (var 0)) → ⊥
  cut941  adequate = bad941  (Adequate.valid adequate Two boolean env2)
  bad942 : PathP (λ _ → Two) (bop (bop (bop b0 b0) b1) (bop b0 b1)) b0 → ⊥
  bad942  p = false≢true (sym (cong lower p))
  cut942 : Adequate {ℓ} ((op (op (op (var 0) (var 1)) (var 2)) (op (var 1) (var 2))) , (var 1)) → ⊥
  cut942  adequate = bad942  (Adequate.valid adequate Two boolean env2)
  holds943 : (z0 z1 z2 : A3) → (mul3 (mul3 (mul3 z0 z1) z2) (mul3 z1 z2)) ≡ z2
  holds943 z0 z1 z2 = refl
  cut943 : Adequate {ℓ} ((op (op (op (var 0) (var 1)) (var 2)) (op (var 1) (var 2))) , (var 2)) → ⊥
  cut943  = reject3 ((op (op (op (var 0) (var 1)) (var 2)) (op (var 1) (var 2))) , (var 2)) (λ env → holds943 (env 0) (env 1) (env 2))
  bad944 : PathP (λ _ → Two) (bop (bop (bop b0 b0) b0) (bop b0 b0)) b1 → ⊥
  bad944  p = false≢true (cong lower p)
  cut944 : Adequate {ℓ} ((op (op (op (var 0) (var 1)) (var 2)) (op (var 1) (var 2))) , (var 3)) → ⊥
  cut944  adequate = bad944  (Adequate.valid adequate Two boolean env5)
  bad945 : PathP (λ _ → Two) (bop (bop (bop b0 b0) b1) (bop b0 b0)) b0 → ⊥
  bad945  p = false≢true (sym (cong lower p))
  cut945 : Adequate {ℓ} ((op (op (op (var 0) (var 1)) (var 2)) (op (var 1) (var 3))) , (var 0)) → ⊥
  cut945  adequate = bad945  (Adequate.valid adequate Two boolean env9)
  bad946 : PathP (λ _ → Two) (bop (bop (bop b0 b0) b1) (bop b0 b0)) b0 → ⊥
  bad946  p = false≢true (sym (cong lower p))
  cut946 : Adequate {ℓ} ((op (op (op (var 0) (var 1)) (var 2)) (op (var 1) (var 3))) , (var 1)) → ⊥
  cut946  adequate = bad946  (Adequate.valid adequate Two boolean env9)
  env13 : ℕ → Two
  env13 zero = b0
  env13 (suc zero) = b1
  env13 (suc (suc zero)) = b0
  env13 (suc (suc (suc zero))) = b1
  env13 (suc (suc (suc (suc rest)))) = b0
  bad947 : PathP (λ _ → Two) (bop (bop (bop b0 b1) b0) (bop b1 b1)) b0 → ⊥
  bad947  p = false≢true (sym (cong lower p))
  cut947 : Adequate {ℓ} ((op (op (op (var 0) (var 1)) (var 2)) (op (var 1) (var 3))) , (var 2)) → ⊥
  cut947  adequate = bad947  (Adequate.valid adequate Two boolean env13)
  bad948 : PathP (λ _ → Two) (bop (bop (bop b0 b0) b0) (bop b0 b1)) b1 → ⊥
  bad948  p = false≢true (cong lower p)
  cut948 : Adequate {ℓ} ((op (op (op (var 0) (var 1)) (var 2)) (op (var 1) (var 3))) , (var 3)) → ⊥
  cut948  adequate = bad948  (Adequate.valid adequate Two boolean env5)
  bad949 : PathP (λ _ → Two) (bop (bop (bop b0 b0) b0) (bop b0 b0)) b1 → ⊥
  bad949  p = false≢true (cong lower p)
  cut949 : Adequate {ℓ} ((op (op (op (var 0) (var 1)) (var 2)) (op (var 1) (var 3))) , (var 4)) → ⊥
  cut949  adequate = bad949  (Adequate.valid adequate Two boolean env10)
  bad950 : PathP (λ _ → Two) (bop (bop (bop b0 b0) b1) (bop b1 b0)) b0 → ⊥
  bad950  p = false≢true (sym (cong lower p))
  cut950 : Adequate {ℓ} ((op (op (op (var 0) (var 1)) (var 2)) (op (var 2) (var 0))) , (var 0)) → ⊥
  cut950  adequate = bad950  (Adequate.valid adequate Two boolean env2)
  bad951 : PathP (λ _ → Two) (bop (bop (bop b0 b0) b1) (bop b1 b0)) b0 → ⊥
  bad951  p = false≢true (sym (cong lower p))
  cut951 : Adequate {ℓ} ((op (op (op (var 0) (var 1)) (var 2)) (op (var 2) (var 0))) , (var 1)) → ⊥
  cut951  adequate = bad951  (Adequate.valid adequate Two boolean env2)
  holds952 : (z0 z1 z2 : A13) → (mul13 (mul13 (mul13 z0 z1) z2) (mul13 z2 z0)) ≡ z2
  holds952 m13c0 m13c0 m13c0 = refl
  holds952 m13c0 m13c0 m13c1 = refl
  holds952 m13c0 m13c0 m13c2 = refl
  holds952 m13c0 m13c0 m13c3 = refl
  holds952 m13c0 m13c1 m13c0 = refl
  holds952 m13c0 m13c1 m13c1 = refl
  holds952 m13c0 m13c1 m13c2 = refl
  holds952 m13c0 m13c1 m13c3 = refl
  holds952 m13c0 m13c2 m13c0 = refl
  holds952 m13c0 m13c2 m13c1 = refl
  holds952 m13c0 m13c2 m13c2 = refl
  holds952 m13c0 m13c2 m13c3 = refl
  holds952 m13c0 m13c3 m13c0 = refl
  holds952 m13c0 m13c3 m13c1 = refl
  holds952 m13c0 m13c3 m13c2 = refl
  holds952 m13c0 m13c3 m13c3 = refl
  holds952 m13c1 m13c0 m13c0 = refl
  holds952 m13c1 m13c0 m13c1 = refl
  holds952 m13c1 m13c0 m13c2 = refl
  holds952 m13c1 m13c0 m13c3 = refl
  holds952 m13c1 m13c1 m13c0 = refl
  holds952 m13c1 m13c1 m13c1 = refl
  holds952 m13c1 m13c1 m13c2 = refl
  holds952 m13c1 m13c1 m13c3 = refl
  holds952 m13c1 m13c2 m13c0 = refl
  holds952 m13c1 m13c2 m13c1 = refl
  holds952 m13c1 m13c2 m13c2 = refl
  holds952 m13c1 m13c2 m13c3 = refl
  holds952 m13c1 m13c3 m13c0 = refl
  holds952 m13c1 m13c3 m13c1 = refl
  holds952 m13c1 m13c3 m13c2 = refl
  holds952 m13c1 m13c3 m13c3 = refl
  holds952 m13c2 m13c0 m13c0 = refl
  holds952 m13c2 m13c0 m13c1 = refl
  holds952 m13c2 m13c0 m13c2 = refl
  holds952 m13c2 m13c0 m13c3 = refl
  holds952 m13c2 m13c1 m13c0 = refl
  holds952 m13c2 m13c1 m13c1 = refl
  holds952 m13c2 m13c1 m13c2 = refl
  holds952 m13c2 m13c1 m13c3 = refl
  holds952 m13c2 m13c2 m13c0 = refl
  holds952 m13c2 m13c2 m13c1 = refl
  holds952 m13c2 m13c2 m13c2 = refl
  holds952 m13c2 m13c2 m13c3 = refl
  holds952 m13c2 m13c3 m13c0 = refl
  holds952 m13c2 m13c3 m13c1 = refl
  holds952 m13c2 m13c3 m13c2 = refl
  holds952 m13c2 m13c3 m13c3 = refl
  holds952 m13c3 m13c0 m13c0 = refl
  holds952 m13c3 m13c0 m13c1 = refl
  holds952 m13c3 m13c0 m13c2 = refl
  holds952 m13c3 m13c0 m13c3 = refl
  holds952 m13c3 m13c1 m13c0 = refl
  holds952 m13c3 m13c1 m13c1 = refl
  holds952 m13c3 m13c1 m13c2 = refl
  holds952 m13c3 m13c1 m13c3 = refl
  holds952 m13c3 m13c2 m13c0 = refl
  holds952 m13c3 m13c2 m13c1 = refl
  holds952 m13c3 m13c2 m13c2 = refl
  holds952 m13c3 m13c2 m13c3 = refl
  holds952 m13c3 m13c3 m13c0 = refl
  holds952 m13c3 m13c3 m13c1 = refl
  holds952 m13c3 m13c3 m13c2 = refl
  holds952 m13c3 m13c3 m13c3 = refl
  cut952 : Adequate {ℓ} ((op (op (op (var 0) (var 1)) (var 2)) (op (var 2) (var 0))) , (var 2)) → ⊥
  cut952  = reject13 ((op (op (op (var 0) (var 1)) (var 2)) (op (var 2) (var 0))) , (var 2)) (λ env → holds952 (env 0) (env 1) (env 2))
  bad953 : PathP (λ _ → Two) (bop (bop (bop b0 b0) b0) (bop b0 b0)) b1 → ⊥
  bad953  p = false≢true (cong lower p)
  cut953 : Adequate {ℓ} ((op (op (op (var 0) (var 1)) (var 2)) (op (var 2) (var 0))) , (var 3)) → ⊥
  cut953  adequate = bad953  (Adequate.valid adequate Two boolean env5)
  bad954 : PathP (λ _ → Two) (bop (bop (bop b0 b0) b1) (bop b1 b0)) b0 → ⊥
  bad954  p = false≢true (sym (cong lower p))
  cut954 : Adequate {ℓ} ((op (op (op (var 0) (var 1)) (var 2)) (op (var 2) (var 1))) , (var 0)) → ⊥
  cut954  adequate = bad954  (Adequate.valid adequate Two boolean env2)
  bad955 : PathP (λ _ → Two) (bop (bop (bop b0 b0) b1) (bop b1 b0)) b0 → ⊥
  bad955  p = false≢true (sym (cong lower p))
  cut955 : Adequate {ℓ} ((op (op (op (var 0) (var 1)) (var 2)) (op (var 2) (var 1))) , (var 1)) → ⊥
  cut955  adequate = bad955  (Adequate.valid adequate Two boolean env2)
  holds956 : (z0 z1 z2 : A13) → (mul13 (mul13 (mul13 z0 z1) z2) (mul13 z2 z1)) ≡ z2
  holds956 m13c0 m13c0 m13c0 = refl
  holds956 m13c0 m13c0 m13c1 = refl
  holds956 m13c0 m13c0 m13c2 = refl
  holds956 m13c0 m13c0 m13c3 = refl
  holds956 m13c0 m13c1 m13c0 = refl
  holds956 m13c0 m13c1 m13c1 = refl
  holds956 m13c0 m13c1 m13c2 = refl
  holds956 m13c0 m13c1 m13c3 = refl
  holds956 m13c0 m13c2 m13c0 = refl
  holds956 m13c0 m13c2 m13c1 = refl
  holds956 m13c0 m13c2 m13c2 = refl
  holds956 m13c0 m13c2 m13c3 = refl
  holds956 m13c0 m13c3 m13c0 = refl
  holds956 m13c0 m13c3 m13c1 = refl
  holds956 m13c0 m13c3 m13c2 = refl
  holds956 m13c0 m13c3 m13c3 = refl
  holds956 m13c1 m13c0 m13c0 = refl
  holds956 m13c1 m13c0 m13c1 = refl
  holds956 m13c1 m13c0 m13c2 = refl
  holds956 m13c1 m13c0 m13c3 = refl
  holds956 m13c1 m13c1 m13c0 = refl
  holds956 m13c1 m13c1 m13c1 = refl
  holds956 m13c1 m13c1 m13c2 = refl
  holds956 m13c1 m13c1 m13c3 = refl
  holds956 m13c1 m13c2 m13c0 = refl
  holds956 m13c1 m13c2 m13c1 = refl
  holds956 m13c1 m13c2 m13c2 = refl
  holds956 m13c1 m13c2 m13c3 = refl
  holds956 m13c1 m13c3 m13c0 = refl
  holds956 m13c1 m13c3 m13c1 = refl
  holds956 m13c1 m13c3 m13c2 = refl
  holds956 m13c1 m13c3 m13c3 = refl
  holds956 m13c2 m13c0 m13c0 = refl
  holds956 m13c2 m13c0 m13c1 = refl
  holds956 m13c2 m13c0 m13c2 = refl
  holds956 m13c2 m13c0 m13c3 = refl
  holds956 m13c2 m13c1 m13c0 = refl
  holds956 m13c2 m13c1 m13c1 = refl
  holds956 m13c2 m13c1 m13c2 = refl
  holds956 m13c2 m13c1 m13c3 = refl
  holds956 m13c2 m13c2 m13c0 = refl
  holds956 m13c2 m13c2 m13c1 = refl
  holds956 m13c2 m13c2 m13c2 = refl
  holds956 m13c2 m13c2 m13c3 = refl
  holds956 m13c2 m13c3 m13c0 = refl
  holds956 m13c2 m13c3 m13c1 = refl
  holds956 m13c2 m13c3 m13c2 = refl
  holds956 m13c2 m13c3 m13c3 = refl
  holds956 m13c3 m13c0 m13c0 = refl
  holds956 m13c3 m13c0 m13c1 = refl
  holds956 m13c3 m13c0 m13c2 = refl
  holds956 m13c3 m13c0 m13c3 = refl
  holds956 m13c3 m13c1 m13c0 = refl
  holds956 m13c3 m13c1 m13c1 = refl
  holds956 m13c3 m13c1 m13c2 = refl
  holds956 m13c3 m13c1 m13c3 = refl
  holds956 m13c3 m13c2 m13c0 = refl
  holds956 m13c3 m13c2 m13c1 = refl
  holds956 m13c3 m13c2 m13c2 = refl
  holds956 m13c3 m13c2 m13c3 = refl
  holds956 m13c3 m13c3 m13c0 = refl
  holds956 m13c3 m13c3 m13c1 = refl
  holds956 m13c3 m13c3 m13c2 = refl
  holds956 m13c3 m13c3 m13c3 = refl
  cut956 : Adequate {ℓ} ((op (op (op (var 0) (var 1)) (var 2)) (op (var 2) (var 1))) , (var 2)) → ⊥
  cut956  = reject13 ((op (op (op (var 0) (var 1)) (var 2)) (op (var 2) (var 1))) , (var 2)) (λ env → holds956 (env 0) (env 1) (env 2))
  bad957 : PathP (λ _ → Two) (bop (bop (bop b0 b0) b0) (bop b0 b0)) b1 → ⊥
  bad957  p = false≢true (cong lower p)
  cut957 : Adequate {ℓ} ((op (op (op (var 0) (var 1)) (var 2)) (op (var 2) (var 1))) , (var 3)) → ⊥
  cut957  adequate = bad957  (Adequate.valid adequate Two boolean env5)
  bad958 : PathP (λ _ → Two) (bop (bop (bop b0 b0) b1) (bop b1 b1)) b0 → ⊥
  bad958  p = false≢true (sym (cong lower p))
  cut958 : Adequate {ℓ} ((op (op (op (var 0) (var 1)) (var 2)) (op (var 2) (var 2))) , (var 0)) → ⊥
  cut958  adequate = bad958  (Adequate.valid adequate Two boolean env2)
  bad959 : PathP (λ _ → Two) (bop (bop (bop b0 b0) b1) (bop b1 b1)) b0 → ⊥
  bad959  p = false≢true (sym (cong lower p))
  cut959 : Adequate {ℓ} ((op (op (op (var 0) (var 1)) (var 2)) (op (var 2) (var 2))) , (var 1)) → ⊥
  cut959  adequate = bad959  (Adequate.valid adequate Two boolean env2)
  holds960 : (z0 z1 z2 : A3) → (mul3 (mul3 (mul3 z0 z1) z2) (mul3 z2 z2)) ≡ z2
  holds960 z0 z1 z2 = refl
  cut960 : Adequate {ℓ} ((op (op (op (var 0) (var 1)) (var 2)) (op (var 2) (var 2))) , (var 2)) → ⊥
  cut960  = reject3 ((op (op (op (var 0) (var 1)) (var 2)) (op (var 2) (var 2))) , (var 2)) (λ env → holds960 (env 0) (env 1) (env 2))
  bad961 : PathP (λ _ → Two) (bop (bop (bop b0 b0) b0) (bop b0 b0)) b1 → ⊥
  bad961  p = false≢true (cong lower p)
  cut961 : Adequate {ℓ} ((op (op (op (var 0) (var 1)) (var 2)) (op (var 2) (var 2))) , (var 3)) → ⊥
  cut961  adequate = bad961  (Adequate.valid adequate Two boolean env5)
  bad962 : PathP (λ _ → Two) (bop (bop (bop b0 b0) b1) (bop b1 b0)) b0 → ⊥
  bad962  p = false≢true (sym (cong lower p))
  cut962 : Adequate {ℓ} ((op (op (op (var 0) (var 1)) (var 2)) (op (var 2) (var 3))) , (var 0)) → ⊥
  cut962  adequate = bad962  (Adequate.valid adequate Two boolean env9)
  bad963 : PathP (λ _ → Two) (bop (bop (bop b0 b0) b1) (bop b1 b0)) b0 → ⊥
  bad963  p = false≢true (sym (cong lower p))
  cut963 : Adequate {ℓ} ((op (op (op (var 0) (var 1)) (var 2)) (op (var 2) (var 3))) , (var 1)) → ⊥
  cut963  adequate = bad963  (Adequate.valid adequate Two boolean env9)
  env14 : ℕ → Two
  env14 zero = b1
  env14 (suc zero) = b1
  env14 (suc (suc zero)) = b1
  env14 (suc (suc (suc zero))) = b0
  env14 (suc (suc (suc (suc rest)))) = b0
  bad964 : PathP (λ _ → Two) (bop (bop (bop b1 b1) b1) (bop b1 b0)) b1 → ⊥
  bad964  p = false≢true (cong lower p)
  cut964 : Adequate {ℓ} ((op (op (op (var 0) (var 1)) (var 2)) (op (var 2) (var 3))) , (var 2)) → ⊥
  cut964  adequate = bad964  (Adequate.valid adequate Two boolean env14)
  bad965 : PathP (λ _ → Two) (bop (bop (bop b0 b0) b0) (bop b0 b1)) b1 → ⊥
  bad965  p = false≢true (cong lower p)
  cut965 : Adequate {ℓ} ((op (op (op (var 0) (var 1)) (var 2)) (op (var 2) (var 3))) , (var 3)) → ⊥
  cut965  adequate = bad965  (Adequate.valid adequate Two boolean env5)
  bad966 : PathP (λ _ → Two) (bop (bop (bop b0 b0) b0) (bop b0 b0)) b1 → ⊥
  bad966  p = false≢true (cong lower p)
  cut966 : Adequate {ℓ} ((op (op (op (var 0) (var 1)) (var 2)) (op (var 2) (var 3))) , (var 4)) → ⊥
  cut966  adequate = bad966  (Adequate.valid adequate Two boolean env10)
  bad967 : PathP (λ _ → Two) (bop (bop (bop b0 b0) b1) (bop b0 b0)) b0 → ⊥
  bad967  p = false≢true (sym (cong lower p))
  cut967 : Adequate {ℓ} ((op (op (op (var 0) (var 1)) (var 2)) (op (var 3) (var 0))) , (var 0)) → ⊥
  cut967  adequate = bad967  (Adequate.valid adequate Two boolean env9)
  bad968 : PathP (λ _ → Two) (bop (bop (bop b0 b0) b1) (bop b0 b0)) b0 → ⊥
  bad968  p = false≢true (sym (cong lower p))
  cut968 : Adequate {ℓ} ((op (op (op (var 0) (var 1)) (var 2)) (op (var 3) (var 0))) , (var 1)) → ⊥
  cut968  adequate = bad968  (Adequate.valid adequate Two boolean env9)
  bad969 : PathP (λ _ → Two) (bop (bop (bop b1 b0) b0) (bop b1 b1)) b0 → ⊥
  bad969  p = false≢true (sym (cong lower p))
  cut969 : Adequate {ℓ} ((op (op (op (var 0) (var 1)) (var 2)) (op (var 3) (var 0))) , (var 2)) → ⊥
  cut969  adequate = bad969  (Adequate.valid adequate Two boolean env12)
  bad970 : PathP (λ _ → Two) (bop (bop (bop b0 b0) b0) (bop b1 b0)) b1 → ⊥
  bad970  p = false≢true (cong lower p)
  cut970 : Adequate {ℓ} ((op (op (op (var 0) (var 1)) (var 2)) (op (var 3) (var 0))) , (var 3)) → ⊥
  cut970  adequate = bad970  (Adequate.valid adequate Two boolean env5)
  bad971 : PathP (λ _ → Two) (bop (bop (bop b0 b0) b0) (bop b0 b0)) b1 → ⊥
  bad971  p = false≢true (cong lower p)
  cut971 : Adequate {ℓ} ((op (op (op (var 0) (var 1)) (var 2)) (op (var 3) (var 0))) , (var 4)) → ⊥
  cut971  adequate = bad971  (Adequate.valid adequate Two boolean env10)
  bad972 : PathP (λ _ → Two) (bop (bop (bop b0 b0) b1) (bop b0 b0)) b0 → ⊥
  bad972  p = false≢true (sym (cong lower p))
  cut972 : Adequate {ℓ} ((op (op (op (var 0) (var 1)) (var 2)) (op (var 3) (var 1))) , (var 0)) → ⊥
  cut972  adequate = bad972  (Adequate.valid adequate Two boolean env9)
  bad973 : PathP (λ _ → Two) (bop (bop (bop b0 b0) b1) (bop b0 b0)) b0 → ⊥
  bad973  p = false≢true (sym (cong lower p))
  cut973 : Adequate {ℓ} ((op (op (op (var 0) (var 1)) (var 2)) (op (var 3) (var 1))) , (var 1)) → ⊥
  cut973  adequate = bad973  (Adequate.valid adequate Two boolean env9)
  bad974 : PathP (λ _ → Two) (bop (bop (bop b0 b1) b0) (bop b1 b1)) b0 → ⊥
  bad974  p = false≢true (sym (cong lower p))
  cut974 : Adequate {ℓ} ((op (op (op (var 0) (var 1)) (var 2)) (op (var 3) (var 1))) , (var 2)) → ⊥
  cut974  adequate = bad974  (Adequate.valid adequate Two boolean env13)
  bad975 : PathP (λ _ → Two) (bop (bop (bop b0 b0) b0) (bop b1 b0)) b1 → ⊥
  bad975  p = false≢true (cong lower p)
  cut975 : Adequate {ℓ} ((op (op (op (var 0) (var 1)) (var 2)) (op (var 3) (var 1))) , (var 3)) → ⊥
  cut975  adequate = bad975  (Adequate.valid adequate Two boolean env5)
  bad976 : PathP (λ _ → Two) (bop (bop (bop b0 b0) b0) (bop b0 b0)) b1 → ⊥
  bad976  p = false≢true (cong lower p)
  cut976 : Adequate {ℓ} ((op (op (op (var 0) (var 1)) (var 2)) (op (var 3) (var 1))) , (var 4)) → ⊥
  cut976  adequate = bad976  (Adequate.valid adequate Two boolean env10)
  bad977 : PathP (λ _ → Two) (bop (bop (bop b0 b0) b1) (bop b0 b1)) b0 → ⊥
  bad977  p = false≢true (sym (cong lower p))
  cut977 : Adequate {ℓ} ((op (op (op (var 0) (var 1)) (var 2)) (op (var 3) (var 2))) , (var 0)) → ⊥
  cut977  adequate = bad977  (Adequate.valid adequate Two boolean env9)
  bad978 : PathP (λ _ → Two) (bop (bop (bop b0 b0) b1) (bop b0 b1)) b0 → ⊥
  bad978  p = false≢true (sym (cong lower p))
  cut978 : Adequate {ℓ} ((op (op (op (var 0) (var 1)) (var 2)) (op (var 3) (var 2))) , (var 1)) → ⊥
  cut978  adequate = bad978  (Adequate.valid adequate Two boolean env9)
  bad979 : PathP (λ _ → Two) (bop (bop (bop b1 b1) b1) (bop b0 b1)) b1 → ⊥
  bad979  p = false≢true (cong lower p)
  cut979 : Adequate {ℓ} ((op (op (op (var 0) (var 1)) (var 2)) (op (var 3) (var 2))) , (var 2)) → ⊥
  cut979  adequate = bad979  (Adequate.valid adequate Two boolean env14)
  bad980 : PathP (λ _ → Two) (bop (bop (bop b0 b0) b0) (bop b1 b0)) b1 → ⊥
  bad980  p = false≢true (cong lower p)
  cut980 : Adequate {ℓ} ((op (op (op (var 0) (var 1)) (var 2)) (op (var 3) (var 2))) , (var 3)) → ⊥
  cut980  adequate = bad980  (Adequate.valid adequate Two boolean env5)
  bad981 : PathP (λ _ → Two) (bop (bop (bop b0 b0) b0) (bop b0 b0)) b1 → ⊥
  bad981  p = false≢true (cong lower p)
  cut981 : Adequate {ℓ} ((op (op (op (var 0) (var 1)) (var 2)) (op (var 3) (var 2))) , (var 4)) → ⊥
  cut981  adequate = bad981  (Adequate.valid adequate Two boolean env10)
  bad982 : PathP (λ _ → Two) (bop (bop (bop b0 b0) b0) (bop b1 b1)) b0 → ⊥
  bad982  p = false≢true (sym (cong lower p))
  cut982 : Adequate {ℓ} ((op (op (op (var 0) (var 1)) (var 2)) (op (var 3) (var 3))) , (var 0)) → ⊥
  cut982  adequate = bad982  (Adequate.valid adequate Two boolean env5)
  bad983 : PathP (λ _ → Two) (bop (bop (bop b0 b0) b0) (bop b1 b1)) b0 → ⊥
  bad983  p = false≢true (sym (cong lower p))
  cut983 : Adequate {ℓ} ((op (op (op (var 0) (var 1)) (var 2)) (op (var 3) (var 3))) , (var 1)) → ⊥
  cut983  adequate = bad983  (Adequate.valid adequate Two boolean env5)
  bad984 : PathP (λ _ → Two) (bop (bop (bop b0 b0) b0) (bop b1 b1)) b0 → ⊥
  bad984  p = false≢true (sym (cong lower p))
  cut984 : Adequate {ℓ} ((op (op (op (var 0) (var 1)) (var 2)) (op (var 3) (var 3))) , (var 2)) → ⊥
  cut984  adequate = bad984  (Adequate.valid adequate Two boolean env5)
  bad985 : PathP (λ _ → Two) (bop (bop (bop b0 b0) b1) (bop b0 b0)) b0 → ⊥
  bad985  p = false≢true (sym (cong lower p))
  cut985 : Adequate {ℓ} ((op (op (op (var 0) (var 1)) (var 2)) (op (var 3) (var 3))) , (var 3)) → ⊥
  cut985  adequate = bad985  (Adequate.valid adequate Two boolean env9)
  bad986 : PathP (λ _ → Two) (bop (bop (bop b0 b0) b0) (bop b0 b0)) b1 → ⊥
  bad986  p = false≢true (cong lower p)
  cut986 : Adequate {ℓ} ((op (op (op (var 0) (var 1)) (var 2)) (op (var 3) (var 3))) , (var 4)) → ⊥
  cut986  adequate = bad986  (Adequate.valid adequate Two boolean env10)
  env15 : ℕ → Two
  env15 zero = b0
  env15 (suc zero) = b0
  env15 (suc (suc zero)) = b0
  env15 (suc (suc (suc zero))) = b1
  env15 (suc (suc (suc (suc zero)))) = b1
  env15 (suc (suc (suc (suc (suc rest))))) = b0
  bad987 : PathP (λ _ → Two) (bop (bop (bop b0 b0) b0) (bop b1 b1)) b0 → ⊥
  bad987  p = false≢true (sym (cong lower p))
  cut987 : Adequate {ℓ} ((op (op (op (var 0) (var 1)) (var 2)) (op (var 3) (var 4))) , (var 0)) → ⊥
  cut987  adequate = bad987  (Adequate.valid adequate Two boolean env15)
  bad988 : PathP (λ _ → Two) (bop (bop (bop b0 b0) b0) (bop b1 b1)) b0 → ⊥
  bad988  p = false≢true (sym (cong lower p))
  cut988 : Adequate {ℓ} ((op (op (op (var 0) (var 1)) (var 2)) (op (var 3) (var 4))) , (var 1)) → ⊥
  cut988  adequate = bad988  (Adequate.valid adequate Two boolean env15)
  bad989 : PathP (λ _ → Two) (bop (bop (bop b0 b0) b0) (bop b1 b1)) b0 → ⊥
  bad989  p = false≢true (sym (cong lower p))
  cut989 : Adequate {ℓ} ((op (op (op (var 0) (var 1)) (var 2)) (op (var 3) (var 4))) , (var 2)) → ⊥
  cut989  adequate = bad989  (Adequate.valid adequate Two boolean env15)
  env16 : ℕ → Two
  env16 zero = b0
  env16 (suc zero) = b0
  env16 (suc (suc zero)) = b0
  env16 (suc (suc (suc zero))) = b1
  env16 (suc (suc (suc (suc zero)))) = b0
  env16 (suc (suc (suc (suc (suc rest))))) = b0
  bad990 : PathP (λ _ → Two) (bop (bop (bop b0 b0) b0) (bop b1 b0)) b1 → ⊥
  bad990  p = false≢true (cong lower p)
  cut990 : Adequate {ℓ} ((op (op (op (var 0) (var 1)) (var 2)) (op (var 3) (var 4))) , (var 3)) → ⊥
  cut990  adequate = bad990  (Adequate.valid adequate Two boolean env16)
  bad991 : PathP (λ _ → Two) (bop (bop (bop b0 b0) b0) (bop b0 b1)) b1 → ⊥
  bad991  p = false≢true (cong lower p)
  cut991 : Adequate {ℓ} ((op (op (op (var 0) (var 1)) (var 2)) (op (var 3) (var 4))) , (var 4)) → ⊥
  cut991  adequate = bad991  (Adequate.valid adequate Two boolean env10)
  env17 : ℕ → Two
  env17 zero = b0
  env17 (suc zero) = b0
  env17 (suc (suc zero)) = b0
  env17 (suc (suc (suc zero))) = b0
  env17 (suc (suc (suc (suc zero)))) = b0
  env17 (suc (suc (suc (suc (suc zero))))) = b1
  env17 (suc (suc (suc (suc (suc (suc rest)))))) = b0
  bad992 : PathP (λ _ → Two) (bop (bop (bop b0 b0) b0) (bop b0 b0)) b1 → ⊥
  bad992  p = false≢true (cong lower p)
  cut992 : Adequate {ℓ} ((op (op (op (var 0) (var 1)) (var 2)) (op (var 3) (var 4))) , (var 5)) → ⊥
  cut992  adequate = bad992  (Adequate.valid adequate Two boolean env17)
