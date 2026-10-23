{-# OPTIONS --safe --cubical --guardedness #-}
module RamseySingleFrameBadAllFaces where
open import Cubical.Foundations.Prelude
open import RamseySingleFrameFaces
bad : (v : Vertex) → Eligible v
bad c0 = refl
bad c1 = refl
bad m0 = refl
bad m1 = refl
