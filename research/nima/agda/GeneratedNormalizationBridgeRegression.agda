{-# OPTIONS --safe --cubical --guardedness #-}
module GeneratedNormalizationBridgeRegression where

open import Cubical.Foundations.Prelude
open import Cubical.Foundations.Equiv
open import Cubical.Data.Bool.Base using (Bool; true; false)
open import Cubical.Data.Bool.Properties using (true≢false)
open import Cubical.Data.Empty.Base using (⊥)
import WholePackageSigmaPi as Whole
import WholePackageResolution as Resolution
import WholePackageUniversalProperty as Universal
import WholeHistoryComparisonInstance as Instance
import GeneratedNormalizationBridge as Bridge

module Check (ℓ : Level) (a : Whole.Universe.Complete ℓ) where
  open Whole.Universe ℓ
  module I = Instance.Concrete ℓ a
  module U = Universal.Universal ℓ I.D.Seed
  module R = Resolution.Generators ℓ
  module High = Whole.Universe (ℓ-suc ℓ)

  -- Concrete wiring regression for the existing endpoint observer. The
  -- generic bridge accepts structured carrier codes as well; this example
  -- is not a claim that endpoint observation is faithful to raw histories.
  carrier-code : Complete → High.Code
  carrier-code q = High.atom (U.Algebra.Carrier I.endpoint-algebra q)

  module B = Bridge.Bridge ℓ I.D.Seed I.endpoint-algebra carrier-code (λ _ → idEquiv _)
  module G = B.Structural I.Law I.interpret-law
  module Bare = B.Structural I.EmptyLaw I.interpret-empty

  checked-law : G.G.Generated I.D.by-identity I.D.by-general-comparison
  checked-law = I.generated-comparison

  normalized-law : B.NormalSemantic I.D.by-identity I.D.by-general-comparison
  normalized-law = G.normal-sound checked-law

  recovered-law : invEq (B.witness-equiv I.D.by-identity I.D.by-general-comparison)
    normalized-law ≡ I.Structural.sound checked-law
  recovered-law = retEq (B.witness-equiv I.D.by-identity I.D.by-general-comparison) _

  double-inversion : G.G.Generated I.D.by-identity I.D.by-general-comparison
  double-inversion = G.G.invert (G.G.invert checked-law)

  is-law : {q : Complete} {d e : R.Resolve I.D.Seed q} → G.G.Generated d e → Bool
  is-law (G.G.law _) = true
  is-law _ = false

  derivations-still-distinct : checked-law ≡ double-inversion → ⊥
  derivations-still-distinct p = true≢false (cong is-law p)

  record-package : High.Complete
  record-package = G.next-Q (G.retain-derivation checked-law)

  left-retained : G.Retained.left (High.value record-package) ≡ I.D.by-identity
  left-retained = refl

  right-retained : G.Retained.right (High.value record-package) ≡ I.D.by-general-comparison
  right-retained = refl

  derivation-retained : G.Retained.derivation (High.value record-package) ≡ checked-law
  derivation-retained = refl

  -- The available normalized endpoint witness cannot repair the absent law.
  available-without-law : B.NormalSemantic I.D.by-identity I.D.by-general-comparison
  available-without-law = refl

  normalization-does-not-repair-missing-law : Bare.NormalCompleteness → ⊥
  normalization-does-not-repair-missing-law complete =
    I.bare-incomplete (Bare.completeness-backward complete)

  no-generated-representative :
    (Σ[ c ∈ Bare.G.Generated I.D.by-identity I.D.by-general-comparison ]
       (Bare.normal-sound c ≡ available-without-law)) → ⊥
  no-generated-representative evidence = I.missing-equation (fst evidence)
