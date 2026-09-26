{-# OPTIONS --safe --cubical --guardedness #-}
module ResolutionNetSubstitution where

open import Cubical.Foundations.Prelude
open import CoherenceResolutionClosure

-- H can describe typed input slots. A valuation supplies actual resolutions,
-- not a proof that missing slots have already been filled.
module Bridge {ℓ : Level}
  (P : Type ℓ) (U : P → P → Type ℓ) (V : P → P → P → Type ℓ) where
  open Closure P U V

  plug : {H S : P → Type ℓ}
       → ((p : P) → H p → Resolve S p)
       → {p : P} → Resolve H p → Resolve S p
  plug f d = flatten (mapSeeds f d)

  plug-unit : {S : P → Type ℓ} {p : P} (d : Resolve S p)
            → plug (λ _ → seed) d ≡ d
  plug-unit = unit-right

  plug-compose : {H S T : P → Type ℓ}
               → (f : (p : P) → H p → Resolve S p)
               → (g : (p : P) → S p → Resolve T p)
               → {p : P} (d : Resolve H p)
               → plug g (plug f d) ≡ plug (λ p h → plug g (f p h)) d
  plug-compose f g (seed h) = refl
  plug-compose f g (unary u d) = cong (unary u) (plug-compose f g d)
  plug-compose f g (binary v d e) i =
    binary v (plug-compose f g d i) (plug-compose f g e i)

  -- Filling slots before or after eliminating an outer closure layer agrees.
  plug-flatten : {H S : P → Type ℓ}
               → (f : (p : P) → H p → Resolve S p)
               → {p : P} (d : Resolve (Resolve H) p)
               → plug f (flatten d) ≡ flatten (mapSeeds (λ _ → plug f) d)
  plug-flatten f (seed d) = refl
  plug-flatten f (unary u d) = cong (unary u) (plug-flatten f d)
  plug-flatten f (binary v d e) i =
    binary v (plug-flatten f d i) (plug-flatten f e i)

  plug-cong : {H S : P → Type ℓ}
            → (f g : (p : P) → H p → Resolve S p)
            → ((p : P) (h : H p) → f p h ≡ g p h)
            → {p : P} (d : Resolve H p) → plug f d ≡ plug g d
  plug-cong f g eq (seed h) = eq _ h
  plug-cong f g eq (unary u d) = cong (unary u) (plug-cong f g eq d)
  plug-cong f g eq (binary v d e) i =
    binary v (plug-cong f g eq d i) (plug-cong f g eq e i)
