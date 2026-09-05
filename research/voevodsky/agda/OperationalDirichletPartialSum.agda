{-# OPTIONS --safe --cubical --no-import-sorts --guardedness #-}
module OperationalDirichletPartialSum where

open import Cubical.Foundations.Prelude
open import Cubical.Data.Nat as ℕ using (ℕ; zero; suc)
open import ConstructiveComplexCompletion
open import RationalLogTaylorApproximants
open import RationalLogConvergenceContract
open import AtanhPowerDecayContract
open import AtanhTailBounds
open import OperationalDirichletTerm

PositiveNaturalLogHalfBlockFamily : Type
PositiveNaturalLogHalfBlockFamily =
  (n : ℕ) → AtanhHalfContractingBlock (positiveNaturalLogRatio n)
    (positive-natural-log-atanh-contraction n
      (reciprocal-bridge-gives-gap-certificate
        canonicalPositiveNaturalLogReciprocalBridge n))

canonicalPositiveNaturalLogHalfBlocks : PositiveNaturalLogHalfBlockFamily
canonicalPositiveNaturalLogHalfBlocks n =
  contraction-gives-half-block (positiveNaturalLogRatio n)
    (positive-natural-log-atanh-contraction n
      (reciprocal-bridge-gives-gap-certificate
        canonicalPositiveNaturalLogReciprocalBridge n))

PositiveNaturalLogEvaluationFamily : Type
PositiveNaturalLogEvaluationFamily =
  (n : ℕ) → PositiveNaturalLogEvaluationInput n

log-evaluation-family-from-half-blocks :
  PositiveNaturalLogHalfBlockFamily → PositiveNaturalLogEvaluationFamily
log-evaluation-family-from-half-blocks blocks n .gap =
  reciprocal-bridge-gives-gap-certificate
    canonicalPositiveNaturalLogReciprocalBridge n
log-evaluation-family-from-half-blocks blocks n .halfBlock = blocks n

canonicalPositiveNaturalLogEvaluationFamily : PositiveNaturalLogEvaluationFamily
canonicalPositiveNaturalLogEvaluationFamily =
  log-evaluation-family-from-half-blocks canonicalPositiveNaturalLogHalfBlocks

log-evaluation-family-from-power-principle :
  DyadicGapHalfPowerPrinciple →
  ((n : ℕ) → PositiveNaturalLogGapCertificate n) →
  PositiveNaturalLogEvaluationFamily
log-evaluation-family-from-power-principle principle gaps n .gap = gaps n
log-evaluation-family-from-power-principle principle gaps n .halfBlock =
  power-principle-gives-half-block principle (positiveNaturalLogRatio n)
    (positive-natural-log-atanh-contraction n (gaps n))

operationalDirichletPartialSum :
  PositiveNaturalLogEvaluationFamily →
  ComplexCompletion → ℕ → ComplexCompletion
operationalDirichletPartialSum logarithms s zero =
  operationalPositiveNaturalDirichletTerm zero (logarithms zero) s
operationalDirichletPartialSum logarithms s (suc cutoff) =
  operationalDirichletPartialSum logarithms s cutoff +complex
  operationalPositiveNaturalDirichletTerm (suc cutoff)
    (logarithms (suc cutoff)) s

canonicalOperationalDirichletPartialSum :
  ComplexCompletion → ℕ → ComplexCompletion
canonicalOperationalDirichletPartialSum =
  operationalDirichletPartialSum canonicalPositiveNaturalLogEvaluationFamily

operationalDirichletPartialSumFromPowerPrinciple :
  DyadicGapHalfPowerPrinciple →
  ((n : ℕ) → PositiveNaturalLogGapCertificate n) →
  ComplexCompletion → ℕ → ComplexCompletion
operationalDirichletPartialSumFromPowerPrinciple principle gaps =
  operationalDirichletPartialSum
    (log-evaluation-family-from-power-principle principle gaps)

operationalFirstDirichletTerm :
  ComplexCompletion → ComplexCompletion
operationalFirstDirichletTerm = operationalDirichletTermOne

operationalFirstTwoDirichletTerms :
  ComplexCompletion → ComplexCompletion
operationalFirstTwoDirichletTerms s =
  operationalDirichletTermOne s +complex operationalDirichletTermTwo s
