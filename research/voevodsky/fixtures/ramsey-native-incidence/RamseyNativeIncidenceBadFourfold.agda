{-# OPTIONS --safe --cubical --guardedness #-}
module RamseyNativeIncidenceBadFourfold where
open import Cubical.Foundations.Prelude
open import Cubical.Data.Unit.Base using (tt)
open import RamseySingleFrameFaces using (Vertex; c0; m0; c1; m1)
open import RamseyNativeIncidenceExamples
bad : S.Common Vertex (λ p → p)
bad = c0 , (λ { c0 → tt ; m0 → tt ; c1 → tt ; m1 → tt })
