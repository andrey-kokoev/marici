{-# OPTIONS --safe --cubical --guardedness #-}
module NandConstructions where

open import Cubical.Foundations.Prelude
open import Cubical.Foundations.Equiv
open import Cubical.Foundations.Isomorphism
open import Cubical.Data.Bool.Base using (Bool; true; false)
open import Cubical.Data.Unit.Base using (Unit; tt)
open import Cubical.Data.Empty.Base using (⊥; rec)
open import Cubical.Data.Sigma.Base using (_×_)
import WholePackageSigmaPi as Whole
import WholePackageResolution as Resolution

open Whole.Universe ℓ-zero
-- Constructor route: input-dependent Pi into an explicitly supplied empty type.
pairCode : Type → Type → Code
pairCode A B = E A (λ _ → atom B)
nandCode : Type → Type → Code
nandCode A B = Pi (El (pairCode A B)) (λ _ → atom ⊥)
curriedCode : Type → Type → Code
curriedCode A B = Pi A (λ _ → Pi B (λ _ → atom ⊥))

curryIso : (A B : Type) → Iso (El (nandCode A B)) (El (curriedCode A B))
Iso.fun (curryIso A B) f a b = f (a , b)
Iso.inv (curryIso A B) g (a , b) = g a b
Iso.rightInv (curryIso A B) g = refl
Iso.leftInv (curryIso A B) f = refl

-- The empty target itself can be expressed as E over an empty index.
emptySumCode : Code
emptySumCode = E ⊥ (λ ())
emptySumIso : Iso (El emptySumCode) ⊥
Iso.fun emptySumIso (() , v)
Iso.inv emptySumIso ()
Iso.rightInv emptySumIso ()
Iso.leftInv emptySumIso (() , v)
emptySumNandCode : Type → Type → Code
emptySumNandCode A B = Pi (El (pairCode A B)) (λ _ → emptySumCode)
emptyTargetIso : (A B : Type) → Iso (El (emptySumNandCode A B)) (El (nandCode A B))
Iso.fun (emptyTargetIso A B) f ab = Iso.fun emptySumIso (f ab)
Iso.inv (emptyTargetIso A B) g ab = Iso.inv emptySumIso (g ab)
Iso.rightInv (emptyTargetIso A B) g = funExt (λ ab → Iso.rightInv emptySumIso (g ab))
Iso.leftInv (emptyTargetIso A B) f = funExt (λ ab → Iso.leftInv emptySumIso (f ab))

Truth : Bool → Type
Truth false = ⊥
Truth true = Unit
nand : Bool → Bool → Bool
nand false b = true
nand true false = true
nand true true = false

emptyLeft : (B : Type) → Iso ((⊥ × B) → ⊥) Unit
Iso.fun (emptyLeft B) f = tt
Iso.inv (emptyLeft B) tt = λ { (() , b) }
Iso.rightInv (emptyLeft B) tt = refl
Iso.leftInv (emptyLeft B) f = funExt λ { (() , b) }
emptyRight : (A : Type) → Iso ((A × ⊥) → ⊥) Unit
Iso.fun (emptyRight A) f = tt
Iso.inv (emptyRight A) tt = λ { (a , ()) }
Iso.rightInv (emptyRight A) tt = refl
Iso.leftInv (emptyRight A) f = funExt λ { (a , ()) }
fullPair : Iso ((Unit × Unit) → ⊥) ⊥
Iso.fun fullPair f = f (tt , tt)
Iso.inv fullPair ()
Iso.rightInv fullPair ()
Iso.leftInv fullPair f = rec (f (tt , tt))

-- Actual equivalence of value types for four Boolean inputs, not just counts.
nand-realization : (a b : Bool) → El (nandCode (Truth a) (Truth b)) ≃ Truth (nand a b)
nand-realization false b = isoToEquiv (emptyLeft (Truth b))
nand-realization true false = isoToEquiv (emptyRight Unit)
nand-realization true true = isoToEquiv fullPair

wolfram : (a b c : Bool)
  → nand (nand (nand a b) c) (nand a (nand (nand a c) a)) ≡ c
wolfram false false false = refl
wolfram false false true = refl
wolfram false true false = refl
wolfram false true true = refl
wolfram true false false = refl
wolfram true false true = refl
wolfram true true false = refl
wolfram true true true = refl

-- Reuse the existing resolution constructor to retain the typed curry
-- comparison. The function witness f is supplied explicitly.
module Retained (A B : Type) (f : El (nandCode A B)) where
  open Resolution.Generators ℓ-zero
  direct curried : Complete
  direct = pack (nandCode A B) f
  curried = pack (curriedCode A B) (Iso.fun (curryIso A B) f)
  data Seeds : Complete → Type₁ where
    direct-seed : Seeds direct
    curried-seed : Seeds curried
  comparisonRule : Rule
  comparisonRule = compare-rule direct curried (isoToEquiv (curryIso A B)) refl
  derivation : Resolve Seeds (output comparisonRule)
  derivation = apply comparisonRule
    λ { (lift true) → seed direct-seed ; (lift false) → seed curried-seed }
  nextQ : Whole.Universe.Complete (ℓ-suc ℓ-zero)
  nextQ = Whole.Universe.pack (Whole.Universe.atom (Closure Seeds))
    (output comparisonRule , derivation)
  recovered-derivation : snd (Whole.Universe.value nextQ) ≡ derivation
  recovered-derivation = refl

module Concrete = Retained ⊥ Unit (λ { (() , b) })

-- Empty joint input makes the actual Pi rule applicable with no seed data.
-- This is a constructor derivation, in addition to the equivalence checks.
module VacuousConstruction (B : Type) where
  open Resolution.Generators ℓ-zero
  family : (⊥ × B) → Complete
  family (() , b)
  emptySeeds : Complete → Type₁
  emptySeeds q = Lift ⊥
  rule : Rule
  rule = Pi-rule (⊥ × B) family
  derivation : Resolve emptySeeds (output rule)
  derivation = apply rule (λ { (lift (() , b)) })

