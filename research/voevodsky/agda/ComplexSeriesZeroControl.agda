{-# OPTIONS --safe --cubical --no-import-sorts --guardedness #-}
module ComplexSeriesZeroControl where

open import Cubical.Foundations.Prelude
open import Cubical.Data.Nat as ℕ using (ℕ; zero; suc)
open import Cubical.Data.Rationals as Q
open import Cubical.Data.Rationals.Order
open import RegularCauchyStructure
open import CauchyProductBounds
open import ConstructiveComplexCompletion
open import ComplexCauchyApproximation
open import ComplexSeriesCompletion

zeroComplexTerms : ℕ → RationalComplex
zeroComplexTerms n = zeroRationalComplex

zeroComplexSeries : ScheduledComplexSeries
zeroComplexSeries = naturalComplexSeriesSchedule zeroComplexTerms

zero-complex-finite-sum : (n : ℕ) →
  rationalComplexFiniteSum zeroComplexTerms n ≡ zeroRationalComplex
zero-complex-finite-sum zero = refl
zero-complex-finite-sum (suc n) =
  cong (_+rationalComplex zeroRationalComplex) (zero-complex-finite-sum n)

zero-complex-series-tail :
  OrderedComplexSeriesTailCertificate zeroComplexSeries
zero-complex-series-tail .forwardDifferenceBound m n m≤n =
  subst (λ value → ComplexMagnitudeBound value (precision m))
    (sym (cong₂ complexDifference
      (zero-complex-finite-sum n) (zero-complex-finite-sum m)))
    (zero-complex-magnitude-bound (precision m) (precision-nonnegative m))

zero-complex-series-completion-certificate :
  ComplexSeriesCompletionCertificate
zero-complex-series-completion-certificate =
  completionCertificateFromOrderedTail zeroComplexSeries
    (naturalComplexSeriesSchedule-is-cofinal zeroComplexTerms)
    zero-complex-series-tail

zero-complex-series-completion : ComplexCompletion
zero-complex-series-completion =
  completedComplexSeries zero-complex-series-completion-certificate
