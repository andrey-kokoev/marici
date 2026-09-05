{-# OPTIONS --safe --cubical --no-import-sorts --guardedness #-}
module RegularCauchyStructure where

open import Cubical.Foundations.Prelude
open import Cubical.Data.Nat as ℕ using (ℕ; zero; suc; _+_)
import Cubical.Data.Nat.Order as ℕOrder
import Cubical.Data.Int.Order as ℤOrder
open import Cubical.Data.Rationals as Q
open import Cubical.Data.Rationals.Order
open import RationalAnalyticSubstrate

-- Dyadic precision is chosen so one refinement exactly absorbs the doubled
-- error produced by binary operations.
precision : ℕ → Q.ℚ
precision zero = 1
precision (suc n) = halfℚ (precision n)

one-half-nonnegative : 0 ≤ one-half
one-half-nonnegative = ℤOrder.zero-≤pos

half-nonnegative : (q : Q.ℚ) → 0 ≤ q → 0 ≤ halfℚ q
half-nonnegative q 0≤q =
  subst (λ z → z ≤ halfℚ q) (Q.·AnnihilL one-half)
    (≤-·o 0 q one-half one-half-nonnegative 0≤q)

precision-nonnegative : (n : ℕ) → 0 ≤ precision n
precision-nonnegative zero = ℤOrder.zero-≤pos
precision-nonnegative (suc n) =
  half-nonnegative (precision n) (precision-nonnegative n)

precision-refines-double : (n : ℕ) →
  precision (suc n) Q.+ precision (suc n) ≡ precision n
precision-refines-double n =
  sym (Q.·DistL+ (precision n) one-half one-half) ∙
  cong (precision n Q.·_) one-half-double ∙
  Q.·IdR (precision n)

≤-add-nonnegative : (q e : Q.ℚ) → 0 ≤ e → q ≤ q Q.+ e
≤-add-nonnegative q e 0≤e =
  subst (λ z → z ≤ q Q.+ e) (Q.+IdR q) (≤-o+ 0 e q 0≤e)

precision-step≤ : (n : ℕ) → precision (suc n) ≤ precision n
precision-step≤ n =
  subst (precision (suc n) ≤_) (precision-refines-double n)
    (≤-add-nonnegative (precision (suc n)) (precision (suc n))
      (precision-nonnegative (suc n)))

precision-antitone-add : (d n : ℕ) →
  precision (d ℕ.+ n) ≤ precision n
precision-antitone-add zero n = isRefl≤ (precision n)
precision-antitone-add (suc d) n =
  isTrans≤ (precision (suc (d ℕ.+ n))) (precision (d ℕ.+ n))
    (precision n) (precision-step≤ (d ℕ.+ n))
    (precision-antitone-add d n)

precision-antitone : (m n : ℕ) → ℕOrder._≤_ m n →
  precision n ≤ precision m
precision-antitone m n (d , d+m≡n) =
  subst (λ j → precision j ≤ precision m) d+m≡n
    (precision-antitone-add d m)

-- Regular Cauchy data. The two directed inequalities avoid assuming an
-- absolute-value interface not supplied for the preferred rational carrier.
record RegularCauchy : Type where
  field
    approximation : ℕ → Q.ℚ
    close-forward : (m n : ℕ) →
      approximation m ≤
      (approximation n Q.+ precision m) Q.+ precision n
    close-backward : (m n : ℕ) →
      approximation n ≤
      (approximation m Q.+ precision m) Q.+ precision n

open RegularCauchy public

regularCauchy-ext : (x y : RegularCauchy) →
  approximation x ≡ approximation y → x ≡ y
regularCauchy-ext x y approximationPath i .approximation =
  approximationPath i
regularCauchy-ext x y approximationPath i .close-forward m n =
  isProp→PathP
    (λ j → isProp≤
      (approximationPath j m)
      ((approximationPath j n Q.+ precision m) Q.+ precision n))
    (close-forward x m n) (close-forward y m n) i
regularCauchy-ext x y approximationPath i .close-backward m n =
  isProp→PathP
    (λ j → isProp≤
      (approximationPath j n)
      ((approximationPath j m Q.+ precision m) Q.+ precision n))
    (close-backward x m n) (close-backward y m n) i

constantCauchy : Q.ℚ → RegularCauchy
constantCauchy q .approximation n = q
constantCauchy q .close-forward m n =
  isTrans≤ q (q Q.+ precision m)
    ((q Q.+ precision m) Q.+ precision n)
    (≤-add-nonnegative q (precision m) (precision-nonnegative m))
    (≤-add-nonnegative (q Q.+ precision m) (precision n)
      (precision-nonnegative n))
constantCauchy q .close-backward m n =
  isTrans≤ q (q Q.+ precision m)
    ((q Q.+ precision m) Q.+ precision n)
    (≤-add-nonnegative q (precision m) (precision-nonnegative m))
    (≤-add-nonnegative (q Q.+ precision m) (precision n)
      (precision-nonnegative n))

-- A bounded comparison at each sequence's own precision. This is deliberately
-- not proposed as the completion equivalence: transitivity would add error
-- bounds and therefore requires a separately proved precision-refinement law.
record CauchyNearAtOwnPrecision (x y : RegularCauchy) : Type where
  field
    near-left : (n : ℕ) →
      approximation x n ≤ approximation y n Q.+ precision n
    near-right : (n : ℕ) →
      approximation y n ≤ approximation x n Q.+ precision n

-- The precompletion carrier needed by the next layer is now explicit.
-- Constructing the equivalence relation, quotient, and descended operations
-- remain separate obligations.
PrecompletionCarrier : Type
PrecompletionCarrier = RegularCauchy
