{-# OPTIONS --safe --cubical --guardedness #-}
module NativeBranchBoundaryCoordinatesRegression where

open import Cubical.Foundations.Prelude
open import Cubical.Foundations.Equiv
open import Cubical.Data.Bool.Base using (Bool; true; false)
open import Cubical.Data.Bool.Properties using (false≢true)
open import Cubical.Data.Unit.Base using (Unit; tt)
open import Cubical.Data.Empty.Base using (⊥)
open import Cubical.Data.Nat.Base using (ℕ)
import WholePackageSigmaPi as Whole
import NativeBranchBoundaryCoordinates as Native

-- Exact retention, uniformly in the universe, seed theory, application,
-- whole boundary and requested witness. No closed large proof expansion.
module Symbolic (ℓ : Level) (S : Whole.Universe.Complete ℓ → Type (ℓ-suc ℓ)) where
  module N = Native.Boundaries ℓ S
  module Given (Input : N.High.Code) (evaluate : N.High.El Input → N.Old.Closure S) where
    module A = N.Application Input evaluate

    whole-application-reconstructs : (v : N.High.El A.Output)
      → invEq A.coordinates (equivFun A.coordinates v) ≡ v
    whole-application-reconstructs = retEq A.coordinates

    higher-witness-reconstructs : {v w : N.High.El A.Output} (p q : v ≡ w) (h : p ≡ q)
      → invEq (A.application-higher p q) (equivFun (A.application-higher p q) h) ≡ h
    higher-witness-reconstructs p q = retEq (A.application-higher p q)

    module Request (b : N.High.El Input) (p : A.B.Semantic A.direct A.normalize-first) where
      packet = A.next-requested b p
      contents = Whole.Universe.value packet

      whole-boundary-retained : A.Retained.boundary contents ≡ b
      whole-boundary-retained = refl

      native-output-retained : fst (snd (A.Retained.application contents)) ≡ evaluate b
      native-output-retained = refl

      requested-witness-retained : A.B.Requested.witness (A.Retained.generated-comparison contents) ≡ p
      requested-witness-retained = refl

open Whole.Universe ℓ-zero
Seeds : Complete → Type (ℓ-suc ℓ-zero)
Seeds _ = Lift {j = ℓ-suc ℓ-zero} Bool
module N = Native.Boundaries ℓ-zero Seeds

unit-packet : Complete
unit-packet = pack (atom Unit) tt
family : Bool → Complete
family _ = unit-packet

all-true : (i : Bool) → N.Old.Resolve Seeds (family i)
all-true _ = N.Old.seed (lift true)
changed-unselected : (i : Bool) → N.Old.Resolve Seeds (family i)
changed-unselected false = N.Old.seed (lift false)
changed-unselected true = N.Old.seed (lift true)

false-boundary true-boundary changed-boundary : N.High.El (N.E-fixed Bool)
false-boundary = family , all-true , lift false
true-boundary = family , all-true , lift true
changed-boundary = family , changed-unselected , lift true

choice : N.High.El (N.E-fixed Bool) → Bool
choice b = lower (snd (snd b))

seed-tag : {q : Complete} → N.Old.Resolve Seeds q → Bool
seed-tag (N.Old.seed tag) = lower tag
seed-tag (N.Old.apply r ds) = false

unselected-tag : N.High.El (N.E-fixed Bool) → Bool
unselected-tag b = seed-tag (fst (snd b) false)

faithful : (x y : N.High.El (N.E-fixed Bool))
  → N.N.normalize (N.E-fixed Bool) x ≡ N.N.normalize (N.E-fixed Bool) y → x ≡ y
faithful x y p = sym (retEq e x) ∙ cong (invEq e) p ∙ retEq e y
  where e = N.N.normalize-equiv (N.E-fixed Bool)

choice-not-erased : N.N.normalize (N.E-fixed Bool) false-boundary
  ≡ N.N.normalize (N.E-fixed Bool) true-boundary → ⊥
choice-not-erased p = false≢true (cong choice (faithful false-boundary true-boundary p))

unselected-history-not-erased : N.N.normalize (N.E-fixed Bool) changed-boundary
  ≡ N.N.normalize (N.E-fixed Bool) true-boundary → ⊥
unselected-history-not-erased p = false≢true (cong unselected-tag (faithful changed-boundary true-boundary p))

-- Endpoint packages alone agree, but their unselected RAW CHILD differs.
-- The new boundary coordinates preserve precisely that extra information.
endpoint-packages-agree : fst (N.evaluate-E-fixed Bool changed-boundary)
  ≡ fst (N.evaluate-E-fixed Bool true-boundary)
endpoint-packages-agree = refl

module E = N.Application (N.E-fixed Bool) (N.evaluate-E-fixed Bool)
application-retains-choice : choice (fst (E.enter true-boundary)) ≡ true
application-retains-choice = refl
application-retains-unselected : unselected-tag (fst (E.enter changed-boundary)) ≡ false
application-retains-unselected = refl

closure-tag : N.Old.Closure Seeds → Bool
closure-tag out = seed-tag (snd out)

wrong-output : N.Old.Closure Seeds
wrong-output = unit-packet , N.Old.seed (lift true)

-- A different raw constructor cannot be smuggled into the evaluation graph.
wrong-output-impossible : N.evaluate-E-fixed Bool true-boundary ≡ wrong-output → ⊥
wrong-output-impossible p = false≢true (cong closure-tag p)

guarded-wrong-output-impossible : (f : E.H.CoherentMap E.H.original E.output-presentation)
  → fst (snd (fst (f true-boundary))) ≡ wrong-output → ⊥
guarded-wrong-output-impossible f p = wrong-output-impossible
  (sym (E.guarded-native-output f true-boundary) ∙ p)

-- Keeping input and arbitrary output WITHOUT their evaluation equation
-- does not make projection to the boundary an equivalence.
Uncertified : Type (ℓ-suc ℓ-zero)
Uncertified = Σ[ b ∈ N.High.El (N.E-fixed Bool) ] N.Old.Closure Seeds

forget-output : Uncertified → N.High.El (N.E-fixed Bool)
forget-output = fst

uncertified-projection-not-equivalence : isEquiv forget-output → ⊥
uncertified-projection-not-equivalence proof = false≢true
  (cong (λ v → closure-tag (snd v))
    (sym (retEq e left) ∙ cong (invEq e) refl ∙ retEq e right))
  where
  e : Uncertified ≃ N.High.El (N.E-fixed Bool)
  e = forget-output , proof
  left right : Uncertified
  left = true-boundary , N.evaluate-E-fixed Bool true-boundary
  right = true-boundary , wrong-output

-- Arbitrarily indexed Pi is not reduced to finite enumerations. These are
-- actual native parent histories with empty and infinite child families.
empty-E-uninhabited : N.High.El (N.E-fixed ⊥) → ⊥
empty-E-uninhabited b = lower (snd (snd b))

dependent-family : Bool → Complete
dependent-family false = unit-packet
dependent-family true = pack (atom Bool) true
dependent-input : N.High.El N.Pi-input
dependent-input = Bool , dependent-family , (λ _ → N.Old.seed (lift true))

dependent-false-value : value (fst (N.evaluate-Pi dependent-input)) false ≡ tt
dependent-false-value = refl
dependent-true-value : value (fst (N.evaluate-Pi dependent-input)) true ≡ true
dependent-true-value = refl

empty-input : N.High.El N.Pi-input
empty-input = ⊥ , (λ ()) , (λ ())
infinite-input : N.High.El N.Pi-input
infinite-input = ℕ , (λ _ → unit-packet) , (λ _ → N.Old.seed (lift true))

empty-native : N.Old.Resolve Seeds (Pi-package ⊥ (λ ()))
empty-native = snd (N.evaluate-Pi empty-input)
infinite-native : N.Old.Resolve Seeds (Pi-package ℕ (λ _ → unit-packet))
infinite-native = snd (N.evaluate-Pi infinite-input)

empty-output-retained : fst (snd (N.Pi-application.enter empty-input)) ≡ N.evaluate-Pi empty-input
empty-output-retained = refl
infinite-output-retained : fst (snd (N.Pi-application.enter infinite-input)) ≡ N.evaluate-Pi infinite-input
infinite-output-retained = refl
