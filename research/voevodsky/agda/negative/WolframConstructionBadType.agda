{-# OPTIONS --safe --cubical --guardedness #-}
module WolframConstructionBadType where
open import Cubical.Data.List.Base using ([])
open import RefutationConstructionWG
import GeneratedWolframConstruction as G

-- Mutate the goal: a NAND swap cannot serve as the Wolfram forward map.
broken : Proof [] (arrow G.W G.D)
broken = G.swap
