{-# OPTIONS --safe --cubical --guardedness #-}
module ResolutionNetCompression where

open import Cubical.Foundations.Prelude
open import Cubical.Data.Nat.Base using (suc; _+_)
open import CoherenceResolutionClosure
open import ResolutionNetLocalSimulation
open import ResolutionNetTermination

module Compression {ℓ : Level}
  (P : Type ℓ) (U : P → P → Type ℓ) (V : P → P → P → Type ℓ)
  (S : P → Type ℓ) where
  open Closure P U V
  open Local P U V S
  open Termination P U V S

  -- Administrative representation changes, not execution of rule witnesses.
  data Compact : {p : P} → Term p → Term p → Type ℓ where
    same : {p : P} {t : Term p} → Compact t t
    chain : {p : P} {t m w : Term p} → Compact t m → Compact m w → Compact t w
    pack-one : {p q : P} (u : U p q) (d : Resolve S p)
             → Compact (one u (keep d)) (keep (unary u d))
    pack-two : {p q r : P} (v : V p q r) (d : Resolve S p) (e : Resolve S q)
             → Compact (two v (keep d) (keep e)) (keep (binary v d e))
    in-one : {p q : P} (u : U p q) {t w : Term p}
           → Compact t w → Compact (one u t) (one u w)
    in-two : {p q r : P} (v : V p q r) {t t' : Term p} {w w' : Term q}
           → Compact t t' → Compact w w' → Compact (two v t w) (two v t' w')

  compact-sound : {p : P} {t w : Term p} → Compact t w → interpret t ≡ interpret w
  compact-sound same = refl
  compact-sound (chain a b) = compact-sound a ∙ compact-sound b
  compact-sound (pack-one u d) = refl
  compact-sound (pack-two v d e) = refl
  compact-sound (in-one u c) = cong (unary u) (compact-sound c)
  compact-sound (in-two v a b) = cong₂ (binary v) (compact-sound a) (compact-sound b)

  compact-work : {p : P} {t w : Term p} → Compact t w → work t ≡ work w
  compact-work same = refl
  compact-work (chain a b) = compact-work a ∙ compact-work b
  compact-work (pack-one u d) = refl
  compact-work (pack-two v d e) = refl
  compact-work (in-one u c) = compact-work c
  compact-work (in-two v a b) = cong₂ _+_ (compact-work a) (compact-work b)

  -- The concrete port diagram should supply these TWO witnesses, not only
  -- equality of endpoint denotations. Constructing them for Python is separate.
  data RepresentedStep {p : P} (t w : Term p) : Type ℓ where
    represented : {m : Term p} → t ↝ m → Compact m w → RepresentedStep t w

  represented-sound : {p : P} {t w : Term p}
                    → RepresentedStep t w → interpret t ≡ interpret w
  represented-sound (represented r c) = step-sound r ∙ compact-sound c

  represented-work : {p : P} {t w : Term p}
                   → RepresentedStep t w → work t ≡ suc (work w)
  represented-work (represented r c) = step-work r ∙ cong suc (compact-work c)
