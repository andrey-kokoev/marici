{-# OPTIONS --safe --cubical --guardedness #-}
module GradedBoundaryCoherence where

open import Cubical.Foundations.Prelude
open import Cubical.Foundations.Isomorphism
open import Cubical.Foundations.Equiv
open import Cubical.Foundations.Univalence using (ua; uaβ)
open import Cubical.Data.Nat.Base using (ℕ; zero; suc)
open import Cubical.Data.Unit.Base using (Unit; tt)
open import Cubical.Data.Sigma.Base using (_×_)
open import Cubical.Data.Empty.Base using (⊥)
open import Cubical.Data.Bool.Base using (Bool; false; true)
open import Cubical.Data.Bool.Properties using (false≢true)

-- A globular tower of parallel fillers. Open boundaries and their answers
-- are separate types. No assumption that every boundary has a filler.
module Tower {ℓ : Level} (A : Type ℓ) where
  mutual
    Boundary : ℕ → Type ℓ
    Boundary zero = Lift {j = ℓ} Unit
    Boundary (suc n) = Σ[ b ∈ Boundary n ] (Fill n b × Fill n b)

    Fill : (n : ℕ) → Boundary n → Type ℓ
    Fill zero b = A
    Fill (suc n) (b , x , y) = x ≡ y

  Cell : ℕ → Type ℓ
  Cell n = Σ[ b ∈ Boundary n ] Fill n b

  -- Expand a completed cell into its reflexive self-comparison.
  up : (n : ℕ) → Cell n → Cell (suc n)
  up n (b , x) = (b , x , x) , refl

  -- Recover the first filler, keeping its original boundary.
  down : (n : ℕ) → Cell (suc n) → Cell n
  down n ((b , x , y) , p) = b , x

  down-up : (n : ℕ) (c : Cell n) → down n (up n c) ≡ c
  down-up n c = refl

  -- Endpoint y moves along p. This is NOT a contraction relative to both
  -- fixed endpoints; the total completed package is the object recovered.
  up-down : (n : ℕ) (c : Cell (suc n)) → up n (down n c) ≡ c
  up-down n ((b , x , y) , p) i = (b , x , p i) , (λ j → p (i ∧ j))

  step-iso : (n : ℕ) → Iso (Cell (suc n)) (Cell n)
  step-iso n = record
    { fun = down n ; inv = up n
    ; rightInv = down-up n ; leftInv = up-down n }

  expand : (n : ℕ) → A → Cell n
  expand zero a = lift tt , a
  expand (suc n) a = up n (expand n a)

  close : (n : ℕ) → Cell n → A
  close zero (b , a) = a
  close (suc n) c = close n (down n c)

  close-expand : (n : ℕ) (a : A) → close n (expand n a) ≡ a
  close-expand zero a = refl
  close-expand (suc n) a = close-expand n a

  expand-close : (n : ℕ) (c : Cell n) → expand n (close n c) ≡ c
  expand-close zero (lift tt , a) = refl
  expand-close (suc n) c = cong (up n) (expand-close n (down n c)) ∙ up-down n c

  grade-iso : (n : ℕ) → Iso (Cell n) A
  grade-iso n = record
    { fun = close n ; inv = expand n
    ; rightInv = close-expand n ; leftInv = expand-close n }

  grade-equivalence : (n : ℕ) → Cell n ≃ A
  grade-equivalence n = isoToEquiv (grade-iso n)

  -- Universal extension of an interpretation of the starting answers.
  -- Restriction along expand and extension along close are inverse maps,
  -- including their retained function-space homotopies.
  interpretation-iso : {ℓ' : Level} (n : ℕ) (Y : Type ℓ')
    → Iso (Cell n → Y) (A → Y)
  interpretation-iso n Y = record
    { fun = λ h a → h (expand n a)
    ; inv = λ f c → f (close n c)
    ; rightInv = λ f → funExt (λ a → cong f (close-expand n a))
    ; leftInv = λ h → funExt (λ c → cong h (expand-close n c)) }

  universal-extension : {ℓ' : Level} (n : ℕ) (Y : Type ℓ')
    → (Cell n → Y) ≃ (A → Y)
  universal-extension n Y = isoToEquiv (interpretation-iso n Y)

  Extension : {ℓ' : Level} (n : ℕ) (Y : Type ℓ') (f : A → Y) → Type (ℓ-max ℓ ℓ')
  Extension n Y f = Σ[ h ∈ (Cell n → Y) ] ((λ a → h (expand n a)) ≡ f)

  unique-extension : {ℓ' : Level} (n : ℕ) (Y : Type ℓ') (f : A → Y)
    → isContr (Extension n Y f)
  unique-extension n Y f = equiv-proof (snd (universal-extension n Y)) f

  -- Rotate a parallel comparison by exchanging its endpoints.
  reverse : (n : ℕ) → Cell (suc n) → Cell (suc n)
  reverse n ((b , x , y) , p) = (b , y , x) , sym p

  reverse-twice : (n : ℕ) (c : Cell (suc n)) → reverse n (reverse n c) ≡ c
  reverse-twice n c = refl

  reverse-base : (n : ℕ) (c : Cell (suc n)) → down n (reverse n c) ≡ down n c
  reverse-base n ((b , x , y) , p) i = b , p (~ i)

  close-four : Cell 4 → A
  close-four = close 4

  four-return : (a : A) → close-four (expand 4 a) ≡ a
  four-return = close-expand 4

-- An open question can exist without any answer, at grade zero.
module EmptyTower = Tower ⊥
empty-question : EmptyTower.Boundary 0
empty-question = lift tt

no-empty-completed-cycle : (n : ℕ) → EmptyTower.Cell n → ⊥
no-empty-completed-cycle = EmptyTower.close

-- Even with an inhabited starting type, not every marked boundary fills.
module BoolTower = Tower Bool
incompatible-boundary : BoolTower.Boundary 1
incompatible-boundary = lift tt , false , true

no-incompatible-filler : BoolTower.Fill 1 incompatible-boundary → ⊥
no-incompatible-filler = false≢true

no-universal-marked-filler : ((b : BoolTower.Boundary 1) → BoolTower.Fill 1 b) → ⊥
no-universal-marked-filler solve = no-incompatible-filler (solve incompatible-boundary)

false-cycle true-cycle : BoolTower.Cell 4
false-cycle = BoolTower.expand 4 false
true-cycle = BoolTower.expand 4 true

answers-retained : false-cycle ≡ true-cycle → ⊥
answers-retained p = false≢true (cong BoolTower.close-four p)

-- A nontrivial proof-space probe: two distinct fillers of the SAME boundary.
-- Total-package recovery must not be confused with unique marked fillers.
flip : Bool → Bool
flip false = true
flip true = false

flip-twice : (b : Bool) → flip (flip b) ≡ b
flip-twice false = refl
flip-twice true = refl

flip-iso : Iso Bool Bool
flip-iso = record
  { fun = flip ; inv = flip ; rightInv = flip-twice ; leftInv = flip-twice }

module TypeTower = Tower (Type ℓ-zero)
marked-type-boundary : TypeTower.Boundary 1
marked-type-boundary = lift tt , Bool , Bool

plain-filler twisted-filler : TypeTower.Fill 1 marked-type-boundary
plain-filler = refl
twisted-filler = ua (isoToEquiv flip-iso)

marked-fillers-distinct : plain-filler ≡ twisted-filler → ⊥
marked-fillers-distinct eq = false≢true
  (sym (transportRefl false)
    ∙ cong (λ p → transport p false) eq
    ∙ uaβ (isoToEquiv flip-iso) false)

marked-fillers-not-contractible : isContr (TypeTower.Fill 1 marked-type-boundary) → ⊥
marked-fillers-not-contractible c = marked-fillers-distinct
  (sym (snd c plain-filler) ∙ snd c twisted-filler)
