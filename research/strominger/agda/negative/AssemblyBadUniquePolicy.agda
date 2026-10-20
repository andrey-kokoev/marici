{-# OPTIONS --safe --cubical --guardedness #-}
module AssemblyBadUniquePolicy where
open import Cubical.Foundations.Prelude
open import Cubical.Data.Unit using (Unit)
import ContinuationPolicyFamily as Tags
import SourceCertifiedCoherentAssembly
bad : isProp (Σ[ k ∈ Tags.Presentation ] Unit)
bad x y = refl
