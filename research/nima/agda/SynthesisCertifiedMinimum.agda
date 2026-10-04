{-# OPTIONS --safe --cubical --guardedness #-}
module SynthesisCertifiedMinimum where
open import Cubical.Foundations.Prelude
open import AlgebraSynthesisSpecification
open import DiscoveredWolframFormula using (found-formula; adequate)
open import GeneratedMinimumCoverage

module Certified (ℓ : Level) where
  minimum : Goal.Minimal ℓ found-formula
  minimum f cheaper = Coverage.no-cheaper ℓ f cheaper

  certificate : Goal.Result ℓ
  certificate = Goal.certify ℓ found-formula adequate minimum

-- Adequacy above is still the explicitly reused proof. This module closes
-- the minimum/Sigma gate, not the independent fresh-proof-search gate.
