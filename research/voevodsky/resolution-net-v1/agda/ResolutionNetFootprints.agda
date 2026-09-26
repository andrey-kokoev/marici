{-# OPTIONS --safe --cubical --guardedness #-}
module ResolutionNetFootprints where

open import Cubical.Foundations.Prelude
open import Cubical.Data.Nat.Base using (ℕ; zero; suc; _+_)
open import CoherenceResolutionClosure

data Status : Type where
  absent free spent : Status

data Empty : Type where

data Owned : Status → Type where
  owns-free : Owned free
  owns-spent : Owned spent

data Fresh : Status → Type where
  fresh-absent : Fresh absent
  fresh-free : Fresh free

data Change : Status → Status → Type where
  stay : (a : Status) → Change a a
  consume : Change free spent

-- Separation concerns OWNERSHIP, including spent resources.
data Separate : Status → Status → Status → Type where
  from-right : (b : Status) → Separate absent b b
  from-left : (a : Status) → Separate a absent a

owned-count spent-count : Status → ℕ
owned-count absent = zero
owned-count free = suc zero
owned-count spent = suc zero
spent-count absent = zero
spent-count free = zero
spent-count spent = suc zero

charge : {a b : Status} → Change a b → ℕ
charge (stay a) = zero
charge consume = suc zero

change-spent : {a b : Status} (c : Change a b)
             → charge c + spent-count a ≡ spent-count b
change-spent (stay a) = refl
change-spent consume = refl

change-owned : {a b : Status} → Change a b → owned-count a ≡ owned-count b
change-owned (stay a) = refl
change-owned consume = refl

join-spent : {a b c : Status} → Separate a b c
           → spent-count a + spent-count b ≡ spent-count c
join-spent (from-right b) = refl
join-spent (from-left absent) = refl
join-spent (from-left free) = refl
join-spent (from-left spent) = refl

join-owned : {a b c : Status} → Separate a b c
           → owned-count a + owned-count b ≡ owned-count c
join-owned (from-right b) = refl
join-owned (from-left absent) = refl
join-owned (from-left free) = refl
join-owned (from-left spent) = refl

fresh-zero : {a : Status} → Fresh a → zero ≡ spent-count a
fresh-zero fresh-absent = refl
fresh-zero fresh-free = refl

no-overlap : {a b c : Status} → Separate a b c → Owned a → Owned b → Empty
no-overlap (from-right b) () _
no-overlap (from-left a) _ ()

data AtMostOne : ℕ → Type where
  none : AtMostOne zero
  once : AtMostOne (suc zero)

owned-bound : (s : Status) → AtMostOne (owned-count s)
owned-bound absent = none
owned-bound free = once
owned-bound spent = once

spent-bound : (s : Status) → AtMostOne (spent-count s)
spent-bound absent = none
spent-bound free = none
spent-bound spent = once

module Resources (Token : Type) where
  World = Token → Status
  U : World → World → Type
  U a b = (t : Token) → Change (a t) (b t)
  V : World → World → World → Type
  V a b c = (t : Token) → Separate (a t) (b t) (c t)
  Initial : World → Type
  Initial w = (t : Token) → Fresh (w t)

  open Closure World U V

  uses origins : {w : World} → Resolve Initial w → Token → ℕ
  uses (seed s) t = zero
  uses (unary u d) t = charge (u t) + uses d t
  uses (binary v d e) t = uses d t + uses e t
  origins {w} (seed s) t = owned-count (w t)
  origins (unary u d) t = origins d t
  origins (binary v d e) t = origins d t + origins e t

  use-accounting : {w : World} (d : Resolve Initial w) (t : Token)
                 → uses d t ≡ spent-count (w t)
  use-accounting (seed s) t = fresh-zero (s t)
  use-accounting (unary u d) t = cong (charge (u t) +_) (use-accounting d t) ∙ change-spent (u t)
  use-accounting (binary v d e) t = cong₂ _+_ (use-accounting d t) (use-accounting e t) ∙ join-spent (v t)

  origin-accounting : {w : World} (d : Resolve Initial w) (t : Token)
                    → origins d t ≡ owned-count (w t)
  origin-accounting (seed s) t = refl
  origin-accounting (unary u d) t = origin-accounting d t ∙ change-owned (u t)
  origin-accounting (binary v d e) t = cong₂ _+_ (origin-accounting d t) (origin-accounting e t) ∙ join-owned (v t)

  no-double-spend : {w : World} (d : Resolve Initial w) (t : Token) → AtMostOne (uses d t)
  no-double-spend {w} d t = subst AtMostOne (sym (use-accounting d t)) (spent-bound (w t))

  no-duplicate-origin : {w : World} (d : Resolve Initial w) (t : Token) → AtMostOne (origins d t)
  no-duplicate-origin {w} d t = subst AtMostOne (sym (origin-accounting d t)) (owned-bound (w t))

module TwoTokenExample where
  data Token : Type where
    a b : Token
  open Resources Token
  open Closure World U V

  left right final : World
  left a = free
  left b = absent
  right a = absent
  right b = free
  final _ = spent

  used-left used-right : World
  used-left a = spent
  used-left b = absent
  used-right a = absent
  used-right b = spent

  left-seed : Initial left
  left-seed a = fresh-free
  left-seed b = fresh-absent
  right-seed : Initial right
  right-seed a = fresh-absent
  right-seed b = fresh-free

  spend-a : U left used-left
  spend-a a = consume
  spend-a b = stay absent
  spend-b : U right used-right
  spend-b a = stay absent
  spend-b b = consume

  separate : V used-left used-right final
  separate a = from-left spent
  separate b = from-right spent

  combined : Resolve Initial final
  combined = binary separate (unary spend-a (seed left-seed))
                             (unary spend-b (seed right-seed))

  a-used-once : uses combined a ≡ suc zero
  a-used-once = use-accounting combined a
  b-used-once : uses combined b ≡ suc zero
  b-used-once = use-accounting combined b

  -- A spent owner cannot join an unused duplicate of the SAME token.
  reject-revival : {c : Status} → Separate spent free c → Empty
  reject-revival proof = no-overlap proof owns-spent owns-free
