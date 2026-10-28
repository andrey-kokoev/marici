{-# OPTIONS --safe --cubical --guardedness #-}
module RamseyEPReaderObstructionBadSquare where
open import Cubical.Foundations.Prelude
open import RamseyEPReaderObstructionExamples
bad : O.readerP (O.adapter context O.unit1) ≡ O.adapter context (O.readerE O.unit1)
bad = refl
