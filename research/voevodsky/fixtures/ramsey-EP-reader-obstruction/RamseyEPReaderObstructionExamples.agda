{-# OPTIONS --safe --cubical --guardedness #-}
module RamseyEPReaderObstructionExamples where
open import Cubical.Foundations.Prelude
open import Cubical.Data.Bool.Base using (Bool; false; true)
open import Cubical.Data.Bool.Properties using (false≢true)
open import Cubical.Data.Empty.Base using (⊥)
open import RamseyEPReaderObstruction
module O = Obstruction Bool false true false≢true
context : O.Context
context x = x s0 , x s1
actual-failure : O.readerP (O.adapter context O.unit1) ≡ O.adapter context (O.readerE O.unit1) → ⊥
actual-failure eq = false≢true (cong (λ x → x s0) eq)
actual-PN-failure : O.pn (O.readerP (O.adapter context O.unit1)) ≡ O.pn (O.adapter context (O.readerE O.unit1)) → ⊥
actual-PN-failure eq = false≢true (cong (λ x → x s3) eq)
