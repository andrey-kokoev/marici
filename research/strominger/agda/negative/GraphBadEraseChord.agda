{-# OPTIONS --safe --cubical --guardedness #-}
module GraphBadEraseChord where
open import Cubical.Foundations.Prelude
open import ActualSeedEndpointTable
open import SeedTetrahedronBridge using (edge)
open import SourceGraphFreeRealization
bad : cong collapse (edge BC) ≡ refl
bad = refl
