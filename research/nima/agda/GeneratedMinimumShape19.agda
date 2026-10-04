{-# OPTIONS --safe --cubical --guardedness #-}
module GeneratedMinimumShape19 where
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
  holds25 : (z0 : A1) → (mul1 (mul1 z0 z0) (mul1 z0 z0)) ≡ z0
  holds25 m1c0 = refl
  holds25 m1c1 = refl
  cut25 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (var 0) (var 0))) , (var 0)) → ⊥
  cut25  = reject1 ((op (op (var 0) (var 0)) (op (var 0) (var 0))) , (var 0)) (λ env → holds25 (env 0))
  env0 : ℕ → Two
  env0 zero = b0
  env0 (suc zero) = b1
  env0 (suc (suc rest)) = b0
  bad26 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 b0)) b1 → ⊥
  bad26  p = false≢true (cong lower p)
  cut26 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (var 0) (var 0))) , (var 1)) → ⊥
  cut26  adequate = bad26  (Adequate.valid adequate Two boolean env0)
  holds27 : (z0 z1 : A2) → (mul2 (mul2 z0 z0) (mul2 z0 z1)) ≡ z0
  holds27 z0 z1 = refl
  cut27 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (var 0) (var 1))) , (var 0)) → ⊥
  cut27  = reject2 ((op (op (var 0) (var 0)) (op (var 0) (var 1))) , (var 0)) (λ env → holds27 (env 0) (env 1))
  bad28 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 b1)) b1 → ⊥
  bad28  p = false≢true (cong lower p)
  cut28 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (var 0) (var 1))) , (var 1)) → ⊥
  cut28  adequate = bad28  (Adequate.valid adequate Two boolean env0)
  env1 : ℕ → Two
  env1 zero = b0
  env1 (suc zero) = b0
  env1 (suc (suc zero)) = b1
  env1 (suc (suc (suc rest))) = b0
  bad29 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 b0)) b1 → ⊥
  bad29  p = false≢true (cong lower p)
  cut29 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (var 0) (var 1))) , (var 2)) → ⊥
  cut29  adequate = bad29  (Adequate.valid adequate Two boolean env1)
  holds30 : (z0 z1 : A2) → (mul2 (mul2 z0 z0) (mul2 z1 z0)) ≡ z0
  holds30 z0 z1 = refl
  cut30 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (var 1) (var 0))) , (var 0)) → ⊥
  cut30  = reject2 ((op (op (var 0) (var 0)) (op (var 1) (var 0))) , (var 0)) (λ env → holds30 (env 0) (env 1))
  bad31 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b1 b0)) b1 → ⊥
  bad31  p = false≢true (cong lower p)
  cut31 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (var 1) (var 0))) , (var 1)) → ⊥
  cut31  adequate = bad31  (Adequate.valid adequate Two boolean env0)
  bad32 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 b0)) b1 → ⊥
  bad32  p = false≢true (cong lower p)
  cut32 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (var 1) (var 0))) , (var 2)) → ⊥
  cut32  adequate = bad32  (Adequate.valid adequate Two boolean env1)
  bad33 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b1 b1)) b0 → ⊥
  bad33  p = false≢true (sym (cong lower p))
  cut33 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (var 1) (var 1))) , (var 0)) → ⊥
  cut33  adequate = bad33  (Adequate.valid adequate Two boolean env0)
  env2 : ℕ → Two
  env2 zero = b1
  env2 (suc zero) = b0
  env2 (suc (suc rest)) = b0
  bad34 : PathP (λ _ → Two) (bop (bop b1 b1) (bop b0 b0)) b0 → ⊥
  bad34  p = false≢true (sym (cong lower p))
  cut34 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (var 1) (var 1))) , (var 1)) → ⊥
  cut34  adequate = bad34  (Adequate.valid adequate Two boolean env2)
  bad35 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 b0)) b1 → ⊥
  bad35  p = false≢true (cong lower p)
  cut35 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (var 1) (var 1))) , (var 2)) → ⊥
  cut35  adequate = bad35  (Adequate.valid adequate Two boolean env1)
  env3 : ℕ → Two
  env3 zero = b0
  env3 (suc zero) = b1
  env3 (suc (suc zero)) = b1
  env3 (suc (suc (suc rest))) = b0
  bad36 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b1 b1)) b0 → ⊥
  bad36  p = false≢true (sym (cong lower p))
  cut36 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (var 1) (var 2))) , (var 0)) → ⊥
  cut36  adequate = bad36  (Adequate.valid adequate Two boolean env3)
  env4 : ℕ → Two
  env4 zero = b0
  env4 (suc zero) = b1
  env4 (suc (suc zero)) = b0
  env4 (suc (suc (suc rest))) = b0
  bad37 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b1 b0)) b1 → ⊥
  bad37  p = false≢true (cong lower p)
  cut37 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (var 1) (var 2))) , (var 1)) → ⊥
  cut37  adequate = bad37  (Adequate.valid adequate Two boolean env4)
  bad38 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 b1)) b1 → ⊥
  bad38  p = false≢true (cong lower p)
  cut38 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (var 1) (var 2))) , (var 2)) → ⊥
  cut38  adequate = bad38  (Adequate.valid adequate Two boolean env1)
  env5 : ℕ → Two
  env5 zero = b0
  env5 (suc zero) = b0
  env5 (suc (suc zero)) = b0
  env5 (suc (suc (suc zero))) = b1
  env5 (suc (suc (suc (suc rest)))) = b0
  bad39 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 b0)) b1 → ⊥
  bad39  p = false≢true (cong lower p)
  cut39 : Adequate {ℓ} ((op (op (var 0) (var 0)) (op (var 1) (var 2))) , (var 3)) → ⊥
  cut39  adequate = bad39  (Adequate.valid adequate Two boolean env5)
  holds40 : (z0 z1 : A2) → (mul2 (mul2 z0 z1) (mul2 z0 z0)) ≡ z0
  holds40 z0 z1 = refl
  cut40 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 0) (var 0))) , (var 0)) → ⊥
  cut40  = reject2 ((op (op (var 0) (var 1)) (op (var 0) (var 0))) , (var 0)) (λ env → holds40 (env 0) (env 1))
  bad41 : PathP (λ _ → Two) (bop (bop b0 b1) (bop b0 b0)) b1 → ⊥
  bad41  p = false≢true (cong lower p)
  cut41 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 0) (var 0))) , (var 1)) → ⊥
  cut41  adequate = bad41  (Adequate.valid adequate Two boolean env0)
  bad42 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 b0)) b1 → ⊥
  bad42  p = false≢true (cong lower p)
  cut42 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 0) (var 0))) , (var 2)) → ⊥
  cut42  adequate = bad42  (Adequate.valid adequate Two boolean env1)
  bad43 : PathP (λ _ → Two) (bop (bop b1 b0) (bop b1 b0)) b1 → ⊥
  bad43  p = false≢true (cong lower p)
  cut43 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 0) (var 1))) , (var 0)) → ⊥
  cut43  adequate = bad43  (Adequate.valid adequate Two boolean env2)
  bad44 : PathP (λ _ → Two) (bop (bop b0 b1) (bop b0 b1)) b1 → ⊥
  bad44  p = false≢true (cong lower p)
  cut44 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 0) (var 1))) , (var 1)) → ⊥
  cut44  adequate = bad44  (Adequate.valid adequate Two boolean env0)
  bad45 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 b0)) b1 → ⊥
  bad45  p = false≢true (cong lower p)
  cut45 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 0) (var 1))) , (var 2)) → ⊥
  cut45  adequate = bad45  (Adequate.valid adequate Two boolean env1)
  env6 : ℕ → Two
  env6 zero = b1
  env6 (suc zero) = b0
  env6 (suc (suc zero)) = b0
  env6 (suc (suc (suc rest))) = b0
  bad46 : PathP (λ _ → Two) (bop (bop b1 b0) (bop b1 b0)) b1 → ⊥
  bad46  p = false≢true (cong lower p)
  cut46 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 0) (var 2))) , (var 0)) → ⊥
  cut46  adequate = bad46  (Adequate.valid adequate Two boolean env6)
  bad47 : PathP (λ _ → Two) (bop (bop b0 b1) (bop b0 b0)) b1 → ⊥
  bad47  p = false≢true (cong lower p)
  cut47 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 0) (var 2))) , (var 1)) → ⊥
  cut47  adequate = bad47  (Adequate.valid adequate Two boolean env4)
  bad48 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 b1)) b1 → ⊥
  bad48  p = false≢true (cong lower p)
  cut48 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 0) (var 2))) , (var 2)) → ⊥
  cut48  adequate = bad48  (Adequate.valid adequate Two boolean env1)
  bad49 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 b0)) b1 → ⊥
  bad49  p = false≢true (cong lower p)
  cut49 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 0) (var 2))) , (var 3)) → ⊥
  cut49  adequate = bad49  (Adequate.valid adequate Two boolean env5)
  bad50 : PathP (λ _ → Two) (bop (bop b1 b0) (bop b0 b1)) b1 → ⊥
  bad50  p = false≢true (cong lower p)
  cut50 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 1) (var 0))) , (var 0)) → ⊥
  cut50  adequate = bad50  (Adequate.valid adequate Two boolean env2)
  bad51 : PathP (λ _ → Two) (bop (bop b0 b1) (bop b1 b0)) b1 → ⊥
  bad51  p = false≢true (cong lower p)
  cut51 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 1) (var 0))) , (var 1)) → ⊥
  cut51  adequate = bad51  (Adequate.valid adequate Two boolean env0)
  bad52 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 b0)) b1 → ⊥
  bad52  p = false≢true (cong lower p)
  cut52 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 1) (var 0))) , (var 2)) → ⊥
  cut52  adequate = bad52  (Adequate.valid adequate Two boolean env1)
  bad53 : PathP (λ _ → Two) (bop (bop b0 b1) (bop b1 b1)) b0 → ⊥
  bad53  p = false≢true (sym (cong lower p))
  cut53 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 1) (var 1))) , (var 0)) → ⊥
  cut53  adequate = bad53  (Adequate.valid adequate Two boolean env0)
  holds54 : (z0 z1 : A3) → (mul3 (mul3 z0 z1) (mul3 z1 z1)) ≡ z1
  holds54 z0 z1 = refl
  cut54 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 1) (var 1))) , (var 1)) → ⊥
  cut54  = reject3 ((op (op (var 0) (var 1)) (op (var 1) (var 1))) , (var 1)) (λ env → holds54 (env 0) (env 1))
  bad55 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 b0)) b1 → ⊥
  bad55  p = false≢true (cong lower p)
  cut55 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 1) (var 1))) , (var 2)) → ⊥
  cut55  adequate = bad55  (Adequate.valid adequate Two boolean env1)
  bad56 : PathP (λ _ → Two) (bop (bop b0 b1) (bop b1 b1)) b0 → ⊥
  bad56  p = false≢true (sym (cong lower p))
  cut56 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 1) (var 2))) , (var 0)) → ⊥
  cut56  adequate = bad56  (Adequate.valid adequate Two boolean env3)
  bad57 : PathP (λ _ → Two) (bop (bop b0 b1) (bop b1 b0)) b1 → ⊥
  bad57  p = false≢true (cong lower p)
  cut57 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 1) (var 2))) , (var 1)) → ⊥
  cut57  adequate = bad57  (Adequate.valid adequate Two boolean env4)
  bad58 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 b1)) b1 → ⊥
  bad58  p = false≢true (cong lower p)
  cut58 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 1) (var 2))) , (var 2)) → ⊥
  cut58  adequate = bad58  (Adequate.valid adequate Two boolean env1)
  bad59 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 b0)) b1 → ⊥
  bad59  p = false≢true (cong lower p)
  cut59 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 1) (var 2))) , (var 3)) → ⊥
  cut59  adequate = bad59  (Adequate.valid adequate Two boolean env5)
  bad60 : PathP (λ _ → Two) (bop (bop b1 b0) (bop b0 b1)) b1 → ⊥
  bad60  p = false≢true (cong lower p)
  cut60 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (var 0))) , (var 0)) → ⊥
  cut60  adequate = bad60  (Adequate.valid adequate Two boolean env6)
  bad61 : PathP (λ _ → Two) (bop (bop b0 b1) (bop b0 b0)) b1 → ⊥
  bad61  p = false≢true (cong lower p)
  cut61 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (var 0))) , (var 1)) → ⊥
  cut61  adequate = bad61  (Adequate.valid adequate Two boolean env4)
  bad62 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b1 b0)) b1 → ⊥
  bad62  p = false≢true (cong lower p)
  cut62 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (var 0))) , (var 2)) → ⊥
  cut62  adequate = bad62  (Adequate.valid adequate Two boolean env1)
  bad63 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 b0)) b1 → ⊥
  bad63  p = false≢true (cong lower p)
  cut63 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (var 0))) , (var 3)) → ⊥
  cut63  adequate = bad63  (Adequate.valid adequate Two boolean env5)
  bad64 : PathP (λ _ → Two) (bop (bop b0 b1) (bop b1 b1)) b0 → ⊥
  bad64  p = false≢true (sym (cong lower p))
  cut64 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (var 1))) , (var 0)) → ⊥
  cut64  adequate = bad64  (Adequate.valid adequate Two boolean env3)
  bad65 : PathP (λ _ → Two) (bop (bop b0 b1) (bop b0 b1)) b1 → ⊥
  bad65  p = false≢true (cong lower p)
  cut65 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (var 1))) , (var 1)) → ⊥
  cut65  adequate = bad65  (Adequate.valid adequate Two boolean env4)
  bad66 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b1 b0)) b1 → ⊥
  bad66  p = false≢true (cong lower p)
  cut66 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (var 1))) , (var 2)) → ⊥
  cut66  adequate = bad66  (Adequate.valid adequate Two boolean env1)
  bad67 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 b0)) b1 → ⊥
  bad67  p = false≢true (cong lower p)
  cut67 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (var 1))) , (var 3)) → ⊥
  cut67  adequate = bad67  (Adequate.valid adequate Two boolean env5)
  bad68 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b1 b1)) b0 → ⊥
  bad68  p = false≢true (sym (cong lower p))
  cut68 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (var 2))) , (var 0)) → ⊥
  cut68  adequate = bad68  (Adequate.valid adequate Two boolean env1)
  bad69 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b1 b1)) b0 → ⊥
  bad69  p = false≢true (sym (cong lower p))
  cut69 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (var 2))) , (var 1)) → ⊥
  cut69  adequate = bad69  (Adequate.valid adequate Two boolean env1)
  env7 : ℕ → Two
  env7 zero = b1
  env7 (suc zero) = b1
  env7 (suc (suc zero)) = b0
  env7 (suc (suc (suc rest))) = b0
  bad70 : PathP (λ _ → Two) (bop (bop b1 b1) (bop b0 b0)) b0 → ⊥
  bad70  p = false≢true (sym (cong lower p))
  cut70 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (var 2))) , (var 2)) → ⊥
  cut70  adequate = bad70  (Adequate.valid adequate Two boolean env7)
  bad71 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 b0)) b1 → ⊥
  bad71  p = false≢true (cong lower p)
  cut71 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (var 2))) , (var 3)) → ⊥
  cut71  adequate = bad71  (Adequate.valid adequate Two boolean env5)
  env8 : ℕ → Two
  env8 zero = b0
  env8 (suc zero) = b0
  env8 (suc (suc zero)) = b1
  env8 (suc (suc (suc zero))) = b1
  env8 (suc (suc (suc (suc rest)))) = b0
  bad72 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b1 b1)) b0 → ⊥
  bad72  p = false≢true (sym (cong lower p))
  cut72 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (var 3))) , (var 0)) → ⊥
  cut72  adequate = bad72  (Adequate.valid adequate Two boolean env8)
  bad73 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b1 b1)) b0 → ⊥
  bad73  p = false≢true (sym (cong lower p))
  cut73 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (var 3))) , (var 1)) → ⊥
  cut73  adequate = bad73  (Adequate.valid adequate Two boolean env8)
  env9 : ℕ → Two
  env9 zero = b0
  env9 (suc zero) = b0
  env9 (suc (suc zero)) = b1
  env9 (suc (suc (suc zero))) = b0
  env9 (suc (suc (suc (suc rest)))) = b0
  bad74 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b1 b0)) b1 → ⊥
  bad74  p = false≢true (cong lower p)
  cut74 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (var 3))) , (var 2)) → ⊥
  cut74  adequate = bad74  (Adequate.valid adequate Two boolean env9)
  bad75 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 b1)) b1 → ⊥
  bad75  p = false≢true (cong lower p)
  cut75 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (var 3))) , (var 3)) → ⊥
  cut75  adequate = bad75  (Adequate.valid adequate Two boolean env5)
  env10 : ℕ → Two
  env10 zero = b0
  env10 (suc zero) = b0
  env10 (suc (suc zero)) = b0
  env10 (suc (suc (suc zero))) = b0
  env10 (suc (suc (suc (suc zero)))) = b1
  env10 (suc (suc (suc (suc (suc rest))))) = b0
  bad76 : PathP (λ _ → Two) (bop (bop b0 b0) (bop b0 b0)) b1 → ⊥
  bad76  p = false≢true (cong lower p)
  cut76 : Adequate {ℓ} ((op (op (var 0) (var 1)) (op (var 2) (var 3))) , (var 4)) → ⊥
  cut76  adequate = bad76  (Adequate.valid adequate Two boolean env10)
