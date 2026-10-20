{-# OPTIONS --safe --cubical --guardedness #-}
module ModeBadTableAsOverlap where
open import InternalSourceComparisons using (exchange)
import ForwardSourceLiftComposition as F
import SourceModeCoherence as M
bad : F.TripleExchangeOverlap
bad c = M.product-assoc exchange exchange exchange
