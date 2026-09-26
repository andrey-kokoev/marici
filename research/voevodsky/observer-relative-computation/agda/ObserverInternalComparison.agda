{-# OPTIONS --safe --cubical --guardedness #-}
module ObserverInternalComparison where

open import Cubical.Foundations.Prelude
open import Cubical.Foundations.Univalence using (uaβ)
open import Cubical.Data.Sigma.Base using (Σ; _,_; fst; snd)
open import Cubical.Data.Bool.Base using (Bool; true; false)
open import Cubical.Data.Bool.Properties using (notEquiv; true≢false)
open import Cubical.Data.Empty.Base using (⊥)
import IndexIdentityCoherenceRegression as Cover
import IndexIdentityCoherence as Indexed
module Ix = Indexed.Indexed ℓ-zero

-- Finite comparison syntax; no evaluator or access callback is stored.
data ComparisonCode : Type where
  stationary turn : ComparisonCode

Reply = Ix.Index Cover.F
base : Reply
base = Cover.base-index

interpret : ComparisonCode → base ≡ base
interpret stationary = refl
interpret turn = Cover.index-loop

record Package : Type where
  constructor package
  field
    code : ComparisonCode
    comparison : base ≡ base
    certified : comparison ≡ interpret code

make : (c : ComparisonCode) → Package
make c = package c (interpret c) refl

-- Distinction is semantic: the actual paths differ, not merely labels.
fixed-witnesses-distinct : interpret turn ≡ interpret stationary → ⊥
fixed-witnesses-distinct = Cover.loop-is-not-reflexive

fixed-read : (base ≡ base) → Bool
fixed-read p = subst (Ix.Fibre Cover.F) p true

stationary-read : fixed-read (interpret stationary) ≡ true
stationary-read = substRefl {B = Ix.Fibre Cover.F} {x = base} true

turn-read : fixed-read (interpret turn) ≡ false
turn-read = uaβ notEquiv true

-- When the reply can move, the full based path space is contractible.
Total : Type
Total = Σ Reply (λ y → base ≡ y)

forget-fixed : ComparisonCode → Total
forget-fixed c = base , interpret c

center : Total
center = base , refl

contract : (q : Total) → center ≡ q
contract (y , p) i = p i , (λ j → p (i ∧ j))

total-contractible : isContr Total
total-contractible = center , contract

same-total-certificate : forget-fixed stationary ≡ forget-fixed turn
same-total-certificate = contract (forget-fixed turn)

-- A constant Bool-valued observer on Total cannot extend fixed-read
-- at both chosen fixed-reply certificates.
no-constant-extension : (read : Total → Bool)
  → read (forget-fixed stationary) ≡ true
  → read (forget-fixed turn) ≡ false → ⊥
no-constant-extension read flat twisted = true≢false
  (sym flat ∙ cong read same-total-certificate ∙ twisted)

-- The correct readout has a dependent codomain. Moving the reply also
-- transports its fibre; it does NOT produce a constant-codomain counterexample.
dependent-read : (q : Total) → Ix.Fibre Cover.F (fst q)
dependent-read q = subst (Ix.Fibre Cover.F) (snd q) true

dependent-comparison : PathP
  (λ i → Ix.Fibre Cover.F (fst (same-total-certificate i)))
  (dependent-read (forget-fixed stationary))
  (dependent-read (forget-fixed turn))
dependent-comparison i = dependent-read (same-total-certificate i)
