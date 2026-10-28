{-# OPTIONS --safe --cubical --guardedness #-}
module PromotedPhysicalReadoutComposition where

open import Cubical.Foundations.Prelude
import PhysicalDomainNativeReadouts as Readouts

-- Two DECLARED adapter stages, their actual recovery witnesses, and an analytic
-- preparation interface. No analytic law or adapter implementation is inferred
-- from these hypotheses. The native readout below consumes only recovered data.
module Composition {ℓ : Level} (Input D P Q : Type ℓ)
  (prepare : Input → D)
  (promote1 : D → P) (recover1 : P → D)
  (law1 : (d : D) → recover1 (promote1 d) ≡ d)
  (promote2 : P → Q) (recover2 : Q → P)
  (law2 : (p : P) → recover2 (promote2 p) ≡ p)
  (W : Type) (zero one : W) (add multiply : W → W → W)
  (weights : D → Readouts.Factor → W) where

  recover : Q → D
  recover q = recover1 (recover2 q)
  produce : Input → Q
  produce x = promote2 (promote1 (prepare x))
  recovered : (x : Input) → recover (produce x) ≡ prepare x
  recovered x = cong recover1 (law2 (promote1 (prepare x))) ∙ law1 (prepare x)

  module At (q : Q) where
    module Native = Readouts.Bindings W zero one add multiply (weights (recover q))
    reflection = Native.A.readout Native.reflection (snd (Native.A.package Native.reflection))
    noise = Native.A.readout Native.noise (snd (Native.A.package Native.noise))
    current = Native.A.readout Native.inflow-current (snd (Native.A.package Native.inflow-current))
    berry = Native.A.readout Native.bargmann (snd (Native.A.package Native.bargmann))
    -- These are actual original Resolve histories from the native compiler,
    -- not seeds containing the final computed answers.
    reflection-history = Native.reflection-history
    noise-history = Native.noise-history
    current-history = Native.current-history
    berry-history = Native.bargmann-history

  reflection-formula : D → W
  reflection-formula d = add one
    (multiply (weights d Readouts.return-coefficient) (weights d Readouts.external-drive))
  noise-formula : D → W
  noise-formula d = multiply (weights d Readouts.return-coefficient) (weights d Readouts.bath-drive)
  current-formula : D → W
  current-formula d = multiply
    (multiply (weights d Readouts.anomaly-level) (weights d Readouts.boundary-normal))
    (weights d Readouts.flavor-sign)

  reflection-preserved : (x : Input) → At.reflection (produce x) ≡ reflection-formula (prepare x)
  reflection-preserved x = At.Native.reflection-correct (produce x)
    ∙ cong reflection-formula (recovered x)
  noise-preserved : (x : Input) → At.noise (produce x) ≡ noise-formula (prepare x)
  noise-preserved x = At.Native.noise-correct (produce x)
    ∙ cong noise-formula (recovered x)
  current-preserved : (x : Input) → At.current (produce x) ≡ current-formula (prepare x)
  current-preserved x = At.Native.current-correct (produce x)
    ∙ cong current-formula (recovered x)

  berry-formula : D → W
  berry-formula d = B.contraction
    where module B = Readouts.Bindings W zero one add multiply (weights d)
  berry-preserved : (x : Input) → At.berry (produce x) ≡ berry-formula (prepare x)
  berry-preserved x = At.Native.bargmann-correct (produce x)
    ∙ cong berry-formula (recovered x)

  -- Analytic observables are preserved as supplied functions; this statement
  -- is not a native implementation of differentiation/integration/solving.
  analytic-readout-preserved : {κ : Level} {O : Type κ}
    (read : D → O) (x : Input) → read (recover (produce x)) ≡ read (prepare x)
  analytic-readout-preserved read x = cong read (recovered x)
