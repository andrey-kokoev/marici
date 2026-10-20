{-# OPTIONS --safe --cubical --guardedness #-}
module OverlapBadBaseCubeAsNative where
import ForwardSourceLiftComposition as F
open import SourceInverseSquareCoherence
bad : F.TripleExchangeOverlap
bad c = AB-square
