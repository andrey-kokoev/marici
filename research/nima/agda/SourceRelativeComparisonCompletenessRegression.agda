{-# OPTIONS --safe --cubical --guardedness #-}
module SourceRelativeComparisonCompletenessRegression where

open import Cubical.Foundations.Prelude
open import Cubical.Foundations.Equiv
open import Cubical.Data.Sigma.Base using (_×_)
open import Cubical.Data.Unit.Base using (Unit; tt)
open import Cubical.Data.Bool.Base using (Bool; true; false)
open import Cubical.Data.Bool.Properties using (notEquiv; true≢false)
open import Cubical.Data.Empty.Base using (⊥)
import WholePackageSigmaPi as Whole
import SigmaPiComparisonDecomposition as Decomposition
import SourceRelativeComparisonCompleteness as Relative
import IndexIdentityCoherenceRegression as Loop

open Whole.Universe ℓ-zero
module D = Decomposition.Decomposition ℓ-zero

-- Redundant source derivations: tags are retained, even when their decoded
-- paths agree. Completeness must not assume injectivity of this decoder.
Duplicate : (A : Type₀) → A → A → Type₀
Duplicate A x y = (x ≡ y) × Bool

decode-duplicate : (A : Type₀) (x y : A) → Duplicate A x y → x ≡ y
decode-duplicate A x y = fst

module Dup = Relative.Relative ℓ-zero Duplicate decode-duplicate

source-complete : Dup.SourceComplete
source-complete A x y p = (p , true) , refl

all-codes-complete : Dup.StructuralComplete
all-codes-complete = Dup.source-to-structural source-complete

c-true c-false : Dup.Supported (atom Unit) tt tt
c-true = refl , ((refl , true) , refl)
c-false = refl , ((refl , false) , refl)

same-witness : Dup.sound (atom Unit) c-true ≡ Dup.sound (atom Unit) c-false
same-witness = refl

source-derivations-stay-distinct : c-true ≡ c-false → ⊥
source-derivations-stay-distinct p = true≢false (cong (λ c → snd (fst (snd c))) p)

-- The two formerly opaque code constructors now really decompose.
BoolCode : Code
BoolCode = atom Bool

identity-not-swap : D.Evidence (equivalences BoolCode BoolCode) (idEquiv Bool) notEquiv → ⊥
identity-not-swap pointwise-paths = true≢false (pointwise-paths true)

CircleCode : Code
CircleCode = atom Loop.Circle

graph-code : Code
graph-code = comparison CircleCode CircleCode (idEquiv Loop.Circle)

graph-point : El graph-code
graph-point = Loop.base , Loop.base , refl

graph-evidence : D.Evidence graph-code graph-point graph-point
graph-evidence = Loop.loop

graph-path : graph-point ≡ graph-point
graph-path = D.decode graph-code graph-evidence

graph-evidence-retained : D.encode graph-code graph-path ≡ graph-evidence
graph-evidence-retained = D.evidence-recovery graph-code
  {x = graph-point} {y = graph-point} graph-evidence

-- This fixed graph needs only the source theory for Circle, not an
-- assumption that the source theory is complete for every small type.
graph-local-completeness : (p : graph-point ≡ graph-point)
  → Σ[ c ∈ Dup.Supported graph-code graph-point graph-point ] (Dup.sound graph-code c ≡ p)
graph-local-completeness = Dup.local-completeness graph-code
  (source-complete Loop.Circle) graph-point graph-point

graph-certificate : Dup.Certificate
graph-certificate = Dup.certify source-complete graph-code graph-path

next-Q : Whole.Universe.Complete (ℓ-suc ℓ-zero)
next-Q = Dup.reify-certificate graph-certificate

-- A source theory restricted to sets cannot cover the declared circle.
SetSource : (A : Type₀) → A → A → Type₀
SetSource A x y = isSet A × (x ≡ y)

decode-set-source : (A : Type₀) (x y : A) → SetSource A x y → x ≡ y
decode-set-source A x y = snd

module Sets = Relative.Relative ℓ-zero SetSource decode-set-source

circle-is-not-a-set : isSet Loop.Circle → ⊥
circle-is-not-a-set h = Loop.loop-is-not-reflexive
  (cong (λ p t → tt , p t) (sym (h Loop.base Loop.base refl Loop.loop)))

set-source-incomplete : Sets.SourceComplete → ⊥
set-source-incomplete complete = circle-is-not-a-set
  (fst (fst (complete Loop.Circle Loop.base Loop.base Loop.loop)))

E-Pi-cannot-repair-set-only-source : Sets.StructuralComplete → ⊥
E-Pi-cannot-repair-set-only-source complete = set-source-incomplete (Sets.structural-to-source complete)
