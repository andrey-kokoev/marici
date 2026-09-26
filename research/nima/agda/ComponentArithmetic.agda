{-# OPTIONS --safe --cubical --guardedness #-}
module ComponentArithmetic where

open import Cubical.Foundations.Prelude hiding (empty)
open import Cubical.Data.Nat.Base using (ℕ; zero; suc)
open import Cubical.Data.Nat.Properties using (isSetℕ)
open import Cubical.Algebra.Semiring.Base

-- Normal forms for finite disjoint unions of one connected generator.
-- The geometric component-normal-form theorem remains a conditional input.
-- Nat supplies only the inductive word type; no library arithmetic is used.
Word = ℕ
empty : Word
empty = zero
unit : Word
unit = suc empty
append : Word → Word → Word
append zero b = b
append (suc a) b = suc (append a b)

append-unit : (a : Word) → append a empty ≡ a
append-unit zero = refl
append-unit (suc a) = cong suc (append-unit a)
append-assoc : (a b c : Word) → append a (append b c) ≡ append (append a b) c
append-assoc zero b c = refl
append-assoc (suc a) b c = cong suc (append-assoc a b c)
append-copy : (a b : Word) → append a (suc b) ≡ suc (append a b)
append-copy zero b = refl
append-copy (suc a) b = cong suc (append-copy a b)
append-comm : (a b : Word) → append a b ≡ append b a
append-comm zero b = sym (append-unit b)
append-comm (suc a) b = cong suc (append-comm a b) ∙ sym (append-copy b a)
interchange : (a b c d : Word) → append (append a b) (append c d) ≡ append (append a c) (append b d)
interchange a b c d = sym (append-assoc a b (append c d))
  ∙ cong (append a) (append-assoc b c d ∙ cong (λ x → append x d) (append-comm b c) ∙ sym (append-assoc c b d))
  ∙ append-assoc a c (append b d)

-- The additive endomorphism classified by its value on the generator.
endo : Word → Word → Word
endo a zero = empty
endo a (suc b) = append a (endo a b)
endo-generator : (a : Word) → endo a unit ≡ a
endo-generator = append-unit
endo-add : (a b c : Word) → endo a (append b c) ≡ append (endo a b) (endo a c)
endo-add a zero c = refl
endo-add a (suc b) c = cong (append a) (endo-add a b c) ∙ append-assoc a (endo a b) (endo a c)
endo-unique : (f : Word → Word) → f empty ≡ empty
  → ((a b : Word) → f (append a b) ≡ append (f a) (f b))
  → (a : Word) → f unit ≡ a → (b : Word) → f b ≡ endo a b
endo-unique f f0 f+ a f1 zero = f0
endo-unique f f0 f+ a f1 (suc b) = f+ unit b ∙ cong₂ append f1 (endo-unique f f0 f+ a f1 b)

-- Multiplication is evaluation of the classified additive endomorphism.
multiply : Word → Word → Word
multiply = endo
zero-left : (a : Word) → multiply empty a ≡ empty
zero-left zero = refl
zero-left (suc a) = zero-left a
unit-left : (a : Word) → multiply unit a ≡ a
unit-left zero = refl
unit-left (suc a) = cong suc (unit-left a)
pointwise-add : (a b c : Word) → multiply (append a b) c ≡ append (multiply a c) (multiply b c)
pointwise-add a b zero = refl
pointwise-add a b (suc c) = cong (append (append a b)) (pointwise-add a b c)
  ∙ interchange a b (multiply a c) (multiply b c)
composition : (a b c : Word) → endo a (endo b c) ≡ endo (endo a b) c
composition a b zero = refl
composition a b (suc c) = endo-add a b (endo b c) ∙ cong (append (endo a b)) (composition a b c)
multiply-comm : (a b : Word) → multiply a b ≡ multiply b a
multiply-comm a b = endo-unique (λ x → multiply x b) (zero-left b)
  (λ x y → pointwise-add x y b) b (unit-left b) a

componentSemiring : Semiring ℓ-zero
componentSemiring = Word , record
  { 0r = empty ; 1r = unit ; _+_ = append ; _·_ = multiply
  ; isSemiring = makeIsSemiring isSetℕ append-assoc append-unit append-comm
      composition endo-generator unit-left endo-add pointwise-add (λ _ → refl) zero-left }

-- Initiality: the target algebra is a readout, not an input to multiplication.
module Readout (S : Semiring ℓ-zero) where
  open SemiringStr (snd S)
  numeral : Word → fst S
  numeral zero = 0r
  numeral (suc a) = 1r + numeral a
  numeral-unit : numeral unit ≡ 1r
  numeral-unit = +IdR 1r
  numeral-add : (a b : Word) → numeral (append a b) ≡ numeral a + numeral b
  numeral-add zero b = sym (+IdL (numeral b))
  numeral-add (suc a) b = cong (1r +_) (numeral-add a b) ∙ +Assoc 1r (numeral a) (numeral b)
  numeral-multiply : (a b : Word) → numeral (multiply a b) ≡ numeral a · numeral b
  numeral-multiply a zero = sym (AnnihilR (numeral a))
  numeral-multiply a (suc b) = numeral-add a (multiply a b)
    ∙ cong₂ _+_ (sym (·IdR (numeral a))) (numeral-multiply a b)
    ∙ sym (·DistR+ (numeral a) 1r (numeral b))
  unique : (f : Word → fst S) → f empty ≡ 0r → f unit ≡ 1r
    → ((a b : Word) → f (append a b) ≡ f a + f b)
    → (a : Word) → f a ≡ numeral a
  unique f f0 f1 f+ zero = f0
  unique f f0 f1 f+ (suc a) = f+ unit a ∙ cong₂ _+_ f1 (unique f f0 f1 f+ a)
