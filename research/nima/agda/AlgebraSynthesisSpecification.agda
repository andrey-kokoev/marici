{-# OPTIONS --safe --cubical --guardedness #-}
module AlgebraSynthesisSpecification where

open import Cubical.Foundations.Prelude
open import Cubical.Data.Nat.Base using (ℕ; zero; suc; _+_)
open import Cubical.Data.Nat.Order using (_<_; ¬m<m)
open import Cubical.Data.Bool.Base using (Bool; true; false)
open import Cubical.Data.Unit.Base using (Unit; tt)
open import Cubical.Data.Empty.Base using (⊥)
open import Cubical.Data.List.Base using (List; []; _∷_; _++_)
open import Cubical.Data.Sigma.Base using (_×_)
import BooleanNandEquivalence as B

module Specification {ℓC ℓP : Level} (Candidate : Type ℓC)
  (cost : Candidate → ℕ) (Adequate : Candidate → Type ℓP) where
  Minimal : Candidate → Type (ℓ-max ℓC ℓP)
  Minimal f = (g : Candidate) → cost g < cost f → Adequate g → ⊥

  Result : Type (ℓ-max ℓC ℓP)
  Result = Σ[ f ∈ Candidate ] (Adequate f × Minimal f)

  certify : (f : Candidate) → Adequate f → Minimal f → Result
  certify f adequate minimal = f , adequate , minimal

  -- A timeout or missing proof has no constructor of this rejection type.
  Rejection : Candidate → Type ℓP
  Rejection f = Adequate f → ⊥

  minimal-from-rejections : (f : Candidate)
    → ((g : Candidate) → cost g < cost f → Rejection g) → Minimal f
  minimal-from-rejections f reject = reject

-- One binary symbol, no constants, and variables named by naturals.
data Term : Type where
  var : ℕ → Term
  op : Term → Term → Term

Equation : Type
Equation = Term × Term

nodes : Term → ℕ
nodes (var _) = zero
nodes (op a b) = suc (nodes a + nodes b)

cost : Equation → ℕ
cost (a , b) = nodes a + nodes b

leaves : Term → List ℕ
leaves (var x) = x ∷ []
leaves (op a b) = leaves a ++ leaves b

-- Restricted-growth naming fixes only alpha-renaming, never commutativity.
data Ordering : Type where less equal greater : Ordering
compare : ℕ → ℕ → Ordering
compare zero zero = equal
compare zero (suc _) = less
compare (suc _) zero = greater
compare (suc x) (suc y) = compare x y

normal : ℕ → List ℕ → Bool
normal bound [] = true
normal bound (x ∷ xs) with compare x bound
... | less = normal bound xs
... | equal = normal (suc bound) xs
... | greater = false

Formula : Type
Formula = Σ[ e ∈ Equation ] (normal zero (leaves (fst e) ++ leaves (snd e)) ≡ true)

eval : {ℓ : Level} {A : Type ℓ} → (A → A → A) → (ℕ → A) → Term → A
eval stroke env (var x) = env x
eval stroke env (op a b) = stroke (eval stroke env a) (eval stroke env b)

Holds : {ℓ : Level} {A : Type ℓ} → Equation → (A → A → A) → Type ℓ
Holds e stroke = (env : ℕ → _) → eval stroke env (fst e) ≡ eval stroke env (snd e)

record Adequate {ℓ : Level} (e : Equation) : Type (ℓ-suc ℓ) where
  field
    valid : (A : Type ℓ) (boolean : B.BooleanStructure A) → Holds e (B.ToWolfram.nand boolean)
    reconstruct : (A : Type ℓ) → isSet A → A → (stroke : A → A → A) → Holds e stroke
      → Σ[ boolean ∈ B.BooleanStructure A ]
          ((x y : A) → stroke x y ≡ B.ToWolfram.nand boolean x y)

module Goal (ℓ : Level) = Specification Formula (λ f → cost (fst f)) (λ f → Adequate {ℓ} (fst f))

-- Necessary laws used by finite countermodel rejection, proved over arbitrary
-- Boolean structures, not inferred from two-valued truth-table samples.
module Necessary {ℓ : Level} {A : Type ℓ} (boolean : B.BooleanStructure A) where
  open B.BooleanStructure boolean
  open B.ToWolfram boolean using (nand; deMorgan; double-negation)
  commutativity : (x y : A) → nand x y ≡ nand y x
  commutativity x y = cong neg (meet-comm x y)
  involution : (x : A) → nand (nand x x) (nand x x) ≡ x
  involution x = cong neg (meet-idem (nand x x)) ∙ double-negation (meet x x) ∙ meet-idem x
  absorption : (x y : A) → nand (nand x x) (nand x (nand y y)) ≡ x
  absorption x y = deMorgan (nand x x) (nand x (nand y y))
    ∙ cong₂ join (double-negation (meet x x)) (double-negation (meet x (nand y y)))
    ∙ cong (λ z → join z (meet x (nand y y))) (meet-idem x)
    ∙ join-absorb x (nand y y)
  top-value : (x : A) → nand x (nand x x) ≡ top
  top-value x = cong neg (cong (meet x) (cong neg (meet-idem x)))
    ∙ cong neg (meet-complement x)
    ∙ B.ToWolfram.Roundtrip.neg-bottom boolean x
  top-independence : (x y : A) → nand x (nand x x) ≡ nand y (nand y y)
  top-independence x y = top-value x ∙ sym (top-value y)

-- Small inhabited test of the complete Sigma interface, independent of W.
module Toy where
  weight : Bool → ℕ
  weight false = zero
  weight true = suc zero
  good : Bool → Type
  good false = ⊥
  good true = Unit
  module S = Specification Bool weight good
  minimal : S.Minimal true
  minimal false cheaper impossible = impossible
  minimal true cheaper adequate = ¬m<m cheaper
  result : S.Result
  result = S.certify true tt minimal
