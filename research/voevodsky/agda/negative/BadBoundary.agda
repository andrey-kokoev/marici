{-# OPTIONS --safe --cubical --no-import-sorts --guardedness #-}
module BadBoundary where

open import Cubical.Foundations.Prelude
open import Cubical.Data.Nat

-- Deliberate failure: the path body ends at zero while its declared
-- endpoint is suc zero. Cubical Agda must reject this boundary mismatch.
badEdge : zero ≡ suc zero
badEdge i = zero
