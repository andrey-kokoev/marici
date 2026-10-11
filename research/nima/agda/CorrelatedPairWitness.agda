{-# OPTIONS --safe --cubical --guardedness #-}
module CorrelatedPairWitness where

open import Cubical.Foundations.Prelude
open import Cubical.Data.Nat.Base using (zero; suc)
import TypedGeneratorLayers as Layers
import MetaWitnessNativeBridge as NativeBridge

-- Representation adapter: the orbitals, correlation factor and scalar
-- multiplication are supplied. Nothing here derives a Coulomb law.
module PairAdapter
  (ℓ : Level)
  (Parameters Configuration Scalar : Type ℓ)
  (orbital factor : Parameters → Configuration → Scalar)
  (multiply : Scalar → Scalar → Scalar)
  where

  data State : Type ℓ where
    independent : Parameters → State
    correlated : Parameters → State

  parameters : State → Parameters
  parameters (independent p) = p
  parameters (correlated p) = p

  data Witness : State → State → Type ℓ where
    attach-pair : (p : Parameters) → Witness (independent p) (correlated p)
    retain-pair : (p : Parameters) → Witness (correlated p) (correlated p)

  generate : (s : State) → Σ[ t ∈ State ] Witness s t
  generate (independent p) = correlated p , attach-pair p
  generate (correlated p) = correlated p , retain-pair p

  WG : Layers.Layer1 ℓ
  WG = record { State = State ; Witness = Witness ; generate = generate }

  evaluate : State → Configuration → Scalar
  evaluate (independent p) x = orbital p x
  evaluate (correlated p) x = multiply (orbital p x) (factor p x)

  generated-readout : (p : Parameters) (x : Configuration)
    → evaluate (fst (generate (independent p))) x
      ≡ multiply (orbital p x) (factor p x)
  generated-readout p x = refl

  parameter-recovery : (s : State)
    → parameters (fst (generate s)) ≡ parameters s
  parameter-recovery (independent p) = refl
  parameter-recovery (correlated p) = refl

  module History = Layers.Histories WG
  retained-step : (p : Parameters)
    → History.History (independent p) (correlated p)
  retained-step p = History.single (attach-pair p)

  retained-length : (p : Parameters)
    → History.length (retained-step p) ≡ suc zero
  retained-length p = refl

  -- Spatial exchange symmetry is inherited only from supplied certificates.
  -- The antisymmetric spin singlet is separate from this scalar adapter.
  module Exchange
    (swap : Configuration → Configuration)
    (orbital-symmetric : (p : Parameters) (x : Configuration)
      → orbital p (swap x) ≡ orbital p x)
    (factor-symmetric : (p : Parameters) (x : Configuration)
      → factor p (swap x) ≡ factor p x)
    where
    correlated-symmetric : (p : Parameters) (x : Configuration)
      → evaluate (correlated p) (swap x) ≡ evaluate (correlated p) x
    correlated-symmetric p x i =
      multiply (orbital-symmetric p x i) (factor-symmetric p x i)

  -- Conditional bridge into the separately application-extended runtime.
  -- Its Runtime requires derivations of both function and argument inputs.
  module Native = NativeBridge.Bridge ℓ WG
