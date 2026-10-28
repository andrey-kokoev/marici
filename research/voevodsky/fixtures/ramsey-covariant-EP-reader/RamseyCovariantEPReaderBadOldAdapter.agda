{-# OPTIONS --safe --cubical --guardedness #-}
module RamseyCovariantEPReaderBadOldAdapter where
open import Cubical.Foundations.Prelude
open import Cubical.Data.Bool.Base using (Bool; false; true)
open import Cubical.Data.Bool.Properties using (false≢true)
open import RamseyEPReaderObstruction
module O = Obstruction Bool false true false≢true
context : O.Context
context x = x s0 , x s1
bad : O.readerP (O.adapter context O.unit1) ≡ O.adapter context (O.readerE O.unit1)
bad = refl
