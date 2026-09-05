{-# OPTIONS --safe --cubical --no-import-sorts --guardedness #-}
module RationalArchimedean where

open import Cubical.Foundations.Prelude
open import Cubical.Data.Nat as ℕ using (ℕ; suc; _+_)
open import Cubical.Data.NatPlusOne using (ℕ₊₁; 1+_)
open import Cubical.Data.Int as ℤ using (ℤ; pos; negsuc)
import Cubical.Data.Int.Order as ℤOrder
open import Cubical.Data.Rationals as Q
open import Cubical.Data.Rationals.Order
open import Cubical.Data.Sigma
open import Cubical.HITs.PropositionalTruncation as PT
open import Cubical.HITs.SetQuotients as SQ
open import DyadicallyBoundedCauchy

-- Exact next interface. The library's preferred rationals are a set quotient,
-- so extracting an exponent requires either a quotient-invariant magnitude
-- algorithm or set-valued elimination with a proof that all choices induce
-- the same completed product.
DyadicDominates : Q.ℚ → Type
DyadicDominates q = ∥ Σ[ n ∈ ℕ ] q ≤ dyadicRadius n ∥₁

dyadic-dominates-isProp : (q : Q.ℚ) → isProp (DyadicDominates q)
dyadic-dominates-isProp q = isPropPropTrunc

record LeastDyadicExponent (q : Q.ℚ) : Type where
  field
    least-exponent : ℕ
    least-dominates : q ≤ dyadicRadius least-exponent
    least-minimal : (m : ℕ) → q ≤ dyadicRadius m →
      Σ[ k ∈ ℕ ] k ℕ.+ least-exponent ≡ m
open LeastDyadicExponent public


record RationalLeastDyadicExponentPrinciple : Type where
  field
    select-least-dyadic : (q : Q.ℚ) → LeastDyadicExponent q
open RationalLeastDyadicExponentPrinciple public

record ArchimedeanExponent (q : Q.ℚ) : Type where
  field
    exponent : ℕ
    dominates : q ≤ dyadicRadius exponent
open ArchimedeanExponent public

least-dyadic-gives-exponent : (q : Q.ℚ) →
  LeastDyadicExponent q → ArchimedeanExponent q
least-dyadic-gives-exponent q least = record
  { exponent = least-exponent least
  ; dominates = least-dominates least
  }

least-principle-gives-exponent :
  RationalLeastDyadicExponentPrinciple →
  (q : Q.ℚ) → ArchimedeanExponent q
least-principle-gives-exponent principle q =
  least-dyadic-gives-exponent q (select-least-dyadic principle q)

witness-gives-truncated : (q : Q.ℚ) →
  ArchimedeanExponent q → DyadicDominates q
witness-gives-truncated q w = ∣ exponent w , dominates w ∣₁

NaturalCeiling : Q.ℚ → Type
NaturalCeiling q = Σ[ n ∈ ℕ ] q ≤ natℚ n

natural-ceiling-gives-exponent : (q : Q.ℚ) →
  NaturalCeiling q → ArchimedeanExponent q
natural-ceiling-gives-exponent q (n , q≤n) = record
  { exponent = n
  ; dominates = isTrans≤ q (natℚ n) (dyadicRadius n)
      q≤n (natℚ≤dyadicRadius n)
  }

natural-ceiling-gives-dyadic-dominance : (q : Q.ℚ) →
  NaturalCeiling q → DyadicDominates q
natural-ceiling-gives-dyadic-dominance q ceiling =
  witness-gives-truncated q (natural-ceiling-gives-exponent q ceiling)

record RationalNaturalCeilingPrinciple : Type where
  field
    ceiling : (q : Q.ℚ) → NaturalCeiling q
open RationalNaturalCeilingPrinciple public

natural-ceiling-principle-gives-dyadic-dominance :
  RationalNaturalCeilingPrinciple →
  (q : Q.ℚ) → DyadicDominates q
natural-ceiling-principle-gives-dyadic-dominance principle q =
  natural-ceiling-gives-dyadic-dominance q (ceiling principle q)

TruncatedNaturalCeiling : Q.ℚ → Type
TruncatedNaturalCeiling q = ∥ NaturalCeiling q ∥₁

truncated-natural-ceiling-isProp : (q : Q.ℚ) →
  isProp (TruncatedNaturalCeiling q)
truncated-natural-ceiling-isProp q = isPropPropTrunc

record RationalTruncatedNaturalCeilingPrinciple : Type where
  field
    truncated-ceiling : (q : Q.ℚ) → TruncatedNaturalCeiling q
open RationalTruncatedNaturalCeilingPrinciple public

RawRationalNaturalCeiling : Type
RawRationalNaturalCeiling =
  (a : ℤ) (b : ℕ₊₁) → NaturalCeiling (Q.[_/_] a b)

positive-raw-rational≤numerator : (n : ℕ) (b : ℕ₊₁) →
  Q.[_/_] (pos n) b ≤ Q.[_/_] (pos n) 1
positive-raw-rational≤numerator n (1+ d) =
  subst2 ℤOrder._≤_
    (ℤ.·Comm (pos 1) (pos n))
    (ℤ.·Comm (pos (suc d)) (pos n))
    (ℤOrder.≤-·o
      (ℤOrder.suc-≤-suc (ℤOrder.zero-≤pos {l = d})))

negative-raw-rational≤zero : (n : ℕ) (b : ℕ₊₁) →
  Q.[_/_] (negsuc n) b ≤ 0
negative-raw-rational≤zero n b =
  subst2 ℤOrder._≤_
    (sym (ℤ.·IdR (negsuc n)))
    (sym (ℤ.·AnnihilL (Q.ℕ₊₁→ℤ b)))
    (ℤOrder.<-weaken ℤOrder.negsuc<-zero)

preferred-raw-rational-natural-ceiling : RawRationalNaturalCeiling
preferred-raw-rational-natural-ceiling (pos n) b =
  n , subst (Q.[_/_] (pos n) b ≤_)
    (sym (natℚ-representative n))
    (positive-raw-rational≤numerator n b)
preferred-raw-rational-natural-ceiling (negsuc n) b =
  0 , negative-raw-rational≤zero n b

raw-ceiling-gives-truncated-principle :
  RawRationalNaturalCeiling → RationalTruncatedNaturalCeilingPrinciple
raw-ceiling-gives-truncated-principle raw .truncated-ceiling =
  SQ.elimProp truncated-natural-ceiling-isProp
    λ { (a , b) → ∣ raw a b ∣₁ }

truncated-natural-ceiling-gives-dyadic-dominance :
  (q : Q.ℚ) → TruncatedNaturalCeiling q → DyadicDominates q
truncated-natural-ceiling-gives-dyadic-dominance q =
  PT.rec isPropPropTrunc
    (λ ceiling → witness-gives-truncated q
      (natural-ceiling-gives-exponent q ceiling))

truncated-ceiling-principle-gives-dyadic-dominance :
  RationalTruncatedNaturalCeilingPrinciple →
  (q : Q.ℚ) → DyadicDominates q
truncated-ceiling-principle-gives-dyadic-dominance principle q =
  truncated-natural-ceiling-gives-dyadic-dominance q
    (truncated-ceiling principle q)
