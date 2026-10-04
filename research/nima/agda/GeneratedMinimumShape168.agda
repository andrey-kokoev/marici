{-# OPTIONS --safe --cubical --guardedness #-}
module GeneratedMinimumShape168 where
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
  holds1540 : (z0 : A1) → (mul1 (mul1 z0 z0) (mul1 z0 (mul1 z0 (mul1 z0 z0)))) ≡ z0
  holds1540 m1c0 = refl
  holds1540 m1c1 = refl
  cut1540 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (var 0) (op (var 0) (op (var 0) (var 0))))) , (var 0)) → ⊥
  cut1540  = reject1 ((op (op (var 0) (var 0)) (op (var 0) (op (var 0) (op (var 0) (var 0))))) , (var 0)) (λ env → holds1540 (env 0))
  env0 : ℕ → Two
  env0 zero = b0
  env0 (suc zero) = b1
  env0 (suc (suc rest)) = b0
  bad1541 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop b0 (bop b0 b0)))) b1 → ⊥
  bad1541  p = false≢true (cong lower p)
  cut1541 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (var 0) (op (var 0) (op (var 0) (var 0))))) , (var 1)) → ⊥
  cut1541  adequate = bad1541  (Adequate.valid adequate Two boolean env0)
  holds1542 : (z0 z1 : A2) → (mul2 (mul2 z0 z0) (mul2 z0 (mul2 z0 (mul2 z0 z1)))) ≡ z0
  holds1542 z0 z1 = refl
  cut1542 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (var 0) (op (var 0) (op (var 0) (var 1))))) , (var 0)) → ⊥
  cut1542  = reject2 ((op (op (var 0) (var 0)) (op (var 0) (op (var 0) (op (var 0) (var 1))))) , (var 0)) (λ env → holds1542 (env 0) (env 1))
  bad1543 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop b0 (bop b0 b1)))) b1 → ⊥
  bad1543  p = false≢true (cong lower p)
  cut1543 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (var 0) (op (var 0) (op (var 0) (var 1))))) , (var 1)) → ⊥
  cut1543  adequate = bad1543  (Adequate.valid adequate Two boolean env0)
  env1 : ℕ → Two
  env1 zero = b0
  env1 (suc zero) = b0
  env1 (suc (suc zero)) = b1
  env1 (suc (suc (suc rest))) = b0
  bad1544 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop b0 (bop b0 b0)))) b1 → ⊥
  bad1544  p = false≢true (cong lower p)
  cut1544 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (var 0) (op (var 0) (op (var 0) (var 1))))) , (var 2)) → ⊥
  cut1544  adequate = bad1544  (Adequate.valid adequate Two boolean env1)
  holds1545 : (z0 z1 : A2) → (mul2 (mul2 z0 z0) (mul2 z0 (mul2 z0 (mul2 z1 z0)))) ≡ z0
  holds1545 z0 z1 = refl
  cut1545 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (var 0) (op (var 0) (op (var 1) (var 0))))) , (var 0)) → ⊥
  cut1545  = reject2 ((op (op (var 0) (var 0)) (op (var 0) (op (var 0) (op (var 1) (var 0))))) , (var 0)) (λ env → holds1545 (env 0) (env 1))
  bad1546 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop b0 (bop b1 b0)))) b1 → ⊥
  bad1546  p = false≢true (cong lower p)
  cut1546 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (var 0) (op (var 0) (op (var 1) (var 0))))) , (var 1)) → ⊥
  cut1546  adequate = bad1546  (Adequate.valid adequate Two boolean env0)
  bad1547 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop b0 (bop b0 b0)))) b1 → ⊥
  bad1547  p = false≢true (cong lower p)
  cut1547 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (var 0) (op (var 0) (op (var 1) (var 0))))) , (var 2)) → ⊥
  cut1547  adequate = bad1547  (Adequate.valid adequate Two boolean env1)
  holds1548 : (z0 z1 : A2) → (mul2 (mul2 z0 z0) (mul2 z0 (mul2 z0 (mul2 z1 z1)))) ≡ z0
  holds1548 z0 z1 = refl
  cut1548 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (var 0) (op (var 0) (op (var 1) (var 1))))) , (var 0)) → ⊥
  cut1548  = reject2 ((op (op (var 0) (var 0)) (op (var 0) (op (var 0) (op (var 1) (var 1))))) , (var 0)) (λ env → holds1548 (env 0) (env 1))
  bad1549 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop b0 (bop b1 b1)))) b1 → ⊥
  bad1549  p = false≢true (cong lower p)
  cut1549 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (var 0) (op (var 0) (op (var 1) (var 1))))) , (var 1)) → ⊥
  cut1549  adequate = bad1549  (Adequate.valid adequate Two boolean env0)
  bad1550 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop b0 (bop b0 b0)))) b1 → ⊥
  bad1550  p = false≢true (cong lower p)
  cut1550 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (var 0) (op (var 0) (op (var 1) (var 1))))) , (var 2)) → ⊥
  cut1550  adequate = bad1550  (Adequate.valid adequate Two boolean env1)
  holds1551 : (z0 z1 z2 : A2) → (mul2 (mul2 z0 z0) (mul2 z0 (mul2 z0 (mul2 z1 z2)))) ≡ z0
  holds1551 z0 z1 z2 = refl
  cut1551 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (var 0) (op (var 0) (op (var 1) (var 2))))) , (var 0)) → ⊥
  cut1551  = reject2 ((op (op (var 0) (var 0)) (op (var 0) (op (var 0) (op (var 1) (var 2))))) , (var 0)) (λ env → holds1551 (env 0) (env 1) (env 2))
  env2 : ℕ → Two
  env2 zero = b0
  env2 (suc zero) = b1
  env2 (suc (suc zero)) = b0
  env2 (suc (suc (suc rest))) = b0
  bad1552 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop b0 (bop b1 b0)))) b1 → ⊥
  bad1552  p = false≢true (cong lower p)
  cut1552 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (var 0) (op (var 0) (op (var 1) (var 2))))) , (var 1)) → ⊥
  cut1552  adequate = bad1552  (Adequate.valid adequate Two boolean env2)
  bad1553 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop b0 (bop b0 b1)))) b1 → ⊥
  bad1553  p = false≢true (cong lower p)
  cut1553 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (var 0) (op (var 0) (op (var 1) (var 2))))) , (var 2)) → ⊥
  cut1553  adequate = bad1553  (Adequate.valid adequate Two boolean env1)
  env3 : ℕ → Two
  env3 zero = b0
  env3 (suc zero) = b0
  env3 (suc (suc zero)) = b0
  env3 (suc (suc (suc zero))) = b1
  env3 (suc (suc (suc (suc rest)))) = b0
  bad1554 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop b0 (bop b0 b0)))) b1 → ⊥
  bad1554  p = false≢true (cong lower p)
  cut1554 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (var 0) (op (var 0) (op (var 1) (var 2))))) , (var 3)) → ⊥
  cut1554  adequate = bad1554  (Adequate.valid adequate Two boolean env3)
  holds1555 : (z0 z1 : A2) → (mul2 (mul2 z0 z0) (mul2 z0 (mul2 z1 (mul2 z0 z0)))) ≡ z0
  holds1555 z0 z1 = refl
  cut1555 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (var 0) (op (var 1) (op (var 0) (var 0))))) , (var 0)) → ⊥
  cut1555  = reject2 ((op (op (var 0) (var 0)) (op (var 0) (op (var 1) (op (var 0) (var 0))))) , (var 0)) (λ env → holds1555 (env 0) (env 1))
  bad1556 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop b1 (bop b0 b0)))) b1 → ⊥
  bad1556  p = false≢true (cong lower p)
  cut1556 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (var 0) (op (var 1) (op (var 0) (var 0))))) , (var 1)) → ⊥
  cut1556  adequate = bad1556  (Adequate.valid adequate Two boolean env0)
  bad1557 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop b0 (bop b0 b0)))) b1 → ⊥
  bad1557  p = false≢true (cong lower p)
  cut1557 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (var 0) (op (var 1) (op (var 0) (var 0))))) , (var 2)) → ⊥
  cut1557  adequate = bad1557  (Adequate.valid adequate Two boolean env1)
  holds1558 : (z0 z1 : A2) → (mul2 (mul2 z0 z0) (mul2 z0 (mul2 z1 (mul2 z0 z1)))) ≡ z0
  holds1558 z0 z1 = refl
  cut1558 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (var 0) (op (var 1) (op (var 0) (var 1))))) , (var 0)) → ⊥
  cut1558  = reject2 ((op (op (var 0) (var 0)) (op (var 0) (op (var 1) (op (var 0) (var 1))))) , (var 0)) (λ env → holds1558 (env 0) (env 1))
  bad1559 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop b1 (bop b0 b1)))) b1 → ⊥
  bad1559  p = false≢true (cong lower p)
  cut1559 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (var 0) (op (var 1) (op (var 0) (var 1))))) , (var 1)) → ⊥
  cut1559  adequate = bad1559  (Adequate.valid adequate Two boolean env0)
  bad1560 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop b0 (bop b0 b0)))) b1 → ⊥
  bad1560  p = false≢true (cong lower p)
  cut1560 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (var 0) (op (var 1) (op (var 0) (var 1))))) , (var 2)) → ⊥
  cut1560  adequate = bad1560  (Adequate.valid adequate Two boolean env1)
  holds1561 : (z0 z1 z2 : A2) → (mul2 (mul2 z0 z0) (mul2 z0 (mul2 z1 (mul2 z0 z2)))) ≡ z0
  holds1561 z0 z1 z2 = refl
  cut1561 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (var 0) (op (var 1) (op (var 0) (var 2))))) , (var 0)) → ⊥
  cut1561  = reject2 ((op (op (var 0) (var 0)) (op (var 0) (op (var 1) (op (var 0) (var 2))))) , (var 0)) (λ env → holds1561 (env 0) (env 1) (env 2))
  bad1562 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop b1 (bop b0 b0)))) b1 → ⊥
  bad1562  p = false≢true (cong lower p)
  cut1562 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (var 0) (op (var 1) (op (var 0) (var 2))))) , (var 1)) → ⊥
  cut1562  adequate = bad1562  (Adequate.valid adequate Two boolean env2)
  bad1563 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop b0 (bop b0 b1)))) b1 → ⊥
  bad1563  p = false≢true (cong lower p)
  cut1563 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (var 0) (op (var 1) (op (var 0) (var 2))))) , (var 2)) → ⊥
  cut1563  adequate = bad1563  (Adequate.valid adequate Two boolean env1)
  bad1564 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop b0 (bop b0 b0)))) b1 → ⊥
  bad1564  p = false≢true (cong lower p)
  cut1564 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (var 0) (op (var 1) (op (var 0) (var 2))))) , (var 3)) → ⊥
  cut1564  adequate = bad1564  (Adequate.valid adequate Two boolean env3)
  holds1565 : (z0 z1 : A2) → (mul2 (mul2 z0 z0) (mul2 z0 (mul2 z1 (mul2 z1 z0)))) ≡ z0
  holds1565 z0 z1 = refl
  cut1565 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (var 0) (op (var 1) (op (var 1) (var 0))))) , (var 0)) → ⊥
  cut1565  = reject2 ((op (op (var 0) (var 0)) (op (var 0) (op (var 1) (op (var 1) (var 0))))) , (var 0)) (λ env → holds1565 (env 0) (env 1))
  bad1566 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop b1 (bop b1 b0)))) b1 → ⊥
  bad1566  p = false≢true (cong lower p)
  cut1566 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (var 0) (op (var 1) (op (var 1) (var 0))))) , (var 1)) → ⊥
  cut1566  adequate = bad1566  (Adequate.valid adequate Two boolean env0)
  bad1567 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop b0 (bop b0 b0)))) b1 → ⊥
  bad1567  p = false≢true (cong lower p)
  cut1567 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (var 0) (op (var 1) (op (var 1) (var 0))))) , (var 2)) → ⊥
  cut1567  adequate = bad1567  (Adequate.valid adequate Two boolean env1)
  holds1568 : (z0 z1 : A2) → (mul2 (mul2 z0 z0) (mul2 z0 (mul2 z1 (mul2 z1 z1)))) ≡ z0
  holds1568 z0 z1 = refl
  cut1568 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (var 0) (op (var 1) (op (var 1) (var 1))))) , (var 0)) → ⊥
  cut1568  = reject2 ((op (op (var 0) (var 0)) (op (var 0) (op (var 1) (op (var 1) (var 1))))) , (var 0)) (λ env → holds1568 (env 0) (env 1))
  bad1569 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop b1 (bop b1 b1)))) b1 → ⊥
  bad1569  p = false≢true (cong lower p)
  cut1569 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (var 0) (op (var 1) (op (var 1) (var 1))))) , (var 1)) → ⊥
  cut1569  adequate = bad1569  (Adequate.valid adequate Two boolean env0)
  bad1570 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop b0 (bop b0 b0)))) b1 → ⊥
  bad1570  p = false≢true (cong lower p)
  cut1570 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (var 0) (op (var 1) (op (var 1) (var 1))))) , (var 2)) → ⊥
  cut1570  adequate = bad1570  (Adequate.valid adequate Two boolean env1)
  holds1571 : (z0 z1 z2 : A2) → (mul2 (mul2 z0 z0) (mul2 z0 (mul2 z1 (mul2 z1 z2)))) ≡ z0
  holds1571 z0 z1 z2 = refl
  cut1571 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (var 0) (op (var 1) (op (var 1) (var 2))))) , (var 0)) → ⊥
  cut1571  = reject2 ((op (op (var 0) (var 0)) (op (var 0) (op (var 1) (op (var 1) (var 2))))) , (var 0)) (λ env → holds1571 (env 0) (env 1) (env 2))
  bad1572 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop b1 (bop b1 b0)))) b1 → ⊥
  bad1572  p = false≢true (cong lower p)
  cut1572 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (var 0) (op (var 1) (op (var 1) (var 2))))) , (var 1)) → ⊥
  cut1572  adequate = bad1572  (Adequate.valid adequate Two boolean env2)
  bad1573 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop b0 (bop b0 b1)))) b1 → ⊥
  bad1573  p = false≢true (cong lower p)
  cut1573 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (var 0) (op (var 1) (op (var 1) (var 2))))) , (var 2)) → ⊥
  cut1573  adequate = bad1573  (Adequate.valid adequate Two boolean env1)
  bad1574 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop b0 (bop b0 b0)))) b1 → ⊥
  bad1574  p = false≢true (cong lower p)
  cut1574 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (var 0) (op (var 1) (op (var 1) (var 2))))) , (var 3)) → ⊥
  cut1574  adequate = bad1574  (Adequate.valid adequate Two boolean env3)
  holds1575 : (z0 z1 z2 : A2) → (mul2 (mul2 z0 z0) (mul2 z0 (mul2 z1 (mul2 z2 z0)))) ≡ z0
  holds1575 z0 z1 z2 = refl
  cut1575 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (var 0) (op (var 1) (op (var 2) (var 0))))) , (var 0)) → ⊥
  cut1575  = reject2 ((op (op (var 0) (var 0)) (op (var 0) (op (var 1) (op (var 2) (var 0))))) , (var 0)) (λ env → holds1575 (env 0) (env 1) (env 2))
  bad1576 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop b1 (bop b0 b0)))) b1 → ⊥
  bad1576  p = false≢true (cong lower p)
  cut1576 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (var 0) (op (var 1) (op (var 2) (var 0))))) , (var 1)) → ⊥
  cut1576  adequate = bad1576  (Adequate.valid adequate Two boolean env2)
  bad1577 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop b0 (bop b1 b0)))) b1 → ⊥
  bad1577  p = false≢true (cong lower p)
  cut1577 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (var 0) (op (var 1) (op (var 2) (var 0))))) , (var 2)) → ⊥
  cut1577  adequate = bad1577  (Adequate.valid adequate Two boolean env1)
  bad1578 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop b0 (bop b0 b0)))) b1 → ⊥
  bad1578  p = false≢true (cong lower p)
  cut1578 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (var 0) (op (var 1) (op (var 2) (var 0))))) , (var 3)) → ⊥
  cut1578  adequate = bad1578  (Adequate.valid adequate Two boolean env3)
  holds1579 : (z0 z1 z2 : A2) → (mul2 (mul2 z0 z0) (mul2 z0 (mul2 z1 (mul2 z2 z1)))) ≡ z0
  holds1579 z0 z1 z2 = refl
  cut1579 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (var 0) (op (var 1) (op (var 2) (var 1))))) , (var 0)) → ⊥
  cut1579  = reject2 ((op (op (var 0) (var 0)) (op (var 0) (op (var 1) (op (var 2) (var 1))))) , (var 0)) (λ env → holds1579 (env 0) (env 1) (env 2))
  bad1580 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop b1 (bop b0 b1)))) b1 → ⊥
  bad1580  p = false≢true (cong lower p)
  cut1580 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (var 0) (op (var 1) (op (var 2) (var 1))))) , (var 1)) → ⊥
  cut1580  adequate = bad1580  (Adequate.valid adequate Two boolean env2)
  bad1581 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop b0 (bop b1 b0)))) b1 → ⊥
  bad1581  p = false≢true (cong lower p)
  cut1581 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (var 0) (op (var 1) (op (var 2) (var 1))))) , (var 2)) → ⊥
  cut1581  adequate = bad1581  (Adequate.valid adequate Two boolean env1)
  bad1582 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop b0 (bop b0 b0)))) b1 → ⊥
  bad1582  p = false≢true (cong lower p)
  cut1582 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (var 0) (op (var 1) (op (var 2) (var 1))))) , (var 3)) → ⊥
  cut1582  adequate = bad1582  (Adequate.valid adequate Two boolean env3)
  holds1583 : (z0 z1 z2 : A2) → (mul2 (mul2 z0 z0) (mul2 z0 (mul2 z1 (mul2 z2 z2)))) ≡ z0
  holds1583 z0 z1 z2 = refl
  cut1583 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (var 0) (op (var 1) (op (var 2) (var 2))))) , (var 0)) → ⊥
  cut1583  = reject2 ((op (op (var 0) (var 0)) (op (var 0) (op (var 1) (op (var 2) (var 2))))) , (var 0)) (λ env → holds1583 (env 0) (env 1) (env 2))
  bad1584 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop b1 (bop b0 b0)))) b1 → ⊥
  bad1584  p = false≢true (cong lower p)
  cut1584 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (var 0) (op (var 1) (op (var 2) (var 2))))) , (var 1)) → ⊥
  cut1584  adequate = bad1584  (Adequate.valid adequate Two boolean env2)
  bad1585 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop b0 (bop b1 b1)))) b1 → ⊥
  bad1585  p = false≢true (cong lower p)
  cut1585 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (var 0) (op (var 1) (op (var 2) (var 2))))) , (var 2)) → ⊥
  cut1585  adequate = bad1585  (Adequate.valid adequate Two boolean env1)
  bad1586 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop b0 (bop b0 b0)))) b1 → ⊥
  bad1586  p = false≢true (cong lower p)
  cut1586 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (var 0) (op (var 1) (op (var 2) (var 2))))) , (var 3)) → ⊥
  cut1586  adequate = bad1586  (Adequate.valid adequate Two boolean env3)
  holds1587 : (z0 z1 z2 z3 : A2) → (mul2 (mul2 z0 z0) (mul2 z0 (mul2 z1 (mul2 z2 z3)))) ≡ z0
  holds1587 z0 z1 z2 z3 = refl
  cut1587 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (var 0) (op (var 1) (op (var 2) (var 3))))) , (var 0)) → ⊥
  cut1587  = reject2 ((op (op (var 0) (var 0)) (op (var 0) (op (var 1) (op (var 2) (var 3))))) , (var 0)) (λ env → holds1587 (env 0) (env 1) (env 2) (env 3))
  env4 : ℕ → Two
  env4 zero = b0
  env4 (suc zero) = b1
  env4 (suc (suc zero)) = b0
  env4 (suc (suc (suc zero))) = b0
  env4 (suc (suc (suc (suc rest)))) = b0
  bad1588 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop b1 (bop b0 b0)))) b1 → ⊥
  bad1588  p = false≢true (cong lower p)
  cut1588 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (var 0) (op (var 1) (op (var 2) (var 3))))) , (var 1)) → ⊥
  cut1588  adequate = bad1588  (Adequate.valid adequate Two boolean env4)
  env5 : ℕ → Two
  env5 zero = b0
  env5 (suc zero) = b0
  env5 (suc (suc zero)) = b1
  env5 (suc (suc (suc zero))) = b0
  env5 (suc (suc (suc (suc rest)))) = b0
  bad1589 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop b0 (bop b1 b0)))) b1 → ⊥
  bad1589  p = false≢true (cong lower p)
  cut1589 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (var 0) (op (var 1) (op (var 2) (var 3))))) , (var 2)) → ⊥
  cut1589  adequate = bad1589  (Adequate.valid adequate Two boolean env5)
  bad1590 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop b0 (bop b0 b1)))) b1 → ⊥
  bad1590  p = false≢true (cong lower p)
  cut1590 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (var 0) (op (var 1) (op (var 2) (var 3))))) , (var 3)) → ⊥
  cut1590  adequate = bad1590  (Adequate.valid adequate Two boolean env3)
  env6 : ℕ → Two
  env6 zero = b0
  env6 (suc zero) = b0
  env6 (suc (suc zero)) = b0
  env6 (suc (suc (suc zero))) = b0
  env6 (suc (suc (suc (suc zero)))) = b1
  env6 (suc (suc (suc (suc (suc rest))))) = b0
  bad1591 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop b0 (bop b0 b0)))) b1 → ⊥
  bad1591  p = false≢true (cong lower p)
  cut1591 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (var 0) (op (var 1) (op (var 2) (var 3))))) , (var 4)) → ⊥
  cut1591  adequate = bad1591  (Adequate.valid adequate Two boolean env6)
  bad1592 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b1 (bop b0 (bop b0 b0)))) b0 → ⊥
  bad1592  p = false≢true (sym (cong lower p))
  cut1592 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (var 1) (op (var 0) (op (var 0) (var 0))))) , (var 0)) → ⊥
  cut1592  adequate = bad1592  (Adequate.valid adequate Two boolean env0)
  env7 : ℕ → Two
  env7 zero = b1
  env7 (suc zero) = b0
  env7 (suc (suc rest)) = b0
  bad1593 : PathP (λ _ → Two) (bop (bop b1 b1) (bop b0 (bop b1 (bop b1 b1)))) b0 → ⊥
  bad1593  p = false≢true (sym (cong lower p))
  cut1593 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (var 1) (op (var 0) (op (var 0) (var 0))))) , (var 1)) → ⊥
  cut1593  adequate = bad1593  (Adequate.valid adequate Two boolean env7)
  bad1594 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop b0 (bop b0 b0)))) b1 → ⊥
  bad1594  p = false≢true (cong lower p)
  cut1594 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (var 1) (op (var 0) (op (var 0) (var 0))))) , (var 2)) → ⊥
  cut1594  adequate = bad1594  (Adequate.valid adequate Two boolean env1)
  bad1595 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b1 (bop b0 (bop b0 b1)))) b0 → ⊥
  bad1595  p = false≢true (sym (cong lower p))
  cut1595 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (var 1) (op (var 0) (op (var 0) (var 1))))) , (var 0)) → ⊥
  cut1595  adequate = bad1595  (Adequate.valid adequate Two boolean env0)
  bad1596 : PathP (λ _ → Two) (bop (bop b1 b1) (bop b0 (bop b1 (bop b1 b0)))) b0 → ⊥
  bad1596  p = false≢true (sym (cong lower p))
  cut1596 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (var 1) (op (var 0) (op (var 0) (var 1))))) , (var 1)) → ⊥
  cut1596  adequate = bad1596  (Adequate.valid adequate Two boolean env7)
  bad1597 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop b0 (bop b0 b0)))) b1 → ⊥
  bad1597  p = false≢true (cong lower p)
  cut1597 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (var 1) (op (var 0) (op (var 0) (var 1))))) , (var 2)) → ⊥
  cut1597  adequate = bad1597  (Adequate.valid adequate Two boolean env1)
  bad1598 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b1 (bop b0 (bop b0 b0)))) b0 → ⊥
  bad1598  p = false≢true (sym (cong lower p))
  cut1598 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (var 1) (op (var 0) (op (var 0) (var 2))))) , (var 0)) → ⊥
  cut1598  adequate = bad1598  (Adequate.valid adequate Two boolean env2)
  env8 : ℕ → Two
  env8 zero = b1
  env8 (suc zero) = b0
  env8 (suc (suc zero)) = b0
  env8 (suc (suc (suc rest))) = b0
  bad1599 : PathP (λ _ → Two) (bop (bop b1 b1) (bop b0 (bop b1 (bop b1 b0)))) b0 → ⊥
  bad1599  p = false≢true (sym (cong lower p))
  cut1599 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (var 1) (op (var 0) (op (var 0) (var 2))))) , (var 1)) → ⊥
  cut1599  adequate = bad1599  (Adequate.valid adequate Two boolean env8)
  bad1600 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop b0 (bop b0 b1)))) b1 → ⊥
  bad1600  p = false≢true (cong lower p)
  cut1600 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (var 1) (op (var 0) (op (var 0) (var 2))))) , (var 2)) → ⊥
  cut1600  adequate = bad1600  (Adequate.valid adequate Two boolean env1)
  bad1601 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop b0 (bop b0 b0)))) b1 → ⊥
  bad1601  p = false≢true (cong lower p)
  cut1601 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (var 1) (op (var 0) (op (var 0) (var 2))))) , (var 3)) → ⊥
  cut1601  adequate = bad1601  (Adequate.valid adequate Two boolean env3)
  bad1602 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b1 (bop b0 (bop b1 b0)))) b0 → ⊥
  bad1602  p = false≢true (sym (cong lower p))
  cut1602 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (var 1) (op (var 0) (op (var 1) (var 0))))) , (var 0)) → ⊥
  cut1602  adequate = bad1602  (Adequate.valid adequate Two boolean env0)
  bad1603 : PathP (λ _ → Two) (bop (bop b1 b1) (bop b0 (bop b1 (bop b0 b1)))) b0 → ⊥
  bad1603  p = false≢true (sym (cong lower p))
  cut1603 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (var 1) (op (var 0) (op (var 1) (var 0))))) , (var 1)) → ⊥
  cut1603  adequate = bad1603  (Adequate.valid adequate Two boolean env7)
  bad1604 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop b0 (bop b0 b0)))) b1 → ⊥
  bad1604  p = false≢true (cong lower p)
  cut1604 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (var 1) (op (var 0) (op (var 1) (var 0))))) , (var 2)) → ⊥
  cut1604  adequate = bad1604  (Adequate.valid adequate Two boolean env1)
  bad1605 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b1 (bop b0 (bop b1 b1)))) b0 → ⊥
  bad1605  p = false≢true (sym (cong lower p))
  cut1605 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (var 1) (op (var 0) (op (var 1) (var 1))))) , (var 0)) → ⊥
  cut1605  adequate = bad1605  (Adequate.valid adequate Two boolean env0)
  bad1606 : PathP (λ _ → Two) (bop (bop b1 b1) (bop b0 (bop b1 (bop b0 b0)))) b0 → ⊥
  bad1606  p = false≢true (sym (cong lower p))
  cut1606 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (var 1) (op (var 0) (op (var 1) (var 1))))) , (var 1)) → ⊥
  cut1606  adequate = bad1606  (Adequate.valid adequate Two boolean env7)
  bad1607 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop b0 (bop b0 b0)))) b1 → ⊥
  bad1607  p = false≢true (cong lower p)
  cut1607 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (var 1) (op (var 0) (op (var 1) (var 1))))) , (var 2)) → ⊥
  cut1607  adequate = bad1607  (Adequate.valid adequate Two boolean env1)
  bad1608 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b1 (bop b0 (bop b1 b0)))) b0 → ⊥
  bad1608  p = false≢true (sym (cong lower p))
  cut1608 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (var 1) (op (var 0) (op (var 1) (var 2))))) , (var 0)) → ⊥
  cut1608  adequate = bad1608  (Adequate.valid adequate Two boolean env2)
  bad1609 : PathP (λ _ → Two) (bop (bop b1 b1) (bop b0 (bop b1 (bop b0 b0)))) b0 → ⊥
  bad1609  p = false≢true (sym (cong lower p))
  cut1609 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (var 1) (op (var 0) (op (var 1) (var 2))))) , (var 1)) → ⊥
  cut1609  adequate = bad1609  (Adequate.valid adequate Two boolean env8)
  bad1610 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop b0 (bop b0 b1)))) b1 → ⊥
  bad1610  p = false≢true (cong lower p)
  cut1610 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (var 1) (op (var 0) (op (var 1) (var 2))))) , (var 2)) → ⊥
  cut1610  adequate = bad1610  (Adequate.valid adequate Two boolean env1)
  bad1611 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop b0 (bop b0 b0)))) b1 → ⊥
  bad1611  p = false≢true (cong lower p)
  cut1611 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (var 1) (op (var 0) (op (var 1) (var 2))))) , (var 3)) → ⊥
  cut1611  adequate = bad1611  (Adequate.valid adequate Two boolean env3)
  bad1612 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b1 (bop b0 (bop b0 b0)))) b0 → ⊥
  bad1612  p = false≢true (sym (cong lower p))
  cut1612 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (var 1) (op (var 0) (op (var 2) (var 0))))) , (var 0)) → ⊥
  cut1612  adequate = bad1612  (Adequate.valid adequate Two boolean env2)
  bad1613 : PathP (λ _ → Two) (bop (bop b1 b1) (bop b0 (bop b1 (bop b0 b1)))) b0 → ⊥
  bad1613  p = false≢true (sym (cong lower p))
  cut1613 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (var 1) (op (var 0) (op (var 2) (var 0))))) , (var 1)) → ⊥
  cut1613  adequate = bad1613  (Adequate.valid adequate Two boolean env8)
  bad1614 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop b0 (bop b1 b0)))) b1 → ⊥
  bad1614  p = false≢true (cong lower p)
  cut1614 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (var 1) (op (var 0) (op (var 2) (var 0))))) , (var 2)) → ⊥
  cut1614  adequate = bad1614  (Adequate.valid adequate Two boolean env1)
  bad1615 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop b0 (bop b0 b0)))) b1 → ⊥
  bad1615  p = false≢true (cong lower p)
  cut1615 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (var 1) (op (var 0) (op (var 2) (var 0))))) , (var 3)) → ⊥
  cut1615  adequate = bad1615  (Adequate.valid adequate Two boolean env3)
  bad1616 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b1 (bop b0 (bop b0 b1)))) b0 → ⊥
  bad1616  p = false≢true (sym (cong lower p))
  cut1616 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (var 1) (op (var 0) (op (var 2) (var 1))))) , (var 0)) → ⊥
  cut1616  adequate = bad1616  (Adequate.valid adequate Two boolean env2)
  bad1617 : PathP (λ _ → Two) (bop (bop b1 b1) (bop b0 (bop b1 (bop b0 b0)))) b0 → ⊥
  bad1617  p = false≢true (sym (cong lower p))
  cut1617 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (var 1) (op (var 0) (op (var 2) (var 1))))) , (var 1)) → ⊥
  cut1617  adequate = bad1617  (Adequate.valid adequate Two boolean env8)
  bad1618 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop b0 (bop b1 b0)))) b1 → ⊥
  bad1618  p = false≢true (cong lower p)
  cut1618 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (var 1) (op (var 0) (op (var 2) (var 1))))) , (var 2)) → ⊥
  cut1618  adequate = bad1618  (Adequate.valid adequate Two boolean env1)
  bad1619 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop b0 (bop b0 b0)))) b1 → ⊥
  bad1619  p = false≢true (cong lower p)
  cut1619 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (var 1) (op (var 0) (op (var 2) (var 1))))) , (var 3)) → ⊥
  cut1619  adequate = bad1619  (Adequate.valid adequate Two boolean env3)
  bad1620 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b1 (bop b0 (bop b0 b0)))) b0 → ⊥
  bad1620  p = false≢true (sym (cong lower p))
  cut1620 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (var 1) (op (var 0) (op (var 2) (var 2))))) , (var 0)) → ⊥
  cut1620  adequate = bad1620  (Adequate.valid adequate Two boolean env2)
  bad1621 : PathP (λ _ → Two) (bop (bop b1 b1) (bop b0 (bop b1 (bop b0 b0)))) b0 → ⊥
  bad1621  p = false≢true (sym (cong lower p))
  cut1621 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (var 1) (op (var 0) (op (var 2) (var 2))))) , (var 1)) → ⊥
  cut1621  adequate = bad1621  (Adequate.valid adequate Two boolean env8)
  bad1622 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop b0 (bop b1 b1)))) b1 → ⊥
  bad1622  p = false≢true (cong lower p)
  cut1622 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (var 1) (op (var 0) (op (var 2) (var 2))))) , (var 2)) → ⊥
  cut1622  adequate = bad1622  (Adequate.valid adequate Two boolean env1)
  bad1623 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop b0 (bop b0 b0)))) b1 → ⊥
  bad1623  p = false≢true (cong lower p)
  cut1623 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (var 1) (op (var 0) (op (var 2) (var 2))))) , (var 3)) → ⊥
  cut1623  adequate = bad1623  (Adequate.valid adequate Two boolean env3)
  bad1624 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b1 (bop b0 (bop b0 b0)))) b0 → ⊥
  bad1624  p = false≢true (sym (cong lower p))
  cut1624 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (var 1) (op (var 0) (op (var 2) (var 3))))) , (var 0)) → ⊥
  cut1624  adequate = bad1624  (Adequate.valid adequate Two boolean env4)
  env9 : ℕ → Two
  env9 zero = b1
  env9 (suc zero) = b0
  env9 (suc (suc zero)) = b0
  env9 (suc (suc (suc zero))) = b0
  env9 (suc (suc (suc (suc rest)))) = b0
  bad1625 : PathP (λ _ → Two) (bop (bop b1 b1) (bop b0 (bop b1 (bop b0 b0)))) b0 → ⊥
  bad1625  p = false≢true (sym (cong lower p))
  cut1625 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (var 1) (op (var 0) (op (var 2) (var 3))))) , (var 1)) → ⊥
  cut1625  adequate = bad1625  (Adequate.valid adequate Two boolean env9)
  bad1626 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop b0 (bop b1 b0)))) b1 → ⊥
  bad1626  p = false≢true (cong lower p)
  cut1626 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (var 1) (op (var 0) (op (var 2) (var 3))))) , (var 2)) → ⊥
  cut1626  adequate = bad1626  (Adequate.valid adequate Two boolean env5)
  bad1627 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop b0 (bop b0 b1)))) b1 → ⊥
  bad1627  p = false≢true (cong lower p)
  cut1627 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (var 1) (op (var 0) (op (var 2) (var 3))))) , (var 3)) → ⊥
  cut1627  adequate = bad1627  (Adequate.valid adequate Two boolean env3)
  bad1628 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop b0 (bop b0 b0)))) b1 → ⊥
  bad1628  p = false≢true (cong lower p)
  cut1628 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (var 1) (op (var 0) (op (var 2) (var 3))))) , (var 4)) → ⊥
  cut1628  adequate = bad1628  (Adequate.valid adequate Two boolean env6)
  holds1629 : (z0 z1 : A2) → (mul2 (mul2 z0 z0) (mul2 z1 (mul2 z1 (mul2 z0 z0)))) ≡ z0
  holds1629 z0 z1 = refl
  cut1629 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (var 1) (op (var 1) (op (var 0) (var 0))))) , (var 0)) → ⊥
  cut1629  = reject2 ((op (op (var 0) (var 0)) (op (var 1) (op (var 1) (op (var 0) (var 0))))) , (var 0)) (λ env → holds1629 (env 0) (env 1))
  bad1630 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b1 (bop b1 (bop b0 b0)))) b1 → ⊥
  bad1630  p = false≢true (cong lower p)
  cut1630 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (var 1) (op (var 1) (op (var 0) (var 0))))) , (var 1)) → ⊥
  cut1630  adequate = bad1630  (Adequate.valid adequate Two boolean env0)
  bad1631 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop b0 (bop b0 b0)))) b1 → ⊥
  bad1631  p = false≢true (cong lower p)
  cut1631 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (var 1) (op (var 1) (op (var 0) (var 0))))) , (var 2)) → ⊥
  cut1631  adequate = bad1631  (Adequate.valid adequate Two boolean env1)
  holds1632 : (z0 z1 : A2) → (mul2 (mul2 z0 z0) (mul2 z1 (mul2 z1 (mul2 z0 z1)))) ≡ z0
  holds1632 z0 z1 = refl
  cut1632 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (var 1) (op (var 1) (op (var 0) (var 1))))) , (var 0)) → ⊥
  cut1632  = reject2 ((op (op (var 0) (var 0)) (op (var 1) (op (var 1) (op (var 0) (var 1))))) , (var 0)) (λ env → holds1632 (env 0) (env 1))
  bad1633 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b1 (bop b1 (bop b0 b1)))) b1 → ⊥
  bad1633  p = false≢true (cong lower p)
  cut1633 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (var 1) (op (var 1) (op (var 0) (var 1))))) , (var 1)) → ⊥
  cut1633  adequate = bad1633  (Adequate.valid adequate Two boolean env0)
  bad1634 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop b0 (bop b0 b0)))) b1 → ⊥
  bad1634  p = false≢true (cong lower p)
  cut1634 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (var 1) (op (var 1) (op (var 0) (var 1))))) , (var 2)) → ⊥
  cut1634  adequate = bad1634  (Adequate.valid adequate Two boolean env1)
  holds1635 : (z0 z1 z2 : A2) → (mul2 (mul2 z0 z0) (mul2 z1 (mul2 z1 (mul2 z0 z2)))) ≡ z0
  holds1635 z0 z1 z2 = refl
  cut1635 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (var 1) (op (var 1) (op (var 0) (var 2))))) , (var 0)) → ⊥
  cut1635  = reject2 ((op (op (var 0) (var 0)) (op (var 1) (op (var 1) (op (var 0) (var 2))))) , (var 0)) (λ env → holds1635 (env 0) (env 1) (env 2))
  bad1636 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b1 (bop b1 (bop b0 b0)))) b1 → ⊥
  bad1636  p = false≢true (cong lower p)
  cut1636 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (var 1) (op (var 1) (op (var 0) (var 2))))) , (var 1)) → ⊥
  cut1636  adequate = bad1636  (Adequate.valid adequate Two boolean env2)
  bad1637 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop b0 (bop b0 b1)))) b1 → ⊥
  bad1637  p = false≢true (cong lower p)
  cut1637 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (var 1) (op (var 1) (op (var 0) (var 2))))) , (var 2)) → ⊥
  cut1637  adequate = bad1637  (Adequate.valid adequate Two boolean env1)
  bad1638 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop b0 (bop b0 b0)))) b1 → ⊥
  bad1638  p = false≢true (cong lower p)
  cut1638 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (var 1) (op (var 1) (op (var 0) (var 2))))) , (var 3)) → ⊥
  cut1638  adequate = bad1638  (Adequate.valid adequate Two boolean env3)
  holds1639 : (z0 z1 : A2) → (mul2 (mul2 z0 z0) (mul2 z1 (mul2 z1 (mul2 z1 z0)))) ≡ z0
  holds1639 z0 z1 = refl
  cut1639 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (var 1) (op (var 1) (op (var 1) (var 0))))) , (var 0)) → ⊥
  cut1639  = reject2 ((op (op (var 0) (var 0)) (op (var 1) (op (var 1) (op (var 1) (var 0))))) , (var 0)) (λ env → holds1639 (env 0) (env 1))
  bad1640 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b1 (bop b1 (bop b1 b0)))) b1 → ⊥
  bad1640  p = false≢true (cong lower p)
  cut1640 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (var 1) (op (var 1) (op (var 1) (var 0))))) , (var 1)) → ⊥
  cut1640  adequate = bad1640  (Adequate.valid adequate Two boolean env0)
  bad1641 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop b0 (bop b0 b0)))) b1 → ⊥
  bad1641  p = false≢true (cong lower p)
  cut1641 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (var 1) (op (var 1) (op (var 1) (var 0))))) , (var 2)) → ⊥
  cut1641  adequate = bad1641  (Adequate.valid adequate Two boolean env1)
  bad1642 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b1 (bop b1 (bop b1 b1)))) b0 → ⊥
  bad1642  p = false≢true (sym (cong lower p))
  cut1642 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (var 1) (op (var 1) (op (var 1) (var 1))))) , (var 0)) → ⊥
  cut1642  adequate = bad1642  (Adequate.valid adequate Two boolean env0)
  bad1643 : PathP (λ _ → Two) (bop (bop b1 b1) (bop b0 (bop b0 (bop b0 b0)))) b0 → ⊥
  bad1643  p = false≢true (sym (cong lower p))
  cut1643 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (var 1) (op (var 1) (op (var 1) (var 1))))) , (var 1)) → ⊥
  cut1643  adequate = bad1643  (Adequate.valid adequate Two boolean env7)
  bad1644 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop b0 (bop b0 b0)))) b1 → ⊥
  bad1644  p = false≢true (cong lower p)
  cut1644 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (var 1) (op (var 1) (op (var 1) (var 1))))) , (var 2)) → ⊥
  cut1644  adequate = bad1644  (Adequate.valid adequate Two boolean env1)
  env10 : ℕ → Two
  env10 zero = b0
  env10 (suc zero) = b1
  env10 (suc (suc zero)) = b1
  env10 (suc (suc (suc rest))) = b0
  bad1645 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b1 (bop b1 (bop b1 b1)))) b0 → ⊥
  bad1645  p = false≢true (sym (cong lower p))
  cut1645 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (var 1) (op (var 1) (op (var 1) (var 2))))) , (var 0)) → ⊥
  cut1645  adequate = bad1645  (Adequate.valid adequate Two boolean env10)
  bad1646 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b1 (bop b1 (bop b1 b0)))) b1 → ⊥
  bad1646  p = false≢true (cong lower p)
  cut1646 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (var 1) (op (var 1) (op (var 1) (var 2))))) , (var 1)) → ⊥
  cut1646  adequate = bad1646  (Adequate.valid adequate Two boolean env2)
  bad1647 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop b0 (bop b0 b1)))) b1 → ⊥
  bad1647  p = false≢true (cong lower p)
  cut1647 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (var 1) (op (var 1) (op (var 1) (var 2))))) , (var 2)) → ⊥
  cut1647  adequate = bad1647  (Adequate.valid adequate Two boolean env1)
  bad1648 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop b0 (bop b0 b0)))) b1 → ⊥
  bad1648  p = false≢true (cong lower p)
  cut1648 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (var 1) (op (var 1) (op (var 1) (var 2))))) , (var 3)) → ⊥
  cut1648  adequate = bad1648  (Adequate.valid adequate Two boolean env3)
  holds1649 : (z0 z1 z2 : A2) → (mul2 (mul2 z0 z0) (mul2 z1 (mul2 z1 (mul2 z2 z0)))) ≡ z0
  holds1649 z0 z1 z2 = refl
  cut1649 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (var 1) (op (var 1) (op (var 2) (var 0))))) , (var 0)) → ⊥
  cut1649  = reject2 ((op (op (var 0) (var 0)) (op (var 1) (op (var 1) (op (var 2) (var 0))))) , (var 0)) (λ env → holds1649 (env 0) (env 1) (env 2))
  bad1650 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b1 (bop b1 (bop b0 b0)))) b1 → ⊥
  bad1650  p = false≢true (cong lower p)
  cut1650 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (var 1) (op (var 1) (op (var 2) (var 0))))) , (var 1)) → ⊥
  cut1650  adequate = bad1650  (Adequate.valid adequate Two boolean env2)
  bad1651 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop b0 (bop b1 b0)))) b1 → ⊥
  bad1651  p = false≢true (cong lower p)
  cut1651 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (var 1) (op (var 1) (op (var 2) (var 0))))) , (var 2)) → ⊥
  cut1651  adequate = bad1651  (Adequate.valid adequate Two boolean env1)
  bad1652 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop b0 (bop b0 b0)))) b1 → ⊥
  bad1652  p = false≢true (cong lower p)
  cut1652 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (var 1) (op (var 1) (op (var 2) (var 0))))) , (var 3)) → ⊥
  cut1652  adequate = bad1652  (Adequate.valid adequate Two boolean env3)
  bad1653 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b1 (bop b1 (bop b1 b1)))) b0 → ⊥
  bad1653  p = false≢true (sym (cong lower p))
  cut1653 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (var 1) (op (var 1) (op (var 2) (var 1))))) , (var 0)) → ⊥
  cut1653  adequate = bad1653  (Adequate.valid adequate Two boolean env10)
  bad1654 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b1 (bop b1 (bop b0 b1)))) b1 → ⊥
  bad1654  p = false≢true (cong lower p)
  cut1654 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (var 1) (op (var 1) (op (var 2) (var 1))))) , (var 1)) → ⊥
  cut1654  adequate = bad1654  (Adequate.valid adequate Two boolean env2)
  bad1655 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop b0 (bop b1 b0)))) b1 → ⊥
  bad1655  p = false≢true (cong lower p)
  cut1655 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (var 1) (op (var 1) (op (var 2) (var 1))))) , (var 2)) → ⊥
  cut1655  adequate = bad1655  (Adequate.valid adequate Two boolean env1)
  bad1656 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop b0 (bop b0 b0)))) b1 → ⊥
  bad1656  p = false≢true (cong lower p)
  cut1656 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (var 1) (op (var 1) (op (var 2) (var 1))))) , (var 3)) → ⊥
  cut1656  adequate = bad1656  (Adequate.valid adequate Two boolean env3)
  bad1657 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b1 (bop b1 (bop b1 b1)))) b0 → ⊥
  bad1657  p = false≢true (sym (cong lower p))
  cut1657 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (var 1) (op (var 1) (op (var 2) (var 2))))) , (var 0)) → ⊥
  cut1657  adequate = bad1657  (Adequate.valid adequate Two boolean env10)
  bad1658 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b1 (bop b1 (bop b0 b0)))) b1 → ⊥
  bad1658  p = false≢true (cong lower p)
  cut1658 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (var 1) (op (var 1) (op (var 2) (var 2))))) , (var 1)) → ⊥
  cut1658  adequate = bad1658  (Adequate.valid adequate Two boolean env2)
  bad1659 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop b0 (bop b1 b1)))) b1 → ⊥
  bad1659  p = false≢true (cong lower p)
  cut1659 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (var 1) (op (var 1) (op (var 2) (var 2))))) , (var 2)) → ⊥
  cut1659  adequate = bad1659  (Adequate.valid adequate Two boolean env1)
  bad1660 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop b0 (bop b0 b0)))) b1 → ⊥
  bad1660  p = false≢true (cong lower p)
  cut1660 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (var 1) (op (var 1) (op (var 2) (var 2))))) , (var 3)) → ⊥
  cut1660  adequate = bad1660  (Adequate.valid adequate Two boolean env3)
  env11 : ℕ → Two
  env11 zero = b0
  env11 (suc zero) = b1
  env11 (suc (suc zero)) = b1
  env11 (suc (suc (suc zero))) = b1
  env11 (suc (suc (suc (suc rest)))) = b0
  bad1661 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b1 (bop b1 (bop b1 b1)))) b0 → ⊥
  bad1661  p = false≢true (sym (cong lower p))
  cut1661 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (var 1) (op (var 1) (op (var 2) (var 3))))) , (var 0)) → ⊥
  cut1661  adequate = bad1661  (Adequate.valid adequate Two boolean env11)
  bad1662 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b1 (bop b1 (bop b0 b0)))) b1 → ⊥
  bad1662  p = false≢true (cong lower p)
  cut1662 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (var 1) (op (var 1) (op (var 2) (var 3))))) , (var 1)) → ⊥
  cut1662  adequate = bad1662  (Adequate.valid adequate Two boolean env4)
  bad1663 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop b0 (bop b1 b0)))) b1 → ⊥
  bad1663  p = false≢true (cong lower p)
  cut1663 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (var 1) (op (var 1) (op (var 2) (var 3))))) , (var 2)) → ⊥
  cut1663  adequate = bad1663  (Adequate.valid adequate Two boolean env5)
  bad1664 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop b0 (bop b0 b1)))) b1 → ⊥
  bad1664  p = false≢true (cong lower p)
  cut1664 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (var 1) (op (var 1) (op (var 2) (var 3))))) , (var 3)) → ⊥
  cut1664  adequate = bad1664  (Adequate.valid adequate Two boolean env3)
  bad1665 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop b0 (bop b0 b0)))) b1 → ⊥
  bad1665  p = false≢true (cong lower p)
  cut1665 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (var 1) (op (var 1) (op (var 2) (var 3))))) , (var 4)) → ⊥
  cut1665  adequate = bad1665  (Adequate.valid adequate Two boolean env6)
  bad1666 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b1 (bop b0 (bop b0 b0)))) b0 → ⊥
  bad1666  p = false≢true (sym (cong lower p))
  cut1666 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (var 1) (op (var 2) (op (var 0) (var 0))))) , (var 0)) → ⊥
  cut1666  adequate = bad1666  (Adequate.valid adequate Two boolean env2)
  bad1667 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b1 (bop b1 (bop b0 b0)))) b1 → ⊥
  bad1667  p = false≢true (cong lower p)
  cut1667 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (var 1) (op (var 2) (op (var 0) (var 0))))) , (var 1)) → ⊥
  cut1667  adequate = bad1667  (Adequate.valid adequate Two boolean env10)
  bad1668 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop b1 (bop b0 b0)))) b1 → ⊥
  bad1668  p = false≢true (cong lower p)
  cut1668 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (var 1) (op (var 2) (op (var 0) (var 0))))) , (var 2)) → ⊥
  cut1668  adequate = bad1668  (Adequate.valid adequate Two boolean env1)
  bad1669 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop b0 (bop b0 b0)))) b1 → ⊥
  bad1669  p = false≢true (cong lower p)
  cut1669 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (var 1) (op (var 2) (op (var 0) (var 0))))) , (var 3)) → ⊥
  cut1669  adequate = bad1669  (Adequate.valid adequate Two boolean env3)
  bad1670 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b1 (bop b0 (bop b0 b1)))) b0 → ⊥
  bad1670  p = false≢true (sym (cong lower p))
  cut1670 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (var 1) (op (var 2) (op (var 0) (var 1))))) , (var 0)) → ⊥
  cut1670  adequate = bad1670  (Adequate.valid adequate Two boolean env2)
  bad1671 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b1 (bop b1 (bop b0 b1)))) b1 → ⊥
  bad1671  p = false≢true (cong lower p)
  cut1671 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (var 1) (op (var 2) (op (var 0) (var 1))))) , (var 1)) → ⊥
  cut1671  adequate = bad1671  (Adequate.valid adequate Two boolean env10)
  bad1672 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop b1 (bop b0 b0)))) b1 → ⊥
  bad1672  p = false≢true (cong lower p)
  cut1672 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (var 1) (op (var 2) (op (var 0) (var 1))))) , (var 2)) → ⊥
  cut1672  adequate = bad1672  (Adequate.valid adequate Two boolean env1)
  bad1673 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop b0 (bop b0 b0)))) b1 → ⊥
  bad1673  p = false≢true (cong lower p)
  cut1673 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (var 1) (op (var 2) (op (var 0) (var 1))))) , (var 3)) → ⊥
  cut1673  adequate = bad1673  (Adequate.valid adequate Two boolean env3)
  bad1674 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b1 (bop b0 (bop b0 b0)))) b0 → ⊥
  bad1674  p = false≢true (sym (cong lower p))
  cut1674 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (var 1) (op (var 2) (op (var 0) (var 2))))) , (var 0)) → ⊥
  cut1674  adequate = bad1674  (Adequate.valid adequate Two boolean env2)
  bad1675 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b1 (bop b1 (bop b0 b1)))) b1 → ⊥
  bad1675  p = false≢true (cong lower p)
  cut1675 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (var 1) (op (var 2) (op (var 0) (var 2))))) , (var 1)) → ⊥
  cut1675  adequate = bad1675  (Adequate.valid adequate Two boolean env10)
  bad1676 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop b1 (bop b0 b1)))) b1 → ⊥
  bad1676  p = false≢true (cong lower p)
  cut1676 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (var 1) (op (var 2) (op (var 0) (var 2))))) , (var 2)) → ⊥
  cut1676  adequate = bad1676  (Adequate.valid adequate Two boolean env1)
  bad1677 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop b0 (bop b0 b0)))) b1 → ⊥
  bad1677  p = false≢true (cong lower p)
  cut1677 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (var 1) (op (var 2) (op (var 0) (var 2))))) , (var 3)) → ⊥
  cut1677  adequate = bad1677  (Adequate.valid adequate Two boolean env3)
  bad1678 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b1 (bop b0 (bop b0 b0)))) b0 → ⊥
  bad1678  p = false≢true (sym (cong lower p))
  cut1678 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (var 1) (op (var 2) (op (var 0) (var 3))))) , (var 0)) → ⊥
  cut1678  adequate = bad1678  (Adequate.valid adequate Two boolean env4)
  env12 : ℕ → Two
  env12 zero = b0
  env12 (suc zero) = b1
  env12 (suc (suc zero)) = b1
  env12 (suc (suc (suc zero))) = b0
  env12 (suc (suc (suc (suc rest)))) = b0
  bad1679 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b1 (bop b1 (bop b0 b0)))) b1 → ⊥
  bad1679  p = false≢true (cong lower p)
  cut1679 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (var 1) (op (var 2) (op (var 0) (var 3))))) , (var 1)) → ⊥
  cut1679  adequate = bad1679  (Adequate.valid adequate Two boolean env12)
  bad1680 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop b1 (bop b0 b0)))) b1 → ⊥
  bad1680  p = false≢true (cong lower p)
  cut1680 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (var 1) (op (var 2) (op (var 0) (var 3))))) , (var 2)) → ⊥
  cut1680  adequate = bad1680  (Adequate.valid adequate Two boolean env5)
  bad1681 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop b0 (bop b0 b1)))) b1 → ⊥
  bad1681  p = false≢true (cong lower p)
  cut1681 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (var 1) (op (var 2) (op (var 0) (var 3))))) , (var 3)) → ⊥
  cut1681  adequate = bad1681  (Adequate.valid adequate Two boolean env3)
  bad1682 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop b0 (bop b0 b0)))) b1 → ⊥
  bad1682  p = false≢true (cong lower p)
  cut1682 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (var 1) (op (var 2) (op (var 0) (var 3))))) , (var 4)) → ⊥
  cut1682  adequate = bad1682  (Adequate.valid adequate Two boolean env6)
  bad1683 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b1 (bop b0 (bop b1 b0)))) b0 → ⊥
  bad1683  p = false≢true (sym (cong lower p))
  cut1683 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (var 1) (op (var 2) (op (var 1) (var 0))))) , (var 0)) → ⊥
  cut1683  adequate = bad1683  (Adequate.valid adequate Two boolean env2)
  bad1684 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b1 (bop b1 (bop b1 b0)))) b1 → ⊥
  bad1684  p = false≢true (cong lower p)
  cut1684 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (var 1) (op (var 2) (op (var 1) (var 0))))) , (var 1)) → ⊥
  cut1684  adequate = bad1684  (Adequate.valid adequate Two boolean env10)
  bad1685 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop b1 (bop b0 b0)))) b1 → ⊥
  bad1685  p = false≢true (cong lower p)
  cut1685 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (var 1) (op (var 2) (op (var 1) (var 0))))) , (var 2)) → ⊥
  cut1685  adequate = bad1685  (Adequate.valid adequate Two boolean env1)
  bad1686 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop b0 (bop b0 b0)))) b1 → ⊥
  bad1686  p = false≢true (cong lower p)
  cut1686 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (var 1) (op (var 2) (op (var 1) (var 0))))) , (var 3)) → ⊥
  cut1686  adequate = bad1686  (Adequate.valid adequate Two boolean env3)
  bad1687 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b1 (bop b0 (bop b1 b1)))) b0 → ⊥
  bad1687  p = false≢true (sym (cong lower p))
  cut1687 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (var 1) (op (var 2) (op (var 1) (var 1))))) , (var 0)) → ⊥
  cut1687  adequate = bad1687  (Adequate.valid adequate Two boolean env2)
  bad1688 : PathP (λ _ → Two) (bop (bop b1 b1) (bop b0 (bop b0 (bop b0 b0)))) b0 → ⊥
  bad1688  p = false≢true (sym (cong lower p))
  cut1688 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (var 1) (op (var 2) (op (var 1) (var 1))))) , (var 1)) → ⊥
  cut1688  adequate = bad1688  (Adequate.valid adequate Two boolean env8)
  bad1689 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop b1 (bop b0 b0)))) b1 → ⊥
  bad1689  p = false≢true (cong lower p)
  cut1689 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (var 1) (op (var 2) (op (var 1) (var 1))))) , (var 2)) → ⊥
  cut1689  adequate = bad1689  (Adequate.valid adequate Two boolean env1)
  bad1690 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop b0 (bop b0 b0)))) b1 → ⊥
  bad1690  p = false≢true (cong lower p)
  cut1690 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (var 1) (op (var 2) (op (var 1) (var 1))))) , (var 3)) → ⊥
  cut1690  adequate = bad1690  (Adequate.valid adequate Two boolean env3)
  bad1691 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b1 (bop b0 (bop b1 b0)))) b0 → ⊥
  bad1691  p = false≢true (sym (cong lower p))
  cut1691 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (var 1) (op (var 2) (op (var 1) (var 2))))) , (var 0)) → ⊥
  cut1691  adequate = bad1691  (Adequate.valid adequate Two boolean env2)
  bad1692 : PathP (λ _ → Two) (bop (bop b1 b1) (bop b0 (bop b0 (bop b0 b0)))) b0 → ⊥
  bad1692  p = false≢true (sym (cong lower p))
  cut1692 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (var 1) (op (var 2) (op (var 1) (var 2))))) , (var 1)) → ⊥
  cut1692  adequate = bad1692  (Adequate.valid adequate Two boolean env8)
  bad1693 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop b1 (bop b0 b1)))) b1 → ⊥
  bad1693  p = false≢true (cong lower p)
  cut1693 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (var 1) (op (var 2) (op (var 1) (var 2))))) , (var 2)) → ⊥
  cut1693  adequate = bad1693  (Adequate.valid adequate Two boolean env1)
  bad1694 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop b0 (bop b0 b0)))) b1 → ⊥
  bad1694  p = false≢true (cong lower p)
  cut1694 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (var 1) (op (var 2) (op (var 1) (var 2))))) , (var 3)) → ⊥
  cut1694  adequate = bad1694  (Adequate.valid adequate Two boolean env3)
  bad1695 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b1 (bop b0 (bop b1 b0)))) b0 → ⊥
  bad1695  p = false≢true (sym (cong lower p))
  cut1695 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (var 1) (op (var 2) (op (var 1) (var 3))))) , (var 0)) → ⊥
  cut1695  adequate = bad1695  (Adequate.valid adequate Two boolean env4)
  bad1696 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b1 (bop b1 (bop b1 b0)))) b1 → ⊥
  bad1696  p = false≢true (cong lower p)
  cut1696 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (var 1) (op (var 2) (op (var 1) (var 3))))) , (var 1)) → ⊥
  cut1696  adequate = bad1696  (Adequate.valid adequate Two boolean env12)
  bad1697 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop b1 (bop b0 b0)))) b1 → ⊥
  bad1697  p = false≢true (cong lower p)
  cut1697 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (var 1) (op (var 2) (op (var 1) (var 3))))) , (var 2)) → ⊥
  cut1697  adequate = bad1697  (Adequate.valid adequate Two boolean env5)
  bad1698 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop b0 (bop b0 b1)))) b1 → ⊥
  bad1698  p = false≢true (cong lower p)
  cut1698 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (var 1) (op (var 2) (op (var 1) (var 3))))) , (var 3)) → ⊥
  cut1698  adequate = bad1698  (Adequate.valid adequate Two boolean env3)
  bad1699 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop b0 (bop b0 b0)))) b1 → ⊥
  bad1699  p = false≢true (cong lower p)
  cut1699 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (var 1) (op (var 2) (op (var 1) (var 3))))) , (var 4)) → ⊥
  cut1699  adequate = bad1699  (Adequate.valid adequate Two boolean env6)
  bad1700 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b1 (bop b0 (bop b0 b0)))) b0 → ⊥
  bad1700  p = false≢true (sym (cong lower p))
  cut1700 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (var 1) (op (var 2) (op (var 2) (var 0))))) , (var 0)) → ⊥
  cut1700  adequate = bad1700  (Adequate.valid adequate Two boolean env2)
  bad1701 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b1 (bop b1 (bop b1 b0)))) b1 → ⊥
  bad1701  p = false≢true (cong lower p)
  cut1701 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (var 1) (op (var 2) (op (var 2) (var 0))))) , (var 1)) → ⊥
  cut1701  adequate = bad1701  (Adequate.valid adequate Two boolean env10)
  bad1702 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop b1 (bop b1 b0)))) b1 → ⊥
  bad1702  p = false≢true (cong lower p)
  cut1702 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (var 1) (op (var 2) (op (var 2) (var 0))))) , (var 2)) → ⊥
  cut1702  adequate = bad1702  (Adequate.valid adequate Two boolean env1)
  bad1703 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop b0 (bop b0 b0)))) b1 → ⊥
  bad1703  p = false≢true (cong lower p)
  cut1703 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (var 1) (op (var 2) (op (var 2) (var 0))))) , (var 3)) → ⊥
  cut1703  adequate = bad1703  (Adequate.valid adequate Two boolean env3)
  bad1704 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b1 (bop b0 (bop b0 b1)))) b0 → ⊥
  bad1704  p = false≢true (sym (cong lower p))
  cut1704 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (var 1) (op (var 2) (op (var 2) (var 1))))) , (var 0)) → ⊥
  cut1704  adequate = bad1704  (Adequate.valid adequate Two boolean env2)
  bad1705 : PathP (λ _ → Two) (bop (bop b1 b1) (bop b0 (bop b0 (bop b0 b0)))) b0 → ⊥
  bad1705  p = false≢true (sym (cong lower p))
  cut1705 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (var 1) (op (var 2) (op (var 2) (var 1))))) , (var 1)) → ⊥
  cut1705  adequate = bad1705  (Adequate.valid adequate Two boolean env8)
  bad1706 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop b1 (bop b1 b0)))) b1 → ⊥
  bad1706  p = false≢true (cong lower p)
  cut1706 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (var 1) (op (var 2) (op (var 2) (var 1))))) , (var 2)) → ⊥
  cut1706  adequate = bad1706  (Adequate.valid adequate Two boolean env1)
  bad1707 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop b0 (bop b0 b0)))) b1 → ⊥
  bad1707  p = false≢true (cong lower p)
  cut1707 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (var 1) (op (var 2) (op (var 2) (var 1))))) , (var 3)) → ⊥
  cut1707  adequate = bad1707  (Adequate.valid adequate Two boolean env3)
  bad1708 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b1 (bop b0 (bop b0 b0)))) b0 → ⊥
  bad1708  p = false≢true (sym (cong lower p))
  cut1708 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (var 1) (op (var 2) (op (var 2) (var 2))))) , (var 0)) → ⊥
  cut1708  adequate = bad1708  (Adequate.valid adequate Two boolean env2)
  bad1709 : PathP (λ _ → Two) (bop (bop b1 b1) (bop b0 (bop b0 (bop b0 b0)))) b0 → ⊥
  bad1709  p = false≢true (sym (cong lower p))
  cut1709 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (var 1) (op (var 2) (op (var 2) (var 2))))) , (var 1)) → ⊥
  cut1709  adequate = bad1709  (Adequate.valid adequate Two boolean env8)
  bad1710 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop b1 (bop b1 b1)))) b1 → ⊥
  bad1710  p = false≢true (cong lower p)
  cut1710 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (var 1) (op (var 2) (op (var 2) (var 2))))) , (var 2)) → ⊥
  cut1710  adequate = bad1710  (Adequate.valid adequate Two boolean env1)
  bad1711 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop b0 (bop b0 b0)))) b1 → ⊥
  bad1711  p = false≢true (cong lower p)
  cut1711 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (var 1) (op (var 2) (op (var 2) (var 2))))) , (var 3)) → ⊥
  cut1711  adequate = bad1711  (Adequate.valid adequate Two boolean env3)
  bad1712 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b1 (bop b0 (bop b0 b0)))) b0 → ⊥
  bad1712  p = false≢true (sym (cong lower p))
  cut1712 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (var 1) (op (var 2) (op (var 2) (var 3))))) , (var 0)) → ⊥
  cut1712  adequate = bad1712  (Adequate.valid adequate Two boolean env4)
  bad1713 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b1 (bop b1 (bop b1 b0)))) b1 → ⊥
  bad1713  p = false≢true (cong lower p)
  cut1713 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (var 1) (op (var 2) (op (var 2) (var 3))))) , (var 1)) → ⊥
  cut1713  adequate = bad1713  (Adequate.valid adequate Two boolean env12)
  bad1714 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop b1 (bop b1 b0)))) b1 → ⊥
  bad1714  p = false≢true (cong lower p)
  cut1714 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (var 1) (op (var 2) (op (var 2) (var 3))))) , (var 2)) → ⊥
  cut1714  adequate = bad1714  (Adequate.valid adequate Two boolean env5)
  bad1715 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop b0 (bop b0 b1)))) b1 → ⊥
  bad1715  p = false≢true (cong lower p)
  cut1715 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (var 1) (op (var 2) (op (var 2) (var 3))))) , (var 3)) → ⊥
  cut1715  adequate = bad1715  (Adequate.valid adequate Two boolean env3)
  bad1716 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop b0 (bop b0 b0)))) b1 → ⊥
  bad1716  p = false≢true (cong lower p)
  cut1716 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (var 1) (op (var 2) (op (var 2) (var 3))))) , (var 4)) → ⊥
  cut1716  adequate = bad1716  (Adequate.valid adequate Two boolean env6)
  bad1717 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b1 (bop b0 (bop b0 b0)))) b0 → ⊥
  bad1717  p = false≢true (sym (cong lower p))
  cut1717 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (var 1) (op (var 2) (op (var 3) (var 0))))) , (var 0)) → ⊥
  cut1717  adequate = bad1717  (Adequate.valid adequate Two boolean env4)
  bad1718 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b1 (bop b1 (bop b0 b0)))) b1 → ⊥
  bad1718  p = false≢true (cong lower p)
  cut1718 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (var 1) (op (var 2) (op (var 3) (var 0))))) , (var 1)) → ⊥
  cut1718  adequate = bad1718  (Adequate.valid adequate Two boolean env12)
  bad1719 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop b1 (bop b0 b0)))) b1 → ⊥
  bad1719  p = false≢true (cong lower p)
  cut1719 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (var 1) (op (var 2) (op (var 3) (var 0))))) , (var 2)) → ⊥
  cut1719  adequate = bad1719  (Adequate.valid adequate Two boolean env5)
  bad1720 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop b0 (bop b1 b0)))) b1 → ⊥
  bad1720  p = false≢true (cong lower p)
  cut1720 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (var 1) (op (var 2) (op (var 3) (var 0))))) , (var 3)) → ⊥
  cut1720  adequate = bad1720  (Adequate.valid adequate Two boolean env3)
  bad1721 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop b0 (bop b0 b0)))) b1 → ⊥
  bad1721  p = false≢true (cong lower p)
  cut1721 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (var 1) (op (var 2) (op (var 3) (var 0))))) , (var 4)) → ⊥
  cut1721  adequate = bad1721  (Adequate.valid adequate Two boolean env6)
  bad1722 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b1 (bop b0 (bop b0 b1)))) b0 → ⊥
  bad1722  p = false≢true (sym (cong lower p))
  cut1722 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (var 1) (op (var 2) (op (var 3) (var 1))))) , (var 0)) → ⊥
  cut1722  adequate = bad1722  (Adequate.valid adequate Two boolean env4)
  bad1723 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b1 (bop b1 (bop b0 b1)))) b1 → ⊥
  bad1723  p = false≢true (cong lower p)
  cut1723 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (var 1) (op (var 2) (op (var 3) (var 1))))) , (var 1)) → ⊥
  cut1723  adequate = bad1723  (Adequate.valid adequate Two boolean env12)
  bad1724 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop b1 (bop b0 b0)))) b1 → ⊥
  bad1724  p = false≢true (cong lower p)
  cut1724 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (var 1) (op (var 2) (op (var 3) (var 1))))) , (var 2)) → ⊥
  cut1724  adequate = bad1724  (Adequate.valid adequate Two boolean env5)
  bad1725 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop b0 (bop b1 b0)))) b1 → ⊥
  bad1725  p = false≢true (cong lower p)
  cut1725 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (var 1) (op (var 2) (op (var 3) (var 1))))) , (var 3)) → ⊥
  cut1725  adequate = bad1725  (Adequate.valid adequate Two boolean env3)
  bad1726 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop b0 (bop b0 b0)))) b1 → ⊥
  bad1726  p = false≢true (cong lower p)
  cut1726 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (var 1) (op (var 2) (op (var 3) (var 1))))) , (var 4)) → ⊥
  cut1726  adequate = bad1726  (Adequate.valid adequate Two boolean env6)
  bad1727 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b1 (bop b0 (bop b0 b0)))) b0 → ⊥
  bad1727  p = false≢true (sym (cong lower p))
  cut1727 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (var 1) (op (var 2) (op (var 3) (var 2))))) , (var 0)) → ⊥
  cut1727  adequate = bad1727  (Adequate.valid adequate Two boolean env4)
  bad1728 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b1 (bop b1 (bop b0 b1)))) b1 → ⊥
  bad1728  p = false≢true (cong lower p)
  cut1728 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (var 1) (op (var 2) (op (var 3) (var 2))))) , (var 1)) → ⊥
  cut1728  adequate = bad1728  (Adequate.valid adequate Two boolean env12)
  bad1729 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop b1 (bop b0 b1)))) b1 → ⊥
  bad1729  p = false≢true (cong lower p)
  cut1729 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (var 1) (op (var 2) (op (var 3) (var 2))))) , (var 2)) → ⊥
  cut1729  adequate = bad1729  (Adequate.valid adequate Two boolean env5)
  bad1730 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop b0 (bop b1 b0)))) b1 → ⊥
  bad1730  p = false≢true (cong lower p)
  cut1730 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (var 1) (op (var 2) (op (var 3) (var 2))))) , (var 3)) → ⊥
  cut1730  adequate = bad1730  (Adequate.valid adequate Two boolean env3)
  bad1731 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop b0 (bop b0 b0)))) b1 → ⊥
  bad1731  p = false≢true (cong lower p)
  cut1731 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (var 1) (op (var 2) (op (var 3) (var 2))))) , (var 4)) → ⊥
  cut1731  adequate = bad1731  (Adequate.valid adequate Two boolean env6)
  bad1732 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b1 (bop b0 (bop b0 b0)))) b0 → ⊥
  bad1732  p = false≢true (sym (cong lower p))
  cut1732 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (var 1) (op (var 2) (op (var 3) (var 3))))) , (var 0)) → ⊥
  cut1732  adequate = bad1732  (Adequate.valid adequate Two boolean env4)
  bad1733 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b1 (bop b1 (bop b0 b0)))) b1 → ⊥
  bad1733  p = false≢true (cong lower p)
  cut1733 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (var 1) (op (var 2) (op (var 3) (var 3))))) , (var 1)) → ⊥
  cut1733  adequate = bad1733  (Adequate.valid adequate Two boolean env12)
  bad1734 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop b1 (bop b0 b0)))) b1 → ⊥
  bad1734  p = false≢true (cong lower p)
  cut1734 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (var 1) (op (var 2) (op (var 3) (var 3))))) , (var 2)) → ⊥
  cut1734  adequate = bad1734  (Adequate.valid adequate Two boolean env5)
  bad1735 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop b0 (bop b1 b1)))) b1 → ⊥
  bad1735  p = false≢true (cong lower p)
  cut1735 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (var 1) (op (var 2) (op (var 3) (var 3))))) , (var 3)) → ⊥
  cut1735  adequate = bad1735  (Adequate.valid adequate Two boolean env3)
  bad1736 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop b0 (bop b0 b0)))) b1 → ⊥
  bad1736  p = false≢true (cong lower p)
  cut1736 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (var 1) (op (var 2) (op (var 3) (var 3))))) , (var 4)) → ⊥
  cut1736  adequate = bad1736  (Adequate.valid adequate Two boolean env6)
  env13 : ℕ → Two
  env13 zero = b0
  env13 (suc zero) = b1
  env13 (suc (suc zero)) = b0
  env13 (suc (suc (suc zero))) = b0
  env13 (suc (suc (suc (suc zero)))) = b0
  env13 (suc (suc (suc (suc (suc rest))))) = b0
  bad1737 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b1 (bop b0 (bop b0 b0)))) b0 → ⊥
  bad1737  p = false≢true (sym (cong lower p))
  cut1737 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (var 1) (op (var 2) (op (var 3) (var 4))))) , (var 0)) → ⊥
  cut1737  adequate = bad1737  (Adequate.valid adequate Two boolean env13)
  env14 : ℕ → Two
  env14 zero = b0
  env14 (suc zero) = b1
  env14 (suc (suc zero)) = b1
  env14 (suc (suc (suc zero))) = b0
  env14 (suc (suc (suc (suc zero)))) = b0
  env14 (suc (suc (suc (suc (suc rest))))) = b0
  bad1738 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b1 (bop b1 (bop b0 b0)))) b1 → ⊥
  bad1738  p = false≢true (cong lower p)
  cut1738 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (var 1) (op (var 2) (op (var 3) (var 4))))) , (var 1)) → ⊥
  cut1738  adequate = bad1738  (Adequate.valid adequate Two boolean env14)
  env15 : ℕ → Two
  env15 zero = b0
  env15 (suc zero) = b0
  env15 (suc (suc zero)) = b1
  env15 (suc (suc (suc zero))) = b0
  env15 (suc (suc (suc (suc zero)))) = b0
  env15 (suc (suc (suc (suc (suc rest))))) = b0
  bad1739 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop b1 (bop b0 b0)))) b1 → ⊥
  bad1739  p = false≢true (cong lower p)
  cut1739 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (var 1) (op (var 2) (op (var 3) (var 4))))) , (var 2)) → ⊥
  cut1739  adequate = bad1739  (Adequate.valid adequate Two boolean env15)
  env16 : ℕ → Two
  env16 zero = b0
  env16 (suc zero) = b0
  env16 (suc (suc zero)) = b0
  env16 (suc (suc (suc zero))) = b1
  env16 (suc (suc (suc (suc zero)))) = b0
  env16 (suc (suc (suc (suc (suc rest))))) = b0
  bad1740 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop b0 (bop b1 b0)))) b1 → ⊥
  bad1740  p = false≢true (cong lower p)
  cut1740 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (var 1) (op (var 2) (op (var 3) (var 4))))) , (var 3)) → ⊥
  cut1740  adequate = bad1740  (Adequate.valid adequate Two boolean env16)
  bad1741 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop b0 (bop b0 b1)))) b1 → ⊥
  bad1741  p = false≢true (cong lower p)
  cut1741 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (var 1) (op (var 2) (op (var 3) (var 4))))) , (var 4)) → ⊥
  cut1741  adequate = bad1741  (Adequate.valid adequate Two boolean env6)
  env17 : ℕ → Two
  env17 zero = b0
  env17 (suc zero) = b0
  env17 (suc (suc zero)) = b0
  env17 (suc (suc (suc zero))) = b0
  env17 (suc (suc (suc (suc zero)))) = b0
  env17 (suc (suc (suc (suc (suc zero))))) = b1
  env17 (suc (suc (suc (suc (suc (suc rest)))))) = b0
  bad1742 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop b0 (bop b0 b0)))) b1 → ⊥
  bad1742  p = false≢true (cong lower p)
  cut1742 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (var 1) (op (var 2) (op (var 3) (var 4))))) , (var 5)) → ⊥
  cut1742  adequate = bad1742  (Adequate.valid adequate Two boolean env17)
  holds1743 : (z0 z1 : A2) → (mul2 (mul2 z0 z1) (mul2 z0 (mul2 z0 (mul2 z0 z0)))) ≡ z0
  holds1743 z0 z1 = refl
  cut1743 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 0) (op (var 0) (op (var 0) (var 0))))) , (var 0)) → ⊥
  cut1743  = reject2 ((op (op (var 0) (var 1)) (op (var 0) (op (var 0) (op (var 0) (var 0))))) , (var 0)) (λ env → holds1743 (env 0) (env 1))
  bad1744 : PathP (λ _ → Two) (bop (bop b0 b1) (bop b0 (bop b0 (bop b0 b0)))) b1 → ⊥
  bad1744  p = false≢true (cong lower p)
  cut1744 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 0) (op (var 0) (op (var 0) (var 0))))) , (var 1)) → ⊥
  cut1744  adequate = bad1744  (Adequate.valid adequate Two boolean env0)
  bad1745 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop b0 (bop b0 b0)))) b1 → ⊥
  bad1745  p = false≢true (cong lower p)
  cut1745 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 0) (op (var 0) (op (var 0) (var 0))))) , (var 2)) → ⊥
  cut1745  adequate = bad1745  (Adequate.valid adequate Two boolean env1)
  bad1746 : PathP (λ _ → Two) (bop (bop b1 b0) (bop b1 (bop b1 (bop b1 b0)))) b1 → ⊥
  bad1746  p = false≢true (cong lower p)
  cut1746 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 0) (op (var 0) (op (var 0) (var 1))))) , (var 0)) → ⊥
  cut1746  adequate = bad1746  (Adequate.valid adequate Two boolean env7)
  bad1747 : PathP (λ _ → Two) (bop (bop b0 b1) (bop b0 (bop b0 (bop b0 b1)))) b1 → ⊥
  bad1747  p = false≢true (cong lower p)
  cut1747 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 0) (op (var 0) (op (var 0) (var 1))))) , (var 1)) → ⊥
  cut1747  adequate = bad1747  (Adequate.valid adequate Two boolean env0)
  bad1748 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop b0 (bop b0 b0)))) b1 → ⊥
  bad1748  p = false≢true (cong lower p)
  cut1748 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 0) (op (var 0) (op (var 0) (var 1))))) , (var 2)) → ⊥
  cut1748  adequate = bad1748  (Adequate.valid adequate Two boolean env1)
  bad1749 : PathP (λ _ → Two) (bop (bop b1 b0) (bop b1 (bop b1 (bop b1 b0)))) b1 → ⊥
  bad1749  p = false≢true (cong lower p)
  cut1749 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 0) (op (var 0) (op (var 0) (var 2))))) , (var 0)) → ⊥
  cut1749  adequate = bad1749  (Adequate.valid adequate Two boolean env8)
  bad1750 : PathP (λ _ → Two) (bop (bop b0 b1) (bop b0 (bop b0 (bop b0 b0)))) b1 → ⊥
  bad1750  p = false≢true (cong lower p)
  cut1750 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 0) (op (var 0) (op (var 0) (var 2))))) , (var 1)) → ⊥
  cut1750  adequate = bad1750  (Adequate.valid adequate Two boolean env2)
  bad1751 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop b0 (bop b0 b1)))) b1 → ⊥
  bad1751  p = false≢true (cong lower p)
  cut1751 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 0) (op (var 0) (op (var 0) (var 2))))) , (var 2)) → ⊥
  cut1751  adequate = bad1751  (Adequate.valid adequate Two boolean env1)
  bad1752 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop b0 (bop b0 b0)))) b1 → ⊥
  bad1752  p = false≢true (cong lower p)
  cut1752 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 0) (op (var 0) (op (var 0) (var 2))))) , (var 3)) → ⊥
  cut1752  adequate = bad1752  (Adequate.valid adequate Two boolean env3)
  bad1753 : PathP (λ _ → Two) (bop (bop b1 b0) (bop b1 (bop b1 (bop b0 b1)))) b1 → ⊥
  bad1753  p = false≢true (cong lower p)
  cut1753 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 0) (op (var 0) (op (var 1) (var 0))))) , (var 0)) → ⊥
  cut1753  adequate = bad1753  (Adequate.valid adequate Two boolean env7)
  bad1754 : PathP (λ _ → Two) (bop (bop b0 b1) (bop b0 (bop b0 (bop b1 b0)))) b1 → ⊥
  bad1754  p = false≢true (cong lower p)
  cut1754 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 0) (op (var 0) (op (var 1) (var 0))))) , (var 1)) → ⊥
  cut1754  adequate = bad1754  (Adequate.valid adequate Two boolean env0)
  bad1755 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop b0 (bop b0 b0)))) b1 → ⊥
  bad1755  p = false≢true (cong lower p)
  cut1755 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 0) (op (var 0) (op (var 1) (var 0))))) , (var 2)) → ⊥
  cut1755  adequate = bad1755  (Adequate.valid adequate Two boolean env1)
  bad1756 : PathP (λ _ → Two) (bop (bop b1 b0) (bop b1 (bop b1 (bop b0 b0)))) b1 → ⊥
  bad1756  p = false≢true (cong lower p)
  cut1756 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 0) (op (var 0) (op (var 1) (var 1))))) , (var 0)) → ⊥
  cut1756  adequate = bad1756  (Adequate.valid adequate Two boolean env7)
  bad1757 : PathP (λ _ → Two) (bop (bop b0 b1) (bop b0 (bop b0 (bop b1 b1)))) b1 → ⊥
  bad1757  p = false≢true (cong lower p)
  cut1757 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 0) (op (var 0) (op (var 1) (var 1))))) , (var 1)) → ⊥
  cut1757  adequate = bad1757  (Adequate.valid adequate Two boolean env0)
  bad1758 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop b0 (bop b0 b0)))) b1 → ⊥
  bad1758  p = false≢true (cong lower p)
  cut1758 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 0) (op (var 0) (op (var 1) (var 1))))) , (var 2)) → ⊥
  cut1758  adequate = bad1758  (Adequate.valid adequate Two boolean env1)
  bad1759 : PathP (λ _ → Two) (bop (bop b1 b0) (bop b1 (bop b1 (bop b0 b0)))) b1 → ⊥
  bad1759  p = false≢true (cong lower p)
  cut1759 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 0) (op (var 0) (op (var 1) (var 2))))) , (var 0)) → ⊥
  cut1759  adequate = bad1759  (Adequate.valid adequate Two boolean env8)
  bad1760 : PathP (λ _ → Two) (bop (bop b0 b1) (bop b0 (bop b0 (bop b1 b0)))) b1 → ⊥
  bad1760  p = false≢true (cong lower p)
  cut1760 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 0) (op (var 0) (op (var 1) (var 2))))) , (var 1)) → ⊥
  cut1760  adequate = bad1760  (Adequate.valid adequate Two boolean env2)
  bad1761 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop b0 (bop b0 b1)))) b1 → ⊥
  bad1761  p = false≢true (cong lower p)
  cut1761 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 0) (op (var 0) (op (var 1) (var 2))))) , (var 2)) → ⊥
  cut1761  adequate = bad1761  (Adequate.valid adequate Two boolean env1)
  bad1762 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop b0 (bop b0 b0)))) b1 → ⊥
  bad1762  p = false≢true (cong lower p)
  cut1762 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 0) (op (var 0) (op (var 1) (var 2))))) , (var 3)) → ⊥
  cut1762  adequate = bad1762  (Adequate.valid adequate Two boolean env3)
  bad1763 : PathP (λ _ → Two) (bop (bop b1 b0) (bop b1 (bop b1 (bop b0 b1)))) b1 → ⊥
  bad1763  p = false≢true (cong lower p)
  cut1763 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 0) (op (var 0) (op (var 2) (var 0))))) , (var 0)) → ⊥
  cut1763  adequate = bad1763  (Adequate.valid adequate Two boolean env8)
  bad1764 : PathP (λ _ → Two) (bop (bop b0 b1) (bop b0 (bop b0 (bop b0 b0)))) b1 → ⊥
  bad1764  p = false≢true (cong lower p)
  cut1764 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 0) (op (var 0) (op (var 2) (var 0))))) , (var 1)) → ⊥
  cut1764  adequate = bad1764  (Adequate.valid adequate Two boolean env2)
  bad1765 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop b0 (bop b1 b0)))) b1 → ⊥
  bad1765  p = false≢true (cong lower p)
  cut1765 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 0) (op (var 0) (op (var 2) (var 0))))) , (var 2)) → ⊥
  cut1765  adequate = bad1765  (Adequate.valid adequate Two boolean env1)
  bad1766 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop b0 (bop b0 b0)))) b1 → ⊥
  bad1766  p = false≢true (cong lower p)
  cut1766 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 0) (op (var 0) (op (var 2) (var 0))))) , (var 3)) → ⊥
  cut1766  adequate = bad1766  (Adequate.valid adequate Two boolean env3)
  bad1767 : PathP (λ _ → Two) (bop (bop b1 b0) (bop b1 (bop b1 (bop b0 b0)))) b1 → ⊥
  bad1767  p = false≢true (cong lower p)
  cut1767 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 0) (op (var 0) (op (var 2) (var 1))))) , (var 0)) → ⊥
  cut1767  adequate = bad1767  (Adequate.valid adequate Two boolean env8)
  bad1768 : PathP (λ _ → Two) (bop (bop b0 b1) (bop b0 (bop b0 (bop b0 b1)))) b1 → ⊥
  bad1768  p = false≢true (cong lower p)
  cut1768 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 0) (op (var 0) (op (var 2) (var 1))))) , (var 1)) → ⊥
  cut1768  adequate = bad1768  (Adequate.valid adequate Two boolean env2)
  bad1769 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop b0 (bop b1 b0)))) b1 → ⊥
  bad1769  p = false≢true (cong lower p)
  cut1769 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 0) (op (var 0) (op (var 2) (var 1))))) , (var 2)) → ⊥
  cut1769  adequate = bad1769  (Adequate.valid adequate Two boolean env1)
  bad1770 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop b0 (bop b0 b0)))) b1 → ⊥
  bad1770  p = false≢true (cong lower p)
  cut1770 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 0) (op (var 0) (op (var 2) (var 1))))) , (var 3)) → ⊥
  cut1770  adequate = bad1770  (Adequate.valid adequate Two boolean env3)
  bad1771 : PathP (λ _ → Two) (bop (bop b1 b0) (bop b1 (bop b1 (bop b0 b0)))) b1 → ⊥
  bad1771  p = false≢true (cong lower p)
  cut1771 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 0) (op (var 0) (op (var 2) (var 2))))) , (var 0)) → ⊥
  cut1771  adequate = bad1771  (Adequate.valid adequate Two boolean env8)
  bad1772 : PathP (λ _ → Two) (bop (bop b0 b1) (bop b0 (bop b0 (bop b0 b0)))) b1 → ⊥
  bad1772  p = false≢true (cong lower p)
  cut1772 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 0) (op (var 0) (op (var 2) (var 2))))) , (var 1)) → ⊥
  cut1772  adequate = bad1772  (Adequate.valid adequate Two boolean env2)
  bad1773 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop b0 (bop b1 b1)))) b1 → ⊥
  bad1773  p = false≢true (cong lower p)
  cut1773 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 0) (op (var 0) (op (var 2) (var 2))))) , (var 2)) → ⊥
  cut1773  adequate = bad1773  (Adequate.valid adequate Two boolean env1)
  bad1774 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop b0 (bop b0 b0)))) b1 → ⊥
  bad1774  p = false≢true (cong lower p)
  cut1774 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 0) (op (var 0) (op (var 2) (var 2))))) , (var 3)) → ⊥
  cut1774  adequate = bad1774  (Adequate.valid adequate Two boolean env3)
  bad1775 : PathP (λ _ → Two) (bop (bop b1 b0) (bop b1 (bop b1 (bop b0 b0)))) b1 → ⊥
  bad1775  p = false≢true (cong lower p)
  cut1775 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 0) (op (var 0) (op (var 2) (var 3))))) , (var 0)) → ⊥
  cut1775  adequate = bad1775  (Adequate.valid adequate Two boolean env9)
  bad1776 : PathP (λ _ → Two) (bop (bop b0 b1) (bop b0 (bop b0 (bop b0 b0)))) b1 → ⊥
  bad1776  p = false≢true (cong lower p)
  cut1776 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 0) (op (var 0) (op (var 2) (var 3))))) , (var 1)) → ⊥
  cut1776  adequate = bad1776  (Adequate.valid adequate Two boolean env4)
  bad1777 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop b0 (bop b1 b0)))) b1 → ⊥
  bad1777  p = false≢true (cong lower p)
  cut1777 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 0) (op (var 0) (op (var 2) (var 3))))) , (var 2)) → ⊥
  cut1777  adequate = bad1777  (Adequate.valid adequate Two boolean env5)
  bad1778 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop b0 (bop b0 b1)))) b1 → ⊥
  bad1778  p = false≢true (cong lower p)
  cut1778 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 0) (op (var 0) (op (var 2) (var 3))))) , (var 3)) → ⊥
  cut1778  adequate = bad1778  (Adequate.valid adequate Two boolean env3)
  bad1779 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop b0 (bop b0 b0)))) b1 → ⊥
  bad1779  p = false≢true (cong lower p)
  cut1779 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 0) (op (var 0) (op (var 2) (var 3))))) , (var 4)) → ⊥
  cut1779  adequate = bad1779  (Adequate.valid adequate Two boolean env6)
  holds1780 : (z0 z1 : A2) → (mul2 (mul2 z0 z1) (mul2 z0 (mul2 z1 (mul2 z0 z0)))) ≡ z0
  holds1780 z0 z1 = refl
  cut1780 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 0) (op (var 1) (op (var 0) (var 0))))) , (var 0)) → ⊥
  cut1780  = reject2 ((op (op (var 0) (var 1)) (op (var 0) (op (var 1) (op (var 0) (var 0))))) , (var 0)) (λ env → holds1780 (env 0) (env 1))
  bad1781 : PathP (λ _ → Two) (bop (bop b0 b1) (bop b0 (bop b1 (bop b0 b0)))) b1 → ⊥
  bad1781  p = false≢true (cong lower p)
  cut1781 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 0) (op (var 1) (op (var 0) (var 0))))) , (var 1)) → ⊥
  cut1781  adequate = bad1781  (Adequate.valid adequate Two boolean env0)
  bad1782 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop b0 (bop b0 b0)))) b1 → ⊥
  bad1782  p = false≢true (cong lower p)
  cut1782 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 0) (op (var 1) (op (var 0) (var 0))))) , (var 2)) → ⊥
  cut1782  adequate = bad1782  (Adequate.valid adequate Two boolean env1)
  holds1783 : (z0 z1 : A2) → (mul2 (mul2 z0 z1) (mul2 z0 (mul2 z1 (mul2 z0 z1)))) ≡ z0
  holds1783 z0 z1 = refl
  cut1783 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 0) (op (var 1) (op (var 0) (var 1))))) , (var 0)) → ⊥
  cut1783  = reject2 ((op (op (var 0) (var 1)) (op (var 0) (op (var 1) (op (var 0) (var 1))))) , (var 0)) (λ env → holds1783 (env 0) (env 1))
  bad1784 : PathP (λ _ → Two) (bop (bop b0 b1) (bop b0 (bop b1 (bop b0 b1)))) b1 → ⊥
  bad1784  p = false≢true (cong lower p)
  cut1784 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 0) (op (var 1) (op (var 0) (var 1))))) , (var 1)) → ⊥
  cut1784  adequate = bad1784  (Adequate.valid adequate Two boolean env0)
  bad1785 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop b0 (bop b0 b0)))) b1 → ⊥
  bad1785  p = false≢true (cong lower p)
  cut1785 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 0) (op (var 1) (op (var 0) (var 1))))) , (var 2)) → ⊥
  cut1785  adequate = bad1785  (Adequate.valid adequate Two boolean env1)
  holds1786 : (z0 z1 z2 : A2) → (mul2 (mul2 z0 z1) (mul2 z0 (mul2 z1 (mul2 z0 z2)))) ≡ z0
  holds1786 z0 z1 z2 = refl
  cut1786 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 0) (op (var 1) (op (var 0) (var 2))))) , (var 0)) → ⊥
  cut1786  = reject2 ((op (op (var 0) (var 1)) (op (var 0) (op (var 1) (op (var 0) (var 2))))) , (var 0)) (λ env → holds1786 (env 0) (env 1) (env 2))
  bad1787 : PathP (λ _ → Two) (bop (bop b0 b1) (bop b0 (bop b1 (bop b0 b0)))) b1 → ⊥
  bad1787  p = false≢true (cong lower p)
  cut1787 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 0) (op (var 1) (op (var 0) (var 2))))) , (var 1)) → ⊥
  cut1787  adequate = bad1787  (Adequate.valid adequate Two boolean env2)
  bad1788 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop b0 (bop b0 b1)))) b1 → ⊥
  bad1788  p = false≢true (cong lower p)
  cut1788 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 0) (op (var 1) (op (var 0) (var 2))))) , (var 2)) → ⊥
  cut1788  adequate = bad1788  (Adequate.valid adequate Two boolean env1)
  bad1789 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop b0 (bop b0 b0)))) b1 → ⊥
  bad1789  p = false≢true (cong lower p)
  cut1789 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 0) (op (var 1) (op (var 0) (var 2))))) , (var 3)) → ⊥
  cut1789  adequate = bad1789  (Adequate.valid adequate Two boolean env3)
  holds1790 : (z0 z1 : A2) → (mul2 (mul2 z0 z1) (mul2 z0 (mul2 z1 (mul2 z1 z0)))) ≡ z0
  holds1790 z0 z1 = refl
  cut1790 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 0) (op (var 1) (op (var 1) (var 0))))) , (var 0)) → ⊥
  cut1790  = reject2 ((op (op (var 0) (var 1)) (op (var 0) (op (var 1) (op (var 1) (var 0))))) , (var 0)) (λ env → holds1790 (env 0) (env 1))
  bad1791 : PathP (λ _ → Two) (bop (bop b0 b1) (bop b0 (bop b1 (bop b1 b0)))) b1 → ⊥
  bad1791  p = false≢true (cong lower p)
  cut1791 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 0) (op (var 1) (op (var 1) (var 0))))) , (var 1)) → ⊥
  cut1791  adequate = bad1791  (Adequate.valid adequate Two boolean env0)
  bad1792 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop b0 (bop b0 b0)))) b1 → ⊥
  bad1792  p = false≢true (cong lower p)
  cut1792 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 0) (op (var 1) (op (var 1) (var 0))))) , (var 2)) → ⊥
  cut1792  adequate = bad1792  (Adequate.valid adequate Two boolean env1)
  holds1793 : (z0 z1 : A2) → (mul2 (mul2 z0 z1) (mul2 z0 (mul2 z1 (mul2 z1 z1)))) ≡ z0
  holds1793 z0 z1 = refl
  cut1793 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 0) (op (var 1) (op (var 1) (var 1))))) , (var 0)) → ⊥
  cut1793  = reject2 ((op (op (var 0) (var 1)) (op (var 0) (op (var 1) (op (var 1) (var 1))))) , (var 0)) (λ env → holds1793 (env 0) (env 1))
  bad1794 : PathP (λ _ → Two) (bop (bop b0 b1) (bop b0 (bop b1 (bop b1 b1)))) b1 → ⊥
  bad1794  p = false≢true (cong lower p)
  cut1794 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 0) (op (var 1) (op (var 1) (var 1))))) , (var 1)) → ⊥
  cut1794  adequate = bad1794  (Adequate.valid adequate Two boolean env0)
  bad1795 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop b0 (bop b0 b0)))) b1 → ⊥
  bad1795  p = false≢true (cong lower p)
  cut1795 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 0) (op (var 1) (op (var 1) (var 1))))) , (var 2)) → ⊥
  cut1795  adequate = bad1795  (Adequate.valid adequate Two boolean env1)
  holds1796 : (z0 z1 z2 : A2) → (mul2 (mul2 z0 z1) (mul2 z0 (mul2 z1 (mul2 z1 z2)))) ≡ z0
  holds1796 z0 z1 z2 = refl
  cut1796 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 0) (op (var 1) (op (var 1) (var 2))))) , (var 0)) → ⊥
  cut1796  = reject2 ((op (op (var 0) (var 1)) (op (var 0) (op (var 1) (op (var 1) (var 2))))) , (var 0)) (λ env → holds1796 (env 0) (env 1) (env 2))
  bad1797 : PathP (λ _ → Two) (bop (bop b0 b1) (bop b0 (bop b1 (bop b1 b0)))) b1 → ⊥
  bad1797  p = false≢true (cong lower p)
  cut1797 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 0) (op (var 1) (op (var 1) (var 2))))) , (var 1)) → ⊥
  cut1797  adequate = bad1797  (Adequate.valid adequate Two boolean env2)
  bad1798 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop b0 (bop b0 b1)))) b1 → ⊥
  bad1798  p = false≢true (cong lower p)
  cut1798 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 0) (op (var 1) (op (var 1) (var 2))))) , (var 2)) → ⊥
  cut1798  adequate = bad1798  (Adequate.valid adequate Two boolean env1)
  bad1799 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop b0 (bop b0 b0)))) b1 → ⊥
  bad1799  p = false≢true (cong lower p)
  cut1799 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 0) (op (var 1) (op (var 1) (var 2))))) , (var 3)) → ⊥
  cut1799  adequate = bad1799  (Adequate.valid adequate Two boolean env3)
  holds1800 : (z0 z1 z2 : A2) → (mul2 (mul2 z0 z1) (mul2 z0 (mul2 z1 (mul2 z2 z0)))) ≡ z0
  holds1800 z0 z1 z2 = refl
  cut1800 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 0) (op (var 1) (op (var 2) (var 0))))) , (var 0)) → ⊥
  cut1800  = reject2 ((op (op (var 0) (var 1)) (op (var 0) (op (var 1) (op (var 2) (var 0))))) , (var 0)) (λ env → holds1800 (env 0) (env 1) (env 2))
  bad1801 : PathP (λ _ → Two) (bop (bop b0 b1) (bop b0 (bop b1 (bop b0 b0)))) b1 → ⊥
  bad1801  p = false≢true (cong lower p)
  cut1801 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 0) (op (var 1) (op (var 2) (var 0))))) , (var 1)) → ⊥
  cut1801  adequate = bad1801  (Adequate.valid adequate Two boolean env2)
  bad1802 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop b0 (bop b1 b0)))) b1 → ⊥
  bad1802  p = false≢true (cong lower p)
  cut1802 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 0) (op (var 1) (op (var 2) (var 0))))) , (var 2)) → ⊥
  cut1802  adequate = bad1802  (Adequate.valid adequate Two boolean env1)
  bad1803 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop b0 (bop b0 b0)))) b1 → ⊥
  bad1803  p = false≢true (cong lower p)
  cut1803 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 0) (op (var 1) (op (var 2) (var 0))))) , (var 3)) → ⊥
  cut1803  adequate = bad1803  (Adequate.valid adequate Two boolean env3)
  holds1804 : (z0 z1 z2 : A2) → (mul2 (mul2 z0 z1) (mul2 z0 (mul2 z1 (mul2 z2 z1)))) ≡ z0
  holds1804 z0 z1 z2 = refl
  cut1804 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 0) (op (var 1) (op (var 2) (var 1))))) , (var 0)) → ⊥
  cut1804  = reject2 ((op (op (var 0) (var 1)) (op (var 0) (op (var 1) (op (var 2) (var 1))))) , (var 0)) (λ env → holds1804 (env 0) (env 1) (env 2))
  bad1805 : PathP (λ _ → Two) (bop (bop b0 b1) (bop b0 (bop b1 (bop b0 b1)))) b1 → ⊥
  bad1805  p = false≢true (cong lower p)
  cut1805 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 0) (op (var 1) (op (var 2) (var 1))))) , (var 1)) → ⊥
  cut1805  adequate = bad1805  (Adequate.valid adequate Two boolean env2)
  bad1806 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop b0 (bop b1 b0)))) b1 → ⊥
  bad1806  p = false≢true (cong lower p)
  cut1806 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 0) (op (var 1) (op (var 2) (var 1))))) , (var 2)) → ⊥
  cut1806  adequate = bad1806  (Adequate.valid adequate Two boolean env1)
  bad1807 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop b0 (bop b0 b0)))) b1 → ⊥
  bad1807  p = false≢true (cong lower p)
  cut1807 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 0) (op (var 1) (op (var 2) (var 1))))) , (var 3)) → ⊥
  cut1807  adequate = bad1807  (Adequate.valid adequate Two boolean env3)
  holds1808 : (z0 z1 z2 : A2) → (mul2 (mul2 z0 z1) (mul2 z0 (mul2 z1 (mul2 z2 z2)))) ≡ z0
  holds1808 z0 z1 z2 = refl
  cut1808 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 0) (op (var 1) (op (var 2) (var 2))))) , (var 0)) → ⊥
  cut1808  = reject2 ((op (op (var 0) (var 1)) (op (var 0) (op (var 1) (op (var 2) (var 2))))) , (var 0)) (λ env → holds1808 (env 0) (env 1) (env 2))
  bad1809 : PathP (λ _ → Two) (bop (bop b0 b1) (bop b0 (bop b1 (bop b0 b0)))) b1 → ⊥
  bad1809  p = false≢true (cong lower p)
  cut1809 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 0) (op (var 1) (op (var 2) (var 2))))) , (var 1)) → ⊥
  cut1809  adequate = bad1809  (Adequate.valid adequate Two boolean env2)
  bad1810 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop b0 (bop b1 b1)))) b1 → ⊥
  bad1810  p = false≢true (cong lower p)
  cut1810 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 0) (op (var 1) (op (var 2) (var 2))))) , (var 2)) → ⊥
  cut1810  adequate = bad1810  (Adequate.valid adequate Two boolean env1)
  bad1811 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop b0 (bop b0 b0)))) b1 → ⊥
  bad1811  p = false≢true (cong lower p)
  cut1811 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 0) (op (var 1) (op (var 2) (var 2))))) , (var 3)) → ⊥
  cut1811  adequate = bad1811  (Adequate.valid adequate Two boolean env3)
  holds1812 : (z0 z1 z2 z3 : A2) → (mul2 (mul2 z0 z1) (mul2 z0 (mul2 z1 (mul2 z2 z3)))) ≡ z0
  holds1812 z0 z1 z2 z3 = refl
  cut1812 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 0) (op (var 1) (op (var 2) (var 3))))) , (var 0)) → ⊥
  cut1812  = reject2 ((op (op (var 0) (var 1)) (op (var 0) (op (var 1) (op (var 2) (var 3))))) , (var 0)) (λ env → holds1812 (env 0) (env 1) (env 2) (env 3))
  bad1813 : PathP (λ _ → Two) (bop (bop b0 b1) (bop b0 (bop b1 (bop b0 b0)))) b1 → ⊥
  bad1813  p = false≢true (cong lower p)
  cut1813 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 0) (op (var 1) (op (var 2) (var 3))))) , (var 1)) → ⊥
  cut1813  adequate = bad1813  (Adequate.valid adequate Two boolean env4)
  bad1814 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop b0 (bop b1 b0)))) b1 → ⊥
  bad1814  p = false≢true (cong lower p)
  cut1814 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 0) (op (var 1) (op (var 2) (var 3))))) , (var 2)) → ⊥
  cut1814  adequate = bad1814  (Adequate.valid adequate Two boolean env5)
  bad1815 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop b0 (bop b0 b1)))) b1 → ⊥
  bad1815  p = false≢true (cong lower p)
  cut1815 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 0) (op (var 1) (op (var 2) (var 3))))) , (var 3)) → ⊥
  cut1815  adequate = bad1815  (Adequate.valid adequate Two boolean env3)
  bad1816 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop b0 (bop b0 b0)))) b1 → ⊥
  bad1816  p = false≢true (cong lower p)
  cut1816 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 0) (op (var 1) (op (var 2) (var 3))))) , (var 4)) → ⊥
  cut1816  adequate = bad1816  (Adequate.valid adequate Two boolean env6)
  holds1817 : (z0 z1 z2 : A2) → (mul2 (mul2 z0 z1) (mul2 z0 (mul2 z2 (mul2 z0 z0)))) ≡ z0
  holds1817 z0 z1 z2 = refl
  cut1817 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 0) (op (var 2) (op (var 0) (var 0))))) , (var 0)) → ⊥
  cut1817  = reject2 ((op (op (var 0) (var 1)) (op (var 0) (op (var 2) (op (var 0) (var 0))))) , (var 0)) (λ env → holds1817 (env 0) (env 1) (env 2))
  bad1818 : PathP (λ _ → Two) (bop (bop b0 b1) (bop b0 (bop b0 (bop b0 b0)))) b1 → ⊥
  bad1818  p = false≢true (cong lower p)
  cut1818 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 0) (op (var 2) (op (var 0) (var 0))))) , (var 1)) → ⊥
  cut1818  adequate = bad1818  (Adequate.valid adequate Two boolean env2)
  bad1819 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop b1 (bop b0 b0)))) b1 → ⊥
  bad1819  p = false≢true (cong lower p)
  cut1819 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 0) (op (var 2) (op (var 0) (var 0))))) , (var 2)) → ⊥
  cut1819  adequate = bad1819  (Adequate.valid adequate Two boolean env1)
  bad1820 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop b0 (bop b0 b0)))) b1 → ⊥
  bad1820  p = false≢true (cong lower p)
  cut1820 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 0) (op (var 2) (op (var 0) (var 0))))) , (var 3)) → ⊥
  cut1820  adequate = bad1820  (Adequate.valid adequate Two boolean env3)
  env18 : ℕ → Two
  env18 zero = b1
  env18 (suc zero) = b0
  env18 (suc (suc zero)) = b1
  env18 (suc (suc (suc rest))) = b0
  bad1821 : PathP (λ _ → Two) (bop (bop b1 b0) (bop b1 (bop b1 (bop b1 b0)))) b1 → ⊥
  bad1821  p = false≢true (cong lower p)
  cut1821 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 0) (op (var 2) (op (var 0) (var 1))))) , (var 0)) → ⊥
  cut1821  adequate = bad1821  (Adequate.valid adequate Two boolean env18)
  bad1822 : PathP (λ _ → Two) (bop (bop b0 b1) (bop b0 (bop b0 (bop b0 b1)))) b1 → ⊥
  bad1822  p = false≢true (cong lower p)
  cut1822 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 0) (op (var 2) (op (var 0) (var 1))))) , (var 1)) → ⊥
  cut1822  adequate = bad1822  (Adequate.valid adequate Two boolean env2)
  bad1823 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop b1 (bop b0 b0)))) b1 → ⊥
  bad1823  p = false≢true (cong lower p)
  cut1823 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 0) (op (var 2) (op (var 0) (var 1))))) , (var 2)) → ⊥
  cut1823  adequate = bad1823  (Adequate.valid adequate Two boolean env1)
  bad1824 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop b0 (bop b0 b0)))) b1 → ⊥
  bad1824  p = false≢true (cong lower p)
  cut1824 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 0) (op (var 2) (op (var 0) (var 1))))) , (var 3)) → ⊥
  cut1824  adequate = bad1824  (Adequate.valid adequate Two boolean env3)
  holds1825 : (z0 z1 z2 : A2) → (mul2 (mul2 z0 z1) (mul2 z0 (mul2 z2 (mul2 z0 z2)))) ≡ z0
  holds1825 z0 z1 z2 = refl
  cut1825 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 0) (op (var 2) (op (var 0) (var 2))))) , (var 0)) → ⊥
  cut1825  = reject2 ((op (op (var 0) (var 1)) (op (var 0) (op (var 2) (op (var 0) (var 2))))) , (var 0)) (λ env → holds1825 (env 0) (env 1) (env 2))
  bad1826 : PathP (λ _ → Two) (bop (bop b0 b1) (bop b0 (bop b0 (bop b0 b0)))) b1 → ⊥
  bad1826  p = false≢true (cong lower p)
  cut1826 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 0) (op (var 2) (op (var 0) (var 2))))) , (var 1)) → ⊥
  cut1826  adequate = bad1826  (Adequate.valid adequate Two boolean env2)
  bad1827 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop b1 (bop b0 b1)))) b1 → ⊥
  bad1827  p = false≢true (cong lower p)
  cut1827 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 0) (op (var 2) (op (var 0) (var 2))))) , (var 2)) → ⊥
  cut1827  adequate = bad1827  (Adequate.valid adequate Two boolean env1)
  bad1828 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop b0 (bop b0 b0)))) b1 → ⊥
  bad1828  p = false≢true (cong lower p)
  cut1828 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 0) (op (var 2) (op (var 0) (var 2))))) , (var 3)) → ⊥
  cut1828  adequate = bad1828  (Adequate.valid adequate Two boolean env3)
  env19 : ℕ → Two
  env19 zero = b1
  env19 (suc zero) = b0
  env19 (suc (suc zero)) = b1
  env19 (suc (suc (suc zero))) = b0
  env19 (suc (suc (suc (suc rest)))) = b0
  bad1829 : PathP (λ _ → Two) (bop (bop b1 b0) (bop b1 (bop b1 (bop b1 b0)))) b1 → ⊥
  bad1829  p = false≢true (cong lower p)
  cut1829 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 0) (op (var 2) (op (var 0) (var 3))))) , (var 0)) → ⊥
  cut1829  adequate = bad1829  (Adequate.valid adequate Two boolean env19)
  bad1830 : PathP (λ _ → Two) (bop (bop b0 b1) (bop b0 (bop b0 (bop b0 b0)))) b1 → ⊥
  bad1830  p = false≢true (cong lower p)
  cut1830 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 0) (op (var 2) (op (var 0) (var 3))))) , (var 1)) → ⊥
  cut1830  adequate = bad1830  (Adequate.valid adequate Two boolean env4)
  bad1831 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop b1 (bop b0 b0)))) b1 → ⊥
  bad1831  p = false≢true (cong lower p)
  cut1831 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 0) (op (var 2) (op (var 0) (var 3))))) , (var 2)) → ⊥
  cut1831  adequate = bad1831  (Adequate.valid adequate Two boolean env5)
  bad1832 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop b0 (bop b0 b1)))) b1 → ⊥
  bad1832  p = false≢true (cong lower p)
  cut1832 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 0) (op (var 2) (op (var 0) (var 3))))) , (var 3)) → ⊥
  cut1832  adequate = bad1832  (Adequate.valid adequate Two boolean env3)
  bad1833 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop b0 (bop b0 b0)))) b1 → ⊥
  bad1833  p = false≢true (cong lower p)
  cut1833 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 0) (op (var 2) (op (var 0) (var 3))))) , (var 4)) → ⊥
  cut1833  adequate = bad1833  (Adequate.valid adequate Two boolean env6)
  bad1834 : PathP (λ _ → Two) (bop (bop b1 b0) (bop b1 (bop b1 (bop b0 b1)))) b1 → ⊥
  bad1834  p = false≢true (cong lower p)
  cut1834 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 0) (op (var 2) (op (var 1) (var 0))))) , (var 0)) → ⊥
  cut1834  adequate = bad1834  (Adequate.valid adequate Two boolean env18)
  bad1835 : PathP (λ _ → Two) (bop (bop b0 b1) (bop b0 (bop b0 (bop b1 b0)))) b1 → ⊥
  bad1835  p = false≢true (cong lower p)
  cut1835 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 0) (op (var 2) (op (var 1) (var 0))))) , (var 1)) → ⊥
  cut1835  adequate = bad1835  (Adequate.valid adequate Two boolean env2)
  bad1836 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop b1 (bop b0 b0)))) b1 → ⊥
  bad1836  p = false≢true (cong lower p)
  cut1836 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 0) (op (var 2) (op (var 1) (var 0))))) , (var 2)) → ⊥
  cut1836  adequate = bad1836  (Adequate.valid adequate Two boolean env1)
  bad1837 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop b0 (bop b0 b0)))) b1 → ⊥
  bad1837  p = false≢true (cong lower p)
  cut1837 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 0) (op (var 2) (op (var 1) (var 0))))) , (var 3)) → ⊥
  cut1837  adequate = bad1837  (Adequate.valid adequate Two boolean env3)
  bad1838 : PathP (λ _ → Two) (bop (bop b1 b0) (bop b1 (bop b1 (bop b0 b0)))) b1 → ⊥
  bad1838  p = false≢true (cong lower p)
  cut1838 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 0) (op (var 2) (op (var 1) (var 1))))) , (var 0)) → ⊥
  cut1838  adequate = bad1838  (Adequate.valid adequate Two boolean env18)
  bad1839 : PathP (λ _ → Two) (bop (bop b0 b1) (bop b0 (bop b0 (bop b1 b1)))) b1 → ⊥
  bad1839  p = false≢true (cong lower p)
  cut1839 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 0) (op (var 2) (op (var 1) (var 1))))) , (var 1)) → ⊥
  cut1839  adequate = bad1839  (Adequate.valid adequate Two boolean env2)
  bad1840 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop b1 (bop b0 b0)))) b1 → ⊥
  bad1840  p = false≢true (cong lower p)
  cut1840 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 0) (op (var 2) (op (var 1) (var 1))))) , (var 2)) → ⊥
  cut1840  adequate = bad1840  (Adequate.valid adequate Two boolean env1)
  bad1841 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop b0 (bop b0 b0)))) b1 → ⊥
  bad1841  p = false≢true (cong lower p)
  cut1841 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 0) (op (var 2) (op (var 1) (var 1))))) , (var 3)) → ⊥
  cut1841  adequate = bad1841  (Adequate.valid adequate Two boolean env3)
  bad1842 : PathP (λ _ → Two) (bop (bop b1 b0) (bop b1 (bop b1 (bop b0 b1)))) b1 → ⊥
  bad1842  p = false≢true (cong lower p)
  cut1842 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 0) (op (var 2) (op (var 1) (var 2))))) , (var 0)) → ⊥
  cut1842  adequate = bad1842  (Adequate.valid adequate Two boolean env18)
  bad1843 : PathP (λ _ → Two) (bop (bop b0 b1) (bop b0 (bop b0 (bop b1 b0)))) b1 → ⊥
  bad1843  p = false≢true (cong lower p)
  cut1843 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 0) (op (var 2) (op (var 1) (var 2))))) , (var 1)) → ⊥
  cut1843  adequate = bad1843  (Adequate.valid adequate Two boolean env2)
  bad1844 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop b1 (bop b0 b1)))) b1 → ⊥
  bad1844  p = false≢true (cong lower p)
  cut1844 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 0) (op (var 2) (op (var 1) (var 2))))) , (var 2)) → ⊥
  cut1844  adequate = bad1844  (Adequate.valid adequate Two boolean env1)
  bad1845 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop b0 (bop b0 b0)))) b1 → ⊥
  bad1845  p = false≢true (cong lower p)
  cut1845 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 0) (op (var 2) (op (var 1) (var 2))))) , (var 3)) → ⊥
  cut1845  adequate = bad1845  (Adequate.valid adequate Two boolean env3)
  bad1846 : PathP (λ _ → Two) (bop (bop b1 b0) (bop b1 (bop b1 (bop b0 b0)))) b1 → ⊥
  bad1846  p = false≢true (cong lower p)
  cut1846 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 0) (op (var 2) (op (var 1) (var 3))))) , (var 0)) → ⊥
  cut1846  adequate = bad1846  (Adequate.valid adequate Two boolean env19)
  bad1847 : PathP (λ _ → Two) (bop (bop b0 b1) (bop b0 (bop b0 (bop b1 b0)))) b1 → ⊥
  bad1847  p = false≢true (cong lower p)
  cut1847 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 0) (op (var 2) (op (var 1) (var 3))))) , (var 1)) → ⊥
  cut1847  adequate = bad1847  (Adequate.valid adequate Two boolean env4)
  bad1848 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop b1 (bop b0 b0)))) b1 → ⊥
  bad1848  p = false≢true (cong lower p)
  cut1848 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 0) (op (var 2) (op (var 1) (var 3))))) , (var 2)) → ⊥
  cut1848  adequate = bad1848  (Adequate.valid adequate Two boolean env5)
  bad1849 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop b0 (bop b0 b1)))) b1 → ⊥
  bad1849  p = false≢true (cong lower p)
  cut1849 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 0) (op (var 2) (op (var 1) (var 3))))) , (var 3)) → ⊥
  cut1849  adequate = bad1849  (Adequate.valid adequate Two boolean env3)
  bad1850 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop b0 (bop b0 b0)))) b1 → ⊥
  bad1850  p = false≢true (cong lower p)
  cut1850 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 0) (op (var 2) (op (var 1) (var 3))))) , (var 4)) → ⊥
  cut1850  adequate = bad1850  (Adequate.valid adequate Two boolean env6)
  holds1851 : (z0 z1 z2 : A2) → (mul2 (mul2 z0 z1) (mul2 z0 (mul2 z2 (mul2 z2 z0)))) ≡ z0
  holds1851 z0 z1 z2 = refl
  cut1851 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 0) (op (var 2) (op (var 2) (var 0))))) , (var 0)) → ⊥
  cut1851  = reject2 ((op (op (var 0) (var 1)) (op (var 0) (op (var 2) (op (var 2) (var 0))))) , (var 0)) (λ env → holds1851 (env 0) (env 1) (env 2))
  bad1852 : PathP (λ _ → Two) (bop (bop b0 b1) (bop b0 (bop b0 (bop b0 b0)))) b1 → ⊥
  bad1852  p = false≢true (cong lower p)
  cut1852 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 0) (op (var 2) (op (var 2) (var 0))))) , (var 1)) → ⊥
  cut1852  adequate = bad1852  (Adequate.valid adequate Two boolean env2)
  bad1853 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop b1 (bop b1 b0)))) b1 → ⊥
  bad1853  p = false≢true (cong lower p)
  cut1853 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 0) (op (var 2) (op (var 2) (var 0))))) , (var 2)) → ⊥
  cut1853  adequate = bad1853  (Adequate.valid adequate Two boolean env1)
  bad1854 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop b0 (bop b0 b0)))) b1 → ⊥
  bad1854  p = false≢true (cong lower p)
  cut1854 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 0) (op (var 2) (op (var 2) (var 0))))) , (var 3)) → ⊥
  cut1854  adequate = bad1854  (Adequate.valid adequate Two boolean env3)
  bad1855 : PathP (λ _ → Two) (bop (bop b1 b0) (bop b1 (bop b1 (bop b1 b0)))) b1 → ⊥
  bad1855  p = false≢true (cong lower p)
  cut1855 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 0) (op (var 2) (op (var 2) (var 1))))) , (var 0)) → ⊥
  cut1855  adequate = bad1855  (Adequate.valid adequate Two boolean env18)
  bad1856 : PathP (λ _ → Two) (bop (bop b0 b1) (bop b0 (bop b0 (bop b0 b1)))) b1 → ⊥
  bad1856  p = false≢true (cong lower p)
  cut1856 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 0) (op (var 2) (op (var 2) (var 1))))) , (var 1)) → ⊥
  cut1856  adequate = bad1856  (Adequate.valid adequate Two boolean env2)
  bad1857 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop b1 (bop b1 b0)))) b1 → ⊥
  bad1857  p = false≢true (cong lower p)
  cut1857 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 0) (op (var 2) (op (var 2) (var 1))))) , (var 2)) → ⊥
  cut1857  adequate = bad1857  (Adequate.valid adequate Two boolean env1)
  bad1858 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop b0 (bop b0 b0)))) b1 → ⊥
  bad1858  p = false≢true (cong lower p)
  cut1858 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 0) (op (var 2) (op (var 2) (var 1))))) , (var 3)) → ⊥
  cut1858  adequate = bad1858  (Adequate.valid adequate Two boolean env3)
  holds1859 : (z0 z1 z2 : A2) → (mul2 (mul2 z0 z1) (mul2 z0 (mul2 z2 (mul2 z2 z2)))) ≡ z0
  holds1859 z0 z1 z2 = refl
  cut1859 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 0) (op (var 2) (op (var 2) (var 2))))) , (var 0)) → ⊥
  cut1859  = reject2 ((op (op (var 0) (var 1)) (op (var 0) (op (var 2) (op (var 2) (var 2))))) , (var 0)) (λ env → holds1859 (env 0) (env 1) (env 2))
  bad1860 : PathP (λ _ → Two) (bop (bop b0 b1) (bop b0 (bop b0 (bop b0 b0)))) b1 → ⊥
  bad1860  p = false≢true (cong lower p)
  cut1860 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 0) (op (var 2) (op (var 2) (var 2))))) , (var 1)) → ⊥
  cut1860  adequate = bad1860  (Adequate.valid adequate Two boolean env2)
  bad1861 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop b1 (bop b1 b1)))) b1 → ⊥
  bad1861  p = false≢true (cong lower p)
  cut1861 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 0) (op (var 2) (op (var 2) (var 2))))) , (var 2)) → ⊥
  cut1861  adequate = bad1861  (Adequate.valid adequate Two boolean env1)
  bad1862 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop b0 (bop b0 b0)))) b1 → ⊥
  bad1862  p = false≢true (cong lower p)
  cut1862 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 0) (op (var 2) (op (var 2) (var 2))))) , (var 3)) → ⊥
  cut1862  adequate = bad1862  (Adequate.valid adequate Two boolean env3)
  bad1863 : PathP (λ _ → Two) (bop (bop b1 b0) (bop b1 (bop b1 (bop b1 b0)))) b1 → ⊥
  bad1863  p = false≢true (cong lower p)
  cut1863 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 0) (op (var 2) (op (var 2) (var 3))))) , (var 0)) → ⊥
  cut1863  adequate = bad1863  (Adequate.valid adequate Two boolean env19)
  bad1864 : PathP (λ _ → Two) (bop (bop b0 b1) (bop b0 (bop b0 (bop b0 b0)))) b1 → ⊥
  bad1864  p = false≢true (cong lower p)
  cut1864 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 0) (op (var 2) (op (var 2) (var 3))))) , (var 1)) → ⊥
  cut1864  adequate = bad1864  (Adequate.valid adequate Two boolean env4)
  bad1865 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop b1 (bop b1 b0)))) b1 → ⊥
  bad1865  p = false≢true (cong lower p)
  cut1865 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 0) (op (var 2) (op (var 2) (var 3))))) , (var 2)) → ⊥
  cut1865  adequate = bad1865  (Adequate.valid adequate Two boolean env5)
  bad1866 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop b0 (bop b0 b1)))) b1 → ⊥
  bad1866  p = false≢true (cong lower p)
  cut1866 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 0) (op (var 2) (op (var 2) (var 3))))) , (var 3)) → ⊥
  cut1866  adequate = bad1866  (Adequate.valid adequate Two boolean env3)
  bad1867 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop b0 (bop b0 b0)))) b1 → ⊥
  bad1867  p = false≢true (cong lower p)
  cut1867 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 0) (op (var 2) (op (var 2) (var 3))))) , (var 4)) → ⊥
  cut1867  adequate = bad1867  (Adequate.valid adequate Two boolean env6)
  bad1868 : PathP (λ _ → Two) (bop (bop b1 b0) (bop b1 (bop b1 (bop b0 b1)))) b1 → ⊥
  bad1868  p = false≢true (cong lower p)
  cut1868 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 0) (op (var 2) (op (var 3) (var 0))))) , (var 0)) → ⊥
  cut1868  adequate = bad1868  (Adequate.valid adequate Two boolean env19)
  bad1869 : PathP (λ _ → Two) (bop (bop b0 b1) (bop b0 (bop b0 (bop b0 b0)))) b1 → ⊥
  bad1869  p = false≢true (cong lower p)
  cut1869 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 0) (op (var 2) (op (var 3) (var 0))))) , (var 1)) → ⊥
  cut1869  adequate = bad1869  (Adequate.valid adequate Two boolean env4)
  bad1870 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop b1 (bop b0 b0)))) b1 → ⊥
  bad1870  p = false≢true (cong lower p)
  cut1870 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 0) (op (var 2) (op (var 3) (var 0))))) , (var 2)) → ⊥
  cut1870  adequate = bad1870  (Adequate.valid adequate Two boolean env5)
  bad1871 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop b0 (bop b1 b0)))) b1 → ⊥
  bad1871  p = false≢true (cong lower p)
  cut1871 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 0) (op (var 2) (op (var 3) (var 0))))) , (var 3)) → ⊥
  cut1871  adequate = bad1871  (Adequate.valid adequate Two boolean env3)
  bad1872 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop b0 (bop b0 b0)))) b1 → ⊥
  bad1872  p = false≢true (cong lower p)
  cut1872 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 0) (op (var 2) (op (var 3) (var 0))))) , (var 4)) → ⊥
  cut1872  adequate = bad1872  (Adequate.valid adequate Two boolean env6)
  bad1873 : PathP (λ _ → Two) (bop (bop b1 b0) (bop b1 (bop b1 (bop b0 b0)))) b1 → ⊥
  bad1873  p = false≢true (cong lower p)
  cut1873 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 0) (op (var 2) (op (var 3) (var 1))))) , (var 0)) → ⊥
  cut1873  adequate = bad1873  (Adequate.valid adequate Two boolean env19)
  bad1874 : PathP (λ _ → Two) (bop (bop b0 b1) (bop b0 (bop b0 (bop b0 b1)))) b1 → ⊥
  bad1874  p = false≢true (cong lower p)
  cut1874 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 0) (op (var 2) (op (var 3) (var 1))))) , (var 1)) → ⊥
  cut1874  adequate = bad1874  (Adequate.valid adequate Two boolean env4)
  bad1875 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop b1 (bop b0 b0)))) b1 → ⊥
  bad1875  p = false≢true (cong lower p)
  cut1875 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 0) (op (var 2) (op (var 3) (var 1))))) , (var 2)) → ⊥
  cut1875  adequate = bad1875  (Adequate.valid adequate Two boolean env5)
  bad1876 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop b0 (bop b1 b0)))) b1 → ⊥
  bad1876  p = false≢true (cong lower p)
  cut1876 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 0) (op (var 2) (op (var 3) (var 1))))) , (var 3)) → ⊥
  cut1876  adequate = bad1876  (Adequate.valid adequate Two boolean env3)
  bad1877 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop b0 (bop b0 b0)))) b1 → ⊥
  bad1877  p = false≢true (cong lower p)
  cut1877 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 0) (op (var 2) (op (var 3) (var 1))))) , (var 4)) → ⊥
  cut1877  adequate = bad1877  (Adequate.valid adequate Two boolean env6)
  bad1878 : PathP (λ _ → Two) (bop (bop b1 b0) (bop b1 (bop b1 (bop b0 b1)))) b1 → ⊥
  bad1878  p = false≢true (cong lower p)
  cut1878 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 0) (op (var 2) (op (var 3) (var 2))))) , (var 0)) → ⊥
  cut1878  adequate = bad1878  (Adequate.valid adequate Two boolean env19)
  bad1879 : PathP (λ _ → Two) (bop (bop b0 b1) (bop b0 (bop b0 (bop b0 b0)))) b1 → ⊥
  bad1879  p = false≢true (cong lower p)
  cut1879 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 0) (op (var 2) (op (var 3) (var 2))))) , (var 1)) → ⊥
  cut1879  adequate = bad1879  (Adequate.valid adequate Two boolean env4)
  bad1880 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop b1 (bop b0 b1)))) b1 → ⊥
  bad1880  p = false≢true (cong lower p)
  cut1880 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 0) (op (var 2) (op (var 3) (var 2))))) , (var 2)) → ⊥
  cut1880  adequate = bad1880  (Adequate.valid adequate Two boolean env5)
  bad1881 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop b0 (bop b1 b0)))) b1 → ⊥
  bad1881  p = false≢true (cong lower p)
  cut1881 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 0) (op (var 2) (op (var 3) (var 2))))) , (var 3)) → ⊥
  cut1881  adequate = bad1881  (Adequate.valid adequate Two boolean env3)
  bad1882 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop b0 (bop b0 b0)))) b1 → ⊥
  bad1882  p = false≢true (cong lower p)
  cut1882 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 0) (op (var 2) (op (var 3) (var 2))))) , (var 4)) → ⊥
  cut1882  adequate = bad1882  (Adequate.valid adequate Two boolean env6)
  bad1883 : PathP (λ _ → Two) (bop (bop b1 b0) (bop b1 (bop b1 (bop b0 b0)))) b1 → ⊥
  bad1883  p = false≢true (cong lower p)
  cut1883 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 0) (op (var 2) (op (var 3) (var 3))))) , (var 0)) → ⊥
  cut1883  adequate = bad1883  (Adequate.valid adequate Two boolean env19)
  bad1884 : PathP (λ _ → Two) (bop (bop b0 b1) (bop b0 (bop b0 (bop b0 b0)))) b1 → ⊥
  bad1884  p = false≢true (cong lower p)
  cut1884 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 0) (op (var 2) (op (var 3) (var 3))))) , (var 1)) → ⊥
  cut1884  adequate = bad1884  (Adequate.valid adequate Two boolean env4)
  bad1885 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop b1 (bop b0 b0)))) b1 → ⊥
  bad1885  p = false≢true (cong lower p)
  cut1885 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 0) (op (var 2) (op (var 3) (var 3))))) , (var 2)) → ⊥
  cut1885  adequate = bad1885  (Adequate.valid adequate Two boolean env5)
  bad1886 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop b0 (bop b1 b1)))) b1 → ⊥
  bad1886  p = false≢true (cong lower p)
  cut1886 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 0) (op (var 2) (op (var 3) (var 3))))) , (var 3)) → ⊥
  cut1886  adequate = bad1886  (Adequate.valid adequate Two boolean env3)
  bad1887 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop b0 (bop b0 b0)))) b1 → ⊥
  bad1887  p = false≢true (cong lower p)
  cut1887 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 0) (op (var 2) (op (var 3) (var 3))))) , (var 4)) → ⊥
  cut1887  adequate = bad1887  (Adequate.valid adequate Two boolean env6)
  env20 : ℕ → Two
  env20 zero = b1
  env20 (suc zero) = b0
  env20 (suc (suc zero)) = b1
  env20 (suc (suc (suc zero))) = b0
  env20 (suc (suc (suc (suc zero)))) = b0
  env20 (suc (suc (suc (suc (suc rest))))) = b0
  bad1888 : PathP (λ _ → Two) (bop (bop b1 b0) (bop b1 (bop b1 (bop b0 b0)))) b1 → ⊥
  bad1888  p = false≢true (cong lower p)
  cut1888 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 0) (op (var 2) (op (var 3) (var 4))))) , (var 0)) → ⊥
  cut1888  adequate = bad1888  (Adequate.valid adequate Two boolean env20)
  bad1889 : PathP (λ _ → Two) (bop (bop b0 b1) (bop b0 (bop b0 (bop b0 b0)))) b1 → ⊥
  bad1889  p = false≢true (cong lower p)
  cut1889 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 0) (op (var 2) (op (var 3) (var 4))))) , (var 1)) → ⊥
  cut1889  adequate = bad1889  (Adequate.valid adequate Two boolean env13)
  bad1890 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop b1 (bop b0 b0)))) b1 → ⊥
  bad1890  p = false≢true (cong lower p)
  cut1890 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 0) (op (var 2) (op (var 3) (var 4))))) , (var 2)) → ⊥
  cut1890  adequate = bad1890  (Adequate.valid adequate Two boolean env15)
  bad1891 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop b0 (bop b1 b0)))) b1 → ⊥
  bad1891  p = false≢true (cong lower p)
  cut1891 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 0) (op (var 2) (op (var 3) (var 4))))) , (var 3)) → ⊥
  cut1891  adequate = bad1891  (Adequate.valid adequate Two boolean env16)
  bad1892 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop b0 (bop b0 b1)))) b1 → ⊥
  bad1892  p = false≢true (cong lower p)
  cut1892 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 0) (op (var 2) (op (var 3) (var 4))))) , (var 4)) → ⊥
  cut1892  adequate = bad1892  (Adequate.valid adequate Two boolean env6)
  bad1893 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop b0 (bop b0 b0)))) b1 → ⊥
  bad1893  p = false≢true (cong lower p)
  cut1893 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 0) (op (var 2) (op (var 3) (var 4))))) , (var 5)) → ⊥
  cut1893  adequate = bad1893  (Adequate.valid adequate Two boolean env17)
  bad1894 : PathP (λ _ → Two) (bop (bop b0 b1) (bop b1 (bop b0 (bop b0 b0)))) b0 → ⊥
  bad1894  p = false≢true (sym (cong lower p))
  cut1894 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 1) (op (var 0) (op (var 0) (var 0))))) , (var 0)) → ⊥
  cut1894  adequate = bad1894  (Adequate.valid adequate Two boolean env0)
  holds1895 : (z0 z1 : A6) → (mul6 (mul6 z0 z1) (mul6 z1 (mul6 z0 (mul6 z0 z0)))) ≡ z1
  holds1895 m6c0 m6c0 = refl
  holds1895 m6c0 m6c1 = refl
  holds1895 m6c0 m6c2 = refl
  holds1895 m6c1 m6c0 = refl
  holds1895 m6c1 m6c1 = refl
  holds1895 m6c1 m6c2 = refl
  holds1895 m6c2 m6c0 = refl
  holds1895 m6c2 m6c1 = refl
  holds1895 m6c2 m6c2 = refl
  cut1895 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 1) (op (var 0) (op (var 0) (var 0))))) , (var 1)) → ⊥
  cut1895  = reject6 ((op (op (var 0) (var 1)) (op (var 1) (op (var 0) (op (var 0) (var 0))))) , (var 1)) (λ env → holds1895 (env 0) (env 1))
  bad1896 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop b0 (bop b0 b0)))) b1 → ⊥
  bad1896  p = false≢true (cong lower p)
  cut1896 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 1) (op (var 0) (op (var 0) (var 0))))) , (var 2)) → ⊥
  cut1896  adequate = bad1896  (Adequate.valid adequate Two boolean env1)
  bad1897 : PathP (λ _ → Two) (bop (bop b0 b1) (bop b1 (bop b0 (bop b0 b1)))) b0 → ⊥
  bad1897  p = false≢true (sym (cong lower p))
  cut1897 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 1) (op (var 0) (op (var 0) (var 1))))) , (var 0)) → ⊥
  cut1897  adequate = bad1897  (Adequate.valid adequate Two boolean env0)
  holds1898 : (z0 z1 : A3) → (mul3 (mul3 z0 z1) (mul3 z1 (mul3 z0 (mul3 z0 z1)))) ≡ z1
  holds1898 z0 z1 = refl
  cut1898 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 1) (op (var 0) (op (var 0) (var 1))))) , (var 1)) → ⊥
  cut1898  = reject3 ((op (op (var 0) (var 1)) (op (var 1) (op (var 0) (op (var 0) (var 1))))) , (var 1)) (λ env → holds1898 (env 0) (env 1))
  bad1899 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop b0 (bop b0 b0)))) b1 → ⊥
  bad1899  p = false≢true (cong lower p)
  cut1899 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 1) (op (var 0) (op (var 0) (var 1))))) , (var 2)) → ⊥
  cut1899  adequate = bad1899  (Adequate.valid adequate Two boolean env1)
  bad1900 : PathP (λ _ → Two) (bop (bop b0 b1) (bop b1 (bop b0 (bop b0 b0)))) b0 → ⊥
  bad1900  p = false≢true (sym (cong lower p))
  cut1900 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 1) (op (var 0) (op (var 0) (var 2))))) , (var 0)) → ⊥
  cut1900  adequate = bad1900  (Adequate.valid adequate Two boolean env2)
  holds1901 : (z0 z1 z2 : A7) → (mul7 (mul7 z0 z1) (mul7 z1 (mul7 z0 (mul7 z0 z2)))) ≡ z1
  holds1901 m7c0 m7c0 m7c0 = refl
  holds1901 m7c0 m7c0 m7c1 = refl
  holds1901 m7c0 m7c0 m7c2 = refl
  holds1901 m7c0 m7c1 m7c0 = refl
  holds1901 m7c0 m7c1 m7c1 = refl
  holds1901 m7c0 m7c1 m7c2 = refl
  holds1901 m7c0 m7c2 m7c0 = refl
  holds1901 m7c0 m7c2 m7c1 = refl
  holds1901 m7c0 m7c2 m7c2 = refl
  holds1901 m7c1 m7c0 m7c0 = refl
  holds1901 m7c1 m7c0 m7c1 = refl
  holds1901 m7c1 m7c0 m7c2 = refl
  holds1901 m7c1 m7c1 m7c0 = refl
  holds1901 m7c1 m7c1 m7c1 = refl
  holds1901 m7c1 m7c1 m7c2 = refl
  holds1901 m7c1 m7c2 m7c0 = refl
  holds1901 m7c1 m7c2 m7c1 = refl
  holds1901 m7c1 m7c2 m7c2 = refl
  holds1901 m7c2 m7c0 m7c0 = refl
  holds1901 m7c2 m7c0 m7c1 = refl
  holds1901 m7c2 m7c0 m7c2 = refl
  holds1901 m7c2 m7c1 m7c0 = refl
  holds1901 m7c2 m7c1 m7c1 = refl
  holds1901 m7c2 m7c1 m7c2 = refl
  holds1901 m7c2 m7c2 m7c0 = refl
  holds1901 m7c2 m7c2 m7c1 = refl
  holds1901 m7c2 m7c2 m7c2 = refl
  cut1901 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 1) (op (var 0) (op (var 0) (var 2))))) , (var 1)) → ⊥
  cut1901  = reject7 ((op (op (var 0) (var 1)) (op (var 1) (op (var 0) (op (var 0) (var 2))))) , (var 1)) (λ env → holds1901 (env 0) (env 1) (env 2))
  bad1902 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop b0 (bop b0 b1)))) b1 → ⊥
  bad1902  p = false≢true (cong lower p)
  cut1902 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 1) (op (var 0) (op (var 0) (var 2))))) , (var 2)) → ⊥
  cut1902  adequate = bad1902  (Adequate.valid adequate Two boolean env1)
  bad1903 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop b0 (bop b0 b0)))) b1 → ⊥
  bad1903  p = false≢true (cong lower p)
  cut1903 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 1) (op (var 0) (op (var 0) (var 2))))) , (var 3)) → ⊥
  cut1903  adequate = bad1903  (Adequate.valid adequate Two boolean env3)
  bad1904 : PathP (λ _ → Two) (bop (bop b0 b1) (bop b1 (bop b0 (bop b1 b0)))) b0 → ⊥
  bad1904  p = false≢true (sym (cong lower p))
  cut1904 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 1) (op (var 0) (op (var 1) (var 0))))) , (var 0)) → ⊥
  cut1904  adequate = bad1904  (Adequate.valid adequate Two boolean env0)
  holds1905 : (z0 z1 : A6) → (mul6 (mul6 z0 z1) (mul6 z1 (mul6 z0 (mul6 z1 z0)))) ≡ z1
  holds1905 m6c0 m6c0 = refl
  holds1905 m6c0 m6c1 = refl
  holds1905 m6c0 m6c2 = refl
  holds1905 m6c1 m6c0 = refl
  holds1905 m6c1 m6c1 = refl
  holds1905 m6c1 m6c2 = refl
  holds1905 m6c2 m6c0 = refl
  holds1905 m6c2 m6c1 = refl
  holds1905 m6c2 m6c2 = refl
  cut1905 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 1) (op (var 0) (op (var 1) (var 0))))) , (var 1)) → ⊥
  cut1905  = reject6 ((op (op (var 0) (var 1)) (op (var 1) (op (var 0) (op (var 1) (var 0))))) , (var 1)) (λ env → holds1905 (env 0) (env 1))
  bad1906 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop b0 (bop b0 b0)))) b1 → ⊥
  bad1906  p = false≢true (cong lower p)
  cut1906 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 1) (op (var 0) (op (var 1) (var 0))))) , (var 2)) → ⊥
  cut1906  adequate = bad1906  (Adequate.valid adequate Two boolean env1)
  bad1907 : PathP (λ _ → Two) (bop (bop b0 b1) (bop b1 (bop b0 (bop b1 b1)))) b0 → ⊥
  bad1907  p = false≢true (sym (cong lower p))
  cut1907 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 1) (op (var 0) (op (var 1) (var 1))))) , (var 0)) → ⊥
  cut1907  adequate = bad1907  (Adequate.valid adequate Two boolean env0)
  holds1908 : (z0 z1 : A3) → (mul3 (mul3 z0 z1) (mul3 z1 (mul3 z0 (mul3 z1 z1)))) ≡ z1
  holds1908 z0 z1 = refl
  cut1908 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 1) (op (var 0) (op (var 1) (var 1))))) , (var 1)) → ⊥
  cut1908  = reject3 ((op (op (var 0) (var 1)) (op (var 1) (op (var 0) (op (var 1) (var 1))))) , (var 1)) (λ env → holds1908 (env 0) (env 1))
  bad1909 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop b0 (bop b0 b0)))) b1 → ⊥
  bad1909  p = false≢true (cong lower p)
  cut1909 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 1) (op (var 0) (op (var 1) (var 1))))) , (var 2)) → ⊥
  cut1909  adequate = bad1909  (Adequate.valid adequate Two boolean env1)
  bad1910 : PathP (λ _ → Two) (bop (bop b0 b1) (bop b1 (bop b0 (bop b1 b0)))) b0 → ⊥
  bad1910  p = false≢true (sym (cong lower p))
  cut1910 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 1) (op (var 0) (op (var 1) (var 2))))) , (var 0)) → ⊥
  cut1910  adequate = bad1910  (Adequate.valid adequate Two boolean env2)
  holds1911 : (z0 z1 z2 : A13) → (mul13 (mul13 z0 z1) (mul13 z1 (mul13 z0 (mul13 z1 z2)))) ≡ z1
  holds1911 m13c0 m13c0 m13c0 = refl
  holds1911 m13c0 m13c0 m13c1 = refl
  holds1911 m13c0 m13c0 m13c2 = refl
  holds1911 m13c0 m13c0 m13c3 = refl
  holds1911 m13c0 m13c1 m13c0 = refl
  holds1911 m13c0 m13c1 m13c1 = refl
  holds1911 m13c0 m13c1 m13c2 = refl
  holds1911 m13c0 m13c1 m13c3 = refl
  holds1911 m13c0 m13c2 m13c0 = refl
  holds1911 m13c0 m13c2 m13c1 = refl
  holds1911 m13c0 m13c2 m13c2 = refl
  holds1911 m13c0 m13c2 m13c3 = refl
  holds1911 m13c0 m13c3 m13c0 = refl
  holds1911 m13c0 m13c3 m13c1 = refl
  holds1911 m13c0 m13c3 m13c2 = refl
  holds1911 m13c0 m13c3 m13c3 = refl
  holds1911 m13c1 m13c0 m13c0 = refl
  holds1911 m13c1 m13c0 m13c1 = refl
  holds1911 m13c1 m13c0 m13c2 = refl
  holds1911 m13c1 m13c0 m13c3 = refl
  holds1911 m13c1 m13c1 m13c0 = refl
  holds1911 m13c1 m13c1 m13c1 = refl
  holds1911 m13c1 m13c1 m13c2 = refl
  holds1911 m13c1 m13c1 m13c3 = refl
  holds1911 m13c1 m13c2 m13c0 = refl
  holds1911 m13c1 m13c2 m13c1 = refl
  holds1911 m13c1 m13c2 m13c2 = refl
  holds1911 m13c1 m13c2 m13c3 = refl
  holds1911 m13c1 m13c3 m13c0 = refl
  holds1911 m13c1 m13c3 m13c1 = refl
  holds1911 m13c1 m13c3 m13c2 = refl
  holds1911 m13c1 m13c3 m13c3 = refl
  holds1911 m13c2 m13c0 m13c0 = refl
  holds1911 m13c2 m13c0 m13c1 = refl
  holds1911 m13c2 m13c0 m13c2 = refl
  holds1911 m13c2 m13c0 m13c3 = refl
  holds1911 m13c2 m13c1 m13c0 = refl
  holds1911 m13c2 m13c1 m13c1 = refl
  holds1911 m13c2 m13c1 m13c2 = refl
  holds1911 m13c2 m13c1 m13c3 = refl
  holds1911 m13c2 m13c2 m13c0 = refl
  holds1911 m13c2 m13c2 m13c1 = refl
  holds1911 m13c2 m13c2 m13c2 = refl
  holds1911 m13c2 m13c2 m13c3 = refl
  holds1911 m13c2 m13c3 m13c0 = refl
  holds1911 m13c2 m13c3 m13c1 = refl
  holds1911 m13c2 m13c3 m13c2 = refl
  holds1911 m13c2 m13c3 m13c3 = refl
  holds1911 m13c3 m13c0 m13c0 = refl
  holds1911 m13c3 m13c0 m13c1 = refl
  holds1911 m13c3 m13c0 m13c2 = refl
  holds1911 m13c3 m13c0 m13c3 = refl
  holds1911 m13c3 m13c1 m13c0 = refl
  holds1911 m13c3 m13c1 m13c1 = refl
  holds1911 m13c3 m13c1 m13c2 = refl
  holds1911 m13c3 m13c1 m13c3 = refl
  holds1911 m13c3 m13c2 m13c0 = refl
  holds1911 m13c3 m13c2 m13c1 = refl
  holds1911 m13c3 m13c2 m13c2 = refl
  holds1911 m13c3 m13c2 m13c3 = refl
  holds1911 m13c3 m13c3 m13c0 = refl
  holds1911 m13c3 m13c3 m13c1 = refl
  holds1911 m13c3 m13c3 m13c2 = refl
  holds1911 m13c3 m13c3 m13c3 = refl
  cut1911 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 1) (op (var 0) (op (var 1) (var 2))))) , (var 1)) → ⊥
  cut1911  = reject13 ((op (op (var 0) (var 1)) (op (var 1) (op (var 0) (op (var 1) (var 2))))) , (var 1)) (λ env → holds1911 (env 0) (env 1) (env 2))
  bad1912 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop b0 (bop b0 b1)))) b1 → ⊥
  bad1912  p = false≢true (cong lower p)
  cut1912 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 1) (op (var 0) (op (var 1) (var 2))))) , (var 2)) → ⊥
  cut1912  adequate = bad1912  (Adequate.valid adequate Two boolean env1)
  bad1913 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop b0 (bop b0 b0)))) b1 → ⊥
  bad1913  p = false≢true (cong lower p)
  cut1913 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 1) (op (var 0) (op (var 1) (var 2))))) , (var 3)) → ⊥
  cut1913  adequate = bad1913  (Adequate.valid adequate Two boolean env3)
  bad1914 : PathP (λ _ → Two) (bop (bop b0 b1) (bop b1 (bop b0 (bop b0 b0)))) b0 → ⊥
  bad1914  p = false≢true (sym (cong lower p))
  cut1914 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 1) (op (var 0) (op (var 2) (var 0))))) , (var 0)) → ⊥
  cut1914  adequate = bad1914  (Adequate.valid adequate Two boolean env2)
  holds1915 : (z0 z1 z2 : A13) → (mul13 (mul13 z0 z1) (mul13 z1 (mul13 z0 (mul13 z2 z0)))) ≡ z1
  holds1915 m13c0 m13c0 m13c0 = refl
  holds1915 m13c0 m13c0 m13c1 = refl
  holds1915 m13c0 m13c0 m13c2 = refl
  holds1915 m13c0 m13c0 m13c3 = refl
  holds1915 m13c0 m13c1 m13c0 = refl
  holds1915 m13c0 m13c1 m13c1 = refl
  holds1915 m13c0 m13c1 m13c2 = refl
  holds1915 m13c0 m13c1 m13c3 = refl
  holds1915 m13c0 m13c2 m13c0 = refl
  holds1915 m13c0 m13c2 m13c1 = refl
  holds1915 m13c0 m13c2 m13c2 = refl
  holds1915 m13c0 m13c2 m13c3 = refl
  holds1915 m13c0 m13c3 m13c0 = refl
  holds1915 m13c0 m13c3 m13c1 = refl
  holds1915 m13c0 m13c3 m13c2 = refl
  holds1915 m13c0 m13c3 m13c3 = refl
  holds1915 m13c1 m13c0 m13c0 = refl
  holds1915 m13c1 m13c0 m13c1 = refl
  holds1915 m13c1 m13c0 m13c2 = refl
  holds1915 m13c1 m13c0 m13c3 = refl
  holds1915 m13c1 m13c1 m13c0 = refl
  holds1915 m13c1 m13c1 m13c1 = refl
  holds1915 m13c1 m13c1 m13c2 = refl
  holds1915 m13c1 m13c1 m13c3 = refl
  holds1915 m13c1 m13c2 m13c0 = refl
  holds1915 m13c1 m13c2 m13c1 = refl
  holds1915 m13c1 m13c2 m13c2 = refl
  holds1915 m13c1 m13c2 m13c3 = refl
  holds1915 m13c1 m13c3 m13c0 = refl
  holds1915 m13c1 m13c3 m13c1 = refl
  holds1915 m13c1 m13c3 m13c2 = refl
  holds1915 m13c1 m13c3 m13c3 = refl
  holds1915 m13c2 m13c0 m13c0 = refl
  holds1915 m13c2 m13c0 m13c1 = refl
  holds1915 m13c2 m13c0 m13c2 = refl
  holds1915 m13c2 m13c0 m13c3 = refl
  holds1915 m13c2 m13c1 m13c0 = refl
  holds1915 m13c2 m13c1 m13c1 = refl
  holds1915 m13c2 m13c1 m13c2 = refl
  holds1915 m13c2 m13c1 m13c3 = refl
  holds1915 m13c2 m13c2 m13c0 = refl
  holds1915 m13c2 m13c2 m13c1 = refl
  holds1915 m13c2 m13c2 m13c2 = refl
  holds1915 m13c2 m13c2 m13c3 = refl
  holds1915 m13c2 m13c3 m13c0 = refl
  holds1915 m13c2 m13c3 m13c1 = refl
  holds1915 m13c2 m13c3 m13c2 = refl
  holds1915 m13c2 m13c3 m13c3 = refl
  holds1915 m13c3 m13c0 m13c0 = refl
  holds1915 m13c3 m13c0 m13c1 = refl
  holds1915 m13c3 m13c0 m13c2 = refl
  holds1915 m13c3 m13c0 m13c3 = refl
  holds1915 m13c3 m13c1 m13c0 = refl
  holds1915 m13c3 m13c1 m13c1 = refl
  holds1915 m13c3 m13c1 m13c2 = refl
  holds1915 m13c3 m13c1 m13c3 = refl
  holds1915 m13c3 m13c2 m13c0 = refl
  holds1915 m13c3 m13c2 m13c1 = refl
  holds1915 m13c3 m13c2 m13c2 = refl
  holds1915 m13c3 m13c2 m13c3 = refl
  holds1915 m13c3 m13c3 m13c0 = refl
  holds1915 m13c3 m13c3 m13c1 = refl
  holds1915 m13c3 m13c3 m13c2 = refl
  holds1915 m13c3 m13c3 m13c3 = refl
  cut1915 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 1) (op (var 0) (op (var 2) (var 0))))) , (var 1)) → ⊥
  cut1915  = reject13 ((op (op (var 0) (var 1)) (op (var 1) (op (var 0) (op (var 2) (var 0))))) , (var 1)) (λ env → holds1915 (env 0) (env 1) (env 2))
  bad1916 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop b0 (bop b1 b0)))) b1 → ⊥
  bad1916  p = false≢true (cong lower p)
  cut1916 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 1) (op (var 0) (op (var 2) (var 0))))) , (var 2)) → ⊥
  cut1916  adequate = bad1916  (Adequate.valid adequate Two boolean env1)
  bad1917 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop b0 (bop b0 b0)))) b1 → ⊥
  bad1917  p = false≢true (cong lower p)
  cut1917 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 1) (op (var 0) (op (var 2) (var 0))))) , (var 3)) → ⊥
  cut1917  adequate = bad1917  (Adequate.valid adequate Two boolean env3)
  bad1918 : PathP (λ _ → Two) (bop (bop b0 b1) (bop b1 (bop b0 (bop b0 b1)))) b0 → ⊥
  bad1918  p = false≢true (sym (cong lower p))
  cut1918 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 1) (op (var 0) (op (var 2) (var 1))))) , (var 0)) → ⊥
  cut1918  adequate = bad1918  (Adequate.valid adequate Two boolean env2)
  holds1919 : (z0 z1 z2 : A3) → (mul3 (mul3 z0 z1) (mul3 z1 (mul3 z0 (mul3 z2 z1)))) ≡ z1
  holds1919 z0 z1 z2 = refl
  cut1919 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 1) (op (var 0) (op (var 2) (var 1))))) , (var 1)) → ⊥
  cut1919  = reject3 ((op (op (var 0) (var 1)) (op (var 1) (op (var 0) (op (var 2) (var 1))))) , (var 1)) (λ env → holds1919 (env 0) (env 1) (env 2))
  bad1920 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop b0 (bop b1 b0)))) b1 → ⊥
  bad1920  p = false≢true (cong lower p)
  cut1920 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 1) (op (var 0) (op (var 2) (var 1))))) , (var 2)) → ⊥
  cut1920  adequate = bad1920  (Adequate.valid adequate Two boolean env1)
  bad1921 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop b0 (bop b0 b0)))) b1 → ⊥
  bad1921  p = false≢true (cong lower p)
  cut1921 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 1) (op (var 0) (op (var 2) (var 1))))) , (var 3)) → ⊥
  cut1921  adequate = bad1921  (Adequate.valid adequate Two boolean env3)
  bad1922 : PathP (λ _ → Two) (bop (bop b0 b1) (bop b1 (bop b0 (bop b0 b0)))) b0 → ⊥
  bad1922  p = false≢true (sym (cong lower p))
  cut1922 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 1) (op (var 0) (op (var 2) (var 2))))) , (var 0)) → ⊥
  cut1922  adequate = bad1922  (Adequate.valid adequate Two boolean env2)
  holds1923 : (z0 z1 z2 : A8) → (mul8 (mul8 z0 z1) (mul8 z1 (mul8 z0 (mul8 z2 z2)))) ≡ z1
  holds1923 m8c0 m8c0 m8c0 = refl
  holds1923 m8c0 m8c0 m8c1 = refl
  holds1923 m8c0 m8c0 m8c2 = refl
  holds1923 m8c0 m8c1 m8c0 = refl
  holds1923 m8c0 m8c1 m8c1 = refl
  holds1923 m8c0 m8c1 m8c2 = refl
  holds1923 m8c0 m8c2 m8c0 = refl
  holds1923 m8c0 m8c2 m8c1 = refl
  holds1923 m8c0 m8c2 m8c2 = refl
  holds1923 m8c1 m8c0 m8c0 = refl
  holds1923 m8c1 m8c0 m8c1 = refl
  holds1923 m8c1 m8c0 m8c2 = refl
  holds1923 m8c1 m8c1 m8c0 = refl
  holds1923 m8c1 m8c1 m8c1 = refl
  holds1923 m8c1 m8c1 m8c2 = refl
  holds1923 m8c1 m8c2 m8c0 = refl
  holds1923 m8c1 m8c2 m8c1 = refl
  holds1923 m8c1 m8c2 m8c2 = refl
  holds1923 m8c2 m8c0 m8c0 = refl
  holds1923 m8c2 m8c0 m8c1 = refl
  holds1923 m8c2 m8c0 m8c2 = refl
  holds1923 m8c2 m8c1 m8c0 = refl
  holds1923 m8c2 m8c1 m8c1 = refl
  holds1923 m8c2 m8c1 m8c2 = refl
  holds1923 m8c2 m8c2 m8c0 = refl
  holds1923 m8c2 m8c2 m8c1 = refl
  holds1923 m8c2 m8c2 m8c2 = refl
  cut1923 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 1) (op (var 0) (op (var 2) (var 2))))) , (var 1)) → ⊥
  cut1923  = reject8 ((op (op (var 0) (var 1)) (op (var 1) (op (var 0) (op (var 2) (var 2))))) , (var 1)) (λ env → holds1923 (env 0) (env 1) (env 2))
  bad1924 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop b0 (bop b1 b1)))) b1 → ⊥
  bad1924  p = false≢true (cong lower p)
  cut1924 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 1) (op (var 0) (op (var 2) (var 2))))) , (var 2)) → ⊥
  cut1924  adequate = bad1924  (Adequate.valid adequate Two boolean env1)
  bad1925 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop b0 (bop b0 b0)))) b1 → ⊥
  bad1925  p = false≢true (cong lower p)
  cut1925 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 1) (op (var 0) (op (var 2) (var 2))))) , (var 3)) → ⊥
  cut1925  adequate = bad1925  (Adequate.valid adequate Two boolean env3)
  bad1926 : PathP (λ _ → Two) (bop (bop b0 b1) (bop b1 (bop b0 (bop b0 b0)))) b0 → ⊥
  bad1926  p = false≢true (sym (cong lower p))
  cut1926 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 1) (op (var 0) (op (var 2) (var 3))))) , (var 0)) → ⊥
  cut1926  adequate = bad1926  (Adequate.valid adequate Two boolean env4)
  holds1927 : (z0 z1 z2 z3 : A13) → (mul13 (mul13 z0 z1) (mul13 z1 (mul13 z0 (mul13 z2 z3)))) ≡ z1
  holds1927 m13c0 m13c0 m13c0 m13c0 = refl
  holds1927 m13c0 m13c0 m13c0 m13c1 = refl
  holds1927 m13c0 m13c0 m13c0 m13c2 = refl
  holds1927 m13c0 m13c0 m13c0 m13c3 = refl
  holds1927 m13c0 m13c0 m13c1 m13c0 = refl
  holds1927 m13c0 m13c0 m13c1 m13c1 = refl
  holds1927 m13c0 m13c0 m13c1 m13c2 = refl
  holds1927 m13c0 m13c0 m13c1 m13c3 = refl
  holds1927 m13c0 m13c0 m13c2 m13c0 = refl
  holds1927 m13c0 m13c0 m13c2 m13c1 = refl
  holds1927 m13c0 m13c0 m13c2 m13c2 = refl
  holds1927 m13c0 m13c0 m13c2 m13c3 = refl
  holds1927 m13c0 m13c0 m13c3 m13c0 = refl
  holds1927 m13c0 m13c0 m13c3 m13c1 = refl
  holds1927 m13c0 m13c0 m13c3 m13c2 = refl
  holds1927 m13c0 m13c0 m13c3 m13c3 = refl
  holds1927 m13c0 m13c1 m13c0 m13c0 = refl
  holds1927 m13c0 m13c1 m13c0 m13c1 = refl
  holds1927 m13c0 m13c1 m13c0 m13c2 = refl
  holds1927 m13c0 m13c1 m13c0 m13c3 = refl
  holds1927 m13c0 m13c1 m13c1 m13c0 = refl
  holds1927 m13c0 m13c1 m13c1 m13c1 = refl
  holds1927 m13c0 m13c1 m13c1 m13c2 = refl
  holds1927 m13c0 m13c1 m13c1 m13c3 = refl
  holds1927 m13c0 m13c1 m13c2 m13c0 = refl
  holds1927 m13c0 m13c1 m13c2 m13c1 = refl
  holds1927 m13c0 m13c1 m13c2 m13c2 = refl
  holds1927 m13c0 m13c1 m13c2 m13c3 = refl
  holds1927 m13c0 m13c1 m13c3 m13c0 = refl
  holds1927 m13c0 m13c1 m13c3 m13c1 = refl
  holds1927 m13c0 m13c1 m13c3 m13c2 = refl
  holds1927 m13c0 m13c1 m13c3 m13c3 = refl
  holds1927 m13c0 m13c2 m13c0 m13c0 = refl
  holds1927 m13c0 m13c2 m13c0 m13c1 = refl
  holds1927 m13c0 m13c2 m13c0 m13c2 = refl
  holds1927 m13c0 m13c2 m13c0 m13c3 = refl
  holds1927 m13c0 m13c2 m13c1 m13c0 = refl
  holds1927 m13c0 m13c2 m13c1 m13c1 = refl
  holds1927 m13c0 m13c2 m13c1 m13c2 = refl
  holds1927 m13c0 m13c2 m13c1 m13c3 = refl
  holds1927 m13c0 m13c2 m13c2 m13c0 = refl
  holds1927 m13c0 m13c2 m13c2 m13c1 = refl
  holds1927 m13c0 m13c2 m13c2 m13c2 = refl
  holds1927 m13c0 m13c2 m13c2 m13c3 = refl
  holds1927 m13c0 m13c2 m13c3 m13c0 = refl
  holds1927 m13c0 m13c2 m13c3 m13c1 = refl
  holds1927 m13c0 m13c2 m13c3 m13c2 = refl
  holds1927 m13c0 m13c2 m13c3 m13c3 = refl
  holds1927 m13c0 m13c3 m13c0 m13c0 = refl
  holds1927 m13c0 m13c3 m13c0 m13c1 = refl
  holds1927 m13c0 m13c3 m13c0 m13c2 = refl
  holds1927 m13c0 m13c3 m13c0 m13c3 = refl
  holds1927 m13c0 m13c3 m13c1 m13c0 = refl
  holds1927 m13c0 m13c3 m13c1 m13c1 = refl
  holds1927 m13c0 m13c3 m13c1 m13c2 = refl
  holds1927 m13c0 m13c3 m13c1 m13c3 = refl
  holds1927 m13c0 m13c3 m13c2 m13c0 = refl
  holds1927 m13c0 m13c3 m13c2 m13c1 = refl
  holds1927 m13c0 m13c3 m13c2 m13c2 = refl
  holds1927 m13c0 m13c3 m13c2 m13c3 = refl
  holds1927 m13c0 m13c3 m13c3 m13c0 = refl
  holds1927 m13c0 m13c3 m13c3 m13c1 = refl
  holds1927 m13c0 m13c3 m13c3 m13c2 = refl
  holds1927 m13c0 m13c3 m13c3 m13c3 = refl
  holds1927 m13c1 m13c0 m13c0 m13c0 = refl
  holds1927 m13c1 m13c0 m13c0 m13c1 = refl
  holds1927 m13c1 m13c0 m13c0 m13c2 = refl
  holds1927 m13c1 m13c0 m13c0 m13c3 = refl
  holds1927 m13c1 m13c0 m13c1 m13c0 = refl
  holds1927 m13c1 m13c0 m13c1 m13c1 = refl
  holds1927 m13c1 m13c0 m13c1 m13c2 = refl
  holds1927 m13c1 m13c0 m13c1 m13c3 = refl
  holds1927 m13c1 m13c0 m13c2 m13c0 = refl
  holds1927 m13c1 m13c0 m13c2 m13c1 = refl
  holds1927 m13c1 m13c0 m13c2 m13c2 = refl
  holds1927 m13c1 m13c0 m13c2 m13c3 = refl
  holds1927 m13c1 m13c0 m13c3 m13c0 = refl
  holds1927 m13c1 m13c0 m13c3 m13c1 = refl
  holds1927 m13c1 m13c0 m13c3 m13c2 = refl
  holds1927 m13c1 m13c0 m13c3 m13c3 = refl
  holds1927 m13c1 m13c1 m13c0 m13c0 = refl
  holds1927 m13c1 m13c1 m13c0 m13c1 = refl
  holds1927 m13c1 m13c1 m13c0 m13c2 = refl
  holds1927 m13c1 m13c1 m13c0 m13c3 = refl
  holds1927 m13c1 m13c1 m13c1 m13c0 = refl
  holds1927 m13c1 m13c1 m13c1 m13c1 = refl
  holds1927 m13c1 m13c1 m13c1 m13c2 = refl
  holds1927 m13c1 m13c1 m13c1 m13c3 = refl
  holds1927 m13c1 m13c1 m13c2 m13c0 = refl
  holds1927 m13c1 m13c1 m13c2 m13c1 = refl
  holds1927 m13c1 m13c1 m13c2 m13c2 = refl
  holds1927 m13c1 m13c1 m13c2 m13c3 = refl
  holds1927 m13c1 m13c1 m13c3 m13c0 = refl
  holds1927 m13c1 m13c1 m13c3 m13c1 = refl
  holds1927 m13c1 m13c1 m13c3 m13c2 = refl
  holds1927 m13c1 m13c1 m13c3 m13c3 = refl
  holds1927 m13c1 m13c2 m13c0 m13c0 = refl
  holds1927 m13c1 m13c2 m13c0 m13c1 = refl
  holds1927 m13c1 m13c2 m13c0 m13c2 = refl
  holds1927 m13c1 m13c2 m13c0 m13c3 = refl
  holds1927 m13c1 m13c2 m13c1 m13c0 = refl
  holds1927 m13c1 m13c2 m13c1 m13c1 = refl
  holds1927 m13c1 m13c2 m13c1 m13c2 = refl
  holds1927 m13c1 m13c2 m13c1 m13c3 = refl
  holds1927 m13c1 m13c2 m13c2 m13c0 = refl
  holds1927 m13c1 m13c2 m13c2 m13c1 = refl
  holds1927 m13c1 m13c2 m13c2 m13c2 = refl
  holds1927 m13c1 m13c2 m13c2 m13c3 = refl
  holds1927 m13c1 m13c2 m13c3 m13c0 = refl
  holds1927 m13c1 m13c2 m13c3 m13c1 = refl
  holds1927 m13c1 m13c2 m13c3 m13c2 = refl
  holds1927 m13c1 m13c2 m13c3 m13c3 = refl
  holds1927 m13c1 m13c3 m13c0 m13c0 = refl
  holds1927 m13c1 m13c3 m13c0 m13c1 = refl
  holds1927 m13c1 m13c3 m13c0 m13c2 = refl
  holds1927 m13c1 m13c3 m13c0 m13c3 = refl
  holds1927 m13c1 m13c3 m13c1 m13c0 = refl
  holds1927 m13c1 m13c3 m13c1 m13c1 = refl
  holds1927 m13c1 m13c3 m13c1 m13c2 = refl
  holds1927 m13c1 m13c3 m13c1 m13c3 = refl
  holds1927 m13c1 m13c3 m13c2 m13c0 = refl
  holds1927 m13c1 m13c3 m13c2 m13c1 = refl
  holds1927 m13c1 m13c3 m13c2 m13c2 = refl
  holds1927 m13c1 m13c3 m13c2 m13c3 = refl
  holds1927 m13c1 m13c3 m13c3 m13c0 = refl
  holds1927 m13c1 m13c3 m13c3 m13c1 = refl
  holds1927 m13c1 m13c3 m13c3 m13c2 = refl
  holds1927 m13c1 m13c3 m13c3 m13c3 = refl
  holds1927 m13c2 m13c0 m13c0 m13c0 = refl
  holds1927 m13c2 m13c0 m13c0 m13c1 = refl
  holds1927 m13c2 m13c0 m13c0 m13c2 = refl
  holds1927 m13c2 m13c0 m13c0 m13c3 = refl
  holds1927 m13c2 m13c0 m13c1 m13c0 = refl
  holds1927 m13c2 m13c0 m13c1 m13c1 = refl
  holds1927 m13c2 m13c0 m13c1 m13c2 = refl
  holds1927 m13c2 m13c0 m13c1 m13c3 = refl
  holds1927 m13c2 m13c0 m13c2 m13c0 = refl
  holds1927 m13c2 m13c0 m13c2 m13c1 = refl
  holds1927 m13c2 m13c0 m13c2 m13c2 = refl
  holds1927 m13c2 m13c0 m13c2 m13c3 = refl
  holds1927 m13c2 m13c0 m13c3 m13c0 = refl
  holds1927 m13c2 m13c0 m13c3 m13c1 = refl
  holds1927 m13c2 m13c0 m13c3 m13c2 = refl
  holds1927 m13c2 m13c0 m13c3 m13c3 = refl
  holds1927 m13c2 m13c1 m13c0 m13c0 = refl
  holds1927 m13c2 m13c1 m13c0 m13c1 = refl
  holds1927 m13c2 m13c1 m13c0 m13c2 = refl
  holds1927 m13c2 m13c1 m13c0 m13c3 = refl
  holds1927 m13c2 m13c1 m13c1 m13c0 = refl
  holds1927 m13c2 m13c1 m13c1 m13c1 = refl
  holds1927 m13c2 m13c1 m13c1 m13c2 = refl
  holds1927 m13c2 m13c1 m13c1 m13c3 = refl
  holds1927 m13c2 m13c1 m13c2 m13c0 = refl
  holds1927 m13c2 m13c1 m13c2 m13c1 = refl
  holds1927 m13c2 m13c1 m13c2 m13c2 = refl
  holds1927 m13c2 m13c1 m13c2 m13c3 = refl
  holds1927 m13c2 m13c1 m13c3 m13c0 = refl
  holds1927 m13c2 m13c1 m13c3 m13c1 = refl
  holds1927 m13c2 m13c1 m13c3 m13c2 = refl
  holds1927 m13c2 m13c1 m13c3 m13c3 = refl
  holds1927 m13c2 m13c2 m13c0 m13c0 = refl
  holds1927 m13c2 m13c2 m13c0 m13c1 = refl
  holds1927 m13c2 m13c2 m13c0 m13c2 = refl
  holds1927 m13c2 m13c2 m13c0 m13c3 = refl
  holds1927 m13c2 m13c2 m13c1 m13c0 = refl
  holds1927 m13c2 m13c2 m13c1 m13c1 = refl
  holds1927 m13c2 m13c2 m13c1 m13c2 = refl
  holds1927 m13c2 m13c2 m13c1 m13c3 = refl
  holds1927 m13c2 m13c2 m13c2 m13c0 = refl
  holds1927 m13c2 m13c2 m13c2 m13c1 = refl
  holds1927 m13c2 m13c2 m13c2 m13c2 = refl
  holds1927 m13c2 m13c2 m13c2 m13c3 = refl
  holds1927 m13c2 m13c2 m13c3 m13c0 = refl
  holds1927 m13c2 m13c2 m13c3 m13c1 = refl
  holds1927 m13c2 m13c2 m13c3 m13c2 = refl
  holds1927 m13c2 m13c2 m13c3 m13c3 = refl
  holds1927 m13c2 m13c3 m13c0 m13c0 = refl
  holds1927 m13c2 m13c3 m13c0 m13c1 = refl
  holds1927 m13c2 m13c3 m13c0 m13c2 = refl
  holds1927 m13c2 m13c3 m13c0 m13c3 = refl
  holds1927 m13c2 m13c3 m13c1 m13c0 = refl
  holds1927 m13c2 m13c3 m13c1 m13c1 = refl
  holds1927 m13c2 m13c3 m13c1 m13c2 = refl
  holds1927 m13c2 m13c3 m13c1 m13c3 = refl
  holds1927 m13c2 m13c3 m13c2 m13c0 = refl
  holds1927 m13c2 m13c3 m13c2 m13c1 = refl
  holds1927 m13c2 m13c3 m13c2 m13c2 = refl
  holds1927 m13c2 m13c3 m13c2 m13c3 = refl
  holds1927 m13c2 m13c3 m13c3 m13c0 = refl
  holds1927 m13c2 m13c3 m13c3 m13c1 = refl
  holds1927 m13c2 m13c3 m13c3 m13c2 = refl
  holds1927 m13c2 m13c3 m13c3 m13c3 = refl
  holds1927 m13c3 m13c0 m13c0 m13c0 = refl
  holds1927 m13c3 m13c0 m13c0 m13c1 = refl
  holds1927 m13c3 m13c0 m13c0 m13c2 = refl
  holds1927 m13c3 m13c0 m13c0 m13c3 = refl
  holds1927 m13c3 m13c0 m13c1 m13c0 = refl
  holds1927 m13c3 m13c0 m13c1 m13c1 = refl
  holds1927 m13c3 m13c0 m13c1 m13c2 = refl
  holds1927 m13c3 m13c0 m13c1 m13c3 = refl
  holds1927 m13c3 m13c0 m13c2 m13c0 = refl
  holds1927 m13c3 m13c0 m13c2 m13c1 = refl
  holds1927 m13c3 m13c0 m13c2 m13c2 = refl
  holds1927 m13c3 m13c0 m13c2 m13c3 = refl
  holds1927 m13c3 m13c0 m13c3 m13c0 = refl
  holds1927 m13c3 m13c0 m13c3 m13c1 = refl
  holds1927 m13c3 m13c0 m13c3 m13c2 = refl
  holds1927 m13c3 m13c0 m13c3 m13c3 = refl
  holds1927 m13c3 m13c1 m13c0 m13c0 = refl
  holds1927 m13c3 m13c1 m13c0 m13c1 = refl
  holds1927 m13c3 m13c1 m13c0 m13c2 = refl
  holds1927 m13c3 m13c1 m13c0 m13c3 = refl
  holds1927 m13c3 m13c1 m13c1 m13c0 = refl
  holds1927 m13c3 m13c1 m13c1 m13c1 = refl
  holds1927 m13c3 m13c1 m13c1 m13c2 = refl
  holds1927 m13c3 m13c1 m13c1 m13c3 = refl
  holds1927 m13c3 m13c1 m13c2 m13c0 = refl
  holds1927 m13c3 m13c1 m13c2 m13c1 = refl
  holds1927 m13c3 m13c1 m13c2 m13c2 = refl
  holds1927 m13c3 m13c1 m13c2 m13c3 = refl
  holds1927 m13c3 m13c1 m13c3 m13c0 = refl
  holds1927 m13c3 m13c1 m13c3 m13c1 = refl
  holds1927 m13c3 m13c1 m13c3 m13c2 = refl
  holds1927 m13c3 m13c1 m13c3 m13c3 = refl
  holds1927 m13c3 m13c2 m13c0 m13c0 = refl
  holds1927 m13c3 m13c2 m13c0 m13c1 = refl
  holds1927 m13c3 m13c2 m13c0 m13c2 = refl
  holds1927 m13c3 m13c2 m13c0 m13c3 = refl
  holds1927 m13c3 m13c2 m13c1 m13c0 = refl
  holds1927 m13c3 m13c2 m13c1 m13c1 = refl
  holds1927 m13c3 m13c2 m13c1 m13c2 = refl
  holds1927 m13c3 m13c2 m13c1 m13c3 = refl
  holds1927 m13c3 m13c2 m13c2 m13c0 = refl
  holds1927 m13c3 m13c2 m13c2 m13c1 = refl
  holds1927 m13c3 m13c2 m13c2 m13c2 = refl
  holds1927 m13c3 m13c2 m13c2 m13c3 = refl
  holds1927 m13c3 m13c2 m13c3 m13c0 = refl
  holds1927 m13c3 m13c2 m13c3 m13c1 = refl
  holds1927 m13c3 m13c2 m13c3 m13c2 = refl
  holds1927 m13c3 m13c2 m13c3 m13c3 = refl
  holds1927 m13c3 m13c3 m13c0 m13c0 = refl
  holds1927 m13c3 m13c3 m13c0 m13c1 = refl
  holds1927 m13c3 m13c3 m13c0 m13c2 = refl
  holds1927 m13c3 m13c3 m13c0 m13c3 = refl
  holds1927 m13c3 m13c3 m13c1 m13c0 = refl
  holds1927 m13c3 m13c3 m13c1 m13c1 = refl
  holds1927 m13c3 m13c3 m13c1 m13c2 = refl
  holds1927 m13c3 m13c3 m13c1 m13c3 = refl
  holds1927 m13c3 m13c3 m13c2 m13c0 = refl
  holds1927 m13c3 m13c3 m13c2 m13c1 = refl
  holds1927 m13c3 m13c3 m13c2 m13c2 = refl
  holds1927 m13c3 m13c3 m13c2 m13c3 = refl
  holds1927 m13c3 m13c3 m13c3 m13c0 = refl
  holds1927 m13c3 m13c3 m13c3 m13c1 = refl
  holds1927 m13c3 m13c3 m13c3 m13c2 = refl
  holds1927 m13c3 m13c3 m13c3 m13c3 = refl
  cut1927 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 1) (op (var 0) (op (var 2) (var 3))))) , (var 1)) → ⊥
  cut1927  = reject13 ((op (op (var 0) (var 1)) (op (var 1) (op (var 0) (op (var 2) (var 3))))) , (var 1)) (λ env → holds1927 (env 0) (env 1) (env 2) (env 3))
  bad1928 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop b0 (bop b1 b0)))) b1 → ⊥
  bad1928  p = false≢true (cong lower p)
  cut1928 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 1) (op (var 0) (op (var 2) (var 3))))) , (var 2)) → ⊥
  cut1928  adequate = bad1928  (Adequate.valid adequate Two boolean env5)
  bad1929 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop b0 (bop b0 b1)))) b1 → ⊥
  bad1929  p = false≢true (cong lower p)
  cut1929 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 1) (op (var 0) (op (var 2) (var 3))))) , (var 3)) → ⊥
  cut1929  adequate = bad1929  (Adequate.valid adequate Two boolean env3)
  bad1930 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop b0 (bop b0 b0)))) b1 → ⊥
  bad1930  p = false≢true (cong lower p)
  cut1930 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 1) (op (var 0) (op (var 2) (var 3))))) , (var 4)) → ⊥
  cut1930  adequate = bad1930  (Adequate.valid adequate Two boolean env6)
  bad1931 : PathP (λ _ → Two) (bop (bop b1 b0) (bop b0 (bop b0 (bop b1 b1)))) b1 → ⊥
  bad1931  p = false≢true (cong lower p)
  cut1931 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 1) (op (var 1) (op (var 0) (var 0))))) , (var 0)) → ⊥
  cut1931  adequate = bad1931  (Adequate.valid adequate Two boolean env7)
  bad1932 : PathP (λ _ → Two) (bop (bop b0 b1) (bop b1 (bop b1 (bop b0 b0)))) b1 → ⊥
  bad1932  p = false≢true (cong lower p)
  cut1932 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 1) (op (var 1) (op (var 0) (var 0))))) , (var 1)) → ⊥
  cut1932  adequate = bad1932  (Adequate.valid adequate Two boolean env0)
  bad1933 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop b0 (bop b0 b0)))) b1 → ⊥
  bad1933  p = false≢true (cong lower p)
  cut1933 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 1) (op (var 1) (op (var 0) (var 0))))) , (var 2)) → ⊥
  cut1933  adequate = bad1933  (Adequate.valid adequate Two boolean env1)
  bad1934 : PathP (λ _ → Two) (bop (bop b1 b0) (bop b0 (bop b0 (bop b1 b0)))) b1 → ⊥
  bad1934  p = false≢true (cong lower p)
  cut1934 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 1) (op (var 1) (op (var 0) (var 1))))) , (var 0)) → ⊥
  cut1934  adequate = bad1934  (Adequate.valid adequate Two boolean env7)
  bad1935 : PathP (λ _ → Two) (bop (bop b0 b1) (bop b1 (bop b1 (bop b0 b1)))) b1 → ⊥
  bad1935  p = false≢true (cong lower p)
  cut1935 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 1) (op (var 1) (op (var 0) (var 1))))) , (var 1)) → ⊥
  cut1935  adequate = bad1935  (Adequate.valid adequate Two boolean env0)
  bad1936 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop b0 (bop b0 b0)))) b1 → ⊥
  bad1936  p = false≢true (cong lower p)
  cut1936 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 1) (op (var 1) (op (var 0) (var 1))))) , (var 2)) → ⊥
  cut1936  adequate = bad1936  (Adequate.valid adequate Two boolean env1)
  bad1937 : PathP (λ _ → Two) (bop (bop b1 b0) (bop b0 (bop b0 (bop b1 b0)))) b1 → ⊥
  bad1937  p = false≢true (cong lower p)
  cut1937 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 1) (op (var 1) (op (var 0) (var 2))))) , (var 0)) → ⊥
  cut1937  adequate = bad1937  (Adequate.valid adequate Two boolean env8)
  bad1938 : PathP (λ _ → Two) (bop (bop b0 b1) (bop b1 (bop b1 (bop b0 b0)))) b1 → ⊥
  bad1938  p = false≢true (cong lower p)
  cut1938 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 1) (op (var 1) (op (var 0) (var 2))))) , (var 1)) → ⊥
  cut1938  adequate = bad1938  (Adequate.valid adequate Two boolean env2)
  bad1939 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop b0 (bop b0 b1)))) b1 → ⊥
  bad1939  p = false≢true (cong lower p)
  cut1939 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 1) (op (var 1) (op (var 0) (var 2))))) , (var 2)) → ⊥
  cut1939  adequate = bad1939  (Adequate.valid adequate Two boolean env1)
  bad1940 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop b0 (bop b0 b0)))) b1 → ⊥
  bad1940  p = false≢true (cong lower p)
  cut1940 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 1) (op (var 1) (op (var 0) (var 2))))) , (var 3)) → ⊥
  cut1940  adequate = bad1940  (Adequate.valid adequate Two boolean env3)
  bad1941 : PathP (λ _ → Two) (bop (bop b1 b0) (bop b0 (bop b0 (bop b0 b1)))) b1 → ⊥
  bad1941  p = false≢true (cong lower p)
  cut1941 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 1) (op (var 1) (op (var 1) (var 0))))) , (var 0)) → ⊥
  cut1941  adequate = bad1941  (Adequate.valid adequate Two boolean env7)
  bad1942 : PathP (λ _ → Two) (bop (bop b0 b1) (bop b1 (bop b1 (bop b1 b0)))) b1 → ⊥
  bad1942  p = false≢true (cong lower p)
  cut1942 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 1) (op (var 1) (op (var 1) (var 0))))) , (var 1)) → ⊥
  cut1942  adequate = bad1942  (Adequate.valid adequate Two boolean env0)
  bad1943 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop b0 (bop b0 b0)))) b1 → ⊥
  bad1943  p = false≢true (cong lower p)
  cut1943 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 1) (op (var 1) (op (var 1) (var 0))))) , (var 2)) → ⊥
  cut1943  adequate = bad1943  (Adequate.valid adequate Two boolean env1)
  bad1944 : PathP (λ _ → Two) (bop (bop b0 b1) (bop b1 (bop b1 (bop b1 b1)))) b0 → ⊥
  bad1944  p = false≢true (sym (cong lower p))
  cut1944 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 1) (op (var 1) (op (var 1) (var 1))))) , (var 0)) → ⊥
  cut1944  adequate = bad1944  (Adequate.valid adequate Two boolean env0)
  holds1945 : (z0 z1 : A3) → (mul3 (mul3 z0 z1) (mul3 z1 (mul3 z1 (mul3 z1 z1)))) ≡ z1
  holds1945 z0 z1 = refl
  cut1945 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 1) (op (var 1) (op (var 1) (var 1))))) , (var 1)) → ⊥
  cut1945  = reject3 ((op (op (var 0) (var 1)) (op (var 1) (op (var 1) (op (var 1) (var 1))))) , (var 1)) (λ env → holds1945 (env 0) (env 1))
  bad1946 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop b0 (bop b0 b0)))) b1 → ⊥
  bad1946  p = false≢true (cong lower p)
  cut1946 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 1) (op (var 1) (op (var 1) (var 1))))) , (var 2)) → ⊥
  cut1946  adequate = bad1946  (Adequate.valid adequate Two boolean env1)
  bad1947 : PathP (λ _ → Two) (bop (bop b0 b1) (bop b1 (bop b1 (bop b1 b1)))) b0 → ⊥
  bad1947  p = false≢true (sym (cong lower p))
  cut1947 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 1) (op (var 1) (op (var 1) (var 2))))) , (var 0)) → ⊥
  cut1947  adequate = bad1947  (Adequate.valid adequate Two boolean env10)
  bad1948 : PathP (λ _ → Two) (bop (bop b0 b1) (bop b1 (bop b1 (bop b1 b0)))) b1 → ⊥
  bad1948  p = false≢true (cong lower p)
  cut1948 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 1) (op (var 1) (op (var 1) (var 2))))) , (var 1)) → ⊥
  cut1948  adequate = bad1948  (Adequate.valid adequate Two boolean env2)
  bad1949 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop b0 (bop b0 b1)))) b1 → ⊥
  bad1949  p = false≢true (cong lower p)
  cut1949 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 1) (op (var 1) (op (var 1) (var 2))))) , (var 2)) → ⊥
  cut1949  adequate = bad1949  (Adequate.valid adequate Two boolean env1)
  bad1950 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop b0 (bop b0 b0)))) b1 → ⊥
  bad1950  p = false≢true (cong lower p)
  cut1950 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 1) (op (var 1) (op (var 1) (var 2))))) , (var 3)) → ⊥
  cut1950  adequate = bad1950  (Adequate.valid adequate Two boolean env3)
  bad1951 : PathP (λ _ → Two) (bop (bop b1 b0) (bop b0 (bop b0 (bop b0 b1)))) b1 → ⊥
  bad1951  p = false≢true (cong lower p)
  cut1951 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 1) (op (var 1) (op (var 2) (var 0))))) , (var 0)) → ⊥
  cut1951  adequate = bad1951  (Adequate.valid adequate Two boolean env8)
  bad1952 : PathP (λ _ → Two) (bop (bop b0 b1) (bop b1 (bop b1 (bop b0 b0)))) b1 → ⊥
  bad1952  p = false≢true (cong lower p)
  cut1952 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 1) (op (var 1) (op (var 2) (var 0))))) , (var 1)) → ⊥
  cut1952  adequate = bad1952  (Adequate.valid adequate Two boolean env2)
  bad1953 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop b0 (bop b1 b0)))) b1 → ⊥
  bad1953  p = false≢true (cong lower p)
  cut1953 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 1) (op (var 1) (op (var 2) (var 0))))) , (var 2)) → ⊥
  cut1953  adequate = bad1953  (Adequate.valid adequate Two boolean env1)
  bad1954 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop b0 (bop b0 b0)))) b1 → ⊥
  bad1954  p = false≢true (cong lower p)
  cut1954 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 1) (op (var 1) (op (var 2) (var 0))))) , (var 3)) → ⊥
  cut1954  adequate = bad1954  (Adequate.valid adequate Two boolean env3)
  bad1955 : PathP (λ _ → Two) (bop (bop b0 b1) (bop b1 (bop b1 (bop b1 b1)))) b0 → ⊥
  bad1955  p = false≢true (sym (cong lower p))
  cut1955 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 1) (op (var 1) (op (var 2) (var 1))))) , (var 0)) → ⊥
  cut1955  adequate = bad1955  (Adequate.valid adequate Two boolean env10)
  bad1956 : PathP (λ _ → Two) (bop (bop b0 b1) (bop b1 (bop b1 (bop b0 b1)))) b1 → ⊥
  bad1956  p = false≢true (cong lower p)
  cut1956 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 1) (op (var 1) (op (var 2) (var 1))))) , (var 1)) → ⊥
  cut1956  adequate = bad1956  (Adequate.valid adequate Two boolean env2)
  bad1957 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop b0 (bop b1 b0)))) b1 → ⊥
  bad1957  p = false≢true (cong lower p)
  cut1957 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 1) (op (var 1) (op (var 2) (var 1))))) , (var 2)) → ⊥
  cut1957  adequate = bad1957  (Adequate.valid adequate Two boolean env1)
  bad1958 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop b0 (bop b0 b0)))) b1 → ⊥
  bad1958  p = false≢true (cong lower p)
  cut1958 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 1) (op (var 1) (op (var 2) (var 1))))) , (var 3)) → ⊥
  cut1958  adequate = bad1958  (Adequate.valid adequate Two boolean env3)
  bad1959 : PathP (λ _ → Two) (bop (bop b0 b1) (bop b1 (bop b1 (bop b1 b1)))) b0 → ⊥
  bad1959  p = false≢true (sym (cong lower p))
  cut1959 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 1) (op (var 1) (op (var 2) (var 2))))) , (var 0)) → ⊥
  cut1959  adequate = bad1959  (Adequate.valid adequate Two boolean env10)
  bad1960 : PathP (λ _ → Two) (bop (bop b0 b1) (bop b1 (bop b1 (bop b0 b0)))) b1 → ⊥
  bad1960  p = false≢true (cong lower p)
  cut1960 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 1) (op (var 1) (op (var 2) (var 2))))) , (var 1)) → ⊥
  cut1960  adequate = bad1960  (Adequate.valid adequate Two boolean env2)
  bad1961 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop b0 (bop b1 b1)))) b1 → ⊥
  bad1961  p = false≢true (cong lower p)
  cut1961 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 1) (op (var 1) (op (var 2) (var 2))))) , (var 2)) → ⊥
  cut1961  adequate = bad1961  (Adequate.valid adequate Two boolean env1)
  bad1962 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop b0 (bop b0 b0)))) b1 → ⊥
  bad1962  p = false≢true (cong lower p)
  cut1962 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 1) (op (var 1) (op (var 2) (var 2))))) , (var 3)) → ⊥
  cut1962  adequate = bad1962  (Adequate.valid adequate Two boolean env3)
  bad1963 : PathP (λ _ → Two) (bop (bop b0 b1) (bop b1 (bop b1 (bop b1 b1)))) b0 → ⊥
  bad1963  p = false≢true (sym (cong lower p))
  cut1963 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 1) (op (var 1) (op (var 2) (var 3))))) , (var 0)) → ⊥
  cut1963  adequate = bad1963  (Adequate.valid adequate Two boolean env11)
  bad1964 : PathP (λ _ → Two) (bop (bop b0 b1) (bop b1 (bop b1 (bop b0 b0)))) b1 → ⊥
  bad1964  p = false≢true (cong lower p)
  cut1964 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 1) (op (var 1) (op (var 2) (var 3))))) , (var 1)) → ⊥
  cut1964  adequate = bad1964  (Adequate.valid adequate Two boolean env4)
  bad1965 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop b0 (bop b1 b0)))) b1 → ⊥
  bad1965  p = false≢true (cong lower p)
  cut1965 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 1) (op (var 1) (op (var 2) (var 3))))) , (var 2)) → ⊥
  cut1965  adequate = bad1965  (Adequate.valid adequate Two boolean env5)
  bad1966 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop b0 (bop b0 b1)))) b1 → ⊥
  bad1966  p = false≢true (cong lower p)
  cut1966 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 1) (op (var 1) (op (var 2) (var 3))))) , (var 3)) → ⊥
  cut1966  adequate = bad1966  (Adequate.valid adequate Two boolean env3)
  bad1967 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop b0 (bop b0 b0)))) b1 → ⊥
  bad1967  p = false≢true (cong lower p)
  cut1967 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 1) (op (var 1) (op (var 2) (var 3))))) , (var 4)) → ⊥
  cut1967  adequate = bad1967  (Adequate.valid adequate Two boolean env6)
  bad1968 : PathP (λ _ → Two) (bop (bop b0 b1) (bop b1 (bop b0 (bop b0 b0)))) b0 → ⊥
  bad1968  p = false≢true (sym (cong lower p))
  cut1968 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 1) (op (var 2) (op (var 0) (var 0))))) , (var 0)) → ⊥
  cut1968  adequate = bad1968  (Adequate.valid adequate Two boolean env2)
  bad1969 : PathP (λ _ → Two) (bop (bop b0 b1) (bop b1 (bop b1 (bop b0 b0)))) b1 → ⊥
  bad1969  p = false≢true (cong lower p)
  cut1969 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 1) (op (var 2) (op (var 0) (var 0))))) , (var 1)) → ⊥
  cut1969  adequate = bad1969  (Adequate.valid adequate Two boolean env10)
  bad1970 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop b1 (bop b0 b0)))) b1 → ⊥
  bad1970  p = false≢true (cong lower p)
  cut1970 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 1) (op (var 2) (op (var 0) (var 0))))) , (var 2)) → ⊥
  cut1970  adequate = bad1970  (Adequate.valid adequate Two boolean env1)
  bad1971 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop b0 (bop b0 b0)))) b1 → ⊥
  bad1971  p = false≢true (cong lower p)
  cut1971 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 1) (op (var 2) (op (var 0) (var 0))))) , (var 3)) → ⊥
  cut1971  adequate = bad1971  (Adequate.valid adequate Two boolean env3)
  bad1972 : PathP (λ _ → Two) (bop (bop b0 b1) (bop b1 (bop b0 (bop b0 b1)))) b0 → ⊥
  bad1972  p = false≢true (sym (cong lower p))
  cut1972 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 1) (op (var 2) (op (var 0) (var 1))))) , (var 0)) → ⊥
  cut1972  adequate = bad1972  (Adequate.valid adequate Two boolean env2)
  bad1973 : PathP (λ _ → Two) (bop (bop b0 b1) (bop b1 (bop b1 (bop b0 b1)))) b1 → ⊥
  bad1973  p = false≢true (cong lower p)
  cut1973 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 1) (op (var 2) (op (var 0) (var 1))))) , (var 1)) → ⊥
  cut1973  adequate = bad1973  (Adequate.valid adequate Two boolean env10)
  bad1974 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop b1 (bop b0 b0)))) b1 → ⊥
  bad1974  p = false≢true (cong lower p)
  cut1974 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 1) (op (var 2) (op (var 0) (var 1))))) , (var 2)) → ⊥
  cut1974  adequate = bad1974  (Adequate.valid adequate Two boolean env1)
  bad1975 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop b0 (bop b0 b0)))) b1 → ⊥
  bad1975  p = false≢true (cong lower p)
  cut1975 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 1) (op (var 2) (op (var 0) (var 1))))) , (var 3)) → ⊥
  cut1975  adequate = bad1975  (Adequate.valid adequate Two boolean env3)
  bad1976 : PathP (λ _ → Two) (bop (bop b0 b1) (bop b1 (bop b0 (bop b0 b0)))) b0 → ⊥
  bad1976  p = false≢true (sym (cong lower p))
  cut1976 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 1) (op (var 2) (op (var 0) (var 2))))) , (var 0)) → ⊥
  cut1976  adequate = bad1976  (Adequate.valid adequate Two boolean env2)
  bad1977 : PathP (λ _ → Two) (bop (bop b0 b1) (bop b1 (bop b1 (bop b0 b1)))) b1 → ⊥
  bad1977  p = false≢true (cong lower p)
  cut1977 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 1) (op (var 2) (op (var 0) (var 2))))) , (var 1)) → ⊥
  cut1977  adequate = bad1977  (Adequate.valid adequate Two boolean env10)
  bad1978 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop b1 (bop b0 b1)))) b1 → ⊥
  bad1978  p = false≢true (cong lower p)
  cut1978 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 1) (op (var 2) (op (var 0) (var 2))))) , (var 2)) → ⊥
  cut1978  adequate = bad1978  (Adequate.valid adequate Two boolean env1)
  bad1979 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop b0 (bop b0 b0)))) b1 → ⊥
  bad1979  p = false≢true (cong lower p)
  cut1979 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 1) (op (var 2) (op (var 0) (var 2))))) , (var 3)) → ⊥
  cut1979  adequate = bad1979  (Adequate.valid adequate Two boolean env3)
  bad1980 : PathP (λ _ → Two) (bop (bop b0 b1) (bop b1 (bop b0 (bop b0 b0)))) b0 → ⊥
  bad1980  p = false≢true (sym (cong lower p))
  cut1980 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 1) (op (var 2) (op (var 0) (var 3))))) , (var 0)) → ⊥
  cut1980  adequate = bad1980  (Adequate.valid adequate Two boolean env4)
  bad1981 : PathP (λ _ → Two) (bop (bop b0 b1) (bop b1 (bop b1 (bop b0 b0)))) b1 → ⊥
  bad1981  p = false≢true (cong lower p)
  cut1981 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 1) (op (var 2) (op (var 0) (var 3))))) , (var 1)) → ⊥
  cut1981  adequate = bad1981  (Adequate.valid adequate Two boolean env12)
  bad1982 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop b1 (bop b0 b0)))) b1 → ⊥
  bad1982  p = false≢true (cong lower p)
  cut1982 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 1) (op (var 2) (op (var 0) (var 3))))) , (var 2)) → ⊥
  cut1982  adequate = bad1982  (Adequate.valid adequate Two boolean env5)
  bad1983 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop b0 (bop b0 b1)))) b1 → ⊥
  bad1983  p = false≢true (cong lower p)
  cut1983 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 1) (op (var 2) (op (var 0) (var 3))))) , (var 3)) → ⊥
  cut1983  adequate = bad1983  (Adequate.valid adequate Two boolean env3)
  bad1984 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop b0 (bop b0 b0)))) b1 → ⊥
  bad1984  p = false≢true (cong lower p)
  cut1984 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 1) (op (var 2) (op (var 0) (var 3))))) , (var 4)) → ⊥
  cut1984  adequate = bad1984  (Adequate.valid adequate Two boolean env6)
  bad1985 : PathP (λ _ → Two) (bop (bop b0 b1) (bop b1 (bop b0 (bop b1 b0)))) b0 → ⊥
  bad1985  p = false≢true (sym (cong lower p))
  cut1985 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 1) (op (var 2) (op (var 1) (var 0))))) , (var 0)) → ⊥
  cut1985  adequate = bad1985  (Adequate.valid adequate Two boolean env2)
  bad1986 : PathP (λ _ → Two) (bop (bop b0 b1) (bop b1 (bop b1 (bop b1 b0)))) b1 → ⊥
  bad1986  p = false≢true (cong lower p)
  cut1986 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 1) (op (var 2) (op (var 1) (var 0))))) , (var 1)) → ⊥
  cut1986  adequate = bad1986  (Adequate.valid adequate Two boolean env10)
  bad1987 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop b1 (bop b0 b0)))) b1 → ⊥
  bad1987  p = false≢true (cong lower p)
  cut1987 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 1) (op (var 2) (op (var 1) (var 0))))) , (var 2)) → ⊥
  cut1987  adequate = bad1987  (Adequate.valid adequate Two boolean env1)
  bad1988 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop b0 (bop b0 b0)))) b1 → ⊥
  bad1988  p = false≢true (cong lower p)
  cut1988 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 1) (op (var 2) (op (var 1) (var 0))))) , (var 3)) → ⊥
  cut1988  adequate = bad1988  (Adequate.valid adequate Two boolean env3)
  bad1989 : PathP (λ _ → Two) (bop (bop b0 b1) (bop b1 (bop b0 (bop b1 b1)))) b0 → ⊥
  bad1989  p = false≢true (sym (cong lower p))
  cut1989 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 1) (op (var 2) (op (var 1) (var 1))))) , (var 0)) → ⊥
  cut1989  adequate = bad1989  (Adequate.valid adequate Two boolean env2)
  holds1990 : (z0 z1 z2 : A3) → (mul3 (mul3 z0 z1) (mul3 z1 (mul3 z2 (mul3 z1 z1)))) ≡ z1
  holds1990 z0 z1 z2 = refl
  cut1990 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 1) (op (var 2) (op (var 1) (var 1))))) , (var 1)) → ⊥
  cut1990  = reject3 ((op (op (var 0) (var 1)) (op (var 1) (op (var 2) (op (var 1) (var 1))))) , (var 1)) (λ env → holds1990 (env 0) (env 1) (env 2))
  bad1991 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop b1 (bop b0 b0)))) b1 → ⊥
  bad1991  p = false≢true (cong lower p)
  cut1991 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 1) (op (var 2) (op (var 1) (var 1))))) , (var 2)) → ⊥
  cut1991  adequate = bad1991  (Adequate.valid adequate Two boolean env1)
  bad1992 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop b0 (bop b0 b0)))) b1 → ⊥
  bad1992  p = false≢true (cong lower p)
  cut1992 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 1) (op (var 2) (op (var 1) (var 1))))) , (var 3)) → ⊥
  cut1992  adequate = bad1992  (Adequate.valid adequate Two boolean env3)
  bad1993 : PathP (λ _ → Two) (bop (bop b0 b1) (bop b1 (bop b0 (bop b1 b0)))) b0 → ⊥
  bad1993  p = false≢true (sym (cong lower p))
  cut1993 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 1) (op (var 2) (op (var 1) (var 2))))) , (var 0)) → ⊥
  cut1993  adequate = bad1993  (Adequate.valid adequate Two boolean env2)
  holds1994 : (z0 z1 z2 : A6) → (mul6 (mul6 z0 z1) (mul6 z1 (mul6 z2 (mul6 z1 z2)))) ≡ z1
  holds1994 m6c0 m6c0 m6c0 = refl
  holds1994 m6c0 m6c0 m6c1 = refl
  holds1994 m6c0 m6c0 m6c2 = refl
  holds1994 m6c0 m6c1 m6c0 = refl
  holds1994 m6c0 m6c1 m6c1 = refl
  holds1994 m6c0 m6c1 m6c2 = refl
  holds1994 m6c0 m6c2 m6c0 = refl
  holds1994 m6c0 m6c2 m6c1 = refl
  holds1994 m6c0 m6c2 m6c2 = refl
  holds1994 m6c1 m6c0 m6c0 = refl
  holds1994 m6c1 m6c0 m6c1 = refl
  holds1994 m6c1 m6c0 m6c2 = refl
  holds1994 m6c1 m6c1 m6c0 = refl
  holds1994 m6c1 m6c1 m6c1 = refl
  holds1994 m6c1 m6c1 m6c2 = refl
  holds1994 m6c1 m6c2 m6c0 = refl
  holds1994 m6c1 m6c2 m6c1 = refl
  holds1994 m6c1 m6c2 m6c2 = refl
  holds1994 m6c2 m6c0 m6c0 = refl
  holds1994 m6c2 m6c0 m6c1 = refl
  holds1994 m6c2 m6c0 m6c2 = refl
  holds1994 m6c2 m6c1 m6c0 = refl
  holds1994 m6c2 m6c1 m6c1 = refl
  holds1994 m6c2 m6c1 m6c2 = refl
  holds1994 m6c2 m6c2 m6c0 = refl
  holds1994 m6c2 m6c2 m6c1 = refl
  holds1994 m6c2 m6c2 m6c2 = refl
  cut1994 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 1) (op (var 2) (op (var 1) (var 2))))) , (var 1)) → ⊥
  cut1994  = reject6 ((op (op (var 0) (var 1)) (op (var 1) (op (var 2) (op (var 1) (var 2))))) , (var 1)) (λ env → holds1994 (env 0) (env 1) (env 2))
  bad1995 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop b1 (bop b0 b1)))) b1 → ⊥
  bad1995  p = false≢true (cong lower p)
  cut1995 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 1) (op (var 2) (op (var 1) (var 2))))) , (var 2)) → ⊥
  cut1995  adequate = bad1995  (Adequate.valid adequate Two boolean env1)
  bad1996 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop b0 (bop b0 b0)))) b1 → ⊥
  bad1996  p = false≢true (cong lower p)
  cut1996 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 1) (op (var 2) (op (var 1) (var 2))))) , (var 3)) → ⊥
  cut1996  adequate = bad1996  (Adequate.valid adequate Two boolean env3)
  bad1997 : PathP (λ _ → Two) (bop (bop b0 b1) (bop b1 (bop b0 (bop b1 b0)))) b0 → ⊥
  bad1997  p = false≢true (sym (cong lower p))
  cut1997 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 1) (op (var 2) (op (var 1) (var 3))))) , (var 0)) → ⊥
  cut1997  adequate = bad1997  (Adequate.valid adequate Two boolean env4)
  bad1998 : PathP (λ _ → Two) (bop (bop b0 b1) (bop b1 (bop b1 (bop b1 b0)))) b1 → ⊥
  bad1998  p = false≢true (cong lower p)
  cut1998 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 1) (op (var 2) (op (var 1) (var 3))))) , (var 1)) → ⊥
  cut1998  adequate = bad1998  (Adequate.valid adequate Two boolean env12)
  bad1999 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop b1 (bop b0 b0)))) b1 → ⊥
  bad1999  p = false≢true (cong lower p)
  cut1999 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 1) (op (var 2) (op (var 1) (var 3))))) , (var 2)) → ⊥
  cut1999  adequate = bad1999  (Adequate.valid adequate Two boolean env5)
  bad2000 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop b0 (bop b0 b1)))) b1 → ⊥
  bad2000  p = false≢true (cong lower p)
  cut2000 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 1) (op (var 2) (op (var 1) (var 3))))) , (var 3)) → ⊥
  cut2000  adequate = bad2000  (Adequate.valid adequate Two boolean env3)
  bad2001 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop b0 (bop b0 b0)))) b1 → ⊥
  bad2001  p = false≢true (cong lower p)
  cut2001 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 1) (op (var 2) (op (var 1) (var 3))))) , (var 4)) → ⊥
  cut2001  adequate = bad2001  (Adequate.valid adequate Two boolean env6)
  bad2002 : PathP (λ _ → Two) (bop (bop b0 b1) (bop b1 (bop b0 (bop b0 b0)))) b0 → ⊥
  bad2002  p = false≢true (sym (cong lower p))
  cut2002 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 1) (op (var 2) (op (var 2) (var 0))))) , (var 0)) → ⊥
  cut2002  adequate = bad2002  (Adequate.valid adequate Two boolean env2)
  bad2003 : PathP (λ _ → Two) (bop (bop b0 b1) (bop b1 (bop b1 (bop b1 b0)))) b1 → ⊥
  bad2003  p = false≢true (cong lower p)
  cut2003 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 1) (op (var 2) (op (var 2) (var 0))))) , (var 1)) → ⊥
  cut2003  adequate = bad2003  (Adequate.valid adequate Two boolean env10)
  bad2004 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop b1 (bop b1 b0)))) b1 → ⊥
  bad2004  p = false≢true (cong lower p)
  cut2004 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 1) (op (var 2) (op (var 2) (var 0))))) , (var 2)) → ⊥
  cut2004  adequate = bad2004  (Adequate.valid adequate Two boolean env1)
  bad2005 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop b0 (bop b0 b0)))) b1 → ⊥
  bad2005  p = false≢true (cong lower p)
  cut2005 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 1) (op (var 2) (op (var 2) (var 0))))) , (var 3)) → ⊥
  cut2005  adequate = bad2005  (Adequate.valid adequate Two boolean env3)
  bad2006 : PathP (λ _ → Two) (bop (bop b0 b1) (bop b1 (bop b0 (bop b0 b1)))) b0 → ⊥
  bad2006  p = false≢true (sym (cong lower p))
  cut2006 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 1) (op (var 2) (op (var 2) (var 1))))) , (var 0)) → ⊥
  cut2006  adequate = bad2006  (Adequate.valid adequate Two boolean env2)
  holds2007 : (z0 z1 z2 : A3) → (mul3 (mul3 z0 z1) (mul3 z1 (mul3 z2 (mul3 z2 z1)))) ≡ z1
  holds2007 z0 z1 z2 = refl
  cut2007 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 1) (op (var 2) (op (var 2) (var 1))))) , (var 1)) → ⊥
  cut2007  = reject3 ((op (op (var 0) (var 1)) (op (var 1) (op (var 2) (op (var 2) (var 1))))) , (var 1)) (λ env → holds2007 (env 0) (env 1) (env 2))
  bad2008 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop b1 (bop b1 b0)))) b1 → ⊥
  bad2008  p = false≢true (cong lower p)
  cut2008 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 1) (op (var 2) (op (var 2) (var 1))))) , (var 2)) → ⊥
  cut2008  adequate = bad2008  (Adequate.valid adequate Two boolean env1)
  bad2009 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop b0 (bop b0 b0)))) b1 → ⊥
  bad2009  p = false≢true (cong lower p)
  cut2009 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 1) (op (var 2) (op (var 2) (var 1))))) , (var 3)) → ⊥
  cut2009  adequate = bad2009  (Adequate.valid adequate Two boolean env3)
  bad2010 : PathP (λ _ → Two) (bop (bop b0 b1) (bop b1 (bop b0 (bop b0 b0)))) b0 → ⊥
  bad2010  p = false≢true (sym (cong lower p))
  cut2010 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 1) (op (var 2) (op (var 2) (var 2))))) , (var 0)) → ⊥
  cut2010  adequate = bad2010  (Adequate.valid adequate Two boolean env2)
  holds2011 : (z0 z1 z2 : A6) → (mul6 (mul6 z0 z1) (mul6 z1 (mul6 z2 (mul6 z2 z2)))) ≡ z1
  holds2011 m6c0 m6c0 m6c0 = refl
  holds2011 m6c0 m6c0 m6c1 = refl
  holds2011 m6c0 m6c0 m6c2 = refl
  holds2011 m6c0 m6c1 m6c0 = refl
  holds2011 m6c0 m6c1 m6c1 = refl
  holds2011 m6c0 m6c1 m6c2 = refl
  holds2011 m6c0 m6c2 m6c0 = refl
  holds2011 m6c0 m6c2 m6c1 = refl
  holds2011 m6c0 m6c2 m6c2 = refl
  holds2011 m6c1 m6c0 m6c0 = refl
  holds2011 m6c1 m6c0 m6c1 = refl
  holds2011 m6c1 m6c0 m6c2 = refl
  holds2011 m6c1 m6c1 m6c0 = refl
  holds2011 m6c1 m6c1 m6c1 = refl
  holds2011 m6c1 m6c1 m6c2 = refl
  holds2011 m6c1 m6c2 m6c0 = refl
  holds2011 m6c1 m6c2 m6c1 = refl
  holds2011 m6c1 m6c2 m6c2 = refl
  holds2011 m6c2 m6c0 m6c0 = refl
  holds2011 m6c2 m6c0 m6c1 = refl
  holds2011 m6c2 m6c0 m6c2 = refl
  holds2011 m6c2 m6c1 m6c0 = refl
  holds2011 m6c2 m6c1 m6c1 = refl
  holds2011 m6c2 m6c1 m6c2 = refl
  holds2011 m6c2 m6c2 m6c0 = refl
  holds2011 m6c2 m6c2 m6c1 = refl
  holds2011 m6c2 m6c2 m6c2 = refl
  cut2011 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 1) (op (var 2) (op (var 2) (var 2))))) , (var 1)) → ⊥
  cut2011  = reject6 ((op (op (var 0) (var 1)) (op (var 1) (op (var 2) (op (var 2) (var 2))))) , (var 1)) (λ env → holds2011 (env 0) (env 1) (env 2))
  bad2012 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop b1 (bop b1 b1)))) b1 → ⊥
  bad2012  p = false≢true (cong lower p)
  cut2012 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 1) (op (var 2) (op (var 2) (var 2))))) , (var 2)) → ⊥
  cut2012  adequate = bad2012  (Adequate.valid adequate Two boolean env1)
  bad2013 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop b0 (bop b0 b0)))) b1 → ⊥
  bad2013  p = false≢true (cong lower p)
  cut2013 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 1) (op (var 2) (op (var 2) (var 2))))) , (var 3)) → ⊥
  cut2013  adequate = bad2013  (Adequate.valid adequate Two boolean env3)
  bad2014 : PathP (λ _ → Two) (bop (bop b0 b1) (bop b1 (bop b0 (bop b0 b0)))) b0 → ⊥
  bad2014  p = false≢true (sym (cong lower p))
  cut2014 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 1) (op (var 2) (op (var 2) (var 3))))) , (var 0)) → ⊥
  cut2014  adequate = bad2014  (Adequate.valid adequate Two boolean env4)
  bad2015 : PathP (λ _ → Two) (bop (bop b0 b1) (bop b1 (bop b1 (bop b1 b0)))) b1 → ⊥
  bad2015  p = false≢true (cong lower p)
  cut2015 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 1) (op (var 2) (op (var 2) (var 3))))) , (var 1)) → ⊥
  cut2015  adequate = bad2015  (Adequate.valid adequate Two boolean env12)
  bad2016 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop b1 (bop b1 b0)))) b1 → ⊥
  bad2016  p = false≢true (cong lower p)
  cut2016 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 1) (op (var 2) (op (var 2) (var 3))))) , (var 2)) → ⊥
  cut2016  adequate = bad2016  (Adequate.valid adequate Two boolean env5)
  bad2017 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop b0 (bop b0 b1)))) b1 → ⊥
  bad2017  p = false≢true (cong lower p)
  cut2017 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 1) (op (var 2) (op (var 2) (var 3))))) , (var 3)) → ⊥
  cut2017  adequate = bad2017  (Adequate.valid adequate Two boolean env3)
  bad2018 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop b0 (bop b0 b0)))) b1 → ⊥
  bad2018  p = false≢true (cong lower p)
  cut2018 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 1) (op (var 2) (op (var 2) (var 3))))) , (var 4)) → ⊥
  cut2018  adequate = bad2018  (Adequate.valid adequate Two boolean env6)
  bad2019 : PathP (λ _ → Two) (bop (bop b0 b1) (bop b1 (bop b0 (bop b0 b0)))) b0 → ⊥
  bad2019  p = false≢true (sym (cong lower p))
  cut2019 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 1) (op (var 2) (op (var 3) (var 0))))) , (var 0)) → ⊥
  cut2019  adequate = bad2019  (Adequate.valid adequate Two boolean env4)
  bad2020 : PathP (λ _ → Two) (bop (bop b0 b1) (bop b1 (bop b1 (bop b0 b0)))) b1 → ⊥
  bad2020  p = false≢true (cong lower p)
  cut2020 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 1) (op (var 2) (op (var 3) (var 0))))) , (var 1)) → ⊥
  cut2020  adequate = bad2020  (Adequate.valid adequate Two boolean env12)
  bad2021 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop b1 (bop b0 b0)))) b1 → ⊥
  bad2021  p = false≢true (cong lower p)
  cut2021 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 1) (op (var 2) (op (var 3) (var 0))))) , (var 2)) → ⊥
  cut2021  adequate = bad2021  (Adequate.valid adequate Two boolean env5)
  bad2022 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop b0 (bop b1 b0)))) b1 → ⊥
  bad2022  p = false≢true (cong lower p)
  cut2022 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 1) (op (var 2) (op (var 3) (var 0))))) , (var 3)) → ⊥
  cut2022  adequate = bad2022  (Adequate.valid adequate Two boolean env3)
  bad2023 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop b0 (bop b0 b0)))) b1 → ⊥
  bad2023  p = false≢true (cong lower p)
  cut2023 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 1) (op (var 2) (op (var 3) (var 0))))) , (var 4)) → ⊥
  cut2023  adequate = bad2023  (Adequate.valid adequate Two boolean env6)
  bad2024 : PathP (λ _ → Two) (bop (bop b0 b1) (bop b1 (bop b0 (bop b0 b1)))) b0 → ⊥
  bad2024  p = false≢true (sym (cong lower p))
  cut2024 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 1) (op (var 2) (op (var 3) (var 1))))) , (var 0)) → ⊥
  cut2024  adequate = bad2024  (Adequate.valid adequate Two boolean env4)
  bad2025 : PathP (λ _ → Two) (bop (bop b0 b1) (bop b1 (bop b1 (bop b0 b1)))) b1 → ⊥
  bad2025  p = false≢true (cong lower p)
  cut2025 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 1) (op (var 2) (op (var 3) (var 1))))) , (var 1)) → ⊥
  cut2025  adequate = bad2025  (Adequate.valid adequate Two boolean env12)
  bad2026 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop b1 (bop b0 b0)))) b1 → ⊥
  bad2026  p = false≢true (cong lower p)
  cut2026 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 1) (op (var 2) (op (var 3) (var 1))))) , (var 2)) → ⊥
  cut2026  adequate = bad2026  (Adequate.valid adequate Two boolean env5)
  bad2027 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop b0 (bop b1 b0)))) b1 → ⊥
  bad2027  p = false≢true (cong lower p)
  cut2027 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 1) (op (var 2) (op (var 3) (var 1))))) , (var 3)) → ⊥
  cut2027  adequate = bad2027  (Adequate.valid adequate Two boolean env3)
  bad2028 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop b0 (bop b0 b0)))) b1 → ⊥
  bad2028  p = false≢true (cong lower p)
  cut2028 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 1) (op (var 2) (op (var 3) (var 1))))) , (var 4)) → ⊥
  cut2028  adequate = bad2028  (Adequate.valid adequate Two boolean env6)
  bad2029 : PathP (λ _ → Two) (bop (bop b0 b1) (bop b1 (bop b0 (bop b0 b0)))) b0 → ⊥
  bad2029  p = false≢true (sym (cong lower p))
  cut2029 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 1) (op (var 2) (op (var 3) (var 2))))) , (var 0)) → ⊥
  cut2029  adequate = bad2029  (Adequate.valid adequate Two boolean env4)
  bad2030 : PathP (λ _ → Two) (bop (bop b0 b1) (bop b1 (bop b1 (bop b0 b1)))) b1 → ⊥
  bad2030  p = false≢true (cong lower p)
  cut2030 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 1) (op (var 2) (op (var 3) (var 2))))) , (var 1)) → ⊥
  cut2030  adequate = bad2030  (Adequate.valid adequate Two boolean env12)
  bad2031 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop b1 (bop b0 b1)))) b1 → ⊥
  bad2031  p = false≢true (cong lower p)
  cut2031 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 1) (op (var 2) (op (var 3) (var 2))))) , (var 2)) → ⊥
  cut2031  adequate = bad2031  (Adequate.valid adequate Two boolean env5)
  bad2032 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop b0 (bop b1 b0)))) b1 → ⊥
  bad2032  p = false≢true (cong lower p)
  cut2032 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 1) (op (var 2) (op (var 3) (var 2))))) , (var 3)) → ⊥
  cut2032  adequate = bad2032  (Adequate.valid adequate Two boolean env3)
  bad2033 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop b0 (bop b0 b0)))) b1 → ⊥
  bad2033  p = false≢true (cong lower p)
  cut2033 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 1) (op (var 2) (op (var 3) (var 2))))) , (var 4)) → ⊥
  cut2033  adequate = bad2033  (Adequate.valid adequate Two boolean env6)
  bad2034 : PathP (λ _ → Two) (bop (bop b0 b1) (bop b1 (bop b0 (bop b0 b0)))) b0 → ⊥
  bad2034  p = false≢true (sym (cong lower p))
  cut2034 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 1) (op (var 2) (op (var 3) (var 3))))) , (var 0)) → ⊥
  cut2034  adequate = bad2034  (Adequate.valid adequate Two boolean env4)
  bad2035 : PathP (λ _ → Two) (bop (bop b0 b1) (bop b1 (bop b1 (bop b0 b0)))) b1 → ⊥
  bad2035  p = false≢true (cong lower p)
  cut2035 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 1) (op (var 2) (op (var 3) (var 3))))) , (var 1)) → ⊥
  cut2035  adequate = bad2035  (Adequate.valid adequate Two boolean env12)
  bad2036 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop b1 (bop b0 b0)))) b1 → ⊥
  bad2036  p = false≢true (cong lower p)
  cut2036 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 1) (op (var 2) (op (var 3) (var 3))))) , (var 2)) → ⊥
  cut2036  adequate = bad2036  (Adequate.valid adequate Two boolean env5)
  bad2037 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop b0 (bop b1 b1)))) b1 → ⊥
  bad2037  p = false≢true (cong lower p)
  cut2037 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 1) (op (var 2) (op (var 3) (var 3))))) , (var 3)) → ⊥
  cut2037  adequate = bad2037  (Adequate.valid adequate Two boolean env3)
  bad2038 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop b0 (bop b0 b0)))) b1 → ⊥
  bad2038  p = false≢true (cong lower p)
  cut2038 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 1) (op (var 2) (op (var 3) (var 3))))) , (var 4)) → ⊥
  cut2038  adequate = bad2038  (Adequate.valid adequate Two boolean env6)
  bad2039 : PathP (λ _ → Two) (bop (bop b0 b1) (bop b1 (bop b0 (bop b0 b0)))) b0 → ⊥
  bad2039  p = false≢true (sym (cong lower p))
  cut2039 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 1) (op (var 2) (op (var 3) (var 4))))) , (var 0)) → ⊥
  cut2039  adequate = bad2039  (Adequate.valid adequate Two boolean env13)
  bad2040 : PathP (λ _ → Two) (bop (bop b0 b1) (bop b1 (bop b1 (bop b0 b0)))) b1 → ⊥
  bad2040  p = false≢true (cong lower p)
  cut2040 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 1) (op (var 2) (op (var 3) (var 4))))) , (var 1)) → ⊥
  cut2040  adequate = bad2040  (Adequate.valid adequate Two boolean env14)
  bad2041 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop b1 (bop b0 b0)))) b1 → ⊥
  bad2041  p = false≢true (cong lower p)
  cut2041 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 1) (op (var 2) (op (var 3) (var 4))))) , (var 2)) → ⊥
  cut2041  adequate = bad2041  (Adequate.valid adequate Two boolean env15)
  bad2042 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop b0 (bop b1 b0)))) b1 → ⊥
  bad2042  p = false≢true (cong lower p)
  cut2042 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 1) (op (var 2) (op (var 3) (var 4))))) , (var 3)) → ⊥
  cut2042  adequate = bad2042  (Adequate.valid adequate Two boolean env16)
  bad2043 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop b0 (bop b0 b1)))) b1 → ⊥
  bad2043  p = false≢true (cong lower p)
  cut2043 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 1) (op (var 2) (op (var 3) (var 4))))) , (var 4)) → ⊥
  cut2043  adequate = bad2043  (Adequate.valid adequate Two boolean env6)
  bad2044 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop b0 (bop b0 b0)))) b1 → ⊥
  bad2044  p = false≢true (cong lower p)
  cut2044 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 1) (op (var 2) (op (var 3) (var 4))))) , (var 5)) → ⊥
  cut2044  adequate = bad2044  (Adequate.valid adequate Two boolean env17)
  bad2045 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b1 (bop b0 (bop b0 b0)))) b0 → ⊥
  bad2045  p = false≢true (sym (cong lower p))
  cut2045 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (var 0) (op (var 0) (var 0))))) , (var 0)) → ⊥
  cut2045  adequate = bad2045  (Adequate.valid adequate Two boolean env1)
  bad2046 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b1 (bop b0 (bop b0 b0)))) b0 → ⊥
  bad2046  p = false≢true (sym (cong lower p))
  cut2046 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (var 0) (op (var 0) (var 0))))) , (var 1)) → ⊥
  cut2046  adequate = bad2046  (Adequate.valid adequate Two boolean env1)
  env21 : ℕ → Two
  env21 zero = b1
  env21 (suc zero) = b1
  env21 (suc (suc zero)) = b0
  env21 (suc (suc (suc rest))) = b0
  bad2047 : PathP (λ _ → Two) (bop (bop b1 b1) (bop b0 (bop b1 (bop b1 b1)))) b0 → ⊥
  bad2047  p = false≢true (sym (cong lower p))
  cut2047 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (var 0) (op (var 0) (var 0))))) , (var 2)) → ⊥
  cut2047  adequate = bad2047  (Adequate.valid adequate Two boolean env21)
  bad2048 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop b0 (bop b0 b0)))) b1 → ⊥
  bad2048  p = false≢true (cong lower p)
  cut2048 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (var 0) (op (var 0) (var 0))))) , (var 3)) → ⊥
  cut2048  adequate = bad2048  (Adequate.valid adequate Two boolean env3)
  bad2049 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b1 (bop b0 (bop b0 b0)))) b0 → ⊥
  bad2049  p = false≢true (sym (cong lower p))
  cut2049 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (var 0) (op (var 0) (var 1))))) , (var 0)) → ⊥
  cut2049  adequate = bad2049  (Adequate.valid adequate Two boolean env1)
  bad2050 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b1 (bop b0 (bop b0 b0)))) b0 → ⊥
  bad2050  p = false≢true (sym (cong lower p))
  cut2050 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (var 0) (op (var 0) (var 1))))) , (var 1)) → ⊥
  cut2050  adequate = bad2050  (Adequate.valid adequate Two boolean env1)
  bad2051 : PathP (λ _ → Two) (bop (bop b1 b0) (bop b1 (bop b1 (bop b1 b0)))) b1 → ⊥
  bad2051  p = false≢true (cong lower p)
  cut2051 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (var 0) (op (var 0) (var 1))))) , (var 2)) → ⊥
  cut2051  adequate = bad2051  (Adequate.valid adequate Two boolean env18)
  bad2052 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop b0 (bop b0 b0)))) b1 → ⊥
  bad2052  p = false≢true (cong lower p)
  cut2052 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (var 0) (op (var 0) (var 1))))) , (var 3)) → ⊥
  cut2052  adequate = bad2052  (Adequate.valid adequate Two boolean env3)
  bad2053 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b1 (bop b0 (bop b0 b1)))) b0 → ⊥
  bad2053  p = false≢true (sym (cong lower p))
  cut2053 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (var 0) (op (var 0) (var 2))))) , (var 0)) → ⊥
  cut2053  adequate = bad2053  (Adequate.valid adequate Two boolean env1)
  bad2054 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b1 (bop b0 (bop b0 b1)))) b0 → ⊥
  bad2054  p = false≢true (sym (cong lower p))
  cut2054 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (var 0) (op (var 0) (var 2))))) , (var 1)) → ⊥
  cut2054  adequate = bad2054  (Adequate.valid adequate Two boolean env1)
  bad2055 : PathP (λ _ → Two) (bop (bop b1 b1) (bop b0 (bop b1 (bop b1 b0)))) b0 → ⊥
  bad2055  p = false≢true (sym (cong lower p))
  cut2055 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (var 0) (op (var 0) (var 2))))) , (var 2)) → ⊥
  cut2055  adequate = bad2055  (Adequate.valid adequate Two boolean env21)
  bad2056 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop b0 (bop b0 b0)))) b1 → ⊥
  bad2056  p = false≢true (cong lower p)
  cut2056 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (var 0) (op (var 0) (var 2))))) , (var 3)) → ⊥
  cut2056  adequate = bad2056  (Adequate.valid adequate Two boolean env3)
  bad2057 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b1 (bop b0 (bop b0 b0)))) b0 → ⊥
  bad2057  p = false≢true (sym (cong lower p))
  cut2057 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (var 0) (op (var 0) (var 3))))) , (var 0)) → ⊥
  cut2057  adequate = bad2057  (Adequate.valid adequate Two boolean env5)
  bad2058 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b1 (bop b0 (bop b0 b0)))) b0 → ⊥
  bad2058  p = false≢true (sym (cong lower p))
  cut2058 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (var 0) (op (var 0) (var 3))))) , (var 1)) → ⊥
  cut2058  adequate = bad2058  (Adequate.valid adequate Two boolean env5)
  bad2059 : PathP (λ _ → Two) (bop (bop b1 b0) (bop b1 (bop b1 (bop b1 b0)))) b1 → ⊥
  bad2059  p = false≢true (cong lower p)
  cut2059 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (var 0) (op (var 0) (var 3))))) , (var 2)) → ⊥
  cut2059  adequate = bad2059  (Adequate.valid adequate Two boolean env19)
  bad2060 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop b0 (bop b0 b1)))) b1 → ⊥
  bad2060  p = false≢true (cong lower p)
  cut2060 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (var 0) (op (var 0) (var 3))))) , (var 3)) → ⊥
  cut2060  adequate = bad2060  (Adequate.valid adequate Two boolean env3)
  bad2061 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop b0 (bop b0 b0)))) b1 → ⊥
  bad2061  p = false≢true (cong lower p)
  cut2061 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (var 0) (op (var 0) (var 3))))) , (var 4)) → ⊥
  cut2061  adequate = bad2061  (Adequate.valid adequate Two boolean env6)
  bad2062 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b1 (bop b0 (bop b0 b0)))) b0 → ⊥
  bad2062  p = false≢true (sym (cong lower p))
  cut2062 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (var 0) (op (var 1) (var 0))))) , (var 0)) → ⊥
  cut2062  adequate = bad2062  (Adequate.valid adequate Two boolean env1)
  bad2063 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b1 (bop b0 (bop b0 b0)))) b0 → ⊥
  bad2063  p = false≢true (sym (cong lower p))
  cut2063 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (var 0) (op (var 1) (var 0))))) , (var 1)) → ⊥
  cut2063  adequate = bad2063  (Adequate.valid adequate Two boolean env1)
  bad2064 : PathP (λ _ → Two) (bop (bop b1 b0) (bop b1 (bop b1 (bop b0 b1)))) b1 → ⊥
  bad2064  p = false≢true (cong lower p)
  cut2064 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (var 0) (op (var 1) (var 0))))) , (var 2)) → ⊥
  cut2064  adequate = bad2064  (Adequate.valid adequate Two boolean env18)
  bad2065 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop b0 (bop b0 b0)))) b1 → ⊥
  bad2065  p = false≢true (cong lower p)
  cut2065 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (var 0) (op (var 1) (var 0))))) , (var 3)) → ⊥
  cut2065  adequate = bad2065  (Adequate.valid adequate Two boolean env3)
  bad2066 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b1 (bop b0 (bop b0 b0)))) b0 → ⊥
  bad2066  p = false≢true (sym (cong lower p))
  cut2066 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (var 0) (op (var 1) (var 1))))) , (var 0)) → ⊥
  cut2066  adequate = bad2066  (Adequate.valid adequate Two boolean env1)
  bad2067 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b1 (bop b0 (bop b0 b0)))) b0 → ⊥
  bad2067  p = false≢true (sym (cong lower p))
  cut2067 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (var 0) (op (var 1) (var 1))))) , (var 1)) → ⊥
  cut2067  adequate = bad2067  (Adequate.valid adequate Two boolean env1)
  bad2068 : PathP (λ _ → Two) (bop (bop b1 b0) (bop b1 (bop b1 (bop b0 b0)))) b1 → ⊥
  bad2068  p = false≢true (cong lower p)
  cut2068 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (var 0) (op (var 1) (var 1))))) , (var 2)) → ⊥
  cut2068  adequate = bad2068  (Adequate.valid adequate Two boolean env18)
  bad2069 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop b0 (bop b0 b0)))) b1 → ⊥
  bad2069  p = false≢true (cong lower p)
  cut2069 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (var 0) (op (var 1) (var 1))))) , (var 3)) → ⊥
  cut2069  adequate = bad2069  (Adequate.valid adequate Two boolean env3)
  bad2070 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b1 (bop b0 (bop b0 b1)))) b0 → ⊥
  bad2070  p = false≢true (sym (cong lower p))
  cut2070 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (var 0) (op (var 1) (var 2))))) , (var 0)) → ⊥
  cut2070  adequate = bad2070  (Adequate.valid adequate Two boolean env1)
  bad2071 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b1 (bop b0 (bop b0 b1)))) b0 → ⊥
  bad2071  p = false≢true (sym (cong lower p))
  cut2071 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (var 0) (op (var 1) (var 2))))) , (var 1)) → ⊥
  cut2071  adequate = bad2071  (Adequate.valid adequate Two boolean env1)
  bad2072 : PathP (λ _ → Two) (bop (bop b1 b0) (bop b1 (bop b1 (bop b0 b1)))) b1 → ⊥
  bad2072  p = false≢true (cong lower p)
  cut2072 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (var 0) (op (var 1) (var 2))))) , (var 2)) → ⊥
  cut2072  adequate = bad2072  (Adequate.valid adequate Two boolean env18)
  bad2073 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop b0 (bop b0 b0)))) b1 → ⊥
  bad2073  p = false≢true (cong lower p)
  cut2073 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (var 0) (op (var 1) (var 2))))) , (var 3)) → ⊥
  cut2073  adequate = bad2073  (Adequate.valid adequate Two boolean env3)
  bad2074 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b1 (bop b0 (bop b0 b0)))) b0 → ⊥
  bad2074  p = false≢true (sym (cong lower p))
  cut2074 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (var 0) (op (var 1) (var 3))))) , (var 0)) → ⊥
  cut2074  adequate = bad2074  (Adequate.valid adequate Two boolean env5)
  bad2075 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b1 (bop b0 (bop b0 b0)))) b0 → ⊥
  bad2075  p = false≢true (sym (cong lower p))
  cut2075 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (var 0) (op (var 1) (var 3))))) , (var 1)) → ⊥
  cut2075  adequate = bad2075  (Adequate.valid adequate Two boolean env5)
  bad2076 : PathP (λ _ → Two) (bop (bop b1 b0) (bop b1 (bop b1 (bop b0 b0)))) b1 → ⊥
  bad2076  p = false≢true (cong lower p)
  cut2076 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (var 0) (op (var 1) (var 3))))) , (var 2)) → ⊥
  cut2076  adequate = bad2076  (Adequate.valid adequate Two boolean env19)
  bad2077 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop b0 (bop b0 b1)))) b1 → ⊥
  bad2077  p = false≢true (cong lower p)
  cut2077 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (var 0) (op (var 1) (var 3))))) , (var 3)) → ⊥
  cut2077  adequate = bad2077  (Adequate.valid adequate Two boolean env3)
  bad2078 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop b0 (bop b0 b0)))) b1 → ⊥
  bad2078  p = false≢true (cong lower p)
  cut2078 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (var 0) (op (var 1) (var 3))))) , (var 4)) → ⊥
  cut2078  adequate = bad2078  (Adequate.valid adequate Two boolean env6)
  bad2079 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b1 (bop b0 (bop b1 b0)))) b0 → ⊥
  bad2079  p = false≢true (sym (cong lower p))
  cut2079 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (var 0) (op (var 2) (var 0))))) , (var 0)) → ⊥
  cut2079  adequate = bad2079  (Adequate.valid adequate Two boolean env1)
  bad2080 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b1 (bop b0 (bop b1 b0)))) b0 → ⊥
  bad2080  p = false≢true (sym (cong lower p))
  cut2080 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (var 0) (op (var 2) (var 0))))) , (var 1)) → ⊥
  cut2080  adequate = bad2080  (Adequate.valid adequate Two boolean env1)
  bad2081 : PathP (λ _ → Two) (bop (bop b1 b1) (bop b0 (bop b1 (bop b0 b1)))) b0 → ⊥
  bad2081  p = false≢true (sym (cong lower p))
  cut2081 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (var 0) (op (var 2) (var 0))))) , (var 2)) → ⊥
  cut2081  adequate = bad2081  (Adequate.valid adequate Two boolean env21)
  bad2082 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop b0 (bop b0 b0)))) b1 → ⊥
  bad2082  p = false≢true (cong lower p)
  cut2082 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (var 0) (op (var 2) (var 0))))) , (var 3)) → ⊥
  cut2082  adequate = bad2082  (Adequate.valid adequate Two boolean env3)
  bad2083 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b1 (bop b0 (bop b1 b0)))) b0 → ⊥
  bad2083  p = false≢true (sym (cong lower p))
  cut2083 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (var 0) (op (var 2) (var 1))))) , (var 0)) → ⊥
  cut2083  adequate = bad2083  (Adequate.valid adequate Two boolean env1)
  bad2084 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b1 (bop b0 (bop b1 b0)))) b0 → ⊥
  bad2084  p = false≢true (sym (cong lower p))
  cut2084 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (var 0) (op (var 2) (var 1))))) , (var 1)) → ⊥
  cut2084  adequate = bad2084  (Adequate.valid adequate Two boolean env1)
  bad2085 : PathP (λ _ → Two) (bop (bop b1 b0) (bop b1 (bop b1 (bop b1 b0)))) b1 → ⊥
  bad2085  p = false≢true (cong lower p)
  cut2085 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (var 0) (op (var 2) (var 1))))) , (var 2)) → ⊥
  cut2085  adequate = bad2085  (Adequate.valid adequate Two boolean env18)
  bad2086 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop b0 (bop b0 b0)))) b1 → ⊥
  bad2086  p = false≢true (cong lower p)
  cut2086 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (var 0) (op (var 2) (var 1))))) , (var 3)) → ⊥
  cut2086  adequate = bad2086  (Adequate.valid adequate Two boolean env3)
  bad2087 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b1 (bop b0 (bop b1 b1)))) b0 → ⊥
  bad2087  p = false≢true (sym (cong lower p))
  cut2087 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (var 0) (op (var 2) (var 2))))) , (var 0)) → ⊥
  cut2087  adequate = bad2087  (Adequate.valid adequate Two boolean env1)
  bad2088 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b1 (bop b0 (bop b1 b1)))) b0 → ⊥
  bad2088  p = false≢true (sym (cong lower p))
  cut2088 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (var 0) (op (var 2) (var 2))))) , (var 1)) → ⊥
  cut2088  adequate = bad2088  (Adequate.valid adequate Two boolean env1)
  bad2089 : PathP (λ _ → Two) (bop (bop b1 b1) (bop b0 (bop b1 (bop b0 b0)))) b0 → ⊥
  bad2089  p = false≢true (sym (cong lower p))
  cut2089 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (var 0) (op (var 2) (var 2))))) , (var 2)) → ⊥
  cut2089  adequate = bad2089  (Adequate.valid adequate Two boolean env21)
  bad2090 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop b0 (bop b0 b0)))) b1 → ⊥
  bad2090  p = false≢true (cong lower p)
  cut2090 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (var 0) (op (var 2) (var 2))))) , (var 3)) → ⊥
  cut2090  adequate = bad2090  (Adequate.valid adequate Two boolean env3)
  bad2091 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b1 (bop b0 (bop b1 b0)))) b0 → ⊥
  bad2091  p = false≢true (sym (cong lower p))
  cut2091 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (var 0) (op (var 2) (var 3))))) , (var 0)) → ⊥
  cut2091  adequate = bad2091  (Adequate.valid adequate Two boolean env5)
  bad2092 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b1 (bop b0 (bop b1 b0)))) b0 → ⊥
  bad2092  p = false≢true (sym (cong lower p))
  cut2092 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (var 0) (op (var 2) (var 3))))) , (var 1)) → ⊥
  cut2092  adequate = bad2092  (Adequate.valid adequate Two boolean env5)
  bad2093 : PathP (λ _ → Two) (bop (bop b1 b0) (bop b1 (bop b1 (bop b1 b0)))) b1 → ⊥
  bad2093  p = false≢true (cong lower p)
  cut2093 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (var 0) (op (var 2) (var 3))))) , (var 2)) → ⊥
  cut2093  adequate = bad2093  (Adequate.valid adequate Two boolean env19)
  bad2094 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop b0 (bop b0 b1)))) b1 → ⊥
  bad2094  p = false≢true (cong lower p)
  cut2094 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (var 0) (op (var 2) (var 3))))) , (var 3)) → ⊥
  cut2094  adequate = bad2094  (Adequate.valid adequate Two boolean env3)
  bad2095 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop b0 (bop b0 b0)))) b1 → ⊥
  bad2095  p = false≢true (cong lower p)
  cut2095 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (var 0) (op (var 2) (var 3))))) , (var 4)) → ⊥
  cut2095  adequate = bad2095  (Adequate.valid adequate Two boolean env6)
  bad2096 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b1 (bop b0 (bop b0 b0)))) b0 → ⊥
  bad2096  p = false≢true (sym (cong lower p))
  cut2096 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (var 0) (op (var 3) (var 0))))) , (var 0)) → ⊥
  cut2096  adequate = bad2096  (Adequate.valid adequate Two boolean env5)
  bad2097 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b1 (bop b0 (bop b0 b0)))) b0 → ⊥
  bad2097  p = false≢true (sym (cong lower p))
  cut2097 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (var 0) (op (var 3) (var 0))))) , (var 1)) → ⊥
  cut2097  adequate = bad2097  (Adequate.valid adequate Two boolean env5)
  bad2098 : PathP (λ _ → Two) (bop (bop b1 b0) (bop b1 (bop b1 (bop b0 b1)))) b1 → ⊥
  bad2098  p = false≢true (cong lower p)
  cut2098 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (var 0) (op (var 3) (var 0))))) , (var 2)) → ⊥
  cut2098  adequate = bad2098  (Adequate.valid adequate Two boolean env19)
  bad2099 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop b0 (bop b1 b0)))) b1 → ⊥
  bad2099  p = false≢true (cong lower p)
  cut2099 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (var 0) (op (var 3) (var 0))))) , (var 3)) → ⊥
  cut2099  adequate = bad2099  (Adequate.valid adequate Two boolean env3)
  bad2100 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop b0 (bop b0 b0)))) b1 → ⊥
  bad2100  p = false≢true (cong lower p)
  cut2100 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (var 0) (op (var 3) (var 0))))) , (var 4)) → ⊥
  cut2100  adequate = bad2100  (Adequate.valid adequate Two boolean env6)
  bad2101 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b1 (bop b0 (bop b0 b0)))) b0 → ⊥
  bad2101  p = false≢true (sym (cong lower p))
  cut2101 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (var 0) (op (var 3) (var 1))))) , (var 0)) → ⊥
  cut2101  adequate = bad2101  (Adequate.valid adequate Two boolean env5)
  bad2102 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b1 (bop b0 (bop b0 b0)))) b0 → ⊥
  bad2102  p = false≢true (sym (cong lower p))
  cut2102 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (var 0) (op (var 3) (var 1))))) , (var 1)) → ⊥
  cut2102  adequate = bad2102  (Adequate.valid adequate Two boolean env5)
  bad2103 : PathP (λ _ → Two) (bop (bop b1 b0) (bop b1 (bop b1 (bop b0 b0)))) b1 → ⊥
  bad2103  p = false≢true (cong lower p)
  cut2103 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (var 0) (op (var 3) (var 1))))) , (var 2)) → ⊥
  cut2103  adequate = bad2103  (Adequate.valid adequate Two boolean env19)
  bad2104 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop b0 (bop b1 b0)))) b1 → ⊥
  bad2104  p = false≢true (cong lower p)
  cut2104 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (var 0) (op (var 3) (var 1))))) , (var 3)) → ⊥
  cut2104  adequate = bad2104  (Adequate.valid adequate Two boolean env3)
  bad2105 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop b0 (bop b0 b0)))) b1 → ⊥
  bad2105  p = false≢true (cong lower p)
  cut2105 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (var 0) (op (var 3) (var 1))))) , (var 4)) → ⊥
  cut2105  adequate = bad2105  (Adequate.valid adequate Two boolean env6)
  bad2106 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b1 (bop b0 (bop b0 b1)))) b0 → ⊥
  bad2106  p = false≢true (sym (cong lower p))
  cut2106 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (var 0) (op (var 3) (var 2))))) , (var 0)) → ⊥
  cut2106  adequate = bad2106  (Adequate.valid adequate Two boolean env5)
  bad2107 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b1 (bop b0 (bop b0 b1)))) b0 → ⊥
  bad2107  p = false≢true (sym (cong lower p))
  cut2107 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (var 0) (op (var 3) (var 2))))) , (var 1)) → ⊥
  cut2107  adequate = bad2107  (Adequate.valid adequate Two boolean env5)
  bad2108 : PathP (λ _ → Two) (bop (bop b1 b0) (bop b1 (bop b1 (bop b0 b1)))) b1 → ⊥
  bad2108  p = false≢true (cong lower p)
  cut2108 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (var 0) (op (var 3) (var 2))))) , (var 2)) → ⊥
  cut2108  adequate = bad2108  (Adequate.valid adequate Two boolean env19)
  bad2109 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop b0 (bop b1 b0)))) b1 → ⊥
  bad2109  p = false≢true (cong lower p)
  cut2109 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (var 0) (op (var 3) (var 2))))) , (var 3)) → ⊥
  cut2109  adequate = bad2109  (Adequate.valid adequate Two boolean env3)
  bad2110 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop b0 (bop b0 b0)))) b1 → ⊥
  bad2110  p = false≢true (cong lower p)
  cut2110 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (var 0) (op (var 3) (var 2))))) , (var 4)) → ⊥
  cut2110  adequate = bad2110  (Adequate.valid adequate Two boolean env6)
  bad2111 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b1 (bop b0 (bop b0 b0)))) b0 → ⊥
  bad2111  p = false≢true (sym (cong lower p))
  cut2111 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (var 0) (op (var 3) (var 3))))) , (var 0)) → ⊥
  cut2111  adequate = bad2111  (Adequate.valid adequate Two boolean env5)
  bad2112 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b1 (bop b0 (bop b0 b0)))) b0 → ⊥
  bad2112  p = false≢true (sym (cong lower p))
  cut2112 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (var 0) (op (var 3) (var 3))))) , (var 1)) → ⊥
  cut2112  adequate = bad2112  (Adequate.valid adequate Two boolean env5)
  bad2113 : PathP (λ _ → Two) (bop (bop b1 b0) (bop b1 (bop b1 (bop b0 b0)))) b1 → ⊥
  bad2113  p = false≢true (cong lower p)
  cut2113 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (var 0) (op (var 3) (var 3))))) , (var 2)) → ⊥
  cut2113  adequate = bad2113  (Adequate.valid adequate Two boolean env19)
  bad2114 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop b0 (bop b1 b1)))) b1 → ⊥
  bad2114  p = false≢true (cong lower p)
  cut2114 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (var 0) (op (var 3) (var 3))))) , (var 3)) → ⊥
  cut2114  adequate = bad2114  (Adequate.valid adequate Two boolean env3)
  bad2115 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop b0 (bop b0 b0)))) b1 → ⊥
  bad2115  p = false≢true (cong lower p)
  cut2115 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (var 0) (op (var 3) (var 3))))) , (var 4)) → ⊥
  cut2115  adequate = bad2115  (Adequate.valid adequate Two boolean env6)
  bad2116 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b1 (bop b0 (bop b0 b0)))) b0 → ⊥
  bad2116  p = false≢true (sym (cong lower p))
  cut2116 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (var 0) (op (var 3) (var 4))))) , (var 0)) → ⊥
  cut2116  adequate = bad2116  (Adequate.valid adequate Two boolean env15)
  bad2117 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b1 (bop b0 (bop b0 b0)))) b0 → ⊥
  bad2117  p = false≢true (sym (cong lower p))
  cut2117 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (var 0) (op (var 3) (var 4))))) , (var 1)) → ⊥
  cut2117  adequate = bad2117  (Adequate.valid adequate Two boolean env15)
  bad2118 : PathP (λ _ → Two) (bop (bop b1 b0) (bop b1 (bop b1 (bop b0 b0)))) b1 → ⊥
  bad2118  p = false≢true (cong lower p)
  cut2118 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (var 0) (op (var 3) (var 4))))) , (var 2)) → ⊥
  cut2118  adequate = bad2118  (Adequate.valid adequate Two boolean env20)
  bad2119 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop b0 (bop b1 b0)))) b1 → ⊥
  bad2119  p = false≢true (cong lower p)
  cut2119 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (var 0) (op (var 3) (var 4))))) , (var 3)) → ⊥
  cut2119  adequate = bad2119  (Adequate.valid adequate Two boolean env16)
  bad2120 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop b0 (bop b0 b1)))) b1 → ⊥
  bad2120  p = false≢true (cong lower p)
  cut2120 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (var 0) (op (var 3) (var 4))))) , (var 4)) → ⊥
  cut2120  adequate = bad2120  (Adequate.valid adequate Two boolean env6)
  bad2121 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop b0 (bop b0 b0)))) b1 → ⊥
  bad2121  p = false≢true (cong lower p)
  cut2121 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (var 0) (op (var 3) (var 4))))) , (var 5)) → ⊥
  cut2121  adequate = bad2121  (Adequate.valid adequate Two boolean env17)
  bad2122 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b1 (bop b0 (bop b0 b0)))) b0 → ⊥
  bad2122  p = false≢true (sym (cong lower p))
  cut2122 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (var 1) (op (var 0) (var 0))))) , (var 0)) → ⊥
  cut2122  adequate = bad2122  (Adequate.valid adequate Two boolean env1)
  bad2123 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b1 (bop b0 (bop b0 b0)))) b0 → ⊥
  bad2123  p = false≢true (sym (cong lower p))
  cut2123 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (var 1) (op (var 0) (var 0))))) , (var 1)) → ⊥
  cut2123  adequate = bad2123  (Adequate.valid adequate Two boolean env1)
  bad2124 : PathP (λ _ → Two) (bop (bop b0 b1) (bop b1 (bop b1 (bop b0 b0)))) b1 → ⊥
  bad2124  p = false≢true (cong lower p)
  cut2124 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (var 1) (op (var 0) (var 0))))) , (var 2)) → ⊥
  cut2124  adequate = bad2124  (Adequate.valid adequate Two boolean env10)
  bad2125 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop b0 (bop b0 b0)))) b1 → ⊥
  bad2125  p = false≢true (cong lower p)
  cut2125 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (var 1) (op (var 0) (var 0))))) , (var 3)) → ⊥
  cut2125  adequate = bad2125  (Adequate.valid adequate Two boolean env3)
  bad2126 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b1 (bop b0 (bop b0 b0)))) b0 → ⊥
  bad2126  p = false≢true (sym (cong lower p))
  cut2126 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (var 1) (op (var 0) (var 1))))) , (var 0)) → ⊥
  cut2126  adequate = bad2126  (Adequate.valid adequate Two boolean env1)
  bad2127 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b1 (bop b0 (bop b0 b0)))) b0 → ⊥
  bad2127  p = false≢true (sym (cong lower p))
  cut2127 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (var 1) (op (var 0) (var 1))))) , (var 1)) → ⊥
  cut2127  adequate = bad2127  (Adequate.valid adequate Two boolean env1)
  bad2128 : PathP (λ _ → Two) (bop (bop b0 b1) (bop b1 (bop b1 (bop b0 b1)))) b1 → ⊥
  bad2128  p = false≢true (cong lower p)
  cut2128 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (var 1) (op (var 0) (var 1))))) , (var 2)) → ⊥
  cut2128  adequate = bad2128  (Adequate.valid adequate Two boolean env10)
  bad2129 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop b0 (bop b0 b0)))) b1 → ⊥
  bad2129  p = false≢true (cong lower p)
  cut2129 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (var 1) (op (var 0) (var 1))))) , (var 3)) → ⊥
  cut2129  adequate = bad2129  (Adequate.valid adequate Two boolean env3)
  bad2130 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b1 (bop b0 (bop b0 b1)))) b0 → ⊥
  bad2130  p = false≢true (sym (cong lower p))
  cut2130 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (var 1) (op (var 0) (var 2))))) , (var 0)) → ⊥
  cut2130  adequate = bad2130  (Adequate.valid adequate Two boolean env1)
  bad2131 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b1 (bop b0 (bop b0 b1)))) b0 → ⊥
  bad2131  p = false≢true (sym (cong lower p))
  cut2131 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (var 1) (op (var 0) (var 2))))) , (var 1)) → ⊥
  cut2131  adequate = bad2131  (Adequate.valid adequate Two boolean env1)
  bad2132 : PathP (λ _ → Two) (bop (bop b0 b1) (bop b1 (bop b1 (bop b0 b1)))) b1 → ⊥
  bad2132  p = false≢true (cong lower p)
  cut2132 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (var 1) (op (var 0) (var 2))))) , (var 2)) → ⊥
  cut2132  adequate = bad2132  (Adequate.valid adequate Two boolean env10)
  bad2133 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop b0 (bop b0 b0)))) b1 → ⊥
  bad2133  p = false≢true (cong lower p)
  cut2133 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (var 1) (op (var 0) (var 2))))) , (var 3)) → ⊥
  cut2133  adequate = bad2133  (Adequate.valid adequate Two boolean env3)
  bad2134 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b1 (bop b0 (bop b0 b0)))) b0 → ⊥
  bad2134  p = false≢true (sym (cong lower p))
  cut2134 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (var 1) (op (var 0) (var 3))))) , (var 0)) → ⊥
  cut2134  adequate = bad2134  (Adequate.valid adequate Two boolean env5)
  bad2135 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b1 (bop b0 (bop b0 b0)))) b0 → ⊥
  bad2135  p = false≢true (sym (cong lower p))
  cut2135 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (var 1) (op (var 0) (var 3))))) , (var 1)) → ⊥
  cut2135  adequate = bad2135  (Adequate.valid adequate Two boolean env5)
  bad2136 : PathP (λ _ → Two) (bop (bop b0 b1) (bop b1 (bop b1 (bop b0 b0)))) b1 → ⊥
  bad2136  p = false≢true (cong lower p)
  cut2136 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (var 1) (op (var 0) (var 3))))) , (var 2)) → ⊥
  cut2136  adequate = bad2136  (Adequate.valid adequate Two boolean env12)
  bad2137 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop b0 (bop b0 b1)))) b1 → ⊥
  bad2137  p = false≢true (cong lower p)
  cut2137 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (var 1) (op (var 0) (var 3))))) , (var 3)) → ⊥
  cut2137  adequate = bad2137  (Adequate.valid adequate Two boolean env3)
  bad2138 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop b0 (bop b0 b0)))) b1 → ⊥
  bad2138  p = false≢true (cong lower p)
  cut2138 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (var 1) (op (var 0) (var 3))))) , (var 4)) → ⊥
  cut2138  adequate = bad2138  (Adequate.valid adequate Two boolean env6)
  bad2139 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b1 (bop b0 (bop b0 b0)))) b0 → ⊥
  bad2139  p = false≢true (sym (cong lower p))
  cut2139 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (var 1) (op (var 1) (var 0))))) , (var 0)) → ⊥
  cut2139  adequate = bad2139  (Adequate.valid adequate Two boolean env1)
  bad2140 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b1 (bop b0 (bop b0 b0)))) b0 → ⊥
  bad2140  p = false≢true (sym (cong lower p))
  cut2140 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (var 1) (op (var 1) (var 0))))) , (var 1)) → ⊥
  cut2140  adequate = bad2140  (Adequate.valid adequate Two boolean env1)
  bad2141 : PathP (λ _ → Two) (bop (bop b0 b1) (bop b1 (bop b1 (bop b1 b0)))) b1 → ⊥
  bad2141  p = false≢true (cong lower p)
  cut2141 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (var 1) (op (var 1) (var 0))))) , (var 2)) → ⊥
  cut2141  adequate = bad2141  (Adequate.valid adequate Two boolean env10)
  bad2142 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop b0 (bop b0 b0)))) b1 → ⊥
  bad2142  p = false≢true (cong lower p)
  cut2142 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (var 1) (op (var 1) (var 0))))) , (var 3)) → ⊥
  cut2142  adequate = bad2142  (Adequate.valid adequate Two boolean env3)
  bad2143 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b1 (bop b0 (bop b0 b0)))) b0 → ⊥
  bad2143  p = false≢true (sym (cong lower p))
  cut2143 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (var 1) (op (var 1) (var 1))))) , (var 0)) → ⊥
  cut2143  adequate = bad2143  (Adequate.valid adequate Two boolean env1)
  bad2144 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b1 (bop b0 (bop b0 b0)))) b0 → ⊥
  bad2144  p = false≢true (sym (cong lower p))
  cut2144 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (var 1) (op (var 1) (var 1))))) , (var 1)) → ⊥
  cut2144  adequate = bad2144  (Adequate.valid adequate Two boolean env1)
  bad2145 : PathP (λ _ → Two) (bop (bop b1 b1) (bop b0 (bop b1 (bop b1 b1)))) b0 → ⊥
  bad2145  p = false≢true (sym (cong lower p))
  cut2145 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (var 1) (op (var 1) (var 1))))) , (var 2)) → ⊥
  cut2145  adequate = bad2145  (Adequate.valid adequate Two boolean env21)
  bad2146 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop b0 (bop b0 b0)))) b1 → ⊥
  bad2146  p = false≢true (cong lower p)
  cut2146 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (var 1) (op (var 1) (var 1))))) , (var 3)) → ⊥
  cut2146  adequate = bad2146  (Adequate.valid adequate Two boolean env3)
  bad2147 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b1 (bop b0 (bop b0 b1)))) b0 → ⊥
  bad2147  p = false≢true (sym (cong lower p))
  cut2147 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (var 1) (op (var 1) (var 2))))) , (var 0)) → ⊥
  cut2147  adequate = bad2147  (Adequate.valid adequate Two boolean env1)
  bad2148 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b1 (bop b0 (bop b0 b1)))) b0 → ⊥
  bad2148  p = false≢true (sym (cong lower p))
  cut2148 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (var 1) (op (var 1) (var 2))))) , (var 1)) → ⊥
  cut2148  adequate = bad2148  (Adequate.valid adequate Two boolean env1)
  bad2149 : PathP (λ _ → Two) (bop (bop b1 b1) (bop b0 (bop b1 (bop b1 b0)))) b0 → ⊥
  bad2149  p = false≢true (sym (cong lower p))
  cut2149 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (var 1) (op (var 1) (var 2))))) , (var 2)) → ⊥
  cut2149  adequate = bad2149  (Adequate.valid adequate Two boolean env21)
  bad2150 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop b0 (bop b0 b0)))) b1 → ⊥
  bad2150  p = false≢true (cong lower p)
  cut2150 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (var 1) (op (var 1) (var 2))))) , (var 3)) → ⊥
  cut2150  adequate = bad2150  (Adequate.valid adequate Two boolean env3)
  bad2151 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b1 (bop b0 (bop b0 b0)))) b0 → ⊥
  bad2151  p = false≢true (sym (cong lower p))
  cut2151 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (var 1) (op (var 1) (var 3))))) , (var 0)) → ⊥
  cut2151  adequate = bad2151  (Adequate.valid adequate Two boolean env5)
  bad2152 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b1 (bop b0 (bop b0 b0)))) b0 → ⊥
  bad2152  p = false≢true (sym (cong lower p))
  cut2152 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (var 1) (op (var 1) (var 3))))) , (var 1)) → ⊥
  cut2152  adequate = bad2152  (Adequate.valid adequate Two boolean env5)
  bad2153 : PathP (λ _ → Two) (bop (bop b0 b1) (bop b1 (bop b1 (bop b1 b0)))) b1 → ⊥
  bad2153  p = false≢true (cong lower p)
  cut2153 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (var 1) (op (var 1) (var 3))))) , (var 2)) → ⊥
  cut2153  adequate = bad2153  (Adequate.valid adequate Two boolean env12)
  bad2154 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop b0 (bop b0 b1)))) b1 → ⊥
  bad2154  p = false≢true (cong lower p)
  cut2154 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (var 1) (op (var 1) (var 3))))) , (var 3)) → ⊥
  cut2154  adequate = bad2154  (Adequate.valid adequate Two boolean env3)
  bad2155 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop b0 (bop b0 b0)))) b1 → ⊥
  bad2155  p = false≢true (cong lower p)
  cut2155 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (var 1) (op (var 1) (var 3))))) , (var 4)) → ⊥
  cut2155  adequate = bad2155  (Adequate.valid adequate Two boolean env6)
  bad2156 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b1 (bop b0 (bop b1 b0)))) b0 → ⊥
  bad2156  p = false≢true (sym (cong lower p))
  cut2156 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (var 1) (op (var 2) (var 0))))) , (var 0)) → ⊥
  cut2156  adequate = bad2156  (Adequate.valid adequate Two boolean env1)
  bad2157 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b1 (bop b0 (bop b1 b0)))) b0 → ⊥
  bad2157  p = false≢true (sym (cong lower p))
  cut2157 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (var 1) (op (var 2) (var 0))))) , (var 1)) → ⊥
  cut2157  adequate = bad2157  (Adequate.valid adequate Two boolean env1)
  bad2158 : PathP (λ _ → Two) (bop (bop b0 b1) (bop b1 (bop b1 (bop b1 b0)))) b1 → ⊥
  bad2158  p = false≢true (cong lower p)
  cut2158 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (var 1) (op (var 2) (var 0))))) , (var 2)) → ⊥
  cut2158  adequate = bad2158  (Adequate.valid adequate Two boolean env10)
  bad2159 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop b0 (bop b0 b0)))) b1 → ⊥
  bad2159  p = false≢true (cong lower p)
  cut2159 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (var 1) (op (var 2) (var 0))))) , (var 3)) → ⊥
  cut2159  adequate = bad2159  (Adequate.valid adequate Two boolean env3)
  bad2160 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b1 (bop b0 (bop b1 b0)))) b0 → ⊥
  bad2160  p = false≢true (sym (cong lower p))
  cut2160 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (var 1) (op (var 2) (var 1))))) , (var 0)) → ⊥
  cut2160  adequate = bad2160  (Adequate.valid adequate Two boolean env1)
  bad2161 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b1 (bop b0 (bop b1 b0)))) b0 → ⊥
  bad2161  p = false≢true (sym (cong lower p))
  cut2161 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (var 1) (op (var 2) (var 1))))) , (var 1)) → ⊥
  cut2161  adequate = bad2161  (Adequate.valid adequate Two boolean env1)
  bad2162 : PathP (λ _ → Two) (bop (bop b1 b1) (bop b0 (bop b1 (bop b0 b1)))) b0 → ⊥
  bad2162  p = false≢true (sym (cong lower p))
  cut2162 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (var 1) (op (var 2) (var 1))))) , (var 2)) → ⊥
  cut2162  adequate = bad2162  (Adequate.valid adequate Two boolean env21)
  bad2163 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop b0 (bop b0 b0)))) b1 → ⊥
  bad2163  p = false≢true (cong lower p)
  cut2163 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (var 1) (op (var 2) (var 1))))) , (var 3)) → ⊥
  cut2163  adequate = bad2163  (Adequate.valid adequate Two boolean env3)
  bad2164 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b1 (bop b0 (bop b1 b1)))) b0 → ⊥
  bad2164  p = false≢true (sym (cong lower p))
  cut2164 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (var 1) (op (var 2) (var 2))))) , (var 0)) → ⊥
  cut2164  adequate = bad2164  (Adequate.valid adequate Two boolean env1)
  bad2165 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b1 (bop b0 (bop b1 b1)))) b0 → ⊥
  bad2165  p = false≢true (sym (cong lower p))
  cut2165 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (var 1) (op (var 2) (var 2))))) , (var 1)) → ⊥
  cut2165  adequate = bad2165  (Adequate.valid adequate Two boolean env1)
  bad2166 : PathP (λ _ → Two) (bop (bop b1 b1) (bop b0 (bop b1 (bop b0 b0)))) b0 → ⊥
  bad2166  p = false≢true (sym (cong lower p))
  cut2166 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (var 1) (op (var 2) (var 2))))) , (var 2)) → ⊥
  cut2166  adequate = bad2166  (Adequate.valid adequate Two boolean env21)
  bad2167 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop b0 (bop b0 b0)))) b1 → ⊥
  bad2167  p = false≢true (cong lower p)
  cut2167 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (var 1) (op (var 2) (var 2))))) , (var 3)) → ⊥
  cut2167  adequate = bad2167  (Adequate.valid adequate Two boolean env3)
  bad2168 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b1 (bop b0 (bop b1 b0)))) b0 → ⊥
  bad2168  p = false≢true (sym (cong lower p))
  cut2168 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (var 1) (op (var 2) (var 3))))) , (var 0)) → ⊥
  cut2168  adequate = bad2168  (Adequate.valid adequate Two boolean env5)
  bad2169 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b1 (bop b0 (bop b1 b0)))) b0 → ⊥
  bad2169  p = false≢true (sym (cong lower p))
  cut2169 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (var 1) (op (var 2) (var 3))))) , (var 1)) → ⊥
  cut2169  adequate = bad2169  (Adequate.valid adequate Two boolean env5)
  bad2170 : PathP (λ _ → Two) (bop (bop b0 b1) (bop b1 (bop b1 (bop b1 b0)))) b1 → ⊥
  bad2170  p = false≢true (cong lower p)
  cut2170 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (var 1) (op (var 2) (var 3))))) , (var 2)) → ⊥
  cut2170  adequate = bad2170  (Adequate.valid adequate Two boolean env12)
  bad2171 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop b0 (bop b0 b1)))) b1 → ⊥
  bad2171  p = false≢true (cong lower p)
  cut2171 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (var 1) (op (var 2) (var 3))))) , (var 3)) → ⊥
  cut2171  adequate = bad2171  (Adequate.valid adequate Two boolean env3)
  bad2172 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop b0 (bop b0 b0)))) b1 → ⊥
  bad2172  p = false≢true (cong lower p)
  cut2172 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (var 1) (op (var 2) (var 3))))) , (var 4)) → ⊥
  cut2172  adequate = bad2172  (Adequate.valid adequate Two boolean env6)
  bad2173 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b1 (bop b0 (bop b0 b0)))) b0 → ⊥
  bad2173  p = false≢true (sym (cong lower p))
  cut2173 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (var 1) (op (var 3) (var 0))))) , (var 0)) → ⊥
  cut2173  adequate = bad2173  (Adequate.valid adequate Two boolean env5)
  bad2174 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b1 (bop b0 (bop b0 b0)))) b0 → ⊥
  bad2174  p = false≢true (sym (cong lower p))
  cut2174 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (var 1) (op (var 3) (var 0))))) , (var 1)) → ⊥
  cut2174  adequate = bad2174  (Adequate.valid adequate Two boolean env5)
  bad2175 : PathP (λ _ → Two) (bop (bop b0 b1) (bop b1 (bop b1 (bop b0 b0)))) b1 → ⊥
  bad2175  p = false≢true (cong lower p)
  cut2175 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (var 1) (op (var 3) (var 0))))) , (var 2)) → ⊥
  cut2175  adequate = bad2175  (Adequate.valid adequate Two boolean env12)
  bad2176 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop b0 (bop b1 b0)))) b1 → ⊥
  bad2176  p = false≢true (cong lower p)
  cut2176 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (var 1) (op (var 3) (var 0))))) , (var 3)) → ⊥
  cut2176  adequate = bad2176  (Adequate.valid adequate Two boolean env3)
  bad2177 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop b0 (bop b0 b0)))) b1 → ⊥
  bad2177  p = false≢true (cong lower p)
  cut2177 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (var 1) (op (var 3) (var 0))))) , (var 4)) → ⊥
  cut2177  adequate = bad2177  (Adequate.valid adequate Two boolean env6)
  bad2178 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b1 (bop b0 (bop b0 b0)))) b0 → ⊥
  bad2178  p = false≢true (sym (cong lower p))
  cut2178 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (var 1) (op (var 3) (var 1))))) , (var 0)) → ⊥
  cut2178  adequate = bad2178  (Adequate.valid adequate Two boolean env5)
  bad2179 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b1 (bop b0 (bop b0 b0)))) b0 → ⊥
  bad2179  p = false≢true (sym (cong lower p))
  cut2179 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (var 1) (op (var 3) (var 1))))) , (var 1)) → ⊥
  cut2179  adequate = bad2179  (Adequate.valid adequate Two boolean env5)
  bad2180 : PathP (λ _ → Two) (bop (bop b0 b1) (bop b1 (bop b1 (bop b0 b1)))) b1 → ⊥
  bad2180  p = false≢true (cong lower p)
  cut2180 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (var 1) (op (var 3) (var 1))))) , (var 2)) → ⊥
  cut2180  adequate = bad2180  (Adequate.valid adequate Two boolean env12)
  bad2181 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop b0 (bop b1 b0)))) b1 → ⊥
  bad2181  p = false≢true (cong lower p)
  cut2181 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (var 1) (op (var 3) (var 1))))) , (var 3)) → ⊥
  cut2181  adequate = bad2181  (Adequate.valid adequate Two boolean env3)
  bad2182 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop b0 (bop b0 b0)))) b1 → ⊥
  bad2182  p = false≢true (cong lower p)
  cut2182 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (var 1) (op (var 3) (var 1))))) , (var 4)) → ⊥
  cut2182  adequate = bad2182  (Adequate.valid adequate Two boolean env6)
  bad2183 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b1 (bop b0 (bop b0 b1)))) b0 → ⊥
  bad2183  p = false≢true (sym (cong lower p))
  cut2183 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (var 1) (op (var 3) (var 2))))) , (var 0)) → ⊥
  cut2183  adequate = bad2183  (Adequate.valid adequate Two boolean env5)
  bad2184 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b1 (bop b0 (bop b0 b1)))) b0 → ⊥
  bad2184  p = false≢true (sym (cong lower p))
  cut2184 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (var 1) (op (var 3) (var 2))))) , (var 1)) → ⊥
  cut2184  adequate = bad2184  (Adequate.valid adequate Two boolean env5)
  bad2185 : PathP (λ _ → Two) (bop (bop b0 b1) (bop b1 (bop b1 (bop b0 b1)))) b1 → ⊥
  bad2185  p = false≢true (cong lower p)
  cut2185 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (var 1) (op (var 3) (var 2))))) , (var 2)) → ⊥
  cut2185  adequate = bad2185  (Adequate.valid adequate Two boolean env12)
  bad2186 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop b0 (bop b1 b0)))) b1 → ⊥
  bad2186  p = false≢true (cong lower p)
  cut2186 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (var 1) (op (var 3) (var 2))))) , (var 3)) → ⊥
  cut2186  adequate = bad2186  (Adequate.valid adequate Two boolean env3)
  bad2187 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop b0 (bop b0 b0)))) b1 → ⊥
  bad2187  p = false≢true (cong lower p)
  cut2187 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (var 1) (op (var 3) (var 2))))) , (var 4)) → ⊥
  cut2187  adequate = bad2187  (Adequate.valid adequate Two boolean env6)
  bad2188 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b1 (bop b0 (bop b0 b0)))) b0 → ⊥
  bad2188  p = false≢true (sym (cong lower p))
  cut2188 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (var 1) (op (var 3) (var 3))))) , (var 0)) → ⊥
  cut2188  adequate = bad2188  (Adequate.valid adequate Two boolean env5)
  bad2189 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b1 (bop b0 (bop b0 b0)))) b0 → ⊥
  bad2189  p = false≢true (sym (cong lower p))
  cut2189 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (var 1) (op (var 3) (var 3))))) , (var 1)) → ⊥
  cut2189  adequate = bad2189  (Adequate.valid adequate Two boolean env5)
  bad2190 : PathP (λ _ → Two) (bop (bop b0 b1) (bop b1 (bop b1 (bop b0 b0)))) b1 → ⊥
  bad2190  p = false≢true (cong lower p)
  cut2190 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (var 1) (op (var 3) (var 3))))) , (var 2)) → ⊥
  cut2190  adequate = bad2190  (Adequate.valid adequate Two boolean env12)
  bad2191 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop b0 (bop b1 b1)))) b1 → ⊥
  bad2191  p = false≢true (cong lower p)
  cut2191 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (var 1) (op (var 3) (var 3))))) , (var 3)) → ⊥
  cut2191  adequate = bad2191  (Adequate.valid adequate Two boolean env3)
  bad2192 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop b0 (bop b0 b0)))) b1 → ⊥
  bad2192  p = false≢true (cong lower p)
  cut2192 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (var 1) (op (var 3) (var 3))))) , (var 4)) → ⊥
  cut2192  adequate = bad2192  (Adequate.valid adequate Two boolean env6)
  bad2193 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b1 (bop b0 (bop b0 b0)))) b0 → ⊥
  bad2193  p = false≢true (sym (cong lower p))
  cut2193 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (var 1) (op (var 3) (var 4))))) , (var 0)) → ⊥
  cut2193  adequate = bad2193  (Adequate.valid adequate Two boolean env15)
  bad2194 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b1 (bop b0 (bop b0 b0)))) b0 → ⊥
  bad2194  p = false≢true (sym (cong lower p))
  cut2194 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (var 1) (op (var 3) (var 4))))) , (var 1)) → ⊥
  cut2194  adequate = bad2194  (Adequate.valid adequate Two boolean env15)
  bad2195 : PathP (λ _ → Two) (bop (bop b0 b1) (bop b1 (bop b1 (bop b0 b0)))) b1 → ⊥
  bad2195  p = false≢true (cong lower p)
  cut2195 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (var 1) (op (var 3) (var 4))))) , (var 2)) → ⊥
  cut2195  adequate = bad2195  (Adequate.valid adequate Two boolean env14)
  bad2196 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop b0 (bop b1 b0)))) b1 → ⊥
  bad2196  p = false≢true (cong lower p)
  cut2196 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (var 1) (op (var 3) (var 4))))) , (var 3)) → ⊥
  cut2196  adequate = bad2196  (Adequate.valid adequate Two boolean env16)
  bad2197 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop b0 (bop b0 b1)))) b1 → ⊥
  bad2197  p = false≢true (cong lower p)
  cut2197 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (var 1) (op (var 3) (var 4))))) , (var 4)) → ⊥
  cut2197  adequate = bad2197  (Adequate.valid adequate Two boolean env6)
  bad2198 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop b0 (bop b0 b0)))) b1 → ⊥
  bad2198  p = false≢true (cong lower p)
  cut2198 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (var 1) (op (var 3) (var 4))))) , (var 5)) → ⊥
  cut2198  adequate = bad2198  (Adequate.valid adequate Two boolean env17)
  bad2199 : PathP (λ _ → Two) (bop (bop b1 b0) (bop b0 (bop b0 (bop b1 b1)))) b1 → ⊥
  bad2199  p = false≢true (cong lower p)
  cut2199 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (var 2) (op (var 0) (var 0))))) , (var 0)) → ⊥
  cut2199  adequate = bad2199  (Adequate.valid adequate Two boolean env8)
  bad2200 : PathP (λ _ → Two) (bop (bop b0 b1) (bop b0 (bop b0 (bop b0 b0)))) b1 → ⊥
  bad2200  p = false≢true (cong lower p)
  cut2200 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (var 2) (op (var 0) (var 0))))) , (var 1)) → ⊥
  cut2200  adequate = bad2200  (Adequate.valid adequate Two boolean env2)
  bad2201 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b1 (bop b1 (bop b0 b0)))) b1 → ⊥
  bad2201  p = false≢true (cong lower p)
  cut2201 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (var 2) (op (var 0) (var 0))))) , (var 2)) → ⊥
  cut2201  adequate = bad2201  (Adequate.valid adequate Two boolean env1)
  bad2202 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop b0 (bop b0 b0)))) b1 → ⊥
  bad2202  p = false≢true (cong lower p)
  cut2202 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (var 2) (op (var 0) (var 0))))) , (var 3)) → ⊥
  cut2202  adequate = bad2202  (Adequate.valid adequate Two boolean env3)
  bad2203 : PathP (λ _ → Two) (bop (bop b1 b0) (bop b0 (bop b0 (bop b1 b0)))) b1 → ⊥
  bad2203  p = false≢true (cong lower p)
  cut2203 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (var 2) (op (var 0) (var 1))))) , (var 0)) → ⊥
  cut2203  adequate = bad2203  (Adequate.valid adequate Two boolean env8)
  bad2204 : PathP (λ _ → Two) (bop (bop b0 b1) (bop b0 (bop b0 (bop b0 b1)))) b1 → ⊥
  bad2204  p = false≢true (cong lower p)
  cut2204 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (var 2) (op (var 0) (var 1))))) , (var 1)) → ⊥
  cut2204  adequate = bad2204  (Adequate.valid adequate Two boolean env2)
  bad2205 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b1 (bop b1 (bop b0 b0)))) b1 → ⊥
  bad2205  p = false≢true (cong lower p)
  cut2205 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (var 2) (op (var 0) (var 1))))) , (var 2)) → ⊥
  cut2205  adequate = bad2205  (Adequate.valid adequate Two boolean env1)
  bad2206 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop b0 (bop b0 b0)))) b1 → ⊥
  bad2206  p = false≢true (cong lower p)
  cut2206 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (var 2) (op (var 0) (var 1))))) , (var 3)) → ⊥
  cut2206  adequate = bad2206  (Adequate.valid adequate Two boolean env3)
  bad2207 : PathP (λ _ → Two) (bop (bop b1 b0) (bop b0 (bop b0 (bop b1 b0)))) b1 → ⊥
  bad2207  p = false≢true (cong lower p)
  cut2207 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (var 2) (op (var 0) (var 2))))) , (var 0)) → ⊥
  cut2207  adequate = bad2207  (Adequate.valid adequate Two boolean env8)
  bad2208 : PathP (λ _ → Two) (bop (bop b0 b1) (bop b0 (bop b0 (bop b0 b0)))) b1 → ⊥
  bad2208  p = false≢true (cong lower p)
  cut2208 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (var 2) (op (var 0) (var 2))))) , (var 1)) → ⊥
  cut2208  adequate = bad2208  (Adequate.valid adequate Two boolean env2)
  bad2209 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b1 (bop b1 (bop b0 b1)))) b1 → ⊥
  bad2209  p = false≢true (cong lower p)
  cut2209 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (var 2) (op (var 0) (var 2))))) , (var 2)) → ⊥
  cut2209  adequate = bad2209  (Adequate.valid adequate Two boolean env1)
  bad2210 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop b0 (bop b0 b0)))) b1 → ⊥
  bad2210  p = false≢true (cong lower p)
  cut2210 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (var 2) (op (var 0) (var 2))))) , (var 3)) → ⊥
  cut2210  adequate = bad2210  (Adequate.valid adequate Two boolean env3)
  bad2211 : PathP (λ _ → Two) (bop (bop b1 b0) (bop b0 (bop b0 (bop b1 b0)))) b1 → ⊥
  bad2211  p = false≢true (cong lower p)
  cut2211 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (var 2) (op (var 0) (var 3))))) , (var 0)) → ⊥
  cut2211  adequate = bad2211  (Adequate.valid adequate Two boolean env9)
  bad2212 : PathP (λ _ → Two) (bop (bop b0 b1) (bop b0 (bop b0 (bop b0 b0)))) b1 → ⊥
  bad2212  p = false≢true (cong lower p)
  cut2212 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (var 2) (op (var 0) (var 3))))) , (var 1)) → ⊥
  cut2212  adequate = bad2212  (Adequate.valid adequate Two boolean env4)
  bad2213 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b1 (bop b1 (bop b0 b0)))) b1 → ⊥
  bad2213  p = false≢true (cong lower p)
  cut2213 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (var 2) (op (var 0) (var 3))))) , (var 2)) → ⊥
  cut2213  adequate = bad2213  (Adequate.valid adequate Two boolean env5)
  bad2214 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop b0 (bop b0 b1)))) b1 → ⊥
  bad2214  p = false≢true (cong lower p)
  cut2214 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (var 2) (op (var 0) (var 3))))) , (var 3)) → ⊥
  cut2214  adequate = bad2214  (Adequate.valid adequate Two boolean env3)
  bad2215 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop b0 (bop b0 b0)))) b1 → ⊥
  bad2215  p = false≢true (cong lower p)
  cut2215 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (var 2) (op (var 0) (var 3))))) , (var 4)) → ⊥
  cut2215  adequate = bad2215  (Adequate.valid adequate Two boolean env6)
  bad2216 : PathP (λ _ → Two) (bop (bop b1 b0) (bop b0 (bop b0 (bop b0 b1)))) b1 → ⊥
  bad2216  p = false≢true (cong lower p)
  cut2216 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (var 2) (op (var 1) (var 0))))) , (var 0)) → ⊥
  cut2216  adequate = bad2216  (Adequate.valid adequate Two boolean env8)
  bad2217 : PathP (λ _ → Two) (bop (bop b0 b1) (bop b0 (bop b0 (bop b1 b0)))) b1 → ⊥
  bad2217  p = false≢true (cong lower p)
  cut2217 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (var 2) (op (var 1) (var 0))))) , (var 1)) → ⊥
  cut2217  adequate = bad2217  (Adequate.valid adequate Two boolean env2)
  bad2218 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b1 (bop b1 (bop b0 b0)))) b1 → ⊥
  bad2218  p = false≢true (cong lower p)
  cut2218 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (var 2) (op (var 1) (var 0))))) , (var 2)) → ⊥
  cut2218  adequate = bad2218  (Adequate.valid adequate Two boolean env1)
  bad2219 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop b0 (bop b0 b0)))) b1 → ⊥
  bad2219  p = false≢true (cong lower p)
  cut2219 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (var 2) (op (var 1) (var 0))))) , (var 3)) → ⊥
  cut2219  adequate = bad2219  (Adequate.valid adequate Two boolean env3)
  bad2220 : PathP (λ _ → Two) (bop (bop b0 b1) (bop b1 (bop b1 (bop b1 b1)))) b0 → ⊥
  bad2220  p = false≢true (sym (cong lower p))
  cut2220 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (var 2) (op (var 1) (var 1))))) , (var 0)) → ⊥
  cut2220  adequate = bad2220  (Adequate.valid adequate Two boolean env10)
  bad2221 : PathP (λ _ → Two) (bop (bop b0 b1) (bop b0 (bop b0 (bop b1 b1)))) b1 → ⊥
  bad2221  p = false≢true (cong lower p)
  cut2221 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (var 2) (op (var 1) (var 1))))) , (var 1)) → ⊥
  cut2221  adequate = bad2221  (Adequate.valid adequate Two boolean env2)
  bad2222 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b1 (bop b1 (bop b0 b0)))) b1 → ⊥
  bad2222  p = false≢true (cong lower p)
  cut2222 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (var 2) (op (var 1) (var 1))))) , (var 2)) → ⊥
  cut2222  adequate = bad2222  (Adequate.valid adequate Two boolean env1)
  bad2223 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop b0 (bop b0 b0)))) b1 → ⊥
  bad2223  p = false≢true (cong lower p)
  cut2223 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (var 2) (op (var 1) (var 1))))) , (var 3)) → ⊥
  cut2223  adequate = bad2223  (Adequate.valid adequate Two boolean env3)
  bad2224 : PathP (λ _ → Two) (bop (bop b0 b1) (bop b1 (bop b1 (bop b1 b1)))) b0 → ⊥
  bad2224  p = false≢true (sym (cong lower p))
  cut2224 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (var 2) (op (var 1) (var 2))))) , (var 0)) → ⊥
  cut2224  adequate = bad2224  (Adequate.valid adequate Two boolean env10)
  bad2225 : PathP (λ _ → Two) (bop (bop b0 b1) (bop b0 (bop b0 (bop b1 b0)))) b1 → ⊥
  bad2225  p = false≢true (cong lower p)
  cut2225 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (var 2) (op (var 1) (var 2))))) , (var 1)) → ⊥
  cut2225  adequate = bad2225  (Adequate.valid adequate Two boolean env2)
  bad2226 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b1 (bop b1 (bop b0 b1)))) b1 → ⊥
  bad2226  p = false≢true (cong lower p)
  cut2226 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (var 2) (op (var 1) (var 2))))) , (var 2)) → ⊥
  cut2226  adequate = bad2226  (Adequate.valid adequate Two boolean env1)
  bad2227 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop b0 (bop b0 b0)))) b1 → ⊥
  bad2227  p = false≢true (cong lower p)
  cut2227 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (var 2) (op (var 1) (var 2))))) , (var 3)) → ⊥
  cut2227  adequate = bad2227  (Adequate.valid adequate Two boolean env3)
  bad2228 : PathP (λ _ → Two) (bop (bop b0 b1) (bop b1 (bop b1 (bop b1 b1)))) b0 → ⊥
  bad2228  p = false≢true (sym (cong lower p))
  cut2228 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (var 2) (op (var 1) (var 3))))) , (var 0)) → ⊥
  cut2228  adequate = bad2228  (Adequate.valid adequate Two boolean env11)
  bad2229 : PathP (λ _ → Two) (bop (bop b0 b1) (bop b0 (bop b0 (bop b1 b0)))) b1 → ⊥
  bad2229  p = false≢true (cong lower p)
  cut2229 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (var 2) (op (var 1) (var 3))))) , (var 1)) → ⊥
  cut2229  adequate = bad2229  (Adequate.valid adequate Two boolean env4)
  bad2230 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b1 (bop b1 (bop b0 b0)))) b1 → ⊥
  bad2230  p = false≢true (cong lower p)
  cut2230 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (var 2) (op (var 1) (var 3))))) , (var 2)) → ⊥
  cut2230  adequate = bad2230  (Adequate.valid adequate Two boolean env5)
  bad2231 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop b0 (bop b0 b1)))) b1 → ⊥
  bad2231  p = false≢true (cong lower p)
  cut2231 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (var 2) (op (var 1) (var 3))))) , (var 3)) → ⊥
  cut2231  adequate = bad2231  (Adequate.valid adequate Two boolean env3)
  bad2232 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop b0 (bop b0 b0)))) b1 → ⊥
  bad2232  p = false≢true (cong lower p)
  cut2232 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (var 2) (op (var 1) (var 3))))) , (var 4)) → ⊥
  cut2232  adequate = bad2232  (Adequate.valid adequate Two boolean env6)
  bad2233 : PathP (λ _ → Two) (bop (bop b1 b0) (bop b0 (bop b0 (bop b0 b1)))) b1 → ⊥
  bad2233  p = false≢true (cong lower p)
  cut2233 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (var 2) (op (var 2) (var 0))))) , (var 0)) → ⊥
  cut2233  adequate = bad2233  (Adequate.valid adequate Two boolean env8)
  bad2234 : PathP (λ _ → Two) (bop (bop b0 b1) (bop b0 (bop b0 (bop b0 b0)))) b1 → ⊥
  bad2234  p = false≢true (cong lower p)
  cut2234 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (var 2) (op (var 2) (var 0))))) , (var 1)) → ⊥
  cut2234  adequate = bad2234  (Adequate.valid adequate Two boolean env2)
  bad2235 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b1 (bop b1 (bop b1 b0)))) b1 → ⊥
  bad2235  p = false≢true (cong lower p)
  cut2235 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (var 2) (op (var 2) (var 0))))) , (var 2)) → ⊥
  cut2235  adequate = bad2235  (Adequate.valid adequate Two boolean env1)
  bad2236 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop b0 (bop b0 b0)))) b1 → ⊥
  bad2236  p = false≢true (cong lower p)
  cut2236 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (var 2) (op (var 2) (var 0))))) , (var 3)) → ⊥
  cut2236  adequate = bad2236  (Adequate.valid adequate Two boolean env3)
  bad2237 : PathP (λ _ → Two) (bop (bop b0 b1) (bop b1 (bop b1 (bop b1 b1)))) b0 → ⊥
  bad2237  p = false≢true (sym (cong lower p))
  cut2237 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (var 2) (op (var 2) (var 1))))) , (var 0)) → ⊥
  cut2237  adequate = bad2237  (Adequate.valid adequate Two boolean env10)
  bad2238 : PathP (λ _ → Two) (bop (bop b0 b1) (bop b0 (bop b0 (bop b0 b1)))) b1 → ⊥
  bad2238  p = false≢true (cong lower p)
  cut2238 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (var 2) (op (var 2) (var 1))))) , (var 1)) → ⊥
  cut2238  adequate = bad2238  (Adequate.valid adequate Two boolean env2)
  bad2239 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b1 (bop b1 (bop b1 b0)))) b1 → ⊥
  bad2239  p = false≢true (cong lower p)
  cut2239 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (var 2) (op (var 2) (var 1))))) , (var 2)) → ⊥
  cut2239  adequate = bad2239  (Adequate.valid adequate Two boolean env1)
  bad2240 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop b0 (bop b0 b0)))) b1 → ⊥
  bad2240  p = false≢true (cong lower p)
  cut2240 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (var 2) (op (var 2) (var 1))))) , (var 3)) → ⊥
  cut2240  adequate = bad2240  (Adequate.valid adequate Two boolean env3)
  bad2241 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b1 (bop b1 (bop b1 b1)))) b0 → ⊥
  bad2241  p = false≢true (sym (cong lower p))
  cut2241 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (var 2) (op (var 2) (var 2))))) , (var 0)) → ⊥
  cut2241  adequate = bad2241  (Adequate.valid adequate Two boolean env1)
  bad2242 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b1 (bop b1 (bop b1 b1)))) b0 → ⊥
  bad2242  p = false≢true (sym (cong lower p))
  cut2242 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (var 2) (op (var 2) (var 2))))) , (var 1)) → ⊥
  cut2242  adequate = bad2242  (Adequate.valid adequate Two boolean env1)
  bad2243 : PathP (λ _ → Two) (bop (bop b1 b1) (bop b0 (bop b0 (bop b0 b0)))) b0 → ⊥
  bad2243  p = false≢true (sym (cong lower p))
  cut2243 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (var 2) (op (var 2) (var 2))))) , (var 2)) → ⊥
  cut2243  adequate = bad2243  (Adequate.valid adequate Two boolean env21)
  bad2244 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop b0 (bop b0 b0)))) b1 → ⊥
  bad2244  p = false≢true (cong lower p)
  cut2244 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (var 2) (op (var 2) (var 2))))) , (var 3)) → ⊥
  cut2244  adequate = bad2244  (Adequate.valid adequate Two boolean env3)
  env22 : ℕ → Two
  env22 zero = b0
  env22 (suc zero) = b0
  env22 (suc (suc zero)) = b1
  env22 (suc (suc (suc zero))) = b1
  env22 (suc (suc (suc (suc rest)))) = b0
  bad2245 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b1 (bop b1 (bop b1 b1)))) b0 → ⊥
  bad2245  p = false≢true (sym (cong lower p))
  cut2245 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (var 2) (op (var 2) (var 3))))) , (var 0)) → ⊥
  cut2245  adequate = bad2245  (Adequate.valid adequate Two boolean env22)
  bad2246 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b1 (bop b1 (bop b1 b1)))) b0 → ⊥
  bad2246  p = false≢true (sym (cong lower p))
  cut2246 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (var 2) (op (var 2) (var 3))))) , (var 1)) → ⊥
  cut2246  adequate = bad2246  (Adequate.valid adequate Two boolean env22)
  bad2247 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b1 (bop b1 (bop b1 b0)))) b1 → ⊥
  bad2247  p = false≢true (cong lower p)
  cut2247 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (var 2) (op (var 2) (var 3))))) , (var 2)) → ⊥
  cut2247  adequate = bad2247  (Adequate.valid adequate Two boolean env5)
  bad2248 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop b0 (bop b0 b1)))) b1 → ⊥
  bad2248  p = false≢true (cong lower p)
  cut2248 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (var 2) (op (var 2) (var 3))))) , (var 3)) → ⊥
  cut2248  adequate = bad2248  (Adequate.valid adequate Two boolean env3)
  bad2249 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop b0 (bop b0 b0)))) b1 → ⊥
  bad2249  p = false≢true (cong lower p)
  cut2249 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (var 2) (op (var 2) (var 3))))) , (var 4)) → ⊥
  cut2249  adequate = bad2249  (Adequate.valid adequate Two boolean env6)
  bad2250 : PathP (λ _ → Two) (bop (bop b1 b0) (bop b0 (bop b0 (bop b0 b1)))) b1 → ⊥
  bad2250  p = false≢true (cong lower p)
  cut2250 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (var 2) (op (var 3) (var 0))))) , (var 0)) → ⊥
  cut2250  adequate = bad2250  (Adequate.valid adequate Two boolean env9)
  bad2251 : PathP (λ _ → Two) (bop (bop b0 b1) (bop b0 (bop b0 (bop b0 b0)))) b1 → ⊥
  bad2251  p = false≢true (cong lower p)
  cut2251 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (var 2) (op (var 3) (var 0))))) , (var 1)) → ⊥
  cut2251  adequate = bad2251  (Adequate.valid adequate Two boolean env4)
  bad2252 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b1 (bop b1 (bop b0 b0)))) b1 → ⊥
  bad2252  p = false≢true (cong lower p)
  cut2252 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (var 2) (op (var 3) (var 0))))) , (var 2)) → ⊥
  cut2252  adequate = bad2252  (Adequate.valid adequate Two boolean env5)
  bad2253 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop b0 (bop b1 b0)))) b1 → ⊥
  bad2253  p = false≢true (cong lower p)
  cut2253 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (var 2) (op (var 3) (var 0))))) , (var 3)) → ⊥
  cut2253  adequate = bad2253  (Adequate.valid adequate Two boolean env3)
  bad2254 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop b0 (bop b0 b0)))) b1 → ⊥
  bad2254  p = false≢true (cong lower p)
  cut2254 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (var 2) (op (var 3) (var 0))))) , (var 4)) → ⊥
  cut2254  adequate = bad2254  (Adequate.valid adequate Two boolean env6)
  bad2255 : PathP (λ _ → Two) (bop (bop b0 b1) (bop b1 (bop b1 (bop b1 b1)))) b0 → ⊥
  bad2255  p = false≢true (sym (cong lower p))
  cut2255 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (var 2) (op (var 3) (var 1))))) , (var 0)) → ⊥
  cut2255  adequate = bad2255  (Adequate.valid adequate Two boolean env11)
  bad2256 : PathP (λ _ → Two) (bop (bop b0 b1) (bop b0 (bop b0 (bop b0 b1)))) b1 → ⊥
  bad2256  p = false≢true (cong lower p)
  cut2256 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (var 2) (op (var 3) (var 1))))) , (var 1)) → ⊥
  cut2256  adequate = bad2256  (Adequate.valid adequate Two boolean env4)
  bad2257 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b1 (bop b1 (bop b0 b0)))) b1 → ⊥
  bad2257  p = false≢true (cong lower p)
  cut2257 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (var 2) (op (var 3) (var 1))))) , (var 2)) → ⊥
  cut2257  adequate = bad2257  (Adequate.valid adequate Two boolean env5)
  bad2258 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop b0 (bop b1 b0)))) b1 → ⊥
  bad2258  p = false≢true (cong lower p)
  cut2258 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (var 2) (op (var 3) (var 1))))) , (var 3)) → ⊥
  cut2258  adequate = bad2258  (Adequate.valid adequate Two boolean env3)
  bad2259 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop b0 (bop b0 b0)))) b1 → ⊥
  bad2259  p = false≢true (cong lower p)
  cut2259 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (var 2) (op (var 3) (var 1))))) , (var 4)) → ⊥
  cut2259  adequate = bad2259  (Adequate.valid adequate Two boolean env6)
  bad2260 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b1 (bop b1 (bop b1 b1)))) b0 → ⊥
  bad2260  p = false≢true (sym (cong lower p))
  cut2260 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (var 2) (op (var 3) (var 2))))) , (var 0)) → ⊥
  cut2260  adequate = bad2260  (Adequate.valid adequate Two boolean env22)
  bad2261 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b1 (bop b1 (bop b1 b1)))) b0 → ⊥
  bad2261  p = false≢true (sym (cong lower p))
  cut2261 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (var 2) (op (var 3) (var 2))))) , (var 1)) → ⊥
  cut2261  adequate = bad2261  (Adequate.valid adequate Two boolean env22)
  bad2262 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b1 (bop b1 (bop b0 b1)))) b1 → ⊥
  bad2262  p = false≢true (cong lower p)
  cut2262 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (var 2) (op (var 3) (var 2))))) , (var 2)) → ⊥
  cut2262  adequate = bad2262  (Adequate.valid adequate Two boolean env5)
  bad2263 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop b0 (bop b1 b0)))) b1 → ⊥
  bad2263  p = false≢true (cong lower p)
  cut2263 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (var 2) (op (var 3) (var 2))))) , (var 3)) → ⊥
  cut2263  adequate = bad2263  (Adequate.valid adequate Two boolean env3)
  bad2264 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop b0 (bop b0 b0)))) b1 → ⊥
  bad2264  p = false≢true (cong lower p)
  cut2264 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (var 2) (op (var 3) (var 2))))) , (var 4)) → ⊥
  cut2264  adequate = bad2264  (Adequate.valid adequate Two boolean env6)
  bad2265 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b1 (bop b1 (bop b1 b1)))) b0 → ⊥
  bad2265  p = false≢true (sym (cong lower p))
  cut2265 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (var 2) (op (var 3) (var 3))))) , (var 0)) → ⊥
  cut2265  adequate = bad2265  (Adequate.valid adequate Two boolean env22)
  bad2266 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b1 (bop b1 (bop b1 b1)))) b0 → ⊥
  bad2266  p = false≢true (sym (cong lower p))
  cut2266 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (var 2) (op (var 3) (var 3))))) , (var 1)) → ⊥
  cut2266  adequate = bad2266  (Adequate.valid adequate Two boolean env22)
  bad2267 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b1 (bop b1 (bop b0 b0)))) b1 → ⊥
  bad2267  p = false≢true (cong lower p)
  cut2267 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (var 2) (op (var 3) (var 3))))) , (var 2)) → ⊥
  cut2267  adequate = bad2267  (Adequate.valid adequate Two boolean env5)
  bad2268 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop b0 (bop b1 b1)))) b1 → ⊥
  bad2268  p = false≢true (cong lower p)
  cut2268 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (var 2) (op (var 3) (var 3))))) , (var 3)) → ⊥
  cut2268  adequate = bad2268  (Adequate.valid adequate Two boolean env3)
  bad2269 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop b0 (bop b0 b0)))) b1 → ⊥
  bad2269  p = false≢true (cong lower p)
  cut2269 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (var 2) (op (var 3) (var 3))))) , (var 4)) → ⊥
  cut2269  adequate = bad2269  (Adequate.valid adequate Two boolean env6)
  env23 : ℕ → Two
  env23 zero = b0
  env23 (suc zero) = b0
  env23 (suc (suc zero)) = b1
  env23 (suc (suc (suc zero))) = b1
  env23 (suc (suc (suc (suc zero)))) = b1
  env23 (suc (suc (suc (suc (suc rest))))) = b0
  bad2270 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b1 (bop b1 (bop b1 b1)))) b0 → ⊥
  bad2270  p = false≢true (sym (cong lower p))
  cut2270 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (var 2) (op (var 3) (var 4))))) , (var 0)) → ⊥
  cut2270  adequate = bad2270  (Adequate.valid adequate Two boolean env23)
  bad2271 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b1 (bop b1 (bop b1 b1)))) b0 → ⊥
  bad2271  p = false≢true (sym (cong lower p))
  cut2271 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (var 2) (op (var 3) (var 4))))) , (var 1)) → ⊥
  cut2271  adequate = bad2271  (Adequate.valid adequate Two boolean env23)
  bad2272 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b1 (bop b1 (bop b0 b0)))) b1 → ⊥
  bad2272  p = false≢true (cong lower p)
  cut2272 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (var 2) (op (var 3) (var 4))))) , (var 2)) → ⊥
  cut2272  adequate = bad2272  (Adequate.valid adequate Two boolean env15)
  bad2273 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop b0 (bop b1 b0)))) b1 → ⊥
  bad2273  p = false≢true (cong lower p)
  cut2273 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (var 2) (op (var 3) (var 4))))) , (var 3)) → ⊥
  cut2273  adequate = bad2273  (Adequate.valid adequate Two boolean env16)
  bad2274 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop b0 (bop b0 b1)))) b1 → ⊥
  bad2274  p = false≢true (cong lower p)
  cut2274 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (var 2) (op (var 3) (var 4))))) , (var 4)) → ⊥
  cut2274  adequate = bad2274  (Adequate.valid adequate Two boolean env6)
  bad2275 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop b0 (bop b0 b0)))) b1 → ⊥
  bad2275  p = false≢true (cong lower p)
  cut2275 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (var 2) (op (var 3) (var 4))))) , (var 5)) → ⊥
  cut2275  adequate = bad2275  (Adequate.valid adequate Two boolean env17)
  bad2276 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b1 (bop b0 (bop b0 b0)))) b0 → ⊥
  bad2276  p = false≢true (sym (cong lower p))
  cut2276 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (var 3) (op (var 0) (var 0))))) , (var 0)) → ⊥
  cut2276  adequate = bad2276  (Adequate.valid adequate Two boolean env5)
  bad2277 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b1 (bop b0 (bop b0 b0)))) b0 → ⊥
  bad2277  p = false≢true (sym (cong lower p))
  cut2277 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (var 3) (op (var 0) (var 0))))) , (var 1)) → ⊥
  cut2277  adequate = bad2277  (Adequate.valid adequate Two boolean env5)
  bad2278 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b1 (bop b1 (bop b0 b0)))) b1 → ⊥
  bad2278  p = false≢true (cong lower p)
  cut2278 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (var 3) (op (var 0) (var 0))))) , (var 2)) → ⊥
  cut2278  adequate = bad2278  (Adequate.valid adequate Two boolean env22)
  bad2279 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop b1 (bop b0 b0)))) b1 → ⊥
  bad2279  p = false≢true (cong lower p)
  cut2279 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (var 3) (op (var 0) (var 0))))) , (var 3)) → ⊥
  cut2279  adequate = bad2279  (Adequate.valid adequate Two boolean env3)
  bad2280 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop b0 (bop b0 b0)))) b1 → ⊥
  bad2280  p = false≢true (cong lower p)
  cut2280 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (var 3) (op (var 0) (var 0))))) , (var 4)) → ⊥
  cut2280  adequate = bad2280  (Adequate.valid adequate Two boolean env6)
  bad2281 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b1 (bop b0 (bop b0 b0)))) b0 → ⊥
  bad2281  p = false≢true (sym (cong lower p))
  cut2281 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (var 3) (op (var 0) (var 1))))) , (var 0)) → ⊥
  cut2281  adequate = bad2281  (Adequate.valid adequate Two boolean env5)
  bad2282 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b1 (bop b0 (bop b0 b0)))) b0 → ⊥
  bad2282  p = false≢true (sym (cong lower p))
  cut2282 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (var 3) (op (var 0) (var 1))))) , (var 1)) → ⊥
  cut2282  adequate = bad2282  (Adequate.valid adequate Two boolean env5)
  bad2283 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b1 (bop b1 (bop b0 b0)))) b1 → ⊥
  bad2283  p = false≢true (cong lower p)
  cut2283 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (var 3) (op (var 0) (var 1))))) , (var 2)) → ⊥
  cut2283  adequate = bad2283  (Adequate.valid adequate Two boolean env22)
  bad2284 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop b1 (bop b0 b0)))) b1 → ⊥
  bad2284  p = false≢true (cong lower p)
  cut2284 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (var 3) (op (var 0) (var 1))))) , (var 3)) → ⊥
  cut2284  adequate = bad2284  (Adequate.valid adequate Two boolean env3)
  bad2285 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop b0 (bop b0 b0)))) b1 → ⊥
  bad2285  p = false≢true (cong lower p)
  cut2285 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (var 3) (op (var 0) (var 1))))) , (var 4)) → ⊥
  cut2285  adequate = bad2285  (Adequate.valid adequate Two boolean env6)
  bad2286 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b1 (bop b0 (bop b0 b1)))) b0 → ⊥
  bad2286  p = false≢true (sym (cong lower p))
  cut2286 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (var 3) (op (var 0) (var 2))))) , (var 0)) → ⊥
  cut2286  adequate = bad2286  (Adequate.valid adequate Two boolean env5)
  bad2287 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b1 (bop b0 (bop b0 b1)))) b0 → ⊥
  bad2287  p = false≢true (sym (cong lower p))
  cut2287 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (var 3) (op (var 0) (var 2))))) , (var 1)) → ⊥
  cut2287  adequate = bad2287  (Adequate.valid adequate Two boolean env5)
  bad2288 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b1 (bop b1 (bop b0 b1)))) b1 → ⊥
  bad2288  p = false≢true (cong lower p)
  cut2288 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (var 3) (op (var 0) (var 2))))) , (var 2)) → ⊥
  cut2288  adequate = bad2288  (Adequate.valid adequate Two boolean env22)
  bad2289 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop b1 (bop b0 b0)))) b1 → ⊥
  bad2289  p = false≢true (cong lower p)
  cut2289 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (var 3) (op (var 0) (var 2))))) , (var 3)) → ⊥
  cut2289  adequate = bad2289  (Adequate.valid adequate Two boolean env3)
  bad2290 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop b0 (bop b0 b0)))) b1 → ⊥
  bad2290  p = false≢true (cong lower p)
  cut2290 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (var 3) (op (var 0) (var 2))))) , (var 4)) → ⊥
  cut2290  adequate = bad2290  (Adequate.valid adequate Two boolean env6)
  bad2291 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b1 (bop b0 (bop b0 b0)))) b0 → ⊥
  bad2291  p = false≢true (sym (cong lower p))
  cut2291 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (var 3) (op (var 0) (var 3))))) , (var 0)) → ⊥
  cut2291  adequate = bad2291  (Adequate.valid adequate Two boolean env5)
  bad2292 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b1 (bop b0 (bop b0 b0)))) b0 → ⊥
  bad2292  p = false≢true (sym (cong lower p))
  cut2292 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (var 3) (op (var 0) (var 3))))) , (var 1)) → ⊥
  cut2292  adequate = bad2292  (Adequate.valid adequate Two boolean env5)
  bad2293 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b1 (bop b1 (bop b0 b1)))) b1 → ⊥
  bad2293  p = false≢true (cong lower p)
  cut2293 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (var 3) (op (var 0) (var 3))))) , (var 2)) → ⊥
  cut2293  adequate = bad2293  (Adequate.valid adequate Two boolean env22)
  bad2294 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop b1 (bop b0 b1)))) b1 → ⊥
  bad2294  p = false≢true (cong lower p)
  cut2294 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (var 3) (op (var 0) (var 3))))) , (var 3)) → ⊥
  cut2294  adequate = bad2294  (Adequate.valid adequate Two boolean env3)
  bad2295 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop b0 (bop b0 b0)))) b1 → ⊥
  bad2295  p = false≢true (cong lower p)
  cut2295 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (var 3) (op (var 0) (var 3))))) , (var 4)) → ⊥
  cut2295  adequate = bad2295  (Adequate.valid adequate Two boolean env6)
  bad2296 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b1 (bop b0 (bop b0 b0)))) b0 → ⊥
  bad2296  p = false≢true (sym (cong lower p))
  cut2296 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (var 3) (op (var 0) (var 4))))) , (var 0)) → ⊥
  cut2296  adequate = bad2296  (Adequate.valid adequate Two boolean env15)
  bad2297 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b1 (bop b0 (bop b0 b0)))) b0 → ⊥
  bad2297  p = false≢true (sym (cong lower p))
  cut2297 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (var 3) (op (var 0) (var 4))))) , (var 1)) → ⊥
  cut2297  adequate = bad2297  (Adequate.valid adequate Two boolean env15)
  env24 : ℕ → Two
  env24 zero = b0
  env24 (suc zero) = b0
  env24 (suc (suc zero)) = b1
  env24 (suc (suc (suc zero))) = b1
  env24 (suc (suc (suc (suc zero)))) = b0
  env24 (suc (suc (suc (suc (suc rest))))) = b0
  bad2298 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b1 (bop b1 (bop b0 b0)))) b1 → ⊥
  bad2298  p = false≢true (cong lower p)
  cut2298 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (var 3) (op (var 0) (var 4))))) , (var 2)) → ⊥
  cut2298  adequate = bad2298  (Adequate.valid adequate Two boolean env24)
  bad2299 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop b1 (bop b0 b0)))) b1 → ⊥
  bad2299  p = false≢true (cong lower p)
  cut2299 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (var 3) (op (var 0) (var 4))))) , (var 3)) → ⊥
  cut2299  adequate = bad2299  (Adequate.valid adequate Two boolean env16)
  bad2300 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop b0 (bop b0 b1)))) b1 → ⊥
  bad2300  p = false≢true (cong lower p)
  cut2300 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (var 3) (op (var 0) (var 4))))) , (var 4)) → ⊥
  cut2300  adequate = bad2300  (Adequate.valid adequate Two boolean env6)
  bad2301 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop b0 (bop b0 b0)))) b1 → ⊥
  bad2301  p = false≢true (cong lower p)
  cut2301 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (var 3) (op (var 0) (var 4))))) , (var 5)) → ⊥
  cut2301  adequate = bad2301  (Adequate.valid adequate Two boolean env17)
  bad2302 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b1 (bop b0 (bop b0 b0)))) b0 → ⊥
  bad2302  p = false≢true (sym (cong lower p))
  cut2302 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (var 3) (op (var 1) (var 0))))) , (var 0)) → ⊥
  cut2302  adequate = bad2302  (Adequate.valid adequate Two boolean env5)
  bad2303 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b1 (bop b0 (bop b0 b0)))) b0 → ⊥
  bad2303  p = false≢true (sym (cong lower p))
  cut2303 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (var 3) (op (var 1) (var 0))))) , (var 1)) → ⊥
  cut2303  adequate = bad2303  (Adequate.valid adequate Two boolean env5)
  bad2304 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b1 (bop b1 (bop b0 b0)))) b1 → ⊥
  bad2304  p = false≢true (cong lower p)
  cut2304 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (var 3) (op (var 1) (var 0))))) , (var 2)) → ⊥
  cut2304  adequate = bad2304  (Adequate.valid adequate Two boolean env22)
  bad2305 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop b1 (bop b0 b0)))) b1 → ⊥
  bad2305  p = false≢true (cong lower p)
  cut2305 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (var 3) (op (var 1) (var 0))))) , (var 3)) → ⊥
  cut2305  adequate = bad2305  (Adequate.valid adequate Two boolean env3)
  bad2306 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop b0 (bop b0 b0)))) b1 → ⊥
  bad2306  p = false≢true (cong lower p)
  cut2306 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (var 3) (op (var 1) (var 0))))) , (var 4)) → ⊥
  cut2306  adequate = bad2306  (Adequate.valid adequate Two boolean env6)
  bad2307 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b1 (bop b0 (bop b0 b0)))) b0 → ⊥
  bad2307  p = false≢true (sym (cong lower p))
  cut2307 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (var 3) (op (var 1) (var 1))))) , (var 0)) → ⊥
  cut2307  adequate = bad2307  (Adequate.valid adequate Two boolean env5)
  bad2308 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b1 (bop b0 (bop b0 b0)))) b0 → ⊥
  bad2308  p = false≢true (sym (cong lower p))
  cut2308 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (var 3) (op (var 1) (var 1))))) , (var 1)) → ⊥
  cut2308  adequate = bad2308  (Adequate.valid adequate Two boolean env5)
  bad2309 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b1 (bop b1 (bop b0 b0)))) b1 → ⊥
  bad2309  p = false≢true (cong lower p)
  cut2309 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (var 3) (op (var 1) (var 1))))) , (var 2)) → ⊥
  cut2309  adequate = bad2309  (Adequate.valid adequate Two boolean env22)
  bad2310 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop b1 (bop b0 b0)))) b1 → ⊥
  bad2310  p = false≢true (cong lower p)
  cut2310 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (var 3) (op (var 1) (var 1))))) , (var 3)) → ⊥
  cut2310  adequate = bad2310  (Adequate.valid adequate Two boolean env3)
  bad2311 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop b0 (bop b0 b0)))) b1 → ⊥
  bad2311  p = false≢true (cong lower p)
  cut2311 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (var 3) (op (var 1) (var 1))))) , (var 4)) → ⊥
  cut2311  adequate = bad2311  (Adequate.valid adequate Two boolean env6)
  bad2312 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b1 (bop b0 (bop b0 b1)))) b0 → ⊥
  bad2312  p = false≢true (sym (cong lower p))
  cut2312 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (var 3) (op (var 1) (var 2))))) , (var 0)) → ⊥
  cut2312  adequate = bad2312  (Adequate.valid adequate Two boolean env5)
  bad2313 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b1 (bop b0 (bop b0 b1)))) b0 → ⊥
  bad2313  p = false≢true (sym (cong lower p))
  cut2313 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (var 3) (op (var 1) (var 2))))) , (var 1)) → ⊥
  cut2313  adequate = bad2313  (Adequate.valid adequate Two boolean env5)
  bad2314 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b1 (bop b1 (bop b0 b1)))) b1 → ⊥
  bad2314  p = false≢true (cong lower p)
  cut2314 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (var 3) (op (var 1) (var 2))))) , (var 2)) → ⊥
  cut2314  adequate = bad2314  (Adequate.valid adequate Two boolean env22)
  bad2315 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop b1 (bop b0 b0)))) b1 → ⊥
  bad2315  p = false≢true (cong lower p)
  cut2315 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (var 3) (op (var 1) (var 2))))) , (var 3)) → ⊥
  cut2315  adequate = bad2315  (Adequate.valid adequate Two boolean env3)
  bad2316 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop b0 (bop b0 b0)))) b1 → ⊥
  bad2316  p = false≢true (cong lower p)
  cut2316 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (var 3) (op (var 1) (var 2))))) , (var 4)) → ⊥
  cut2316  adequate = bad2316  (Adequate.valid adequate Two boolean env6)
  bad2317 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b1 (bop b0 (bop b0 b0)))) b0 → ⊥
  bad2317  p = false≢true (sym (cong lower p))
  cut2317 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (var 3) (op (var 1) (var 3))))) , (var 0)) → ⊥
  cut2317  adequate = bad2317  (Adequate.valid adequate Two boolean env5)
  bad2318 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b1 (bop b0 (bop b0 b0)))) b0 → ⊥
  bad2318  p = false≢true (sym (cong lower p))
  cut2318 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (var 3) (op (var 1) (var 3))))) , (var 1)) → ⊥
  cut2318  adequate = bad2318  (Adequate.valid adequate Two boolean env5)
  bad2319 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b1 (bop b1 (bop b0 b1)))) b1 → ⊥
  bad2319  p = false≢true (cong lower p)
  cut2319 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (var 3) (op (var 1) (var 3))))) , (var 2)) → ⊥
  cut2319  adequate = bad2319  (Adequate.valid adequate Two boolean env22)
  bad2320 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop b1 (bop b0 b1)))) b1 → ⊥
  bad2320  p = false≢true (cong lower p)
  cut2320 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (var 3) (op (var 1) (var 3))))) , (var 3)) → ⊥
  cut2320  adequate = bad2320  (Adequate.valid adequate Two boolean env3)
  bad2321 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop b0 (bop b0 b0)))) b1 → ⊥
  bad2321  p = false≢true (cong lower p)
  cut2321 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (var 3) (op (var 1) (var 3))))) , (var 4)) → ⊥
  cut2321  adequate = bad2321  (Adequate.valid adequate Two boolean env6)
  bad2322 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b1 (bop b0 (bop b0 b0)))) b0 → ⊥
  bad2322  p = false≢true (sym (cong lower p))
  cut2322 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (var 3) (op (var 1) (var 4))))) , (var 0)) → ⊥
  cut2322  adequate = bad2322  (Adequate.valid adequate Two boolean env15)
  bad2323 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b1 (bop b0 (bop b0 b0)))) b0 → ⊥
  bad2323  p = false≢true (sym (cong lower p))
  cut2323 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (var 3) (op (var 1) (var 4))))) , (var 1)) → ⊥
  cut2323  adequate = bad2323  (Adequate.valid adequate Two boolean env15)
  bad2324 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b1 (bop b1 (bop b0 b0)))) b1 → ⊥
  bad2324  p = false≢true (cong lower p)
  cut2324 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (var 3) (op (var 1) (var 4))))) , (var 2)) → ⊥
  cut2324  adequate = bad2324  (Adequate.valid adequate Two boolean env24)
  bad2325 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop b1 (bop b0 b0)))) b1 → ⊥
  bad2325  p = false≢true (cong lower p)
  cut2325 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (var 3) (op (var 1) (var 4))))) , (var 3)) → ⊥
  cut2325  adequate = bad2325  (Adequate.valid adequate Two boolean env16)
  bad2326 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop b0 (bop b0 b1)))) b1 → ⊥
  bad2326  p = false≢true (cong lower p)
  cut2326 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (var 3) (op (var 1) (var 4))))) , (var 4)) → ⊥
  cut2326  adequate = bad2326  (Adequate.valid adequate Two boolean env6)
  bad2327 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop b0 (bop b0 b0)))) b1 → ⊥
  bad2327  p = false≢true (cong lower p)
  cut2327 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (var 3) (op (var 1) (var 4))))) , (var 5)) → ⊥
  cut2327  adequate = bad2327  (Adequate.valid adequate Two boolean env17)
  bad2328 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b1 (bop b0 (bop b1 b0)))) b0 → ⊥
  bad2328  p = false≢true (sym (cong lower p))
  cut2328 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (var 3) (op (var 2) (var 0))))) , (var 0)) → ⊥
  cut2328  adequate = bad2328  (Adequate.valid adequate Two boolean env5)
  bad2329 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b1 (bop b0 (bop b1 b0)))) b0 → ⊥
  bad2329  p = false≢true (sym (cong lower p))
  cut2329 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (var 3) (op (var 2) (var 0))))) , (var 1)) → ⊥
  cut2329  adequate = bad2329  (Adequate.valid adequate Two boolean env5)
  bad2330 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b1 (bop b1 (bop b1 b0)))) b1 → ⊥
  bad2330  p = false≢true (cong lower p)
  cut2330 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (var 3) (op (var 2) (var 0))))) , (var 2)) → ⊥
  cut2330  adequate = bad2330  (Adequate.valid adequate Two boolean env22)
  bad2331 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop b1 (bop b0 b0)))) b1 → ⊥
  bad2331  p = false≢true (cong lower p)
  cut2331 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (var 3) (op (var 2) (var 0))))) , (var 3)) → ⊥
  cut2331  adequate = bad2331  (Adequate.valid adequate Two boolean env3)
  bad2332 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop b0 (bop b0 b0)))) b1 → ⊥
  bad2332  p = false≢true (cong lower p)
  cut2332 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (var 3) (op (var 2) (var 0))))) , (var 4)) → ⊥
  cut2332  adequate = bad2332  (Adequate.valid adequate Two boolean env6)
  bad2333 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b1 (bop b0 (bop b1 b0)))) b0 → ⊥
  bad2333  p = false≢true (sym (cong lower p))
  cut2333 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (var 3) (op (var 2) (var 1))))) , (var 0)) → ⊥
  cut2333  adequate = bad2333  (Adequate.valid adequate Two boolean env5)
  bad2334 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b1 (bop b0 (bop b1 b0)))) b0 → ⊥
  bad2334  p = false≢true (sym (cong lower p))
  cut2334 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (var 3) (op (var 2) (var 1))))) , (var 1)) → ⊥
  cut2334  adequate = bad2334  (Adequate.valid adequate Two boolean env5)
  bad2335 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b1 (bop b1 (bop b1 b0)))) b1 → ⊥
  bad2335  p = false≢true (cong lower p)
  cut2335 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (var 3) (op (var 2) (var 1))))) , (var 2)) → ⊥
  cut2335  adequate = bad2335  (Adequate.valid adequate Two boolean env22)
  bad2336 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop b1 (bop b0 b0)))) b1 → ⊥
  bad2336  p = false≢true (cong lower p)
  cut2336 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (var 3) (op (var 2) (var 1))))) , (var 3)) → ⊥
  cut2336  adequate = bad2336  (Adequate.valid adequate Two boolean env3)
  bad2337 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop b0 (bop b0 b0)))) b1 → ⊥
  bad2337  p = false≢true (cong lower p)
  cut2337 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (var 3) (op (var 2) (var 1))))) , (var 4)) → ⊥
  cut2337  adequate = bad2337  (Adequate.valid adequate Two boolean env6)
  bad2338 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b1 (bop b0 (bop b1 b1)))) b0 → ⊥
  bad2338  p = false≢true (sym (cong lower p))
  cut2338 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (var 3) (op (var 2) (var 2))))) , (var 0)) → ⊥
  cut2338  adequate = bad2338  (Adequate.valid adequate Two boolean env5)
  bad2339 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b1 (bop b0 (bop b1 b1)))) b0 → ⊥
  bad2339  p = false≢true (sym (cong lower p))
  cut2339 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (var 3) (op (var 2) (var 2))))) , (var 1)) → ⊥
  cut2339  adequate = bad2339  (Adequate.valid adequate Two boolean env5)
  env25 : ℕ → Two
  env25 zero = b1
  env25 (suc zero) = b1
  env25 (suc (suc zero)) = b0
  env25 (suc (suc (suc zero))) = b0
  env25 (suc (suc (suc (suc rest)))) = b0
  bad2340 : PathP (λ _ → Two) (bop (bop b1 b1) (bop b0 (bop b0 (bop b0 b0)))) b0 → ⊥
  bad2340  p = false≢true (sym (cong lower p))
  cut2340 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (var 3) (op (var 2) (var 2))))) , (var 2)) → ⊥
  cut2340  adequate = bad2340  (Adequate.valid adequate Two boolean env25)
  bad2341 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop b1 (bop b0 b0)))) b1 → ⊥
  bad2341  p = false≢true (cong lower p)
  cut2341 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (var 3) (op (var 2) (var 2))))) , (var 3)) → ⊥
  cut2341  adequate = bad2341  (Adequate.valid adequate Two boolean env3)
  bad2342 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop b0 (bop b0 b0)))) b1 → ⊥
  bad2342  p = false≢true (cong lower p)
  cut2342 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (var 3) (op (var 2) (var 2))))) , (var 4)) → ⊥
  cut2342  adequate = bad2342  (Adequate.valid adequate Two boolean env6)
  bad2343 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b1 (bop b0 (bop b1 b0)))) b0 → ⊥
  bad2343  p = false≢true (sym (cong lower p))
  cut2343 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (var 3) (op (var 2) (var 3))))) , (var 0)) → ⊥
  cut2343  adequate = bad2343  (Adequate.valid adequate Two boolean env5)
  bad2344 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b1 (bop b0 (bop b1 b0)))) b0 → ⊥
  bad2344  p = false≢true (sym (cong lower p))
  cut2344 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (var 3) (op (var 2) (var 3))))) , (var 1)) → ⊥
  cut2344  adequate = bad2344  (Adequate.valid adequate Two boolean env5)
  bad2345 : PathP (λ _ → Two) (bop (bop b1 b1) (bop b0 (bop b0 (bop b0 b0)))) b0 → ⊥
  bad2345  p = false≢true (sym (cong lower p))
  cut2345 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (var 3) (op (var 2) (var 3))))) , (var 2)) → ⊥
  cut2345  adequate = bad2345  (Adequate.valid adequate Two boolean env25)
  bad2346 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop b1 (bop b0 b1)))) b1 → ⊥
  bad2346  p = false≢true (cong lower p)
  cut2346 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (var 3) (op (var 2) (var 3))))) , (var 3)) → ⊥
  cut2346  adequate = bad2346  (Adequate.valid adequate Two boolean env3)
  bad2347 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop b0 (bop b0 b0)))) b1 → ⊥
  bad2347  p = false≢true (cong lower p)
  cut2347 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (var 3) (op (var 2) (var 3))))) , (var 4)) → ⊥
  cut2347  adequate = bad2347  (Adequate.valid adequate Two boolean env6)
  bad2348 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b1 (bop b0 (bop b1 b0)))) b0 → ⊥
  bad2348  p = false≢true (sym (cong lower p))
  cut2348 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (var 3) (op (var 2) (var 4))))) , (var 0)) → ⊥
  cut2348  adequate = bad2348  (Adequate.valid adequate Two boolean env15)
  bad2349 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b1 (bop b0 (bop b1 b0)))) b0 → ⊥
  bad2349  p = false≢true (sym (cong lower p))
  cut2349 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (var 3) (op (var 2) (var 4))))) , (var 1)) → ⊥
  cut2349  adequate = bad2349  (Adequate.valid adequate Two boolean env15)
  bad2350 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b1 (bop b1 (bop b1 b0)))) b1 → ⊥
  bad2350  p = false≢true (cong lower p)
  cut2350 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (var 3) (op (var 2) (var 4))))) , (var 2)) → ⊥
  cut2350  adequate = bad2350  (Adequate.valid adequate Two boolean env24)
  bad2351 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop b1 (bop b0 b0)))) b1 → ⊥
  bad2351  p = false≢true (cong lower p)
  cut2351 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (var 3) (op (var 2) (var 4))))) , (var 3)) → ⊥
  cut2351  adequate = bad2351  (Adequate.valid adequate Two boolean env16)
  bad2352 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop b0 (bop b0 b1)))) b1 → ⊥
  bad2352  p = false≢true (cong lower p)
  cut2352 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (var 3) (op (var 2) (var 4))))) , (var 4)) → ⊥
  cut2352  adequate = bad2352  (Adequate.valid adequate Two boolean env6)
  bad2353 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop b0 (bop b0 b0)))) b1 → ⊥
  bad2353  p = false≢true (cong lower p)
  cut2353 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (var 3) (op (var 2) (var 4))))) , (var 5)) → ⊥
  cut2353  adequate = bad2353  (Adequate.valid adequate Two boolean env17)
  bad2354 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b1 (bop b0 (bop b0 b0)))) b0 → ⊥
  bad2354  p = false≢true (sym (cong lower p))
  cut2354 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (var 3) (op (var 3) (var 0))))) , (var 0)) → ⊥
  cut2354  adequate = bad2354  (Adequate.valid adequate Two boolean env5)
  bad2355 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b1 (bop b0 (bop b0 b0)))) b0 → ⊥
  bad2355  p = false≢true (sym (cong lower p))
  cut2355 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (var 3) (op (var 3) (var 0))))) , (var 1)) → ⊥
  cut2355  adequate = bad2355  (Adequate.valid adequate Two boolean env5)
  bad2356 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b1 (bop b1 (bop b1 b0)))) b1 → ⊥
  bad2356  p = false≢true (cong lower p)
  cut2356 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (var 3) (op (var 3) (var 0))))) , (var 2)) → ⊥
  cut2356  adequate = bad2356  (Adequate.valid adequate Two boolean env22)
  bad2357 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop b1 (bop b1 b0)))) b1 → ⊥
  bad2357  p = false≢true (cong lower p)
  cut2357 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (var 3) (op (var 3) (var 0))))) , (var 3)) → ⊥
  cut2357  adequate = bad2357  (Adequate.valid adequate Two boolean env3)
  bad2358 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop b0 (bop b0 b0)))) b1 → ⊥
  bad2358  p = false≢true (cong lower p)
  cut2358 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (var 3) (op (var 3) (var 0))))) , (var 4)) → ⊥
  cut2358  adequate = bad2358  (Adequate.valid adequate Two boolean env6)
  bad2359 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b1 (bop b0 (bop b0 b0)))) b0 → ⊥
  bad2359  p = false≢true (sym (cong lower p))
  cut2359 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (var 3) (op (var 3) (var 1))))) , (var 0)) → ⊥
  cut2359  adequate = bad2359  (Adequate.valid adequate Two boolean env5)
  bad2360 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b1 (bop b0 (bop b0 b0)))) b0 → ⊥
  bad2360  p = false≢true (sym (cong lower p))
  cut2360 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (var 3) (op (var 3) (var 1))))) , (var 1)) → ⊥
  cut2360  adequate = bad2360  (Adequate.valid adequate Two boolean env5)
  bad2361 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b1 (bop b1 (bop b1 b0)))) b1 → ⊥
  bad2361  p = false≢true (cong lower p)
  cut2361 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (var 3) (op (var 3) (var 1))))) , (var 2)) → ⊥
  cut2361  adequate = bad2361  (Adequate.valid adequate Two boolean env22)
  bad2362 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop b1 (bop b1 b0)))) b1 → ⊥
  bad2362  p = false≢true (cong lower p)
  cut2362 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (var 3) (op (var 3) (var 1))))) , (var 3)) → ⊥
  cut2362  adequate = bad2362  (Adequate.valid adequate Two boolean env3)
  bad2363 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop b0 (bop b0 b0)))) b1 → ⊥
  bad2363  p = false≢true (cong lower p)
  cut2363 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (var 3) (op (var 3) (var 1))))) , (var 4)) → ⊥
  cut2363  adequate = bad2363  (Adequate.valid adequate Two boolean env6)
  bad2364 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b1 (bop b0 (bop b0 b1)))) b0 → ⊥
  bad2364  p = false≢true (sym (cong lower p))
  cut2364 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (var 3) (op (var 3) (var 2))))) , (var 0)) → ⊥
  cut2364  adequate = bad2364  (Adequate.valid adequate Two boolean env5)
  bad2365 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b1 (bop b0 (bop b0 b1)))) b0 → ⊥
  bad2365  p = false≢true (sym (cong lower p))
  cut2365 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (var 3) (op (var 3) (var 2))))) , (var 1)) → ⊥
  cut2365  adequate = bad2365  (Adequate.valid adequate Two boolean env5)
  bad2366 : PathP (λ _ → Two) (bop (bop b1 b1) (bop b0 (bop b0 (bop b0 b0)))) b0 → ⊥
  bad2366  p = false≢true (sym (cong lower p))
  cut2366 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (var 3) (op (var 3) (var 2))))) , (var 2)) → ⊥
  cut2366  adequate = bad2366  (Adequate.valid adequate Two boolean env25)
  bad2367 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop b1 (bop b1 b0)))) b1 → ⊥
  bad2367  p = false≢true (cong lower p)
  cut2367 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (var 3) (op (var 3) (var 2))))) , (var 3)) → ⊥
  cut2367  adequate = bad2367  (Adequate.valid adequate Two boolean env3)
  bad2368 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop b0 (bop b0 b0)))) b1 → ⊥
  bad2368  p = false≢true (cong lower p)
  cut2368 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (var 3) (op (var 3) (var 2))))) , (var 4)) → ⊥
  cut2368  adequate = bad2368  (Adequate.valid adequate Two boolean env6)
  bad2369 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b1 (bop b0 (bop b0 b0)))) b0 → ⊥
  bad2369  p = false≢true (sym (cong lower p))
  cut2369 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (var 3) (op (var 3) (var 3))))) , (var 0)) → ⊥
  cut2369  adequate = bad2369  (Adequate.valid adequate Two boolean env5)
  bad2370 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b1 (bop b0 (bop b0 b0)))) b0 → ⊥
  bad2370  p = false≢true (sym (cong lower p))
  cut2370 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (var 3) (op (var 3) (var 3))))) , (var 1)) → ⊥
  cut2370  adequate = bad2370  (Adequate.valid adequate Two boolean env5)
  bad2371 : PathP (λ _ → Two) (bop (bop b1 b1) (bop b0 (bop b0 (bop b0 b0)))) b0 → ⊥
  bad2371  p = false≢true (sym (cong lower p))
  cut2371 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (var 3) (op (var 3) (var 3))))) , (var 2)) → ⊥
  cut2371  adequate = bad2371  (Adequate.valid adequate Two boolean env25)
  bad2372 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop b1 (bop b1 b1)))) b1 → ⊥
  bad2372  p = false≢true (cong lower p)
  cut2372 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (var 3) (op (var 3) (var 3))))) , (var 3)) → ⊥
  cut2372  adequate = bad2372  (Adequate.valid adequate Two boolean env3)
  bad2373 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop b0 (bop b0 b0)))) b1 → ⊥
  bad2373  p = false≢true (cong lower p)
  cut2373 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (var 3) (op (var 3) (var 3))))) , (var 4)) → ⊥
  cut2373  adequate = bad2373  (Adequate.valid adequate Two boolean env6)
  bad2374 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b1 (bop b0 (bop b0 b0)))) b0 → ⊥
  bad2374  p = false≢true (sym (cong lower p))
  cut2374 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (var 3) (op (var 3) (var 4))))) , (var 0)) → ⊥
  cut2374  adequate = bad2374  (Adequate.valid adequate Two boolean env15)
  bad2375 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b1 (bop b0 (bop b0 b0)))) b0 → ⊥
  bad2375  p = false≢true (sym (cong lower p))
  cut2375 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (var 3) (op (var 3) (var 4))))) , (var 1)) → ⊥
  cut2375  adequate = bad2375  (Adequate.valid adequate Two boolean env15)
  bad2376 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b1 (bop b1 (bop b1 b0)))) b1 → ⊥
  bad2376  p = false≢true (cong lower p)
  cut2376 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (var 3) (op (var 3) (var 4))))) , (var 2)) → ⊥
  cut2376  adequate = bad2376  (Adequate.valid adequate Two boolean env24)
  bad2377 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop b1 (bop b1 b0)))) b1 → ⊥
  bad2377  p = false≢true (cong lower p)
  cut2377 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (var 3) (op (var 3) (var 4))))) , (var 3)) → ⊥
  cut2377  adequate = bad2377  (Adequate.valid adequate Two boolean env16)
  bad2378 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop b0 (bop b0 b1)))) b1 → ⊥
  bad2378  p = false≢true (cong lower p)
  cut2378 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (var 3) (op (var 3) (var 4))))) , (var 4)) → ⊥
  cut2378  adequate = bad2378  (Adequate.valid adequate Two boolean env6)
  bad2379 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop b0 (bop b0 b0)))) b1 → ⊥
  bad2379  p = false≢true (cong lower p)
  cut2379 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (var 3) (op (var 3) (var 4))))) , (var 5)) → ⊥
  cut2379  adequate = bad2379  (Adequate.valid adequate Two boolean env17)
  bad2380 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b1 (bop b0 (bop b0 b0)))) b0 → ⊥
  bad2380  p = false≢true (sym (cong lower p))
  cut2380 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (var 3) (op (var 4) (var 0))))) , (var 0)) → ⊥
  cut2380  adequate = bad2380  (Adequate.valid adequate Two boolean env15)
  bad2381 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b1 (bop b0 (bop b0 b0)))) b0 → ⊥
  bad2381  p = false≢true (sym (cong lower p))
  cut2381 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (var 3) (op (var 4) (var 0))))) , (var 1)) → ⊥
  cut2381  adequate = bad2381  (Adequate.valid adequate Two boolean env15)
  bad2382 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b1 (bop b1 (bop b0 b0)))) b1 → ⊥
  bad2382  p = false≢true (cong lower p)
  cut2382 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (var 3) (op (var 4) (var 0))))) , (var 2)) → ⊥
  cut2382  adequate = bad2382  (Adequate.valid adequate Two boolean env24)
  bad2383 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop b1 (bop b0 b0)))) b1 → ⊥
  bad2383  p = false≢true (cong lower p)
  cut2383 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (var 3) (op (var 4) (var 0))))) , (var 3)) → ⊥
  cut2383  adequate = bad2383  (Adequate.valid adequate Two boolean env16)
  bad2384 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop b0 (bop b1 b0)))) b1 → ⊥
  bad2384  p = false≢true (cong lower p)
  cut2384 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (var 3) (op (var 4) (var 0))))) , (var 4)) → ⊥
  cut2384  adequate = bad2384  (Adequate.valid adequate Two boolean env6)
  bad2385 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop b0 (bop b0 b0)))) b1 → ⊥
  bad2385  p = false≢true (cong lower p)
  cut2385 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (var 3) (op (var 4) (var 0))))) , (var 5)) → ⊥
  cut2385  adequate = bad2385  (Adequate.valid adequate Two boolean env17)
  bad2386 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b1 (bop b0 (bop b0 b0)))) b0 → ⊥
  bad2386  p = false≢true (sym (cong lower p))
  cut2386 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (var 3) (op (var 4) (var 1))))) , (var 0)) → ⊥
  cut2386  adequate = bad2386  (Adequate.valid adequate Two boolean env15)
  bad2387 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b1 (bop b0 (bop b0 b0)))) b0 → ⊥
  bad2387  p = false≢true (sym (cong lower p))
  cut2387 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (var 3) (op (var 4) (var 1))))) , (var 1)) → ⊥
  cut2387  adequate = bad2387  (Adequate.valid adequate Two boolean env15)
  bad2388 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b1 (bop b1 (bop b0 b0)))) b1 → ⊥
  bad2388  p = false≢true (cong lower p)
  cut2388 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (var 3) (op (var 4) (var 1))))) , (var 2)) → ⊥
  cut2388  adequate = bad2388  (Adequate.valid adequate Two boolean env24)
  bad2389 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop b1 (bop b0 b0)))) b1 → ⊥
  bad2389  p = false≢true (cong lower p)
  cut2389 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (var 3) (op (var 4) (var 1))))) , (var 3)) → ⊥
  cut2389  adequate = bad2389  (Adequate.valid adequate Two boolean env16)
  bad2390 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop b0 (bop b1 b0)))) b1 → ⊥
  bad2390  p = false≢true (cong lower p)
  cut2390 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (var 3) (op (var 4) (var 1))))) , (var 4)) → ⊥
  cut2390  adequate = bad2390  (Adequate.valid adequate Two boolean env6)
  bad2391 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop b0 (bop b0 b0)))) b1 → ⊥
  bad2391  p = false≢true (cong lower p)
  cut2391 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (var 3) (op (var 4) (var 1))))) , (var 5)) → ⊥
  cut2391  adequate = bad2391  (Adequate.valid adequate Two boolean env17)
  bad2392 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b1 (bop b0 (bop b0 b1)))) b0 → ⊥
  bad2392  p = false≢true (sym (cong lower p))
  cut2392 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (var 3) (op (var 4) (var 2))))) , (var 0)) → ⊥
  cut2392  adequate = bad2392  (Adequate.valid adequate Two boolean env15)
  bad2393 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b1 (bop b0 (bop b0 b1)))) b0 → ⊥
  bad2393  p = false≢true (sym (cong lower p))
  cut2393 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (var 3) (op (var 4) (var 2))))) , (var 1)) → ⊥
  cut2393  adequate = bad2393  (Adequate.valid adequate Two boolean env15)
  bad2394 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b1 (bop b1 (bop b0 b1)))) b1 → ⊥
  bad2394  p = false≢true (cong lower p)
  cut2394 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (var 3) (op (var 4) (var 2))))) , (var 2)) → ⊥
  cut2394  adequate = bad2394  (Adequate.valid adequate Two boolean env24)
  bad2395 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop b1 (bop b0 b0)))) b1 → ⊥
  bad2395  p = false≢true (cong lower p)
  cut2395 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (var 3) (op (var 4) (var 2))))) , (var 3)) → ⊥
  cut2395  adequate = bad2395  (Adequate.valid adequate Two boolean env16)
  bad2396 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop b0 (bop b1 b0)))) b1 → ⊥
  bad2396  p = false≢true (cong lower p)
  cut2396 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (var 3) (op (var 4) (var 2))))) , (var 4)) → ⊥
  cut2396  adequate = bad2396  (Adequate.valid adequate Two boolean env6)
  bad2397 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop b0 (bop b0 b0)))) b1 → ⊥
  bad2397  p = false≢true (cong lower p)
  cut2397 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (var 3) (op (var 4) (var 2))))) , (var 5)) → ⊥
  cut2397  adequate = bad2397  (Adequate.valid adequate Two boolean env17)
  bad2398 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b1 (bop b0 (bop b0 b0)))) b0 → ⊥
  bad2398  p = false≢true (sym (cong lower p))
  cut2398 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (var 3) (op (var 4) (var 3))))) , (var 0)) → ⊥
  cut2398  adequate = bad2398  (Adequate.valid adequate Two boolean env15)
  bad2399 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b1 (bop b0 (bop b0 b0)))) b0 → ⊥
  bad2399  p = false≢true (sym (cong lower p))
  cut2399 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (var 3) (op (var 4) (var 3))))) , (var 1)) → ⊥
  cut2399  adequate = bad2399  (Adequate.valid adequate Two boolean env15)
  bad2400 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b1 (bop b1 (bop b0 b1)))) b1 → ⊥
  bad2400  p = false≢true (cong lower p)
  cut2400 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (var 3) (op (var 4) (var 3))))) , (var 2)) → ⊥
  cut2400  adequate = bad2400  (Adequate.valid adequate Two boolean env24)
  bad2401 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop b1 (bop b0 b1)))) b1 → ⊥
  bad2401  p = false≢true (cong lower p)
  cut2401 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (var 3) (op (var 4) (var 3))))) , (var 3)) → ⊥
  cut2401  adequate = bad2401  (Adequate.valid adequate Two boolean env16)
  bad2402 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop b0 (bop b1 b0)))) b1 → ⊥
  bad2402  p = false≢true (cong lower p)
  cut2402 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (var 3) (op (var 4) (var 3))))) , (var 4)) → ⊥
  cut2402  adequate = bad2402  (Adequate.valid adequate Two boolean env6)
  bad2403 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop b0 (bop b0 b0)))) b1 → ⊥
  bad2403  p = false≢true (cong lower p)
  cut2403 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (var 3) (op (var 4) (var 3))))) , (var 5)) → ⊥
  cut2403  adequate = bad2403  (Adequate.valid adequate Two boolean env17)
  bad2404 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b1 (bop b0 (bop b0 b0)))) b0 → ⊥
  bad2404  p = false≢true (sym (cong lower p))
  cut2404 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (var 3) (op (var 4) (var 4))))) , (var 0)) → ⊥
  cut2404  adequate = bad2404  (Adequate.valid adequate Two boolean env15)
  bad2405 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b1 (bop b0 (bop b0 b0)))) b0 → ⊥
  bad2405  p = false≢true (sym (cong lower p))
  cut2405 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (var 3) (op (var 4) (var 4))))) , (var 1)) → ⊥
  cut2405  adequate = bad2405  (Adequate.valid adequate Two boolean env15)
  bad2406 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b1 (bop b1 (bop b0 b0)))) b1 → ⊥
  bad2406  p = false≢true (cong lower p)
  cut2406 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (var 3) (op (var 4) (var 4))))) , (var 2)) → ⊥
  cut2406  adequate = bad2406  (Adequate.valid adequate Two boolean env24)
  bad2407 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop b1 (bop b0 b0)))) b1 → ⊥
  bad2407  p = false≢true (cong lower p)
  cut2407 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (var 3) (op (var 4) (var 4))))) , (var 3)) → ⊥
  cut2407  adequate = bad2407  (Adequate.valid adequate Two boolean env16)
  bad2408 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop b0 (bop b1 b1)))) b1 → ⊥
  bad2408  p = false≢true (cong lower p)
  cut2408 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (var 3) (op (var 4) (var 4))))) , (var 4)) → ⊥
  cut2408  adequate = bad2408  (Adequate.valid adequate Two boolean env6)
  bad2409 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop b0 (bop b0 b0)))) b1 → ⊥
  bad2409  p = false≢true (cong lower p)
  cut2409 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (var 3) (op (var 4) (var 4))))) , (var 5)) → ⊥
  cut2409  adequate = bad2409  (Adequate.valid adequate Two boolean env17)
  env26 : ℕ → Two
  env26 zero = b0
  env26 (suc zero) = b0
  env26 (suc (suc zero)) = b1
  env26 (suc (suc (suc zero))) = b0
  env26 (suc (suc (suc (suc zero)))) = b0
  env26 (suc (suc (suc (suc (suc zero))))) = b0
  env26 (suc (suc (suc (suc (suc (suc rest)))))) = b0
  bad2410 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b1 (bop b0 (bop b0 b0)))) b0 → ⊥
  bad2410  p = false≢true (sym (cong lower p))
  cut2410 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (var 3) (op (var 4) (var 5))))) , (var 0)) → ⊥
  cut2410  adequate = bad2410  (Adequate.valid adequate Two boolean env26)
  bad2411 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b1 (bop b0 (bop b0 b0)))) b0 → ⊥
  bad2411  p = false≢true (sym (cong lower p))
  cut2411 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (var 3) (op (var 4) (var 5))))) , (var 1)) → ⊥
  cut2411  adequate = bad2411  (Adequate.valid adequate Two boolean env26)
  env27 : ℕ → Two
  env27 zero = b0
  env27 (suc zero) = b0
  env27 (suc (suc zero)) = b1
  env27 (suc (suc (suc zero))) = b1
  env27 (suc (suc (suc (suc zero)))) = b0
  env27 (suc (suc (suc (suc (suc zero))))) = b0
  env27 (suc (suc (suc (suc (suc (suc rest)))))) = b0
  bad2412 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b1 (bop b1 (bop b0 b0)))) b1 → ⊥
  bad2412  p = false≢true (cong lower p)
  cut2412 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (var 3) (op (var 4) (var 5))))) , (var 2)) → ⊥
  cut2412  adequate = bad2412  (Adequate.valid adequate Two boolean env27)
  env28 : ℕ → Two
  env28 zero = b0
  env28 (suc zero) = b0
  env28 (suc (suc zero)) = b0
  env28 (suc (suc (suc zero))) = b1
  env28 (suc (suc (suc (suc zero)))) = b0
  env28 (suc (suc (suc (suc (suc zero))))) = b0
  env28 (suc (suc (suc (suc (suc (suc rest)))))) = b0
  bad2413 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop b1 (bop b0 b0)))) b1 → ⊥
  bad2413  p = false≢true (cong lower p)
  cut2413 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (var 3) (op (var 4) (var 5))))) , (var 3)) → ⊥
  cut2413  adequate = bad2413  (Adequate.valid adequate Two boolean env28)
  env29 : ℕ → Two
  env29 zero = b0
  env29 (suc zero) = b0
  env29 (suc (suc zero)) = b0
  env29 (suc (suc (suc zero))) = b0
  env29 (suc (suc (suc (suc zero)))) = b1
  env29 (suc (suc (suc (suc (suc zero))))) = b0
  env29 (suc (suc (suc (suc (suc (suc rest)))))) = b0
  bad2414 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop b0 (bop b1 b0)))) b1 → ⊥
  bad2414  p = false≢true (cong lower p)
  cut2414 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (var 3) (op (var 4) (var 5))))) , (var 4)) → ⊥
  cut2414  adequate = bad2414  (Adequate.valid adequate Two boolean env29)
  bad2415 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop b0 (bop b0 b1)))) b1 → ⊥
  bad2415  p = false≢true (cong lower p)
  cut2415 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (var 3) (op (var 4) (var 5))))) , (var 5)) → ⊥
  cut2415  adequate = bad2415  (Adequate.valid adequate Two boolean env17)
  env30 : ℕ → Two
  env30 zero = b0
  env30 (suc zero) = b0
  env30 (suc (suc zero)) = b0
  env30 (suc (suc (suc zero))) = b0
  env30 (suc (suc (suc (suc zero)))) = b0
  env30 (suc (suc (suc (suc (suc zero))))) = b0
  env30 (suc (suc (suc (suc (suc (suc zero)))))) = b1
  env30 (suc (suc (suc (suc (suc (suc (suc rest))))))) = b0
  bad2416 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 (bop b0 (bop b0 b0)))) b1 → ⊥
  bad2416  p = false≢true (cong lower p)
  cut2416 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (op (var 3) (op (var 4) (var 5))))) , (var 6)) → ⊥
  cut2416  adequate = bad2416  (Adequate.valid adequate Two boolean env30)
