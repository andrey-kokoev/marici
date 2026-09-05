{-# OPTIONS --safe --cubical --no-import-sorts --guardedness #-}
module CriticalStripZeroContract where

open import Cubical.Foundations.Prelude
open import Cubical.Data.Sigma
open import Cubical.Data.Sum
open import Cubical.HITs.PropositionalTruncation as PT
open import Cubical.Data.Empty
open import Cubical.Relation.Nullary
open import ConstructiveComplexCompletion
open import ConstructiveZetaInterfaces

CriticalStripZero :
  {evaluator : CertifiedRightHalfPlaneDirichletSeries} →
  {continuation : AnalyticContinuationInterface evaluator} →
  CriticalStripInterface continuation → Type
CriticalStripZero {continuation = continuation} strip =
  Σ[ s ∈ CriticalStripPoint strip ]
    certifiedCriticalStrip strip s ×
    (continuationValue continuation (asContinuationPoint strip s) ≡ zeroComplex)

MereCriticalStripZero :
  {evaluator : CertifiedRightHalfPlaneDirichletSeries} →
  {continuation : AnalyticContinuationInterface evaluator} →
  CriticalStripInterface continuation → Type
MereCriticalStripZero strip = ∥ CriticalStripZero strip ∥₁

record CriticalStripNameSystem
  {evaluator : CertifiedRightHalfPlaneDirichletSeries}
  {continuation : AnalyticContinuationInterface evaluator}
  (strip : CriticalStripInterface continuation) : Type₁ where
  field
    Name : Type
    denotesStripPoint : Name → CriticalStripPoint strip
open CriticalStripNameSystem public

NamedCriticalStripZero :
  {evaluator : CertifiedRightHalfPlaneDirichletSeries} →
  {continuation : AnalyticContinuationInterface evaluator} →
  (strip : CriticalStripInterface continuation) →
  CriticalStripNameSystem strip → Type
NamedCriticalStripZero {continuation = continuation} strip naming =
  Σ[ name ∈ Name naming ]
    certifiedCriticalStrip strip (denotesStripPoint naming name) ×
    (continuationValue continuation
      (asContinuationPoint strip (denotesStripPoint naming name)) ≡ zeroComplex)

NoNamedCriticalStripZero :
  {evaluator : CertifiedRightHalfPlaneDirichletSeries} →
  {continuation : AnalyticContinuationInterface evaluator} →
  (strip : CriticalStripInterface continuation) →
  CriticalStripNameSystem strip → Type
NoNamedCriticalStripZero strip naming =
  ¬ NamedCriticalStripZero strip naming

named-critical-strip-zero-gives-zero :
  {evaluator : CertifiedRightHalfPlaneDirichletSeries} →
  {continuation : AnalyticContinuationInterface evaluator} →
  (strip : CriticalStripInterface continuation) →
  (naming : CriticalStripNameSystem strip) →
  NamedCriticalStripZero strip naming → CriticalStripZero strip
named-critical-strip-zero-gives-zero strip naming (name , certificate) =
  denotesStripPoint naming name , certificate

record PointCompleteCriticalStripNaming
  {evaluator : CertifiedRightHalfPlaneDirichletSeries}
  {continuation : AnalyticContinuationInterface evaluator}
  {strip : CriticalStripInterface continuation}
  (naming : CriticalStripNameSystem strip) : Type₁ where
  field
    namesEveryStripPoint : (s : CriticalStripPoint strip) →
      Σ[ name ∈ Name naming ] denotesStripPoint naming name ≡ s
open PointCompleteCriticalStripNaming public

complete-critical-strip-naming-lifts-zero :
  {evaluator : CertifiedRightHalfPlaneDirichletSeries} →
  {continuation : AnalyticContinuationInterface evaluator} →
  (strip : CriticalStripInterface continuation) →
  (naming : CriticalStripNameSystem strip) →
  PointCompleteCriticalStripNaming naming →
  CriticalStripZero strip → NamedCriticalStripZero strip naming
complete-critical-strip-naming-lifts-zero strip naming completeness
  (s , certificate) =
  let named = namesEveryStripPoint completeness s
      name = fst named
      namePath = snd named
  in name , subst
    (λ point → certifiedCriticalStrip strip point ×
      (criticalStripZetaValue strip point ≡ zeroComplex))
    (sym namePath) certificate

complete-naming-no-named-critical-zero-implies-no-zero :
  {evaluator : CertifiedRightHalfPlaneDirichletSeries} →
  {continuation : AnalyticContinuationInterface evaluator} →
  (strip : CriticalStripInterface continuation) →
  (naming : CriticalStripNameSystem strip) →
  PointCompleteCriticalStripNaming naming →
  NoNamedCriticalStripZero strip naming → ¬ CriticalStripZero strip
complete-naming-no-named-critical-zero-implies-no-zero
  strip naming completeness noNamed zero =
  noNamed (complete-critical-strip-naming-lifts-zero
    strip naming completeness zero)

complete-naming-no-named-critical-zero-implies-no-mere-zero :
  {evaluator : CertifiedRightHalfPlaneDirichletSeries} →
  {continuation : AnalyticContinuationInterface evaluator} →
  (strip : CriticalStripInterface continuation) →
  (naming : CriticalStripNameSystem strip) →
  PointCompleteCriticalStripNaming naming →
  NoNamedCriticalStripZero strip naming → ¬ MereCriticalStripZero strip
complete-naming-no-named-critical-zero-implies-no-mere-zero
  strip naming completeness noNamed =
  PT.rec isProp⊥
    (complete-naming-no-named-critical-zero-implies-no-zero
      strip naming completeness noNamed)

certified-zero-and-no-name-refutes-complete-naming :
  {evaluator : CertifiedRightHalfPlaneDirichletSeries} →
  {continuation : AnalyticContinuationInterface evaluator} →
  (strip : CriticalStripInterface continuation) →
  (naming : CriticalStripNameSystem strip) →
  CriticalStripZero strip → NoNamedCriticalStripZero strip naming →
  ¬ PointCompleteCriticalStripNaming naming
certified-zero-and-no-name-refutes-complete-naming
  strip naming zero noNamed completeness =
  noNamed (complete-critical-strip-naming-lifts-zero
    strip naming completeness zero)

mere-zero-and-no-name-refutes-complete-naming :
  {evaluator : CertifiedRightHalfPlaneDirichletSeries} →
  {continuation : AnalyticContinuationInterface evaluator} →
  (strip : CriticalStripInterface continuation) →
  (naming : CriticalStripNameSystem strip) →
  MereCriticalStripZero strip → NoNamedCriticalStripZero strip naming →
  ¬ PointCompleteCriticalStripNaming naming
mere-zero-and-no-name-refutes-complete-naming
  strip naming mereZero noNamed completeness =
  complete-naming-no-named-critical-zero-implies-no-mere-zero
    strip naming completeness noNamed mereZero

record ConstructiveCriticalStripZeroTest
  {evaluator : CertifiedRightHalfPlaneDirichletSeries}
  {continuation : AnalyticContinuationInterface evaluator}
  (strip : CriticalStripInterface continuation) : Type₁ where
  field
    naming : CriticalStripNameSystem strip
    namingDecision :
      NamedCriticalStripZero strip naming ⊎
      NoNamedCriticalStripZero strip naming
open ConstructiveCriticalStripZeroTest public

constructive-test-positive-branch :
  {evaluator : CertifiedRightHalfPlaneDirichletSeries} →
  {continuation : AnalyticContinuationInterface evaluator} →
  (strip : CriticalStripInterface continuation) →
  (test : ConstructiveCriticalStripZeroTest strip) →
  NamedCriticalStripZero strip (naming test) → CriticalStripZero strip
constructive-test-positive-branch strip test =
  named-critical-strip-zero-gives-zero strip (naming test)

constructive-test-negative-branch-needs-completeness :
  {evaluator : CertifiedRightHalfPlaneDirichletSeries} →
  {continuation : AnalyticContinuationInterface evaluator} →
  (strip : CriticalStripInterface continuation) →
  (test : ConstructiveCriticalStripZeroTest strip) →
  PointCompleteCriticalStripNaming (naming test) →
  NoNamedCriticalStripZero strip (naming test) →
  ¬ MereCriticalStripZero strip
constructive-test-negative-branch-needs-completeness strip test =
  complete-naming-no-named-critical-zero-implies-no-mere-zero
    strip (naming test)
