{-# OPTIONS --safe --cubical --guardedness #-}
module NestedWitnessTransport where

open import Cubical.Foundations.Prelude
open import Cubical.Data.Bool.Base using (Bool; true; false; not)
open import Cubical.Data.Bool.Properties using (true≢false)
open import Cubical.Data.Empty.Base using (⊥)

-- Free marked syntax: this declares the attachment constructor; it does
-- not derive a physical attachment rule from the frozen native signature.
data Term : Type where
  core : Term
  attach : Term → Bool → Term

flip-twice : (e : Bool) → not (not e) ≡ e
flip-twice false = refl
flip-twice true = refl

exchange : Term → Term
exchange core = core
exchange (attach parent e) = attach (exchange parent) (not e)

exchange-twice : (t : Term) → exchange (exchange t) ≡ t
exchange-twice core = refl
exchange-twice (attach parent e) i =
  attach (exchange-twice parent i) (flip-twice e i)

attachment-natural : (parent : Term) (e : Bool)
  → exchange (attach parent e) ≡ attach (exchange parent) (not e)
attachment-natural parent e = refl

parent-of : Term → Term
parent-of core = core
parent-of (attach parent e) = parent

parent-transport : (t : Term)
  → parent-of (exchange t) ≡ exchange (parent-of t)
parent-transport core = refl
parent-transport (attach parent e) = refl

nested : Term
nested = attach (attach core false) true

outer-label : Term → Bool
outer-label core = false
outer-label (attach parent e) = e

-- Exchange is a structural transport, not equality of marked syntax.
nested-distinct : nested ≡ exchange nested → ⊥
nested-distinct equality = true≢false (cong outer-label equality)
