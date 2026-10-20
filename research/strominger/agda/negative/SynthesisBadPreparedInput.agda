{-# OPTIONS --safe --cubical --guardedness #-}
module SynthesisBadPreparedInput where
open import InternalSourceComparisons using (stay)
open import GeneratedReaderClassification using (hidden)
open import CanonicalComparisonSynthesis
module Bad = Compile stay hidden hidden
