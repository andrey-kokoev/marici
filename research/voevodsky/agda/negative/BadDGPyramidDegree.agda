{-# OPTIONS --safe --cubical --guardedness #-}
module BadDGPyramidDegree where

open import Cubical.Foundations.Prelude
open import DGPyramidBoundary

-- EXPECTED FAILURE: hM has degree -1, while this result asks for degree 0.
-- Keeping JQminus1 and JQzero distinct makes the bad convention untypable.
badMorseDegree : {ℓ : Level} (P : DGPyramidBoundary {ℓ}) → JQzero P
badMorseDegree P = hM P
