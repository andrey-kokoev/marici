{-# OPTIONS --safe --cubical --guardedness #-}
module RamseySingleFrameFaces where
open import Cubical.Foundations.Prelude
open import Cubical.Data.Nat.Base using (ℕ; zero; suc; _+_)
open import Cubical.Data.Unit.Base using (Unit; tt)
open import Cubical.Data.Empty.Base using (⊥)
open import Cubical.Relation.Nullary using (¬_)
open import RamseyUniformRelative using (Slot; first; next)

data Vertex : Type where
  c0 m0 c1 m1 : Vertex
M-role : Vertex → ℕ
M-role c0 = 0
M-role m0 = 1
M-role c1 = 0
M-role m1 = 1
face : Vertex → Slot 3 → Vertex
face c0 first = m0
face c0 (next first) = c1
face c0 (next (next first)) = m1
face c0 (next (next (next ())))
face m0 first = c0
face m0 (next first) = c1
face m0 (next (next first)) = m1
face m0 (next (next (next ())))
face c1 first = c0
face c1 (next first) = m0
face c1 (next (next first)) = m1
face c1 (next (next (next ())))
face m1 first = c0
face m1 (next first) = m0
face m1 (next (next first)) = c1
face m1 (next (next (next ())))
count : (Slot 3 → ℕ) → ℕ
count f = f first + (f (next first) + f (next (next first)))
M-count : Vertex → ℕ
M-count v = count (λ i → M-role (face v i))
Eligible : Vertex → Type
Eligible v = M-count v ≡ 2
c-faces : Σ (Eligible c0) (λ _ → Eligible c1)
c-faces = refl , refl
OneNat : ℕ → Type
OneNat zero = ⊥
OneNat (suc zero) = Unit
OneNat (suc (suc n)) = ⊥
one-not-two : ¬ (1 ≡ 2)
one-not-two p = transport (cong OneNat p) tt
blocked-m0 : ¬ Eligible m0
blocked-m0 = one-not-two
blocked-m1 : ¬ Eligible m1
blocked-m1 = one-not-two
no-full-frame : ¬ ((v : Vertex) → Eligible v)
no-full-frame all-faces = blocked-m0 (all-faces m0)
reader : Vertex → Vertex
reader c0 = c1
reader c1 = c0
reader m0 = m1
reader m1 = m0
reader-preserves-role : (v : Vertex) → M-role (reader v) ≡ M-role v
reader-preserves-role c0 = refl
reader-preserves-role c1 = refl
reader-preserves-role m0 = refl
reader-preserves-role m1 = refl

-- This proof does not depend on coordinates or enumeration of sample chambers.
module Realization (Carrier : Type) (frame : Vertex → Carrier)
  (role : Carrier → ℕ) (agrees : (v : Vertex) → role (frame v) ≡ M-role v) where
  actual-count : Vertex → ℕ
  actual-count v = count (λ i → role (frame (face v i)))
  count-cell : (v : Vertex) → actual-count v ≡ M-count v
  count-cell v = cong₂ _+_ (agrees (face v first))
    (cong₂ _+_ (agrees (face v (next first))) (agrees (face v (next (next first)))))
  no-full-role-preserving-map : ¬ ((v : Vertex) → actual-count v ≡ 2)
  no-full-role-preserving-map all-faces = one-not-two (sym (count-cell m0) ∙ all-faces m0)
