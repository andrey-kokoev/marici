{-# OPTIONS --safe --cubical --guardedness #-}
module ClosurePushoutTransportCoherence where

open import Cubical.Foundations.Prelude
open import Cubical.Foundations.Equiv
open import Cubical.Foundations.Univalence using (pathToEquiv; pathToEquivRefl)
open import Cubical.Foundations.GroupoidLaws using (rUnit)
open import Cubical.Foundations.Path using (compPath→Square)
import Cubical.HITs.Pushout.Base as PO
open import ClosureFiniteGluingNormalization using (module LiftSpan)
open import ClosureGeneralRotationAdmission using (module IdentitySpan)

-- A path of right-hand pieces AND attachment functions. The left piece
-- and boundary stay fixed. No attachment map is assumed invertible.
module FixedLeft {S A : Type} (f : S → A) where
  Diagram : Type₁
  Diagram = Σ[ C ∈ Type ] (S → C)

  Realize : Diagram → Type
  Realize D = PO.Pushout f (snd D)

  replacement : {D E : Diagram} (p : D ≡ E) → Realize D ≃ Realize E
  replacement {D} {E} p = LiftSpan.equivalence f (snd D) f (snd E)
    (idEquiv S) (idEquiv A) (pathToEquiv (λ i → fst (p i)))
    refl (funExt (λ s → fromPathP (λ i → snd (p i) s)))

  leftWitness : {D E : Diagram} (p : D ≡ E) (a : A) →
    transport (cong Realize p) (PO.inl a) ≡ PO.inl a
  leftWitness p a = fromPathP {A = λ i → Realize (p i)} (λ i → PO.inl a)

  -- Carry the endpoint coherence through path induction together with
  -- the homotopy; do not choose an unrelated homotopy afterwards.
  ComparisonData : {D E : Diagram} (p : D ≡ E) → Type
  ComparisonData {D} p = Σ[
    h ∈ ((x : Realize D) → transport (cong Realize p) x ≡ equivFun (replacement p) x) ]
    ((a : A) → h (PO.inl a) ≡ leftWitness p a)

  module Constant (D : Diagram) where
    module Id = IdentitySpan f (snd D)

    frames : I → Realize D ≃ Realize D
    frames i = LiftSpan.equivalence f (snd D) f (snd D)
      (idEquiv S) (idEquiv A) (pathToEquivRefl {A = fst D} i)
      refl (λ j s → transp (λ _ → fst D) (i ∨ j) (snd D s))

    homotopy : (x : Realize D) →
      transport (cong Realize refl) x ≡ equivFun (replacement (refl {x = D})) x
    homotopy x = transportRefl x ∙ sym (Id.unchanged x)
      ∙ sym (λ i → equivFun (frames i) x)

    onLeft : (a : A) → homotopy (PO.inl a) ≡ leftWitness (refl {x = D}) a
    onLeft a = cong (λ q → transportRefl (PO.inl a) ∙ q) (sym (rUnit refl))
      ∙ sym (rUnit (transportRefl (PO.inl a)))

    comparison : ComparisonData (refl {x = D})
    comparison = homotopy , onLeft

  comparison : {D E : Diagram} (p : D ≡ E) → ComparisonData p
  comparison {D} p = J (λ E q → ComparisonData q) (Constant.comparison D) p

  agreesWithTransport : {D E : Diagram} (p : D ≡ E) (x : Realize D) →
    transport (cong Realize p) x ≡ equivFun (replacement p) x
  agreesWithTransport p = fst (comparison p)

  onLeft : {D E : Diagram} (p : D ≡ E) (a : A) →
    agreesWithTransport p (PO.inl a) ≡ leftWitness p a
  onLeft p = snd (comparison p)

  framePath : {D E : Diagram} (p : D ≡ E) →
    pathToEquiv (cong Realize p) ≡ replacement p
  framePath p = equivEq (funExt (agreesWithTransport p))

  leftWitnessPath : {D E : Diagram} (p : D ≡ E) (a : A) →
    PathP (λ i → equivFun (framePath p i) (PO.inl a) ≡ PO.inl a)
      (leftWitness p a) refl
  leftWitnessPath p a = compPath→Square (cong (λ q → q ∙ refl) (onLeft p a))
