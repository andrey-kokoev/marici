{-# OPTIONS --safe --cubical --no-import-sorts --guardedness #-}
module MissingNaturality where

open import Cubical.Foundations.Prelude
open import Cubical.Data.Int
open import SourceInterpretation

identitySource : SourceVertex
Parameter identitySource = ℤ
Object identitySource = ℤ
Residue identitySource = ℤ
generator identitySource x = x
coherencer identitySource x = x

-- Deliberate failure: coordinate functions alone do not constitute an
-- interpretation; generator and coherencer naturality paths are omitted.
badInterpretation : VertexInterpretation identitySource
parameter-coordinate badInterpretation x = x
object-coordinate badInterpretation x = x
residue-coordinate badInterpretation x = x
