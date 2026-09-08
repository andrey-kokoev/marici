{-# OPTIONS --safe --cubical --guardedness #-}
module ReesTwoChartMonomials where

open import Cubical.Foundations.Prelude
open import Cubical.Data.Nat using (ℕ; zero; suc)
open import Cubical.Data.Int using (ℤ; pos; negsuc)

-- Overlap monomial X^a t^b e_X for the dualizing line e_X=1/X.
-- These are exponent descriptors, not inverses adjoined to the base ring.
record OverlapMonomial : Type where
  constructor overlapMonomial
  field
    xDegree : ℕ
    tDegree : ℤ

add : ℕ → ℕ → ℕ
add zero n = n
add (suc m) n = suc (add m n)

-- For b=n>=0 the monomial extends to the X-chart.
-- It extends to both charts exactly when a=n+1+k for some k>=0.
-- Otherwise n=a+k, and only the X-chart admits it.
data NonnegativeClassification (a n : ℕ) : Type where
  onlyX : (gap : ℕ) → n ≡ add a gap → NonnegativeClassification a n
  both : (baseX : ℕ) → a ≡ suc (add n baseX)
    → NonnegativeClassification a n

classifyNonnegative : (a n : ℕ) → NonnegativeClassification a n
classifyNonnegative zero n = onlyX n refl
classifyNonnegative (suc a) zero = both a refl
classifyNonnegative (suc a) (suc n) with classifyNonnegative a n
... | onlyX gap equation = onlyX gap (cong suc equation)
... | both baseX equation = both baseX (cong suc equation)

-- Negative b=-1-j always extends to the u-chart, never the X-chart.
-- In u-chart coordinates u^a s^(a+j) e_u equals X^a t^(-1-j) e_X.
data ChartCover : OverlapMonomial → Type where
  negativeU : (a j : ℕ) → ChartCover (overlapMonomial a (negsuc j))
  nonnegative : (a n : ℕ) → NonnegativeClassification a n
    → ChartCover (overlapMonomial a (pos n))

coverEveryMonomial : (m : OverlapMonomial) → ChartCover m
coverEveryMonomial (overlapMonomial a (negsuc j)) = negativeU a j
coverEveryMonomial (overlapMonomial a (pos n)) = nonnegative a n (classifyNonnegative a n)

-- Explicit transition in the u-chart: u^a s^j e_u becomes
-- X^a t^(a-j-1) e_X. Use integers without subtraction by recording cases.
record UChartNegativeCoordinates : Type where
  constructor uNegative
  field
    uDegree : ℕ
    excess : ℕ

negativeCoordinates : (a j : ℕ) → UChartNegativeCoordinates
negativeCoordinates a j = uNegative a j

uChartSDegree : UChartNegativeCoordinates → ℕ
uChartSDegree (uNegative a j) = add a j

negativeOverlap : UChartNegativeCoordinates → OverlapMonomial
negativeOverlap (uNegative a j) = overlapMonomial a (negsuc j)

negativeRoundtrip : (a j : ℕ) → negativeOverlap (negativeCoordinates a j)
  ≡ overlapMonomial a (negsuc j)
negativeRoundtrip a j = refl

-- Common sections are encoded by the actual base exponents X^k u^n.
-- Their overlapMonomial representative is X^(n+k+1) t^n e_X.
record BaseMonomial : Type where
  constructor base
  field
    baseXDegree baseUDegree : ℕ

baseToOverlap : BaseMonomial → OverlapMonomial
baseToOverlap (base k n) = overlapMonomial (suc (add n k)) (pos n)

baseHasBothCharts : (k n : ℕ)
  → NonnegativeClassification (suc (add n k)) n
baseHasBothCharts k n = both k refl

-- Every common-monomial certificate reconstructs a base monomial.
reconstructCommon : (a n k : ℕ) → a ≡ suc (add n k)
  → baseToOverlap (base k n) ≡ overlapMonomial a (pos n)
reconstructCommon a n k equation =
  cong (λ degree → overlapMonomial degree (pos n)) (sym equation)

predecessor : ℕ → ℕ
predecessor zero = zero
predecessor (suc n) = n

cancelAddedPrefix : (n k l : ℕ) → add n k ≡ add n l → k ≡ l
cancelAddedPrefix zero k l equation = equation
cancelAddedPrefix (suc n) k l equation =
  cancelAddedPrefix n k l (cong predecessor equation)

-- The reconstructed base X exponent is unique at the given overlap degrees.
commonBaseExponentUnique : (a n k l : ℕ)
  → a ≡ suc (add n k) → a ≡ suc (add n l) → k ≡ l
commonBaseExponentUnique a n k l left right =
  cancelAddedPrefix n k l (cong predecessor (sym left ∙ right))

-- Executable regression descriptors: no finite sample is used as the proof.
unitBaseRepresentative : baseToOverlap (base zero zero)
  ≡ overlapMonomial (suc zero) (pos zero)
unitBaseRepresentative = refl

-- t^m alone as a dualizing section (a=0) is X-chart-only.
localPositivePower : (m : ℕ) → NonnegativeClassification zero m
localPositivePower m = onlyX m refl

-- X^(m+1)t^m e_X represents u^m and belongs to both charts.
correctedPositivePower : (m : ℕ)
  → NonnegativeClassification (suc (add m zero)) m
correctedPositivePower m = both zero refl

-- Each overlapMonomial coefficient is therefore present in at least one chart.
-- No Cech differential, derived pushforward, S-linear trace, or base-change
-- theorem is asserted by this combinatorial module alone.
