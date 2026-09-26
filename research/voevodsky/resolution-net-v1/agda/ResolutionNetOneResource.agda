{-# OPTIONS --safe --cubical --guardedness #-}
module ResolutionNetOneResource where

open import Cubical.Foundations.Prelude
open import Cubical.Data.Nat.Base using (ℕ; zero; suc)
open import CoherenceResolutionClosure

data World : Type where
  fresh used : World

-- Two distinct use witnesses exhibit alternative histories; neither restores
-- a used token. Arbitrarily many idle steps remain possible.
data Use : World → World → Type where
  idle : {w : World} → Use w w
  spend-left spend-right : Use fresh used

data NoJoin : World → World → World → Type where

data Initial : World → Type where
  initial : Initial fresh

open Closure World Use NoJoin

uses : {w : World} → Resolve Initial w → ℕ
uses (seed initial) = zero
uses (unary idle d) = uses d
uses (unary spend-left d) = suc (uses d)
uses (unary spend-right d) = suc (uses d)
uses (binary () d e)

spent-count : World → ℕ
spent-count fresh = zero
spent-count used = suc zero

-- Every history has exactly the use count dictated by its endpoint.
-- In particular no admitted history spends the single resource twice.
accounting : {w : World} (d : Resolve Initial w) → uses d ≡ spent-count w
accounting (seed initial) = refl
accounting (unary idle d) = accounting d
accounting (unary spend-left d) = cong suc (accounting d)
accounting (unary spend-right d) = cong suc (accounting d)
accounting (binary () d e)

left-history right-history : Resolve Initial used
left-history = unary spend-left (seed initial)
right-history = unary spend-right (seed initial)

-- Both alternative histories are legal. This type contains no mechanism
-- choosing which one is the externally committed transition.
left-once : uses left-history ≡ suc zero
left-once = accounting left-history
right-once : uses right-history ≡ suc zero
right-once = accounting right-history
