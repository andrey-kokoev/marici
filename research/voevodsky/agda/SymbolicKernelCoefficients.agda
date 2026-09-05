{-# OPTIONS --safe --cubical --no-import-sorts --guardedness #-}
module SymbolicKernelCoefficients where

open import Cubical.Foundations.Prelude
open import Cubical.HITs.FreeAbGroup
open import Cubical.Algebra.AbGroup
open import Cubical.Algebra.AbGroup.Instances.FreeAbGroup
open import GenericPastingComplex

private variable ℓ : Level

module SymbolicKernel (Parameter : Type ℓ) where
  data KernelAtom : Type ℓ where
    positive-frequency : Parameter → KernelAtom
    negative-frequency : Parameter → KernelAtom
    tail-discrepancy : Parameter → KernelAtom
    normalization-residue : Parameter → KernelAtom
    deformation-residue : Parameter → KernelAtom

  KernelCoefficientGroup : AbGroup ℓ
  KernelCoefficientGroup = FAGAbGroup {A = KernelAtom}
  open AbGroupStr (snd KernelCoefficientGroup)

  atom : KernelAtom → KernelCoefficientGroup .fst
  atom k = ⟦ k ⟧

  tail : Parameter → KernelCoefficientGroup .fst
  tail τ = atom (tail-discrepancy τ)

  module Exact = Triangle KernelCoefficientGroup

  omega : Parameter → Exact.M³
  omega τ = Exact.triple (KernelCoefficientGroup .snd .AbGroupStr.0g)
                         (tail τ)
                         (KernelCoefficientGroup .snd .AbGroupStr.0g)

  omega-boundary : (τ : Parameter) → Exact.∂₂ (omega τ) ≡ tail τ
  omega-boundary τ = cong (_+ 0g) (+IdL (tail τ)) ∙ +IdR (tail τ)

  filler-exists :
    (D : KernelCoefficientGroup .fst) →
    Σ[ f ∈ Exact.M³ ] Exact.∂₂ f ≡ D
  filler-exists D = Exact.∂₂-preimage D , Exact.∂₂-surjective D

  filler-difference-is-adjustment :
    (v : Exact.M³) →
    Exact.∂₂ v ≡ KernelCoefficientGroup .snd .AbGroupStr.0g →
    Σ[ u ∈ Exact.M³ ] Exact.∂₁ u ≡ v
  filler-difference-is-adjustment = Exact.middle-exact
