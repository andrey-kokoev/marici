{-# OPTIONS --safe --cubical --no-import-sorts --guardedness #-}
module CauchyCompletionRelation where

open import Cubical.Foundations.Prelude
open import Cubical.Foundations.HLevels
open import Cubical.Data.Nat using (ℕ)
open import Cubical.Data.Rationals as Q
open import Cubical.Data.Rationals.Order
open import Cubical.Data.Sigma
open import Cubical.HITs.PropositionalTruncation as PT
open import Cubical.HITs.SetQuotients as SQ
  using ([_]; squash/)
  renaming (_/_ to _//_)
open import Cubical.Relation.Binary.Base
open BinaryRelation
open import RegularCauchyStructure

-- A rational lies observably below a regular sequence when this is witnessed
-- at some approximation with an explicit precision margin.
LowerObservation : RegularCauchy → Q.ℚ → Type
LowerObservation x q =
  ∥ Σ[ n ∈ ℕ ] (q Q.+ precision n < approximation x n) ∥₁

lower-isProp : (x : RegularCauchy) (q : Q.ℚ) →
  isProp (LowerObservation x q)
lower-isProp x q = isPropPropTrunc

-- Two sequences are identified only when every rational lower observation is
-- logically equivalent. This avoids the non-transitive fixed-error relation.
infix 4 _≈cut_
_≈cut_ : RegularCauchy → RegularCauchy → Type
x ≈cut y = (q : Q.ℚ) →
  (LowerObservation x q → LowerObservation y q) ×
  (LowerObservation y q → LowerObservation x q)

≈cut-isProp : (x y : RegularCauchy) → isProp (x ≈cut y)
≈cut-isProp x y = isPropΠ λ q →
  isProp× (isProp→ (lower-isProp y q))
          (isProp→ (lower-isProp x q))

≈cut-refl : isRefl _≈cut_
≈cut-refl x q = (λ z → z) , (λ z → z)

≈cut-sym : isSym _≈cut_
≈cut-sym x y r q = snd (r q) , fst (r q)

≈cut-trans : isTrans _≈cut_
≈cut-trans x y z r s q =
  (λ obs → fst (s q) (fst (r q) obs)) ,
  (λ obs → snd (r q) (snd (s q) obs))

≈cut-isEquivRel : isEquivRel _≈cut_
isEquivRel.reflexive ≈cut-isEquivRel = ≈cut-refl
isEquivRel.symmetric ≈cut-isEquivRel = ≈cut-sym
isEquivRel.transitive ≈cut-isEquivRel = ≈cut-trans

-- This quotient is a completion candidate. Calling it a constructive real
-- still requires inhabitedness, cut axioms, rational embedding, and descended
-- field operations.
CauchyCompletionCandidate : Type
CauchyCompletionCandidate = RegularCauchy // _≈cut_

embedℚ : Q.ℚ → CauchyCompletionCandidate
embedℚ q = [ constantCauchy q ]

candidate-zero : CauchyCompletionCandidate
candidate-zero = embedℚ 0

candidate-isSet : isSet CauchyCompletionCandidate
candidate-isSet = squash/
