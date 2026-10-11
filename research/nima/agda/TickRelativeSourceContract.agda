{-# OPTIONS --safe --cubical --guardedness #-}
module TickRelativeSourceContract where

open import Cubical.Foundations.Prelude
open import Cubical.Data.Bool.Base using (Bool)
open import Cubical.Data.Sigma.Base using (_×_)
open import Cubical.Algebra.Ring.Base
import TickPolynomialRealization as P

-- Algebraic provenance only. Analytic laws for half, angularScale and phase
-- are separate obligations; this module does not assert their existence.
module Relative (K : Ring ℓ-zero) (half angularScale : fst K)
  (Time : Type) (phase : Time → fst K) where
  open RingStr (snd K)
  module V = P.Polynomial K
  Label = Bool × Bool
  Vector = V.Vector

  projector : (Vector → Vector) → Vector → Vector
  projector flip v q = half · (v q + (- flip v q))

  generator : (Vector → Vector) → Vector → Vector
  generator flip v q = angularScale · projector flip v q

  spectral-leg : (Vector → Vector) → Time → Vector → Vector
  spectral-leg flip t v q = v q + ((phase t + (- 1r)) · projector flip v q)

  -- The candidate must agree with the declared construction, not merely
  -- satisfy endpoints/coherence. Extra analytic premises are shared globally.
  record DerivedComponents : Type where
    field
      encode : Label → Vector
      left right : Vector → Vector
      left-generator right-generator : Vector → Vector
      left-leg right-leg : Time → Vector → Vector
      encode-derived : encode ≡ V.basis
      left-derived : left ≡ V.L
      right-derived : right ≡ V.R
      left-generator-derived : left-generator ≡ generator V.L
      right-generator-derived : right-generator ≡ generator V.R
      left-leg-derived : left-leg ≡ spectral-leg V.L
      right-leg-derived : right-leg ≡ spectral-leg V.R

  canonical : DerivedComponents
  DerivedComponents.encode canonical = V.basis
  DerivedComponents.left canonical = V.L
  DerivedComponents.right canonical = V.R
  DerivedComponents.left-generator canonical = generator V.L
  DerivedComponents.right-generator canonical = generator V.R
  DerivedComponents.left-leg canonical = spectral-leg V.L
  DerivedComponents.right-leg canonical = spectral-leg V.R
  DerivedComponents.encode-derived canonical = refl
  DerivedComponents.left-derived canonical = refl
  DerivedComponents.right-derived canonical = refl
  DerivedComponents.left-generator-derived canonical = refl
  DerivedComponents.right-generator-derived canonical = refl
  DerivedComponents.left-leg-derived canonical = refl
  DerivedComponents.right-leg-derived canonical = refl

  -- Extensional rigidity WITH THE SAME declared analytic profile; this is
  -- not uniqueness across profiles or proof that Tick selects that profile.
  legs-agree : (a b : DerivedComponents)
    → DerivedComponents.left-leg a ≡ DerivedComponents.left-leg b
  legs-agree a b = DerivedComponents.left-leg-derived a
    ∙ sym (DerivedComponents.left-leg-derived b)
