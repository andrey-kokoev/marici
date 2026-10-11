{-# OPTIONS --safe --cubical --guardedness #-}
module TickMachinCayleyInputs where

open import Cubical.Foundations.Prelude
open import Cubical.Data.Nat using (ℕ)
open import Cubical.Data.Rationals as Q
import Cubical.HITs.SetQuotients as SQ
open import RationalAnalyticSubstrate using (one-half)
open import RegularCauchyStructure using (regularCauchy-ext)
open import CauchyMetricEquivalence
open import CauchyProductBounds
open import CauchyAdditionCongruence using (_+completion_)
open import TaylorTermBounds using (reciprocal-after-zero-magnitude≤half)
open import TickSmallArctangent using (smallAtanRegular)
open import TickAtanCompletionFirstOrder using (atanCompletion; atan-completion-class)
open import TickMachinPiCandidate using (atanFifth; atan239th; oneFifth; one239th; atanFifthRegular; atan239thRegular; atan-fifth-samples; atan-239th-samples)
open import TickCayleyGridIncrement using (gridValue)
open import TickCayleyOuterRotor using (cayleyRotor)
open import TickRotationDefectTransport using (Rotor)
open import TickOperationalRotorIncrement using (rotation)
open import TickOperationalCayleyIdentity using (operational-cayley-grid)

fifth-small : MagnitudeBound (gridValue 1 4) one-half
fifth-small = reciprocal-after-zero-magnitude≤half 3
small239 : MagnitudeBound (gridValue 1 238) one-half
small239 = reciprocal-after-zero-magnitude≤half 237

abstract
  gridCayley : ℕ → ℕ → Rotor
  gridCayley = cayleyRotor

  grid-cayley-definition : (n d : ℕ) → gridCayley n d ≡ cayleyRotor n d
  grid-cayley-definition n d = refl

  fifth-completion-agreement : atanCompletion (gridValue 1 4) fifth-small ≡ atanFifth
  fifth-completion-agreement = atan-completion-class oneFifth fifth-small
    ∙ cong SQ.[_] (regularCauchy-ext (smallAtanRegular oneFifth fifth-small) atanFifthRegular
      (funExt λ n → sym (atan-fifth-samples n)))

  completion239-agreement : atanCompletion (gridValue 1 238) small239 ≡ atan239th
  completion239-agreement = atan-completion-class one239th small239
    ∙ cong SQ.[_] (regularCauchy-ext (smallAtanRegular one239th small239) atan239thRegular
      (funExt λ n → sym (atan-239th-samples n)))

  cayley-at-presentation : (n d : ℕ) (h : MagnitudeBound (gridValue n d) one-half)
    (a : MetricCompletionCandidate) → atanCompletion (gridValue n d) h ≡ a →
    rotation (a +completion a) ≡ gridCayley n d
  cayley-at-presentation n d h a p = cong rotation (sym (cong₂ _+completion_ p p)) ∙ operational-cayley-grid n d h

machin-fifth-cayley : rotation (atanFifth +completion atanFifth) ≡ gridCayley 1 4
machin-fifth-cayley = cayley-at-presentation 1 4 fifth-small atanFifth fifth-completion-agreement

machin239-cayley : rotation (atan239th +completion atan239th) ≡ gridCayley 1 238
machin239-cayley = cayley-at-presentation 1 238 small239 atan239th completion239-agreement
