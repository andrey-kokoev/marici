{-# OPTIONS --safe --cubical --guardedness #-}
module NewtonFromPoisson where

open import Cubical.Foundations.Prelude
open import Cubical.Foundations.Equiv using (idEquiv)
open import Cubical.Data.Bool.Base using (Bool; true; false)
open import Cubical.Algebra.CommRing.Base
import WholePackageSigmaPi as Whole
import WholePackageResolution as RRC

-- CONDITIONAL algebra/calculus interface, NOT an implementation of real
-- distributions, the divergence theorem or Poisson uniqueness.
module Radial (R : CommRing ℓ-zero) where
  A = fst R
  open CommRingStr (snd R)

  -- This elementary cancellation is proved, not a physical assumption.
  solve-flux : (area invArea slope charge : A)
    → invArea · area ≡ 1r → area · slope ≡ charge
    → slope ≡ invArea · charge
  solve-flux area invArea slope charge inverse flux =
    sym (·IdL slope)
    ∙ cong (λ w → w · slope) (sym inverse)
    ∙ sym (·Assoc invArea area slope)
    ∙ cong (λ w → invArea · w) flux

  record Exterior : Type₁ where
    field
      Radius : Type
      radius reciprocal inverseArea : Radius → A
      inverse-radius : (s : Radius) → reciprocal s · radius s ≡ 1r
      inverse-area : (s : Radius)
        → inverseArea s · (radius s · radius s) ≡ 1r
  open Exterior

  module CalculusInterface (E : Exterior) where
    Function = Radius E → A
    candidate : A → Function
    candidate k s = (- k) · reciprocal E s

    -- All these are explicit mathematical obligations on a REAL model.
    -- No particular real-analysis instance is supplied by this module.
    record Calculus : Type₁ where
      field
        regular : Function → Type
        derivative : (f : Function) → regular f → Function
        decays : Function → Type
        primitive-regular : (k : A) → regular (candidate k)
        primitive-derivative : (k : A)
          → derivative (candidate k) (primitive-regular k)
          ≡ (λ s → inverseArea E s · k)
        primitive-decays : (k : A) → decays (candidate k)
        decay-uniqueness : (f g : Function) (rf : regular f) (rg : regular g)
          → decays f → decays g
          → derivative f rf ≡ derivative g rg → f ≡ g
    open Calculus

    record BoundaryData (C : Calculus) : Type where
      field
        charge : A
        phi : Function
        regularity : regular C phi
        boundary : decays C phi
        -- Normalized spherical Gauss law from Poisson + point source:
        -- r^2 Phi'(r) = GM. This is an INPUT here, not a checked PDE theorem.
        gauss : (s : Radius E)
          → (radius E s · radius E s) · derivative C phi regularity s ≡ charge
    open BoundaryData

    module Derive (C : Calculus) (p : BoundaryData C) where
      inverse-square : (s : Radius E)
        → derivative C (phi p) (regularity p) s ≡ inverseArea E s · charge p
      inverse-square s = solve-flux
        (radius E s · radius E s) (inverseArea E s)
        (derivative C (phi p) (regularity p) s) (charge p) (inverse-area E s) (gauss p s)

      potential-derived : phi p ≡ candidate (charge p)
      potential-derived = decay-uniqueness C (phi p) (candidate (charge p))
        (regularity p) (primitive-regular C (charge p))
        (boundary p) (primitive-decays C (charge p))
        (funExt inverse-square ∙ sym (primitive-derivative C (charge p)))

      acceleration-derived : (s : Radius E)
        → (- derivative C (phi p) (regularity p) s) ≡ (- (inverseArea E s · charge p))
      acceleration-derived s = cong (λ v → - v) (inverse-square s)

      -- Retain the conditional boundary data and the derived comparison in
      -- the existing RRC. This is parameterized, not an instantiated real PDE.
      open Whole.Universe ℓ-zero
      open RRC.Generators ℓ-zero
      sourcePackage candidatePackage : Complete
      sourcePackage = pack (retain (atom (BoundaryData C)) p (atom Function)) (phi p)
      candidatePackage = pack (atom Function) (candidate (charge p))
      data Seeds : Complete → Type₁ where
        boundary-seed : Seeds sourcePackage
        candidate-seed : Seeds candidatePackage
      comparisonRule : Rule
      comparisonRule = compare-rule sourcePackage candidatePackage
        (idEquiv Function) potential-derived
      history : Resolve Seeds (output comparisonRule)
      history = apply comparisonRule
        λ { (lift true) → seed boundary-seed ; (lift false) → seed candidate-seed }
      retainedHistory : Whole.Universe.Complete (ℓ-suc ℓ-zero)
      retainedHistory = reify-history history
      retains-history : snd (Whole.Universe.value retainedHistory) ≡ history
      retains-history = refl
