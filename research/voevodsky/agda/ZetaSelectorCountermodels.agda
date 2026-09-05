{-# OPTIONS --safe --cubical --no-import-sorts --guardedness #-}
module ZetaSelectorCountermodels where

open import Cubical.Foundations.Prelude
open import Cubical.Foundations.HLevels
open import Cubical.Data.Unit
open import Cubical.Data.Empty as Empty
open import Cubical.Data.Sigma
open import Cubical.HITs.PropositionalTruncation as PT
open import Cubical.Relation.Nullary
open import ConstructiveComplexCompletion
open import ZetaConstructibilityContract
open import ZetaZeroNamingContract

zeroZetaProblem : ZetaZeroProblem
zeroZetaProblem .zeta z = zeroComplex
zeroZetaProblem .CriticalStrip z = Unit
zeroZetaProblem .criticalStrip-isProp z = isPropUnit

zero-is-nontrivial-zero : NontrivialZero zeroZetaProblem zeroComplex
zero-is-nontrivial-zero = refl , tt

zero-zeta-certified-zero : CertifiedNontrivialZero zeroZetaProblem
zero-zeta-certified-zero = zeroComplex , zero-is-nontrivial-zero

zero-zeta-mere-zero : MereNontrivialZeroExists zeroZetaProblem
zero-zeta-mere-zero = ∣ zero-zeta-certified-zero ∣₁

zeroZetaSearchFamily : ZeroSearchFamily zeroZetaProblem
zeroZetaSearchFamily .SearchParameter = Unit
zeroZetaSearchFamily .admissible p = Unit
zeroZetaSearchFamily .admissible-isProp p = isPropUnit
zeroZetaSearchFamily .accepts p z = NontrivialZero zeroZetaProblem z
zeroZetaSearchFamily .accepts-isProp p z =
  nontrivialZero-isProp zeroZetaProblem z
zeroZetaSearchFamily .accepted-is-nontrivial-zero p z admissible accepted =
  accepted

zeroZetaTotalSelector : TotalCertifiedSelector zeroZetaSearchFamily
zeroZetaTotalSelector p admissible = zeroComplex , zero-is-nontrivial-zero

emptyCodeSemantics : AlgorithmSemantics zeroZetaSearchFamily
emptyCodeSemantics .Code = Empty.⊥
emptyCodeSemantics .realizes code selector = Empty.⊥
emptyCodeSemantics .realizes-isProp code selector = Empty.isProp⊥

empty-code-has-no-constructible-selector :
  NoConstructibleTotalSelector zeroZetaSearchFamily emptyCodeSemantics
empty-code-has-no-constructible-selector (code , selector , realization) = code

selector-impossibility-can-coexist-with-certified-zero :
  NoConstructibleTotalSelector zeroZetaSearchFamily emptyCodeSemantics ×
  CertifiedNontrivialZero zeroZetaProblem
selector-impossibility-can-coexist-with-certified-zero =
  empty-code-has-no-constructible-selector , zero-zeta-certified-zero

unitCodeSemantics : AlgorithmSemantics zeroZetaSearchFamily
unitCodeSemantics .Code = Unit
unitCodeSemantics .realizes code selector = Unit
unitCodeSemantics .realizes-isProp code selector = isPropUnit

unit-code-constructs-selector :
  ConstructibleTotalSelector zeroZetaSearchFamily unitCodeSemantics
unit-code-constructs-selector = tt , zeroZetaTotalSelector , tt

algorithm-semantics-changes-constructibility :
  NoConstructibleTotalSelector zeroZetaSearchFamily emptyCodeSemantics ×
  ConstructibleTotalSelector zeroZetaSearchFamily unitCodeSemantics
algorithm-semantics-changes-constructibility =
  empty-code-has-no-constructible-selector , unit-code-constructs-selector

emptyComplexNameSystem : ComplexNameSystem
emptyComplexNameSystem .Name = Empty.⊥
emptyComplexNameSystem .denotes name = Empty.rec name

empty-system-has-no-named-zero :
  NoNamedNontrivialZero zeroZetaProblem emptyComplexNameSystem
empty-system-has-no-named-zero (name , certificate) = name

unnamed-system-can-coexist-with-certified-zero :
  NoNamedNontrivialZero zeroZetaProblem emptyComplexNameSystem ×
  CertifiedNontrivialZero zeroZetaProblem
unnamed-system-can-coexist-with-certified-zero =
  empty-system-has-no-named-zero , zero-zeta-certified-zero

identityComplexNameSystem : ComplexNameSystem
identityComplexNameSystem .Name = ComplexCompletion
identityComplexNameSystem .denotes z = z

identity-name-system-is-complete :
  PointCompleteNameSystem identityComplexNameSystem
identity-name-system-is-complete .namesEveryPoint z = z , refl

identity-system-names-zero :
  NamedNontrivialZero zeroZetaProblem identityComplexNameSystem
identity-system-names-zero = zeroComplex , zero-is-nontrivial-zero

name-system-changes-zero-constructibility :
  NoNamedNontrivialZero zeroZetaProblem emptyComplexNameSystem ×
  NamedNontrivialZero zeroZetaProblem identityComplexNameSystem
name-system-changes-zero-constructibility =
  empty-system-has-no-named-zero , identity-system-names-zero
