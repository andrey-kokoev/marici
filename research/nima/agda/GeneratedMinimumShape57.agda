{-# OPTIONS --safe --cubical --guardedness #-}
module GeneratedMinimumShape57 where
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
  holds587 : (z0 : A1) → (mul1 (mul1 z0 (mul1 z0 z0)) (mul1 z0 z0)) ≡ z0
  holds587 m1c0 = refl
  holds587 m1c1 = refl
  cut587 : Adequate {ℓ} ((op (op (var 0) (op (var 0) (var 0))) (op (var 0) (var 0))) , (var 0)) → ⊥
  cut587  = reject1 ((op (op (var 0) (op (var 0) (var 0))) (op (var 0) (var 0))) , (var 0)) (λ env → holds587 (env 0))
  env0 : ℕ → Two
  env0 zero = b0
  env0 (suc zero) = b1
  env0 (suc (suc rest)) = b0
  bad588 : PathP (λ _ → Two) (bop (bop b0 (bop b0 b0)) (bop b0 b0)) b1 → ⊥
  bad588  p = false≢true (cong lower p)
  cut588 : Adequate {ℓ} ((op (op (var 0) (op (var 0) (var 0))) (op (var 0) (var 0))) , (var 1)) → ⊥
  cut588  adequate = bad588  (Adequate.valid adequate Two boolean env0)
  env1 : ℕ → Two
  env1 zero = b1
  env1 (suc zero) = b0
  env1 (suc (suc rest)) = b0
  bad589 : PathP (λ _ → Two) (bop (bop b1 (bop b1 b1)) (bop b1 b0)) b1 → ⊥
  bad589  p = false≢true (cong lower p)
  cut589 : Adequate {ℓ} ((op (op (var 0) (op (var 0) (var 0))) (op (var 0) (var 1))) , (var 0)) → ⊥
  cut589  adequate = bad589  (Adequate.valid adequate Two boolean env1)
  bad590 : PathP (λ _ → Two) (bop (bop b0 (bop b0 b0)) (bop b0 b1)) b1 → ⊥
  bad590  p = false≢true (cong lower p)
  cut590 : Adequate {ℓ} ((op (op (var 0) (op (var 0) (var 0))) (op (var 0) (var 1))) , (var 1)) → ⊥
  cut590  adequate = bad590  (Adequate.valid adequate Two boolean env0)
  env2 : ℕ → Two
  env2 zero = b0
  env2 (suc zero) = b0
  env2 (suc (suc zero)) = b1
  env2 (suc (suc (suc rest))) = b0
  bad591 : PathP (λ _ → Two) (bop (bop b0 (bop b0 b0)) (bop b0 b0)) b1 → ⊥
  bad591  p = false≢true (cong lower p)
  cut591 : Adequate {ℓ} ((op (op (var 0) (op (var 0) (var 0))) (op (var 0) (var 1))) , (var 2)) → ⊥
  cut591  adequate = bad591  (Adequate.valid adequate Two boolean env2)
  bad592 : PathP (λ _ → Two) (bop (bop b1 (bop b1 b1)) (bop b0 b1)) b1 → ⊥
  bad592  p = false≢true (cong lower p)
  cut592 : Adequate {ℓ} ((op (op (var 0) (op (var 0) (var 0))) (op (var 1) (var 0))) , (var 0)) → ⊥
  cut592  adequate = bad592  (Adequate.valid adequate Two boolean env1)
  bad593 : PathP (λ _ → Two) (bop (bop b0 (bop b0 b0)) (bop b1 b0)) b1 → ⊥
  bad593  p = false≢true (cong lower p)
  cut593 : Adequate {ℓ} ((op (op (var 0) (op (var 0) (var 0))) (op (var 1) (var 0))) , (var 1)) → ⊥
  cut593  adequate = bad593  (Adequate.valid adequate Two boolean env0)
  bad594 : PathP (λ _ → Two) (bop (bop b0 (bop b0 b0)) (bop b0 b0)) b1 → ⊥
  bad594  p = false≢true (cong lower p)
  cut594 : Adequate {ℓ} ((op (op (var 0) (op (var 0) (var 0))) (op (var 1) (var 0))) , (var 2)) → ⊥
  cut594  adequate = bad594  (Adequate.valid adequate Two boolean env2)
  bad595 : PathP (λ _ → Two) (bop (bop b0 (bop b0 b0)) (bop b1 b1)) b0 → ⊥
  bad595  p = false≢true (sym (cong lower p))
  cut595 : Adequate {ℓ} ((op (op (var 0) (op (var 0) (var 0))) (op (var 1) (var 1))) , (var 0)) → ⊥
  cut595  adequate = bad595  (Adequate.valid adequate Two boolean env0)
  holds596 : (z0 z1 : A3) → (mul3 (mul3 z0 (mul3 z0 z0)) (mul3 z1 z1)) ≡ z1
  holds596 z0 z1 = refl
  cut596 : Adequate {ℓ} ((op (op (var 0) (op (var 0) (var 0))) (op (var 1) (var 1))) , (var 1)) → ⊥
  cut596  = reject3 ((op (op (var 0) (op (var 0) (var 0))) (op (var 1) (var 1))) , (var 1)) (λ env → holds596 (env 0) (env 1))
  bad597 : PathP (λ _ → Two) (bop (bop b0 (bop b0 b0)) (bop b0 b0)) b1 → ⊥
  bad597  p = false≢true (cong lower p)
  cut597 : Adequate {ℓ} ((op (op (var 0) (op (var 0) (var 0))) (op (var 1) (var 1))) , (var 2)) → ⊥
  cut597  adequate = bad597  (Adequate.valid adequate Two boolean env2)
  env3 : ℕ → Two
  env3 zero = b0
  env3 (suc zero) = b1
  env3 (suc (suc zero)) = b1
  env3 (suc (suc (suc rest))) = b0
  bad598 : PathP (λ _ → Two) (bop (bop b0 (bop b0 b0)) (bop b1 b1)) b0 → ⊥
  bad598  p = false≢true (sym (cong lower p))
  cut598 : Adequate {ℓ} ((op (op (var 0) (op (var 0) (var 0))) (op (var 1) (var 2))) , (var 0)) → ⊥
  cut598  adequate = bad598  (Adequate.valid adequate Two boolean env3)
  env4 : ℕ → Two
  env4 zero = b0
  env4 (suc zero) = b1
  env4 (suc (suc zero)) = b0
  env4 (suc (suc (suc rest))) = b0
  bad599 : PathP (λ _ → Two) (bop (bop b0 (bop b0 b0)) (bop b1 b0)) b1 → ⊥
  bad599  p = false≢true (cong lower p)
  cut599 : Adequate {ℓ} ((op (op (var 0) (op (var 0) (var 0))) (op (var 1) (var 2))) , (var 1)) → ⊥
  cut599  adequate = bad599  (Adequate.valid adequate Two boolean env4)
  bad600 : PathP (λ _ → Two) (bop (bop b0 (bop b0 b0)) (bop b0 b1)) b1 → ⊥
  bad600  p = false≢true (cong lower p)
  cut600 : Adequate {ℓ} ((op (op (var 0) (op (var 0) (var 0))) (op (var 1) (var 2))) , (var 2)) → ⊥
  cut600  adequate = bad600  (Adequate.valid adequate Two boolean env2)
  env5 : ℕ → Two
  env5 zero = b0
  env5 (suc zero) = b0
  env5 (suc (suc zero)) = b0
  env5 (suc (suc (suc zero))) = b1
  env5 (suc (suc (suc (suc rest)))) = b0
  bad601 : PathP (λ _ → Two) (bop (bop b0 (bop b0 b0)) (bop b0 b0)) b1 → ⊥
  bad601  p = false≢true (cong lower p)
  cut601 : Adequate {ℓ} ((op (op (var 0) (op (var 0) (var 0))) (op (var 1) (var 2))) , (var 3)) → ⊥
  cut601  adequate = bad601  (Adequate.valid adequate Two boolean env5)
  holds602 : (z0 z1 : A2) → (mul2 (mul2 z0 (mul2 z0 z1)) (mul2 z0 z0)) ≡ z0
  holds602 z0 z1 = refl
  cut602 : Adequate {ℓ} ((op (op (var 0) (op (var 0) (var 1))) (op (var 0) (var 0))) , (var 0)) → ⊥
  cut602  = reject2 ((op (op (var 0) (op (var 0) (var 1))) (op (var 0) (var 0))) , (var 0)) (λ env → holds602 (env 0) (env 1))
  bad603 : PathP (λ _ → Two) (bop (bop b0 (bop b0 b1)) (bop b0 b0)) b1 → ⊥
  bad603  p = false≢true (cong lower p)
  cut603 : Adequate {ℓ} ((op (op (var 0) (op (var 0) (var 1))) (op (var 0) (var 0))) , (var 1)) → ⊥
  cut603  adequate = bad603  (Adequate.valid adequate Two boolean env0)
  bad604 : PathP (λ _ → Two) (bop (bop b0 (bop b0 b0)) (bop b0 b0)) b1 → ⊥
  bad604  p = false≢true (cong lower p)
  cut604 : Adequate {ℓ} ((op (op (var 0) (op (var 0) (var 1))) (op (var 0) (var 0))) , (var 2)) → ⊥
  cut604  adequate = bad604  (Adequate.valid adequate Two boolean env2)
  holds605 : (z0 z1 : A2) → (mul2 (mul2 z0 (mul2 z0 z1)) (mul2 z0 z1)) ≡ z0
  holds605 z0 z1 = refl
  cut605 : Adequate {ℓ} ((op (op (var 0) (op (var 0) (var 1))) (op (var 0) (var 1))) , (var 0)) → ⊥
  cut605  = reject2 ((op (op (var 0) (op (var 0) (var 1))) (op (var 0) (var 1))) , (var 0)) (λ env → holds605 (env 0) (env 1))
  bad606 : PathP (λ _ → Two) (bop (bop b0 (bop b0 b1)) (bop b0 b1)) b1 → ⊥
  bad606  p = false≢true (cong lower p)
  cut606 : Adequate {ℓ} ((op (op (var 0) (op (var 0) (var 1))) (op (var 0) (var 1))) , (var 1)) → ⊥
  cut606  adequate = bad606  (Adequate.valid adequate Two boolean env0)
  bad607 : PathP (λ _ → Two) (bop (bop b0 (bop b0 b0)) (bop b0 b0)) b1 → ⊥
  bad607  p = false≢true (cong lower p)
  cut607 : Adequate {ℓ} ((op (op (var 0) (op (var 0) (var 1))) (op (var 0) (var 1))) , (var 2)) → ⊥
  cut607  adequate = bad607  (Adequate.valid adequate Two boolean env2)
  env6 : ℕ → Two
  env6 zero = b1
  env6 (suc zero) = b1
  env6 (suc (suc zero)) = b0
  env6 (suc (suc (suc rest))) = b0
  bad608 : PathP (λ _ → Two) (bop (bop b1 (bop b1 b1)) (bop b1 b0)) b1 → ⊥
  bad608  p = false≢true (cong lower p)
  cut608 : Adequate {ℓ} ((op (op (var 0) (op (var 0) (var 1))) (op (var 0) (var 2))) , (var 0)) → ⊥
  cut608  adequate = bad608  (Adequate.valid adequate Two boolean env6)
  bad609 : PathP (λ _ → Two) (bop (bop b0 (bop b0 b1)) (bop b0 b0)) b1 → ⊥
  bad609  p = false≢true (cong lower p)
  cut609 : Adequate {ℓ} ((op (op (var 0) (op (var 0) (var 1))) (op (var 0) (var 2))) , (var 1)) → ⊥
  cut609  adequate = bad609  (Adequate.valid adequate Two boolean env4)
  bad610 : PathP (λ _ → Two) (bop (bop b0 (bop b0 b0)) (bop b0 b1)) b1 → ⊥
  bad610  p = false≢true (cong lower p)
  cut610 : Adequate {ℓ} ((op (op (var 0) (op (var 0) (var 1))) (op (var 0) (var 2))) , (var 2)) → ⊥
  cut610  adequate = bad610  (Adequate.valid adequate Two boolean env2)
  bad611 : PathP (λ _ → Two) (bop (bop b0 (bop b0 b0)) (bop b0 b0)) b1 → ⊥
  bad611  p = false≢true (cong lower p)
  cut611 : Adequate {ℓ} ((op (op (var 0) (op (var 0) (var 1))) (op (var 0) (var 2))) , (var 3)) → ⊥
  cut611  adequate = bad611  (Adequate.valid adequate Two boolean env5)
  holds612 : (z0 z1 : A2) → (mul2 (mul2 z0 (mul2 z0 z1)) (mul2 z1 z0)) ≡ z0
  holds612 z0 z1 = refl
  cut612 : Adequate {ℓ} ((op (op (var 0) (op (var 0) (var 1))) (op (var 1) (var 0))) , (var 0)) → ⊥
  cut612  = reject2 ((op (op (var 0) (op (var 0) (var 1))) (op (var 1) (var 0))) , (var 0)) (λ env → holds612 (env 0) (env 1))
  bad613 : PathP (λ _ → Two) (bop (bop b0 (bop b0 b1)) (bop b1 b0)) b1 → ⊥
  bad613  p = false≢true (cong lower p)
  cut613 : Adequate {ℓ} ((op (op (var 0) (op (var 0) (var 1))) (op (var 1) (var 0))) , (var 1)) → ⊥
  cut613  adequate = bad613  (Adequate.valid adequate Two boolean env0)
  bad614 : PathP (λ _ → Two) (bop (bop b0 (bop b0 b0)) (bop b0 b0)) b1 → ⊥
  bad614  p = false≢true (cong lower p)
  cut614 : Adequate {ℓ} ((op (op (var 0) (op (var 0) (var 1))) (op (var 1) (var 0))) , (var 2)) → ⊥
  cut614  adequate = bad614  (Adequate.valid adequate Two boolean env2)
  bad615 : PathP (λ _ → Two) (bop (bop b0 (bop b0 b1)) (bop b1 b1)) b0 → ⊥
  bad615  p = false≢true (sym (cong lower p))
  cut615 : Adequate {ℓ} ((op (op (var 0) (op (var 0) (var 1))) (op (var 1) (var 1))) , (var 0)) → ⊥
  cut615  adequate = bad615  (Adequate.valid adequate Two boolean env0)
  bad616 : PathP (λ _ → Two) (bop (bop b1 (bop b1 b0)) (bop b0 b0)) b0 → ⊥
  bad616  p = false≢true (sym (cong lower p))
  cut616 : Adequate {ℓ} ((op (op (var 0) (op (var 0) (var 1))) (op (var 1) (var 1))) , (var 1)) → ⊥
  cut616  adequate = bad616  (Adequate.valid adequate Two boolean env1)
  bad617 : PathP (λ _ → Two) (bop (bop b0 (bop b0 b0)) (bop b0 b0)) b1 → ⊥
  bad617  p = false≢true (cong lower p)
  cut617 : Adequate {ℓ} ((op (op (var 0) (op (var 0) (var 1))) (op (var 1) (var 1))) , (var 2)) → ⊥
  cut617  adequate = bad617  (Adequate.valid adequate Two boolean env2)
  bad618 : PathP (λ _ → Two) (bop (bop b0 (bop b0 b1)) (bop b1 b1)) b0 → ⊥
  bad618  p = false≢true (sym (cong lower p))
  cut618 : Adequate {ℓ} ((op (op (var 0) (op (var 0) (var 1))) (op (var 1) (var 2))) , (var 0)) → ⊥
  cut618  adequate = bad618  (Adequate.valid adequate Two boolean env3)
  bad619 : PathP (λ _ → Two) (bop (bop b0 (bop b0 b1)) (bop b1 b0)) b1 → ⊥
  bad619  p = false≢true (cong lower p)
  cut619 : Adequate {ℓ} ((op (op (var 0) (op (var 0) (var 1))) (op (var 1) (var 2))) , (var 1)) → ⊥
  cut619  adequate = bad619  (Adequate.valid adequate Two boolean env4)
  bad620 : PathP (λ _ → Two) (bop (bop b0 (bop b0 b0)) (bop b0 b1)) b1 → ⊥
  bad620  p = false≢true (cong lower p)
  cut620 : Adequate {ℓ} ((op (op (var 0) (op (var 0) (var 1))) (op (var 1) (var 2))) , (var 2)) → ⊥
  cut620  adequate = bad620  (Adequate.valid adequate Two boolean env2)
  bad621 : PathP (λ _ → Two) (bop (bop b0 (bop b0 b0)) (bop b0 b0)) b1 → ⊥
  bad621  p = false≢true (cong lower p)
  cut621 : Adequate {ℓ} ((op (op (var 0) (op (var 0) (var 1))) (op (var 1) (var 2))) , (var 3)) → ⊥
  cut621  adequate = bad621  (Adequate.valid adequate Two boolean env5)
  bad622 : PathP (λ _ → Two) (bop (bop b1 (bop b1 b1)) (bop b0 b1)) b1 → ⊥
  bad622  p = false≢true (cong lower p)
  cut622 : Adequate {ℓ} ((op (op (var 0) (op (var 0) (var 1))) (op (var 2) (var 0))) , (var 0)) → ⊥
  cut622  adequate = bad622  (Adequate.valid adequate Two boolean env6)
  bad623 : PathP (λ _ → Two) (bop (bop b0 (bop b0 b1)) (bop b0 b0)) b1 → ⊥
  bad623  p = false≢true (cong lower p)
  cut623 : Adequate {ℓ} ((op (op (var 0) (op (var 0) (var 1))) (op (var 2) (var 0))) , (var 1)) → ⊥
  cut623  adequate = bad623  (Adequate.valid adequate Two boolean env4)
  bad624 : PathP (λ _ → Two) (bop (bop b0 (bop b0 b0)) (bop b1 b0)) b1 → ⊥
  bad624  p = false≢true (cong lower p)
  cut624 : Adequate {ℓ} ((op (op (var 0) (op (var 0) (var 1))) (op (var 2) (var 0))) , (var 2)) → ⊥
  cut624  adequate = bad624  (Adequate.valid adequate Two boolean env2)
  bad625 : PathP (λ _ → Two) (bop (bop b0 (bop b0 b0)) (bop b0 b0)) b1 → ⊥
  bad625  p = false≢true (cong lower p)
  cut625 : Adequate {ℓ} ((op (op (var 0) (op (var 0) (var 1))) (op (var 2) (var 0))) , (var 3)) → ⊥
  cut625  adequate = bad625  (Adequate.valid adequate Two boolean env5)
  bad626 : PathP (λ _ → Two) (bop (bop b0 (bop b0 b1)) (bop b1 b1)) b0 → ⊥
  bad626  p = false≢true (sym (cong lower p))
  cut626 : Adequate {ℓ} ((op (op (var 0) (op (var 0) (var 1))) (op (var 2) (var 1))) , (var 0)) → ⊥
  cut626  adequate = bad626  (Adequate.valid adequate Two boolean env3)
  bad627 : PathP (λ _ → Two) (bop (bop b0 (bop b0 b1)) (bop b0 b1)) b1 → ⊥
  bad627  p = false≢true (cong lower p)
  cut627 : Adequate {ℓ} ((op (op (var 0) (op (var 0) (var 1))) (op (var 2) (var 1))) , (var 1)) → ⊥
  cut627  adequate = bad627  (Adequate.valid adequate Two boolean env4)
  bad628 : PathP (λ _ → Two) (bop (bop b0 (bop b0 b0)) (bop b1 b0)) b1 → ⊥
  bad628  p = false≢true (cong lower p)
  cut628 : Adequate {ℓ} ((op (op (var 0) (op (var 0) (var 1))) (op (var 2) (var 1))) , (var 2)) → ⊥
  cut628  adequate = bad628  (Adequate.valid adequate Two boolean env2)
  bad629 : PathP (λ _ → Two) (bop (bop b0 (bop b0 b0)) (bop b0 b0)) b1 → ⊥
  bad629  p = false≢true (cong lower p)
  cut629 : Adequate {ℓ} ((op (op (var 0) (op (var 0) (var 1))) (op (var 2) (var 1))) , (var 3)) → ⊥
  cut629  adequate = bad629  (Adequate.valid adequate Two boolean env5)
  bad630 : PathP (λ _ → Two) (bop (bop b0 (bop b0 b0)) (bop b1 b1)) b0 → ⊥
  bad630  p = false≢true (sym (cong lower p))
  cut630 : Adequate {ℓ} ((op (op (var 0) (op (var 0) (var 1))) (op (var 2) (var 2))) , (var 0)) → ⊥
  cut630  adequate = bad630  (Adequate.valid adequate Two boolean env2)
  bad631 : PathP (λ _ → Two) (bop (bop b0 (bop b0 b0)) (bop b1 b1)) b0 → ⊥
  bad631  p = false≢true (sym (cong lower p))
  cut631 : Adequate {ℓ} ((op (op (var 0) (op (var 0) (var 1))) (op (var 2) (var 2))) , (var 1)) → ⊥
  cut631  adequate = bad631  (Adequate.valid adequate Two boolean env2)
  env7 : ℕ → Two
  env7 zero = b1
  env7 (suc zero) = b0
  env7 (suc (suc zero)) = b0
  env7 (suc (suc (suc rest))) = b0
  bad632 : PathP (λ _ → Two) (bop (bop b1 (bop b1 b0)) (bop b0 b0)) b0 → ⊥
  bad632  p = false≢true (sym (cong lower p))
  cut632 : Adequate {ℓ} ((op (op (var 0) (op (var 0) (var 1))) (op (var 2) (var 2))) , (var 2)) → ⊥
  cut632  adequate = bad632  (Adequate.valid adequate Two boolean env7)
  bad633 : PathP (λ _ → Two) (bop (bop b0 (bop b0 b0)) (bop b0 b0)) b1 → ⊥
  bad633  p = false≢true (cong lower p)
  cut633 : Adequate {ℓ} ((op (op (var 0) (op (var 0) (var 1))) (op (var 2) (var 2))) , (var 3)) → ⊥
  cut633  adequate = bad633  (Adequate.valid adequate Two boolean env5)
  env8 : ℕ → Two
  env8 zero = b0
  env8 (suc zero) = b0
  env8 (suc (suc zero)) = b1
  env8 (suc (suc (suc zero))) = b1
  env8 (suc (suc (suc (suc rest)))) = b0
  bad634 : PathP (λ _ → Two) (bop (bop b0 (bop b0 b0)) (bop b1 b1)) b0 → ⊥
  bad634  p = false≢true (sym (cong lower p))
  cut634 : Adequate {ℓ} ((op (op (var 0) (op (var 0) (var 1))) (op (var 2) (var 3))) , (var 0)) → ⊥
  cut634  adequate = bad634  (Adequate.valid adequate Two boolean env8)
  bad635 : PathP (λ _ → Two) (bop (bop b0 (bop b0 b0)) (bop b1 b1)) b0 → ⊥
  bad635  p = false≢true (sym (cong lower p))
  cut635 : Adequate {ℓ} ((op (op (var 0) (op (var 0) (var 1))) (op (var 2) (var 3))) , (var 1)) → ⊥
  cut635  adequate = bad635  (Adequate.valid adequate Two boolean env8)
  env9 : ℕ → Two
  env9 zero = b0
  env9 (suc zero) = b0
  env9 (suc (suc zero)) = b1
  env9 (suc (suc (suc zero))) = b0
  env9 (suc (suc (suc (suc rest)))) = b0
  bad636 : PathP (λ _ → Two) (bop (bop b0 (bop b0 b0)) (bop b1 b0)) b1 → ⊥
  bad636  p = false≢true (cong lower p)
  cut636 : Adequate {ℓ} ((op (op (var 0) (op (var 0) (var 1))) (op (var 2) (var 3))) , (var 2)) → ⊥
  cut636  adequate = bad636  (Adequate.valid adequate Two boolean env9)
  bad637 : PathP (λ _ → Two) (bop (bop b0 (bop b0 b0)) (bop b0 b1)) b1 → ⊥
  bad637  p = false≢true (cong lower p)
  cut637 : Adequate {ℓ} ((op (op (var 0) (op (var 0) (var 1))) (op (var 2) (var 3))) , (var 3)) → ⊥
  cut637  adequate = bad637  (Adequate.valid adequate Two boolean env5)
  env10 : ℕ → Two
  env10 zero = b0
  env10 (suc zero) = b0
  env10 (suc (suc zero)) = b0
  env10 (suc (suc (suc zero))) = b0
  env10 (suc (suc (suc (suc zero)))) = b1
  env10 (suc (suc (suc (suc (suc rest))))) = b0
  bad638 : PathP (λ _ → Two) (bop (bop b0 (bop b0 b0)) (bop b0 b0)) b1 → ⊥
  bad638  p = false≢true (cong lower p)
  cut638 : Adequate {ℓ} ((op (op (var 0) (op (var 0) (var 1))) (op (var 2) (var 3))) , (var 4)) → ⊥
  cut638  adequate = bad638  (Adequate.valid adequate Two boolean env10)
  holds639 : (z0 z1 : A2) → (mul2 (mul2 z0 (mul2 z1 z0)) (mul2 z0 z0)) ≡ z0
  holds639 z0 z1 = refl
  cut639 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (var 0))) (op (var 0) (var 0))) , (var 0)) → ⊥
  cut639  = reject2 ((op (op (var 0) (op (var 1) (var 0))) (op (var 0) (var 0))) , (var 0)) (λ env → holds639 (env 0) (env 1))
  bad640 : PathP (λ _ → Two) (bop (bop b0 (bop b1 b0)) (bop b0 b0)) b1 → ⊥
  bad640  p = false≢true (cong lower p)
  cut640 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (var 0))) (op (var 0) (var 0))) , (var 1)) → ⊥
  cut640  adequate = bad640  (Adequate.valid adequate Two boolean env0)
  bad641 : PathP (λ _ → Two) (bop (bop b0 (bop b0 b0)) (bop b0 b0)) b1 → ⊥
  bad641  p = false≢true (cong lower p)
  cut641 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (var 0))) (op (var 0) (var 0))) , (var 2)) → ⊥
  cut641  adequate = bad641  (Adequate.valid adequate Two boolean env2)
  holds642 : (z0 z1 : A2) → (mul2 (mul2 z0 (mul2 z1 z0)) (mul2 z0 z1)) ≡ z0
  holds642 z0 z1 = refl
  cut642 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (var 0))) (op (var 0) (var 1))) , (var 0)) → ⊥
  cut642  = reject2 ((op (op (var 0) (op (var 1) (var 0))) (op (var 0) (var 1))) , (var 0)) (λ env → holds642 (env 0) (env 1))
  bad643 : PathP (λ _ → Two) (bop (bop b0 (bop b1 b0)) (bop b0 b1)) b1 → ⊥
  bad643  p = false≢true (cong lower p)
  cut643 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (var 0))) (op (var 0) (var 1))) , (var 1)) → ⊥
  cut643  adequate = bad643  (Adequate.valid adequate Two boolean env0)
  bad644 : PathP (λ _ → Two) (bop (bop b0 (bop b0 b0)) (bop b0 b0)) b1 → ⊥
  bad644  p = false≢true (cong lower p)
  cut644 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (var 0))) (op (var 0) (var 1))) , (var 2)) → ⊥
  cut644  adequate = bad644  (Adequate.valid adequate Two boolean env2)
  bad645 : PathP (λ _ → Two) (bop (bop b1 (bop b1 b1)) (bop b1 b0)) b1 → ⊥
  bad645  p = false≢true (cong lower p)
  cut645 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (var 0))) (op (var 0) (var 2))) , (var 0)) → ⊥
  cut645  adequate = bad645  (Adequate.valid adequate Two boolean env6)
  bad646 : PathP (λ _ → Two) (bop (bop b0 (bop b1 b0)) (bop b0 b0)) b1 → ⊥
  bad646  p = false≢true (cong lower p)
  cut646 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (var 0))) (op (var 0) (var 2))) , (var 1)) → ⊥
  cut646  adequate = bad646  (Adequate.valid adequate Two boolean env4)
  bad647 : PathP (λ _ → Two) (bop (bop b0 (bop b0 b0)) (bop b0 b1)) b1 → ⊥
  bad647  p = false≢true (cong lower p)
  cut647 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (var 0))) (op (var 0) (var 2))) , (var 2)) → ⊥
  cut647  adequate = bad647  (Adequate.valid adequate Two boolean env2)
  bad648 : PathP (λ _ → Two) (bop (bop b0 (bop b0 b0)) (bop b0 b0)) b1 → ⊥
  bad648  p = false≢true (cong lower p)
  cut648 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (var 0))) (op (var 0) (var 2))) , (var 3)) → ⊥
  cut648  adequate = bad648  (Adequate.valid adequate Two boolean env5)
  holds649 : (z0 z1 : A2) → (mul2 (mul2 z0 (mul2 z1 z0)) (mul2 z1 z0)) ≡ z0
  holds649 z0 z1 = refl
  cut649 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (var 0))) (op (var 1) (var 0))) , (var 0)) → ⊥
  cut649  = reject2 ((op (op (var 0) (op (var 1) (var 0))) (op (var 1) (var 0))) , (var 0)) (λ env → holds649 (env 0) (env 1))
  bad650 : PathP (λ _ → Two) (bop (bop b0 (bop b1 b0)) (bop b1 b0)) b1 → ⊥
  bad650  p = false≢true (cong lower p)
  cut650 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (var 0))) (op (var 1) (var 0))) , (var 1)) → ⊥
  cut650  adequate = bad650  (Adequate.valid adequate Two boolean env0)
  bad651 : PathP (λ _ → Two) (bop (bop b0 (bop b0 b0)) (bop b0 b0)) b1 → ⊥
  bad651  p = false≢true (cong lower p)
  cut651 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (var 0))) (op (var 1) (var 0))) , (var 2)) → ⊥
  cut651  adequate = bad651  (Adequate.valid adequate Two boolean env2)
  bad652 : PathP (λ _ → Two) (bop (bop b0 (bop b1 b0)) (bop b1 b1)) b0 → ⊥
  bad652  p = false≢true (sym (cong lower p))
  cut652 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (var 0))) (op (var 1) (var 1))) , (var 0)) → ⊥
  cut652  adequate = bad652  (Adequate.valid adequate Two boolean env0)
  bad653 : PathP (λ _ → Two) (bop (bop b1 (bop b0 b1)) (bop b0 b0)) b0 → ⊥
  bad653  p = false≢true (sym (cong lower p))
  cut653 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (var 0))) (op (var 1) (var 1))) , (var 1)) → ⊥
  cut653  adequate = bad653  (Adequate.valid adequate Two boolean env1)
  bad654 : PathP (λ _ → Two) (bop (bop b0 (bop b0 b0)) (bop b0 b0)) b1 → ⊥
  bad654  p = false≢true (cong lower p)
  cut654 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (var 0))) (op (var 1) (var 1))) , (var 2)) → ⊥
  cut654  adequate = bad654  (Adequate.valid adequate Two boolean env2)
  bad655 : PathP (λ _ → Two) (bop (bop b0 (bop b1 b0)) (bop b1 b1)) b0 → ⊥
  bad655  p = false≢true (sym (cong lower p))
  cut655 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (var 0))) (op (var 1) (var 2))) , (var 0)) → ⊥
  cut655  adequate = bad655  (Adequate.valid adequate Two boolean env3)
  bad656 : PathP (λ _ → Two) (bop (bop b0 (bop b1 b0)) (bop b1 b0)) b1 → ⊥
  bad656  p = false≢true (cong lower p)
  cut656 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (var 0))) (op (var 1) (var 2))) , (var 1)) → ⊥
  cut656  adequate = bad656  (Adequate.valid adequate Two boolean env4)
  bad657 : PathP (λ _ → Two) (bop (bop b0 (bop b0 b0)) (bop b0 b1)) b1 → ⊥
  bad657  p = false≢true (cong lower p)
  cut657 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (var 0))) (op (var 1) (var 2))) , (var 2)) → ⊥
  cut657  adequate = bad657  (Adequate.valid adequate Two boolean env2)
  bad658 : PathP (λ _ → Two) (bop (bop b0 (bop b0 b0)) (bop b0 b0)) b1 → ⊥
  bad658  p = false≢true (cong lower p)
  cut658 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (var 0))) (op (var 1) (var 2))) , (var 3)) → ⊥
  cut658  adequate = bad658  (Adequate.valid adequate Two boolean env5)
  bad659 : PathP (λ _ → Two) (bop (bop b1 (bop b1 b1)) (bop b0 b1)) b1 → ⊥
  bad659  p = false≢true (cong lower p)
  cut659 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (var 0))) (op (var 2) (var 0))) , (var 0)) → ⊥
  cut659  adequate = bad659  (Adequate.valid adequate Two boolean env6)
  bad660 : PathP (λ _ → Two) (bop (bop b0 (bop b1 b0)) (bop b0 b0)) b1 → ⊥
  bad660  p = false≢true (cong lower p)
  cut660 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (var 0))) (op (var 2) (var 0))) , (var 1)) → ⊥
  cut660  adequate = bad660  (Adequate.valid adequate Two boolean env4)
  bad661 : PathP (λ _ → Two) (bop (bop b0 (bop b0 b0)) (bop b1 b0)) b1 → ⊥
  bad661  p = false≢true (cong lower p)
  cut661 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (var 0))) (op (var 2) (var 0))) , (var 2)) → ⊥
  cut661  adequate = bad661  (Adequate.valid adequate Two boolean env2)
  bad662 : PathP (λ _ → Two) (bop (bop b0 (bop b0 b0)) (bop b0 b0)) b1 → ⊥
  bad662  p = false≢true (cong lower p)
  cut662 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (var 0))) (op (var 2) (var 0))) , (var 3)) → ⊥
  cut662  adequate = bad662  (Adequate.valid adequate Two boolean env5)
  bad663 : PathP (λ _ → Two) (bop (bop b0 (bop b1 b0)) (bop b1 b1)) b0 → ⊥
  bad663  p = false≢true (sym (cong lower p))
  cut663 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (var 0))) (op (var 2) (var 1))) , (var 0)) → ⊥
  cut663  adequate = bad663  (Adequate.valid adequate Two boolean env3)
  bad664 : PathP (λ _ → Two) (bop (bop b0 (bop b1 b0)) (bop b0 b1)) b1 → ⊥
  bad664  p = false≢true (cong lower p)
  cut664 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (var 0))) (op (var 2) (var 1))) , (var 1)) → ⊥
  cut664  adequate = bad664  (Adequate.valid adequate Two boolean env4)
  bad665 : PathP (λ _ → Two) (bop (bop b0 (bop b0 b0)) (bop b1 b0)) b1 → ⊥
  bad665  p = false≢true (cong lower p)
  cut665 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (var 0))) (op (var 2) (var 1))) , (var 2)) → ⊥
  cut665  adequate = bad665  (Adequate.valid adequate Two boolean env2)
  bad666 : PathP (λ _ → Two) (bop (bop b0 (bop b0 b0)) (bop b0 b0)) b1 → ⊥
  bad666  p = false≢true (cong lower p)
  cut666 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (var 0))) (op (var 2) (var 1))) , (var 3)) → ⊥
  cut666  adequate = bad666  (Adequate.valid adequate Two boolean env5)
  bad667 : PathP (λ _ → Two) (bop (bop b0 (bop b0 b0)) (bop b1 b1)) b0 → ⊥
  bad667  p = false≢true (sym (cong lower p))
  cut667 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (var 0))) (op (var 2) (var 2))) , (var 0)) → ⊥
  cut667  adequate = bad667  (Adequate.valid adequate Two boolean env2)
  bad668 : PathP (λ _ → Two) (bop (bop b0 (bop b0 b0)) (bop b1 b1)) b0 → ⊥
  bad668  p = false≢true (sym (cong lower p))
  cut668 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (var 0))) (op (var 2) (var 2))) , (var 1)) → ⊥
  cut668  adequate = bad668  (Adequate.valid adequate Two boolean env2)
  bad669 : PathP (λ _ → Two) (bop (bop b1 (bop b0 b1)) (bop b0 b0)) b0 → ⊥
  bad669  p = false≢true (sym (cong lower p))
  cut669 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (var 0))) (op (var 2) (var 2))) , (var 2)) → ⊥
  cut669  adequate = bad669  (Adequate.valid adequate Two boolean env7)
  bad670 : PathP (λ _ → Two) (bop (bop b0 (bop b0 b0)) (bop b0 b0)) b1 → ⊥
  bad670  p = false≢true (cong lower p)
  cut670 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (var 0))) (op (var 2) (var 2))) , (var 3)) → ⊥
  cut670  adequate = bad670  (Adequate.valid adequate Two boolean env5)
  bad671 : PathP (λ _ → Two) (bop (bop b0 (bop b0 b0)) (bop b1 b1)) b0 → ⊥
  bad671  p = false≢true (sym (cong lower p))
  cut671 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (var 0))) (op (var 2) (var 3))) , (var 0)) → ⊥
  cut671  adequate = bad671  (Adequate.valid adequate Two boolean env8)
  bad672 : PathP (λ _ → Two) (bop (bop b0 (bop b0 b0)) (bop b1 b1)) b0 → ⊥
  bad672  p = false≢true (sym (cong lower p))
  cut672 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (var 0))) (op (var 2) (var 3))) , (var 1)) → ⊥
  cut672  adequate = bad672  (Adequate.valid adequate Two boolean env8)
  bad673 : PathP (λ _ → Two) (bop (bop b0 (bop b0 b0)) (bop b1 b0)) b1 → ⊥
  bad673  p = false≢true (cong lower p)
  cut673 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (var 0))) (op (var 2) (var 3))) , (var 2)) → ⊥
  cut673  adequate = bad673  (Adequate.valid adequate Two boolean env9)
  bad674 : PathP (λ _ → Two) (bop (bop b0 (bop b0 b0)) (bop b0 b1)) b1 → ⊥
  bad674  p = false≢true (cong lower p)
  cut674 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (var 0))) (op (var 2) (var 3))) , (var 3)) → ⊥
  cut674  adequate = bad674  (Adequate.valid adequate Two boolean env5)
  bad675 : PathP (λ _ → Two) (bop (bop b0 (bop b0 b0)) (bop b0 b0)) b1 → ⊥
  bad675  p = false≢true (cong lower p)
  cut675 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (var 0))) (op (var 2) (var 3))) , (var 4)) → ⊥
  cut675  adequate = bad675  (Adequate.valid adequate Two boolean env10)
  holds676 : (z0 z1 : A2) → (mul2 (mul2 z0 (mul2 z1 z1)) (mul2 z0 z0)) ≡ z0
  holds676 z0 z1 = refl
  cut676 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (var 1))) (op (var 0) (var 0))) , (var 0)) → ⊥
  cut676  = reject2 ((op (op (var 0) (op (var 1) (var 1))) (op (var 0) (var 0))) , (var 0)) (λ env → holds676 (env 0) (env 1))
  bad677 : PathP (λ _ → Two) (bop (bop b0 (bop b1 b1)) (bop b0 b0)) b1 → ⊥
  bad677  p = false≢true (cong lower p)
  cut677 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (var 1))) (op (var 0) (var 0))) , (var 1)) → ⊥
  cut677  adequate = bad677  (Adequate.valid adequate Two boolean env0)
  bad678 : PathP (λ _ → Two) (bop (bop b0 (bop b0 b0)) (bop b0 b0)) b1 → ⊥
  bad678  p = false≢true (cong lower p)
  cut678 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (var 1))) (op (var 0) (var 0))) , (var 2)) → ⊥
  cut678  adequate = bad678  (Adequate.valid adequate Two boolean env2)
  holds679 : (z0 z1 : A2) → (mul2 (mul2 z0 (mul2 z1 z1)) (mul2 z0 z1)) ≡ z0
  holds679 z0 z1 = refl
  cut679 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (var 1))) (op (var 0) (var 1))) , (var 0)) → ⊥
  cut679  = reject2 ((op (op (var 0) (op (var 1) (var 1))) (op (var 0) (var 1))) , (var 0)) (λ env → holds679 (env 0) (env 1))
  bad680 : PathP (λ _ → Two) (bop (bop b0 (bop b1 b1)) (bop b0 b1)) b1 → ⊥
  bad680  p = false≢true (cong lower p)
  cut680 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (var 1))) (op (var 0) (var 1))) , (var 1)) → ⊥
  cut680  adequate = bad680  (Adequate.valid adequate Two boolean env0)
  bad681 : PathP (λ _ → Two) (bop (bop b0 (bop b0 b0)) (bop b0 b0)) b1 → ⊥
  bad681  p = false≢true (cong lower p)
  cut681 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (var 1))) (op (var 0) (var 1))) , (var 2)) → ⊥
  cut681  adequate = bad681  (Adequate.valid adequate Two boolean env2)
  bad682 : PathP (λ _ → Two) (bop (bop b1 (bop b1 b1)) (bop b1 b0)) b1 → ⊥
  bad682  p = false≢true (cong lower p)
  cut682 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (var 1))) (op (var 0) (var 2))) , (var 0)) → ⊥
  cut682  adequate = bad682  (Adequate.valid adequate Two boolean env6)
  bad683 : PathP (λ _ → Two) (bop (bop b0 (bop b1 b1)) (bop b0 b0)) b1 → ⊥
  bad683  p = false≢true (cong lower p)
  cut683 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (var 1))) (op (var 0) (var 2))) , (var 1)) → ⊥
  cut683  adequate = bad683  (Adequate.valid adequate Two boolean env4)
  bad684 : PathP (λ _ → Two) (bop (bop b0 (bop b0 b0)) (bop b0 b1)) b1 → ⊥
  bad684  p = false≢true (cong lower p)
  cut684 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (var 1))) (op (var 0) (var 2))) , (var 2)) → ⊥
  cut684  adequate = bad684  (Adequate.valid adequate Two boolean env2)
  bad685 : PathP (λ _ → Two) (bop (bop b0 (bop b0 b0)) (bop b0 b0)) b1 → ⊥
  bad685  p = false≢true (cong lower p)
  cut685 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (var 1))) (op (var 0) (var 2))) , (var 3)) → ⊥
  cut685  adequate = bad685  (Adequate.valid adequate Two boolean env5)
  holds686 : (z0 z1 : A2) → (mul2 (mul2 z0 (mul2 z1 z1)) (mul2 z1 z0)) ≡ z0
  holds686 z0 z1 = refl
  cut686 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (var 1))) (op (var 1) (var 0))) , (var 0)) → ⊥
  cut686  = reject2 ((op (op (var 0) (op (var 1) (var 1))) (op (var 1) (var 0))) , (var 0)) (λ env → holds686 (env 0) (env 1))
  bad687 : PathP (λ _ → Two) (bop (bop b0 (bop b1 b1)) (bop b1 b0)) b1 → ⊥
  bad687  p = false≢true (cong lower p)
  cut687 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (var 1))) (op (var 1) (var 0))) , (var 1)) → ⊥
  cut687  adequate = bad687  (Adequate.valid adequate Two boolean env0)
  bad688 : PathP (λ _ → Two) (bop (bop b0 (bop b0 b0)) (bop b0 b0)) b1 → ⊥
  bad688  p = false≢true (cong lower p)
  cut688 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (var 1))) (op (var 1) (var 0))) , (var 2)) → ⊥
  cut688  adequate = bad688  (Adequate.valid adequate Two boolean env2)
  bad689 : PathP (λ _ → Two) (bop (bop b0 (bop b1 b1)) (bop b1 b1)) b0 → ⊥
  bad689  p = false≢true (sym (cong lower p))
  cut689 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (var 1))) (op (var 1) (var 1))) , (var 0)) → ⊥
  cut689  adequate = bad689  (Adequate.valid adequate Two boolean env0)
  bad690 : PathP (λ _ → Two) (bop (bop b1 (bop b0 b0)) (bop b0 b0)) b0 → ⊥
  bad690  p = false≢true (sym (cong lower p))
  cut690 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (var 1))) (op (var 1) (var 1))) , (var 1)) → ⊥
  cut690  adequate = bad690  (Adequate.valid adequate Two boolean env1)
  bad691 : PathP (λ _ → Two) (bop (bop b0 (bop b0 b0)) (bop b0 b0)) b1 → ⊥
  bad691  p = false≢true (cong lower p)
  cut691 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (var 1))) (op (var 1) (var 1))) , (var 2)) → ⊥
  cut691  adequate = bad691  (Adequate.valid adequate Two boolean env2)
  bad692 : PathP (λ _ → Two) (bop (bop b0 (bop b1 b1)) (bop b1 b1)) b0 → ⊥
  bad692  p = false≢true (sym (cong lower p))
  cut692 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (var 1))) (op (var 1) (var 2))) , (var 0)) → ⊥
  cut692  adequate = bad692  (Adequate.valid adequate Two boolean env3)
  bad693 : PathP (λ _ → Two) (bop (bop b0 (bop b1 b1)) (bop b1 b0)) b1 → ⊥
  bad693  p = false≢true (cong lower p)
  cut693 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (var 1))) (op (var 1) (var 2))) , (var 1)) → ⊥
  cut693  adequate = bad693  (Adequate.valid adequate Two boolean env4)
  bad694 : PathP (λ _ → Two) (bop (bop b0 (bop b0 b0)) (bop b0 b1)) b1 → ⊥
  bad694  p = false≢true (cong lower p)
  cut694 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (var 1))) (op (var 1) (var 2))) , (var 2)) → ⊥
  cut694  adequate = bad694  (Adequate.valid adequate Two boolean env2)
  bad695 : PathP (λ _ → Two) (bop (bop b0 (bop b0 b0)) (bop b0 b0)) b1 → ⊥
  bad695  p = false≢true (cong lower p)
  cut695 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (var 1))) (op (var 1) (var 2))) , (var 3)) → ⊥
  cut695  adequate = bad695  (Adequate.valid adequate Two boolean env5)
  bad696 : PathP (λ _ → Two) (bop (bop b1 (bop b1 b1)) (bop b0 b1)) b1 → ⊥
  bad696  p = false≢true (cong lower p)
  cut696 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (var 1))) (op (var 2) (var 0))) , (var 0)) → ⊥
  cut696  adequate = bad696  (Adequate.valid adequate Two boolean env6)
  bad697 : PathP (λ _ → Two) (bop (bop b0 (bop b1 b1)) (bop b0 b0)) b1 → ⊥
  bad697  p = false≢true (cong lower p)
  cut697 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (var 1))) (op (var 2) (var 0))) , (var 1)) → ⊥
  cut697  adequate = bad697  (Adequate.valid adequate Two boolean env4)
  bad698 : PathP (λ _ → Two) (bop (bop b0 (bop b0 b0)) (bop b1 b0)) b1 → ⊥
  bad698  p = false≢true (cong lower p)
  cut698 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (var 1))) (op (var 2) (var 0))) , (var 2)) → ⊥
  cut698  adequate = bad698  (Adequate.valid adequate Two boolean env2)
  bad699 : PathP (λ _ → Two) (bop (bop b0 (bop b0 b0)) (bop b0 b0)) b1 → ⊥
  bad699  p = false≢true (cong lower p)
  cut699 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (var 1))) (op (var 2) (var 0))) , (var 3)) → ⊥
  cut699  adequate = bad699  (Adequate.valid adequate Two boolean env5)
  bad700 : PathP (λ _ → Two) (bop (bop b0 (bop b1 b1)) (bop b1 b1)) b0 → ⊥
  bad700  p = false≢true (sym (cong lower p))
  cut700 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (var 1))) (op (var 2) (var 1))) , (var 0)) → ⊥
  cut700  adequate = bad700  (Adequate.valid adequate Two boolean env3)
  bad701 : PathP (λ _ → Two) (bop (bop b0 (bop b1 b1)) (bop b0 b1)) b1 → ⊥
  bad701  p = false≢true (cong lower p)
  cut701 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (var 1))) (op (var 2) (var 1))) , (var 1)) → ⊥
  cut701  adequate = bad701  (Adequate.valid adequate Two boolean env4)
  bad702 : PathP (λ _ → Two) (bop (bop b0 (bop b0 b0)) (bop b1 b0)) b1 → ⊥
  bad702  p = false≢true (cong lower p)
  cut702 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (var 1))) (op (var 2) (var 1))) , (var 2)) → ⊥
  cut702  adequate = bad702  (Adequate.valid adequate Two boolean env2)
  bad703 : PathP (λ _ → Two) (bop (bop b0 (bop b0 b0)) (bop b0 b0)) b1 → ⊥
  bad703  p = false≢true (cong lower p)
  cut703 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (var 1))) (op (var 2) (var 1))) , (var 3)) → ⊥
  cut703  adequate = bad703  (Adequate.valid adequate Two boolean env5)
  bad704 : PathP (λ _ → Two) (bop (bop b0 (bop b0 b0)) (bop b1 b1)) b0 → ⊥
  bad704  p = false≢true (sym (cong lower p))
  cut704 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (var 1))) (op (var 2) (var 2))) , (var 0)) → ⊥
  cut704  adequate = bad704  (Adequate.valid adequate Two boolean env2)
  bad705 : PathP (λ _ → Two) (bop (bop b0 (bop b0 b0)) (bop b1 b1)) b0 → ⊥
  bad705  p = false≢true (sym (cong lower p))
  cut705 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (var 1))) (op (var 2) (var 2))) , (var 1)) → ⊥
  cut705  adequate = bad705  (Adequate.valid adequate Two boolean env2)
  bad706 : PathP (λ _ → Two) (bop (bop b1 (bop b0 b0)) (bop b0 b0)) b0 → ⊥
  bad706  p = false≢true (sym (cong lower p))
  cut706 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (var 1))) (op (var 2) (var 2))) , (var 2)) → ⊥
  cut706  adequate = bad706  (Adequate.valid adequate Two boolean env7)
  bad707 : PathP (λ _ → Two) (bop (bop b0 (bop b0 b0)) (bop b0 b0)) b1 → ⊥
  bad707  p = false≢true (cong lower p)
  cut707 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (var 1))) (op (var 2) (var 2))) , (var 3)) → ⊥
  cut707  adequate = bad707  (Adequate.valid adequate Two boolean env5)
  bad708 : PathP (λ _ → Two) (bop (bop b0 (bop b0 b0)) (bop b1 b1)) b0 → ⊥
  bad708  p = false≢true (sym (cong lower p))
  cut708 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (var 1))) (op (var 2) (var 3))) , (var 0)) → ⊥
  cut708  adequate = bad708  (Adequate.valid adequate Two boolean env8)
  bad709 : PathP (λ _ → Two) (bop (bop b0 (bop b0 b0)) (bop b1 b1)) b0 → ⊥
  bad709  p = false≢true (sym (cong lower p))
  cut709 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (var 1))) (op (var 2) (var 3))) , (var 1)) → ⊥
  cut709  adequate = bad709  (Adequate.valid adequate Two boolean env8)
  bad710 : PathP (λ _ → Two) (bop (bop b0 (bop b0 b0)) (bop b1 b0)) b1 → ⊥
  bad710  p = false≢true (cong lower p)
  cut710 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (var 1))) (op (var 2) (var 3))) , (var 2)) → ⊥
  cut710  adequate = bad710  (Adequate.valid adequate Two boolean env9)
  bad711 : PathP (λ _ → Two) (bop (bop b0 (bop b0 b0)) (bop b0 b1)) b1 → ⊥
  bad711  p = false≢true (cong lower p)
  cut711 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (var 1))) (op (var 2) (var 3))) , (var 3)) → ⊥
  cut711  adequate = bad711  (Adequate.valid adequate Two boolean env5)
  bad712 : PathP (λ _ → Two) (bop (bop b0 (bop b0 b0)) (bop b0 b0)) b1 → ⊥
  bad712  p = false≢true (cong lower p)
  cut712 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (var 1))) (op (var 2) (var 3))) , (var 4)) → ⊥
  cut712  adequate = bad712  (Adequate.valid adequate Two boolean env10)
  holds713 : (z0 z1 z2 : A2) → (mul2 (mul2 z0 (mul2 z1 z2)) (mul2 z0 z0)) ≡ z0
  holds713 z0 z1 z2 = refl
  cut713 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (var 2))) (op (var 0) (var 0))) , (var 0)) → ⊥
  cut713  = reject2 ((op (op (var 0) (op (var 1) (var 2))) (op (var 0) (var 0))) , (var 0)) (λ env → holds713 (env 0) (env 1) (env 2))
  bad714 : PathP (λ _ → Two) (bop (bop b0 (bop b1 b0)) (bop b0 b0)) b1 → ⊥
  bad714  p = false≢true (cong lower p)
  cut714 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (var 2))) (op (var 0) (var 0))) , (var 1)) → ⊥
  cut714  adequate = bad714  (Adequate.valid adequate Two boolean env4)
  bad715 : PathP (λ _ → Two) (bop (bop b0 (bop b0 b1)) (bop b0 b0)) b1 → ⊥
  bad715  p = false≢true (cong lower p)
  cut715 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (var 2))) (op (var 0) (var 0))) , (var 2)) → ⊥
  cut715  adequate = bad715  (Adequate.valid adequate Two boolean env2)
  bad716 : PathP (λ _ → Two) (bop (bop b0 (bop b0 b0)) (bop b0 b0)) b1 → ⊥
  bad716  p = false≢true (cong lower p)
  cut716 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (var 2))) (op (var 0) (var 0))) , (var 3)) → ⊥
  cut716  adequate = bad716  (Adequate.valid adequate Two boolean env5)
  holds717 : (z0 z1 z2 : A2) → (mul2 (mul2 z0 (mul2 z1 z2)) (mul2 z0 z1)) ≡ z0
  holds717 z0 z1 z2 = refl
  cut717 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (var 2))) (op (var 0) (var 1))) , (var 0)) → ⊥
  cut717  = reject2 ((op (op (var 0) (op (var 1) (var 2))) (op (var 0) (var 1))) , (var 0)) (λ env → holds717 (env 0) (env 1) (env 2))
  bad718 : PathP (λ _ → Two) (bop (bop b0 (bop b1 b0)) (bop b0 b1)) b1 → ⊥
  bad718  p = false≢true (cong lower p)
  cut718 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (var 2))) (op (var 0) (var 1))) , (var 1)) → ⊥
  cut718  adequate = bad718  (Adequate.valid adequate Two boolean env4)
  bad719 : PathP (λ _ → Two) (bop (bop b0 (bop b0 b1)) (bop b0 b0)) b1 → ⊥
  bad719  p = false≢true (cong lower p)
  cut719 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (var 2))) (op (var 0) (var 1))) , (var 2)) → ⊥
  cut719  adequate = bad719  (Adequate.valid adequate Two boolean env2)
  bad720 : PathP (λ _ → Two) (bop (bop b0 (bop b0 b0)) (bop b0 b0)) b1 → ⊥
  bad720  p = false≢true (cong lower p)
  cut720 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (var 2))) (op (var 0) (var 1))) , (var 3)) → ⊥
  cut720  adequate = bad720  (Adequate.valid adequate Two boolean env5)
  holds721 : (z0 z1 z2 : A2) → (mul2 (mul2 z0 (mul2 z1 z2)) (mul2 z0 z2)) ≡ z0
  holds721 z0 z1 z2 = refl
  cut721 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (var 2))) (op (var 0) (var 2))) , (var 0)) → ⊥
  cut721  = reject2 ((op (op (var 0) (op (var 1) (var 2))) (op (var 0) (var 2))) , (var 0)) (λ env → holds721 (env 0) (env 1) (env 2))
  bad722 : PathP (λ _ → Two) (bop (bop b0 (bop b1 b0)) (bop b0 b0)) b1 → ⊥
  bad722  p = false≢true (cong lower p)
  cut722 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (var 2))) (op (var 0) (var 2))) , (var 1)) → ⊥
  cut722  adequate = bad722  (Adequate.valid adequate Two boolean env4)
  bad723 : PathP (λ _ → Two) (bop (bop b0 (bop b0 b1)) (bop b0 b1)) b1 → ⊥
  bad723  p = false≢true (cong lower p)
  cut723 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (var 2))) (op (var 0) (var 2))) , (var 2)) → ⊥
  cut723  adequate = bad723  (Adequate.valid adequate Two boolean env2)
  bad724 : PathP (λ _ → Two) (bop (bop b0 (bop b0 b0)) (bop b0 b0)) b1 → ⊥
  bad724  p = false≢true (cong lower p)
  cut724 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (var 2))) (op (var 0) (var 2))) , (var 3)) → ⊥
  cut724  adequate = bad724  (Adequate.valid adequate Two boolean env5)
  env11 : ℕ → Two
  env11 zero = b1
  env11 (suc zero) = b1
  env11 (suc (suc zero)) = b1
  env11 (suc (suc (suc zero))) = b0
  env11 (suc (suc (suc (suc rest)))) = b0
  bad725 : PathP (λ _ → Two) (bop (bop b1 (bop b1 b1)) (bop b1 b0)) b1 → ⊥
  bad725  p = false≢true (cong lower p)
  cut725 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (var 2))) (op (var 0) (var 3))) , (var 0)) → ⊥
  cut725  adequate = bad725  (Adequate.valid adequate Two boolean env11)
  env12 : ℕ → Two
  env12 zero = b0
  env12 (suc zero) = b1
  env12 (suc (suc zero)) = b0
  env12 (suc (suc (suc zero))) = b0
  env12 (suc (suc (suc (suc rest)))) = b0
  bad726 : PathP (λ _ → Two) (bop (bop b0 (bop b1 b0)) (bop b0 b0)) b1 → ⊥
  bad726  p = false≢true (cong lower p)
  cut726 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (var 2))) (op (var 0) (var 3))) , (var 1)) → ⊥
  cut726  adequate = bad726  (Adequate.valid adequate Two boolean env12)
  bad727 : PathP (λ _ → Two) (bop (bop b0 (bop b0 b1)) (bop b0 b0)) b1 → ⊥
  bad727  p = false≢true (cong lower p)
  cut727 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (var 2))) (op (var 0) (var 3))) , (var 2)) → ⊥
  cut727  adequate = bad727  (Adequate.valid adequate Two boolean env9)
  bad728 : PathP (λ _ → Two) (bop (bop b0 (bop b0 b0)) (bop b0 b1)) b1 → ⊥
  bad728  p = false≢true (cong lower p)
  cut728 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (var 2))) (op (var 0) (var 3))) , (var 3)) → ⊥
  cut728  adequate = bad728  (Adequate.valid adequate Two boolean env5)
  bad729 : PathP (λ _ → Two) (bop (bop b0 (bop b0 b0)) (bop b0 b0)) b1 → ⊥
  bad729  p = false≢true (cong lower p)
  cut729 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (var 2))) (op (var 0) (var 3))) , (var 4)) → ⊥
  cut729  adequate = bad729  (Adequate.valid adequate Two boolean env10)
  holds730 : (z0 z1 z2 : A2) → (mul2 (mul2 z0 (mul2 z1 z2)) (mul2 z1 z0)) ≡ z0
  holds730 z0 z1 z2 = refl
  cut730 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (var 2))) (op (var 1) (var 0))) , (var 0)) → ⊥
  cut730  = reject2 ((op (op (var 0) (op (var 1) (var 2))) (op (var 1) (var 0))) , (var 0)) (λ env → holds730 (env 0) (env 1) (env 2))
  bad731 : PathP (λ _ → Two) (bop (bop b0 (bop b1 b0)) (bop b1 b0)) b1 → ⊥
  bad731  p = false≢true (cong lower p)
  cut731 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (var 2))) (op (var 1) (var 0))) , (var 1)) → ⊥
  cut731  adequate = bad731  (Adequate.valid adequate Two boolean env4)
  bad732 : PathP (λ _ → Two) (bop (bop b0 (bop b0 b1)) (bop b0 b0)) b1 → ⊥
  bad732  p = false≢true (cong lower p)
  cut732 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (var 2))) (op (var 1) (var 0))) , (var 2)) → ⊥
  cut732  adequate = bad732  (Adequate.valid adequate Two boolean env2)
  bad733 : PathP (λ _ → Two) (bop (bop b0 (bop b0 b0)) (bop b0 b0)) b1 → ⊥
  bad733  p = false≢true (cong lower p)
  cut733 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (var 2))) (op (var 1) (var 0))) , (var 3)) → ⊥
  cut733  adequate = bad733  (Adequate.valid adequate Two boolean env5)
  bad734 : PathP (λ _ → Two) (bop (bop b0 (bop b1 b0)) (bop b1 b1)) b0 → ⊥
  bad734  p = false≢true (sym (cong lower p))
  cut734 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (var 2))) (op (var 1) (var 1))) , (var 0)) → ⊥
  cut734  adequate = bad734  (Adequate.valid adequate Two boolean env4)
  bad735 : PathP (λ _ → Two) (bop (bop b1 (bop b0 b0)) (bop b0 b0)) b0 → ⊥
  bad735  p = false≢true (sym (cong lower p))
  cut735 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (var 2))) (op (var 1) (var 1))) , (var 1)) → ⊥
  cut735  adequate = bad735  (Adequate.valid adequate Two boolean env7)
  bad736 : PathP (λ _ → Two) (bop (bop b0 (bop b0 b1)) (bop b0 b0)) b1 → ⊥
  bad736  p = false≢true (cong lower p)
  cut736 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (var 2))) (op (var 1) (var 1))) , (var 2)) → ⊥
  cut736  adequate = bad736  (Adequate.valid adequate Two boolean env2)
  bad737 : PathP (λ _ → Two) (bop (bop b0 (bop b0 b0)) (bop b0 b0)) b1 → ⊥
  bad737  p = false≢true (cong lower p)
  cut737 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (var 2))) (op (var 1) (var 1))) , (var 3)) → ⊥
  cut737  adequate = bad737  (Adequate.valid adequate Two boolean env5)
  bad738 : PathP (λ _ → Two) (bop (bop b0 (bop b1 b1)) (bop b1 b1)) b0 → ⊥
  bad738  p = false≢true (sym (cong lower p))
  cut738 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (var 2))) (op (var 1) (var 2))) , (var 0)) → ⊥
  cut738  adequate = bad738  (Adequate.valid adequate Two boolean env3)
  bad739 : PathP (λ _ → Two) (bop (bop b0 (bop b1 b0)) (bop b1 b0)) b1 → ⊥
  bad739  p = false≢true (cong lower p)
  cut739 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (var 2))) (op (var 1) (var 2))) , (var 1)) → ⊥
  cut739  adequate = bad739  (Adequate.valid adequate Two boolean env4)
  bad740 : PathP (λ _ → Two) (bop (bop b0 (bop b0 b1)) (bop b0 b1)) b1 → ⊥
  bad740  p = false≢true (cong lower p)
  cut740 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (var 2))) (op (var 1) (var 2))) , (var 2)) → ⊥
  cut740  adequate = bad740  (Adequate.valid adequate Two boolean env2)
  bad741 : PathP (λ _ → Two) (bop (bop b0 (bop b0 b0)) (bop b0 b0)) b1 → ⊥
  bad741  p = false≢true (cong lower p)
  cut741 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (var 2))) (op (var 1) (var 2))) , (var 3)) → ⊥
  cut741  adequate = bad741  (Adequate.valid adequate Two boolean env5)
  env13 : ℕ → Two
  env13 zero = b0
  env13 (suc zero) = b1
  env13 (suc (suc zero)) = b0
  env13 (suc (suc (suc zero))) = b1
  env13 (suc (suc (suc (suc rest)))) = b0
  bad742 : PathP (λ _ → Two) (bop (bop b0 (bop b1 b0)) (bop b1 b1)) b0 → ⊥
  bad742  p = false≢true (sym (cong lower p))
  cut742 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (var 2))) (op (var 1) (var 3))) , (var 0)) → ⊥
  cut742  adequate = bad742  (Adequate.valid adequate Two boolean env13)
  bad743 : PathP (λ _ → Two) (bop (bop b0 (bop b1 b0)) (bop b1 b0)) b1 → ⊥
  bad743  p = false≢true (cong lower p)
  cut743 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (var 2))) (op (var 1) (var 3))) , (var 1)) → ⊥
  cut743  adequate = bad743  (Adequate.valid adequate Two boolean env12)
  bad744 : PathP (λ _ → Two) (bop (bop b0 (bop b0 b1)) (bop b0 b0)) b1 → ⊥
  bad744  p = false≢true (cong lower p)
  cut744 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (var 2))) (op (var 1) (var 3))) , (var 2)) → ⊥
  cut744  adequate = bad744  (Adequate.valid adequate Two boolean env9)
  bad745 : PathP (λ _ → Two) (bop (bop b0 (bop b0 b0)) (bop b0 b1)) b1 → ⊥
  bad745  p = false≢true (cong lower p)
  cut745 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (var 2))) (op (var 1) (var 3))) , (var 3)) → ⊥
  cut745  adequate = bad745  (Adequate.valid adequate Two boolean env5)
  bad746 : PathP (λ _ → Two) (bop (bop b0 (bop b0 b0)) (bop b0 b0)) b1 → ⊥
  bad746  p = false≢true (cong lower p)
  cut746 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (var 2))) (op (var 1) (var 3))) , (var 4)) → ⊥
  cut746  adequate = bad746  (Adequate.valid adequate Two boolean env10)
  holds747 : (z0 z1 z2 : A2) → (mul2 (mul2 z0 (mul2 z1 z2)) (mul2 z2 z0)) ≡ z0
  holds747 z0 z1 z2 = refl
  cut747 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (var 2))) (op (var 2) (var 0))) , (var 0)) → ⊥
  cut747  = reject2 ((op (op (var 0) (op (var 1) (var 2))) (op (var 2) (var 0))) , (var 0)) (λ env → holds747 (env 0) (env 1) (env 2))
  bad748 : PathP (λ _ → Two) (bop (bop b0 (bop b1 b0)) (bop b0 b0)) b1 → ⊥
  bad748  p = false≢true (cong lower p)
  cut748 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (var 2))) (op (var 2) (var 0))) , (var 1)) → ⊥
  cut748  adequate = bad748  (Adequate.valid adequate Two boolean env4)
  bad749 : PathP (λ _ → Two) (bop (bop b0 (bop b0 b1)) (bop b1 b0)) b1 → ⊥
  bad749  p = false≢true (cong lower p)
  cut749 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (var 2))) (op (var 2) (var 0))) , (var 2)) → ⊥
  cut749  adequate = bad749  (Adequate.valid adequate Two boolean env2)
  bad750 : PathP (λ _ → Two) (bop (bop b0 (bop b0 b0)) (bop b0 b0)) b1 → ⊥
  bad750  p = false≢true (cong lower p)
  cut750 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (var 2))) (op (var 2) (var 0))) , (var 3)) → ⊥
  cut750  adequate = bad750  (Adequate.valid adequate Two boolean env5)
  bad751 : PathP (λ _ → Two) (bop (bop b0 (bop b1 b1)) (bop b1 b1)) b0 → ⊥
  bad751  p = false≢true (sym (cong lower p))
  cut751 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (var 2))) (op (var 2) (var 1))) , (var 0)) → ⊥
  cut751  adequate = bad751  (Adequate.valid adequate Two boolean env3)
  bad752 : PathP (λ _ → Two) (bop (bop b0 (bop b1 b0)) (bop b0 b1)) b1 → ⊥
  bad752  p = false≢true (cong lower p)
  cut752 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (var 2))) (op (var 2) (var 1))) , (var 1)) → ⊥
  cut752  adequate = bad752  (Adequate.valid adequate Two boolean env4)
  bad753 : PathP (λ _ → Two) (bop (bop b0 (bop b0 b1)) (bop b1 b0)) b1 → ⊥
  bad753  p = false≢true (cong lower p)
  cut753 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (var 2))) (op (var 2) (var 1))) , (var 2)) → ⊥
  cut753  adequate = bad753  (Adequate.valid adequate Two boolean env2)
  bad754 : PathP (λ _ → Two) (bop (bop b0 (bop b0 b0)) (bop b0 b0)) b1 → ⊥
  bad754  p = false≢true (cong lower p)
  cut754 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (var 2))) (op (var 2) (var 1))) , (var 3)) → ⊥
  cut754  adequate = bad754  (Adequate.valid adequate Two boolean env5)
  bad755 : PathP (λ _ → Two) (bop (bop b0 (bop b0 b1)) (bop b1 b1)) b0 → ⊥
  bad755  p = false≢true (sym (cong lower p))
  cut755 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (var 2))) (op (var 2) (var 2))) , (var 0)) → ⊥
  cut755  adequate = bad755  (Adequate.valid adequate Two boolean env2)
  bad756 : PathP (λ _ → Two) (bop (bop b0 (bop b0 b1)) (bop b1 b1)) b0 → ⊥
  bad756  p = false≢true (sym (cong lower p))
  cut756 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (var 2))) (op (var 2) (var 2))) , (var 1)) → ⊥
  cut756  adequate = bad756  (Adequate.valid adequate Two boolean env2)
  bad757 : PathP (λ _ → Two) (bop (bop b1 (bop b0 b0)) (bop b0 b0)) b0 → ⊥
  bad757  p = false≢true (sym (cong lower p))
  cut757 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (var 2))) (op (var 2) (var 2))) , (var 2)) → ⊥
  cut757  adequate = bad757  (Adequate.valid adequate Two boolean env7)
  bad758 : PathP (λ _ → Two) (bop (bop b0 (bop b0 b0)) (bop b0 b0)) b1 → ⊥
  bad758  p = false≢true (cong lower p)
  cut758 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (var 2))) (op (var 2) (var 2))) , (var 3)) → ⊥
  cut758  adequate = bad758  (Adequate.valid adequate Two boolean env5)
  bad759 : PathP (λ _ → Two) (bop (bop b0 (bop b0 b1)) (bop b1 b1)) b0 → ⊥
  bad759  p = false≢true (sym (cong lower p))
  cut759 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (var 2))) (op (var 2) (var 3))) , (var 0)) → ⊥
  cut759  adequate = bad759  (Adequate.valid adequate Two boolean env8)
  bad760 : PathP (λ _ → Two) (bop (bop b0 (bop b0 b1)) (bop b1 b1)) b0 → ⊥
  bad760  p = false≢true (sym (cong lower p))
  cut760 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (var 2))) (op (var 2) (var 3))) , (var 1)) → ⊥
  cut760  adequate = bad760  (Adequate.valid adequate Two boolean env8)
  bad761 : PathP (λ _ → Two) (bop (bop b0 (bop b0 b1)) (bop b1 b0)) b1 → ⊥
  bad761  p = false≢true (cong lower p)
  cut761 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (var 2))) (op (var 2) (var 3))) , (var 2)) → ⊥
  cut761  adequate = bad761  (Adequate.valid adequate Two boolean env9)
  bad762 : PathP (λ _ → Two) (bop (bop b0 (bop b0 b0)) (bop b0 b1)) b1 → ⊥
  bad762  p = false≢true (cong lower p)
  cut762 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (var 2))) (op (var 2) (var 3))) , (var 3)) → ⊥
  cut762  adequate = bad762  (Adequate.valid adequate Two boolean env5)
  bad763 : PathP (λ _ → Two) (bop (bop b0 (bop b0 b0)) (bop b0 b0)) b1 → ⊥
  bad763  p = false≢true (cong lower p)
  cut763 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (var 2))) (op (var 2) (var 3))) , (var 4)) → ⊥
  cut763  adequate = bad763  (Adequate.valid adequate Two boolean env10)
  bad764 : PathP (λ _ → Two) (bop (bop b1 (bop b1 b1)) (bop b0 b1)) b1 → ⊥
  bad764  p = false≢true (cong lower p)
  cut764 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (var 2))) (op (var 3) (var 0))) , (var 0)) → ⊥
  cut764  adequate = bad764  (Adequate.valid adequate Two boolean env11)
  bad765 : PathP (λ _ → Two) (bop (bop b0 (bop b1 b0)) (bop b0 b0)) b1 → ⊥
  bad765  p = false≢true (cong lower p)
  cut765 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (var 2))) (op (var 3) (var 0))) , (var 1)) → ⊥
  cut765  adequate = bad765  (Adequate.valid adequate Two boolean env12)
  bad766 : PathP (λ _ → Two) (bop (bop b0 (bop b0 b1)) (bop b0 b0)) b1 → ⊥
  bad766  p = false≢true (cong lower p)
  cut766 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (var 2))) (op (var 3) (var 0))) , (var 2)) → ⊥
  cut766  adequate = bad766  (Adequate.valid adequate Two boolean env9)
  bad767 : PathP (λ _ → Two) (bop (bop b0 (bop b0 b0)) (bop b1 b0)) b1 → ⊥
  bad767  p = false≢true (cong lower p)
  cut767 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (var 2))) (op (var 3) (var 0))) , (var 3)) → ⊥
  cut767  adequate = bad767  (Adequate.valid adequate Two boolean env5)
  bad768 : PathP (λ _ → Two) (bop (bop b0 (bop b0 b0)) (bop b0 b0)) b1 → ⊥
  bad768  p = false≢true (cong lower p)
  cut768 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (var 2))) (op (var 3) (var 0))) , (var 4)) → ⊥
  cut768  adequate = bad768  (Adequate.valid adequate Two boolean env10)
  bad769 : PathP (λ _ → Two) (bop (bop b0 (bop b1 b0)) (bop b1 b1)) b0 → ⊥
  bad769  p = false≢true (sym (cong lower p))
  cut769 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (var 2))) (op (var 3) (var 1))) , (var 0)) → ⊥
  cut769  adequate = bad769  (Adequate.valid adequate Two boolean env13)
  bad770 : PathP (λ _ → Two) (bop (bop b0 (bop b1 b0)) (bop b0 b1)) b1 → ⊥
  bad770  p = false≢true (cong lower p)
  cut770 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (var 2))) (op (var 3) (var 1))) , (var 1)) → ⊥
  cut770  adequate = bad770  (Adequate.valid adequate Two boolean env12)
  bad771 : PathP (λ _ → Two) (bop (bop b0 (bop b0 b1)) (bop b0 b0)) b1 → ⊥
  bad771  p = false≢true (cong lower p)
  cut771 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (var 2))) (op (var 3) (var 1))) , (var 2)) → ⊥
  cut771  adequate = bad771  (Adequate.valid adequate Two boolean env9)
  bad772 : PathP (λ _ → Two) (bop (bop b0 (bop b0 b0)) (bop b1 b0)) b1 → ⊥
  bad772  p = false≢true (cong lower p)
  cut772 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (var 2))) (op (var 3) (var 1))) , (var 3)) → ⊥
  cut772  adequate = bad772  (Adequate.valid adequate Two boolean env5)
  bad773 : PathP (λ _ → Two) (bop (bop b0 (bop b0 b0)) (bop b0 b0)) b1 → ⊥
  bad773  p = false≢true (cong lower p)
  cut773 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (var 2))) (op (var 3) (var 1))) , (var 4)) → ⊥
  cut773  adequate = bad773  (Adequate.valid adequate Two boolean env10)
  bad774 : PathP (λ _ → Two) (bop (bop b0 (bop b0 b1)) (bop b1 b1)) b0 → ⊥
  bad774  p = false≢true (sym (cong lower p))
  cut774 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (var 2))) (op (var 3) (var 2))) , (var 0)) → ⊥
  cut774  adequate = bad774  (Adequate.valid adequate Two boolean env8)
  bad775 : PathP (λ _ → Two) (bop (bop b0 (bop b0 b1)) (bop b1 b1)) b0 → ⊥
  bad775  p = false≢true (sym (cong lower p))
  cut775 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (var 2))) (op (var 3) (var 2))) , (var 1)) → ⊥
  cut775  adequate = bad775  (Adequate.valid adequate Two boolean env8)
  bad776 : PathP (λ _ → Two) (bop (bop b0 (bop b0 b1)) (bop b0 b1)) b1 → ⊥
  bad776  p = false≢true (cong lower p)
  cut776 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (var 2))) (op (var 3) (var 2))) , (var 2)) → ⊥
  cut776  adequate = bad776  (Adequate.valid adequate Two boolean env9)
  bad777 : PathP (λ _ → Two) (bop (bop b0 (bop b0 b0)) (bop b1 b0)) b1 → ⊥
  bad777  p = false≢true (cong lower p)
  cut777 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (var 2))) (op (var 3) (var 2))) , (var 3)) → ⊥
  cut777  adequate = bad777  (Adequate.valid adequate Two boolean env5)
  bad778 : PathP (λ _ → Two) (bop (bop b0 (bop b0 b0)) (bop b0 b0)) b1 → ⊥
  bad778  p = false≢true (cong lower p)
  cut778 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (var 2))) (op (var 3) (var 2))) , (var 4)) → ⊥
  cut778  adequate = bad778  (Adequate.valid adequate Two boolean env10)
  bad779 : PathP (λ _ → Two) (bop (bop b0 (bop b0 b0)) (bop b1 b1)) b0 → ⊥
  bad779  p = false≢true (sym (cong lower p))
  cut779 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (var 2))) (op (var 3) (var 3))) , (var 0)) → ⊥
  cut779  adequate = bad779  (Adequate.valid adequate Two boolean env5)
  bad780 : PathP (λ _ → Two) (bop (bop b0 (bop b0 b0)) (bop b1 b1)) b0 → ⊥
  bad780  p = false≢true (sym (cong lower p))
  cut780 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (var 2))) (op (var 3) (var 3))) , (var 1)) → ⊥
  cut780  adequate = bad780  (Adequate.valid adequate Two boolean env5)
  bad781 : PathP (λ _ → Two) (bop (bop b0 (bop b0 b0)) (bop b1 b1)) b0 → ⊥
  bad781  p = false≢true (sym (cong lower p))
  cut781 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (var 2))) (op (var 3) (var 3))) , (var 2)) → ⊥
  cut781  adequate = bad781  (Adequate.valid adequate Two boolean env5)
  env14 : ℕ → Two
  env14 zero = b1
  env14 (suc zero) = b0
  env14 (suc (suc zero)) = b0
  env14 (suc (suc (suc zero))) = b0
  env14 (suc (suc (suc (suc rest)))) = b0
  bad782 : PathP (λ _ → Two) (bop (bop b1 (bop b0 b0)) (bop b0 b0)) b0 → ⊥
  bad782  p = false≢true (sym (cong lower p))
  cut782 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (var 2))) (op (var 3) (var 3))) , (var 3)) → ⊥
  cut782  adequate = bad782  (Adequate.valid adequate Two boolean env14)
  bad783 : PathP (λ _ → Two) (bop (bop b0 (bop b0 b0)) (bop b0 b0)) b1 → ⊥
  bad783  p = false≢true (cong lower p)
  cut783 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (var 2))) (op (var 3) (var 3))) , (var 4)) → ⊥
  cut783  adequate = bad783  (Adequate.valid adequate Two boolean env10)
  env15 : ℕ → Two
  env15 zero = b0
  env15 (suc zero) = b0
  env15 (suc (suc zero)) = b0
  env15 (suc (suc (suc zero))) = b1
  env15 (suc (suc (suc (suc zero)))) = b1
  env15 (suc (suc (suc (suc (suc rest))))) = b0
  bad784 : PathP (λ _ → Two) (bop (bop b0 (bop b0 b0)) (bop b1 b1)) b0 → ⊥
  bad784  p = false≢true (sym (cong lower p))
  cut784 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (var 2))) (op (var 3) (var 4))) , (var 0)) → ⊥
  cut784  adequate = bad784  (Adequate.valid adequate Two boolean env15)
  bad785 : PathP (λ _ → Two) (bop (bop b0 (bop b0 b0)) (bop b1 b1)) b0 → ⊥
  bad785  p = false≢true (sym (cong lower p))
  cut785 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (var 2))) (op (var 3) (var 4))) , (var 1)) → ⊥
  cut785  adequate = bad785  (Adequate.valid adequate Two boolean env15)
  bad786 : PathP (λ _ → Two) (bop (bop b0 (bop b0 b0)) (bop b1 b1)) b0 → ⊥
  bad786  p = false≢true (sym (cong lower p))
  cut786 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (var 2))) (op (var 3) (var 4))) , (var 2)) → ⊥
  cut786  adequate = bad786  (Adequate.valid adequate Two boolean env15)
  env16 : ℕ → Two
  env16 zero = b0
  env16 (suc zero) = b0
  env16 (suc (suc zero)) = b0
  env16 (suc (suc (suc zero))) = b1
  env16 (suc (suc (suc (suc zero)))) = b0
  env16 (suc (suc (suc (suc (suc rest))))) = b0
  bad787 : PathP (λ _ → Two) (bop (bop b0 (bop b0 b0)) (bop b1 b0)) b1 → ⊥
  bad787  p = false≢true (cong lower p)
  cut787 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (var 2))) (op (var 3) (var 4))) , (var 3)) → ⊥
  cut787  adequate = bad787  (Adequate.valid adequate Two boolean env16)
  bad788 : PathP (λ _ → Two) (bop (bop b0 (bop b0 b0)) (bop b0 b1)) b1 → ⊥
  bad788  p = false≢true (cong lower p)
  cut788 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (var 2))) (op (var 3) (var 4))) , (var 4)) → ⊥
  cut788  adequate = bad788  (Adequate.valid adequate Two boolean env10)
  env17 : ℕ → Two
  env17 zero = b0
  env17 (suc zero) = b0
  env17 (suc (suc zero)) = b0
  env17 (suc (suc (suc zero))) = b0
  env17 (suc (suc (suc (suc zero)))) = b0
  env17 (suc (suc (suc (suc (suc zero))))) = b1
  env17 (suc (suc (suc (suc (suc (suc rest)))))) = b0
  bad789 : PathP (λ _ → Two) (bop (bop b0 (bop b0 b0)) (bop b0 b0)) b1 → ⊥
  bad789  p = false≢true (cong lower p)
  cut789 : Adequate {ℓ} ((op (op (var 0) (op (var 1) (var 2))) (op (var 3) (var 4))) , (var 5)) → ⊥
  cut789  adequate = bad789  (Adequate.valid adequate Two boolean env17)
