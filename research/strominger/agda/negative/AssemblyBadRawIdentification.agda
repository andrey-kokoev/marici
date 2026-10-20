{-# OPTIONS --safe --cubical --guardedness #-}
module AssemblyBadRawIdentification where
open import Cubical.Foundations.Prelude
import ContinuationPolicyFamily as Tags
import SourceCertifiedCoherentAssembly as Assembly
module X = Assembly.Regression.Bound
bad : (k : Tags.Presentation) → X.raw k ≡ X.targetClosure
bad k = refl
