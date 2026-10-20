{-# OPTIONS --safe --cubical --guardedness #-}
module NonsetWitnessEnvelopes where

open import Cubical.Foundations.Prelude
open import Cubical.Foundations.Equiv
open import Cubical.Foundations.Isomorphism using (isoToEquiv)
open import Cubical.Data.Unit using (Unit; tt)
open import Cubical.Data.Sigma.Properties using (ΣPath≃PathΣ)
open import Cubical.Data.Bool.Base using (true; false)
open import Cubical.Relation.Nullary.Base using (¬_)
import Cubical.HITs.S1.Base as Circle
import WholePackageSigmaPi as Whole
import WholePackageResolution as Resolution
import HigherWitnessAdmission as Admission
import CoherentDependentExtensions as General
import SourceCircleProvenanceAudit as Prior
import ClosureGluingTreeRegression as Regression
open import NativeExtensionFamilyAudit using (Seeds; A)
open import InternalSourceComparisons using (loopEquiv; loop-refl)
open Whole.Universe ℓ-zero
open Resolution.Generators ℓ-zero

-- No h-level hypothesis on F, the native carriers, their loops, or Resolve.
-- Higher paths are inputs: faithful admission is not discovery of coherence.
module Envelope (F : Type) (q : F → Complete) (d : (f : F) → Resolve Seeds (q f)) where
  branch : F → Complete
  branch f = path-package (expression (q f)) (value (q f)) (value (q f)) refl
  branch-native : (f : F) → Resolve Seeds (branch f)
  branch-native f = apply (reflexivity-rule (expression (q f)) (value (q f))) (λ _ → d f)
  CodeE : Code
  CodeE = E F (λ f → retained (branch f))
  encoded : F → Complete
  encoded f = E-package F branch f
  native : (f : F) → Resolve Seeds (encoded f)
  native f = apply (E-rule F branch f) (λ { (lift g) → branch-native g })
  section : F → El CodeE
  section f = f , refl
  liftPath : {f g : F} → f ≡ g → section f ≡ section g
  liftPath = cong section
  path-recovery : {f g : F} (p : f ≡ g) → cong fst (liftPath p) ≡ p
  path-recovery p = refl
  module Admit = Admission.PathAdmission Seeds
  path-native : {f g : F} (p : f ≡ g)
    → Resolve Seeds (path-package CodeE (section f) (section g) (liftPath p))
  path-native {f} p = Admit.from-derived-point CodeE (section f) (native f) (liftPath p)
  liftHigher : {f g : F} {p r : f ≡ g} → p ≡ r → liftPath p ≡ liftPath r
  liftHigher = cong liftPath
  higher-recovery : {f g : F} {p r : f ≡ g} (α : p ≡ r)
    → cong (cong fst) (liftHigher α) ≡ α
  higher-recovery α = refl
  higher-native : {f g : F} {p r : f ≡ g} (α : p ≡ r)
    → Resolve Seeds (higher-package CodeE (section f) (section g) (liftPath p) (liftPath r) (liftHigher α))
  higher-native {p = p} {r} α = apply
    (higher-rule CodeE _ _ (liftPath p) (liftPath r) (liftHigher α))
    (λ { (lift true) → path-native p ; (lift false) → path-native r })

  -- Arbitrary envelope values require BOTH a base path and a dependent
  -- fiber path. Port/index equality alone is not an admission boundary.
  Boundary : (u v : El CodeE) → Type
  Boundary u v = Σ[ p ∈ (fst u ≡ fst v) ]
    PathP (λ i → El (retained (branch (p i)))) (snd u) (snd v)
  boundaryEquiv : (u v : El CodeE) → Boundary u v ≃ (u ≡ v)
  boundaryEquiv u v = ΣPath≃PathΣ
  boundary-recovered : (u v : El CodeE) (b : Boundary u v)
    → invEq (boundaryEquiv u v) (equivFun (boundaryEquiv u v) b) ≡ b
  boundary-recovered u v = retEq (boundaryEquiv u v)
  boundary-native : (u v : El CodeE) → Resolve Seeds (pack CodeE u)
    → (b : Boundary u v)
    → Resolve Seeds (path-package CodeE u v (equivFun (boundaryEquiv u v) b))
  boundary-native u v du b = Admit.from-derived-point CodeE u du (equivFun (boundaryEquiv u v) b)

  module Projection = General.Projection F (λ f → El (retained (branch f)))
  projection-if : ((f : F) → isContr (El (retained (branch f)))) → El CodeE ≃ F
  projection-if c = isoToEquiv (Projection.contractible-projection c)
  projection-only-if : isEquiv (λ (z : El CodeE) → fst z)
    → (f : F) → isContr (El (retained (branch f)))
  projection-only-if = Projection.projection-isEquiv-forces-contractible

-- Reuse the actual prior native pushout/circle envelope under original Seeds.
-- Its span/policy was explicitly supplied in that packet, not selected here.
qCircle = Prior.NativeCircle.encoded A
dCircle = Prior.NativeCircle.derived A
X = El (expression qCircle)
x : X
x = value qCircle
toCircle : X ≃ Circle.S¹
toCircle = compEquiv (Prior.NativeCircle.projection A) Regression.circleEquiv
loops : (x ≡ x) ≃ (Circle.base ≡ Circle.base)
loops = loopEquiv toCircle refl
nontrivial : x ≡ x
nontrivial = invEq loops Circle.loop
nontrivial-not-refl : ¬ (nontrivial ≡ refl)
nontrivial-not-refl p = Regression.circleLoopNotRefl
  (sym (secEq loops Circle.loop) ∙ cong (equivFun loops) p ∙ loop-refl toCircle {x = x} {y = Circle.base} refl)
carrier-not-set : ¬ isSet X
carrier-not-set setX = nontrivial-not-refl (setX x x nontrivial refl)
loops-not-contractible : ¬ isContr (x ≡ x)
loops-not-contractible c = nontrivial-not-refl (isContr→isProp c nontrivial refl)
module Admit = Admission.PathAdmission Seeds
nontrivial-loop-native : Resolve Seeds (path-package (expression qCircle) x x nontrivial)
nontrivial-loop-native = Admit.from-derived-point (expression qCircle) x dCircle nontrivial

module Test = Envelope Unit (λ _ → qCircle) (λ _ → dCircle)
projection-not-equivalence : ¬ isEquiv (λ (z : El Test.CodeE) → fst z)
projection-not-equivalence e = loops-not-contractible (Test.projection-only-if e tt)
left right : El Test.CodeE
left = tt , refl
right = tt , nontrivial
distinct-over-same-index : ¬ (left ≡ right)
distinct-over-same-index p = nontrivial-not-refl (sym (cong snd p))
same-index : fst left ≡ fst right
same-index = refl
