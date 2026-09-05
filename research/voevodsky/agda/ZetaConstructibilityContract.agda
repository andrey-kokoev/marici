{-# OPTIONS --safe --cubical --no-import-sorts --guardedness #-}
module ZetaConstructibilityContract where

open import Cubical.Foundations.Prelude
open import Cubical.Foundations.HLevels
open import Cubical.Data.Sigma
open import Cubical.Relation.Nullary
open import Cubical.HITs.PropositionalTruncation as PT
open import ConstructiveComplexCompletion

record ZetaZeroProblem : Type₁ where
  field
    zeta : ComplexCompletion → ComplexCompletion
    CriticalStrip : ComplexCompletion → Type
    criticalStrip-isProp : (z : ComplexCompletion) → isProp (CriticalStrip z)
open ZetaZeroProblem public

NontrivialZero : (problem : ZetaZeroProblem) → ComplexCompletion → Type
NontrivialZero problem z =
  IsComplexZero (zeta problem z) × CriticalStrip problem z

nontrivialZero-isProp : (problem : ZetaZeroProblem) (z : ComplexCompletion) →
  isProp (NontrivialZero problem z)
nontrivialZero-isProp problem z =
  isProp× (isComplexZero-isProp (zeta problem z))
    (criticalStrip-isProp problem z)

CertifiedNontrivialZero : ZetaZeroProblem → Type
CertifiedNontrivialZero problem =
  Σ[ z ∈ ComplexCompletion ] NontrivialZero problem z

MereNontrivialZeroExists : ZetaZeroProblem → Type
MereNontrivialZeroExists problem = ∥ CertifiedNontrivialZero problem ∥₁

record ZeroSearchFamily (problem : ZetaZeroProblem) : Type₁ where
  field
    SearchParameter : Type
    admissible : SearchParameter → Type
    admissible-isProp : (p : SearchParameter) → isProp (admissible p)
    accepts : SearchParameter → ComplexCompletion → Type
    accepts-isProp : (p : SearchParameter) (z : ComplexCompletion) →
      isProp (accepts p z)
    accepted-is-nontrivial-zero :
      (p : SearchParameter) (z : ComplexCompletion) →
      admissible p → accepts p z → NontrivialZero problem z
open ZeroSearchFamily public

TotalCertifiedSelector :
  {problem : ZetaZeroProblem} → ZeroSearchFamily problem → Type
TotalCertifiedSelector family =
  (p : SearchParameter family) → admissible family p →
  Σ[ z ∈ ComplexCompletion ] accepts family p z

record AlgorithmSemantics
  {problem : ZetaZeroProblem} (family : ZeroSearchFamily problem) : Type₁ where
  field
    Code : Type
    realizes : Code → TotalCertifiedSelector family → Type
    realizes-isProp : (code : Code) (selector : TotalCertifiedSelector family) →
      isProp (realizes code selector)
open AlgorithmSemantics public

ConstructibleTotalSelector :
  {problem : ZetaZeroProblem} (family : ZeroSearchFamily problem) →
  AlgorithmSemantics family → Type
ConstructibleTotalSelector family semantics =
  Σ[ code ∈ Code semantics ]
    Σ[ selector ∈ TotalCertifiedSelector family ]
      realizes semantics code selector

NoConstructibleTotalSelector :
  {problem : ZetaZeroProblem} (family : ZeroSearchFamily problem) →
  AlgorithmSemantics family → Type
NoConstructibleTotalSelector family semantics =
  ¬ ConstructibleTotalSelector family semantics

-- This is intentionally distinct from selector impossibility.  No implication
-- between these types is assumed by the contract.
NoConstructiveExistenceProof : ZetaZeroProblem → Type
NoConstructiveExistenceProof problem = ¬ MereNontrivialZeroExists problem

record InhabitedSearchDomain
  {problem : ZetaZeroProblem} (family : ZeroSearchFamily problem) : Type where
  field
    parameter : SearchParameter family
    parameter-admissible : admissible family parameter
open InhabitedSearchDomain public

selector-produces-certified-zero :
  {problem : ZetaZeroProblem} (family : ZeroSearchFamily problem) →
  InhabitedSearchDomain family → TotalCertifiedSelector family →
  CertifiedNontrivialZero problem
selector-produces-certified-zero family domain selector =
  let selected = selector (parameter domain) (parameter-admissible domain)
      z = fst selected
      accepted = snd selected
  in z , accepted-is-nontrivial-zero family
    (parameter domain) z (parameter-admissible domain) accepted

selector-produces-mere-zero :
  {problem : ZetaZeroProblem} (family : ZeroSearchFamily problem) →
  InhabitedSearchDomain family → TotalCertifiedSelector family →
  MereNontrivialZeroExists problem
selector-produces-mere-zero family domain selector =
  ∣ selector-produces-certified-zero family domain selector ∣₁

constructible-selector-produces-mere-zero :
  {problem : ZetaZeroProblem} (family : ZeroSearchFamily problem) →
  (semantics : AlgorithmSemantics family) → InhabitedSearchDomain family →
  ConstructibleTotalSelector family semantics →
  MereNontrivialZeroExists problem
constructible-selector-produces-mere-zero family semantics domain
  (code , selector , realization) =
  selector-produces-mere-zero family domain selector

no-existence-proof-implies-no-constructible-selector :
  {problem : ZetaZeroProblem} (family : ZeroSearchFamily problem) →
  (semantics : AlgorithmSemantics family) → InhabitedSearchDomain family →
  NoConstructiveExistenceProof problem →
  NoConstructibleTotalSelector family semantics
no-existence-proof-implies-no-constructible-selector
  family semantics domain noExistence constructible =
  noExistence
    (constructible-selector-produces-mere-zero
      family semantics domain constructible)

SemanticsRepresentsSelector :
  {problem : ZetaZeroProblem} {family : ZeroSearchFamily problem} →
  AlgorithmSemantics family → TotalCertifiedSelector family → Type
SemanticsRepresentsSelector semantics selector =
  Σ[ code ∈ Code semantics ] realizes semantics code selector

record ExtensionallyCompleteSemantics
  {problem : ZetaZeroProblem} {family : ZeroSearchFamily problem}
  (semantics : AlgorithmSemantics family) : Type₁ where
  field
    representsEverySelector : (selector : TotalCertifiedSelector family) →
      SemanticsRepresentsSelector semantics selector
open ExtensionallyCompleteSemantics public

complete-semantics-constructs-every-selector :
  {problem : ZetaZeroProblem} {family : ZeroSearchFamily problem} →
  (semantics : AlgorithmSemantics family) →
  ExtensionallyCompleteSemantics semantics →
  (selector : TotalCertifiedSelector family) →
  ConstructibleTotalSelector family semantics
complete-semantics-constructs-every-selector semantics completeness selector =
  let representation = representsEverySelector completeness selector
  in fst representation , selector , snd representation

no-constructible-selector-under-completeness-implies-no-total-selector :
  {problem : ZetaZeroProblem} {family : ZeroSearchFamily problem} →
  (semantics : AlgorithmSemantics family) →
  ExtensionallyCompleteSemantics semantics →
  NoConstructibleTotalSelector family semantics →
  ¬ TotalCertifiedSelector family
no-constructible-selector-under-completeness-implies-no-total-selector
  semantics completeness noConstructible selector =
  noConstructible
    (complete-semantics-constructs-every-selector
      semantics completeness selector)

record UniformlySolvableSearchFamily
  {problem : ZetaZeroProblem} (family : ZeroSearchFamily problem) : Type where
  field
    chooseAccepted : (p : SearchParameter family) → admissible family p →
      Σ[ z ∈ ComplexCompletion ] accepts family p z
open UniformlySolvableSearchFamily public

uniform-solvability-gives-total-selector :
  {problem : ZetaZeroProblem} (family : ZeroSearchFamily problem) →
  UniformlySolvableSearchFamily family → TotalCertifiedSelector family
uniform-solvability-gives-total-selector family solvable =
  chooseAccepted solvable

complete-semantics-no-selector-refutes-uniform-solvability :
  {problem : ZetaZeroProblem} {family : ZeroSearchFamily problem} →
  (semantics : AlgorithmSemantics family) →
  ExtensionallyCompleteSemantics semantics →
  NoConstructibleTotalSelector family semantics →
  ¬ UniformlySolvableSearchFamily family
complete-semantics-no-selector-refutes-uniform-solvability
  semantics completeness noConstructible solvable =
  no-constructible-selector-under-completeness-implies-no-total-selector
    semantics completeness noConstructible
    (uniform-solvability-gives-total-selector _ solvable)
