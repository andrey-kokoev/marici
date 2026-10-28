{-# OPTIONS --safe --cubical --guardedness #-}
module OriginalBridgeBadExactPacket where
open import Cubical.Foundations.Prelude
import OriginalRuleGeometricCompiler as C
import SeedGeometricResponseState as G
import SeedSeamPathComparisonBoundary as W
bad : C.Running.packet (C.compile W.x0)
  ≡ G.FromA.Running.packet (G.FromA.RetainedRun.native (G.FromA.run W.x0))
bad = refl
