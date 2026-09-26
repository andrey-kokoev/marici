{-# OPTIONS --safe --cubical --guardedness #-}
module IndexIdentityCoherenceRegression where

open import Cubical.Foundations.Prelude
open import Cubical.Foundations.Equiv
open import Cubical.Foundations.Univalence using (ua; uaβ)
open import Cubical.Data.Unit.Base using (Unit; tt)
open import Cubical.Data.Bool.Base using (Bool; true; false)
open import Cubical.Data.Bool.Properties using (notEquiv; true≢false; false≢true)
open import Cubical.Data.Empty.Base using (⊥)
import WholePackageSigmaPi as Whole
import SigmaPiComparisonDecomposition as Decomposition
import IndexIdentityCoherence as Indexed

open Whole.Universe ℓ-zero
module Dec = Decomposition.Decomposition ℓ-zero
open Indexed.Indexed ℓ-zero

-- A genuine loop and a double cover with nontrivial monodromy.
-- This is a homotopy/index test, not a temporal process.
data Circle : Type₀ where
  base : Circle
  loop : base ≡ base

cover : Circle → Code
cover base = atom Bool
cover (loop t) = atom (ua notEquiv t)

-- The index is itself an E expression, so its comparison is decomposed
-- recursively rather than always handled as an opaque atomic path.
index-code : Code
index-code = E Unit (λ _ → atom Circle)

F : Family
F = family index-code (λ i → cover (snd i))

base-index : Index F
base-index = tt , base

index-loop : base-index ≡ base-index
index-loop t = tt , loop t

c : IndexEvidence F base-index base-index
c = Dec.encode index-code index-loop

flip-true : act F c true ≡ false
flip-true = cong (λ p → subst (Fibre F) p true)
  (Dec.witness-completeness index-code index-loop) ∙ uaβ notEquiv true

flip-false : act F c false ≡ true
flip-false = cong (λ p → subst (Fibre F) p false)
  (Dec.witness-completeness index-code index-loop) ∙ uaβ notEquiv false

loop-is-not-reflexive : index-loop ≡ refl → ⊥
loop-is-not-reflexive p = false≢true
  (sym (uaβ notEquiv true)
    ∙ cong (λ q → subst (Fibre F) q true) p
    ∙ substRefl {B = Fibre F} {x = base-index} true)

-- Identity endpoints do not justify replacing their path with reflexivity.
identity-evidence-is-insufficient :
  act F (identity-index F base-index) true ≡ false → ⊥
identity-evidence-is-insufficient p = true≢false
  (sym (identity-action F base-index true) ∙ p)

sum-evidence : SumEvidence F (base-index , true) (base-index , false)
sum-evidence = c , flip-true

sum-comparison : (base-index , true) ≡ (base-index , false)
sum-comparison = equivFun (sum-equiv F _ _) sum-evidence

sum-witness-retained :
  equivFun (sum-equiv F _ _) (invEq (sum-equiv F _ _) sum-comparison) ≡ sum-comparison
sum-witness-retained = sum-recovery F sum-comparison

-- Composing the loop's action twice restores the Bool value.
twice : act F c (act F c true) ≡ true
twice = cong (act F c) flip-true ∙ flip-false

inverse-restores : act F (inverse-index F c) (act F c true) ≡ true
inverse-restores = inverse-action F c true

no-fixed-value : (b : Bool) → act F c b ≡ b → ⊥
no-fixed-value true p = false≢true (sym flip-true ∙ p)
no-fixed-value false p = true≢false (sym flip-false ∙ p)

-- Pi compatibility has content: this family admits no global section.
no-section : Sections F → ⊥
no-section s = no-fixed-value (s base-index) (section-action F s c)

action-record : ActionCertificate
action-record = action-certificate F base-index base-index c true false flip-true

next-Q : Whole.Universe.Complete (ℓ-suc ℓ-zero)
next-Q = reify-action action-record

index-witness-retained :
  ActionCertificate.index-evidence (Whole.Universe.value next-Q) ≡ c
index-witness-retained = refl

higher-index-record : HigherActionCertificate
higher-index-record = retain-higher-action F (index-cancellation F c)

higher-next-Q : Whole.Universe.Complete (ℓ-suc ℓ-zero)
higher-next-Q = reify-higher-action higher-index-record

higher-index-witness-retained :
  HigherActionCertificate.index-comparison (Whole.Universe.value higher-next-Q)
    ≡ index-cancellation F c
higher-index-witness-retained = refl
