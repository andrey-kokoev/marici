{-# OPTIONS --safe --cubical --no-import-sorts --guardedness #-}
module ComplexSeriesCompletion where

open import Cubical.Foundations.Prelude
open import Cubical.Data.Nat as ℕ using (ℕ; zero; suc)
import Cubical.Data.Nat.Order as ℕOrder
open import Cubical.Data.Rationals as Q
open import Cubical.Data.Rationals.Order
open import Cubical.Data.Sum
open import Cubical.Algebra.CommRing
open import Cubical.Tactics.CommRingSolver
open import RationalAnalyticSubstrate
open import RegularCauchyStructure
open import CauchyProductBounds
open import CauchyProductCongruence
open import CauchyProductErrorBounds
open import ConstructiveComplexCompletion
open import ComplexCauchyApproximation

module RegularDifferencePaths {ℓ} (R : CommRing ℓ) where
  open CommRingStr (snd R) renaming (_+_ to _+S_; -_ to -S_)

  cancel-translated-right : (x y p q : fst R) →
    ((y +S p) +S q) +S (-S y) ≡ p +S q
  cancel-translated-right x y p q = solve! R

  negate-difference : (x y : fst R) →
    -S (x +S (-S y)) ≡ y +S (-S x)
  negate-difference x y = solve! R

regular-approximation-difference-bound : (x : RegularCauchy) (m n : ℕ) →
  MagnitudeBound
    (approximation x m Q.+ (Q.- approximation x n))
    (precision m Q.+ precision n)
regular-approximation-difference-bound x m n .positive-upper =
  let translated = ≤-+o
        (approximation x m)
        ((approximation x n Q.+ precision m) Q.+ precision n)
        (Q.- approximation x n)
        (close-forward x m n)
  in subst
    ((approximation x m Q.+ (Q.- approximation x n)) ≤_)
    (RegularDifferencePaths.cancel-translated-right PreferredℚCommRing
      (approximation x m) (approximation x n) (precision m) (precision n))
    translated
regular-approximation-difference-bound x m n .negative-upper =
  subst (_≤ precision m Q.+ precision n)
    (sym (RegularDifferencePaths.negate-difference PreferredℚCommRing
      (approximation x m) (approximation x n)))
    (let translated = ≤-+o
           (approximation x n)
           ((approximation x m Q.+ precision m) Q.+ precision n)
           (Q.- approximation x m)
           (close-backward x m n)
     in subst
       ((approximation x n Q.+ (Q.- approximation x m)) ≤_)
       (RegularDifferencePaths.cancel-translated-right PreferredℚCommRing
         (approximation x n) (approximation x m) (precision m) (precision n))
       translated)

record ComplexMagnitudeBound (z : RationalComplex) (bound : Q.ℚ) : Type where
  field
    realBound : MagnitudeBound (rationalRealPart z) bound
    imaginaryBound : MagnitudeBound (rationalImaginaryPart z) bound
open ComplexMagnitudeBound public

zero-complex-magnitude-bound : (bound : Q.ℚ) → 0 ≤ bound →
  ComplexMagnitudeBound zeroRationalComplex bound
zero-complex-magnitude-bound bound 0≤bound .realBound = record
  { positive-upper = 0≤bound ; negative-upper = 0≤bound }
zero-complex-magnitude-bound bound 0≤bound .imaginaryBound = record
  { positive-upper = 0≤bound ; negative-upper = 0≤bound }

add-complex-magnitude-bounds :
  (z w : RationalComplex) (Z W : Q.ℚ) →
  ComplexMagnitudeBound z Z → ComplexMagnitudeBound w W →
  ComplexMagnitudeBound (z +rationalComplex w) (Z Q.+ W)
add-complex-magnitude-bounds z w Z W zBound wBound .realBound =
  add-magnitude-bounds _ _ _ _ (realBound zBound) (realBound wBound)
add-complex-magnitude-bounds z w Z W zBound wBound .imaginaryBound =
  add-magnitude-bounds _ _ _ _
    (imaginaryBound zBound) (imaginaryBound wBound)

negate-complex-magnitude-bound : (z : RationalComplex) (bound : Q.ℚ) →
  ComplexMagnitudeBound z bound →
  ComplexMagnitudeBound (negRationalComplex z) bound
negate-complex-magnitude-bound z bound zBound .realBound =
  negate-magnitude-bound _ _ (realBound zBound)
negate-complex-magnitude-bound z bound zBound .imaginaryBound =
  negate-magnitude-bound _ _ (imaginaryBound zBound)

weaken-complex-magnitude-bound : (z : RationalComplex) (small large : Q.ℚ) →
  small ≤ large → ComplexMagnitudeBound z small →
  ComplexMagnitudeBound z large
weaken-complex-magnitude-bound z small large small≤large zBound .realBound =
  weaken-magnitude-bound _ _ large small≤large (realBound zBound)
weaken-complex-magnitude-bound z small large small≤large zBound .imaginaryBound =
  weaken-magnitude-bound _ _ large small≤large (imaginaryBound zBound)

rationalComplexFiniteSum : (ℕ → RationalComplex) → ℕ → RationalComplex
rationalComplexFiniteSum term zero = term zero
rationalComplexFiniteSum term (suc n) =
  rationalComplexFiniteSum term n +rationalComplex term (suc n)

record ScheduledComplexSeries : Type where
  field
    term : ℕ → RationalComplex
    cutoff : ℕ → ℕ
open ScheduledComplexSeries public

naturalComplexSeriesSchedule : (ℕ → RationalComplex) → ScheduledComplexSeries
naturalComplexSeriesSchedule terms .term = terms
naturalComplexSeriesSchedule terms .cutoff n = n

scheduledComplexPartialSum : ScheduledComplexSeries → ℕ → RationalComplex
scheduledComplexPartialSum series n =
  rationalComplexFiniteSum (term series) (cutoff series n)

record CofinalComplexSeriesSchedule (series : ScheduledComplexSeries) : Type where
  field
    cutoffMonotone : (m n : ℕ) → ℕOrder._≤_ m n →
      ℕOrder._≤_ (cutoff series m) (cutoff series n)
    reachesEveryTerm : (k : ℕ) →
      Σ[ stage ∈ ℕ ] ℕOrder._≤_ k (cutoff series stage)
open CofinalComplexSeriesSchedule public

naturalComplexSeriesSchedule-is-cofinal : (terms : ℕ → RationalComplex) →
  CofinalComplexSeriesSchedule (naturalComplexSeriesSchedule terms)
naturalComplexSeriesSchedule-is-cofinal terms .cutoffMonotone m n m≤n = m≤n
naturalComplexSeriesSchedule-is-cofinal terms .reachesEveryTerm k =
  k , ℕOrder.≤-refl

complexDifference : RationalComplex → RationalComplex → RationalComplex
complexDifference z w = z +rationalComplex negRationalComplex w

record OrderedComplexSeriesTailCertificate
  (series : ScheduledComplexSeries) : Type where
  field
    forwardDifferenceBound : (m n : ℕ) → ℕOrder._≤_ m n →
      ComplexMagnitudeBound
        (complexDifference
          (scheduledComplexPartialSum series n)
          (scheduledComplexPartialSum series m))
        (precision m)
open OrderedComplexSeriesTailCertificate public

record ScheduledComplexSeriesDifferenceCertificate
  (series : ScheduledComplexSeries) : Type where
  field
    differenceBound : (m n : ℕ) →
      ComplexMagnitudeBound
        (complexDifference
          (scheduledComplexPartialSum series m)
          (scheduledComplexPartialSum series n))
        (precision m Q.+ precision n)
open ScheduledComplexSeriesDifferenceCertificate public

module ComplexDifferenceRingPaths {ℓ} (R : CommRing ℓ) where
  open CommRingStr (snd R) renaming (_+_ to _+S_; -_ to -S_)

  difference-negate : (a b : fst R) →
    a +S (-S b) ≡ -S (b +S (-S a))
  difference-negate a b = solve! R

module ComplexDifferencePaths where
  negate-difference : (z w : RationalComplex) →
    complexDifference z w ≡ negRationalComplex (complexDifference w z)
  negate-difference (zr , zi) (wr , wi) =
    cong₂ _,_
      (ComplexDifferenceRingPaths.difference-negate
        PreferredℚCommRing zr wr)
      (ComplexDifferenceRingPaths.difference-negate
        PreferredℚCommRing zi wi)

orderedTailGivesDifferenceCertificate :
  (series : ScheduledComplexSeries) →
  OrderedComplexSeriesTailCertificate series →
  ScheduledComplexSeriesDifferenceCertificate series
orderedTailGivesDifferenceCertificate series tail .differenceBound m n
  with ℕOrder.splitℕ-≤ m n
... | inl m≤n =
  let forward = forwardDifferenceBound tail m n m≤n
      reversed = subst
        (λ value → ComplexMagnitudeBound value (precision m))
        (sym (ComplexDifferencePaths.negate-difference
          (scheduledComplexPartialSum series m)
          (scheduledComplexPartialSum series n)))
        (negate-complex-magnitude-bound
          (complexDifference
            (scheduledComplexPartialSum series n)
            (scheduledComplexPartialSum series m))
          (precision m) forward)
  in
  weaken-complex-magnitude-bound _ (precision m)
    (precision m Q.+ precision n)
    (≤-add-nonnegative (precision m) (precision n)
      (precision-nonnegative n)) reversed
... | inr n<m =
  let forward = forwardDifferenceBound tail n m (ℕOrder.<-weaken n<m)
      precisionN≤sum = subst (precision n ≤_)
        (Q.+Comm (precision n) (precision m))
        (≤-add-nonnegative (precision n) (precision m)
          (precision-nonnegative m))
  in
  weaken-complex-magnitude-bound _ (precision n)
    (precision m Q.+ precision n) precisionN≤sum forward

record ScheduledComplexSeriesRegularity
  (series : ScheduledComplexSeries) : Type where
  field
    closeRealForward : (m n : ℕ) →
      rationalRealPart (scheduledComplexPartialSum series m) ≤
      (rationalRealPart (scheduledComplexPartialSum series n) Q.+
        precision m) Q.+ precision n
    closeRealBackward : (m n : ℕ) →
      rationalRealPart (scheduledComplexPartialSum series n) ≤
      (rationalRealPart (scheduledComplexPartialSum series m) Q.+
        precision m) Q.+ precision n
    closeImaginaryForward : (m n : ℕ) →
      rationalImaginaryPart (scheduledComplexPartialSum series m) ≤
      (rationalImaginaryPart (scheduledComplexPartialSum series n) Q.+
        precision m) Q.+ precision n
    closeImaginaryBackward : (m n : ℕ) →
      rationalImaginaryPart (scheduledComplexPartialSum series n) ≤
      (rationalImaginaryPart (scheduledComplexPartialSum series m) Q.+
        precision m) Q.+ precision n
open ScheduledComplexSeriesRegularity public

split-error-directed : (a b p q : Q.ℚ) →
  a Q.+ (Q.- b) ≤ p Q.+ q → a ≤ (b Q.+ p) Q.+ q
split-error-directed a b p q differenceBound =
  subst (a ≤_) (Q.+Assoc b p q)
    (single-difference-bound→directed a b (p Q.+ q) differenceBound)

regularityFromDifferenceCertificate :
  (series : ScheduledComplexSeries) →
  ScheduledComplexSeriesDifferenceCertificate series →
  ScheduledComplexSeriesRegularity series
regularityFromDifferenceCertificate series certificate .closeRealForward m n =
  split-error-directed
    (rationalRealPart (scheduledComplexPartialSum series m))
    (rationalRealPart (scheduledComplexPartialSum series n))
    (precision m) (precision n)
    (positive-upper (realBound (differenceBound certificate m n)))
regularityFromDifferenceCertificate series certificate .closeRealBackward m n =
  split-error-directed
    (rationalRealPart (scheduledComplexPartialSum series n))
    (rationalRealPart (scheduledComplexPartialSum series m))
    (precision m) (precision n)
    (subst
      (λ bound →
        rationalRealPart (scheduledComplexPartialSum series n) Q.+
          (Q.- rationalRealPart (scheduledComplexPartialSum series m)) ≤ bound)
      (Q.+Comm (precision n) (precision m))
      (positive-upper (realBound (differenceBound certificate n m))))
regularityFromDifferenceCertificate series certificate .closeImaginaryForward m n =
  split-error-directed
    (rationalImaginaryPart (scheduledComplexPartialSum series m))
    (rationalImaginaryPart (scheduledComplexPartialSum series n))
    (precision m) (precision n)
    (positive-upper (imaginaryBound (differenceBound certificate m n)))
regularityFromDifferenceCertificate series certificate .closeImaginaryBackward m n =
  split-error-directed
    (rationalImaginaryPart (scheduledComplexPartialSum series n))
    (rationalImaginaryPart (scheduledComplexPartialSum series m))
    (precision m) (precision n)
    (subst
      (λ bound →
        rationalImaginaryPart (scheduledComplexPartialSum series n) Q.+
          (Q.- rationalImaginaryPart (scheduledComplexPartialSum series m)) ≤ bound)
      (Q.+Comm (precision n) (precision m))
      (positive-upper (imaginaryBound (differenceBound certificate n m))))

complexRegularFromSeries :
  (series : ScheduledComplexSeries) →
  ScheduledComplexSeriesRegularity series → ComplexRegular
complexRegularFromSeries series regularity = realRegular , imaginaryRegular
  where
  realRegular : RegularCauchy
  realRegular .approximation n =
    rationalRealPart (scheduledComplexPartialSum series n)
  realRegular .close-forward = closeRealForward regularity
  realRegular .close-backward = closeRealBackward regularity

  imaginaryRegular : RegularCauchy
  imaginaryRegular .approximation n =
    rationalImaginaryPart (scheduledComplexPartialSum series n)
  imaginaryRegular .close-forward = closeImaginaryForward regularity
  imaginaryRegular .close-backward = closeImaginaryBackward regularity

record ComplexSeriesCompletionCertificate : Type₁ where
  field
    series : ScheduledComplexSeries
    cofinalSchedule : CofinalComplexSeriesSchedule series
    regularity : ScheduledComplexSeriesRegularity series
open ComplexSeriesCompletionCertificate public

completionCertificateFromOrderedTail :
  (series : ScheduledComplexSeries) →
  CofinalComplexSeriesSchedule series →
  OrderedComplexSeriesTailCertificate series →
  ComplexSeriesCompletionCertificate
completionCertificateFromOrderedTail series cofinal tail .series = series
completionCertificateFromOrderedTail series cofinal tail .cofinalSchedule = cofinal
completionCertificateFromOrderedTail series cofinal tail .regularity =
  regularityFromDifferenceCertificate series
    (orderedTailGivesDifferenceCertificate series tail)

completedComplexSeries :
  ComplexSeriesCompletionCertificate → ComplexCompletion
completedComplexSeries certificate =
  complexRegularClass
    (complexRegularFromSeries (series certificate) (regularity certificate))
