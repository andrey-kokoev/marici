{-# OPTIONS --safe --cubical --no-import-sorts --guardedness #-}
module LeastDyadicExponentSearch where

open import Cubical.Foundations.Prelude
open import Cubical.Data.Nat as ℕ using (ℕ; zero; suc)
import Cubical.Data.Nat.Order as ℕOrder
open import Cubical.Data.Sum
open import Cubical.Data.Empty as Empty
open import Cubical.Relation.Nullary
open import Cubical.Data.Rationals as Q
open import Cubical.Data.Rationals.Order
open import Cubical.HITs.PropositionalTruncation as PT
open import DyadicallyBoundedCauchy
open import RationalArchimedean
open import LeastDyadicExponent

least-dyadic-from-upper-bound :
  (q : Q.ℚ) (n : ℕ) → q ≤ dyadicRadius n → LeastDyadicExponent q
least-dyadic-from-upper-bound q zero qBound = record
  { least-exponent = zero
  ; least-dominates = qBound
  ; least-minimal = λ m _ → ℕOrder.zero-≤
  }
least-dyadic-from-upper-bound q (suc n) qBound
  with ≤Dec q (dyadicRadius n)
... | yes qPrevious = least-dyadic-from-upper-bound q n qPrevious
... | no qNotPrevious = record
  { least-exponent = suc n
  ; least-dominates = qBound
  ; least-minimal = minimal
  }
  where
  minimal : (m : ℕ) → q ≤ dyadicRadius m → ℕOrder._≤_ (suc n) m
  minimal m qM with ℕOrder.splitℕ-≤ (suc n) m
  ... | inl successorLeM = successorLeM
  ... | inr mLtSuccessor = Empty.rec
      (qNotPrevious
        (isTrans≤ q (dyadicRadius m) (dyadicRadius n)
          qM
          (dyadicRadius-monotone m n
            (ℕOrder.pred-≤-pred mLtSuccessor))))

least-dyadic-from-dominance :
  (q : Q.ℚ) → DyadicDominates q → LeastDyadicExponent q
least-dyadic-from-dominance q =
  PT.rec (least-dyadic-exponent-isProp q)
    (λ { (n , qBound) → least-dyadic-from-upper-bound q n qBound })

preferred-least-dyadic-exponent-principle :
  RationalLeastDyadicExponentPrinciple
preferred-least-dyadic-exponent-principle .select-least-dyadic q =
  least-dyadic-from-dominance q
    (truncated-ceiling-principle-gives-dyadic-dominance
      (raw-ceiling-gives-truncated-principle
        preferred-raw-rational-natural-ceiling) q)
