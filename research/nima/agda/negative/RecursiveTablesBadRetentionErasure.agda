{-# OPTIONS --safe --cubical --guardedness #-}
module negative.RecursiveTablesBadRetentionErasure where
open import Cubical.Foundations.Prelude
open import RecursiveTableRegression using (module G; module Run; choice)
-- EXPECTED FAILURE: an output type graph alone is not the retained result.
bad : Run.old-code choice ≡ G.decode (Run.code choice)
bad = refl
