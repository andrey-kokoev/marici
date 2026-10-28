{-# OPTIONS --safe --cubical --guardedness #-}
module PhysicalDomainNativeReadouts where

open import Cubical.Foundations.Prelude
open import Cubical.Data.Bool.Base using (Bool; false; true)
import NativeAmplitudeResolution as Amplitude
import NativeResolvedDomainRepresentation as Coverage

-- Only the finite algebraic readout layer is compiled here. Coefficients and
-- algebra operations are declared inputs, not inferred physical laws.
data Vertex : Type where
  i j k : Vertex

data Factor : Type where
  external-drive bath-drive return-coefficient : Factor
  anomaly-level boundary-normal flavor-sign minus-one : Factor
  projector-entry : Vertex → Bool → Bool → Factor

module Bindings (W : Type) (zero one : W)
  (add multiply : W → W → W) (weight : Factor → W) where
  module A = Amplitude.Algebra Factor W weight zero one add multiply
  module Source = Coverage.ForSource ℓ-zero A.Run.OldSeeds

  reflection : A.Expr
  reflection = A.binary A.sum-mode A.one-expr
    (A.binary A.product-mode (A.factor return-coefficient) (A.factor external-drive))
  noise : A.Expr
  noise = A.binary A.product-mode (A.factor return-coefficient) (A.factor bath-drive)
  inflow-current : A.Expr
  inflow-current = A.binary A.product-mode
    (A.binary A.product-mode (A.factor anomaly-level) (A.factor boundary-normal))
    (A.factor flavor-sign)
  inflow-energy : A.Expr
  inflow-energy = A.binary A.product-mode (A.factor minus-one) inflow-current

  sum2 : (Bool → A.Expr) → A.Expr
  sum2 f = A.binary A.sum-mode (f false) (f true)
  term : Bool → Bool → Bool → A.Expr
  term a b c = A.binary A.product-mode
    (A.binary A.product-mode (A.factor (projector-entry i a b))
      (A.factor (projector-entry j b c)))
    (A.factor (projector-entry k c a))
  bargmann : A.Expr
  bargmann = sum2 (λ a → sum2 (λ b → sum2 (λ c → term a b c)))

  reflection-history noise-history current-history energy-history bargmann-history : Source.Domain
  reflection-history = A.original reflection
  noise-history = A.original noise
  current-history = A.original inflow-current
  energy-history = A.original inflow-energy
  bargmann-history = A.original bargmann

  reflection-correct : A.readout reflection (snd (A.package reflection))
    ≡ add one (multiply (weight return-coefficient) (weight external-drive))
  reflection-correct = A.native-correct reflection

  noise-correct : A.readout noise (snd (A.package noise))
    ≡ multiply (weight return-coefficient) (weight bath-drive)
  noise-correct = A.native-correct noise

  current-correct : A.readout inflow-current (snd (A.package inflow-current))
    ≡ multiply (multiply (weight anomaly-level) (weight boundary-normal)) (weight flavor-sign)
  current-correct = A.native-correct inflow-current

  sumW : (Bool → W) → W
  sumW f = add (f false) (f true)
  contraction : W
  contraction = sumW (λ a → sumW (λ b → sumW (λ c →
    multiply (multiply (weight (projector-entry i a b)) (weight (projector-entry j b c)))
      (weight (projector-entry k c a)))))

  bargmann-correct : A.readout bargmann (snd (A.package bargmann)) ≡ contraction
  bargmann-correct = A.native-correct bargmann
