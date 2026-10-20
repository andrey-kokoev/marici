{-# OPTIONS --safe --cubical --guardedness #-}
module GraphBadEndpointRetraction where
open import Cubical.Foundations.Prelude
open import ActualSeedEndpointTable
open import SeedTetrahedronBridge using (Realization; node; edge)
open import SourceGraphFreeRealization
bad : Realization → Vertex
bad (node v) = v
bad (edge AB i) = A
bad (edge BC i) = B
bad (edge CA i) = C
bad (edge AD i) = A
bad (edge DB i) = D
bad (edge BA i) = B
