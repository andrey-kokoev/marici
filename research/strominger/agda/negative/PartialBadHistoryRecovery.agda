{-# OPTIONS --safe --cubical --guardedness #-}
module PartialBadHistoryRecovery where
open import Cubical.Foundations.Prelude
open import ActualSeedEndpointTable
import SeedSeamPathComparisonBoundary as W
import TransportObservationPartialCorrespondence as P
emptyWord triangle : P.Test.Word
emptyWord = W.stop
triangle = W.step AB (W.step BC (W.step CA W.stop))
same-parity : P.parity emptyWord ≡ P.parity triangle
same-parity = refl
bad : emptyWord ≡ triangle
bad = refl
