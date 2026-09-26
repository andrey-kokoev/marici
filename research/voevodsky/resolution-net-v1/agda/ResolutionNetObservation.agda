{-# OPTIONS --safe --cubical --guardedness #-}
module ResolutionNetObservation where

open import Cubical.Foundations.Prelude
open import Cubical.Foundations.Transport using (substComposite)
open import Cubical.Data.Unit.Base using (Unit; tt)
open import Cubical.Data.Empty.Base using (⊥)
open import Cubical.Data.Bool.Base using (true; false)
open import Cubical.Data.Bool.Properties using (true≢false)
import IndexIdentityCoherence as Indexed
import IndexIdentityCoherenceRegression as Cover
module Ix = Indexed.Indexed ℓ-zero

-- A probe p : O → X specifies access to a structure X with fibres F.
-- O need not embed into X: this includes interfaces with repeated access.
-- No ordering, clock, evaluator, or global section is assumed.
module Observation {ℓ : Level} (X : Type ℓ) (F : X → Type ℓ) where
  Observe : {O : Type ℓ} → (O → X) → Type ℓ
  Observe {O} p = (o : O) → F (p o)

  restrict : {O Q : Type ℓ} {p : O → X}
    (access : Q → O) → Observe p → Observe (λ q → p (access q))
  restrict access s q = s (access q)

  restriction-id : {O : Type ℓ} {p : O → X} (s : Observe p)
    → restrict (λ o → o) s ≡ s
  restriction-id s = refl

  restriction-compose : {O Q R : Type ℓ} {p : O → X}
    (f : Q → O) (g : R → Q) (s : Observe p)
    → restrict g (restrict f s) ≡ restrict (λ r → f (g r)) s
  restriction-compose f g s = refl

  -- Losing access cannot distinguish observations already equal.
  restriction-respects : {O Q : Type ℓ} {p : O → X}
    (f : Q → O) {s t : Observe p} → s ≡ t → restrict f s ≡ restrict f t
  restriction-respects f = cong (restrict f)

  -- A global assignment, IF supplied, restricts to any probe.
  from-global : {O : Type ℓ} (p : O → X) → ((x : X) → F x) → Observe p
  from-global p s o = s (p o)

  -- Witnessed comparisons act on observation without an execution clock.
  compare : {O : Type ℓ} {p q : O → X}
    → ((o : O) → p o ≡ q o) → Observe p → Observe q
  compare h s o = subst F (h o) (s o)

  compare-identity : {O : Type ℓ} {p : O → X} (s : Observe p)
    → compare (λ _ → refl) s ≡ s
  compare-identity s = funExt (λ o → substRefl {B = F} (s o))

  compare-compose : {O : Type ℓ} {p q r : O → X}
    (h : (o : O) → p o ≡ q o) (k : (o : O) → q o ≡ r o)
    (s : Observe p)
    → compare (λ o → h o ∙ k o) s ≡ compare k (compare h s)
  compare-compose h k s = funExt (λ o → substComposite F (h o) (k o) (s o))

  comparison-restricts : {O Q : Type ℓ} {p q : O → X}
    (h : (o : O) → p o ≡ q o) (f : Q → O) (s : Observe p)
    → restrict f (compare h s) ≡ compare (λ q → h (f q)) (restrict f s)
  comparison-restricts h f s = refl

-- Empty support carries no distinguishable observations.
module EmptyObservation (X : Type) (F : X → Type) where
  open Observation X F
  empty-probe : ⊥ → X
  empty-probe ()
  empty-observation : Observe empty-probe
  empty-observation ()
  empty-unique : (s t : Observe empty-probe) → s ≡ t
  empty-unique s t = funExt (λ ())

-- In this experiment positivity means inhabited support, not a measure.
-- Positivity by itself does not supply a coherent fibre inhabitant.
positive-support : Unit
positive-support = tt

positive-but-unsatisfiable : ((o : Unit) → ⊥) → ⊥
positive-but-unsatisfiable s = s tt

-- Actual observations of the double cover exist on a point probe,
-- although no compatible assignment exists over the entire base.
module DoubleCover where
  open Observation (Ix.Index Cover.F) (Ix.Fibre Cover.F)

  point : Unit → Ix.Index Cover.F
  point _ = Cover.base-index

  see-true see-false : Observe point
  see-true _ = true
  see-false _ = false

  distinguishable : see-true ≡ see-false → ⊥
  distinguishable e = true≢false (cong (λ s → s tt) e)

  -- Same support and same endpoint map; a different comparison witness
  -- acts nontrivially. This is not asserted to be a temporal transition.
  witnessed-loop : compare (λ _ → Cover.index-loop) see-true ≡ see-false
  witnessed-loop = funExt (λ _ → direct-flip)
    where
    open import Cubical.Foundations.Univalence using (uaβ)
    open import Cubical.Data.Bool.Properties using (notEquiv)
    direct-flip = uaβ notEquiv true

  no-global-observation : Observe (λ x → x) → ⊥
  no-global-observation = Cover.no-section
