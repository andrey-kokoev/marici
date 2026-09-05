{-# OPTIONS --safe --cubical --no-import-sorts --guardedness #-}
module FiniteZetaNoSelector where

open import Cubical.Foundations.Prelude
open import Cubical.Foundations.HLevels
open import Cubical.Data.Nat as ℕ using (ℕ)
open import Cubical.Data.Unit
open import Cubical.Data.Empty
open import Cubical.Data.Sigma
open import Cubical.HITs.PropositionalTruncation as PT
open import Cubical.Relation.Nullary
open import RegularCauchyStructure
open import ConstructiveComplexCompletion
open import ComplexCauchyApproximation
open import ZetaConstructibilityContract
open import RationalDirichletZeta
open import FiniteZetaExactExclusion

finiteZetaCompletionValue : ℕ → ℕ → ComplexCompletion
finiteZetaCompletionValue exponent cutoff =
  complexRegularClass
    (finiteZetaRegularMap exponent cutoff
      (embedRationalComplexRegular zeroRationalComplex))

finiteZetaProblem : ℕ → ℕ → ZetaZeroProblem
finiteZetaProblem exponent cutoff .zeta z =
  finiteZetaCompletionValue exponent cutoff
finiteZetaProblem exponent cutoff .CriticalStrip z = Unit
finiteZetaProblem exponent cutoff .criticalStrip-isProp z = isPropUnit

finite-zeta-problem-has-no-zero : (exponent cutoff : ℕ) →
  (z : ComplexCompletion) →
  ¬ NontrivialZero (finiteZetaProblem exponent cutoff) z
finite-zeta-problem-has-no-zero exponent cutoff z (zeroPath , strip) =
  finite-zeta-completion-value-nonzero exponent cutoff zeroPath

finite-zeta-problem-has-no-certified-zero : (exponent cutoff : ℕ) →
  ¬ CertifiedNontrivialZero (finiteZetaProblem exponent cutoff)
finite-zeta-problem-has-no-certified-zero exponent cutoff (z , certificate) =
  finite-zeta-problem-has-no-zero exponent cutoff z certificate

finite-zeta-problem-has-no-mere-zero : (exponent cutoff : ℕ) →
  NoConstructiveExistenceProof (finiteZetaProblem exponent cutoff)
finite-zeta-problem-has-no-mere-zero exponent cutoff =
  PT.rec isProp⊥ (finite-zeta-problem-has-no-certified-zero exponent cutoff)

finiteZetaSearchFamily : (exponent cutoff : ℕ) →
  ZeroSearchFamily (finiteZetaProblem exponent cutoff)
finiteZetaSearchFamily exponent cutoff .SearchParameter = Unit
finiteZetaSearchFamily exponent cutoff .admissible p = Unit
finiteZetaSearchFamily exponent cutoff .admissible-isProp p = isPropUnit
finiteZetaSearchFamily exponent cutoff .accepts p z =
  NontrivialZero (finiteZetaProblem exponent cutoff) z
finiteZetaSearchFamily exponent cutoff .accepts-isProp p z =
  nontrivialZero-isProp (finiteZetaProblem exponent cutoff) z
finiteZetaSearchFamily exponent cutoff .accepted-is-nontrivial-zero
  p z admissible accepted = accepted

finiteZetaSearchDomain : (exponent cutoff : ℕ) →
  InhabitedSearchDomain (finiteZetaSearchFamily exponent cutoff)
finiteZetaSearchDomain exponent cutoff .parameter = tt
finiteZetaSearchDomain exponent cutoff .parameter-admissible = tt

finite-zeta-no-total-selector : (exponent cutoff : ℕ) →
  ¬ TotalCertifiedSelector (finiteZetaSearchFamily exponent cutoff)
finite-zeta-no-total-selector exponent cutoff selector =
  finite-zeta-problem-has-no-certified-zero exponent cutoff
    (selector-produces-certified-zero
      (finiteZetaSearchFamily exponent cutoff)
      (finiteZetaSearchDomain exponent cutoff) selector)

finite-zeta-no-constructible-selector : (exponent cutoff : ℕ) →
  (semantics : AlgorithmSemantics (finiteZetaSearchFamily exponent cutoff)) →
  NoConstructibleTotalSelector
    (finiteZetaSearchFamily exponent cutoff) semantics
finite-zeta-no-constructible-selector exponent cutoff semantics =
  no-existence-proof-implies-no-constructible-selector
    (finiteZetaSearchFamily exponent cutoff) semantics
    (finiteZetaSearchDomain exponent cutoff)
    (finite-zeta-problem-has-no-mere-zero exponent cutoff)
