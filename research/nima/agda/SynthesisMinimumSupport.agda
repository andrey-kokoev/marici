{-# OPTIONS --safe --cubical --guardedness #-}
module SynthesisMinimumSupport where
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


Canonical : Equation → Type
Canonical e = normal zero (leaves (fst e) ++ leaves (snd e)) ≡ true

data Sized : ℕ → Type where
  leaf : ℕ → Sized zero
  fork : {n m : ℕ} → Sized n → Sized m → Sized (suc (n + m))

erase : {n : ℕ} → Sized n → Term
erase (leaf x) = var x
erase (fork a b) = op (erase a) (erase b)
index : (t : Term) → Sized (nodes t)
index (var x) = leaf x
index (op a b) = fork (index a) (index b)
retract : (t : Term) → erase (index t) ≡ t
retract (var x) = refl
retract (op a b) = cong₂ op (retract a) (retract b)
unerase : {n : ℕ} → Sized (suc n) → Equation
unerase (fork a b) = erase a , erase b
index-equation : (e : Equation) → Sized (suc (cost e))
index-equation (a , b) = fork (index a) (index b)
retract-equation : (e : Equation) → unerase (index-equation e) ≡ e
retract-equation (a , b) = cong₂ _,_ (retract a) (retract b)

change-stroke : {ℓ : Level} {A : Type ℓ} {s t : A → A → A}
  → ((x y : A) → s x y ≡ t x y) → (env : ℕ → A) → (e : Term)
  → eval s env e ≡ eval t env e
change-stroke p env (var x) = refl
change-stroke {s = s} p env (op a b) =
  cong₂ s (change-stroke p env a) (change-stroke p env b)
  ∙ p _ _

module Support (ℓ : Level) where
  Two : Type ℓ
  Two = Lift {j = ℓ} Bool
  pattern b0 = lift false
  pattern b1 = lift true
  bn : Two → Two
  bn b0 = b1
  bn b1 = b0
  bm bj : Two → Two → Two
  bm b0 y = b0
  bm b1 y = y
  bj b0 y = y
  bj b1 y = b1

  b-meet-comm : (x0 x1 : Two) → (bm x0 x1) ≡ (bm x1 x0)
  b-meet-comm b0 b0 = refl
  b-meet-comm b0 b1 = refl
  b-meet-comm b1 b0 = refl
  b-meet-comm b1 b1 = refl
  b-join-comm : (x0 x1 : Two) → (bj x0 x1) ≡ (bj x1 x0)
  b-join-comm b0 b0 = refl
  b-join-comm b0 b1 = refl
  b-join-comm b1 b0 = refl
  b-join-comm b1 b1 = refl
  b-meet-assoc : (x0 x1 x2 : Two) → (bm (bm x0 x1) x2) ≡ (bm x0 (bm x1 x2))
  b-meet-assoc b0 b0 b0 = refl
  b-meet-assoc b0 b0 b1 = refl
  b-meet-assoc b0 b1 b0 = refl
  b-meet-assoc b0 b1 b1 = refl
  b-meet-assoc b1 b0 b0 = refl
  b-meet-assoc b1 b0 b1 = refl
  b-meet-assoc b1 b1 b0 = refl
  b-meet-assoc b1 b1 b1 = refl
  b-join-assoc : (x0 x1 x2 : Two) → (bj (bj x0 x1) x2) ≡ (bj x0 (bj x1 x2))
  b-join-assoc b0 b0 b0 = refl
  b-join-assoc b0 b0 b1 = refl
  b-join-assoc b0 b1 b0 = refl
  b-join-assoc b0 b1 b1 = refl
  b-join-assoc b1 b0 b0 = refl
  b-join-assoc b1 b0 b1 = refl
  b-join-assoc b1 b1 b0 = refl
  b-join-assoc b1 b1 b1 = refl
  b-meet-idem : (x0 : Two) → (bm x0 x0) ≡ x0
  b-meet-idem b0 = refl
  b-meet-idem b1 = refl
  b-join-idem : (x0 : Two) → (bj x0 x0) ≡ x0
  b-join-idem b0 = refl
  b-join-idem b1 = refl
  b-meet-absorb : (x0 x1 : Two) → (bm x0 (bj x0 x1)) ≡ x0
  b-meet-absorb b0 b0 = refl
  b-meet-absorb b0 b1 = refl
  b-meet-absorb b1 b0 = refl
  b-meet-absorb b1 b1 = refl
  b-join-absorb : (x0 x1 : Two) → (bj x0 (bm x0 x1)) ≡ x0
  b-join-absorb b0 b0 = refl
  b-join-absorb b0 b1 = refl
  b-join-absorb b1 b0 = refl
  b-join-absorb b1 b1 = refl
  b-meet-distrib : (x0 x1 x2 : Two) → (bm x0 (bj x1 x2)) ≡ (bj (bm x0 x1) (bm x0 x2))
  b-meet-distrib b0 b0 b0 = refl
  b-meet-distrib b0 b0 b1 = refl
  b-meet-distrib b0 b1 b0 = refl
  b-meet-distrib b0 b1 b1 = refl
  b-meet-distrib b1 b0 b0 = refl
  b-meet-distrib b1 b0 b1 = refl
  b-meet-distrib b1 b1 b0 = refl
  b-meet-distrib b1 b1 b1 = refl
  b-join-distrib : (x0 x1 x2 : Two) → (bj x0 (bm x1 x2)) ≡ (bm (bj x0 x1) (bj x0 x2))
  b-join-distrib b0 b0 b0 = refl
  b-join-distrib b0 b0 b1 = refl
  b-join-distrib b0 b1 b0 = refl
  b-join-distrib b0 b1 b1 = refl
  b-join-distrib b1 b0 b0 = refl
  b-join-distrib b1 b0 b1 = refl
  b-join-distrib b1 b1 b0 = refl
  b-join-distrib b1 b1 b1 = refl
  b-meet-top : (x0 : Two) → (bm x0 b1) ≡ x0
  b-meet-top b0 = refl
  b-meet-top b1 = refl
  b-join-bottom : (x0 : Two) → (bj x0 b0) ≡ x0
  b-join-bottom b0 = refl
  b-join-bottom b1 = refl
  b-meet-complement : (x0 : Two) → (bm x0 (bn x0)) ≡ b0
  b-meet-complement b0 = refl
  b-meet-complement b1 = refl
  b-join-complement : (x0 : Two) → (bj x0 (bn x0)) ≡ b1
  b-join-complement b0 = refl
  b-join-complement b1 = refl
  boolean : B.BooleanStructure Two
  boolean = record
    { carrier-is-set = isOfHLevelLift 2 isSetBool ; bottom = b0 ; top = b1
    ; neg = bn ; meet = bm ; join = bj
    ; meet-comm = b-meet-comm
    ; join-comm = b-join-comm
    ; meet-assoc = b-meet-assoc
    ; join-assoc = b-join-assoc
    ; meet-idem = b-meet-idem
    ; join-idem = b-join-idem
    ; meet-absorb = b-meet-absorb
    ; join-absorb = b-join-absorb
    ; meet-distrib = b-meet-distrib
    ; join-distrib = b-join-distrib
    ; meet-top = b-meet-top
    ; join-bottom = b-join-bottom
    ; meet-complement = b-meet-complement
    ; join-complement = b-join-complement
    }
  bop : Two → Two → Two
  bop = B.ToWolfram.nand boolean
  all0 all1 : ℕ → Two
  all0 _ = b0
  all1 _ = b1
  A0 : Type ℓ
  A0 = Lift {j = ℓ} (Bool)
  pattern m0c0 = lift false
  pattern m0c1 = lift true
  mul0 : A0 → A0 → A0
  mul0 _ _ = m0c0
  failed0 : Equation
  failed0 = (op (op (var 0) (var 0)) (op (var 0) (var 0))) , (var 0)
  at0 : ℕ → A0
  at0 _ = m0c1
  distinguish0 : A0 → Bool
  distinguish0 m0c0 = false
  distinguish0 m0c1 = true
  reject0 : (e : Equation) → Holds e mul0 → Adequate {ℓ} e → ⊥
  reject0 e holds adequate =
    let pair = Adequate.reconstruct adequate A0 (isOfHLevelLift 2 isSetBool) m0c0 mul0 holds
        structure = fst pair
        recover = snd pair
        path = change-stroke recover at0 (fst failed0)
          ∙ Necessary.involution structure m0c1
          ∙ sym (change-stroke recover at0 (snd failed0))
    in false≢true (cong distinguish0 path)
  A1 : Type ℓ
  A1 = Lift {j = ℓ} (Bool)
  pattern m1c0 = lift false
  pattern m1c1 = lift true
  mul1 : A1 → A1 → A1
  mul1 m1c0 _ = m1c0
  mul1 m1c1 m1c0 = m1c0
  mul1 m1c1 m1c1 = m1c1
  failed1 : Equation
  failed1 = (op (var 0) (op (var 0) (var 0))) , (op (var 1) (op (var 1) (var 1)))
  at1 : ℕ → A1
  at1 zero = m1c0
  at1 (suc _) = m1c1
  distinguish1 : A1 → Bool
  distinguish1 m1c0 = false
  distinguish1 m1c1 = true
  reject1 : (e : Equation) → Holds e mul1 → Adequate {ℓ} e → ⊥
  reject1 e holds adequate =
    let pair = Adequate.reconstruct adequate A1 (isOfHLevelLift 2 isSetBool) m1c0 mul1 holds
        structure = fst pair
        recover = snd pair
        path = change-stroke recover at1 (fst failed1)
          ∙ Necessary.top-independence structure m1c0 m1c1
          ∙ sym (change-stroke recover at1 (snd failed1))
    in false≢true (cong distinguish1 path)
  A2 : Type ℓ
  A2 = Lift {j = ℓ} (Bool)
  pattern m2c0 = lift false
  pattern m2c1 = lift true
  mul2 : A2 → A2 → A2
  mul2 x _ = x
  failed2 : Equation
  failed2 = (op (var 0) (var 1)) , (op (var 1) (var 0))
  at2 : ℕ → A2
  at2 zero = m2c0
  at2 (suc _) = m2c1
  distinguish2 : A2 → Bool
  distinguish2 m2c0 = false
  distinguish2 m2c1 = true
  reject2 : (e : Equation) → Holds e mul2 → Adequate {ℓ} e → ⊥
  reject2 e holds adequate =
    let pair = Adequate.reconstruct adequate A2 (isOfHLevelLift 2 isSetBool) m2c0 mul2 holds
        structure = fst pair
        recover = snd pair
        path = change-stroke recover at2 (fst failed2)
          ∙ Necessary.commutativity structure m2c0 m2c1
          ∙ sym (change-stroke recover at2 (snd failed2))
    in false≢true (cong distinguish2 path)
  A3 : Type ℓ
  A3 = Lift {j = ℓ} (Bool)
  pattern m3c0 = lift false
  pattern m3c1 = lift true
  mul3 : A3 → A3 → A3
  mul3 _ y = y
  failed3 : Equation
  failed3 = (op (var 0) (var 1)) , (op (var 1) (var 0))
  at3 : ℕ → A3
  at3 zero = m3c0
  at3 (suc _) = m3c1
  distinguish3 : A3 → Bool
  distinguish3 m3c0 = true
  distinguish3 m3c1 = false
  reject3 : (e : Equation) → Holds e mul3 → Adequate {ℓ} e → ⊥
  reject3 e holds adequate =
    let pair = Adequate.reconstruct adequate A3 (isOfHLevelLift 2 isSetBool) m3c0 mul3 holds
        structure = fst pair
        recover = snd pair
        path = change-stroke recover at3 (fst failed3)
          ∙ Necessary.commutativity structure m3c0 m3c1
          ∙ sym (change-stroke recover at3 (snd failed3))
    in false≢true (cong distinguish3 path)
  A4 : Type ℓ
  A4 = Lift {j = ℓ} (Bool)
  pattern m4c0 = lift false
  pattern m4c1 = lift true
  mul4 : A4 → A4 → A4
  mul4 m4c0 m4c0 = m4c0
  mul4 m4c0 m4c1 = m4c1
  mul4 m4c1 m4c0 = m4c1
  mul4 m4c1 m4c1 = m4c0
  failed4 : Equation
  failed4 = (op (var 0) (op (var 0) (var 0))) , (op (var 1) (op (var 1) (var 1)))
  at4 : ℕ → A4
  at4 zero = m4c0
  at4 (suc _) = m4c1
  distinguish4 : A4 → Bool
  distinguish4 m4c0 = false
  distinguish4 m4c1 = true
  reject4 : (e : Equation) → Holds e mul4 → Adequate {ℓ} e → ⊥
  reject4 e holds adequate =
    let pair = Adequate.reconstruct adequate A4 (isOfHLevelLift 2 isSetBool) m4c0 mul4 holds
        structure = fst pair
        recover = snd pair
        path = change-stroke recover at4 (fst failed4)
          ∙ Necessary.top-independence structure m4c0 m4c1
          ∙ sym (change-stroke recover at4 (snd failed4))
    in false≢true (cong distinguish4 path)
  A5 : Type ℓ
  A5 = Lift {j = ℓ} (Maybe Bool)
  pattern m5c0 = lift nothing
  pattern m5c1 = lift (just false)
  pattern m5c2 = lift (just true)
  mul5 : A5 → A5 → A5
  mul5 m5c0 m5c0 = m5c0
  mul5 m5c0 m5c1 = m5c2
  mul5 m5c0 m5c2 = m5c1
  mul5 m5c1 m5c0 = m5c2
  mul5 m5c1 m5c1 = m5c2
  mul5 m5c1 m5c2 = m5c0
  mul5 m5c2 m5c0 = m5c1
  mul5 m5c2 m5c1 = m5c0
  mul5 m5c2 m5c2 = m5c1
  failed5 : Equation
  failed5 = (op (op (var 0) (var 0)) (op (var 0) (op (var 1) (var 1)))) , (var 0)
  at5 : ℕ → A5
  at5 zero = m5c0
  at5 (suc _) = m5c1
  distinguish5 : A5 → Bool
  distinguish5 m5c0 = true
  distinguish5 m5c1 = true
  distinguish5 m5c2 = false
  reject5 : (e : Equation) → Holds e mul5 → Adequate {ℓ} e → ⊥
  reject5 e holds adequate =
    let pair = Adequate.reconstruct adequate A5 (isOfHLevelLift 2 (isOfHLevelMaybe 0 isSetBool)) m5c0 mul5 holds
        structure = fst pair
        recover = snd pair
        path = change-stroke recover at5 (fst failed5)
          ∙ Necessary.absorption structure m5c0 m5c1
          ∙ sym (change-stroke recover at5 (snd failed5))
    in false≢true (cong distinguish5 path)
  A6 : Type ℓ
  A6 = Lift {j = ℓ} (Maybe Bool)
  pattern m6c0 = lift nothing
  pattern m6c1 = lift (just false)
  pattern m6c2 = lift (just true)
  mul6 : A6 → A6 → A6
  mul6 m6c0 m6c0 = m6c0
  mul6 m6c0 m6c1 = m6c0
  mul6 m6c0 m6c2 = m6c1
  mul6 m6c1 m6c0 = m6c2
  mul6 m6c1 m6c1 = m6c2
  mul6 m6c1 m6c2 = m6c1
  mul6 m6c2 m6c0 = m6c0
  mul6 m6c2 m6c1 = m6c0
  mul6 m6c2 m6c2 = m6c1
  failed6 : Equation
  failed6 = (op (var 0) (var 1)) , (op (var 1) (var 0))
  at6 : ℕ → A6
  at6 zero = m6c0
  at6 (suc _) = m6c1
  distinguish6 : A6 → Bool
  distinguish6 m6c0 = false
  distinguish6 m6c1 = true
  distinguish6 m6c2 = true
  reject6 : (e : Equation) → Holds e mul6 → Adequate {ℓ} e → ⊥
  reject6 e holds adequate =
    let pair = Adequate.reconstruct adequate A6 (isOfHLevelLift 2 (isOfHLevelMaybe 0 isSetBool)) m6c0 mul6 holds
        structure = fst pair
        recover = snd pair
        path = change-stroke recover at6 (fst failed6)
          ∙ Necessary.commutativity structure m6c0 m6c1
          ∙ sym (change-stroke recover at6 (snd failed6))
    in false≢true (cong distinguish6 path)
  A7 : Type ℓ
  A7 = Lift {j = ℓ} (Maybe Bool)
  pattern m7c0 = lift nothing
  pattern m7c1 = lift (just false)
  pattern m7c2 = lift (just true)
  mul7 : A7 → A7 → A7
  mul7 m7c0 m7c0 = m7c0
  mul7 m7c0 m7c1 = m7c0
  mul7 m7c0 m7c2 = m7c1
  mul7 m7c1 m7c0 = m7c2
  mul7 m7c1 m7c1 = m7c0
  mul7 m7c1 m7c2 = m7c2
  mul7 m7c2 m7c0 = m7c2
  mul7 m7c2 m7c1 = m7c0
  mul7 m7c2 m7c2 = m7c2
  failed7 : Equation
  failed7 = (op (var 0) (var 1)) , (op (var 1) (var 0))
  at7 : ℕ → A7
  at7 zero = m7c0
  at7 (suc _) = m7c1
  distinguish7 : A7 → Bool
  distinguish7 m7c0 = false
  distinguish7 m7c1 = true
  distinguish7 m7c2 = true
  reject7 : (e : Equation) → Holds e mul7 → Adequate {ℓ} e → ⊥
  reject7 e holds adequate =
    let pair = Adequate.reconstruct adequate A7 (isOfHLevelLift 2 (isOfHLevelMaybe 0 isSetBool)) m7c0 mul7 holds
        structure = fst pair
        recover = snd pair
        path = change-stroke recover at7 (fst failed7)
          ∙ Necessary.commutativity structure m7c0 m7c1
          ∙ sym (change-stroke recover at7 (snd failed7))
    in false≢true (cong distinguish7 path)
  A8 : Type ℓ
  A8 = Lift {j = ℓ} (Maybe Bool)
  pattern m8c0 = lift nothing
  pattern m8c1 = lift (just false)
  pattern m8c2 = lift (just true)
  mul8 : A8 → A8 → A8
  mul8 m8c0 m8c0 = m8c0
  mul8 m8c0 m8c1 = m8c1
  mul8 m8c0 m8c2 = m8c2
  mul8 m8c1 m8c0 = m8c2
  mul8 m8c1 m8c1 = m8c0
  mul8 m8c1 m8c2 = m8c1
  mul8 m8c2 m8c0 = m8c1
  mul8 m8c2 m8c1 = m8c2
  mul8 m8c2 m8c2 = m8c0
  failed8 : Equation
  failed8 = (op (var 0) (var 1)) , (op (var 1) (var 0))
  at8 : ℕ → A8
  at8 zero = m8c0
  at8 (suc _) = m8c1
  distinguish8 : A8 → Bool
  distinguish8 m8c0 = true
  distinguish8 m8c1 = false
  distinguish8 m8c2 = true
  reject8 : (e : Equation) → Holds e mul8 → Adequate {ℓ} e → ⊥
  reject8 e holds adequate =
    let pair = Adequate.reconstruct adequate A8 (isOfHLevelLift 2 (isOfHLevelMaybe 0 isSetBool)) m8c0 mul8 holds
        structure = fst pair
        recover = snd pair
        path = change-stroke recover at8 (fst failed8)
          ∙ Necessary.commutativity structure m8c0 m8c1
          ∙ sym (change-stroke recover at8 (snd failed8))
    in false≢true (cong distinguish8 path)
  A9 : Type ℓ
  A9 = Lift {j = ℓ} (Maybe Bool)
  pattern m9c0 = lift nothing
  pattern m9c1 = lift (just false)
  pattern m9c2 = lift (just true)
  mul9 : A9 → A9 → A9
  mul9 m9c0 m9c0 = m9c0
  mul9 m9c0 m9c1 = m9c2
  mul9 m9c0 m9c2 = m9c1
  mul9 m9c1 m9c0 = m9c1
  mul9 m9c1 m9c1 = m9c0
  mul9 m9c1 m9c2 = m9c2
  mul9 m9c2 m9c0 = m9c2
  mul9 m9c2 m9c1 = m9c1
  mul9 m9c2 m9c2 = m9c0
  failed9 : Equation
  failed9 = (op (var 0) (var 1)) , (op (var 1) (var 0))
  at9 : ℕ → A9
  at9 zero = m9c0
  at9 (suc _) = m9c1
  distinguish9 : A9 → Bool
  distinguish9 m9c0 = true
  distinguish9 m9c1 = true
  distinguish9 m9c2 = false
  reject9 : (e : Equation) → Holds e mul9 → Adequate {ℓ} e → ⊥
  reject9 e holds adequate =
    let pair = Adequate.reconstruct adequate A9 (isOfHLevelLift 2 (isOfHLevelMaybe 0 isSetBool)) m9c0 mul9 holds
        structure = fst pair
        recover = snd pair
        path = change-stroke recover at9 (fst failed9)
          ∙ Necessary.commutativity structure m9c0 m9c1
          ∙ sym (change-stroke recover at9 (snd failed9))
    in false≢true (cong distinguish9 path)
  A10 : Type ℓ
  A10 = Lift {j = ℓ} (Maybe Bool)
  pattern m10c0 = lift nothing
  pattern m10c1 = lift (just false)
  pattern m10c2 = lift (just true)
  mul10 : A10 → A10 → A10
  mul10 m10c0 m10c0 = m10c0
  mul10 m10c0 m10c1 = m10c0
  mul10 m10c0 m10c2 = m10c1
  mul10 m10c1 m10c0 = m10c0
  mul10 m10c1 m10c1 = m10c2
  mul10 m10c1 m10c2 = m10c1
  mul10 m10c2 _ = m10c1
  failed10 : Equation
  failed10 = (op (var 0) (op (var 0) (var 0))) , (op (var 1) (op (var 1) (var 1)))
  at10 : ℕ → A10
  at10 zero = m10c0
  at10 (suc _) = m10c1
  distinguish10 : A10 → Bool
  distinguish10 m10c0 = false
  distinguish10 m10c1 = true
  distinguish10 m10c2 = true
  reject10 : (e : Equation) → Holds e mul10 → Adequate {ℓ} e → ⊥
  reject10 e holds adequate =
    let pair = Adequate.reconstruct adequate A10 (isOfHLevelLift 2 (isOfHLevelMaybe 0 isSetBool)) m10c0 mul10 holds
        structure = fst pair
        recover = snd pair
        path = change-stroke recover at10 (fst failed10)
          ∙ Necessary.top-independence structure m10c0 m10c1
          ∙ sym (change-stroke recover at10 (snd failed10))
    in false≢true (cong distinguish10 path)
  A11 : Type ℓ
  A11 = Lift {j = ℓ} (Maybe Bool)
  pattern m11c0 = lift nothing
  pattern m11c1 = lift (just false)
  pattern m11c2 = lift (just true)
  mul11 : A11 → A11 → A11
  mul11 m11c0 m11c0 = m11c0
  mul11 m11c0 m11c1 = m11c0
  mul11 m11c0 m11c2 = m11c1
  mul11 m11c1 _ = m11c2
  mul11 m11c2 m11c0 = m11c0
  mul11 m11c2 m11c1 = m11c0
  mul11 m11c2 m11c2 = m11c1
  failed11 : Equation
  failed11 = (op (var 0) (var 1)) , (op (var 1) (var 0))
  at11 : ℕ → A11
  at11 zero = m11c0
  at11 (suc _) = m11c1
  distinguish11 : A11 → Bool
  distinguish11 m11c0 = false
  distinguish11 m11c1 = true
  distinguish11 m11c2 = true
  reject11 : (e : Equation) → Holds e mul11 → Adequate {ℓ} e → ⊥
  reject11 e holds adequate =
    let pair = Adequate.reconstruct adequate A11 (isOfHLevelLift 2 (isOfHLevelMaybe 0 isSetBool)) m11c0 mul11 holds
        structure = fst pair
        recover = snd pair
        path = change-stroke recover at11 (fst failed11)
          ∙ Necessary.commutativity structure m11c0 m11c1
          ∙ sym (change-stroke recover at11 (snd failed11))
    in false≢true (cong distinguish11 path)
  A12 : Type ℓ
  A12 = Lift {j = ℓ} (Maybe Bool)
  pattern m12c0 = lift nothing
  pattern m12c1 = lift (just false)
  pattern m12c2 = lift (just true)
  mul12 : A12 → A12 → A12
  mul12 m12c0 m12c0 = m12c0
  mul12 m12c0 m12c1 = m12c0
  mul12 m12c0 m12c2 = m12c1
  mul12 m12c1 _ = m12c2
  mul12 m12c2 m12c0 = m12c0
  mul12 m12c2 m12c1 = m12c0
  mul12 m12c2 m12c2 = m12c2
  failed12 : Equation
  failed12 = (op (var 0) (var 1)) , (op (var 1) (var 0))
  at12 : ℕ → A12
  at12 zero = m12c0
  at12 (suc _) = m12c1
  distinguish12 : A12 → Bool
  distinguish12 m12c0 = false
  distinguish12 m12c1 = true
  distinguish12 m12c2 = true
  reject12 : (e : Equation) → Holds e mul12 → Adequate {ℓ} e → ⊥
  reject12 e holds adequate =
    let pair = Adequate.reconstruct adequate A12 (isOfHLevelLift 2 (isOfHLevelMaybe 0 isSetBool)) m12c0 mul12 holds
        structure = fst pair
        recover = snd pair
        path = change-stroke recover at12 (fst failed12)
          ∙ Necessary.commutativity structure m12c0 m12c1
          ∙ sym (change-stroke recover at12 (snd failed12))
    in false≢true (cong distinguish12 path)
  A13 : Type ℓ
  A13 = Lift {j = ℓ} (Bool × Bool)
  pattern m13c0 = lift (false , false)
  pattern m13c1 = lift (false , true)
  pattern m13c2 = lift (true , false)
  pattern m13c3 = lift (true , true)
  mul13 : A13 → A13 → A13
  mul13 m13c0 m13c0 = m13c1
  mul13 m13c0 m13c1 = m13c2
  mul13 m13c0 m13c2 = m13c2
  mul13 m13c0 m13c3 = m13c1
  mul13 m13c1 m13c0 = m13c3
  mul13 m13c1 m13c1 = m13c0
  mul13 m13c1 m13c2 = m13c0
  mul13 m13c1 m13c3 = m13c3
  mul13 m13c2 m13c0 = m13c1
  mul13 m13c2 m13c1 = m13c2
  mul13 m13c2 m13c2 = m13c2
  mul13 m13c2 m13c3 = m13c1
  mul13 m13c3 m13c0 = m13c3
  mul13 m13c3 m13c1 = m13c0
  mul13 m13c3 m13c2 = m13c0
  mul13 m13c3 m13c3 = m13c3
  failed13 : Equation
  failed13 = (op (var 0) (var 1)) , (op (var 1) (var 0))
  at13 : ℕ → A13
  at13 zero = m13c0
  at13 (suc _) = m13c1
  distinguish13 : A13 → Bool
  distinguish13 m13c0 = true
  distinguish13 m13c1 = true
  distinguish13 m13c2 = false
  distinguish13 m13c3 = true
  reject13 : (e : Equation) → Holds e mul13 → Adequate {ℓ} e → ⊥
  reject13 e holds adequate =
    let pair = Adequate.reconstruct adequate A13 (isOfHLevelLift 2 (isSet× isSetBool isSetBool)) m13c0 mul13 holds
        structure = fst pair
        recover = snd pair
        path = change-stroke recover at13 (fst failed13)
          ∙ Necessary.commutativity structure m13c0 m13c1
          ∙ sym (change-stroke recover at13 (snd failed13))
    in false≢true (cong distinguish13 path)
