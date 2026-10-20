{-# OPTIONS --safe --cubical --guardedness #-}
module AdapterBadRawReturn where
open import Cubical.Foundations.Prelude
open import ContinuationSidePolicies using (ab)
open import SourceIndexedContinuationAdapter
-- The derived return is mode-adjusted, not the raw source edge endpoint.
bad : fst (Example.route ab) ≡ fst ab
bad = sym (Example.return-port ab)
