{-# OPTIONS --safe --cubical --guardedness #-}
module ObserverSignedBoundAdmission where

open import Cubical.Foundations.Prelude
open import Cubical.Data.Sigma.Base using (Σ; _,_; fst; snd)
open import Cubical.Data.Nat.Base using (ℕ; suc; _+_)
open import Cubical.Data.Nat.Order using (_≤_; suc-≤-suc; ≤-k+; ≤-trans; ≤SumLeft; ≤SumRight)
open import Cubical.Data.Empty.Base using (⊥)
open import Cubical.HITs.PropositionalTruncation.Base using (∣_∣₁)
import Cubical.Data.Int.Base as Z
import Cubical.Data.Int.Properties as ZP
import ObserverSignedNormalization as N
import ObserverSignedBounded as D

-- Admission supplies an actual slot, rather than assuming a representation.
Admission : ℕ → Z.ℤ → Type
Admission bound z = Σ (D.Slot bound) (λ x → N.integer (D.offset bound x) ≡ z)

positive-arithmetic : (bound n : ℕ)
  → (Z.- Z.pos bound) Z.+ Z.pos (bound + n) ≡ Z.pos n
positive-arithmetic bound n = cong (λ z → (Z.- Z.pos bound) Z.+ z) (ZP.pos+ bound n)
  ∙ ZP.+Assoc (Z.- Z.pos bound) (Z.pos bound) (Z.pos n)
  ∙ cong (λ z → z Z.+ Z.pos n) (ZP.-Cancel' (Z.pos bound))
  ∙ sym (ZP.pos0+ (Z.pos n))

negative-arithmetic : (slack n : ℕ)
  → (Z.- Z.pos (slack + suc n)) Z.+ Z.pos slack ≡ Z.negsuc n
negative-arithmetic slack n = ZP.inj-z+ {z = Z.pos (slack + suc n)}
  (ZP.+Assoc (Z.pos (slack + suc n)) (Z.- Z.pos (slack + suc n)) (Z.pos slack)
    ∙ cong (λ z → z Z.+ Z.pos slack) (ZP.-Cancel (Z.pos (slack + suc n)))
    ∙ sym (ZP.pos0+ (Z.pos slack))
    ∙ sym (cong (λ z → z Z.+ Z.negsuc n) (ZP.pos+ slack (suc n))
      ∙ ZP.plusMinus (Z.pos (suc n)) (Z.pos slack)))

positive-slot : (slack n : ℕ) → D.Slot (slack + n)
positive-slot slack n = (slack + n) + n , suc-≤-suc
  (≤-k+ {k = slack + n} (≤SumRight {n = n} {k = slack}))

negative-slot : (slack n : ℕ) → D.Slot (slack + suc n)
negative-slot slack n = slack , suc-≤-suc
  (≤-trans (≤SumLeft {n = slack} {k = suc n})
    (≤SumLeft {n = slack + suc n} {k = slack + suc n}))

-- Nat ≤ contains slack + magnitude = bound. Transport the whole
-- admission along that equality, avoiding specialized indexed matches.
admit-integer : (bound : ℕ) (z : Z.ℤ) → Z.abs z ≤ bound → Admission bound z
admit-integer bound (Z.pos n) (slack , e) = subst (λ b → Admission b (Z.pos n)) e
  (positive-slot slack n , D.offset-integer (slack + n) (positive-slot slack n)
    ∙ positive-arithmetic (slack + n) n)
admit-integer bound (Z.negsuc n) (slack , e) = subst (λ b → Admission b (Z.negsuc n)) e
  (negative-slot slack n , D.offset-integer (slack + suc n) (negative-slot slack n)
    ∙ negative-arithmetic slack n)

admit-path : (bound : ℕ) (p : N.Loop) → Z.abs (N.integer p) ≤ bound → D.Bounded bound p
admit-path bound p numerical with admit-integer bound (N.integer p) numerical
... | x , e = ∣ x , N.complete (D.offset bound x) p e ∣₁

recover-numerical : (bound : ℕ) (p : N.Loop) → Z.abs (N.integer p) ≤ bound
  → D.recover bound (D.read bound p) ≡ p
recover-numerical bound p numerical = D.faithful bound p (admit-path bound p numerical)

common : N.Loop → N.Loop → ℕ
common p q = Z.abs (N.integer p) + Z.abs (N.integer q)

common-separates : (p q : N.Loop)
  → D.read (common p q) p ≡ D.read (common p q) q → p ≡ q
common-separates p q = D.separates (common p q) p q
  (admit-path (common p q) p ≤SumLeft)
  (admit-path (common p q) q ≤SumRight)

pairwise-separation : (p q : N.Loop) → (p ≡ q → ⊥)
  → D.read (common p q) p ≡ D.read (common p q) q → ⊥
pairwise-separation p q different e = different (common-separates p q e)

all-calibrated-probes-faithful : (p q : N.Loop)
  → ((bound : ℕ) → D.read bound p ≡ D.read bound q) → p ≡ q
all-calibrated-probes-faithful p q agreement = common-separates p q (agreement (common p q))
