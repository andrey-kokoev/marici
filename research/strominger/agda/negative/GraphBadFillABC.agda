{-# OPTIONS --safe --cubical --guardedness #-}
module GraphBadFillABC where
open import Cubical.Foundations.Prelude
open import SeedTetrahedronBridge using (TriangleABC)
open import SourceGraphFreeRealization
bad : TriangleABC
bad = refl
