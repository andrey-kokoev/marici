{-# OPTIONS --safe --cubical --guardedness #-}
module ObserverRRCWitnessSynthesis where

open import Cubical.Foundations.Prelude
open import Cubical.Foundations.Equiv
open import Cubical.Data.Sigma.Base using (Σ; _,_)
open import Cubical.Data.Bool.Base using (Bool; true; false)
open import Cubical.Data.Bool.Properties using (notEquiv; true≢false; false≢true)
open import Cubical.Data.Empty.Base using (⊥) renaming (rec to absurd)
open import Cubical.Relation.Nullary.Base using (Dec; yes; no)
import WholePackageSigmaPi as W
import WholePackageResolution as RRC

module U = W.Universe ℓ-zero
module R = RRC.Generators ℓ-zero

data Mode : Type where
  identity swap : Mode

equivalence : Mode → Bool ≃ Bool
equivalence identity = idEquiv Bool
equivalence swap = notEquiv

packet : Bool → U.Complete
packet b = U.pack (U.atom Bool) b

-- Only the two explicitly exhibited Boolean packets are source generators.
Source : U.Complete → Type₁
Source q = Lift {j = ℓ-zero} (Σ Bool (λ b → packet b ≡ q))

source : (b : Bool) → R.Resolve Source (packet b)
source b = R.seed (lift (b , refl))

Boundary : Mode → Bool → Bool → Type
Boundary m x y = equivFun (equivalence m) x ≡ y

record Solution (m : Mode) (x y : Bool) : Type₁ where
  constructor solved
  field
    witness : Boundary m x y
    history : R.Resolve Source (U.comparison-package (packet x) (packet y) (equivalence m) witness)
open Solution public

-- A constructor used AFTER the algorithm has computed its boundary proof.
construct : (m : Mode) (x y : Bool) → Boundary m x y → Solution m x y
construct m x y p = solved p (R.apply (R.compare-rule (packet x) (packet y) (equivalence m) p) premises)
  where
  premises : (i : Lift Bool) → R.Resolve Source (R.input (R.compare-rule (packet x) (packet y) (equivalence m) p) i)
  premises (lift true) = source x
  premises (lift false) = source y

decideBool : (x y : Bool) → Dec (x ≡ y)
decideBool true true = yes refl
decideBool true false = no true≢false
decideBool false true = no false≢true
decideBool false false = yes refl

-- Total decision procedure: no equivalence or equality oracle argument.
-- The negative branch excludes EVERY Solution, not merely one route.
synthesize : (m : Mode) (x y : Bool) → Dec (Solution m x y)
synthesize m x y with decideBool (equivFun (equivalence m) x) y
... | yes p = yes (construct m x y p)
... | no impossible = no (λ candidate → impossible (witness candidate))

synthesis-complete : (m : Mode) (x y : Bool) → Solution m x y
  → Σ (Solution m x y) (λ result → synthesize m x y ≡ yes result)
synthesis-complete m x y candidate with synthesize m x y
... | yes result = result , refl
... | no impossible = absurd (impossible candidate)

-- Unspecified mode can always be chosen for these two source values.
choose : Bool → Bool → Mode
choose true true = identity
choose true false = swap
choose false true = swap
choose false false = identity

chosen-boundary : (x y : Bool) → Boundary (choose x y) x y
chosen-boundary true true = refl
chosen-boundary true false = refl
chosen-boundary false true = refl
chosen-boundary false false = refl

synthesize-any : (x y : Bool) → Σ Mode (λ m → Solution m x y)
synthesize-any x y = choose x y , construct (choose x y) x y (chosen-boundary x y)

-- Explicit positive and impossible-boundary regressions.
swap-true-false : Solution swap true false
swap-true-false = construct swap true false refl

identity-true-false-impossible : Solution identity true false → ⊥
identity-true-false-impossible candidate = true≢false (witness candidate)

positive-computes : synthesize swap true false ≡ yes swap-true-false
positive-computes = refl

negative-computes : synthesize identity true false ≡ no identity-true-false-impossible
negative-computes = refl
