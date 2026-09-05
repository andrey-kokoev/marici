{-# OPTIONS --safe --cubical --no-import-sorts --guardedness #-}
module ZetaZeroNamingContract where

open import Cubical.Foundations.Prelude
open import Cubical.Data.Sigma
open import Cubical.Data.Empty
open import Cubical.HITs.PropositionalTruncation as PT
open import Cubical.Relation.Nullary
open import ConstructiveComplexCompletion
open import ZetaConstructibilityContract

record ComplexNameSystem : Type₁ where
  field
    Name : Type
    denotes : Name → ComplexCompletion
open ComplexNameSystem public

NamesPoint : ComplexNameSystem → ComplexCompletion → Type
NamesPoint naming z = Σ[ name ∈ Name naming ] denotes naming name ≡ z

NamedNontrivialZero : ZetaZeroProblem → ComplexNameSystem → Type
NamedNontrivialZero problem naming =
  Σ[ name ∈ Name naming ] NontrivialZero problem (denotes naming name)

NoNamedNontrivialZero : ZetaZeroProblem → ComplexNameSystem → Type
NoNamedNontrivialZero problem naming =
  ¬ NamedNontrivialZero problem naming

named-zero-gives-certified-zero :
  (problem : ZetaZeroProblem) (naming : ComplexNameSystem) →
  NamedNontrivialZero problem naming → CertifiedNontrivialZero problem
named-zero-gives-certified-zero problem naming (name , certificate) =
  denotes naming name , certificate

named-zero-gives-mere-zero :
  (problem : ZetaZeroProblem) (naming : ComplexNameSystem) →
  NamedNontrivialZero problem naming → MereNontrivialZeroExists problem
named-zero-gives-mere-zero problem naming named =
  ∣ named-zero-gives-certified-zero problem naming named ∣₁

record PointCompleteNameSystem (naming : ComplexNameSystem) : Type₁ where
  field
    namesEveryPoint : (z : ComplexCompletion) → NamesPoint naming z
open PointCompleteNameSystem public

complete-naming-lifts-certified-zero :
  (problem : ZetaZeroProblem) (naming : ComplexNameSystem) →
  PointCompleteNameSystem naming → CertifiedNontrivialZero problem →
  NamedNontrivialZero problem naming
complete-naming-lifts-certified-zero problem naming completeness
  (z , zeroCertificate) =
  let named = namesEveryPoint completeness z
      name = fst named
      namePath = snd named
  in name , subst (NontrivialZero problem) (sym namePath) zeroCertificate

complete-naming-no-named-zero-implies-no-certified-zero :
  (problem : ZetaZeroProblem) (naming : ComplexNameSystem) →
  PointCompleteNameSystem naming → NoNamedNontrivialZero problem naming →
  ¬ CertifiedNontrivialZero problem
complete-naming-no-named-zero-implies-no-certified-zero
  problem naming completeness noNamed certified =
  noNamed (complete-naming-lifts-certified-zero
    problem naming completeness certified)

complete-naming-no-named-zero-implies-no-mere-zero :
  (problem : ZetaZeroProblem) (naming : ComplexNameSystem) →
  PointCompleteNameSystem naming → NoNamedNontrivialZero problem naming →
  NoConstructiveExistenceProof problem
complete-naming-no-named-zero-implies-no-mere-zero
  problem naming completeness noNamed =
  PT.rec isProp⊥
    (complete-naming-no-named-zero-implies-no-certified-zero
      problem naming completeness noNamed)

record NameSystemEmbedding
  (source target : ComplexNameSystem) : Type₁ where
  field
    translateName : Name source → Name target
    preservesDenotation : (name : Name source) →
      denotes target (translateName name) ≡ denotes source name
open NameSystemEmbedding public

named-zero-transports :
  (problem : ZetaZeroProblem) {source target : ComplexNameSystem} →
  NameSystemEmbedding source target →
  NamedNontrivialZero problem source → NamedNontrivialZero problem target
named-zero-transports problem embedding (name , certificate) =
  translateName embedding name ,
  subst (NontrivialZero problem)
    (sym (preservesDenotation embedding name)) certificate

no-named-zero-reflects-along-embedding :
  (problem : ZetaZeroProblem) {source target : ComplexNameSystem} →
  NameSystemEmbedding source target → NoNamedNontrivialZero problem target →
  NoNamedNontrivialZero problem source
no-named-zero-reflects-along-embedding problem embedding noTarget sourceZero =
  noTarget (named-zero-transports problem embedding sourceZero)
