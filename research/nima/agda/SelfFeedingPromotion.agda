{-# OPTIONS --safe --cubical --guardedness #-}
module SelfFeedingPromotion where

open import Cubical.Foundations.Prelude
open import Cubical.Data.Nat.Base using (ℕ; zero; suc)
open import Cubical.Data.Bool.Base using (Bool; false; true)
open import Cubical.Data.Bool.Properties using (true≢false)
open import Cubical.Data.Empty.Base using (rec)
open import Cubical.Data.Sigma.Base using (_×_)
open import Cubical.Data.List.Base using (List; []; _∷_; map; length)
open import Cubical.Data.FinData.Base using (Fin; toℕ) renaming (zero to fzero; suc to fsuc)
import RetainedRelationshipPromotion as Promotion

all : (n : ℕ) → List (Fin n)
all zero = []
all (suc n) = fzero ∷ map fsuc (all n)
less : ℕ → ℕ → Bool
less zero zero = false
less zero (suc n) = true
less (suc m) zero = false
less (suc m) (suc n) = less m n
lookup : {A : Type} (xs : List A) → Fin (length xs) → A
lookup (x ∷ xs) fzero = x
lookup (x ∷ xs) (fsuc i) = lookup xs i
eqFin : {n : ℕ} → Fin n → Fin n → Bool
eqFin fzero fzero = true
eqFin fzero (fsuc y) = false
eqFin (fsuc x) fzero = false
eqFin (fsuc x) (fsuc y) = eqFin x y
eqFin-sound : {n : ℕ} (x y : Fin n) → eqFin x y ≡ true → x ≡ y
eqFin-sound fzero fzero p = refl
eqFin-sound fzero (fsuc y) p = rec (true≢false (sym p))
eqFin-sound (fsuc x) fzero p = rec (true≢false (sym p))
eqFin-sound (fsuc x) (fsuc y) p = cong fsuc (eqFin-sound x y p)

record Graph : Type where
  constructor graph
  field
    vertex-count edge-count : ℕ
    ends : Fin edge-count → Fin vertex-count × Fin vertex-count
open Graph

module Step (g : Graph) where
  V = Fin (vertex-count g)
  E = Fin (edge-count g)
  before : E → E → Bool
  before x y = less (toℕ x) (toℕ y)
  module P = Promotion.Promote V E (all (vertex-count g)) (all (edge-count g))
    (ends g) before eqFin eqFin-sound

  -- IDs are positions in the GENERATED witnessed connection list.
  -- Its payload remains available under exactly that index.
  generated : Fin (length P.connections) → P.Connection
  generated = lookup P.connections
  next-ends : Fin (length P.connections) → E × E
  next-ends i = P.Connection.left (generated i) , P.Connection.right (generated i)
  output : Graph
  output = graph (edge-count g) (length P.connections) next-ends
  retained = P.run
  -- Exact typed incidence witnesses for each newly indexed connection.
  left-incidence : (i : Fin (length P.connections))
    → P.EndpointWitness (P.Connection.shared (generated i)) (fst (next-ends i))
  left-incidence i = P.real-left (generated i)
  right-incidence : (i : Fin (length P.connections))
    → P.EndpointWitness (P.Connection.shared (generated i)) (snd (next-ends i))
  right-incidence i = P.real-right (generated i)

successor : Graph → Graph
successor g = Step.output g
Bundle : Graph → Type₁
Bundle g = Step.P.RetainedPromotion g
bundle : (g : Graph) → Bundle g
bundle g = Step.retained g

-- An iteration retains its actual predecessor and the generated fiber package.
-- The carrier is promoted structurally, not supplied afresh by the caller.
data History : Graph → Type₁ where
  initial : (g : Graph) → History g
  promoted : {g : Graph} → History g → Bundle g → History (successor g)

iterate : ℕ → Graph → Graph
iterate zero g = g
iterate (suc n) g = successor (iterate n g)
run : (n : ℕ) (g : Graph) → History (iterate n g)
run zero g = initial g
run (suc n) g = promoted (run n g) (bundle (iterate n g))

origin : {g : Graph} → History g → Graph
origin (initial g) = g
origin (promoted h receipt) = origin h
origin-run : (n : ℕ) (g : Graph) → origin (run n g) ≡ g
origin-run zero g = refl
origin-run (suc n) g = origin-run n g

either : Bool → Bool → Bool
either false b = b
either true b = true
both : Bool → Bool → Bool
both false b = false
both true b = b
any : {A : Type} → (A → Bool) → List A → Bool
any f [] = false
any f (x ∷ xs) = either (f x) (any f xs)
adjacent : (g : Graph) → Fin (vertex-count g) → Fin (vertex-count g) → Bool
adjacent g u v = any matches (all (edge-count g))
  where
  matches : Fin (edge-count g) → Bool
  matches e = either
    (both (eqFin u (fst (ends g e))) (eqFin v (snd (ends g e))))
    (both (eqFin v (fst (ends g e))) (eqFin u (snd (ends g e))))
