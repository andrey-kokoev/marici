{-# OPTIONS --safe --cubical --guardedness #-}
module Su32PortEqualityIsNotValueEquality where
open import Cubical.Foundations.Prelude
open import Su32RecordReaderClassification
module P = PortOnlyCounterexample
bad : P.z0 ≡ P.z1
bad = refl
